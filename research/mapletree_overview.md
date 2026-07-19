# MapleTree — Platform Overview (1 page)

> Draft for reading + cutting into slides · Focused on the Earnings Update Cycle (Equity Research's biggest pain point)

---

## 1. What is MapleTree (one sentence)

**MapleTree = a platform that ingests earnings reports from listed companies and runs them
through the real workflow of an Equity Research analyst — from digesting the results,
updating the model, and running valuation, to drafting the report — with a licensed
analyst always signing off before anything publishes.**

In short: work that used to take an analyst **5.7 hours per company** every time a company
reports earnings, MapleTree compresses to **~45 minutes**, while the human stays the one
making the decision and taking responsibility.

---

## 2. Why it's needed (the problem it solves)

- One analyst covers **50–60 companies** and must publish **at least once per company per
  quarter**.
- During earnings season, companies report all at once → **~16 hrs/day**, work overload.
- **70–80%** of the time goes to **repetitive, mechanical work** (digesting statements,
  updating models), not analytical thinking.
- This is a structural pain point (the math of coverage load), not a laziness problem.

---

## 3. User Journey — walked through the analyst's eyes

> "What happens when a company I cover reports earnings" — 6 steps from earnings release to published report

| # | Step | Manual (before) | What MapleTree does | What the human still does |
|---|---|---|---|---|
| 1 | **Earnings release + listen to the call** | Sit through a 90-min call, take notes manually | Transcribe the call + capture guidance/management tone + compute the surprise automatically | Read the AI-generated summary |
| 2 | **Update the financial model** | Edit Excel cell by cell to make it tie | Feed actuals + new guidance into the model, check that it balances | Review flagged items |
| 3 | **Re-value + revise rating** | Calculate comps/DCF, compare to consensus | Calculate it (comps primary, DCF cross-check) vs. IAA consensus | **Decide when it deviates >15% from consensus** |
| 4 | **Draft the report** | Write the whole thing from scratch | Draft headline/key points/revised figures, every sentence cited | Read / polish the language |
| 5 | **Compliance sign-off** ★ | Analyst signs off themselves | Package the document + citations, ready for review | **Sign off (mandatory — human only)** |
| 6 | **Publish** | Send into the distribution system | Distribute to institutional clients | — |

**The core idea:** AI handles nearly all the mechanical steps (1, 2, 4, 6) · the human's
time is reserved for **judgment (step 3)** and **legal accountability (step 5)** — not
clerical work.

---

## 4. AI Architecture — platform structure

MapleTree splits cleanly into 2 parts — this is the technical selling point:

```
┌────────────────────────────────────────────────────────────┐
│  🟠 SECTOR PLUG — "the sector's brain"  (swappable)          │
│  Real Equity Research workflow + valuation formulas          │
│  (comps, DCF, WACC) + the points where a human must sign     │
│  → plugged into ER today · could plug into Wealth / IB /     │
│    Risk tomorrow                                              │
├────────────────────────────────────────────────────────────┤
│  🔵 ENGINE — "the central engine"  (built once, used by all) │
│                                                              │
│  Ingest documents → agent team works step by step →          │
│  human reviews/signs → publish                                │
│                                                              │
│  3 quality guarantees that make numbers trustworthy:          │
│   1. Numbers are computed by code, never guessed by an LLM    │
│      (comps/DCF = real code)                                  │
│   2. Every statement traces back to a source (click a number  │
│      → see where it came from)                                │
│   3. Whenever it's not confident → flags a human instead of   │
│      guessing                                                 │
└────────────────────────────────────────────────────────────┘
```

**Why it's designed this way (the pitch to judges):**
- **Separating engine from plug** → the finance team just needs to say "here's how this
  sector works," no need to touch the AI · and one engine can be sold across multiple
  sectors (genuinely scalable)
- **Separating numbers from the LLM** → the biggest weakness of AI in finance is "making up
  numbers" — we move the calculation into real code; the LLM only handles language
- **Human-in-the-loop at the critical points** → aligns with MiFID II / FINRA / SEC Thailand
  rules requiring a licensed analyst to sign off before publication = usable in the real
  world, not just a pretty demo

---

## 5. Framework summary (remember in 3 lines)

1. **Ingest** — Earnings reports + earnings calls of listed companies
2. **Process** — Agents follow the real ER workflow: digest → model → value → draft
   (numbers computed by code, everything cited)
3. **Output** — Report ready to publish **after the analyst signs off** (the human always
   decides and is always accountable)

> **Usable tagline:** *"AI drafts — humans approve"*

---

## 6. Impact numbers usable on the slide

| Metric | Value |
|---|---|
| Time per company update | 5.7 hrs → 45 min (**−87%**) |
| Analyst time recovered | 20–25 hrs/week |
| Data used in the demo | **100% public** (filings/IAA consensus/price) — no confidential data touched |

---

## ❓ Open questions — want to settle before going to slides

1. **The name "MapleTree"** — is there a meaning/origin you want it to convey? (would help
   shape a tagline that fits the name) — no official tagline yet.
2. **Will this overview be one slide, or split across several?** (User Journey + AI
   Architecture will feel cramped on a single slide — usually splitting into 2 slides reads
   easier.)
3. **Proxy company for the demo** — has MTC been locked in? (affects the example shown in
   the User Journey)
4. **Show only Earnings Update (P2), or also cover Coverage Initiation (P1)?** Currently
   written focused on P2 only, per what we discussed.
