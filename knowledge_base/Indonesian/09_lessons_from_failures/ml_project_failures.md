---
# Metadata
title: "Machine Learning Project Failures"
description: "Data leakage, expectation mismatches, deployment failures, model decay"
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
tags: [ml, project, failures, lessons-from-failures]
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

# Kegagalan Proyek Pembelajaran Mesin
Proyek pembelajaran mesin mengalami kegagalan pada tingkat yang mengkhawatirkan — perkiraan industri menunjukkan 60-85% proyek ML tidak pernah mencapai produksi. Kegagalan biasanya tidak terjadi pada algoritme; mereka sedang dalam proses, data, harapan, dan konteks organisasi. Memahami mengapa proyek ML gagal sangat penting bagi siapa pun yang membangun sistem ML, karena mode kegagalan dapat diprediksi dan sebagian besar dapat dihindari.
---

## Mengapa Proyek ML Gagal
### Kategori Kegagalan
| Kategori | Pangsa Kegagalan | Deskripsi |
|----------|------------------|-------------|
| **Masalah data** | ~30% | Data tidak mencukupi, bias, basi, atau tidak dapat diakses |
| **Definisi masalah** | ~20% | Masalah ML Tidak Sesuai Kebutuhan Bisnis |
| **Ketidaksesuaian ekspektasi** | ~15% | Para pemangku kepentingan mengharapkan keajaiban; kenyataannya adalah perbaikan bertahap |
| **Kegagalan penerapan** | ~15% | Model berfungsi di buku catatan tetapi tidak dapat diproduksi |
| **masalah organisasi** | ~10% | Tidak ada kepemilikan yang jelas; tim tidak memiliki keterampilan; tidak ada dukungan eksekutif |
| **Performa model** | ~10% | Model tidak mencapai akurasi yang diperlukan atau menggeneralisasi dengan buruk |
---

## Kegagalan Terkait Data
### Masalah Data Umum
| Masalah | Deskripsi | Contoh |
|---------|-------------|---------|
| **Data tidak mencukupi** | Tidak cukup contoh untuk mempelajari pola yang bermakna | Pelatihan model deteksi penipuan pada 500 transaksi |
| **Kualitas label** | Label pelatihan salah, tidak konsisten, atau subyektif | Gambar medis yang diberi label oleh non-ahli; label sentimen dengan kesepakatan antar penilai yang rendah |
| **Kebocoran data** | Informasi dari masa depan atau target bocor ke dalam fitur | Menggunakan hasil churn pelanggan sebagai fitur; termasuk data uji dalam pelatihan |
| **Bias seleksi** | Data pelatihan tidak mewakili populasi penerapan | Melatih model medis berdasarkan data dari satu rumah sakit; disebarkan secara nasional |
| **Penyimpangan konsep** | Hubungan antara fitur dan target berubah seiring waktu | Perubahan perilaku konsumen setelah pandemi; model yang dilatih berdasarkan data pra-pandemi |
| **Ketidakcocokan fitur** | Fitur yang tersedia selama pelatihan berbeda dengan yang tersedia di produksi | Pelatihan dengan label manual; produksi menggunakan label otomatis dengan distribusi berbeda |
| **Ketidakseimbangan kelas** | Kelas sasaran sangat tidak seimbang | 99% negatif, 1% positif; model belajar untuk selalu memprediksi negatif |
### Masalah Kebocoran Data
| Ketik | Deskripsi | Contoh |
|------|-------------|---------|
| **Target kebocoran** | Sebuah fitur hanya tersedia setelah target terjadi | "Hasil pengobatan" digunakan sebagai fitur untuk memprediksi "keberhasilan pengobatan" |
| **Kontaminasi uji kereta** | Data pengujian mempengaruhi pelatihan | Penskalaan dengan statistik global (termasuk data pengujian); augmentasi data yang bocor |
| **Bias pengambilan sampel** | Pelatihan dan produksi menggunakan sampling yang berbeda | Pelatihan lalu lintas web; penerapan pada lalu lintas aplikasi seluler |
| **Kebocoran pra-pemrosesan** | Langkah prapemrosesan menggunakan informasi dari dataset lengkap | Menghitung nilai yang hilang dengan mean global (termasuk data pengujian) |
---

