#!/usr/bin/env python3
"""
benchmark_channels.py

Measures the performance impact of the multi-channel communication protocol.

Two dimensions:
  1. Mission blocking time — how long picard's orchestration loop waits for
     webhook notifications before it can continue.

     BEFORE: synchronous curl (one blocking call per signal, single channel)
     AFTER:  fire-and-forget background threads (zero blocking; fan-out to N channels)

  2. Signal-to-noise ratio — what fraction of signals reaching a channel
     are actually relevant to that channel's subscribers.

     BEFORE: one channel receives 100% of signals; every subscriber sees everything
     AFTER:  each channel receives only routed signals (typically 20–50%)

Usage:
  python3 scripts/benchmark_channels.py
  python3 scripts/benchmark_channels.py --latency 200 --runs 10
"""

import argparse
import statistics
import threading
import time
from typing import List, Tuple

# ── Defaults ──────────────────────────────────────────────────────────────────
DEFAULT_LATENCY_MS = 150   # realistic Teams/Slack webhook round-trip
DEFAULT_RUNS       = 5     # repetitions for stable statistics

# ── Channel registry ──────────────────────────────────────────────────────────
ALL_CHANNELS = [
    "tng-bridge",
    "tng-ready-room",
    "tng-execution",
    "tng-review",
    "tng-oncall",
    "tng-stakeholders",
]

# ── Mission signal routing table ──────────────────────────────────────────────
# Represents one full Ready Room → Bridge → Track C cycle.
# Mirrors the fan-out rules in PLAYBOOK.md Multi-Channel Communication Protocol.
# Each entry: (signal_name, sender, target_channels)
# tng-bridge always included — it is the superset/audit channel.

MISSION_SIGNALS: List[Tuple[str, str, List[str]]] = [
    # Phase 1: Ready Room
    ("READY-ROOM-OPEN",       "picard",  ["tng-bridge", "tng-ready-room", "tng-stakeholders"]),
    ("MDR-ISSUED",             "picard",  ["tng-bridge", "tng-ready-room"]),
    ("PRIORITY:P1",            "worf",    ["tng-bridge", "tng-oncall", "tng-ready-room"]),
    ("AC-APPROVED",            "picard",  ["tng-bridge", "tng-ready-room"]),
    ("READY-ROOM-CLOSED",      "picard",  ["tng-bridge", "tng-ready-room"]),
    # Phase 2: Bridge execution
    ("execution-wave-1",       "riker",   ["tng-bridge", "tng-execution"]),
    ("BLOCKER",                "geordi",  ["tng-bridge", "tng-oncall", "tng-execution"]),
    ("execution-wave-2",       "riker",   ["tng-bridge", "tng-execution"]),
    # Phase 3: Track C review
    ("Track-C:CONDITIONAL",    "troi",    ["tng-bridge", "tng-review"]),
    ("FIX-IN-PLACE",           "picard",  ["tng-bridge", "tng-review"]),
    ("Track-C:PASS",           "worf",    ["tng-bridge", "tng-review"]),
    # Phase 4: Mission close
    ("MISSION-CLOSED",         "picard",  ["tng-bridge", "tng-stakeholders"]),
]

# ── Mock webhook ──────────────────────────────────────────────────────────────

def _mock_webhook(channel: str, signal: str, latency_ms: float) -> None:
    """Simulates an HTTP POST to a webhook endpoint with realistic round-trip latency."""
    time.sleep(latency_ms / 1000)


# ── Scenario: BEFORE (single channel, synchronous) ───────────────────────────

def scenario_before(latency_ms: float) -> float:
    """
    Single channel (tng-bridge only), synchronous blocking call.

    Mirrors the original PLAYBOOK.md curl pattern:
      curl -s -X POST -H 'Content-Type: application/json' -d '...' "<webhook-url>"

    picard cannot continue until curl returns. One call per signal.
    Returns total milliseconds the orchestration loop was blocked.
    """
    blocked_ms = 0.0
    for signal, _agent, _channels in MISSION_SIGNALS:
        t0 = time.perf_counter()
        _mock_webhook("tng-bridge", signal, latency_ms)   # synchronous, blocks
        blocked_ms += (time.perf_counter() - t0) * 1000
    return blocked_ms


# ── Scenario: AFTER (multi-channel, fire-and-forget) ─────────────────────────

