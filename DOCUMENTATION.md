# TNG Agent Team — Documentation Navigation Map

**Complete index of all project documentation. Start here to find what you need.**

---

## 🎯 Choose Your Path

### I'm Brand New to TNG
1. **Read** [README.md](README.md) (2 min) — Project overview
2. **Read** [FIRST-MISSION.md](FIRST-MISSION.md) (15 min) — Step-by-step tutorial
3. **Run** your first mission (30-60 min) — Get hands-on experience
4. **Bookmark** [QUICK-REFERENCE.md](QUICK-REFERENCE.md) — For fast lookups

### I Want to Use TNG Right Now
1. **Read** [QUICK-REFERENCE.md](QUICK-REFERENCE.md) (3 min) — Commands at a glance
2. **Open Copilot Chat** and state your mission
3. **Reference** [SETUP.md](SETUP.md) if you hit a snag

### I Want to Understand Everything
1. **Read** [README.md](README.md) (overview)
2. **Read** [SETUP.md](SETUP.md) (complete guide)
3. **Read** [FEATURES.md](FEATURES.md) (deep dives)
4. **Browse** [knowledge_base/documents/](knowledge_base/documents/) (domain knowledge)

### I'm Setting Up a New Spoke Repo
1. **Read** [SETUP.md — Section 5: Spoke Repos](SETUP.md#5-spoke-repos--using-tng-in-your-services)
2. **Copy** [`.tng-context.md`](.tng-context.md) to your repo
3. **Fill out** the metadata
4. **Run** a mission in your repo (picard auto-routes)

### I'm Managing the Team/Hub
1. **Review** [TEAM-TOPOLOGY.md](TEAM-TOPOLOGY.md) — Routing and roles
2. **Review** [STATUS.md](STATUS.md) — Workflow status
3. **Review** [RUNBOOK.md](RUNBOOK.md) — Execution guidelines
4. **Manage** [knowledge_base/documents/sprint-state.md](knowledge_base/documents/sprint-state.md) — Carry-forwards

---

## 📚 Documentation by Purpose

### Getting Started
| Document | Purpose | Time | Audience |
|----------|---------|------|----------|
| [README.md](README.md) | Project overview, feature list | 5 min | Everyone |
| [FIRST-MISSION.md](FIRST-MISSION.md) | Step-by-step walkthrough | 15 min + 30-60 min mission | New users |
| [QUICK-REFERENCE.md](QUICK-REFERENCE.md) | Command cheat sheet, one-pager | 3 min | Daily reference |

### Complete Reference
| Document | Purpose | Time | Audience |
|----------|---------|------|----------|
| [SETUP.md](SETUP.md) | Full setup, features, best practices, troubleshooting | 30 min | Full reference |
| [FEATURES.md](FEATURES.md) | Deep documentation of 12 system features | 20 min | Understanding capability |
| [RUNBOOK.md](RUNBOOK.md) | Decision gates, execution guidelines | 5 min | Workflow reference |

### Team Structure & Governance
| Document | Purpose | Time | Audience |
|----------|---------|------|----------|
| [TEAM-TOPOLOGY.md](TEAM-TOPOLOGY.md) | Agent roster, routing, team structure | 5 min | Team members |
| [STATUS.md](STATUS.md) | Workflow activation, agent status | 2 min | Monitoring |
| [knowledge_base/documents/index.md](knowledge_base/documents/index.md) | KB document navigation | 5 min | Finding knowledge |

### Domain Knowledge (Knowledge Base)
| Category | Documents | Owner | Update Cadence |
|----------|-----------|-------|-----------------|
| **Architecture & Design** | [principles](knowledge_base/documents/architecture-principles.md), [ADRs](knowledge_base/documents/architecture-decision-records.md), [patterns](knowledge_base/documents/system-design-patterns.md), [standards](knowledge_base/documents/coding-standards.md) | data | Quarterly + per decision |
| **DevOps & CI/CD** | [ci-cd-recommendations](knowledge_base/documents/ci-cd-pipeline-recommendations.md), [devops-best-practices](knowledge_base/documents/devops-best-practices.md), [gh-actions-bp](knowledge_base/documents/github-actions-best-practices.md), [security-hardening](knowledge_base/documents/github-actions-security-hardening.md) | geordi | Quarterly + per change |
| **Operations & Reliability** | [monitoring-observability](knowledge_base/documents/monitoring-observability.md), [incident-response](knowledge_base/documents/incident-response-playbook.md) | crusher, obrien | Quarterly + per incident |
| **Team Practices** | [best-practices](knowledge_base/documents/best-practices.md), [conventions](knowledge_base/documents/team-conventions.md), [onboarding](knowledge_base/documents/onboarding-guide.md) | picard | Quarterly |
| **Learning & State** | [past-lessons](knowledge_base/documents/past-lessons-learned.md), [sprint-state](knowledge_base/documents/sprint-state.md), [performance-log](knowledge_base/documents/agent-performance-log.md) | picard, guinan | Per mission + weekly |
| **Technical Debt** | [tech-debt-register](knowledge_base/documents/tech-debt-register.md) | barclay | Quarterly + per sprint |

---

## 🗂️ File Location Reference

### Top-Level Documentation
```
team-building/
├── README.md               ← Start here (project overview)
├── QUICK-REFERENCE.md      ← Fast lookup (one-pager)
├── SETUP.md                ← Full guide (setup, features, best practices)
├── FEATURES.md             ← Feature deep-dives
├── FIRST-MISSION.md        ← Step-by-step tutorial
├── RUNBOOK.md              ← Execution guidelines
├── TEAM-TOPOLOGY.md        ← Agent roster & routing
├── STATUS.md               ← Workflow status
└── .tng-context.md         ← Spoke template
```

### Agent Definitions
```
.github/agents/
├── picard.agent.md
├── picard-fast.agent.md
├── picard-thinking.agent.md
├── data.agent.md
├── riker.agent.md
├── geordi.agent.md
├── worf.agent.md
├── troi.agent.md
├── crusher.agent.md
├── barclay.agent.md
├── guinan.agent.md
├── obrien.agent.md
├── wes.agent.md
└── PLAYBOOK.md             ← Team protocol & handoffs
```

### Prompts & Workflows
```
.github/
├── prompts/
│   ├── ready-room.prompt.md
│   ├── pr-review.prompt.md
│   ├── security-audit.prompt.md
│   └── ...
└── workflows/
    ├── ci.yml
    ├── adr-workflow.yml
    └── ...
```

### Knowledge Base
```
knowledge_base/
├── documents/              ← KB documents (source of truth)
│   ├── architecture-*.md
│   ├── devops-*.md
│   ├── best-practices.md
│   ├── past-lessons-learned.md
│   ├── sprint-state.md
│   └── index.md            ← KB navigation
├── sessions/               ← Session journals (one per mission)
│   ├── YYYY-MM-DD-HH-*.md
│   ├── mission-debrief-template.md
│   └── session-template.md
├── archive/                ← Historical records
└── current/                ← Real-time team state
```

---

## 🔗 Common Document Links

### Want to Understand...

**How the workflow works?**
- [FEATURES.md — Feature 2: Structured 4-Phase Workflow](FEATURES.md#feature-2-structured-4-phase-workflow)
- [SETUP.md — Section 2: Quick Start](SETUP.md#2-quick-start--your-first-mission)

**How agents work?**
- [FEATURES.md — Feature 1: Multi-Agent Orchestration](FEATURES.md#feature-1-multi-agent-orchestration)
- [SETUP.md — Section 3: How to Use the Multi-Agent Team](SETUP.md#3-how-to-use-the-multi-agent-team)

**How decisions get made?**
- [SETUP.md — Section 4: Knowledge Base Management](SETUP.md#4-knowledge-base-management)
- [FEATURES.md — Feature 5: Mission Decision Records](FEATURES.md#feature-5-mission-decision-records-mdrs)

**How security reviews work?**
- [SETUP.md — Section 7: Security & Compliance](SETUP.md#7-security--compliance)
- [FEATURES.md — Feature 7: Security & Compliance Reviews](FEATURES.md#feature-7-security--compliance-reviews)
- [knowledge_base/documents/github-actions-security-hardening.md](knowledge_base/documents/github-actions-security-hardening.md)

**How to set up a spoke repo?**
- [SETUP.md — Section 5: Spoke Repos](SETUP.md#5-spoke-repos--using-tng-in-your-services)
- [.tng-context.md](.tng-context.md) — Template

**How to use institutional memory?**
- [FEATURES.md — Feature 4: Institutional Memory (guinan)](FEATURES.md#feature-4-institutional-memory-guinan)
- [SETUP.md — Section 4.2: Anatomy of a Session Journal](SETUP.md#42-anatomy-of-a-session-journal)

**What happened in the past?**
- [knowledge_base/documents/past-lessons-learned.md](knowledge_base/documents/past-lessons-learned.md) — Timestamped lessons
- [knowledge_base/sessions/](knowledge_base/sessions/) — Session journals from prior missions
- [knowledge_base/documents/architecture-decision-records.md](knowledge_base/documents/architecture-decision-records.md) — Major decisions

---

## ⏱️ Time Commitments

| Activity | Time | What You Get |
|----------|------|-------------|
| Read README | 5 min | Project understanding |
| Read QUICK-REFERENCE | 3 min | Command patterns |
| Read FIRST-MISSION | 15 min | Walkthrough guide |
| Run first mission | 30-60 min | Hands-on experience + session journal |
| Review session journal | 5 min | See how history is captured |
| Read SETUP (full) | 30 min | Complete reference knowledge |
| Set up spoke repo | 10 min | Multi-service integration |

---

## 🚀 Quick Command Reference

### Start a Mission
```
"Mission: [your objective]"
```

### Request Single Agent
```
"@[agent_name] — [your question]"
```

### Check History
```
"@guinan — what carry-forward items are open?"
"Show me past lessons learned around [topic]"
```

### Get Status
```
"@riker — status report"
"picard, what's blocking closure?"
```

See [QUICK-REFERENCE.md](QUICK-REFERENCE.md) for full command list.

---

## 📊 Document Maintenance

| Document | Owner | Update Frequency | Last Updated |
|----------|-------|------------------|--------------|
| README.md | picard | Quarterly | 2026-04-11 |
| SETUP.md | picard | Quarterly | 2026-04-11 |
| FEATURES.md | picard | Quarterly | 2026-04-11 |
| QUICK-REFERENCE.md | picard | Quarterly | 2026-04-11 |
| FIRST-MISSION.md | picard | Quarterly | 2026-04-11 |
| TEAM-TOPOLOGY.md | picard | Per change | 2026-04-11 |
| STATUS.md | picard | Per mission | 2026-04-11 |
| past-lessons-learned.md | guinan | Per mission | 2026-04-11 |
| sprint-state.md | picard | Per mission | 2026-04-11 |

---

## 🎯 Next Step

👉 **New to TNG?** Go to [FIRST-MISSION.md](FIRST-MISSION.md)

👉 **Need quick commands?** See [QUICK-REFERENCE.md](QUICK-REFERENCE.md)

👉 **Want full details?** Read [SETUP.md](SETUP.md)

---

**"Make it so."**
