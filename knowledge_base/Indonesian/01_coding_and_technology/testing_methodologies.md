---
# Metadata
title: "Testing Methodologies"
description: "Unit, integration, E2E, TDD, BDD, test pyramids"
category: "Coding and Technology"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "AI Model Training Team"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.0"
    date: "2026-08-05"
    author: "AI Model Training Team"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-05"
review_date: "2027-02-05"
reviewed_by: "Coding & Technology Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [testing, methodologies, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "10 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Metodologi Pengujian
Pengujian adalah cara Anda mendapatkan keyakinan bahwa kode Anda berfungsi — dan yang lebih penting, bahwa perubahan pada kode tersebut tidak merusak apa yang sudah berfungsi. Pengujian yang baik mendeteksi bug sebelum pengguna melakukannya, mendokumentasikan perilaku yang diharapkan, dan memungkinkan pemfaktoran ulang tanpa rasa takut. File ini mencakup spektrum penuh strategi pengujian, mulai dari pengujian unit hingga pengujian menyeluruh, dan prinsip-prinsip yang membuat pengujian menjadi efektif.
---

## Piramida Pengujian
Piramida pengujian menggambarkan distribusi pengujian yang ideal dalam suatu proyek.
```
        /  E2E  \          ← Few; slow; expensive; test the whole system
       /─────────\
      / Integration\       ← Some; test how components work together
     /───────────────\
    /   Unit Tests    \    ← Many; fast; cheap; test individual functions
   /─────────────────────\
```

| Tingkat | Hitung | Kecepatan | Biaya | Apa yang Diuji |
|-------|-------|-------|------|---------------|
| **Satuan** | Banyak | Cepat (ms) | Rendah | Fungsi individu, kelas, metode |
| **Integrasi** | Beberapa | Sedang (100ms-s) | Sedang | Bagaimana komponen berinteraksi; pertanyaan basis data; Panggilan API |
| **E2E** | Sedikit | Lambat (detik-menit) | Tinggi | Pengguna penuh mengalir melalui sistem nyata |
---

## Pengujian Satuan
Menguji unit kode individual secara terpisah.
### Prinsip
| Prinsip | Deskripsi |
|-----------|-------------|
| **cepat** | Setiap pengujian harus dijalankan dalam milidetik |
| **Terisolasi** | Ujian tidak bergantung satu sama lain; tidak ada status bersama |
| **Deterministik** | Input yang sama → output yang sama setiap saat (tidak ada keacakan, tidak ada ketergantungan waktu) |
| **Memeriksa mandiri** | Tes lulus atau gagal secara otomatis; tidak ada pemeriksaan manual |
| **Tepat waktu** | Ditulis disamping atau sebelum kode (TDD) |
### Anatomi Tes
| Fase | Deskripsi |
|-------|-------------|
| **Atur** | Siapkan data pengujian dan dependensi |
| **Bertindak** | Panggil fungsi atau metode yang sedang diuji |
| **Tegaskan** | Pastikan hasilnya sesuai ekspektasi |
### Apa yang Harus Diuji
| Kategori | Contoh |
|----------|---------|
| **Jalan bahagia** | Masukan normal menghasilkan keluaran yang diharapkan |
| **Kasus tepi** | Input kosong, null, nol, nilai maksimum, elemen tunggal |
| **Kasus kesalahan** | Input tidak valid, data hilang, izin ditolak |
| **Kondisi batas** | Off-per-satu; tepat pada batas |
### Mengejek dan Mematikan
| Istilah | Deskripsi | Kapan Menggunakan |
|------|-------------|-------------|
| **Ejekan** | Objek palsu yang mencatat sebutannya | Memverifikasi interaksi (apakah metode ini disebut?) |
| **Rintisan** | Objek palsu yang mengembalikan nilai yang telah ditentukan | Menyediakan data uji (mengembalikan pengguna ini dari database) |
| **Mata-mata** | Pembungkus yang mencatat panggilan ke objek nyata | Verifikasi sebagian |
| **Palsu** | Implementasi yang disederhanakan namun berhasil | Basis data dalam memori untuk pengujian |
| Perpustakaan Mengejek | Bahasa |
|----------------|--------|
| **unittest.mock** | ular piton |
| **Lelucon** | JavaScript/Skrip Ketik |
| **Mockito** | Jawa |
| **Moq** | C#|
| **bersaksi / gomock** | Pergi |
---

