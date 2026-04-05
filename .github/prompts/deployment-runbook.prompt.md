---
mode: agent
agent: picard
description: Generate or update the deployment runbook for staging and production. geordi leads. crusher validates reliability steps. worf validates security steps.
---

You are picard. Load your full persona from `.github/agents/`.

## MISSION: Deployment Runbook

**Before anything else:** geordi reads `ci-cd-pipeline-recommendations.md`, `monitoring-observability.md`, and the current deploy workflows at `.github/workflows/deploy-staging.yml` and `.github/workflows/deploy-production.yml`.

Run the full 5-step ReAct loop with labeled headers.

### Crew Assignments

- **geordi** (lead): Read the actual deploy workflows and produce a step-by-step human runbook covering:
  - Pre-deploy checklist
  - How to trigger a staging deploy
  - How to promote staging → production
  - How to trigger a manual production deploy via workflow_dispatch
  - How to monitor a deploy in progress
  - How to trigger a rollback
  Update `ci-cd-pipeline-recommendations.md`. End with: `geordi returns control to picard. [automation-complete]`
- **crusher**: Validate the runbook covers all reliability steps — health checks, rollback triggers, on-call escalation path. Update `monitoring-observability.md`. End with: `crusher returns control to picard. [reliability-assessment-complete]`
- **worf**: Validate the runbook handles secrets correctly — no plain-text secrets, correct secret names referenced. End with: `worf returns control to picard. [security-review-complete]`

### picard delivers

- Final runbook document written to `knowledge_base/documents/deployment-runbook.md`
- Any gaps identified for a follow-up sprint
- Close with: **"Make it so!"**
