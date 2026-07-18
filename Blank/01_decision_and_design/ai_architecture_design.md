# AI Architecture Design — ให้ทีม Finance

### Generic Finance Agent Engine + Human-in-the-Loop (flagship demo: Sell-side Equity Research P2)

> เป้าหมายเอกสาร: ทีม finance เห็นโครงหลักของ engine กลาง แล้วเข้าใจว่า **demo/build รอบ hackathon = Sell-side Equity Research P2: Earnings Update Cycle** ส่วนสายงานอื่นเป็น expansion story ที่เสียบเข้า engine เดียวกันได้ภายหลัง

---

## 1. Concept 1 ประโยค

สร้าง **engine กลาง** ที่รับข้อมูลของสายงาน → agent หลายตัวทำงานตาม **framework จริงของสายนั้น** → ส่ง output ให้คนตรวจ/เติม → **loop** ต่อจนได้งานดีสุด
(AI ทำ framework แทนงาน, คนกำกับเป็นระยะ, ทุกก้าวตรวจสอบได้)

---

## 2. เส้นแบ่งสำคัญ: อะไรคงที่ / อะไรทีมเสียบ

**🔵 ENGINE (คงที่ทุกสาย — ทีม tech ทำ):**
10 layer (L0-L9 ในข้อ 3) + รับประกันคุณภาพเหมือนกันหมดทุกสาย

1. **Grounding + Citation** — ทุก output อ้างอิงกลับ source
2. **Debate (maker/checker)** — agent เถียงกันกันเตือนผิด/bias
3. **Verify** — ตรวจเลข AI vs source, flag ความมั่นใจต่ำ
4. **Eval** — วัด precision/recall กับ gold-set
5. **Human-in-Loop + State** — gate ให้คนตรวจ, จำข้าม loop

**🟠 SECTOR PLUG (เปลี่ยนต่อสาย — ทีม finance หา):**

1. Workflow steps — สายนั้นทำงานกี่ขั้น
2. Quant/Math framework — สูตร/model ที่สายนั้นใช้
3. Input data — ใช้ข้อมูลอะไร
4. Gate points — ขั้นไหนคนต้องตรวจ

→ **ทีม finance โฟกัสแค่ 🟠 — engine 🔵 จัดการให้**

**Flagship demo ที่ล็อกสำหรับ hackathon:**  
ใช้ Equity Research P2 เป็น plug หลัก: งบประกาศ → digest + earnings-call NLP → update model → re-value/rating → earnings note → compliance gate → publish. เหตุผลคือ scope สั้นพอ build จริง, มีตัวชี้วัด before/after ชัด, และโยงเกณฑ์คะแนนเรื่อง problem, AI solution, feasibility, impact ได้ครบ.

---

## 3. โครงสร้าง 10 Layer (L0-L9)

```
╔═══════════════════════════════════════════════════╗
║ ENGINE 🔵 (คงที่ทุกสาย)                            ║
╠═══════════════════════════════════════════════════╣
║ PRE-PROCESS (ก่อนเริ่มงาน)                         ║
║  L0 INGESTION       OCR+table extract+normalize    ║  ← แก้ Thai DBD PDF
╠═══════════════════════════════════════════════════╣
║ CORE (เดินงาน)                                     ║
║  L1 TASK MAP        สายงาน→ขั้น 1..N→งานแต่ละขั้น  ║  ← 🟠 finance นิยาม
║  L2 ORCHESTRATION   agent+quant+debate+self-consist║
║  L3 HUMAN-LOOP+STATE gate + คนเติม + re-run        ║
╠═══════════════════════════════════════════════════╣
║ CROSS-CUTTING (ครอบทุกขั้น)                        ║
║  L4 MEMORY          จำข้ามดีล/ข้ามรอบ+เรียนจากคนแก้║
║  L5 GUARDRAIL+RETRIEVAL  rail + hybrid search+rerank║
║  L6 OBSERVABILITY   trace ทุก step + data lineage  ║
║  L7 GOVERNANCE+EVAL model inventory+audit+eval harn║
║  L8 SCHEMA CONTRACT บังคับ JSON schema ทุก handoff  ║
║  L9 ROUTING+CACHING เลือก model ตามงาน + cache     ║
╚═══════════════════════════════════════════════════╝
```

> **หมายเหตุ performance:** โครง engine ปัจจุบันใช้ **10 layer (L0-L9)** โดยเพิ่ม L0 (Ingestion), L8 (Schema Contract), L9 (Routing & Caching) และ upgrade L2/L3/L4/L5/L6/L7 ด้วยเทคนิค 2026 ที่ดัน accuracy สูงสุด (ดูหัวข้อ "Performance Engineering" ท้ายเอกสาร)

### L0 — Ingestion & Document Intelligence *(ใหม่ — แก้ปัญหา Thai DBD โดยตรง)*

ก่อน AI ทำงาน ต้องแปลงเอกสารดิบให้เป็น data ที่ใช้ได้ก่อน:

