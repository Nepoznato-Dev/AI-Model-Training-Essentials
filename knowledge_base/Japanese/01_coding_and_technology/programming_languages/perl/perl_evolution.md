---
# Metadata
title: "Perl — Version History & Evolution"
description: "Comprehensive version history and evolution of Perl from 1.0 to modern Perl."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
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

# Perl — バージョン履歴と進化
## タイムライン
|バージョン |年 |主要テーマ |
|----------|------|----------|
| 1.0 | 1987年 |初期リリース (ラリー・ウォール) |
| 2.0 | 1988年 | `study`関数、より良い正規表現 |
| 3.0 | 1989年 | `my`変数 (字句スコープ) |
| 4.0 | 1991年 | `O'Reilly`『プログラミング Perl』 (ラクダ本) |
| 5.0 | 1994年 | **主要**: モジュール、リファレンス、クロージャ、`use strict` |
| 5.6 | 2000年 | `our`、`state`(後で)、`v-strings`、`y2k`の修正 |
| 5.8 | 2002年 | **Unicode サポート**、`ithreads`、`open`プラグマ |
| 5.10 | 2007年 | `say`、`//`定義 - または、`given`/`when`、`~~`スマートマッチ |
| 5.12 | 2010年 | `package NAME VERSION`、`...`(ヤダヤダ)、Unicode 5.2 |
| 5.14 | 2011年 | `s///r`(非破壊置換)、`package` の改善 |
| 5.16 | 2012年 |  `__SUB__`、`unicode_eval` |
| 5.18 | 2013年 |字句`$_`、ハッシュのランダム化、条件文の`my`|
| 5.20 | 2014年 | **サブルーチン署名** (実験的)、`%hash` スライス |
| 5.22 | 2015年 | `&`逆参照、`<<>>` (セーフ オープン) |
| 5.24 | 2016年 | Postfix の逆参照は安定しています |
| 5.26 | 2017年 | **`while` の字句`$_`**、`@INC` の`.`が削除されました (セキュリティ) |
| 5.28 | 2018年 | Unicode 10.0、キー/値スライスの`delete`|
| 5.30 | 2019年 | `for`/`while`条件の`my`|
| 5.32 | 2020年 | `isa`演算子、Unicode 13.0 |
| 5.34 | 2021年 | `try`/`catch`(実験的)、`defer` ブロック |
| 5.36 | 2022年 | **`use v5.36`**: 署名は有効、`$_` はデフォルト、`defer` |
| 5.38 | 2023年 | `class`キーワード (実験的)、`try` /`catch`安定版 |
| 5.40 | 2024年 | `^`ビット演算子、`for` リストの改善 |
| 5.42 | 2025年 |進行中の開発 |
## 主要なマイルストーン
### Perl 1 ～ 4: スクリプト時代 (1987 ～ 1993 年)
- **1987**: Larry Wall が Perl をリリース — 「実用的な抽出およびレポート言語」
- **目標**: sed、awk、grep、shell を 1 つの強力なスクリプト ツールに結合します。
- **3.0**: 字句スコープ (`my`)
- **4.0**: The Camel Book — Perl がシステム管理タスクに広く採用される
### Perl 5: 黄金時代 (1994 ～ 2019)
- **5.0 (1994)**: 完全な書き直し — **モジュール**、**参照**、**クロージャ**、**オブジェクト**
- **5.6 (2000)**:`our`、v-strings
- **5.8 (2002)**: **Unicode サポート**、インタプリタ スレッド (`ithreads`)
- **5.10 (2007)**:`say`、`//`(定義済みまたは)、`given`/`when`(スイッチ)、スマートマッチ
- **5.12–5.28**: 段階的な改善、Unicode のアップグレード
### モダン Perl (2020–現在)
- **5.32 (2020)**:`isa`演算子 (クリーナー タイプのチェック)
- **5.34 (2021)**:`try`/`catch`(実験的)、`defer` ブロック
- **5.36 (2022)**: **`use v5.36`** — 署名はデフォルトで有効、`$_` デフォルト、`defer` 
- **5.38 (2023)**:`class`キーワード (実験的 - 組み込み OOP)、`try` /`catch`安定版
- **5.40 (2024)**: ビット単位の演算子の改善
## 構文の進化
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

## CPAN エコシステム
```
1995: CPAN (Comprehensive Perl Archive Network) launched
2000: Module::Build — alternative to MakeMaker
2008: CPANPLUS — enhanced CPAN client
2010: Dist::Zilla — release builder
2012: Carton — dependency pinning (like Bundler)
2013: cpanminus — zero-config CPAN client
2025: CPAN hosts 200,000+ modules from 14,000+ authors
```

## 主要な設計原則
```
1. "TMTOWTDI" — There's More Than One Way To Do It
2. "Practical, not pure" — solve real problems
3. "Text processing king" — regex built into the language
4. "Glue language" — connect systems, protocols, formats
5. "Backward compatible" — old Perl code keeps running
6. "Community-driven" — CPAN, Perl Mongers, YAPC conferences
```

## エコシステムの成長
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
