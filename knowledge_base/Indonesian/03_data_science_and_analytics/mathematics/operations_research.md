<!--
---
# Metadata
title: "Operations Research"
description: "Linear programming formulations, transportation and assignment problems, network flow optimization, integer programming, dynamic programming, queueing theory, inventory models, and scheduling"
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
    changes: "Initial deep-dive into operations research"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2027-02-10"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-10"

# Classification
tags: [operations-research, linear-programming, transportation-problem, dynamic-programming, queueing-theory, inventory-models, scheduling, network-flow]
difficulty_level: "intermediate"
prerequisites:
  - "mathematics.md"
  - "optimization.md"
  - "graph_theory.md"
estimated_reading_time: "25 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Riset Operasi
Riset operasi (OR) adalah penerapan metode matematika untuk pengambilan keputusan. Lahir pada masa Perang Dunia II untuk logistik militer, perusahaan ini kini mengoptimalkan rantai pasokan, menjadwalkan maskapai penerbangan, mengarahkan armada pengiriman, mengelola inventaris, dan mengalokasikan sumber daya di setiap industri. OR menyediakan perangkat matematika untuk membuat keputusan terbaik dalam batasan.
---

## Formulasi Pemrograman Linier
### Formulir Standar
Minimalkan cᵀx
Tunduk pada: Ax = b, x ≥ 0
### Formulasi LP Umum
**Bauran Produk:**
- Variabel keputusan: xⱼ = jumlah produk j yang akan diproduksi
- Tujuan: memaksimalkan keuntungan Σ pⱼxⱼ
- Kendala: batasan sumber daya Σ aᵢⱼxⱼ ≤ bᵢ
**Masalah Pola Makan:**
- Variabel keputusan: xⱼ = jumlah makanan j yang akan dibeli
- Tujuan: meminimalkan biaya Σ cⱼxⱼ
- Kendala : kebutuhan nutrisi Σ nᵢⱼxⱼ ≥ rᵢ
**Masalah Pencampuran:**
- Variabel keputusan: xⱼ = proporsi bahan j dalam campuran
- Tujuan: meminimalkan biaya
- Kendala: persyaratan kualitas (peringkat oktan, kekuatan, dll.)
### Contoh Pekerjaan: Perencanaan Produksi
Sebuah pabrik membuat produk A dan B.
- A membutuhkan tenaga kerja 2 jam, bahan 1 kg; untung $30
- B membutuhkan tenaga kerja 1 jam, material 3 kg; untung $40
- Tersedia: 40 jam kerja, 30 kg material
**Formulasi:**
- Maksimalkan: 30x_A + 40x_B
- Tunduk pada : 2x_A + x_B ≤ 40 (buruh)
- x_A + 3x_B ≤ 30 (bahan)
- x_A, x_B ≥ 0
**Solusi:** Titik daerah layak: (0,0), (20,0), (18,4), (0,10)
- (0,0): keuntungan = 0
- (20,0) : keuntungan = 600
- (18,4) : keuntungan = 700 ← optimal
- (0,10) : keuntungan = 400
---

## Masalah Transportasi
Memindahkan barang dari m sumber ke n tujuan dengan biaya minimum.
### Formulasi
- Variabel keputusan: xᵢⱼ = jumlah yang dikirim dari sumber i ke tujuan j
- Tujuan: meminimalkan Σᵢ Σⱼ cᵢⱼxᵢⱼ
- Tunduk pada: Σⱼ xᵢⱼ = sᵢ (batasan pasokan)
- Σᵢ xᵢⱼ = dⱼ (batas permintaan)
- xᵢⱼ ≥ 0
### Metode Solusi
| Metode | Deskripsi | Kualitas Solusi Awal |
|--------|-------------|---------------------------|
| **Sudut Barat Laut** | Mulai dari kiri atas, alokasikan dengan rakus | Layak tetapi seringkali buruk |
| **Pendekatan Vogel** | Pertimbangkan biaya penalti | Solusi awal yang lebih baik |
| **MODI / Batu Loncatan** | Tingkatkan solusi awal secara berulang | Menemukan |
### Contoh yang Berhasil
| | D1 | D2 | D3 | Pasokan |
|---|----|----|----|--------|
| S1 | 2 | 3 | 1 | 50 |
| S2 | 4 | 1 | 5 | 30 |
| S3 | 3 | 2 | 4 | 20 |
| Permintaan | 40 | 30 | 30 | 100 |
---

