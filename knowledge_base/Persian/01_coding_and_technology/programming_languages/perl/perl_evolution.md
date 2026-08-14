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

# Perl - تاریخچه نسخه و تکامل
## جدول زمانی
| نسخه | سال | تم کلید |
|---------|------|-----------|
| 1.0 | 1987 | انتشار اولیه (لری وال) |
| 2.0 | 1988 |  تابع `study`، regex بهتر |
| 3.0 | 1989 |  متغیرهای`my`(محدوده لغوی) |
| 4.0 | 1991 | `O'Reilly`"برنامه نویسی پرل" (کتاب شتر) |
| 5.0 | 1994 | **عناوین**: ماژول ها، مراجع، بسته شدن،`use strict`|
| 5.6 | 2000 |  اصلاحات`our`,`state`(بعدها)،`v-strings`,`y2k`|
| 5.8 | 2002 | **پشتیبانی از یونیکد**، `ithreads`،`open`پراگما |
| 5.10 | 2007 | `say`,`//`تعریف شده-یا,`given`/`when`,`~~`هماهنگی هوشمند |
| 5.12 | 2010 | `package NAME VERSION`,`...`(yada-yada), Unicode 5.2 |
| 5.14 | 2011 | `s///r`(جایگزینی غیر مخرب)، بهبود`package`|
| 5.16 | 2012 | `__SUB__`,`unicode_eval`|
| 5.18 | 2013 |`$_`واژگانی، تصادفی سازی هش،`my`به صورت شرطی |
| 5.20 | 2014 | **امضاهای زیر برنامه** (تجربی)، برش`%hash`|
| 5.22 | 2015 | `&`عدم ارجاع،`<<>>`(ایمن باز) |
| 5.24 | 2016 | Postfix عدم ارجاع پایدار |
| 5.26 | 2017 | **واژه نامه`$_`در`while`**،`.`در`@INC`حذف (امنیت) |
| 5.28 | 2018 | Unicode 10.0،`delete`در برش های کلید/مقدار |
| 5.30 | 2019 | `my`در شرایط`for`/`while`|
| 5.32 | 2020 |  اپراتور `isa`، Unicode 13.0 |
| 5.34 | 2021 |  بلوک های`try`/`catch`(تجربی)،`defer`|
| 5.36 | 2022 | **`use v5.36`**: امضاها فعال است، پیش فرض `$_`،`defer`|
| 5.38 | 2023 |  کلمه کلیدی`class`(تجربی)،`try`/`catch`پایدار |
| 5.40 | 2024 |  اپراتورهای بیتی `^`، بهبود لیست`for`|
| 5.42 | 2025 | توسعه در حال انجام |
## نقاط عطف اصلی
### Perl 1–4: The Scripting Era (1987–1993)
- **1987**: لری وال Perl را منتشر کرد - "زبان استخراج و گزارش عملی"
- **هدف**: ترکیب sed، awk، grep، shell در یک ابزار برنامه نویسی قدرتمند
- **3.0**: محدوده واژگانی (`my`)
- **4.0**: کتاب شتر - Perl به طور گسترده برای وظایف sysadmin پذیرفته می شود
### Perl 5: The Golden Age (1994–2019)
- **5.0 (1994)**: بازنویسی کامل - **ماژول**، **مرجع**، **بسته**، **اشیاء**
- **5.6 (2000)**: `our`، رشته های v
- **5.8 (2002)**: **پشتیبانی از یونیکد**، رشته های مفسر (`ithreads`)
- **5.10 (2007)**: `say`،`//`(تعریف شده یا)،`given`/`when`(سوئیچ)، هماهنگی هوشمند
- **5.12–5.28**: بهبودهای افزایشی، ارتقاء یونیکد
### پرل مدرن (2020–اکنون)
- **5.32 (2020)**: اپراتور`isa`(بررسی نوع پاک کننده)
- **5.34 (2021)**: بلوک های`try`/`catch`(تجربی)، `defer`
- **5.36 (2022)**: **`use v5.36`** - امضاها به طور پیش فرض فعال هستند،`$_`پیش فرض،`defer`
- **5.38 (2023)**: کلمه کلیدی`class`(تجربی - OOP داخلی)،`try`/`catch`پایدار
- **5.40 (2024)**: بهبودهای عملگر بیتی
## تکامل نحو
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

## اکوسیستم CPAN
```
1995: CPAN (Comprehensive Perl Archive Network) launched
2000: Module::Build — alternative to MakeMaker
2008: CPANPLUS — enhanced CPAN client
2010: Dist::Zilla — release builder
2012: Carton — dependency pinning (like Bundler)
2013: cpanminus — zero-config CPAN client
2025: CPAN hosts 200,000+ modules from 14,000+ authors
```

## اصول کلیدی طراحی
```
1. "TMTOWTDI" — There's More Than One Way To Do It
2. "Practical, not pure" — solve real problems
3. "Text processing king" — regex built into the language
4. "Glue language" — connect systems, protocols, formats
5. "Backward compatible" — old Perl code keeps running
6. "Community-driven" — CPAN, Perl Mongers, YAPC conferences
```

## رشد اکوسیستم
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
