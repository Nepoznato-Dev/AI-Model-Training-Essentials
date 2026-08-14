<!--
---
# Metadata
title: "Model Optimisation and Deployment"
description: "Quantisation, pruning, distillation, ONNX, serving infrastructure"
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
tags: [model, optimization, deployment, ai-and-machine-learning]
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
# Optimasi dan Penerapan Model
Melatih model AI berukuran besar merupakan pencapaian yang signifikan, namun menerapkannya secara efisien adalah hal yang memerlukan sebagian besar upaya rekayasa. Model yang membutuhkan waktu 10 detik untuk merespons atau memerlukan delapan GPU A100 tidak praktis untuk sebagian besar aplikasi dunia nyata. Pengoptimalan model adalah proses menjadikan model lebih kecil, lebih cepat, dan lebih hemat biaya — dengan tetap mempertahankan kualitas yang dapat diterima. File ini mencakup kuantisasi, pemangkasan, distilasi, dan alat praktis untuk menerapkan model dalam produksi.
---

## Mengapa Optimalkan?
| Kekhawatiran | Dampak |
|---------|--------|
| **Latensi** | Pengguna mengharapkan tanggapan dalam waktu kurang dari 1 detik; setiap 100 md tambahan kehilangan keterlibatan |
| **Biaya** | Inferensi GPU itu mahal; model 70 miliar berharga ~$0,05-0,15 per 1 juta token di perangkat keras cloud |
| **Memori** | Model 7B di FP32 membutuhkan VRAM 28 GB; sebagian besar GPU konsumen memiliki 8-24 GB |
| **Energi** | Menjalankan model besar menghabiskan banyak listrik; penting untuk seluler dan edge |
| **Skala** | Melayani jutaan pengguna memerlukan model yang sesuai dengan perangkat keras yang tersedia |
---

## Kuantisasi
Kuantisasi mengurangi presisi bobot model dari floating point 32-bit (FP32) ke format yang lebih kecil seperti INT8, INT4, atau bahkan lebih rendah.
### Format Presisi
| Format | Bit per Berat | Memori untuk Model 7B | Kualitas |
|--------|----------------|--------------------|---------|
| **FP32** | 32 | 28GB | Baseline (presisi penuh) |
| **FP16 / BF16** | 16 | 14 GB | Hampir identik dengan FP32 |
| **INT8** | 8 | 7 GB | Kehilangan kualitas yang sangat kecil |
| **INT4** | 4 | 3,5GB | Kehilangan kualitas sedang; masih dapat digunakan |
| **INT3 / INT2** | 3-2 | 2,6-1,75GB | Kehilangan kualitas yang signifikan; tahap penelitian |
### Metode Kuantisasi
| Metode | Kapan Itu Terjadi | Cara Kerja | Kualitas |
|--------|----------------|--------------|---------|
| **Kuantisasi Pasca Pelatihan (PTQ)** | Setelah pelatihan selesai | Kalibrasi model pada kumpulan data kecil; temukan skala optimal | Bagus untuk INT8; terdegradasi di INT4 |
| **GPTQ** | Setelah pelatihan | Kuantisasi INT4 ramah GPU menggunakan perkiraan informasi orde kedua | Kualitas bagus di INT4 |
| **AWQ** (Kuantisasi Berat Sadar Aktivasi) | Setelah pelatihan | Lindungi bobot yang menonjol berdasarkan besaran aktivasi | Lebih baik dari GPTQ di INT4 |
| **GGUF** (format llama.cpp) | Setelah pelatihan | kuantisasi ramah CPU; presisi campuran per lapisan | Dioptimalkan untuk inferensi CPU |
| **Pelatihan Sadar Kuantisasi (QAT)** | Selama pelatihan | Simulasikan kuantisasi selama pelatihan sehingga model belajar mengatasinya | Kualitas terbaik; membutuhkan pelatihan ulang |
### Dampak Praktis
| Model | Ukuran FP16 | Ukuran INT4 | Mempercepat | Kehilangan Kualitas |
|-------|-----------|-----------|---------|-------------|
| **LLaMA 7B** | 14 GB | 3,5GB | 2-4x | ~1-2% pada tolok ukur |
| **LLaMA 70B** | 140GB | 35GB | 2-3x | ~2-3% pada tolok ukur |
---

