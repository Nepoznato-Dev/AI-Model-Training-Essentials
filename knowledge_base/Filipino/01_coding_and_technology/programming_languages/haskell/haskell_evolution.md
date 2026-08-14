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
# Haskell — Kasaysayan ng Bersyon at Ebolusyon
## Timeline
| Bersyon | Taon | Pangunahing Tema |
|---------|------|-----------|
| Haskell 1.0 | 1990 | Paunang paglabas (pagsisikap ng komite) |
| Haskell 1.2 | 1992 | Mga eksperimento sa Object system |
| Haskell 1.3 | 1996 | Uri ng mga klase na ipinakilala |
| Haskell 1.4 | 1997 | `IO`monad nilinaw |
| Haskell 98 | 1998 | **Unang matatag na pamantayan** |
| Haskell 2010 | 2010 | **Binagong pamantayan**, Cabal, mga module |
| GHC 7.0 | 2011 | Uri ng mga pamilya, mga uri ng data |
| GHC 7.4 | 2012 | Nagsisimula ang panukalang Applicative-Monad |
| GHC 7.6 | 2013 | Uri ng mga pagpapabuti ng pamilya |
| GHC 7.8 | 2014 | Mga kasingkahulugan ng pattern,`NegativeLiterals`|
| GHC 7.10 | 2015 | **Applicative-Monad Proposal (AMP)**,`-XStrict`|
| GHC 8.0 | 2016 | **TypeApplications**,`MonadFail`, mga custom na error sa uri |
| GHC 8.2 | 2017 | Unboxed sums, backpack (module system) |
| GHC 8.4 | 2018 | Abstract na base path,`Semigroup`>>`Monoid`|
| GHC 8.6 | 2018 | StarIsType,`DerivingVia`|
| GHC 8.8 | 2019 | MonadFail sa Prelude |
| GHC 8.10 | 2020 | Pinag-isang`do`notation, uri polymorphism |
| GHC 9.0 | 2021 | **Levity polymorphism**, mga linear na uri |
| GHC 9.2 | 2022 | Kwalipikadong`do`, pinahusay na mga mensahe ng error |
| GHC 9.4 | 2022 | **GHC2021** hanay ng extension ng wika,`OverloadedRecordDot`|
| GHC 9.6 | 2023 | Mga kinakailangang uri ng argumento,`TypeAbstractions`|
| GHC 9.8 | 2024 | `TypeAbstractions`stable, pinahusay na mga mensahe ng error |
| GHC 9.10 | 2024 | Mga karagdagang pagpipino, pagganap |
| GHC 9.12 | 2025 | Patuloy na pag-unlad |
## Mga Pangunahing Milestone
### Haskell 1.x — The Committee Years (1990–1998)
- **1990**: Haskell 1.0 — tamad na functional na wika na dinisenyo ng komite
- **1.3 (1996)**: Mga uri ng klase — ang tampok na pagtukoy ng Haskell
- **1.4 (1997)**:`IO`monad nilinaw — kung paano haharapin ang mga side effect nang puro
- **Haskell 98**: Unang matatag na pamantayan; tinutukoy pa rin ngayon
### Haskell 2010 — Ang Makabagong Pamantayan
- **2010**: Binagong pamantayan — Cabal (package system), mga pagpapahusay ng module system
- Nagiging de facto compiler ang GHC
- Cabal + Hackage = Ang package ecosystem ng Haskell
### GHC 7.x — Uri ng System Power (2011–2015)
- Uri ng mga pamilya, mga uri ng data, uri polymorphism
- Applicative-Monad Proposal (AMP) — pag-aayos ng uri ng hierarchy ng klase
- Mga kasingkahulugan ng pattern,`Strict`extension
### GHC 8.x — Modern Haskell (2016–2020)
-`TypeApplications`— tahasang uri ng mga argumento sa mga site ng tawag
- Mga error sa custom na uri - mas mahusay na mga mensahe ng compiler
- Backpack — module system para sa component-based na disenyo
-`DerivingVia`— nababaluktot na mga diskarte sa pagkuha
### GHC 9.x — Usability Revolution (2021–kasalukuyan)
- **9.0**: Levity polymorphism, mga linear na uri (kaligtasan ng mapagkukunan)
- **9.2**: Kwalipikadong`do`, pinahusay na mga mensahe ng error
- **9.4**: **GHC2021** — mga modernong default na extension; `OverloadedRecordDot`(access sa field na may`.`)
- **9.6**: Mga kinakailangang uri ng argumento,`TypeAbstractions`
- **9.8–9.12**: Patuloy na pagpapahusay ng mensahe ng error, pagganap
## Syntax Evolution
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

## Uri ng System Evolution
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

## Concurrency at Paralelismo
```
Haskell 98:  No standard concurrency model
2004: GHC 6.2 — Software Transactional Memory (STM)
2007: GHC 6.8 — lightweight threads (green threads)
2011: async library — structured concurrency
2018: io-streams, conduit — streaming I/O
2021: Linear types — resource-safe concurrency
2025: GHC + effect systems (Effectful, UnliftIO)
```

## Pangunahing Prinsipyo ng Disenyo
```
1. "Lazy by default" — non-strict evaluation
2. "Pure by default" — side effects explicit via monads
3. "Types are truth" — strong static typing
4. "Referential transparency" — same input → same output
5. "Composability" — small building blocks, compose freely
6. "Make illegal states unrepresentable" — type system as design tool
```

## Paglago ng Ecosystem
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
