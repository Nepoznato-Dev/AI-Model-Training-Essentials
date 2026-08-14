---
# Metadata
title: "Haskell — Version History & Evolution"
description: "Comprehensive version history and evolution of Haskell from Haskell 1.0 to modern Haskell."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial version history"
tags: [haskell, version-history, evolution, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "10 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---
# هاسكل — تاريخ الإصدار وتطوره
## الجدول الزمني
| النسخة | سنة | الموضوع الرئيسي |
|---------|------|-----------|
| هاسكل 1.0 | 1990 | الإصدار الأولي (مجهود اللجنة) |
| هاسكل 1.2 | 1992 | تجارب نظام الكائنات |
| هاسكل 1.3 | 1996 | فئات النوع المقدمة |
| هاسكل 1.4 | 1997 |  وأوضح`IO`موناد |
| هاسكل 98 | 1998 | **المعيار المستقر الأول** |
| هاسكل 2010 | 2010 | **المعيار المنقح**، كابال، الوحدات |
| جي اتش سي 7.0 | 2011 | اكتب العائلات وأنواع البيانات |
| جي اتش سي 7.4 | 2012 | يبدأ اقتراح موناد التطبيقي |
| جي اتش سي 7.6 | 2013 | اكتب تحسينات العائلات |
| جي اتش سي 7.8 | 2014 | مرادفات النمط،`NegativeLiterals`|
| جي اتش سي 7.10 | 2015 | **اقتراح موناد التطبيقي (AMP)**،`-XStrict`|
| جي اتش سي 8.0 | 2016 | **TypeApplications**، `MonadFail`، أخطاء الكتابة المخصصة |
| جي اتش سي 8.2 | 2017 | مبالغ غير معلبة، حقيبة الظهر (نظام الوحدة) |
| جي اتش سي 8.4 | 2018 | المسار الأساسي المجرد،`Semigroup`>>`Monoid`|
| جي اتش سي 8.6 | 2018 | ستار آيستيب،`DerivingVia`|
| جي اتش سي 8.8 | 2019 | MonadFail في مقدمة |
| جي اتش سي 8.10 | 2020 | تدوين`do`الموحد، تعدد الأشكال النوعي |
| جي اتش سي 9.0 | 2021 | **تعدد أشكال الرفع**، الأنواع الخطية |
| جي اتش سي 9.2 | 2022 |`do`المؤهل، رسائل خطأ محسنة |
| جي اتش سي 9.4 | 2022 | **GHC2021** مجموعة امتدادات اللغة،`OverloadedRecordDot`|
| جي اتش سي 9.6 | 2023 | وسيطات النوع المطلوبة،`TypeAbstractions`|
| جي اتش سي 9.8 | 2024 | `TypeAbstractions`رسائل خطأ مستقرة ومحسنة |
| جي اتش سي 9.10 | 2024 | مزيد من التحسينات والأداء |
| جي اتش سي 9.12 | 2025 | التطوير المستمر |
## المعالم الرئيسية
### هاسكل 1.x — سنوات اللجنة (1990-1998)
- **1990**: هاسكل 1.0 — لغة وظيفية كسولة مصممة من قبل اللجنة
- **1.3 (1996)**: فئات الكتابة — السمة المميزة لهاسكل
- **1.4 (1997)**: توضيح`IO`monad - كيفية التعامل مع الآثار الجانبية تمامًا
- **هاسكل 98**: أول معيار مستقر؛ لا يزال يشار إليه اليوم
### هاسكل 2010 — المعيار الحديث
- **2010**: المعيار المنقح — Cabal (نظام الحزمة)، تحسينات نظام الوحدة
- تصبح GHC المترجم الفعلي
- Cabal + Hackage = النظام البيئي لحزمة هاسكل
### GHC 7.x — نوع طاقة النظام (2011–2015)
- عائلات النوع، أنواع البيانات، تعدد أشكال النوع
- اقتراح موناد التطبيقي (AMP) - إصلاح التسلسل الهرمي لفئة النوع
- مرادفات الأنماط، امتداد `Strict`
### GHC 8.x — هاسكل الحديثة (2016–2020)
-`TypeApplications`- وسيطات الكتابة الصريحة في مواقع الاتصال
- أخطاء في النوع المخصص - رسائل مترجم أفضل
- حقيبة الظهر - نظام وحدة للتصميم القائم على المكونات
-`DerivingVia`— استراتيجيات الاشتقاق المرنة
### GHC 9.x — ثورة سهولة الاستخدام (2021 إلى الوقت الحاضر)
- **9.0**: تعدد الأشكال، الأنواع الخطية (سلامة الموارد)
- **9.2**:`do`المؤهل، تحسين رسائل الخطأ
- **9.4**: **GHC2021** — الامتدادات الافتراضية الحديثة؛ `OverloadedRecordDot`(الوصول الميداني باستخدام `.`)
- **9.6**: وسيطات النوع المطلوبة،`TypeAbstractions`
- **9.8–9.12**: تحسينات مستمرة لرسائل الخطأ والأداء
## تطور بناء الجملة
```haskell
-- Haskell 98: Basic type classes
class Eq a where
  (==) :: a -> a -> Bool

-- GHC extensions: Type applications (GHC 8.0)
-- Before:
read "[1,2,3]" :: [Int]
-- After:
read @[Int] "[1,2,3]"

-- GHC 9.4: OverloadedRecordDot
-- Before:
name (getPerson user)
-- After:
user.person.name

-- GHC 9.0: Linear types
-- Before:
processFile :: FilePath -> IO Result
-- After:
processFile :: FilePath %1 -> IO Result  -- file handle used exactly once

-- GHC 8.0: Custom type errors
type family ErrorMessage (a :: Type) :: ErrorMessage where
  ErrorMessage (NotSerializable a) =
    'Text "Cannot serialize type " ':<>: 'ShowType a
```

## نوع تطور النظام
```
Haskell 1.0:  Basic types, algebraic data types, pattern matching
Haskell 1.3:  Type classes
Haskell 98:   Multi-parameter type classes, functional dependencies
GHC 6.x:     GADTs, type families, rank-N types
GHC 7.0:     Data kinds, kind polymorphism
GHC 7.10:    Applicative-Monad Proposal
GHC 8.0:     TypeApplications, custom type errors
GHC 8.2:     Unboxed sums
GHC 9.0:     Levity polymorphism, linear types
GHC 9.4:     OverloadedRecordDot, GHC2021
GHC 9.6:     Required type arguments, TypeAbstractions
```

## التزامن والتوازي
```
Haskell 98:  No standard concurrency model
2004: GHC 6.2 — Software Transactional Memory (STM)
2007: GHC 6.8 — lightweight threads (green threads)
2011: async library — structured concurrency
2018: io-streams, conduit — streaming I/O
2021: Linear types — resource-safe concurrency
2025: GHC + effect systems (Effectful, UnliftIO)
```

## مبادئ التصميم الرئيسية
```
1. "Lazy by default" — non-strict evaluation
2. "Pure by default" — side effects explicit via monads
3. "Types are truth" — strong static typing
4. "Referential transparency" — same input → same output
5. "Composability" — small building blocks, compose freely
6. "Make illegal states unrepresentable" — type system as design tool
```

## نمو النظام البيئي
```
1990: Haskell 1.0 — academic curiosity
1998: Haskell 98 — stable standard
2007: Cabal + Hackage — package ecosystem
2010: Haskell 2010 — revised standard
2012: Stack build tool — reproducible builds
2015: Haskell in industry — Facebook, Standard Chartered, Well-Typed
2021: GHC 9.0 — levity polymorphism, linear types
2023: GHC 9.6 — type abstractions
2025: Haskell used in finance, compilers, formal verification,
       blockchain (Cardano), and academic research
       GHC, Stack, Cabal; key libraries: lens, aeson, servant, yesod
```
