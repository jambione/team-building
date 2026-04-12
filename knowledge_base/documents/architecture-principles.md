# Architecture Principles

## Current State

**As of**: 2026-04-05  
**Health**: GREEN  
**Top active item**: All foundational patterns (composition over inheritance, stateless components, built-in features first) accepted and active. ADR-001 through ADR-003 all in force. No active violations flagged.

---

## Foundational Rules

- Keep solutions as simple as possible, but no simpler.
- Strictly follow the Single Responsibility Principle.
- Prefer composition over inheritance.
- Design for long-term maintainability, not just short-term speed.

## Decision Framework

- Evaluate every design against simplicity, performance, and future maintenance cost.
- Document major architectural decisions in this knowledge base.
- Favor built-in language features over heavy external libraries when reasonable.

## Common Patterns Used by the Team

- Clear separation of concerns (UI, business logic, data access) — see ADR-002
- Stateless services where possible — see ADR-002 (Stateless Component Design)
- Components should be easily testable
- Use established patterns rather than inventing new ones
- Composition over inheritance — see ADR-001
- Built-in language features before external dependencies — see ADR-003
- Acceptance Criteria are a hard gate before execution starts (no code without `[AC-APPROVED]`) — see ADR-004 and [spec-driven-development.md](spec-driven-development.md)

## ADR Coherence Rule (added 2026-04-12)

The KB must have exactly one canonical location for each ADR's full text. Because `adr-workflow.yml` creates separate files (`knowledge_base/documents/adr-NNNN-slug.md`), `architecture-decision-records.md` is the **index only** — not the full text. Inline ADR text in the index document must be migrated to separate files, and the index updated to point to those files. Mixing inline text and workflow-generated separate files creates two sources of truth.

**Rule**: Any ADR proposed or accepted after ADR-003 must be stored as a separate file. ADR-001 through ADR-003 have been migrated to separate files (Sprint 3 complete, 2026-04-12, owner: data).

## Version History

```
2026-04-05: picard — Initial architecture principles document
2026-04-12: data — Added ADR links to common patterns; added ADR Coherence Rule (Sprint Health Check finding D-1, D-5)
2026-04-12: troi — Added AC gate pattern reference (ADR-004); marked ADR-001/002/003 migration complete
```
