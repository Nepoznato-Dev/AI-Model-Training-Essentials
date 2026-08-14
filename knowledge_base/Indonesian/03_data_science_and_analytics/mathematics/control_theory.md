---
# Metadata
title: "Control Theory"
description: "Transfer functions, block diagrams, feedback loops, PID controllers, stability analysis, state-space representation, and optimal control"
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
    changes: "Initial deep-dive into control theory"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2027-02-10"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-10"

# Classification
tags: [control-theory, transfer-functions, pid-controllers, feedback, stability, state-space, optimal-control]
difficulty_level: "advanced"
prerequisites:
  - "mathematics.md"
  - "signal_processing.md"
  - "dynamical_systems.md"
estimated_reading_time: "22 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# Teori Kontrol
Teori kontrol adalah ilmu matematika yang membuat sistem berperilaku sesuai keinginan Anda. Dari termostat hingga autopilot, dari lengan robot hingga reaktor kimia, sistem kendali merasakan, memutuskan, dan bertindak untuk mempertahankan perilaku yang diinginkan. Bidang ini menyediakan alat yang canggih untuk menganalisis stabilitas, kinerja, dan ketahanan — konsep yang telah bermigrasi ke pembelajaran penguatan, penyesuaian hyperparameter, dan sistem adaptif.
---

## Konsep Dasar
### Loop Terbuka vs Loop Tertutup
| Ketik | Deskripsi | Contoh | Keuntungan |
|------|-------------|---------|-----------|
| **Loop terbuka** | Tindakan kontrol tidak bergantung pada keluaran | Pengatur waktu mesin cuci | Sederhana, tidak perlu sensor |
| **Loop tertutup (umpan balik)** | Tindakan pengendalian bergantung pada keluaran | Termostat, kendali jelajah | Menolak gangguan, kuat |
### Elemen Diagram Blok
| Elemen | Simbol | Fungsi |
|---------|--------|----------|
| **Tanaman** | G(s) | Sistem yang dikendalikan |
| **Pengontrol** | C(s) | Menghitung tindakan kontrol |
| **Sensor** | H(s) | Mengukur keluaran |
| **Menjumlahkan persimpangan** | ⊕ | Menghitung kesalahan: r − y |
| **Referensi** | r(t) | Keluaran yang diinginkan |
| **Kesalahan** | e(t) = r(t) − y(t) | Perbedaan antara yang diinginkan dan sebenarnya |
| **Gangguan** | d(t) | Masukan yang tidak diinginkan mempengaruhi tanaman |
### Fungsi Transfer Loop Tertutup
Untuk sistem umpan balik negatif standar:
T(s) = C(s)G(s) / (1 + C(s)G(s)H(s))
| Kuantitas | Rumus |
|----------|---------|
| Fungsi transfer loop terbuka | L(s) = C(s)G(s)H(s) |
| Fungsi transfer loop tertutup | T(s) = L(s)/H(s) / (1 + L(s)) |
| Fungsi transfer kesalahan | E(s)/R(s) = 1 / (1 + L(s)) |
| Sensitivitas | S(s) = 1 / (1 + L(s)) |
---

