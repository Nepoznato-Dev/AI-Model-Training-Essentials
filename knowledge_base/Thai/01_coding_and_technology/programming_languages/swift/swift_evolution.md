---
# Metadata
title: "Swift — Version History & Evolution"
description: "Comprehensive version history and evolution of Swift from 1.0 to modern Swift."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial version history"
tags: [swift, version-history, evolution, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "10 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---
# Swift - ประวัติเวอร์ชันและวิวัฒนาการ
## ไทม์ไลน์
| เวอร์ชั่น | ปี | ธีมหลัก |
|---------|-|-----------|
| 1.0 | 2014 | การเปิดตัวครั้งแรก (Chris Lattner, Apple) |
| 1.1 | 2014 | ตัวเริ่มต้นที่ล้มเหลว`@autoclosure`|
| 1.2 | 2558 | `as?`/`as!`, ประเภท `Set`, การเปรียบเทียบทูเพิล |
| 2.0 | 2558 | ส่วนขยายโปรโตคอล`defer`,`guard`,`errortype`|
| 2.1 | 2558 | `try?`การแก้ไขสตริงในตัวอักษร |
| 2.2 | 2559 | `#selector`,`defer`, tuple ส่งกลับ |
| 3.0 | 2559 | **สำคัญ**: การออกแบบ API ใหม่ — รูปแบบการตั้งชื่อ`@discardableResult`|
| 4.0 | 2017 | `Codable`,`String`เขียนใหม่ ตัวอักษรหลายบรรทัด |
| 5.0 | 2019 | **หลัก**: การเตรียม `async/await`, ความเสถียรของ ABI, ประเภท`Result`|
| 5.1 | 2019 | `some`(ชนิดทึบแสง), ตัวห่อคุณสมบัติ,`@resultBuilder`|
| 5.2 | 2020 | การเรียกตามฟังก์ชัน`KeyPath`เป็นฟังก์ชัน |
| 5.3 | 2020 | `@MainActor`, การปิดต่อท้ายหลายรายการ, การปรับปรุง`enum`|
| 5.4 | 2021 | พารามิเตอร์ตัวแปรหลายตัว การปรับปรุง `@resultBuilder`
| 5.5 | 2021 | **`async/await`** นักแสดง`Sendable`|
| 5.6 | 2022 | `any`คีย์เวิร์ด,`Clock`,`Duration`|
| 5.7 | 2022 | `if let`ชวเลข,`Regex`ตัวอักษร, โปรโตคอล`Clock`|
| 5.8 | 2023 | การปรับใช้ฟังก์ชันด้านหลัง การปรับปรุง`Clock`|
| 5.9 | 2023 | **มาโคร**, แพ็กพารามิเตอร์,`consume`/`discard`|
| 5.10 | 2024 | การตรวจสอบพร้อมกันอย่างสมบูรณ์ ความปลอดภัยของข้อมูลการแข่งขันที่เข้มงวด |
| 6.0 | 2024 | **หลัก**: การทำงานพร้อมกันอย่างเข้มงวดโดยค่าเริ่มต้น พิมพ์การพ่น |
| 6.1 | 2025 | (คาดว่า) การปรับปรุงการทำงานพร้อมกันเพิ่มเติม |
## เหตุการณ์สำคัญที่สำคัญ
### Swift 1.x — เกิด (2014–2015)
- **2014**: ประกาศที่ WWDC; แทนที่ Objective-C สำหรับการพัฒนาของ Apple
- **1.0**: ตัวเลือก, ข้อมูลทั่วไป, การปิด, การอนุมานประเภท, โปรโตคอล
- **1.2**: รูปแบบ`as?`/ `as!`, ประเภท `Set`
### Swift 2.x - การจัดการข้อผิดพลาด (2015–2016)
- **2.0**: ส่วนขยายโปรโตคอล (การเขียนโปรแกรมเชิงโปรโตคอล),`guard`,`defer`,`do/try/catch`
- **2.1**:`try?`สำหรับการจัดการข้อผิดพลาดเพิ่มเติม
### Swift 3.x - การเปลี่ยนชื่อ API ที่ยอดเยี่ยม (2016)
- **3.0**: การออกแบบ API ครั้งใหญ่ — "การเปลี่ยนชื่อแบบครบวงจรที่ยิ่งใหญ่"
- แบบแผนการตั้งชื่อ:`stringByAppendingString`→`appending`
- ลบลูป`for`สไตล์ C, ตัวดำเนินการ`++`/`--`ออก
- ป้ายกำกับพารามิเตอร์แรกตามค่าเริ่มต้น
### Swift 4.x — เขียนโค้ดได้ (2017)
- **4.0**: โปรโตคอล`Codable`(การเข้ารหัส/ถอดรหัส JSON),`String`เขียนใหม่, ตัวอักษรสตริงหลายบรรทัด
### Swift 5.x — ความเสถียร (2019–2024)
- **5.0**: ความเสถียรของ ABI (แอปมีขนาดเล็กลง), ประเภท `Result`, สตริงดิบ
- **5.1**: ประเภททึบแสง (`some View`), Wrappers คุณสมบัติ (`@State`,`@Binding`)
- **5.5**: **`async/await`** นักแสดง โปรโตคอล `Sendable`
- **5.9**: มาโคร (การสร้างโค้ดเวลาคอมไพล์) ชุดพารามิเตอร์
### Swift 6.x — ความปลอดภัยในการทำงานพร้อมกัน (2024–ปัจจุบัน)
- **6.0**: การตรวจสอบการทำงานพร้อมกันอย่างเข้มงวดตามค่าเริ่มต้น การพิมพ์แบบพ่น
## วิวัฒนาการพร้อมกัน
```
1.0:  GCD (Grand Central Dispatch) — Objective-C pattern
2.0:  Protocol extensions for async patterns
5.5:  async/await, actors, Sendable
5.10: Complete concurrency checking
6.0:  Strict concurrency by default (data race safety)
```

## ประเภทวิวัฒนาการของระบบ
```
1.0:  Optionals, generics, protocols
2.0:  Protocol extensions, protocol composition
4.0:  Codable, associated type constraints
5.1:  Opaque types (some), property wrappers
5.9:  Macros, parameter packs (variadic generics)
6.0:  Typed throws, strict Sendable
```

## Swift บนแพลตฟอร์มอื่น ๆ
```
2015: Swift open-sourced (Apache 2.0)
2015: Swift on Linux (Ubuntu)
2016: Swift on ARM (Raspberry Pi)
2017: Swift on Windows (experimental)
2019: TensorFlow Swift (later discontinued)
2020: Swift on AWS Lambda
2021: Vapor (server-side Swift framework)
2023: Swift on embedded systems (embedded Swift)
2025: Swift — cross-platform systems language
```

## กระบวนการวิวัฒนาการที่รวดเร็ว
```
SE-0001 (2015): First proposal
Over 400 proposals accepted by 2025
Key proposals:
  SE-0044: Import as member
  SE-0110: Distributed actors
  SE-0295: Codable improvements
  SE-0302: Sendable and @Sendable closures
  SE-0335: Introduce existential any
  SE-0346: Lightweight same-type requirements (some)
  SE-0401: Remove Actor Isolation Inference
  SE-0413: Typed throws
```

## การเติบโตของระบบนิเวศ
```
2014: Swift announced — replaces Objective-C
2015: Open source; Swift Package Manager
2016: Swift 3 — API redesign
2017: Swift 4 — Codable
2019: Swift 5 — ABI stability
2021: SwiftUI matures
2023: Swift 5.9 — macros
2025: Swift 6 — data race safety; used in iOS, macOS, server, embedded
```
