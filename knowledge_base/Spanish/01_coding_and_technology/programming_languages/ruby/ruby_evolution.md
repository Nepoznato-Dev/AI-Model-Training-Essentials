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
# Ruby: Historial de versiones y evolución
## Línea de tiempo
| Versión | Año | Tema clave |
|---------|------|-----------|
| 0,95 | 1995 | Lanzamiento inicial (Yukihiro "Matz" Matsumoto) |
| 1.0 | 1996 | Primera versión estable |
| 1.2 | 1998 | Primera documentación en inglés |
| 1.4 | 1999 | `BEGIN`/`END`,`String#unpack`|
| 1.6 | 2000 | Mejoras en la recogida de basura |
| 1.8 | 2003 | $KCODE, motor de expresiones regulares oniguruma |
| 1.9 | 2007 | **Principal**: M17N (multilingüe), nueva sintaxis hash, fibras |
| 2.0 | 2013 | Argumentos de palabras clave, `Enumerator::Lazy`,`Module#prepend`|
| 2.1 | 2013 | Llamadas a métodos refinados,`frozen_string_literal`|
| 2.2 | 2014 | Símbolo GC, GC incremental |
| 2.3 | 2015 | Pragma literal de cadena congelada, navegación segura`&.`|
| 2.4 | 2016 | `Integer`unificado,`String`Mapeo de casos Unicode |
| 2.5 | 2017 |  `yield_self`, bloques en `rescue`/`ensure` |
| 2.6 | 2018 | **Compilador JIT (MJIT)**, rango infinito`1..`|
| 2.7 | 2019 | Coincidencia de patrones (experimental), parámetros de bloques numerados |
| 3.0 | 2020 | **Principales**: Ractor (concurrencia), Fiber Scheduler, tipos de RBS |
| 3.1 | 2021 | `Anonymous`reenvío de bloques,`Hash#compact`|
| 3.2 | 2022 |  Clase `Data`, mejoras `File.realpath`, producción YJIT |
| 3.3 | 2023 | **YJIT** mejoras importantes, parámetro de bloque`it`|
| 3.4 | 2024 | Analizador de prismas predeterminado,`it`como parámetro de bloque predeterminado |
## Hitos importantes
### Rubí temprano (1995-2003)
- **1995**: Matz crea Ruby, combinando Perl, Smalltalk y Lisp.
- **1.0 (1996)**: Primera versión estable
- **1.8 (2003)**: El Ruby "clásico": rápido, estable y ampliamente adoptado
### La era de los rieles (2004-2013)
- **2004**: Lanzamiento de Ruby on Rails: revolución del desarrollo web
- **1.9 (2007)**: M17N (cadenas multilingües), nueva sintaxis hash `{key: value}`, fibras
- **2.0 (2013)**: argumentos de palabras clave, enumeradores diferidos, `Module#prepend`
### Rubí moderno (2015-presente)
- **2.6 (2018)**: compilador JIT (MJIT): primer impulso de rendimiento
- **2.7 (2019)**: Coincidencia de patrones (experimental), parámetros de bloque numerados`_1`
- **3.0 (2020)**: **Ractor** (simultaneidad de modelo de actor), **Fiber Scheduler** (E/S asíncrona), **RBS** (firmas de tipo)
- **3.2 (2022)**: clase`Data`(objetos de valor inmutable), YJIT listo para producción
- **3.3 (2023)**: Aceleraciones importantes de YJIT (hasta 3 veces más rápidas), parámetro de bloque `it`
- **3.4 (2024)**: el analizador de prismas pasa a ser el predeterminado
## Evolución del rendimiento
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

## Evolución de la concurrencia
```
1.8:  Green threads (GIL)
1.9:  Native threads (still GIL)
2.0:  Fiber (cooperative)
2.6:  Fiber Scheduler proposal
3.0:  Ractor (Actor model, no GIL sharing)
3.0:  Fiber Scheduler (async I/O without threads)
3.3:  Improved Fiber Scheduler
```

## Evolución de la coincidencia de patrones
```
2.7:  Experimental — case/in
3.0:  Improved — pin operator, find pattern
3.1:  One-line pattern matching
3.2:  Shortcut syntax, infinite patterns
3.4:  Pattern matching stabilized
```

## Principios clave de diseño
```
1. "MINASWAN" — Matz is nice and so we are nice
2. "Programmer happiness" — surprising is bad
3. "Everything is an object" — even numbers, nil, true
4. "Blocks are fundamental" — closures as first-class
5. "Duck typing" — behavior over type
6. "Convention over configuration" — Rails philosophy
```

## Crecimiento del ecosistema
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
