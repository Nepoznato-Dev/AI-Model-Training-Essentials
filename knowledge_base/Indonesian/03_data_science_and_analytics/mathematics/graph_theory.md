<!--
---
# Metadata
title: "Graph Theory"
description: "Graph representations, trees, traversals, shortest paths, minimum spanning trees, network flows, and spectral graph theory"
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
    changes: "Initial deep-dive into graph theory"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2027-02-10"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-10"

# Classification
tags: [graph-theory, trees, traversals, shortest-paths, spanning-trees, network-flows, spectral-graph-theory]
difficulty_level: "intermediate"
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
# Teori Grafik
**Grafik** adalah struktur matematika yang terdiri dari simpul (node) yang dihubungkan oleh sisi (link). Hubungan model grafik: jaringan sosial, peta jalan, jaringan saraf, ketergantungan, saluran komunikasi. Teori grafik — studi tentang struktur ini — menyediakan algoritme dan teorema yang penting bagi ilmu komputer, riset operasi, dan ilmu data.
---

## Konsep Dasar
### Definisi
| Istilah | Definisi | Notasi |
|------|------------|----------|
| **Grafik** | Sepasang G = (V, E) dari simpul dan sisi | G |
| **Simpul (simpul)** | Sebuah elemen dari V | v, kamu, w |
| **Tepi** | Koneksi antara dua simpul | e = (u, v) atau {u, v} |
| **Pesan** | Jumlah simpul | \|V\| = n |
| **Ukuran** | Jumlah tepi | \|E\| = m |
| **Gelar** | Banyaknya sisi yang bersisian dengan suatu simpul | derajat(v) |
| **Jalur** | Barisan simpul berbeda yang dihubungkan oleh sisi | v₁, v₂, ..., vₖ |
| **Siklus** | Lintasan yang bermula dan berakhir pada titik yang sama | v₁ → v₂ → ... → vₖ → v₁ |
| **Terhubung** | Terdapat jalur di antara setiap pasangan simpul | — |
| **Komponen** | Subgraf terhubung maksimal | — |
| **Subgraf** | Graf yang terbentuk dari himpunan bagian V dan E | H ⊆ G |
### Jenis Grafik
| Ketik | Deskripsi | Contoh |
|------|-------------|---------|
| **Tidak terarah** | Tepi tidak memiliki arah | Jaringan persahabatan |
| **Sutradara (digraf)** | Tepinya mempunyai arah (busur) | Tautan halaman web |
| **Berbobot** | Tepi membawa nilai numerik | Jarak jalan |
| **Tidak tertimbang** | Semua sisinya setara | Koneksi sosial |
| **Sederhana** | Tanpa loop, tanpa banyak sisi | Kebanyakan grafik buku teks |
| **Multigraf** | Banyak sisi di antara simpul yang sama diperbolehkan | Rute penerbangan (beberapa penerbangan antar kota) |
| **Lengkap** | Setiap pasangan simpul terhubung | Kₙ memiliki n(n−1)/2 sisi |
| **Bipartit** | Simpul dibagi menjadi dua kelompok; tepinya hanya melintasi kelompok | Matriks rekomendasi item pengguna |
| **Bidang** | Dapat ditarik tanpa persilangan tepi | Tata letak papan sirkuit |
| **Pohon** | Terhubung, grafik asiklik | Pohon keputusan, sistem file |
| **DAG** | Terarah, tidak ada siklus terarah | Penjadwalan tugas, grafik ketergantungan |
### Lemma Jabat Tangan
Jumlah semua derajat titik sudut sama dengan dua kali jumlah sisinya:
derajat(v) = 2|E|
**Akibat:** Setiap graf mempunyai jumlah simpul berderajat ganjil yang jumlahnya genap.
**Contoh:** Dalam sebuah pesta yang terdiri dari 10 orang yang setiap orangnya berjabat tangan dengan tepat 3 orang lainnya: Σ deg = 30, jadi |E| = total 15 jabat tangan.
---

