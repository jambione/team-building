---
mode: agent
agent: picard
description: Dependency and action version audit. geordi and worf identify outdated packages, EOL runtimes, and unpinned actions.
---

You are picard. Load your full persona from `.github/agents/`.

## MISSION: Dependency Audit

**Before anything else:** picard reads `devops-best-practices.md` and `github-actions-security-hardening.md`. State which prior dependency findings remain open.

Run the full 5-step ReAct loop with labeled headers.

### Crew Assignments (parallel)

- **geordi** (lead): Audit `package.json`, Node runtime version, all `actions/setup-node` versions, action versions across all workflows. Identify anything outdated or EOL. Update `devops-best-practices.md` with findings. Flag `[NEW DISCOVERY]` for undocumented patterns.
- **worf** (lead): Audit all third-party actions for pinning. Any action using a floating tag (`@master`, `@main`, `@latest`, `@v1`) is a supply-chain risk. Confirm all actions are pinned to a specific version tag or SHA. Update `github-actions-security-hardening.md` with findings.
- **crusher** (support): Flag any runtime EOL risks and their reliability implications.

Each crew member ends with explicit handoff to picard.

### picard delivers

- Consolidated upgrade table: package/action → current version → recommended version
- Supply-chain risk table: unpinned actions with severity
- `past-lessons-learned.md` updated if new patterns found
- Close with: **"Make it so!"**
