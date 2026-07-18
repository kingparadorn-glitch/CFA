# CFA AI × Finance Hackathon — Team Workspace

This is not a software codebase — it's a working folder for a team competing in the
**AI × Finance Hackathon**, organized by CFA Society Thailand. Files here are competition
rules, an internal architecture concept doc, and raw recordings from the workshop day.

## Where things stand (as of 2026-07-15)

We are one of the **20 selected teams** (announced 2026-07-06), past the Orientation &
AI Workshop Day (2026-07-11), and now in the **build phase**: designing the solution and
preparing the slide deck due **Sunday 2026-07-19, 20:00** (`event@thailand.cfasociety.org`).

Full competition timeline (from the rules PDF):
| Stage | Date |
|---|---|
| Team registration | 2026-06-15 → 2026-06-28 |
| 20 teams announced | 2026-07-06 |
| Pre-workshop Zoom (tool setup) | 2026-07-07 |
| Orientation & AI Workshop Day (on-site, mandatory) | 2026-07-11 |
| **Slide deck submission (PDF, ≤10 slides)** | **2026-07-19, by 20:00** |
| 5 finalist teams announced | 2026-07-31 |
| Final round — 10 min pitch + 10 min Q&A | 2026-08-02, K+ Building |

## Competition rules that constrain our solution

- Deliverable for this phase: a **PDF, max 10 slides**, Thai or English.
- Judged on: quality of idea, understanding of the finance problem, real-world
  applicability, and communication to a professional audience.
- AI tools (ChatGPT, Claude, etc.) may assist analysis/drafting, but the core thinking,
  analysis, and ideas **must originate from the team** — cite any external data/models used.
- No confidential/proprietary data; must not reuse content already submitted to another
  competition; team composition is locked (no swapping members after confirmed registration).
- Full rules: `AI × Finance Hackathon_รายละเอียดสำหรับผู้เข้าแข่งขัน.pdf`.

## Our architecture concept — `research/ai_architecture_design.md` + `research/equity_research_deep_dive.md`

Core idea: a **generic agent engine + human-in-the-loop**, with **Equity Research
(sell-side)** as the flagship worked example.

- **Engine (fixed, built once)**: grounding/citation, maker-checker debate, numeric
  verification vs. source, precision/recall eval against a gold set, human-in-loop gating
  with state (so re-runs are incremental, not from scratch).
- **Sector plug (Equity Research, decided)**: workflow steps, the quant/math framework the
  sector actually uses (comps/multiples primary, DCF cross-check), input data, and where a
  human must gate the process — fully specified in `research/equity_research_deep_dive.md`.
- 3-layer structure: Task Map (finance-defined) → Agent Orchestration (engine) →
  Human-Loop + State (engine).
- ER flagship flow (demo = P1 Coverage Initiation + P2 Earnings Update Cycle): Ingest &
  Primer → Financial Modeling → Valuation & Rating → Draft Report → Compliance Review +
  Sign-off (hard gate, licensed analyst) → Publish.
- Open gaps: which public company to use as a data proxy for the demo (candidate: MTC —
  see `research/equity_research_deep_dive.md` §20).

**Immediate next step**: turn the Equity Research pipeline spec into the ≤10-slide deck.

> Note: `CFA AI jaa.md` and the Private Equity sections of the research files describe an
> earlier direction (PE as flagship) that the team has since moved on from. They're kept
> as reference but should not be treated as current.

## Grading criteria — how the slide deck gets scored (100 pts, cuts to 5 finalists)

From `4. Grading Criteria_เกณฑ์การคัดเลือก 5 ทีมเข้าสู่รอบชิง.pdf`. Weight decisions and
slide space toward this breakdown — the AI solution concept alone is worth as much as
the other three content criteria combined:

| Criterion | Points | What scores high (16–20 / top band) |
|---|---|---|
| Problem identification & industry linkage | 20 | Sharp, specific pain point with real evidence it matters to actual finance workflows — not just "related to the industry" |
| **AI solution concept** | **25** | Creative, logically sound, technically credible approach with an appropriate technology choice (LLM, ML model, RPA, etc.) and a clearly explained mechanism |
| Feasibility & practicality of implementation | 20 | Credible, realistic path to real deployment — explicitly addresses data limitations, regulatory constraints, and integration with existing financial industry systems |
| Impact & value creation | 20 | Strategic, measurable impact (efficiency, cost reduction, risk management, or customer experience) with a reasoned impact estimate |
| Slide quality & clarity | 15 | Professional, well-structured storytelling; reader understands problem, solution, and impact directly from the slides alone, within 10 pages, with no extra explanation needed |

Implications for how we build the deck:
- **AI solution concept (25 pts) is the single biggest lever** — don't under-invest here
  relative to the problem framing.
- Feasibility scoring explicitly checks for **data constraints, regulatory constraints, and
  system integration** — the deck should address these head-on, not gloss over them.
- Impact needs to be **quantified/measurable**, not just "this will help."
- Slide quality is graded on whether the deck is **self-explanatory** — assume no verbal
  pitch is happening at this stage (that's reserved for the final round).

## Other files in this folder

- `Jubilee Prestige Hotel Ratchadapisek.m4a`, `New Recording 56.m4a`,
  `Siam Sport World Co.,.m4a`, `Recording 2026-07-13 103401.mp4` — raw audio/video from
  workshop day, likely including the **CFA Charterholder panel** (Investment Banking /
  Wealth Management / Fund Management pain points) that's meant to seed our problem
  selection.
- `CFA/` — an Obsidian vault, currently just scaffolding (`Welcome.md`, empty `s.md`).

## Working with this project

- When asked to help build the solution: ground suggestions in the actual competition
  rules and deadlines above, not generic hackathon advice.
- Keep the slide deck within the stated constraints (≤10 slides, PDF, cite external
  sources) since rule violations are Pass/Fail before content is even judged.
