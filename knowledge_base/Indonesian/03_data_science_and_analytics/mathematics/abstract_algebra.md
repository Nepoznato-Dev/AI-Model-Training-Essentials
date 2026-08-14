<!--
---
# Metadata
title: "Abstract Algebra"
description: "Groups, subgroups, homomorphisms, rings, fields, vector spaces, linear maps, eigen theory, and applications in coding theory and quantum computing"
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
    changes: "Initial deep-dive into abstract algebra"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2027-02-10"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-10"

# Classification
tags: [abstract-algebra, groups, rings, fields, vector-spaces, linear-maps, eigen-theory, coding-theory, quantum-computing]
difficulty_level: "advanced"
prerequisites:
  - "mathematics.md"
  - "discrete_mathematics.md"
estimated_reading_time: "28 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Aljabar Abstrak
Aljabar abstrak mempelajari struktur aljabar — himpunan yang dilengkapi dengan operasi yang mengikuti aturan tertentu. Daripada bekerja dengan angka, aljabar abstrak bekerja dengan objek apa pun yang memenuhi aksioma. Sifat umum ini sangat kuat: teorema yang terbukti untuk "grup" berlaku pada bilangan bulat, simetri, matriks, permutasi, dan keadaan kuantum secara bersamaan. Aljabar abstrak mendasari kriptografi, kode koreksi kesalahan, komputasi kuantum, dan analisis simetri yang digunakan dalam fisika.
---

## Grup
**Grup** adalah struktur aljabar paling mendasar. Ini menangkap esensi simetri.
### Definisi
**Grup** (G, ∗) adalah himpunan G dengan operasi biner ∗ yang memuaskan:
| Aksioma | Pernyataan | Contoh (ℤ, +) |
|-------|-----------|-----------------|
| **Penutupan** | ∀a,b ∈ G: a ∗ b ∈ G | a + b adalah bilangan bulat |
| **Asosiasi** | (a ∗ b) ∗ c = a ∗ (b ∗ c) | (a + b) + c = a + (b + c) |
| **Identitas** | ∃e ∈ G: e ∗ a = a ∗ e = a | 0 + a = a + 0 = a |
| **Terbalik** | ∀a ∈ G, ∃a⁻¹: a ∗ a⁻¹ = a⁻¹ ∗ a = e | a + (−a) = 0 |
Jika operasinya juga **komutatif** (a ∗ b = b ∗ a), grup tersebut disebut **abelian**.
### Contoh Grup
| Grup | Tetapkan | Operasi | Identitas | Terbalik | Abelian? |
|-------|-----|-----------|----------|---------|----------|
| (ℤ, +) | Bilangan bulat | Tambahan | 0 | −sebuah | Ya |
| (ℚ*, ×) | Rasional bukan nol | Perkalian | 1 | 1/a | Ya |
| (ℤ/nℤ, +) | Residu mod n | Mod tambahan n | [0] | [n−a] | Ya |
| Sₙ | Permutasi dari {1,...,n} | Komposisi | identitas | Permutasi terbalik | Tidak (n ≥ 3) |
| GL(n, ℝ) | Matriks n×n yang dapat dibalik | Perkalian matriks | sayaₙ | A⁻¹ | Tidak (n ≥ 2) |
| (ℝⁿ, +) | vektor berdimensi n | Penambahan vektor | 0 | −v | Ya |
### Urutan Grup dan Elemen
| Istilah | Definisi | Contoh |
|------|------------|---------|
| **Urutan G** (\|G\|) | Jumlah elemen di G | \|ℤ/5ℤ\| = 5 |
| **Urutan elemen a** (ord(a)) | K positif terkecil dengan aᵏ = e | ord(2) in (ℤ/7ℤ)* = 3 (karena 2³ = 8 ≡ 1) |
| **Grup terbatas** | \|G\| terbatas | S₃ mempunyai orde 6 |
| **Grup tak terbatas** | \|G\| tidak terbatas | (ℤ, +) |
### Subgrup
**subgrup** H dari G adalah himpunan bagian H ⊆ G yang merupakan grup dalam operasi yang sama.
**Tes subgrup:** H adalah subgrup dari G iff:
1. H tidak kosong
2. Untuk semua a, b ∈ H: a ∗ b⁻¹ ∈ H
**Contoh:**
- (ℤ, +) mempunyai subgrup nℤ = {..., −2n, −n, 0, n, 2n, ...} untuk setiap n ≥ 0
- **Subgrup sepele** {e} dan grup G itu sendiri selalu merupakan subgrup
- Pada S₃, himpunan {id, (12)} merupakan subgrup berorde 2
### Koset dan Teorema Lagrange
Untuk subgrup H dari G dan elemen a ∈ G:
- **Koset kiri:** aH = {ah : h ∈ H}
- **Coset kanan:** Ha = {ha : h ∈ H}
**Teorema Lagrange:** Untuk grup berhingga G dan subgrup H:
|H| membagi |G|
**Akibatnya:**
- Urutan setiap elemen terbagi |G|
- Jika |G| = p (prima), maka G bersifat siklik (tidak mempunyai subgrup non-trivial)
- a^|G| = e untuk semua a ∈ G (menggeneralisasikan Teorema Kecil Fermat)
### Grup Siklik
Suatu golongan G disebut **siklik** jika terdapat g ∈ G sehingga setiap elemen dari G pangkat g. Kita menulis G = ⟨g⟩.
| Properti | Pernyataan |
|----------|-----------|
| Setiap grup siklik adalah abelian | — |
| ℤ/nℤ di bawah penjumlahan adalah siklik | Dihasilkan oleh [1] |
| (ℤ/pℤ)* adalah siklik untuk bilangan prima p | Generator disebut root primitif |
| Klasifikasi | Setiap grup siklik berhingga bersifat isomorfik terhadap ℤ/nℤ untuk beberapa n |
---

