# /incident-postmortem

Blameless incident postmortem. crusher leads. Usage: /incident-postmortem <describe the incident, timeline, and impact>

Load personas from `.clinerules/TNG/`. Read `incident-response-playbook.md` and `past-lessons-learned.md` before starting. State if this type of incident has occurred before.

**crusher** (lead): blameless postmortem — Summary, Timeline, Root Cause, Contributing Factors, Detection, Response, Action Items. Update `monitoring-observability.md` and `incident-response-playbook.md`. Flag `[NEW DISCOVERY]`. End with handoff.
**geordi**: CI/CD or infrastructure changes in the causal chain? End with handoff.
**worf**: security dimension — was it exploitable? Data exposed? End with handoff.
**troi**: what tests or monitoring would have caught this earlier? End with handoff.

picard delivers: postmortem written to `knowledge_base/documents/postmortem-[date]-[incident].md`, action item register (item, owner, due date), `past-lessons-learned.md` updated. Close with **"Make it so!"**
