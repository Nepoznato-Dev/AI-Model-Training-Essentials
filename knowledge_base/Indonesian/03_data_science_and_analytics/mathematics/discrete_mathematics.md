<!--
---
# Metadata
title: "Discrete Mathematics"
description: "Sets in depth, relations, functions, combinatorics, pigeonhole principle, recurrence relations, and generating functions"
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
    changes: "Initial deep-dive into discrete mathematics"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2027-02-10"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-10"

# Classification
tags: [discrete-mathematics, set-theory, relations, combinatorics, pigeonhole-principle, recurrence-relations, generating-functions]
difficulty_level: "intermediate"
prerequisites:
  - "mathematics.md"
  - "../logic_and_critical_thinking.md"
estimated_reading_time: "25 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
#Matematika Diskrit
Matematika diskrit adalah studi tentang struktur matematika yang pada dasarnya dapat dihitung atau dipisahkan — sebagai lawan dari matematika berkelanjutan (kalkulus, analisis real), yang berhubungan dengan besaran yang halus dan tidak terputus. Matematika diskrit mendasari ilmu komputer, kriptografi, desain algoritma, dan struktur data. Jika matematika kontinu menggambarkan dunia fisik, maka matematika diskrit menggambarkan dunia komputasi.
---

## Tetapkan Teori Secara Mendalam
Himpunan adalah fondasi di mana hampir semua matematika modern dibangun. **Set** adalah kumpulan objek berbeda yang tidak berurutan, disebut **elemen** atau **anggota**.
### Landasan Aksiomatik (ZFC)
Teori himpunan modern bertumpu pada **aksioma Zermelo-Fraenkel dengan Aksioma Pilihan (ZFC)**. Aksioma-aksioma ini menyelesaikan paradoks seperti Paradoks Russell ("himpunan semua himpunan yang tidak memuat dirinya sendiri") dengan membatasi bagaimana himpunan dapat dibentuk.
| Aksioma | Pernyataan Informal |
|-------|--------------------|
| Ekstensionalitas | Dua himpunan dikatakan sama jika mempunyai elemen yang sama |
| Set Kosong | Terdapat himpunan tanpa elemen: ∅ |
| Memasangkan | Untuk setiap a, b, terdapat {a, b} |
| Persatuan | Untuk setiap keluarga himpunan, kesatuannya ada |
| Kumpulan Daya | Untuk himpunan S mana pun, himpunan semua himpunan bagian dari S ada: P(S) |
| Tak terhingga | Terdapat himpunan tak terhingga |
| Spesifikasi | Untuk sembarang himpunan A dan properti P, ada {x ∈ A : P(x)} |
| Penggantian | Bayangan himpunan pada fungsi terdefinisi adalah himpunan |
| Keteraturan | Setiap himpunan tak kosong mengandung elemen yang terpisah darinya (mencegah keanggotaan mandiri) |
| Pilihan | Untuk setiap keluarga himpunan lepas berpasangan tak kosong, terdapat fungsi pilihan |
### Kardinalitas dan Ukuran Himpunan
**Kardinalitas** suatu himpunan, dinotasikan |S|, mengukur "ukurannya".
| Konsep | Definisi | Contoh |
|---------|------------|---------|
| Himpunan terbatas | Memiliki bilangan asli sebagai kardinalitas | |{a,b,c}| = 3 |
| Sangat tak terbatas | Kardinalitas yang sama dengan ℕ | ℤ, ℚ tak terhingga |
| Tak terhitung | Lebih besar dari ℕ | ℝ, P(ℕ), himpunan semua fungsi ℕ → {0,1} |
| Teorema Penyanyi | Untuk himpunan S apa pun, |P(S)| > |S| | |P(ℕ)| > |ℕ| |
**Argumen diagonal Cantor** membuktikan bahwa ℝ tidak dapat dihitung: asumsikan Anda dapat membuat daftar semua real di [0,1], lalu buat real baru yang berbeda dari real ke-n di tempat desimal ke-n — kontradiksi.
### Operasi pada Set
| Operasi | Notasi | Definisi | Properti |
|-----------|----------|------------|----------|
| Persatuan | A ∪ B | {x : x ∈ A atau x ∈ B} | Komutatif, asosiatif |
| Persimpangan | A ∩ B | {x : x ∈ A dan x ∈ B} | Komutatif, asosiatif |
| Perbedaan | A \ B | {x : x ∈ A dan x ∉ B} | Tidak komutatif |
| Perbedaan Simetris | A △ B | (A\B) ∪ (B\A) | Komutatif, asosiatif |
| Pelengkap | Dan | U \ A (di mana U adalah himpunan semesta) | (Aᶜ)ᶜ = SEBUAH |
| Produk Kartesius | A×B | {(a,b) : a ∈ A, b ∈ B} | |A×B| = |SEBUAH| · |B| |
**Hukum De Morgan:**
- (A ∪ B)ᶜ = Aᶜ ∩ Bᶜ
- (A ∩ B)ᶜ = Aᶜ ∪ Bᶜ
**Prinsip Inklusi-Eklusi** (untuk himpunan berhingga):
|A₁ ∪ A₂ ∪ ... ∪ Aₙ| = Σ|Aᵢ| − Σ|Aᵢ ∩ Aⱼ| + Σ|Aᵢ ∩ Aⱼ ∩ Aₖ| − ... + (−1)ⁿ⁺¹|A₁ ∩ ... ∩ Aₙ|
---

