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
# Haskell — バージョン履歴と進化
## タイムライン
|バージョン |年 |主要テーマ |
|----------|------|----------|
|ハスケル 1.0 | 1990年 |初期リリース (委員会の取り組み) |
|ハスケル 1.2 | 1992年 |オブジェクトシステムの実験 |
|ハスケル 1.3 | 1996年 |型クラスの導入 |
|ハスケル 1.4 | 1997年 | `IO`モナドの説明 |
|ハスケル98 | 1998年 | **最初の安定した標準** |
|ハスケル2010 | 2010年 | **改訂された標準**、陰謀団、モジュール |
| GHC7.0 | 2011年 |型ファミリー、データの種類 |
| GHC7.4 | 2012年 | Applicative-Monad の提案が始まる |
| GHC7.6 | 2013年 |型ファミリーの改善 |
| GHC7.8 | 2014年 |パターンの同義語、`NegativeLiterals` |
| GHC7.10 | 2015年 | **アプリカティブモナド提案 (AMP)**、`-XStrict` |
| GHC8.0 | 2016年 | **TypeApplications**、`MonadFail`、カスタム タイプ エラー |
| GHC8.2 | 2017年 |箱なし合計、バックパック (モジュール システム) |
| GHC8.4 | 2018年 |抽象ベースパス、`Semigroup` >>`Monoid`|
| GHC8.6 | 2018年 | StarIsType、`DerivingVia` |
| GHC8.8 | 2019年 |プレリュードのモナド失敗 |
| GHC8.10 | 2020年 |`do`表記法、種類多態性の統一 |
| GHC9.0 | 2021年 | **レビティポリモーフィズム**、線形型 |
| GHC9.2 | 2022年 |`do`を修飾し、エラー メッセージを改善しました。
| GHC9.4 | 2022年 | **GHC2021** 言語拡張セット、`OverloadedRecordDot` |
| GHC9.6 | 2023年 |必須の型引数、`TypeAbstractions` |
| GHC9.8 | 2024年 | `TypeAbstractions`安定し、改善されたエラー メッセージ |
| GHC9.10 | 2024年 |さらなる改良、パフォーマンス |
| GHC9.12 | 2025年 |進行中の開発 |
## 主要なマイルストーン
### Haskell 1.x — 委員会時代 (1990 ～ 1998 年)
- **1990**: Haskell 1.0 — 委員会が設計した遅延関数型言語
- **1.3 (1996)**: 型クラス — Haskell の定義機能
- **1.4 (1997)**:`IO`モナドを明確化 — 副作用を純粋に処理する方法
- **Haskell 98**: 最初の安定した標準。今でも参照されています
### Haskell 2010 — 現代の標準
- **2010**: 改訂された標準 — Cabal (パッケージ システム)、モジュール システムの改善
- GHCがデファクトコンパイラとなる
- Cabal + Hackage = Haskell のパッケージ エコシステム
### GHC 7.x — システム電源のタイプ (2011 ～ 2015)
- 型ファミリー、データ種類、種類多態性
- Applicative-Monad Proposal (AMP) — 型クラス階層の修正
- パターンの同義語、`Strict` 拡張子
### GHC 8.x — 最新の Haskell (2016–2020)
-`TypeApplications`— 呼び出しサイトでの明示的な型引数
- カスタム型エラー - コンパイラ メッセージの改善
- バックパック — コンポーネントベースの設計のためのモジュールシステム
-`DerivingVia`— 柔軟な導出戦略
### GHC 9.x — ユーザビリティ革命 (2021–現在)
- **9.0**: レビティポリモーフィズム、線形型 (リソースの安全性)
- **9.2**:`do`が修飾され、エラー メッセージが改善されました
- **9.4**: **GHC2021** — 最新のデフォルト拡張機能。 `OverloadedRecordDot`(`.`によるフィールド アクセス)
- **9.6**: 必須の型引数、`TypeAbstractions` 
- **9.8–9.12**: 継続的なエラー メッセージの改善、パフォーマンス
## 構文の進化
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

## 型システムの進化
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

## 同時実行性と並列処理
```
Haskell 98:  No standard concurrency model
2004: GHC 6.2 — Software Transactional Memory (STM)
2007: GHC 6.8 — lightweight threads (green threads)
2011: async library — structured concurrency
2018: io-streams, conduit — streaming I/O
2021: Linear types — resource-safe concurrency
2025: GHC + effect systems (Effectful, UnliftIO)
```

## 主要な設計原則
```
1. "Lazy by default" — non-strict evaluation
2. "Pure by default" — side effects explicit via monads
3. "Types are truth" — strong static typing
4. "Referential transparency" — same input → same output
5. "Composability" — small building blocks, compose freely
6. "Make illegal states unrepresentable" — type system as design tool
```

## エコシステムの成長
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
