<!--
---
# Metadata
title: "Graph Neural Networks"
description: "GCNs, GATs, message passing, knowledge graphs, graph tasks"
category: "AI and Machine Learning"
subcategory: "Model Architectures"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "Nepoznato-Dev"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.1"
    date: "2026-08-09"
    author: "Nepoznato-Dev"
    changes: "Moved to architectures/ subfolder; added subcategory field"
  - version: "1.0.0"
    date: "2026-08-05"
    author: "Nepoznato-Dev"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-09"
review_date: "2027-02-05"
reviewed_by: "AI & Machine Learning Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [graph, neural, networks, ai-and-machine-learning]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "8 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Grafik Jaringan Syaraf Tiruan
Graph Neural Networks (GNNs) adalah jaringan neural yang dirancang untuk beroperasi pada data terstruktur grafik — jaringan node yang dihubungkan oleh edge. Sementara jaringan saraf tradisional bekerja pada grid (gambar) atau urutan (teks), GNN menangani struktur relasional yang sewenang-wenang: jaringan sosial, grafik molekuler, grafik pengetahuan, jaringan jalan, grafik rekomendasi, dan banyak lagi. Mereka menjadi penting untuk penemuan obat, deteksi penipuan, sistem rekomendasi, dan domain apa pun yang mengutamakan hubungan antar entitas.
---

## Apa Itu Grafik?
| Komponen | Deskripsi | Contoh |
|-----------|-------------|---------|
| **Node (puncak)** | Sebuah entitas | Seseorang, atom molekul, kota |
| **Tepi** | Hubungan antara dua node | Persahabatan, ikatan kimia, jalan |
| **Berat tepi** | Kekuatan atau jenis hubungan | Jarak, persamaan, kapasitas |
| **Fitur simpul** | Atribut setiap node | Umur, nomor atom, populasi |
| **Fitur tepi** | Atribut setiap sisi | Jenis hubungan, jarak |
| **Matriks ketetanggaan** | Matriks A dimana A[i][j] = 1 jika node i dan j terhubung | Mengkodekan struktur grafik |
### Jenis Grafik
| Ketik | Deskripsi | Contoh |
|------|-------------|---------|
| **Tidak terarah** | Tepi tidak memiliki arah | Jaringan persahabatan |
| **Disutradarai** | Tepi memiliki arah (A→B ≠ B→A) | Pengikut Twitter |
| **Berbobot** | Tepi memiliki nilai numerik | Jaringan jalan dengan jarak |
| **Heterogen** | Beberapa tipe node dan tepi | Grafik akademik (makalah, penulis, tempat) |
| **Dinamis** | Struktur grafik berubah seiring waktu | Jejaring sosial berkembang seiring waktu |
| **Bipartit** | Dua jenis node; tepi hanya antar tipe | Grafik rekomendasi item pengguna |
---

## Mengapa Bukan Jaringan Neural Biasa?
| Pendekatan | Mengapa Gagal |
|----------|-------------|
| **Jaringan umpan maju** | Memerlukan masukan berukuran tetap; grafik bervariasi dalam ukuran dan struktur |
| **CNN** | Mengasumsikan struktur grid; grafik tidak memiliki grid biasa |
| **RNN/Transformator** | Mengasumsikan urutan berurutan; grafik tidak memiliki urutan alami |
GNN menyelesaikan masalah ini dengan mengoperasikan langsung struktur grafik, memproses setiap node dalam konteks tetangganya.
---

