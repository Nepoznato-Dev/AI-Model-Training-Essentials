---
# Metadata
title: "Federated Learning and Privacy"
description: "Decentralised training, differential privacy, secure aggregation"
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
tags: [federated, learning, privacy, ai-and-machine-learning]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "9 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# Pembelajaran Federasi dan Privasi
Pembelajaran gabungan adalah teknik untuk melatih model pembelajaran mesin di beberapa perangkat atau organisasi tanpa berbagi data mentah. Daripada mengirim data ke server pusat, setiap perangkat melatih model lokal dan hanya membagikan pembaruan model (gradien atau bobot). Server pusat mengumpulkan pembaruan ini untuk menghasilkan model global. Ini dirancang oleh Google untuk melatih model bahasa keyboard di ponsel Android — dan sejak itu menjadi teknik utama untuk AI yang menjaga privasi.
---

## Mengapa Pembelajaran Federasi?
| Motivasi | Deskripsi | Contoh |
|------------|-------------|---------|
| **Privasi data** | Data mentah tidak pernah meninggalkan perangkat | Rekam medis tinggal di rumah sakit; foto tetap di telepon |
| **Kepatuhan terhadap peraturan** | GDPR, HIPAA, dan peraturan lainnya membatasi berbagi data | Bank dapat berkolaborasi tanpa berbagi data nasabah |
| **Volume data** | Memindahkan data itu mahal dan lambat | Pelatihan miliaran ponsel tidak praktis jika data harus diunggah |
| **Sensitivitas data** | Beberapa data terlalu sensitif untuk dibagikan, bahkan dengan persetujuan | Intelijen pemerintah; data kesehatan pribadi |
---

## Cara Kerja Pembelajaran Federasi
### Protokol Dasar (FedAvg)
| Langkah | Apa yang Terjadi |
|------|-------------|
| **1. Inisialisasi** | Server pusat membuat model global dengan bobot acak |
| **2. Distribusikan** | Server mengirimkan model global saat ini ke perangkat yang dipilih |
| **3. Pelatihan lokal** | Setiap perangkat melatih model pada data lokalnya selama beberapa periode |
| **4. Unggah** | Perangkat mengirimkan bobot model yang diperbarui (bukan data) kembali ke server |
| **5. Agregat** | Server menghitung rata-rata bobotnya (Federasi Rata-rata) untuk membuat model global baru |
| **6. Ulangi** | Kembali ke langkah 2 hingga model konvergen |
```
Server: global_model = average(local_model_1, local_model_2, ..., local_model_n)
```

### Properti Utama
| Properti | Deskripsi |
|----------|-------------|
| **Data non-IID** | Setiap perangkat mempunyai sebaran data yang berbeda-beda (tidak mandiri dan terdistribusi secara identik) |
| **Data tidak seimbang** | Beberapa perangkat memiliki banyak data, perangkat lainnya hanya memiliki sedikit |
| **Partisipasi sebagian** | Tidak semua perangkat tersedia di setiap putaran |
| **Efisiensi komunikasi** | Hambatannya adalah komunikasi, bukan komputasi |
---

## Varian Pembelajaran Federasi
| Varian | Deskripsi | Keuntungan |
|---------|-------------|-----------|
| **Rata-rata Fed** | Bobot model rata-rata di seluruh perangkat | Sederhana; berfungsi dengan baik untuk data IID |
| **FedProx** | Menambahkan istilah proksimal ke pelatihan lokal | Lebih baik untuk data non-IID |
| **PERANGKAT** | Menggunakan variasi kontrol untuk mengoreksi heterogenitas data | Konvergensi lebih cepat pada data non-IID |
| **FedSGD** | Seperti FedAvg tetapi dengan satu langkah gradien per putaran | Biaya komunikasi lebih rendah per putaran |
| **FL yang Dipersonalisasi** | Setiap perangkat mempertahankan model yang dipersonalisasi bersama dengan model global | Performa per perangkat yang lebih baik |
| **FL Vertikal** | Fitur yang berbeda (bukan sampel yang berbeda) antar pihak | Ketika para pihak memegang aspek berbeda dari data yang sama |
---

## Privasi Diferensial
Privasi diferensial (DP) memberikan jaminan matematis bahwa keluaran algoritme tidak mengungkapkan apakah data individu disertakan.
### Definisi Inti
Mekanisme M memenuhi privasi diferensial (ε, δ) jika untuk dua kumpulan data D dan D' yang berbeda dalam satu catatan:
```
P(M(D) ∈ S) ≤ e^ε × P(M(D') ∈ S) + Î´
```

