---
# Metadata
title: "Rust — Version History & Evolution"
description: "Comprehensive version history and evolution of Rust from early development to modern Rust."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial version history"
tags: [rust, version-history, evolution, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "10 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---
# Rust - ประวัติเวอร์ชันและวิวัฒนาการ
## ไทม์ไลน์
| เวอร์ชั่น | วันที่วางจำหน่าย | ธีมหลัก |
|---------|-------------|-----------|
| 0.1 | ม.ค. 2555 | คอมไพเลอร์ตัวแรก (rustc) การทำงานพร้อมกันตามงาน |
| 0.5 | 2555 | ระบบประเภทตามลักษณะเริ่มเป็นรูปเป็นร่าง |
| 0.6 | 2555 | การลบกล่องที่ได้รับการจัดการ`@`|
| 0.7 | 2013 | `@`ถูกลบ`~`สำหรับกล่องที่เป็นเจ้าของ |
| 0.8 | 2013 | คำอธิบายประกอบตลอดอายุการใช้งาน`&mut`|
| 0.9 | ม.ค. 2557 | การล้างข้อมูลก่อน 1.0 ขั้นสุดท้าย |
| 0.10 | ก.พ. 2557 | รุ่นก่อน 1.0 ล่าสุด |
| 0.11 | เม.ย. 2557 | `Box<T>`แทนที่`~T`|
| 0.12 | พฤษภาคม 2557 | `io`โมดูลเขียนใหม่เริ่มต้น |
| 1.0 | 15 พฤษภาคม 2558 | **รุ่นเสถียร** — "Rust 1.0" |
| 1.10 | ส.ค. 2559 |  การแพร่กระจายข้อผิดพลาด`?`(เช่น`try!`→`?`) |
| 1.15 | ก.พ. 2560 | สนิมครั้งแรกบนความเสถียรด้วยการเตรียม`impl Trait`|
| 1.18 | มิ.ย. 2560 | `pub(crate)`การรวบรวมแบบเพิ่มหน่วย |
| 1.20 | ต.ค. 2560 | ค่าคงที่ที่เกี่ยวข้อง |
| 1.26 | พฤษภาคม 2561 | `impl Trait`ในตำแหน่งอาร์กิวเมนต์/ส่งคืน |
| 1.28 | ก.ย. 2561 | ตัวจัดสรรทั่วโลก |
| 1.31 | ธ.ค. 2561 | **Rust 2018 Edition** — โมดูล`dyn Trait`|
| 1.34 | เม.ย. 2562 | รีจิสทรีทางเลือก |
| 1.39 | พ.ย. 2562 | `async/await`บน |
| 1.44 | ก.ค. 2563 | การปรับปรุงการวินิจฉัย |
| 1.51 | เม.ย. 2564 | `const`ยาสามัญ (MVP) |
| 1.56 | ต.ค. 2564 | **Rust 2021 Edition** — การปิดตัวลง, IntoIterator |
| 1.59 | ก.พ. 2565 | การประกอบแบบอินไลน์ |
| 1.62 | มิ.ย. 2565 | `#[default]`สำหรับแจงนับ |
| 1.65 | ธ.ค. 2565 | `let else`|
| 1.68 | มี.ค. 2566 | `#[ffi_pure]`การเพิ่มประสิทธิภาพตามโปรไฟล์ |
| 1.70 | มิ.ย. 2566 | แยกการพึ่งพา`crates.io`|
| 1.74 | พ.ย. 2566 | โหมดการขนส่งสินค้าแบบออฟไลน์ |
| 1.76 | ก.พ. 2567 | **รุ่นสนิมปี 2024** — บล็อก `gen`,`unsafe extern`|
| 1.79 | มิ.ย. 2567 | `LazyCell`,`LazyLock`|
| 1.82 | ต.ค. 2567 |  ต้องใช้`unsafe`ในบล็อก`extern`|
| 1.85 | ก.พ. 2568 | ฉบับ Rust 2024 มีความเสถียร |
## เหตุการณ์สำคัญที่สำคัญ
### พรี-1.0 (2010–2015)
- **2010**: โปรเจ็กต์ข้างของ Graydon Hoare ที่ Mozilla ได้รับแรงผลักดัน
- **2012**: ผู้รวบรวมสาธารณะคนแรก; ระบบประเภทได้รับการออกแบบใหม่ครั้งใหญ่
- **2013**: โมเดลการเป็นเจ้าของตกผลึก  นำกล่อง`@`ออกแล้ว
- **2014**: กระบวนการ Rust RFC เป็นทางการ ชุมชนเติบโตขึ้น
- **2015**: **1.0** — รับประกันความเสถียร; "นามธรรมไร้ต้นทุน"
### ปีแห่งการเติบโต (2558–2562)
- **2015**: Cargo กลายเป็นผู้จัดการบรรจุภัณฑ์มาตรฐาน
- **2018**: **Rust 2018 Edition** — ยกเครื่องระบบโมดูล`dyn Trait`,`impl Trait`
- **2019**:`async/await`เข้าสู่ความเสถียร — เริ่มต้นระบบนิเวศแบบอะซิงโครนัส
### ครบกำหนด (2020–ปัจจุบัน)
- **2021**: **Rust 2021 Edition** — แยกแยะฟิลด์ในการปิด`IntoIterator`สำหรับอาร์เรย์
- **2024**: **Rust 2024 Edition** — บล็อก `gen`, ข้อกำหนด `unsafe extern`
- **2025**: Rust ในเคอร์เนล Linux, Android, Windows, โครงสร้างพื้นฐาน AWS
## ระบบฉบับ
```
Rust 2015:  The baseline (1.0)
Rust 2018:  Module system, async/await prep, dyn Trait
Rust 2021:  Closure changes, IntoIterator, panic macros
Rust 2024:  gen blocks, unsafe extern, tail expressions

Key principle: Editions are opt-in, never break existing code.
Old editions always compile. New editions add features.
```

## วิวัฒนาการความเป็นเจ้าของ
```
2010: GC-based, like Erlang
2011: Region-based lifetimes proposed
2012: Ownership model emerges (unique, shared, owned)
2013: Simplified to &T / &mut T / Box<T>
2014: Box<T> replaces ~T; Rc<T> for shared ownership
2015: 1.0 — ownership model finalized
2018: Non-Lexical Lifetimes (NLL) in Rust 2018
2021: IntoIterator for arrays (was blocked by edition concerns)
2024: Further NLL improvements
```

## วิวัฒนาการแบบอะซิงก์
```
2018: futures 0.1 — early async with manual polling
2019: async/await syntax (Rust 1.39)
2019: tokio 0.2 — async runtime
2020: async-std — std-like async API
2021: tokio 1.0 — stable async runtime
2023: async fn in traits (Rust 1.75)
2024: async closures, improved Send bounds
```

## การเติบโตของระบบนิเวศ
```
2015: crates.io launches (~2,000 crates)
2018: Rust most loved language (Stack Overflow survey)
2019: 30,000 crates on crates.io
2021: Most admired language (6th consecutive year)
2023: 130,000+ crates
2025: Used in Linux kernel, Android, Windows, Chromium, AWS, Cloudflare, Discord, Dropbox
```

## RFC ที่สำคัญ
| อาร์เอฟซี | ปี | คุณสมบัติ |
|------|-|--------|
| 25 | 2013 | การจับคู่รูปแบบ |
| 153 | 2014 | `Result`ประเภท |
| 217 | 2014 |  ตัวดำเนินการ`?`(ลอง) |
| 460 | 2559 | `?`แทนที่`try!`|
| 1210 | 2558 | `impl Trait`|
| 1414 | 2559 | รุ่นสนิม 2018 |
| 2394 | 2018 | `async/await`|
| 2515 | 2018 | `const`ยาสามัญ |
| 3013 | 2020 | กำลังตรวจสอบการคอมไพล์แบบมีเงื่อนไข |
| 3517 | 2023 | `gen`บล็อก |