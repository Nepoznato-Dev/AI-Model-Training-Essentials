---
# Metadata
title: "Game Theory"
description: "Strategic-form games, Nash equilibrium, dominant strategies, minimax theorem, cooperative games, Shapley value, mechanism design, auction theory, and connections to multi-agent reinforcement learning"
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
    changes: "Initial deep-dive into game theory"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2027-02-10"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-10"

# Classification
tags: [game-theory, nash-equilibrium, minimax, cooperative-games, shapley-value, mechanism-design, auction-theory, multi-agent-rl]
difficulty_level: "intermediate"
prerequisites:
  - "mathematics.md"
  - "optimization.md"
  - "statistics_and_probability.md"
estimated_reading_time: "25 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Teori Permainan
Teori permainan adalah matematika interaksi strategis - situasi di mana hasil Anda tidak hanya bergantung pada pilihan Anda sendiri, namun juga pada pilihan orang lain. Dari perang harga antar perusahaan hingga perlombaan senjata nuklir, dari lelang online hingga biologi evolusi, teori permainan menyediakan alat untuk menganalisis konflik dan kerja sama. Hal ini menjadi semakin relevan dengan pembelajaran mesin melalui pembelajaran penguatan multi-agen, jaringan permusuhan generatif (GAN), dan desain mekanisme untuk platform online.
---

## Permainan Berbentuk Strategis
### Definisi
**Permainan bentuk strategis (bentuk normal)** terdiri dari:
- Sekumpulan pemain N = {1, 2, ..., n}
- Strategi menetapkan S₁, S₂, ..., Sₙ untuk setiap pemain
- Fungsi pembayaran u₁, u₂, ..., uₙ memetakan profil strategi ke bilangan real
### Contoh: Dilema Tahanan
| | Bekerja Sama (C) | Cacat (D) |
|---|---------------|------------|
| **Bekerjasama (C)** | (−1, −1) | (−3, 0) |
| **Cacat (D)** | (0, −3) | (−2, −2) |
| Analisis | Hasil |
|----------|--------|
| Strategi dominan | Cacat (D mendominasi C untuk kedua pemain) |
| Kesetimbangan Nash | (D, D) dengan hasil (−2, −2) |
| Optimal sosial | (C, C) dengan hasil (−1, −1) |
| Dilema | Rasionalitas individu mengarah pada irasionalitas kolektif |
### Lebih Banyak Game Klasik
**Pertempuran Jenis Kelamin:**
| | Opera | Sepak Bola |
|---|-------|----------|
| Opera | (2, 1) | (0, 0) |
| Sepak Bola | (0, 0) | (1, 2) |
Dua keseimbangan Nash: (Opera, Opera) dan (Sepak Bola, Sepak Bola).
**Ayam (Merpati Elang):**
| | Elang | Merpati |
|---|------|------|
| Elang | (−10, −10) | (5, 0) |
| Merpati | (0, 5) | (1, 1) |
Dua keseimbangan Nash: (Elang, Merpati) dan (Merpati, Elang).
---

## Strategi Dominan
| Konsep | Definisi |
|---------|------------|
| **Sangat dominan** | Strategi sᵢ memberikan hasil yang lebih tinggi dibandingkan strategi lainnya, apapun pilihan lawan |
| **Dominan lemah** | Strategi sᵢ memberikan setidaknya hasil yang sama tinggi dengan strategi lainnya, dan jauh lebih tinggi untuk beberapa profil lawan |
| **Strategi yang didominasi** | Sebuah strategi yang tidak pernah memberikan respon terbaik |
**Penghapusan strategi yang didominasi secara berulang:**
1. Hapus semua strategi yang didominasi secara ketat
2. Ulangi sampai tidak ada lagi yang bisa dikeluarkan
3. Jika satu profil strategi tetap ada, maka itu adalah ekuilibrium Nash yang unik
---

