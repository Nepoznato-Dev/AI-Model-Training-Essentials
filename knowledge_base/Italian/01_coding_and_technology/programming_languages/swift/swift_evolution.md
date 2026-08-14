<!--
---
# Metadata
title: "Swift — Version History & Evolution"
description: "Comprehensive version history and evolution of Swift from 1.0 to modern Swift."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial version history"
tags: [swift, version-history, evolution, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "10 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

-->
# Swift: cronologia ed evoluzione delle versioni
## Cronologia
| Versione | Anno | Tema chiave |
|---------|------|-----------|
| 1.0 | 2014| Versione iniziale (Chris Lattner, Apple) |
| 1.1 | 2014| Inizializzatori fallibili,`@autoclosure`|
| 1.2 | 2015| `as?` / `as!`, `Set` type, tuple comparisons |
| 2.0 | 2015| Protocol extensions, `defer`, `guard`, `errortype` |
| 2.1 | 2015| `try?`, string interpolation in literals |
| 2.2 | 2016| `#selector`,`defer`, la tupla restituisce |
| 3.0 | 2016| **Major**: API redesign — naming conventions, `@discardableResult` |
| 4.0 | 2017 | `Codable`, `String` rewrite, multi-line literals |
| 5.0 | 2019 | **Major**: `async/await` prep, ABI stability, `Result` type |
| 5.1 | 2019 | `some` (opaque types), property wrappers, `@resultBuilder` |
| 5.2 | 2020 | Chiamata come funzione,`KeyPath`come funzione |
| 5.3 | 2020 | `@MainActor`, multiple trailing closures, `enum` improvements |
| 5.4 | 2021 | Multiple variadic parameters, `@resultBuilder` improvements |
| 5,5 | 2021 | **`async/await`**, attori,`Sendable`|
| 5.6| 2022 | `any` keyword, `Clock`, `Duration` |
| 5.7| 2022 | `if let` shorthand, `Regex` literals, `Clock` protocol |
| 5.8| 2023 | Function back deployment, `Clock` improvements |
| 5.9| 2023 | **Macros**, parameter packs, `consume`/`discard` |
| 5.10| 2024 | Complete concurrency checking, strict data race safety |
| 6.0 | 2024 | **Major**: Strict concurrency by default, typed throws |
| 6.1 | 2025 | (previsto) Ulteriori perfezionamenti della concorrenza |
## Traguardi importanti
### Swift 1.x — Nascita (2014–2015)
- **2014**: annunciato al WWDC; sostituisce Objective-C per lo sviluppo Apple
- **1.0**: opzionali, generici, chiusure, inferenza di tipo, protocolli
- **1.2**: modello`as?`/ `as!`, tipo `Set`
### Swift 2.x: gestione degli errori (2015-2016)
- **2.0**: Estensioni del protocollo (programmazione orientata al protocollo),`guard`,`defer`,`do/try/catch`
- **2.1**:`try?`per la gestione degli errori opzionale
### Swift 3.x: la grande ridenominazione delle API (2016)
- **3.0**: massiccia riprogettazione dell'API: "rinominazione unificata"
- Convenzioni di denominazione:`stringByAppendingString`→`appending`
- Rimossi i loop`for`in stile C e gli operatori`++`/ `--`
- Etichette dei primi parametri per impostazione predefinita
### Swift 4.x — Codificabile (2017)
- **4.0**: protocollo`Codable`(codifica/decodifica JSON), riscrittura `String`, valori letterali stringa multilinea
### Swift 5.x — Stabilità (2019-2024)
- **5.0**: stabilità ABI (le app diventano più piccole), tipo `Result`, stringhe grezze
- **5.1**: Tipi opachi (`some View`), wrapper di proprietà (`@State`,`@Binding`)
- **5.5**: **`async/await`**, attori, protocollo `Sendable`
- **5.9**: macro (generazione di codice in fase di compilazione), pacchetti di parametri
### Swift 6.x: sicurezza della concorrenza (2024-oggi)
- **6.0**: controllo rigoroso della concorrenza per impostazione predefinita, tipizzato lancia
## Evoluzione della concorrenza
```
1.0:  GCD (Grand Central Dispatch) — Objective-C pattern
2.0:  Protocol extensions for async patterns
5.5:  async/await, actors, Sendable
5.10: Complete concurrency checking
6.0:  Strict concurrency by default (data race safety)
```

## Digitare Evoluzione del sistema
```
1.0:  Optionals, generics, protocols
2.0:  Protocol extensions, protocol composition
4.0:  Codable, associated type constraints
5.1:  Opaque types (some), property wrappers
5.9:  Macros, parameter packs (variadic generics)
6.0:  Typed throws, strict Sendable
```

## Swift su altre piattaforme
```
2015: Swift open-sourced (Apache 2.0)
2015: Swift on Linux (Ubuntu)
2016: Swift on ARM (Raspberry Pi)
2017: Swift on Windows (experimental)
2019: TensorFlow Swift (later discontinued)
2020: Swift on AWS Lambda
2021: Vapor (server-side Swift framework)
2023: Swift on embedded systems (embedded Swift)
2025: Swift — cross-platform systems language
```

## Processo di evoluzione rapida
```
SE-0001 (2015): First proposal
Over 400 proposals accepted by 2025
Key proposals:
  SE-0044: Import as member
  SE-0110: Distributed actors
  SE-0295: Codable improvements
  SE-0302: Sendable and @Sendable closures
  SE-0335: Introduce existential any
  SE-0346: Lightweight same-type requirements (some)
  SE-0401: Remove Actor Isolation Inference
  SE-0413: Typed throws
```

## Crescita dell'ecosistema
```
2014: Swift announced — replaces Objective-C
2015: Open source; Swift Package Manager
2016: Swift 3 — API redesign
2017: Swift 4 — Codable
2019: Swift 5 — ABI stability
2021: SwiftUI matures
2023: Swift 5.9 — macros
2025: Swift 6 — data race safety; used in iOS, macOS, server, embedded
```
