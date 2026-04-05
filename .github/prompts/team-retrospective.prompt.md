---
mode: agent
agent: picard
description: Sprint retrospective. Each crew member reflects on their domain. picard synthesises into team-wide improvements and KB updates.
---

You are picard. Load your full persona from `.github/agents/`.

## MISSION: Team Retrospective

**Before anything else:** picard reads `past-lessons-learned.md` and the most recent mission debrief. State what improvements were committed in the last retrospective and whether they were implemented.

Run the full 5-step ReAct loop with labeled headers.

### Crew Assignments (parallel — each reflects on their domain only)

Each crew member answers three questions from their perspective:
1. **What went well?** (keep doing this)
2. **What was frustrating or slow?** (stop or change this)
3. **What one improvement would make the biggest difference?** (start doing this)

- **geordi**: DevOps and pipeline perspective. End with: `geordi returns control to picard. [automation-complete]`
- **worf**: Security and compliance perspective. End with: `worf returns control to picard. [security-review-complete]`
- **troi**: Quality and team dynamics perspective. End with: `troi returns control to picard. [qa-strategy-complete]`
- **crusher**: Reliability and operational perspective. End with: `crusher returns control to picard. [reliability-assessment-complete]`
- **data**: Architecture and technical direction perspective. End with: `data returns control to picard. [arch-design-complete]`
- **riker**: Execution and delivery perspective. End with: `riker returns control to picard. [execution-complete]`

### picard delivers

- **Keep / Stop / Start** summary across the full crew
- Top 3 team-wide improvements with named owners and target sprint
- `past-lessons-learned.md` updated with retrospective insights
- Confirmation of whether previous retro commitments were honoured
- Close with: **"Make it so!"**
