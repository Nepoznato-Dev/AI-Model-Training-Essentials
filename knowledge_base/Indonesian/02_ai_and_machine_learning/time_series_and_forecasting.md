---
# Metadata
title: "Time Series and Forecasting"
description: "ARIMA, Prophet, LSTMs, seasonality, anomaly detection"
category: "AI and Machine Learning"
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
reviewed_by: "AI & Machine Learning Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [time, series, forecasting, ai-and-machine-learning]
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
# Rangkaian Waktu dan Peramalan
Data deret waktu adalah data apa pun yang dikumpulkan dari waktu ke waktu: harga saham, pembacaan suhu, lalu lintas situs web, angka penjualan, monitor detak jantung, konsumsi energi. Peramalan berarti memprediksi nilai masa depan berdasarkan pola masa lalu. Ini adalah salah satu penerapan ilmu data yang paling berharga secara praktis — dan salah satu yang tersulit, karena masa depan benar-benar tidak pasti dan rangkaian waktu di dunia nyata penuh dengan kebisingan, perubahan musim, dan perubahan struktural.
---

## Karakteristik Rangkaian Waktu
| Komponen | Deskripsi | Contoh |
|-----------|-------------|---------|
| **Tren** | Peningkatan atau penurunan jangka panjang | Suhu global meningkat selama beberapa dekade |
| **musiman** | Pola teratur dan dapat diprediksi pada interval tetap | Penjualan ritel melonjak setiap bulan Desember |
| **Siklisitas** | Fluktuasi pada interval tidak tetap (sering kali ekonomis) | Resesi setiap 5-10 tahun |
| **Kebisingan (sisa)** | Variasi acak yang tidak dapat dijelaskan | Pergerakan harga saham harian |
| **Autokorelasi** | Nilai saat ini bergantung pada nilai masa lalu | Suhu hari ini sama dengan suhu kemarin |
### Stasioneritas
Deret waktu bersifat **stasioner** jika properti statistiknya (rata-rata, varians) tidak berubah seiring waktu. Kebanyakan metode peramalan mengasumsikan stasioneritas.
| Tes | Tujuan |
|------|---------|
| **Augmented Dickey-Fuller (ADF)** | Menguji apakah ada akar unit (tidak stasioner) |
| **Tes KPSS** | Menguji apakah rangkaian tersebut stasioner tren |
| Transformasi | Kapan Menggunakan |
|---------------|-------------|
| **Perbedaan** | Hapus tren: y'(t) = y(t) - y(t-1) |
| **Transformasi log** | Stabilkan varians (untuk pertumbuhan eksponensial) |
| **Perbedaan musiman** | Hapus kemusiman: y'(t) = y(t) - y(t-s) dengan s adalah lamanya musim |
---

## Metode Peramalan Klasik
### Rata-Rata Pergerakan
| Metode | Deskripsi | Terbaik Untuk |
|--------|-------------|----------|
| **Rata-Rata Pergerakan Sederhana (SMA)** | Rata-rata N observasi terakhir | Menghaluskan data yang berisik |
| **Rata-Rata Pergerakan Tertimbang** | Pengamatan yang lebih baru mendapat bobot lebih tinggi | Ketika data terkini lebih penting |
| **Rata-Rata Pergerakan Eksponensial (EMA)** | Mengurangi bobot secara eksponensial | Melacak tren dengan lebih sedikit jeda |
### Penghalusan Eksponensial
| Metode | Komponen | Kasus Penggunaan |
|--------|-----------|----------|
| **Sederhana (SES)** | Hanya tingkat | Tidak ada tren, tidak ada musiman |
| **Holt (Ganda)** | Tingkat + tren | Data dengan tren tetapi tanpa musiman |
| **Holt-Winters (Triple)** | Level + tren + musiman | Data dengan tren dan musiman |
### ARIMA dan Variannya
ARIMA (AutoRegressive Integrated Moving Average) adalah alat peramalan deret waktu klasik.
| Komponen | Arti | Parameter |
|-----------|---------|-----------|
| **AR (p)** | Regresi nilai p sebelumnya | Berapa banyak nilai masa lalu yang akan digunakan |
| **Saya (d)** | Banyaknya langkah pembedaan untuk membuat stasioner | Berapa kali selisihnya |
| **MA (q)** | Modelkan kesalahan sebagai kombinasi kesalahan masa lalu | Berapa banyak kesalahan masa lalu yang digunakan |
| Varian | Ekstensi | Kasus Penggunaan |
|---------|-----------|----------|
| **SARIMA** | Menambahkan komponen musiman (P, D, Q, s) | Data dengan musiman yang kuat |
| **ARIMAX** | Menambahkan variabel eksternal | Ketika Anda tahu tentang acara mendatang |
| **VAR** | ARIMA multivariat; beberapa deret yang saling bergantung | Ketika variabel saling mempengaruhi |
---

