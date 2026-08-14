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

# C++ — Historia wersji i ewolucja
## Oś czasu
| Wersja | Rok | Kluczowy motyw |
|--------|------|-----------|
| Front | 1983 | „C z klasami” — klasy, dziedziczenie |
| C++98 | 1998 | Pierwsza norma ISO; STL, szablony, wyjątki |
| C++03 | 2003 | Naprawa usterek |
| C++11 | 2011 | **Główne**: Przenieś semantykę, lambdy, `auto`, inteligentne wskaźniki,`nullptr`|
| C++14 | 2014 | Ogólne lambdy, powrót `auto`,`std::make_unique`|
| C++17 | 2017 | `std::optional`,`std::variant`,`if constexpr`, oprawy strukturalne |
| C++20 | 2020 | **Główne**: Koncepcje, zakresy, współprogramy, moduły, `std::span`, porównanie trójstronne |
| C++23 | 2024 | `std::expected`,`std::print`,`std::flat_map`, dedukcja`this`|
| C++26 | ~2026 | `std::execution`, odbicie (oczekiwane), kontrakty |
## Główne kamienie milowe
### Era przedstandardowa (1983–1998)
- **1983**: Bjarne Stroustrup tworzy „C z klasami” w Bell Labs
- **1985**: Zmieniono nazwę na C++; pierwsze wydanie „Języka programowania C++”
- **1989**: Zaproponowano szablony, wyjątki, przestrzenie nazw
- **1990**: STL (standardowa biblioteka szablonów) autorstwa Aleksandra Stiepanowa
- **1991**: Ustandaryzowane szablony; „Podręcznik C++ z adnotacjami”
### C++98 — Fundacja (1998)
- Klasy, dziedziczenie, funkcje wirtualne
- Szablony (funkcje, klasy, specjalizacja)
- STL: `vector`, `map`, `set`, `algorithm`,`iterator`
- Wyjątki (`try/catch/throw`)
- `namespace`, `bool`, `const_cast`,`dynamic_cast`
- Konstruktorzy `explicit`, elementy `mutable`
-RTTI (`typeid`, `dynamic_cast`)
### C++11 — Renesans (2011)
- **Przesuń semantykę**: odniesienia do wartości `&&`,`std::move`
- **Inteligentne wskaźniki**:`unique_ptr`,`shared_ptr`,`weak_ptr`
- **`auto`**: wnioskowanie o typie
- **`nullptr`**: zastępuje`NULL`
- **Lambda**:`[](int x) { return x * 2; }`
- **Przedział dla**:`for (auto& x : container)`
- **`constexpr`**: obliczenia w czasie kompilacji
- **`static_assert`**: asercje w czasie kompilacji
- **`using`**: aliasy typów (zastępujące`typedef`)
- **Szablony wariadyczne**:`template<typename... Args>`
- **`enum class`**: silnie wpisane wyliczenia
- **`override`/`final`**: sterowanie funkcjami wirtualnymi
- **`std::thread`**: natywne wątki
- **`std::atomic`**: programowanie bez blokady
- **`std::function`/`std::bind`**: funkcje najwyższej klasy
### C++17 — Udoskonalenie (2017)
- `std::optional<T>`, `std::variant<T...>`,`std::any`
-`if constexpr`— rozgałęzianie w czasie kompilacji
- Wiązania strukturalne:`auto [x, y] = point;`
-`std::filesystem`
-`std::string_view`
- Algorytmy równoległe:`std::execution::par`
- Zagnieżdżone przestrzenie nazw:`namespace A::B::C {}`
- `[[nodiscard]]`, `[[maybe_unused]]`, `[[fallthrough]]`
### C++20 — język nowożytny (2020)
- **Koncepcje**:`template<std::integral T>`— szablony ograniczone
- **Zakresy**:`views::filter`,`views::transform`— leniwe potoki
- **Współprogramy**:`co_await`,`co_yield`,`co_return`
- **Moduły**:`import`/`export`— szybsza kompilacja
- **`std::span`**: widok sąsiadujących danych bez własności
- **Porównanie trójstronne**:`<=>`(operator statku kosmicznego)
- **`std::format`**: Formatowanie w stylu Pythona
- **`consteval`/`constinit`**: wymuszanie w czasie kompilacji
- **Wyznaczone inicjatory**:`Point{.x = 1, .y = 2}`
- **`std::jthread`**: wątek automatycznego łączenia z tokenem zatrzymania
### C++23 — praktyczne ulepszenia (2024)
-`std::expected<T, E>`— Obsługa błędów inspirowana rdzą
-`std::print`/`std::println`— szybkie formatowanie wyjściowe
- `std::flat_map`,`std::flat_set`
- Wyprowadzenie`this`— jawny parametr obiektu
-`std::mdspan`— rozpiętość wielowymiarowa
-`std::generator`— generator synchroniczny
-`#include <debugging>`— punkt przerwania, zrzut
## Ewolucja kluczowych wzorców
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

## Proces standaryzacji
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

## Wpływ na ekosystem
```
1998: C++ dominates systems, games, finance
2005: Boost library ecosystem grows
2011: Modern C++ makes C++ safer and more expressive
2020: C++20 concepts simplify template code
2025: C++ remains #4 most used language; dominant in games, embedded, HFT, OS kernels
```
