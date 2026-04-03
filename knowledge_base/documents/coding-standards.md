# Coding Standards

## Core Philosophy

- Readability and maintainability come before cleverness.
- Code should be understandable by someone new to the project in under 30 seconds.
- Small, focused functions and components are preferred.

## Naming Conventions

- Variables & functions: camelCase
- Classes & Types: PascalCase
- Constants: UPPER_SNAKE_CASE
- Files: kebab-case (e.g., user-profile.service.ts)

## Style Guidelines

- Maximum line length: 100 characters
- Use 2 spaces for indentation
- Avoid deep nesting (max 3 levels when possible)
- Add comments only for "why", never for "what"
- Always handle errors with meaningful messages
- Prefer early returns over deep if/else chains

## Testing Standards

- Every new business logic must have unit tests
- Tests should be clear and readable
- Cover both happy path and important edge cases
