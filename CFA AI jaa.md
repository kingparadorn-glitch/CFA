\# AI Architecture Design — ให้ทีม Finance

\#\#\# Generic Agent Engine \+ Human-in-the-Loop (flagship: Private Equity)

\> เป้าหมายเอกสารนี้: ทีม finance เห็นโครงหลัก แล้วไปหา "workflow จริงของแต่ละสาย" มาเสียบเข้า template ท้ายเอกสาร

\---

\#\# 1\. Concept 1 ประโยค

สร้าง \*\*engine กลาง\*\* ที่รับข้อมูลของสายงาน → agent หลายตัวทำงานตาม \*\*framework จริงของสายนั้น\*\* → ส่ง output ให้คนตรวจ/เติม → \*\*loop\*\* ต่อจนได้งานดีสุด  
(AI ทำ framework แทนงาน, คนกำกับเป็นระยะ)

\---

\#\# 2\. เส้นแบ่งสำคัญ: อะไรคงที่ / อะไรทีมเสียบ

\*\*🔵 ENGINE (คงที่ทุกสาย — ทีม tech ทำ):\*\*  
รับประกันคุณภาพ 5 อย่างเหมือนกันหมดไม่ว่าสายไหน

1\. \*\*Grounding \+ Citation\*\* — ทุก output อ้างอิงกลับ source  
2\. \*\*Debate (maker/checker)\*\* — agent เถียงกันกันเตือนผิด/bias  
3\. \*\*Verify\*\* — ตรวจเลข AI vs source, flag ความมั่นใจต่ำ  
4\. \*\*Eval\*\* — วัด precision/recall กับ gold-set  
5\. \*\*Human-in-Loop \+ State\*\* — gate ให้คนตรวจ, จำข้าม loop

\*\*🟠 SECTOR PLUG (เปลี่ยนต่อสาย — ทีม finance หา):\*\*

1\. \*\*Workflow steps\*\* — สายนั้นทำงานกี่ขั้น แต่ละขั้นทำอะไร  
2\. \*\*Quant/Math framework\*\* — สูตร/model ที่สายนั้นใช้ (เสียบตรงที่ช่วยได้)  
3\. \*\*Input data\*\* — สายนั้นใช้ข้อมูลอะไร  
4\. \*\*Gate points\*\* — ขั้นไหนคนต้องตรวจ

→ \*\*ทีม finance โฟกัสแค่ 🟠 — engine 🔵 จัดการให้\*\*

\#\# 3\. โครงสร้าง 3 Layer

