<!--
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

-->
# Perl — 版本历史和演变
## 时间轴
|版本 |年份|关键主题 |
|--------|------|------------|
| 1.0 | 1987 |初始版本（拉里·沃尔）|
| 2.0 | 1988 | `study`函数，更好的正则表达式 |
| 3.0 | 1989 | `my`变量（词法范围）|
| 4.0 | 1991 | `O'Reilly`《Programming Perl》（Camel 书）|
| 5.0 | 1994 | **主要**：模块、引用、闭包、`use strict` |
| 5.6 | 5.6 2000 | 2000 `our`、`state`（稍后）、`v-strings`、`y2k`修复 |
| 5.8 | 2002 | **Unicode 支持**、`ithreads`、`open`编译指示 |
| 5.10 | 5.10 2007 | `say`、`//`定义或、`given`/`when`、`~~`智能匹配 |
| 5.12 | 5.12 2010 | `package NAME VERSION`,`...`(yada-yada), Unicode 5.2 |
| 5.14 | 5.14 2011 |  `s///r`（无损替换）、`package` 改进 |
| 5.16 | 5.16 2012 |  `__SUB__`、`unicode_eval` |
| 5.18 | 5.18 2013 |条件中的词法`$_`、哈希随机化、`my` |
| 5.20 | 5.20 2014年| **子程序签名**（实验），`%hash` 切片 |
| 5.22 | 5.22 2015 | 2015 `&`取消引用，`<<>>`（安全打开）|
| 5.24 | 5.24 2016 | 2016 Postfix 取消引用稳定 |
| 5.26 | 5.26 2017 | 2017 **`while` 中的词法`$_`**、`@INC` 中的`.`已删除（安全）|
| 5.28 | 5.28 2018 |键/值切片上的 Unicode 10.0、`delete` |
| 5.30 | 5.30 2019 | 2019 `my`在`for`/`while`条件下 |
| 5.32 | 5.32 2020 | `isa`运算符，Unicode 13.0 |
| 5.34 | 5.34 2021 | `try`/ `catch`（实验）、`defer` 块 |
| 5.36 | 5.36 2022 | 2022 **`use v5.36`**：启用签名，`$_` 默认，`defer` |
| 5.38 | 5.38 2023 | `class`关键字（实验）、`try` /`catch`稳定 |
| 5.40 | 5.40 2024 | 2024 `^`按位运算符、`for` 列表改进 |
| 5.42 | 5.42 2025 | 2025持续发展|
## 主要里程碑
### Perl 1–4：脚本时代（1987–1993）
- **1987**：Larry Wall 发布 Perl —“实用提取和报告语言”
- **目标**：将 sed、awk、grep、shell 组合成一个强大的脚本工具
- **3.0**：词法作用域（`my`）
- **4.0**：The Camel Book — Perl 被广泛应用于系统管理任务
### Perl 5：黄金时代（1994–2019）
- **5.0 (1994)**：完全重写 — **模块**、**引用**、**闭包**、**对象**
- **5.6 (2000)**：`our`，v 弦
- **5.8 (2002)**：**Unicode 支持**，解释器线程 (`ithreads`)
- **5.10 (2007)**：`say`、`//`（定义或）、`given` / `when`（开关）、smartmatch
- **5.12–5.28**：增量改进，Unicode 升级
### 现代 Perl（2020 年至今）
- **5.32 (2020)**：`isa` 运算符（清洁器类型检查）
- **5.34 (2021)**：`try` / `catch`（实验性）、`defer` 块
- **5.36 (2022)**：**`use v5.36`** — 默认启用签名，`$_` 默认启用，`defer` 
- **5.38 (2023)**：`class` 关键字（实验性 — 内置 OOP），`try` /`catch`稳定
- **5.40 (2024)**：按位运算符改进
## 语法演变
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

## CPAN 生态系统
```
1995: CPAN (Comprehensive Perl Archive Network) launched
2000: Module::Build — alternative to MakeMaker
2008: CPANPLUS — enhanced CPAN client
2010: Dist::Zilla — release builder
2012: Carton — dependency pinning (like Bundler)
2013: cpanminus — zero-config CPAN client
2025: CPAN hosts 200,000+ modules from 14,000+ authors
```

## 关键设计原则
```
1. "TMTOWTDI" — There's More Than One Way To Do It
2. "Practical, not pure" — solve real problems
3. "Text processing king" — regex built into the language
4. "Glue language" — connect systems, protocols, formats
5. "Backward compatible" — old Perl code keeps running
6. "Community-driven" — CPAN, Perl Mongers, YAPC conferences
```

## 生态系统增长
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
