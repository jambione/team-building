# GitHub Actions Best Practices

## Core Principles

- Simplicity and maintainability first.
- Security by default.
- Fast feedback loops with efficient caching.
- Reproducible and auditable workflows.

## Workflow Structure

- Use composite actions for reusable logic.
- Keep workflows in `.github/workflows/` and name them descriptively (e.g. `ci.yml`, `deploy-staging.yml`).
- Prefer YAML anchors and reusable workflows when possible.
- Use `concurrency` to prevent overlapping runs on the same branch.

## Security & Secrets

- Never hard-code secrets or tokens.
- Use `secrets.GITHUB_TOKEN` when possible instead of personal tokens.
- Require approval gates for production deployments.
- Enable dependency and code scanning.
- Use `permissions` block to follow least-privilege principle.

## Performance & Cost Optimization

- Cache aggressively (`actions/cache`, `setup-node` with cache, etc.).
- Use self-hosted runners only when necessary.
- Limit workflow triggers (use paths, branches, and types wisely).
- Use `matrix` strategy efficiently.

## Observability & Logging

- Always use structured logging when possible.
- Upload artifacts and test results for easy debugging.
- Add clear step names and summary outputs.

## Ethics & Responsibility

- geordi must prioritize security and reliability over speed when in conflict.
- All workflows must be reviewed for maintainability before merging.
- Never expose sensitive data in logs or artifacts.
- Document any non-obvious decisions in the knowledge base.

## Recommended Tools / Commands

- GitHub CLI (`gh`) for repository management
- `actions/checkout`, `actions/setup-node`, `actions/cache`, etc.
- Trivy, SonarQube, or CodeQL for scanning

geordi must always reference this document when working on GitHub Actions.
