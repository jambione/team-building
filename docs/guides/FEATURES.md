# TNG Agent Team — Feature Reference

**Complete documentation of all features and capabilities.**

---

## Feature 1: Multi-Agent Orchestration

### What It Is

A system of 13 specialized agents modeled after Star Trek characters, each with distinct expertise. Agents collaborate on complex tasks following explicit protocols with clear handoffs.

### How It Works

1. State your mission
2. Agents analyze in parallel or sequence (picard decides)
3. Each agent speaks in-character, using their distinctive voice
4. All decisions and actions are logged with ownership attribution
5. Handoffs use explicit control signals with acknowledgment

### Key Agents

- **picard** — Orchestrator; makes strategic decisions; leads all phases
- **picard-thinking** — Deep analysis mode for complex decisions
- **picard-fast** — Lightweight execution mode for straightforward tasks
- **riker** — First Officer; coordinates Phase 2 execution
- **data** — Architecture and system design expert
- **geordi** — DevOps and CI/CD automation
- **worf** — Security and compliance specialist
- **troi** — QA, testing, and user experience
- **crusher** — Reliability and failure-mode analysis
- **barclay** — Technical debt and maintainability
- **guinan** — Institutional memory and cross-session continuity
- **obrien** — Observability, monitoring, and operations
- **wes** — Explores unconventional solutions (approval required)

### Usage Example

```
User: "Mission: Integrate Claude API into CI pipeline for PR reviews"

System triggers 4-phase workflow automatically:
  Phase 1 → Ready Room (decision)
  Phase 2 → Bridge execution (implementation)
  Phase 3 → Track C review (quality gates)
  Phase 4 → Mission close (learning capture)
```

### Features

✅ Parallel agent analysis (reduced decision time)
✅ In-character communication (consistency, personality)
✅ Explicit handoff protocol (no silent failures)
✅ Role-based expertise (right person for each task)
✅ Historical context (guinan surfaces prior lessons)

---

## Feature 2: Structured 4-Phase Workflow

### Phase 1: Ready Room (Decision-Making)

**What happens**:

1. picard opens the Ready Room
2. guinan scans institutional memory for relevant history
3. All decision-relevant agents analyze in parallel:
   - data (architecture)
   - worf (security)
   - troi (QA/UX)
   - crusher (reliability)
   - barclay (technical debt)
   - obrien (observability)
4. picard synthesizes findings into a Mission Decision Record (MDR)
5. picard locks all decisions: `[READY-ROOM-CLOSED]`

**Key rule**: No code is written until Ready Room closes.

**Output**: Mission Decision Record with:

- Decision or approach
- Options considered + rationale
- Risks and mitigations
- Crew assignments for Phase 2

**Example MDR**:

```markdown
## Decision: Integrate Claude API via GitHub Actions

## Options

1. Webhook-based external service (rejected)
   Rationale: Adds latency, creates single point of failure
2. GitHub App (rejected)
   Rationale: Complexity + approval process overhead
3. GitHub Actions + Claude API (selected)
   Rationale: In-band with workflow, simple, observable

## Risks

- P1: API rate limits → Mitigation: queue with backoff
- P2: Token exposure → Mitigation: GitHub Secrets + audit
- P3: CI logic changes reviewed → Mitigation: manual approval gate

## Crew Assignments

| Task               | Agent   | Estimate |
| ------------------ | ------- | -------- |
| Update workflows   | geordi  | 1h       |
| Harden token perms | worf    | 30m      |
| Add test harness   | troi    | 2h       |
| Design rollback    | crusher | 30m      |
| Code review        | barclay | 1h       |
```

### Phase 2: Bridge Execution (Implementation)

**What happens**:

1. riker takes lead as First Officer
2. riker announces Execution Coordination Report (parallel/sequence/dependencies)
3. Each assigned agent executes their task
4. Every action announced BEFORE work (never after)
5. Every handoff uses explicit signal + ACK
6. riker returns when complete: `[execution-complete]`

**Example flow**:

```
🔴★★★ riker — Crew assignments locked. Beginning execution.

▶ geordi — Updating .github/workflows/ci.yml with proper permissions
🟡★★☆ geordi — Give geordi a few minutes. geordi already sees the problem.
[... work happens ...]
geordi returns control to riker. [workflow-updated ✓]

[riker] ACK: [workflow-updated ✓ riker]

▶ worf — Hardening GitHub token scope for CodeQL
🟡★★☆ worf — worf does not look for problems. worf finds them.
[... work happens ...]
worf returns control to riker. [hardened-tokens ✓]

[riker] ACK: [hardened-tokens ✓ riker]
```

**Key rule**: Agents work sequentially OR parallel with explicit riker coordination. Never ambiguous.

### Phase 3: Track C Review (Quality Gates)

**What happens**:

1. Three mandatory reviewers publish blocks in chat
2. Each reviewer issues VERDICT: PASS / FAIL / CONDITIONAL
3. Findings listed with severity ratings
4. picard classifies open items and issues Go/No-Go

### Phase 4: Mission Close (Learning Capture)

**What happens**:

1. Each specialist updates their KB document
2. picard fills Mission Debrief
3. Session journal marked closed
4. picard notifies guinan
5. picard closes: **"Make it so."**

---

## Feature 3: Knowledge Base System

### What It Is

Persistent, team-wide repository of decisions, lessons, and best practices organized by domain.

### Documents by Category

**Architecture & Design**

- `architecture-principles.md` — Foundational rules, patterns
- `architecture-decision-records.md` — ADRs for major decisions

**DevOps & CI/CD**