## Homomorfisme dan Isomorfisme
**homomorfisme** adalah peta yang mempertahankan struktur antarkelompok.
### Definisi
| Istilah | Definisi | Contoh |
|------|------------|---------|
| **Homomorfisme** | φ: G → H dimana φ(ab) = φ(a)φ(b) | yaitu: GL(n,ℝ) → ℝ* |
| **Isomorfisme** | Homomorfisme bijektif (grupnya "sama") | (ℤ/6ℤ) ≅ (ℤ/2ℤ) × (ℤ/3ℤ) |
| **Kernel** | ker(φ) = {g ∈ G : φ(g) = e_H} | ker(det) = SL(n, ℝ) |
| **Gambar** | im(φ) = {φ(g) : g ∈ G} | im(det) = ℝ* |
### Teorema Isomorfisme Pertama
Jika φ: G → H adalah homomorfisme, maka:
G / ker(φ) ≅ im(φ)
Ini adalah salah satu teorema paling penting dalam aljabar - yang menyatakan bahwa setiap homomorfisme didekomposisi menjadi hasil bagi yang diikuti oleh isomorfisme.
---

## Dering
**Ring** menambahkan operasi kedua ke grup, memodelkan aritmatika dengan penjumlahan dan perkalian.
### Definisi
**ring** (R, +, ×) adalah himpunan R dengan dua operasi yang memuaskan:
| Aksioma | Pernyataan |
|-------|-----------|
| (R, +) merupakan grup abelian | Penjumlahan bersifat komutatif, asosiatif, beridentitas 0, setiap elemen mempunyai invers penjumlahan |
| Perkalian bersifat asosiatif | (a × b) × c = a × (b × c) |
| Hukum distributif | a(b + c) = ab + ac dan (a + b)c = ac + bc |
Jika perkalian juga bersifat komutatif dan mempunyai identitas (1), R adalah **ringing komutatif dengan kesatuan**.
### Contoh Cincin
| Dering | Deskripsi | Komutatif? | Memiliki 1? |
|------|-------------|-------------|--------|
| (ℤ, +, ×) | Bilangan bulat | Ya | Ya |
| (ℚ, +, ×) | Rasional | Ya | Ya |
| (ℝ, +, ×) | Bilangan nyata | Ya | Ya |
| (ℤ/nℤ, +, ×) | Mod bilangan bulat n | Ya | Ya |
| Mₙ(ℝ) | n×n matriks nyata | Tidak (n ≥ 2) | Ya |
| ℝ[x] | Polinomial dengan koefisien real | Ya | Ya |
### Cita-cita dan Cincin Kecerdasan
I **ideal** dari ring R adalah himpunan bagian yang:
1. Merupakan subgrup di bawah penjumlahan
2. Menyerap perkalian: untuk semua r ∈ R dan a ∈ I, baik ra ∈ I maupun ar ∈ I
**Ring hasil bagi** R/I: elemen adalah koset dari I, dengan operasi yang diwarisi dari R.
**Contoh:** ℤ/nℤ = ℤ/nℤ adalah hasil bagi ℤ dengan nℤ ideal.
### Domain dan Bidang Integral
| Struktur | Definisi | Contoh |
|-----------|------------|----------|
| **Domain integral** | Ring komutatif dengan 1, tanpa pembagi nol (ab = 0 → a = 0 atau b = 0) | ℤ, ℚ[x], ℝ[x] |
| **Bidang** | Ring komutatif dimana setiap elemen bukan nol mempunyai invers perkalian | ℚ, ℝ, ℂ, ℤ/pℤ (p prima) |
---

