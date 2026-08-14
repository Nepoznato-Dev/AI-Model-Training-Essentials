<!--
---
# Metadata
title: "Number Theory"
description: "Divisibility, primes, modular arithmetic, Euler's theorem, Fermat's little theorem, Chinese Remainder Theorem, and applications to cryptography"
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
    changes: "Initial deep-dive into number theory"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2027-02-10"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-10"

# Classification
tags: [number-theory, primes, divisibility, modular-arithmetic, cryptography, euler-theorem, fermat, chinese-remainder-theorem]
difficulty_level: "advanced"
prerequisites:
  - "mathematics.md"
  - "discrete_mathematics.md"
estimated_reading_time: "25 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Teori Angka
Teori bilangan adalah studi tentang bilangan bulat — bilangan bulat dan sifat-sifatnya. Gauss menyebutnya "ratu matematika". Meskipun mempelajari objek paling sederhana (1, 2, 3, ...), teori bilangan menghasilkan beberapa masalah terdalam dan tersulit dalam seluruh matematika. Saat ini, ini mendasari kriptografi modern, algoritma hashing, kode koreksi kesalahan, dan pembuatan angka acak.
---

## Pembagian dan Algoritma Pembagian
### Definisi Inti
| Istilah | Definisi | Contoh |
|------|------------|---------|
| **Dibagi** | sebuah \| b artinya ∃k ∈ ℤ: b = ak | 3 \| 12 (karena 12 = 3×4) |
| **Pembagi** | Bilangan yang membagi bilangan lain | Pembagi 12 : 1, 2, 3, 4, 6, 12 |
| **Beberapa** | b adalah kelipatan a jika a \| b | 15 adalah kelipatan 5 |
| **Hasil Bagi** | Hasil pembagian | 17 5 = hasil bagi 3 |
| **Sisa** | Apa yang tersisa setelah pembagian | 17 5 = sisa 2 |
### Algoritma Pembagian
Untuk bilangan bulat a dan b dengan b > 0, terdapat bilangan bulat unik q (hasil bagi) dan r (sisa) sehingga:
a = bq + r, dimana 0 ≤ r < b
**Contoh:** 23 = 5 × 4 + 3. Hasil bagi q = 4, sisa r = 3.
### Sifat Dapat Dibagi
| Properti | Pernyataan |
|----------|-----------|
| Transitivitas | Jika \| b dan b \| c, lalu \| c |
| Linearitas | Jika \| b dan a \| c, lalu \| (bx + cy) untuk semua bilangan bulat x, y |
| Perbandingan | Jika \| b dan b > 0, maka a ≤ b |
| Sepele | sebuah \| 0 untuk semua a; 1 \| a untuk semua a; sebuah \| a untuk semua a ≠ 0 |
---

## Pembagi Persekutuan Terbesar (PBT)
**pembagi persekutuan terbesar** dari a dan b, dilambangkan dengan gcd(a, b), adalah bilangan bulat positif terbesar yang membagi a dan b.
### Algoritma Euclidean
Algoritma klasik paling efisien untuk menghitung GCD.
**Wawasan utama:** gcd(a, b) = gcd(b, a mod b)
**Algoritma:**```
function gcd(a, b):
    while b ≠ 0:
        t = b
        b = a mod b
        a = t
    return a
```

**Contoh yang Dikerjakan:** gcd(252, 105)
- 252 = 105 × 2 + 42 → gcd(105, 42)
- 105 = 42 × 2 + 21 → gcd(42, 21)
- 42 = 21 × 2 + 0 → gcd(21, 0)
- Hasil: gcd(252, 105) = 21
| Properti | Nilai |
|----------|-------|
| Kompleksitas waktu | HAI(log(min(a, b))) |
| Kompleksitas ruang | O(1) berulang |
### Identitas Bézout
Untuk sembarang bilangan bulat a, b, terdapat bilangan bulat x, y sehingga:
kapak + oleh = gcd(a, b)
**Algoritma Euclidean Diperluas** menghitung gcd(a, b) dan koefisien x, y secara bersamaan.
**Contoh Pengerjaan:** Carilah x, y sehingga 252x + 105y = 21.
- Penggantian kembali dari algoritma Euclidean:
  - 21 = 105 − 42 × 2
  - 42 = 252 − 105 × 2
  - 21 = 105 − (252 − 105 × 2) × 2 = 105 × 5 − 252 × 2
