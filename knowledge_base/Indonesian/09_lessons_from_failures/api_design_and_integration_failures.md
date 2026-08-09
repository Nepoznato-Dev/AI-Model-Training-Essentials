---
# Metadata
title: "API Design and Integration Failures"
description: "API anti-patterns, breaking changes, versioning failures, cascading failures"
category: "Lessons from Failures"
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
reviewed_by: "Lessons from Failures Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [api, design, integration, failures, lessons-from-failures]
difficulty_level: "advanced"
prerequisites: []
estimated_reading_time: "6 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# Kegagalan Desain dan Integrasi API
API (Antarmuka Pemrograman Aplikasi) adalah jaringan penghubung perangkat lunak modern — API memungkinkan layanan berkomunikasi, memungkinkan pihak ketiga berintegrasi, dan memungkinkan tim bekerja secara mandiri. Ketika desain API berjalan salah, konsekuensinya akan dirasakan oleh setiap sistem yang bergantung padanya: integrasi yang rusak, kerentanan keamanan, frustrasi pengembang, dan penulisan ulang yang mahal. Kegagalan integrasi — ketika sistem tidak dapat berkomunikasi dengan andal — merupakan salah satu sumber insiden produksi yang paling umum.
---

## Kegagalan Desain API Umum
### Kesalahan Desain
| Kesalahan | Deskripsi | Konsekuensi |
|---------|-------------|-------------|
| **Penamaan tidak konsisten** | `/getUsers`vs`/list_users`vs`/fetch-users`| Kebingungan; kesalahan; perkembangan lambat |
| **Titik akhir kelebihan beban** | Satu titik akhir yang melakukan 10 hal berbeda berdasarkan parameter | Sulit dimengerti; sulit untuk diuji; sulit diubah |
| **Kurang diambil** | Klien perlu melakukan 5 panggilan API untuk mendapatkan data terkait | Lambat; boros; kode klien yang kompleks |
| **Pengambilan berlebihan** | API mengembalikan semua bidang ketika klien hanya membutuhkan 2 | Bandwidth yang terbuang; lambat di perangkat seluler; risiko keamanan (mengekspos data yang tidak diperlukan) |
| **Tidak ada versi** | Perubahan yang dapat menyebabkan gangguan diterapkan tanpa peringatan | Klien istirahat; pengembang yang marah |
| **Pesan kesalahan tidak jelas** | "Kesalahan 500: Kesalahan Server Internal" tanpa detail | Tidak mungkin untuk di-debug; resolusi lambat |
| **Penomoran halaman tidak ada** | Endpoint mengembalikan semua catatan (bisa jutaan) | Batas waktu; kelelahan memori; klien mogok |
| **Kode status tidak konsisten** | 200 OK untuk kesalahan; 500 untuk kesalahan klien | Klien tidak dapat membedakan kesuksesan dan kegagalan |
### Anti-Pola REST API
| Anti-Pola | Deskripsi | Pendekatan yang Lebih Baik |
|-------------|-------------|-----------------|
| **Menggunakan GET untuk mutasi** | `GET /delete-user?id=5`| Gunakan metode HAPUS |
| **Menggunakan POST untuk semuanya** | `POST /get-users`; `POST /update-user`| Gunakan metode HTTP yang sesuai (GET, POST, PUT, PATCH, DELETE) |
| **Mengembalikan HTML dari API** | API mengembalikan fragmen HTML | Kembalikan JSON; biarkan klien merender |
| **Logika bisnis di URL** | `/users/active/premium/from-2023`| Gunakan parameter kueri atau isi permintaan untuk filter kompleks |
| **Mengekspos skema database** | `/api/table_name/column`| Rancang API berdasarkan sumber daya dan konsep domain, bukan tabel |
| **Tanpa HATEOAS / tautan** | Klien melakukan hardcode pada semua URL | Sertakan tautan ke sumber daya terkait dalam tanggapan |
---

