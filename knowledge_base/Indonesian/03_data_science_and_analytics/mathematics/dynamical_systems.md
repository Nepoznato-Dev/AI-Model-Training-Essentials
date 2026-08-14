---
# Metadata
title: "Dynamical Systems"
description: "Ordinary and partial differential equations, phase portraits, equilibrium and stability, Lyapunov functions, chaos theory, Lorenz attractor, bifurcation diagrams, and PDEs"
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
    changes: "Initial deep-dive into dynamical systems"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2027-02-10"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-10"

# Classification
tags: [dynamical-systems, ode, pde, phase-portraits, stability, chaos, lorenz-attractor, bifurcation, lyapunov]
difficulty_level: "advanced"
prerequisites:
  - "mathematics.md"
  - "real_analysis.md"
  - "numerical_methods.md"
estimated_reading_time: "28 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# Sistem Dinamis
**sistem dinamis** menggambarkan bagaimana suatu negara berkembang dari waktu ke waktu berdasarkan aturan yang tetap. Dari orbit planet hingga dinamika populasi, dari pola cuaca hingga pelatihan jaringan saraf, teori sistem dinamik menyediakan bahasa dan alat untuk memahami bagaimana segala sesuatunya berubah. File ini mencakup persamaan diferensial biasa (ODE), persamaan diferensial parsial (PDE), analisis stabilitas, chaos, dan bifurkasi.
---

## Persamaan Diferensial Biasa (ODE)
Sebuah ODE menghubungkan suatu fungsi dengan turunannya terhadap satu variabel independen (biasanya waktu).
### Klasifikasi
| Properti | Jenis |
|----------|-------|
| **Pesan** | Hadiah turunan tertinggi (orde 1, orde 2, dst) |
| **Linier vs Nonlinier** | Linier: y'' + p(t)y' + q(t)y = g(t); Nonlinier: apa pun |
| **homogen** | g(t) = 0 (tidak ada istilah paksaan) |
| **Otonomi** | Tidak ada ketergantungan waktu yang eksplisit: dy/dt = f(y) |
| **Koefisien konstan** | p, q adalah konstanta |
### ODE Orde Pertama
**Bentuk umum:** dy/dt = f(t, y)
| Ketik | Formulir | Metode Solusi |
|------|------|-----------------|
| Dapat dipisahkan | dy/dt = g(t)h(y) | Pisahkan dan integrasikan: ∫dy/h(y) = ∫g(t)dt |
| Linier orde pertama | dy/dt + p(t)y = q(t) | Faktor pengintegrasian: μ(t) = e^(∫p dt) |
| Tepat | M(t,y)dt + N(t,y)dy = 0 dengan ∂M/∂y = ∂N/∂t | Temukan fungsi potensial F(t,y) |
| Bernoulli | dy/dt + p(t)y = q(t)yⁿ | Substitusikan v = y^(1−n) untuk linierisasi |
**Contoh Pekerjaan (Faktor Integrasi):** Selesaikan dy/dt + 2y = e^(−t), y(0) = 1.
- Faktor pengintegrasian: μ(t) = e^(∫2 dt) = e^(2t)
- Kalikan: d/dt[e^(2t)y] = e^(2t) · e^(−t) = e^t
- Integrasikan: e^(2t)y = e^t + C
- y(t) = e^(−t) + Ce^(−2t)
- Kondisi awal: y(0) = 1 → 1 = 1 + C → C = 0
- Solusi: y(t) = e^(−t)
### ODE Linier Orde Kedua
**Bentuk umum:** ay'' + by' + cy = g(t)
**Kasus homogen** (g ​​= 0): Selesaikan persamaan karakteristik ar² + br + c = 0.
| Diskriminan | Akar | Solusi Umum |
|-------------|-------|------------------|
| b² > 4ac (teredam berlebihan) | Dua r₁ nyata yang berbeda, r₂ | y = C₁e^(r₁t) + C₂e^(r₂t) |
| b² = 4ac (teredam kritis) | Akar asli berulang r | y = (C₁ + C₂t)e^(rt) |
| b² < 4ac (kurang teredam) | Akar kompleks α ± βi | y = e^(αt)(C₁ cos βt + C₂ sin βt) |
**Interpretasi fisis:** Sistem peredam pegas massa mx'' + bx' + kx = 0.
- Overdamped: redaman berat, tidak ada osilasi (penutup pintu)
- Redaman kritis: pengembalian tercepat tanpa osilasi (target desain suspensi mobil)
- Underdamped: berosilasi dengan amplitudo yang menurun (senar gitar)
### Sistem ODE
Banyak sistem nyata melibatkan banyak variabel yang saling berinteraksi:
dx/dt = f(x, y)
dy/dt = g(x, y)
Ini dapat ditulis dalam bentuk vektor: d**x**/dt = **F**(**x**)
**Sistem linier:** d**x**/dt = A**x**, dengan A adalah matriks.
Solusi bergantung pada nilai eigen A:
| Nilai eigen | Perilaku |
|-------------|-----------|
| Keduanya nyata, negatif | Node stabil (semua lintasan menyatu ke titik asal) |
| Keduanya nyata, positif | Node tidak stabil |
| Nyata, tanda berlawanan | Titik pelana (tidak stabil) |
| Bagian real negatif yang kompleks | Spiral stabil (osilasi teredam) |
| Bagian nyata yang kompleks dan positif | Spiral tidak stabil |
| Imajinasi murni | Pusat (orbit tertutup) |
---

