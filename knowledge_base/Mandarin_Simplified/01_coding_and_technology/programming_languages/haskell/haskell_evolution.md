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
# Haskell — 版本历史和演变
## 时间轴
|版本 |年份|关键主题 |
|--------|------|------------|
|哈斯克尔 1.0 | 1990 |初始版本（委员会努力）|
|哈斯克尔 1.2 | 1992 |对象系统实验|
|哈斯克尔 1.3 | 1996 |类型类介绍 |
|哈斯克尔 1.4 | 1997 | `IO`monad 澄清 |
|哈斯克尔 98 | 1998 | **第一个稳定标准** |
|哈斯克尔 2010 | 2010 | **修订标准**，Cabal，模块 |
| GHC 7.0 | 2011 |类型族、数据类型 |
| GHC 7.4 | 2012 | Applicative-Monad 提案开始 |
| GHC 7.6 | 2013 |类型系列改进 |
| GHC 7.8 | 2014年|模式同义词，`NegativeLiterals` |
| GHC 7.10 | 2015 | 2015 **应用单子提案（AMP）**，`-XStrict` |
| GHC 8.0 | 2016 | 2016 **类型应用程序**，`MonadFail`，自定义类型错误 |
| GHC 8.2 | 2017 | 2017开箱金额，背包（模块系统）|
| GHC 8.4 | 2018 |抽象基本路径，`Semigroup` >>`Monoid`|
| GHC 8.6 | 2018 |星型，`DerivingVia` |
| GHC 8.8 | 2019 | 2019前奏中的 MonadFail |
| GHC 8.10 | 2020 |统一`do`表示法，种多态性|
| GHC 9.0 | 2021 | **轻量多态性**，线性类型 |
| GHC 9.2 | 2022 | 2022合格的`do`，改进的错误消息|
| GHC 9.4 | 2022 | 2022 **GHC2021** 语言扩展集，`OverloadedRecordDot` |
| GHC 9.6 | 2023 |必需的类型参数，`TypeAbstractions` |
| GHC 9.8 | 2024 | 2024  `TypeAbstractions`稳定，改进错误消息|
| GHC 9.10 | 2024 | 2024进一步完善，性能|
| GHC 9.12 | 2025 | 2025持续发展|
## 主要里程碑
### Haskell 1.x — 委员会年（1990–1998）
- **1990**：Haskell 1.0 — 委员会设计的惰性函数式语言
- **1.3 (1996)**：类型类 — Haskell 的定义功能
- **1.4 (1997)**：`IO` monad 澄清 - 如何纯粹处理副作用
- **Haskell 98**：第一个稳定标准；今天仍然被引用
### Haskell 2010 — 现代标准
- **2010**：修订标准 - Cabal（软件包系统）、模块系统改进
- GHC 成为事实上的编译器
- Cabal + Hackage = Haskell 的软件包生态系统
### GHC 7.x — 类型系统功率 (2011–2015)
- 类型族、数据种类、种类多态性
- Applicative-Monad Proposal (AMP) — 修复类型类层次结构
- 模式同义词，`Strict` 扩展
### GHC 8.x — 现代 Haskell (2016–2020)
-`TypeApplications`— 调用站点的显式类型参数
- 自定义类型错误——更好的编译器消息
- Backpack — 用于基于组件的设计的模块系统
-`DerivingVia`— 灵活的派生策略
### GHC 9.x — 可用性革命（2021 年至今）
- **9.0**：轻量多态性，线性类型（资源安全）
- **9.2**：合格的`do`，改进的错误消息
- **9.4**：**GHC2021** — 现代默认扩展；  `OverloadedRecordDot`（使用`.`进行现场访问）
- **9.6**：必需的类型参数，`TypeAbstractions` 
- **9.8–9.12**：持续改进错误消息、性能
## 语法演变
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

## 类型系统的演变
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

## 并发与并行
```
Haskell 98:  No standard concurrency model
2004: GHC 6.2 — Software Transactional Memory (STM)
2007: GHC 6.8 — lightweight threads (green threads)
2011: async library — structured concurrency
2018: io-streams, conduit — streaming I/O
2021: Linear types — resource-safe concurrency
2025: GHC + effect systems (Effectful, UnliftIO)
```

## 关键设计原则
```
1. "Lazy by default" — non-strict evaluation
2. "Pure by default" — side effects explicit via monads
3. "Types are truth" — strong static typing
4. "Referential transparency" — same input → same output
5. "Composability" — small building blocks, compose freely
6. "Make illegal states unrepresentable" — type system as design tool
```

## 生态系统增长
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
