---
# Metadata
title: "Feature Engineering"
description: "Transformations, encodings, feature selection, dimensionality reduction"
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
tags: [feature, engineering, data-science-and-analytics]
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
# Rekayasa Fitur
Rekayasa fitur adalah proses mengubah data mentah menjadi representasi yang membuat model pembelajaran mesin lebih efektif. Ini sering digambarkan sebagai langkah paling penting dalam pipeline ML — fitur yang Anda berikan pada model lebih penting daripada algoritme yang Anda pilih. Model sederhana dengan fitur yang dibuat dengan baik biasanya akan mengungguli model kompleks dengan masukan mentah dan belum diproses. Seninya terletak pada pemahaman domain dan data dengan cukup baik untuk menciptakan sinyal yang dapat dipelajari oleh model.
---

## Mengapa Rekayasa Fitur Penting
| Faktor | Dampak |
|--------|--------|
| **Kualitas sinyal** | Fitur yang lebih baik = pola yang lebih jelas untuk dipelajari model |
| **Kesederhanaan model** | Fitur bagus memungkinkan model yang lebih sederhana berperforma baik; lebih sedikit kebutuhan akan arsitektur yang kompleks |
| **Kecepatan latihan** | Fitur-fitur yang relevan dan berskala baik menyatu lebih cepat |
| **Generalisasi** | Fitur informasi domain membantu model bekerja pada data yang tidak terlihat |
| **Interpretabilitas** | Fitur yang bermakna lebih mudah dijelaskan kepada pemangku kepentingan |
---

## Jenis Transformasi Fitur
### Transformasi Numerik
| Transformasi | Rumus / Deskripsi | Kapan Menggunakan |
|---------------|----------------------|-------------|
| **Transformasi log** | log(x) atau log(x + 1) | Distribusi miring ke kanan; nilai moneter |
| **Akar kuadrat** | persegi(x) | Kemiringan sedang; menghitung data |
| **Kotak-Cox** | Transformasi parametrik yang menemukan transformasi daya terbaik | Menjadikan data lebih terdistribusi normal |
| **Yeo-Johnson** | Seperti Box-Cox tetapi menangani nilai negatif | Data miring dengan nilai negatif |
| **Standarisasi** | (x - berarti) / std | Fitur dengan skala berbeda; algoritma dengan asumsi normalitas |
| **Penskalaan min-maks** | (x - mnt) / (maks - mnt) | Fitur pembatas ke [0, 1]; nilai piksel gambar |
| **Penskalaan yang kuat** | (x - median) / IQR | Data dengan outlier |
| **Pengelompokan** | Ubah kontinu menjadi kategorikal | hubungan nonlinier; pohon keputusan |
| **Fitur polinomial** | x², x³, x₁×x₂ | Menangkap hubungan non-linier dalam model linier |
### Pengkodean Kategoris
| Pengkodean | Deskripsi | Kapan Menggunakan |
|----------|-------------|-------------|
| **Encoding satu-panas** | Buat kolom biner untuk setiap kategori | Kategori kardinalitas rendah; model berbasis pohon menangani secara asli |
| **Pengkodean label** | Tetapkan bilangan bulat untuk setiap kategori | Kategori biasa; model berbasis pohon |
| **Encoding target** | Ganti kategori dengan rata-rata variabel target | Kategori berkardinalitas tinggi; hindari overfitting dengan smoothing |
| **Pengkodean frekuensi** | Ganti kategori dengan jumlah atau frekuensinya | Ketika frekuensi itu sendiri bersifat informatif |
| **Pengkodean biner** | Ubah kategori berkode bilangan bulat menjadi digit biner | Kardinalitas tinggi; mengurangi dimensi vs one-hot |
| **Penyematan** | Pelajari representasi vektor padat | Kardinalitas sangat tinggi; NLP; sistem pemberi rekomendasi |
| **Pengkodean hash** | Hash kategori ke sejumlah fitur tetap | Kardinalitas sangat tinggi; pembelajaran daring |
### Fitur Tanggal dan Waktu
| Fitur | Deskripsi |
|---------|-------------|
| **Jam dalam sehari** | Menangkap pola harian (jam sibuk, malam hari) |
| **Hari dalam seminggu** | Efek hari kerja vs akhir pekan |
| **Bulan/kuartal** | Pola musiman |
| **Apakah akhir pekan** | Bendera biner untuk akhir pekan |
| **Apakah hari libur** | Bendera biner untuk hari libur |
| **Waktu sejak kejadian** | Hari sejak pembelian terakhir; jam sejak login terakhir |
| **Pengkodean siklis** | sin(2π × jam / 24), cos(2π × jam / 24) — mempertahankan sifat melingkar waktu |
---

## Menangani Nilai yang Hilang
| Strategi | Deskripsi | Kapan Menggunakan |
|----------|-------------|-------------|
| **Lepaskan baris** | Hapus baris dengan nilai yang hilang | Data yang hilang hanyalah sebagian kecil; MCAR (hilang sepenuhnya secara acak) |
| **Lepaskan kolom** | Hapus fitur dengan terlalu banyak nilai yang hilang | Sebagian besar fitur hilang; tidak penting |
| **Imputasi rata-rata / median** | Isi dengan mean atau median fitur | Sederhana; mempertahankan mean tetapi mengurangi varians |
| **Mode imputasi** | Isikan kategorikal dengan nilai yang paling sering | Fitur kategorikal |
| **Imputasi KNN** | Gunakan k-tetangga terdekat untuk memperkirakan nilai yang hilang | Ketika contoh serupa membantu memprediksi nilai yang hilang |
| **Imputasi berbasis model** | Latih model untuk memprediksi nilai yang hilang | Lebih akurat; mahal secara komputasi |
| **Indikator tidak ada** | Tambahkan kolom biner yang menandai hilangnya | Ketika ketidakhadiran itu sendiri bersifat informatif |
| **Interpolasi** | Isi dengan nilai interpolasi (linier, spline) | Rangkaian waktu; data yang dipesan |
---

