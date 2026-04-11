# Agent Runbook v2

Keep execution simple. Use this flow for every mission.

## 1) Choose Mode

- Use `picard-thinking` when decisions are ambiguous, high impact, or cross-cutting.
- Use `picard-fast` when the path is already decided and low risk.
- Use domain specialists only for domain work.

## 2) Decision Gate

- For complex tasks, produce a decision record before implementation.
- No implementation before decision lock on high-risk work.

## 3) Execute

- Delegate only to agents listed in `TEAM-TOPOLOGY.md`.
- Keep handoffs explicit and one-directional per step.
- Keep updates short, concrete, and action-oriented.

## 4) Verify

- Validate changes with tests, lint, or workflow checks.
- Run structure validation before merging.

## 5) Capture Learning

- Update only the relevant knowledge base document.
- Avoid broad documentation edits unless a process changed.

## Multi-Repo Missions

When the workspace contains multiple repos, follow this additional flow before step 1:

### Step 0: Workspace Orientation

```
0a. Read knowledge_base/current/workspace-context.md
0b. Determine current_repo (see multi-repo-conventions.md for the decision order)
0c. If spoke repo: read its .tng-context.md for domain context and dependency map
0d. Set current_repo in workspace-context.md
0e. Announce: "picard has identified the mission target: <current_repo>."
```

### Single-Repo Mission (most common)

Proceed with the normal flow. Include `Repo: <current_repo>` in the session journal metadata.

### Cross-Repo Mission (rare — loosely coupled workspace)

When a mission genuinely touches two repos:

1. Open **separate Ready Rooms and MDRs** — one per repo. Never combine into one MDR.
2. riker sequences waves: Wave 1 = upstream repo tasks; Wave 2 = downstream repo tasks (gated on Wave 1 picard ACK).
3. Issue creation: include `Target-Repo: <owner>/<repo>` in each MDR signal to route issues correctly.
4. Document the dependency in each session journal's `Cross-Repo Dependencies` field.
5. Add a row to `sprint-state.md` Cross-Repo Carry-Forwards if any items span sprints.

### Onboarding a New Spoke Repo

1. Add a row to `WORKSPACE-TOPOLOGY.md`.
2. Copy `.tng-context.md` template to the spoke repo's root and fill it out.
3. Add the repo to `knowledge_base/current/workspace-context.md` `Active Repos` table.
4. Update `sprint-state.md` `Active Repos This Sprint` field.
5. Trigger: `[GUINAN-SYNTHESIZE: workspace-onboarding-<repo-name>]` so guinan indexes the new context.

## Minimal Team Standards

- Prefer minimal prompts over verbose persona text.
- Keep mandatory pre-reads for complex tasks only.
- One source of truth for topology (`TEAM-TOPOLOGY.md`) and current state (`STATUS.md`).
- One source of truth for workspace repos: `WORKSPACE-TOPOLOGY.md`.