## Bidang
Bidang adalah objek aljabar paling terstruktur yang umum digunakan. Setiap unsur yang bukan nol dapat dijumlahkan, dikurangi, dikalikan, dan dibagi.
### Properti Utama
| Properti | Pernyataan |
|----------|-----------|
| Setiap bidang merupakan domain integral | — |
| Setiap domain integral hingga adalah bidang | — |
| Karakteristik | N terkecil dengan n·1 = 0, atau 0 jika tidak ada n tersebut |
| arang(ℚ) = arang(ℝ) = arang(ℂ) | = 0 |
| arang(ℤ/pℤ) | = p (untuk p prima) |
### Bidang Terbatas (Lapangan Galois)
Untuk setiap pangkat prima pᵏ, terdapat bidang berhingga unik (hingga isomorfisme) dengan orde pᵏ, yang dilambangkan dengan GF(pᵏ) atau 𝔽_{pᵏ}.
| Bidang | Ukuran | Konstruksi | Aplikasi |
|-------|------|-------------|-------------|
| GF(2) | 2 | {0, 1} mod 2 | Aritmatika biner, XOR |
| GF(2ᵏ) | 2ᵏ | Polinomial mod poli yang tidak dapat direduksi pada GF(2) | Enkripsi AES, kode CRC |
| GF(p) | hal | ℤ/pℤ untuk bilangan prima p | Aritmatika modular, teori pengkodean |
| GF(pᵏ) | pᵏ | Bidang ekstensi | Kode Reed-Solomon, kurva elips |
**Konstruksi GF(2⁸)** (digunakan dalam AES):
- Mulai dengan GF(2) = {0, 1}
- Pilih polinomial tak tereduksi p(x) = x⁸ + x⁴ + x³ + x + 1 pada GF(2)
- Elemen adalah polinomial berderajat < 8 dengan koefisien dalam GF(2)
- Aritmatika: penjumlahan polinomial (XOR) dan mod perkalian p(x)
---

