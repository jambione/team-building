# Workspace Topology

> Single source of truth for all repos in this workspace. picard reads this before opening any Ready Room to understand service boundaries and inter-repo dependencies.
> Updated by picard when repos are added, deprecated, or re-scoped.

**Owner**: picard  
**Last Updated**: 2026-04-11

---

## Hub

| Repo | Role | Primary Owner | Notes |
|------|------|---------------|-------|
| `team-building` | **Workspace Hub** — all agent definitions, KB, mission history, session journals live here | picard | Never used as a deployment target; agents are always loaded from this repo |

---

## Spoke Repos

> Add a row here for every service/codebase in the workspace. Each spoke repo should contain a `.tng-context.md` file in its root that mirrors this entry.

| Repo | Service Domain | Owner Agent | Depends On | Status | Notes |
|------|---------------|-------------|------------|--------|-------|
| _(add spoke repos here)_ | | | | | |

**Example format:**
```
| `org/service-api`    | Backend REST API       | data    | `org/service-db`    | active     | Primary API surface |
| `org/service-ui`     | Frontend React app     | troi    | `org/service-api`   | active     | User-facing product |
| `org/service-db`     | Database migrations    | data    | —                   | active     | Schema ownership    |
| `org/service-infra`  | Terraform / IaC        | geordi  | —                   | active     | Cloud infrastructure|
| `org/service-auth`   | Auth service           | worf    | —                   | deprecated | Migrating to service-api v2 |
```

---

## Inter-Repo Dependency Map

> Use this section to document which repos must be coordinated when making changes. For loosely coupled repos, most missions will be single-repo. Only document real runtime or build-time dependencies here.

| Upstream Repo | Downstream Repo | Dependency Type | Notes |
|---------------|-----------------|-----------------|-------|
| _(add when known)_ | | | |

**Dependency types:**
- `api-contract` — downstream calls upstream's API; breaking changes require coordination
- `shared-lib` — downstream imports a package published by upstream
- `build-order` — downstream's CI must build after upstream (e.g., base Docker images)
- `data-schema` — downstream reads a database or data store owned by upstream
- `config` — downstream reads configuration/secrets provisioned by upstream

---

## Workspace Routing Rules

When picard opens a Ready Room, determine the `current_repo` using this priority order:

1. **Explicit declaration**: User or requester states which repo the mission is for.
2. **`.tng-context.md` present**: If the AI agent is invoked from inside a spoke repo with a `.tng-context.md`, that repo is `current_repo`.
3. **Inferred from mission type**: Architecture decisions → check `data`'s domain in this table. Security audit → check `worf`'s assigned repos.
4. **Default**: If no repo can be determined, picard asks before proceeding.

---

## Workspace Conventions

- **One MDR per repo**: When a mission touches multiple repos, picard opens sequential Mission Decision Records — one per affected repo — not a combined MDR. This keeps KB updates, issue creation, and session journals cleanly scoped.
- **Cross-repo coordination**: If repo-A must change before repo-B, riker sequences waves accordingly: Wave 1 = repo-A tasks, Wave 2 = repo-B tasks (gated on Wave 1 completion). Document the dependency in the session journal's `Cross-Repo Dependencies` field.
- **Issue targeting**: MDR signals include `Target-Repo: <owner>/<repo>` when the tracking issue should be created in a spoke repo, not the hub.
- **Spoke repo identification**: Every spoke repo should have `.tng-context.md` in its root (see template). Agents read this to orient themselves when invoked in an unfamiliar repo.

---

## Fluid Workspace — Repos Come and Go

The workspace is intentionally fluid. Repos can be added or removed at any time without breaking active missions. The system handles this via **auto-discovery** and **graceful removal**.

### Auto-Discovery: Adding a Repo

When picard encounters a repo during mission orientation that is **not yet listed** in the Spoke Repos table above, it does the following:

1. If the repo has a `.tng-context.md`, read it — this is a self-declaring spoke repo.
2. If no `.tng-context.md` exists, picard treats the repo as `unregistered` and asks the user to confirm whether to register it before proceeding.
3. Once confirmed, picard adds a row to this file (Spoke Repos table) and updates `knowledge_base/current/workspace-context.md`.
4. Emit: `[GUINAN-SYNTHESIZE: workspace-onboarding-<repo-name>]` so guinan can start tracking context from scratch for this repo.

**No manual setup required**: placing a `.tng-context.md` in a repo is sufficient for the team to recognise it.

### Graceful Removal: Removing a Repo

When a spoke repo is no longer in the workspace (deleted, archived, transferred, or out of scope), the team handles it without disrupting the hub:

1. picard marks the repo `status: removed` (not deleted from the table — history is preserved).
2. Any **open carry-forward items** from that repo are marked `[REPO-REMOVED]` and escalated to picard for disposition: cancel, migrate to another repo, or park in `knowledge_base/archive/`.
3. Any **active missions** targeting the removed repo are closed with status `cancelled` and a note in the mission log.
4. The repo remains in the mission index as historical record — missions don't get erased.
5. `knowledge_base/current/workspace-context.md` `Active Repos` list is updated immediately.

**Graceful rule**: agents encountering a removed repo in historical context simply skip it — they do not error or halt the current mission.

### Adding a New Spoke Repo (manual)

1. Add a row to the **Spoke Repos** table above.
2. Add rows to the **Inter-Repo Dependency Map** if applicable.
3. Copy `.tng-context.md` template into the new repo's root and fill it out.
4. Update `knowledge_base/current/workspace-context.md` to include the new repo in `active_repos`.
5. Notify guinan: `[GUINAN-SYNTHESIZE: workspace-onboarding-<repo-name>]`.

### Deprecating a Spoke Repo (manual)

1. Change the repo's `Status` column to `deprecated` or `removed`.
2. Add a `deprecated_at` date in the Notes column.
3. Remove from `knowledge_base/current/workspace-context.md` `active_repos` list.
4. Carry any open missions forward with `[EXTERNAL-EVENT: repo-removed | picard | Repo <name> removed from workspace | severity: significant]`.
