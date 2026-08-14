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
# Java — historia wersji i ewolucja
## Oś czasu
| Wersja | Data wydania | Kluczowy motyw |
|--------|------------|---------|
| JDK 1.0 | styczeń 1996 | Pierwsze wydanie („Dąb”) |
| JDK 1.1 | luty 1997 | Klasy wewnętrzne, JDBC, RMI |
| J2SE 1.2 | grudzień 1998 | Framework kolekcji, Swing,`strictfp`|
| J2SE 1.3 | maj 2000 | HotSpot JVM,`assert`|
| J2SE 1.4 | luty 2002 | `assert`, NIO, wyrażenie regularne,`java.net`|
| J2SE 5.0 | wrzesień 2004 | **Główne**: Generics, wyliczenia, adnotacje, autoboxing, varargs |
| Java SE6 | grudzień 2006 | Skrypty, API kompilatora,`@Override`na interfejsach |
| Java SE7 | lipiec 2011 | `try-with-resources`,`switch`na łańcuchu znaków, NIO.2 |
| Java SE 8 | marzec 2014 | **Główne**: Lambdy, Strumienie,`Optional`,`java.time`, metody domyślne |
| Java 9 | wrzesień 2017 | Moduły (JPMS),`var`,`jshell`, metody interfejsu prywatnego |
| Java 10 | marzec 2018 | `var`dla zmiennych lokalnych |
| Java 11 | wrzesień 2018 | **LTS**: metody `String`,`HttpClient`, uruchamianie jednoplikowe |
| Java 12 | marzec 2019 | Przełącz wyrażenia (podgląd) |
| Java 13 | wrzesień 2019 | Bloki tekstowe (podgląd) |
| Java 14 | marzec 2020 | `record`(wersja zapoznawcza), wyrażenia przełączające, wzorzec`instanceof`|
| Java 15 | wrzesień 2020 | Bloki tekstu, klasy zapieczętowane (podgląd) |
| Java 16 | marzec 2021 | `record`,`instanceof`dopasowanie wzorca |
| Java 17 | wrzesień 2021 | **LTS**: Klasy zapieczętowane, dopasowanie wzorca dla`switch`|
| Java 18 | marzec 2022 | Prosty serwer WWW, domyślny UTF-8 |
| Java 19 | wrzesień 2022 | Wątki wirtualne (podgląd), dopasowywanie wzorców |
| Java 20 | marzec 2023 | Wartości o określonym zakresie (inkubator), wzorce rekordów |
| Java 21 | wrzesień 2023 | **LTS**: **Wątki wirtualne**, dopasowywanie wzorców, wzorce `switch`, kolekcje sekwencyjne |
| Java 22 | marzec 2024 | Szablony ciągów (podgląd), API pamięci obcej |
| Java 23 | wrzesień 2024 | Typy pierwotne we wzorach (podgląd) |
| Java 24 | marzec 2025 | Współbieżność strukturalna (wersja zapoznawcza) |
| Java 25 | wrzesień 2025 | **LTS**: (oczekiwane) |
## Główne kamienie milowe
### Era klasyczna (1996–2004)
- **1.0 (1996)**: „Napisz raz, uruchom gdziekolwiek” — aplety, AWT
- **1.2 (1998)**: Framework kolekcji (podstawa kolekcji Java)
- **1.4 (2002)**: NIO, logowanie, wyrażenie regularne, asercje
- **5.0 (2004)**: Największa aktualizacja — generyczne, wyliczenia, adnotacje, autoboxing, ulepszona pętla for, varargs, `static import`
### Era przedsiębiorczości (2006–2014)
- **6 (2006)**: Obsługa skryptów, API kompilatora
- **7 (2011)**:`try-with-resources`, operator diamentowy,`switch`na sznurku, NIO.2
- **8 (2014)**: Drugi „wielki wybuch” — lambdy, strumienie,`Optional`,`java.time`, metody domyślne, `CompletableFuture`
### Era nowożytna (2017 – obecnie)
- **9 (2017)**: System modułowy (JPMS),`var`,`jshell`REPL
- **11 (2018)**: Pierwszy LTS w okresie wydawniczym krótszym niż 6 miesięcy; `HttpClient`; Zmiana licencji Oracle JDK
- **17 (2021)**: LTS — zajęcia zamknięte, dopasowywanie wzorców
- **21 (2023)**: LTS — **wirtualne wątki** (Project Loom), dopasowywanie wzorców, rejestrowanie wzorców
## 6-miesięczny cykl wydawania
```
Before Java 9:  Major releases every 2-4 years
Java 9+:        New release every 6 months (March & September)
LTS releases:   Every ~2 years (8, 11, 17, 21, 25...)
Non-LTS:        Feature previews, 6-month support
```

## Podróż po lekach generycznych
```
2004: Java 5.0 — type erasure generics (backward compatible)
2014: Java 8 — improved inference with lambdas
2016: Java 9 — diamond operator with anonymous classes
2018: Java 11 — `var` with generics
2023: Java 21 — record patterns with generics
```

## Ewolucja programowania funkcjonalnego
```
2004: Anonymous inner classes (verbose)
2004: Java 5 — enums as pseudo-functional
2014: Java 8 — lambdas, streams, Optional
2017: Java 9 — Stream API additions
2019: Java 12 — switch expressions
2023: Java 21 — pattern matching in switch, record patterns
```

## Ewolucja współbieżności
```
1.0:     Thread class, synchronized
1.5:     java.util.concurrent (Executors, locks, atomics)
1.7:     ForkJoinPool
1.8:     CompletableFuture, parallel streams
1.9:     Flow API (reactive streams)
1.19:    Virtual threads preview
1.21:    **Virtual threads** (Project Loom) — lightweight threads
```

## Ewolucja funkcji językowych
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

## Ewolucja JVM
```
1.0:  Interpreter
1.3:  HotSpot (JIT compilation)
1.5:  Generics via type erasure
1.7:  InvokeDynamic (for JVM languages)
1.9:  Module system, AOT compilation (experimental)
16:   ZGC (low-latency GC) production-ready
21:   Virtual threads, generational ZGC
```

## Rozwój ekosystemu
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
