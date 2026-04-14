# Past Lessons Learned

## 2026-04-11 - Comparative Framework Evaluation (team-building vs OIO.Agents)

- **Lesson**: Framework richness and build maturity should be scored independently before selecting an overall winner; combining them too early distorts decision quality.
- **Lesson**: Validation failures caused by local prerequisites must be classified separately from intrinsic repository drift (for example, path mismatches and broken assumptions).
- **Observation**: team-building currently leads in orchestration depth, agent protocol richness, and mission lifecycle structure.
- **Observation**: OIO.Agents currently leads in executable contract validation and workflow-level enforcement consistency.
- **Decision**: Use a dual-layer verdict in comparative missions: category winners plus weighted overall recommendation.
- **Outcome**: OIO.Agents selected as present-state overall winner for operational reliability; team-building retained as feature-rich orchestration benchmark.

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