## Fungsi Transfer
**Fungsi transfer** H(s) = Y(s)/X(s) menjelaskan hubungan input-output sistem invarian waktu linier (LTI) dalam domain Laplace.
### Formulir Standar
| Sistem | Fungsi Transfer | Parameter |
|--------|-------------------|------------|
| **Pesanan pertama** | K/(τs + 1) | K = penguatan, τ = konstanta waktu |
| **Pesanan kedua** | Kωₙ²/(s² + 2ζωₙs + ωₙ²) | ωₙ = frekuensi natural, ζ = rasio redaman |
| **Integrator** | K/dtk | — |
| **Pembeda** | Ks | — |
| **Penundaan** | e^{−sT_d} | T_d = waktu tunda |
### Perilaku Sistem Orde Kedua
| Rasio Redaman ζ | Perilaku | Lokasi Tiang |
|-----------------|-----------|---------------|
| = 0 | Osilasi tak teredam | Imajinasi murni |
| 0< ζ < 1 | Underdamped (oscillates, decays) | Complex with negative real part |
| ζ = 1 | Critically damped (fastest no-oscillation) | Real, repeated |
| ζ >1 | Overdamped (lambat, tidak ada osilasi) | Nyata, berbeda |
### Metrik Kinerja (Respon Langkah)
| Metrik | Formula (urutan ke-2, underdamped) | Deskripsi |
|--------|----------------------------------|-------------|
| Waktu terbit (t_r) | ≈ 1,8/ωₙ | Saatnya beralih dari 10% ke 90% |
| Waktu puncak (t_p) | π/(ωₙ√(1−ζ²)) | Waktunya mencapai maksimum pertama |
| Melampaui (M_p) | e^{−πζ/√(1−ζ²)} × 100% | Puncak maksimum di atas nilai akhir |
| Waktu penyelesaian (t_s) | ≈ 4/(ζωₙ) | Saatnya untuk tetap berada dalam 2% dari final |
| Kesalahan keadaan tunak | Tergantung pada tipe sistem | Selisih antara yang diinginkan dan aktual sebagai t → ∞ |
---

## Pengontrol PID
**Pengontrol PID** adalah pengontrol yang paling banyak digunakan di industri (lebih dari 90% pengontrol industri).
### Rumus PID
u(t) = K_p e(t) + K_i ∫₀ᵗ e(τ)dτ + K_d de(t)/dt
Dalam domain Laplace: C(s) = K_p + K_i/s + K_d s
| Istilah | Efek | Terlalu Banyak | Terlalu Sedikit |
|------|--------|----------|------------|
| **Proporsional (K_p)** | Bereaksi terhadap kesalahan saat ini | Osilasi, ketidakstabilan | Respon lambat, kesalahan besar |
| **Integral (K_i)** | Menghilangkan kesalahan kondisi tunak | Overshoot, osilasi | Offset persisten |
| **Derivatif (K_d)** | Memprediksi kesalahan di masa depan (redaman) | Amplifikasi kebisingan | Penolakan gangguan yang buruk |
### Metode Penyetelan PID
| Metode | Pendekatan |
|--------|----------|
| **Ziegler-Nichols** | Tingkatkan K_u hingga berosilasi; gunakan K_u dan titik P_u untuk menetapkan keuntungan |
| **Cohen-Coon** | Berdasarkan parameter respon langkah (gain, konstanta waktu, waktu mati) |
| **IMC (Kontrol Model Internal)** | Berdasarkan model proses; memberikan ketahanan yang baik |
| **Penyetelan otomatis** | Identifikasi online + penyetelan (banyak pengontrol modern) |
| **Pedoman** | Mulailah dengan K_p saja, tambahkan K_i untuk menghilangkan offset, tambahkan K_d untuk redaman |
### Aturan Ziegler-Nichols
1. Tetapkan K_i = K_d = 0
2. Tingkatkan K_p hingga osilasi berkelanjutan: penguatan akhir K_u, periode P_u
3. Tetapkan keuntungan:
| Pengendali | K_p | K_i | K_d |
|-----------|-----|-----|-----|
| P | 0,5K_u | — | — |
| PI | 0,45K_u | 1.2K_u/P_u | — |
| PID | 0,6K_u | 2K_u/P_u | K_u P_u/8 |
---

