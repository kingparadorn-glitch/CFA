# ER P2 MVP — Developer Implementation Blueprint
### Walking skeleton: Earnings Update Cycle (P2) วิ่งครบ L0-L9 + before/after harness — build จริงในกรอบ hackathon

> **Scope:** build **P2 (Earnings Update) เส้นเดียว** วิ่ง end-to-end จริง · P1/P3-P7 = use case/vision (ไม่ build รอบนี้)
> **Spec source of truth:** schema + สูตร + workflow อยู่ใน `equity_research_deep_dive.md` (§4-10, §11, §18) และ engine design ใน `ai_architecture_design.md` (L0-L9) — ไฟล์นี้ = "แปลง spec → build" ไม่ inline ซ้ำ
> **Company universe locked for current smoke work:** MSFT + AMZN + PTT. Runtime design ยัง company-agnostic ได้ แต่ data/fixtures รอบนี้มี 3 บริษัทจริงใน `07_implementation/data/raw/`.
> **Step 7 execution order:** ใช้ `implementation_readiness_plan.md` เป็น canonical file map, interface/dependency order, test/eval plan, risk register และ entry gate. Phase 0-8 ใน §8 เป็น phase-level view; Work Package 0-13 ในแผน readiness เป็นลำดับลงมือจริง.

## 0. Current Build Status — 2026-07-17

ตอนนี้มี **deterministic L0-L9 I/O smoke harness** แล้ว เพื่อพิสูจน์ว่า fixtures และสูตรพื้นฐานวิ่งครบ contract ก่อนต่อ LangGraph/LLM runtime จริง:

| Area | Current artifact | Status |
|---|---|---|
| Fixtures | `07_implementation/data/raw/MSFT_FY26Q3_golden.json`, `AMZN_FY26Q1_golden.json`, `PTT_1Q2026_demo.json` | Ready for I/O + PIT/citation audit |
| Evidence pack | `02_sector_db/company_db/source_catalog.csv`, `processed/field_provenance_2026-07-17.csv` | Verified public/broker sources; licensed consensus gap explicit |
| Quant tools | `07_implementation/src/er_engine/tools/quant.py` | Implemented: surprise, expected return, consensus deviation, forecast error |
| Smoke pipeline | `07_implementation/src/er_engine/pipeline.py` | Implemented deterministic L0-L9 output |
| CLI | `07_implementation/src/er_engine/cli.py` | Implemented; writes `07_implementation/data/processed/l0_l9_smoke_summary.json` |
| Tests | `07_implementation/tests/test_l0_l9_io.py` | 16 unit/smoke/doc-contract tests including PIT and nested evidence regressions |
| Commands | `make test`, `make smoke-l0-l9` | Passing in current session |

**Still not implemented:** FastAPI/Next.js product surface, PostgreSQL schema/migrations and durable worker, LangGraph nodes, LLM calls, pgvector/full-text retrieval, memory tables, model router/cache, OTel-compatible runtime trace, human interrupt UI. MVP has no authentication and must remain local/private.

---

## 1. Purpose & Scope

**เป้า:** สร้างของที่ **วิ่งได้จริง** เพื่อ present "ความต่างใช้/ไม่ใช้ AI" เป็นตัวเลข (เร็วขึ้น · แม่นขึ้น · ปลอดภัยขึ้น) → ตอบเกณฑ์ a/b/c/d สูงสุด

**Build รอบนี้:** P2 Earnings Update — วน loop 1 บริษัท: งบประกาศ → digest+earnings-call NLP → update model → re-value+rating → earnings note → compliance gate → publish · วิ่งครบ 10 layer จริง

**ไม่ build (ขายเป็น use case/vision):** P1 Initiation (b ceiling สูงแต่ยาว), P3 Flash, P4 Thematic, P5 Maintenance, P6 Marketing, P7 Idea-gen — พูดว่า "engine เดียวกันเสียบ pipeline อื่นได้" (โชว์ generic)

