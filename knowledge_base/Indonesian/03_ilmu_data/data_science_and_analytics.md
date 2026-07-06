# Ilmu Data dan Analitik

## Konsep Inti

### Apa itu Ilmu Data?
Ilmu data adalah bidang interdisipliner yang menggunakan metode ilmiah, proses, algoritma, dan sistem untuk mengekstrak pengetahuan dan wawasan dari data terstruktur dan tidak terstruktur. Bidang ini menggabungkan:
- **Statistika**: Fondasi matematis untuk analisis
- **Ilmu Komputer**: Pemrograman, algoritma, struktur data
- **Keahlian Domain**: Pengetahuan materi subjek
- **Visualisasi Data**: Mengkomunikasikan temuan secara efektif

### Jenis Data
- **Data Terstruktur**: Diorganisir dalam baris/kolom (basis data, spreadsheet)
- **Data Tidak Terstruktur**: Tanpa format yang telah ditentukan (teks, gambar, audio, video)
- **Data Semi-terstruktur**: Beberapa organisasi tetapi tidak kaku (JSON, XML, HTML)
- **Data Deret Waktu**: Titik data berurutan yang diindeks dalam urutan waktu
- **Data Spasial**: Informasi geografis/berbasis lokasi
- **Data Graf**: Node dan edge yang merepresentasikan hubungan

### Proses Ilmu Data (CRISP-DM)
1. **Pemahaman Bisnis**: Menentukan tujuan dan persyaratan
2. **Pemahaman Data**: Mengumpulkan dan menjelajahi data awal
3. **Persiapan Data**: Membersihkan, mentransformasi, dan memformat data (80% pekerjaan)
4. **Pemodelan**: Memilih dan menerapkan teknik pemodelan
5. **Evaluasi**: Menilai kinerja model terhadap tujuan
6. **Penerapan**: Mengimplementasikan model di lingkungan produksi

## Fondasi Statistika

### Statistika Deskriptif
- **Ukuran Tendensi Sentral**: Mean, median, modus
- **Ukuran Dispersi**: Rentang, varians, deviasi standar, rentang antar kuartil
- **Bentuk Distribusi**: Kemencengan (asimetri), kurtosis (ketebalan ekor)
- **Persentil dan Kuartil**: Posisi dalam distribusi

### Statistika Inferensial
- **Pengujian Hipotesis**: Hipotesis nol, hipotesis alternatif, nilai-p
- **Interval Kepercayaan**: Rentang nilai yang kemungkinan mengandung parameter populasi
- **Signifikansi Statistik**: Kemungkinan hasil terjadi karena kebetulan
- **Kesalahan Tipe I**: Positif palsu (menolak hipotesis nol yang benar)
- **Kesalahan Tipe II**: Negatif palsu (gagal menolak hipotesis nol yang salah)
- **Power**: Probabilitas menolak hipotesis nol yang salah dengan benar

### Distribusi Probabilitas
- **Distribusi Normal**: Kurva lonceng, mean = median = modus
- **Distribusi Binomial**: Hasil sukses/gagal
- **Distribusi Poisson**: Jumlah kejadian dalam interval tetap
- **Distribusi Uniform**: Semua hasil memiliki kemungkinan sama
- **Distribusi Eksponensial**: Waktu antar kejadian
- **Distribusi-t**: Ukuran sampel kecil, varians populasi tidak diketahui
- **Distribusi Chi-Square**: Analisis data kategorikal

### Uji Statistik
- **Uji-t**: Membandingkan mean antara dua kelompok
- **ANOVA**: Membandingkan mean di beberapa kelompok
- **Uji Chi-Square**: Menguji independensi variabel kategorikal
- **Mann-Whitney U**: Alternatif non-parametrik untuk uji-t
- **Korelasi Pearson**: Hubungan linear antara variabel kontinu
- **Korelasi Spearman**: Hubungan monotonik (berbasis peringkat)
- **Kolmogorov-Smirnov**: Membandingkan distribusi

## Pengumpulan dan Penyimpanan Data

### Sumber Data
- **Basis Data**: SQL, NoSQL, relasional, penyimpanan dokumen
- **API**: REST, GraphQL, web scraping
- **File**: CSV, JSON, XML, Parquet, Avro
- **Data Streaming**: Kafka, Kinesis, umpan real-time
- **Survei dan Eksperimen**: Pengumpulan data primer
- **Dataset Publik**: Data pemerintah, Kaggle, repositori akademik

