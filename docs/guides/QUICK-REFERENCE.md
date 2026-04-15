# TNG Agent Team — Quick Reference Card

**Print this or bookmark it.** One-page lookup for common tasks.

---

## Mission Workflow (4 Phases)

| Phase                         | Who                   | What                                | When Done                              |
| ----------------------------- | --------------------- | ----------------------------------- | -------------------------------------- |
| **Phase 1: Ready Room**       | picard + 6 agents     | Parallel analysis, decisions locked | `[READY-ROOM-CLOSED]`                  |
| **Phase 2: Bridge Execution** | riker + team          | Code/tasks executed, handoffs       | `[execution-complete]`                 |
| **Phase 3: Track C Review**   | worf + troi + crusher | Security, QA, reliability gates     | Verdict issued (PASS/FAIL/CONDITIONAL) |
| **Phase 4: Mission Close**    | picard                | KB updated, debrief captured        | **"Make it so."**                      |

---

## Agent Quick Reference

| Call This  | For This                                         |
| ---------- | ------------------------------------------------ |
| `@data`    | Architecture, design, patterns, scalability      |
| `@geordi`  | GitHub Actions, docker, CI/CD, caching           |
| `@worf`    | Security, tokens, compliance, secrets            |
| `@troi`    | QA, testing strategy, UX, quality gates          |
| `@crusher` | Reliability, edge cases, failure modes, rollback |
| `@barclay` | Technical debt, refactoring, DRY/YAGNI           |
| `@obrien`  | Monitoring, metrics, alerting, observability     |
| `@wes`     | Cross-model alternative proposals — runs on a different Copilot model than the crew (approval required) |
| `@guinan`  | Historical context, past lessons, carry-forwards |
| `Computer` | KB queries, note recording, doc lookup, quick answers — no ceremony |

---

## Computer — Always-On Lightweight Agent

**Invoke with**: `Computer: [query or command]`

No phases. No Ready Room. No crew dispatch. Just an answer or a record.

### When to Use Computer vs Full Team

| Task | Use |
|---|---|
| Query a KB document | Computer |
| Look up document ownership | Computer |
| Record a quick observation | Computer |
| Check current sprint / carry-forward state | Computer |
| Get a session-continuity summary | Computer |
| Make an architecture or design decision | Full team (picard) |
| Security review or code change | Full team (picard) |
| Multiple agents needed | Full team (picard) |

### Invocation Examples

```
Computer: what does architecture-principles.md say about stateless design?
Computer: record — worf and crusher should be mandatory for any external integration
Computer: who owns monitoring-observability.md?
Computer: look up the circuit breaker pattern
Computer: what are the open carry-forwards for this sprint?
Computer: summarize ops-log from this week
```

### Parallel Diff Scan

Run `/computer-scan` to dispatch sub-agents in parallel against all uncommitted changes. Each agent analyzes the diff through their domain lens, flags discoveries, and updates their KB document. Results recorded to ops-log.

```
/computer-scan
```

### wes Diff Suggestions (cross-model, no mission needed)

Run `/wes-diff` to invoke wes standalone against uncommitted changes. **First switch Copilot's model picker to wes's designated model** (opposite series from the crew — see routing table in `wes.agent.md`). wes reads the diff and produces up to 3 cross-model proposals on how the changes could be approached differently. No picard required. No mission ceremony.

```
/wes-diff
```

| Crew's active model | Switch Copilot to before running /wes-diff |
|---|---|
| Claude | GPT-4o mini → GPT-4o → o3-mini |
| GPT-4o / GPT-4o mini | Claude 3.5 Sonnet → Claude 3.7 Sonnet |
| Gemini | GPT-4o mini → GPT-4o → o1 |

---

## Common Commands

### Start Full Mission Workflow

```
"Mission: [your objective]"
```

Triggers all 4 phases.

### Request Single Agent Analysis (No Workflow)

```
"@data — design a caching strategy for this API"
```

Agent responds in character, no full workflow.

### Open Ready Room Only (Decision Phase Only)

```
"Open the Ready Room for: [topic]"
```

### Check Knowledge Base

```
"Show me past lessons learned around [topic]"
"@guinan — what carry-forward items are open?"
```

---

## Phase 1 Triggers Ready Room

Just state your mission:

```
"Integrate Claude API into CI pipeline for automated PR reviews"
```

Then:

1. picard opens Ready Room
2. guinan surfaces history
3. 6 agents analyze in parallel (data, worf, troi, crusher, barclay, obrien)
4. picard assembles **Mission Decision Record (MDR)** with decision, options, rationale, risks, crew assignments
5. picard issues hard close: `[READY-ROOM-CLOSED]`

---

## Phase 2: Execution Coordination

riker announces tasks:

- Which agents are assigned
- Parallel vs. sequential order
- Dependencies

Each agent works in-character, speaks opening phrase → does work → speaks closing phrase → hands to riker.