**ทำไม P2:** คะแนน analytical 95/105 สูงสุด — before/after ชัดสุด (5.7hr→45min เป็น industry benchmark ที่ต้อง label), loop สั้นจบใน demo, วัดได้กับ typed dated reference + realized direction โดยไม่เคลม aggregate consensus ถ้าไม่มี licensed evidence, ครอบ layer เด่นครบ

---

## 2. Architecture → Module Map (L0-L9 → โค้ดจริง)

| Layer | Module (โค้ด) | Lib/Tech | MVP scope |
|---|---|---|---|
| L0 Ingestion | `ingest/` — loader + PIT tagger | pdfplumber (digital PDF), feedparser | **MVP:** ใช้ data digital (SET filing text, oppday deck, IAA) — **skip OCR** (→prod) |
| L1 Task Map | `graph/p2_graph.py` | LangGraph `StateGraph` | **MVP:** P2 hard-coded graph |
| L2 Orchestration | `nodes/` | LangGraph nodes + LiteLLM | **MVP:** 6 typed nodes + shared Verify/Fact-checker; do not split logic into `agents/` unless `implementation_readiness_plan.md` is amended first |
| L3 Human-Loop | LangGraph `interrupt()` + durable checkpoint | PostgreSQL-backed checkpoint/state | **MVP:** gate 2 จุด (deviation, compliance) + resume; no `MemorySaver` in runtime path |
| L4 Memory | `memory/forecast_error.py` | PostgreSQL | **MVP:** forecast-error store ง่าย (MAPE/bias ต่อ ticker) |
| L5 Retrieval | `retrieval/` — hybrid retrieval | PostgreSQL full-text + pgvector | **MVP:** corpus = official actuals + dated estimates + PIT peers + past notes; filter PIT/license/purpose ก่อน rank; reranker เมื่อ eval พิสูจน์ |
| L6 Observability | `obs/trace.py` + lineage | OTel-compatible PostgreSQL/JSON trace | **MVP:** trace ทุก node + number-lineage map; external exporter เป็น Enterprise option |
| L7 Governance+Eval | `eval/harness.py` | own harness | **MVP:** eval vs explicitly typed dated reference + post-event analyst target/rating + realized direction |
| L8 Schema Contract | `schemas/*.py` | Pydantic + LiteLLM structured output | **MVP:** ทุก handoff = Pydantic model, constrained decoding |
| L9 Routing+Caching | `router/model_router.py` | LiteLLM + cache | **MVP:** cost-tier route + exact-match cache |

**โครง repo (MVP):**
```
07_implementation/
├── src/er_engine/
│   ├── pipeline.py       # CURRENT: deterministic L0-L9 smoke harness
│   ├── cli.py            # CURRENT: writes smoke summary JSON
│   ├── tools/quant.py    # CURRENT: quant helpers; later expands to full tool registry
│   ├── ingest/           # NEXT: L0 parser/PIT loader
│   ├── graph/p2_graph.py # NEXT: L1 + L2 LangGraph orchestration
│   ├── nodes/            # NEXT: L2 typed node ต่อ stage; runtime orchestration lives here
│   ├── schemas/          # NEXT: L8 Pydantic handoff objects
│   ├── retrieval/        # NEXT: L5
│   ├── memory/           # NEXT: L4
│   ├── router/           # NEXT: L9
│   ├── obs/              # NEXT: L6
│   ├── eval/harness.py   # NEXT: L7 + before/after
│   └── run_p2.py         # NEXT: full runtime entrypoint
├── tests/                # CURRENT: unittest regression suite
└── data/                 # CURRENT: raw fixtures + processed smoke output
```

---

## 3. Tech Stack (concrete + model swappable)

