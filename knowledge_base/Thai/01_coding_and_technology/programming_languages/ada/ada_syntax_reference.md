---
# Metadata
title: "Ada — Syntax Reference"
description: "Detailed syntax reference for Ada covering tasking, protected objects, generics, contracts, and safety-critical programming patterns."
category: "Coding and Technology"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "Nepoznato-Dev"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    author: "Nepoznato-Dev"
    changes: "Initial syntax reference document"

# Review
created: "2026-08-09"
last_modified: "2026-08-09"
review_date: "2027-02-09"
reviewed_by: "Coding & Technology Knowledge Base Team"
next_review: "2027-08-09"

# Classification
tags: [ada, syntax-reference, tasking, protected-objects, generics, contracts, safety-critical, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "30 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Ada - การอ้างอิงไวยากรณ์
เอกสารนี้มีการอ้างอิงไวยากรณ์ที่มีโครงสร้างและครอบคลุมสำหรับ Ada (2012/2022) ช่วยเสริมการอ้างอิง Ada หลักโดยมุ่งเน้นไปที่รูปแบบไวยากรณ์ที่ละเอียดถี่ถ้วน การมอบหมายงาน อ็อบเจ็กต์ที่ได้รับการป้องกัน ข้อมูลทั่วไป และการเขียนโปรแกรมที่มีความสำคัญต่อความปลอดภัย
---

## ตัวดำเนินการและนิพจน์
| ตัวดำเนินการ | ชื่อ | ตัวอย่าง | หมายเหตุ |
|----------|-|---------|-------|
| `+``-``*``/``**`| เลขคณิต | `A ** 2`| |
| `mod``rem` | โมดูลาร์/ส่วนที่เหลือ | `A mod B`| `mod`เป็นบวกเสมอ |
| `&`| การต่อข้อมูล | `"hello" & " world"`| |
| `=``/=` | ความเท่าเทียมกัน | `A = B`| |
| `<``>``<=``>=` | การเปรียบเทียบ | `A >= B`| |
| `and``or``not``xor` | ตรรกะ | `A and B`| |
| `and then``or else` | ลัดวงจร | `A and then B`| |
| `in``not in` | สมาชิกช่วง | `X in 1 .. 10`| |
| `:=`| การมอบหมายงาน | `X := 10`| |
---

## ประเภทและประเภทย่อย
```ada
-- Scalar types
type Temperature is range -273 .. 5000;
type Byte is mod 256;
type Color is (Red, Green, Blue);

-- Subtypes (constrained views)
subtype Percentage is Integer range 0 .. 100;
subtype Port_Number is Integer range 0 .. 65535;

-- Records
type Point is record
   X : Float;
   Y : Float;
end record;

-- Tagged types (OOP)
type Shape is tagged record
   Name : String(1 .. 20);
end record;

type Circle is new Shape with record
   Radius : Float;
end record;

-- Access types (pointers)
type Node_Ptr is access all Node;
type Node is record
   Value : Integer;
   Next  : Node_Ptr;
end record;
```

---

## การควบคุมการไหล
```ada
-- if / elsif / else
if X > 0 then
   Put("positive");
elsif X < 0 then
   Put("negative");
else
   Put("zero");
end if;

-- case (exhaustive)
case Light is
   when Red    => Put("Stop");
   when Yellow => Put("Caution");
   when Green  => Put("Go");
end case;

-- for loop
for I in 1 .. 10 loop
   Put_Line(Integer'Image(I));
end loop;

-- for with reverse
for I in reverse 1 .. 10 loop
   Put_Line(Integer'Image(I));
end loop;

-- while loop
while not Done loop
   Process;
end loop;

-- loop (infinite with exit)
loop
   exit when Condition;
   Do_Something;
end loop;
```

---

## วัตถุและงานที่ได้รับการป้องกัน
```ada
-- Protected object (safe shared state)
protected type Buffer is
   entry Put(Item : Integer);
   entry Get(Item : out Integer);
   function Count return Natural;
private
   Data : array(1 .. 100) of Integer;
   Head, Tail : Positive := 1;
   Size : Natural := 0;
end Buffer;

protected body Buffer is
   entry Put(Item : Integer) when Size < Data'Length is
   begin
      Data(Tail) := Item;
      Tail := (Tail mod Data'Length) + 1;
      Size := Size + 1;
   end Put;

   entry Get(Item : out Integer) when Size > 0 is
   begin
      Item := Data(Head);
      Head := (Head mod Data'Length) + 1;
      Size := Size - 1;
   end Get;

   function Count return Natural is (Size);
end Buffer;

-- Task type
task type Worker is
   entry Start(Job : Integer);
end Worker;

task body Worker is
   My_Job : Integer;
begin
   accept Start(Job : Integer) do
      My_Job := Job;
   end Start;
   -- Process job...
end Worker;
```

---

## สัญญาและการตรวจสอบ
```ada
-- Pre/postconditions
function Sqrt(X : Float) return Float
   with Pre  => X >= 0.0,
        Post => Sqrt'Result >= 0.0;

-- Type invariants
type Bounded_Int is new Integer
   with Type_Invariant => Bounded_Int in 0 .. 100;

-- Loop invariants
while Condition loop
   -- Loop_Invariant => ...
   pragma Loop_Invariant (X >= 0);
   Process;
end loop;
```

---

## สรุป
ไวยากรณ์ของ Ada นั้นละเอียดแต่แม่นยำ โครงสร้างทุกชิ้นได้รับการออกแบบเพื่อความชัดเจนและปลอดภัย วัตถุที่ได้รับการป้องกันจะช่วยลดการแข่งขันของข้อมูลในระดับภาษา สัญญา (เงื่อนไขก่อน/หลัง, ค่าคงที่) ทำให้ข้อกำหนดด้านความถูกต้องชัดเจนและสามารถตรวจสอบได้ ยาสามัญให้นำกลับมาใช้ใหม่ได้อย่างปลอดภัย สำหรับระบบที่มีความสำคัญด้านความปลอดภัย ไวยากรณ์ของ Ada ไม่ใช่ภาระ แต่เป็นการรับประกันว่าโค้ดจะดำเนินการตามที่กล่าวไว้