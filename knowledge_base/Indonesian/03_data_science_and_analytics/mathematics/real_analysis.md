---
# Metadata
title: "Real Analysis"
description: "Sequences and series, limits, continuity, differentiability, Riemann and Lebesgue integration, metric spaces, uniform convergence, and measure theory"
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
    changes: "Initial deep-dive into real analysis"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2027-02-10"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-10"

# Classification
tags: [real-analysis, sequences, series, limits, continuity, integration, metric-spaces, measure-theory, convergence]
difficulty_level: "advanced"
prerequisites:
  - "mathematics.md"
  - "discrete_mathematics.md"
estimated_reading_time: "30 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Analisis Nyata
Analisis nyata adalah dasar kalkulus yang kuat. Meskipun kalkulus pengantar mengajarkan Anda cara menghitung turunan dan integral, analisis sebenarnya menanyakan *mengapa* teknik ini berhasil — dan kapan gagal. Ini memberikan definisi yang tepat tentang batasan, kontinuitas, konvergensi, dan integrasi yang mendukung teori probabilitas, analisis fungsional, pengoptimalan, dan jaminan teoretis di balik algoritme pembelajaran mesin.
---

## Urutan dan Seri
### Urutan
**Deret** adalah daftar bilangan real yang diurutkan (aₙ)ₙ₌₁^∞. Pertanyaan utamanya adalah: apakah barisan **menyatu** hingga suatu batas?
**Definisi Konvergensi:** Suatu barisan (aₙ) konvergen ke L jika untuk setiap ε > 0 terdapat N sehingga untuk semua n > N: |aₙ − L| <ε.
| Konsep | Definisi | Contoh |
|---------|------------|---------|
| **Konvergen** | lim aₙ = L ada dan terbatas | aₙ = 1/n → 0 |
| **Divergen** | Tidak menyatu | aₙ = (−1)ⁿ berosilasi |
| **Divergen ke ∞** | aₙ tumbuh tanpa batas | aₙ = n² → ∞ |
| **Dibatasi** | \|aₙ\| ≤ M untuk beberapa M | Setiap barisan konvergen dibatasi |
| **Mototon** | Entah selalu tidak berkurang atau tidak bertambah | aₙ = 1 − 1/n bertambah |
| **Urutan Cauchy** | ∀ε > 0, ∃N: ∀m,n > N, \|aₘ − aₙ\| <ε | Dalam ℝ, Cauchy ⟺ konvergen |
**Teorema kunci:**
- **Teorema Konvergensi Monoton:** Setiap barisan monoton berbatas konvergen
- **Teorema Bolzano-Weierstrass:** Setiap barisan berbatas mempunyai barisan yang konvergen
- **Kelengkapan ℝ:** Setiap barisan Cauchy di ℝ konvergen (ini yang membedakan ℝ dari ℚ)
### Seri
**Deret** adalah jumlah suatu barisan: Σₙ₌₁^∞ aₙ. Deret tersebut konvergen jika barisan jumlah parsial Sₙ = Σₖ₌₁ⁿ aₖ konvergen.
### Tes Konvergensi
| Tes | Kondisi | Kesimpulan |
|------|-----------|------------|
| **Uji Divergensi** | lim aₙ ≠ 0 | Seri menyimpang |
| **Uji perbandingan** | 0 ≤ aₙ ≤ bₙ dan Σbₙ konvergen | Σaₙ konvergen |
| **Uji rasio** | lim \|aₙ₊₁/aₙ\| = L | Konvergen jika L< 1, diverges if L >1 |
| **Uji akar** | lim sup \|aₙ\|^(1/n) = L | Menyatu jika L< 1, diverges if L >1 |
| **Tes integral** | aₙ = f(n), f menurun, positif | Σaₙ konvergen jika ∫f(x)dx konvergen |
| **Seri bergantian** | aₙ menurun, lim aₙ = 0, tanda bolak-balik | Deret konvergen |
| **Konvergensi mutlak** | Σ\|aₙ\| menyatu | Σaₙ konvergen (dan penataan ulang menghasilkan jumlah yang sama) |
| **Konvergensi bersyarat** | Σaₙ konvergen tetapi Σ\|aₙ\| menyimpang | Penataan ulang dapat menghasilkan jumlah berapa pun (Riemann) |
### Seri Penting
| Seri | Jumlah | Kondisi |
|--------|-----|-----------|
| Geometris: Σ rⁿ | 1/(1−r) | \|r\| < 1 |
| p-series: Σ 1/nᵖ | Converges | p >1 |
| Harmonik: Σ 1/n | Divergen (= ∞) | — |
| Eksponensial: Σ xⁿ/n! | eˣ | Semua x |
| Taylor untuk ln(1+x): Σ (−1)ⁿ⁺¹xⁿ/n | ln(1+x) | −1 < x ≤ 1 |
---

