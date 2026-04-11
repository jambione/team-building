# TNG Agent Team — First Mission Tutorial

**Step-by-step walkthrough of your first team mission.**

Duration: ~5 minutes setup + ~30-60 minutes mission time.

---

## Part 1: Setup (5 minutes)

### Step 1: Verify Prerequisites

- [ ] VS Code installed
- [ ] GitHub Copilot Chat extension installed (`Cmd+Shift+I` / `Ctrl+Shift+I` opens chat)
- [ ] `team-building` repo cloned locally
- [ ] Git configured with author name/email

### Step 2: Verify Agent Files

Navigate to `.github/agents/` in the repo and verify all 13 files exist:

```
✅ picard.agent.md
✅ picard-fast.agent.md
✅ picard-thinking.agent.md
✅ data.agent.md
✅ riker.agent.md
✅ geordi.agent.md
✅ worf.agent.md
✅ troi.agent.md
✅ crusher.agent.md
✅ barclay.agent.md
✅ guinan.agent.md
✅ obrien.agent.md
✅ wes.agent.md
```

If any are missing, the system won't initialize properly.

### Step 3: Activate Copilot

1. Open the `team-building` folder in VS Code
2. Press `Ctrl+Shift+I` (Windows/Linux) or `Cmd+Shift+I` (Mac)
3. The Copilot Chat panel should open on the right
4. Wait 2-3 seconds for initialization

You should see:

```
Tea. Earl Grey. Hot.
🔴★★★★ picard — the crew is assembled. The Ready Room is available. State your mission.
```

If not, refresh the chat or restart VS Code.

---

## Part 2: Choose Your First Mission (5 minutes)

Pick one of these beginner missions (all have clear scope):

### Option 1: Simple Feature (Recommended)
```
"Mission: Add a feature flag system to our CI pipeline"
```

**Why it's good**: 
- Defined scope
- Forces thinking about options (local, GitHub, external)
- Exercises all phases
- Realistic deliverable

### Option 2: Security Review
```
"Mission: Audit our GitHub Actions workflows for security compliance"
```

