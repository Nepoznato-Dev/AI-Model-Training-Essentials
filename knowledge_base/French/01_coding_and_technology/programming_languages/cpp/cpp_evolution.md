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

# C++ — Historique et évolution des versions
## Chronologie
| Version | Année | Thème clé |
|---------|------|-----------|
| Cfront | 1983 | "C avec classes" — classes, héritage |
| C++98 | 1998 | Première norme ISO ; STL, modèles, exceptions |
| C++03 | 2003 | Corrections de défauts |
| C++11 | 2011 | **Majeur** : Sémantique de déplacement, lambdas,`auto`, pointeurs intelligents,`nullptr`|
| C++14 | 2014 | Lambdas génériques, retour `auto`,`std::make_unique`|
| C++17 | 2017 | `std::optional`,`std::variant`,`if constexpr`, liaisons structurées |
| C++20 | 2020 | **Majeur** : concepts, plages, coroutines, modules, `std::span`, comparaison à trois |
| C++23 | 2024 | `std::expected`,`std::print`,`std::flat_map`, déduire`this`|
| C++26 | ~2026 | `std::execution`, réflexion (attendue), contrats |
## Étapes majeures
### L'ère pré-standard (1983-1998)
- **1983** : Bjarne Stroustrup crée "C with Classes" aux Bell Labs
- **1985** : renommé C++ ; première édition de "Le langage de programmation C++"
- **1989** : Modèles, exceptions, espaces de noms proposés
- **1990** : STL (Standard Template Library) par Alexander Stepanov
- **1991** : Modèles standardisés ; "Le manuel de référence C++ annoté"
### C++98 — La Fondation (1998)
- Classes, héritage, fonctions virtuelles
- Modèles (fonctions, classes, spécialisation)
- STL :`vector`,`map`,`set`,`algorithm`,`iterator`
-Exceptions (`try/catch/throw`)
-`namespace`, `bool`, `const_cast`,`dynamic_cast`
- Constructeurs `explicit`, membres `mutable`
-RTTI (`typeid`, `dynamic_cast`)
### C++11 — La Renaissance (2011)
- **Déplacer la sémantique** : références rvalue `&&`,`std::move`
- **Pointeurs intelligents** :`unique_ptr`,`shared_ptr`,`weak_ptr`
- **`auto`** : inférence de type
- **`nullptr`** : remplace`NULL`
- **Lambda** :`[](int x) { return x * 2; }`
- **Plage pour** :`for (auto& x : container)`
- **`constexpr`** : calcul à la compilation
- **`static_assert`** : assertions à la compilation
- **`using`** : alias de type (en remplacement de`typedef`)
- **Modèles variadiques** :`template<typename... Args>`
- **`enum class`** : énumérations fortement typées
- **`override`/`final`** : contrôle de fonction virtuelle
- **`std::thread`** : threading natif
- **`std::atomic`** : programmation sans verrouillage
- **`std::function`/`std::bind`** : fonctions de première classe
### C++17 — Raffinement (2017)
-`std::optional<T>`, `std::variant<T...>`,`std::any`
-`if constexpr`— branchement au moment de la compilation
- Liaisons structurées :`auto [x, y] = point;`
-`std::filesystem` 
-`std::string_view` 
- Algorithmes parallèles :`std::execution::par`
- Espaces de noms imbriqués :`namespace A::B::C {}`
-`[[nodiscard]]`, `[[maybe_unused]]`, `[[fallthrough]]`
### C++20 — Le langage moderne (2020)
- **Concepts** :`template<std::integral T>`— modèles contraints
- **Plages** :`views::filter`,`views::transform`— pipelines paresseux
- **Coroutines** :`co_await`,`co_yield`,`co_return`
- **Modules** :`import`/`export`— compilation plus rapide
- **`std::span`** : vue non propriétaire des données contiguës
- **Comparaison à trois** :`<=>`(opérateur de vaisseau spatial)
- **`std::format`** : formatage de style Python
- **`consteval`/`constinit`** : application au moment de la compilation
- **Initialiseurs désignés** :`Point{.x = 1, .y = 2}`
- **`std::jthread`** : thread à jointure automatique avec jeton d'arrêt
### C++23 — Améliorations pratiques (2024)
-`std::expected<T, E>`— Gestion des erreurs inspirée de Rust
-`std::print`/`std::println`— sortie formatée rapide
-`std::flat_map`,`std::flat_set`
- Déduire`this`— paramètre d'objet explicite
-`std::mdspan`— étendue multidimensionnelle
-`std::generator`— générateur synchrone
-`#include <debugging>`— point d'arrêt, dump
## Évolution des modèles clés
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

## Processus de normalisation
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

## Impact sur l'écosystème
```
1998: C++ dominates systems, games, finance
2005: Boost library ecosystem grows
2011: Modern C++ makes C++ safer and more expressive
2020: C++20 concepts simplify template code
2025: C++ remains #4 most used language; dominant in games, embedded, HFT, OS kernels
```
