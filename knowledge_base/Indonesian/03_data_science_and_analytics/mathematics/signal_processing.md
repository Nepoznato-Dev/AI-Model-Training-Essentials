---
# Metadata
title: "Signal Processing"
description: "Fourier transforms, FFT, Laplace transforms, Z-transforms, filtering, sampling theorem, windowing, spectral analysis, and wavelets"
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
    changes: "Initial deep-dive into signal processing"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2027-02-10"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-10"

# Classification
tags: [signal-processing, fourier-transform, fft, laplace-transform, z-transform, filtering, sampling-theorem, wavelets]
difficulty_level: "advanced"
prerequisites:
  - "mathematics.md"
  - "optics_and_waves.md"
  - "numerical_methods.md"
estimated_reading_time: "25 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Pemrosesan Sinyal
Pemrosesan sinyal adalah ilmu menganalisis, memodifikasi, dan mensintesis sinyal — representasi kuantitas fisik yang bervariasi seiring waktu, ruang, atau frekuensi. Audio, gambar, video, data sensor, gelombang otak, harga saham — semuanya adalah sinyal. Alat matematika pemrosesan sinyal (transformasi Fourier, filter, teori pengambilan sampel) merupakan dasar pembelajaran mesin, komunikasi, pencitraan medis, dan hampir semua bidang yang bekerja dengan data.
---

## Sinyal dan Sistem
### Klasifikasi Sinyal
| Ketik | Deskripsi | Contoh |
|------|-------------|---------|
| **Waktu berkelanjutan** | Didefinisikan untuk semua t ∈ ℝ | Tegangan audio, suhu |
| **Waktu diskrit** | Didefinisikan pada indeks bilangan bulat n | Sampel audio, nilai piksel |
| **Analog** | Kontinyu dalam waktu dan amplitudo | Alur rekaman vinil |
| **Digital** | Diskrit dalam waktu dan amplitudo terkuantisasi | File MP3, gambar JPEG |
| **Berkala** | x(t + T) = x(t) untuk semua t | Gelombang sinus, gelombang persegi |
| **Aperiodik** | Tidak ada pola berulang | Pidato, musik |
| **Deterministik** | Benar-benar dapat diprediksi | Gelombang sinus |
| **Stokastik** | Berisi keacakan | Kebisingan, harga saham |
### Properti Sistem
| Properti | Definisi | Contoh |
|----------|-----------|---------|
| **Linier** | T[ax₁ + bx₂] = aT[x₁] + bT[x₂] | Filter lolos rendah |
| **Invarian waktu** | Pergeseran masukan → pergeseran keluaran yang sama | Filter tetap apa pun |
| **Kausal** | Output hanya bergantung pada input sekarang dan masa lalu | Sistem waktu nyata |
| **Stabil (BIBO)** | Masukan terbatas → keluaran terbatas | Filter yang dirancang dengan baik |
| **Tanpa memori** | Output hanya bergantung pada input saat ini | Penguat |
---

## Transformasi Fourier
**Transformasi Fourier** menguraikan sinyal menjadi frekuensi penyusunnya.
### Transformasi Fourier Berkelanjutan
X(f) = ∫_{−∞}^{∞} x(t) e^{−j2πft} dt
Invers: x(t) = ∫_{−∞}^{∞} X(f) e^{j2πft} df
### Pasangan Transformasi Fourier
| Domain Waktu x(t) | Domain Frekuensi X(f) |
|-------------------|----------------------|
| Pulsa persegi panjang | fungsi sin |
| fungsi sin | Pulsa persegi panjang |
| Gaussian e^{−at²} | Gaussian (√(π/a))e^{−π²f²/a} |
| Delta Dirac δ(t) | 1 (semua frekuensi) |
| Eksponensial kompleks e^{j2πf₀t} | δ(f − f₀) |
| Cosinus cos(2πf₀t) | ½[δ(f−f₀) + δ(f+f₀)] |
### Properti Utama
| Properti | Domain Waktu | Domain Frekuensi |
|----------|-------------|-----------------|
| Linearitas | kapak₁(t) + bx₂(t) | aX₁(f) + bX₂(f) |
| Pergeseran waktu | x(t − t₀) | X(f)e^{−j2πft₀} |
| Pergeseran frekuensi | x(t)e^{j2πf₀t} | X(f − f₀) |
| Konvolusi | x₁(t) ∗ x₂(t) | X₁(f) · X₂(f) |
| Perkalian | x₁(t) · x₂(t) | X₁(f) ∗ X₂(f) |
| Diferensiasi | dx/dt | j2πf X(f) |
| Teorema Parseval | ∫\|x(t)\|² dt | ∫\|X(f)\|² df |
**Teorema konvolusi:** Konvolusi waktu = perkalian frekuensi. Ini adalah properti yang paling penting — ini mengubah operasi konvolusi yang mahal menjadi perkalian yang murah.
### Transformasi Fourier Diskrit (DFT)
Untuk barisan x[0], x[1], ..., x[N−1]:
X[k] = Σ_{n=0}^{N−1} x[n] e^{−j2πkn/N}, k = 0, 1, ..., N−1
| Properti | Nilai |
|----------|-------|
| Masukan | N sampel nyata atau kompleks |
| Keluaran | N tempat frekuensi kompleks |
| Resolusi frekuensi | f_s/N (di mana f_s adalah laju pengambilan sampel) |
| Frekuensi Nyquist | f_s/2 (frekuensi maksimum yang dapat direpresentasikan) |
| Kompleksitas | O(N²) perhitungan langsung |
### Transformasi Fourier Cepat (FFT)
**FFT** menghitung DFT dalam O(N log N) dan bukan O(N²).
| tidak | Operasi O(N²) | O(N log N) Operasi | Mempercepat |
|---|------------------|----------------------|---------|
| 1.024 | 1.048.576 | 10.240 | 102× |
| 1.048.576 | 1,1 × 10¹² | 20.971.520 | 52.428× |
FFT adalah salah satu algoritma terpenting yang pernah ditemukan. Ini memungkinkan pemrosesan audio real-time, kompresi gambar (JPEG), komunikasi nirkabel (OFDM), dan analisis spektral.
---

