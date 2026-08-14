<!--
---
# Metadata
title: "Rust — Version History & Evolution"
description: "Comprehensive version history and evolution of Rust from early development to modern Rust."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial version history"
tags: [rust, version-history, evolution, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "10 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

-->
# Rust — Historique et évolution des versions
## Chronologie
| Version | Date de sortie | Thème clé |
|---------|-------------|---------------|
| 0,1 | janvier 2012 | Premier compilateur (rustc), concurrence basée sur les tâches |
| 0,5 | 2012 | Un système de types basé sur les traits prend forme |
| 0,6 | 2012 | Suppression des boîtes gérées`@`|
| 0,7 | 2013 | `@`supprimé,`~`pour les boîtes possédées |
| 0,8 | 2013 | Annotations à vie,`&mut`|
| 0,9 | janvier 2014 | Nettoyage final avant la version 1.0 |
| 0,10 | Février 2014 | Dernière version antérieure à la version 1.0 |
| 0,11 | avril 2014 | `Box<T>`remplace`~T`|
| 0,12 | mai 2014 |  La réécriture du module`io`commence |
| 1.0 | 15 mai 2015 | **Version stable** — "Rust 1.0" |
| 1.10 | Août 2016 |  Propagation d'erreur`?`(comme`try!`→`?`) |
| 1.15 | Février 2017 | Premier Rust sur stable avec la préparation`impl Trait`|
| 1.18 | juin 2017 | `pub(crate)`, compilation incrémentielle |
| 1.20 | octobre 2017 | Constantes associées |
| 1.26 | mai 2018 | `impl Trait`en position argument/retour |
| 1.28 | septembre 2018 | Répartiteurs mondiaux |
| 1.31 | décembre 2018 | **Édition Rust 2018** — modules,`dyn Trait`|
| 1.34 | avril 2019 | Registres alternatifs |
| 1.39 | novembre 2019 | `async/await`sur stable |
| 1,44 | juillet 2020 | Améliorations du diagnostic |
| 1.51 | avril 2021 | `const`génériques (MVP) |
| 1,56 | octobre 2021 | **Rust 2021 Edition** — fermetures, IntoIterator |
| 1,59 | Février 2022 | Assemblage en ligne |
| 1,62 | juin 2022 | `#[default]`pour les énumérations |
| 1,65 | décembre 2022 | `let else`|
| 1,68 | mars 2023 | `#[ffi_pure]`, optimisation guidée par profil |
| 1,70 | juin 2023 | Dépendances`crates.io`isolées |
| 1,74 | novembre 2023 | Mode hors ligne de fret |
| 1,76 | février 2024 | **Édition Rust 2024** — Blocs `gen`,`unsafe extern`|
| 1,79 | juin 2024 | `LazyCell`,`LazyLock`|
| 1,82 | octobre 2024 | `unsafe`dans les blocs`extern`requis |
| 1,85 | Février 2025 | Édition Rust 2024 stabilisée |
## Étapes majeures
### Pré-1.0 (2010-2015)
- **2010** : le projet parallèle de Graydon Hoare chez Mozilla gagne du terrain
- **2012** : Premier compilateur public ; le système de types subit une refonte majeure
- **2013** : Le modèle actionnarial se cristallise ;  Boîtes`@`supprimées
- **2014** : formalisation du processus Rust RFC ; la communauté grandit
- **2015** : **1,0** — garantie de stabilité ; "abstractions à coût nul"
### Les années de croissance (2015-2019)
- **2015** : Cargo devient le gestionnaire de paquets standard
- **2018** : **Rust 2018 Edition** — révision du système de modules,`dyn Trait`,`impl Trait`
- **2019** :`async/await`atterrit sur stable — l'écosystème asynchrone commence
### Maturité (2020-présent)
- **2021** : **Rust 2021 Edition** — lever l'ambiguïté des champs dans les fermetures,`IntoIterator`pour les tableaux
- **2024** : **Rust 2024 Edition** — Blocs `gen`, exigences `unsafe extern`
- **2025** : Rust dans le noyau Linux, Android, Windows, infrastructure AWS
## Système d'édition
```
Rust 2015:  The baseline (1.0)
Rust 2018:  Module system, async/await prep, dyn Trait
Rust 2021:  Closure changes, IntoIterator, panic macros
Rust 2024:  gen blocks, unsafe extern, tail expressions

Key principle: Editions are opt-in, never break existing code.
Old editions always compile. New editions add features.
```

## Évolution de la propriété
```
2010: GC-based, like Erlang
2011: Region-based lifetimes proposed
2012: Ownership model emerges (unique, shared, owned)
2013: Simplified to &T / &mut T / Box<T>
2014: Box<T> replaces ~T; Rc<T> for shared ownership
2015: 1.0 — ownership model finalized
2018: Non-Lexical Lifetimes (NLL) in Rust 2018
2021: IntoIterator for arrays (was blocked by edition concerns)
2024: Further NLL improvements
```

## Évolution asynchrone
```
2018: futures 0.1 — early async with manual polling
2019: async/await syntax (Rust 1.39)
2019: tokio 0.2 — async runtime
2020: async-std — std-like async API
2021: tokio 1.0 — stable async runtime
2023: async fn in traits (Rust 1.75)
2024: async closures, improved Send bounds
```

## Croissance de l'écosystème
```
2015: crates.io launches (~2,000 crates)
2018: Rust most loved language (Stack Overflow survey)
2019: 30,000 crates on crates.io
2021: Most admired language (6th consecutive year)
2023: 130,000+ crates
2025: Used in Linux kernel, Android, Windows, Chromium, AWS, Cloudflare, Discord, Dropbox
```

## RFC clés
| RFC | Année | Fonctionnalité |
|------|------|--------------|
| 25 | 2013 | Correspondance de motifs |
| 153 | 2014 |  XQZMARKER0Type XQZ |
| 217 | 2014 |  Opérateur`?`(essayer) |
| 460 | 2016 | `?`remplace`try!`|
| 1210 | 2015 | `impl Trait`|
| 1414 | 2016 | Édition Rust 2018 |
| 2394 | 2018 | `async/await`|
| 2515 | 2018 | `const`génériques |
| 3013 | 2020 | Vérification de la compilation conditionnelle |
| 3517 | 2023 |  Blocs`gen`|