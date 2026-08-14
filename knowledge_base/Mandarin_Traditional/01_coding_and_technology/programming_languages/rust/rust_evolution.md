<!--
---
# Metadata
title: "Rust — Version History & Evolution"
description: "Comprehensive version history and evolution of Rust from early development to modern Rust."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial version history"
tags: [rust, version-history, evolution, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "10 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

-->
# Rust — 版本歷史與演變
## 時間軸
|版本 |發佈日期 |關鍵主題 |
|--------|-------------|------------|
| 0.1 | 0.1 2012 年 1 月 |第一個編譯器（rustc），基於任務的並發 |
| 0.5 | 0.5 2012 |基於特質的型別系統初具規模|
| 0.6 | 0.6 2012 |刪除`@`託管框 |
| 0.7 | 0.7 2013 |`@`已刪除，`~` 用於自有盒子 |
| 0.8 | 0.8 2013 |生命週期註釋，`&mut` |
| 0.9 | 0.9 2014 年 1 月 | 1.0 之前的最終清理 |
| 0.10 | 0.10 2014 年 2 月 |最新 1.0 之前版本 |
| 0.11 | 0.11 2014 年 4 月 |`Box<T>`取代`~T`|
| 0.12 | 0.12 2014 年 5 月 | `io`模組重寫開始 |
| 1.0 | 2015 年 5 月 15 日 | **穩定版本** — “Rust 1.0” |
| 1.10 | 1.10 2016 年 8 月 |`?`錯誤傳播（如`try!`→`?`）|
| 1.15 | 1.15 2017 年 2 月 |第一個 Rust 穩定版與`impl Trait`準備 |
| 1.18 | 1.18 2017 年 6 月 | `pub(crate)`，增量編譯|
| 1.20 | 1.20 2017 年 10 月 |相關常數 |
| 1.26 | 1.26 2018 年 5 月 |`impl Trait`處於參數/返回位置 |
| 1.28 | 1.28 2018 年 9 月 |全域分配器|
| 1.31 | 1.31 2018 年 12 月 | **Rust 2018 版** — 模組，`dyn Trait` |
| 1.34 | 1.34 2019 年 4 月 |替代註冊表 |
| 1.39 | 1.39 2019 年 11 月 |`async/await`穩定 |
| 1.44 | 1.44 2020 年 7 月 |診斷改善 |
| 1.51 | 1.51 2021 年 4 月 |`const`仿製藥 (MVP) |
| 1.56 | 1.56 2021 年 10 月 | **Rust 2021 版** — 閉包、IntoIterator |
| 1.59 | 1.59 2022 年 2 月 |內嵌組裝 |
| 1.62 | 1.62 2022 年 6 月 |`#[default]`用於枚舉 |
| 1.65 | 1.65 2022 年 12 月 |`let else`|
| 1.68 | 1.68 2023 年 3 月 | `#[ffi_pure]`，設定檔引導優化 |
| 1.70 | 1.70 2023 年 6 月 |隔離`crates.io`相依性 |
| 1.74 | 1.74 2023 年 11 月 |貨物離線模式|
| 1.76 | 1.76 2024 年 2 月 | **Rust 2024 版** —`gen`區塊、`unsafe extern` |
| 1.79 | 1.79 2024 年 6 月 | `LazyCell`、`LazyLock` |
| 1.82 | 1.82 2024 年 10 月 | 需要`extern`區塊中的`unsafe`|
| 1.85 | 1.85 2025 年 2 月 | Rust 2024 版穩定 |
## 主要里程碑
### Pre-1.0 (2010–2015)
- **2010**：Graydon Hoare 在 Mozilla 的副業項目中獲得關注
- **2012**：第一個公共編譯器；類型系統經歷重大重新設計
- **2013**：所有權模式具體化；`@`框已移除
- **2014**：Rust RFC 流程正式化；社群成長
- **2015**：**1.0** — 穩定性保證； “零成本抽象”
### 成長歲月（2015-2019）
- **2015**：Cargo 成為標準套件管理器
- **2018**：**Rust 2018 版** — 模組系統大修，`dyn Trait` 、 `impl Trait`
- **2019**：`async/await` 穩定 - 非同步生態系統開始
### 成熟度（2020 年至今）
- **2021**：**Rust 2021 Edition** — 消除閉包中字段的歧義，數組的 `IntoIterator`
- **2024**：**Rust 2024 版** —`gen`區塊、`unsafe extern` 需求
- **2025**：Linux 核心、Android、Windows、AWS 基礎架構中的 Rust
## 版本系統
```
Rust 2015:  The baseline (1.0)
Rust 2018:  Module system, async/await prep, dyn Trait
Rust 2021:  Closure changes, IntoIterator, panic macros
Rust 2024:  gen blocks, unsafe extern, tail expressions

Key principle: Editions are opt-in, never break existing code.
Old editions always compile. New editions add features.
```

## 所有權演變
```
2010: GC-based, like Erlang
2011: Region-based lifetimes proposed
2012: Ownership model emerges (unique, shared, owned)
2013: Simplified to &T / &mut T / Box<T>
2014: Box<T> replaces ~T; Rc<T> for shared ownership
2015: 1.0 — ownership model finalized
2018: Non-Lexical Lifetimes (NLL) in Rust 2018
2021: IntoIterator for arrays (was blocked by edition concerns)
2024: Further NLL improvements
```

## 非同步進化
```
2018: futures 0.1 — early async with manual polling
2019: async/await syntax (Rust 1.39)
2019: tokio 0.2 — async runtime
2020: async-std — std-like async API
2021: tokio 1.0 — stable async runtime
2023: async fn in traits (Rust 1.75)
2024: async closures, improved Send bounds
```

## 生態系成長
```
2015: crates.io launches (~2,000 crates)
2018: Rust most loved language (Stack Overflow survey)
2019: 30,000 crates on crates.io
2021: Most admired language (6th consecutive year)
2023: 130,000+ crates
2025: Used in Linux kernel, Android, Windows, Chromium, AWS, Cloudflare, Discord, Dropbox
```

## 關鍵 RFC
| RFC |年份|特色 |
|------|------|---------|
| 25 | 25 2013 |模式匹配|
| 153 | 153 2014年| `Result`型 |
| 217 | 217 2014年| `?`（嘗試）運算子|
| 460 | 460 2016 | 2016`?`取代`try!`|
| 1210 | 1210 2015 | 2015`impl Trait`|
| 1414 | 1414 2016 | 2016 Rust 2018 版 |
| 2394 | 2394 2018 |`async/await`|
| 2515 | 2515 2018 |`const`仿製藥 |
| 3013| 2020 |檢查條件編譯 |
| 3517 | 3517 2023 |`gen`塊 |