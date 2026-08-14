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

# Perl – Versionsgeschichte und Entwicklung
## Zeitleiste
| Version | Jahr | Schlüsselthema |
|---------|------|-----------|
| 1,0 | 1987 | Erstveröffentlichung (Larry Wall) |
| 2,0 | 1988 |  `study`-Funktion, besserer regulärer Ausdruck |
| 3,0 | 1989 |  `my`-Variablen (lexikalisches Scoping) |
| 4,0 | 1991 | `O'Reilly`„Programming Perl“ (Camel-Buch) |
| 5,0 | 1994 | **Hauptfach**: Module, Referenzen, Abschlüsse,`use strict`|
| 5,6 | 2000 |  `our`,`state`(später), `v-strings`,`y2k`behebt |
| 5,8 | 2002 | **Unicode-Unterstützung**, `ithreads`,`open`Pragma |
| 5.10 | 2007 | `say`,`//`definiert-oder,`given`/`when`,`~~`Smartmatch |
| 5.12 | 2010 | `package NAME VERSION`,`...`(mehr), Unicode 5.2 |
| 5.14 | 2011 | `s///r`(zerstörungsfreie Substitution),`package`Verbesserungen |
| 5.16 | 2012 | `__SUB__`,`unicode_eval`|
| 5,18 | 2013 | Lexikalisches `$_`, Hash-Randomisierung,`my`in Bedingungen |
| 5,20 | 2014 | **Unterprogrammsignaturen** (experimentell),`%hash`Slicing |
| 5,22 | 2015 | `&`Dereferenzierung,`<<>>`(sicher offen) |
| 5,24 | 2016 | Postfix-Dereferenzierung stabil |
| 5,26 | 2017 | **Lexikalisches`$_`in`while`**,`.`in`@INC`entfernt (Sicherheit) |
| 5,28 | 2018 | Unicode 10.0,`delete`auf Schlüssel/Wert-Slices |
| 5.30 | 2019 | `my`in`for`/`while`Bedingungen |
| 5,32 | 2020 |  `isa`-Operator, Unicode 13.0 |
| 5,34 | 2021 | `try`/`catch`(experimentell),`defer`Blöcke |
| 5,36 | 2022 | **`use v5.36`**: Signaturen aktiviert,`$_`Standard,`defer`|
| 5,38 | 2023 | `class`Schlüsselwort (experimentell),`try`/`catch`stabil |
| 5,40 | 2024 | `^`bitweise Operatoren,`for`Listenverbesserungen |
| 5,42 | 2025 | Kontinuierliche Entwicklung |
## Wichtige Meilensteine
### Perl 1–4: Die Skript-Ära (1987–1993)
- **1987**: Larry Wall veröffentlicht Perl – „Practical Extraction and Report Language“
- **Ziel**: Sed, Awk, Grep und Shell in einem leistungsstarken Skripttool kombinieren
- **3.0**: Lexikalisches Scoping (`my`)
- **4.0**: The Camel Book – Perl wird weithin für Systemadministrationsaufgaben eingesetzt
### Perl 5: Das Goldene Zeitalter (1994–2019)
- **5.0 (1994)**: Vollständige Neufassung – **Module**, **Referenzen**, **Abschlüsse**, **Objekte**
- **5.6 (2000)**:`our`, V-Saiten
- **5.8 (2002)**: **Unicode-Unterstützung**, Interpreter-Threads (`ithreads`)
- **5.10 (2007)**: `say`,`//`(definiert-oder),`given`/`when`(Schalter), Smartmatch
- **5.12–5.28**: Inkrementelle Verbesserungen, Unicode-Upgrades
### Modernes Perl (2020–heute)
- **5.32 (2020)**: `isa`-Operator (Überprüfung des Reinigertyps)
- **5.34 (2021)**:`try`/`catch`(experimentell), `defer`-Blöcke
- **5.36 (2022)**: **`use v5.36`** – Signaturen standardmäßig aktiviert,`$_`Standard,`defer`
- **5.38 (2023)**: Schlüsselwort`class`(experimentell – integriertes OOP),`try`/`catch`stabil
- **5.40 (2024)**: Bitweise Operatorverbesserungen
## Syntaxentwicklung
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

## CPAN-Ökosystem
```
1995: CPAN (Comprehensive Perl Archive Network) launched
2000: Module::Build — alternative to MakeMaker
2008: CPANPLUS — enhanced CPAN client
2010: Dist::Zilla — release builder
2012: Carton — dependency pinning (like Bundler)
2013: cpanminus — zero-config CPAN client
2025: CPAN hosts 200,000+ modules from 14,000+ authors
```

## Wichtige Designprinzipien
```
1. "TMTOWTDI" — There's More Than One Way To Do It
2. "Practical, not pure" — solve real problems
3. "Text processing king" — regex built into the language
4. "Glue language" — connect systems, protocols, formats
5. "Backward compatible" — old Perl code keeps running
6. "Community-driven" — CPAN, Perl Mongers, YAPC conferences
```

## Ökosystemwachstum
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
