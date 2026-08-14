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

# অ্যাডা - সিনট্যাক্স রেফারেন্স
এই নথিটি Ada (2012/2022) এর জন্য একটি ব্যাপক, কাঠামোগত সিনট্যাক্স রেফারেন্স প্রদান করে। এটি সম্পূর্ণ সিনট্যাক্স প্যাটার্ন, টাস্কিং, সুরক্ষিত বস্তু, জেনেরিক, এবং নিরাপত্তা-সমালোচনামূলক প্রোগ্রামিং এর উপর ফোকাস করে প্রধান অ্যাডা রেফারেন্সের পরিপূরক।
---

## অপারেটর এবং এক্সপ্রেশন
| অপারেটর | নাম | উদাহরণ | নোট |
|----------|------|---------|-------|
| `+``-``*``/``**`| পাটিগণিত | `A ** 2`| |
| `mod``rem` | মডুলার/বাকি | `A mod B`| `mod`সবসময় ইতিবাচক |
| `&`| সংযুক্তি | `"hello" & " world"`| |
| `=``/=` | সমতা | `A = B`| |
| `<``>``<=``>=` | তুলনা | `A >= B`| |
| `and``or``not``xor` | যৌক্তিক | `A and B`| |
| `and then``or else` | শর্ট সার্কিট | `A and then B`| |
| `in``not in` | রেঞ্জ সদস্যপদ | `X in 1 .. 10`| |
| `:=`| অ্যাসাইনমেন্ট | `X := 10`| |
---

## প্রকার ও উপপ্রকার
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

## নিয়ন্ত্রণ প্রবাহ
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

## সুরক্ষিত বস্তু এবং কাজ
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

## চুক্তি ও যাচাইকরণ
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

## সারাংশ
অ্যাডা এর সিনট্যাক্স ভার্বস কিন্তু সুনির্দিষ্ট। প্রতিটি নির্মাণ স্বচ্ছতা এবং নিরাপত্তার জন্য ডিজাইন করা হয়েছে। সুরক্ষিত বস্তু ভাষা স্তরে ডেটা রেস দূর করে। চুক্তিগুলি (পূর্ব/পরবর্তী শর্তাবলী, অপরিবর্তনীয়) সঠিকতার প্রয়োজনীয়তাগুলিকে সুস্পষ্ট এবং পরীক্ষাযোগ্য করে তোলে। জেনেরিক টাইপ-নিরাপদ পুনঃব্যবহার প্রদান করে। নিরাপত্তা-সমালোচনামূলক সিস্টেমের জন্য, Ada এর সিনট্যাক্স একটি বোঝা নয় - এটি একটি গ্যারান্টি যে কোডটি যা বলে তা করে৷