---
# Metadata
title: "Genetics and Genomics"
description: "DNA, gene expression, CRISPR, GWAS, sequencing technologies"
category: "Natural Sciences"
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
    date: "2026-08-05"
    author: "AI Model Training Team"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-05"
review_date: "2027-02-05"
reviewed_by: "Natural Sciences Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [genetics, genomics, natural-sciences]
difficulty_level: "beginner"
prerequisites: []
estimated_reading_time: "6 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Genetika dan Genomik
Genetika adalah studi tentang keturunan - bagaimana sifat-sifat diturunkan dari orang tua ke keturunannya melalui DNA. Genomik adalah studi tentang keseluruhan genom: semua gen, wilayah non-pengkode, cara interaksinya, dan variasinya antar individu dan populasi. Transisi dari genetika ke genomik didorong oleh teknologi pengurutan — kami beralih dari mempelajari satu gen pada satu waktu hingga membaca seluruh genom dalam hitungan jam, menghasilkan data yang mengubah bidang kedokteran, pertanian, forensik, dan pemahaman kita tentang evolusi.
---

## Dasar-Dasar DNA
### Struktur DNA
| Komponen | Deskripsi |
|-----------|-------------|
| **Nukleotida** | Bahan penyusun DNA; terdiri dari gula (deoksiribosa), gugus fosfat, dan basa nitrogen |
| **Basis** | Adenin (A), Timin (T), Guanin (G), Sitosin (C) |
| **Pemasangan basa** | A berpasangan dengan T (2 ikatan hidrogen); G berpasangan dengan C (3 ikatan hidrogen) |
| **Heliks ganda** | Dua helai berjalan anti-paralel (5' hingga 3' dan 3' hingga 5'); dipelintir menjadi heliks |
| **Kromosom** | Molekul DNA tunggal yang panjang melilit protein histon; manusia mempunyai 46 (23 pasang) |
| **Genom** | Kumpulan lengkap DNA dalam suatu organisme; genom manusia ~3,2 miliar pasangan basa |
### Dogma Sentral Biologi Molekuler
| Langkah | Proses | Lokasi | Produk |
|------|---------|----------|---------|
| **Replikasi** | DNA → DNA | Inti | Dua molekul DNA identik |
| **Transkripsi** | DNA → mRNA | Inti | RNA pembawa pesan |
| **Terjemahan** | mRNA → protein | Ribosom (sitoplasma) | Rantai polipeptida (protein) |
---

## Ekspresi Gen
### Bagaimana Gen Diatur
| Tingkat | Mekanisme | Contoh |
|-------|-----------|---------|
| **Epigenetik** | Metilasi DNA; modifikasi histon; remodeling kromatin | Membungkam satu kromosom X pada wanita |
| **Transkripsi** | Faktor transkripsi mengikat promotor/peningkat; aktifkan atau tekan | Lac operon pada bakteri; gen yang responsif terhadap hormon |
| **Pasca-transkripsi** | Penyambungan alternatif; stabilitas mRNA; mikroRNA | Satu gen → banyak varian protein |
| **Terjemahan** | Ketersediaan ribosom; regulasi faktor inisiasi | Regulasi zat besi melalui feritin mRNA |
| **Pasca-translasi** | Modifikasi protein (fosforilasi, ubiquitinasi); degradasi | Kontrol siklus sel |
---

## Pola Warisan
### Genetika Mendel
| Pola | Deskripsi | Contoh |
|---------|-------------|---------|
| **Dominan autosomal** | Satu salinan alel sudah cukup | penyakit Huntington; akondroplasia |
| **Resesif autosomal** | Diperlukan dua salinan | Fibrosis kistik; anemia sel sabit |
| **Dominan terkait X** | Gen pada kromosom X; satu salinan cukup | Sindrom Rett |
| **Resesif terkait X** | Gen pada kromosom X; laki-laki lebih terpengaruh | Penyakit darah; buta warna |
| **Kodominan** | Kedua alel dinyatakan sama | Golongan darah ABO (A dan B) |
| **Dominasi tidak lengkap** | Heterozigot adalah perantara | Bunga berwarna merah muda dari induk merah putih |
| **Poligenik** | Banyak gen berkontribusi pada satu sifat | Tinggi; warna kulit; intelijen |
| **Pleiotropi** | Satu gen mempengaruhi banyak sifat | Sindrom Marfan (jaringan ikat, mata, jantung) |
---

## Genomik
### Jenis Genomik
| Ketik | Fokus | Aplikasi |
|------|-------|-------------|
| **Genomik struktural** | Struktur 3D semua protein dalam genom | desain obat; rekayasa protein |
| **Genomik fungsional** | Apa yang dilakukan gen; interaksi gen; pola ekspresi | Memahami mekanisme penyakit |
| **Genomik komparatif** | Membandingkan genom antar spesies | Hubungan evolusioner; mengidentifikasi kawasan konservasi |
| **Metagenomics** | DNA dari sampel lingkungan (tidak dikultur) | Studi mikrobioma; menemukan organisme baru |
| **Farmakogenomik** | Bagaimana gen mempengaruhi respon obat | Obat yang dipersonalisasi; dosis obat |
| **Epigenomics** | Modifikasi epigenetik seluruh genom | diagnosis kanker; biologi perkembangan |
### Teknologi Pengurutan DNA
| Generasi | Teknologi | Baca Panjang | Keluaran | Fitur Utama |
|-----------|-----------|-------------|------------|-------------|
| **Generasi pertama** | Urutan sanger | ~1.000bp | Rendah | Akurasi standar emas; digunakan untuk validasi |
| **Generasi kedua** | Iluminasi (Solexa) | 50–300bp | Sangat tinggi | Bacaan singkat; platform dominan; biaya rendah per basis |
| **Generasi kedua** | Torn Ion | 200–400bp | Tinggi | Berbasis semikonduktor; tidak ada optik |
| **Generasi ketiga** | PacBio (SMRT) | 10.000–100.000bp | Sedang | Bacaan panjang; menyelesaikan wilayah yang berulang |
| **Generasi ketiga** | Oxford Nanopori | Hingga jutaan bp | Sedang hingga tinggi | Bacaan yang sangat panjang; portabel (Mion); waktu nyata |
---

