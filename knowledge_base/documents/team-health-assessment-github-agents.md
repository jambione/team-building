# Team Health Assessment — GitHub Agents

## Purpose

Canonical summary of the latest GitHub Agents health review.

## Current Status

- Latest assessed state: **AMBER**
- Last full assessment date: **2026-04-12**
- Previous state: GREEN (2026-04-05)
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

| ID | Finding | Owner | Sprint |
|----|---------|-------|--------|
| W-1 | `security-scan.yml` does not exist — Trivy + CodeQL not running despite KB claiming complete | worf + geordi | 3 |
| G-5 | `STATUS.md` missing — `validate-agent-structure.py` fails, `agent-structure-check.yml` broken | geordi | 3 (immediate) |

### High Priority Findings

| ID | Finding | Owner | Sprint |
|----|---------|-------|--------|
| W-2 / C-1 | `deploy-staging.yml` + `deploy-production.yml` absent — zero deployment automation | geordi + crusher | 3 |
| D-1 / D-2 | ADR storage dual-mode conflict + 8 KB docs unindexed | data + picard | 3 |
| T-1 / T-2 | No test artifacts uploaded, no coverage gate in CI | troi | 3 |
| G-1 | `npm ci` redundantly executes in every CI job | geordi | 3 |

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

## Version History

- 2026-04-08: picard — Converted to canonical summary and archived long-form report.
- 2026-04-12: picard — Sprint Health Check debrief appended. Status downgraded GREEN → AMBER. Two critical findings: security-scan.yml absent, STATUS.md absent. 15 total findings logged across 5 domains.
