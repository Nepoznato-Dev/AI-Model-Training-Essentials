---
# Metadata
title: "Stochastic Processes"
description: "Random variables review, Markov chains, random walks, Brownian motion, Poisson processes, martingales, Monte Carlo methods, and MCMC"
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
    changes: "Initial deep-dive into stochastic processes"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2027-02-10"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-10"

# Classification
tags: [stochastic-processes, markov-chains, random-walks, brownian-motion, poisson-processes, martingales, monte-carlo, mcmc]
difficulty_level: "advanced"
prerequisites:
  - "statistics_and_probability.md"
  - "real_analysis.md"
estimated_reading_time: "28 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Proses Stokastik
**Proses stokastik** adalah kumpulan variabel acak yang diindeks berdasarkan waktu (atau ruang). Jika teori probabilitas mempelajari peristiwa acak individual, proses stokastik mempelajari bagaimana keacakan berkembang seiring berjalannya waktu. Mereka memodelkan harga saham, panjang antrian, penyebaran penyakit, generasi bahasa, dan dinamika pelatihan model pembelajaran mesin.
---

## Yayasan
### Definisi
Proses stokastik {X_t : t ∈ T} adalah sekumpulan variabel acak yang didefinisikan pada ruang probabilitas umum. T adalah **kumpulan indeks** (waktu):
- **Waktu diskrit:** T = {0, 1, 2, ...}
- **Waktu Berkelanjutan:** T = [0, ∞)
**Ruang status** S adalah himpunan nilai yang mungkin dapat diambil oleh X_t.
### Properti Utama
| Properti | Definisi |
|----------|------------|
| **Stasionaritas** | Distribusi gabungan (X_{t₁}, ..., X_{tₖ}) sama dengan (X_{t₁+τ}, ..., X_{tₖ+τ}) |
| **Kemerdekaan** | X_t tidak bergantung pada X_s untuk t ≠ s |
| **Ergodisitas** | Rata-rata waktu menyatu dengan rata-rata ansambel |
| **Properti Markov** | Masa depan hanya bergantung pada masa kini, bukan masa lalu |
| **Martingale** | Nilai masa depan yang diharapkan sama dengan nilai saat ini |
---

## Rantai Markov
**Rantai Markov** adalah proses stokastik di mana keadaan masa depan hanya bergantung pada keadaan saat ini (properti tanpa memori).
### Rantai Markov Waktu Diskrit (DTMC)
P(X_{n+1} = j | X_n = saya, X_{n-1} = i_{n-1}, ...) = P(X_{n+1} = j | X_n = i) = p_{ij}
**matriks transisi** P memiliki entri p_{ij} = P(buka j | saat ini di i).
| Properti | Pernyataan |
|----------|-----------|
| Jumlah baris | Setiap baris berjumlah 1: Σⱼ p_{ij} = 1 |
| transisi n-langkah | P(X_{n+m} = j | X_m = i) = (Pⁿ)_{ij} |
| Distribusi stasioner | πP = π (vektor eigen kiri dengan nilai eigen 1) |
### Klasifikasi Negara
| Istilah | Definisi |
|------|------------|
| **Berulang** | Rantai kembali ke keadaan i dengan probabilitas 1 |
| **Sementara** | Kemungkinan bukan nol untuk tidak pernah kembali |
| **Menyerap** | p_{ii} = 1 (sekali masuk, tidak pernah keluar) |
| **Periode** | GCD waktu pengembalian; periode 1 = aperiodik |
| **Berkomunikasi** | Negara bagian i dan j dapat saling menghubungi |
### Distribusi Alat Tulis
Untuk rantai Markov berulang positif yang tidak dapat direduksi, distribusi stasioner π ada, unik, dan memenuhi:
πP = π, Σᵢ πᵢ = 1
**Interpretasi:** πᵢ = proporsi waktu jangka panjang yang dihabiskan di negara bagian i.
**Contoh yang Berhasil:** Model cuaca dengan status {Cerah, Hujan}.
P = [[0.9, 0.1], [0.5, 0.5]] (baris: dari Cerah, dari Hujan)
Distribusi stasioner: πP = π
- π₁ = 0,9π₁ + 0,5π₂
- π₂ = 0,1π₁ + 0,5π₂
- π₁ + π₂ = 1
- Penyelesaian: π₁ = 5/6 ≈ 0,833, π₂ = 1/6 ≈ 0,167
### Konvergensi ke Stasioneritas
Untuk rantai berulang positif yang tidak dapat direduksi, aperiodik, dan positif:
- Pⁿ → Π (matriks dengan semua baris sama dengan π) sebagai n → ∞
- **Waktu pencampuran:** Jumlah langkah hingga distribusi mendekati π
- **Kesenjangan spektral:** 1 − |λ₂| (di mana λ₂ adalah nilai eigen terbesar kedua) menentukan kecepatan pencampuran
### Rantai Markov Waktu Berkelanjutan (CTMC)
Transisi terjadi pada waktu acak yang diatur oleh distribusi eksponensial.
| Konsep | Deskripsi |
|---------|-------------|
| **Matriks tarif Q** | q_{ij} ≥ 0 untuk i ≠ j; q_{ii} = −Σ_{j≠i} q_{ij} |
| **Probabilitas transisi** | P(t) = e^{Qt} (matriks eksponensial) |
| **Distribusi alat tulis** | πQ = 0 |
| **Waktu menunggu** | Waktu di negara bagian i adalah Exp(−q_{ii}) |
---

