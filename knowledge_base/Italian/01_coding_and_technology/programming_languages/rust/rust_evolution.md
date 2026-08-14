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
# Rust: cronologia ed evoluzione delle versioni
## Cronologia
| Versione | Data di rilascio | Tema chiave |
|---------|-------------|-----------|
| 0,1 | Gennaio 2012 | Primo compilatore (rustc), concorrenza basata su attività |
| 0,5 | 2012| Il sistema di tipo basato sui tratti prende forma |
| 0,6 | 2012| Rimozione delle caselle gestite`@`|
| 0,7 | 2013| `@`rimosso,`~`per box di proprietà |
| 0,8 | 2013| Annotazioni a vita,`&mut`|
| 0,9 | Gennaio 2014 | Pulizia finale pre-1.0 |
| 0,10 | Febbraio 2014 | Ultima versione precedente alla 1.0 |
| 0,11 | aprile 2014 | `Box<T>`sostituisce`~T`|
| 0,12 | Maggio 2014 |  Inizia la riscrittura del modulo`io`|
| 1.0 | 15 maggio 2015 | **Versione stabile** — "Rust 1.0" |
| 1.10| Agosto 2016 |  Propagazione dell'errore`?`(come`try!`→`?`) |
| 1.15| Febbraio 2017 | Prima ruggine su stalla con preparazione`impl Trait`|
| 1.18 | giugno 2017 | `pub(crate)`, compilazione incrementale |
| 1.20| ottobre 2017 | Costanti associate |
| 1.26 | Maggio 2018 | `impl Trait`nella posizione argomento/ritorno |
| 1.28 | settembre 2018 | Assegnatori globali |
| 1.31 | dicembre 2018 | **Edizione Rust 2018** — moduli,`dyn Trait`|
| 1.34 | aprile 2019 | Registri alternativi |
| 1,39 | novembre 2019 | `async/await`su stabile |
| 1.44| Lug 2020 | Miglioramenti della diagnostica |
| 1,51 | aprile 2021 | `const`generici (MVP) |
| 1,56| Ott 2021 | **Edizione Rust 2021** — chiusure, IntoIterator |
| 1,59 | Febbraio 2022 | Assemblaggio in linea |
| 1,62 | giugno 2022 | `#[default]`per enumerazioni |
| 1,65| dic 2022 | `let else`|
| 1,68 | marzo 2023 | `#[ffi_pure]`, ottimizzazione guidata dal profilo |
| 1,70| giugno 2023 | Dipendenze`crates.io`isolate |
| 1,74 | novembre 2023 | Modalità offline carico |
| 1,76 | Febbraio 2024 | **Edizione Rust 2024** — Blocchi `gen`,`unsafe extern`|
| 1,79 | giugno 2024 | `LazyCell`,`LazyLock`|
| 1,82 | ottobre 2024 | `unsafe`nei blocchi`extern`richiesti |
| 1,85| Febbraio 2025 | Edizione Rust 2024 stabilizzata |
## Traguardi importanti
### Pre-1.0 (2010–2015)
- **2010**: il progetto parallelo di Graydon Hoare presso Mozilla prende piede
- **2012**: Primo compilatore pubblico; il sistema di tipi subisce un'importante riprogettazione
- **2013**: il modello di proprietà si cristallizza;  Scatole`@`rimosse
- **2014**: Formalizzato il processo Rust RFC; la comunità cresce
- **2015**: **1,0** — garanzia di stabilità; "Astrazioni a costo zero"
### Gli anni della crescita (2015–2019)
- **2015**: Cargo diventa il gestore di pacchetti standard
- **2018**: **Edizione Rust 2018** - revisione del sistema dei moduli, `dyn Trait`,`impl Trait`
- **2019**:`async/await`arriva su stabile: inizia l'ecosistema asincrono
### Maturità (2020-oggi)
- **2021**: **Rust 2021 Edition**: disambigua i campi nelle chiusure,`IntoIterator`per gli array
- **2024**: **Edizione Rust 2024** — Blocchi `gen`, requisiti `unsafe extern`
- **2025**: Rust nel kernel Linux, Android, Windows, infrastruttura AWS
## Sistema di edizione
```
Rust 2015:  The baseline (1.0)
Rust 2018:  Module system, async/await prep, dyn Trait
Rust 2021:  Closure changes, IntoIterator, panic macros
Rust 2024:  gen blocks, unsafe extern, tail expressions

Key principle: Editions are opt-in, never break existing code.
Old editions always compile. New editions add features.
```

## Evoluzione della proprietà
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

## Evoluzione asincrona
```
2018: futures 0.1 — early async with manual polling
2019: async/await syntax (Rust 1.39)
2019: tokio 0.2 — async runtime
2020: async-std — std-like async API
2021: tokio 1.0 — stable async runtime
2023: async fn in traits (Rust 1.75)
2024: async closures, improved Send bounds
```

## Crescita dell'ecosistema
```
2015: crates.io launches (~2,000 crates)
2018: Rust most loved language (Stack Overflow survey)
2019: 30,000 crates on crates.io
2021: Most admired language (6th consecutive year)
2023: 130,000+ crates
2025: Used in Linux kernel, Android, Windows, Chromium, AWS, Cloudflare, Discord, Dropbox
```

## RFC chiave
| RFC | Anno | Caratteristica |
|------|------|---------|
| 25| 2013| Corrispondenza di modelli |
| 153| 2014| `Result`tipo |
| 217| 2014| `?`(prova) operatore |
| 460| 2016| `?`sostituisce`try!`|
| 1210| 2015| `impl Trait`|
| 1414| 2016| Ruggine edizione 2018 |
| 2394| 2018 | `async/await`|
| 2515| 2018 | `const`generici |
| 3013| 2020 | Controllo della compilazione condizionale |
| 3517| 2023 | `gen`blocchi |