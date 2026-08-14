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
# Rust — Sürüm Geçmişi ve Gelişimi
## Zaman Çizelgesi
| Sürüm | Çıkış Tarihi | Anahtar Tema |
|-----------|---------------|-----------|
| 0.1 | Ocak 2012 | İlk derleyici (rustc), görev tabanlı eşzamanlılık |
| 0,5 | 2012 | Özellik tabanlı tip sistemi şekilleniyor |
| 0.6 | 2012 |`@`yönetilen kutuların kaldırılması |
| 0.7 | 2013 | `@`kaldırıldı, sahip olunan kutular için`~`|
| 0.8 | 2013 | Ömür boyu ek açıklamalar,`&mut`|
| 0.9 | Ocak 2014 | 1.0 öncesi son temizlik |
| 0.10 | Şubat 2014 | 1.0 öncesi son sürüm |
| 0.11 | Nisan 2014 |  `Box<T>`, `~T`'nin yerini alıyor |
| 0.12 | Mayıs 2014 | `io`modülünün yeniden yazılması başlıyor |
| 1.0 | 15 Mayıs 2015 | **Kararlı sürüm** — "Rust 1.0" |
| 1.10 | Ağustos 2016 | `?`hata yayılımı (`try!` →`?`olarak) |
| 1.15 | Şubat 2017 |`impl Trait`hazırlığıyla ilk Rust stabil hale geldi |
| 1.18 | Haziran 2017 |  `pub(crate)`, artımlı derleme |
| 1.20 | Ekim 2017 | İlişkili sabitler |
| 1.26 | Mayıs 2018 | `impl Trait`bağımsız değişken/dönüş konumunda |
| 1.28 | Eylül 2018 | Küresel tahsisçiler |
| 1.31 | Aralık 2018 | **Rust 2018 Sürümü** — modüller,`dyn Trait`|
| 1.34 | Nis 2019 | Alternatif kayıtlar |
| 1.39 | Kasım 2019 | `async/await`stabil |
| 1.44 | Temmuz 2020 | Tanılama iyileştirmeleri |
| 1.51 | Nis 2021 | `const`jenerikler (MVP) |
| 1.56 | Ekim 2021 | **Rust 2021 Sürümü** — kapanışlar, IntoIterator |
| 1.59 | Şubat 2022 | Hat içi montaj |
| 1.62 | Haziran 2022 |  numaralandırmalar için`#[default]`|
| 1.65 | Aralık 2022 | `let else`|
| 1.68 | Mart 2023 |  `#[ffi_pure]`, profil kılavuzlu optimizasyon |
| 1.70 | Haziran 2023 | Yalıtılmış`crates.io`bağımlılıkları |
| 1.74 | Kasım 2023 | Kargo çevrimdışı modu |
| 1.76 | Şubat 2024 | **Rust 2024 Sürümü** —`gen`blokları,`unsafe extern`|
| 1.79 | Haziran 2024 | `LazyCell`,`LazyLock`|
| 1.82 | Ekim 2024 | `extern`bloklarında`unsafe`gerekli |
| 1.85 | Şubat 2025 | Rust 2024 sürümü stabilize edildi |
## Önemli Kilometre Taşları
### 1.0 Öncesi (2010–2015)
- **2010**: Graydon Hoare'nin Mozilla'daki yan projesi ilgi görüyor
- **2012**: İlk halka açık derleyici; Tip sistemi büyük bir yeniden tasarıma tabi tutuluyor
- **2013**: Mülkiyet modeli netleşiyor; `@`kutuları kaldırıldı
- **2014**: Rust RFC süreci resmileştirildi; topluluk büyüyor
- **2015**: **1,0** — istikrar garantisi; "sıfır maliyetli soyutlamalar"
### Büyüme Yılları (2015–2019)
- **2015**: Cargo standart paket yöneticisi haline geldi
- **2018**: **Rust 2018 Sürümü** — modül sistemi revizyonu,`dyn Trait`,`impl Trait`
- **2019**:`async/await`kararlı duruma geçiyor - eşzamansız ekosistem başlıyor
### Olgunluk (2020-günümüz)
- **2021**: **Rust 2021 Sürümü** — kapanışlardaki alanların belirsizliğini giderin, diziler için `IntoIterator`
- **2024**: **Rust 2024 Sürümü** —`gen`blokları,`unsafe extern`gereksinimleri
- **2025**: Linux çekirdeğinde, Android, Windows, AWS altyapısında Rust
## Sürüm Sistemi
```
Rust 2015:  The baseline (1.0)
Rust 2018:  Module system, async/await prep, dyn Trait
Rust 2021:  Closure changes, IntoIterator, panic macros
Rust 2024:  gen blocks, unsafe extern, tail expressions

Key principle: Editions are opt-in, never break existing code.
Old editions always compile. New editions add features.
```

## Sahiplik Gelişimi
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

## Eşzamansız Evrim
```
2018: futures 0.1 — early async with manual polling
2019: async/await syntax (Rust 1.39)
2019: tokio 0.2 — async runtime
2020: async-std — std-like async API
2021: tokio 1.0 — stable async runtime
2023: async fn in traits (Rust 1.75)
2024: async closures, improved Send bounds
```

## Ekosistem Büyümesi
```
2015: crates.io launches (~2,000 crates)
2018: Rust most loved language (Stack Overflow survey)
2019: 30,000 crates on crates.io
2021: Most admired language (6th consecutive year)
2023: 130,000+ crates
2025: Used in Linux kernel, Android, Windows, Chromium, AWS, Cloudflare, Discord, Dropbox
```

## Anahtar RFC'ler
| RFC | Yıl | Özellik |
|------|------|-----------|
| 25 | 2013 | Desen eşleştirme |
| 153 | 2014 | `Result`tipi |
| 217 | 2014 | `?`(dene) operatörü |
| 460 | 2016 |  `?`, `try!`'nin yerine geçiyor |
| 1210 | 2015 | `impl Trait`|
| 1414 | 2016 | Rust 2018 baskısı |
| 2394 | 2018 | `async/await`|
| 2515 | 2018 | `const`jenerikler |
| 3013 | 2020 | Koşullu derleme kontrol ediliyor |
| 3517 | 2023 | `gen`blokları |