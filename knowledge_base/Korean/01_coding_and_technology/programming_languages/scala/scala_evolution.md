---
# Metadata
title: "Scala — Version History & Evolution"
description: "Comprehensive version history and evolution of Scala from 1.0 to modern Scala."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial version history"
tags: [scala, version-history, evolution, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "10 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

# Scala — 버전 기록 및 진화
## 타임라인
| 버전 | 연도 | 주요 테마 |
|---------|------|------------|
| 1.0 | 2004년 | 최초 출시(Martin Odersky, EPFL) |
| 2.0 | 2006년 | 구조 유형, 패턴 일치 개선 |
| 2.7 | 2009 | 액터 라이브러리, 향상된 유형 추론 |
| 2.8 | 2010 | **명명된/기본 인수**, 패키지 객체, 컬렉션 재설계 |
| 2.9 | 2011 | 병렬 컬렉션, 문자열 보간 |
| 2.10 | 2013 | **값 클래스**, 암시적 개선, 문자열 보간 |
| 2.11 | 2014 | 문자열 보간, 향상된 컬렉션 |
| 2.12 | 2016 | **SAM 유형**(Java 8 람다), Strawman |
| 2.13 | 2019 | **컬렉션 재설계**, 암시적 이름별 매개변수 |
| 3.0 | 2021 | **주요**: 새로운 컴파일러(Dotty),`enum`,`given`/`using`, 확장 방법 |
| 3.1 | 2022 | 절 내보내기,`opaque`유형 별칭 |
| 3.2 | 2022 | `inline`개선,`erased`키워드 |
| 3.3 | 2023년 | **LTS 릴리스** — 명시적 null,`derives`절 |
| 3.4 | 2024 | 명명된 유형 인수,`@experimental`주석 |
| 3.5 | 2024 | 캡처 검사기, 오류 메시지 개선 |
| 3.6 | 2025 | 추가 개선, 성능 개선 |
## 주요 이정표
### 초기 스칼라(2004~2010)
- **2004**: Martin Odersky가 Scala 출시 - JVM에서 OOP와 FP를 결합
- **2.0–2.7**: 구조적 유형, 행위자, 향상된 유형 추론
- **2.8 (2010)**: 명명된/기본 인수, 패키지 객체, 컬렉션 재설계 — "현대적인 스칼라 시작"
### Scala 2.x 성숙도(2011~2020)
- **2.9**: 병렬 컬렉션
- **2.10**: 값 클래스, 문자열 보간, 암시적 개선
- **2.12**: SAM 유형 — 원활한 Java 8 상호 운용성
- **2.13**: 주요 컬렉션 라이브러리 재설계(기본값은 변경할 수 없음)
### 스칼라 3 — 르네상스(2021~현재)
- **3.0(2021)**: 완전한 컴파일러 재작성(Dotty → Scala 3)
  - `enum`는 봉인된 특성 + 케이스 클래스 상용구를 대체합니다.
  -`given`/ `using`는 암시적 매개변수를 대체합니다.
  - 확장 메소드는 암시적 클래스를 대체합니다.
  - `match`형, 유니온형, 교차형
  - 단순화된 구문(선택적 중괄호, 더 적은 키워드)
- **3.3(2023)**: 첫 번째 LTS — 명시적 null,`derives`절
- **3.4–3.6**: 명명된 유형 인수, 캡처 검사기, 성능
## 구문 진화
```scala
// Scala 2: Implicit class for extension methods
implicit class StringOps(val s: String) extends AnyVal {
  def shout: String = s.toUpperCase + "!"
}

// Scala 3: Extension methods
extension (s: String)
  def shout: String = s.toUpperCase + "!"

// Scala 2: Sealed trait + case class (ADT)
sealed trait Color
case object Red extends Color
case object Blue extends Color

// Scala 3: enum
enum Color:
  case Red, Blue, Green

// Scala 2: Implicit parameters
def greet(implicit ctx: Context): String = ctx.name

// Scala 3: given/using
given ctx: Context = Context("Alice")
def greet(using ctx: Context): String = ctx.name

// Scala 3: Union types
def process(input: String | Int): String = input.toString

// Scala 3: Match types
type Elem[X] = X match
  case String => Char
  case List[t] => t
  case _ => X
```

## 유형 시스템 진화
```
Scala 2.0:  Structural types, refinements
Scala 2.7:  Existential types
Scala 2.8:  Implicit resolution rules
Scala 2.10: Value classes, macro annotations
Scala 2.12: SAM conversion, Java 8 interop
Scala 2.13: Implicit by-name, literal types
Scala 3.0:  Union types, intersection types, match types,
            opaque types, enum, given/using, extension methods
Scala 3.3:  Explicit nulls, derives clause
Scala 3.4:  Named type arguments
Scala 3.5:  Capture checker (experimental)
```

## 동시성 진화
```
2009: Scala Actors library (green threads)
2011: Akka library (Actor model, JVM-based)
2013: Scala Futures + Promises (standard library)
2018: Cats Effect (functional effect system)
2020: ZIO (functional effect system, high performance)
2025: Scala 3 + virtual threads (Java 21 Loom integration)
```

## 주요 디자인 원칙
```
1. "Scalable language" — from scripts to large systems
2. "Unify OOP and FP" — everything is an object, everything is a function
3. "Type safety" — leverage the type system for correctness
4. "Interoperability" — seamless Java interop
5. "Expressiveness" — concise, elegant syntax
6. "Evidence-based" — type classes via given/using (Scala 3)
```

## 생태계 성장
```
2004: Scala released by Martin Odersky (EPFL)
2009: Twitter adopts Scala — puts Scala on the map
2011: Akka framework — distributed computing
2012: Play Framework 2.0 — web development
2014: Apache Spark — big data processing in Scala
2016: sbt becomes standard build tool
2021: Scala 3 — modernized language
2025: Scala powers LinkedIn, Twitter, Netflix, The Guardian, Stripe
       sbt, Mill build tools; Akka, ZIO, Cats Effect ecosystems
```
