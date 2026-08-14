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
# Swift — Riwayat Versi & Evolusi
## Garis Waktu
| Versi | Tahun | Tema Utama |
|---------|------|-----------|
| 1.0 | 2014 | Rilis awal (Chris Lattner, Apple) |
| 1.1 | 2014 | Inisialisasi gagal,`@autoclosure`|
| 1.2 | 2015 |  Tipe`as?`/`as!`, `Set`, perbandingan tupel |
| 2.0 | 2015 | Ekstensi protokol,`defer`,`guard`,`errortype`|
| 2.1 | 2015 | `try?`, interpolasi string dalam literal |
| 2.2 | 2016 | `#selector`,`defer`, tupel kembali |
| 3.0 | 2016 | **Mayor**: Desain ulang API — konvensi penamaan,`@discardableResult`|
| 4.0 | 2017 | `Codable`,`String`penulisan ulang, literal multi-baris |
| 5.0 | 2019 | **Mayor**: Persiapan `async/await`, stabilitas ABI, tipe`Result`|
| 5.1 | 2019 | `some`(tipe buram), pembungkus properti,`@resultBuilder`|
| 5.2 | 2020 | Panggilan sebagai fungsi,`KeyPath`sebagai fungsi |
| 5.3 | 2020 |  `@MainActor`, beberapa penutupan akhir, peningkatan`enum`|
| 5.4 | 2021 | Beberapa parameter variadik, peningkatan`@resultBuilder`|
| 5.5 | 2021 | **`async/await`**, aktor,`Sendable`|
| 5.6 | 2022 |  Kata kunci `any`,`Clock`,`Duration`|
| 5.7 | 2022 |  Singkatan `if let`, literal `Regex`, protokol`Clock`|
| 5.8 | 2023 | Penerapan kembali fungsi, peningkatan`Clock`|
| 5.9 | 2023 | **Makro**, paket parameter,`consume`/`discard`|
| 5.10 | 2024 | Pemeriksaan konkurensi lengkap, keamanan data race yang ketat |
| 6.0 | 2024 | **Mayor**: Konkurensi ketat secara default, lemparan yang diketik |
| 6.1 | 2025 | (diharapkan) Penyempurnaan konkurensi lebih lanjut |
## Tonggak Penting
### Swift 1.x — Kelahiran (2014–2015)
- **2014**: Diumumkan di WWDC; menggantikan Objective-C untuk pengembangan Apple
- **1.0**: Opsional, generik, penutupan, inferensi tipe, protokol
- **1.2**: Pola`as?`/ `as!`, tipe `Set`
### Swift 2.x — Penanganan Kesalahan (2015–2016)
- **2.0**: Ekstensi protokol (pemrograman berorientasi protokol),`guard`,`defer`,`do/try/catch`
- **2.1**:`try?`untuk penanganan kesalahan opsional
### Swift 3.x — Penggantian Nama API yang Hebat (2016)
- **3.0**: Desain ulang API besar-besaran — "Penggantian Nama Terpadu Besar"
- Konvensi penamaan:`stringByAppendingString`→`appending`
- Menghapus loop`for`gaya C, operator`++`/ `--`
- Label parameter pertama secara default
### Swift 4.x — Dapat Dikodekan (2017)
- **4.0**: Protokol`Codable`(pengkodean/dekode JSON), penulisan ulang `String`, literal string multi-baris
### Swift 5.x — Stabilitas (2019–2024)
- **5.0**: Stabilitas ABI (aplikasi menjadi lebih kecil), tipe `Result`, string mentah
- **5.1**: Jenis buram (`some View`), pembungkus properti (`@State`,`@Binding`)
- **5.5**: **`async/await`**, aktor, protokol `Sendable`
- **5.9**: Makro (pembuatan kode waktu kompilasi), paket parameter
### Swift 6.x — Keamanan Konkurensi (2024–sekarang)
- **6.0**: Pemeriksaan konkurensi yang ketat secara default, lemparan yang diketik
## Evolusi Konkurensi
```
1.0:  GCD (Grand Central Dispatch) — Objective-C pattern
2.0:  Protocol extensions for async patterns
5.5:  async/await, actors, Sendable
5.10: Complete concurrency checking
6.0:  Strict concurrency by default (data race safety)
```

## Ketik Evolusi Sistem
```
1.0:  Optionals, generics, protocols
2.0:  Protocol extensions, protocol composition
4.0:  Codable, associated type constraints
5.1:  Opaque types (some), property wrappers
5.9:  Macros, parameter packs (variadic generics)
6.0:  Typed throws, strict Sendable
```

## Swift di Platform Lain
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

## Proses Evolusi Cepat
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

## Pertumbuhan Ekosistem
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
