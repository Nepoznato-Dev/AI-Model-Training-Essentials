<!--
---
# Metadata
title: "Data Pipeline and ETL Failures"
description: "Schema drift, duplicate data, validation gaps, pipeline monitoring"
category: "Lessons from Failures"
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
reviewed_by: "Lessons from Failures Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [data, pipeline, etl, failures, lessons-from-failures]
difficulty_level: "advanced"
prerequisites: []
estimated_reading_time: "5 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Kegagalan Saluran Data dan ETL
Saluran data adalah saluran bagi organisasi modern — saluran ini memindahkan data dari sistem sumber melalui transformasi ke dalam database, gudang, dan danau yang digunakan untuk analisis, pembelajaran mesin, dan pengambilan keputusan. Saat mereka bekerja, tidak ada yang memperhatikan. Ketika mereka gagal, keputusan dibuat berdasarkan data yang sudah usang, model dilatih berdasarkan sampah, laporan menunjukkan angka yang mustahil, dan kepercayaan pada seluruh platform data terkikis. Kegagalan saluran data adalah salah satu kegagalan paling umum dan paling merugikan dalam organisasi teknologi.
---

## Mode Kegagalan Umum
### Masalah Kualitas Data
| Kegagalan | Deskripsi | Dampak | Kesulitan Deteksi |
|---------|-------------|--------|---------------------|
| **Korupsi data senyap** | Data diubah secara tidak benar tanpa ada kesalahan yang dimunculkan | Sistem hilir mempercayai data yang buruk; keputusan berdasarkan informasi palsu | Sangat sulit — tidak ada sinyal kesalahan |
| **Penyimpangan skema** | Skema perubahan sistem sumber (menambah, menghapus, mengganti nama kolom) | Pipeline rusak atau menjatuhkan data secara diam-diam | Sedang — saluran pipa mungkin gagal atau memberikan hasil sebagian |
| **Jenis data tidak cocok** | Sumber mengirimkan string ke tempat bilangan bulat diharapkan; perubahan presisi float | Saluran pipa gagal; data terpotong; kesalahan pembulatan | Sedang — dapat menyebabkan kesalahan saluran atau masalah data yang tidak kentara |
| **Data duplikat** | Acara yang sama diproses beberapa kali | Jumlah yang meningkat; agregasi yang salah | Sulit — setiap catatan terlihat valid satu per satu |
| **Nilai nol/hilang** | Bidang yang diharapkan kosong | Perhitungan gagal; model menghasilkan prediksi yang salah | Sedang — bergantung pada penanganan null |
| **Nilai di luar rentang** | Nilai di luar batas yang diharapkan (usia negatif; tanggal mendatang) | Statistik yang miring; logika bisnis yang rusak | Sedang — memerlukan aturan validasi |
| **Data yang datang terlambat** | Data tiba setelah jendela pemrosesan ditutup | Hasil tidak lengkap; catatan yang terlewat | Sulit — hasil terlihat lengkap tetapi tidak |
### Masalah Infrastruktur Saluran Pipa
| Kegagalan | Deskripsi | Dampak |
|---------|-------------|--------|
| **Kegagalan orkestrasi** | Penjadwal (Aliran Udara, Prefek) tidak memicu saluran pipa | Data sudah basi; tidak ada pemrosesan yang terjadi |
| **Kehabisan sumber daya** | Pipeline kehabisan memori, CPU, atau disk | Kerusakan saluran pipa; hasil parsial |
| **Kegagalan ketergantungan** | Sistem hulu sedang down atau lambat | Pipeline menunggu tanpa batas waktu atau gagal |
| **Masalah konkurensi** | Beberapa saluran pipa mengubah data yang sama secara bersamaan | Kondisi balapan; kerusakan data |
| **Penyimpangan konfigurasi** | Perubahan lingkungan (jaringan, kredensial, titik akhir) tidak tercermin dalam saluran pipa | Saluran pipa gagal tiba-tiba |
| **Tekanan Balik** | Data tiba lebih cepat daripada yang dapat diproses oleh pipeline | Antrean yang bertambah; meningkatkan latensi |
---

