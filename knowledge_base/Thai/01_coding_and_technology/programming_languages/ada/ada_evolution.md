---
# Metadata
title: "Ada — Version History & Evolution"
description: "Comprehensive version history and evolution of Ada from Ada 83 to modern Ada."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial version history"
tags: [ada, version-history, evolution, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "10 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

# Ada - ประวัติเวอร์ชันและวิวัฒนาการ
## ไทม์ไลน์
| เวอร์ชั่น | ปี | ธีมหลัก |
|---------|-|-----------|
| เอด้า 83 | 1983 | **มาตรฐานแรก** (MIL-STD-1815A) — ตั้งชื่อตาม Ada Lovelace |
| เอด้า 87 | 1987 | การแก้ไขเล็กน้อย (ความแม่นยำ กฎการเข้าถึง) |
| เอด้า 95 | 1995 | **หลัก**: OOP (ประเภทแท็ก), ออบเจ็กต์ที่ได้รับการป้องกัน, การปรับปรุงการกำหนดงาน |
| เอด้า 2548 | 2548 | **อินเทอร์เฟซ**, ประเภทการเข้าถึงแบบไม่ระบุชื่อ, การปรับปรุงลูป`for`/ `while`
| เอด้า 2012 | 2555 | **การเขียนโปรแกรมเชิงมุมมอง**, สัญญา (ก่อน/หลังเงื่อนไข),`iterator`|
| เอด้า 2022 | 2022 | **`with ghost`** โครงสร้างแบบคู่ขนาน การปรับปรุงแบบเรียลไทม์ |
## เหตุการณ์สำคัญที่สำคัญ
### Ada 83 — การกำเนิด (1983)
- **1983**: กระทรวงกลาโหมสหรัฐฯ กำหนดให้ระบบฝังตัวเป็นภาษาเดียว
- Jean Ichbiah เป็นผู้นำการออกแบบที่ CII Honeywell Bull (ฝรั่งเศส)
- ตั้งชื่อตาม Ada Lovelace - โปรแกรมเมอร์คอมพิวเตอร์คนแรก
- คุณสมบัติที่สำคัญ: การพิมพ์ที่แข็งแกร่ง, แพ็คเกจ, งาน (การทำงานพร้อมกัน), ข้อมูลทั่วไป, ข้อยกเว้น
- **เป้าหมาย**: ระบบที่มีความสำคัญต่อความปลอดภัย — การบิน การป้องกัน อวกาศ
### Ada 95 - Ada เชิงวัตถุ (1995)
- **ภาษา OO ที่เป็นมาตรฐาน ISO แรก** (ก่อนที่ Java จะเป็นมาตรฐาน)
- ประเภทที่ติดแท็ก (คลาส), ประเภททั้งคลาส, การจัดส่งแบบไดนามิก
- วัตถุที่ได้รับการป้องกัน (การเข้าถึงข้อมูลพร้อมกันอย่างปลอดภัย)
- แพ็คเกจย่อย (ไลบรารีแบบลำดับชั้น)
- การกำหนดค่าตาม Pragma
### Ada 2005 — การปรับแต่ง (2005)
- อินเทอร์เฟซ (อินเทอร์เฟซหลายมรดก)
- ประเภทการเข้าถึงแบบไม่ระบุชื่อ (พอยน์เตอร์แบบง่าย)
- การปรับปรุงวง `for`
- ไลบรารีคอนเทนเนอร์ (รายการเชื่อมโยงสองเท่า เวกเตอร์ แผนที่)
- ขยายคำสั่ง `return`
### Ada 2012 — สัญญาและแง่มุม (2012)
- **การเขียนโปรแกรมเชิงมุมมอง**: ส่วนคำสั่ง`aspect`ที่แนบมากับการประกาศ
- **สัญญา**:`Pre`,`Post`,`Type_Invariant`— การตรวจสอบอย่างเป็นทางการในตัว
- การสนับสนุนตัววนซ้ำ (`for X of Container loop`)
- ตัวบ่งชี้ `overriding`
- ฟังก์ชั่นนิพจน์: `function F(X: Integer) return Integer is (X * 2);`
### เอด้า 2022 — Parallel & Ghost (2022)
- **`with ghost`**: รหัสผีสำหรับการตรวจสอบ (รวบรวมไว้ในการผลิต)
- **โครงสร้างแบบขนาน**: ลูป `parallel`, บล็อก `parallel`
- การปรับปรุงตามเวลาจริง
- การปรับปรุงคอนเทนเนอร์
- การปรับปรุงด้าน `Iterator`
## วิวัฒนาการไวยากรณ์
```ada
-- Ada 83: Package-based design
package Stack is
   procedure Push(Item : in Integer);
   function Pop return Integer;
   Stack_Empty : exception;
end Stack;

package body Stack is
   Max : constant := 100;
   Data : array(1..Max) of Integer;
   Top : Integer range 0..Max := 0;

   procedure Push(Item : in Integer) is
   begin
      Top := Top + 1;
      Data(Top) := Item;
   end Push;

   function Pop return Integer is
      Result : Integer;
   begin
      if Top = 0 then raise Stack_Empty; end if;
      Result := Data(Top);
      Top := Top - 1;
      return Result;
   end Pop;
end Stack;

-- Ada 95: Object-oriented
type Shape is tagged record
   X, Y : Float;
end record;

function Area(S : Shape) return Float is
begin
   return 0.0;
end Area;

type Circle is new Shape with record
   Radius : Float;
end record;

function Area(C : Circle) return Float is
begin
   return 3.14159 * C.Radius ** 2;
end Area;

-- Ada 2012: Contracts and aspects
type Temperature is new Float
   with Dynamic_Predicate => Temperature >= -273.15;

procedure Set_Temp(T : in out Temperature)
   with Pre  => T >= -273.15,
        Post => T'Old < T;  -- temperature must increase

-- Expression functions (Ada 2012)
function Double(X : Integer) return Integer is (X * 2);

-- Ada 2022: Parallel constructs
parallel
   for I in Data'Range loop
      Data(I) := Compute(I);
   end loop;

-- Ada 2022: Ghost code for verification
procedure Process(X : in out Integer)
   with Ghost => True,
        Pre   => X > 0,
        Post  => X > X'Old;
```

## วิวัฒนาการคุณสมบัติ
```
Ada 83:   Packages, strong typing, tasks, generics, exceptions
Ada 95:   Tagged types (OOP), protected objects, child packages
Ada 2005: Interfaces, anonymous access, containers
Ada 2012: Aspects, contracts (Pre/Post), iterators, expression functions
Ada 2022: Ghost code, parallel constructs, real-time improvements
```

## หลักการออกแบบที่สำคัญ
```
1. "Reliability first" — designed for safety-critical systems
2. "Strong typing" — catch errors at compile time
3. "Readability" — verbose but clear syntax
4. "Concurrency-safe" — protected objects, rendezvous, parallel
5. "Verifiable" — contracts, aspects, ghost code
6. "No hidden costs" — what you see is what you get (no GC required)
```

## การเติบโตของระบบนิเวศ
```
1983: Ada 83 — DoD mandate, defense/aviation adoption
1987: Ada 87 — minor fixes
1995: Ada 95 — OOP, ISO standard
1995: GNAT (GNU NYU Ada Translator) — open source compiler
2005: Ada 2005 — interfaces, containers
2012: Ada 2012 — contracts, aspects
2015: SPARK 2014 — formal verification for Ada
2022: Ada 2022 — parallel, ghost code
2025: Ada used in: aviation (DO-178C), space (ESA), rail, defense
       Compilers: GNAT (open source), ObjectAda, AdaCore tools
       SPARK subset used for formal verification of critical code
```
