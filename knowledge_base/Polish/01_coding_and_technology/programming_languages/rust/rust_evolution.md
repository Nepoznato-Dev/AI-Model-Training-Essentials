---
# Metadata
title: "Rust — Version History & Evolution"
description: "Comprehensive version history and evolution of Rust from early development to modern Rust."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
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

# Rust — historia wersji i ewolucja
## Oś czasu
| Wersja | Data wydania | Kluczowy motyw |
|--------|------------|---------|
| 0,1 | styczeń 2012 | Pierwszy kompilator (rustc), współbieżność oparta na zadaniach |
| 0,5 | 2012 | System typów oparty na cechach nabiera kształtu |
| 0,6 | 2012 | Usuwanie skrzynek zarządzanych`@`|
| 0,7 | 2013 |  Usunięto `@`,`~`dla posiadanych skrzynek |
| 0,8 | 2013 | Adnotacje dożywotnie,`&mut`|
| 0,9 | styczeń 2014 | Końcowe porządki przed wersją 1.0 |
| 0,10 | luty 2014 | Ostatnie wydanie wcześniejsze niż 1.0 |
| 0,11 | kwiecień 2014 | `Box<T>`zastępuje`~T`|
| 0,12 | maj 2014 |  Rozpoczyna się przepisywanie modułu`io`|
| 1,0 | 15 maja 2015 | **Wersja stabilna** — „Rust 1.0” |
| 1.10 | sierpień 2016 |  Propagacja błędów`?`(jako`try!`→`?`) |
| 1,15 | luty 2017 | Pierwsza rdza w stajni z przygotowaniem`impl Trait`|
| 1.18 | czerwiec 2017 | `pub(crate)`, kompilacja przyrostowa |
| 1,20 | październik 2017 | Powiązane stałe |
| 1,26 | maj 2018 | `impl Trait`w pozycji argumentu/zwrotu |
| 1,28 | wrzesień 2018 | Globalne alokatory |
| 1,31 | grudzień 2018 | **Edycja Rust 2018** — moduły,`dyn Trait`|
| 1,34 | kwiecień 2019 | Rejestry alternatywne |
| 1,39 | listopad 2019 | `async/await`na stabilnym |
| 1,44 | lipiec 2020 | Ulepszenia diagnostyki |
| 1,51 | kwiecień 2021 |  Generyki`const`(MVP) |
| 1,56 | październik 2021 r. | **Rust 2021 Edition** — zamknięcia, IntoIterator |
| 1,59 | luty 2022 | Montaż liniowy |
| 1,62 | czerwiec 2022 | `#[default]`dla wyliczeń |
| 1,65 | grudzień 2022 | `let else`|
| 1,68 | marzec 2023 | `#[ffi_pure]`, optymalizacja oparta na profilu |
| 1,70 | czerwiec 2023 | Izolowane zależności`crates.io`|
| 1,74 | listopad 2023 | Tryb offline ładunku |
| 1,76 | luty 2024 | **Edycja Rust 2024** — bloki `gen`,`unsafe extern`|
| 1,79 | czerwiec 2024 | `LazyCell`,`LazyLock`|
| 1,82 | październik 2024 |  Wymagane`unsafe`w blokach`extern`|
| 1,85 | luty 2025 | Edycja Rust 2024 ustabilizowana |
## Główne kamienie milowe
### Wersja wcześniejsza niż 1.0 (2010–2015)
- **2010**: Poboczny projekt Graydona Hoare'a w Mozilli zyskuje na popularności
- **2012**: Pierwszy publiczny kompilator; system typów przechodzi poważne przeprojektowanie
- **2013**: Krystalizuje się model własności;  Usunięto pola `@`
- **2014**: Sformalizowanie procesu RFC w Rust; społeczność rośnie
- **2015**: **1,0** – gwarancja stabilności; „abstrakcje o zerowych kosztach”
### Lata wzrostu (2015–2019)
- **2015**: Cargo staje się standardowym menedżerem przesyłek
- **2018**: **Edycja Rust 2018** — remont systemu modułowego,`dyn Trait`,`impl Trait`
- **2019**:`async/await`ląduje na stabilnym poziomie — rozpoczyna się ekosystem asynchroniczny
### Dojrzałość (2020 – obecnie)
- **2021**: **Rust 2021 Edition** — ujednoznacznienie pól w domknięciach,`IntoIterator`dla tablic
- **2024**: **Rust 2024 Edition** — bloki `gen`, wymagania `unsafe extern`
- **2025**: Rdza w jądrze Linuksa, Androidzie, Windowsie, infrastrukturze AWS
## System edycji
```
Rust 2015:  The baseline (1.0)
Rust 2018:  Module system, async/await prep, dyn Trait
Rust 2021:  Closure changes, IntoIterator, panic macros
Rust 2024:  gen blocks, unsafe extern, tail expressions

Key principle: Editions are opt-in, never break existing code.
Old editions always compile. New editions add features.
```

## Ewolucja własności
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

## Asynchroniczna ewolucja
```
2018: futures 0.1 — early async with manual polling
2019: async/await syntax (Rust 1.39)
2019: tokio 0.2 — async runtime
2020: async-std — std-like async API
2021: tokio 1.0 — stable async runtime
2023: async fn in traits (Rust 1.75)
2024: async closures, improved Send bounds
```

## Rozwój ekosystemu
```
2015: crates.io launches (~2,000 crates)
2018: Rust most loved language (Stack Overflow survey)
2019: 30,000 crates on crates.io
2021: Most admired language (6th consecutive year)
2023: 130,000+ crates
2025: Used in Linux kernel, Android, Windows, Chromium, AWS, Cloudflare, Discord, Dropbox
```

## Kluczowe dokumenty RFC
| RFC | Rok | Funkcja |
|------|------|-------------|
| 25 | 2013 | Dopasowanie wzoru |
| 153 | 2014 |  Typ`Result`|
| 217 | 2014 |  Operator`?`(spróbuj) |
| 460 | 2016 | `?`zastępuje`try!`|
| 1210 | 2015 | `impl Trait`|
| 1414 | 2016 | Wydanie Rust 2018 |
| 2394 | 2018 | `async/await`|
| 2515 | 2018 |  Generyki`const`|
| 3013 | 2020 | Sprawdzanie kompilacji warunkowej |
| 3517 | 2023 |  Bloki`gen`|