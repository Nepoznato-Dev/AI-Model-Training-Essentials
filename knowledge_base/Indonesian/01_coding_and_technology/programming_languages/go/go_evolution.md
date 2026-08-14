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
# Go — Riwayat Versi & Evolusi
## Garis Waktu
| Versi | Tanggal Rilis | Tema Utama |
|---------|-------------|-----------|
| 1.0 | Maret 2012 | Rilis stabil pertama |
| 1.1 | Mei 2013 | Performa, pendeteksi balapan |
| 1.3 | Juni 2014 | Jajak pendapat jaringan, crypto/tls |
| 1.4 | Desember 2014 | Bootstrap dengan Go (hosting mandiri) |
| 1.5 | Agustus 2015 | **GC serentak**, tulis hambatan |
| 1.7 | Agustus 2016 |  Paket `context`, subtes`testing`|
| 1.8 | Februari 2017 |  `http.Server.Shutdown`, plugin |
| 1.9 | Agustus 2017 | Ketik alias, paralel`make`|
| 1.10 | Februari 2018 |  Kumpulan koneksi`database/sql`|
| 1.11 | Agustus 2018 | **Buka modul**,`go mod`|
| 1.12 | Februari 2019 | TLS 1.3, pembuatan versi modul |
| 1.13 | September 2019 | `errors.Is/As`, angka literal`0b`,`0o`|
| 1.14 | Februari 2020 | **I/O yang tumpang tindih di Windows**, preemption goroutine |
| 1.15 | Agustus 2020 |  Reset`time.Ticker`/ `Timer`, proksi modul |
| 1.16 | Februari 2021 |  Paket `embed`,`io/fs`, sadar modul secara default |
| 1.17 | Agustus 2021 | Konversi irisan ke array,`unsafe.Slice`|
| 1.18 | Maret 2022 | **Generik**, fuzzing, ruang kerja |
| 1.19 | Agustus 2022 | Komentar dokumen, revisi model memori |
| 1.20 | Februari 2023 |  `errors.Join`, pengoptimalan yang dipandu profil |
| 1.21 | Agustus 2023 | **`slog`**,`min/max`bawaan,`maps/slices`|
| 1.22 | Februari 2024 | Rentang bilangan bulat, perutean yang ditingkatkan |
| 1.23 | Agustus 2024 | Paket Iterator (`iter`), pengatur waktu berubah |
| 1.24 | Februari 2025 |  Paket `weak`, peta yang ditingkatkan |
## Tonggak Penting
### Awal (2009–2012)
- **2009**: Go diumumkan oleh Google (Robert Griesemer, Rob Pike, Ken Thompson)
- **2012**: **Go 1.0** — "Janji kompatibilitas Go 1"
### Performa & Peralatan (2012–2018)
- **1.1**: 30%+ peningkatan kinerja; detektor balapan
- **1,5**: Pengumpul sampah serentak (jeda GC turun dari milidetik ke mikrodetik)
- **1.5**: Kompiler Go di-bootstrap — ditulis dalam Go (tidak ada lagi C)
- **1.7**: Paket`context`menjadi standar
### Modul & Ekosistem (2018–2021)
- **1.11**: **Modul Go** — manajemen ketergantungan resmi
- **1.13**:`errors.Is/As`— pembungkusan kesalahan menjadi idiomatis
- **1.16**: Paket`embed`— menyematkan file pada waktu kompilasi
### Modern Go (2022–sekarang)
- **1.18**: **Generik** — mengetikkan parameter dengan batasan
- **1.21**:`slog`— logging terstruktur di stdlib; `min/max`bawaan
- **1.22**: Rentang bilangan bulat (`for i := range 10`)
- **1.23**: Paket Iterator — evaluasi malas di stdlib
## Perjalanan Generik
```
2010: "Go doesn't need generics" (early stance)
2016: Go generics proposal discussions begin
2018: Type parameters design draft published
2020: Go 2 generics proposal (draft designs)
2022: Go 1.18 — generics land! Type parameters, constraints
2023: Generic code patterns emerge (slices, maps packages)
2024: Community adapts — generic data structures, algorithms
```

## Filosofi Penanganan Kesalahan
```
1.0:     Explicit error returns — "errors are values"
1.13:    Error wrapping with %w — "inspect and unwrap"
1.20:    errors.Join — multiple errors
Future:  go2 proposal for try/handle (not yet adopted)
```

## Evolusi Konkurensi
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

## Janji Kompatibilitas Go
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

## Pertumbuhan Ekosistem
```
2012: Go 1.0 — basic stdlib, no package manager
2014: dep (early dependency management experiments)
2018: Go modules — official solution
2019: Go used by Uber, Twitch, Dropbox, Cloudflare
2022: Generics — opens new library design patterns
2023: Go in Kubernetes, Docker, Terraform, Hugo
2025: Top 10 most used language; cloud-native standard
```

## Evolusi Kinerja
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
