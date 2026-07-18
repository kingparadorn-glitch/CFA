# P2 Earnings Update Flow — 12 บริษัท ข้าม 3 ตลาด (US / Vietnam / Thai)

> ⚠️ **ไฟล์นี้ = qualitative flow/ingestion spec (บอกว่า "extract อะไร" ต่อบริษัท/ตลาด) — ไม่ใช่ test dataset.** ไม่มีค่าตัวเลขจริง → ทดสอบ flow ไม่ได้จากไฟล์นี้อย่างเดียว. **ค่าจริง + ground-truth สำหรับทดสอบ L0-L9 อยู่ที่ `07_implementation/data/`** (golden_dataset_schema.md + MSFT golden fixture + Thai template). ใช้ไฟล์นี้เป็น: (1) market-aware ingestion design (2) scalability story ในสไลด์ (3) รู้ว่าแต่ละบริษัท extract อะไร

> เอกสารประกอบโปรเจกต์ AI × Finance Hackathon (ทีม claude.md)
> P2 = Earnings Update Pipeline: จากงบออก → updated model + earnings note draft ภายใน ~45-90 นาที
> โครง 7 step เหมือนกันทุกบริษัท — สิ่งที่ต่างคือ data source, trigger, transcript availability และ model driver ของแต่ละตลาด

---

## ชั้นที่ 1 — P2 Universal Flow (ใช้ร่วมกันทั้ง 12 ตัว)

```
TRIGGER: งบออก
   ↓
STEP 1  Ingest      → ดึงงบ + presentation + transcript เข้าระบบ → structured JSON
STEP 2  Surprise    → เทียบ actual vs prior estimate (house/consensus) → beat/miss flag
STEP 3  Model       → AI extract ตัวเลข → ANALYST key เข้า model (AI = cross-check)
STEP 4  Commentary  → AI สกัด guidance, tone, red flags จาก transcript/MD&A
STEP 5  Draft Note  → AI สร้าง first draft ตาม house template + citation ทุกตัวเลข
STEP 6  Human Gate  → Analyst ตรวจ + ตัดสิน Rating/TP + sign-off (licensed IA)
STEP 7  Publish     → Compliance check + audit log + เผยแพร่
```

**หลักการที่ไม่เปลี่ยนทุกตลาด:** AI ทำ extraction / surprise / draft — มนุษย์ทำ judgment / rating / sign-off

**หมายเหตุ Step 3 (จาก practice จริง):** analyst อัปเดต model เองจาก source document โดยใช้ตัวเลขที่ AI extract เป็น reference/cross-check เท่านั้น — ไม่ให้ AI เขียนลง model โดยตรง เพราะถ้าตัวเลขผิด 1 จุด model พังโดย analyst ไม่รู้

---

## ชั้นที่ 2 — ความต่างของ Flow ตาม 3 ตลาด

| ขั้นตอน | 🇺🇸 US (AAPL, MSFT, AMZN, NVDA) | 🇻🇳 Vietnam (VIC, VNM, FPT, HPG) | 🇹🇭 Thai (PTT, CPALL, ADVANC, AOT) |
|---|---|---|---|
| **Trigger** | 8-K + press release หลังตลาดปิด → earnings call **วันเดียวกัน** | งบส่ง HOSE/HNX เป็นภาษาเวียดนาม มัก delay | SET filing → Oppday ตามมา 1-4 สัปดาห์ |
| **Step 1 Input** | 10-Q/10-K (structured XBRL), press release, call transcript | งบ VAS ภาษาเวียดนาม ต้องแปล + map เข้า schema | งบ TFRS, MD&A, Oppday deck (PDF) |
| **Transcript** | ✅ มีทุกบริษัท ภายในชั่วโมง (Seeking Alpha / Motley Fool) | ❌ แทบไม่มี — ใช้ press release + analyst meeting notes | ⚠️ Oppday recording → ต้อง ASR; PTT มี Analyst Meeting webcast + transcript |
| **Consensus** | ✅ ลึกมาก (Visible Alpha, FactSet, Yahoo ฟรีบางส่วน) | ⚠️ บางเบา — FiinGroup/Bloomberg เท่านั้น มัก fallback เป็น own-forecast | ✅ IAA Consensus (อ่าน manual จาก SETTRADE — ห้าม scrape ตามเงื่อนไขลิขสิทธิ์) |
| **มาตรฐานบัญชี** | US GAAP | **VAS** (ต่างจาก IFRS — ระวัง revaluation, provision, revenue recognition อสังหา) | TFRS (≈IFRS, ระวัง TFRS 16) |
| **สกุลเงิน** | USD | VND (หลักพันล้าน–ล้านล้าน dong) | THB |
| **AI-readiness** | ✅ สูงสุด — XBRL structured | ❌ ต่ำสุด — ภาษา + format | ⚠️ กลาง — PDF สแกน/พิมพ์ปน |
| **จุดที่ AI ประหยัดเวลาสุด** | Transcript analysis (call ยาว 60 นาที) | **แปลภาษา + restructure งบ** | Extract จาก PDF + อ่าน MD&A |

