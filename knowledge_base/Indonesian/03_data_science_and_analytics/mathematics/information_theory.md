<!--
---
# Metadata
title: "Information Theory"
description: "Shannon entropy, differential entropy, joint and mutual information, KL divergence, cross-entropy, channel capacity, source coding, compression, and connections to machine learning loss functions"
category: "Data Science and Analytics"
subcategory: "Mathematics"
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
    date: "2026-08-10"
    author: "Nepoznato-Dev"
    changes: "Initial deep-dive into information theory"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2027-02-10"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-10"

# Classification
tags: [information-theory, entropy, kl-divergence, cross-entropy, mutual-information, channel-capacity, compression, machine-learning]
difficulty_level: "intermediate"
prerequisites:
  - "mathematics.md"
  - "statistics_and_probability.md"
estimated_reading_time: "25 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Teori Informasi
Teori informasi, yang didirikan oleh Claude Shannon pada tahun 1948, mengkuantifikasi informasi itu sendiri. Berapa banyak pesan yang disampaikan kepada Anda? Berapa banyak Anda dapat mengompresi data? Seberapa cepat Anda dapat berkomunikasi melalui saluran yang bising? Pertanyaan-pertanyaan ini memiliki jawaban matematis yang tepat. Selain komunikasi, teori informasi telah menjadi dasar pembelajaran mesin — entropi silang adalah fungsi kerugian default untuk klasifikasi, divergensi KL mengukur kesamaan distribusi, dan informasi timbal balik mendorong pemilihan fitur.
---

## Entropi
**Entropi** mengukur ketidakpastian rata-rata atau "kejutan" dari variabel acak.
### Entropi Shannon (Diskrit)
Untuk variabel acak diskrit X dengan fungsi massa probabilitas p(x):
H(X) = −Σₓ p(x) log₂ p(x)
Satuan: **bits** (saat menggunakan log₂) atau **nats** (saat menggunakan ln).
| Distribusi | Entropi | Intuisi |
|-------------|---------|-----------|
| Koin adil (p = 0,5, 0,5) | 1 sedikit | Ketidakpastian maksimum untuk hasil biner |
| Koin bias (p = 0,9, 0,1) | 0,469 bit | Tidak terlalu mengejutkan — kebanyakan kepala |
| deterministik (p = 1, 0) | 0 bit | Tidak ada ketidakpastian sama sekali |
| Mati adil (6 sisi) | 2.585 bit | Lebih banyak hasil = lebih banyak ketidakpastian |
| Seragam atas n hasil | log₂(n) bit | Entropi maksimum untuk n hasil |
### Sifat Entropi
| Properti | Pernyataan |
|----------|-----------|
| Non-negatif | H(X) ≥ 0 |
| Maksimum | H(X) ≤ log₂(\|X\|) dengan persamaan untuk distribusi seragam |
| Aturan rantai | H(X, Y) = H(X) + H(Y \| X) |
| Pengkondisian mengurangi | H(X \| Y) ≤ H(X) |
| Cekungan | H adalah fungsi cekung dari distribusi probabilitas |
### Entropi Diferensial (Kontinu)
Untuk variabel acak kontinu X dengan kepadatan p(x):
h(X) = −∫ p(x) log p(x) dx
Tidak seperti entropi diskrit, entropi diferensial dapat bernilai **negatif**.
| Distribusi | Entropi Diferensial |
|-------------|---------------------|
| Seragam pada [a,b] | catatan(b − a) |
| Biasa N(μ, σ²) | (1/2) log(2πeσ²) |
| Eksponensial(λ) | 1 − ln(λ) |
---

## Informasi Bersama, Bersyarat, dan Saling Menguntungkan
### Entropi Gabungan
H(X, Y) = −Σₓ Σᵧ p(x, y) log p(x, y)
Mengukur ketidakpastian total pasangan (X, Y).
### Entropi Bersyarat
H(Y | X) = −Σₓ Σᵧ p(x, y) log p(y | x) = H(X, Y) − H(X)
Mengukur sisa ketidakpastian tentang Y setelah mengamati X.
### Saling Informasi
I(X; Y) = Σₓ Σᵧ p(x, y) log [p(x, y) / (p(x)p(y))]
Mengukur seberapa banyak pengetahuan X memberitahu Anda tentang Y (dan sebaliknya).
| Properti | Pernyataan |
|----------|-----------|
| Non-negatif | Saya(X; Y) ≥ 0 |
| Simetri | Saya(X; Y) = Saya(Y; X) |
| Kaitannya dengan entropi | I(X; Y) = H(X) − H(X \| Y) = H(Y) − H(Y \| X) |
| Kaitannya dengan gabungan | Saya(X; Y) = H(X) + H(Y) − H(X, Y) |
| Kemerdekaan | I(X; Y) = 0 jika X dan Y saling bebas |
| Informasi diri | Saya(X; X) = H(X) |
### Visual: Diagram Entropi
```
┌─────────────────────────────────────────┐
│            H(X, Y)                      │
│  ┌──────────────┐  ┌──────────────┐    │
│  │   H(X|Y)     │  │   H(Y|X)     │    │
│  │              │I │              │    │
│  │              │( │              │    │
│  │   H(X)−I    │X │   H(Y)−I    │    │
│  │              │; │              │    │
│  │              │Y │              │    │
│  └──────────────┘  └──────────────┘    │
│         H(X)              H(Y)          │
└─────────────────────────────────────────┘
```