## Potret Fase
**Potret fase** memvisualisasikan lintasan sistem dinamis dalam ruang keadaan (tanpa penyelesaian secara eksplisit).
### Fitur Utama
| Fitur | Deskripsi |
|---------|-------------|
| **Titik tetap (kesetimbangan)** | Dimana dx/dt = 0 (tidak ada gerak) |
| **Lintasan** | Jalur yang ditelusuri oleh sistem dalam ruang keadaan |
| **Nullcline** | Kurva yang turunan salah satu komponennya adalah nol |
| **Batasi siklus** | Orbit tertutup terisolasi (osilasi mandiri) |
| **Cekungan daya tarik** | Himpunan kondisi awal yang mengarah ke penarik tertentu |
| **Pemisah** | Batas antar cekungan daya tarik yang berbeda |
### Model Predator-Mangsa (Lotka-Volterra)
dx/dt = αx − βxy (mangsa)
dy/dt = δxy − γy (pemangsa)
**Poin tetap:**
1. (0, 0) — kepunahan (titik pelana)
2. (γ/δ, α/β) — hidup berdampingan (pusat — orbit tertutup)
Sistem ini menunjukkan osilasi periodik: mangsa bertambah → predator bertambah → mangsa berkurang → predator berkurang → siklus berulang.
---

## Analisis Stabilitas
### Stabilitas Linier
Untuk titik tetap x*, linierkan sekelilingnya: misalkan u = x − x*, maka du/dt ≈ J(x*)u dengan J adalah matriks Jacobian.
**Kriteria stabilitas:** Titik tetapnya adalah:
- **Stabil** jika semua nilai eigen J memiliki bagian real negatif
- **Tidak stabil** jika ada nilai eigen yang memiliki bagian real positif
- **Sedikit stabil** jika nilai eigen memiliki bagian real nol (membutuhkan analisis nonlinier)
### Stabilitas Lyapunov
**Metode langsung Lyapunov** menentukan stabilitas tanpa linearisasi.
A **Fungsi Lyapunov** V(x) memenuhi:
1. V(x*) = 0 dan V(x) > 0 untuk x ≠ x* (pasti positif)
2. dV/dt ≤ 0 sepanjang lintasan (tidak meningkat)
| Kondisi | Kesimpulan |
|-----------|------------|
| dV/dt< 0 (negative definite) | Asymptotically stable |
| dV/dt ≤ 0 (negative semi-definite) | Stable (but may not converge) |
| dV/dt >0 | Tidak stabil |
**Contoh Pengerjaan:** Sistem dx/dt = −x + y², dy/dt = −y.
- Coba V(x,y) = x² + y² (fungsi mirip energi)
- dV/dt = 2x(−x + y²) + 2y(−y) = −2x² + 2xy² − 2y²
- Dekat titik asal: dV/dt ≈ −2x² − 2y² < 0 (untuk y kecil, −2y² mendominasi)
- Kesimpulan: asal stabil secara asimtotik lokal
---

