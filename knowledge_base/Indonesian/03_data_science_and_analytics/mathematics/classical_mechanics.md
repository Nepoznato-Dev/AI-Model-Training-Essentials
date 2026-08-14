---
# Metadata
title: "Classical Mechanics"
description: "Newton's laws, free-body diagrams, work-energy theorem, conservation laws, Lagrangian mechanics, Hamiltonian mechanics, rigid body dynamics, and orbital mechanics"
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
    changes: "Initial deep-dive into classical mechanics"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2027-02-10"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-10"

# Classification
tags: [classical-mechanics, newton, lagrangian, hamiltonian, conservation-laws, orbital-mechanics, rigid-body]
difficulty_level: "intermediate"
prerequisites:
  - "mathematics.md"
  - "real_analysis.md"
estimated_reading_time: "25 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# Mekanika Klasik
Mekanika klasik menggambarkan gerak benda di bawah pengaruh gaya. Dari apel yang jatuh hingga planet yang mengorbit, dari string yang bergetar hingga partikel yang bertabrakan, prinsip-prinsipnya mengatur dunia makroskopis. Di luar penerapan fisiknya, mekanika klasik melahirkan kalkulus variasi, geometri simplektis, dan kerangka Hamilton yang mendasari mekanika kuantum dan optimasi modern.
---

## Mekanika Newton
### Tiga Hukum Newton
| Hukum | Pernyataan | Bentuk Matematika |
|-----|-----------|-------------------|
| **Pertama (Inersia)** | Suatu benda akan tetap diam atau bergerak beraturan kecuali jika ada gaya | Jika F_net = 0, maka v = konstanta |
| **Kedua (F = ma)** | Gaya sama dengan massa dikali percepatan | **F** = m**a** = m(d²**x**/dt²) |
| **Ketiga (Aksi-Reaksi)** | Setiap aksi mempunyai reaksi yang sama besar dan berlawanan arah | **F**₁₂ = −**F**₂₁ |
### Diagram Benda Bebas
**Diagram benda bebas** mengisolasi suatu benda dan menunjukkan semua gaya yang bekerja padanya.
**Kekuatan bersama:**
| Memaksa | Rumus | Arah |
|-------|---------|-----------|
| Gravitasi (dekat Bumi) | F = mg | Ke bawah |
| Kekuatan biasa | tidak | Tegak lurus terhadap permukaan |
| Gesekan (statis) | f_s ≤ μ_s N | Menentang gerakan yang akan datang |
| Gesekan (kinetik) | f_k = μ_k N | Menentang gerak |
| Pegas (hukum Hooke) | F = −kx | Memulihkan (menuju keseimbangan) |
| Ketegangan | T | Sepanjang tali/tali |
| Seret | F_d = ½C_d ρAv² | Menentang kecepatan |
### Contoh yang Berhasil: Blokir pada Kemiringan
Sebuah balok bermassa m pada bidang miring tanpa gesekan dengan sudut θ.
- Gaya: gravitasi (mg ke bawah), gaya normal (N tegak lurus permukaan)
- Penguraian gravitasi: mg sin θ (sepanjang tanjakan), mg cos θ (ke permukaan)
- N = mg cos θ (tidak ada gerak tegak lurus permukaan)
- Percepatan di tanjakan: a = g sin θ
---

## Metode Energi
### Usaha dan Energi Kinetik
**Usaha** yang dilakukan oleh suatu gaya: W = ∫ **F** · d**r**
**Teorema Usaha-Energi:** W_net = ΔKE = ½mv₂² − ½mv₁²
### Energi Potensial
| Memaksa | Energi Potensial | Catatan |
|-------|-----------------|-------|
| Gravitasi (dekat permukaan) | kamu = mgh | h = tinggi di atas referensi |
| Gravitasi (umum) | kamu = −GMm/r | Nol di tak terhingga |
| Musim semi | kamu = kx² | x = perpindahan dari kesetimbangan |
| Elektrostatis | U = kq₁q₂/r | Muatan sejenis: positif U |
### Konservasi Energi
Jika hanya gaya konservatif yang bekerja: E = KE + PE = konstan
½mv₁² + U₁ = ½mv₂² + U₂
**Contoh Pekerjaan:** Sebuah bola dijatuhkan dari ketinggian h.
- Awal : KE = 0, PE = mgh
- Sesaat sebelum menyentuh tanah: KE = ½mv², PE = 0
- Konservasi: mgh = ½mv² → v = √(2gh)
### Kekuatan
P = dW/dt = **F** · **v** (kecepatan melakukan usaha)
---

