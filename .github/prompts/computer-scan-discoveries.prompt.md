---
name: computer-scan-discoveries
description: "Use when: Computer document changes — scan uncommitted changes for NEW DISCOVERY items, map each to the right KB document owner, and escalate to picard if decisions are required. Lightweight discovery audit without full Ready Room."
tags: [computer, scan, discoveries, kb-audit, knowledge-base]
---

# Computer: Scan for Document Changes & Discovery Mapping

**Invocation**: `Computer: document changes` or `/computer-scan-discoveries`

**Purpose**: Identify uncommitted changes that contain new discoveries, map each discovery to the correct KB domain and owner, and flag items requiring picard escalation.

---

## Execution Steps

### 1. Scan Both Workspaces

Scan `knowledge-components` and `team-building` for uncommitted changes (modified, added, deleted, untracked files).

### 2. Assess for NEW DISCOVERY Items

For each uncommitted change, determine if it represents:

- A new finding, pattern, or insight
- A breaking change or architectural decision
- A reliability, security, or observability gap
- A team convention or best-practice update

If none of the above, it is not a discovery — skip it.

### 3. Map Each Discovery to KB Domain

Use this routing map from `knowledge_base/documents/index.md`:

| Discovery Type                                             | KB Domain             | Document Owner |
| ---------------------------------------------------------- | --------------------- | -------------- |
| Architecture pattern, design principle, decision rationale | Architecture & Design | data           |
| CI/CD, infrastructure, automation, DevOps                  | DevOps & CI/CD        | geordi         |
| Security finding, compliance, hardening                    | Security              | worf           |
| Testing, QA, quality gates, acceptance criteria            | Quality & Spec        | troi           |
| Reliability, edge cases, failure modes                     | Reliability           | crusher        |
| Performance, efficiency, code quality, tech debt           | Technical Debt        | barclay        |
| Observability, logging, monitoring, alerting               | Observability         | obrien         |
| Team process, convention, workflow change                  | Development Practices | picard         |
| Historical lessons, cross-mission patterns                 | Agent Governance      | guinan         |

### 4. Flag picard Escalation

Escalate to picard (emit `[COMPUTER-ROUTED: picard | reason]`) if:

- The discovery impacts architectural decisions or system design
- The discovery reveals a P0 or P1 risk
- The discovery requires a decision before code can be written
- The discovery conflicts with an existing KB document or convention
- The discovery affects multiple KB domains (cross-cutting concern)

Otherwise, the discovery is flagged for the identified KB domain owner to update progressively.

### 5. Report Format

```
**Scan Result** — <timestamp>

Workspace: knowledge-components
- <count> uncommitted files scanned
- <count> NEW DISCOVERY items identified

Workspace: team-building
- <count> uncommitted files scanned
- <count> NEW DISCOVERY items identified

NEW DISCOVERY Items:
(if zero, emit: "No matching records found.")

| Discovery | Type | KB Domain | Owner | Escalation |
|-----------|------|-----------|-------|-----------|
| <desc> | <type> | <domain> | <agent> | picard / local-update |

Escalation Required: Yes / No
(If yes, emit: [COMPUTER-ROUTED: picard | <reason>])

[COMPUTER-LOOKUP: <primary-doc>] — Nearest relevant document
```

### 6. Return Control

If escalating:

```
[COMPUTER-ROUTED: picard | <reason>]
Suggested Mission: <reframed objective based on discoveries>
```

Otherwise:

```
[COMPUTER-QUERY: scan-complete | domain-owners notified]
```

---

## KB Routing Quick Reference

**Architecture & Design** → `architecture-principles.md`, `system-design-patterns.md`, `architecture-decision-records.md`, `adr-*.md` (data)

**DevOps & CI/CD** → `ci-cd-pipeline-recommendations.md`, `devops-best-practices.md`, `github-actions-best-practices.md`, `github-actions-security-hardening.md` (geordi)

**Quality & Spec** → `spec-driven-development.md`, `best-practices.md` (troi)

**Technical Debt** → `tech-debt-register.md` (barclay)

**Observability** → `monitoring-observability.md` (obrien)

**Security** → `github-actions-security-hardening.md`, `incident-response-playbook.md` (worf)

**Reliability** → `monitoring-observability.md` (crusher)

**Agent Governance** → `past-lessons-learned.md`, `agent-performance-log.md` (guinan)

---

## Rules

- **Always check Current State first**: `knowledge_base/current/session-continuity.md`, `knowledge_base/current/workspace-context.md`, `knowledge_base/current/ops-log.md`
- **Zero changes = zero discoveries** — "No matching records found" is a valid result
- **One discovery = one KB update** — map each to exactly one owner (or flag as cross-cutting for picard)
- **Specific mapping required** — do not roll multiple unrelated discoveries into one entry
- **Escalation is binary** — picard or local-update, not "maybe"