## Pemangkasan
Pemangkasan menghilangkan bobot atau neuron yang tidak perlu dari model terlatih.
| Ketik | Deskripsi | Keuntungan | Tantangan |
|------|-------------|-----------|-----------|
| **Tidak terstruktur** | Hapus bobot individu (setel ke nol) | Rasio kompresi tertinggi | Memerlukan dukungan perangkat keras yang jarang |
| **Terstruktur** | Hapus seluruh neuron, kepala perhatian, atau lapisan | Langsung mengurangi ukuran model | Mungkin kehilangan lebih banyak kualitas |
| **Berbasis besaran** | Hapus bobot dengan nilai absolut terkecil | Sederhana; berfungsi dengan baik | Mungkin melewatkan beban kecil yang penting |
| **Berbasis kepentingan** | Hapus bobot berdasarkan kontribusinya terhadap keluaran | Pelestarian kualitas yang lebih baik | Lebih mahal untuk dihitung |
### Pemangkasan Pipa
| Langkah | Deskripsi |
|------|-------------|
| 1. Kereta | Latih model lengkap secara normal |
| 2. Skor | Hitung skor kepentingan untuk setiap bobot/neuron |
| 3. Pangkas | Hapus elemen yang paling tidak penting |
| 4. Menyempurnakan | Latih kembali untuk memulihkan akurasi yang hilang |
| 5. Ulangi | Ulangi pemangkasan dan penyesuaian untuk kompresi yang lebih tinggi |
---

## Penyulingan Pengetahuan
Melatih model “siswa” kecil untuk meniru model “guru” yang besar.
| Komponen | Peran |
|-----------|------|
| **Guru** | Model besar dan berkualitas tinggi |
| **Siswa** | Model kecil yang belajar dari guru |
| **Kerugian distilasi** | Siswa mencoba mencocokkan distribusi keluaran guru (label lunak) |
### Jenis Distilasi
| Ketik | Deskripsi | Contoh |
|------|-------------|---------|
| **Berbasis logit** | Siswa cocok dengan probabilitas keluaran guru | Distilasi asli Hinton |
| **Berbasis fitur** | Siswa mencocokkan representasi perantara guru | FitNet |
| **Berbasis hubungan** | Siswa mencocokkan hubungan antar sampel | RKD (Distilasi Pengetahuan Relasional) |
| **Bebas data** | Tidak diperlukan data pelatihan asli; gunakan generasi guru | DAFL, Inversi Dalam |
### Contoh Distilasi Terkemuka
| Guru | Siswa | Hasil |
|---------|---------|--------|
| **GPT-4** | GPT-3.5-turbo (dikabarkan) | Model yang lebih kecil dengan kualitas GPT-4 |
| **BERT-Besar** | DistilBERT | 40% lebih kecil, 60% lebih cepat, 97% kinerja BERT |
| **LLaMA 70B** | LLaMA 7B (melalui distilasi) | Model kecil sumber terbuka mendekati kualitas model besar |
---

## Optimasi Khusus LLM
### Optimasi KV-Cache
Model bahasa besar menyimpan pasangan nilai kunci dari token sebelumnya untuk menghindari penghitungan ulang.
| Teknik | Deskripsi | Dampak |
|-----------|-------------|--------|
| **Perhatian Multi-Kueri (MQA)** | Semua kepala perhatian berbagi satu pasangan KV | Mengurangi memori; sedikit penurunan kualitas |
| **Perhatian Kueri yang Dikelompokkan (GQA)** | Kelompok kepala berbagi pasangan KV | Keseimbangan antara MQA dan perhatian standar |
| **Perhatian jendela geser** | Hanya hadir pada token W terakhir | Mengurangi ukuran cache KV untuk konteks yang panjang |
### Penguraian Kode Spekulatif
| Langkah | Deskripsi |
|------|-------------|
| 1 | Model "draf" kecil menghasilkan token K dengan cepat |
| 2 | Model besar memverifikasi semua token K dalam satu forward pass |
| 3 | Token yang diterima disimpan; yang ditolak dibuat ulang |
Hasil: peningkatan kecepatan 2-3x dalam pembuatannya tanpa kehilangan kualitas (model besar selalu memiliki keputusan akhir).
### Perhatian Kilat
| Fitur | Deskripsi |
|---------|-------------|
| **Masalah** | Perhatian standar memerlukan memori O(n²) untuk matriks perhatian |
| **Solusi** | Hitung perhatian dalam blok; tidak pernah mewujudkan matriks penuh dalam memori |
| **Hasil** | 2-4x lebih cepat; mengaktifkan jendela konteks yang lebih panjang |
| **Varian** | Flash Attention 2 (lebih cepat), FlashDecoding (dioptimalkan untuk inferensi) |
---

