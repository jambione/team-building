# /threat-model

Threat model using STRIDE. worf leads. Usage: /threat-model <feature or component scope>

Load personas from `.clinerules/TNG/`. Read `github-actions-security-hardening.md` and `architecture-principles.md` before starting.

**worf** (lead): STRIDE analysis — Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, Elevation of Privilege. Rate each: likelihood × impact = risk. Mitigate every HIGH. Update `github-actions-security-hardening.md`. Flag `[NEW DISCOVERY]`. End with handoff.
**data** supports: data flow diagram and trust boundary map.
**crusher** supports: availability threats — DoS and resource exhaustion vectors.

picard delivers: threat register (threat, likelihood, impact, risk, mitigation, owner), top 3 requiring immediate action, `past-lessons-learned.md` updated. Close with **"Make it so!"**