## Ruang Vektor
**Ruang vektor** adalah sekumpulan vektor yang dapat dijumlahkan dan diskalakan, sehingga menjadi dasar aljabar linier.
### Definisi
**ruang vektor** V pada bidang F adalah himpunan dengan:
- Penjumlahan vektor: V × V → V (menjadikan V grup abelian)
- Perkalian skalar: F × V → V
Memuaskan: asosiatif, komutatifitas penjumlahan, distributifitas perkalian skalar, dan 1·v = v.
### Konsep Utama
| Konsep | Definisi | Contoh |
|---------|------------|---------|
| **Dasar** | Himpunan rentang bebas linier | {e₁, e₂, ..., eₙ} untuk Fⁿ |
| **Dimensi** | Jumlah vektor dalam basis apa pun | redup(ℝ³) = 3 |
| **Subruang** | Subset ditutup pada penjumlahan dan perkalian skalar | Sebuah bidang yang melalui titik asal di ℝ³ |
| **Kombinasi linier** | Σ cᵢvᵢ dimana cᵢ ∈ F | 3v₁ + 2v₂ − v₃ |
| **Rentang** | Himpunan semua kombinasi linier | Span({v₁, v₂}) = bidang jika v₁, v₂ bebas |
| **Independensi linier** | Tidak ada vektor yang merupakan kombinasi linier dari vektor lainnya | e₁, e₂, e₃ dalam ℝ³ |
### Ruang Vektor Penting
| Ruang | Deskripsi | Dimensi |
|-------|-------------|-----------|
| Fⁿ | n-tupel di atas bidang F | n |
| Pₙ(P) | Polinomial derajat ≤ n | n + 1 |
| Mₘₓₙ(P) | m × n matriks pada F | mn |
| C[a,b] | Fungsi kontinu pada [a,b] | Tak Terbatas |
| L²(ℝ) | Fungsi yang dapat diintegralkan persegi | Tak Terbatas (Ruang Hilbert) |
---

## Peta Linier dan Teori Eigen
### Peta Linier
A **peta linier** (transformasi linier) T: V → W memenuhi:
- T(u + v) = T(u) + T(v)
- T(cv) = cT(v) untuk semua skalar c
| Konsep | Definisi | Contoh |
|---------|------------|---------|
| **Kernel** | {v ∈ V : T(v) = 0} | Ruang kosong suatu matriks |
| **Gambar** | {T(v) : v ∈ V} | Ruang kolom suatu matriks |
| **Teorema Peringkat-Nulitas** | redup(ker T) + redup(im T) = redup(V) | Kendala mendasar |
| **Representasi matriks** | T(v) = Av untuk beberapa matriks A | Setiap peta linier antara ruang berdimensi hingga |
### Nilai Eigen dan Vektor Eigen
Untuk peta linier T: V → V (atau matriks A):
**Persamaan nilai eigen:** Av = λv, dengan v ≠ 0
| Istilah | Definisi |
|------|------------|
| **Nilai eigen** λ | Skalar sedemikian sehingga Av = λv untuk beberapa v ≠ 0 |
| **Vektor eigen** v | Vektor bukan nol yang memuaskan Av = λv |
| **Polinomial karakteristik** | det(A − λI) = 0 |
| **Ruang Eigen** | {v : Av = λv} — himpunan semua vektor eigen untuk λ (ditambah 0) |
| **Spektrum** | Himpunan semua nilai eigen |
### Menghitung Nilai Eigen
Untuk matriks 2×2 A = [[a, b], [c, d]]:
- Polinomial karakteristik: λ² − (a+d)λ + (ad−bc) = 0
- λ = ((a+d) ± √((a+d)² − 4(ad−bc))) / 2
**Properti utama:**
- Jumlah nilai eigen = jejak(A) = jumlah elemen diagonal
- Hasil kali nilai eigen = det(A)
### Diagonalisasi
Matriks A **dapat didiagonalisasikan** jika matriks tersebut mempunyai n vektor eigen bebas linier (dengan A adalah n×n).
Jika A = PDP⁻¹ dengan D diagonal:
- Aᵏ = PDᵏP⁻¹ (eksponen matriks cepat)
- D berisi nilai eigen pada diagonal
- P berisi vektor eigen sebagai kolom
**Teorema Spektral:** Setiap matriks simetris nyata dapat didiagonalisasi oleh matriks ortogonal. Nilai eigennya adalah nyata.
---

