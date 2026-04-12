# IT Team Best Practices

## General Development Guidelines

- Always follow the team's coding standards and conventions.
- Write clean, readable, maintainable code with meaningful naming and clear structure.
- Use appropriate comments to explain complex logic or decisions.
- Avoid over-engineering; keep solutions simple and focused on solving the problem at hand.

## Team Collaboration

- Communicate clearly and frequently using team conventions.
- Use third-person language in all documentation and communication.
- Document changes, decisions, and rationale for future reference.

## Quality Assurance

- Write tests to cover critical paths and edge cases.
- Perform QA checks before merging or deploying code.
- Report bugs and issues promptly with clear reproduction steps.

### CI Test Requirements (added 2026-04-12)

All CI test runs must:
1. Produce a JUnit-compatible test result file (or framework equivalent)
2. Upload test results as a workflow artifact (`actions/upload-artifact`)
3. Enforce a minimum coverage threshold via `--coverageThreshold` (Jest), `--cov-fail-under` (pytest), or equivalent
4. Report coverage percentage in the CI step summary

A CI run that reports "tests passed" without an artifact and without a coverage gate is motion, not signal. Skipping coverage upload is only acceptable when the test framework explicitly does not support it — this must be documented, not silently absent.

> **Status (2026-04-12)**: TD-004 (coverage gate) and TD-005 (test artifact upload) are both open in ci.yml. TD-004 is High severity and past-due from Sprint 2. Target: add `python -m pytest --cov --cov-fail-under=70 --junitxml=test-results.xml` and `actions/upload-artifact` step to ci.yml before Sprint 2 closes (2026-04-19).

### Test Naming and Types

- Unit tests: co-located with source (`*.test.ts` / `*.spec.ts`)
- Integration tests: `tests/integration/`
- Test file naming must match the module under test (e.g. `auth.service.test.ts` for `auth.service.ts`)

## DevOps & Infrastructure

- Follow established CI/CD pipelines and deployment practices.
- Use Docker for consistent environments across development, testing, and production.
- Monitor deployments and logs for any anomalies.

## Documentation

- Keep documentation up to date and accurate.
- Document new features, changes, and known limitations.
- Use the team's knowledge base as a central reference for past decisions and lessons learned.

## Continuous Improvement

- Review and reflect on completed tasks to identify opportunities for improvement.
- Share insights and best practices with the team regularly.
