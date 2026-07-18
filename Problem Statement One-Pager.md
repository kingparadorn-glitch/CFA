# Problem Statement — One-Pager Outline (4-Quadrant)

> Draft content for the deck's "Problem identification & industry linkage" slide(s).
> Three roles carry **equal weight** as parallel personas — do not let ER dominate; PM and IB get matched treatment even though the underlying data depth differs (noted below).
> Every stat is tagged with its source file. **[GAP]** = no verified number exists; flagged so it doesn't get overclaimed on the slide.

---

## Quadrant 1 (top-left) — WHO: The Research/Analysis Roles

| Role | What they own | Where they sit |
|---|---|---|
| **Fund Manager (buy-side PM)** | Capital allocation decisions — idea generation → thesis validation → portfolio construction/rebalancing → monitoring/risk → client reporting | Asset manager / hedge fund |
| **IB Associate (sell-side FA)** | Deal execution — financial due diligence, trading comps, valuation, contract/risk review that determines if a deal happens and at what price | Investment bank / boutique FA |
| **Equity Research Analyst** | Stock coverage — 3-statement models, ratings, price targets, published research notes that institutional clients trade on | Brokerage / IB research desk (sell-side) |

*Sources: `research/2. PM.md`, `Dcap.md` + `research/6. IB.md`, `Blank/02_sector_db/equity_research_deep_dive.md` §2*

---

## Quadrant 2 (top-right) — IMPACT: Market Size & KPIs

| Role | KPI that matters to the firm | Number |
|---|---|---|
| **Fund Manager** | AUM growth per headcount (scalability = the business) | Real Thai case: AUM grew **~4-5B → 12B THB over ~6 years** on ~flat headcount (~15 people); next target **30B THB with ≤20 people**. Industry backdrop: Thai mutual + private fund AUM = **6.5T + 2.3T THB (~54% of Thai GDP)** |
| **IB Associate** | Deal value enabled / protected by DD quality | Thailand M&A Q1 2026: **57 deals, US$7.9B** (up from $1.3B in Q4 2025); average deal size **~$47.7M** (2024) — DD determines whether these deals close at the right price |
| **Equity Research Analyst** | Output quality feeding trading commission (research = client-facing "marketing" for the desk) | **[GAP]** — no clean Thai $ figure for commission generated per analyst/coverage found. Use as proxy instead: **94.5% of analysts rely on comps-based valuation**, with a **55.1% price-target hit rate** — i.e., output quality is measurable even where $ attribution isn't |

*Sources: `Seminar Summary — Structured.md` (Panel 1), `Thai AI Finance Opportunity Validation.md` Domain 1 & 2, `equity_research_deep_dive.md` §11*

**Framing note:** PM and IB both have hard $ market-size numbers; ER's strongest KPI is a quality/coverage metric, not a $ figure — say this plainly rather than forcing an unsupported revenue number onto the slide.

---

## Quadrant 3 (bottom-left) — PAIN: Hours, Workload, Why It's Crucial

| Role | Pain point | Evidence |
|---|---|---|
| **Equity Research Analyst** | Coverage overload + earnings-season crunch | Covers **50-60+ companies** each; must publish minimum 1 note/company/quarter; **12h/day normal, 16h/day during earnings season**; **70-80% of time** on 5 recurring workflows; earnings review alone = **5.7hr/company pre-AI** |
| **IB Associate** | DD bottleneck + non-standardized data | DD takes **2 weeks to 1 month per deal**; trading comp reconciliation across mismatched sources (SET vs Cap IQ methodology) is the single hardest step; boutique-firm structure means no hierarchy — pressure concentrates on few people |
| **Fund Manager** | Information overload, not information scarcity | Must triage earnings, news, macro, sell-side notes, filings, and risk output into real-time decisions. **[GAP]** — no verified public benchmark for PM hours/week exists (industry has no standard survey on this); treat any hours claim here as directional, not fact |

**Cross-functional drag (the "so what"):** this bottleneck is exactly what forces headcount into analysis/investment functions instead of scaling revenue-facing work. The fund-manager case above is the clean proof: when analysis got faster, AUM scaled while headcount didn't move.

*Sources: `equity_research_deep_dive.md` §12, `Dcap.md`, `research/2. PM.md`*

---

## Quadrant 4 (bottom-right) — BOTTOM LINE: How the Investment Function Reflects in Firm P&L

- **Buy-side:** AUM 4-5B→12B THB in 6 years on flat headcount (~15 people), next target 30B THB with ≤20 people — the investment/research function is a **direct revenue multiplier**, not a cost center, when it scales without scaling cost.
- **Sell-side ER:** faster/broader coverage at the same headcount = more client touchpoints = more trading commission (ER's actual commercial purpose).
- **Sell-side IB:** DD speed and quality directly gate deal value captured (advisory fees scale with completed deal value, not hours billed).
- **Bank-wide macro tailwind:** Thai commercial banks are explicitly pivoting toward **non-interest/fee income** (wealth, research-driven advisory) as loan growth slows — this makes research-function efficiency a direct, current P&L lever for the industry, not a hypothetical future benefit.

*Sources: `Seminar Summary — Structured.md`, `Thai AI Finance Opportunity Validation.md` Executive Summary*

---

## Open items before this goes on a slide
1. **ER $-impact KPI is a real gap** — either find/estimate one (e.g., average commission per covered name) or keep the quality-metric framing and own it explicitly.
2. **PM hours/week has no public benchmark** — decide whether to omit the hours claim for PM entirely or caveat it visibly on the slide.
3. Given equal-weight framing, the slide will be dense at 3 roles × 4 quadrants — may need two slides (problem framing / impact-and-pain) rather than one, to stay legible per the "self-explanatory, no verbal pitch" grading criterion.