| ชั้น | เลือกใช้ | เหตุผล | swap ได้ไหม |
|---|---|---|---|
| Model gateway | **LiteLLM** (หรือ OpenRouter) | เปลี่ยน model ข้าม provider ด้วย config เดียว | — (คือตัว abstraction) |
| Orchestration | **LangGraph** | interrupt=L3 gate ตรงตัว, checkpoint=incremental re-run, state ฟรี | ✅ (own loop ได้) |
| Schema | **Pydantic v2** | structured output + validation = L8 | ✅ |
| Product UI/API | **React/Next.js + FastAPI** | analyst workbench + typed REST/SSE contract | ✅ |
| State/jobs | **PostgreSQL + durable worker** | run/checkpoint/gate/eval/audit source of truth | ✅ |
| Retrieval | **PostgreSQL full-text + pgvector** | hybrid retrieval ในฐานเดียว; rerankerเพิ่มเมื่อ eval จำเป็น | ✅ |
| Trace | **OTel-compatible PostgreSQL/JSON trace** | local trace+lineage source of truth; exporter optional | ✅ |
| Quant | **Python** (numpy/pandas) | คำนวณใน code ไม่ให้ LLM เดา | — |

### Cost-tiered model routing (L9) — **model แพงเฉพาะที่จำเป็น**
| งาน (stage) | tier | ตัวอย่าง model (ถูก→แรง) | เหตุผล |
|---|---|---|---|
| extract/digest, screen, format | **cheap** | Gemini Flash / GPT-mini / DeepSeek-V3 / Qwen / Claude Haiku | งาน mechanical ปริมาณมาก |
| transcript NLP (extract facts) | **mid** | DeepSeek / Sonnet / GPT | ต้องเข้าใจ nuance แต่ไม่ตัดสินใจ |
| rating/thesis/valuation judgment | **strong** | Sonnet/Opus / GPT / DeepSeek-R1 | ตัดสินใจสำคัญ ผูก compliance |
> บังคับแค่: model ต้องรองรับ **structured output/tool-use** (ทุกเจ้าหลักมีแล้ว) · default config เปลี่ยนที่ `router/model_router.py` ที่เดียว

---

## 4. Agent-Loop Runtime Spec (หัวใจ — professional agent-loop engineering)

### 4.1 State object (ผ่านทุก node — L3 state)
```python
# schemas/state.py
from pydantic import BaseModel
from typing import Optional

class P2State(BaseModel):
    ticker: str
    # stage outputs (L8-validated handoffs)
    digest: Optional[dict] = None          # surprise + management_cues
    updated_model: Optional[dict] = None
    valuation: Optional[dict] = None        # target, rating, consensus_deviation
    note: Optional[dict] = None
    approved: bool = False
    # control
    confidence: float = 1.0                 # จาก self-consistency (L2)
    gate_reason: Optional[str] = None       # ทำไมต้องให้คนดู
    override_log: list = []                 # L7 audit → L4 learning
    trace_id: Optional[str] = None          # L6
```

**Runtime schema lock ก่อน Step 3:** skeleton จริงต้องเปลี่ยน `dict` กว้างๆ ข้างบนให้เป็น typed Pydantic objects ตั้งแต่ Phase 1: `SourceRef`, `Citation`, `SurpriseMetric{actual, estimate, unit, basis, actual_source_id, estimate_source_id}`, `ValuationReference`, `ValuationResult`, `ResearchNote`. ทุก object ที่เป็น factual claim ต้องมี `source_id` และ `purpose` เพื่อให้ citation renderer + PIT audit ทำงานได้ตั้งแต่ runtime ไม่ใช่แค่ใน fixture.

### 4.2 Loop diagram (P2)
```
                 ┌─────────────────────────────────────────────┐
INGEST(L0) ─► [digest] ─► [update_model] ─► [revalue_rating] ─┤
 PIT tag        │            │                   │             │
                ▼            ▼                   ▼             │
             (L8 schema enforce ทุก handoff · L6 trace ทุก node)│
                                                 │             │
                          confidence<θ  OR  consensus_dev>15%  │
                                                 │ yes         │
                                                 ▼             │
                                      ┌──► [GATE: interrupt(L3)] ──human แก้──┐
                                      │         │ resume (checkpoint)          │
                                      │         ▼                              │
                                      └── [draft_note] ─► [COMPLIANCE GATE(L3 บังคับ)] ─► [publish]
                                                                │ human sign-off
                          override → L7 audit → L4 forecast-error memory ◄─────┘
```

