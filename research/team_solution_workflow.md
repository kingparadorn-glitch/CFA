# Team Solution Workflow — Equity Research AI Co-Pilot

> Consolidated from `ai_architecture_design.md` + `equity_research_deep_dive.md`.
> Purpose: single reference to build the ≤10-slide deck (due 2026-07-19, 20:00) — this is the
> "how the solution actually works" backbone for the Problem → Solution → Impact slides.

---

## 1. One-sentence pitch

An **agent engine with a human-in-the-loop gate**, plugged with the real workflow of
**sell-side Equity Research**: agents draft the model, valuation, and report; a **licensed
analyst signs off** before anything publishes — turning the earnings-update bottleneck
(5.7 hrs → 45 min per company) into the flagship demo.

---

## 2. Two layers of the solution

| Layer                                                          | What it is                                                                                                                                                                     | Who owns it                                          |
| -------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------- |
| 🔵**Engine** (fixed, reusable across any finance sector) | 10 layers: ingestion, task map, agent orchestration, human-gate + state, memory, guardrails/retrieval, observability, governance/eval, schema contracts, model routing/caching | built once                                           |
| 🟠**Sector plug** (Equity Research, decided)             | Workflow steps, valuation formulas, input data, gate points — specific to how sell-side ER actually works                                                                     | supplied by finance team, "clicked in" to the engine |

This split is the core design argument: **the same engine could later plug into Wealth
Management, IB, or Risk** without rebuilding — ER is the flagship worked example, not the
whole product.

---

## 3. The pain point (why ER)

- One analyst covers **50–60+ companies**, must publish **at least once per company per
  quarter**, even with nothing new to say.
- During earnings season (~2–3 weeks/quarter): **~16 hr/day**, all companies report at once.
- Digesting one earnings release + call + updating the model + drafting a note currently
  takes **~5.7 hours per company** — this is the number the demo targets.
- Root cause is structural (coverage math), not laziness — evidenced from the CFA
  charterholder panel context and industry sources (Marvin Labs, WSO).

---

## 4. Demo scope: two flows

We build/demo **P1 (Coverage Initiation)** and **P2 (Earnings Update Cycle)** in full;
the other 5 ER workflows (Flash Note, Thematic Deep-Dive, Model Maintenance, Marketing,
Idea Generation) are shown as breadth the same engine already supports, not built out.

- **P1 — Coverage Initiation**: rare event, first time covering a new stock (initiation
  report, 20–50+ pages). Shows the engine handling a large, one-shot synthesis job.
- **P2 — Earnings Update Cycle**: the frequent, painful one (quarterly, time-critical).
  **This is the headline demo number**: 5.7 hr → 45 min (−87%).

---

## 5. P2 workflow — Earnings Update Cycle (headline demo)

```
Earnings released + call happens
        │
        ▼
┌─────────────────────────────────────────────┐
│ 1. Digest Results + Earnings Call NLP        │  agents: Digest-agent, Transcript-NLP-agent
│    - compute surprise vs prior estimate       │  (run in parallel)
│    - diarize/transcribe call → mgmt cues,     │
│      sentiment, guidance change               │
│    flag: |EPS surprise| > 10% → material      │
└─────────────────────────────────────────────┘
        │
        ▼
┌─────────────────────────────────────────────┐
│ 2. Update 3-Statement Model                   │  agent: Model-agent + Verify-agent
│    - roll actuals + new guidance into model   │
│    - model must "tie" (BS balances, cash ties)│
│    branch: model_ties == false → kick back    │
└─────────────────────────────────────────────┘
        │
        ▼
┌─────────────────────────────────────────────┐
│ 3. Re-value & Revise Rating                   │  agents: Valuation-agent, Rating-agent
│    - comps (primary) + DCF (cross-check)      │
│    - compare to IAA consensus target          │
│    gate: consensus_deviation > 15% → human    │
└─────────────────────────────────────────────┘
        │
        ▼
┌─────────────────────────────────────────────┐
│ 4. Draft Earnings Note                        │  agent: Note-agent + Fact-checker
│    - headline, key takeaways, estimate         │
│      revisions, rating line — every claim      │
│      carries a citation                        │
└─────────────────────────────────────────────┘
        │
        ▼
┌─────────────────────────────────────────────┐
│ 5. Compliance Review + Sign-off  ★ HARD GATE  │  actor: LICENSED ANALYST (human, mandatory)
│    - MiFID II / Reg AC / FINRA / IAA          │  no auto-publish possible
│    branch: not approved → back to draft        │
└─────────────────────────────────────────────┘
        │
        ▼
┌─────────────────────────────────────────────┐
│ 6. Publish                                    │  agent: Publish-agent + sales distribution
└─────────────────────────────────────────────┘
```

