---
# Metadata
title: "Optimization"
description: "Linear programming, convex optimization, gradient descent variants, Lagrange multipliers, KKT conditions, duality, integer programming, and heuristic methods"
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
    changes: "Initial deep-dive into optimization"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2027-02-10"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-10"

# Classification
tags: [optimization, linear-programming, convex-optimization, gradient-descent, lagrange-multipliers, kkt, duality, integer-programming]
difficulty_level: "intermediate"
prerequisites:
  - "mathematics.md"
  - "real_analysis.md"
estimated_reading_time: "30 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# Optimasi
Optimasi adalah ilmu matematika untuk menemukan solusi terbaik dari serangkaian solusi yang layak. Pertanyaannya: dengan adanya fungsi dan batasan, masukan apa yang meminimalkan (atau memaksimalkan) keluaran? Pengoptimalan adalah mesin pembelajaran mesin — melatih model berarti meminimalkan fungsi kerugian. Ini muncul dalam riset operasi, ekonomi, desain teknik, dan hampir semua bidang kuantitatif.
---

## Rumusan Masalah
**Masalah pengoptimalan** umum berbentuk:
Minimalkan f(x)
Tunduk pada: gᵢ(x) ≤ 0 (batasan ketimpangan), hⱼ(x) = 0 (batasan persamaan)
| Istilah | Arti |
|------|---------|
| **Fungsi tujuan** f(x) | Kuantitas yang harus diminimalkan (atau dimaksimalkan) |
| **Variabel keputusan** x | Nilai yang dapat kita kendalikan |
| **Wilayah yang layak** | Himpunan semua x yang memenuhi semua batasan |
| **Minimum global** | Layak x* dengan f(x*) ≤ f(x) untuk semua x | yang layak
| **Minimum lokal** | X* yang layak dengan f(x*) ≤ f(x) untuk semua x yang layak di beberapa lingkungan |
| **Masalah cembung** | f cembung, daerah layak himpunan cembung (min lokal = min global) |
---

## Pemrograman Linier (LP)
Jika tujuan dan semua batasannya **linier**, maka masalahnya adalah program linier.
### Formulir Standar
Minimalkan cᵀx
Tunduk pada: Ax ≤ b, x ≥ 0
dimana c, x ∈ ℝⁿ, A ∈ ℝᵐˣⁿ, b ∈ ℝᵐ.
### Properti
| Properti | Pernyataan |
|----------|-----------|
| Konveksitas | LP selalu merupakan soal cembung |
| Solusi optimal | Selalu berada pada titik sudut (titik sudut) dari politop yang layak |
| Keberadaan | Jika daerah layak dibatasi dan tidak kosong, maka ada solusi optimal |
| Beberapa optimal | Jika dua simpul optimal, setiap titik pada sisi di antara keduanya juga optimal |
### Metode Simpleks
**Metode sederhana** (Dantzig, 1947) bergerak di sepanjang tepi politop yang layak dari titik ke titik, selalu meningkatkan tujuan, hingga mencapai titik optimal.
| Properti | Nilai |
|----------|-------|
| Waktu terburuk | O(2ⁿ) (eksponensial — jarang dalam praktiknya) |
| Waktu kasus rata-rata | Polinomial untuk sebagian besar masalah praktis |
| Ide kunci | Pindah ke titik bertetangga yang mempunyai nilai obyektif lebih baik |
**Algoritma (ikhtisar):**
1. Mulai dari solusi dasar yang layak (puncak politope)
2. Pilih variabel masuk (variabel yang meningkatkan tujuan)
3. Pilih variabel keluar (pertahankan kelayakan)
4. Pivot: pindah ke titik baru
5. Ulangi sampai tidak ada arah perbaikan
### Metode Titik Interior
Alternatif terhadap simpleks: pendekatan optimal dari dalam wilayah yang layak.
| Properti | Nilai |
|----------|-------|
| Waktu terburuk | Polinomial (O(n³·⁵) untuk beberapa varian) |
| Kinerja praktis | Kompetitif dengan simpleks pada permasalahan besar |
| Ide kunci | Ikuti "jalur pusat" melalui interior |
### Contoh LP yang berhasil
**Masalah:** Sebuah pabrik memproduksi kursi (x₁) dan meja (x₂).
- Keuntungan: $30 per kursi, $50 per meja
- Kayu: 2x₁ + 4x₂ ≤ 100 (kaki papan tersedia)
- Tenaga Kerja: x₁ + 3x₂ ≤ 60 (jam tersedia)
- Maksimalkan: 30x₁ + 50x₂
**Solusi (metode grafis untuk 2 variabel):**
- Titik daerah layak: (0,0), (30,0), (40,10), (0,20)
- Evaluasi tujuan di setiap titik:
  - (0,0): keuntungan = 0
  - (30,0) : keuntungan = 900
  - (40,10) : keuntungan = 1700 ← optimal
  - (0,20) : keuntungan = 1000
