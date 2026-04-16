#!/usr/bin/env python3
"""
Benchmark mission discovery bottlenecks using real workspace scans.

Compares:
- BASELINE: direct multi-doc reads + broad scan without ignored folders
- OPTIMIZED: context packet read + scan with default ignored folders
"""

from __future__ import annotations

import argparse
import os
import re
import statistics
import subprocess
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Set

DEFAULT_DOCS = [
    "knowledge_base/current/workspace-context.md",
    "knowledge_base/current/session-continuity.md",
    "knowledge_base/current/team-quick-reference.md",
    "knowledge_base/documents/past-lessons-learned.md",
]

DEFAULT_IGNORE_DIRS = {
    ".git",
    ".angular",
    "node_modules",
    "dist",
    "build",
    "bin",
    "obj",
    "coverage",
    "__pycache__",
    "Web",
}

TEXT_EXTENSIONS: Set[str] = {
    ".md", ".txt", ".json", ".yaml", ".yml", ".py", ".ps1", ".ts", ".tsx", ".js", ".cs", ".xml"
}

SEARCH_PATTERNS = re.compile(
    r"READY-ROOM|PRIORITY|MDR|acceptance criteria|discovery|mission|bottleneck",
    flags=re.IGNORECASE,
)


@dataclass
class ScanStats:
    elapsed_ms: float
    files_seen: int
    files_scanned: int
    hits: int


@dataclass
class DiscoveryStats:
    elapsed_ms: float
    doc_load_ms: float
    scan_ms: float
    files_seen: int
    files_scanned: int
    hits: int


def repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def load_docs_direct(root: Path, docs: Iterable[str]) -> int:
    loaded = 0
    for rel in docs:
        path = root / rel
        if path.exists():
            _ = path.read_text(encoding="utf-8", errors="ignore")
            loaded += 1
    return loaded


def load_packet(root: Path, packet_rel: str) -> bool:
    packet = root / packet_rel
    if not packet.exists():
        return False
    _ = packet.read_text(encoding="utf-8", errors="ignore")
    return True


def scan_workspace(
    roots: List[Path],
    ignore_dirs: Optional[Set[str]],
    max_files: int,
    max_bytes: int,
) -> ScanStats:
    t0 = time.perf_counter()
    files_seen = 0
    files_scanned = 0
    hits = 0

    for root in roots:
        if not root.exists():
            continue

        for current, dirs, files in os.walk(root):
            if ignore_dirs:
                dirs[:] = [d for d in dirs if d not in ignore_dirs]

            for name in files:
                files_seen += 1
                if files_scanned >= max_files:
                    elapsed = (time.perf_counter() - t0) * 1000
                    return ScanStats(elapsed, files_seen, files_scanned, hits)

                ext = Path(name).suffix.lower()
                if ext not in TEXT_EXTENSIONS:
                    continue

                path = Path(current) / name
                try:
                    if path.stat().st_size > max_bytes:
                        continue
                    text = path.read_text(encoding="utf-8", errors="ignore")
                except OSError:
                    continue

                files_scanned += 1
                if SEARCH_PATTERNS.search(text):
                    hits += 1

    elapsed = (time.perf_counter() - t0) * 1000
    return ScanStats(elapsed, files_seen, files_scanned, hits)


def run_baseline(root: Path, roots: List[Path], max_files: int, max_bytes: int) -> DiscoveryStats:
    t0 = time.perf_counter()

    d0 = time.perf_counter()
    load_docs_direct(root, DEFAULT_DOCS)
    doc_ms = (time.perf_counter() - d0) * 1000

    s = scan_workspace(roots=roots, ignore_dirs=None, max_files=max_files, max_bytes=max_bytes)

    total_ms = (time.perf_counter() - t0) * 1000
    return DiscoveryStats(total_ms, doc_ms, s.elapsed_ms, s.files_seen, s.files_scanned, s.hits)


def ensure_packet(root: Path, packet_rel: str) -> None:
    packet = root / packet_rel
    if packet.exists():
        return

    script = root / "scripts" / "generate_context_packet.py"
    subprocess.run(
        ["python", str(script), "--output", packet_rel],
        check=True,
        cwd=str(root),
    )


def run_optimized(
    root: Path,
    roots: List[Path],
    max_files: int,
    max_bytes: int,
    packet_rel: str,
    ignore_dirs: Set[str],
) -> DiscoveryStats:
    t0 = time.perf_counter()

    ensure_packet(root, packet_rel)
    d0 = time.perf_counter()
    load_packet(root, packet_rel)
    doc_ms = (time.perf_counter() - d0) * 1000

    s = scan_workspace(roots=roots, ignore_dirs=ignore_dirs, max_files=max_files, max_bytes=max_bytes)

    total_ms = (time.perf_counter() - t0) * 1000
    return DiscoveryStats(total_ms, doc_ms, s.elapsed_ms, s.files_seen, s.files_scanned, s.hits)