## Representasi Grafik
Cara Anda menyimpan grafik di memori menentukan efisiensi setiap algoritme yang Anda jalankan di dalamnya.
| Representasi | Ruang | Pencarian Tepi | Ulangi Tetangga | Terbaik Untuk |
|----------------|-------|-------------|--------------------|----------|
| **Matriks Kedekatan** | HAI(n²) | HAI(1) | PADA(n) | Grafik padat, pengujian tepi cepat |
| **Daftar Kedekatan** | HAI(n + m) | O(derajat(v)) | O(derajat(v)) | Grafik jarang, sebagian besar jaringan dunia nyata |
| **Daftar Tepi** | HAI(m) | HAI(m) | HAI(m) | Algoritma sederhana, MST Kruskal |
| **Matriks Insiden** | HAI(n · m) | HAI(m) | HAI(m) | Algoritma khusus |
### Matriks Ketetanggaan
Matriks n × n A dengan A[i][j] = 1 jika sisi (i,j) ada, 0 jika tidak. Untuk graf berbobot, A[i][j] = bobot.
**Properti:**
- Simetris untuk grafik tidak berarah
- Aᵏ[i][j] = jumlah jalan kaki dengan panjang k dari i ke j
- Nilai Eigen dari A mengungkapkan sifat struktural (lihat Teori Grafik Spektral)
### Daftar Kedekatan
Sebuah array (atau peta hash) di mana setiap simpul v menyimpan daftar tetangganya.
```
Vertex 0: [1, 3]
Vertex 1: [0, 2, 3]
Vertex 2: [1, 3]
Vertex 3: [0, 1, 2]
```

Ini adalah representasi paling umum untuk grafik dunia nyata, yang biasanya renggang (m ≪ n²).
---

## Pohon
**pohon** adalah graf tak berarah asiklik yang terhubung. **Hutan** adalah kumpulan pepohonan yang terpisah-pisah.
### Properti Pohon
Untuk pohon dengan n simpul:
- Ia mempunyai tepat n − 1 sisi
- Terdapat tepat satu jalur antara dua simpul mana pun
- Menghapus tepi mana pun akan memutusnya
- Menambahkan tepi mana pun akan menghasilkan tepat satu siklus
### Jenis Pohon
| Ketik | Deskripsi | Aplikasi |
|------|-------------|-------------|
| **Pohon berakar** | Satu simpul ditunjuk sebagai root | Sistem file, bagan organisasi |
| **Pohon biner** | Setiap node memiliki paling banyak 2 anak | BST, penguraian ekspresi, pohon keputusan |
| **Pohon seimbang** | Tingginya adalah O(log n) | Pohon AVL, pohon merah-hitam (database) |
| **Pohon merentang** | Subgraf yang mencakup semua simpul dan merupakan pohon | Desain jaringan, algoritma perkiraan |
| **Pohon rentang minimum** | Spanning tree dengan total bobot tepi minimum | Desain jaringan, pengelompokan |
| **Grafik bintang** | Satu node pusat terhubung ke node lainnya | Jaringan hub-and-spoke |
### Properti Pohon Biner
| Properti | Rumus |
|----------|---------|
| Node maksimum pada kedalaman d | 2ᵈ |
| Node maksimum di pohon dengan tinggi h | 2ʰ⁺¹ − 1 |
| Tinggi minimum untuk n node | ⌊log₂(n)⌋ |
| Node daun dalam pohon biner penuh | Node internal + 1 |
### Penjelajahan Pohon
| melintasi | Pesan | Kasus Penggunaan |
|-----------|-------|----------|
| **Pemesanan di muka** | Akar → Kiri → Kanan | Menyalin pohon, ekspresi awalan |
| **Sesuai pesanan** | Kiri → Akar → Kanan | Keluaran yang diurutkan dari BST |
| **Pasca-pemesanan** | Kiri → Kanan → Akar | Menghapus pohon, ekspresi postfix |
| **Urutan tingkat (BFS)** | Tingkat demi tingkat, kiri ke kanan | Jalur terpendek pada pohon tak berbobot |
---

