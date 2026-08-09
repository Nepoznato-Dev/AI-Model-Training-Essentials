---
# Metadata
title: "Ensemble Methods"
description: "Bagging, boosting, stacking, voting, random forests, XGBoost"
category: "Data Science and Analytics"
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
reviewed_by: "Data Science & Analytics Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [ensemble, methods, data-science-and-analytics]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "7 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Metode Ensembel
Metode ansambel menggabungkan beberapa model pembelajaran mesin untuk menghasilkan prediksi yang lebih baik daripada yang dapat dicapai oleh satu model saja. Intuisinya sederhana: jika Anda memiliki beberapa model yang masing-masing agak akurat tetapi menghasilkan kesalahan yang berbeda, menggabungkan prediksi mereka akan menghilangkan kesalahan individual dan menghasilkan hasil yang lebih kuat. Ensembel berada di balik sebagian besar solusi pembelajaran mesin yang kompetitif dan tetap menjadi salah satu teknik paling andal dalam sistem produksi.
---

## Mengapa Ensemble Berhasil
| Prinsip | Deskripsi |
|-----------|-------------|
| **Kebijaksanaan orang banyak** | Beberapa perkiraan yang tidak sempurna, dirata-ratakan, lebih baik daripada perkiraan tunggal apa pun |
| **Pertukaran bias-varians** | Ansambel dapat mengurangi varians (bagging) atau bias (boosting) tanpa mengorbankan yang lain |
| **Keberagaman kesalahan** | Jika model membuat kesalahan yang berbeda, menggabungkannya akan membatalkan kesalahan individu |
| **Pemulusan batas keputusan** | Beberapa model menciptakan permukaan keputusan yang lebih kuat dibandingkan satu model |
---

## Bagging (Agregasi Bootstrap)
### Cara Kerjanya
| Langkah | Deskripsi |
|------|-------------|
| **1. Pengambilan sampel bootstrap** | Ambil beberapa sampel acak (dengan penggantian) dari data pelatihan |
| **2. Model dasar kereta** | Latih satu model pada setiap sampel bootstrap (biasanya pohon keputusan) |
| **3. Agregat** | Untuk regresi: prediksi rata-rata. Untuk klasifikasi : suara terbanyak |
### Karakteristik Utama
| Karakteristik | Deskripsi |
|---------------|-------------|
| **Mengurangi varians** | Rata-rata menghaluskan fluktuasi model individual |
| **Pelatihan paralel** | Setiap model dasar bersifat independen; dapat dilatih secara bersamaan |
| **Evaluasi langsung** | Setiap sampel tidak disertakan dalam beberapa sampel bootstrap; gunakan itu untuk validasi |
| **Dekorelasi** | Pemilihan fitur acak pada setiap pemisahan mengurangi korelasi antar pohon |
### Hutan Acak
| Aspek | Deskripsi |
|--------|-------------|
| **Pembelajar dasar** | Pohon keputusan |
| **Penambahan kunci** | Pada setiap pemisahan, pertimbangkan hanya subkumpulan fitur acak (biasanya sqrt(n_features)) |
| **Mengapa berhasil** | Pemilihan fitur acak menghiasi pepohonan, menjadikan ansambel lebih kuat |
| **Hyperparameter** | Jumlah pohon; kedalaman maksimal; sampel minimal per daun; fitur maksimal |
| **Kekuatan** | Menangani data berdimensi tinggi; kuat terhadap outlier; menyediakan fitur penting |
| **Kelemahan** | Kurang dapat ditafsirkan dibandingkan pohon tunggal; dapat melakukan overfit pada tugas regresi yang berisik |
---

## Meningkatkan
### Cara Kerjanya
| Langkah | Deskripsi |
|------|-------------|
| **1. Latih model pertama** | Latih model dasar (seringkali berupa pohon dangkal/"tunggul") pada data |
| **2. Identifikasi kesalahan** | Temukan contoh mana yang salah |
| **3. Latih model berikutnya** | Latih model baru yang berfokus pada kesalahan (ditimbang ulang atau dipasang sisa) |
| **4. Gabungkan secara berurutan** | Setiap model baru memperbaiki akumulasi kesalahan dari semua model sebelumnya |
| **5. Ulangi** | Lanjutkan untuk jumlah putaran yang ditentukan |
### Meningkatkan Algoritma
| Algoritma | Fungsi Kerugian | Fitur Utama |
|-----------|--------------|-------------|
| **AdaBoost** | Eksponensial | Menimbang ulang kejadian yang salah klasifikasi; sederhana; sensitif terhadap kebisingan |
| **Peningkatan Gradien** | Setiap kerugian yang dapat dibedakan | Cocok dengan sisa (gradien kerugian); lebih fleksibel |
| **Peningkatan XGB** | Peningkatan gradien yang diatur | Regularisasi L1/L2; gradien orde kedua; optimasi perangkat keras |
| **GBM Ringan** | Pengambilan sampel satu sisi berbasis gradien | Pertumbuhan berdasarkan daun; berbasis histogram; cepat pada kumpulan data besar |
| **Peningkatan Kucing** | Memesan peningkatan | Menangani fitur kategorikal secara asli; mengurangi overfitting |
### Meningkatkan vs Mengantongi
| Dimensi | mengantongi | Meningkatkan |
|-----------|---------|----------|
| **Pelatihan** | Paralel | Berurutan |
| **Fokus** | Mengurangi varians | Mengurangi bias |
| **Model dasar** | Varians tinggi, bias rendah (pohon dalam) | Varians rendah, bias tinggi (pohon/tunggul dangkal) |
| **Kombinasi** | Berat yang sama | Ditimbang berdasarkan kinerja |
| **Kelebihan Kesesuaian** | Kurang rawan | Bisa overfit jika terlalu banyak putaran |
| **Sensitivitas kebisingan** | Kuat | Sensitif terhadap data yang berisik |
---

