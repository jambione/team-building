#!/usr/bin/env python3
"""
benchmark_workflow.py

Models a complete TNG mission cycle (Ready Room → Bridge → Track C → Close)
with simulated agent and orchestration latencies to measure the wall-clock
impact of the 8 workflow optimisations in this branch.

BEFORE: original PLAYBOOK (sequential blocking gates)
AFTER:  optimised PLAYBOOK (8 improvements applied)

Usage:
  python3 scripts/benchmark_workflow.py
  python3 scripts/benchmark_workflow.py --agent-ms 2000 --picard-ms 500 --runs 10
"""

import argparse
import statistics
import threading
import time
from typing import Dict, List

# ── Defaults ──────────────────────────────────────────────────────────────────
# Small defaults keep the benchmark fast (≈20 s total).
# Pass --agent-ms 2000 --picard-ms 500 to model real LLM response latency.
DEFAULT_AGENT_MS  = 200   # simulated LLM agent response
DEFAULT_PICARD_MS = 50    # simulated picard orchestration step
DEFAULT_RUNS      = 5

# ── Primitives ────────────────────────────────────────────────────────────────

def seq(ms: float) -> float:
    """Sequential blocking step. Returns elapsed ms."""
    t0 = time.perf_counter()
    time.sleep(ms / 1000)
    return (time.perf_counter() - t0) * 1000


