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
# Perl — historia wersji i ewolucja
## Oś czasu
| Wersja | Rok | Kluczowy motyw |
|--------|------|-----------|
| 1,0 | 1987 | Pierwsze wydanie (Larry Wall) |
| 2,0 | 1988 |  Funkcja `study`, lepsze wyrażenie regularne |
| 3,0 | 1989 |  Zmienne`my`(zakres leksykalny) |
| 4,0 | 1991 | `O'Reilly`„Programowanie Perl” (książka Camel) |
| 5,0 | 1994 | **Główne**: moduły, referencje, zamknięcia,`use strict`|
| 5,6 | 2000 |  Poprawki`our`,`state`(później),`v-strings`,`y2k`|
| 5,8 | 2002 | **Obsługa Unicode**,`ithreads`,`open`pragma |
| 5.10 | 2007 | `say`,`//`zdefiniowany-lub,`given`/`when`,`~~`smartmatch |
| 5.12 | 2010 | `package NAME VERSION`,`...`(yada-yada), Unicode 5.2 |
| 5.14 | 2011 | `s///r`(zastąpienie nieniszczące), ulepszenia`package`|
| 5.16 | 2012 | `__SUB__`,`unicode_eval`|
| 5.18 | 2013 | Leksykalny`$_`, randomizacja skrótu,`my`w trybie warunkowym |
| 5.20 | 2014 | **Podpisy podprogramów** (eksperymentalne), krojenie`%hash`|
| 5.22 | 2015 |  Dereferencja `&`,`<<>>`(bezpieczne otwarcie) |
| 5.24 | 2016 | Stabilne dereferencje Postfixa |
| 5.26 | 2017 | **Usunięto leksykalny`$_`w`while`**,`.`w`@INC`usunięty (bezpieczeństwo) |
| 5.28 | 2018 | Unicode 10.0,`delete`na wycinkach klucz/wartość |
| 5.30 | 2019 | `my`w warunkach`for`/`while`|
| 5,32 | 2020 |  Operator `isa`, Unicode 13.0 |
| 5,34 | 2021 | `try`/`catch`(eksperymentalny), bloki`defer`|
| 5,36 | 2022 | **`use v5.36`**: podpisy włączone, domyślnie `$_`,`defer`|
| 5,38 | 2023 |  Słowo kluczowe`class`(eksperymentalne),`try`/`catch`stabilne |
| 5.40 | 2024 |  Operatory bitowe `^`, ulepszenia listy`for`|
| 5,42 | 2025 | Ciągły rozwój |
## Główne kamienie milowe
### Perl 1–4: Era skryptów (1987–1993)
- **1987**: Larry Wall wypuszcza Perl — „Praktyczny język ekstrakcji i raportowania”
- **Cel**: Połączyć sed, awk, grep i Shell w jedno potężne narzędzie skryptowe
- **3.0**: Zakres leksykalny (`my`)
- **4.0**: The Camel Book — Perl jest powszechnie stosowany w zadaniach administratora systemu
### Perl 5: Złoty wiek (1994–2019)
- **5.0 (1994)**: Całkowite przepisanie — **moduły**, **referencje**, **zamknięcia**, **obiekty**
- **5,6 (2000)**:`our`, v-stringi
- **5.8 (2002)**: **Obsługa Unicode**, wątki interpretera (`ithreads`)
- **5.10 (2007)**:`say`,`//`(zdefiniowany lub),`given`/`when`(przełącznik), smartmatch
- **5.12–5.28**: Przyrostowe ulepszenia, aktualizacje Unicode
### Nowoczesny Perl (2020 – obecnie)
- **5.32 (2020)**: operator`isa`(sprawdzanie typu odkurzacza)
- **5.34 (2021)**:`try`/`catch`(eksperymentalny),`defer`bloki
- **5.36 (2022)**: **`use v5.36`** — sygnatury domyślnie włączone, domyślnie `$_`,`defer`
- **5.38 (2023)**: słowo kluczowe`class`(eksperymentalne — wbudowane OOP), stabilne`try`/ `catch`
- **5.40 (2024)**: Ulepszenia operatora bitowego
## Ewolucja składni
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

## Ekosystem CPAN
```
1995: CPAN (Comprehensive Perl Archive Network) launched
2000: Module::Build — alternative to MakeMaker
2008: CPANPLUS — enhanced CPAN client
2010: Dist::Zilla — release builder
2012: Carton — dependency pinning (like Bundler)
2013: cpanminus — zero-config CPAN client
2025: CPAN hosts 200,000+ modules from 14,000+ authors
```

## Kluczowe zasady projektowania
```
1. "TMTOWTDI" — There's More Than One Way To Do It
2. "Practical, not pure" — solve real problems
3. "Text processing king" — regex built into the language
4. "Glue language" — connect systems, protocols, formats
5. "Backward compatible" — old Perl code keeps running
6. "Community-driven" — CPAN, Perl Mongers, YAPC conferences
```

## Rozwój ekosystemu
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