**Result:** what took 5.7 hours of manual digest → model update → valuation → drafting
now runs through agents in minutes, with the analyst spending their time on the ~45-min
judgment calls (gate 3 and gate 5), not the mechanical steps.

---

## 6. P1 workflow — Coverage Initiation (secondary demo)

Same 6-stage shape, heavier on stage 1 (ingest a 400–600 page prospectus/56-1 filing) and
stage 4 (draft a full 20–50 page report instead of a short note). Same hard gate at
Compliance sign-off. Shows the engine scales from a short reactive note to a long-form
synthesis job without changing the architecture — only the task map content changes.

---

## 7. Where the human sits (non-negotiable gates)

| Gate                          | Trigger                            | Why it can't be automated away                                                                                                                                                                  |
| ----------------------------- | ---------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Model-tie check               | model fails to balance             | numeric integrity — can't value a broken model                                                                                                                                                 |
| Consensus deviation           | AI target > 15% from IAA consensus | prevents AI from silently drifting from the Street with nobody noticing                                                                                                                         |
| **Compliance sign-off** | every report, every time           | **regulatory hard requirement** — MiFID II/Reg AC/FINRA require licensed-analyst sign-off before publication; SEC Thailand requires an analyst license; not a design choice, a legal one |

This directly answers the "feasibility & practicality" grading criterion (20 pts): the
solution is designed *around* the regulatory constraint, not in spite of it.

---

## 8. What makes numbers trustworthy (the "AI solution concept" differentiators)

- **Quant separated from LLM** — valuation math (comps, DCF, WACC) runs in **deterministic
  code**, not LLM-generated numbers. The LLM drafts prose; code computes figures.
- **Citation-by-ID** — every factual claim in a report must point to a source passage ID,
  or it can't be stated.
- **Number-level lineage** — every number in the output traces back to the exact cell in
  the source filing ("defend every number" — the standard auditors/regulators expect).
- **Self-consistency / uncertainty routing** — if agents disagree with themselves across
  repeated attempts, that's treated as a low-confidence signal and auto-routed to a human
  instead of silently guessing.
- **Point-in-time (PIT) data tagging** — retrieval is time-aware so the model can never see
  information published after the report date (avoids look-ahead bias).

---

## 9. Impact — quantified (for the "Impact & Value" criterion)

| Metric                                      | Value                                     | Source                                                                         |
| ------------------------------------------- | ----------------------------------------- | ------------------------------------------------------------------------------ |
| Time per earnings update                    | 5.7 hr → 45 min (−87%)                  | Marvin Labs                                                                    |
| Weekly time recovered per analyst           | 20–25 hrs/week                           | Marvin Labs (5 core workflows = 70–80% of analyst time; automation cuts ~40%) |
| JSON handoff failure rate (schema-enforced) | 8–15% → <0.1%                           | internal architecture design, 2M API call analysis                             |
| Cost reduction via model routing/caching    | 45–85% lower cost, ~95% quality retained | architecture design (route-then-cascade + semantic cache)                      |

---

## 10. Feasibility — addressing constraints head-on

- **Data**: demo uses a **public company as proxy** (candidate: MTC — has oppday decks,
  IAA consensus coverage, clear NIM driver as a financial stock) — no confidential/
  proprietary data, satisfies competition rules and real deployment feasibility alike.
- **Regulatory**: architecture is built around MiFID II/FINRA/IAA sign-off as a hard gate,
  not bolted on afterward.
- **Integration**: output objects (JSON schemas for model, valuation, note) are designed
  as clean handoffs — the kind of structured object that could feed an existing publishing/
  distribution system rather than requiring a rebuild.

---

## 11. Open items before the deck is finalized

- [ ] Confirm MTC (or alternative) as the demo proxy company
- [ ] Decide how much of P1 vs P2 gets slide real estate (P2 is the stronger, quantified
  story — likely the anchor demo slide)
- [ ] Pull 1–2 concrete before/after artifacts (e.g., a sample earnings note) if time allows,
  to make slide quality (15 pts) land as self-explanatory without a verbal pitch
