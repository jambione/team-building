# /release-readiness

Release readiness gate. All crew return GO or NO-GO. Usage: /release-readiness <release scope>

Load personas from `.clinerules/TNG/`. Read the most recent health assessment and `past-lessons-learned.md` before starting.

All crew run in parallel. Each returns **GO / NO-GO + blockers**:

**geordi**: pipeline green? Build artefact clean? End with handoff.
**worf**: security gates passing? No CRITICAL CVEs? CodeQL clean? End with handoff.
**troi**: all tests passing? Coverage thresholds met? No open defects above threshold? End with handoff.
**crusher**: production currently healthy? Rollback validated? Health checks in place? End with handoff.
**data**: no architectural regressions or ADR violations? End with handoff.

picard delivers: **RELEASE: GO** (all crew GO) or **RELEASE: NO-GO** (any crew NO-GO) with blocker list and owners. Close with **"Make it so!"** (GO) or **"Not yet. Address the blockers first."** (NO-GO)
