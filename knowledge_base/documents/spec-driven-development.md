# Spec-Driven Development

## Why This Exists

The TNG agent system has strong decision discipline (Ready Room, MDR) and test strategy tooling (troi). The gap is the space between "decision made" and "code written." Without a shared behavior contract, scope is ambiguous, tests are written after the fact, and "done" means different things to different crew members.

Acceptance Criteria fix this by making the behavior contract **explicit, testable, and approved before a single line of code is written**.

---

## The Contract

Acceptance Criteria are the gate between a closed decision and the start of execution.

```
MDR approved → AC drafted → [AC-APPROVED] → [READY-ROOM-CLOSED] → execution begins
```

No code. No PR. No infrastructure change. Until `[AC-APPROVED]` is emitted by picard.

---

## Format: Given/When/Then

Every Acceptance Criterion is written in Gherkin-style Given/When/Then. This is a deliberate choice: it forces the author to name a precondition, an action, and an observable outcome — making the spec independently verifiable.

```
### AC-<N>: <Short Title>

**Scenario**: <one-sentence description of the situation>

- **Given** <precondition — the system or user is in a specific state>
- **When** <an action or event occurs>
- **Then** <expected observable, testable outcome>
- **And** <additional assertion> *(optional)*
```

### Rules for writing valid ACs

| Rule | Rationale |
|------|-----------|
| Every MDR decision outcome gets at least one AC | If an outcome has no spec, it is not being built to any agreed standard |
| Rejection and error paths get their own ACs | Happy-path-only specs are incomplete specs |
| Every **Then** must be observable and testable | "System behaves correctly" is not a Then — it is a wish |
| No prose paragraphs — bullets only | Forces precision; prevents hidden assumptions |
| troi authors; picard approves | Single authorship prevents spec drift; single approval prevents gate bypass |

---

## Who Does What

| Role | Responsibility |
|------|----------------|
| **troi** | Drafts all ACs in STEP 5B — one per MDR decision outcome plus edge cases and error paths. Files at `knowledge_base/missions/acceptance-criteria/YYYY-MM-DD-<mission-slug>-ac.md`. Ends with `[ac-draft-complete]`. |
| **picard** | Reviews ACs against MDR. Requests revision if any outcome is unspecced, any Then is untestable, or any error path is missing. Emits `[AC-APPROVED: <mission-slug>]` when complete. |
| **riker** | Reads approved ACs before beginning execution. Uses them to scope work assignments. |
| **crew (execution)** | Each assigned agent writes tests against the ACs before implementing. |
| **Track C (troi, post-execution)** | Verifies each AC has passing tests in the Traceability table during the Track C review. |

---

## The Gate

`[READY-ROOM-CLOSED]` is **blocked** until picard emits `[AC-APPROVED: <mission-slug>]`.

This is enforced by:
1. STEP 5B in `ready-room.prompt.md` — the AC phase is an explicit step before STEP 6 (Close)
2. Pre-close Crew Checklist in PLAYBOOK.md — `Acceptance Criteria approved: yes / no` is a checklist item
3. picard Pre-Close Crew Validation in `picard.agent.md` — step 5 in the validation sequence

The gate cannot be bypassed by conditional close. `[READY-ROOM-CONDITIONAL-CLOSE]` also requires `[AC-APPROVED]` — the difference is that execution is gated on a pre-req checklist, not that specs are optional.

---

## Traceability

Every AC document includes a Traceability table:

| AC ID | MDR Decision Outcome | Tests Written | Track C Verified |
|-------|---------------------|:-------------:|:----------------:|

- **Tests Written**: riker or the assigned execution agent marks this `[x]` when at least one test exists for the scenario.
- **Track C Verified**: troi marks this `[x]` during the post-execution Track C review when tests pass and the behavior is observable.

A Track C **PASS** verdict is not valid if any row in the Traceability table has an empty Track C Verified checkbox.

---

## Template

See `knowledge_base/missions/acceptance-criteria-template.md`.

AC documents are filed at: `knowledge_base/missions/acceptance-criteria/YYYY-MM-DD-<mission-slug>-ac.md`

---

## Lessons Learned

_This section is updated by troi as patterns emerge across missions._

| Pattern | Observation | First Mission |
|---------|-------------|---------------|
| Missing error-path ACs | Teams most commonly skip rejection and error-path scenarios. Always ask: "what happens when the user or system does the wrong thing?" | spec-driven-development (infrastructure) |
| Untestable Thens | "System is responsive" and "behaves correctly" are not Thens. Every Then should be verifiable by a test assertion or a human observer in < 30 seconds. | spec-driven-development (infrastructure) |
