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
# C++ – Versionsverlauf und Entwicklung
## Zeitleiste
| Version | Jahr | Schlüsselthema |
|---------|------|-----------|
| Cfront | 1983 | „C mit Klassen“ – Klassen, Vererbung |
| C++98 | 1998 | Erster ISO-Standard; STL, Vorlagen, Ausnahmen |
| C++03 | 2003 | Fehlerbehebungen |
| C++11 | 2011 | **Hauptsächlich**: Bewegungssemantik, Lambdas, `auto`, intelligente Zeiger,`nullptr`|
| C++14 | 2014 | Generische Lambdas,`auto`return,`std::make_unique`|
| C++17 | 2017 | `std::optional`,`std::variant`,`if constexpr`, strukturierte Bindungen |
| C++20 | 2020 | **Hauptfach**: Konzepte, Bereiche, Coroutinen, Module,`std::span`, Drei-Wege-Vergleich |
| C++23 | 2024 | `std::expected`,`std::print`,`std::flat_map`, abgeleitet von`this`|
| C++26 | ~2026 | `std::execution`, Reflexion (erwartet), Verträge |
## Wichtige Meilensteine
### Die Pre-Standard-Ära (1983–1998)
- **1983**: Bjarne Stroustrup erstellt „C with Classes“ bei Bell Labs
- **1985**: Umbenannt in C++; erste Ausgabe von „The C++ Programming Language“
- **1989**: Vorlagen, Ausnahmen, Namensräume vorgeschlagen
- **1990**: STL (Standard Template Library) von Alexander Stepanov
- **1991**: Vorlagen standardisiert; „Das Annotated C++ Referenzhandbuch“
### C++98 – Die Stiftung (1998)
- Klassen, Vererbung, virtuelle Funktionen
- Vorlagen (Funktionen, Klassen, Spezialisierung)
- STL: `vector`, `map`, `set`, `algorithm`,`iterator`
- Ausnahmen (`try/catch/throw`)
- `namespace`, `bool`, `const_cast`,`dynamic_cast`
- `explicit`-Konstruktoren, `mutable`-Mitglieder
- RTTI (`typeid`, `dynamic_cast`)
### C++11 – Die Renaissance (2011)
- **Semantik verschieben**:`&&`R-Wert-Referenzen,`std::move`
- **Intelligente Zeiger**: `unique_ptr`, `shared_ptr`,`weak_ptr`
- **`auto`**: Typinferenz
- **`nullptr`**: ersetzt`NULL`
- **Lambdas**:`[](int x) { return x * 2; }`
- **Bereich für**:`for (auto& x : container)`
- **`constexpr`**: Berechnung zur Kompilierungszeit
- **`static_assert`**: Behauptungen zur Kompilierungszeit
- **`using`**: Typ-Aliase (ersetzt`typedef`)
- **Variadische Vorlagen**:`template<typename... Args>`
- **`enum class`**: stark typisierte Aufzählungen
- **`override`/`final`**: virtuelle Funktionssteuerung
- **`std::thread`**: natives Threading
- **`std::atomic`**: Sperrfreie Programmierung
- **`std::function`/`std::bind`**: erstklassige Funktionen
### C++17 – Verfeinerung (2017)
- `std::optional<T>`, `std::variant<T...>`,`std::any`
-`if constexpr`– Verzweigung zur Kompilierungszeit
- Strukturierte Bindungen:`auto [x, y] = point;`
-`std::filesystem`
-`std::string_view`
- Parallele Algorithmen:`std::execution::par`
- Verschachtelte Namespaces:`namespace A::B::C {}`
- `[[nodiscard]]`, `[[maybe_unused]]`, `[[fallthrough]]`
### C++20 – Die moderne Sprache (2020)
- **Konzepte**:`template<std::integral T>`– eingeschränkte Vorlagen
- **Bereiche**:`views::filter`,`views::transform`– Lazy Pipelines
- **Koroutinen**: `co_await`, `co_yield`,`co_return`
- **Module**:`import`/`export`– schnellere Kompilierung
- **`std::span`**: nicht besitzende Ansicht zusammenhängender Daten
- **Dreiervergleich**:`<=>`(Raumschiffbetreiber)
- **`std::format`**: Formatierung im Python-Stil
- **`consteval`/`constinit`**: Durchsetzung zur Kompilierungszeit
- **Designierte Initialisierer**:`Point{.x = 1, .y = 2}`
- **`std::jthread`**: Thread mit Stopp-Token automatisch verbinden
### C++23 – Praktische Verbesserungen (2024)
-`std::expected<T, E>`– Von Rust inspirierte Fehlerbehandlung
-`std::print`/`std::println`– schnelle formatierte Ausgabe
-`std::flat_map`,`std::flat_set`
- Ableitung von`this`– expliziter Objektparameter
-`std::mdspan`– mehrdimensionale Spanne
-`std::generator`– Synchrongenerator
-`#include <debugging>`– Haltepunkt, Dump
## Entwicklung von Schlüsselmustern
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

## Standardprozess
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

## Auswirkungen auf das Ökosystem
```
1998: C++ dominates systems, games, finance
2005: Boost library ecosystem grows
2011: Modern C++ makes C++ safer and more expressive
2020: C++20 concepts simplify template code
2025: C++ remains #4 most used language; dominant in games, embedded, HFT, OS kernels
```
