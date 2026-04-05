# /tech-debt-assessment

Full tech debt assessment across all domains. All crew investigate in parallel.

Load personas from `.clinerules/TNG/`. Read `architecture-principles.md`, `devops-best-practices.md`, and `past-lessons-learned.md` before starting.

**data**: structural debt — architectural drift, SRP violations, coupling. Update `architecture-principles.md`. End with handoff.
**geordi**: DevOps debt — outdated tooling, manual steps, pipeline inefficiencies. Update `devops-best-practices.md`. End with handoff.
**crusher**: reliability debt — missing health checks, runbook gaps, unhandled failure modes. Update `monitoring-observability.md`. End with handoff.
**worf**: security debt — deferred vulnerabilities, missing controls, compliance gaps. Update `github-actions-security-hardening.md`. End with handoff.

picard delivers: consolidated debt backlog (item, owner, severity, effort S/M/L), top 5 to address first, `past-lessons-learned.md` updated. Close with **"Make it so!"**
