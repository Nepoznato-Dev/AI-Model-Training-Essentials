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
# Ada - تاریخچه نسخه و تکامل
## جدول زمانی
| نسخه | سال | تم کلید |
|---------|------|-----------|
| آدا 83 | 1983 | **اولین استاندارد** (MIL-STD-1815A) — به نام آدا لاولیس |
| آدا 87 | 1987 | بازبینی جزئی (دقت، قوانین دسترسی) |
| آدا 95 | 1995 | **عمده**: OOP (انواع برچسب گذاری شده)، اشیاء محافظت شده، بهبود وظایف |
| Ada 2005 | 2005 | **رابط**، انواع دسترسی ناشناس، بهبودهای حلقه`for`/`while`|
| Ada 2012 | 2012 | **برنامه نویسی جنبه گرا**، قراردادها (پیش/پسشرط)،`iterator`|
| Ada 2022 | 2022 | **`with ghost`**، ساختارهای موازی، بهبودهای زمان واقعی |
## نقاط عطف اصلی
### Ada 83 - The Birth (1983)
- **1983**: وزارت دفاع ایالات متحده یک زبان واحد را برای سیستم های تعبیه شده الزام می کند
- Jean Ichbiah طراحی را در CII Honeywell Bull (فرانسه) رهبری می کند
- به نام آدا لاولیس - اولین برنامه نویس کامپیوتر
- ویژگی های کلیدی: تایپ قوی، بسته ها، وظایف (همزمان)، ژنریک، استثناها
- **هدف**: سیستم های ایمنی حیاتی - هوانوردی، دفاع، فضا
### Ada 95 - Ada شی گرا (1995)
- **اولین زبان OO استاندارد ISO** (قبل از استانداردسازی جاوا)
- انواع برچسب گذاری شده (کلاس ها)، انواع در سطح کلاس، اعزام پویا
- اشیاء محافظت شده (دسترسی ایمن به داده های همزمان)
- بسته های کودک (کتابخانه سلسله مراتبی)
- پیکربندی مبتنی بر پراگما
### Ada 2005 - Refinements (2005)
- رابط ها (ارث بری چندگانه رابط)
- انواع دسترسی ناشناس (نشانگرهای ساده شده)
- بهبودهای حلقه `for`
- کتابخانه های کانتینری (لیست های دارای پیوند دوگانه، بردارها، نقشه ها)
- بیانیه`return`توسعه یافته
### Ada 2012 — Contracts & Aspects (2012)
- **برنامه نویسی جنبه گرا**: بندهای`aspect`پیوست شده به اعلان ها
- **قراردادها**: `Pre`، `Post`،`Type_Invariant`- تأیید رسمی ساخته شده در
- پشتیبانی Iterator (`for X of Container loop`)
- نشانگر `overriding`
- توابع بیان: `function F(X: Integer) return Integer is (X * 2);`
### Ada 2022 — Parallel & Ghost (2022)
- **`with ghost`**: کد شبح برای تأیید (کامپایل شده در تولید)
- **ساختارهای موازی**: حلقه های `parallel`، بلوک های `parallel`
- بهبود زمان واقعی
- بهبود کانتینر
- اصلاحات جنبه `Iterator`
## تکامل نحو
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

## تکامل ویژگی
```
Ada 83:   Packages, strong typing, tasks, generics, exceptions
Ada 95:   Tagged types (OOP), protected objects, child packages
Ada 2005: Interfaces, anonymous access, containers
Ada 2012: Aspects, contracts (Pre/Post), iterators, expression functions
Ada 2022: Ghost code, parallel constructs, real-time improvements
```

## اصول کلیدی طراحی
```
1. "Reliability first" — designed for safety-critical systems
2. "Strong typing" — catch errors at compile time
3. "Readability" — verbose but clear syntax
4. "Concurrency-safe" — protected objects, rendezvous, parallel
5. "Verifiable" — contracts, aspects, ghost code
6. "No hidden costs" — what you see is what you get (no GC required)
```

## رشد اکوسیستم
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