## Hubungan
**relasi** R pada himpunan A dan B adalah himpunan bagian dari A × B. Jika (a, b) ∈ R, kita tuliskan aRb.
### Jenis Relasi
Suatu relasi R pada himpunan A mempunyai sifat sebagai berikut:
| Properti | Definisi | Contoh |
|----------|------------|---------|
| refleksif | ∀a ∈ A: aRa | ≤ pada ℤ |
| Tidak refleksif | ∀a ∈ A: ¬(aRa) | < pada ℤ |
| Simetris | ∀a,b: aRb → bRa | = di himpunan mana pun |
| Antisimetris | ∀a,b: aRb ∧ bRa → a = b | ≤ pada ℤ |
| Transitif | ∀a,b,c: aRb ∧ bRc → aRc | <, ≤, = pada ℤ |
### Hubungan Kesetaraan
**Relasi ekivalensi** bersifat refleksif, simetris, dan transitif. Ini mempartisi satu set menjadi **kelas kesetaraan** yang terpisah.
**Contoh:** Aritmatika modular. Definisikan a ~ b jika a ≡ b (mod n). Kelas ekivalensinya adalah [0], [1], ..., [n−1], yang mempartisi ℤ menjadi n kelas.
**Contoh Pengerjaan:** Pada ℤ × ℤ, tentukan (a,b) ~ (c,d) iff a + d = b + c. Ini adalah hubungan kesetaraan. Kelas [(0,0)] = {(n,n) : n ∈ ℤ}. Kelas [(1,0)] = {(n+1,n) : n ∈ ℤ}. Konstruksi ini sebenarnya mendefinisikan bilangan bulat dari bilangan asli.
### Pesanan Sebagian
**urutan parsial** bersifat refleksif, antisimetris, dan transitif. Himpunan dengan urutan sebagian disebut **himpunan terurut sebagian (poset)**.
| Konsep | Definisi | Contoh |
|---------|------------|---------|
| Pose | (S, ≤) dengan ≤ urutan parsial | (P(A), ⊆) — himpunan bagian diurutkan berdasarkan penyertaan |
| Rantai | Subset yang terurut seluruhnya | {∅, {a}, {a,b}} dalam P({a,b,c}) |
| Antirantai | Subset dimana tidak ada dua elemen yang sebanding | {{a}, {b}} dalam P({a,b}) |
| Diagram Hasse | Representasi visual dari sebuah poset | Gambarkan tepi hanya untuk menutupi relasi |
| Batas Atas | Sebuah elemen ≥ setiap elemen dalam subset | sup({2,3}) = 6 in (ℤ, \|) (dapat dibagi) |
| Batas Atas Terkecil (sup) | Batas atas terkecil | sup({2,3}) pada (ℕ, ≤) adalah 3 |
| Batas Bawah Terbesar (inf) | Batas bawah terbesar | inf({4,6}) pada (ℕ, \|) adalah 2 |
---

