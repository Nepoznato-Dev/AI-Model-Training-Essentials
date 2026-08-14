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
# Rust – Versionsgeschichte und Entwicklung
## Zeitleiste
| Version | Erscheinungsdatum | Schlüsselthema |
|---------|-------------|-----------|
| 0,1 | Januar 2012 | Erster Compiler (rustc), aufgabenbasierte Parallelität |
| 0,5 | 2012 | Merkmalsbasiertes Typensystem nimmt Gestalt an |
| 0,6 | 2012 | Entfernung der verwalteten `@`-Boxen |
| 0,7 | 2013 | `@`entfernt,`~`für eigene Boxen |
| 0,8 | 2013 | Lebenslange Anmerkungen,`&mut`|
| 0,9 | Januar 2014 | Letzte Bereinigung vor 1.0 |
| 0,10 | Februar 2014 | Letzte Version vor 1.0 |
| 0,11 | April 2014 | `Box<T>`ersetzt`~T`|
| 0,12 | Mai 2014 |  Das Neuschreiben des `io`-Moduls beginnt |
| 1,0 | 15. Mai 2015 | **Stabile Version** – „Rust 1.0“ |
| 1.10 | August 2016 | `?`Fehlerausbreitung (als`try!`→ `?`) |
| 1,15 | Februar 2017 | Erster Rost am Stall mit`impl Trait`prep |
| 1,18 | Juni 2017 | `pub(crate)`, inkrementelle Kompilierung |
| 1,20 | Okt. 2017 | Zugehörige Konstanten |
| 1,26 | Mai 2018 | `impl Trait`in Argument-/Rückgabeposition |
| 1,28 | September 2018 | Globale Allokatoren |
| 1,31 | Dez. 2018 | **Rust 2018 Edition** – Module,`dyn Trait`|
| 1,34 | April 2019 | Alternative Register |
| 1,39 | November 2019 | `async/await`auf stabil |
| 1,44 | Juli 2020 | Diagnoseverbesserungen |
| 1,51 | Apr. 2021 | `const`Generika (MVP) |
| 1,56 | Okt. 2021 | **Rust 2021 Edition** – Schließungen, IntoIterator |
| 1,59 | Februar 2022 | Inline-Montage |
| 1,62 | Juni 2022 | `#[default]`für Aufzählungen |
| 1,65 | Dez. 2022 | `let else`|
| 1,68 | März 2023 | `#[ffi_pure]`, profilgeführte Optimierung |
| 1,70 | Juni 2023 | Isolierte `crates.io`-Abhängigkeiten |
| 1,74 | Nov. 2023 | Fracht-Offline-Modus |
| 1,76 | Februar 2024 | **Rust 2024 Edition** – `gen`-Blöcke,`unsafe extern`|
| 1,79 | Juni 2024 | `LazyCell`,`LazyLock`|
| 1,82 | Okt. 2024 | `unsafe`in `extern`-Blöcken erforderlich |
| 1,85 | Februar 2025 | Rust 2024 Edition stabilisiert |
## Wichtige Meilensteine
### Vor 1.0 (2010–2015)
- **2010**: Graydon Hoares Nebenprojekt bei Mozilla gewinnt an Bedeutung
- **2012**: Erster öffentlicher Compiler; Das Typensystem wird einer umfassenden Neugestaltung unterzogen
- **2013**: Eigentumsmodell kristallisiert sich heraus;  `@`-Boxen entfernt
- **2014**: Rust RFC-Prozess formalisiert; Gemeinschaft wächst
- **2015**: **1.0** – Stabilitätsgarantie; „Kostenlose Abstraktionen“
### Die Wachstumsjahre (2015–2019)
- **2015**: Cargo wird zum Standard-Paketmanager
- **2018**: **Rust 2018 Edition** – Überarbeitung des Modulsystems, `dyn Trait`,`impl Trait`
- **2019**:`async/await`landet im stabilen – asynchronen Ökosystem beginnt
### Fälligkeit (2020–heute)
- **2021**: **Rust 2021 Edition** – Felder in Abschlüssen eindeutig machen,`IntoIterator`für Arrays
- **2024**: **Rust 2024 Edition** – `gen`-Blöcke, `unsafe extern`-Anforderungen
- **2025**: Rust im Linux-Kernel, Android, Windows, AWS-Infrastruktur
## Editionssystem
```
Rust 2015:  The baseline (1.0)
Rust 2018:  Module system, async/await prep, dyn Trait
Rust 2021:  Closure changes, IntoIterator, panic macros
Rust 2024:  gen blocks, unsafe extern, tail expressions

Key principle: Editions are opt-in, never break existing code.
Old editions always compile. New editions add features.
```

## Eigentumsentwicklung
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

## Asynchrone Entwicklung
```
2018: futures 0.1 — early async with manual polling
2019: async/await syntax (Rust 1.39)
2019: tokio 0.2 — async runtime
2020: async-std — std-like async API
2021: tokio 1.0 — stable async runtime
2023: async fn in traits (Rust 1.75)
2024: async closures, improved Send bounds
```

## Ökosystemwachstum
```
2015: crates.io launches (~2,000 crates)
2018: Rust most loved language (Stack Overflow survey)
2019: 30,000 crates on crates.io
2021: Most admired language (6th consecutive year)
2023: 130,000+ crates
2025: Used in Linux kernel, Android, Windows, Chromium, AWS, Cloudflare, Discord, Dropbox
```

## Wichtige RFCs
| RFC | Jahr | Funktion |
|------|------|---------|
| 25 | 2013 | Mustervergleich |
| 153 | 2014 |  `Result`-Typ |
| 217 | 2014 | `?`(versuchen) Operator |
| 460 | 2016 | `?`ersetzt`try!`|
| 1210 | 2015 | `impl Trait`|
| 1414 | 2016 | Rust-Ausgabe 2018 |
| 2394 | 2018 | `async/await`|
| 2515 | 2018 | `const`Generika |
| 3013 | 2020 | Bedingte Kompilierung prüfen |
| 3517 | 2023 |  `gen`-Blöcke |