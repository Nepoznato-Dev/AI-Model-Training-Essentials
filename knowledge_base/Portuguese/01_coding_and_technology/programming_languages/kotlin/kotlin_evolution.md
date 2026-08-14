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
# Kotlin – Histórico de versões e evolução
## Linha do tempo
| Versão | Ano | Tema principal |
|--------|------|-----------|
| 1,0 | 2016 | Primeira versão estável (JetBrains) |
| 1.1 | 2017 | Corrotinas, aliases de tipo, desestruturação em lambdas |
| 1.2 | 2017 | Propagação da matriz, nível superior `lateinit`, vírgulas finais |
| 1.3 | 2018 |  `inline class`,`contracts`(experimental) |
| 1.4 | 2020 | `@JvmDefault`, conversões SAM para interfaces Kotlin |
| 1,5 | 2021 | `value class`, anotação `OptIn`, literais regex |
| 1.6 | 2021 |  Exaustividade `when`, otimização de retorno`Unit`|
| 1.7 | 2022 |  Entradas `enum`, classes de valor`@JvmInline`|
| 1.8 | 2022 |  `@SubclassOptInRequired`, visualização do compilador K2 |
| 1,9 | 2023 | **Compilador K2**, objetos`@ConsistentCopyVisibility`,`data`|
| 2.0 | 2024 | **Compilador K2 estável**,`@SubclassOptInRequired`, melhorias de conversão inteligente |
| 2.1 | 2024 |  Assuntos `when`, melhorias de delegação de propriedade |
| 2.2 | 2025 | (esperado) Outras melhorias no K2 |
## Marcos importantes
### O começo (2011–2016)
- **2011**: JetBrains anuncia Kotlin (em homenagem à Ilha Kotlin, perto de São Petersburgo)
- **2012**: código aberto Kotlin
- **2016**: **Kotlin 1.0** — pronto para produção para JVM e Android
### Adoção do Android (2017–2019)
- **2017**: Google anuncia suporte Kotlin de primeira classe no Google I/O
- **1.1 (2017)**: **Corrotinas** — programação assíncrona leve
- **1.2 (2017)**: Projetos multiplataforma (Kotlin/Native, Kotlin/JS)
- **1.3 (2018)**:`inline class`, contratos
### Os anos de crescimento (2020–2023)
- **1.5 (2021)**:`value class`, anotação `OptIn`, tipos inteiros sem sinal
- **1.7 (2022)**: entradas `enum`, visualização do compilador K2
- **1.9 (2023)**: compilador K2 (novo frontend, compilação 30% mais rápida), objetos `data`
### Kotlin moderno (2024-presente)
- **2.0 (2024)**: **Compilador K2 estável** — grandes melhorias de desempenho, melhor análise
- **2.1 (2024)**:`when`aprimorado, delegação de propriedade
## Evolução da corrotina
```
1.1:  Experimental coroutines (suspend functions, launch, async)
1.2:  Coroutine builder improvements
1.3:  Coroutine scope, structured concurrency, Dispatchers
1.5:  Flow API (cold async streams), StateFlow, SharedFlow
1.6:  Flow improvements, structured concurrency enforcement
1.9:  Coroutine debugging improvements
2.0:  Stable coroutine API
```

## Evolução Multiplataforma
```
1.2:  Kotlin Multiplatform (experimental)
1.3:  Kotlin/Native (iOS support)
1.4:  expect/actual mechanism
1.5:  Hierarchical multiplatform structure
1.9:  K2 with multiplatform support
2.0:  Compose Multiplatform (Jetpack Compose on iOS)
```

## Evolução dos recursos de linguagem
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

## Kotlin em diferentes plataformas
```
2016: Kotlin/JVM (Android, server)
2017: Kotlin/JS (JavaScript)
2017: Kotlin/Native (iOS, macOS, Linux, Windows)
2018: Kotlin Multiplatform Mobile (KMM)
2021: Compose Multiplatform (desktop)
2023: Compose Multiplatform (iOS)
2025: Kotlin — official Android language; used server-side, iOS, web, embedded
```

## Crescimento do Ecossistema
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

## Princípios-chave de design
```
1. Pragmatism — solve real problems
2. Conciseness — less boilerplate than Java
3. Safety — null safety at compile time
4. Interoperability — 100% Java compatible
5. Tooling — IntelliJ IDEA first-class support
6. Multiplatform — one language, many targets
```
