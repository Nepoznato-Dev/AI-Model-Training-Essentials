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
# Haskell: cronologia ed evoluzione delle versioni
## Cronologia
| Versione | Anno | Tema chiave |
|---------|------|-----------|
| Haskell 1.0 | 1990 | Versione iniziale (impegno del comitato) |
| Haskell1.2 | 1992 | Esperimenti sul sistema di oggetti |
| Haskell 1.3 | 1996 | Classi di tipo introdotte |
| Haskell1.4 | 1997 | `IO`monade chiarita |
| Haskell98 | 1998 | **Primo standard stabile** |
| Haskell 2010 | 2010| **Standard rivisto**, Cabal, moduli |
| GHC7.0 | 2011 | Famiglie di tipi, tipi di dati |
| GHC7.4 | 2012| Inizia la proposta della Monade Applicativa |
| GHC7.6 | 2013| Miglioramenti delle famiglie di tipo |
| GHC7.8 | 2014| Sinonimi del modello,`NegativeLiterals`|
| GHC7.10 | 2015| **Proposta di monade applicativa (AMP)**,`-XStrict`|
| GHC8.0 | 2016| **TypeApplications**,`MonadFail`, errori di tipo personalizzato |
| GHC8.2 | 2017 | Somme senza scatola, zaino (sistema modulare) |
| GHC8.4 | 2018 | Percorso base astratto,`Semigroup`>>`Monoid`|
| GHC8.6 | 2018 | StarIsType,`DerivingVia`|
| GHC8.8 | 2019 | MonadFail nel Preludio |
| GHC 8.10 | 2020 | Notazione`do`unificata, polimorfismo gentile |
| GHC9.0 | 2021 | **Polimorfismo di levità**, tipi lineari |
| GHC9.2 | 2022 |`do`qualificato, messaggi di errore migliorati |
| GHC9.4 | 2022 | **GHC2021** set di estensioni linguistiche,`OverloadedRecordDot`|
| GHC9.6 | 2023 | Argomenti di tipo obbligatori,`TypeAbstractions`|
| GHC9.8 | 2024 | `TypeAbstractions`messaggi di errore stabili e migliorati |
| GHC 9.10 | 2024 | Ulteriori perfezionamenti, prestazioni |
| GHC 9.12 | 2025 | Sviluppo continuo |
## Traguardi importanti
### Haskell 1.x - Gli anni del Comitato (1990-1998)
- **1990**: Haskell 1.0: linguaggio funzionale pigro progettato dal comitato
- **1.3 (1996)**: classi di tipi: la caratteristica distintiva di Haskell
- **1.4 (1997)**:`IO`monad chiarito: come gestire esclusivamente gli effetti collaterali
- **Haskell 98**: Primo standard stabile; referenziato ancora oggi
### Haskell 2010: lo standard moderno
- **2010**: standard rivisto - Cabal (sistema di pacchetti), miglioramenti al sistema dei moduli
- GHC diventa il compilatore de facto
- Cabal + Hackage = ecosistema di pacchetti Haskell
### GHC 7.x: tipo di alimentazione del sistema (2011–2015)
- Famiglie di tipi, tipi di dati, polimorfismo di tipi
- Proposta Applicative-Monad (AMP): fissa la gerarchia delle classi di tipo
- Sinonimi del modello, estensione `Strict`
### GHC 8.x — Haskell moderno (2016-2020)
- `TypeApplications`: argomenti di tipo esplicito nei siti di chiamata
- Errori di tipo personalizzato: messaggi del compilatore migliori
- Zaino: sistema modulare per la progettazione basata su componenti
- `DerivingVia`: strategie di derivazione flessibili
### GHC 9.x — Rivoluzione dell'usabilità (2021-oggi)
- **9.0**: Polimorfismo di levità, tipi lineari (sicurezza delle risorse)
- **9.2**:`do`qualificato, messaggi di errore migliorati
- **9.4**: **GHC2021**: estensioni predefinite moderne; `OverloadedRecordDot`(accesso al campo con`.`)
- **9.6**: argomenti di tipo richiesti,`TypeAbstractions`
- **9.8–9.12**: miglioramenti continui dei messaggi di errore e delle prestazioni
## Evoluzione della sintassi
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

## Digitare Evoluzione del sistema
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

## Concorrenza e parallelismo
```
Haskell 98:  No standard concurrency model
2004: GHC 6.2 — Software Transactional Memory (STM)
2007: GHC 6.8 — lightweight threads (green threads)
2011: async library — structured concurrency
2018: io-streams, conduit — streaming I/O
2021: Linear types — resource-safe concurrency
2025: GHC + effect systems (Effectful, UnliftIO)
```

## Principi chiave di progettazione
```
1. "Lazy by default" — non-strict evaluation
2. "Pure by default" — side effects explicit via monads
3. "Types are truth" — strong static typing
4. "Referential transparency" — same input → same output
5. "Composability" — small building blocks, compose freely
6. "Make illegal states unrepresentable" — type system as design tool
```

## Crescita dell'ecosistema
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
