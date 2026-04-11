# /deployment-runbook

Generate or update the step-by-step deployment runbook for staging and production.

Load personas from `.clinerules/TNG/`. Read `ci-cd-pipeline-recommendations.md` and `monitoring-observability.md` before starting.

**geordi** (lead): Read the actual deploy workflows in `.github/workflows/`, then produce a human-readable runbook covering:
- Pre-deploy checklist
- How to trigger a staging deploy
- How to promote staging → production
- How to trigger a manual production deploy via workflow_dispatch
- How to monitor a deploy in progress
- How to trigger a rollback
Update `ci-cd-pipeline-recommendations.md`. End with: `[automation-complete]`

**crusher** supports: Validate that runbook covers all reliability steps — health checks, rollback triggers, on-call escalation path. Update `monitoring-observability.md`. End with: `[reliability-assessment-complete]`

**worf** supports: Validate the runbook handles secrets correctly — no plain-text secrets, correct secret names referenced. End with: `[security-review-complete]`

picard delivers: Final runbook written to `knowledge_base/documents/deployment-runbook.md`, any gaps identified for a follow-up sprint. Close with **"Make it so!"**