- **Optimal:** x₁ = 40 kursi, x₂ = 10 meja, keuntungan = $1700
---

## Optimasi Cembung
Suatu permasalahan bersifat **cembung** jika fungsi tujuannya cembung dan daerah layaknya adalah himpunan cembung.
### Himpunan dan Fungsi Cembung
| Konsep | Definisi |
|---------|------------|
| **Set cembung** | Untuk setiap x, y di himpunan dan t ∈ [0,1]: tx + (1−t)y juga ada di himpunan |
| **Fungsi cembung** | f(tx + (1−t)y) ≤ tf(x) + (1−t)f(y) untuk semua t ∈ [0,1] |
| **Sangat cembung** | Ketimpangan sangat ketat untuk t ∈ (0,1) dan x ≠ y |
**Properti utama:** Untuk pengoptimalan konveks, setiap minimum lokal adalah minimum global.
### Fungsi Cembung Umum
| Fungsi | Cembung? | Dimana |
|----------|---------|-------|
| kapak + b (linier) | Ya (dan cekung) | Dimana-mana |
| x² | Ya | ℝ |
| eˣ | Ya | ℝ |
| −log(x) | Ya | x > 0 |
| \|x\|ᵖ (p ≥ 1) | Ya | ℝⁿ |
| max(f₁, f₂) jika f₁, f₂ cembung | Ya | Persimpangan domain |
### Penurunan Gradien
Algoritme pengoptimalan paling mendasar dalam pembelajaran mesin.
**Aturan pembaruan:** x_{k+1} = x_k − α∇f(x_k)
dengan α > 0 adalah **kecepatan pemelajaran** (ukuran langkah).
| Varian | Perbarui Aturan | Keuntungan |
|---------|-------------|-----------|
| **Kelompok GD** | x ← x − α∇f(x) | Konvergensi stabil |
| **Stochastic GD (SGD)** | x ← x − α∇fᵢ(x) (satu sampel) | Per iterasi yang cepat, lolos dari minimum lokal |
| **SGD batch mini** | x ← x − α(1/|B|)Σᵢ∈B ∇fᵢ(x) | Keseimbangan antara batch dan stokastik |
| **Momentumnya** | v ← βv − α∇f(x); x ← x + v | Berakselerasi melalui daerah datar |
| **Adam** | Kecepatan pembelajaran adaptif per parameter | Berfungsi dengan baik untuk pembelajaran mendalam |
| **RMSprop** | Menskalakan kecepatan pembelajaran dengan menjalankan rata-rata besaran gradien | Bagus untuk RNN ​​|
### Tingkat Konvergensi
| Metode | Cembung f | Sangat Cembung f |
|--------|----------|-------------------|
| Penurunan gradien | HAI(1/k) | O((1−μ/L)ᵏ) (linier) |
| SGD | HAI(1/√k) | HAI(1/k) |
| GD yang Dipercepat (Nesterov) | HAI(1/k²) | HAI((1−√(μ/L))ᵏ) |
dimana k = jumlah iterasi, μ = parameter konveksitas kuat, L = Konstanta Lipschitz.
### Memilih Kecepatan Pembelajaran
| Strategi | Deskripsi |
|----------|-------------|
| Memperbaiki | Sederhana namun mungkin menyimpang (terlalu besar) atau menyatu secara perlahan (terlalu kecil) |
| Pencarian garis | Temukan α yang meminimalkan f(x − α∇f(x)) sepanjang arah gradien |
| Jadwal peluruhan | α_t = α₀ / (1 + βt) atau α_t = α₀ · βᵗ |
| Pemanasan | Mulai dari yang kecil, tingkatkan, lalu pembusukan (umum dalam pelatihan transformator) |
| Adaptif (Adam) | Kecepatan pembelajaran per parameter berdasarkan statistik gradien |
---

