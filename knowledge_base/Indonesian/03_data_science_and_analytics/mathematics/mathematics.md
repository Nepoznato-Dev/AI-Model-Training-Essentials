---
# Metadata
title: "Mathematics"
description: "Number systems, algebra, geometry, calculus, set theory, linear algebra, and binary — the mathematical foundations for data science and ML"
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
    date: "2026-08-09"
    author: "AI Model Training Team"
    changes: "Split from math_and_logic.md; expanded into standalone file"

# Review
created: "2026-08-09"
last_modified: "2026-08-09"
review_date: "2027-02-09"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-09"

# Classification
tags: [mathematics, algebra, calculus, geometry, linear-algebra, number-theory, set-theory]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "14 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

#Matematika
Matematika bukan hanya mata pelajaran yang dipelajari di sekolah — matematika mendasari hampir semua bidang teknis. Fisika menggunakannya untuk menggambarkan alam semesta. Ilmu komputer menggunakannya untuk merancang algoritma. Pembelajaran mesin menggunakannya untuk mengoptimalkan bobot. Keuangan menggunakannya untuk menilai risiko. Penguasaan setiap cabang tidak diperlukan, namun memahami lanskapnya — dan mengetahui di mana setiap cabang berlaku — membuat topik lain lebih mudah untuk dipahami.
---

## Sistem Angka
Sebelum hal lain, ada baiknya untuk memahami jenis angka yang Anda gunakan. Setiap lapisan memperluas lapisan sebelumnya untuk memecahkan masalah yang tidak dapat dipecahkan oleh lapisan lama.
| Jenis Nomor | Apa yang Termasuk | Mengapa Diciptakan | Contoh |
|---|---|---|---|
| Bilangan asli | 1, 2, 3, 4, ... | Menghitung sesuatu | 5 apel |
| Bilangan bulat | 0, 1, 2, 3, ... | Mewakili "tidak ada" | 0 derajat |
| Bilangan bulat | ..., −2, −1, 0, 1, 2, ... | Hutang, suhu di bawah nol | −15°C |
| Bilangan rasional | p/q dimana q ≠ 0 | Membagi sesuatu secara tidak merata | 1/3, 0,75 |
| Bilangan irasional | Tidak dapat dinyatakan sebagai pecahan | Diagonal, lingkaran, pertumbuhan | √2, π, e |
| Bilangan nyata | Semua rasional + irasional | Garis bilangan lengkap | 3.14159... |
| Bilangan imajiner | Kelipatan i = √(−1) | Menyelesaikan x² + 1 = 0 | 3i |
| Bilangan kompleks | a + bi (nyata + imajiner) | Teknik elektro, mekanika kuantum | 2 + 3i |
---

## Aritmatika dan Teori Bilangan
Dasar-dasarnya: penjumlahan, pengurangan, perkalian, pembagian, dan aturan-aturan yang mengatur urutannya.
**Urutan operasi** (PEMDAS/BODMAS): Tanda kurung → Eksponen → Perkalian/Pembagian (kiri ke kanan) → Penjumlahan/Pengurangan (kiri ke kanan).
**Bilangan prima** — bilangan bulat yang lebih besar dari 1 tanpa pembagi selain 1 dan bilangan itu sendiri — adalah atom dalam teori bilangan. Beberapa yang pertama: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29.
Mengapa bilangan prima penting di luar kelas matematika: enkripsi modern (RSA) bergantung pada fakta bahwa mengalikan dua bilangan prima besar itu mudah, tetapi memfaktorkan kembali hasilnya merupakan proses komputasi yang brutal.
**Operasi yang berguna:**
- Faktorisasi prima: 84 = 2² × 3 × 7
- Pembagi Persekutuan Terbesar (PBT) dari 24 dan 36: 12
- Kelipatan Persekutuan Terkecil (KPK) dari 4 dan 6:12
---

## Aljabar
Aljabar adalah tempat Anda berhenti bekerja dengan angka tertentu dan mulai bekerja dengan *hubungan*. Variabel seperti`x`tidak memiliki nilai tetap — variabel mewakili apa pun yang menjadikan persamaan tersebut benar.
**Rumus kuadrat** menyelesaikan ax² + bx + c = 0:
x = (−b ± √(b² − 4ac)) / 2a
**Jenis fungsi umum dan lokasi kemunculannya:**
| Fungsi | Rumus | Bentuk | Contoh Dunia Nyata |
|---|---|---|---|
| Linier | kamu = mx + b | Garis lurus | Biaya per unit dengan tarif tetap |
| Kuadrat | y = kapak² + bx + c | Parabola | Gerak proyektil, jarak pengereman |
| Eksponensial | kamu = a × b² | Pertumbuhan / pembusukan yang cepat | Bunga majemuk, pertumbuhan populasi, penyebaran virus |
| Logaritma | y = log_b(x) | Pertumbuhan lambat, kebalikan dari eksponensial | Skala desibel, skala pH, kompleksitas algoritma |
**Kosakata kunci:**
- **Domain**: semua input valid (misalnya, tidak dapat dibagi dengan nol, tidak dapat mengambil √ dari bilangan real negatif)
- **Rentang**: semua kemungkinan keluaran
- **Kemiringan** (m): laju perubahan — "untuk setiap 1 unit x, y berubah sebesar m"
- **Intercept**: ketika fungsi melintasi suatu sumbu
---

