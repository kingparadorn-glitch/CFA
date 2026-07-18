# Master Reference — 5 สายงานการเงิน สำหรับ AI Engine (PE, M&A, IB, Equity Research, Risk/Model Validation)
### DB หลักฉบับเดียว — Self-contained · ป้อนเข้า L1 Task Map + L2 Orchestration ของ AI Engine (7-layer, flagship PE)

---

## 1. Purpose & วิธีอ่านไฟล์นี้

ไฟล์นี้คือ**แหล่งข้อมูลหลักฉบับเดียว (self-contained)** รวมทุกอย่างที่รู้เกี่ยวกับ 5 สายงานการเงิน ใช้เป็น input ป้อนเข้า AI engine ที่ออกแบบไว้ (โครง 7 layer):
- **L1 Task Map** — สายงาน→ขั้น 1..N→งานแต่ละขั้น (finance นิยาม)
- **L2 Agent Orchestration** — agent-per-task + quant model + debate
- **L3 Human-Loop + State** — gate + คนเติม + re-run
- **L4 Memory** — จำข้ามดีล/ข้ามรอบ
- **L5 Guardrail Rails** — input/output/retrieval rail
- **L6 Observability/Trace** — บันทึกทุก step
- **L7 Governance** — model inventory + audit trail

แต่ละสายในไฟล์นี้มี 6 ส่วนเหมือนกัน: **(A) Workflow narrative เต็ม → (B) TEMPLATE กรอกครบ 5 field → (C) AI pain point + หลักฐาน → (D) Quant/model detail → (E) Step-Level Task Graph (ป้อน L1) → (F) L2 Orchestration Spec (ป้อน L2)**

ไฟล์นี้ผูกทุกเนื้อหาเข้ากับ**เกณฑ์ให้คะแนนจริงของการแข่งขัน** (หัวข้อ 2) เพื่อหยิบไปตอบกรรมการได้ตรงจุด

**5 สายในไฟล์นี้:** §3 Private Equity · §4 M&A (Corporate Development) · §5 Investment Banking (M&A Advisory) · §6 Equity Research (sell-side) · §7 Risk/Model Validation

> **หมายเหตุ:** ไฟล์นี้ self-contained 100% — ไม่ลิงก์ไฟล์อื่นในโปรเจกต์ อ้างอิงเฉพาะแหล่งเว็บภายนอก (ดูหัวข้อ Sources ท้ายไฟล์)

---

## 2. เกณฑ์ให้คะแนนจริง + Cross-reference Matrix

**เกณฑ์การคัดเลือก 5 ทีมเข้ารอบชิงชนะเลิศ (CFA Society Thailand, รวม 100 คะแนน):**

| # | หมวด (ไทย) | English | คะแนน | เกณฑ์การให้คะแนน (ย่อ) |
|---|---|---|---|---|
| a | การระบุปัญหาและความเชื่อมโยงกับอุตสาหกรรม | Problem identification & industry relevance | 20 | 1-5 คลุมเครือ · 6-10 กว้างไป · 11-15 ชัดเจนและเกี่ยวข้อง · 16-20 เจาะจง เฉพาะเจาะจง มีหลักฐาน |
| b | แนวคิด Solution AI | AI solution concept | 25 | 1-8 ไม่ชัด · 9-15 เป็นไปได้แต่รายละเอียดบาง · 16-20 แข็งแรงมีตรรกะ · 21-25 สร้างสรรค์ มีตรรกะ น่าเชื่อถือสูง |
| c | ความเป็นไปได้และความสมเหตุสมผลในการนำไปใช้ (รวม data/regulatory/PDPA) | Feasibility & practicality | 20 | 1-5 แทบเป็นไปไม่ได้ · 6-10 เป็นไปได้บางส่วน · 11-15 feasibility ดี · 16-20 เส้นทางน่าเชื่อถือ ใช้งานจริงได้ |
| d | ผลกระทบและการสร้างมูลค่า | Impact & value creation | 20 | 1-5 ผลกระทบไม่ชัด · 6-10 ประโยชน์ทั่วไป · 11-15 ผลกระทบชัดเจน · 16-20 ผลกระทบเชิงกลยุทธ์วัดผลได้ |
| e | คุณภาพและความชัดเจนของสไลด์ (สูงสุด 10 หน้า) | Slide quality & clarity | 15 | 1-4 โครงสร้างแย่ · 5-8 บางส่วนดี · 9-12 มีโครงสร้างดี ชัดเจน · 13-15 มืออาชีพ น่าสนใจ เข้าใจได้ในตัวเอง |

**รวม 100 คะแนน** (หมวด e ขึ้นกับการออกแบบสไลด์ ไฟล์นี้ตอบ a-d เป็นหลัก)

### Cross-reference matrix: สายไหนตอบเกณฑ์ไหนในหัวข้อไหน

| สาย | a (20) — Problem | b (25) — Solution | c (20) — Feasibility | d (20) — Impact |
|---|---|---|---|---|
| **Private Equity** (§3) | §3C pain points + §3.5 Thai-specific | §3B template + §3D valuation + §3F orchestration | §3B input data (public proxy, PDPA ต่ำ) | §3C หลักฐาน (DD 90%→10%, Third Bridge 60-70%) |
| **M&A Corp Dev** (§4) | §4C pain points (synergy capture gap) | §4B template + §4D synergy model + §4F | §4B input data (public M&A filing) | §4C หลักฐาน (McKinsey GenAI ลด M&A cost 20%) |
| **Investment Banking** (§5) | §5C pain points (pitchbook/CIM drafting) | §5B template + §5F orchestration | §5B input data (public deal data) | §5C หลักฐาน (Deloitte IB productivity 27-35%) |
| **Equity Research** (§6) | §6C pain points + §6.4 regulatory | §6B template + §6D rating methodology | §6B input data (public filings 100%, PDPA ต่ำสุด) | §6C หลักฐาน (Marvin Labs 5.7hr→45min, ลดงาน 40%) |
| **Risk/Model Validation** (§7) | §7A workflow (SR 11-7/Basel/BOT) | §7B template + §7D validation tech + §7F | §7B input data + regulatory alignment | §7.3 governance value (engine ตรวจตัวเอง) |

---

## 3. Sector — Private Equity (flagship)

### 3A. Workflow เต็ม (7 ขั้น) — วงจรชีวิตดีล PE

งานของบริษัท Private Equity (PE) แบ่งเป็นสองงานใหญ่ต่อกัน: **ซื้อบริษัทให้ดี** และ **บริหารบริษัทนั้นให้ดีพอจะขายต่อได้ราคาสูงกว่าที่ซื้อมา** บริษัท PE ไม่ได้ใช้เงินตัวเองอย่างเดียว — ระดมเงินก้อนใหญ่จากนักลงทุน (Limited Partners หรือ LP เช่น กองทุนบำนาญ กองทุนมหาวิทยาลัย ครอบครัวที่มีฐานะ) แล้วเอาเงินก้อนนี้บวกกับเงินกู้ไปซื้อบริษัท

**ขั้นที่ 1 — หาบริษัทที่จะซื้อ (Sourcing) ~3 เดือน**
หาบริษัทเข้าเกณฑ์ (ขนาด/อุตสาหกรรม/รูปแบบกำไร) ส่วนใหญ่มาจากคอนเนคชั่นไม่ใช่สุ่มหา: investment banker/นายหน้า/ที่ปรึกษาส่ง "teaser" (เอกสารสรุปหน้าเดียวไม่บอกชื่อบริษัท) มาให้ หรือมาจากคอนเนคชั่นของบริษัทเอง (อดีตเพื่อนร่วมงาน, PE อื่น, portfolio company ที่รู้จักเป้าหมาย) — analyst/associate เช็คคร่าวๆ ว่าเข้าเกณฑ์ไหม ไม่เข้าตัดทิ้งทันที ดีลส่วนใหญ่ถูกปฏิเสธภายในไม่กี่วัน มีแค่ส่วนน้อยผ่านต่อ

**ขั้นที่ 2 — ดูจริงจังครั้งแรก + เสนอราคาไม่ผูกมัด ~1 เดือน**
เข้าสู่ due diligence แบบเบา: management meeting (ทีมดีลคุยกับผู้บริหาร ทำความเข้าใจธุรกิจ ดูว่าน่าร่วมงานไหม), สร้าง valuation คร่าวๆ (ยังไม่ละเอียด แค่พอรู้ช่วงราคาสมเหตุสมผล), ถ้ายังดูดียื่น **Letter of Intent (LOI)** — เอกสารไม่ผูกมัด บอกความจริงจัง เข้าสู่การคุยแบบ exclusive

**ขั้นที่ 3 — Due Diligence เจาะลึก ~3 เดือน (ขั้นใหญ่สุด หนักสุด)**
จุดประสงค์: หาเหตุผลทุกอย่างที่อาจทำให้ดีลนี้แย่ ก่อนทุ่มเงินจริง แบ่ง 4 สายทำพร้อมกัน:
- **Financial diligence** — ดึงงบย้อนหลังหลายปี เช็ครายได้/กำไรเป็นของจริงยั่งยืนไหม ไม่ใช่ boost ครั้งเดียว
- **Operational diligence** — ธุรกิจดำเนินงานจริงยังไง supply chain, production, technology, staffing
- **Market/commercial diligence** — คู่แข่งเป็นใคร อุตสาหกรรมโต/หด ลูกค้าซื่อสัตย์แค่ไหน
- **Legal diligence** — ทนายไล่ตรวจสัญญาทุกฉบับ คดีในอดีต compliance issue

ทำ "expert call" (คุยลูกค้า/อดีตพนักงานจริง sanity-check คำบอกเล่าผู้บริหาร) และช่วงนี้สร้างโมเดลการเงินละเอียด (หลาย scenario อนาคต — ที่มาของชื่อเสียง spreadsheet-obsession ของ PE) หลายคนทำงานเกือบทุกสุดสัปดาห์ช่วงนี้ **~25% ของดีลที่มาถึงขั้นนี้ไม่ไปถึงปิดดีล** (เจอปัญหาใหญ่ หรือช่องว่างราคาเชื่อมกันไม่ได้)

**ขั้นที่ 4 — เจรจาดีลจริง ~4 เดือน**
- **จัดหาแหล่งเงินทุน**: ผสมเงินกองทุน+เงินกู้ธนาคาร/credit fund → เรียก "Leveraged Buyout (LBO)" (leverage=หนี้) ใช้หนี้ = ใช้เงินตัวเองน้อยลง ขยายผลตอบแทนได้ถ้าไปดี (เพิ่มความเสี่ยงด้วย)
- ผู้ก่อตั้ง/ผู้บริหารเดิมอาจถือหุ้นต่อ ("rolling over") ให้ incentive สอดคล้องเจ้าของใหม่
- เสนอ **Investment Committee (IC)** ภายใน — พาร์ทเนอร์อาวุโสอนุมัติ/ปฏิเสธ อาจหลายรอบคำถาม
- ทนายทั้งสองฝ่ายร่าง+เจรจาสัญญาซื้อขายจริง (ราคา, เงื่อนไข, เหตุการณ์หลังปิดดีล)