## Jalan Acak
**Jalan acak** adalah jalur yang dibentuk oleh langkah acak yang berurutan.
### Jalan Acak Sederhana
X_n = X_{n-1} + Z_n, dimana Z_n ∈ {+1, −1} dengan probabilitas p, q = 1−p.
| Properti | p = 1/2 (simetris) | p ≠ 1/2 (bias) |
|----------|---------------------|-------------------|
| E[X_n] | 0 | n(2p−1) |
| Var[X_n] | n | 4npq |
| Kembali ke asal? | Ya (dengan probabilitas 1) | Tidak (melayang) |
| Berulang? | Ya (dalam 1D dan 2D) | Tidak |
### Jalan Acak dalam Dimensi Tinggi
| Dimensi | Berulang? | Intuisi |
|-----------|------------|-----------|
| 1D | Ya | "Orang mabuk selalu menemukan jalan pulang" |
| 2D | Ya | "Burung yang mabuk selalu menemukan jalan pulang" |
| 3D+ | Tidak | "Seekor burung pipit yang mabuk tidak pernah menemukan jalan pulang" |
### Koneksi ke Gerak Brown
Menskalakan jalan acak: misalkan S_n = ΣZ_i. Kemudian sebagai ukuran langkah → 0 dan langkah → ∞:
S_{⌊nt⌋} / √n → B(t) (Gerak Brown, menurut teorema Donsker)
---

## Gerak Brown
**Gerak Brown** (Proses Wiener) B(t) adalah batas waktu kontinu dari suatu jalan acak.
### Definisi
B(t) memenuhi:
1.B(0) = 0
2. B(t) memiliki jalur yang berkesinambungan
3. Kenaikan bebas: B(t) − B(s) tidak bergantung pada B(s) − B(r) untuk r < s < t
4. B(t) − B(s) ~ N(0, t − s) (kenaikan Gaussian)
### Properti Utama
| Properti | Pernyataan |
|----------|-----------|
| E[B(t)] | = 0 |
| Var[B(t)] | = t |
| Cov[B(s), B(t)] | = menit(s, t) |
| Tidak ada tempat yang dapat dibedakan | Jalurnya kontinu tetapi tidak mempunyai turunan |
| Dimensi fraktal | Graf mempunyai dimensi Hausdorff 3/2 |
| Properti Markov | Masa depan hanya bergantung pada posisi saat ini |
| Martingal | E[B(t) | F_s] = B(s) untuk s < t |
### Gerak Brown Geometris
S(t) = S(0) exp((μ − σ²/2)t + σB(t))
Ini adalah model standar harga saham dalam kerangka Black-Scholes.
- μ: drift (pengembalian yang diharapkan)
- σ: volatilitas
---

