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
# Haskell — Version History & Evolution

## Timeline

| Version | Year | Key Theme |
|---------|------|-----------|
| Haskell 1.0 | 1990 | Initial release (committee effort) |
| Haskell 1.2 | 1992 | Object system experiments |
| Haskell 1.3 | 1996 | Type classes introduced |
| Haskell 1.4 | 1997 | `IO` monad clarified |
| Haskell 98  | 1998 | **First stable standard** |
| Haskell 2010 | 2010 | **Revised standard**, Cabal, modules |
| GHC 7.0  | 2011 | Type families, data kinds |
| GHC 7.4  | 2012 | Applicative-Monad proposal begins |
| GHC 7.6  | 2013 | Type families improvements |
| GHC 7.8  | 2014 | Pattern synonyms, `NegativeLiterals` |
| GHC 7.10 | 2015 | **Applicative-Monad Proposal (AMP)**, `-XStrict` |
| GHC 8.0  | 2016 | **TypeApplications**, `MonadFail`, custom type errors |
| GHC 8.2  | 2017 | Unboxed sums, backpack (module system) |
| GHC 8.4  | 2018 | Abstract base path, `Semigroup` >> `Monoid` |
| GHC 8.6  | 2018 | StarIsType, `DerivingVia` |
| GHC 8.8  | 2019 | MonadFail in Prelude |
| GHC 8.10 | 2020 | Unified `do` notation, kind polymorphism |
| GHC 9.0  | 2021 | **Levity polymorphism**, linear types |
| GHC 9.2  | 2022 | Qualified `do`, improved error messages |
| GHC 9.4  | 2022 | **GHC2021** language extension set, `OverloadedRecordDot` |
| GHC 9.6  | 2023 | Required type arguments, `TypeAbstractions` |
| GHC 9.8  | 2024 | `TypeAbstractions` stable, improved error messages |
| GHC 9.10 | 2024 | Further refinements, performance |
| GHC 9.12 | 2025 | Ongoing development |

## Major Milestones

### Haskell 1.x — The Committee Years (1990–1998)
- **1990**: Haskell 1.0 — committee-designed lazy functional language
- **1.3 (1996)**: Type classes — the defining feature of Haskell
- **1.4 (1997)**: `IO` monad clarified — how to handle side effects purely
- **Haskell 98**: First stable standard; still referenced today

### Haskell 2010 — The Modern Standard
- **2010**: Revised standard — Cabal (package system), module system improvements
- GHC becomes the de facto compiler
- Cabal + Hackage = Haskell's package ecosystem

### GHC 7.x — Type System Power (2011–2015)
- Type families, data kinds, kind polymorphism
- Applicative-Monad Proposal (AMP) — fixing the type class hierarchy
- Pattern synonyms, `Strict` extension

### GHC 8.x — Modern Haskell (2016–2020)
- `TypeApplications` — explicit type arguments at call sites
- Custom type errors — better compiler messages
- Backpack — module system for component-based design
- `DerivingVia` — flexible deriving strategies

### GHC 9.x — Usability Revolution (2021–present)
- **9.0**: Levity polymorphism, linear types (resource safety)
- **9.2**: Qualified `do`, improved error messages
- **9.4**: **GHC2021** — modern default extensions; `OverloadedRecordDot` (field access with `.`)
- **9.6**: Required type arguments, `TypeAbstractions`
- **9.8–9.12**: Continued error message improvements, performance

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

## Type System Evolution

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

## Concurrency & Parallelism

```
Haskell 98:  No standard concurrency model
2004: GHC 6.2 — Software Transactional Memory (STM)
2007: GHC 6.8 — lightweight threads (green threads)
2011: async library — structured concurrency
2018: io-streams, conduit — streaming I/O
2021: Linear types — resource-safe concurrency
2025: GHC + effect systems (Effectful, UnliftIO)
```

## Key Design Principles

```
1. "Lazy by default" — non-strict evaluation
2. "Pure by default" — side effects explicit via monads
3. "Types are truth" — strong static typing
4. "Referential transparency" — same input → same output
5. "Composability" — small building blocks, compose freely
6. "Make illegal states unrepresentable" — type system as design tool
```

## Ecosystem Growth

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
