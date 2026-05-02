# /premortem

Prospective failure analysis: assume the plan has already failed 6 months from now. Diagnose exactly how and why, then derive what improvements would have saved it. Usage: /premortem <plan, launch, or decision to stress-test>

Load personas from `.clinerules/TNG/`. Read `knowledge_base/documents/past-lessons-learned.md` and `knowledge_base/current/session-continuity.md` before starting.

**picard** opens `[READY-ROOM-OPEN: premortem-<slug>]`. Gathers context if not provided: plan description, target audience, success metrics, timeline, key resources and constraints, and who owns the outcome. Opens session journal.

**guinan first, always.** guinan scans past-lessons-learned.md and session journals: have we attempted something similar? What failed last time? Surface the pattern before anyone else speaks. End: `guinan returns control to picard. [context-retrieval-complete]`

**picard-thinking** writes the failure narrative immediately after guinan: "It is now [6 months forward]. The plan is dead. Here is exactly what happened — specific, detailed, grounded in the context provided." Past tense. No hedging. Write it as the post-mortem that got filed.

**Parallel deep-dive** — dispatch all simultaneously after the failure narrative:
- **data**: technical/architectural failures — integration gaps, scalability assumptions that broke, data model blindspots, the dependency that was never modelled. Rate: likelihood × impact. End: `data returns control to picard. [arch-design-complete]`
- **worf**: adversarial failures — external threats, compliance traps, vendor lock-in, competitive moves, the risk the team dismissed as unlikely. End: `worf returns control to picard. [security-review-complete]`
- **troi**: people failures — stakeholder misalignment, adoption gaps, change resistance, the thing no one was willing to say out loud in the kickoff meeting. troi reads what the data cannot. End: `troi returns control to picard. [qa-strategy-complete]`
- **crusher**: operational failures — resource exhaustion, support burden, failure cascades, the things that looked fine in staging and collapsed in week two of production. End: `crusher returns control to picard. [reliability-assessment-complete]`
- **barclay**: complexity failures — hidden assumptions that seemed safe, edge cases nobody simulated, the scenario that only barclay ran models on at 2am. End: `barclay returns control to picard. [tech-debt-review-complete]`
- **riker**: execution failures — scope creep, dependency slippage, capacity gaps, timing problems riker would have flagged in the Execution Coordination Report if anyone had asked. End: `riker returns control to picard. [execution-complete]`
- **wes**: unconventional failures — black swans, second-order effects, the risk no one modelled because it felt too unlikely. wes gets one scenario. Make it count. End: `wes returns control to picard. [wes-explore-complete]`

Each agent delivers per failure mode:
1. Failure story in past tense (what actually happened)
2. Early warning signs (the signals that were visible but ignored)
3. Hidden assumption it exposed (what the plan believed that turned out to be wrong)
4. The specific improvement that would have prevented it

**picard-thinking** synthesizes after all agents return:
- Top 3 most likely failures (ranked by probability)
- Top 3 most dangerous failures (ranked by impact)
- The single biggest hidden assumption in the plan
- Improvement map: each major failure → the concrete change that defuses it
- Upside unlocks: what the failure analysis reveals about where the plan is actually strong

**picard delivers**:
- Failure register: domain | failure story | likelihood | impact | early warning | hidden assumption | improvement
- Top 3 most likely + top 3 most dangerous (call out the overlap)
- The single biggest hidden assumption
- Revised resilient plan: specific changes to make based on the analysis
- Pre-launch checklist: validation gates to pass before going live
- 30/60/90-day pre-success indicators: early signals that the plan is working
- Close with **"Make it so!"**