## Batasan dan Kontinuitas
### Batasan Fungsi
**Definisi:** lim_{x→c} f(x) = L artinya: untuk setiap ε > 0, terdapat δ > 0 sehingga 0 < |x − c| < δ menyiratkan |f(x) − L| <ε.
Ini adalah definisi **ε-δ** — versi ketat dari "f(x) mendekati L saat x mendekati c."
### Kontinuitas
Suatu fungsi f **kontinu di c** jika lim_{x→c} f(x) = f(c). Setara: untuk setiap ε > 0, terdapat δ > 0 sehingga |x − c| < δ menyiratkan |f(x) − f(c)| <ε.
**Jenis diskontinuitas:**
| Ketik | Deskripsi | Contoh |
|------|-------------|---------|
| Dapat dilepas | Batasnya ada tetapi ≠ f(c) | f(x) = sin(x)/x pada x = 0 |
| Lompat | Batas kiri dan kanan ada tetapi berbeda | Fungsi langkah |
| Tak Terbatas | Batasnya adalah ±∞ | f(x) = 1/x² pada x = 0 |
| Berosilasi | Batas tidak ada | f(x) = sin(1/x) di x = 0 |
### Teorema Kunci untuk Fungsi Kontinu
| Teorema | Pernyataan |
|---------|-----------|
| **Teorema Nilai Menengah** | Jika f kontinu pada [a,b] dan f(a) < k < f(b), maka ∃c ∈ (a,b): f(c) = k |
| **Teorema Nilai Ekstrem** | Jika f kontinu pada [a,b], f mencapai maksimum dan minimum pada [a,b] |
| **Teorema Keterbatasan** | Jika f kontinu pada [a,b], f dibatasi pada [a,b] |
| **Kontinuitas Seragam** | f kontinu seragam di [a,b] jika f kontinu di [a,b] (Heine-Cantor) |
**Contoh Kerja (IVT):** Tunjukkan x³ + x − 1 = 0 memiliki solusi dalam (0, 1).
- Misalkan f(x) = x³ + x − 1. f kontinu (polinomial).
- f(0) = −1< 0 and f(1) = 1 >0.
- Dengan IVT, ∃c ∈ (0,1): f(c) = 0.
---

## Diferensiasi
### Definisi
f'(c) = lim_{h→0} (f(c+h) − f(c)) / jam
Jika batas ini ada, f **dapat dibedakan** di c.
### Diferensiabilitas vs Kontinuitas
| Hubungan | Pernyataan |
|--------------|-----------|
| Dapat Dibedakan → Kontinu | Jika f terdiferensialkan di c, f kontinu di c |
| Kontinu ↛ Dapat Didiferensiasi | f(x) = \|x\| kontinu di 0 tetapi tidak terdiferensiasi di sana |
| Tidak ada tempat yang dapat dibedakan | Fungsi Weierstrass: kontinu di mana saja, tidak dapat dibedakan di mana pun |
### Hasil Utama
| Teorema | Pernyataan |
|---------|-----------|
| **Teorema Nilai Rata-rata** | Jika f kontinu di [a,b] dan terdiferensialkan di (a,b), ∃c: f'(c) = (f(b)−f(a))/(b−a) |
| **Teorema Rolle** | Kasus khusus MVT ketika f(a) = f(b): ∃c: f'(c) = 0 |
| **Peraturan L'Hôpital** | Jika lim f/g = 0/0 atau ∞/∞, maka lim f/g = lim f'/g' (jika ada yang terakhir) |
| **Teorema Taylor** | f(x) = Σₖ₌₀ⁿ f⁽ᵏ⁾(a)/k! · (x−a)ᵏ + Rₙ(x) dengan sisa eksplisit |
---

