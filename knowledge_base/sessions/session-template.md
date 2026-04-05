# Session Journal — [YYYY-MM-DD-HH]

> **Instructions**: Copy this template for each new session. File as `YYYY-MM-DD-HH-<mission-slug>.md`.
> guinan is the designated reader of session journals for cross-session continuity.

---

## Session Metadata

| Field | Value |
|-------|-------|
| **Session ID** | YYYY-MM-DD-HH |
| **Date** | YYYY-MM-DD |
| **Mission** | _One-line description_ |
| **Opened By** | picard |
| **Status** | open / closed |

---

## Mission Objective

_Describe what this session set out to accomplish._

---

## KB Documents Consulted

_List every KB document picard and crew referenced during this session._

- [ ] `knowledge_base/documents/<doc>.md` — reason consulted

---

## Crew Engaged

_Which agents were activated and in what order._

| Agent | Role in Mission | Trigger | Handoff ACK |
|-------|----------------|---------|-------------|
| picard | Orchestrator | — | — |
| | | | |

---

## Decisions Made

_Record every significant decision with rationale. These become candidates for ADRs._

| # | Decision | Rationale | Decided By | Date |
|---|----------|-----------|------------|------|
| 1 | | | picard | |

---

## Conflicts Escalated

_Record any `[CONFLICT]` items raised, their resolution, and who decided._

| Conflict ID | Agents | Topic | Raised At (step #) | Resolution | Decided By |
|-------------|--------|-------|-------------------|-----------|------------|
| — | — | No conflicts | — | — | — |

---

## PRIORITY Items

_All `[PRIORITY]` tags raised during the Ready Room. P1 items block `[READY-ROOM-CLOSED]`._

| ID | Level | Raised By | Summary | Resolution | Status |
|----|-------|-----------|---------|------------|--------|
| P-01 | P1/P2/P3 | | | | open / resolved / mitigated / accepted-risk |

---

## [NEW DISCOVERY] Flags

_All new discoveries raised this session. Must be resolved or explicitly deferred before session close._

| Flag | Raised By | KB Document to Update | Status |
|------|-----------|-----------------------|--------|
| | | | pending / resolved / deferred |

---

## External Events

_`[EXTERNAL-EVENT]` signals raised against this mission's MDR — at any point, including post-close. Each must be logged here AND in `agent-performance-log.md` External Event Log._

| Date | Raised By | Event Summary | Severity | picard Response Signal | Status |
|------|-----------|---------------|----------|----------------------|--------|
| — | — | None | — | — | — |

---

## Handoff Log

_Complete record of handoffs and ACK confirmations during this session._

| # | From | To | Trigger | ACK Confirmed |
|---|------|----|---------|-|
| 1 | picard | | `[trigger]` | `[trigger-received ✓ picard]` |

---

## Open Items (Carry Forward)

_Items not resolved this session. Each must have an owner and target sprint._

| # | Item | Owner | Target Sprint | Priority |
|---|------|-------|---------------|----------|
| 1 | | | | |

---

## Mission Summary

_picard's closing summary — what was accomplished, what was learned, what was deferred._

---

## WES Proposals

_All `WES-PROPOSAL-<N>` items submitted this session and their disposition._

| Proposal ID | Summary | Status | Rationale |
|-------------|---------|--------|-----------|
| WES-PROPOSAL-1 | | awaiting-approval / approved / rejected / deferred | |

---

## Session Close

- [ ] Ready Room closed with `[READY-ROOM-CLOSED]` or `[READY-ROOM-CONDITIONAL-CLOSE]` before execution began
- [ ] If conditional close: Pre-req Checklist recorded with owner + sprint for every item
- [ ] If conditional close: Full `[READY-ROOM-CLOSED]` issued after all checklist items verified before riker engaged
- [ ] All P1 PRIORITY items resolved (or conditionally resolved with checklist) before Ready Room closed
- [ ] Mission Decision Record (MDR) produced by picard-thinking
- [ ] All crew have updated their domain KB documents
- [ ] All `[NEW DISCOVERY]` flags resolved or explicitly deferred with owner + sprint
- [ ] All `[EXTERNAL-EVENT]` signals raised during this session logged in `agent-performance-log.md` External Event Log
- [ ] All WES proposals dispositioned (approved / rejected / deferred)
- [ ] All open items recorded with owner + sprint
- [ ] Conflict resolution log updated
- [ ] Agent performance log updated
- [ ] Mission Debrief filled (`mission-debrief-template.md`)
- [ ] guinan notified of session journal availability for cross-session continuity

**Session Status**: open / **closed**

_"Make it so!"_ — picard
