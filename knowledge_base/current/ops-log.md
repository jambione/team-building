# Ops Log

> **Purpose**: Lightweight rolling log for quick notes, KB queries, and observations.
> No phases. No handoffs. No crew ceremony.
> Invoke: `Computer: record — [your note]`
>
> **Owner**: Computer (auto-appended)
> **Rolling window**: Keep last 50 entries. Archive older entries to
>   `knowledge_base/archive/ops-log-archive-YYYY-MM.md` when this file exceeds 50 entries.
> **Read by**: guinan (cross-session pattern detection), picard (ops context at mission open)

---

## Log Entries

<!-- Entries are prepended here — newest first. -->

**[2026-04-13]** `[COMPUTER-RECORDED]` — Uncommitted changes audit on branch `chore/agent-setup-v2`. No sessions or missions have pending changes. All knowledge_base/sessions/ and knowledge_base/missions/ are clean.

**New files (untracked — not yet staged):**

| File | Description |
|---|---|
| `.clinerules/TNG/computer.md` | Computer agent personality + KB routing map for VS Code / clinerules |
| `.github/agents/computer.agent.md` | Computer agent definition for GitHub Copilot (YAML frontmatter + rules) |
| `knowledge_base/current/ops-log.md` | This file — lightweight rolling ops log, 50-entry window |

**Modified files (not yet staged):**

| File | Change |
|---|---|
| `docs/guides/QUICK-REFERENCE.md` | +34 lines — added Computer section (decision table, invocation examples), Computer row to Agent Quick Reference, ops-log row to Key Files |
| `knowledge_base/documents/index.md` | +1 line — ops-log added to Session Continuity section |

**Sessions / Missions status:** Clean. No uncommitted changes in `knowledge_base/sessions/` or `knowledge_base/missions/`.

**[2026-04-13 00:00]** `[COMPUTER-RECORDED]` — Ops log initialized. Computer agent online.

---

## Archive Index

| Archive File | Date Range | Entry Count |
|---|---|---|
| _(none yet)_ | | |
