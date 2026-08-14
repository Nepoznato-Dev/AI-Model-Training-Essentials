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
# بيرل — تاريخ الإصدار وتطوره
## الجدول الزمني
| النسخة | سنة | الموضوع الرئيسي |
|---------|------|-----------|
| 1.0 | 1987 | الإصدار الأولي (لاري وول) |
| 2.0 | 1988 |  وظيفة `study`، تعبير عادي أفضل |
| 3.0 | 1989 |  متغيرات`my`(النطاق المعجمي) |
| 4.0 | 1991 | `O'Reilly`"برمجة بيرل" (كتاب الجمل) |
| 5.0 | 1994 | **التخصص**: الوحدات، المراجع، الخاتمات،`use strict`|
| 5.6 | 2000 |  إصلاحات`our`و`state` (أحدث) و`v-strings` و`y2k` |
| 5.8 | 2002 | **دعم Unicode**,`ithreads`,`open`pragma |
| 5.10 | 2007 | `say`,`//`محدد أو`given`/`when`,`~~`تطابق ذكي |
| 5.12 | 2010 |  `package NAME VERSION`،`...`(yada-yada)، Unicode 5.2 |
| 5.14 | 2011 | `s///r`(الاستبدال غير المدمر)، تحسينات`package`|
| 5.16 | 2012 | `__SUB__`,`unicode_eval`|
| 5.18 | 2013 | معجم `$_`، التجزئة العشوائية،`my`في الشروط |
| 5.20 | 2014 | **توقيعات الروتين الفرعي** (تجريبية)، تقطيع`%hash`|
| 5.22 | 2015 |  إلغاء مرجعية `&`،`<<>>`(فتح آمن) |
| 5.24 | 2016 | Postfix إلغاء مرجعية مستقرة |
| 5.26 | 2017 | ** معجمي`$_`في`while`**، تمت إزالة`.`في`@INC`(الأمان) |
| 5.28 | 2018 | Unicode 10.0،`delete`على شرائح المفتاح/القيمة |
| 5.30 | 2019 | `my`في ظروف`for`/`while`|
| 5.32 | 2020 |  مشغل `isa`، Unicode 13.0 |
| 5.34 | 2021 | `try`/`catch`(تجريبي)، كتل`defer`|
| 5.36 | 2022 | **`use v5.36`**: تم تمكين التوقيعات،`$_`الافتراضي،`defer`|
| 5.38 | 2023 |  الكلمة الأساسية`class`(تجريبية)،`try`/`catch`المستقر |
| 5.40 | 2024 |  مشغلي `^`، تحسينات قائمة`for`|
| 5.42 | 2025 | التطوير المستمر |
## المعالم الرئيسية
### بيرل 1-4: عصر البرمجة النصية (1987-1993)
- **1987**: أطلق لاري وول لغة Perl — "الاستخراج العملي ولغة التقرير"
- **الهدف**: الجمع بين sed وawk وgrep وshell في أداة برمجة نصية واحدة قوية
- **3.0**: النطاق المعجمي (`my`)
- **4.0**: The Camel Book — أصبح لغة Perl معتمدة على نطاق واسع في مهام مسؤول النظام
### بيرل 5: العصر الذهبي (1994-2019)
- **5.0 (1994)**: إعادة كتابة كاملة — **الوحدات**، **المراجع**، **الإغلاقات**، **الكائنات**
- **5.6 (2000)**:`our`, v-strings
- **5.8 (2002)**: **دعم Unicode**، سلاسل المترجم (`ithreads`)
- **5.10 (2007)**:`say`,`//`(محدد-أو)،`given`/`when`(التبديل)، التوافق الذكي
- **5.12–5.28**: تحسينات تدريجية وترقيات Unicode
### لغة بيرل الحديثة (2020 إلى الوقت الحاضر)
- **5.32 (2020)**: مشغل`isa`(التحقق من نوع المنظف)
- **5.34 (2021)**:`try`/`catch`(تجريبي)، كتل `defer`
- **5.36 (2022)**: **`use v5.36`** — التوقيعات ممكّنة افتراضيًا،`$_`افتراضيًا،`defer`
- **5.38 (2023)**: الكلمة الرئيسية`class`(تجريبية - OOP مدمجة)،`try`/`catch`المستقر
- **5.40 (2024)**: تحسينات عامل Bitwise
## تطور بناء الجملة
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

## النظام البيئي CPAN
```
1995: CPAN (Comprehensive Perl Archive Network) launched
2000: Module::Build — alternative to MakeMaker
2008: CPANPLUS — enhanced CPAN client
2010: Dist::Zilla — release builder
2012: Carton — dependency pinning (like Bundler)
2013: cpanminus — zero-config CPAN client
2025: CPAN hosts 200,000+ modules from 14,000+ authors
```

## مبادئ التصميم الرئيسية
```
1. "TMTOWTDI" — There's More Than One Way To Do It
2. "Practical, not pure" — solve real problems
3. "Text processing king" — regex built into the language
4. "Glue language" — connect systems, protocols, formats
5. "Backward compatible" — old Perl code keeps running
6. "Community-driven" — CPAN, Perl Mongers, YAPC conferences
```

## نمو النظام البيئي
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
