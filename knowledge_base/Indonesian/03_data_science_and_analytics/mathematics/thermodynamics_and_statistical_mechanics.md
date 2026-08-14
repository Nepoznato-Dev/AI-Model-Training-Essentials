<!--
---
# Metadata
title: "Thermodynamics and Statistical Mechanics"
description: "Laws of thermodynamics, entropy (thermodynamic and statistical), enthalpy, free energy, Carnot cycle, Boltzmann distribution, partition functions, and connections to information-theoretic entropy"
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
    changes: "Initial deep-dive into thermodynamics and statistical mechanics"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2027-02-10"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-10"

# Classification
tags: [thermodynamics, statistical-mechanics, entropy, enthalpy, free-energy, carnot-cycle, boltzmann, partition-function]
difficulty_level: "advanced"
prerequisites:
  - "mathematics.md"
  - "statistics_and_probability.md"
  - "classical_mechanics.md"
estimated_reading_time: "25 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Termodinamika dan Mekanika Statistik
Termodinamika menggambarkan perilaku makroskopis sistem dalam hal suhu, tekanan, dan entropi — tanpa mengetahui seperti apa bentuk atom. Mekanika statistik menjelaskan termodinamika dari bawah ke atas: ia memperoleh sifat makroskopis dari perilaku mikroskopis sejumlah besar partikel. Bersama-sama, mereka memberikan pemahaman terdalam tentang energi, entropi, dan keseimbangan – konsep yang telah bermigrasi ke teori informasi, pembelajaran mesin, dan seterusnya.
---

## Variabel dan Keadaan Termodinamika
### Variabel Status
| Variabel | Ketik | Satuan | Deskripsi |
|----------|------|------|-------------|
| Suhu (T) | Intensif | Kelvin (K) | Energi kinetik rata-rata per partikel |
| Tekanan (P) | Intensif | Pascal (Pa) | Gaya per satuan luas |
| Jilid (V) | Luas | m³ | Ruang ditempati |
| Energi dalam (U) | Luas | Joule (J) | Energi mikroskopis total |
| Entropi (S) | Luas | J/K | Ukuran gangguan/keadaan mikro |
| Jumlah partikel (N) | Luas | mol atau hitung | Jumlah zat |
Variabel **Intensif** tidak bergantung pada ukuran sistem; variabel **luas** bisa.
### Persamaan Keadaan
Untuk gas ideal: PV = nRT = Nk_BT
| Konstan | Nilai |
|----------|-------|
| R (konstanta gas) | 8,314 J/(mol·K) |
| k_B (Konstanta Boltzmann) | 1,381 × 10⁻²³ J/K |
| N_A (bilangan Avogadro) | 6,022 × 10²³ /mol |
---

## Hukum Termodinamika
### Hukum Nol
Jika A berada dalam kesetimbangan termal dengan B, dan B dengan C, maka A berada dalam kesetimbangan termal dengan C.
**Arti:** Suhu dapat ditentukan dan diukur dengan baik.
### Hukum Pertama (Konservasi Energi)
ΔU = Q − W
| Simbol | Arti |
|--------|---------|
| kamu | Perubahan energi dalam |
| Q | Panas ditambahkan ke sistem |
| W | Usaha yang dilakukan oleh sistem |
**Bentuk Diferensial:** dU = δQ − δW = δQ − PdV
| Proses | Batasan | Konsekuensi |
|---------|-----------|-------------|
| Isokorik | dV = 0 | W = 0, U = Q |
| Isobarik | dP = 0 | W = PΔV |
| Isotermal | dT = 0 | ΔU = 0 (gas ideal), Q = W |
| Adiabatik | δQ = 0 | ΔU = −W |
### Hukum Kedua (Entropi)
**Pernyataan Clausius:** Panas tidak dapat mengalir secara spontan dari dingin ke panas.
**Pernyataan Kelvin-Planck:** Tidak ada mesin yang dapat mengubah seluruh panas menjadi kerja.
**Pernyataan entropi:** Untuk proses apa pun: ΔS_universe ≥ 0
| Jenis proses | ΔS_alam semesta |
|-------------|-------------|
| Reversibel | = 0 |
| Tidak dapat diubah (nyata) | > 0 |
**Perubahan entropi:** dS = δQ_rev / T
### Hukum Ketiga
Ketika T → 0 K, entropi kristal sempurna mendekati nol: lim_{T→0} S = 0
**Arti:** Nol mutlak tidak dapat dicapai dalam langkah-langkah yang terbatas.
---

