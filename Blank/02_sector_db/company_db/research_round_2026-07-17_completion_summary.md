# Professional ER Evidence Completion - 2026-07-17

Scope: close all publicly obtainable data gaps required by the deterministic MSFT, AMZN, and PTT L0-L9 workflow; keep licensed or unavailable fields explicit.

## Research Log

1. Audited fixtures, pipeline, roadmap, schema, and existing processed files.
2. Identified current-date peer multiples, post-event consensus leakage, a false L3 gate, low-confidence PTT Finanzen estimates, and a mislabeled PTT event window.
3. Downloaded and extracted official Amazon releases/slides plus dated MSFT/PTT research evidence.
4. Replaced PTT estimate/history proxies with KS, InnovestX, UOB Kay Hian, TrueID/Thunhoon, and Globlex evidence.
5. Added source IDs, field provenance, PIT enforcement, company-specific surprise metrics, and compact retrieval chunks.
6. Updated fixtures and canonical documentation, then verified with unit tests and L0-L9 smoke commands.

## Claim-Source-Confidence Matrix

| Claim | Source IDs | Confidence | Limitation |
|---|---|---|---|
| MSFT Q3 actuals and Azure growth are supported by official/regulatory evidence | `MSFT_IR_Q3_RELEASE`, `MSFT_SEC_FACTS` | High | None for stated fields |
| MSFT pre-event estimates and target/count existed by the cutoff | `MSFT_CAPITAL_PRE_20260429` | Medium-High | Aggregates Bloomberg/Public.com data through a dated secondary page |
| US cloud peer multiples are point-in-time before both events | `MSFT_HENRY_20260422` | Medium-High | Academic report table rather than provider-native export |
| AMZN Q1 actuals, AWS revenue, and AWS margin are official | `AMZN_IR_Q1_RELEASE` | High | GAAP EPS includes an investment gain and needs quality-of-earnings context |
| AMZN pre-event revenue/EPS/AWS estimates and target/count are dated | `AMZN_CAPITAL_PRE_20260429`, `AMZN_SP_PRE_20260423` | Medium-High | S&P page is remote-only because archival download returned HTTP 403 |
| PTT reported/core profit estimates are dated before results | `PTT_KS_PRE_20260511` | High for net/core figures | KS page EPS is internally inconsistent and intentionally excluded |
| PTT PIT peers and SOTP target are dated before the event | `PTT_INVX_PRE_20260507` | High | Single broker house, not market-wide consensus |
| PTT three-quarter forecast history is broker-backed | `PTT_UOB_PRE_20251106`, `PTT_TRUEID_PRE_20260206`, `PTT_KS_PRE_20260511`, `PTT_GLOBLEX_POST_20260219`, `PTT_GLOBLEX_POST_20260514` | Medium-High | 4Q25 forecast is a dated news summary of broker work, not the original full report |
| All runtime-required fields have known verified sources and pass PIT | `field_provenance_2026-07-17.csv`; automated audit | High | Applies to deterministic fixture contract, not future live ingestion |

## Closed Gaps

- Point-in-time event metadata and pre/post separation for all three companies.
- Company-specific surprise metrics for Azure, AWS, and PTT core/reported profit.
- Event-date peer multiples for US cloud and Thai energy sets.
- PTT forecast history without Finanzen placeholders.
- Distinct L3 model test vector versus reference target.
- Field-level source mapping and automated look-ahead detection.
- Compact source-backed retrieval corpus for L5 I/O.

## Residual Gaps

| Gap | Status | How to obtain | Blocks public-data smoke? |
|---|---|---|---|
| Provider-native historical aggregate consensus | Not publicly complete | FactSet, Bloomberg, Visible Alpha, LSEG, or SETSMART/IAA licensed/manual export | No |
| AMZN full earnings-call Q&A transcript | Not locally archived | Licensed transcript provider or manual transcription of official replay | Only tone/Q&A NLP |
| Immediate post-event US target history | Current July snapshot is later | Licensed target-change history | No; relevant to strict short-horizon analyst eval |
| Real AI valuation output | Not a data artifact | Implement and evaluate L2/L3 runtime | Yes for full product |

## Canonical Outputs

Use `source_catalog.csv`, `collection_status.csv`, `source_manifest.json`, `processed/professional_er_event_inputs_2026-07-17.csv`, `processed/peer_multiples_pit_2026-07-17.csv`, `processed/forecast_history_professional_2026-07-17.csv`, `processed/field_provenance_2026-07-17.csv`, and `processed/professional_er_completeness_2026-07-17.csv`.

Earlier public snapshot and research-fill CSVs are retained only as historical work products and are not professional PIT runtime inputs.
