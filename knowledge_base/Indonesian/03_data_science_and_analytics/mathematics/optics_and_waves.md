<!--
---
# Metadata
title: "Optics and Waves"
description: "Wave equation, superposition, interference, diffraction, polarization, geometric optics, Fourier optics, and applications to signal processing and imaging"
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
    changes: "Initial deep-dive into optics and waves"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2027-02-10"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-10"

# Classification
tags: [optics, waves, wave-equation, interference, diffraction, polarization, geometric-optics, fourier-optics]
difficulty_level: "intermediate"
prerequisites:
  - "mathematics.md"
  - "electromagnetism.md"
estimated_reading_time: "22 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Optik dan Gelombang
Gelombang ada dimana-mana: suara, cahaya, air, sinyal radio, amplitudo probabilitas kuantum, fluktuasi pasar saham, dan getaran aktivasi jaringan saraf. Optik - studi tentang cahaya - adalah ilmu gelombang yang paling berkembang, dan alat matematikanya (analisis Fourier, interferensi, difraksi) berlaku untuk setiap fenomena gelombang. Memahami gelombang sangat penting untuk pemrosesan sinyal, analisis gambar, komunikasi, dan lapisan fisik dari semua teknologi modern.
---

## Persamaan Gelombang
### Persamaan Gelombang Umum
Persamaan gelombang satu dimensi:
∂²u/∂t² = c² ∂²u/∂x²
dimana u(x,t) adalah perpindahan gelombang dan c adalah cepat rambat gelombang.
### Solusi Umum (d'Alembert)
u(x,t) = f(x − ct) + g(x + ct)
dimana f adalah gelombang merambat ke kanan dan g adalah gelombang merambat ke kiri.
### Parameter Gelombang Kunci
| Parameter | Simbol | Satuan | Deskripsi |
|-----------|--------|------|-------------|
| Amplitudo | SEBUAH | bervariasi | Perpindahan maksimum |
| Panjang gelombang | | meter | Jarak antara puncak yang berurutan |
| Frekuensi | f atau | Hertz (Hz) | Siklus per detik |
| Periode | T = 1/f | detik | Waktu untuk satu siklus penuh |
| Nomor gelombang | k = 2π/λ | rad/m | Frekuensi spasial |
| Frekuensi sudut | ω = 2πf | rad/s | Frekuensi sementara |
| Kecepatan gelombang | c = fλ = ω/k | m/dtk | Kecepatan propagasi |
### Gelombang Sinusoidal
u(x,t) = Dosa(kx − ωt + φ)
di mana φ adalah konstanta fase.
### Kecepatan Gelombang di Berbagai Media
| Jenis Gelombang | Sedang | Rumus Kecepatan |
|-----------|--------|---------------|
| Tali | Ketegangan T, kerapatan linier μ | c = √(T/μ) |
| Suara | Modulus massal B, kepadatan ρ | c = √(B/ρ) |
| Bunyi (gas ideal) | γ, R, T, M | c = √(γRT/M) |
| Gelombang EM | Permitivitas ε, permeabilitas μ | c = 1/√(με) |
| Gelombang EM (vakum) | ε₀, μ₀ | c = 3 × 10⁸ m/s |
---

## Superposisi dan Interferensi
### Prinsip Superposisi
Ketika dua gelombang atau lebih saling tumpang tindih, perpindahan yang dihasilkan adalah jumlah perpindahan masing-masing gelombang:
u_total = u₁ + u₂ + ... + uₙ
Hal ini berlaku untuk persamaan gelombang linier.
### Interferensi Dua Gelombang
Dua gelombang dengan frekuensi dan amplitudo yang sama, beda fasa Δφ:
u_total = 2A cos(Δφ/2) sin(kx − ωt + Δφ/2)
| Perbedaan Fase | Hasil | Intensitas |
|-----------------|--------|-----------|
| Δφ = 0, 2π, 4π, ... | **Konstruktif** (amplitudo = 2A) | 4I₀ (maksimum) |
| Δφ = π, 3π, 5π, ... | **Merusak** (amplitudo = 0) | 0 (minimal) |
| Δφ = π/2 | Parsial | 2Saya₀ |
### Kondisi Interferensi
| Kondisi | Ketik | Perbedaan Jalur |
|-----------|------|-----------------|
| Konstruktif | Pinggiran cerah | ΔL = mλ (m = 0, 1, 2, ...) |
| Merusak | Pinggiran gelap | ΔL = (m + ½)λ |
---

