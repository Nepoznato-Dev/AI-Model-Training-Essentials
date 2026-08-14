<!--
---
# Metadata
title: "Rust — Version History & Evolution"
description: "Comprehensive version history and evolution of Rust from early development to modern Rust."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial version history"
tags: [rust, version-history, evolution, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "10 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

-->
# Rust - Historial de versiones y evolución
## Línea de tiempo
| Versión | Fecha de lanzamiento | Tema clave |
|---------|-------------|-----------|
| 0,1 | enero de 2012 | Primer compilador (rustc), concurrencia basada en tareas |
| 0,5 | 2012 | El sistema de tipos basado en rasgos toma forma |
| 0,6 | 2012 | Eliminación de cajas gestionadas`@`|
| 0,7 | 2013 | `@`eliminado,`~`para cajas propias |
| 0,8 | 2013 | Anotaciones de por vida,`&mut`|
| 0,9 | enero de 2014 | Limpieza final previa a 1.0 |
| 0,10 | febrero de 2014 | Última versión anterior a la 1.0 |
| 0,11 | abril de 2014 | `Box<T>`reemplaza a`~T`|
| 0,12 | Mayo 2014 |  Comienza la reescritura del módulo`io`|
| 1.0 | 15 de mayo de 2015 | **Lanzamiento estable** — "Rust 1.0" |
| 1.10 | agosto de 2016 |  Propagación de errores`?`(como`try!`→ `?`) |
| 1.15 | febrero de 2017 | Primer Rust en establo con preparación`impl Trait`|
| 1.18 | junio de 2017 |  `pub(crate)`, compilación incremental |
| 1.20 | Octubre de 2017 | Constantes asociadas |
| 1.26 | Mayo 2018 | `impl Trait`en posición de argumento/retorno |
| 1.28 | Septiembre de 2018 | Asignadores globales |
| 1.31 | diciembre de 2018 | **Edición Rust 2018** — módulos,`dyn Trait`|
| 1,34 | abril de 2019 | Registros alternativos |
| 1,39 | noviembre de 2019 | `async/await`en establo |
| 1,44 | julio de 2020 | Mejoras en el diagnóstico |
| 1,51 | abril de 2021 | `const`genéricos (MVP) |
| 1,56 | Octubre de 2021 | **Edición Rust 2021** — cierres, IntoIterator |
| 1,59 | febrero de 2022 | Montaje en línea |
| 1,62 | junio de 2022 | `#[default]`para enumeraciones |
| 1,65 | diciembre de 2022 | `let else`|
| 1,68 | marzo de 2023 |  `#[ffi_pure]`, optimización guiada por perfiles |
| 1,70 | junio de 2023 | Dependencias`crates.io`aisladas |
| 1,74 | noviembre de 2023 | Modo de carga fuera de línea |
| 1,76 | febrero de 2024 | **Edición Rust 2024** — Bloques `gen`,`unsafe extern`|
| 1,79 | junio de 2024 |  `LazyCell`,`LazyLock`|
| 1,82 | octubre de 2024 |  Se requieren`unsafe`en bloques`extern`|
| 1,85 | febrero de 2025 | Edición Rust 2024 estabilizada |
## Hitos importantes
### Pre-1.0 (2010-2015)
- **2010**: El proyecto paralelo de Graydon Hoare en Mozilla gana terreno
- **2012**: Primer compilador público; El sistema de tipos sufre un importante rediseño.
- **2013**: Cristaliza el modelo de propiedad;  Cajas`@`eliminadas
- **2014**: Se formaliza el proceso RFC de Rust; la comunidad crece
- **2015**: **1,0** — garantía de estabilidad; "abstracciones de coste cero"
### Los años de crecimiento (2015-2019)
- **2015**: Cargo se convierte en el administrador de paquetes estándar
- **2018**: **Rust 2018 Edition** — revisión del sistema de módulos, `dyn Trait`,`impl Trait`
- **2019**:`async/await`aterriza en estable: comienza el ecosistema asíncrono
### Madurez (2020-presente)
- **2021**: **Rust 2021 Edition**: eliminar ambigüedades en los cierres,`IntoIterator`para matrices
- **2024**: **Edición Rust 2024**: bloques `gen`, requisitos `unsafe extern`
- **2025**: Rust en el kernel de Linux, Android, Windows, infraestructura de AWS
## Sistema de edición
```
Rust 2015:  The baseline (1.0)
Rust 2018:  Module system, async/await prep, dyn Trait
Rust 2021:  Closure changes, IntoIterator, panic macros
Rust 2024:  gen blocks, unsafe extern, tail expressions

Key principle: Editions are opt-in, never break existing code.
Old editions always compile. New editions add features.
```

## Evolución de la propiedad
```
2010: GC-based, like Erlang
2011: Region-based lifetimes proposed
2012: Ownership model emerges (unique, shared, owned)
2013: Simplified to &T / &mut T / Box<T>
2014: Box<T> replaces ~T; Rc<T> for shared ownership
2015: 1.0 — ownership model finalized
2018: Non-Lexical Lifetimes (NLL) in Rust 2018
2021: IntoIterator for arrays (was blocked by edition concerns)
2024: Further NLL improvements
```

## Evolución asíncrona
```
2018: futures 0.1 — early async with manual polling
2019: async/await syntax (Rust 1.39)
2019: tokio 0.2 — async runtime
2020: async-std — std-like async API
2021: tokio 1.0 — stable async runtime
2023: async fn in traits (Rust 1.75)
2024: async closures, improved Send bounds
```

## Crecimiento del ecosistema
```
2015: crates.io launches (~2,000 crates)
2018: Rust most loved language (Stack Overflow survey)
2019: 30,000 crates on crates.io
2021: Most admired language (6th consecutive year)
2023: 130,000+ crates
2025: Used in Linux kernel, Android, Windows, Chromium, AWS, Cloudflare, Discord, Dropbox
```

## RFC clave
| RFC | Año | Característica |
|------|------|---------|
| 25 | 2013 | Coincidencia de patrones |
| 153 | 2014 | `Result`tipo |
| 217 | 2014 |  Operador`?`(intentar) |
| 460 | 2016 | `?`reemplaza`try!`|
| 1210 | 2015 | `impl Trait`|
| 1414 | 2016 | Óxido edición 2018 |
| 2394 | 2018 | `async/await`|
| 2515 | 2018 | `const`genéricos |
| 3013 | 2020 | Comprobando la compilación condicional |
| 3517 | 2023 |  Bloques`gen`|