### 4.3 หลักการ loop (ต่อ concept → layer)
- **node = stage** (L2) · **edge = control flow** (L1 task graph)
- **conditional edge**: `confidence < θ` หรือ `consensus_deviation > 0.15` → route ไป **interrupt** (L3 auto-gate) · ไม่งั้นเดินต่อ
- **interrupt() = human gate** (L3) — LangGraph หยุด, คนแก้ state, `resume` เดินต่อจาก checkpoint (= incremental re-run, ไม่รันซ้ำ stage ที่ผ่าน)
- **compliance gate = interrupt บังคับ** ก่อน publish (MiFID/IAA — ห้าม auto)
- **self-consistency** (L2): rating/valuation node sample N ครั้ง → วัด disagreement → set `confidence`
- **ทุก handoff ผ่าน Pydantic** (L8) — node คืน model ผิด schema = fail ทันที ไม่ไหลต่อเงียบ
- **ทุก node emit trace** (L6) + number-lineage
- **override เก็บ L7** → feed `memory/forecast_error` (L4)

---

## 5. P2 Build — Node-by-Node (6 stage)

> I/O schema + สูตรเต็มอยู่ `equity_research_deep_dive.md` §5(b)(c) + §18 — ตารางนี้ = build mapping

| Node | Agent | Input model | Output model | Tool (quant) | Model tier | Gate condition |
|---|---|---|---|---|---|---|
| 1 `digest` | Digest + Transcript-NLP (ขนาน) | `EarningsInput` | `DigestResult{surprise, cues[], guidance}` | `surprise_fn`, `transcript_nlp` | mid (NLP), cheap (surprise) | flag `if |eps_surprise|>0.10` |
| 2 `update_model` | Model + Verify | `DigestResult`+`ThreeStatementModel` | `ThreeStatementModel{ties}` | `three_statement_engine` | cheap | `if not ties → re-run` |
| 3 `revalue_rating` | Valuation + Rating | `ThreeStatementModel`+peers+consensus | `ValuationResult{tp,rating,consensus_deviation}` | `comps_engine`,`dcf_engine`,`rating_fn`,`consensus_dev_fn` | **strong** | **`if dev>0.15 → GATE`** + self-consistency confidence |
| 4 `draft_note` | Note + Fact-checker | `ValuationResult`+cues | `ResearchNote{citations}` | — | mid | grounding: ทุก claim ต้องมี citation |
| 5 `compliance` | Compliance pre-check → **human** | `ResearchNote` | `{approved, reviewer_id}` | — | strong (pre) | **GATE บังคับ (interrupt)** |
| 6 `publish` | Publish | approved note | `{published_url, ts}` | — | cheap | — |

---

## 6. Layer Implementation L0-L9 (MVP / stub / production)

**Scope lock:** ตารางนี้แยกสิ่งที่จะ build ใน hackathon ออกจาก production extension อย่างตั้งใจ. Layer 3 build ต้องทำเฉพาะคอลัมน์ **MVP** ให้รัน end-to-end ได้ก่อน; คอลัมน์ **Stub** คือทางลัดที่ยอมรับได้ใน demo; คอลัมน์ **Production extension** ใช้เล่า roadmap/feasibility ห้ามกลายเป็น promise ของรอบ build นี้.