## Eksperimen Celah Ganda Young
Cahaya melewati dua celah sempit yang dipisahkan oleh jarak d, menciptakan pola interferensi pada layar pada jarak L.
### Posisi Pinggiran
| Pinggiran | Posisi di Layar |
|--------|-------------------|
| Cerah (maksimal) | y_m = mλL/d |
| Gelap (minima) | y_m = (m + ½)λL/d |
| Jarak pinggiran | Δy = λL/d |
Eksperimen ini membuktikan sifat gelombang cahaya (Thomas Young, 1801) dan kemudian menjadi inti mekanika kuantum (dualitas gelombang-partikel).
---

## Difraksi
**Difraksi** adalah pembelokan dan penyebaran gelombang di sekitar rintangan dan melalui bukaan.
### Difraksi Celah Tunggal
Cahaya melalui celah lebar a menghasilkan pola pinggiran terang dan gelap.
| Fitur | Kondisi |
|---------|-----------|
| Maksimum pusat | Terluas dan paling terang; lebar = 2λL/a |
| Minima (pinggiran gelap) | dosa θ = mλ (m = ±1, ±2, ...) |
| Maksimum sekunder | Kira-kira antara minimum; jauh lebih redup |
### Kisi Difraksi
N celah dengan jarak yang sama (jarak d) menghasilkan maksimum yang sangat tajam:
d dosa θ = mλ (m = 0, 1, 2, ...)
| Properti | Efek |
|----------|--------|
| Lebih banyak celah (N lebih besar) | Maksimum yang lebih tajam dan cerah |
| Kekuatan penyelesaian | R = mN (dapat membedakan panjang gelombang dekat) |
| Aplikasi | Spektroskopi, pengukuran panjang gelombang |
### Kriteria Rayleigh (Batas Resolusi)
Dua sumber titik hanya dapat diselesaikan jika maksimum pusat dari salah satu sumber berada pada minimum pertama sumber titik lainnya:
θ_min = 1,22 λ/D
di mana D adalah diameter bukaan.
| Sistem | | D | θ_min |
|--------|---|---|-------|
| Mata manusia | 550nm | 5 mm | 1,3 × 10⁻⁴ rad (~0,01°) |
| Teleskop Luar Angkasa Hubble | 550nm | 2,4 m | 2,8 × 10⁻⁷ rad |
| Teleskop Radio (Arecibo) | 21cm | 305 m | 8,4 × 10⁻⁴ rad |
---

## Polarisasi
**Polarisasi** menjelaskan orientasi osilasi medan listrik pada gelombang transversal.
### Jenis Polarisasi
| Ketik | Deskripsi |
|------|-------------|
| **Linier** | E berosilasi pada bidang tetap |
| **Lingkaran** | E berputar melingkar (tangan kanan atau kiri) |
| **Elips** | E menelusuri elips (paling umum) |
| **Tidak terpolarisasi** | Campuran acak dari semua polarisasi (cahaya paling alami) |
### Hukum Malus
Ketika cahaya terpolarisasi melewati polariser dengan sudut θ terhadap arah polarisasi:
Saya = Saya₀ cos²θ
| Sudut | Intensitas yang Ditransmisikan |
|---------|----------------------|
| 0° | 100% (Saya₀) |
| 30° | 75% |
| 45° | 50% |
| 60° | 25% |
| 90° | 0% (diblokir sepenuhnya) |
### Polarisasi berdasarkan Refleksi (Sudut Brewster)
Cahaya yang dipantulkan pada sudut Brewster terpolarisasi sempurna:
tan θ_B = n₂/n₁
| Antarmuka | n₁ | n₂ | θ_B |
|-----------|----|----|-----|
| Udara → kaca | 1.0 | 1.5 | 56,3° |
| Udara → air | 1.0 | 1.33 | 53,1° |
| Kaca → berlian | 1.5 | 2.42 | 58,1° |
---

