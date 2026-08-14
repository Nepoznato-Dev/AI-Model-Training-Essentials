---
# Metadata
title: "Ruby — Version History & Evolution"
description: "Comprehensive version history and evolution of Ruby from 1.0 to modern Ruby."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial version history"
tags: [ruby, version-history, evolution, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "10 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

# Ruby — ประวัติเวอร์ชันและวิวัฒนาการ
## ไทม์ไลน์
| เวอร์ชั่น | ปี | ธีมหลัก |
|---------|-|-----------|
| 0.95 | 1995 | การเปิดตัวครั้งแรก (Yukihiro "Matz" Matsumoto) |
| 1.0 | 1996 | การเปิดตัวที่เสถียรครั้งแรก |
| 1.2 | 1998 | เอกสารภาษาอังกฤษฉบับแรก |
| 1.4 | 1999 | `BEGIN`/`END`,`String#unpack`|
| 1.6 | 2000 | การปรับปรุงการเก็บขยะ |
| 1.8 | 2546 | $KCODE เครื่องยนต์ oniguruma regex |
| 1.9 | 2550 | **หลัก**: M17N (หลายภาษา), ไวยากรณ์แฮชใหม่, ไฟเบอร์ |
| 2.0 | 2013 | อาร์กิวเมนต์คำหลัก`Enumerator::Lazy`,`Module#prepend`|
| 2.1 | 2013 | การเรียกเมธอดอย่างละเอียด`frozen_string_literal`|
| 2.2 | 2014 | สัญลักษณ์ GC, GC แบบเพิ่มหน่วย |
| 2.3 | 2558 | Pragma ตัวอักษรสตริงที่แช่แข็ง,`&.`การนำทางที่ปลอดภัย |
| 2.4 | 2559 | `Integer`แบบรวม`String`การแมปกรณี Unicode |
| 2.5 | 2017 | `yield_self`, บล็อกใน`rescue`/`ensure`|
| 2.6 | 2018 | **คอมไพเลอร์ JIT (MJIT)** ช่วงที่ไม่มีที่สิ้นสุด`1..`|
| 2.7 | 2019 | การจับคู่รูปแบบ (ทดลอง) พารามิเตอร์บล็อกที่มีหมายเลข |
| 3.0 | 2020 | **หลัก**: Ractor (การทำงานพร้อมกัน), Fiber Scheduler, ประเภท RBS |
| 3.1 | 2021 | `Anonymous`การส่งต่อบล็อก,`Hash#compact`|
| 3.2 | 2022 |  คลาส `Data`, การปรับปรุง `File.realpath`, การผลิต YJIT |
| 3.3 | 2023 | **YJIT** การปรับปรุงที่สำคัญ พารามิเตอร์บล็อก`it`|
| 3.4 | 2024 | ตัวแยกวิเคราะห์ปริซึมเริ่มต้น`it`เป็นพารามิเตอร์บล็อกเริ่มต้น |
## เหตุการณ์สำคัญที่สำคัญ
### รูบี้ตอนต้น (1995–2003)
- **1995**: Matz สร้าง Ruby — ผสมผสาน Perl, Smalltalk, Lisp
- **1.0 (1996)**: เปิดตัวเสถียรครั้งแรก
- **1.8 (2003)**: Ruby "คลาสสิก" — รวดเร็ว เสถียร และได้รับการยอมรับอย่างกว้างขวาง
### ยุคทางรถไฟ (2547–2556)
- **2004**: เปิดตัว Ruby on Rails — การปฏิวัติการพัฒนาเว็บไซต์
- **1.9 (2007)**: M17N (สตริงหลายภาษา), ไวยากรณ์แฮชใหม่`{key: value}`, ไฟเบอร์
- **2.0 (2013)**: อาร์กิวเมนต์ของคำหลัก, ตัวแจงนับแบบขี้เกียจ, `Module#prepend`
### โมเดิร์นรูบี้ (2558–ปัจจุบัน)
- **2.6 (2018)**: คอมไพเลอร์ JIT (MJIT) — การพุชประสิทธิภาพครั้งแรก
- **2.7 (2019)**: การจับคู่รูปแบบ (ทดลอง) พารามิเตอร์บล็อกที่มีหมายเลข`_1`
- **3.0 (2020)**: **Ractor** (การทำงานพร้อมกันของโมเดลนักแสดง), **Fiber Scheduler** (async I/O), **RBS** (ลายเซ็นประเภท)
- **3.2 (2022)**: คลาส`Data`(ออบเจ็กต์ค่าที่ไม่เปลี่ยนรูป) พร้อมการผลิต YJIT
- **3.3 (2023)**: การเร่งความเร็วหลักของ YJIT (เร็วขึ้นสูงสุด 3 เท่า) พารามิเตอร์บล็อก `it`
- **3.4 (2024)**: Prism parser กลายเป็นค่าเริ่มต้น
## วิวัฒนาการด้านประสิทธิภาพ
```
Ruby 1.8:  Baseline (interpreted)
Ruby 1.9:  ~1.5x faster (YARV bytecode)
Ruby 2.0:  ~1x (focus on features)
Ruby 2.6:  MJIT (experimental JIT)
Ruby 3.0:  Fiber Scheduler (async I/O)
Ruby 3.2:  YJIT (production JIT)
Ruby 3.3:  YJIT 3x faster (Rails benchmarks)
Ruby 3.4:  Prism parser (faster parsing)
Target:    3x faster than Ruby 2.5 (Ruby 3x3 goal)
```

## วิวัฒนาการพร้อมกัน
```
1.8:  Green threads (GIL)
1.9:  Native threads (still GIL)
2.0:  Fiber (cooperative)
2.6:  Fiber Scheduler proposal
3.0:  Ractor (Actor model, no GIL sharing)
3.0:  Fiber Scheduler (async I/O without threads)
3.3:  Improved Fiber Scheduler
```

## วิวัฒนาการการจับคู่รูปแบบ
```
2.7:  Experimental — case/in
3.0:  Improved — pin operator, find pattern
3.1:  One-line pattern matching
3.2:  Shortcut syntax, infinite patterns
3.4:  Pattern matching stabilized
```

## หลักการออกแบบที่สำคัญ
```
1. "MINASWAN" — Matz is nice and so we are nice
2. "Programmer happiness" — surprising is bad
3. "Everything is an object" — even numbers, nil, true
4. "Blocks are fundamental" — closures as first-class
5. "Duck typing" — behavior over type
6. "Convention over configuration" — Rails philosophy
```

## การเติบโตของระบบนิเวศ
```
2004: Rails launches — Ruby enters mainstream
2005: RubyGems package manager
2006: Ruby wins "Language of the Year" (TIOBE)
2008: Bundler (dependency management)
2010: Ruby 1.9 adoption accelerates
2013: Ruby 2.0 — enterprise adoption
2020: Ruby 3.0 — concurrency revolution
2023: YJIT makes Ruby fast again
2025: Ruby remains top 10; Rails powers GitHub, Shopify, Basecamp, Stripe
```