| Layer | MVP (build เลย) | Stub (ทำง่าย) | Production extension |
|---|---|---|---|
| L0 | loader งบ/oppday/IAA (digital text) + PIT tag | — | **OCR** งบสแกน (layout-preserving), audio→transcript diarize |
| L1 | P2 graph hard-coded | — | generic graph loader (P1-P7) |
| L2 | 6 node + shared Verify/Fact-checker | best-of-N (ทำ 1 node) | ครบทุก pipeline |
| L3 | 2 gate (deviation + compliance) + resume | — | uncertainty routing เต็ม, abstain |
| L4 | forecast-error store (PostgreSQL) | preference memory | RLTHF active-learning จาก override |
| L5 | PostgreSQL FTS+pgvector + PIT/license/purpose filter | — | full corpus entitlements/ACL; rerankerเมื่อ eval จำเป็น |
| L6 | local OTel-compatible trace + lineage หลัก | external exporter | number-lineage ครบทุก cell + production alerting |
| L7 | eval harness vs typed dated reference + realized direction | — | provider-native aggregate consensus, drift monitor, LLM-as-judge, gold-set ใหญ่ |
| L8 | Pydantic ทุก handoff + structured output | — | constrained decoding เต็ม provider |
| L9 | cost-tier route + exact cache | — | semantic cache, cascade escalation |

**Honest note ตอน present:** โชว์ว่า MVP รันจริงครบ 10 layer (แม้บาง layer ยังตื้น) + roadmap production ชัด — ไม่เคลมว่า production-ready. สิ่งที่ต้อง label เป็น production extension เสมอ: OCR เต็มรูปแบบ, generic graph loader, active learning/RLTHF, semantic cache/cascade, full gold-set/drift monitoring, number-lineage ระดับ cell ครบทุกจุด.

---

## 7. Before/After Harness (หัวใจ present "ความต่าง")

### 4 metric (วัดจริง)
| Metric | Before (ไม่ใช้ AI) | After (engine) | วิธีวัด |
|---|---|---|---|
| **เวลา/บริษัท** | ~5.7 ชม. (Marvin Labs benchmark — label ชัดว่า industry est.) | engine wall-clock จริง (นาที) | จับเวลา `run_p2.py` end-to-end |
| **ความแม่น (rating/target)** | — | AI target vs **IAA consensus** + **ทิศราคาจริงหลังงบ** | `eval/harness.py`: |AI_tp−iaa_tp|/iaa_tp + sign(price move) |
| **Grounding** | — | % claim ที่มี citation-by-ID | นับ citation/claim ใน note |
| **Error-caught** | (คนต้องจับเอง) | gate จับ deviation/hallucination กี่ครั้ง | นับ interrupt เหตุ deviation>15% + fact-check fail |

### Output สำหรับสไลด์

> **Placeholder only until Work Package 11/13:** ตัวเลขด้านล่างเป็น shape ตัวอย่างของ output ไม่ใช่ measured product claim. ค่า speedup, time, consensus/reference deviation, citation coverage และ errors-caught ต้องมาจาก eval harness/release scorecard จริงก่อนใช้ในสไลด์.

```python
# eval/harness.py -> returns after Work Package 11/13
{ "time_min": "<measured>",
  "baseline_hr": 5.7,
  "speedup": "<measured>",
  "tp_vs_reference_pct": "<measured>",
  "direction_correct": "<measured>",
  "grounding_pct": "<measured>",
  "errors_caught": "<measured>" }
```
→ ตาราง/กราฟ before vs after บนสไลด์ต้องใช้ค่าที่วัดจริงเท่านั้น; ถ้าใช้ broker/manual reference ต้อง label ว่าไม่ใช่ provider-native aggregate consensus.

---

## 8. Build Phases (step-by-step + Definition of Done)

> **Execution note:** phase number ไม่ได้แปลว่าทุกงานใน phase ทำแบบเส้นตรง. ใช้ crosswalk ใน `implementation_readiness_plan.md` §5 เพื่อให้ PostgreSQL/contracts มาก่อน worker/gate, retrieval มาก่อน cited drafting และ hard tests มาก่อน capability eval.

