# TNG Agent Team — Multi-Agent Orchestration Framework

**A structured, collaborative workflow for complex software engineering tasks.**

Version 2.2 | Last updated: 2026-04-11

A sophisticated multi-agent system modeled after Star Trek: The Next Generation. Rather than working alone, you work _with_ a team of 13 specialized agents that analyze, decide, execute, and review your work — all with explicit handoffs and full history tracking.

---

---

## 📚 Documentation Hub

**👉 [Browse All Documentation](docs/index.md)** — Complete navigation for guides, reference, and knowledge base.

### Quick Start

1. **New to TNG?** Start here: [docs/guides/SETUP.md](docs/guides/SETUP.md)
2. **Need quick commands?** See: [docs/guides/QUICK-REFERENCE.md](docs/guides/QUICK-REFERENCE.md)
3. **Feature deep-dives?** Check: [docs/guides/FEATURES.md](docs/guides/FEATURES.md)

---

## 📖 Documentation

| Type           | Document                                                               | Purpose                                     |
| -------------- | ---------------------------------------------------------------------- | ------------------------------------------- |
| **Guides**     | [docs/guides/SETUP.md](docs/guides/SETUP.md)                           | Complete setup and usage guide (read first) |
|                | [docs/guides/QUICK-REFERENCE.md](docs/guides/QUICK-REFERENCE.md)       | One-page command cheat sheet                |
|                | [docs/guides/FEATURES.md](docs/guides/FEATURES.md)                     | Feature deep dives and explanations         |
| **Reference**  | [docs/reference/TEAM-TOPOLOGY.md](docs/reference/TEAM-TOPOLOGY.md)     | Agent roster and routing rules              |
|                | [docs/reference/RUNBOOK.md](docs/reference/RUNBOOK.md)                 | Execution guidelines for team               |
|                | [docs/reference/STATUS.md](docs/reference/STATUS.md)                   | System activation status                    |
| **Navigation** | [docs/index.md](docs/index.md)                                         | Full documentation index                    |
| **Knowledge**  | [knowledge_base/documents/index.md](knowledge_base/documents/index.md) | All KB documents navigation                 |

---

## 🎭 What Is TNG Agent Team?

The TNG Agent Team is a multi-agent orchestration framework modeled after Star Trek: The Next Generation. It guides complex software engineering work through **structured, collaborative decision-making and execution**.

### Core Features

- **🤖 13 Specialized Agents** — Each with distinct expertise (architecture, security, DevOps, QA, reliability, tech debt, memory, etc.)
- **📋 4-Phase Workflow** — Ready Room (decisions) → Bridge (execution) → Track C (review) → Close (learning)
- **📚 Institutional Memory** — guinan remembers all prior sessions and surfaces relevant history automatically
- **🔒 Security-First** — Mandatory security reviews (worf) before production deployment
- **📊 Observable** — All decisions, risks, and outcomes are logged for future reference
- **🚁 Multi-Service Support** — Handle multiple repos (hub + spokes) with single agent knowledge base

### Key Philosophy

> **No code is written until the Ready Room closes.**

Decisions are made collaboratively _before_ implementation begins. Risks are identified. Options are weighed. Once the Mission Decision Record is locked, execution is fast and coordinated.

---

## 🚀 Getting Started in 30 Seconds

### 1. Open Copilot Chat

```
Press Ctrl+Shift+I (Windows/Linux) or Cmd+Shift+I (Mac)
```

### 2. State Your Mission

```
"Mission: [your objective here]"
```

Example:

```
"Mission: Add JWT expiry validation to our authentication middleware"
```

### 3. Sit Back and Watch

The system automatically:

- Analyzes your mission (guinan surfaces history)
- Gathers crew input (parallel expert analysis)
- Locks decisions (Mission Decision Record)
- Coordinates execution (riker leads)
- Validates quality (3 review gates)
- Captures learning (session journal + KB updates)

---

## 🎯 Common Missions

- **Architecture & Design** → `@data — design [component]`
- **CI/CD & DevOps** → `@geordi — review our workflows`
- **Security & Compliance** → `@worf — audit our token permissions`
- **QA & Testing** → `@troi — design a test strategy`
- **Reliability** → `@crusher — analyze failure modes`
- **Technical Debt** → `@barclay — identify refactoring opportunities`
- **History & Context** → `@guinan — what is the history here?`
- **Exploring Ideas** → `@wes — propose unconventional solutions`

