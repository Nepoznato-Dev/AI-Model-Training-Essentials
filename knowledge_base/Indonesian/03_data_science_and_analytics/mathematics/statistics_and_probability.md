---
# Metadata
title: "Statistics and Probability"
description: "Probability theory, statistical inference, hypothesis testing, regression, and Bayesian methods"
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
    date: "2026-08-09"
    author: "Nepoznato-Dev"
    changes: "Split from mathematics_and_logic.md; expanded into standalone file"

# Review
created: "2026-08-09"
last_modified: "2026-08-09"
review_date: "2027-02-09"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-09"

# Classification
tags: [statistics, probability, hypothesis-testing, regression, bayesian-methods, data-analysis]
difficulty_level: "intermediate"
prerequisites:
  - "../mathematics/mathematics.md"
estimated_reading_time: "14 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Statistik dan Probabilitas
Probabilitas dan statistik adalah dasar matematika dari ilmu data, pembelajaran mesin, dan penelitian ilmiah. Probabilitas memberi tahu Anda seberapa besar kemungkinan suatu peristiwa terjadi; statistik memberi tahu Anda cara menarik kesimpulan dari data. Bersama-sama, mereka mengubah ketidakpastian menjadi pengetahuan yang dapat diukur dan dikelola.
---

## Teori Probabilitas
### Konsep Inti
| Konsep | Deskripsi | Contoh |
|---------|-------------|---------|
| **Ruang Sampel** | Himpunan semua hasil yang mungkin | Pelemparan sebuah dadu: {1, 2, 3, 4, 5, 6} |
| **Acara** | Bagian dari ruang sampel | Menggulirkan bilangan genap: {2, 4, 6} |
| **Probabilitas** | Angka antara 0 dan 1 mengukur kemungkinan | P(bergulir 6) = 1/6 |
| **Probabilitas Bersyarat** | P(A|B): probabilitas A tertentu B telah terjadi | P(hujan | mendung) |
| **Kemerdekaan** | Peristiwa dimana yang satu tidak mempengaruhi yang lain | Pembalikan koin bersifat independen |
### Aturan Probabilitas
| Aturan | Rumus | Kasus Penggunaan |
|------|---------|----------|
| **Aturan Penjumlahan** | P(A ∪ B) = P(A) + P(B) − P(A ∩ B) | Probabilitas A atau B |
| **Aturan Perkalian** | P(A ∩ B) = P(A) × P(B|A) | Probabilitas A dan B |
| **Aturan Pelengkap** | P(bukan A) = 1 − P(A) | Probabilitas suatu peristiwa tidak terjadi |
| **Hukum Probabilitas Total** | P(A) = Σ P(A|Bᵢ) × P(Bᵢ) | Partisi berdasarkan acara yang saling eksklusif |
| **Teorema Bayes** | P(A|B) = P(B|A) × P(A) / P(B) | Memperbarui keyakinan dengan bukti |
### Distribusi Probabilitas
| Distribusi | Ketik | Parameter Kunci | Kasus Penggunaan |
|-------------|------|----------------|----------|
| **Normal (Gaussian)** | Terus menerus | Rata-rata (μ), Standar deviasi (σ) | Fenomena alam, kesalahan pengukuran |
| **Binomial** | Diskrit | n (percobaan), p (probabilitas) | Jumlah keberhasilan/kegagalan |
| **Racun** | Diskrit | λ (tingkat) | Peristiwa langka dalam waktu/ruang |
| **Eksponensial** | Terus menerus | λ (nilai) | Waktu antar acara |
| **Seragam** | Keduanya | a, b (batas) | Kemungkinan hasil yang sama |
| **Chi-Kuadrat** | Terus menerus | k (derajat kebebasan) | Tes kesesuaian |
| **t-Distribusi** | Terus menerus | ν (derajat kebebasan) | Inferensi sampel kecil |
### Properti Utama Distribusi
| Properti | Deskripsi |
|----------|-------------|
| **Rata-rata (Nilai yang Diharapkan)** | Pusat massa distribusi: E[X] = Σ xᵢ × P(xᵢ) |
| **Varians** | Sebaran di sekitar mean: Var(X) = E[(X − μ)²] |
| **Deviasi Standar** | Akar kuadrat dari varians; satuan yang sama dengan data |
| **Kemiringan** | Asimetri distribusi |
| **Kurtosis** | "Tailedness" — seberapa berat ekornya |
---

