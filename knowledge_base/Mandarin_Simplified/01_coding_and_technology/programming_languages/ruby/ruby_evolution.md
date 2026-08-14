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
# Ruby — 版本历史和演变
## 时间轴
|版本 |年份|关键主题 |
|--------|------|------------|
| 0.95 | 0.95 1995 |初次发布（松本幸弘“Matz”）|
| 1.0 | 1996 |第一个稳定版本 |
| 1.2 | 1.2 1998 |第一个英文文档 |
| 1.4 | 1.4 1999 | `BEGIN`/`END`,`String#unpack`|
| 1.6 | 1.6 2000 | 2000垃圾收集改进 |
| 1.8 | 1.8 2003 | $KCODE，oniguruma 正则表达式引擎 |
| 1.9 | 1.9 2007 | **主要**：M17N（多语言）、新的哈希语法、纤维 |
| 2.0 | 2013 |关键字参数、`Enumerator::Lazy`、`Module#prepend`|
| 2.1 | 2.1 2013 |精致的方法调用，`frozen_string_literal` |
| 2.2 | 2.2 2014年|符号GC、增量GC |
| 2.3 | 2.3 2015 | 2015冻结字符串文字杂注，`&.` 安全导航 |
| 2.4 | 2.4 2016 | 2016 `Integer`统一，`String` Unicode 大小写映射 |
| 2.5 | 2.5 2017 | 2017 `yield_self`，`rescue` /`ensure`中的块 |
| 2.6 | 2.6 2018 | **JIT 编译器 (MJIT)**，无限范围`1..`|
| 2.7 | 2.7 2019 | 2019模式匹配（实验），编号块参数 |
| 3.0 | 2020 | **主要**：Ractor（并发）、Fiber Scheduler、RBS 类型 |
| 3.1| 2021 | `Anonymous`块转发、`Hash#compact` |
| 3.2 | 2022 | 2022 `Data`级、`File.realpath` 改进、YJIT 生产 |
| 3.3 | 2023 | **YJIT**重大改进，`it`块参数|
| 3.4 | 3.4 2024 | 2024 Prism 解析器默认，`it` 作为默认块参数 |
## 主要里程碑
### 早期红宝石 (1995–2003)
- **1995**：Matz 创建 Ruby — 混合 Perl、Smalltalk、Lisp
- **1.0 (1996)**：第一个稳定版本
- **1.8 (2003)**：“经典”Ruby — 快速、稳定、广泛采用
### Rails 时代（2004–2013）
- **2004**：Ruby on Rails 发布 — Web 开发革命
- **1.9 (2007)**：M17N（多语言字符串），新的哈希语法`{key: value}`，纤维
- **2.0 (2013)**：关键字参数、惰性枚举器、`Module#prepend`
### 现代红宝石（2015 年至今）
- **2.6 (2018)**：JIT 编译器 (MJIT) — 首次性能提升
- **2.7 (2019)**：模式匹配（实验性），编号块参数`_1`
- **3.0 (2020)**：**Ractor**（Actor 模型并发）、**Fiber Scheduler**（异步 I/O）、**RBS**（类型签名）
- **3.2 (2022)**：`Data` 类（不可变值对象），YJIT 生产就绪
- **3.3 (2023)**：YJIT 主要加速（最多快 3 倍），`it` 块参数
- **3.4 (2024)**：Prism 解析器成为默认值
## 性能演变
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

## 并发演进
```
1.8:  Green threads (GIL)
1.9:  Native threads (still GIL)
2.0:  Fiber (cooperative)
2.6:  Fiber Scheduler proposal
3.0:  Ractor (Actor model, no GIL sharing)
3.0:  Fiber Scheduler (async I/O without threads)
3.3:  Improved Fiber Scheduler
```

## 模式匹配的演变
```
2.7:  Experimental — case/in
3.0:  Improved — pin operator, find pattern
3.1:  One-line pattern matching
3.2:  Shortcut syntax, infinite patterns
3.4:  Pattern matching stabilized
```

## 关键设计原则
```
1. "MINASWAN" — Matz is nice and so we are nice
2. "Programmer happiness" — surprising is bad
3. "Everything is an object" — even numbers, nil, true
4. "Blocks are fundamental" — closures as first-class
5. "Duck typing" — behavior over type
6. "Convention over configuration" — Rails philosophy
```

## 生态系统增长
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
