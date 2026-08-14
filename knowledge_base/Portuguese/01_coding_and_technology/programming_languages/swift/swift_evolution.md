<!--
---
# Metadata
title: "Swift — Version History & Evolution"
description: "Comprehensive version history and evolution of Swift from 1.0 to modern Swift."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial version history"
tags: [swift, version-history, evolution, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "10 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

-->
# Swift – Histórico de versões e evolução
## Linha do tempo
| Versão | Ano | Tema principal |
|--------|------|-----------|
| 1,0 | 2014 | Lançamento inicial (Chris Lattner, Apple) |
| 1.1 | 2014 | Inicializadores com falha,`@autoclosure`|
| 1.2 | 2015 | `as?`/`as!`, tipo `Set`, comparações de tupla |
| 2.0 | 2015 | Extensões de protocolo,`defer`,`guard`,`errortype`|
| 2.1 | 2015 | `try?`, interpolação de strings em literais |
| 2.2 | 2016 | `#selector`,`defer`, tupla retorna |
| 3.0 | 2016 | **Principal**: Redesenho da API — convenções de nomenclatura,`@discardableResult`|
| 4,0 | 2017 | `Codable`,`String`reescrita, literais multilinhas |
| 5,0 | 2019 | **Principal**: preparação `async/await`, estabilidade ABI, tipo`Result`|
| 5.1 | 2019 | `some`(tipos opacos), wrappers de propriedades,`@resultBuilder`|
| 5.2 | 2020 | Chamada como função,`KeyPath`como função |
| 5.3 | 2020 |  `@MainActor`, vários fechamentos finais, melhorias`enum`|
| 5.4 | 2021 | Vários parâmetros variados, melhorias`@resultBuilder`|
| 5.5 | 2021 | **`async/await`**, atores,`Sendable`|
| 5.6 | 2022 |  Palavra-chave `any`,`Clock`,`Duration`|
| 5.7 | 2022 |  Abreviação `if let`, literais `Regex`, protocolo`Clock`|
| 5.8 | 2023 | Implantação de volta de função, melhorias`Clock`|
| 5.9 | 2023 | **Macros**, pacotes de parâmetros,`consume`/`discard`|
| 5.10 | 2024 | Verificação completa de simultaneidade, segurança rigorosa na corrida de dados |
| 6,0 | 2024 | **Principal**: Simultaneidade estrita por padrão, lançamentos digitados |
| 6.1 | 2025 | (esperado) Mais refinamentos de simultaneidade |
## Marcos importantes
### Swift 1.x - Nascimento (2014–2015)
- **2014**: Anunciado na WWDC; substitui Objective-C para desenvolvimento Apple
- **1.0**: Opcionais, genéricos, fechamentos, inferência de tipo, protocolos
- **1.2**: padrão`as?`/ `as!`, tipo `Set`
### Swift 2.x — Tratamento de erros (2015–2016)
- **2.0**: Extensões de protocolo (programação orientada a protocolo),`guard`,`defer`,`do/try/catch`
- **2.1**:`try?`para tratamento de erros opcional
### Swift 3.x — A grande renomeação de API (2016)
- **3.0**: Redesenho massivo da API — "Grand Unified Renomeing"
- Convenções de nomenclatura:`stringByAppendingString`→`appending`
- Removidos loops`for`estilo C, operadores`++`/ `--`
- Primeiros rótulos de parâmetros por padrão
### Swift 4.x – Codificável (2017)
- **4.0**: protocolo`Codable`(codificação/decodificação JSON), reescrita `String`, literais de string multilinha
### Swift 5.x – Estabilidade (2019–2024)
- **5.0**: estabilidade ABI (aplicativos ficam menores), tipo `Result`, strings brutas
- **5.1**: Tipos opacos (`some View`), wrappers de propriedades (`@State`,`@Binding`)
- **5.5**: **`async/await` **, atores, protocolo `Sendable`
- **5.9**: Macros (geração de código em tempo de compilação), pacotes de parâmetros
### Swift 6.x — Segurança de simultaneidade (2024–presente)
- **6.0**: verificação estrita de simultaneidade por padrão, lançamentos digitados
## Evolução da simultaneidade
```
1.0:  GCD (Grand Central Dispatch) — Objective-C pattern
2.0:  Protocol extensions for async patterns
5.5:  async/await, actors, Sendable
5.10: Complete concurrency checking
6.0:  Strict concurrency by default (data race safety)
```

## Tipo Evolução do Sistema
```
1.0:  Optionals, generics, protocols
2.0:  Protocol extensions, protocol composition
4.0:  Codable, associated type constraints
5.1:  Opaque types (some), property wrappers
5.9:  Macros, parameter packs (variadic generics)
6.0:  Typed throws, strict Sendable
```

## Swift em outras plataformas
```
2015: Swift open-sourced (Apache 2.0)
2015: Swift on Linux (Ubuntu)
2016: Swift on ARM (Raspberry Pi)
2017: Swift on Windows (experimental)
2019: TensorFlow Swift (later discontinued)
2020: Swift on AWS Lambda
2021: Vapor (server-side Swift framework)
2023: Swift on embedded systems (embedded Swift)
2025: Swift — cross-platform systems language
```

## Processo de evolução rápida
```
SE-0001 (2015): First proposal
Over 400 proposals accepted by 2025
Key proposals:
  SE-0044: Import as member
  SE-0110: Distributed actors
  SE-0295: Codable improvements
  SE-0302: Sendable and @Sendable closures
  SE-0335: Introduce existential any
  SE-0346: Lightweight same-type requirements (some)
  SE-0401: Remove Actor Isolation Inference
  SE-0413: Typed throws
```

## Crescimento do Ecossistema
```
2014: Swift announced — replaces Objective-C
2015: Open source; Swift Package Manager
2016: Swift 3 — API redesign
2017: Swift 4 — Codable
2019: Swift 5 — ABI stability
2021: SwiftUI matures
2023: Swift 5.9 — macros
2025: Swift 6 — data race safety; used in iOS, macOS, server, embedded
```
