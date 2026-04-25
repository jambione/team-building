# Mission Intake Template

> **Instructions**: Fill this out before picard opens the Ready Room.
> Paste your completed intake into chat to trigger the full mission workflow.
> Every field is required. picard will not open the Ready Room on an incomplete intake.

---

## Mission Intake — DE61356 rally-context-retrieval-and-mission-kickoff

**Mission:** Fix DE61356 in AGP so blank line-level HCPCS and PX dates do not default to current date and instead trigger the required field validation behavior.

**Target repo:** knowledge-components

**Done when:**

- Rally context for DE61356 is retrieved from WSAPI live mode with authenticated evidence captured.
- Mission branch mission/de61356-rally-context-retrieval-and-mission-kickoff is created in knowledge-components before implementation work starts.
- AGP no longer defaults blank line-level HCPCS and PX dates to current date in request processing.
- Validation returns required field errors for missing HCPCS and PX dates while preserving existing defaults for Thru Date, Facility, and Grouper ID.

**Constraints:**

- Defect context (live Rally): State Submitted, Schedule State Refining, Owner Larisa Dubb, Severity 3-Minor Problem, Project KC CXT.
- Work must use knowledge-components Rally PowerShell scripts (.github/agents/scripts/kc-rally-agent.ps1 and get-rally-context.ps1).
- Do not regress current defaulting behavior for Thru Date, Facility, and Grouper ID.

---

## Example (filled)

**Mission:** Fix the KC Cloud token service to handle concurrent authentication requests from the same user — DE35854. Currently only the 1st of N concurrent requests succeeds; all remaining fail when the same username/password is submitted simultaneously across ~50 Load Runner instances.

**Target repo:** `knowledge-components`

**Done when:**

- Token service returns HTTP 200 for all concurrent requests when the same credentials are used across multiple simultaneous instances
- Performance test at 50 concurrent instances with identical user/password all pass
- No regression on single-instance login behavior

**Constraints:**

- Severity 3-Minor / Priority Normal — no emergency timeline
- Schedule State: Refining — investigation phase first, no direct implementation until root cause confirmed
- Reproducing requires Load Runner or equivalent concurrency harness (50 instance run)
- Fix must not break existing SSO token flows or session behavior
