# Mission Debrief — [YYYY-MM-DD] [mission-slug]

> **Instructions**: picard fills this at mission close, after all crew KB updates are confirmed.
> File alongside the session journal: `YYYY-MM-DD-HH-<mission-slug>-debrief.md`
> guinan reads this as part of cross-session continuity.

---

## Debrief Metadata

| Field               | Value                                                          |
| ------------------- | -------------------------------------------------------------- |
| **Mission**         | _One-line description_                                         |
| **Date**            | YYYY-MM-DD                                                     |
| **Session Journal** | `knowledge_base/sessions/YYYY-MM-DD-HH-<mission-slug>.md`      |
| **MDR**             | `[READY-ROOM-CLOSED: <mission-slug>]` — link to MDR in journal |
| **Mission Status**  | success / partial / blocked / cancelled                        |
| **Debrief Author**  | picard                                                         |

---

## Mission Objective vs Outcome

|               | Detail                                   |
| ------------- | ---------------------------------------- |
| **Objective** | _What the mission set out to accomplish_ |
| **Outcome**   | _What was actually accomplished_         |
| **Delta**     | _What was not accomplished and why_      |

---

## Crew Performance Summary

> **Scoring guide — Contribution Quality (1–5)**:
> 5 = decisive contribution that changed the mission outcome; 4 = substantive, domain-specific value; 3 = present and correct, no surprises; 2 = contributed but findings were shallow or late; 1 = invoked but no meaningful output.
> Score only agents that were active this mission. Leave inactive agents blank.

| Agent           | Contribution Quality (1–5) | PRIORITY Items Raised | Conflicts Raised | Conflicts Resolved | KB Updated | New Discoveries | Notes |
| --------------- | -------------------------- | --------------------- | ---------------- | ------------------ | ---------- | --------------- | ----- |
| picard          |                            | —                     |                  |                    |            |                 |       |
| picard-thinking |                            | —                     | —                | —                  |            |                 |       |
| data            |                            |                       |                  | —                  |            |                 |       |
| riker           |                            | —                     | —                | —                  |            |                 |       |
| geordi          |                            |                       | —                | —                  |            |                 |       |
| worf            |                            |                       |                  | —                  |            |                 |       |
| troi            |                            |                       | —                | —                  |            |                 |       |
| crusher         |                            |                       | —                | —                  |            |                 |       |
| barclay         |                            |                       | —                | —                  |            |                 |       |
| guinan          |                            | —                     | —                | —                  |            |                 |       |
| obrien          |                            |                       | —                | —                  |            |                 |       |
| wes             |                            | —                     | —                | —                  |            |                 |       |

---

## KB Documents Updated This Mission

_Every KB update made. picard verified these before closing._

| Document | Updated By | Nature of Change |
| -------- | ---------- | ---------------- |
|          |            |                  |

---

## Repo Knowledge Captured

_Repo-specific knowledge captured in `knowledge_base/documents/repo-discoveries/<repo>.md`. data is responsible for this update._

| Repo | Feature Area | What Was Learned | Updated By |
| ---- | ------------ | ---------------- | ---------- |
|      |              |                  | data       |

---

## PRIORITY Items — Resolution Summary

| ID  | Severity | Raised By | Summary | Resolution                          | Resolved In |
| --- | -------- | --------- | ------- | ----------------------------------- | ----------- |
|     | P1/P2/P3 |           |         | resolved / deferred / accepted-risk |             |

---

## WES Proposals — Disposition

| Proposal       | Decision                       | Rationale | Implemented By |
| -------------- | ------------------------------ | --------- | -------------- |
| WES-PROPOSAL-N | approved / rejected / deferred |           |                |

---

## Conflicts — Resolution Summary

| Conflict ID | Agents | Topic | Decision | Logged In Performance Log |
| ----------- | ------ | ----- | -------- | ------------------------- |
| —           | —      | None  | —        | —                         |

---

## Decisions Made (Candidates for ADRs)

_Significant decisions that may warrant a formal ADR. picard flags these for data._

| #   | Decision | ADR Needed?        | Owner |
| --- | -------- | ------------------ | ----- |
| 1   |          | yes / no / pending |       |

---

## Lessons Learned

_Cross-cutting lessons that should be added to `past-lessons-learned.md`. guinan will incorporate these._

| #   | Lesson | Category                   | Applies To             |
| --- | ------ | -------------------------- | ---------------------- |
| 1   |        | process / technical / team | all / <specific agent> |

---

## Open Items Carried Forward

_Items not resolved this mission. Each has an owner and target sprint._

| #   | Item | Owner | Target Sprint | Priority |
| --- | ---- | ----- | ------------- | -------- |
| 1   |      |       |               | P1/P2/P3 |

---

## Next Mission Recommendations

_picard's recommendations for what the team should tackle next, in priority order._

1.
2.
3.

---

## Ready Room Assessment

_Was the Ready Room protocol followed? Did it surface what it needed to?_

| Question                                          | Answer             |
| ------------------------------------------------- | ------------------ |
| Ready Room opened before execution?               | yes / no / partial |
| All P1 items resolved before [READY-ROOM-CLOSED]? | yes / no — reason: |
| MDR completed before riker engaged?               | yes / no           |
| picard-thinking used appropriately?               | yes / no — reason: |
| picard-fast used appropriately?                   | yes / no — reason: |
| Anything the Ready Room missed?                   |                    |

---

## Debrief Close

- [ ] Session journal marked `status: closed`
- [ ] All KB updates confirmed from crew — every `[KB-UPDATED]` signal verified for specific content (not just signal presence)
- [ ] Lessons learned added to `past-lessons-learned.md` (guinan's domain — verify guinan emitted `[KB-UPDATED]` with content)
- [ ] `agent-performance-log.md` updated — guinan's KB update count must be non-zero if any lessons were found
- [ ] Mission log filed at `knowledge_base/missions/YYYY-MM-DD-<mission-slug>.md` — includes Lessons Learned table and KB Documents Updated table
- [ ] Mission index updated at `knowledge_base/missions/mission-index.md`
- [ ] `[LEARNING-LOOP-VERIFIED: <mission-slug>]` emitted by picard
- [ ] `[GUINAN-SYNTHESIZE: <mission-slug>]` triggered — guinan updates `knowledge_base/current/session-continuity.md`
- [ ] guinan `[KB-UPDATED: knowledge_base/current/session-continuity.md | ...]` signal received
- [ ] ADR candidates handed to data for Sprint N

**Debrief Status**: complete

_"Make it so."_ — picard
