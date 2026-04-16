# Multi-Repo Conventions

**Owner**: picard | **Last Updated**: 2026-04-11

---

## Purpose

This document defines how the TNG agent team operates across a multi-repo workspace. The team follows a **hub model**: all agents, the knowledge base, mission history, and session journals live in `team-building` (the hub). Spoke repos are the actual services being worked on. They declare themselves with a `.tng-context.md` file; they do not contain agents or a KB.

Because repos in this workspace are **loosely coupled**, most missions are single-repo. Cross-repo coordination is the exception, not the rule.

---

## Mission Start Protocol (Multi-Repo)

At the start of every Ready Room, picard executes the workspace orientation sequence **before** any crew dispatch:

```
1. Read `knowledge_base/current/workspace-context.md`   ← step 0
2. Read `knowledge_base/current/session-continuity.md`  ← step 1 (as before)
3. Determine `current_repo`:
   a. If user/requester specified a repo — use it.
   b. If agent is invoked inside a spoke repo with `.tng-context.md` — read that file, use its `repo_name`.
   c. If ambiguous — ask before proceeding. Never assume.
4. Set `current_repo` in `knowledge_base/current/workspace-context.md`.
5. Announce: "picard has identified the mission target: `<current_repo>`."
6. Continue with normal Ready Room flow.
```

---

## KB Signal Format (Repo-Scoped)

When an agent emits a KB update or no-change signal, it must include the `repo:` field:

```
[KB-UPDATED: knowledge_base/documents/<doc>.md | repo: <current_repo> | <nature of change>]
[KB-NO-CHANGE: knowledge_base/documents/<doc>.md | repo: <current_repo> | reason: <brief>]
```

This allows guinan to filter lessons learned by repo when surfacing historical context.

---

## Session Journal: Repo Fields

Every session journal (copied from `session-template.md`) must populate these fields at the top of **Session Metadata**:

| Field                       | Value                                                                                           |
| --------------------------- | ----------------------------------------------------------------------------------------------- |
| **Repo**                    | _(which spoke repo this mission targets — set by picard at start)_                              |
| **Affected Repos**          | _(comma-separated list if mission touches multiple repos; usually same as Repo)_                |
| **Cross-Repo Dependencies** | _(describe any dependencies on other repos relevant to this mission; "none" if not applicable)_ |

Decisions that apply only to one repo go in the **Decisions Made** table with a `[repo-scoped]` tag in the Rationale column.

---

## Mission Index: Repo Column

`knowledge_base/missions/mission-index.md` includes a `Repo(s)` column. picard fills this when filing the mission log:

```
| Date | Slug | Mission | Sprint | Repo(s) | Status | Crew | P1s | Open Items | Log |
```

For single-repo missions, `Repo(s)` is one value (e.g., `service-api`). For cross-repo missions, comma-separate them.

---

## Issue Creation: Target-Repo

When picard emits `[MDR-ISSUED]`, it may optionally include `Target-Repo:` to route the auto-created GitHub Issue to the correct spoke repo (not always the hub):

```
[MDR-ISSUED: <mission-slug>] Priority: <P0|P1|P2|P3>
Mission: <one-line description>
Target-Repo: <owner>/<repo>
```

If `Target-Repo:` is absent, the issue is created in `team-building` (the hub). For spoke-repo missions, always specify `Target-Repo:`.

---

## Mission Branch Convention

Every mission that touches code or infrastructure runs on a dedicated branch in `current_repo`. Branch naming is deterministic — always `mission/<mission-slug>`.

**riker creates the branch** as the first act after `[READY-ROOM-CLOSED]`, before any wave planning:

```bash
git checkout main && git pull origin main
git checkout -b mission/<mission-slug>
```

**geordi opens the PR** after Track C PASS, targeting the repo's base branch (`main` or `develop`).

**Full protocol**: see `PLAYBOOK.md` — Mission Branch Protocol.

**Branch lifecycle summary**:

| Event                 | Branch                                                   |
| --------------------- | -------------------------------------------------------- |
| `[READY-ROOM-CLOSED]` | riker creates `mission/<mission-slug>` on `current_repo` |
| Track C PASS + Go     | geordi opens PR                                          |
| `[MISSION-PAUSED]`    | Preserved, no PR                                         |
| `[MISSION-ABORTED]`   | Preserved for reference                                  |
| PR merged             | Complete — repo policy governs deletion                  |

---

## The `.tng-context.md` File (Spoke Repos)

Every spoke repo in the workspace places a `.tng-context.md` in its root. This file tells TNG agents who this repo is, what it does, and what it depends on. picard reads it during mission orientation (step 3c above).

See the `.tng-context.md` template at the root of `team-building` for the full format.

Minimum required fields:

- `repo_name` — matches the entry in `WORKSPACE-TOPOLOGY.md`
- `service_domain` — what this repo does in one phrase
- `owner_agent` — the TNG agent responsible for this repo's domain
- `depends_on` — comma-separated list of repos this one depends on (or "none")

---

## Cross-Repo Missions (Rare Case)