## Analisis Stabilitas
Suatu sistem **stabil** jika outputnya tetap dibatasi oleh input yang dibatasi (stabilitas BIBO).
### Stabilitas Berbasis Tiang
| Kondisi | Stabilitas |
|-----------|-----------|
| Semua kutub di setengah bidang kiri (Re(s)< 0) | Stable |
| Any pole in right half-plane (Re(s) >0) | Tidak stabil |
| Kutub pada sumbu imajiner (Re(s) = 0) | Sedikit stabil (atau tidak stabil untuk pengulangan) |
### Kriteria Routh-Hurwitz
Menentukan stabilitas tanpa menghitung kutub secara eksplisit. Membangun array Routh dari koefisien polinomial karakteristik.
**Peraturan:** Banyaknya perubahan tanda pada kolom pertama sama dengan jumlah tiang setengah bidang kanan.
### Kriteria Stabilitas Nyquist
Plot respons frekuensi loop terbuka L(jω) pada bidang kompleks.
**Peraturan:** Sistem loop tertutup stabil jika plot Nyquist mengelilingi titik (−1, 0) berlawanan arah jarum jam beberapa kali sama dengan jumlah kutub tidak stabil loop terbuka.
**Margin keuntungan:** Berapa banyak keuntungan yang dapat ditingkatkan sebelum ketidakstabilan (jarak dari plot ke −1 pada sumbu nyata).
**Margin fase:** Berapa banyak jeda fase yang dapat meningkat sebelum ketidakstabilan (sudut dari plot ke lingkaran unit pada persilangan penguatan).
### Analisis Plot Pertanda
Penguatan plot (dB) dan fase (derajat) vs frekuensi (skala log).
| Metrik | Definisi | Nilai yang Diinginkan |
|--------|-----------|---------------|
| **Margin keuntungan (GM)** | Dapatkan peningkatan hingga mencapai 0 dB pada fase = −180° | > 6 dB |
| **Margin fase (PM)** | Fase pada penguatan crossover (0 dB) + 180° | > 45° |
| **Dapatkan persilangan** | Frekuensi dimana gain = 0 dB | — |
| **Persilangan fase** | Frekuensi dimana fase = −180° | — |
---

## Representasi Ruang-Negara
Untuk sistem multi-input multi-output (MIMO), bentuk ruang keadaan lebih alami dibandingkan fungsi transfer.
### Formulir Standar
ẋ(t) = Ax(t) + Bu(t) (persamaan keadaan)
y(t) = Cx(t) + Du(t) (persamaan keluaran)
| Matriks | Nama | Dimensi |
|--------|------|-----------|
| SEBUAH | Matriks sistem/keadaan | n × n |
| B | Matriks masukan | n × m |
| C | Matriks keluaran | p × n |
| D | Matriks umpan balik | hal × m |
### Fungsi Transfer dari State-Space
G(s) = C(sI − A)⁻¹B + D
### Pengendalian dan Pengamatan
| Properti | Tes | Arti |
|----------|------|---------|
| **Dapat dikontrol** | Peringkat[C_B] = n (di mana C_B = [B, AB, A²B, ...]) | Dapat mengarahkan ke negara bagian mana pun |
| **Dapat Diamati** | Peringkat[O_B] = n (di mana O_B = [C; CA; CA²; ...]) | Dapat menentukan keadaan dari keluaran |
Suatu sistem harus dapat dikontrol agar dapat distabilkan dengan umpan balik, dan dapat diamati untuk estimasi keadaan.
### Nyatakan Masukan
u = −Kx + r (umpan balik keadaan penuh)
Loop tertutup: ẋ = (A − BK)x + Br
**Penempatan tiang:** Pilih K sedemikian rupa sehingga A − BK memiliki nilai eigen (kutub) yang diinginkan.
---

