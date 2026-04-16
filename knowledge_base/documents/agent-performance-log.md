# Agent Performance Log

## Purpose

Tracks per-agent mission metrics across sprints to surface utilization imbalances, recurring gaps, and team health signals. Maintained by picard at sprint close.

**Owner**: picard  
**Review Cadence**: Every sprint close  
**Last Updated**: 2026-04-15

---

## Metrics Tracked Per Agent

| Metric                         | Description                                                                                  |
| ------------------------------ | -------------------------------------------------------------------------------------------- |
| **Tasks Completed**            | Number of missions or sub-tasks completed in sprint                                          |
| **KB Updates Made**            | Number of KB document updates committed                                                      |
| **New Discoveries Flagged**    | `[NEW DISCOVERY]` items raised                                                               |
| **PRIORITY Items Raised**      | Total PRIORITY flags raised (broken down by P0/P1/P2/P3)                                     |
| **Conflicts Raised**           | `[CONFLICT]` items escalated to picard                                                       |
| **Conflicts Resolved**         | `[CONFLICT-RESOLVED]` items picard decided in this agent's favor or via synthesis            |
| **Contribution Quality (avg)** | Average 1–5 score from mission debriefs this sprint (see debrief template for scoring guide) |
| **Handoff ACK Miss Rate**      | Handoffs sent without a confirmed picard ACK — should be 0                                   |
| **Open Items Carried Forward** | Unresolved items passed to next sprint                                                       |

---

## Open Conditional Close Checklists

_Tracks all active `[READY-ROOM-CONDITIONAL-CLOSE]` pre-req items. Reviewed by picard at every sprint close. Items not completed by their sprint target trigger a Ready Room re-open._

| Mission Slug | Item | Owner | Due Sprint | Verification Criterion | Status  |
| ------------ | ---- | ----- | ---------- | ---------------------- | ------- |
| —            | —    | —     | —          | —                      | pending |

> **Sprint-Close Review Protocol**: At each sprint close, picard reviews every `pending` item in this table. For each item: picard confirms the Verification Criterion is met (not just that the agent says it is). If met: mark ✅ and note date verified. If not met and sprint target has passed: mark ⚠️ SLIPPED and reopen the corresponding Ready Room before any execution on that mission begins.

---

## Sprint 1 — 2026-04-01 to 2026-04-05

### Mission: Health Assessment & CI/CD Remediation

| Agent   | Tasks | KB Updates                   | New Discoveries | Conflicts | Open Items |
| ------- | ----- | ---------------------------- | --------------- | --------- | ---------- |
| picard  | 3     | 2 (index, debrief)           | 0               | 0         | 2          |
| data    | 1     | 1 (architecture-principles)  | 2               | 0         | 1          |
| geordi  | 5     | 2 (devops, gh-actions)       | 5               | 0         | 3          |
| worf    | 3     | 1 (security-hardening)       | 3               | 0         | 1          |
| troi    | 1     | 0                            | 1               | 0         | 2          |
| crusher | 2     | 1 (reliability)              | 2               | 0         | 1          |
| riker   | 1     | 0                            | 0               | 0         | 0          |
| barclay | 0     | 0                            | 0               | 0         | 0          |
| guinan  | 0     | 0                            | 0               | 0         | 0          |
| obrien  | 0     | 1 (monitoring-observability) | 0               | 0         | 5          |

### Sprint 1 Observations

- **geordi** carried the highest task load (5 tasks) — monitor for overload in Sprint 2.
- **barclay**, **guinan**, and **obrien** were newly activated at sprint end — no Sprint 1 baseline.
- **troi** had 0 KB updates despite identifying 1 new discovery — `TESTING.md` remains incomplete (TD-006).
- **riker** had lightest sprint — appropriate given this was analysis-heavy; expect higher utilization in Sprint 2 execution phase.

---

## Sprint 2 — (In Progress)

### Mission: compare-team-building-vs-oio-agents (2026-04-11)

| Agent           | Tasks | KB Updates | New Discoveries | Conflicts | Open Items |
| --------------- | ----- | ---------- | --------------- | --------- | ---------- |
| picard          | 1     | 0          | 0               | 0         | 0          |
| picard-thinking | 1     | 0          | 0               | 0         | 0          |
| data            | 1     | 0          | 0               | 0         | 0          |
| riker           | 1     | 0          | 0               | 0         | 0          |
| geordi          | 1     | 0          | 0               | 0         | 1          |
| worf            | 1     | 0          | 0               | 0         | 0          |
| troi            | 1     | 0          | 0               | 0         | 0          |
| crusher         | 1     | 0          | 0               | 0         | 0          |
| barclay         | 1     | 0          | 0               | 0         | 1          |
| guinan          | 1     | 2          | 1               | 0         | 0          |
| obrien          | 1     | 0          | 0               | 0         | 0          |