## Transformasi Laplace
**Transformasi Laplace** memperluas transformasi Fourier untuk menangani sistem yang tidak stabil dan analisis sementara.
F(s) = ∫₀^∞ f(t) e^{−st} dt, dengan s = σ + jω
### Transformasi Laplace Umum
| f(t) | F(s) | Wilayah Konvergensi |
|------|------|----------------------|
| δ(t) (impuls) | 1 | Semua |
| kamu(t) (langkah) | 1/dtk | Ulang > 0 |
| e^{−at}u(t) | 1/(s+a) | Re(s) > −a |
| kamu(t) | n!/s^{n+1} | Ulang > 0 |
| dosa(ωt)kamu(t) | ω/(s²+ω²) | Ulang > 0 |
| cos(ωt)kamu(t) | s/(s²+ω²) | Ulang > 0 |
### Koneksi ke Transformasi Fourier
Ketika σ = 0 (s = jω), transformasi Laplace tereduksi menjadi transformasi Fourier. Transformasi Laplace memberikan gambaran yang lebih lengkap dengan memasukkan informasi tentang pertumbuhan/peluruhan (σ).
---

## Z-Transformasi
**Transformasi Z** adalah persamaan waktu diskrit dengan transformasi Laplace.
X(z) = Σ_{n=−∞}^{∞} x[n] z^{−n}
### Transformasi Z Umum
| x[n] | X(z) | ROC |
|------|------|-----|
| δ[n] | 1 | Semua z |
| kamu[n] (langkah) | z/(z−1) | \|z\| > 1 |
| aⁿu[n] | z/(z−a) | \|z\| > \|a\| |
| naⁿu[n] | az/(z−a)² | \|z\| > \|a\| |
| dosa(ω₀n)kamu[n] | z sin(ω₀)/(z²−2z cos(ω₀)+1) | \|z\| > 1 |
### Hubungan dengan Transformasi Lainnya
| Transformasi | Domain | Variabel |
|-----------|--------|----------|
| Fourier | Frekuensi kontinu | f atau ω |
| Laplace | Frekuensi kompleks | s = σ + jω |
| Transformasi Z | Frekuensi kompleks (diskrit) | z = e^{sT} |
Lingkaran satuan pada bidang z (|z| = 1) berhubungan dengan transformasi Fourier.
---

