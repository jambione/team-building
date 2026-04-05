# Agent Performance Log

## Purpose

Tracks per-agent mission metrics across sprints to surface utilization imbalances, recurring gaps, and team health signals. Maintained by picard at sprint close.

**Owner**: picard  
**Review Cadence**: Every sprint close  
**Last Updated**: 2026-04-05

---

## Metrics Tracked Per Agent

| Metric | Description |
|--------|-------------|
| **Tasks Completed** | Number of missions or sub-tasks completed in sprint |
| **KB Updates Made** | Number of KB document updates committed |
| **New Discoveries Flagged** | `[NEW DISCOVERY]` items raised |
| **Conflicts Escalated** | `[CONFLICT]` items escalated to picard |
| **Handoff ACKs Sent** | Confirmed handoff receipts issued |
| **Handoff ACKs Received** | Confirmed handoff receipts received from picard |
| **Open Items Carried Forward** | Unresolved items passed to next sprint |

---

## Sprint 1 — 2026-04-01 to 2026-04-05

### Mission: Health Assessment & CI/CD Remediation

| Agent | Tasks | KB Updates | New Discoveries | Conflicts | Open Items |
|-------|-------|-----------|-----------------|-----------|------------|
| picard | 3 | 2 (index, debrief) | 0 | 0 | 2 |
| data | 1 | 1 (architecture-principles) | 2 | 0 | 1 |
| geordi | 5 | 2 (devops, gh-actions) | 5 | 0 | 3 |
| worf | 3 | 1 (security-hardening) | 3 | 0 | 1 |
| troi | 1 | 0 | 1 | 0 | 2 |
| crusher | 2 | 1 (reliability) | 2 | 0 | 1 |
| riker | 1 | 0 | 0 | 0 | 0 |
| barclay | 0 | 0 | 0 | 0 | 0 |
| guinan | 0 | 0 | 0 | 0 | 0 |
| obrien | 0 | 1 (monitoring-observability) | 0 | 0 | 5 |

### Sprint 1 Observations

- **geordi** carried the highest task load (5 tasks) — monitor for overload in Sprint 2.
- **barclay**, **guinan**, and **obrien** were newly activated at sprint end — no Sprint 1 baseline.
- **troi** had 0 KB updates despite identifying 1 new discovery — `TESTING.md` remains incomplete (TD-006).
- **riker** had lightest sprint — appropriate given this was analysis-heavy; expect higher utilization in Sprint 2 execution phase.

---

## Sprint 2 — (Pending)

*To be populated at Sprint 2 close by picard.*

---

## Utilization Health Signals

### Warning Thresholds

| Signal | Threshold | Action |
|--------|-----------|--------|
| Single agent > 40% of total tasks | Overload risk | Redistribute to riker or picard-fast |
| Agent with 0 tasks for 2+ sprints | Underutilization | Review if role is redundant or under-triggered |
| KB updates < 50% of tasks completed | Knowledge loss risk | picard to enforce KB update requirement |
| New discoveries flagged but not resolved in 2 sprints | Process gap | Escalate to picard for explicit sprint assignment |
| Conflicts > 2 per sprint | Team friction | picard to review conflict resolution log |

---

## Conflict Resolution Log

*Records all `[CONFLICT]` escalations, their resolution, and the rationale.*

| Date | Conflict ID | Agents | Topic | Resolution | Decided By |
|------|-------------|--------|-------|-----------|------------|
| — | — | — | — | — | — |

*No conflicts recorded as of 2026-04-05.*

---

## Version History

```
- 2026-04-05: picard — Initial log created; Sprint 1 data backfilled from health assessment
```
