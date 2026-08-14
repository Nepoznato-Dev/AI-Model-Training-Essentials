---
# Metadata
title: "Numerical Methods"
description: "Floating-point arithmetic, root finding, numerical integration, ODE solvers, interpolation, numerical stability, and conditioning"
category: "Data Science and Analytics"
subcategory: "Mathematics"
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
    date: "2026-08-10"
    author: "AI Model Training Team"
    changes: "Initial deep-dive into numerical methods"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2027-02-10"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-10"

# Classification
tags: [numerical-methods, floating-point, root-finding, numerical-integration, ode-solvers, interpolation, stability]
difficulty_level: "intermediate"
prerequisites:
  - "mathematics.md"
  - "real_analysis.md"
estimated_reading_time: "25 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# Metode Numerik
Metode numerik adalah jembatan antara teori matematika dan komputasi praktis. Meskipun matematika murni membuktikan adanya solusi, metode numerik sebenarnya menghitung perkiraan jawaban dengan presisi terbatas. Setiap model pembelajaran mesin, simulasi fisika, dan saluran analisis data pada akhirnya bergantung pada komputasi numerik. Memahami metode ini – keakuratan, stabilitas, dan keterbatasannya – sangat penting untuk membangun perangkat lunak yang andal.
---

## Aritmatika Titik Mengambang
Komputer mewakili bilangan real dengan presisi terbatas. **Standar IEEE 754** menentukan cara bilangan floating-point disimpan dan dimanipulasi.
### Format IEEE 754
| Format | Bit | Eksponen | Mantissa | Perkiraan Digit Desimal | Rentang |
|--------|------|----------|----------|---------------------------|-------|
| Setengah (fp16) | 16 | 5 | 10 | 3.3 | ±6,5 × 10⁴ |
| Lajang (fp32) | 32 | 8 | 23 | 7.2 | ±3,4 × 10³⁸ |
| Ganda (fp64) | 64 | 11 | 52 | 15.9 | ±1,8 × 10³⁰⁸ |
### Mesin Epsilon
**Mesin epsilon** (ε_mach) adalah bilangan terkecil sehingga 1 + ε_mach > 1 dalam floating-point.
| Format | ε_mach |
|--------|--------|
| fp16 | 2⁻¹⁰ ≈ 9,8 × 10⁻⁴ |
| fp32 | 2⁻²³ ≈ 1,2 × 10⁻⁷ |
| fp64 | 2⁻⁵² ≈ 2,2 × 10⁻¹⁶ |
### Kesalahan Umum
| Jebakan | Contoh | Konsekuensi |
|---------|---------|-------------|
| **Pembatalan bencana** | Menghitung (1 + x) − 1 untuk x kecil | Hilangnya angka penting |
| **Penyerapan** | 10⁸ + 1 = 10⁸ di fp32 | Nilai-nilai kecil hilang dalam jumlah besar |
| **Non-asosiasi** | (a + b) + c ≠ a + (b + c) | Jumlah urutan penting |
| **Pembagian dengan mendekati nol** | 1 / 10⁻³⁰⁰ → meluap | Tak terhingga atau NaN |
### Strategi Mitigasi
| Strategi | Deskripsi |
|----------|-------------|
| **Penjumlahan Kahan** | Penjumlahan terkompensasi untuk mengurangi kesalahan penyerapan |
| **Kahan-Babuska-Neumaier** | Versi penjumlahan Kahan yang ditingkatkan |
| **Penjumlahan yang diurutkan** | Jumlahkan dulu bilangan kecil agar tidak terserap |
| **Aritmatika ganda-ganda** | Gunakan pasangan ganda untuk presisi yang lebih luas |
| **Analisis pengkondisian** | Pahami jika masalahnya sendiri memperparah kesalahan |
---

