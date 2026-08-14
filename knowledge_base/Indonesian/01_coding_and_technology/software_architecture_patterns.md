---
# Metadata
title: "Software Architecture Patterns"
description: "Monolith, microservices, event-driven, DDD, caching, SOLID"
category: "Coding and Technology"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "Nepoznato-Dev"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.0"
    date: "2026-08-05"
    author: "Nepoznato-Dev"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-05"
review_date: "2027-02-05"
reviewed_by: "Coding & Technology Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [software, architecture, patterns, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "9 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Pola Arsitektur Perangkat Lunak
Arsitektur adalah serangkaian keputusan struktural tentang bagaimana suatu sistem diorganisasikan — komponen apa yang dimilikinya, bagaimana mereka berkomunikasi, dan di mana letak tanggung jawabnya. Arsitektur yang baik membuat sistem mudah dipahami, dimodifikasi, dan diskalakan. Arsitektur yang buruk membuat setiap perubahan menjadi sebuah perjuangan. File ini mencakup pola-pola utama, kapan menggunakan masing-masing pola, dan trade-off yang terlibat.
---

## Monolit vs Layanan Mikro
Ini adalah keputusan arsitektur paling mendasar, dan patut dilakukan dengan benar.
| Aspek | Monolit | Layanan mikro |
|--------|----------|---------------|
| **Struktur** | Unit tunggal yang dapat diterapkan | Banyak layanan kecil yang dapat diterapkan secara mandiri |
| **Data** | Basis data bersama | Setiap layanan memiliki datanya |
| **Komunikasi** | Panggilan fungsi dalam proses | Panggilan jaringan (HTTP, gRPC, perpesanan) |
| **Penskalaan** | Skala seluruh aplikasi | Skalakan layanan individual |
| **Penerapan** | Siklus rilis tunggal | Penerapan independen |
| **Kompleksitas** | Lebih mudah untuk dikembangkan pada awalnya | Kompleksitas operasional (jaringan, pemantauan) |
| **Terbaik Untuk** | Tim kecil, produk tahap awal | Tim besar, domain kompleks, skala tinggi |
### Kapan Memulai dengan Monolit
Sebagian besar aplikasi harus dimulai sebagai monolit. Lebih mudah untuk membangun, menguji, menerapkan, dan melakukan debug. Anda selalu dapat mengekstrak layanan nanti ketika Anda memiliki gambaran yang lebih jelas tentang batas domain Anda. Ini kadang-kadang disebut "monolit modular" — monolit dengan batas internal bersih yang nantinya memudahkan ekstraksi.
### Kapan Harus Menggunakan Layanan Mikro
Pertimbangkan layanan mikro ketika:
- Jumlah tim cukup besar sehingga koordinasi menjadi hambatan.
- Bagian sistem yang berbeda memiliki persyaratan penskalaan yang sangat berbeda.
- Anda memerlukan penerapan komponen secara independen.
- Domain Anda memiliki konteks yang jelas (lihat DDD di bawah).
---

## Arsitektur Berlapis (N-Tier)
Pola arsitektur yang paling umum. Kode disusun dalam beberapa lapisan, masing-masing dengan tanggung jawab tertentu.
```
â”Œ─────────────────────────┐
│   Presentation Layer    │  ← UI, controllers, API endpoints
├─────────────────────────┤
│   Application Layer     │  ← Use cases, orchestration
├─────────────────────────┤
│   Domain Layer          │  ← Business logic, entities
├─────────────────────────┤
│   Infrastructure Layer  │  ← Database, external services, file I/O
└─────────────────────────┘
```

| Lapisan | Tanggung jawab | Aturan |
|-------|---------------|------|
| **Presentasi** | Menangani permintaan pengguna/HTTP | Hanya dapat memanggil lapisan Aplikasi |
| **Aplikasi** | Mengatur kasus penggunaan | Dapat memanggil lapisan Domain |
| **Domain** | Logika bisnis inti | Tidak boleh bergantung pada lapisan lain |
| **Infrastruktur** | Masalah teknis | Mengimplementasikan antarmuka yang ditentukan dalam Domain |
**Aturan utama**: dependensi mengarah ke dalam. Lapisan Domain tidak mengetahui tentang database atau kerangka web.
---

