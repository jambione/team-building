# Acceptance Criteria — phoenix-code-summary-features-observations

## Metadata

| Field        | Value                                                                      |
| ------------ | -------------------------------------------------------------------------- |
| Mission      | Add focused Phoenix code-summary features and remediate known observations |
| Mission Slug | phoenix-code-summary-features-observations                                 |
| Date         | 2026-04-19                                                                 |
| Author       | troi                                                                       |
| Approved By  | picard — [AC-APPROVED: phoenix-code-summary-features-observations]         |
| Status       | approved                                                                   |

---

## Definition of Done

Execution is complete when:

1. Each AC has at least one passing automated verification in the touched area.
2. Track C reviews from worf, troi, and crusher each return PASS or CONDITIONAL with explicit disposition.

---

## Acceptance Criteria

### AC-01: Phoenix feature enhancement is visible and scoped

Scenario: A new Phoenix code-summary feature is introduced in scoped components without broad legacy migration.

- Given the Phoenix code-summary components selected in the MDR
- When the new feature implementation is applied
- Then the feature is visible in the affected Phoenix UI state
- And no unrelated legacy code-summary layout is materially changed

---

### AC-02: Known styling observations are corrected

Scenario: Existing observation defects in Phoenix code-summary styling are addressed.

- Given the documented observation list in prior mission artifacts
- When the observation fixes are implemented
- Then each targeted visual defect has an explicit before/after verification note
- And no new style regressions are introduced in unaffected code-summary states

---

### AC-03: Verification noise blocker is removed

Scenario: Previously unrelated Phoenix spec typing errors no longer block mission-level verification.

- Given the known procedure-renderer spec typing blocker
- When the blocker fix is applied
- Then the targeted test command for this mission runs without that pre-existing blocker
- And test output clearly attributes any remaining failures to non-blocker causes

---

### AC-04: Error path and rollback clarity

Scenario: If any fix introduces an unintended regression, rollback scope is clear and safe.

- Given a regression is detected during verification
- When rollback is initiated for a specific touched file set
- Then the rollback scope is limited to mission changes
- And the verification suite can be rerun to confirm restoration

---

## Traceability

| AC ID | MDR Decision Outcome                            | Tests Written | Track C Verified |
| ----- | ----------------------------------------------- | :-----------: | :--------------: |
| AC-01 | Scoped feature delivery in Phoenix code-summary |      [ ]      |       [ ]        |
| AC-02 | Observation remediation in targeted styles      |      [ ]      |       [ ]        |
| AC-03 | Procedure-renderer spec blocker removal         |      [ ]      |       [ ]        |
| AC-04 | Safe rollback and recovery path                 |      [ ]      |       [ ]        |

---

## troi Notes

- Scope control is mandatory. This mission is not a full legacy code-summary migration.
- Verification should include at least one targeted UI path and one targeted automated test path.
- Any conditional Track C verdict must include a concrete disposition in the Mission Go/No-Go block.

troi returns control to picard. [ac-draft-complete]
