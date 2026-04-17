# Team Health Assessment — GitHub Agents

## Purpose

Canonical summary of the latest GitHub Agents health review.

## Current Status

- Latest assessed state: **AMBER** (path to GREEN clear — 2 High items remain)
- Last full assessment date: **2026-04-12** (second pass)
- Previous state: AMBER (2026-04-12 first pass)
- Scope: CI/CD, security, testing, reliability, architecture

## Active Guidance

- Treat this file as the canonical status summary.
- For historical long-form detail, see:
  `knowledge_base/archive/team-health-assessment-github-agents-2026-04-05.md`.

## Follow-up

- Continue tracking new findings in domain KB docs.
- Use `agent-performance-log.md` for sprint-level team health signals.

---

## Sprint Health Check Debrief — 2026-04-12

**Crew**: picard (orchestrator), geordi, worf, troi, crusher, data  
**Overall Rating**: **AMBER** (downgraded from GREEN)  
**Trigger for downgrade**: Two critical findings — `security-scan.yml` absent (zero security scanning running) and `STATUS.md` absent (CI gate broken on every push).

### Critical Findings

| ID  | Finding                                                                                       | Owner         | Sprint        |
| --- | --------------------------------------------------------------------------------------------- | ------------- | ------------- |
| W-1 | `security-scan.yml` does not exist — Trivy + CodeQL not running despite KB claiming complete  | worf + geordi | 3             |
| G-5 | `STATUS.md` missing — `validate-agent-structure.py` fails, `agent-structure-check.yml` broken | geordi        | 3 (immediate) |

### High Priority Findings

| ID        | Finding                                                                            | Owner            | Sprint |
| --------- | ---------------------------------------------------------------------------------- | ---------------- | ------ |
| W-2 / C-1 | `deploy-staging.yml` + `deploy-production.yml` absent — zero deployment automation | geordi + crusher | 3      |
| D-1 / D-2 | ADR storage dual-mode conflict + 8 KB docs unindexed                               | data + picard    | 3      |
| T-1 / T-2 | No test artifacts uploaded, no coverage gate in CI                                 | troi             | 3      |
| G-1       | `npm ci` redundantly executes in every CI job                                      | geordi           | 3      |

### Cross-Cutting Themes

1. **KB-vs-Reality Drift**: Multiple KB documents assert implementation of files that do not exist. Verification criteria must include file paths, not just dates.
2. **CI produces motion, not signal**: Pipeline runs but test artifacts, coverage gates, and lint parallelism are absent.
3. **Deployment capability is zero**: No workflow exists to deploy, roll back, or emit telemetry for any spoke-repo service.

### Path to GREEN

1. Create `STATUS.md` (unblocks CI gate — immediate)
2. Create `security-scan.yml` with Trivy + CodeQL
3. Create deployment workflow scaffolding (staging first)
4. Resolve ADR storage model; index 8 unindexed KB docs
5. Add test artifact upload + coverage gate to `ci.yml`

---

---

## Sprint Health Check Debrief — 2026-04-12 (Second Pass)

**Crew**: picard (orchestrator), geordi, worf, troi, crusher, data  
**Overall Rating**: **AMBER** (holding; 2 High items block GREEN)  
**Progress since first pass**: All 15 prior findings resolved or in-flight. New pass identified 12 findings — predominantly KB drift corrections and two genuine gaps (Dependabot, coverage gate).

### Resolved Since First Pass

| Prior ID    | Finding                               | Resolution                                                                       |
| ----------- | ------------------------------------- | -------------------------------------------------------------------------------- |
| W-1         | `security-scan.yml` absent            | RESOLVED — created with CodeQL + Trivy                                           |
| G-5         | `STATUS.md` absent                    | RESOLVED — incoming commit f9fa388                                               |
| W-2/C-1     | Deploy workflows absent               | RESOLVED — staging + production created                                          |
| D-1         | ADR dual-mode storage                 | RESOLVED — 4 separate ADR files, index-only architecture-decision-records.md     |
| W-3         | JSON injection in Teams notifications | RESOLVED — jq-safe payloads across all workflows                                 |
| NEW-1/2/3/4 | AC gate gaps                          | RESOLVED — STEP 5B in copilot-instructions.md, directory, indexed, MDR checklist |

