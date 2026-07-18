# Build Roadmap — ลำดับงานจริงจาก pre-build → present (วิเคราะห์+จัดลำดับ 9 ขั้นที่ทีมเสนอ)

> ต่อยอดจาก `er_p2_mvp_dev_blueprint.md` (มี build phases 0-8 อยู่แล้ว) — ไฟล์นี้เติม**ช่วงก่อน**และ**หลัง**ที่ blueprint เดิมไม่ครอบ (confirm/data/risk-audit/test-tooling/iteration)

## สรุปการจัดลำดับใหม่ (จาก 9 ข้อที่ทีมเสนอ)

ลำดับที่ทีมให้มาเกือบถูกแล้ว แต่มี **dependency ผิดที่ 2 จุด**: (1) "หาจุดอ่อน" (ข้อ 2) ต้องทำ**หลัง** connect เอกสาร (ข้อ 1) แต่**ก่อน** confirm (ข้อ 3) — เพราะจุดอ่อนที่เจอต้องเอาไปเป็น input ตอน confirm ไม่ใช่ confirm ไปแล้วค่อยเจอปัญหา (2) "ได้ข้อมูล company" (ข้อ 4) ต้องมาก่อนหรือพร้อมกับ confirm scope (ข้อ 3) เพราะ scope ขึ้นกับข้อมูลที่หาได้จริง — ถ้า confirm scope ก่อนแล้วข้อมูลไม่มี ต้องรื้อ

**ลำดับที่แก้แล้ว:**
```
1 เชื่อมเอกสาร (เข้าใจร่วมกัน)
     │
2 Risk/gap audit (หาจุดอ่อนจากเอกสารที่มี — cited)
     │
3+4 Confirm scope/stack/loop  ⟷  หาข้อมูล company (ทำคู่ขนาน วนกลับแก้กันได้)
     │
5 Research best-practice การสร้าง product จริง (cited)
     │
6 วิเคราะห์แผน + เลือกเครื่องมือทดสอบ + risk ก่อน implement (cited)
     │
7 Follow the plan (build จริง — ตาม er_p2_mvp_dev_blueprint.md phase 0-8)
     │
8 ทดสอบให้ครอบคลุมสำหรับ present
     │
9 Loop หา error → แก้ → พัฒนา (ต่อเนื่องจนวันพรีเซนต์)
```

---

## ขั้น 1 — เชื่อมต่อ DB + Architecture + Blueprint ให้เข้าใจร่วมกัน

**ทำอะไร:** ทีม tech ทุกคนอ่าน 3 ไฟล์ตามลำดับ (`01_decision_and_design/ai_architecture_design.md` → `02_sector_db/equity_research_deep_dive.md` → `03_dev_blueprint/er_p2_mvp_dev_blueprint.md`) แล้วทำ **cross-check matrix**: ทุก layer (L0-L9) ใน architecture ต้องมี mechanism ตรงกันใน ER deep-dive §14 และมี module ตรงกันใน blueprint §2 — ถ้า layer ไหนไม่ตรงกัน 3 ไฟล์ = จุดที่ต้องเคลียร์ก่อนไปต่อ

**Output:** checklist "L0-L9 × 3 ไฟล์ ตรงกันไหม" (ถ้าทำแล้วพบว่าตรงกันหมด = ผ่านขั้นนี้)

### Step 1 Execution — L0-L9 Cross-Check Matrix

**วันที่ทำ:** 2026-07-17  
**ไฟล์ที่ตรวจ:** `01_decision_and_design/ai_architecture_design.md`, `02_sector_db/equity_research_deep_dive.md`, `03_dev_blueprint/er_p2_mvp_dev_blueprint.md`  
**Scope ที่ใช้เป็นตัวตั้ง:** build รอบนี้ = **Equity Research P2 Earnings Update เส้นเดียว**; P1/P3-P7 = expansion story ไม่ใช่ build scope

| Layer | Architecture mechanism | ER deep-dive mechanism | MVP blueprint module | Step 1 status | ต้องส่งต่อ Step 2 |
|---|---|---|---|---|---|
| **L0 Ingestion** | OCR + table extract + normalization; confidence flag ส่ง L3 ถ้าอ่านเอกสารเสี่ยง | P2 ต้อง ingest earnings release + audio/transcript, diarize/timestamp, PIT tag | `ingest/` loader + PIT tagger; MVP ใช้ digital text/oppday/IAA และ **skip OCR** | **Partial alignment** | Architecture ขาย OCR หนัก แต่ MVP skip OCR; ต้อง label ให้ชัดว่า OCR = production extension ไม่ใช่ demo promise |
| **L1 Task Map** | finance plug นิยาม workflow steps แล้ว engine อ่านเป็น task map | P2 spec = 6 ขั้น: digest, update model, revalue/rating, draft note, compliance, publish | `graph/p2_graph.py` hard-coded P2 `StateGraph` | **Aligned** | ต้อง freeze narrative ว่า build = P2 hard-coded graph ไม่ใช่ generic graph loader |
| **L2 Orchestration** | agent + quant + debate/self-consistency/best-of-N/reflection | Digest+NLP ขนาน, model update, valuation/rating, note/fact-check, compliance pre-check | `nodes/`, LiteLLM, 6-node runtime, shared Verify/Fact-checker | **Aligned with MVP narrowing** | self-consistency/best-of-N ยังไม่ใช่ทุก node; runtime orchestration อยู่ใน `nodes/` ตาม readiness plan |
| **L3 Human-Loop + State** | gate + human edit + state + incremental rerun; confidence routing | gate เมื่อ material surprise/deviation สูง และ compliance sign-off บังคับ | LangGraph `interrupt()` + checkpoint; gate 2 จุด: deviation + compliance | **Aligned** | ต้องนิยาม demo reviewer role และ state fields ที่คนแก้ได้จริง |
| **L4 Memory** | จำข้ามดีล/รอบ + active learning จาก human override | forecast-error memory ต่อ ticker: MAPE/bias, analyst preference, past note | `memory/forecast_error.py` PostgreSQL store | **Partial alignment** | ใน demo รอบเดียว memory เห็นผลยาก; ต้องขายเป็น lightweight store/vision ไม่ใช่ core proof |
| **L5 Guardrail + Retrieval** | input/output/retrieval rails, hybrid search, citation-by-ID | PIT retrieval, IAA consensus, peer/price/past notes, citation-by-ID | `retrieval/` PostgreSQL full-text + pgvector; reranker เมื่อ eval จำเป็น | **Aligned but data-dependent** | provider-native aggregate consensus ยังเป็น data-access risk; corpus ต้องผ่าน PIT/license/provenance |
| **L6 Observability** | trace ทุก step + data/number lineage | trace + lineage ทุกเลขใน note ย้อนถึง cell/transcript | `obs/trace.py`, OTel-compatible PostgreSQL/JSON | **Aligned** | local PostgreSQL/JSON เป็น source of truth; external exporter เป็น optional Enterprise adapter |
| **L7 Governance + Eval** | model inventory, validation record, monitoring, override audit, eval harness | TP/rating เทียบ typed reference + realized price, audit, gold-set eval | `eval/harness.py`, before/after metrics vs typed reference + realized | **Resolved into Step 6/7 plan** | threshold policy, regression/capability split, and 20-case spec are locked; runnable harness is Work Package 11 |
| **L8 Schema Contract** | JSON schema/constrained decoding ทุก handoff | ER handoff schema + master schema/tool registry | `schemas/*.py`, Pydantic v2, LiteLLM structured output | **Aligned** | สูตร `consensus_dev_fn` ถูกเติมแล้ว; Step 2 ต้องตรวจต่อว่า quant tests ครอบคลุมสูตรนี้ |
| **L9 Routing + Caching** | route/cascade model ตามงาน + cache | digest/model-update ใช้ model เล็ก, rating/thesis ใช้ model ใหญ่, cache earnings ซ้ำ | `router/model_router.py`, LiteLLM, exact-match cache | **Aligned for MVP** | semantic cache/cascade = production; MVP ควรเริ่ม exact cache + tier config เดียว |

