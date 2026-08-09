---
# Metadata
title: "Computer Vision Fundamentals"
description: "CNNs, object detection, segmentation, transfer learning"
category: "AI and Machine Learning"
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
reviewed_by: "AI & Machine Learning Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [computer, vision, ai-and-machine-learning]
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
# Dasar-dasar Visi Komputer
Visi komputer memberi mesin kemampuan untuk menafsirkan dan memahami informasi visual dari dunia — gambar, video, dan data 3D. Ini mendukung segalanya mulai dari pengenalan wajah di ponsel Anda hingga mobil tanpa pengemudi, analisis citra medis, dan kontrol kualitas industri. File ini mencakup konsep inti, arsitektur, dan teknik.
---

## Bagaimana Komputer Melihat Gambar
### Piksel dan Saluran
Gambar digital adalah kisi-kisi piksel. Setiap piksel memiliki nilai numerik yang mewakili intensitas warna.
| Jenis Gambar | Saluran | Nilai per Piksel | Contoh |
|-----------|----------|-----------------|---------|
| **Skala abu-abu** | 1 | 0 (hitam) hingga 255 (putih) | Rontgen Medis |
| **RGB** | 3 | Merah, Hijau, Biru (masing-masing 0–255) | Foto berwarna standar |
| **RGBA** | 4 | RGB + Alpha (transparansi) | Gambar dengan background transparan |
| **HSV** | 3 | Hue, Saturasi, Nilai | Segmentasi berdasarkan warna |
Gambar RGB 1920×1080 adalah tensor dengan bentuk`(1080, 1920, 3)`— berukuran 6,2 juta piksel, masing-masing dengan 3 nilai.
### Operasi Kunci
| Operasi | Deskripsi |
|-----------|-------------|
| **Mengubah ukuran** | Skalakan gambar ke dimensi target (bilinear, interpolasi tetangga terdekat) |
| **Memotong** | Ekstrak wilayah yang diminati |
| **Normalisasi** | Skalakan nilai piksel ke [0,1] atau [-1,1] untuk jaringan saraf |
| **Augmentasi** | Perluas data pelatihan secara artifisial (rotasi, flip, jitter warna, potong) |
---

## Konvolusi: Operasi Inti
Konvolusi menggeser filter kecil (kernel) melintasi gambar, menghitung perkalian titik di setiap posisi. Beginilah cara CNN mendeteksi tepi, tekstur, dan pola.
### Parameter Konvolusi
| Parameter | Efek |
|-----------|--------|
| **Ukuran kernel** | 3×3, 5×5, 7×7 — kernel yang lebih besar menangkap pola yang lebih besar |
| **Langkah** | Ukuran langkah; stride=2 membagi dua dimensi keluaran |
| **Bantalan** | Tambahkan angka nol di sekeliling batas untuk mempertahankan dimensi spasial |
| **Jumlah filter** | Setiap filter mempelajari fitur yang berbeda (tepi, tekstur, pola warna) |
### Apa yang Dipelajari Konvolusi
| Kedalaman Lapisan | Fitur Terdeteksi |
|-------------|------------------|
| **Lapisan awal** | Tepi, sudut, tekstur sederhana |
| **Lapisan tengah** | Bentuk, Bagian Benda (Roda, Mata, Daun) |
| **Lapisan dalam** | Konsep tingkat tinggi (wajah, mobil, hewan) |
---

## Arsitektur CNN
Evolusi arsitektur CNN menceritakan kisah kemajuan pembelajaran mendalam dalam visi komputer.
| Arsitektur | Tahun | Inovasi Utama |
|-------------|------|---------------|
| **LeNet-5** | 1998 | CNN praktis pertama; pengenalan angka |
| **AlexNet** | 2012 | Deep CNN memenangkan ImageNet; ReLU, putus sekolah, pelatihan GPU |
| **VGGNet** | 2014 | Konvolusi 3×3 bertumpuk (lebih dalam = lebih baik) |
| **GoogLeNet (Permulaan)** | 2014 | Modul awal (ukuran filter paralel); 22 lapisan |
| **ResNet** | 2015 | Lewati koneksi (pembelajaran sisa); 152+ lapisan |
| **Jaring Efisien** | 2019 | Penskalaan gabungan (kedalaman + lebar + resolusi) |
| **KonvNeXt** | 2022 | ResNet yang dimodernisasi; bersaing dengan Transformers |
### Mengapa ResNet Mengubah Segalanya
Sebelum ResNet, pelatihan jaringan yang sangat dalam hampir tidak mungkin dilakukan karena masalah gradien yang hilang. ResNet memperkenalkan **lewati koneksi** (juga disebut koneksi sisa): masukan ke lapisan ditambahkan ke keluarannya.
```
output = F(x) + x    # Skip connection
```

Ide sederhana ini memungkinkan jaringan dengan 152+ lapisan dilatih secara efektif, dan sekarang menjadi standar di hampir semua arsitektur mendalam.
---

