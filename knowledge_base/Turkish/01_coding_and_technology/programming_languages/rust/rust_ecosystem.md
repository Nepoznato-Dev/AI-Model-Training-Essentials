---
# Metadata
title: "Rust — Ecosystem & Tooling Guide"
description: "Comprehensive guide to the Rust ecosystem including package management, build tools, testing, frameworks, and deployment."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial ecosystem guide"
tags: [rust, ecosystem, tooling, cargo, testing, web, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "20 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

# Rust — Ekosistem ve Takım İşleme Kılavuzu
Bu kılavuz Rust ekosistemindeki temel araçları, çerçeveleri ve altyapıyı kapsar.
---

## Paket Yönetimi ve Oluşturma
| Araç | Amaç |
|------|------------|
| **Kargo** | Paket yöneticisi, derleme sistemi, test çalıştırıcısı |
| **crates.io** | Resmi paket kaydı |
| **paslanma** | Takım zinciri yükleyicisi ve yöneticisi |
| **kargo düzenleme** | Bağımlılık ekleme/kaldırma/yükseltme |
| **kargo-izle** | Dosya değişikliklerine göre yeniden oluşturma |
| **kargo denetimi** | Güvenlik açığı denetleyicisi |
| **kargo-kırpılmış** | Linter (yerleşik) |
| **kargo-fmt** | Kod biçimlendirici (rustfmt) |
```bash
cargo new project               # new binary project
cargo new --lib project         # new library
cargo build                     # debug build
cargo build --release           # optimized build
cargo run                       # build and run
cargo test                      # run tests
cargo clippy                    # lint
cargo fmt                       # format
cargo doc --open                # generate and view docs
```

---

## Test etme
| Araç | Amaç |
|------|------------|
| **kargo testi** | Yerleşik ünite + entegrasyon testleri |
| **kriter** | Karşılaştırma çerçevesi |
| **protesto** | Mülkiyet bazlı testler |
| **sahtekarlık** | Alaycı çerçeve |
| **tokio::test** | Eşzamansız test desteği |
| **instagram** | Anlık görüntü testi |
```rust
#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_addition() {
        assert_eq!(2 + 2, 4);
    }

    #[test]
    #[should_panic(expected = "overflow")]
    fn test_overflow() {
        panic!("overflow!");
    }
}
```

---

## Web Çerçeveleri
| Çerçeve | Tür | En İyisi |
|-----------|----------|----------|
| **Actix-web** | Performans | Yüksek verimli API'ler |
| **Axum** | Tokyo yerlisi | Modern eşzamansız web |
| **Roket** | Ergonomik | Geliştirici deneyimi |
| **Çarpma** | Fonksiyonel | Şekillendirilebilir filtreler |
| **Gelgit** | Basit | Minimum API'ler |
---

## Eşzamansız Çalışma Zamanı
| Çalışma zamanı | Özellikler |
|-----------|----------|
| **Tokio** | Baskın, tam özellikli |
| **eşzamansız-std** | std benzeri eşzamansız |
| **smol** | Hafif |
---

## Veritabanı
| Sandık | Veritabanı |
|----------|----------|
| **Dizel** | PostgreSQL, MySQL, SQLite (ORM) |
| **SQLx** | PostgreSQL, MySQL, SQLite (zaman uyumsuz, derleme zamanı kontrol edildi) |
| **DenizORM** | Zaman uyumsuz ORM, dinamik sorgular |
| **Kırmızı** | Gömülü anahtar/değer çifti |
| **Kızak** | Gömülü anahtar/değer çifti |
---

## Serileştirme
| Sandık | Amaç |
|----------|-----------|
| **serde** | Serileştirme çerçevesi |
| **serde_json** | JSON |
| **serde_yaml** | YAML |
| **toml** | TOML (Kargo bunu kullanır) |
| **bin kodu** | İkili |
| **prost** | Protokol Tamponları |
---

## CLI Araçları
| Sandık | Amaç |
|----------|-----------|
| **alkış** | Bağımsız değişken ayrıştırma |
| **ratatui** | Terminal Kullanıcı Arayüzü |
| **çapraz terim** | Çapraz platform terminali |
| **gösterge** | İlerleme çubukları |
| **diyalogcu** | Kullanıcı istemleri |
| **konsol** | Terminal stili |
---

## Gömülü ve Sistemler
| Sandık | Amaç |
|----------|-----------|
| **gömülü-hal** | Donanım soyutlaması |
| **no_std** | Çıplak metal programlama |
| **wasm-bingen** | WebAssembly birlikte çalışma |
| **tonik** | gRPC |
---

## IDE'ler ve Düzenleyiciler
| IDE | Güçlü Yönler |
|-----|-----------|
| **VS Kodu + pas analiz cihazı** | Mükemmel LSP desteği |
| **CLion + Rust eklentisi** | Eksiksiz JetBrains deneyimi |
| **Neovim + pas analiz cihazı** | Terminal tabanlı |
| **Helis** | Rust'ta yerleşik editör |
---

## Dağıtım
| Yöntem | Araç |
|----------|------|
| **Statik ikili** | `cargo build --release`(tek ikili!) |
| **Çapraz derleme** | `cross`(Docker tabanlı) |
| **Konteynerler** | Docker, dağıtımsız |
| **Web Montajı** | `wasm-pack`|
| **müslü** | Linux için statik bağlantı |
---

## Özet
Rust'un ekosistemi uyumlu ve yüksek kaliteli olup Cargo merkezlidir. Standart yığın şudur: Her şey için **Cargo** (derleme, test etme, yayınlama), async için **Tokio**, web için **Axum** veya **Actix-web**, serileştirme için **serde**, veritabanları için **SQLx** ve CLI'ler için **clap**. Rust'un harika özelliği, çalışma zamanı bağımlılığı olmayan tek bir statik ikili dosya olarak dağıtılmasıdır. Ekosistem, kolaylıktan ziyade doğruluk ve performansa öncelik verir.