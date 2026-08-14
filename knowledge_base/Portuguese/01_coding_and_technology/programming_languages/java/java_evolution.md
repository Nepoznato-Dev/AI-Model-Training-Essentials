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
# Java – Histórico de versões e evolução
## Linha do tempo
| Versão | Data de lançamento | Tema principal |
|--------|-------------|-----------|
| JDK 1.0 | Janeiro de 1996 | Lançamento inicial ("Oak") |
| JDK 1.1 | Fevereiro de 1997 | Classes internas, JDBC, RMI |
| J2SE 1.2 | Dezembro de 1998 | Estrutura de coleções, Swing,`strictfp`|
| J2SE 1.3 | Maio de 2000 | HotSpot JVM,`assert`|
| J2SE 1.4 | Fevereiro de 2002 |  `assert`, NIO, regex,`java.net`|
| J2SE 5.0 | Setembro de 2004 | **Principal**: Genéricos, enums, anotações, autoboxing, varargs |
| Java SE 6 | Dezembro de 2006 | Scripting, API do compilador,`@Override`em interfaces |
| Java SE 7 | Julho de 2011 | `try-with-resources`,`switch`na string, NIO.2 |
| Java SE 8 | Março de 2014 | **Principal**: Lambdas, Streams,`Optional`,`java.time`, métodos padrão |
| Java 9 | Setembro de 2017 | Módulos (JPMS),`var`,`jshell`, métodos de interface privada |
| Java 10 | março de 2018 | `var`para variáveis ​​locais |
| Java 11 | Setembro de 2018 | **LTS**: métodos `String`,`HttpClient`, inicialização de arquivo único |
| Java 12 | março de 2019 | Alternar expressões (visualização) |
| Java 13 | Setembro de 2019 | Blocos de texto (visualização) |
| Java 14 | Março de 2020 | `record`(visualização), expressões de alternância, padrão`instanceof`|
| Java 15 | Setembro de 2020 | Blocos de texto, classes seladas (visualização) |
| Java 16 | Março de 2021 | `record`,`instanceof`correspondência de padrões |
| Java 17 | Setembro de 2021 | **LTS**: Classes seladas, correspondência de padrões para`switch`|
| Java 18 | Março de 2022 | Servidor web simples, padrão UTF-8 |
| Java 19 | Setembro de 2022 | Threads virtuais (visualização), correspondência de padrões |
| Java 20 | Março de 2023 | Valores com escopo definido (incubadora), padrões de registro |
| Java 21 | Setembro de 2023 | **LTS**: **Threads virtuais**, correspondência de padrões, padrões `switch`, coleções sequenciadas |
| Java 22 | Março de 2024 | Modelos de string (visualização), API de memória externa |
| Java 23 | Setembro de 2024 | Tipos primitivos em padrões (visualização) |
| Java 24 | Março de 2025 | Simultaneidade estruturada (visualização) |
| Java 25 | Setembro de 2025 | **LTS**: (esperado) |
## Marcos importantes
### A Era Clássica (1996–2004)
- **1.0 (1996)**: "Escreva uma vez, execute em qualquer lugar" - miniaplicativos, AWT
- **1.2 (1998)**: Estrutura de coleções (a base das coleções Java)
- **1.4 (2002)**: NIO, registro em log, regex, asserções
- **5.0 (2004)**: A maior atualização — genéricos, enums, anotações, autoboxing, loop for aprimorado, varargs, `static import`
### A Era Empresarial (2006–2014)
- **6 (2006)**: Suporte a scripts, API do compilador
- **7 (2011)**:`try-with-resources`, operador diamante,`switch`em String, NIO.2
- **8 (2014)**: O outro "big bang" — lambdas, streams,`Optional`,`java.time`, métodos padrão, `CompletableFuture`
### A Era Moderna (2017-presente)
- **9 (2017)**: Sistema de módulo (JPMS), `var`,`jshell`REPL
- **11 (2018)**: Primeiro LTS com cadência de lançamento de 6 meses; `HttpClient`; Alteração de licenciamento do Oracle JDK
- **17 (2021)**: LTS — classes seladas, correspondência de padrões
- **21 (2023)**: LTS — **threads virtuais** (Project Loom), correspondência de padrões, padrões de registro
## A cadência de lançamento de 6 meses
```
Before Java 9:  Major releases every 2-4 years
Java 9+:        New release every 6 months (March & September)
LTS releases:   Every ~2 years (8, 11, 17, 21, 25...)
Non-LTS:        Feature previews, 6-month support
```

## Jornada dos Genéricos
```
2004: Java 5.0 — type erasure generics (backward compatible)
2014: Java 8 — improved inference with lambdas
2016: Java 9 — diamond operator with anonymous classes
2018: Java 11 — `var` with generics
2023: Java 21 — record patterns with generics
```

## Evolução da Programação Funcional
```
2004: Anonymous inner classes (verbose)
2004: Java 5 — enums as pseudo-functional
2014: Java 8 — lambdas, streams, Optional
2017: Java 9 — Stream API additions
2019: Java 12 — switch expressions
2023: Java 21 — pattern matching in switch, record patterns
```

## Evolução da simultaneidade
```
1.0:     Thread class, synchronized
1.5:     java.util.concurrent (Executors, locks, atomics)
1.7:     ForkJoinPool
1.8:     CompletableFuture, parallel streams
1.9:     Flow API (reactive streams)
1.19:    Virtual threads preview
1.21:    **Virtual threads** (Project Loom) — lightweight threads
```

## Evolução dos recursos de linguagem
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

## Evolução da JVM
```
1.0:  Interpreter
1.3:  HotSpot (JIT compilation)
1.5:  Generics via type erasure
1.7:  InvokeDynamic (for JVM languages)
1.9:  Module system, AOT compilation (experimental)
16:   ZGC (low-latency GC) production-ready
21:   Virtual threads, generational ZGC
```

## Crescimento do Ecossistema
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