**Why it's good**:
- Clear success criteria (worf's checklist)
- Forces learning of security patterns
- Produces immediately useful KB updates

### Option 3: Technical Debt
```
"Mission: Identify and triage technical debt in our build pipeline"
```

**Why it's good**:
- Collaborative analysis (barclay leads)
- Produces a prioritized debt register
- No code required (pure analysis)

### Option 4: Architecture Decision
```
"Mission: Design a caching strategy for our API endpoints"
```

**Why it's good**:
- Forces architectural thinking
- Multiple options to weigh
- Produces an ADR (Architecture Decision Record)

---

## Part 3: Your First Mission (30-60 minutes)

### Step 1: State the Mission (Trigger Phase 1)

In Copilot Chat, type your chosen mission statement clearly and specifically.

**Example**:
```
Mission: Add a feature flag system to our CI pipeline so we can safely
roll out new features without breaking production jobs.
```

**What happens**:
- picard opens the Ready Room
- Session journal is created
- guinan scans for relevant history

### Step 2: Let Phase 1 Complete (Ready Room)

You'll see this sequence:

1. **picard opens**:
   ```
   [READY-ROOM-OPEN: feature-flag-system]
   
   picard is analyzing: Add a feature flag system to our CI pipeline
   so we can safely roll out new features without breaking production jobs.
   ```

2. **guinan speaks first**:
   ```
   ⚪— guinan — scanning past-lessons-learned.md, 
       session journals, and ADRs for relevant history
   
   "guinan has heard that before. Let guinan tell you how it ended."
   
   [guinan surfaces prior lessons on feature flags, CI safety, etc.]
   
   guinan returns control to picard. [context-retrieval-complete]
   ```

3. **Crew analyzes in parallel**:
   ```
   🟡★★☆ data — Processing. There is a pattern here worth examining.
   [architecture analysis...]
   Fascinating. data returns control to picard.
   
   🟡★★☆ worf — worf does not look for problems. worf finds them.
   [security review...]
   The defense holds. Qapla'.
   
   🔵★★☆ troi — troi senses more here than the logs are showing.
   [QA considerations...]
   troi has said what needs to be said.
   [... more agents speak ...]
   ```

4. **picard issues MDR**:
   ```
   ## Mission Decision Record
   
   **Decision**: Use environment variables + GitHub Secrets for feature flags
   
   **Options**:
   1. External SaaS (LaunchDarkly, etc.) → Rejected: adds operational overhead
   2. Database-backed flags → Rejected: too complex for simple on/off
   3. Environment variables + Secrets → Selected: simple, CI-native
   
   **Risks**:
   - P1: Secrets exposure in logs → Mitigation: GitHub Secrets + audit
   - P2: Rollback procedure undefined → Mitigation: Document + test
   
   **Crew Assignments**:
   | Task | Agent | Estimate |
   |------|-------|----------|
   | Implement flag system | geordi | 2h |
   | Harden secrets config | worf | 1h |
   | Add tests | troi | 1.5h |
   | Design rollback | crusher | 1h |
   ```

5. **Ready Room closes**:
   ```
   [READY-ROOM-CLOSED: feature-flag-system]
   
   picard has locked all decisions. The MDR is above.
   riker, the Ready Room is closed. Engage.
   ```

**⏱️ Expected duration**: 3-5 minutes of generated content

### Step 3: Let Phase 2 Execute (Bridge Execution)

riker takes over:

```
🔴★★★ riker — the Ready Room is closed. riker has the MDR. 
       Coordinating Bridge execution now.

Execution Coordination Report:
- Task 1: Implement (.github/workflows/*.yml update) by geordi [parallel]
- Task 2: Harden secrets config by worf [sequential after Task 1]
- Task 3: Add tests by troi [parallel with Task 2]
- Task 4: Design rollback by crusher [sequential after Tasks 2 & 3]

Beginning execution...

▶ geordi — Updating .github/workflows/ with feature flag logic

🟡★★☆ geordi — Give geordi a few minutes. geordi already sees the problem.

[... actual workflow updates ...]

geordi returns control to riker. [workflows-updated ✓]
[riker] ACK: [workflows-updated ✓ riker]

▶ worf — Hardening secrets configuration

🟡★★☆ worf — worf does not look for problems. worf finds them.

[... secrets hardening ...]

worf returns control to riker. [secrets-hardened ✓]
[riker] ACK: [secrets-hardened ✓ riker]

[... more agents execute ...]

riker returns control to picard. [execution-complete]
```

**⏱️ Expected duration**: 5-10 minutes of generated content

### Step 4: Track C Review (Quality Gates)

Three reviewers publish findings:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🟡★★☆ WORF — Security Review
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
VERDICT: PASS
- GitHub Secrets used correctly [GOOD]
- No hardcoded flags [GOOD]
- Log redaction configured [GOOD]
worf returns control to picard. [security-review-complete]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🔵★★☆ TROI — QA & Quality Review
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
VERDICT: CONDITIONAL
- Test coverage 82% (target 85%) [WEAK]
- Flag toggle behavior tested [GOOD]
- All edge cases covered [GOOD]
troi returns control to picard. [qa-review-complete]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🔵★★★ CRUSHER — Reliability Review
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
VERDICT: PASS
- Rollback procedure documented [GOOD]
- Canary deployment tested [GOOD]
- Fallback behavior validated [GOOD]
crusher returns control to picard. [reliability-review-complete]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🔴★★★★ PICARD — Mission Go/No-Go
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

GO with conditions:
  - Test coverage gap → Fix-in-place [reach 85% before merge]

Ready for production deployment.
```

**⏱️ Expected duration**: 2-3 minutes

### Step 5: Mission Close (Learning Capture)

```
picard is closing the mission...

picard has updated KB documents:
  ✅ github-actions-best-practices.md (new pattern documented)
  ✅ past-lessons-learned.md (lesson added)
  ✅ tech-debt-register.md (debt items reviewed)

Session journal closed:
  ✅ status: closed
  ✅ debrief: captured
  
picard has notified guinan of the session closure.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🔴★★★★ PICARD — Mission Debrief
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Mission: Add Feature Flag System

### Outcome
✅ COMPLETE — All tasks delivered, quality gates passed (with condition)

### Key Lesson
Feature flags are simple to implement if you use existing GitHub 
secrets infrastructure. Don't over-engineer with external SaaS tools 
for simple on/off switches.

### Metrics
- Ready Room decisions: 3 options, 1 selected
- Risks identified: 2 (1 P1, 1 P2)
- Review verdicts: 2 PASS, 1 CONDITIONAL
- Total duration: 47 minutes

### Rating
🟢 GREEN — Ready for production

Make it so.
```

**⏱️ Expected duration**: 2-3 minutes

---

## Part 4: After Your First Mission (5-10 minutes)

### What Was Captured?

1. **Session journal** at `knowledge_base/sessions/YYYY-MM-DD-HH-feature-flag-system.md`
   - Full record of decisions, findings, crew participation
   - Accessible to guinan for future reference

2. **KB updates**:
   - `past-lessons-learned.md` — new lesson row added
   - `architecture-decision-records.md` — new ADR if applicable
   - `ci-cd-pipeline-recommendations.md` — new pattern documented

3. **Git history** (if you committed):
   - Your changes are tracked with clear commit messages
   - Linked to session journal via commit body

### What You Should Do Now

1. **Commit the session to git** (optional, but recommended):
   ```bash
   git add knowledge_base/sessions/YYYY-MM-DD-HH-feature-flag-system.md
   git commit -m "Mission: Add feature flag system

   - Implemented via GitHub Secrets + env vars
   - All quality gates passed
   - Session: knowledge_base/sessions/2026-04-11-14-feature-flag-system.md"
   ```

2. **Review the KB updates**:
   Look at `knowledge_base/documents/past-lessons-learned.md` to see the new lesson row that was added.

3. **Run your next mission**:
   ```
   "Mission: [next objective]"
   ```
   
   Watch how guinan surfaces history from your first mission!

---

## Common Questions During Your First Mission

### "Why does the Ready Room need to close before code starts?"

- **Decision lock**: No decisions change mid-mission
- **Scope clarity**: Everyone knows what they're building
- **Risk mitigation**: All risks are identified upfront
- **Efficiency**: Parallel execution is coordinated by riker based on locked MDR

### "Can I interrupt the mission if I disagree?"

**Yes.** Type at any point:

```
"Hold. Objection to [decision or crew assignment]."
```

picard will re-open Ready Room for specific items. No need to restart.

### "How long does this usually take?"

- **Ready Room**: 3-5 minutes (analysis + decision)
- **Execution**: 5-10 minutes (varies by complexity)
- **Review**: 2-3 minutes (quality gates)
- **Close**: 2-3 minutes (debrief capture)

**Total**: 12-21 minutes for a straightforward mission. Complex missions (architecture, security audit) may take 45-60 minutes.

### "What if phase 2 execution gets stuck?"

Type:
```
"@riker — status report on current tasks"
```

riker will surface:
- Current agent and task
- Expected completion time
- Any blockers

### "Can I request a specific agent only?"

**Yes**, without a full workflow:

```
"@data — design a caching strategy for these endpoints"
```

Agent responds in character, no full 4-phase workflow unless you say "Mission:".

### "Where do I find the session journal afterwards?"

```
knowledge_base/sessions/YYYY-MM-DD-HH-<mission-slug>.md
```

Example:
```
knowledge_base/sessions/2026-04-11-14-feature-flag-system.md
```

---

## Next Steps After Your First Mission

1. **Review QUICK-REFERENCE.md** — Fast lookup for all commands
2. **Review SETUP.md** — Full feature documentation
3. **Review FEATURES.md** — Deep dives on individual features
4. **Create a spoke repo** — Add `.tng-context.md` to your API or frontend service
5. **Run a security audit mission** — `"Mission: Audit our GitHub Actions for security"`
6. **Run an architecture mission** — `"Mission: Design [component or system]"`

---

## Troubleshooting Your First Mission

| Symptom | Fix |
|---------|-----|
| "Crew not assembled" | Restart VS Code. Verify all agent files exist in `.github/agents/`. |
| picard doesn't respond | Wait 5 seconds. Sometimes there's a slight delay. |
| Ready Room won't close | Resolve all P1 items. Review Priority Triage summary. |
| Phase 2 seems stuck | Type `"@riker — status"` to get a report. |
| Tests failed in Phase 3 | This is expected. Review troi's findings. Decide: fix-in-place or scoped reopen. |

---

## Mission Statement Checklist

Before you type "Mission:", make sure your statement includes:

- [ ] **What** you want to build/decide/audit
- [ ] **Why** it matters (business value or risk reduction)
- [ ] **Scope** boundary (what's in, what's not)
- [ ] **Success criteria** (how you know it's done)

### Good Example:
```
Mission: Implement rate limiting for our API endpoints to prevent 
abuse and ensure service stability. Success = 95th percentile 
response time < 500ms under 1000 req/min load.
```

### Weak Example:
```
Mission: Fix the API
```

---

**Congratulations on your first TNG Agent Team mission!**

*"Make it so."*
