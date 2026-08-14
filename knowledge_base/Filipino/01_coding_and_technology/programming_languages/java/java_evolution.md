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
# Java — Kasaysayan ng Bersyon at Ebolusyon
## Timeline
| Bersyon | Petsa ng Paglabas | Pangunahing Tema |
|---------|-------------|-----------|
| JDK 1.0 | Ene 1996 | Paunang release ("Oak") |
| JDK 1.1 | Peb 1997 | Mga panloob na klase, JDBC, RMI |
| J2SE 1.2 | Dis 1998 | Framework ng mga koleksyon, Swing,`strictfp`|
| J2SE 1.3 | Mayo 2000 | HotSpot JVM,`assert`|
| J2SE 1.4 | Peb 2002 | `assert`, NIO, regex,`java.net`|
| J2SE 5.0 | Set 2004 | **Major**: Mga generic, enum, anotasyon, autoboxing, varargs |
| Java SE 6 | Dis 2006 | Scripting, compiler API,`@Override`sa mga interface |
| Java SE 7 | Hul 2011 | `try-with-resources`,`switch`sa String, NIO.2 |
| Java SE 8 | Mar 2014 | **Major**: Lambdas, Streams,`Optional`,`java.time`, mga default na pamamaraan |
| Java 9 | Set 2017 | Mga Module (JPMS),`var`,`jshell`, pribadong paraan ng interface |
| Java 10 | Mar 2018 | `var`para sa mga lokal na variable |
| Java 11 | Set 2018 | **LTS**:`String`method,`HttpClient`, single-file launch |
| Java 12 | Mar 2019 | Lumipat ng mga expression (preview) |
| Java 13 | Set 2019 | Mga bloke ng teksto (preview) |
| Java 14 | Mar 2020 | `record`(preview), lumipat ng mga expression,`instanceof`pattern |
| Java 15 | Set 2020 | Mga bloke ng teksto, mga selyadong klase (preview) |
| Java 16 | Mar 2021 | `record`,`instanceof`pattern na tumutugma |
| Java 17 | Set 2021 | **LTS**: Mga selyadong klase, pagtutugma ng pattern para sa`switch`|
| Java 18 | Mar 2022 | Simpleng web server, UTF-8 default |
| Java 19 | Set 2022 | Mga virtual na thread (preview), pagtutugma ng pattern |
| Java 20 | Mar 2023 | Mga saklaw na halaga (incubator), record pattern |
| Java 21 | Set 2023 | **LTS**: **Mga virtual na thread**, pagtutugma ng pattern, mga pattern ng `switch`, mga sequence na koleksyon |
| Java 22 | Mar 2024 | Mga template ng string (preview), foreign memory API |
| Java 23 | Set 2024 | Mga primitive na uri sa mga pattern (preview) |
| Java 24 | Mar 2025 | Structured concurrency (preview) |
| Java 25 | Set 2025 | **LTS**: (inaasahan) |
## Mga Pangunahing Milestone
### Ang Klasikong Panahon (1996–2004)
- **1.0 (1996)**: "Write Once, Run Anywhere" — applets, AWT
- **1.2 (1998)**: Framework ng mga koleksyon (ang pundasyon ng mga koleksyon ng Java)
- **1.4 (2002)**: NIO, logging, regex, assertions
- **5.0 (2004)**: Ang pinakamalaking update — generics, enums, annotation, autoboxing, enhanced for-loop, varargs, `static import`
### The Enterprise Era (2006–2014)
- **6 (2006)**: Suporta sa script, compiler API
- **7 (2011)**:`try-with-resources`, diamond operator,`switch`sa String, NIO.2
- **8 (2014)**: Ang iba pang "big bang" — lambdas, stream,`Optional`,`java.time`, mga default na pamamaraan, `CompletableFuture`
### Ang Makabagong Panahon (2017–kasalukuyan)
- **9 (2017)**: Module system (JPMS),`var`,`jshell`REPL
- **11 (2018)**: Unang LTS sa ilalim ng 6-buwang release cadence; `HttpClient`; Pagbabago sa paglilisensya ng Oracle JDK
- **17 (2021)**: LTS — mga selyadong klase, pagtutugma ng pattern
- **21 (2023)**: LTS — **virtual thread** (Project Loom), pattern matching, record patterns
## Ang 6 na Buwan na Indayog ng Pagpapalabas
```
Before Java 9:  Major releases every 2-4 years
Java 9+:        New release every 6 months (March & September)
LTS releases:   Every ~2 years (8, 11, 17, 21, 25...)
Non-LTS:        Feature previews, 6-month support
```

## Generics na Paglalakbay
```
2004: Java 5.0 — type erasure generics (backward compatible)
2014: Java 8 — improved inference with lambdas
2016: Java 9 — diamond operator with anonymous classes
2018: Java 11 — `var` with generics
2023: Java 21 — record patterns with generics
```

## Functional Programming Evolution
```
2004: Anonymous inner classes (verbose)
2004: Java 5 — enums as pseudo-functional
2014: Java 8 — lambdas, streams, Optional
2017: Java 9 — Stream API additions
2019: Java 12 — switch expressions
2023: Java 21 — pattern matching in switch, record patterns
```

## Ebolusyon ng Concurrency
```
1.0:     Thread class, synchronized
1.5:     java.util.concurrent (Executors, locks, atomics)
1.7:     ForkJoinPool
1.8:     CompletableFuture, parallel streams
1.9:     Flow API (reactive streams)
1.19:    Virtual threads preview
1.21:    **Virtual threads** (Project Loom) — lightweight threads
```

## Ebolusyon ng Tampok ng Wika
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

## Ebolusyon ng JVM
```
1.0:  Interpreter
1.3:  HotSpot (JIT compilation)
1.5:  Generics via type erasure
1.7:  InvokeDynamic (for JVM languages)
1.9:  Module system, AOT compilation (experimental)
16:   ZGC (low-latency GC) production-ready
21:   Virtual threads, generational ZGC
```

## Paglago ng Ecosystem
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
