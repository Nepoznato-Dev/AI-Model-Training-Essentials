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
# Scala — バージョンの歴史と進化
## タイムライン
|バージョン |年 |主要テーマ |
|----------|------|----------|
| 1.0 | 2004年 |初期リリース (Martin Odersky、EPFL) |
| 2.0 | 2006年 |構造タイプ、パターン マッチングの改善 |
| 2.7 | 2009年 |アクター ライブラリ、型推論の改善 |
| 2.8 | 2010年 | **名前付き/デフォルト引数**、パッケージ オブジェクト、コレクションの再設計 |
| 2.9 | 2011年 |並列コレクション、文字列補間 |
| 2.10 | 2013年 | **値クラス**、暗黙の改善、文字列補間 |
| 2.11 | 2014年 |文字列補間、コレクションの改善 |
| 2.12 | 2016年 | **SAM タイプ** (Java 8 ラムダ)、Strawman のコレクション |
| 2.13 | 2019年 | **コレクションの再設計**、暗黙的な名前によるパラメータ |
| 3.0 | 2021年 | **主要**: 新しいコンパイラ (Dotty)、`enum`、`given`/`using`、拡張メソッド |
| 3.1 | 2022年 |エクスポート句、`opaque` タイプのエイリアス |
| 3.2 | 2022年 | `inline`の改善、`erased` キーワード |
| 3.3 | 2023年 | **LTS リリース** - 明示的な null、`derives` 句 |
| 3.4 | 2024年 |名前付き型引数、`@experimental` 注釈 |
| 3.5 | 2024年 |キャプチャ チェッカー、エラー メッセージの改善 |
| 3.6 | 2025年 |さらなる改良、パフォーマンスの向上 |
## 主要なマイルストーン
### 初期の Scala (2004 ～ 2010)
- **2004**: Martin Odersky が Scala をリリース — JVM 上で OOP と FP を組み合わせたもの
- **2.0–2.7**: 構造型、アクター、型推論の改善
- **2.8 (2010)**: 名前付き/デフォルト引数、パッケージ オブジェクト、コレクションの再設計 — 「モダンな Scala の始まり」
### Scala 2.x の成熟度 (2011 ～ 2020)
- **2.9**: 並列コレクション
- **2.10**: 値クラス、文字列補間、暗黙的な改善
- **2.12**: SAM タイプ — シームレスな Java 8 相互運用性
- **2.13**: 主要なコレクション ライブラリの再設計 (不変のデフォルト)
### Scala 3 — ルネッサンス (2021–現在)
- **3.0 (2021)**: コンパイラーを完全に書き直しました (Dotty → Scala 3)
  -`enum`は、sealed trait + case クラスのボイラープレートを置き換えます
  -`given`/`using`は暗黙的なパラメーターを置き換えます
  - 拡張メソッドは暗黙的なクラスを置き換えます
  - `match`型、和集合型、交差型
  - 簡素化された構文 (オプションの中括弧、少ないキーワード)
- **3.3 (2023)**: 最初の LTS — 明示的な null、`derives` 句
- **3.4–3.6**: 名前付き型引数、キャプチャ チェッカー、パフォーマンス
## 構文の進化
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

## 型システムの進化
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

## 同時実行の進化
```
2009: Scala Actors library (green threads)
2011: Akka library (Actor model, JVM-based)
2013: Scala Futures + Promises (standard library)
2018: Cats Effect (functional effect system)
2020: ZIO (functional effect system, high performance)
2025: Scala 3 + virtual threads (Java 21 Loom integration)
```

## 主要な設計原則
```
1. "Scalable language" — from scripts to large systems
2. "Unify OOP and FP" — everything is an object, everything is a function
3. "Type safety" — leverage the type system for correctness
4. "Interoperability" — seamless Java interop
5. "Expressiveness" — concise, elegant syntax
6. "Evidence-based" — type classes via given/using (Scala 3)
```

## エコシステムの成長
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
