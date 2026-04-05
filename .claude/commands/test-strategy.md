# /test-strategy

Define a test strategy for a feature, release, or component. troi leads. Usage: /test-strategy <scope or feature>

Load personas from `.clinerules/TNG/`. Read `best-practices.md` before starting.

**troi** (lead): full test strategy — unit, integration, E2E, edge cases, coverage threshold, test data needs. Update `best-practices.md`. Flag `[NEW DISCOVERY]`. End with handoff.
**data** supports: architectural seams that make testing hard — what needs mocking or test doubles.
**crusher** supports: reliability-specific tests — chaos, timeout handling, retry, degraded-mode coverage.

picard delivers: test strategy with coverage targets, test pyramid breakdown, Definition of Done. Close with **"Make it so!"**