## Pendekatan ML Modern
### Model Berbasis LSTM dan RNN
| Model | Arsitektur | Keuntungan |
|-------|-------------|-----------|
| **LSTM** | Jaringan Memori Jangka Pendek Panjang | Menangkap ketergantungan temporal jangka panjang |
| **GRU** | Unit Berulang Berpagar (LSTM lebih sederhana) | Pelatihan lebih cepat; kinerja serupa |
| **Seq2Seq** | Encoder-decoder untuk deret waktu | Panjang input/output yang fleksibel |
| **Jaringan Konvolusional Temporal (TCN)** | Konvolusi sebab akibat yang melebar | Pelatihan paralel; bidang reseptif panjang |
### Nabi (Meta)
Alat perkiraan praktis yang dirancang untuk deret waktu bisnis.
| Fitur | Deskripsi |
|---------|-------------|
| **Dekomposisi** | Tren + musiman + hari libur |
| **Fleksibel** | Menangani data yang hilang, outlier, dan kerusakan struktural |
| **Dapat Ditafsirkan** | Komponen dapat dibaca manusia |
| **Otomatis** | Default yang wajar; diperlukan penyetelan minimal |
| Kekuatan | Batasan |
|----------|------------|
| Cocok untuk metrik bisnis (penjualan, pengguna) | Tidak ideal untuk data frekuensi sangat tinggi |
| Menangani hari libur dan acara khusus | Mengasumsikan musiman aditif atau multiplikatif |
| Kuat terhadap outlier | Kurang akurat dibandingkan pembelajaran mendalam untuk pola kompleks |
### Model Berbasis Transformator
| Model | Fitur Utama |
|-------|-------------|
| **Informan** | Mungkin Perhatian yang jarang untuk urutan yang panjang |
| **Pembentuk Otomatis** | Mekanisme korelasi otomatis untuk dekomposisi deret |
| **PatchTST** | Menambal rangkaian waktu; saluran-independen |
| **TimesFM** (Google) | Model landasan untuk deret waktu; dilatih sebelumnya tentang beragam data |
| **Chronos** (Amazon) | Tokenisasi deret waktu; menggunakan arsitektur bergaya LLM |
---

## Deteksi Anomali dalam Rangkaian Waktu
Mendeteksi pola tidak biasa yang menyimpang dari perilaku yang diharapkan.
| Metode | Pendekatan | Kasus Penggunaan |
|--------|----------|----------|
| **Statistik** | Skor Z, IQR, diagram kendali | Sederhana, dipahami dengan baik |
| **Hutan Isolasi** | Berbasis pohon; mengisolasi anomali dengan partisi acak | Deteksi anomali multivariat |
| **LOF** (Faktor Outlier Lokal) | Berbasis kepadatan; membandingkan kepadatan lokal dengan tetangga | Ketika anomali berada di wilayah dengan kepadatan rendah |
| **Autoencoder** | kesalahan rekonstruksi; kesalahan tinggi = anomali | Pola kompleks dan non-linier |
| **Berbasis LSTM** | Prediksi langkah selanjutnya; kesalahan prediksi besar = anomali | Anomali berurutan |
### Aplikasi
| Domain | Apa Arti Anomali |
|--------|-------------------|
| **Keuangan** | Penipuan, pasar ambruk, flash ambruk |
| **Perawatan Kesehatan** | Denyut jantung tidak normal, timbulnya kejang |
| **Manufaktur** | Kegagalan peralatan, cacat kualitas |
| **Keamanan siber** | Upaya intrusi, serangan DDoS |
| **Infrastruktur** | Server kelebihan beban, kegagalan jaringan |
---