**Key rule**: Every action announced BEFORE the work, never after.

---

## Phase 3: Quality Gates (Mandatory)

Three reviewers publish findings directly in chat:

1. **worf — Security Review**

   - VERDICT: PASS / FAIL / CONDITIONAL
   - Lists security issues by severity

2. **troi — QA & Quality Review**

   - VERDICT: PASS / FAIL / CONDITIONAL
   - Test coverage, UX concerns

3. **crusher — Reliability Review**
   - VERDICT: PASS / FAIL / CONDITIONAL
   - Edge cases, failure modes

picard then issues Go/No-Go and classifies open items as:

- **Fix-in-place** — resolve now
- **Scoped Ready Room** — brief re-analysis needed
- **Full Reopen** — major changes needed

---

## Phase 4: Mission Close

1. Agents update their KB documents
2. picard fills **Mission Debrief**
3. Session journal marked `closed`
4. picard closes: **"Make it so."**

guinan now knows about this session for future reference.

---

## Session Journal Location

```
knowledge_base/sessions/YYYY-MM-DD-HH-<mission-slug>.md

Examples:
  2026-04-05-10-claude-api-pr-review.md
  2026-04-11-10-dark-mode-toggle.md
```

---

## Spoke Repo Setup

Optional but recommended for auto-routing: copy `.tng-context.md` into each service repo and fill out:

```yaml
repo_name: "org/service-api"
service_domain: "Backend REST API — auth and accounts"
owner_agent: "data"
status: "active"
```

If no `.tng-context.md` exists, routing falls back to `knowledge_base/current/workspace-context.md` and picard asks for confirmation when needed.

---

## Critical Rules

❌ **No code until `[READY-ROOM-CLOSED]` is issued**

❌ **No P0/P1 items unresolved at Close**

❌ **No handoff without ACK signal**

❌ **All agents speak in third person** ("picard has", not "I have")

✅ **Always reference KB documents when stating missions**

✅ **Let guinan speak first in Ready Room**

✅ **Capture learning in debrief at Phase 4 close**

---

## Troubleshooting (TL;DR)

| Problem                | Fix                                                                                  |
| ---------------------- | ------------------------------------------------------------------------------------ |
| "Crew not assembled"   | Check agent files in `.github/agents/` exist. Restart VS Code.                       |
| Ready Room won't close | Resolve all P0/P1 items. Review Priority Triage.                                     |
| Agent doesn't respond  | Verify agent name spelling; use `@name` format.                                      |
| History not mentioned  | Check `past-lessons-learned.md` has recent entries. Session journals must be closed. |
| Token permission error | Reference `github-actions-security-hardening.md`. Never use `write-all`.             |
| Track C verdict = FAIL | Review findings. Decide: fix-in-place, scoped reopen, or full reopen.                |

---

## Key Files

| File                                               | Purpose                                                              |
| -------------------------------------------------- | -------------------------------------------------------------------- |
| `.github/copilot-instructions.md`                  | System initialization (don't edit unless you know what you're doing) |
| `.github/agents/*.agent.md`                        | Agent personas (reference only)                                      |
| `TEAM-TOPOLOGY.md`                                 | Agent roster and canonical routing                                   |
| `STATUS.md`                                        | Workflow activation status                                           |
| `RUNBOOK.md`                                       | Decision/execution guidelines                                        |
| `docs/guides/SETUP.md`                             | Full setup guide (detailed version)                                  |
| `workspace-config.json`                            | Workspace validation/routing contract defaults                       |
| `scripts/workspace_config.py`                      | Shared config loader used by validators                              |
| `knowledge_base/documents/index.md`                | KB navigation                                                        |
| `knowledge_base/documents/past-lessons-learned.md` | Lessons from prior missions                                          |
| `knowledge_base/documents/sprint-state.md`         | Open carry-forwards                                                  |
| `knowledge_base/current/ops-log.md`                | Rolling lightweight log — Computer-recorded notes and queries        |
| `.tng-context.md` (optional in spoke repos)        | Service identity override for repo-local auto-routing                |

---

## Voice Examples

Each agent has a distinctive opening and closing:

- **data**: _"Processing. There is a pattern here."_ → _"Fascinating."_
- **worf**: _"worf does not look for problems."_ → _"The defense holds. Qapla'."_
- **troi**: _"troi senses more than metrics show."_ → _"troi has said what needs saying."_
- **crusher**: _"Let crusher look at vitals first."_ → _"Stable is not healthy."_
- **geordi**: _"Give geordi a few minutes."_ → _"I can make that work."_

---

## Next Steps

1. **First time?** Read `docs/guides/SETUP.md` (full version)
2. **Starting a mission?** State it clearly with scope and success criteria
3. **Questions about agents?** See `.github/agents/<name>.agent.md`
4. **Knowledge base?** Browse `knowledge_base/documents/index.md`
5. **Need history?** Ask `"@guinan — what is the history here?"`

---

**"Make it so."**
