<!--
---
# Metadata
title: "C — Version History & Evolution"
description: "Comprehensive version history and evolution of C from K&R to C23."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial version history"
tags: [c, version-history, evolution, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "10 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

-->
# C — ประวัติเวอร์ชันและวิวัฒนาการ
## ไทม์ไลน์
| เวอร์ชั่น | ปี | ธีมหลัก |
|---------|-|-----------|
| เคแอนด์อาร์ซี | พ.ศ. 2515–2521 | ต้นฉบับ C (Kernighan & Ritchie) |
| C89/C90 | 1989/90 | มาตรฐาน ANSI/ISO แรก |
| C95 | 1995 | การแก้ไข 1:`wchar.h`, digraphs |
| C99 | 1999 |  ความคิดเห็น `//`,`inline`,`bool`, VLAs, ตัวเริ่มต้นที่กำหนด |
| C11 | 2554 | อะตอมมิกส์ เธรด`_Static_assert`โครงสร้าง/สหภาพที่ไม่ระบุชื่อ |
| C17 | 2018 | แก้ไขข้อบกพร่อง (ไม่มีคุณสมบัติใหม่) |
| C23 | 2024 | `nullptr`,`typeof`,`constexpr`,`#embed`, แอ็ตทริบิวต์ |
## เหตุการณ์สำคัญที่สำคัญ
### เคแอนด์อาร์ ซี (1972–1989)
- **1972**: Dennis Ritchie สร้างภาษา C ที่ Bell Labs สำหรับ Unix
- **1978**: Kernighan & Ritchie เผยแพร่ "ภาษาการเขียนโปรแกรม C"
- คุณสมบัติหลัก:`struct`,`int`,`char`, พอยน์เตอร์, ฟังก์ชัน,`#include`
- ไม่มี`void`, ไม่มี`enum`, ไม่มี`unsigned`, ไม่มี `const`
### C89/C90 - มาตรฐาน (1989)
- มาตรฐาน ANSI แรก (ANSI X3.159-1989)
- เพิ่ม:`void`,`enum`,`const`,`volatile`, ฟังก์ชั่นต้นแบบ,`signed`
- "ยุคทอง" — พกพาสะดวก นำมาใช้กันอย่างแพร่หลาย
- ยังคงเป็นพื้นฐานสำหรับระบบฝังตัวจำนวนมาก
### C99 — โมเดิร์นซี (1999)
-`//`ความคิดเห็นบรรทัดเดียว
- ฟังก์ชัน `inline`
-`bool`ผ่าน`<stdbool.h>`
- อาร์เรย์ความยาวแปรผัน (VLA)
- ตัวเริ่มต้นที่กำหนด:`struct Point p = {.x = 1, .y = 2};`
-`for (int i = 0; ...)`— การประกาศแบบวนซ้ำ
-`<stdint.h>`:`int32_t`,`uint64_t`ฯลฯ
- คีย์เวิร์ด `restrict`
- มาโครแปรผัน
- ตัวอักษรผสม
### C11 — ความปลอดภัยและการทำงานพร้อมกัน (2011)
-`<stdatomic.h>`— การทำงานของอะตอมมิก
-`<threads.h>`— รองรับเธรด
-`_Static_assert`- การยืนยันเวลาคอมไพล์
- โครงสร้าง/สหภาพที่ไม่ระบุชื่อในโครงสร้างที่ซ้อนกัน
-`_Alignof`,`_Alignas`— การควบคุมการจัดตำแหน่ง
- ตัวเลือกทั่วไป:`_Generic(x, int: ..., default: ...)`
- รองรับยูนิโค้ด:`<uchar.h>`
- การสนับสนุน VLA เสริม (ทำเป็นทางเลือกเนื่องจากข้อกังวลที่ฝังอยู่)
### C23 — ยุคฟื้นฟูศิลปวิทยา (2024)
-`nullptr`- ค่าคงที่ของตัวชี้ null (แทนที่มาโคร `NULL`)
-`typeof`— การอนุมานประเภท
-`constexpr`— นิพจน์คงที่
-`#embed`— ฝังข้อมูลไบนารี ณ เวลารวบรวม
- ไวยากรณ์`[[attribute]]`(แอตทริบิวต์สไตล์ C23)
-`true`/`false`เป็นคำหลัก (ไม่ต้องการ`<stdbool.h>`อีกต่อไป)
- การอนุมานประเภท `auto`
-`static_assert`(ไม่มีขีดล่าง)
-`alignof`(ไม่มีขีดล่าง)
- ลบการส่งคืน`int`เริ่มต้นแล้ว
## กระบวนการมาตรฐาน
```
1983: ANSI X3J11 committee formed
1989: C89 ratified (ANSI)
1990: C90 ratified (ISO/IEC 9899:1990)
1999: C99 (ISO/IEC 9899:1999)
2011: C11 (ISO/IEC 9899:2011)
2018: C17 (ISO/IEC 9899:2018) — defect fixes only
2024: C23 (ISO/IEC 9899:2024)
```

## ปรัชญาความเข้ากันได้
```
C has always valued backward compatibility:
- C99 compilers accept most C89 code
- C11 compilers accept most C99 code
- C23 makes some breaking changes (removes K&R function definitions)
- Key principle: "Trust the programmer"
- Key principle: "No hidden costs"
- Key principle: "Portability through standardization"
```

## วิวัฒนาการของพรีโปรเซสเซอร์
```
K&R:    #include, #define, #ifdef, #if
C89:    #elif, function-like macros, stringification
C99:    Variadic macros (__VA_ARGS__), _Pragma
C11:    _Static_assert
C23:    #embed, [[attribute]], #if has_include
```

## ประเภทวิวัฒนาการของระบบ
```
K&R:    int, char, float, double, struct, pointer, function
C89:    void, enum, const, volatile, signed, unsigned
C99:    bool (via macro), complex, long long, intN_t types
C11:    _Atomic, _Alignas, _Generic, char16_t, char32_t
C23:    typeof, nullptr, auto, bool (keyword), constexpr
```

## ผลกระทบต่อระบบนิเวศ
```
1970s: C replaces assembly for OS development (Unix)
1980s: C becomes dominant systems language
1990s: C99 influences Java, C#, JavaScript
2000s: C89 still widely used in embedded
2010s: C11 adds modern concurrency
2020s: C23 modernizes while preserving simplicity
2025: C remains the foundation of all computing (Linux, Windows, macOS kernels)
```
