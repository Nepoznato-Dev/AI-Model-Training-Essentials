---
# Metadata
title: "Recommendation Systems"
description: "Collaborative filtering, content-based, hybrid, matrix factorisation"
category: "AI and Machine Learning"
subcategory: "Model Architectures"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "AI Model Training Team"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.1"
    date: "2026-08-09"
    author: "AI Model Training Team"
    changes: "Moved to architectures/ subfolder; added subcategory field"
  - version: "1.0.0"
    date: "2026-08-05"
    author: "AI Model Training Team"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-09"
review_date: "2027-02-05"
reviewed_by: "AI & Machine Learning Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [recommendation, systems, ai-and-machine-learning]
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

# Sistem Rekomendasi
Sistem rekomendasi memprediksi apa yang selanjutnya ingin dilihat, dibeli, atau berinteraksi oleh pengguna. Mereka mendukung umpan konten di media sosial, saran produk di situs e-niaga, pilihan film di platform streaming, dan hasil pencarian. Meskipun tidak terlihat oleh sebagian besar pengguna, sistem ini merupakan salah satu sistem AI yang paling berdampak secara komersial di dunia — Netflix memperkirakan mesin rekomendasinya menghemat lebih dari $1 miliar per tahun dengan mengurangi churn pelanggan.
---

## Mengapa Rekomendasi Itu Sulit
| Tantangan | Deskripsi |
|-----------|-------------|
| **Skala** | Jutaan pengguna × jutaan item = miliaran kemungkinan pasangan |
| **Ketersebaran** | Setiap pengguna telah berinteraksi dengan sebagian kecil dari item yang tersedia |
| **Awal dingin** | Pengguna baru dan item baru tidak memiliki riwayat interaksi |
| **Preferensi dinamis** | Selera pengguna berubah seiring waktu |
| **Melampaui akurasi** | Rekomendasi juga harus beragam, baru, dan kebetulan |
| **Tujuan bisnis** | Memaksimalkan keterlibatan ≠ memaksimalkan kesejahteraan pengguna |
---

## Pendekatan Inti
### Pemfilteran Kolaboratif
Idenya: jika pengguna A dan B sebelumnya setuju, mereka mungkin akan setuju di masa mendatang.
| Ketik | Cara Kerja | Contoh |
|------|-------------|---------|
| **Berbasis pengguna** | Temukan pengguna serupa; merekomendasikan apa yang mereka sukai | "Pengguna yang menyukai ini juga menyukai..." |
| **Berbasis item** | Temukan item serupa dengan apa yang disukai pengguna | "Karena kamu menonton..." |
| **Faktorisasi matriks** | Dekomposisi matriks interaksi pengguna-item menjadi faktor laten | SVD, ALS (Kuadrat Terkecil Bergantian) |
| Kekuatan | Kelemahan |
|----------|----------|
| Tidak perlu memahami item sendiri | Masalah cold start: tidak dapat merekomendasikan item baru |
| Menangkap preferensi yang kompleks dan implisit | Membutuhkan banyak data interaksi |
| Berfungsi di semua tipe konten | Bias popularitas: merekomendasikan item yang sudah populer |
### Pemfilteran Berbasis Konten
Merekomendasikan item serupa dengan yang disukai pengguna, berdasarkan fitur item.
| Tipe Fitur | Contoh |
|-------------|---------|
| **Teks** | Genre, deskripsi, kata kunci, pemeran |
| **Audio** | Tempo, genre, mood (untuk musik) |
| **Visual** | Palet warna, gaya (untuk gambar/mode) |
| **Metadata** | Harga, merek, kategori |
| Kekuatan | Kelemahan |
|----------|----------|
| Tidak ada awal yang dingin untuk item (fitur diketahui) | Tidak dapat merekomendasikan item di luar selera pengguna |
| Bekerja dengan lebih sedikit data interaksi | Memerlukan rekayasa fitur yang baik |
| Dapat dijelaskan ("disarankan karena mirip dengan X") | Kurangnya kebetulan |
### Pendekatan Hibrid
Kebanyakan sistem produksi menggabungkan metode kolaboratif dan berbasis konten.
| Strategi Hibrid | Deskripsi |
|----------------|-------------|
| **Berbobot** | Gabungkan skor dari beberapa model |
| **Beralih** | Gunakan berbasis konten untuk pengguna baru, kolaboratif untuk pengguna lama |
| **Bertingkat** | Gunakan model yang sederhana terlebih dahulu, lalu sempurnakan dengan model yang kompleks |
| **Kombinasi fitur** | Gabungkan fitur kolaboratif dan konten ke dalam satu model |
| **Pembelajaran meta** | Pelajari cara menggabungkan berbagai rekomendasi |
---

