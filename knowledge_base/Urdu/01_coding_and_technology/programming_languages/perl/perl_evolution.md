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
# پرل - ورژن کی تاریخ اور ارتقاء
## ٹائم لائن
| ورژن | سال | کلیدی تھیم |
|---------|------|------------|
| 1.0 | 1987 | ابتدائی ریلیز (لیری وال) |
| 2.0 | 1988 | `study`فنکشن، بہتر ریجیکس |
| 3.0 | 1989 | `my`متغیرات (لغوی اسکوپنگ) |
| 4.0 | 1991 | `O'Reilly`"پروگرامنگ پرل" (اونٹ کی کتاب) |
| 5.0 | 1994 | **بڑا**: ماڈیولز، حوالہ جات، بندش،`use strict`|
| 5.6 | 2000 | `our`,`state`(بعد میں),`v-strings`,`y2k`اصلاحات |
| 5.8 | 2002 | **یونیکوڈ سپورٹ**،`ithreads`,`open`پراگما |
| 5.10 | 2007 | `say`,`//`defined-یا,`given`/`when`,`~~`سمارٹ میچ |
| 5.12 | 2010 | `package NAME VERSION`,`...`(yada-yada), Unicode 5.2 |
| 5.14 | 2011 | `s///r`(غیر تباہ کن متبادل)،`package`بہتری |
| 5.16 | 2012 | `__SUB__`,`unicode_eval`|
| 5.18 | 2013 | لغوی`$_`, hash randomization,`my`مشروط میں |
| 5.20 | 2014 | **سب روٹین دستخط** (تجرباتی)،`%hash`سلائسنگ |
| 5.22 | 2015 | `&`dereferencing,`<<>>`(محفوظ کھلا) |
| 5.24 | 2016 | پوسٹ فکس ڈیریفرنسنگ مستحکم |
| 5.26 | 2017 | **`while` میں Lexical`$_`**،`.`میں`@INC`ہٹا دیا گیا (سیکیورٹی) |
| 5.28 | 2018 | یونیکوڈ 10.0،`delete`کلید/قدر کے ٹکڑوں پر |
| 5.30 | 2019 | `my``for` /`while`حالات میں |
| 5.32 | 2020 | `isa`آپریٹر، یونیکوڈ 13.0 |
| 5.34 | 2021 | `try`/`catch`(تجرباتی)،`defer`بلاکس |
| 5.36 | 2022 | **`use v5.36`**: دستخط فعال،`$_`ڈیفالٹ،`defer`|
| 5.38 | 2023 | `class`مطلوبہ الفاظ (تجرباتی)،`try`/`catch`مستحکم |
| 5.40 | 2024 | `^`بٹ وائز آپریٹرز،`for`فہرست میں بہتری |
| 5.42 | 2025 | جاری ترقی |
## اہم سنگ میل
### پرل 1–4: اسکرپٹنگ ایرا (1987–1993)
- **1987**: لیری وال نے پرل کو جاری کیا - "عملی نکالنے اور رپورٹ کی زبان"
- **مقصد**: sed، awk، grep، shell کو ایک طاقتور اسکرپٹنگ ٹول میں یکجا کریں
- **3.0**: لغوی اسکوپنگ (`my`)
- **4.0**: دی کیمل بک - پرل کو سیسڈمین کے کاموں کے لیے بڑے پیمانے پر اپنایا جاتا ہے۔
### پرل 5: گولڈن ایج (1994–2019)
- **5.0 (1994)**: مکمل دوبارہ لکھنا — **ماڈیول**، **حوالہ جات**، **بند ہونے**، **آبجیکٹ**
- **5.6 (2000)**:`our`, v-strings
- **5.8 (2002)**: **یونیکوڈ سپورٹ**، انٹرپریٹر تھریڈز (`ithreads`)
- **5.10 (2007)**: `say`،`//`(تعریف شدہ-یا)،`given`/`when`(سوئچ)، اسمارٹ میچ
- **5.12–5.28**: بڑھتی ہوئی بہتری، یونیکوڈ اپ گریڈ
### ماڈرن پرل (2020–موجودہ)
- **5.32 (2020)**:`isa`آپریٹر (کلینر ٹائپ چیکنگ)
- **5.34 (2021)**:`try`/`catch`(تجرباتی)،`defer`بلاکس
- **5.36 (2022)**: **`use v5.36`** — دستخط بطور ڈیفالٹ،`$_`ڈیفالٹ،`defer`
- **5.38 (2023)**:`class`کلیدی لفظ (تجرباتی — بلٹ ان OOP)،`try`/`catch`مستحکم
- **5.40 (2024): Bitwise آپریٹر کی بہتری
## نحوی ارتقاء
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

## CPAN ایکو سسٹم
```
1995: CPAN (Comprehensive Perl Archive Network) launched
2000: Module::Build — alternative to MakeMaker
2008: CPANPLUS — enhanced CPAN client
2010: Dist::Zilla — release builder
2012: Carton — dependency pinning (like Bundler)
2013: cpanminus — zero-config CPAN client
2025: CPAN hosts 200,000+ modules from 14,000+ authors
```

## ڈیزائن کے کلیدی اصول
```
1. "TMTOWTDI" — There's More Than One Way To Do It
2. "Practical, not pure" — solve real problems
3. "Text processing king" — regex built into the language
4. "Glue language" — connect systems, protocols, formats
5. "Backward compatible" — old Perl code keeps running
6. "Community-driven" — CPAN, Perl Mongers, YAPC conferences
```

## ماحولیاتی نظام کی نمو
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
