# Team Health Assessment — TNG Crew Evaluation
## Project: team-building | Stardate: 2026-04-05

**Orchestrator:** picard  
**Crew:** data, riker, geordi, worf, troi, crusher  
**Assessment Scope:** CI/CD pipeline health, security posture, test coverage, system reliability

---

## Executive Summary

The TNG crew conducted a full-spectrum health evaluation of the project at
`c:\Users\jonmb\Desktop\Claude\team-building`. The project possesses a well-intentioned
architectural foundation and a strong knowledge base built by the prior kirk-era crew.
However, a consistent and critical gap exists between documented best practices and
actual workflow implementation. Placeholder logic pervades the deployment, verification,
and rollback systems. Multiple high-priority security and reliability issues require
immediate remediation before this project can be considered production-ready.

**Overall Health Rating: AMBER — Structurally sound, operationally incomplete.**

---

## 1. Architecture & System Design (data)

### Findings
- Four active workflow files present: `ci.yml`, `deploy-staging.yml`, `deploy-production.yml`,
  `security-scan.yml`. Structure aligns with the single-responsibility boundary model in the
  knowledge base.
- A `ci.yml.tmp` file exists in `.github/workflows/` containing concatenated, improperly quoted
  YAML fragments. This file is inert but represents technical debt and a source of confusion.
- **Version drift detected:** Active workflows use `actions/setup-node@v3` and `NODE_VERSION: '18'`;
  the `.tmp` draft targets `@v4` and Node.js `'20'`. The knowledge base recommends a matrix across
  Node.js 16, 18, and 20 — no matrix build is implemented in any active workflow.
- No `package.json` found in the repository root; the project's actual source code is not present,
  suggesting this repository is a workflow/documentation template rather than a deployed application.

### Recommendations
- Remove `ci.yml.tmp` immediately.
- Upgrade all workflows to `actions/setup-node@v4` and `NODE_VERSION: '20'`.
- Implement matrix builds as specified in `ci-cd-pipeline-recommendations.md`.

---

## 2. Operational Readiness (riker)

### Findings
- CI pipeline job graph is well-structured: `prepare` → `build` → parallel (`test`, `lint`,
  `security-scan`) → `deploy-staging`. Dependency chain is logical.
- `deploy-staging` in `ci.yml` runs without any environment protection gate or manual approval
  on push to `main`. Any push to main triggers staging deployment automatically.
- **Critical gap:** `deploy-production.yml` triggers on pushes to a `production` branch, but no
  branch promotion workflow exists to move code from `main` to `production` in a controlled,
  gated manner. The promotion path is undefined.
- `rollback-on-failure` job in production is structurally correct (`if: failure()`) but contains
  only placeholder logic — no real rollback is executed.
- `post-deploy-verification` runs with `if: always()` — correct — but is also a placeholder.

### Recommendations
- Define and document the `main` → `production` branch promotion process.
- Add an environment protection rule to `deploy-staging` requiring at least one reviewer.
- Implement real rollback logic (e.g., previous container tag promotion or blue/green switch).
- Add real smoke tests to post-deploy verification.

---

## 3. CI/CD Engineering (geordi)

### Findings
- **Critical bug:** All jobs in `ci.yml` set `cache: 'actions/cache'` in `setup-node`. The correct
  value is `cache: 'npm'`. This means npm dependency caching is broken, causing full reinstall on
  every run. Estimated unnecessary overhead: 2-3 minutes per workflow execution.
- `npm install` is used throughout instead of `npm ci`. In CI environments, `npm ci` is required:
  it installs from lockfile exactly, is faster, and prevents dependency drift.
- The `prepare` job installs dependencies but does not share them with downstream jobs via a
  reliable cache key. Each job independently reinstalls — redundant and slow.
- No third-party action is pinned to a SHA digest hash. All use floating version tags (`@v3`,
  `@v4`), which is a supply-chain risk.
