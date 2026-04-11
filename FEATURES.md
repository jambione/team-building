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
| Task | Agent | Estimate |
|------|-------|----------|
| Update workflows | geordi | 1h |
| Harden token perms | worf | 30m |
| Add test harness | troi | 2h |
| Design rollback | crusher | 30m |
| Code review | barclay | 1h |
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

**Review blocks**:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🟡★★☆ WORF — Security Review
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
VERDICT: PASS
- Token scope correctly limited to `actions:read` [GOOD]
- No secrets hardcoded [GOOD]
worf returns control to picard. [security-review-complete]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🔵★★☆ TROI — QA & Quality Review
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
VERDICT: CONDITIONAL
- Test coverage at 78% [WEAK — target 85%]
- API call edge cases not tested [CARELESS]
- Manual override tested [GOOD]
troi returns control to picard. [qa-review-complete]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🔵★★★ CRUSHER — Reliability Review
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
VERDICT: CONDITIONAL
- Rollback procedure documented [GOOD]
- No canary deployment strategy [WEAK]
- Rate-limit fallback tested [GOOD]
crusher returns control to picard. [reliability-review-complete]
```

**picard then issues**:
```
VERDICT: GO with conditions
- Test coverage gap (troi) → Fix-in-place (must reach 85% before merge)
- No canary deployment (crusher) → Scoped Ready Room (next sprint)
```

### Phase 4: Mission Close (Learning Capture)

**What happens**:
1. Each specialist updates their KB document
2. picard fills Mission Debrief
3. Session journal marked closed
4. picard notifies guinan
5. picard closes: **"Make it so."**

**What gets captured**:
- Session journal (events, decisions, findings)
- Lessons learned (added to `past-lessons-learned.md`)
- KB document updates (new patterns, decisions)
- Carry-forwards (if work deferred)
- Agent performance notes (for monitoring)

**Example debrief**:
```markdown
## Mission Debrief

### Objective
Integrate Claude API into CI pipeline for automated PR code reviews

### Outcome
✅ ALL TASKS COMPLETE

    - Workflow file updated and deployed
    - Security hardening completed
    - Tests added (85%+ coverage)
    - Rollback procedure documented & tested

### Key Lessons

1. GitHub token permission scoping is critical
   Lesson: Omitting `permissions:` defaults to `write-all`
   Decision: Always use minimal scope explicitly
   
2. CodeQL requires precise 3-step sequence
   Lesson: Using only `upload-artifact` produces no security analysis
   Decision: Update template to enforce init → autobuild → analyze
   
3. SARIF uploads require `security-events: write` permission
   Lesson: Scans silently fail without this specific permission
   Decision: Document permission matrix in KB

### Metrics
- Ready Room decisions: 3 (options considered, 1 selected)
- Risks identified: 5 (3 P1, 2 P2)
- Review verdicts: 2 CONDITIONAL, 1 PASS
- Session duration: 3.5 hours
- Crew utilization: All 6 agents active

### Outcome Rating
🟢 GREEN — All objectives met, quality gates passed (with conditions).
        Work ready for production.
```

---

## Feature 3: Knowledge Base System

### What It Is
Persistent, team-wide repository of decisions, lessons, and best practices organized by domain.

### Documents by Category

**Architecture & Design**
- `architecture-principles.md` — Foundational rules, patterns
- `architecture-decision-records.md` — ADRs for major decisions
- `system-design-patterns.md` — Reusable patterns
- `coding-standards.md` — Readability, naming, style

**DevOps & CI/CD**
- `ci-cd-pipeline-recommendations.md` — Production-grade setup
- `devops-best-practices.md` — Speed targets, caching, Docker
- `github-actions-best-practices.md` — Workflow structure, secrets
- `github-actions-security-hardening.md` — Security checklist (SOC 2/ISO)

**Development Practices**
- `best-practices.md` — General guidelines
- `team-conventions.md` — Orchestration rules, communication style
- `onboarding-guide.md` — New team member orientation

**Reliability & Operations**
- `monitoring-observability.md` — Metrics, dashboards, alerting
- `incident-response-playbook.md` — Crisis procedures
- `tech-debt-register.md` — Known debt, prioritization

**Team State**
- `past-lessons-learned.md` — Timestamped lessons with outcomes
- `sprint-state.md` — Open carry-forward items
- `agent-performance-log.md` — Agent utilization, effectiveness

### How guinan Uses the KB

When you start a new mission, **guinan speaks first**:

```
⚪— guinan — scanning past-lessons-learned.md, session journals, and ADRs...

