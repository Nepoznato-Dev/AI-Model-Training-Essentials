<!--
---
# Metadata
title: "Scala — Version History & Evolution"
description: "Comprehensive version history and evolution of Scala from 1.0 to modern Scala."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
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

-->
# Scala — 版本歷史與演變
## 時間軸
|版本 |年份|關鍵主題 |
|--------|------|------------|
| 1.0 | 2004 |初始版本（Martin Odersky，EPFL）|
| 2.0 | 2006 |結構類型、模式匹配改進|
| 2.7 | 2.7 2009 |演員庫，改進的類型推論 |
| 2.8 | 2.8 2010 | **命名/預設參數**，包對象，集合重新設計 |
| 2.9 | 2.9 2011 |平行集合、字串插值 |
| 2.10 | 2.10 2013 | **值類別**、隱式改進、字串插值 |
| 2.11 | 2.11 2014年|字串插值，改進集合 |
| 2.12 | 2.12 2016 | 2016 **SAM 類型**（Java 8 lambda），Strawman 上的集合 |
| 2.13 | 2.13 2019 | 2019 **集合重新設計**，隱含依名稱參數 |
| 3.0 | 2021 | **主要**：新編譯器 (Dotty)、`enum`、`given`/`using`、擴充方法 |
| 3.1| 2022 | 2022匯出子句，`opaque` 型別別名 |
| 3.2 | 2022 | 2022`inline`改進，`erased` 關鍵字 |
| 3.3 | 2023 | **LTS 版本** — 明確 null、`derives` 子句 |
| 3.4 | 3.4 2024 | 2024命名型別參數，`@experimental` 註解 |
| 3.5 | 3.5 2024 | 2024捕獲檢查器，改進的錯誤訊息 |
| 3.6 | 3.6 2025 | 2025進一步完善，性能改進|
## 主要里程碑
### 早期 Scala (2004–2010)
- **2004**：Martin Odersky 發布了 Scala — 在 JVM 上結合了 OOP 和 FP
- **2.0–2.7**：結構類型、參與者、改進的類型推斷
- **2.8 (2010)**：命名/預設參數、套件物件、集合重新設計 — “現代 Scala 開始”
### Scala 2.x 成熟度 (2011–2020)
- **2.9**：平行集合
- **2.10**：值類別、字串插值、隱式改進
- **2.12**：SAM 類型 — 無縫 Java 8 互通
- **2.13**：主要集合庫重新設計（不可變的預設值）
### Scala 3 — 文藝復興（2021 年至今）
- **3.0 (2021)**：完整的編譯器重寫（Dotty → Scala 3）
  -`enum`替換密封特徵 + 案例類樣板
  -`given`/`using`取代隱式參數
  - 擴展方法取代隱式類
  -`match`類型、並集類型、交集類型
  - 簡化的語法（可選的大括號，較少的關鍵字）
- **3.3 (2023)**：第一個 LTS — 明確空值、`derives` 子句
- **3.4–3.6**：命名類型參數、擷取檢查器、效能
## 語法演變
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

## 類型系統的演變
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

## 並發演進
```
2009: Scala Actors library (green threads)
2011: Akka library (Actor model, JVM-based)
2013: Scala Futures + Promises (standard library)
2018: Cats Effect (functional effect system)
2020: ZIO (functional effect system, high performance)
2025: Scala 3 + virtual threads (Java 21 Loom integration)
```

## 關鍵設計原則
```
1. "Scalable language" — from scripts to large systems
2. "Unify OOP and FP" — everything is an object, everything is a function
3. "Type safety" — leverage the type system for correctness
4. "Interoperability" — seamless Java interop
5. "Expressiveness" — concise, elegant syntax
6. "Evidence-based" — type classes via given/using (Scala 3)
```

## 生態系成長
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
