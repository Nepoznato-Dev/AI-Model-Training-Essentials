---
# Metadata
title: "Technology and Computing"
description: "Computing basics, internet, databases, cloud, security"
category: "General Reference"
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
reviewed_by: "General Reference Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [technology, computing, general-reference]
difficulty_level: "beginner"
prerequisites: []
estimated_reading_time: "8 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Teknologi dan Komputasi
Komputasi ada dimana-mana — di ponsel Anda, mobil Anda, lemari es Anda, perangkat medis Anda, dan infrastruktur yang menjalankan masyarakat modern. Anda tidak perlu menjadi seorang programmer untuk mendapatkan manfaat dari memahami cara kerjanya. File ini mencakup dasar-dasar: apa itu komputer, cara kerja internet, cara perangkat lunak dibuat, dan konsep yang membentuk dunia digital.
> **Ingin mempelajari lebih dalam?** File ini adalah ikhtisar yang luas. Untuk liputan mendetail tentang topik apa pun, lihat file khusus di[`01_coding_and_technology/`](../01_coding_and_technology/)— termasuk[database systems](../01_coding_and_technology/database_systems.md),[cloud architecture](../01_coding_and_technology/cloud_architecture.md),[networking](../01_coding_and_technology/networking_basics.md), dan.
---

## Apa itu Komputer?
Pada intinya, setiap komputer – mulai dari ponsel pintar hingga superkomputer – melakukan hal yang sama: mengambil masukan, memprosesnya sesuai instruksi (program), dan menghasilkan keluaran. Keajaibannya ada pada kecepatan dan skala.
### Arsitektur Von Neumann
Hampir semua komputer modern mengikuti desain dasar ini:
| Komponen | Apa Fungsinya | Analogi |
|-----------|-------------|---------|
| **CPU** (Unit Pemrosesan Pusat) | Menjalankan instruksi; "otak" | Koki mengikuti resep |
| **RAM** (Memori) | Menyimpan data yang digunakan secara aktif oleh CPU; hilang saat listrik mati | Meja — akses cepat, ruang terbatas |
| **Penyimpanan** (SSD/HDD) | Menyimpan data secara permanen | Dapur — akses lebih lambat, lebih banyak ruang |
| **Masukan/Keluaran** | Keyboard, mouse, layar, jaringan | Bagaimana koki menerima pesanan dan mengantarkan makanan |
| **GPU** (Unit Pemrosesan Grafis) | Prosesor khusus untuk tugas paralel (grafis, AI) | Sebuah tim asisten semuanya mengerjakan tugas yang sama secara bersamaan |
**Informasi penting**: RAM cepat namun bersifat sementara. Penyimpanan lambat tapi permanen. Ketika komputer Anda "terasa lambat", hal ini sering kali disebabkan karena komputer kehabisan RAM dan harus menggunakan penyimpanan sebagai memori sementara (swapping), yang jauh lebih lambat.
---

## Bahasa Pemrograman — Berbicara dengan Komputer
Bahasa pemrograman adalah sekumpulan instruksi yang dapat dieksekusi oleh komputer. Bahasa yang berbeda dirancang untuk tujuan yang berbeda. Untuk cakupan rinci dari 34 bahasa, lihat folder [`programming_languages/`](../01_coding_and_technology/programming_languages/).
| Bahasa | Terbaik Untuk | Mengapa Memilihnya |
|----------|---------|---------------|
| **Piton** | Ilmu data, AI, otomatisasi, backend web | Sintaks sederhana; ekosistem yang sangat besar; bagus untuk pemula |
| **JavaScript** | Frontend web, tumpukan penuh (Node.js) | Berjalan di setiap browser; penting untuk pengembangan web |
| **Jawa** | Perangkat lunak perusahaan, aplikasi Android | Platform-independen (JVM); ekosistem besar |
| **C/C++** | Pemrograman sistem, permainan, tertanam | Performa maksimal; kontrol perangkat keras langsung |
| **Karat** | Pemrograman sistem dengan jaminan keamanan | Keamanan memori tanpa pengumpulan sampah |
| **Pergi** | Layanan cloud, layanan mikro, alat CLI | Sederhana; konkurensi yang sangat baik; kompilasi cepat |
| **SQL** | Kueri basis data | Bahasa universal untuk bekerja dengan data |
| **Skrip Ketik** | Aplikasi web skala besar | JavaScript dengan pemeriksaan tipe; menangkap bug lebih awal |
---