## Geometri
Geometri mempelajari bentuk, ukuran, dan hubungan spasial. Itu muncul di mana-mana: mesin game menggunakannya untuk rendering, robotika menggunakannya untuk perencanaan jalur, arsitektur menggunakannya untuk desain struktural.
**Rumus penting:**
| Bentuk | Properti | Rumus |
|---|---|---|
| Segitiga | Jumlah sudut | 180° |
| Segi Empat | Jumlah sudut | 360° |
| Lingkaran | Keliling | 2πr |
| Lingkaran | Daerah | πr² |
| Bola | Jilid | (4/3)πr³ |
| Segitiga siku-siku | Teorema Pythagoras | a² + b² = c² |
**π (pi)** ≈ 3,14159 — rasio keliling lingkaran terhadap diameternya. Ini muncul di tempat yang tidak Anda duga: probabilitas (distribusi normal), rekayasa (pemrosesan sinyal), bahkan persamaan prinsip ketidakpastian Heisenberg.
---

## Kalkulus
Studi kalkulus *perubahan* dan *akumulasi*. Jika aljabar menangani snapshot, kalkulus menangani gambar bergerak.
### Kalkulus Diferensial
Tingkat perubahan. Turunan f'(x) menunjukkan seberapa cepat f berubah pada suatu titik.
| Fungsi f(x) | Turunan f'(x) | Intuisi |
|---|---|---|
| xⁿ | n·xⁿ⁻¹ | Aturan kekuasaan |
| eˣ | eˣ | Satu-satunya fungsi yang sama dengan turunannya sendiri |
| dalam(x) | 1/x | Laju pertumbuhan melambat seiring bertambahnya x |
| dosa(x) | karena(x) | Laju perubahan osilasi |
**Mengapa turunan penting dalam ML:** penurunan gradien — algoritme yang melatih sebagian besar jaringan neural — bekerja dengan menghitung turunan fungsi kerugian dan melangkah ke arah yang mengurangi kesalahan.
### Aturan Diferensiasi Utama
| Aturan | Rumus | Kasus Penggunaan |
|------|---------|----------|
| **Aturan Rantai** | (f∘g)' = f'(g(x)) · g'(x) | Fungsi bersarang — propagasi mundur di jaringan saraf |
| **Peraturan Produk** | (fg)' = f'g + fg' | Mengalikan dua fungsi x |
| **Aturan Hasil Bagi** | (f/g)' = (f'g − fg') / g² | Membagi dua fungsi x |
### Kalkulus Integral
Akumulasi. Integral mewakili area di bawah kurva. Jika turunan menjawab “seberapa cepat perubahannya?”, integral menjawab “berapa akumulasinya?”
**Teorema dasar kalkulus** menghubungkan keduanya: diferensiasi dan integrasi adalah operasi invers.
| Integral | Hasil | Kasus Penggunaan |
|----------|--------|----------|
| ∫ xⁿ dx | xⁿ⁺¹/(n+1) + C | Luas di bawah kurva polinomial |
| ∫ eˣ dx | eˣ + C | Total akumulasi pertumbuhan |
| ∫ 1/x dx | dalam|x| + C | Akumulasi logaritma |
---

## Set
**Set** adalah kumpulan objek berbeda — dasar matematika modern.
| Operasi | Simbol | Arti | Contoh (A={1,2,3}, B={2,4}) |
|---|---|---|---|
| Persatuan | A ∪ B | Elemen di salah satu set | {1, 2, 3, 4} |
| Persimpangan | A ∩ B | Elemen di kedua set | {2} |
| Perbedaan | A \ B | Elemen di A tetapi tidak di B | {1, 3} |
| Kumpulan kosong | ∅ | Tidak mengandung apa pun | {} |
| Bagian | A ⊂ B | Semua elemen A ada di B | {1,2} ⊂ {1,2,3} |
Teori himpunan muncul dalam database (SQL JOIN pada dasarnya adalah operasi himpunan), probabilitas (peristiwa adalah himpunan hasil), dan pemrograman (himpunan, peta hash).
---

