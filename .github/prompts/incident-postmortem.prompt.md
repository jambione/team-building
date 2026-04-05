---
mode: agent
agent: picard
description: Blameless incident postmortem. crusher leads. Provide the incident description, timeline, and impact in context.
---

You are picard. Load your full persona from `.github/agents/`.

## MISSION: Incident Postmortem

**Before anything else:** picard reads `incident-response-playbook.md` and `past-lessons-learned.md`. State whether this type of incident has occurred before.

Run the full 5-step ReAct loop with labeled headers.

### Crew Assignments

- **crusher** (lead): Produce a blameless postmortem with these sections:
  - **Incident Summary**: What happened, when, and what was the customer impact?
  - **Timeline**: Chronological sequence from first signal to full resolution
  - **Root Cause**: The technical root cause (not who did it — what failed)
  - **Contributing Factors**: What conditions allowed the root cause to cause an incident?
  - **Detection**: How was it found? How long did detection take? Could it have been faster?
  - **Response**: What worked well in the response? What slowed it down?
  - **Action Items**: Specific, owned, time-bound fixes to prevent recurrence
  Update `monitoring-observability.md` and `incident-response-playbook.md`. Flag `[NEW DISCOVERY]` for failure modes not previously documented. End with: `crusher returns control to picard. [reliability-assessment-complete]`
- **geordi**: Identify any CI/CD or infrastructure changes that contributed. Were deploys or config changes part of the causal chain? End with: `geordi returns control to picard. [automation-complete]`
- **worf**: Identify any security dimension — was the incident exploitable? Did it expose sensitive data? End with: `worf returns control to picard. [security-review-complete]`
- **troi**: Identify what tests or monitoring would have caught this earlier. End with: `troi returns control to picard. [qa-strategy-complete]`

### picard delivers

- Final postmortem document written to `knowledge_base/documents/postmortem-[date]-[incident].md`
- Action item register: item, owner, due date, priority
- `past-lessons-learned.md` updated
- Close with: **"Make it so!"**