## Masalah Penugasan
Menugaskan n pekerja ke n pekerjaan (satu-ke-satu) untuk meminimalkan total biaya.
### Formulasi
- Variabel keputusan: xᵢⱼ ∈ {0, 1} (1 jika pekerja i ditugaskan pada pekerjaan j)
- Minimalkan: Σᵢ Σⱼ cᵢⱼxᵢⱼ
- Tunduk pada: Σⱼ xᵢⱼ = 1 (setiap pekerja mendapat satu pekerjaan)
- Σᵢ xᵢⱼ = 1 (setiap pekerjaan mendapat satu pekerja)
### Algoritma Hongaria
| Properti | Nilai |
|----------|-------|
| Kompleksitas waktu | HAI(n³) |
| Optimal? | Ya |
| Pendekatan | Pengurangan matriks + penutup minimum |
**Langkah-langkah:**
1. Kurangi jumlah minimum baris dari setiap baris
2. Kurangi minimum kolom dari setiap kolom
3. Tutupi semua angka nol dengan jumlah baris minimum
4. Jika garis = n, penugasan optimal ditemukan di antara angka nol
5. Jika tidak, sesuaikan matriks dan ulangi
---

## Optimasi Aliran Jaringan
### Aliran Biaya Minimum
Mengingat jaringan dengan kapasitas dan biaya yang terbatas, temukan aliran yang memenuhi permintaan dengan biaya minimum.
**Formulasi:**
- Minimalkan: Σ cᵢⱼxᵢⱼ
- Tunduk pada: konservasi aliran pada setiap node
- Batasan kapasitas: 0 ≤ xᵢⱼ ≤ uᵢⱼ
### Jalur Terpendek sebagai Aliran Jaringan
Masalah jalur terpendek merupakan kasus khusus aliran biaya minimum (kirim 1 unit dari s ke t).
### Aplikasi
| Aplikasi | Model Jaringan |
|-------------|--------------|
| Rantai pasokan | Node = gudang, edge = rute pengiriman |
| Komunikasi | Node = router, edge = link dengan bandwidth |
| Lalu Lintas | Node = persimpangan, tepi = jalan dengan kapasitas |
| Manajemen proyek | Jaringan BPS/PERT |
---

## Pemrograman Dinamis
**Pemrograman dinamis (DP)** memecahkan masalah kompleks dengan memecahnya menjadi submasalah yang tumpang tindih.
### Prinsip Optimalitas Bellman
Kebijakan yang optimal mempunyai sifat bahwa apa pun keadaan awal dan keputusannya, keputusan-keputusan selanjutnya harus merupakan kebijakan yang optimal untuk keadaan yang dihasilkan.
### Elemen Kunci
| Elemen | Deskripsi |
|---------|-------------|
| **Panggung** | Titik keputusan (langkah waktu, indeks item) |
| **Negara** | Informasi yang dibutuhkan untuk mengambil keputusan |
| **Keputusan** | Pilihan dibuat pada setiap tahap |
| **Pengulangan** | Nilai optimal pada tahap n dalam hal tahap n−1 |
### Masalah DP Klasik
| Masalah | Kekambuhan | Kompleksitas |
|---------|-----------|------------|
| **Fibonacci** | F(n) = F(n−1) + F(n−2) | O(n) dengan memoisasi |
| **Ransel** | V(i,w) = maks(V(i−1,w), vᵢ + V(i−1,w−wᵢ)) | HAI(nW) |
| **Jalur terpendek** | d(i) = min_j(d(j) + cⱼᵢ) | O(V²) atau O(E log V) |
| **Edit jarak** | D(i,j) = min(D(i−1,j)+1, D(i,j−1)+1, D(i−1,j−1)+biaya) | HAI(mn) |
| **Urutan umum terpanjang** | L(i,j) = L(i−1,j−1)+1 jika cocok, jika tidak max(L(i−1,j), L(i,j−1)) | HAI(mn) |
| **Perkalian rantai matriks** | M(i,j) = min_k(M(i,k) + M(k+1,j) + pᵢ₋₁pₖpⱼ) | HAI(n³) |
### Contoh Berhasil: 0/1 Knapsack
Item: {berat: nilai} = {(2, 12), (3, 10), (4, 8), (5, 11)}. Kapasitas W = 7.
V(i, w) = nilai maksimal menggunakan i item pertama dengan kapasitas w
| saya\w | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|-----|---|---|---|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 1 | 0 | 0 | 12 | 12 | 12 | 12 | 12 | 12 |
| 2 | 0 | 0 | 12 | 12 | 12 | 22 | 22 | 22 |
| 3 | 0 | 0 | 12 | 12 | 12 | 22 | 22 | 22 |
| 4 | 0 | 0 | 12 | 12 | 12 | 22 | 23 | 23 |
Optimal: V(4, 7) = 23 (item 1 dan 4: berat 2+5=7, nilai 12+11=23).
---