**Insight สำหรับ deck:** flow เดียวกัน แต่ *คอขวดคนละที่* — US ติดที่ปริมาณ transcript, VN ติดที่ภาษา/format, ไทยติดที่ PDF extraction → engine ต้องมี **market-aware ingestion layer**

---

## ชั้นที่ 3 — Spec รายบริษัท (12 ตัว)

### 🇺🇸 กลุ่ม US

#### 1. AAPL — Apple Inc.
| หัวข้อ | รายละเอียด |
|---|---|
| Trigger | งบ fiscal Q (FY จบ ก.ย.) + earnings call วันเดียวกัน |
| Step 1 extract | Revenue by product (iPhone / Mac / iPad / Wearables / **Services**), by geography (ระวัง Greater China), Gross margin แยก Products vs Services |
| Step 2 surprise metrics | iPhone revenue vs consensus, Services growth %, GM%, EPS |
| Step 4 จับใน call | Guidance ไตรมาสหน้า (Apple ให้เป็นช่วง), China commentary, capex AI |
| Model quirk | ไม่มี unit sales (เลิกเปิดเผยปี 2018) → model ขับด้วย revenue โดยตรง; buyback มหาศาลกด share count ลงทุกไตรมาส → EPS โตเร็วกว่า net income |

#### 2. MSFT — Microsoft Corporation
| หัวข้อ | รายละเอียด |
|---|---|
| Step 1 extract | 3 segment — Productivity, Intelligent Cloud (**Azure growth % คือตัวเลขเดียวที่ตลาดดู**), More Personal Computing |
| Step 2 | Azure YoY constant currency vs consensus คือ headline surprise; miss 1-2pp = หุ้นลงได้ |
| Step 4 | Capex guidance (AI datacenter), Copilot monetization commentary |
| Model quirk | FY จบ มิ.ย.; Azure ไม่เปิดเผยเป็น dollar แค่ % growth → model ต้อง back into |

#### 3. AMZN — Amazon.com, Inc.
| หัวข้อ | รายละเอียด |
|---|---|
| Step 1 extract | AWS revenue + **AWS operating margin**, North America/International retail, Advertising |
| Step 2 | AWS growth + AWS margin คือ 80% ของ story; retail margin เป็นรอง |
| Step 4 | Capex guidance, Q ถัดไป revenue/operating income range (Amazon ให้ guidance กว้าง) |
| Model quirk | Operating income สำคัญกว่า net income (มี Rivian mark-to-market ทำ noise) → AI ต้อง flag one-time ทุกไตรมาส |

#### 4. NVDA — NVIDIA Corporation
| หัวข้อ | รายละเอียด |
|---|---|
| Step 1 extract | Data Center revenue (คือเกือบทั้งบริษัท), Gaming, GM% |
| Step 2 | Data Center vs consensus + **guidance ไตรมาสหน้า vs consensus** — สำหรับ NVDA guidance สำคัญกว่า actual |
| Step 4 | Supply constraint commentary, China export restriction, next-gen chip ramp |
| Model quirk | FY จบ ม.ค.; ความคาดหวังสูงมาก — beat 5% อาจยังทำหุ้นลงถ้า guidance ไม่แรงพอ → Step 2 ต้องคำนวณ "beat vs whisper number" ไม่ใช่แค่ vs consensus |

---

### 🇻🇳 กลุ่ม Vietnam

#### 5. VIC — Vingroup JSC
| หัวข้อ | รายละเอียด |
|---|---|
| Step 1 extract | แยก segment: Vinhomes (อสังหา), VinFast (EV — ขาดทุนหนัก), Vincom Retail, Vinpearl |
| Step 2 | ถ้าไม่มี consensus → own-forecast baseline; ตัวชี้: presales อสังหา, VinFast deliveries, VinFast loss run-rate |
| Step 4 | จาก press release + ประกาศ HOSE (ไม่มี transcript) |
| Model quirk | Conglomerate ซับซ้อนสุดใน 12 ตัว — inter-company transaction เยอะ, VinFast listed แยกที่ US (VFS) ต้อง reconcile; VAS revenue recognition อสังหาต่างจาก IFRS → AI ต้อง flag ว่าเทียบ cross-border ตรงๆ ไม่ได้ |

