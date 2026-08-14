<!--
---
# Metadata
title: "Performance Optimisation"
description: "Profiling, caching, CDN, query optimisation, front-end perf"
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
tags: [performance, optimization, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "8 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Optimasi Kinerja
Pengoptimalan kinerja adalah praktik membuat perangkat lunak lebih cepat — mengurangi waktu respons, meningkatkan throughput, menurunkan penggunaan memori, dan menghilangkan kemacetan. Ini adalah salah satu keterampilan paling berdampak yang dapat dimiliki seorang pengembang, karena perangkat lunak yang lambat akan kehilangan pengguna, membuang-buang sumber daya, dan membuat frustrasi semua orang. Tapi ini juga salah satu kesalahan yang paling sering dilakukan, karena pengembang mengoptimalkan hal yang salah berdasarkan intuisi dan bukan bukti.
---

## Aturan Emas
> **Ukur dulu, optimalkan kedua.** Jangan pernah mengoptimalkan berdasarkan asumsi. Buat profil kodenya, temukan hambatan sebenarnya, dan perbaiki.
| Anti-pola | Mengapa Ini Buruk |
|-------------|-------------|
| **Pengoptimalan dini** | Menghabiskan waktu untuk mempercepat kode yang tidak lambat |
| **Mengoptimalkan tanpa pengukuran** | Memperbaiki kemacetan yang salah; tidak ada cara untuk memverifikasi peningkatan |
| **Mengorbankan keterbacaan demi kecepatan** | Kode yang tidak dapat dibaca harganya lebih mahal daripada peningkatan kinerja |
| **Menyimpan semuanya dalam cache** | Data basi, memori membengkak, kompleksitas |
---

## Pembuatan profil
Sebelum Anda dapat membuat sesuatu lebih cepat, Anda perlu mengetahui *di mana* waktu tersebut dihabiskan.
| Jenis Alat | Apa yang Diukurnya | Contoh |
|-----------|-----------------|----------|
| **profil CPU** | Fungsi mana yang paling banyak menghabiskan waktu CPU | cProfile (Python), kinerja (Linux), Chrome DevTools (JS) |
| **Profiler memori** | Alokasi dan kebocoran memori | tracemalloc (Python), Valgrind, heaptrack |
| **profil I/O** | Kemacetan disk dan jaringan I/O | iotop, strace, Wireshark |
| **APM (Pemantauan Kinerja Aplikasi)** | Waktu permintaan ujung ke ujung | Peninggalan Baru, Datadog, Jaeger |
| **Alat Pengembang Peramban** | Render frontend, eksekusi JavaScript, jaringan | Alat Pengembang Chrome, Profiler Firefox |
### Alur Kerja Pembuatan Profil
| Langkah | Deskripsi |
|------|-------------|
| 1. Identifikasi operasi yang lambat | Pengguna melaporkan pemuatan halaman yang lambat; pemantauan menunjukkan latensi tinggi |
| 2. Profil jalur lengkap | Temukan komponen mana yang paling banyak memakan waktu |
| 3. Telusuri | Profil komponen spesifik tersebut untuk menemukan fungsi hot |
| 4. Perbaiki kemacetan | Terapkan optimasi yang sesuai |
| 5. Ukur kembali | Verifikasi peningkatannya; periksa regresi |
---

## Optimasi Algoritma
Peningkatan kinerja terbesar berasal dari pemilihan algoritma yang lebih baik, bukan dari optimasi mikro.
| Ubah | Peningkatan |
|--------|------------|
| Pencarian linier O(n) → Pencarian tabel hash O(1) | 100x+ untuk kumpulan data besar |
| Loop bersarang O(n²) → Urutkan + pencarian biner O(n log n) | Urutan besarnya untuk n | besar
| Perhitungan berulang → Memoisasi / caching | Menghilangkan pekerjaan yang mubazir |
| Penggabungan string dalam satu lingkaran → Pembuat / gabung | Menghindari penyalinan string kuadrat |
| Data tidak disortir → Data diurutkan dengan pencarian biner | O(log n) bukan O(n) per pencarian |
---

## Strategi Caching
Caching menyimpan hasil yang dihitung sehingga tidak perlu dihitung ulang.
| Jenis Tembolok | Lokasi | Kecepatan | Seumur Hidup |
|-----------|----------|-------|----------|
| **Cache CPU** | L1/L2/L3 | ~1 ns | Otomatis |
| **Dalam memori** | RAM Aplikasi (dict, HashMap) | ~100 ns | Sampai dibersihkan atau digusur |
| **Cache terdistribusi** | Redis, Memcache | ~1 mdtk | TTL yang dapat dikonfigurasi |
| **CDN** | Server tepi di seluruh dunia | ~10-50 mdtk | TTL yang dapat dikonfigurasi |
| **Cache peramban** | Peramban pengguna | ~1 mdtk | Header cache HTTP |
| **Cache kueri basis data** | Tingkat basis data atau ORM | ~1-10 mdtk | Sampai data berubah |
### Pola Caching
| Pola | Deskripsi | Kapan Menggunakan |
|---------|-------------|-------------|
| **Selain cache** | Aplikasi memeriksa cache; memuat dari DB jika terlewat; menyimpan dalam cache | Paling umum; sederhana |
| **Tulis melalui** | Menulis ke cache dan DB secara bersamaan | Saat membaca >> menulis; konsistensi penting |
| **Tulis di belakang** | Menulis ke cache; menulis secara asinkron ke DB | Throughput penulisan yang tinggi; beberapa risiko kehilangan data |
| **TTL (Waktunya untuk Hidup)** | Entri cache kedaluwarsa setelah waktu yang ditentukan | Ketika data berubah secara berkala |
| **Pembatalan** | Hapus entri cache basi secara eksplisit | Ketika Anda tahu persis kapan data berubah |
### Pembatalan Cache
Dua masalah tersulit dalam ilmu komputer: pembatalan cache, penamaan sesuatu, dan kesalahan satu per satu.
| Strategi | Deskripsi |
|----------|-------------|
| **Berbasis TTL** | Entri kedaluwarsa setelah N detik; sederhana namun mungkin menyajikan data basi |
| **Berbasis peristiwa** | Tidak valid ketika data berubah; lebih kompleks tapi akurat |
| **Berbasis versi** | Sertakan nomor versi; kenaikan perubahan |
| **Berbasis tag** | Tandai entri cache terkait; batalkan semua entri dengan tag |
---

## Optimasi Basis Data
Basis data sering kali menjadi hambatan terbesar dalam aplikasi web.
| Teknik | Deskripsi | Dampak |
|-----------|-------------|--------|
| **Pengindeksan** | Tambahkan indeks pada kolom yang digunakan di WHERE, JOIN, ORDER BY | Kueri 10-1000x lebih cepat |
| **Pengoptimalan kueri** | Hindari PILIH *; gunakan EXPLAIN untuk menganalisis kueri | Kurangi I/O |
| **Penggabungan koneksi** | Gunakan kembali koneksi database daripada membuat yang baru | Hilangkan overhead koneksi |
| **Baca replika** | Merutekan kueri baca ke database replika | Distribusikan beban baca |
| **Mempartisi** | Membagi tabel besar menjadi partisi yang lebih kecil | Kueri lebih cepat pada kumpulan data besar |
| **Denormalisasi** | Tambahkan data yang berlebihan untuk menghindari penggabungan | Membaca lebih cepat; menulis lebih lambat |
| **Pandangan yang terwujud** | Hasil kueri yang telah dihitung sebelumnya | Kueri kompleks instan |
| **Pencegahan N+1** | Gunakan GABUNG, pemuatan bersemangat, atau kueri batch | Hilangkan ribuan pertanyaan |
---

## Konkurensi dan Paralelisme
| Konsep | Deskripsi | Kapan Menggunakan |
|---------|-------------|-------------|
| **Mengikat** | Beberapa thread dalam satu proses | Tugas terikat I/O (jaringan, disk) |
| **Multiproses** | Banyak proses (melewati GIL dengan Python) | Tugas yang terikat CPU |
| **Async/menunggu** | Multitugas kooperatif; utas tunggal | I/O konkurensi tinggi (server web) |
| **Komputasi GPU** | Ribuan inti paralel | Operasi matriks; pemrosesan gambar; ml |
### Asinkron vs Threading
| Aspek | Asinkron/Tunggu | Mengulir |
|--------|------------|-----------|
| **Model** | Koperasi (pengendalian hasil tugas) | Preemptive (OS mengganti thread) |
| **Di atas** | Sangat rendah (tidak ada peralihan konteks) | Lebih tinggi (pembuatan thread, peralihan konteks) |
| **Kompleksitas** | Penalaran yang lebih sederhana (utas tunggal) | Kondisi balapan, kebuntuan, terkunci |
| **Terbaik untuk** | Banyak operasi I/O secara bersamaan | Memblokir operasi yang tidak dapat dilakukan async |
| **Batasan** | Tidak dapat menggunakan kode terikat CPU tanpa memblokir | GIL dengan Python membatasi paralelisme yang sebenarnya |
---

## Performa Bagian Depan
| Teknik | Deskripsi | Dampak |
|-----------|-------------|--------|
| **Minifikasi** | Hapus spasi dan persingkat nama variabel | 20-40% file lebih kecil |
| **Bundling** | Gabungkan beberapa file menjadi lebih sedikit permintaan | Lebih sedikit permintaan HTTP |
| **Pemisahan kode** | Muat hanya kode yang diperlukan untuk halaman saat ini | Pemuatan awal lebih cepat |
| **Pemuatan lambat** | Muat gambar dan komponen saat dibutuhkan | Render awal lebih cepat |
| **Pohon gemetar** | Hapus kode yang tidak digunakan dari bundel | Bundel yang lebih kecil |
| **Optimasi gambar** | Gunakan WebP/AVIF; gambar responsif; pemuatan lambat | 50-80% gambar lebih kecil |
| **CDN** | Sajikan aset statis dari server edge | Latensi lebih rendah secara global |
| **HTTP/2 dan HTTP/3** | multipleksing; kompresi tajuk; 0-RTT | Overhead protokol lebih cepat |
| **Pekerja layanan** | Aset cache untuk penggunaan offline; pemberitahuan push | Kunjungan berulang lebih cepat |
---

## Optimasi Memori
| Teknik | Deskripsi |
|-----------|-------------|
| **Penggabungan objek** | Gunakan kembali objek alih-alih membuat objek baru |
| **Streaming** | Memproses data dalam potongan-potongan alih-alih memuat semuanya ke dalam memori |
| **Generator / iterator** | Hasilkan nilai satu per satu alih-alih membuat daftar |
| **File yang dipetakan memori** | Akses file besar tanpa memuat seluruhnya |
| **Penyetelan pengumpulan sampah** | Sesuaikan parameter GC untuk beban kerja Anda |
| **Pilihan struktur data** | Gunakan array alih-alih daftar tertaut untuk lokalitas cache; gunakan set untuk pengujian keanggotaan |
---

## Optimasi Jaringan
| Teknik | Deskripsi |
|-----------|-------------|
| **Kompresi** | gzip, brotli untuk tanggapan HTTP |
| **Penggunaan kembali koneksi** | Koneksi yang tetap hidup; multipleksing HTTP/2 |
| **Permintaan pengelompokan** | Gabungkan beberapa panggilan API menjadi satu |
| **Paginasi** | Muat data dalam halaman, bukan sekaligus |
| **Kompresi saat istirahat** | Kompres data dalam database dan cache |
| **Pilihan protokol** | gRPC (biner, efisien) vs REST (dapat dibaca manusia) |
---

## Pemantauan dan Peringatan
| Metrik | Apa yang Dikatakannya kepada Anda |
|--------|------------------|
| **Latensi P50 / P95 / P99** | Waktu respons pada berbagai persentil |
| **Melalui** | Permintaan per detik |
| **Tingkat kesalahan** | Persentase permintaan yang gagal |
| **Pemanfaatan CPU** | Berapa kapasitas pemrosesan yang digunakan |
| **Penggunaan memori** | konsumsi RAM; mendekati batas? |
| **Waktu kueri basis data** | Kueri lambat yang memerlukan pengoptimalan |
---

## Ringkasan
Optimalisasi kinerja adalah proses yang sistematis: mengukur, mengidentifikasi hambatan, memperbaikinya, mengukur lagi. Kemenangan terbesar datang dari perbaikan algoritmik dan menghilangkan pekerjaan yang tidak perlu — bukan dari optimasi mikro. Caching, pengindeksan database, dan konkurensi adalah alat yang paling ampuh. Performa frontend bergantung pada minimalisasi ukuran muatan dan perjalanan bolak-balik. Dan aturan terpentingnya selalu sama: jangan menebak-nebak — profil.