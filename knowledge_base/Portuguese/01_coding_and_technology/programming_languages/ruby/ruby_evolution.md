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
# Ruby — Histórico de versões e evolução
## Linha do tempo
| Versão | Ano | Tema principal |
|--------|------|-----------|
| 0,95 | 1995 | Lançamento inicial (Yukihiro "Matz" Matsumoto) |
| 1,0 | 1996 | Primeira versão estável |
| 1.2 | 1998 | Primeira documentação em inglês |
| 1.4 | 1999 | `BEGIN`/`END`,`String#unpack`|
| 1.6 | 2000 | Melhorias na coleta de lixo |
| 1.8 | 2003 | $KCODE, mecanismo regex oniguruma |
| 1,9 | 2007 | **Principal**: M17N (multilíngue), nova sintaxe hash, fibras |
| 2.0 | 2013 | Argumentos de palavra-chave,`Enumerator::Lazy`,`Module#prepend`|
| 2.1 | 2013 | Chamadas de método refinadas,`frozen_string_literal`|
| 2.2 | 2014 | Símbolo GC, GC incremental |
| 2.3 | 2015 | Pragma literal de string congelada, navegação segura`&.`|
| 2.4 | 2016 | `Integer`unificado, mapeamento de casos Unicode`String`|
| 2,5 | 2017 | `yield_self`, blocos em`rescue`/`ensure`|
| 2.6 | 2018 | **Compilador JIT (MJIT)**, intervalo infinito`1..`|
| 2.7 | 2019 | Correspondência de padrões (experimental), parâmetros de blocos numerados |
| 3.0 | 2020 | **Principais**: Ractor (simultaneidade), Fiber Scheduler, tipos RBS |
| 3.1 | 2021 |  Encaminhamento de bloco `Anonymous`,`Hash#compact`|
| 3.2 | 2022 |  Classe `Data`, melhorias `File.realpath`, produção YJIT |
| 3.3 | 2023 | **YJIT** grandes melhorias, parâmetro de bloco`it`|
| 3.4 | 2024 | Padrão do analisador de prisma,`it`como parâmetro de bloco padrão |
## Marcos importantes
### Primeiro Ruby (1995–2003)
- **1995**: Matz cria Ruby — misturando Perl, Smalltalk, Lisp
- **1.0 (1996)**: Primeira versão estável
- **1.8 (2003)**: O Ruby "clássico" — rápido, estável, amplamente adotado
### A Era dos Trilhos (2004–2013)
- **2004**: Ruby on Rails lançado — revolução no desenvolvimento web
- **1.9 (2007)**: M17N (strings multilíngues), nova sintaxe de hash`{key: value}`, fibras
- **2.0 (2013)**: argumentos de palavras-chave, enumeradores preguiçosos, `Module#prepend`
### Ruby Moderno (2015-presente)
- **2.6 (2018)**: compilador JIT (MJIT) — primeiro impulso de desempenho
- **2.7 (2019)**: correspondência de padrões (experimental), parâmetros de bloco numerados`_1`
- **3.0 (2020)**: **Ractor** (simultaneidade de modelo de ator), **Fiber Scheduler** (E/S assíncrona), **RBS** (assinaturas de tipo)
- **3.2 (2022)**: classe`Data`(objetos de valor imutável), YJIT pronto para produção
- **3.3 (2023)**: Grandes acelerações YJIT (até 3x mais rápido), parâmetro de bloco `it`
- **3.4 (2024)**: O analisador Prism se torna padrão
## Evolução do desempenho
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

## Evolução da simultaneidade
```
1.8:  Green threads (GIL)
1.9:  Native threads (still GIL)
2.0:  Fiber (cooperative)
2.6:  Fiber Scheduler proposal
3.0:  Ractor (Actor model, no GIL sharing)
3.0:  Fiber Scheduler (async I/O without threads)
3.3:  Improved Fiber Scheduler
```

## Evolução da correspondência de padrões
```
2.7:  Experimental — case/in
3.0:  Improved — pin operator, find pattern
3.1:  One-line pattern matching
3.2:  Shortcut syntax, infinite patterns
3.4:  Pattern matching stabilized
```

## Princípios-chave de design
```
1. "MINASWAN" — Matz is nice and so we are nice
2. "Programmer happiness" — surprising is bad
3. "Everything is an object" — even numbers, nil, true
4. "Blocks are fundamental" — closures as first-class
5. "Duck typing" — behavior over type
6. "Convention over configuration" — Rails philosophy
```

## Crescimento do Ecossistema
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
