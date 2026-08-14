<!--
---
# Metadata
title: "Ruby — Version History & Evolution"
description: "Comprehensive version history and evolution of Ruby from 1.0 to modern Ruby."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
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

-->
# Ruby – Versionsgeschichte und Entwicklung
## Zeitleiste
| Version | Jahr | Schlüsselthema |
|---------|------|-----------|
| 0,95 | 1995 | Erstveröffentlichung (Yukihiro „Matz“ Matsumoto) |
| 1,0 | 1996 | Erste stabile Veröffentlichung |
| 1.2 | 1998 | Erste englische Dokumentation |
| 1,4 | 1999 | `BEGIN`/`END`,`String#unpack`|
| 1,6 | 2000 | Verbesserungen bei der Speicherbereinigung |
| 1,8 | 2003 | $KCODE, Oniguruma-Regex-Engine |
| 1,9 | 2007 | **Major**: M17N (mehrsprachig), neue Hash-Syntax, Fasern |
| 2,0 | 2013 | Schlüsselwortargumente,`Enumerator::Lazy`,`Module#prepend`|
| 2.1 | 2013 | Verfeinerte Methodenaufrufe,`frozen_string_literal`|
| 2.2 | 2014 | Symbol GC, inkrementeller GC |
| 2.3 | 2015 | Eingefrorenes String-Literal-Pragma,`&.`sichere Navigation |
| 2,4 | 2016 | `Integer`einheitlich,`String`Unicode-Fallzuordnung |
| 2,5 | 2017 | `yield_self`, Blöcke in`rescue`/`ensure`|
| 2,6 | 2018 | **JIT-Compiler (MJIT)**, endloser Bereich`1..`|
| 2,7 | 2019 | Mustervergleich (experimentell), nummerierte Blockparameter |
| 3,0 | 2020 | **Major**: Ractor (Parallelität), Fibre Scheduler, RBS-Typen |
| 3.1 | 2021 | `Anonymous`Blockweiterleitung,`Hash#compact`|
| 3.2 | 2022 |  `Data`-Klasse, `File.realpath`-Verbesserungen, YJIT-Produktion |
| 3.3 | 2023 | **YJIT** wesentliche Verbesserungen, Blockparameter`it`|
| 3,4 | 2024 | Prism-Parser-Standard,`it`als Standardblockparameter |
## Wichtige Meilensteine
### Early Ruby (1995–2003)
- **1995**: Matz kreiert Ruby – eine Mischung aus Perl, Smalltalk und Lisp
- **1.0 (1996)**: Erste stabile Version
- **1.8 (2003)**: Das „klassische“ Ruby – schnell, stabil, weit verbreitet
### Die Rails-Ära (2004–2013)
- **2004**: Ruby on Rails veröffentlicht – Revolution in der Webentwicklung
- **1.9 (2007)**: M17N (mehrsprachige Zeichenfolgen), neue Hash-Syntax `{key: value}`, Fasern
- **2.0 (2013)**: Schlüsselwortargumente, Lazy Enumeratoren, `Module#prepend`
### Modern Ruby (2015–heute)
- **2.6 (2018)**: JIT-Compiler (MJIT) – erster Leistungsschub
- **2.7 (2019)**: Mustervergleich (experimentell), nummerierte Blockparameter`_1`
- **3.0 (2020)**: **Ractor** (Actor-Modell-Parallelität), **Fiber Scheduler** (asynchrone E/A), **RBS** (Typsignaturen)
- **3.2 (2022)**: `Data`-Klasse (unveränderliche Wertobjekte), YJIT-produktionsbereit
- **3.3 (2023)**: Große YJIT-Beschleunigung (bis zu 3x schneller), Blockparameter `it`
- **3.4 (2024)**: Prism-Parser wird zum Standard
## Leistungsentwicklung
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

## Parallelitätsentwicklung
```
1.8:  Green threads (GIL)
1.9:  Native threads (still GIL)
2.0:  Fiber (cooperative)
2.6:  Fiber Scheduler proposal
3.0:  Ractor (Actor model, no GIL sharing)
3.0:  Fiber Scheduler (async I/O without threads)
3.3:  Improved Fiber Scheduler
```

## Pattern-Matching-Evolution
```
2.7:  Experimental — case/in
3.0:  Improved — pin operator, find pattern
3.1:  One-line pattern matching
3.2:  Shortcut syntax, infinite patterns
3.4:  Pattern matching stabilized
```

## Wichtige Designprinzipien
```
1. "MINASWAN" — Matz is nice and so we are nice
2. "Programmer happiness" — surprising is bad
3. "Everything is an object" — even numbers, nil, true
4. "Blocks are fundamental" — closures as first-class
5. "Duck typing" — behavior over type
6. "Convention over configuration" — Rails philosophy
```

## Ökosystemwachstum
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