## Momentum dan Tabrakan
### Momentum Linier
**p** = m**v**
Hukum kedua Newton (bentuk alternatif): **F** = d**p**/dt
### Konservasi Momentum
Jika tidak ada gaya luar: momentum total kekal.
| Jenis Tabrakan | KE Dikonservasi? | Momentumnya Dilestarikan? |
|---------------|---------------|---------------------|
| **Elastis** | Ya | Ya |
| **Inelastis** | Tidak | Ya |
| **Inelastis sempurna** | Tidak (kerugian maksimum) | Ya (benda saling menempel) |
**Tumbukan elastik 1D:** Dua massa m₁, m₂ dengan kecepatan awal u₁, u₂:
- v₁ = ((m₁−m₂)u₁ + 2m₂u₂) / (m₁+m₂)
- v₂ = ((m₂−m₁)u₂ + 2m₁u₁) / (m₁+m₂)
### Momentum Sudut
**L** = **r** × **p** = m(**r** × **v**)
Torsi: **τ** = d**L**/dt = **r** × **F**
**Kekekalan:** Jika tidak ada torsi eksternal, momentum sudut kekal.
---

## Mekanika Lagrangian
Formulasi **Lagrangian** menggantikan gaya dengan energi, memberikan kerangka kerja yang lebih elegan dan umum.
### Orang Lagrangian
L = T − V (energi kinetik dikurangi energi potensial)
### Prinsip Tindakan Terkecil (Prinsip Hamilton)
Jalur sebenarnya yang diambil oleh sistem antara waktu t₁ dan t₂ meminimalkan (lebih tepatnya, membuat stasioner) **aksi**:
S = ∫_{t₁}^{t₂} L(q, q̇, t) dt
### Persamaan Euler-Lagrange
Kondisi δS = 0 menghasilkan:
d/dt(∂L/∂q̇) − ∂L/∂q = 0
untuk setiap koordinat umum q.
**Contoh Pengerjaan:** Bandul sederhana (panjang l, massa m, sudut θ dari vertikal).
- T = ½ml²θ̇²
- V = −mgl cos θ
- L = ½ml²θ̇² + mgl cos θ
- ∂L/∂θ = −mgl dosa θ
- ∂L/∂θ̇ = ml²θ̇ → d/dt(∂L/∂θ̇) = ml²θ̈
- Euler-Lagrange: ml²θ̈ + mgl sin θ = 0 → θ̈ + (g/l) sin θ = 0
### Keuntungan Mekanika Lagrangian
| Keuntungan | Penjelasan |
|-----------|-------------|
| Koordinat-independen | Bekerja di sistem koordinat apa pun |
| Menangani kendala secara alami | Tidak perlu menghitung kekuatan kendala |
| Simetri → konservasi | Teorema Noether menghubungkan kesimetrian dengan besaran kekal |
| Generalisasi dengan mudah | Untuk bidang, relativitas, mekanika kuantum |
---

## Mekanika Hamilton
Formulasi **Hamiltonian** merupakan reformulasi mekanika Lagrangian yang menggunakan posisi dan momentum (bukan posisi dan kecepatan).
### Orang Hamilton
H = Σᵢ pᵢq̇ᵢ − L = T + V (untuk sebagian besar sistem mekanis)
dimana pᵢ = ∂L/∂q̇ᵢ adalah **momen umum**.
### Persamaan Hamilton
q̇ᵢ = ∂H/∂pᵢ
ṗᵢ = −∂H/∂qᵢ
Ini adalah 2n ODE orde pertama (vs n persamaan Euler-Lagrange orde kedua).
**Contoh Pengerjaan:** Osilator harmonik (massa m, konstanta pegas k).
- T = p²/(2m) + ½kx²
- ẋ = ∂H/∂p = p/m → p = mẋ (seperti yang diharapkan)
- ṗ = −∂H/∂x = −kx → mẍ = −kx (Hukum Hooke)
### Kurung Poisson
Untuk fungsi f(q, p) dan g(q, p):
{f, g} = Σᵢ (∂f/∂qᵢ · ∂g/∂pᵢ − ∂f/∂pᵢ · ∂g/∂qᵢ)
| Properti | Pernyataan |
|----------|-----------|
| Evolusi waktu | df/dt = {f, H} + ∂f/∂t |
| Konservasi | f kekal jika {f, H} = 0 (dan ∂f/∂t = 0) |
| Tanda kurung dasar | {qᵢ, pⱼ} = δᵢⱼ, {qᵢ, qⱼ} = 0, {pᵢ, pⱼ} = 0 |
**Hubungan dengan mekanika kuantum:** Tanda kurung Poisson menjadi komutator: {f, g} → (1/iℏ)[f̂, ĝ]
---

