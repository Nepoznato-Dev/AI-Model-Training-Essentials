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
# Haskell — 버전 기록 및 진화
## 타임라인
| 버전 | 연도 | 주요 테마 |
|---------|------|------------|
| 하스켈 1.0 | 1990 | 최초 출시(위원회 노력) |
| 하스켈 1.2 | 1992 | 객체 시스템 실험 |
| 하스켈 1.3 | 1996 | 유형 클래스 소개 |
| 하스켈 1.4 | 1997 | `IO`모나드 명확화 |
| 하스켈 98 | 1998 | **최초의 안정적인 표준** |
| 하스켈 2010 | 2010 | **개정표준**, Cabal, 모듈 |
| GHC 7.0 | 2011 | 유형군, 데이터 종류 |
| GHC 7.4 | 2012 | Applicative-Monad 제안 시작 |
| GHC 7.6 | 2013 | 유형군 개선 |
| GHC 7.8 | 2014 | 패턴 동의어,`NegativeLiterals`|
| GHC 7.10 | 2015 | **애플리케이션 모나드 제안(AMP)**,`-XStrict`|
| GHC 8.0 | 2016 | **TypeApplications**, `MonadFail`, 사용자 정의 유형 오류 |
| GHC 8.2 | 2017 | 박스포장되지 않은 금액, 백팩(모듈시스템) |
| GHC 8.4 | 2018 | 추상 기본 경로,`Semigroup`>>`Monoid`|
| GHC 8.6 | 2018 | StarIsType,`DerivingVia`|
| GHC 8.8 | 2019 | Prelude의 MonadFail |
| GHC 8.10 | 2020 |`do`표기법 통일, 종류 다형성 |
| GHC 9.0 | 2021 | **경박 다형성**, 선형 유형 |
| GHC 9.2 | 2022 | 정규화된 `do`, 향상된 오류 메시지 |
| GHC 9.4 | 2022 | **GHC2021** 언어 확장 세트,`OverloadedRecordDot`|
| GHC 9.6 | 2023년 | 필수 유형 인수,`TypeAbstractions`|
| GHC 9.8 | 2024 | `TypeAbstractions`안정적이고 개선된 오류 메시지 |
| GHC 9.10 | 2024 | 추가 개선, 성능 |
| GHC 9.12 | 2025 | 지속적인 개발 |
## 주요 이정표
### Haskell 1.x — 위원회 시절(1990-1998)
- **1990**: Haskell 1.0 — 위원회가 설계한 게으른 함수형 언어
- **1.3 (1996)**: 유형 클래스 — Haskell의 정의 기능
- **1.4 (1997)**:`IO`모나드가 명확해졌습니다 — 부작용을 순수하게 처리하는 방법
- **Haskell 98**: 최초의 안정적인 표준; 오늘날에도 여전히 참조됨
### Haskell 2010 — 현대 표준
- **2010년**: 표준 개정 — Cabal(패키지 시스템), 모듈 시스템 개선
- GHC가 사실상의 컴파일러가 됨
- Cabal + Hackage = Haskell의 패키지 생태계
### GHC 7.x — 유형 시스템 전원(2011~2015)
- 유형군, 데이터 종류, 종류 다형성
- AMP(Applicative-Monad Proposal) — 유형 클래스 계층 구조 수정
- 패턴 동의어,`Strict`확장
### GHC 8.x — 최신 하스켈(2016-2020)
-`TypeApplications`— 호출 사이트의 명시적 유형 인수
- 사용자 정의 유형 오류 — 더 나은 컴파일러 메시지
- 백팩 - 구성 요소 기반 설계를 위한 모듈 시스템
-`DerivingVia`— 유연한 파생 전략
### GHC 9.x — 사용성 혁명(2021~현재)
- **9.0**: 경솔 다형성, 선형 유형(자원 안전성)
- **9.2**: 정규화된`do`, 오류 메시지 개선
- **9.4**: **GHC2021** — 최신 기본 확장;  `OverloadedRecordDot`(`.`를 사용한 필드 액세스)
- **9.6**: 필수 유형 인수,`TypeAbstractions`
- **9.8~9.12**: 지속적인 오류 메시지 개선, 성능
## 구문 진화
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

## 유형 시스템 진화
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

## 동시성 및 병렬성
```
Haskell 98:  No standard concurrency model
2004: GHC 6.2 — Software Transactional Memory (STM)
2007: GHC 6.8 — lightweight threads (green threads)
2011: async library — structured concurrency
2018: io-streams, conduit — streaming I/O
2021: Linear types — resource-safe concurrency
2025: GHC + effect systems (Effectful, UnliftIO)
```

## 주요 디자인 원칙
```
1. "Lazy by default" — non-strict evaluation
2. "Pure by default" — side effects explicit via monads
3. "Types are truth" — strong static typing
4. "Referential transparency" — same input → same output
5. "Composability" — small building blocks, compose freely
6. "Make illegal states unrepresentable" — type system as design tool
```

## 생태계 성장
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