- `github-actions-best-practices.md` — Workflow structure, secrets
- `github-actions-security-hardening.md` — Security checklist

**Reliability & Operations**

- `monitoring-observability.md` — Metrics, dashboards, alerting
- `incident-response-playbook.md` — Crisis procedures

**Team State**

- `past-lessons-learned.md` — Timestamped lessons with outcomes
- `sprint-state.md` — Open carry-forward items

---

## Feature 4: Institutional Memory (guinan)

### What It Is

A special agent that remembers ALL prior sessions and surfaces relevant history automatically.

### How It Works

1. **Session journals** are saved at `knowledge_base/sessions/YYYY-MM-DD-HH-<slug>.md`
2. Each session captures:
   - Mission objective
   - Crew engaged
   - Decisions made
   - Risks identified
   - Lessons learned
   - Final outcome
3. **guinan reads** at mission start:
   - All prior session journals (filtered by topic)
   - `past-lessons-learned.md` entries
   - Architecture Decision Records
   - Carry-forward items from `sprint-state.md`
4. **guinan synthesizes** and surfaces:
   - Similar past situations and their outcomes
   - Lessons learned (patterns, mistakes, successes)
   - Open or deferred work related to this mission

---

## Feature 5: Mission Decision Records (MDRs)

### What It Is

A structured decision artifact that captures:

- What decision was made
- Why (rationale)
- What alternatives were considered
- What risks exist (and mitigation plans)
- Who implements what

### Why It Matters

- **Decisions are locked** before code starts (no scope creep mid-mission)
- **Rationale is captured** (why you chose this, not that)
- **Risks are explicit** (mitigations planned upfront)
- **Work is assigned** (no ambiguity about who does what)
- **Success is measurable** (clear "done" criteria)

---

## Feature 6: Spoke Repo Integration

### What It Is

A way to manage multiple service repos (API, frontend, migrations, etc.) in a single team workspace while maintaining centralized agent knowledge.

### How It Works

1. **Hub repo** (`team-building/`) contains:

   - All agent definitions
   - All KB documents
   - All session history
   - All shared workflows

2. **Spoke repos** (each service) contain:

   - Optional `.tng-context.md` file (service identity override)
   - Local code (API, frontend, etc.)
   - Can reference hub for decisions/history

3. **When you state a mission in a spoke**:
   - picard reads `.tng-context.md` when present to identify service
   - if absent, picard falls back to `knowledge_base/current/workspace-context.md`
   - picard routes to correct owner agent
   - picard syncs carry-forwards from hub
   - Work proceeds with hub knowledge

---

## Feature 7: Security & Compliance Reviews

### What It Is

Mandatory security review phase (Track C) that covers:

- GitHub token permissions
- Secrets management
- Compliance requirements (SOC 2, ISO)
- Code security analysis

### How It Works

**worf conducts security review**:

```
🟡★★☆ WORF — Security Review

"worf does not look for problems. worf finds them."

Reviewing token permissions... Checking secrets exposure...

VERDICT: PASS with findings
- Token scope correctly limited [GOOD]
- Secrets stored in GitHub Secrets [GOOD]
- No hardcoded credentials [GOOD]

worf returns control to picard. [security-review-complete]
```

---

## Feature 8: Carry-Forwards & Sprint Planning

### What It Is

A system for tracking work that's deferred from one sprint to the next.

### How It Works

During Phase 3 (Track C Review), if items are classified as:

- **Scoped Ready Room** — Brief re-analysis needed (deferrable)
- **Full Reopen** — Major changes required (deferrable)

picard updates `sprint-state.md`:

```markdown
| CF-ID  | Service      | Item                  | Owner | Target Sprint |
| ------ | ------------ | --------------------- | ----- | ------------- |
| CF-087 | org/api      | JWT expiry validation | data  | Sprint 26     |
| CF-088 | org/frontend | Mobile dark mode      | troi  | Sprint 26     |
```

---

## Feature 9: Handoff Protocol

### What It Is

An explicit signaling system that ensures no action is ambiguous or lost.

### Structure

Each handoff has 4 steps:

1. **Announcement** (before work starts)

   ```
   ▶ [agent] — [action]
   ```

2. **In-character opening** (agent acknowledges)

   ```
   🟡★★☆ geordi — Give geordi a few minutes.
   ```

3. **Work execution**

   ```
   [... actual work happens ...]
   ```

4. **Return with trigger signal**

   ```
   geordi returns control to riker. [workflow-updated ✓]
   ```

5. **Acknowledgment** (receiver confirms)
   ```
   [riker] ACK: [workflow-updated ✓ riker]
   ```

### Why It Matters

- **Nothing is lost**: Every action starts and ends explicitly
- **Clarity**: Receiver acknowledges before next step
- **Auditability**: Full trace of who did what and when
- **Parallelism**: riker can coordinate multiple agents because handoffs are explicit

---

## Feature 10: Track C Review Gates

### What It Is

Three mandatory quality checks (security, QA, reliability) that happen after all work is complete but before mission closes.

### The Three Reviews

1. **Security (worf)**

   - Token permissions correctly scoped
   - No hardcoded secrets
   - Compliance requirements met

2. **QA/Quality (troi)**

   - Test coverage meets targets
   - Edge cases tested
   - No regressions introduced

3. **Reliability (crusher)**
   - Failure modes identified
   - Rollback procedures documented & tested
   - Alerts configured for failure conditions

### Verdict Options

Each reviewer issues:

- **PASS** — All checks clear
- **CONDITIONAL** — Pass with items to fix or monitor
- **FAIL** — Blocking issues; requires rework

---

**"Make it so."**