## Hukum Konservasi dan Teorema Noether
### Teorema Noether
Setiap simetri Lagrangian yang berkesinambungan berhubungan dengan kuantitas yang kekal.
| Simetri | Kuantitas yang Dikonservasi |
|----------|-------------------|
| Invariansi terjemahan waktu | Energi |
| Invariansi terjemahan spasial | Momentum linier |
| Invariansi rotasi | Momentum sudut |
| Invariansi pengukur | Muatan listrik |
Ini adalah salah satu hasil terdalam dalam seluruh ilmu fisika - ini menghubungkan geometri ruangwaktu dengan hukum kekekalan dasar.
---

## Dinamika Tubuh Kaku
**benda tegar** adalah benda yang semua jarak internalnya tetap.
### Konsep Utama
| Konsep | Rumus | Deskripsi |
|---------|---------|-------------|
| **Momen inersia** | Saya = Σmᵢrᵢ² atau Saya = ∫r² dm | Ketahanan terhadap percepatan rotasi |
| **Ke Rotasi** | KE = ½Iω² | Energi rotasi |
| **Momentum sudut** | L = Sayaω | Analog rotasi p = mv |
| **Torsi** | τ = Sayaα | Analog rotasi F = ma |
### Momen Inersia (Bentuk Umum)
| Bentuk | Sumbu | saya |
|-------|------|---|
| Bola padat | Melalui pusat | (2/5)MR² |
| Bola berongga | Melalui pusat | (2/3)MR² |
| Silinder padat | Sepanjang sumbu | (1/2)MR² |
| Batang tipis | Melalui pusat, tegak lurus | (1/12)ML² |
| Batang tipis | Melalui ujung, tegak lurus | (1/3)ML² |
| Disk | Melalui pusat, tegak lurus | (1/2)MR² |
---

## Mekanika Orbital
### Hukum Kepler
| Hukum | Pernyataan |
|-----|-----------|
| **Pertama (Ellipsis)** | Planet-planet bergerak berbentuk elips dengan Matahari pada satu fokus |
| **Kedua (Area yang sama)** | Garis dari Matahari ke planet menyapu luas yang sama dalam waktu yang sama |
| **Ketiga (Harmonik)** | T² ∝ a³ (periode dikuadratkan sebanding dengan sumbu semi mayor pangkat tiga) |
### Energi Orbital
E = ½mv² − GMm/r
| E | Jenis Orbit |
|---|-----------|
| E< 0 | Elliptical (bound) |
| E = 0 | Parabolic (escape trajectory) |
| E >0 | Hiperbolik (tidak terikat) |
### Kecepatan Melarikan Diri
v_escape = √(2GM/Kanan)
Untuk Bumi: v_escape ≈ 11,2 km/s
---

## Relevansi dengan Pembelajaran Mesin dan Ilmu Data
| Konsep Mekanika | Aplikasi |
|------------------|-------------|
| Hukum Newton | Mesin fisika dalam simulasi, game AI, robotika |
| Metode energi | Model berbasis energi, jaringan Hopfield, mesin Boltzmann |
| Mekanika Lagrangian | Jaringan saraf berbasis fisika, kontrol optimal, optimalisasi lintasan |
| Mekanika Hamilton | Jaringan saraf Hamiltonian (HNN), integrator simplektis untuk simulasi |
| Hukum Konservasi | Bias induktif dalam model ML, jaringan saraf ekuivalen |
| Teorema Noether | Pembelajaran mesin sadar simetri, pembelajaran mendalam geometris |
| Dinamika bodi kaku | Simulasi robotika, dinamika molekuler, animasi 3D |
| Mekanika orbital | Penentuan posisi satelit (GPS untuk ML berbasis lokasi), desain misi luar angkasa |
| Ruang fase (Hamiltonian) | Memahami sistem dinamis, jaringan penarik |
| Kalkulus variasi | Transportasi optimal, pemodelan generatif (pencocokan aliran) |
---

## Ringkasan
| Kerangka | Persamaan Inti | Kekuatan |
|-----------|--------------|----------|
| Newton | **F** = m**a** | Analisis gaya langsung yang intuitif |
| Lagrangian | d/dt(∂L/∂q̇) − ∂L/∂q = 0 | Bebas koordinat, menangani kendala |
| Hamiltonian | q̇ = ∂H/∂p, ṗ = −∂H/∂q | Struktur sederhana, terhubung ke QM |
| Hukum Konservasi | Teorema Noether | Koneksi konservasi simetri yang mendalam |
Mekanika klasik bukan hanya tentang bola jatuh dan ayunan pendulum. Kerangka matematikanya – mekanika Lagrangian dan Hamiltonian – adalah salah satu gagasan paling berpengaruh dalam semua sains. Mereka menggeneralisasi mekanika kuantum, teori medan, dan bahkan pembelajaran mesin modern, di mana model berbasis energi dan jaringan saraf berbasis fisika memanfaatkan langsung formulasi yang telah berusia berabad-abad ini.