---
# Metadata
title: "AI Ethics and Governance"
description: "AI bias, fairness, accountability, regulation, governance frameworks"
category: "AI and Machine Learning"
subcategory: "Ethics and Safety"
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
    changes: "Moved to ethics_and_safety/ subfolder; added subcategory field"
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
tags: [ai, ethics, governance, ai-and-machine-learning]
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
# Etika dan Tata Kelola AI
Sistem AI tidak netral. Mereka mencerminkan data yang menjadi dasar pelatihan mereka, nilai-nilai penciptanya, dan insentif dari organisasi yang menerapkannya. Etika bukan sekedar menanyakan "dapatkah kita membangun ini?" tapi "haruskah kita melakukannya?" Tata kelola adalah tentang menciptakan struktur – undang-undang, standar, badan pengawas – yang memastikan AI dikembangkan dan digunakan secara bertanggung jawab. File ini mencakup dimensi etika utama AI dan kerangka tata kelola yang muncul untuk mengatasinya.
---

## Prinsip Inti Etika untuk AI
Sebagian besar kerangka etika AI menyatu pada serangkaian prinsip bersama.
| Prinsip | Apa Artinya | Tantangan |
|-----------|--------------|-----------|
| **Keadilan** | AI tidak boleh mendiskriminasi kelompok yang dilindungi | Mendefinisikan keadilan secara matematis sangatlah sulit; definisi keadilan yang berbeda dapat menimbulkan konflik |
| **Transparansi** | Pengguna harus mengetahui kapan mereka berinteraksi dengan AI dan cara kerjanya | Transparansi penuh dapat memungkinkan bermain game; sistem kepemilikan menolak pengungkapan |
| **Akuntabilitas** | Seseorang harus bertanggung jawab ketika AI menyebabkan kerugian | Menyebarkan tanggung jawab antar pengembang, penyebar, dan pengguna |
| **Privasi** | AI harus menghormati data pribadi dan otonomi | Data pelatihan sering kali mencakup informasi pribadi; konflik privasi dan utilitas |
| **Keamanan** | AI tidak boleh menyebabkan kerugian fisik atau psikologis | Mendefinisikan kerugian bergantung pada konteks; kasus tepi tidak dapat diprediksi |
| **Pengawasan manusia** | Manusia harus mempertahankan kendali yang berarti | Bias otomasi berarti manusia tunduk pada AI; pengawasan menjadi stempel |
---

## Bias dalam Sistem AI
### Dari Mana Bias Berasal
| Sumber | Deskripsi | Contoh |
|--------|-------------|---------|
| **Data pelatihan** | Bias historis yang dikodekan dalam data | Data perekrutan mencerminkan diskriminasi di masa lalu → model melakukan diskriminasi |
| **Bias label** | Anotator manusia memaksakan bias mereka | Resume dengan nama "perempuan" dinilai lebih rendah oleh anotator |
| **Bias seleksi** | Data tidak mewakili populasi sasaran | Pengenalan wajah sebagian besar dilatih pada wajah berkulit terang |
| **Bias pengukuran** | Fitur proxy untuk atribut yang dilindungi | Kode pos berkorelasi dengan ras |
| **Bias algoritma** | Optimasi memperkuat bias kecil | Kesenjangan kecil dalam data pelatihan menjadi kesenjangan besar dalam prediksi |
### Metrik Kewajaran
| Metrik | Definisi | Kapan Menggunakan |
|--------|-----------|-------------|
| **Kesetaraan demografi** | Tingkat positif sama antar kelompok | Bila Anda menginginkan hasil yang sama |
| **Peluang yang disamakan** | Tingkat positif benar dan tingkat positif palsu sama di seluruh kelompok | Bila Anda ingin tingkat kesalahan yang sama |
| **Paritas prediktif** | Presisinya sama antar grup | Bila Anda ingin prediksi mempunyai arti yang sama untuk semua kelompok |
| **Keadilan individu** | Individu serupa diperlakukan sama | Bila Anda menginginkan konsistensi |
**Teorema ketidakmungkinan**: Anda biasanya tidak dapat memenuhi beberapa definisi keadilan secara bersamaan. Memilih metrik keadilan mana yang akan digunakan merupakan pertimbangan nilai.
### Mitigasi Bias
| Tahap | Teknik |
|-------|-----------|
| **Pra-pemrosesan** | Menyeimbangkan kembali data pelatihan; menghapus fitur-fitur yang bias; pengambilan sampel berlebih sintetis |
| **Dalam proses** | Tambahkan batasan keadilan pada fungsi kerugian; debiasasi permusuhan |
| **Pasca-pemrosesan** | Sesuaikan ambang batas per grup; kalibrasi prediksi |
| **Evaluasi** | Audit kewajaran secara berkala; metrik kinerja terpilah |
---