## Ekuilibrium Nash
**Ekuilibrium Nash** adalah profil strategi di mana tidak ada pemain yang dapat meningkatkan keuntungannya dengan mengubah strateginya secara sepihak.
### Definisi
(s₁*, s₂*, ..., sₙ*) adalah keseimbangan Nash jika untuk setiap pemain i:
uᵢ(sᵢ*, s₋ᵢ*) ≥ uᵢ(sᵢ, s₋ᵢ*) untuk semua sᵢ ∈ Sᵢ
### Menemukan Ekuilibria Nash (Permainan 2×2)
**Metode respons terbaik:**
1. Untuk setiap kolom, garis bawahi respon terbaik pemain 1
2. Untuk setiap baris, garis bawahi respon terbaik pemain 2
3. Sel yang keduanya digarisbawahi adalah kesetimbangan Nash
### Keberadaan (Teorema Nash)
Setiap permainan berhingga memiliki setidaknya satu ekuilibrium Nash (mungkin dalam strategi campuran).
### Strategi Campuran
**Strategi campuran** adalah distribusi probabilitas atas strategi murni.
| Konsep | Definisi |
|---------|------------|
| Strategi campuran σᵢ | Distribusi probabilitas pada Sᵢ |
| Strategi campuran NE | Tidak ada pemain yang dapat meningkatkan hasil yang diharapkan dengan mengubah campuran mereka |
| Dukungan | Kumpulan strategi murni yang dimainkan dengan probabilitas positif |
**Contoh yang Berhasil: Mencocokkan Uang**
| | Kepala | Ekor |
|---|-------|-------|
| Kepala | (1, −1) | (−1, 1) |
| Ekor | (−1, 1) | (1, −1) |
Tidak ada strategi murni NE. Campuran NE: keduanya memainkan H dan T dengan probabilitas masing-masing ½.
---

## Teorema Minimaks
### Permainan Jumlah Nol
Dalam **zero-sum game**, keuntungan satu pemain sama dengan kerugian pemain lainnya: u₁ + u₂ = 0.
### Teorema Minimax Von Neumann
Untuk setiap permainan zero-sum dua pemain yang terbatas:
max_{σ₁} min_{σ₂} u₁(σ₁, σ₂) = min_{σ₂} max_{σ₁} u₁(σ₁, σ₂)
**maximin** (kasus terburuk terbaik untuk pemain 1) sama dengan **minimax** (kasus terburuk terbaik untuk pemain 2). Nilai umum ini adalah **nilai permainan**.
### Menyelesaikan Permainan Zero-Sum
Untuk permainan zero-sum 2×2 dengan matriks:
| | aku | R |
|---|---|---|
| T | sebuah | b |
| B | c | d |
Strategi campuran optimal pemain 1: mainkan T dengan probabilitas p = (d−c)/((a−b)+(d−c))
Nilai permainan: v = (ad−bc)/((a−b)+(d−c))
---

## Game Berbentuk Ekstensif
Game dengan gerakan berurutan direpresentasikan sebagai **pohon permainan**.
### Konsep Utama
| Konsep | Definisi |
|---------|------------|
| **Pohon permainan** | Pohon yang menunjukkan semua kemungkinan urutan gerakan |
| **Kumpulan informasi** | Kumpulan node yang tidak dapat dibedakan oleh pemain |
| **Informasi sempurna** | Setiap kumpulan informasi adalah satu kesatuan (semua gerakan dapat diamati) |
| **Subgame sempurna NE** | Ekuilibrium Nash di setiap subgame |
| **Induksi mundur** | Selesaikan dari ujung pohon ke belakang |
### Teorema Zermelo
Dalam permainan dua pemain yang terbatas dan memiliki informasi sempurna tanpa peluang: salah satu pemain memiliki strategi kemenangan, atau keduanya dapat memaksakan hasil seri (misalnya catur).
---

