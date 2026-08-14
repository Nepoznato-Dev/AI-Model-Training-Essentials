---
# Metadata
title: "Perl — Version History & Evolution"
description: "Comprehensive version history and evolution of Perl from 1.0 to modern Perl."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial version history"
tags: [perl, version-history, evolution, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "10 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---
# Perl — 版本歷史與演變
## 時間軸
|版本 |年份|關鍵主題 |
|--------|------|------------|
| 1.0 | 1987 |初始版本（拉里·沃爾）|
| 2.0 | 1988 |`study`函數，更好的正規表示式 |
| 3.0 | 1989 |`my`變數（詞法範圍）|
| 4.0 | 1991 |`O'Reilly`《Programming Perl》（Camel 書）|
| 5.0 | 1994 | **主要**：模組、引用、閉包、`use strict` |
| 5.6 | 5.6 2000 | 2000`our`、`state`（稍後）、`v-strings`、`y2k`修復 |
| 5.8 | 2002 | **Unicode 支援**、`ithreads`、`open`編譯指示 |
| 5.10 | 5.10 2007 |`say`、`//`定義或、`given`/`when`、`~~`智慧匹配 |
| 5.12 | 5.12 2010 |`package NAME VERSION`,`...`(yada-yada), Unicode 5.2 |
| 5.14 | 5.14 2011 | `s///r`（無損替換）、`package` 改進 |
| 5.16 | 5.16 2012 | `__SUB__`、`unicode_eval` |
| 5.18 | 5.18 2013 |條件中的詞法`$_`、哈希隨機化、`my` |
| 5.20 | 5.20 2014年| **子程式簽名**（實驗），`%hash` 切片 |
| 5.22 | 5.22 2015 | 2015`&`取消引用，`<<>>`（安全開啟）|
| 5.24 | 5.24 2016 | 2016 Postfix 取消引用穩定 |
| 5.26 | 5.26 2017 | 2017 **`while` 中的詞法`$_`**、`@INC` 中的`.`已刪除（安全）|
| 5.28 | 5.28 2018 |鍵/值切片上的 Unicode 10.0、`delete` |
| 5.30 | 5.30 2019 | 2019`my`在`for`/`while`條件下 |
| 5.32 | 5.32 2020 |`isa`運算符，Unicode 13.0 |
| 5.34 | 5.34 2021 |`try`/ `catch`（實驗）、`defer` 區塊 |
| 5.36 | 5.36 2022 | 2022 **`use v5.36`**：啟用簽名，`$_` 默認，`defer` |
| 5.38 | 5.38 2023 |`class`關鍵字（實驗）、`try` /`catch`穩定 |
| 5.40 | 5.40 2024 | 2024`^`位元運算子、`for` 清單改進 |
| 5.42 | 5.42 2025 | 2025持續發展|
## 主要里程碑
### Perl 1–4：腳本時代（1987–1993）
- **1987**：Larry Wall 發佈 Perl —“實用提取和報告語言”
- **目標**：將 sed、awk、grep、shell 組合成一個強大的腳本工具
- **3.0**：詞法作用域（`my`）
- **4.0**：The Camel Book — Perl 被廣泛應用於系統管理任務
### Perl 5：黃金時代（1994–2019）
- **5.0 (1994)**：完全重寫 — **模組**、**引用**、**閉包**、**物件**
- **5.6 (2000)**：`our`，v 弦
- **5.8 (2002)**：**Unicode 支援**，解釋器執行緒 (`ithreads`)
- **5.10 (2007)**：`say`、`//`（定義或）、`given` / `when`（開關）、smartmatch
- **5.12–5.28**：漸進式改進，Unicode 升級
### 現代 Perl（2020 年至今）
- **5.32 (2020)**：`isa` 運算子（清潔器類型檢查）
- **5.34 (2021)**：`try` / `catch`（實驗性）、`defer` 區塊
- **5.36 (2022)**：**`use v5.36`** — 預設啟用簽名，`$_` 預設啟用，`defer`
- **5.38 (2023)**：`class` 關鍵字（實驗性 — 內建 OOP），`try` /`catch`穩定
- **5.40 (2024)**：位元運算子改進
## 語法演變
```perl
# Perl 1-4: Basic scripting
#!/usr/bin/perl
$name = "World";
print "Hello, $name\n";

# Perl 5.0: References, closures, modules
use strict;
use warnings;
my $greeting = sub { "Hello, $_[0]" };
print $greeting->("World");

# Perl 5.8: Unicode
use utf8;
my $text = "café";

# Perl 5.10: say, defined-or
use v5.10;
say "Hello!";
my $value = $input // 'default';

# Perl 5.20: Subroutine signatures (experimental)
use experimental 'signatures';
sub greet ($name, $greeting = "Hello") {
    say "$greeting, $name!";
}

# Perl 5.36: Modern Perl
use v5.36;
sub greet ($name, $greeting = "Hello") {
    say "$greeting, $name!";
}

# Perl 5.38: class keyword (experimental)
use experimental 'class';
class Dog {
    field $name :param;
    field $breed :param;
    method bark { say "$name says Woof!" }
}
my $dog = Dog->new(name => "Rex", breed => "Lab");
```

## CPAN 生態系統
```
1995: CPAN (Comprehensive Perl Archive Network) launched
2000: Module::Build — alternative to MakeMaker
2008: CPANPLUS — enhanced CPAN client
2010: Dist::Zilla — release builder
2012: Carton — dependency pinning (like Bundler)
2013: cpanminus — zero-config CPAN client
2025: CPAN hosts 200,000+ modules from 14,000+ authors
```

## 關鍵設計原則
```
1. "TMTOWTDI" — There's More Than One Way To Do It
2. "Practical, not pure" — solve real problems
3. "Text processing king" — regex built into the language
4. "Glue language" — connect systems, protocols, formats
5. "Backward compatible" — old Perl code keeps running
6. "Community-driven" — CPAN, Perl Mongers, YAPC conferences
```

## 生態系成長
```
1987: Perl 1.0 — sysadmin scripting
1994: Perl 5.0 — modules, OOP, the web CGI era
1995: CPAN launched — module ecosystem
2000: Perl powers the early web (CGI scripts)
2002: Perl 5.8 — Unicode, ithreads
2005: Catalyst, Dancer — web frameworks
2007: Perl 5.10 — modern syntax additions
2010: Moose — modern OOP (meta-object protocol)
2022: Perl 5.36 — modern defaults
2025: Perl still powers sysadmin, bioinformatics, legacy web apps
       CPAN: 200,000+ modules; used by cPanel, DuckDuckGo
```