## Teori Antrian
Teori antrian mempelajari antrean tunggu — berapa lama antrean tersebut, berapa lama Anda menunggu, dan bagaimana mengurangi keduanya.
### Notasi Kendall
A/B/c/K/N/D dimana:
- A = proses kedatangan (M = Markovian/Poisson, D = deterministik, G = umum)
- B = proses pelayanan (pilihan yang sama)
- c = jumlah server
- K = kapasitas (default ∞)
- N = populasi (default ∞)
- D = disiplin (FIFO, LIFO, Prioritas)
### Antrian M/M/1 (Server Tunggal)
| Metrik | Rumus |
|--------|---------|
| Pemanfaatan | ρ = λ/μ |
| Jumlah rata-rata dalam sistem | L = ρ/(1−ρ) |
| Waktu rata-rata dalam sistem | W = 1/(μ−λ) |
| Jumlah rata-rata dalam antrian | L_q = ρ²/(1−ρ) |
| Waktu tunggu rata-rata | W_q = ρ/(μ−λ) |
dimana λ = tingkat kedatangan, μ = tingkat pelayanan, ρ = pemanfaatan.
### Antrean M/M/c (Beberapa Server)
| Metrik | Rumus |
|--------|---------|
| Pemanfaatan | ρ = λ/(cμ) |
| Probabilitas menunggu (Erlang C) | P_w = rumus kompleks yang melibatkan ρ dan c |
| Rata-rata panjang antrian | L_q = P_w · ρ/(1−ρ) |
### Hukum Kecil
L = λW (angka rata-rata dalam sistem = tingkat kedatangan × waktu rata-rata)
Hal ini berlaku untuk sistem antrian APAPUN, terlepas dari distribusi kedatangan/layanan.
### Contoh Aplikasi
| Skenario | Model Antrian |
|----------|-------------|
| Pusat panggilan | M/M/c (agen c) |
| Permintaan server web | M/M/1 atau M/G/1 |
| Darurat rumah sakit | M/G/c dengan prioritas |
| Jalur manufaktur | Jaringan antrian |
| Penjadwalan CPU Komputer | Berbagi prosesor M/M/1 |
---

## Model Inventaris
### Kuantitas Pesanan Ekonomis (EOQ)
Kuantitas pesanan optimal yang meminimalkan total biaya persediaan.
Q* = √(2DS/JAM)
| Variabel | Arti |
|----------|---------|
| D | Permintaan tahunan |
| S | Biaya pemesanan per pesanan |
| H | Biaya penyimpanan per unit per tahun |
| T* | Kuantitas pesanan optimal |
**Total biaya di Q*:** TC = √(2DSH)
### Ekstensi
| Model | Ekstensi |
|-------|-----------|
| **EOQ dengan diskon** | Diskon kuantitas mengubah fungsi biaya |
| **Jumlah pesanan produksi** | Barang diproduksi bertahap, tidak dikirim sekaligus |
| **(s, Q) model** | Susun ulang unit Q ketika persediaan turun ke level s |
| **(s, S) model** | Pesan hingga S ketika persediaan turun ke s |
| **Model penjual koran** | Permintaan satu periode dan tidak pasti |
### Model Penjual Koran
Kuantitas pesanan optimal untuk inventaris yang mudah rusak dalam satu periode:
P(D ≤ Q*) = c_u / (c_u + c_o)
dimana c_u = biaya di bawah umur (keuntungan hilang) dan c_o = biaya kelebihan (pemborosan).
---

