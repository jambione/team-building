# Mission Log — [YYYY-MM-DD] [mission-slug]

> **Instructions**: picard fills this at mission close, after the session journal is marked `status: closed`.
> File as `YYYY-MM-DD-<mission-slug>.md` in `knowledge_base/missions/`.
> Add a one-line entry to `mission-index.md` after filing.
> guinan consults mission logs for cross-mission pattern detection.

---

## Captain's Log

**Stardate**: YYYY-MM-DD  
**Mission**: _One-line description_  
**Status**: success / partial / blocked / cancelled

> _picard's narrative summary of the mission — what was attempted, what was decided, what was accomplished, and what was left undone. Written in picard's voice, third person. Two to four sentences._

---

## Mission Stats

| Field                          | Value                                                                                                                               |
| ------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------- |
| **Mission Slug**               | `<mission-slug>`                                                                                                                    |
| **Session Journal**            | [`YYYY-MM-DD-HH-<mission-slug>.md`](../sessions/YYYY-MM-DD-HH-<mission-slug>.md)                                                    |
| **Mission Debrief**            | [`YYYY-MM-DD-HH-<mission-slug>-debrief.md`](../sessions/YYYY-MM-DD-HH-<mission-slug>-debrief.md)                                    |
| **Sprint**                     | Sprint N                                                                                                                            |
| **Crew Active**                | picard, data, riker, …                                                                                                              |
| **P1 Items Raised**            | N                                                                                                                                   |
| **P1 Items Resolved**          | N                                                                                                                                   |
| **Conflicts**                  | N                                                                                                                                   |
| **WES Proposals**              | N (approved / rejected / deferred)                                                                                                  |
| **KB Documents Updated**       | N                                                                                                                                   |
| **Open Items Carried Forward** | N                                                                                                                                   |
| **Execution Manifest**         | [`manifests/YYYY-MM-DD-<mission-slug>.manifest.md`](manifests/YYYY-MM-DD-<mission-slug>.manifest.md) / `—` for single-repo missions |

---

## Key Decisions

| #   | Decision | Decided By |
| --- | -------- | ---------- |
| 1   |          | picard     |

---

## PRIORITY Items — Summary

| ID   | Level    | Raised By | Resolution                          |
| ---- | -------- | --------- | ----------------------------------- |
| P-01 | P1/P2/P3 |           | resolved / deferred / accepted-risk |

---

## WES Proposals — Disposition

| Proposal       | Status                         |
| -------------- | ------------------------------ |
| WES-PROPOSAL-1 | approved / rejected / deferred |

---

## Track C Verdicts

| Reviewer | Verdict                   | Key Finding |
| -------- | ------------------------- | ----------- |
| worf     | PASS / FAIL / CONDITIONAL |             |
| troi     | PASS / FAIL / CONDITIONAL |             |
| crusher  | PASS / FAIL / CONDITIONAL |             |

---

## Outcome & Carry-Forward

**What was shipped**: _brief description_

**What was deferred**:

- Item — Owner — Target Sprint

---

## Deterministic Delivery Evidence

_Required for multi-repo missions. Optional for single-repo missions._

| Repo           | Base Ref          | Mission Branch           | Final Commit SHA                          | Checkpoint Commit(s)   | Wave            |
| -------------- | ----------------- | ------------------------ | ----------------------------------------- | ---------------------- | --------------- |
| `<owner/repo>` | `<branch-or-sha>` | `mission/<mission-slug>` | `<40-char-sha>` / `n/a` (no code changes) | `<sha1, sha2>` / `n/a` | Wave 1 / Wave 2 |

**Dependency gates**:

- `repo-B` gated on `repo-A` commit `<sha>`

---

## Lessons Learned

_Cross-cutting lessons distilled from this mission. Sourced from the debrief's Lessons Learned table. guinan incorporates these into `past-lessons-learned.md` during cross-session synthesis._

| #   | Lesson | Category                   | Applies To             |
| --- | ------ | -------------------------- | ---------------------- |
| 1   |        | process / technical / team | all / <specific agent> |

---

## KB Documents Updated

_Every KB document updated this mission. Verified by picard via [KB-UPDATED] signals before close._

| Document | Updated By | Nature of Change |
| -------- | ---------- | ---------------- |
|          |            |                  |

---

_"Make it so."_ — picard