## Menumpuk
### Cara Kerjanya
| Langkah | Deskripsi |
|------|-------------|
| **1. Model dasar kereta** | Latih beragam model (misalnya, hutan acak, SVM, jaringan saraf, peningkatan gradien) |
| **2. Hasilkan prediksi** | Gunakan prediksi out-of-fold (validasi silang) sebagai fitur masukan |
| **3. Latih model meta** | Latih model tingkat kedua berdasarkan prediksi model dasar |
| **4. Prediksi akhir** | Model dasar memprediksi; meta-model menggabungkan prediksi mereka |
### Menumpuk Praktik Terbaik
| Latihan | Alasan |
|----------|--------|
| **Gunakan model dasar yang beragam** | Algoritme yang berbeda menghasilkan kesalahan yang berbeda pula; keberagaman adalah inti |
| **Gunakan validasi silang untuk prediksi dasar** | Mencegah model meta belajar mengeksploitasi model dasar overfit |
| **Buat model meta tetap sederhana** | Regresi logistik atau pohon dangkal; model dasar melakukan pekerjaan berat |
| **Sertakan fitur mentah dalam meta-model** | Terkadang bermanfaat untuk memberikan akses model meta ke fitur asli juga |
---

## Voting dan Rata-rata
### Voting Keras (Klasifikasi)
| Model | Prediksi |
|-------|-----------|
| Model A | Kelas 1 |
| Model B | Kelas 0 |
| Model C | Kelas 1 |
| **Suara terbanyak** | **Kelas 1** |
### Soft Voting (Klasifikasi)
| Model | P(Kelas 0) | P(Kelas 1) |
|-------|-----------|-----------|
| Model A | 0,3 | 0,7 |
| Model B | 0,6 | 0,4 |
| Model C | 0,4 | 0,6 |
| **Rata-rata** | **0,43** | **0,57** |
| **Prediksi** | | **Kelas 1** |
### Rata-rata Tertimbang
| Model | Berat | Prediksi |
|-------|--------|-----------|
| Model A | 0,5 | 0,8 |
| Model B | 0,3 | 0,6 |
| Model C | 0,2 | 0,9 |
| **Rata-rata tertimbang** | | 0,5×0,8 + 0,3×0,6 + 0,2×0,9 = 0,76 |
---

## Panduan Praktis
### Kapan Menggunakan Ensembel Yang Mana
| Skenario | Metode yang Direkomendasikan |
|----------|-------------------|
| **Garis dasar cepat; data tabel** | Hutan Acak |
| **Akurasi maksimum; data tabel** | XGBoost / LightGBM / CatBoost |
| **Data berisik** | Bagging (boosting akan menghilangkan kebisingan) |
| **Diperlukan interpretasi** | Model tunggal atau ansambel kecil dengan fitur penting |
| **Jenis model yang beragam** | Penumpukan atau pemungutan suara |
| **Pembelajaran daring** | Metode streaming ansambel; peningkatan adaptif |
| **Data tidak seimbang** | Hutan Acak Seimbang; peningkatan yang sensitif terhadap biaya |
### Ansambel Strategi Keberagaman
| Strategi | Deskripsi |
|----------|-------------|
| **Algoritma berbeda** | Gabungkan model berbasis pohon, linier, dan saraf |
| **Fitur berbeda** | Latih model pada subkumpulan fitur yang berbeda |
| **Subkumpulan data yang berbeda** | mengantongi; subsampling |
| **Hyperparameter berbeda** | Algoritma yang sama dengan konfigurasi bervariasi |
| **Periode waktu berbeda** | Berlatih di jendela waktu yang berbeda |
---

## Ringkasan
Metode ansambel berhasil karena menggabungkan beberapa model yang tidak sempurna menjadi satu prediktor yang kuat. Bagging (hutan acak) mengurangi varians dengan melatih model secara paralel pada sampel bootstrap dan membuat rata-rata. Peningkatan (XGBoost, LightGBM, CatBoost) mengurangi bias dengan melatih model secara berurutan, masing-masing memperbaiki kesalahan sebelumnya. Penumpukan menggunakan model meta untuk menggabungkan beragam model dasar. Voting dan averaging adalah ansambel yang paling sederhana. Benang merahnya adalah keberagaman: ansambel bekerja paling baik ketika model komponennya masuk akal secara individual tetapi membuat kesalahan yang berbeda. Dalam praktiknya, peningkatan gradien pada data tabular sering kali merupakan pendekatan tunggal dengan performa tertinggi, sementara penumpukan model yang beragam akan mendorong akurasi lebih jauh dalam kompetisi dan aplikasi berisiko tinggi.