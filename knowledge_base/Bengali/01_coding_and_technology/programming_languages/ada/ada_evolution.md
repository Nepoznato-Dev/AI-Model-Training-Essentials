<!--
---
# Metadata
title: "Ada — Version History & Evolution"
description: "Comprehensive version history and evolution of Ada from Ada 83 to modern Ada."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
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

-->
# অ্যাডা - সংস্করণ ইতিহাস এবং বিবর্তন
## টাইমলাইন
| সংস্করণ | বছর | মূল থিম |
|---------|------|------------|
| আদা 83 | 1983 | **প্রথম মান** (MIL-STD-1815A) — অ্যাডা লাভলেসের নামে নামকরণ করা হয়েছে |
| আদা 87 | 1987 | ক্ষুদ্র সংশোধন (নির্ভুলতা, অ্যাক্সেসযোগ্যতার নিয়ম) |
| আদা 95 | 1995 | **মেজর**: OOP (ট্যাগ করা প্রকার), সুরক্ষিত বস্তু, টাস্কিং উন্নতি |
| অ্যাডা 2005 | 2005 | **ইন্টারফেস**, বেনামী অ্যাক্সেসের ধরন,`for`/`while`লুপ উন্নতি |
| অ্যাডা 2012 | 2012 | **আসপেক্ট-ওরিয়েন্টেড প্রোগ্রামিং**, চুক্তি (পূর্ব/পরবর্তী শর্তাবলী),`iterator`|
| অ্যাডা 2022 | 2022 | **`with ghost`**, সমান্তরাল নির্মাণ, রিয়েল-টাইম উন্নতি |
## প্রধান মাইলফলক
### অ্যাডা 83 — দ্য বার্থ (1983)
- **1983**: মার্কিন প্রতিরক্ষা বিভাগ এমবেডেড সিস্টেমের জন্য একটি একক ভাষা বাধ্যতামূলক করে
- জিন ইচবিয়াহ CII হানিওয়েল বুল (ফ্রান্স) এর ডিজাইনে নেতৃত্ব দেন
- অ্যাডা লাভলেসের নামানুসারে - প্রথম কম্পিউটার প্রোগ্রামার
- মূল বৈশিষ্ট্য: শক্তিশালী টাইপিং, প্যাকেজ, কাজ (একসঙ্গে), জেনেরিক, ব্যতিক্রম
- **লক্ষ্য**: নিরাপত্তা-সমালোচনা ব্যবস্থা — বিমান চলাচল, প্রতিরক্ষা, স্থান
### অ্যাডা 95 — অবজেক্ট-ওরিয়েন্টেড অ্যাডা (1995)
- **প্রথম ISO-প্রমিত OO ভাষা** (জাভা প্রমিত হওয়ার আগে)
- ট্যাগ করা প্রকার (ক্লাস), ক্লাস-ওয়াইড প্রকার, ডাইনামিক ডিসপ্যাচ
- সুরক্ষিত বস্তু (নিরাপদ সমসাময়িক ডেটা অ্যাক্সেস)
- চাইল্ড প্যাকেজ (অনুক্রমিক লাইব্রেরি)
- প্রাগমা-ভিত্তিক কনফিগারেশন
### অ্যাডা 2005 — পরিমার্জন (2005)
- ইন্টারফেস (ইন্টারফেসের একাধিক উত্তরাধিকার)
- বেনামী অ্যাক্সেসের ধরন (সরলীকৃত পয়েন্টার)
-`for`লুপ উন্নতি
- কন্টেইনার লাইব্রেরি (দ্বৈত লিঙ্কযুক্ত তালিকা, ভেক্টর, মানচিত্র)
- বর্ধিত`return`বিবৃতি
### অ্যাডা 2012 — চুক্তি এবং দিক (2012)
- **আসপেক্ট-ওরিয়েন্টেড প্রোগ্রামিং**: ঘোষণার সাথে`aspect`ধারা সংযুক্ত
- **চুক্তি**: `Pre`, `Post`,`Type_Invariant`— আনুষ্ঠানিক যাচাইকরণ বিল্ট ইন
- ইটারেটর সমর্থন (`for X of Container loop`)
-`overriding`সূচক
- এক্সপ্রেশন ফাংশন: `function F(X: Integer) return Integer is (X * 2);`
### অ্যাডা 2022 — সমান্তরাল এবং ভূত (2022)
- **`with ghost`**: যাচাইকরণের জন্য ঘোস্ট কোড (উৎপাদনে সংকলিত)
- **সমান্তরাল নির্মাণ**:`parallel`লুপ,`parallel`ব্লক
- রিয়েল-টাইম উন্নতি
- ধারক উন্নতি
-`Iterator`দিক পরিমার্জন
## সিনট্যাক্স বিবর্তন
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

## বৈশিষ্ট্য বিবর্তন
```
Ada 83:   Packages, strong typing, tasks, generics, exceptions
Ada 95:   Tagged types (OOP), protected objects, child packages
Ada 2005: Interfaces, anonymous access, containers
Ada 2012: Aspects, contracts (Pre/Post), iterators, expression functions
Ada 2022: Ghost code, parallel constructs, real-time improvements
```

## মূল ডিজাইনের নীতি
```
1. "Reliability first" — designed for safety-critical systems
2. "Strong typing" — catch errors at compile time
3. "Readability" — verbose but clear syntax
4. "Concurrency-safe" — protected objects, rendezvous, parallel
5. "Verifiable" — contracts, aspects, ghost code
6. "No hidden costs" — what you see is what you get (no GC required)
```

## ইকোসিস্টেম বৃদ্ধি
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