- No step-level `timeout-minutes` values are set in active workflows (only job-level in the draft).

### Recommendations
- Fix `cache: 'npm'` in all `setup-node` steps immediately.
- Replace all `npm install` with `npm ci --ignore-scripts`.
- Add step-level timeouts to all long-running steps.
- Pin third-party actions to SHA digests for supply-chain security.
- Consider uploading the `node_modules` artifact from `prepare` and restoring it in downstream jobs.

---

## 4. Security Posture (worf)

### Findings
- **Critical:** `ci.yml` and `deploy-staging.yml` have NO `permissions:` block. They execute with
  GitHub's default permissions, which grant write access to repository contents and packages.
  This is a known attack surface for supply-chain compromise.
- `deploy-production.yml` uses an `environment: production` block (implying protection rules) but
  also lacks an explicit `permissions:` block.
- **Misconfiguration detected:** `security-scan.yml` references `github/codeql-action/upload-artifact@v2`
  instead of the correct `github/codeql-action/analyze`. CodeQL analysis is non-functional as
  configured.
- `npm install --legacy-peer-deps` in the `prepare` job bypasses peer dependency conflict resolution.
  This can allow installation of packages with known vulnerabilities that would otherwise be blocked.
- No scheduled security scan is configured (e.g., weekly cron). Scans only run on push/PR.
- `security-events: write` permission is not present in any workflow — required for uploading
  SARIF results to GitHub Security tab.

### Recommendations
- Add `permissions:` blocks to ALL workflows, restricting to minimum required scope.
- Fix CodeQL action reference: `github/codeql-action/analyze@v3`.
- Remove `--legacy-peer-deps` flag; resolve peer dependency conflicts properly.
- Add a weekly scheduled security scan (`cron: '0 4 * * 1'`).
- Add `security-events: write` permission to `security-scan.yml`.
- Pin all action references to SHA digests.

---

## 5. Test Coverage & QA (troi)

### Findings
- `TESTING.md` exists but contains only Cline chat startup instructions — not a test specification,
  test plan, or coverage strategy.
- No `package.json` is present; the actual test framework, test scripts, and test files cannot be
  verified. The `npm test` command in CI would fail immediately in a real project if not configured.
- No test coverage reporting step exists in any workflow. No coverage artifact is uploaded.
- No minimum coverage threshold gate is enforced.
- No integration test, end-to-end test, contract test, or performance test configuration exists.
- The `.tmp` draft references `test-pattern: ['unit', 'integration']` — intent to separate test
  suites was planned but never promoted to active workflows.
- No test results are uploaded as workflow artifacts in the active `ci.yml` test job.

### Recommendations
- Establish a formal test strategy document in the knowledge base.
- Implement coverage reporting (e.g., `nyc`, `c8`, or Jest `--coverage`) with artifact upload.
- Define and enforce a minimum coverage threshold (recommended: 80%).
- Separate unit and integration test jobs using matrix strategy.
- Upload test results as artifacts with appropriate retention.
- Update `TESTING.md` to serve as a genuine testing guide.

---

## 6. System Reliability & Long-Term Health (crusher)

### Findings
- Knowledge base contains `incident-response-playbook.md` and `monitoring-observability.md` —
  strategically sound foundations that exist at the documentation layer.
- **All deployment verification is placeholder.** `post-deploy-verification` in production,
  `Verify deployment` in staging — both echo statements with no real health checks, no endpoint
  pings, no observability platform integration.
- `rollback-on-failure` contains only placeholder logic. In a real incident, no corrective action
  would be taken.
- No observability integration exists in any workflow (no Datadog, CloudWatch, Grafana, PagerDuty,
  or similar notification/metrics hooks).
- No retry logic on any workflow step. Transient failures will cause full pipeline failure with
  no automatic recovery attempt.
- `README.md` contains only a timestamp — no operational runbook, no architecture overview, no
  "getting started" guidance. The repository is not self-documenting.
