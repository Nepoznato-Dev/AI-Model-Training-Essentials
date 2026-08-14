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

# হাসকেল — সংস্করণ ইতিহাস এবং বিবর্তন
## টাইমলাইন
| সংস্করণ | বছর | মূল থিম |
|---------|------|------------|
| হাসকেল 1.0 | 1990 | প্রাথমিক প্রকাশ (কমিটির প্রচেষ্টা) |
| হাসকেল 1.2 | 1992 | অবজেক্ট সিস্টেম পরীক্ষা |
| হাসকেল 1.3 | 1996 | টাইপ ক্লাস চালু |
| হাসকেল 1.4 | 1997 | `IO`মোনাড স্পষ্টীকৃত |
| হাসকেল 98 | 1998 | **প্রথম স্থিতিশীল মান** |
| হাসকেল 2010 | 2010 | **সংশোধিত মান**, ক্যাবল, মডিউল |
| GHC 7.0 | 2011 | টাইপ পরিবার, তথ্য প্রকার |
| GHC 7.4 | 2012 | প্রযোজ্য-মোনাদ প্রস্তাব শুরু হয় |
| জিএইচসি 7.6 | 2013 | পরিবারের উন্নতির ধরন |
| GHC 7.8 | 2014 | প্যাটার্ন প্রতিশব্দ,`NegativeLiterals`|
| GHC 7.10 | 2015 | **প্রয়োগমূলক-মোনাড প্রস্তাব (AMP)**,`-XStrict`|
| GHC 8.0 | 2016 | **TypeApplications**,`MonadFail`, কাস্টম টাইপ ত্রুটি |
| জিএইচসি 8.2 | 2017 | আনবক্সড সমষ্টি, ব্যাকপ্যাক (মডিউল সিস্টেম) |
| জিএইচসি 8.4 | 2018 | বিমূর্ত ভিত্তি পথ,`Semigroup`>>`Monoid`|
| জিএইচসি 8.6 | 2018 | StarIsType,`DerivingVia`|
| জিএইচসি 8.8 | 2019 | প্রিলিউডে মোনাডফেইল |
| GHC 8.10 | 2020 | ইউনিফাইড`do`স্বরলিপি, ধরনের পলিমারফিজম |
| GHC 9.0 | 2021 | **লেভিটি পলিমারফিজম**, লিনিয়ার প্রকার |
| জিএইচসি 9.2 | 2022 | যোগ্য`do`, উন্নত ত্রুটি বার্তা |
| জিএইচসি 9.4 | 2022 | **GHC2021** ভাষা এক্সটেনশন সেট,`OverloadedRecordDot`|
| জিএইচসি 9.6 | 2023 | প্রয়োজনীয় ধরনের আর্গুমেন্ট,`TypeAbstractions`|
| জিএইচসি 9.8 | 2024 | `TypeAbstractions`স্থিতিশীল, উন্নত ত্রুটি বার্তা |
| জিএইচসি 9.10 | 2024 | আরও পরিমার্জন, কর্মক্ষমতা |
| জিএইচসি 9.12 | 2025 | চলমান উন্নয়ন |
## প্রধান মাইলফলক
### Haskell 1.x — কমিটির বছর (1990-1998)
- **1990**: হাসকেল 1.0 — কমিটি-পরিকল্পিত অলস কার্যকরী ভাষা
- **1.3 (1996): টাইপ ক্লাস - হাসকেলের সংজ্ঞায়িত বৈশিষ্ট্য
- **1.4 (1997)**:`IO`মোনাড স্পষ্ট করা হয়েছে — কীভাবে বিশুদ্ধভাবে পার্শ্বপ্রতিক্রিয়াগুলি পরিচালনা করা যায়
- **হাস্কেল 98**: প্রথম স্থিতিশীল মান; আজও উল্লেখ করা হয়েছে
### হাসকেল 2010 — আধুনিক স্ট্যান্ডার্ড
- **2010**: সংশোধিত মান — ক্যাবল (প্যাকেজ সিস্টেম), মডিউল সিস্টেমের উন্নতি
- জিএইচসি ডি ফ্যাক্টো কম্পাইলার হয়ে যায়
- ক্যাবল + হ্যাকেজ = হাসকেলের প্যাকেজ ইকোসিস্টেম
### GHC 7.x — টাইপ সিস্টেম পাওয়ার (2011–2015)
- টাইপ ফ্যামিলি, ডাটা ধরনের, ধরনের পলিমারফিজম
- অ্যাপ্লিকেটিভ-মোনাড প্রপোজাল (এএমপি) — টাইপ ক্লাস হায়ারার্কি ঠিক করা
- প্যাটার্ন প্রতিশব্দ,`Strict`এক্সটেনশন
### GHC 8.x — আধুনিক হাসকেল (2016-2020)
-`TypeApplications`— কল সাইটগুলিতে স্পষ্ট ধরনের আর্গুমেন্ট
- কাস্টম টাইপ ত্রুটি - ভাল কম্পাইলার বার্তা
- ব্যাকপ্যাক - উপাদান-ভিত্তিক ডিজাইনের জন্য মডিউল সিস্টেম
-`DerivingVia`- নমনীয় আহরণ কৌশল
### GHC 9.x — ব্যবহারযোগ্যতার বিপ্লব (2021-বর্তমান)
- **9.0**: লেভিটি পলিমারফিজম, লিনিয়ার প্রকার (রিসোর্স সেফটি)
- **9.2**: যোগ্য `do`, উন্নত ত্রুটি বার্তা
- **9.4**: **GHC2021** — আধুনিক ডিফল্ট এক্সটেনশন; `OverloadedRecordDot`(`.` সহ ক্ষেত্রের অ্যাক্সেস)
- **9.6**: প্রয়োজনীয় টাইপ আর্গুমেন্ট,`TypeAbstractions`
- **9.8–9.12**: ক্রমাগত ত্রুটি বার্তা উন্নতি, কর্মক্ষমতা
## সিনট্যাক্স বিবর্তন
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

## টাইপ সিস্টেম বিবর্তন
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

## সামঞ্জস্য এবং সমান্তরালতা
```
Haskell 98:  No standard concurrency model
2004: GHC 6.2 — Software Transactional Memory (STM)
2007: GHC 6.8 — lightweight threads (green threads)
2011: async library — structured concurrency
2018: io-streams, conduit — streaming I/O
2021: Linear types — resource-safe concurrency
2025: GHC + effect systems (Effectful, UnliftIO)
```

## মূল ডিজাইনের নীতি
```
1. "Lazy by default" — non-strict evaluation
2. "Pure by default" — side effects explicit via monads
3. "Types are truth" — strong static typing
4. "Referential transparency" — same input → same output
5. "Composability" — small building blocks, compose freely
6. "Make illegal states unrepresentable" — type system as design tool
```

## ইকোসিস্টেম বৃদ্ধি
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
