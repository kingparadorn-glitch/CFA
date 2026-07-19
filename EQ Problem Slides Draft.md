# EQ Research Problem Framing — Draft (2 slides)

Status: DRAFT for review. Global/industry stats are well-sourced; **Thailand-specific numbers below are placeholders** — I could not find a public, citable figure for "number of TH-licensed investment analysts" or "SET-listed companies with active analyst coverage" via web search. Flagging exactly where you need to plug in a real number or a workshop-panel quote before this goes in the deck (per your rules doc: cite external data, core thinking must be the team's).

---

## Slide 1 — Why Equity Research, and how big is the problem

**What EQ research is (1 line):**
Equity research analysts build financial models and forecasts on covered companies, then translate them into research reports and recommendations that fund managers, IBs, and traders act on. It's the analytical layer that sits between raw company disclosures and every buy/sell/deal decision downstream.

**Why it matters to the firm / market (impact):**

- EQ output isn't just "one report" — it's consumed by fund managers making allocation calls, IB teams pricing deals and building pitch comps, and corporates on the deal side. A single earnings model error or delay propagates into every downstream decision that relies on it.
- During earnings season, analyst workload spikes sharply: outside earnings season the role is closer to standard hours, but during reporting weeks analysts are pushed toward 10–12+ hour days updating models, revising forecasts, and publishing under deadline pressure. [Toptal — Equity Research Analyst Job Description](https://www.toptal.com/finance/equity-research-analysts/job-description)
- Historically, **~80% of an analyst's time goes to manual data extraction/organization, leaving ~20% for actual analysis and insight** — the exact inversion of what the role is supposed to be for. [Daloopa — AI-Powered Earnings Report Analysis](https://daloopa.com/blog/analyst-best-practices/ai-powered-earnings-report-analysis)
- Separately, analysts spend **60–70% of their time** building models, parsing filings, and writing reports across a 15–20 company coverage universe. [Marvin Labs — Equity Research Automation](https://www.marvin-labs.com/resources/equity-research-automation/)

**Market-sizing option (TH) — needs a real number, pick one:**

- Placeholder A: number of SET-listed companies (~800+ tickers trade on SET per market trackers, though this figure needs verification against SET's own investor stats page: [SET Market Overview](https://www.set.or.th/en/market/product/stock/overview)) × estimated analyst coverage ratio.
- Placeholder B: Thailand's total mutual fund assets under management reached **USD 284B as of end-2024** (~15.7M beneficiary accounts), per AIMC — every baht of that AUM is allocated using research that traces back to EQ analyst output. [AIMC / Caproasia summary](https://www.caproasia.com/2026/05/06/thailand-association-of-investment-management-companies-aimc-proposes-private-trust-framework-for-private-wealth-management-position-thailand-as-regional-asset-management-hub-targets-30-billion/)
- Placeholder C (strongest if you can get it): number of SEC Thailand-licensed investment analysts/consultants. SEC maintains a public searchable registry but I could not extract a total count via search — pull this directly from [SEC&#39;s IC01 licensee list](https://market.sec.or.th/public/orap/IC01.aspx?lang=en) or SET's [Investment Analyst program page](https://www.set.or.th/th/education-research/education/professional/investment-analyst).

**Suggested framing for the slide:** lead with the AIMC AUM figure (it's the most solid, citable number found) — "Every year, [X trillion baht / USD 284B] in Thai fund assets is allocated on the back of equity research that still runs on largely manual, earnings-season-bottlenecked workflows."

---

## Slide 2 — Where EQ analysts (and adjacent roles) lose time

| Role                              | Core JD                                                                                         | Where earnings-report flow hurts                                                                                                                      | Time cost                                                                                                                                                                                                                                                                                                                                                                                                         |
| --------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Fund Manager / PM**       | Allocate capital based on research + own view; monitor portfolio names through reporting season | Manual reading/extraction of earnings docs into a consistent schema; reconciling inconsistent data across systems to flag discrepancies before acting | Front-office staff lose meaningful time daily to unraveling data inconsistencies from disparate systems[Linnovate Partners](https://linnovatepartners.com/the-role-of-analytics-and-reporting-in-effective-portfolio-management/); PMs already work 45–60 hrs/week even outside earnings crunch [FE Training](https://www.fe.training/free-resources/careers-in-finance/a-day-in-the-life-of-a-portfolio-manager/) |
| **IB (deal/coverage team)** | Pitch comps, deal execution support, financial restatement handling                             | Updating financials whenever a covered company restates earnings; manually building comps under same-day MD deadlines                                 | A typical analyst morning includes ~15 new deal-document emails plus ad hoc "summarize this by EOD" requests[V7 Labs — AI in IB](https://www.v7labs.com/blog/best-ai-tools-for-investment-banking)                                                                                                                                                                                                                |
| **EQ Analyst**              | Build/maintain earnings models, write reports, cover 15–20 names                               | Extracting numbers from filings/transcripts by hand, reconciling line items into the model, then re-deriving the same numbers every quarter           | ~80% manual extraction vs. ~20% analysis historically[Daloopa](https://daloopa.com/blog/analyst-best-practices/ai-powered-earnings-report-analysis); earnings calls now run ~90 min vs. ~45 min historically, adding to the parsing burden [Marvin Labs 2026](https://www.marvin-labs.com/blog/equity-research-in-2025-evolution-in-the-ai-era/)                                                                    |

**Shared pain across all three roles:** the bottleneck isn't judgment — it's the manual document-to-structured-data step between "company publishes earnings" and "I can actually reason about the number." Every role above is re-doing that extraction independently, on the same underlying disclosure, on the same tight earnings-week timeline.

**Evidence / quote — ACTION NEEDED:**
Your outline calls for a quote proving this pain is real, not hypothetical. I did not fetch this — it needs to come from your own workshop recordings (`Jubilee Prestige Hotel Ratchadapisek.m4a`, `New Recording 56.m4a`, `Siam Sport World Co.,.m4a`, or `Recording 2026-07-13 103401.mp4`), since that's primary evidence from the CFA charterholder panel and scores higher than a generic industry stat. Suggest: transcribe the relevant segment, pull one specific line where a panelist describes time lost to earnings-report handling, and cite it with a timestamp.

---

## Open items before this is deck-ready

1. **Pick ONE market-sizing stat for Slide 1** (AUM is best-sourced; analyst-count/coverage-ratio would be stronger but needs a direct pull from SEC/SET, not search).
2. **Pull the actual workshop quote** for Slide 2 — this is the one thing I can't source for you.
3. Global stats above (80/20 split, 60–70% time-on-modeling, 90-min earnings calls) are from **US/global equity research sources**, not Thailand-specific — the deck should either caveat this ("global benchmarks, TH dynamics may differ") or you replace with a TH-sourced figure if the panel gave one.
4. Everything here is problem-framing only (Slides 1–2 of ≤10) — keep it to these two pages so there's room for the AI solution concept (25/100 pts, your biggest lever per the grading criteria).
