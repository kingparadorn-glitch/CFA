# Sector Selection Decision — จัดอันดับ 5 สาย + Tier List (อ้างอิงเกณฑ์คะแนนจริง)
### เลือกสายไหนทำ AI Engine ในการแข่ง CFA Society Thailand AI × Finance Hackathon

> **ข้อจำกัดของเอกสาร:** คะแนนในไฟล์นี้เป็น **analytical judgment เทียบ rubric จริง** (ไม่ใช่คะแนนจากกรรมการ) — ใช้เพื่อจัดลำดับความเหมาะสมเชิงเปรียบเทียบ ไม่ใช่ทำนายคะแนนจริง. ทุกคะแนนสูง/ต่ำมีเหตุผลอ้างหลักฐานกำกับ

---

## 0. TIER LIST (สรุปบนสุด)

| Tier | สาย | คะแนนคาดการณ์ /85 | บทบาทที่เหมาะ |
|---|---|---|---|
| **S** | **Private Equity** | **75** | 🏆 Flagship demo (concept แข็งสุด + wow) |
| **A** | **Equity Research** | **74** | ⭐ Co-flagship / demo เสถียรสุด (feasibility สูงสุด) |
| **B** | **Risk / Model Validation** | **67** | 🛡️ สายพิสูจน์ governance (L7) |
| **B** | **Investment Banking** | **67** | 📊 สายโชว์ productivity impact |
| **C** | **M&A (Corporate Dev)** | **66** | 🧩 สายเสริม breadth (อ่อนสุดเชิงแข่ง) |

**Bottom line:** ทำ **PE เป็น flagship + ER เป็น co-flagship/demo เสถียร** เป็นแกนหลัก → ใช้ Risk เป็นสไลด์พิสูจน์ governance (differentiator) → IB/M&A พูดเป็น "breadth ของ generic engine" ไม่ต้อง demo ลึก

---

## 1. TL;DR — คำแนะนำ

**อันดับ 1-5:** PE (75) → ER (74) → Risk (67) = IB (67) → M&A (66)

- **Flagship = Private Equity** — solution concept (b) แข็งสุดเพราะใช้ครบทุก layer (multi-agent + forensic + DCF/LBO/Monte Carlo + human gate + governance) มี "wow factor" และ AI adoption สูง (Deloitte 86%) ลบความเสี่ยง "ของจริงไหม" ออกจากใจกรรมการ
- **Co-flagship / demo เสถียร = Equity Research** — feasibility (c) สูงสุดเพราะข้อมูล **public 100%** (filing/consensus/price) ไม่ต้องพึ่ง proxy, PDPA risk ต่ำสุด, demo ล่มยากสุด + ตัวเลข impact แรง (คืนเวลา 20-25 ชม./สัปดาห์)
- **Governance proof = Risk/Model Validation** — ไม่เด่นเชิง demo แต่เป็นตัว**พิสูจน์ L7 (Governance/SR 11-7/BOT Guideline)** = differentiator ที่คู่แข่งไม่ค่อยมี → ใส่เป็นสไลด์เชิงลึก 1-2 หน้า
- **IB / M&A** — เก็บไว้แสดง "engine เดียวเสียบได้หลายสาย (generic)" ไม่ต้องลงลึก — ระวังถ้าทำเยอะเกินจะกระจายโฟกัส

⚠️ **กับดักใหญ่:** เกณฑ์ a ให้คะแนน "เฉพาะเจาะจง/มีหลักฐาน" สูง — ถ้าพิตช์กว้างเกิน ("engine ทำได้ 5 สาย!") เสี่ยงโดนหักเพราะดูไม่เจาะ. **ลึก 1-2 สาย + โชว์ breadth เป็น bonus** ปลอดภัยกว่ากระจาย 5 สายเท่ากัน

---

## 2. วิธีให้คะแนน (โปร่งใส)

**เกณฑ์จริง 100 คะแนน** (CFA Society Thailand): a=Problem/industry relevance (20) · b=AI solution concept (25) · c=Feasibility/practicality incl. data/regulatory/PDPA (20) · d=Impact/value creation (20) · e=Slide quality (15)

**ไฟล์นี้ให้คะแนน a-d (รวม /85)** — ข้าม e เพราะขึ้นกับการออกแบบสไลด์ ไม่ใช่ตัวสาย

