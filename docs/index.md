# Documentation Index

Navigate all TNG Agent Team documentation here.

---

## Getting Started

| Document                                                         | Purpose                               | Audience                    |
| ---------------------------------------------------------------- | ------------------------------------- | --------------------------- |
| [docs/guides/SETUP.md](docs/guides/SETUP.md)                     | Complete setup and usage guide        | Everyone — read this first  |
| [docs/guides/QUICK-REFERENCE.md](docs/guides/QUICK-REFERENCE.md) | One-page command & workflow reference | Daily reference card        |
| [docs/guides/FEATURES.md](docs/guides/FEATURES.md)               | Detailed feature documentation        | Deep dive into capabilities |

---

## Quick Links

- **First time?** Start with [docs/guides/SETUP.md](docs/guides/SETUP.md)
- **Quick lookup?** Use [docs/guides/QUICK-REFERENCE.md](docs/guides/QUICK-REFERENCE.md)
- **Understand features?** Browse [docs/guides/FEATURES.md](docs/guides/FEATURES.md)

---

## Reference & Operations

| Document                       | Purpose                     | Location                                                           |
| ------------------------------ | --------------------------- | ------------------------------------------------------------------ |
| Team Topology (agents & roles) | Agent roster and routing    | [docs/reference/TEAM-TOPOLOGY.md](docs/reference/TEAM-TOPOLOGY.md) |
| Runbook (execution rules)      | Decision and execution flow | [docs/reference/RUNBOOK.md](docs/reference/RUNBOOK.md)             |
| Status (system health)         | Active agents and workflows | [docs/reference/STATUS.md](docs/reference/STATUS.md)               |

---

## Knowledge Base

All domain knowledge and team decisions are stored in `knowledge_base/`:

| Category            | Location                    | Purpose                                     |
| ------------------- | --------------------------- | ------------------------------------------- |
| **Architecture**    | `knowledge_base/documents/` | Design principles, ADRs, patterns           |
| **DevOps & CI/CD**  | `knowledge_base/documents/` | Workflow best practices, security hardening |
| **Reliability**     | `knowledge_base/documents/` | Observability, incident response, SLOs      |
| **Team Learning**   | `knowledge_base/documents/` | Lessons learned, past decisions             |
| **Session History** | `knowledge_base/sessions/`  | Timestamped mission records                 |
| **Archive**         | `knowledge_base/archive/`   | Historical sessions and assessments         |

Browse the full KB: [knowledge_base/documents/index.md](knowledge_base/documents/index.md)

---

## Agent Definitions

All agent personas are in `.github/agents/`:

| Agent           | File                                                                               | Role            |
| --------------- | ---------------------------------------------------------------------------------- | --------------- |
| picard          | [.github/agents/picard.agent.md](.github/agents/picard.agent.md)                   | Orchestrator    |
| picard-thinking | [.github/agents/picard-thinking.agent.md](.github/agents/picard-thinking.agent.md) | Deep analysis   |
| picard-fast     | [.github/agents/picard-fast.agent.md](.github/agents/picard-fast.agent.md)         | Quick execution |
| data            | [.github/agents/data.agent.md](.github/agents/data.agent.md)                       | Architecture    |
| riker           | [.github/agents/riker.agent.md](.github/agents/riker.agent.md)                     | First Officer   |
| geordi          | [.github/agents/geordi.agent.md](.github/agents/geordi.agent.md)                   | DevOps          |
| worf            | [.github/agents/worf.agent.md](.github/agents/worf.agent.md)                       | Security        |
| troi            | [.github/agents/troi.agent.md](.github/agents/troi.agent.md)                       | QA & UX         |
| crusher         | [.github/agents/crusher.agent.md](.github/agents/crusher.agent.md)                 | Reliability     |
| barclay         | [.github/agents/barclay.agent.md](.github/agents/barclay.agent.md)                 | Technical Debt  |
| guinan          | [.github/agents/guinan.agent.md](.github/agents/guinan.agent.md)                   | Memory          |
| obrien          | [.github/agents/obrien.agent.md](.github/agents/obrien.agent.md)                   | Observability   |
| wes             | [.github/agents/wes.agent.md](.github/agents/wes.agent.md)                         | Innovation      |

---

## System Configuration

| File                                                                         | Purpose                            |
| ---------------------------------------------------------------------------- | ---------------------------------- |
| [.github/copilot-instructions.md](.github/copilot-instructions.md)           | System initialization & activation |
| [.github/prompts/ready-room.prompt.md](.github/prompts/ready-room.prompt.md) | Ready Room protocol                |
| [.github/workflows/](<(.github/workflows/)>)                                 | CI/CD automation                   |

---

## Workspace Structure

```
team-building/                     ← Hub repo
├── README.md                       ← This file
├── docs/
│   ├── guides/                     ← User-facing guides
│   │   ├── SETUP.md               ← Full setup (read first)
│   │   ├── QUICK-REFERENCE.md     ← Command reference
│   │   └── FEATURES.md            ← Feature deep dives
│   └── reference/                  ← Operational reference
│       ├── TEAM-TOPOLOGY.md       ← Agent roster
│       ├── RUNBOOK.md             ← Execution rules
│       └── STATUS.md              ← System status
├── .github/
│   ├── agents/                     ← Agent personas (13 files)
│   ├── prompts/                    ← Protocol templates
│   └── workflows/                  ← CI/CD automation
└── knowledge_base/
    ├── documents/                  ← Domain KB (source of truth)
    ├── sessions/                   ← Mission session journals
    └── archive/                    ← Historical records
```

---

## Quick Commands

### Start a Mission

```
"Mission: [your objective]"
```

### Request Specific Agent

```
"@data — design a caching strategy"
```

### Check Carry-Forwards

```
"@guinan — what carry-forward items are open?"
```

### Open Ready Room Only

```
"Open the Ready Room for: [topic]"
```

---

## Need Help?

- **Setup questions?** See [docs/guides/SETUP.md](docs/guides/SETUP.md)
- **Command reference?** See [docs/guides/QUICK-REFERENCE.md](docs/guides/QUICK-REFERENCE.md)
- **Feature explanation?** See [docs/guides/FEATURES.md](docs/guides/FEATURES.md)
- **Agent details?** See `.github/agents/<name>.agent.md`
- **Operational flow?** See [docs/reference/RUNBOOK.md](docs/reference/RUNBOOK.md)
- **Knowledge base?** See [knowledge_base/documents/index.md](knowledge_base/documents/index.md)

---

**"Make it so."**
