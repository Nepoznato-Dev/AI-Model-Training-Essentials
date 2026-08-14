---
# Metadata
title: "Go — Version History & Evolution"
description: "Comprehensive version history and evolution of Go from 1.0 to modern Go."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
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
# Ir - Historial de versiones y evolución
## Línea de tiempo
| Versión | Fecha de lanzamiento | Tema clave |
|---------|-------------|-----------|
| 1.0 | marzo de 2012 | Primera versión estable |
| 1.1 | Mayo 2013 | Rendimiento, detector de carreras |
| 1.3 | junio de 2014 | Sondeo de red, cripto/tls |
| 1.4 | diciembre de 2014 | Bootstrap con Go (autohospedaje) |
| 1.5 | agosto de 2015 | **GC concurrente**, barreras de escritura |
| 1.7 | agosto de 2016 |  Paquete `context`, subpruebas`testing`|
| 1.8 | febrero de 2017 |  `http.Server.Shutdown`, complementos |
| 1.9 | agosto de 2017 | Alias ​​de tipos, paralelos`make`|
| 1.10 | febrero de 2018 |  Grupo de conexiones`database/sql`|
| 1.11 | agosto de 2018 | **Ir a módulos**,`go mod`|
| 1.12 | febrero de 2019 | TLS 1.3, versionado del módulo |
| 1.13 | Septiembre de 2019 |  `errors.Is/As`, números literales `0b`,`0o`|
| 1.14 | febrero de 2020 | **E/S superpuestas en Windows**, preferencia de rutinas |
| 1.15 | agosto de 2020 |  Restablecimiento de`time.Ticker`/ `Timer`, proxy del módulo |
| 1.16 | febrero de 2021 |  Paquete `embed`, `io/fs`, compatible con módulos de forma predeterminada |
| 1.17 | agosto de 2021 | Conversión de segmento a matriz,`unsafe.Slice`|
| 1.18 | marzo de 2022 | **Genéricos**, fuzzing, espacios de trabajo |
| 1.19 | agosto de 2022 | Comentarios del documento, revisión del modelo de memoria |
| 1.20 | febrero de 2023 |  `errors.Join`, optimización guiada por perfiles |
| 1.21 | agosto de 2023 | **`slog`**,`min/max`incorporados,`maps/slices`|
| 1.22 | febrero de 2024 | Rango sobre números enteros, enrutamiento mejorado |
| 1.23 | agosto de 2024 | Paquete iterador (`iter`), cambios de temporizador |
| 1.24 | febrero de 2025 |  Paquete `weak`, mapas mejorados |
## Hitos importantes
### El comienzo (2009-2012)
- **2009**: Go anunciado por Google (Robert Griesemer, Rob Pike, Ken Thompson)
- **2012**: **Go 1.0** — "La promesa de compatibilidad de Go 1"
### Rendimiento y herramientas (2012-2018)
- **1.1**: mejora del rendimiento superior al 30%; detector de carrera
- **1.5**: Recolector de basura simultáneo (las pausas del GC caen de milisegundos a microsegundos)
- **1.5**: compilador de Go arrancado, escrito en Go (no más C)
- **1.7**: el paquete`context`se convierte en estándar
### Módulos y ecosistema (2018-2021)
- **1.11**: **Módulos Go** — gestión oficial de dependencias
- **1.13**: `errors.Is/As`: el ajuste de errores se vuelve idiomático
- **1.16**: paquete `embed`: incrustar archivos en tiempo de compilación
### Go moderno (2022-presente)
- **1.18**: **Genéricos** — parámetros de tipo con restricciones
- **1.21**:`slog`— registro estructurado en stdlib; `min/max`incorporados
- **1.22**: Rango sobre números enteros (`for i := range 10`)
- **1.23**: Paquete Iterador: evaluación diferida en stdlib
## Viaje de genéricos
```
2010: "Go doesn't need generics" (early stance)
2016: Go generics proposal discussions begin
2018: Type parameters design draft published
2020: Go 2 generics proposal (draft designs)
2022: Go 1.18 — generics land! Type parameters, constraints
2023: Generic code patterns emerge (slices, maps packages)
2024: Community adapts — generic data structures, algorithms
```

## Filosofía de manejo de errores
```
1.0:     Explicit error returns — "errors are values"
1.13:    Error wrapping with %w — "inspect and unwrap"
1.20:    errors.Join — multiple errors
Future:  go2 proposal for try/handle (not yet adopted)
```

## Evolución de la concurrencia
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

## Ir a la promesa de compatibilidad
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

## Crecimiento del ecosistema
```
2012: Go 1.0 — basic stdlib, no package manager
2014: dep (early dependency management experiments)
2018: Go modules — official solution
2019: Go used by Uber, Twitch, Dropbox, Cloudflare
2022: Generics — opens new library design patterns
2023: Go in Kubernetes, Docker, Terraform, Hugo
2025: Top 10 most used language; cloud-native standard
```

## Evolución del rendimiento
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
