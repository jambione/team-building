# /regression-plan

Pre-release regression plan. troi identifies what must be re-tested. crusher validates operational readiness. Usage: /regression-plan <release scope or changelog>

Load personas from `.clinerules/TNG/`. Read `best-practices.md` and `defect-management-process.md` before starting.

**troi** (lead): what existing tests cover changed areas, what areas are at risk but uncovered (manual regression needed), what new tests to write, regression priority order for time-constrained testing. Update `best-practices.md`. End with handoff.
**crusher**: operational readiness — health checks, rollback, monitoring in place for all changes. End with handoff.
**worf**: confirm no security-sensitive area changed without a security review. End with handoff.

picard delivers: regression checklist ordered by priority, GO / NO-GO recommendation with criteria, blocking items. Close with **"Make it so!"**
