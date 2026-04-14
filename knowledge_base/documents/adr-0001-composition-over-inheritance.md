# ADR-0001: Composition Over Inheritance Pattern

## Status

**Accepted** — 2026-03-15

| Field | Value |
|-------|-------|
| **ADR Number** | 0001 |
| **Date Accepted** | 2026-03-15 |
| **Decided By** | picard |
| **Domain** | Architecture |
| **Owner** | data |

---

## Context

The team was using deep inheritance hierarchies across components, which led to fragile base class problems. Changes to parent classes caused unexpected breakages in unrelated child classes, making refactoring expensive and testing difficult. The coupling between layers was high.

---

## Decision

All new components must use composition rather than inheritance. Existing hierarchies are to be refactored over 2 sprints. A component may only extend another when there is a genuine is-a relationship that cannot be expressed through composition.

---

## Consequences

### Positive
- Components become independently testable
- Reduced coupling between layers
- Easier to swap implementations at runtime
- No fragile base class problem

### Negative / Trade-offs
- Slightly more boilerplate in some cases (explicit delegation vs. inherited methods)
- Existing code requires refactoring investment over 2 sprints

### Neutral
- Aligns with ADR-002 (Stateless Component Design) — composition pairs naturally with stateless components

---

## References

- Related: ADR-0002 (Stateless Component Design)
- Related: ADR-0003 (Built-in Language Features First)

---

## Version History

```
- 2026-03-15: data — ADR accepted
- 2026-04-12: data — Migrated from inline text in architecture-decision-records.md to separate file per ADR Coherence Rule
```
