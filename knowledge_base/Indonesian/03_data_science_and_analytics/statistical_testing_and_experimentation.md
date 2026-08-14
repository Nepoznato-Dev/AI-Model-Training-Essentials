<!--
---
# Metadata
title: "Statistical Testing and Experimentation"
description: "Hypothesis testing, A/B testing, effect size, causal inference"
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
tags: [statistical, testing, experimentation, data-science-and-analytics]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "10 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Pengujian Statistik dan Eksperimen
Statistika adalah tata bahasa ilmu pengetahuan. Ini memberi Anda alat untuk membedakan pola nyata dari gangguan acak, untuk mengukur apakah suatu perubahan benar-benar memperbaiki keadaan, dan untuk membuat keputusan dalam kondisi ketidakpastian. File ini mencakup konsep inti pengujian hipotesis, desain eksperimental, dan kendala umum yang membuat orang tersandung.
---

## Kerangka Pengujian Hipotesis
Setiap uji statistik mengikuti logika yang sama:
1. **Nyatakan hipotesis nol (H₀)** : Tidak ada pengaruh/tidak ada perbedaan.
2. **Nyatakan hipotesis alternatif (H₁)** : Terdapat pengaruh/perbedaan.
3. **Pilih tingkat signifikansi (α)**: Biasanya 0,05 (5% kemungkinan positif palsu).
4. **Kumpulkan data dan hitung statistik pengujian**.
5. **Hitung nilai p**: Probabilitas mengamati hasil ini (atau lebih ekstrim) jika H₀ benar.
6. **Buat keputusan**: Jika p < α, tolak H₀ (signifikan secara statistik). Jika tidak, gagal menolak H₀.
### Konsep Utama
| Konsep | Arti | Kesalahpahaman Umum |
|---------|---------|---------------------|
| **nilai-p** | P(data \| H₀ benar) | BUKAN "probabilitas H₀ benar" |
| **α (tingkat signifikansi)** | Ambang batas penolakan H₀ | Bukan ukuran pentingnya efek |
| **Signifikansi statistik** | Hasil tidak mungkin karena kebetulan saja | TIDAK berarti signifikan secara praktis |
| **Ukuran efek** | Besaran efek yang diamati | Pisahkan dari nilai p; efek kecil bisa menjadi signifikan dengan N | yang besar
| **Kekuatan** | Probabilitas menolak H₀ | palsu dengan benar Biasanya bertujuan untuk 80%+ |
| **Interval kepercayaan** | Rentang nilai yang masuk akal untuk parameter | CI 95% tidak berarti "95% kemungkinan nilai sebenarnya berada dalam kisaran ini" |
---

## Jenis Kesalahan
| | H₀ Benar | H₀ Salah |
|---|-----------|------------|
| **Tolak H₀** | Kesalahan Tipe I (positif palsu) | ✅ Benar (benar positif) |
| **Gagal menolak H₀** | ✅ Benar (negatif sebenarnya) | Kesalahan Tipe II (negatif palsu) |
| Kesalahan | Simbol | Arti |
|-------|--------|---------|
| **Tipe I** | | Menyimpulkan ada efek padahal tidak ada |
| **Tipe II** | | Hilangnya efek nyata |
---

## Memilih Tes yang Tepat
| Skenario | Tes | Asumsi |
|----------|------|-------------|
| Bandingkan rata-rata 2 kelompok | **uji-t** (independen) | Distribusi normal, varians sama |
| Bandingkan cara observasi berpasangan | **Uji-t berpasangan** | Selisihnya berdistribusi normal |
| Bandingkan rata-rata 3+ grup | **ANOVA** | Distribusi normal, varians sama |
| Bandingkan distribusi kategorikal | **Uji chi-kuadrat** | Ukuran sampel yang cukup per sel |
| Bandingkan distribusi (non-parametrik) | **Mann-Whitney U** | Tidak ada asumsi normalitas |
| Bandingkan 3+ grup (non-parametrik) | **Kruskal-Wallis** | Tidak ada asumsi normalitas |
| Uji korelasi | **Pearson** (linier) atau **Spearman** (monoton) | Pearson: normalitas; Spearman: berdasarkan peringkat |
| Uji apakah data mengikuti distribusi | **Kolmogorov-Smirnov** | Data berkelanjutan |
### Parametrik vs Non-Parametrik
| | Parametrik | Non-Parametrik |
|---|-----------|---------------|
| **Asumsi** | Data mengikuti distribusi tertentu (biasanya normal) | Tidak ada asumsi distribusi |
| **Kekuatan** | Lebih tinggi bila asumsi terpenuhi | Lebih rendah, tapi lebih kuat |
| **Kapan menggunakan** | Sampel besar, data mendekati normal | Sampel kecil, data miring, data ordinal |
---

