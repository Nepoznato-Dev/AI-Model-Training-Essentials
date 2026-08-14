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
# Java: historial de versiones y evolución
## Línea de tiempo
| Versión | Fecha de lanzamiento | Tema clave |
|---------|-------------|-----------|
| JDK 1.0 | Enero de 1996 | Lanzamiento inicial ("Roble") |
| JDK 1.1 | febrero de 1997 | Clases internas, JDBC, RMI |
| J2SE 1.2 | diciembre de 1998 | Marco de colecciones, Swing,`strictfp`|
| J2SE 1.3 | mayo de 2000 | JVM de punto de acceso,`assert`|
| J2SE 1.4 | febrero de 2002 |  `assert`, NIO, expresión regular,`java.net`|
| J2SE 5.0 | Septiembre de 2004 | **Principal**: Genéricos, enumeraciones, anotaciones, autoboxing, varargs |
| JavaSE6 | diciembre de 2006 | Scripting, API del compilador,`@Override`en interfaces |
| Java SE 7 | julio de 2011 |  `try-with-resources`,`switch`en cadena, NIO.2 |
| Java SE 8 | marzo de 2014 | **Principal**: Lambdas, Streams, `Optional`, `java.time`, métodos predeterminados |
| Java 9 | Septiembre de 2017 | Módulos (JPMS), `var`, `jshell`, métodos de interfaz privada |
| Java 10 | marzo de 2018 | `var`para variables locales |
| Java 11 | Septiembre de 2018 | **LTS**: métodos `String`, `HttpClient`, inicio de archivo único |
| Java 12 | marzo de 2019 | Cambiar expresiones (vista previa) |
| Java 13 | Septiembre de 2019 | Bloques de texto (vista previa) |
| Java 14 | marzo de 2020 | `record`(vista previa), cambiar expresiones, patrón`instanceof`|
| Java 15 | septiembre de 2020 | Bloques de texto, clases selladas (vista previa) |
| Java 16 | marzo de 2021 |  `record`,`instanceof`coincidencia de patrones |
| Java 17 | septiembre de 2021 | **LTS**: Clases selladas, coincidencia de patrones para`switch`|
| Java 18 | marzo de 2022 | Servidor web simple, UTF-8 predeterminado |
| Java 19 | septiembre de 2022 | Hilos virtuales (vista previa), coincidencia de patrones |
| Java 20 | marzo de 2023 | Valores de alcance (incubadora), patrones de registro |
| Java 21 | septiembre de 2023 | **LTS**: **Hilos virtuales**, coincidencia de patrones, patrones `switch`, colecciones secuenciadas |
| Java 22 | marzo de 2024 | Plantillas de cadenas (vista previa), API de memoria externa |
| Java 23 | septiembre de 2024 | Tipos primitivos en patrones (vista previa) |
| Java 24 | marzo de 2025 | Simultaneidad estructurada (vista previa) |
| Java 25 | septiembre de 2025 | **LTS**: (esperado) |
## Hitos importantes
### La era clásica (1996-2004)
- **1.0 (1996)**: "Escribe una vez, ejecuta en cualquier lugar" — subprogramas, AWT
- **1.2 (1998)**: Marco de colecciones (la base de las colecciones de Java)
- **1.4 (2002)**: NIO, registro, expresiones regulares, afirmaciones
- **5.0 (2004)**: la mayor actualización: genéricos, enumeraciones, anotaciones, autoboxing, bucle for mejorado, varargs, `static import`
### La era empresarial (2006-2014)
- **6 (2006)**: compatibilidad con secuencias de comandos, API del compilador
- **7 (2011)**: `try-with-resources`, operador de diamante,`switch`en String, NIO.2
- **8 (2014)**: El otro "big bang": lambdas, streams, `Optional`, `java.time`, métodos predeterminados, `CompletableFuture`
### La era moderna (2017-presente)
- **9 (2017)**: Sistema de módulos (JPMS), `var`,`jshell`REPL
- **11 (2018)**: primer LTS con una cadencia de lanzamiento de 6 meses;  `HttpClient`; Cambio de licencia de Oracle JDK
- **17 (2021)**: LTS: clases selladas, coincidencia de patrones
- **21 (2023)**: LTS — **hilos virtuales** (Project Loom), coincidencia de patrones, registro de patrones
## La cadencia de lanzamiento de 6 meses
```
Before Java 9:  Major releases every 2-4 years
Java 9+:        New release every 6 months (March & September)
LTS releases:   Every ~2 years (8, 11, 17, 21, 25...)
Non-LTS:        Feature previews, 6-month support
```

## Viaje de genéricos
```
2004: Java 5.0 — type erasure generics (backward compatible)
2014: Java 8 — improved inference with lambdas
2016: Java 9 — diamond operator with anonymous classes
2018: Java 11 — `var` with generics
2023: Java 21 — record patterns with generics
```

## Evolución de la programación funcional
```
2004: Anonymous inner classes (verbose)
2004: Java 5 — enums as pseudo-functional
2014: Java 8 — lambdas, streams, Optional
2017: Java 9 — Stream API additions
2019: Java 12 — switch expressions
2023: Java 21 — pattern matching in switch, record patterns
```

## Evolución de la concurrencia
```
1.0:     Thread class, synchronized
1.5:     java.util.concurrent (Executors, locks, atomics)
1.7:     ForkJoinPool
1.8:     CompletableFuture, parallel streams
1.9:     Flow API (reactive streams)
1.19:    Virtual threads preview
1.21:    **Virtual threads** (Project Loom) — lightweight threads
```

## Evolución de las funciones del idioma
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

## Evolución de JVM
```
1.0:  Interpreter
1.3:  HotSpot (JIT compilation)
1.5:  Generics via type erasure
1.7:  InvokeDynamic (for JVM languages)
1.9:  Module system, AOT compilation (experimental)
16:   ZGC (low-latency GC) production-ready
21:   Virtual threads, generational ZGC
```

## Crecimiento del ecosistema
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
