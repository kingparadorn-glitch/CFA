# Professional Build Methodology — ER P2 Internal Analyst Copilot

Status: **Step 5 approved design and execution methodology**  
Decision date: 2026-07-18  
Applies to: P2 Earnings Update for MSFT + AMZN + PTT  
Target path: **local/private MVP Internal Analyst Copilot → Enterprise Research Platform**  
Does not mean: production-ready, public deployment, autonomous publishing, or legal approval

> This document defines *how the team builds, verifies, releases, and operates the product*. Runtime implementation remains under `07_implementation/`. Every external framework or factual claim is cited; project choices are labeled **Project decision**. Thai legal applicability still requires qualified legal/compliance review before real use.

---

## 0. Research Log and Evidence Quality

### 0.1 Structural grounding performed

The methodology was rebuilt from named professional frameworks rather than generic AI-product advice:

- AI/product lifecycle: AWS Generative AI Lens, Google MLOps, ISO/IEC 42001 Plan-Do-Check-Act.
- Agent design and runtime: Anthropic workflow-first patterns and LangGraph persistence/interrupts.
- AI governance and model risk: NIST AI RMF + GenAI Profile, ISO/IEC 42001, US interagency SR 26-2.
- Secure engineering: NIST SSDF, OWASP LLM/Agentic risks, CycloneDX ML-BOM.
- Evaluation: LangSmith offline/online evaluation concepts plus human calibration.
- Reliability and release: Google SRE production-readiness and canary guidance.
- Equity-research controls: CFA Standard V(A), CFA Research Objectivity Standards, FINRA Rule 2241, SEC Regulation AC, EU 2016/958, and Thai SEC IA practice guidance.

### 0.2 Claim → source → confidence