## Kegagalan Keamanan
### Kerentanan API Umum
| Kerentanan | Deskripsi | Contoh |
|--------------|-------------|---------|
| **Otentikasi rusak** | API tidak memverifikasi identitas dengan benar | Validasi token tidak ada; token kedaluwarsa diterima |
| **Paparan data berlebihan** | API mengembalikan lebih banyak data daripada kebutuhan klien | Titik akhir pengguna mengembalikan hash kata sandi dan ID internal |
| **Tugas massal** | Klien dapat menyetel kolom yang tidak boleh | `PATCH /user`memungkinkan pengaturan`role: "admin"`|
| **Injeksi** | Input pengguna diartikan sebagai kode | injeksi SQL; injeksi NoSQL; injeksi perintah |
| **IDOR** (Referensi Objek Langsung Tidak Aman) | Mengakses sumber daya dengan mengubah ID di URL | `/api/users/5`→ ubah ke`/api/users/6`untuk melihat data orang lain |
| **Pembatasan tarif tidak ada** | Tidak ada batasan pada panggilan API | kekerasan; penolakan layanan; menggores |
| **Kesalahan konfigurasi CORS** | Akses lintas asal yang terlalu permisif | `Access-Control-Allow-Origin: *`pada titik akhir yang diautentikasi |
### Kegagalan Otentikasi dan Otorisasi
| Kegagalan | Deskripsi | Dampak |
|---------|-------------|--------|
| **Kredensial yang di-hardcode** | Kunci API atau kata sandi dalam kode sumber | Bocor melalui kontrol versi; dapat diakses oleh semua pengembang |
| **Tidak ada masa berlaku token** | Token tidak pernah kedaluwarsa | Token yang dicuri memberikan akses permanen |
| **Kunci rahasia yang lemah** | Kunci penandatanganan yang pendek atau dapat diprediksi | Token dapat dipalsukan |
| **Tidak ada cakupan/izin** | Semua token memiliki akses penuh | Token yang disusupi = akses sistem penuh |
| **Mencatat data sensitif** | Token atau kata sandi di log | Dapat diakses oleh siapa saja yang memiliki akses log |
| **Otorisasi tidak konsisten** | Beberapa titik akhir memeriksa izin; yang lain tidak | Akses tidak sah melalui titik akhir yang tidak dijaga |
---

## Kegagalan Integrasi
### Masalah Integrasi Sistem Terdistribusi
| Kegagalan | Deskripsi | Contoh |
|---------|-------------|---------|
| **Kopling ketat** | Layanan bergantung pada detail implementasi internal satu sama lain | Mengubah database satu layanan akan merusak tiga layanan lainnya |
| **Rantai sinkron** | Layanan A panggilan B panggilan C panggilan D; latensi terakumulasi | 200 ms + 300 ms + 500 ms = waktu respons 1 detik |
| **Tidak ada pemutus arus** | Layanan yang gagal menyebabkan kegagalan berjenjang | Layanan D lambat; semua layanan upstream menghabiskan threadnya menunggu |
| **Tidak ada logika coba lagi** | Kegagalan sementara menjadi permanen | Jaringan blip = transaksi gagal; pengguna harus mencoba lagi secara manual |
| **Percobaan ulang yang berlebihan** | Percobaan ulang tanpa kemunduran membebani layanan pemulihan | Masalah kawanan guntur |
| **Tidak ada idempotensi** | Mencoba kembali operasi non-idempoten akan menghasilkan duplikat | Pembayaran dibebankan dua kali; pesanan dibuat dua kali |
| **Kejutan konsistensi akhirnya** | Klien membaca data basi setelah menulis | Profil pembaruan pengguna; menyegarkan halaman; data lama masih ditampilkan |
### Kegagalan Integrasi Pihak Ketiga
| Kegagalan | Deskripsi | Mitigasi |
|---------|-------------|------------|
| **Perubahan API Vendor** | Pihak ketiga mengubah API mereka tanpa pemberitahuan | Penyematan versi; lapisan abstraksi; memantau log perubahan vendor |
| **Pembatasan tarif** | Pihak ketiga membatasi permintaan Anda | cache; permintaan antrian; menegosiasikan batas yang lebih tinggi |
| **Waktu henti vendor** | Layanan pihak ketiga tidak tersedia | Pemutus arus; perilaku mundur; strategi multi-vendor |
| **Format data berubah** | Pihak ketiga mengubah format respons | Validasi skema; lapisan transformasi; peringatan tentang perubahan format |
| **Penghentian tanpa jalur migrasi** | Vendor tidak lagi menggunakan titik akhir yang tidak memiliki | Tetap terinformasi; mempertahankan abstraksi; rencanakan migrasi lebih awal |
---