## Filter
Filter secara selektif melewatkan atau memblokir komponen frekuensi tertentu.
### Jenis Filter
| Ketik | Lulus | Blok | Aplikasi |
|------|--------|--------|-------------|
| **Lulus rendah** | Frekuensi rendah | Frekuensi tinggi | Menghaluskan, anti-aliasing |
| **Lulusan tinggi** | Frekuensi tinggi | Frekuensi rendah | Deteksi tepi, penghilangan kebisingan |
| **Band-pass** | Rentang frekuensi | Di luar jangkauan | Pemilihan saluran (radio) |
| **Band-stop (takik)** | Semuanya kecuali rentang | Rentang tertentu | Penghapusan dengungan saluran listrik |
### Filter FIR vs IIR
| Properti | FIR (Respon Impuls Terbatas) | IIR (Respon Impuls Tak Terbatas) |
|----------|-------------------------------|--------------------------------|
| Respon impuls | Durasi terbatas | Durasi tak terbatas |
| Stabilitas | Selalu stabil | Bisa tidak stabil |
| Fase | Bisa persis linier | Umumnya fase nonlinier |
| Umpan Balik | Tidak | Ya |
| Perhitungan | Diperlukan lebih banyak koefisien | Koefisien lebih sedikit untuk roll-off yang sama |
| Desain | Jendela, Taman-McClellan | Butterworth, Chebyshev, elips |
| Fungsi alih | H(z) = Σ bₖz⁻ᵏ | H(z) = Σ bₖz⁻ᵏ / (1 + Σ aₖz⁻ᵏ) |
### Spesifikasi Desain Filter
| Parameter | Deskripsi |
|-----------|-------------|
| **Passband** | Rentang frekuensi yang harus dilewati dengan kerugian minimal |
| **Stopband** | Rentang frekuensi yang harus dilemahkan |
| **Frekuensi batas** | Batas antara passband dan stopband |
| **Riak** | Variasi penguatan passband (atau stopband) |
| **Peluncuran** | Tingkat redaman (dB per oktaf atau dekade) |
| **Pita transisi** | Wilayah antara passband dan stopband |
### Desain Filter Umum
| Desain | Karakteristik | Kasus Penggunaan |
|--------|----------------|----------|
| **Butterworth** | Passband datar maksimal, roll-off sedang | Tujuan umum |
| **Chebyshev Tipe I** | Ripple di passband, roll-off lebih curam | Ketika roll-off penting |
| **Chebyshev Tipe II** | Riak di stopband, passband datar | Ketika kerataan pita sandi penting |
| **Eliptik (Cauer)** | Riak di keduanya, roll-off paling curam | Diperlukan minimum pemesanan |
| **Bessel** | Fase linier (penundaan grup datar maksimal) | Mempertahankan bentuk gelombang |
---

## Teori Pengambilan Sampel
### Teorema Pengambilan Sampel Nyquist-Shannon
Sinyal kontinu dapat direkonstruksi secara sempurna dari sampelnya jika laju pengambilan sampel melebihi dua kali frekuensi maksimum:
f_s > 2f_maks
| Istilah | Definisi |
|------|------------|
| **Tingkat pengambilan sampel** (f_s) | Jumlah sampel per detik |
| **Tingkat Nyquist** | 2f_max (tingkat pengambilan sampel minimum) |
| **Frekuensi Nyquist** | f_s/2 (frekuensi maksimum yang dapat direpresentasikan) |
| **Alias** | Frekuensi tinggi menyamar sebagai frekuensi rendah ketika f_s < 2f_max |
### Tarif Pengambilan Sampel Umum
| Aplikasi | Nilai | Frekuensi Nyquist |
|-------------|------|-------------------|
| Pidato telepon | 8kHz | 4kHz |
| CD Audio | 44,1 kHz | 22,05kHz |
| Audio profesional | 48kHz | 24kHz |
| Audio resolusi tinggi | 96kHz | 48kHz |
| Video (30fps) | 30 Hz (sementara) | 15Hz |
### Anti-Aliasing
Sebelum pengambilan sampel, **filter anti-aliasing** (low-pass) menghilangkan frekuensi di atas f_s/2 untuk mencegah aliasing.
---

## Jendela
Saat menganalisis segmen sinyal yang terbatas, kita secara implisit mengalikannya dengan jendela persegi panjang, yang menyebabkan kebocoran spektral. **Fungsi jendela** mengurangi kebocoran ini.
### Jendela Umum
| Jendela | Lebar Lobus Utama | Tingkat Lobus Samping | Kasus Penggunaan |
|--------|----------------|-----------------|----------|
| Persegi Panjang | Tersempit | −13 dB | Ketika resolusi paling penting |
| Han | 2× persegi panjang | −31dB | Tujuan umum |
| Hamming | 2× persegi panjang | −41 dB | Mengurangi lobus samping terdekat |
| orang kulit hitam | 3× persegi panjang | −58 dB | Rentang dinamis tinggi |
| Kaiser | Dapat disesuaikan | Dapat disesuaikan (melalui β) | Ketika trade-off dapat diatur |
### Kebocoran Spektral
Mengalikan sinyal dengan jendela akan menggabungkan spektrumnya dengan spektrum jendela. Lobus utama yang lebih lebar mengurangi resolusi frekuensi; lobus sisi bawah mengurangi kebocoran.
---

