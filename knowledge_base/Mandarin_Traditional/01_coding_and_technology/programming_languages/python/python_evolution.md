<!--
---
# Metadata
title: "Python — Version History & Evolution"
description: "Comprehensive version history and evolution of Python from 1.x to modern Python."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial version history"
tags: [python, version-history, evolution, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "12 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

-->
# Python — 版本歷史與演變
## 時間軸
|版本 |發佈日期 |關鍵主題 |
|--------|-------------|------------|
| 1.0 | 1994 年 1 月 |首次發布 |
| 1.5 | 1.5 1997 年 12 月 |類、異常、模組 |
| 2.0 | 2000 年 10 月 |列表推導式、垃圾回收 |
| 2.2 | 2.2 2001 年 12 月 |統一型別（型/類）、產生器 |
| 2.5 | 2.5 2006 年 9 月 |`with`語句，`yield` 作為表達式 |
| 2.6 | 2.6 2008 年 10 月 |`bytes`、`future`導入，過渡到 3 |
| 2.7 | 2.7 2010 年 7 月 |字典/集合理解，`argparse` |
| 3.0 | 2008 年 12 月 | **突破**：`print()`、`str`/`bytes`、迭代器 |
| 3.3 | 2012 年 9 月 | `yield from`，命名空間包 |
| 3.4 | 3.4 2014 年 3 月 | `asyncio`、`pathlib`、`enum` |
| 3.5 | 3.5 2015 年 9 月 |`async/await`，類型提示 (PEP 484)，`**` 拆包 |
| 3.6 | 2016 年 12 月 | f 字串、`async` compreh、有序字典 |
| 3.7 | 3.7 2018 年 6 月 |`dataclasses`、`contextvars`、保留`async`|
| 3.8 | 2019 年 10 月 | Walrus 運算子`:=`，僅位置參數 |
| 3.9 | 3.9 2020 年 10 月 |字典聯合`|`，泛型型`list[int]`|
| 3.10 | 3.10 2021 年 10 月 | `match/case`，結構模式匹配|
| 3.11 | 3.11 2022 年 10 月 |異常組，`Self` 類型，更快的 CPython |
| 3.12 | 3.12 2023 年 10 月 |每個解釋器的 GIL 準備，類型參數語法 |
| 3.13 | 3.13 2024 年 10 月 |自由線程模式（實驗性），改進的 REPL |
| 3.14 | 3.14 2025 年 10 月 | No-GIL 穩定、延遲評估註釋 |
## 主要里程碑
### Python 2.x 時代（2000–2020）
- **2.0**：受 Haskell 啟發的列表推導式；循環氣相層析
- **2.2**：`object` 基底類別；`yield`關鍵字（產生器）
- **2.5**：`with` 語句；`yield`成為表達式
- **2.7**：最終 2.x 版本；聽寫理解； `argparse`
- **生命週期結束**：2020 年 1 月 1 日
### Python 3.x 革命（2008 年至今）
- **3.0**：徹底打破 -`print`作為函數，`str`與`bytes`，所有迭代器返回視圖
- **3.5**：`async` /`await`語法；使用`typing`模組的型別提示
- **3.6**：f-strings（最需要的功能）；`asyncio`穩定
- **3.8**：用於內嵌賦值的海象運算符
- **3.10**：結構模式匹配（`match`/`case`）
- **3.11**：速度提高 10-60%；帶有`except*`的例外組
- **3.13**：實驗性自由執行緒模式（無 GIL）
## 設計理念的演變
```
1994: "There should be one — and preferably only one — obvious way to do it"
2004: "Batteries included" (extensive stdlib)
2011: "Beautiful is better than ugly" (Zen of Python, PEP 20)
2015: Gradual typing accepted (Guido's compromise)
2018: "Black" formatter — consistency over preference
2023: Performance becomes priority (faster CPython, Shannon plan)
```

## 塑造 Python 的關鍵 PEP
|政治公眾人物 |年份|特色 |
|------|------|---------|
| 20 | 2004 | Python之禪 |
| 257 | 257 2001 |文檔字串約定 |
| 279 | 279 2002 |`enumerate()`|
| 289 | 289 2002 |生成器表達式 |
| 342 | 342 2005 |`yield`作為表達式，`send()` |
| 380 | 380 2009 |`yield from`|
| 484 | 484 2014年|型別提示 |
| 492 | 492 2014 |`async`/`await`|
| 498 | 498 2015 | 2015 f 弦 |
| 572 | 572 2018 |海像操作員`:=`|
| 622 | 622 2020 |結構模式匹配 |
| 654 | 654 2021 |例外群體|
| 684 | 684 2022 | 2022每位口譯員 GIL |
| 703 | 703 2023 |使 GIL 成為可選 |
## 效能演變
```
Python 3.10:  baseline
Python 3.11:  ~1.25x faster (Faster CPython project)
Python 3.12:  ~1.3x faster (specializing adaptive interpreter)
Python 3.13:  ~1.4x faster (JIT compiler experiment)
Target 3.14:  5x faster than 3.10 (Shannon plan goal)
```

## 社區和生態系統的發展
```
2004: PyPI launches (7,000+ packages by 2010)
2008: First PyCon (300 attendees)
2012: pip replaces easy_install
2018: Python overtakes Java in popularity (Stack Overflow)
2020: Python 2 end-of-life; 3.x migration completes
2023: 500,000+ packages on PyPI
2025: #1 most used language (multiple surveys)
```