Or start a **full mission**:

```
"Mission: Integrate Claude API into CI pipeline for automated PR reviews"
```

---

## 📁 Project Structure

```
team-building/               ← Hub repo
├── README.md                ← You are here
├── docs/                    ← User documentation
│   ├── guides/              ← Getting started & feature docs
│   │   ├── SETUP.md        ← Full setup guide (read first)
│   │   ├── QUICK-REFERENCE.md
│   │   └── FEATURES.md
│   ├── reference/           ← Operational reference
│   │   ├── TEAM-TOPOLOGY.md
│   │   ├── RUNBOOK.md
│   │   └── STATUS.md
│   └── index.md             ← Full navigation
├── .github/
│   ├── agents/              ← 13 agent definitions
│   ├── prompts/             ← Protocol templates
│   └── workflows/           ← CI/CD automation
├── knowledge_base/          ← Team KB (source of truth)
│   ├── documents/           ← Domain KB docs
│   ├── sessions/            ← Session journals
│   └── archive/             ← Historical records
└── scripts/                 ← Validation & utilities
```

---

## 👥 The Crew (13 Agents)

| Agent               | Role                        | Badge  | When to Use                  |
| ------------------- | --------------------------- | ------ | ---------------------------- |
| **picard**          | Orchestrator & captain      | 🔴★★★★ | Primary coordinator          |
| **data**            | Architecture & design       | 🟡★★☆  | System design decisions      |
| **riker**           | First Officer/execution     | 🔴★★★  | Coordinating tasks           |
| **geordi**          | DevOps & CI/CD              | 🟡★★☆  | GitHub Actions, Docker       |
| **worf**            | Security & compliance       | 🟡★★☆  | Token permissions, secrets   |
| **troi**            | QA & testing                | 🔵★★☆  | Test strategy, quality gates |
| **crusher**         | Reliability & failure modes | 🔵★★★  | Edge cases, rollback         |
| **barclay**         | Technical debt              | 🟡★★   | Refactoring, maintainability |
| **guinan**          | Institutional memory        | ⚪☆☆   | Historical context           |
| **obrien**          | Observability & ops         | 🟡★    | Monitoring, metrics          |
| **wes**             | Exploratory proposals       | ⚡★☆   | Unconventional solutions     |
| **picard-thinking** | Deep analysis mode          | ⚫★★★  | Complex decisions            |
| **picard-fast**     | Bridge execution mode       | 🟢★★   | Fast, low-risk tasks         |

---

## 🔄 The 4-Phase Workflow

### Phase 1: Ready Room (Decisions)

- picard opens the Ready Room
- guinan surfaces relevant history
- All agents analyze in parallel
- Decision record is locked
- No code written yet

### Phase 2: Bridge Execution (Implementation)

- riker coordinates crew
- Each agent executes their task
- Explicit handoffs with acknowledgment
- Work tracked and logged

### Phase 3: Track C Review (Quality Gates)

- Security (worf), QA (troi), Reliability (crusher)
- Each issues VERDICT: PASS / CONDITIONAL / FAIL
- picard issues Go/No-Go

### Phase 4: Mission Close (Learning)

- KB documents updated
- Session journal captured
- Debrief recorded
- Next mission benefits from this history

---

## 🎓 Learning Resources

### For First-Time Users

1. Read [docs/guides/SETUP.md](docs/guides/SETUP.md) (20 min)
2. Run your first mission (30-60 min)
3. Review session journal at `knowledge_base/sessions/`

### For Quick Reference

- [docs/guides/QUICK-REFERENCE.md](docs/guides/QUICK-REFERENCE.md) — Commands & patterns (bookmark this)
- [docs/guides/FEATURES.md](docs/guides/FEATURES.md) — Feature deep-dives

### For Team Members

- [docs/reference/RUNBOOK.md](docs/reference/RUNBOOK.md) — Execution guidelines
- [docs/reference/TEAM-TOPOLOGY.md](docs/reference/TEAM-TOPOLOGY.md) — Team structure
- [knowledge_base/documents/](knowledge_base/documents/) — Domain KB

---

## ⚙️ Configuration

### Prerequisites

- VS Code with GitHub Copilot Chat extension
- Git
- This `team-building` hub repo

### Activation

1. Open the `team-building` folder in VS Code
2. Open Copilot Chat (`Ctrl+Shift+I` / `Cmd+Shift+I`)
3. Wait for initialization
4. See: _"Tea. Earl Grey. Hot. — the crew is assembled."_