## Teori Kekacauan
**Kekacauan** bersifat deterministik namun tidak dapat diprediksi: sistem mengikuti aturan yang pasti, namun perbedaan kecil dalam kondisi awal akan menghasilkan hasil yang sangat berbeda.
### Persyaratan untuk Kekacauan
| Properti | Deskripsi |
|----------|-------------|
| deterministik | Tidak ada keacakan — diatur oleh persamaan eksak |
| Peka terhadap kondisi awal | Lintasan terdekat berbeda secara eksponensial |
| Dibatasi | Lintasan tidak lepas hingga tak terhingga |
| Non-periodik | Tidak pernah mengulangi dengan tepat |
### Sistem Lorenz
Contoh klasik dari kekacauan deterministik:
dx/dt = σ(y − x)
dy/dt = x(ρ − z) − y
dz/dt = xy − βz
Dengan parameter standar σ = 10, ρ = 28, β = 8/3:
- Sistem mempunyai tiga titik tetap, semuanya tidak stabil
- Lintasan mengorbit satu titik tetap, lalu tiba-tiba beralih ke titik lainnya
- Hasilnya adalah **penarik Lorenz** — penarik aneh dengan struktur fraktal
**Eksponen Lyapunov:** Mengukur laju divergensi lintasan terdekat.
- Eksponen Lyapunov positif → kekacauan
- Untuk sistem Lorenz dengan parameter standar: eksponen terbesar ≈ 0,9 > 0
### Peta Logistik
Sistem diskrit sederhana yang menunjukkan kekacauan:
x_{n+1} = rx_n(1 − x_n)
| Parameter r | Perilaku |
|-------------|-----------|
| 0 < r < 1 | Populasi punah (x → 0) |
| 1 < r < 3 | Titik tetap stabil di x = 1 − 1/r |
| 3 < r < 3,449 | Osilasi periode-2 |
| 3,449 < r < 3,544 | Osilasi periode-4 |
| 3,544 < r < 3,570 | Periode-8, 16, 32, ... (riam penggandaan periode) |
| r ≈ 3,570 | Permulaan kekacauan |
| 3,570 < r < 4 | Sebagian besar kacau, dengan jendela berkala |
| r = 4 | Sepenuhnya kacau pada [0, 1] |
### Efek Kupu-Kupu
Nama populer untuk ketergantungan sensitif pada kondisi awal. Dalam sistem cuaca (yang dimodelkan dengan persamaan Lorenz), seekor kupu-kupu yang mengepakkan sayapnya di Brasil dapat memicu terjadinya tornado di Texas – bukan karena kupu-kupu yang menyebabkannya, namun karena gangguan kecil yang tumbuh secara eksponensial.
---

## Teori Bifurkasi
**Bifurkasi** adalah perubahan kualitatif dalam perilaku sistem sebagai parameter yang bervariasi.
### Jenis Bifurkasi
| Bifurkasi | Bentuk Biasa | Apa yang Terjadi |
|-------------|-------------|--------------|
| **Simpul pelana** | dx/dt = r − x² | Dua titik tetap muncul/menghilang |
| **Transkritis** | dx/dt = rx − x² | Stabilitas pertukaran dua titik tetap |
| **Pitchfork (superkritis)** | dx/dt = rx − x³ | Satu titik stabil terbagi menjadi dua titik stabil + satu titik tidak stabil |
| **Pitchfork (subkritis)** | dx/dt = rx + x³ | Cabang-cabang yang tidak stabil runtuh (seringkali menimbulkan bencana) |
| **Hopf** | sistem 2D | Titik tetap menjadi tidak stabil, muncul siklus batas |
### Diagram Bifurkasi
Plot titik tetap vs nilai parameter, menunjukkan stabilitas (padat = stabil, putus-putus = tidak stabil). Diagram bifurkasi peta logistik mengungkapkan rute penggandaan periode menuju kekacauan dan **konstanta Feigenbaum** yang terkenal δ ≈ 4,669 (rasio universal antara interval bifurkasi yang berurutan).
---