### Pergudangan Data
- **ETL**: Proses Extract, Transform, Load
- **Danau Data**: Penyimpanan data mentah dalam format asli
- **Gudang Data**: Data terstruktur dan diproses untuk analisis
- **Mart Data**: Subset gudang untuk departemen tertentu
- **OLAP**: Online Analytical Processing, kueri multidimensi
- **Skema Bintang**: Tabel fakta dikelilingi oleh tabel dimensi
- **Skema Snowflake**: Tabel dimensi yang dinormalisasi

### Jenis Basis Data
- **Relasional (SQL)**: MySQL, PostgreSQL, Oracle, SQL Server
- **Dokumen**: MongoDB, CouchDB (dokumen seperti JSON)
- **Key-Value**: Redis, DynamoDB (pasangan key-value sederhana)
- **Column-Family**: Cassandra, HBase (dioptimalkan untuk kolom)
- **Graf**: Neo4j, Amazon Neptune (node dan hubungan)
- **Deret Waktu**: InfluxDB, TimescaleDB (data bertanda waktu)
- **Vektor**: Pinecone, Milvus (penyimpanan embedding untuk ML)

## Pra-pemrosesan Data

### Pembersihan Data
- **Nilai Hilang**: Imputasi (mean, median, modus, prediksi), penghapusan
- **Outlier**: Deteksi (IQR, Z-score), penanganan (pembatasan, transformasi)
- **Duplikat**: Identifikasi dan penghapusan
- **Inkonsistensi**: Standarisasi format, memperbaiki kesalahan ketik
- **Validasi Data**: Memeriksa constraint, rentang, tipe

### Transformasi Data
- **Normalisasi**: Skala ke rentang 0-1
- **Standarisasi**: Normalisasi Z-score (mean=0, std=1)
- **Encoding**: One-hot, label, ordinal, target encoding
- **Binning**: Mengelompokkan nilai kontinu ke dalam kategori
- **Transformasi Log**: Mengurangi kemencengan
- **Skala Fitur**: Membuat fitur dapat dibandingkan

### Rekayasa Fitur
- **Pembuatan Fitur**: Menurunkan fitur baru dari yang sudah ada
- **Seleksi Fitur**: Memilih fitur yang paling relevan
  - Metode filter (korelasi, chi-square)
  - Metode wrapper (eliminasi fitur rekursif)
  - Metode embedded (LASSO, pentingnya berbasis pohon)
- **Reduksi Dimensi**: PCA, t-SNE, UMAP
- **Suku Interaksi**: Menggabungkan fitur secara multiplikatif
- **Fitur Polinomial**: Membuat suku orde lebih tinggi

## Analisis Data Eksploratori (EDA)

### Teknik EDA
- **Statistik Ringkasan**: Menjelaskan tendensi sentral, sebaran, bentuk
- **Analisis Univariat**: Distribusi variabel tunggal
- **Analisis Bivariat**: Hubungan antara dua variabel
- **Analisis Multivariat**: Interaksi beberapa variabel
- **Analisis Korelasi**: Mengidentifikasi hubungan dan multikolinearitas
- **Segmentasi**: Mengelompokkan observasi serupa

### Alat Visualisasi
- **Histogram**: Distribusi variabel tunggal
- **Box Plot**: Ringkasan lima angka, deteksi outlier
- **Scatter Plot**: Hubungan antara dua variabel kontinu
- **Heatmap**: Matriks korelasi, kepadatan
- **Diagram Batang**: Perbandingan kategorikal
- **Diagram Garis**: Tren dari waktu ke waktu
- **Violin Plot**: Kepadatan distribusi dengan elemen box plot
- **Pair Plot**: Beberapa scatter plot untuk pasangan variabel

### Pustaka Python untuk EDA
- **pandas**: Manipulasi dan analisis data
- **numpy**: Komputasi numerik
- **matplotlib**: Plotting dasar
- **seaborn**: Visualisasi statistik
- **plotly**: Visualisasi interaktif
- **scipy**: Komputasi ilmiah dan statistika

## Machine Learning dalam Ilmu Data

### Supervised Learning
- **Regresi**: Memprediksi nilai kontinu
  - Regresi Linear
  - Regresi Polinomial
  - Ridge/LASSO/Elastic Net
  - Decision Tree Regressor
  - Random Forest Regressor
  - Gradient Boosting (XGBoost, LightGBM, CatBoost)

- **Klasifikasi**: Memprediksi label kategorikal
  - Regresi Logistik
  - k-Nearest Neighbors
  - Naive Bayes
  - Support Vector Machines
  - Decision Trees
  - Random Forest
  - Gradient Boosting
  - Neural Networks

