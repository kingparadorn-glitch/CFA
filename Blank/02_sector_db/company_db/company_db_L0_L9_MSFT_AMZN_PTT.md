# Company Data DB for L0-L9 - MSFT + AMZN + PTT

> Status as of 2026-07-17: the three-company public evidence pack is complete for deterministic L0-L9 data I/O and point-in-time validation. Licensed historical aggregate consensus and the real agent runtime are separate dependencies, not hidden data gaps.

## 1. Source Of Truth

| Artifact | Role | Status |
|---|---|---|
| `07_implementation/data/raw/MSFT_FY26Q3_golden.json` | US golden anchor | Professional public-data fixture |
| `07_implementation/data/raw/AMZN_FY26Q1_golden.json` | US cloud peer | Professional public-data fixture; full Q&A transcript optional |
| `07_implementation/data/raw/PTT_1Q2026_demo.json` | Thai local case | Professional broker-backed fixture; historical IAA aggregate unavailable |
| `source_catalog.csv` | Source inventory | Canonical |
| `processed/field_provenance_2026-07-17.csv` | Field-level citations | Canonical |
| `processed/row_source_provenance_2026-07-17.csv` | Nested row-level citations | Canonical |
| `processed/professional_er_completeness_2026-07-17.csv` | Gap matrix | Canonical |

## 2. Event Policy

| Company | Event | Report date | Information cutoff | Evaluation window | Source IDs |
|---|---|---:|---:|---:|---|
| MSFT | Earnings release | 2026-04-29 | 2026-04-29 | 2026-04-28 to 2026-04-30 | `MSFT_IR_Q3_RELEASE`, `MSFT_YAHOO_PRE`, `MSFT_YAHOO_POST` |
| AMZN | Earnings release | 2026-04-29 | 2026-04-29 | 2026-04-29 to 2026-04-30 | `AMZN_IR_Q1_RELEASE`, `AMZN_YAHOO_PRE`, `AMZN_YAHOO_POST` |
| PTT | Analyst meeting update | 2026-05-14 | 2026-05-20 | 2026-05-19 to 2026-05-21 | `PTT_OFFICIAL_FIN_20260514`, `PTT_IR_CALL_20260520`, `PTT_YAHOO_PRE`, `PTT_YAHOO_POST` |

PTT's return window is deliberately labeled `analyst_meeting_update`. Calling the May 19-21 prices an earnings-release reaction would be wrong.

## 3. Professional Surprise Inputs

| Company | Metric | Actual | Pre-event estimate | Result | Evidence |
|---|---|---:|---:|---:|---|
| MSFT | Revenue | USD82.886bn | USD81.46bn | +1.75% | `MSFT_IR_Q3_RELEASE`, `MSFT_CAPITAL_PRE_20260429` |
| MSFT | GAAP EPS | USD4.27 | USD4.04 | +5.69% | Same sources |
| MSFT | Azure growth, constant currency | 39.0% | 37.5% midpoint | +4.00% relative | Same sources |
| AMZN | Revenue | USD181.519bn | USD177.10bn | +2.50% | `AMZN_IR_Q1_RELEASE`, `AMZN_CAPITAL_PRE_20260429` |
| AMZN | GAAP EPS | USD2.78 | USD1.63 | +70.55% | Same sources; includes investment gain |
| AMZN | AWS revenue | USD37.587bn | USD36.80bn | +2.14% | Same sources |
| AMZN | AWS operating margin | 37.7% | 35.7% | +5.60% relative | Same sources |
| PTT | Reported net income | THB25.738bn | THB26.4bn | -2.51% | `PTT_GLOBLEX_POST_20260514`, `PTT_KS_PRE_20260511` |
| PTT | Core profit | THB28.589bn | THB31.2bn | -8.37% | Same sources |

The Kasikorn page also displays an EPS value that does not reconcile with its net-income forecast and PTT share count. That EPS is excluded and recorded as a source contradiction rather than forced into the dataset.

## 4. Valuation And Gate Inputs

| Company | Pre-event reference | Test-vector target | Gate implication | Evidence |
|---|---|---:|---|---|
| MSFT | Consensus USD565.28; 32 analysts; Buy | USD470 | Deviation above 15%; human gate | `MSFT_CAPITAL_PRE_20260429`, `MSFT_HENRY_20260422` |
| AMZN | Consensus USD287.24; 41 analysts; Buy | USD285 | Deviation below 15% | `AMZN_CAPITAL_PRE_20260429`, `AMZN_SP_PRE_20260423` |
| PTT | KS Hold / THB37.20; one house | INVX SOTP / THB44 | Deviation above 15%; human gate | `PTT_KS_PRE_20260511`, `PTT_INVX_PRE_20260507` |

`model_output` is explicitly a deterministic test vector. It is not presented as output from a completed AI valuation model.

## 5. L0-L9 Data Readiness

| Layer | Status | Evidence artifact | Remaining implementation work |
|---|---|---|---|
| L0 | Complete data | Official filings, IR text, extracted presentations | Production parsers and OCR fallbacks |
| L1 | Complete metadata | Fixture event/task fields | Real task classifier |
| L2 | Complete data and deterministic quant | `professional_er_event_inputs`, PIT peers | Production valuation model |
| L3 | Complete gate test inputs | Dated references and distinct model vectors | Editable human gate UI |
| L4 | Complete history | Fixture history + professional PTT history | Persistent memory store |
| L5 | Complete compact corpus | `retrieval_corpus_2026-07-17.jsonl` | Retrieval index and citation renderer |
| L6 | Complete field lineage | `field_provenance_2026-07-17.csv` | Trace backend and monitoring |
| L7 | Complete deterministic labels | Post-event target/rating + prices | Formal evaluation dashboard |
| L8 | Complete contract | `FixtureStore.evidence_audit` | CI integration beyond local Makefile |
| L9 | Complete smoke metadata | Deterministic route/cache key | Real router, model policy, and cache |

## 6. What Is Still Unavailable

| Gap | Why it is not silently filled | How to obtain it | Blocking? |
|---|---|---|---|
| Historical aggregate consensus exported directly from a provider | Public pages do not guarantee point-in-time constituent history | FactSet, Bloomberg, Visible Alpha, LSEG, or SETSMART/IAA manual/licensed export | No for public-data demo; yes if judges require provider-native history |
| AMZN first-party full call Q&A transcript | Official local pack contains release and slides; third-party full transcript has licensing/copyright constraints | Licensed transcript provider or manual transcription from official replay | Only for deep tone/Q&A NLP |
| Immediate post-result US target history | Current July snapshots are later than the event | Historical target-change feed from a licensed provider | No for I/O; medium for strict short-horizon analyst evaluation |
| Real AI target/rating | Data collection cannot substitute for a model run | Implement L2/L3 model and human-review path | Yes for full product, not for data readiness |

## 7. Verification

```bash
make test
make smoke-l0-l9
```

The expected contract is 11 passing tests, three fixtures with no missing evidence, no unknown source IDs, no point-in-time violations, and `all_schema_contracts_ok = true`.
