<!--
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

-->
# Ada — عام غلطیاں اور اینٹی پیٹرن
یہ دستاویز ایڈا میں سب سے عام غلطیوں، ٹریپس، اور اینٹی پیٹرن کو تصحیح کے ساتھ کیٹلاگ کرتی ہے۔
---

## 1.`pragma Strict`استعمال نہیں کرنا
```ada
-- ❌ WRONG — allowing implicit conversions
X : Integer := 3.14;  -- may compile with warnings

-- ✅ CORRECT — strict mode catches issues
pragma Strict;
X : Integer := 3.14;  -- compile error: type mismatch
```

---

## 2. ذیلی قسموں پر رینج کی خرابیاں
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

## 3. پڑھنے کی اہلیت کے لیے نامزد پیرامیٹرز کا استعمال نہیں کرنا
```ada
-- ❌ WRONG — positional parameters
Create(File, Out_File, "data.txt");

-- ✅ CORRECT — named association
Create(File => File, Mode => Out_File, Name => "data.txt");
```

---

## 4. مستثنیات کو ہینڈل کرنا بھول جانا
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

## 5. ٹاسک ڈیڈ لاک
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

## خلاصہ
Ada کی مضبوط ٹائپنگ بہت سے کیڑوں کو روکتی ہے لیکن نظم و ضبط کی ضرورت ہوتی ہے:`pragma Strict`استعمال کریں، ذیلی قسموں کے لیے`Constraint_Error`کو ہینڈل کریں، پڑھنے کی اہلیت کے لیے نامزد پیرامیٹر ایسوسی ایشن کا استعمال کریں، ہمیشہ مستثنیات کو ہینڈل کریں، اور تعطل سے بچنے کے لیے ٹاسک کمیونیکیشن کو احتیاط سے ڈیزائن کریں۔ Ada محتاط، حفاظت سے متعلق پروگرامنگ کو انعام دیتا ہے۔