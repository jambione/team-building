# Agent Team Playbook

## Core Principles

- Simplicity first, then performance, maintainability, and operational excellence.
- Single responsibility everywhere.
- picard is the single orchestrator. Every specialist must stay strictly in their lane.
- Use parallel execution when tasks are independent.
- Maintain and consult the shared knowledge base at `knowledge_base/documents/`.
- Every session is journaled at `knowledge_base/sessions/` for cross-session continuity.

---

## TNG Team (picard)

**Captain**: picard  
**Core Crew**: data, riker, geordi, worf, troi, crusher  
**Extended Crew**: barclay (tech debt), guinan (institutional memory), obrien (observability)  
**Variants**: picard-fast (quick tasks), picard-thinking (complex tasks)

### Standard Workflow

1. Open session journal (`knowledge_base/sessions/`) — picard
2. Consult historical context if needed → guinan
3. Check Knowledge Base (`knowledge_base/documents/`)
4. Architecture & Analysis → data (when needed)
5. Planning & Execution → riker
6. DevOps & Automation → geordi
7. Security & Compliance → worf
8. QA & Testing → troi
9. Reliability & Edge Cases → crusher
10. Technical Debt Assessment → barclay (each sprint or when refactors proposed)
11. Observability Review → obrien (each deployment or monitoring gap identified)
12. Synthesis, KB Update & session journal close → picard

---

## Handoff Acknowledgement Protocol

Every handoff is a two-part exchange:

1. **Specialist sends**: `"<agent> returns control to picard. [<trigger>]"`
2. **picard ACKs**: `[<trigger>-received ✓ picard]` at the top of the next response

A handoff with no ACK is **incomplete**. Any crew member may flag an unACKed handoff.

---

## Conflict Resolution Protocol

When two crew members produce conflicting recommendations:

1. Either crew member raises: `[CONFLICT: <agent-a> vs <agent-b>: <topic>]`
2. picard pauses the mission and requests written positions from both agents in the session journal.
3. picard consults relevant KB documents, decides, and records: `[CONFLICT-RESOLVED: <conflict-id>: <decision>]`
4. No crew member proceeds on a conflicted item until picard issues `[CONFLICT-RESOLVED]`.
5. Resolution is logged in `knowledge_base/documents/agent-performance-log.md`.

---

## Session Journal Protocol

- picard opens a new session journal at mission start using `knowledge_base/sessions/session-template.md`.
- Naming: `YYYY-MM-DD-HH-<mission-slug>.md`
- Journals track: decisions, handoffs, ACKs, `[NEW DISCOVERY]` flags, open items, conflicts.
- At mission close: journal is marked `status: closed`; guinan is notified for cross-session synthesis.
- guinan is the sole reader authorized to synthesize across session journals.
