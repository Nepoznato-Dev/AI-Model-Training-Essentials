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
# एडा - सामान्य गलतियाँ और विरोधी पैटर्न
यह दस्तावेज़ सुधार के साथ एडीए में सबसे आम गलतियों, जाल और विरोधी पैटर्न को सूचीबद्ध करता है।
---

## 1.`pragma Strict`का उपयोग नहीं करना
```ada
-- ❌ WRONG — allowing implicit conversions
X : Integer := 3.14;  -- may compile with warnings

-- ✅ CORRECT — strict mode catches issues
pragma Strict;
X : Integer := 3.14;  -- compile error: type mismatch
```

---

## 2. उपप्रकारों पर रेंज त्रुटियाँ
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

## 3. पठनीयता के लिए नामित पैरामीटर्स का उपयोग न करना
```ada
-- ❌ WRONG — positional parameters
Create(File, Out_File, "data.txt");

-- ✅ CORRECT — named association
Create(File => File, Mode => Out_File, Name => "data.txt");
```

---

## 4. अपवादों को संभालना भूल जाना
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

##5. कार्य गतिरोध
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

## सारांश
एडा की मजबूत टाइपिंग कई बग को रोकती है लेकिन अनुशासन की आवश्यकता होती है:`pragma Strict`का उपयोग करें, उपप्रकारों के लिए`Constraint_Error`को संभालें, पठनीयता के लिए नामित पैरामीटर एसोसिएशन का उपयोग करें, हमेशा अपवादों को संभालें, और गतिरोध से बचने के लिए कार्य संचार को सावधानीपूर्वक डिजाइन करें। एडा सावधान, सुरक्षा के प्रति सचेत प्रोग्रामिंग को पुरस्कृत करता है।