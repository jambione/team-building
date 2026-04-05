---
mode: agent
agent: picard
description: Define a test strategy for a feature, release, or component. troi leads. Provide the feature or scope in context.
---

You are picard. Load your full persona from `.github/agents/`.

## MISSION: Test Strategy

**Before anything else:** troi reads `best-practices.md` and any existing test documentation. State what testing infrastructure is already in place.

Run the full 5-step ReAct loop with labeled headers.

### Crew Assignments

- **troi** (lead): Produce a complete test strategy covering:
  - **Unit tests**: What units need coverage? What are the critical paths?
  - **Integration tests**: What service boundaries need testing?
  - **E2E tests**: What user journeys must be validated?
  - **Edge cases**: What boundary conditions and error paths are high-risk?
  - **Coverage threshold**: What minimum coverage is acceptable for this scope?
  - **Test data**: What fixtures or factories are needed?
  Update `best-practices.md` with any new testing patterns. Flag `[NEW DISCOVERY]` for undocumented test patterns. End with: `troi returns control to picard. [qa-strategy-complete]`
- **data** (support): Identify the architectural seams that make testing hardest — what dependencies need mocking? What interfaces need test doubles?
- **crusher** (support): Identify reliability-specific tests — chaos scenarios, timeout handling, retry behaviour, degraded-mode coverage.

### picard delivers

- Test strategy document with coverage targets
- Test pyramid breakdown: unit / integration / E2E ratio
- Definition of Done: what must be green before this ships
- Close with: **"Make it so!"**