def scenario_after(latency_ms: float) -> float:
    """
    Multi-channel fan-out, fire-and-forget background threads.

    Mirrors the _tng_notify helper in PLAYBOOK.md:
      _tng_notify "$TEAMS_WEBHOOK_READY_ROOM" "..." &
      _tng_notify "$TEAMS_WEBHOOK_BRIDGE"     "..." &
      # No wait — fire-and-forget

    picard fires all channel webhooks as background threads and moves on
    immediately. Blocked time is only the thread-start overhead (~microseconds).
    Returns total milliseconds the orchestration loop was blocked.
    """
    blocked_ms = 0.0
    background_threads: List[threading.Thread] = []

    for signal, _agent, channels in MISSION_SIGNALS:
        t0 = time.perf_counter()
        for ch in channels:
            t = threading.Thread(
                target=_mock_webhook,
                args=(ch, signal, latency_ms),
                daemon=True,
            )
            t.start()
            background_threads.append(t)
        # Mission continues — does NOT join. This is the fire-and-forget boundary.
        blocked_ms += (time.perf_counter() - t0) * 1000

    # Let background threads finish (they run while the mission continues onward;
    # their completion time is NOT added to blocked_ms).
    for t in background_threads:
        t.join()

    return blocked_ms


# ── Noise analysis ────────────────────────────────────────────────────────────

def signal_noise_analysis() -> dict:
    """
    Computes per-channel signal relevance statistics.

    BEFORE baseline: all subscribers watch tng-bridge → receive 100% of signals.
    AFTER:           each channel receives only the signals routed to it.
    """
    total = len(MISSION_SIGNALS)
    hits = {ch: 0 for ch in ALL_CHANNELS}

    for _signal, _agent, channels in MISSION_SIGNALS:
        for ch in channels:
            if ch in hits:
                hits[ch] += 1

    result = {}
    for ch in ALL_CHANNELS:
        rcvd = hits[ch]
        relevance = round(rcvd / total * 100, 1)
        noise_cut = round((1 - rcvd / total) * 100, 1) if ch != "tng-bridge" else 0.0
        result[ch] = {
            "received": rcvd,
            "total": total,
            "relevance_pct": relevance,
            "noise_reduction_pct": noise_cut,
        }
    return result


# ── Formatting helpers ────────────────────────────────────────────────────────

def _ms(val: float) -> str:
    return f"{val:8.2f} ms"

def _divider(width: int = 64) -> str:
    return "  " + "─" * width


# ── Main ──────────────────────────────────────────────────────────────────────