## Integrasi
### Integrasi Riemann
**Integral Riemann** mendefinisikan ∫ₐᵇ f(x)dx sebagai limit jumlah Riemann.
**Konstruksi:**
1. Partisi [a,b] menjadi subinterval: P = {x₀, x₁, ..., xₙ}
2. Pilih titik sampel tᵢ ∈ [xᵢ₋₁, xᵢ]
3. Jumlah Riemann: S(P,f) = Σᵢ f(tᵢ)(xᵢ − xᵢ₋₁)
4. Jika limit S(P,f) terdapat pada mesh → 0, f merupakan integral Riemann
**Kriteria keterintegrasian Riemann:**
| Kondisi | Dapat diintegrasikan? |
|-----------|-------------|
| Berkelanjutan pada [a,b] | Ya |
| Dibatasi dengan banyak diskontinuitas | Ya |
| Monoton pada [a,b] | Ya |
| Fungsi Dirichlet (1 pada ℚ, 0 pada irasional) | Tidak |
### Teorema Dasar Kalkulus
| Bagian | Pernyataan |
|------|-----------|
| **Bagian 1** | Jika f kontinu di [a,b], maka F(x) = ∫ₐˣ f(t)dt terdiferensiasi dan F'(x) = f(x) |
| **Bagian 2** | Jika F' = f dan f merupakan integral Riemann, maka ∫ₐᵇ f(x)dx = F(b) − F(a) |
### Integrasi Lebesgue
Integral Riemann memiliki keterbatasan - tidak dapat mengintegrasikan banyak fungsi yang muncul dalam analisis dan probabilitas. **Integral Lebesgue** memperluas integrasi ke kelas fungsi yang lebih luas.
**Ide utama:** Daripada mempartisi domain (sumbu x), partisilah rentang (sumbu y).
| Aspek | Integral Riemann | Integral Lebesgue |
|--------|-----------------|-------------------|
| Pendekatan | Domain partisi (sumbu x) | Rentang partisi (sumbu y) |
| Terintegrasi | Terus menerus, sedikit demi sedikit terus menerus | Fungsi terukur |
| Batasi teorema | Lemah | Kuat (Konvergensi Dominasi, Konvergensi Monoton) |
| Menangani | Fungsi "Bagus" | Fungsi dengan diskontinuitas padat |
| Yayasan | Kalkulus klasik | Teori probabilitas modern |
**Kriteria Lebesgue:** f dapat diintegralkan Riemann pada [a,b] jika f terbatas dan kontinu hampir di semua tempat (himpunan diskontinuitas mempunyai ukuran nol).
---

