---
# Metadata
title: "Ada — Version History & Evolution"
description: "Comprehensive version history and evolution of Ada from Ada 83 to modern Ada."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
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

# اڈا - ورژن کی تاریخ اور ارتقاء
## ٹائم لائن
| ورژن | سال | کلیدی تھیم |
|---------|------|------------|
| ادا 83 | 1983 | **پہلا معیار** (MIL-STD-1815A) — Ada Lovelace کے نام سے منسوب |
| اڈا 87 | 1987 | معمولی نظرثانی (صحیحیت، رسائی کے اصول) |
| ادا 95 | 1995 | **بڑا**: OOP (ٹیگ شدہ اقسام)، محفوظ اشیاء، ٹاسکنگ میں بہتری |
| اڈا 2005 | 2005 | **انٹرفیس**، گمنام رسائی کی اقسام،`for`/`while`لوپ میں بہتری |
| اڈا 2012 | 2012 | ** پہلو پر مبنی پروگرامنگ**، معاہدے (پہلے/ بعد کی شرائط)،`iterator`|
| اڈا 2022 | 2022 | **`with ghost`**، متوازی تعمیرات، حقیقی وقت میں بہتری |
## اہم سنگ میل
### ادا 83 — دی برتھ (1983)
- **1983**: یو ایس ڈپارٹمنٹ آف ڈیفنس ایمبیڈڈ سسٹمز کے لیے ایک زبان کا حکم دیتا ہے۔
- جین اچبیہ CII ہنی ویل بل (فرانس) میں ڈیزائن کی قیادت کر رہے ہیں
- Ada Lovelace کے نام پر رکھا گیا - پہلا کمپیوٹر پروگرامر
- کلیدی خصوصیات: مضبوط ٹائپنگ، پیکجز، کام (کنکرنسی)، جنرک، مستثنیات
- **مقصد**: حفاظت کے اہم نظام — ہوا بازی، دفاع، خلائی
### ایڈا 95 — آبجیکٹ اورینٹڈ ایڈا (1995)
- **پہلی آئی ایس او معیاری OO زبان** (جاوا کو معیاری بنانے سے پہلے)
- ٹیگ شدہ اقسام (کلاسز)، کلاس وسیع اقسام، متحرک ترسیل
- محفوظ اشیاء (محفوظ سمورتی ڈیٹا تک رسائی)
- چائلڈ پیکجز (درجہ بندی لائبریری)
- پراگما پر مبنی ترتیب
### ایڈا 2005 - ریفائنمنٹس (2005)
- انٹرفیس (انٹرفیس کی ایک سے زیادہ وراثت)
- گمنام رسائی کی اقسام (آسان پوائنٹرز)
-`for`لوپ میں بہتری
- کنٹینر لائبریریاں (دوہری منسلک فہرستیں، ویکٹر، نقشے)
- توسیع شدہ`return`بیان
### Ada 2012 — معاہدے اور پہلو (2012)
- ** پہلو پر مبنی پروگرامنگ**: اعلانات کے ساتھ منسلک`aspect`شقیں
- **معاہدے**: `Pre`, `Post`,`Type_Invariant`— باضابطہ توثیق شامل ہے
- Iterator سپورٹ (`for X of Container loop`)
-`overriding`اشارے
- اظہار کے افعال: `function F(X: Integer) return Integer is (X * 2);`
### Ada 2022 — Parallel & Ghost (2022)
- **`with ghost`**: تصدیق کے لیے گھوسٹ کوڈ (پروڈکشن میں مرتب کیا گیا)
- **متوازی تعمیرات**:`parallel`لوپس،`parallel`بلاکس
- اصل وقت میں بہتری
- کنٹینر میں بہتری
-`Iterator`پہلوؤں کی اصلاح
## نحوی ارتقاء
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

## فیچر ارتقاء
```
Ada 83:   Packages, strong typing, tasks, generics, exceptions
Ada 95:   Tagged types (OOP), protected objects, child packages
Ada 2005: Interfaces, anonymous access, containers
Ada 2012: Aspects, contracts (Pre/Post), iterators, expression functions
Ada 2022: Ghost code, parallel constructs, real-time improvements
```

## ڈیزائن کے کلیدی اصول
```
1. "Reliability first" — designed for safety-critical systems
2. "Strong typing" — catch errors at compile time
3. "Readability" — verbose but clear syntax
4. "Concurrency-safe" — protected objects, rendezvous, parallel
5. "Verifiable" — contracts, aspects, ghost code
6. "No hidden costs" — what you see is what you get (no GC required)
```

## ماحولیاتی نظام کی نمو
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