## Tugas Visi Inti
### Klasifikasi Gambar
Tetapkan label ke seluruh gambar.
| Model | Pendekatan |
|-------|----------|
| CNN (ResNet, EfficientNet) | Pendekatan tradisional; akurasi luar biasa |
| Transformator Visi (ViT) | Perlakukan gambar sebagai rangkaian tambalan; Encoder transformator |
| Transfer Pembelajaran | Sempurnakan model terlatih pada kumpulan data Anda |
### Deteksi Objek
Temukan dan klasifikasikan beberapa objek dalam sebuah gambar, dengan kotak pembatas.
| Model | Ketik | Kecepatan |
|-------|------|-------|
| **R-CNN** | Dua tahap (proposal + klasifikasi) | Lambat |
| **R-CNN Cepat** | Peningkatan dua tahap | Sedang |
| **R-CNN Lebih Cepat** | Jaringan Proposal Wilayah + detektor | Sedang |
| **YOLO** (v1–v10) | Satu tahap; prediksi kotak + kelas dalam satu lintasan | Sangat cepat |
| **DETR** | Berbasis transformator; tidak ada kotak jangkar | Sedang |
**YOLO** (Anda Hanya Melihat Sekali) adalah pilihan untuk deteksi waktu nyata. **R-CNN yang lebih cepat** lebih disukai ketika akurasi lebih penting daripada kecepatan.
### Segmentasi Gambar
Klasifikasikan setiap piksel dalam suatu gambar.
| Ketik | Deskripsi | Kasus Penggunaan |
|------|-------------|----------|
| **Segmentasi Semantik** | Setiap piksel mendapat label kelas | Mengemudi otonom (jalan raya, mobil, pejalan kaki) |
| **Segmentasi Instance** | Setiap piksel + ID instance objek | Menghitung benda, pencitraan medis |
| **Segmentasi Panoptik** | Gabungan semantik + contoh | Pemahaman adegan yang komprehensif |
Model utama: U-Net (pencitraan medis), Mask R-CNN (contoh), DeepLab (semantik), Segment Anything Model (SAM — segmentasi universal).
### Pembuatan Gambar
| Pendekatan | Deskripsi | Contoh |
|----------|-------------|----------|
| **GAN** | Pelatihan permusuhan generator vs diskriminator | GayaGAN, SiklusGAN |
| **VAE** | Pelajari distribusi laten; sampel untuk menghasilkan | Autoencoder Variasi |
| **Model Difusi** | Tolak derau acak secara berulang | Difusi Stabil, DALL-E, Tengah Perjalanan |
Model difusi sebagian besar telah melampaui GAN dalam hal kualitas pembuatan gambar.
---

## Mentransfer Pembelajaran untuk Visi
Melatih CNN dari awal memerlukan data dan komputasi yang sangat besar. Pembelajaran transfer memungkinkan Anda memulai dengan model yang telah dilatih pada jutaan gambar (ImageNet) dan menyempurnakannya untuk tugas spesifik Anda.
### Langkah
1. **Pilih model terlatih** (ResNet50, EfficientNet-B0, ViT).
2. **Ganti kepala klasifikasi** dengan milik Anda sendiri (sesuaikan dengan jumlah kelas Anda).
3. **Bekukan lapisan awal** (lapisan ini menangkap fitur umum seperti tepian).
4. **Sempurnakan** kumpulan data Anda dengan kecepatan pemelajaran rendah.
5. **Cairkan secara bertahap** jika Anda membutuhkan lebih banyak adaptasi.
Pendekatan ini secara rutin mencapai akurasi tinggi hanya dengan 1.000–10.000 gambar berlabel.
---

## Augmentasi Data
Augmentasi secara artifisial memperluas kumpulan data pelatihan Anda dengan menerapkan transformasi.
| Augmentasi | Efek | Kapan Menggunakan |
|-------------|--------|-------------|
| **Pangkasan acak** | Pangkas ke wilayah acak | Hampir selalu |
| **Balik horizontal** | Gambar cermin | Ketika orientasi tidak penting |
| **Rotasi** | Putar dengan sudut acak | Ketika benda muncul di sudut mana pun |
| **Gangguan warna** | Sesuaikan kecerahan, kontras, saturasi | Saat pencahayaan bervariasi |
| **Penghapusan acak** | Tutupi wilayah acak | Meningkatkan ketahanan |
| **Campuran / PotongMix** | Padukan dua gambar dan label | Regularisasi |
Perpustakaan:`torchvision.transforms`,`albumentations`,`imgaug`,`tf.keras.preprocessing`.
---

## Alat dan Kerangka
| Alat | Tujuan |
|------|---------|
| **OpenCV** | Operasi CV klasik (pemfilteran, deteksi tepi, transformasi geometri) |
| **penglihatan obor** | Model visi PyTorch, transformasi, kumpulan data |
| **tf.keras.aplikasi** | Model terlatih di TensorFlow/Keras |
| **Ultralitik (YOLOv8/v11)** | Deteksi objek, segmentasi, klasifikasi |
| **Memeluk Wajah (transformator)** | Transformator Visi, SegFormer, DETR |
| **Segmen Apa Saja (SAM)** | Segmentasi gambar universal dari Meta |
| **Albumentasi** | Pustaka augmentasi gambar yang cepat dan fleksibel |
---

## Tips Praktis
- **Mulailah dengan pembelajaran transfer.** Menyempurnakan model yang telah dilatih sebelumnya akan mengalahkan pelatihan dari awal dalam hampir semua kasus.
- **Normalisasi masukan Anda.** Sesuaikan dengan normalisasi yang diharapkan oleh model terlatih (biasanya mean/std ImageNet).
- **Gunakan metrik yang sesuai.** Akurasi untuk kumpulan data yang seimbang; F1, mAP, atau IoU untuk tugas ketidakseimbangan atau deteksi.
- **Visualisasikan data Anda.** Lihat contoh gambar, periksa distribusi kelas, periksa prediksi model.
- **Tambahkan dengan bijak.** Hanya terapkan transformasi yang masuk akal untuk domain Anda (jangan membalik gambar medis secara vertikal).
- **Pantau overfitting.** Jika akurasi pelatihan tinggi namun validasinya rendah, tingkatkan augmentasi atau tambahkan dropout.