## Penjelasan
### Mengapa Penjelasan Itu Penting
| Alasan | Deskripsi |
|--------|-------------|
| **Kepercayaan** | Pengguna perlu memahami mengapa keputusan itu dibuat |
| **Men-debug** | Pengembang perlu menemukan dan memperbaiki kesalahan model |
| **Peraturan** | "hak atas penjelasan" GDPR; Persyaratan UU AI UE |
| **Keadilan** | Anda tidak dapat mendeteksi bias tanpa memahami perilaku model |
| **Akuntabilitas** | Organisasi perlu membenarkan keputusan otomatis |
### Metode Penjelasan
| Metode | Ketik | Cara Kerja | Batasan |
|--------|------|-------------|------------|
| **BENTUK** | Pentingnya fitur | Memperkirakan kontribusi setiap fitur menggunakan teori permainan | Mahal secara komputasi; perkiraan |
| **jeruk nipis** | Pengganti lokal | Cocok dengan model sederhana seputar prediksi | Tidak stabil; tidak mencerminkan logika model sebenarnya |
| **Visualisasi perhatian** | Mekanisme internal | Tunjukkan input mana yang dilayani oleh model | Perhatian ≠ pentingnya; bisa menyesatkan |
| **Kontrafaktual** | Analisis bagaimana-jika | “Jika fitur ini berbeda, apakah prediksinya akan berubah?” | Tergantung pada kontrafaktual yang realistis |
| **Atribusi fitur** | Skor penting | Peta arti-penting, gradien terintegrasi | Tidak menjelaskan *mengapa*; hanya *dimana* |
---

## Peraturan AI
### Undang-Undang AI UE (2026)
Hukum AI komprehensif pertama di dunia.
| Tingkat Risiko | Contoh | Persyaratan |
|------------|----------|-------------|
| **Risiko yang tidak dapat diterima** | Penilaian sosial; manipulasi bawah sadar; pengawasan biometrik waktu nyata (dengan pengecualian) | Dilarang |
| **Risiko tinggi** | AI medis; kendaraan otonom; penegakan hukum; infrastruktur penting | Penilaian kesesuaian; pengawasan manusia; transparansi |
| **Risiko terbatas** | bot obrolan; palsu; sistem rekomendasi | Harus mengungkapkan keterlibatan AI |
| **Risiko minimal** | Filter spam; permainan video; sebagian besar aplikasi AI | Tidak ada persyaratan khusus |
### Pendekatan Peraturan Lainnya
| Wilayah | Pendekatan | Status |
|--------|----------|--------|
| **Amerika Serikat** | Khusus sektor; perintah eksekutif; komitmen sukarela | Terfragmentasi; tidak ada hukum federal yang komprehensif |
| **Inggris Raya** | Berbasis prinsip; regulator sektor | Institut Keamanan AI; pendekatan pro-inovasi |
| **Cina** | Peraturan khusus untuk AI generatif, deepfake, rekomendasi | Penegakan hukum secara aktif; persyaratan konten |
| **Kanada** | AIDA (Undang-undang Kecerdasan Buatan dan Data) | Diajukan; mirip dengan pendekatan UE |
| **Brasil** | Kerangka regulasi AI | Sedang berlangsung |
---

## Dampak Lingkungan
Pelatihan dan menjalankan model AI menghabiskan energi dan menghasilkan emisi karbon.
| Aktivitas | Perkiraan Emisi | Perbandingan |
|----------|-------------------|------------|
| **Pelatihan GPT-4** | Diperkirakan 50+ ton CO₂ | Setara dengan emisi tahunan beberapa mobil |
| **Melatih Transformer besar** | 280-620 ton CO₂ | 5x emisi seumur hidup mobil |
| **Inferensi harian (1 juta pengguna)** | Sedang berlangsung; tergantung pada ukuran model dan perangkat keras | Dapat melebihi emisi pelatihan dari waktu ke waktu |
| **Menyempurnakan model 7B** | 1-5 ton CO₂ | Signifikan tetapi jauh lebih kecil dibandingkan pra-pelatihan |
### Mitigasi
| Strategi | Dampak |
|----------|--------|
| **Perangkat keras yang efisien** | GPU baru lebih hemat energi per komputasi |
| **Pengoptimalan model** | Model terkuantisasi yang lebih kecil menggunakan lebih sedikit energi |
| **Energi hijau** | Pusat data daya dengan energi terbarukan |
| **Arsitektur yang efisien** | Campuran Ahli; model yang jarang; distilasi |
| **Penjadwalan sadar karbon** | Jalankan pelatihan saat jaringan paling bersih |
---

