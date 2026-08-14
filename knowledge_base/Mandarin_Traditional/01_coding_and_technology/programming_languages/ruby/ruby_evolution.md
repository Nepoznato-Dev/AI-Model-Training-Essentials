---
# Metadata
title: "Ruby — Version History & Evolution"
description: "Comprehensive version history and evolution of Ruby from 1.0 to modern Ruby."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
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

# Ruby — 版本歷史與演變
## 時間軸
|版本 |年份|關鍵主題 |
|--------|------|------------|
| 0.95 | 0.95 1995 |初次發布（松本幸弘「Matz」）|
| 1.0 | 1996 |第一個穩定版本 |
| 1.2 | 1.2 1998 |第一個英文文檔 |
| 1.4 | 1.4 1999 |`BEGIN`/`END`,`String#unpack`|
| 1.6 | 1.6 2000 | 2000垃圾收集改進 |
| 1.8 | 1.8 2003 | $KCODE，oniguruma 正規表示式引擎 |
| 1.9 | 1.9 2007 | **主要**：M17N（多語言）、新的雜湊語法、纖維 |
| 2.0 | 2013 |關鍵字參數、`Enumerator::Lazy`、`Module#prepend`|
| 2.1 | 2.1 2013 |精緻的方法調用，`frozen_string_literal` |
| 2.2 | 2.2 2014 |符號GC、增量GC |
| 2.3 | 2.3 2015 | 2015凍結字串文字雜注，`&.` 安全導航 |
| 2.4 | 2.4 2016 | 2016`Integer`統一，`String` Unicode 大小寫映射 |
| 2.5 | 2.5 2017 | 2017`yield_self`，`rescue` /`ensure`中的區塊 |
| 2.6 | 2.6 2018 | **JIT 編譯器 (MJIT)**，無限範圍`1..`|
| 2.7 | 2.7 2019 | 2019模式匹配（實驗），編號塊參數 |
| 3.0 | 2020 | **主要**：Ractor（併發）、Fiber Scheduler、RBS 類型 |
| 3.1| 2021 |`Anonymous`區塊轉送、`Hash#compact` |
| 3.2 | 2022 | 2022`Data`級、`File.realpath` 改進、YJIT 生產 |
| 3.3 | 2023 | **YJIT**重大改進，`it`區塊參數|
| 3.4 | 3.4 2024 | 2024 Prism 解析器默認，`it` 作為預設區塊參數 |
## 主要里程碑
### 早期紅寶石 (1995–2003)
- **1995**：Matz 建立 Ruby — 混合 Perl、Smalltalk、Lisp
- **1.0 (1996)**：第一個穩定版本
- **1.8 (2003)**：「經典」Ruby — 快速、穩定、廣泛採用
### Rails 時代（2004–2013）
- **2004**：Ruby on Rails 發佈 — Web 開發革命
- **1.9 (2007)**：M17N（多語言字串），新的雜湊語法`{key: value}`，纖維
- **2.0 (2013)**：關鍵字參數、惰性枚舉器、`Module#prepend`
### 現代紅寶石（2015 年至今）
- **2.6 (2018)**：JIT 編譯器 (MJIT) — 首次效能提升
- **2.7 (2019)**：模式匹配（實驗性），編號區塊參數 `_1`
- **3.0 (2020)**：**Ractor**（Actor 模型並發）、**Fiber Scheduler**（非同步 I/O）、**RBS**（型別簽名）
- **3.2 (2022)**：`Data` 類別（非可變值物件），YJIT 生產就緒
- **3.3 (2023)**：YJIT 主要加速（最多快 3 倍），`it` 區塊參數
- **3.4 (2024)**：Prism 解析器成為預設值
## 效能演變
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

## 並發演進
```
1.8:  Green threads (GIL)
1.9:  Native threads (still GIL)
2.0:  Fiber (cooperative)
2.6:  Fiber Scheduler proposal
3.0:  Ractor (Actor model, no GIL sharing)
3.0:  Fiber Scheduler (async I/O without threads)
3.3:  Improved Fiber Scheduler
```

## 模式匹配的演變
```
2.7:  Experimental — case/in
3.0:  Improved — pin operator, find pattern
3.1:  One-line pattern matching
3.2:  Shortcut syntax, infinite patterns
3.4:  Pattern matching stabilized
```

## 關鍵設計原則
```
1. "MINASWAN" — Matz is nice and so we are nice
2. "Programmer happiness" — surprising is bad
3. "Everything is an object" — even numbers, nil, true
4. "Blocks are fundamental" — closures as first-class
5. "Duck typing" — behavior over type
6. "Convention over configuration" — Rails philosophy
```

## 生態系成長
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