#### 6. VNM — Vinamilk
| หัวข้อ | รายละเอียด |
|---|---|
| Step 1 extract | Domestic vs export revenue, GM% (ขับด้วยราคานมผงโลก), market share |
| Step 2 | GM% คือหัวใจ — ราคา whole milk powder ขึ้น = margin หด |
| Step 4 | Commentary เรื่อง demand ในประเทศ + ราคา input |
| Model quirk | โครงสร้างง่ายสุดในกลุ่ม VN — เหมาะเป็น "ตัวแรก" ถ้าจะ demo VN market; dividend สูงสม่ำเสมอ |

#### 7. FPT — FPT Corporation
| หัวข้อ | รายละเอียด |
|---|---|
| Step 1 extract | Global IT Services (ตัวโต — ญี่ปุ่น/US), Telecom, Education |
| Step 2 | IT Services revenue growth + new signed contracts vs คาด |
| Step 4 | Order book/backlog commentary, AI services push |
| Model quirk | รายงาน **monthly business update** (หายากมาก) → P2 สำหรับ FPT รันได้ถี่กว่าไตรมาส — จุดขายที่น่าสนใจสำหรับ demo |

#### 8. HPG — Hoa Phat Group
| หัวข้อ | รายละเอียด |
|---|---|
| Step 1 extract | ปริมาณขายเหล็ก (ตัน), ASP, GM%, construction steel vs HRC |
| Step 2 | Volume × spread (ราคาเหล็ก − ราคา iron ore/coking coal) คือทั้ง story |
| Step 4 | Commentary กำลังการผลิต Dung Quat 2, จีน dumping |
| Model quirk | Commodity cyclical — model ขับด้วย spread ไม่ใช่ revenue growth; AI ควรดึงราคาเหล็กโลกมาประกอบ (external data) |

---

### 🇹🇭 กลุ่มไทย

#### 9. PTT — PTT Public Company Limited
| หัวข้อ | รายละเอียด |
|---|---|
| Step 1 extract | แยก segment: E&P (PTTEP), Gas, Refining (**GRM**), Petrochemical, Oil retail (OR) |
| Step 2 | ตัวขับ: ราคาน้ำมัน, GRM (gross refining margin), petrochemical spread, stock gain/loss |
| Step 4 | **PTT มี Analyst Meeting + webcast + transcript จริง** (ระดับใกล้ US สุดในไทย) → input tier ดีสุด |
| Model quirk | SOTP-based (บริษัทลูก listed หลายตัว: PTTEP, GC, OR, GPSC) → model = รวม stake; stock gain/loss จาก inventory ทำ earnings volatile → AI ต้องแยก core vs stock effect ทุกไตรมาส |

#### 10. CPALL — CP ALL Public Company Limited
| หัวข้อ | รายละเอียด |
|---|---|
| Step 1 extract | SSSG, GM%, store count, avg daily sales/store, customers/store/day, basket size |
| Step 2 | SSSG คือ headline; GM% expansion + Makro/Lotus's contribution เป็นรอง |
| Step 4 | Guidance เปิดสาขาใหม่, SSSG target, Makro integration synergy |
| Model quirk | TFRS 16 lease หนักมาก (เช่าที่ 7-Eleven 14,000+ สาขา) → EBITDA เทียบ pre-2020 ไม่ได้; 4 segment + บริษัทย่อยหลายสิบ → ใช้เวลา review นานกว่า simple structure |

#### 11. ADVANC — Advanced Info Service (AIS)
| หัวข้อ | รายละเอียด |
|---|---|
| Step 1 extract | Mobile ARPU, subscriber net adds, Fixed broadband subs, Enterprise/5G revenue, EBITDA margin |
| Step 2 | ARPU trend + service revenue growth vs คาด; ตลาด mature → margin สำคัญกว่า growth |
| Step 4 | Commentary การแข่งขันกับ TRUE (duopoly หลัง merger), 3BB integration |
| Model quirk | เสถียรที่สุดในกลุ่มไทย — คาดการณ์ง่าย, dividend yield play; ระวัง one-time จาก 3BB acquisition accounting |

