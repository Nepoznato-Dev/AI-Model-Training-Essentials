<!--
---
# Metadata
title: "C++ — Version History & Evolution"
description: "Comprehensive version history and evolution of C++ from C with Classes to C++26."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial version history"
tags: [cpp, version-history, evolution, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "12 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

-->
# C++: cronologia ed evoluzione delle versioni
## Cronologia
| Versione | Anno | Tema chiave |
|---------|------|-----------|
| Cfront | 1983 | "C con classi" — classi, ereditarietà |
| C++98 | 1998 | Prima norma ISO; STL, modelli, eccezioni |
| C++03 | 2003| Correzioni di difetti |
| C++11 | 2011 | **Maggiore**: sposta semantica, lambda,`auto`, puntatori intelligenti,`nullptr`|
| C++14 | 2014| Lambda generici,`auto`return,`std::make_unique`|
| C++17 | 2017 | `std::optional`,`std::variant`,`if constexpr`, rilegature strutturate |
| C++20 | 2020 | **Maggiore**: concetti, intervalli, coroutine, moduli, `std::span`, confronto a tre vie |
| C++23 | 2024 | `std::expected`,`std::print`,`std::flat_map`, deducendo`this`|
| C++26 | ~2026 | `std::execution`, riflessione (prevista), contratti |
## Traguardi importanti
### L'era pre-standard (1983–1998)
- **1983**: Bjarne Stroustrup crea "C with Classes" ai Bell Labs
- **1985**: rinominato C++; prima edizione di "Il linguaggio di programmazione C++"
- **1989**: modelli, eccezioni, spazi dei nomi proposti
- **1990**: STL (Libreria modelli standard) di Alexander Stepanov
- **1991**: Modelli standardizzati; "Il manuale di riferimento C++ annotato"
### C++98 — La Fondazione (1998)
- Classi, ereditarietà, funzioni virtuali
- Modelli (funzioni, classi, specializzazione)
- STL: `vector`, `map`, `set`, `algorithm`,`iterator`
- Eccezioni (`try/catch/throw`)
-`namespace`, `bool`, `const_cast`,`dynamic_cast`
- Costruttori `explicit`, membri `mutable`
-RTTI (`typeid`, `dynamic_cast`)
### C++11 — Il Rinascimento (2011)
- **Sposta semantica**: riferimenti rvalue `&&`,`std::move`
- **Puntatori intelligenti**:`unique_ptr`,`shared_ptr`,`weak_ptr`
- **`auto`**: tipo inferenza
- **`nullptr`**: sostituisce`NULL`
- **Lambda**:`[](int x) { return x * 2; }`
- **Intervallo per**:`for (auto& x : container)`
- **`constexpr`**: calcolo in fase di compilazione
- **`static_assert`**: asserzioni in fase di compilazione
- **`using`**: tipo alias (in sostituzione di`typedef`)
- **Modelli variadici**:`template<typename... Args>`
- **`enum class`**: enumerazioni fortemente tipizzate
- **`override`/`final`**: controllo funzione virtuale
- **`std::thread`**: filettatura nativa
- **`std::atomic`**: programmazione senza blocco
- **`std::function`/`std::bind`**: funzioni di prima classe
### C++17 — Perfezionamento (2017)
-`std::optional<T>`, `std::variant<T...>`,`std::any`
- `if constexpr`: ramificazioni in fase di compilazione
- Attacchi strutturati:`auto [x, y] = point;`
-`std::filesystem` 
-`std::string_view` 
- Algoritmi paralleli:`std::execution::par`
- Spazi dei nomi nidificati:`namespace A::B::C {}`
-`[[nodiscard]]`, `[[maybe_unused]]`, `[[fallthrough]]`
### C++20: il linguaggio moderno (2020)
- **Concetti**: `template<std::integral T>`: modelli vincolati
- **Intervalli**: `views::filter`,`views::transform`— pipeline lente
- **Coroutine**:`co_await`,`co_yield`,`co_return`
- **Moduli**:`import`/`export`— compilazione più veloce
- **`std::span`**: vista non proprietaria di dati contigui
- **Confronto a tre**:`<=>`(operatore astronave)
- **`std::format`**: formattazione in stile Python
- **`consteval`/`constinit`**: applicazione in fase di compilazione
- **Inizializzatori designati**:`Point{.x = 1, .y = 2}`
- **`std::jthread`**: filo ad unione automatica con gettone di arresto
### C++23 — Miglioramenti pratici (2024)
-`std::expected<T, E>`— Gestione degli errori ispirata a Rust
-`std::print`/ `std::println`: output formattato velocemente
-`std::flat_map`,`std::flat_set`
- Deduzione `this`: parametro oggetto esplicito
-`std::mdspan`— campata multidimensionale
-`std::generator`— generatore sincrono
- `#include <debugging>`: punto di interruzione, dump
## Evoluzione dei modelli chiave
```
Memory Management:
  1998: Raw pointers, manual new/delete
  2011: Smart pointers (unique_ptr, shared_ptr)
  2020: std::span, views (zero-copy abstractions)
  2023: std::expected (error without exceptions)

Error Handling:
  1998: Exceptions (try/catch)
  2011: noexcept, error codes
  2023: std::expected (Rust-inspired)
  2026: Contracts (expected)

Concurrency:
  1998: None (OS threads)
  2011: std::thread, std::mutex, std::atomic
  2017: Parallel algorithms
  2020: Coroutines, std::jthread

Abstraction:
  1998: Templates (unconstrained)
  2011: Move semantics, perfect forwarding
  2020: Concepts (constrained templates)
```

## Processo di standardizzazione
```
1998: C++98 (ISO/IEC 14882:1998)
2003: C++03 (defect fixes)
2011: C++11 — "modern C++" begins
2014: C++14 — incremental
2017: C++17 — incremental
2020: C++20 — another revolution
2024: C++23 — practical improvements
2026: C++26 — reflection, contracts (expected)

3-year release cycle since C++11
```

## Impatto sull'ecosistema
```
1998: C++ dominates systems, games, finance
2005: Boost library ecosystem grows
2011: Modern C++ makes C++ safer and more expressive
2020: C++20 concepts simplify template code
2025: C++ remains #4 most used language; dominant in games, embedded, HFT, OS kernels
```
