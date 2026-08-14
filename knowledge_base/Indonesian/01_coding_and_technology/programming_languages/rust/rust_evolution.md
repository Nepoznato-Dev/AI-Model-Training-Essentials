---
# Metadata
title: "Rust — Version History & Evolution"
description: "Comprehensive version history and evolution of Rust from early development to modern Rust."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
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
# Rust — Riwayat Versi & Evolusi
## Garis Waktu
| Versi | Tanggal Rilis | Tema Utama |
|---------|-------------|-----------|
| 0,1 | Januari 2012 | Kompiler pertama (rustc), konkurensi berbasis tugas |
| 0,5 | 2012 | Sistem tipe berbasis sifat mulai terbentuk |
| 0,6 | 2012 | Penghapusan kotak terkelola`@`|
| 0,7 | 2013 | `@`dihapus,`~`untuk kotak milik |
| 0,8 | 2013 | Anotasi seumur hidup,`&mut`|
| 0,9 | Januari 2014 | Pembersihan akhir pra-1.0 |
| 0,10 | Februari 2014 | Rilis terakhir sebelum 1.0 |
| 0,11 | April 2014 | `Box<T>`menggantikan`~T`|
| 0,12 | Mei 2014 |  Penulisan ulang modul`io`dimulai |
| 1.0 | 15 Mei 2015 | **Rilis stabil** — "Rust 1.0" |
| 1.10 | Agustus 2016 |  Propagasi kesalahan`?`(sebagai`try!`→`?`) |
| 1.15 | Februari 2017 | Rust Pertama di stabil dengan persiapan`impl Trait`|
| 1.18 | Juni 2017 | `pub(crate)`, kompilasi tambahan |
| 1.20 | Oktober 2017 | Konstanta terkait |
| 1.26 | Mei 2018 | `impl Trait`dalam posisi argumen/kembali |
| 1.28 | September 2018 | Pengalokasi global |
| 1.31 | Desember 2018 | **Rust Edisi 2018** — modul,`dyn Trait`|
| 1.34 | April 2019 | Registri alternatif |
| 1.39 | November 2019 | `async/await`dalam kondisi stabil |
| 1.44 | Juli 2020 | Peningkatan diagnostik |
| 1.51 | April 2021 | `const`obat generik (MVP) |
| 1.56 | Oktober 2021 | **Rust Edisi 2021** — penutupan, IntoIterator |
| 1.59 | Februari 2022 | Perakitan sebaris |
| 1.62 | Juni 2022 | `#[default]`untuk enum |
| 1.65 | Desember 2022 | `let else`|
| 1.68 | Maret 2023 |  `#[ffi_pure]`, pengoptimalan yang dipandu profil |
| 1,70 | Juni 2023 | Dependensi`crates.io`terisolasi |
| 1.74 | November 2023 | Mode offline kargo |
| 1.76 | Februari 2024 | **Edisi Rust 2024** — Blok `gen`,`unsafe extern`|
| 1.79 | Juni 2024 | `LazyCell`,`LazyLock`|
| 1.82 | Oktober 2024 | `unsafe`di blok`extern`diperlukan |
| 1,85 | Februari 2025 | Edisi Rust 2024 stabil |
## Tonggak Penting
### Pra-1.0 (2010–2015)
- **2010**: Proyek sampingan Graydon Hoare di Mozilla mendapatkan daya tarik
- **2012**: Kompiler publik pertama; sistem tipe mengalami desain ulang besar-besaran
- **2013**: Model kepemilikan terkristalisasi;  Kotak`@`dihapus
- **2014**: Proses Rust RFC diformalkan; komunitas tumbuh
- **2015**: **1.0** — jaminan stabilitas; "abstraksi tanpa biaya"
### Tahun Pertumbuhan (2015–2019)
- **2015**: Cargo menjadi pengelola paket standar
- **2018**: **Rust 2018 Edition** — perombakan sistem modul,`dyn Trait`,`impl Trait`
- **2019**:`async/await`berada dalam kondisi stabil — ekosistem asinkron dimulai
### Kedewasaan (2020–sekarang)
- **2021**: **Rust 2021 Edition** — membedakan bidang dalam penutupan,`IntoIterator`untuk array
- **2024**: **Rust 2024 Edition** — Blok `gen`, persyaratan `unsafe extern`
- **2025**: Karat di kernel Linux, Android, Windows, infrastruktur AWS
## Sistem Edisi
```
Rust 2015:  The baseline (1.0)
Rust 2018:  Module system, async/await prep, dyn Trait
Rust 2021:  Closure changes, IntoIterator, panic macros
Rust 2024:  gen blocks, unsafe extern, tail expressions

Key principle: Editions are opt-in, never break existing code.
Old editions always compile. New editions add features.
```

## Evolusi Kepemilikan
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

## Evolusi Asinkron
```
2018: futures 0.1 — early async with manual polling
2019: async/await syntax (Rust 1.39)
2019: tokio 0.2 — async runtime
2020: async-std — std-like async API
2021: tokio 1.0 — stable async runtime
2023: async fn in traits (Rust 1.75)
2024: async closures, improved Send bounds
```

## Pertumbuhan Ekosistem
```
2015: crates.io launches (~2,000 crates)
2018: Rust most loved language (Stack Overflow survey)
2019: 30,000 crates on crates.io
2021: Most admired language (6th consecutive year)
2023: 130,000+ crates
2025: Used in Linux kernel, Android, Windows, Chromium, AWS, Cloudflare, Discord, Dropbox
```

## RFC Utama
| RFC | Tahun | Fitur |
|------|------|---------|
| 25 | 2013 | Pencocokan pola |
| 153 | 2014 |  Tipe`Result`|
| 217 | 2014 | `?`(coba) operator |
| 460 | 2016 | `?`menggantikan`try!`|
| 1210 | 2015 | `impl Trait`|
| 1414 | 2016 | Karat edisi 2018 |
| 2394 | 2018 | `async/await`|
| 2515 | 2018 | `const`generik |
| 3013 | 2020 | Memeriksa kompilasi bersyarat |
| 3517 | 2023 |  Blok`gen`|