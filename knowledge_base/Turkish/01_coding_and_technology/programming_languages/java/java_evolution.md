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

# Java — Sürüm Geçmişi ve Gelişimi
## Zaman Çizelgesi
| Sürüm | Çıkış Tarihi | Anahtar Tema |
|-----------|---------------|-----------|
| JDK 1.0 | Ocak 1996 | İlk sürüm ("Meşe") |
| JDK 1.1 | Şubat 1997 | İç sınıflar, JDBC, RMI |
| J2SE 1.2 | Aralık 1998 | Koleksiyonlar çerçevesi, Swing,`strictfp`|
| J2SE 1.3 | Mayıs 2000 | HotSpot JVM,`assert`|
| J2SE 1.4 | Şubat 2002 |  `assert`, NIO, normal ifade,`java.net`|
| J2SE 5.0 | Eylül 2004 | **Ana**: Geneller, numaralandırmalar, ek açıklamalar, otomatik kutulama, varargs |
| Java SE 6 | Aralık 2006 | Komut dosyası oluşturma, derleyici API'si, arayüzlerde`@Override`|
| Java SE 7 | Temmuz 2011 | `try-with-resources`, Dize üzerinde `switch`, NIO.2 |
| Java SE 8 | Mart 2014 | **Ana**: Lambdalar, Akışlar, `Optional`, `java.time`, varsayılan yöntemler |
| Java 9 | Eylül 2017 | Modüller (JPMS),`var`,`jshell`, özel arayüz yöntemleri |
| Java 10 | Mart 2018 |  yerel değişkenler için`var`|
| Java 11 | Eylül 2018 | **LTS**:`String`yöntemleri, `HttpClient`, tek dosya başlatma |
| Java 12 | Mart 2019 | İfadeleri değiştir (önizleme) |
| Java 13 | Eylül 2019 | Metin blokları (önizleme) |
| Java 14 | Mart 2020 | `record`(önizleme), anahtar ifadeleri,`instanceof`modeli |
| Java 15 | Eylül 2020 | Metin blokları, mühürlü sınıflar (önizleme) |
| Java 16 | Mart 2021 | `record`,`instanceof`desen eşleştirme |
| Java 17 | Eylül 2021 | **LTS**: Kapalı sınıflar,`switch`için model eşleştirme |
| Java 18 | Mart 2022 | Basit web sunucusu, varsayılan UTF-8 |
| Java 19 | Eylül 2022 | Sanal konular (önizleme), desen eşleştirme |
| Java 20 | Mart 2023 | Kapsamlı değerler (kuluçka makinesi), kayıt modelleri |
| Java 21 | Eylül 2023 | **LTS**: **Sanal iş parçacıkları**, desen eşleştirme,`switch`desenleri, sıralı koleksiyonlar |
| Java 22 | Mart 2024 | Dize şablonları (önizleme), yabancı bellek API'si |
| Java 23 | Eylül 2024 | Desenlerdeki ilkel türler (önizleme) |
| Java 24 | Mart 2025 | Yapılandırılmış eşzamanlılık (önizleme) |
| Java 25 | Eylül 2025 | **LTS**: (beklenen) |
## Önemli Kilometre Taşları
### Klasik Çağ (1996–2004)
- **1.0 (1996)**: "Bir Kez Yaz, Her Yerde Çalıştır" — uygulamalar, AWT
- **1.2 (1998)**: Koleksiyonlar çerçevesi (Java koleksiyonlarının temeli)
- **1.4 (2002)**: NIO, günlük kaydı, normal ifade, iddialar
- **5.0 (2004)**: En büyük güncelleme — jenerikler, numaralandırmalar, ek açıklamalar, otomatik kutulama, geliştirilmiş for-döngüsü, varargs, `static import`
### İşletme Çağı (2006–2014)
- **6 (2006)**: Komut dosyası desteği, derleyici API'si
- **7 (2011)**:`try-with-resources`, elmas operatörü, String üzerinde `switch`, NIO.2
- **8 (2014)**: Diğer "büyük patlama" — lambdalar, akışlar,`Optional`,`java.time`, varsayılan yöntemler, `CompletableFuture`
### Modern Çağ (2017-günümüz)
- **9 (2017)**: Modül sistemi (JPMS),`var`,`jshell`REPL
- **11 (2018)**: 6 aylık yayın temposu altındaki ilk LTS; `HttpClient`; Oracle JDK lisans değişikliği
- **17 (2021)**: LTS — mühürlü sınıflar, kalıp eşleştirme
- **21 (2023)**: LTS — **sanal iş parçacıkları** (Proje Tezgahı), desen eşleştirme, kayıt desenleri
## 6 Aylık Yayın Temposu
```
Before Java 9:  Major releases every 2-4 years
Java 9+:        New release every 6 months (March & September)
LTS releases:   Every ~2 years (8, 11, 17, 21, 25...)
Non-LTS:        Feature previews, 6-month support
```

## Jenerik Yolculuğu
```
2004: Java 5.0 — type erasure generics (backward compatible)
2014: Java 8 — improved inference with lambdas
2016: Java 9 — diamond operator with anonymous classes
2018: Java 11 — `var` with generics
2023: Java 21 — record patterns with generics
```

## Fonksiyonel Programlamanın Evrimi
```
2004: Anonymous inner classes (verbose)
2004: Java 5 — enums as pseudo-functional
2014: Java 8 — lambdas, streams, Optional
2017: Java 9 — Stream API additions
2019: Java 12 — switch expressions
2023: Java 21 — pattern matching in switch, record patterns
```

## Eşzamanlılık Gelişimi
```
1.0:     Thread class, synchronized
1.5:     java.util.concurrent (Executors, locks, atomics)
1.7:     ForkJoinPool
1.8:     CompletableFuture, parallel streams
1.9:     Flow API (reactive streams)
1.19:    Virtual threads preview
1.21:    **Virtual threads** (Project Loom) — lightweight threads
```

## Dil Özelliği Gelişimi
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

## JVM'nin Evrimi
```
1.0:  Interpreter
1.3:  HotSpot (JIT compilation)
1.5:  Generics via type erasure
1.7:  InvokeDynamic (for JVM languages)
1.9:  Module system, AOT compilation (experimental)
16:   ZGC (low-latency GC) production-ready
21:   Virtual threads, generational ZGC
```

## Ekosistem Büyümesi
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