## Arsitektur Berbasis Peristiwa
Komponen berkomunikasi dengan memancarkan dan bereaksi terhadap **peristiwa** — hal-hal yang telah terjadi.
| Pola | Deskripsi |
|---------|-------------|
| **Pemberitahuan Acara** | Layanan A mengeluarkan "OrderPlaced"; jasa B, C, D bereaksi |
| **Sumber Acara** | Simpan semua perubahan status sebagai rangkaian peristiwa (bukan hanya status saat ini) |
| **CQRS** | Pisahkan model baca (kueri) dari model tulis (perintah) |
### Sumber Acara
Daripada menyimpan "keadaan saat ini" dalam database, simpan setiap perubahan keadaan sebagai sebuah peristiwa:
```
OrderCreated(order_id=123, total=$50)
OrderPaid(order_id=123, payment_id=456)
OrderShipped(order_id=123, tracking=ABC)
```

Manfaat: jejak audit yang lengkap, kemampuan untuk merekonstruksi keadaan masa lalu, memisahkan konsumen. Tantangan: evolusi skema peristiwa, konsistensi akhir, kompleksitas proses debug.
### CQRS (Pemisahan Tanggung Jawab Permintaan Perintah)
| Sisi | Tujuan | Basis Data |
|------|---------|----------|
| **Perintah (Tulis)** | Menangani mutasi; menegakkan aturan bisnis | Dioptimalkan untuk penulisan (dinormalisasi) |
| **Kueri (Baca)** | Melayani permintaan baca | Dioptimalkan untuk dibaca (dinormalisasi) |
CQRS berpasangan secara alami dengan Sumber Peristiwa: peristiwa dari sisi tulis diproyeksikan ke tampilan yang dioptimalkan untuk dibaca.
---

## Antrean Pesan dan Broker Acara
Ketika layanan perlu berkomunikasi secara asinkron, antrian pesan adalah tulang punggungnya.
| Alat | Ketik | Terbaik Untuk |
|------|------|----------|
| **Apache Kafka** | Log peristiwa terdistribusi | Streaming acara dengan throughput tinggi, sumber acara |
| **KelinciMQ** | Broker pesan dengan perutean | Antrian tugas, pola perutean yang rumit |
| **AWS SQS** | Antrian terkelola | Antrean sederhana dan asli AWS |
| **AWS SNS** | Pemberitahuan pub/sub | Disebarkan ke banyak pelanggan |
| **Google Pub/Sub** | Pub/sub yang dikelola | Streaming acara asli GCP |
| **Aliran Redis** | Aliran ringan | Pencatatan peristiwa sederhana, kasus penggunaan cache |
### Pola Pesan
| Pola | Deskripsi |
|---------|-------------|
| **Titik-ke-Titik** | Satu produsen, satu konsumen per pesan |
| **Terbitkan/Berlangganan** | Satu produser, banyak pelanggan |
| **Permintaan/Balasan** | Gaya sinkron melalui transportasi async |
| **Antrian Surat Mati** | Pesan yang gagal diproses akan dimasukkan ke antrian terpisah untuk diperiksa |
---

## Desain Berbasis Domain (DDD)
DDD adalah pendekatan strategis terhadap desain perangkat lunak yang memusatkan kode pada konsep bisnis daripada masalah teknis.
### Konsep Utama
| Konsep | Deskripsi |
|---------|-------------|
| **Konteks Terbatas** | Batas di mana model domain konsisten (misalnya, "Pemesanan", "Pengiriman", "Penagihan") |
| **Bahasa yang Ada di Mana-Mana** | Kosakata bersama antara pengembang dan pakar domain |
| **Agregat** | Cluster entitas terkait diperlakukan sebagai satu unit untuk perubahan data |
| **Entitas** | Objek dengan identitas (misalnya, Pengguna dengan user_id) |
| **Objek Nilai** | Benda tanpa identitas; ditentukan oleh atributnya (misalnya, Uang, Alamat) |
| **Acara Domain** | Sesuatu yang terjadi di domain (mis., OrderPlaced) |
| **Lapisan Anti Korupsi** | Lapisan terjemahan antara domain Anda dan sistem eksternal |
### Saat DDD Membantu
DDD paling berharga ketika domain bisnisnya kompleks — misalnya e-commerce, logistik, jasa keuangan, layanan kesehatan. Jika domain Anda sederhana (blog, aplikasi rencana), DDD berlebihan.
---