## Definisi Masalah Kegagalan
### Pola Ketidaksejajaran
| Pola | Deskripsi | Konsekuensi |
|---------|-------------|-------------|
| **Memecahkan masalah yang salah** | Kebutuhan bisnis X; membangun tim Y | Model secara teknis bagus tetapi tidak berguna |
| **ML jika aturan sudah mencukupi** | Masalah mempunyai aturan deterministik; ML menambah kompleksitas | Direkayasa secara berlebihan; lebih sulit untuk dipertahankan; kurang bisa ditafsirkan |
| **ML bila data tidak ada** | Soal memerlukan data yang belum dikumpulkan | Proyek tidak dapat dimulai; bulan terbuang untuk kelayakan |
| **Target akurasi tanpa konteks bisnis** | "Kami memerlukan akurasi 95%" — namun apa pengaruhnya bagi bisnis? | Model memenuhi akurasi tetapi tidak menyelesaikan masalah bisnis |
| **Mengabaikan biaya kesalahan** | Positif palsu dan negatif palsu memiliki biaya yang berbeda | Model mengoptimalkan metrik yang salah |
| **Tidak ada dasar** | Tidak ada perbandingan dengan pendekatan yang ada | Tidak tahu apakah ML sebenarnya lebih baik daripada heuristik sederhana |
---

## Kegagalan Ekspektasi
### Siklus Hype dalam Proyek ML
| Fase | Deskripsi | Resiko |
|-------|-------------|------|
| **Kegembiraan** | "AI akan menyelesaikan semuanya!" | Terlalu menjanjikan; kekurangan sumber daya |
| **Bukti konsep** | Model bekerja pada data bersih di buku catatan | Keyakinan yang salah; "berhasil!" |
| **Pemeriksaan realitas** | Data produksi berantakan; kinerja turun | Kekecewaan; "ML tidak berfungsi" |
| **Pawai kematian** | Tim mencoba memaksanya masuk ke produksi | Hutang teknis; kelelahan |
| **Pengabaian atau penerapan senyap** | Proyek dibatalkan atau diterapkan tanpa pemantauan | Investasi yang sia-sia |
### Mengelola Harapan
| Strategi | Deskripsi |
|----------|-------------|
| **Mulai dengan dasar** | Bandingkan dengan pendekatan yang paling sederhana (aturan; kinerja manusia) |
| **Tentukan metrik keberhasilan di awal** | Metrik bisnis (pendapatan; penghematan biaya) bukan hanya metrik ML (akurasi; F1) |
| **Eksplorasi kotak waktu** | Beri tim waktu 2-4 minggu untuk menilai kelayakan sebelum melakukan |
| **Tunjukkan apa yang tidak bisa dilakukan ML** | Jujurlah tentang keterbatasan; tetapkan harapan yang realistis |
| **Iterasi secara bertahap** | Terapkan model sederhana terlebih dahulu; tingkatkan secara berulang |
| **Hitung biaya kesalahan** | Terjemahkan kinerja model menjadi dampak bisnis |
---

## Kegagalan Penerapan
### Mengapa Model Tidak Sampai Produksi
| Masalah | Deskripsi | Solusi |
|---------|-------------|----------|
| **Kesenjangan notebook dan produksi** | Kode berfungsi di Jupyter tetapi belum siap produksi | praktik MLOps; CI/CD untuk ML; ulasan kode |
| **Persyaratan latensi** | Inferensi model terlalu lambat untuk penggunaan waktu nyata | Optimasi model; kuantisasi; cache |
| **Skalabilitas** | Model tidak dapat menangani lalu lintas produksi | Pemrosesan batch; penskalaan horizontal; model melayani infrastruktur |
| **Memantau kesenjangan** | Tidak ada cara untuk mendeteksi kapan model mengalami penurunan | Pemantauan penyimpangan data; pemantauan kinerja; memperingatkan |
| **Manajemen ketergantungan** | Lingkungan pelatihan dan penyajian berbeda | Kontainerisasi; lingkungan yang dapat direproduksi |
| **Tidak ada rencana pengembalian** | Tidak dapat kembali ke model sebelumnya jika model baru gagal | Registri model; pembuatan versi; pengembalian otomatis |
### Model Peluruhan
| Ketik | Deskripsi | Deteksi |
|------|-------------|-----------|
| **Penyimpangan data** | Distribusi fitur masukan berubah | Pantau statistik fitur; divergensi KL; PSI |
| **Penyimpangan konsep** | Hubungan antara fitur dan perubahan target | Pantau keakuratan prediksi dari waktu ke waktu |
| **Label melayang** | Definisi atau sebaran sasaran perubahan | Distribusi label lagu; korelasi metrik bisnis |
| **Perubahan hulu** | Sumber data mengubah format, waktu, atau kualitas | Validasi skema; pemantauan kesegaran |
---