"guinan found 3 prior sessions on API integration:
  - 2024-03-15: Webhook-based approach (failed: latency)
  - 2024-05-20: GitHub App (failed: complexity)
  - 2025-11-10: GitHub Actions integration (succeeded)
  
Relevant lesson: In-band workflows outperform external services.
Relevant decision: Token scoping matrix in github-actions-security-hardening.md
Relevant carry-forward: Rate-limit handling from 2025-11-10 still pending."

guinan returns control to picard. [context-retrieval-complete]
```

### KB Updates (Phase 4)

After every mission, agents update their documents:

| Agent | Updates | Example |
|-------|---------|---------|
| data | `architecture-decision-records.md` | New ADR: Claude API integration approach |
| geordi | `github-actions-best-practices.md`, `ci-cd-pipeline-recommendations.md` | New pattern: rate-limited API calls in workflows |
| worf | `github-actions-security-hardening.md` | Token scope matrix for AI integrations |
| troi | `best-practices.md` | Edge-case test patterns for API calls |
| crusher | `incident-response-playbook.md`, `tech-debt-register.md` | Rollback procedures for failed API reviews |
| picard | `past-lessons-learned.md`, `sprint-state.md` | New lessons, open carry-forwards |

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

### Example

```
Mission: "Implement JWT expiry validation"

guinan surfaces:
  "guinan recalls 2 prior sessions on authentication:
  
  • 2026-02-10: Auth redesign (crusher noted edge case: token refresh race condition)
  • 2026-03-05: OAuth2 exploration (deferred: complex scope, pushed to Sprint 26)
  
  Lessons learned:
  - Test token expiry under concurrent requests (2026-02-10 had bugs)
  - Validate against database (not just local timestamp)
  
  Open carry-forward: OAuth2 migration still pending (CF-087, target Sprint 26)
  
  Recommendation: Pull crusher into this mission for edge-case review."
```

---

## Feature 5: Mission Decision Records (MDRs)

### What It Is
A structured decision artifact that captures:
- What decision was made
- Why (rationale)
- What alternatives were considered
- What risks exist (and mitigation plans)
- Who implements what

### Structure

```markdown
## Mission Decision Record

**Mission**: [your objective]

**Decision**: [the chosen approach in one sentence]

**Options Considered**:
1. [Option A]
   - Pros: ...
   - Cons: ...
   - Rationale for rejection: ...

2. [Option B] ← SELECTED
   - Pros: ...
   - Cons: ...
   - Why selected: ...

**Rationale**: [Why this decision is the right one]

**Risks**:
- [P0 RISK] [description] → Mitigation: [plan]
- [P1 RISK] [description] → Mitigation: [plan]
- [P2 RISK] [description] → Mitigation: [plan]

**Crew Assignments**:
| Task | Agent | Est. Time | Success Criteria |
|------|-------|-----------|------------------|
| [task 1] | data | 2h | [measurable outcome] |
| [task 2] | geordi | 1h | [measurable outcome] |
```

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
   - `.tng-context.md` file (service identity)
   - Local code (API, frontend, etc.)
   - Can reference hub for decisions/history

3. **When you state a mission in a spoke**:
   - picard reads `.tng-context.md` to identify service
   - picard routes to correct owner agent
   - picard syncs carry-forwards from hub
   - Work proceeds with hub knowledge

### Example: Setting Up a Spoke

**In `/api` repo**:

```yaml
# .tng-context.md
repo_name: "org/service-api"
service_domain: "Backend REST API — user auth and accounts"
owner_agent: "data"
status: "active"