## Studi Kasus
### Studi Kasus 1: Duplikasi Data Senyap
| Aspek | Deskripsi |
|--------|-------------|
| **Skenario** | Saluran pesanan perusahaan e-niaga memproses peristiwa dari antrean pesan |
| **Apa yang salah** | Pengulangan ulang konsumen menyebabkan pesan dikonsumsi kembali; tidak ada logika deduplikasi |
| **Dampak** | Angka pendapatan meningkat sebesar 15% selama 3 minggu sebelum ada yang menyadarinya |
| **Akar penyebab** | Tidak ada kunci idempotensi; setidaknya sekali pengiriman tanpa deduplikasi |
| **Perbaiki** | Menambahkan kunci idempotensi berdasarkan ID pesanan; mengimplementasikan semantik tepat sekali |
| **Pelajaran** | Pengiriman setidaknya sekali memerlukan deduplikasi; selalu memvalidasi total terhadap sistem sumber |
### Studi Kasus 2: Perubahan Skema Terganggu di Hilir
| Aspek | Deskripsi |
|--------|-------------|
| **Skenario** | Penyedia pembayaran mengubah nama bidang dalam respons API mereka |
| **Apa yang salah** | Pipeline ETL secara diam-diam mulai menulis nilai null; tidak ada validasi skema |
| **Dampak** | Laporan keuangan menunjukkan pendapatan nol dari metode pembayaran tersebut selama 2 bulan |
| **Akar penyebab** | Tidak ada validasi skema saat penyerapan; nilai nol diperlakukan sebagai valid |
| **Perbaiki** | Menambahkan validasi skema dengan peringatan; bidang wajib ditegakkan; pemeriksaan nol |
| **Pelajaran** | Jangan pernah mempercayai skema eksternal untuk tetap stabil; validasi di batas |
### Studi Kasus 3: Bencana Zona Waktu
| Aspek | Deskripsi |
|--------|-------------|
| **Skenario** | Perusahaan global mengumpulkan metrik harian di seluruh kantor |
| **Apa yang salah** | Beberapa sumber menggunakan UTC, sumber lainnya menggunakan waktu setempat; pipa tidak normal |
| **Dampak** | Total harian tidak cocok; beberapa transaksi dihitung pada hari yang salah; penutupan akhir bulan salah |
| **Akar penyebab** | Tidak ada kebijakan zona waktu standar; stempel waktu disimpan secara tidak konsisten |
| **Perbaiki** | Semua cap waktu disimpan sebagai UTC; konversi ke waktu lokal hanya pada lapisan presentasi |
| **Pelajaran** | Standarisasi pada UTC di mana pun; bersikap eksplisit tentang zona waktu di setiap batas |
---

