# Pre-mortem Analysis — Cline Protocol

**Trigger**: When the user invokes `/premortem`, mentions "premortem", "pre-mortem", or asks to stress-test, pressure-test, or failure-analyze a plan.

**Purpose**: Prospective failure analysis. Assume the plan has already failed 6 months from now. Diagnose exactly how and why. Then derive the improvements that would have prevented each failure — and surface where the plan is actually stronger than feared.

---

## Activation

When triggered, announce:

> **Pre-mortem initiated.** Assuming it is now [6 months from today]. The plan has failed. Beginning failure analysis.

Load TNG personas from `.clinerules/TNG/` if available. If not available, run all steps as a single structured analysis.

---

## Step 1 — Context Intake

Gather the following if not already provided. Ask as a single list, not one question at a time:

- **Plan**: What is being launched, decided, or built?
- **Audience**: Who is the target? Who must adopt or approve it?
- **Success metrics**: What does "it worked" look like at 6 months?
- **Timeline**: Key milestones and go-live date
- **Resources**: Team size, budget, tooling, key dependencies
- **Constraints**: What cannot change? What is already locked in?
- **Owner**: Who is accountable for the outcome?

---

## Step 2 — Historical Pattern Check (guinan)

Before any failure analysis, scan `knowledge_base/documents/past-lessons-learned.md` if it exists. Have we seen this type of initiative fail before? What was the signal that was ignored?

State either:
- `[PATTERN-MATCH]` — we have seen this before; here is what happened
- `[NEW TERRITORY]` — no prior signal; the crew is operating without historical data

---

## Step 3 — Failure Narrative

Write the post-mortem as if it has already been filed. Past tense. Specific. Grounded in the context provided.

> *"It is now [6 months forward]. Here is the post-mortem that was submitted."*

Include:
- The moment the failure became undeniable
- The sequence of events that led there
- What stakeholders said when it collapsed
- What the team had been telling themselves was fine

No hedging. This happened. Write it that way.

---

## Step 4 — Domain Failure Analysis

Run analysis across all eight failure domains. For each domain, deliver:
1. **Failure story** — past tense, specific to the context given
2. **Early warning signs** — the signals that were visible but ignored
3. **Hidden assumption** — what the plan believed that turned out to be wrong
4. **Improvement** — the specific change that would have prevented it

Present each domain as a labeled section:

### Technical & Architectural Failures
Integration gaps, scalability assumptions that broke, data model blindspots, undocumented dependencies.

### Adversarial & Compliance Failures
External threats, regulatory traps, vendor lock-in, competitive responses, low-probability risks that materialized.

### People & Communication Failures
Stakeholder misalignment, adoption friction, change resistance, the thing no one said in the kickoff meeting.

### Operational & Reliability Failures
Resource exhaustion, support burden underestimated, failure cascades, things that worked in staging but not production.

### Complexity & Hidden Assumption Failures
The assumption that seemed safe, edge cases never simulated, components that were "just configuration" and weren't.

### Execution & Timeline Failures
Scope creep, dependency delays, capacity gaps, timing problems that were visible early but unaddressed.

### Unconventional / Black-Swan Failure
One scenario only. The failure no one modelled. Second-order effects, unexpected actor, external shift. Make it count.

---

## Step 5 — Synthesis

After all domains are analyzed, synthesize:

**Top 3 most likely failures** — ranked by probability with supporting evidence from the domain analysis.

**Top 3 most dangerous failures** — ranked by impact, regardless of likelihood.

**`[CRITICAL]` flag** — any failure that is both likely AND dangerous gets this flag. Treat as non-negotiable to address.

**The single biggest hidden assumption** — the one belief the plan depends on most that the analysis revealed as fragile. Name it explicitly.

**Improvement map** — for each major failure, state the concrete change that defuses it. Not abstract — something actionable before launch.

**Upside unlocks** — what the failure analysis reveals about where the plan is genuinely strong. Where fears turned out to be overblown. Where to lean in.

---

## Step 6 — Output

Produce the following artifacts in order:

### Failure Register
| Domain | Failure Story | Likelihood | Impact | Early Warning | Hidden Assumption | Improvement |
|--------|--------------|-----------|--------|--------------|-----------------|-------------|

### Risk Summary
- Top 3 most likely (with evidence)
- Top 3 most dangerous (with evidence)
- `[CRITICAL]` failures called out explicitly
- The single biggest hidden assumption

### Revised Resilient Plan
Specific, actionable changes to make before launch. Each change tied to the failure it prevents.

### Pre-Launch Checklist
Validation gates that must pass before going live. Each gate references the failure it guards against.

### 30/60/90-Day Pre-Success Indicators
Early signals that the plan is working before the final success metrics are measurable.

### Upside Unlocks
Where the plan is stronger than the fear analysis suggested. Where to invest more confidence and resources.

---

## Output Format

- Use markdown headers and tables for structure
- Keep failure stories to 3–5 sentences each — specific, not generic
- The improvement for each failure must be specific: a decision, a validation step, a design change, a conversation to have
- Pre-launch checklist items must be checkboxes: `- [ ] item [guards against: domain]`
- Do not pad with summaries of what you just wrote

---

## Rules

- Write failure narratives in past tense. No "could", "might", "may". It happened.
- Every hidden assumption must be a belief statement: "We assumed that X" — name what was believed
- Every improvement must be actionable before launch, not a general principle
- Do not skip the Upside Unlocks section — the user needs to know where the plan is strong, not just where it is weak
- If the plan context is thin, ask for more before writing the failure narrative — vague inputs produce useless failure stories
