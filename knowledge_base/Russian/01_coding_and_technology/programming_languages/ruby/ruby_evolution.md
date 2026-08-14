---
# Metadata
title: "Ruby — Version History & Evolution"
description: "Comprehensive version history and evolution of Ruby from 1.0 to modern Ruby."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial version history"
tags: [ruby, version-history, evolution, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "10 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

# Ruby — история версий и эволюция
## Временная шкала
| Версия | Год | Ключевая тема |
|---------|------|-----------|
| 0,95 | 1995 | Первоначальный выпуск (Юкихиро «Мац» Мацумото) |
| 1.0 | 1996 | Первый стабильный выпуск |
| 1,2 | 1998 | Первая англоязычная документация |
| 1,4 | 1999 | `BEGIN`/`END`,`String#unpack`|
| 1,6 | 2000 | Улучшения в сборе мусора |
| 1,8 | 2003 | $KCODE, механизм регулярных выражений онигурумы |
| 1,9 | 2007 | **Основное**: M17N (многоязычный), новый синтаксис хеширования, волокна |
| 2.0 | 2013 | Аргументы ключевого слова,`Enumerator::Lazy`,`Module#prepend`|
| 2.1 | 2013 | Усовершенствованные вызовы методов`frozen_string_literal`|
| 2.2 | 2014 | Символ GC, инкрементальный GC |
| 2.3 | 2015 | Прагма замороженной строки, безопасная навигация`&.`|
| 2,4 | 2016 | `Integer`унифицированный,`String`сопоставление регистра Юникода |
| 2,5 | 2017 | `yield_self`, блоки в`rescue`/`ensure`|
| 2,6 | 2018 | **JIT-компилятор (MJIT)**, бесконечный диапазон`1..`|
| 2,7 | 2019 | Сопоставление с образцом (экспериментальное), параметры пронумерованного блока |
| 3.0 | 2020 | **Основные**: Ractor (параллелизм), Fiber Scheduler, типы RBS |
| 3.1 | 2021 |  Пересылка блоков `Anonymous`,`Hash#compact`|
| 3.2 | 2022 |  Класс `Data`, улучшения `File.realpath`, производство YJIT |
| 3.3 | 2023 | **YJIT** значительные улучшения, параметр блока`it`|
| 3,4 | 2024 | Парсер Prism по умолчанию,`it`как параметр блока по умолчанию |
## Основные вехи
### Ранний Рубин (1995–2003)
- **1995**: Мац создает Ruby, смешивая Perl, Smalltalk и Lisp.
- **1.0 (1996 г.)**: Первый стабильный выпуск.
- **1.8 (2003 г.)**: «Классический» Ruby — быстрый, стабильный, широко распространенный.
### Эра рельсов (2004–2013)
- **2004**: выпуск Ruby on Rails — революция в веб-разработке.
- **1.9 (2007 г.)**: M17N (многоязычные строки), новый синтаксис хеширования `{key: value}`, волокна
- **2.0 (2013 г.)**: аргументы ключевых слов, ленивые перечислители, `Module#prepend`.
### Современный Рубин (2015 – настоящее время)
- **2.6 (2018 г.)**: JIT-компилятор (MJIT) — первое повышение производительности
- **2.7 (2019 г.)**: Сопоставление с образцом (экспериментальное), параметры пронумерованного блока`_1`
- **3.0 (2020 г.)**: **Ractor** (параллелизм модели актера), **Fiber Scheduler** (асинхронный ввод-вывод), **RBS** (сигнатуры типов).
- **3.2 (2022 г.)**: класс`Data`(объекты неизменяемых значений), готовность к производству YJIT.
- **3.3 (2023 г.)**: значительное ускорение YJIT (до 3 раз быстрее), параметр блока `it`.
- **3.4 (2024 г.)**: парсер Prism становится по умолчанию.
## Эволюция производительности
```
Ruby 1.8:  Baseline (interpreted)
Ruby 1.9:  ~1.5x faster (YARV bytecode)
Ruby 2.0:  ~1x (focus on features)
Ruby 2.6:  MJIT (experimental JIT)
Ruby 3.0:  Fiber Scheduler (async I/O)
Ruby 3.2:  YJIT (production JIT)
Ruby 3.3:  YJIT 3x faster (Rails benchmarks)
Ruby 3.4:  Prism parser (faster parsing)
Target:    3x faster than Ruby 2.5 (Ruby 3x3 goal)
```

## Эволюция параллелизма
```
1.8:  Green threads (GIL)
1.9:  Native threads (still GIL)
2.0:  Fiber (cooperative)
2.6:  Fiber Scheduler proposal
3.0:  Ractor (Actor model, no GIL sharing)
3.0:  Fiber Scheduler (async I/O without threads)
3.3:  Improved Fiber Scheduler
```

## Эволюция сопоставления с образцом
```
2.7:  Experimental — case/in
3.0:  Improved — pin operator, find pattern
3.1:  One-line pattern matching
3.2:  Shortcut syntax, infinite patterns
3.4:  Pattern matching stabilized
```

## Ключевые принципы проектирования
```
1. "MINASWAN" — Matz is nice and so we are nice
2. "Programmer happiness" — surprising is bad
3. "Everything is an object" — even numbers, nil, true
4. "Blocks are fundamental" — closures as first-class
5. "Duck typing" — behavior over type
6. "Convention over configuration" — Rails philosophy
```

## Рост экосистемы
```
2004: Rails launches — Ruby enters mainstream
2005: RubyGems package manager
2006: Ruby wins "Language of the Year" (TIOBE)
2008: Bundler (dependency management)
2010: Ruby 1.9 adoption accelerates
2013: Ruby 2.0 — enterprise adoption
2020: Ruby 3.0 — concurrency revolution
2023: YJIT makes Ruby fast again
2025: Ruby remains top 10; Rails powers GitHub, Shopify, Basecamp, Stripe
```
