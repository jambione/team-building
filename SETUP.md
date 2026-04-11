# TNG Agent Team — Setup & Usage Guide

**Version 2.2** | Last updated: 2026-04-11

---

## Quick Overview

**TNG Agent Team** is a multi-agent orchestration framework that guides complex software engineering work through structured, collaborative decision-making and execution. Rather than doing work alone, you work *with* the team: state your mission, the crew analyzes in parallel, decisions get recorded, and execution is coordinated with explicit handoffs.

**Key principle**: No code is written until the Ready Room closes and decisions are locked.

---

## 1. Initial Setup

### 1.1 Prerequisites

- **GitHub Copilot** with Chat enabled in VS Code
- **VS Code** with the Copilot Chat extension installed
- **Git** for version control
- A workspace folder containing this `team-building` hub repo

### 1.2 Workspace Structure

```
workspace/
├── team-building/          ← Hub repo (agents, KB, workflows, prompts)
│   ├── .github/
│   │   ├── agents/         ← 13 agent personas
│   │   ├── prompts/        ← Protocol templates
│   │   └── workflows/      ← CI/CD automation
│   ├── knowledge_base/
│   │   ├── documents/      ← Domain docs (KB source of truth)
│   │   ├── sessions/       ← Session journals & debriefs
│   │   └── archive/        ← Historical records
│   ├── copilot-instructions.md  ← System initialization
│   ├── TEAM-TOPOLOGY.md    ← Agent roster
│   ├── STATUS.md           ← Workflow activation status
│   └── RUNBOOK.md          ← Execution guidelines
│
└── [spoke repos]/          ← Service repos (feature, API, etc.)
    ├── .tng-context.md     ← Spoke identity & routing
    └── ...
```

### 1.3 First-Time Activation

1. Open the `team-building` repo in VS Code
2. Open **Copilot Chat** (`Ctrl+Shift+I` / `Cmd+Shift+I`)
3. The system will auto-load from `.github/copilot-instructions.md`
4. You should see:
   ```
   Tea. Earl Grey. Hot.
   🔴★★★★ picard — the crew is assembled. The Ready Room is available. State your mission.
   ```

If activation fails:
- Verify `.github/copilot-instructions.md` exists and is valid YAML
- Check that all agent files in `.github/agents/` are present
- Restart VS Code and open Copilot Chat again

---

## 2. Quick Start — Your First Mission

### 2.1 State Your Mission

In Copilot Chat, describe what you need the team to work on. Examples:

```
"Integrate Claude API into our CI pipeline for automated PR code reviews"

"Refactor the authentication module to reduce technical debt"

"Design and implement a dark mode toggle for the frontend"

"Perform a security audit of our GitHub Actions workflows"
```

### 2.2 What Happens Automatically

The moment you state a mission, this **4-phase workflow** triggers automatically:

#### Phase 1: Ready Room (Decision-Making)
- picard opens the Ready Room
- **guinan** surfaces relevant history (past lessons, related decisions)
- **Parallel crew analysis**: Each agent (data, worf, troi, crusher, barclay, obrien) speaks in character and delivers findings
- picard aggregates findings from all agents
- picard issues a **Mission Decision Record (MDR)** with:
  - Decision or approach
  - Options considered
  - Rationale
  - Risks and mitigations
  - Crew assignments for Phase 2
- picard issues hard close: `[READY-ROOM-CLOSED]`

**Duration**: Usually 2-5 minutes. All decisions are locked before code starts.

#### Phase 2: Bridge Execution (Action)
- **riker** takes lead as First Officer
- riker announces the **Execution Coordination Report** (parallel tasks, sequence, dependencies)
- Each assigned agent (geordi, worf, troi, etc.) executes their task in character
- Every action is announced before the work, never after
- Every handoff uses an explicit control signal with acknowledgment
- riker returns control when all assignments complete: `[execution-complete]`

**Duration**: Varies by task complexity.

#### Phase 3: Track C Review (Quality Gates)
Three mandatory review blocks appear directly in chat:

1. **worf** — Security Review
   - VERDICT: PASS / FAIL / CONDITIONAL
   - Lists security findings by severity

2. **troi** — UX & Quality Review
   - VERDICT: PASS / FAIL / CONDITIONAL
   - Quality and testing concerns

3. **crusher** — Reliability Review
   - VERDICT: PASS / FAIL / CONDITIONAL
   - Edge cases and failure modes

