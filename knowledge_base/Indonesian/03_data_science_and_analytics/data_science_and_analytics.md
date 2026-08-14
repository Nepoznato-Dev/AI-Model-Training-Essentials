---
# Metadata
title: "Data Science and Analytics"
description: "Data processing, ML, big data, BI"
category: "Data Science and Analytics"
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
reviewed_by: "Data Science & Analytics Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [data, science, analytics, data-science-and-analytics]
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
# Ilmu Data dan Analisis
Ilmu data adalah disiplin mengubah data mentah menjadi wawasan yang dapat ditindaklanjuti. Hal ini merupakan titik temu antara statistik, ilmu komputer, dan keahlian domain — dan hal ini menjadi hal yang penting di setiap sektor, mulai dari keuangan hingga layanan kesehatan. File ini menjelaskan konsep inti, alat, dan alur kerja yang harus diketahui oleh setiap praktisi.
---

## Proses Ilmu Data
Sebagian besar proyek mengikuti beberapa variasi **CRISP-DM**, siklus hidup standar industri:
| Fase | Apa yang Terjadi | Waktu Khas |
|-------|-------------|--------------|
| **Pemahaman Bisnis** | Tentukan tujuan, metrik keberhasilan, dan kendala | 10–15% |
| **Pemahaman Data** | Kumpulkan, jelajahi, dan buat profil data | 10–15% |
| **Persiapan Data** | Bersihkan, ubah, rekayasa fitur | ~50–60% |
| **Pemodelan** | Pilih dan latih model | 10–15% |
| **Evaluasi** | Menilai kinerja terhadap tujuan bisnis | 5–10% |
| **Penerapan** | Kirim model ke produksi | 5–10% |
Persiapan data, khususnya pembersihan data, diperkirakan menghabiskan sekitar 80% waktu data scientist.
---

## Sekilas Tipe Data
| Ketik | Deskripsi | Contoh |
|------|-------------|---------|
| **Terstruktur** | Disusun dalam baris dan kolom | Tabel SQL, spreadsheet |
| **Tidak terstruktur** | Tidak ada format standar | Teks, gambar, audio, video |
| **Semi-terstruktur** | Beberapa organisasi tetapi fleksibel | JSON, XML, HTML |
| **Rangkaian waktu** | Data berurutan diindeks berdasarkan waktu | Harga saham, pembacaan sensor |
| **Spasial** | Berbasis geografis atau lokasi | Koordinat GPS, data peta |
| **Grafik** | Node dan edge mewakili hubungan | Jejaring sosial, grafik pengetahuan |
---

## Dasar-Dasar Statistik
### Statistik Deskriptif vs Inferensial
Statistik deskriptif merangkum apa yang Anda *miliki*; statistik inferensial memungkinkan Anda menarik kesimpulan tentang apa yang *tidak* Anda miliki (populasi yang lebih luas).
| Konsep | Ide Utama |
|---------|-----------|
| **Kecenderungan sentral** | Mean (sensitif terhadap outlier), median (kuat), mode (paling sering) |
| **Dispersi** | Jangkauan, varians, simpangan baku, jangkauan antarkuartil |
| **Bentuk distribusi** | Skewness (asimetri), kurtosis (ekor berat) |
| **Pengujian hipotesis** | Hipotesis nol vs alternatif, nilai p, tingkat signifikansi (α) |
| **Interval kepercayaan** | Rentang kemungkinan berisi parameter populasi sebenarnya |
| **Kesalahan Tipe I / Tipe II** | Positif palsu (menolak nol yang sebenarnya) / negatif palsu (tidak ada efek nyata) |
### Tes Statistik Umum
| Tes | Kapan Menggunakan |
|------|-------------|
| **uji-t** | Bandingkan rata-rata antara dua kelompok |
| **ANOVA** | Bandingkan rata-rata pada tiga kelompok atau lebih |
| **Chi-kuadrat** | Uji independensi variabel kategori |
| **Mann-Whitney U** | Alternatif non parametrik uji t (tidak ada asumsi normalitas) |
| **Korelasi Pearson** | Hubungan linier antara dua variabel kontinu |
| **Korelasi Spearman** | Hubungan monoton (berbasis peringkat, lebih kuat) |
### Distribusi Probabilitas yang Perlu Diketahui
| Distribusi | Kasus Penggunaan |
|-------------|----------|
| **Biasa** | Fenomena alam, kesalahan pengukuran — kurva lonceng klasik |
| **Binomial** | Jumlah keberhasilan/kegagalan (pembalikan koin, tingkat konversi) |
| **Racun** | Jumlah kejadian dalam interval tetap (panggilan per jam, kerusakan per batch) |
| **Eksponensial** | Waktu antar peristiwa (waktu tunggu, interval kegagalan) |
| **t-Distribusi** | Sampel kecil atau varians populasi tidak diketahui |
| **Chi-kuadrat** | Analisis data kategorikal, uji kesesuaian |
---

