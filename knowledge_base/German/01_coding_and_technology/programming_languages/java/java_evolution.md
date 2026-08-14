<!--
---
# Metadata
title: "Java — Version History & Evolution"
description: "Comprehensive version history and evolution of Java from 1.0 to modern Java."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
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

-->
# Java – Versionsverlauf und Entwicklung
## Zeitleiste
| Version | Erscheinungsdatum | Schlüsselthema |
|---------|-------------|-----------|
| JDK 1.0 | Januar 1996 | Erstveröffentlichung („Eiche“) |
| JDK 1.1 | Februar 1997 | Innere Klassen, JDBC, RMI |
| J2SE 1.2 | Dez. 1998 | Sammlungsrahmen, Swing,`strictfp`|
| J2SE 1.3 | Mai 2000 | HotSpot-JVM,`assert`|
| J2SE 1.4 | Februar 2002 | `assert`, NIO, Regex,`java.net`|
| J2SE 5.0 | September 2004 | **Hauptsächlich**: Generics, Enumerationen, Anmerkungen, Autoboxing, Varargs |
| Java SE 6 | Dez. 2006 | Scripting, Compiler-API,`@Override`auf Schnittstellen |
| Java SE 7 | Juli 2011 | `try-with-resources`,`switch`auf String, NIO.2 |
| Java SE 8 | März 2014 | **Major**: Lambdas, Streams, `Optional`, `java.time`, Standardmethoden |
| Java 9 | September 2017 | Module (JPMS), `var`, `jshell`, private Schnittstellenmethoden |
| Java 10 | März 2018 | `var`für lokale Variablen |
| Java 11 | September 2018 | **LTS**: `String`-Methoden, `HttpClient`, Einzeldateistart |
| Java 12 | März 2019 | Ausdrücke wechseln (Vorschau) |
| Java 13 | September 2019 | Textblöcke (Vorschau) |
| Java 14 | März 2020 | `record`(Vorschau), Ausdrücke wechseln, `instanceof`-Muster |
| Java 15 | September 2020 | Textblöcke, versiegelte Klassen (Vorschau) |
| Java 16 | März 2021 | `record`,`instanceof`Mustervergleich |
| Java 17 | September 2021 | **LTS**: Versiegelte Klassen, Mustervergleich für`switch`|
| Java 18 | März 2022 | Einfacher Webserver, UTF-8-Standard |
| Java 19 | September 2022 | Virtuelle Threads (Vorschau), Mustervergleich |
| Java 20 | März 2023 | Bereichswerte (Inkubator), Aufzeichnungsmuster |
| Java 21 | September 2023 | **LTS**: **Virtuelle Threads**, Mustervergleich,`switch`Muster, sequenzierte Sammlungen |
| Java 22 | März 2024 | String-Vorlagen (Vorschau), Fremdspeicher-API |
| Java 23 | September 2024 | Primitive Typen in Mustern (Vorschau) |
| Java 24 | März 2025 | Strukturierte Parallelität (Vorschau) |
| Java 25 | September 2025 | **LTS**: (erwartet) |
## Wichtige Meilensteine
### Die klassische Ära (1996–2004)
- **1.0 (1996)**: „Einmal schreiben, überall ausführen“ – Applets, AWT
- **1.2 (1998)**: Collections-Framework (die Grundlage von Java-Sammlungen)
- **1.4 (2002)**: NIO, Protokollierung, Regex, Behauptungen
- **5.0 (2004)**: Das größte Update – Generika, Aufzählungen, Anmerkungen, Autoboxing, erweiterte For-Schleife, Varargs, `static import`
### Die Unternehmensära (2006–2014)
- **6 (2006)**: Skriptunterstützung, Compiler-API
- **7 (2011)**: `try-with-resources`, Diamantoperator,`switch`auf String, NIO.2
- **8 (2014)**: Der andere „Urknall“ – Lambdas, Streams, `Optional`, `java.time`, Standardmethoden, `CompletableFuture`
### Die Moderne (2017–heute)
- **9 (2017)**: Modulsystem (JPMS), `var`,`jshell`REPL
- **11 (2018)**: Erstes LTS im Veröffentlichungsrhythmus von 6 Monaten; `HttpClient`; Änderung der Oracle JDK-Lizenzierung
- **17 (2021)**: LTS – versiegelte Klassen, Mustervergleich
- **21 (2023)**: LTS – **virtuelle Threads** (Project Loom), Mustervergleich, Muster aufzeichnen
## Der 6-monatige Veröffentlichungsrhythmus
```
Before Java 9:  Major releases every 2-4 years
Java 9+:        New release every 6 months (March & September)
LTS releases:   Every ~2 years (8, 11, 17, 21, 25...)
Non-LTS:        Feature previews, 6-month support
```

## Generika-Reise
```
2004: Java 5.0 — type erasure generics (backward compatible)
2014: Java 8 — improved inference with lambdas
2016: Java 9 — diamond operator with anonymous classes
2018: Java 11 — `var` with generics
2023: Java 21 — record patterns with generics
```

## Entwicklung der funktionalen Programmierung
```
2004: Anonymous inner classes (verbose)
2004: Java 5 — enums as pseudo-functional
2014: Java 8 — lambdas, streams, Optional
2017: Java 9 — Stream API additions
2019: Java 12 — switch expressions
2023: Java 21 — pattern matching in switch, record patterns
```

## Parallelitätsentwicklung
```
1.0:     Thread class, synchronized
1.5:     java.util.concurrent (Executors, locks, atomics)
1.7:     ForkJoinPool
1.8:     CompletableFuture, parallel streams
1.9:     Flow API (reactive streams)
1.19:    Virtual threads preview
1.21:    **Virtual threads** (Project Loom) — lightweight threads
```

## Entwicklung der Sprachmerkmale
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

## JVM-Entwicklung
```
1.0:  Interpreter
1.3:  HotSpot (JIT compilation)
1.5:  Generics via type erasure
1.7:  InvokeDynamic (for JVM languages)
1.9:  Module system, AOT compilation (experimental)
16:   ZGC (low-latency GC) production-ready
21:   Virtual threads, generational ZGC
```

## Ökosystemwachstum
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
