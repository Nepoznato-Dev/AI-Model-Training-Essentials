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

# Perl — история версий и эволюция
## Временная шкала
| Версия | Год | Ключевая тема |
|---------|------|-----------|
| 1.0 | 1987 | Первоначальный выпуск (Ларри Уолл) |
| 2.0 | 1988 |  Функция `study`, улучшенное регулярное выражение |
| 3.0 | 1989 |  Переменные`my`(лексическая область видимости) |
| 4.0 | 1991 | `O'Reilly`«Программирование на Perl» (книга Camel) |
| 5.0 | 1994 | **Основное**: модули, ссылки, замыкания,`use strict`|
| 5,6 | 2000 | `our`,`state`(позже),`v-strings`,`y2k`исправления |
| 5,8 | 2002 | **Поддержка Unicode**, директива `ithreads`,`open`|
| 5.10 | 2007 | `say`,`//`определено-или,`given`/`when`,`~~`умное сопоставление |
| 5.12 | 2010 | `package NAME VERSION`,`...`(яда-яда), Юникод 5.2 |
| 5.14 | 2011 | `s///r`(неразрушающая замена), улучшения`package`|
| 5.16 | 2012 | `__SUB__`,`unicode_eval`|
| 5.18 | 2013 | Лексический`$_`, рандомизация хеша,`my`в условных выражениях |
| 5.20 | 2014 | **Сигнатуры подпрограмм** (экспериментально), нарезка`%hash`|
| 5.22 | 2015 |  Разыменование `&`,`<<>>`(безопасное открытие) |
| 5,24 | 2016 | Разыменование Postfix стабильно |
| 5,26 | 2017 | **Лексический`$_`в`while`**,`.`в`@INC`удален (безопасность) |
| 5.28 | 2018 | Unicode 10.0,`delete`для срезов «ключ-значение» |
| 5.30 | 2019 | `my`в условиях `for`/`while` |
| 5.32 | 2020 |  Оператор `isa`, Юникод 13.0 |
| 5.34 | 2021 | `try`/`catch`(экспериментальный),`defer`блоки |
| 5,36 | 2022 | **`use v5.36`**: подписи включены,`$_`по умолчанию,`defer`|
| 5,38 | 2023 |  Ключевое слово`class`(экспериментальное),`try`/`catch`стабильное |
| 5.40 | 2024 |  Побитовые операторы `^`, улучшения списка`for`|
| 5.42 | 2025 | Постоянное развитие |
## Основные вехи
### Perl 1–4: Эра сценариев (1987–1993)
- **1987**: Ларри Уолл выпускает Perl — «Практический язык извлечения и создания отчетов».
- **Цель**: объединить sed, awk, grep и Shell в один мощный инструмент для создания сценариев.
- **3.0**: Лексическая область видимости (`my`)
- **4.0**: The Camel Book — Perl получает широкое распространение для задач системного администратора.
### Perl 5: Золотой век (1994–2019)
- **5.0 (1994)**: Полная переработка — **модули**, **ссылки**, **замыкания**, **объекты**.
- **5.6 (2000)**: `our`, v-струны
- **5.8 (2002 г.)**: **Поддержка Unicode**, потоки интерпретатора (`ithreads`)
- **5.10 (2007 г.)**:`say`,`//`(определенное-или),`given`/`when`(переключатель), smartmatch
- **5.12–5.28**: дополнительные улучшения, обновления Unicode.
### Современный Perl (2020 – настоящее время)
- **5.32 (2020)**: оператор`isa`(проверка типа очистителя)
- **5.34 (2021 г.)**: блоки`try`/`catch`(экспериментальный), `defer`
- **5.36 (2022 г.)**: **`use v5.36`** — подписи включены по умолчанию,`$_`по умолчанию,`defer`
- **5.38 (2023 г.)**: ключевое слово`class`(экспериментальное — встроенное ООП),`try`/`catch`стабильное
- **5.40 (2024 г.)**: Улучшения побитовых операторов.
## Эволюция синтаксиса
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

## Экосистема CPAN
```
1995: CPAN (Comprehensive Perl Archive Network) launched
2000: Module::Build — alternative to MakeMaker
2008: CPANPLUS — enhanced CPAN client
2010: Dist::Zilla — release builder
2012: Carton — dependency pinning (like Bundler)
2013: cpanminus — zero-config CPAN client
2025: CPAN hosts 200,000+ modules from 14,000+ authors
```

## Ключевые принципы проектирования
```
1. "TMTOWTDI" — There's More Than One Way To Do It
2. "Practical, not pure" — solve real problems
3. "Text processing king" — regex built into the language
4. "Glue language" — connect systems, protocols, formats
5. "Backward compatible" — old Perl code keeps running
6. "Community-driven" — CPAN, Perl Mongers, YAPC conferences
```

## Рост экосистемы
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
