# Evaluasi Pembelajaran Mesin dan Alur Kerja

Panduan praktis untuk siklus hidup ML — mulai dari penyusunan masalah hingga pemantauan produksi — dengan fokus pada metrik, validasi, dan proses debug.

---

## Alur Kerja ML (CRISP-ML)

1. **Pemahaman Bisnis**: Tentukan tujuan dan kriteria keberhasilan.
2. **Pemahaman Data**: Jelajahi data yang tersedia, identifikasi masalah kualitas.
3. **Persiapan Data**: Membersihkan, mengubah, dan memisahkan data.
4. **Pemodelan**: Latih model, sesuaikan hyperparameter.
5. **Evaluasi**: Menilai kinerja berdasarkan metrik.
6. **Deployment**: Melayani model dalam produksi.
7. **Pemantauan**: Melacak penyimpangan, kinerja, dan anomali.

Ini adalah perulangan berulang — Anda akan meninjau kembali langkah-langkah sebelumnya berdasarkan hasil evaluasi.

---

## Pemisahan Data

### Pelatihan / Validasi / Pemisahan Tes
- **Set pelatihan** (~70%): Digunakan untuk menyesuaikan parameter model.
- **Kumpulan validasi** (~15%): Digunakan untuk menyesuaikan hyperparameter dan memilih varian model.
- **Set pengujian** (~15%): Hanya digunakan sekali di akhir untuk memperkirakan performa generalisasi.

**Penting:** Set pengujian harus tetap tidak disentuh hingga evaluasi akhir untuk menghindari kebocoran data.

### Validasi Silang (k-fold)
Untuk kumpulan data kecil, gunakan validasi silang k-fold: bagi data menjadi k lipatan, latih pada k-1, validasi sisanya, dan ulangi sebanyak k kali. Rata-ratakan kinerjanya. k=5 atau k=10 adalah hal biasa.

### Pemisahan Berstrata
Untuk klasifikasi dengan kelas yang tidak seimbang, gunakan pemisahan bertingkat untuk mempertahankan proporsi kelas di setiap subset.

### Pemisahan Berbasis Waktu
Untuk data deret waktu, pisahkan secara kronologis (latih di masa lalu, uji di masa depan) dan bukan secara acak.

---

## Metrik Evaluasi

### Metrik Klasifikasi

| Metrik | Apa yang diukur | Paling baik digunakan untuk |
|--------|------------------|---------------|
| **Akurasi** | (TP + TN) / (TP + TN + FP + FN) | Kumpulan data seimbang |
| **Presisi** | TP / (TP + FP) | Ketika positif palsu itu mahal (misalnya deteksi spam) |
| **Ingat** | TP / (TP + FN) | Ketika hasil negatif palsu mahal (misalnya skrining kanker) |
| **Skor F1** | Arti harmonik dari presisi dan perolehan | Kumpulan data tidak seimbang, metrik angka tunggal |
| **AUC-ROC** | Area di bawah kurva ROC; tradeoff antara TPR dan FPR | Kinerja pengklasifikasi umum tidak bergantung pada ambang batas |
| **AUC-PR** | Area di bawah kurva Precision-Recall | Kumpulan data yang sangat tidak seimbang |

**Definisi:**
- TP = Benar Positif
- TN = Benar Negatif
- FP = False Positive (kesalahan Tipe I)
- FN = False Negative (kesalahan Tipe II)

### Metrik Regresi

| Metrik | Apa yang diukur | Sensitivitas terhadap outlier |
|--------|------------------|--------------------------|
| **MSE** (Kesalahan Kuadrat Rata-rata) | Selisih kuadrat rata-rata | Tinggi |
| **RMSE** (Kesalahan Root Mean Squared) | Akar kuadrat UMK (unit yang sama dengan target) | Tinggi |
| **MAE** (Berarti Kesalahan Absolut) | Beda mutlak rata-rata | Rendah |
| **R²** (Koefisien Tekad) | Proporsi varians dijelaskan | Tidak ada secara langsung, namun sensitif terhadap outlier secara tidak langsung |

### Peringkat dan Metrik Pengambilan
- **Precision@k**: Sebagian kecil item yang relevan di antara rekomendasi teratas.
- **Recall@k**: Bagian dari semua item relevan yang muncul di top-k.
- **NDCG** (Keuntungan Kumulatif Diskon yang Dinormalisasi): Memperhitungkan relevansi posisi.
- **Hit Rate**: Apakah item yang relevan muncul di top-k.

### Metrik Generatif / LLM
- **Kebingungan**: Betapa "terkejutnya" model dengan teks yang dipanjangkan (lebih rendah lebih baik).
- **BLEU**: n-gram tumpang tindih dengan terjemahan referensi (berfokus pada presisi).
- **ROUGE**: Tumpang tindih berorientasi penarikan untuk ringkasan.
- **BERTScore**: Kesamaan semantik menggunakan penyematan kontekstual (lebih kuat dari BLEU).
- **METEOR**: Sejajar dengan sinonim dan batang WordNet.

---

## Kesalahan Evaluasi

### Kebocoran Data
Terjadi ketika informasi dari set tes secara tidak sengaja mempengaruhi pelatihan.
- **Mencegah:** Jangan pernah menggunakan data pengujian untuk rekayasa fitur, normalisasi, atau penyetelan hyperparameter.
- **Deteksi:** Jika skor model Anda sangat tinggi, curigai adanya kebocoran.

