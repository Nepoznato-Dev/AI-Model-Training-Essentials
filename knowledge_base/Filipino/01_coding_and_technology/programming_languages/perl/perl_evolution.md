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

# Perl — Kasaysayan ng Bersyon at Ebolusyon
## Timeline
| Bersyon | Taon | Pangunahing Tema |
|---------|------|-----------|
| 1.0 | 1987 | Paunang paglabas (Larry Wall) |
| 2.0 | 1988 | `study`function, mas magandang regex |
| 3.0 | 1989 | `my`variable (lexical scoping) |
| 4.0 | 1991 | `O'Reilly`"Programming Perl" (Camel book) |
| 5.0 | 1994 | **Major**: mga module, sanggunian, pagsasara,`use strict`|
| 5.6 | 2000 | `our`,`state`(mamaya),`v-strings`,`y2k`mga pag-aayos |
| 5.8 | 2002 | **Suporta sa Unicode**,`ithreads`,`open`pragma |
| 5.10 | 2007 | `say`,`//`tinukoy-o,`given`/`when`,`~~`smartmatch |
| 5.12 | 2010 | `package NAME VERSION`,`...`(yada-yada), Unicode 5.2 |
| 5.14 | 2011 | `s///r`(hindi mapanirang pagpapalit),`package`mga pagpapabuti |
| 5.16 | 2012 | `__SUB__`,`unicode_eval`|
| 5.18 | 2013 | Lexical`$_`, hash randomization,`my`sa mga kondisyon |
| 5.20 | 2014 | **Mga subroutine signature** (pang-eksperimento),`%hash`slicing |
| 5.22 | 2015 | `&`dereferencing,`<<>>`(ligtas na bukas) |
| 5.24 | 2016 | Postfix dereferencing stable |
| 5.26 | 2017 | **Lexical`$_`sa`while`**,`.`sa`@INC`inalis (seguridad) |
| 5.28 | 2018 | Unicode 10.0,`delete`sa key/value slices |
| 5.30 | 2019 | `my`sa`for`/`while`kundisyon |
| 5.32 | 2020 | `isa`operator, Unicode 13.0 |
| 5.34 | 2021 | `try`/`catch`(pang-eksperimento),`defer`block |
| 5.36 | 2022 | **`use v5.36`**: pinagana ang mga lagda,`$_`default,`defer`|
| 5.38 | 2023 | `class`keyword (pang-eksperimento),`try`/`catch`matatag |
| 5.40 | 2024 | `^`bitwise operator,`for`listahan ng mga pagpapabuti |
| 5.42 | 2025 | Patuloy na pag-unlad |
## Mga Pangunahing Milestone
### Perl 1–4: The Scripting Era (1987–1993)
- **1987**: Inilabas ni Larry Wall ang Perl — "Practical Extraction at Report Language"
- **Layunin**: Pagsamahin ang sed, awk, grep, shell sa isang mahusay na tool sa pag-script
- **3.0**: Lexical scoping (`my`)
- **4.0**: The Camel Book — Ang Perl ay naging malawak na pinagtibay para sa mga gawaing sysadmin
### Perl 5: The Golden Age (1994–2019)
- **5.0 (1994)**: Kumpletuhin ang muling pagsulat — **mga module**, **mga sanggunian**, **mga pagsasara**, **mga bagay**
- **5.6 (2000)**:`our`, v-strings
- **5.8 (2002)**: **Suporta sa Unicode**, mga interpreter thread (`ithreads`)
- **5.10 (2007)**:`say`,`//`(defined-o),`given`/`when`(switch), smartmatch
- **5.12–5.28**: Mga incremental na pagpapabuti, Unicode upgrade
### Modern Perl (2020–kasalukuyan)
- **5.32 (2020)**:`isa`operator (mas malinis na uri ng pagsusuri)
- **5.34 (2021)**:`try`/`catch`(pang-eksperimento),`defer`block
- **5.36 (2022)**: **`use v5.36`** — pinagana ang mga lagda bilang default,`$_`default,`defer`
- **5.38 (2023)**:`class`keyword (pang-eksperimento — built-in na OOP),`try`/`catch`stable
- **5.40 (2024)**: Mga pagpapahusay sa bitwise operator
## Syntax Evolution
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

## Ecosystem ng CPAN
```
1995: CPAN (Comprehensive Perl Archive Network) launched
2000: Module::Build — alternative to MakeMaker
2008: CPANPLUS — enhanced CPAN client
2010: Dist::Zilla — release builder
2012: Carton — dependency pinning (like Bundler)
2013: cpanminus — zero-config CPAN client
2025: CPAN hosts 200,000+ modules from 14,000+ authors
```

## Pangunahing Prinsipyo ng Disenyo
```
1. "TMTOWTDI" — There's More Than One Way To Do It
2. "Practical, not pure" — solve real problems
3. "Text processing king" — regex built into the language
4. "Glue language" — connect systems, protocols, formats
5. "Backward compatible" — old Perl code keeps running
6. "Community-driven" — CPAN, Perl Mongers, YAPC conferences
```

## Paglago ng Ecosystem
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