## Optik Geometris
Optik geometris (sinar) memperlakukan cahaya sebagai sinar yang merambat dalam garis lurus, membelok pada antarmuka.
### Hukum Snell (Refraksi)
n₁ dosa θ₁ = n₂ dosa θ₂
| Bahan | Indeks Bias n |
|----------|-------------------|
| vakum | 1.000 |
| Udara | 1.0003 |
| Air | 1.33 |
| Kaca (mahkota) | 1.52 |
| Kaca (batu api) | 1.62 |
| berlian | 2.42 |
### Refleksi Internal Total
Saat cahaya merambat dari medium yang lebih rapat ke medium yang kurang rapat, melampaui **sudut kritis**:
θ_c = arcsin(n₂/n₁)
Semua cahaya dipantulkan — begitulah cara kerja serat optik.
### Persamaan Lensa Tipis
1/f = 1/d_o + 1/d_i
| Kuantitas | Arti |
|----------|---------|
| f | Panjang fokus |
| lakukan_o | Jarak benda |
| d_i | Jarak gambar |
| M = −d_i/d_o | Pembesaran |
| Jenis Lensa | f | Gambar |
|-----------|---|-------|
| Konvergen (cembung) | Positif | Nyata (jika d_o > f) atau maya |
| Divergen (cekung) | Negatif | Selalu maya, tegak, diperkecil |
### Persamaan Cermin
Bentuknya sama dengan persamaan lensa: 1/f = 1/d_o + 1/d_i, dimana f = R/2 untuk cermin bola.
---

## Optik Fourier
Optik Fourier memperlakukan pencitraan dan difraksi sebagai operasi transformasi Fourier.
### Prinsip Utama
Pola difraksi medan jauh pada bukaan adalah **Transformasi Fourier** dari fungsi bukaan.
| Bukaan | Pola Difraksi (Transformasi Fourier) |
|----------|----------------------------------------|
| Celah tunggal | fungsi sin |
| Bukaan melingkar | Disk lapang (J₁(r)/r) |
| Bukaan persegi panjang | Sinkronisasi 2D |
| Kisi | Fungsi delta diskrit |
### Transformasi Fourier Optik
Lensa melakukan transformasi Fourier 2D: menempatkan objek pada bidang fokus depan menghasilkan transformasi Fourier pada bidang fokus belakang.
### Aplikasi
| Aplikasi | Bagaimana Optik Fourier Membantu |
|-------------|-------------------------|
| Pemfilteran gambar | Tempatkan masker pada bidang Fourier untuk memblokir/melewati frekuensi spasial |
| Deteksi tepi | Penyaringan lolos tinggi pada bidang Fourier |
| Pengenalan pola | Korelasi melalui transformasi Fourier |
| Holografi | Merekam dan merekonstruksi muka gelombang |
| Komputasi optik | Melakukan transformasi Fourier dengan kecepatan cahaya |
---

