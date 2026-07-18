# CFA AI × Finance — Workshop Panel Summary

> **Source:** `Sum from seminar.md` (raw transcript + partial auto-summaries from the CFA Charterholder panel, Workshop Day 2026-07-11)
> **Purpose:** Extract the panel's *real* pain points and the judging rubric so we can pick a sharp problem and build a rubric-aligned deck (due **2026-07-19, 20:00**).
> **Who spoke:** 3 CFA Charterholders across Buy-Side, Sell-Side, and Strategy — each explicitly **handing us their workflow as a project "โจทย์" (problem to solve).**

---

## ⭐ START HERE — The Judging Rubric (this overrides everything)
*พี่เอม / Mattana Watcharawarathorn — Head of Investment Strategy, KAsset · CFA Thailand board*

This is exactly how **20 teams → 5 finalists**. Weight slide space to match.

| # | Criterion | Weight | What actually scores high |
|---|-----------|:---:|---|
| 1 | **Pain point + industry linkage** | **20%** | A problem so specific an insider thinks *"they already know what we struggle with."* Talk to the mentors/CFAs to find the **real** pain — don't guess. |
| 2 | **AI solution concept** | **25%** | Clear idea + *appropriate* technique. **Judges do NOT reward the most advanced tech — they reward tech that genuinely solves the problem.** |
| 3 | **Feasibility & reasonableness** | **20%** | The AI is not too exotic, not too hard — it *makes sense* that this problem should use this AI. |
| 4 | **Impact & value creation** | **20%** | **"Bigger problem, bigger solution."** Same clarity + bigger problem = more points. |
| 5 | **Slide quality & clarity** | **15%** | Broad-picture, self-explanatory (problem → solution). Speak slow, no jargon. Teams were cut in the 70→20 round for **unclear audio / bad presentation alone.** |

> ### 🔑 Key messages that stand out
> - **"ใครก็สร้าง AI ได้ แต่จะเอา AI มาแก้ปัญหาได้จริง ๆ ไม่ง่าย"** — anyone can build AI; solving a *real* problem with it is the hard part.
> - **"กรรมการไม่ได้มองหาเทคโนโลยีที่ล้ำที่สุด แต่มองหาเทคโนโลยีที่แก้ปัญหาได้จริง"** — pick the *fitting* tool, not the flashiest.
> - **Networking beats winning:** even if you don't win, pairing with a mentor/CFA can lead to internships or jobs. Ask to be matched.

---

## Panel 1 — Buy-Side / Private Fund (the flagship AI-in-production case)
*พี่โน้ต / "Note" — Head of Private Fund, SCB group (small hedge-fund-style shop)*

**What the fund does:** Takes client money → **active stock-picking** to *beat* the market (not track it).

### The strategy in one glance
- **5 target markets — all Emerging Asia:** 🇹🇭 Thailand, 🇻🇳 Vietnam, 🇮🇩 Indonesia, 🇮🇳 India, 🇨🇳 China.
- **Why EM, not the US:** developed markets are too efficient — passive ETFs already win there. EM has **lower information efficiency** → room for active alpha.
- **Active vs. Passive:** From ~800 Thai stocks they hold only **~10 best names** at a time — not 50–100 (mutual fund) or the whole index (passive).
- **The real edge is proprietary data:** public info + AI is now available to everyone → **no edge.** Their edge = non-public research: management meetings, suppliers, competitors, supply-chain contacts.

### 5-step workflow (the map to attack with AI)
1. **Investment Idea** (screen the 5-country universe)
2. **Paper + Meeting** (weekly Mon-PM meeting → best ideas go to the **Watch List**)
3. **Trading / Execution**
4. **Back-office Operations**
5. **Monitoring**
> Steps **1, 2, 5 = Investment Team (7–8 people); 3, 4 = Back Office (7–8 people).**

### Where AI is *already* running (last ~6 months)
- AI agents speed up **research & data summarization** — an analyst who could cover **3 stocks/day** now covers far more (no need to read 100-page annual reports manually).
- **Emerging quant play → factor Scoring:** ~**30 factors** score each stock; high scorers auto-surface into the Watch List. *(He half-joked this "is basically the project brief.")*
- **NOT yet automated:** actual trading/execution — still human-driven.
- **Building now (kept confidential):** a **proprietary Data Lake** — running AI/Big Data over data competitors don't have = durable edge.

> ### 🔑 Key messages that stand out
> - **"AI + Human, not AI 100%"** — the goal is to make *people* smarter/faster, not replace them.
> - **Scalability is the business:** AUM grew **~4–5B → 12B THB** (over ~6 yrs) while headcount rose by only **3–4 people**; ~15 staff total. Projects **30B THB with ≤20 people.** More AUM = more revenue, ~flat headcount → strong incentive to build AI.
> - **Hiring signal:** they now seek people who can bridge the **investment workflow (left) with AI/technical build (right).**

