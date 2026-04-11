# Team Topology v2

This file is the single source of truth for agent roles and handoffs.

## Orchestrator

- `picard`: primary coordinator and final decision owner.
- `picard-thinking`: deep analysis mode for architecture, risk, and trade-offs.
- `picard-fast`: execution mode for straightforward, low-risk tasks after decision lock.

## Specialists

- `data`: architecture and system design.
- `riker`: execution coordination.
- `geordi`: CI/CD and DevOps implementation.
- `worf`: security and compliance review.
- `troi`: QA, UX, and testing strategy.
- `crusher`: reliability and failure-mode analysis.
- `barclay`: technical debt and maintainability.
- `guinan`: historical context and cross-session memory.
- `obrien`: observability, metrics, and operations.
- `wes`: exploratory proposals (approval required before implementation).

## Canonical Routing

- Design and architecture -> `data`
- Delivery orchestration -> `riker`
- Workflow automation -> `geordi`
- Security and controls -> `worf`
- Test strategy and quality -> `troi`
- Reliability and resiliency -> `crusher`
- Debt and simplification -> `barclay`
- Historical context -> `guinan`
- Monitoring and alerting -> `obrien`
- Novel options and experiments -> `wes`

## Workspace Routing

When a mission targets a spoke repo (not the hub), picard determines the routing context at mission start:

1. Read `knowledge_base/current/workspace-context.md` to get `current_repo`.
2. If the spoke repo has `.tng-context.md`, read it to find the `owner_agent` override.
3. Use `WORKSPACE-TOPOLOGY.md` to check inter-repo dependencies before Ready Room opens.
4. All canonical routing above still applies — the owner agent for a spoke domain leads that section of the Ready Room.

**Example**: If `current_repo = org/service-ui` and `.tng-context.md` names `troi` as owner, troi leads the Ready Room analysis for UI concerns; worf still owns security, geordi still owns CI/CD.

## Rules For Clean Structure

- Every handoff target in `.github/agents/*.agent.md` must map to a real agent file.
- `picard` `agents:` list must include all handoff targets used by `picard`.
- This topology file should be updated in the same PR as role or routing changes.
- `WORKSPACE-TOPOLOGY.md` is the source of truth for which repos exist; update it when repos are added or deprecated.