- Jadi x = −2, y = 5. Periksa: 252(−2) + 105(5) = −504 + 525 = 21.
### Properti Utama GCD
| Properti | Pernyataan |
|----------|-----------|
| gcd(a, 0) | = sebuah |
| gcd(a, 1) | = 1 (a dan 1 selalu koprima) |
| gcd(a, b) = gcd(b, a) | Komutatif |
| gcd(a, b) = gcd(a, b + ka) | Menambahkan kelipatan tidak mengubah GCD |
| gcd(ca, cb) | = c · gcd(a, b) |
| koprima | gcd(a, b) = 1 berarti a dan b tidak mempunyai faktor persekutuan |
---

## Bilangan Prima
**prima** adalah bilangan bulat yang lebih besar dari 1 yang pembagi positifnya hanyalah 1 dan dirinya sendiri.
### Properti Dasar
| Properti | Pernyataan |
|----------|-----------|
| **Teorema Dasar Aritmatika** | Setiap bilangan bulat n > 1 mempunyai faktorisasi prima yang unik |
| **Ketakterhinggaan bilangan prima** | Ada banyak sekali bilangan prima (Euclid, ~300 SM) |
| **Teorema Bilangan Prima** | Banyaknya bilangan prima ≤ n kira-kira n / ln(n) |
| ** Postulat Bertrand ** | Untuk setiap n > 1, terdapat p prima dengan n < p < 2n |
### Bilangan Prima Pertama
2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97...

### Faktorisasi Prima
Setiap bilangan bulat n > 1 dapat ditulis secara unik sebagai:
n = p₁^a₁ · p₂^a₂ · ... · pₖ^aₖ
dimana p₁ < p₂ < ... < pₖ adalah bilangan prima dan aᵢ ≥ 1.
**Contoh:**
- 60 = 2² × 3 × 5
- 360 = 2³ × 3² × 5
- 1001 = 7×11×13
**Menggunakan faktorisasi untuk menghitung GCD dan KPK:**
- gcd(a, b) = hasil kali pangkat min dari bilangan prima bersama
- lcm(a, b) = hasil kali pangkat maks semua bilangan prima
**Contoh:** a = 12 = 2² × 3, b = 18 = 2 × 3²
- gcd(12, 18) = 2¹ × 3¹ = 6
- lcm(12, 18) = 2² × 3² = 36
### Saringan Eratosthenes
Algoritma klasik untuk mencari semua bilangan prima hingga batas N.
| Properti | Nilai |
|----------|-------|
| Kompleksitas waktu | HAI(N log log N) |
| Kompleksitas ruang | PADA(N) |
**Algoritma:**
1. Daftarkan semua bilangan bulat dari 2 sampai N.
2. Mulailah dengan p = 2. Coret semua kelipatan p (dimulai dari p²).
3. Carilah bilangan tak bersilangan berikutnya > p. Tetapkan p ke nomor itu.
4. Ulangi sampai p² > N. Semua bilangan yang tidak disilang adalah bilangan prima.
### Pengujian Primalitas
| Metode | Ketik | Waktu | Kasus Penggunaan |
|--------|------|------|----------|
| Divisi percobaan | deterministik | HAI(√n) | Angka kecil |
| Uji Fermat | Probabilistik | HAI(k log² n) | Pemutaran cepat |
| Miller-Rabin | Probabilistik | HAI(k log² n) | Tujuan umum |
| AK | deterministik | HAI(log⁶ n) | Pentingnya teoretis |
**Uji primalitas fermat:** Jika p bilangan prima dan gcd(a, p) = 1, maka aᵖ⁻¹ ≡ 1 (mod p). Jika hal ini gagal untuk beberapa a, maka p pasti komposit. Jika melewati banyak nilai a acak, p kemungkinan besar adalah bilangan prima.
**Perhatian:** Bilangan Carmichael (misalnya 561) lulus uji Fermat untuk semua basa koprima tetapi merupakan bilangan komposit. Miller-Rabin menghindari masalah ini.
---