## Arsitektur Inti GNN
### Kerangka Pengiriman Pesan
Kebanyakan GNN mengikuti pola yang sama: setiap node mengumpulkan informasi dari tetangganya, menggabungkannya, dan memperbarui representasinya sendiri.
| Langkah | Deskripsi |
|------|-------------|
| **1. Pesan** | Setiap node mengirimkan pesan ke tetangganya (berdasarkan fiturnya saat ini) |
| **2. Agregat** | Setiap node mengumpulkan dan menggabungkan pesan dari semua tetangga |
| **3. Pembaruan** | Setiap node memperbarui representasinya sendiri menggunakan pesan gabungan |
| **4. Ulangi** | Lakukan ini untuk K lapisan → setiap node menangkap informasi dari K hop |
### Model Utama GNN
| Model | Metode Agregasi | Inovasi Utama |
|-------|-------------------|----------------|
| **GCN** (Jaringan Konvolusional Grafik) | Rata-rata fitur tetangga | Sederhana; efektif; motivasi spektral |
| **GrafikSAGE** | Sampel dan agregat; dapat menggunakan mean, LSTM, atau pooling | Induktif (menangani node yang tidak terlihat); terukur |
| **GAT** (Jaringan Perhatian Grafik) | Agregasi tetangga yang memperhatikan perhatian | Pelajari tetangga mana yang paling penting |
| **GIN** (Jaringan Isomorfisme Grafik) | Jumlah fitur tetangga | Ekspresif secara maksimal; dapat membedakan grafik apa pun yang dapat dibedakan dengan uji WL |
| **MPNN** (Jaringan Syaraf Penyampaian Pesan) | Kerangka penyampaian pesan umum | Menyatukan banyak varian GNN |
### Cara Kerja GCN (Langkah demi Langkah)
```
For each layer:
  1. For each node, collect features from all neighbours
  2. Multiply by a learnable weight matrix W
  3. Normalise by node degree (so high-degree nodes don't dominate)
  4. Apply non-linearity (ReLU)
  5. This becomes the node's new representation
```

Setelah K lapisan, representasi setiap node mengkodekan informasi dari K hop dalam grafik.
---

## Tugas Tingkat Grafik
| Tugas | Deskripsi | Contoh |
|------|-------------|---------|
| **Klasifikasi simpul** | Prediksi label setiap node | Klasifikasikan pengguna sebagai bot atau manusia |
| **Prediksi tautan** | Memprediksi apakah suatu edge ada (atau akan ada) | Memprediksi hubungan yang hilang; merekomendasikan koneksi |
| **Klasifikasi grafik** | Memprediksi label untuk keseluruhan grafik | Mengklasifikasikan molekul sebagai toksik atau tidak toksik |
| **Deteksi komunitas** | Temukan kelompok node yang terhubung erat | Identifikasi kelompok sosial |
| **Pembuatan grafik** | Hasilkan grafik baru dengan properti yang diinginkan | Rancang molekul baru |
---

## Aplikasi
### Penemuan Obat dan Prediksi Sifat Molekuler
| Tugas | Bagaimana GNN Membantu |
|------|--------------|
| **Prediksi sifat molekul** | Mewakili molekul sebagai grafik (atom=simpul, ikatan=tepi); memprediksi toksisitas, kelarutan, afinitas pengikatan |
| **Interaksi obat-obat** | Modelkan obat dan target dalam bentuk grafik; memprediksi interaksi yang merugikan |
| **De novo desain obat** | Hasilkan grafik molekul baru dengan sifat yang diinginkan |
### Sistem Rekomendasi
| Pendekatan | Deskripsi |
|----------|-------------|
| **Grafik item pengguna** | Pengguna dan item adalah node; pembelian/tampilan adalah tepi |
| **Pemfilteran kolaboratif berbasis grafik** | GNN menyebarkan preferensi melalui grafik |
| **Rekomendasi grafik pengetahuan** | Gabungkan preferensi pengguna dengan pengetahuan item (genre, aktor, sutradara) |
### Deteksi Penipuan
| Aplikasi | Struktur Grafik |
|-------------|----------------|
| **Penipuan keuangan** | Transaksi membentuk grafik; pola penipuan muncul sebagai struktur subgraf |
| **Penipuan asuransi** | Penggugat, penyedia, dan kebijakan membentuk grafik; jaringan penipu terdeteksi |
| **Pengambilalihan akun** | Pola login membentuk grafik; koneksi anomali sinyal kompromi |
### Grafik Pengetahuan
| Tugas | Deskripsi |
|------|-------------|
| **Prediksi tautan** | Memprediksi fakta yang hilang (misalnya, "Paris adalah ibu kotanya?") |
| **Resolusi entitas** | Tentukan apakah dua penyebutan merujuk pada entitas yang sama |
| **Menjawab pertanyaan** | Navigasikan grafik untuk menemukan jawaban |
---