| Phase | ทำอะไร | DoD (เสร็จเมื่อ) |
|---|---|---|
| **0 Data + deterministic smoke** | fixtures, quant helpers, deterministic L0-L9 harness | ✅ `make test` + `make smoke-l0-l9` ผ่าน; 3 fixtures มี L0-L9 summary |
| **1 Runtime contract + setup** | สร้าง typed domain/API schema, PostgreSQL schema/migrations, job/checkpoint protocol, trace/eval contracts, LiteLLM tier config | contract docs ตรง Step 3/5; migration และ state/idempotency contract tests ผ่าน; ยังไม่ผูก provider เดียว |
| **2 Walking skeleton** | Next.js → FastAPI → durable worker → 1 `digest` node → PostgreSQL checkpoint/trace → UI | คืน `run_id`, digest typed object valid, restart/retry/resume ได้โดยไม่สร้าง duplicate; trace conform `json_trace_schema.md` |
| **3 ครบ 6 node** | ต่อ node 2-6 + edge + state | รัน P2 end-to-end คืน `ResearchNote` (ยังไม่มี gate/retrieval เต็ม) |
| **4 Quant tools in runtime** | ใช้ `tools/quant.py` ใน valuation node + เพิ่ม comps/rating wrappers | valuation node ใช้ tool จริง เลขตรง (ไม่ให้ LLM เดา) |
| **5 Retrieval + typed reference** | PostgreSQL FTS+pgvector + PIT/license/purpose filter + ดึง aggregate consensus หรือ broker/manual reference ตามชนิดหลักฐานจริงจาก processed corpus | Recall@5 ผ่าน target, rating มี typed reference/deviation + claim-level citation; limitation label preserved และไม่เรียก single-house/manual ว่า aggregate consensus |
| **6 Gate + Eval** | interrupt 2 จุด + resume + `eval/harness.py` | คนแก้ที่ gate แล้ว resume ได้ + eval คืน metric |
| **7 Before/After** | harness ครบ 4 metric + baseline | ได้ตาราง before/after เป็นตัวเลขจริง |
| **8 Demo polish** | script + trace UI + สไลด์ + backup video | รัน demo จบใน X นาที + video สำรอง |

---

## 9. Demo Script + Score Hooks

| ช่วง demo | โชว์อะไร live | ผูกเกณฑ์ | คำพูด |
|---|---|---|---|
| เปิด | ปัญหา ER ไทย (coverage 50-60 หุ้น, earnings season, IAA) | **a** | "analyst ไทยจมงานซ้ำ ตอน earnings season" |
| รัน engine | `run_p2.py <TICKER>` — เห็น loop เดินทีละ node (trace live) | **b** | "engine เดิน 6 ขั้น แต่ละขั้น agent+quant จริง" |
| Gate moment | consensus_deviation>15% → หยุด ให้คนแก้ → resume | **c** | "AI ไม่มั่ว — ต่างจาก street เกิน 15% มันหยุดถามคน (MiFID/IAA)" |
| Lineage | คลิกตัวเลขใน note → ย้อนถึง cell งบ/บรรทัด transcript | **c** | "ทุกตัวเลข defend ได้ ต่อ compliance" |
| Before/After | ตาราง measured scorecard: baseline 5.7hr industry estimate เทียบ engine wall-clock จริง, reference deviation, citation coverage, gate events | **d** | "เราวัดความเร็ว ความใกล้ reference และ safety gate จาก replay/eval จริง; ถ้าเป็น broker/manual reference จะ label limitation ชัดเจน" |
| ปิด | "engine เดียวเสียบ P1/P3-P7 ได้" (use case) | **b** | "generic — ขยายทุก workflow ER + สายอื่น" |

---

## 10. Historical Code Sketches (intent only)

> **Historical illustration only:** snippets ใน §10 แสดง intent ของ P2 flow แต่ไม่ใช่ runtime contract ปัจจุบัน. ห้ามคัดลอกส่วนที่ใช้ loose `dict`, `MemorySaver`, hard-coded provider/model, in-place state mutation หรือ provider-specific config เข้า production path. Implementation ปัจจุบันต้องใช้ strict schemas ใน `runtime_schema_contract.md`, durable PostgreSQL/checkpoints, provider-neutral tier config และ file/interfaces ใน `implementation_readiness_plan.md`.
>
> **Runtime warning:** Work Package 6 ต้อง implement graph จาก `implementation_readiness_plan.md` + `runtime_schema_contract.md` เท่านั้น. โค้ดตัวอย่างใน §10.4 ที่ใช้ `MemorySaver` เป็น anti-pattern สำหรับ MVP runtime และมีไว้เตือนสิ่งที่ห้าม copy.

