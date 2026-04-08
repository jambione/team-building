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

## Rules For Clean Structure

- Every handoff target in `.github/agents/*.agent.md` must map to a real agent file.
- `picard` `agents:` list must include all handoff targets used by `picard`.
- This topology file should be updated in the same PR as role or routing changes.
