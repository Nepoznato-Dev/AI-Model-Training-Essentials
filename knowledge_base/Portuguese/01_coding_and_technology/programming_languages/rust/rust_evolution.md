---
# Metadata
title: "Rust — Version History & Evolution"
description: "Comprehensive version history and evolution of Rust from early development to modern Rust."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial version history"
tags: [rust, version-history, evolution, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "10 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

# Rust – Histórico de versões e evolução
## Linha do tempo
| Versão | Data de lançamento | Tema principal |
|--------|-------------|-----------|
| 0,1 | Janeiro de 2012 | Primeiro compilador (rustc), simultaneidade baseada em tarefas |
| 0,5 | 2012 | Sistema de tipos baseado em características toma forma |
| 0,6 | 2012 | Remoção de caixas gerenciadas`@`|
| 0,7 | 2013 | `@`removido,`~`para caixas próprias |
| 0,8 | 2013 | Anotações vitalícias,`&mut`|
| 0,9 | Janeiro de 2014 | Limpeza final pré-1.0 |
| 0,10 | Fevereiro 2014 | Última versão pré-1.0 |
| 0,11 | abril de 2014 | `Box<T>`substitui`~T`|
| 0,12 | Maio de 2014 |  A reescrita do módulo`io`começa |
| 1,0 | 15 de maio de 2015 | **Lançamento estável** — "Rust 1.0" |
| 1.10 | agosto de 2016 |  Propagação de erro`?`(como`try!`→`?`) |
| 1,15 | Fevereiro de 2017 | Primeiro Rust estável com preparação`impl Trait`|
| 1.18 | Junho de 2017 | `pub(crate)`, compilação incremental |
| 1,20 | Outubro 2017 | Constantes associadas |
| 1,26 | Maio de 2018 | `impl Trait`na posição de argumento/retorno |
| 1,28 | Setembro de 2018 | Alocadores globais |
| 1.31 | dezembro de 2018 | **Edição Rust 2018** — módulos,`dyn Trait`|
| 1,34 | abril de 2019 | Registros alternativos |
| 1,39 | Novembro de 2019 | `async/await`em estável |
| 1,44 | Julho de 2020 | Melhorias de diagnóstico |
| 1,51 | abril de 2021 |  Genéricos`const`(MVP) |
| 1,56 | Out 2021 | **Edição Rust 2021** — fechamentos, IntoIterator |
| 1,59 | Fevereiro de 2022 | Montagem em linha |
| 1,62 | Junho de 2022 | `#[default]`para enumerações |
| 1,65 | dezembro de 2022 | `let else`|
| 1,68 | Março de 2023 |  `#[ffi_pure]`, otimização guiada por perfil |
| 1,70 | Junho de 2023 | Dependências`crates.io`isoladas |
| 1,74 | Novembro de 2023 | Modo off-line de carga |
| 1,76 | Fevereiro de 2024 | **Edição Rust 2024** — Blocos `gen`,`unsafe extern`|
| 1,79 | Junho de 2024 | `LazyCell`,`LazyLock`|
| 1,82 | Out 2024 | `unsafe`em blocos`extern`necessários |
| 1,85 | Fevereiro de 2025 | Edição Rust 2024 estabilizada |
## Marcos importantes
### Pré-1.0 (2010–2015)
- **2010**: O projeto paralelo de Graydon Hoare na Mozilla ganha força
- **2012**: Primeiro compilador público; sistema de tipos passa por grande reformulação
- **2013**: O modelo de propriedade se cristaliza;  Caixas`@`removidas
- **2014**: Processo Rust RFC formalizado; comunidade cresce
- **2015**: **1,0** — garantia de estabilidade; "abstrações de custo zero"
### Os anos de crescimento (2015–2019)
- **2015**: Cargo se torna o gerenciador de pacotes padrão
- **2018**: **Rust 2018 Edition** — revisão do sistema do módulo,`dyn Trait`,`impl Trait`
- **2019**:`async/await`chega à estabilidade — início do ecossistema assíncrono
### Maturidade (2020-presente)
- **2021**: **Rust 2021 Edition** — desambiguação de campos em encerramentos,`IntoIterator`para matrizes
- **2024**: **Edição Rust 2024** — Blocos `gen`, requisitos `unsafe extern`
- **2025**: Ferrugem no kernel Linux, Android, Windows, infraestrutura AWS
## Sistema de Edição
```
Rust 2015:  The baseline (1.0)
Rust 2018:  Module system, async/await prep, dyn Trait
Rust 2021:  Closure changes, IntoIterator, panic macros
Rust 2024:  gen blocks, unsafe extern, tail expressions

Key principle: Editions are opt-in, never break existing code.
Old editions always compile. New editions add features.
```

## Evolução da propriedade
```
2010: GC-based, like Erlang
2011: Region-based lifetimes proposed
2012: Ownership model emerges (unique, shared, owned)
2013: Simplified to &T / &mut T / Box<T>
2014: Box<T> replaces ~T; Rc<T> for shared ownership
2015: 1.0 — ownership model finalized
2018: Non-Lexical Lifetimes (NLL) in Rust 2018
2021: IntoIterator for arrays (was blocked by edition concerns)
2024: Further NLL improvements
```

## Evolução Assíncrona
```
2018: futures 0.1 — early async with manual polling
2019: async/await syntax (Rust 1.39)
2019: tokio 0.2 — async runtime
2020: async-std — std-like async API
2021: tokio 1.0 — stable async runtime
2023: async fn in traits (Rust 1.75)
2024: async closures, improved Send bounds
```

## Crescimento do Ecossistema
```
2015: crates.io launches (~2,000 crates)
2018: Rust most loved language (Stack Overflow survey)
2019: 30,000 crates on crates.io
2021: Most admired language (6th consecutive year)
2023: 130,000+ crates
2025: Used in Linux kernel, Android, Windows, Chromium, AWS, Cloudflare, Discord, Dropbox
```

## Principais RFCs
| RFC | Ano | Recurso |
|------|------|---------|
| 25 | 2013 | Correspondência de padrões |
| 153 | 2014 |  Tipo`Result`|
| 217 | 2014 |  Operador`?`(tentar) |
| 460 | 2016 | `?`substitui`try!`|
| 1210 | 2015 | `impl Trait`|
| 1414 | 2016 | Edição Ferrugem 2018 |
| 2394 | 2018 | `async/await`|
| 2515 | 2018 | `const`genéricos |
| 3013 | 2020 | Verificando compilação condicional |
| 3517 | 2023 |  Blocos`gen`|