## Proses Poisson
**Proses Poisson** N(t) menghitung jumlah peristiwa yang terjadi di [0, t].
### Definisi
N(t) ~ Poisson(λt), dimana λ adalah laju (kejadian per satuan waktu).
| Properti | Pernyataan |
|----------|-----------|
| N(0) = 0 | — |
| Peningkatan independen | Kejadian-kejadian dalam interval yang saling lepas bersifat bebas |
| Kenaikan stasioner | N(t+s) − N(s) ~ Poisson(λt) |
| E[N(t)] | = λt |
| Var[N(t)] | = λt |
| Waktu antar kedatangan | Terdistribusi secara eksponensial: T_i ~ Exp(λ) |
### Generalisasi
| Varian | Deskripsi |
|---------|-------------|
| **Tidak homogen** | Nilai λ(t) bervariasi terhadap waktu |
| **Senyawa Poisson** | Setiap kejadian mempunyai ukuran acak: S(t) = Σᵢ₌₁^{N(t)} Yᵢ |
| **Ukuran acak racun** | Titik dalam ruang-waktu, bukan hanya waktu |
| **Multivarian** | Berbagai jenis peristiwa dengan kemungkinan interaksi |
---

## Martingale
**martingale** adalah permainan yang adil: nilai yang diharapkan di masa depan, berdasarkan semua informasi terkini, sama dengan nilai saat ini.
### Definisi
{X_n} adalah martingale sehubungan dengan filtrasi {F_n} jika:
1. X_n dapat diukur dengan F_n (diadaptasi)
2. E[|X_n|] < ∞ (terintegrasi)
3. E[X_{n+1} | F_n] = X_n (permainan adil)
| Varian | Kondisi | Interpretasi |
|---------|-----------|----------------|
| **Martingale** | E[X_{n+1} | F_n] = X_n | Permainan yang adil |
| **Submartingale** | E[X_{n+1} | F_n] ≥ X_n | Permainan yang disukai (tren naik) |
| **Supermartingale** | E[X_{n+1} | F_n] ≤ X_n | Permainan kurang menguntungkan (tren turun) |
### Teorema Kunci
| Teorema | Pernyataan |
|---------|-----------|
| **Penghentian opsional** | Dalam kondisi, E[X_T] = E[X_0] untuk waktu berhenti T |
| **Konvergensi** | Martingale yang dibatasi hampir pasti bertemu |
| **Ketimpangan maksimal** | P(max_{k≤n} X_k ≥ λ) ≤ E[X_n] / λ (Doob) |
---

## Metode Monte Carlo
**Metode Monte Carlo** menggunakan pengambilan sampel acak untuk memperkirakan besaran deterministik.
### Ide Dasar
Untuk memperkirakan E[f(X)] di mana X ~ P:
1. Gambarlah N sampel: x₁, x₂, ..., x_N dari P
2. Hitung: Î = (1/N) Σᵢ f(xᵢ)
3. Berdasarkan hukum bilangan besar: Î → E[f(X)] sebagai N → ∞
**Kesalahan:** Kesalahan standar = σ_f / √N, dengan σ_f² = Var[f(X)]
### Teknik Pengurangan Varians
| Teknik | Ide | Mempercepat |
|-----------|------|---------|
| **Contoh pentingnya** | Sampel dari Q bukannya P, bobotnya sebesar P/Q | Bisa dramatis |
| **Variasi antitesis** | Gunakan pasangan (x, −x) untuk membatalkan varians | ~2x |
| **Kontrol bervariasi** | Kurangi fungsi ekspektasi yang diketahui yang berkorelasi dengan f | Bervariasi |
| **Pengambilan sampel bertingkat** | Bagilah domain, ambil sampel setiap strata | Mengurangi varians |
| **Rao-Blackwell** | Kondisi pada statistik yang memadai | Selalu membantu |
---

