---
# Team Quick Reference — Canonical First-Reference Guide

> **Purpose**: Distilled, action-oriented guidance for the most common decisions. Read this before domain docs.
> **Owner**: picard (updated quarterly; domain owners flag when their section is stale)
> **Deep references**: `knowledge_base/documents/` for full treatment; `knowledge_base/archive/` for historical context

---

## Agent Dispatch — When to Call Whom

| Need | Agent | Mandatory? |
|------|-------|-----------|
| Architecture or system design decision | data | Yes — any design |
| Security implications, secrets, permissions | worf | Yes — any external integration |
| CI/CD, GitHub Actions, Docker, infra | geordi | Yes — any pipeline change |
| Test strategy, QA, user experience | troi | Yes — any user-facing feature |
| Reliability, failure modes, edge cases | crusher | Yes — any resilience decision |
| Technical debt, DRY, maintainability | barclay | Yes — any refactor |
| Observability, metrics, alerting | obrien | Yes — any new system component |
| Historical context, prior decisions | guinan | Always first — every mission |
| Novel approaches, experiments | wes | Optional — exploratory missions |
| Execution coordination | riker | After [READY-ROOM-CLOSED] only |

**Parallel dispatch rule**: Ready Room analysts (all above except riker) run in a single parallel batch. Track C reviewers (worf, troi, crusher) run in a single parallel batch. Never call them sequentially when they can run simultaneously.

---

## Architecture Decisions — The Short List

1. **Simplicity first** — if the simple solution works, use it. Do not over-engineer.
2. **Composition over inheritance**
3. **Single Responsibility Principle** — everywhere, always
4. **CI step over webhook** for third-party integrations (lower operational surface)
5. **Graceful degradation for third-party APIs** — timeout at 60s, treat failure as warning not error
6. **Instrument before go-live** — metrics and alerts before a new system component ships, not after

---

## Security Non-Negotiables

1. All workflows must have explicit `permissions:` blocks — no implicit `write-all`
2. External API keys go in org-level secrets with environment protection gates — not repo secrets
3. `security-events: write` required for any step uploading SARIF results
4. Pin all third-party action versions and SDK versions; add to Dependabot
5. CodeQL requires: `init` → `autobuild` → `analyze` in sequence

---

## CI/CD — Proven Patterns

- Cache `node_modules` and Docker layers — reduces build time ~65%
- Rollback jobs need `fetch-depth: 0` on checkout (shallow clone lacks parent commit)
- AI review steps: scope to changed lines only (diff-aware) — better signal/noise, lower token cost
- Health-check polling loops over placeholder `echo` statements in deployment jobs

---

## Knowledge Base — How It Works

| Signal | Meaning |
|--------|---------|
| `[KB-UPDATED: <doc> \| Added: <specific content>]` | Agent updated a doc — content description is mandatory |
| `[KB-NO-CHANGE: <doc> \| reason: <brief>]` | Agent checked, nothing new to add |
| `[NEW DISCOVERY: <topic>]` | New knowledge surfaced — blocks mission close until KB doc updated |
| `[LEARNING-LOOP-VERIFIED: <slug>]` | picard confirmed all discoveries have matching KB updates |
| `[GUINAN-SYNTHESIZE: <slug>]` | Trigger for guinan to run cross-session synthesis |

**Quality standard**: A `[KB-UPDATED]` signal without a specific content description is invalid. "Updated the document" is not acceptable. Name what was added and why.

---

## Mission Lifecycle — At a Glance

```
[READY-ROOM-OPEN] → guinan (history) + picard KB reads [parallel]
                 → All analysts [single parallel batch]
                 → PRIORITY triage → MDR → [READY-ROOM-CLOSED]
                 → riker wave plan → Bridge execution [wave batches]
                 → Track C: worf + troi + crusher [single parallel batch]
                 → Go/No-Go → KB updates [single parallel batch]
                 → [LEARNING-LOOP-VERIFIED] → [GUINAN-SYNTHESIZE]
                 → Mission log + mission index → "Make it so!"
```

---

## Lessons Learned — Top Items

| Lesson | Source |
|--------|--------|
| Graceful degradation for third-party CI APIs: 60s timeout, failure = warning | `claude-api-pr-review` |
| Org-level secrets + environment protection for external API keys | `claude-api-pr-review` |
| Instrument latency/cost metrics before go-live, not after | `claude-api-pr-review` |
| Pin SDK versions and Dependabot at integration time | `claude-api-pr-review` |
| Test on real devices — emulators miss touch/layout issues | 2026-01-15 |
| Fetch Rally acceptance criteria before starting, not after | 2026-02-10 |

*Full list: `knowledge_base/documents/past-lessons-learned.md`*
