<!--
---
# Metadata
title: "Electromagnetism"
description: "Electric and magnetic fields, Coulomb's law, Gauss's law, Faraday's law, Ampere's law, Maxwell's equations, electromagnetic waves, and RLC circuits"
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
    changes: "Initial deep-dive into electromagnetism"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2027-02-10"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-10"

# Classification
tags: [electromagnetism, maxwell-equations, electric-fields, magnetic-fields, electromagnetic-waves, circuits, gauss-law, faraday]
difficulty_level: "advanced"
prerequisites:
  - "mathematics.md"
  - "classical_mechanics.md"
  - "real_analysis.md"
estimated_reading_time: "25 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Elektromagnetisme
Elektromagnetisme adalah studi tentang medan listrik dan magnet serta interaksinya. Disatukan oleh Maxwell pada tahun 1860-an, elektromagnetisme menjelaskan cahaya, listrik, magnet, gelombang radio, dan struktur atom. Ini adalah gaya fundamental pertama yang dipahami sepenuhnya secara matematis, dan persamaannya mengilhami relativitas khusus dan teori medan modern Einstein.
---

## Medan Listrik
### Hukum Coulomb
Gaya antara dua muatan titik q₁ dan q₂ yang dipisahkan oleh jarak r:
**F** = (1/4πε₀) · (q₁q₂/r²) · r̂
| Konstan | Nilai |
|----------|-------|
| ε₀ (permitivitas ruang kosong) | 8,854 × 10⁻¹² F/m |
| 1/4πε₀ (Konstanta Coulomb k) | 8,988 × 10⁹ N·m²/C² |
### Definisi Medan Listrik
**E** = **F**/q (gaya per satuan muatan)
Untuk muatan titik Q: **E** = (1/4πε₀) · (Q/r²) · r̂
### Garis Medan Listrik
| Properti | Aturan |
|----------|------|
| Arah | Arahkan menjauhi muatan positif menuju negatif |
| Kepadatan | Garis yang lebih dekat = medan yang lebih kuat |
| Menyeberang | Garis medan tidak pernah bersilangan |
| Konduktor | Garis bertemu permukaan tegak lurus |
### Potensi Listrik (Tegangan)
V = −∫ **E** · d**l** (beda potensial adalah integral garis negatif dari E)
**E** = −∇V (medan adalah gradien potensial negatif)
Untuk muatan titik: V = (1/4πε₀) · Q/r
| Konsep | Rumus | Satuan |
|---------|---------|------|
| Energi Potensial | kamu = qV | Joule |
| Elektron-volt | 1 eV = 1,602 × 10⁻¹⁹ J | Satuan energi |
| Permukaan ekuipotensial | Permukaan dimana V konstan | E tegak lurus terhadapnya |
---

## Hukum Gauss
### Penyataan
Total fluks listrik yang melalui suatu permukaan tertutup sama dengan muatan tertutup dibagi dengan ε₀:
∮ **E** · d**A** = Q_enc / ε₀
Dalam bentuk diferensial: ∇ · **E** = ρ/ε₀
### Menggunakan Hukum Gauss
Hukum Gauss paling berguna ketika simetri memungkinkan E dikeluarkan dari integral.
| Simetri | Permukaan Gaussian | Hasil |
|----------|-----------------|--------|
| Bulat | Bola | E = Q/(4πε₀r²) di luar |
| Silinder (muatan saluran) | Silinder | E = λ/(2πε₀r) |
| Planar (lembar tak terbatas) | Kotak obat | E = σ/(2ε₀) |
| Antar pelat sejajar | Kotak obat | E = σ/ε₀ |
---

## Konduktor dan Kapasitor
### Konduktor dalam Kesetimbangan Elektrostatis
| Properti | Penjelasan |
|----------|-------------|
| E = 0 di dalam | Biaya diatur ulang untuk membatalkan bidang internal |
| Semua muatan di permukaan | Tidak ada biaya bersih di interior |
| E tegak lurus pada permukaan | Tidak ada komponen tangensial (jika tidak, muatan akan berpindah) |
| Ekipotensial sepanjang | V yang sama di mana pun di dalam dan di permukaan |
### Kapasitor
**Kapasitor** menyimpan energi dalam medan listrik di antara dua konduktor.
| Konfigurasi | Kapasitansi |
|--------------|-------------|
| Pelat paralel | C = ε₀A/d |
| Silinder | C = 2πε₀L / ln(b/a) |
| Bulat | C = 4πε₀ab / (b−a) |
| Rumus | Ekspresi |
|---------|------------|
| Tegangan pengisian | Q = CV |
| Energi tersimpan | U = ½CV² = ½Q²/C |
| Kepadatan energi | kamu = ½ε₀E² |
| Kombinasi seri | 1/C_total = 1/C₁ + 1/C₂ + ... |
| Kombinasi paralel | C_total = C₁ + C₂ + ... |
### Dielektrik
Memasukkan dielektrik (bahan isolasi) dengan konstanta κ meningkatkan kapasitansi: C = κC₀.
---

