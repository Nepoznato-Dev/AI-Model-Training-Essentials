---
# Metadata
title: "C++ — Version History & Evolution"
description: "Comprehensive version history and evolution of C++ from C with Classes to C++26."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
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

# C++ — Kasaysayan ng Bersyon at Ebolusyon
## Timeline
| Bersyon | Taon | Pangunahing Tema |
|---------|------|-----------|
| Cfront | 1983 | "C with Classes" — mga klase, mana |
| C++98 | 1998 | Unang pamantayan ng ISO; STL, mga template, mga exception |
| C++03 | 2003 | Pag-aayos ng depekto |
| C++11 | 2011 | **Major**: Ilipat ang mga semantika, lambdas,`auto`, matalinong mga pointer,`nullptr`|
| C++14 | 2014 | Mga generic na lambdas,`auto`return,`std::make_unique`|
| C++17 | 2017 | `std::optional`,`std::variant`,`if constexpr`, structured bindings |
| C++20 | 2020 | **Major**: Mga konsepto, hanay, coroutine, module,`std::span`, three-way na paghahambing |
| C++23 | 2024 | `std::expected`,`std::print`,`std::flat_map`, deducing`this`|
| C++26 | ~2026 | `std::execution`, pagmuni-muni (inaasahan), mga kontrata |
## Mga Pangunahing Milestone
### Ang Pre-Standard Era (1983–1998)
- **1983**: Lumilikha si Bjarne Stroustrup ng "C with Classes" sa Bell Labs
- **1985**: Pinalitan ang pangalan ng C++; unang edisyon ng "The C++ Programming Language"
- **1989**: Mga template, exception, namespaces na iminungkahi
- **1990**: STL (Standard Template Library) ni Alexander Stepanov
- **1991**: Na-standardize ang mga template; "Ang Annotated C++ Reference Manual"
### C++98 — The Foundation (1998)
- Mga klase, mana, virtual function
- Mga template (mga function, klase, espesyalisasyon)
- STL:`vector`,`map`,`set`,`algorithm`,`iterator`
- Mga Pagbubukod (`try/catch/throw`)
-`namespace`,`bool`,`const_cast`,`dynamic_cast`
- Mga konstruktor ng `explicit`, mga miyembro ng `mutable`
- RTTI (`typeid`,`dynamic_cast`)
### C++11 — The Renaissance (2011)
- **Ilipat ang mga semantika**:`&&`rvalue reference,`std::move`
- **Mga matalinong payo**:`unique_ptr`,`shared_ptr`,`weak_ptr`
- **`auto`**: uri ng hinuha
- **`nullptr`**: pinapalitan ang`NULL`
- **Lambdas**:`[](int x) { return x * 2; }`
- **Range-for**:`for (auto& x : container)`
- **`constexpr`**: computation-time na computation
- **`static_assert`**: compile-time assertions
- **`using`**: uri ng mga alias (pinapalitan ang`typedef`)
- **Variadic na template**:`template<typename... Args>`
- **`enum class`**: malakas na pag-type ng mga enum
- **`override`/`final`**: virtual function control
- **`std::thread`**: katutubong threading
- **`std::atomic`**: lock-free programming
- **`std::function`/`std::bind`**: mga first-class na function
### C++17 — Pagpipino (2017)
-`std::optional<T>`,`std::variant<T...>`,`std::any`
-`if constexpr`— compile-time branching
- Mga istrukturang binding:`auto [x, y] = point;`
-`std::filesystem`
-`std::string_view`
- Parallel algorithm:`std::execution::par`
- Mga nested namespace:`namespace A::B::C {}`
-`[[nodiscard]]`,`[[maybe_unused]]`, `[[fallthrough]]`
### C++20 — Ang Makabagong Wika (2020)
- **Mga Konsepto**:`template<std::integral T>`— mga napiling template
- **Mga Saklaw**:`views::filter`,`views::transform`— tamad na mga pipeline
- **Mga Coroutine**:`co_await`,`co_yield`,`co_return`
- **Mga Module**:`import`/`export`— mas mabilis na compilation
- **`std::span`**: hindi pagmamay-ari ng view ng magkadikit na data
- **Three-way na paghahambing**:`<=>`(spaceship operator)
- **`std::format`**: Python-style na pag-format
- **`consteval`/`constinit`**: compile-time na pagpapatupad
- **Mga itinalagang initializer**:`Point{.x = 1, .y = 2}`
- **`std::jthread`**: auto-joining thread na may stop token
### C++23 — Mga Praktikal na Pagpapabuti (2024)
-`std::expected<T, E>`— Pangangasiwa ng error na dulot ng kalawang
-`std::print`/`std::println`— mabilis na na-format na output
-`std::flat_map`,`std::flat_set`
- Deducing`this`— tahasang object parameter
-`std::mdspan`— multidimensional span
-`std::generator`— kasabay na generator
-`#include <debugging>`— breakpoint, dump
## Ebolusyon ng Mga Pangunahing Pattern
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

## Proseso ng Pamantayan
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

## Epekto sa Ecosystem
```
1998: C++ dominates systems, games, finance
2005: Boost library ecosystem grows
2011: Modern C++ makes C++ safer and more expressive
2020: C++20 concepts simplify template code
2025: C++ remains #4 most used language; dominant in games, embedded, HFT, OS kernels
```
