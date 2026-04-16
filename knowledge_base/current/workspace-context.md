# Workspace Context

> **Purpose**: This is the FIRST document picard reads when starting any new mission — loaded before `session-continuity.md`. It tells every agent which repo the current mission targets and what the workspace looks like.
>
> **Owner**: picard  
> **Updated by**: picard at the start of every mission (set `current_repo`) and when workspace topology changes.

---

## Workspace Identity

| Field              | Value                  |
| ------------------ | ---------------------- |
| **Workspace Name** | _(set workspace name)_ |
| **Hub Repo**       | `team-building`        |
| **Last Updated**   | 2026-04-16             |

---

## Current Mission Context

> picard sets these fields at the start of each mission. Agents read them to scope their work, KB updates, and issue creation.

| Field            | Value                                      |
| ---------------- | ------------------------------------------ |
| **current_repo** | `knowledge-components`                     |
| **mission_slug** | `phoenix-code-summary-context-menu-style`  |
| **mission_type** | `frontend styling / Phoenix design system` |

**How to set `current_repo`**: At the start of a Ready Room, picard reads the requester's context. If invoked inside a spoke repo with a `.tng-context.md`, that repo is `current_repo`. Otherwise picard asks. Then picard updates this field before dispatching crew.

---

## Active Repos

> All repos currently active in this workspace. picard maintains this list. guinan uses it to scope cross-session pattern detection.

| Repo                   | Domain                             | Owner Agent | Status         |
| ---------------------- | ---------------------------------- | ----------- | -------------- |
| `team-building`        | Hub / Agent System                 | picard      | active — hub   |
| `alpaca_trading_bot`   | Algorithmic Trading / Momentum Bot | geordi      | active — spoke |
| `knowledge-components` | Healthcare coding application      | data        | active — spoke |

---

## Cross-Repo Dependencies (Active This Sprint)

> Only document dependencies that are actively relevant to current sprint missions. For the full dependency map, see `WORKSPACE-TOPOLOGY.md`.

| Upstream Repo   | Downstream Repo | Dependency Type | Relevant To |
| --------------- | --------------- | --------------- | ----------- |
| _(none active)_ |                 |                 |             |

---

## Workspace Notes

> Free-text field for picard — workspace-level context that doesn't fit the table format. E.g., "repo-auth is in a code freeze this sprint", "repo-ui is being retired after Sprint 4".

_(none)_

---

## Instructions for Agents

When reading this file, every agent must:

1. **Note `current_repo`** — all work, KB signals, and issue creation should be scoped to this repo.
2. **Include repo in KB signals**: `[KB-UPDATED: <doc> | repo: <current_repo> | <nature of change>]`
3. **Include repo in carry-forward items**: Every CF item in the session journal must record its source repo.
4. **If `current_repo` is blank or unclear** — stop and ask picard to set it before proceeding.

guinan additionally:

- Tags every cross-session pattern with the repos it was detected in.
- When scanning session journals, notes which repo each session was for.
- Includes repo tags in `past-lessons-learned.md` entries: `(Repo: <name>)`.