## Pengumpulan dan Penyimpanan Data
### Dari Mana Data Berasal
Data dunia nyata berasal dari banyak sumber: database relasional, API (REST, GraphQL), file datar (CSV, JSON, Parket), platform streaming (Kafka, Kinesis), survei, dan repositori publik (Kaggle, portal pemerintah). Format yang Anda terima menentukan sebagian besar strategi prapemrosesan Anda.
### Konsep Pergudangan Data
| Konsep | Deskripsi |
|---------|-------------|
| **ETL** | Ekstrak → Transformasi → Muat — pendekatan jalur pipa tradisional |
| **ELT** | Ekstrak → Muat → Transformasi — pendekatan cloud modern (muat mentah, transformasi dalam gudang) |
| **Danau Data** | Data mentah disimpan dalam format asli (skema-on-read) |
| **Gudang Data** | Data terstruktur dan diproses yang dioptimalkan untuk analisis (skema-on-write) |
| **DataMart** | Subset gudang, tercakup dalam satu departemen atau domain |
| **Skema Bintang** | Tabel fakta pusat dikelilingi oleh tabel dimensi |
| **Skema Kepingan Salju** | Tabel dimensi yang dinormalisasi (lebih sedikit redundansi, lebih banyak gabungan) |
### Jenis Basis Data
| Ketik | Contoh | Terbaik Untuk |
|------|----------|----------|
| **Relasional (SQL)** | PostgreSQL, MySQL, Oracle | Data terstruktur, transaksi ACID |
| **Dokumen** | MongoDB, SofaDB | Skema fleksibel, data seperti JSON |
| **Nilai-Kunci** | Redis, DynamoDB | Caching, sesi, pencarian sederhana |
| **Kolom-Keluarga** | Cassandra, HBase | Beban kerja tulis-berat, deret waktu |
| **Grafik** | Neo4j, Amazon Neptunus | Hubungan, jejaring sosial |
| **Rangkaian Waktu** | InfluxDB, TimescaleDB | Metrik IoT, pemantauan |
| **Vektor** | Biji Pinus, Milvus | Menyematkan penyimpanan untuk pencarian ML/AI |
---

## Pemrosesan Awal Data dan Rekayasa Fitur
### Daftar Periksa Pembersihan
Setiap kumpulan data nyata memiliki masalah. Inilah pembersihan standar:
| Edisi | Pendekatan |
|-------|----------|
| **Nilai tidak ada** | Imputasi (rata-rata, median, prediksi), atau penghapusan jika jarang |
| **Pencilan** | Deteksi melalui IQR atau Z-score; obati dengan capping atau transformasi |
| **Duplikat** | Identifikasi dan hapus |
| **Inkonsistensi** | Standarisasi format, perbaiki kesalahan ketik, normalkan unit |
### Teknik Transformasi
| Teknik | Apa Fungsinya |
|-----------|-------------|
| **Normalisasi** | Menskalakan nilai ke rentang 0–1 |
| **Standarisasi** | Skor Z: mean = 0, std = 1 |
| **Encoding satu-panas** | Mengonversi kategori menjadi kolom biner |
| **Pengkodean label** | Menetapkan label bilangan bulat ke kategori |
| **Transformasi log** | Mengurangi kemiringan kanan pada data |
| **Pengelompokan** | Mengelompokkan nilai kontinu ke dalam keranjang diskrit |
### Rekayasa Fitur
Rekayasa fitur sering kali menjadi pembeda antara model biasa-biasa saja dan model hebat. Teknik utama meliputi:
- **Pembuatan fitur**: Mendapatkan kolom baru dari kolom yang sudah ada (misalnya,`age_group`dari`age`).
- **Pemilihan fitur**: Metode filter (korelasi), metode pembungkus (eliminasi rekursif), metode tersemat (LASSO, kepentingan pohon).
- **Pengurangan dimensi**: PCA untuk linier, t-SNE atau UMAP untuk visualisasi.
- **Istilah interaksi**: Menggabungkan fitur secara multiplikatif untuk menangkap efek gabungan.
---

