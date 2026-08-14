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
# Go — historia wersji i ewolucja
## Oś czasu
| Wersja | Data wydania | Kluczowy motyw |
|--------|------------|---------|
| 1,0 | marzec 2012 | Pierwsza stabilna wersja |
| 1.1 | maj 2013 | Wydajność, wykrywacz wyścigów |
| 1.3 | czerwiec 2014 | Odpytywanie sieci, krypto/tls |
| 1,4 | grudzień 2014 | Bootstrap z Go (samodzielny hosting) |
| 1,5 | sierpień 2015 | **Wspólne GC**, bariery zapisu |
| 1,7 | sierpień 2016 |  Pakiet `context`, podtesty`testing`|
| 1,8 | luty 2017 | `http.Server.Shutdown`, wtyczki |
| 1,9 | sierpień 2017 | Aliasy typów, równoległe`make`|
| 1.10 | luty 2018 |  Pula połączeń`database/sql`|
| 1.11 | sierpień 2018 | **Moduły Go**,`go mod`|
| 1.12 | luty 2019 | TLS 1.3, wersjonowanie modułów |
| 1.13 | wrzesień 2019 | `errors.Is/As`, literały liczbowe`0b`,`0o`|
| 1.14 | luty 2020 | **Nakładające się wejścia/wyjścia w systemie Windows**, wywłaszczanie goroutine |
| 1,15 | sierpień 2020 |  Reset`time.Ticker`/ `Timer`, moduł proxy |
| 1.16 | luty 2021 |  Pakiet `embed`,`io/fs`, domyślnie obsługujący moduły |
| 1,17 | sierpień 2021 | Konwersja plasterka na tablicę,`unsafe.Slice`|
| 1.18 | marzec 2022 | **Ogólne**, fuzzing, obszary robocze |
| 1.19 | sierpień 2022 | Komentarze do dokumentu, rewizja modelu pamięci |
| 1,20 | luty 2023 | `errors.Join`, optymalizacja oparta na profilu |
| 1.21 | sierpień 2023 | **`slog`**, wbudowane `min/max`,`maps/slices`|
| 1,22 | luty 2024 | Zakres na liczbach całkowitych, ulepszone routing |
| 1,23 | sierpień 2024 | Pakiet iteratora (`iter`), zmiany timera |
| 1,24 | luty 2025 |  Pakiet `weak`, ulepszone mapy |
## Główne kamienie milowe
### Początek (2009–2012)
- **2009**: Go ogłoszone przez Google (Robert Griesemer, Rob Pike, Ken Thompson)
- **2012**: **Go 1.0** — „Obietnica kompatybilności z Go 1”
### Wydajność i oprzyrządowanie (2012–2018)
- **1.1**: poprawa wydajności o ponad 30%; wykrywacz wyścigów
- **1,5**: Współbieżny moduł zbierający elementy bezużyteczne (spadek pauz GC z milisekund do mikrosekund)
- **1.5**: Uruchomiony kompilator Go — napisany w Go (nie więcej C)
- **1.7**: Pakiet`context`staje się standardem
### Moduły i ekosystem (2018–2021)
- **1.11**: **Moduły Go** — oficjalne zarządzanie zależnościami
- **1.13**:`errors.Is/As`— zawijanie błędów staje się idiomatyczne
- **1.16**: Pakiet`embed`— osadzaj pliki w czasie kompilacji
### Nowoczesne Go (od 2022 r. – obecnie)
- **1.18**: **Generics** — parametry typu z ograniczeniami
- **1.21**:`slog`— logowanie strukturalne w stdlib;  Wbudowane `min/max`
- **1,22**: Zakres wartości całkowitych (`for i := range 10`)
- **1.23**: Pakiet iteratora — leniwa ocena w stdlib
## Podróż po lekach generycznych
```
2010: "Go doesn't need generics" (early stance)
2016: Go generics proposal discussions begin
2018: Type parameters design draft published
2020: Go 2 generics proposal (draft designs)
2022: Go 1.18 — generics land! Type parameters, constraints
2023: Generic code patterns emerge (slices, maps packages)
2024: Community adapts — generic data structures, algorithms
```

## Filozofia obsługi błędów
```
1.0:     Explicit error returns — "errors are values"
1.13:    Error wrapping with %w — "inspect and unwrap"
1.20:    errors.Join — multiple errors
Future:  go2 proposal for try/handle (not yet adopted)
```

## Ewolucja współbieżności
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

## Obietnica zgodności Go
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

## Rozwój ekosystemu
```
2012: Go 1.0 — basic stdlib, no package manager
2014: dep (early dependency management experiments)
2018: Go modules — official solution
2019: Go used by Uber, Twitch, Dropbox, Cloudflare
2022: Generics — opens new library design patterns
2023: Go in Kubernetes, Docker, Terraform, Hugo
2025: Top 10 most used language; cloud-native standard
```

## Ewolucja wydajności
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
