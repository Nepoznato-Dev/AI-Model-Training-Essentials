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
# Python – Versionsgeschichte und Entwicklung
## Zeitleiste
| Version | Erscheinungsdatum | Schlüsselthema |
|---------|-------------|-----------|
| 1,0 | Januar 1994 | Erstveröffentlichung |
| 1,5 | Dez. 1997 | Klassen, Ausnahmen, Module |
| 2,0 | Okt. 2000 | Listenverständnis, Garbage Collection |
| 2.2 | Dez. 2001 | Einheitliche Typen (Typen/Klassen), Generatoren |
| 2,5 | September 2006 |  `with`-Anweisung,`yield`als Ausdruck |
| 2,6 | Okt. 2008 | `bytes`,`future`Importe, Übergang zu 3 |
| 2,7 | Juli 2010 | Diktat-/Satzverständnis,`argparse`|
| 3,0 | Dez. 2008 | **Breaking**:`print()`,`str`/`bytes`, Iteratoren |
| 3.3 | September 2012 | `yield from`, Namespace-Pakete |
| 3,4 | März 2014 | `asyncio`,`pathlib`,`enum`|
| 3,5 | September 2015 | `async/await`, Typhinweise (PEP 484),`**`Auspacken |
| 3,6 | Dez. 2016 | f-strings,`async`compreh, geordnete Diktate |
| 3,7 | Juni 2018 | `dataclasses`,`contextvars`, reserviert`async`|
| 3,8 | Okt. 2019 | Walross-Operator`:=`, Nur-Positions-Parameter |
| 3,9 | Okt. 2020 | Dict Union`|`, generische Typen`list[int]`|
| 3.10 | Okt. 2021 | `match/case`, Strukturmustervergleich |
| 3.11 | Okt. 2022 | Ausnahmegruppen, Typ `Self`, schnelleres CPython |
| 3.12 | Okt. 2023 | GIL-Vorbereitung pro Interpreter, Typparametersyntax |
| 3.13 | Okt. 2024 | Free-Threaded-Modus (experimentell), verbesserte REPL |
| 3.14 | Okt. 2025 | No-GIL stabile, verzögerte Auswertung von Anmerkungen |
## Wichtige Meilensteine
### Python 2.x-Ära (2000–2020)
- **2.0**: Von Haskell inspirierte Listenverständnisse; zyklische GC
- **2.2**: `object`-Basisklasse;  Schlüsselwort`yield`(Generatoren)
- **2.5**: `with`-Anweisung; `yield`wird zum Ausdruck
- **2.7**: Endgültige 2.x-Version; Diktierverständnis; `argparse`
- **Lebensende**: 1. Januar 2020
### Python 3.x Revolution (2008–heute)
- **3.0**: Sauberer Bruch –`print`als Funktion,`str`vs. `bytes`, alle Iteratoren geben Ansichten zurück
- **3.5**:`async`/ `await`-Syntax; Geben Sie Hinweise mit dem `typing`-Modul ein
- **3.6**: F-Strings (am häufigsten nachgefragte Funktion); `asyncio`stabilisiert
- **3.8**: Walross-Operator für Inline-Zuweisung
- **3.10**: Struktureller Musterabgleich (`match`/`case`)
- **3.11**: 10–60 % schneller; Ausnahmegruppen mit`except*`
- **3.13**: Experimenteller Free-Threaded-Modus (keine GIL)
## Evolution der Designphilosophie
```
1994: "There should be one — and preferably only one — obvious way to do it"
2004: "Batteries included" (extensive stdlib)
2011: "Beautiful is better than ugly" (Zen of Python, PEP 20)
2015: Gradual typing accepted (Guido's compromise)
2018: "Black" formatter — consistency over preference
2023: Performance becomes priority (faster CPython, Shannon plan)
```

## Wichtige PEPs, die Python geprägt haben
| PEP | Jahr | Funktion |
|------|------|---------|
| 20 | 2004 | Zen von Python |
| 257 | 2001 | Docstring-Konventionen |
| 279 | 2002 | `enumerate()`|
| 289 | 2002 | Generatorausdrücke |
| 342 | 2005 | `yield`als Ausdruck,`send()`|
| 380 | 2009 | `yield from`|
| 484 | 2014 | Geben Sie Hinweise ein |
| 492 | 2014 | `async`/`await`|
| 498 | 2015 | F-Saiten |
| 572 | 2018 | Walrossbetreiber`:=`|
| 622 | 2020 | Strukturmustervergleich |
| 654 | 2021 | Ausnahmegruppen |
| 684 | 2022 | GIL pro Dolmetscher |
| 703 | 2023 | GIL optional machen |
## Leistungsentwicklung
```
Python 3.10:  baseline
Python 3.11:  ~1.25x faster (Faster CPython project)
Python 3.12:  ~1.3x faster (specializing adaptive interpreter)
Python 3.13:  ~1.4x faster (JIT compiler experiment)
Target 3.14:  5x faster than 3.10 (Shannon plan goal)
```

## Gemeinschafts- und Ökosystemwachstum
```
2004: PyPI launches (7,000+ packages by 2010)
2008: First PyCon (300 attendees)
2012: pip replaces easy_install
2018: Python overtakes Java in popularity (Stack Overflow)
2020: Python 2 end-of-life; 3.x migration completes
2023: 500,000+ packages on PyPI
2025: #1 most used language (multiple surveys)
```
