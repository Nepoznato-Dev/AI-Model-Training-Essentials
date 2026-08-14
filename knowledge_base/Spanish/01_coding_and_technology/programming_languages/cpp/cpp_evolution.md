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
# C++: Historial de versiones y evolución
## Línea de tiempo
| Versión | Año | Tema clave |
|---------|------|-----------|
| Frente | 1983 | "C con clases" — clases, herencia |
| C++98 | 1998 | Primera norma ISO; STL, plantillas, excepciones |
| C++03 | 2003 | Correcciones de defectos |
| C++11 | 2011 | **Principal**: Mover semántica, lambdas, `auto`, punteros inteligentes,`nullptr`|
| C++14 | 2014 | Lambdas genéricas, retorno `auto`,`std::make_unique`|
| C++17 | 2017 |  `std::optional`, `std::variant`, `if constexpr`, fijaciones estructuradas |
| C++20 | 2020 | **Principal**: Conceptos, rangos, corrutinas, módulos, `std::span`, comparación de tres vías |
| C++23 | 2024 |  `std::expected`, `std::print`, `std::flat_map`, deduciendo`this`|
| C++26 | ~2026 |  `std::execution`, reflexión (esperada), contratos |
## Hitos importantes
### La era anterior al estándar (1983-1998)
- **1983**: Bjarne Stroustrup crea "C con clases" en Bell Labs
- **1985**: Renombrado C++; primera edición de "El lenguaje de programación C++"
- **1989**: Plantillas, excepciones, espacios de nombres propuestos
- **1990**: STL (Biblioteca de plantillas estándar) de Alexander Stepanov
- **1991**: Plantillas estandarizadas; "El manual de referencia de C++ comentado"
### C++98 — La Fundación (1998)
- Clases, herencia, funciones virtuales.
- Plantillas (funciones, clases, especialización)
- STL: `vector`, `map`, `set`, `algorithm`,`iterator`
- Excepciones (`try/catch/throw`)
- `namespace`, `bool`, `const_cast`,`dynamic_cast`
- Constructores `explicit`, miembros `mutable`
-RTTI (`typeid`, `dynamic_cast`)
### C++11 — El Renacimiento (2011)
- **Mover semántica**:`&&`referencias de valor,`std::move`
- **Punteros inteligentes**: `unique_ptr`, `shared_ptr`,`weak_ptr`
- **`auto`**: inferencia de tipos
- **`nullptr`**: reemplaza a`NULL`
- **Lambdas**:`[](int x) { return x * 2; }`
- **Rango para**:`for (auto& x : container)`
- **`constexpr`**: cálculo en tiempo de compilación
- **`static_assert`**: afirmaciones en tiempo de compilación
- **`using`**: escriba alias (reemplazando `typedef`)
- **Plantillas variadas**:`template<typename... Args>`
- **`enum class`**: enumeraciones fuertemente tipadas
- **`override` / `final`**: control de funciones virtuales
- **`std::thread`**: subprocesamiento nativo
- **`std::atomic`**: programación sin bloqueo
- **`std::function` / `std::bind`**: funciones de primera clase
### C++17 — Refinamiento (2017)
- `std::optional<T>`, `std::variant<T...>`,`std::any`
- `if constexpr`: ramificación en tiempo de compilación
- Fijaciones estructuradas:`auto [x, y] = point;`
-`std::filesystem`
-`std::string_view`
- Algoritmos paralelos:`std::execution::par`
- Espacios de nombres anidados:`namespace A::B::C {}`
- `[[nodiscard]]`, `[[maybe_unused]]`, `[[fallthrough]]`
### C++20 — El lenguaje moderno (2020)
- **Conceptos**:`template<std::integral T>`— plantillas restringidas
- **Rangos**: `views::filter`,`views::transform`— canalizaciones diferidas
- **Corrutinas**: `co_await`, `co_yield`,`co_return`
- **Módulos**:`import`/`export`— compilación más rápida
- **`std::span`**: vista no propietaria de datos contiguos
- **Comparación de tres vías**:`<=>`(operador de nave espacial)
- **`std::format`**: formato estilo Python
- **`consteval`/`constinit`**: aplicación en tiempo de compilación
- **Inicializadores designados**:`Point{.x = 1, .y = 2}`
- **`std::jthread`**: hilo de unión automática con token de parada
### C++23: mejoras prácticas (2024)
-`std::expected<T, E>`— Manejo de errores inspirado en Rust
-`std::print`/ `std::println`: salida formateada rápida
- `std::flat_map`,`std::flat_set`
- Deduciendo`this`— parámetro de objeto explícito
-`std::mdspan`— tramo multidimensional
-`std::generator`— generador síncrono
- `#include <debugging>`: punto de interrupción, volcado
## Evolución de patrones clave
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

## Proceso de estándares
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

## Impacto en el ecosistema
```
1998: C++ dominates systems, games, finance
2005: Boost library ecosystem grows
2011: Modern C++ makes C++ safer and more expressive
2020: C++20 concepts simplify template code
2025: C++ remains #4 most used language; dominant in games, embedded, HFT, OS kernels
```