## Metrik Evaluasi
| Metrik | Rumus (konseptual) | Kapan Menggunakan |
|--------|---------------------|-------------|
| **MAE** (Berarti Kesalahan Absolut) | Rata-rata kesalahan absolut | Dapat ditafsirkan; satuan yang sama dengan data |
| **RMSE** (Kesalahan Root Mean Squared) | Akar kuadrat dari kesalahan kuadrat rata-rata | Menghukum kesalahan besar lebih banyak |
| **MAPE** (Rata-rata Kesalahan Persentase Absolut) | Rata-rata persentase kesalahan absolut | Ketika kesalahan relatif penting |
| **SMAPE** (MAPE Simetris) | Versi simetris MAPE | Menangani nilai mendekati nol dengan lebih baik |
| **MASE** (Rata-rata Kesalahan Berskala Absolut) | MAE relatif terhadap perkiraan naif | Membandingkan berbagai seri |
---

## Alur Kerja Praktis
| Langkah | Deskripsi |
|------|-------------|
| **1. Jelajahi** | Plot serinya; mengidentifikasi tren, musiman, outlier |
| **2. Terurai** | Pisahkan menjadi komponen tren, musiman, dan sisa |
| **3. Stasionerisasi** | Terapkan pembedaan atau transformasi jika diperlukan |
| **4. Pisahkan** | Pemisahan berdasarkan waktu (tidak pernah pemisahan acak untuk rangkaian waktu) |
| **5. Dasar** | Mulailah dengan perkiraan naif (nilai terakhir, naif musiman) |
| **6. Model** | Coba metode klasik (ARIMA, Nabi), lalu metode ML |
| **7. Evaluasi** | Gunakan metrik yang sesuai; bandingkan dengan dasar |
| **8. Ulangi** | Tambahkan fitur, coba model berbeda, sesuaikan hyperparameter |
---

## Alat dan Perpustakaan
| Alat | Tujuan |
|------|---------|
| **model statistik** | Deret waktu klasik (ARIMA, ETS, dekomposisi) |
| **Nabi** (Meta) | Peramalan rangkaian waktu bisnis |
| **waktu sk** | Antarmuka ML terpadu untuk deret waktu |
| **Anak panah** | Pustaka perkiraan yang komprehensif (klasik + pembelajaran mendalam) |
| **GluonTS** (Amazon) | Pemodelan deret waktu probabilistik |
| **NeuralProphet** | Nabi dengan komponen jaringan saraf |
| **segar** | Ekstraksi fitur deret waktu otomatis |
| **panda** | Manipulasi deret waktu dan pengambilan sampel ulang |
---

## Ringkasan
Perkiraan deret waktu memadukan statistik klasik dengan pembelajaran mesin modern. Metode klasik (ARIMA, pemulusan eksponensial, Nabi) dapat ditafsirkan, cepat, dan seringkali akurat. Metode pembelajaran mendalam (LSTM, Transformers) menangkap pola yang kompleks tetapi memerlukan lebih banyak data dan penyesuaian. Prinsip utamanya tetap sama, apa pun metodenya: pahami struktur data Anda (tren, musiman, kebisingan), selalu bandingkan dengan data dasar yang sederhana, evaluasi dengan metrik yang sesuai, dan ingat bahwa masa depan tidak pernah merupakan pengulangan sempurna dari masa lalu.