## Medan Magnet
### Gaya Magnetik
**F** = q(**v** × **B**) (gaya Lorentz, komponen magnet)
| Properti | Pernyataan |
|----------|-----------|
| Arah | Tegak lurus terhadap v dan B (aturan tangan kanan) |
| Pekerjaan selesai | Nol (gaya tegak lurus kecepatan) |
| Gerak melingkar | Radius r = mv/(qB) pada bidang seragam B |
### Hukum Biot-Savart
Medan magnet akibat elemen berarus kecil:
d**B** = (μ₀/4π) · I(d**l** × r̂) / r²
| Konstan | Nilai |
|----------|-------|
| μ₀ (permeabilitas ruang kosong) | 4π × 10⁻⁷ T·m/A |
### Hukum Ampere
∮ **B** · d**l** = μ₀I_enc
Dalam bentuk diferensial: ∇ × **B** = μ₀**J**
**Aplikasi:**
| Konfigurasi | bidang B |
|--------------|---------|
| Kawat lurus panjang | B = μ₀I/(2πr) |
| Solenoid (di dalam) | B = μ₀nI |
| Toroid (di dalam) | B = μ₀NI/(2πr) |
---

## Induksi Elektromagnetik
### Hukum Faraday
Fluks magnet yang berubah menginduksi gaya gerak listrik (EMF):
EMF = −dΦ_B/dt
dimana Φ_B = ∫ **B** · d**A** adalah fluks magnet.
Dalam bentuk diferensial: ∇ × **E** = −∂**B**/∂t
**Hukum Lenz:** EMF induksi melawan perubahan fluks (tanda minus).
### Aplikasi Induksi
| Aplikasi | Prinsip |
|-------------|-----------|
| Pembangkit | Kumparan berputar di bidang B → EMF bergantian |
| Transformator | Mengubah arus di primer → EMF di sekunder |
| Induktor | Menentang perubahan arus: EMF = −L(dI/dt) |
| Arus Eddy | Arus induksi pada konduktor curah (pengereman, pemanasan) |
### Induktor
| Rumus | Ekspresi |
|---------|------------|
| Hubungan fluks | Φ = LI |
| Energi tersimpan | kamu = ½LI² |
| Kombinasi seri | L_total = L₁ + L₂ + ... |
| Kombinasi paralel | 1/L_total = 1/L₁ + 1/L₂ + ... |
---

## Persamaan Maxwell
Persamaan Maxwell menyatukan listrik dan magnet menjadi satu teori.
### Dalam Bentuk Integral
| Persamaan | Nama | Pernyataan |
|----------|------|-----------|
| ∮ **E** · d**A** = Q/ε₀ | Hukum Gauss (listrik) | Fluks listrik = muatan tertutup |
| ∮ **B** · d**A** = 0 | Hukum Gauss (magnetik) | Tidak ada monopole magnet |
| ∮ **E** · d**l** = −dΦ_B/dt | Hukum Faraday | Mengubah B menginduksi E |
| ∮ **B** · d**l** = μ₀I + μ₀ε₀ dΦ_E/dt | Hukum Ampere-Maxwell | Arus dan perubahan E menghasilkan B |
### Dalam Bentuk Diferensial
| Persamaan | Nama | Ekspresi |
|----------|------|------------|
| Gauss (listrik) | ∇ · **E** = ρ/ε₀ |
| Gauss (magnetik) | ∇ · **B** = 0 |
| Faraday | ∇ × **E** = −∂**B**/∂t |
| Ampere-Maxwell | ∇ × **B** = μ₀**J** + μ₀ε₀ ∂**E**/∂t |
### Arus Perpindahan
Penambahan kunci Maxwell: istilah μ₀ε₀ ∂**E**/∂t (arus perpindahan). Hal ini memastikan konservasi muatan dan memprediksi gelombang elektromagnetik.
---

