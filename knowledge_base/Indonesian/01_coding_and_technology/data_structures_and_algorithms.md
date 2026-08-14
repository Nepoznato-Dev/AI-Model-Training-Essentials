---
# Metadata
title: "Data Structures and Algorithms"
description: "Arrays, trees, graphs, sorting, searching, complexity"
category: "Coding and Technology"
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
    date: "2026-08-05"
    author: "Nepoznato-Dev"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-05"
review_date: "2027-02-05"
reviewed_by: "Coding & Technology Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [data, structures, algorithms, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "6 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Struktur Data dan Algoritma
Struktur data adalah cara kita mengatur data dalam memori sehingga pengoperasiannya menjadi efisien. Algoritma adalah prosedur langkah demi langkah untuk memecahkan masalah. Bersama-sama, keduanya membentuk landasan ilmu komputer — setiap program yang pernah Anda gunakan bergantung pada keduanya. Memilih struktur data yang tepat dapat mengubah program yang sangat lambat menjadi program yang cepat, dan mengetahui algoritma yang tepat dapat mengubah masalah yang tidak terpecahkan menjadi masalah yang sepele.
---

## Struktur Data Dasar
### Struktur Linier
| Struktur | Akses | Cari | Sisipkan | Hapus | Kasus Penggunaan |
|-----------|--------|--------|--------|--------|----------|
| **Susunan** | O(1) berdasarkan indeks | PADA(n) | PADA(n) | PADA(n) | Koleksi berukuran tetap; akses acak |
| **Daftar Tertaut** | PADA(n) | PADA(n) | O(1) di kepala | O(1) di kepala | Ukuran dinamis; penyisipan/penghapusan |
| **Tumpukan** | PADA(n) | PADA(n) | O(1) tekan/letupkan | HAI(1) pop | Panggilan fungsi; membuka; penguraian |
| **Antrian** | PADA(n) | PADA(n) | O(1) antrian | O(1) dequeue | Penjadwalan tugas; sahabat; antrian pesan |
| **Dek** | O(1) di kedua ujungnya | PADA(n) | O(1) di kedua ujungnya | O(1) di kedua ujungnya | Jendela geser; mencuri pekerjaan |
### Struktur Berbasis Hash
| Struktur | Cari | Sisipkan | Hapus | Kasus Penggunaan |
|-----------|--------|--------|--------|----------|
| **Tabel Hash** | HAI(1) rata-rata | HAI(1) rata-rata | HAI(1) rata-rata | Pencarian nilai kunci; cache; set |
| **Kumpulan Hash** | HAI(1) | HAI(1) | HAI(1) | pengujian keanggotaan; deduplikasi |
**Tabrakan hash**: ketika dua kunci di-hash ke slot yang sama, kunci tersebut disimpan dalam daftar tertaut (rantai) atau slot berikutnya yang tersedia (pengalamatan terbuka). Fungsi hash yang baik meminimalkan tabrakan.
### Struktur Pohon
| Struktur | Cari | Sisipkan | Hapus | Kasus Penggunaan |
|-----------|--------|--------|--------|----------|
| **Pohon Pencarian Biner** | O(log n) rata-rata | HAI(log n) | HAI(log n) | data yang diurutkan; rentang pertanyaan |
| **AVL / Pohon Merah-Hitam** | O(log n) dijamin | HAI(log n) | HAI(log n) | Menyeimbangkan diri; digunakan dalam peta/set |
| **B-Pohon / B+ Pohon** | HAI(log n) | HAI(log n) | HAI(log n) | Indeks basis data; sistem file |
| **Uji** | O(k) dimana k = panjang kunci | Oke (k) | Oke (k) | Pelengkapan otomatis; pencocokan awalan |
| **Tumpukan (Biner)** | PADA(n) | HAI(log n) | HAI(log n) | Antrian prioritas; penjadwalan |
### Representasi Grafik
| Representasi | Ruang | Pencarian Tepi | Tambahkan Tepi | Ulangi Tetangga |
|---------------|-------|-------------|----------|-------------------|
| **Matriks ketetanggaan** | HAI(V²) | HAI(1) | HAI(1) | HAI(V) |
| **Daftar kedekatan** | HAI(V + E) | HAI(derajat) | HAI(1) | HAI(derajat) |
| **Daftar tepi** | HAI(E) | HAI(E) | HAI(1) | HAI(E) |
---

## Kompleksitas Algoritma (Big-O)
Notasi Big-O menggambarkan bagaimana kebutuhan waktu atau ruang suatu algoritma bertambah seiring dengan bertambahnya ukuran masukan.
| Kompleksitas | Nama | Contoh |
|-----------|------|---------|
| **O(1)** | Konstan | Pencarian tabel hash; akses array berdasarkan indeks |
| **O(log n)** | Logaritma | Pencarian biner; operasi pohon seimbang |
| **O(n)** | Linier | Pencarian linier; mengulangi array |
| **O(n log n)** | Linearitma | Gabungkan sortir; pengurutan tumpukan; jenis tujuan umum yang paling efisien |
| **O(n²)** | Kuadrat | semacam gelembung; loop bersarang pada data yang sama |
| **O(2^n)** | Eksponensial | Pembuatan subset brute force; Fibonacci rekursif naif |
| **O(n!)** | Faktorial | Penjual keliling (kekerasan); permutasi |
### Kesalahpahaman Umum
| Kesalahpahaman | Realitas |
|--------------|---------|
| "O(n) selalu lebih cepat dari O(n²)" | Untuk n kecil, faktor konstanta | lebih penting
| "Big-O Bawah selalu lebih baik" | Ada trade-off ruang-waktu; Pencarian O(1) menggunakan memori O(n) |
| "Big-O memberi tahu Anda kecepatan pastinya" | Ini menggambarkan tingkat pertumbuhan, bukan waktu absolut |
---

