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
# Perl: cronologia ed evoluzione delle versioni
## Cronologia
| Versione | Anno | Tema chiave |
|---------|------|-----------|
| 1.0 | 1987 | Versione iniziale (Larry Wall) |
| 2.0 | 1988 |  Funzione `study`, migliore espressione regolare |
| 3.0 | 1989 |  Variabili`my`(ambito lessicale) |
| 4.0 | 1991 | `O'Reilly`"Programmazione Perl" (libro Camel) |
| 5.0 | 1994 | **Maggiori**: moduli, referenze, chiusure,`use strict`|
| 5.6| 2000 | `our`,`state`(successivo),`v-strings`,`y2k`correzioni |
| 5.8| 2002| **Supporto Unicode**, pragma`ithreads`,`open`|
| 5.10| 2007| `say`,`//`definito-o,`given`/`when`,`~~`smartmatch |
| 5.12| 2010| `package NAME VERSION`,`...`(yada-yada), Unicode 5.2 |
| 5.14| 2011 | `s///r`(sostituzione non distruttiva), miglioramenti`package`|
| 5.16| 2012| `__SUB__`,`unicode_eval`|
| 5.18| 2013|`$_`lessicale , randomizzazione hash,`my`nei condizionali |
| 5.20| 2014| **Firme di subroutine** (sperimentale), affettatura`%hash`|
| 5.22| 2015|  Dereferenziazione `&`,`<<>>`(cassaforte aperta) |
| 5.24| 2016| Dereferenziamento suffisso stabile |
| 5.26| 2017 | **`$_` lessicale in`while`**,`.`in`@INC`rimosso (sicurezza) |
| 5.28| 2018 | Unicode 10.0,`delete`su sezioni chiave/valore |
| 5.30| 2019 | `my`nelle condizioni`for`/`while`|
| 5.32| 2020 |  Operatore `isa`, Unicode 13.0 |
| 5.34| 2021 | `try`/`catch`(sperimentale),`defer`blocchi |
| 5.36| 2022 | **`use v5.36`**: firme abilitate,`$_`predefinito,`defer`|
| 5.38| 2023 |  Parola chiave`class`(sperimentale),`try`/`catch`stabile |
| 5,40| 2024 |  Operatori bit a bit `^`, miglioramenti all'elenco`for`|
| 5.42| 2025 | Sviluppo continuo |
## Traguardi importanti
### Perl 1–4: L'era degli script (1987–1993)
- **1987**: Larry Wall rilascia Perl — "Practical Extraction and Report Language"
- **Obiettivo**: combinare sed, awk, grep e shell in un unico potente strumento di scripting
- **3.0**: Ambito lessicale (`my`)
- **4.0**: The Camel Book: Perl viene ampiamente adottato per le attività di amministrazione di sistema
### Perl 5: L'età dell'oro (1994–2019)
- **5.0 (1994)**: riscrittura completa: **moduli**, **riferimenti**, **chiusure**, **oggetti**
- **5.6 (2000)**:`our`, stringhe a V
- **5.8 (2002)**: **Supporto Unicode**, thread di interprete (`ithreads`)
- **5.10 (2007)**:`say`,`//`(definito-or),`given`/`when`(switch), smartmatch
- **5.12–5.28**: miglioramenti incrementali, aggiornamenti Unicode
### Perl moderno (2020-oggi)
- **5.32 (2020)**: operatore`isa`(controllo del tipo di pulitore)
- **5.34 (2021)**:`try`/`catch`(sperimentale), blocchi `defer`
- **5.36 (2022)**: **`use v5.36`**: firme abilitate per impostazione predefinita,`$_`impostazione predefinita,`defer`
- **5.38 (2023)**: parola chiave`class`(sperimentale - OOP integrata),`try`/`catch`stabile
- **5.40 (2024)**: miglioramenti dell'operatore bit a bit
## Evoluzione della sintassi
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

## Ecosistema CPAN
```
1995: CPAN (Comprehensive Perl Archive Network) launched
2000: Module::Build — alternative to MakeMaker
2008: CPANPLUS — enhanced CPAN client
2010: Dist::Zilla — release builder
2012: Carton — dependency pinning (like Bundler)
2013: cpanminus — zero-config CPAN client
2025: CPAN hosts 200,000+ modules from 14,000+ authors
```

## Principi chiave di progettazione
```
1. "TMTOWTDI" — There's More Than One Way To Do It
2. "Practical, not pure" — solve real problems
3. "Text processing king" — regex built into the language
4. "Glue language" — connect systems, protocols, formats
5. "Backward compatible" — old Perl code keeps running
6. "Community-driven" — CPAN, Perl Mongers, YAPC conferences
```

## Crescita dell'ecosistema
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