## Pemilihan Fitur
### Metode Penyaringan
| Metode | Deskripsi |
|--------|-------------|
| **Korelasi** | Hapus fitur yang sangat berkorelasi satu sama lain |
| **Ambang varians** | Hapus fitur dengan varian mendekati nol |
| **Informasi timbal balik** | Ukur informasi yang disediakan setiap fitur tentang target |
| **Chi-kuadrat** | Uji independensi antara fitur kategorikal dan target |
| **Uji F ANOVA** | Uji apakah fitur numerik berbeda antar kelas target |
### Metode Pembungkus
| Metode | Deskripsi |
|--------|-------------|
| **Pilihan maju** | Mulai kosong; tambahkan fitur terbaik satu per satu |
| **Eliminasi mundur** | Mulailah dengan semua; hapus fitur terburuk satu per satu |
| **Penghapusan fitur rekursif (RFE)** | Melatih model berulang kali; hapus fitur yang paling tidak penting |
### Metode Tersemat
| Metode | Deskripsi |
|--------|-------------|
| **Regulerisasi L1 (Lasso)** | Mengurangi bobot fitur yang tidak relevan menjadi nol |
| **Kepentingan berbasis pohon** | Gunakan fitur penting dari model pohon |
| **Nilai SHAP** | Ukur kontribusi setiap fitur terhadap prediksi |
---

## Rekayasa Fitur Khusus Domain
### Fitur Teks
| Fitur | Deskripsi |
|---------|-------------|
| **TF-IDF** | Frekuensi term diberi bobot berdasarkan frekuensi dokumen terbalik |
| **Penyematan kata** | Vektor padat menangkap makna semantik (Word2Vec, GloVe) |
| **Karakter n-gram** | Menangkap pola sub-kata; berguna untuk kesalahan ketik dan morfologi |
| **Statistik teks** | Panjang; jumlah kata; jumlah kalimat; rata-rata panjang kata |
| **Skor keterbacaan** | Flesch-Kincaid; Indeks kabut tembak |
### Fitur Rangkaian Waktu
| Fitur | Deskripsi |
|---------|-------------|
| **Fitur lag** | Nilai sebelumnya: y(t-1), y(t-7), y(t-30) |
| **Statistik bergulir** | Berarti, std, min, max melalui jendela |
| **Perbedaan** | kamu(t) - kamu(t-1); menangkap tren |
| **Perbedaan musim** | y(t) - y(t-12) untuk data bulanan dengan musiman tahunan |
| **Istilah empatier** | Suku sinus dan kosinus untuk pola musiman |
### Fitur Gambar (Pra-Pembelajaran Mendalam)
| Fitur | Deskripsi |
|---------|-------------|
| **HOG** (Histogram Gradien Berorientasi) | Distribusi arah tepi |
| **LBP** (Pola Biner Lokal) | Deskripsi tekstur |
| **SIFT** (Transformasi Fitur Invarian Skala) | Deskriptor titik kunci |
| **Histogram warna** | Distribusi warna pada gambar |
---

## Praktik Terbaik Rekayasa Fitur
| Latihan | Deskripsi |
|----------|-------------|
| **Hindari kebocoran data** | Jangan pernah menggunakan informasi dari masa depan atau kumpulan pengujian untuk membuat fitur |
| **Dokumentasikan semuanya** | Catat transformasi apa yang diterapkan dan alasannya |
| **Versi fitur Anda** | Lacak perubahan fitur bersamaan dengan perubahan model |
| **Validasi dengan dan tanpa** | Uji apakah fitur baru benar-benar meningkatkan kinerja model |
| **Jaga agar dapat direproduksi** | Jalur rekayasa fitur harus bersifat deterministik dan dapat diulang |
| **Pantau penyimpangan fitur** | Distribusi fitur dapat berubah seiring waktu; pantau dan latih kembali |
---

## Ringkasan
Rekayasa fitur adalah tempat pengetahuan domain bertemu dengan pembelajaran mesin. Ini adalah proses mengubah data mentah — yang berantakan, tidak lengkap, berdimensi tinggi — menjadi representasi yang bersih dan informatif sehingga model dapat belajar darinya. Transformasi numerik menangani kemiringan dan skala. Pengkodean kategorikal mengubah label menjadi model angka yang dapat digunakan. Fitur tanggal menangkap pola temporal. Strategi nilai yang hilang menangani data yang tidak lengkap. Pemilihan fitur menghilangkan noise dan redundansi. Insinyur fitur terbaik berpikir seperti detektif: mereka menanyakan sinyal apa yang harus ada dalam data, di mana sinyal tersebut mungkin disembunyikan, dan cara mengekstraknya dengan cara yang jujur ​​(tidak ada kebocoran data), dapat direproduksi, dan kuat untuk berubah seiring waktu.