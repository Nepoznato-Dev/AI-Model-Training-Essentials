---
# Metadata
title: "Quantum Mechanics"
description: "Wave-particle duality, Schrodinger equation, operators and observables, uncertainty principle, quantum states and superposition, entanglement, qubits, quantum gates, and relevance to quantum computing"
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
    changes: "Initial deep-dive into quantum mechanics"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2027-02-10"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-10"

# Classification
tags: [quantum-mechanics, schrodinger-equation, uncertainty-principle, superposition, entanglement, qubits, quantum-gates, quantum-computing]
difficulty_level: "advanced"
prerequisites:
  - "mathematics.md"
  - "abstract_algebra.md"
  - "classical_mechanics.md"
estimated_reading_time: "28 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Mekanika Kuantum
Mekanika kuantum adalah teori fisika pada skala terkecil — atom, elektron, foton, dan partikel dasar alam. Ini menggantikan dunia deterministik mekanika klasik dengan probabilitas, superposisi, dan keterjeratan. Meskipun sifatnya berlawanan dengan intuisi, mekanika kuantum adalah teori yang paling tepat diuji di seluruh ilmu pengetahuan. Saat ini, prinsip-prinsipnya menjadi relevan secara langsung dengan komputasi melalui komputer kuantum, yang menjanjikan penyelesaian masalah tertentu secara eksponensial lebih cepat daripada mesin klasik.
---

## Motivasi Sejarah
### Kegagalan Fisika Klasik
| Masalah | Prediksi Klasik | Pengamatan | Resolusi |
|---------|---------------------|-------------|------------|
| Radiasi benda hitam | Bencana ultraviolet (energi tak terbatas disingkat λ) | Panjang gelombang puncak terbatas | Planck: energi terkuantisasi (E = nhν) |
| Efek fotolistrik | KE bergantung pada intensitas, bukan frekuensi | KE bergantung pada frekuensi | Einstein: cahaya terkuantisasi (foton, E = hν) |
| Spektrum atom | Spektrum emisi berkelanjutan | Garis spektral diskrit | Bohr: elektron menempati orbit terkuantisasi |
| Difraksi elektron | Partikel tidak terdifraksi | Elektron menghasilkan pola interferensi | de Broglie: partikel mempunyai panjang gelombang λ = h/p |
### Konstanta Kunci
| Konstan | Simbol | Nilai |
|----------|--------|-------|
| Konstanta Planck | jam | 6,626 × 10⁻³⁴ J·s |
| Mengurangi konstanta Planck | ℏ = h/2π | 1,055 × 10⁻³⁴ J·s |
| Kecepatan cahaya | c | 3,0 × 10⁸ m/s |
| Massa elektron | saya_e | 9,109 × 10⁻³¹kg |
| Muatan dasar | e | 1,602 × 10⁻¹⁹ C |
| Jari-jari Bohr | sebuah₀ | 5,292 × 10⁻¹¹ m |
---

## Dualitas Gelombang-Partikel
### de Broglie Panjang Gelombang
Setiap partikel dengan momentum p memiliki panjang gelombang yang terkait:
λ = h/p = h/(mv)
| Partikel | Khas λ | Perilaku Gelombang yang Dapat Diamati? |
|----------|-----------|---------------------------|
| Elektron (100 eV) | 0,12nm | Ya (difraksi kristal) |
| Proton | 0,003nm | Ya (hamburan neutron) |
| Bisbol (40 m/s) | 10⁻³⁴ m | Tidak (terlalu kecil untuk dideteksi) |
### Eksperimen Celah Ganda
Eksperimen kuantum klasik:
1. Partikel api (elektron, foton) satu per satu pada dua celah
2. Setiap partikel mendarat di satu titik pada detektor
3. Seiring waktu, pola interferensi muncul — seolah-olah setiap partikel melewati kedua celah secara bersamaan
4. Jika Anda mengukur celah mana yang dilalui partikel, pola interferensi akan hilang
**Kesimpulan:** Objek kuantum bukanlah partikel murni dan bukan pula gelombang murni. Mereka menunjukkan perilaku seperti gelombang ketika tidak teramati dan perilaku seperti partikel ketika diukur.
---

## Fungsi Gelombang
### Definisi
**Fungsi gelombang** ψ(x, t) sepenuhnya menggambarkan sistem kuantum. Ini adalah fungsi bernilai kompleks yang modulus kuadratnya memberikan kepadatan probabilitas:
P(x) = |ψ(x)|² = ψ*(x)ψ(x)
### Normalisasi
Probabilitas totalnya harus sama dengan 1:
∫ |ψ(x)|² dx = 1 (di seluruh ruang)
### Lahir Aturan
Peluang menemukan partikel antara x dan x + dx:
P(x sampai x+dx) = |ψ(x)|² dx
Untuk observasi umum dengan status eigen φₙ:
P(mengukur nilai eigen aₙ) = |⟨φₙ|ψ⟩|²
---

