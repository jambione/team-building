# IT Agent Team Playbook

## Core Principles

- Simplicity first, then performance, maintainability, and operational excellence.
- Single responsibility everywhere.
- All work must be driven by accurate Rally requirements.
- kirk is the single orchestrator. Every specialist must stay strictly in their lane.
- Use parallel execution when tasks are independent.
- Maintain and consult the shared knowledge base at `knowledge_base/documents/`.

## Standard Workflow (kirk enforces)

1. Gather Requirements → kc-rally
2. Check Knowledge Base (`knowledge_base/documents/`)
3. Architecture → spock (when needed)
4. Parallel Implementation → sulu, chekov
5. DevOps & Automation + Git → scotty, kc-git
6. Comprehensive QA → bones (parallel)
7. Final Review, Integration & Polish → kirk
8. Reflect & Improve → suggest additions to the knowledge base

Every specialist must return results to kirk in clear, structured format and hand control back.
