# Architecture Decision Records (ADRs) — IT Team Template

## Current State

**As of**: 2026-04-12  
**Health**: AMBER  
**Top active item**: ADR-004 (Spec-Driven Development Gate) accepted 2026-04-12 — AC gate is now enforced in three places. Owner is troi.

---

## ADR Index

Agents: scan this table before beginning architecture analysis. Do not propose or implement anything that contradicts an Accepted ADR without explicitly flagging and resolving the conflict first.

| ID | Title | Status | Date | Domain | Owner | File |
|----|-------|--------|------|--------|-------|------|
| ADR-001 | Composition Over Inheritance Pattern | Accepted | 2026-03-15 | Architecture | data | [adr-0001-composition-over-inheritance.md](adr-0001-composition-over-inheritance.md) |
| ADR-002 | Stateless Component Design | Accepted | 2026-03-20 | Architecture | data | [adr-0002-stateless-component-design.md](adr-0002-stateless-component-design.md) |
| ADR-003 | Built-in Language Features First | Accepted | 2026-04-01 | Architecture | data | [adr-0003-built-in-language-features-first.md](adr-0003-built-in-language-features-first.md) |
| ADR-004 | Spec-Driven Development Gate | Accepted | 2026-04-12 | Process / Quality | troi | [adr-0004-spec-driven-development-gate.md](adr-0004-spec-driven-development-gate.md) |

> data adds a row here when picard approves a new ADR. Each ADR lives in its own file — this table is the index only. ADR Coherence Rule: never duplicate ADR content inline here.

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

## ADR Full Text

Each ADR lives in its own canonical file. This section is intentionally empty — do not add inline ADR text here.

- [ADR-001](adr-0001-composition-over-inheritance.md) — Composition Over Inheritance Pattern
- [ADR-002](adr-0002-stateless-component-design.md) — Stateless Component Design
- [ADR-003](adr-0003-built-in-language-features-first.md) — Built-in Language Features First
- [ADR-004](adr-0004-spec-driven-development-gate.md) — Spec-Driven Development Gate

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
