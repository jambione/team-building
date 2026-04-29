# Mission Intake Template

> **Instructions**: Fill this out before picard opens the Ready Room.
> Paste your completed intake into chat to trigger the full mission workflow.
> Every field is required. picard will not open the Ready Room on an incomplete intake.

---

## Mission Intake — [DEFECT/STORY ID] [short-slug]

**Mission:** [One sentence describing the objective.]

**Target repo:** [repo-name]

**Done when:**

- [Acceptance criterion 1]
- [Acceptance criterion 2]
- [Acceptance criterion 3]

**Constraints:**

- [Constraint 1 — e.g. no regression on existing behavior X]
- [Constraint 2 — e.g. severity/priority from Rally or issue tracker]
- [Constraint 3 — e.g. must not break Y]

---

## Example (filled)

**Mission:** Fix the authentication service to handle concurrent login requests from the same user — DE00001. Currently only the first of N concurrent requests succeeds; all remaining fail when the same credentials are submitted simultaneously.

**Target repo:** `your-spoke-repo`

**Done when:**

- Auth service returns HTTP 200 for all concurrent requests when the same credentials are used across multiple simultaneous instances
- Load test at 50 concurrent instances with identical credentials all pass
- No regression on single-instance login behavior

**Constraints:**

- Severity 3-Minor / Priority Normal — no emergency timeline
- Investigation phase first; no implementation until root cause confirmed
- Fix must not break existing SSO or session flows