## Strategi Pencegahan
### Validasi Data
| Strategi | Deskripsi | Contoh Alat |
|----------|-------------|---------------|
| **Validasi skema** | Verifikasi data sesuai dengan skema yang diharapkan pada setiap tahap | Besar harapan; Deequ; soda |
| **Pemeriksaan rentang** | Nilai berada dalam batas yang diharapkan | Pernyataan khusus; tes dbt |
| **Pemeriksaan kesegaran** | Data cukup terkini sehingga berguna | Memantau stempel waktu; Peringatan SLA |
| **Pemeriksaan volume** | Jumlah baris berada dalam kisaran yang diharapkan | Deteksi anomali pada jumlah baris |
| **Integritas referensial** | Kunci asing cocok; tidak ada catatan yatim piatu | kendala SQL; alat kualitas data |
| **Rekonsiliasi lintas sumber** | Total cocok antara sumber dan target | Pekerjaan rekonsiliasi otomatis |
### Pola Desain Saluran Pipa
| Pola | Deskripsi | Manfaat |
|---------|-------------|---------|
| **Idempotensi** | Menjalankan pipeline beberapa kali menghasilkan hasil yang sama | Aman untuk mencoba lagi; tidak ada duplikat |
| **Atomisitas** | Pipeline berhasil sepenuhnya atau gagal sepenuhnya (tidak ada sebagian keadaan) | Tidak ada data yang setengah diproses |
| **Titik pemeriksaan** | Simpan kemajuan di setiap tahap; melanjutkan dari pos pemeriksaan terakhir | Toleransi kesalahan; tidak ada pemrosesan ulang |
| **Antrian surat mati** | Catatan yang gagal dimasukkan ke antrian terpisah untuk diselidiki | Tidak ada kehilangan data; dapat menyelidiki dan memutar ulang |
| **Pemutus arus** | Hentikan pemrosesan ketika downstream gagal | Mencegah kegagalan berjenjang |
| **Kontrak data** | Kesepakatan antara produsen dan konsumen tentang format data | Perubahan skema dikoordinasikan |
### Pemantauan dan Peringatan
| Apa yang Harus Dipantau | Mengapa | Bagaimana |
|-----------------|-----|-----|
| **Durasi saluran** | Peningkatan durasi menandakan masalah | Analisis tren; Pelacakan SLA |
| **Jumlah baris** | Perubahan mendadak menunjukkan masalah | Bandingkan dengan rata-rata historis |
| **Tarif nol** | Meningkatkan skema sinyal nol atau masalah sumber | Pelacakan nol tingkat kolom |
| **Kesegaran data** | Data basi berarti saluran pipa tidak berjalan | Stempel waktu rekor terbaru |
| **Dampak hilir** | Apakah laporan dan model menggunakan data yang benar? | Silsilah data ujung ke ujung |
| **Penggunaan sumber daya** | CPU; ingatan; cakram; jaringan | Pemantauan infrastruktur |
---

## Strategi Pemulihan
| Situasi | Strategi |
|-----------|----------|
| **Data buruk sudah ada di gudang** | Identifikasi rentang waktu yang terpengaruh; memproses ulang dari sumber; memberitahukan konsumen hilir |
| **Kegagalan saluran pipa di tengah proses** | Desain idempoten memungkinkan pengoperasian kembali dengan aman; pos pemeriksaan memungkinkan melanjutkan |
| **Perubahan skema menyebabkan kerusakan saluran** | Perbaiki transformasi; pengisian ulang data yang terkena dampak; tambahkan penanganan evolusi skema |
| **Korupsi diam-diam terlambat ditemukan** | Analisis akar permasalahan; menentukan radius ledakan; memproses ulang; tambahkan pemantauan untuk menangkap kekambuhan |
| **Kehilangan data** | Pulihkan dari cadangan; memutar ulang dari sumber; menilai apakah kerugian dapat dipulihkan |
---

## Ringkasan
Kegagalan saluran data terjadi di mana-mana dan sering kali lebih mahal dibandingkan penghentian aplikasi karena menghasilkan jawaban yang salah dibandingkan kesalahan yang nyata. Kerusakan data diam-diam, penyimpangan skema, duplikat, bug zona waktu, dan nilai yang hilang adalah penyebab paling umum. Strategi pencegahan utama adalah: memvalidasi data pada setiap batasan (skema, rentang, volume, kesegaran); merancang saluran pipa menjadi idempoten dan atomik; pantau semuanya (durasi, jumlah baris, tarif nol, kesegaran); menggunakan antrian surat mati untuk catatan yang gagal; dan menetapkan kontrak data antara produsen dan konsumen. Ketika kegagalan terjadi, responsnya harus mencakup analisis akar permasalahan, pemrosesan ulang data yang terkena dampak, pemberitahuan kepada konsumen hilir, dan – yang terpenting – menambahkan pemantauan untuk mendeteksi jenis kegagalan yang sama di masa mendatang. Organisasi yang melakukan hal ini dengan benar memperlakukan saluran data dengan ketelitian yang sama seperti perangkat lunak produksi: pengujian, pemantauan, peringatan, respons insiden, dan pemeriksaan mayat.