\`\`\`  
┌─────────────────────────────────────────────┐  
│ LAYER 1: TASK MAP (ทีม finance นิยาม)         │  
│ สายงาน → ขั้นที่ 1..N → "แต่ละขั้นทำงานอะไร"   │  
└─────────────────────────────────────────────┘  
                    │ เลือก agent ต่อขั้น (มีได้ \>1)  
                    ▼  
┌─────────────────────────────────────────────┐  
│ LAYER 2: AGENT ORCHESTRATION (engine)         │  
│ agent-per-task \+ quant model \+ debate         │  
│ → orchestrator เดินตาม flow                   │  
└─────────────────────────────────────────────┘  
                    │ output แต่ละขั้น  
                    ▼  
┌─────────────────────────────────────────────┐  
│ LAYER 3: HUMAN-LOOP \+ STATE (engine)          │  
│ gate ขั้นสำคัญ \+ final review                 │  
│ คนเติม → เขียนลง state → re-run เฉพาะขั้น      │  
│ ที่เกี่ยว+ถัดไป (incremental)                  │  
└─────────────────────────────────────────────┘  
\`\`\`

\---

\#\# 4\. Flow การทำงาน (step-by-step)

1\. \*\*Ingest\*\* — โหลดข้อมูลสายงาน (flagship PE: ใช้บริษัทมหาชนเป็น proxy \= ข้อมูล public เลี่ยงความลับ; สถาปัตยกรรมรองรับ on-prem สำหรับ data room จริง)  
2\. \*\*Task Map\*\* — engine อ่าน workflow spec ของสาย → รู้ว่ามีกี่ขั้น  
3\. \*\*Agent ทำงานต่อขั้น\*\* — แต่ละขั้น agent(1+) ทำงาน \+ เรียก quant model ถ้ามี  
4\. \*\*Debate \+ Verify\*\* — ก่อนออกจากขั้น agent เถียงกัน \+ ตรวจเลข  
5\. \*\*Gate (ขั้นสำคัญ)\*\* — ส่งให้คนตรวจ → คนเติม/แก้ → เขียนลง state  
6\. \*\*Incremental re-run\*\* — แก้ขั้นไหน rerun จากตรงนั้นลงล่าง (ขั้นที่ผ่านแล้วไม่ทำซ้ำ)  
7\. \*\*Final review\*\* — คนตรวจ output รวม  
8\. \*\*Output\*\* — งานพร้อมใช้ \+ citation ทุกจุด

\---

\#\# 5\. ตัวอย่าง flagship: Private Equity (worked example)

\*\*Workflow จริง PE (ตัวอย่าง — ทีมไปยืนยัน/ปรับ):\*\*

| ขั้น          | งานในขั้น                              | agent                              | quant/model                      

| 1 Sourcing/Screen | คัดบริษัทเข้าเกณฑ์            | Screening agent                    | filter rules                     |  
| 2 Financial DD    | อ่านงบ ตรวจสุขภาพการเงิน | DD agent \+\*\*Forensic agent\*\* | Beneish/Altman/Benford           |  
| 3 Valuation       | ประเมินมูลค่า                      | Valuation agent                    | DCF, comps,\*\*Monte Carlo\*\* |  
| 4 Risk/Scenario   | stress test ดีล                              | Risk agent                         | MC scenario, sensitivity         |  
| 5 IC Memo         | ร่างเอกสารเสนอ IC                 | Memo agent                         | —                               

\*\*Gate:\*\* หลังขั้น 2 (DD) และ 3 (Valuation) \+ final review ที่ IC memo  
\*\*Human เติม:\*\* สมมติฐาน, ข้อมูล qualitative, ปรับ weight

\---

\#\# 6\. เหตุผลออกแบบแบบนี้ (อธิบายทีม)

\- \*\*แยก engine/plug\*\* → ทีม finance ไม่ต้องแตะ AI แค่บอก "สายนี้ทำงานยังไง" → engine เดินให้  
\- \*\*agent-per-task\*\* → map ตรงกับวิธีคิด finance (workflow เป็นขั้น) เข้าใจง่าย  
\- \*\*quality ฝัง engine\*\* → ทุกสายได้ grounding/debate/verify เท่ากัน ไม่ต้องคิดใหม่  
\- \*\*incremental loop \+ state\*\* → เร็ว \+ ไม่ทิ้งงานที่คนตรวจแล้ว  
\- \*\*human gate\*\* → ตรง ก.ล.ต./CFA ที่เน้นมนุษย์กำกับ \+ practitioner ทุก deck เน้น

\---

\#\# 7\. 📋 TEMPLATE ให้ทีม finance กรอก (ต่อ 1 สาย)

\> กรอกอันนี้ต่อสายที่จะทำ แล้วส่งให้ทีม tech เสียบเข้า engine

\`\`\`  
สายงาน: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

1\. WORKFLOW STEPS (สายนี้ทำงานกี่ขั้น แต่ละขั้นทำอะไร)  
   ขั้น 1: \_\_\_\_\_\_  → งาน: \_\_\_\_\_\_  
   ขั้น 2: \_\_\_\_\_\_  → งาน: \_\_\_\_\_\_  
   ...

2\. QUANT/MATH FRAMEWORK (สูตร/model ที่สายนี้ใช้จริง)  
   ขั้นไหน: \_\_\_\_\_\_  → ใช้: \_\_\_\_\_\_ (เช่น DCF, Beneish, VaR)

3\. INPUT DATA (ใช้ข้อมูลอะไร / public หรือ private)  
   \_\_\_\_\_\_

4\. GATE POINTS (ขั้นไหนคนต้องตรวจ \+ ตรวจอะไร)  
   \_\_\_\_\_\_

5\. OUTPUT (ขั้นสุดท้ายได้อะไร ใช้ทำอะไรต่อ)  
   \_\_\_\_\_\_  
\`\`\`

\---

\#\# 8\. สิ่งที่ทีม finance ต้องไปหา (action)

1\. เลือกสายที่จะทำ (flagship \= PE)  
2\. ไปหา \*\*workflow จริง\*\* ของสายนั้น (จากคนทำงานจริง / เอกสาร workshop เป็นแนว)  
3\. ระบุ \*\*quant/model\*\* ที่สายนั้นใช้  
4\. กรอก template ข้อ 7  
5\. ชี้ \*\*gate\*\* ว่าคนควรตรวจตรงไหน

→ ทีม tech เอาไปเสียบ engine \+ ทำ demo

\---

\#\# 9\. Gaps / ต้องตัดสินต่อ

\- เลือกสายที่ 2-3 (นอก PE) จะเป็นอะไร — รอทีม finance  
\- quant model ต่อสาย — รอ finance ยืนยัน  
\- demo ใช้บริษัทมหาชนตัวไหนเป็น proxy — ต้องเลือก  
