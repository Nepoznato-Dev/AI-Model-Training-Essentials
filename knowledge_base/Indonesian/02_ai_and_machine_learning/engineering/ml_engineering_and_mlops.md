---
# Metadata
title: "ML Engineering and MLOps"
description: "Model serving, registries, deployment strategies, drift monitoring"
category: "AI and Machine Learning"
subcategory: "ML Engineering"
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
    changes: "Moved to engineering/ subfolder; added subcategory field"
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
tags: [ml, engineering, mlops, ai-and-machine-learning]
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
# Rekayasa ML dan MLOps
Membangun model pembelajaran mesin hanyalah setengah dari perjuangan. Memasukkannya ke dalam produksi, menjaganya tetap berjalan dengan andal, memantau penyimpangan, dan mengulanginya — di situlah rekayasa ML dan MLOps berperan. File ini mencakup seluruh siklus hidup mulai dari eksperimen hingga sistem produksi.
---

## Siklus Hidup ML
| Fase | Deskripsi | Kegiatan Utama |
|-------|-------------|---------------|
| **1. Definisi Masalah** | Bingkai masalah bisnis sebagai tugas ML | Tentukan metrik, batasan, kriteria keberhasilan |
| **2. Pengumpulan Data** | Kumpulkan dan beri label data pelatihan | ETL, pelabelan, augmentasi |
| **3. Eksperimen** | Melatih dan mengevaluasi model | Rekayasa fitur, penyetelan hyperparameter |
| **4. Pemilihan Model** | Pilih model terbaik | Bandingkan metrik, nilai trade-off |
| **5. Penerapan** | Kirim model ke produksi | Melayani infrastruktur, API, batch |
| **6. Pemantauan** | Waspadai penyimpangan dan degradasi | Penyimpangan data, penyimpangan konsep, kinerja |
| **7. Pelatihan ulang** | Perbarui model dengan data baru | Pelatihan ulang terjadwal atau dipicu |
Sebagian besar nilai (dan kesulitan) ada pada fase 5–7. Model yang ada di notebook Jupyter tidak menciptakan nilai bisnis.
---

## Pola Penyajian Model
| Pola | Deskripsi | Latensi | Kasus Penggunaan |
|---------|-------------|---------|----------|
| **Inferensi Batch** | Jalankan model pada kumpulan data sesuai jadwal | Jam | Rekomendasi harian, penilaian penipuan |
| **Inferensi Online** | Prediksi waktu nyata per permintaan | Milidetik | Peringkat pencarian, klasifikasi waktu nyata |
| **Inferensi Streaming** | Memproses prediksi pada aliran data | Detik | Deteksi anomali, pemrosesan peristiwa |
### Melayani Infrastruktur
| Alat | Ketik | Terbaik Untuk |
|------|------|----------|
| **Penyajian TensorFlow** | Server model | Model TensorFlow |
| **Layanan Obor** | Server model | Model PyTorch |
| **Server Inferensi Triton** | Multi-kerangka | Inferensi GPU, berbagai kerangka kerja |
| **vLLM** | LLM melayani | Inferensi LLM throughput tinggi |
| **BentoML** | Penyajian terpadu | Penerapan kerangka-agnostik |
| **Jarang** | K8s-asli | Penerapan model Kubernetes |
| **Ray Sajikan** | Penyajian yang terukur | Model besar, inferensi terdistribusi |
---

## Registri Model
Registri model adalah penyimpanan terpusat untuk mengelola model ML — versi, metadata, metrik, dan status penerapannya.
| Kemampuan | Deskripsi |
|-----------|-------------|
| **Versi** | Lacak setiap versi model dengan ID unik |
| **Metadata** | Data pelatihan, hyperparameter, metrik, penulis |
| **Transisi Tahap** | Pindahkan model melalui tahapan: Pementasan → Produksi → Diarsipkan |
| **Silsilah** | Lacak data dan kode mana yang dihasilkan setiap model |
| Alat | Deskripsi |
|------|-------------|
| **MLaliran** | Sumber terbuka; registri model + pelacakan eksperimen |
| **Bobot & Bias (W&B)** | Komersial; pelacakan eksperimen + registri model |
| **DVC** | Pembuatan versi data dan model dengan Git |
| **Azure ML / SageMaker** | Manajemen model cloud-native |
---

## Pelacakan Eksperimen
Setiap eksperimen ML harus dilacak: data apa yang digunakan, hyperparameter apa, metrik apa yang dihasilkan.
| Alat | Fitur Utama |
|------|-------------|
| **MLaliran** | Sumber terbuka, dihosting sendiri, melacak param/metrik/artefak |
| **W&B** | UI yang kaya, sapuan, pembuatan versi artefak, laporan |
| **Neptunus** | Penyimpanan metadata untuk MLOps |
| **Papan Tensor** | Dibangun pada TensorFlow; memvisualisasikan kurva pelatihan |
### Apa yang Harus Dilacak
| Kategori | Contoh |
|----------|---------|
| **Parameter** | Kecepatan pembelajaran, ukuran batch, arsitektur model, jumlah zaman |
| **Metrik** | Akurasi, kerugian, F1, AUC-ROC (per epoch dan final) |
| **Artefak** | Bobot model, matriks konfusi, sampel prediksi |
| **Data** | Versi kumpulan data, rasio pemisahan, langkah-langkah pra-pemrosesan |
| **Lingkungan** | Versi Python, versi perpustakaan, perangkat keras |
---