| Parameter | Arti |
|-----------|---------|
| **ε (epsilon)** | Anggaran privasi. Lebih kecil = lebih pribadi. Nilai tipikal: 0,1–10. |
| **δ (delta)** | Kemungkinan kegagalan jaminan privasi. Biasanya disetel ke 1/N (kebalikan dari ukuran kumpulan data). |
### Mekanisme Penambahan Privasi
| Mekanisme | Cara Kerja | Kasus Penggunaan |
|-----------|-------------|----------|
| **Mekanisme Gaussian** | Tambahkan noise Gaussian yang dikalibrasi ke sensitivitas kueri | Nilai kontinu (bobot model) |
| **Mekanisme Laplace** | Tambahkan kebisingan Laplace | Menghitung kueri |
| **Mekanisme eksponensial** | Pilih keluaran dengan probabilitas sebanding dengan kegunaannya | Pilihan diskrit |
### DP-SGD (Penurunan Gradien Stochastic Privat Diferensial)
| Langkah | Deskripsi |
|------|-------------|
| 1. Hitung gradien per sampel | Alih-alih gradien batch |
| 2. Klip gradien | Terikat norma maksimum setiap gradien (membatasi pengaruh sampel tunggal) |
| 3. Tambahkan kebisingan | Tambahkan noise Gaussian yang telah dikalibrasi ke gradien gabungan |
| 4. Perbarui parameter | Langkah penurunan gradien standar |
| Pertukaran | Deskripsi |
|-----------|-------------|
| **Privasi vs akurasi** | Privasi yang lebih kuat (ε lebih rendah) memerlukan lebih banyak noise, sehingga mengurangi akurasi model |
| **Privasi vs waktu pelatihan** | Lebih banyak noise berarti konvergensi lebih lambat |
| **Pelacakan anggaran privasi** | Setiap langkah pelatihan menghabiskan sebagian anggaran privasi; sekali dihabiskan, tidak dapat dipulihkan |
---

## Menggabungkan Pembelajaran Federasi dengan Privasi Diferensial
| Lapisan | Perlindungan |
|-------|-----------|
| **Pembelajaran gabungan** | Data mentah tetap ada di perangkat |
| **Privasi diferensial** | Bahkan pembaruan model pun berisik, melindungi kontribusi individu |
| **Agregasi aman** | Server hanya melihat keseluruhan pembaruan, bukan pembaruan individual |
Kombinasi ini memberikan jaminan privasi yang kuat: meskipun server disusupi, server tidak dapat menentukan apakah data individu tertentu digunakan dalam pelatihan.
---

## Teknik Menjaga Privasi Lainnya
### Komputasi Multi-Pihak Aman (SMPC)
Banyak pihak menghitung suatu fungsi atas data gabungan mereka tanpa mengungkapkan masukan masing-masing.
| Fitur | Deskripsi |
|---------|-------------|
| **Cara kerjanya** | Data dibagi menjadi beberapa bagian yang didistribusikan ke berbagai pihak; perhitungan terjadi pada saham |
| **Jaminan** | Tidak ada pihak yang mengetahui apa pun tentang masukan pihak lain |
| **Di atas** | Biaya komunikasi dan komputasi yang signifikan |
| **Kasus penggunaan** | Bank menghitung model risiko bersama tanpa berbagi data nasabah |
### Enkripsi Homomorfik (HE)
Lakukan komputasi secara langsung pada data terenkripsi.
| Ketik | Apa yang Didukungnya | Atas |
|------|--|----------|
| **Sebagian HE** | Satu operasi (penjumlahan ATAU perkalian) | Rendah |
| **Agak DIA** | Terbatasnya jumlah kedua operasi | Sedang |
| **Sepenuhnya DIA** | Perhitungan sewenang-wenang | Sangat tinggi (perlambatan 100-1000x) |
| Aplikasi | Deskripsi |
|-------------|-------------|
| **Inferensi pribadi** | Jalankan model ML pada data terenkripsi; kembalikan prediksi terenkripsi |
| **Pelatihan terenkripsi** | Melatih data terenkripsi (sebagian besar masih bersifat teoritis untuk pembelajaran mendalam) |
| **Pertanyaan pribadi** | Kueri database tanpa mengungkapkan kueri atau data |
### Lingkungan Eksekusi Tepercaya (TEE)
Isolasi berbasis perangkat keras (Intel SGX, ARM Trustzone) yang melindungi data bahkan dari OS.
| Keuntungan | Batasan |
|-----------|------------|
| Performa mendekati asli | Membutuhkan perangkat keras khusus |
| Jaminan keamanan yang kuat | Memori terbatas (ukuran enklave) |
| Tidak ada overhead kriptografi | Serangan saluran samping mungkin terjadi |
---