## Optimasi Terbatas
### Pengganda Lagrange
Untuk soal: minimalkan f(x) dengan syarat h(x) = 0.
**Lagrangian:** L(x, λ) = f(x) + λh(x)
Pada kondisi optimum: ∇ₓL = 0 dan ∇_λL = 0 (menghasilkan h(x) = 0).
**Contoh yang Dikerjakan:** Minimalkan f(x,y) = x² + y² dengan syarat x + y = 1.
- L = x² + y² + λ(x + y − 1)
- ∂L/∂x = 2x + λ = 0 → x = −λ/2
- ∂L/∂y = 2y + λ = 0 → y = −λ/2
- Batasan: x + y = 1 → −λ = 1 → λ = −1
- Penyelesaian: x = 1/2, y = 1/2, f = 1/2
### Ketentuan KKT
**Kondisi Karush-Kuhn-Tucker (KKT)** menggeneralisasi pengganda Lagrange ke batasan ketimpangan.
Untuk: minimalkan f(x) jika gᵢ(x) ≤ 0, hⱼ(x) = 0.
**Lagrangian:** L(x, λ, ν) = f(x) + Σᵢ λᵢgᵢ(x) + Σⱼ νⱼhⱼ(x)
**Kondisi KKT** (diperlukan untuk optimalitas):
| Kondisi | Persamaan |
|-----------|----------|
| stasioneritas | ∇ₓL = 0 |
| Kelayakan utama | gᵢ(x) ≤ 0, hⱼ(x) = 0 |
| Kelayakan ganda | λᵢ ≥ 0 |
| Kelambanan yang saling melengkapi | λᵢgᵢ(x) = 0 untuk semua i |
**Kelonggaran komplementer** artinya: jika batasan gᵢ tidak aktif (gᵢ(x) < 0), maka λᵢ = 0 (batasan tidak memengaruhi solusi).
Untuk soal cembung yang memenuhi syarat Slater, syarat KKT perlu dan cukup.
---

## Dualitas
Setiap masalah pengoptimalan (**primal**) memiliki masalah **dual** yang terkait.
### Dualitas Lemah dan Kuat
| Konsep | Pernyataan |
|---------|-----------|
| **Fungsi ganda** | g(λ, ν) = infₓ L(x, λ, ν) |
| **Masalah ganda** | Maksimalkan g(λ, ν) sesuai dengan λ ≥ 0 |
| **Dualitas lemah** | Optimal ganda ≤ Primal optimal (selalu bertahan) |
| **Dualitas yang kuat** | Dual optimal = Primal optimal (berlaku untuk soal cembung dengan kondisi Slater) |
| **Kesenjangan dualitas** | Primal optimal - Dual optimal (nol di bawah dualitas kuat) |
### Mengapa Dualitas Penting
| Aplikasi | Bagaimana Dualitas Membantu |
|-------------|-------------------|
| Batas bawah | Dual memberikan sertifikat seberapa bagus solusi primal |
| SVM | Masalah ganda SVM mengarah ke trik kernel |
| Analisis sensitivitas | Variabel ganda mengukur seberapa besar perubahan optimal jika batasan dilonggarkan |
| Dekomposisi | Permasalahan yang besar dapat dipecah menjadi submasalah yang lebih kecil melalui dual |
---

## Pemrograman Integer
Ketika beberapa atau semua variabel harus berupa **integer**, masalahnya menjadi jauh lebih sulit (NP-hard secara umum).
### Jenis
| Ketik | Deskripsi |
|------|-------------|
| IP Murni | Semua variabel harus berupa bilangan bulat |
| IP Campuran (MIP) | Beberapa variabel bilangan bulat, beberapa kontinu |
| IP Biner | Variabel dibatasi hingga {0, 1} |
### Metode Solusi
| Metode | Ide |
|--------|------|
| **Cabang dan terikat** | Bagi menjadi submasalah, selesaikan relaksasi LP, pangkas |
| **Memotong pesawat** | Tambahkan batasan linier untuk memperketat relaksasi LP |
| **Cabang dan potong** | Gabungkan cabang-dan-terikat dengan bidang potong |
| **Heuristik** | Serakah, pencarian lokal, simulasi anil untuk solusi perkiraan |
---