- **Layout-preserving OCR + table-aware chunking + structure-preserving parse** — งบการเงินไทยที่ยื่น DBD เป็น **PDF สแกนภาษาไทย** (ตารางเยอะ) — เทคนิคนี้ดึงตารางโดยรักษาโครงสร้าง (column/row/merged cell) ได้ **field accuracy 95-99%** ลดเวลาแกะมือ 85-95%
- **Deterministic normalization** — กฎ SET-vs-Capital-IQ / TFRS-16 lease (ที่ทำ EV/EBITDA เพี้ยน) เขียนเป็น **rule ใน code ไม่ให้ LLM เดา** → เลขตรงเสมอ
- ⚠️ scanned PDF คุณภาพต่ำ (เอียง/เบลอ) ทำ accuracy ตก — ต้องมี confidence flag ส่งต่อ L3

> 🧒 **ภาษาง่าย:** เหมือนแปลรูปถ่ายเมนูอาหารเป็นข้อความก่อนทำครัว — ถ้าอ่านรูปผิดตั้งแต่แรก อาหารก็ผิดทั้งจาน layer นี้คือทำให้ "อ่านรูปให้แม่นก่อน" โดยเฉพาะตารางตัวเลขที่เครื่องอ่านง่ายพลาด

### L1 — Task Map  *(🟠 finance นิยาม)*

สายงาน → ขั้นที่ 1..N → "แต่ละขั้นทำงานอะไร" · engine อ่าน spec นี้แล้วรู้ว่ามีกี่ขั้น

> 🧒 **ภาษาง่าย:** เหมือนเขียน "สูตรอาหาร" ก่อนทำครัว — บอกว่าทำอาหารจานนี้ต้องทำกี่ขั้นตอน แต่ละขั้นตอนทำอะไร (หั่นผัก → ผัด → ปรุงรส) พอเขียนสูตรเสร็จ ใครมาทำก็ทำตามสูตรได้เลย ไม่ต้องคิดใหม่ทุกครั้ง

### L2 — Agent Orchestration

แต่ละขั้นมี agent(1+) ทำงาน + เรียก **quant model** ถ้ามี · agent เถียงกัน (maker/checker debate) ก่อนออกจากขั้น · orchestrator เดินตาม flow

**⚡ Performance techniques (เพิ่มปี 2026 ดัน accuracy):**

- **Self-consistency / N-best disagreement** — ให้ agent ตอบหลายครั้ง (sample N) แล้ววัดว่าตรงกันไหม → ถ้าเถียงกันเอง = สัญญาณ "ไม่มั่นใจ" ที่เชื่อถือสุดในปี 2026 → ส่งเข้า human gate (L3)
- **Best-of-N reranking** — สร้างคำตอบ N ตัว เลือกตัวที่ **faithful กับ source สุด** ด้วย factuality metric เบาๆ → ลด error โดยไม่ต้อง retrain
- **Self-RAG reflection loop** — agent สร้างคำตอบ → ดึง source มาตรวจตัวเอง → refine ก่อนส่ง

> 🧒 **ภาษาง่าย:** เหมือนมี "ทีมงาน" ตัวจิ๋วหลายคนช่วยกันทำงานคนละขั้น แต่ละคนถนัดคนละอย่าง (คนหนึ่งเก่งอ่านงบ อีกคนเก่งคำนวณ) ทำเสร็จแล้วต้อง "เถียงกันเช็คงาน" ก่อนส่งต่อ — และให้ลองทำหลายรอบ ถ้าได้คำตอบไม่ตรงกันแปลว่ายังไม่ชัวร์ ต้องส่งให้คนดู

### L3 — Human-Loop + State

gate ขั้นสำคัญ → คนตรวจ/เติม → เขียนลง **state** · แก้ขั้นไหน re-run จากตรงนั้นลงล่าง (incremental, ขั้นที่ผ่านแล้วไม่ทำซ้ำ)

**⚡ Confidence-calibration routing (เพิ่มปี 2026):** LLM มักมั่นใจเกินจริง (over-confident) — engine ไม่รอแค่ gate ที่ตั้งไว้ แต่**คำนวณ confidence จาก self-consistency (L2)** → ถ้าต่ำ/agent เถียงกันหนัก → **auto-route ให้คนดูทันที** (ไม่ปล่อยผ่าน) · ถ้ามั่นใจต่ำมากจริงๆ ให้ **abstain** (บอก "ไม่ชัวร์" แทนเดา)

**⚡ Cross-agent state-consistency:** ทุก agent อ่าน **state snapshot เดียวกัน** (version เดียว) — กัน agent ขั้นหลังอ่านค่าเก่าที่คนแก้ไปแล้ว (เช่น คนปรับ WACC ที่ gate แล้ว agent ถัดไปยังใช้ค่าเดิม = เลขไม่ตรงกันทั้งเอกสาร)

