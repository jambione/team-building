# Mission Discovery KPI

## Purpose

Tracks mission discovery performance over time so bottlenecks can be identified and reduced with measurable impact.

**Owner**: picard  
**Review Cadence**: every benchmark run and sprint close  
**Last Updated**: 2026-04-15

---

## KPI Definitions

| KPI                     | Definition                                                  |
| ----------------------- | ----------------------------------------------------------- |
| Discovery Total (ms)    | End-to-end mission discovery wall-clock time per run        |
| Discovery Doc Load (ms) | Time to load mission context docs or packet                 |
| Discovery Scan (ms)     | Time spent scanning workspace files for discovery signals   |
| Discovery Speedup (x)   | Baseline discovery time divided by optimized discovery time |
| Discovery Faster (%)    | Relative reduction from baseline to optimized               |
| Time Saved (ms)         | Baseline discovery time minus optimized discovery time      |

---

## Default Discovery Optimization Policy

1. Use `knowledge_base/current/mission-context-packet.json` as the default context source.
2. Regenerate packet via `scripts/generate_context_packet.py` when stale or missing.
3. Exclude noisy folders by default in discovery scans:
   - `.git`, `.angular`, `node_modules`, `dist`, `build`, `bin`, `obj`, `coverage`, `__pycache__`, `Web`
4. Benchmark and report discovery in baseline vs optimized mode using `scripts/benchmark_discovery.py`.

---

## Benchmark History

| Date | Runs | Roots | Max Files | Baseline (ms) | Optimized (ms) | Speedup (x) | Faster (%) | Saved (ms) |
| ---- | ---- | ----- | --------- | ------------: | -------------: | ----------: | ---------: | ---------: |

---

## Latest Benchmark Notes

_(no benchmarks recorded yet)_
