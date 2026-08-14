---
# Metadata
title: "Swift — Version History & Evolution"
description: "Comprehensive version history and evolution of Swift from 1.0 to modern Swift."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial version history"
tags: [swift, version-history, evolution, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "10 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---
# Swift — Historique et évolution des versions
## Chronologie
| Version | Année | Thème clé |
|---------|------|-----------|
| 1.0 | 2014 | Version initiale (Chris Lattner, Apple) |
| 1.1 | 2014 | Initialiseurs défaillants,`@autoclosure`|
| 1.2 | 2015 | `as?`/`as!`, type `Set`, comparaisons de tuples |
| 2.0 | 2015 | Extensions de protocole,`defer`,`guard`,`errortype`|
| 2.1 | 2015 | `try?`, interpolation de chaîne en littéraux |
| 2.2 | 2016 | `#selector`,`defer`, retours de tuple |
| 3.0 | 2016 | **Majeur** : refonte de l'API — conventions de dénomination,`@discardableResult`|
| 4.0 | 2017 | `Codable`, réécriture `String`, littéraux multilignes |
| 5.0 | 2019 | **Majeur** : préparation `async/await`, stabilité ABI, type`Result`|
| 5.1 | 2019 | `some`(types opaques), enveloppes de propriétés,`@resultBuilder`|
| 5.2 | 2020 | Appel en tant que fonction,`KeyPath`en fonction |
| 5.3 | 2020 | `@MainActor`, fermetures de fin multiples, améliorations`enum`|
| 5.4 | 2021 | Paramètres variadiques multiples, améliorations`@resultBuilder`|
| 5.5 | 2021 | **`async/await`**, acteurs,`Sendable`|
| 5.6 | 2022 |  Mot-clé `any`,`Clock`,`Duration`|
| 5.7 | 2022 |  Raccourci `if let`, littéraux `Regex`, protocole`Clock`|
| 5.8 | 2023 | Déploiement arrière des fonctions, améliorations`Clock`|
| 5.9 | 2023 | **Macros**, packs de paramètres,`consume`/`discard`|
| 5.10 | 2024 | Vérification complète de la concurrence, sécurité stricte de la course aux données |
| 6.0 | 2024 | **Majeur** : concurrence stricte par défaut, lancements typés |
| 6.1 | 2025 | (attendu) Autres améliorations de la concurrence |
## Étapes majeures
### Swift 1.x — Naissance (2014-2015)
- **2014** : Annoncé à la WWDC ; remplace Objective-C pour le développement Apple
- **1.0** : Options, génériques, fermetures, inférence de type, protocoles
- **1.2** : motif`as?`/ `as!`, type `Set`
### Swift 2.x — Gestion des erreurs (2015-2016)
- **2.0** : Extensions de protocole (programmation orientée protocole),`guard`,`defer`,`do/try/catch`
- **2.1** :`try?`pour la gestion facultative des erreurs
### Swift 3.x — Le grand renommage de l'API (2016)
- **3.0** : refonte massive de l'API — "Grand Unified Renaming"
- Conventions de dénomination :`stringByAppendingString`→`appending`
- Suppression des boucles`for`de style C, des opérateurs`++`/ `--`
- Premiers libellés de paramètres par défaut
### Swift 4.x — Codable (2017)
- **4.0** : protocole`Codable`(encodage/décodage JSON), réécriture `String`, littéraux de chaîne multilignes
### Swift 5.x — Stabilité (2019-2024)
- **5.0** : stabilité ABI (les applications deviennent plus petites), type `Result`, chaînes brutes
- **5.1** : types opaques (`some View`), wrappers de propriétés (`@State`,`@Binding`)
- **5.5** : **`async/await`**, acteurs, protocole `Sendable`
- **5.9** : Macros (génération de code au moment de la compilation), packs de paramètres
### Swift 6.x — Sécurité de la concurrence (2024-présent)
- **6.0** : Vérification de concurrence stricte par défaut, lancements typés
## Évolution de la concurrence
```
1.0:  GCD (Grand Central Dispatch) — Objective-C pattern
2.0:  Protocol extensions for async patterns
5.5:  async/await, actors, Sendable
5.10: Complete concurrency checking
6.0:  Strict concurrency by default (data race safety)
```

## Évolution du système de types
```
1.0:  Optionals, generics, protocols
2.0:  Protocol extensions, protocol composition
4.0:  Codable, associated type constraints
5.1:  Opaque types (some), property wrappers
5.9:  Macros, parameter packs (variadic generics)
6.0:  Typed throws, strict Sendable
```

## Swift sur d'autres plateformes
```
2015: Swift open-sourced (Apache 2.0)
2015: Swift on Linux (Ubuntu)
2016: Swift on ARM (Raspberry Pi)
2017: Swift on Windows (experimental)
2019: TensorFlow Swift (later discontinued)
2020: Swift on AWS Lambda
2021: Vapor (server-side Swift framework)
2023: Swift on embedded systems (embedded Swift)
2025: Swift — cross-platform systems language
```

## Processus d'évolution rapide
```
SE-0001 (2015): First proposal
Over 400 proposals accepted by 2025
Key proposals:
  SE-0044: Import as member
  SE-0110: Distributed actors
  SE-0295: Codable improvements
  SE-0302: Sendable and @Sendable closures
  SE-0335: Introduce existential any
  SE-0346: Lightweight same-type requirements (some)
  SE-0401: Remove Actor Isolation Inference
  SE-0413: Typed throws
```

## Croissance de l'écosystème
```
2014: Swift announced — replaces Objective-C
2015: Open source; Swift Package Manager
2016: Swift 3 — API redesign
2017: Swift 4 — Codable
2019: Swift 5 — ABI stability
2021: SwiftUI matures
2023: Swift 5.9 — macros
2025: Swift 6 — data race safety; used in iOS, macOS, server, embedded
```