## Kegagalan Organisasi
| Kegagalan | Deskripsi | Pencegahan |
|---------|-------------|------------|
| **Tidak ada kepemilikan yang jelas** | Tidak ada yang bertanggung jawab atas model dalam produksi | Tetapkan pemilik model; tentukan RACI |
| **Tim yang terisolasi** | Ilmuwan data membuat model; penempatan insinyur; tidak ada yang berkomunikasi | Tim lintas fungsi; tujuan bersama |
| **Tidak ada jatuh tempo MLOps** | Tidak ada registri model; tidak ada CI/CD; tidak ada pemantauan | Berinvestasi dalam infrastruktur MLOps secara bertahap |
| **Jadwal yang tidak realistis** | "Bangun sistem ML produksi dalam 2 minggu" | Eksplorasi kotak waktu; ulangi; mengkomunikasikan kompleksitas |
| **Kurangnya keahlian domain** | Tim ML tidak memahami masalah bisnis | Sematkan pakar domain di tim ML |
| **Tidak ada kerangka evaluasi** | Tidak tahu apakah model tersebut berfungsi dalam produksi | Tentukan metrik bisnis; mengatur dasbor; ulasan reguler |
---

## Pelajaran yang Dipetik
### Daftar Periksa Proyek ML
| Fase | Pertanyaan Kunci |
|-------|-------------|
| **Definisi masalah** | Apakah ini sebenarnya masalah ML? Apa dasarnya? Seperti apa kesuksesan itu? |
| **Penilaian data** | Apakah kita memiliki cukup data? Apakah ini representatif? Apakah label dapat diandalkan? |
| **Kelayakan** | Bisakah kita membuat prototipe yang berfungsi dalam 2-4 minggu? Apa risikonya? |
| **Pengembangan** | Apakah ada kebocoran data? Apakah kita menggunakan metrik evaluasi yang tepat? |
| **Pra-produksi** | Apakah ini berfungsi dengan data produksi? Apakah cukup cepat? Apakah itu dipantau? |
| **Penerapan** | Bisakah kita mundur? Siapa yang siap dihubungi? Apa yang terjadi jika kualitasnya menurun? |
| **Pasca penerapan** | Apakah kita memantau penyimpangan? Apakah metrik bisnis dilacak? Apakah ada rencana pelatihan ulang? |
---

## Ringkasan
Proyek ML gagal bukan karena algoritmenya terlalu keras, namun karena proses di sekitarnya rusak. Masalah data — data yang tidak mencukupi, label yang buruk, kebocoran, penyimpangan — merupakan penyebab terbesar kegagalan. Kegagalan definisi masalah - menyelesaikan masalah yang salah, menggunakan ML ketika aturan sudah mencukupi, mengabaikan akibat dari kesalahan - membuang-buang usaha selama berbulan-bulan. Kegagalan ekspektasi — memberikan janji yang berlebihan, tidak memberikan hasil, dan tidak mengelola pemangku kepentingan — menghancurkan kepercayaan organisasi terhadap ML. Kegagalan penerapan — kesenjangan notebook-ke-produksi, masalah latensi, tidak adanya pemantauan — berarti model yang berfungsi dalam pengembangan tidak pernah menciptakan nilai dalam produksi. Kegagalan organisasi — tidak ada kepemilikan, tim yang terisolasi, tidak ada MLOps — membuat kesuksesan secara struktural tidak mungkin tercapai. Penawarnya adalah praktik disiplin: mulailah dengan dasar; eksplorasi kotak waktu; memvalidasi data secara ketat; periksa kebocoran; menentukan metrik bisnis; menyebarkan secara bertahap; memantau secara terus menerus; dan ulangi. Tim ML terbaik menghabiskan lebih banyak waktu pada data dan proses dibandingkan pada model.