## Basis Biner dan Angka
Komputer berpikir dalam biner (basis 2): hanya 0 dan 1. Manusia berpikir dalam desimal (basis 10). Pemrogram sering menggunakan heksadesimal (basis 16) sebagai cara ringkas untuk merepresentasikan biner.
| Basis | Digit yang Digunakan | Contoh | Setara Desimal |
|---|---|---|---|
| Biner (basis 2) | 0, 1 | 1011 | 8 + 0 + 2 + 1 = 11 |
| Desimal (basis 10) | 0–9 | 11 | 11 |
| Heksadesimal (basis 16) | 0–9, SEBUAH–F | B | 11 |
| Heksadesimal | 0–9, SEBUAH–F | A3 | 160 + 3 = 163 |
**Mengapa penting:** setiap bagian data di komputer — teks, gambar, audio, video — pada akhirnya hanyalah biner. Satu byte (8 bit) dapat mewakili 256 nilai berbeda. Warna dalam CSS (#FF5733), alamat memori (0x7FFF), dan alamat IP semuanya menggunakan hex karena memampatkan string biner yang panjang menjadi sesuatu yang dapat dibaca.
---

## Aljabar Linier untuk ML dan Grafik
Aljabar linier — vektor, matriks, dan transformasi — adalah mesin matematika di balik pembelajaran mesin, grafik komputer, simulasi fisika, dan mesin pencari.
### Vektor
**Vektor** adalah daftar angka yang diurutkan. Di ML, setiap titik data adalah vektor fitur:
- [23, 1.8, 75] dapat mewakili usia seseorang, tinggi badan dalam meter, dan berat badan dalam kg.
| Operasi Vektor | Rumus | Kasus Penggunaan |
|-----------------|---------|----------|
| **Penambahan** | a + b = [a₁+b₁, a₂+b₂, ...] | Menggabungkan vektor fitur |
| **Perkalian skalar** | c·a = [c·a₁, c·a₂, ...] | Fitur penskalaan |
| **Produk titik** | a·b = Σ aᵢbᵢ | Kesamaan, proyeksi |
| **Norma (besarnya)** | ||sebuah|| = √(Σ aᵢ²) | Panjang vektor |
| **Lintas produk** | a × b (hanya 3D) | Vektor tegak lurus, luas |
### Matriks
**Matriks** adalah susunan angka 2D. Bobot jaringan saraf disimpan sebagai matriks. Kumpulan 100 gambar mungkin berbentuk matriks (100, 784) — 100 baris, masing-masing dengan nilai 784 piksel.
**Operasi utama:**
| Operasi | Apa Fungsinya | Dimana Itu Muncul |
|---|---|---|
| Produk titik | Mengukur kesamaan antara dua vektor | Sistem rekomendasi, kesamaan kosinus |
| Perkalian matriks | Menggabungkan transformasi linier | Setiap lapisan jaringan saraf |
| Nilai eigen/vektor eigen | Arah suatu matriks berskala (tidak berputar) | Pengurangan dimensi PCA, PageRank |
| Peringkat matriks | Jumlah informasi independen | Kompresi, perkiraan peringkat rendah |
| Ubah urutan | Membalik baris dan kolom | Perhitungan gradien |
| Terbalik | A⁻¹ sehingga A·A⁻¹ = I | Memecahkan sistem linier |
**Kesamaan kosinus** = (a·b) / (||a|| × ||b||) — berkisar dari −1 (berlawanan) hingga 1 (arah yang sama). Beginilah cara mesin pencari mengukur apakah dua dokumen "tentang hal yang sama" dan bagaimana model penyematan membandingkan kesamaan semantik.
---

## Ringkasan
| Cabang | Pertanyaan Inti | Aplikasi Kunci |
|---|---|---|
| Teori Aritmatika & Bilangan | Bagaimana perilaku angka? | Kriptografi, hashing |
| Aljabar | Bagaimana hubungan yang tidak diketahui? | Pemodelan, persamaan |
| Geometri | Bagaimana cara kerja bentuk dan ruang? | Grafik, robotika, arsitektur |
| Kalkulus | Bagaimana keadaannya berubah? | Pelatihan jaringan saraf, fisika |
| Himpunan Teori | Bagaimana hubungan koleksi? | Basis data, probabilitas |
| Aljabar Linier | Bagaimana cara kerja transformasi? | ML, grafik, mesin pencari |
Tidak semua topik ini diperlukan segera. Namun, ketika seseorang mendalami bidang teknis apa pun, fondasi ini menjadi semakin relevan. Setiap cabang menjadi lebih jelas setelah masalah yang dirancang untuk dipecahkannya dipahami.