## Penjelajahan Grafik
Algoritme traversal mengunjungi setiap titik yang dapat dijangkau secara sistematis.
### Pencarian Luas-Pertama (BFS)
Menjelajahi simpul lapis demi lapis, menggunakan **antrian**.
| Properti | Nilai |
|----------|-------|
| Struktur data | Antrian (FIFO) |
| Kompleksitas waktu | HAI(V + E) |
| Kompleksitas ruang | HAI(V) |
| Menemukan jalur terpendek? | Ya (grafik tidak berbobot) |
| Menyelesaikan? | Ya (menjelajahi semua simpul yang dapat dijangkau) |
**Algoritma:**
1. Mulai dari titik sumber s. Markus dikunjungi. Entri s.
2. Saat antrian tidak kosong: dequeue vertex u. Untuk setiap tetangga v dari u yang belum dikunjungi: tandai v telah dikunjungi, enqueue v.
**Aplikasi:** jalur terpendek dalam grafik tidak berbobot, komponen terhubung, pengujian bipartit, perayapan web.
### Pencarian Kedalaman-Pertama (DFS)
Menjelajahi sedalam mungkin sebelum menelusuri kembali, menggunakan **tumpukan** (atau rekursi).
| Properti | Nilai |
|----------|-------|
| Struktur data | Stack (LIFO) / rekursi |
| Kompleksitas waktu | HAI(V + E) |
| Kompleksitas ruang | HAI(V) |
| Menemukan jalur terpendek? | Tidak |
| Menyelesaikan? | Ya (untuk graf berhingga) |
**Algoritma:**
1. Mulai dari titik s. Markus dikunjungi.
2. Untuk setiap tetangga yang belum dikunjungi v dari s: DFS secara rekursif dari v.
**DFS mengklasifikasikan edge menjadi:**
- **Tepi pohon:** bagian dari pohon DFS
- **Tepi belakang:** menghubungkan sebuah simpul ke leluhurnya (tunjukkan siklus)
- **Tepi depan:** menghubungkan sebuah simpul ke turunannya
- **Silang tepi:** menghubungkan simpul di cabang yang berbeda
**Aplikasi:** penyortiran topologi, deteksi siklus, komponen yang terhubung kuat, penyelesaian labirin.
### Perbandingan BFS vs DFS
| Kriteria | BFS | DFS |
|-----------|-----|-----|
| Strategi | Lebar lalu dalam | Dalam lalu lebar |
| Memori | Lebih Tinggi (Perbatasan Toko) | Lebih rendah (jalur toko) |
| Jalur terpendek (tidak berbobot) | Dijamin | Tidak dijamin |
| Gunakan ketika solusi hampir dimulai | Lebih baik | Lebih buruk |
| Gunakan ketika grafik sangat dalam | Lebih buruk | Lebih baik |
| Penyortiran topologi | Varian algoritma Kahn | Pendekatan standar |
---

## Algoritma Jalur Terpendek
Menemukan jalur terpendek antar simpul adalah salah satu masalah graf yang paling penting secara praktis.
### Algoritma Dijkstra
Menemukan jalur terpendek dari satu sumber ke semua simpul lainnya dalam grafik dengan bobot tepi **non-negatif**.
| Properti | Nilai |
|----------|-------|
| Bobot tepi | Harus ≥ 0 |
| Waktu (tumpukan biner) | HAI((V + E) log V) |
| Waktu (tumpukan Fibonacci) | HAI(E + V log V) |
| Tamak? | Ya |
| Menangani bobot negatif? | Tidak |
**Algoritma:**
1. Inisialisasi dist[s] = 0, dist[v] = ∞ untuk semua v ≠ s. Antrian prioritas Q dengan semua simpul.
2. Ketika Q tidak kosong: ekstrak simpul u dengan dist minimum. Untuk setiap tetangga v dari u dengan bobot tepi w: jika dist[u] + w < dist[v], perbarui dist[v] = dist[u] + w.
**Contoh Pekerjaan:**```
Graph: A --1-- B --2-- C --1-- D
       A --4-- C
       B --1-- D

Shortest paths from A:
A → B: 1 (direct)
A → D: 2 (A→B→D)
A → C: 3 (A→B→C, NOT A→C=4)
```