def mean(values: List[float]) -> float:
    return statistics.mean(values) if values else 0.0


def main() -> None:
    parser = argparse.ArgumentParser(description="Benchmark mission discovery performance")
    parser.add_argument("--runs", type=int, default=5)
    parser.add_argument("--roots", nargs="*", default=["."])
    parser.add_argument("--max-files", type=int, default=6000)
    parser.add_argument("--max-bytes", type=int, default=524288)
    parser.add_argument("--packet", default="knowledge_base/current/mission-context-packet.json")
    parser.add_argument(
        "--ignore-dirs",
        default=",".join(sorted(DEFAULT_IGNORE_DIRS)),
        help="Comma-separated ignored folder names for optimized discovery",
    )
    args = parser.parse_args()

    root = repo_root()
    scan_roots = [Path(p).resolve() for p in args.roots]
    ignore_dirs = {d.strip() for d in args.ignore_dirs.split(",") if d.strip()}

    print("=" * 72)
    print("  Mission Discovery Benchmark")
    print("=" * 72)
    print(f"  Runs: {args.runs}")
    print(f"  Scan roots: {', '.join(str(p) for p in scan_roots)}")
    print(f"  Max scanned files per run: {args.max_files}")
    print(f"  Max file size: {args.max_bytes} bytes")
    print(f"  Optimized ignored dirs: {', '.join(sorted(ignore_dirs))}")
    print("=" * 72)
    print()

    baseline_runs: List[DiscoveryStats] = []
    optimized_runs: List[DiscoveryStats] = []

    print("  Running", end="", flush=True)
    for _ in range(args.runs):
        baseline_runs.append(run_baseline(root, scan_roots, args.max_files, args.max_bytes))
        optimized_runs.append(run_optimized(root, scan_roots, args.max_files, args.max_bytes, args.packet, ignore_dirs))
        print(".", end="", flush=True)
    print(" done")
    print()

    b_total = mean([r.elapsed_ms for r in baseline_runs])
    o_total = mean([r.elapsed_ms for r in optimized_runs])
    b_doc = mean([r.doc_load_ms for r in baseline_runs])
    o_doc = mean([r.doc_load_ms for r in optimized_runs])
    b_scan = mean([r.scan_ms for r in baseline_runs])
    o_scan = mean([r.scan_ms for r in optimized_runs])

    b_seen = mean([float(r.files_seen) for r in baseline_runs])
    o_seen = mean([float(r.files_seen) for r in optimized_runs])
    b_scanned = mean([float(r.files_scanned) for r in baseline_runs])
    o_scanned = mean([float(r.files_scanned) for r in optimized_runs])

    saved = b_total - o_total
    pct = (saved / b_total * 100.0) if b_total > 0 else 0.0

    print("-" * 72)
    print("  Discovery Timing (mean per run)")
    print("-" * 72)
    print(f"  {'Metric':<34} {'Baseline':>12} {'Optimized':>12} {'Delta':>12}")
    print(f"  {'Total discovery':<34} {b_total:>10.1f} ms {o_total:>10.1f} ms {saved:>10.1f} ms")
    print(f"  {'Doc load':<34} {b_doc:>10.1f} ms {o_doc:>10.1f} ms {(b_doc - o_doc):>10.1f} ms")
    print(f"  {'Workspace scan':<34} {b_scan:>10.1f} ms {o_scan:>10.1f} ms {(b_scan - o_scan):>10.1f} ms")
    print()

    print("-" * 72)
    print("  Scan Throughput Signals")
    print("-" * 72)
    print(f"  {'Files seen':<34} {b_seen:>12.0f} {o_seen:>12.0f} {(o_seen - b_seen):>12.0f}")
    print(f"  {'Files scanned':<34} {b_scanned:>12.0f} {o_scanned:>12.0f} {(o_scanned - b_scanned):>12.0f}")
    print(f"  {'Keyword hits':<34} {mean([float(r.hits) for r in baseline_runs]):>12.0f} {mean([float(r.hits) for r in optimized_runs]):>12.0f} {(mean([float(r.hits) for r in optimized_runs]) - mean([float(r.hits) for r in baseline_runs])):>12.0f}")
    print()

    print("=" * 72)
    print("  Summary")
    print("=" * 72)
    print(f"  Discovery speedup: {(b_total / o_total) if o_total > 0 else 0.0:.2f}x")
    print(f"  Discovery faster by: {pct:.1f}%")
    print(f"  Time saved per mission discovery run: {saved:.1f} ms")
    print("=" * 72)


if __name__ == "__main__":
    main()
