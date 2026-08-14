<!--
---
# Metadata
title: "Ruby — Version History & Evolution"
description: "Comprehensive version history and evolution of Ruby from 1.0 to modern Ruby."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial version history"
tags: [ruby, version-history, evolution, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "10 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

-->
# Ruby — バージョン履歴と進化
## タイムライン
|バージョン |年 |主要テーマ |
|----------|------|----------|
| 0.95 | 1995年 |初回リリース (まつもとゆきひろ "Matz") |
| 1.0 | 1996年 |最初の安定版リリース |
| 1.2 | 1998年 |最初の英語ドキュメント |
| 1.4 | 1999年 | `BEGIN`/`END`、`String#unpack`|
| 1.6 | 2000年 |ガベージ コレクションの改善 |
| 1.8 | 2003年 | $KCODE、鬼車正規表現エンジン |
| 1.9 | 2007年 | **主要**: M17N (多言語)、新しいハッシュ構文、ファイバー |
| 2.0 | 2013年 |キーワード引数、`Enumerator::Lazy`、`Module#prepend`|
| 2.1 | 2013年 |洗練されたメソッド呼び出し、`frozen_string_literal` |
| 2.2 | 2014年 |シンボル GC、インクリメンタル GC |
| 2.3 | 2015年 |凍結された文字列リテラル プラグマ、`&.` 安全なナビゲーション |
| 2.4 | 2016年 | `Integer`統合、`String` Unicode ケース マッピング |
| 2.5 | 2017年 | `yield_self`、`rescue`/`ensure`のブロック |
| 2.6 | 2018年 | **JIT コンパイラ (MJIT)**、無限範囲`1..`|
| 2.7 | 2019年 |パターン マッチング (実験的)、番号付きブロック パラメーター |
| 3.0 | 2020年 | **主要**: Ractor (同時実行)、Fibre Scheduler、RBS タイプ |
| 3.1 | 2021年 | `Anonymous`ブロック転送、`Hash#compact` |
| 3.2 | 2022年 | `Data`クラス、`File.realpath` の改善、YJIT 制作 |
| 3.3 | 2023年 | **YJIT** の大幅な改善、`it` ブロック パラメーター |
| 3.4 | 2024年 | Prism パーサーのデフォルト、デフォルトのブロックパラメータとして`it`|
## 主要なマイルストーン
### 初期の Ruby (1995 ～ 2003)
- **1995**: Matz が Ruby を作成 — Perl、Smalltalk、Lisp をブレンドして
- **1.0 (1996)**: 最初の安定版リリース
- **1.8 (2003)**: 「古典的な」Ruby — 高速で安定しており、広く採用されています
### Rails 時代 (2004 ～ 2013 年)
- **2004**: Ruby on Rails リリース — Web 開発革命
- **1.9 (2007)**: M17N (多言語文字列)、新しいハッシュ構文`{key: value}`、ファイバー
- **2.0 (2013)**: キーワード引数、遅延列挙子、`Module#prepend`
### 最新の Ruby (2015–現在)
- **2.6 (2018)**: JIT コンパイラー (MJIT) — 最初のパフォーマンスの向上
- **2.7 (2019)**: パターン マッチング (実験的)、番号付きブロック パラメーター`_1`
- **3.0 (2020)**: **Ractor** (アクター モデルの同時実行)、**ファイバー スケジューラ** (非同期 I/O)、**RBS** (型シグネチャ)
- **3.2 (2022)**:`Data`クラス (不変値オブジェクト)、YJIT 実稼働対応
- **3.3 (2023)**: YJIT の大幅な高速化 (最大 3 倍高速化)、`it` ブロック パラメーター
- **3.4 (2024)**: Prism パーサーがデフォルトになります
## パフォーマンスの進化
```
Ruby 1.8:  Baseline (interpreted)
Ruby 1.9:  ~1.5x faster (YARV bytecode)
Ruby 2.0:  ~1x (focus on features)
Ruby 2.6:  MJIT (experimental JIT)
Ruby 3.0:  Fiber Scheduler (async I/O)
Ruby 3.2:  YJIT (production JIT)
Ruby 3.3:  YJIT 3x faster (Rails benchmarks)
Ruby 3.4:  Prism parser (faster parsing)
Target:    3x faster than Ruby 2.5 (Ruby 3x3 goal)
```

## 同時実行の進化
```
1.8:  Green threads (GIL)
1.9:  Native threads (still GIL)
2.0:  Fiber (cooperative)
2.6:  Fiber Scheduler proposal
3.0:  Ractor (Actor model, no GIL sharing)
3.0:  Fiber Scheduler (async I/O without threads)
3.3:  Improved Fiber Scheduler
```

## パターン マッチングの進化
```
2.7:  Experimental — case/in
3.0:  Improved — pin operator, find pattern
3.1:  One-line pattern matching
3.2:  Shortcut syntax, infinite patterns
3.4:  Pattern matching stabilized
```

## 主要な設計原則
```
1. "MINASWAN" — Matz is nice and so we are nice
2. "Programmer happiness" — surprising is bad
3. "Everything is an object" — even numbers, nil, true
4. "Blocks are fundamental" — closures as first-class
5. "Duck typing" — behavior over type
6. "Convention over configuration" — Rails philosophy
```

## エコシステムの成長
```
2004: Rails launches — Ruby enters mainstream
2005: RubyGems package manager
2006: Ruby wins "Language of the Year" (TIOBE)
2008: Bundler (dependency management)
2010: Ruby 1.9 adoption accelerates
2013: Ruby 2.0 — enterprise adoption
2020: Ruby 3.0 — concurrency revolution
2023: YJIT makes Ruby fast again
2025: Ruby remains top 10; Rails powers GitHub, Shopify, Basecamp, Stripe
```