## Pendekatan Pembelajaran Mendalam Modern
### Model Dua Menara
Arsitektur dominan untuk rekomendasi skala besar (digunakan oleh YouTube, Pinterest, Spotify).
| Komponen | Peran |
|-----------|------|
| **Menara pengguna** | Jaringan saraf yang mengkodekan fitur dan riwayat pengguna ke dalam |
| **Menara barang** | Jaringan saraf yang mengkodekan fitur item ke dalam penyematan |
| **Kesamaan** | Kesamaan perkalian titik atau kosinus antara penyematan pengguna dan item |
| Langkah | Deskripsi |
|------|-------------|
| 1 | Latih kedua menara untuk menghasilkan penyematan serupa untuk pasangan item pengguna yang berinteraksi |
| 2 | Pada waktu penayangan, lakukan pra-hitung penyematan item |
| 3 | Untuk permintaan pengguna, hitung penyematan pengguna |
| 4 | Gunakan pencarian perkiraan tetangga terdekat (ANN) untuk menemukan item yang paling mirip |
### Model Urutan untuk Rekomendasi
Perilaku pengguna bersifat berurutan — apa yang Anda tonton kemarin memengaruhi apa yang akan Anda tonton hari ini.
| Model | Pendekatan |
|-------|----------|
| **Rek GRU4** | Model berbasis GRU untuk rekomendasi berbasis sesi |
| **SASRec** | Rekomendasi sekuensial berbasis perhatian diri |
| **BERT4Rek** | Transformator Dua Arah untuk rekomendasi sekuensial |
| **DNN YouTube** | Jaringan saraf dalam memperlakukan riwayat tontonan sebagai urutan |
### Pengambilan vs Pemeringkatan
Sistem modern membagi rekomendasi menjadi dua tahap:
| Tahap | Tujuan | Metode |
|-------|---------|--------|
| **Pengambilan (generasi kandidat)** | Persempit jutaan item menjadi ~1.000 kandidat | Model dua menara; pencarian JST; cepat tapi perkiraan |
| **Peringkat (skor)** | Skor dan urutkan kandidat secara tepat | Model mendalam dengan banyak fitur; lebih lambat tapi akurat |
| **Pemeringkatan ulang** | Sesuaikan dengan keberagaman, aturan bisnis, kesegaran | Bandit kontekstual; optimasi kendala |
---

## Metrik Evaluasi
| Metrik | Apa yang Diukurnya | Kapan Menggunakan |
|--------|-----------------|-------------|
| **Presisi@K** | Sebagian kecil rekomendasi K teratas yang relevan | Ketika Anda peduli dengan keakuratan pilihan teratas |
| **Ingat@K** | Sebagian kecil item relevan ditemukan di top-K | Ketika Anda peduli untuk tidak melewatkan barang bagus |
| **NDCG** (Keuntungan Kumulatif Diskon yang Dinormalisasi) | Kualitas peringkat; imbalan menempatkan item yang relevan lebih tinggi | Ketika urutan peringkat penting |
| **MAP** (Rata-rata Presisi) | Presisi rata-rata di seluruh pengguna | Kualitas peringkat keseluruhan |
| **Tingkat Hit@K** | Apakah setidaknya satu item relevan muncul di top-K | Skenario relevansi biner |
| **Cakupan** | Sebagian kecil item yang direkomendasikan | Keberagaman dan keadilan |
| **Kebetulan** | Rekomendasi yang tidak terduga namun relevan | Kepuasan pengguna |
---

## Masalah Start Dingin
| Skenario | Tantangan | Solusi |
|----------|-----------|-----------|
| **Pengguna baru** | Tidak ada riwayat interaksi | Gunakan demografi; tampilkan item populer; gunakan sinyal kontekstual (lokasi, perangkat, waktu) |
| **Barang baru** | Belum ada yang berinteraksi dengannya | Gunakan fitur konten; strategi eksplorasi-eksploitasi; algoritma bandit |
| **Sistem baru** | Tidak ada data sama sekali | Mentransfer pembelajaran dari domain serupa; kurasi konten awal |
---