## Fungsi
A **fungsi** f: A → B menugaskan ke setiap elemen A tepat satu elemen B.
### Klasifikasi Fungsi
| Ketik | Definisi | Contoh |
|------|------------|---------|
| Suntikan (satu-ke-satu) | f(a) = f(b) → a = b | f(x) = 2x dari ℤ → ℤ |
| Surjektif (ke) | ∀b ∈ B, ∃a ∈ A: f(a) = b | f(x) = x mod 2 dari ℤ → {0,1} |
| Bijektif | Baik injektif maupun dugaan | f(x) = x + 1 dari ℤ → ℤ |
### Konsep Fungsi Penting
| Konsep | Definisi | Kasus Penggunaan |
|---------|------------|----------|
| Fungsi terbalik | f⁻¹ ada jika f bersifat bijektif | Mendekripsi data terenkripsi |
| Komposisi | (g ∘ f)(x) = g(f(x)) | Transformasi berantai |
| Fungsi identitas | nomor identitas(x) = x | Elemen netral untuk komposisi |
| Titik tetap | f(x) = x | Definisi rekursif, semantik |
| Permutasi | Sebuah bijeksi dari suatu himpunan ke dirinya sendiri | Menata ulang data, mengacak |
### Fungsi Menghitung
Diberikan himpunan berhingga |A| = m dan |B| = n:
| Ketik | Hitung |
|------|-------|
| Semua fungsi A → B | tidak |
| Fungsi injeksi | N! / (n−m)! (jika n ≥ m, jika tidak 0) |
| Fungsi surjektif | Σₖ₌₀ⁿ (−1)ᵏ · C(n,k) · (n−k)ᵐ (dengan inklusi-eksklusi) |
| Fungsi Bijektif | N! (bila m = n) |
---

## Kombinatorik
Kombinatorik adalah matematika menghitung, mengatur, dan memilih.
### Prinsip Dasar Penghitungan
| Prinsip | Pernyataan | Contoh |
|-----------|-----------|---------|
| Aturan Jumlah | Jika A dan B saling lepas, |A ∪ B| = |SEBUAH| + |B| | Memilih buah: 3 apel + 4 jeruk = 7 pilihan |
| Aturan Produk | |A×B| = |SEBUAH| · |B| | Pakaian : 3 baju × 4 celana = 12 baju |
| Aturan Bijeksi | Jika f: A → B adalah sebuah bijeksi, |A| = |B| | Hitung himpunan bagian dengan menghitung string biner |
| Pelengkap | |SEBUAH| = |kamu| − |Aᶜ| | Hitung "setidaknya satu" sebagai total dikurangi "tidak ada" |
### Permutasi dan Kombinasi
| Notasi | Nama | Rumus | Arti |
|----------|------|---------|---------|
| C(n, k) atau (nk) | Koefisien binomial | N! / (k!(n−k)!) | Cara memilih k item dari n (urutan tidak masalah) |
| P(n, k) | k-permutasi dari n | N! / (n−k)! | Cara menyusun k item dari n (urutan penting) |
| N! | Faktorial | n × (n−1) × ... × 1 | Cara menyusun semua n item |
| (nk) dengan pengulangan | Pilih banyak | C(n+k−1, k) | Pilih k dari n dengan pengulangan diperbolehkan |
**Teorema Binomial:**
(x + y)ⁿ = Σₖ₌₀ⁿ C(n,k) · xᵏ · yⁿ⁻ᵏ
**Identitas Pascal:** C(n,k) = C(n−1,k−1) + C(n−1,k)
### Prinsip Lubang Merpati
**Bentuk dasar:** Jika n+1 objek ditempatkan ke dalam n kotak, setidaknya satu kotak berisi ≥ 2 objek.
**Bentuk umum:** Jika N objek ditempatkan ke dalam k kotak, setidaknya satu kotak berisi ≥ ⌈N/k⌉ objek.
**Contoh yang Dikerjakan:**
1. Di antara 13 orang, paling sedikit 2 orang mempunyai bulan lahir yang sama. (13 orang, 12 bulan → merpati.)
2. Tunjukkan bahwa di antara 5 bilangan bulat ada 3 yang jumlahnya habis dibagi 3.
   - Pertimbangkan residu mod 3: {0, 1, 2}. Dengan 5 bilangan bulat dan 3 kelas residu, secara umum, setidaknya ⌈5/3⌉ = 2 berbagi residu.
   - Jika 3 berbagi residu r: jumlah mereka ≡ 3r ≡ 0 (mod 3).
   - Jika 2 berbagi residu 0 dan 2 berbagi residu 1: pilih satu dari setiap pasangan ditambah elemen residu-0 → jumlah ≡ 0 (mod 3).