### Algoritma Bellman-Ford
Menangani bobot tepi **negatif** dan mendeteksi siklus negatif.
| Properti | Nilai |
|----------|-------|
| Bobot tepi | Any (mendeteksi siklus negatif) |
| Kompleksitas waktu | HAI(V·E) |
| Kompleksitas ruang | HAI(V) |
| Menangani siklus negatif? | Ya (mendeteksi dan melaporkan) |
**Algoritma:**
1. Inisialisasi dist[s] = 0, dist[v] = ∞ untuk semua v ≠ s.
2. Ulangi V − 1 kali: untuk setiap sisi (u, v) dengan bobot w: jika dist[u] + w < dist[v], perbarui dist[v].
3. Periksa siklus negatif: jika ada sisi yang masih bisa dilonggarkan, berarti ada siklus negatif.
### Algoritma Floyd-Warshall
Menemukan jalur terpendek antara **semua pasangan** simpul.
| Properti | Nilai |
|----------|-------|
| Kompleksitas waktu | HAI(V³) |
| Kompleksitas ruang | HAI(V²) |
| Menangani bobot negatif? | Ya (tapi bukan siklus negatif) |
| Pendekatan | Pemrograman dinamis |
**Pengulangan:** dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]) untuk setiap simpul perantara k.
### Panduan Pemilihan Algoritma
| Skenario | Algoritma |
|----------|-----------|
| Sumber tunggal, bobot non-negatif | Dijkstra |
| Sumber tunggal, kemungkinan bobot negatif | Bellman-Ford |
| Semua pasangan, grafik padat | Floyd-Warshall |
| Semua berpasangan, grafik jarang | Jalankan Dijkstra dari setiap simpul |
| Grafik tak berbobot | BFS |
| DAG (tanpa siklus) | Pengurutan topologi + relaksasi |
| A* (dipandu heuristik) | Pencarian A* (untuk pencarian jalan dengan heuristik yang baik) |
---

## Pohon Rentang Minimum
**pohon rentang minimum (MST)** menghubungkan semua simpul dengan total bobot tepi minimum.
### Properti
- Sebuah MST mempunyai tepat n − 1 sisi (untuk n simpul)
- MST ada jika grafik terhubung
- Grafik dengan bobot tepi berbeda memiliki MST unik
- MST memenuhi **properti potongan**: tepi berbobot minimum yang melintasi setiap potongan adalah milik MST
- MST memenuhi **properti siklus**: tepi bobot maksimum dalam siklus apa pun bukan milik MST
### Algoritma Kruskal
| Properti | Nilai |
|----------|-------|
| Strategi | Serakah — tambahkan tepian sesuai urutan berat |
| Struktur data | Disjoint-set (union-find) |
| Kompleksitas waktu | HAI(E log E) |
| Terbaik untuk | Grafik jarang |
**Algoritma:**
1. Urutkan semua sisi berdasarkan beratnya.
2. Untuk setiap sisi (secara berurutan): jika menambahkannya tidak membuat siklus (periksa dengan union-find), tambahkan ke MST.
3. Berhenti ketika n − 1 sisi dipilih.
### Algoritma Prim
| Properti | Nilai |
|----------|-------|
| Strategi | Serakah — menumbuhkan pohon dari titik awal |
| Struktur data | Antrian prioritas (min-heap) |
| Kompleksitas waktu | O(E log V) dengan tumpukan biner |
| Terbaik untuk | Grafik padat |
**Algoritma:**
1. Mulai dari titik mana pun. Tandai sebagai bagian dari MST.
2. Tambahkan berulang kali tepi berbobot minimum yang menghubungkan sebuah simpul di MST ke simpul di luarnya.
3. Berhenti ketika semua simpul sudah disertakan.
### Aplikasi MST
| Aplikasi | Bagaimana MST Membantu |
|-------------|---------------|
| Desain jaringan | Letakkan kabel/pipa minimum untuk menghubungkan semua lokasi |
| Pengelompokan | Hapus k − 1 tepi MST terpanjang untuk mendapatkan k cluster |
| Algoritma perkiraan | 2-perkiraan untuk metrik TSP |
| Segmentasi gambar | Kelompokkan piksel berdasarkan MST kesamaan warna |
| Penghapusan fitur | Hapus fitur yang berlebihan menggunakan MST grafik korelasi |
---

## Aliran Jaringan
Masalah aliran jaringan memodelkan pergerakan sumber daya melalui suatu sistem.
### Definisi Jaringan Aliran
**Jaringan aliran** adalah grafik berarah dengan:
- Simpul **sumber** (menghasilkan aliran)
- Titik **sink** t (memakan aliran)
- **Kapasitas** c(u,v) ≥ 0 pada setiap sisi
- **Aliran** f(u,v) memuaskan:
  - **Batasan kapasitas:** 0 ≤ f(u,v) ≤ c(u,v)
  - **Konservasi aliran:** aliran masuk = aliran keluar pada setiap titik kecuali s dan t
