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
# Java: cronologia ed evoluzione delle versioni
## Cronologia
| Versione | Data di rilascio | Tema chiave |
|---------|-------------|-----------|
| JDK 1.0 | Gennaio 1996 | Versione iniziale ("Oak") |
| JDK 1.1 | Febbraio 1997 | Classi interne, JDBC, RMI |
| J2SE1.2 | dicembre 1998 | Quadro collezioni, Swing,`strictfp`|
| J2SE1.3 | Maggio 2000 | JVM HotSpot,`assert`|
| J2SE1.4 | Febbraio 2002 | `assert`, NIO, espressione regolare,`java.net`|
| J2SE5.0 | settembre 2004 | **Maggiore**: generici, enumerazioni, annotazioni, autoboxing, varargs |
| Java SE6 | dicembre 2006 | Scripting, API del compilatore,`@Override`sulle interfacce |
| JavaSE7 | Luglio 2011 | `try-with-resources`,`switch`su stringa, NIO.2 |
| JavaSE8 | marzo 2014 | **Maggiore**: Lambda, Streams,`Optional`,`java.time`, metodi predefiniti |
| Giava9 | settembre 2017 | Moduli (JPMS),`var`,`jshell`, metodi di interfaccia privata |
| Giava10 | marzo 2018 | `var`per variabili locali |
| Giava11 | settembre 2018 | **LTS**: metodi `String`,`HttpClient`, lancio di file singoli |
| Giava12 | marzo 2019 | Cambia espressioni (anteprima) |
| Giava13 | settembre 2019 | Blocchi di testo (anteprima) |
| Giava14 | marzo 2020 | `record`(anteprima), cambia espressione, modello`instanceof`|
| Giava15 | settembre 2020 | Blocchi di testo, classi sigillate (anteprima) |
| Giava16 | Mar 2021 | `record`,`instanceof`corrispondenza del modello |
| Giava17 | Set 2021 | **LTS**: classi sigillate, corrispondenza di modelli per`switch`|
| Giava18 | marzo 2022 | Server Web semplice, impostazione predefinita UTF-8 |
| Giava19 | Set 2022 | Discussioni virtuali (anteprima), corrispondenza dei modelli |
| Giava20 | marzo 2023 | Valori con ambito (incubatrice), modelli di record |
| Giava21 | settembre 2023 | **LTS**: **Thread virtuali**, corrispondenza di modelli, modelli `switch`, raccolte in sequenza |
| Giava22 | marzo 2024 | Modelli di stringhe (anteprima), API di memoria esterna |
| Giava23 | settembre 2024 | Tipi primitivi nei modelli (anteprima) |
| Giava24 | marzo 2025 | Concorrenza strutturata (anteprima) |
| Giava25 | settembre 2025 | **LTS**: (previsto) |
## Traguardi importanti
### L'era classica (1996-2004)
- **1.0 (1996)**: "Write Once, Run Anywhere" — applet, AWT
- **1.2 (1998)**: framework delle raccolte (la base delle raccolte Java)
- **1.4 (2002)**: NIO, registrazione, espressioni regolari, asserzioni
- **5.0 (2004)**: l'aggiornamento più importante: generici, enumerazioni, annotazioni, autoboxing, loop for potenziato, varargs, `static import`
### L'era aziendale (2006–2014)
- **6 (2006)**: supporto per script, API del compilatore
- **7 (2011)**:`try-with-resources`, operatore diamante,`switch`su corda, NIO.2
- **8 (2014)**: L'altro "big bang": lambda, flussi, `Optional`, `java.time`, metodi predefiniti, `CompletableFuture`
### L'era moderna (2017-oggi)
- **9 (2017)**: Sistema di moduli (JPMS), `var`,`jshell`REPL
- **11 (2018)**: primo LTS con cadenza di rilascio inferiore a 6 mesi; `HttpClient`; Modifica della licenza Oracle JDK
- **17 (2021)**: LTS: classi sigillate, abbinamento di modelli
- **21 (2023)**: LTS — **thread virtuali** (Project Loom), corrispondenza di modelli, record di modelli
## La cadenza di rilascio di 6 mesi
```
Before Java 9:  Major releases every 2-4 years
Java 9+:        New release every 6 months (March & September)
LTS releases:   Every ~2 years (8, 11, 17, 21, 25...)
Non-LTS:        Feature previews, 6-month support
```

## Viaggio sui generici
```
2004: Java 5.0 — type erasure generics (backward compatible)
2014: Java 8 — improved inference with lambdas
2016: Java 9 — diamond operator with anonymous classes
2018: Java 11 — `var` with generics
2023: Java 21 — record patterns with generics
```

## Evoluzione della programmazione funzionale
```
2004: Anonymous inner classes (verbose)
2004: Java 5 — enums as pseudo-functional
2014: Java 8 — lambdas, streams, Optional
2017: Java 9 — Stream API additions
2019: Java 12 — switch expressions
2023: Java 21 — pattern matching in switch, record patterns
```

## Evoluzione della concorrenza
```
1.0:     Thread class, synchronized
1.5:     java.util.concurrent (Executors, locks, atomics)
1.7:     ForkJoinPool
1.8:     CompletableFuture, parallel streams
1.9:     Flow API (reactive streams)
1.19:    Virtual threads preview
1.21:    **Virtual threads** (Project Loom) — lightweight threads
```

## Evoluzione delle funzionalità del linguaggio
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

## Evoluzione della JVM
```
1.0:  Interpreter
1.3:  HotSpot (JIT compilation)
1.5:  Generics via type erasure
1.7:  InvokeDynamic (for JVM languages)
1.9:  Module system, AOT compilation (experimental)
16:   ZGC (low-latency GC) production-ready
21:   Virtual threads, generational ZGC
```

## Crescita dell'ecosistema
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
