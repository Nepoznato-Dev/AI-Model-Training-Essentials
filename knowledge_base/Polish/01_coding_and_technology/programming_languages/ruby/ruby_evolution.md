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
# Ruby — historia wersji i ewolucja
## Oś czasu
| Wersja | Rok | Kluczowy motyw |
|--------|------|-----------|
| 0,95 | 1995 | Pierwsze wydanie (Yukihiro „Matz” Matsumoto) |
| 1,0 | 1996 | Pierwsza stabilna wersja |
| 1.2 | 1998 | Pierwsza angielska dokumentacja |
| 1,4 | 1999 | `BEGIN`/`END`,`String#unpack`|
| 1,6 | 2000 | Ulepszenia zbierania śmieci |
| 1,8 | 2003 | $KCODE, silnik regex oniguruma |
| 1,9 | 2007 | **Główny**: M17N (wielojęzyczny), nowa składnia mieszająca, włókna |
| 2,0 | 2013 | Argumenty słów kluczowych,`Enumerator::Lazy`,`Module#prepend`|
| 2.1 | 2013 | Udoskonalone wywołania metod,`frozen_string_literal`|
| 2.2 | 2014 | Symbol GC, przyrostowy GC |
| 2.3 | 2015 | Zamrożona pragma literacka,`&.`bezpieczna nawigacja |
| 2.4 | 2016 | `Integer`ujednolicone,`String`mapowanie wielkości liter Unicode |
| 2,5 | 2017 | `yield_self`, bloki w`rescue`/`ensure`|
| 2.6 | 2018 | **Kompilator JIT (MJIT)**, nieograniczony zakres`1..`|
| 2.7 | 2019 | Dopasowywanie wzorców (eksperymentalne), parametry bloków numerowanych |
| 3,0 | 2020 | **Główne**: Ractor (współbieżność), Harmonogram światłowodowy, typy RBS |
| 3.1 | 2021 |  Przekazywanie bloków `Anonymous`,`Hash#compact`|
| 3.2 | 2022 |  Klasa `Data`, ulepszenia `File.realpath`, produkcja YJIT |
| 3.3 | 2023 | **YJIT** duże ulepszenia, parametr bloku`it`|
| 3.4 | 2024 | Domyślny parser pryzmatu,`it`jako domyślny parametr bloku |
## Główne kamienie milowe
### Wczesny Rubin (1995–2003)
- **1995**: Matz tworzy Ruby — łącząc Perl, Smalltalk, Lisp
- **1.0 (1996)**: Pierwsza stabilna wersja
- **1,8 (2003)**: „Klasyczny” Rubin — szybki, stabilny, powszechnie stosowany
### Era kolei (2004–2013)
- **2004**: Wydanie Ruby on Rails — rewolucja w tworzeniu stron internetowych
- **1.9 (2007)**: M17N (ciągi wielojęzyczne), nowa składnia skrótu `{key: value}`, włókna
- **2.0 (2013)**: Argumenty słów kluczowych, leniwe wyliczacze, `Module#prepend`
### Nowoczesny rubin (2015 – obecnie)
- **2.6 (2018)**: Kompilator JIT (MJIT) — pierwsze wypychanie wydajności
- **2.7 (2019)**: Dopasowywanie wzorców (eksperymentalne), parametry bloków numerowanych`_1`
- **3.0 (2020)**: **Ractor** (współbieżność modelu aktora), **Fiber Scheduler** (asynchroniczne we/wy), **RBS** (sygnatury typów)
- **3.2 (2022)**: klasa`Data`(obiekty o niezmiennej wartości), YJIT gotowy do produkcji
- **3.3 (2023)**: Główne przyspieszenia YJIT (nawet 3x szybsze), parametr bloku `it`
- **3.4 (2024)**: Parser Prism staje się domyślny
## Ewolucja wydajności
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

## Ewolucja współbieżności
```
1.8:  Green threads (GIL)
1.9:  Native threads (still GIL)
2.0:  Fiber (cooperative)
2.6:  Fiber Scheduler proposal
3.0:  Ractor (Actor model, no GIL sharing)
3.0:  Fiber Scheduler (async I/O without threads)
3.3:  Improved Fiber Scheduler
```

## Ewolucja dopasowywania wzorców
```
2.7:  Experimental — case/in
3.0:  Improved — pin operator, find pattern
3.1:  One-line pattern matching
3.2:  Shortcut syntax, infinite patterns
3.4:  Pattern matching stabilized
```

## Kluczowe zasady projektowania
```
1. "MINASWAN" — Matz is nice and so we are nice
2. "Programmer happiness" — surprising is bad
3. "Everything is an object" — even numbers, nil, true
4. "Blocks are fundamental" — closures as first-class
5. "Duck typing" — behavior over type
6. "Convention over configuration" — Rails philosophy
```

## Rozwój ekosystemu
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