## Tes Spesifik Secara Detail
### Uji-t
Membandingkan rata-rata dua kelompok.
| Varian | Kasus Penggunaan |
|---------|----------|
| **Uji-t independen** | Dua kelompok terpisah (perlakuan vs kontrol) |
| **Uji-t berpasangan** | Kelompok yang sama diukur dua kali (sebelum vs sesudah) |
| **Uji-t satu sampel** | Bandingkan mean sampel dengan nilai yang diketahui |
```python
from scipy import stats

# Independent t-test
t_stat, p_value = stats.ttest_ind(group_a, group_b)
```

### ANOVA (Analisis Varians)
Membandingkan berarti melintasi 3 kelompok atau lebih. Menguji apakah setidaknya satu rata-rata kelompok berbeda dari yang lain.
| Ketik | Desain |
|------|--------|
| **ANOVA satu arah** | Satu variabel independen dengan 3+ level |
| **ANOVA dua arah** | Dua variabel independen; menguji efek interaksi |
| **Pengukuran Berulang ANOVA** | Subyek yang sama diukur dalam kondisi berbeda |
Jika ANOVA signifikan, tindak lanjuti dengan **tes post-hoc** (HSD Tukey) untuk menemukan kelompok tertentu yang berbeda.
### Uji Chi-Kuadrat
Menguji apakah dua variabel kategori bersifat independen.
| Kasus Penggunaan | Contoh |
|----------|---------|
| **Uji Kemerdekaan** | Apakah gender dikaitkan dengan preferensi produk? |
| **Kesesuaian** | Apakah pelemparan dadu mengikuti distribusi seragam? |
**Aturan praktis**: setiap sel harus memiliki jumlah yang diharapkan minimal 5.
---

## Pengujian A/B
Pengujian A/B adalah penerapan pengujian hipotesis pada keputusan bisnis — biasanya membandingkan kontrol (A) dengan varian (B).
### Proses Desain
| Langkah | Deskripsi |
|------|-------------|
| **1. Definisikan hipotesis** | "Mengubah warna tombol dari biru menjadi hijau akan meningkatkan rasio klik-tayang" |
| **2. Pilih metrik** | Utama: rasio klik-tayang. Sekunder: tingkat konversi, pendapatan. |
| **3. Hitung ukuran sampel** | Berdasarkan efek minimum yang dapat dideteksi, kekuatan (80%), dan signifikansi (5%) |
| **4. Acak** | Tetapkan pengguna secara acak untuk kontrol dan pengobatan |
| **5. Jalankan eksperimen** | Kumpulkan data hingga ukuran sampel target tercapai |
| **6. Analisis** | Bandingkan metrik menggunakan uji statistik yang sesuai |
| **7. Putuskan** | Terapkan jika signifikan secara statistik dan praktis |
### Perhitungan Ukuran Sampel
Ukuran sampel yang Anda butuhkan bergantung pada:
| Faktor | Pengaruh terhadap Ukuran Sampel |
|--------|----------------------|
| **Efek lebih kecil untuk dideteksi** | Perlu lebih banyak sampel |
| **Kekuatan lebih tinggi** | Perlu lebih banyak sampel |
| **Tingkat signifikansi lebih rendah** | Perlu lebih banyak sampel |
| **Varians lebih tinggi** | Perlu lebih banyak sampel |
### Kesalahan Umum Pengujian A/B
| Kesalahan | Mengapa Itu Salah |
|---------|---------------|
| **Mengintip lebih awal** | Memeriksa hasil setiap hari meningkatkan tingkat positif palsu |
| **Beberapa metrik tanpa koreksi** | Menguji 20 metrik pada α=0,05 → mengharapkan 1 positif palsu secara kebetulan |
| **Berhenti sebelum target N** | Tes yang kurang bertenaga tidak dapat mendeteksi efek nyata |
| **Mengabaikan musim** | Menjalankan tes selama periode liburan vs minggu normal |
| **Penugasan non-acak** | Bias seleksi (misalnya, menugaskan pengguna baru untuk menjalani pengobatan) |
| **Membingungkan signifikansi dengan kepentingan** | Peningkatan sebesar 0,1% bisa menjadi signifikan secara statistik tetapi tidak layak untuk dikirimkan |
---

## Beberapa Perbandingan
Saat Anda menjalankan banyak tes secara bersamaan, kemungkinan terjadinya setidaknya satu positif palsu meningkat secara dramatis.
| Jumlah Tes | Probabilitas ≥1 Positif Palsu (pada α=0,05) |
|----------------|-------------------------------|
| 1 | 5% |
| 5 | 23% |
| 10 | 40% |
| 20 | 64% |
### Koreksi
| Metode | Cara Kerja | Kapan Menggunakan |
|--------|-------------|-------------|
| **Bonferroni** | Bagilah α dengan jumlah tes (α/n) | Konservatif; sedikit perbandingan |
| **Holm-Bonferroni** | Prosedur penurunan; kurang konservatif | Penggunaan umum |
| **Benjamini-Hochberg (FDR)** | Mengontrol tingkat penemuan palsu | Banyak ujian; analisis eksplorasi |
---

