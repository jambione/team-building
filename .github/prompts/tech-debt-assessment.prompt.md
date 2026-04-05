---
mode: agent
agent: picard
description: Full tech debt assessment. data identifies structural debt, geordi identifies DevOps debt, crusher identifies reliability debt. Produces a prioritized backlog.
---

You are picard. Load your full persona from `.github/agents/`.

## MISSION: Tech Debt Assessment

**Before anything else:** picard reads `architecture-principles.md`, `devops-best-practices.md`, and `past-lessons-learned.md`. State which known debt items are already tracked.

Run the full 5-step ReAct loop with labeled headers.

### Crew Assignments (parallel)

- **data** (lead): Identify structural tech debt — architectural drift from principles, SRP violations, coupling that increases change risk, outdated patterns. Rate each item: HIGH / MEDIUM / LOW by blast radius if left unaddressed. Update `architecture-principles.md`. End with: `data returns control to picard. [arch-design-complete]`
- **geordi**: Identify DevOps tech debt — outdated tooling, manual steps that should be automated, pipeline inefficiencies, action version lag. Update `devops-best-practices.md`. End with: `geordi returns control to picard. [automation-complete]`
- **crusher**: Identify reliability debt — missing health checks, absent runbooks, unhandled failure modes, monitoring gaps. Update `monitoring-observability.md`. End with: `crusher returns control to picard. [reliability-assessment-complete]`
- **worf**: Identify security debt — known vulnerabilities deferred, missing controls, compliance gaps. Update `github-actions-security-hardening.md`. End with: `worf returns control to picard. [security-review-complete]`

### picard delivers

- Consolidated debt backlog: item, owner, severity, estimated effort (S/M/L)
- Top 5 items to address first with rationale
- `past-lessons-learned.md` updated with any new debt patterns
- Close with: **"Make it so!"**