## Cara Kerja Internet
Internet tidak sama dengan web. Internet adalah jaringan fisik — kabel, router, server, dan protokol yang menghubungkan miliaran perangkat. World Wide Web adalah salah satu layanan yang berjalan di internet (bersama dengan email, transfer file, streaming, permainan, dll.).
### Perjalanan Permintaan Web
Saat Anda mengetik`https://www.example.com`di browser Anda:
1. **Pencarian DNS**: Browser Anda meminta server DNS untuk menerjemahkan "www.example.com" menjadi alamat IP (seperti 93.184.216.34).
2. **Koneksi TCP**: Perangkat Anda membuat koneksi ke alamat IP tersebut menggunakan TCP (protokol yang menjamin pengiriman yang andal).
3. **TLS handshake**: Jika menggunakan HTTPS, browser Anda dan server menegosiasikan koneksi terenkripsi.
4. **Permintaan HTTP**: Browser Anda mengirimkan permintaan: "Beri saya halaman di /index.html."
5. **Pemrosesan server**: Server web menemukan halaman, mungkin menanyakan database, dan menyiapkan respons.
6. **Respon HTTP**: Server mengirimkan kembali HTML, CSS, dan JavaScript.
7. **Rendering**: Browser Anda mengurai HTML, menerapkan gaya CSS, dan mengeksekusi JavaScript untuk menampilkan halaman.
Keseluruhan proses ini biasanya memakan waktu kurang dari satu detik.
### Protokol Kunci
| Protokol | Apa Fungsinya | Lapisan |
|----------|-------------|-------|
| **IP** (Protokol Internet) | Merutekan paket antar jaringan | Jaringan |
| **TCP** | Pengiriman yang andal dan teratur (mentransmisikan ulang paket yang hilang) | Transportasi |
| **UDP** | Pengiriman cepat, tidak dapat diandalkan (tidak ada transmisi ulang) | Transportasi |
| **HTTP/HTTPS** | Transfer halaman web (HTTPS menambahkan enkripsi) | Aplikasi |
| **DNS** | Menerjemahkan nama domain ke alamat IP | Aplikasi |
| **SSH** | Mengamankan akses jarak jauh ke komputer | Aplikasi |
| **SMTP/IMAP** | Pengiriman dan penerimaan email | Aplikasi |
---

## Pengembangan Perangkat Lunak — Bagaimana Program Dibangun
### Proses Pengembangan
1. **Menulis kode**: Pengembang menulis instruksi dalam bahasa pemrograman.
2. **Kode uji**: Jalankan kode untuk memverifikasi bahwa kode berfungsi dengan benar.
3. **Kontrol versi**: Lacak perubahan menggunakan Git — standar universal.
4. **Ulasan**: Pengembang lain memeriksa kesalahan dan kualitas kode.
5. **Build**: Mengubah kode sumber menjadi program yang dapat dijalankan (kompilasi).
6. **Deploy**: Merilis program ke pengguna (server, toko aplikasi, dll.).
7. **Monitor**: Perhatikan kesalahan dan masalah kinerja dalam produksi.
### Konsep Utama
| Konsep | Apa Artinya | Mengapa Itu Penting |
|---------|---------------|----------------|
| **Kontrol versi (Git)** | Lacak setiap perubahan kode dari waktu ke waktu | Kolaborasi; kemampuan untuk membatalkan kesalahan |
| **API** (Antarmuka Pemrograman Aplikasi) | Cara yang ditentukan bagi komponen perangkat lunak untuk berkomunikasi | Memungkinkan sistem yang berbeda untuk bekerja sama |
| **Basis Data** | Penyimpanan terorganisir untuk data | Setiap aplikasi perlu menyimpan dan mengambil data |
| **Pengujian** | Otomatis memeriksa apakah kode berfungsi dengan benar | Mencegah bug menjangkau pengguna |
| **CI/CD** (Integrasi/Pengiriman Berkelanjutan) | Saluran pipa otomatis dari penerapan kode ke produksi | Rilis lebih cepat dan aman |
| **Kontainerisasi (Docker)** | Kemas aplikasi dengan semua dependensinya | "Berfungsi di mesin saya" menjadi "berfungsi di mana saja" |
---

