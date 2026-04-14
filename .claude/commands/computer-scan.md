# /computer-scan

Computer-orchestrated parallel scan of uncommitted GitHub changes. No Ready Room. No mission ceremony. Sub-agents run their learning loop against the current diff and document any discoveries. Results recorded to ops-log.

---

## Step 1 — Computer: Inventory the Diff

Run `git status` and `git diff` (including untracked files) to build the change inventory.

```
[COMPUTER-QUERY: git-status | building change inventory]
```

Produce a **Change Inventory Table**:

| File | Status | Domains Touched |
|---|---|---|
| `<path>` | modified / new / deleted | architecture / security / devops / qa / debt / reliability / observability |

Domain tagging rules:
- `.github/workflows/` or `ci` or `docker` → **devops**
- `auth`, `token`, `secret`, `permission`, `cred` → **security**
- `test`, `spec`, `coverage` → **qa**
- `architecture`, `design`, `pattern`, `adr` → **architecture**
- `debt`, `refactor`, `duplicate`, `TODO` → **debt**
- `monitor`, `alert`, `metric`, `log`, `slo` → **observability**
- `error`, `rollback`, `migration`, `retry`, `timeout` → **reliability**
- agent files (`.clinerules/`, `.github/agents/`) → **architecture + security**
- KB documents (`knowledge_base/`) → **architecture**
- Anything else → flag domain as **general**

---

## Step 2 — Computer: Dispatch Parallel Learning Loop

Based on domains identified in Step 1, dispatch the relevant agents **in parallel**. Print the dispatch board:

```
⚡ PARALLEL SCAN — uncommitted-changes
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  [agents listed by domain match]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Dispatching <N> agents in parallel...
```

**Domain → Agent routing:**

| Domain | Agent | KB Document |
|---|---|---|
| architecture | data | `architecture-principles.md` |
| security | worf | `github-actions-security-hardening.md` |
| devops | geordi | `devops-best-practices.md` |
| qa | troi | `best-practices.md` |
| reliability | crusher | `monitoring-observability.md` |
| debt | barclay | `tech-debt-register.md` |
| observability | obrien | `monitoring-observability.md` |
| always included | guinan | `past-lessons-learned.md` |

guinan is always dispatched regardless of domain — cross-session pattern detection runs on every scan.

---

## Step 3 — Each Agent: Learning Loop

Each dispatched agent runs this loop against the uncommitted diff:

1. **Read** their assigned KB document
2. **Read** the relevant changed files from the diff
3. **Analyze** through their domain lens only — stay in lane
4. **Report** findings in third person with their catchphrase
5. **Flag** any undocumented finding as `[NEW DISCOVERY: <kb-doc> | <proposed text>]`
6. **Update** their KB document directly if a discovery warrants it — use the Edit tool
7. **Emit** one of:
   - `[KB-UPDATED: <doc> | <nature of change>]`
   - `[KB-NO-CHANGE: <doc> | reason: <brief>]`
8. **Return** control: `[<agent>-scan-complete]`

Agents report only on what is in the diff. No scope creep into the broader codebase.

---

## Step 4 — Computer: Completion Board + Ops-Log Record

Print the completion board:

```
✅ PARALLEL SCAN COMPLETE — uncommitted-changes
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ✓ [agent]  [KB-UPDATED or KB-NO-CHANGE]
  ...
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

Then write a single consolidated entry to `knowledge_base/current/ops-log.md` (prepend, newest first):

```
**[YYYY-MM-DD HH:MM]** `[COMPUTER-RECORDED]` — /computer-scan complete.
Files scanned: <N> | Agents dispatched: <N> | Discoveries: <N> | KB updates: <N>

**Changes inventoried:**
- `<file>` — <status> — <domains>

**Discoveries:**
- [NEW DISCOVERY] `<kb-doc>` — <finding> (owner: <agent>)
- _(none)_ if no discoveries

**KB updates made:**
- [KB-UPDATED] `<doc>` — <nature> (agent: <agent>)
- _(none)_ if no updates
```

Emit `[COMPUTER-RECORDED: /computer-scan — <N> discoveries, <N> KB updates]`.

---

## Step 5 — Computer: Escalation Check

If any discovery is flagged with P1 or P2 risk by an agent, emit:

```
[COMPUTER-ROUTED: picard | <N> P1/P2 discoveries found — recommend Mission: review scan findings]
```

Otherwise close with:

```
Scan complete. <N> files reviewed. <N> discoveries documented. <N> KB updates made.
```