## Strategi Penerapan Model
| Strategi | Cara Kerja | Resiko |
|----------|-------------|------|
| **Penyebaran Bayangan** | Model baru berjalan berdampingan dengan model lama; prediksi dibandingkan tetapi tidak ditayangkan | Risiko nol; memvalidasi sebelum ditayangkan |
| **Pelepasan Kenari** | Rutekan sebagian kecil lalu lintas ke model baru; meningkat secara bertahap | Risiko rendah; kembalikan cepat |
| **Pengujian A/B** | Pisahkan pengguna antara lama dan baru; bandingkan metrik bisnis | Mengukur dampak aktual |
| **Biru-Hijau** | Dua lingkungan yang identik; alihkan semua lalu lintas sekaligus | Kembalikan secara instan; biaya ganda selama transisi |
| **Bendera Fitur** | Mengaktifkan/menonaktifkan model per segmen pengguna | Kontrol berbutir halus |
---

## Memantau Sistem ML
Sistem ML memerlukan lebih banyak pemantauan dibandingkan perangkat lunak tradisional karena datanya sendiri dapat berubah.
### Jenis Melayang
| Tipe Melayang | Apa yang Berubah | Contoh |
|-----------|-------------|---------|
| **Penyimpangan Data** | Perubahan distribusi masukan | Pergeseran demografi pelanggan setelah kampanye pemasaran |
| **Konsep Melayang** | Hubungan antara perubahan masukan dan keluaran | Perubahan Perilaku Konsumen Selama Resesi |
| **Label Melayang** | Perubahan Sasaran Distribusi | Tingkat penipuan meningkat dari 1% menjadi 5% |
### Apa yang Harus Dipantau
| Kategori | Metrik |
|----------|---------|
| **Performa Model** | Akurasi, presisi, recall, F1, AUC (dibandingkan baseline) |
| **Kualitas Data** | Nilai, distribusi fitur, outlier |
| **Deteksi Drift** | Uji statistik (uji KS, PSI, divergensi KL) |
| **Infrastruktur** | Latensi, throughput, pemanfaatan GPU, memori |
| **Metrik Bisnis** | Tingkat konversi, dampak pendapatan, kepuasan pengguna |
### Alat Pemantauan
| Alat | Ketik |
|------|------|
| **Ternyata AI** | Penyimpangan data sumber terbuka dan pemantauan kinerja model |
| **Grafana** | Visualisasi dasbor (berfungsi dengan Prometheus) |
| **MengapaLabs** | Platform observasi data |
| **Bangkit** | Observabilitas ML dan analisis akar permasalahan |
| **Prometheus + Grafana** | Metrik infrastruktur dan aplikasi |
---

## Pelatihan yang Dapat Direproduksi
Reproduksibilitas berarti Anda dapat menjalankan kembali eksperimen dan mendapatkan hasil yang sama. Ini penting untuk proses debug, audit, dan kepatuhan.
### Persyaratan
| Persyaratan | Cara Mencapainya |
|-------------|-------------------|
| **Versi data** | DVC, Delta Lake, atau snapshot himpunan data dengan hash |
| **Versi kode** | Git untuk semua kode pelatihan |
| **Penyematan lingkungan** | `requirements.txt`,`conda env`, image Docker dengan versi yang tepat |
| **Pengaturan benih** | Perbaiki benih acak untuk numpy, torch, tensorflow |
| **Manajemen konfigurasi** | Konfigurasi Hydra, OmegaConf, atau YAML untuk semua hyperparameter |
| **Pelacakan artefak** | MLflow atau W&B untuk mencatat setiap eksperimen |
---

## Penskalaan Inferensi
Saat sebuah model perlu melayani jutaan permintaan per hari, performa menjadi hal yang penting.
| Teknik | Deskripsi |
|-----------|-------------|
| **Pengelompokan** | Kelompokkan beberapa permintaan ke dalam satu forward pass |
| **Kuantisasi** | Kurangi presisi model (FP32 → INT8 atau INT4) untuk inferensi lebih cepat |
| **Model Distilasi** | Latih model yang lebih kecil untuk meniru model yang lebih besar |
| **Pemangkasan** | Hapus bobot atau neuron yang tidak penting |
| **Caching** | Cache prediksi yang sering dilakukan untuk menghindari penghitungan ulang |
| **Optimasi GPU** | TensorRT, Waktu Proses ONNX, Perhatian Flash |
| **Penskalaan Horisontal** | Jalankan beberapa replika model di belakang penyeimbang beban |
---

## Bendera Fitur untuk ML
Tanda fitur memungkinkan Anda mengontrol versi model mana yang melayani pengguna tertentu, tanpa menerapkan ulang.
| Kasus Penggunaan | Deskripsi |
|----------|-------------|
| **Peluncuran bertahap** | Sajikan model baru ke 5% pengguna, lalu tingkatkan |
| **Tombol mati** | Segera kembali ke model sebelumnya jika masalah terdeteksi |
| **Berbasis segmen** | Model berbeda untuk segmen pengguna berbeda |
| **Eksperimen** | Varian model pengujian A/B dengan metrik bisnis |
Alat: LaunchDarkly, Unleash, Flagsmith, atau tanda fitur sederhana yang didukung database.
---

## Kurva Kematangan MLOps
| Tingkat | Karakteristik |
|-------|----------------|
| **Tingkat 0 — Panduan** | Pelatihan manual, penerapan manual, tanpa pemantauan |
| **Level 1 — Eksperimen** | Pelacakan eksperimen, registrasi model, CI dasar |
| **Tingkat 2 — Otomatisasi** | Pelatihan ulang otomatis, CI/CD untuk model, pengujian otomatis |
| **Level 3 — Saluran Penuh** | Saluran pipa otomatis ujung ke ujung dengan pemantauan, deteksi penyimpangan, dan pelatihan ulang otomatis |
Sebagian besar organisasi berada di antara Level 0 dan Level 1. Sasarannya adalah Level 2–3, di mana siklus hidup ML diotomatisasi dan melakukan pemulihan mandiri.