picard then issues the Go/No-Go decision and classifies any open items as:
- Fix-in-place (resolve now)
- Scoped Ready Room (brief re-analysis)
- Full Reopen (major changes needed)

#### Phase 4: Mission Close
- Each specialist updates their domain KB document
- picard records the **Mission Debrief** (lessons, decisions, outcomes)
- Session journal is updated with final status
- picard closes with: **"Make it so."**

All session history is captured for guinan's future reference.

---

## 3. How to Use the Multi-Agent Team

### 3.1 Agents & Their Roles

| Agent | Badge | Role | When to Trust |
|-------|-------|------|---------------|
| **picard** | 🔴★★★★ | Orchestrator & commander | Strategic decisions, mission objective |
| **picard-thinking** | ⚫★★★ | Deep deliberation | Complex architecture, ethical trade-offs, risk analysis |
| **picard-fast** | 🟢★★ | Bridge execution | After Ready Room closes, low-risk tasks |
| **data** | 🟡★★☆ | Architecture & design | System design, patterns, scalability |
| **riker** | 🔴★★★ | First Officer execution | Coordinating parallel tasks, handoff orchestration |
| **geordi** | 🟡★★☆ | DevOps & CI/CD | GitHub Actions, Docker, caching, deployment |
| **worf** | 🟡★★☆ | Security & compliance | Token permissions, secrets, SOC 2/ISO |
| **troi** | 🔵★★☆ | QA, testing & UX | Test strategy, quality gates, user experience |
| **crusher** | 🔵★★★ | Reliability & edge cases | Failure modes, canaries, rollback, observability |
| **barclay** | 🟡★★ | Technical debt | Refactoring, DRY/YAGNI, long-term maintainability |
| **guinan** | ⚪☆☆ | Institutional memory | Historical context, past lessons, cross-session continuity |
| **obrien** | 🟡★ | Observability & ops | Monitoring, metrics, alerting, incident response |
| **wes** | ⚡★☆ | Exploratory proposals | Unconventional solutions, experiments (approval required) |

### 3.2 Agent Communication Patterns

Each agent has a **Voice** with opening phrases, critical language, and sign-offs. Examples:

- `data`: *"Processing. There is a pattern here worth examining."* → findings → *"Fascinating. data returns control to picard."*
- `worf`: *"worf does not look for problems. worf finds them."* → findings → *"The defense holds. Qapla'."*
- `troi`: *"troi senses more here than the logs are showing."* → findings → *"troi has said what needs to be said."*
- `crusher`: *"Stable is not healthy. crusher will explain the difference."* → findings → *"Stable is stable."*

**Agents always operate in third person.** Never "I did this." Always "picard has completed that."

### 3.3 How to Request a Specific Agent

If you need analysis from just one agent (without a full mission workflow), you can ask directly:

```
"@data — design a caching strategy for this API"
"@geordi — review our GitHub Actions workflow for security issues"
"@troi — what test coverage should we target for this module?"
```

The agent will respond in character, analyze, and return control to you. No full workflow unless you state a mission.

---

## 4. Knowledge Base Management

### 4.1 What Gets Stored

The knowledge base is the **source of truth for team decisions and learning**. It contains:

| Category | Documents | Owner | Update Cadence |
|----------|-----------|-------|-----------------|
| **Architecture & Design** | `architecture-principles.md`, `architecture-decision-records.md` | data | Quarterly + per major decision |
| **DevOps & CI/CD** | `ci-cd-pipeline-recommendations.md`, `github-actions-best-practices.md`, `github-actions-security-hardening.md` | geordi | Quarterly + per pipeline change |
| **Development Practices** | `coding-standards.md`, `best-practices.md`, `team-conventions.md` | picard | Quarterly |
| **Reliability & Observability** | `monitoring-observability.md`, `incident-response-playbook.md` | crusher, obrien | Quarterly + per incident |
| **Technical Debt** | `tech-debt-register.md` | barclay | Per sprint + quarterly review |
| **Lessons Learned** | `past-lessons-learned.md` | guinan | After every mission |
| **Team State** | `sprint-state.md`, `agent-performance-log.md` | picard | Weekly + per mission |

### 4.2 Anatomy of a Session Journal

After each mission, a session journal is created at `knowledge_base/sessions/YYYY-MM-DD-HH-<mission-slug>.md`:

