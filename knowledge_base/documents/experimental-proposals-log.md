# Experimental Proposals Log

**Owner**: wes
**Updated by**: wes at each Mission Close — one entry per decided proposal
**Read by**: guinan (pattern detection), picard (MDR context), wes (divergence self-check)

---

## Purpose

Cross-mission log of every `WES-PROPOSAL-<N>` submitted to the crew. This document exists for two reasons:

1. **guinan reads it** — to surface "wes tried this before and it was rejected because X" before the crew commits to a direction. The log is the institutional memory of divergent thinking. Without it, the same alternative gets proposed and rejected repeatedly without learning.

2. **wes reads it before generating proposals** — to check whether any of his current ideas have been tried already. If they have, wes either makes a stronger case (addressing the prior rejection reason) or picks a genuinely new direction.

---

## Active Proposals (awaiting decision)

| Proposal ID | Mission Slug | Title | Submitted | Model Used |
|---|---|---|---|---|
| *(none)* | | | | |

---

## Decided Proposals

| Proposal ID | Mission Slug | Title | Model | Decision | Decision Date | Rationale | What wes learned |
|---|---|---|---|---|---|---|---|
| *(none yet — log populates at first Mission Close)* | | | | | | | |

---

## Recurring Patterns (guinan-synthesized)

> *This section is written by guinan at `[GUINAN-SYNTHESIZE: <mission-slug>]` time, not by wes.*
> *guinan scans Decided Proposals above and surfaces themes — what gets approved, what gets rejected, what keeps coming up.*

*(No patterns yet — will populate after first mission featuring wes.)*

---

## How wes Updates This Log

At every Mission Close, wes writes one row per decided proposal into the **Decided Proposals** table above.

**Required fields**:
- `Proposal ID` — e.g. `claude-api-pr-review / WES-PROPOSAL-2`
- `Mission Slug` — the mission this was part of
- `Title` — short title from the proposal block
- `Model` — the Copilot model wes was running on (from `[MODEL: <model>]` tag)
- `Decision` — `WES-APPROVED` / `WES-REJECTED` / `WES-DEFERRED`
- `Decision Date` — YYYY-MM-DD
- `Rationale` — picard's stated reason for the decision (quote it exactly if possible)
- `What wes learned` — one sentence. Honest. If it was rejected for a good reason, say so.

wes emits after updating:
```
[KB-UPDATED: knowledge_base/documents/experimental-proposals-log.md | Added: <N> decided proposal(s) from <mission-slug>]
```

If no proposals were decided this mission (all still pending):
```
[KB-NO-CHANGE: knowledge_base/documents/experimental-proposals-log.md | reason: no proposals reached a decision this mission]
```

---

## How guinan Uses This Log

At `[GUINAN-SYNTHESIZE: <mission-slug>]`, guinan:

1. Scans Decided Proposals for the last 90 days
2. Identifies any proposal theme that has appeared ≥ 2 times
3. Identifies any proposal that was rejected and then re-proposed in a later mission
4. Updates the **Recurring Patterns** section above
5. Surfaces relevant patterns in the next Ready Room before wes generates proposals

---

*"The log does not lie — and neither does wes, when wes is paying attention."*
