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
# Perl - Historia ya Toleo na Mageuzi
## Rekodi ya matukio
| Toleo | Mwaka | Mandhari Muhimu |
|---------|------|-----------|
| 1.0 | 1987 | Toleo la awali (Larry Wall) |
| 2.0 | 1988 | `study`kazi, bora regex |
| 3.0 | 1989 |  Vigezo vya`my`(upeo wa kileksia) |
| 4.0 | 1991 | `O'Reilly`"Programming Perl" (Kitabu cha ngamia) |
| 5.0 | 1994 | **Kubwa**: moduli, marejeleo, kufungwa,`use strict`|
| 5.6 | 2000 | `our`,`state`(baadaye),`v-strings`,`y2k`marekebisho |
| 5.8 | 2002 | **Usaidizi wa Unicode**,`ithreads`,`open`pragma |
| 5.10 | 2007 | `say`,`//`imefafanuliwa-au,`given`/`when`,`~~`smartmatch |
| 5.12 | 2010 | `package NAME VERSION`,`...`(yada-yada), Unicode 5.2 |
| 5.14 | 2011 | `s///r`(badala isiyoharibu),`package`maboresho |
| 5.16 | 2012 | `__SUB__`,`unicode_eval`|
| 5.18 | 2013 | Lexical`$_`, ubahatishaji wa hashi,`my`katika masharti |
| 5.20 | 2014 | **Saini ndogo** (majaribio),`%hash`kukatwa |
| 5.22 | 2015 | `&`dereferencing,`<<>>`(imefunguliwa salama) |
| 5.24 | 2016 | Postfix dereferencing imara |
| 5.26 | 2017 | **`$_` ya Leksika katika`while`**,`.`katika`@INC`imeondolewa (usalama) |
| 5.28 | 2018 | Unicode 10.0,`delete`kwenye vipande muhimu/thamani |
| 5.30 | 2019 | `my`katika`for`/`while`masharti |
| 5.32 | 2020 |  Opereta wa `isa`, Unicode 13.0 |
| 5.34 | 2021 | `try`/`catch`(majaribio),`defer`vitalu |
| 5.36 | 2022 | **`use v5.36`**: saini zimewezeshwa,`$_`chaguo-msingi,`defer`|
| 5.38 | 2023 | `class`neno kuu (majaribio),`try`/`catch`thabiti |
| 5.40 | 2024 | `^`waendeshaji kidogo,`for`uboreshaji wa orodha |
| 5.42 | 2025 | Maendeleo yanayoendelea |
## Mafanikio Makuu
### Perl 1–4: Enzi ya Maandishi (1987–1993)
- **1987**: Larry Wall atoa Perl — "Uchimbaji Vitendo na Lugha ya Ripoti"
- **Lengo**: Changanya sed, awk, grep, shell kwenye zana moja yenye nguvu ya uandishi
- **3.0**: Upeo wa Lexical (`my`)
- **4.0**: Kitabu cha Ngamia - Perl inakubaliwa sana kwa kazi za sysadmin
### Perl 5: The Golden Age (1994–2019)
- **5.0 (1994)**: Kamilisha kuandika upya — **moduli**, **marejeleo**, **kufungwa**, **vitu**
- **5.6 (2000)**:`our`, v-strings
- **5.8 (2002)**: **Msaada wa Unicode**, nyuzi za mkalimani (`ithreads`)
- **5.10 (2007)**:`say`,`//`(imefafanuliwa-au),`given`/`when`(switch), smartmatch
- **5.12–5.28**: Maboresho ya ziada, uboreshaji wa Unicode
### Modern Perl (2020–sasa)
- **5.32 (2020)**: Opereta wa`isa`(kuangalia aina safi)
- **5.34 (2021)**:`try`/`catch`(majaribio),`defer`vitalu
- **5.36 (2022)**: **`use v5.36`** — saini zimewezeshwa kwa chaguo-msingi,`$_`chaguomsingi,`defer`
- **5.38 (2023)**:`class`neno kuu (majaribio - iliyojengwa ndani OOP),`try`/`catch`thabiti
- **5.40 (2024)**: Maboresho ya waendeshaji Bitwise
## Mageuzi ya Sintaksia
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

## Mfumo ikolojia wa CPAN
```
1995: CPAN (Comprehensive Perl Archive Network) launched
2000: Module::Build — alternative to MakeMaker
2008: CPANPLUS — enhanced CPAN client
2010: Dist::Zilla — release builder
2012: Carton — dependency pinning (like Bundler)
2013: cpanminus — zero-config CPAN client
2025: CPAN hosts 200,000+ modules from 14,000+ authors
```

## Kanuni Muhimu za Usanifu
```
1. "TMTOWTDI" — There's More Than One Way To Do It
2. "Practical, not pure" — solve real problems
3. "Text processing king" — regex built into the language
4. "Glue language" — connect systems, protocols, formats
5. "Backward compatible" — old Perl code keeps running
6. "Community-driven" — CPAN, Perl Mongers, YAPC conferences
```

## Ukuaji wa Mfumo ikolojia
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
