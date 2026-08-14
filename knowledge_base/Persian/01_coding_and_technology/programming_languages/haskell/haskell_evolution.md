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

# Haskell - تاریخچه نسخه و تکامل
## جدول زمانی
| نسخه | سال | تم کلید |
|---------|------|-----------|
| Haskell 1.0 | 1990 | انتشار اولیه (تلاش کمیته) |
| Haskell 1.2 | 1992 | آزمایشات سیستم شی |
| Haskell 1.3 | 1996 | کلاس های تایپ معرفی شدند |
| Haskell 1.4 | 1997 | `IO`موناد روشن شد |
| Haskell 98 | 1998 | **اولین استاندارد پایدار** |
| Haskell 2010 | 2010 | **استاندارد تجدیدنظر شده**، Cabal، ماژول ها |
| GHC 7.0 | 2011 | نوع خانواده، انواع داده |
| GHC 7.4 | 2012 | پیشنهاد Applicative-Monad آغاز شد |
| GHC 7.6 | 2013 | بهبود خانواده های نوع |
| GHC 7.8 | 2014 | مترادف الگو،`NegativeLiterals`|
| GHC 7.10 | 2015 | **پیشنهاد کاربردی-موناد (AMP)**،`-XStrict`|
| GHC 8.0 | 2016 | **TypeApplications**، `MonadFail`، خطاهای نوع سفارشی |
| GHC 8.2 | 2017 | مبالغ جعبه نشده کوله پشتی (سیستم ماژول) |
| GHC 8.4 | 2018 | مسیر پایه انتزاعی،`Semigroup`>>`Monoid`|
| GHC 8.6 | 2018 | StarIsType،`DerivingVia`|
| GHC 8.8 | 2019 | MonadFail در Prelude |
| GHC 8.10 | 2020 | نماد یکپارچه `do`، پلی مورفیسم نوع |
| GHC 9.0 | 2021 | **چند ریختی لِویتی**، انواع خطی |
| GHC 9.2 | 2022 |`do`واجد شرایط، پیام های خطای بهبود یافته |
| GHC 9.4 | 2022 | ** مجموعه پسوند زبان GHC2021**،`OverloadedRecordDot`|
| GHC 9.6 | 2023 | آرگومان های نوع مورد نیاز،`TypeAbstractions`|
| GHC 9.8 | 2024 | `TypeAbstractions`پیام های خطای پایدار، بهبود یافته |
| GHC 9.10 | 2024 | اصلاحات بیشتر، عملکرد |
| GHC 9.12 | 2025 | توسعه در حال انجام |
## نقاط عطف اصلی
### هاسکل 1.x - سالهای کمیته (1990-1998)
- **1990**: Haskell 1.0 - زبان کاربردی تنبل طراحی شده توسط کمیته
- **1.3 (1996)**: کلاس های نوع - ویژگی تعیین کننده Haskell
- **1.4 (1997)**:`IO`موناد روشن شد - نحوه کنترل صرفاً عوارض جانبی
- **Haskell 98**: اولین استاندارد پایدار. هنوز هم امروز به آن اشاره می شود
### هاسکل 2010 - استاندارد مدرن
- **2010**: استاندارد تجدید نظر شده - Cabal (سیستم بسته)، بهبود سیستم ماژول
- GHC تبدیل به کامپایلر واقعی می شود
- کابال + هک = اکوسیستم بسته هاسکل
### GHC 7.x - نوع سیستم قدرت (2011–2015)
- خانواده های نوع، انواع داده ها، چندشکلی نوع
- پیشنهاد کاربردی-موناد (AMP) - رفع سلسله مراتب کلاس نوع
- مترادف های الگو، پسوند `Strict`
### GHC 8.x - مدرن هاسکل (2016–2020)
-`TypeApplications`- آرگومان های نوع صریح در سایت های تماس
- خطاهای نوع سفارشی - پیام های کامپایلر بهتر
- کوله پشتی - سیستم ماژول برای طراحی مبتنی بر کامپوننت
-`DerivingVia`- استراتژی های مشتق انعطاف پذیر
### GHC 9.x — انقلاب قابلیت استفاده (2021–اکنون)
- **9.0**: پلی مورفیسم Levity، انواع خطی (ایمنی منابع)
- **9.2**:`do`واجد شرایط، پیام های خطای بهبود یافته
- **9.4**: **GHC2021** - پسوندهای پیش فرض مدرن؛ `OverloadedRecordDot`(دسترسی به میدان با `.`)
- **9.6**: آرگومان های نوع مورد نیاز،`TypeAbstractions`
- **9.8–9.12**: ادامه بهبود پیام خطا، عملکرد
## تکامل نحو
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

## تایپ سیستم تکامل
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

## همزمانی و موازی
```
Haskell 98:  No standard concurrency model
2004: GHC 6.2 — Software Transactional Memory (STM)
2007: GHC 6.8 — lightweight threads (green threads)
2011: async library — structured concurrency
2018: io-streams, conduit — streaming I/O
2021: Linear types — resource-safe concurrency
2025: GHC + effect systems (Effectful, UnliftIO)
```

## اصول کلیدی طراحی
```
1. "Lazy by default" — non-strict evaluation
2. "Pure by default" — side effects explicit via monads
3. "Types are truth" — strong static typing
4. "Referential transparency" — same input → same output
5. "Composability" — small building blocks, compose freely
6. "Make illegal states unrepresentable" — type system as design tool
```

## رشد اکوسیستم
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
