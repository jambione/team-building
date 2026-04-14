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
