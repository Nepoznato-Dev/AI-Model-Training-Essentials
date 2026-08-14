---
# Metadata
title: "Ada — Common Mistakes & Anti-Patterns"
description: "Common pitfalls, traps, and anti-patterns in Ada with explanations and corrections."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
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
# Ada — Những lỗi thường gặp và những mẫu phản đối
Tài liệu này liệt kê các lỗi, bẫy và mô hình phản đối phổ biến nhất trong Ada kèm theo các chỉnh sửa.
---

## 1. Không sử dụng `pragma Strict`
```ada
-- ❌ WRONG — allowing implicit conversions
X : Integer := 3.14;  -- may compile with warnings

-- ✅ CORRECT — strict mode catches issues
pragma Strict;
X : Integer := 3.14;  -- compile error: type mismatch
```

---

## 2. Lỗi phạm vi trên các kiểu con
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

## 3. Không sử dụng tham số được đặt tên để dễ đọc
```ada
-- ❌ WRONG — positional parameters
Create(File, Out_File, "data.txt");

-- ✅ CORRECT — named association
Create(File => File, Mode => Out_File, Name => "data.txt");
```

---

## 4. Quên xử lý các ngoại lệ
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

## 5. Nhiệm vụ bế tắc
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

## Bản tóm tắt
Khả năng gõ mạnh của Ada ngăn ngừa nhiều lỗi nhưng yêu cầu kỷ luật: sử dụng `pragma Strict`, xử lý`Constraint_Error`cho các kiểu con, sử dụng liên kết tham số được đặt tên để dễ đọc, luôn xử lý các trường hợp ngoại lệ và thiết kế giao tiếp nhiệm vụ một cách cẩn thận để tránh bế tắc. Ada khen thưởng việc lập trình cẩn thận, có ý thức an toàn.