**Factor เสริมนอกเกณฑ์ตรง (แต่กระทบการเลือกจริง):** demo feasibility, PDPA risk, wow-factor ตอน present, Thai-specificity (ป้องกันการก็อป), implementation effort ในเวลาจำกัด, hallucination-defense, และ**สายนั้นพิสูจน์ layer ไหนของ engine ได้เด่น** (L1-L7)

---

## 3. ตารางคะแนนหลัก (a-d, รวม /85)

| สาย | a Problem /20 | b Solution /25 | c Feasibility /20 | d Impact /20 | รวม /85 |
|---|---|---|---|---|---|
| **Private Equity** | 18 | **23** | 16 | 18 | **75** |
| **Equity Research** | 18 | 19 | **19** | 18 | **74** |
| **Risk/Model Validation** | 17 | 21 | 15 | 14 | **67** |
| **Investment Banking** | 15 | 20 | 15 | 17 | **67** |
| **M&A (Corp Dev)** | 16 | 19 | 15 | 16 | **66** |

### เหตุผลต่อช่อง (อ้างหลักฐาน)

**Private Equity — 75**
- a=18: DD pain ชัด+วัดผลได้ (analyst ใช้ 90% เวลากับ data processing, 10% judgment) + Thai-specific (DBD extraction, SET vs Capital IQ) — เจาะจงสูง
- b=23 (สูงสุด): ใช้ครบทุก layer — multi-agent (screening/DD/forensic/valuation/risk/memo) + quant หลากหลาย (Beneish/Altman/Benford/DCF/LBO 7-step/Monte Carlo) + debate + human gate (IC) + governance → concept ซับซ้อนน่าเชื่อถือสุด
- c=16: ติด proxy — deal จริงลับ ต้องใช้บริษัทมหาชนแทน; แต่ Deloitte 86% adoption + Third Bridge "zero data retention/SOC2/audit trail" ช่วยลบข้อกังขา feasibility
- d=18: Third Bridge DD time -60-70% financial workstream, PwC 35-85% productivity — วัดผลชัด

**Equity Research — 74**
- a=18: earnings-season pain วัดผลชัด (5.7hr→45min) + Thai SET vs Capital IQ comps กระทบ valuation ตรง
- b=19: solid แต่ซับซ้อนน้อยกว่า PE (agent น้อยกว่า, comps-centric) — routing (initiation vs earnings) + 3-statement + rating; ไม่มี forensic/LBO ที่ตื่นตา
- c=19 (สูงสุด): **ข้อมูล public 100%** (10-K/10-Q/56-1, consensus, transcript, price) — ไม่ต้อง proxy, PDPA risk ต่ำสุดในทุกสาย, demo ล่มยากสุด
- d=18: 5 core workflow กิน 70-80% เวลา analyst, automate ลดงาน 40% = คืนเวลา 20-25 ชม./สัปดาห์

**Risk/Model Validation — 67**
- a=17: กรอบ regulatory แข็ง (SR 11-7/Basel/BOT) แต่ "ปัญหา" เป็น back-office/compliance ไม่ใช่ pain ที่มีตัวเลขเวลาประหยัด headline ชัดเท่า PE/ER
- b=21: แข็งจากมุม governance — พิสูจน์ L7 ตรงตัว, agent-as-a-judge (FinCon) map ตรง, "engine ตรวจตัวเอง" เป็น narrative แรง
- c=15: ต้องมี "โมเดลอื่น" ให้ตรวจก่อน; ข้อมูลเป็น model doc/synthetic — demo ต้องเตรียม setup
- d=14 (ต่ำสุด): impact เป็น compliance value วัดยากกว่า "ประหยัด X ชม." — กรรมการเห็นภาพ ROI ยากกว่า

**Investment Banking — 67**
- a=15: pitchbook/CIM drafting pain น่าเชื่อถือ แต่ **generic ระดับโลก ไม่ Thai-specific** — เจาะจงน้อยกว่า PE/ER
- b=20: pitchbook automation + comps ดี แต่ AI ยังสร้าง IB chart (waterfall/football field) ไม่ดี + คำนวณหลายขั้นพลาด — จุดอ่อนที่ต้องยอมรับ
- c=15: public deal data ใช้ได้ แต่ CIM/data room ลับ; hallucination risk ใน IB chart สูง
- d=17: Deloitte top-14 IB productivity +27-35%, ~$3.5M/front-office employee — ตัวเลขแรง