> 🧒 **ภาษาง่าย:** เหมือนทำการบ้านเป็นข้อๆ ครูตรวจให้ผ่านก่อนค่อยทำข้อต่อไป ถ้าข้อ 2 ผิด แก้แค่ข้อ 2 แล้วทำข้อ 3 ต่อ — และถ้า AI รู้สึกว่าข้อไหน "ไม่ชัวร์" มันจะยกมือถามคนเองก่อน แทนที่จะเดาแล้วส่งเลย

### L4 — Memory *(ใหม่)*

จำ **ข้ามดีล/ข้ามรอบ** (ต่างจาก State ที่จำแค่ดีลนี้)

- ดีลคล้ายในอดีต → ดึงมาเทียบ ("SaaS ตัวนี้ margin ต่ำกว่าดีลเก่าที่เคยเจอ")
- preference ผู้ใช้ (analyst ชอบ WACC conservative) → ไม่ต้องบอกซ้ำ
- ยิ่งใช้ยิ่งเก่ง
- **⚡ Active-learning จาก human override (เพิ่มปี 2026):** ทุกครั้งที่คนแก้ AI ที่ gate (บันทึกใน L7 อยู่แล้ว) — เอา override นั้นกลับมาเป็น **preference data** สอน engine แบบ RLTHF (targeted human feedback): งานวิจัยพบใช้แรงคน annotate แค่ **6-7% ของ full annotation** ก็ได้ alignment เทียบเท่า → engine "เก่งขึ้นจากการถูกแก้" ไม่ใช่แค่จดไว้เฉยๆ (เป็น design choice แบบ offline/batch — ไม่ใช่เรียนสดใน call เดียว)
- ⚠️ เห็นผลชัดตอนใช้จริงระยะยาว — ใน demo รอบเดียวขายเป็น "vision ตอน scale"

> 🧒 **ภาษาง่าย:** เหมือนเพื่อนที่เคยช่วยติวหนังสือให้เรามาหลายเทอม พอเทอมนี้เจอโจทย์คล้ายเก่า เพื่อนจะจำได้ทันทีว่า "ข้อแบบนี้เคยทำผิดตรงไหน" ไม่ต้องเริ่มสอนใหม่จากศูนย์ทุกครั้ง — ยิ่งช่วยกันนาน เพื่อนคนนี้ยิ่งเข้าใจนิสัยเรามากขึ้น (State คือจำแค่ "ข้อสอบวันนี้" ส่วน Memory คือจำ "ทั้งเทอม")

### L5 — Guardrail Rails *(ใหม่)*

3 rail กันปัญหา + **retrieval quality** (เพิ่มปี 2026 = ตัวดัน accuracy สูงสุดตัวเดียว)

- **input rail** — กัน prompt-injection (เอกสาร data room อาจแฝงคำสั่งหลอก AI)
- **output rail** — คุมรูปแบบ/policy คำตอบก่อนส่งออก
- **retrieval rail (ACL)** — คุมให้ดึงแต่ data ที่อนุญาต
- **⚡ Retrieval quality (ใหม่):**
  - **Hybrid search (BM25 + dense)** + **cross-encoder reranker** — ค้นแบบ 2 ชั้น (ดึงกว้างก่อน → rerank ให้ตรงสุด) = ตัวเพิ่ม retrieval accuracy มากสุด **ลด hallucination ได้เกือบครึ่ง**
  - **Strict citation-by-ID contract** — ทุกประโยคที่อ้างข้อเท็จจริง **ต้องชี้ passage ID** ที่ดึงมา ถ้าไม่มี ID = ไม่ให้พูด → ตัดมั่วลอยๆ
- อ้างอิง OWASP LLM Top-10 2025

> 🧒 **ภาษาง่าย:** เหมือน "รั้วกั้น" รอบสนามเด็กเล่น — กันของแปลกปลอม (คำสั่งหลอก), เช็คของก่อนส่งออก, กันหยิบของต้องห้าม — **บวกกับ "บรรณารักษ์เก่งๆ"** ที่หาหน้าหนังสือที่ตรงคำถามที่สุดมาให้ และบังคับว่า "พูดอะไรต้องชี้หน้าที่เอามา" ห้ามพูดลอยๆ

### L6 — Observability / Trace *(ใหม่)*

บันทึกทุก step: agent ไหนทำอะไร ใช้ data ไหน ตัดสินใจยังไง ใช้ token เท่าไหร่ (มาตรฐาน OpenTelemetry)

- **demo:** เปิดโชว์ "เส้นทางความคิด" AI ให้จูจดู ไม่ใช่กล่องดำ
- **debug:** AI ผิดตรงไหน เปิด trace ดูได้
- **⚡ Data lineage ระดับตัวเลข (เพิ่มปี 2026):** จาก trace ระดับ step → ลึกถึง **ทุกตัวเลขใน output ย้อนได้ถึง cell ต้นทางในงบ** ("defend every number") — มาตรฐานที่สถาบันการเงินใช้ปกป้องทุกตัวเลขที่รายงานต่อ auditor/regulator: คลิกตัวเลขไหนก็เห็นว่ามาจากไฟล์ไหน หน้าไหน ผ่านการแปลงอะไรบ้าง
- เป็นวัตถุดิบของ audit trail ใน L7

