---
# Metadata
title: "Haskell — Version History & Evolution"
description: "Comprehensive version history and evolution of Haskell from Haskell 1.0 to modern Haskell."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
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

# ہاسکل - ورژن کی تاریخ اور ارتقاء
## ٹائم لائن
| ورژن | سال | کلیدی تھیم |
|---------|------|------------|
| ہاسکل 1.0 | 1990 | ابتدائی ریلیز (کمیٹی کی کوشش) |
| ہاسکل 1.2 | 1992 | آبجیکٹ سسٹم کے تجربات |
| ہاسکل 1.3 | 1996 | قسم کی کلاسیں متعارف کرائی گئیں |
| ہاسکل 1.4 | 1997 | `IO`monad واضح |
| ہاسکل 98 | 1998 | **پہلا مستحکم معیار** |
| ہاسکل 2010 | 2010 | **نظرثانی شدہ معیار**، کیبل، ماڈیولز |
| GHC 7.0 | 2011 | خاندانوں کی قسم، ڈیٹا کی قسمیں |
| GHC 7.4 | 2012 | Applicative-Monad تجویز شروع ہوتی ہے |
| GHC 7.6 | 2013 | خاندانوں میں بہتری کی قسم |
| GHC 7.8 | 2014 | پیٹرن کے مترادفات،`NegativeLiterals`|
| GHC 7.10 | 2015 | **Applicative-Monad Proposal (AMP)**,`-XStrict`|
| GHC 8.0 | 2016 | **TypeApplications**,`MonadFail`, اپنی مرضی کی قسم کی غلطیاں |
| GHC 8.2 | 2017 | ان باکس شدہ رقم، بیگ (ماڈیول سسٹم) |
| GHC 8.4 | 2018 | خلاصہ بنیادی راستہ،`Semigroup`>>`Monoid`|
| GHC 8.6 | 2018 | StarIsType,`DerivingVia`|
| GHC 8.8 | 2019 | Prelude میں MonadFail |
| GHC 8.10 | 2020 | یونیفائیڈ`do`نوٹیشن، قسم کی پولیمورفزم |
| GHC 9.0 | 2021 | **لیویٹی پولیمورفزم**، لکیری اقسام |
| GHC 9.2 | 2022 | اہل `do`، بہتر خرابی کے پیغامات |
| GHC 9.4 | 2022 | **GHC2021** زبان کی توسیع سیٹ،`OverloadedRecordDot`|
| GHC 9.6 | 2023 | مطلوبہ قسم کے دلائل،`TypeAbstractions`|
| GHC 9.8 | 2024 | `TypeAbstractions`مستحکم، بہتر خرابی کے پیغامات |
| GHC 9.10 | 2024 | مزید تطہیر، کارکردگی |
| GHC 9.12 | 2025 | جاری ترقی |
## اہم سنگ میل
### ہاسکل 1.x - کمیٹی کے سال (1990-1998)
- **1990**: ہاسکل 1.0 - کمیٹی کی طرف سے ڈیزائن کردہ سست فنکشنل زبان
- **1.3 (1996)**: ٹائپ کلاسز - ہاسکل کی وضاحتی خصوصیت
- **1.4 (1997)**:`IO`monad کی وضاحت کی گئی — ضمنی اثرات کو خالصتاً ہینڈل کرنے کا طریقہ
- **ہاسکیل 98**: پہلا مستحکم معیار؛ آج بھی حوالہ دیا جاتا ہے۔
### ہاسکل 2010 - جدید معیار
- **2010**: نظر ثانی شدہ معیار - کیبل (پیکیج سسٹم)، ماڈیول سسٹم میں بہتری
- جی ایچ سی ڈی فیکٹو کمپائلر بن جاتا ہے۔
- کیبل + ہیکیج = ہاسکل کا پیکیج ماحولیاتی نظام
### GHC 7.x — ٹائپ سسٹم پاور (2011–2015)
- قسم کے خاندان، ڈیٹا کی قسمیں، قسم کی پولیمورفزم
- Applicative-Monad Proposal (AMP) - قسم کی درجہ بندی کو درست کرنا
- پیٹرن کے مترادفات،`Strict`توسیع
### GHC 8.x — Modern Haskell (2016–2020)
-`TypeApplications`— کال سائٹس پر واضح قسم کے دلائل
- حسب ضرورت قسم کی غلطیاں - بہتر مرتب کرنے والے پیغامات
- بیگ - اجزاء پر مبنی ڈیزائن کے لیے ماڈیول سسٹم
-`DerivingVia`- لچکدار اخذ کرنے کی حکمت عملی
### GHC 9.x — قابل استعمال انقلاب (2021–موجودہ)
- **9.0**: لیویٹی پولیمورفزم، لکیری اقسام (وسائل کی حفاظت)
- **9.2**: اہل `do`، بہتر خرابی کے پیغامات
- **9.4**: **GHC2021** — جدید ڈیفالٹ ایکسٹینشنز؛ `OverloadedRecordDot`(`.` کے ساتھ فیلڈ تک رسائی)
- **9.6**: مطلوبہ قسم کے دلائل،`TypeAbstractions`
- **9.8–9.12**: خرابی کے پیغام میں مسلسل بہتری، کارکردگی
## نحوی ارتقاء
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

## ٹائپ سسٹم ارتقاء
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

## ہم آہنگی اور ہم آہنگی
```
Haskell 98:  No standard concurrency model
2004: GHC 6.2 — Software Transactional Memory (STM)
2007: GHC 6.8 — lightweight threads (green threads)
2011: async library — structured concurrency
2018: io-streams, conduit — streaming I/O
2021: Linear types — resource-safe concurrency
2025: GHC + effect systems (Effectful, UnliftIO)
```

## ڈیزائن کے کلیدی اصول
```
1. "Lazy by default" — non-strict evaluation
2. "Pure by default" — side effects explicit via monads
3. "Types are truth" — strong static typing
4. "Referential transparency" — same input → same output
5. "Composability" — small building blocks, compose freely
6. "Make illegal states unrepresentable" — type system as design tool
```

## ماحولیاتی نظام کی نمو
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