## Ruang Metrik
**Ruang metrik** menggeneralisasi gagasan "jarak" ke himpunan abstrak.
### Definisi
**ruang metrik** (X, d) adalah himpunan X dengan fungsi jarak d: X × X → ℝ memuaskan:
| Aksioma | Pernyataan |
|-------|-----------|
| Non-negatif | d(x,y) ≥ 0 |
| Identitas | d(x,y) = 0 jika x = y |
| Simetri | d(x,y) = d(y,x) |
| Ketimpangan segitiga | d(x,z) ≤ d(x,y) + d(y,z) |
### Ruang Metrik Umum
| Ruang | Tetapkan | Metrik | Aplikasi |
|-------|-----|--------|-------------|
| ℝⁿ dengan Euclidean | ℝⁿ | d(x,y) = √Σ(xᵢ−yᵢ)² | Geometri standar |
| ℝⁿ dengan Manhattan | ℝⁿ | d(x,y) = Σ\|xᵢ−yᵢ\| | Jalur berbasis grid, LASSO |
| ℝⁿ dengan Chebyshev | ℝⁿ | d(x,y) = maks\|xᵢ−yᵢ\| | Jarak raja catur |
| Metrik diskrit | Set apa saja | d(x,y) = 1 jika x≠y, 0 jika x=y | Contoh Topologi |
| Ruang fungsi C[a,b] | Fungsi berkelanjutan | d(f,g) = maks\|f(x)−g(x)\| | Teori pendekatan |
| ruang | fungsi yang dapat diintegrasikan p | d(f,g) = (∫\|f−g\|ᵖ)^(1/p) | Analisis fungsional, norma ML |
### Konsep Topologi dalam Ruang Metrik
| Konsep | Definisi | Contoh |
|---------|------------|---------|
| **Buka bola** | B(x,r) = {y : d(x,y) < r} | Interval terbuka (x−r, x+r) di ℝ |
| **Buka set** | Setiap titik mempunyai bola yang terdapat pada himpunan | (0,1) terbuka di ℝ |
| **Set tertutup** | Komplemen himpunan terbuka | [0,1] ditutup pada ℝ |
| **Penutupan** | Himpunan tertutup terkecil yang mengandung S | Penutupan (0,1) = [0,1] |
| **Ringkas** | Setiap sampul terbuka mempunyai subcover yang terbatas | Dalam ℝⁿ: tertutup dan dibatasi (Heine-Borel) |
| **Lengkap** | Setiap barisan Cauchy konvergen | ℝ selesai; ℚ bukan |
---

## Konvergensi Seragam
Barisan fungsi (fₙ) dapat konvergen dalam dua cara:
| Ketik | Definisi | Mempertahankan Kontinuitas? |
|------|------------|----------------------|
| **Searah** | ∀x: fₙ(x) → f(x) | Tidak |
| **Seragam** | sup\|fₙ(x) − f(x)\| → 0 | Ya |
**Konvergensi seragam** lebih kuat: laju konvergensi sama di semua tempat.
**Teorema kunci:**
- Batas seragam fungsi kontinu adalah kontinu
- Limit seragam fungsi integral Riemann adalah integral Riemann, dan integral limitnya sama dengan limit integralnya
- **Uji M Weierstrass:** Jika |fₙ(x)| ≤ Mₙ untuk semua x dan ΣMₙ konvergen, maka Σfₙ konvergen seragam
---

## Teori Ukur
**Teori ukuran** menggeneralisasi konsep panjang, luas, dan volume.
### Definisi
**Ukuran** pada himpunan X adalah fungsi μ: Σ → [0, ∞] (dengan Σ adalah aljabar σ dari himpunan bagian) yang memuaskan:
- μ(∅) = 0
- **Tambahan yang dapat dihitung:** μ(∪ᵢ Aᵢ) = Σᵢ μ(Aᵢ) untuk Aᵢ yang terputus-putus
### Ukuran Lebesgue
**Ukuran Lebesgue** λ pada ℝ memperluas gagasan tentang panjang:
| Tetapkan | Ukuran Lebesgue |
|-----|-----------------|
| Interval [a,b] | b− a |
| Titik tunggal {x} | 0 |
| Himpunan terbatas | 0 |
| Himpunan yang dapat dihitung (mis., ℚ) | 0 |
| Kumpulan penyanyi | 0 (tidak terhitung tetapi diukur nol) |
| [0,1] ∩ ℚ | 0 |
| [0,1] \ ℚ | 1 |
### Konsep Utama
| Konsep | Definisi |
|---------|------------|
| **Hampir di semua tempat (a.e.)** | Suatu properti berlaku kecuali pada himpunan ukuran nol |
| **Fungsi terukur** | Preimage dari setiap set terbuka dapat diukur |
| **Integral Lebesgue** | Integral didefinisikan menggunakan teori ukuran |
| **Lᵖ spasi** | Ruang fungsi dengan integral daya ke-p berhingga |
### Teorema Konvergensi Penting
Teorema berikut adalah alasan mengapa integrasi Lebesgue lebih disukai dalam matematika tingkat lanjut:
| Teorema | Pernyataan |
|---------|-----------|
| **Konvergensi Monoton** | Jika fₙ ↑ f searah dan fₙ ≥ 0, maka ∫fₙ → ∫f |
| **Konvergensi yang Didominasi** | Jika fₙ → f searah dan \|fₙ\| ≤ g (terintegrasi), maka ∫fₙ → ∫f |
| **Lema Fatou** | ∫lim inf fₙ ≤ lim inf ∫fₙ |
Teorema ini memungkinkan pertukaran limit dan integral — sesuatu yang gagal dalam integrasi Riemann secara umum.
---