## Penjadwalan
### Penjadwalan Toko Pekerjaan
| Notasi | Arti |
|----------|---------|
| n/m/J/C_max | n pekerjaan, m mesin, job shop, minimalkan Makespan |
| Toko aliran | Semua pekerjaan mengunjungi mesin dalam urutan yang sama |
| Toko pekerjaan | Setiap pekerjaan memiliki urutan mesinnya sendiri |
| Buka toko | Tidak ada batasan pemesanan |
### Aturan Prioritas
| Aturan | Deskripsi | Efek |
|------|-------------|--------|
| FCFS | Pertama datang, pertama dilayani | Cukup, tapi belum optimal |
| SPT | Waktu pemrosesan terpendek dulu | Meminimalkan penyelesaian rata-rata |
| EDD | Tanggal jatuh tempo paling awal dulu | Meminimalkan keterlambatan maksimum |
| CR | Rasio kritis (sisa tanggal jatuh tempo/waktu pemrosesan) | Seimbang |
| LPT | Waktu pemrosesan paling lama dulu | Baik untuk makepan pada mesin paralel |
### Algoritma Johnson (Toko Aliran 2 Mesin)
Untuk n pekerjaan pada 2 mesin, meminimalkan makespan:
1. Temukan pekerjaan dengan waktu pemrosesan terpendek
2. Jika di mesin 1, jadwalkan terlebih dahulu; jika di mesin 2, jadwalkan terakhir
3. Hapus pekerjaan itu dan ulangi
Optimal untuk 2 mesin; NP-hard untuk 3+ mesin.
---

## Relevansi dengan Pembelajaran Mesin dan Ilmu Data
| ATAU Konsep | Aplikasi |
|-----------|-------------|
| Pemrograman linier | Alokasi sumber daya, optimalisasi portofolio, alokasi anggaran iklan |
| Transportasi/penugasan | Logistik, pencocokan perjalanan, penetapan tugas |
| Aliran jaringan | Optimalisasi rantai pasokan, perutean lalu lintas pusat data |
| Pemrograman dinamis | Penyelarasan urutan (bioinformatika), Algoritma Viterbi (HMMs), RL (Persamaan Bellman) |
| Teori antrian | Perencanaan kapasitas server, pemodelan latensi, alokasi sumber daya cloud |
| Model inventaris | Integrasi perkiraan permintaan, ML rantai pasokan |
| Penjadwalan | Orkestrasi pipeline ML, penjadwalan tugas GPU, penjadwalan pencarian hyperparameter |
| Pemrograman bilangan bulat | Pemilihan fitur (biner), pemilihan model, desain jaringan |
---

## Ringkasan
| Topik | Masalah Inti | Metode Kunci |
|-------|-------------|------------|
| Formulasi LP | Optimalkan tujuan linier dengan batasan | Simpleks, titik interior |
| Transportasi | Kirim barang dengan biaya minimum | MODI, batu loncatan |
| Tugas | Cocokkan pekerja dengan pekerjaan | Algoritma Hongaria |
| Aliran Jaringan | Aliran rute melalui jaringan | Algoritma aliran biaya minimum |
| Pemrograman Dinamis | Submasalah yang tumpang tindih | Prinsip Bellman, memoisasi |
| Teori Antrian | Analisis garis tunggu | M/M/1, Hukum Kecil |
| Persediaan | Kapan dan berapa banyak yang harus dipesan | EOQ, penjual koran |
| Penjadwalan | Urutan pekerjaan pada mesin | Aturan prioritas, algoritma Johnson |
Riset operasi mengubah pengambilan keputusan dari seni menjadi sains. Dengan merumuskan masalah dunia nyata secara matematis, OR memberikan solusi yang terbukti optimal (atau hampir optimal) terhadap masalah logistik, penjadwalan, alokasi sumber daya, dan perencanaan yang mempengaruhi setiap industri. Bagi data scientist, metode OR melengkapi pembelajaran mesin: meskipun ML memprediksi, OR menentukan — dan secara bersamaan, keduanya membentuk fondasi sistem keputusan yang cerdas.