## Kekayaan Intelektual dan Hak Cipta
| Edisi | Deskripsi | Status |
|-------|-------------|--------|
| **Pelatihan tentang karya berhak cipta** | Model dilatih berdasarkan buku, artikel, gambar tanpa izin | Tuntutan hukum aktif; debat penggunaan wajar |
| **Keluaran yang dihasilkan AI** | Siapa pemilik konten yang dihasilkan oleh AI? | Kantor Hak Cipta AS: Konten yang dihasilkan AI tidak dapat dilindungi hak cipta tanpa kepengarangan manusia yang memadai |
| **Imitasi gaya** | AI bisa meniru gaya artis | Secara hukum berwarna abu-abu; masalah etika |
| **Mekanisme penyisihan** | Beberapa penyedia mengizinkan pembuat konten untuk tidak mengikuti pelatihan | robots.txt; pemfilteran konten |
---

## Pengungkapan yang Bertanggung Jawab
| Prinsip | Deskripsi |
|-----------|-------------|
| **Pengujian pra-penerapan** | Tim merah, audit bias, evaluasi keselamatan sebelum rilis |
| **Penerapan bertahap** | Mulailah dengan akses terbatas; berkembang seiring dengan terbuktinya keamanan |
| **Pelaporan insiden** | Dokumentasikan dan bagikan informasi tentang kegagalan dan kerugian |
| **Hadiah bug** | Hadiahi peneliti eksternal yang menemukan kerentanan |
| **Kartu model** | Kemampuan model dokumen, batasan, dan tujuan penggunaan |
---

## Asal Data
| Kekhawatiran | Deskripsi |
|---------|-------------|
| **Pelatihan transparansi data** | Kebanyakan model frontier tidak mengungkapkan data pelatihannya |
| **Persetujuan** | Apakah data individu digunakan dengan sepengetahuan dan izin mereka? |
| **Keracunan data** | Bisakah penyerang memasukkan data berbahaya ke dalam set pelatihan? |
| **Kartu kumpulan data** | Dokumentasi komposisi dataset, metode pengumpulan, dan batasan |
| **Tanda Air** | Menanamkan penanda tak terlihat dalam konten yang dihasilkan AI untuk mengidentifikasinya |
---

## Kerangka Etika Praktis
### Untuk Pengembang AI
| Pertanyaan | Mengapa Itu Penting |
|----------|---------------|
| **Siapa yang dapat dirugikan oleh sistem ini?** | Mengidentifikasi pemangku kepentingan yang terkena dampak |
| **Apa yang terjadi jika modelnya salah?** | Menilai biaya kesalahan |
| **Dapatkah keputusan model dijelaskan?** | Menentukan persyaratan penjelasan |
| **Apakah data pelatihan representatif?** | Memeriksa bias seleksi dan pengukuran |
| **Apa saja mode kegagalannya?** | Mengantisipasi kasus tepi dan penyalahgunaan |
| **Bagaimana sistem akan dipantau?** | Rencana pengawasan berkelanjutan |
### Untuk Organisasi yang Menerapkan AI
| Latihan | Deskripsi |
|----------|-------------|
| **Dewan tata kelola AI** | Tim lintas fungsi meninjau penerapan AI |
| **Penilaian dampak** | Evaluasi potensi bahaya sebelum penerapan |
| **Proses pengawasan manusia** | Hapus jalur eskalasi ketika AI membuat kesalahan |
| **Audit rutin** | Periksa bias, penyimpangan, dan konsekuensi yang tidak diinginkan |
| **Saluran masukan pengguna** | Izinkan orang yang terkena dampak untuk melaporkan masalah |
| **Dokumentasi** | Menyimpan catatan keputusan model dan alasan |
---

## Ringkasan
Etika dan tata kelola AI adalah persyaratan teknis. Bias, ketidakjelasan, kerugian lingkungan, dan pelanggaran privasi bukan hanya masalah etika; itu adalah cacat yang menyebabkan kerugian nyata. Lanskap tata kelola berkembang pesat, dengan Undang-undang AI UE yang menetapkan standar global. Regulasi saja tidak cukup – keadilan, penjelasan, dan akuntabilitas harus diintegrasikan ke dalam pekerjaan sehari-hari setiap pengembang AI. Pertanyaan utamanya adalah bagaimana membangun sistem yang layak dipercaya.