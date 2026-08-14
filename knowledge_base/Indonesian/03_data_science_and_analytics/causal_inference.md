---
# Metadata
title: "Causal Inference"
description: "DAGs, confounders, difference-in-differences, instrumental variables"
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
tags: [causal, inference, data-science-and-analytics]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "5 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Inferensi Kausal
Inferensi kausal adalah ilmu yang menentukan apakah suatu hal benar-benar menyebabkan hal lain — bukan hanya apakah hal-hal tersebut berkorelasi. Korelasi memberitahu Anda bahwa dua variabel bergerak bersama. Sebab-akibat memberitahu Anda bahwa mengubah yang satu akan mengubah yang lain. Perbedaan ini sangat penting dalam bidang kedokteran (apakah obat ini manjur?), kebijakan (apakah intervensi ini mengurangi kemiskinan?), dunia usaha (apakah kampanye iklan ini meningkatkan penjualan?), dan ilmu pengetahuan (apakah mekanisme ini menjelaskan fenomena tersebut?).
---

## Korelasi vs Penyebab
| Konsep | Deskripsi | Contoh |
|---------|-------------|---------|
| **Korelasi** | Dua variabel bergerak bersama | Penjualan es krim dan kematian akibat tenggelam meningkat di musim panas |
| **Penyebab** | Satu variabel secara langsung mempengaruhi | Merokok menyebabkan kanker paru-paru |
| **Membingungkan** | Variabel ketiga menyebabkan keduanya | Cuaca panas menyebabkan penjualan es krim dan berenang (dan tenggelam) |
| **Penyebab terbalik** | Akibat sebenarnya menyebabkan dugaan penyebab | Orang membeli suplemen kesehatan karena sakit, bukan sebaliknya |
| **Korelasi palsu** | Hubungan kebetulan | Konsumsi keju per kapita berkorelasi dengan kematian akibat terbelit sprei |
---

## Kerangka Hasil Potensial
### Model Kausal Rubin
| Konsep | Deskripsi |
|---------|-------------|
| **Potensi hasil** | Untuk setiap unit, terdapat hasil jika diberi perlakuan Y(1) dan hasil jika tidak diberi perlakuan Y(0) |
| **Efek pengobatan** | Perbedaannya: Y(1) - Y(0) untuk satuan tertentu |
| **Masalah mendasar** | Kita tidak pernah bisa mengamati Y(1) dan Y(0) untuk satuan yang sama — kita hanya bisa melihat satu |
| **Efek Perawatan Rata-Rata (ATE)** | Rata-rata efek pengobatan individu di seluruh populasi |
| **Kontrafaktual** | Hasil yang tidak teramati — apa yang akan terjadi pada kondisi lain |
### Asumsi Utama
| Asumsi | Arti | Cara Memuaskan |
|-----------|--------|----------------|
| **Ketidaktahuan (ketidakbingungan)** | Penugasan pengobatan tidak bergantung pada hasil potensial, mengingat kovariat yang diamati | Pengacakan; mengukur semua perancu |
| **Positif (tumpang tindih)** | Setiap unit mempunyai peluang bukan nol untuk menerima salah satu perlakuan | Periksa kovariat yang tumpang tindih antar kelompok |
| **SUTVA** (Asumsi Nilai Perawatan Satuan Stabil) | Perlakuan pada satu unit tidak mempengaruhi hasil unit lainnya; pengobatannya konsisten | Tidak ada gangguan; tidak ada versi pengobatan yang tersembunyi |
| **Konsistensi** | Hasil yang diamati sama dengan hasil potensial berdasarkan pengobatan yang diterima | Perawatan yang terdefinisi dengan baik |
---

## Metode Inferensi Kausal
### Metode Eksperimental
| Metode | Deskripsi | Kekuatan | Batasan |
|--------|-------------|----------|------------|
| **Uji coba terkontrol secara acak (RCT)** | Tetapkan unit secara acak untuk perlakuan atau kontrol | Standar emas; menghilangkan perancu | Mahal; terkadang tidak etis; tidak boleh menggeneralisasi |
| **Pengujian A/B** | RCT dalam konteks bisnis/teknologi | Sederhana; ketat | Metrik jangka pendek; efek kebaruan; gangguan |
| **Eksperimen peralihan balik** | Pengobatan alternatif dalam jangka waktu tertentu | Menangani gangguan di pasar | Membutuhkan lingkungan yang stabil |
### Metode Kuasi Eksperimental
| Metode | Deskripsi | Asumsi Kunci |
|--------|-------------|----------------|
| **Perbedaan dalam Perbedaan (DiD)** | Bandingkan perubahan hasil antara kelompok yang diberi perlakuan dan kelompok kontrol dari waktu ke waktu | Tren paralel: kelompok akan mengikuti jalur yang sama tanpa pengobatan |
| **Diskontinuitas regresi (RD)** | Bandingkan unit tepat di atas dan tepat di bawah batas pengobatan | Unit-unit di dekat titik potong dapat dibandingkan (seolah-olah acak) |
| **Variabel instrumental (IV)** | Gunakan variabel yang mempengaruhi pengobatan tetapi tidak mempengaruhi hasil kecuali melalui pengobatan | Instrumen dikorelasikan dengan pengobatan; mempengaruhi hasil hanya melalui pengobatan |
| **Kontrol sintetis** | Buatlah kombinasi tertimbang dari unit kontrol agar sesuai dengan unit yang diberi perlakuan | Kontrol sintetis secara akurat mewakili kontrafaktual | unit yang dirawat
| **Pencocokan skor kecenderungan** | Cocokkan unit yang diberi perlakuan dan unit kontrol dengan probabilitas perlakuan yang serupa | Semua perancu diukur dan dimasukkan dalam model kecenderungan |
### Perbedaan-dalam-Perbedaan (Divisualisasikan)
| Periode | Grup yang Diperlakukan | Grup Kontrol | Perbedaan |
|--------|--------------|---------------|------------|
| **Pra-perawatan** | Y_t_pra | Y_c_pre | Y_t_pre - Y_c_pre |
| **Pasca perawatan** | Y_t_posting | Y_c_posting | Y_t_posting - Y_c_posting |
| **Perkiraan berhasil** | | | (Y_t_post - Y_t_pre) - (Y_c_post - Y_c_pre) |
---

