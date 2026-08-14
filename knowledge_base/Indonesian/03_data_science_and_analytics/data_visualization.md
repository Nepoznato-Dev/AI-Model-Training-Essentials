---
# Metadata
title: "Data Visualization"
description: "Chart selection, design principles, storytelling, tools"
category: "Data Science and Analytics"
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
reviewed_by: "Data Science & Analytics Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [data, visualization, data-science-and-analytics]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "7 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Visualisasi Data
Bagan yang dirancang dengan baik dapat mengungkapkan pola yang disembunyikan oleh tabel angka. Desain yang buruk dapat menyesatkan, membingungkan, atau membosankan. Visualisasi data adalah keahlian mengubah data menjadi cerita visual yang menginformasikan keputusan. File ini mencakup pemilihan bagan, prinsip desain, kesalahan umum, dan alat yang memungkinkan semuanya terjadi.
---

## Memilih Grafik yang Tepat
Keputusan terpenting dalam visualisasi apa pun adalah memilih jenis bagan yang tepat untuk data dan pesan Anda.
### Panduan Pemilihan Bagan
| Tujuan Anda | Jenis Bagan Terbaik |
|-----------|-----------------|
| **Bandingkan kategori** | Bagan batang, bagan batang yang dikelompokkan |
| **Tampilkan perubahan seiring waktu** | Bagan garis, bagan area |
| **Tampilkan distribusi** | Histogram, plot kotak, plot biola |
| **Tunjukkan hubungan** | Plot sebar, bagan gelembung |
| **Tampilkan komposisi** | Batang bertumpuk, diagram lingkaran (bagian terbatas), peta pohon |
| **Tampilkan korelasi** | Plot sebar, peta panas, plot berpasangan |
| **Tampilkan peringkat** | Bagan batang horizontal |
| **Tampilkan pola geografis** | Peta Choropleth, peta titik |
| **Tampilkan bagian-ke-keseluruhan dari waktu ke waktu** | Bagan area bertumpuk |
### Kapan Menggunakan Setiap Bagan
| Bagan | Kekuatan | Hindari Saat |
|-------|-----------|-----------|
| **Batang** | Perbandingan yang jelas antar kategori | Terlalu banyak kategori (>15) |
| **Garis** | Tren dari waktu ke waktu; data berkelanjutan | Data tidak berurutan |
| **Menyebar** | Hubungan Dua Variabel | Terlalu banyak titik yang tumpang tindih |
| **Histogram** | Bentuk distribusi satu variabel | Ukuran sampel kecil (<20) |
| **Box plot** | Summary statistics + outliers; compare distributions | Audience unfamiliar with them |
| **Heatmap** | Correlation matrices; patterns in 2D data | Too many variables |
| **Pie chart** | Simple composition (2–5 slices) | More than 5 slices; precise comparisons needed |
| **Violin plot** | Distribution density + quartiles | Small audiences unfamiliar with them |
| **Pair plot** | Quick overview of all variable relationships | Many variables (>8) |
---

## Prinsip Desain
### Ide Inti Tufte
Prinsip Edward Tufte tetap menjadi standar emas untuk visualisasi data:
| Prinsip | Deskripsi |
|-----------|-------------|
| **Maksimalkan rasio tinta data** | Setiap tetes tinta harus menyampaikan data. Hapus semuanya. |
| **Hilangkan sampah grafik** | Tidak ada efek 3D, gradien serampangan, atau elemen dekoratif. |
| **Tampilkan datanya** | Jangan mendistorsi, menyembunyikan, atau memilih-milih. Biarkan data berbicara. |
| **Kelipatan kecil** | Gunakan bagan kecil berulang untuk perbandingan antar kategori. |
| **Garis Mini** | Bagan kecil seukuran kata untuk data tren sebaris. |
### Aturan Desain Praktis
| Aturan | Mengapa |
|------|-----|
| **Mulai sumbu y dari nol** (untuk diagram batang) | Jika tidak, Anda membesar-besarkan perbedaan |
| **Beri label secara langsung** | Letakkan label pada garis/batang daripada menggunakan legenda jika memungkinkan |
| **Gunakan warna dengan sengaja** | Soroti hal-hal yang penting; gunakan abu-abu untuk konteks |
| **Tetap sederhana** | Satu pesan per bagan; jangan membebani |
| **Gunakan skala yang konsisten** | Saat membandingkan grafik, pertahankan sumbu yang sama |
| **Pesan dengan penuh arti** | Urutkan batang berdasarkan nilai (bukan berdasarkan abjad) kecuali ada urutan alami |
| **Berikan konteks** | Tambahkan tolok ukur, target, atau rata-rata historis |
### Pedoman Warna
| Kasus Penggunaan | Pendekatan |
|----------|----------|
| **Kategoris** | Warna yang berbeda (biru, oranye, hijau, merah) — maksimal 7–8 kategori |
| **Berurutan** | Terang sampai gelap dengan satu rona (biru muda → biru tua) |
| **Divergen** | Gradien dua warna untuk data dengan titik tengah yang bermakna (merah ← putih → biru) |
| **Aksesibilitas** | Tes dengan simulator buta warna; jangan hanya mengandalkan warna (tambahkan label atau corak) |
---