## Tech Stack
- Language: Node.js 20
- Framework: Express
- Database: PostgreSQL 15
- Deploy: AWS ECS

## Dependencies
| Depends On | Type | Notes |
|------------|------|-------|
| org/shared-lib | shared-lib | Auth utilities |
| org/migration-scripts | data-schema | DB migrations |
```

**When you state a mission**:

```
[User opens mission in /api directory]

User: "Implement JWT expiry validation"

picard reads .tng-context.md:
  repo_name: org/service-api
  owner_agent: data
  status: active

picard announces:
  "picard is working in org/service-api
   (Backend REST API — user auth and accounts).
   data is the owner agent for this service domain."

Ready Room opens with data as primary handler.
```

### Carry-Forwards

When you close a mission with open items, picard updates `sprint-state.md` in the hub:

```markdown
| CF-ID | Service | Item | Owner | Target Sprint |
|-------|---------|------|-------|---------------|
| CF-087 | org/service-api | Implement JWT expiry validation | data | Sprint 26 |
| CF-088 | org/frontend | Dark mode mobile fixes | troi | Sprint 26 |
```

Next time you work in that service, **guinan surfaces the carry-forwards automatically**.

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
Validating SARIF configurations... Auditing action versions...

VERDICT: PASS with findings
- Token scope correctly limited [GOOD]
- Secrets stored in GitHub Secrets [GOOD]
- No hardcoded credentials [GOOD]
- SARIF report needs security-events: write [CARELESS]
  → Action: Update workflow permissions block

worf returns control to picard. [security-review-complete]
```

### Security KB Documents

**`github-actions-security-hardening.md`** contains:

- ✅ Token scope matrix (minimum permissions by workflow type)
- ✅ Secrets management checklist
- ✅ CodeQL setup (3-step sequence required)
- ✅ SARIF upload configuration (requires `security-events: write`)
- ✅ Action version pinning rules
- ✅ Audit logging setup
- ✅ Compliance requirements (SOC 2, ISO, etc.)

**Examples**:

```yaml
# Minimum permissions for a CI workflow
permissions:
  actions: read          # Read workflows
  contents: read         # Clone repo
  pull-requests: write   # Comment on PRs
  # NO write-all — never

# Minimum permissions for CodeQL
permissions:
  contents: read         # Read code
  security-events: write # Upload SARIF results
  # That's it

# Minimum permissions for Trivy scanning
permissions:
  contents: read
  security-events: write
```

---

## Feature 8: Observability & Monitoring

### What It Is
Built-in tracking of:
- What decisions were made and why
- Which agents are effective at what tasks
- How long missions take
- What risks materialized vs. mitigated

### How It Works

**Session journals capture**:
- Crew engaged (who participated)
- Handoff signals (communication audit trail)
- Priority triage (risk identification)
- Phase durations (time tracking)
- Review verdicts (quality metrics)

**Agent performance log tracks**:
- Tasks per agent
- Success rates
- Common handoff patterns
- Specialization effectiveness

### Example Metrics

```markdown
## Agent Performance Log — April 2026

| Agent | Missions | Avg Tasks/Mission | Success Rate | Specialization |
|-------|----------|-------------------|--------------|-----------------|
| picard | 12 | 1 (orchestrator) | 100% | Strategic decisions |
| data | 11 | 1.8 | 95% | Architecture/design |
| geordi | 10 | 2.1 | 98% | CI/CD, DevOps |
| worf | 12 | 1.2 | 100% | Security reviews |
| crusher | 9 | 1.7 | 89% | Reliability analysis |
| barclay | 7 | 1.4 | 86% | Tech debt assessment |
```

---

## Feature 9: Carry-Forwards & Sprint Planning

### What It Is
A system for tracking work that's deferred from one sprint to the next.

### How It Works

During Phase 3 (Track C Review), if items are classified as:
- **Scoped Ready Room** — Brief re-analysis needed (deferrable)
- **Full Reopen** — Major changes required (deferrable)

picard updates `sprint-state.md`:

```markdown
| CF-ID | Service | Item | Owner | Status | Target Sprint |
|-------|---------|------|-------|--------|---------------|
| CF-087 | org/api | OAuth2 migration | data | OPEN | Sprint 27 |
| CF-088 | org/frontend | Mobile dark mode tests | troi | OPEN | Sprint 26 |
| CF-089 | org/api | Rate-limit alerting | obrien | BLOCKED | Sprint 27 (depends on CF-087) |
```

### guinan's Role

When you start a new mission:

```
@guinan — what carry-forwards apply to this mission?"

⚪— guinan — Scanning sprint-state.md...

"guinan found 2 open carry-forwards for org/api:
  • CF-087: OAuth2 migration (data, target Sprint 27)
  • CF-089: Rate-limit alerting (obrien, depends on CF-087)
  
These may be related to your current mission on JWT validation.
Recommendation: Discuss sequencing with data and obrien."
```

---

## Feature 10: Third-Person Communication

### What It Is
A unique communication style where agents refer to themselves in third person.

### Why
- **Clarity**: "picard has decided X" vs "I decided X" (consistent, unambiguous)
- **Personality**: Enforces distinct character voice
- **Professionalism**: Maintains distance, authority
- **Auditability**: Makes it clear who was speaking

### Examples

✅ **Correct**:
- "picard has opened the Ready Room"
- "data is analyzing the architecture"
- "worf has completed the security review"
- "riker returns control to picard"

❌ **Incorrect**:
- "I have opened the Ready Room"
- "I am analyzing the architecture"
- "I have completed the security review"
- "I return control to picard"

---

## Feature 11: Handoff Protocol

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
   🟡★★☆ geordi — Give geordi a few minutes. geordi already sees the problem.
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

## Feature 12: Track C Review Gates

### What It Is
Three mandatory quality checks (security, QA, reliability) that happen after all work is complete but before mission closes.

### The Three Reviews

1. **Security (worf)**
   - Token permissions correctly scoped
   - No hardcoded secrets
   - Compliance requirements met (SOC 2/ISO/HIPAA)
   - Audit logging configured
   - Results: SARIF uploads working

2. **QA/Quality (troi)**
   - Test coverage meets targets
   - Edge cases tested
   - Manual testing completed
   - No regressions introduced
   - Documentation updated

3. **Reliability (crusher)**
   - Failure modes identified
   - Rollback procedures documented & tested
   - Canary deployment strategy defined (if applicable)
   - Observability configured
   - Alerts configured for failure conditions

### Verdict Options

Each reviewer issues:
- **PASS** — All checks clear
- **CONDITIONAL** — Pass with items to fix or monitor
- **FAIL** — Blocking issues; requires rework

### picard's Go/No-Go

After all 3 reviews:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🔴★★★★ PICARD — Mission Go/No-Go
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

GO with conditions:
  - Test coverage gap (troi) → Fix-in-place [must reach 85% before merge]
  - No canary strategy (crusher) → Scoped Ready Room [next sprint]

Ready for production with monitoring for [specific conditions].
```

---

## Summary: All Features at a Glance

| Feature | Purpose | Owner | Trigger |
|---------|---------|-------|---------|
| Multi-Agent Orchestration | Parallel expert analysis | picard | Mission statement |
| 4-Phase Workflow | Structured decision + execution + review | picard | Phase boundaries |
| Knowledge Base | Persistent team memory | All agents | Phase 4 (updates), Phase 1 (guinan reads) |
| Institutional Memory (guinan) | History surfacing | guinan | Mission start |
| Mission Decision Records | Decision capture | picard | Phase 1 close |
| Spoke Repo Integration | Multi-service coordination | picard + hub | Mission in spoke folder |
| Security Reviews | Compliance gates | worf | Phase 3 |
| Observability | Metrics tracking | obrien | Continuous (updates Phase 4) |
| Carry-Forwards | Sprint planning | picard | Phase 3 (classification) |
| Third-Person Communication | Clarity & auditability | All agents | All interactions |
| Handoff Protocol | Explicit control flow | All agents | Between tasks |
| Track C Review | Quality gates | worf + troi + crusher | Phase 3 |

---

**"Make it so."**