## Entropi secara Mendalam
### Entropi Termodinamika
S adalah fungsi keadaan. Untuk proses reversibel antara keadaan A dan B:
ΔS = ∫_A^B δQ_rev / T
**Contoh Pekerjaan:** Perubahan entropi saat memanaskan air dari T₁ ke T₂ pada tekanan konstan.
ΔS = ∫_{T₁}^{T₂} (mc_p/T) dT = mc_p ln(T₂/T₁)
### Entropi Statistik (Boltzmann)
S = k_B dalam Ω
dimana Ω adalah jumlah keadaan mikro yang konsisten dengan keadaan makro.
| keadaan makro | Keadaan mikro (Ω) | Entropi |
|-----------|-----------------|---------|
| Semua gas dalam satu setengah kotak | Kecil | Rendah |
| Gas merata | Sangat besar | Tinggi |
| Kristal sempurna pada 0 K | 1 | 0 |
**Koneksi:** Hukum kedua menjadi statistik — sistem berevolusi menuju keadaan makro dengan lebih banyak keadaan mikro hanya karena kemungkinannya jauh lebih besar.
---

## Entalpi dan Energi Bebas
### Entalpi
H = U + PV
Berguna untuk proses pada tekanan konstan (sebagian besar kimia dan biologi).
ΔH = Q_p (panas pada tekanan konstan)
### Energi Bebas Helmholtz
F = U − TS
| Properti | Pernyataan |
|----------|-----------|
| Arti | Usaha maksimum yang dapat diekstraksi pada konstanta T, V |
| Kesetimbangan | Sistem meminimalkan F pada konstanta T, V |
| Kaitannya dengan fungsi partisi | F = −k_BT dalam Z |
### Energi Bebas Gibbs
G = H − TS = U + PV − TS
| Properti | Pernyataan |
|----------|-----------|
| Arti | Usaha non muai maksimum pada konstanta T, P |
| Kesetimbangan | Sistem meminimalkan G pada konstanta T, P |
| Spontanitas | ΔG < 0 → spontan; ΔG = 0 → kesetimbangan |
| Reaksi kimia | ΔG = ΔH − TΔS menentukan arah |
### Ringkasan Potensi Termodinamika
| Potensi | Variabel Alam | Diferensial | Diminimalkan Ketika |
|-----------|-------------------|-------------|----------------|
| U (energi dalam) | S,V | dU = TdS − PdV | Sistem terisolasi |
| H (entalpi) | S, P | dH = TdS + VdP | Konstanta P, adiabatik |
| F (Helmholtz) | T,V | dF = −SdT − PdV | Konstanta T, V |
| G (Gibbs) | T, P | dG = −SdT + VdP | Konstanta T, P |
---

## Siklus Carnot
**Siklus Carnot** adalah mesin kalor yang paling efisien, beroperasi antara temperatur T_H (panas) dan T_C (dingin).
### Empat Tahap
| Tahap | Proses | Apa yang Terjadi |
|-------|---------|-------------|
| 1 → 2 | Ekspansi isotermal | Menyerap kalor Q_H dari reservoir panas di T_H |
| 2 → 3 | Ekspansi adiabatik | Gas mendingin dari T_H ke T_C |
| 3 → 4 | Kompresi isotermal | Tolak kalor Q_C ke reservoir dingin pada T_C |
| 4 → 1 | Kompresi adiabatik | Gas memanas dari T_C ke T_H |
### Efisiensi Carnot
η_Carnot = 1 − T_C/T_H
| T_H | T_C | η_Carnot |
|-----|-----|----------|
| 500K | 300K | 40% |
| 1000K | 300K | 70% |
| 300K | 299K | 0,33% |
**Tidak ada mesin nyata yang dapat melebihi efisiensi Carnot.** Mesin nyata selalu tidak dapat diubah (gesekan, turbulensi, perbedaan suhu terbatas).
---

## Mekanika Statistik
### Distribusi Boltzmann
Untuk sistem dalam kesetimbangan termal pada suhu T, probabilitas berada dalam keadaan mikro dengan energi E_i:
P(E_i) = (1/Z) e^{−E_i / k_BT}
di mana Z adalah **fungsi partisi**:
Z = Σᵢ e^{−E_i / k_BT}
### Fungsi Partisi
Z mengkodekan semua informasi termodinamika tentang sistem.
| Kuantitas | Rumus |
|----------|---------|
| Energi bebas Helmholtz | F = −k_BT dalam Z |
| Energi rata-rata | ⟨E⟩ = −∂(ln Z)/∂β dengan β = 1/(k_BT) |
| Entropi | S = k_B(ln Z + β⟨E⟩) |
| Kapasitas panas | C_V = ∂⟨E⟩/∂T = k_Bβ²(⟨E²⟩ − ⟨E⟩²) |
| Tekanan | P = (1/β) ∂(ln Z)/∂V |
### Contoh yang Berhasil: Sistem Dua Negara
Sebuah partikel dapat berada dalam keadaan 0 (energi 0) atau keadaan 1 (energi ε).
Z = 1 + e^{−βε}
| Kuantitas | Hasil |
|----------|--------|
| P(negara bagian 0) | 1/(1 + e^{−βε}) |
| P(negara bagian 1) | e^{−βε}/(1 + e^{−βε}) |
| ⟨E⟩ | ε/(1 + e^{βε}) |
| Batas T tinggi (β→0) | ⟨E⟩ → ε/2 (probabilitas sama) |
| Batas T rendah (β→∞) | ⟨E⟩ → 0 (keadaan dasar) |
### Teorema Ekipartisi
Setiap derajat kebebasan kuadrat menyumbang ½k_BT terhadap energi rata-rata.
| Sistem | Derajat Kebebasan | ⟨E⟩ |
|--------|-------------------|------|
| Gas monatomik (He) | 3 terjemahan | (3/2)k_BT |
| Gas diatomik (N₂) di ruang T | 3 trans + 2 busuk | (5/2)k_BT |
| Gas diatomik pada T tinggi | 3 trans + 2 busuk + 1 vib | (7/2)k_BT |
| Padat (model Einstein) | 3 getaran (per atom) | 3k_BT |
---

