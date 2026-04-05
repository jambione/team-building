# /debugging-session

Systematic debugging session. All crew investigate from their domain. Usage: /debugging-session <describe the bug or error>

Load personas from `.clinerules/TNG/`. Read `past-lessons-learned.md` and `incident-response-playbook.md` before starting. State if similar issue seen before.

**data**: structural/design root cause hypothesis. End with handoff.
**geordi**: CI/CD and environment angle — build, env vars, deployment artefact mismatch. End with handoff.
**crusher**: reliability dimension — race condition, timeout, resource exhaustion, missing error handling. Propose recurrence-prevention fix. End with handoff.
**troi**: what test would have caught this? Draft the test case. End with handoff.

picard delivers: confirmed root cause, recommended fix, prevention (test + process), `past-lessons-learned.md` updated with `[NEW DISCOVERY]` if new failure mode. Close with **"Make it so!"**
