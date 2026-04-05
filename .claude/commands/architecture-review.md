# /architecture-review

Architecture review led by data. Evaluates a proposed design against existing principles. Usage: /architecture-review <describe the design>

Load personas from `.clinerules/TNG/`. Read `architecture-principles.md` and `architecture-decision-records.md` before starting.

**data** leads: evaluate against principles, check for SRP violations and coupling risks, produce APPROVED / APPROVED WITH CONDITIONS / REJECTED verdict, draft ADR if a decision is reached. Update `architecture-principles.md`. Flag `[NEW DISCOVERY]`. End with: `data returns control to picard. [arch-design-complete]`

**worf** supports: security implications of the architecture.
**crusher** supports: reliability risks, single points of failure.

picard delivers: final verdict, risk register, ADR if applicable. Close with **"Make it so!"**