**M&A (Corp Dev) — 66**
- a=16: synergy capture gap จริง แต่ razor-specific น้อยกว่า PE DD
- b=19: synergy model + PMI ดี แต่ไม่ตื่นตาเท่า forensic/LBO
- c=15: ข้อมูล synergy ลับ ต้อง proxy; PMI ยาว 1-3 ปี demo ยาก
- d=16: McKinsey GenAI ลดต้นทุน M&A 20% — ชัดแต่ทั่วไป

---

## 4. Factor เสริม (นอกเกณฑ์ตรง แต่กระทบการเลือก)

| Factor | PE | Equity Research | Risk/Val | IB | M&A |
|---|---|---|---|---|---|
| **Demo feasibility (ข้อมูล)** | 🟡 ต้อง proxy (บ.มหาชน) | 🟢 public 100% ไม่ต้อง proxy | 🟡 ต้องมี model ให้ตรวจ | 🟡 deal data ลับบางส่วน | 🔴 synergy data ลับ |
| **PDPA risk** | 🟡 กลาง (ถ้าใช้ deal จริง) | 🟢 ต่ำสุด | 🟢 ต่ำ (synthetic ได้) | 🟡 กลาง | 🟡 กลาง |
| **Wow-factor ตอน present** | 🟢 สูง (deal/valuation ใหญ่) | 🟡 กลาง (report/rating) | 🔴 ต่ำ (back-office) | 🟢 สูง (pitchbook สวย) | 🟡 กลาง (synergy) |
| **Thai-specific (ป้องกันก็อป)** | 🟢 DBD/SET-CapIQ/TFRS16 | 🟢 SET vs CapIQ | 🟢 BOT Guideline ก.ย.2025 | 🔴 generic ระดับโลก | 🟡 ทั่วไป |
| **Implementation effort (เวลาจำกัด)** | 🔴 หนัก (quant เยอะ MC/LBO) | 🟢 เบา (comps/3-statement) | 🟡 กลาง (backtest engine) | 🟡 กลาง (chart ยาก) | 🟡 กลาง (synergy model) |
| **Hallucination-defense แข็งแค่ไหน** | 🟢 แยก quant ชัด (Beneish/DCF) | 🟢 แยก 3-statement/comps | 🟢 backtest = code จริง | 🔴 chart-gen เป็นจุดอ่อน AI | 🟡 synergy overstate เสี่ยง |
| **พิสูจน์ layer engine เด่น** | ครบทุก layer (L1-L7) | L2 debate + L3 gate (บังคับ) | **L7 Governance (เด่นสุด)** | L2 orchestrator-workers | L4 memory (deal คล้าย) |

**อ่านตาราง:**
- **ER = ตัวเลือกปลอดภัยสุดเชิง execution** — เขียว 4/7 factor, feasibility/PDPA/hallucination-defense/effort ดีหมด → demo ไม่ล่ม
- **PE = ตัวเลือก impact สูงสุด** — wow + ครบทุก layer แต่ effort หนัก + ต้อง proxy
- **Risk = พิสูจน์ L7 ได้คนเดียว** — จุดขาย governance ที่สายอื่นทำไม่ได้เท่า แม้ wow ต่ำ
- **IB = จุดอ่อน hallucination (chart)** — เสี่ยงถ้า demo live
- **M&A = อ่อนสุดเชิง demo** — synergy data ลับ + PMI ยาว

---

## 5. วิเคราะห์ราย Sector เชิงลึก

### 🏆 Private Equity (S-tier, 75) — Flagship
**จุดแข็ง:** concept ซับซ้อนน่าเชื่อถือสุด ใช้ครบทุก layer; forensic agent (งานเดิมไม่เสียเปล่า) = component ในขั้น DD; wow-factor สูง (deal/valuation); AI adoption สูงลบข้อกังขา
**จุดอ่อน:** implementation หนักสุด (Monte Carlo/LBO 7-step); ต้องใช้ proxy data; feasibility รองจาก ER
**ความเสี่ยง:** ถ้า demo quant ครบไม่ทันเวลา ต้องลดเหลือ mock บางส่วน
**เหมาะเป็น:** **Flagship** — เล่าเรื่องได้ครบ engine ตั้งแต่ L1-L7