**ขั้นที่ 5 — ปิดดีล (Closing) ~1 เดือน**
ผ่านอนุมัติ regulator ที่จำเป็น → โอนเงิน กรรมสิทธิ์เปลี่ยนมือ → เขียน **"แผน 100 วัน"** (รายการสิ่งที่จะแก้/ปรับปรุงทันทีที่เป็นเจ้าของ กันเสียเวลาช่วงแรก)

**ขั้นที่ 6 — เป็นเจ้าของ + ทำให้ธุรกิจดีขึ้น 4-7 ปี (ช่วงสร้างมูลค่าจริง)**
ทีมดีลนั่งบอร์ด รีวิวผลงานทุกเดือน/ไตรมาส, ผลักดัน operational improvement (ลดต้นทุน, บริหารรัดกุมขึ้น, เปลี่ยนผู้บริหาร), โตผ่าน "bolt-on acquisitions" (ซื้อบริษัทเล็กมาผนวก — เร็วกว่าโตธรรมชาติ), บริหาร/refinance หนี้ — associate/VP ดูแล 1-3 portfolio company พร้อมกัน เป้าหมายมูลค่าโต **2x-3x** ตลอดช่วงถือครอง มาจาก 3 ส่วนใกล้เคียงกัน: กำไรบริษัทเพิ่ม + จ่ายหนี้ลด + multiple ที่ผู้ซื้ออนาคตยอมจ่ายสูงขึ้น

**ขั้นที่ 7 — ขายออก (Exit) ~8 เดือน**
บริษัทถูก "แต่งตัว" ให้น่าดึงดูด (บางทีทำ DD ตัวเองก่อนเพื่อรู้ทันปัญหา) — ขาย 4 ทาง: strategic buyer (บริษัทดำเนินงานอุตสาหกรรมเดียวกัน), secondary buyout (PE อื่น), IPO (เข้าตลาดหลักทรัพย์), dividend recap (refinance ดึงเงินสดจ่ายนักลงทุนโดยยังถือบริษัทอยู่ — ไม่ใช่ขายเต็มรูปแบบ) — เจรจา+ปิดดีล มักจ้าง investment bank ดูแลกระบวนการขาย เงินที่ได้แบ่ง: ส่วนหนึ่งกลับ LP, ส่วนหนึ่ง ("carried interest"/"carry") เป็นของบริษัท PE+คนอาวุโส

**บันไดตำแหน่ง (คนกลุ่มเดียวเดินผ่านทั้ง 7 ขั้น รับผิดชอบมากขึ้นตามตำแหน่ง):**
- **Analyst** — พนักงานใหม่สุด: วิจัย ดึงข้อมูล สร้างส่วนโมเดล เตรียมสไลด์ภายใน
- **Associate** — ดูแลโมเดลการเงินรายวัน ทำงานหนัก DD ประสานทนาย/นักบัญชี/banker
- **Senior Associate** — อิสระขึ้น นำบางส่วนดีล บริหารจูเนียร์ ติดต่อผู้บริหารบริษัทตรง
- **Vice President** — บริหารดีลทั้งหมดรายวัน นำ session DD เอง สร้างความสัมพันธ์ภายนอก
- **Principal/Director** — หาดีลเข้ามา นำเจรจา มีส่วนปรับปรุงพอร์ตหลังซื้อ
- **Partner/Managing Director** — ตัดสินใจสุดท้ายว่าดีลเกิดไหม ระดมเงินจาก LP เป็นตัวแทนบริษัท

### 3B. TEMPLATE กรอกเต็ม — Private Equity

```
สายงาน: Private Equity

1. WORKFLOW STEPS
   ขั้น 1: Sourcing/Screening      → งาน: คัดบริษัทเข้าเกณฑ์จาก teaser/เครือข่าย
   ขั้น 2: Financial DD            → งาน: อ่านงบ ตรวจสุขภาพการเงิน หา red flag
   ขั้น 3: Valuation                → งาน: ประเมินมูลค่าบริษัท (DCF/comps/LBO/Monte Carlo)
   ขั้น 4: Risk/Scenario            → งาน: stress test ดีล (base/upside/downside/recession case)
   ขั้น 5: IC Memo                  → งาน: ร่างเอกสารเสนอ Investment Committee

2. QUANT/MATH FRAMEWORK
   ขั้น 2 (Financial DD)  → Beneish M-Score, Altman Z-Score, Benford's Law (ตรวจการตกแต่งบัญชี)
   ขั้น 3 (Valuation)     → DCF (WACC/CAPM + terminal value), Trading Comps (EV/EBITDA, EV/EBIT, EV/Revenue),
                            Precedent Transactions, LBO model (7 ขั้นย่อย), Monte Carlo simulation
   ขั้น 4 (Risk)          → Sensitivity grid (exit multiple × EBITDA growth), scenario modeling

3. INPUT DATA
   - Public: งบการเงินบริษัทมหาชน (ใช้เป็น proxy กันปัญหาข้อมูลลับ), industry data, comps set
   - Private (จริง): CIM (Confidential Information Memorandum), data room documents, contracts,
     HR data, management presentation — ต้องผ่าน PDPA/confidentiality controls ถ้าใช้ของจริง

4. GATE POINTS
   - หลังขั้น 2 (Financial DD) — คนตรวจก่อนเข้า valuation
   - หลังขั้น 3 (Valuation) — คนตรวจสมมติฐานก่อนเข้า IC
   - Final review ที่ IC Memo — Investment Committee อนุมัติ/ปฏิเสธ (บังคับ ไม่ใช่ optional)

5. OUTPUT
   IC Memo (เอกสารเสนอ Investment Committee: thesis, risk, returns case, recommendation)
```

### 3C. AI Pain Points + หลักฐานเต็ม (ตอบเกณฑ์ a, d)

