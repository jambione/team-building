# Architecture Decision Records (ADRs) — IT Team Template

## Current State

**As of**: 2026-04-05  
**Health**: GREEN  
**Top active item**: ADR-003 (Built-in Language Features First) is newest — verify all new dependency introductions against it. Owner is data for Sprint 2 onward.

---

## ADR Index

Agents: scan this table before beginning architecture analysis. Do not propose or implement anything that contradicts an Accepted ADR without explicitly flagging and resolving the conflict first.

| ID | Title | Status | Date | Domain | Owner |
|----|-------|--------|------|--------|-------|
| ADR-001 | Composition Over Inheritance Pattern | Accepted | 2026-03-15 | Architecture | data |
| ADR-002 | Stateless Component Design | Accepted | 2026-03-20 | Architecture | data |
| ADR-003 | Built-in Language Features First | Accepted | 2026-04-01 | Architecture | data |

> data adds a row here when picard approves a new ADR. The full ADR text lives in the sections below.

---

## Purpose

Document significant architectural decisions with context, alternatives considered, and rationale. Updated quarterly by data.

---

## ADR Template

```markdown
# [Short Title] — [Date]

## Status

[Proposed | Accepted | Superseded | Deprecated]

## Context

- Problem we're solving
- Relevant decisions that preceded this one
- Limitations of existing approaches

## Decision

[Clear statement of the chosen direction]

## Consequences

- Positive outcomes expected
- Compromises made
- Future implications

## References

- Links to related documentation, RFCs, or external resources
```

---

## Historical ADRs — data's Contributions

### ADR-001: Composition Over Inheritance Pattern (2026-03-15)

**Status:** Accepted

**Context:** Team was using deep inheritance hierarchies causing fragile base class problems.

**Decision:** All new components must use composition; existing hierarchies to be refactored over 2 sprints.

---

### ADR-002: Stateless Component Design (2026-03-20)

**Status:** Accepted

**Context:** Components were maintaining state internally, causing testing difficulties and memory leaks.

**Decision:** All components must be stateless by default; state lifted to parent or external store.

---

### ADR-003: Built-in Language Features First (2026-04-01)

**Status:** Accepted

**Context:** Heavy dependency on utility libraries for basic operations.

**Decision:** Prefer native language features and standard library before adding dependencies.

---

## Verification Commands

```bash
# Search knowledge base for ADR references
grep -r "ADR-" knowledge_base/documents/*.md | head -20

# Check recent commits mentioning architecture decisions
git log --since="1 month ago" --oneline -- "*arch*" | head -20
```

---

_Created: 2026-04-04 | Owner: data (Architect) | Review Cadence: Quarterly_