## Bercerita dengan Data
Bagan tanpa narasi hanyalah sebuah gambar. Bercerita mengubah data menjadi wawasan.
### Kerangka Bercerita
1. **Konteks**: Bagaimana situasinya? Apa yang sudah diketahui penonton?
2. **Konflik**: Apa masalah, kejutan, atau ketegangan dalam data?
3. **Resolusi**: Apa yang harus dilakukan penonton dengan wawasan ini?
### Tip Praktis
| Kiat | Deskripsi |
|-----|-------------|
| **Memimpin dengan wawasan** | Beri judul bagan dengan kesimpulannya, bukan datanya ("Pendapatan tumbuh 30%" bukan "Pendapatan per Kuartal") |
| **Beri anotasi pada poin-poin penting** | Tambahkan keterangan teks untuk peristiwa penting atau titik balik |
| **Gunakan pengungkapan progresif** | Tampilkan satu grafik dalam satu waktu; membangun cerita langkah demi langkah |
| **Sorot hal yang penting** | Gunakan warna atau ukuran untuk menarik perhatian ke titik data utama |
| **Berikan "lalu apa?"** | Setiap bagan harus menjawab pertanyaan atau mendorong tindakan |
---

## Kesalahan Umum
| Kesalahan | Mengapa Ini Buruk | Perbaiki |
|---------|-------------|-----|
| **Sumbu y terpotong** | Membesar-besarkan perbedaan kecil | Mulai dari nol untuk diagram batang |
| **Rentang waktu memetik ceri** | Menyesatkan tentang tren | Tampilkan rangkaian lengkap yang tersedia |
| **Terlalu banyak warna** | Membanjiri pemirsa | Batasi hingga 5–7; gunakan abu-abu untuk konteks |
| **Sumbu y ganda** | Menyiratkan korelasi yang mungkin tidak ada | Gunakan dua bagan terpisah |
| **Bagan 3D** | Mendistorsi proporsi | Selalu gunakan 2D |
| **Diagram pai dengan 10+ irisan** | Tidak mungkin untuk membandingkan | Gunakan diagram batang sebagai gantinya |
| **Label tidak ada** | Pemirsa tidak dapat memahami bagan | Selalu beri label pada sumbu, judul, dan satuan |
| **Bagan area yang menyesatkan** | Area bertumpuk mendistorsi persepsi rangkaian individu | Gunakan diagram garis atau kelipatan kecil |
---

## Peralatan
### Piton
| Perpustakaan | Kekuatan |
|---------|----------|
| **matplotlib** | Landasan plot Python; sepenuhnya dapat disesuaikan |
| **lahir di laut** | Visualisasi statistik; default yang indah; dibangun di atas matplotlib |
| **secara plot** | Grafik interaktif berbasis web; dasbor |
| **altair** | Tata bahasa grafis deklaratif (Vega-Lite) |
| **bokeh** | Visualisasi interaktif untuk browser |
###JavaScript/Web
| Perpustakaan | Kekuatan |
|---------|----------|
| **D3.js** | Fleksibilitas maksimum; kurva belajar yang curam |
| **Bagan.js** | Bagan sederhana dan responsif |
| **Membuat grafik ulang** | Pembuatan bagan ramah reaksi |
| **Plot yang Dapat Diamati** | Tata bahasa grafis yang ringan dan ekspresif |
### Tanpa Kode / Alat BI
| Alat | Ketik |
|------|------|
| **Tabel** | Analisis visual standar industri |
| **Kekuatan BI** | ekosistem Microsoft; BI perusahaan |
| **Penampil** | Google Awan; eksplorasi data |
| **Metabase** | Sumber terbuka; pengaturan sederhana |
| **Superset Apache** | Sumber terbuka; SQL-asli |
---

## Desain Dasbor
Dasbor adalah kumpulan visualisasi yang bersama-sama menceritakan kisah lengkap tentang suatu proses, sistem, atau bisnis.
### Jenis Dasbor
| Ketik | Penonton | Tujuan |
|------|----------|---------|
| **Strategis** | Eksekutif | KPI tingkat tinggi; tren jangka panjang |
| **Operasional** | Manajer | Pemantauan waktu nyata; operasi sehari-hari |
| **Analitis** | Analis | Eksplorasi mendalam; pemfilteran, penelusuran |
### Daftar Periksa Desain
- **Kenali audiens Anda**: Keputusan apa yang akan mereka ambil dari dasbor ini?
- **Aturan 5 detik**: Bisakah intisari utama dipahami dalam 5 detik?
- **Tata Letak**: Metrik terpenting di kiri atas (tempat pertama kali dilihat).
- **Batasi jenis bagan**: maks 3–4 jenis per dasbor untuk konsistensi.
- **Interaktif secara default**: Filter, pemilih rentang tanggal, penelusuran.
- **Kinerja**: Dasbor yang memuat >5 detik tidak akan digunakan.
- **Seluler**: Pertimbangkan desain responsif jika pengguna membutuhkannya saat bepergian.
---

## Ringkasan
Visualisasi data yang baik adalah tentang kejelasan, kejujuran, dan dampak. Pilih bagan yang tepat untuk data Anda. Hapus semua yang tidak sesuai dengan pesan. Gunakan warna dan anotasi untuk memandu pemirsa. Dan selalu, biarkan data menceritakan kisahnya — bukan sebaliknya.