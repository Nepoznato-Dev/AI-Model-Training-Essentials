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
# Python – Histórico e evolução da versão
## Linha do tempo
| Versão | Data de lançamento | Tema principal |
|--------|-------------|-----------|
| 1,0 | Janeiro de 1994 | Lançamento inicial |
| 1,5 | Dezembro de 1997 | Classes, exceções, módulos |
| 2.0 | Outubro de 2000 | Compreensões de lista, coleta de lixo |
| 2.2 | Dezembro de 2001 | Tipos unificados (tipos/classes), geradores |
| 2,5 | Setembro de 2006 |  Instrução `with`,`yield`como expressão |
| 2.6 | Outubro 2008 |  Importações`bytes`, `future`, transição para 3 |
| 2.7 | Julho de 2010 | Compreensão de ditado/conjunto,`argparse`|
| 3.0 | Dezembro de 2008 | **Quebra**:`print()`,`str`/`bytes`, iteradores |
| 3.3 | Setembro de 2012 | `yield from`, pacotes de namespace |
| 3.4 | Março de 2014 | `asyncio`,`pathlib`,`enum`|
| 3.5 | Setembro de 2015 | `async/await`, dicas de tipo (PEP 484), descompactação`**`|
| 3.6 | dezembro de 2016 | strings f,`async`compreh, dictos ordenados |
| 3.7 | Junho de 2018 | `dataclasses`,`contextvars`, reservado`async`|
| 3.8 | Outubro 2019 | Operador Walrus`:=`, parâmetros somente posicionais |
| 3.9 | Out 2020 | Dict union`|`, tipos genéricos`list[int]`|
| 3.10 | Out 2021 |  `match/case`, correspondência de padrão estrutural |
| 3.11 | Outubro de 2022 | Grupos de exceção, tipo `Self`, CPython mais rápido |
| 3.12 | Outubro de 2023 | Preparação GIL por interpretador, sintaxe de parâmetro de tipo |
| 3.13 | Out 2024 | Modo free-threaded (experimental), REPL aprimorado |
| 3.14 | Out 2025 | No-GIL estável, avaliação diferida de anotações |
## Marcos importantes
### Era Python 2.x (2000–2020)
- **2.0**: Compreensão de lista inspirada em Haskell; GC cíclico
- **2.2**: classe base `object`;  Palavra-chave`yield`(geradores)
- **2.5**: instrução `with`; `yield`torna-se expressão
- **2.7**: versão final 2.x; ditar compreensões; `argparse`
- **Fim da vida útil**: 1º de janeiro de 2020
### Revolução Python 3.x (2008-presente)
- **3.0**: Quebra limpa —`print`como função,`str`vs`bytes`, todos os iteradores retornam visualizações
- **3.5**: sintaxe `async`/`await`; dicas de tipo com módulo `typing`
- **3.6**: f-strings (recurso mais solicitado); `asyncio`estabilizado
- **3.8**: Operador Walrus para atribuição inline
- **3.10**: Correspondência de padrões estruturais (`match`/`case`)
- **3.11**: 10-60% mais rápido; grupos de exceção com`except*`
- **3.13**: modo experimental de thread livre (sem GIL)
## Evolução da Filosofia do Design
```
1994: "There should be one — and preferably only one — obvious way to do it"
2004: "Batteries included" (extensive stdlib)
2011: "Beautiful is better than ugly" (Zen of Python, PEP 20)
2015: Gradual typing accepted (Guido's compromise)
2018: "Black" formatter — consistency over preference
2023: Performance becomes priority (faster CPython, Shannon plan)
```

## Principais PEPs que moldaram o Python
| PEP | Ano | Recurso |
|------|------|---------|
| 20 | 2004 | Zen de Python |
| 257 | 2001 | Convenções de doutrina |
| 279 | 2002 | `enumerate()`|
| 289 | 2002 | Expressões geradoras |
| 342 | 2005 | `yield`como expressão,`send()`|
| 380 | 2009 | `yield from`|
| 484 | 2014 | Dicas de tipo |
| 492 | 2014 | `async`/`await`|
| 498 | 2015 | cordas F |
| 572 | 2018 | Operador de morsa`:=`|
| 622 | 2020 | Correspondência de padrões estruturais |
| 654 | 2021 | Grupos de exceção |
| 684 | 2022 | GIL por intérprete |
| 703 | 2023 | Tornando o GIL opcional |
## Evolução do desempenho
```
Python 3.10:  baseline
Python 3.11:  ~1.25x faster (Faster CPython project)
Python 3.12:  ~1.3x faster (specializing adaptive interpreter)
Python 3.13:  ~1.4x faster (JIT compiler experiment)
Target 3.14:  5x faster than 3.10 (Shannon plan goal)
```

## Crescimento da comunidade e do ecossistema
```
2004: PyPI launches (7,000+ packages by 2010)
2008: First PyCon (300 attendees)
2012: pip replaces easy_install
2018: Python overtakes Java in popularity (Stack Overflow)
2020: Python 2 end-of-life; 3.x migration completes
2023: 500,000+ packages on PyPI
2025: #1 most used language (multiple surveys)
```