### 10.1 Pydantic schemas (L8 — จาก spec §18.1)
```python
# schemas/p2.py
from pydantic import BaseModel, Field
from typing import Literal, Optional

class EarningsInput(BaseModel):
    ticker: str
    actuals: dict            # {revenue, eps, nim?}
    prior_estimates: dict    # {revenue, eps}
    transcript_segments: list # [{speaker, role, text, timestamp}]
    pub_date: str            # PIT

class DigestResult(BaseModel):
    surprise: dict           # {revenue_pct, eps_pct}
    management_cues: list
    guidance_change: dict

class ValuationResult(BaseModel):
    ticker: str
    price_target: float
    rating: Literal["Buy","Hold","Sell"]
    comps_tp: float
    dcf_tp: float
    expected_return: float
    consensus_deviation: float
    citations: list = []
```

### 10.2 Quant tool (L2 binding — สูตร §18.2, คำนวณใน code)
```python
# tools/quant.py
import numpy as np

def comps_engine(fwd_eps: float, peer_pe: list[float]) -> float:
    return fwd_eps * float(np.median(peer_pe))          # TP = fwd_EPS × median(peer P/E)

def rating_fn(exp_return: float) -> str:
    if exp_return > 0.15: return "Buy"
    if exp_return < -0.10: return "Sell"
    return "Hold"

def consensus_dev_fn(tp: float, iaa_tp: float) -> float:
    return abs(tp - iaa_tp) / iaa_tp                     # >0.15 → gate
```

### 10.3 Model router (L9 — cost-tier, swappable)
```python
# router/model_router.py — เปลี่ยน model ที่เดียว
import litellm
TIER = {
    "cheap":  "gemini/gemini-2.0-flash",     # extract/digest — swap ได้
    "mid":    "deepseek/deepseek-chat",       # NLP
    "strong": "anthropic/claude-sonnet",      # rating/thesis (swap ↔ gpt/deepseek-r1)
}
def call(tier: str, messages: list, schema=None):
    return litellm.completion(model=TIER[tier], messages=messages,
                              response_format=schema)     # structured output = L8
```

### 10.4 Historical LangGraph P2 graph sketch (do not copy)
```python
# graph/p2_graph.py
from langgraph.graph import StateGraph, END
from langgraph.checkpoint.memory import MemorySaver
from schemas.state import P2State

def build_p2():
    g = StateGraph(P2State)
    g.add_node("digest", digest_node)
    g.add_node("update_model", update_model_node)
    g.add_node("revalue_rating", revalue_node)
    g.add_node("valuation_gate", valuation_gate_node)  # interrupt ข้างใน; resume กลับไป draft
    g.add_node("draft_note", draft_node)
    g.add_node("compliance", compliance_node)   # interrupt ข้างใน
    g.add_node("publish", publish_node)

    g.set_entry_point("digest")
    g.add_edge("digest", "update_model")
    g.add_edge("update_model", "revalue_rating")
    # conditional: deviation/confidence → gate ก่อนไป draft
    g.add_conditional_edges("revalue_rating", route_after_valuation,
                            {"gate": "valuation_gate", "ok": "draft_note"})
    g.add_edge("valuation_gate", "draft_note")
    g.add_edge("draft_note", "compliance")
    g.add_edge("compliance", "publish")
    g.add_edge("publish", END)
    # checkpoint = incremental re-run + resume หลัง human gate
    return g.compile(checkpointer=MemorySaver(),
                     interrupt_before=["compliance"])     # L3 hard gate

def route_after_valuation(state: P2State) -> str:
    if state.confidence < 0.7 or state.valuation["consensus_deviation"] > 0.15:
        state.gate_reason = "deviation/confidence"
        return "gate"
    return "ok"
```

