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

# Java — Riwayat Versi & Evolusi
## Garis Waktu
| Versi | Tanggal Rilis | Tema Utama |
|---------|-------------|-----------|
| JDK 1.0 | Januari 1996 | Rilis awal ("Oak") |
| JDK 1.1 | Februari 1997 | Kelas dalam, JDBC, RMI |
| J2SE 1.2 | Desember 1998 | Kerangka koleksi, Ayunan,`strictfp`|
| J2SE 1.3 | Mei 2000 | HotSpot JVM,`assert`|
| J2SE 1.4 | Februari 2002 | `assert`, NIO, regex,`java.net`|
| J2SE 5.0 | September 2004 | **Mayor**: Generik, enum, anotasi, autoboxing, varargs |
| Jawa SE 6 | Desember 2006 | Scripting, API compiler,`@Override`pada antarmuka |
| Jawa SE 7 | Juli 2011 | `try-with-resources`,`switch`pada String, NIO.2 |
| Jawa SE 8 | Maret 2014 | **Mayor**: Lambdas, Streams,`Optional`,`java.time`, metode default |
| Jawa 9 | September 2017 | Modul (JPMS),`var`,`jshell`, metode antarmuka pribadi |
| Jawa 10 | Maret 2018 | `var`untuk variabel lokal |
| Jawa 11 | September 2018 | **LTS**: Metode `String`,`HttpClient`, peluncuran file tunggal |
| Jawa 12 | Maret 2019 | Ganti ekspresi (pratinjau) |
| Jawa 13 | September 2019 | Blok teks (pratinjau) |
| Jawa 14 | Maret 2020 | `record`(pratinjau), ekspresi peralihan, pola`instanceof`|
| Jawa 15 | September 2020 | Blok teks, kelas tersegel (pratinjau) |
| Jawa 16 | Maret 2021 |  Pencocokan pola`record`,`instanceof`|
| Jawa 17 | September 2021 | **LTS**: Kelas tersegel, pencocokan pola untuk`switch`|
| Jawa 18 | Maret 2022 | Server web sederhana, default UTF-8 |
| Jawa 19 | September 2022 | Utas virtual (pratinjau), pencocokan pola |
| Jawa 20 | Maret 2023 | Nilai cakupan (inkubator), pola rekaman |
| Jawa 21 | September 2023 | **LTS**: **Utas virtual**, pencocokan pola, pola `switch`, koleksi berurutan |
| Jawa 22 | Maret 2024 | Templat string (pratinjau), API memori asing |
| Jawa 23 | September 2024 | Tipe primitif dalam pola (pratinjau) |
| Jawa 24 | Maret 2025 | Konkurensi terstruktur (pratinjau) |
| Jawa 25 | September 2025 | **LTS**: (diharapkan) |
## Tonggak Penting
### Era Klasik (1996–2004)
- **1.0 (1996)**: "Tulis Sekali, Jalankan Di Mana Saja" — applet, AWT
- **1.2 (1998)**: Kerangka koleksi (dasar koleksi Java)
- **1.4 (2002)**: NIO, logging, regex, pernyataan
- **5.0 (2004)**: Pembaruan terbesar — generik, enum, anotasi, autoboxing, peningkatan for-loop, varargs, `static import`
### Era Perusahaan (2006–2014)
- **6 (2006)**: Dukungan skrip, API kompiler
- **7 (2011)**:`try-with-resources`, operator berlian,`switch`pada String, NIO.2
- **8 (2014)**: "big bang" lainnya — lambda, stream,`Optional`,`java.time`, metode default, `CompletableFuture`
### Era Modern (2017–sekarang)
- **9 (2017)**: Sistem modul (JPMS),`var`,`jshell`REPL
- **11 (2018)**: LTS pertama dengan irama rilis 6 bulan; `HttpClient`; Perubahan lisensi Oracle JDK
- **17 (2021)**: LTS — kelas tersegel, pencocokan pola
- **21 (2023)**: LTS — **utas virtual** (Project Loom), pencocokan pola, pola rekaman
## Irama Rilis 6 Bulan
```
Before Java 9:  Major releases every 2-4 years
Java 9+:        New release every 6 months (March & September)
LTS releases:   Every ~2 years (8, 11, 17, 21, 25...)
Non-LTS:        Feature previews, 6-month support
```

## Perjalanan Generik
```
2004: Java 5.0 — type erasure generics (backward compatible)
2014: Java 8 — improved inference with lambdas
2016: Java 9 — diamond operator with anonymous classes
2018: Java 11 — `var` with generics
2023: Java 21 — record patterns with generics
```

## Evolusi Pemrograman Fungsional
```
2004: Anonymous inner classes (verbose)
2004: Java 5 — enums as pseudo-functional
2014: Java 8 — lambdas, streams, Optional
2017: Java 9 — Stream API additions
2019: Java 12 — switch expressions
2023: Java 21 — pattern matching in switch, record patterns
```

## Evolusi Konkurensi
```
1.0:     Thread class, synchronized
1.5:     java.util.concurrent (Executors, locks, atomics)
1.7:     ForkJoinPool
1.8:     CompletableFuture, parallel streams
1.9:     Flow API (reactive streams)
1.19:    Virtual threads preview
1.21:    **Virtual threads** (Project Loom) — lightweight threads
```

## Evolusi Fitur Bahasa
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

## Evolusi JVM
```
1.0:  Interpreter
1.3:  HotSpot (JIT compilation)
1.5:  Generics via type erasure
1.7:  InvokeDynamic (for JVM languages)
1.9:  Module system, AOT compilation (experimental)
16:   ZGC (low-latency GC) production-ready
21:   Virtual threads, generational ZGC
```

## Pertumbuhan Ekosistem
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
