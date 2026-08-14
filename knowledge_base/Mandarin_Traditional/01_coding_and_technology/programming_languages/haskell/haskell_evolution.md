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

# Haskell — 版本歷史與演變
## 時間軸
|版本 |年份|關鍵主題 |
|--------|------|------------|
|哈斯克爾 1.0 | 1990 |初始版本（委員會努力）|
|哈斯克爾 1.2 | 1992 |物件系統實驗|
|哈斯克爾 1.3 | 1996 |模式類介紹 |
|哈斯克爾 1.4 | 1997 |`IO`monad 澄清 |
|哈斯克爾 98 | 1998 | **第一個穩定標準** |
|哈斯克爾 2010 | 2010 | **修訂標準**，Cabal，模組 |
| GHC 7.0 | 2011 |型別族、資料型別 |
| GHC 7.4 | 2012 | Applicative-Monad 提案開始 |
| GHC 7.6 | 2013 |類型系列改良 |
| GHC 7.8 | 2014年|模式同義詞，`NegativeLiterals` |
| GHC 7.10 | 2015 | 2015 **應用單子提案（AMP）**，`-XStrict` |
| GHC 8.0 | 2016 | 2016 **類型應用程式**，`MonadFail`，自訂類型錯誤 |
| GHC 8.2 | 2017 | 2017開箱金額，背包（模組系統）|
| GHC 8.4 | 2018 |抽象基本路徑，`Semigroup` >>`Monoid`|
| GHC 8.6 | 2018 |星型，`DerivingVia` |
| GHC 8.8 | 2019 | 2019前奏中的 MonadFail |
| GHC 8.10 | 2020 |統一`do`表示法，種多態性|
| GHC 9.0 | 2021 | **輕量多型**，線性型別|
| GHC 9.2 | 2022 | 2022合格的`do`，改進的錯誤訊息|
| GHC 9.4 | 2022 | 2022 **GHC2021** 語言擴充集，`OverloadedRecordDot` |
| GHC 9.6 | 2023 |必要的型別參數，`TypeAbstractions` |
| GHC 9.8 | 2024 | 2024 `TypeAbstractions`穩定，改進錯誤訊息|
| GHC 9.10 | 2024 | 2024進一步完善，性能|
| GHC 9.12 | 2025 | 2025持續發展|
## 主要里程碑
### Haskell 1.x — 委員會年（1990–1998）
- **1990**：Haskell 1.0 — 委員會設計的惰性函數式語言
- **1.3 (1996)**：型別類別 — Haskell 的定義功能
- **1.4 (1997)**：`IO` monad 澄清 - 如何純粹處理副作用
- **Haskell 98**：第一個穩定標準；今天仍然被引用
### Haskell 2010 — 現代標準
- **2010**：修訂標準 - Cabal（軟體包系統）、模組系統改進
- GHC 成為事實上的編譯器
- Cabal + Hackage = Haskell 的軟體包生態系統
### GHC 7.x — 型系統功率 (2011–2015)
- 類型族、資料種類、種類多態性
- Applicative-Monad Proposal (AMP) — 修正類型類別層次結構
- 模式同義詞，`Strict` 擴展
### GHC 8.x — 現代 Haskell (2016–2020)
-`TypeApplications`— 呼叫站點的明確型別參數
- 自訂類型錯誤－更好的編譯器訊息
- Backpack — 用於基於組件的設計的模組系統
-`DerivingVia`— 靈活的衍生策略
### GHC 9.x — 可用性革命（2021 年至今）
- **9.0**：輕量多型性，線性型別（資源安全）
- **9.2**：合格的`do`，改進的錯誤訊息
- **9.4**：**GHC2021** — 現代預設擴充； `OverloadedRecordDot`（使用`.`進行現場存取）
- **9.6**：必需的型別參數，`TypeAbstractions`
- **9.8–9.12**：持續改善錯誤訊息、效能
## 語法演變
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

## 類型系統的演變
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

## 並發與平行
```
Haskell 98:  No standard concurrency model
2004: GHC 6.2 — Software Transactional Memory (STM)
2007: GHC 6.8 — lightweight threads (green threads)
2011: async library — structured concurrency
2018: io-streams, conduit — streaming I/O
2021: Linear types — resource-safe concurrency
2025: GHC + effect systems (Effectful, UnliftIO)
```

## 關鍵設計原則
```
1. "Lazy by default" — non-strict evaluation
2. "Pure by default" — side effects explicit via monads
3. "Types are truth" — strong static typing
4. "Referential transparency" — same input → same output
5. "Composability" — small building blocks, compose freely
6. "Make illegal states unrepresentable" — type system as design tool
```

## 生態系成長
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