3. **Aplikasi di CS:** Algoritme kompresi lossless apa pun harus memperluas beberapa input. (Jika setiap string n-bit dikompresi menjadi < n bit, Anda akan memetakan 2ⁿ string menjadi kurang dari 2ⁿ string terkompresi — melanggar injektivitas.)
### Nomor Katalan
**Nomor Catalan** ke-n Cₙ = C(2n, n) / (n+1) dihitung:
| Struktur | Contoh |
|-----------|---------|
| Urutan tanda kurung yang valid | ()(), (()) untuk n = 2 |
| Pohon biner dengan n node internal | 2 pohon untuk n = 2 |
| Jalur tidak melintasi diagonal | Jalur kisi dari (0,0) ke (n,n) tetap di bawah y = x |
| Triangulasi poligon | Cara membagi (n+2)-gon menjadi segitiga |
Beberapa yang pertama: C₀ = 1, C₁ = 1, C₂ = 2, C₃ = 5, C₄ = 14, C₅ = 42.
Perulangan: Cₙ₊₁ = Σᵢ₌₀ⁿ Cᵢ · Cₙ₋ᵢ
---

## Hubungan Pengulangan
**Relasi perulangan** mendefinisikan setiap suku suatu barisan sebagai fungsi dari suku-suku sebelumnya.
### Jenis dan Solusi
| Ketik | Formulir | Metode Solusi |
|------|------|-----------------|
| Linear homogen (koefisien konstan) | aₙ = c₁aₙ₋₁ + c₂aₙ₋₂ + ... + cₖaₙ₋ₖ | Persamaan karakteristik |
| Linier tidak homogen | aₙ = c₁aₙ₋₁ + ... + f(n) | Solusi khusus + solusi homogen |
| Bagilah dan taklukkan | T(n) = pada(n/b) + f(n) | Teorema utama |
### Metode Persamaan Karakteristik
Untuk aₙ = c₁aₙ₋₁ + c₂aₙ₋₂, bentuk persamaan karakteristiknya:
r² − c₁r − c₂ = 0
| Kasus | Akar | Solusi Umum |
|------|-------|------------------|
| Dua akar real berbeda r₁, r₂ | r₁ ≠ r₂ | aₙ = A·r₁ⁿ + B·r₂ⁿ |
| Akar berulang r | r₁ = r₂ = r | aₙ = (A + Bn)·rⁿ |
| Akar kompleks α ± βi | Ubah ke polar: r·e^(±iθ) | aₙ = rⁿ(A cos(nθ) + B sin(nθ)) |
**Contoh Pengerjaan:** Deret Fibonacci Fₙ = Fₙ₋₁ + Fₙ₋₂, F₀ = 0, F₁ = 1.
- Persamaan karakteristik: r² − r − 1 = 0
- Akar: r = (1 ± √5) / 2 → φ = (1+√5)/2 ≈ 1.618, ψ = (1−√5)/2 ≈ −0.618
- Solusi umum: Fₙ = A·φⁿ + B·ψⁿ
- Dari kondisi awal: A = 1/√5, B = −1/√5
- **Bentuk tertutup:** Fₙ = (φⁿ − ψⁿ) / √5 (Rumus Binet)
### Teorema Utama
Untuk perulangan dalam bentuk T(n) = aT(n/b) + f(n) dimana a ≥ 1, b > 1:
Misalkan c = log_b(a).
| Kasus | Kondisi | Solusi |
|------|-----------|----------|
| 1 | f(n) = O(nᵈ) dengan d< c | T(n) = Θ(nᶜ) |
| 2 | f(n) = Θ(nᶜ) | T(n) = Θ(nᶜ log n) |
| 3 | f(n) = Θ(nᵈ) where d >c, dan af(n/b) ≤ kf(n) untuk beberapa k < 1 | T(n) = Θ(nᵈ) |
**Contoh:**
- Pengurutan gabungan: T(n) = 2T(n/2) + O(n). Di sini a=2, b=2, c=1, f(n)=n=Θ(n¹). Kasus 2: T(n) = Θ(n log n).
- Pencarian biner: T(n) = T(n/2) + O(1). Di sini a=1, b=2, c=0, f(n)=1=Θ(n⁰). Kasus 2: T(n) = Θ(log n).
---