## Pencarian Akar
Menemukan x sedemikian rupa sehingga f(x) = 0.
### Metode Bagi Dua
| Properti | Nilai |
|----------|-------|
| Membutuhkan | f kontinu, f(a) dan f(b) mempunyai tanda berlawanan |
| Konvergensi | Linear (kesalahan membagi dua setiap langkah) |
| Terjamin? | Ya — selalu menyatu |
| Iterasi untuk d digit | ≈ d / log₁₀(2) ≈ 3,32d |
**Algoritma:**
1. Mulailah dengan interval [a, b] di mana f(a) · f(b) < 0
2. Hitung titik tengah c = (a + b) / 2
3. Jika f(c) = 0 atau |b − a| < toleransi, berhenti
4. Jika f(a) · f(c) < 0, himpunan b = c; jika tidak, tetapkan a = c
5. Ulangi
### Metode Newton-Raphson
| Properti | Nilai |
|----------|-------|
| Membutuhkan | f terdiferensiasi, f'(x) ≠ 0 pada akar |
| Konvergensi | Kuadrat (dekat akar) |
| Terjamin? | Tidak — mungkin menyimpang atau berputar |
| Perbarui aturan | x_{n+1} = x_n − f(x_n) / f'(x_n) |
**Contoh Pekerjaan:** Cari √2 dengan menyelesaikan f(x) = x² − 2 = 0.
- f'(x) = 2x
- x₀ = 1,5
- x₁ = 1,5 − (2,25 − 2) / 3 = 1,5 − 0,0833 = 1,4167
- x₂ = 1,4167 − (2,0069 − 2) / 2,8333 = 1,4142
- x₃ = 1,41421356... (benar hingga 8 desimal)
### Metode Garis Potong
Seperti metode Newton tetapi mendekati turunannya:
x_{n+1} = x_n − f(x_n) · (x_n − x_{n-1}) / (f(x_n) − f(x_{n-1}))
| Properti | Nilai |
|----------|-------|
| Konvergensi | Superlinear (urutan ≈ 1,618, rasio emas) |
| Membutuhkan | Dua tebakan awal (tidak perlu turunan) |
### Perbandingan Metode Pencarian Akar
| Metode | Konvergensi | Dibutuhkan Derivatif? | Terjamin? | Biaya per Langkah |
|--------|-------------|-------------------|-------------|---------------|
| Bagi dua | Linier (1) | Tidak | Ya | 1 fungsi evaluasi |
| Newton-Raphson | Kuadrat (2) | Ya | Tidak | 2 evaluasi fungsi |
| Garis potong | Superlinier (1.618) | Tidak | Tidak | 1 fungsi evaluasi |
| Metode Brent | Superlinier | Tidak | Ya | Bervariasi |
**Metode Brent** menggabungkan pembagian dua (konvergensi terjamin) dengan interpolasi kuadrat potong/terbalik (konvergensi cepat). Ini adalah pencari root default di sebagian besar perpustakaan numerik.
---

## Integrasi Numerik (Kuadrat)
Menghitung kira-kira ∫ₐᵇ f(x) dx.
### Metode
| Metode | Rumus | Kesalahan | Pesan |
|--------|---------|-------|-------|
| **Persegi Panjang (titik tengah)** | (b−a) · f((a+b)/2) | HAI(h²) | 1 |
| **Trapesium** | (b−a)/2 · [f(a) + f(b)] | HAI(h²) | 2 |
| **1/3 Simpson** | (b−a)/6 · [f(a) + 4f(m) + f(b)] | HAI(h⁴) | 3 |
| **Simpson 3/8** | Menggunakan 4 titik yang berjarak sama | HAI(h⁴) | 4 |
| **Kuadratur Gaussian** | Penempatan node yang optimal | HAI(h²ⁿ) | n poin |
### Aturan Gabungan
Untuk n subinterval lebar h = (b−a)/n:
| Aturan | Rumus Komposit | Kesalahan |
|------|-------------------|-------|
| Trapesium Komposit | h[f(a)/2 + Σf(xᵢ) + f(b)/2] | HAI(h²) |
| Komposit Simpson | h/3[f(a) + 4Σf(ganjil) + 2Σf(genap) + f(b)] | HAI(h⁴) |
**Contoh Pekerjaan:** Perkiraan ∫₀¹ e^(−x²) dx menggunakan trapesium komposit dengan n = 4.
- h = 0,25, poin: 0, 0,25, 0,5, 0,75, 1
- f(0) = 1, f(0,25) = 0,9394, f(0,5) = 0,7788, f(0,75) = 0,5698, f(1) = 0,3679
- T = 0,25[1/2 + 0,9394 + 0,7788 + 0,5698 + 0,3679/2] = 0,25[1/2 + 2,2880 + 0,1840] = 0,7430
- Nilai sebenarnya: ≈ 0,7468 (kesalahan ≈ 0,5%)
### Kuadratur Adaptif
Secara otomatis membagi interval ketika fungsinya berubah dengan cepat, menggunakan lebih sedikit titik yang mulus. Inilah yang digunakan`scipy.integrate.quad`(berdasarkan QUADPACK).
---

