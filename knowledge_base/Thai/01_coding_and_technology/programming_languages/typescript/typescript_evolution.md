---
# Metadata
title: "TypeScript — Version History & Evolution"
description: "Comprehensive version history and evolution of TypeScript from 0.8 to modern TypeScript."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial version history"
tags: [typescript, version-history, evolution, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "10 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

# TypeScript - ประวัติเวอร์ชันและวิวัฒนาการ
## ไทม์ไลน์
| เวอร์ชั่น | วันที่วางจำหน่าย | ธีมหลัก |
|---------|-------------|-----------|
| 0.8 | ต.ค. 2555 | การเผยแพร่สู่สาธารณะครั้งแรก (Anders Hejlsberg) |
| 0.9 | เม.ย. 2556 | ข้อมูลทั่วไป |
| 1.0 | เม.ย. 2557 | การเปิดตัวที่เสถียรครั้งแรก |
| 1.1 | พ.ย. 2557 | ประสิทธิภาพของคอมไพเลอร์ |
| 1.4 | ม.ค. 2558 | ประเภทตัวอักษรเทมเพลต (พื้นฐาน),`let`|
| 1.5 | ก.ค. 2558 | `namespace`,`destructuring`,`for...of`|
| 1.6 | ก.ย. 2558 |  คลาส`abstract`รองรับ JSX |
| 1.7 | พ.ย. 2558 | `async/await`(เป้าหมาย ES2017) |
| 1.8 | ก.พ. 2559 | แท็กสตริงเทมเพลต`--strictNullChecks`|
| 2.0 | ก.ย. 2559 | **หลัก**: ประเภทสหภาพ/ทางแยก,`never`,`keyof`,`protected`|
| 2.1 | ธ.ค. 2559 | `keyof`, ประเภทแมป, เครื่องกำเนิด`async`|
| 2.2 | ก.พ. 2560 |  ประเภท`object`ปรับปรุง`this`|
| 2.3 | เม.ย. 2560 | ค่าเริ่มต้นทั่วไป โหมด`--strict`|
| 2.4 | มิ.ย. 2560 | ประเภทที่อ่อนแอ สตริง enums |
| 2.5 | ก.ย. 2560 | การผูก catch ที่เป็นตัวเลือก |
| 2.6 | ต.ค. 2560 | ประเภทฟังก์ชันที่เข้มงวด`--strictFunctionTypes`|
| 2.7 | ม.ค. 2561 | การมอบหมายที่แน่นอน (`!`),`const`enums |
| 2.8 | มี.ค. 2561 | **ประเภทมีเงื่อนไข**,`Exclude`,`Extract`|
| 2.9 | มิ.ย. 2561 | `keyof`สำหรับตัวเลข/สัญลักษณ์ ประเภท`import()`|
| 3.0 | ก.ค. 2561 | **หลัก**: Tuples ที่เหลือ`unknown`การอ้างอิงโครงการ |
| 3.1 | ก.ย. 2561 | ประเภทที่แมปบนสิ่งอันดับ อาร์เรย์`readonly`|
| 3.2 | พ.ย. 2561 | `bigint`,`object`สเปรด |
| 3.4 | มี.ค. 2562 |  การยืนยัน`const`การอนุมานประเภทลำดับที่สูงกว่า |
| 3.5 | พฤษภาคม 2562 | `Omit`ชนิดตัวช่วย |
| 3.7 | พ.ย. 2562 | **การผูกมัดทางเลือก**, การรวมกันเป็นโมฆะ, ประเภทการเรียกซ้ำ |
| 3.8 | ก.พ. 2563 | `type-only`นำเข้า/ส่งออก ฟิลด์`#private`|
| 3.9 | พฤษภาคม 2563 | `// @ts-expect-error`ปรับปรุงการอนุมาน |
| 4.0 | ส.ค. 2563 | **หลัก**: สิ่งอันดับ Variadic, สิ่งอันดับที่มีป้ายกำกับ, ประเภทตัวอักษรของเทมเพลต |
| 4.1 | พ.ย. 2563 | **ประเภทตัวอักษรของเทมเพลต**, การแมปคีย์ใหม่, เงื่อนไขแบบเรียกซ้ำ |
| 4.2 | ก.พ. 2564 | คุณสมบัตินามธรรม`~`ในประเภทที่แมป |
| 4.3 | มิ.ย. 2564 | แยกประเภทการเขียน`override`คีย์เวิร์ด |
| 4.4 | ส.ค. 2564 | ลายเซ็นสัญลักษณ์/ดัชนี ควบคุมการไหลให้แคบลง |
| 4.5 | พ.ย. 2564 | `.d.ts`จาก`.js`,`await`ใน`.d.ts`|
| 4.6 | ก.พ. 2565 | การตรวจสอบฟังก์ชันแบบบล็อก ประเภทที่แน่นอนของส่วนที่เหลือของวัตถุ |
| 4.7 | พฤษภาคม 2565 |  ข้อจำกัด`extends`สำหรับ`infer`, ESM ใน`.ts`|
| 4.8 | ส.ค. 2565 | ปรับปรุงการลดจุดตัด แก้ไข`--strictNullChecks`|
| 4.9 | พ.ย. 2565 | ** ตัวดำเนินการ `satisfies`**,`in`การทำให้แคบลง |
| 5.0 | มี.ค. 2566 | **หลัก**: พารามิเตอร์ประเภท `const`, อุปกรณ์ตกแต่ง,`enum`ยกเครื่อง |
| 5.1 | มิ.ย. 2566 | ตัวตั้งค่าประเภทที่ไม่เกี่ยวข้อง`--exactOptionalPropertyTypes`|
| 5.2 | ส.ค. 2566 |  การประกาศ`using`(การจัดการทรัพยากรที่ชัดเจน) |
| 5.3 | พ.ย. 2566 | นำเข้าแอตทริบิวต์`switch true`ทำให้แคบลง |
| 5.4 | มี.ค. 2567 |  ยูทิลิตี้`NoInfer`พารามิเตอร์ปิดแคบลง
| 5.5 | มิ.ย. 2567 | เพรดิเคตประเภทที่อนุมาน`@`สำหรับ regex |
| 5.6 | ก.ย. 2567 | `--erasableSyntaxOnly`ตัวช่วยตัววนซ้ำ |
| 5.7 | พ.ย. 2567 | `--noCheck`การเสร็จสิ้นเส้นทาง |
| 5.8 | ก.พ. 2568 | ปรับปรุง`isolatedDeclarations`|
## เหตุการณ์สำคัญที่สำคัญ
### วันแรก (2555–2558)
- **0.8 (2012)**: Anders Hejlsberg (ผู้สร้าง C#) เป็นผู้นำ TypeScript ที่ Microsoft
- **1.0 (2014)**: รุ่นเสถียร; คลาส, อินเตอร์เฟส, ประเภทพื้นฐาน
- **1.5 (2015)**: ฟีเจอร์ ES6 — การทำลายล้าง, เนมสเปซ, `for...of`
### การปฏิวัติประเภท (2559–2561)
- **2.0 (2016)**: ประเภทยูเนี่ยน, ประเภททางแยก,`never`,`keyof`— ระบบประเภทของ TypeScript จะไม่ซ้ำกัน
- **2.8 (2018)**: ประเภทแบบมีเงื่อนไข — รากฐานสำหรับการเขียนโปรแกรมระดับประเภทขั้นสูง
- **3.0 (2018)**: สิ่งอันดับในพารามิเตอร์ส่วนที่เหลือ ประเภท`unknown`การอ้างอิงโครงการ
### Modern TypeScript (2019–ปัจจุบัน)
- **3.7 (2019)**: การผูกมัดเสริม`?.`และการรวมกันเป็นโมฆะ`??`(ก่อนมาตรฐาน JS!)
- **4.0 (2020)**: สิ่งอันดับที่หลากหลาย, ประเภทลิเทอรัลเทมเพลต
- **4.1 (2020)**: ประเภทตัวอักษรของเทมเพลต — การจัดการสตริงระดับประเภท
- **4.9 (2022)**: ตัวดำเนินการ`satisfies`— การตรวจสอบประเภทโดยไม่ต้องขยับขยาย
- **5.0 (2023)**: พารามิเตอร์ประเภท `const`, อุปกรณ์ตกแต่ง (ระยะที่ 3)
- **5.2 (2023)**: การประกาศ`using`— การจัดการทรัพยากรที่ชัดเจน
## ประเภทวิวัฒนาการของระบบ
```
2012: Basic types, classes, interfaces
2014: Generics, enums
2016: Union types, intersection types, discriminated unions
2018: Conditional types, mapped types, keyof, infer
2020: Template literal types, variadic tuples
2022: satisfies operator
2023: const type parameters
2023: using declarations
```

## วิวัฒนาการมัณฑนากร
```
2014: TypeScript experimental decorators (legacy)
2022: TC39 stage 3 decorators proposal
2023: TypeScript 5.0 — standard decorators (stage 3)
2024: Both legacy and standard decorators supported
```

## วิวัฒนาการการกำหนดค่า
```
2014: Basic tsconfig.json
2016: --strict flag introduced
2017: --strictFunctionTypes, --strictNullChecks
2018: --strict mode becomes recommended
2020: --strictPropertyInitialization
2023: --exactOptionalPropertyTypes
2024: --erasableSyntaxOnly, --noCheck
```

## การเติบโตของระบบนิเวศ
```
2012: TypeScript launches — few adopters
2014: Angular 2 built with TypeScript
2016: VS Code (built with TS) drives adoption
2018: TypeScript overtakes Flow (React community)
2020: TypeScript used by most npm packages
2023: TypeScript 5.0 — decorators, const generics
2025: TypeScript — de facto standard for large JS projects
```

## การตัดสินใจออกแบบที่สำคัญ
```
1. Structural typing (not nominal) — duck typing for types
2. Gradual adoption — any type, type widening
3. Erased types — no runtime overhead
4. JS compatibility — all valid JS is valid TS
5. Declaration files (.d.ts) — types for JS libraries
6. Playground — interactive type exploration
```
