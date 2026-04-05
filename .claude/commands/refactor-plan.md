# /refactor-plan

Plan a refactoring. data validates target architecture, riker sequences execution, troi defines test safety net, crusher assesses risk. Usage: /refactor-plan <describe the refactoring goal>

Load personas from `.clinerules/TNG/`. Read `architecture-principles.md` and `coding-standards.md` before starting.

**data** (lead): validate target architecture, identify what must not change (interfaces, contracts, behaviours). End with handoff.
**riker**: Execution Coordination Report — sequence steps to minimise risk, identify feature flag needs. End with handoff.
**troi**: test safety net — what must be green before starting, during, and at completion. Regression risk assessment. End with handoff.
**crusher**: rollback plan if a step fails in production. End with handoff.

picard delivers: phased execution plan with risk gates, rollback decision points, Definition of Done. Close with **"Make it so!"**
