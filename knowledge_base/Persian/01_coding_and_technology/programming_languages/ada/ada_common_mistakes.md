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

# آدا - اشتباهات رایج و ضد الگوها
این سند متداول ترین اشتباهات، تله ها و ضد الگوها در آدا را با اصلاحات فهرست می کند.
---

## 1. عدم استفاده از `pragma Strict`
```ada
-- ❌ WRONG — allowing implicit conversions
X : Integer := 3.14;  -- may compile with warnings

-- ✅ CORRECT — strict mode catches issues
pragma Strict;
X : Integer := 3.14;  -- compile error: type mismatch
```

---

## 2. خطاهای محدوده در زیرگروه ها
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

## 3. عدم استفاده از پارامترهای نامگذاری شده برای خوانایی
```ada
-- ❌ WRONG — positional parameters
Create(File, Out_File, "data.txt");

-- ✅ CORRECT — named association
Create(File => File, Mode => Out_File, Name => "data.txt");
```

---

## 4. فراموش کردن رسیدگی به استثناها
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

## 5. Task Deadlock
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

## خلاصه
تایپ قوی Ada از بسیاری از اشکالات جلوگیری می کند اما مستلزم نظم و انضباط است: از`pragma Strict`استفاده کنید،`Constraint_Error`را برای انواع فرعی مدیریت کنید، از تداعی پارامترهای نامگذاری شده برای خوانایی استفاده کنید، همیشه استثناها را مدیریت کنید، و ارتباطات وظیفه را با دقت طراحی کنید تا از بن بست جلوگیری شود. Ada به برنامه ریزی دقیق و ایمنی آگاهانه پاداش می دهد.