> 🧒 **ภาษาง่าย:** เหมือนติดกล้องวงจรปิดไว้ทุกจุดในครัว — ถ้าอาหารออกมาไม่อร่อย เปิดกล้องย้อนดูได้เลยว่าพลาดตรงไหน (ใส่เกลือเยอะไปตอนไหน) ไม่ต้องเดา และถ้ามีคนมาถามว่า "ทำไมอาหารจานนี้ถึงเป็นแบบนี้" ก็เปิดกล้องให้ดูได้ทันที ไม่ใช่บอกว่า "จำไม่ได้"

### L7 — Governance + Eval (SR 26-2 risk-based reference) *(differentiator)*

ทำให้ engine "ผ่าน model-risk review ของ regulator" ได้ ไม่ใช่แค่ demo สวย

- **model inventory** — ทะเบียน model/agent ทุกตัวที่ใช้
- **validation record** — บันทึกว่าแต่ละ model ตรวจสอบแล้ว
- **monitoring threshold + drift** — เฝ้าระวังคุณภาพเมื่อเวลาผ่าน
- **documented human-override** — บันทึกทุกครั้งที่คนแก้ AI · **⚡ และไม่ใช่แค่ audit — override record ป้อนกลับเป็น training signal ให้ L4 (active-learning) → ยิ่งถูกแก้ ยิ่งเก่ง**
- **examiner audit trail** — ผู้ตรวจย้อนดูได้ทุกการตัดสินใจ
- **⚡ Eval harness (เพิ่มปี 2026 — เดิมเป็นแค่แนวคิด ตอนนี้ทำจริง):** วัดคุณภาพ engine เป็นตัวเลข ไม่ใช่แค่เคลม
  - **Faithfulness score** — output ตรงกับ source แค่ไหน (%)
  - **Gold-set** — ชุดคำตอบมาตรฐานที่คนตรวจแล้ว เทียบ precision/recall
  - **Tool-calling / trajectory eval** — agent เรียก quant tool ถูกตัว/ถูกลำดับไหม
  - **LLM-as-judge (calibrated)** — ใช้ AI ตรวจ AI แต่ปรับให้ไม่มั่นใจเกินจริง
  - → ผลทั้งหมดเก็บเป็น **validation record** (ตอบ regulator ได้ว่า "วัดแล้ว ได้เท่านี้")