## Aritmatika Modular
Aritmatika modular mempelajari bilangan bulat di bawah "sampul" — aritmatika pada tampilan jam.
### Hubungan Kesesuaian
a ≡ b (mod n) artinya n | (a − b), yaitu a dan b meninggalkan sisa yang sama jika dibagi n.
### Properti Aritmatika
| Operasi | Aturan |
|-----------|------|
| Tambahan | (a + b) mod n = ((a mod n) + (b mod n)) mod n |
| Perkalian | (a × b) mod n = ((a mod n) × (b mod n)) mod n |
| Eksponen | aᵇ mod n dapat dihitung secara efisien dengan mengkuadratkan |
| Negasi | (−a) mod n = n − (sebuah mod n) |
### Eksponen Modular
Menghitung mod n secara efisien menggunakan **pengkuadratan berulang**:
**Contoh Pekerjaan:** 3¹³ mod 7
- 13 dalam biner: 1101
- 3¹ = 3 mod 7 = 3
- 3² = 9 mod 7 = 2
- 3⁴ = 4 mod 7 = 4
- 3⁸ = 16 mod 7 = 2
- 3¹³ = 3⁸ × 3⁴ × 3¹ = 2 × 4 × 3 = 24 mod 7 = 3
| Properti | Nilai |
|----------|-------|
| Kompleksitas waktu | HAI(log b · log² n) |
| Kompleksitas ruang | HAI(1) |
### Fungsi Total Euler
φ(n) menghitung bilangan bulat dari 1 hingga n yang koprima hingga n.
| n | φ(n) | Bilangan bulat koprima |
|---|------|------------------|
| 1 | 1 | {1} |
| 2 | 1 | {1} |
| 6 | 2 | {1, 5} |
| 7 | 6 | {1, 2, 3, 4, 5, 6} (7 bilangan prima) |
| 10 | 4 | {1, 3, 7, 9} |
| 12 | 4 | {1, 5, 7, 11} |
**Rumus:**
- Jika p bilangan prima: φ(p) = p − 1
- Jika p bilangan prima: φ(pᵏ) = pᵏ − pᵏ⁻¹ = pᵏ⁻¹(p − 1)
- Jika gcd(m, n) = 1: φ(mn) = φ(m) · φ(n) (perkalian)
- Umum: φ(n) = n · Π_{p|n} (1 − 1/p) dengan hasil kali faktor prima berbeda dari n
---

