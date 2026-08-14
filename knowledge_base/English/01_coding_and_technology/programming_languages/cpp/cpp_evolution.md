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
# C++ — Version History & Evolution

## Timeline

| Version | Year | Key Theme |
|---------|------|-----------|
| Cfront  | 1983  | "C with Classes" — classes, inheritance |
| C++98   | 1998  | First ISO standard; STL, templates, exceptions |
| C++03   | 2003  | Defect fixes |
| C++11   | 2011  | **Major**: Move semantics, lambdas, `auto`, smart pointers, `nullptr` |
| C++14   | 2014  | Generic lambdas, `auto` return, `std::make_unique` |
| C++17   | 2017  | `std::optional`, `std::variant`, `if constexpr`, structured bindings |
| C++20   | 2020  | **Major**: Concepts, ranges, coroutines, modules, `std::span`, three-way compare |
| C++23   | 2024  | `std::expected`, `std::print`, `std::flat_map`, deducing `this` |
| C++26   | ~2026 | `std::execution`, reflection (expected), contracts |

## Major Milestones

### The Pre-Standard Era (1983–1998)
- **1983**: Bjarne Stroustrup creates "C with Classes" at Bell Labs
- **1985**: Renamed C++; first edition of "The C++ Programming Language"
- **1989**: Templates, exceptions, namespaces proposed
- **1990**: STL (Standard Template Library) by Alexander Stepanov
- **1991**: Templates standardized; "The Annotated C++ Reference Manual"

### C++98 — The Foundation (1998)
- Classes, inheritance, virtual functions
- Templates (functions, classes, specialization)
- STL: `vector`, `map`, `set`, `algorithm`, `iterator`
- Exceptions (`try/catch/throw`)
- `namespace`, `bool`, `const_cast`, `dynamic_cast`
- `explicit` constructors, `mutable` members
- RTTI (`typeid`, `dynamic_cast`)

### C++11 — The Renaissance (2011)
- **Move semantics**: `&&` rvalue references, `std::move`
- **Smart pointers**: `unique_ptr`, `shared_ptr`, `weak_ptr`
- **`auto`**: type inference
- **`nullptr`**: replaces `NULL`
- **Lambdas**: `[](int x) { return x * 2; }`
- **Range-for**: `for (auto& x : container)`
- **`constexpr`**: compile-time computation
- **`static_assert`**: compile-time assertions
- **`using`**: type aliases (replacing `typedef`)
- **Variadic templates**: `template<typename... Args>`
- **`enum class`**: strongly typed enums
- **`override`/`final`**: virtual function control
- **`std::thread`**: native threading
- **`std::atomic`**: lock-free programming
- **`std::function`/`std::bind`**: first-class functions

### C++17 — Refinement (2017)
- `std::optional<T>`, `std::variant<T...>`, `std::any`
- `if constexpr` — compile-time branching
- Structured bindings: `auto [x, y] = point;`
- `std::filesystem`
- `std::string_view`
- Parallel algorithms: `std::execution::par`
- Nested namespaces: `namespace A::B::C {}`
- `[[nodiscard]]`, `[[maybe_unused]]`, `[[fallthrough]]`

### C++20 — The Modern Language (2020)
- **Concepts**: `template<std::integral T>` — constrained templates
- **Ranges**: `views::filter`, `views::transform` — lazy pipelines
- **Coroutines**: `co_await`, `co_yield`, `co_return`
- **Modules**: `import`/`export` — faster compilation
- **`std::span`**: non-owning view of contiguous data
- **Three-way comparison**: `<=>` (spaceship operator)
- **`std::format`**: Python-style formatting
- **`consteval`/`constinit`**: compile-time enforcement
- **Designated initializers**: `Point{.x = 1, .y = 2}`
- **`std::jthread`**: auto-joining thread with stop token

### C++23 — Practical Improvements (2024)
- `std::expected<T, E>` — Rust-inspired error handling
- `std::print` / `std::println` — fast formatted output
- `std::flat_map`, `std::flat_set`
- Deducing `this` — explicit object parameter
- `std::mdspan` — multidimensional span
- `std::generator` — synchronous generator
- `#include <debugging>` — breakpoint, dump

## Evolution of Key Patterns

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

## Standards Process

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

## Ecosystem Impact

```
1998: C++ dominates systems, games, finance
2005: Boost library ecosystem grows
2011: Modern C++ makes C++ safer and more expressive
2020: C++20 concepts simplify template code
2025: C++ remains #4 most used language; dominant in games, embedded, HFT, OS kernels
```