### Terlalu pas
Model berkinerja baik pada data pelatihan tetapi buruk pada validasi/pengujian.
- **Mitigasi:** Gunakan regularisasi, penghentian awal, sederhanakan arsitektur, atau kumpulkan lebih banyak data.

### Kurang pas
Model berkinerja buruk pada pelatihan dan validasi.
- **Mitigasi:** Gunakan model yang lebih kompleks, tambahkan fitur, atau kurangi regularisasi.

### Data Tidak Seimbang
- **Mitigasi:** Gunakan bobot kelas, sampel berlebih (SMOTE), sampel kurang, atau gunakan metrik yang sesuai (F1, AUC-PR) daripada akurasi.

### Temporal Drift (Konsep Drift)
Hubungan antara fitur dan target berubah seiring waktu.
- **Mitigasi:** Latih ulang secara berkala, pantau performa, gunakan algoritme deteksi penyimpangan.

---

## Penyetelan Hyperparameter- **Penelusuran Grid**: Coba secara menyeluruh semua kombinasi kumpulan hyperparameter yang telah ditentukan sebelumnya. Sederhana namun mahal secara komputasi.
- **Pencarian Acak**: Contoh kombinasi acak dari distribusi. Lebih efisien daripada pencarian grid untuk ruang berdimensi tinggi.
- **Optimasi Bayesian**: Membangun model probabilistik dari fungsi tujuan dan memilih hyperparameter dengan cerdas. Perpustakaan: Optuna, Hyperopt, scikit-optimise.
- **Penalaan Otomatis**: Gunakan alat seperti Optuna, Ray Tune, atau Weights & Biases Sweeps untuk penyetelan terdistribusi.

**Rentang penelusuran yang disarankan untuk hyperparameter umum:**

| Parameter | Rentang yang disarankan (skala log) |
|-----------|-----------------------------|
| Kecepatan pembelajaran | 1e-5 hingga 1e-1 |
| Ukuran kumpulan | 16, 32, 64, 128, 256 |
| Jumlah lapisan (NN) | 2 sampai 6 |
| Jumlah neuron (NN) | 32 hingga 1024 |
| Regularisasi (L2) | 1e-6 hingga 1e-2 |
| Kedalaman pohon (XGBoost) | 3 sampai 12 |

---

## Pemilihan dan Validasi Model

1. **Model dasar**: Mulailah dengan heuristik sederhana atau model sederhana (misalnya regresi logistik, prediktor rata-rata) untuk menetapkan batas bawah.
2. **Model kandidat**: Melatih beberapa kelompok model (misalnya, Random Forest, XGBoost, Neural Network).
3. **Validasi silang** setiap kandidat pada set validasi.
4. **Bandingkan metrik** (dengan interval kepercayaan) dan pilih kandidat terbaik.
5. **Evaluasi akhir** pada set tes yang diadakan.
6. **Analisis kesalahan**: Lihat contoh kesalahan model. Identifikasi pola (misalnya, kelas langka, masukan ambigu) dan berikan wawasan kembali ke dalam persiapan data atau rekayasa fitur.

---

## Penerapan dan Pemantauan

### Pola Penyajian
- **Inferensi batch**: Memproses data dalam jumlah besar secara offline (misalnya, rekomendasi setiap malam).
- **Inferensi online**: Prediksi real-time melalui API (misalnya, penilaian kredit, deteksi penipuan).
- **Inferensi streaming**: Berdasarkan peristiwa, real-time dengan latensi rendah (misalnya, peringatan sensor IoT).

### Pemantauan Model
- **Pemantauan kinerja**: Akurasi pelacakan/F1 dari waktu ke waktu pada data langsung (bila kebenaran dasar tersedia).
- **Penyimpangan data**: Memantau perubahan dalam distribusi fitur masukan (misalnya, menggunakan PSI – Indeks Stabilitas Populasi).
- **Penyimpangan konsep**: Memantau perubahan hubungan antara input dan output.
- **Penyimpangan prediksi**: Melacak distribusi keluaran yang diprediksi.
- **Latensi dan throughput**: Pastikan SLA (Perjanjian Tingkat Layanan) terpenuhi.

### Pencatatan dan Peringatan
- Catat semua permintaan dan tanggapan prediksi (dengan anonimisasi).
- Atur peringatan untuk:
  - Penurunan kinerja yang signifikan.
  - Tingginya persentase input yang hilang atau tidak valid.
  - Keluaran model di luar batas yang diharapkan.

### Pembuatan Versi Model dan Registri
- Gunakan registri model (misalnya, MLflow, Weights & Biases, Sagemaker Model Registry) untuk menyimpan dan membuat versi model, metadata, dan hasil evaluasi.
- Simpan kode pelatihan dan versi data (melalui DVC atau Git LFS) di samping model.

---

## Daftar Periksa Alur Kerja Praktis

- [ ] Masalah dibingkai dan metrik keberhasilan ditentukan.
- [ ] Eksplorasi data dilakukan (nilai yang hilang, outlier, distribusi).
- [ ] Pemisahan pelatihan/validasi/pengujian dibuat (distratifikasi jika diperlukan).
- [ ] Model dasar ditetapkan.
- [ ] Model kandidat dilatih dan divalidasi.
- [ ] Hyperparameter disetel.
- [ ] Model terbaik dipilih melalui validasi silang.
- [ ] Evaluasi akhir pada set tes.
- [ ] Analisis kesalahan dilakukan.
- [ ] Rencana penerapan sudah siap (melayani infrastruktur).
- [ ] Pengaturan dasbor pemantauan.
- [ ] Dokumentasi (kartu data, kartu model) selesai.