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

# Python: historial de versiones y evolución
## Línea de tiempo
| Versión | Fecha de lanzamiento | Tema clave |
|---------|-------------|-----------|
| 1.0 | Enero de 1994 | Lanzamiento inicial |
| 1.5 | diciembre de 1997 | Clases, excepciones, módulos |
| 2.0 | Octubre de 2000 | Listas por comprensión, recolección de basura |
| 2.2 | diciembre de 2001 | Tipos unificados (tipos/clases), generadores |
| 2.5 | Septiembre de 2006 |  Declaración `with`,`yield`como expresión |
| 2.6 | Octubre de 2008 |  Importaciones `bytes`, `future`, transición a 3 |
| 2.7 | julio de 2010 | Comprensiones de dictado/conjunto,`argparse`|
| 3.0 | diciembre de 2008 | **Última hora**: `print()`,`str`/ `bytes`, iteradores |
| 3.3 | Septiembre de 2012 |  `yield from`, paquetes de espacios de nombres |
| 3.4 | marzo de 2014 |  `asyncio`, `pathlib`,`enum`|
| 3.5 | Septiembre de 2015 |  `async/await`, sugerencias de tipo (PEP 484), desembalaje`**`|
| 3.6 | diciembre de 2016 | cuerdas f, comprensión `async`, dictados ordenados |
| 3.7 | junio de 2018 |  `dataclasses`, `contextvars`, reservado`async`|
| 3.8 | Octubre de 2019 | Operador de morsa `:=`, parámetros solo posicionales |
| 3.9 | octubre de 2020 | Unión dictada `|`, tipos genéricos`list[int]`|
| 3.10 | Octubre de 2021 |  `match/case`, coincidencia de patrones estructurales |
| 3.11 | Octubre de 2022 | Grupos de excepciones, tipo `Self`, CPython más rápido |
| 3.12 | octubre de 2023 | Preparación GIL por intérprete, sintaxis de parámetro de tipo |
| 3.13 | octubre de 2024 | Modo de subproceso libre (experimental), REPL mejorado |
| 3.14 | octubre de 2025 | Evaluación estable y diferida de anotaciones sin GIL |
## Hitos importantes
### Era Python 2.x (2000-2020)
- **2.0**: Listas por comprensión inspiradas en Haskell; GC cíclico
- **2.2**: clase base `object`;  Palabra clave`yield`(generadores)
- **2.5**: declaración `with`; `yield`se convierte en expresión
- **2.7**: versión final 2.x; dictar comprensiones; `argparse`
- **Fin de vida**: 1 de enero de 2020
### Revolución de Python 3.x (2008-presente)
- **3.0**: ruptura limpia:`print`como función,`str`vs `bytes`, todos los iteradores devuelven vistas
- **3.5**: sintaxis`async`/ `await`; escriba sugerencias con el módulo `typing`
- **3.6**: cuerdas f (función más solicitada); `asyncio`estabilizado
- **3.8**: operador de morsa para asignación en línea
- **3.10**: Coincidencia de patrones estructurales (`match`/`case`)
- **3.11**: 10-60 % más rápido; grupos de excepción con`except*`
- **3.13**: Modo experimental de subprocesos libres (sin GIL)
## Evolución de la filosofía del diseño
```
1994: "There should be one — and preferably only one — obvious way to do it"
2004: "Batteries included" (extensive stdlib)
2011: "Beautiful is better than ugly" (Zen of Python, PEP 20)
2015: Gradual typing accepted (Guido's compromise)
2018: "Black" formatter — consistency over preference
2023: Performance becomes priority (faster CPython, Shannon plan)
```

## PEP clave que dieron forma a Python
| PEP | Año | Característica |
|------|------|---------|
| 20 | 2004 | Zen de Pitón |
| 257 | 2001 | Convenciones de cadenas de documentos |
| 279 | 2002 | `enumerate()`|
| 289 | 2002 | Expresiones generadoras |
| 342 | 2005 | `yield`como expresión,`send()`|
| 380 | 2009 | `yield from`|
| 484 | 2014 | Escriba sugerencias |
| 492 | 2014 | `async`/`await`|
| 498 | 2015 | cuerdas f |
| 572 | 2018 | Operador de morsa`:=`|
| 622 | 2020 | Coincidencia de patrones estructurales |
| 654 | 2021 | Grupos de excepción |
| 684 | 2022 | Por intérprete GIL |
| 703 | 2023 | Hacer que GIL sea opcional |
## Evolución del rendimiento
```
Python 3.10:  baseline
Python 3.11:  ~1.25x faster (Faster CPython project)
Python 3.12:  ~1.3x faster (specializing adaptive interpreter)
Python 3.13:  ~1.4x faster (JIT compiler experiment)
Target 3.14:  5x faster than 3.10 (Shannon plan goal)
```

## Crecimiento de comunidades y ecosistemas
```
2004: PyPI launches (7,000+ packages by 2010)
2008: First PyCon (300 attendees)
2012: pip replaces easy_install
2018: Python overtakes Java in popularity (Stack Overflow)
2020: Python 2 end-of-life; 3.x migration completes
2023: 500,000+ packages on PyPI
2025: #1 most used language (multiple surveys)
```