## Konsep GNN Tingkat Lanjut
### Terlalu Menghaluskan
| Masalah | Deskripsi | Solusi |
|---------|-------------|----------|
| **Sangat menghaluskan** | Setelah banyak lapisan, semua representasi node menjadi serupa | Batasi kedalaman (2-4 lapisan); gunakan koneksi sisa; gunakan Pengetahuan Melompat |
### Terlalu Terjepit
| Masalah | Deskripsi | Solusi |
|---------|-------------|----------|
| **Terlalu terjepit** | Informasi dari node yang jauh dikompresi menjadi vektor berukuran tetap | Gunakan transformator grafik; pengumpulan hierarki |
### Transformator Grafik
| Model | Fitur Utama |
|-------|-------------|
| **Grafik Transformator** | Terapkan perhatian Transformer standar ke semua pasangan node |
| **GPS** (Sistem Prompt Grafik) | Gabungkan lapisan GNN lokal dengan lapisan Transformer global |
| **Graformer** | Tambahkan pengkodean posisi berdasarkan struktur grafik |
### Jaringan Grafik Heterogen
| Model | Deskripsi |
|-------|-------------|
| **R-GCN** | GCN Relasional; matriks bobot berbeda untuk tipe tepi berbeda |
| **HAN** | Jaringan Perhatian Heterogen; perhatian pada tipe node dan tepi yang berbeda |
| **HetGNN** | Jaringan Syaraf Tiruan Grafik Heterogen; menangani beberapa tipe node |
---

## Skalabilitas
| Tantangan | Solusi |
|-----------|----------|
| **Grafik besar** (jutaan node) | Pelatihan kelompok kecil; pengambilan sampel tetangga |
| **Memori** | Partisi grafik di seluruh GPU |
| **Kecepatan** | Operasi matriks renggang; perpustakaan khusus |
### Strategi Pengambilan Sampel
| Strategi | Deskripsi |
|----------|-------------|
| **Pengambilan sampel simpul** | Contoh subset node dan lingkungan K-hopnya |
| **Pengambilan sampel tepi** | Contoh tepi dan simpul yang dihubungkannya |
| **Pengambilan sampel klaster** | Partisi grafik menjadi beberapa cluster; berlatih dalam cluster |
| **Pengambilan sampel jalan acak** | Sampel node melalui jalan acak dari node target |
---

## Alat dan Kerangka
| Alat | Tujuan |
|------|---------|
| **Geometris PyTorch (PyG)** | Perpustakaan GNN terpopuler; kumpulan model dan kumpulan data yang kaya |
| **DGL** (Perpustakaan Grafik Dalam) | Kerangka-agnostik; mendukung PyTorch, TensorFlow, MXNet |
| **JaringanX** | Algoritma grafik klasik; manipulasi data |
| **OGB** (Tolok Ukur Grafik Terbuka) | Tolok ukur standar dan kumpulan data untuk penelitian GNN |
| **CogDL** | Pembelajaran mendalam untuk grafik; berorientasi pada penelitian |
| **Spektral** | Pustaka GNN untuk TensorFlow/Keras |
---

## Ringkasan
Graph Neural Networks memperluas pembelajaran mendalam pada data relasional — jaringan, molekul, grafik pengetahuan, dan sistem apa pun tempat entitas terhubung. Mereka bekerja dengan meneruskan pesan antar tetangga, memungkinkan setiap node belajar dari konteks lokalnya. GNN telah menemukan penerapan terkuatnya dalam penemuan obat, sistem rekomendasi, deteksi penipuan, dan grafik pengetahuan. Bidang ini berkembang menuju transformator grafik, grafik heterogen, dan pelatihan yang dapat diskalakan untuk jaringan besar di dunia nyata. Jika data Anda memiliki hubungan, GNN mungkin layak untuk dipertimbangkan.