### Spoke Repos (Multi-Service)

Use [`.tng-context.md`](.tng-context.md) in a spoke repo when you want repo-local auto-routing metadata. If omitted, picard falls back to [knowledge_base/current/workspace-context.md](knowledge_base/current/workspace-context.md) and asks for confirmation when context is ambiguous.

### Workspace Config Layer

- [`workspace-config.json`](workspace-config.json) defines reusable validation and topology intent (required files, workflow assertions, deterministic validation sections).
- [`scripts/workspace_config.py`](scripts/workspace_config.py) is the shared loader used by workspace validators.

---

## 📊 Knowledge Base

The KB is the source of truth for team decisions and learning:

| Category         | Documents                                       | Owner   |
| ---------------- | ----------------------------------------------- | ------- |
| **Architecture** | Principles, ADRs, patterns, coding standards    | data    |
| **DevOps**       | CI/CD setup, GitHub Actions, security hardening | geordi  |
| **Development**  | Best practices, team conventions, onboarding    | picard  |
| **Operations**   | Monitoring, incident response, playbooks        | obrien  |
| **Reliability**  | Failure modes, rollback procedures              | crusher |
| **Debt**         | Technical debt register, refactoring priorities | barclay |
| **Memory**       | Past lessons, session journals, carry-forwards  | guinan  |

See [knowledge_base/documents/index.md](knowledge_base/documents/index.md) for full navigation.

---

## 🔒 Security & Compliance

- **GitHub Token Scoping** — Minimal permissions per workflow type
- **Secrets Management** — Uses GitHub Secrets, never hardcoded
- **Security Reviews** — Mandatory worf review before production
- **Compliance** — SOC 2, ISO, HIPAA checkpoints in Track C

See [knowledge_base/documents/github-actions-security-hardening.md](knowledge_base/documents/github-actions-security-hardening.md) for security matrix.

---

## 📝 Example Missions

### 1. Quick Feature Review

```
"@data — design a caching strategy for our checkout endpoints"
```

### 2. Full Mission: Security Audit

```
"Mission: Audit our GitHub Actions workflows for security compliance
including token scoping, secrets management, and SARIF uploads."
```

### 3. Full Mission: Architecture Decision

```
"Mission: Evaluate pros/cons of migrating from monolith to microservices.
Scope: API, not mobile. Constraints: backward compatibility required."
```

### 4. Full Mission: Technical Debt

```
"Mission: Identify and prioritize technical debt in our CI pipeline
that's blocking automation improvements in the next quarter."
```

---

## 🐛 Troubleshooting

| Issue                           | Fix                                                                                  |
| ------------------------------- | ------------------------------------------------------------------------------------ |
| "Crew not assembled"            | Verify agent files in `.github/agents/`. Restart VS Code.                            |
| Copilot Chat not opening        | Install GitHub Copilot Chat extension. Restart VS Code.                              |
| Ready Room won't close          | Resolve all P1 priority items. Type: `"picard, what's blocking closure?"`            |
| Missing history (guinan silent) | Check `past-lessons-learned.md` has recent entries. Session journals must be closed. |

See [docs/guides/SETUP.md](docs/guides/SETUP.md#9-troubleshooting) for more troubleshooting.

---

## 📞 Getting Help

| Question                           | Resource                                                               |
| ---------------------------------- | ---------------------------------------------------------------------- |
| "How do I use this?"               | [docs/guides/SETUP.md](docs/guides/SETUP.md)                           |
| "What command...?"                 | [docs/guides/QUICK-REFERENCE.md](docs/guides/QUICK-REFERENCE.md)       |
| "How does [feature] work?"         | [docs/guides/FEATURES.md](docs/guides/FEATURES.md)                     |
| "What's our policy on [domain]?"   | [knowledge_base/documents/index.md](knowledge_base/documents/index.md) |
| "What happened in prior missions?" | [knowledge_base/sessions/](knowledge_base/sessions/)                   |

---

## 🎬 Next Steps

1. **Read** [docs/guides/SETUP.md](docs/guides/SETUP.md) (20 minutes)
2. **Run** your first mission (30-60 minutes)
3. **Review** your session journal (5 minutes)
4. **Bookmark** [docs/guides/QUICK-REFERENCE.md](docs/guides/QUICK-REFERENCE.md) (fast lookup)

---

**"Make it so."**