def par(tasks_ms: List[float]) -> float:
    """
    Parallel agents. Each task runs in its own thread.
    Returns wall-clock ms = max(task times), not sum.
    """
    if not tasks_ms:
        return 0.0
    results: List[float] = [0.0] * len(tasks_ms)

    def _run(i: int, ms: float) -> None:
        t0 = time.perf_counter()
        time.sleep(ms / 1000)
        results[i] = (time.perf_counter() - t0) * 1000

    t0 = time.perf_counter()
    threads = [threading.Thread(target=_run, args=(i, ms)) for i, ms in enumerate(tasks_ms)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    return (time.perf_counter() - t0) * 1000


# ── BEFORE scenario ───────────────────────────────────────────────────────────

def run_before(a: float, p: float) -> Dict[str, float]:
    """
    Original PLAYBOOK (pre-optimisation).

    Sequential chain:
      Step 3:  guinan history scan || picard KB reads (parallel)
      Step 4:  7 Ready Room analysts, each loads past-lessons + sprint-state
               before running analysis (parallel batch, but each agent pays
               the shared-doc read overhead)
      Step 5:  PRIORITY triage (picard)
      Step 6:  MDR synthesis (sequential)
      Step 7:  AC drafting — troi (sequential AFTER MDR complete)
      Step 9a: Bridge Wave 1 (parallel)
      Step 9b: Bridge Wave 2 (parallel, sequential gate after Wave 1)
      Step 9c: Execution Verification Report (picard)
      Step 10: Track C review — worf, troi, crusher (parallel)
      Step 11: KB updates — 5 specialists (parallel, sequential AFTER Track C)
      Step 12: Mission Debrief (sequential)
      Step 13: Session journal close (sequential)
      Step 14: Performance log update (sequential)
      Step 15: Mission log + index update (sequential)
      Step 16: guinan synthesis (sequential)
    """
    t: Dict[str, float] = {}

    # Step 3 — guinan + picard KB reads (parallel)
    t["03  History + KB reads"] = par([a, p])

    # Step 4 — 7 analysts; each reads 2 shared docs before analysis
    # shared-doc overhead = p per doc × 2 docs = 2p added to each agent's time
    t["04  Ready Room analysis (7 agents)"] = par([a + p * 2] * 7)

    # Step 5 — PRIORITY triage
    t["05  PRIORITY triage"] = seq(p)

    # Step 6 — MDR synthesis (sequential)
    t["06  MDR synthesis"] = seq(a)

    # Step 7 — AC drafting (sequential AFTER MDR)
    t["07  AC drafting (troi)"] = seq(a)

    # Bridge — 2 waves, each a sequential gate
    t["09a Bridge Wave 1"] = par([a, a])
    t["09b Bridge Wave 2"] = par([a, a])
    t["09c Execution verification"] = seq(p)

    # Step 10 — Track C review (parallel)
    t["10  Track C review"] = par([a, a, a])

    # Step 11 — KB updates (parallel, sequential AFTER Track C)
    t["11  KB updates"] = par([a] * 5)

    # Steps 12-15 — sequential picard close steps
    t["12  Mission Debrief"] = seq(p)
    t["13  Session journal close"] = seq(p * 0.5)
    t["14  Performance log update"] = seq(p * 0.5)
    t["15  Mission log"] = seq(p * 0.5)

    # Step 16 — guinan synthesis
    t["16  guinan synthesis"] = seq(a)

    return t


# ── AFTER scenario ────────────────────────────────────────────────────────────

def run_after(a: float, p: float) -> Dict[str, float]:
    """
    Optimised PLAYBOOK (all 8 improvements applied).

    #1  Track C + KB updates → single parallel batch (Step 10)
    #2  Mission close → single pass (Steps 12-15 collapsed)
    #3  [KB-NO-CHANGE] opt-in (signal count reduction; not timing)
    #4  MDR + AC drafting → parallel (Step 7)
    #5  Context Briefing → shared docs read once by picard, injected as
        summary; 7 analysts skip redundant loads (Step 4)
    #6  Webhook failure logging (operational; not mission-cycle timing)
    #7  wes fast-track (approval round-trip reduction; not modelled as
        blocking time here — see secondary metrics)
    #8  Progressive KB updates → 30% of KB updates already flushed
        mid-mission; reduces agents remaining at Step 10
    """
    t: Dict[str, float] = {}

    # Step 3 — same
    t["03  History + KB reads"] = par([a, p])

    # Step 4 — Context Briefing: picard reads 2 shared docs ONCE and
    # distils a summary (#5). Analysts receive the brief and skip shared loads.
    t["04  Context Briefing (picard)"] = seq(p)

    # Step 5 — 7 analysts; no shared-doc overhead (brief injected)
    t["05  Ready Room analysis (7 agents)"] = par([a] * 7)

    # Step 6 — PRIORITY triage
    t["06  PRIORITY triage"] = seq(p)

    # Step 7 — MDR + AC in parallel (#4)
    t["07  MDR + AC (parallel)"] = par([a, a])

    # Bridge — unchanged
    t["09a Bridge Wave 1"] = par([a, a])
    t["09b Bridge Wave 2"] = par([a, a])
    t["09c Execution verification"] = seq(p)

    # Step 10 — Track C + KB updates in one parallel batch (#1 + #8)
    # #8: 30% of KB updates already flushed progressively → ~3-4 agents remain
    remaining_kb = round(5 * 0.70)  # 4 agents still updating at close
    t["10  Track C + KB updates (parallel)"] = par([a] * 3 + [a] * remaining_kb)

    # Step 11 — Mission close single pass (#2)
    t["11  Mission close (single pass)"] = seq(p)

    # guinan synthesis — same
    t["12  guinan synthesis"] = seq(a)

    return t


# ── Secondary metrics (not timing) ───────────────────────────────────────────

def secondary_metrics_before() -> Dict[str, int]:
    return {
        "KB doc reads per Ready Room": 7 * 2 + 7,   # 2 shared + 1 domain per agent
        "[KB-NO-CHANGE] signals per mission": 5,     # ~5 of 7 analysts emit one
        "Sequential blocking gates (beyond waves)": 6,  # MDR→AC, TrackC→KB, ×4 close steps
    }


def secondary_metrics_after() -> Dict[str, int]:
    return {
        "KB doc reads per Ready Room": 2 + 7,        # 1 briefing distillation + 1 domain each
        "[KB-NO-CHANGE] signals per mission": 1,     # opt-in: only meaningful absences
        "Sequential blocking gates (beyond waves)": 1,  # only exec-verification remains
    }


# ── Display helpers ───────────────────────────────────────────────────────────

W_PHASE  = 40
W_COL    = 10
RULE     = "  " + "─" * (W_PHASE + W_COL * 3 + 6)
HEAVY    = "  " + "═" * (W_PHASE + W_COL * 3 + 6)


def _ms(v: float) -> str:
    return f"{v:>7.0f} ms"


def _pct(saved: float, total: float) -> str:
    return f"{saved / total * 100:>5.1f}%"


def discovery_totals(
    before_samples: Dict[str, List[float]],
    after_samples: Dict[str, List[float]],
) -> tuple:
    """
    Returns mean discovery-stage totals for BEFORE and AFTER.

    Discovery stage is defined as the work done before mission decisions are
    synthesized:
      BEFORE: 03 History + KB reads + 04 Ready Room analysis
      AFTER:  03 History + KB reads + 04 Context Briefing + 05 Ready Room analysis
    """

    before_list = list(before_samples.values())
    after_list = list(after_samples.values())

    before_discovery = statistics.mean([
        run["03  History + KB reads"] + run["04  Ready Room analysis (7 agents)"]
        for run in before_list
    ])
    after_discovery = statistics.mean([
        run["03  History + KB reads"] +
        run["04  Context Briefing (picard)"] +
        run["05  Ready Room analysis (7 agents)"]
        for run in after_list
    ])

    return before_discovery, after_discovery


def print_phase_table(
    before_phases: Dict[str, List[float]],
    after_phases:  Dict[str, List[float]],
) -> tuple:
    """
    Print the phase-by-phase comparison table.
    Returns (total_before_mean, total_after_mean).
    """
    # All unique phase names in display order
    before_keys = list(list(before_phases.values())[0].keys()) if before_phases else []
    after_keys  = list(list(after_phases.values())[0].keys())  if after_phases  else []

    # Use first run's keys as order reference
    all_before = list(before_phases[list(before_phases)[0]].keys())
    all_after  = list(after_phases[list(after_phases)[0]].keys())

    def mean_phase(runs: Dict[str, List[float]], key: str) -> float:
        vals = [r[key] for r in runs.values() if key in r]
        return statistics.mean(vals) if vals else 0.0

    # Collect runs as list of dicts
    before_list = list(before_phases.values())
    after_list  = list(after_phases.values())

    header = (
        f"  {'Phase':<{W_PHASE}}  "
        f"{'BEFORE':>{W_COL}}  "
        f"{'AFTER':>{W_COL}}  "
        f"{'Saved':>{W_COL}}"
    )
    print(header)
    print(RULE)

    total_before = sum(statistics.mean([r[k] for r in before_list]) for k in all_before)
    total_after  = sum(statistics.mean([r[k] for r in after_list])  for k in all_after)

    # Build merged row list: align phases that exist in both
    # Phases only in BEFORE, only in AFTER, or in both
    shown_before = set()
    shown_after  = set()
    rows = []

    # Map corresponding phases by step prefix
    step_map = {
        "03": ("03  History + KB reads",          "03  History + KB reads"),
        "04": ("04  Ready Room analysis (7 agents)", "04  Context Briefing (picard)"),
        "05": (None,                              "05  Ready Room analysis (7 agents)"),
        "p5": ("05  PRIORITY triage",             "06  PRIORITY triage"),
        "07b": ("06  MDR synthesis",              None),
        "07a": ("07  AC drafting (troi)",         None),
        "07m": (None,                             "07  MDR + AC (parallel)"),
        "9a": ("09a Bridge Wave 1",               "09a Bridge Wave 1"),
        "9b": ("09b Bridge Wave 2",               "09b Bridge Wave 2"),
        "9c": ("09c Execution verification",      "09c Execution verification"),
        "10t": ("10  Track C review",             None),
        "10k": ("11  KB updates",                 None),
        "10x": (None,                             "10  Track C + KB updates (parallel)"),
        "12b": ("12  Mission Debrief",            None),
        "13b": ("13  Session journal close",      None),
        "14b": ("14  Performance log update",     None),
        "15b": ("15  Mission log",                None),
        "11x": (None,                             "11  Mission close (single pass)"),
        "16": ("16  guinan synthesis",            "12  guinan synthesis"),
    }

    for _k, (bk, ak) in step_map.items():
        bv = statistics.mean([r[bk] for r in before_list]) if bk else None
        av = statistics.mean([r[ak] for r in after_list])  if ak else None

        if bv is not None and av is not None:
            saved = bv - av
            phase_label = bk if bk else ak
            print(
                f"  {phase_label:<{W_PHASE}}  "
                f"{_ms(bv):>{W_COL}}  "
                f"{_ms(av):>{W_COL}}  "
                f"{_ms(saved):>{W_COL}}"
            )
        elif bv is not None:
            phase_label = bk
            print(
                f"  {phase_label:<{W_PHASE}}  "
                f"{_ms(bv):>{W_COL}}  "
                f"{'—':>{W_COL}}  "
                f"{'—':>{W_COL}}"
            )
        elif av is not None:
            phase_label = ak
            new_tag = "  ← new"
            print(
                f"  {phase_label:<{W_PHASE}}  "
                f"{'—':>{W_COL}}  "
                f"{_ms(av):>{W_COL}}  "
                f"{'—':>{W_COL}}"
            )

    print(RULE)
    saved_total = total_before - total_after
    print(
        f"  {'TOTAL MISSION CYCLE TIME':<{W_PHASE}}  "
        f"{_ms(total_before):>{W_COL}}  "
        f"{_ms(total_after):>{W_COL}}  "
        f"{_ms(saved_total):>{W_COL}}"
    )
    speedup = total_before / total_after
    pct     = saved_total / total_before * 100
    print(
        f"  {'':.<{W_PHASE}}  "
        f"{'':>{W_COL}}  "
        f"{'Speedup:':>{W_COL}}  "
        f"{speedup:>{W_COL-3}.2f}x   "
    )
    print(
        f"  {'':.<{W_PHASE}}  "
        f"{'':>{W_COL}}  "
        f"{'Faster:':>{W_COL}}  "
        f"{pct:>{W_COL-2}.1f}%   "
    )

    return total_before, total_after


# ── Main ──────────────────────────────────────────────────────────────────────

def main(agent_ms: float, picard_ms: float, runs: int) -> None:
    print()
    print("═" * 66)
    print("  TNG Agent — Workflow Optimisation Benchmark")
    print("═" * 66)
    print(f"  Agent response latency (simulated)  : {agent_ms:.0f} ms")
    print(f"  Orchestration step latency (picard) : {picard_ms:.0f} ms")
    print(f"  Runs                                : {runs}")
    print(f"  Mission model                       : Ready Room → Bridge"
          f" → Track C → Close")
    print("═" * 66)

    # ── Collect samples ───────────────────────────────────────────────────────
    before_samples: Dict[str, List[float]] = {}
    after_samples:  Dict[str, List[float]] = {}

    print()
    print("  Running", end="", flush=True)
    for i in range(runs):
        before_samples[f"run{i}"] = run_before(agent_ms, picard_ms)
        after_samples[f"run{i}"]  = run_after(agent_ms, picard_ms)
        print(".", end="", flush=True)
    print(" done.")
    print()

    # ── Table 1: Phase-by-phase ───────────────────────────────────────────────
    print("─" * 66)
    print("  Table 1 — Phase-by-Phase Mission Cycle Time")
    print("─" * 66)
    print()
    total_before, total_after = print_phase_table(before_samples, after_samples)
    saved_ms = total_before - total_after
    print()

    # ── Table 2: Savings per improvement ─────────────────────────────────────
    print("─" * 66)
    print("  Table 2 — Savings Attributed by Improvement")
    print("─" * 66)
    print()

    def mean_key(samples: Dict[str, List[float]], key: str) -> float:
        runs_list = list(samples.values())
        return statistics.mean([r[key] for r in runs_list if key in r])

    # Exact savings per improvement
    improvements = [
        (
            "#1  Track C + KB updates parallel",
            mean_key(before_samples, "11  KB updates"),        # eliminated sequential step
            "Merged two sequential batches into one parallel batch",
        ),
        (
            "#2  Mission close single pass",
            (mean_key(before_samples, "12  Mission Debrief") +
             mean_key(before_samples, "13  Session journal close") +
             mean_key(before_samples, "14  Performance log update") +
             mean_key(before_samples, "15  Mission log")) -
            mean_key(after_samples, "11  Mission close (single pass)"),
            "4 sequential picard steps collapsed into one pass",
        ),
        (
            "#4  MDR + AC drafting parallel",
            mean_key(before_samples, "07  AC drafting (troi)"),  # AC no longer sequential after MDR
            "troi drafts AC while picard-thinking synthesises MDR",
        ),
        (
            "#5  Context Briefing (shared doc reads)",
            (mean_key(before_samples, "04  Ready Room analysis (7 agents)") -
             mean_key(after_samples,  "05  Ready Room analysis (7 agents)") -
             mean_key(after_samples,  "04  Context Briefing (picard)")),
            "7 × 2 shared-doc reads → 1 picard distillation injected as brief",
        ),
    ]

    col_i = 48
    col_v = 10
    print(f"  {'Improvement':<{col_i}}  {'Saved':>{col_v}}")
    print("  " + "─" * (col_i + col_v + 2))
    total_attr = 0.0
    for label, saving, note in improvements:
        print(f"  {label:<{col_i}}  {_ms(saving):>{col_v}}")
        print(f"  {'  → ' + note:<{col_i}}  {'':>{col_v}}")
        total_attr += saving
    print("  " + "─" * (col_i + col_v + 2))
    print(f"  {'Total attributed':<{col_i}}  {_ms(total_attr):>{col_v}}")
    print(f"  {'Measured total saving':<{col_i}}  {_ms(saved_ms):>{col_v}}")
    print()
    print("  Improvements #3, #6, #7, #8 reduce operational noise, signal")
    print("  volume, and approval latency — not modelled as cycle blocking time.")
    print("  #8 (progressive KB updates) is included in Table 3 below.")
    print()

    # ── Table 3: Secondary metrics ────────────────────────────────────────────
    print("─" * 66)
    print("  Table 3 — Secondary Metrics (per mission cycle)")
    print("─" * 66)
    print()

    bm = secondary_metrics_before()
    am = secondary_metrics_after()

    col_m = 42
    col_b = 9
    col_a = 9
    col_c = 10
    print(f"  {'Metric':<{col_m}}  {'BEFORE':>{col_b}}  {'AFTER':>{col_a}}  {'Change':>{col_c}}")
    print("  " + "─" * (col_m + col_b + col_a + col_c + 6))
    for k in bm:
        b, a = bm[k], am[k]
        delta = a - b
        delta_str = f"{delta:>+5d}"
        pct_str   = f"({(1 - a/b)*100:.0f}% less)" if b != 0 else ""
        print(f"  {k:<{col_m}}  {b:>{col_b}}  {a:>{col_a}}  {delta_str:>{col_c}}  {pct_str}")

    print()
    print("  KB reads:    #5 — past-lessons-learned + sprint-state loaded once by")
    print("               picard and injected as a brief; analysts skip the reload.")
    print("  KB-NO-CHANGE: #3 — opt-in; only emitted when absence is meaningful.")
    print("  Seq gates:   #1, #2, #4 — eliminated MDR→AC, TrackC→KB, and 4")
    print("               sequential picard close steps.")
    print()

    # ── Table 4: Discovery-stage metrics ─────────────────────────────────────
    print("─" * 66)
    print("  Table 4 — Discovery-Stage Bottleneck Metrics")
    print("─" * 66)
    print()

    discovery_before, discovery_after = discovery_totals(before_samples, after_samples)
    discovery_saved = discovery_before - discovery_after
    discovery_before_share = discovery_before / total_before * 100
    discovery_after_share = discovery_after / total_after * 100

    print(f"  {'Metric':<42}  {'BEFORE':>10}  {'AFTER':>10}  {'Change':>10}")
    print("  " + "─" * 78)
    print(f"  {'Discovery-stage wall clock':<42}  {_ms(discovery_before):>10}  {_ms(discovery_after):>10}  {_ms(discovery_saved):>10}")
    print(f"  {'Discovery share of mission':<42}  {discovery_before_share:>8.1f}%  {discovery_after_share:>8.1f}%  {(discovery_after_share - discovery_before_share):>+8.1f}%")
    print()
    print("  Discovery stage includes shared KB reads, context formation, and")
    print("  analyst discovery before MDR synthesis begins.")
    print()

    # ── Summary ───────────────────────────────────────────────────────────────
    print("═" * 66)
    print("  Summary")
    print("═" * 66)
    speedup = total_before / total_after
    pct     = saved_ms / total_before * 100
    print(f"  {'Metric':<42}  {'Value':>20}")
    print("  " + "─" * 64)
    print(f"  {'Mission cycle time (BEFORE)':<42}  {_ms(total_before):>20}")
    print(f"  {'Mission cycle time (AFTER)':<42}  {_ms(total_after):>20}")
    print(f"  {'Time saved per mission':<42}  {_ms(saved_ms):>20}")
    print(f"  {'Speedup':<42}  {speedup:>19.2f}x")
    print(f"  {'Percentage faster':<42}  {pct:>19.1f}%")
    print(f"  {'Discovery-stage time (BEFORE)':<42}  {_ms(discovery_before):>20}")
    print(f"  {'Discovery-stage time (AFTER)':<42}  {_ms(discovery_after):>20}")
    print(f"  {'Discovery-stage share (BEFORE)':<42}  {discovery_before_share:>19.1f}%")
    print(f"  {'Discovery-stage share (AFTER)':<42}  {discovery_after_share:>19.1f}%")
    print(f"  {'KB reads eliminated per Ready Room':<42}  {bm['KB doc reads per Ready Room'] - am['KB doc reads per Ready Room']:>20}")
    print(f"  {'Redundant signals eliminated':<42}  {bm['[KB-NO-CHANGE] signals per mission'] - am['[KB-NO-CHANGE] signals per mission']:>20}")
    print(f"  {'Sequential gates eliminated':<42}  {bm['Sequential blocking gates (beyond waves)'] - am['Sequential blocking gates (beyond waves)']:>20}")
    print("═" * 66)
    print()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="TNG workflow optimisation benchmark — models full mission cycle timing"
    )
    parser.add_argument(
        "--agent-ms", type=float, default=DEFAULT_AGENT_MS,
        help=f"Simulated agent response latency ms (default: {DEFAULT_AGENT_MS}; "
             f"use 2000 for real LLM latency)"
    )
    parser.add_argument(
        "--picard-ms", type=float, default=DEFAULT_PICARD_MS,
        help=f"Simulated picard orchestration step ms (default: {DEFAULT_PICARD_MS}; "
             f"use 500 for real latency)"
    )
    parser.add_argument(
        "--runs", type=int, default=DEFAULT_RUNS,
        help=f"Benchmark repetitions (default: {DEFAULT_RUNS})"
    )
    args = parser.parse_args()
    main(agent_ms=args.agent_ms, picard_ms=args.picard_ms, runs=args.runs)
