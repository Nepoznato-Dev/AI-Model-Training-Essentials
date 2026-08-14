---
# Metadata
title: "Go — Version History & Evolution"
description: "Comprehensive version history and evolution of Go from 1.0 to modern Go."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial version history"
tags: [go, golang, version-history, evolution, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "10 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---
# Go — Historique et évolution des versions
## Chronologie
| Version | Date de sortie | Thème clé |
|---------|-------------|---------------|
| 1.0 | mars 2012 | Première version stable |
| 1.1 | mai 2013 | Performance, détecteur de course |
| 1.3 | juin 2014 | Interrogation réseau, crypto/tls |
| 1.4 | décembre 2014 | Bootstrap avec Go (auto-hébergement) |
| 1.5 | août 2015 | **GC simultané**, écriture des barrières |
| 1.7 | Août 2016 |  Package `context`, sous-tests`testing`|
| 1.8 | Février 2017 | `http.Server.Shutdown`, plugins |
| 1.9 | août 2017 | Alias ​​de type, parallèles`make`|
| 1.10 | Février 2018 |  Pool de connexions`database/sql`|
| 1.11 | Août 2018 | **Modules Go**,`go mod`|
| 1.12 | Février 2019 | TLS 1.3, versionnage des modules |
| 1.13 | septembre 2019 | `errors.Is/As`, littéraux numériques`0b`,`0o`|
| 1.14 | Février 2020 | **E/S superposées sous Windows**, préemption goroutine |
| 1.15 | août 2020 |  Réinitialisation`time.Ticker`/ `Timer`, proxy de module |
| 1.16 | Février 2021 |  Package `embed`, `io/fs`, compatible module par défaut |
| 1.17 | août 2021 | Conversion tranche en tableau,`unsafe.Slice`|
| 1.18 | mars 2022 | **Génériques**, fuzzing, espaces de travail |
| 1.19 | août 2022 | Commentaires du document, révision du modèle de mémoire |
| 1.20 | février 2023 | `errors.Join`, optimisation guidée par profil |
| 1.21 | août 2023 | **`slog`**,`min/max`intégrés,`maps/slices`|
| 1.22 | février 2024 | Plage sur des nombres entiers, routage amélioré |
| 1.23 | août 2024 | Package Itérateur (`iter`), modifications de la minuterie |
| 1.24 | Février 2025 |  Package `weak`, cartes améliorées |
## Étapes majeures
### Le début (2009-2012)
- **2009** : Go annoncé par Google (Robert Griesemer, Rob Pike, Ken Thompson)
- **2012** : **Go 1.0** — "La promesse de compatibilité Go 1"
### Performances et outils (2012-2018)
- **1.1** : 30 %+ d'amélioration des performances ; détecteur de course
- **1.5** : garbage collector simultané (les pauses du GC passent de millisecondes à microsecondes)
- **1.5** : Compilateur Go amorcé — écrit en Go (plus de C)
- **1.7** : le package`context`devient standard
### Modules et écosystème (2018-2021)
- **1.11** : **Modules Go** — gestion officielle des dépendances
- **1.13** :`errors.Is/As`— le retour à la ligne des erreurs devient idiomatique
- **1.16** : package `embed` – intégrer les fichiers au moment de la compilation
### Go moderne (2022-présent)
- **1.18** : **Génériques** — paramètres de type avec contraintes
- **1.21** :`slog`— journalisation structurée dans stdlib ; `min/max`intégré
- **1.22** : Plage sur des nombres entiers (`for i := range 10`)
- **1.23** : Package itérateur — évaluation paresseuse dans stdlib
## Parcours des génériques
```
2010: "Go doesn't need generics" (early stance)
2016: Go generics proposal discussions begin
2018: Type parameters design draft published
2020: Go 2 generics proposal (draft designs)
2022: Go 1.18 — generics land! Type parameters, constraints
2023: Generic code patterns emerge (slices, maps packages)
2024: Community adapts — generic data structures, algorithms
```

## Philosophie de gestion des erreurs
```
1.0:     Explicit error returns — "errors are values"
1.13:    Error wrapping with %w — "inspect and unwrap"
1.20:    errors.Join — multiple errors
Future:  go2 proposal for try/handle (not yet adopted)
```

## Évolution de la concurrence
```
1.0:  Goroutines + channels — CSP-inspired
1.1:  Race detector
1.4:  Non-blocking syscalls (net poller)
1.5:  Concurrent GC
1.7:  context package for cancellation
1.14: Cooperative goroutine preemption (signals)
1.21: Synchronization improvements
1.23: iter package — iterator pattern
```

## Go Promesse de compatibilité
```
Go 1.0 (2012): "Go 1 will be available for a long time.
  Compatibility is important. Programs that work at Go 1
  will continue to work at every subsequent Go 1 release."

This means:
- No breaking changes to the language spec
- No breaking changes to the standard library
- Only additive changes
- Forward compatibility guaranteed
```

## Croissance de l'écosystème
```
2012: Go 1.0 — basic stdlib, no package manager
2014: dep (early dependency management experiments)
2018: Go modules — official solution
2019: Go used by Uber, Twitch, Dropbox, Cloudflare
2022: Generics — opens new library design patterns
2023: Go in Kubernetes, Docker, Terraform, Hugo
2025: Top 10 most used language; cloud-native standard
```

## Évolution des performances
```
Go 1.0:  Baseline
Go 1.1:  ~30% faster (register-based calling prep)
Go 1.5:  Concurrent GC (pause time: ms → μs)
Go 1.7:  SSA backend (15-30% faster)
Go 1.11: PGO experiments
Go 1.13: Faster map operations
Go 1.18: Generics (initial overhead, optimized in 1.19+)
Go 1.20: Profile-guided optimization
Go 1.22: Faster crypto, improved compiler
```
