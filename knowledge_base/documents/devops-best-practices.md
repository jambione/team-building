# DevOps Best Practices

## Current State

**As of**: 2026-04-05  
**Health**: GREEN  
**Top active item**: Graceful degradation pattern for third-party API dependencies in CI added (Sprint 1). Claude API rate-limit handling in burst windows deferred to Sprint 2 (CF-001).

---

## CI/CD & Pipelines

- Keep pipelines fast and reliable — target under 5 minutes for normal builds.
- Cache aggressively (dependencies, Docker layers, build artifacts).
- Always include security/vulnerability scanning (e.g., Trivy or similar).

## Docker & Containerization

- Use multi-stage builds to keep final images small.
- Minimize layers and use .dockerignore effectively.
- Run containers as non-root users where possible.

## General Rules

- Use Conventional Commits for all changes.
- Document deployment procedures clearly in the knowledge base.
- Prefer simple, understandable solutions over complex orchestration tools when they suffice.
- Monitor build times and flaky tests regularly.

## Lessons Applied Here

- Caching dependencies and Docker layers has repeatedly reduced build times by 50-65%.

---

## Artifact-Sharing Pattern for Multi-Job Pipelines

When a `prepare` job installs dependencies, subsequent jobs should not re-run `npm ci` independently. Even with npm cache, each job pays restore overhead and install time.

**Recommended pattern**: Upload `node_modules` as a workflow artifact in `prepare`; download in downstream jobs. Alternatively, use a deterministic, shared cache key so all jobs hit the same cache entry.

Re-running `npm ci` in every job has two costs: (1) ~25–45 seconds of redundant work per job, and (2) it obscures install failures by spreading them across jobs rather than surfacing them once in `prepare`.

## Lint Should Not Depend on Build

Static analysis (ESLint, type-check without emit) does not consume compiled output. Lint jobs must only depend on `prepare` (dependencies installed), not on `build`. Chaining lint behind build adds unnecessary latency to PR feedback. Parallelize build and lint after prepare.

---

## Dependabot for GitHub Actions

Pin GitHub Actions by major version tag (`@v4`) and configure Dependabot to watch for updates.

**Recommended `.github/dependabot.yml`**:

```yaml
version: 2
updates:
  - package-ecosystem: "github-actions"
    directory: "/"
    schedule:
      interval: "weekly"
      day: "monday"
```

Without Dependabot, pinned action versions become stale silently. A patched `actions/checkout@v4` will not be received unless someone manually updates the pin. This is the easiest supply-chain hygiene step available.

**Rule**: Any new workflow using an action must check that the ecosystem is covered by Dependabot before merging. If adding a new package ecosystem (npm, pip, docker), add a matching Dependabot entry simultaneously.

---

## Version History

```
2026-04-05: picard — Initial document
2026-04-12: geordi — Added artifact-sharing pattern and lint-vs-build dependency rule (Sprint Health Check findings G-1, G-2)
2026-04-12: geordi — Added Dependabot section (closes TD-003 documentation gap; dependabot.yml created in repo)
```