## Basis Data — Tempat Data Berada
Setiap aplikasi perlu menyimpan data. Basis data adalah sistem yang melakukan hal ini secara efisien dan andal.
| Ketik | Bagaimana Data Disimpan | Terbaik Untuk | Contoh |
|------|-------------------|----------|---------|
| **Relasional (SQL)** | Tabel dengan baris dan kolom; skema ketat | Data terstruktur; pertanyaan kompleks; transaksi | PostgreSQL, MySQL, SQLite |
| **Dokumen (NoSQL)** | Dokumen mirip JSON; skema fleksibel | Data semi terstruktur; iterasi cepat | MongoDB, SofaDB |
| **Nilai kunci** | Kunci sederhana → pasangan nilai | cache; penyimpanan sesi; pencarian cepat | Redis, DynamoDB |
| **Grafik** | Node dan edge (hubungan) | Jejaring sosial; mesin rekomendasi | Neo4j, JanusGraph |
| **Rangkaian waktu** | Dioptimalkan untuk data dengan cap waktu | Pemantauan; analitik; IoT | InfluxDB, TimescaleDB |
**SQL** (Structured Query Language) adalah bahasa standar untuk database relasional. Ini adalah salah satu keterampilan teknis paling berharga yang dapat Anda pelajari — hampir setiap organisasi menggunakan database, dan SQL adalah cara Anda berkomunikasi dengannya.
---

## Sistem Operasi
Sistem operasi (OS) adalah lapisan perangkat lunak antara Anda (dan program Anda) dan perangkat keras. Ia mengelola memori, proses, file, dan perangkat.
| sistem operasi | Dimana Ia Mendominasi | Fitur Utama |
|----|----|-------------|
| **Jendela** | PC desktop/laptop (~72% pangsa pasar) | Kompatibilitas perangkat lunak/perangkat keras terluas |
| **macOS** | Profesional kreatif, pengembang | Berbasis Unix; UI yang dipoles; Ekosistem Apple |
| **Linux** | Server (~96%), superkomputer (100%), tertanam, pengembang | Sumber terbuka; bebas; sangat dapat disesuaikan |
| **Android** | Seluler (~72% pangsa pasar global) | Berdasarkan kernel Linux; sumber terbuka |
| **iOS** | Seluler (~27% global, tetapi pendapatan lebih tinggi) | Ekosistem tertutup; dipoles; berfokus pada privasi |
Linux patut mendapat perhatian khusus: Linux mendukung sebagian besar internet, setiap 500 superkomputer teratas, sebagian besar infrastruktur cloud, dan semua ponsel Android. Ini gratis, open source, dan dikelola oleh komunitas global.
---

## Komputasi Awan
Komputasi awan berarti menyewa sumber daya komputasi (server, penyimpanan, database, dll.) melalui internet alih-alih membeli dan memelihara perangkat keras Anda sendiri. Untuk panduan komprehensif mengenai arsitektur cloud, model layanan, dan perbandingan penyedia, lihat[cloud architecture](../01_coding_and_technology/cloud_architecture.md).
| Model Layanan | Apa yang Anda Dapatkan | Analogi | Contoh |
|---------------|-------------|---------|---------|
| **IaaS** (Infrastruktur) | Server virtual, penyimpanan, jaringan | Menyewa sebidang tanah dan bangunan sesuai keinginan | AWS EC2, Mesin Komputasi Google |
| **PaaS** (Platform) | Lingkungan waktu proses; Anda membawa kode | Menyewa apartemen berperabotan | Heroku, Mesin Aplikasi Google |
| **SaaS** (Perangkat Lunak) | Aplikasi lengkap; kamu cukup menggunakannya | Menginap di hotel | Gmail, Slack, Tenaga Penjualan |
Tiga penyedia cloud utama adalah **AWS** (Amazon, ~32% pangsa pasar), **Azure** (Microsoft, ~23%), dan **GCP** (Google, ~10%). Mereka menawarkan ratusan layanan yang mencakup komputasi, penyimpanan, database, AI, jaringan, dan banyak lagi.
---

