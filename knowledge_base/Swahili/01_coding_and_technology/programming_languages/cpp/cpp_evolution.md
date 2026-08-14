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
# C++ - Historia ya Toleo & Mageuzi
## Rekodi ya matukio
| Toleo | Mwaka | Mandhari Muhimu |
|---------|------|-----------|
| Mbele | 1983 | "C na Madarasa" - madarasa, urithi |
| C++98 | 1998 | Kiwango cha kwanza cha ISO; STL, violezo, vighairi |
| C++03 | 2003 | Marekebisho ya kasoro |
| C++11 | 2011 | **Kubwa**: Sogeza semantiki, lambda,`auto`, viashiria mahiri,`nullptr`|
| C++14 | 2014 | Lambda za kawaida,`auto`kurudi,`std::make_unique`|
| C++17 | 2017 | `std::optional`,`std::variant`,`if constexpr`, vifungo vilivyoundwa |
| C++20 | 2020 | **Meja**: Dhana, safu, coroutines, moduli,`std::span`, njia tatu linganisha |
| C++23 | 2024 | `std::expected`,`std::print`,`std::flat_map`, toleo la`this`|
| C++26 | ~2026 | `std::execution`, tafakari (inatarajiwa), mikataba |
## Mafanikio Makuu
### Enzi ya Kabla ya Kiwango (1983–1998)
- **1983**: Bjarne Stroustrup anaunda "C na Madarasa" katika Bell Labs
- **1985**: Ilibadilishwa Jina C++; toleo la kwanza la "Lugha ya Kupanga ya C++"
- **1989**: Violezo, vighairi, nafasi za majina zilizopendekezwa
- **1990**: STL (Maktaba ya Kiolezo cha Kawaida) na Alexander Stepanov
- **1991**: Violezo vilivyosanifishwa; "Mwongozo wa Marejeleo wa C++ Uliofafanuliwa"
### C++98 — The Foundation (1998)
- Madarasa, urithi, kazi za kawaida
- Violezo (kazi, madarasa, utaalam)
- STL :`vector`,`map`,`set`,`algorithm`,`iterator`
- Isipokuwa (`try/catch/throw`)
`namespace` ,`bool`,`const_cast`,`dynamic_cast`
- Wajenzi wa `explicit`, wanachama wa `mutable`
- RTTI (`typeid`,`dynamic_cast`)
### C++11 — Renaissance (2011)
- **Sogeza semantiki**: marejeleo ya thamani ya `&&`,`std::move`
- **Viashiria mahiri**:`unique_ptr`,`shared_ptr`,`weak_ptr`
- **`auto`**: aina ya uelekezaji
- **`nullptr`**: inachukua nafasi ya`NULL`
- **Lambda**:`[](int x) { return x * 2; }`
- **Msururu wa**:`for (auto& x : container)`
- **`constexpr`**: hesabu ya wakati wa kukusanya
- **`static_assert`**: kusanya madai ya wakati
- **`using`**: lakabu za aina (ikichukua nafasi ya `typedef`)
- **Violezo mbalimbali**:`template<typename... Args>`
- **`enum class`**: enum zilizoandikwa kwa nguvu
- **`override`/`final`**: udhibiti wa utendaji kazi
- **`std::thread`**: threading asili
- **`std::atomic`**: programu bila kufuli
- **`std::function`/`std::bind`**: kazi za daraja la kwanza
### C++17 - Uboreshaji (2017)
`std::optional<T>` ,`std::variant<T...>`,`std::any`
-`if constexpr`- kukusanya matawi ya wakati
- Vifungo vilivyowekwa:`auto [x, y] = point;`
-`std::filesystem`
-`std::string_view`
- Algorithms Sambamba:`std::execution::par`
- Nafasi za majina zilizowekwa:`namespace A::B::C {}`
`[[nodiscard]]` ,`[[maybe_unused]]`, `[[fallthrough]]`
### C++20 — Lugha ya Kisasa (2020)
- **Dhana**:`template<std::integral T>`- violezo vyenye vikwazo
- **Safu**:`views::filter`,`views::transform`— mabomba ya uvivu
- **Coutines**:`co_await`,`co_yield`,`co_return`
- **Moduli**:`import`/`export`- mkusanyiko wa haraka zaidi
- **`std::span`**: mtazamo usio na umiliki wa data iliyounganishwa
- **Ulinganisho wa njia tatu**:`<=>`(opereta wa anga za juu)
- **`std::format`**: Uumbizaji wa mtindo wa Python
- **`consteval`/`constinit`**: utekelezaji wa wakati wa kukusanya
- **Vianzishaji vilivyoteuliwa**:`Point{.x = 1, .y = 2}`
- **`std::jthread`**: uzi wa kujiunga kiotomatiki na ishara ya kuacha
### C++23 - Maboresho ya Kivitendo (2024)
-`std::expected<T, E>`- Ushughulikiaji wa hitilafu ulioongozwa na kutu
-`std::print`/`std::println`— towe lililoumbizwa haraka
-`std::flat_map`,`std::flat_set`
- Kupunguza`this`- parameta ya kitu wazi
-`std::mdspan`- muda wa multidimensional
-`std::generator`- jenereta ya synchronous
-`#include <debugging>`- sehemu ya kuvunja, dampo
## Mageuzi ya Miundo Muhimu
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

## Mchakato wa Viwango
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

## Athari za Mfumo ikolojia
```
1998: C++ dominates systems, games, finance
2005: Boost library ecosystem grows
2011: Modern C++ makes C++ safer and more expressive
2020: C++20 concepts simplify template code
2025: C++ remains #4 most used language; dominant in games, embedded, HFT, OS kernels
```
