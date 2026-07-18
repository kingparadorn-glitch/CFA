# Step 6 Implementation Readiness Plan

> **For agentic workers:** implement this plan task-by-task with tests first. Do not start a later work package until the current exit gate passes.

**Goal:** make Step 7 directly executable by defining the canonical file map, dependency order, interfaces, tests/evaluations, risks, and entry gates for the ER P2 private MVP.

**Architecture:** preserve the existing deterministic L0-L9 harness as the regression baseline, then add a typed FastAPI/PostgreSQL/durable-worker walking skeleton before expanding to the six-node LangGraph workflow. Next.js is a thin analyst workbench; deterministic finance, evidence policy, workflow state, gates, and audit logic remain server-side.

**Tech stack:** Python 3.11+, FastAPI, Pydantic v2 strict models, PostgreSQL + pgvector, SQLAlchemy 2 + psycopg 3 + Alembic, LangGraph, LiteLLM provider gateway, Next.js/React/TypeScript, Vitest + React Testing Library + Playwright, Server-Sent Events with polling fallback, OpenTelemetry-compatible local traces, Docker Compose for local/private execution.

Persistence-tooling rationale: SQLAlchemy documents first-class PostgreSQL support through the psycopg 3 dialect, while Alembic is the migration tool built for SQLAlchemy metadata and versioned schema changes. Sources: [SQLAlchemy PostgreSQL/psycopg](https://docs.sqlalchemy.org/en/20/dialects/postgresql.html), [Alembic documentation](https://alembic.sqlalchemy.org/en/latest/).

## Global Constraints

- Scope is P2 Earnings Update only; MSFT, AMZN, and PTT are the demo/eval universe.
- MVP is local/private and has no authentication. `demo_actor` is not a trusted identity.
- No autonomous external publishing. Export requires an approved compliance decision.
- Every factual claim and finance number must resolve to verified evidence and citation IDs.
- Every source-dependent object must pass point-in-time, permitted-use, and basis validation.
- All financial arithmetic stays in deterministic tools; LLMs may explain but may not calculate finance outputs.
- PostgreSQL is the durable source of truth for runs, jobs, checkpoints, gates, traces, and artifacts.
- PostgreSQL full-text search plus pgvector is the only MVP retrieval path; do not add Chroma.
- Model calls go through provider-neutral `cheap` / `mid` / `strong` tier configuration; no fine-tuning in MVP.
- Exact model names are benchmarked and frozen during Work Package 0/11; nodes never hard-code providers.
- Git state-changing commands are owner-run only. AI may inspect status/diff and propose commands/messages, but must not run `git init`, `git add`, `git commit`, branch/tag creation, reset, clean, or checkout.
- No dependency installation, runtime implementation, Git initialization, or commit is part of Step 6.
- Step 7 follows dependency order, not calendar dates.

---

## 0. Research Log and Evidence Basis

### Structural grounding

This plan uses the project-approved lifecycle in `professional_build_methodology.md` and converts it into independently testable work packages. The structure follows:

- secure-development tasks and verification criteria from [NIST SSDF](https://csrc.nist.gov/projects/ssdf);
- typed API contracts from [OpenAPI](https://spec.openapis.org/oas/latest.html) and [Pydantic strict mode](https://docs.pydantic.dev/latest/concepts/strict_mode/);
- persistent checkpoints and human resume semantics from [LangGraph persistence](https://docs.langchain.com/oss/python/langgraph/persistence) and [interrupts](https://docs.langchain.com/oss/python/langgraph/interrupts);
- layered API and browser testing from [FastAPI testing](https://fastapi.tiangolo.com/tutorial/testing/) and [Next.js testing](https://nextjs.org/docs/app/guides/testing);
- tests versus quality evaluation separation from [LangSmith evaluation concepts](https://docs.langchain.com/langsmith/evaluation-concepts);
- vendor-neutral trace concepts from [OpenTelemetry](https://opentelemetry.io/docs/).

### Project facts inspected

- `pipeline.py`, `tools/quant.py`, and `cli.py` implement a deterministic fixture-driven smoke path.
- `test_l0_l9_io.py` currently contains 16 unit/smoke/document-contract tests.
- three company fixtures exist under `07_implementation/data/raw/`.
- `make test` and `make smoke-l0-l9` are the only current project verification commands.
- FastAPI, Next.js, PostgreSQL, worker/checkpoint runtime, LangGraph nodes, retrieval, runtime trace, and human-gate UI are not implemented.
- `07_implementation/requirements.txt` is stale: it still names Chroma and Langfuse while omitting the approved API/database stack. It must not be installed as-is.

No external factual market data is introduced by this plan. Finance facts remain governed by the company evidence pack and fixture provenance.

---

## 1. Step 6 Outcome and Status

Step 6 does not build the product. It removes ambiguity before Step 7 by producing five controls:

1. one source-of-truth hierarchy;
2. one target file map;
3. one dependency-ordered implementation sequence;
4. one test/evaluation ownership and release matrix;
5. one explicit Step 7 entry checklist.

**Step 6 verdict:** Step 7 implementation readiness is locked at 100% for starting Work Package 0. This does not mean the product is built; it means the decisions, file map, order, gates, and verification rules are now unambiguous enough to begin product implementation without reopening planning.

Professional rationale: outcome-based preparation and verification criteria reduce ambiguity before software production. Source: [NIST SSDF](https://csrc.nist.gov/projects/ssdf).

---

## 2. Source-of-Truth and File Map

### 2.1 Precedence when documents disagree

| Priority | Source | Governs | Does not govern |
|---:|---|---|---|
| 1 | `04_reference_materials/` competition PDFs | judging rules and competition constraints | runtime design |
| 2 | `professional_build_methodology.md` decision register | approved product, stack, trust, release, and operating decisions | finance formulas |
| 3 | `runtime_schema_contract.md` + `json_trace_schema.md` | runtime handoff and trace fields | product scope |
| 4 | `equity_research_deep_dive.md` | P2 finance workflow, formulas, rating/valuation meaning | software layout |
| 5 | `ai_architecture_design.md` | L0-L9 responsibilities and control intent | exact package names |
| 6 | `er_p2_mvp_dev_blueprint.md` | build phases and module boundaries | outdated illustrative snippets when they conflict with priorities 1-5 |
| 7 | this file | Step 7 file map, dependency order, tests, risks, and entry gates | new product scope |
| 8 | `07_implementation/README.md` | current implementation status and commands | design decisions |

Conflict rule: use the higher-priority source, record the conflict as a plan issue, and update the lower-priority document before implementing the affected task. Do not silently choose one interpretation.

### 2.2 Existing files that remain authoritative

| File | Role in Step 7 | Read by work packages |
|---|---|---|
| `07_implementation/src/er_engine/pipeline.py` | deterministic baseline; remains until runtime parity is proven | 0, 4, 11, 13 |
| `07_implementation/src/er_engine/tools/quant.py` | approved home for finance arithmetic | 4, 8 |
| `07_implementation/tests/test_l0_l9_io.py` | current regression baseline | every package |
| `07_implementation/data/raw/*.json` | versioned company fixtures | 4, 7, 12, 13 |
| `07_implementation/docs/runtime_schema_contract.md` | domain object contract | 1-11 |
| `07_implementation/docs/json_trace_schema.md` | trace/audit contract | 3, 6, 9-13 |
| `07_implementation/docs/eval_case_plan.md` | seed eval catalogue | 11, 13 |

### 2.3 Target implementation tree

Paths below are the approved destinations for Step 7. A task may create only its listed paths or make a documented amendment to this plan first.

```text
07_implementation/
├── compose.yaml
├── .env.example
├── alembic.ini
├── alembic/
│   ├── env.py
│   └── versions/
├── apps/web/
│   ├── package.json
│   ├── next.config.ts
│   ├── app/
│   │   ├── page.tsx
│   │   └── runs/[runId]/page.tsx
│   ├── components/
│   │   ├── run-setup.tsx
│   │   ├── evidence-review.tsx
│   │   ├── valuation-gate.tsx
│   │   ├── note-review.tsx
│   │   └── trace-panel.tsx
│   ├── lib/
│       ├── api.ts
│       └── types.ts
│   └── e2e/analyst-workflow.spec.ts
├── config/
│   ├── model_tiers.yaml
│   └── p2_policy.yaml
├── prompts/p2/
│   ├── digest.txt
│   ├── draft_note.txt
│   └── compliance.txt
├── src/er_engine/
│   ├── api/
│   │   ├── app.py
│   │   ├── dependencies.py
│   │   └── routes/{runs,gates,events,exports,evals}.py
│   ├── config/settings.py
│   ├── schemas/{common,source,event,finance,note,gate,run,trace,eval}.py
│   ├── db/{engine,models,repositories}.py
│   ├── worker/{main,queue}.py
│   ├── ingest/{loader,validator}.py
│   ├── retrieval/{indexer,hybrid,repository}.py
│   ├── graph/{state,p2_graph}.py
│   ├── nodes/{digest,update_model,revalue_rating,draft_note,compliance,publish}.py
│   ├── memory/forecast_error.py
│   ├── model_gateway/{client,structured_output}.py
│   ├── router/{cache,model_router,tiers}.py
│   ├── obs/trace.py
│   ├── eval/{cases,evaluators,harness,rubric}.py
│   ├── pipeline.py
│   └── tools/quant.py
└── tests/
    ├── unit/
    ├── contract/
    ├── integration/
    ├── workflow/
    ├── eval/
    └── e2e/
```

Boundary rules:

- `schemas/` contains transport/domain types, not persistence queries.
- `db/` owns transactions and persistence, not finance policy.
- `nodes/` orchestrate schemas, tools, retrieval, and model calls; they contain no raw finance arithmetic.
- `tools/quant.py` remains deterministic and model-independent.
- `config/` and `prompts/` are versioned inputs; model names, thresholds, budgets, and prompt text are not hard-coded in nodes.
- `api/` exposes commands/queries but does not execute long-running P2 work in request threads.
- `apps/web/` contains presentation state only; it cannot approve itself, compute valuation, or bypass server gates.
- `eval/` consumes public contracts and traces; runtime modules never special-case eval IDs.

Sources: [OpenAPI](https://spec.openapis.org/oas/latest.html), [Pydantic strict mode](https://docs.pydantic.dev/latest/concepts/strict_mode/), [FastAPI testing](https://fastapi.tiangolo.com/tutorial/testing/).

---

## 3. Runtime Interfaces to Freeze Before Coding

### 3.1 Run state machine

```text
created -> queued -> running -> requires_human
                         |              |
                         |              +-> queued -> running
                         |              +-> blocked
                         +-> succeeded
                         +-> failed
                         +-> blocked
```

Allowed transitions must be enforced in the repository/service layer. A gate decision cannot change a terminal run. A resume must use the same `run_id`, graph `thread_id`, expected `checkpoint_id`, and an unused idempotency key.

### 3.2 API surface

| Method and path | Purpose | Idempotency | Main response |
|---|---|---|---|
| `POST /v1/runs` | create one P2 run from a verified fixture/event | required | `RunView` with `run_id`, `status=queued` |
| `GET /v1/runs/{run_id}` | read current state and artifact pointers | no | `RunView` |
| `GET /v1/runs/{run_id}/events` | stream status/trace events via SSE | no | ordered `RunEvent` stream |
| `POST /v1/runs/{run_id}/gates/{gate_id}/decisions` | approve, edit/resume, reject, or request evidence | required | `GateDecisionView` |
| `POST /v1/runs/{run_id}/exports` | create private note artifact after compliance approval | required | `ArtifactView` |
| `POST /v1/eval-runs` | execute a versioned eval selection | required | `EvalRunView` |
| `GET /v1/eval-runs/{eval_run_id}` | read eval results | no | per-case result list and scorecard |

Every command accepts `Idempotency-Key`. MVP actor input is `demo_actor`; responses and UI must label it `actor_trust=unauthenticated_demo`.

### 3.3 Durable job contract

```python
class JobStatus(str, Enum):
    queued = "queued"
    claimed = "claimed"
    running = "running"
    retry_wait = "retry_wait"
    succeeded = "succeeded"
    failed = "failed"

def enqueue_run(run_id: UUID, idempotency_key: str) -> UUID: ...
def claim_next_job(worker_id: str) -> JobRecord | None: ...
def checkpoint_job(job_id: UUID, node_name: str, checkpoint_id: str) -> None: ...
def complete_job(job_id: UUID, artifact_id: UUID) -> None: ...
```

`claim_next_job` must use one transaction and PostgreSQL row locking so two workers cannot claim the same job. Side effects before a LangGraph interrupt must be idempotent because the interrupted node restarts from its beginning on resume. Source: [LangGraph interrupt rules](https://docs.langchain.com/oss/python/langgraph/interrupts).

### 3.4 Workflow node contract

```python
class P2State(BaseModel):
    run_id: UUID
    thread_id: str
    event: EarningsEvent
    digest: DigestResult | None = None
    model_update: ModelUpdateResult | None = None
    valuation: ValuationResult | None = None
    note: ResearchNote | None = None
    pending_gate: GateRequest | None = None
    trace_id: str

Node = Callable[[P2State, RuntimeContext], dict[str, object]]
```

Node return values are validated updates. Do not mutate shared state in place and do not call `.model_dump()` merely to pass loose dictionaries between production nodes.

### 3.5 Error taxonomy

| Code family | Retry? | Run effect | Example |
|---|---:|---|---|
| `INPUT_*` | no | blocked | unverified source, invalid basis, future source |
| `CONTRACT_*` | no | failed | malformed structured model output after allowed repair |
| `MODEL_TRANSIENT_*` | bounded | retry_wait | timeout, rate limit, provider unavailable |
| `MODEL_POLICY_*` | no | blocked | prohibited model/data-egress route |
| `DB_TRANSIENT_*` | bounded | retry_wait | reconnectable database failure |
| `GATE_*` | no | requires_human/blocked | deviation threshold, citation failure, rejection |
| `EXPORT_*` | bounded only if idempotent | failed/blocked | missing approval, duplicate artifact attempt |

The exact error code and retry count must be written to the trace. Fail-closed behavior follows the approved methodology and [NIST SSDF](https://csrc.nist.gov/projects/ssdf).

---

## 4. Dependency-Ordered Step 7 Work Packages

Each package is a review gate. The engineer writes the named failing tests first, observes failure, implements the smallest passing behavior, and reruns the current baseline. Git commands are intentionally absent until the project owner initializes Git.

### Work Package 0: Reconcile toolchain and preserve the baseline

**Files:**

- Modify: root `pyproject.toml`
- Modify: root `Makefile`
- Replace during Step 7: `07_implementation/requirements.txt` with a generated/locked dependency artifact or remove it after the canonical dependency source is approved
- Create: `07_implementation/apps/web/package.json`
- Test: existing `07_implementation/tests/test_l0_l9_io.py`

**Consumes:** approved stack in `professional_build_methodology.md` §21.

**Produces:** one canonical Python dependency declaration, one frontend manifest, and real commands for unit, integration, eval, backend, worker, frontend, and E2E tasks.

- [ ] Add FastAPI, Pydantic v2, SQLAlchemy 2, psycopg 3, Alembic, LangGraph, LiteLLM, pgvector client support, pytest, and HTTP test dependencies to the canonical Python manifest.
- [ ] Remove Chroma, `rank-bm25`, `sentence-transformers`, and mandatory Langfuse from the MVP path unless a later measured requirement reintroduces them.
- [ ] Add Next.js, React, TypeScript, unit/component test tooling, and Playwright scripts to the frontend manifest.
- [ ] Record the approved SQLAlchemy 2 + psycopg 3 + Alembic choice, or amend Packages 2-5 consistently before installing dependencies.
- [ ] Run the old baseline before and after manifest changes.

Run before changes:

```bash
make test
make smoke-l0-l9
```

Expected: 16 tests pass and output contains three fixture results. If this baseline fails, stop and diagnose before adding the runtime.

**Exit gate:** dependency sources no longer contradict the approved stack; baseline behavior is unchanged; no package has been installed from the stale requirements file.

### Work Package 1: Implement strict domain and API contracts

**Files:**

- Create: `07_implementation/src/er_engine/schemas/{common,source,event,finance,note,gate,run,trace,eval}.py`
- Create: `07_implementation/tests/contract/test_runtime_schemas.py`
- Modify: `07_implementation/docs/runtime_schema_contract.md` only if implementation exposes a genuine ambiguity

**Consumes:** `runtime_schema_contract.md`, `json_trace_schema.md`, company fixtures.

**Produces:** strict Pydantic models named in §3 and JSON Schema/OpenAPI-compatible representations.

- [ ] Write tests proving valid MSFT/AMZN/PTT records round-trip without losing source, basis, PIT, or citation fields.
- [ ] Write rejection tests for unknown fields, missing citation IDs, mixed actual/estimate basis, invalid enum values, and future source use.
- [ ] Implement strict models and validators.
- [ ] Add schema-version fields to persisted top-level objects.

Run:

```bash
python3 -m pytest 07_implementation/tests/contract/test_runtime_schemas.py -q
make test
```

Expected: contract tests pass and all 16 legacy tests remain green.

**Exit gate:** no production handoff requires an untyped `dict`; every factual/numeric object preserves source, basis, unit, and citation linkage. Source: [Pydantic strict mode](https://docs.pydantic.dev/latest/concepts/strict_mode/).

### Work Package 2: Implement PostgreSQL schema, migrations, and repositories

**Files:**

- Create: `07_implementation/alembic.ini`, `07_implementation/alembic/env.py`, migration files
- Create: `07_implementation/src/er_engine/db/{engine,models,repositories}.py`
- Create: `07_implementation/tests/integration/test_database_contract.py`
- Create: `07_implementation/compose.yaml`, `07_implementation/.env.example`

**Consumes:** strict schemas and state machine in §3.

**Produces:** tables for runs, jobs, checkpoints, sources, passages, claims, citations, gates, traces, artifacts, idempotency keys, exact-cache entries, eval runs, and eval results.

- [ ] Write migration-up and clean-database tests.
- [ ] Write uniqueness tests for idempotency keys and artifact identity.
- [ ] Write legal/illegal run-transition tests.
- [ ] Write concurrent job-claim test proving one job has one owner.
- [ ] Implement repositories with explicit transaction boundaries.
- [ ] Run a backup/restore smoke against disposable local data before release work.

Run:

```bash
docker compose -f 07_implementation/compose.yaml up -d db
python3 -m pytest 07_implementation/tests/integration/test_database_contract.py -q
```

Expected: migrations apply to an empty database, constraints reject illegal states, and the concurrent claim test yields one successful claimant.

**Exit gate:** PostgreSQL is the source of truth and restart-safe state exists before any background workflow is added. Sources: [PostgreSQL transactions](https://www.postgresql.org/docs/current/tutorial-transactions.html), [LangGraph persistence](https://docs.langchain.com/oss/python/langgraph/persistence).

### Work Package 3: Add trace writer and durable job worker

**Files:**

- Create: `07_implementation/src/er_engine/obs/trace.py`
- Create: `07_implementation/src/er_engine/worker/{queue,main}.py`
- Create: `07_implementation/tests/integration/test_worker_recovery.py`
- Create: `07_implementation/tests/contract/test_trace_contract.py`

**Consumes:** database repositories, `json_trace_schema.md`.

**Produces:** job claim/retry/checkpoint lifecycle and versioned OTel-compatible trace records.

- [ ] Test worker crash after checkpoint and restart from the last successful step.
- [ ] Test retry budget exhaustion and error persistence.
- [ ] Test duplicate enqueue and completion produce one job/artifact.
- [ ] Test every node event conforms to the trace contract.
- [ ] Implement bounded exponential retry only for retryable error families.

Run:

```bash
python3 -m pytest 07_implementation/tests/contract/test_trace_contract.py 07_implementation/tests/integration/test_worker_recovery.py -q
```

Expected: restart resumes without duplicate effects and trace records contain run/config/prompt/schema versions.

**Exit gate:** worker/API restarts cannot lose run state or duplicate completed artifacts. Sources: [LangGraph persistence](https://docs.langchain.com/oss/python/langgraph/persistence), [OpenTelemetry](https://opentelemetry.io/docs/).

### Work Package 4: Convert fixtures into validated runtime inputs

**Files:**

- Create: `07_implementation/src/er_engine/ingest/{loader,validator}.py`
- Create: `07_implementation/tests/unit/test_ingest_policy.py`
- Add parser fixtures under: `07_implementation/tests/fixtures/ingest/`
- Preserve: `07_implementation/src/er_engine/pipeline.py`

**Consumes:** company fixtures, source registry, schema models.

**Produces:** `EarningsEvent`, `EarningsInput`, `SourceRef`, `Citation`, and rejected-source records.

- [ ] Test valid fixtures, duplicate checksum, unsupported type, unknown source, future source, prohibited use, missing citation, and GAAP/non-GAAP mismatch.
- [ ] Implement deterministic fixture adapter and validation pipeline.
- [ ] Quarantine invalid input instead of partially indexing it.
- [ ] Compare typed runtime input with deterministic baseline output for all three companies.

Run:

```bash
python3 -m pytest 07_implementation/tests/unit/test_ingest_policy.py -q
make smoke-l0-l9
```

Expected: all invalid inputs fail closed and all three verified fixtures preserve their current deterministic outputs.

**Exit gate:** only verified, permitted, PIT-safe evidence can enter runtime storage. Sources: [CFA Standard V(A)](https://www.cfainstitute.org/standards/professionals/code-ethics-standards/standards-of-practice-v-a), [NIST SSDF](https://csrc.nist.gov/projects/ssdf).

### Work Package 5: Build the FastAPI run lifecycle

**Files:**

- Create: `07_implementation/src/er_engine/api/app.py`
- Create: `07_implementation/src/er_engine/api/dependencies.py`
- Create: `07_implementation/src/er_engine/api/routes/{runs,gates,events,exports,evals}.py`
- Create: `07_implementation/tests/contract/test_openapi_contract.py`
- Create: `07_implementation/tests/integration/test_run_api.py`

**Consumes:** schemas, repositories, queue.

**Produces:** API surface in §3.2 and generated OpenAPI schema.

- [ ] Test invalid event/source rejection, create idempotency, run lookup, unknown run, gate conflict, unauthorized export-by-state, SSE event ordering/reconnect, polling fallback, and stable error envelopes.
- [ ] Test OpenAPI response schemas against Pydantic models.
- [ ] Implement create as enqueue-only; request handlers must not execute P2 work.
- [ ] Bind local/private by default and expose no production-trust language.

Run:

```bash
python3 -m pytest 07_implementation/tests/contract/test_openapi_contract.py 07_implementation/tests/integration/test_run_api.py -q
```

Expected: repeated create command returns the same logical run and no request thread performs long-running work.

**Exit gate:** UI can create/read a durable run through a typed API without bypassing state or evidence policy. Source: [FastAPI testing](https://fastapi.tiangolo.com/tutorial/testing/).

### Work Package 6: Deliver the one-node walking skeleton

**Files:**

- Create: `07_implementation/src/er_engine/model_gateway/{client,structured_output}.py`
- Create: `07_implementation/src/er_engine/router/{cache,model_router,tiers}.py`
- Create: `07_implementation/config/{model_tiers,p2_policy}.yaml`
- Create: `07_implementation/prompts/p2/digest.txt`
- Create: `07_implementation/src/er_engine/graph/{state,p2_graph}.py`
- Create: `07_implementation/src/er_engine/nodes/digest.py`
- Create: `07_implementation/tests/workflow/test_digest_walking_skeleton.py`

**Consumes:** typed input, API run, worker, checkpoints, trace, model tier contract.

**Produces:** API -> job -> digest -> checkpoint/trace -> API result path.

- [ ] Start with a deterministic model-gateway stub and test the complete path.
- [ ] Test malformed structured output, timeout/fallback, cost budget, restart, duplicate job, and replay.
- [ ] Add one configured real model adapter only after the stub path is green.
- [ ] Test exact-match cache key includes model tier, model/config/prompt versions, normalized input hash, and evidence snapshot; stale versions must miss.
- [ ] Persist model/config/prompt versions and citation IDs in the digest trace.

Run:

```bash
python3 -m pytest 07_implementation/tests/workflow/test_digest_walking_skeleton.py -q
```

Expected: one run survives API/worker restart, returns a typed cited digest, and creates one trace/artifact chain.

**Exit gate:** the simplest end-to-end product path works before adding five more nodes. Sources: [LangGraph persistence](https://docs.langchain.com/oss/python/langgraph/persistence), [Anthropic building effective agents](https://www.anthropic.com/engineering/building-effective-agents).

### Work Package 7: Implement retrieval and citation resolution

**Files:**

- Create: `07_implementation/src/er_engine/retrieval/{indexer,hybrid,repository}.py`
- Create: `07_implementation/tests/integration/test_retrieval_policy.py`
- Create: `07_implementation/tests/eval/test_retrieval_recall.py`

**Consumes:** verified source/passages and event cutoff.

**Produces:** `retrieve(query, company, cutoff, purpose, permitted_use, k) -> list[RetrievalDocument]` and citation resolver.

- [ ] Test hard filtering before ranking for company, PIT, permission, purpose, and verification status.
- [ ] Test claim-to-passage citation resolution.
- [ ] Build the golden retrieval query set from all three fixtures.
- [ ] Measure Recall@5 and record failures; do not add a reranker unless target misses are ranking-related.

Run:

```bash
python3 -m pytest 07_implementation/tests/integration/test_retrieval_policy.py 07_implementation/tests/eval/test_retrieval_recall.py -q
```

Expected: zero prohibited/future documents and Recall@5 at least 90% on the frozen golden set.

**Exit gate:** retrieval quality and evidence policy are measured independently of note quality. Sources: [PostgreSQL full-text search](https://www.postgresql.org/docs/current/textsearch.html), [pgvector](https://github.com/pgvector/pgvector).

### Work Package 8: Add deterministic model update, valuation, and forecast memory

**Files:**

- Modify: `07_implementation/src/er_engine/tools/quant.py`
- Create: `07_implementation/src/er_engine/nodes/{update_model,revalue_rating}.py`
- Create: `07_implementation/src/er_engine/memory/forecast_error.py`
- Create: `07_implementation/tests/unit/test_finance_tools.py`
- Create: `07_implementation/tests/integration/test_forecast_memory.py`
- Create: `07_implementation/tests/workflow/test_valuation_path.py`

**Consumes:** digest, estimates, peer/reference evidence, quant tools.

**Produces:** typed model update and valuation result with reference type/deviation, plus a PostgreSQL-backed forecast-error record keyed by ticker, period, metric, model/config version, and source IDs.

- [ ] Add tests for zero denominators, currency/unit mismatch, basis mismatch, missing peer/reference evidence, rating boundaries, and 15% gate boundary.
- [ ] Extend deterministic tools only for formulas defined in `equity_research_deep_dive.md`.
- [ ] Have nodes call tools and explain results; prohibit raw arithmetic by AST guard across `nodes/`, legacy `agents/` if it exists, and `pipeline.py`.
- [ ] Preserve single-house/manual labels; never render them as aggregate consensus.
- [ ] Test forecast memory separates metrics/bases, rejects future actuals, and never overwrites an earlier versioned record.

Run:

```bash
python3 -m pytest 07_implementation/tests/unit/test_finance_tools.py 07_implementation/tests/integration/test_forecast_memory.py 07_implementation/tests/workflow/test_valuation_path.py -q
```

Expected: deterministic outputs match fixtures and basis/reference errors block valuation.

**Exit gate:** every valuation number is reproducible from cited inputs and deterministic formulas.

### Work Package 9: Add valuation interrupt, edit, and idempotent resume

**Files:**

- Modify: `07_implementation/src/er_engine/graph/p2_graph.py`
- Create: `07_implementation/tests/workflow/test_valuation_gate.py`
- Modify: gate API/repositories from Packages 2 and 5

**Consumes:** valuation result, checkpoint, gate decision contract.

**Produces:** persistent valuation gate and resume to `draft_note`.

- [ ] Test below-threshold pass, above-threshold interrupt, request-more-evidence, edit/resume, reject, duplicate decision, stale checkpoint, and restart while paused.
- [ ] Ensure effects before `interrupt()` are idempotent.
- [ ] Persist original value, edited value, actor trust, comment, and decision time.
- [ ] Resume with the same thread/checkpoint identity and emit a new trace event.

Run:

```bash
python3 -m pytest 07_implementation/tests/workflow/test_valuation_gate.py -q
```

Expected: a rejected or stale decision never reaches drafting; duplicate resume creates no duplicate node/artifact.

**Exit gate:** G-01 behavior is executable and restart-safe. Source: [LangGraph interrupts](https://docs.langchain.com/oss/python/langgraph/interrupts).

### Work Package 10: Add cited draft, compliance gate, and private export

**Files:**

- Create: `07_implementation/src/er_engine/nodes/{draft_note,compliance,publish}.py`
- Create: `07_implementation/prompts/p2/{draft_note,compliance}.txt`
- Create: `07_implementation/tests/workflow/test_note_compliance_export.py`
- Modify: export API/repositories

**Consumes:** approved valuation, retrieved evidence, citation resolver, trace.

**Produces:** typed research note, checker results, compliance decision, immutable private artifact pointer.

- [ ] Test missing citation, unknown citation, future citation, unsupported claim, rejected compliance, duplicate export, and model timeout.
- [ ] Require 100% factual-claim citation coverage before compliance review.
- [ ] Require explicit human approval before export.
- [ ] Store an artifact checksum and reject a second logical artifact for the same idempotency key.

Run:

```bash
python3 -m pytest 07_implementation/tests/workflow/test_note_compliance_export.py -q
```

Expected: no rejection, missing citation, or future source can reach export; successful export remains private and trace-linked.

**Exit gate:** the six-node P2 workflow completes both allow and block branches without autonomous publishing. Sources: [OWASP Excessive Agency](https://owasp.org/www-project-top-10-for-large-language-model-applications/2_0_vulns/LLM06_ExcessiveAgency.html), [CFA Standard V(A)](https://www.cfainstitute.org/standards/professionals/code-ethics-standards/standards-of-practice-v-a).

### Work Package 11: Make all 20 eval cases executable

**Files:**

- Create: `07_implementation/src/er_engine/eval/{cases,evaluators,harness,rubric}.py`
- Create: `07_implementation/tests/eval/test_eval_harness.py`
- Create: versioned case records under `07_implementation/data/eval_cases/`
- Modify: `07_implementation/docs/eval_case_plan.md` status table as cases become runnable

**Consumes:** completed workflow, traces, fixtures, mutation builders, finance rubric.

**Produces:** per-case `EvalResult`, aggregate scorecard, failure taxonomy, and reproducible configuration pointer.

- [ ] Implement R-01 to R-08 as deployment-blocking assertions.
- [ ] Implement G-01 to G-04 as allow/block branch tests.
- [ ] Implement D-01 to D-03 as deterministic replay tests.
- [ ] Implement C-01 to C-05 as scored capability evaluations with human rubric records.
- [ ] Calibrate any LLM judge against finance labels; it cannot approve release.
- [ ] Record evaluator version, fixture version, prompt/config version, trace ID, artifact paths, failures, and reviewer decision.

Run:

```bash
python3 -m pytest 07_implementation/tests/eval/test_eval_harness.py -q
python3 -m er_engine.eval.harness --suite all --output 07_implementation/data/processed/eval_scorecard.json
```

Expected: regression/gate/replay cases are machine-runnable; capability cases produce a score plus review status rather than a fabricated automatic pass.

**Exit gate:** hard controls pass 100%, no critical failure is hidden by aggregate scoring, and quality results are reproducible. Sources: [LangSmith evaluation concepts](https://docs.langchain.com/langsmith/evaluation-concepts), [judge alignment](https://docs.langchain.com/langsmith/improve-judge-evaluator-feedback).

### Work Package 12: Build the Next.js analyst workbench

**Files:**

- Create/modify paths under `07_implementation/apps/web/` listed in §2.3
- Create: frontend unit/component tests beside components
- Create: `07_implementation/apps/web/e2e/analyst-workflow.spec.ts`

**Consumes:** OpenAPI contract, SSE events, gate/export commands.

**Produces:** five views: run setup, evidence review, valuation gate, note/compliance review, trace/eval/replay.

- [ ] Generate or manually maintain TypeScript types from the frozen API schema with a schema-drift test.
- [ ] Test loading/error/empty/reconnect/blocked/requires-human/succeeded states.
- [ ] Test SSE disconnect and polling fallback.
- [ ] Test actor warning remains visible: `Private demo - unauthenticated actor`.
- [ ] Test complete browser path for create -> gate -> edit/resume -> compliance -> export -> trace.

Run:

```bash
npm --prefix 07_implementation/apps/web run test
npm --prefix 07_implementation/apps/web run build
npm --prefix 07_implementation/apps/web run test:e2e
```

Expected: build passes and Playwright completes both approved and rejected workflows without UI-only state changes.

**Exit gate:** the UI is a faithful client of server contracts and can demonstrate the two human gates. Source: [Next.js testing](https://nextjs.org/docs/app/guides/testing).

### Work Package 13: Security, reliability, and private release proof

**Files:**

- Create: `07_implementation/docs/threat_model.md`
- Create: `07_implementation/docs/private_demo_runbook.md`
- Create: `07_implementation/docs/release_manifest_schema.md`
- Create: security/recovery/E2E tests under their matching test folders
- Modify: `08_presentation/README.md` only after verified artifacts exist

**Consumes:** complete product and eval scorecard.

**Produces:** threat/control evidence, clean-environment deployment proof, database restore proof, three-company replays, kill switches, rollback target, and known-limitations sheet.

- [ ] Test prompt injection in uploaded/retrieved text, prohibited tool/model route, secret leakage, oversized input, retry loop budget, and gate bypass.
- [ ] Test worker/model/export kill switches.
- [ ] Test clean Compose startup, database restore, and one full replay per company.
- [ ] Capture actual latency/cost/citation/gate metrics; do not reuse illustrative blueprint numbers.
- [ ] Freeze a replay pack and backup video only from a passing release candidate.

Run:

```bash
make test
make smoke-l0-l9
make eval
make e2e
make demo-replay
```

Expected: all hard gates pass, no critical open risk remains, and every presentation claim points to a verified artifact.

**Exit gate:** Private MVP Definition of Done in `professional_build_methodology.md` §18.3 passes. Sources: [NIST SSDF](https://csrc.nist.gov/projects/ssdf), [Google SRE canarying](https://sre.google/workbook/canarying-releases/).

---

## 5. Phase Crosswalk

This table prevents the roadmap, methodology, blueprint, and Step 7 packages from becoming four competing plans.

| Blueprint phase | Methodology phase | Work packages | Result |
|---|---|---:|---|
| 0 Data + deterministic smoke | C-D foundation/evidence | already present; preserved by 0 and 4 | verified baseline |
| 1 Runtime contract + setup | C Contract foundation | 0-3 | typed contracts, DB, jobs, trace |
| 2 Walking skeleton | E One-node skeleton | 4-6 | first recoverable product path |
| 3 Six nodes | F P2 slices | 6, 8-10 | complete workflow branches |
| 4 Quant runtime + L4 memory | F P2 slices | 8 | deterministic valuation and versioned forecast error |
| 5 Retrieval + reference | D/F/G | 7-8 | policy-filtered cited evidence |
| 6 Gate + Eval | F/G | 9-11 | human control and runnable eval |
| 7 Before/After | G/I | 11 and 13 | measured scorecard |
| 8 Demo polish | I Private release | 12-13 | workbench and replay pack |

The actual dependency order is the work-package order, not the numeric blueprint order. Retrieval precedes cited drafting; database/checkpoints precede gates; hard workflow tests precede capability scoring.

---

## 6. Test and Evaluation Matrix

| Layer | Tool/mode | Blocks package/release? | Owner | Required evidence |
|---|---|---:|---|---|
| Static/contract | Pydantic/OpenAPI/schema/AST assertions | yes | Engineering | test report + schema version |
| Unit | pytest/unittest deterministic functions and policy | yes | Engineering + Finance for expected values | inputs, expected values, source/formula ref |
| Integration | disposable PostgreSQL, API client, worker/model stubs | yes | Engineering | migration/log/trace output |
| Workflow | full state branches, restart, retry, interrupt/resume | yes | Engineering | trace and artifact IDs |
| Retrieval | policy assertions + Recall@5 | yes | Data/Engineering; Finance verifies evidence set | query set, ranked IDs, misses |
| Security | adversarial fixtures and gate-bypass tests | yes for Critical/High policy | Security/Engineering | finding and disposition |
| Regression | R-01..R-08 plus real failures | yes; 100% | Engineering | per-case result |
| Gate/safety | G-01..G-04 | yes; 100% | Finance/Compliance + Engineering | interrupt/decision/resume trace |
| Demo replay | D-01..D-03 | yes; 100% | Release owner | saved run/artifact/trace |
| Capability | C-01..C-05 | target, not single-case automatic release authority | Finance + second reviewer | rubric and disagreement record |
| LLM judge | optional calibrated evaluator | no independent authority | Eval owner | calibration against human labels |

Release targets remain those approved in `professional_build_methodology.md` §12 and `eval_case_plan.md` §9. Tests are deterministic deployment assertions; evaluation measures variable quality. Source: [LangSmith evaluation concepts](https://docs.langchain.com/langsmith/evaluation-concepts).

---

## 7. Eval Case-to-Package Readiness Map

| Cases | First runnable after | Blocking dependency |
|---|---:|---|
| R-01..R-06 | 4 | typed ingest and evidence policy |
| R-07 | 8 | AST guard expanded to all LLM-adjacent modules |
| R-08 | 8 | typed valuation tools |
| C-01..C-04 | 10 | complete cited note workflow + finance rubric |
| C-05 | 7 | frozen retrieval query/evidence set |
| G-01 | 9 | persistent valuation interrupt/resume |
| G-02..G-04 | 10 | compliance checker, decision, export policy |
| D-01..D-03 | 11 | complete backend workflow, harness, and saved replay; Package 12 adds browser E2E proof |

Until its dependency package passes, a case may be `specified` but may not be called `runnable` or counted as passing.

---

## 8. Risk Register Before Step 7

| ID | Severity | Risk/evidence | Required treatment | Owner | Gate |
|---|---|---|---|---|---|
| IR-01 | Critical | `requirements.txt` contradicts approved PostgreSQL/pgvector stack and omits product dependencies | Work Package 0 reconciles dependency authority before install | Tech lead | Step 7 start |
| IR-02 | Critical | blueprint §10 snippets use loose dicts, `MemorySaver`, hard-coded providers, and in-place state patterns that conflict with approved contracts | treat snippets as historical illustration; implement from this plan/contracts | Tech lead | Packages 1 and 6 |
| IR-03 | High | custom PostgreSQL worker can duplicate work under crash/concurrency | transaction claim, idempotency table, checkpoint/restart/concurrency tests | Backend | Package 3 |
| IR-04 | High | LangGraph resumes a node from its beginning, so pre-interrupt effects can repeat | isolate/idempotently upsert effects and test duplicate resume | Workflow | Package 9 |
| IR-05 | High | no authentication means reviewer identity is untrusted | local/private bind, visible warning, `actor_trust`, no enterprise claim | Product/Engineering | Packages 5, 12, 13 |
| IR-06 | High | provider-native aggregate consensus is absent for full production claim | use typed broker/manual reference labels; buy licensed export only if claim requires it | Finance/Data | Packages 4, 8, 13 |
| IR-07 | High | AMZN full Q&A transcript is not licensed | scope NLP claims to available official excerpts or obtain licensed transcript | Finance/Data | Packages 4, 13 |
| IR-08 | High | LLM output may be fluent but numerically or factually wrong | strict output, deterministic tools, citation checker, finance review | AI/Finance | Packages 6, 8, 10, 11 |
| IR-09 | Medium | SSE can disconnect during long runs | ordered event IDs plus polling fallback and reconnect tests | API/UI | Packages 5, 12 |
| IR-10 | Medium | illustrative before/after metrics may be mistaken for measured results | presentation consumes only release-candidate scorecard | Product/Eval | Packages 11, 13 |
| IR-11 | Medium | model tier/provider remains uncalibrated | stub first; benchmark approved tiers on capability/cost/latency before freeze | AI owner | Packages 6, 11 |
| IR-12 | Medium | thresholds 0.70 confidence and 15% deviation are project policies, not proven universal constants | keep versioned/configurable; finance calibrates and records rationale | Finance/Product | Packages 8, 11 |

Risk process follows Govern/Map/Measure/Manage and secure-development verification. Sources: [NIST AI RMF](https://airc.nist.gov/airmf-resources/airmf/5-sec-core/), [NIST SSDF](https://csrc.nist.gov/projects/ssdf).

---

## 9. Definition of Ready for Each Work Package

Before starting a package, all answers must be yes:

- [ ] Inputs and upstream exit gates are available.
- [ ] Exact files and interfaces are named in this plan.
- [ ] Positive, negative, retry/error, and trace expectations are listed.
- [ ] Finance expected values cite the governing formula/source.
- [ ] Data fixtures are versioned and permitted for the test purpose.
- [ ] No unresolved Critical risk affects the package.
- [ ] Verification command exists and has an observable expected result.
- [ ] The previous baseline remains runnable.

After a package, all answers must be yes:

- [ ] Named tests fail for the intended reason before implementation and pass afterward.
- [ ] `make test` still passes.
- [ ] Runtime behavior emits the required trace/source/citation IDs.
- [ ] Contract/docs are updated only where behavior genuinely changed.
- [ ] Any discovered failure is added to the regression or risk register.
- [ ] Exit-gate evidence is saved in a deterministic path.

---

## 10. Step 7 Entry Gate

**Readiness status:** 100% ready to start Step 7 at Work Package 0.

**Meaning of 100%:** the team may begin implementation from Work Package 0 with no remaining Critical planning ambiguity. The team may not skip dependency reconciliation, baseline verification, contracts, or persistence setup.

### Must Fix / accept before implementation begins

- [x] Team accepts the source-of-truth precedence in §2.1.
- [x] Team agrees Work Package 0 is the first Step 7 action; nobody installs `07_implementation/requirements.txt` as-is.
- [x] Team accepts the target implementation tree and server-side boundary rules.
- [x] Team accepts PostgreSQL durable state and the run/job state machines in §3.
- [x] Tech lead accepts SQLAlchemy 2 + psycopg 3 + Alembic for MVP persistence/migrations.
- [x] Team accepts that existing blueprint §10 code is illustrative and superseded where it conflicts with strict contracts, durable PostgreSQL, or provider-neutral routing.
- [x] Finance owner confirms existing fixture labels are sufficient for the MVP claims: aggregate consensus and full-call NLP are not claimed without licensed evidence.
- [x] Product owner accepts local/private no-auth language and no autonomous publishing.
- [x] Engineering accepts tests-first package gates and preservation of the 16-test baseline.
- [x] Team accepts manual Git control: the project owner runs all Git state-changing commands; AI only proposes and summarizes.

### Should Fix before the affected package

- [x] Freeze dependency authority in Work Package 0: root `pyproject.toml` for Python; `07_implementation/apps/web/package.json` for frontend.
- [x] Use Vitest + React Testing Library + Playwright for frontend unit/component/E2E proof.
- [x] Freeze model/data policy: provider-neutral LiteLLM tiers, no provider hard-coding, no fine-tuning, no real model call until data-egress policy is recorded in config.
- [x] Freeze threshold policy as configurable MVP defaults: confidence `< 0.70` or valuation deviation `> 15%` triggers human review; finance calibration is recorded when Package 8/11 produces evidence.
- [x] Decide licensed-data boundary for MVP: no provider-native aggregate consensus or full-call NLP claim unless licensed/manual evidence is added later.
- [ ] Assign named human owners for Product, Tech, Finance/Data, AI/Eval, Compliance/Security, and Release evidence.
- [ ] Freeze exact Python/Node package versions in Work Package 0.

### Can defer

- authentication/RBAC/SSO;
- managed queue, managed cloud, staging/production, and production SLO/on-call;
- reranker unless Recall@5 diagnosis proves it necessary;
- OCR and broad web scraping;
- fine-tuning, semantic cache, generic workflow loader, P1/P3-P7;
- provider-native aggregate consensus and full transcript only when the corresponding claim is removed from MVP.

**Entry decision:** Step 7 is approved to start at Work Package 0. Approval does not mean the product is runtime-ready; it means the implementation plan is unambiguous and controlled. Any deviation from Work Package 0-13 must update this plan before implementation continues.

---

## 11. Step 6 Sign-off Record

Record team acceptance here before Step 7:

| Role | Decision to record | Status |
|---|---|---|
| Product owner | scope, no-auth/private limitation, claim boundary | Accepted for Step 7 start |
| Tech lead | file map, interfaces, package order, dependency authority | Accepted for Step 7 start; exact package versions freeze in Work Package 0 |
| Finance/Data owner | formulas, evidence labels, ground truth, licensed-data claim boundary | Accepted for Step 7 start; no full aggregate-consensus/full-transcript claim without later evidence |
| AI/Eval owner | model gateway, evaluator modes, release metrics | Accepted for Step 7 start; model names benchmark before real model calls |
| Compliance/Security | gate/export, threat tests, residual-risk ownership | Accepted for Step 7 start; local/private no-auth boundary remains visible |
| Project owner | manual Git control | Accepted: owner runs Git state-changing commands |

Step 6 is complete. There is no unresolved Critical planning ambiguity blocking Step 7 Work Package 0.