## Inferensi Statistik
### Statistik Deskriptif vs. Inferensial
| | Deskriptif | Inferensial |
|---|-------------|-------------|
| **Tujuan** | Meringkas dan mendeskripsikan data | Menarik kesimpulan tentang suatu populasi dari sampel |
| **Alat** | Mean, median, modus, deviasi standar, grafik | Uji hipotesis, interval kepercayaan, regresi |
| **Ruang Lingkup** | Hanya data yang Anda miliki | Generalisasi di luar sampel Anda |
### Kerangka Pengujian Hipotesis
| Langkah | Deskripsi |
|------|-------------|
| 1. **Nyatakan hipotesis** | Hipotesis nol (H₀): tidak berpengaruh; Alternatif (H₁): efek ada |
| 2. **Pilih tingkat signifikansi** | α = 0,05 (konvensional) |
| 3. **Pilih tes** | Berdasarkan tipe data, ukuran sampel, dan asumsi |
| 4. **Hitung statistik pengujian** | Tergantung tes yang dipilih |
| 5. **Temukan nilai p** | Peluang mengamati data jika H₀ benar |
| 6. **Ambil keputusan** | Jika p < α, tolak H₀; jika tidak, gagal menolak H₀ |
### Tes Statistik Umum
| Tes | Kapan Menggunakan | Apa Perbandingannya |
|------|-------------|-----------------|
| **uji-t** | Bandingkan rata-rata 1–2 kelompok | Kelompok berarti terhadap suatu nilai atau terhadap satu sama lain |
| **Uji chi-kuadrat** | Data kategorikal | Frekuensi yang diamati vs. yang diharapkan |
| **ANOVA** | Bandingkan rata-rata 3+ grup | Varians antar kelompok vs. dalam kelompok |
| **Mann-Whitney U** | Alternatif non-parametrik untuk uji-t | Distribusi peringkat dua kelompok |
| **Korelasi Pearson** | Hubungan linier antara dua variabel kontinu | nilai r dari −1 hingga +1 |
| **Korelasi Spearman** | Hubungan monoton (berbasis peringkat) | nilai ρ untuk data ordinal atau tidak normal |
### Interval Keyakinan
Interval kepercayaan memberikan kisaran nilai yang masuk akal untuk parameter populasi:
- **95% CI untuk mean** (dikenal σ): x̄ ± 1,96 × (σ / √n)
- **Interpretasi**: "Kami 95% yakin bahwa rata-rata populasi sebenarnya berada dalam interval ini"
- **CI yang lebih luas** = ketidakpastian yang lebih besar (sampel lebih kecil, variabilitas lebih tinggi, atau tingkat kepercayaan lebih tinggi)
---

