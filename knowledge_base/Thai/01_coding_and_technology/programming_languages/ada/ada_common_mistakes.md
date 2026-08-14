---
# Metadata
title: "Ada — Common Mistakes & Anti-Patterns"
description: "Common pitfalls, traps, and anti-patterns in Ada with explanations and corrections."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial common mistakes document"
tags: [ada, common-mistakes, anti-patterns, pitfalls, best-practices, coding-and-technology]
difficulty_level: "intermediate"
estimated_reading_time: "15 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

# Ada - ข้อผิดพลาดทั่วไปและการต่อต้านรูปแบบ
เอกสารนี้รวบรวมข้อผิดพลาด กับดัก และรูปแบบการต่อต้านที่พบบ่อยที่สุดใน Ada พร้อมการแก้ไข
---

## 1. ไม่ได้ใช้ `pragma Strict`
```ada
-- ❌ WRONG — allowing implicit conversions
X : Integer := 3.14;  -- may compile with warnings

-- ✅ CORRECT — strict mode catches issues
pragma Strict;
X : Integer := 3.14;  -- compile error: type mismatch
```

---

## 2. ข้อผิดพลาดช่วงของประเภทย่อย
```ada
-- ❌ WRONG — assuming subtype checks at compile time
type Day is range 1 .. 31;
D : Day := 32;  -- Constraint_Error at runtime

-- ✅ CORRECT — validate input
D : Day := Day'Value(Input);
exception
   when Constraint_Error => Put_Line("Invalid day");
```

---

## 3. ไม่ใช้พารามิเตอร์ที่มีชื่อเพื่อให้อ่านง่าย
```ada
-- ❌ WRONG — positional parameters
Create(File, Out_File, "data.txt");

-- ✅ CORRECT — named association
Create(File => File, Mode => Out_File, Name => "data.txt");
```

---

## 4. ลืมที่จะจัดการกับข้อยกเว้น
```ada
-- ❌ WRONG — no exception handling
procedure Process is
   F : File_Type;
begin
   Open(F, In_File, "data.txt");
   -- use F...
end Process;
-- raises Name_Error if file doesn't exist

-- ✅ CORRECT — handle exceptions
procedure Process is
   F : File_Type;
begin
   Open(F, In_File, "data.txt");
   -- use F...
   Close(F);
exception
   when Name_Error => Put_Line("File not found");
   when others => Put_Line("Unexpected error");
end Process;
```

---

## 5. การหยุดชะงักของงาน
```ada
-- ❌ WRONG — tasks waiting on each other
task A is
   entry Start;
end A;
task body A is
begin
   B.Start;  -- waits for B
   accept Start do null; end Start;  -- B waits for A
end A;

-- ✅ CORRECT — design task communication carefully
-- Use protected objects for shared state
protected Counter is
   function Get return Integer;
   procedure Increment;
private
   Value : Integer := 0;
end Counter;
```

---

## สรุป
การพิมพ์ที่เข้มงวดของ Ada ป้องกันข้อผิดพลาดมากมาย แต่ต้องมีวินัย: ใช้`pragma Strict`จัดการ`Constraint_Error`สำหรับประเภทย่อย ใช้การเชื่อมโยงพารามิเตอร์ที่มีชื่อเพื่อให้อ่านง่าย จัดการกับข้อยกเว้นเสมอ และออกแบบการสื่อสารงานอย่างระมัดระวังเพื่อหลีกเลี่ยงการหยุดชะงัก Ada ให้รางวัลแก่การเขียนโปรแกรมที่คำนึงถึงความปลอดภัยและระมัดระวัง