## Eksplorasi vs Eksploitasi
| Strategi | Deskripsi | Pertukaran |
|----------|-------------|-----------|
| **ε-serakah** | Tampilkan item acak dengan probabilitas ε | Sederhana namun tidak efisien |
| **Pengambilan sampel Thompson** | Sampel dari distribusi posterior kualitas item | Berprinsip; sifat teoritis yang baik |
| **Batas Keyakinan Atas (UCB)** | Lebih menyukai item dengan ketidakpastian tinggi | Keseimbangan yang baik antara eksplorasi dan eksploitasi |
| **Bandit kontekstual** | Eksplorasi dikondisikan pada konteks pengguna | Lebih efisien dibandingkan eksplorasi buta |
| **Injeksi Keanekaragaman** | Sengaja menyertakan item yang beragam atau baru | Sederhana; dapat mengurangi keterlibatan jangka pendek |
---

## Bias dan Keadilan
| Tipe Bias | Deskripsi | Dampak |
|-----------|-------------|--------|
| **Bias popularitas** | Item populer semakin direkomendasikan, menjadi lebih populer | Item berekor panjang kurang terlayani |
| **Bias seleksi** | Model belajar dari interaksi yang diamati, tidak semua interaksi yang mungkin | Condong ke arah pengguna aktif |
| **Bias posisi** | Item yang ditampilkan di posisi lebih tinggi mendapatkan lebih banyak klik, apa pun kualitasnya | Memperkuat posisi teratas |
| **Bias eksposur** | Item yang telah ditampilkan mendapatkan lebih banyak sinyal pelatihan | Putaran umpan balik |
| **Bias demografi** | Rekomendasi berbeda antar demografi dengan cara yang tidak adil | Diskriminasi; pengalaman buruk untuk beberapa kelompok |
### Strategi Mitigasi
| Strategi | Deskripsi |
|----------|-------------|
| **Pembobotan kecenderungan terbalik** | Item populer untuk menurunkan berat badan dalam pelatihan |
| **Lapisan debiasing** | Tambahkan komponen debiasing ke model |
| **Kendala keadilan** | Tambahkan batasan untuk memastikan perlakuan yang adil |
| **Beragam rekomendasi** | Optimalkan keberagaman dan relevansi secara eksplisit |
| **Audit dan pemantauan** | Periksa secara teratur rekomendasi untuk mengetahui adanya bias antar kelompok |
---

## Contoh Industri
| Perusahaan | Sistem | Pendekatan |
|---------|--------|----------|
| **Netflix** | Rekomendasi Film/TV | Pengambilan dua menara + peringkat mendalam + bandit kontekstual untuk karya seni |
| **YouTube** | Rekomendasi video | Jaringan saraf dalam untuk menghasilkan kandidat; model peringkat terpisah |
| **Spotify** | Rekomendasi musik | Pemfilteran kolaboratif + NLP pada daftar putar + analisis audio |
| **Amazon** | Rekomendasi Produk | Pemfilteran kolaboratif item-ke-item; dipersonalisasi dalam skala besar |
| **TikTok** | Umpan video pendek | Pembelajaran penguatan; penekanan kuat pada eksplorasi |
| **Pinterest** | Rekomendasi visual | Model dua menara; kesamaan visual |
---

## Alat dan Kerangka
| Alat | Tujuan |
|------|---------|
| **Pemberi Rekomendasi TensorFlow (TFRS)** | Model dua menara, pengambilan, pemeringkatan |
| **RecSys PyTorch** | Model rekomendasi berorientasi penelitian |
| **Kejutan** | Pemfilteran kolaboratif klasik (SVD, NMF, KNN) |
| **Tersirat** | Pemfilteran kolaboratif cepat untuk umpan balik implisit (ALS, BPR) |
| **Faiss** (Meta) | Perkiraan pencarian tetangga terdekat dalam skala |
| **Milvus / Biji Pinus / Weaviate** | Database vektor untuk pencarian kesamaan |
| **Recbole** | Perpustakaan penelitian rekomendasi yang komprehensif |
| **Merlin** (NVIDIA) | Saluran rekomendasi yang dipercepat GPU |
---

## Ringkasan
Sistem rekomendasi adalah salah satu aplikasi AI yang paling berdampak di industri. Bidang ini telah berevolusi dari pemfilteran kolaboratif sederhana menjadi arsitektur pembelajaran mendalam yang menggabungkan riwayat pengguna, konten item, sinyal kontekstual, dan tujuan bisnis. Sistem modern menggunakan alur pengambilan-peringkat-peringkat-ulang, dengan model dua menara untuk menghasilkan kandidat dengan cepat dan model mendalam untuk penilaian yang tepat. Tantangannya – cold start, bias, eksplorasi, dan menyeimbangkan kepuasan pengguna dengan tujuan bisnis – tetap menjadi bidang penelitian dan rekayasa yang aktif.