## Kontrol Optimal
### Regulator Kuadrat Linier (LQR)
Minimalkan: J = ∫₀^∞ (xᵀQx + uᵀRu) dt
dimana Q ≥ 0 (biaya negara) dan R > 0 (biaya pengendalian).
**Solusi:** u = −Kx dengan K = R⁻¹BᵀP, dan P menyelesaikan **persamaan aljabar Riccati:**
AᵀP + PA − PBR⁻¹BᵀP + Q = 0
| Penyetelan | Efek |
|--------|--------|
| Tingkatkan Q | Respon lebih cepat, upaya kontrol lebih banyak |
| Tingkatkan R | Respons lebih lambat, upaya kontrol lebih sedikit |
| Q ≫ R | Kontrol agresif (seperti K_p tinggi) |
### Filter Kalman
Penduga keadaan optimal untuk sistem linier dengan derau Gaussian.
**Model sistem:**
ẋ = Ax + Bu + w (kebisingan proses w ~ N(0, Q))
y = Cx + v (pengukuran kebisingan v ~ N(0, R))
**Persamaan filter Kalman:**
- Prediksi: x̂⁻ = Ax̂ + Bu, P⁻ = APAᵀ + Q
- Pembaruan: K = P⁻Cᵀ(CP⁻Cᵀ + R)⁻¹, x̂ = x̂⁻ + K(y − Cx̂⁻), P = (I − KC)P⁻
Filter Kalman adalah LQR ganda — filter ini meminimalkan varians kesalahan estimasi.
---

## Relevansi dengan Pembelajaran Mesin dan Ilmu Data
| Konsep Teori Kontrol | Aplikasi |
|-------|-------------|
| Kontrol umpan balik | Kecepatan pembelajaran adaptif, stabilisasi pelatihan |
| Pengontrol PID | Penyetelan hyperparameter, kontrol suhu di pusat data |
| Model ruang negara | Pemodelan deret waktu, jaringan saraf berulang |
| Filter Kalman | Pelacakan, fusi sensor, estimasi keadaan, perkiraan deret waktu |
| LQR / kontrol optimal | Pembelajaran penguatan (kontrol LQG), robotika |
| Analisis stabilitas | Dinamika pelatihan GAN, konvergensi algoritma RL |
| Pengendalian/observabilitas | Memahami ekspresi RNN, identifikasi sistem |
| Fungsi alih | Memahami CNN sebagai filter linier, analisis domain frekuensi |
| Nyquist/Pertanda | Analisis ketahanan untuk sistem adaptif |
| Penempatan tiang | Merancang dinamika sistem yang dipelajari (Neural ODEs) |
---

## Ringkasan
| Konsep | Ide Inti | Alat Kunci |
|---------|-----------|----------|
| Umpan Balik | Gunakan keluaran untuk memperbaiki masukan | Fungsi transfer loop tertutup |
| Fungsi alih | Hubungan input-output di s-domain | G(s) = Y(s)/X(s) |
| Kontrol PID | Proporsional + Integral + Turunan | Pengontrol industri yang paling banyak digunakan |
| Stabilitas | Keluaran yang dibatasi untuk masukan yang dibatasi | Routh-Hurwitz, Nyquist, Bode |
| Ruang negara | Representasi internal negara | ẋ = Kapak + Bu, y = Cx + Du |
| Pengendalian | Bisakah kita mencapai negara bagian mana pun? | Uji peringkat pada matriks keterkendalian |
| Observabilitas | Bisakah kita menyimpulkan keadaannya? | Uji peringkat pada matriks observabilitas |
| LQR | Umpan balik keadaan optimal | Persamaan Riccati |
| Filter Kalman | Estimasi keadaan optimal | Siklus prediksi-pembaruan |
Teori kontrol adalah ilmu matematika yang membuat sistem melakukan apa yang Anda inginkan — andal, kuat, dan efisien. Prinsip umpan balik, stabilitas, dan optimalitasnya telah terbukti universal, muncul di berbagai bidang mulai dari robotika hingga pembelajaran penguatan, dari ekonomi hingga biologi. Bagi ilmuwan data, teori kontrol menyediakan bahasa untuk memahami sistem adaptif, merancang prosedur pelatihan yang stabil, dan membangun agen cerdas yang berinteraksi dengan lingkungan dinamis.