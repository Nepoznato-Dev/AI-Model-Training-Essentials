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
# Perl — Historique et évolution des versions
## Chronologie
| Version | Année | Thème clé |
|---------|------|-----------|
| 1.0 | 1987 | Version initiale (Larry Wall) |
| 2.0 | 1988 |  Fonction `study`, meilleure regex |
| 3.0 | 1989 |  Variables`my`(portée lexicale) |
| 4.0 | 1991 | `O'Reilly`"Programmation Perl" (Livre Camel) |
| 5.0 | 1994 | **Majeur** : modules, références, fermetures,`use strict`|
| 5.6 | 2000 | `our`,`state`(plus tard),`v-strings`,`y2k`correctifs |
| 5.8 | 2002 | **Prise en charge Unicode**,`ithreads`,`open`pragma |
| 5.10 | 2007 | `say`,`//`défini-ou,`given`/`when`,`~~`smartmatch |
| 5.12 | 2010 | `package NAME VERSION`,`...`(yada-yada), Unicode 5.2 |
| 5.14 | 2011 | `s///r`(substitution non destructive), améliorations`package`|
| 5.16 | 2012 | `__SUB__`,`unicode_eval`|
| 5.18 | 2013 | Lexical`$_`, randomisation de hachage,`my`au conditionnel |
| 5.20 | 2014 | **Signatures de sous-programmes** (expérimental), découpage`%hash`|
| 5.22 | 2015 |  Déréférencement `&`,`<<>>`(ouverture sécurisée) |
| 5.24 | 2016 | Postfix déréférencement stable |
| 5.26 | 2017 | **`$_` lexical dans`while`**,`.`dans`@INC`supprimé (sécurité) |
| 5.28 | 2018 | Unicode 10.0,`delete`sur les tranches clé/valeur |
| 17h30 | 2019 | `my`dans les conditions`for`/`while`|
| 5.32 | 2020 |  Opérateur `isa`, Unicode 13.0 |
| 5.34 | 2021 | `try`/`catch`(expérimental), blocs`defer`|
| 5.36 | 2022 | **`use v5.36`** : signatures activées,`$_`par défaut,`defer`|
| 5.38 | 2023 |  Mot-clé`class`(expérimental),`try`/`catch`stable |
| 5h40 | 2024 |  Opérateurs bit à bit `^`, améliorations de la liste`for`|
| 5.42 | 2025 | Développement en cours |
## Étapes majeures
### Perl 1–4 : L'ère des scripts (1987–1993)
- **1987** : Larry Wall lance Perl — "Practical Extraction and Report Language"
- **Objectif** : Combinez sed, awk, grep et shell en un seul outil de script puissant
- **3.0** : Portée lexicale (`my`)
- **4.0** : The Camel Book — Perl est largement adopté pour les tâches d'administration système
### Perl 5 : L'âge d'or (1994-2019)
- **5.0 (1994)** : Réécriture complète — **modules**, **références**, **fermetures**, **objets**
- **5.6 (2000)** :`our`, v-strings
- **5.8 (2002)** : **Support Unicode**, threads d'interprétation (`ithreads`)
- **5.10 (2007)** :`say`,`//`(ou défini),`given`/`when`(commutateur), smartmatch
- **5.12–5.28** : améliorations incrémentielles, mises à niveau Unicode
### Perl moderne (2020-présent)
- **5.32 (2020)** : opérateur`isa`(vérification du type de nettoyeur)
- **5.34 (2021)** :`try`/`catch`(expérimental), blocs `defer`
- **5.36 (2022)** : **`use v5.36`** — signatures activées par défaut,`$_`par défaut,`defer`
- **5.38 (2023)** : mot-clé`class`(expérimental — POO intégré),`try`/`catch`stable
- **5.40 (2024)** : améliorations de l'opérateur au niveau du bit
## Évolution de la syntaxe
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

## Écosystème CPAN
```
1995: CPAN (Comprehensive Perl Archive Network) launched
2000: Module::Build — alternative to MakeMaker
2008: CPANPLUS — enhanced CPAN client
2010: Dist::Zilla — release builder
2012: Carton — dependency pinning (like Bundler)
2013: cpanminus — zero-config CPAN client
2025: CPAN hosts 200,000+ modules from 14,000+ authors
```

## Principes de conception clés
```
1. "TMTOWTDI" — There's More Than One Way To Do It
2. "Practical, not pure" — solve real problems
3. "Text processing king" — regex built into the language
4. "Glue language" — connect systems, protocols, formats
5. "Backward compatible" — old Perl code keeps running
6. "Community-driven" — CPAN, Perl Mongers, YAPC conferences
```

## Croissance de l'écosystème
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
