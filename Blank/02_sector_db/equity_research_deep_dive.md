# Equity Research (sell-side) — Deep-Dive DB หลักของสายงาน

### แหล่งข้อมูลหลักฉบับเดียว · Implementation-ready · ป้อน AI Engine 10-layer (L0-L9)

> **กฎไฟล์:** self-contained 100% — อ้างอิงเฉพาะลิงก์เว็บภายนอก ไม่ลิงก์ไฟล์อื่นในโปรเจกต์ · ภาษาไทยหลัก · ทุก pipeline spec ครบพอ tech เขียนโค้ดต่อได้ทันที (I/O JSON schema + สูตรเต็ม + นิยามตัวแปร)

---

## 1. Purpose & วิธีอ่าน

ไฟล์นี้คือ **DB หลักของสายงาน Equity Research** — รวมทุกอย่างที่ทีมต้องใช้: อาชีพ ER ทำงานจริงยังไง, ทุก workflow (7 แบบ), สูตร valuation เต็ม, ข้อบังคับกฎหมาย, และ **spec ป้อน engine 10-layer** (L0 Ingestion · L1 Task Map · L2 Orchestration · L3 Human-Loop · L4 Memory · L5 Guardrail+Retrieval · L6 Observability · L7 Governance+Eval · L8 Schema Contract · L9 Routing+Caching)

**วิธีอ่าน:**

- อยากเข้าใจอาชีพ → §2
- อยากเห็น workflow ทั้งหมด → §3 (สรุป) → §4-10 (pipeline เต็มทีละอัน)
- ทีม tech จะ build → อ่าน §4-10 บล็อก (b)(c)(d) + §7 สูตร + §14 master schema/tool registry
- อยากรู้ engine ต้องเพิ่มอะไรเพื่อ ER → §10

**นิยามศัพท์หลัก (ใช้ทั้งไฟล์):**

- **EPS** = Earnings Per Share (กำไรต่อหุ้น) · **forward_EPS** = EPS คาดการณ์ 12 เดือนข้างหน้า
- **P/E** = Price / EPS · **EV** = Enterprise Value = market cap + net debt + minority + preferred
- **EBITDA** = Earnings Before Interest, Tax, Depreciation, Amortization · **EBIT** = ก่อนดอกเบี้ย+ภาษี
- **NIM** = Net Interest Margin (สำหรับหุ้นการเงิน) · **WACC** = Weighted Average Cost of Capital
- **FCFF** = Free Cash Flow to Firm · **consensus** = ค่าเฉลี่ยประมาณการของ analyst ทุกคน (ไทยใช้ IAA Consensus)
- **PIT** = Point-In-Time (ข้อมูล ณ เวลาที่ประกาศจริง กัน lookahead bias)
- **rating** = คำแนะนำ Buy/Hold/Sell · **price target (TP)** = ราคาเป้าหมาย 12 เดือน

---

## 2. อาชีพ Equity Research — Professional Context

### 2.1 Sell-side vs Buy-side (โฟกัสงานนี้ = sell-side)

| มิติ             | Sell-side (งานนี้)                                                                                         | Buy-side                                                |
| -------------------- | ---------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------- |
| นายจ้าง       | brokerage / investment bank                                                                                      | hedge fund / asset manager / กองทุน               |
| output               | research report เผยแพร่ให้ลูกค้าสถาบัน (paid access)                                       | บันทึกภายใน ไม่เผยแพร่             |
| จุดประสงค์ | **research = marketing** ดึง trading commission เข้า firm                                           | หา alpha ให้พอร์ตตัวเอง                 |
| ความลึก       | เจาะ sector แคบ ลึก + timely + comps ที่ตรวจสอบได้                                        | กว้างกว่า, proprietary model, alternative data |
| skin-in-game         | ไม่มีเงินตัวเอง (แนะนำ)                                                                      | **มี** (ตัดสินใจลงเงินจริง)   |
| ภาระ             | **ต้อง publish ขั้นต่ำต่อบริษัทต่อไตรมาส แม้ไม่มีอะไรจะพูด** | เลือกได้ ทำเฉพาะที่สนใจ           |

