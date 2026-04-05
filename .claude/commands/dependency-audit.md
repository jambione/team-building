# /dependency-audit

Audit all dependencies and action versions. geordi and worf lead. Identifies outdated packages, EOL runtimes, and unpinned actions.

Load personas from `.clinerules/TNG/`. Read `devops-best-practices.md` and `github-actions-security-hardening.md` before starting.

## MISSION: Dependency Audit

Run the full 5-step ReAct loop with labeled headers. In the **Reason** step, state which prior dependency findings remain open.

### Crew Assignments (parallel)

- **geordi** (lead): Audit `package.json`, Node runtime, all action versions. Update `devops-best-practices.md`. Flag `[NEW DISCOVERY]`. End with: `geordi returns control to picard. [automation-complete]`
- **worf** (lead): Audit all third-party actions for floating tags (`@master`, `@main`, `@latest`, `@v1`). Every unpinned action is a supply-chain risk. Update `github-actions-security-hardening.md`. End with: `worf returns control to picard. [security-review-complete]`
- **crusher** (support): Flag runtime EOL risks and reliability implications.

### picard delivers

- Upgrade table: current → recommended for all outdated items
- Supply-chain risk table: unpinned actions with severity
- `past-lessons-learned.md` updated if new patterns found
- Close with: **"Make it so!"**
