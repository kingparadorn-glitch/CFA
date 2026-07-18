# Public Source Extraction Status

Updated: 2026-07-17

## Completed

| Area | Output | Verification |
|---|---|---|
| MSFT SEC/IR actuals and transcript | `raw/sec/MSFT_*`, `raw/ir/MSFT/*` | Primary sources |
| MSFT dated consensus and PIT peers | `MSFT_capital_pre_earnings_2026-04-29.txt`, `MSFT_henry_fund_2026-04-22.txt` | Source IDs `MSFT_CAPITAL_PRE_20260429`, `MSFT_HENRY_20260422` |
| AMZN official release and slides | `AMZN_q1_2026_earnings_release.txt`, `AMZN_q1_2026_webcast_slides.txt` | Primary sources |
| AMZN dated estimates | `AMZN_capital_pre_earnings_2026-04-29.txt` | Source ID `AMZN_CAPITAL_PRE_20260429` |
| PTT official actuals and performance call | `PTT_1Q2026_*` | Primary sources |
| PTT dated previews/results/history | `PTT_innovestx_*`, `PTT_globlex_*`, `PTT_uobkh_*`, local KS/TrueID HTML | Dated broker/public evidence |
| Point-in-time peer tables | `peer_multiples_pit_2026-07-17.csv` | Dates precede information cutoffs |
| Field provenance and retrieval chunks | `field_provenance_2026-07-17.csv`, `retrieval_corpus_2026-07-17.jsonl` | Automated source/PIT audit |

## Public Pack Limitations

| Data | Status | Required source if needed |
|---|---|---|
| Historical aggregate consensus constituents/changes | Unavailable in a complete public export | FactSet, Bloomberg, Visible Alpha, LSEG, or SETSMART/IAA licensed/manual export |
| AMZN full call Q&A text | Official release/slides available; full transcript not locally archived | Licensed transcript or manual transcription from official replay |
| Immediate post-result MSFT/AMZN target history | July snapshot is available but later than the event | Licensed analyst target-change history |

## Quality Notes

- AMZN GAAP EPS includes a material investment gain. Do not mix it with adjusted EPS history; use explicit `basis` labels.
- The Kasikorn PTT page's EPS does not reconcile with its own net-income estimate and PTT share count. The fixture excludes that EPS.
- PTT May 19-21 prices measure the analyst-meeting update, not the May 14 earnings release.
- S&P Global's AMZN preview was verified online but archival download returned HTTP 403; its URL remains in the source catalog as remote-only.
