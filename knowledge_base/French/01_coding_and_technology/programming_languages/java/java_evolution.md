---
# Metadata
title: "Java — Version History & Evolution"
description: "Comprehensive version history and evolution of Java from 1.0 to modern Java."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial version history"
tags: [java, version-history, evolution, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "12 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

# Java — Historique et évolution des versions
## Chronologie
| Version | Date de sortie | Thème clé |
|---------|-------------|---------------|
| JDK 1.0 | janvier 1996 | Version initiale ("Chêne") |
| JDK 1.1 | Février 1997 | Classes internes, JDBC, RMI |
| J2SE 1.2 | décembre 1998 | Cadre de collections, Swing,`strictfp`|
| J2SE 1.3 | mai 2000 | Machine virtuelle Java HotSpot,`assert`|
| J2SE 1.4 | Février 2002 | `assert`, NIO, expression régulière,`java.net`|
| J2SE 5.0 | septembre 2004 | **Majeur** : Génériques, énumérations, annotations, autoboxing, varargs |
| JavaSE6 | décembre 2006 | Scripting, API du compilateur,`@Override`sur interfaces |
| JavaSE7 | juillet 2011 | `try-with-resources`,`switch`sur chaîne, NIO.2 |
| Java SE 8 | mars 2014 | **Majeur** : Lambdas, Streams,`Optional`,`java.time`, méthodes par défaut |
| Java9 | septembre 2017 | Modules (JPMS),`var`,`jshell`, méthodes d'interface privée |
| Java10 | mars 2018 | `var`pour les variables locales |
| Java11 | septembre 2018 | **LTS** : méthodes `String`,`HttpClient`, lancement d'un seul fichier |
| Java12 | mars 2019 | Changer d'expression (aperçu) |
| Java13 | septembre 2019 | Blocs de texte (aperçu) |
| Java14 | mars 2020 | `record`(aperçu), expressions de commutation, modèle`instanceof`|
| Java15 | septembre 2020 | Blocs de texte, classes scellées (aperçu) |
| Java16 | mars 2021 | `record`, correspondance de motifs`instanceof`|
| Java17 | septembre 2021 | **LTS** : classes scellées, correspondance de modèles pour`switch`|
| Java18 | mars 2022 | Serveur Web simple, UTF-8 par défaut |
| Java19 | septembre 2022 | Threads virtuels (aperçu), correspondance de modèles |
| Java20 | mars 2023 | Valeurs ciblées (incubateur), modèles d'enregistrement |
| Java21 | septembre 2023 | **LTS** : **Fils virtuels**, correspondance de motifs, motifs `switch`, collections séquencées |
| Java22 | mars 2024 | Modèles de chaînes (aperçu), API de mémoire étrangère |
| Java23 | septembre 2024 | Types primitifs dans les modèles (aperçu) |
| Java24 | mars 2025 | Concurrence structurée (aperçu) |
| Java25 | septembre 2025 | **LTS** : (attendu) |
## Étapes majeures
### L'ère classique (1996-2004)
- **1.0 (1996)** : "Écrire une fois, exécuter n'importe où" — applets, AWT
- **1.2 (1998)** : Framework Collections (la base des collections Java)
- **1.4 (2002)** : NIO, journalisation, regex, assertions
- **5.0 (2004)** : La plus grande mise à jour — génériques, énumérations, annotations, autoboxing, boucle for améliorée, varargs, `static import`
### L'ère de l'entreprise (2006-2014)
- **6 (2006)** : Prise en charge des scripts, API du compilateur
- **7 (2011)** :`try-with-resources`, opérateur diamant,`switch`sur String, NIO.2
- **8 (2014)** : L'autre "big bang" — lambdas, streams,`Optional`,`java.time`, méthodes par défaut, `CompletableFuture`
### L'ère moderne (2017-présent)
- **9 (2017)** : Système de modules (JPMS),`var`,`jshell`REPL
- **11 (2018)** : première LTS sous une cadence de sortie de 6 mois ; `HttpClient`; Modification de la licence Oracle JDK
- **17 (2021)** : LTS — classes scellées, correspondance de modèles
- **21 (2023)** : LTS — **thèmes virtuels** (Project Loom), correspondance de modèles, enregistrement de modèles
## La cadence de sortie de 6 mois
```
Before Java 9:  Major releases every 2-4 years
Java 9+:        New release every 6 months (March & September)
LTS releases:   Every ~2 years (8, 11, 17, 21, 25...)
Non-LTS:        Feature previews, 6-month support
```

## Parcours des génériques
```
2004: Java 5.0 — type erasure generics (backward compatible)
2014: Java 8 — improved inference with lambdas
2016: Java 9 — diamond operator with anonymous classes
2018: Java 11 — `var` with generics
2023: Java 21 — record patterns with generics
```

## Évolution de la programmation fonctionnelle
```
2004: Anonymous inner classes (verbose)
2004: Java 5 — enums as pseudo-functional
2014: Java 8 — lambdas, streams, Optional
2017: Java 9 — Stream API additions
2019: Java 12 — switch expressions
2023: Java 21 — pattern matching in switch, record patterns
```

## Évolution de la concurrence
```
1.0:     Thread class, synchronized
1.5:     java.util.concurrent (Executors, locks, atomics)
1.7:     ForkJoinPool
1.8:     CompletableFuture, parallel streams
1.9:     Flow API (reactive streams)
1.19:    Virtual threads preview
1.21:    **Virtual threads** (Project Loom) — lightweight threads
```

## Évolution des fonctionnalités linguistiques
```
Java 5:   Generics, enums, annotations, autoboxing, varargs
Java 7:   try-with-resources, diamond <>, switch on String
Java 8:   Lambdas, streams, default methods, Optional
Java 9:   var (local), modules, jshell
Java 14:  record (preview), switch expressions
Java 16:  record, instanceof pattern
Java 17:  sealed classes, switch pattern matching
Java 21:  virtual threads, pattern matching, record patterns
```

## Évolution de la JVM
```
1.0:  Interpreter
1.3:  HotSpot (JIT compilation)
1.5:  Generics via type erasure
1.7:  InvokeDynamic (for JVM languages)
1.9:  Module system, AOT compilation (experimental)
16:   ZGC (low-latency GC) production-ready
21:   Virtual threads, generational ZGC
```

## Croissance de l'écosystème
```
1998: J2EE — enterprise Java begins
2001: Spring Framework
2004: Hibernate, Maven
2006: Java on Android (modified Java)
2010: Oracle acquires Sun (Java)
2014: Java 8 — Spring Boot era
2018: Java 11 — modular JDK, GraalVM
2023: Java 21 — virtual threads, Spring Boot 3
2025: Java remains #1 enterprise language
```
