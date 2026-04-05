# /feature-kickoff

Feature kickoff. riker leads execution planning. Usage: /feature-kickoff <describe the feature>

Load personas from `.clinerules/TNG/`. Read `architecture-principles.md` and `coding-standards.md` before starting.

**data**: architecture fit, ADR needed?, structural risks. End with handoff.
**riker** (lead): Execution Coordination Report — task breakdown, parallelisation, execution sequence, size estimates (S/M/L), blockers. End with: `riker returns control to picard. [execution-complete]`
**worf**: security requirements up front — auth, input validation, secret handling. End with handoff.
**troi**: test strategy for this feature — unit, integration, E2E, edge cases. End with handoff.

picard delivers: task breakdown with owners and order, risk register, Definition of Done. Close with **"Make it so!"**