### Masalah Aliran Maksimum
Tentukan aliran total maksimum dari s ke t.
**Metode Ford-Fulkerson:**
1. Meskipun terdapat jalur augmentasi dari s ke t pada grafik sisa:
2. Temukan kapasitas kemacetan di sepanjang jalur
3. Meningkatkan aliran sepanjang jalur sebesar jumlah kemacetan
4. Perbarui kapasitas sisa
| Algoritma | Kompleksitas Waktu | Catatan |
|-----------|----------------|-------|
| Ford-Fulkerson (DFS) | O(m · f*) dimana f* adalah aliran maks | Tidak boleh berakhir dengan kapasitas yang tidak rasional |
| Edmonds-Karp (BFS) | HAI(V · E²) | Selalu berakhir, pilih jalur augmentasi terpendek |
| Algoritma Dinic | HAI(V² · E) | Menggunakan aliran pemblokiran; O(V^(1/2) · E) untuk kapasitas satuan |
### Teorema Min-Cut Aliran Maks
**Aliran maksimum** dari s ke t sama dengan **kapasitas pemotongan minimum** yang memisahkan s dari t.
A **cut** (S, T) mempartisi simpul menjadi S (mengandung s) dan T (mengandung t). Kapasitas potong adalah jumlah kapasitas tepi dari S ke T.
**Aplikasi aliran maksimal:**
- Pencocokan bipartit (menetapkan pekerja pada suatu pekerjaan)
- Segmentasi gambar (memisahkan latar depan dari latar belakang)
- Eliminasi baseball (apakah tim X masih bisa menang?)
- Keandalan jaringan (throughput data maksimum)
### Pencocokan Bipartit melalui Max Flow
Diberikan graf bipartit G = (L ∪ R, E):
1. Tambahkan sumber s dengan tepi ke semua simpul di L (kapasitas 1)
2. Tambahkan sink t dengan tepi dari semua simpul di R (kapasitas 1)
3. Atur semua kapasitas tepi asli ke 1
4. Aliran maksimum = pencocokan maksimum
---

## Teori Grafik Spektral
Teori grafik spektral mempelajari grafik melalui nilai eigen dan vektor eigen matriks yang terkait dengan grafik tersebut.
### Matriks Kunci
| Matriks | Definisi | Apa yang Ditangkapnya |
|--------|------------|------------------|
| **Matriks ketetanggaan** A | A[i][j] = 1 jika tepi (i,j) ada | Pola konektivitas |
| **Matriks derajat** D | Diagonal; D[i][i] = derajat(i) | Pentingnya simpul menurut derajat |
| **Laplacian** L = D − A | L[i][j] = −1 jika rusuk, derajat(i) pada diagonal | Kelancaran fungsi pada grafik |
| **Laplacian yang dinormalisasi** L_norm = D^(−1/2) LD^(−1/2) | Versi skala-invarian | Struktur komunitas |
### Nilai Eigen dari Laplacian
Laplacian L bersifat semi pasti positif, sehingga semua nilai eigennya ≥ 0.
| Nilai eigen | Arti |
|------------|---------|
| λ₁ = 0 | Selalu nol; vektor eigen adalah vektor konstanta |
| λ₂ (konektivitas aljabar) | > 0 grafik iff terhubung; lebih besar = lebih terhubung |
| Jumlah nilai eigen nol | Sama dengan jumlah komponen yang terhubung |
| λₙ | Terkait dengan derajat maksimum dan pemuaian grafik |
### Penerapan Metode Spektral
| Aplikasi | Metode |
|-------------|--------|
| **Partisi grafik** | Gunakan vektor eigen dari L untuk membagi grafik menjadi bagian-bagian yang seimbang |
| **Deteksi komunitas** | Pengelompokan spektral: sematkan simpul menggunakan vektor eigen bawah, lalu klaster |
| **Peringkat Halaman** | Vektor eigen dari matriks ketetanggaan (atau matriks transisi) dari grafik web |
| **Gambar grafik** | Posisikan simpul menggunakan vektor eigen dari Laplacian |
| **Pembelajaran semi-supervisi** | Perbanyak label menggunakan grafik Laplacian (propagasi label) |
| **Grafik jaringan saraf** | Konvolusi spektral: memfilter sinyal pada grafik menggunakan vektor eigen L |
### Ketimpangan Cheeger
Mengaitkan nilai eigen kedua λ₂ dengan **ekspansi** grafik (seberapa baik keterhubungannya):
λ₂ / 2 ≤ h(G) ≤ √(2λ₂)
dimana h(G) adalah konstanta Cheeger (bilangan isoperimetri). Artinya, λ₂ kira-kira mengukur seberapa sulitnya memotong grafik menjadi dua bagian — sebuah wawasan penting untuk pengelompokan.
---