**Deal sourcing/origination:** firm ส่วนใหญ่เห็นแค่เศษเสี้ยวของดีลทั้งหมดในตลาด — AI sourcing engine (EQT's Motherbrain, Grata, SourceScrub, Meridian Scout AI) สแกน website/filing/hiring signal หาเป้าหมาย

**Screening:** PE firm ทั่วไปเห็น **200-500 CIM ต่อปี** — associate อ่านและเตรียม one-pager สำหรับ pipeline review AI สามารถให้คะแนน CIM เทียบเกณฑ์ mandate (revenue range, EBITDA margin, sector, geography) ได้ — "รีวิว 30 CIM ในเวลาที่เคยรีวิวได้ 3"

**Due diligence (คอขวดใหญ่สุด):** phase หนักสุดของ PE operation ส่วนใหญ่ — **historically analyst ใช้เวลา ~90% กับ data processing, 10% กับ judgment** — AI กลับสัดส่วนนี้ได้
- **PwC benchmark: productivity gain 35-85%** บาง diligence task ไปจาก "สัปดาห์เป็นวัน" ([pwc.com](https://www.pwc.com/us/en/industries/financial-services/library/private-equity-ai-transformation.html))
- **2026 (Third Bridge): AI DD ลด time 60-70% สำหรับ financial workstream** พร้อมข้อกำหนดสำคัญ "zero data retention, private model deployment, SOC 2 compliance, full audit trail = prerequisite สำหรับข้อมูลดีลลับ" — ตรงกับ L5 Guardrail + L7 Governance ของ engine โดยตรง ([thirdbridge.com](https://www.thirdbridge.com/en-us/about-us/media/perspectives/ai-due-diligence-private-equity))
- Tools 2026 landscape: Hebbia (LLM trained บนเอกสารการเงิน/สัญญา วิเคราะห์ data room ทั้งห้องพร้อม citation+confidence score), AlphaSense, Tegus, Third Bridge, PitchBook (private market data gold standard), Kira, V7 Go, BDO/Datasite AI

**Portfolio reporting standardization:** portfolio company รายงานในฟอร์แมตต่างกันหมด AI ทำให้เป็น dashboard เดียว

**AI adoption ในวงการนี้ไม่ใช่ความเสี่ยงแล้ว:** Deloitte 2025 GenAI in M&A Study (สำรวจผู้นำอาวุโส 1,000 คนในสหรัฐฯ ครึ่งแรกปี 2025) พบ **86% ขององค์กรที่ตอบ integrate GenAI เข้า M&A workflow แล้ว และ 65% ทำภายในปีที่ผ่านมา** ด้านการลงทุน **83% ลงทุน $1M+ เฉพาะสำหรับทีม M&A** (88% ของ PE firm, 77% ของ corporate) — use case หลัก: **40% strategy/market assessment, 35% target identification/screening, 35% due diligence** — barrier หลัก: **67% กังวล data security, 65% กังวล data quality/availability** (ตรงกับเกณฑ์ c feasibility/PDPA — ยิ่งย้ำว่า human-in-loop + private deployment จำเป็น) ([deloitte.com press](https://www.deloitte.com/us/en/about/press-room/deloitte-survey-genai-in-mna.html), [deloitte.com study](https://www.deloitte.com/us/en/what-we-do/capabilities/mergers-acquisitions-restructuring/articles/m-and-a-generative-ai-study.html))

### 3D. Valuation Model Mechanics เต็มสูตร (ตอบเกณฑ์ b — ใช้ร่วมกับ M&A/IB/ER)

**DCF (core ของ ER & IB ด้วย):**
1. Project unlevered free cash flow (FCFF) 5-10 ปี
2. คำนวณ WACC ผ่าน CAPM: **Ke = Rf + β×(equity risk premium)** ผสมกับ after-tax cost of debt ถ่วงน้ำหนักด้วย market-value capital structure
3. Terminal value ผ่าน Gordon Growth: **FCFₙ×(1+g)/(WACC−g)** (g ≤ long-run nominal GDP growth) หรือ exit multiple — terminal value มักเป็น **60-80% ของ enterprise value**
4. Discount กลับมาเป็น present value
5. Bridge EV → equity value (ลบ net debt, preferred, minority interest)
6. Sensitivity table บน WACC × g, นำเสนอเป็น **football field** คู่กับ comps และ precedent
**ข้อสังเกต:** WACC เปลี่ยน 1% ทำให้ value เปลี่ยนได้ ~25% สำหรับหุ้น high-growth

**Trading Comps (IB & ER):**
1. เลือก peer 8-15 บริษัท
2. "spread" และ scrub การเงิน — ตัดรายการ non-recurring, calendarize fiscal year-end ต่างกัน, ปรับ operating lease
3. คำนวณ EV/EBITDA, EV/EBIT, EV/Revenue, P/E (match ประเภททุน: EV metric คู่กับ EV, equity metric คู่กับ equity value)
4. ใช้ median และ 25th-75th percentile range เทียบกับ metric ของ target
**ข้อผิดพลาดร้ายแรง:** ผสม EV กับ equity multiple, ข้าม normalization, ไม่ปรับ operating-lease (อาจเป็น 30-60% ของ EV สำหรับ retail/restaurant)

**Precedent Transactions (IB):**
ดึง announced-deal EV และ LTM metric จาก filing สาธารณะ → คำนวณ EV/LTM EBITDA, EV/Revenue, implied control premium → ปรับตาม market vintage → apply กับ target — precedent วิ่งสูงกว่า trading comps เพราะ **control premium (มักประมาณ 20-35%)**

**LBO (แกนของ PE; IB ใช้เป็น floor/"financial sponsor bid"):** 7 ขั้นที่เชื่อมโยงกัน
1. Entry valuation (entry multiple × EBITDA = entry EV)
2. Sources & Uses (ต้อง balance พอดี)
3. 3-statement operating projections
4. Debt schedule (senior/Term Loan B/mezz; mandatory amortization + cash sweep; ดอกเบี้ยบน average balance — สร้าง circular reference โดยตั้งใจ)
5. Exit assumptions + returns waterfall (exit EV − net debt = equity proceeds)
6. Sensitivity (5×5 grid: exit multiple × EBITDA growth)
7. Management incentive plan (MIP) / equity rollover
**Output:** **IRR** (ใช้ Excel XIRR ไม่ใช่ IRR ธรรมดา) และ **MOIC** (exit equity ÷ initial equity)
**Benchmark 2026:** leverage ~5.0-5.5x, equity 45-50%, target IRR 20%+ / MOIC 2.5-3.5x
**Value-creation bridge:** decompose returns เป็น EBITDA growth + multiple expansion + debt paydown

**Accretion/Dilution (IB):** รวม pro forma EPS ของ acquirer+target รวมค่า financing และ synergy — ดีล accretive ถ้า pro forma EPS > acquirer standalone EPS

**Returns & Downside Modeling (PE):** Base/upside/downside case บวก recession scenario (revenue ลด, margin compression 200bps, exit-multiple compression, PIK toggle บน sub-debt) — base case ~23% IRR / 2.6x MOIC อาจร่วงเหลือ ~8% IRR / 1.4x MOIC ภายใต้ stress

### 3.5 Thai-specific Pain Point เต็ม (จุดป้องกันการก็อป — ตอบเกณฑ์ a)

**1. DBD financial-statement extraction:** งบที่ยื่นผ่าน DBD e-Filing เป็น XBRL แต่งบเซ็นชื่อจริงฉบับเต็มอยู่ใน**เอกสารแนบ PDF สแกนภาษาไทย** — DataWarehouse+ ฟรีเปิดให้ดูแค่ summary line item — income statement มาในฟอร์แมต single-step/multi-step ต่างกัน — SME filing มักช้า/ไม่ครบ → แปลงเป็น model-ready data ยากมากด้วยมือ (Juslaws & Consult: filing ตั้งแต่ 1 เม.ย. 2020 ต้องผ่าน DBD e-Filing เป็น XBRL แต่ "signed Thai-language financial statements ถูกอัปโหลดเป็นเอกสารประกอบ" และ "ขั้นตอนแปลง XBRL คือจุดที่เกิด filing error บ่อยสุด โดยเฉพาะ mapping mismatch")

**2. Comps standardization (SET vs Capital IQ):** SET ระบุตัวเลข as-reported ("ตามที่บริษัทจดทะเบียนนำส่ง") ส่วน Capital IQ/Bloomberg "scrub" เป็น normalized EBITDA — TFRS 16 (มีผล 1 ม.ค. 2020 ในไทย) capitalize lease ทำให้ "เมื่อตัด lease expense ออกจาก EBITDA, metric อย่าง EV/EBITDA ดูต่ำลง สร้าง artificial comparability gap" (FTI Consulting) → นักวิเคราะห์ได้ multiple ต่างกันสำหรับบริษัทไทยเดียวกันจาก SET vs Capital IQ

**3. Contract review ใน DD:** 2 สัปดาห์-1 เดือน หา change-of-control clause และข้อจำกัด — Kira/Litera รายงาน time saving ถึง 50%, Clifford Chance "ลดเวลา review สัญญาลง 60%"

**4. Routine monthly reporting:** McKinsey ("AI in finance") พบ finance professional "ใช้เวลากับการประมวลข้อมูลน้อยลง 20-30%" ([mckinsey.com](https://www.mckinsey.com/capabilities/strategy-and-corporate-finance/our-insights/how-finance-teams-are-putting-ai-to-work-today)); close-automation vendor รายงาน cycle reduction 40-70% (นำเสนอเป็นทิศทาง)

### 3E. Step-Level Task Graph — Private Equity (ป้อน L1)

| ขั้น | Input (รับจาก) | Output (ส่งต่อ) | Actor/Role | Parallel/Seq | เวลา/effort | Decision/Branch | Pain point ผูกขั้นนี้ |
|---|---|---|---|---|---|---|---|
| 1 Sourcing | teaser, mandate criteria, network signal | shortlist ผ่านเกณฑ์ `{targets[]}` | Analyst/Associate | Seq | ~3 เดือน | ไม่เข้าเกณฑ์ → reject ทันที (ดีลส่วนใหญ่ตายที่นี่ในไม่กี่วัน) | เห็นแค่เศษเสี้ยวของดีลในตลาด (200-500 CIM/ปี) |
| 2 Financial DD | shortlist + งบย้อนหลัง + CIM | `{financial_health_flags[], adjusted_EBITDA, red_flag_severity}` | Associate + Forensic | **Parallel** (financial/operational/market/legal 4 lane) | ~3 เดือน (หนักสุด) | red flag ใหญ่ → **kill deal (~25% ตายที่นี่)**; ผ่าน → valuation | 90% เวลาไปกับ data processing แค่ 10% judgment |
| 3 Valuation | DD output + comps set + assumption | `{enterprise_value_range, entry_multiple, base/up/down case}` | Associate/VP | Seq (หลาย model ขนานภายใน) | ~2-4 สัปดาห์ | ราคาไม่ผ่าน hurdle → walk away | spreadsheet-obsession, model rebuild ซ้ำ |
| 4 Risk/Scenario | valuation base case | `{stress_IRR, stress_MOIC, sensitivity_grid}` | VP | Seq | ~1-2 สัปดาห์ | downside แย่เกิน → ปรับ price/ถอน | IC จะ pressure-test ตัวเลข downside |
| 5 IC Memo | ทุก output ข้างบน | IC Memo (thesis+risk+returns+recommendation) | VP/Principal | Seq | ~1-2 สัปดาห์ | IC ปฏิเสธ → จบ; อนุมัติ → เข้า negotiate/close | prep เอกสารให้ senior ตัดสินใจ |

### 3F. L2 Orchestration Spec — Private Equity (ป้อน L2)

| ขั้น | Agent(s) (ชื่อ+หน้าที่) | Orchestration pattern (Anthropic) | Debate/maker-checker | Quant binding (agent เรียก tool) | Handoff object |
|---|---|---|---|---|---|
| 1 Sourcing | Screening-agent (ให้คะแนน CIM เทียบ mandate) | **Routing** (คัดเข้า/ออก) | — | filter rules (เกณฑ์ revenue/EBITDA/sector) | `{scored_targets[]}` |
| 2 Financial DD | DD-Reader (extract งบ), Forensic-agent (รัน fraud score), Checker-agent (เตือน false positive) | **Parallelization-sectioning** (DD-Reader+Forensic ขนาน) + **Evaluator-Optimizer** (Checker หุ้ม) | Forensic (maker) ↔ Checker (checker) | Forensic เรียก quant tool: Beneish M-Score / Altman Z / Benford — คำนวณใน code จริง ไม่ให้ LLM เดาเลข | `{financial_health_flags[], adjusted_EBITDA, red_flag_severity}` |
| 3 Valuation | Valuation-agent (สร้าง model), Comps-agent (spread peers) | **Orchestrator-Workers** (orchestrator แตกงานเป็น DCF/comps/LBO ให้ worker) | Valuation (maker) ↔ Verify-agent (ตรวจเลข vs source) | เรียก quant tool: DCF engine, LBO engine, Monte Carlo — LLM อ่านผลกลับ ไม่คำนวณเอง | `{EV_range, entry_multiple, cases{}}` |
| 4 Risk/Scenario | Risk-agent (stress test) | **Parallelization-sectioning** (หลาย scenario ขนาน) | Risk (maker) ↔ Checker | เรียก sensitivity/MC scenario tool | `{stress_IRR, stress_MOIC, grid}` |
| 5 IC Memo | Memo-agent (ร่าง), Manager/Judge-agent (สังเคราะห์+ตัดสิน) | **Orchestrator-Workers** + agent-as-a-judge | Memo (maker) ↔ Judge (checker เลียน IC) | — (drafting) | IC Memo + citation ครบ → **human gate (IC)** |

> **หมายเหตุ Forensic agent:** งาน forensic (เช่น Hermes) = 1 agent ในขั้น 2 ของ engine นี้ = งานเดิมไม่เสียเปล่า กลายเป็น component

---

## 4. Sector — M&A (Corporate Development / Strategic Acquisition)

### 4A. Workflow เต็ม — ต่างจาก PE อย่างไร

M&A แบบ **corporate development** คือทีมภายในบริษัทใหญ่ (เช่น Microsoft, Google, Cisco) ที่ซื้อกิจการเพื่อ **strategic fit + synergy** ไม่ใช่เพื่อผลตอบแทนการเงินแบบ PE — **ต่างจาก PE 3 จุดหลัก:** (1) ไม่มี LP/IC แต่มี **corporate board** อนุมัติ (2) เป้าหมายคือ **synergy** (cost/revenue) ไม่ใช่ IRR/MOIC (3) มี **Post-Merger Integration (PMI)** เป็นขั้นหลักที่ PE ไม่เน้น — PE ถือแล้วปรับปรุงแล้วขาย, M&A ผนวกเข้าองค์กรถาวร

**6-step M&A strategy (workflow ที่ corporate dev team ใช้จริง):**
1. **นิยาม merger strategy** — "ทำไม" ต้องซื้อ (เข้าตลาดใหม่? เทคโนโลยี? กำจัดคู่แข่ง?)
2. **นิยาม acquisition criteria** — "อะไร" ที่เข้าเกณฑ์ (ขั้น 1-3 ตอบ why/what ของ strategy)
3. **สร้าง hunting mandate** — แปลง strategy เป็นเกณฑ์ให้ทีม sourcing ล่าเป้าหมาย
4. **Opportunity sourcing** — scout เป้าหมาย, สำรวจตลาดใหม่, จับความเคลื่อนไหวคู่แข่ง
5. **Strategic assessment & fit analysis** — ทดสอบแต่ละโอกาสเทียบ strategy บริษัท
6. **Financial modeling & scenario** — forecast cash flow, **synergy**, dilution

**Deal archetype 3 แบบ (จาก synergy validation ตอน DD):**
- **Horizontal scale** — รวมส่วนแบ่งตลาดอุตสาหกรรมเดียวกัน จับ **cost synergy**
- **Vertical chain control** — ซื้อ supplier/distribution channel จับ margin
- **Geographic entry** — เข้าตลาด/ประเทศใหม่ทันที

**Post-Merger Integration (PMI) — ขั้นเด่นที่ทำให้ M&A ต่างจาก PE:**
- ทำ **PMI program** ที่นิยาม value driver ของดีล + วิธีบรรลุ merger benefit
- ทำ **PMI timeline + work plan** ที่มี milestone/KPI/deadline ชัด
- แต่ละ business function (HR, product, legal, IT) ต้องมี **synergy goal + implementation plan + dedicated resource** เพื่อ execute ไม่ให้ synergy หลุด "ตั้งแต่วันแรกหลังปิดดีล"

### 4B. TEMPLATE กรอกเต็ม — M&A (Corporate Development)

```
สายงาน: M&A (Corporate Development / Strategic Acquisition)

1. WORKFLOW STEPS
   ขั้น 1: Strategy + Criteria       → งาน: นิยาม why/what ของ merger + สร้าง hunting mandate
   ขั้น 2: Sourcing + Fit Analysis   → งาน: scout เป้าหมาย + ทดสอบ strategic fit
   ขั้น 3: Synergy Modeling          → งาน: forecast synergy (cost/revenue), dilution, cash flow
   ขั้น 4: DD + Synergy Validation   → งาน: ตรวจ growth model + validate synergy hypothesis
   ขั้น 5: Board Approval + Deal      → งาน: เสนอ corporate board, เจรจา, ปิดดีล
   ขั้น 6: Post-Merger Integration   → งาน: PMI program + timeline + synergy tracking ต่อ function

2. QUANT/MATH FRAMEWORK
   ขั้น 3 → Synergy model (cost/revenue synergy NPV), Accretion/Dilution (pro forma EPS),
            DCF ของ combined entity
   ขั้น 4 → Sensitivity บน synergy realization %, integration cost
   ขั้น 6 → Synergy tracking KPI (actual vs planned)

3. INPUT DATA
   - Public: M&A announced-deal filing, target 10-K/annual report, industry data
   - Internal: acquirer strategy doc, product roadmap, internal financials (สำหรับ synergy)
   - ใช้ public company เป็น proxy สำหรับ demo (เลี่ยงข้อมูล synergy ลับ)

4. GATE POINTS
   - หลังขั้น 4 (Synergy Validation) — คนตรวจ synergy hypothesis สมจริงไหม (ชอบ overstate)
   - ขั้น 5 (Board Approval) — corporate board อนุมัติ (บังคับ)
   - ระหว่างขั้น 6 (PMI) — review milestone/KPI เป็นระยะ

5. OUTPUT
   Board deck (strategic rationale + synergy case + integration plan) + PMI tracking dashboard
```

### 4C. AI Pain Points + หลักฐาน (ตอบเกณฑ์ a, d)

**Synergy hypothesis generation:** AI parse filing/product doc/internal note สร้าง buyer rationale + synergy hypothesis "จากที่เคยใช้สัปดาห์เหลือชั่วโมง" ([auxi.ai](https://www.auxi.ai/blog/ai-in-investment-banking-pitchbooks-generation))

**Strategic fit screening:** เหมือน PE screening — AI ให้คะแนนเป้าหมายเทียบ strategic criteria ได้เร็ว

**PMI/integration tracking:** synergy หลุดบ่อยเพราะ integration ล้มเหลว — AI standardize synergy KPI tracking ข้าม function

**หลักฐานตัวเลข:** McKinsey — **Generative AI ลดต้นทุน M&A ลง 20%** ([cfodive.com อ้าง McKinsey](https://www.cfodive.com/news/generative-ai-reduces-merger-acquisition-costs-20percent-mckinsey/812514/)); Deloitte GenAI in M&A — 86% adoption, use case 40% strategy/market assessment (ตรงกับงาน corp dev)

**Caveat:** synergy มักถูก overstate ตอนเสนอ board — AI ที่ generate synergy ต้องมี human validation เข้ม (ตรง gate ขั้น 4)

### 4D. Quant/Model Detail

- **Synergy NPV:** ประเมิน cost synergy (ลดพนักงานซ้ำ, รวม procurement) + revenue synergy (cross-sell) → discount เป็น NPV, หัก integration cost + one-time charge
- **Accretion/Dilution:** pro forma EPS ของ combined entity (รวม financing + synergy) เทียบ acquirer standalone EPS
- **Combined DCF:** value ของ combined entity รวม synergy vs sum ของ standalone
- **Synergy realization tracking:** actual synergy captured / planned synergy (KPI ต่อ function ต่อไตรมาส)

### 4E. Step-Level Task Graph — M&A (ป้อน L1)

| ขั้น | Input | Output | Actor/Role | Parallel/Seq | เวลา/effort | Decision/Branch | Pain point |
|---|---|---|---|---|---|---|---|
| 1 Strategy+Criteria | corporate strategy, board mandate | `{acquisition_criteria, hunting_mandate}` | Corp Dev Head | Seq | ต่อเนื่อง | strategy ไม่ชัด → ไม่ล่า | strategy fit หลุดง่ายถ้าเกณฑ์คลุมเครือ |
| 2 Sourcing+Fit | mandate + market scan | `{fit_scored_targets[]}` | Corp Dev Analyst | Seq | ต่อเนื่อง | fit ต่ำ → reject | scout ตลาดกว้าง เห็นไม่ทั่ว |
| 3 Synergy Modeling | target financials + acquirer data | `{synergy_NPV, dilution, combined_DCF}` | Corp Dev + Finance | Seq | ~2-4 สัปดาห์ | synergy ไม่คุ้ม → drop | synergy overstate เสี่ยง |
| 4 DD+Synergy Validation | synergy model + DD | `{validated_synergy, integration_cost}` | Corp Dev + external advisor | **Parallel** (financial/commercial/tech DD) | ~1-3 เดือน | synergy จริงต่ำกว่าคาด → renegotiate/kill | validate synergy hypothesis ยาก |
| 5 Board Approval+Deal | validated case | `{signed_agreement}` | Corp Dev Head + CFO/CEO | Seq | ~1-4 เดือน | board ปฏิเสธ → จบ | เตรียม board deck |
| 6 PMI | signed deal + integration plan | PMI dashboard (synergy actual vs plan) | Integration Mgmt Office | **Parallel** (ทุก function พร้อมกัน) | 1-3 ปี | synergy หลุด → escalate | integration ล้ม = synergy หาย |

### 4F. L2 Orchestration Spec — M&A (ป้อน L2)

| ขั้น | Agent(s) | Pattern (Anthropic) | Debate/maker-checker | Quant binding | Handoff object |
|---|---|---|---|---|---|
| 1 Strategy | Strategy-agent (แปลง strategy→criteria) | **Context-Augmentation** (ดึง corporate strategy doc) | — | — | `{criteria, mandate}` |
| 2 Sourcing+Fit | Sourcing-agent, Fit-agent | **Routing** (fit สูง/ต่ำ) | Fit (maker) ↔ Checker | fit scoring rules | `{fit_targets[]}` |
| 3 Synergy Modeling | Synergy-agent, Model-agent | **Orchestrator-Workers** (แตก cost/revenue synergy + dilution) | Synergy (maker) ↔ Verify (ตรวจเลข) | เรียก synergy NPV / accretion-dilution engine (code จริง) | `{synergy_NPV, dilution}` |
| 4 DD+Validation | DD-agent (หลาย lane), Validator-agent (ท้าทาย synergy) | **Parallelization** + **Evaluator-Optimizer** | Synergy-agent (maker) ↔ Validator (checker เข้ม เพราะ overstate เสี่ยง) | เรียก sensitivity tool บน realization % | `{validated_synergy}` → **human gate** |
| 5 Board Approval | Board-deck-agent, Judge-agent | **Orchestrator-Workers** + agent-as-a-judge | Deck (maker) ↔ Judge (เลียน board) | — | board deck → **human gate (board)** |
| 6 PMI | PMI-tracker-agent (ต่อ function) | **Parallelization-sectioning** (ทุก function ขนาน) | Tracker (maker) ↔ Checker (flag synergy หลุด) | เรียก KPI tracking tool (actual vs plan) | PMI dashboard |

---

## 5. Sector — Investment Banking (M&A Advisory)

### 5A. Workflow เต็ม — Sell-side & Buy-side

Investment Banking (IB) แบบ M&A advisory คือ **ที่ปรึกษารับค่าธรรมเนียม** — ไม่ได้ซื้อเอง แต่ช่วย client (seller หรือ buyer) ทำดีลให้สำเร็จ **ต่างจาก PE/M&A: banker เป็น advisor ไม่ใช่ principal** รายได้มาจาก success fee ไม่ใช่ผลตอบแทนการลงทุน

**Sell-side timeline จริง: 9-12 เดือนจาก mandate ถึงปิดดีล** (execution period engagement→signing ~6-9 เดือน) แบ่ง 3 ช่วงใหญ่:
- Drafting process material + หา buyer (~2-3 เดือน)
- Running auction + ได้ winning bid (~3-4 เดือน)
- Confirmatory diligence + เจรจา definitive agreement (~1-3 เดือน)

**Engagement Letter** (จุดเริ่ม) — กำหนดขอบเขตงาน, fee structure, expense reimbursement, indemnification, **exclusivity (bank เป็น sole sell-side advisor 12-18 เดือน)**

**Sell-side 5 ขั้น (หลัง engagement letter):**
1. **Preparation** — รวบรวมงบ, ร่าง **CIM (Confidential Information Memorandum)**, สร้าง buyer list
2. **Marketing** — ส่ง **teaser** (anonymous one-pager), เซ็น **NDA**, กระจาย CIM ให้ buyer สนใจ
3. **Bidding** — เก็บ **IOI (Indication of Interest)**, จัด management presentation, รับ **LOI**
4. **Due Diligence** — เปิด **data room (VDR)** ให้ buyer ตรวจ financial/legal/operational + จัดการ buyer Q&A
5. **Closing** — เจรจา purchase agreement (SPA), disclosure schedule, ปิดดีล — ผ่าน regulatory clearance (อาจกิน "หลายสัปดาห์ถึงเกิน 1 ปี" ขึ้นกับความซับซ้อน antitrust)

**Buy-side (กลับด้าน):** origination เป็น **target-driven** ไม่ใช่ mandate-driven — banker หาบริษัทเฉพาะเจาะจงให้ client ซื้อ แทนรอ seller มาหา — **IC memo แทนที่ CIM** (เอกสารเสนอฝั่งซื้อ)

**Pitch (ก่อน mandate):** สร้าง pitchbook (market map, comps, football field) — Day 1 associate ดึง research + build template ก่อนเริ่มวิเคราะห์

### 5B. TEMPLATE กรอกเต็ม — Investment Banking (M&A Advisory)

```
สายงาน: Investment Banking (M&A Advisory, sell-side)

1. WORKFLOW STEPS
   ขั้น 0: Pitch                    → งาน: สร้าง pitchbook ชนะ mandate (market map/comps/football field)
   ขั้น 1: Preparation             → งาน: ร่าง CIM, spread การเงิน, สร้าง buyer list
   ขั้น 2: Marketing               → งาน: ส่ง teaser, จัดการ NDA, กระจาย CIM
   ขั้น 3: Bidding                 → งาน: เก็บ IOI, management presentation, รับ LOI
   ขั้น 4: Due Diligence           → งาน: run data room, จัดการ buyer Q&A
   ขั้น 5: Closing                 → งาน: เจรจา SPA, disclosure schedule, ปิดดีล

2. QUANT/MATH FRAMEWORK
   ขั้น 0/1 → Trading Comps, Precedent Transactions, DCF, LBO (financial sponsor bid floor),
              Accretion/Dilution — นำเสนอเป็น football field
   ขั้น 3   → เปรียบเทียบ bid (IOI/LOI) เทียบ valuation range

3. INPUT DATA
   - Public: announced-deal EV/LTM metric (precedent), peer financials (comps), target filing
   - Deal-specific: CIM content, data room documents, buyer Q&A (ลับ — ใช้ proxy สำหรับ demo)

4. GATE POINTS
   - หลังขั้น 0/1 (Pitch/CIM) — senior banker (MD) review ก่อนส่ง client/buyer
   - ขั้น 3 (Bidding) — เลือก winning bid ต้องคนตัดสิน
   - ขั้น 5 (Closing) — legal + MD sign-off ก่อนปิดดีล

5. OUTPUT
   Pitchbook / CIM (sell-side) หรือ IC memo (buy-side) + fairness opinion + closed deal
```

### 5C. AI Pain Points + หลักฐาน (ตอบเกณฑ์ a, d)

**Pitchbook/CIM drafting (จุดปวดหลัก):** ใช้เวลาหลายสิบชั่วโมงต่อดีล — GenAI สร้าง slide brand-compliant ใน PowerPoint ตรง ลด manual formatting/table rebuild/content structuring **ได้ถึง 50%** ([chatfin.ai](https://chatfin.ai/blog/ai-pitchbook-presentation-automation-for-investment-banking-2026/)) — client เคยบีบ CIM creation จาก 6 สัปดาห์เหลือ 10 วัน

**Comps spreading:** standardize peer financials (จุดปวด #2)

**Contract/DD review:** change-of-control clause + restriction (จุดปวด #3)

**หลักฐานตัวเลข:** Deloitte Insights ("Unleashing a new era of productivity in investment banking") — **top 14 global IB เพิ่ม front-office productivity 27-35%** ด้วย GenAI, IB-division gain ~34%, รายได้เพิ่ม ~US$3.5M ต่อ front-office employee ภายในปี 2026

**Fairness opinion + synergy:** AI parse filing/product doc/internal note สร้าง buyer rationale + synergy hypothesis "จากสัปดาห์เหลือชั่วโมง"

**⚠️ Caveat สำคัญ (ต้องพูดตอน pitch):** AI ยัง**คำนวณการเงินหลายขั้นตอนพลาดบ่อย**, สร้าง **IB-standard chart ไม่ได้ดี** (waterfall, football field), **hallucination เป็นความเสี่ยงจริง** (general Copilot เคยสร้างตัวเลขปลอม "43% vs actual 12%") — **best practice 2026: "AI ร่างก่อน + senior banker review + strategic overlay" ไม่ใช่ full-autonomous end-to-end** ([finalis.com](https://www.finalis.com/blog/the-real-impact-of-ai-on-dealmaking-what-boutique-investment-banks-need-to-know-in-2026)) — ตรงกับ L3 human-gate ของ engine

### 5D. Quant/Model Detail
ใช้ valuation mechanics เดียวกับ §3D (Trading Comps, Precedent Transactions, DCF, LBO เป็น financial-sponsor-bid floor, Accretion/Dilution) — นำเสนอรวมเป็น **football field** (แสดง valuation range จากหลายวิธีเทียบกัน)

### 5E. Step-Level Task Graph — Investment Banking (ป้อน L1)

| ขั้น | Input | Output | Actor/Role | Parallel/Seq | เวลา/effort | Decision/Branch | Pain point |
|---|---|---|---|---|---|---|---|
| 0 Pitch | client lead + market data | pitchbook | Analyst→MD | Seq | Day 1 grind | ไม่ชนะ mandate → จบ | หลายสิบชม./ดีล, Day1 build template |
| 1 Preparation | engagement letter + target financials | CIM + buyer list | Analyst/Associate | **Parallel** (CIM draft + comps spread + buyer list) | ~2-3 เดือน | — | CIM drafting กินเวลา (6 สัปดาห์) |
| 2 Marketing | CIM + buyer list | signed NDA + CIM distributed | Associate/VP | Seq | (ในช่วง 2-3 เดือนแรก) | buyer ไม่สนใจ → ขยาย list | teaser/NDA workflow |
| 3 Bidding | buyer interest | `{IOI[], LOI[], shortlist}` | VP/MD | Seq | ~3-4 เดือน | bid ต่ำเกิน → renegotiate/ถอน | เทียบ bid หลายราย |
| 4 Due Diligence | LOI winner | data room Q&A resolved | Associate/VP | **Parallel** (buyer หลายราย + หลาย workstream) | ~1-3 เดือน | DD เจอปัญหา → price adjust | จัดการ VDR + Q&A กระจัดกระจาย |
| 5 Closing | confirmatory DD | signed SPA | VP/MD + legal | Seq | ~1-3 เดือน | regulatory ไม่ผ่าน → delay/kill | เจรจา SPA + disclosure |

### 5F. L2 Orchestration Spec — Investment Banking (ป้อน L2)

| ขั้น | Agent(s) | Pattern (Anthropic) | Debate/maker-checker | Quant binding | Handoff object |
|---|---|---|---|---|---|
| 0 Pitch | Research-agent, Comps-agent, Deck-agent | **Orchestrator-Workers** (pitchbook มี sub-task หลากหลาย: market map/comps/football field) | Deck (maker) ↔ MD-Judge (checker) | เรียก comps/precedent/DCF engine → football field | pitchbook → **human gate (MD)** |
| 1 Preparation | CIM-agent, Comps-agent, Buyerlist-agent | **Parallelization-sectioning** | CIM (maker) ↔ Verify (ตรวจเลข vs source) | เรียก comps spread tool (scrub/normalize) | `{CIM, buyer_list}` |
| 2 Marketing | Teaser-agent, NDA-tracker | **Prompt-Chaining** (teaser→NDA→CIM) | — | — | `{distributed_status}` |
| 3 Bidding | Bid-eval-agent | **Parallelization-voting** (เทียบ bid หลายราย) | Bid-eval (maker) ↔ Checker | เรียก valuation-range compare tool | `{ranked_bids}` → **human gate** |
| 4 Due Diligence | DD-QA-agent, Redflag-agent | **Routing** (route Q&A ไป workstream) + **Evaluator-Optimizer** | Redflag (maker) ↔ Checker | — | `{dd_resolved, price_adjustments}` |
| 5 Closing | SPA-agent, Legal-check-agent | **Evaluator-Optimizer** (ร่าง↔ตรวจ) | SPA (maker) ↔ Legal-check (checker) | — | signed SPA → **human gate (MD+legal)** |

---

## 6. Sector — Equity Research (sell-side)

### 6A. Workflow เต็ม (6 ขั้น)

| ขั้น | งานในขั้น | รายละเอียด |
|---|---|---|
| **1. Coverage Initiation** | เขียน initiation report | primer เจาะลึกบริษัท/อุตสาหกรรม — IPO prospectus ยาว 400-600 หน้า, initiation report เองยาว **20-50 หน้า** (บางที่ 50-100+) |
| **2. Financial Modeling** | สร้างโมเดล | build **3-statement model** (IS/BS/CF เชื่อมกัน) + valuation model |
| **3. Valuation & Rating** | ประเมิน + กำหนด rating | ใช้ earnings-multiple เป็นหลัก (ดู §6D) กำหนด Buy/Hold/Sell + price target (12-เดือน) |
| **4. Draft Report** | ร่างรายงาน | investment thesis, สรุปประเด็น, เหตุผลของ rating |
| **5. Compliance Review + Sign-off** | ตรวจ+อนุมัติ | **บังคับกฎหมาย** licensed analyst ต้อง sign-off (MiFID II/Reg AC) + "reasonable and adequate basis" (FINRA) |
| **6. Publish + Client Communication** | เผยแพร่ | ส่งรายงาน, host/attend roadshow, รับสาย buy-side PM/analyst |

**Earnings Update Cycle (ความถี่สูงสุด — ทุกไตรมาส):** ทำซ้ำขั้น 2-6 แบบเร่งด่วนทุกครั้งบริษัทประกาศผล — ก่อน AI ใช้ **5.7 ชม./บริษัท** ตอน peak earnings season, ปัจจุบันบีบเหลือ **45 นาที (ลด 87%)** ([marvin-labs.com](https://www.marvin-labs.com/solutions/earnings-season/))

**บริบทเสริม:** coverage ขยายจาก **30-40 บริษัท/analyst (ต้นยุค 2000)** เป็น **50-60+ ปัจจุบัน**, earnings call ยาวขึ้นจาก 45 เป็น **90 นาที**

### 6B. TEMPLATE กรอกเต็ม — Equity Research (sell-side)

```
สายงาน: Equity Research (sell-side)

1. WORKFLOW STEPS
   ขั้น 1: Coverage Initiation      → งาน: เขียน primer ลึกบริษัท/อุตสาหกรรม
   ขั้น 2: Financial Modeling       → งาน: สร้าง 3-statement model + valuation model
   ขั้น 3: Valuation & Rating       → งาน: ประเมิน กำหนด Buy/Hold/Sell + price target
   ขั้น 4: Draft Report             → งาน: ร่าง investment thesis + บทวิเคราะห์
   ขั้น 5: Compliance Review        → งาน: licensed analyst ตรวจ+เซ็นก่อนเผยแพร่ (บังคับกฎหมาย)
   ขั้น 6: Publish                  → งาน: เผยแพร่ + สื่อสารลูกค้า/roadshow

2. QUANT/MATH FRAMEWORK
   ขั้น 2 → 3-statement model (IS/BS/CF เชื่อมกัน)
   ขั้น 3 → Earnings-multiple/P/E approach (default — ใช้จริง 93-94.5%, ดู §6D),
            Trading Comps (EV/EBITDA, EV/EBIT, EV/Revenue, P/E), DCF (ใช้จริงแค่ 4-13%, ทางเลือกเสริม)

3. INPUT DATA (public 100% — PDPA risk ต่ำสุดในทุกสาย)
   - Public filings (10-K/10-Q หรือ 56-1/แบบรายงานประจำปีของไทย)
   - Consensus estimates (Bloomberg/Refinitiv/IBES-style)
   - Earnings call transcripts
   - Historical price data
   - Industry/sector data, comps set (peer companies)

4. GATE POINTS
   - หลังขั้น 3 (Valuation) — ตรวจ rating มี "reasonable and adequate basis" (CFA/FINRA)
   - ขั้น 5 (Compliance Review) — บังคับกฎหมาย ห้าม AI เผยแพร่เองโดยไม่มี licensed analyst เซ็น

5. OUTPUT
   Research report (initiation 20-50+ หน้า หรือ earnings note สั้นกว่า)
   + Rating (Buy/Hold/Sell) + Price target (12-เดือน horizon)
```

### 6C. AI Pain Points + หลักฐาน (ตอบเกณฑ์ a, d)

**Earnings-season coverage (จุดปวดหลัก):** **5.7 ชม. → 45 นาที/บริษัท (ลด 87%)** จาก Marvin Labs — research agent auto-generate earnings review ภายในนาทีหลัง filing publish, monitor live transcript, maintain living doc ที่อัปเดตเอง ([marvin-labs.com](https://www.marvin-labs.com/solutions/earnings-season/))

**ภาพรวมที่แรงกว่าเดิม:** 5 core workflow กิน **70-80% ของเวลา analyst ทั้งหมด** — automate รวมกันได้ **ลดงาน 40% หรือคืนเวลา 20-25 ชม./สัปดาห์** ให้ analyst ไปทำ strategic analysis/relationship/conviction development

**Report drafting:** สร้าง first-draft note จากตัวเลข analyst เอง + house style — **ข้อจำกัดกฎหมาย: MiFID II/Reg AC บังคับ licensed analyst review+sign-off ก่อนเผยแพร่, ต้องมี audit trail + MNPI control**

**Caveat:** general AI เคยสร้างตัวเลขปลอม ("43% vs actual 12%"), สร้าง IB chart ไม่ได้ดี — hallucination จริง ต้อง human review

### 6D. Rating/Valuation Methodology Detail (cross-verified — ตอบเกณฑ์ b)

**Earnings-multiple ครองตลาด (ยืนยัน 2 แหล่งอิสระ):**
- **94.5% ของ analyst ใช้ multiples approach, DCF ใช้แค่ 4% ของ recommendation** (การศึกษาตลาดอินเดีย [tandfonline](https://www.tandfonline.com/doi/full/10.1080/23322039.2024.2423261))
- **93% ใช้ multiple approach** (78% holistic + 15% homogeneous SOTP)
- วิธีมาตรฐาน: คูณ earnings forecast ด้วย P/E ที่เหมาะกับบริษัท/อุตสาหกรรม → price target 12 เดือน

**Insight สำคัญ — DCF ไม่ได้แม่นกว่า:** price target hit rate: **DCF 52.3%** vs **revenue-multiple 55.1%** (48.4-55.1% ข้าม multiple แบบต่างๆ) → **การตั้ง default engine เป็น comps/multiple ไม่ใช่แค่พฤติกรรม analyst แต่ accuracy จริงก็ดีกว่า/เท่า DCF** — จุดขายเชิงหลักฐานว่า design เลือก quant model ถูก

**Rating scale:** Buy (คาด outperform ตลาด) / Hold (average) / Sell (underperform) — บางที่ใช้ Strong Buy...Strong Sell หรือ 1-5 — rating change (upgrade/downgrade) มี information มากกว่า static rating

### 6.4 Regulatory เต็ม (โยงตรง L3 human-gate)

- **MiFID II / Reg AC** — บังคับ licensed analyst review+sign-off ก่อนเผยแพร่ทุกฉบับ, ต้องมี audit trail + MNPI control — **primary source: ESMA — Article 52 MiFID II Delegated Regulation** (firm ต้องอธิบายขอบเขต instrument ที่แนะนำได้ + analyst ต้อง physically separated จากผู้มี conflict of interest) ([esma.europa.eu](https://www.esma.europa.eu/sites/default/files/library/esma35-43-349_mifid_ii_qas_on_investor_protection_topics.pdf))
- **FINRA** — recommendation/rating/price-target ต้องมี **"reasonable basis"** และเป็นอิสระจาก conflict of interest
- **CFA Institute Standard** — research/recommendation ต้อง objective มี **"reasonable and adequate basis"**, แยก fact กับ opinion ชัดเจน
- **ผลต่อ design:** ตรงกับ L3 (human gate) + L2 (grounding+citation) อยู่แล้ว — แค่ทำให้ gate ขั้น 5 เป็น **บังคับ ไม่ใช่ optional**

### 6E. Step-Level Task Graph — Equity Research (ป้อน L1)

| ขั้น | Input | Output | Actor/Role | Parallel/Seq | เวลา/effort | Decision/Branch | Pain point |
|---|---|---|---|---|---|---|---|
| 1 Initiation | filing + industry data | `{company_primer, thesis_draft}` | Analyst | Seq | สัปดาห์-เดือน (ครั้งเดียว) | นอก coverage → ข้าม | prospectus 400-600 หน้า |
| 2 Financial Modeling | filing + historical | `{3statement_model, forecast}` | Analyst/Associate | Seq | 5.7 ชม./บริษัท (earnings) | model ไม่ tie → แก้ | model update ซ้ำทุกไตรมาส |
| 3 Valuation & Rating | model + comps + consensus | `{price_target, rating}` | Analyst | Seq | ต่อจากขั้น 2 | rating ไม่มี basis → กลับไปแก้ | ต้องมี reasonable basis |
| 4 Draft Report | valuation + thesis | `{draft_note}` | Analyst | Seq | 45 นาที-ชม. (ด้วย AI) | — | drafting ตาม house style |
| 5 Compliance Review | draft note | `{approved_note}` | **Licensed Analyst (supervisor)** | Seq | — | ไม่ผ่าน → กลับแก้ | **บังคับกฎหมาย sign-off** |
| 6 Publish | approved note | published report + rating | Analyst + sales | Seq | — | — | สื่อสาร buy-side |

### 6F. L2 Orchestration Spec — Equity Research (ป้อน L2)

| ขั้น | Agent(s) | Pattern (Anthropic) | Debate/maker-checker | Quant binding | Handoff object |
|---|---|---|---|---|---|
| entry | Router-agent (initiation vs earnings-update = 2 path) | **Routing** | — | — | route decision |
| 1 Initiation | Primer-agent | **Context-Augmentation** (ดึง filing/industry) | Primer (maker) ↔ Checker | — | `{primer}` |
| 2 Financial Modeling | Model-agent | **Prompt-Chaining** (IS→BS→CF เชื่อมกัน) | Model (maker) ↔ Verify (ตรวจ model tie) | เรียก 3-statement engine (คำนวณ code จริง ไม่ให้ LLM เดาเลข) | `{model, forecast}` |
| 3 Valuation & Rating | Valuation-agent, Rating-agent | **Orchestrator-Workers** | Rating (maker) ↔ Basis-checker (ตรวจ reasonable basis) | เรียก comps/multiple engine (default) + DCF (option) | `{price_target, rating}` |
| 4 Draft Report | Draft-agent | **Prompt-Chaining** | Draft (maker) ↔ Fact-checker (แยก fact/opinion) | — | `{draft_note}` |
| 5 Compliance | Compliance-agent (pre-check) → **human licensed analyst** | **Evaluator-Optimizer** | Compliance (maker) ↔ human (final) | — | `{approved}` → **human gate (บังคับ)** |
| 6 Publish | Publish-agent | **Prompt-Chaining** | — | — | published report |

---

## 7. Sector — Risk / Model Validation

### 7A. Workflow เต็ม 7 ขั้น (อิง SR 11-7 + Basel CRR Art.185 + BOT Guideline)

**กรอบอ้างอิงหลัก:**
- **SR 11-7** (Federal Reserve/OCC, สหรัฐฯ) — **3 core validation activities**: conceptual soundness evaluation, outcomes analysis, benchmarking
- **Basel CRR Article 185** (EU) — บังคับ validate IRB model สม่ำเสมอ ครอบทั้ง qualitative (design/documentation/governance/management oversight) และ quantitative (backtest/benchmark)
- **BOT AI Risk Management Guidelines** (ธนาคารแห่งประเทศไทย ประกาศจริง 12 ก.ย. 2025 ต่อยอดจากร่างเดือน มิ.ย. 2025) — ครอบ financial service provider ทุกแห่งภายใต้ Financial Institution Business Act + payment provider ภายใต้ Payment Systems Act, ครอบทั้ง AI ที่พัฒนาเอง+จาก third-party — **2 เสาหลัก: (1) governance การใช้ AI (2) AI system development + security control** อิงหลัก **FEAT** (Fairness, Ethics, Accountability, Transparency) — core validation principle ตรงกัน: **conceptual soundness, data quality, performance testing** ([tilleke.com](https://www.tilleke.com/insights/thailand-issues-ai-risk-management-guidelines-for-financial-service-providers/25/)) — **จุดป้องกันการก็อปแรงสุด: กรอบไทยที่ใหม่มาก จากหน่วยงานกำกับดูแลไทยโดยตรง**

| ขั้น | งาน | เทคนิค/มาตรฐาน |
|---|---|---|
| **1. Scope + Tiering** | ระบุ model ที่ต้อง validate จัด tier ตาม materiality | Tier 1 (กระทบ capital/credit decision ใหญ่) = full independent validation + ongoing monitoring; tier ต่ำกว่า = periodic review เบากว่า |
| **2. Conceptual Soundness** | ตรวจ theory/methodology/assumption เหมาะกับ intended use ไหม | Basel Art.185 qualitative checklist — mathematical framework, simplifying assumption สมเหตุสมผล, ครอบ key risk factor |
| **3. Data Quality** | เช็ค input data ที่ใช้ train/run สะอาด/ครบ | completeness check, PSI (Population Stability Index) |
| **4. Quantitative Testing** | backtest, benchmark, sensitivity, out-of-time test | Backtesting, Benchmarking, Sensitivity Analysis, เช็ค discrimination/calibration/stability |
| **5. Outcomes Analysis** | เทียบ prediction จริงระยะยาวกับที่คาดการณ์ | drift detection, ongoing performance monitoring |
| **6. Findings + Rating** | สรุปผล risk rating, severity, remediation | Rating green/amber/red (หรือ numeric), ระบุ limitation, remediation owner+deadline |
| **7. Governance Sign-off** | เสนอ model risk governance committee | อนุมัติ / อนุมัติแบบมีเงื่อนไข / ต้อง remediate ก่อน — **บังคับมนุษย์ ห้าม AI ตัดสินเอง** |

**Credit model เฉพาะทาง (PD/LGD/EAD):**
- **F-IRB:** bank ประเมิน PD เอง, regulator กำหนด LGD/EAD
- **A-IRB:** bank ประเมินเองทั้ง PD/LGD/EAD
- Validate ด้วย backtest + out-of-time test + benchmarking + เช็ค discrimination/calibration/stability

**ความถี่:** model ความเสี่ยงสูง/ซับซ้อน/material ต้อง validate **อย่างน้อยปีละครั้ง** — performance เปลี่ยน trigger validation รอบใหม่ทันที

**Independent validation:** ผู้ validate ต้อง**ไม่มีสายบังคับบัญชาเดียวกับทีมสร้าง model** มี authority+expertise ทำ **"effective challenge"** (ไม่ใช่ rubber-stamp)

### 7B. TEMPLATE กรอกเต็ม — Risk / Model Validation

```
สายงาน: Risk / Model Validation

1. WORKFLOW STEPS
   ขั้น 1: Scope + Tiering          → งาน: ระบุ model ต้อง validate, จัด risk tier
   ขั้น 2: Conceptual Soundness     → งาน: ตรวจ theory/methodology/assumption
   ขั้น 3: Data Quality             → งาน: เช็ค input data สะอาด/ครบ
   ขั้น 4: Quantitative Testing     → งาน: backtest, benchmark, sensitivity, out-of-time
   ขั้น 5: Outcomes Analysis        → งาน: เทียบ prediction จริง vs คาดการณ์ระยะยาว
   ขั้น 6: Findings + Rating        → งาน: สรุป risk rating + remediation plan
   ขั้น 7: Governance Sign-off      → งาน: เสนอ model risk committee อนุมัติ (บังคับมนุษย์)

2. QUANT/MATH FRAMEWORK
   ขั้น 3 → completeness check, PSI (Population Stability Index)
   ขั้น 4 → Backtesting, Benchmarking, Sensitivity Analysis, KS test,
            discrimination/calibration/stability (สำหรับ credit: PD/LGD/EAD backtest)
   ขั้น 5 → drift detection

3. INPUT DATA
   - Model documentation (ของ model ที่จะถูกตรวจ)
   - Loan-level/transaction-level data (credit model)
   - Historical prediction vs actual outcome data
   - Prior validation report (ถ้ามี)
   - External benchmark data/model (สำหรับ benchmarking)

4. GATE POINTS
   - ขั้น 4 (Quantitative Testing) — คนอ่านผลตรวจเชิงปริมาณก่อนสรุป finding
   - ขั้น 7 (Governance Sign-off) — บังคับกฎหมาย (SR 11-7/Basel Art.185/BOT Guideline)
     ห้าม AI อนุมัติเอง ต้องผ่าน model risk governance committee

5. OUTPUT
   Validation Report (risk rating green/amber/red + findings + limitation +
   remediation action พร้อม owner+deadline) + Governance committee decision record
```

### 7C. AI Pain Points + หลักฐาน (ตอบเกณฑ์ a, d)
- **Manual validation ใช้เวลานาน** — conceptual review + backtest + documentation กินแรง; AI decompose เป็น sub-task ให้ agent เฉพาะทางได้ (แต่ขั้น sign-off ยังต้องคน)
- **Drift monitoring** ต้องเฝ้าต่อเนื่อง — AI agent monitor แบบ real-time flag เมื่อ threshold แตก
- **หลักฐาน adoption:** finance team ~44% deploy agentic AI ปี 2026 (โต 600%+ จาก 2025), Goldman/JPMorgan deploy agentic AI at scale ([ruh.ai](https://www.ruh.ai/blogs/tradingagents-playbook-multi-agent-ai-financial-services))

### 7.3 ทำไมสายนี้พิสูจน์ L7 (Governance) ได้ชัดสุด — "Engine ตรวจสอบตัวเอง"
Workflow ของ Risk/Model Validation **คือของจริงที่ layer Governance ของ engine อ้างอิงอยู่แล้ว** (SR 11-7/BOT Guideline) — ถ้าทำสายนี้ demo ได้ = พิสูจน์ว่า engine เข้าใจมาตรฐาน model-risk จริง ไม่ใช่พูดลอย

**มุมแรง (meta-validation):** เอา governance layer ของ engine (ที่ตรวจ output สายอื่น เช่น PE valuation model, ER rating model) ไปใช้ตรวจตัว engine เอง = สถาปัตยกรรมเดียวกันที่**ตรวจสอบตัวเอง** — pitch: "engine ไม่ใช่แค่ทำงาน แต่ validate งานตัวเองได้ตามมาตรฐาน regulator"

**ข้อจำกัดตรงๆ:** สายนี้ "เท่" น้อยกว่า PE ตอน demo — ไม่มี deal/valuation number ใหญ่ให้ตื่นเต้น เป็น back-office/compliance ต้องมี "โมเดลอื่น" ให้ตรวจก่อน — เหมาะเป็น**สายเสริมโชว์ Governance** มากกว่า flagship

### 7D. Validation Technique Detail เต็ม
- **Backtesting:** เทียบ model output กับ actual outcome อดีต — predicted risk measurement (PD/LGD/CCF) เทียบ observed ด้วย test statistic เพื่อประเมิน calibration/discrimination/stability
- **Benchmarking:** เทียบผล model/metric กับ model อื่น หรือ external reference/standard — ประเมิน relative performance/validity/robustness
- **Sensitivity Analysis:** ตรวจการเปลี่ยน input/assumption ส่งผลต่อ output ยังไง
- **กรอบครบวงจร:** independent validation + backtesting + stress testing + benchmarking + sensitivity analysis
- **Validation Report ต้องมี:** risk rating (green/amber/red), findings, limitations, conditions for approval + severity rating + remediation tracking จนปิด (unresolved → escalate ผ่าน governance channel)
- **Governance Workflow:** development doc + validation report → model risk governance committee → อนุมัติ/มีเงื่อนไข/ต้อง remediate — decision+เงื่อนไขบันทึกลายลักษณ์อักษร
- **Governance คือ:** policy, roles/responsibilities, risk appetite statement, escalation procedure, board-level oversight — รับประกัน development+validation ทำงานด้วยความเป็นอิสระ

### 7E. Step-Level Task Graph — Risk/Model Validation (ป้อน L1)

| ขั้น | Input | Output | Actor/Role | Parallel/Seq | เวลา/effort | Decision/Branch | Pain point |
|---|---|---|---|---|---|---|---|
| 1 Scope+Tiering | model inventory | `{model_tier, validation_scope}` | Validation lead | Seq | สั้น | Tier ต่ำ → light review | จัด tier ตาม materiality |
| 2 Conceptual Soundness | model doc | `{soundness_findings}` | Independent validator | Seq | สัปดาห์ | methodology พัง → return to dev | ตรวจ assumption ลึก |
| 3 Data Quality | training/run data | `{data_quality_flags, PSI}` | Validator (quant) | **Parallel** (หลาย data check) | วัน-สัปดาห์ | data ไม่ผ่าน → หยุด | completeness/PSI |
| 4 Quantitative Testing | model + historical outcome | `{backtest_result, benchmark_gap}` | Validator (quant) | **Parallel** (backtest/benchmark/sensitivity ขนาน) | สัปดาห์ | fail test → finding severity สูง | discrimination/calibration/stability |
| 5 Outcomes Analysis | prediction vs actual | `{drift_status}` | Validator | Seq/ongoing | ต่อเนื่อง | drift แตก threshold → re-validate | เฝ้าต่อเนื่อง |
| 6 Findings+Rating | ทุก output ข้างบน | `{risk_rating, remediation_plan}` | Validation lead | Seq | สัปดาห์ | severity สูง → **escalate ทันที ไม่รอรอบถัดไป** | rating+remediation tracking |
| 7 Governance Sign-off | validation report | committee decision record | **Model Risk Committee (มนุษย์)** | Seq | — | ปฏิเสธ → remediate; อนุมัติ | บังคับกฎหมาย ห้าม AI ตัดสิน |

### 7F. L2 Orchestration Spec — Risk/Model Validation (ป้อน L2)

| ขั้น | Agent(s) | Pattern (Anthropic) | Debate/maker-checker | Quant binding | Handoff object |
|---|---|---|---|---|---|
| 1 Scope+Tiering | Tiering-agent | **Routing** (tier→depth) | — | tiering rules | `{tier, scope}` |
| 2 Conceptual Soundness | Review-agent | **Context-Augmentation** (ดึง model doc + Basel checklist) | Review (maker) ↔ Challenger (effective challenge) | — | `{soundness_findings}` |
| 3 Data Quality | DataQC-agent | **Parallelization-sectioning** | DataQC (maker) ↔ Checker | เรียก PSI/completeness tool (code จริง) | `{data_flags, PSI}` |
| 4 Quantitative Testing | Backtest-agent, Benchmark-agent, Sensitivity-agent | **Parallelization-sectioning** (3 test ขนาน) | แต่ละ test-agent (maker) ↔ Verify (checker) | เรียก backtest/KS/benchmark engine (code จริง ไม่ให้ LLM เดาเลข) | `{test_results}` |
| 5 Outcomes Analysis | Drift-agent | **Evaluator-Optimizer** (monitor loop) | Drift (maker) ↔ Checker | เรียก drift-detection tool | `{drift_status}` |
| 6 Findings+Rating | Findings-agent, **Judge-agent** | **Orchestrator-Workers** + **agent-as-a-judge** (ตรงตัวกับ governance) | Findings (maker) ↔ Judge (checker) | — | `{risk_rating, remediation}` |
| 7 Governance Sign-off | Presenter-agent → **Model Risk Committee (มนุษย์)** | — (human decision) | agent เตรียม, มนุษย์ตัดสิน | — | committee record → **human gate (บังคับ)** |

> **หมายเหตุ:** สายนี้ mapping ตรงกับ pattern **agent-as-a-judge** (FinCon) มากที่สุด — manager/judge agent = ผู้สังเคราะห์ก่อนส่ง committee มนุษย์

---

## 8. Cross-sector Synthesis (5 สาย)

### จุดร่วมทั้ง 5 สาย
- **Human gate ก่อน sign-off เป็นข้อบังคับ ไม่ใช่ทางเลือก** — PE: IC · M&A: corporate board · IB: MD+legal · ER: licensed analyst (MiFID II/Reg AC) · Risk: governance committee (SR 11-7/BOT) — engine ทุกสายต้องมี hard-stop
- **ต้องมี grounding/citation ทุก output** — ทุกสายเสี่ยง hallucination สูง (ตัวเลขการเงินผิดกระทบเงินจริง)
- **แยก quant model ออกจาก LLM** — ทุกสายให้ code จริงคำนวณเลข (DCF/LBO/Beneish/backtest) ไม่ให้ LLM เดา — จุดแข็งร่วมของ design
- **PDPA/confidentiality** — ใช้ proxy data (บริษัทมหาชน/public filing/synthetic) ในการ demo ทุกสาย ไม่ใช้ข้อมูลลูกค้าจริง
- **AI ร่างก่อน + คนตรวจ (ไม่ full-autonomous)** — best practice 2026 ตรงกันทุกสาย

### จุด Thai-specific/ป้องกันการก็อป
- **PE/M&A/IB:** DBD extraction (งบเซ็นเป็น PDF สแกนไทย, XBRL mapping error), SET vs Capital IQ (TFRS-16 distortion)
- **Equity Research:** SET vs Capital IQ comps กระทบ valuation ตรง
- **Risk/Model Validation:** **BOT AI Risk Management Guidelines (ก.ย. 2025)** — กรอบไทยใหม่มาก จากหน่วยงานกำกับไทยโดยตรง = จุดป้องกันการก็อปแรงสุด

### คำแนะนำ: สายไหน demo หลัก vs เสริม
- **PE (flagship)** — solution concept (b) แข็งสุด (multi-agent + quant ซับซ้อน + forensic) มี "wow factor"
- **Equity Research (demo เสถียรสุด)** — feasibility (c) สูงสุด: ข้อมูล public 100%, PDPA ต่ำสุด, demo ง่าย/เสถียร
- **M&A** — เด่นเรื่อง synergy + PMI แต่ข้อมูล synergy ลับ ต้อง proxy
- **IB** — เด่น pitchbook automation (ตัวเลข productivity ชัด) แต่ chart-generation ยังเป็นจุดอ่อน AI
- **Risk/Model Validation** — b แข็งจากมุม governance (พิสูจน์ L7) แต่ demo ยาก impact วัดยาก — **สายเสริมโชว์ governance**

---

## 8.5 Engine Layer Input Map — สายไหนป้อนอะไรเข้า layer ไหน

> เดิมไฟล์นี้ป้อน **L1 (task graph §E)** และ **L2 (orchestration §F)** ครบทุกสายแล้ว — ตารางนี้เติมส่วนที่ engine 10-layer ต้องการเพิ่ม: **L0 Ingestion** (เอกสารดิบต่อสาย), **L5 Retrieval** (คลังข้อมูลที่ต้องค้น), **L9 Routing** (ขั้นถูก/แพง) — เพื่อให้ทีม tech เสียบครบทุก layer ไม่ใช่แค่ L1/L2

| สาย | L0 Ingestion (เอกสารดิบที่ต้องแปลง) | L5 Retrieval corpus (คลังที่ต้องค้น) | L9 Routing (ขั้นถูก→model เล็ก / ขั้นแพง→model ใหญ่) |
|---|---|---|---|
| **Private Equity** | CIM (PDF), data room docs, งบย้อนหลัง (สแกน), management presentation | ดีลเก่า (L4), งบ peer, industry report | ถูก: screening, extract งบ · แพง: valuation judgment, IC memo reasoning |
| **M&A (Corp Dev)** | target 10-K/annual report, acquirer strategy doc, product roadmap | synergy case เก่า, deal archetype library | ถูก: fit screening, extract · แพง: synergy modeling, board narrative |
| **Investment Banking** | target filing, precedent-deal 8-K/proxy, peer financials | precedent transaction DB, comps set | ถูก: comps spread, teaser · แพง: fairness opinion, football field synthesis |
| **Equity Research** | filing (10-K/10-Q/56-1), earnings transcript, IPO prospectus | consensus estimate, historical price, peer set | ถูก: earnings extract, model update · แพง: rating decision, thesis reasoning |
| **Risk/Model Validation** | model documentation, loan-level data, prior validation report | benchmark model, historical outcome data | ถูก: data QC, completeness check · แพง: conceptual soundness review, judge decision |

**L8 Schema Contract (handoff object ต่อสาย — เสริมจาก §F):** ทุกสายส่ง handoff เป็น JSON schema บังคับ — ตัวอย่าง field หลักต่อสาย:
- PE: `{financial_health_flags[], adjusted_EBITDA, EV_range, stress_IRR}`
- M&A: `{fit_score, synergy_NPV, dilution, validated_synergy}`
- IB: `{comps_multiples{}, ranked_bids[], valuation_range}`
- ER: `{forecast{}, price_target, rating, basis_citations[]}`
- Risk: `{data_flags[], backtest_result, risk_rating, remediation[]}`

**L4 Memory (จำอะไรข้ามดีลต่อสาย):** PE=multiple/margin ดีลคล้าย · M&A=synergy realization จริง vs plan · IB=precedent bid range · ER=forecast error ย้อนหลัง (เรียนจากพลาด) · Risk=finding pattern ที่เจอบ่อย

**หมายเหตุ:** ตารางนี้ synthesis จากเนื้อหา §3-7 เดิม + นิยาม layer L0/L5/L8/L9 (ดู source ในเอกสาร architecture) — ไม่มี fact ภายนอกใหม่ที่ต้องอ้างเพิ่ม

---

## 9. Gap ที่ยังเปิดอยู่ (finance team ต้องหาต่อ)

- เลือกบริษัทมหาชนตัวไหนเป็น proxy data สำหรับ demo แต่ละสาย — ยังไม่เคาะ
- quant model ตัวไหน implement จริงในเดโม vs พูดเป็น vision (Monte Carlo, LBO 7-step เต็ม, synergy model อาจกินเวลา implement)
- MiFID II/Reg AC — มี ESMA primary source แล้ว แต่เนื้อ Article เต็มยังไม่ fetch ทั้งฉบับ
- Basel SS1/23 (UK), OSFI Guideline E-23 (แคนาดา) — เจอชื่อ framework แต่ยังไม่ deep-dive
- BOT AI Risk Management Guidelines (ก.ย. 2025) — เจอกรอบใหญ่ แต่ยังไม่อ่าน requirement ย่อยระดับข้อ ควร fetch ต้นฉบับก่อนอ้างเจาะจงในสไลด์
- ตัวเลข earnings-multiple (94.5%/93%) มาจากตลาดอินเดีย + survey — ควรหาข้อมูลตลาดไทย/US เสริมถ้าจะเจาะจง
- DBD public API availability ยังไม่ยืนยัน — ออกแบบให้ ingest PDF/Excel ที่ดาวน์โหลดแทนสมมติมี API
- M&A/IB workflow — verify กับ practitioner จริงถ้าเป็นไปได้ (ตอนนี้จากแหล่งเว็บ)

---

## 10. Sources (เฉพาะลิงก์เว็บภายนอก)

**PE / M&A / IB — AI adoption & pain points:**
- Deloitte 2025 GenAI in M&A (press) — https://www.deloitte.com/us/en/about/press-room/deloitte-survey-genai-in-mna.html
- Deloitte 2025 GenAI in M&A (study) — https://www.deloitte.com/us/en/what-we-do/capabilities/mergers-acquisitions-restructuring/articles/m-and-a-generative-ai-study.html
- PwC — Private equity AI transformation — https://www.pwc.com/us/en/industries/financial-services/library/private-equity-ai-transformation.html
- Third Bridge — AI due diligence PE (2026, DD time -60-70%) — https://www.thirdbridge.com/en-us/about-us/media/perspectives/ai-due-diligence-private-equity
- McKinsey — AI in finance (data-crunching -20-30%) — https://www.mckinsey.com/capabilities/strategy-and-corporate-finance/our-insights/how-finance-teams-are-putting-ai-to-work-today
- CFO Dive — GenAI reduces M&A cost 20% (McKinsey) — https://www.cfodive.com/news/generative-ai-reduces-merger-acquisition-costs-20percent-mckinsey/812514/

**M&A Corporate Development:**
- M&A Institute — 6-step M&A strategy — https://mnainstitute.com/ma-strategy/
- SmartRoom — corporate development strategy — https://smartroom.com/blog/industries/corporate/corporate-development-strategy/
- IMAA — 5 steps to unlock M&A synergy value — https://www.imaa-institute.org/blog/5-steps-to-unlock-m-and-a-synergy-value/
- BCG — value from synergy PMI four essential steps — https://www.bcg.com/publications/2025/value-from-synergy-pmi-four-essential-steps
- DealRoom — post-merger integration process — https://dealroom.net/faq/post-merger-and-acquisition-m-a-integration-process

**Investment Banking:**
- IB Interview Questions — M&A pitch process mandate to close — https://ibinterviewquestions.com/blog/m-and-a-pitch-process-from-mandate-to-close
- Exitwise — sell-side M&A process — https://exitwise.com/blog/sell-side-m-a-process
- Auxi — AI in IB pitchbooks — https://www.auxi.ai/blog/ai-in-investment-banking-pitchbooks-generation
- ChatFin — AI pitchbook automation 2026 — https://chatfin.ai/blog/ai-pitchbook-presentation-automation-for-investment-banking-2026/
- Finalis — real impact of AI on dealmaking 2026 — https://www.finalis.com/blog/the-real-impact-of-ai-on-dealmaking-what-boutique-investment-banks-need-to-know-in-2026

**Equity Research:**
- CFA Institute — Elements of a Company Research Report — https://analystprep.com/cfa-level-1-exam/equity/elements-of-company-research-report/
- CFA Institute — Equity Research Report Essentials (PDF) — https://www.cfainstitute.org/sites/default/files/-/media/documents/support/research-challenge/challenge/rc-equity-research-report-essentials.pdf
- CFA Institute — Analyst/Corporate Issuer Guidelines — https://rpc.cfainstitute.org/sites/default/files/-/media/documents/code/other-codes-standards/analyst-issuer-guidelines.pdf
- WallStreetPrep — Equity Research Report format — https://www.wallstreetprep.com/knowledge/sample-equity-research-report/
- Marvin Labs — earnings-season solution (5.7hr→45min, -40% workload) — https://www.marvin-labs.com/solutions/earnings-season/
- Analyst ratings/price target methodology — https://pro.stockalarm.io/blog/analyst-ratings-guide
- Target price accuracy of sell-side analysts (94.5% multiples, DCF 4%) — https://www.tandfonline.com/doi/full/10.1080/23322039.2024.2423261
- ESMA — MiFID II Q&A investor protection (Article 52, analyst separation) — https://www.esma.europa.eu/sites/default/files/library/esma35-43-349_mifid_ii_qas_on_investor_protection_topics.pdf

**Risk / Model Validation:**
- SR 11-7 Model Risk Management — https://www.magicmirrorsecurity.com/blog/sr-11-7-model-risk-management-guidance-explained
- SR 11-7 governance & validation — https://ryanoconnellfinance.com/model-risk-management/
- SR 11-7 checklist/tiering — https://www.popprobe.com/checklist-library/financial-services-banking/model-risk/model-risk-management-validation-checklist
- Model risk governance — https://www.risk.net/journal-of-risk-model-validation/5379046/governance-and-organizational-requirements-for-effective-model-risk-management
- Backtesting/Benchmarking/Sensitivity — https://fastercapital.com/topics/backtesting,-benchmarking,-and-sensitivity-analysis.html/1
- PD Backtesting/Benchmarking framework — https://www.researchgate.net/publication/46429464_Quantitative_Validation_An_Overview_and_Framework_for_PD_Backtesting_and_Benchmarking
- Credit risk model validation (PD/LGD/EAD) — https://roopya.money/credit-risk-model-validation/
- Thailand BOT AI Risk Management Guidelines — https://www.tilleke.com/insights/thailand-issues-ai-risk-management-guidelines-for-financial-service-providers/25/
- Thailand PDPA overview — https://securiti.ai/thailand-personal-data-protection-act-pdpa/

**Agentic architecture (L2 Orchestration):**
- Anthropic — Building Effective AI Agents (6 patterns) — https://www.anthropic.com/research/building-effective-agents
- TradingAgents playbook (specialist+debate+risk oversight) — https://www.ruh.ai/blogs/tradingagents-playbook-multi-agent-ai-financial-services
- Agent-as-a-Judge evaluation (FinCon) — https://arxiv.org/pdf/2508.02994
- Multi-Agent Orchestration for VC Due Diligence — https://arxiv.org/pdf/2605.13110
- Agentic workflows (task graph, input/output schema) — https://mastra.ai/articles/agentic-workflows