## Permainan Kooperatif
Dalam **permainan kooperatif**, pemain dapat membentuk perjanjian dan koalisi yang mengikat.
### Fungsi Karakteristik
Permainan kooperatif ditentukan oleh **fungsi karakteristik** v: 2^N → ℝ, dengan v(S) adalah nilai yang dapat dicapai oleh koalisi S.
| Properti | Definisi |
|----------|------------|
| **Superaditif** | v(S ∪ T) ≥ v(S) + v(T) untuk disjoint S, T |
| **Cembung** | v(S ∪ {i}) − v(S) ≤ v(T ∪ {i}) − v(T) untuk S ⊂ T |
### Inti
**Inti** adalah serangkaian alokasi yang tidak dapat ditingkatkan oleh koalisi apa pun jika memisahkan diri:
Inti = {x ∈ ℝⁿ : Σᵢ∈N xᵢ = v(N), Σᵢ∈S xᵢ ≥ v(S) untuk semua S ⊂ N}
Inti mungkin kosong — dalam hal ini tidak ada alokasi stabil.
### Nilai Shapley
**Nilai Shapley** memberikan alokasi adil yang unik berdasarkan kontribusi marjinal:
φᵢ = Σ_{S ⊂ N\{i}} (|S|!(n−|S|−1)!/n!) · [v(S ∪ {i}) − v(S)]
| Properti | Pernyataan |
|----------|-----------|
| Efisiensi | Σ φᵢ = v(N) (semua nilai terdistribusi) |
| Simetri | Kontributor yang setara mendapat imbalan yang sama |
| Pemain tiruan | Non-kontributor mendapat nol |
| Aditivitas | φ(v + w) = φ(v) + φ(w) |
**Interpretasi:** Nilai Shapley setiap pemain adalah kontribusi marjinal rata-rata mereka di semua kemungkinan urutan pembentukan koalisi.
### Contoh yang Berhasil
Tiga pemain: v(∅) = 0, v({1}) = 0, v({2}) = 0, v({3}) = 0, v({1,2}) = 50, v({1,3}) = 70, v({2,3}) = 60, v({1,2,3}) = 100.
| Pemain | Kontribusi marjinal (dirata-ratakan atas pemesanan) | Nilai Shapley |
|--------|--------------------------------------------------|------------------------------|
| 1 | (100+50+70+70+50+0)/6 = 56,7 | 37,5 |
| 2 | (100+50+60+60+50+0)/6 | 27.5 |
| 3 | (100+70+60+70+60+0)/6 | 35.0 |
(Dihitung secara tepat menggunakan rumus Shapley untuk setiap permutasi.)
---

## Desain Mekanisme
**Desain mekanisme** adalah "teori permainan terbalik" — alih-alih menganalisis game tertentu, desainlah game yang memberikan hasil yang diinginkan.
### Prinsip Wahyu
Mekanisme apa pun yang mencapai hasil yang diinginkan dapat digantikan dengan **mekanisme pengungkapan langsung** di mana pengungkapan kebenaran merupakan keseimbangan Nash.
### Teori Lelang
| Jenis Lelang | Aturan | Kesetaraan Pendapatan |
|-------------|-------|---------------------|
| **Tawaran tersegel harga pertama** | Penawar tertinggi menang, membayar tawarannya | Semua lelang standar menghasilkan pendapatan yang diharapkan sama |
| **Tawaran tersegel harga kedua (Vickrey)** | Penawar tertinggi menang, membayar tawaran tertinggi kedua | (di bawah nilai-nilai pribadi independen) |
| **Bahasa Inggris (naik)** | Harga naik; pertama yang menerima kemenangan | — |
| **Belanda (turun)** | Harga turun; pertama yang menerima kemenangan | — |
### Lelang Vickrey (Harga Kedua)
**Strategi dominan:** Tawarkan nilai Anda yang sebenarnya.
| Properti | Pernyataan |
|----------|-----------|
| Penawaran yang jujur ​​| Strategi dominan lemah |
| Efisiensi | Item diberikan kepada penawar dengan nilai tertinggi |
| Pendapatan | Pendapatan yang diharapkan sama dengan harga pertama (Teorema Kesetaraan Pendapatan) |
### Desain Lelang Optimal (Myerson)
Lelang yang memaksimalkan pendapatan:
- Mengalokasikan kepada penawar dengan **penilaian virtual** tertinggi
- Menetapkan harga cadangan
- Penilaian virtual: ψ(v) = v − (1−F(v))/f(v)
---

