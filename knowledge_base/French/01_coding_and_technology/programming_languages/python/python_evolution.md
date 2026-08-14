---
# Metadata
title: "Python — Version History & Evolution"
description: "Comprehensive version history and evolution of Python from 1.x to modern Python."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial version history"
tags: [python, version-history, evolution, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "12 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---
# Python — Historique et évolution des versions
## Chronologie
| Version | Date de sortie | Thème clé |
|---------|-------------|---------------|
| 1.0 | janvier 1994 | Version initiale |
| 1.5 | décembre 1997 | Classes, exceptions, modules |
| 2.0 | octobre 2000 | Compréhensions de listes, garbage collection |
| 2.2 | décembre 2001 | Types unifiés (types/classes), générateurs |
| 2.5 | septembre 2006 |  Instruction `with`,`yield`comme expression |
| 2.6 | octobre 2008 | `bytes`, importations `future`, transition vers 3 |
| 2.7 | juillet 2010 | Compréhensions de dictés/ensembles,`argparse`|
| 3.0 | décembre 2008 | **Rupture** :`print()`,`str`/`bytes`, itérateurs |
| 3.3 | septembre 2012 | `yield from`, packages d'espace de noms |
| 3.4 | mars 2014 | `asyncio`,`pathlib`,`enum`|
| 3.5 | septembre 2015 | `async/await`, astuces de type (PEP 484), déballage`**`|
| 3.6 | décembre 2016 | f-strings, compréhension `async`, dicts ordonnés |
| 3.7 | juin 2018 | `dataclasses`,`contextvars`, réservé`async`|
| 3.8 | octobre 2019 | Opérateur Walrus `:=`, paramètres de position uniquement |
| 3.9 | octobre 2020 | Union dictée`|`, types génériques`list[int]`|
| 3.10 | octobre 2021 | `match/case`, correspondance de modèles structurels |
| 3.11 | octobre 2022 | Groupes d'exceptions, type `Self`, CPython plus rapide |
| 3.12 | octobre 2023 | Préparation GIL par interprète, syntaxe des paramètres de type |
| 3.13 | octobre 2024 | Mode thread libre (expérimental), REPL amélioré |
| 3.14 | octobre 2025 | No-GIL stable, évaluation différée des annotations |
## Étapes majeures
### Ère Python 2.x (2000-2020)
- **2.0** : Compréhensions de listes inspirées de Haskell ; CPG cyclique
- **2.2** : classe de base `object` ;  Mot-clé`yield`(générateurs)
- **2.5** : instruction `with` ; `yield`devient expression
- **2.7** : version finale 2.x ; dicter les compréhensions ; `argparse`
- **Fin de vie** : 1er janvier 2020
### Révolution Python 3.x (depuis 2008)
- **3.0** : Clean break —`print`en fonction,`str`vs`bytes`, tous les itérateurs renvoient des vues
- **3.5** : syntaxe`async`/`await`; tapez des indices avec le module `typing`
- **3.6** : f-strings (fonctionnalité la plus demandée) ; `asyncio`stabilisé
- **3.8** : Opérateur Walrus pour l'affectation en ligne
- **3.10** : Correspondance de modèles structurels (`match`/`case`)
- **3.11** : 10 à 60 % plus rapide ; groupes d'exceptions avec`except*`
- **3.13** : Mode expérimental free-thread (pas de GIL)
## Évolution de la philosophie de conception
```
1994: "There should be one — and preferably only one — obvious way to do it"
2004: "Batteries included" (extensive stdlib)
2011: "Beautiful is better than ugly" (Zen of Python, PEP 20)
2015: Gradual typing accepted (Guido's compromise)
2018: "Black" formatter — consistency over preference
2023: Performance becomes priority (faster CPython, Shannon plan)
```

## PEP clés qui ont façonné Python
| PPE | Année | Fonctionnalité |
|------|------|--------------|
| 20 | 2004 | Zen de Python |
| 257 | 2001 | Conventions Docstring |
| 279 | 2002 | `enumerate()`|
| 289 | 2002 | Expressions génératrices |
| 342 | 2005 | `yield`comme expression,`send()`|
| 380 | 2009 | `yield from`|
| 484 | 2014 | Astuces de saisie |
| 492 | 2014 | `async`/`await`|
| 498 | 2015 | cordes f |
| 572 | 2018 | Opérateur de morse`:=`|
| 622 | 2020 | Correspondance des modèles structurels |
| 654 | 2021 | Groupes d'exception |
| 684 | 2022 | GIL par interprète |
| 703 | 2023 | Rendre GIL facultatif |
## Évolution des performances
```
Python 3.10:  baseline
Python 3.11:  ~1.25x faster (Faster CPython project)
Python 3.12:  ~1.3x faster (specializing adaptive interpreter)
Python 3.13:  ~1.4x faster (JIT compiler experiment)
Target 3.14:  5x faster than 3.10 (Shannon plan goal)
```

## Croissance des communautés et des écosystèmes
```
2004: PyPI launches (7,000+ packages by 2010)
2008: First PyCon (300 attendees)
2012: pip replaces easy_install
2018: Python overtakes Java in popularity (Stack Overflow)
2020: Python 2 end-of-life; 3.x migration completes
2023: 500,000+ packages on PyPI
2025: #1 most used language (multiple surveys)
```