### 10.5 Agent node (L2 — Digest ตัวอย่างเต็ม)
```python
# nodes/digest.py
from router.model_router import call
from tools.quant import surprise
from schemas.p2 import DigestResult

def digest_node(state):
    # 1. quant (code จริง ไม่ให้ LLM เดา)
    surprise_result = {"eps_pct": surprise(state.actuals["eps"], state.prior["eps"])}
    # 2. LLM extract facts จาก transcript (mid tier)
    cues = call("mid", [{"role":"user","content": build_prompt(state.transcript_segments)}],
                schema=DigestResult)
    result = DigestResult(surprise=surprise_result, management_cues=cues.cues,
                          guidance_change=cues.guidance)
    # 3. flag material
    if abs(surprise_result["eps_pct"]) > 0.10:
        state.gate_reason = "material_surprise"
    state.digest = result.model_dump()   # L8 validated handoff
    emit_trace(state, "digest", result)  # L6
    return state
```

---

## 11. Risks / Backup

| Risk | Backup |
|---|---|
| Live demo พัง (network/model timeout) | **อัดวิดีโอ run จริงไว้ล่วงหน้า** + screenshot trace/before-after |
| Data source ชั่วคราวเข้าไม่ได้ | ใช้ verified replay จาก MSFT/AMZN/PTT golden fixtures + saved source evidence pack; ห้ามใช้ synthetic/hardcode เป็นหลักฐานจริง |
| Model cost บาน | default cheap tier + cache; strong tier เฉพาะ rating node |
| IAA/provider consensus เข้าถึงยาก | ใช้ verified manual snapshot / broker-backed reference ที่มี source ID และ label ว่าไม่ใช่ production feed |
| LangGraph learning curve | fallback ชั่วคราว: plain Python loop ที่ยังรับ/คืน strict Pydantic state และเขียน PostgreSQL checkpoint/trace; ห้ามลด contract กลับเป็น loose `dict` |

---

## 12. Gaps (ต้องเคาะ/หาต่อ)
- **company universe เคาะแล้ว** — MSFT + AMZN + PTT เป็น current smoke/demo fixtures; runtime ต้อง company-agnostic แต่ไม่ต้องวนกลับไปหา proxy ticker ใหม่
- **licensed/provider-native consensus history** — public pack พอสำหรับ demo แต่ถ้าจะเคลม production consensus feed ต้องใช้ FactSet/Bloomberg/Visible Alpha/LSEG/SETSMART หรือ manual licensed export
- **model tier tuning** — ทดสอบจริงว่า cheap model พอไหมสำหรับ digest/NLP (อาจต้องขยับ mid)
- **θ confidence threshold** (0.7) + **deviation 15%** — ปรับจากการทดลองจริง
- **AMZN full Q&A transcript** — official release/slides พอสำหรับ numeric demo; deep tone/Q&A NLP ต้อง licensed transcript หรือ manual transcript จาก official replay
- **runtime-readiness ก่อน Step 7** — file map, typed schema, API/DB/job/gate contract, JSON trace, test/eval dependency map และ risk entry gate ถูกจัดไว้ใน `implementation_readiness_plan.md`; Step 6 sign-off ผ่านแล้ว และ implementation เริ่ม Work Package 0 เท่านั้น

---

## Sources (external — web only)
- Marvin Labs earnings-season (5.7hr→45min baseline) — https://www.marvin-labs.com/solutions/earnings-season/
- IAA Consensus (SETTRADE) — https://www.settrade.com/th/research/iaa-consensus/main
- LangGraph (interrupt/checkpoint = human-in-loop) — https://langchain-ai.github.io/langgraph/
- LiteLLM (model gateway) — https://docs.litellm.ai/
- Look-ahead bias / PIT — https://www.pfolio.io/academy/look-ahead-bias
