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
# Ruby — Historique et évolution des versions
## Chronologie
| Version | Année | Thème clé |
|---------|------|-----------|
| 0,95 | 1995 | Version initiale (Yukihiro "Matz" Matsumoto) |
| 1.0 | 1996 | Première version stable |
| 1.2 | 1998 | Première documentation en anglais |
| 1.4 | 1999 | `BEGIN`/`END`,`String#unpack`|
| 1.6 | 2000 | Améliorations de la collecte des déchets |
| 1.8 | 2003 | $KCODE, moteur d'expression régulière oniguruma |
| 1.9 | 2007 | **Majeur** : M17N (multilingue), nouvelle syntaxe de hachage, fibres |
| 2.0 | 2013 | Arguments de mot clé,`Enumerator::Lazy`,`Module#prepend`|
| 2.1 | 2013 | Appels de méthode affinés,`frozen_string_literal`|
| 2.2 | 2014 | Symbole GC, GC incrémentiel |
| 2.3 | 2015 | Pragma littéral de chaîne gelée, navigation sécurisée`&.`|
| 2.4 | 2016 | `Integer`unifié, mappage de cas Unicode`String`|
| 2.5 | 2017 | `yield_self`, blocs dans`rescue`/`ensure`|
| 2.6 | 2018 | **Compilateur JIT (MJIT)**, plage infinie`1..`|
| 2.7 | 2019 | Correspondance de modèles (expérimental), paramètres de blocs numérotés |
| 3.0 | 2020 | **Majeur** : Ractor (concurrence), Fiber Scheduler, types RBS |
| 3.1 | 2021 | `Anonymous`transfert de bloc,`Hash#compact`|
| 3.2 | 2022 |  Classe `Data`, améliorations `File.realpath`, production YJIT |
| 3.3 | 2023 | **YJIT** améliorations majeures, paramètre de bloc`it`|
| 3.4 | 2024 | Analyseur de prisme par défaut,`it`comme paramètre de bloc par défaut |
## Étapes majeures
### Rubis précoce (1995-2003)
- **1995** : Matz crée Ruby — mélangeant Perl, Smalltalk et Lisp
- **1.0 (1996)** : Première version stable
- **1.8 (2003)** : Le Ruby "classique" — rapide, stable, largement adopté
### L'ère Rails (2004-2013)
- **2004** : sortie de Ruby on Rails – révolution du développement Web
- **1.9 (2007)** : M17N (chaînes multilingues), nouvelle syntaxe de hachage`{key: value}`, fibres
- **2.0 (2013)** : arguments de mots clés, énumérateurs paresseux, `Module#prepend`
### Rubis moderne (2015-présent)
- **2.6 (2018)** : compilateur JIT (MJIT) — première poussée de performances
- **2.7 (2019)** : Correspondance de modèles (expérimental), paramètres de blocs numérotés`_1`
- **3.0 (2020)** : **Ractor** (concurrence acteur-modèle), **Fiber Scheduler** (E/S asynchrones), **RBS** (signatures de type)
- **3.2 (2022)** : classe`Data`(objets à valeur immuable), prêt pour la production YJIT
- **3.3 (2023)** : accélérations majeures de YJIT (jusqu'à 3 fois plus rapides), paramètre de bloc `it`
- **3.4 (2024)** : L'analyseur Prism devient par défaut
## Évolution des performances
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

## Évolution de la concurrence
```
1.8:  Green threads (GIL)
1.9:  Native threads (still GIL)
2.0:  Fiber (cooperative)
2.6:  Fiber Scheduler proposal
3.0:  Ractor (Actor model, no GIL sharing)
3.0:  Fiber Scheduler (async I/O without threads)
3.3:  Improved Fiber Scheduler
```

## Évolution de la correspondance de modèles
```
2.7:  Experimental — case/in
3.0:  Improved — pin operator, find pattern
3.1:  One-line pattern matching
3.2:  Shortcut syntax, infinite patterns
3.4:  Pattern matching stabilized
```

## Principes de conception clés
```
1. "MINASWAN" — Matz is nice and so we are nice
2. "Programmer happiness" — surprising is bad
3. "Everything is an object" — even numbers, nil, true
4. "Blocks are fundamental" — closures as first-class
5. "Duck typing" — behavior over type
6. "Convention over configuration" — Rails philosophy
```

## Croissance de l'écosystème
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