---

## Panel 2 — Strategy / Buy-Side Strategist (how market calls are made)
*พี่เอม / Mattana — Head of Investment Strategy, KAsset*

**The strategist's job in 4 lenses, feeding portfolio construction:**

1. **Macroeconomic** — GDP, PMI, CPI/PCE (inflation), M2/central-bank liquidity (Fed/ECB/BOJ), labor market → read the **Economic Cycle → Earnings Cycle → Financial Conditions.**
2. **Market** — movement across **Equity, Rates, Credit, FX, Commodity**; Volatility (VIX); Position/Flow (e.g., overcrowded KOSPI or 2x/3x speculative ETF flows → alert). *"What is the market trying to price/tell us?"*
3. **Ideas** — combine Macro + Market into a **recommendation** (sector / country / asset class to buy or sell).
4. **Portfolio** — express ideas as **SAA + TAA**.

### SAA vs. TAA (core framework)
| | **SAA — Strategic** | **TAA — Tactical** |
|---|---|---|
| Role | Core portfolio (~**80%**) | Satellite (~**20%**) |
| Horizon | **5–10 years**, rarely changed | **3–12 months**, opportunistic |
| Driven by | Capital Market Assumptions, big themes, high ROE | Macro + Market + Valuation dislocations |

### Case study — 2025 Reciprocal Tariffs ("Liberation Day," Apr 2)
Everything sold off together: **S&P −10% in 2 days, NASDAQ −11%, Energy −12%, Consumer Disc. −11%**; DXY down, bond yields *up*, gold and Bitcoin also down (stocks + bonds + dollar + gold all sold).

> ### 🔑 Key message that stands out — the alpha recipe
> **Find the "dislocation": where the market moved but it doesn't make sense.**
> A trade war should hit *risk* assets and push money *into* safe havens — yet gold fell too. That irrational move = the **trading idea** (e.g., add gold; buy sold-off US domestic-consumption names like Walmart that aren't actually export-exposed).
> **The 3-step logic to automate:** (1) only track macro indicators that *move* markets → (2) check if the market's reaction *makes sense* → (3) hunt the **dislocation** = the opportunity.

---

## Panel 3 — Sell-Side / Wealth Management
*พี่ริศา ("พี่ใหม่") / Risa Theerawat — Head of HN Strategy, KKP Securities · CFA Thailand board*

**Core reframe:** Wealth Management is **NOT just investing.** It's a **lifelong partnership** across every Stage of Life — **Protect → Grow → Transfer** wealth, "from birth to death to passing it on to the next generation."

### The lifecycle lens
- **Top triangle:** income/**Wealth Creation** rises while working, drops at retirement.
- **Bottom:** life goals to fund at each stage — house, car, children's education, travel, then **inheritance/legacy transfer.**
- Client conversations start with **goals** ("send kids to school," "retire early"), *then* products — via **Financial Planning**, not a product pitch.

### The project focus: **Mass Affluent (KKP Edge)**
| Tier | Investable assets | Note |
|---|---|---|
| High Net Worth | **50M+ THB** | Small in number; often *don't need* retirement planning — already wealthy. |
| **Mass Affluent (KKP Edge)** ← target | **2M–50M THB** | **High purchasing power + large in number + genuinely need goal-based planning** (retirement, education, budgeting). |

- Served under **KKP FG** (bank + securities + asset management): deposits, insurance, investments (stocks, mutual funds, hedge funds, private markets), and loans (home/car/business) — full coverage.

> ### 🔑 Key message that stands out
> The **Mass Affluent** are the sweet spot: rich enough to matter, numerous enough to scale, and **complex enough to need real financial planning** — unlike the ultra-wealthy who don't. This is where goal-based planning + AI can create the most leverage.

---

## 📌 So What — Implications for Our Deck
1. **The rubric is the spec.** AI Solution (25%) + Impact (20%) are the biggest levers — and *"bigger problem, bigger solution"* rewards picking a large, quantifiable pain point.
2. **Three ready-made problem domains, each explicitly offered as a project:**
   - **Buy-Side (Note):** factor **Scoring** to auto-surface stocks / speed EM research → clear pain, AI already proven internally.
   - **Strategy (Aim):** filter market-moving macro signals + **detect dislocations** for tactical calls.
   - **Wealth/Sell-Side (Risa):** goal-based **financial planning at scale** for the Mass Affluent.
3. **Frame every solution as "AI + Human," feasible, and appropriately-scoped** — the panel repeatedly signaled that fitting, deployable tech beats flashy tech.
4. **Next step (per CLAUDE.md):** pick ONE domain, fill the §7 "sector plug" template in `CFA AI jaa.md`, then build the ≤10-slide deck.
