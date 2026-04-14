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

- Clear separation of concerns (UI, business logic, data access)
- Stateless services where possible
- Components should be easily testable
- Use established patterns rather than inventing new ones