## Kaitannya dengan Teori Informasi
### Entropi Shannon vs Entropi Termodinamika
| Aspek | Entropi Shannon H(X) | Entropi Termodinamika S |
|--------|---------------------|------------------------|
| Definisi | −Σ pᵢ log pᵢ | k_B ln Ω (atau −k_B Σ pᵢ ln pᵢ) |
| Maksimum ketika | Distribusi seragam | Kesetimbangan termal |
| Tindakan | Ketidakpastian/isi informasi | Jumlah negara mikro yang dapat diakses |
| Satuan | Bit atau nat | J/K |
**Rumus entropi Gibbs:** S = −k_B Σᵢ pᵢ ln pᵢ (bentuknya identik dengan entropi Shannon)
### Prinsip Entropi Maksimum
Kedua bidang tersebut menggunakan prinsip yang sama: distribusi yang paling mewakili kondisi pengetahuan kita adalah distribusi yang memaksimalkan entropi dengan batasan yang diketahui.
| Batasan | Distribusi yang Dihasilkan |
|-----------|----------------------|
| Rata-rata yang diketahui | Distribusi eksponensial |
| Mean dan varians yang diketahui | Distribusi Gaussian |
| Energi yang diketahui ⟨E⟩ | Distribusi Boltzmann |
| Tidak ada kendala | Distribusi seragam |
### Prinsip Landauer
Menghapus sedikit informasi akan menghilangkan setidaknya k_BT ln 2 energi sebagai panas. Hal ini menghubungkan pemrosesan informasi secara langsung dengan termodinamika - komputasi memerlukan biaya energi yang mendasar.
---

## Relevansi dengan Pembelajaran Mesin dan Ilmu Data
| Konsep Termo/StatMech | Aplikasi |
|---------|-------------|
| Distribusi Boltzmann | Fungsi Softmax, model berbasis energi, simulasi anil |
| Fungsi partisi | Normalisasi konstanta dalam model probabilistik, sulit dilakukan secara umum |
| Energi bebas | Inferensi variasional (meminimalkan energi bebas variasional = meminimalkan divergensi KL) |
| Entropi | Regularisasi, eksplorasi dalam RL (RL entropi maksimum), pohon keputusan |
| Prinsip entropi maksimum | Pengklasifikasi MaxEnt, seleksi sebelumnya, estimasi distribusi |
| Simulasi anil | Optimalisasi global dengan mengurangi "suhu" secara bertahap |
| Mekanika statistik | Pengertian peralihan fase dalam pembelajaran (grokking, double descending) |
| Ekuipartisi | Memahami Distribusi Energi dalam Simulasi Fisika |
| Prinsip Landauer | Batasan mendasar komputasi, komputasi reversibel |
| Pengambilan sampel Gibbs | Metode MCMC terinspirasi langsung dari mekanika statistik |
| Suhu (dalam softmax) | Mengontrol keacakan prediksi: P(i) ∝ exp(z_i/T) |
---

## Ringkasan
| Hukum/Konsep | Ide Inti | Rumus |
|------------|-----------|---------|
| Hukum nol | Suhu terdefinisi dengan baik | Transitivitas kesetimbangan termal |
| Hukum pertama | Energi dihemat | ΔU = Q − W |
| Hukum Kedua | Entropi alam semesta meningkat | ΔS ≥ 0 |
| Hukum ketiga | Nol mutlak tidak mungkin tercapai | S → 0 sebagai T → 0 |
| Entropi Boltzmann | Entropi menghitung keadaan mikro | S = k_B ln |
| Distribusi Boltzmann | Probabilitas keadaan energi | P ∝ e^{−E/k_BT} |
| Fungsi partisi | Mengkodekan semua informasi termodinamika | Z = Σ e^{−E_i/k_BT} |
| Energi bebas | Pekerjaan yang bermanfaat tersedia | F = U − TS, G = H − TS |
| Efisiensi Carnot | Efisiensi mesin kalor maksimum | η = 1 − T_C/T_H |
Termodinamika dan mekanika statistik adalah tempat pertemuan fisika dengan teori informasi. Entropi yang sama yang mengatur mesin panas juga mengatur kompresi data. Distribusi Boltzmann yang sama yang menggambarkan molekul gas memberi kekuatan pada lapisan softmax di setiap pengklasifikasi. Memahami hubungan ini memberi Anda pandangan terpadu tentang fisika, probabilitas, dan pembelajaran mesin.