## Analisis Regresi
### Jenis Regresi
| Ketik | Variabel Dependen | Kasus Penggunaan |
|------|-------------------|----------|
| **Regresi Linier** | Terus menerus | Memprediksi harga rumah, penjualan |
| **Regresi Logistik** | Biner (0/1) | Klasifikasi: deteksi spam, diagnosis penyakit |
| **Regresi Polinomial** | Kontinu (melengkung) | Kurva pertumbuhan, tren non-linier |
| **Regresi Berganda** | Berkelanjutan (2+ prediktor) | Mengontrol perancu |
| **Punggungan / Laso** | Berkelanjutan (diatur) | Mencegah overfitting, pemilihan fitur |
### Dasar-dasar Regresi Linier
Modelnya: **y = β₀ + β₁x + ε**
| Komponen | Arti |
|-----------|---------|
| β₀ (mencegat) | Nilai y bila x = 0 |
| β₁ (kemiringan) | Perubahan y untuk perubahan satu satuan pada x |
| ε (istilah kesalahan) | Variasi yang tidak dapat dijelaskan |
**Metrik utama:**
- **R² (koefisien determinasi)**: Proporsi varians yang dijelaskan oleh model (0 hingga 1)
- **R² yang Disesuaikan**: R² dikenai penalti untuk jumlah prediktor
- **RMSE**: Root mean squared error — kesalahan prediksi rata-rata dalam satuan yang sama dengan y
### Asumsi Regresi Linier
| Asumsi | Apa Artinya | Cara Memeriksa |
|-----------|--------------|--------------|
| **Linearitas** | Hubungan antara X dan Y adalah linier | Plot sebar |
| **Kemerdekaan** | Pengamatan bersifat independen | Desain studi |
| **Homoskedastisitas** | Varians residu yang konstan | Plot sisa |
| **Normalitas** | Residu berdistribusi normal | Plot QQ, tes Shapiro-Wilk |
| **Tidak ada multikolinearitas** | Prediktor tidak berkorelasi tinggi | VIF (Faktor Inflasi Varians) |
---

## Statistik Bayesian
### Frekuensiist vs. Bayesian
| | Sering | Bayesian |
|---|-------------|----------|
| **Probabilitas artinya** | Frekuensi jangka panjang | Derajat Keyakinan |
| **Parameternya adalah** | Diperbaiki tetapi tidak diketahui | Variabel acak dengan distribusi |
| **Kegunaan** | nilai p, interval kepercayaan | Distribusi posterior, interval yang kredibel |
| **Kekuatan** | Objektif, mapan | Menggabungkan pengetahuan sebelumnya, interpretasi intuitif |
### Teorema Bayes dalam Praktek
**Posterior = (Kemungkinan × Sebelumnya) / Bukti**
Contoh — pengujian kesehatan:
- Prevalensi penyakit: 1% (sebelumnya)
- Sensitivitas tes: 95% (tingkat positif sebenarnya)
- Spesifisitas tes: 90% (tingkat negatif sebenarnya)
- Jika hasil tes Anda positif: P(penyakit | positif) = (0,95 × 0,01) / (0,95 × 0,01 + 0,10 × 0,99) ≈ 8,8%
Hasil yang berlawanan dengan intuisi ini – sebagian besar hasil positif adalah positif palsu ketika penyakit ini jarang terjadi – adalah **kekeliruan tingkat dasar**, dan ini menunjukkan mengapa pemikiran Bayesian penting.
---

## Tips Praktis
- **Selalu visualisasikan data Anda** sebelum menjalankan uji statistik apa pun
- **Periksa asumsi** — pelanggaran dapat membatalkan hasil
- **Ukuran efek penting** — hasil yang signifikan secara statistik mungkin tidak ada artinya
- **Korelasi bukanlah sebab-akibat** — bahkan korelasi yang kuat pun mungkin memiliki perancu
- **Beberapa perbandingan** meningkatkan tingkat positif palsu — menerapkan koreksi (Bonferroni, FDR)
- **Laporkan interval kepercayaan**, bukan hanya nilai p
---

## Mengapa Ini Penting
Statistik adalah tulang punggung penelitian ilmiah, analisis bisnis, dan pembelajaran mesin. Tanpanya, Anda tidak dapat membedakan sinyal dari noise, mengidentifikasi efek nyata dari fluktuasi acak, atau membuat prediksi dengan ketidakpastian terukur. Baik Anda menganalisis pengujian A/B, melatih model ML, atau membaca makalah penelitian, literasi statistik sangatlah penting.