## Fungsi Pembangkit
**Fungsi pembangkit** mengkodekan barisan (aₙ) sebagai koefisien deret pangkat formal.
### Jenis
| Ketik | Formulir | Kasus Penggunaan |
|------|------|----------|
| Biasa (OGF) | G(x) = Σₙ₌₀^∞ aₙxⁿ | Struktur, komposisi tidak berlabel |
| Eksponensial (EGF) | E(x) = Σₙ₌₀^∞ aₙxⁿ/n! | Struktur berlabel, permutasi |
### Fungsi Pembangkit Umum
| Urutan aₙ | OGF G(x) |
|-------------|-----------|
| 1, 1, 1, 1, ... | 1/(1−x) |
| 1, 2, 3, 4, ... | 1/(1−x)² |
| 1, r, r², r³, ... | 1/(1−rx) |
| C(n,k) untuk k | tetap xᵏ/(1−x)ᵏ⁺¹ |
| Fibonacci Fₙ | x/(1−x−x²) |
| Katalan Cₙ | (1 − √(1−4x)) / (2x) |
### Menggunakan Fungsi Pembangkit untuk Mengatasi Perulangan
**Contoh Pekerjaan:** Selesaikan aₙ = 3aₙ₋₁ − 2aₙ₋₂, a₀ = 1, a₁ = 3.
1. Misalkan G(x) = Σ aₙxⁿ.
2. Dari perulangan: G(x) − a₀ − a₁x = 3x(G(x) − a₀) − 2x²G(x)
3. Pengganti: G(x) − 1 − 3x = 3x(G(x) − 1) − 2x²G(x)
4. G(x)(1 − 3x + 2x²) = 1
5. G(x) = 1 / (1 − 3x + 2x²) = 1 / ((1−x)(1−2x))
6. Pecahan parsial: G(x) = 2/(1−2x) − 1/(1−x)
7. Ekstrak koefisien: aₙ = 2·2ⁿ − 1 = 2ⁿ⁺¹ − 1
**Verifikasi:** a₀ = 2−1 = 1, a₁ = 4−1 = 3, a₂ = 8−1 = 7. Periksa: 3(3) − 2(1) = 7.
---

