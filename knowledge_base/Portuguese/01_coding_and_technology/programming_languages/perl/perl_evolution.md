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
# Perl — Histórico e evolução da versão
## Linha do tempo
| Versão | Ano | Tema principal |
|--------|------|-----------|
| 1,0 | 1987 | Lançamento inicial (Larry Wall) |
| 2.0 | 1988 |  Função `study`, melhor regex |
| 3.0 | 1989 |  Variáveis ​​`my` (escopo léxico) |
| 4,0 | 1991 | `O'Reilly`"Programação Perl" (livro Camel) |
| 5,0 | 1994 | **Principais**: módulos, referências, fechamentos,`use strict`|
| 5.6 | 2000 | `our`,`state`(mais tarde),`v-strings`,`y2k`correções |
| 5.8 | 2002 | **Suporte Unicode**, pragma`ithreads`,`open`|
| 5.10 | 2007 | `say`,`//`definido-ou,`given`/`when`,`~~`smartmatch |
| 5.12 | 2010 | `package NAME VERSION`,`...`(yada-yada), Unicode 5.2 |
| 5.14 | 2011 | `s///r`(substituição não destrutiva), melhorias`package`|
| 5.16 | 2012 | `__SUB__`,`unicode_eval`|
| 5.18 | 2013 | Lexical`$_`, randomização de hash,`my`em condicionais |
| 5,20 | 2014 | **Assinaturas de subrotina** (experimental), fatiamento`%hash`|
| 5.22 | 2015 |  Desreferenciação `&`,`<<>>`(abertura segura) |
| 5.24 | 2016 | Desreferenciação do Postfix estável |
| 5.26 | 2017 | **Lexical`$_`em`while`**,`.`em`@INC`removido (segurança) |
| 5.28 | 2018 | Unicode 10.0,`delete`em fatias de chave/valor |
| 5h30 | 2019 | `my`em condições`for`/`while`|
| 5.32 | 2020 |  Operador `isa`, Unicode 13.0 |
| 5,34 | 2021 | `try`/`catch`(experimental), blocos`defer`|
| 5,36 | 2022 | **`use v5.36`**: assinaturas habilitadas, padrão `$_`,`defer`|
| 5,38 | 2023 |  Palavra-chave`class`(experimental),`try`/`catch`estável |
| 5,40 | 2024 |  Operadores bit a bit `^`, melhorias na lista`for`|
| 5,42 | 2025 | Desenvolvimento contínuo |
## Marcos importantes
### Perl 1–4: A Era dos Scripts (1987–1993)
- **1987**: Larry Wall lança Perl — "Practical Extraction and Report Language"
- **Objetivo**: Combinar sed, awk, grep, shell em uma poderosa ferramenta de script
- **3.0**: Escopo léxico (`my`)
- **4.0**: The Camel Book — Perl é amplamente adotado para tarefas de administração de sistemas
### Perl 5: A Idade de Ouro (1994–2019)
- **5.0 (1994)**: Reescrita completa — **módulos**, **referências**, **fechamentos**, **objetos**
- **5.6 (2000)**:`our`, v-strings
- **5.8 (2002)**: **suporte Unicode**, threads de interpretação (`ithreads`)
- **5.10 (2007)**:`say`,`//`(definido ou),`given`/`when`(switch), smartmatch
- **5.12–5.28**: Melhorias incrementais, atualizações Unicode
### Perl moderno (2020-presente)
- **5.32 (2020)**: operador`isa`(verificação do tipo de limpador)
- **5.34 (2021)**:`try`/`catch`(experimental), blocos `defer`
- **5.36 (2022)**: **`use v5.36`** — assinaturas habilitadas por padrão, padrão `$_`,`defer`
- **5.38 (2023)**: palavra-chave`class`(experimental — OOP integrado), `try`/`catch` estável
- **5.40 (2024)**: Melhorias no operador bit a bit
## Evolução da Sintaxe
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

## Ecossistema CPAN
```
1995: CPAN (Comprehensive Perl Archive Network) launched
2000: Module::Build — alternative to MakeMaker
2008: CPANPLUS — enhanced CPAN client
2010: Dist::Zilla — release builder
2012: Carton — dependency pinning (like Bundler)
2013: cpanminus — zero-config CPAN client
2025: CPAN hosts 200,000+ modules from 14,000+ authors
```

## Princípios-chave de design
```
1. "TMTOWTDI" — There's More Than One Way To Do It
2. "Practical, not pure" — solve real problems
3. "Text processing king" — regex built into the language
4. "Glue language" — connect systems, protocols, formats
5. "Backward compatible" — old Perl code keeps running
6. "Community-driven" — CPAN, Perl Mongers, YAPC conferences
```

## Crescimento do Ecossistema
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
