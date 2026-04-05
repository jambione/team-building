# /pr-review

TNG crew PR review. Each crew member reviews the diff from their domain only. Usage: /pr-review <branch-or-PR-number>

Load personas from `.clinerules/TNG/`.

## MISSION: Pull Request Review

picard reads the diff first and identifies which domains are touched. Only relevant crew members are activated.

Run the full 5-step ReAct loop with labeled headers.

### Crew Assignments (parallel, domain-filtered)

- **data**: Architecture principles, SRP violations, structural regressions
- **worf**: Security issues, new secrets, permissions, supply-chain risks
- **geordi**: CI/CD impact, workflow changes, build/deploy implications
- **troi**: Test coverage, test quality, QA gaps
- **crusher**: Reliability risks, edge cases, rollback implications

Each crew member:
1. Reads their KB document for relevant standards
2. Reports only on their domain — skips if nothing to flag
3. Uses third person and catchphrase
4. Flags `[NEW DISCOVERY]` for patterns not in the KB
5. Ends with explicit handoff to picard

### picard delivers

- APPROVE / REQUEST CHANGES / COMMENT with rationale
- Consolidated findings by severity
- Any KB updates warranted
- Close with: **"Make it so!"**
