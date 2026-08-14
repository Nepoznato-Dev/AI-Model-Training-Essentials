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

# Ada — تاريخ الإصدار وتطوره
## الجدول الزمني
| النسخة | سنة | الموضوع الرئيسي |
|---------|------|-----------|
| ادا 83 | 1983 | **المعيار الأول** (MIL-STD-1815A) — سمي على اسم آدا لوفلايس |
| ادا 87 | 1987 | مراجعة ثانوية (الدقة، قواعد الوصول) |
| ادا 95 | 1995 | **التخصص**: OOP (الأنواع ذات العلامات)، الكائنات المحمية، تحسينات المهام |
| أدا 2005 | 2005 | **الواجهات**، أنواع الوصول المجهول، تحسينات حلقة`for`/`while`|
| ادا 2012 | 2012 | **برمجة موجهة نحو الجوانب**، العقود (الشروط المسبقة/اللاحقة)،`iterator`|
| ادا 2022 | 2022 | **`with ghost`**، بنيات متوازية، تحسينات في الوقت الحقيقي |
## المعالم الرئيسية
### آدا 83 – الميلاد (1983)
- **1983**: وزارة الدفاع الأمريكية تفرض لغة واحدة للأنظمة المدمجة
- جان إشبيا يقود التصميم في CII Honeywell Bull (فرنسا)
- سُميت على اسم آدا لوفلايس، أول مبرمجة كمبيوتر
- الميزات الرئيسية: الكتابة القوية، والحزم، والمهام (التزامن)، والأدوية العامة، والاستثناءات
- **الهدف**: أنظمة السلامة الحيوية - الطيران والدفاع والفضاء
### Ada 95 — Ada كائنية التوجه (1995)
- **أول لغة OO متوافقة مع معايير ISO** (قبل توحيد لغة Java)
- الأنواع الموسومة (الفئات)، والأنواع على مستوى الفصل، والإرسال الديناميكي
- الكائنات المحمية (الوصول الآمن للبيانات المتزامنة)
- حزم الطفل (المكتبة الهرمية)
- التكوين القائم على براغما
### Ada 2005 — التحسينات (2005)
- واجهات (الميراث المتعدد للواجهة)
- أنواع الوصول المجهول (مؤشرات مبسطة)
- تحسينات حلقة `for`
- مكتبات الحاويات (القوائم المرتبطة بشكل مزدوج والمتجهات والخرائط)
- بيان`return`الموسع
### Ada 2012 — العقود والجوانب (2012)
- **البرمجة الموجهة نحو الجانب**: عبارات`aspect`المرفقة بالإعلانات
- **العقود**:`Pre`,`Post`,`Type_Invariant`— التحقق الرسمي مدمج
- دعم التكرار (`for X of Container loop`)
- مؤشر `overriding`
- وظائف التعبير: `function F(X: Integer) return Integer is (X * 2);`
### Ada 2022 — الموازي والشبح (2022)
- **`with ghost`**: رمز شبح للتحقق (تم تجميعه في الإنتاج)
- **الإنشاءات المتوازية**: حلقات `parallel`، وكتل `parallel`
- تحسينات في الوقت الحقيقي
- تحسينات الحاوية
- تحسينات الجانب `Iterator`
## تطور بناء الجملة
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

## تطور الميزة
```
Ada 83:   Packages, strong typing, tasks, generics, exceptions
Ada 95:   Tagged types (OOP), protected objects, child packages
Ada 2005: Interfaces, anonymous access, containers
Ada 2012: Aspects, contracts (Pre/Post), iterators, expression functions
Ada 2022: Ghost code, parallel constructs, real-time improvements
```

## مبادئ التصميم الرئيسية
```
1. "Reliability first" — designed for safety-critical systems
2. "Strong typing" — catch errors at compile time
3. "Readability" — verbose but clear syntax
4. "Concurrency-safe" — protected objects, rendezvous, parallel
5. "Verifiable" — contracts, aspects, ghost code
6. "No hidden costs" — what you see is what you get (no GC required)
```

## نمو النظام البيئي
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
