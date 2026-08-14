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

# Ruby - Historia ya Toleo na Mageuzi
## Rekodi ya matukio
| Toleo | Mwaka | Mandhari Muhimu |
|---------|------|-----------|
| 0.95 | 1995 | Toleo la awali (Yukihiro "Matz" Matsumoto) |
| 1.0 | 1996 | Toleo la kwanza thabiti |
| 1.2 | 1998 | Nyaraka za kwanza za Kiingereza |
| 1.4 | 1999 | `BEGIN`/`END`,`String#unpack`|
| 1.6 | 2000 | Maboresho ya ukusanyaji wa taka |
| 1.8 | 2003 | $KCODE, injini ya regex ya oniguruma |
| 1.9 | 2007 | **Meja**: M17N (lugha nyingi), sintaksia mpya ya hashi, nyuzi |
| 2.0 | 2013 | Hoja za maneno,`Enumerator::Lazy`,`Module#prepend`|
| 2.1 | 2013 | Simu za mbinu iliyoboreshwa,`frozen_string_literal`|
| 2.2 | 2014 | Alama ya GC, GC inayoongezeka |
| 2.3 | 2015 | pragma halisi ya kamba iliyoganda,`&.`urambazaji salama |
| 2.4 | 2016 | `Integer`iliyounganishwa,`String`Uchoraji ramani ya umbo la Unicode |
| 2.5 | 2017 | `yield_self`, vitalu katika`rescue`/`ensure`|
| 2.6 | 2018 | **Mkusanyaji wa JIT (MJIT)**, anuwai isiyo na mwisho`1..`|
| 2.7 | 2019 | Kulinganisha muundo (majaribio), vigezo vya vitalu vilivyo na nambari |
| 3.0 | 2020 | **Meja**: Rakta (sarafu), Kiratibu cha Fiber, aina za RBS |
| 3.1 | 2021 |  Usambazaji wa vizuizi vya `Anonymous`,`Hash#compact`|
| 3.2 | 2022 | `Data`darasa,`File.realpath`maboresho, uzalishaji wa YJIT |
| 3.3 | 2023 | **YJIT** maboresho makubwa, kigezo cha kuzuia`it`|
| 3.4 | 2024 | Chaguo-msingi la kichanganuzi cha Prism,`it`kama param chaguo-msingi ya kizuizi |
## Mafanikio Makuu
### Ruby ya Mapema (1995–2003)
- **1995**: Matz inaunda Ruby — inachanganya Perl, Smalltalk, Lisp
- **1.0 (1996)**: Toleo la kwanza thabiti
- **1.8 (2003)**: Ruby "ya kawaida" - haraka, thabiti, iliyopitishwa sana
### The Rails Era (2004–2013)
- **2004**: Ruby on Rails iliyotolewa - mapinduzi ya maendeleo ya wavuti
- **1.9 (2007)**: M17N (kamba za lugha nyingi), syntax mpya ya hashi`{key: value}`, nyuzi
- **2.0 (2013)**: Hoja za maneno muhimu, wadadisi wavivu, `Module#prepend`
### Ruby ya Kisasa (2015–sasa)
- **2.6 (2018)**: Kikusanyaji cha JIT (MJIT) — kisukuma cha kwanza cha utendaji
- **2.7 (2019)**: Ulinganishaji wa muundo (majaribio), vigezo vya vitalu vyenye nambari`_1`
- **3.0 (2020)**: **Ractor** (Muigizaji-mfano maridhawa), ** Kiratibu cha Fiber** (async I/O), **RBS** (saini za aina)
- **3.2 (2022)**: darasa la`Data`(vitu vya thamani visivyobadilika), YJIT tayari kwa uzalishaji
- **3.3 (2023)**: kasi kuu za YJIT (hadi 3x haraka), kigezo cha kuzuia cha `it`
- **3.4 (2024)**: Kichanganuzi cha Prism kinakuwa chaguomsingi
## Mageuzi ya Utendaji
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

## Mageuzi ya Sarafu
```
1.8:  Green threads (GIL)
1.9:  Native threads (still GIL)
2.0:  Fiber (cooperative)
2.6:  Fiber Scheduler proposal
3.0:  Ractor (Actor model, no GIL sharing)
3.0:  Fiber Scheduler (async I/O without threads)
3.3:  Improved Fiber Scheduler
```

## Mageuzi Yanayolingana Muundo
```
2.7:  Experimental — case/in
3.0:  Improved — pin operator, find pattern
3.1:  One-line pattern matching
3.2:  Shortcut syntax, infinite patterns
3.4:  Pattern matching stabilized
```

## Kanuni Muhimu za Usanifu
```
1. "MINASWAN" — Matz is nice and so we are nice
2. "Programmer happiness" — surprising is bad
3. "Everything is an object" — even numbers, nil, true
4. "Blocks are fundamental" — closures as first-class
5. "Duck typing" — behavior over type
6. "Convention over configuration" — Rails philosophy
```

## Ukuaji wa Mfumo ikolojia
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
