# ADR-0002: Stateless Component Design

## Status

**Accepted** — 2026-03-20

| Field | Value |
|-------|-------|
| **ADR Number** | 0002 |
| **Date Accepted** | 2026-03-20 |
| **Decided By** | picard |
| **Domain** | Architecture |
| **Owner** | data |

---

## Context

Components were maintaining state internally, which caused testing difficulties (tests had to account for state side effects), memory leaks (stateful objects not being cleaned up), and unpredictable behaviour across component reuse. The internal state also made components harder to reason about in isolation.

---

## Decision

All components must be stateless by default. Any required state is lifted to a parent component or external state store. A component may only hold state when there is an explicit, documented reason why the state cannot be managed externally.

---

## Consequences

### Positive
- Components become pure functions of their inputs — trivially testable
- No memory leaks from stale internal state
- Components are safe to reuse and cache
- State management is centralised and visible

### Negative / Trade-offs
- Parent components / state stores become more responsible
- Requires discipline to avoid drifting back to internal state

### Neutral
- Aligns with ADR-0001 (Composition Over Inheritance) — stateless components compose cleanly

---

## References

- Related: ADR-0001 (Composition Over Inheritance Pattern)
- Related: ADR-0003 (Built-in Language Features First)

---

## Version History

```
- 2026-03-20: data — ADR accepted
- 2026-04-12: data — Migrated from inline text in architecture-decision-records.md to separate file per ADR Coherence Rule
```