## Variasi Genetik
### Jenis Variasi
| Ketik | Deskripsi | Frekuensi |
|------|-------------|-----------|
| **SNP** (Polimorfisme Nukleotida Tunggal) | Perubahan basis tunggal | Paling umum; ~1 dalam 1.000 pangkalan |
| **Penyisipan / Penghapusan (indel)** | Penambahan atau penghapusan pangkalan | Dapat menyebabkan mutasi frameshift |
| **CNV** (Variasi Nomor Salinan) | Segmen yang diduplikasi atau dihapus (1 kb – beberapa Mb) | Berkontribusi pada penyakit dan evolusi |
| **Variasi struktural** | Inversi; translokasi; penataan ulang besar | Kurang umum; bisa bersifat patogen |
| **Mikrosatelit (STR)** | Pengulangan tandem pendek (pengulangan 2–6 bp) | Forensik; pengujian garis ayah |
### GWAS (Studi Asosiasi Seluruh Genom)
| Langkah | Deskripsi |
|------|-------------|
| **1. Kumpulkan sampel** | Kasus (dengan penyakit) dan kontrol (tanpa) |
| **2. Genotipe** | Gunakan array SNP untuk melakukan genotipe ratusan ribu varian |
| **3. Uji statistik** | Uji setiap SNP untuk mengetahui hubungannya dengan sifat |
| **4. Plot Manhattan** | Visualisasikan hasil di semua kromosom |
| **5. Replikasi** | Konfirmasikan temuan dalam sampel independen |
---

## Pengeditan Gen
### CRISPR-Cas9
| Komponen | Fungsi |
|-----------|----------|
| **Panduan RNA (gRNA)** | ~20 nukleotida; cocok dengan urutan DNA target |
| **Protein Cas9** | Gunting molekuler; memotong DNA di lokasi target |
| **Urutan PAM** | Motif pendek (NGG) di samping sasaran; diperlukan untuk pengikatan Cas9 |
| **HDR** (Perbaikan yang Diarahkan Homologi) | Pengeditan yang tepat menggunakan template donor |
| **NHEJ** (Penggabungan Akhir Non-Homolog) | Perbaikan yang rawan kesalahan; membuat penyisipan/penghapusan (knockout) |
### Aplikasi Pengeditan Gen
| Aplikasi | Deskripsi |
|-------------|-------------|
| **Terapi** | Memperbaiki mutasi penyebab penyakit (sel sabit; beta-thalassemia) |
| **Pertanian** | Tanaman tahan penyakit; peningkatan ternak |
| **Penelitian** | Buat model sistem gugur; mempelajari fungsi gen |
| **Penggerak gen** | Menyebarkan modifikasi genetik ke seluruh populasi (misalnya nyamuk yang resisten terhadap malaria) |
---

## Pertimbangan Etis
| Edisi | Kekhawatiran |
|-------|---------|
| **Privasi genetik** | Siapa pemilik data genom Anda? Bisakah pemberi kerja atau perusahaan asuransi menggunakannya? |
| **Pengeditan gen pada embrio** | Perubahan yang diwariskan; bayi desainer; efek di luar target yang tidak diinginkan |
| **Diskriminasi genetik** | GINA (AS) melindungi terhadap beberapa diskriminasi namun memiliki kesenjangan |
| **Persetujuan berdasarkan informasi** | Data genom mengungkap informasi tentang kerabat yang belum memberikan persetujuan |
| **Penyimpanan data** | Genom berukuran besar (~200 GB mentah); tantangan penyimpanan dan keamanan jangka panjang |
| **Ekuitas** | Pengobatan genom berisiko memperlebar kesenjangan kesehatan jika hanya tersedia bagi populasi kaya |
---

## Ringkasan
Genetika mempelajari bagaimana gen individu bekerja dan diwariskan. Genomik mempelajari keseluruhan genom — semua gen, interaksinya, dan variasinya. DNA ditranskripsi menjadi RNA, yang diterjemahkan menjadi protein. Ekspresi gen diatur pada berbagai tingkatan: epigenetik, transkripsional, pasca-transkripsional, translasi, dan pasca-translasi. Warisan mengikuti pola (dominan, resesif, poligenik) yang menentukan bagaimana suatu sifat diturunkan antar generasi. Teknologi pengurutan modern (Illumina, PacBio, Nanopore) dapat membaca seluruh genom dengan cepat dan murah. CRISPR-Cas9 memungkinkan pengeditan gen yang tepat dengan potensi transformatif dalam bidang kedokteran dan pertanian. Tantangan terbesarnya adalah etika: siapa yang mengontrol data genom, bagaimana mengatur pengeditan gen pada embrio, dan bagaimana memastikan pengobatan genom bermanfaat bagi semua orang, bukan hanya kelompok yang memiliki hak istimewa.