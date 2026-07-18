# Company DB - MSFT + AMZN + PTT

This folder is the evidence-backed company database for the ER P2 Earnings Update MVP.

## Status - 2026-07-17

The public-data pack is complete for deterministic L0-L9 I/O across MSFT, AMZN, and PTT. Runtime-required fields now have verified `source_id` mappings and pass point-in-time checks. This does not mean the full LangGraph/LLM product is implemented, and it does not provide licensed historical consensus exports.

Run from the repository root:

```bash
make test
make smoke-l0-l9
```

## Canonical Artifacts

| Artifact | Purpose |
|---|---|
| `company_db_L0_L9_MSFT_AMZN_PTT.md` | Human-readable readiness summary and remaining gaps |
| `source_catalog.csv` | One row per source with URL, local evidence, publication date, tier, and verification status |
| `collection_status.csv` | Current layer-by-layer status; this supersedes earlier gap trackers |
| `source_manifest.json` | Machine-readable pointers and data policies |
| `processed/professional_er_event_inputs_2026-07-17.csv` | Company-specific actual-versus-estimate metrics |
| `processed/peer_multiples_pit_2026-07-17.csv` | Point-in-time peer multiples before each information cutoff |
| `processed/forecast_history_professional_2026-07-17.csv` | Dated PTT broker forecast history; US history remains in fixtures |
| `processed/field_provenance_2026-07-17.csv` | Runtime-required field to source mapping |
| `processed/row_source_provenance_2026-07-17.csv` | Actual/estimate, peer-row, forecast-row, reference, and model-vector source mapping |
| `processed/retrieval_corpus_2026-07-17.jsonl` | Short source-backed retrieval chunks; no full copyrighted transcript reproduction |
| `processed/professional_er_completeness_2026-07-17.csv` | Honest complete/partial/not-available matrix |
| `processed/evidence_audit_summary_2026-07-17.json` | Frozen result of source, PIT, provenance, and smoke verification |

Files named `L0_L9_research_fill_2026-07-17.csv`, `peer_multiples_2026-07-17.csv`, `forecast_history_2026-07-17.csv`, and `public_market_snapshot_unverified.csv` are retained as historical research artifacts. They are not inputs to the professional point-in-time run.

## Data Contract

1. Every fixture defines `event.report_date`, `event.information_cutoff`, and an evaluation window.
2. Every runtime-required field maps to a verified `source_id` in `evidence`.
3. Any evidence labeled `pre_decision` must be published on or before the information cutoff.
4. Company-specific surprise metrics carry separate actual and estimate source IDs plus an explicit basis.
5. PTT uses dated broker-house references where historical IAA aggregate data is unavailable; it is never mislabeled as consensus.
6. Unknown licensed data stays unavailable. No fabricated values or silent current-date substitutions.

## Residual External Dependencies

- Provider-native historical consensus: FactSet, Bloomberg, Visible Alpha, LSEG, or SETSMART/IAA licensed/manual export.
- Amazon full call Q&A transcript: licensed transcript or manual transcription from the official replay if tone/Q&A NLP is required.
- Real L0-L9 application runtime: parser, graph, retrieval index, memory, UI gate, and observability remain implementation work.