---

## Divergensi KL
**Divergensi Kullback-Leibler (KL)** mengukur seberapa berbeda suatu distribusi dengan distribusi lainnya.
D_KL(P || Q) = Σₓ P(x) log [P(x) / Q(x)]
| Properti | Pernyataan |
|----------|-----------|
| Non-negatif | D_KL(P \|\| Q) ≥ 0 (ketidaksamaan Gibbs) |
| Identitas | D_KL(P \|\| Q) = 0 jika P = Q |
| Asimetri | D_KL(P \|\| Q) ≠ D_KL(Q \|\| P) secara umum |
| Bukan metrik | Gagal simetri dan pertidaksamaan segitiga |
**Interpretasi:** D_KL(P || Q) adalah jumlah bit tambahan yang diperlukan untuk menyandikan data dari P menggunakan kode yang dioptimalkan untuk Q.
### Hubungan dengan Besaran Lain
| Hubungan | Rumus |
|-------------|---------|
| Entropi silang | H(P, Q) = H(P) + D_KL(P \|\| Q) |
| Saling informasi | Saya(X; Y) = D_KL(P(X,Y) \|\| P(X)P(Y)) |
| KL Bersyarat | D_KL(P(Y\|X) \|\| Q(Y\|X)) dirata-ratakan pada X |
---

## Lintas Entropi
**Entropi silang** antara distribusi P dan Q:
H(P, Q) = −Σₓ P(x) log Q(x) = H(P) + D_KL(P || Q)
### Cross-Entropy sebagai Fungsi Kerugian
Dalam klasifikasi, P adalah distribusi sebenarnya (label berkode one-hot) dan Q adalah distribusi prediksi model.
**Entropi silang biner (BCE):**
L = −[y log(ŷ) + (1−y) log(1−ŷ)]
**Entropi silang kategoris:**
L = −Σᵢ yᵢ log(ŷᵢ)
| Skenario | kamu (benar) | ŷ (diprediksi) | Kerugian |
|----------|----------|---------------|------|
| Benar, percaya diri | 1 | 0,95 | 0,051 |
| Benar, tidak pasti | 1 | 0,55 | 0,598 |
| Salah, percaya diri | 1 | 0,05 | 2.996 |
| Salah, tidak pasti | 1 | 0,45 | 0,799 |
Meminimalkan entropi silang sama dengan meminimalkan divergensi KL dari distribusi sebenarnya — itulah sebabnya fungsi ini berfungsi dengan baik sebagai fungsi kerugian.
---

## Kapasitas Saluran
### Model Saluran Komunikasi
```
X → [Channel] → Y
```

- X: masukan variabel acak
- Y: keluaran variabel acak
- Saluran: ditentukan oleh probabilitas bersyarat p(y|x)
### Teorema Pengkodean Saluran Bising Shannon
Untuk saluran dengan kapasitas C, jika laju transmisi R< C, there exists a coding scheme that achieves arbitrarily small error probability. If R >C, komunikasi yang andal tidak mungkin dilakukan.
**Kapasitas saluran:**
C = maks_{p(x)} saya(X; Y)
### Contoh Saluran Penting
| Saluran | Deskripsi | Kapasitas |
|---------|-------------|----------|
| **Biner simetris (BSC)** | Membalik setiap bit dengan probabilitas p | 1 − H(p) bit |
| **Penghapusan biner (BEC)** | Menghapus setiap bit dengan probabilitas ε | 1 − ε bit |
| **Gaussian (AWGN)** | Y = X + Z, Z ~ N(0, σ²) | (1/2)log(1 + SNR) bit |
| **Biner tak bersuara** | Transmisi sempurna | 1 sedikit |
---