## Peraturan Privasi dan ML
| Peraturan | Wilayah | Dampak pada ML |
|------------|--------|-------------|
| **GDPR** | UE | Hak atas penjelasan; minimalisasi data; persetujuan untuk pemrosesan; hak untuk menghapus |
| **CCPA** | Kalifornia | Hak untuk mengetahui, menghapus, dan memilih tidak ikut penjualan data |
| **HIPAA** | AS (layanan kesehatan) | Kontrol ketat terhadap data kesehatan; persyaratan de-identifikasi |
| **PIPL** | Cina | Lokalisasi data; persyaratan persetujuan; aturan transfer lintas batas |
| **Tindakan AI** | UE | Persyaratan transparansi; klasifikasi risiko; praktik terlarang |
### Dampak pada Alur Kerja ML
| Prinsip GDPR | Implikasi ML |
|----------------|---------------|
| **Minimalisasi data** | Kumpulkan hanya yang diperlukan; pembelajaran gabungan membantu |
| **Batasan tujuan** | Tidak dapat menggunakan kembali data tanpa persetujuan baru |
| **Hak untuk menghapus** | Harus dapat menghapus data seseorang dari model terlatih (machine unlearning) |
| **Hak atas penjelasan** | Model harus cukup dapat diinterpretasikan untuk menjelaskan prediksi individu |
| **Privasi berdasarkan desain** | Privasi harus dibangun ke dalam sistem sejak awal |
---

## Tantangan
| Tantangan | Deskripsi |
|-----------|-------------|
| **Biaya komunikasi** | Mengirim pembaruan model ke jutaan perangkat itu mahal |
| **Data non-IID** | Perangkat memiliki distribusi data yang sangat berbeda, sehingga mengganggu konvergensi |
| **Orang yang tersesat** | Perangkat lambat menunda seluruh putaran |
| **Pertukaran privasi-utilitas** | Privasi yang lebih kuat berarti kinerja model yang lebih buruk |
| **Serangan keracunan** | Peserta yang jahat dapat merusak model global |
| **Ekstraksi model** | Bahkan pembaruan model bersama dapat membocorkan informasi tentang data pelatihan |
| **Heterogenitas perangkat keras** | Perangkat yang berbeda memiliki kemampuan komputasi yang berbeda |
---

## Alat dan Kerangka
| Alat | Tujuan |
|------|---------|
| **Bunga** | Kerangka pembelajaran gabungan sumber terbuka; kerangka-agnostik |
| **TensorFlow Federasi** | Framework FL Google untuk model TensorFlow |
| **PySyft** (Penambangan Terbuka) | ML yang menjaga privasi di PyTorch |
| **NASIB** (Webank) | Platform pembelajaran gabungan tingkat industri |
| **DAUN** | Rangkaian tolok ukur untuk penelitian pembelajaran gabungan |
| **Opaku** (Meta) | Privasi diferensial untuk PyTorch |
| **Privasi TF Google** | Privasi diferensial untuk TensorFlow |
---

## Ringkasan
Pembelajaran gabungan dan teknik menjaga privasi mengatasi permasalahan mendasar: bagaimana Anda membangun model AI yang kuat ketika data didistribusikan, sensitif, atau diatur? Pembelajaran gabungan menyimpan data di perangkat dan hanya membagikan pembaruan model. Privasi diferensial menambahkan jaminan matematis bahwa kontribusi individu tidak dapat dideteksi. Komputasi yang aman dan enkripsi homomorfik melangkah lebih jauh, memungkinkan komputasi pada data terenkripsi. Masing-masing teknik mempunyai biaya – overhead komunikasi, berkurangnya akurasi, biaya komputasi – namun secara keseluruhan ketiga teknik tersebut membentuk perangkat untuk membangun AI yang menghormati privasi sambil tetap belajar dari data dunia.