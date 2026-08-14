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

# Haskell — historia wersji i ewolucja
## Oś czasu
| Wersja | Rok | Kluczowy motyw |
|--------|------|-----------|
| Haskell 1.0 | 1990 | Pierwsze wydanie (wysiłek komisji) |
| Haskell 1.2 | 1992 | Eksperymenty z systemem obiektowym |
| Haskell 1.3 | 1996 | Wprowadzono klasy typów |
| Haskell 1.4 | 1997 |  Monada`IO`wyjaśniona |
| Haskella 98 | 1998 | **Pierwszy stabilny standard** |
| Haskell 2010 | 2010 | **Zmieniony standard**, Cabal, moduły |
| GHC 7.0 | 2011 | Rodziny typów, rodzaje danych |
| GHC 7.4 | 2012 | Rozpoczyna się propozycja aplikacji-monady |
| GHC 7.6 | 2013 | Wpisz ulepszenia rodzin |
| GHC 7.8 | 2014 | Synonimy wzoru,`NegativeLiterals`|
| GHC 7.10 | 2015 | **Propozycja monady aplikacyjnej (AMP)**,`-XStrict`|
| GHC 8.0 | 2016 | **TypeApplications**, `MonadFail`, błędy typów niestandardowych |
| GHC 8.2 | 2017 | Sumy rozpakowane, plecak (system modułowy) |
| GHC 8.4 | 2018 | Abstrakcyjna ścieżka bazowa,`Semigroup`>>`Monoid`|
| GHC 8.6 | 2018 | StarIsType,`DerivingVia`|
| GHC 8.8 | 2019 | MonadFail w Preludium |
| GHC 8.10 | 2020 | Ujednolicona notacja `do`, rodzaj polimorfizmu |
| GHC 9.0 | 2021 | **Polimorfizm lekkości**, typy liniowe |
| GHC 9.2 | 2022 | Kwalifikowany `do`, ulepszone komunikaty o błędach |
| GHC 9.4 | 2022 | **GHC2021** zestaw rozszerzeń językowych,`OverloadedRecordDot`|
| GHC 9.6 | 2023 | Wymagane argumenty typu,`TypeAbstractions`|
| GHC 9.8 | 2024 | `TypeAbstractions`stabilne, ulepszone komunikaty o błędach |
| GHC 9.10 | 2024 | Dalsze udoskonalenia, wydajność |
| GHC 9.12 | 2025 | Ciągły rozwój |
## Główne kamienie milowe
### Haskell 1.x — Lata Komitetu (1990–1998)
- **1990**: Haskell 1.0 — zaprojektowany przez komisję leniwy język funkcjonalny
- **1.3 (1996)**: Klasy typów — cecha definiująca Haskell
- **1.4 (1997)**: Wyjaśniono monadę`IO`— jak radzić sobie wyłącznie z efektami ubocznymi
- **Haskell 98**: Pierwszy stabilny standard; wspomina się do dziś
### Haskell 2010 — nowoczesny standard
- **2010**: Zmieniony standard — Cabal (system pakietowy), ulepszenia systemu modułowego
- GHC staje się de facto kompilatorem
- Cabal + Hackage = ekosystem pakietów Haskell
### GHC 7.x — typ Moc systemu (2011–2015)
- Rodziny typów, rodzaje danych, rodzaj polimorfizmu
- Applicative-Monad Proposal (AMP) — naprawianie hierarchii klas typów
- Synonimy wzorca, rozszerzenie `Strict`
### GHC 8.x — nowoczesny Haskell (2016–2020)
-`TypeApplications`— argumenty typu jawnego w witrynach wywołań
- Błędy typów niestandardowych — lepsze komunikaty kompilatora
- Plecak — system modułowy do projektowania opartego na komponentach
-`DerivingVia`— elastyczne strategie wyprowadzania
### GHC 9.x — rewolucja w zakresie użyteczności (2021–obecnie)
- **9.0**: Polimorfizm Levity’ego, typy liniowe (bezpieczeństwo zasobów)
- **9.2**: Kwalifikowano `do`, ulepszone komunikaty o błędach
- **9.4**: **GHC2021** — nowoczesne rozszerzenia domyślne; `OverloadedRecordDot`(dostęp do pola za pomocą`.`)
- **9.6**: Wymagane argumenty typu,`TypeAbstractions`
- **9,8–9,12**: Ciągłe ulepszanie komunikatów o błędach i wydajności
## Ewolucja składni
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

## Wpisz ewolucję systemu
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

## Współbieżność i równoległość
```
Haskell 98:  No standard concurrency model
2004: GHC 6.2 — Software Transactional Memory (STM)
2007: GHC 6.8 — lightweight threads (green threads)
2011: async library — structured concurrency
2018: io-streams, conduit — streaming I/O
2021: Linear types — resource-safe concurrency
2025: GHC + effect systems (Effectful, UnliftIO)
```

## Kluczowe zasady projektowania
```
1. "Lazy by default" — non-strict evaluation
2. "Pure by default" — side effects explicit via monads
3. "Types are truth" — strong static typing
4. "Referential transparency" — same input → same output
5. "Composability" — small building blocks, compose freely
6. "Make illegal states unrepresentable" — type system as design tool
```

## Rozwój ekosystemu
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