## Strategi Caching
Caching adalah salah satu cara paling efektif untuk meningkatkan kinerja, namun hal ini menimbulkan kompleksitas seputar konsistensi.
| Strategi | Deskripsi | Pertukaran |
|----------|-------------|-----------|
| **Selain Cache** | Aplikasi memeriksa cache terlebih dahulu; memuat dari DB saat miss | Sederhana; konsistensi akhirnya |
| **Tulis Melalui** | Menulis ke cache dan DB secara bersamaan | Konsisten; menulis lebih lambat |
| **Tulis di Belakang** | Menulis ke cache; async tulis ke DB | Menulis cepat; risiko kehilangan data |
| **Baca-Melalui** | Cache dimuat dari DB jika hilang secara transparan | Lebih sederhana dari selain cache |
### Apa yang harus di-Cache
| Lapisan | Apa | Alat |
|-------|------|-------|
| **CDN** | Aset statis, respons API | CloudFront, Cloudflare |
| **Aplikasi** | Hasil yang dihitung, data sesi | Redis, Memcache |
| **Basis Data** | Hasil kueri, baris yang sering diakses | Cache kueri, tampilan terwujud |
**Pembatalan cache** terkenal sulit. Strategi umum: TTL (time-to-live), pembatalan validasi berdasarkan peristiwa (menghapus cache pada perubahan data), dan penggusuran LRU (paling jarang digunakan).
---

## Pola Desain
### Prinsip PADAT
| Prinsip | Apa Artinya |
|-----------|--------------|
| **S** — Tanggung Jawab Tunggal | Sebuah kelas harus mempunyai satu alasan untuk mengubah |
| **O** — Buka/Tutup | Terbuka untuk perpanjangan, ditutup untuk modifikasi |
| **L** — Pergantian Liskov | Subtipe harus dapat diganti dengan tipe dasarnya |
| **I** — Pemisahan Antarmuka | Banyak antarmuka spesifik > satu antarmuka tujuan umum |
| **D** — Pembalikan Ketergantungan | Bergantung pada abstraksi, bukan konkresi |
### Pola Umum
| Pola | Maksud | Contoh |
|---------|--------|---------|
| **Lajang** | Pastikan suatu kelas hanya memiliki satu instance | Kumpulan koneksi database |
| **Pabrik** | Buat objek tanpa menentukan kelas pastinya | `UserFactory.create(type="admin")`|
| **Pengamat** | Beritahu tanggungan ketika keadaan berubah | Pendengar acara, pub/sub |
| **Strategi** | Tukar algoritma saat runtime | Strategi Pembayaran: Kartu Kredit, PayPal, Crypto |
| **Repositori** | Akses data abstrak di balik antarmuka yang bersih | `UserRepository.find_by_id(123)`|
| **Dekorator** | Tambahkan perilaku secara dinamis | Mencatat dekorator di sekitar layanan |
| **Adaptor** | Membuat antarmuka yang tidak kompatibel bekerja sama | Adaptor API lama |
---

## Memilih Arsitektur yang Tepat
Tidak ada arsitektur yang “terbaik” secara universal. Pilihan yang tepat bergantung pada:
| Faktor | Pilih Monolit Saat... | Pilih Layanan Mikro Saat... |
|--------|------------------------|------------------------------|
| **Ukuran tim** | < 10 developers | >20 pengembang, banyak tim |
| **Kompleksitas domain** | Sederhana atau dipahami dengan baik | Konteks yang kompleks dan banyak batasnya |
| **Persyaratan skala** | Kebutuhan penskalaan yang seragam | Komponen yang berbeda memerlukan skala yang berbeda |
| **Irama penerapan** | Siklus rilis tunggal | Diperlukan penerapan independen |
| **Keberagaman teknologi** | Satu tumpukan baik-baik saja | Layanan yang berbeda memerlukan teknologi yang berbeda |
**Saran praktis**: mulailah dengan monolit modular. Ekstrak layanan hanya jika Anda memiliki kebutuhan yang jelas dan batasan domain yang jelas. Layanan mikro yang prematur adalah salah satu kesalahan arsitektur paling umum di industri.