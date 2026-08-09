---
# Metadata
title: "Database Systems"
description: "SQL, NoSQL, design patterns, optimization"
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
tags: [database, systems, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "13 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Sistem Basis Data
## Dasar-Dasar Basis Data
### Apa itu Basis Data?
Basis data adalah kumpulan informasi terstruktur terorganisir yang disimpan secara elektronik, dirancang untuk pengambilan, penyisipan, pembaruan, dan penghapusan data secara efisien.
### Sistem Manajemen Basis Data (DBMS)
Perangkat lunak yang berinteraksi dengan pengguna akhir, aplikasi, dan database itu sendiri untuk menangkap dan menganalisis data. Contoh: MySQL, PostgreSQL, Oracle, MongoDB.
### Konsep Utama
- **Skema**: Struktur/organisasi database (tabel, bidang, hubungan)
- **Instance**: Data aktual yang disimpan pada saat tertentu
- **Properti ASAM**: Atomisitas, Konsistensi, Isolasi, Daya Tahan
- **Teorema CAP**: Konsistensi, Ketersediaan, Toleransi Partisi (pilih 2)
- **Normalisasi**: Mengatur data untuk mengurangi redundansi
- **Denormalisasi**: Menambahkan redundansi untuk meningkatkan kinerja membaca
## Basis Data Relasional (SQL)
### Konsep Inti
- **Tabel**: Baris (catatan) dan kolom (bidang)
- **Kunci Utama**: Pengidentifikasi unik untuk setiap baris
- **Kunci Asing**: Referensi ke kunci utama di tabel lain
- **Indeks**: Struktur data meningkatkan kecepatan kueri
- **Tampilan**: Tabel virtual berdasarkan hasil kueri
- **Prosedur Tersimpan**: Blok kode SQL yang telah dikompilasi sebelumnya
- **Pemicu**: Tindakan otomatis terhadap perubahan data
### Operasi SQL (CRUD)```sql
-- Create
INSERT INTO users (name, email) VALUES ('Alice', 'alice@example.com');

-- Read
SELECT * FROM users WHERE id = 1;
SELECT name, email FROM users ORDER BY name LIMIT 10;

-- Update
UPDATE users SET email = 'new@example.com' WHERE id = 1;

-- Delete
DELETE FROM users WHERE id = 1;
```

### Bergabung
- **INNER JOIN**: Mengembalikan baris yang cocok dari kedua tabel
- **LEFT JOIN**: Semua baris dari tabel kiri, cocok dari kanan
- **RIGHT JOIN**: Semua baris dari tabel kanan, cocok dari kiri
- **FULL OUTER JOIN**: Semua baris dari kedua tabel
- **CROSS JOIN**: Produk kartesius dari kedua tabel
- **SELF JOIN**: Tabel digabungkan dengan dirinya sendiri
### Bentuk Normalisasi
- **1NF**: Nilai atom, tidak ada grup berulang
- **2NF**: 1NF + tidak ada ketergantungan parsial (semua atribut non-kunci bergantung pada seluruh kunci utama)
- **3NF**: 2NF + tidak ada ketergantungan transitif (atribut non-kunci tidak bergantung pada atribut non-kunci lainnya)
- **BCNF**: 3NF yang lebih kuat, setiap determinan adalah kunci kandidat
- **4NF**: Tidak ada ketergantungan multinilai
- **5NF**: Tidak ada ketergantungan gabungan
### RDBMS Populer
- **PostgreSQL**: Fitur lanjutan, dapat diperluas, sesuai ACID
- **MySQL**: Aplikasi web yang banyak digunakan dan dapat dibaca dengan cepat
- **Oracle**: Fitur perusahaan, skalabilitas, mahal
- **SQL Server**: ekosistem Microsoft, alat terintegrasi
- **SQLite**: Tertanam, tanpa server, ringan
- **MariaDB**: Garpu MySQL, sumber terbuka
## Basis Data NoSQL
### Jenis Basis Data NoSQL
#### Penyimpanan Dokumen
- **Struktur**: dokumen mirip JSON (BSON)
- **Kasus Penggunaan**: Manajemen konten, katalog, profil pengguna
- **Contoh**: MongoDB, CouchDB, DocumentDB
- **Contoh Kueri** (MongoDB):```javascript
db.users.find({ age: { $gt: 25 } }).sort({ name: 1 });
```

#### Penyimpanan Nilai Kunci
- **Struktur**: Pasangan nilai kunci sederhana
- **Kasus Penggunaan**: Caching, sesi, keranjang belanja
- **Contoh**: Redis, DynamoDB, Riak
- **Karakteristik**: Kueri yang cepat, sederhana, dan terbatas
#### Toko Kolom-Keluarga
- **Struktur**: Kolom dikelompokkan ke dalam kelompok
- **Kasus Penggunaan**: Big data, analitik, rangkaian waktu
- **Contoh**: Cassandra, HBase, ScyllaDB
- **Karakteristik**: Dioptimalkan untuk penulisan, didistribusikan, dapat diskalakan
#### Basis Data Grafik
- **Struktur**: Node, tepi, properti
- **Kasus Penggunaan**: Jejaring sosial, deteksi penipuan, rekomendasi
- **Contoh**: Neo4j, Amazon Neptune, ArangoDB
- **Bahasa Kueri**: Cypher (Neo4j), GREMLIN
### Kapan Menggunakan NoSQL
- Skema yang fleksibel/berkembang
- Persyaratan penskalaan horizontal
- Throughput tulis tinggi
- Data hierarki/bersarang
- Sistem terdistribusi
- Aplikasi waktu nyata
## Desain Basis Data
### Pemodelan Hubungan Entitas
- **Entitas**: Objek/konsep (Pelanggan, Produk, Pesanan)
- **Atribut**: Properti entitas (nama, harga, tanggal)
- **Hubungan**: Koneksi antar entitas (satu-ke-satu, satu-ke-banyak, banyak-ke-banyak)
- **Kardinalitas**: Jumlah instance dalam hubungan
### Pola Desain Skema
- **Pewarisan Tabel Tunggal**: Semua tipe dalam satu tabel dengan diskriminator tipe
- **Pewarisan Tabel Kelas**: Tabel terpisah untuk basis dan subkelas
- **Pewarisan Tabel Beton**: Tabel terpisah untuk setiap kelas beton
- **Tabel Persimpangan**: Menyelesaikan hubungan banyak-ke-banyak
- **Tabel Audit**: Melacak perubahan (dibuat_at, diperbarui_at, dihapus_at)
### Strategi Pengindeksan
- **B-Tree**: Default, kueri rentang, penyortiran
- **Hash**: Pencarian pencocokan tepat
- **Bitmap**: Kolom berkardinalitas rendah (gender, status)
- **Teks Lengkap**: Kemampuan pencarian teks
- **Spasial**: Data Geografis (GIS)
- **Komposit**: Gabungan beberapa kolom
- **Menutup**: Menyertakan semua kolom yang diperlukan untuk kueri
## Optimasi Kueri
### Rencana Eksekusi
- Memahami bagaimana database mengeksekusi query
- Mengidentifikasi kemacetan (pemindaian tabel penuh, indeks hilang)
- Alat: JELASKAN, JELASKAN ANALISIS
### Teknik Optimasi
- **Penggunaan Indeks**: Pastikan kueri menggunakan indeks yang sesuai
- **Penulisan Ulang Kueri**: Menyederhanakan kueri kompleks
- **Pengoptimalan Gabung**: Pilih jenis dan urutan gabungan yang benar
- **Partisi**: Membagi tabel besar (rentang, hash, daftar)
- **Tampilan Terwujud**: Hasil kueri yang telah dihitung sebelumnya
- **Caching Kueri**: Menyimpan hasil kueri yang sering
### Masalah Kinerja Umum
- **Masalah Kueri N+1**: Pengambilan data terkait tidak efisien
- **Indeks Hilang**: Pemindaian tabel lengkap pada tabel besar
- **Pengindeksan berlebih**: Penulisan lambat karena terlalu banyak indeks
- **Lock Contention**: Transaksi menunggu untuk dikunci
- **Kueri Tidak Efisien**: SELECT *, gabungan yang tidak diperlukan
## Transaksi dan Konkurensi
### Tingkat Isolasi Transaksi
- **BACA TANPA KOMITMEN**: Isolasi terendah, kemungkinan pembacaan kotor
- **BACA BERKOMITMEN**: Hanya data yang dikomit yang terlihat (default di sebagian besar DB)
- **BACA BERULANG**: Kueri yang sama mengembalikan hasil yang sama dalam transaksi
- **SERIALIZABLE**: Isolasi tertinggi, transaksi dieksekusi secara berurutan
### Kontrol Konkurensi
- **Penguncian Pesimis**: Mengunci sumber daya sebelum mengakses
- **Penguncian Optimis**: Periksa versi sebelum melakukan
- **MVCC (Kontrol Konkurensi Multi-Versi)**: Mempertahankan beberapa versi baris
- **Penguncian Tingkat Baris**: Mengunci baris tertentu
- **Penguncian Tingkat Meja**: Mengunci seluruh meja
### Kebuntuan
- Ketergantungan melingkar dimana transaksi menunggu satu sama lain
- Pencegahan: Pengurutan kunci yang konsisten, batas waktu, deteksi kebuntuan
- Resolusi: Membatalkan satu transaksi
## Replikasi dan Penskalaan
### Jenis Replikasi
- **Master-Slave**: Satu replika baca utama dan beberapa
- **Master-Master**: Beberapa pemilihan pendahuluan, replikasi dua arah
- **Multi-Master**: N pemilihan pendahuluan, diperlukan penyelesaian konflik
- **Replikasi Rantai**: Replikasi berurutan melalui node
### Pendekatan Penskalaan
- **Penskalaan Vertikal**: Meningkatkan sumber daya server (CPU, RAM, penyimpanan)
- **Penskalaan Horizontal**: Tambahkan lebih banyak server (sharding, partisi)
- **Baca Replika**: Membongkar lalu lintas baca
- **Sharding**: Membagi data di seluruh server berdasarkan kunci/rentang/hash
- **Federasi**: Dibagi berdasarkan fungsi/layanan
### Model Konsistensi
- **Konsistensi Kuat**: Semua node melihat data yang sama pada waktu yang sama
- **Konsistensi Akhirnya**: Node menyatu seiring waktu
- **Konsistensi Kausal**: Hubungan sebab-akibat dipertahankan
- **Baca-Tulisan-Anda**: Pengguna segera melihat pembaruannya sendiri
## Pencadangan dan Pemulihan
### Strategi Cadangan
- **Cadangan Penuh**: Salinan database lengkap
- **Cadangan Tambahan**: Perubahan sejak pencadangan terakhir
- **Cadangan Diferensial**: Perubahan sejak pencadangan penuh terakhir
- **Pemulihan Point-in-Time**: Kembalikan ke momen tertentu
- **Cadangan Berkelanjutan**: Replikasi pencadangan secara real-time
### Prosedur Pemulihan
- **RTO (Tujuan Waktu Pemulihan)**: Waktu henti maksimum yang dapat diterima
- **RPO (Recovery Point Objective)**: Kehilangan data maksimum yang dapat diterima
- **Rencana Pemulihan Bencana**: Prosedur kegagalan yang terdokumentasi
- **Pengujian**: Latihan pemulihan rutin
## Keamanan
### Kontrol Akses
- **Otentikasi**: Verifikasi identitas pengguna
- **Otorisasi**: Memberikan izin (GRANT, REVOKE)
- **Peran**: Izin grup untuk pengelolaan yang lebih mudah
- **Prinsip Hak Istimewa Terkecil**: Akses minimum yang diperlukan
### Perlindungan Data
- **Enkripsi Saat Istirahat**: Mengenkripsi data yang disimpan
- **Enkripsi dalam Transit**: TLS/SSL untuk koneksi
- **Masking**: Menyembunyikan data sensitif di non-produksi
- **Tokenisasi**: Ganti data sensitif dengan token
### Kerentanan Umum
- **Injeksi SQL**: SQL berbahaya dalam input pengguna
- **Eskalasi Hak Istimewa**: Mendapatkan akses tidak sah
- **Pencatatan Audit**: Melacak semua aktivitas basis data
- **Kepatuhan**: Persyaratan GDPR, HIPAA, PCI-DSS
## Teknologi Basis Data Modern
### Basis Data Awan
- **AWS**: RDS, Aurora, DynamoDB, Pergeseran Merah
- **Google Cloud**: Cloud SQL, Spanner, Bigtable, Firestore
- **Azure**: Database SQL, Cosmos DB, Sinaps
- **Manfaat**: Layanan terkelola, penskalaan otomatis, termasuk pencadangan
### Basis Data NewSQL
- Gabungkan konsistensi SQL dengan skalabilitas NoSQL
- **Contoh**: CockroachDB, TiDB, YugabyteDB, Google Spanner
- **Fitur**: Terdistribusi, transaksi ACID, penskalaan horizontal
### Database Rangkaian Waktu
- Dioptimalkan untuk data yang diberi stempel waktu
- **Contoh**: InfluxDB, TimescaleDB, Prometheus
- **Kasus Penggunaan**: IoT, pemantauan, data keuangan
### Basis Data Vektor
- Menyimpan dan menanyakan vektor penyematan
- **Contoh**: Biji Pinus, Milvus, Weaviate, Qdrant
- **Kasus Penggunaan**: Pencarian semantik, sistem rekomendasi, aplikasi AI
### Basis Data Multi-Model
- Mendukung banyak model data dalam satu sistem
- **Contoh**: ArangoDB, OrientDB, Azure Cosmos DB
- **Manfaat**: Fleksibilitas tanpa banyak database
## ORM dan Akses Data
### Pemetaan Objek-Relasional
- **Tujuan**: Memetakan tabel database ke objek pemrograman
- **ORM Populer**:
  - Python: SQLAlkimia, Django ORM, Peewee
  - JavaScript: Sekuel, Prisma, TypeORM
  - Java: Hibernasi, JPA
  - Ruby: Rekaman Aktif
  - .NET: Kerangka Entitas
### Manfaat
- Abstraksi dari SQL
- Ketik keamanan
- Manajemen migrasi
- API pembuatan kueri
### Kekurangan
- Overhead kinerja
- Kueri kompleks lebih sulit untuk ditulis
- Masalah kueri N+1
- Kurva belajar
## Administrasi Basis Data
### Tanggung Jawab DBA
- Instalasi dan konfigurasi
- Penyetelan kinerja
- Pencadangan dan pemulihan
- Manajemen keamanan
- Perencanaan kapasitas
- Pemantauan dan peringatan
- Manajemen tambalan
### Metrik Pemantauan
- Waktu respons permintaan
- Throughput (transaksi per detik)
- Jumlah koneksi
- Rasio cache hit
- Disk I/O
- Kunci waktu tunggu
- Keterlambatan replikasi
### Tugas Pemeliharaan
- **Vakum/Analisis**: Perbarui statistik, dapatkan kembali ruang
- **Pembangunan Kembali Indeks**: Defragmentasi indeks
- **Pembaruan Statistik**: Terus beri tahu pengoptimal kueri
- **Rotasi Log**: Kelola ukuran file log
- **Perencanaan Kapasitas**: Memprediksi pertumbuhan, meningkatkan rencana