| Claim used in this methodology | Primary source checked | Confidence |
|---|---|---|
| AI risk management should run continuously through Govern, Map, Measure, Manage | [NIST AI RMF Core](https://airc.nist.gov/airmf-resources/airmf/5-sec-core/) | High |
| AI management should be continually improved through a management-system cycle | [ISO/IEC 42001 overview](https://www.iso.org/standard/42001) | High |
| Reliable agentic systems should begin with the simplest workflow that meets the need | [Anthropic: Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents) | High |
| Production ML/AI needs validation, metadata, reproducibility, deployment, and monitoring | [Google MLOps](https://docs.cloud.google.com/architecture/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning) | High |
| Human-interrupt workflows require persistent state/checkpoints to resume safely | [LangGraph interrupts](https://docs.langchain.com/oss/python/langgraph/interrupts), [persistence](https://docs.langchain.com/oss/python/langgraph/persistence) | High |
| Agent permissions and autonomy must be limited to reduce excessive-agency risk | [OWASP LLM06:2025](https://owasp.org/www-project-top-10-for-large-language-model-applications/2_0_vulns/LLM06_ExcessiveAgency.html) | High |
| Secure-development controls must be integrated into the SDLC, not added only at release | [NIST SP 800-218 SSDF](https://csrc.nist.gov/pubs/sp/800/218/final) | High |
| Offline evaluation and online monitoring serve different purposes; human feedback is important for subjective quality | [LangSmith evaluation concepts](https://docs.langchain.com/langsmith/evaluation-concepts) | High |
| Research recommendations require a reasonable and adequate basis | [CFA Standard V(A)](https://www.cfainstitute.org/standards/professionals/code-ethics-standards/standards-of-practice-v-a) | High |
| Equity research should disclose conflicts and provide valuation/risk basis | [FINRA Rule 2241](https://www.finra.org/rules-guidance/rulebooks/finra-rules/2241) | High |
| US model-risk guidance is now SR 26-2; it superseded SR 11-7 on 2026-04-17 | [Federal Reserve SR 26-2](https://www.federalreserve.gov/supervisionreg/srletters/SR2602.htm) | High |
| Thai IA guidance requires sources to be identified and market-moving rumors not to be spread without verification | [Thai SEC IA practice guidance, unofficial English translation](https://publish.sec.or.th/nrs/7901se.pdf) | Medium — translation; Thai counsel must confirm current applicability |

### 0.3 Remaining uncertainty

- `[legal-review-required]` Exact Thai SEC/IAA obligations depend on the deploying entity, user license, distribution model, and current notifications. This methodology supplies controls, not legal advice.
- `[provider-contract-required]` Retention, embedding, redistribution, and model-processing rights must be checked against each licensed-data contract.
- Model pricing, availability, and quality are intentionally not hard-coded. They must be measured during provider selection.

---

## 1. Product Charter and Boundaries

Professional teams start with an explicit decision boundary because risk, testing, and accountability differ sharply between decision support and autonomous action. NIST requires the context, intended purpose, users, and impacts to be mapped; AWS begins the GenAI lifecycle with scoping the business problem. Sources: [NIST AI RMF Core](https://airc.nist.gov/airmf-resources/airmf/5-sec-core/), [AWS Generative AI lifecycle](https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/generative-ai-lifecycle.html).

### 1.1 Product statement

**Project decision:** Build a P2 Earnings Update Internal Analyst Copilot that converts verified company evidence into a cited draft, deterministic valuation outputs, and reviewable trace. A human analyst owns rating/target judgment; compliance owns final approval. The system never publishes externally on its own.

### 1.2 Users and jobs

| User/actor | Job to be done | System may do | System must not do |
|---|---|---|---|
| Analyst | Understand earnings, update model/valuation, draft note | Extract verified evidence, calculate via tools, draft cited content | Invent facts, silently mix bases, approve compliance for production |
| Finance reviewer | Check valuation assumptions and reasonable basis | Inspect evidence, edit assumptions, resume workflow | Bypass failed PIT/citation controls |
| Compliance reviewer | Review disclosures, claims, conflicts, and publishability | Approve/reject/request evidence | Delegate final approval to an LLM |
| Product/engineering | Operate, evaluate, and improve the system | Change versioned config through eval gates | Edit frozen demo/production config without a decision record |
| Judge/demo viewer | Observe value, control, and feasibility | View before/after, gate, citations, and trace | Be told that demo role selection is authenticated approval |

### 1.3 Scope classes

- **MVP required:** P2 only; MSFT/AMZN/PTT; FastAPI + Next.js; PostgreSQL; durable worker; six-node LangGraph workflow; typed contracts; hybrid retrieval; two human gates; trace/eval/replay.
- **Enterprise gate:** authentication, RBAC/SSO, trusted reviewer identity, managed secrets, licensed-provider legal review, managed queue/database, staging/production, production SLO/alerts, backup/PITR, DR testing.
- **Deferred until evidence supports it:** P1/P3-P7 workflows, autonomous planning, multi-agent delegation, fine-tuning, reranker, semantic cache, active learning, public distribution.

### 1.4 Non-negotiable claims policy

The team may claim “private MVP,” “walking skeleton,” “verified replay,” and “production path.” It may not claim “production-ready,” “regulator-approved,” “historical aggregate consensus” without provider-native evidence, or “authenticated approval” while the MVP has no authentication. CFA requires diligence and a supportable basis; FINRA requires reliable factual information and a reasonable basis for ratings/targets. Sources: [CFA Standard V(A)](https://www.cfainstitute.org/standards/professionals/code-ethics-standards/standards-of-practice-v-a), [FINRA Rule 2241(c)](https://www.finra.org/rules-guidance/rulebooks/finra-rules/2241).

---

## 2. Operating Principles

### 2.1 Workflow-first, limited agency

**Project decision:** Use a fixed six-node graph (`digest → update_model → revalue_rating → valuation_gate → draft_note → compliance_gate → export`) with explicit branches. Open-ended agent planning is outside MVP. Anthropic recommends starting with simple composable workflows and adding autonomy only when needed; OWASP identifies excessive functionality, permissions, and autonomy as causes of excessive agency. Sources: [Anthropic](https://www.anthropic.com/engineering/building-effective-agents), [OWASP LLM06](https://owasp.org/www-project-top-10-for-large-language-model-applications/2_0_vulns/LLM06_ExcessiveAgency.html).

### 2.2 Deterministic finance, probabilistic language

Financial arithmetic, thresholds, basis conversion, and valuation calculations live in deterministic Python tools. LLMs summarize, classify, retrieve, and draft around validated outputs. Every numeric claim must preserve unit, basis, actual/estimate source, and calculation lineage. This implements CFA’s reasonable-basis requirement and FINRA’s requirement for a clear valuation basis and fair presentation of risks. Sources: [CFA Standard V(A)](https://www.cfainstitute.org/standards/professionals/code-ethics-standards/standards-of-practice-v-a), [FINRA Rule 2241(c)](https://www.finra.org/rules-guidance/rulebooks/finra-rules/2241).

### 2.3 Fail closed

An invalid schema, PIT violation, prohibited license use, missing citation, failed valuation gate, rejected compliance gate, or uncertain output blocks the next risk-bearing action. No fallback may silently replace missing evidence with model memory. NIST frames risk management as continuous, while OWASP recommends minimizing permissions and validating outputs before downstream actions. Sources: [NIST AI RMF](https://airc.nist.gov/airmf-resources/airmf/5-sec-core/), [OWASP LLM Top 10](https://owasp.org/www-project-top-10-for-large-language-model-applications/).

### 2.4 Reproducibility before sophistication

A release is a versioned bundle of code identifier, schema/migration version, fixture/evidence checksums, prompt/model/retrieval config, evaluator version, and output/trace pointers. Google MLOps calls for metadata and lineage covering code, data, model, parameters, metrics, and artifacts. Source: [Google MLOps](https://docs.cloud.google.com/architecture/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning).

### 2.5 Quality and auditability first

Correct controls are hard gates; latency and cost are measured budgets. This prioritization follows the product’s regulated-research context and the agreed Internal Analyst Copilot boundary. The specific thresholds in §12 are team-defined requirements, not claims of universal industry standards.

---

## 3. Target Architecture and Stack

Professional architecture separates responsibilities and creates testable contracts. AWS Well-Architected guidance emphasizes ownership, protection, resilience, traceability, and reusable modular components. Sources: [AWS ML design principles](https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/design-principles.html), [AWS GenAI lifecycle](https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/generative-ai-lifecycle.html).

### 3.1 Component map

| Component | MVP decision | Responsibility | Hard boundary/test |
|---|---|---|---|
| Analyst UI | Next.js/React | Run setup, evidence review, valuation gate, note/compliance review, trace/eval | No business rules or finance arithmetic in UI |
| Application API | FastAPI | Typed REST commands/queries, SSE status stream, polling fallback | OpenAPI/schema contract tests; idempotency on create/resume/export |
| Worker | Separate durable process | Claim jobs, execute graph, retry/recover | HTTP lifetime cannot own workflow state |
| Orchestrator | LangGraph StateGraph | Six nodes, checkpoints, interrupts, resume | Persistent checkpoint/thread ID required for gates |
| Contracts | Pydantic v2 strict models | Validate node/tool/API boundaries | Invalid/extra/coerced critical data fails |
| Transaction store | PostgreSQL | Runs, jobs, checkpoints, gates, claims, citations, config/eval/audit | Migrations, constraints, transactions, restore test |
| Retrieval | PostgreSQL full-text + pgvector | Hybrid retrieval with metadata/PIT/license filters | Filter before ranking; Recall@5 evaluation |
| Evidence store | Filesystem in MVP; object-storage adapter later | Immutable raw/normalized artifacts and manifests | Checksum, MIME/type validation, access policy |
| Model gateway | Provider-neutral tier router | Approved models, fallbacks, budget, structured-output policy | Nodes use tiers, not provider names |
| Observability | OTel-compatible schema in PostgreSQL/JSON | Node/tool/model/gate traces, cost, latency, lineage | Trace ID links every artifact |
| Packaging | Docker/Compose, cloud-neutral | Reproducible local `dev/test/demo` environments | Pinned images/config; no public MVP endpoint |

LangGraph documents persistent checkpoints for interrupts and resume; pgvector supports vector search inside PostgreSQL and can be combined with PostgreSQL full-text search; OpenTelemetry supplies vendor-neutral telemetry conventions. Sources: [LangGraph persistence](https://docs.langchain.com/oss/python/langgraph/persistence), [pgvector](https://github.com/pgvector/pgvector), [PostgreSQL full-text search](https://www.postgresql.org/docs/current/textsearch.html), [OpenTelemetry](https://opentelemetry.io/docs/).

### 3.2 Explicit exclusions

- No Chroma: PostgreSQL + pgvector is the single retrieval path.
- No Celery/Redis initially: use a PostgreSQL-backed durable job contract; add a queue adapter when load evidence requires it.
- No Langfuse dependency in MVP: preserve an optional exporter interface.
- No authentication in MVP: role selection is demo-only and the app must remain local/private.
- No public internet deployment, autonomous publish, full enterprise admin UI, or password lifecycle.

### 3.3 Trust boundaries

1. Untrusted upload/web content → quarantine.
2. Quarantine → deterministic parser/schema/PIT/license validation.
3. Verified evidence → retrieval corpus.
4. Retrieval/model output → strict schema + claim/citation checker.
5. Valuation output → human valuation gate when triggered.
6. Draft note → compliance gate.
7. Approved note → private export only.

OWASP’s current LLM and agentic guidance treats prompt injection, tool misuse, excessive agency, data disclosure, and supply-chain risk as distinct controls; NIST SSDF requires security practices throughout development. Sources: [OWASP GenAI Security Project](https://genai.owasp.org/), [NIST SSDF](https://csrc.nist.gov/pubs/sp/800/218/final).

---

## 4. End-to-End Build Lifecycle

Every phase uses the same professional record:

`inputs → activities → artifacts → tests/evals → exit gate → owner → evidence`

The lifecycle combines ISO/IEC 42001 Plan-Do-Check-Act, NIST Govern/Map/Measure/Manage, and production AI lifecycle guidance. Sources: [ISO/IEC 42001](https://www.iso.org/standard/42001), [NIST AI RMF](https://airc.nist.gov/airmf-resources/airmf/5-sec-core/), [Google MLOps](https://docs.cloud.google.com/architecture/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning).

### Phase A — Product framing and claim boundary

**Why professionals include it:** A technically successful system can still fail if the user, decision, benefit, and prohibited claims are unclear.

- Inputs: competition criteria, Step 1-4 decisions, P2 analyst workflow, available company evidence.
- Activities: define actor/JTBD, current baseline, desired outcome, non-goals, decision rights, value metrics, release claims.
- Artifacts: product charter, user/task map, scope/non-scope table, success-metric dictionary, claims register.
- Tests: each proposed feature maps to a user task and score/value hypothesis; no feature lacks an owner or acceptance rule.
- Exit gate: Product + Finance approve the exact MVP sentence and prohibited claims.
- Owner: Product owner; Finance accountable.
- Evidence: signed decision log and criteria traceability matrix.

Sources: [AWS GenAI scoping](https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/generative-ai-lifecycle.html), [NIST AI RMF Map](https://airc.nist.gov/airmf-resources/airmf/5-sec-core/).

### Phase B — Risk, regulatory, and control mapping

**Why professionals include it:** Controls must be designed before implementation choices make them expensive to add.

- Inputs: product charter, data classes, tool permissions, distribution boundary, jurisdictions.
- Activities: threat model, AI risk assessment, model-use classification, data/license review, research-conflict/disclosure map, owner assignment.
- Artifacts: risk register; control matrix with preventive/detective/corrective controls; data-classification policy; legal-review questions; human-accountability RACI.
- Tests: each Critical/High risk has trigger, owner, control, detector, response, and residual-risk decision.
- Exit gate: no Critical risk without an accepted treatment; legal applicability gaps explicitly labeled.
- Owner: Compliance/risk accountable; Security and Finance consulted.
- Evidence: control IDs linked to requirements/tests/runbook.

Sources: [NIST AI RMF + GenAI Profile](https://www.nist.gov/itl/ai-risk-management-framework), [ISO/IEC 42001](https://www.iso.org/standard/42001), [FINRA GenAI Notice 24-09](https://www.finra.org/rules-guidance/notices/24-09).

### Phase C — Contract foundation

**Why professionals include it:** Stable contracts allow UI, workflow, data, tools, and evaluation to evolve independently.

- Inputs: approved architecture, `runtime_schema_contract.md`, `json_trace_schema.md`, `eval_case_plan.md`.
- Activities: define domain/API/event/error models; PostgreSQL schema and migrations; IDs/idempotency; config/version model; job/checkpoint lifecycle.
- Artifacts: Pydantic models, OpenAPI schema, DB ERD/migrations, error catalog, state-transition table, architecture decision records.
- Tests: schema round-trip, invalid-input rejection, migration up/down on disposable DB, idempotency, state-machine invariants.
- Exit gate: one typed object can travel UI → API → DB → worker → trace and back without loose production `dict` handoff.
- Owner: Tech lead accountable; Product/Finance approve domain meaning.
- Evidence: contract-test report and migration log.

Sources: [Pydantic strict mode](https://docs.pydantic.dev/latest/concepts/strict_mode/), [OpenAPI Specification](https://spec.openapis.org/oas/latest.html), [LangGraph persistence](https://docs.langchain.com/oss/python/langgraph/persistence).

### Phase D — Evidence ingestion and retrieval corpus

**Why professionals include it:** Research output quality is bounded by evidence quality, time consistency, and usage rights.

- Inputs: curated uploads, official-source adapters, source contracts, event information cutoff.
- Activities: quarantine; checksum/MIME/type/malware checks; deterministic parse; normalize; actual-vs-estimate basis tagging; PIT/license/provenance validation; chunk/index only verified evidence.
- Artifacts: source registry, evidence manifest, rejected-source log, normalized tables, corpus records, parser fixtures.
- Tests: malicious/unsupported file, duplicate checksum, future source, unknown source ID, prohibited permitted-use, parser drift, claim-to-passage resolution.
- Exit gate: all demo facts have verified source IDs; no indexed record fails PIT/license/schema policy.
- Owner: Data owner accountable; Finance verifies meaning; Security reviews upload boundary.
- Evidence: data-quality report and manifest checksum.

Sources: [Google MLOps data/model validation and metadata](https://docs.cloud.google.com/architecture/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning), [CFA Standard V(A)](https://www.cfainstitute.org/standards/professionals/code-ethics-standards/standards-of-practice-v-a), [Thai SEC IA practice guidance](https://publish.sec.or.th/nrs/7901se.pdf).

### Phase E — One-node walking skeleton

**Why professionals include it:** It exposes integration and operational failures before six nodes multiply debugging paths.

- Inputs: one verified event, contracts, database, UI shell, model gateway stub.
- Activities: Next.js creates run; FastAPI returns `run_id`; worker executes digest; state/checkpoint/trace persist; UI receives SSE/poll status and renders cited output.
- Artifacts: runnable Compose stack, one end-to-end trace, retry/resume proof, API examples.
- Tests: process restart, duplicate command, model timeout/fallback, DB reconnect, malformed structured output, SSE reconnect/poll fallback.
- Exit gate: the same run is recoverable and replayable after worker/API restart without duplicate artifact.
- Owner: Tech lead.
- Evidence: test result, trace JSON, screenshot/replay artifact.

Sources: [Anthropic start simple](https://www.anthropic.com/engineering/building-effective-agents), [LangGraph persistence](https://docs.langchain.com/oss/python/langgraph/persistence), [Google SRE data-processing readiness](https://sre.google/workbook/data-processing/).

### Phase F — P2 vertical slices

Build in this dependency order:

1. Digest actual-versus-estimate drivers.
2. Deterministic model-update inputs/outputs.
3. Revalue/rating with explicit valuation references.
4. Valuation interrupt, edit, and resume to draft.
5. Cited research-note draft.
6. Compliance pre-check and human decision.
7. Private export plus immutable artifact pointer.

For each slice:

- Add positive, negative, timeout, retry, and trace expectations first.
- Implement deterministic tool and schema before LLM prompt.
- Add capability eval only after hard correctness tests exist.
- Promote only when previous slices remain green.

Exit gate: the six-node workflow passes all branch tests; neither rejection nor interruption can reach export. Sources: [LangGraph interrupts](https://docs.langchain.com/oss/python/langgraph/interrupts), [OWASP Excessive Agency](https://owasp.org/www-project-top-10-for-large-language-model-applications/2_0_vulns/LLM06_ExcessiveAgency.html).

### Phase G — Evaluation hardening

**Why professionals include it:** Tests assert deterministic correctness; evaluation measures variable quality. Both are required.

- Inputs: 20 seed cases, versioned fixtures, human rubric, baseline config.
- Activities: implement regression/capability/gate/replay suites; retrieval evaluation; human labels; calibrate any LLM judge; compare experiments.
- Artifacts: runnable eval dataset, evaluator registry, baseline report, failure taxonomy, release scorecard.
- Tests: evaluator determinism where applicable; human agreement sampling; critical branch coverage; no data leakage across time cutoff.
- Exit gate: §12 release targets pass; critical controls have both allow and block cases.
- Owner: Finance owns ground truth; Engineering owns harness; second reviewer adjudicates rating/target/compliance cases.
- Evidence: per-case trace, scores, config versions, reviewer decisions.

Sources: [LangSmith evaluation concepts](https://docs.langchain.com/langsmith/evaluation-concepts), [aligning LLM judges with human feedback](https://docs.langchain.com/langsmith/improve-judge-evaluator-feedback).

### Phase H — Security and compliance readiness

- Inputs: control matrix, full workflow, dependency/model/provider inventory.
- Activities: prompt-injection/tool-misuse tests; secret/data-leak review; file-upload abuse; dependency/license scan; gate-bypass review; disclosure/certification checklist.
- Artifacts: threat model, security test report, ML/SBOM inventory, compliance checklist, unresolved legal questions.
- Exit gate: no open Critical issue; all accepted High residual risks have owner and expiry; public exposure remains disabled.
- Owner: Security/Compliance accountable.

Sources: [NIST SSDF](https://csrc.nist.gov/pubs/sp/800/218/final), [OWASP GenAI Security](https://genai.owasp.org/), [CycloneDX ML-BOM](https://cyclonedx.org/capabilities/mlbom/), [CFA Research Objectivity Standards](https://www.cfainstitute.org/sites/default/files/-/media/documents/code/other-codes-standards/read-research-objectivity-standards.pdf).

### Phase I — Private release readiness

- Inputs: frozen candidate, verified data pack, passing scorecard, runbooks.
- Activities: clean-environment deploy; migration/restore; full MSFT/AMZN/PTT replays; gate drill; kill-switch/rollback; backup video/artifacts; claims review.
- Artifacts: release manifest, backup, restore proof, rollback target, demo/replay pack, known-limitations sheet.
- Exit gate: Product, Finance, Engineering, and Compliance sign their checklist; release is local/private only.
- Owner: Release owner coordinates; domain owners sign their evidence.

Google SRE defines canarying as a partial, time-limited release evaluated before broader rollout and emphasizes rollback; the MVP equivalent is a frozen private candidate plus verified replays, not a claim of production availability. Sources: [Google SRE canarying](https://sre.google/workbook/canarying-releases/), [configuration and rollback](https://sre.google/workbook/configuration-design/).

### Phase J — Operate, learn, and improve

- Inputs: traces, user review, failures, cost/latency metrics, incidents.
- Activities: triage by failure taxonomy; root-cause analysis; convert real failure to regression case; run controlled experiment; promote/rollback config.
- Artifacts: incident/problem records, new eval cases, experiment comparison, updated risk register/model inventory.
- Exit gate per change: baseline hard gates still pass and change decision is recorded.
- Owner: Product prioritizes; Finance validates quality; Engineering owns corrective action.

Sources: [ISO/IEC 42001 continual improvement](https://www.iso.org/standard/42001), [LangSmith offline/online loop](https://docs.langchain.com/langsmith/evaluation-concepts), [SR 26-2 model lifecycle/governance](https://www.federalreserve.gov/frrs/guidance/supervisory-guidance-on-model-risk-management.htm).

### Phase K — Enterprise hardening

The MVP cannot enter enterprise use until all of these are implemented and tested:

- Authentication + RBAC/SSO and trusted reviewer identity.
- Segregation of analyst, compliance, admin, and service roles.
- Managed secrets, encryption/key policy, environment isolation, vulnerability process.
- Licensed-provider contract review, entitlements, retention, redistribution controls.
- Managed queue/database, staging/production, backup/PITR, RPO/RTO and DR drill.
- Production SLOs, alerting/on-call, capacity and cost controls.
- Jurisdiction-specific legal approval, disclosures, conflicts, records, and change governance.
- Independent validation proportional to model risk and use.

SR 26-2 emphasizes risk-based model development, validation/monitoring, governance, clear responsibilities, and third-party products. FINRA states that existing securities obligations remain technology-neutral when firms use GenAI. Sources: [Federal Reserve SR 26-2](https://www.federalreserve.gov/supervisionreg/srletters/SR2602.htm), [FINRA Notice 24-09](https://www.finra.org/rules-guidance/notices/24-09).

---

## 5. Requirements and Control Traceability

Every requirement receives a stable ID and must link forward to implementation/test evidence and backward to user/risk/scoring rationale.

| ID family | Meaning | Required links |
|---|---|---|
| `PRD-*` | Product/user requirement | user task → acceptance metric → UI/API artifact |
| `FIN-*` | Finance methodology | formula/basis → deterministic tool → finance test → reviewer |
| `DATA-*` | Data/provenance/license/PIT | source policy → manifest/schema → audit test |
| `AI-*` | Model/prompt/retrieval behavior | config version → eval cases → baseline comparison |
| `SEC-*` | Security control | threat → control → abuse test → response runbook |
| `COMP-*` | Research/compliance control | rule/principle → gate/checklist → reviewer evidence |
| `OPS-*` | Reliability/operations | SLO/budget → telemetry → alert/runbook → drill |
| `DEMO-*` | Hackathon proof | scoring criterion → scene → artifact → backup |

No requirement is complete when only prose exists. It is complete when its artifact and verification evidence are linked. NIST SSDF calls for tracking security requirements, risks, and design decisions; Google MLOps calls for metadata and lineage across pipeline executions. Sources: [NIST SSDF project](https://csrc.nist.gov/projects/ssdf), [Google MLOps](https://docs.cloud.google.com/architecture/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning).

---

## 6. Team Operating Model

Roles are accountabilities, not required headcount; one person may wear several hats, but the author should not be the sole approver for critical research judgments.

| Role | Accountable for | Cannot self-certify alone |
|---|---|---|
| Product owner | Scope, outcome, priority, claims | Compliance/legal applicability |
| Finance owner | Metrics, basis, valuation method, ground truth | Critical rating/target cases requiring second review |
| Tech lead | Architecture, contracts, delivery quality | Finance reasonableness |
| Data owner | Source registry, PIT/license/provenance, parser quality | Provider legal rights without contract review |
| Evaluation owner | Dataset/evaluator versions, scorecards | Subjective finance labels without finance owner |
| Security owner | Threat model, secrets, supply chain, incident controls | Legal conclusions |
| Compliance reviewer | Disclosure/gate/release decision | Authenticated production approval while MVP has no auth |
| Release owner | Candidate manifest, restore/rollback/replay | Domain sign-offs on behalf of owners |

CFA Research Objectivity Standards call for review/approval by a supervisory analyst or review committee and written policies supporting objectivity; SR 26-2 stresses clear roles and accountability across the model lifecycle. Sources: [CFA Research Objectivity Standards](https://www.cfainstitute.org/sites/default/files/-/media/documents/code/other-codes-standards/read-research-objectivity-standards.pdf), [SR 26-2 guidance](https://www.federalreserve.gov/frrs/guidance/supervisory-guidance-on-model-risk-management.htm).

---

## 7. Data and Evidence Methodology

### 7.1 Source hierarchy

1. Regulatory filings and official company disclosures.
2. Licensed market/consensus/transcript providers within contract rights.
3. Official exchange/industry sources and dated broker research where permitted.
4. Manual evidence exports with timestamp, operator, and checksum.
5. Derived fixtures clearly labeled; never represented as provider-native evidence.

### 7.2 Mandatory source fields

`source_id`, publisher, title, source type, ticker, published/event/effective times, information cutoff, URL/path, checksum, verification status, license status, permitted use, retention class, parser/version, and reviewer.

### 7.3 Ingestion state machine

`received → quarantined → parsed → normalized → verified → indexed`  
Failure states: `rejected_schema`, `rejected_pit`, `rejected_license`, `rejected_security`, `needs_human`.

### 7.4 Tiered data policy

- MVP: public/official/manual-approved sources only.
- Enterprise: provider adapter plus entitlements, contract controls, expiry and deletion workflow.
- Raw licensed content is not sent to an external model unless permitted by contract and provider policy.
- If raw content must be deleted, retain only allowed provenance/checksum metadata.

Professional basis: CFA requires diligence over third-party research; Google MLOps emphasizes data validation and metadata; Thai SEC guidance requires identification and verification of sources in investment analysis. Sources: [CFA Standard V(A)](https://www.cfainstitute.org/standards/professionals/code-ethics-standards/standards-of-practice-v-a), [Google MLOps](https://docs.cloud.google.com/architecture/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning), [Thai SEC guidance](https://publish.sec.or.th/nrs/7901se.pdf).

---

## 8. Agent and Model Methodology

### 8.1 Model gateway contract

Nodes request `cheap`, `mid`, or `strong` capabilities with structured-output/tool/latency/cost requirements. Only gateway config names providers/models. Every call records model/version, config/prompt version, input/output object IDs, token/cost estimate, latency, retries/fallbacks, and policy decision.

### 8.2 Data egress policy

Classify each input before model invocation: `public`, `internal`, `licensed-restricted`, `MNPI/sensitive`. MVP accepts public/manual-approved data only. Restricted or MNPI-classified input fails closed until an Enterprise-approved provider and contract are configured.

### 8.3 Prompt/config change control

Prompt templates, model tiers, temperatures, tool schemas, retrieval weights, and thresholds are config-as-code. A change creates a versioned experiment against the same dataset and cannot enter `demo` unless hard gates pass and the decision is recorded.

### 8.4 No fine-tuning in MVP

Fine-tuning is reconsidered only when repeated, labeled errors cannot be solved by deterministic tools, retrieval, schema, or prompt changes and enough rights-cleared examples exist. This follows the agreed YAGNI boundary and Anthropic’s guidance to add complexity only when simpler patterns are insufficient. Source: [Anthropic](https://www.anthropic.com/engineering/building-effective-agents).

---

## 9. Retrieval Methodology

### 9.1 Single production path

Use PostgreSQL full-text search plus pgvector. Apply hard filters (`company`, `information_cutoff`, `license/permitted_use`, `purpose`, `verified`) before lexical/vector ranking. Fuse results with a versioned policy. Add a cross-encoder reranker only when measured retrieval errors justify its latency/cost.

### 9.2 Retrieval evaluation

- Curate expected passage/source IDs for each query.
- Report Recall@k, source precision, PIT violations, prohibited-source retrievals, latency, and empty-result rate.
- Test exact numbers/names, semantic paraphrases, ambiguous periods, stale documents, and conflicting sources.
- A good final answer cannot compensate for a prohibited/future source; that is a hard failure.

PostgreSQL documents full-text search; pgvector supports exact/approximate nearest-neighbor search and hybrid use with PostgreSQL text search. Sources: [PostgreSQL FTS](https://www.postgresql.org/docs/current/textsearch.html), [pgvector](https://github.com/pgvector/pgvector).

---

## 10. API, Worker, and UI Methodology

### 10.1 API pattern

- REST commands/queries with typed OpenAPI contracts.
- `POST /runs` returns `run_id`; it does not hold the workflow in the request.
- SSE streams server-to-client status/trace; polling is the fallback.
- Create/resume/export commands require idempotency keys.
- API errors use stable machine codes and safe human messages.

### 10.2 Durable execution

The worker claims a PostgreSQL job, checkpoints after each node/tool/gate, and records retry attempts. Resume validates run version, gate decision, expected checkpoint, and idempotency key before continuing. LangGraph interruptions rely on persisted state and resume commands. Sources: [LangGraph interrupts](https://docs.langchain.com/oss/python/langgraph/interrupts), [persistence](https://docs.langchain.com/oss/python/langgraph/persistence).

### 10.3 Next.js workbench

Required MVP views:

1. Run setup and source selection/upload.
2. Evidence/actual-estimate review.
3. Valuation gate and editable assumptions.
4. Note/citation/compliance review.
5. Trace/eval/replay results.

**No-auth limitation:** role selection sets a `demo_actor`; it does not prove identity. The UI must display “Private demo — unauthenticated actor” and the service must bind to local/private interfaces only.

---

## 11. Testing Strategy

| Layer | Protects against | Required examples |
|---|---|---|
| Static/contract | Boundary drift | Pydantic/OpenAPI/DB schema, prohibited imports/arithmetic |
| Unit | Local deterministic error | quant formulas, basis, PIT, citation resolver, policy rules |
| Integration | Component mismatch | PostgreSQL/pgvector, worker/checkpoint, model gateway, parser |
| Workflow | State/branch failure | happy path, gate edit/reject, timeout, retry, duplicate resume |
| Security | Adversarial misuse | prompt injection, malicious upload, tool misuse, data/secret leak, loop budget |
| Offline regression | Known behavior regression | 20 seed cases, all prior incidents |
| Capability | Quality progress | digest, grounding, note usefulness, retrieval, rating explanation |
| Human review | Domain judgment | finance rubric and second review on rating/target/compliance |
| Release/replay | Operational failure | clean deploy, backup/restore, rollback, kill switch, three-company replay |

LangSmith distinguishes tests (deployment-blocking assertions) from evaluations (quality measurements), recommends curated examples, and connects offline evaluation with production feedback. Sources: [LangSmith evaluation concepts](https://docs.langchain.com/langsmith/evaluation-concepts), [evaluation types](https://docs.langchain.com/langsmith/evaluation-types).

---

## 12. Evaluation and Release Targets

These are **approved project targets** to calibrate after baseline measurement:

| Metric/control | MVP release target | Failure action |
|---|---:|---|
| Schema, PIT, citation, deterministic math, gate-control tests | 100% | Block release |
| Critical factual error / future-source leakage / unauthorized export | 0 | Block and quarantine |
| Retrieval Recall@5 on golden evidence | ≥90% | Diagnose corpus/filter/query/fusion |
| Analyst correctness/completeness/usefulness rubric | Mean ≥4/5 and no Critical fail | Finance review and regression case |
| Full run before human gate | p95 ≤120 seconds | Profile model/retrieval/tools |
| Resume after approval | p95 ≤60 seconds | Profile checkpoint/downstream nodes |
| Model cost per complete run | p95 ≤US$0.50 | Route/context/tool optimization |
| Retry/resume duplicate artifact in test suite | 0 | Block release; fix idempotency |

### 12.1 Eval corpus growth

Start with the approved 20-case plan. Add every real demo/operation failure as a regression case. Coverage, not a vanity case count, controls growth: every critical branch needs at least one allow-path and one block-path case.

### 12.2 LLM judge policy

An LLM judge may triage or score only after comparison with finance-labeled examples. It is never release authority for rating, target, compliance, or critical factual correctness. LangSmith’s guidance explicitly supports aligning judges to human labels and inspecting disagreements. Source: [LangSmith judge alignment](https://docs.langchain.com/langsmith/improve-judge-evaluator-feedback).

---

## 13. Security and Supply-Chain Methodology

### 13.1 Threats required in the MVP threat model

- Direct/indirect prompt injection in filings, transcripts, or retrieved passages.
- Tool misuse or arguments outside allowlisted schemas.
- Excessive loops, token/cost exhaustion, retry storms.
- Sensitive/licensed data disclosure to model/provider/log/UI.
- Malicious upload, parser exploit, oversized/decompression input.
- Dependency/model/provider supply-chain compromise.
- Gate bypass, forged resume, duplicate export, trace tampering.
- Secrets in repo, prompt, trace, exception, or frontend bundle.

### 13.2 Required controls

- Least-functionality tool registry and deny-by-default permissions.
- Quarantine and deterministic validation before retrieval.
- Structured outputs and downstream validation.
- Per-run model/tool/time/token/cost budgets.
- Immutable audit events/checksums and append-only release evidence.
- Dependency inventory/SBOM and reviewed provider/model inventory.
- Kill switches for model calls, workflow resume, and export.

Sources: [OWASP LLM Top 10](https://owasp.org/www-project-top-10-for-large-language-model-applications/), [OWASP Agentic Security](https://genai.owasp.org/), [NIST SSDF](https://csrc.nist.gov/pubs/sp/800/218/final), [CycloneDX ML-BOM](https://cyclonedx.org/capabilities/mlbom/).

---

## 14. Equity-Research Governance

### 14.1 Reasonable basis and objectivity

Every recommendation must link to verified facts, methodology, assumptions, valuation evidence, risks, and reviewer decisions. The analyst remains accountable for personal judgment; conflicts and compensation/distribution requirements depend on jurisdiction and firm policy. Sources: [CFA Standard V(A)](https://www.cfainstitute.org/standards/professionals/code-ethics-standards/standards-of-practice-v-a), [CFA Research Objectivity Standards](https://www.cfainstitute.org/sites/default/files/-/media/documents/code/other-codes-standards/read-research-objectivity-standards.pdf), [SEC Regulation AC](https://www.sec.gov/rules-regulations/2003/03/regulation-analyst-certification), [FINRA Rule 2241](https://www.finra.org/rules-guidance/rulebooks/finra-rules/2241).

### 14.2 Jurisdiction policy

**Project decision:** Thailand-first. Thai SEC/IAA context drives deployment questions; CFA, US, and EU rules are global professional references and are not automatically asserted as directly applicable. EU 2016/958 covers objective presentation and disclosure of interests for investment recommendations. Sources: [EU 2016/958](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32016R0958), [Thai SEC IA guidance](https://publish.sec.or.th/nrs/7901se.pdf), [IAA role](https://www.iaathai.org/about/).

### 14.3 Model-risk reference update

Use **SR 26-2**, not SR 11-7, as the current US interagency model-risk reference. SR 26-2 superseded SR 11-7 on 2026-04-17 and retains a risk-based lifecycle covering model development/use, validation/monitoring, governance/controls, and third-party products. It is a reference framework here, not a statement that this hackathon product is a regulated bank model. Sources: [SR 26-2 letter](https://www.federalreserve.gov/supervisionreg/srletters/SR2602.htm), [current guidance](https://www.federalreserve.gov/frrs/guidance/supervisory-guidance-on-model-risk-management.htm).

---

## 15. Observability, Reliability, and Cost

### 15.1 Trace requirements

Every run links spans/events for API, worker, node, retrieval, tool, model, gate, checker, and export. Record object/source/citation IDs, model/config versions, tokens/cost, latency, retries/fallbacks, checkpoint, errors, and actor decision. OpenTelemetry provides vendor-neutral trace/metric/log concepts and GenAI conventions are evolving; keep the local schema compatible but versioned. Sources: [OpenTelemetry docs](https://opentelemetry.io/docs/), [GenAI observability](https://opentelemetry.io/blog/2026/genai-observability/).

### 15.2 SLO/budget process

- Define user-visible service indicator, target, measurement window, and owner.
- Separate hard correctness controls from service budgets.
- Alert only on actionable conditions with a runbook.
- Review p50/p95/p99 latency, error/retry rate, token/cost, retrieval misses, gate rate, citation/PIT failures, and human overrides.
- Enterprise SLOs and error budgets are set only after representative load and operational ownership exist.

Google SRE treats SLOs and production-readiness checks as operating agreements and recommends evaluating safer partial releases with rollback. Sources: [Google SRE SLO resources](https://sre.google/resources/practices-and-processes/art-of-slos/), [canarying](https://sre.google/workbook/canarying-releases/).

### 15.3 Cost control

Track cost per run/node/model tier, token volume, cache/fallback behavior, and business-value metric. Enforce maximum token/tool/loop budgets. Google’s AI/ML cost guidance recommends explicit cost/value KPIs, budgets/alerts, experimentation, and continuous optimization. Source: [Google AI/ML cost optimization](https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml/cost-optimization).

---

## 16. Environments, Change, and Release

### 16.1 MVP environments

| Environment | Purpose | Data/config rule |
|---|---|---|
| `dev` | Local implementation and exploratory runs | May change; no release claims |
| `test` | Automated unit/integration/eval | Disposable DB; versioned test data |
| `demo` | Frozen private candidate | Immutable evidence/config/release manifest |

Enterprise later adds `staging` and `production` with trusted identity, managed secrets, alerts, backups, and deployment approvals.

### 16.2 Source-control procedure when Git is enabled

**Project decision:** trunk-based development with short-lived branches, reviewed changes, required CI checks, and tagged demo releases. This document does not initialize Git. NIST SSDF supports protecting code, tracking security requirements/design decisions, and retaining release provenance. Source: [NIST SSDF](https://csrc.nist.gov/pubs/sp/800/218/final).

### 16.3 Release manifest

Each candidate records code/build ID, migration/schema, image/dependency inventory, evidence checksums, fixture/dataset/evaluator versions, model/prompt/retrieval config, test/eval scorecard, known limitations, backup/restore proof, rollback target, and sign-offs.

---

## 17. Incident, Continuity, and Recovery

### 17.1 MVP incident controls

- Severity: `Critical` (unsafe disclosure/control bypass), `High` (material factual/valuation failure), `Normal` (recoverable quality/availability issue).
- Kill switches: model calls, workflow resume, and export.
- Fail-closed response: stop/quarantine run, preserve trace/evidence, rotate/revoke affected secret if relevant, rollback config, use verified replay for demo continuity.
- Every material incident creates root cause, corrective action, owner, and regression case.

### 17.2 Backup and recovery

MVP requires a reproducible release pack, PostgreSQL backup, and at least one tested restore. Enterprise adds automated backups, PITR, RPO/RTO targets, and DR drills. Google SRE emphasizes production readiness, recoverability, rollback, and verification of data-processing releases. Sources: [Google SRE data processing](https://sre.google/workbook/data-processing/), [configuration rollback](https://sre.google/workbook/configuration-design/).

---

## 18. Definition of Done

### 18.1 Work-item DoD

- Requirement/control ID and owner exist.
- Acceptance tests/eval rubric written.
- Typed contract and error behavior documented.
- Implementation has trace/metrics at the required boundary.
- Positive and negative paths pass.
- Security/data/license impact reviewed.
- User/domain reviewer accepts the artifact.
- Documentation and release evidence are linked.

### 18.2 Phase DoD

- Required artifacts exist and contain no unresolved blocker/TBD.
- Exit-gate evidence is reproducible from a clean environment.
- Regression suite remains green.
- New risks and residual-risk decisions are recorded.
- Rollback/recovery path remains valid.

### 18.3 Private MVP DoD

- MSFT/AMZN/PTT run through the complete P2 path.
- Valuation and compliance interrupts/resume/reject paths work.
- §12 hard gates and targets pass.
- Evidence/citation/PIT/license checks are visible in UI/trace.
- Clean deploy, backup/restore, kill switch, rollback, and verified replay are demonstrated.
- UI states the no-auth/private-demo limitation.
- Final claims match actual evidence; missing aggregate-consensus evidence is not overstated.

This DoD combines release validation, metadata/reproducibility, secure-SDLC evidence, and domain approval rather than treating test execution alone as completion. Sources: [Google MLOps](https://docs.cloud.google.com/architecture/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning), [NIST SSDF](https://csrc.nist.gov/pubs/sp/800/218/final), [CFA Research Objectivity Standards](https://www.cfainstitute.org/sites/default/files/-/media/documents/code/other-codes-standards/read-research-objectivity-standards.pdf).

---

## 19. Anti-Patterns and Stop Rules

Stop the build/release when any of these appears:

- Adding a new framework before the walking skeleton or an eval-proven need.
- Hiding business/finance logic in UI, prompt, or broad dictionaries.
- Allowing an LLM to calculate authoritative finance values.
- Using current/future evidence in a point-in-time decision without explicit post-event mode.
- Calling single-house/manual evidence “aggregate consensus.”
- Sending restricted/MNPI content to an unapproved provider.
- Retrying non-idempotent export/resume without protection.
- Treating an LLM judge as the final finance/compliance reviewer.
- Exposing the no-auth MVP publicly.
- Promoting a model/prompt/retrieval change without baseline comparison.
- Declaring production readiness without trusted identity, licensed-data review, operational controls, and legal approval.

These stop rules operationalize limited agency, secure SDLC, reasonable basis, and continuous risk management. Sources: [OWASP LLM06](https://owasp.org/www-project-top-10-for-large-language-model-applications/2_0_vulns/LLM06_ExcessiveAgency.html), [NIST SSDF](https://csrc.nist.gov/pubs/sp/800/218/final), [CFA Standard V(A)](https://www.cfainstitute.org/standards/professionals/code-ethics-standards/standards-of-practice-v-a), [NIST AI RMF](https://airc.nist.gov/airmf-resources/airmf/5-sec-core/).

---

## 20. Ordered Next Artifacts — No Date Assumptions

1. Freeze this methodology and update the roadmap/blueprint decision references.
2. Convert approved product decisions into a requirements/control traceability table.
3. Finalize domain/API/DB/state/error contracts and ADRs.
4. Define PostgreSQL schema/migrations and durable job/checkpoint protocol.
5. Define Next.js page/state map and FastAPI OpenAPI contract.
6. Build evidence quarantine/manifest/validation pipeline.
7. Build PostgreSQL FTS + pgvector corpus and retrieval eval set.
8. Build one-node walking skeleton end-to-end.
9. Add six P2 slices in dependency order with tests first.
10. Make the 20-case eval plan executable and calibrate human rubric.
11. Add threat tests, supply-chain inventory, kill switches, and runbooks.
12. Produce reproducible private release pack and complete the Private MVP DoD.
13. Only then plan Enterprise hardening gates.

This ordering follows the professional pattern of scope/risk → contracts/data → walking skeleton → capability → evaluation/security → release/operate, while preserving the project’s existing Phase 0-8 blueprint. Sources: [AWS GenAI lifecycle](https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/generative-ai-lifecycle.html), [Google MLOps](https://docs.cloud.google.com/architecture/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning), [Anthropic](https://www.anthropic.com/engineering/building-effective-agents).

---

## 21. Decision Register — Approved 2026-07-18

Evidence for this section is the Step 5 design review with the project owner on 2026-07-18. These rows are project decisions, not external factual claims; cited professional rationale appears in §§1-20.

The register format also supports traceability and continual risk review described by [NIST AI RMF](https://airc.nist.gov/airmf-resources/airmf/5-sec-core/) and [NIST SSDF](https://csrc.nist.gov/projects/ssdf).

| Decision | Approved outcome |
|---|---|
| Product path | Internal Analyst Copilot MVP → Enterprise Research Platform |
| Publishing | No autonomous external publishing |
| Deployment | Local/private, Dockerized, cloud-neutral MVP |
| Frontend/API | React/Next.js + FastAPI |
| Authentication | None in MVP; explicit demo actor/limitation; auth/RBAC/SSO blocks Enterprise |
| Runtime state | PostgreSQL from first product build |
| Long-running jobs | Durable worker + PostgreSQL job/checkpoint state |
| API updates | REST + SSE, polling fallback, idempotency |
| Data policy | Public/manual-approved MVP; licensed adapters + contract controls for Enterprise |
| Ingestion | Curated upload + official adapters; quarantine and deterministic validation |
| Retrieval | PostgreSQL full-text + pgvector; no Chroma; reranker only if eval proves need |
| Models | Provider-neutral tier gateway; no fine-tuning in MVP |
| Observability | OTel-compatible local PostgreSQL/JSON trace; external exporter optional |
| Quality priority | Correctness/auditability before latency/cost |
| Eval ownership | Finance ground truth + second review for critical judgment |
| Eval growth | Coverage-driven from 20 seed cases and real failures |
| Environments | `dev`, `test`, `demo`; Enterprise adds `staging`, `production` |
| Git workflow | Future trunk-based workflow; do not initialize Git in this step |
| Jurisdiction | Thailand-first; global references labeled; legal review required |
| Retention | Policy/contract-driven with immutable release evidence |
| Recovery | Reproducible release pack + restore-tested PostgreSQL backup |
| Incident control | Kill switches + fail-closed runbook |
| Schedule | No dates in methodology; dependency order only |

---

## 22. Canonical Sources

### AI lifecycle, governance, and architecture

- [NIST AI RMF Core](https://airc.nist.gov/airmf-resources/airmf/5-sec-core/)
- [NIST AI RMF Generative AI Profile](https://www.nist.gov/itl/ai-risk-management-framework)
- [ISO/IEC 42001:2023](https://www.iso.org/standard/42001)
- [AWS Generative AI Lens](https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/generative-ai-lifecycle.html)
- [AWS Machine Learning Lens](https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/)
- [Google MLOps](https://docs.cloud.google.com/architecture/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning)
- [Anthropic: Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents)

### Runtime, retrieval, evaluation, and operations

- [LangGraph interrupts](https://docs.langchain.com/oss/python/langgraph/interrupts)
- [LangGraph persistence](https://docs.langchain.com/oss/python/langgraph/persistence)
- [Pydantic strict mode](https://docs.pydantic.dev/latest/concepts/strict_mode/)
- [PostgreSQL full-text search](https://www.postgresql.org/docs/current/textsearch.html)
- [pgvector](https://github.com/pgvector/pgvector)
- [OpenTelemetry](https://opentelemetry.io/docs/)
- [LangSmith evaluation concepts](https://docs.langchain.com/langsmith/evaluation-concepts)
- [Google SRE canarying](https://sre.google/workbook/canarying-releases/)
- [Google SRE data processing](https://sre.google/workbook/data-processing/)
- [Google AI/ML cost optimization](https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml/cost-optimization)

### Security and supply chain

- [NIST SP 800-218 SSDF](https://csrc.nist.gov/pubs/sp/800/218/final)
- [OWASP LLM Top 10](https://owasp.org/www-project-top-10-for-large-language-model-applications/)
- [OWASP GenAI/Agentic Security](https://genai.owasp.org/)
- [CycloneDX ML-BOM](https://cyclonedx.org/capabilities/mlbom/)

### Equity research and financial-services governance

- [CFA Standard V(A): Diligence and Reasonable Basis](https://www.cfainstitute.org/standards/professionals/code-ethics-standards/standards-of-practice-v-a)
- [CFA Research Objectivity Standards](https://www.cfainstitute.org/sites/default/files/-/media/documents/code/other-codes-standards/read-research-objectivity-standards.pdf)
- [FINRA Rule 2241](https://www.finra.org/rules-guidance/rulebooks/finra-rules/2241)
- [FINRA Notice 24-09 on GenAI](https://www.finra.org/rules-guidance/notices/24-09)
- [SEC Regulation Analyst Certification](https://www.sec.gov/rules-regulations/2003/03/regulation-analyst-certification)
- [EU Delegated Regulation 2016/958](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32016R0958)
- [Federal Reserve SR 26-2](https://www.federalreserve.gov/supervisionreg/srletters/SR2602.htm)
- [Thai SEC IA practice guidance — unofficial English translation](https://publish.sec.or.th/nrs/7901se.pdf)
- [Investment Analysts Association Thailand](https://www.iaathai.org/about/)
