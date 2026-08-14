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

# Go – Versionsverlauf und Entwicklung
## Zeitleiste
| Version | Erscheinungsdatum | Schlüsselthema |
|---------|-------------|-----------|
| 1,0 | März 2012 | Erste stabile Veröffentlichung |
| 1.1 | Mai 2013 | Leistung, Renndetektor |
| 1,3 | Juni 2014 | Netzwerkabfrage, Krypto/TLS |
| 1,4 | Dez. 2014 | Bootstrap mit Go (Selbsthosting) |
| 1,5 | August 2015 | **Gleichzeitiger GC**, Schreibbarrieren |
| 1,7 | August 2016 |  `context`-Paket, `testing`-Untertests |
| 1,8 | Februar 2017 | `http.Server.Shutdown`, Plugins |
| 1,9 | August 2017 | Geben Sie Aliase ein, parallel`make`|
| 1.10 | Februar 2018 | `database/sql`Verbindungspool |
| 1.11 | August 2018 | **Go-Module**,`go mod`|
| 1.12 | Februar 2019 | TLS 1.3, Modulversionierung |
| 1.13 | September 2019 | `errors.Is/As`, Zahlenliterale`0b`,`0o`|
| 1,14 | Februar 2020 | **Überlappende E/A unter Windows**, Goroutine-Präemption |
| 1,15 | August 2020 | `time.Ticker`/`Timer`zurückgesetzt, Modul-Proxy |
| 1,16 | Februar 2021 |  `embed`-Paket, `io/fs`, standardmäßig modulbewusst |
| 1,17 | August 2021 | Slice-zu-Array-Konvertierung,`unsafe.Slice`|
| 1,18 | März 2022 | **Generika**, Fuzzing, Arbeitsbereiche |
| 1,19 | August 2022 | Doc-Kommentare, Überarbeitung des Speichermodells |
| 1,20 | Februar 2023 | `errors.Join`, profilgeführte Optimierung |
| 1,21 | August 2023 | **`slog`**,`min/max`eingebaut,`maps/slices`|
| 1,22 | Februar 2024 | Bereich über Ganzzahlen, erweitertes Routing |
| 1,23 | August 2024 | Iterator-Paket (`iter`), Timer-Änderungen |
| 1,24 | Februar 2025 |  `weak`-Paket, verbesserte Karten |
## Wichtige Meilensteine
### Der Anfang (2009–2012)
- **2009**: Go von Google angekündigt (Robert Griesemer, Rob Pike, Ken Thompson)
- **2012**: **Go 1.0** – „Das Go 1-Kompatibilitätsversprechen“
### Leistung und Werkzeuge (2012–2018)
- **1.1**: Leistungsverbesserung um mehr als 30 %; Renndetektor
- **1.5**: Gleichzeitiger Garbage Collector (GC-Pausen sinken von Millisekunden auf Mikrosekunden)
- **1.5**: Go-Compiler gebootet – geschrieben in Go (nicht mehr C)
- **1.7**: Das Paket`context`wird zum Standard
### Module & Ökosystem (2018–2021)
- **1.11**: **Go-Module** – offizielles Abhängigkeitsmanagement
- **1.13**:`errors.Is/As`– Fehlerumbruch wird idiomatisch
- **1.16**: `embed`-Paket – Dateien zur Kompilierungszeit einbetten
### Modern Go (2022–heute)
- **1.18**: **Generics** – Typparameter mit Einschränkungen
- **1.21**:`slog`– strukturierte Protokollierung in stdlib;  `min/max`-Einbauten
- **1.22**: Bereich über ganze Zahlen (`for i := range 10`)
- **1.23**: Iterator-Paket – verzögerte Auswertung in stdlib
## Generika-Reise
```
2010: "Go doesn't need generics" (early stance)
2016: Go generics proposal discussions begin
2018: Type parameters design draft published
2020: Go 2 generics proposal (draft designs)
2022: Go 1.18 — generics land! Type parameters, constraints
2023: Generic code patterns emerge (slices, maps packages)
2024: Community adapts — generic data structures, algorithms
```

## Fehlerbehandlungsphilosophie
```
1.0:     Explicit error returns — "errors are values"
1.13:    Error wrapping with %w — "inspect and unwrap"
1.20:    errors.Join — multiple errors
Future:  go2 proposal for try/handle (not yet adopted)
```

## Parallelitätsentwicklung
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

## Go-Kompatibilitätsversprechen
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

## Ökosystemwachstum
```
2012: Go 1.0 — basic stdlib, no package manager
2014: dep (early dependency management experiments)
2018: Go modules — official solution
2019: Go used by Uber, Twitch, Dropbox, Cloudflare
2022: Generics — opens new library design patterns
2023: Go in Kubernetes, Docker, Terraform, Hugo
2025: Top 10 most used language; cloud-native standard
```

## Leistungsentwicklung
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
