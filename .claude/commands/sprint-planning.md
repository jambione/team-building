# /sprint-planning

Sprint planning. Full crew reviews the backlog. Usage: /sprint-planning <paste backlog items>

Load personas from `.clinerules/TNG/`. Read `past-lessons-learned.md` and the most recent health assessment before starting. State carry-forward items from the previous sprint.

**data**: architectural complexity and ADR requirements per item. Risk: HIGH / MEDIUM / LOW. End with handoff.
**riker** (lead): Execution Coordination Report — dependencies, sequencing, parallelisation opportunities, capacity allocation. End with handoff.
**worf**: security requirements per item that must be addressed during implementation. End with handoff.
**troi**: QA effort estimate per item. Flag items without a clear test strategy. End with handoff.
**crusher**: flag items touching deployment, reliability, or monitoring — these need extra capacity. End with handoff.

picard delivers: ordered sprint backlog (effort S/M/L, domain owners), risk items with mitigation, sprint goal statement, carry-forward items explicitly accepted. Close with **"Make it so!"**
