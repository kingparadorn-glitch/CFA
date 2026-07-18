# Manual Snapshot Template

Use this template for data that cannot be collected safely or legally by script, especially consensus, ratings, paid data terminals, broker reports, and SETTRADE IAA Consensus.

## Snapshot metadata

| Field | Value |
|---|---|
| Company |  |
| Ticker |  |
| Period |  |
| Snapshot date/time |  |
| Source/provider |  |
| Source URL or platform |  |
| Collector |  |
| License/access note |  |
| Intended purpose | `pre_decision` / `evaluation` |
| Source ID |  |

## Captured values

| Field | Value | Unit | As-of date | Notes |
|---|---:|---|---|---|
| Consensus target price |  |  |  |  |
| Analyst count |  |  |  |  |
| Consensus rating |  |  |  |  |
| Revenue estimate |  |  |  |  |
| EPS estimate |  |  |  |  |
| Other key estimate |  |  |  |  |

## Evidence

- Screenshot/file path:
- Notes:

## JSON fixture mapping

| Fixture field | Snapshot field |
|---|---|
| `valuation_reference.target` | Consensus target price |
| `valuation_reference.n_analysts` | Analyst count |
| `valuation_reference.rating` | Consensus rating |
| `ground_truth.gt_analyst_rating` | Consensus rating |
| `surprise_metrics[].estimate` | Revenue/EPS/company-driver estimate |
| `sources[]` | Snapshot metadata and license note |
| `evidence[]` | Field path, source ID, and intended purpose |
