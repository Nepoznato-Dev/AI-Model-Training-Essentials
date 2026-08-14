---
# Metadata
title: "Python — Version History & Evolution"
description: "Comprehensive version history and evolution of Python from 1.x to modern Python."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
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

# Python: cronologia ed evoluzione delle versioni
## Cronologia
| Versione | Data di rilascio | Tema chiave |
|---------|-------------|-----------|
| 1.0 | Gennaio 1994 | Versione iniziale |
| 1,5 | dicembre 1997 | Classi, eccezioni, moduli |
| 2.0 | ottobre 2000 | Comprensioni dell'elenco, raccolta dei rifiuti |
| 2.2 | dicembre 2001 | Tipi unificati (tipi/classi), generatori |
| 2,5 | settembre 2006 |  Istruzione `with`,`yield`come espressione |
| 2.6 | ottobre 2008 | `bytes`,`future`importazioni, transizione a 3 |
| 2.7 | Luglio 2010 | Comprensioni dict/set,`argparse`|
| 3.0 | dicembre 2008 | **Interruzione**:`print()`,`str`/`bytes`, iteratori |
| 3.3 | settembre 2012 | `yield from`, pacchetti dello spazio dei nomi |
| 3.4 | marzo 2014 | `asyncio`,`pathlib`,`enum`|
| 3,5 | settembre 2015 | `async/await`, suggerimenti sul tipo (PEP 484),`**`disimballaggio |
| 3.6 | dicembre 2016 | stringhe f, comprensione `async`, dict ordinati |
| 3.7 | giugno 2018 | `dataclasses`,`contextvars`, riservato`async`|
| 3.8 | ottobre 2019 | Operatore Walrus`:=`, parametri solo posizionali |
| 3.9 | Ott 2020 | Unione dict`|`, tipi generici`list[int]`|
| 3.10| Ott 2021 | `match/case`, abbinamento modello strutturale |
| 3.11 | Ott 2022 | Gruppi di eccezioni, tipo `Self`, CPython più veloce |
| 3.12 | Ott 2023 | Preparazione GIL per interprete, digitare la sintassi del parametro |
| 3.13 | ottobre 2024 | Modalità a thread libero (sperimentale), REPL migliorata |
| 3.14 | ottobre 2025 | No-GIL stabile, valutazione differita delle annotazioni |
## Traguardi importanti
### Era Python 2.x (2000-2020)
- **2.0**: comprensioni degli elenchi ispirate a Haskell; GC ciclico
- **2.2**: classe base `object`;  Parola chiave`yield`(generatori)
- **2.5**: istruzione `with`; `yield`diventa espressione
- **2.7**: versione finale 2.x; comprensioni dei dettami; `argparse`
- **Fine vita**: 1 gennaio 2020
### Python 3.x Revolution (2008-oggi)
- **3.0**: interruzione netta:`print`come funzione,`str`vs `bytes`, tutti gli iteratori restituiscono visualizzazioni
- **3.5**: sintassi`async`/ `await`; digitare suggerimenti con il modulo `typing`
- **3.6**: f-string (caratteristica più richiesta); `asyncio`stabilizzato
- **3.8**: operatore Walrus per l'assegnazione in linea
- **3.10**: Corrispondenza modello strutturale (`match`/`case`)
- **3.11**: 10-60% più veloce; gruppi di eccezioni con`except*`
- **3.13**: modalità sperimentale a thread libero (no GIL)
## Evoluzione della filosofia del design
```
1994: "There should be one — and preferably only one — obvious way to do it"
2004: "Batteries included" (extensive stdlib)
2011: "Beautiful is better than ugly" (Zen of Python, PEP 20)
2015: Gradual typing accepted (Guido's compromise)
2018: "Black" formatter — consistency over preference
2023: Performance becomes priority (faster CPython, Shannon plan)
```

## PEP chiave che hanno plasmato Python
| PEP | Anno | Caratteristica |
|------|------|---------|
| 20| 2004| Zen di Pitone |
| 257| 2001 | Convenzioni docstring |
| 279| 2002| `enumerate()`|
| 289| 2002| Espressioni del generatore |
| 342| 2005| `yield`come espressione,`send()`|
| 380| 2009| `yield from`|
| 484| 2014| Digita suggerimenti |
| 492| 2014| `async`/`await`|
| 498| 2015| f-stringhe |
| 572| 2018 | Operatore tricheco`:=`|
| 622| 2020 | Corrispondenza del modello strutturale |
| 654| 2021 | Gruppi di eccezioni |
| 684| 2022 | GIL per interprete |
| 703| 2023 | Rendere GIL facoltativo |
## Evoluzione delle prestazioni
```
Python 3.10:  baseline
Python 3.11:  ~1.25x faster (Faster CPython project)
Python 3.12:  ~1.3x faster (specializing adaptive interpreter)
Python 3.13:  ~1.4x faster (JIT compiler experiment)
Target 3.14:  5x faster than 3.10 (Shannon plan goal)
```

## Crescita della comunità e dell'ecosistema
```
2004: PyPI launches (7,000+ packages by 2010)
2008: First PyCon (300 attendees)
2012: pip replaces easy_install
2018: Python overtakes Java in popularity (Stack Overflow)
2020: Python 2 end-of-life; 3.x migration completes
2023: 500,000+ packages on PyPI
2025: #1 most used language (multiple surveys)
```