## Pengujian Integrasi
Menguji bagaimana beberapa komponen bekerja sama.
| Apa yang Harus Diuji | Contoh |
|-------------|---------|
| **Permintaan basis data** | Apakah ORM menghasilkan SQL yang benar? Apakah indeks digunakan? |
| **Titik akhir API** | Apakah siklus penuh permintaan-respons berfungsi? |
| **Interaksi layanan** | Apakah layanan A memanggil layanan B dengan benar? |
| **Ketergantungan eksternal** | Apakah integrasi gateway pembayaran berfungsi? |
### Strategi
| Strategi | Deskripsi | Pertukaran |
|----------|-------------|-----------|
| **Ketergantungan nyata** | Gunakan database nyata, antrian pesan nyata | Paling realistis; lebih lambat; lebih sulit untuk diatur |
| **Kontainer uji** | Putar kontainer Docker untuk setiap pengujian yang dijalankan | Keseimbangan yang baik; dapat direproduksi |
| **Alternatif dalam memori** | H2 bukannya PostgreSQL; bus pesan dalam memori | Cepat; mungkin melewatkan masalah dunia nyata |
| **Pengujian kontrak** | Verifikasi bahwa layanan menghormati kontrak API mereka | Menangkap perubahan antarmuka |
---

## Pengujian Ujung-ke-Ujung (E2E).
Menguji sistem secara lengkap dari sudut pandang pengguna.
| Alat | Ketik | Terbaik Untuk |
|------|------|----------|
| **Penulis drama** | Otomatisasi peramban | Aplikasi web; lintas browser |
| **cemara** | Otomatisasi peramban | Aplikasi web; pengalaman pengembang |
| **Selenium** | Otomatisasi peramban | Warisan; dukungan bahasa yang luas |
| **Detoks** | Seluler E2E | Bereaksi Aplikasi asli |
| **Aplikasi** | Seluler E2E | Aplikasi seluler asli dan hibrid |
| **Maestro** | Seluler E2E | Aplikasi seluler; sintaks YAML sederhana |
| **k6 / Belalang** | Pengujian beban | Kinerja di bawah beban |
### Praktik Terbaik E2E
| Latihan | Mengapa |
|----------|-----|
| **Uji jalur kritis saja** | Tes E2E lambat; fokus pada hal yang paling penting |
| **Gunakan pabrik data pengujian** | Buat data uji secara terprogram; jangan mengandalkan data benih |
| **Bersihkan setelah pengujian** | Setiap pengujian harus meninggalkan sistem dalam keadaan yang diketahui |
| **Hindari pengujian detail UI** | Uji perilaku, bukan kelas CSS atau posisi elemen |
| **Jalankan di CI** | Tes E2E harus dijalankan secara otomatis pada setiap perubahan |
---

## Pengembangan Berbasis Tes (TDD)
Tulis tesnya terlebih dahulu, lalu tulis kode agar lulus.
| Langkah | Deskripsi |
|------|-------------|
| **1. Merah** | Tulis tes yang gagal yang menggambarkan perilaku yang diinginkan |
| **2. Hijau** | Tulis kode minimum agar tes lulus |
| **3. Pemfaktoran ulang** | Bersihkan kode sambil menjaga pengujian tetap hijau |
| Manfaat | Deskripsi |
|---------|-------------|
| **Umpan balik desain** | Pengujian memaksa Anda memikirkan antarmuka sebelum implementasi |
| **Keamanan regresi** | Setiap bug mendapat ujian; bug tidak akan pernah bisa kembali |
| **Dokumentasi** | Tes berfungsi sebagai dokumentasi hidup dari perilaku yang diharapkan |
| **Keyakinan** | Cakupan pengujian yang tinggi memungkinkan pemfaktoran ulang tanpa rasa takut |
---

## Pengembangan Berbasis Perilaku (BDD)
BDD memperluas TDD dengan menulis tes dalam bahasa alami yang menggambarkan perilaku dari sudut pandang pengguna.
### Format Mengingat-Kapan-Lalu
```
Given a user with an empty shopping cart
When they add a "Python Book" priced at $29.99
Then the cart total should be $29.99
And the cart should contain 1 item
```

| Alat | Bahasa |
|------|----------|
| **Mentimun** | Java, JavaScript, Ruby, dan lainnya |
| **Berperilaku** | ular piton |
| **Alur Spesifikasi** | C#|
| **Jest** (dengan deskripsikan/itu) | JavaScript |
---

## Jenis Pengujian Lainnya
| Ketik | Apa yang Diuji | Alat |
|------|--------------|-------|
| **Kinerja/Beban** | Perilaku sistem sedang dimuat | k6, JMeter, Belalang, Gatling |
| **Keamanan** | Kerentanan dan vektor serangan | OWASP ZAP, Suite Burp, Snyk |
| **Aksesibilitas** | Kepatuhan WCAG | kapak, Mercusuar, pa11y |
| **Kontrak** | Kompatibilitas API antar layanan | Pakta, Kontrak Spring Cloud |
| **Mutasi** | Kualitas rangkaian pengujian itu sendiri | Stryker, mutmut, PIT |
| **Regresi visual** | Perubahan UI antar versi | Percy, Berwarna, BackstopJS |
| **Kekacauan** | Ketahanan sistem terhadap kegagalan | Monyet Kekacauan, Litmus, Gremlin |
| **Asap** | Fungsionalitas dasar setelah penerapan | Skrip khusus; pemeriksaan kesehatan |
| **Rendam** | Perilaku sistem dalam jangka waktu lama | Tes beban yang berjalan lama |
---

