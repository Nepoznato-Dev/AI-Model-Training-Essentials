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
# C++ — Histórico e evolução da versão
## Linha do tempo
| Versão | Ano | Tema principal |
|--------|------|-----------|
| Frente | 1983 | "C com Classes" — classes, herança |
| C++98 | 1998 | Primeiro padrão ISO; STL, modelos, exceções |
| C++03 | 2003 | Correções de defeitos |
| C++11 | 2011 | **Principal**: Semântica de movimentação, lambdas,`auto`, ponteiros inteligentes,`nullptr`|
| C++14 | 2014 | Lambdas genéricas, retorno `auto`,`std::make_unique`|
| C++17 | 2017 | `std::optional`,`std::variant`,`if constexpr`, ligações estruturadas |
| C++20 | 2020 | **Principal**: Conceitos, intervalos, corrotinas, módulos,`std::span`, comparação de três vias |
| C++23 | 2024 | `std::expected`,`std::print`,`std::flat_map`, deduzindo`this`|
| C++26 | ~2026 | `std::execution`, reflexão (esperada), contratos |
## Marcos importantes
### A era pré-padrão (1983–1998)
- **1983**: Bjarne Stroustrup cria "C with Classes" no Bell Labs
- **1985**: Renomeado C++; primeira edição de "A Linguagem de Programação C++"
- **1989**: Modelos, exceções, namespaces propostos
- **1990**: STL (Biblioteca de Modelos Padrão) por Alexander Stepanov
- **1991**: Modelos padronizados; "O manual de referência anotado de C++"
### C++98 — A Fundação (1998)
- Classes, herança, funções virtuais
- Templates (funções, classes, especialização)
- STL: `vector`, `map`, `set`, `algorithm`,`iterator`
- Exceções (`try/catch/throw`)
- `namespace`, `bool`, `const_cast`,`dynamic_cast`
- Construtores `explicit`, membros `mutable`
- RTTI (`typeid`, `dynamic_cast`)
### C++11 — A Renascença (2011)
- **Semântica de movimentação**: referências de valor `&&`,`std::move`
- **Ponteiros inteligentes**:`unique_ptr`,`shared_ptr`,`weak_ptr`
- **`auto`**: inferência de tipo
- **`nullptr`**: substitui`NULL`
- **Lambdas**:`[](int x) { return x * 2; }`
- **Intervalo para**:`for (auto& x : container)`
- **`constexpr`**: cálculo em tempo de compilação
- **`static_assert`**: asserções em tempo de compilação
- **`using`**: aliases de tipo (substituindo`typedef`)
- **Modelos variados**:`template<typename... Args>`
- **`enum class`**: enumerações fortemente digitadas
- **`override`/`final`**: controle de função virtual
- **`std::thread`**: threading nativo
- **`std::atomic`**: programação sem bloqueio
- **`std::function`/`std::bind`**: funções de primeira classe
### C++17 — Refinamento (2017)
- `std::optional<T>`, `std::variant<T...>`,`std::any`
-`if constexpr`— ramificação em tempo de compilação
- Ligações estruturadas:`auto [x, y] = point;`
-`std::filesystem` 
-`std::string_view` 
- Algoritmos paralelos:`std::execution::par`
- Namespaces aninhados:`namespace A::B::C {}`
- `[[nodiscard]]`, `[[maybe_unused]]`, `[[fallthrough]]`
### C++20 — A linguagem moderna (2020)
- **Conceitos**:`template<std::integral T>`— modelos restritos
- **Intervalos**:`views::filter`,`views::transform`— pipelines lentos
- **Corrotinas**:`co_await`,`co_yield`,`co_return`
- **Módulos**:`import`/`export`— compilação mais rápida
- **`std::span`**: visualização sem propriedade de dados contíguos
- **Comparação de três vias**:`<=>`(operador de nave espacial)
- **`std::format`**: formatação estilo Python
- **`consteval`/`constinit`**: aplicação em tempo de compilação
- **Inicializadores designados**:`Point{.x = 1, .y = 2}`
- **`std::jthread`**: thread de junção automática com token de parada
### C++23 — Melhorias Práticas (2024)
-`std::expected<T, E>`— Tratamento de erros inspirado na ferrugem
-`std::print`/`std::println`— saída formatada rapidamente
-`std::flat_map`,`std::flat_set`
- Deduzindo`this`— parâmetro de objeto explícito
-`std::mdspan`— extensão multidimensional
-`std::generator`— gerador síncrono
-`#include <debugging>`— ponto de interrupção, despejo
## Evolução dos principais padrões
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

## Processo de padrões
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

## Impacto no ecossistema
```
1998: C++ dominates systems, games, finance
2005: Boost library ecosystem grows
2011: Modern C++ makes C++ safer and more expressive
2020: C++20 concepts simplify template code
2025: C++ remains #4 most used language; dominant in games, embedded, HFT, OS kernels
```