## Interpolasi
Memperkirakan nilai antara titik data yang diketahui.
### Metode
| Metode | Deskripsi | Kelancaran | Osilasi |
|--------|-------------|------------|-------------|
| **Tetangga terdekat** | Gunakan titik data terdekat | Terputus | Tidak ada |
| **Linier** | Hubungkan titik-titik dengan garis lurus | C⁰ (terus menerus) | Tidak ada |
| **Polinomial (Lagrange)** | Polinomial tunggal melalui semua titik | C^∞ | Parah di banyak titik (fenomena Runge) |
| **Spline kubik** | Sepotong kubik, halus pada sambungan | C² | Minimal |
| **Fungsi basis radial** | Jumlah tertimbang inti radial | Tergantung pada kernel | Rendah |
### Interpolasi Lagrange
Diketahui n+1 titik (x₀, y₀), ..., (xₙ, yₙ), polinomial unik berderajat ≤ n yang melalui semua titik:
P(x) = Σᵢ₌₀ⁿ yᵢ · Πⱼ≠ᵢ (x − xⱼ) / (xᵢ − xⱼ)
**Fenomena Runge:** Interpolasi polinomial derajat tinggi pada titik-titik yang berjarak sama dapat berosilasi secara liar di dekat tepinya. Dimitigasi dengan menggunakan node atau spline Chebyshev.
### Spline Kubik
Polinomial kubik sepotong-sepotong yang kontinu C² (turunan kedua kontinu).
| Ketik | Kondisi Batas |
|------|-------------------|
| Spline alami | S''(x₀) = S''(xₙ) = 0 |
| Spline terjepit | S'(x₀) dan S'(xₙ) ditentukan |
| Bukan simpul | Turunan ketiga kontinu di x₁ dan xₙ₋₁ |
---

## Pemecah ODE
Menyelesaikan persamaan diferensial biasa dy/dt = f(t, y) secara numerik.
### Metode Euler
Pemecah ODE paling sederhana.
**Pembaruan:** y_{n+1} = y_n + h · f(t_n, y_n)
| Properti | Nilai |
|----------|-------|
| Pesan | 1 (kesalahan per langkah: O(h²), global: O(h)) |
| Stabilitas | Stabil bersyarat (diperlukan h kecil) |
| Biaya | 1 evaluasi fungsi per langkah |
### Metode Runge-Kutta
| Metode | Pesan | Tahapan | Catatan |
|--------|-------|--------|-------|
| **Euler** | 1 | 1 | paling sederhana |
| **Titik tengah** | 2 | 2 | Akurasi yang lebih baik |
| **Heun (RK2)** | 2 | 2 | Prediktor-korektor |
| **RK4 Klasik** | 4 | 4 | Pekerja keras standar |
| **Pangeran Dormand (RK45)** | 4(5) | 6 | Ukuran langkah adaptif (digunakan di ode45) |
### Klasik RK4 (Runge-Kutta urutan ke-4)
k₁ = f(t_n, y_n)
k₂ = f(t_n + h/2, y_n + hk₁/2)
k₃ = f(t_n + h/2, y_n + hk₂/2)
k₄ = f(t_n + jam, y_n + hk₃)
y_{n+1} = y_n + h(k₁ + 2k₂ + 2k₃ + k₄) / 6
| Properti | Nilai |
|----------|-------|
| Pesan | 4 (kesalahan global: O(h⁴)) |
| Biaya | 4 evaluasi fungsi per langkah |
| Stabilitas | Jauh lebih baik dari Euler |
| Penggunaan | Default untuk ODE yang tidak kaku |
### ODE yang kaku
ODE **kaku** memiliki komponen yang bervariasi pada skala waktu yang sangat berbeda. Metode eksplisit (Euler, RK4) memerlukan ukuran langkah yang sangat kecil.
| Metode | Ketik | Stabilitas |
|--------|------|-----------|
| Euler implisit | Tersirat | A-stable (stabil tanpa syarat) |
| Rumus Diferensiasi Mundur (BDF) | Tersirat | A-stabil (hingga pesanan 5) |
| Runge-Kutta Tersirat | Tersirat | Varian L-stabil ada |
| LSODA | Otomatis | Beralih antara kaku/tidak kaku |
---