### Step 1 Review Verdict

**ผ่านแบบมีเงื่อนไข (conditional pass).** ทั้ง 10 layer มี mapping ครบระหว่าง architecture → ER deep-dive → MVP blueprint และเพียงพอให้ทีมคุยภาษาเดียวกันก่อนทำ risk audit. หลังการแก้ alignment รอบนี้ สถานะเอกสารเชื่อมกันแล้ว:

1. **Narrative resolved:** `ai_architecture_design.md` ตอนนี้เล่าเป็น generic finance agent engine ที่มี flagship demo = Sell-side ER P2.
2. **Scope resolved:** `equity_research_deep_dive.md` เปลี่ยนจาก demo P1+P2 เป็น demo/build หลัก = P2 เท่านั้น; P1/P3-P7 เป็น expansion story.
3. **MVP vs production clarified:** `er_p2_mvp_dev_blueprint.md` เพิ่ม scope lock แยก MVP, stub, production extension ชัดเจน.
4. **Spec defect resolved:** `consensus_dev_fn` ใน ER tool registry ถูกเติมสูตร `dev = abs(tp - iaa_tp) / iaa_tp` แล้ว.
5. **Historical Step 2 carry-over resolved by Step 6:** data dependency ของ L5/L7 ถูกแยกเป็น typed reference policy แล้ว: public/broker/manual evidence ใช้ได้ถ้า label ชัด; provider-native aggregate consensus และ full transcript เป็น optional licensed evidence เฉพาะเมื่อ claim ต้องใช้. Threshold policy และ eval split ถูกล็อกใน `implementation_readiness_plan.md`.

**Step 1 Done When:** ทีมยอมรับ scope line นี้: **"Build P2 Earnings Update walking skeleton ที่วิ่งครบ L0-L9 แบบ MVP; ใช้ ER data ของ MSFT + AMZN + PTT fixtures; P1/P3-P7 และ production-grade features เป็น expansion story."**

---

## ขั้น 2 — หาจุดอ่อน/ความเสี่ยง/สิ่งต้องแก้ (cited)

**ทำอะไร:** ตรวจ 3 ไฟล์หา gap เทียบมาตรฐานวงการ AI agent product:

| จุดตรวจ | มาตรฐานอ้างอิง | เช็คในเอกสารเรา |
|---|---|---|
| **KPI วัดผลชัดไหม** | metric/target ต้องผูกกับ use case และวัด quality, cost, latency, safety แยกกัน; ไม่มี universal accuracy benchmark ([LangSmith evaluation concepts](https://docs.langchain.com/langsmith/evaluation-concepts), [Google AI/ML cost optimization](https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml/cost-optimization)) | Step 5 ล็อก project targets แล้ว: hard controls 100%, Recall@5 ≥90%, analyst rubric ≥4/5, latency/cost budgets |
| **Governance/security ระหว่าง dev** | secure-development practices ต้อง integrate ตลอด SDLC และ AI risk ต้อง Govern/Map/Measure/Manage ต่อเนื่อง ([NIST SSDF](https://csrc.nist.gov/pubs/sp/800/218/final), [NIST AI RMF](https://airc.nist.gov/airmf-resources/airmf/5-sec-core/)) | Step 5 Phase B/H + control traceability ล็อก security/risk ก่อน release |
| **Continuous monitoring ตั้งแต่วันแรก** | offline eval ก่อน deploy และ online/operational feedback หลัง deployทำงานเป็น improvement loop ([LangSmith evaluation concepts](https://docs.langchain.com/langsmith/evaluation-concepts), [Google MLOps](https://docs.cloud.google.com/architecture/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning)) | local PostgreSQL/JSON trace เป็น MVP source of truth; Enterprise เพิ่ม SLO/alerting/on-call |
| **Data ที่ใช้ demo** | company universe เคาะแล้ว: MSFT + AMZN + PTT; deterministic L0-L9 smoke ผ่าน | ไม่บล็อก I/O build แล้ว; ยังต้อง freeze final evidence pack ก่อน present |
| **Test separation** | ต้องแยก capability eval (วัด progress) กับ regression eval (กันพัง — pass ~100%) ไม่งั้นจะหยุดพัฒนาหรือปล่อยของพัง ([langchain readiness checklist](https://www.langchain.com/blog/agent-evaluation-readiness-checklist)) | Step 6 เพิ่มแผนแยก regression/capability/gate/demo replay แล้ว; Step 7 Work Package 11 ทำให้ runnable |

**Output:** list gap ที่ต้องปิดก่อน confirm (ขั้น 3)

### Step 2 Execution — Risk/Gap Audit (post-data-collection, 2026-07-17)

**Scope:** หลังมี MSFT/AMZN/PTT fixtures จริงแล้ว (ขั้น 3+4) — ตรวจซ้ำว่า data ที่เก็บมาเปิด risk ใหม่อะไรบ้าง เทียบ 3 ไฟล์ (architecture/ER deep-dive/blueprint) กับหลักฐานภายนอก. **กติกา:** ใส่เฉพาะ finding ที่มี source จริงยืนยันได้ — ไม่มี source ห้ามใส่

| # | Risk finding | Source | Confidence | กระทบ layer/ขั้นไหน |
|---|---|---|---|---|
| R1 | **LLM extract ตัวเลขจากงบ (SEC 10-K/10-Q) โดยตรงล้มเหลวสูงมาก** — benchmark ปี 2026 ทดสอบ 6 model บน SEC filing จริง 7 ฉบับ ไม่มี model ไหนได้ valid output แม้แต่ฉบับเดียว (0/7) | [ExtractBench arxiv](https://arxiv.org/html/2602.12247v2) | High (arxiv benchmark, primary) | **L0 Ingestion** — ยืนยันว่า design เดิม (deterministic parser, ไม่ให้ LLM parse ตาราง) ถูกทางแล้ว; ถ้า implementation จริงหลุดไปใช้ LLM parse PDF ตรงๆ = เสี่ยงสูงสุด |
| R2 | **LLM คำนวณเชิงตัวเลขหลายตัวแปร (multivariate) พังหนัก** — accuracy ร่วงจาก 95.6% (lookup ตัวเลขเดี่ยว) เหลือใกล้ 0% เมื่อโจทย์ต้องคำนวณข้ามหลายตัวแปร; และ format ที่ AI ตอบสวย **ไม่สัมพันธ์กับความถูกต้อง** (บาง model ตอบตารางสวยแต่ตัวเลขมั่ว) | [FAITH arxiv](https://arxiv.org/html/2508.05201v1) | High (arxiv benchmark) | **L2 Orchestration (quant)** — ยืนยันหลักการเดิม "quant tool แยกจาก LLM, ห้าม LLM เดาเลข" (comps_engine/dcf_engine ใน code) เป็นสิ่งจำเป็นจริง ไม่ใช่แค่ design choice ทั่วไป — ต้อง**บังคับ** ห้าม agent คำนวณ surprise/valuation เองแม้แต่ตอน debug |
| R3 | **Non-GAAP metric (เช่น "adjusted EPS") เทียบกับ GAAP metric ตรงๆ ไม่ได้ตามกฎ** — SEC Regulation G บังคับว่าต้องโชว์ GAAP measure คู่กันเสมอ + reconciliation เมื่อเผยแพร่ non-GAAP figure (ครอบคลุมถึง earnings call/investor presentation ไม่ใช่แค่ filing) | [SEC.gov Reg G](https://www.sec.gov/rules-regulations/2003/03/conditions-use-non-gaap-financial-measures) | High (regulator primary source) | **L2 surprise_fn + L8 schema** — ตรงกับ caveat ที่เจอจริงใน AMZN fixture (`prior_estimates.eps` เป็น adjusted EPS ปนกับ `raw_financials.eps_diluted` ที่เป็น GAAP) → ต้องเพิ่ม field `eps_basis: enum[GAAP, non_GAAP]` ใน schema กัน surprise_fn เทียบข้ามฐานผิด |
| R4 | **Redistribution ข้อมูลจาก public snapshot (Zacks/StockAnalysis screenshot) มีความเสี่ยงด้าน ToS/licensing** — เว็บ financial data ส่วนใหญ่ระบุ "personal use only"; การ resell/redistribute ข้อมูลที่ scrape มาโดยไม่ได้รับอนุญาตเป็นสาเหตุหลักของคดีความ | [OECD analysis via medium/zyte](https://www.zyte.com/blog/regulatory-compliance-for-alternative-web-scraped-financial-data/) | Medium (secondary source สรุปจาก legal analysis, ไม่ใช่ ToS ต้นฉบับของแต่ละ provider โดยตรง) | **L5 Retrieval + presentation** — peer_multiples/consensus ที่เก็บไว้ตอนนี้เป็น "public snapshot" ใช้ทดสอบ I/O ได้ แต่**ห้ามโชว์เป็น production data source ถาวรตอน present** — ต้อง frame ว่าเป็น demo/research snapshot ไม่ใช่ data pipeline ที่จะ resell |
| R5 | **deviation gate ถ้า route ผิดจะ publish โดยยังไม่มี note** — skeleton เดิมส่ง `"gate": "compliance"` จาก `revalue_rating` ทำให้เคส deviation สูงอาจข้าม `draft_note` แล้วไป `publish` ได้หลัง compliance | `03_dev_blueprint/er_p2_mvp_dev_blueprint.md` §10.4 + [LangGraph persistence docs](https://docs.langchain.com/oss/python/langgraph/persistence) | High (code/doc trace + primary framework docs) | **L3 Human Loop** — ต้องมี `valuation_gate` แยกจาก `compliance` และ resume กลับ `draft_note`; test ต้องล็อก path นี้ก่อน Step 3 |
| R6 | **schema skeleton กว้างเกินไป (`dict/list`) ทำให้ citation/provenance หลุดได้เงียบๆ** — data pack มี source/evidence contract แล้ว แต่ runtime skeleton ยังไม่บังคับ `source_id`, `basis`, `published_at`, `purpose` | `07_implementation/data/golden_dataset_schema.md`; [ExtractBench schema-driven eval](https://arxiv.org/html/2602.12247v2) | High | **L8 Schema Contract** — ก่อน Step 3 ต้องสร้าง typed Pydantic schema หรืออย่างน้อยล็อก doc contract: `SourceRef`, `Citation`, `SurpriseMetric`, `ValuationReference`, `ResearchNote` |
| R7 | **claim-level citation ยังเป็น data artifact ไม่ใช่ runtime behavior** — L5 corpus พร้อม แต่ยังไม่มี citation renderer ที่ fail ถ้า factual claim ไม่มี source ID | `02_sector_db/company_db/processed/retrieval_corpus_2026-07-17.jsonl`; `field_provenance_2026-07-17.csv`; CFA report essentials source ใน ER deep-dive §13/§17 | High | **L5 Retrieval + L6 Lineage** — runtime note ต้องนับ factual claims และบังคับ claim-level citation-by-ID ก่อนส่ง compliance |
| R8 | **regression eval ยังไม่แยกจาก capability eval** — smoke test บอก schema/data ผ่าน แต่ยังไม่บอกว่า agent ดีขึ้นหรือ regression ไม่พัง | [LangChain Agent Evaluation Readiness Checklist](https://www.langchain.com/blog/agent-evaluation-readiness-checklist) | High | **L7 Eval** — ก่อน Step 3 ต้องล็อก eval plan: regression eval ต้อง pass ใกล้ 100%; capability eval ใช้วัด progress ได้แม้ pass rate ต่ำ |
| R9 | **valuation tool registry ยังมากกว่า code จริง** — docs มี comps/DCF/rating/wacc/capm แต่ `07_implementation/src/er_engine/tools/quant.py` ตอนนี้มีแค่ surprise/expected_return/consensus_deviation/forecast_error | `02_sector_db/equity_research_deep_dive.md` §18.2; `07_implementation/src/er_engine/tools/quant.py` | Medium-High | **L2 Quant** — Step 3 ต้องเริ่มจาก minimal `comps_engine` + `rating_fn` wrappers หรือระบุชัดว่า DCF เป็น cross-check roadmap ไม่ใช่ current runtime |
| R10 | **observability ตอนนี้เป็น trace counter ไม่ใช่ audit trail ที่จูจเห็นได้** — deterministic pipeline มี trace message แต่ยังไม่มี node input/output lineage, model tier, latency, source IDs | `07_implementation/src/er_engine/pipeline.py`; blueprint L6 | Medium | **L6 Observability** — ก่อน Step 3 ต้องกำหนด JSON trace schema ที่ demo ได้แม้ยังไม่ใช้ Langfuse |
| R11 | **backup wording แบบ synthetic/hardcode ลดความน่าเชื่อถือของ evidence story** — hackathon scoring ให้ feasibility/impact จากความสมเหตุสมผล; synthetic/hardcode ถ้าไม่ label จะดูเหมือนปลอมข้อมูล | Grading criteria PDF; `er_p2_mvp_dev_blueprint.md` risk table | Medium | **Demo readiness** — ใช้ verified replay จาก golden fixtures + source pack เป็น backup; synthetic ใช้ได้เฉพาะ unit test ไม่ใช่ demo evidence |
| R12 | **เอกสาร gaps บางจุดยังอ้าง MTC/proxy ticker เก่า** ทั้งที่ company universe เคาะเป็น MSFT+AMZN+PTT แล้ว | `02_sector_db/equity_research_deep_dive.md` §20; `er_p2_mvp_dev_blueprint.md` §12 | Medium | **Docs consistency** — ก่อน Step 3 ต้องลบ/แก้ obsolete MTC/proxy gap เพื่อไม่ให้ทีมวนกลับไป scope เก่า |

**Excluded (ค้นแล้วไม่พบ source ที่ยืนยันตรงพอ — ไม่ใส่ตามกติกา):**
- ข้อกล่าวอ้างเรื่อง SETTRADE/Zacks/StockAnalysis ToS ข้อความเฉพาะเจาะจง (พบแค่ pattern ทั่วไปของอุตสาหกรรม ไม่ใช่ข้อความจริงจาก 3 เว็บนี้ — R4 จึงลงเป็น Medium confidence ไม่ใช่ High)

### Step 2 Review Verdict

**ผ่านแบบมีเงื่อนไข.** พบ risk ใหม่ 4 ข้อจากข้อมูลจริงที่เก็บมา — **R1/R2 ยืนยัน (ไม่ใช่แค่ทำลาย) การตัดสินใจ design เดิม** ว่าถูกทาง (deterministic L0 parser + quant tool แยกจาก LLM) — ควรถือเป็น **hard requirement** ไม่ใช่ nice-to-have แล้วหลังเห็น benchmark. R3/R4 เป็น**ของใหม่ที่ยังไม่เคยแก้**:

**Step 2 Done When (เพิ่มจาก audit นี้):**
1. schema เพิ่ม `eps_basis` field กัน GAAP/non-GAAP ปนกัน (R3) — ก่อนเขียน `surprise_fn` จริง
2. สไลด์/เอกสาร present ระบุชัดว่า peer/consensus data = research snapshot ไม่ใช่ production feed (R4)
3. L0 ingestion implementation ต้อง**ห้าม**ใช้ LLM parse ตารางงบดิบตรงๆ — บังคับ deterministic parser (pdfplumber/XBRL) ก่อนเข้า LLM ขั้นไหนก็ตาม (R1)
4. ทุก quant calculation (surprise/valuation/deviation) ต้องมาจาก `tools/quant.py` เท่านั้น ไม่มี agent prompt ไหนขอให้ LLM "คำนวณ" เอง แม้จะดู simple (R2)
5. `deviation gate` ต้องแยกจาก compliance gate และ resume กลับ `draft_note` เสมอ (R5)
6. runtime schema ต้องมี typed source/citation/basis fields และห้ามใช้ `dict` กว้างเป็น contract หลัก (R6)
7. note generator ต้องมี `claim-level citation` renderer/checker: factual claim ไม่มี source ID = fail ก่อน compliance (R7)
8. สร้างแผน `regression eval` แยกจาก capability eval และผูกกับ `make test`/future eval harness (R8)
9. docs ต้องตรงกันว่า MSFT + AMZN + PTT คือ current universe; MTC/proxy ticker เก่าไม่ใช่ open blocker แล้ว (R12)

---

## ขั้น 3+4 — Confirm (stack/agent-loop/phase/scope) + หาข้อมูล company (ทำคู่ขนาน)

**ทำไมทำคู่กัน:** scope/phase ที่ confirm ได้ ขึ้นกับว่าหาข้อมูล company ได้จริงแค่ไหน — ถ้า confirm ก่อนแล้วข้อมูลไม่มี ต้องย้อนมาแก้ scope ใหม่ เสียเวลาซ้ำ

**Step 3 sign-off (updated 2026-07-18 — professional source confirmed):**  
เป้าหมายของขั้นนี้คือ "ล็อก decision ที่ต้องใช้ก่อน build runtime จริง" ไม่ใช่เริ่ม implement. ทุก decision ด้านล่าง map กลับไป blueprint และแหล่งอ้างอิงมาตรฐานแล้ว.

| Decision area | Sign-off | Professional / official evidence | Confidence | Risk / action before Step 7 |
|---|---|---|---|---|
| **Scope** | Build เฉพาะ **P2 Earnings Update** สำหรับ MSFT+AMZN+PTT; P1/P3-P7 เป็น vision/demo roadmap เท่านั้น | Blueprint §6 ล็อก MVP vs production extension; AWS Responsible AI Lens แนะนำให้ scope use case แคบและกำหนด release criteria ชัด ([AWS Responsible AI Lens](https://aws.amazon.com/blogs/machine-learning/announcing-the-aws-well-architected-responsible-ai-lens/)) | High | ห้ามเพิ่ม generic graph loader, OCR เต็ม, full corpus ACL, RLTHF หรือ semantic cache เข้า MVP; เล่าเป็น extension ใน pitch |
| **Model gateway / L9** | ใช้ **LiteLLM** เป็น abstraction/router; MVP ใช้ Python SDK/config ได้ก่อน ยังไม่ต้องมี proxy server | LiteLLM ระบุว่าใช้ OpenAI-format I/O กับ 100+ models และมี routing/retry/fallback/budget controls ([LiteLLM docs](https://docs.litellm.ai/)) | High | ก่อน runtime ต้องสร้าง config tier: cheap/mid/strong + fallback; อย่าผูก code กับ provider เดียว |
| **Graph / L1-L3** | ใช้ **LangGraph StateGraph** สำหรับ 6-node P2 loop + human interrupt 2 จุด; durable state อยู่ PostgreSQL ตั้งแต่ product MVP | LangGraph รองรับ persistence, checkpoint และ interrupt/resume ผ่าน checkpointer/thread ID ([LangGraph interrupts](https://docs.langchain.com/oss/python/langgraph/interrupts), [LangGraph persistence](https://docs.langchain.com/oss/python/langgraph/persistence)) | High | HTTP request ห้ามถือ workflow state; FastAPI คืน `run_id` แล้ว durable worker/checkpoint ทำงานต่อ |
| **Runtime schema / L8** | ใช้ **Pydantic v2 strict typed models** ทุก handoff; ห้ามใช้ `dict/list` กว้างเป็น production contract | Pydantic strict mode ลด coercion และ fail เมื่อ type ไม่ตรง ([Pydantic strict mode](https://pydantic.dev/docs/validation/2.5/concepts/strict_mode/)); Step 2 R6 ล็อก schema objects แล้ว | High | Phase 1 ต้องสร้าง `SourceRef`, `Citation`, `SurpriseMetric`, `ValuationResult`, `ResearchNote`; claim ไม่มี `source_id`/`purpose` = fail |
| **Retrieval / L5** | ใช้ **PostgreSQL full-text + pgvector** เป็น path เดียวตั้งแต่ MVP; filter company/PIT/license/purpose ก่อน ranking; reranker เพิ่มเมื่อ eval พิสูจน์ | PostgreSQL มี full-text search และ pgvector รองรับ vector/hybrid search ([PostgreSQL FTS](https://www.postgresql.org/docs/current/textsearch.html), [pgvector](https://github.com/pgvector/pgvector)) | High | ไม่ใช้ Chroma เพื่อตัด migration/dual-store; corpus ต้องมี `published_at`, `source_id`, `company`, `purpose`, `permitted_use` |
| **Observability / L6** | OTel-compatible trace contract เก็บ local PostgreSQL/JSON และแสดงใน Next.js; external exporter เป็น optional Enterprise adapter | OpenTelemetry เป็น vendor-neutral telemetry framework และมี GenAI conventions ที่พัฒนาต่อเนื่อง ([OpenTelemetry docs](https://opentelemetry.io/docs/), [GenAI observability](https://opentelemetry.io/blog/2026/genai-observability/)) | High | trace ต้องมี node/tool/model/gate, source IDs, config version, token/cost, latency, retry และ artifact pointer |
| **Product surface** | FastAPI + React/Next.js; REST command/query + SSE status/poll fallback; durable worker + PostgreSQL state | OpenAPI เป็นมาตรฐาน API contract; LangGraph persistence รองรับ durable state ([OpenAPI](https://spec.openapis.org/oas/latest.html), [LangGraph persistence](https://docs.langchain.com/oss/python/langgraph/persistence)) | High | UI ไม่มี business/finance logic; create/resume/export ต้อง idempotent |
| **MVP security boundary** | ไม่มี authentication; ใช้ `demo_actor` และรัน local/private เท่านั้น | OWASP แนะนำลด functionality, permission และ autonomy เพื่อคุม excessive agency ([OWASP LLM06](https://owasp.org/www-project-top-10-for-large-language-model-applications/2_0_vulns/LLM06_ExcessiveAgency.html)) | High | ห้าม public exposure/production approval claim; auth+RBAC/SSO เป็น Enterprise blocker |
| **Agent safety / governance** | Agent ต้องมี limited agency: ไม่มี autonomous publish, ไม่มี tool permission กว้าง, มี human compliance gate เสมอ | OWASP LLM Top 10 ระบุ prompt injection, insecure output handling, sensitive info disclosure, excessive agency, overreliance เป็น risk หลัก ([OWASP LLM Top 10](https://owasp.org/www-project-top-10-for-large-language-model-applications/)); NIST AI RMF ใช้ Govern/Map/Measure/Manage เป็น lifecycle risk functions ([NIST AI RMF](https://airc.nist.gov/airmf-resources/airmf/5-sec-core/)) | High | Publish node ต้องรับเฉพาะ note ที่ approved แล้ว; external action ทุกอย่างต้อง audit และ human sign-off |
| **Build phase** | แก้ lock เป็น **Phase 0-8** ตาม blueprint §8: 0 Data/smoke → 8 Demo polish | Blueprint §8 มี Phase 8 Demo polish; AWS ML Lens และ Google MLOps แยก lifecycle เป็น framing/design/build/evaluate/deploy/monitor ([AWS ML Lens](https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/), [Google MLOps](https://docs.cloud.google.com/architecture/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning)) | High | เอกสารทุกที่ต้องใช้ 0-8 ให้ตรงกัน; Phase 8 คือ demo polish/backup ไม่ใช่ runtime feature creep |
| **Evaluation / L7** | แยก regression eval กับ capability eval; specification มี 20 cases และทำให้ runnable ตาม runtime dependency | LangChain แนะนำ review 20-50 traces, กำหนด success criteriaชัด, แยก capability vs regression และใช้ CI/CD gate ([LangChain eval readiness](https://www.langchain.com/blog/agent-evaluation-readiness-checklist)); MLflow GenAI datasets/golden sets ใช้กัน regression ข้าม version ([MLflow GenAI datasets](https://mlflow.org/docs/latest/genai/datasets/)) | High | รักษา deterministic regression baseline ตั้งแต่แรก; ทำแต่ละ case ให้ runnable เมื่อ package dependency พร้อม และครบทั้ง 20 ก่อน private release |

**Confirmed agent loop (Step 3 locked):**
1. `digest` → `update_model` → `revalue_rating` → `valuation_gate` เมื่อ confidence ต่ำหรือ consensus deviation > 15%.
2. Gate แรกต้อง resume กลับ `draft_note` หลัง human แก้ assumption/target ไม่ใช่ข้ามไป publish.
3. `draft_note` ต้อง render claim-level citations จาก `source_id`/passage id.
4. `compliance` เป็น human interrupt บังคับก่อน `publish`.
5. `publish` ทำได้เฉพาะเมื่อ `approved=True` และ trace/citation/eval checks ผ่าน.

**Step 3 entry gate ไป Step 7 build runtime:**
- [x] Stack locked: FastAPI + Next.js + PostgreSQL/pgvector + durable worker + LiteLLM + LangGraph + Pydantic + OTel-compatible local trace + deterministic Python quant.
- [x] Agent loop locked: 6-node P2 graph + valuation gate + compliance gate.
- [x] Phase locked: **0-8**.
- [x] Scope locked: P2 only; production extensions แยกชัด.
- [x] Company universe locked: MSFT + AMZN + PTT.
- [x] ก่อนเริ่ม coding runtime: เพิ่ม contract docs ให้ dev ยึดก่อนเขียน Phase 1 runtime:
  - `07_implementation/docs/runtime_schema_contract.md`
  - `07_implementation/docs/json_trace_schema.md`
  - `07_implementation/docs/eval_case_plan.md`

**Step 3 artifact checklist (ต้องใช้เป็น DoD ก่อน Phase 1 runtime):**

| Artifact | Owner path | Required content | Blocks what if missing |
|---|---|---|---|
| Runtime schema contract | `07_implementation/docs/runtime_schema_contract.md` → later code in `07_implementation/src/er_engine/schemas/` | Typed Pydantic objects for source, citation, surprise, valuation, note, gate, publish; strict validation; no loose handoff dicts | Blocks `digest`, `revalue_rating`, `draft_note`, `compliance` nodes because provenance can silently drop |
| JSON trace schema | `07_implementation/docs/json_trace_schema.md` → later code in `07_implementation/src/er_engine/obs/` | Node run envelope, source lineage, model tier, latency, gate events, checker results, replay pointer | Blocks demo trace, audit trail, gate debugging, Langfuse migration |
| Eval case plan | `07_implementation/docs/eval_case_plan.md` → later code in `07_implementation/src/er_engine/eval/` and `07_implementation/tests/` | 20 cases split into regression/capability/gate/demo-replay with pass/fail criteria | Blocks replacing deterministic smoke with LLM/LangGraph runtime |
| Model tier config contract | Documented in runtime schema + README, later code in `07_implementation/src/er_engine/router/` | `cheap`, `mid`, `strong`, fallback, budget guard, provider-agnostic names | Blocks LiteLLM integration only, not current smoke |
| Retrieval corpus contract | Documented in runtime schema, later code in `07_implementation/src/er_engine/retrieval/` | `source_id`, `passage_id`, `company`, `published_at`, `purpose`, PIT cutoff, evidence type | Blocks claim-level citation and PIT retrieval |

**หาข้อมูล company — แยก 2 บทบาท (อัปเดต 2026-07-17: ทำครบสำหรับ I/O smoke แล้ว):**

*Test fixture (ปลดบล็อก dev ทันที — US data ฟรีครบ):*
- [x] Schema นิยามครบ → `07_implementation/data/golden_dataset_schema.md` (layer→field→ground-truth)
- [x] MSFT FY26Q3 golden fixture พร้อม L0/L2/L3/L4/L7 → `07_implementation/data/raw/MSFT_FY26Q3_golden.json`
- [x] AMZN FY26Q1 golden fixture พร้อม L0/L2/L3/L4/L7 → `07_implementation/data/raw/AMZN_FY26Q1_golden.json`

*Demo company (โชว์จูจ — Thai เพื่อ criterion a, ทีมเคาะ):*
- [x] Thai ticker = PTT → `07_implementation/data/raw/PTT_1Q2026_demo.json`
- [x] SETTRADE IAA values filled for I/O: target/rating/count → fixture + `processed/L0_L9_research_fill_2026-07-17.csv`
- [ ] **Final evidence pack:** save manual screenshot/export from SETTRADE IAA with date/time before presentation

**Data access reality (updated 2026-07-17):** public evidence pack ปิด actuals, company-specific surprise, PIT peer multiples, forecast history และ field-level provenance สำหรับ MSFT/AMZN/PTT แล้ว. PTT ใช้ dated KS/InnovestX/UOBKH/Globlex แทน Finanzen proxy. สิ่งที่ยังไม่มีคือ **provider-native historical aggregate consensus** ซึ่งต้องใช้ FactSet/Bloomberg/Visible Alpha/LSEG/SETSMART หรือ manual licensed export; fixture จะ label single-house reference ตรงๆ และไม่ปลอมว่าเป็น consensus. Canonical status อยู่ที่ `02_sector_db/company_db/collection_status.csv` และ `processed/professional_er_completeness_2026-07-17.csv`.

**Current I/O proof:** `make test` + `make smoke-l0-l9` ผ่าน และเขียน `07_implementation/data/processed/l0_l9_smoke_summary.json` ที่มี AMZN/MSFT/PTT ครบ L0-L9.

---

## ขั้น 5 — Research วิธีทำ product แบบมืออาชีพ (cited)

> **✅ Step 5 methodology approved and expanded (2026-07-18):** [`professional_build_methodology.md`](professional_build_methodology.md) เป็น executable playbook 22 sections: research log/claim-source-confidence, product boundary, target architecture, lifecycle Phase A-K, artifacts/tests/gates/owners, traceability, data/model/retrieval/API methodology, eval targets, security/compliance, release/incident/DoD และ decision register.

**Step 5 locked outcomes:**
- Product path = **Internal Analyst Copilot (private MVP) → Enterprise Research Platform**; ไม่มี autonomous external publishing.
- Product stack = **FastAPI + React/Next.js + PostgreSQL + pgvector + durable worker + LangGraph/Pydantic/LiteLLM**.
- MVP ไม่มี authentication จึงเป็น local/private demo เท่านั้น; trusted identity/RBAC/SSO เป็น Enterprise gate.
- Build order = framing/control map → contracts/data → one-node walking skeleton → P2 vertical slices → eval/security → private release → operate/improve → Enterprise hardening.
- Current model-risk reference = **SR 26-2**, which superseded SR 11-7 on 2026-04-17 ([Federal Reserve](https://www.federalreserve.gov/supervisionreg/srletters/SR2602.htm)).
- Professional backbone = NIST AI RMF, ISO/IEC 42001, NIST SSDF, Anthropic workflow-first, Google MLOps/SRE, CFA/FINRA/Thai SEC controls; see cited rationale in every methodology section.

---

## ขั้น 6 — วิเคราะห์แผน + เลือกเครื่องมือทดสอบ + หาจุดอ่อนก่อน implement (cited)

> **Canonical Step 6 execution plan:** [`implementation_readiness_plan.md`](implementation_readiness_plan.md) เป็น source of truth สำหรับ file map, interface freeze, dependency-ordered work packages, test/eval ownership, risk register และ Step 7 entry gate. ถ้ารายละเอียดลำดับ implement ในไฟล์นี้หรือ blueprint ขัดกับแผนดังกล่าว ให้แก้ conflict ก่อนลงมือ ไม่เลือกเองแบบเงียบๆ.

**กรอบทดสอบ — 3 evaluator modes ที่ใช้ร่วมกัน** ([LangSmith evaluation concepts](https://docs.langchain.com/langsmith/evaluation-concepts)):

| ชั้น | คืออะไร | ใช้กับ ER engine ยังไง |
|---|---|---|
| **1. Programmatic assertion** (ฐาน) | เช็ค schema valid, required field, latency, forbidden action | Pydantic validation (L8) ที่มีอยู่แล้ว — เพิ่ม assert สูตรคำนวณ (comps_engine/dcf_engine) ให้ผลตรง unit test |
| **2. LLM-as-judge** (กลาง) | ให้ AI ตรวจ AI แบบ calibrated | eval harness (L7) — ตรวจ note มี citation ครบ, thesis สมเหตุสมผลไหม |
| **3. Human review** (บนสุด) | คนตรวจ case ที่ 2 ชั้นแรกจับไม่ได้ | licensed-analyst gate (มีอยู่แล้วใน design) |

**แยก eval 2 ชุด (สำคัญ — จุดที่ blueprint เดิมยังไม่มี):**
- **Regression eval** (เริ่ม 20-case plan แล้วโตตาม coverage/failure; hard controls pass 100%) — กันของที่ทำงานได้อยู่แล้วพัง
- **Capability eval** (case ยาก, pass rate ต่ำได้) — วัดว่า AI ทำงานยาก (เช่น rating judgment) ดีขึ้นเรื่อยๆ ไหม
- **เหตุผลต้องแยก:** testing เป็น deployment-blocking correctness assertion ส่วน evaluation วัดคุณภาพที่อาจเป็น relative/subjective; ใช้ทั้งสองร่วมกัน ([LangSmith evaluation concepts](https://docs.langchain.com/langsmith/evaluation-concepts))

**Practical:** เลือก workflow เดียว (P2 — ตรงกับ scope ที่ confirm แล้ว). ตอนนี้มี deterministic smoke harness แล้ว:

- `07_implementation/src/er_engine/pipeline.py` วิ่ง L0-L9 จาก fixtures
- `07_implementation/src/er_engine/tools/quant.py` มีสูตร deterministic เบื้องต้น
- `07_implementation/tests/test_l0_l9_io.py` มี 16 unit/smoke/doc-contract tests รวม PIT/nested citation contract
- `make smoke-l0-l9` สร้าง output summary

ขั้นต่อไปก่อน agent จริง: ปิด Must Fix ใน `implementation_readiness_plan.md` §10 แล้วเริ่ม Step 7 ที่ Work Package 0. **20 eval cases** ใน `07_implementation/docs/eval_case_plan.md` จะถูกทำให้ runnable ตาม dependency map ในแผน §7; ไม่บังคับทำ case ที่ยังไม่มี runtime dependency ให้เสร็จก่อน walking skeleton.

**เครื่องมือแนะนำ:** deterministic tests (ชั้น 1) + versioned custom eval harness/optional calibrated judge (ชั้น 2) + finance-owner and second-review checklist (ชั้น 3). Local PostgreSQL/JSON trace เป็น source of truth; external eval/trace platform เป็น optional adapter.

**Output ขั้นนี้:** `implementation_readiness_plan.md` + smoke baseline + 20-case specification + risk/entry checklist. Step 6 ผ่านแล้วในระดับ readiness 100% สำหรับเริ่ม Step 7 Work Package 0: Must Fix ถูก sign-off, stack/test/model/data/Git-control decisions ถูกล็อก, และไม่มี Critical planning ambiguity เหลืออยู่. Runtime/eval implementation เริ่มใน Step 7 เท่านั้น.

---

## ขั้น 7 — Follow the plan

เริ่มจาก `implementation_readiness_plan.md` Work Package 0→13 ซึ่ง crosswalk กลับไปยัง `er_p2_mvp_dev_blueprint.md` §8 Phase 0→8. สถานะตอนนี้พร้อมเริ่ม implement 100% ที่ Work Package 0: มี Phase 0 data/smoke harness แล้ว, persistence/tooling decision ถูกล็อกเป็น PostgreSQL + pgvector + SQLAlchemy 2 + psycopg 3 + Alembic, frontend test stack ถูกล็อกเป็น Vitest + React Testing Library + Playwright, และ Git state-changing command ทั้งหมดให้ project owner รันเอง. ห้ามติดตั้ง `07_implementation/requirements.txt` เดิมก่อน reconcile dependency authority ใน Work Package 0. จากนั้นค่อยแทน deterministic pieces ทีละชั้น:

1. L0 parser/PIT loader จาก raw/processed sources.
2. L2 quant node ใช้ `07_implementation/src/er_engine/tools/quant.py`.
3. L3 gate state + editable resume.
4. L5 retrieval/citation index.
5. L6 trace/lineage surface.
6. L7 eval/before-after metrics.

ทุก work package เขียน test/eval ที่ dependency พร้อมแล้วเป็น failing case ก่อน แล้ว implement ให้ผ่าน; deterministic baseline 16 tests ต้องยังเขียวทุก package.

---

## ขั้น 8 — ทดสอบให้ครอบคลุมสำหรับ present

**เกิน unit test ธรรมดา — ต้องทดสอบ "demo scenario" ตรงๆ:**
- รัน end-to-end ด้วย company data จริง (ไม่ mock) อย่างน้อย 3 รอบ — เช็ค consistency
- จงใจ trigger gate (ป้อนเคสที่ deviation เกิน 15%) — เช็คว่า interrupt+resume ทำงานจริง ไม่ค้าง
- จับเวลา wall-clock จริงหลายรอบ — เอาค่าเฉลี่ยไปทำตาราง before/after (blueprint §7)
- **Canary run** — รันเงียบๆ ก่อนวันจริง เก็บผลไว้เป็น backup ถ้า live พัง ([langchain readiness checklist](https://www.langchain.com/blog/agent-evaluation-readiness-checklist) แนะนำ staged rollout ก่อน full release — hackathon = "staged" คือซ้อมก่อนวันจริง)
- อัดวิดีโอ 1 รอบที่รันสำเร็จสมบูรณ์ (backup ตาม blueprint §11)

---

## ขั้น 9 — Loop หาข้อผิดพลาด → แก้ → พัฒนา

**นี่คือ Measure/Manage + continual-improvement loop** ([NIST AI RMF](https://airc.nist.gov/airmf-resources/airmf/5-sec-core/), [ISO/IEC 42001](https://www.iso.org/standard/42001)) — ไม่ใช่ทำครั้งเดียวจบ:

```
รัน eval suite (regression+capability) → พบ fail
        │
   เข้าใจ root cause (log/trace จาก L6 Observability)
        │
   แก้ (prompt/schema/tool/threshold)
        │
   รัน regression eval ซ้ำ (ต้องยัง pass ~100% ของเดิม)
        │
   วนซ้ำ จนก่อนวัน present X วัน → freeze (หยุดแก้ กันของพังก่อนพรีเซนต์จริง)
```

**กฎ freeze:** กำหนดวัน "code freeze" ล่วงหน้าก่อน present (เช่น 1 วันก่อน) — ทดสอบซ้อมรอบสุดท้ายเท่านั้น ห้ามแก้ logic ใหม่ (กันพังตอนใกล้เวลา)

---

## Sources
- NIST AI RMF Core — https://airc.nist.gov/airmf-resources/airmf/5-sec-core/
- NIST SP 800-218 SSDF — https://csrc.nist.gov/pubs/sp/800/218/final
- ISO/IEC 42001 — https://www.iso.org/standard/42001
- Google MLOps — https://docs.cloud.google.com/architecture/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning
- LangSmith evaluation concepts — https://docs.langchain.com/langsmith/evaluation-concepts
- Google SRE canarying releases — https://sre.google/workbook/canarying-releases/
- Full Step 5 source register — `03_dev_blueprint/professional_build_methodology.md` §22