## Teorema Kunci
### Teorema Kecil Fermat
Jika p bilangan prima dan gcd(a, p) = 1, maka:
aᵖ⁻¹ ≡ 1 (mod p)
**Akibat wajar (untuk semua a):** aᵖ ≡ a (mod p)
**Penggunaan:** Invers modular cepat ketika modulusnya prima: a⁻¹ ≡ aᵖ⁻² (mod p)
**Contoh yang Berhasil:** Temukan 3⁻¹ mod 7.
- Oleh Fermat: 3⁻¹ ≡ 3⁵ (mod 7)
- 3² = 9 ≡ 2 (mod 7)
- 3⁴ = 4 (mod 7)
- 3⁵ = 3⁴ × 3 = 4 × 3 = 12 ≡ 5 (mod 7)
- Centang : 3×5 = 15 ≡ 1 (mod 7).
### Teorema Euler (Generalisasi Fermat)
Jika gcd(a, n) = 1, maka:
a^φ(n) ≡ 1 (mod n)
Ini menggeneralisasi Teorema Kecil Fermat dari bilangan prima ke modulus apa pun.
### Teorema Sisa Cina (CRT)
Jika m₁, m₂, ..., mₖ adalah koprima berpasangan, sistemnya:
x ≡ a₁ (mod m₁)
x ≡ a₂ (mod m₂)
...
x ≡ aₖ (mod mₖ)
memiliki solusi unik modulo M = m₁ · m₂ · ... · mₖ.
**Contoh Pekerjaan:** Selesaikan x ≡ 2 (mod 3), x ≡ 3 (mod 5), x ≡ 2 (mod 7).
- M = 3 × 5 × 7 = 105
- M₁ = 105/3 = 35; M₂ = 105/5 = 21; M₃ = 105/7 = 15
- Cari invers: 35y₁ ≡ 1 (mod 3) → 2y₁ ≡ 1 → y₁ = 2
  21y₂ ≡ 1 (mod 5) → y₂ ≡ 1 (mod 5) → y₂ = 1
  15y₃ ≡ 1 (mod 7) → y₃ ≡ 1 (mod 7) → y₃ = 1
- x = 2·35·2 + 3·21·1 + 2·15·1 = 140 + 63 + 30 = 233
- x ≡ 233 mod 105 = 23
- Periksa: 23 mod 3 = 2, 23 mod 5 = 3, 23 mod 7 = 2.
### Teorema Wilson
(p − 1)! ≡ −1 (mod p) jika dan hanya jika p adalah bilangan prima.
Sebagian besar untuk kepentingan teoritis — tidak praktis untuk pengujian primalitas karena menghitung faktorial mahal.
### Residu Kuadrat
Bilangan bulat a adalah **mod residu kuadrat n** jika x² ≡ a (mod n) mempunyai penyelesaian.
**Kriteria Euler:** a adalah residu kuadrat mod prime p iff a^((p−1)/2) ≡ 1 (mod p).
**Simbol legenda:** (a/p) = a^((p−1)/2) mod p, menghasilkan +1, −1, atau 0.
**Timbal Balik Kuadrat** (Gauss): Untuk bilangan prima ganjil yang berbeda p, q:
(p/q)(q/p) = (−1)^((p−1)/2 · (q−1)/2)
Teorema mendalam ini menghubungkan residu kuadrat pada bilangan prima yang berbeda dan memiliki delapan hukum tambahan yang menangani kasus p = 2.
---

## Penerapan Kriptografi
### Sistem Kripto RSA
Kriptosistem kunci publik yang paling banyak digunakan, berdasarkan pada kesulitan memfaktorkan bilangan bulat besar.
**Pengaturan:**
1. Pilih dua bilangan prima besar p, q (biasanya masing-masing 1024+ bit)
2. Hitung n = pq dan φ(n) = (p−1)(q−1)
3. Pilih e sehingga 1 < e < φ(n) dan gcd(e, φ(n)) = 1 (umum: e = 65537)
4. Hitung d ≡ e⁻¹ (mod φ(n)) menggunakan Algoritma Extended Euclidean
5. **Kunci publik:** (n, e). **Kunci pribadi:** (n, d)
**Enkripsi:** c = mᵉ mod n (di mana m adalah pesan teks biasa)
**Dekripsi:** m = cᵈ mod n
**Mengapa berhasil:** cᵈ = m^(ed) ≡ m (mod n) berdasarkan teorema Euler, karena ed ≡ 1 (mod φ(n)).
**Keamanan:** Memfaktorkan n ke dalam p dan q secara komputasi tidak layak untuk n yang besar (2048+ bit). Tanpa p dan q, penyerang tidak dapat menghitung φ(n) sehingga tidak dapat menemukan d.
### Pertukaran Kunci Diffie-Hellman
Memungkinkan dua pihak untuk membuat rahasia bersama melalui saluran yang tidak aman.
**Penyiapan:** Setuju dengan p prima besar dan generator g (mod p).
**Protokol:**
1. Alice memilih rahasia a, mengirimkan A = gᵃ mod p ke Bob
2. Bob memilih rahasia b, mengirimkan B = gᵇ mod p ke Alice
3. Alice menghitung s = Bᵃ mod p = gᵃᵇ mod p
4. Bob menghitung s = Aᵇ mod p = gᵃᵇ mod p
5. Keduanya berbagi rahasia s = gᵃᵇ mod p
**Keamanan:** Berdasarkan tingkat kesulitan **masalah logaritma diskrit** — menemukan a dari gᵃ mod p.
### Fungsi Hash dan Teori Bilangan
Fungsi hash yang baik menggunakan aritmatika modular untuk mendistribusikan kunci secara seragam:
- **Hash perkalian:** h(k) = (k · A) mod m, dengan A ≈ m · (√5 − 1) / 2 (rasio emas)
- **Hashing universal:** h(k) = ((ak + b) mod p) mod m, dengan p adalah bilangan prima, a, b adalah acak
---

