# Knowledge Base Governance Policy

## Purpose

This document defines how the IT team maintains, updates, and governs the shared knowledge base at `knowledge_base/documents/`.

---

## Document Structure & Naming Convention

### KB Tiers

- `knowledge_base/current/` — canonical, concise, first-reference guidance.
- `knowledge_base/documents/` — working reference docs and domain standards.
- `knowledge_base/archive/` — historical long-form and superseded material.

### Naming Rules

```
<topic>-<specificity>.md
```

Examples:

- `architecture-principles.md` ✓
- `ci-cd-pipeline-recommendations.md` ✓
- `database-migration-strategies.md` (pending)

---

## Document Ownership & Maintenance

### Owner Registry

| Document | Primary Owner | Review Cadence | Last Reviewed |
|----------|---------------|----------------|---------------|
| `architecture-principles.md` | data | Quarterly | 2026-04-05 |
| `architecture-decision-records.md` | data | Per-ADR | 2026-04-05 |
| `system-design-patterns.md` | data | Quarterly | 2026-04-04 |
| `github-actions-best-practices.md` | geordi | Monthly | 2026-04-05 |
| `github-actions-security-hardening.md` | geordi + worf | Monthly | 2026-04-05 |
| `devops-best-practices.md` | geordi | Quarterly | 2026-04-05 |
| `ci-cd-pipeline-recommendations.md` | geordi | Quarterly | 2026-04-05 |
| `github-actions-security-hardening.md` | worf | Monthly | 2026-04-05 |
| `incident-response-playbook.md` | crusher + obrien | Quarterly | 2026-04-04 |
| `monitoring-observability.md` | obrien | Monthly | 2026-04-05 |
| `tech-debt-register.md` | barclay | Every sprint | 2026-04-05 |
| `past-lessons-learned.md` | guinan | Every mission | 2026-04-05 |
| `best-practices.md` | picard | Biannual | 2026-04-04 |
| `coding-standards.md` | picard | Biannual | 2026-04-04 |
| `team-conventions.md` | picard | Quarterly | 2026-04-04 |
| `onboarding-guide.md` | picard | Quarterly | 2026-04-04 |
| `rally-patterns.md` | picard | Quarterly | 2026-04-04 |
| `defect-management-process.md` | troi | Quarterly | 2026-04-04 |
| `knowledge-base-governance.md` | picard | Quarterly | 2026-04-09 |
| `agent-performance-log.md` | picard | Every sprint | 2026-04-05 |
| `sprint-state.md` | picard | Every sprint | 2026-04-05 |
| `index.md` | picard | Quarterly | 2026-04-05 |
| `current/session-continuity.md` | guinan | Every mission | 2026-04-09 |

---

## Document Review Cadence

### Standard Review Schedule

- **Critical/Architecture**: Quarterly review required
- **Best Practices**: Biannual review recommended
- **Implementation Guides**: Annual review minimum

### Review Checklist

When reviewing a document, the owner must verify:

1. [ ] Content is current and accurate
2. [ ] Examples are still valid (test commands, code snippets)
3. [ ] References to other documents are not broken
4. [ ] Document follows team writing conventions

---

## Version History Tracking

Each significant update should be logged at the bottom of the document:

```markdown
---
Version History:
    - 2026-04-04: picard — Added CI/CD pipeline recommendations section
    - 2026-03-15: geordi — Updated caching best practices
---
```

---

## Deprecation Policy

### When to Deprecate a Document

A document should be deprecated when:

1. The topic is fully covered by another, more comprehensive document
2. The content is outdated and cannot be reasonably updated
3. The document has been superseded by industry standards

### Deprecation Process

1. Owner marks document as `[DEPRECATED]` at the top
2. Adds deprecation notice with migration path in the first section
3. Archives to `knowledge_base/archived/` after 90 days

> Note: active archive path is `knowledge_base/archive/`.

---

## Document Quality Standards

### Minimum Requirements for All Documents

- [ ] Clear title and purpose statement (first paragraph)
- [ ] Relevant headings with logical hierarchy (H1 → H2 → H3)
- [ ] Actionable, specific guidance — avoid vague statements
- [ ] Working code examples or command snippets where applicable
- [ ] References to related documents in the knowledge base

---

## Knowledge Base Index (Auto-Generated Target)

The team should maintain an index document that lists all active documents with brief descriptions. This will be managed separately as `knowledge_base/documents/index.md`.

---

## Ethics & Responsibility

- picard must review and update this governance policy quarterly
- Any team member can suggest improvements to this policy by creating a draft PR
- Documents that violate these standards may be archived without warning after 60 days notice

---

_Created: 2026-04-04 | Owner: picard (orchestrator)_
