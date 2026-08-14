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
# Ruby: cronologia ed evoluzione delle versioni
## Cronologia
| Versione | Anno | Tema chiave |
|---------|------|-----------|
| 0,95| 1995 | Versione iniziale (Yukihiro "Matz" Matsumoto) |
| 1.0 | 1996 | Prima versione stabile |
| 1.2 | 1998 | Prima documentazione inglese |
| 1.4 | 1999 | `BEGIN`/`END`,`String#unpack`|
| 1.6 | 2000 | Miglioramenti alla raccolta dei rifiuti |
| 1.8 | 2003| $KCODE, motore regex oniguruma |
| 1.9 | 2007| **Maggiore**: M17N (multilingue), nuova sintassi hash, fibre |
| 2.0 | 2013| Argomenti parola chiave,`Enumerator::Lazy`,`Module#prepend`|
| 2.1 | 2013| Chiamate di metodo perfezionate,`frozen_string_literal`|
| 2.2 | 2014| Simbolo GC, GC incrementale |
| 2.3 | 2015| Pragma letterale stringa congelato,`&.`navigazione sicura |
| 2.4 | 2016| `Integer`unificato,`String`Mappatura maiuscole Unicode |
| 2,5 | 2017 | `yield_self`, blocchi in`rescue`/`ensure`|
| 2.6 | 2018 | **Compilatore JIT (MJIT)**, intervallo infinito`1..`|
| 2.7 | 2019 | Corrispondenza di modelli (sperimentale), parametri di blocco numerati |
| 3.0 | 2020 | **Maggiore**: Ractor (concorrenza), Fiber Scheduler, tipi RBS |
| 3.1 | 2021 | `Anonymous`inoltro di blocchi,`Hash#compact`|
| 3.2 | 2022 |  Classe `Data`, miglioramenti `File.realpath`, produzione YJIT |
| 3.3 | 2023 | **YJIT** miglioramenti importanti, parametro del blocco`it`|
| 3.4 | 2024 | Parser prisma predefinito,`it`come parametro di blocco predefinito |
## Traguardi importanti
### Primo rubino (1995-2003)
- **1995**: Matz crea Ruby, unendo Perl, Smalltalk e Lisp
- **1.0 (1996)**: prima versione stabile
- **1.8 (2003)**: il "classico" Ruby: veloce, stabile, ampiamente adottato
### L'era delle rotaie (2004–2013)
- **2004**: rilascio di Ruby on Rails: rivoluzione nello sviluppo web
- **1.9 (2007)**: M17N (stringhe multilingue), nuova sintassi hash`{key: value}`, fibre
- **2.0 (2013)**: argomenti di parole chiave, enumeratori pigri, `Module#prepend`
### Rubino moderno (2015-oggi)
- **2.6 (2018)**: compilatore JIT (MJIT) — primo push delle prestazioni
- **2.7 (2019)**: corrispondenza di pattern (sperimentale), parametri di blocco numerati`_1`
- **3.0 (2020)**: **Ractor** (concorrenza modello attore), **Fiber Scheduler** (I/O asincrono), **RBS** (firme di tipo)
- **3.2 (2022)**: classe`Data`(oggetti con valore immutabile), pronto per la produzione YJIT
- **3.3 (2023)**: maggiori accelerazioni YJIT (fino a 3 volte più veloci), parametro del blocco `it`
- **3.4 (2024)**: il parser del prisma diventa predefinito
## Evoluzione delle prestazioni
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

## Evoluzione della concorrenza
```
1.8:  Green threads (GIL)
1.9:  Native threads (still GIL)
2.0:  Fiber (cooperative)
2.6:  Fiber Scheduler proposal
3.0:  Ractor (Actor model, no GIL sharing)
3.0:  Fiber Scheduler (async I/O without threads)
3.3:  Improved Fiber Scheduler
```

## Evoluzione della corrispondenza dei modelli
```
2.7:  Experimental — case/in
3.0:  Improved — pin operator, find pattern
3.1:  One-line pattern matching
3.2:  Shortcut syntax, infinite patterns
3.4:  Pattern matching stabilized
```

## Principi chiave di progettazione
```
1. "MINASWAN" — Matz is nice and so we are nice
2. "Programmer happiness" — surprising is bad
3. "Everything is an object" — even numbers, nil, true
4. "Blocks are fundamental" — closures as first-class
5. "Duck typing" — behavior over type
6. "Convention over configuration" — Rails philosophy
```

## Crescita dell'ecosistema
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
