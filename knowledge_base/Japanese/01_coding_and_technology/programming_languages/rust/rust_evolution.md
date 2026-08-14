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
# Rust — バージョンの歴史と進化
## タイムライン
|バージョン |発売日 |主要テーマ |
|----------|---------------|----------|
| 0.1 | 2012 年 1 月 |最初のコンパイラ (rustc)、タスクベースの同時実行 |
| 0.5 | 2012年 |特性ベースの型システムが具体化 |
| 0.6 | 2012年 |`@`管理ボックスの削除 |
| 0.7 | 2013年 | `@`が削除され、所有ボックスは`~`|
| 0.8 | 2013年 |生涯の注釈、`&mut` |
| 0.9 | 2014年1月 | 1.0 より前の最終クリーンアップ |
| 0.10 | 2014年2月 | 1.0 より前の最後のリリース |
| 0.11 | 2014年4月 | `Box<T>`は`~T`を置き換えます。
| 0.12 | 2014年5月 | `io`モジュールの書き換えが開始される |
| 1.0 | 2015年5月15日 | **安定版リリース** — 「Rust 1.0」 |
| 1.10 | 2016 年 8 月 | `?`エラーの伝播 (`try!`→`?`として) |
| 1.15 | 2017年2月 |`impl Trait`を準備して安定した最初の Rust |
| 1.18 | 2017年6月 | `pub(crate)`、増分コンパイル |
| 1.20 | 2017年10月 |関連する定数 |
| 1.26 | 2018年5月 |  引数/戻り位置の`impl Trait`|
| 1.28 | 2018年9月 |グローバル アロケータ |
| 1.31 | 2018年12月 | **Rust 2018 Edition** — モジュール、`dyn Trait` |
| 1.34 | 2019年4月 |代替レジストリ |
| 1.39 | 2019年11月 | `async/await`安定版 |
| 1.44 | 2020年7月 |診断の改善 |
| 1.51 | 2021年4月 | `const`ジェネリック (MVP) |
| 1.56 | 2021年10月 | **Rust 2021 Edition** — クロージャ、IntoIterator |
| 1.59 | 2022 年 2 月 |インラインアセンブリ |
| 1.62 | 2022 年 6 月 |  列挙型の`#[default]`|
| 1.65 | 2022 年 12 月 | `let else`|
| 1.68 | 2023 年 3 月 | `#[ffi_pure]`、プロファイルに基づく最適化 |
| 1.70 | 2023 年 6 月 |分離された`crates.io`依存関係 |
| 1.74 | 2023 年 11 月 |貨物オフラインモード |
| 1.76 | 2024 年 2 月 | **Rust 2024 Edition** —`gen`ブロック、`unsafe extern` |
| 1.79 | 2024 年 6 月 |  `LazyCell`、`LazyLock` |
| 1.82 | 2024 年 10 月 | `extern`ブロック内の`unsafe`が必要です。
| 1.85 | 2025 年 2 月 | Rust 2024 版が安定化 |
## 主要なマイルストーン
### 1.0 より前 (2010 ～ 2015)
- **2010**: Mozilla での Graydon Hoare のサイド プロジェクトが注目を集める
- **2012**: 最初の公開コンパイラ。型システムが大幅に再設計される
- **2013**: 所有権モデルが具体化。 `@`ボックスが削除されました
- **2014**: Rust RFC プロセスが正式化。コミュニティが成長する
- **2015**: **1.0** — 安定性の保証。 「ゼロコストの抽象化」
### 成長期 (2015 ～ 2019 年)
- **2015**: Cargo が標準のパッケージ マネージャーになる
- **2018**: **Rust 2018 Edition** — モジュール システムのオーバーホール、`dyn Trait`、`impl Trait`
- **2019**:`async/await`が安定版に到達 — 非同期エコシステムが開始
### 成熟度 (2020 ～現在)
- **2021**: **Rust 2021 Edition** — クロージャ内のフィールドの曖昧さをなくす、配列の `IntoIterator`
- **2024**: **Rust 2024 Edition** —`gen`ブロック、`unsafe extern` 要件
- **2025**: Linux カーネル、Android、Windows、AWS インフラストラクチャにおける Rust
## エディション システム
```
Rust 2015:  The baseline (1.0)
Rust 2018:  Module system, async/await prep, dyn Trait
Rust 2021:  Closure changes, IntoIterator, panic macros
Rust 2024:  gen blocks, unsafe extern, tail expressions

Key principle: Editions are opt-in, never break existing code.
Old editions always compile. New editions add features.
```

## 所有権の進化
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

## 非同期進化
```
2018: futures 0.1 — early async with manual polling
2019: async/await syntax (Rust 1.39)
2019: tokio 0.2 — async runtime
2020: async-std — std-like async API
2021: tokio 1.0 — stable async runtime
2023: async fn in traits (Rust 1.75)
2024: async closures, improved Send bounds
```

## エコシステムの成長
```
2015: crates.io launches (~2,000 crates)
2018: Rust most loved language (Stack Overflow survey)
2019: 30,000 crates on crates.io
2021: Most admired language (6th consecutive year)
2023: 130,000+ crates
2025: Used in Linux kernel, Android, Windows, Chromium, AWS, Cloudflare, Discord, Dropbox
```

## 主要な RFC
| RFC |年 |特集 |
|------|------|-----------|
| 25 | 2013年 |パターンマッチング |
| 153 | 2014年 | `Result`タイプ |
| 217 | 2014年 | `?`(試行) 演算子 |
| 460 | 2016年 | `?`は`try!`を置き換えます |
| 1210 | 2015年 | `impl Trait`|
| 1414 | 2016年 | Rust 2018 版 |
| 2394 | 2018年 | `async/await`|
| 2515 | 2018年 | `const`ジェネリック |
| 3013 | 2020年 |条件付きコンパイルのチェック |
| 3517 | 2023年 | `gen`ブロック |