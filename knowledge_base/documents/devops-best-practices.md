# DevOps Best Practices

- Use multi-stage Docker builds to minimize image size.
- Always include security scanning (e.g., Trivy) in CI/CD pipelines.
- Cache aggressively (dependencies, Docker layers, build artifacts).
- Keep pipelines fast and reliable — aim for under 5 minutes for normal builds.
- Use Conventional Commits for all changes.
- Document deployment procedures clearly in the knowledge base.
- Prefer simple, understandable solutions over complex orchestration tools when they suffice.