## Stabilitas dan Pengkondisian Numerik
### Nomor Kondisi
**Nomor kondisi** mengukur seberapa besar perubahan keluaran suatu masalah relatif terhadap perubahan kecil pada masukan.
Untuk sistem linier Ax = b: κ(A) = ||A|| · ||A⁻¹||
| κ(A) | Interpretasi |
|-------|---------------|
| ≈ 1 | Berkondisi baik |
| 10³ | Agak sensitif |
| 10⁸ | Kondisi buruk (kehilangan ~8 digit akurasi) |
| → ∞ | Tunggal (tidak ada solusi unik) |
### Stabilitas Algoritma
Suatu algoritma **stabil secara numerik** jika gangguan kecil pada masukan menyebabkan gangguan kecil pada keluaran (relatif terhadap jumlah kondisi masalahnya).
| Algoritma | Stabil? | Catatan |
|-----------|---------|-------|
| Eliminasi Gaussian dengan pivoting parsial | Ya | Pendekatan standar |
| Menghitung nilai eigen melalui QR | Ya | Stabil mundur |
| Penjumlahan naif (besar + kecil dulu) | Tidak | Gunakan penjumlahan Kahan |
| Menghitung varians sebagai E[X²] − (E[X])² | Berpotensi tidak | Gunakan algoritma online Welford |
### Algoritma Daring Welford
Perhitungan mean dan varians berjalan yang stabil secara numerik:
```
mean_new = mean_old + (x − mean_old) / n
M2_new = M2_old + (x − mean_old)(x − mean_new)
variance = M2 / (n − 1)
```

Hal ini untuk menghindari bencana pembatalan yang terjadi pada rumus dua langkah yang naif.
---

## Relevansi dengan Pembelajaran Mesin dan Ilmu Data
| Metode Numerik | Aplikasi |
|-----------------|-------------|
| Titik mengambang (fp16/fp32/bf16) | Pelatihan presisi campuran, kuantisasi model, efisiensi memori |
| Pencarian akar | Estimasi kemungkinan maksimum (menemukan gradien = 0) |
| Integrasi numerik | Inferensi Bayesian (menghitung kemungkinan marjinal), nilai yang diharapkan |
| Interpolasi | Pemulusan, imputasi, model pengganti, fungsi aktivasi |
| Pemecah ODE | ODE Neural, RNN waktu berkelanjutan, dinamika populasi, ML berbasis fisika |
| Nomor kondisi | Memahami Masalah Numerik Pada Regresi Linier Persamaan Normal |
| Penjumlahan stabil | Menghitung fungsi kerugian, statistik normalisasi batch |
| RK4 / pemecah adaptif | Mensimulasikan sistem dinamis, melatih jaringan mendalam berkelanjutan |
---

## Ringkasan
| Topik | Ide Inti | Metode Kunci |
|-------|-----------|------------|
| Titik mengambang | Representasi presisi hingga | IEEE 754, penjumlahan Kahan |
| Pencarian akar | Selesaikan f(x) = 0 | Bagi dua, Newton-Raphson, Brent |
| Integrasi numerik | Perkiraan ∫f(x)dx | Kuadratur Trapesium, Simpson, Gaussian |
| Interpolasi | Perkiraan antar titik data | Spline kubik, Lagrange, RBF |
| Pemecah ODE | Selesaikan dy/dt = f(t,y) | Euler, RK4, metode adaptif |
| Stabilitas | Sensitivitas terhadap kesalahan pembulatan | Nomor kondisi, algoritma stabil |
Metode numerik adalah tempat matematika bertemu dengan kenyataan. Tidak ada komputer yang dapat mewakili sebagian besar bilangan real dengan tepat, tidak ada turunan yang dihitung secara simbolis dalam praktiknya, dan tidak ada integral yang dievaluasi dalam bentuk tertutup untuk permasalahan dunia nyata. Memahami metode numerik memungkinkan Anda memilih algoritme yang tepat, memprediksi keakuratannya, dan menghindari kesalahan halus yang muncul dari aritmatika presisi hingga.