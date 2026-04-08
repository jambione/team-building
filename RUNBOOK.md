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

## Minimal Team Standards

- Prefer minimal prompts over verbose persona text.
- Keep mandatory pre-reads for complex tasks only.
- One source of truth for topology (`TEAM-TOPOLOGY.md`) and current state (`STATUS.md`).
