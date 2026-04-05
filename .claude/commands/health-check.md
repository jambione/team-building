# /health-check

Run a full TNG team sprint health check. picard orchestrates the full crew across CI/CD, security, QA, reliability, and architecture. The knowledge base is consulted before work begins and updated after.

Load each persona from `.clinerules/TNG/`. Read all `knowledge_base/documents/` before starting.

## MISSION: Sprint Health Check

Run the full 5-step ReAct loop with labeled headers. In the **Reason** step, list which KB documents were consulted and which prior findings remain open.

### Crew Assignments (run in parallel)

| Crew | Domain | KB Document to Update |
|------|--------|-----------------------|
| geordi | CI/CD pipeline — workflows, caching, action versions, build times | `devops-best-practices.md` |
| worf | Security — permissions blocks, secret exposure, dependency CVEs, SAST | `github-actions-security-hardening.md` |
| troi | QA — test coverage, test artifacts, CI test step correctness | `best-practices.md` |
| crusher | Reliability — deployment logic, rollback, health checks, runtime EOL | `monitoring-observability.md` |
| data | Architecture — structural coherence, duplication, SRP violations | `architecture-principles.md` |

### Each crew member must

1. Read their KB document before starting
2. Investigate their domain in `.github/workflows/` and the project root
3. Report in third person with their catchphrase
4. Flag undocumented findings as `[NEW DISCOVERY]` with KB document and proposed text
5. Update their KB document directly
6. End with: `[agent] returns control to picard. [trigger]`

### picard delivers

- Cross-cutting themes (findings flagged by 2+ crew members)
- Overall health rating: GREEN / AMBER / RED with justification
- Priority matrix: CRITICAL / HIGH / MEDIUM with owner and sprint
- Explicit acceptance of any open items with owner and sprint
- KB debrief appended to `team-health-assessment-github-agents.md`
- `past-lessons-learned.md` updated with cross-cutting lessons
- Close with: **"Make it so!"**
