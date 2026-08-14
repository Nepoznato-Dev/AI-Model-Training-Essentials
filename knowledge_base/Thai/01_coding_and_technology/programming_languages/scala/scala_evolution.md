<!--
---
# Metadata
title: "Scala — Version History & Evolution"
description: "Comprehensive version history and evolution of Scala from 1.0 to modern Scala."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial version history"
tags: [scala, version-history, evolution, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "10 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

-->
# Scala - ประวัติเวอร์ชันและวิวัฒนาการ
## ไทม์ไลน์
| เวอร์ชั่น | ปี | ธีมหลัก |
|---------|-|-----------|
| 1.0 | 2547 | การเปิดตัวครั้งแรก (Martin Odersky, EPFL) |
| 2.0 | 2549 | ประเภทโครงสร้าง การปรับปรุงการจับคู่รูปแบบ |
| 2.7 | 2552 | ห้องสมุดนักแสดง การอนุมานประเภทที่ได้รับการปรับปรุง |
| 2.8 | 2010 | **อาร์กิวเมนต์ที่มีชื่อ/ค่าเริ่มต้น** วัตถุแพ็คเกจ การออกแบบคอลเลกชันใหม่ |
| 2.9 | 2554 | คอลเลกชันแบบขนาน การแก้ไขสตริง |
| 2.10 | 2013 | **คลาสค่า** การปรับปรุงโดยนัย การแก้ไขสตริง |
| 2.11 | 2014 | การแก้ไขสตริง คอลเลกชันที่ปรับปรุงแล้ว |
| 2.12 | 2559 | **ประเภท SAM** (Java 8 lambdas) คอลเลกชันบน Strawman |
| 2.13 | 2019 | **การออกแบบคอลเลกชันใหม่** พารามิเตอร์ตามชื่อโดยนัย |
| 3.0 | 2021 | **หลัก**: คอมไพเลอร์ใหม่ (Dotty),`enum`,`given`/`using`, วิธีการขยาย |
| 3.1 | 2022 | ส่วนคำสั่งการส่งออก`opaque`นามแฝงประเภท |
| 3.2 | 2022 |  การปรับปรุง `inline`, คำหลัก`erased`|
| 3.3 | 2023 | **LTS release** — ค่าว่างที่ชัดเจน,`derives`clause |
| 3.4 | 2024 | อาร์กิวเมนต์ประเภทที่มีชื่อ, คำอธิบายประกอบ`@experimental`|
| 3.5 | 2024 | ตัวตรวจสอบการจับภาพ ปรับปรุงข้อความแสดงข้อผิดพลาด |
| 3.6 | 2025 | การปรับแต่งเพิ่มเติม การปรับปรุงประสิทธิภาพ |
## เหตุการณ์สำคัญที่สำคัญ
### สกาลายุคแรก (2547–2553)
- **2004**: Martin Odersky เปิดตัว Scala ซึ่งรวม OOP และ FP บน JVM
- **2.0–2.7**: ประเภทโครงสร้าง ตัวแสดง การอนุมานประเภทที่ได้รับการปรับปรุง
- **2.8 (2010)**: อาร์กิวเมนต์ที่มีชื่อ/ค่าเริ่มต้น วัตถุแพ็คเกจ การออกแบบคอลเลกชันใหม่ — "การเริ่มต้นสกาล่ายุคใหม่"
### สกาล่า 2.x ครบกำหนด (2011–2020)
- **2.9**: คอลเลกชันคู่ขนาน
- **2.10**: คลาสค่า, การแก้ไขสตริง, การปรับปรุงโดยนัย
- **2.12**: ประเภท SAM — การทำงานร่วมกันของ Java 8 ที่ราบรื่น
- **2.13**: การออกแบบไลบรารีคอลเลกชันหลักใหม่ (ค่าเริ่มต้นไม่เปลี่ยนรูป)
### สกาล่า 3 — ยุคฟื้นฟูศิลปวิทยา (2021–ปัจจุบัน)
- **3.0 (2021)**: เขียนคอมไพเลอร์ใหม่ทั้งหมด (Dotty → Scala 3)
  -`enum`แทนที่ลักษณะปิดผนึก + ต้นแบบคลาสเคส
  -`given`/`using`แทนที่พารามิเตอร์โดยนัย
  - วิธีการขยายจะแทนที่คลาสโดยนัย
  - ประเภท `match`, ประเภทสหภาพ, ประเภททางแยก
  - ไวยากรณ์แบบง่าย (วงเล็บปีกกาเสริม, คำหลักน้อยลง)
- **3.3 (2023)**: LTS แรก — ค่าว่างที่ชัดเจน, ส่วนคำสั่ง `derives`
- **3.4–3.6**: อาร์กิวเมนต์ประเภทที่มีชื่อ, ตัวตรวจสอบการจับภาพ, ประสิทธิภาพ
## วิวัฒนาการไวยากรณ์
```scala
// Scala 2: Implicit class for extension methods
implicit class StringOps(val s: String) extends AnyVal {
  def shout: String = s.toUpperCase + "!"
}

// Scala 3: Extension methods
extension (s: String)
  def shout: String = s.toUpperCase + "!"

// Scala 2: Sealed trait + case class (ADT)
sealed trait Color
case object Red extends Color
case object Blue extends Color

// Scala 3: enum
enum Color:
  case Red, Blue, Green

// Scala 2: Implicit parameters
def greet(implicit ctx: Context): String = ctx.name

// Scala 3: given/using
given ctx: Context = Context("Alice")
def greet(using ctx: Context): String = ctx.name

// Scala 3: Union types
def process(input: String | Int): String = input.toString

// Scala 3: Match types
type Elem[X] = X match
  case String => Char
  case List[t] => t
  case _ => X
```

## ประเภทวิวัฒนาการของระบบ
```
Scala 2.0:  Structural types, refinements
Scala 2.7:  Existential types
Scala 2.8:  Implicit resolution rules
Scala 2.10: Value classes, macro annotations
Scala 2.12: SAM conversion, Java 8 interop
Scala 2.13: Implicit by-name, literal types
Scala 3.0:  Union types, intersection types, match types,
            opaque types, enum, given/using, extension methods
Scala 3.3:  Explicit nulls, derives clause
Scala 3.4:  Named type arguments
Scala 3.5:  Capture checker (experimental)
```

## วิวัฒนาการพร้อมกัน
```
2009: Scala Actors library (green threads)
2011: Akka library (Actor model, JVM-based)
2013: Scala Futures + Promises (standard library)
2018: Cats Effect (functional effect system)
2020: ZIO (functional effect system, high performance)
2025: Scala 3 + virtual threads (Java 21 Loom integration)
```

## หลักการออกแบบที่สำคัญ
```
1. "Scalable language" — from scripts to large systems
2. "Unify OOP and FP" — everything is an object, everything is a function
3. "Type safety" — leverage the type system for correctness
4. "Interoperability" — seamless Java interop
5. "Expressiveness" — concise, elegant syntax
6. "Evidence-based" — type classes via given/using (Scala 3)
```

## การเติบโตของระบบนิเวศ
```
2004: Scala released by Martin Odersky (EPFL)
2009: Twitter adopts Scala — puts Scala on the map
2011: Akka framework — distributed computing
2012: Play Framework 2.0 — web development
2014: Apache Spark — big data processing in Scala
2016: sbt becomes standard build tool
2021: Scala 3 — modernized language
2025: Scala powers LinkedIn, Twitter, Netflix, The Guardian, Stripe
       sbt, Mill build tools; Akka, ZIO, Cats Effect ecosystems
```
