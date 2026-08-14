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
# Java - Historia ya Toleo na Mageuzi
## Rekodi ya matukio
| Toleo | Tarehe ya Kutolewa | Mandhari Muhimu |
|---------|-------------|-----------|
| JDK 1.0 | Januari 1996 | Toleo la awali ("Oak") |
| JDK 1.1 | Februari 1997 | Madarasa ya ndani, JDBC, RMI |
| J2SE 1.2 | Desemba 1998 | Mfumo wa makusanyo, Swing,`strictfp`|
| J2SE 1.3 | Mei 2000 | HotSpot JVM,`assert`|
| J2SE 1.4 | Februari 2002 | `assert`, NIO, regex,`java.net`|
| J2SE 5.0 | Septemba 2004 | **Kubwa**: Jenerali, enum, maelezo, boxing otomatiki, varargs |
| Java SE 6 | Desemba 2006 | Maandishi, API ya mkusanyaji,`@Override`kwenye violesura |
| Java SE 7 | Julai 2011 | `try-with-resources`,`switch`kwenye Kamba, NIO.2 |
| Java SE 8 | Machi 2014 | **Meja**: Lambdas, Mipasho,`Optional`,`java.time`, mbinu chaguo-msingi |
| Java 9 | Septemba 2017 | Moduli (JPMS),`var`,`jshell`, mbinu za kiolesura cha faragha |
| Java 10 | Machi 2018 | `var`kwa vigeu vya ndani |
| Java 11 | Septemba 2018 | **LTS**: Mbinu za `String`,`HttpClient`, uzinduzi wa faili moja |
| Java 12 | Machi 2019 | Badili misemo (hakiki) |
| Java 13 | Septemba 2019 | Vizuizi vya maandishi (hakiki) |
| Java 14 | Machi 2020 | `record`(hakiki), badilisha misemo, muundo wa`instanceof`|
| Java 15 | Septemba 2020 | Vitalu vya maandishi, madarasa yaliyofungwa (hakiki) |
| Java 16 | Machi 2021 | `record`,`instanceof`muundo unaolingana |
| Java 17 | Septemba 2021 | **LTS**: Madarasa yaliyofungwa, muundo unaolingana wa`switch`|
| Java 18 | Machi 2022 | Seva rahisi ya wavuti, chaguomsingi ya UTF-8 |
| Java 19 | Septemba 2022 | Nyuzi pepe (hakiki), muundo unaolingana |
| Java 20 | Machi 2023 | Thamani zilizopimwa (incubator), rekodi ruwaza |
| Java 21 | Septemba 2023 | **LTS**: **Nyezi pepe**, ulinganishaji wa mchoro, ruwaza za `switch`, mikusanyiko iliyofuatana |
| Java 22 | Machi 2024 | Violezo vya kamba (hakiki), API ya kumbukumbu ya kigeni |
| Java 23 | Septemba 2024 | Aina za awali katika ruwaza (hakiki) |
| Java 24 | Machi 2025 | Concurrency Muundo (hakikisho) |
| Java 25 | Septemba 2025 | **LTS**: (inatarajiwa) |
## Mafanikio Makuu
### Enzi ya Kawaida (1996–2004)
- **1.0 (1996)**: "Andika Mara Moja, Kimbia Popote" — applets, AWT
- **1.2 (1998)**: Mfumo wa makusanyo (msingi wa makusanyo ya Java)
- **1.4 (2002)**: NIO, ukataji miti, regex, madai
- **5.0 (2004)**: Sasisho kubwa zaidi - jeneriki, enum, maelezo, boxing otomatiki, kuboreshwa kwa kitanzi, varargs, `static import`
### Enzi ya Biashara (2006–2014)
- **6 (2006)**: Usaidizi wa uandishi, API ya mkusanyaji
- **7 (2011)**:`try-with-resources`, mwendeshaji wa almasi,`switch`kwenye String, NIO.2
- **8 (2014)**: Nyingine "big bang" — lambdas, mitiririko,`Optional`,`java.time`, mbinu chaguo-msingi, `CompletableFuture`
### Enzi ya Kisasa (2017–sasa)
- **9 (2017)**: Mfumo wa moduli (JPMS),`var`,`jshell`REPL
- **11 (2018)**: LTS ya kwanza chini ya mwako wa kutolewa wa miezi 6; `HttpClient`; Mabadiliko ya leseni ya Oracle JDK
- **17 (2021)**: LTS - madarasa yaliyofungwa, kulinganisha muundo
- **21 (2023)**: LTS — **nyuzi za mtandaoni** (Mfumo wa Mradi), kulinganisha muundo, rekodi za mifumo
## Miezi 6 ya Kutolewa
```
Before Java 9:  Major releases every 2-4 years
Java 9+:        New release every 6 months (March & September)
LTS releases:   Every ~2 years (8, 11, 17, 21, 25...)
Non-LTS:        Feature previews, 6-month support
```

## Safari ya Jenerali
```
2004: Java 5.0 — type erasure generics (backward compatible)
2014: Java 8 — improved inference with lambdas
2016: Java 9 — diamond operator with anonymous classes
2018: Java 11 — `var` with generics
2023: Java 21 — record patterns with generics
```

## Mageuzi ya Kuandaa Programu
```
2004: Anonymous inner classes (verbose)
2004: Java 5 — enums as pseudo-functional
2014: Java 8 — lambdas, streams, Optional
2017: Java 9 — Stream API additions
2019: Java 12 — switch expressions
2023: Java 21 — pattern matching in switch, record patterns
```

## Mageuzi ya Sarafu
```
1.0:     Thread class, synchronized
1.5:     java.util.concurrent (Executors, locks, atomics)
1.7:     ForkJoinPool
1.8:     CompletableFuture, parallel streams
1.9:     Flow API (reactive streams)
1.19:    Virtual threads preview
1.21:    **Virtual threads** (Project Loom) — lightweight threads
```

## Mageuzi ya Kipengele cha Lugha
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

## Mageuzi ya JVM
```
1.0:  Interpreter
1.3:  HotSpot (JIT compilation)
1.5:  Generics via type erasure
1.7:  InvokeDynamic (for JVM languages)
1.9:  Module system, AOT compilation (experimental)
16:   ZGC (low-latency GC) production-ready
21:   Virtual threads, generational ZGC
```

## Ukuaji wa Mfumo ikolojia
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