## Aplikasi
### Teori Pengkodean (Kode Pengoreksi Kesalahan)
Bidang terbatas adalah dasar dari kode koreksi kesalahan modern.
| Kode | Bidang | Memperbaiki | Aplikasi |
|------|-------|----------|-------------|
| Kode Hamming | GF(2) | 1 kesalahan per blok | RAM ECC, jaringan awal |
| Reed-Salomo | GF(2ᵏ) | Banyak kesalahan | CD, DVD, kode QR, komunikasi satelit |
| Kode BCH | GF(2ᵏ) | Banyak kesalahan | Memori flash, satelit |
| Kode LDPC | GF(2) | Banyak kesalahan | Wi-Fi (802.11n), DVB-S2, 5G |
**Pengkodean Reed-Solomon:** Perlakukan data sebagai polinomial di atas GF(2ᵏ), evaluasi pada beberapa titik. Bahkan jika beberapa evaluasi rusak, polinomial aslinya dapat dipulihkan.
### Komputasi Kuantum
Keadaan kuantum berada dalam ruang vektor kompleks (ruang Hilbert). Gerbang kuantum adalah matriks kesatuan.
| Konsep Kuantum | Struktur Aljabar |
|----------------|-------------------|
| Qubit | Vektor satuan dalam ℂ² (ruang vektor 2D kompleks) |
| Gerbang kuantum | Matriks kesatuan U ∈ U(2ⁿ) |
| Pengukuran | Operator proyeksi |
| Keterikatan | Status produk tensor yang tidak dapat dipisahkan |
| Teorema tanpa kloning | Tidak ada peta linier yang dapat menyalin keadaan kuantum yang tidak diketahui |
**Gerbang qubit tunggal:**
| Gerbang | Matriks | Efek |
|------|--------|--------|
| Pauli-X (TIDAK) | [[0,1],[1,0]] | Sedikit membalik |
| Pauli-Z | [[1,0],[0,−1]] | Pembalikan fase |
| Hadamard | (1/√2)[[1,1],[1,−1]] | Menciptakan superposisi |
| CNOT | Gerbang terkendali 4×4 | Melibatkan dua qubit |
### Kriptografi
| Aplikasi | Aljabar yang Digunakan |
|-------------|-------------|
| RSA | Grup perkalian (ℤ/nℤ)* |
| Kriptografi kurva elips | Sekelompok titik pada kurva elips pada bidang berhingga |
| AES | Aritmatika dalam GF(2⁸) |
| Diffie-Hellman | Subgrup siklik dari (ℤ/pℤ)* atau grup kurva elips |
---

## Relevansi dengan Pembelajaran Mesin dan Ilmu Data
| Konsep Aljabar | Aplikasi |
|----------------|-------------|
| Ruang vektor | Ruang fitur, ruang penyematan, pembelajaran representasi |
| Peta linier | Lapisan jaringan saraf (y = Wx + b), reduksi dimensi |
| Nilai eigen/vektor | PCA, pengelompokan spektral, PageRank, analisis stabilitas |
| Dekomposisi matriks | SVD, dekomposisi eigend untuk kompresi model |
| Bidang terbatas | Kode koreksi kesalahan untuk penyimpanan/transmisi data yang andal |
| Teori grup | Simetri dalam fisika (hukum kekekalan), augmentasi data (rotasi, refleksi) |
| Produk sensor | Pembelajaran multi-modal, komputasi kuantum, mekanisme perhatian |
| Cincin dan polinomial | Metode kernel, peta fitur polinomial |
---

## Ringkasan
| Struktur | Operasi | Properti Utama | Contoh |
|-----------|-----------|--------------|---------|
| Grup | Satu (∗) | Penutupan, asosiatif, identitas, invers | (ℤ, +), Sₙ |
| Dering | Dua (+, ×) | Grup abelian di bawah +, monoid di bawah ×, distributif | ℤ, ℤ/nℤ, Mₙ(ℝ) |
| Bidang | Dua (+, ×) | Lingkaran yang elemen bukan nolnya membentuk grup di bawah × | ℚ, ℝ, ℂ, GF(p) |
| Ruang vektor | Skalar multi + penambahan | Modul di atas bidang | ℝⁿ, Pₙ(F), ruang fungsi |
Aljabar abstrak menyediakan bahasa untuk struktur itu sendiri. Grup menangkap simetri, cincin menangkap aritmatika, bidang menangkap pembagian, dan ruang vektor menangkap linearitas. Struktur ini tidak bersifat abstrak — mereka muncul dalam setiap kode koreksi kesalahan yang melindungi data Anda, setiap protokol kriptografi yang mengamankan komunikasi Anda, setiap algoritme kuantum yang suatu hari nanti dapat mengubah komputasi, dan setiap transformasi linier yang berjalan melalui jaringan saraf.