## Relevansi dengan Pembelajaran Mesin dan Ilmu Data
| Konsep Analisis | Aplikasi |
|-----------------|-------------|
| Batasan dan konvergensi | Memahami kapan algoritma berulang (gradient descending, EM) bertemu |
| Kontinuitas | Fungsi aktivasi harus kontinyu untuk backpropagation |
| Diferensiabilitas | Pengoptimalan berbasis gradien memerlukan fungsi kerugian yang dapat dibedakan |
| Teorema Nilai Rata-rata | Batas kesalahan dalam perkiraan numerik, bukti konvergensi |
| Ruang metrik | Fungsi jarak dalam clustering (k-means, DBSCAN), tetangga terdekat |
| Kekompakan | Bukti keberadaan solusi optimal, Heine-Borel dalam optimasi dimensi hingga |
| Konvergensi seragam | Menjamin bahwa perkiraan (perkiraan universal jaringan saraf) berfungsi di mana saja |
| Teori pengukuran | Landasan probabilitas modern (probabilitas adalah ukuran), nilai yang diharapkan sebagai integral Lebesgue |
| Integrasi Lebesgue | Nilai yang diharapkan E[X] = ∫X dP merupakan integral Lebesgue |
| spasi | L¹ (LASSO), L² (Ridge), Lᵖ norma dalam regularisasi |
| Konvergensi yang Didominasi | Membuktikan konsistensi penduga, pertukaran batas dalam inferensi Bayesian |
---

## Ringkasan
| Topik | Ide Inti | Hasil Utama |
|-------|-----------|------------|
| Urutan | Daftar nomor yang diurutkan | Konvergensi, kriteria Cauchy, Bolzano-Weierstrass |
| Seri | Jumlah tak terbatas | Tes konvergensi, absolut vs bersyarat |
| Batas | Pendekatan yang ketat untuk "mendekati" | definisi ε-δ |
| Kontinuitas | Tidak ada istirahat atau lompatan | IVT, Teorema Nilai Ekstrem |
| Diferensiasi | Laju perubahan seketika | Teorema Nilai Rata-rata, Teorema Taylor |
| Integrasi Riemann | Area di bawah kurva | Teorema Dasar Kalkulus |
| Integrasi Lebesgue | Integrasi melalui ukuran | Konvergensi yang Didominasi/Monoton |
| Ruang Metrik | Jarak abstrak | Himpunan terbuka/tertutup, kekompakan, kelengkapan |
| Konvergensi Seragam | Konvergensi pada tingkat yang sama di semua tempat | Menjaga kesinambungan dan keterpaduan |
| Teori Ukur | Panjang/luas/volume umum | Landasan probabilitas, ukuran Lebesgue |
Analisis nyata adalah tempat berkembangnya matematika. Ini menggantikan gagasan intuitif tentang "mendekati", "berkelanjutan", dan "area" dengan definisi tepat yang dapat dibuktikan dan digeneralisasikan. Bagi ilmuwan data dan teknisi ML, analisis memberikan jaminan teoretis: kapan penurunan gradien bertemu? Kapan fungsi kerugian berperilaku baik? Kapan kita bisa bertukar batasan dan ekspektasi? Ini bukanlah pertanyaan filosofis — pertanyaan ini menentukan apakah algoritme Anda berfungsi atau gagal secara diam-diam.