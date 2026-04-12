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

## Version History

```
2026-04-05: picard — Initial document
2026-04-12: geordi — Added artifact-sharing pattern and lint-vs-build dependency rule (Sprint Health Check findings G-1, G-2)
```
