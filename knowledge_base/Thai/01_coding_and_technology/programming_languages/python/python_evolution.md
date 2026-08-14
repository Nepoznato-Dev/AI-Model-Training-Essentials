---
# Metadata
title: "Python — Version History & Evolution"
description: "Comprehensive version history and evolution of Python from 1.x to modern Python."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial version history"
tags: [python, version-history, evolution, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "12 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---
# Python — ประวัติเวอร์ชันและวิวัฒนาการ
## ไทม์ไลน์
| เวอร์ชั่น | วันที่วางจำหน่าย | ธีมหลัก |
|---------|-------------|-----------|
| 1.0 | ม.ค. 2537 | การเปิดตัวครั้งแรก |
| 1.5 | ธ.ค. 2540 | คลาส ข้อยกเว้น โมดูล |
| 2.0 | ต.ค. 2543 | รายการความเข้าใจ การรวบรวมขยะ |
| 2.2 | ธ.ค. 2544 | ประเภทรวม (ประเภท/คลาส) เครื่องกำเนิดไฟฟ้า |
| 2.5 | ก.ย. 2549 |  คำสั่ง `with`,`yield`เป็นนิพจน์ |
| 2.6 | ต.ค. 2551 | `bytes`,`future`นำเข้า เปลี่ยนเป็น 3 |
| 2.7 | ก.ค. 2553 | ความเข้าใจตามคำบอก/ชุด`argparse`|
| 3.0 | ธ.ค. 2551 | **การทำลายล้าง**:`print()`,`str`/`bytes`, ตัววนซ้ำ |
| 3.3 | ก.ย. 2555 | `yield from`แพ็คเกจเนมสเปซ |
| 3.4 | มี.ค. 2557 | `asyncio`,`pathlib`,`enum`|
| 3.5 | ก.ย. 2558 | `async/await`, พิมพ์คำแนะนำ (PEP 484),`**`กำลังแกะกล่อง |
| 3.6 | ธ.ค. 2559 | f-strings,`async`compreh, สั่งคำสั่ง |
| 3.7 | มิ.ย. 2561 | `dataclasses`,`contextvars`, สงวนไว้`async`|
| 3.8 | ต.ค. 2562 | ตัวดำเนินการ Walrus`:=`พารามิเตอร์เฉพาะตำแหน่ง |
| 3.9 | ต.ค. 2563 | Dict union`|`ประเภททั่วไป`list[int]`|
| 3.10 | ต.ค. 2564 | `match/case`การจับคู่รูปแบบโครงสร้าง |
| 3.11 | ต.ค. 2565 | กลุ่มข้อยกเว้น ประเภท `Self`, CPython ที่เร็วกว่า |
| 3.12 | ต.ค. 2566 | การเตรียม GIL ต่อล่าม พิมพ์ไวยากรณ์พารามิเตอร์ |
| 3.13 | ต.ค. 2567 | โหมดฟรีเธรด (ทดลอง) ปรับปรุง REPL |
| 3.14 | ต.ค. 2568 | No-GIL การประเมินคำอธิบายประกอบที่เสถียรและเลื่อนออกไป
## เหตุการณ์สำคัญที่สำคัญ
### ยุค Python 2.x (2000–2020)
- **2.0**: รายการความเข้าใจที่ได้รับแรงบันดาลใจจาก Haskell วงจร GC
- **2.2**: คลาสพื้นฐาน`object` คีย์เวิร์ด`yield`(ตัวสร้าง)
- **2.5**: คำสั่ง `with`; `yield`กลายเป็นการแสดงออก
- **2.7**: การเปิดตัว 2.x สุดท้าย; ความเข้าใจตามคำบอก; `argparse`
- **สิ้นสุดอายุการใช้งาน**: 1 มกราคม 2020
### Python 3.x Revolution (2551–ปัจจุบัน)
- **3.0**: คลีนเบรก —`print`เป็นฟังก์ชัน,`str`เทียบกับ`bytes`ตัววนซ้ำทั้งหมดส่งคืนการดู
- **3.5**: ไวยากรณ์`async`/ `await`; พิมพ์คำแนะนำด้วยโมดูล `typing`
- **3.6**: f-strings (ฟีเจอร์ที่ได้รับการร้องขอมากที่สุด); `asyncio`เสถียร
- **3.8**: ตัวดำเนินการ Walrus สำหรับการมอบหมายแบบอินไลน์
- **3.10**: การจับคู่รูปแบบโครงสร้าง (`match`/`case`)
- **3.11**: เร็วขึ้น 10-60%; กลุ่มข้อยกเว้นด้วย`except*`
- **3.13**: โหมดทดลองฟรีเธรด (ไม่มี GIL)
## วิวัฒนาการปรัชญาการออกแบบ
```
1994: "There should be one — and preferably only one — obvious way to do it"
2004: "Batteries included" (extensive stdlib)
2011: "Beautiful is better than ugly" (Zen of Python, PEP 20)
2015: Gradual typing accepted (Guido's compromise)
2018: "Black" formatter — consistency over preference
2023: Performance becomes priority (faster CPython, Shannon plan)
```

## PEP หลักที่มีรูปร่างเป็น Python
| เป๊ป | ปี | คุณสมบัติ |
|------|-|--------|
| 20 | 2547 | เซนแห่งหลาม |
| 257 | 2544 | แบบแผน Docstring |
| 279 | 2545 | `enumerate()`|
| 289 | 2545 | นิพจน์ตัวสร้าง |
| 342 | 2548 | `yield`เป็นนิพจน์`send()`|
| 380 | 2552 | `yield from`|
| 484 | 2014 | พิมพ์คำแนะนำ |
| 492 | 2014 | `async`/`await`|
| 498 | 2558 | เอฟสตริง |
| 572 | 2018 | ตัวดำเนินการวอลรัส`:=`|
| 622 | 2020 | การจับคู่รูปแบบโครงสร้าง |
| 654 | 2021 | กลุ่มข้อยกเว้น |
| 684 | 2022 | ต่อล่าม GIL |
| 703 | 2023 | การทำให้ GIL เป็นตัวเลือก |
## วิวัฒนาการด้านประสิทธิภาพ
```
Python 3.10:  baseline
Python 3.11:  ~1.25x faster (Faster CPython project)
Python 3.12:  ~1.3x faster (specializing adaptive interpreter)
Python 3.13:  ~1.4x faster (JIT compiler experiment)
Target 3.14:  5x faster than 3.10 (Shannon plan goal)
```

## การเติบโตของชุมชนและระบบนิเวศ
```
2004: PyPI launches (7,000+ packages by 2010)
2008: First PyCon (300 attendees)
2012: pip replaces easy_install
2018: Python overtakes Java in popularity (Stack Overflow)
2020: Python 2 end-of-life; 3.x migration completes
2023: 500,000+ packages on PyPI
2025: #1 most used language (multiple surveys)
```
