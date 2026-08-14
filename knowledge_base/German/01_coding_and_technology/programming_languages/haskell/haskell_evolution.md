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

# Haskell – Versionsgeschichte und Entwicklung
## Zeitleiste
| Version | Jahr | Schlüsselthema |
|---------|------|-----------|
| Haskell 1.0 | 1990 | Erstveröffentlichung (Komiteearbeit) |
| Haskell 1.2 | 1992 | Objektsystemexperimente |
| Haskell 1.3 | 1996 | Typklassen eingeführt |
| Haskell 1.4 | 1997 | `IO`Monade geklärt |
| Haskell 98 | 1998 | **Erster stabiler Standard** |
| Haskell 2010 | 2010 | **Überarbeiteter Standard**, Cabal, Module |
| GHC 7.0 | 2011 | Typfamilien, Datenarten |
| GHC 7,4 | 2012 | Applicative-Monad-Vorschlag beginnt |
| GHC 7,6 | 2013 | Verbesserungen bei Typfamilien |
| GHC 7,8 | 2014 | Mustersynonyme,`NegativeLiterals`|
| GHC 7.10 | 2015 | **Applicative-Monad Proposal (AMP)**,`-XStrict`|
| GHC 8.0 | 2016 | **TypeApplications**,`MonadFail`, benutzerdefinierte Typfehler |
| GHC 8.2 | 2017 | Unverpackte Summen, Rucksack (Modulsystem) |
| GHC 8.4 | 2018 | Abstrakter Basispfad,`Semigroup`>>`Monoid`|
| GHC 8,6 | 2018 | StarIsType,`DerivingVia`|
| GHC 8,8 | 2019 | MonadFail im Präludium |
| GHC 8.10 | 2020 | Einheitliche `do`-Notation, Art-Polymorphismus |
| GHC 9.0 | 2021 | **Levity-Polymorphismus**, lineare Typen |
| GHC 9.2 | 2022 | Qualifiziertes `do`, verbesserte Fehlermeldungen |
| GHC 9,4 | 2022 | **GHC2021** Spracherweiterungssatz,`OverloadedRecordDot`|
| GHC 9,6 | 2023 | Erforderliche Typargumente,`TypeAbstractions`|
| GHC 9,8 | 2024 | `TypeAbstractions`stabil, verbesserte Fehlermeldungen |
| GHC 9.10 | 2024 | Weitere Verfeinerungen, Leistung |
| GHC 9.12 | 2025 | Kontinuierliche Entwicklung |
## Wichtige Meilensteine
### Haskell 1.x – Die Ausschussjahre (1990–1998)
- **1990**: Haskell 1.0 – vom Ausschuss entworfene, träge funktionale Sprache
- **1.3 (1996)**: Typklassen – das bestimmende Merkmal von Haskell
- **1.4 (1997)**:`IO`Monade klargestellt – wie man mit Nebenwirkungen umgeht
- **Haskell 98**: Erster stabiler Standard; wird auch heute noch erwähnt
### Haskell 2010 – Der moderne Standard
- **2010**: Überarbeiteter Standard – Cabal (Paketsystem), Modulsystemverbesserungen
- GHC wird zum De-facto-Compiler
- Cabal + Hackage = Haskells Paket-Ökosystem
### GHC 7.x – Typ Systemleistung (2011–2015)
- Typfamilien, Datenarten, Artpolymorphismus
- Applicative-Monad Proposal (AMP) – Festlegung der Typklassenhierarchie
- Mustersynonyme, `Strict`-Erweiterung
### GHC 8.x – Modernes Haskell (2016–2020)
-`TypeApplications`– explizite Typargumente an Aufrufseiten
- Benutzerdefinierte Typfehler – bessere Compiler-Meldungen
- Rucksack – Modulsystem für komponentenbasiertes Design
-`DerivingVia`– flexible Ableitungsstrategien
### GHC 9.x – Usability-Revolution (2021–heute)
- **9.0**: Levity-Polymorphismus, lineare Typen (Ressourcensicherheit)
- **9.2**: Qualifizierter`do`, verbesserte Fehlermeldungen
- **9.4**: **GHC2021** – moderne Standarderweiterungen; `OverloadedRecordDot`(Feldzugriff mit`.`)
- **9.6**: Erforderliche Typargumente,`TypeAbstractions`
- **9.8–9.12**: Weitere Verbesserungen bei Fehlermeldungen und Leistung
## Syntaxentwicklung
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

## Typsystementwicklung
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

## Parallelität und Parallelität
```
Haskell 98:  No standard concurrency model
2004: GHC 6.2 — Software Transactional Memory (STM)
2007: GHC 6.8 — lightweight threads (green threads)
2011: async library — structured concurrency
2018: io-streams, conduit — streaming I/O
2021: Linear types — resource-safe concurrency
2025: GHC + effect systems (Effectful, UnliftIO)
```

## Wichtige Designprinzipien
```
1. "Lazy by default" — non-strict evaluation
2. "Pure by default" — side effects explicit via monads
3. "Types are truth" — strong static typing
4. "Referential transparency" — same input → same output
5. "Composability" — small building blocks, compose freely
6. "Make illegal states unrepresentable" — type system as design tool
```

## Ökosystemwachstum
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