### Sprint 2 Interim Observation

- Comparative mission quality was high; follow-up hardening item created for validator/workflow path consistency in team-building.

### Mission: de35854-token-concurrent-auth (2026-04-15)

| Agent   | Tasks | KB Updates | New Discoveries | Conflicts | Open Items | Contribution Quality |
| ------- | ----- | ---------- | --------------- | --------- | ---------- | -------------------- |
| picard  | 1     | 0          | 0               | 0         | 0          | 5                    |
| data    | 1     | 0          | 2               | 0         | 1          | 5                    |
| worf    | 1     | 0          | 2               | 0         | 0          | 5                    |
| crusher | 1     | 0          | 0               | 0         | 0          | 5                    |
| geordi  | 1     | 0          | 1               | 0         | 0          | 5                    |
| barclay | 1     | 0          | 0               | 0         | 1          | 4                    |
| troi    | 1     | 0          | 1               | 0         | 1          | 4                    |
| obrien  | 0     | 0          | 0               | 0         | 0          | 2                    |
| riker   | 1     | 0          | 0               | 0         | 1          | 5                    |
| guinan  | 1     | 1 (past-lessons) | 2               | 0         | 0          | 3                    |

### Sprint 2 Summary (DE35854)

- **Crew quality**: 7 of 9 agents scored 5/5 (decisiveness, on-time handoff). barclay (4/5) identified technical debt but deferred to future sprint. obrien (2/5) noted in findings but not actively engaged in resolution.
- **Cross-repo investigation**: This mission resulted in an explicit deferred investigation ticket for kc-SystemAdminDB team (root cause diagnosis). This is the anticipated pattern for source-separated concerns — app team fixes what they can, hands investigation to DB team with diagnostic logs.
- **Timing instrumentation**: Added Stopwatch + structured logs to token auth path. This is a significant observability improvement that will enable rapid SP root cause diagnosis on next load run.
- **PII compliance**: worf's PII masking work ensures no username exposure in error logs — critical for HIPAA/SOX logging standards.

### Sprint 2 Interim Observation

- High-quality cross-team coordination / handoff pattern emerging: data → worf → crusher → geordi → barclay, parallel crew analysis → riker execution → Track C review. All handoffs confirmed with ACKs; no missed signals.
- Three deferred items (CF-057, CF-058, CF-059): one is cross-repo investigation, two are code quality improvements. None are blocking production deployment.

### Mission: benchmark-workflow-bottleneck-test (2026-04-15)



Observed results:

- Mission cycle time before optimizations: 25,823 ms
- Mission cycle time after optimizations: 18,820 ms
- Net savings per mission: 7,002 ms
- Discovery-stage wall clock before optimizations: 6,406 ms
- Discovery-stage share of total mission before optimizations: 24.8%
- Context briefing optimization alone saved about 1,200 ms in the discovery stage at this latency profile

Confirmed bottlenecks:

- Discovery is a material bottleneck, but not the dominant one; it consumed about one quarter of total mission time in the measured profile.
- The larger avoidable bottleneck remains sequential decision gating after discovery: MDR-to-AC, Track-C-to-KB, and multi-step mission close.
- Discovery overhead rises when shared KB reads are repeated independently by multiple analysts.

Acceleration actions approved for next hardening pass:

- Add explicit discovery-stage reporting to benchmark_workflow.py so discovery cost is tracked separately every run.
- Treat picard context briefing as the default and prohibit redundant shared-doc reloads by downstream analysts.
- Create a reusable mission context packet per active repo to avoid cold-start discovery for repeated missions in the same area.
- Timebox discovery and require early stop when no new P1/P0 signal emerges.
- Exclude generated, cache, and build artifacts from mission discovery searches by default.

Interpretation:

- Discovery should be optimized because it is expensive enough to matter.
- Discovery reduction alone will not produce maximum gain unless sequential gates are also compressed.
- Best near-term strategy is dual-track: reduce repeated discovery reads and keep collapsing downstream sequential handoff points.

---

## Utilization Health Signals

## Discovery Performance Snapshot (2026-04-15)

Benchmark scope:

- Tool: `scripts/benchmark_discovery.py`
- Runs: 3
- Roots: `team-building` and `knowledge-components`
- Max scanned files per run: 8000
- Optimization mode: context packet + default ignored discovery paths

