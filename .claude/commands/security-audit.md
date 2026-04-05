# /security-audit

Focused security audit led by worf, with data and geordi in support. Reads `github-actions-security-hardening.md` before starting. Updates it after.

Load personas from `.clinerules/TNG/`. Read `github-actions-security-hardening.md` and `past-lessons-learned.md` before starting.

## MISSION: Security Audit

Run the full 5-step ReAct loop with labeled headers. In the **Reason** step, state which prior security findings remain open.

### Crew Assignments

- **worf** (lead): Audit all `.github/workflows/` — permissions blocks, secret exposure, pinned action versions, SAST coverage, supply-chain risks. Update `github-actions-security-hardening.md`. Flag `[NEW DISCOVERY]` for anything not in the KB. End with catchphrase and: `worf returns control to picard. [security-review-complete]`
- **data** (support): Assess the architectural attack surface implied by the workflow structure.
- **geordi** (support): Identify DevOps-layer risks — insecure build steps, artifact exposure, caching risks.

### picard delivers

- Synthesized security posture rating
- Remediation priority matrix with owners and sprints
- `past-lessons-learned.md` updated
- Close with: **"Make it so!"**
