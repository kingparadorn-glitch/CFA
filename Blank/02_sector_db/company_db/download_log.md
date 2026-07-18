# Company DB Download Log

Downloaded on: 2026-07-17

## Summary

Public/free raw source files were downloaded into `02_sector_db/company_db/raw/` for the MSFT + AMZN + PTT test universe.

## Files downloaded

| File | Source | Status | Notes |
|---|---|---|---|
| `raw/sec/MSFT_companyfacts.json` | SEC companyfacts API | OK | JSON parse passed |
| `raw/sec/MSFT_submissions.json` | SEC submissions API | OK | JSON parse passed |
| `raw/sec/AMZN_companyfacts.json` | SEC companyfacts API | OK | JSON parse passed |
| `raw/sec/AMZN_submissions.json` | SEC submissions API | OK | JSON parse passed |
| `raw/ir/MSFT/msft_fy26q3_press_release_webcast.html` | Microsoft IR | OK | Contains FY26 Q3 press release, financial statement links, Azure/Microsoft Cloud references |
| `raw/ir/MSFT/msft_fy26q3_earnings_call.html` | Microsoft IR | OK | Earnings call/transcript page saved |
| `raw/ir/AMZN/about_amazon_q1_2026_results.html` | About Amazon | OK | Use as primary AMZN raw HTML if Amazon IR page is thin/redirected |
| `raw/ir/AMZN/amzn_q1_2026_results.html` | Amazon IR | Needs inspect | File is much smaller than expected; may be redirect/thin shell page |
| `raw/ir/PTT/ptt_presentations_webcasts.html` | PTT IR | OK | Contains Analyst Meeting 1Q/2026 and Opp Day references |
| `raw/ir/PTT/ptt_financial_statements_mda.html` | PTT IR | OK | Contains Financial Statement and MD&A references |
| `raw/ir/PTT/set_ptt_latest_balance.html` | SET | OK | Contains PTT latest financial statement page and Q1/2026 references |
| `raw/sec/filings/MSFT/msft-20260331-10q.htm` | SEC filing document | OK | Official 10-Q downloaded |
| `raw/sec/filings/AMZN/amzn-20260331-10q.htm` | SEC filing document | OK | Official 10-Q downloaded |
| `raw/market_prices/MSFT_yahoo_chart_2026-04-27_2026-05-02.json` | Yahoo chart API | OK | Used for MSFT pre/post earnings price |
| `raw/market_prices/AMZN_yahoo_chart_2026-04-27_2026-05-02.json` | Yahoo chart API | OK | Used for AMZN pre/post earnings price |
| `raw/market_prices/PTT.BK_yahoo_chart_2026-05-15_2026-05-25.json` | Yahoo chart API | OK | Used for PTT analyst-meeting event window |
| `raw/ir/PTT/files/ptt_1q2026_financials_all.zip` | PTT IR | OK | Contains AUDITOR_REPORT.DOCX, FINANCIAL_STATEMENTS.XLSX, NOTES.DOCX |
| `raw/ir/PTT/files/ptt_1q2026_mdna.pdf` | PTT IR | OK | PDF downloaded and text extracted |
| `raw/ir/PTT/files/ptt_analyst_meeting_1q2026.pdf` | PTT IR | OK | PDF downloaded and text extracted |
| `raw/ir/PTT/files/ptt_oppday_1q2026.pdf` | PTT IR | OK | PDF downloaded and text extracted |
| `raw/ir/PTT/files/ptt_performance_conference_call_1q2026.pdf` | PTT IR | OK | PDF downloaded and text extracted |
| `raw/research/MSFT/msft_henry_fund_2026-04-22.pdf` | Henry Fund | OK | Dated report; PIT US peer table extracted |
| `raw/research/MSFT/msft_capital_pre_earnings_2026-04-29.html` | Capital.com | OK | Dated pre-event estimates and target/count extracted |
| `raw/research/MSFT/msft_stockanalysis_statistics_2026-07-17.html` | StockAnalysis | OK | Post-event target/rating/count frozen as HTML and text |
| `raw/research/AMZN/amzn_q1_2026_earnings_release.pdf` | Amazon IR | OK | Official 14-page release extracted |
| `raw/research/AMZN/amzn_q1_2026_webcast_slides.pdf` | Amazon IR | OK | Official 15-page slides extracted |
| `raw/research/AMZN/amzn_capital_pre_earnings_2026-04-29.html` | Capital.com | OK | Dated pre-event estimates and target/count extracted |
| `raw/research/AMZN/amzn_stockanalysis_statistics_2026-07-17.html` | StockAnalysis | OK | Post-event target/rating/count frozen as HTML and text |
| `raw/research/PTT/ptt_innovestx_preview_2026-05-07.pdf` | InnovestX | OK | PIT SOTP target and Thai peer multiples extracted |
| `raw/research/PTT/ptt_kasikorn_preview_2026-05-11.html` | Kasikorn Securities | OK | Net/core forecasts and house target captured |
| `raw/research/PTT/ptt_globlex_results_2026-05-14.pdf` | Globlex | OK | Actual/core bridge and post-result rating/target extracted |
| `raw/research/PTT/ptt_uobkh_3q25_preview_2025-11-06.pdf` | UOB Kay Hian | OK | 3Q25 forecast history extracted |
| `raw/research/PTT/ptt_4q25_preview_trueid_2026-02-06.html` | TrueID/Thunhoon | OK | Dated Krungsri 4Q25 forecast summary captured |
| `raw/research/PTT/ptt_globlex_results_2026-02-19.pdf` | Globlex | OK | 4Q25 actual history extracted |

## Verification performed

- SEC JSON files were checked with `jq empty`.
- Raw HTML files were checked with keyword search for company-specific evidence:
  - MSFT: `Azure`, `Microsoft Cloud`, `Financial Statements`
  - AMZN: `AWS`, `North America`, result-page metadata
  - PTT: `Analyst Meeting`, `Financial Statement`, `PTT`, `Q1/2026`

## Residual Evidence Not Publicly Complete

| Evidence item | Current status | How to close before final presentation |
|---|---|---|
| Provider-native historical aggregate consensus | Public dated snapshots do not expose full constituent/change history | FactSet, Bloomberg, Visible Alpha, LSEG, or SETSMART/IAA licensed/manual export |
| Full AMZN earnings-call Q&A transcript | Official release and slides are local; full transcript licensing is separate | Licensed provider or manual transcription from official replay |
| Immediate post-result US target-change history | July snapshots are later than the release window | Licensed historical analyst target feed |
| S&P Global AMZN preview local archive | Page verified online; direct archival request returned HTTP 403 | Keep remote URL or save manually under permitted access |