## Persamaan Schrodinger
### Persamaan Schrodinger Bergantung Waktu
iℏ ∂ψ/∂t = Ĥψ
dimana Ĥ adalah **operator Hamiltonian** (operator energi total).
### Persamaan Schrodinger Bebas Waktu
Untuk keadaan stasioner (keadaan eigen energi):
Ĥψ = Eψ
Ini adalah persamaan nilai eigen: energi yang diperbolehkan E adalah nilai eigen dari Ĥ.
### Partikel dalam Kotak (Sumur Kotak Tak Terbatas)
Sistem kuantum paling sederhana: partikel terbatas pada 0 < x < L.
| Kuantitas | Hasil |
|----------|--------|
| Fungsi gelombang | ψₙ(x) = √(2/L) sin(nπx/L) |
| Tingkat energi | Eₙ = n²π²ℏ²/(2mL²) = n²h²/(8mL²) |
| Keadaan dasar | n = 1, E₁ = h²/(8mL²) |
| Energi titik nol | E₁ > 0 (partikel tidak bisa diam sempurna) |
| Bilangan kuantum | n = 1, 2, 3, ... (bilangan bulat positif saja) |
### Osilator Harmonik Kuantum
V(x) = ½mω²x²
| Kuantitas | Hasil |
|----------|--------|
| Tingkat energi | Eₙ = (n + ½)ℏω |
| Energi titik nol | E₀ = ½ℏω |
| Spasi | ΔE = ℏω (seragam) |
| Fungsi gelombang | Polinomial pertapa × Gaussian |
---

## Operator dan Observable
Dalam mekanika kuantum, setiap pengamatan fisik berhubungan dengan **operator Hermitian**.
### Operator Kunci
| Dapat Diamati | Operator (ruang posisi) | Nilai eigen |
|-----------|--------------------------|-------------|
| Posisi | x̂ = x | Semua nyata x |
| Momentum | p̂ = −iℏ ∂/∂x | Semua p nyata |
| Energi (Hamiltonian) | Ĥ = −(ℏ²/2m)∂²/∂x² + V(x) | Eₙ (diskrit untuk keadaan terikat) |
| Momentum sudut | L̂ = r × p̂ | ℏ√(l(l+1)) |
| Putar | Ŝ = (ℏ/2)σ (matriks Pauli) | ±ℏ/2 (untuk putaran-½) |
### Nilai Harapan
Rata-rata hasil pengukuran A yang dapat diamati pada keadaan ψ:
⟨A⟩ = ⟨ψ|Â|ψ⟩ = ∫ ψ*(x) Â ψ(x) dx
### Hubungan Pergantian
[Â, B̂] = ÂB̂ − B̂Â
| Komutator | Hasil | Signifikansi |
|-----------|--------|-------------|
| [x̂, p̂] | sayaℏ | Posisi dan momentum tidak sejalan |
| [L̂ₓ, L̂ᵧ] | sayaℏL̂_z | Komponen momentum sudut tidak kompatibel |
| [σ̂ₓ, σ̂ᵧ] | 2iσ̂_z | Matriks Pauli (komponen putaran) |
Jika [Â, B̂] = 0, observasi dapat diukur secara bersamaan (berbagi status eigen).
---

## Prinsip Ketidakpastian
### Prinsip Ketidakpastian Heisenberg
Δx · Δp ≥ ℏ/2
Secara lebih umum, untuk dua observasi A dan B:
ΔA · ΔB ≥ (1/2)|⟨[Â, B̂]⟩|
### Hubungan Ketidakpastian
| Pasangkan | Hubungan | Interpretasi |
|------|----------|----------------|
| Posisi-momentum | ΔxΔp ≥ ℏ/2 | Tidak dapat mengetahui keduanya secara tepat |
| Energi-waktu | ΔEΔt ≥ ℏ/2 | Negara-negara yang berumur pendek memiliki energi yang tidak pasti |
| Momentum sudut | ΔLₓΔLᵧ ≥ (ℏ/2)\|⟨L_z⟩\| | Tidak dapat mengetahui semua komponen secara bersamaan |
**Penting:** Ketidakpastian bukan berarti gangguan pengukuran — melainkan merupakan sifat dasar keadaan kuantum. Suatu partikel tidak mempunyai posisi dan momentum tertentu secara bersamaan.
---