## Algoritma Penyortiran
| Algoritma | Terbaik | Rata-rata | Terburuk | Ruang | Stabil | Di Tempat |
|-----------|------|---------|-------|-------|--------|----------|
| **Urutkan Gelembung** | PADA(n) | HAI(n²) | HAI(n²) | HAI(1) | Ya | Ya |
| **Urutan Penyisipan** | PADA(n) | HAI(n²) | HAI(n²) | HAI(1) | Ya | Ya |
| **Urutan Seleksi** | HAI(n²) | HAI(n²) | HAI(n²) | HAI(1) | Tidak | Ya |
| **Gabungkan Urutkan** | HAI(n log n) | HAI(n log n) | HAI(n log n) | PADA(n) | Ya | Tidak |
| **Urutan Cepat** | HAI(n log n) | HAI(n log n) | HAI(n²) | HAI(log n) | Tidak | Ya |
| **Urutkan Tumpukan** | HAI(n log n) | HAI(n log n) | HAI(n log n) | HAI(1) | Tidak | Ya |
| **Pengurutan Tim** | PADA(n) | HAI(n log n) | HAI(n log n) | PADA(n) | Ya | Tidak |
**Saran praktis**: gunakan pengurutan bawaan bahasa Anda (`sorted()` Python,`Array.sort()`JavaScript). Mereka menggunakan algoritma yang sangat optimal (Tim Sort, Introsort) yang menangani semua kasus edge.
---

## Algoritma Pencarian
| Algoritma | Struktur Data | Kompleksitas | Persyaratan |
|-----------|---------------|-----------|-------------|
| **Penelusuran linier** | Apa saja | PADA(n) | Tidak ada |
| **Penelusuran biner** | Array yang diurutkan | HAI(log n) | Data harus diurutkan |
| **Pencarian tabel hash** | Tabel hash | HAI(1) rata-rata | Fungsi hash yang bagus |
| **BFS** (Pencarian Luas-Pertama) | Grafik / pohon | HAI(V + E) | Jalur terpendek tak berbobot |
| **DFS** (Pencarian Mendalam-Pertama) | Grafik / pohon | HAI(V + E) | Pencarian jalan; deteksi siklus |
| **Dijkstra** | Grafik berbobot | HAI((V + E) log V) | Bobot non-negatif; jalur terpendek |
| **A* Pencarian** | Grafik berbobot | HAI((V + E) log V) | Dipandu heuristik; optimal dengan heuristik yang dapat diterima |
---

## Pola Algoritma Kunci
| Pola | Deskripsi | Contoh Soal |
|---------|-------------|-----------------|
| **Membagi dan menaklukkan** | Membagi masalah menjadi submasalah; selesaikan secara rekursif; menggabungkan | Gabungkan sortir; penyortiran cepat; pencarian biner |
| **Pemrograman dinamis** | Memecah sub-masalah yang tumpang tindih; hasil cache | Fibonacci; ransel; barisan persekutuan terpanjang |
| **Serakah** | Buatlah pilihan optimal secara lokal di setiap langkah | Dijkstra; Pengkodean Huffman; pemilihan aktivitas |
| **Mundur** | Cobalah berbagai kemungkinan; membatalkan pilihan yang buruk; coba alternatif | Pemecah Sudoku; N-ratu; permutasi |
| **Jendela geser** | Pertahankan jendela elemen; geser ke seluruh data | Jumlah maksimum subarray ukuran K; substring terpanjang tanpa pengulangan |
| **Dua petunjuk** | Gunakan dua penunjuk yang bergerak ke arah satu sama lain atau ke arah yang sama | Pasangkan jumlah dalam array yang diurutkan; hapus duplikat |
| **Pencarian biner pada jawaban** | Pencarian biner ruang jawaban | Alokasikan halaman minimum; sapi agresif |
---

## Kapan Menggunakan Apa
| Masalah | Struktur Data | Algoritma |
|---------|---------------|-----------|
| Pencarian nilai kunci cepat | Tabel hash / kamus | Pencirian |
| Pertahankan urutan yang diurutkan | BST Seimbang (Peta Pohon, std::set) | Operasi pohon |
| Pemrosesan berbasis prioritas | Antrian tumpukan/prioritas | Operasi tumpukan |
| Jalur terpendek (tidak berbobot) | Grafik (daftar ketetanggaan) | BFS |
| Jalur terpendek (berbobot) | Grafik (daftar ketetanggaan) | Dijkstra / A* |
| Pengujian keanggotaan | Kumpulan hash / Filter Bloom | Pencirian |
| Pencocokan awalan | Coba | Coba traversal |
| Rentang kueri | Pohon ruas / Pohon Fenwick | Operasi pohon |
| cache LRU | Peta hash + daftar tertaut ganda | Operasi gabungan |
| Komponen yang terhubung | Persatuan Himpunan Terpisah (Union-Find) | Gabungkan dan Temukan |
---

## Ringkasan
Struktur data dan algoritme bukan sekadar topik wawancara — namun merupakan elemen penyusun perangkat lunak yang efisien. Array dan tabel hash menangani sebagian besar kebutuhan sehari-hari. Pohon dan grafik menangani data hierarki dan relasional. Penyortiran dan pencarian memecahkan masalah di perpustakaan standar. Pola algoritmik – membagi dan menaklukkan, pemrograman dinamis, serakah, mundur – adalah strategi yang dapat digunakan kembali untuk mengatasi masalah baru. Keterampilan kuncinya bukanlah menghafal algoritma; hal ini mengenali pola mana yang sesuai dengan masalah tertentu dan memilih struktur data yang tepat untuk pekerjaan tersebut.