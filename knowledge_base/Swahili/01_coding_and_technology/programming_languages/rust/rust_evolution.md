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
# Kutu - Historia ya Toleo na Mageuzi
## Rekodi ya matukio
| Toleo | Tarehe ya Kutolewa | Mandhari Muhimu |
|---------|-------------|-----------|
| 0.1 | Januari 2012 | Mkusanyaji wa kwanza (rustc), upatanishi unaotegemea kazi |
| 0.5 | 2012 | Mfumo wa aina unaotegemea sifa huchukua sura |
| 0.6 | 2012 | Kuondolewa kwa visanduku vinavyodhibitiwa vya`@`|
| 0.7 | 2013 | `@`imeondolewa,`~`kwa masanduku yanayomilikiwa |
| 0.8 | 2013 | Ufafanuzi wa maisha yote,`&mut`|
| 0.9 | Januari 2014 | Usafishaji wa mwisho kabla ya 1.0 |
| 0.10 | Februari 2014 | Toleo la mwisho la kabla ya 1.0 |
| 0.11 | Aprili 2014 | `Box<T>`inachukua nafasi ya`~T`|
| 0.12 | Mei 2014 |  Kuandika upya kwa moduli ya`io`kunaanza |
| 1.0 | Mei 15, 2015 | **Toleo thabiti** — "Rust 1.0" |
| 1.10 | Agosti 2016 | `?`uenezi wa makosa (kama`try!`→`?`) |
| 1.15 | Februari 2017 | Kwanza Rust on stable na`impl Trait`prep |
| 1.18 | Juni 2017 | `pub(crate)`, mkusanyiko wa nyongeza |
| 1.20 | Oktoba 2017 | Vipengele vinavyohusishwa |
| 1.26 | Mei 2018 | `impl Trait`katika nafasi ya hoja/rejesha |
| 1.28 | Septemba 2018 | Wagawaji wa kimataifa |
| 1.31 | Desemba 2018 | **Toleo la Rust 2018** — moduli,`dyn Trait`|
| 1.34 | Aprili 2019 | Usajili mbadala |
| 1.39 | Novemba 2019 | `async/await`kwenye imara |
| 1.44 | Julai 2020 | Maboresho ya uchunguzi |
| 1.51 | Aprili 2021 |  Jenerali za`const`(MVP) |
| 1.56 | Oktoba 2021 | **Toleo la Rust 2021** - kufungwa, IntoIterator |
| 1.59 | Februari 2022 | Mkutano wa ndani |
| 1.62 | Juni 2022 | `#[default]`kwa enums |
| 1.65 | Desemba 2022 | `let else`|
| 1.68 | Machi 2023 | `#[ffi_pure]`, uboreshaji unaoongozwa na wasifu |
| 1.70 | Juni 2023 | Vitegemezi vilivyotengwa vya`crates.io`|
| 1.74 | Novemba 2023 | Mizigo ya nje ya mtandao |
| 1.76 | Februari 2024 | **Toleo la Rust 2024** —`gen`blocks,`unsafe extern`|
| 1.79 | Juni 2024 | `LazyCell`,`LazyLock`|
| 1.82 | Oktoba 2024 | `unsafe`katika vizuizi vya`extern`vinahitajika |
| 1.85 | Februari 2025 | Toleo la Rust 2024 limeimarishwa |
## Mafanikio Makuu
### Kabla ya 1.0 (2010–2015)
- **2010**: Mradi wa kando wa Graydon Hoare huko Mozilla wapata mvuto
- **2012**: Mkusanyaji wa kwanza wa umma; mfumo wa aina hupitia upya mkubwa
- **2013**: Muundo wa umiliki unang'aa;  Sanduku za`@`zimeondolewa
- **2014**: Mchakato wa Rust RFC umerasimishwa; jamii inakua
- **2015**: **1.0** - dhamana ya utulivu; "vifupisho vya gharama sifuri"
### Miaka ya Ukuaji (2015–2019)
- **2015**: Mizigo inakuwa msimamizi wa kifurushi wa kawaida
- **2018**: **Toleo la Rust 2018** — urekebishaji wa mfumo wa moduli,`dyn Trait`,`impl Trait`
- **2019**:`async/await`inatua kwa utulivu - mfumo wa ikolojia usio na usawa huanza
### Ukomavu (2020–sasa)
- **2021**: **Toleo la Rust 2021** — tenganisha sehemu zilizofungwa,`IntoIterator`kwa safu
- **2024**: **Toleo la Rust 2024** — Vitalu vya `gen`, mahitaji ya `unsafe extern`
- **2025**: Kutu katika Linux kernel, Android, Windows, miundombinu ya AWS
## Mfumo wa Toleo
```
Rust 2015:  The baseline (1.0)
Rust 2018:  Module system, async/await prep, dyn Trait
Rust 2021:  Closure changes, IntoIterator, panic macros
Rust 2024:  gen blocks, unsafe extern, tail expressions

Key principle: Editions are opt-in, never break existing code.
Old editions always compile. New editions add features.
```

## Mageuzi ya Umiliki
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

## Mageuzi ya Async
```
2018: futures 0.1 — early async with manual polling
2019: async/await syntax (Rust 1.39)
2019: tokio 0.2 — async runtime
2020: async-std — std-like async API
2021: tokio 1.0 — stable async runtime
2023: async fn in traits (Rust 1.75)
2024: async closures, improved Send bounds
```

## Ukuaji wa Mfumo ikolojia
```
2015: crates.io launches (~2,000 crates)
2018: Rust most loved language (Stack Overflow survey)
2019: 30,000 crates on crates.io
2021: Most admired language (6th consecutive year)
2023: 130,000+ crates
2025: Used in Linux kernel, Android, Windows, Chromium, AWS, Cloudflare, Discord, Dropbox
```

## RFC muhimu
| RFC | Mwaka | Kipengele |
|------|------|---------|
| 25 | 2013 | Ulinganishaji wa muundo |
| 153 | 2014 |  aina ya`Result`|
| 217 | 2014 |  Opereta wa`?`(jaribu) |
| 460 | 2016 | `?`inachukua nafasi ya`try!`|
| 1210 | 2015 | `impl Trait`|
| 1414 | 2016 | Kutu toleo la 2018 |
| 2394 | 2018 | `async/await`|
| 2515 | 2018 |  Jenerali za`const`|
| 3013 | 2020 | Kuangalia mkusanyiko wa masharti |
| 3517 | 2023 | `gen`vitalu |