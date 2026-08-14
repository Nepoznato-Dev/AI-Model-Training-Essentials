---
# Metadata
title: "Ada — Syntax Reference"
description: "Detailed syntax reference for Ada covering tasking, protected objects, generics, contracts, and safety-critical programming patterns."
category: "Coding and Technology"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "AI Model Training Team"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    author: "AI Model Training Team"
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

# एडा - सिंटैक्स संदर्भ
यह दस्तावेज़ Ada (2012/2022) के लिए एक व्यापक, संरचित वाक्यविन्यास संदर्भ प्रदान करता है। यह संपूर्ण सिंटैक्स पैटर्न, टास्किंग, संरक्षित ऑब्जेक्ट, जेनरिक और सुरक्षा-महत्वपूर्ण प्रोग्रामिंग पर ध्यान केंद्रित करके मुख्य एडीए संदर्भ को पूरक करता है।
---

## ऑपरेटर्स और अभिव्यक्तियाँ
| ऑपरेटर | नाम | उदाहरण | नोट्स |
|-------|------|------|-------|
| `+``-``*``/``**`| अंकगणित | `A ** 2`| |
| `mod``rem` | मॉड्यूलर/शेष | `A mod B`| `mod`सदैव सकारात्मक |
| `&`| सम्मिलन | `"hello" & " world"`| |
| `=``/=` | समानता | `A = B`| |
| `<``>``<=``>=` | तुलना | `A >= B`| |
| `and``or``not``xor` | तार्किक | `A and B`| |
| `and then``or else` | शॉर्ट-सर्किट | `A and then B`| |
| `in``not in` | रेंज सदस्यता | `X in 1 .. 10`| |
| `:=`| असाइनमेंट | `X := 10`| |
---

## प्रकार एवं उपप्रकार
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

## प्रवाह को नियंत्रित करें
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

## संरक्षित वस्तुएँ एवं कार्य
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

## अनुबंध एवं सत्यापन
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

## सारांश
एडा का वाक्यविन्यास क्रियात्मक लेकिन सटीक है। प्रत्येक निर्माण स्पष्टता और सुरक्षा के लिए डिज़ाइन किया गया है। संरक्षित वस्तुएँ भाषा स्तर पर डेटा दौड़ को समाप्त करती हैं। अनुबंध (पूर्व/बाद की शर्तें, अपरिवर्तनीय) शुद्धता आवश्यकताओं को स्पष्ट और जांचने योग्य बनाते हैं। जेनेरिक प्रकार-सुरक्षित पुन: उपयोग प्रदान करते हैं। सुरक्षा-महत्वपूर्ण प्रणालियों के लिए, एडा का सिंटैक्स कोई बोझ नहीं है - यह गारंटी है कि कोड वही करता है जो वह कहता है।