## Rantai Markov Monte Carlo (MCMC)
MCMC membangun rantai Markov yang distribusi stasionernya merupakan distribusi target. Setelah periode "burn-in", sampel diambil dari target.
### Algoritma Metropolis-Hastings
| Langkah | Aksi |
|------|--------|
| 1 | Keadaan saat ini: x_t |
| 2 | Usulkan: x* ~ q(x* \| x_t) (distribusi proposal) |
| 3 | Rasio penerimaan: α = min(1, [π(x*)q(x_t\|x*)] / [π(x_t)q(x*\|x_t)]) |
| 4 | Terima dengan probabilitas α: x_{t+1} = x* (menerima) atau x_t (menolak) |
**Kasus khusus — Algoritma Metropolis:** Proposal simetris q(x*|x) = q(x|x*), jadi α = min(1, π(x*)/π(x_t)).
### Pengambilan Sampel Gibbs
Kasus khusus Metropolis-Hastings di mana setiap variabel diperbarui dari distribusi kondisional penuhnya.
Untuk target π(x₁, x₂, ..., xₖ):
1. Contoh x₁^{(t+1)} ~ π(x₁ | x₂^{(t)}, ..., xₖ^{(t)})
2. Contoh x₂^{(t+1)} ~ π(x₂ | x₁^{(t+1)}, x₃^{(t)}, ..., xₖ^{(t)})
3. Lanjutkan untuk semua variabel
4. Ulangi
| Properti | Pernyataan |
|----------|-----------|
| Selalu menerima | α = 1 (tidak ada langkah penolakan) |
| Membutuhkan | Kemampuan untuk mengambil sampel dari setiap kondisi penuh |
| Konvergensi | Dijamin untuk rantai aperiodik yang tidak dapat direduksi |
### Diagnostik MCMC
| Diagnostik | Tujuan |
|-----------|---------|
| **Pelacakan plot** | Pemeriksaan visual untuk pencampuran dan stasioneritas |
| **Autokorelasi** | Mengukur ketergantungan sampel (menginginkan autokorelasi rendah) |
| **Gelman-Rubin (Kanan)** | Bandingkan beberapa rantai; R̂ < 1,05 menunjukkan konvergensi |
| **Ukuran sampel efektif** | N_eff = N / (1 + 2Σρₖ); memperhitungkan autokorelasi |
| **Pembakaran** | Buang sampel awal sebelum rantai mencapai stasioneritas |
---

## Relevansi dengan Pembelajaran Mesin dan Ilmu Data
| Proses Stokastik | Aplikasi |
|-------------------|-------------|
| Rantai Markov | PageRank (berjalan acak di grafik web), pembuatan teks (model n-gram), MCMC |
| Jalan acak | Node2Vec dan DeepWalk (penyematan grafik), eksplorasi di RL |
| Gerak Brown | Pemodelan harga saham, model difusi dalam AI generatif |
| Proses Poisson | Pemodelan kejadian kedatangan (klik, kegagalan), teori antrian |
| Martingale | Matematika keuangan, membuktikan konvergensi SGD (pendekatan stokastik) |
| Monte Carlo | Memperkirakan nilai yang diharapkan, inferensi Bayesian, pembelajaran penguatan (evaluasi kebijakan) |
| MCMC (Metropolis-Hastings) | Pengambilan sampel posterior Bayesian, pemrograman probabilistik (Stan, PyMC) |
| Pengambilan sampel Gibbs | Model topik (LDA), jaringan Bayesian, penolakan gambar |
| Diagnostik MCMC | Memastikan inferensi yang andal dari model probabilistik |
---

## Ringkasan
| Proses | Ruang Negara | Waktu | Properti Utama |
|---------|-------------|------|--------------|
| Rantai Markov | Diskrit/kontinu | Diskrit/kontinu | Tanpa memori (properti Markov) |
| Jalan acak | ℤᵈ | Diskrit | Jumlah i.i.d. langkah |
| Gerak Brown | ℝ | Terus menerus | Peningkatan Gaussian, jalur berkelanjutan |
| Proses Poisson | ℕ | Terus menerus | Proses penghitungan dengan kesenjangan eksponensial |
| Martingal | ℝ | Diskrit/kontinu | Permainan yang adil (E[X_{t+1}|F_t] = X_t) |
Proses stokastik adalah matematika keacakan sepanjang waktu. Mereka mendasari inferensi Bayesian modern (MCMC), pembelajaran penguatan (proses pengambilan keputusan Markov), pemodelan generatif (model difusi), matematika keuangan, dan teori antrian. Memahami proses-proses ini memberi Anda alat untuk memodelkan ketidakpastian secara dinamis — tidak hanya sebagai gambaran singkat, namun seiring perkembangannya.