---
# Metadata
title: "Haskell — Version History & Evolution"
description: "Comprehensive version history and evolution of Haskell from Haskell 1.0 to modern Haskell."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial version history"
tags: [haskell, version-history, evolution, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "10 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

# Haskell - ประวัติเวอร์ชันและวิวัฒนาการ
## ไทม์ไลน์
| เวอร์ชั่น | ปี | ธีมหลัก |
|---------|-|-----------|
| ฮาสเคล 1.0 | 1990 | การเปิดตัวครั้งแรก (ความพยายามของคณะกรรมการ) |
| ฮาสเคล 1.2 | 1992 | การทดลองระบบวัตถุ |
| ฮาสเคล 1.3 | 1996 | ประเภทคลาสแนะนำ |
| ฮาสเคล 1.4 | 1997 | `IO`monad ชี้แจง |
| ฮาสเคล 98 | 1998 | **มาตรฐานมั่นคงอันดับหนึ่ง** |
| ฮาสเคล 2010 | 2010 | **ปรับปรุงมาตรฐาน** Cabal โมดูล |
| GHC 7.0 | 2554 | พิมพ์ตระกูล ชนิดข้อมูล |
| GHC 7.4 | 2555 | ข้อเสนอการสมัคร-Monad เริ่มต้น |
| GHC 7.6 | 2013 | พิมพ์การปรับปรุงตระกูล |
| GHC 7.8 | 2014 | คำพ้องความหมายรูปแบบ`NegativeLiterals`|
| GHC 7.10 | 2558 | **ข้อเสนอ Monad แบบสมัคร (AMP)**,`-XStrict`|
| GHC 8.0 | 2559 | **TypeApplications**,`MonadFail`, ข้อผิดพลาดประเภทที่กำหนดเอง |
| GHC 8.2 | 2017 | แกะกล่อง กระเป๋าเป้ (ระบบโมดูล) |
| GHC 8.4 | 2018 | พาธฐานแบบนามธรรม`Semigroup`>>`Monoid`|
| GHC 8.6 | 2018 | StarIsType,`DerivingVia`|
| GHC 8.8 | 2019 | MonadFail ในโหมโรง |
| GHC 8.10 | 2020 | สัญกรณ์`do`แบบครบวงจร ชนิดความหลากหลาย |
| GHC 9.0 | 2021 | **ความหลากหลายแบบลิวิตี** ประเภทเชิงเส้น |
| GHC 9.2 | 2022 |`do`ที่ผ่านการรับรอง ปรับปรุงข้อความแสดงข้อผิดพลาด |
| GHC 9.4 | 2022 | **GHC2021** ชุดส่วนขยายภาษา`OverloadedRecordDot`|
| GHC 9.6 | 2023 | อาร์กิวเมนต์ประเภทที่จำเป็น`TypeAbstractions`|
| GHC 9.8 | 2024 | `TypeAbstractions`มีเสถียรภาพและปรับปรุงข้อความแสดงข้อผิดพลาด |
| GHC 9.10 | 2024 | การปรับแต่งประสิทธิภาพเพิ่มเติม |
| GHC 9.12 | 2025 | การพัฒนาอย่างต่อเนื่อง |
## เหตุการณ์สำคัญที่สำคัญ
### Haskell 1.x - ปีของคณะกรรมการ (1990–1998)
- **1990**: Haskell 1.0 — ภาษาการทำงานแบบขี้เกียจที่ออกแบบโดยคณะกรรมการ
- **1.3 (1996)**: ประเภทคลาส — คุณลักษณะการกำหนดของ Haskell
- **1.4 (1997)**:`IO`monad ชี้แจง — วิธีจัดการกับผลข้างเคียงอย่างหมดจด
- **Haskell 98**: มาตรฐานเสถียรตัวแรก; ยังคงอ้างอิงถึงวันนี้
### Haskell 2010 - มาตรฐานสมัยใหม่
- **2010**: ปรับปรุงมาตรฐาน — Cabal (ระบบแพ็คเกจ) ปรับปรุงระบบโมดูล
- GHC กลายเป็นคอมไพเลอร์โดยพฤตินัย
- Cabal + Hackage = ระบบนิเวศแพ็คเกจของ Haskell
### GHC 7.x — ประเภท กำลังของระบบ (2011–2015)
- ประเภทตระกูล ชนิดข้อมูล ชนิดพหุสัณฐาน
- Applicative-Monad Proposal (AMP) - แก้ไขลำดับชั้นของคลาสประเภท
- คำพ้องรูปแบบ, ส่วนขยาย `Strict`
### GHC 8.x — Haskell สมัยใหม่ (2016–2020)
-`TypeApplications`- อาร์กิวเมนต์ประเภทที่ชัดเจนที่ไซต์การโทร
- ข้อผิดพลาดประเภทกำหนดเอง — ข้อความคอมไพเลอร์ที่ดีกว่า
- กระเป๋าเป้สะพายหลัง — ระบบโมดูลสำหรับการออกแบบตามส่วนประกอบ
-`DerivingVia`— กลยุทธ์การหามาแบบยืดหยุ่น
### GHC 9.x — การปฏิวัติการใช้งาน (2021–ปัจจุบัน)
- **9.0**: Levity polymorphism ประเภทเชิงเส้น (ความปลอดภัยของทรัพยากร)
- **9.2**:`do`ที่ผ่านการรับรอง ปรับปรุงข้อความแสดงข้อผิดพลาด
- **9.4**: **GHC2021** — ส่วนขยายเริ่มต้นที่ทันสมัย `OverloadedRecordDot`(การเข้าถึงฟิลด์ด้วย`.`)
- **9.6**: อาร์กิวเมนต์ประเภทที่จำเป็น`TypeAbstractions`
- **9.8–9.12**: ปรับปรุงข้อความแสดงข้อผิดพลาดและประสิทธิภาพอย่างต่อเนื่อง
## วิวัฒนาการไวยากรณ์
```haskell
-- Haskell 98: Basic type classes
class Eq a where
  (==) :: a -> a -> Bool

-- GHC extensions: Type applications (GHC 8.0)
-- Before:
read "[1,2,3]" :: [Int]
-- After:
read @[Int] "[1,2,3]"

-- GHC 9.4: OverloadedRecordDot
-- Before:
name (getPerson user)
-- After:
user.person.name

-- GHC 9.0: Linear types
-- Before:
processFile :: FilePath -> IO Result
-- After:
processFile :: FilePath %1 -> IO Result  -- file handle used exactly once

-- GHC 8.0: Custom type errors
type family ErrorMessage (a :: Type) :: ErrorMessage where
  ErrorMessage (NotSerializable a) =
    'Text "Cannot serialize type " ':<>: 'ShowType a
```

## ประเภทวิวัฒนาการของระบบ
```
Haskell 1.0:  Basic types, algebraic data types, pattern matching
Haskell 1.3:  Type classes
Haskell 98:   Multi-parameter type classes, functional dependencies
GHC 6.x:     GADTs, type families, rank-N types
GHC 7.0:     Data kinds, kind polymorphism
GHC 7.10:    Applicative-Monad Proposal
GHC 8.0:     TypeApplications, custom type errors
GHC 8.2:     Unboxed sums
GHC 9.0:     Levity polymorphism, linear types
GHC 9.4:     OverloadedRecordDot, GHC2021
GHC 9.6:     Required type arguments, TypeAbstractions
```

## การเห็นพ้องต้องกันและความเท่าเทียม
```
Haskell 98:  No standard concurrency model
2004: GHC 6.2 — Software Transactional Memory (STM)
2007: GHC 6.8 — lightweight threads (green threads)
2011: async library — structured concurrency
2018: io-streams, conduit — streaming I/O
2021: Linear types — resource-safe concurrency
2025: GHC + effect systems (Effectful, UnliftIO)
```

## หลักการออกแบบที่สำคัญ
```
1. "Lazy by default" — non-strict evaluation
2. "Pure by default" — side effects explicit via monads
3. "Types are truth" — strong static typing
4. "Referential transparency" — same input → same output
5. "Composability" — small building blocks, compose freely
6. "Make illegal states unrepresentable" — type system as design tool
```

## การเติบโตของระบบนิเวศ
```
1990: Haskell 1.0 — academic curiosity
1998: Haskell 98 — stable standard
2007: Cabal + Hackage — package ecosystem
2010: Haskell 2010 — revised standard
2012: Stack build tool — reproducible builds
2015: Haskell in industry — Facebook, Standard Chartered, Well-Typed
2021: GHC 9.0 — levity polymorphism, linear types
2023: GHC 9.6 — type abstractions
2025: Haskell used in finance, compilers, formal verification,
       blockchain (Cardano), and academic research
       GHC, Stack, Cabal; key libraries: lens, aeson, servant, yesod
```