### ⭐ Equity Research (A-tier, 74) — Co-flagship / Demo เสถียร
**จุดแข็ง:** feasibility สูงสุด (public data 100%, PDPA ต่ำสุด); implementation เบา; hallucination-defense ดี; impact ตัวเลขแรง; regulatory (MiFID II/FINRA) map ตรง L3 gate บังคับ
**จุดอ่อน:** wow-factor กลาง (ไม่มี deal ใหญ่); concept ซับซ้อนน้อยกว่า PE
**ความเสี่ยง:** ต่ำสุด — demo ล่มยาก
**เหมาะเป็น:** **Co-flagship** หรือ demo หลักถ้าทีมกลัว PE ทำไม่ทัน — เป็น "safe bet" ที่คะแนนเกือบเท่า PE

### 🛡️ Risk / Model Validation (B-tier, 67) — Governance Proof
**จุดแข็ง:** พิสูจน์ L7 (Governance) ได้คนเดียว; BOT Guideline (ก.ย. 2025) = Thai-specific ใหม่มากป้องกันก็อป; "engine ตรวจตัวเอง" narrative แรง; agent-as-a-judge map ตรง
**จุดอ่อน:** wow ต่ำ (back-office); impact วัดยาก (d=14 ต่ำสุด); ต้องมี model ให้ตรวจก่อน demo
**ความเสี่ยง:** ถ้าดันเป็น flagship อาจดูน่าเบื่อ/นามธรรมสำหรับกรรมการ
**เหมาะเป็น:** **สไลด์เชิงลึก 1-2 หน้า** โชว์ว่า engine ผ่าน model-risk review ได้ — differentiator ปิดจุดที่คู่แข่งอ่อน

### 📊 Investment Banking (B-tier, 67) — Productivity Story
**จุดแข็ง:** ตัวเลข productivity แรง (Deloitte 27-35%, $3.5M/employee); pitchbook สวยตอน present
**จุดอ่อน:** generic ระดับโลก (a=15 ไม่ Thai); AI สร้าง IB chart ไม่ดี = hallucination risk; CIM ลับ
**ความเสี่ยง:** ถ้า demo live แล้ว chart เพี้ยน = เสียความน่าเชื่อถือ
**เหมาะเป็น:** พูดเป็น breadth ("engine เสียบ IB ได้ด้วย") ไม่ต้อง demo chart จริง

### 🧩 M&A Corporate Development (C-tier, 66) — Breadth เสริม
**จุดแข็ง:** synergy + PMI เป็นมุมที่ PE ไม่มี; McKinsey -20% cost
**จุดอ่อน:** synergy data ลับสุด; PMI ยาว 1-3 ปี demo ไม่ได้; a เจาะจงน้อย
**ความเสี่ยง:** อ่อนสุดเชิงแข่ง — ถ้าทำลึกเสียเวลาโดยได้คะแนนน้อย
**เหมาะเป็น:** พูดผ่านๆ เป็น breadth เท่านั้น หรือตัดออกถ้าเวลาน้อย

---

## 6. Lineup ที่แนะนำ

**แกนหลัก (ทำ demo จริง):** **PE (flagship) + ER (co-flagship)**
- PE ให้ concept-depth + wow (ตอบ b สูงสุด)
- ER ให้ feasibility + demo เสถียร (ตอบ c สูงสุด) — กันเหนียวถ้า PE ทำไม่ทัน
- 2 สายนี้คะแนนรวมสูงสุด (75, 74) และ **เสริมจุดอ่อนกัน** (PE feasibility อ่อน ← ER แข็ง; ER wow อ่อน ← PE แข็ง)

**สไลด์เสริม (ไม่ demo ลึก):**
- **Risk** = 1-2 หน้าโชว์ L7 governance (จุดขาย regulator-ready + BOT Guideline ไทย)
- **IB + M&A** = รวมใน 1 หน้า "generic engine เสียบสายอื่นได้" (breadth) — ไม่ลงลึก

**ทำไม lineup นี้ครอบเกณฑ์ดีสุด:**
- a (Problem): PE+ER Thai-specific ชัด + Risk เพิ่ม BOT angle
- b (Solution): PE โชว์ concept ครบ layer
- c (Feasibility): ER public data ตอบตรง
- d (Impact): ทั้ง PE+ER มีตัวเลขแรง
- breadth (IB/M&A) = โชว์ generic โดยไม่กระจายโฟกัส

