<!--
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

-->
# Python - Historia ya Toleo na Mageuzi
## Rekodi ya matukio
| Toleo | Tarehe ya Kutolewa | Mandhari Muhimu |
|---------|-------------|-----------|
| 1.0 | Januari 1994 | Toleo la awali |
| 1.5 | Desemba 1997 | Madarasa, vighairi, moduli |
| 2.0 | Oktoba 2000 | Ufahamu wa orodha, ukusanyaji wa takataka |
| 2.2 | Desemba 2001 | Aina zilizounganishwa (aina/madarasa), jenereta |
| 2.5 | Septemba 2006 |  Taarifa ya `with`,`yield`kama usemi |
| 2.6 | Oktoba 2008 | `bytes`,`future`uagizaji, mpito hadi 3 |
| 2.7 | Julai 2010 | Dict/weka ufahamu,`argparse`|
| 3.0 | Desemba 2008 | **Kuvunja**:`print()`,`str`/`bytes`, warudiaji |
| 3.3 | Septemba 2012 | `yield from`, vifurushi vya nafasi ya majina |
| 3.4 | Machi 2014 | `asyncio`,`pathlib`,`enum`|
| 3.5 | Septemba 2015 | `async/await`, aina ya vidokezo (PEP 484),`**`unpacking |
| 3.6 | Desemba 2016 | f-strings,`async`compreh, dicts zilizoagizwa |
| 3.7 | Juni 2018 | `dataclasses`,`contextvars`, zimehifadhiwa`async`|
| 3.8 | Oktoba 2019 | Opereta wa Walrus`:=`, vigezo vya nafasi pekee |
| 3.9 | Oktoba 2020 | Dict union`|`, aina za jumla`list[int]`|
| 3.10 | Oktoba 2021 | `match/case`, muundo wa muundo unaolingana |
| 3.11 | Oktoba 2022 | Vikundi vya ubaguzi, aina ya `Self`, CPython ya haraka zaidi |
| 3.12 | Oktoba 2023 | Matayarisho ya GIL ya kila mkalimani, chapa sintaksia ya kigezo |
| 3.13 | Oktoba 2024 | Hali yenye nyuzi bila malipo (ya majaribio), REPL | iliyoboreshwa
| 3.14 | Oktoba 2025 | No-GIL tathmini thabiti, iliyoahirishwa kwa maelezo |
## Mafanikio Makuu
### Python 2.x Era (2000–2020)
- **2.0**: Orodha ya ufahamu iliyoongozwa na Haskell; GC ya mzunguko
- **2.2**: darasa la msingi la `object`; `yield`neno kuu (jenereta)
- **2.5**: Taarifa ya `with`; `yield`inakuwa usemi
- ** 2.7 **: Mwisho 2.x kutolewa; ufahamu wa maagizo; `argparse`
- **Mwisho wa maisha**: Januari 1, 2020
### Chatu 3.x Mapinduzi (2008–sasa)
- **3.0**: Mapumziko safi —`print`kama utendaji,`str`dhidi ya`bytes`, warudiaji wote wanarudisha maoni
- **3.5**:`async`/`await`syntax; aina ya vidokezo na moduli ya `typing`
- **3.6**: f-strings (kipengele kilichoombwa zaidi); `asyncio`imetulia
- **3.8**: Opereta wa Walrus kwa mgawo wa ndani
- **3.10**: Ulinganifu wa muundo wa muundo (`match`/`case`)
- ** 3.11 **: 10-60% kwa kasi; vikundi vya ubaguzi vilivyo na`except*`
- **3.13**: Hali ya majaribio isiyo na nyuzi (hakuna GIL)
## Mageuzi ya Falsafa ya Usanifu
```
1994: "There should be one — and preferably only one — obvious way to do it"
2004: "Batteries included" (extensive stdlib)
2011: "Beautiful is better than ugly" (Zen of Python, PEP 20)
2015: Gradual typing accepted (Guido's compromise)
2018: "Black" formatter — consistency over preference
2023: Performance becomes priority (faster CPython, Shannon plan)
```

## PEPs Muhimu Zilizotengeneza Chatu
| PEP | Mwaka | Kipengele |
|------|------|---------|
| 20 | 2004 | Zen ya Python |
| 257 | 2001 | Makubaliano ya hati |
| 279 | 2002 | `enumerate()`|
| 289 | 2002 | Maneno ya jenereta |
| 342 | 2005 | `yield`kama usemi,`send()`|
| 380 | 2009 | `yield from`|
| 484 | 2014 | Andika vidokezo |
| 492 | 2014 | `async`/`await`|
| 498 | 2015 | f-strings |
| 572 | 2018 | Opereta wa Walrus`:=`|
| 622 | 2020 | Ulinganifu wa muundo wa muundo |
| 654 | 2021 | Vikundi vya ubaguzi |
| 684 | 2022 | GIL ya kila mkalimani |
| 703 | 2023 | Kufanya GIL kuwa ya hiari |
## Mageuzi ya Utendaji
```
Python 3.10:  baseline
Python 3.11:  ~1.25x faster (Faster CPython project)
Python 3.12:  ~1.3x faster (specializing adaptive interpreter)
Python 3.13:  ~1.4x faster (JIT compiler experiment)
Target 3.14:  5x faster than 3.10 (Shannon plan goal)
```

## Ukuaji wa Jumuiya na Mfumo ikolojia
```
2004: PyPI launches (7,000+ packages by 2010)
2008: First PyCon (300 attendees)
2012: pip replaces easy_install
2018: Python overtakes Java in popularity (Stack Overflow)
2020: Python 2 end-of-life; 3.x migration completes
2023: 500,000+ packages on PyPI
2025: #1 most used language (multiple surveys)
```