### Unsupervised Learning
- **Clustering**: Mengelompokkan observasi serupa
  - k-Means
  - Hierarchical Clustering
  - DBSCAN (berbasis kepadatan)
  - Gaussian Mixture Models
  - Spectral Clustering

- **Reduksi Dimensi**: Mengurangi jumlah fitur
  - Principal Component Analysis (PCA)
  - t-Distributed Stochastic Neighbor Embedding (t-SNE)
  - Uniform Manifold Approximation (UMAP)
  - Autoencoder

- **Aturan Asosiasi**: Menemukan item yang muncul bersama
  - Algoritma Apriori
  - FP-Growth

### Evaluasi Model
- **Metrik Klasifikasi**: Akurasi, presisi, recall, F1-score, ROC-AUC, matriks konfusi
- **Metrik Regresi**: MAE, MSE, RMSE, R², Adjusted R²
- **Cross-Validation**: k-fold, stratified, leave-one-out, time series split
- **Penyetelan Hyperparameter**: Grid search, random search, optimisasi Bayesian
- **Kurva Pembelajaran**: Mendiagnosis tradeoff bias-varians

## Teknologi Big Data

### Framework Komputasi Terdistribusi
- **Apache Hadoop**: MapReduce, HDFS (Hadoop Distributed File System)
- **Apache Spark**: Pemrosesan dalam memori, lebih cepat dari Hadoop
  - Spark SQL: Pemrosesan data terstruktur
  - Spark Streaming: Data real-time
  - MLlib: Pustaka machine learning
  - GraphX: Pemrosesan graf
- **Apache Flink**: Pemrosesan stream dengan latensi rendah
- **Apache Beam**: Batch dan streaming terunifikasi

### Platform Cloud
- **AWS**: S3, EMR, Redshift, SageMaker, Glue
- **Google Cloud**: BigQuery, Dataproc, AI Platform, Cloud Storage
- **Azure**: Synapse Analytics, Databricks, Machine Learning, Data Lake
- **Snowflake**: Gudang data cloud

### Alat Pipeline Data
- **Apache Airflow**: Orkestrasi alur kerja
- **Luigi**: Manajemen pipeline (Spotify)
- **Prefect**: Orkestrasi alur kerja modern
- **Dagster**: Orkestrator data dengan fokus aset
- **dbt**: Transformasi data di gudang

## Business Intelligence dan Analitik

### Alat BI
- **Tableau**: Platform analitik visual
- **Power BI**: Analitik bisnis Microsoft
- **Looker**: Eksplorasi data dan wawasan (Google)
- **Qlik Sense**: Analitik asosiatif
- **Metabase**: BI open-source
- **Superset**: Apache BI open-source

### Prinsip Desain Dashboard
- **Kenali Audiens Anda**: Sesuaikan dengan kebutuhan pengguna
- **Pilih Visualisasi yang Tepat**: Cocokkan grafik dengan jenis data
- **Gunakan Warna Secara Strategis**: Sorot informasi penting
- **Jaga Konsistensi**: Standarisasi format dan skala
- **Aktifkan Interaktivitas**: Filter, drill-down, tooltip
- **Optimalkan Kinerja**: Pemuatan cepat, kueri efisien
- **Pertimbangan Mobile**: Desain responsif

### Key Performance Indicators (KPI)
- **Keuangan**: Pendapatan, margin laba, ROI, customer lifetime value
- **Pelanggan**: Biaya akuisisi, tingkat churn, skor kepuasan, NPS
- **Operasional**: Tingkat efisiensi, waktu siklus, tingkat cacat
- **Pemasaran**: Tingkat konversi, click-through rates, atribusi
- **Produk**: Pengguna aktif, keterlibatan, retensi, adopsi fitur

## Analitik Lanjutan

### Analitik Prediktif
- **Peramalan**: Prediksi deret waktu (ARIMA, Prophet, LSTM)
- **Pemodelan Risiko**: Skor kredit, deteksi penipuan, asuransi
- **Analitik Pelanggan**: Prediksi churn, pemodelan kecenderungan
- **Peramalan Permintaan**: Optimasi inventaris, rantai pasokan
- **Prediksi Pemeliharaan**: Antisipasi kegagalan peralatan

### Analitik Preskriptif
- **Optimisasi**: Pemrograman linear, pemrograman integer
- **Simulasi**: Metode Monte Carlo, simulasi event diskrit
- **Analisis Keputusan**: Pohon keputusan, diagram pengaruh
- **Pengujian A/B**: Desain eksperimen, signifikansi statistik
- **Multi-Armed Bandits**: Eksperimentasi adaptif

