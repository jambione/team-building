# /pipeline-optimize

CI/CD pipeline optimization. geordi identifies bottlenecks and parallelization opportunities.

Load personas from `.clinerules/TNG/`. Read `devops-best-practices.md` and `github-actions-best-practices.md` before starting.

**geordi** (lead): analyse all `.github/workflows/` — parallel opportunities, redundant steps, cache misses, slow steps, timeout tuning. Propose changes with estimated time savings. Update `devops-best-practices.md`. Flag `[NEW DISCOVERY]`. End with handoff.
**crusher** supports: reliability risk of proposed optimisations.
**worf** supports: no security regression from optimisations.

picard delivers: prioritised change list (impact vs effort), safe-to-apply-now vs needs-testing, `devops-best-practices.md` updated. Close with **"Make it so!"**
