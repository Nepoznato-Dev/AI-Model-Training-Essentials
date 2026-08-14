<!--
---
# Metadata
title: "Rust — Ecosystem & Tooling Guide"
description: "Comprehensive guide to the Rust ecosystem including package management, build tools, testing, frameworks, and deployment."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
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

-->
# Rust — Panduan Ekosistem & Peralatan
Panduan ini mencakup alat, kerangka kerja, dan infrastruktur penting dalam ekosistem Rust.
---

## Manajemen & Pembuatan Paket
| Alat | Tujuan |
|------|---------|
| **Kargo** | Manajer paket, sistem pembangunan, pelari uji |
| **peti.io** | Registri paket resmi |
| **karat** | Penginstal dan pengelola Toolchain |
| **edit kargo** | Tambahkan/hapus/tingkatkan dependensi |
| **penjaga kargo** | Membangun kembali perubahan file |
| **audit kargo** | Pemeriksa kerentanan keamanan |
| **kargo-clippy** | Linter (bawaan) |
| **kargo-fmt** | Pemformat kode (rustfmt) |
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

## Pengujian
| Alat | Tujuan |
|------|---------|
| **uji kargo** | Unit bawaan + pengujian integrasi |
| **kriteria** | Kerangka pembandingan |
| **protes** | Pengujian berbasis properti |
| **olok-olok** | Kerangka mengejek |
| **tokio::uji** | Dukungan pengujian asinkron |
| **insta** | Pengujian cuplikan |
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

## Kerangka Web
| Kerangka | Ketik | Terbaik Untuk |
|-----------|------|----------|
| **Actix-web** | Kinerja | API throughput tinggi |
| **Aksum** | Tokio-asli | Web asinkron modern |
| **Roket** | Ergonomis | Pengalaman pengembang |
| **Melengkungkan** | Fungsional | Filter yang dapat disusun |
| **Pasang** | Sederhana | API Minimal |
---

## Waktu Proses Asinkron
| Waktu proses | Fitur |
|---------|----------|
| **Tokio** | Dominan, berfitur lengkap |
| **async-std** | asinkron seperti std |
| **smol** | Ringan |
---

## Basis Data
| Peti | Basis Data |
|-------|----------|
| **Diesel** | PostgreSQL, MySQL, SQLite (ORM) |
| **SQLx** | PostgreSQL, MySQL, SQLite (async, waktu kompilasi diperiksa) |
| **ORM Laut** | ORM asinkron, kueri dinamis |
| **Redb** | Nilai kunci tersemat |
| **Kereta luncur** | Nilai kunci tersemat |
---

## Serialisasi
| Peti | Tujuan |
|-------|---------|
| **serde** | Kerangka serialisasi |
| **serde_json** | JSON |
| **serde_yaml** | YAML |
| **tombol** | TOML (Kargo menggunakan ini) |
| **kode bin** | Biner |
| **prost** | Buffer Protokol |
---

## Alat CLI
| Peti | Tujuan |
|-------|---------|
| **tepuk tangan** | Penguraian argumen |
| **ratatui** | Antarmuka Pengguna Terminal |
| **lintas jangka** | Terminal lintas platform |
| **indikatif** | Bilah kemajuan |
| **dialog** | Perintah pengguna |
| **konsol** | Penataan terminal |
---

## Tertanam & Sistem
| Peti | Tujuan |
|-------|---------|
| **hal tertanam** | Abstraksi perangkat keras |
| **tidak_std** | Pemrograman bare-metal |
| **wasm-bindgen** | Interop Majelis Web |
| **tonik** | gRPC |
---

## IDE & Editor
| IDE | Kekuatan |
|-----|-----------|
| **Kode VS + penganalisis karat** | Dukungan LSP yang luar biasa |
| **CLion + Plugin Karat** | Pengalaman JetBrains lengkap |
| **Neovim + penganalisis karat** | Berbasis terminal |
| **Heliks** | Editor asli karat |
---

## Penerapan
| Metode | Alat |
|--------|------|
| **Biner statis** | `cargo build --release`(biner tunggal!) |
| **Kompilasi silang** | `cross`(berbasis Docker) |
| **Wadah** | Docker, tanpa distro |
| **Perakitan Web** | `wasm-pack`|
| **muslus** | Tautan statis untuk Linux |
---

## Ringkasan
Ekosistem Rust kohesif dan berkualitas tinggi, berpusat di sekitar Cargo. Tumpukan standarnya adalah: **Cargo** untuk semuanya (buat, uji, terbitkan), **Tokio** untuk async, **Axum** atau **Actix-web** untuk web, **serde** untuk serialisasi, **SQLx** untuk database, dan **clap** untuk CLI. Fitur mematikan Rust diterapkan sebagai biner statis tunggal tanpa ketergantungan waktu proses. Ekosistem mengutamakan kebenaran dan kinerja dibandingkan kenyamanan.