## Koneksi ke Pembelajaran Mesin
### Jaringan Adversarial Generatif (GAN)
GAN adalah permainan dua pemain antara generator G dan diskriminator D:
min_G max_D V(D, G) = E[log D(x)] + E[log(1 − D(G(z)))]
| Konsep Teori Permainan | Setara GAN |
|--------------------|-----------------|
| Permainan zero-sum dua pemain | Generator vs diskriminator |
| Kesetimbangan Nash | G menghasilkan data nyata, D menghasilkan ½ di mana-mana |
| Minimaks | Fungsi tujuan GAN |
| Mode runtuh | Kegagalan mencapai keseimbangan |
### Pembelajaran Penguatan Multi-Agen (MARL)
| Konsep | Aplikasi MARL |
|---------|-----------------|
| Kesetimbangan Nash | Kebijakan yang stabil dalam pengaturan multi-agen |
| Minimaks | Kebijakan yang kuat terhadap lawan yang bermusuhan |
| Permainan kooperatif | Pembentukan koalisi, alokasi tugas |
| Nilai Shapley | Penugasan kredit (agen mana yang menyumbang apa?) |
| Desain mekanisme | Merancang insentif dalam sistem multi-agen |
| Drama fiktif | Algoritma pembelajaran konvergen ke keseimbangan Nash |
### Koneksi ML Lainnya
| Aplikasi | Alat Teori Permainan |
|-------------|-----------------|
| Desain lelang iklan (Google, Facebook) | Desain mekanisme, teori lelang |
| Desain pasar (Uber, Airbnb) | Teori pencocokan, desain mekanisme |
| Ketahanan permusuhan | Permainan zero-sum antara penyerang dan bek |
| Pembagian yang adil | Nilai Shapley, alokasi bebas rasa iri |
| Pembelajaran gabungan | Teori permainan kooperatif untuk pengukuran kontribusi |
| Sistem rekomendasi | Desain mekanisme untuk perolehan preferensi yang jujur ​​|
---

## Ringkasan
| Konsep | Ide Inti | Hasil Utama |
|---------|-----------|------------|
| Permainan bentuk strategis | Pemain, strategi, hasil | Representasi matriks permainan |
| Strategi dominan | Terbaik terlepas dari yang lain | Eliminasi berulang |
| Kesetimbangan Nash | Tidak ada penyimpangan sepihak yang menguntungkan | Ada di setiap game terbatas |
| Strategi Campuran | Acak tindakan | Teorema keberadaan Nash |
| Minimaks | Kasus terburuk terbaik (zero-sum) | Teorema minimaks Von Neumann |
| Bentuk ekstensif | Gerakan berurutan | Induksi mundur, kesempurnaan subgame |
| Permainan kooperatif | Koalisi yang mengikat | Inti, nilai Shapley |
| Desain mekanisme | Rancang permainan untuk hasil | Prinsip Wahyu, Lelang Optimal |
| Teori lelang | Menjual lewat kompetisi | Kesetaraan pendapatan, lelang Vickrey |
Teori permainan adalah matematika pemikiran strategis. Di dunia yang semakin padat penduduknya dengan interaksi agen AI, pasar otomatis, dan sistem persaingan, teori permainan menyediakan perangkat penting untuk memprediksi perilaku, merancang mekanisme, dan membangun sistem multi-agen yang kuat. Bagi data scientist, panduan ini menjelaskan cara kerja GAN, cara lelang online menghasilkan pendapatan miliaran, dan cara membangun sistem AI yang berkinerja baik di lingkungan yang kompetitif.