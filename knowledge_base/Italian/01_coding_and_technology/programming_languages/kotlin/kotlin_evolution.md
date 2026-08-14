<!--
---
# Metadata
title: "Kotlin — Version History & Evolution"
description: "Comprehensive version history and evolution of Kotlin from 1.0 to modern Kotlin."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial version history"
tags: [kotlin, version-history, evolution, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "10 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

-->
# Kotlin: cronologia ed evoluzione delle versioni
## Cronologia
| Versione | Anno | Tema chiave |
|---------|------|-----------|
| 1.0 | 2016| Prima versione stabile (JetBrains) |
| 1.1 | 2017 | Coroutine, alias di tipo, destrutturazione in lambda |
| 1.2 | 2017 | Diffusione dell'array,`lateinit`livello superiore, virgole finali |
| 1.3 | 2018 | `inline class`,`contracts`(sperimentale) |
| 1.4 | 2020 | `@JvmDefault`, conversioni SAM per interfacce Kotlin |
| 1,5 | 2021 | `value class`, annotazione `OptIn`, valori letterali regex |
| 1.6 | 2021 | `when`esaustività,`Unit`ottimizzazione del rendimento |
| 1.7 | 2022 |  Voci `enum`, classi di valore`@JvmInline`|
| 1.8 | 2022 | `@SubclassOptInRequired`, anteprima del compilatore K2 |
| 1.9 | 2023 | **Compilatore K2**, oggetti`@ConsistentCopyVisibility`,`data`|
| 2.0 | 2024 | **Compilatore K2 stabile**, `@SubclassOptInRequired`, miglioramenti al cast intelligente |
| 2.1 | 2024 | `when`soggetti, miglioramenti alla delega della proprietà |
| 2.2 | 2025 | (previsto) Ulteriori miglioramenti K2 |
## Traguardi importanti
### L'inizio (2011–2016)
- **2011**: JetBrains annuncia Kotlin (dal nome dell'isola di Kotlin vicino a San Pietroburgo)
- **2012**: Kotlin open source
- **2016**: **Kotlin 1.0**: pronto per la produzione per JVM e Android
### Adozione di Android (2017-2019)
- **2017**: Google annuncia il supporto Kotlin di prima classe al Google I/O
- **1.1 (2017)**: **Coroutine**: programmazione asincrona leggera
- **1.2 (2017)**: progetti multipiattaforma (Kotlin/Native, Kotlin/JS)
- **1.3 (2018)**:`inline class`, contratti
### Gli anni della crescita (2020–2023)
- **1.5 (2021)**: `value class`, annotazione `OptIn`, tipi interi senza segno
- **1.7 (2022)**: voci `enum`, anteprima del compilatore K2
- **1.9 (2023)**: compilatore K2 (nuovo frontend, compilazione più veloce del 30%), oggetti `data`
### Kotlin moderno (2024-oggi)
- **2.0 (2024)**: **Compilatore K2 stabile**: importanti miglioramenti delle prestazioni, analisi migliore
- **2.1 (2024)**:`when`migliorato, delega della proprietà
## Evoluzione della coroutine
```
1.1:  Experimental coroutines (suspend functions, launch, async)
1.2:  Coroutine builder improvements
1.3:  Coroutine scope, structured concurrency, Dispatchers
1.5:  Flow API (cold async streams), StateFlow, SharedFlow
1.6:  Flow improvements, structured concurrency enforcement
1.9:  Coroutine debugging improvements
2.0:  Stable coroutine API
```

## Evoluzione multipiattaforma
```
1.2:  Kotlin Multiplatform (experimental)
1.3:  Kotlin/Native (iOS support)
1.4:  expect/actual mechanism
1.5:  Hierarchical multiplatform structure
1.9:  K2 with multiplatform support
2.0:  Compose Multiplatform (Jetpack Compose on iOS)
```

## Evoluzione delle funzionalità del linguaggio
```
Null Safety:
  1.0:  Nullable types (String?), safe calls (?.), Elvis (?:)
  1.5:  OptIn annotation for experimental APIs
  2.0:  Smart cast improvements

Pattern Matching:
  1.0:  when expression, is/as operators
  1.7:  when exhaustiveness checking
  2.1:  Enhanced when subjects

Data Classes:
  1.0:  data class (equals, hashCode, toString, copy, componentN)
  1.9:  data object
  2.0:  @ConsistentCopyVisibility

Value Classes:
  1.3:  inline class (experimental)
  1.5:  value class (renamed)
  1.7:  @JvmInline value class
```

## Kotlin su diverse piattaforme
```
2016: Kotlin/JVM (Android, server)
2017: Kotlin/JS (JavaScript)
2017: Kotlin/Native (iOS, macOS, Linux, Windows)
2018: Kotlin Multiplatform Mobile (KMM)
2021: Compose Multiplatform (desktop)
2023: Compose Multiplatform (iOS)
2025: Kotlin — official Android language; used server-side, iOS, web, embedded
```

## Crescita dell'ecosistema
```
2016: Kotlin 1.0 — JetBrains IDE plugin
2017: Google I/O — first-class Android support
2018: Android KTX, Spring Framework 5 Kotlin support
2019: Kotlin 1.3 — coroutines stable
2021: Kotlin 1.5 — multiplatform matures
2023: Kotlin 1.9 — K2 compiler
2024: Kotlin 2.0 — K2 stable, Compose Multiplatform
2025: Kotlin — top 15 most used language; dominant in Android
```

## Principi chiave di progettazione
```
1. Pragmatism — solve real problems
2. Conciseness — less boilerplate than Java
3. Safety — null safety at compile time
4. Interoperability — 100% Java compatible
5. Tooling — IntelliJ IDEA first-class support
6. Multiplatform — one language, many targets
```