## Aljabar Boolean dan Logika Proposisional
Aljabar Boolean adalah aljabar dari dua nilai kebenaran: **True (1)** dan **False (0)**. Ini adalah dasar matematika dari sirkuit digital, kueri basis data, dan persyaratan pemrograman.
### Operasi dan Hukum
| Operasi | Simbol | Arti | Tabel Kebenaran |
|-----------|--------|---------|-------------|
| DAN | p ∧ q | Benar hanya jika keduanya benar | T∧T=T, T∧F=F, F∧T=F, F∧F=F |
| ATAU | p ∨ q | Benar jika setidaknya satu benar | T∨T=T, T∨F=T, F∨T=T, F∨F=F |
| BUKAN | ¬p | Negasi | ¬T=F, ¬F=T |
| XOR | p ⊕ q | Benar jika salah satunya benar | T⊕T=F, T⊕F=T, F⊕T=T, F⊕F=F |
| TERSIRAT | hal → q | Salah hanya jika p=T dan q=F | T→T=T, T→F=F, F→T=T, F→F=T |
| DUA KONDISI | p ↔ q | Benar jika keduanya mempunyai nilai yang sama | T↔T=T, T↔F=F, F↔T=F, F↔F=T |
### Identitas Boolean Kunci
| Hukum | Rumus |
|-----|--------|
| Komutatifitas | p ∧ q = q ∧ p; p ∨ q = q ∨ p |
| Asosiatif | (p ∧ q) ∧ r = p ∧ (q ∧ r) |
| Distribusi | p ∧ (q ∨ r) = (p ∧ q) ∨ (p ∧ r) |
| Hukum De Morgan | ¬(p ∧ q) = ¬p ∨ ¬q; ¬(p ∨ q) = ¬p ∧ ¬q |
| Negasi Ganda | ¬(¬p) = p |
| Idempotensi | p ∧ p = p; p ∨ p = p |
| Penyerapan | p ∨ (p ∧ q) = p; p ∧ (p ∨ q) = p |
| Kontrapositif | (p → q) ≡ (¬q → ¬p) |
### Bentuk Biasa
| Formulir | Struktur | Kasus Penggunaan |
|------|-----------|----------|
| Bentuk Normal Konjungtif (CNF) | AND dari OR: (A∨B) ∧ (C∨D) | Pemecah SAT, pembuktian teorema resolusi |
| Bentuk Normal Disjungtif (DNF) | ATAU dari AND: (A∧B) ∨ (C∧D) | Desain sirkuit, sistem berbasis aturan |
**Mengonversi ke CNF:** Terapkan hukum De Morgan, distribusikan OR pada AND, hilangkan negasi ganda.
---

## Aritmatika dan Kesesuaian Modular
Aritmatika modular mempelajari bilangan bulat dengan operasi "sisa setelah pembagian". Ini penting untuk kriptografi, hashing, dan teori bilangan.
### Definisi Inti
| Konsep | Notasi | Definisi |
|---------|----------|------------|
| Kesesuaian | a ≡ b (mod n) | n membagi (a − b) |
| Kelas residu | [a]ₙ | Himpunan {a + kn : k ∈ ℤ} |
| Pembalikan modular | a⁻¹ mod n | Nilai x sedemikian rupa sehingga ax ≡ 1 (mod n) |
| Total Euler | φ(n) | Jumlah bilangan bulat dalam {1,...,n} koprima sampai n |
### Properti Utama
| Properti | Pernyataan |
|----------|----------|
| Tambahan | Jika a ≡ b dan c ≡ d (mod n), maka a+c ≡ b+d (mod n) |
| Perkalian | Jika a ≡ b dan c ≡ d (mod n), maka ac ≡ bd (mod n) |
| Teorema Kecil Fermat | Jika p bilangan prima dan gcd(a,p) = 1, maka aᵖ⁻¹ ≡ 1 (mod p) |
| Teorema Euler | Jika gcd(a,n) = 1, maka a^φ(n) ≡ 1 (mod n) |
| Teorema Sisa Cina | Jika gcd(m,n) = 1, sistem x ≡ a (mod m), x ≡ b (mod n) mempunyai solusi unik mod mn |
### Menghitung Jumlah Euler
Untuk n = p₁^a₁ · p₂^a₂ · ... · pₖ^aₖ (faktorisasi prima):
φ(n) = n · (1 − 1/p₁) · (1 − 1/p₂) · ... · (1 − 1/pₖ)
**Contoh:** φ(12) = 12 · (1 − 1/2) · (1 − 1/3) = 12 · 1/2 · 2/3 = 4. Memang benar, {1, 5, 7, 11} koprima dengan 12.
### Aplikasi: Kriptografi RSA (Ikhtisar)
1. Pilih bilangan prima besar p, q. Hitung n = pq, φ(n) = (p−1)(q−1).
2. Pilih e sehingga gcd(e, φ(n)) = 1 (eksponen publik).
3. Hitung d ≡ e⁻¹ (mod φ(n)) (eksponen hasil privat).
4. Enkripsi: c = mᵉ mod n. Dekripsi: m = cᵈ mod n.
5. Keamanan bergantung pada sulitnya memfaktorkan n untuk mencari p dan q.
---