## Keadaan Kuantum dan Superposisi
### Notasi Dirac (Bra-Ket)
| Simbol | Nama | Arti |
|--------|------|---------|
| \|ψ⟩ | Ket | Vektor keadaan (vektor kolom) |
| ⟨ψ\| | BH | Transpos konjugasi (vektor baris) |
| ⟨φ\|ψ⟩ | Produk dalam | Amplitudo untuk ψ dapat ditemukan dalam keadaan φ |
| \|ψ\|² | Norma kuadrat | Probabilitas |
### Prinsip Superposisi
Jika \|ψ₁⟩ dan \|ψ₂⟩ merupakan keadaan kuantum yang valid, maka kombinasi linier apa pun juga valid:
\|ψ⟩ = α\|ψ₁⟩ + β\|ψ₂⟩

dimana |α|² + |β|² = 1 (normalisasi).
**Pengukuran:** Saat diukur, sistem "runtuh" ​​menjadi \|ψ₁⟩ dengan probabilitas |α|² atau \|ψ₂⟩ dengan probabilitas |β|².
### Qubit
**qubit** adalah bit kuantum: sistem kuantum dua tingkat.
\|ψ⟩ = α\|0⟩ + β\|1⟩, dimana |α|² + |β|² = 1
| Representasi | \|0⟩ | \|1⟩ |
|---------------|------|------|
| Putar | Putar ↑ | Putar ke bawah ↓ |
| Polarisasi foton | Horisontal | Vertikal |
| Tingkat energi | Keadaan dasar | Keadaan bersemangat |
| Sirkuit | \|0⟩ = [1, 0]ᵀ | \|1⟩ = [0, 1]ᵀ |
**Bloch Sphere:** Status qubit apa pun dapat ditulis sebagai:
\|ψ⟩ = cos(θ/2)\|0⟩ + e^{iφ} sin(θ/2)\|1⟩
dimana θ ∈ [0, π] dan φ ∈ [0, 2π). Ruang negara berbentuk bola.
---

## Keterikatan
Dua qubit **terjerat** ketika status gabungannya tidak dapat ditulis sebagai produk dari masing-masing status.
### Status Lonceng (Terjerat Maksimal)
| Negara | Ekspresi | Nama |
|-------|-----------|------|
| \|Φ⁺⟩ | (1/√2)(\|00⟩ + \|11⟩) | Negara bel |
| \|Φ⁻⟩ | (1/√2)(\|00⟩ − \|11⟩) | Negara bel |
| \|Ψ⁺⟩ | (1/√2)(\|01⟩ + \|10⟩) | Negara bel |
| \|Ψ⁻⟩ | (1/√2)(\|01⟩ − \|10⟩) | Status singlet |
### Sifat Keterikatan
| Properti | Deskripsi |
|----------|-------------|
| Korelasi | Mengukur satu qubit secara instan menentukan qubit lainnya, berapapun jaraknya |
| Tidak ada komunikasi | Tidak dapat menggunakan keterikatan saja untuk mengirim informasi lebih cepat dari cahaya |
| Monogami | Jika A terjerat maksimal dengan B, maka ia tidak dapat terjerat dengan C |
| Kerapuhan | Interaksi dengan lingkungan menghancurkan keterikatan (dekoherensi) |
### Paradoks EPR dan Teorema Bell
Einstein, Podolsky, dan Rosen berpendapat bahwa mekanika kuantum pasti tidak lengkap (variabel tersembunyi). Bell menunjukkan bahwa teori variabel tersembunyi lokal dapat memenuhi kesenjangan tertentu. Eksperimen melanggar ketidaksetaraan Bell - membenarkan mekanika kuantum dan mengesampingkan variabel lokal yang tersembunyi.
---

