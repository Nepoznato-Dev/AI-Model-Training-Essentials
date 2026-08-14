---
# Metadata
title: "Go — Version History & Evolution"
description: "Comprehensive version history and evolution of Go from 1.0 to modern Go."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial version history"
tags: [go, golang, version-history, evolution, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "10 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

# Go – Histórico de versões e evolução
## Linha do tempo
| Versão | Data de lançamento | Tema principal |
|--------|-------------|-----------|
| 1,0 | Março de 2012 | Primeira versão estável |
| 1.1 | Maio de 2013 | Desempenho, detector de corrida |
| 1.3 | Junho de 2014 | Pesquisa de rede, criptografia/tls |
| 1.4 | dezembro de 2014 | Bootstrap com Go (auto-hospedagem) |
| 1,5 | agosto de 2015 | **GC simultâneo**, barreiras de gravação |
| 1.7 | agosto de 2016 |  Pacote `context`, subtestes`testing`|
| 1.8 | Fevereiro de 2017 |  `http.Server.Shutdown`, plug-ins |
| 1,9 | agosto de 2017 | Aliases de tipo, paralelos`make`|
| 1.10 | Fevereiro de 2018 |  Conjunto de conexões`database/sql`|
| 1.11 | agosto de 2018 | **Módulos Go**,`go mod`|
| 1.12 | Fevereiro de 2019 | TLS 1.3, versionamento de módulo |
| 1.13 | Setembro de 2019 | `errors.Is/As`, números literais`0b`,`0o`|
| 1.14 | Fevereiro de 2020 | **E/S sobreposta no Windows**, preempção de goroutine |
| 1,15 | Agosto de 2020 |  Redefinição de`time.Ticker`/ `Timer`, proxy do módulo |
| 1.16 | Fevereiro de 2021 |  Pacote `embed`,`io/fs`, com reconhecimento de módulo por padrão |
| 1.17 | agosto de 2021 | Conversão de fatia para matriz,`unsafe.Slice`|
| 1.18 | Março de 2022 | **Genéricos**, difusão, espaços de trabalho |
| 1.19 | agosto de 2022 | Comentários do documento, revisão do modelo de memória |
| 1,20 | Fevereiro de 2023 |  `errors.Join`, otimização guiada por perfil |
| 1.21 | agosto de 2023 | **`slog`**,`min/max`integrado,`maps/slices`|
| 1.22 | Fevereiro de 2024 | Faixa sobre números inteiros, roteamento aprimorado |
| 1.23 | agosto de 2024 | Pacote Iterador (`iter`), alterações no temporizador |
| 1,24 | Fevereiro de 2025 |  Pacote `weak`, mapas aprimorados |
## Marcos importantes
### O começo (2009–2012)
- **2009**: Go anunciado pelo Google (Robert Griesemer, Rob Pike, Ken Thompson)
- **2012**: **Go 1.0** — "A promessa de compatibilidade do Go 1"
### Desempenho e ferramentas (2012–2018)
- **1,1**: 30%+ melhoria de desempenho; detector de corrida
- **1,5**: coletor de lixo simultâneo (as pausas do GC caem de milissegundos para microssegundos)
- **1.5**: compilador Go inicializado - escrito em Go (não mais C)
- **1.7**: pacote`context`torna-se padrão
### Módulos e Ecossistema (2018–2021)
- **1.11**: **Módulos Go** — gerenciamento oficial de dependências
- **1.13**:`errors.Is/As`— o agrupamento de erros torna-se idiomático
- **1.16**: pacote`embed`— incorpora arquivos em tempo de compilação
### Modern Go (2022-presente)
- **1.18**: **Genéricos** — digite parâmetros com restrições
- **1.21**:`slog`— registro estruturado em stdlib; `min/max`integrado
- **1,22**: Intervalo sobre números inteiros (`for i := range 10`)
- **1.23**: Pacote Iterator — avaliação lenta em stdlib
## Jornada dos Genéricos
```
2010: "Go doesn't need generics" (early stance)
2016: Go generics proposal discussions begin
2018: Type parameters design draft published
2020: Go 2 generics proposal (draft designs)
2022: Go 1.18 — generics land! Type parameters, constraints
2023: Generic code patterns emerge (slices, maps packages)
2024: Community adapts — generic data structures, algorithms
```

## Filosofia de tratamento de erros
```
1.0:     Explicit error returns — "errors are values"
1.13:    Error wrapping with %w — "inspect and unwrap"
1.20:    errors.Join — multiple errors
Future:  go2 proposal for try/handle (not yet adopted)
```

## Evolução da simultaneidade
```
1.0:  Goroutines + channels — CSP-inspired
1.1:  Race detector
1.4:  Non-blocking syscalls (net poller)
1.5:  Concurrent GC
1.7:  context package for cancellation
1.14: Cooperative goroutine preemption (signals)
1.21: Synchronization improvements
1.23: iter package — iterator pattern
```

## Promessa de compatibilidade Go
```
Go 1.0 (2012): "Go 1 will be available for a long time.
  Compatibility is important. Programs that work at Go 1
  will continue to work at every subsequent Go 1 release."

This means:
- No breaking changes to the language spec
- No breaking changes to the standard library
- Only additive changes
- Forward compatibility guaranteed
```

## Crescimento do Ecossistema
```
2012: Go 1.0 — basic stdlib, no package manager
2014: dep (early dependency management experiments)
2018: Go modules — official solution
2019: Go used by Uber, Twitch, Dropbox, Cloudflare
2022: Generics — opens new library design patterns
2023: Go in Kubernetes, Docker, Terraform, Hugo
2025: Top 10 most used language; cloud-native standard
```

## Evolução do desempenho
```
Go 1.0:  Baseline
Go 1.1:  ~30% faster (register-based calling prep)
Go 1.5:  Concurrent GC (pause time: ms → μs)
Go 1.7:  SSA backend (15-30% faster)
Go 1.11: PGO experiments
Go 1.13: Faster map operations
Go 1.18: Generics (initial overhead, optimized in 1.19+)
Go 1.20: Profile-guided optimization
Go 1.22: Faster crypto, improved compiler
```