## Gelombang kecil
**Wavelet** adalah fungsi kecil seperti gelombang terlokalisasi yang digunakan untuk analisis sinyal multi-resolusi.
### Transformasi Gelombang
Berbeda dengan transformasi Fourier (yang memberikan informasi frekuensi global), transformasi wavelet memberikan lokalisasi **frekuensi waktu**.
| Transformasi | Resolusi Waktu | Resolusi Frekuensi |
|-----------|----------------|---------------------|
| Fourier | Tidak ada (global) | Luar biasa |
| FT Waktu Singkat | Memperbaiki (ukuran jendela) | Memperbaiki |
| gelombang kecil | Variabel (bagus pada frekuensi tinggi) | Variabel (bagus pada frekuensi rendah) |
### Keluarga Wavelet Umum
| Keluarga | Properti | Aplikasi |
|--------|-----------|-------------|
| **Haar** | Paling sederhana, terputus-putus | Deteksi tepi, analisis cepat |
| **Daubechies** (dbN) | Dukungan kompak, N momen hilang | Kompresi, mencela |
| **Symlet** | Daubechies yang hampir simetris | Mengurangi distorsi fase |
| **Koiflet** | Dirancang untuk kondisi momen | Pemrosesan sinyal |
| **Morlet** | Sinusoid berjendela Gaussian | Analisis frekuensi waktu |
| **Topi Meksiko** | Turunan kedua dari Gaussian | Deteksi fitur |
### Penerapan Wavelet
| Aplikasi | Bagaimana Wavelet Membantu |
|-------------|-------------------|
| Kompresi gambar (JPEG 2000) | Representasi multi-resolusi, lebih baik dari DCT untuk edge |
| Mencela | Ambang batas koefisien wavelet kecil (sinyal dalam koefisien besar) |
| Deteksi fitur | Deteksi tepi, deteksi sementara dalam deret waktu |
| Analisis EKG | Mendeteksi Kompleks QRS, Klasifikasi Aritmia |
| Analisis seismik | Identifikasi Lapisan Geologi, Pengolahan Sinyal Gempa |
---

## Relevansi dengan Pembelajaran Mesin dan Ilmu Data
| Konsep Pemrosesan Sinyal | Aplikasi |
|-----------|-------------|
| Transformasi Fourier | Fitur spektral untuk audio ML, analisis domain frekuensi deret waktu |
| FFT | Konvolusi cepat di CNN (konvolusi spektral), korelasi efisien |
| Teorema konvolusi | Memahami cara kerja CNN (itu adalah filter yang dipelajari) |
| Filter | Pra-pemrosesan (penghalusan, denoising), ekstraksi fitur |
| Teorema pengambilan sampel | Memahami diskritisasi, memilih laju sensor, menghindari aliasing |
| Jendela | STFT untuk audio ML (spektogram), analisis frekuensi waktu |
| Gelombang kecil | Ekstraksi fitur untuk deret waktu, kompresi, denoising |
| Laplace/Z-transformasi | Teori kendali untuk robotika, memahami stabilitas sistem |
| Analisis spektral | Analisis EEG/fMRI, pemantauan getaran, pemeliharaan prediktif |
| Tingkat Nyquist | Memilih kecepatan pengumpulan data yang sesuai untuk pipeline ML |
---

## Ringkasan
| Alat | Domain | Wawasan Utama |
|------|--------|-------------|
| Transformasi Fourier | Waktu → Frekuensi | Sinyal adalah jumlah sinusoid |
| Transformasi Laplace | Waktu → Frekuensi kompleks | Menangani transien dan stabilitas |
| Z-Transformasi | Waktu diskrit → Kompleks | Analisis dan desain filter digital |
| FFT | Perhitungan DFT yang efisien | O(N log N) bukannya O(N²) |
| Filter | Pemilihan frekuensi | Berikan apa yang Anda perlukan, blokir apa yang tidak Anda butuhkan |
| Teorema Pengambilan Sampel | Kontinu ↔ diskrit | Sampel cukup cepat, tidak ada ruginya |
| Jendela | Pertukaran frekuensi waktu | Resolusi keseimbangan dan kebocoran |
| Gelombang kecil | Analisis multi-resolusi | Lokal baik waktu maupun frekuensi |
Pemrosesan sinyal memberikan landasan matematika untuk memahami, menganalisis, dan memanipulasi data. Setiap pipeline pembelajaran mesin yang bekerja dengan deret waktu, audio, gambar, atau data sensor secara implisit menggunakan konsep pemrosesan sinyal. Transformasi Fourier, khususnya, bisa dibilang merupakan alat matematika terpenting setelah kalkulus bagi ilmuwan data mana pun.