## Studi Kasus
### Studi Kasus 1: API yang Mengembalikan Segalanya
| Aspek | Deskripsi |
|--------|-------------|
| **Skenario** | API pengguna perusahaan SaaS mengembalikan semua bidang pengguna termasuk metadata internal |
| **Apa yang salah** | Tidak ada pemfilteran bidang; respons termasuk hash kata sandi, catatan internal, dan tanda admin |
| **Dampak** | Peneliti keamanan menemukan paparan tersebut; keterbukaan publik; Investigasi GDPR |
| **Akar penyebab** | API membuat serial seluruh model database tanpa memfilter |
| **Perbaiki** | Model respons eksplisit; kontrol akses tingkat lapangan; tinjauan keamanan semua titik akhir |
| **Pelajaran** | Jangan pernah mengekspos model database Anda secara langsung melalui API; gunakan DTO (Objek Transfer Data) |
### Studi Kasus 2: Kegagalan Bertingkat
| Aspek | Deskripsi |
|--------|-------------|
| **Skenario** | Arsitektur layanan mikro dengan komunikasi antar layanan yang sinkron |
| **Apa yang salah** | Salah satu layanan mengalami perlambatan basis data; layanan hulu menunggu tanggapan; kumpulan thread habis |
| **Dampak** | Pemadaman sistem total selama 45 menit; semua layanan terpengaruh |
| **Akar penyebab** | Tidak ada pemutus arus; tidak ada batas waktu; rantai ketergantungan sinkron |
| **Perbaiki** | Pemutus arus; batas waktu; komunikasi asinkron jika memungkinkan; sekat |
| **Pelajaran** | Panggilan yang sinkron antar layanan menciptakan rantai yang rapuh; desain untuk kegagalan |
---

## Praktik Terbaik
### Daftar Periksa Desain API
| Daerah | Latihan |
|------|----------|
| **Penamaan** | Gunakan kata benda untuk sumber daya; Metode HTTP untuk tindakan; konvensi penamaan yang konsisten |
| **Versi** | Versi dari hari pertama; gunakan versi URL (`/v1/`) atau versi header |
| **Paginasi** | Selalu memberi nomor halaman pada titik akhir daftar; gunakan penomoran halaman berbasis kursor untuk kumpulan data besar |
| **Penanganan kesalahan** | Format kesalahan yang konsisten; sertakan kode kesalahan; memberikan pesan yang dapat ditindaklanjuti |
| **Pembatasan tarif** | Menerapkan batasan tarif; kembalikan 429 dengan coba lagi setelah header |
| **Idempotensi** | Mendukung kunci idempotensi untuk titik akhir mutasi |
| **Dokumentasi** | Spesifikasi OpenAPI / Swagger; terus perbarui; berikan contoh |
| **Pengujian** | Tes kontrak; tes integrasi; tes kontrak berbasis konsumen |
| **Pemantauan** | Lacak latensi; tingkat kesalahan; hasil; kesehatan ketergantungan |
| **Penghentian** | Umumkan penghentian jauh sebelumnya; memberikan panduan migrasi |
---

## Ringkasan
Kegagalan desain API berkisar dari yang bersifat kosmetik (penamaan yang tidak konsisten) hingga bencana (kerentanan keamanan, kegagalan berjenjang). Kesalahan desain yang paling umum — titik akhir yang kelebihan beban, pengambilan berlebihan, penomoran halaman yang hilang, kesalahan yang tidak jelas — membuat API sulit digunakan dan dipelihara. Kegagalan keamanan — autentikasi yang rusak, IDOR, penugasan massal, paparan data yang berlebihan — membuat sistem rentan terhadap serangan. Kegagalan integrasi — kopling ketat, rantai sinkron, pemutus sirkuit yang hilang, tidak ada idempotensi — menciptakan sistem yang rapuh di mana satu kegagalan terjadi di seluruh layanan. Integrasi pihak ketiga menambah risiko eksternal: perubahan API, pembatasan tarif, dan waktu henti vendor. Strategi pencegahannya sudah ditetapkan: gunakan model respons yang eksplisit; versi dari hari pertama; menerapkan pemutus sirkuit dan batas waktu; desain untuk idempotensi; memvalidasi dan membersihkan semua masukan; pantau semuanya; dan memperlakukan kontrak API sebagai perjanjian mengikat yang memerlukan koordinasi untuk berubah. API terbaik itu membosankan — dapat diprediksi, konsisten, terdokumentasi dengan baik, dan tahan terhadap kegagalan.