## Suara dan Akustik
### Properti Gelombang Suara
| Properti | Rentang Khas | Satuan |
|----------|--------------|------|
| Frekuensi | 20 − 20.000 (pendengaran manusia) | Hz |
| Kecepatan (udara, 20°C) | 343 | m/dtk |
| Kecepatan (air) | 1.480 | m/dtk |
| Kecepatan (baja) | 5.960 | m/dtk |
| Ambang batas intensitas | 10⁻¹² | L/m² |
### Skala Desibel
β = 10 log₁₀(I/I₀) dB, dengan I₀ = 10⁻¹² W/m²
| Suara | Intensitas (W/m²) | Tingkat (dB) |
|-------|-------------------|------------|
| Ambang pendengaran | 10⁻¹² | 0 |
| Gemerisik daun | 10⁻¹¹ | 10 |
| Percakapan biasa | 10⁻⁶ | 60 |
| Konser rock | 1 | 120 |
| Ambang batas rasa sakit | 10 | 130 |
| Mesin jet | 100 | 140 |
### Efek Doppler
Frekuensi teramati ketika sumber dan pengamat bergerak relatif satu sama lain:
f' = f(v ± v_o)/(v ∓ v_s)
| Skenario | Efek |
|----------|--------|
| Sumber mendekat | Frekuensi lebih tinggi (pergeseran biru untuk cahaya) |
| Sumber surut | Frekuensi lebih rendah (pergeseran merah untuk cahaya) |
| Aplikasi | Radar, USG medis, astronomi (pergeseran merah galaksi) |
---

## Relevansi dengan Pembelajaran Mesin dan Ilmu Data
| Konsep Gelombang/Optik | Aplikasi |
|------|-------------|
| Persamaan gelombang | Jaringan saraf berbasis fisika, analisis data seismik, pemrosesan audio |
| Analisis Fourier | Landasan pemrosesan sinyal, analisis spektral, ekstraksi fitur |
| Transformasi Fourier | CNN secara implisit melakukan analisis Fourier lokal; FFT digunakan dalam prapemrosesan data |
| Interferensi | Komputasi analog, jaringan saraf optik |
| Difraksi | Model pembentukan gambar, algoritma deblurring, fotografi komputasi |
| Polarisasi | Penginderaan jauh, klasifikasi material, analisis citra satelit |
| Optik geometris | Model kamera dalam visi komputer, penelusuran sinar untuk pembuatan data sintetis |
| Persamaan lensa | Kalibrasi kamera, estimasi kedalaman, rekonstruksi 3D |
| Optik Fourier | Komputasi optik, jaringan saraf dalam difraksi (D²NN) |
| Efek Doppler | Pemrosesan sinyal radar, pencitraan medis (USG Doppler), estimasi kecepatan |
| Skala desibel | Rekayasa fitur audio, prapemrosesan pengenalan suara |
| Teori pengambilan sampel | Teorema Nyquist-Shannon menghubungkan teori gelombang dengan pemrosesan sinyal digital |
---

## Ringkasan
| Topik | Ide Inti | Persamaan Kunci |
|-------|-----------|-------------|
| Persamaan gelombang | Gelombang merambat dengan kecepatan c | ∂²u/∂t² = c²∂²u/∂x² |
| Superposisi | Gelombang bertambah secara linier | kamu = u₁ + u₂ |
| Interferensi | Fase menentukan penguatan | Δφ = 2πΔL/λ |
| Difraksi | Gelombang membelok di sekitar rintangan | a sin θ = mλ (celah tunggal) |
| Polarisasi | Orientasi osilasi | Hukum Malus : I = I₀cos²θ |
| Optik geometris | Seringan sinar | Hukum Snell: n₁sinθ₁ = n₂sinθ₂ |
| Optik Fourier | Pencitraan sebagai transformasi Fourier | Medan jauh = FT bukaan |
| Efek Doppler | Pergeseran frekuensi dari gerak | f' = f(v ± v_o)/(v ∓ v_s) |
Gelombang adalah bahasa universal sistem berosilasi. Baik Anda memproses sinyal audio, menganalisis deret waktu, merancang sistem pengenalan gambar, atau membuat simulasi fisika, matematika gelombang — superposisi, analisis Fourier, interferensi, difraksi — menyediakan perangkat yang penting. Optik, sebagai ilmu gelombang paling matang, menawarkan landasan teoretis dan teknik praktis yang mencakup ilmu data modern.