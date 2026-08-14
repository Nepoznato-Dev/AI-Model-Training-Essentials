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
# Haskell — Histórico de versões e evolução
## Linha do tempo
| Versão | Ano | Tema principal |
|--------|------|-----------|
| Haskell 1.0 | 1990 | Versão inicial (esforço do comitê) |
| Haskell 1.2 | 1992 | Experimentos de sistemas de objetos |
| Haskell 1.3 | 1996 | Classes de tipo introduzidas |
| Haskell 1.4 | 1997 |  Mônada`IO`esclarecida |
| Haskell 98 | 1998 | **Primeiro padrão estável** |
| Haskell 2010 | 2010 | **Padrão revisado**, Cabal, módulos |
| GHC 7.0 | 2011 | Famílias de tipos, tipos de dados |
| GHC 7.4 | 2012 | Proposta Applicative-Monad começa |
| GHC 7.6 | 2013 | Tipo melhorias de famílias |
| GHC 7.8 | 2014 | Sinônimos de padrão,`NegativeLiterals`|
| GHC 7.10 | 2015 | **Proposta Aplicativa-Mônada (AMP)**,`-XStrict`|
| GHC 8.0 | 2016 | **TypeApplications**,`MonadFail`, erros de tipo personalizado |
| GHC 8.2 | 2017 | Somas fora da caixa, mochila (sistema de módulos) |
| GHC 8.4 | 2018 | Caminho base abstrato,`Semigroup`>>`Monoid`|
| GHC 8.6 | 2018 | StarIsType,`DerivingVia`|
| GHC 8.8 | 2019 | MonadFail no Prelúdio |
| GHC 8.10 | 2020 | Notação`do`unificada, tipo polimorfismo |
| GHC 9.0 | 2021 | **Polimorfismo de leveza**, tipos lineares |
| GHC 9.2 | 2022 |`do`qualificado, mensagens de erro aprimoradas |
| GHC 9.4 | 2022 | **GHC2021** conjunto de extensão de idioma,`OverloadedRecordDot`|
| GHC 9.6 | 2023 | Argumentos de tipo obrigatórios,`TypeAbstractions`|
| GHC 9.8 | 2024 | `TypeAbstractions`estável, mensagens de erro aprimoradas |
| GHC 9.10 | 2024 | Mais refinamentos, desempenho |
| GHC 9.12 | 2025 | Desenvolvimento contínuo |
## Marcos importantes
### Haskell 1.x — Os anos do comitê (1990–1998)
- **1990**: Haskell 1.0 — linguagem funcional preguiçosa projetada pelo comitê
- **1.3 (1996)**: Classes de tipo — o recurso que define Haskell
- **1.4 (1997)**: mônada`IO`esclarecida - como lidar puramente com os efeitos colaterais
- **Haskell 98**: Primeiro padrão estável; ainda referenciado hoje
### Haskell 2010 — O padrão moderno
- **2010**: Padrão revisado — Cabal (sistema de pacotes), melhorias no sistema de módulos
- GHC se torna o compilador de fato
- Cabal + Hackage = ecossistema de pacotes de Haskell
### GHC 7.x – Tipo de alimentação do sistema (2011–2015)
- Famílias de tipos, tipos de dados, polimorfismo de tipos
- Applicative-Monad Proposal (AMP) — corrigindo a hierarquia de classes de tipo
- Sinônimos de padrão, extensão `Strict`
### GHC 8.x — Haskell moderno (2016–2020)
-`TypeApplications`— argumentos de tipo explícitos em sites de chamada
- Erros de tipo personalizado — melhores mensagens do compilador
- Mochila — sistema de módulos para design baseado em componentes
-`DerivingVia`— estratégias de derivação flexíveis
### GHC 9.x — Revolução da Usabilidade (2021–presente)
- **9.0**: Polimorfismo de Levity, tipos lineares (segurança de recursos)
- **9.2**:`do`qualificado, mensagens de erro aprimoradas
- **9.4**: **GHC2021** — extensões padrão modernas; `OverloadedRecordDot`(acesso ao campo com`.`)
- **9.6**: argumentos de tipo obrigatórios,`TypeAbstractions`
- **9.8–9.12**: Melhorias contínuas nas mensagens de erro e desempenho
## Evolução da Sintaxe
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

## Tipo Evolução do Sistema
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

## Simultaneidade e paralelismo
```
Haskell 98:  No standard concurrency model
2004: GHC 6.2 — Software Transactional Memory (STM)
2007: GHC 6.8 — lightweight threads (green threads)
2011: async library — structured concurrency
2018: io-streams, conduit — streaming I/O
2021: Linear types — resource-safe concurrency
2025: GHC + effect systems (Effectful, UnliftIO)
```

## Princípios-chave de design
```
1. "Lazy by default" — non-strict evaluation
2. "Pure by default" — side effects explicit via monads
3. "Types are truth" — strong static typing
4. "Referential transparency" — same input → same output
5. "Composability" — small building blocks, compose freely
6. "Make illegal states unrepresentable" — type system as design tool
```

## Crescimento do Ecossistema
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
