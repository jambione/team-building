# Coding Standards

## Core Philosophy

- Readability and long-term maintainability come before cleverness or minor performance gains.
- Code should be understandable by a new team member in under 30 seconds.
- Keep functions, classes, and components small and focused (Single Responsibility Principle).

## Minimalism & Refactoring Standards

- **Signal Principle**: Only include code that provides value (signal) — remove noise.
- **Minimal Change**: Refactor only what is necessary to achieve the goal.
- **Reduce Bloat**: Eliminate extraneous and duplicate code.
- **Refactor Duplication**: Replace duplicated logic with reusable components.

## Naming Conventions

- Variables and functions: `camelCase`
- Classes, types, and interfaces: `PascalCase`
- Constants: `UPPER_SNAKE_CASE`
- Files and folders: `kebab-case` (e.g., `user-profile.service.ts`)
- Boolean variables: prefix with `is`, `has`, `can` (e.g., `isAuthenticated`)

## Style Guidelines

- Maximum line length: 100 characters
- Use 2 spaces for indentation
- Avoid deep nesting (prefer early returns)
- Add comments only for "why" (not "what")
- Always handle errors with meaningful, user-friendly messages
- Prefer built-in language features over heavy external libraries when reasonable

## Testing Standards

- Every new or changed business logic must have unit tests
- Tests must cover happy path + important edge cases
- Keep tests clear, readable, and focused
- Aim for high test coverage on critical paths

## Example (Good vs Bad)

**Good:**

```ts
function calculateTotal(items: CartItem[]): number {
    if (items.length === 0) return 0;
    return items.reduce((sum, item) => sum + item.price * item.quantity, 0);
}
```

### 3. `architecture-principles.md` (Expanded)

```markdown
# Architecture Principles

## Foundational Rules

- Keep solutions as simple as possible, but no simpler.
- Strictly follow the Single Responsibility Principle.
- Prefer composition over inheritance.
- Design for long-term maintainability and readability first.

## Decision Framework

- Evaluate every design against three factors: simplicity, performance, and future maintenance cost.
- Document major architectural decisions by suggesting updates to this knowledge base.
- Favor built-in language features and established patterns over inventing new solutions.

## Common Patterns Used by the Team

- Clear separation of concerns (UI / business logic / data access)
- Stateless services where possible
- Components and services should be easily testable
- Use dependency injection for flexibility without tight coupling

## When kc-michael Should Be Called

- Any task involving new features, refactoring of core logic, or unclear system structure.
- kc-michael provides high-level design, folder structure, and Mermaid diagrams before implementation begins.
```
