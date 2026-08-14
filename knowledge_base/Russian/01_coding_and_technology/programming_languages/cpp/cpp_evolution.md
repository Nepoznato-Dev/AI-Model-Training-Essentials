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
# C++ — история версий и эволюция
## Временная шкала
| Версия | Год | Ключевая тема |
|---------|------|-----------|
| Передняя часть | 1983 | «C с классами» — классы, наследование |
| С++98 | 1998 | Первый стандарт ISO; STL, шаблоны, исключения |
| С++03 | 2003 | Исправления дефектов |
| С++11 | 2011 | **Основное**: семантика перемещения, лямбда-выражения, `auto`, интеллектуальные указатели,`nullptr`|
| С++14 | 2014 | Общие лямбда-выражения, возврат `auto`,`std::make_unique`|
| С++17 | 2017 |  `std::optional`, `std::variant`, `if constexpr`, структурированные привязки |
| С++20 | 2020 | **Основные**: концепции, диапазоны, сопрограммы, модули, `std::span`, трехстороннее сравнение |
| С++23 | 2024 | `std::expected`,`std::print`,`std::flat_map`, вывод`this`|
| С++26 | ~2026 | `std::execution`, отражение (ожидаемое), контракты |
## Основные вехи
### Достандартная эра (1983–1998)
- **1983**: Бьерн Страуструп создает «C с классами» в Bell Labs.
- **1985**: переименован в C++; первое издание «Языка программирования C++».
- **1989**: предложены шаблоны, исключения, пространства имен.
- **1990**: STL (стандартная библиотека шаблонов) Александра Степанова.
- **1991**: стандартизированы шаблоны; «Аннотированное справочное руководство по C++»
### C++98 — Фонд (1998)
- Классы, наследование, виртуальные функции
- Шаблоны (функции, классы, специализация)
- STL: `vector`, `map`, `set`, `algorithm`,`iterator`
- Исключения (`try/catch/throw`)
- `namespace`, `bool`, `const_cast`,`dynamic_cast`
— Конструкторы `explicit`, члены `mutable`.
- RTTI (`typeid`,`dynamic_cast`)
### C++11 — Возрождение (2011)
- **Семантика перемещения**: ссылки на rvalue `&&`, `std::move`. 
- **Умные указатели**: `unique_ptr`, `shared_ptr`, `weak_ptr`. 
- **`auto`**: вывод типа
- **`nullptr`**: заменяет `NULL`. 
- **Лямбды**:`[](int x) { return x * 2; }`
- **Диапазон**:`for (auto& x : container)`
- **`constexpr`**: вычисление во время компиляции.
- **`static_assert`**: утверждения времени компиляции.
- **`using`**: псевдонимы типов (заменяющие`typedef`)
- **Шаблоны с вариациями**: `template<typename... Args>`. 
- **`enum class`**: строго типизированные перечисления.
- **`override`/`final`**: управление виртуальными функциями.
- **`std::thread`**: встроенная обработка потоков.
- **`std::atomic`**: программирование без блокировки
- **`std::function`/`std::bind`**: первоклассные функции
### C++17 — Уточнение (2017)
- `std::optional<T>`, `std::variant<T...>`,`std::any`
-`if constexpr`— ветвление во время компиляции.
- Структурированные привязки: `auto [x, y] = point;`. 
-`std::filesystem`
-`std::string_view`
- Параллельные алгоритмы:`std::execution::par`
- Вложенные пространства имен: `namespace A::B::C {}`. 
- `[[nodiscard]]`, `[[maybe_unused]]`, `[[fallthrough]]`
### C++20 — Современный язык (2020)
- **Концепции**:`template<std::integral T>`— шаблоны с ограничениями.
- **Диапазоны**:`views::filter`,`views::transform`— ленивые конвейеры.
- **Сопрограммы**: `co_await`, `co_yield`,`co_return`
- **Модули**:`import`/`export`— более быстрая компиляция.
- **`std::span`**: представление смежных данных без владения
- **Трёхстороннее сравнение**:`<=>`(оператор космического корабля)
- **`std::format`**: форматирование в стиле Python.
- **`consteval`/`constinit`**: принудительное применение во время компиляции.
- **Назначенные инициализаторы**: `Point{.x = 1, .y = 2}`. 
- **`std::jthread`**: автоматическое присоединение к потоку с маркером остановки.
### C++23 — Практические улучшения (2024 г.)
-`std::expected<T, E>`— обработка ошибок в стиле Rust.
-`std::print`/`std::println`— быстрый форматированный вывод
- `std::flat_map`,`std::flat_set`
- Вывод`this`— явный параметр объекта
-`std::mdspan`— многомерный диапазон
-`std::generator`— синхронный генератор
-`#include <debugging>`— точка останова, дамп
## Эволюция ключевых паттернов
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

## Процесс стандартизации
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

## Воздействие на экосистему
```
1998: C++ dominates systems, games, finance
2005: Boost library ecosystem grows
2011: Modern C++ makes C++ safer and more expressive
2020: C++20 concepts simplify template code
2025: C++ remains #4 most used language; dominant in games, embedded, HFT, OS kernels
```
