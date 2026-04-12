# Knowledge Base Index — IT Team Documentation Hub

## Purpose

Central navigation for all team knowledge base documents. Updated quarterly by picard.

---

## Architecture & Design

| Document                     | Description                                             | Last Updated | Owner  |
| ---------------------------- | ------------------------------------------------------- | ------------ | ------ |
| `architecture-decision-records.md` | Formal ADR index and decision rationale history            | 2026-04-05   | data   |
| `architecture-principles.md` | Foundational rules, decision framework, common patterns | 2026-04-04   | data   |
| `system-design-patterns.md`  | Reusable system design templates and implementation patterns | 2026-04-11   | data   |
| `coding-standards.md`        | Readability, naming conventions, style guidelines       | 2026-04-04   | picard |

---

## DevOps & CI/CD

| Document                               | Description                                                      | Last Updated | Owner  |
| -------------------------------------- | ---------------------------------------------------------------- | ------------ | ------ |
| `ci-cd-pipeline-recommendations.md`    | Production-grade GitHub Actions setup, caching, matrix builds    | 2026-04-04   | geordi |
| `devops-best-practices.md`             | CI/CD speed targets, Docker multi-stage builds, caching          | 2026-04-04   | geordi |
| `github-actions-best-practices.md`     | Workflow structure, secrets management, performance optimization | 2026-04-04   | geordi |
| `github-actions-security-hardening.md` | Security checklist, compliance requirements (SOC 2/ISO)          | 2026-04-04   | geordi |
| `notification-integration.md`          | Teams/Slack webhook setup, signal→channel mapping, payload formats, security requirements | 2026-04-11   | geordi |

---

## Development Practices

| Document              | Description                                     | Last Updated | Owner  |
| --------------------- | ----------------------------------------------- | ------------ | ------ |
| `best-practices.md`   | General development guidelines, QA requirements | 2026-04-04   | picard |
| `defect-management-process.md` | Defect triage workflow, severity handling, and remediation standards | 2026-04-11   | troi   |
| `onboarding-guide.md` | New team member onboarding flow and operating checklist | 2026-04-11   | picard |
| `team-conventions.md` | Orchestration rules, third-person communication | 2026-04-04   | picard |
| `team-tools-recommendations.md` | Recommended toolchain and usage patterns for team workflows | 2026-04-11   | picard |

---

## Domain-Specific Knowledge

| Document                     | Description                                       | Last Updated | Owner    |
| ---------------------------- | ------------------------------------------------- | ------------ | -------- |
| `rally-patterns.md`          | Rally story handling, acceptance criteria mapping | 2026-04-04   | kc-rally |

---

## Governance & Maintenance

| Document                       | Description                                            | Last Updated | Owner  |
| ------------------------------ | ------------------------------------------------------ | ------------ | ------ |
| `knowledge-base-governance.md` | Document ownership, review cadence, deprecation policy | 2026-04-04   | picard |
| `multi-repo-conventions.md`    | Hub model, workspace orientation protocol, repo-scoped KB signals, cross-repo mission rules | 2026-04-11 | picard |

---

## Incident Response & Operations

| Document                        | Description                                             | Last Updated | Owner  |
| ------------------------------- | ------------------------------------------------------- | ------------ | ------ |
| `incident-response-playbook.md` | Production incident procedures, severity classification | 2026-04-04   | picard |

---

## Health Assessments (NEW)

| Document                                  | Description                                                                             | Last Updated | Owner  |
| ----------------------------------------- | --------------------------------------------------------------------------------------- | ------------ | ------ |
| `team-health-assessment-clinerules.md`    | Team health assessment focused on instruction and agent-rules quality                   | 2026-04-05   | picard |
| `team-health-assessment-github-agents.md` | Full-spectrum health review: CI/CD, security, test coverage, reliability — currently GREEN (see latest entry) | 2026-04-05   | picard |

---

## Quality Gates & Spec-Driven Development

| Document                     | Description                                                                        | Last Updated | Owner |
| ---------------------------- | ---------------------------------------------------------------------------------- | ------------ | ----- |
| `spec-driven-development.md` | AC gate mechanics, Given/When/Then format, traceability, role assignments, lessons | 2026-04-12   | troi  |

---

## Technical Debt & Quality

| Document                | Description                                                         | Last Updated | Owner   |
| ----------------------- | ------------------------------------------------------------------- | ------------ | ------- |
| `tech-debt-register.md` | Debt registry by severity; velocity impact tracking; resolution log | 2026-04-05   | barclay |

---

## Observability & Operations

| Document                      | Description                                                               | Last Updated | Owner  |
| ----------------------------- | ------------------------------------------------------------------------- | ------------ | ------ |
| `monitoring-observability.md` | Logging, metrics, alerting standards, SLO definitions, observability gaps | 2026-04-05   | obrien |

---

## Agent Governance

| Document                   | Description                                                            | Last Updated | Owner  |
| -------------------------- | ---------------------------------------------------------------------- | ------------ | ------ |
| `agent-performance-log.md` | Per-agent sprint metrics; utilization signals; conflict resolution log | 2026-04-05   | picard |
| `past-lessons-learned.md`  | Cross-mission lessons and decision outcomes synthesized by guinan      | 2026-04-11   | guinan |
| `sprint-state.md`          | Current sprint goals, carry-forwards, and active mission state         | 2026-04-11   | picard |

---

## Session Continuity

| Location                                              | Description                                               | Maintained By |
| ----------------------------------------------------- | --------------------------------------------------------- | ------------- |
| `knowledge_base/sessions/`                            | Per-mission session journals for cross-session continuity | guinan        |
| `knowledge_base/sessions/session-template.md`         | Template for opening new session journals                 | picard        |
| `knowledge_base/sessions/mission-debrief-template.md` | Post-mission debrief template filled by picard at close   | picard        |

---

## Archive Tier

| Location | Description | Maintained By |
| -------- | ----------- | ------------- |
| `knowledge_base/archive/` | Historical long-form artifacts and superseded guidance | picard |
| `knowledge_base/current/` | Canonical high-signal guidance for active execution | picard |

---

## Pending Additions (Backlog)

- [ ] `database-migration-strategies.md` — Zero-downtime migration patterns

---

## Version History

```markdown
---
Version History:
    - 2026-04-04: picard — Updated index; marked incident-response-playbook.md as complete (now ~75% knowledge base coverage)
    - 2026-04-05: picard — Added team-health-assessment-github-agents.md; 15 remediation items identified across CI/CD, security, testing, and reliability domains
    - 2026-04-05: picard — Added tech-debt-register (barclay), monitoring-observability enhancements (obrien), agent-performance-log (picard), session journal infrastructure (guinan); removed resolved pending items
    - 2026-04-11: geordi — Added notification-integration.md (connectivity layer: Teams/Slack webhooks, MDR-to-Issue workflow, signal mapping)
    - 2026-04-11: picard — Added multi-repo-conventions.md (hub model, workspace orientation, repo-scoped KB signals, cross-repo mission rules)
    - 2026-04-11: picard — Indexed all top-level KB documents so kb-lint has full top-level coverage and no warning-only gaps
    - 2026-04-12: picard — Added spec-driven-development.md to new Quality Gates section (NEW-3 fix)
---
```

---

_Managed by picard (orchestrator) | Review cadence: Quarterly_