## Gerbang Kuantum
Gerbang kuantum adalah operasi kesatuan pada qubit.
### Gerbang Qubit Tunggal
| Gerbang | Matriks | Efek |
|------|--------|--------|
| **Pauli-X** (TIDAK) | [[0,1],[1,0]] | Balik sedikit: \|0⟩ ↔ \|1⟩ |
| **Pauli-Y** | [[0,−i],[i,0]] | Bit + pembalikan fase |
| **Pauli-Z** | [[1,0],[0,−1]] | Pembalikan fase: \|1⟩ → −\|1⟩ |
| **Hadamard** (H) | (1/√2)[[1,1],[1,−1]] | Membuat superposisi: \|0⟩ → (\|0⟩+\|1⟩)/√2 |
| **Fase** (S) | [[1,0],[0,i]] | rotasi π/2 di sekitar Z |
| **Gerbang T** | [[1,0],[0,e^{iπ/4}]] | rotasi π/4 di sekitar Z |
| **Rotasi** Rₓ(θ) | cos(θ/2)Saya − saya dosa(θ/2)σₓ | Rotasi sebesar θ di sekitar sumbu X |
### Gerbang Dua Qubit
| Gerbang | Deskripsi | Efek |
|------|-------------|--------|
| **COT** | Terkendali-TIDAK | Membalik target jika kontrolnya \|1⟩ |
| **CZ** | Terkendali-Z | Menerapkan Z ke target jika kontrolnya adalah \|1⟩ |
| **TUKAR** | Pertukaran qubit | \|ab⟩ → \|ba⟩ |
### Menciptakan Keterikatan
Terapkan H ke qubit 1, lalu CNOT dengan qubit 1 sebagai kontrol:
\|00⟩ → (H⊗I)\|00⟩ → CNOT → (1/√2)(\|00⟩ + \|11⟩) = \|Φ⁺⟩
---

## Algoritma Kuantum
| Algoritma | Mempercepat | Aplikasi |
|-----------|---------|-------------|
| **Shor** | Eksponensial (pemfaktoran) | Merusak enkripsi RSA |
| **Grover** | Kuadrat (pencarian) | Pencarian tidak terstruktur di O(√N) |
| **VQE** | Heuristik | Menemukan energi keadaan dasar (kimia, material) |
| **QAOA** | Heuristik | Optimasi kombinatorial |
| **HHL** | Eksponensial (dalam kondisi) | Memecahkan sistem linier |
| **Simulasi kuantum** | Eksponensial | Mensimulasikan sistem kuantum (motivasi asli Feynman) |
---

## Relevansi dengan Pembelajaran Mesin dan Ilmu Data
| Konsep Kuantum | Aplikasi |
|----------------|-------------|
| Qubit dan superposisi | Pembelajaran mesin kuantum, pengambilan sampel yang ditingkatkan kuantum |
| Keterikatan | Komunikasi kuantum, distribusi kunci kuantum (QKD) |
| Gerbang kuantum | Desain sirkuit kuantum untuk subrutin ML |
| Algoritma Grover | Percepatan kuadrat untuk optimasi berbasis pencarian |
| Algoritma Shor | Ancaman terhadap kriptografi saat ini; memotivasi kripto pasca-kuantum |
| Simulasi kuantum | Penemuan obat, ilmu material, simulasi kimia |
| Algoritma variasi (VQE, QAOA) | ML kuantum jangka pendek pada perangkat NISQ |
| Aturan lahir | Hasil probabilistik dianalogikan dengan pengambilan sampel dari distribusi |
| Produk sensor | Sistem multi-qubit (ruang keadaan eksponensial — matematika yang sama dengan aljabar multilinier di ML) |
| Matriks kesatuan | Analog kuantum transformasi ortogonal |
---

## Ringkasan
| Konsep | Ide Inti | Persamaan Kunci |
|---------|-----------|-------------|
| Dualitas gelombang-partikel | Materi mempunyai sifat gelombang | λ = jam/p |
| Fungsi gelombang | Deskripsi lengkap keadaan kuantum | P(x) = \|ψ(x)\|² |
| Persamaan Schrodinger | Bagaimana keadaan kuantum berevolusi | iℏ ∂ψ/∂t = Ĥψ |
| Operator | Yang dapat diamati adalah operator Hermitian | ⟨A⟩ = ⟨ψ\|Â\|ψ⟩ |
| Ketidakpastian | Batasan mendasar pada pengetahuan simultan | ΔxΔp ≥ ℏ/2 |
| Superposisi | Negara dapat ditambahkan | \|ψ⟩ = α\|0⟩ + β\|1⟩ |
| Keterikatan | Negara-negara gabungan yang tidak dapat dipisahkan | \|Φ⁺⟩ = (\|00⟩ + \|11⟩)/√2 |
| Gerbang kuantum | Operasi kesatuan pada qubit | H, CNOT, dan set gerbang universal |
Mekanika kuantum menantang intuisi terdalam kita tentang realitas - partikel yang berupa gelombang, benda di dua tempat sekaligus, korelasi yang tidak dapat dijelaskan secara klasik. Namun matematikanya tepat dan akurasi prediksinya tidak tertandingi. Bagi ilmuwan data, mekanika kuantum menjadi relevan secara langsung melalui komputasi kuantum, yang menjanjikan transformasi optimasi, kriptografi, simulasi, dan potensi pembelajaran mesin itu sendiri.