- No `CODEOWNERS` file detected; there is no enforced review ownership for sensitive workflow files.

### Recommendations
- Implement real smoke tests in post-deploy verification (health endpoint checks, critical
  path validation).
- Implement real rollback logic (e.g., previous deployment tag promotion).
- Add observability hooks to deployment workflows (success/failure notifications via Slack/PagerDuty).
- Add `continue-on-error: false` and `retry` patterns for flaky steps.
- Create a `CODEOWNERS` file assigning workflow files to senior engineers.
- Populate `README.md` with operational guidance, architecture summary, and local dev setup.

---

## Consolidated Priority Matrix

| Priority | Finding | Owner | Action |
|----------|---------|-------|--------|
| CRITICAL | No `permissions:` blocks on `ci.yml`, `deploy-staging.yml` | worf / geordi | Add least-privilege blocks immediately |
| CRITICAL | `cache: 'actions/cache'` broken — caching non-functional | geordi | Fix to `cache: 'npm'` |
| CRITICAL | CodeQL action misconfigured — security analysis non-functional | worf | Fix to `github/codeql-action/analyze@v3` |
| HIGH | `npm install` instead of `npm ci` throughout | geordi | Replace all instances |
| HIGH | Placeholder rollback logic in production deploy | riker / crusher | Implement real rollback |
| HIGH | No test coverage reporting or enforcement | troi | Add coverage step + threshold gate |
| HIGH | `ci.yml.tmp` technical debt file present | data | Delete file |
| HIGH | `setup-node@v3` — outdated action version | data / geordi | Upgrade to `@v4` |
| HIGH | No branch promotion gate `main` → `production` | riker | Define promotion workflow |
| MEDIUM | No scheduled security scans | worf | Add weekly cron scan |
| MEDIUM | No observability hooks in deployments | crusher | Add notification/metrics steps |
| MEDIUM | No matrix builds implemented | data | Implement per knowledge base spec |
| MEDIUM | `--legacy-peer-deps` flag in prepare job | worf | Remove; resolve conflicts properly |
| MEDIUM | No step-level timeouts | geordi | Add timeouts to all long-running steps |
| LOW | `README.md` empty of operational content | crusher | Populate with runbook and overview |
| LOW | No `CODEOWNERS` file | worf | Create with workflow file assignments |
| LOW | Third-party actions not SHA-pinned | worf / geordi | Pin all to digest hashes |

---

## What Is Working Well

- Four-workflow separation of concerns is architecturally correct and matches knowledge base spec.
- Concurrency groups are correctly configured on all active workflows.
- Production deployment has `cancel-in-progress: false` — correct for production safety.
- `post-deploy-verification` uses `if: always()` — correct sentinel pattern.
- `rollback-on-failure` uses `if: failure()` — correct trigger condition.
- Knowledge base is comprehensive, well-organized, and provides a clear remediation roadmap.
- Prior crew (kirk-era) left actionable recommendations that remain valid and applicable.

---

## Knowledge Base Cross-References

The following existing documents provide remediation guidance for findings above:

- `ci-cd-pipeline-recommendations.md` — caching, matrix builds, `npm ci` usage
- `github-actions-security-hardening.md` — `permissions:` blocks, CodeQL, secret rotation
- `devops-best-practices.md` — CI/CD speed targets, Docker patterns
- `github-actions-best-practices.md` — workflow structure, secrets management
- `incident-response-playbook.md` — operational runbook for production incidents
- `monitoring-observability.md` — logging, metrics, alerting standards

---

## Version History

```
2026-04-05: picard (TNG crew) — Initial team health assessment. Full crew evaluation.
            Findings documented across CI/CD, security, testing, and reliability domains.
```

---

_Assessed by the TNG crew under Captain picard | Stardate 2026-04-05_
_data (architecture) | riker (operations) | geordi (engineering) | worf (security) | troi (QA) | crusher (reliability)_