## Metode Heuristik dan Metaheuristik
Ketika optimasi yang tepat sulit dilakukan, heuristik menemukan solusi yang baik (belum tentu optimal).
| Metode | Ide Kunci | Terbaik Untuk |
|--------|----------|----------|
| **Penurunan gradien** | Ikuti turunan paling curam | Fungsi halus dan terdiferensiasi |
| **Metode Newton** | Gunakan informasi orde kedua (kelengkungan) | Soal Mulus dan Berkondisi Baik |
| **Simulasi anil** | Terima solusi yang lebih buruk dengan probabilitas yang menurun | Pengoptimalan global, kombinatorial |
| **Algoritma genetika** | Evolusi suatu populasi menggunakan seleksi, persilangan, mutasi | Multi-tujuan, tidak dapat dibedakan |
| **Kawanan partikel** | Agen menjelajahi luar angkasa, dipengaruhi oleh posisi paling terkenal | Kontinu, tidak cembung |
| **Pengoptimalan Bayesian** | Bangun model pengganti, gunakan fungsi akuisisi | Fungsi kotak hitam yang mahal (penyetelan hyperparameter) |
### Metode Optimasi Newton
**Aturan pembaruan:** x_{k+1} = x_k − [H(x_k)]⁻¹ ∇f(x_k)
dimana H adalah matriks Hessian (matriks turunan kedua).
| Properti | Nilai |
|----------|-------|
| Tingkat konvergensi | Kuadrat (mendekati optimal) |
| Biaya per iterasi | O(n³) untuk inversi Hessian |
| Membutuhkan | Hessian | yang terdiferensiasi dua kali dan pasti positif
| Kuasi-Newton (BFGS) | Perkiraan Goni dari gradien | O(n²) per iterasi |
---

## Relevansi dengan Pembelajaran Mesin dan Ilmu Data
| Konsep Optimasi | Aplikasi |
|------|-------------|
| Penurunan gradien | Pelatihan jaringan saraf, regresi logistik, model terdiferensiasi apa pun |
| SGD dan variannya | ML skala besar (pelatihan mini-batch), pembelajaran online |
| Adam, RMSprop | Pengoptimal default untuk pembelajaran mendalam |
| Optimasi cembung | SVM, regresi logistik, LASSO, Ridge (dijamin optimal global) |
| Pengganda Lagrange | Pembelajaran terbatas, ML yang adil, alokasi sumber daya |
| Syarat KKT | Menurunkan SVM ganda, memahami aktivitas kendala |
| Dualitas | Trik kernel SVM, analisis sensitivitas, metode dekomposisi |
| Pemrograman linier | Alokasi sumber daya, optimalisasi portofolio, aliran jaringan |
| Pemrograman bilangan bulat | Seleksi fitur (biner), penjadwalan, masalah kombinatorial |
| Optimasi Bayesian | Penyetelan hyperparameter (Optuna, Hyperopt) |
| Newton/kuasi-Newton | Metode orde kedua untuk masalah kecil-menengah (L-BFGS) |
---

## Ringkasan
| Metode | Jenis Masalah | Jaminan | Skala |
|--------|-------------|------------|-------|
| Simpleks | Pemrograman linier | Optimal tepat | Jutaan variabel |
| Titik interior | Cembung (LP, QP, SOCP) | Optimal tepat | Skala besar |
| Penurunan gradien | Halus tanpa kendala | Menyatu ke min lokal | Sangat besar (pembelajaran mendalam) |
| SGD | Risiko empiris skala besar | Menyatu (dengan peluruhan) | Kumpulan data besar-besaran |
| Newton / BFGS | Halus, dapat dibedakan dua kali | Konvergensi kuadrat | Kecil-menengah |
| KKT / Lagrange | Terkendala (cembung) | Tepat dalam kondisi | Sedang |
| Cabang dan terikat | Pemrograman bilangan bulat | Optimal tepat | Kecil-menengah |
| Heuristik | Apa saja (non-cembung, kombinatorial) | Tidak ada jaminan | Bervariasi |
Pengoptimalan bisa dibilang merupakan alat matematika paling penting dalam pembelajaran mesin. Setiap model yang Anda latih — mulai dari regresi linier hingga model bahasa besar — ​​​​melibatkan penyelesaian masalah pengoptimalan. Memahami kapan suatu masalah bersifat cembung (dijamin optimal secara global), kapan penurunan gradien akan menyatu, dan cara menangani batasan memberi Anda landasan teoretis untuk merancang, men-debug, dan meningkatkan algoritme pembelajaran.