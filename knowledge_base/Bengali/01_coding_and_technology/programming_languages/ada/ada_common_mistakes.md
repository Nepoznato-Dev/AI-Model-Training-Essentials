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
# অ্যাডা — সাধারণ ভুল এবং অ্যান্টি-প্যাটার্নস
এই নথিটি সংশোধন সহ অ্যাডা-তে সবচেয়ে সাধারণ ভুল, ফাঁদ এবং অ্যান্টি-প্যাটার্নগুলি ক্যাটালগ করে৷
---

## 1.`pragma Strict`ব্যবহার করছেন না
```ada
-- ❌ WRONG — allowing implicit conversions
X : Integer := 3.14;  -- may compile with warnings

-- ✅ CORRECT — strict mode catches issues
pragma Strict;
X : Integer := 3.14;  -- compile error: type mismatch
```

---

## 2. সাবটাইপগুলিতে রেঞ্জ ত্রুটি
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

## 3. পঠনযোগ্যতার জন্য নামযুক্ত পরামিতি ব্যবহার করছেন না
```ada
-- ❌ WRONG — positional parameters
Create(File, Out_File, "data.txt");

-- ✅ CORRECT — named association
Create(File => File, Mode => Out_File, Name => "data.txt");
```

---

## 4. ব্যতিক্রমগুলি পরিচালনা করতে ভুলে যাওয়া
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

## 5. টাস্ক ডেডলক
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

## সারাংশ
Ada এর শক্তিশালী টাইপিং অনেক বাগ প্রতিরোধ করে কিন্তু শৃঙ্খলার প্রয়োজন:`pragma Strict`ব্যবহার করুন, সাব-টাইপের জন্য`Constraint_Error`পরিচালনা করুন, পঠনযোগ্যতার জন্য নামযুক্ত প্যারামিটার অ্যাসোসিয়েশন ব্যবহার করুন, সর্বদা ব্যতিক্রমগুলি পরিচালনা করুন এবং অচলাবস্থা এড়াতে সাবধানে কাজ যোগাযোগ ডিজাইন করুন। অ্যাডা সতর্ক, নিরাপত্তা-সচেতন প্রোগ্রামিংকে পুরস্কৃত করে।