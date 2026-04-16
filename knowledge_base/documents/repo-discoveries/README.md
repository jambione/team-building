# Repo Discoveries

## Purpose

Per-repo living documents that capture **everything the crew learns** about a spoke repo through missions — feature locations, service purposes, architecture patterns, build/test commands, integration points, and gotchas.

Unlike `past-lessons-learned.md` (team-wide patterns) or `session-continuity.md` (cross-session handoff), repo discovery docs are **repo-specific and cumulative**. They grow richer with every mission and serve as the crew's institutional memory about each codebase.

---

## Ownership

**data** owns all repo discovery documents. Other agents contribute findings via `[NEW DISCOVERY: repo:<current_repo>]` tags; data incorporates them.

---

## When to Create

- **New repo enters workspace**: When guinan detects no repo discovery doc exists for `current_repo` during Ready Room context-retrieval, guinan flags it as `[NEW DISCOVERY]`. data bootstraps a skeleton from available sources (`.tng-context.md`, `.github/copilot-instructions.md`, or crew exploration).
- **Two-pass approach**: data creates a skeleton during the Ready Room (so analysts have a shared reference), then enriches it at mission close with everything learned during execution.

## When to Update

- **Every mission that touches the repo**: data updates the Feature Map and Mission Discovery Log at minimum.
- **Significant architectural findings**: New patterns, dependency chains, integration points, or gotchas discovered during any phase.

---

## Template

Use `_template.md` in this directory. Copy it to `<repo-name>.md` and populate.

### Required Sections

1. **Overview** — Repo identity, tech stack, domain
2. **Feature Map** — Table of explored feature areas with locations and key components
3. **Architecture Discoveries** — Patterns and design decisions, organized by feature area
4. **Integration Points** — Cross-service calls, shared libraries, external deps
5. **Build & Test** — Commands, watch modes, config locations learned
6. **Gotchas & Pitfalls** — Non-obvious behaviors and environment quirks
7. **Mission Discovery Log** — Rolling record of what was learned per mission

---

## Naming Convention

```
<repo-name>.md
```

Use the exact repo name as it appears in `workspace-context.md` and `WORKSPACE-TOPOLOGY.md`.

---

## Review Cadence

Every mission that touches the repo (same cadence as `past-lessons-learned.md`).

---

_Managed by data (architecture specialist) | Created: 2026-04-16_
