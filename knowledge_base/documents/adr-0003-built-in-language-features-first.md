# ADR-0003: Built-in Language Features First

## Status

**Accepted** — 2026-04-01

| Field | Value |
|-------|-------|
| **ADR Number** | 0003 |
| **Date Accepted** | 2026-04-01 |
| **Decided By** | picard |
| **Domain** | Architecture |
| **Owner** | data |

---

## Context

The codebase had accumulated heavy dependencies on utility libraries for operations that are natively supported by the language and standard library. This increased bundle size, introduced transitive dependency risk, and made it harder for contributors to understand the code without knowing the library APIs.

---

## Decision

Prefer native language features and the standard library before introducing an external dependency. A new dependency may only be added when: (1) the native equivalent requires significantly more code, (2) the library provides battle-tested edge-case handling that would be expensive to replicate, or (3) the dependency is already present in the project for another purpose.

All new dependency additions must be reviewed against this ADR before merging.

---

## Consequences

### Positive
- Reduced dependency surface — fewer CVEs, fewer supply-chain risks
- Code is readable without library knowledge
- Smaller install size and faster CI
- Easier onboarding for new contributors

### Negative / Trade-offs
- Some operations require more verbose native code
- Team must resist the convenience of grabbing a utility library

### Neutral
- data is responsible for reviewing dependency additions against this ADR from Sprint 2 onward

---

## References

- Related: ADR-0001 (Composition Over Inheritance Pattern)
- Related: ADR-0002 (Stateless Component Design)

---

## Version History

```
- 2026-04-01: data — ADR accepted
- 2026-04-12: data — Migrated from inline text in architecture-decision-records.md to separate file per ADR Coherence Rule
```
