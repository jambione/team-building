# Knowledge Base Governance Policy

## Purpose
This document defines how the kc- team maintains, updates, and governs the shared knowledge base at `knowledge_base/documents/`.

---

## Document Structure & Naming Convention

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

### Owner Registry (To Be Completed)

| Document | Primary Owner | Review Cadence | Last Reviewed |
|----------|---------------|----------------|---------------|
| architecture-principles.md | kc-michael | Quarterly | TBD |
| github-actions-best-practices.md | kc-hang | Monthly | TBD |
| devops-best-practices.md | kc-shawn, kc-hang | Quarterly | TBD |

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
- 2026-04-04: kc-dave — Added CI/CD pipeline recommendations section
- 2026-03-15: kc-hang — Updated caching best practices
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

- kc-dave must review and update this governance policy quarterly
- Any team member can suggest improvements to this policy by creating a draft PR
- Documents that violate these standards may be archived without warning after 60 days notice

---

*Created: 2026-04-04 | Owner: kc-dave (orchestrator)*