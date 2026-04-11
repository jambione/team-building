# Technical Debt Register

## Current State

**As of**: 2026-04-11  
**Health**: GREEN  
**Top active item**: TD-002 — Matrix testing configuration (Medium severity, geordi, Sprint 2). Previous TD-001 (ci.yml.tmp) resolved during 2026-04-11 code review mission. Net debt trend: stable; lightweight documentation enhancements queued for Sprint 3.

---

## Purpose

Centralized registry of known technical debt items across the codebase and infrastructure. Maintained by barclay. Reviewed by picard at each sprint close. Items are categorized by severity and tracked to resolution.

**Owner**: barclay  
**Review Cadence**: Every sprint  
**Last Updated**: 2026-04-11

---

## Severity Definitions

| Severity | Definition |
|----------|------------|
| **Critical** | Blocks delivery, causes production failures, or creates security exposure. Address immediately. |
| **High** | Measurably slows velocity, increases defect rate, or makes onboarding significantly harder. Address within current sprint. |
| **Medium** | Causes friction, increases cognitive load, or will compound if not addressed within 2 sprints. |
| **Low** | Cosmetic, stylistic, or aspirational. Address in cleanup sprints. |

---

## Active Debt Items

### CI/CD & Infrastructure

| ID | Item | Severity | Owner | Effort | Added | Target Sprint | Status |
|----|------|----------|-------|--------|-------|---------------|--------|
| TD-001 | `ci.yml.tmp` stray file — malformed YAML draft not deleted | Low | geordi | 5 min | 2026-04-05 | Sprint 2 | **RESOLVED 2026-04-11** |
| TD-002 | Matrix testing (Node 18/20/22 × OS) drafted in `.tmp` but not migrated to active `ci.yml` | Medium | geordi | 1 hr | 2026-04-05 | Sprint 2 | open |
| TD-003 | No Dependabot configuration — dependency updates are fully manual | High | geordi | 30 min | 2026-04-05 | Sprint 2 | open |
| TD-004 | No test coverage thresholds enforced — coverage can regress silently | High | troi | 1 hr | 2026-04-05 | Sprint 2 | open |
| TD-005 | No test result artifact uploads — CI results not persisted for analysis | Medium | troi | 30 min | 2026-04-05 | Sprint 3 | open |

### Documentation & Governance

| ID | Item | Severity | Owner | Effort | Added | Target Sprint | Status |
|----|------|----------|-------|--------|-------|---------------|--------|
| TD-006 | `TESTING.md` contains only placeholder header — no actual test strategy | Medium | troi | 2 hrs | 2026-04-05 | Sprint 2 | open |
| TD-007 | `onboarding-guide.md` listed as pending in KB index — new member onboarding undocumented | Medium | picard | 3 hrs | 2026-04-05 | Sprint 3 | open |
| TD-008 | No `main` → `production` branch promotion workflow defined | High | geordi | 2 hrs | 2026-04-05 | Sprint 2 | open |
| TD-009 | Validation script fragmentation — 3 separate tools, no unified runner | Medium | barclay | 2 hrs | 2026-04-11 | Sprint 3 | open |
| TD-010 | No unit tests for validation scripts (`kb-lint.py`, etc.) | Medium | barclay | 2 hrs | 2026-04-11 | Sprint 3 | open |

---

## Resolved Debt Items

| ID | Item | Resolved | Sprint | Resolved By |
|----|------|----------|--------|-------------|
| TD-R001 | Placeholder deployment logic (echo only) | 2026-04-05 | Sprint 1 | geordi |
| TD-R002 | Missing `permissions:` blocks on all workflows | 2026-04-05 | Sprint 1 | worf |
| TD-R003 | Node.js 18 (EOL) used across workflows | 2026-04-05 | Sprint 1 | geordi |
| TD-R004 | `npx trivy` used instead of official action | 2026-04-05 | Sprint 1 | geordi |
| TD-R005 | CodeQL sequence incorrect (autobuild before init) | 2026-04-05 | Sprint 1 | geordi |
| TD-R006 | `npm install` used instead of `npm ci --ignore-scripts` | 2026-04-05 | Sprint 1 | worf |
| TD-R007 | No health check loops in deployment workflows | 2026-04-05 | Sprint 1 | crusher |
| TD-R008 | No rollback logic in production deployment | 2026-04-05 | Sprint 1 | geordi |

---

## Velocity Impact Tracking

> barclay tracks the cumulative cost of unaddressed debt each sprint. Items not resolved within their target sprint are escalated one severity level.

| Sprint | Items Added | Items Resolved | Net Change | Escalations |
|--------|-------------|----------------|------------|-------------|
| Sprint 1 | 10 | 8 | -8 resolved | 0 |
| Sprint 2 | 2 | 1 | TD-001 resolved; TD-009/TD-010 added | 0 |

---

## Version History

```
- 2026-04-05: barclay — Initial register created from Sprint 1 health assessment findings
```