## Grafik Asiklik Terarah (DAG)
DAG adalah alat visual untuk mengkodekan asumsi sebab akibat dan mengidentifikasi perancu.
### Struktur Dasar
| Struktur | Pola | Implikasi |
|-----------|---------|-------------|
| **Rantai** | A → B → C | A dan C dihubungkan melalui B; mengendalikan B memblokir jalur |
| **Garpu** | A ← B → C | A dan C dibingungkan oleh B; mengendalikan B memblokir jalur |
| **Tabrakan** | A → B ← C | A dan C saling independen; mengendalikan B membuka jalur (menciptakan asosiasi palsu) |
### Aturan untuk DAG
| Aturan | Deskripsi |
|------|-------------|
| **Kriteria pintu belakang** | Untuk memperkirakan dampak sebab akibat dari X pada Y, blok semua jalur pintu belakang (jalur dengan panah ke X) dengan mengondisikan variabel |
| **Kriteria pintu depan** | Jika jalur pintu belakang tidak dapat diblokir, gunakan mediator: perkirakan X → M → Y dalam dua tahap |
| **Jangan mengkondisikan pada collider** | Mengontrol efek umum membuka jalur palsu |
| **Jangan mengkondisikan keturunan collider** | Masalah yang sama seperti pengkondisian pada collider itu sendiri |
---

## Kesalahan Umum
| Jebakan | Deskripsi | Contoh |
|---------|-------------|---------|
| **Bias variabel dihilangkan** | Gagal mengendalikan perancu | Memperkirakan pendidikan → penghasilan tanpa mengontrol kemampuan |
| **Pengendalian berlebihan** | Pengkondisian pada mediator atau collider | Mengontrol jabatan saat memperkirakan pendidikan → penghasilan |
| **Bias seleksi** | Pengkondisian pada variabel yang dipengaruhi oleh perlakuan | Hanya menganalisis orang-orang yang bekerja ketika mempelajari pelatihan → upah |
| **Bias waktu abadi** | Kesalahan mengklasifikasikan waktu orang dalam studi kohort | Pasien harus bertahan hidup cukup lama untuk menerima pengobatan |
| **Regresi terhadap mean** | Nilai ekstrim cenderung bergerak menuju rata-rata | Pasien yang sakit membaik setelah pengobatan |
| **Bias pasca perawatan** | Pengkondisian pada variabel yang terjadi setelah perlakuan | Mengontrol efek samping saat memperkirakan kemanjuran obat |
---

## Alat dan Perpustakaan
| Alat | Bahasa | Deskripsi |
|------|----------|-------------|
| **LakukanMengapa** | ular piton | perpustakaan Microsoft; Inferensi kausal berbasis DAG |
| **ML Kausal** | ular piton | Perpustakaan Uber untuk pemodelan peningkatan dan ML kausal |
| **EkonML** | ular piton | ML ganda, hutan sebab akibat, variabel instrumental |
| **model linier** | ular piton | IV, model data panel, DiD |
| **Cocokkan** | R | Pencocokan skor kecenderungan |
| **dagitty** | R / web | analisis DAG; mengidentifikasi set penyesuaian |
| **Dampak Kausal** | R/Python | Deret waktu struktural Bayesian untuk inferensi kausal |
---

## Ringkasan
Inferensi kausal adalah tentang berpindah dari “apa yang terjadi” menjadi “apa yang akan terjadi jika segala sesuatunya berbeda.” Tantangan mendasarnya adalah kita tidak akan pernah bisa mengamati hasil yang diberi perlakuan dan tidak ditangani pada unit yang sama – kontrafaktualnya selalu hilang. Eksperimen acak memecahkan masalah ini dengan membuat kelompok perlakuan dan kelompok kontrol sebanding. Ketika pengacakan tidak memungkinkan, metode eksperimen semu — DiD, diskontinuitas regresi, variabel instrumental, kontrol sintetik — mencoba merekonstruksi kontrafaktual dari data observasi. DAG membantu membuat asumsi menjadi eksplisit dan mengidentifikasi variabel yang tepat untuk dikontrol. Keterampilan kuncinya adalah memikirkan secara hati-hati proses pembuatan data: apa yang menyebabkan apa, apa yang menjadi perancu, apa yang menjadi penghambat, dan apa yang akan terjadi jika ada alternatif lain.