Because repos are loosely coupled, true cross-repo missions are uncommon. When one does occur:

**Rule: One MDR per repo.**

picard opens sequential Mission Decision Records — one per affected repo — never a combined MDR. This keeps KB updates, issue creation, and session journals cleanly scoped.

**Execution sequencing (riker):**

- If repo-A changes must precede repo-B changes, riker structures waves accordingly:
  - Wave 1: repo-A tasks (deploy, merge, validate)
  - Wave 2: repo-B tasks — gated on Wave 1 ACK from picard
- Document the dependency in the session journal's `Cross-Repo Dependencies` field.

**When NOT to use cross-repo missions:**

- If the only "cross-repo" concern is an API contract change — raise it as a `[NEW DISCOVERY]` in the primary repo's mission and create a follow-up carry-forward item for the dependent repo.
- If repos share only configuration or documentation — handle in separate, independent missions.

---

## guinan: Workspace-Aware Pattern Detection

guinan scans mission journals and carry-forwards across all repos. When detecting cross-session patterns:

- Tag each pattern with source repo: `Pattern detected in: <repo-A>, <repo-B>` (or `team-wide`)
- When a pattern is **repo-specific** (e.g., geordi's CI cache misses always happen in repo-ui), note the repo in `past-lessons-learned.md`
- When a pattern is **cross-repo** (e.g., auth failures cascade from service-auth to service-api), flag it as a workspace-level risk

---

## Repo Discovery Protocol

Each spoke repo accumulates a **living discovery document** at `knowledge_base/documents/repo-discoveries/<repo>.md`. These capture everything the crew learns about a repo through missions — feature locations, architecture patterns, build/test commands, integration points, and gotchas.

**data owns all repo discovery documents.** Other agents contribute findings via `[NEW DISCOVERY: repo:<current_repo>]` tags; data incorporates them.

### When to Create

- **New repo enters workspace**: guinan checks for the doc during Ready Room context-retrieval. If missing, guinan flags `[NEW DISCOVERY]`. data bootstraps a skeleton from available sources (`.tng-context.md`, `.github/copilot-instructions.md`, or crew exploration).
- **Two-pass approach**: data creates a skeleton during the Ready Room (so analysts have a shared reference), then enriches it at mission close with everything learned during execution.

### When to Update

- **Every mission that touches the repo**: data updates the Feature Map and Mission Discovery Log at minimum.
- **Significant architectural findings**: New patterns, dependency chains, integration points, or gotchas.

### Relationship to `.tng-context.md`

- `.tng-context.md` lives in the **spoke repo** and declares identity, stack, and dependencies. It is the initial seed.
- The repo discovery doc lives in the **hub** (`team-building`) and is the living, growing version enriched by every mission.
- When a new repo has `.tng-context.md`, data reads it to populate the initial discovery doc. After that, the discovery doc is the authoritative reference.

### Template

See `knowledge_base/documents/repo-discoveries/_template.md` for the standard 7-section format (Overview, Feature Map, Architecture Discoveries, Integration Points, Build & Test, Gotchas, Mission Discovery Log).

---

## Fluid Workspace Protocol

The workspace is dynamic — repos can appear or disappear at any time. The team must handle this without breaking in-flight missions.

### When a new repo appears

1. If it has `.tng-context.md` → **self-declaring**. picard reads it, registers it in `WORKSPACE-TOPOLOGY.md` and `workspace-context.md`, and emits `[GUINAN-SYNTHESIZE: workspace-onboarding-<repo>]`.
2. If it has **no** `.tng-context.md` → **unregistered**. picard asks the user to confirm before registering. Agents do not assume context for unknown repos.
3. No manual admin steps required for the common case — `.tng-context.md` presence is the trigger.

### When a repo disappears

1. picard marks it `status: removed` in `WORKSPACE-TOPOLOGY.md` (never deletes the row — history stays).
2. Open carry-forwards from that repo are marked `[REPO-REMOVED]` and picard disposes them (cancel / migrate / park).
3. Active missions targeting the repo are closed as `cancelled` with a note.
4. Historical context (past missions, session journals) referencing the repo is preserved — guinan still reads it.
5. **Graceful rule**: any agent that encounters a `removed` repo in historical context skips it silently without erroring.

### Defensive agent behaviour

- Agents should never hardcode a repo name. Always read `current_repo` from `workspace-context.md`.
- If `current_repo` does not appear in `WORKSPACE-TOPOLOGY.md`'s active repos, picard raises `[EXTERNAL-EVENT: unregistered-repo | picard | <repo> not in workspace topology | severity: informational]` and registers it before proceeding.
- `Target-Repo:` in MDR signals is validated: if the target repo is not in the active list, geordi logs a warning and falls back to the hub repo.

---

## Version History

```
2026-04-11: picard — Created. Hub model + loosely coupled repos. Covers orientation protocol, KB signal format, repo fields, issue targeting, .tng-context.md spec, cross-repo mission rules, guinan workspace-awareness.
2026-04-16: data — Added Repo Discovery Protocol section (per-repo living documents for feature maps and architecture knowledge).
```