- อ้างอิง current US interagency model-risk guidance **SR 26-2** ซึ่ง supersede SR 11-7 เมื่อ 2026-04-17; ใช้เป็น professional reference ไม่ได้เคลมว่า hackathon MVP เป็น regulated bank model ([Federal Reserve SR 26-2](https://www.federalreserve.gov/supervisionreg/srletters/SR2602.htm))

> 🧒 **ภาษาง่าย:** เหมือนโรงเรียนที่ต้องมี "ทะเบียนนักเรียน" ครบทุกคน มีสมุดพกบันทึกผลการเรียนของแต่ละคน มีระบบเช็คว่าใครเกรดตกต้องรีบดูแล มีบันทึกทุกครั้งที่ครูแก้คะแนนให้นักเรียน (บอกเหตุผลด้วย) และถ้าผู้ตรวจสอบจากกระทรวงมาขอดู ก็เปิดสมุดให้ดูได้ทุกหน้า — นี่คือสิ่งที่ทำให้โรงเรียน (หรือ AI) "น่าเชื่อถือพอให้คนภายนอกมาตรวจได้" ไม่ใช่แค่ "บอกว่าดี" ลอยๆ

### L8 — Schema Contract *(ใหม่ — บังคับรูปแบบทุกจุดส่งต่อ)*

ทุกจุดที่ agent ส่งงานต่อกัน + ทุกครั้งที่ agent เรียก quant tool **บังคับ JSON schema ด้วย constrained decoding** (ตัวถอดรหัสบังคับให้ output ตรง schema เสมอ ไม่ใช่แค่ขอร้อง):

- ปัญหาจริง: ถ้าไม่บังคับ — LLM ตอบ JSON พังโครงสร้าง **8-15% ของ call** (วิเคราะห์จาก 2 ล้าน API call) → บังคับแล้วเหลือ **<0.1%**
- ทุก provider หลักรองรับ native แล้ว (OpenAI Structured Outputs, Anthropic tool use, Gemini schema)
- แก้ปัญหา **"silent error ไหลข้ามขั้น"** — handoff object อย่าง `{adjusted_EBITDA, red_flag_severity}` ถ้า field หายเงียบๆ ขั้นถัดไปคำนวณบนข้อมูลไม่ครบโดยไม่มีใครรู้
- ค่า overhead แค่ 30-300 token ต่อ call — ถูกกว่า retry (แต่ละ fail = cost ×2 + latency 500-2,000ms)

> 🧒 **ภาษาง่าย:** เหมือนฟอร์มราชการที่ "บังคับกรอกครบทุกช่องถึงจะส่งได้" — ไม่ใช่กระดาษเปล่าที่ใครเขียนตกหล่นก็ส่งผ่านไปเงียบๆ แล้วไปพังเอาข้างหน้า ทุกใบที่ส่งต่อระหว่างทีมจิ๋วต้องครบช่องเสมอ

### L9 — Model Routing & Caching *(ใหม่ — ใช้จริงได้เชิงต้นทุน)*

เลือก "ขนาด model ให้เหมาะกับงาน" + จำคำตอบที่เคยตอบแล้ว:

- **Hybrid route-then-cascade** — งานง่าย (extract field, format) → model เล็ก/ถูก; งานยาก/confidence ต่ำ (valuation judgment) → model ใหญ่ · ผลจริง: **ลด cost 45-85% โดยคง quality ~95%**
- **Semantic caching** — คำถามซ้ำ/ใกล้เคียงดึงจาก cache: latency ลด **3.4 เท่า** (near-duplicate) ถึง **123 เท่า** (ตรงเป๊ะ), cost รวมลดได้ 60%+ ใน workload ที่ query ซ้ำสูง (เช่น earnings season ถามงบบริษัทเดิมซ้ำๆ)
- ผูกกับ L3: cascade ใช้ confidence จาก self-consistency ตัดสินว่า escalate ขึ้น model ใหญ่เมื่อไหร่
- **ทำไมสำคัญกับเกณฑ์ feasibility (c):** engine ที่แม่นแต่แพงเกิน = ใช้จริงไม่ได้ — layer นี้ทำให้ตอบ "ต้นทุนต่อดีล/ต่อรายงาน" ได้จริง

> 🧒 **ภาษาง่าย:** เหมือนร้านซ่อมที่ไม่เรียกวิศวกรใหญ่มาเปลี่ยนหลอดไฟ — งานเล็กให้ช่างทั่วไปทำ (ถูกกว่า เร็วกว่า) งานยากค่อยส่งผู้เชี่ยวชาญ และถ้าเคยตอบคำถามนี้แล้ว ก็หยิบคำตอบเดิมมาให้เลยไม่ต้องคิดใหม่

---

## 4. คุณภาพที่ engine รับประกัน (ครอบทุกสาย)

| ด้าน                                                           | layer ที่จัดการ                                               | ลดปัญหาได้แค่ไหน                                 |
| ------------------------------------------------------------------ | ---------------------------------------------------------------------- | ---------------------------------------------------------------- |
| **Hallucination มั่วข้อมูล**                       | Grounding+Citation (L2), Verify (L2), Debate (L2), Retrieval rail (L5) | **มาก** ไม่ใช่ 0% — จึงต้อง human-loop    |
| **คิดเลขผิด**                                       | Quant model แยกจาก LLM (L2) + Verify                             | **มากสุด** — เอาเลขให้ code จริงคิด |
| **Bias/มองด้านเดียว**                            | Debate (L2) + Human gate (L3)                                          | ปานกลาง                                                   |
| **Prompt-injection**                                         | Input rail (L5)                                                        | มาก                                                           |
| **กล่องดำ อธิบายไม่ได้**                  | Trace (L6) + Citation                                                  | มาก                                                           |
| **Model drift**                                              | Monitoring (L7)                                                        | มาก (ระยะยาว)                                          |
| **อ่านเอกสาร/ตารางผิด (extraction error)** | Layout-OCR + table-aware chunking (L0)                                 | **มาก** — field accuracy 95-99%                        |
| **ดึงข้อมูลผิด/ไม่ตรง (retrieval error)**  | Hybrid search + reranker + citation-by-ID (L5)                         | **มาก** — hallucination ~ครึ่ง                    |
| **AI มั่นใจเกินจริง (over-confidence)**        | Self-consistency (L2) + uncertainty routing (L3)                       | มาก — ส่งเคสไม่ชัวร์ให้คน                 |
| **Handoff/format พังเงียบ (silent error)**           | Schema Contract — constrained decoding (L8)                           | **มากสุด** — fail 8-15% → <0.1%                    |
| **ต้นทุนแพงเกินใช้จริง**                 | Route-then-cascade + semantic caching (L9)                             | มาก — cost -45-85% คง quality ~95%                         |

**⚠️ ห้ามเคลม "แก้ hallucination 100%"** — จูจ CFA สวนทันที
**พูดแบบปลอดภัย:** "ลดความเสี่ยงผ่าน deterministic tools, evidence controls, evaluation และ human gates ตาม risk-based model lifecycle; ไม่เคลมว่าแก้ hallucination ได้ทั้งหมด" ([Federal Reserve SR 26-2](https://www.federalreserve.gov/supervisionreg/srletters/SR2602.htm), [NIST AI RMF](https://airc.nist.gov/airmf-resources/airmf/5-sec-core/))
**จุดแข็งเน้นได้:** เก่งเรื่อง **เลขการเงิน** เพราะแยก quant model ออกจาก LLM ไม่ปล่อย AI เดาเลข

---

## 5. Flow การทำงาน (step-by-step)

1. **Ingest** — โหลดข้อมูลสายงาน (flagship demo: ER P2 ใช้ข้อมูล public ของบริษัทจดทะเบียน เช่น งบ, oppday, IAA consensus, transcript/summary เพื่อเลี่ยงข้อมูลลับ; สถาปัตยกรรมยังรองรับ on-prem/private data สำหรับสายงานอื่นภายหลัง) → ผ่าน **input rail (L5)**
2. **Task Map (L1)** — engine อ่าน workflow spec → รู้ว่ามีกี่ขั้น
3. **Agent ทำงานต่อขั้น (L2)** — agent(1+) + quant model · **Memory (L4)** ดึงดีลคล้ายมาช่วย
4. **Debate + Verify (L2)** — เถียงกัน + ตรวจเลข · **output rail (L5)** คุมก่อนออก
5. **Gate ขั้นสำคัญ (L3)** — คนตรวจ/เติม → เขียนลง state · บันทึก override ลง **L7**
6. **Incremental re-run (L3)** — แก้ขั้นไหน rerun จากตรงนั้นลงล่าง
7. **Final review (L3)** — คนตรวจ output รวม
8. **Output** — งานพร้อมใช้ + citation ทุกจุด + **trace (L6)** ครบ + **audit record (L7)**

*ทุกขั้น L6 บันทึก trace, L7 เก็บ audit ตลอด*

---

## 6. ตัวอย่าง flagship demo: Equity Research P2 Earnings Update

**Workflow จริง ER P2 (build รอบ hackathon):**

| ขั้น | งานในขั้น | agent | quant/model |
|---|---|---|---|
| 1 Digest results + call | อ่านงบ/oppday/transcript แล้วสรุป surprise + management cues | Digest-agent + Transcript-NLP-agent | `surprise_fn`, transcript NLP |
| 2 Update model | อัปเดต 3-statement forecast จาก actuals/guidance | Model-agent + Verify-agent | `three_statement_engine` |
| 3 Re-value + revise rating | คำนวณ target price, rating, consensus deviation | Valuation-agent + Rating-agent | `comps_engine`, `dcf_engine`, `rating_fn`, `consensus_dev_fn` |
| 4 Draft earnings note | ร่าง earnings note พร้อม citation | Note-agent + Fact-checker | citation-by-ID |
| 5 Compliance gate | licensed analyst/human reviewer ตรวจและ approve | Compliance pre-check + human | hard gate |
| 6 Publish/demo output | ส่งออก note + before/after metrics + trace | Publish-agent | eval harness |

**Gate (L3):** consensus deviation > 15% หรือ confidence ต่ำ → human gate; compliance gate บังคับก่อน publish  
**Human เติม:** ปรับ assumption, rating basis, compliance note, override reason  
**Memory (L4):** forecast-error memory ต่อ ticker เช่น MAPE/bias ของ NIM/revenue/EPS  
**Governance (L7):** เก็บ model route, validation record, override log, before/after metrics  

→ **Build scope:** P2 เส้นเดียวให้วิ่งครบ L0-L9 แบบ MVP. P1/P3-P7 และสายงานอื่นเป็น expansion story ไม่ใช่สิ่งที่จะ build รอบนี้.

---

## 7. เหตุผลออกแบบแบบนี้ (อธิบายทีม)

- **แยก engine/plug** → finance ไม่ต้องแตะ AI แค่บอก "สายนี้ทำงานยังไง"
- **agent-per-task** → map ตรงวิธีคิด finance (workflow เป็นขั้น)
- **quality ฝัง engine** → ทุกสายได้ grounding/debate/verify เท่ากัน
- **incremental loop + state** → เร็ว + ไม่ทิ้งงานที่คนตรวจแล้ว
- **human gate + governance (L7)** → ตรงกับ CFA reasonable-basis/objectivity และใช้ SR 26-2/NIST AI RMF เป็น risk-governance references; Thai applicability ต้อง legal/compliance review
- **trace (L6) + guardrail (L5)** → โปร่งใส + กันเอกสารแฝงคำสั่ง (สำคัญเพราะ ER อ่าน filing, transcript, consensus, และแหล่งข้อมูล public หลายชนิด)

---

## 8. 📋 TEMPLATE ให้ทีม finance กรอก (ต่อ 1 สาย)

> กรอกอันนี้ต่อสายที่จะทำ แล้วส่งให้ทีม tech เสียบเข้า engine

```
สายงาน: ___________________

1. WORKFLOW STEPS (สายนี้ทำงานกี่ขั้น แต่ละขั้นทำอะไร)
   ขั้น 1: ______  → งาน: ______
   ขั้น 2: ______  → งาน: ______
   ...

2. QUANT/MATH FRAMEWORK (สูตร/model ที่สายนี้ใช้จริง)
   ขั้นไหน: ______  → ใช้: ______ (เช่น DCF, Beneish, VaR)

3. INPUT DATA (ใช้ข้อมูลอะไร / public หรือ private)
   ______

4. GATE POINTS (ขั้นไหนคนต้องตรวจ + ตรวจอะไร)
   ______

5. OUTPUT (ขั้นสุดท้ายได้อะไร ใช้ทำอะไรต่อ)
   ______
```

*L4–L7 ทีม finance ไม่ต้องกรอก — engine ให้อัตโนมัติทุกสาย*

---

## 9. สิ่งที่ทีม finance ต้องไปหา (action)

1. ล็อกสายที่จะทำรอบ hackathon = **Sell-side Equity Research P2 Earnings Update**
2. ใช้ `02_sector_db/equity_research_deep_dive.md` เป็น sector plug หลัก และใช้ P2 §5 เป็น workflow source of truth
3. ระบุ quant/model ที่ต้องใช้จริง: surprise, 3-statement update, comps, DCF cross-check, rating, consensus deviation
4. เลือก ticker/demo data 1 บริษัทให้ครบก่อน build
5. ชี้ gate ที่คนต้องตรวจ: consensus deviation/material surprise และ compliance sign-off
   → ทีม tech เอาไปเสียบ engine + ทำ P2 walking skeleton

---

## 10. Gaps / ต้องตัดสินต่อ

- scope รอบ hackathon ล็อกแล้ว = ER P2; สายอื่น/P1/P3-P7 เป็น expansion story
- quant model ของ P2 ล็อกเป็น surprise, 3-statement, comps, DCF cross-check, rating, consensus deviation — ต้องทดสอบสูตรจริง
- demo company ล็อกแล้ว = MSFT + AMZN + PTT
- SR 26-2 อ่านและอัปเดตเป็น current reference แล้ว; ห้ามใช้ถ้อยคำว่า “ผ่าน regulator” โดยไม่มี independent/legal review
- Thailand-first compliance boundary ล็อกแล้ว; exact Thai SEC/IAA applicability ยังต้อง qualified legal/compliance review ก่อนใช้งานจริง
- Memory (L4) ในเดโมรอบเดียวเห็นผลยาก — ขายเป็น vision

---

## 11. ⚡ Performance Engineering — technique → ปัญหาที่แก้ → เกณฑ์คะแนนที่ได้

โต๊ะนี้เชื่อม "เทคนิคเพิ่ม performance" กับ "ปัญหาจริงในสายงาน" และ "เกณฑ์ให้คะแนน" — ใช้ตอบจูจว่าทำไมออกแบบแบบนี้

| Technique (layer)                                            | ปัญหาจริงที่แก้                                             | เกณฑ์คะแนนที่ได้                                                                 |
| ------------------------------------------------------------ | -------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ |
| **Layout-OCR + table-aware chunking** (L0)             | งบ DBD เป็น PDF สแกนไทย ตารางเยอะ แกะมือยาก | **a** (Thai-specific เฉพาะเจาะจง) + **d** (ลดเวลา 85-95%)           |
| **Deterministic normalization** (L0)                   | SET vs Capital IQ / TFRS-16 ทำ EV/EBITDA เพี้ยน                    | **a** (Thai-specific) + **b** (แก้ตรงจุด)                                   |
| **Hybrid search + cross-encoder reranker** (L5)        | ดึงข้อมูลผิด → AI มั่ว                                    | **b** (solution แข็ง) + **d** (hallucination ~ครึ่ง)                        |
| **Citation-by-ID contract** (L5)                       | AI พูดลอยไม่มี source                                           | **b** + **c** (ตรวจสอบได้ = credible)                                      |
| **Self-consistency / N-best** (L2)                     | AI มั่นใจเกินจริง เดาเลข                               | **b** + **c** (รู้ตัวว่าไม่ชัวร์)                                   |
| **Best-of-N + Self-RAG reflection** (L2)               | คำตอบเดียวอาจพลาด                                         | **b** (สร้างสรรค์ น่าเชื่อถือ)                                        |
| **Uncertainty routing** (L3)                           | ปล่อยเคสเสี่ยงผ่านโดยไม่มีคนดู               | **c** (feasible ใช้จริง) + human-in-loop                                            |
| **Eval harness (faithfulness/gold-set)** (L7)          | เคลมว่าดีแต่วัดไม่ได้                                 | **c** (measurable) + **b** (พิสูจน์ได้)                                    |
| **Schema Contract — constrained decoding** (L8)       | handoff object พังเงียบ ข้อมูลหายระหว่างขั้น   | **b** (solution แข็ง) + **c** (fail <0.1%)                                       |
| **Route-then-cascade + semantic caching** (L9)         | engine แม่นแต่แพงเกินใช้จริง                          | **c** (cost -45-85%) + **d** (scale ได้จริง)                                  |
| **Active-learning จาก override (RLTHF-style)** (L4) | คนแก้ AI แล้ว AI ไม่เคยเรียนรู้                     | **b** (ยิ่งใช้ยิ่งเก่ง) + **d** (แรงคนแค่ 6-7%)               |
| **Data lineage ระดับตัวเลข** (L6)           | ตัวเลขใน output ย้อนที่มาไม่ได้                     | **a** (มาตรฐาน finance จริง) + **c** (defend every number ต่อ auditor) |

**สรุปเล่าจูจ:** "engine ไม่ได้แค่มี agent — แต่ใส่เทคนิค accuracy ระดับ production ปี 2026 ทุกชั้น: อ่านเอกสารแม่น (L0) → ค้นข้อมูลตรง (L5) → ตอบแบบรู้ตัวว่าชัวร์แค่ไหน (L2/L3) → วัดผลได้เป็นตัวเลข (L7)" — ตอบเกณฑ์ b (solution) และ c (feasibility) พร้อมกัน

**⚠️ ยังคงเตือน:** ทุกเทคนิค **ลด** error ไม่ใช่ขจัด 100% — จึงยังต้อง human gate (L3) เสมอ

---

## Sources (layer ใหม่ L4–L7 + Performance Engineering)

- Agent ref arch / memory / guardrail / observability: [futureagi](https://futureagi.com/blog/llm-agent-architectures-core-components/), [augmentcode](https://www.augmentcode.com/guides/agent-platform-engineering-reference-architecture)
- Guardrail rails / OWASP LLM Top-10 2025: [bigdataboutique](https://bigdataboutique.com/blog/ai-guardrails-implementing-safety-production-llm-apps)
- **Current model-risk reference:** [Federal Reserve SR 26-2](https://www.federalreserve.gov/supervisionreg/srletters/SR2602.htm), [current interagency guidance](https://www.federalreserve.gov/frrs/guidance/supervisory-guidance-on-model-risk-management.htm)
- **Hallucination mitigation (RAG/self-consistency/best-of-N/reflection):** [futureagi-hallucination](https://futureagi.com/blog/taming-hallucination-beast-strategies-reliable-llms/), [keymakr](https://keymakr.com/blog/preventing-llm-hallucinations-techniques-best-practices-2026/), [mbrenndoerfer](https://mbrenndoerfer.com/writing/hallucination-mitigation), [getmaxim](https://www.getmaxim.ai/articles/llm-hallucination-detection-and-mitigation-best-techniques/)
- **RAG best practices (hybrid search/reranking/chunking):** [stackai](https://www.stackai.com/insights/retrieval-augmented-generation-(rag)-best-practices-for-enterprise-ai-chunking-embeddings-reranking-and-hybrid-search-optimization), [BM25-to-CorrectiveRAG](https://arxiv.org/pdf/2604.01733), [MimirRAG financial](https://arxiv.org/html/2605.25030v1)
- **Financial document OCR / table extraction:** [unstract](https://unstract.com/blog/financial-statement-ocr/), [llamaindex-ocr-tables](https://www.llamaindex.ai/blog/ocr-for-tables)
- **Confidence calibration / uncertainty routing:** [uncertainty-routing arxiv](https://arxiv.org/pdf/2502.04428), [confident-ai-agent-eval](https://www.confident-ai.com/blog/llm-agent-evaluation-complete-guide)
- **Agent eval harness:** [confident-ai-eval-guide](https://www.confident-ai.com/blog/definitive-ai-agent-evaluation-guide)
- **Structured output / constrained decoding (L8):** [tokenmix](https://tokenmix.ai/blog/structured-output-json-guide), [eastondev](https://eastondev.com/blog/en/posts/ai/20260506-llm-structured-output/)
- **Model routing / cascade / semantic caching (L9):** [tianpan](https://tianpan.co/blog/2025-11-03-llm-routing-model-cascades), [mbrenndoerfer-routing](https://mbrenndoerfer.com/writing/model-routing-selection-ab-testing-cascades-strategies)
- **Active-learning จาก human override (L4):** [RLTHF arxiv](https://arxiv.org/pdf/2502.13417), [Agent-in-the-Loop arxiv](https://arxiv.org/pdf/2510.06674)
- **Data lineage finance (L6):** [safebooks](https://safebooks.ai/resources/financial-data-governance/trust-every-number-implementing-data-lineage-across-the-finance-stack/), [collibra](https://www.collibra.com/blog/what-is-data-lineage-how-end-to-end-traceability-builds-confidence-in-your-data)