```markdown
# Session Journal — 2026-04-05-10

## Session Metadata
| Field | Value |
|-------|-------|
| **Session ID** | 2026-04-05-10 |
| **Mission** | Add automated PR code review via Claude API |
| **Status** | closed |

## Mission Objective
Integrate Claude API into the GitHub Actions CI pipeline...

## KB Documents Consulted
- past-lessons-learned.md
- github-actions-security-hardening.md
- ...

## Crew Engaged
| Agent | Role | Trigger | Handoff ACK |
|-------|------|---------|-------------|
| picard | Orchestrator | — | — |
| guinan | Context lookup | `context-lookup` | `[context-retrieval-received ✓ picard]` |
| ...

## Priority Triage
- [PRIORITY: P0] Token permissions not hardened
- [PRIORITY: P1] CodeQL sequence missing `analyze` step
- ...

## Mission Decision Record (MDR)
**Decision**: ...
**Rationale**: ...
**Risks**: ...
**Crew Assignments**: ...

## Phase 1 Findings
- [guinan findings]
- [data findings]
- [worf findings]
- ...

## Phase 2 Execution
- ▶ geordi — Updated `.github/workflows/ci.yml` with proper permissions blocks
- ▶ worf — Hardened token scopes for CodeQL and Trivy
- ...

## Phase 3 Reviews
- Security: PASS
- QA: PASS
- Reliability: CONDITIONAL (fix in next sprint)

## Debrief
**Key Lesson**: Omitting `permissions:` defaults to `write-all` — a critical misconfiguration.
**Outcome**: All 13 issues resolved. Health GREEN.
```

### 4.3 How Guinan Uses Session Journals

When you start a new mission, **guinan speaks first**:

```
"guinan has heard that before. Let guinan tell you how it ended."

⚪— guinan — scanning past-lessons-learned.md, session journals, and ADRs...
```

guinan reads:
- All previous session journals for similar topics
- `past-lessons-learned.md` for relevant lessons
- Architecture Decision Records (ADRs) for context
- `sprint-state.md` for carry-forward items

This ensures **you never repeat the same mistake twice** and benefit from institutional memory.

---

## 5. Spoke Repos — Using TNG in Your Services

If you have multiple service repos (API, frontend, migrations, etc.), each one gets a `.tng-context.md` file:

### 5.1 Setting Up a Spoke Repo

1. Copy [`.tng-context.md`](.tng-context.md) into your service root
2. Fill out the metadata:
   ```yaml
   repo_name: "org/service-api"
   service_domain: "Backend REST API — user auth and accounts"
   owner_agent: "data"      # Primary domain owner
   status: "active"
   hub_repo: "team-building"  # Do NOT change
   ```