## Analisis Data Eksplorasi (EDA)
EDA adalah tempat Anda mengembangkan intuisi tentang data Anda sebelum membuat model. Tujuannya adalah untuk menemukan pola, anomali, dan hubungan.
### Memilih Grafik yang Tepat
| Jenis Bagan | Terbaik Untuk |
|-----------|----------|
| **Histogram** | Distribusi variabel tunggal |
| **Plot kotak** | Ringkasan lima angka, deteksi outlier |
| **Plot sebar** | Hubungan antara dua variabel kontinu |
| **Peta Panas** | Matriks korelasi, visualisasi kepadatan |
| **Diagram batang** | Membandingkan kategori |
| **Bagan garis** | Tren dari waktu ke waktu |
| **Plot biola** | Kepadatan distribusi + ringkasan plot kotak |
| **Plot berpasangan** | Ikhtisar singkat semua pasangan variabel |
### Tumpukan Python EDA
| Perpustakaan | Peran |
|---------|------|
| **panda** | Manipulasi dan analisis data |
| **numpy** | Komputasi numerik |
| **matplotlib** | Perencanaan pondasi |
| **lahir di laut** | Visualisasi statistik (dibangun di matplotlib) |
| **secara plot** | Visualisasi interaktif berbasis web |
| **licin** | Komputasi ilmiah dan statistik |
---

## Pembelajaran Mesin dalam Ilmu Data
### Sekilas tentang Pembelajaran yang Diawasi
| Tugas | Algoritma |
|------|-----------|
| **Regresi** (memprediksi angka) | Linear, Ridge/LASSO, Pohon Keputusan, Hutan Acak, Peningkatan Gradien (XGBoost, LightGBM) |
| **Klasifikasi** (memprediksi suatu kategori) | Regresi Logistik, k-NN, Naive Bayes, SVM, Pohon Keputusan, Hutan Acak, Jaringan Syaraf Tiruan |
### Sekilas tentang Pembelajaran Tanpa Pengawasan
| Tugas | Algoritma |
|------|-----------|
| **Pengelompokan** | k-Means, Hierarki, DBSCAN, Model Campuran Gaussian |
| **Pengurangan Dimensi** | PCA, t-SNE, UMAP, Autoencoder |
| **Peraturan Asosiasi** | Apriori, FP-Pertumbuhan |
### Evaluasi Model
| Tipe Metrik | Metrik Utama |
|-------------|-------------|
| **Klasifikasi** | Akurasi, presisi, perolehan, skor F1, ROC-AUC, matriks kebingungan |
| **Regresi** | MAE, MSE, RMSE, R², R² Disesuaikan |
| **Validasi** | validasi silang k-fold, bertingkat, pembagian deret waktu |
| **Penyetelan** | Pencarian grid, pencarian acak, optimasi Bayesian |
---

## Teknologi Data Besar
Ketika kumpulan data melebihi apa yang dapat ditangani oleh satu mesin, komputasi terdistribusi akan ikut berperan.
| Kerangka | Kekuatan |
|-----------|----------|
| **Apache Spark** | Pemrosesan dalam memori; Percikan SQL, Streaming, MLlib, GraphX ​​|
| **Apache Hadoop** | MapReduce + HDFS — tumpukan data besar asli |
| **Apache Flink** | Pemrosesan aliran latensi rendah |
| **Sinar Apache** | Model batch dan streaming terpadu |
### Platform Data Awan
| Penyedia | Layanan Utama |
|----------|-------------|
| **AWS** | S3, EMR, Redshift, SageMaker, Lem |
| **Google Awan** | BigQuery, Dataproc, Platform AI, Penyimpanan Cloud |
| **Azure** | Synapse Analytics, Databricks, Pembelajaran Mesin, Data Lake |
| **Kepingan Salju** | Gudang data cloud-native (penyedia-agnostik) |
### Orkestrasi Saluran Pipa
| Alat | Catatan |
|------|-------|
| **Aliran Udara Apache** | standar industri; DAG berbasis Python |
| **Prefek** | Alternatif modern dengan API yang lebih bersih |
| **Belati** | Orkestrasi yang berpusat pada aset |
| **dbt** | Transformasi data SQL-pertama di gudang |
---

