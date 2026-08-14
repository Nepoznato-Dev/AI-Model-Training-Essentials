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
# Haskell — Historique et évolution des versions
## Chronologie
| Version | Année | Thème clé |
|---------|------|-----------|
| Haskell 1.0 | 1990 | Version initiale (effort du comité) |
| Haskell 1.2 | 1992 | Expériences de systèmes d'objets |
| Haskell 1.3 | 1996 | Classes de types introduites |
| Haskell 1.4 | 1997 |  Monade`IO`clarifiée |
| Haskell 98 | 1998 | **Premier standard stable** |
| Haskell2010 | 2010 | **Norme révisée**, Cabale, modules |
| GHC 7.0 | 2011 | Familles de types, types de données |
| GHC 7.4 | 2012 | La proposition Applicative-Monad commence |
| GHC 7.6 | 2013 | Améliorations des familles de types |
| GHC 7.8 | 2014 | Synonymes de motifs,`NegativeLiterals`|
| GHC 7.10 | 2015 | **Proposition de monade applicative (AMP)**,`-XStrict`|
| GHC 8.0 | 2016 | **TypeApplications**,`MonadFail`, erreurs de type personnalisé |
| GHC 8.2 | 2017 | Sommes non emballées, sac à dos (système de modules) |
| GHC 8.4 | 2018 | Chemin de base abstrait,`Semigroup`>>`Monoid`|
| GHC 8.6 | 2018 | StarIsType,`DerivingVia`|
| GHC 8.8 | 2019 | MonadFail dans le prélude |
| GHC 8.10 | 2020 | Notation unifiée `do`, polymorphisme de type |
| GHC 9.0 | 2021 | **Polymorphisme de légèreté**, types linéaires |
| GHC 9.2 | 2022 |`do`qualifié, messages d'erreur améliorés |
| GHC 9.4 | 2022 | **GHC2021** ensemble d'extensions de langue,`OverloadedRecordDot`|
| GHC 9.6 | 2023 | Arguments de type requis,`TypeAbstractions`|
| GHC 9,8 | 2024 | `TypeAbstractions`stable, messages d'erreur améliorés |
| GHC 9.10 | 2024 | Autres améliorations, performances |
| GHC 9.12 | 2025 | Développement en cours |
## Étapes majeures
### Haskell 1.x — Les années comité (1990-1998)
- **1990** : Haskell 1.0 — langage fonctionnel paresseux conçu par un comité
- **1.3 (1996)** : Classes de types — la caractéristique déterminante de Haskell
- **1.4 (1997)** : clarification de la monade`IO`— comment gérer les effets secondaires de manière pure
- **Haskell 98** : Premier standard stable ; toujours référencé aujourd'hui
### Haskell 2010 — La norme moderne
- **2010** : Norme révisée — Cabal (système de package), améliorations du système de modules
- GHC devient le compilateur de facto
- Cabal + Hackage = l'écosystème de packages de Haskell
### GHC 7.x — Tapez l'alimentation du système (2011-2015)
- Familles de types, types de données, polymorphisme des types
- Proposition Applicative-Monad (AMP) — correction de la hiérarchie des classes de types
- Synonymes de motifs, extension `Strict`
### GHC 8.x — Haskell moderne (2016-2020)
-`TypeApplications`— arguments de type explicites sur les sites d'appel
- Erreurs de type personnalisé - meilleurs messages du compilateur
- Backpack — système de modules pour une conception basée sur des composants
-`DerivingVia`— stratégies de dérivation flexibles
### GHC 9.x — Révolution de la convivialité (2021-présent)
- **9.0** : Polymorphisme de légèreté, types linéaires (sécurité des ressources)
- **9.2** :`do`qualifié, messages d'erreur améliorés
- **9.4** : **GHC2021** — extensions modernes par défaut ; `OverloadedRecordDot`(accès au champ avec`.`)
- **9.6** : arguments de type requis,`TypeAbstractions`
- **9.8–9.12** : améliorations continues des messages d'erreur et des performances
## Évolution de la syntaxe
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

## Évolution du système de types
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

## Concurrence et parallélisme
```
Haskell 98:  No standard concurrency model
2004: GHC 6.2 — Software Transactional Memory (STM)
2007: GHC 6.8 — lightweight threads (green threads)
2011: async library — structured concurrency
2018: io-streams, conduit — streaming I/O
2021: Linear types — resource-safe concurrency
2025: GHC + effect systems (Effectful, UnliftIO)
```

## Principes de conception clés
```
1. "Lazy by default" — non-strict evaluation
2. "Pure by default" — side effects explicit via monads
3. "Types are truth" — strong static typing
4. "Referential transparency" — same input → same output
5. "Composability" — small building blocks, compose freely
6. "Make illegal states unrepresentable" — type system as design tool
```

## Croissance de l'écosystème
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