def main(latency_ms: float, runs: int) -> None:
    total_webhooks_before = len(MISSION_SIGNALS)
    total_webhooks_after  = sum(len(ch) for _s, _a, ch in MISSION_SIGNALS)

    print()
    print("=" * 66)
    print("  TNG Agent — Multi-Channel Communication Benchmark")
    print("=" * 66)
    print(f"  Simulated webhook latency : {latency_ms:.0f} ms per call")
    print(f"  Mission signals per cycle : {len(MISSION_SIGNALS)}")
    print(f"  Benchmark runs            : {runs}")
    print(f"  Webhooks fired — BEFORE   : {total_webhooks_before} "
          f"(1 per signal, sequential, blocking)")
    print(f"  Webhooks fired — AFTER    : {total_webhooks_after} "
          f"(fan-out, parallel, non-blocking)")
    print("=" * 66)
    print()

    before_samples: List[float] = []
    after_samples:  List[float] = []

    print("  Running scenarios", end="", flush=True)
    for _ in range(runs):
        before_samples.append(scenario_before(latency_ms))
        after_samples.append(scenario_after(latency_ms))
        print(".", end="", flush=True)
    print(" done.")
    print()

    before_mean   = statistics.mean(before_samples)
    after_mean    = statistics.mean(after_samples)
    time_saved_ms = before_mean - after_mean
    pct_saved     = time_saved_ms / before_mean * 100
    speedup       = before_mean / after_mean if after_mean > 0 else float("inf")

    # ── Section 1: Mission blocking time ─────────────────────────────────────
    print(_divider())
    print("  1. Mission Blocking Time  (time orchestration loop is stalled)")
    print(_divider())
    print()
    print(f"  {'Metric':<32}  {'BEFORE':>12}  {'AFTER':>12}")
    print(f"  {'':32}  {'(sync, 1 ch)':>12}  {'(async, N ch)':>13}")
    print(f"  {'─'*62}")
    print(f"  {'Mean block per mission':32}  {_ms(before_mean):>12}  {_ms(after_mean):>12}")
    print(f"  {'Median block per mission':32}  "
          f"{_ms(statistics.median(before_samples)):>12}  "
          f"{_ms(statistics.median(after_samples)):>12}")
    print(f"  {'Min block per mission':32}  "
          f"{_ms(min(before_samples)):>12}  "
          f"{_ms(min(after_samples)):>12}")
    print(f"  {'Max block per mission':32}  "
          f"{_ms(max(before_samples)):>12}  "
          f"{_ms(max(after_samples)):>12}")
    print()
    print(f"  Orchestration speedup    : {speedup:>10,.0f}x")
    print(f"  Time returned per mission: {time_saved_ms:>10.1f} ms  "
          f"({pct_saved:.1f}% of blocking eliminated)")
    print()

    # ── Section 2: Signal noise per subscriber ────────────────────────────────
    print(_divider())
    print("  2. Signal Relevance Per Channel Subscriber")
    print(_divider())
    print()
    print(f"  {'Channel':<22}  {'Rcvd / Total':>13}  {'Relevant':>9}  {'Noise cut':>10}")
    print(f"  {'─'*60}")
    noise = signal_noise_analysis()
    for ch in ALL_CHANNELS:
        s = noise[ch]
        nr = f"{s['noise_reduction_pct']:>8.1f}%" if ch != "tng-bridge" else "     N/A"
        print(
            f"  {ch:<22}  "
            f"{s['received']:>3} / {s['total']:<8}  "
            f"{s['relevance_pct']:>8.1f}%  "
            f"{nr}"
        )
    print()
    print("  BEFORE baseline: all subscribers watch tng-bridge → 100% of signals.")
    print("  AFTER:  each channel receives only its routed signals.")
    print("  Noise cut = fraction of irrelevant signals eliminated per subscriber.")
    print()

    # ── Section 3: P0/P1 time-to-alert ───────────────────────────────────────
    p1 = next(s for s in MISSION_SIGNALS if "P1" in s[0])
    print(_divider())
    print("  3. P0/P1 Time-to-Alert")
    print(_divider())
    print()
    print(f"  Signal : [{p1[0]}]  sender: {p1[1]}")
    print(f"  Fan-out: {', '.join(p1[2])}")
    print()
    print(f"  BEFORE  On-call engineer watches tng-bridge (all {total_webhooks_before} signals).")
    print(f"          P1 arrives synchronously, buried among unrelated notifications.")
    print(f"          Time from signal emission to delivery: ~{latency_ms:.0f} ms (blocking).")
    print()
    print(f"  AFTER   tng-oncall fires in parallel with tng-bridge and tng-ready-room.")
    print(f"          On-call receives a dedicated feed: "
          f"{noise['tng-oncall']['received']} of {len(MISSION_SIGNALS)} signals "
          f"({noise['tng-oncall']['relevance_pct']}% relevance).")
    print(f"          Time from signal emission to delivery: ~{latency_ms:.0f} ms (non-blocking).")
    print(f"          Mission orchestration continues in <1 ms.")
    print()

    # ── Summary ───────────────────────────────────────────────────────────────
    print("=" * 66)
    print("  Summary")
    print("=" * 66)
    print(f"  Blocking eliminated    : {time_saved_ms:.1f} ms / mission  ({pct_saved:.1f}%)")
    print(f"  tng-oncall noise cut   : {noise['tng-oncall']['noise_reduction_pct']:.1f}%"
          f"  (from 100% to {noise['tng-oncall']['relevance_pct']}% of signals)")
    print(f"  tng-review noise cut   : {noise['tng-review']['noise_reduction_pct']:.1f}%")
    print(f"  tng-execution noise cut: {noise['tng-execution']['noise_reduction_pct']:.1f}%")
    print()
    print("  The multi-channel protocol eliminates nearly all orchestration blocking")
    print("  from webhook delivery and reduces subscriber noise by 50–75%,")
    print("  meaning fewer missed P0/P1 alerts and faster human response times.")
    print("=" * 66)
    print()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="TNG multi-channel communication benchmark")
    parser.add_argument(
        "--latency", type=float, default=DEFAULT_LATENCY_MS,
        help=f"Simulated webhook latency in ms (default: {DEFAULT_LATENCY_MS})"
    )
    parser.add_argument(
        "--runs", type=int, default=DEFAULT_RUNS,
        help=f"Number of benchmark repetitions (default: {DEFAULT_RUNS})"
    )
    args = parser.parse_args()
    main(latency_ms=args.latency, runs=args.runs)
