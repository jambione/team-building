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

| Date       | Runs | Roots                                | Max Files | Baseline (ms) | Optimized (ms) | Speedup (x) | Faster (%) | Saved (ms) |
| ---------- | ---- | ------------------------------------ | --------- | ------------: | -------------: | ----------: | ---------: | ---------: |
| 2026-04-15 | 3    | team-building + knowledge-components | 8000      |       50083.2 |        35527.0 |        1.41 |       29.1 |    14556.3 |

---

## Latest Benchmark Notes (2026-04-15)

- Measurement command:
  - `python scripts/benchmark_discovery.py --runs 3 --roots . "c:\inetpub\wwwroot\knowledge-components" --max-files 8000`
- Context packet coverage: `4/4` docs included.
- Largest gain came from faster workspace scan under ignored-path policy.
- Result confirms discovery acceleration with current defaults.