## Relevansi dengan Pembelajaran Mesin dan Ilmu Data
| Konsep Teori Bilangan | Aplikasi |
|-------|-------------|
| Aritmatika modular | Hashing (tabel hash, peta hash), pembuatan angka acak |
| Bilangan prima | Ukuran tabel hash (gunakan ukuran tabel prima untuk mengurangi tabrakan) |
| Algoritma GCD / Euclidean | Aritmatika rasional, menyederhanakan pecahan dalam probabilitas |
| Eksponen modular | Keamanan kriptografi untuk model ML yang disajikan melalui HTTPS |
| Total Euler | Pembuatan kunci RSA, memahami jaminan kriptografi |
| Teorema Sisa Cina | Komputasi terdistribusi, aritmatika modular paralel |
| Pengujian primalitas | Menghasilkan bilangan prima untuk operasi kriptografi |
| Residu kuadrat | Masalah residuositas kuadrat dalam kriptografi tingkat lanjut |
| Bidang terbatas (GF(p), GF(2ᵏ)) | Kode koreksi kesalahan, kode Reed-Solomon, enkripsi AES |
---

## Ringkasan
| Topik | Ide Inti | Hasil Utama |
|-------|-----------|------------|
| Dapat dibagi | Pembagian dengan sisa | Algoritma pembagian: a = bq + r |
| simpul | Faktor bersama terbesar | Algoritma Euclidean: O(log n) |
| Bilangan prima | Atom bilangan bulat | Teorema Dasar Aritmatika (faktorisasi unik) |
| Aritmatika Modular | Aritmatika sampul | Kelas kongruensi, eksponensial modular |
| Total Euler | Menghitung bilangan bulat koprima | φ(n) = n · Π(1 − 1/p) |
| Teorema Kecil Fermat | Pintasan modulus prima | aᵖ⁻¹ ≡ 1 (mod p) |
| Teorema Euler | Fermat Umum | a^φ(n) ≡ 1 (mod n) |
| Teorema Sisa Cina | Menggabungkan sistem modular | Produk mod solusi unik dari coprime moduli |
| Kriptografi | Masalah teori bilangan yang sulit | RSA (anjak piutang), Diffie-Hellman (log diskrit) |
Teori bilangan mengubah pertanyaan sederhana tentang bilangan bulat menjadi matematika mendalam dengan penerapan praktis yang mendalam. Setiap koneksi web yang aman, pesan terenkripsi, dan tanda tangan digital bergantung pada hasil teori bilangan yang ditemukan berabad-abad sebelum komputer ada. Bagi ilmuwan data dan teknisi ML, memahami teori bilangan memberikan wawasan tentang hashing, pembuatan angka acak, dan infrastruktur kriptografi yang melindungi data saat transit dan saat disimpan.