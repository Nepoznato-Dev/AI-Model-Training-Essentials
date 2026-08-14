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
# Python — Kasaysayan ng Bersyon at Ebolusyon
## Timeline
| Bersyon | Petsa ng Paglabas | Pangunahing Tema |
|---------|-------------|-----------|
| 1.0 | Ene 1994 | Paunang paglabas |
| 1.5 | Dis 1997 | Mga klase, exception, modules |
| 2.0 | Okt 2000 | Listahan ng mga pag-unawa, pagkolekta ng basura |
| 2.2 | Dis 2001 | Pinag-isang uri (mga uri/klase), mga generator |
| 2.5 | Set 2006 | `with`na pahayag,`yield`bilang expression |
| 2.6 | Okt 2008 | `bytes`,`future`import, paglipat sa 3 |
| 2.7 | Hul 2010 | Dict/set comprehension,`argparse`|
| 3.0 | Dis 2008 | **Breaking**:`print()`,`str`/`bytes`, mga iterator |
| 3.3 | Set 2012 | `yield from`, mga namespace na pakete |
| 3.4 | Mar 2014 | `asyncio`,`pathlib`,`enum`|
| 3.5 | Set 2015 | `async/await`, uri ng mga pahiwatig (PEP 484),`**`pag-unpack |
| 3.6 | Dis 2016 | f-strings,`async`compreh, ordered dicts |
| 3.7 | Hun 2018 | `dataclasses`,`contextvars`, nakalaan`async`|
| 3.8 | Okt 2019 | Walrus operator`:=`, positional-only params |
| 3.9 | Okt 2020 | Dict union`|`, mga generic na uri`list[int]`|
| 3.10 | Okt 2021 | `match/case`, pagtutugma ng pattern ng istruktura |
| 3.11 | Okt 2022 | Exception group,`Self`type, mas mabilis na CPython |
| 3.12 | Okt 2023 | Per-interpreter GIL prep, uri ng parameter syntax |
| 3.13 | Okt 2024 | Free-threaded mode (pang-eksperimento), pinahusay na REPL |
| 3.14 | Okt 2025 | Walang-GIL stable, ipinagpaliban ang pagsusuri ng mga anotasyon |
## Mga Pangunahing Milestone
### Python 2.x Era (2000–2020)
- **2.0**: Listahan ng mga pag-unawa na inspirasyon ng Haskell; paikot na GC
- **2.2**:`object`batayang klase; `yield`keyword (mga generator)
- **2.5**:`with`na pahayag;  Nagiging expression ang `yield`
- **2.7**: Panghuling 2.x na paglabas; dict comprehension; `argparse`
- **Pagtatapos ng buhay**: Enero 1, 2020
### Python 3.x Revolution (2008–kasalukuyan)
- **3.0**: Clean break —`print`bilang function,`str`vs`bytes`, lahat ng iterator ay nagbabalik ng mga view
- **3.5**:`async`/`await`syntax; mag-type ng mga pahiwatig gamit ang`typing`module
- **3.6**: f-strings (pinaka hinihiling na feature);  Na-stabilize ang `asyncio`
- **3.8**: Walrus operator para sa inline na pagtatalaga
- **3.10**: Pagtutugma ng pattern ng istruktura (`match`/`case`)
- **3.11**: 10-60% mas mabilis; mga pangkat ng exception na may`except*`
- **3.13**: Eksperimental na free-threaded mode (walang GIL)
## Ebolusyon ng Pilosopiya ng Disenyo
```
1994: "There should be one — and preferably only one — obvious way to do it"
2004: "Batteries included" (extensive stdlib)
2011: "Beautiful is better than ugly" (Zen of Python, PEP 20)
2015: Gradual typing accepted (Guido's compromise)
2018: "Black" formatter — consistency over preference
2023: Performance becomes priority (faster CPython, Shannon plan)
```

## Mga Pangunahing PEP na Hugis Python
| PEP | Taon | Tampok |
|------|------|---------|
| 20 | 2004 | Zen ng Python |
| 257 | 2001 | Docstring convention |
| 279 | 2002 | `enumerate()`|
| 289 | 2002 | Mga expression ng generator |
| 342 | 2005 | `yield`bilang expression,`send()`|
| 380 | 2009 | `yield from`|
| 484 | 2014 | I-type ang mga pahiwatig |
| 492 | 2014 | `async`/`await`|
| 498 | 2015 | f-strings |
| 572 | 2018 | Walrus operator`:=`|
| 622 | 2020 | Pagtutugma ng pattern ng istruktura |
| 654 | 2021 | Mga pangkat ng pagbubukod |
| 684 | 2022 | Per-interpreter GIL |
| 703 | 2023 | Ginagawang opsyonal ang GIL |
## Ebolusyon ng Pagganap
```
Python 3.10:  baseline
Python 3.11:  ~1.25x faster (Faster CPython project)
Python 3.12:  ~1.3x faster (specializing adaptive interpreter)
Python 3.13:  ~1.4x faster (JIT compiler experiment)
Target 3.14:  5x faster than 3.10 (Shannon plan goal)
```

## Paglago ng Komunidad at Ecosystem
```
2004: PyPI launches (7,000+ packages by 2010)
2008: First PyCon (300 attendees)
2012: pip replaces easy_install
2018: Python overtakes Java in popularity (Stack Overflow)
2020: Python 2 end-of-life; 3.x migration completes
2023: 500,000+ packages on PyPI
2025: #1 most used language (multiple surveys)
```