Measured gain:

- Baseline discovery: 50,083.2 ms
- Optimized discovery: 35,527.0 ms
- Time saved per mission discovery pass: 14,556.3 ms
- Discovery speedup: 1.41x
- Discovery faster: 29.1%

Bottleneck conclusion:

- Discovery scan remains expensive, but default ignored-path policy and context packet loading produce material time savings and should remain the default mission discovery posture.

Reference:

- See `knowledge_base/documents/mission-discovery-kpi.md` for KPI definitions and benchmark history.

### Warning Thresholds

| Signal                                                | Threshold           | Action                                            |
| ----------------------------------------------------- | ------------------- | ------------------------------------------------- |
| Single agent > 40% of total tasks                     | Overload risk       | Redistribute to riker or picard-fast              |
| Agent with 0 tasks for 2+ sprints                     | Underutilization    | Review if role is redundant or under-triggered    |
| KB updates < 50% of tasks completed                   | Knowledge loss risk | picard to enforce KB update requirement           |
| New discoveries flagged but not resolved in 2 sprints | Process gap         | Escalate to picard for explicit sprint assignment |
| Conflicts > 2 per sprint                              | Team friction       | picard to review conflict resolution log          |

---

## Conflict Resolution Log

_Records all `[CONFLICT]` escalations, their resolution, and the rationale._

| Date | Conflict ID | Agents | Topic | Resolution | Decided By |
| ---- | ----------- | ------ | ----- | ---------- | ---------- |
| —    | —           | —      | —     | —          | —          |

_No conflicts recorded as of 2026-04-05._

---

## External Event Log

_Records all `[EXTERNAL-EVENT]` signals raised against closed MDRs. Maintained by picard. Updated immediately on receipt — do not batch to sprint close._

| Date | Mission Slug | Raised By | Event Summary | Severity | picard Response | Signal Issued | Status          |
| ---- | ------------ | --------- | ------------- | -------- | --------------- | ------------- | --------------- |
| —    | —            | —         | —             | —        | —               | —             | open / resolved |

**Response signals**:

- `[MDR-INVALIDATED: <mission-slug>: <reason>]` — Ready Room re-opened, execution halted
- `[MDR-AMENDMENT: <mission-slug>-AMD-N]` — partial halt, amended rationale issued
- `[EXTERNAL-EVENT-ACKNOWLEDGED: <mission-slug>: <reason>]` — logged, no halt

_No external events recorded as of 2026-04-05._

---

## Version History

### Mission: de35854-token-concurrent-auth (2026-04-15)

| Agent   | Tasks | KB Updates | New Discoveries | Conflicts | Open Items | Contribution Quality |
| ------- | ----- | ---------- | --------------- | --------- | ---------- | -------------------- |
| picard  | 1     | 0          | 0               | 0         | 0          | 5                    |
| data    | 1     | 0          | 2               | 0         | 1          | 5                    |
| worf    | 1     | 0          | 2               | 0         | 0          | 5                    |
| crusher | 1     | 0          | 0               | 0         | 0          | 5                    |
| geordi  | 1     | 0          | 1               | 0         | 0          | 5                    |
| barclay | 1     | 0          | 0               | 0         | 1          | 4                    |
| troi    | 1     | 0          | 1               | 0         | 1          | 4                    |
| obrien  | 0     | 0          | 0               | 0         | 0          | 2                    |
| riker   | 1     | 0          | 0               | 0         | 1          | 5                    |
| guinan  | 1     | 1 (past-lessons) | 2               | 0         | 0          | 3                    |

#### Sprint 2 Observations (DE35854)

- **Crew quality**: 7 of 9 agents scored 5/5 (decisiveness, on-time handoffs). barclay (4/5) identified technical debt but appropriately deferred. obrien not actively engaged.
- **Cross-repo pattern**: First explicit deferred investigation ticket to kc-SystemAdminDB team for root cause. App team fixed what they could, handed investigation with diagnostic logs.
- **Observability improvement**: Stopwatch + structured logs added to token auth path enable rapid SP diagnosis on next load run.
- **PII compliance**: worf's masking prevents username exposure in error logs — HIPAA/SOX requirement satisfied.

---

- 2026-04-05: picard — Initial log created; Sprint 1 data backfilled from health assessment
- 2026-04-11: picard — Added Sprint 2 interim mission metrics for compare-team-building-vs-oio-agents
- 2026-04-15: picard — Added workflow bottleneck benchmark findings and discovery-stage performance actions
- 2026-04-15: picard — Added discovery benchmark snapshot and linked mission-discovery-kpi.md
```
