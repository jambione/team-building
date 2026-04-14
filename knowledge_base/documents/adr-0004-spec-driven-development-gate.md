# ADR-0004: Spec-Driven Development Gate (Acceptance Criteria Before Execution)

## Status

**Accepted** — 2026-04-12

| Field | Value |
|-------|-------|
| **ADR Number** | 0004 |
| **Date Accepted** | 2026-04-12 |
| **Decided By** | picard |
| **Domain** | Process / Quality |
| **Owner** | troi |

---

## Context

The TNG agent team had strong decision discipline (Ready Room, MDR) and a post-execution review process (Track C). The gap was the space between "decision made" and "code written." Without a shared, explicit behavior contract, scope was ambiguous, tests were written after the fact, and "done" meant different things to different crew members.

Two failure patterns were observed:
1. Execution began from an MDR that described intent but not observable outcomes — crew members disagreed on what completion looked like.
2. Track C reviews caught gaps that could have been specified upfront, requiring rework.

---

## Options Considered

### Option A — No change (continue MDR → execution)

- **Pros**: Less ceremony; faster to start execution
- **Cons**: Ambiguous definition of done; tests written after the fact; Track C catches avoidable rework

### Option B — Acceptance Criteria as a hard gate (STEP 5B)

- **Pros**: Behavior contract is explicit and testable before any code starts; traceability between MDR decisions and tests; Track C becomes a verification step rather than a discovery step
- **Cons**: Additional step in the Ready Room; troi must draft specs for every mission

### Option C — Optional AC drafting (team decides per mission)

- **Pros**: Flexibility
- **Cons**: Inconsistent application; gate becomes meaningless when skipped under pressure

---

## Decision

Acceptance Criteria are a hard gate between MDR approval and `[READY-ROOM-CLOSED]`. troi drafts Given/When/Then specs for every MDR decision outcome. picard approves with `[AC-APPROVED: <mission-slug>]`. `[READY-ROOM-CLOSED]` may not be issued until `[AC-APPROVED]` is emitted. This applies to all missions without exception — Option C was explicitly rejected because optional gates erode under delivery pressure.

---

## Consequences

### Positive
- Every execution starts from a shared, testable definition of done
- Tests can be written before implementation (spec-first)
- Track C has an explicit traceability table to verify against
- Rework from ambiguous scope is reduced

### Negative / Trade-offs
- Every Ready Room has an additional step (STEP 5B)
- troi carries a drafting responsibility on every mission
- Short missions may feel over-specified

### Neutral
- The AC gate is enforced in three places: `ready-room.prompt.md` (STEP 5B), `copilot-instructions.md` (PHASE 1 non-negotiable rules), and `picard.agent.md` (Pre-Close Crew Validation step 5)

---

## References

- Implementation: `knowledge_base/documents/spec-driven-development.md`
- Template: `knowledge_base/missions/acceptance-criteria-template.md`
- Filed ACs: `knowledge_base/missions/acceptance-criteria/`
- Related: ADR-0001, ADR-0002, ADR-0003

---

## Version History

```
- 2026-04-12: troi — ADR proposed and accepted; spec-driven-development infrastructure shipped in commit f9fa388
- 2026-04-12: picard — ADR-0004 registered (D-4 finding from sprint health diagnostic)
```