## Keamanan Siber — Melindungi Sistem Digital
Keamanan siber adalah praktik melindungi komputer, jaringan, dan data dari serangan. Hal ini penting karena semuanya saling terhubung, dan dampak pelanggarannya sangat besar. Untuk panduan lengkap yang mencakup 10 Besar OWASP, siklus hidup pengembangan yang aman, dan manajemen rahasia, lihat.
### Ancaman Umum
| Ancaman | Apa Itu | Pencegahan |
|--------|-----------|------------|
| **Perangkat lunak jahat** | Perangkat lunak berbahaya (virus, worm, trojan) | Anti Virus; terus perbarui perangkat lunak |
| **Phishing** | Email/pesan palsu yang menipu Anda agar mengungkapkan informasi | Pelatihan; pemfilteran email; skeptisisme |
| **Ransomware** | Mengenkripsi data Anda; menuntut pembayaran untuk kunci | Cadangan; sistem tambalan; jangan membayar |
| **DDoS** | Membanjiri layanan dengan lalu lintas | Penyaringan lalu lintas; Perlindungan CDN |
| **Injeksi SQL** | Memasukkan SQL berbahaya ke dalam kolom input | Kueri yang diparameterisasi; validasi masukan |
| **Man-di-tengah** | Menyadap komunikasi antara dua pihak | Enkripsi HTTPS/TLS |
### Dasar-Dasar Keamanan
- **Enkripsi**: Mengacak data sehingga hanya pihak yang berwenang yang dapat membacanya. HTTPS menggunakan TLS untuk mengenkripsi lalu lintas web.
- **Otentikasi**: Verifikasi identitas. Gunakan otentikasi multi-faktor (MFA) — kata sandi + sesuatu yang lain (kode, biometrik).
- **Otorisasi**: Verifikasi izin. Hanya karena Anda login bukan berarti Anda harus mengakses semuanya.
- **Prinsip hak istimewa paling rendah**: Berikan pengguna dan sistem hanya akses yang mereka perlukan, tidak lebih.
- **Manajemen patch**: Selalu memperbarui perangkat lunak. Sebagian besar pelanggaran mengeksploitasi kerentanan yang diketahui dan sudah memiliki patch.
---

## Format Data
Program bertukar data dalam format tertentu. Yang paling umum:
| Format | Struktur | Digunakan Untuk |
|--------|-----------|----------|
| **JSON** | Pasangan kunci-nilai; dapat dibaca manusia | Lebah; konfigurasi; pertukaran data |
| **XML** | Berbasis tag; bertele-tele tapi fleksibel | Sistem warisan; dokumen; API SOAP |
| **YAML** | Berbasis lekukan; sangat mudah dibaca | Konfigurasi (Docker, Kubernetes, CI/CD) |
| **CSV** | Baris dan kolom teks biasa | Impor/ekspor data; spreadsheet |
---

## Ringkasan
Komputasi bukanlah keajaiban, melainkan rekayasa. Komputer mengikuti instruksi dengan kecepatan luar biasa. Internet menghubungkan miliaran dari mereka menggunakan protokol standar. Perangkat lunak dibangun oleh tim yang terdiri dari orang-orang yang menulis, menguji, dan menerapkan kode dalam siklus berulang. Basis data menyimpan dan mengambil data. Komputasi awan memungkinkan siapa pun mengakses sumber daya komputasi besar-besaran sesuai permintaan. Dan keamanan siber adalah perjuangan berkelanjutan untuk menjaga semua ini aman dari orang-orang yang ingin mengeksploitasinya. Memahami dasar-dasar ini membantu Anda menavigasi dunia digital — baik Anda pengguna, pengembang, atau sekadar seseorang yang mencoba memahami teknologi yang membentuk kehidupan modern.