## Kerangka Penyajian
| Kerangka | Terbaik Untuk | Fitur Utama |
|-----------|----------|-------------|
| **vLLM** | LLM melayani | PagedPerhatian; pengelompokan terus menerus; throughput tinggi |
| **TensorRT-LLM** | Inferensi GPU NVIDIA | Performa maksimal pada perangkat keras NVIDIA |
| **llama.cpp** | Inferensi CPU dan GPU konsumen | Menjalankan model terkuantisasi pada laptop dan ponsel |
| **Olama** | Model lokal berjalan | Pembungkus yang ramah pengguna di sekitar llama.cpp |
| **Server Inferensi Triton** | Penyajian multi-kerangka | Mendukung TensorFlow, PyTorch, ONNX, TensorRT |
| **Layanan Obor** | Penyajian model PyTorch | Integrasi PyTorch asli |
| **Waktu Proses ONNX** | Inferensi lintas platform | Eksekusi yang dioptimalkan di seluruh perangkat keras |
| **BentoML** | Penyebaran produksi | Kerangka-agnostik; menangani pengemasan dan penyajian |
---

## Pola Penerapan
| Pola | Deskripsi | Kapan Menggunakan |
|---------|-------------|-------------|
| **Penerapan Edge** | Jalankan model di ponsel, perangkat IoT, atau perangkat keras tertanam | Latensi rendah; luring; privasi |
| **API Awan** | Model host pada GPU cloud; melayani melalui API | Komputasi maksimum; bayar per penggunaan |
| **Hibrida** | Model kecil di perangkat; model besar di cloud | Terbaik dari kedua dunia |
| **Tanpa Server** | Skala ke nol; bayar hanya bila dipakai | Lalu lintas sporadis; sensitif terhadap biaya |
| **Inferensi kumpulan** | Memproses data secara massal sesuai jadwal | Ketika waktu nyata tidak diperlukan |
---

## Pembandingan
| Metrik | Apa yang Diukurnya |
|--------|-----------------|
| **Token per detik** | Throughput generasi (lebih tinggi lebih baik) |
| **Waktunya untuk token pertama (TTFT)** | Latensi sebelum token keluaran pertama muncul |
| **Latensi per permintaan** | Total waktu dari input hingga output selesai |
| **Penggunaan memori** | VRAM atau RAM yang dikonsumsi selama inferensi |
| **Melalui** | Permintaan dilayani per detik |
| **Biaya per 1 juta token** | Biaya dolar untuk memproses 1 juta token |
---

## Tips Praktis
- **Mulai dengan kuantisasi.** Kuantisasi INT4 (AWQ atau GPTQ) memberikan trade-off kualitas dan ukuran terbaik. Sebagian besar model 7B berjalan dengan nyaman pada satu GPU konsumen di INT4.
- **Gunakan vLLM untuk penyajian LLM.** Ini adalah opsi sumber terbuka tercepat untuk inferensi LLM throughput tinggi.
- **Profil sebelum mengoptimalkan.** Ukur di mana waktu sebenarnya dihabiskan. Seringkali bandwidth memori, bukan komputasi, itulah hambatannya.
- **Cocokkan model dengan tugas.** Model 7B cocok untuk sebagian besar tugas. Jangan gunakan 70B ketika 7B sudah cukup.
- **Pertimbangkan penyulingan.** Jika Anda memerlukan model yang kecil dan cepat untuk produksi, lakukan penyulingan dari model yang lebih besar daripada melatihnya dari awal.
- **Pantau terus menerus.** Performa model dapat menurun seiring waktu seiring dengan pergeseran distribusi data. Lacak metrik latensi, throughput, dan kualitas.
---

## Ringkasan
Optimalisasi model adalah jembatan antara penelitian dan produksi. Kuantisasi memperkecil model sebesar 4-8x dengan penurunan kualitas minimal. Pemangkasan menghilangkan bobot mati. Distilasi mentransfer pengetahuan dari model besar ke model kecil. Flash Attention dan trik KV-cache membuat inferensi lebih cepat. Bersama-sama, teknik-teknik ini mengubah model yang memerlukan pusat data menjadi model yang dapat dijalankan di laptop atau ponsel. Bidang ini bergerak cepat — apa yang dibutuhkan delapan A100 pada tahun lalu dijalankan pada GPU konsumen saat ini.