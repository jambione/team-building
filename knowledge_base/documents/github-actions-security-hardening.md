# GitHub Actions Security Hardening Checklist

## Current State

**As of**: 2026-04-12  
**Health**: AMBER  
**Top active item**: Environment protection rules — manual GitHub Settings step for production environment reviewers still outstanding. All workflows now created and correctly configured.

---

## Critical Items (Must-Have)

- [x] **Least-Privilege Permissions**: `permissions:` block added to all workflows (2026-04-05)
- [ ] **Environment Protection Rules**: Require 2+ PR reviewers for production deployments (GitHub Settings → Environments → production → Required reviewers — manual step not yet completed)
- [x] **Dependency Scanning**: Trivy running in `security-scan.yml` — created 2026-04-12 (Trivy misconfig + secret scan, SARIF upload to Security tab)
- [x] **CodeQL Security Analysis**: CodeQL Python analysis running in `security-scan.yml` — created 2026-04-12 (scripts/ and tests/ scoped)

### Permissions Model Reference (verified 2026-04-12)

| Workflow                       | permissions                                                                      | Notes                                                                  |
| ------------------------------ | -------------------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| ci.yml                         | contents: read                                                                   | Minimal scope — validates Python only, no PR/check writes needed       |
| security-scan.yml              | contents: read, actions: read, security-events: write                            | security-events: write required for SARIF upload                       |
| deploy-staging.yml             | contents: read, actions: read, deployments: write, pages: write, id-token: write | pages + id-token required for OIDC-based Pages deploy                  |
| deploy-production.yml          | contents: read, actions: read, deployments: write, pages: write, id-token: write | Same as staging; environment gate adds approval layer                  |
| promote-main-to-production.yml | contents: read, pull-requests: write                                             | Opens/refreshes PR from `main` to `production` for auditable promotion |
| kb-staleness-check.yml         | contents: read, issues: write                                                    | issues: write for opening staleness tracking issues                    |
| adr-workflow.yml               | contents: write, pull-requests: write                                            | Wide but necessary — creates branches and PRs for ADR review           |
| mdr-to-issue.yml               | contents: read, issues: write                                                    | issues: write for creating MDR tracking issues                         |

### Critical Pattern: Rollback Jobs Require Full Git History

Any rollback job using `git rev-parse HEAD^1` MUST set `fetch-depth: 0` on `actions/checkout`. The default
shallow clone does not include parent commits. Failure to set this causes rollback to fail exactly when it
is needed most.

### Critical Finding: KB-vs-Reality Drift (2026-04-12)

> **KB-vs-Reality Drift Pattern**: Security checklist items marked `[x]` with implementation dates are assumptions, not verified states, unless the workflow file is confirmed to exist. Any checklist item that references a specific workflow file must include the file path as a verification criterion. If the referenced file does not exist, the item must be re-opened regardless of the recorded implementation date.
>
> **Current drift detected (2026-04-12)**: `security-scan.yml` is marked as implemented but does not exist in `.github/workflows/`. `deploy-staging.yml` and `deploy-production.yml` are referenced in the permissions table but also do not exist. These items are re-opened below.

---

## Compliance Requirements

| Standard        | Requirement                                  | Status          |
| --------------- | -------------------------------------------- | --------------- |
| SOC 2/ISO 27001 | Access controls, workflow retention policies | ❌ Incomplete   |
| PCI-DSS/HIPAA   | Artifact encryption verification             | ⚠️ Needs review |

## Sprint 3 Status — Completed 2026-04-12

1. **[RESOLVED] `security-scan.yml` created** — Trivy (misconfig + secret, SARIF) + CodeQL (Python, scripts/ + tests/). Owner: worf + geordi.
2. **[RESOLVED] `deploy-staging.yml` and `deploy-production.yml` created** — health-check polling, rollback with fetch-depth:0, structured telemetry, jq-safe Teams notifications. Owner: geordi.
3. **[RESOLVED] JSON injection fixed** in `mdr-to-issue.yml`, `deploy-staging.yml`, `deploy-production.yml`. Owner: worf.

## Open Items

1. **[MEDIUM] Add environment protection rules** — Manual GitHub Settings step (see below). Without this, `environment: production` in deploy-production.yml has no approval gate. Owner: picard. Sprint 3.
2. **[RESOLVED] Dependabot configuration** — `.github/dependabot.yml` created 2026-04-12 for `github-actions` ecosystem, weekly Monday schedule.
3. Configure artifact encryption and retention policies (carried forward).

### PROD-GATE Automation Attempt (2026-04-17)

- Attempted API-based configuration using `gh api -X PUT repos/jambione/team-building/environments/production ...`
- Result: `HTTP 403 Must have admin rights to Repository`
- Disposition: blocked by repository admin permissions; must be completed by a repo admin in GitHub Settings

### How to Configure the Production Environment Gate (PROD-GATE)

This is a one-time manual step in GitHub Settings. It cannot be automated from within the repository.

1. Go to `https://github.com/<owner>/<repo>/settings/environments`
2. Click **New environment** (or click the existing `production` environment if it was auto-created by the workflow)
3. Name it exactly `production` (must match `environment: name: production` in `deploy-production.yml`)
4. Under **Deployment protection rules**, enable **Required reviewers**
5. Add at least 1 required reviewer (e.g. `jambione`)
6. Optionally set a **Wait timer** (e.g. 5 minutes) for emergency cancellation
7. Click **Save protection rules**

**Verification**: On next `deploy-production.yml` dispatch, the `deploy` job should pause at "Waiting for review" before proceeding. Without this step, the job runs immediately with no approval gate.

---

Generated by picard orchestration on 2026-04-04  
Last updated: 2026-04-17 (worf — promotion workflow permissions reference + PROD-GATE admin blocker note)
