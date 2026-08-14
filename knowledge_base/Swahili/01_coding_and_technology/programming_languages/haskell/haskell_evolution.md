<!--
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

-->
# Haskell - Historia ya Toleo na Mageuzi
## Rekodi ya matukio
| Toleo | Mwaka | Mandhari Muhimu |
|---------|------|-----------|
| Haskell 1.0 | 1990 | Toleo la awali (juhudi za kamati) |
| Haskell 1.2 | 1992 | Majaribio ya mfumo wa kitu |
| Haskell 1.3 | 1996 | Madarasa ya aina yalianzishwa |
| Haskell 1.4 | 1997 | `IO`monad imefafanuliwa |
| Haskell 98 | 1998 | **Kiwango thabiti cha kwanza** |
| Haskell 2010 | 2010 | ** Kiwango kilichorekebishwa **, Cabal, moduli |
| GHC 7.0 | 2011 | Aina za familia, aina za data |
| GHC 7.4 | 2012 | Pendekezo la Uombaji-Monad linaanza |
| GHC 7.6 | 2013 | Chapa maboresho ya familia |
| GHC 7.8 | 2014 | Sawe za muundo,`NegativeLiterals`|
| GHC 7.10 | 2015 | **Pendekezo Linalotumika-Monad (AMP)**,`-XStrict`|
| GHC 8.0 | 2016 | **TypeApplications**,`MonadFail`, hitilafu za aina maalum |
| GHC 8.2 | 2017 | Hesabu zisizo na sanduku, mkoba (mfumo wa moduli) |
| GHC 8.4 | 2018 | Njia ya msingi ya muhtasari,`Semigroup`>>`Monoid`|
| GHC 8.6 | 2018 | StarIsType,`DerivingVia`|
| GHC 8.8 | 2019 | MonadFail katika Dibaji |
| GHC 8.10 | 2020 | Nukuu ya Umoja wa `do`, aina nyingi za upolimishaji |
| GHC 9.0 | 2021 | **Lawi polymorphism**, aina za mstari |
| GHC 9.2 | 2022 |`do`Iliyohitimu, ujumbe wa makosa ulioboreshwa |
| GHC 9.4 | 2022 | **GHC2021** seti ya kiendelezi cha lugha,`OverloadedRecordDot`|
| GHC 9.6 | 2023 | Hoja za aina zinazohitajika,`TypeAbstractions`|
| GHC 9.8 | 2024 | `TypeAbstractions`ujumbe thabiti, ulioboreshwa wa makosa |
| GHC 9.10 | 2024 | Marekebisho zaidi, utendaji |
| GHC 9.12 | 2025 | Maendeleo yanayoendelea |
## Mafanikio Makuu
### Haskell 1.x - Miaka ya Kamati (1990–1998)
- **1990**: Haskell 1.0 - lugha ya kiutendaji iliyoundwa na kamati
- **1.3 (1996)**: Aina za madarasa - kipengele kinachobainisha cha Haskell
- **1.4 (1997)**:`IO`monad imefafanuliwa - jinsi ya kushughulikia madhara
- ** Haskell 98 **: Kiwango cha kwanza cha utulivu; bado inarejelewa leo
### Haskell 2010 — The Modern Standard
- **2010**: Kiwango kilichorekebishwa - Cabal (mfumo wa pakiti), uboreshaji wa mfumo wa moduli
- GHC inakuwa mkusanyaji wa ukweli
- Cabal + Hackage = Mfumo wa ikolojia wa kifurushi cha Haskell
### GHC 7.x — Aina ya Nguvu ya Mfumo (2011–2015)
- Aina za familia, aina za data, aina nyingi za polymorphism
- Applicative-Monad Proposal (AMP) - kurekebisha aina ya daraja la daraja
- Visawe vya muundo, ugani wa `Strict`
### GHC 8.x — Haskell ya Kisasa (2016–2020)
-`TypeApplications`- hoja za aina wazi katika tovuti za simu
- Hitilafu za aina maalum - ujumbe bora wa mkusanyaji
- Mkoba - mfumo wa moduli kwa muundo wa msingi wa sehemu
-`DerivingVia`- mikakati rahisi ya kupata
### GHC 9.x — Mapinduzi ya Utumiaji (2021–sasa)
- **9.0**: Upolimishaji wa Levity, aina za mstari (usalama wa rasilimali)
- **9.2**: Iliyohitimu`do`, ujumbe wa makosa ulioboreshwa
- **9.4**: **GHC2021** - viendelezi vya kisasa vya chaguo-msingi; `OverloadedRecordDot`(ufikiaji wa shamba na `.`)
- **9.6**: Hoja za aina zinazohitajika,`TypeAbstractions`
- **9.8–9.12**: Kuendelea kuboreshwa kwa ujumbe wa hitilafu, utendakazi
## Mageuzi ya Sintaksia
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

## Aina ya Mageuzi ya Mfumo
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

## Concurrency & Usambamba
```
Haskell 98:  No standard concurrency model
2004: GHC 6.2 — Software Transactional Memory (STM)
2007: GHC 6.8 — lightweight threads (green threads)
2011: async library — structured concurrency
2018: io-streams, conduit — streaming I/O
2021: Linear types — resource-safe concurrency
2025: GHC + effect systems (Effectful, UnliftIO)
```

## Kanuni Muhimu za Usanifu
```
1. "Lazy by default" — non-strict evaluation
2. "Pure by default" — side effects explicit via monads
3. "Types are truth" — strong static typing
4. "Referential transparency" — same input → same output
5. "Composability" — small building blocks, compose freely
6. "Make illegal states unrepresentable" — type system as design tool
```

## Ukuaji wa Mfumo ikolojia
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