⚠️ **เตือน:** อย่าทำ demo ครบ 5 สาย — เกณฑ์ a เน้น "เฉพาะเจาะจง" ลึก 2 สาย + breadth เป็น bonus ได้คะแนนดีกว่าเฉลี่ย 5 สายบางๆ

---

## 7. Decision Matrix — ถ้าจูจเน้นอะไร ให้ปรับยังไง

| ถ้ากรรมการเน้น... | ปรับ lineup |
|---|---|
| **Solution concept/นวัตกรรม (b)** | ดัน **PE** เป็นพระเอกเดี่ยว โชว์ multi-agent + forensic + quant ครบ |
| **Feasibility/ทำได้จริง (c)** | ดัน **ER** ขึ้นเป็น flagship — public data 100% ตอบตรงสุด |
| **Governance/regulator (สาย ก.ล.ต./ธปท.)** | ยก **Risk** จาก B→โชว์เด่น เล่า BOT Guideline + SR 11-7 + "engine ตรวจตัวเอง" |
| **Impact/ROI ตัวเลข (d)** | เน้น **ER** (คืน 20-25 ชม./สัปดาห์) + **IB** (Deloitte 27-35%) |
| **Thai-context เฉพาะถิ่น (a)** | เน้น **PE/ER** (DBD/SET-CapIQ) + **Risk** (BOT Guideline) — เลี่ยง IB (generic) |
| **Demo ต้องไม่ล่ม (เสถียร)** | **ER** เป็นหลัก — hallucination-defense + public data ดีสุด |

**Insight:** ไม่ว่าเน้นด้านไหน **PE หรือ ER อยู่ในคำตอบเสมอ** → 2 สายนี้คือแกนที่ปลอดภัยที่สุด ส่วน Risk เป็น "wildcard" ที่พุ่งขึ้นเฉพาะเมื่อกรรมการสาย compliance/regulator

---

## 8. Sources (เฉพาะลิงก์เว็บ)

- Deloitte 2025 GenAI in M&A (86% adoption) — https://www.deloitte.com/us/en/about/press-room/deloitte-survey-genai-in-mna.html
- PwC — Private equity AI transformation (35-85%) — https://www.pwc.com/us/en/industries/financial-services/library/private-equity-ai-transformation.html
- Third Bridge — AI due diligence PE (DD time -60-70%, SOC2/audit trail) — https://www.thirdbridge.com/en-us/about-us/media/perspectives/ai-due-diligence-private-equity
- Marvin Labs — earnings-season (5.7hr→45min, -40% workload, คืน 20-25 ชม./สัปดาห์) — https://www.marvin-labs.com/solutions/earnings-season/
- Target price accuracy (94.5% multiples, DCF hit rate 52.3% vs revenue-multiple 55.1%) — https://www.tandfonline.com/doi/full/10.1080/23322039.2024.2423261
- McKinsey — GenAI ลดต้นทุน M&A 20% — https://www.cfodive.com/news/generative-ai-reduces-merger-acquisition-costs-20percent-mckinsey/812514/
- Deloitte — IB productivity 27-35% ($3.5M/employee) — https://www.deloitte.com/us/en/what-we-do/capabilities/mergers-acquisitions-restructuring/articles/m-and-a-generative-ai-study.html
- Thailand BOT AI Risk Management Guidelines (ก.ย. 2025) — https://www.tilleke.com/insights/thailand-issues-ai-risk-management-guidelines-for-financial-service-providers/25/
- SR 11-7 Model Risk Management — https://www.magicmirrorsecurity.com/blog/sr-11-7-model-risk-management-guidance-explained
- ESMA — MiFID II Q&A (Article 52, analyst separation) — https://www.esma.europa.eu/sites/default/files/library/esma35-43-349_mifid_ii_qas_on_investor_protection_topics.pdf
- Anthropic — Building Effective AI Agents (6 patterns) — https://www.anthropic.com/research/building-effective-agents
- IB pitchbook automation 2026 (AI chart weakness) — https://www.finalis.com/blog/the-real-impact-of-ai-on-dealmaking-what-boutique-investment-banks-need-to-know-in-2026