3. List your dependencies and tech stack
4. Override default routing if needed (e.g., if geordi isn't your DevOps agent)

### 5.2 Running a Mission in a Spoke Repo

When you state a mission while in a spoke repo (say, `/api`), picard automatically:
1. Reads the local `.tng-context.md` to identify the service
2. Routes to the correct owner agent (from the file)
3. Applies any repo-specific routing overrides
4. Syncs carry-forward items from `knowledge_base/documents/sprint-state.md` in the hub

Example:

```
[User is in /api directory, with .tng-context.md present]

User: "Add JWT expiry validation to the auth middleware"

picard reads .tng-context.md and sees:
  - service_domain: "Backend REST API — user auth"
  - owner_agent: "data"

picard opens Ready Room:
  [READY-ROOM-OPEN: jwt-expiry-validation]
  
  "We are working in org/service-api (Backend REST API).
   data is the owner agent for this domain."
   
  guinan scans for prior auth-related sessions...
```

When execution begins, riker remains in the hub repo but directs work logically to the spoke.

### 5.3 Carry-Forwards

When you close a mission with open items, picard updates `sprint-state.md` in the hub:

```markdown
| CF-ID | Service | Item | Owner | Target Sprint |
|-------|---------|------|-------|---------------|
| CF-087 | org/service-api | Migrate auth to OAuth2 | data | Sprint 26 |
| CF-088 | org/frontend | Dark mode mobile fixes | troi | Sprint 26 |
```

The next time you work in that service, guinan surfaces these carry-forwards automatically.

---

## 6. Mission Decision Record (MDR) — What to Expect

When the Ready Room closes, picard issues an MDR. Here's what it contains:

```markdown
## Mission Decision Record

**Mission**: Add automated PR code review via Claude API

**Decision**: Integrate Claude API directly into GitHub Actions CI pipeline
with optional manual override and rate limiting.

**Options Considered**:
1. Webhook-based external service (rejected: adds latency, single point of failure)
2. GitHub App (rejected: complexity, approval process)
3. GitHub Actions + Claude API (selected: simple, in-band with workflow)

**Rationale**:
- Options 1 & 2 add operational overhead without corresponding benefit
- GitHub Actions integration keeps the workflow data-local and observable
- API costs scale with volume (acceptable for our PR frequency)

**Risks**:
- P1: API rate limits during high-volume sprints → Mitigation: queue with backoff
- P2: Token exposure in logs → Mitigation: use GitHub Secrets, audit logging
- P3: Reviewing code changes to CI logic itself → Mitigation: manual approval gate

**Crew Assignments for Phase 2**:
| Task | Agent | Estimate | Success Criteria |
|------|-------|----------|------------------|
| Update `.github/workflows/ci.yml` | geordi | 1h | Workflow validates, no permission errors |
| Harden GitHub token permissions | worf | 30m | Token scoped to `actions:read` only |
| Add test harness for Claude API calls | troi | 2h | 80%+ coverage, edge cases tested |
| Design rollback procedure | crusher | 30m | Documented, tested on staging |
| Review final code for debt | barclay | 1h | No new debt introduced, baseline maintained |
```

**Rules**:
- No P0 or P1 items may remain unresolved when Ready Room closes
- All crew assignments are mandatory; agents will not skip tasks
- You can request clarification on any option or risk before approving

---

## 7. Security & Compliance

### 7.1 GitHub Token Permissions

**Never use `write-all` permissions.** Always scope tokens to minimum required:

```yaml
permissions:
  actions: read
  contents: read
  security-events: write     # ONLY if uploading SARIF
  pull-requests: write       # ONLY if commenting on PRs
```

See `knowledge_base/documents/github-actions-security-hardening.md` for full checklist.

### 7.2 Secrets Management

- Store API keys in GitHub Secrets, never in code or logs
- Use `run: echo "*** CENSORED ***"` to redact sensitive output
- Audit all agents with access to secrets (worf reviews this)

### 7.3 Compliance Reviews

Before any production deployment, **worf conducts a security review**:

- Token permission audit
- Secrets scanning
- SARIF report validation
- External dependency constraints (if applicable)

---

## 8. Common Commands & Patterns

### 8.1 Request Full Mission Workflow

```
"Mission: Identify and remediate technical debt in the checkout flow"
```

Triggers Ready Room → Bridge → Track C Review → Close.

### 8.2 Request Specific Analysis (No Full Workflow)

```
"@data — what's the best caching strategy for these endpoints?"
"@worf — audit our GitHub token permissions"
"@troi — design a test plan for the mobile checkout flow"
```

Agent responds in character, no full workflow.

### 8.3 Request Ready Room Only

```
"Open the Ready Room for: Evaluate migrating to monorepo structure"
```

Triggers Phase 1 (analysis & decision only), no Phase 2 execution.

### 8.4 Check Carry-Forwards

```
"@guinan — what carry-forward items are open from prior sprints?"
```

guinan surfaces items from `sprint-state.md`.

### 8.5 Reference the Knowledge Base

```
"Show me the past lessons learned around CI/CD performance"
```

picard retrieves and summarizes from `past-lessons-learned.md`.

---

## 9. Troubleshooting

### Issue: "The crew is not assembled" or agent names not recognized

**Cause**: Agent files missing or YAML syntax error in `.github/copilot-instructions.md`

**Fix**:
1. Verify all files exist in `.github/agents/`:
   ```
   picard.agent.md, data.agent.md, riker.agent.md, geordi.agent.md, worf.agent.md,
   troi.agent.md, crusher.agent.md, barclay.agent.md, guinan.agent.md, obrien.agent.md,
   wes.agent.md, picard-fast.agent.md, picard-thinking.agent.md
   ```
2. Validate YAML in `.github/copilot-instructions.md` (no syntax errors)
3. Restart VS Code and open Copilot Chat

### Issue: Guinan doesn't mention relevant history

**Cause**: Session journals not logged or file naming convention wrong

**Fix**:
1. Ensure sessions are saved at `knowledge_base/sessions/YYYY-MM-DD-HH-<slug>.md`
2. Check that `past-lessons-learned.md` has recent entries (should be updated per mission)
3. Verify status field is `closed` in session metadata

### Issue: Ready Room won't close or P1 items remain unresolved

**Cause**: Unresolved high-priority findings blocking closure

**Fix**:
1. Review the Priority Triage summary
2. Work with picard to resolve each P0/P1 item before close
3. If item needs to be deferred, reclassify as P2 with documented rationale

### Issue: Phase 2 execution seems stuck

**Cause**: Handoff signals not properly acknowledged

**Fix**:
1. Check the last handoff trigger in the conversation
2. Verify picard issues an ACK: `[<trigger>-received ✓ picard]`
3. If stuck, type: `"riker, status report"` to get execution coordination summary

### Issue: Track C reviews show CONDITIONAL or FAIL verdict

**Cause**: Quality gates identified issues before production deploy

**Fix**:
1. Review each reviewer's findings (worf, troi, crusher)
2. Prioritize DISHONORABLE/WEAK findings (security, reliability)
3. Decide disposition: Fix-in-place → Scoped Ready Room → Full Reopen
4. If fix-in-place, picard assigns to crew and re-validates

---

## 10. Best Practices

### 10.1 Mission Crafting

✅ **Good**: "Integrate Claude API into CI pipeline for automated PR reviews, including rate limiting and manual override"

❌ **Bad**: "Fix the CI"

Be specific about scope, constraints, and success criteria.

### 10.2 Handoff Protocol

✅ Always wait for handoff ACK before proceeding to next task

❌ Never batch tasks or assume parallel execution without explicit riker coordination

### 10.3 Knowledge Base Updates

✅ Update KB at mission close (Phase 4) — every session adds a row to `past-lessons-learned.md`

❌ Never leave open items without a debrief entry

### 10.4 Third-Person Communication

✅ "picard has closed the Ready Room"

❌ "I have closed the Ready Room"

Agents always refer to themselves in third person — this keeps the team persona consistent and clear.

### 10.5 Session Continuity

✅ Always open the next session with `"@guinan — surface relevant history"` before starting complex work

❌ Starting fresh without historical context leads to repeated mistakes

---

## 11. Advanced: Customization

### 11.1 Adding a New Spoke Repo

1. Create `.tng-context.md` in repo root (copy template)
2. Fill in metadata (name, domain, owner agent, tech stack)
3. Commit and push to main branch
4. Next time you state a mission in that repo, picard auto-routes

### 11.2 Customizing Agent Routing

Edit `TEAM-TOPOLOGY.md` to change default routing, then update `.github/agents/picard.agent.md` `agents:` list to match.

Example:
```yaml
# TEAM-TOPOLOGY.md — change from geordi to custom-ci-agent
- custom-ci-agent: CI/CD specialist (new hire)

# Then update picard.agent.md agents: list
agents:
  - data
  - custom-ci-agent  ← Added
  - ...
```

### 11.3 Creating New Ready Room Protocols

If you need a specialized workflow (e.g., incident postmortem, security audit, sprint planning), add new `.prompt` files to `.github/prompts/` and reference them in the mission context.

---

## 12. Reference: File Locations

| What | Where |
|------|-------|
| Agent personas | `.github/agents/*.agent.md` |
| System initialization | `.github/copilot-instructions.md` |
| Workflows | `.github/workflows/` |
| Ready Room protocol | `.github/prompts/ready-room.prompt.md` |
| Team topology | `TEAM-TOPOLOGY.md` |
| Workflow status | `STATUS.md` |
| Execution guidelines | `RUNBOOK.md` |
| Architecture principles | `knowledge_base/documents/architecture-principles.md` |
| Past lessons | `knowledge_base/documents/past-lessons-learned.md` |
| Sprint state | `knowledge_base/documents/sprint-state.md` |
| Session journals | `knowledge_base/sessions/YYYY-MM-DD-HH-*.md` |
| Spoke context | `<spoke-repo>/.tng-context.md` |

---

## 13. Getting Help

- **Technical questions about agents**: See `.github/agents/<name>.agent.md`
- **Workflow questions**: See `RUNBOOK.md`
- **Knowledge base questions**: See `knowledge_base/documents/index.md`
- **Process questions**: Open a mission with: `"Help: [your question]"`

---

**"Make it so."**