### Analitik Teks (NLP)
- **Pra-pemrosesan Teks**: Tokenisasi, stemming, lemmatisasi
- **Analisis Sentimen**: Klasifikasi positif/negatif/netral
- **Pemodelan Topik**: LDA, NMF untuk penemuan tema
- **Named Entity Recognition**: Mengidentifikasi orang, tempat, organisasi
- **Klasifikasi Teks**: Deteksi spam, kategorisasi
- **Word Embeddings**: Word2Vec, GloVe, BERT

## Etika dan Tata Kelola Data

### Privasi Data
- **GDPR**: Peraturan Perlindungan Data Umum UE
- **CCPA**: Undang-Undang Privasi Konsumen California
- **HIPAA**: Undang-Undang Portabilitas dan Akuntabilitas Asuransi Kesehatan (layanan kesehatan AS)
- **Anonimisasi**: Menghapus informasi yang dapat diidentifikasi secara pribadi
- **Privasi Diferensial**: Menambahkan noise untuk melindungi individu
- **Manajemen Persetujuan**: Mekanisme opt-in/opt-out

### Kualitas Data
- **Akurasi**: Kebenaran data
- **Kelengkapan**: Semua data yang diperlukan hadir
- **Konsistensi**: Tidak ada kontradiksi di seluruh sumber
- **Ketepatan Waktu**: Data tersedia saat dibutuhkan
- **Validitas**: Sesuai dengan aturan yang ditentukan
- **Keunikan**: Tidak ada duplikat

### Bias dan Keadilan
- **Bias Sampling**: Pengumpulan data yang tidak representatif
- **Bias Pengukuran**: Instrumen pengumpulan data yang cacat
- **Bias Algoritmik**: Prediksi model yang diskriminatif
- **Metrik Keadilan**: Paritas demografis, kesempatan yang sama
- **Mitigasi Bias**: Pra-pemrosesan, dalam pemrosesan, pasca-pemrosesan

### Kerangka Tata Kelola Data
- **Stewardship Data**: Tanggung jawab atas aset data
- **Manajemen Metadata**: Dokumentasi data tentang data
- **Lineage Data**: Melacak aliran dan transformasi data
- **Kontrol Akses**: Izin berbasis peran
- **Audit Trails**: Mencatat akses dan perubahan data
- **Kepatuhan**: Kepatuhan terhadap peraturan

## Jalur Karir dalam Ilmu Data

### Peran
- **Analis Data**: Fokus pada analitik deskriptif, dashboard, pelaporan
- **Ilmuwan Data**: Pemodelan statistik, machine learning, analitik lanjutan
- **ML Engineer**: Sistem ML produksi, penerapan model, MLOps
- **Data Engineer**: Pipeline data, infrastruktur, proses ETL
- **Manajer Analitik**: Kepemimpinan tim, strategi, manajemen pemangku kepentingan
- **Pengembang BI**: Pembuatan dashboard, pengembangan laporan
- **Ilmuwan Penelitian**: Algoritma baru, publikasi, penelitian lanjutan

### Matriks Keterampilan
- **Teknis**: Python/R, SQL, statistika, framework ML, platform cloud
- **Analitis**: Pemecahan masalah, pemikiran kritis, desain eksperimen
- **Komunikasi**: Storytelling, visualisasi, keterampilan presentasi
- **Bisnis**: Pengetahuan domain, manajemen pemangku kepentingan, analisis ROI
- **Alat**: Git, Jupyter, Docker, CI/CD, kontrol versi untuk model

## Tren Muncul

### Perkembangan Saat Ini
- **AutoML**: Pembuatan pipeline machine learning otomatis
- **MLOps**: Praktik DevOps untuk machine learning
- **Feature Stores**: Manajemen fitur terpusat
- **Data Mesh**: Arsitektur data terdesentralisasi
- **LLM dan AI Generatif**: Model bahasa besar, pembuatan konten
- **Edge Analytics**: Pemrosesan data di perangkat sumber
- **Analitik Real-Time**: Analisis data streaming
- **Augmented Analytics**: Persiapan data dan wawasan berbantuan AI

### Arah Masa Depan
- **Quantum Machine Learning**: Komputasi kuantum untuk ML
- **Federated Learning**: Pelatihan model di data terdesentralisasi
- **Inferensi Kausal**: Bergerak melampaui korelasi ke kausalitas
- **AI yang Bertanggung Jawab**: Etika, kemampuan penjelasan, transparansi
- **Data Fabric**: Manajemen data terintegrasi di seluruh lingkungan