## Gelombang Elektromagnetik
Dalam ruang hampa (tanpa muatan, tanpa arus), persamaan Maxwell menghasilkan persamaan gelombang:
∇²**E** = μ₀ε₀ ∂²**E**/∂t²
∇²**B** = μ₀ε₀ ∂²**B**/∂t²
**Kecepatan cahaya:** c = 1/√(μ₀ε₀) ≈ 3 × 10⁸ m/s
### Sifat Gelombang EM
| Properti | Deskripsi |
|----------|-------------|
| Melintang | E dan B saling tegak lurus dan terhadap arah rambat |
| Dalam fase | E dan B mencapai maksimum secara bersamaan |
| Rasio besaran | E = cB |
| Fluks energi | S = (1/μ₀)**E** × **B** (vektor Poynting) |
| Intensitas | Saya = ⟨S⟩ = E₀²/(2μ₀c) |
### Spektrum Elektromagnetik
| Ketik | Panjang gelombang | Frekuensi | Sumber |
|------|-----------|-----------|--------|
| Radio | > 1 m | < 300 MHz | Antennas |
| Microwave | 1 mm − 1 m | 300 MHz − 300 GHz | Magnetrons, klystrons |
| Infrared | 700 nm − 1 mm | 300 GHz − 430 THz | Thermal radiation |
| Visible | 400 − 700 nm | 430 − 750 THz | Atomic transitions |
| Ultraviolet | 10 − 400 nm | 750 THz − 30 PHz | Hot objects, stars |
| X-ray | 0.01 − 10 nm | 30 PHz − 30 EHz | Electron deceleration |
| Gamma ray | < 0.01 nm | >30 EHz | Proses nuklir |
---

## Sirkuit AC
### Komponen Sirkuit RLC
| Komponen | Hubungan Tegangan-Arus | Impedansi |
|-----------|------------------------|-----------|
| Resistor (R) | V = IR | Z_R = R |
| Induktor (Kiri) | V = L(dI/dt) | Z_L = jωL |
| Kapasitor (C) | Saya = C(dV/dt) | Z_C = 1/(jωC) |
### Impedansi dan Resonansi
Impedansi total (seri RLC): Z = R + j(ωL − 1/ωC)
|ω| = √(R² + (ωL − 1/ωC)²)
**Resonansi:** Ketika ωL = 1/ωC → ω₀ = 1/√(LC)
- Pada resonansi: impedansi minimum (= R), arus maksimum
- **Faktor kualitas:** Q = ω₀L/R (ketajaman resonansi)
### Daya pada Rangkaian AC
| Kuantitas | Rumus |
|----------|---------|
| Kekuatan rata-rata | P_avg = V_rms · I_rms · cos φ |
| Faktor daya | karena φ = R/\|Z\| |
| Tegangan RMS | V_rms = V₀/√2 |
---

## Relevansi dengan Pembelajaran Mesin dan Ilmu Data
| Konsep EM | Aplikasi |
|-----------|-------------|
| Persamaan Maxwell | Jaringan saraf berbasis fisika, elektromagnetik komputasi |
| Persamaan gelombang | Landasan pemrosesan sinyal, motivasi analisis Fourier |
| Spektrum elektromagnetik | Data sensor (kamera inframerah, radar, citra satelit) |
| Rangkaian/impedansi AC | Memahami perangkat keras yang menjalankan ML (catu daya, integritas sinyal) |
| vektor penunjuk | Aliran energi dalam komunikasi nirkabel (relevan dengan IoT/edge ML) |
| Hukum Gauss | Analog dengan divergensi dalam kalkulus vektor, digunakan dalam simulasi dinamika fluida |
| Kapasitor/induktor | Komputasi analog untuk jaringan saraf, perangkat keras neuromorfik |
| Resonansi | Desain filter, analisis domain frekuensi, metode spektral |
| Masalah nilai batas | Metode elemen hingga, simulasi berbasis mesh |
| Kalkulus vektor (∇·, ∇×) | Alat matematika penting yang digunakan di seluruh teori ML |
---

## Ringkasan
| Hukum | Apa yang Dikatakan | Bentuk Diferensial |
|-----|-------------|-------------------|
| Gauss (listrik) | Muatan menimbulkan divergensi medan listrik | ∇ · E = ρ/ε₀ |
| Gauss (magnetik) | Tidak ada monopole magnet | ∇ · B = 0 |
| Faraday | Mengubah B menghasilkan pengeritingan E | ∇ × E = −∂B/∂t |
| Ampere-Maxwell | Arus dan perubahan E membuat pengeritingan B | ∇ × B = μ₀J + μ₀ε₀∂E/∂t |
Elektromagnetisme adalah teori fisika paling lengkap dan teruji yang pernah dibuat. Persamaannya – hanya empat – menggambarkan segalanya mulai dari listrik statis hingga cahaya hingga perilaku setiap perangkat elektronik yang pernah dibuat. Bagi ilmuwan data, pemahaman elektromagnetisme memberikan intuisi mendalam tentang fenomena gelombang, kalkulus vektor, dan fisika yang mendasari semua perangkat keras komputasi modern.