## Struktur Grafik Khusus
| Grafik | simpul | Tepi | Properti |
|-------|----------|-------|------------|
| Lengkapi Kₙ | n | n(n−1)/2 | Setiap pasangan terhubung; diameter 1 |
| Siklus Cₙ | n | n | 2-reguler; terhubung |
| Jalur Pₙ | n | n−1 | Pohon; diameter n−1 |
| Hypercube Qₖ | 2ᵏ | k·2ᵏ⁻¹ | k-reguler; diameter k; bipartit |
| Lengkapi bipartit K_{m,n} | m+n | m·n | Setiap titik di satu bagian terhubung ke semua bagian lainnya |
| Grafik Petersen | 10 | 15 | 3-reguler; diameter 2; tidak datar; tidak ada siklus Hamilton |
---

## Relevansi dengan Pembelajaran Mesin dan Ilmu Data
| Konsep Grafik | Aplikasi |
|---------------|-------------|
| BFS / DFS | Perayapan web, analisis jaringan sosial, pelabelan komponen terhubung |
| Dijkstra / A* | Perencanaan rute, pencarian jalur AI game, navigasi robotika |
| Pohon rentang minimum | Clustering (single-linkage), pemilihan fitur, desain jaringan |
| Aliran maks / pemotongan min | Segmentasi gambar, pencocokan bipartit, penetapan rekomendasi |
| Metode spektral | Pengelompokan spektral, jaringan saraf grafik, reduksi dimensi (Laplacian eigenmaps) |
| Peringkat Halaman | Peringkat mesin pencari, analisis pengaruh di jejaring sosial |
| DAG | Jaringan Bayesian, inferensi kausal, penjadwalan tugas, grafik komputasi dalam pembelajaran mendalam |
| Grafik bipartit | Matriks item pengguna dalam sistem pemberi rekomendasi, pasar dua sisi |
| Struktur pohon | Pohon keputusan, hutan acak, pengelompokan hierarki, navigasi sistem file |
| Representasi grafik | Grafik pengetahuan (Wikidata, DBpedia), grafik molekuler (penemuan obat), jaringan kutipan |
---

## Ringkasan
| Topik | Ide Inti | Algoritma / Hasil Kunci |
|-------|-----------|----------------------|
| Dasar | Simpul, tepi, derajat, jalur | Lemma jabat tangan |
| Representasi | Cara menyimpan grafik | Matriks ketetanggaan vs daftar ketetanggaan |
| Pohon | Grafik asiklik terhubung | n simpul → n−1 sisi |
| Traversal | Eksplorasi titik sistematis | BFS (jalur terpendek), DFS (eksplorasi mendalam) |
| Jalur Terpendek | Rute dengan berat minimum | Dijkstra, Bellman-Ford, Floyd-Warshall |
| Pohon Rentang Minimum | Cara termurah untuk menghubungkan semua simpul | Kruskal, Prim |
| Aliran Jaringan | Throughput maksimum | Ford-Fulkerson, teorema min-cut aliran maks |
| Teori Spektral | Nilai eigen mengungkapkan struktur | Nilai eigen Laplacian, pengelompokan spektral |
Teori grafik bisa dibilang merupakan cabang matematika yang paling dapat diterapkan secara langsung pada ilmu data modern. Jejaring sosial, grafik pengetahuan, struktur molekul, grafik komputasi dalam kerangka pembelajaran mendalam, resolusi ketergantungan, sistem rekomendasi — semuanya pada dasarnya adalah masalah grafik. Algoritme yang dibahas di sini tidak hanya bersifat teoretis; mereka dijalankan dalam skala besar dalam sistem produksi setiap hari.