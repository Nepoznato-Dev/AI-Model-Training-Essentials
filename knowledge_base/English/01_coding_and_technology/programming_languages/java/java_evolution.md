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
# Java — Version History & Evolution

## Timeline

| Version | Release Date | Key Theme |
|---------|-------------|-----------|
| JDK 1.0 | Jan 1996    | Initial release ("Oak") |
| JDK 1.1 | Feb 1997    | Inner classes, JDBC, RMI |
| J2SE 1.2 | Dec 1998   | Collections framework, Swing, `strictfp` |
| J2SE 1.3 | May 2000    | HotSpot JVM, `assert` |
| J2SE 1.4 | Feb 2002    | `assert`, NIO, regex, `java.net` |
| J2SE 5.0 | Sep 2004    | **Major**: Generics, enums, annotations, autoboxing, varargs |
| Java SE 6 | Dec 2006    | Scripting, compiler API, `@Override` on interfaces |
| Java SE 7 | Jul 2011    | `try-with-resources`, `switch` on String, NIO.2 |
| Java SE 8 | Mar 2014    | **Major**: Lambdas, Streams, `Optional`, `java.time`, default methods |
| Java 9   | Sep 2017     | Modules (JPMS), `var`, `jshell`, private interface methods |
| Java 10  | Mar 2018     | `var` for local variables |
| Java 11  | Sep 2018     | **LTS**: `String` methods, `HttpClient`, single-file launch |
| Java 12  | Mar 2019     | Switch expressions (preview) |
| Java 13  | Sep 2019     | Text blocks (preview) |
| Java 14  | Mar 2020     | `record` (preview), switch expressions, `instanceof` pattern |
| Java 15  | Sep 2020     | Text blocks, sealed classes (preview) |
| Java 16  | Mar 2021     | `record`, `instanceof` pattern matching |
| Java 17  | Sep 2021     | **LTS**: Sealed classes, pattern matching for `switch` |
| Java 18  | Mar 2022     | Simple web server, UTF-8 default |
| Java 19  | Sep 2022     | Virtual threads (preview), pattern matching |
| Java 20  | Mar 2023     | Scoped values (incubator), record patterns |
| Java 21  | Sep 2023     | **LTS**: **Virtual threads**, pattern matching, `switch` patterns, sequenced collections |
| Java 22  | Mar 2024     | String templates (preview), foreign memory API |
| Java 23  | Sep 2024     | Primitive types in patterns (preview) |
| Java 24  | Mar 2025     | Structured concurrency (preview) |
| Java 25  | Sep 2025     | **LTS**: (expected) |

## Major Milestones

### The Classic Era (1996–2004)
- **1.0 (1996)**: "Write Once, Run Anywhere" — applets, AWT
- **1.2 (1998)**: Collections framework (the foundation of Java collections)
- **1.4 (2002)**: NIO, logging, regex, assertions
- **5.0 (2004)**: The biggest update — generics, enums, annotations, autoboxing, enhanced for-loop, varargs, `static import`

### The Enterprise Era (2006–2014)
- **6 (2006)**: Scripting support, compiler API
- **7 (2011)**: `try-with-resources`, diamond operator, `switch` on String, NIO.2
- **8 (2014)**: The other "big bang" — lambdas, streams, `Optional`, `java.time`, default methods, `CompletableFuture`

### The Modern Era (2017–present)
- **9 (2017)**: Module system (JPMS), `var`, `jshell` REPL
- **11 (2018)**: First LTS under 6-month release cadence; `HttpClient`; Oracle JDK licensing change
- **17 (2021)**: LTS — sealed classes, pattern matching
- **21 (2023)**: LTS — **virtual threads** (Project Loom), pattern matching, record patterns

## The 6-Month Release Cadence

```
Before Java 9:  Major releases every 2-4 years
Java 9+:        New release every 6 months (March & September)
LTS releases:   Every ~2 years (8, 11, 17, 21, 25...)
Non-LTS:        Feature previews, 6-month support
```

## Generics Journey

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

## Concurrency Evolution

```
1.0:     Thread class, synchronized
1.5:     java.util.concurrent (Executors, locks, atomics)
1.7:     ForkJoinPool
1.8:     CompletableFuture, parallel streams
1.9:     Flow API (reactive streams)
1.19:    Virtual threads preview
1.21:    **Virtual threads** (Project Loom) — lightweight threads
```

## Language Feature Evolution

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

## JVM Evolution

```
1.0:  Interpreter
1.3:  HotSpot (JIT compilation)
1.5:  Generics via type erasure
1.7:  InvokeDynamic (for JVM languages)
1.9:  Module system, AOT compilation (experimental)
16:   ZGC (low-latency GC) production-ready
21:   Virtual threads, generational ZGC
```

## Ecosystem Growth

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