## Ukuran Efek
Nilai-P memberi tahu Anda *apakah* suatu efek ada. Ukuran efek memberi tahu Anda *seberapa besar* efeknya.
| Ukur | Untuk | Interpretasi |
|---------|-----|---------------|
| **Makanan Cohen** | Perbedaan antara dua cara | 0,2 = kecil, 0,5 = sedang, 0,8 = besar |
| **Kamar Pearson** | Korelasi | 0,1 = kecil, 0,3 = sedang, 0,5 = besar |
| **η² (eta-kuadrat)** | ANOVA | 0,01 = kecil, 0,06 = sedang, 0,14 = besar |
| **Rasio Peluang** | Hasil kategorikal | 1,0 = tidak berpengaruh; >1 atau <1 = efek |
**Selalu laporkan ukuran efek bersama dengan nilai p.** Hasil bisa signifikan secara statistik namun secara praktis tidak ada artinya.
---

## Bayesian vs Sering
| Aspek | Sering | Bayesian |
|--------|------------|----------|
| **Probabilitas** | Frekuensi kejadian jangka panjang | Derajat Keyakinan |
| **Parameter** | Diperbaiki tetapi tidak diketahui | Variabel acak dengan distribusi |
| **Kegunaan** | nilai p, interval kepercayaan, uji hipotesis | Distribusi posterior, interval yang kredibel |
| **Sebelumnya** | Tidak ada keyakinan sebelumnya yang dimasukkan | Distribusi sebelumnya yang eksplisit |
| **Interpretasi** | "Jika kita mengulangi percobaan ini berkali-kali..." | "Mengingat datanya, kemungkinan bahwa..." |
| **Kekuatan** | Objektif, mapan, sederhana | Interpretasi intuitif, menggabungkan pengetahuan sebelumnya |
| **Kelemahan** | nilai-p banyak disalahpahami | Pilihan prior bisa subjektif |
---

## Dasar-dasar Inferensi Kausal
Korelasi bukanlah sebab-akibat. Namun terkadang Anda perlu mengetahui *apakah X menyebabkan Y*, bukan hanya apakah keduanya terkait.
| Metode | Deskripsi | Kapan Menggunakan |
|--------|-------------|-------------|
| **Eksperimen acak** | Standar emas; penugasan acak menghilangkan perancu | Kapan Anda dapat mengacak |
| **Perbedaan dalam Perbedaan (DiD)** | Bandingkan perubahan dari waktu ke waktu antara pengobatan dan kontrol | Perubahan kebijakan, eksperimen alami |
| **Diskontinuitas Regresi (RDD)** | Memanfaatkan ambang batas | Beasiswa, ambang batas kelayakan |
| **Variabel Instrumental (IV)** | Gunakan instrumen yang mempengaruhi pengobatan tetapi tidak mempengaruhi hasil secara langsung | Ketika pengacakan tidak memungkinkan |
| **Pencocokan Skor Kecenderungan** | Cocokkan unit yang diberi perlakuan dan unit kontrol berdasarkan karakteristik yang diamati | Studi observasional |
---

## Kesalahan Statistik Umum
| Kesalahan | Deskripsi |
|---------|-------------|
| **p-peretasan** | Mencoba banyak analisis sampai Anda menemukan p <0,05 |
| **Mendengar** | Membuat Hipotesis Setelah Hasil Diketahui |
| **Bias bertahan hidup** | Hanya melihat kesuksesan (misalnya, perusahaan sukses) |
| **Paradoks Simpson** | Tren berbalik ketika data dikumpulkan vs dipisahkan berdasarkan grup |
| **Pengabaian tarif dasar** | Mengabaikan probabilitas sebelumnya saat menafsirkan hasil |
| **Kekeliruan ekologi** | Menyimpulkan perilaku individu dari data tingkat kelompok |
| **Membingungkan** | Variabel ketiga menjelaskan hubungan yang diamati |
| **Kelebihan Kesesuaian** | Model menangkap kebisingan, bukan sinyal |
---

## Ringkasan
Pengujian statistik adalah tentang pengambilan keputusan dalam ketidakpastian dengan kejujuran intelektual. Selalu nyatakan hipotesis Anda sebelum mengumpulkan data. Pilih pengujian yang tepat untuk tipe data Anda. Laporkan ukuran efek, bukan hanya nilai p. Benar untuk beberapa perbandingan. Dan ingat: signifikansi statistik tidak sama dengan signifikansi praktis.