*(sources: [wallstreetprep buy/sell](https://www.wallstreetprep.com/knowledge/sell-side-vs-buy-side-equity-research/), [mergersandinquisitions](https://mergersandinquisitions.com/buy-side-vs-sell-side-equity-research/))*

### 2.2 Role ladder

Research Associate (สร้าง/อัปเดตโมเดล, ดึงข้อมูล) → **Analyst / VP** (เจ้าของ coverage, ออก rating/TP, เซ็นรายงาน — เป็น licensed analyst) → Senior Analyst → **Director of Research** (คุมทีม, จัดสรร coverage)

### 2.3 Day-in-the-life

- **วันปกติ (ส่วนใหญ่ของไตรมาส):** ~12 ชม./วัน — อัปเดตโมเดล, ตอบคำถาม buy-side, morning meeting, เขียน note สั้น
- **Earnings season / conference (2-3 สัปดาห์/ไตรมาส):** ~16 ชม./วัน — ฟังงบ, ถามใน call, อัปเดตโมเดล, ส่ง note ด่วนให้ลูกค้า
  *(source: [wallstreetoasis sell-side](https://www.wallstreetoasis.com/resources/careers/jobs/sell-side-analysts))*

### 2.4 ใครบริโภค research (สำคัญต่อการออกแบบ output)

buy-side PM/analyst (ตัดสินใจลงทุน) · sales (ขาย idea ให้ลูกค้า) · trader · **corporate access** (จัดให้ผู้บริหารบริษัทเจอนักลงทุน) — output ต้อง timely + มี thesis ชัด + มี catalyst

### 2.5 Coverage universe + maintenance obligation

analyst 1 คน cover **50-60+ บริษัท** (เดิม 30-40 ต้นยุค 2000) — ต้อง maintain โมเดล + publish ขั้นต่ำต่อบริษัท/ไตรมาส → **นี่คือ pain หลักที่ AI แก้** (งานซ้ำ ปริมาณมาก deadline พร้อมกันตอน earnings)

### 2.6 บทบาท regulatory

รายงานทุกฉบับต้องผ่าน **licensed analyst sign-off** ก่อนเผยแพร่ (MiFID II/Reg AC/FINRA) — ดู §9

### 2.7 Thai context

- **IAA (สมาคมนักวิเคราะห์การลงทุน)** — รวบรวม **IAA Consensus** (ประมาณการ+target price หุ้นไทย) เผยแพร่บน SETTRADE.com ฟรี · IAA review รายงานก่อนขึ้น consensus ([settrade IAA](https://www.settrade.com/th/research/iaa-consensus/main), [iaathai](https://www.iaathai.org/))
- **SET Opportunity Day (oppday)** — บริษัทจดทะเบียนนำเสนอผลประกอบการต่อนักลงทุน (แหล่ง data สำคัญ)
- **SEC Thailand** — นักวิเคราะห์ต้องมีใบอนุญาต (analyst license)

---

## 3. ทุก Workflow ที่ ER ทำ — ตารางสรุป (7 แบบ)

| #  | Workflow                                    | ความถี่                         | Output artifact                    | AI-fit                                                |
| -- | ------------------------------------------- | -------------------------------------- | ---------------------------------- | ----------------------------------------------------- |
| P1 | **Coverage Initiation**               | นานๆ ครั้ง (หุ้นใหม่) | Initiation report 20-50+ หน้า  | สูง (สังเคราะห์ข้อมูลมหาศาล) |
| P2 | **Earnings Update Cycle**             | รายไตรมาส (ถี่สุด)      | Earnings note + model update       | **สูงสุด** (5.7hr→45min)                 |
| P3 | **Flash / Update Note**               | reactive ต่อข่าว/event          | Flash note สั้น                | สูง (เร็ว = คุณค่า)                      |
| P4 | **Thematic / Industry Deep-Dive**     | เป็นครั้งคราว             | Thought piece ยาว               | ปานกลาง-สูง (วิจัยกว้าง)          |
| P5 | **Model Maintenance**                 | ต่อเนื่อง                     | โมเดลอัปเดต             | สูง (งานซ้ำ)                                 |
| P6 | **Marketing & Client Service**        | ต่อเนื่อง                     | talking points, Q&A, roadshow deck | ปานกลาง (ช่วย prep)                        |
| P7 | **Idea Generation / Morning Meeting** | รายวัน                           | idea list, screening               | ปานกลาง (คัดกรอง)                       |

**demo/build หลักรอบ hackathon = P2 เท่านั้น** (Earnings Update Cycle: scope สั้น, ROI วัดได้, วิ่งครบ L0-L9 ได้จริง) · P1/P3-P7 = expansion story เพื่อโชว์ว่า engine เดียวกันรองรับ workflow ER อื่นได้ภายหลัง

> **หมายเหตุความจริง:** P6/P7 บทบาท AI เบากว่า P1-P5 (งาน comms/internal) — engine ช่วย prep/คัดกรอง ไม่ผลิต research artifact โดยตรง จึงไม่มีสูตร valuation ในสองอันนี้ (spec I/O ตามจริง)

---

# §4-10. Pipeline เต็มทุก workflow (implementation-ready)

> **โครงทุก pipeline เหมือนกัน 4 บล็อก:** (a) Workflow narrative · (b) L1 Task Graph (I/O schema จริง) · (c) L2 Orchestration (agent + tool signature + สูตร) · (d) L0-L9 input/output ครบ 10 layer
> สูตรเต็มรวมอยู่ §11 (Valuation Methodology) + §14 (tool registry) — pipeline อ้างถึง

---

## §4. P1 — Coverage Initiation

### (a) Workflow narrative

เริ่ม cover หุ้นใหม่ครั้งแรก — analyst อ่าน prospectus/56-1 (400-600 หน้า) + ศึกษาอุตสาหกรรม → สร้าง 3-statement model → valuation → เขียน thesis+catalyst+risk → compliance sign-off → publish initiation report 20-50+ หน้า ให้ลูกค้าสถาบัน · ความถี่: นานๆ ครั้ง · ทำโดย: Analyst (เจ้าของ coverage) + Associate (model)

### (b) L1 Task Graph — implementation-ready

**ขั้น 1 — Ingest & Primer**

- input: `{ "ticker": str, "filings": [{"doc_id": str, "type": enum[56-1,prospectus,annual], "url": str, "pub_date": date}], "industry_tag": str }`
- output: `{ "company_primer": {"business_model": str, "revenue_segments": [{"name": str, "pct": float}], "competitive_position": str}, "industry_map": {"tam": float, "growth_rate": float, "peers": [str]} }`
- actor: Primer-agent · seq · เวลา: วัน-สัปดาห์ · branch: `if filing_completeness < 0.8 → flag L3` · pain: prospectus 400-600 หน้า

**ขั้น 2 — Financial Modeling**

- input: `{ "ticker": str, "historical_financials": {"periods": [str], "IS": {}, "BS": {}, "CF": {}}, "primer": {...} }`
- output: `{ "three_statement_model": {"IS_forecast": {}, "BS_forecast": {}, "CF_forecast": {}}, "forecast_assumptions": {"revenue_growth": [float], "gross_margin": [float], "tax_rate": float}, "model_ties": bool }`
- actor: Model-agent + Verify-agent · seq · branch: `if model_ties == false → กลับแก้` · pain: model ต้อง balance (BS ต้อง tie, cash ต้องตรง)

**ขั้น 3 — Valuation & Rating**

- input: `{ "three_statement_model": {}, "peer_multiples": [{"ticker": str, "pe": float, "ev_ebitda": float}], "consensus": {"iaa_target": float, "n_analysts": int}, "current_price": float }`
- output: `{ "price_target": float, "rating": enum[Buy,Hold,Sell], "valuation_bridge": {"method": enum[comps,dcf], "comps_tp": float, "dcf_tp": float}, "expected_return": float, "consensus_deviation": float }`
- actor: Valuation-agent + Rating-agent · seq · branch: `if consensus_deviation > 0.15 → gate L3` + `if rating ไม่มี basis → กลับแก้`
- สูตร (ดู §11): `comps_tp = forward_EPS × justified_PE` · `expected_return = (TP − price + dividend)/price` · `consensus_deviation = |TP − iaa_target|/iaa_target`

**ขั้น 4 — Draft Report**

- input: `{ "valuation": {}, "primer": {}, "risks": [str] }`
- output: `{ "report_sections": {"exec_summary": str, "thesis": str, "catalysts": [str], "valuation": str, "risks": str, "esg": str, "disclosures": str}, "citations": [{"claim": str, "source_id": str}] }`
- actor: Draft-agent + Fact-checker · seq · pain: ต้องแยก fact/opinion, ทุก claim มี citation

**ขั้น 5 — Compliance Review + Sign-off**

- input: `{ "report_sections": {}, "citations": [], "rating": str, "target": float }`
- output: `{ "approved": bool, "reviewer_id": str, "override_notes": [str] }`
- actor: **Licensed Analyst (มนุษย์)** — hard gate บังคับ · branch: `if approved == false → กลับแก้`

**ขั้น 6 — Publish**

- input: `{ "approved_report": {}, "rating": str, "target": float }`
- output: `{ "published_url": str, "distribution_list": [str], "publish_ts": datetime }`
- actor: Publish-agent + sales

### (c) L2 Orchestration — implementation-ready

| ขั้น | Agent                              | pattern                      | input→output schema                     | quant tool (signature + สูตร)                                                                                           | debate pair                    | handoff                   |
| -------- | ---------------------------------- | ---------------------------- | ---------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- | ------------------------------ | ------------------------- |
| 1        | Primer-agent                       | Context-Augmentation         | filings[] → primer{}                    | —                                                                                                                          | Primer ↔ Checker              | primer{}                  |
| 2        | Model-agent                        | Prompt-Chaining (IS→BS→CF) | historical{} → model{}                  | `three_statement_engine(hist, assumptions) → {IS,BS,CF,ties:bool}` (คำนวณใน code)                                 | Model ↔ Verify (ตรวจ tie) | model{}                   |
| 3        | Valuation-agent, Rating-agent      | Orchestrator-Workers         | model{}+peers[]+consensus → {tp,rating} | `comps_engine(fwd_eps, peer_pe_median) → tp` ; `dcf_engine(fcff[], wacc, g) → tp` ; `rating_fn(exp_return) → enum` | Rating ↔ Basis-checker        | {tp,rating}               |
| 4        | Draft-agent                        | Prompt-Chaining              | valuation{} → sections{}                | —                                                                                                                          | Draft ↔ Fact-checker          | sections{}                |
| 5        | Compliance-agent →**human** | Evaluator-Optimizer          | sections{} → approved                   | —                                                                                                                          | Compliance ↔ human            | approved →**gate** |
| 6        | Publish-agent                      | Prompt-Chaining              | approved{} → published                  | —                                                                                                                          | —                             | published                 |

### (d) L0-L9 input/output — P1

| Layer              | input                           | ทำอะไร                                                                      | output                                         |
| ------------------ | ------------------------------- | --------------------------------------------------------------------------------- | ---------------------------------------------- |
| L0 Ingestion       | prospectus/56-1 PDF (สแกน)  | OCR+table extract+PIT tag                                                         | structured financials +`pub_date` ต่อ doc |
| L1 Task Map        | workflow spec P1                | รู้ 6 ขั้น                                                                 | task graph P1                                  |
| L2 Orchestration   | task graph + agent roster       | เดิน agent ต่อขั้น + เรียก quant                                  | handoff objects                                |
| L3 Human-Loop      | consensus_deviation, model_ties | gate ขั้น 3 (deviation>15%) + ขั้น 5 (บังคับ)                       | approved/override                              |
| L4 Memory          | ticker                          | ดึง note เก่า/ดีล sector เดียวกัน (ครั้งแรก = ว่าง) | prior context                                  |
| L5 Retrieval       | query จาก agent              | hybrid search peer/industry + citation-by-ID                                      | passages[] + ids                               |
| L6 Observability   | ทุก step                     | trace + number-level lineage                                                      | trace log + lineage map                        |
| L7 Governance+Eval | rating/target                   | บันทึก validation record                                                    | audit record                                   |
| L8 Schema Contract | ทุก handoff                  | บังคับ JSON schema (constrained decoding)                                   | validated object                               |
| L9 Routing         | ขั้น                        | primer/model→model ใหญ่ (ครั้งแรกงานหนัก)                     | model selection                                |

---

## §5. P2 — Earnings Update Cycle (ถี่สุด — demo หลัก)

### (a) Workflow narrative

ทุกครั้งบริษัทประกาศงบ (รายไตรมาส): analyst digest ผลประกอบการ + ฟัง earnings call → เทียบ actual vs ประมาณการเดิม/consensus → อัปเดต 3-statement model → ปรับ rating/TP → เขียน earnings note → compliance → publish (ด่วน — ลูกค้าอยากได้ทันที) · **ก่อน AI 5.7 ชม./บริษัท → 45 นาที (ลด 87%)** · ทำโดย Analyst+Associate

### (b) L1 Task Graph — implementation-ready

**ขั้น 1 — Digest Results + Earnings Call NLP**

- input: `{ "ticker": str, "earnings_release": {"doc_id": str, "pub_date": date, "actuals": {"revenue": float, "eps": float, "nim": float}}, "transcript": {"doc_id": str, "segments": [{"speaker": str, "role": enum[CEO,CFO,analyst], "text": str, "timestamp": str}]}, "prior_estimates": {"revenue": float, "eps": float} }`
- output: `{ "surprise": {"revenue_pct": float, "eps_pct": float}, "management_cues": [{"topic": str, "sentiment": enum[pos,neg,neutral], "quote_id": str}], "guidance_change": {"direction": enum[up,down,none], "detail": str} }`
- actor: Digest-agent · seq · branch: `if |eps_surprise| > 0.10 → flag material` · pain: earnings call 90 นาที
- สูตร: `eps_surprise_pct = (actual_eps − prior_est_eps)/prior_est_eps`

**ขั้น 2 — Update Model**

- input: `{ "existing_model": {}, "actuals": {}, "guidance_change": {} }`
- output: `{ "updated_model": {}, "revised_forecast": {"revenue_growth": [float], "eps": [float]}, "model_ties": bool }`
- actor: Model-agent + Verify · seq · branch: `if model_ties == false → แก้`

**ขั้น 3 — Re-value & Revise Rating**

- input: `{ "updated_model": {}, "peer_multiples": [], "consensus": {"iaa_target": float}, "current_price": float, "prior_rating": str }`
- output: `{ "new_target": float, "new_rating": enum[Buy,Hold,Sell], "rating_changed": bool, "consensus_deviation": float, "expected_return": float }`
- actor: Valuation-agent + Rating-agent · branch: `if consensus_deviation > 0.15 → gate` · `rating_changed == true` = สัญญาณสำคัญ (upgrade/downgrade มี information มากกว่า static)

**ขั้น 4 — Draft Earnings Note** (สั้นกว่า initiation)

- input: `{ "surprise": {}, "new_target": float, "management_cues": [], "thesis_update": str }`
- output: `{ "note": {"headline": str, "key_takeaways": [str], "estimate_revisions": {}, "rating_line": str}, "citations": [] }`
- actor: Note-agent + Fact-checker

**ขั้น 5 — Compliance** (เหมือน P1 ขั้น 5) · **ขั้น 6 — Publish** (ด่วน)

### (c) L2 Orchestration — implementation-ready

| ขั้น | Agent                              | pattern                                                    | tool (signature + สูตร)                                                                                                          | handoff                  |
| -------- | ---------------------------------- | ---------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------ |
| 1        | Digest-agent, Transcript-NLP-agent | Parallelization-sectioning (release + transcript ขนาน) | `surprise_fn(actual, prior) → pct` ; `transcript_nlp(segments) → {cues[], sentiment}` (diarize→NER→sentiment→extract facts) | surprise{}+cues[]        |
| 2        | Model-agent                        | Prompt-Chaining                                            | `three_statement_engine(model, actuals, guidance) → updated{}`                                                                    | updated_model{}          |
| 3        | Valuation-agent, Rating-agent      | Orchestrator-Workers                                       | `comps_engine` + `dcf_engine` (cross-check) ; `rating_fn(exp_return)` ; `consensus_dev_fn(tp, iaa)`                          | {target,rating}          |
| 4        | Note-agent                         | Prompt-Chaining                                            | —                                                                                                                                   | note{}                   |
| 5        | Compliance→human                  | Evaluator-Optimizer                                        | —                                                                                                                                   | approved→**gate** |
| 6        | Publish-agent                      | —                                                         | —                                                                                                                                   | published                |

### (d) L0-L9 — P2

| Layer | input                                            | ทำอะไร                                                                                                                                                                  | output                                         |
| ----- | ------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------- |
| L0    | earnings release PDF +**audio/transcript** | OCR +**transcript diarize+timestamp** + PIT tag (ใช้ได้หลัง pub_date)                                                                                         | structured actuals + speaker-tagged transcript |
| L1    | P2 spec                                          | 6 ขั้น                                                                                                                                                                    | task graph P2                                  |
| L2    | roster                                           | Digest+NLP ขนาน → model → rating                                                                                                                                        | handoffs                                       |
| L3    | eps_surprise, deviation                          | gate ถ้า material/deviation สูง + ขั้น 5 บังคับ                                                                                                               | approved                                       |
| L4    | ticker                                           | **forecast-error memory** — ดึงว่าเคยพลาด NIM/revenue บริษัทนี้ตรงไหน → ปรับ assumption                                               | error-adjusted prior                           |
| L5    | query                                            | time-aware retrieval (PIT — ห้ามดึงข้อมูลหลังวันประกาศ) + IAA consensus                                                                            | passages + consensus                           |
| L6    | steps                                            | trace + lineage ทุกเลขในโน้ต                                                                                                                                      | lineage                                        |
| L7    | target vs consensus vs realized                  | eval: เก็บ AI target เทียบ realized price ภายหลัง                                                                                                             | validation record                              |
| L8    | handoffs                                         | schema enforce                                                                                                                                                                | validated                                      |
| L9    | ขั้น                                         | **digest/model-update→model เล็ก (ถูก/เร็ว)** ; rating/thesis→model ใหญ่ + **semantic cache** (บริษัทเดิม ถามซ้ำช่วง season) | selection                                      |

---

## §6. P3 — Flash / Update Note

### (a) Workflow narrative

มีข่าว/event สำคัญนอกรอบงบ (M&A, เปลี่ยนผู้บริหาร, กฎหมาย, guidance ระหว่างไตรมาส) → analyst ออก flash note สั้นเร็ว บอกผลกระทบต่อ thesis/estimate · คุณค่า = **ความเร็ว** · บ่อยครั้งไม่แก้ตัวเลขมาก แค่ interpret

### (b) L1 Task Graph

**ขั้น 1 — Event Ingest & Impact Assess**

- input: `{ "ticker": str, "event": {"type": enum[M&A,mgmt,regulatory,guidance,other], "source_id": str, "pub_date": date, "text": str}, "current_thesis": str, "current_estimates": {} }`
- output: `{ "impact": {"thesis_affected": bool, "estimate_delta": {"eps_pct": float}, "rating_review_needed": bool}, "commentary": str }`
- actor: Flash-agent · branch: `if rating_review_needed → เข้า P2 ขั้น 3 (re-value)` else publish note

**ขั้น 2 — Draft Flash** → **ขั้น 3 — Compliance** → **ขั้น 4 — Publish (ด่วนสุด)**

- flash note output: `{ "headline": str, "event_summary": str, "impact_line": str, "rating_unchanged_or_new": str }`

### (c) L2 Orchestration

| ขั้น | Agent             | pattern                                         | tool                                              | handoff                  |
| -------- | ----------------- | ----------------------------------------------- | ------------------------------------------------- | ------------------------ |
| 1        | Flash-agent       | Routing (rating review ต้อง/ไม่ต้อง) | `impact_fn(event, thesis) → {affected, delta}` | impact{}                 |
| 2        | Note-agent        | Prompt-Chaining                                 | —                                                | flash{}                  |
| 3        | Compliance→human | Evaluator-Optimizer                             | —                                                | approved→**gate** |
| 4        | Publish-agent     | —                                              | —                                                | published                |

### (d) L0-L9 — P3

L0: ingest ข่าว/filing + PIT · L1: task graph P3 · L2: flash→note · **L3: gate เร็ว (บังคับ sign-off แม้ note สั้น)** · L4: ดึง thesis/estimate ปัจจุบันจาก memory · L5: retrieval ข่าวยืนยัน + citation · L6: lineage · L7: audit · L8: schema · **L9: งาน interpret เบา→model กลาง; cache ข่าว sector ซ้ำ**

---

## §7. P4 — Thematic / Industry Deep-Dive

### (a) Workflow narrative

วิเคราะห์ธีม/อุตสาหกรรมข้ามหลายบริษัท (เช่น "ผลกระทบดอกเบี้ยขาลงต่อกลุ่มไฟแนนซ์") → thought piece ยาว มี framework + หุ้นที่ได้/เสียประโยชน์ · เป็น long-form ใช้เวลา + วิจัยกว้าง

### (b) L1 Task Graph

**ขั้น 1 — Scope & Research**

- input: `{ "theme": str, "sector_scope": [str], "tickers_in_scope": [str] }`
- output: `{ "framework": {"drivers": [str], "hypothesis": str}, "evidence": [{"claim": str, "source_id": str}] }`

**ขั้น 2 — Cross-company Impact Analysis**

- input: `{ "framework": {}, "tickers_in_scope": [str], "models_by_ticker": {} }`
- output: `{ "winners": [{"ticker": str, "reason": str, "estimate_impact": float}], "losers": [{...}], "ranking": [str] }`
- tool: apply sensitivity ต่อ theme driver ข้ามหลาย model

**ขั้น 3 — Draft Thought Piece** → **ขั้น 4 — Compliance** → **ขั้น 5 — Publish**

### (c) L2 Orchestration

| ขั้น | Agent                               | pattern                                                                           | tool                                                       | handoff                  |
| -------- | ----------------------------------- | --------------------------------------------------------------------------------- | ---------------------------------------------------------- | ------------------------ |
| 1        | Research-agent                      | Context-Augmentation (ดึงข้อมูลกว้าง)                               | —                                                         | framework{}              |
| 2        | Impact-agent (worker ต่อ ticker) | **Orchestrator-Workers** (แตกงานต่อบริษัท) + Parallelization | `sensitivity_fn(model, driver_delta) → estimate_impact` | winners/losers           |
| 3        | ThoughtPiece-agent                  | Prompt-Chaining                                                                   | —                                                         | draft{}                  |
| 4        | Compliance→human                   | Evaluator-Optimizer                                                               | —                                                         | approved→**gate** |
| 5        | Publish-agent                       | —                                                                                | —                                                         | published                |

### (d) L0-L9 — P4

L0: ingest industry report/หลายบริษัท · L1: P4 graph · **L2: orchestrator-workers แตกต่อ ticker (เด่น)** · L3: gate ก่อน publish · **L4: ดึง theme/framework เก่าที่เคยเขียน** · L5: retrieval ข้ามบริษัท+macro · L6: lineage · L7: audit · L8: schema · **L9: วิจัยกว้าง→model ใหญ่; แต่ละ ticker worker→model กลาง ขนาน**

---

## §8. P5 — Model Maintenance

### (a) Workflow narrative

งานเบื้องหลังต่อเนื่อง: sync ราคาล่าสุด, ปรับ FX/ดอกเบี้ย/ราคาสินค้าโภคภัณฑ์ที่กระทบ input, roll forward งวด, เช็คโมเดลยัง tie · ไม่ผลิต report แต่ keep โมเดลพร้อมใช้ทุกเมื่อ (feed P2/P3)

### (b) L1 Task Graph

**ขั้น 1 — Refresh Inputs**

- input: `{ "ticker": str, "model_ref": str, "market_data": {"price": float, "fx": {}, "rates": {}, "commodity": {}}, "as_of": date }`
- output: `{ "refreshed_model": {}, "changed_cells": [{"cell": str, "old": float, "new": float}], "model_ties": bool }`
- branch: `if model_ties == false → flag L3` · `if drift > threshold → trigger re-value (P2 ขั้น 3)`

**ขั้น 2 — Consistency Check** → output `{ "anomalies": [{"cell": str, "issue": str}], "ok": bool }`

### (c) L2 Orchestration

| ขั้น | Agent             | pattern             | tool                                                                                               | handoff     |
| -------- | ----------------- | ------------------- | -------------------------------------------------------------------------------------------------- | ----------- |
| 1        | Refresh-agent     | Prompt-Chaining     | `three_statement_engine(model, new_inputs) → {model, ties}` ; `roll_forward_fn(model, as_of)` | refreshed{} |
| 2        | Consistency-agent | Evaluator-Optimizer | `anomaly_detect(model) → issues[]`                                                              | anomalies[] |

### (d) L0-L9 — P5

L0: ingest market data feed + PIT · L1: P5 graph · L2: refresh→check · **L3: gate เฉพาะเมื่อ anomaly/drift** (งาน routine ส่วนใหญ่ auto) · L4: จำ threshold/pattern anomaly บริษัทนี้ · L5: retrieval market data · L6: lineage cell-level (เด่น — ทุก cell รู้ที่มา) · L7: audit เปลี่ยนแปลง · L8: schema · **L9: งาน mechanical→model เล็กสุด/rule-based (ถูกสุด)**

---

## §9. P6 — Marketing & Client Service

> **AI role เบา** (งาน comms) — engine ช่วย prep ไม่ผลิต research artifact · ไม่มีสูตร valuation

### (a) Workflow narrative

analyst ทำ marketing งานวิจัย: จัด roadshow, corporate access (พาผู้บริหารเจอ buy-side), รับสาย buy-side ตอบคำถามเชิงลึก, เตรียม deck นำเสนอ · จุดประสงค์ = ดึง trading commission

### (b) L1 Task Graph

**ขั้น 1 — Prep Talking Points / Q&A**

- input: `{ "ticker_or_theme": str, "audience": enum[PM,analyst,corp], "published_research": [{"doc_id": str}], "likely_questions": [str] }`
- output: `{ "talking_points": [str], "anticipated_qa": [{"q": str, "a": str, "source_id": str}], "roadshow_deck_outline": [str] }`
- branch: `if question นอกเหนือ published basis → flag "ต้อง research เพิ่ม ห้ามเดา"` (กัน MNPI/บอกเกิน basis)

### (c) L2 Orchestration

| ขั้น | Agent            | pattern                                          | tool | handoff                              |
| -------- | ---------------- | ------------------------------------------------ | ---- | ------------------------------------ |
| 1        | Prep-agent       | Context-Augmentation (ดึง published research) | —   | talking_points{}                     |
| —       | Compliance-check | Guardrail (L5 output rail)                       | —   | ห้ามหลุด MNPI/เกิน basis |

### (d) L0-L9 — P6

L0: — (ใช้ published research ที่ ingest แล้ว) · L1: P6 graph · L2: prep-agent · **L3: human นำเสมอ (AI แค่ช่วย prep)** · L4: จำ FAQ/preference ลูกค้า · L5: retrieval published research เท่านั้น + **output rail กัน MNPI** · L6: trace · L7: audit (ใครถามอะไร) · L8: schema · **L9: งานเบา→model กลาง + cache Q&A ซ้ำ**

---

## §10-mid. P7 — Idea Generation / Morning Meeting

> **AI role เบา** — คัดกรอง/สรุป ไม่ผลิต artifact · ไม่มีสูตร valuation (ใช้ screening rule)

### (a) Workflow narrative

รายวัน: analyst หา idea (screen หุ้นเข้าเกณฑ์, จับ dislocation ราคา vs thesis), เข้า morning meeting เสนอ idea สั้นๆ ต่อ sales/trader · engine ช่วย screen + สรุป overnight news

### (b) L1 Task Graph

**ขั้น 1 — Overnight Digest & Screen**

- input: `{ "coverage_universe": [str], "overnight_news": [{"ticker": str, "source_id": str, "pub_date": date}], "screen_criteria": {"metric": str, "op": enum[gt,lt], "value": float} }`
- output: `{ "flagged_ideas": [{"ticker": str, "trigger": str, "note": str}], "morning_summary": str }`
- branch: `if idea = actionable → เสนอ morning meeting → อาจ trigger P3 flash`

### (c) L2 Orchestration

| ขั้น | Agent        | pattern                                   | tool                                           | handoff   |
| -------- | ------------ | ----------------------------------------- | ---------------------------------------------- | --------- |
| 1        | Screen-agent | Routing (คัดเข้า/ออกเกณฑ์) | `screen_fn(universe, criteria) → flagged[]` | flagged[] |
| 2        | Digest-agent | Prompt-Chaining (สรุป overnight)      | —                                             | summary   |

### (d) L0-L9 — P7

L0: ingest overnight news + PIT · L1: P7 graph · **L2: routing/screen (เด่น)** · L3: human ตัดสิน idea · L4: จำ idea ที่เคยเวิร์ค/ไม่เวิร์ค · L5: retrieval news + price · L6: trace · L7: audit · L8: schema · **L9: screen จำนวนมาก→model เล็กสุด (ถูก)**

---

## §11. Rating / Valuation Methodology — สูตรเต็ม (implementation-ready)

**หลัก: Comps/multiple + DCF cross-check** (หลักฐาน: **94.5% analyst ใช้ multiple, DCF แค่ 4%**; price-target hit rate DCF 52.3% vs revenue-multiple 55.1% → multiple แม่นกว่า/เท่า [tandfonline](https://www.tandfonline.com/doi/full/10.1080/23322039.2024.2423261))

### 11.1 Comps / Multiple (default)

- **P/E:** `P/E = price / EPS` → target: `TP = forward_EPS × justified_PE` (justified_PE = median/percentile ของ peer หรือ historical band)
- **EV/EBITDA:** `EV = price×shares + net_debt + minority + preferred` ; `EV/EBITDA = EV / EBITDA` → `implied_EV = target_EV/EBITDA × EBITDA` → bridge → equity value → /shares = TP
- **EV/EBIT, EV/Revenue:** เหมือนกัน เปลี่ยนตัวหาร
- **PEG:** `PEG = (P/E) / earnings_growth_pct` (ปรับ P/E ตามการเติบโต)
- peer set: เลือก 8-15 บริษัท → ใช้ **median + 25th-75th percentile** (ไม่ใช่ mean กัน outlier)
- ⚠️ ต้อง scrub: ตัด non-recurring, calendarize FY ต่างกัน, ปรับ operating lease (TFRS-16)

### 11.2 DCF (cross-check)

- **FCFF** = `EBIT×(1−tax) + D&A − capex − ΔNWC`
- **WACC** = `(E/V)×Ke + (D/V)×Kd×(1−tax)` ; E=equity, D=debt, V=E+D (market value)
- **Ke (CAPM)** = `Rf + β×ERP` ; Rf=risk-free, ERP=equity risk premium
- **Terminal value (Gordon)** = `FCFF_n×(1+g) / (WACC − g)` ; g ≤ long-run nominal GDP · TV มัก 60-80% ของ EV
- discount → PV → sum = EV → bridge: `equity = EV − net_debt − minority − preferred` → `TP = equity/shares`
- ⚠️ WACC ±1% → value ±~25% (high-growth) → sensitivity table WACC×g

### 11.3 3-statement forecast (feed valuation)

- revenue: `rev_t = rev_{t-1}×(1+growth_t)` · gross profit = rev×margin · เชื่อม IS→BS→CF (retained earnings, working capital, D&A, capex, debt)
- **หุ้นการเงิน (เช่น MTC):** `NIM = net_interest_income / avg_earning_assets` ; `net_interest_income = interest_income − interest_expense` — driver หลักแทน gross margin

### 11.4 Rating logic

- `expected_return = (TP − current_price + expected_dividend) / current_price`
- threshold (ปรับได้ต่อ house): `Buy if exp_return > +15%` · `Hold if −10% ≤ exp_return ≤ +15%` · `Sell if exp_return < −10%`
- **rating change (upgrade/downgrade) มี information มากกว่า static rating** → เป็น event สำคัญ

### 11.5 Quality/consistency metrics

- **Consensus deviation:** `dev = |AI_TP − IAA_consensus_TP| / IAA_consensus_TP` → `if dev > 0.15 → gate L3`
- **Forecast error (L4):** `MAPE = mean(|forecast − actual|/|actual|)` ; `bias = mean(forecast − actual)` (บวก=มองโลกสวยเกิน)

---

## §12. AI Pain Points + หลักฐานเต็ม

- **Earnings-season (จุดปวดหลัก):** manual **5.7 ชม./บริษัท → 45 นาที (ลด 87%)** — agent auto-generate earnings review ภายในนาทีหลัง filing, monitor live transcript ([marvin-labs](https://www.marvin-labs.com/solutions/earnings-season/))
- **ภาพรวม:** 5 core workflow กิน **70-80% เวลา analyst** → automate ลดงาน **40% / คืน 20-25 ชม./สัปดาห์** ([marvin-labs](https://www.marvin-labs.com/solutions/earnings-season/))
- **Coverage overload:** 50-60+ บริษัท/analyst + ต้อง publish ขั้นต่ำ/ไตรมาส → งานซ้ำปริมาณมาก
- **Earnings-call NLP:** pipeline fetch→clean→diarize→NER→sentiment→summarize→score; LLM ควร **extract facts ไม่ใช่แค่ sentiment** ([stockalpha](https://stockalpha.ai/alpha-learning/earnings-call-analysis-with-ai-extracting-insights-from-transcripts), [LSEG](https://www.lseg.com/en/insights/data-analytics/ai-unlock-investment-risk-management-opportunities-earnings-call-transcripts))
- **⚠️ Caveat (พูดตอน pitch):** general AI เคยสร้างตัวเลขปลอม ("43% vs actual 12%"), สร้าง IB chart ไม่ดี — hallucination จริง ต้อง human review เสมอ

---

## §13. Regulatory เต็ม (โยง L3 hard-gate)

- **MiFID II / Reg AC** — licensed analyst ต้อง review+sign-off ก่อนเผยแพร่ทุกฉบับ + audit trail + MNPI control · primary: **ESMA Article 52 MiFID II Delegated Regulation** (firm ต้องอธิบายขอบเขต instrument + analyst physically separated จากผู้มี conflict) ([esma.europa.eu](https://www.esma.europa.eu/sites/default/files/library/esma35-43-349_mifid_ii_qas_on_investor_protection_topics.pdf))
- **FINRA** — rating/target ต้องมี **"reasonable basis"** + อิสระจาก conflict of interest
- **CFA Institute Standard** — research ต้อง objective, **"reasonable and adequate basis"**, แยก fact/opinion ([CFA Institute](https://www.cfainstitute.org/sites/default/files/-/media/documents/support/research-challenge/challenge/rc-equity-research-report-essentials.pdf))
- **Thai:** IAA review รายงานก่อนขึ้น consensus · SEC Thailand analyst license
- **ผลต่อ design:** ทุกอย่างตรงกับ **L3 hard-gate** (ขั้น compliance บังคับ ห้าม AI เผยแพร่เอง) + L2 grounding/citation

---

## §14. 🔬 วิเคราะห์ทุก Layer L0-L9 — ER-specific mechanism ใหม่

| Layer        | mechanism ER-specific ใหม่                                                                                                  | ปัญหา ER ที่แก้                                  | เกณฑ์ | source                                                                                                                                                           |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------- | ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **L0** | transcript ingestion (diarize+timestamp) + oppday deck parser +**PIT tagging** (ทุก data มี pub_date)                | earnings call 90 นาที + งบสแกน + กัน lookahead | a,c        | [LSEG](https://www.lseg.com/en/insights/data-analytics/ai-unlock-investment-risk-management-opportunities-earnings-call-transcripts)                              |
| **L2** | **Consensus-deviation detector** — `if dev>15% → flag`                                                                | AI หลุดจาก street โดยไม่มีคนดู           | b,c        | [settrade IAA](https://www.settrade.com/th/research/iaa-consensus/main)                                                                                           |
| **L3** | MiFID/FINRA/IAA**hard-gate** + **projection-quality gate**                                                          | projection = แหล่ง error อันดับ 1 ใน ER        | c          | [CFA Institute](https://www.cfainstitute.org/sites/default/files/-/media/documents/support/research-challenge/challenge/rc-equity-research-report-essentials.pdf) |
| **L4** | **Forecast-error memory** (MAPE/bias ต่อบริษัท)                                                                  | AI พยากรณ์บริษัทเดิมพลาดซ้ำ         | b,d        | —                                                                                                                                                               |
| **L5** | **Time-aware retrieval (anti-lookahead/PIT)** + ER corpus (IAA consensus/price/peer/past note)                            | lookahead bias inflate 100-500bps                           | b,c        | [Look-Ahead-Bench](https://arxiv.org/pdf/2601.13770), [pfolio](https://www.pfolio.io/academy/look-ahead-bias)                                                      |
| **L6** | number-level lineage (ทุกเลขย้อนถึง cell งบ/บรรทัด transcript)                                             | defend every number ต่อ compliance                       | a,c        | —                                                                                                                                                               |
| **L7** | **ER gold-set eval** (AI TP vs IAA consensus vs realized price) + Look-Ahead-Bench                                        | เคลมแม่นแต่วัดไม่ได้                    | b,c        | [Look-Ahead-Bench](https://arxiv.org/pdf/2601.13770)                                                                                                              |
| **L8** | ER handoff JSON schema (ทุก object ใน §4-10)                                                                              | silent error ข้ามขั้น                               | b,c        | —                                                                                                                                                               |
| **L9** | cheap (digest/extract/model-update/screen→model เล็ก) vs expensive (rating/thesis→model ใหญ่) + cache earnings ซ้ำ | ต้นทุน/latency ตอน earnings season                 | c,d        | —                                                                                                                                                               |

---

## §15. Step-Level Task Graph L0-L9 — ภาพรวมข้ามทุก pipeline

| Layer | บทบาทใน ER (ภาพรวม)                            | input ทั่วไป   | output ทั่วไป        |
| ----- | ----------------------------------------------------------- | -------------------- | -------------------------- |
| L0    | แปลงเอกสารดิบ (งบ/transcript/deck) + PIT tag | PDF/audio/feed       | structured data + pub_date |
| L1    | เลือก pipeline (P1-P7) + รู้ขั้น                | workflow spec        | task graph                 |
| L2    | เดิน agent + เรียก quant + debate                  | task graph           | handoff objects            |
| L3    | gate (deviation/compliance บังคับ)                    | confidence/deviation | approved/override          |
| L4    | ดึง forecast-error + note เก่า                       | ticker               | prior context              |
| L5    | ค้น consensus/peer/price (time-aware)                    | query                | passages+ids               |
| L6    | trace + number lineage                                      | ทุก step          | audit trail                |
| L7    | eval (TP vs consensus vs realized) + audit                  | output               | validation record          |
| L8    | บังคับ schema ทุก handoff                          | object               | validated object           |
| L9    | เลือก model ตามงาน + cache                       | task                 | model selection            |

---

## §16. Engine Layer Input Map — ER (ป้อนอะไรเข้าแต่ละ layer)

| Layer | ER ป้อนอะไรเข้า                                                                              |
| ----- | -------------------------------------------------------------------------------------------------------- |
| L0    | 56-1/annual report (สแกน), earnings release,**earnings call transcript/audio**, oppday deck    |
| L1    | workflow spec P1-P7 (7 pipeline)                                                                         |
| L2    | agent roster ต่อ pipeline (§4-10 บล็อก c)                                                       |
| L3    | gate rule: consensus_deviation>15%, projection-quality, MiFID/IAA sign-off บังคับ                  |
| L4    | forecast-error history ต่อบริษัท, analyst preference, past note                                 |
| L5    | corpus:**IAA Consensus**, historical price, peer financials, past published notes (time-aware/PIT) |
| L6    | lineage requirement: ทุกเลขในรายงานย้อนถึง source                                   |
| L7    | gold-set: AI TP/rating เทียบ IAA consensus + realized price                                         |
| L8    | JSON schema ทุก handoff object (§14 master schema)                                                   |
| L9    | routing rule: digest/screen→เล็ก, rating/thesis→ใหญ่; cache earnings ซ้ำ                    |

---

## §17. Output — ER Report Structure (CFA Research Challenge format)

รายงานมาตรฐานที่จูจ CFA รู้จัก — engine ผลิตตามโครงนี้:

1. **Executive Summary** + recommendation + price target
2. **Investment Thesis** + catalysts (near/long-term)
3. **Business Description**
4. **Industry Analysis** (competitive positioning)
5. **Financial Analysis**
6. **Valuation** (comps หลัก + DCF cross-check, football field)
7. **Risk Factors**
8. **ESG Considerations**
9. **Disclosures & Disclaimers**

> **projection quality = แหล่ง error อันดับ 1** ([CFA Institute](https://www.cfainstitute.org/sites/default/files/-/media/documents/support/research-challenge/challenge/rc-equity-research-report-essentials.pdf)) → นี่คือเหตุผลวาง projection-quality gate (L3) + forecast-error memory (L4)

---

## §18. Master Schema + Tool Registry (implementation-ready — เปิดหน้าเดียวเห็นครบ)

### 18.1 Core JSON objects (handoff ข้าม pipeline)

```json
// FinancialsActual
{ "ticker": "str", "period": "str", "pub_date": "date(PIT)",
  "revenue": "float", "eps": "float", "ebitda": "float", "nim": "float?" }

// ThreeStatementModel
{ "ticker": "str", "IS": {}, "BS": {}, "CF": {},
  "forecast_assumptions": {"revenue_growth": ["float"], "margin": ["float"], "tax_rate": "float"},
  "model_ties": "bool" }

// ValuationResult
{ "ticker": "str", "price_target": "float", "rating": "enum[Buy,Hold,Sell]",
  "method_primary": "comps", "comps_tp": "float", "dcf_tp": "float",
  "expected_return": "float", "consensus_deviation": "float",
  "citations": [{"claim": "str", "source_id": "str"}] }

// ResearchNote
{ "ticker": "str", "type": "enum[initiation,earnings,flash,thematic]",
  "sections": {"exec_summary": "str", "thesis": "str", "catalysts": ["str"],
               "valuation": "str", "risks": "str", "esg": "str", "disclosures": "str"},
  "rating": "str", "target": "float", "approved_by": "str(licensed_analyst_id)" }

// TranscriptSignal
{ "ticker": "str", "management_cues": [{"topic": "str", "sentiment": "enum[pos,neg,neutral]", "quote_id": "str", "timestamp": "str"}],
  "guidance_change": {"direction": "enum[up,down,none]", "detail": "str"} }
```

### 18.2 Tool registry (quant — คำนวณใน code ไม่ให้ LLM เดา)

| tool                       | signature                                  | สูตรหลัก                         |
| -------------------------- | ------------------------------------------ | ---------------------------------------- |
| `three_statement_engine` | `(hist, assumptions) → {IS,BS,CF,ties}` | เชื่อม IS→BS→CF, ties check      |
| `comps_engine`           | `(fwd_eps, peer_multiples) → tp`        | `tp = fwd_eps × median(peer_pe)`      |
| `dcf_engine`             | `(fcff[], wacc, g) → tp`                | PV(FCFF)+TV, TV=`FCFFn(1+g)/(wacc−g)` |
| `wacc_fn`                | `(E,D,Ke,Kd,tax) → wacc`                | `E/V·Ke + D/V·Kd·(1−tax)`          |
| `capm_fn`                | `(rf,β,erp) → Ke`                      | `rf + β·erp`                         |
| `rating_fn`              | `(exp_return) → enum`                   | threshold Buy>15%/Sell<−10%             |
| `consensus_dev_fn`       | `(tp, iaa_tp) → dev`                    | `dev = abs(tp - iaa_tp) / iaa_tp` |
| `surprise_fn`            | `(actual, prior) → pct`                 | `(actual−prior)/prior`                |
| `transcript_nlp`         | `(segments) → {cues[],guidance}`        | diarize→NER→sentiment→extract facts   |
| `forecast_error_fn`      | `(forecast[], actual[]) → {mape,bias}`  | `mape=mean(\|f−a\|/\|a\|)`                |
| `screen_fn`              | `(universe, criteria) → flagged[]`      | filter ตามเกณฑ์                  |

---

## §19. Grading Criteria Mapping

| ER technique/feature                                            | เกณฑ์ที่ได้                               |
| --------------------------------------------------------------- | ---------------------------------------------------- |
| public data 100% (filing/IAA/price) — no PDPA                  | **c** (feasibility สูงสุด)               |
| earnings-season 5.7hr→45min, คืน 20-25 ชม./สัปดาห์ | **d** (impact วัดได้)                    |
| 7 pipeline ครบ + implementation-ready spec                   | **b** (solution ลึก น่าเชื่อถือ) |
| comps-primary (94.5% analyst, accuracy 55.1%)                   | **a+b** (อิงหลักฐานจริง)         |
| Thai IAA consensus + oppday + SEC license                       | **a** (เชื่อมอุตสาหกรรมไทย) |
| MiFID/FINRA/IAA hard-gate + projection-quality gate             | **c** (regulatory-aware)                       |
| anti-lookahead/PIT + gold-set eval                              | **b+c** (แม่น + วัดได้)              |
| number-level lineage (defend every number)                      | **c** (ตรวจสอบได้)                   |

---

## §20. Gaps (ต้องตัดสิน/หาต่อ)

- **company universe เคาะแล้ว:** MSFT + AMZN + PTT เป็น current public-data fixture set สำหรับ smoke/demo. Runtime ยังออกแบบให้ company-agnostic แต่ Step 3 ไม่ต้องหา proxy ticker ใหม่.
- **provider-native historical aggregate consensus:** public evidence pack ใช้ dated source/broker-backed reference ได้สำหรับ demo; ถ้าจะเคลม production consensus feed ต้องใช้ FactSet/Bloomberg/Visible Alpha/LSEG/SETSMART หรือ manual licensed export.
- **AMZN full Q&A transcript:** release/slides พอสำหรับ numeric P2 demo; ถ้าจะโชว์ deep tone/Q&A NLP ต้อง licensed transcript หรือ manual transcript จาก official replay.
- **rating threshold (Buy>15%?)** — ใช้เป็น MVP default ได้ แต่ต้องแยกเป็น configurable house policy และ calibrate ด้วย eval หลัง runtime มี output จริง.
- **SEC Thailand analyst license / compliance wording** — สำหรับ demo ให้พูดว่า human licensed analyst sign-off เป็น hard gate; ห้ามเคลมว่า AI publish research ได้เอง.
- **demo/build scope:** ทำ P2 จริงบน MSFT + AMZN + PTT; P1/P3-P7 โชว์เป็น breadth/expansion story.

---

## §21. Sources (เว็บเท่านั้น)

**ER profession / workflows:**

- Sell-side analyst day-to-day — https://www.wallstreetoasis.com/resources/careers/jobs/sell-side-analysts
- Buy vs sell-side — https://www.wallstreetprep.com/knowledge/sell-side-vs-buy-side-equity-research/
- Buy vs sell-side detailed — https://mergersandinquisitions.com/buy-side-vs-sell-side-equity-research/

**Rating/valuation methodology:**

- Target price accuracy (94.5% multiples, DCF 52.3% vs 55.1%) — https://www.tandfonline.com/doi/full/10.1080/23322039.2024.2423261
- Analyst ratings/price target — https://pro.stockalarm.io/blog/analyst-ratings-guide

**Earnings-call NLP:**

- AI earnings call analysis — https://stockalpha.ai/alpha-learning/earnings-call-analysis-with-ai-extracting-insights-from-transcripts
- LSEG earnings transcript AI — https://www.lseg.com/en/insights/data-analytics/ai-unlock-investment-risk-management-opportunities-earnings-call-transcripts

**Lookahead bias / PIT:**

- Look-ahead bias — https://www.pfolio.io/academy/look-ahead-bias
- Look-Ahead-Bench (arxiv) — https://arxiv.org/pdf/2601.13770
- Point-in-time backtesting — https://sharpely.in/blog/bias-free-backtesting-explained:-how-sharpely-uses-point-in-time-data-to-avoid-look-ahead-and-survivorship-bias

**Thai context:**

- IAA Consensus (SETTRADE) — https://www.settrade.com/th/research/iaa-consensus/main
- IAA Thailand — https://www.iaathai.org/

**CFA / report structure:**

- CFA Research Challenge Report Essentials — https://www.cfainstitute.org/sites/default/files/-/media/documents/support/research-challenge/challenge/rc-equity-research-report-essentials.pdf
- Equity research report format — https://www.wallstreetprep.com/knowledge/sample-equity-research-report/

**AI pain evidence:**

- Marvin Labs earnings-season (5.7hr→45min) — https://www.marvin-labs.com/solutions/earnings-season/

**Regulatory:**

- ESMA MiFID II Q&A (Art.52) — https://www.esma.europa.eu/sites/default/files/library/esma35-43-349_mifid_ii_qas_on_investor_protection_topics.pdf