## Intelijen Bisnis dan Analisis
### Alat BI Dibandingkan
| Alat | Ketik | Kekuatan |
|------|------|----------|
| **Tabel** | Komersial | Analisis visual yang kaya, drag-and-drop |
| **Kekuatan BI** | Komersial (Microsoft) | Integrasi Office/Azure yang mendalam |
| **Penampil** | Komersial (Google) | Eksplorasi data, pemodelan LookML |
| **Metabase** | Sumber terbuka | Pengaturan mudah, SQL-asli |
| **Superset** | Sumber terbuka (Apache) | Dapat diskalakan, SQL-pertama |
### Prinsip Desain Dasbor
Dasbor yang efektif mengikuti prinsip-prinsip yang telah ditetapkan: mengidentifikasi audiens, memilih visualisasi yang sesuai untuk setiap metrik, menggunakan warna secara strategis (bukan dekoratif), mempertahankan skala yang konsisten, dan memungkinkan interaktivitas (filter, penelusuran). Performa juga penting — dasbor dengan waktu muat yang lambat mengurangi adopsi pengguna.
### Kategori KPI Umum
| Kategori | Contoh |
|----------|---------|
| **Keuangan** | Pendapatan, margin keuntungan, ROI, nilai seumur hidup pelanggan |
| **Pelanggan** | Biaya akuisisi (CAC), churn rate, NPS, skor kepuasan |
| **Operasional** | Tingkat efisiensi, waktu siklus, tingkat kerusakan |
| **Pemasaran** | Rasio konversi, rasio klik-tayang, ROAS, atribusi |
| **Produk** | Pengguna aktif harian, keterlibatan, retensi, adopsi fitur |
---

## Analisis Tingkat Lanjut
| Pendekatan | Teknik | Kapan Menggunakan |
|----------|-----------|-------------|
| **Prediktif** | Rangkaian waktu (ARIMA, Prophet, LSTM), pemodelan risiko, prediksi churn | Meramalkan nilai masa depan |
| **Preskriptif** | Pemrograman linier, simulasi Monte Carlo, pengujian A/B, bandit multi-bersenjata | Mengoptimalkan keputusan |
| **Analisis Teks** | Tokenisasi, analisis sentimen, pemodelan topik (LDA), NER, penyematan kata (Word2Vec, BERT) | Mengekstraksi wawasan dari teks |
---

## Etika dan Tata Kelola Data
### Peraturan Privasi
| Peraturan | Ruang Lingkup |
|-----------|-------|
| **GDPR** | Subjek data UE; hak atas penghapusan, persetujuan, portabilitas data |
| **CCPA** | Konsumen Kalifornia; menyisih dari penjualan data |
| **HIPAA** | data layanan kesehatan AS; aturan kerahasiaan yang ketat |
### Dimensi Kualitas Data
| Dimensi | Pertanyaan |
|-----------|----------|
| **Akurasi** | Apakah datanya benar? |
| **Kelengkapan** | Apakah ada yang hilang? |
| **Konsistensi** | Apakah sumber setuju? |
| **Ketepatan waktu** | Apakah ini terkini? |
| **Validitas** | Apakah itu sesuai dengan format yang diharapkan? |
| **Keunikan** | Apakah ada duplikat? |
### Bias dan Keadilan
Bias dapat terjadi pada tahap apa pun: bias pengambilan sampel (data yang tidak representatif), bias pengukuran (instrumen yang cacat), atau bias algoritmik (prediksi diskriminatif). Strategi mitigasi mencakup pra-pemrosesan (memperbaiki data), dalam pemrosesan (membatasi model), dan pasca-pemrosesan (menyesuaikan keluaran). Metrik keadilan seperti kesetaraan demografi dan kesetaraan kesempatan membantu mengukur permasalahan yang ada.
---

## Jalur Karir
| Peran | Fokus |
|------|-------|
| **Analis Data** | Analisis deskriptif, dasbor, pelaporan |
| **Ilmuwan Data** | Pemodelan statistik, ML, analitik tingkat lanjut |
| **Insinyur ML** | Sistem ML produksi, penerapan model, MLOps |
| **Insinyur Data** | Saluran data, infrastruktur, ETL |
| **Manajer Analytics** | Kepemimpinan tim, strategi, manajemen pemangku kepentingan |
| **Ilmuwan Riset** | Algoritma baru, publikasi |
---

## Tren yang Muncul
- **AutoML**: Pembuatan pipeline otomatis dan pemilihan model.
- **MLOps**: Praktik DevOps diterapkan pada manajemen siklus hidup ML.
- **Penyimpanan Fitur**: Manajemen fitur terpusat untuk digunakan kembali di seluruh tim.
- **Data Mesh**: Arsitektur data milik domain yang terdesentralisasi.
- **LLM dan AI Generatif**: Model bahasa besar yang mengubah alur kerja teks, kode, dan gambar.
- **Edge Analytics**: Memproses data di perangkat, bukan di cloud.
- **Inferensi Kausal**: Beralih melampaui korelasi untuk memahami sebab dan akibat yang sebenarnya.
- **Pembelajaran Federasi**: Melatih model di seluruh data yang terdesentralisasi tanpa memindahkannya.
- **AI yang bertanggung jawab**: Etika, kemampuan menjelaskan, dan transparansi menjadi persyaratan standar.