## Persamaan Diferensial Parsial (PDE)
PDE melibatkan fungsi banyak variabel dan turunan parsialnya.
### Klasifikasi PDE Linier Orde Kedua
Untuk Au_xx + 2Bu_xy + Cu_yy + ... = 0:
| Ketik | Kondisi | Perilaku | Contoh |
|------|-----------|-----------|---------|
| **Eliptik** | B²− AC< 0 | Steady-state, no time dependence | Laplace's equation: ∇²u = 0 |
| **Parabolic** | B² − AC = 0 | Diffusion, smoothing over time | Heat equation: u_t = αu_xx |
| **Hyperbolic** | B² − AC >0 | Perambatan gelombang, mempertahankan fitur tajam | Persamaan gelombang: u_tt = c²u_xx |
### Persamaan Panas
∂u/∂t = α ∂²u/∂x²
Model difusi panas, penyebaran populasi, penetapan harga opsi (Black-Scholes).
| Properti | Pernyataan |
|----------|-----------|
| Menghaluskan | Solusi menjadi lancar seketika, bahkan dari data awal yang terputus-putus |
| Prinsip maksimum | Temperatur maksimum terjadi pada batas atau waktu awal |
| Pembalikan waktu | Tidak dapat diubah — tidak dapat berjalan mundur |
### Persamaan Gelombang
∂²u/∂t² = c² ∂²u/∂x²
Model senar getar, suara, gelombang elektromagnetik.
| Properti | Pernyataan |
|----------|-----------|
| Propagasi | Gangguan merambat dengan kecepatan c |
| Reversibilitas | Dapat dibalik waktu |
| solusi d'Alembert | u(x,t) = f(x−ct) + g(x+ct) (superposisi gelombang kiri/kanan) |
### Persamaan Laplace
∇²u = ∂²u/∂x² + ∂²u/∂y² = 0
Solusi (fungsi harmonik) mewakili suhu keadaan tunak, potensial elektrostatik, aliran fluida yang tidak dapat dimampatkan.
| Properti | Pernyataan |
|----------|-----------|
| Nilai rata-rata properti | u(x₀) = rata-rata u pada setiap lingkaran yang berpusat di x₀ |
| Prinsip maksimum | Tidak ada interior maxima atau minima |
| Keunikan | Ditentukan seluruhnya oleh syarat batas |
---

## Relevansi dengan Pembelajaran Mesin dan Ilmu Data
| Konsep DS | Aplikasi |
|-----------|-------------|
| ODE | Neural ODE (jaringan kedalaman berkelanjutan), dinamika jaringan berulang |
| Analisis stabilitas | Dinamika pelatihan penurunan gradien (apakah kerugiannya menurun secara stabil?) |
| Fungsi Lyapunov | Membuktikan konvergensi algoritma pembelajaran, penguatan stabilitas pembelajaran |
| Kekacauan | Memahami sensitivitas dalam RNN (gradien hilang/meledak), prediksi cuaca |
| Bifurkasi | Transisi Fase Pembelajaran (Grokking), Perubahan Rezim Dinamika Latihan |
| PDE | Model difusi (model generatif berbasis skor), jaringan saraf berbasis fisika |
| Persamaan panas | Proses difusi dalam pemodelan generatif, grafik Laplacian smoothing |
| Persamaan gelombang | Pengolahan data seismik, pemodelan sinyal audio |
| Lotka-Volterra | Dinamika populasi, epidemiologi, persaingan agen ML |
| Potret fase | Memvisualisasikan dinamika lanskap kerugian, memahami pelatihan GAN |
---

## Ringkasan
| Topik | Ide Inti | Alat Kunci |
|-------|-----------|----------|
| ODE | Fungsi dan turunan waktunya | Persamaan karakteristik, pengintegrasian faktor |
| Sistem ODE | Beberapa variabel yang berinteraksi | Analisis nilai eigen Jacobian |
| Potret fase | Memvisualisasikan dinamika ruang negara | Titik tetap, garis nol, siklus batas |
| Stabilitas | Akankah sistem kembali ke keseimbangan? | Linearisasi, fungsi Lyapunov |
| Kekacauan | Ketidakpastian deterministik | Eksponen Lyapunov, penarik aneh |
| Bifurkasi | Perubahan kualitatif dengan parameter | Bentuk normal, diagram bifurkasi |
| PDE | Fungsi Banyak Variabel | Persamaan panas, gelombang, dan Laplace |
Teori sistem dinamis adalah matematika perubahan. Hal ini menjelaskan mengapa beberapa sistem menjadi tenang, mengapa beberapa sistem berosilasi, dan mengapa beberapa sistem berperilaku kacau. Bagi ilmuwan data, ini menyediakan alat untuk memahami dinamika pelatihan, merancang algoritme yang stabil, memodelkan deret waktu, dan membangun model pembelajaran mesin berbasis fisika generasi berikutnya.