#### 12. AOT — Airports of Thailand
| หัวข้อ | รายละเอียด |
|---|---|
| Step 1 extract | **จำนวนผู้โดยสาร** (Int'l vs Domestic แยก 6 สนามบิน), aero vs non-aero revenue, concession revenue |
| Step 2 | Passenger traffic vs คาด คือทั้ง story — โดยเฉพาะนักท่องเที่ยวจีน |
| Step 4 | Commentary King Power concession terms, capacity expansion (Suvarnabhumi) |
| Model quirk | FY จบ ก.ย. (ต่างจากบริษัทไทยส่วนใหญ่); รายงาน traffic **รายเดือน** → P2 รันได้ถี่กว่าไตรมาสเหมือน FPT; concession accounting ซับซ้อน |

---

## ตารางสรุป — Headline Surprise Metric ของแต่ละตัว

| บริษัท | ตัวเลขเดียวที่ตลาดดูก่อน | AI-readiness ของ data |
|---|---|---|
| AAPL | iPhone rev + Services growth | ⭐⭐⭐⭐⭐ |
| MSFT | Azure growth % | ⭐⭐⭐⭐⭐ |
| AMZN | AWS margin | ⭐⭐⭐⭐⭐ |
| NVDA | Data Center + **guidance** | ⭐⭐⭐⭐⭐ |
| VIC | VinFast loss + presales | ⭐⭐ |
| VNM | Gross margin | ⭐⭐⭐ |
| FPT | IT Services growth (monthly!) | ⭐⭐⭐ |
| HPG | Steel spread | ⭐⭐⭐ |
| PTT | GRM + stock gain/loss | ⭐⭐⭐⭐ |
| CPALL | SSSG | ⭐⭐⭐⭐ |
| ADVANC | ARPU + EBITDA margin | ⭐⭐⭐⭐ |
| AOT | Passenger traffic (monthly!) | ⭐⭐⭐⭐ |

---

## จุดที่เอาไปใช้ใน Hackathon ได้ทันที

1. **Flow เดียว 7 step ใช้ได้ 3 ตลาด — แต่ ingestion layer ต้อง market-aware** (ภาษา, มาตรฐานบัญชี, transcript availability) = พิสูจน์ scalability ของ architecture
2. **Coverage 12 ตัวข้ามตลาด = impact story ชัด**: analyst 1 คน cover 12 ตัวข้าม 3 ตลาดด้วยเวลาเท่าเดิม = capacity expansion ที่วัดได้
3. **FPT + AOT รายงาน monthly** → P2 ไม่ใช่แค่ quarterly tool แต่เป็น continuous monitoring ได้
4. **VN คือ proof of hardest case**: ถ้า engine ผ่าน VAS + ภาษาเวียดนามได้ ไทยกับ US คือของง่าย
5. **Compliance ต่างตลาด**: ไทย = IA license (ก.ล.ต. สข. 25/2547), US = Reg AC, ทุกตลาดต้องมี human sign-off → human-in-the-loop เป็น universal requirement ไม่ใช่ข้อจำกัดเฉพาะไทย

---

## ภาคผนวก — แหล่งข้อมูลต่อตลาด

### 🇺🇸 US
| แหล่ง | ใช้ทำอะไร | Cost |
|---|---|---|
| SEC EDGAR | 10-K, 10-Q, 8-K (XBRL structured) | ฟรี |
| Seeking Alpha / Motley Fool | Earnings call transcript | ฟรีบางส่วน |
| Yahoo Finance | Consensus estimate ย่อ | ฟรี |
| Visible Alpha / FactSet | Line-by-line consensus | มีค่าใช้จ่าย |

### 🇻🇳 Vietnam
| แหล่ง | ใช้ทำอะไร | Cost |
|---|---|---|
| HOSE / HNX | Filing, งบการเงิน (ภาษาเวียดนาม) | ฟรี |
| Vietstock / CafeF | ข้อมูลหุ้น + ข่าว | ฟรี |
| VCSC / SSI research | Broker research (EN บางส่วน) | ฟรีบางส่วน |
| FiinGroup | Consensus + data platform | มีค่าใช้จ่าย |

### 🇹🇭 Thai
| แหล่ง | ใช้ทำอะไร | Cost |
|---|---|---|
| SET.or.th | งบ 56-1, MD&A, Oppday deck | ฟรี |
| SETTRADE.com | IAA Consensus (อ่าน manual — ห้าม scrape) | ฟรี |
| DBD DataWarehouse+ | งบบริษัท non-listed | ฟรี (summary) |
| Broker research (KS, ASP, CGS ฯลฯ) | House estimate + full model | ต้องมีบัญชี |

---

*เอกสารนี้เป็นส่วนหนึ่งของการเตรียม AI × Finance Hackathon (CFA Society Thailand) — ทีม claude.md*
*หมายเหตุ: spec รายบริษัทอิงโครงสร้างธุรกิจ ณ ต้นปี 2026 — ตรวจสอบ segment structure ล่าสุดก่อนใช้จริงใน demo*
