# Acceptance Criteria — <mission-slug>

> **Instructions**: Copy this template for each mission. File as `knowledge_base/missions/acceptance-criteria/YYYY-MM-DD-<mission-slug>-ac.md`.
> troi drafts. picard approves with `[AC-APPROVED: <mission-slug>]`. No code begins until approval is emitted.

---

## Metadata

| Field | Value |
|-------|-------|
| **Mission** | _One-line mission description_ |
| **Mission Slug** | `<mission-slug>` |
| **Date** | YYYY-MM-DD |
| **Author** | troi |
| **Approved By** | picard — `[AC-APPROVED: <mission-slug>]` |
| **Status** | draft / approved |

---

## Definition of Done

> Execution is complete when all Acceptance Criteria below have:
> 1. At least one passing automated test per scenario
> 2. Track C (troi) verified in the post-execution review
>
> Code may not be merged until both conditions are met.

---

## Acceptance Criteria

### AC-01: <Short Title>

**Scenario**: <What situation this spec covers — one sentence>

- **Given** <precondition — the system or user is in a specific state>
- **When** <an action or event occurs>
- **Then** <the expected observable, testable outcome>
- **And** <additional assertion> *(optional — add as many And lines as needed)*

---

### AC-02: <Short Title>

**Scenario**: <What situation this spec covers>

- **Given** <precondition>
- **When** <action or event>
- **Then** <expected observable outcome>

---

### AC-03: <Error / Rejection Path — Short Title>

**Scenario**: <What error or invalid-input situation this covers>

- **Given** <precondition — system or user state>
- **When** <invalid action or edge-case event>
- **Then** <expected observable failure or rejection outcome>
- **And** <the system remains in a consistent, safe state> *(adapt as needed)*

---

## Traceability

> Each AC must trace to a decision outcome in the MDR. If an outcome has no AC, it is out of scope or an oversight — picard decides which.

| AC ID | MDR Decision Outcome | Tests Written | Track C Verified |
|-------|---------------------|:-------------:|:----------------:|
| AC-01 | | [ ] | [ ] |
| AC-02 | | [ ] | [ ] |
| AC-03 | | [ ] | [ ] |

---

## troi's Notes

_troi uses this section for any quality or UX observations that do not fit neatly into a Given/When/Then scenario — e.g., performance expectations, accessibility considerations, error message clarity._

---

*"troi returns control to picard. [ac-draft-complete]"*
