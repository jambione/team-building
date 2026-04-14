# Past Lessons Learned

## 2026-04-12 – Sprint Health Check Second Pass

- **Lesson (KB drift is never fully closed in one pass)**: Three KB documents were corrected in the first health-check pass but still showed pre-improvement state when re-read this pass. Each health check should explicitly re-read every KB document it updated in prior passes and verify the content reflects reality — not just that the update was committed.
- **Lesson (Dependabot is a prerequisite, not an improvement)**: A repo with 7 workflows using pinned action versions and no Dependabot configuration is not hardened — it is frozen. TD-003 was High severity and sat open two sprints. Every repo should have `dependabot.yml` for `github-actions` ecosystem as a baseline requirement, added when the first workflow is written.
- **Lesson (Validate-workspace index check has a semantic gap)**: The `check_index_completeness` regex matches backtick-wrapped filenames anywhere in index.md, including the Pending Additions backlog. A file in the backlog satisfies the validator even though it is not in a table row. The check confuses *mentioned* with *indexed*. Future improvement: restrict the regex to table rows only, or move the "pending" section to a non-backtick format.
- **Decision**: AMBER held for second pass. All critical items from first pass confirmed resolved. Two High items remain (coverage gate, Dependabot). Dependabot created; coverage gate deferred to Sprint 2 close (2026-04-19).

## 2026-04-12 – Sprint Health Check (Full-Spectrum)

- **Lesson (KB-vs-Reality Drift)**: A checklist item marked `[x]` with a date is not evidence of implementation. `security-scan.yml` was recorded as implemented in 2026-04-05 KB entries but does not exist in the repository. Any KB checklist item referencing a file must include the file path as its verification criterion. If the file cannot be confirmed to exist, the item is not complete.
- **Lesson (CI gate failure is silent until you run the script)**: `STATUS.md` is required by `validate-agent-structure.py` but was never created. The `agent-structure-check.yml` workflow has been failing on every push and PR since it was introduced. Scripts that gate CI must be run manually at least once after creation to confirm they pass against the current repo state.
- **Lesson (deploy workflows are a prerequisite, not a follow-up)**: Documenting security requirements for deployment workflows (permissions, environment gates, rollback patterns) before the deployment workflows exist creates a false sense of security preparedness. Create the workflow skeleton — even a no-op — before documenting its security model.
- **Lesson (lint depends only on prepare, not build)**: Static analysis jobs (ESLint, type-check) do not consume compiled output. Chaining them behind `build` adds latency to every PR. Parallelize lint with build after the prepare step.
- **Pattern (KB index drift)**: 8 of 27 top-level KB documents are not indexed. The index is only useful if it is complete. Promote unindexed documents from lint warnings to lint errors so new documents cannot be added without indexing.
- **Decision**: All 15 findings logged in `team-health-assessment-github-agents.md`. Health rating downgraded GREEN → AMBER. Two critical items (missing `security-scan.yml`, missing `STATUS.md`) assigned to Sprint 3 immediate lane.

## 2026-04-11 – Code Review & Framework Health Assessment

- **Lesson**: Documentation reorganization requires prominent navigation update. When migrating user-facing docs to new structure, add explicit link from entry point (README.md).
- **Observation**: All GitHub Actions workflows were already well-hardened (no `write-all` usage); security practices established in Sprint 1 held firm.
- **Enhancement**: Added YAML docstring headers to all 13 agent files to guide new contributors on structure (`handoffs:`, `agents:`, `tools:` fields).
- **Reliability Improvement**: Implemented agent availability check at system startup to catch missing agent files before mission execution fails.
- **Process**: KB backup procedures documented in RUNBOOK.md to ensure disaster recovery is clear for future operators.
- **Decision**: Deferred 4 P3 enhancements (validation script unification, unit tests, lightweight journal, KB quick-start) to Sprint 3 — all P1/P2 items resolved during execution.
- **Result**: Mission health: GREEN. All roadblocks cleared. 9 P2 items resolved in single sprint review mission.

## 2026-04-05 – CI/CD Pipeline Sprint 1 Remediation

- **Lesson**: Omitting `permissions:` blocks in GitHub Actions workflows defaults to `write-all` token scope — a critical security misconfiguration that exposes the entire repo to any compromised action or step.
- **Lesson**: `cache: 'actions/cache'` is not a valid value for `actions/setup-node`; the correct value is `cache: 'npm'`. Always verify action input schemas against official documentation.
- **Lesson**: CodeQL requires a precise 3-step sequence: `init` → `autobuild` → `analyze`. Using only `upload-artifact` is not a substitute and produces no security analysis whatsoever.
- **Lesson**: Rollback jobs using `git rev-parse HEAD^1` require `fetch-depth: 0` on the checkout step. The default shallow clone will not have the parent commit available, causing rollback to fail at the worst possible moment.
- **Lesson**: `security-events: write` is the specific GitHub token permission required for any workflow step that uploads SARIF results (Trivy, CodeQL). Without it, scan results silently fail to appear in the Security tab.
- **Decision**: All deployment workflows now use real rsync+SSH+systemctl logic with health-check polling loops rather than placeholder `echo` statements.
- **Outcome**: All 13 critical/high/medium issues from the Sprint 1 remediation plan resolved in a single mission. Health rating upgraded from AMBER to GREEN.

## 2026-04-04 – Dark Mode Implementation (New)

- **Lesson**: Using CSS variables + a single `dark` class on `<html>` is far simpler and more maintainable than multiple theme providers or context-heavy solutions.
- **Decision**: Store user preference in both localStorage (for instant UI) and backend profile (for persistence).

## 2026-04-04 – Login Component with Mobile Optimization (New)

- **Lesson**: Implementing mobile-specific components requires careful validation and testing on real devices to ensure usability.
- **Decision**: Use a simple, maintainable approach with clear error handling and mobile-friendly form layout.
- **Outcome**: Good performance and easy future extensions. Code follows clean architecture principles.

## 2026-03-20 – Dark Mode Implementation

- **Lesson**: Using CSS variables + a single `dark` class on `<html>` is far simpler and more maintainable than multiple theme providers or context-heavy solutions.
- **Decision**: Store user preference in both localStorage (for instant UI) and backend profile (for persistence).

## 2026-02-28 – CI/CD Performance Issues

- **Problem**: Long build times due to repeated dependency installation.
- **Solution**: Added proper caching for `node_modules` and Docker layers.
- **Result**: Build time reduced by ~65%. Always evaluate caching early.

## 2026-02-10 – Rally Story Handling

- **Lesson**: Always fetch and carefully review full acceptance criteria from Rally before starting implementation.
- **Outcome**: Significantly reduced scope creep and rework.

## 2026-01-15 – Mobile Bug Example

- **Lesson**: Test on real devices early — emulators can miss subtle layout and touch issues.