## Induksi Matematika
**Induksi matematika** adalah teknik pembuktian utama untuk pernyataan tentang semua bilangan asli.
### Struktur Pembuktian dengan Induksi
1. **Kasus dasar:** Buktikan pernyataan untuk n = 0 (atau n = 1).
2. **Langkah induktif:** Asumsikan pernyataan tersebut berlaku untuk n = k (hipotesis induktif), lalu buktikan untuk n = k + 1.
### Varian
| Varian | Kapan Menggunakan |
|---------|-------------|
| Induksi sederhana | Buktikan P(k) → P(k+1) |
| Induksi kuat | Asumsikan P(0), P(1), ..., P(k) untuk membuktikan P(k+1) |
| Induksi struktural | Buktikan sifat-sifat struktur yang didefinisikan secara rekursif (pohon, rumus) |
| Induksi transfinit | Perluas induksi ke set yang tertata rapi di luar ℕ |
**Contoh Kerja (Induksi Kuat):** Buktikan setiap bilangan bulat n ≥ 2 dapat ditulis sebagai hasil kali bilangan prima.
- Basis: n = 2 adalah bilangan prima, jadi merupakan hasil kali bilangan prima (itu sendiri).
- Langkah induktif: Asumsikan benar untuk semua bilangan bulat dari 2 sampai k. Misalkan k+1.
  - Jika k+1 bilangan prima, selesai.
  - Jika k+1 komposit, k+1 = ab dimana 2 ≤ a, b ≤ k. Berdasarkan hipotesis induktif, a dan b adalah hasil kali bilangan prima, jadi k+1 adalah hasil kali bilangan prima.
---

## Relevansi dengan Pembelajaran Mesin dan Ilmu Data
| Konsep Matematika Diskrit | Aplikasi dalam ML / Ilmu Data |
|-----------------------|----------------------------------|
| Himpunan teori | Operasi basis data (SQL JOINs), manipulasi kumpulan fitur, kejadian probabilitas |
| Hubungan | Skema database, pemodelan hubungan entitas, grafik pengetahuan |
| Fungsi | Fungsi aktivasi, transformasi fitur, pemetaan antar spasi |
| Kombinatorik | Pemilihan fitur (memilih k dari n), ukuran pencarian grid hyperparameter |
| Prinsip lubang merpati | Tabrakan hashing, batas bawah kompresi, bukti teori informasi |
| Hubungan perulangan | Pemrograman dinamis, analisis kompleksitas algoritma, model deret waktu |
| Fungsi pembangkitan | Fungsi penghasil probabilitas, menyelesaikan masalah kombinatorial dalam rekayasa fitur |
| Nomor Katalan | Menghitung struktur pohon (pohon keputusan), mengurai ekspresi, operasi tumpukan |
| Teori graf (lihat file selanjutnya) | Analisis jaringan sosial, sistem rekomendasi, representasi pengetahuan |
---

## Ringkasan
| Topik | Ide Inti | Alat Kunci |
|-------|-----------|----------|
| Himpunan Teori | Koleksi objek yang berbeda | Aksioma ZFC, kardinalitas, operasi |
| Hubungan | Koneksi antar elemen | Hubungan ekuivalensi, orde parsial |
| Fungsi | Pemetaan antar set | Injektivitas, dugaantivitas, bijeksi |
| Kombinatorik | Pengaturan penghitungan | Koefisien binomial, prinsip merpati |
| Hubungan Perulangan | Urutan didefinisikan secara rekursif | Persamaan Karakteristik, Teorema Utama |
| Fungsi Pembangkit | Barisan sebagai deret pangkat | OGF/EGF, menyelesaikan perulangan secara aljabar |
Matematika diskrit menyediakan bahasa dan alat untuk berpikir tentang struktur yang terbatas atau dapat dihitung — yang merupakan hal yang dimanipulasi oleh komputer. Setiap algoritme, struktur data, kueri basis data, dan protokol kriptografi bertumpu pada fondasi yang berbeda. Penguasaan topik-topik ini mempertajam kemampuan pemecahan masalah dan memberikan kosakata untuk studi lanjutan dalam algoritma, teori kompleksitas, dan pembelajaran mesin.