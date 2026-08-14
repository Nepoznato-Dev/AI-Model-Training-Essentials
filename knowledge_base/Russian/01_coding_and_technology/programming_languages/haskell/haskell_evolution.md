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
# Haskell — история версий и эволюция
## Временная шкала
| Версия | Год | Ключевая тема |
|---------|------|-----------|
| Хаскелл 1.0 | 1990 | Первоначальный выпуск (усилия комитета) |
| Хаскелл 1.2 | 1992 | Эксперименты с объектной системой |
| Хаскелл 1.3 | 1996 | Представлены классы типов |
| Хаскелл 1.4 | 1997 |  Уточнена монада`IO`|
| Хаскелл 98 | 1998 | **Первый стабильный стандарт** |
| Хаскелл 2010 | 2010 | **Пересмотренный стандарт**, Кабал, модули |
| ГХК 7.0 | 2011 | Семейства типов, виды данных |
| ГХК 7.4 | 2012 | Начало предложения аппликативной монады |
| ГХК 7.6 | 2013 | Улучшения типовых семейств |
| ГХК 7.8 | 2014 | Синонимы шаблонов,`NegativeLiterals`|
| ГХК 7.10 | 2015 | **Предложение аппликативной монады (AMP)**,`-XStrict`|
| ГХК 8.0 | 2016 | **TypeApplications**,`MonadFail`, ошибки пользовательского типа |
| ГХК 8.2 | 2017 | Суммы без коробки, рюкзак (система модулей) |
| ГХК 8.4 | 2018 | Абстрактный базовый путь,`Semigroup`>>`Monoid`|
| ГХК 8.6 | 2018 | StarIsType,`DerivingVia`|
| ГХК 8.8 | 2019 | MonadFail в Prelude |
| ГХК 8.10 | 2020 | Унифицированная нотация `do`, видовой полиморфизм |
| ГХК 9.0 | 2021 | **Полиморфизм левитации**, линейные типы |
| ГХК 9.2 | 2022 | Квалифицированный `do`, улучшенные сообщения об ошибках |
| ГХК 9.4 | 2022 | **GHC2021** Набор языковых расширений,`OverloadedRecordDot`|
| ГХК 9.6 | 2023 | Обязательные аргументы типа`TypeAbstractions`|
| ГХК 9.8 | 2024 | `TypeAbstractions`стабильная, улучшенные сообщения об ошибках |
| ГХК 9.10 | 2024 | Дальнейшие усовершенствования, производительность |
| ГХК 9.12 | 2025 | Постоянное развитие |
## Основные вехи
### Haskell 1.x — Годы работы Комитета (1990–1998)
- **1990**: Haskell 1.0 — разработанный комитетом ленивый функциональный язык.
- **1.3 (1996 г.)**: Классы типов — определяющая особенность Haskell.
- **1.4 (1997)**: разъяснена монада`IO`— как обрабатывать только побочные эффекты
- **Haskell 98**: первый стабильный стандарт; все еще упоминается сегодня
### Haskell 2010 — современный стандарт
- **2010**: Пересмотренный стандарт — Cabal (система пакетов), улучшения системы модулей.
- GHC становится фактическим компилятором
- Cabal + Hackage = экосистема пакетов Haskell
### GHC 7.x — Тип питания системы (2011–2015 гг.)
- Семейства типов, виды данных, полиморфизм видов.
— Applicative-Monad Proposal (AMP) — исправление иерархии классов типов.
- Синонимы шаблонов, расширение `Strict`.
### GHC 8.x — Современный Haskell (2016–2020 гг.)
-`TypeApplications`— аргументы явного типа на сайтах вызова.
- Ошибки пользовательского типа — улучшенные сообщения компилятора.
- Рюкзак — модульная система для компонентного проектирования.
-`DerivingVia`— гибкие стратегии деривации
### GHC 9.x — революция юзабилити (с 2021 г. по настоящее время)
- **9.0**: Полиморфизм левитации, линейные типы (ресурсобезопасность)
- **9.2**: уточненный `do`, улучшенные сообщения об ошибках.
- **9.4**: **GHC2021** — современные расширения по умолчанию; `OverloadedRecordDot`(доступ к полю с помощью`.`)
- **9.6**: обязательные аргументы типа `TypeAbstractions`. 
- **9.8–9.12**: постоянные улучшения сообщений об ошибках, производительность.
## Эволюция синтаксиса
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

## Эволюция системы типов
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

## Параллелизм и параллелизм
```
Haskell 98:  No standard concurrency model
2004: GHC 6.2 — Software Transactional Memory (STM)
2007: GHC 6.8 — lightweight threads (green threads)
2011: async library — structured concurrency
2018: io-streams, conduit — streaming I/O
2021: Linear types — resource-safe concurrency
2025: GHC + effect systems (Effectful, UnliftIO)
```

## Ключевые принципы проектирования
```
1. "Lazy by default" — non-strict evaluation
2. "Pure by default" — side effects explicit via monads
3. "Types are truth" — strong static typing
4. "Referential transparency" — same input → same output
5. "Composability" — small building blocks, compose freely
6. "Make illegal states unrepresentable" — type system as design tool
```

## Рост экосистемы
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