## Organisasi Uji
| Pola | Deskripsi | Kapan Menggunakan |
|---------|-------------|-------------|
| **Berlokasi bersama** | Tes di sebelah kode yang mereka uji (`src/utils.test.ts`) | Sebagian besar proyek; mudah ditemukan |
| **Direktori terpisah** | Pengujian dalam folder`tests/`atau`__tests__/`| Proyek besar; pemisahan yang jelas |
| **Perlengkapan tes** | Data pengujian bersama di direktori`fixtures/`| Ketika beberapa pengujian membutuhkan data yang sama |
| **Uji utilitas** | Pembantu bersama di direktori`test-utils/`| Ketika logika pengaturan rumit |
---

## Cakupan Kode
| Metrik | Apa yang Diukurnya | Batasan |
|--------|-----------------|------------|
| **Cakupan jalur** | Persentase baris kode yang dieksekusi oleh tes | Tidak mengukur kualitas pernyataan |
| **Cakupan cabang** | Persentase cabang (jika/lainnya) yang diambil | Lebih baik dari cakupan garis; masih tidak menangkap semua bug |
| **Cakupan jalur** | Persentase jalur eksekusi yang diambil | Paling teliti; eksponensial dalam kode kompleks |
| **Skor mutasi** | Persentase mutasi yang tertangkap oleh tes | Ukuran terbaik kualitas tes |
**Target**: Cakupan saluran 80% adalah standar yang wajar. Namun cakupan adalah panduan, bukan tujuan — cakupan 100% dengan pernyataan yang lemah lebih buruk daripada cakupan 70% dengan pengujian yang menyeluruh.
---

## Integrasi dan Pengujian Berkelanjutan
| Latihan | Deskripsi |
|----------|-------------|
| **Jalankan semua pengujian unit pada setiap penerapan** | Umpan balik cepat; segera menangkap regresi |
| **Jalankan pengujian integrasi pada PR** | Menangkap masalah yang terlewatkan oleh pengujian unit |
| **Jalankan tes E2E setiap malam atau saat digabungkan ke utama** | Lambat tapi menyeluruh |
| **Gagal cepat** | Hentikan saluran pipa jika terjadi kegagalan pertama untuk menghemat waktu |
| **Kebijakan pengujian tidak stabil** | Segera karantina atau hapus tes yang tidak stabil; jangan pernah mengabaikan |
| **Uji paralelisasi** | Jalankan pengujian secara paralel untuk mengurangi waktu CI |
---

## Tips Praktis
- **Sebutkan tes dengan jelas.**`test_calculates_tax_for_high_earner`memberi tahu Anda apa yang rusak. `test_1`tidak memberi tahu Anda apa pun.
- **Satu pernyataan per pengujian (bila praktis).** Membuat kegagalan mudah didiagnosis.
- **Jangan menguji detail penerapan.** Uji perilaku. Jika Anda melakukan refactor internal, pengujian tidak akan rusak.
- **Hindari pengujian kode pihak ketiga.** Tiruan perpustakaan eksternal; uji interaksi kode Anda dengan mereka.
- **Lakukan pengujian dengan cepat.** Jika rangkaian pengujian Anda memerlukan waktu 10 menit, pengembang akan berhenti menjalankannya. Optimalkan tanpa henti.
- **Hapus pengujian yang mati.** Pengujian yang selalu lolos atau pengujian kode yang dihapus adalah gangguan.
- **Perlakukan kode pengujian seperti kode produksi.** Kode tersebut harus dapat dibaca, dipelihara, dan terstruktur dengan baik.
---

## Ringkasan
Pengujian bukanlah suatu pilihan — ini adalah cara Anda membangun perangkat lunak yang tidak rusak. Piramida pengujian memandu Anda menuju banyak pengujian unit cepat, beberapa pengujian integrasi, dan beberapa pengujian E2E. TDD dan BDD memberikan pendekatan terstruktur. Mengolok-olok unit isolasi untuk pengujian. Cakupan kode mengukur luasnya tetapi tidak mengukur kedalamannya. Prinsip yang paling penting adalah ini: jika tidak diuji, berarti rusak — Anda belum mengetahuinya.