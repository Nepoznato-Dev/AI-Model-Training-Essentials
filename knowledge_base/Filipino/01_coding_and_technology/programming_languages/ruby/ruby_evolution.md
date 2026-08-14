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
# Ruby — Kasaysayan ng Bersyon at Ebolusyon
## Timeline
| Bersyon | Taon | Pangunahing Tema |
|---------|------|-----------|
| 0.95 | 1995 | Paunang paglabas (Yukihiro "Matz" Matsumoto) |
| 1.0 | 1996 | Unang matatag na release |
| 1.2 | 1998 | Unang dokumentasyong Ingles |
| 1.4 | 1999 | `BEGIN`/`END`,`String#unpack`|
| 1.6 | 2000 | Mga pagpapabuti sa pangongolekta ng basura |
| 1.8 | 2003 | $KCODE, oniguruma regex engine |
| 1.9 | 2007 | **Major**: M17N (multilingual), bagong hash syntax, fibers |
| 2.0 | 2013 | Mga argumento ng keyword,`Enumerator::Lazy`,`Module#prepend`|
| 2.1 | 2013 | Pinong paraan ng mga tawag,`frozen_string_literal`|
| 2.2 | 2014 | Simbolong GC, incremental na GC |
| 2.3 | 2015 | Frozen string literal pragma,`&.`ligtas na nabigasyon |
| 2.4 | 2016 | `Integer`pinag-isa,`String`Unicode case mapping |
| 2.5 | 2017 | `yield_self`, mga bloke sa`rescue`/`ensure`|
| 2.6 | 2018 | **JIT compiler (MJIT)**, walang katapusang saklaw`1..`|
| 2.7 | 2019 | Pagtutugma ng pattern (pang-eksperimento), may bilang na block params |
| 3.0 | 2020 | **Major**: Ractor (concurrency), Fiber Scheduler, mga uri ng RBS |
| 3.1 | 2021 | `Anonymous`block forwarding,`Hash#compact`|
| 3.2 | 2022 | `Data`klase,`File.realpath`mga pagpapabuti, YJIT production |
| 3.3 | 2023 | **YJIT** pangunahing mga pagpapahusay,`it`block parameter |
| 3.4 | 2024 | Prism parser default,`it`bilang default na block param |
## Mga Pangunahing Milestone
### Maagang Ruby (1995–2003)
- **1995**: Nilikha ni Matz si Ruby — pinaghalo ang Perl, Smalltalk, Lisp
- **1.0 (1996)**: Unang stable na release
- **1.8 (2003)**: Ang "classic" na Ruby — mabilis, matatag, malawak na pinagtibay
### The Rails Era (2004–2013)
- **2004**: Inilabas ang Ruby on Rails — rebolusyon sa pagbuo ng web
- **1.9 (2007)**: M17N (multilingual string), bagong hash syntax`{key: value}`, mga fibers
- **2.0 (2013)**: Mga argumento ng keyword, tamad na enumerator, `Module#prepend`
### Modern Ruby (2015–kasalukuyan)
- **2.6 (2018)**: JIT compiler (MJIT) — unang performance push
- **2.7 (2019)**: Pagtutugma ng pattern (pang-eksperimento), may bilang na block params`_1`
- **3.0 (2020)**: **Ractor** (Actor-model concurrency), **Fiber Scheduler** (async I/O), **RBS** (type signatures)
- **3.2 (2022)**:`Data`class (immutable value objects), YJIT production-ready
- **3.3 (2023)**: YJIT major speedups (hanggang 3x mas mabilis),`it`block parameter
- **3.4 (2024)**: Nagiging default ang prism parser
## Ebolusyon ng Pagganap
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

## Ebolusyon ng Concurrency
```
1.8:  Green threads (GIL)
1.9:  Native threads (still GIL)
2.0:  Fiber (cooperative)
2.6:  Fiber Scheduler proposal
3.0:  Ractor (Actor model, no GIL sharing)
3.0:  Fiber Scheduler (async I/O without threads)
3.3:  Improved Fiber Scheduler
```

## Ebolusyon ng Pagtutugma ng Pattern
```
2.7:  Experimental — case/in
3.0:  Improved — pin operator, find pattern
3.1:  One-line pattern matching
3.2:  Shortcut syntax, infinite patterns
3.4:  Pattern matching stabilized
```

## Pangunahing Prinsipyo ng Disenyo
```
1. "MINASWAN" — Matz is nice and so we are nice
2. "Programmer happiness" — surprising is bad
3. "Everything is an object" — even numbers, nil, true
4. "Blocks are fundamental" — closures as first-class
5. "Duck typing" — behavior over type
6. "Convention over configuration" — Rails philosophy
```

## Paglago ng Ecosystem
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