### New Findings — Second Pass

| ID      | Finding                                                                                    | Owner   | Sprint    | Severity |
| ------- | ------------------------------------------------------------------------------------------ | ------- | --------- | -------- |
| G-NEW-3 | No Dependabot config — action version pins go stale silently                               | geordi  | 3         | HIGH     |
| T-NEW-1 | No coverage gate in CI (TD-004 past-due from Sprint 2)                                     | troi    | 2         | HIGH     |
| W-NEW-1 | security-hardening.md KB stale — showing resolved items as open                            | worf    | IMMEDIATE | MEDIUM   |
| C-NEW-1 | monitoring-observability.md stale — showing resolved telemetry gap as open                 | crusher | IMMEDIATE | MEDIUM   |
| G-NEW-1 | kb-staleness-check.yml missing timeout-minutes                                             | geordi  | 3         | MEDIUM   |
| G-NEW-2 | deploy-staging.yml rollback notification missing actor field                               | geordi  | 3         | MEDIUM   |
| W-NEW-3 | Production environment protection gate not configured in GitHub Settings                   | picard  | 3         | MEDIUM   |
| T-NEW-2 | No test result artifact uploads from CI (TD-005)                                           | troi    | 3         | MEDIUM   |
| D-NEW-1 | architecture-principles.md stale "As of" header date                                       | data    | IMMEDIATE | LOW      |
| D-NEW-2 | validate-workspace.py false-positive: pending backlog backtick entries satisfy index check | data    | 3         | LOW      |
| D-NEW-3 | adr-workflow.yml ADR number generation uses file count, not max number                     | data    | 3         | LOW      |

### Fixes Applied This Pass

- `github-actions-security-hardening.md`: updated to reflect all three workflows created; permissions table corrected for all 7 workflows
- `monitoring-observability.md`: deployment telemetry gap closed; duplicate section 7 fixed; staging rollback actor gap noted
- `architecture-principles.md`: "As of" date updated to 2026-04-12
- `devops-best-practices.md`: Dependabot section added
- `best-practices.md`: coverage gate urgency noted with Sprint 2 deadline
- `.github/dependabot.yml`: created — closes TD-003 (High, past-due)
- `kb-staleness-check.yml`: `timeout-minutes: 10` added
- `deploy-staging.yml`: rollback notification now includes `actor` field
- `sprint-state.md`: tech debt snapshot corrected (TD-001 was resolved; active High/Medium items shown)
- `index.md`: `database-migration-strategies.md` moved from Pending backlog to Observability table; Pending backlog cleared

### Path to GREEN

1. **Add coverage gate to ci.yml** — `pytest --cov --cov-fail-under=70` (TD-004, High, Sprint 2 deadline 2026-04-19)
2. **Configure GitHub Settings environment protection** — production environment, required reviewers (manual step, picard)
3. **Track promotion workflow first run** — validate `.github/workflows/promote-main-to-production.yml` opens/refreshes PRs as expected on next `main` push or manual dispatch

## Version History

- 2026-04-08: picard — Converted to canonical summary and archived long-form report.
- 2026-04-12: picard — Sprint Health Check debrief appended (first pass). Status downgraded GREEN → AMBER. Two critical findings: security-scan.yml absent, STATUS.md absent. 15 total findings logged across 5 domains.
- 2026-04-12: picard — Sprint Health Check debrief appended (second pass). AMBER holding. 11 new findings, predominantly KB drift. Dependabot created, 9 KB/workflow fixes applied. 2 High items remain.
- 2026-04-17: picard — TD-008 closed via new promotion workflow; Path to GREEN updated to production-gate + promotion-run verification.