## Pengodean dan Kompresi Sumber
### Teorema Pengkodean Sumber
Jumlah rata-rata bit yang diperlukan untuk menyandikan suatu sumber dibatasi oleh entropinya:
L ≥ H(X)
Kode optimal mencapai L ≈ H(X).
### Pengkodean Huffman
Kode **bebas awalan** yang menetapkan kode lebih pendek ke simbol yang lebih mungkin.
| Simbol | Probabilitas | Kode Huffman | Panjang |
|--------|-------------|-------------|--------|
| SEBUAH | 0,5 | 0 | 1 |
| B | 0,25 | 10 | 2 |
| C | 0,125 | 110 | 3 |
| D | 0,125 | 111 | 3 |
Panjang rata-rata: 0,5(1) + 0,25(2) + 0,125(3) + 0,125(3) = 1,75 bit/simbol
Entropi: H = 1,75 bit/simbol (optimal dalam kasus ini!)
### Kompresi Lossless vs Lossy
| Ketik | Prinsip | Contoh | Batasi |
|------|-----------|----------|-------|
| **Tanpa Rugi** | Hapus redundansi statistik | ZIP, PNG, FLAC | Laju entropi H(X) |
| **Rugi** | Hapus informasi yang dianggap tidak relevan | JPEG, MP3, H.264 | Fungsi distorsi laju R(D) |
**Teori distorsi laju:** Untuk kompresi lossy dengan distorsi maksimum D, laju minimumnya adalah R(D) = min I(X; X̂) sesuai dengan E[d(X, X̂)] ≤ D.
---

## Koneksi ke Bidang Lain
### Teori Informasi dan Termodinamika
| Konsep | Information Theory | Thermodynamics |
|---------|-------------------|----------------|
| Entropi | Shannon entropy H(X) | Entropi Boltzmann S = k_B ln W |
| Maximum entropy | Uniform distribution | Thermal equilibrium |
| KL divergence | Perbedaan Distribusi | Free energy difference |
| Saling informasi | Shared information | Korelasi dalam sistem fisik |
Bentuk matematikanya identik — Shannon sengaja meminjam istilah "entropi" dari mekanika statistik.
### Teori dan Statistik Informasi
| Konsep | Aplikasi |
|---------|-------------|
| Kemungkinan maksimum | Setara dengan meminimalkan divergensi KL dari distribusi empiris ke model |
| Informasi nelayan | Kelengkungan divergensi KL; batas bawah varian penduga (Cramér-Rao) |
| Panjang deskripsi minimum (MDL) | Pemilihan model dengan meminimalkan total panjang pengkodean |
| AIC / BIC | Perkiraan kriteria pemilihan model berbasis KL |
---

## Relevansi dengan Pembelajaran Mesin dan Ilmu Data
| Konsep TI | Aplikasi ML |
|-----------|----------------|
| Kerugian lintas entropi | Kerugian klasifikasi default (biner dan kelas jamak) |
| Divergensi KL | Kehilangan VAE (istilah regularisasi), pencocokan distribusi, distilasi |
| Saling informasi | Seleksi fitur (MIFS), pembelajaran representasi (InfoMax), penguraian |
| Entropi | Kriteria pemisahan pohon keputusan (perolehan informasi), eksplorasi dalam RL (entropi maksimum RL) |
| Kapasitas saluran | Kompleksitas komunikasi, pemahaman batasan generalisasi |
| Pengkodean sumber | Kompresi data untuk penyimpanan dan transmisi, pengkodean yang efisien |
| Entropi maksimum | Pengklasifikasi MaxEnt, seleksi sebelumnya dalam inferensi Bayesian |
| Distorsi laju | Memahami trade-off dalam kompresi lossy, kuantisasi dalam jaringan saraf |
| Informasi nelayan | Penurunan gradien alami, memahami sensitivitas parameter |
| MDL/AIC/BIC | Pemilihan model, mencegah overfitting |
---

## Ringkasan
| Kuantitas | Rumus (diskrit) | Arti |
|----------|-------------------|---------|
| Entropi H(X) | −Σ p(x) log p(x) | Ketidakpastian rata-rata |
| Entropi gabungan H(X,Y) | −Σ p(x,y) log p(x,y) | Ketidakpastian total pasangan |
| Entropi bersyarat H(Y\|X) | H(X,Y) − H(X) | Ketidakpastian yang tersisa tentang Y diberikan X |
| Informasi timbal balik I(X;Y) | H(X) − H(X\|Y) | Informasi yang dibagikan antara X dan Y |
| Divergensi KL D_KL(P\|\|Q) | Σ P(x) log(P(x)/Q(x)) | "Jarak" antar distribusi |
| Entropi silang H(P,Q) | −Σ P(x) log Q(x) | Pengkodean biaya menggunakan distribusi yang salah |
| Kapasitas saluran C | maks I(X;Y) | Kecepatan komunikasi maksimum yang dapat diandalkan |
Teori informasi memberikan batasan mendasar tentang apa yang dapat dipelajari, dikompresi, dan dikomunikasikan. Bagi praktisi pembelajaran mesin, hal ini menjelaskan mengapa entropi silang berfungsi sebagai fungsi kerugian, cara mengukur kualitas representasi yang dipelajari, dan cara memikirkan trade-off antara kompleksitas model dan kesesuaian data. Wawasan Shannon dari tahun 1948 tetap relevan dengan AI modern dan juga telekomunikasi.