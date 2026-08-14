---
# Metadata
title: "Management and Project Methodologies"
description: "Leadership, Agile/Scrum/Kanban, OKRs, risk management"
category: "Business and Economics"
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
reviewed_by: "Business & Economics Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [management, project, methodologies, business-and-economics]
difficulty_level: "beginner"
prerequisites: []
estimated_reading_time: "12 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# Manajemen dan Metodologi Proyek
Mengelola orang dan proyek adalah salah satu tanggung jawab yang paling menuntut di organisasi mana pun. Keterampilan teknis memberikan jalan masuk, namun kemampuan untuk memimpin tim, membuat keputusan, berkomunikasi secara efektif, dan memberikan hasil menentukan apakah tujuan tercapai. File ini mencakup kerangka kerja, metodologi, dan keterampilan praktis yang diterapkan oleh manajer dan pemimpin proyek yang efektif.
---

## Gaya Kepemimpinan
Tidak ada satu pun cara yang "benar" untuk memimpin. Gaya terbaik bergantung pada tim, tugas, dan konteks.
| Gaya | Deskripsi | Kapan Terbaik | Resiko |
|-------|-------------|----------|------|
| **Otokratis** | Pemimpin membuat keputusan dengan masukan minimal | Krisis; tim yang tidak berpengalaman; tekanan waktu | Semangat rendah; ketergantungan pada pemimpin |
| **Demokrat** | Pemimpin meminta masukan; tim memiliki pengaruh nyata | Tim yang terampil; keputusan kompleks yang membutuhkan dukungan | Keputusan yang lebih lambat; bisa merasa plin-plan |
| **Laissez-faire** | Pemimpin memberikan arahan; tim mengelola sendiri | Pakar yang sangat terampil dan memiliki motivasi diri | Kurangnya koordinasi; akuntabilitas yang tidak jelas |
| **Transformasional** | Pemimpin menginspirasi visi dan pertumbuhan pribadi | Mengubah inisiatif; membangun budaya kinerja tinggi | Dapat terbakar jika tidak di-ground-kan dalam eksekusi |
| **Kepemimpinan yang melayani** | Pemimpin memprioritaskan kebutuhan dan pengembangan tim | Pekerja berpengetahuan; membangun kepercayaan dan loyalitas | Mungkin dianggap lemah dalam budaya hierarki |
| **Situasi** | Pemimpin menyesuaikan gaya dengan kematangan tim dan tugas | Sebagian besar situasi dunia nyata | Membutuhkan kecerdasan emosional yang tinggi |
### Apa yang Sebenarnya Dilakukan Manajer Hebat
Penelitian (terutama dari Project Oxygen Google) mengidentifikasi perilaku terbaik dari manajer yang efektif:
1. **Merupakan pelatih yang baik** — mengajukan pertanyaan, membantu orang berpikir, tidak hanya memberikan jawaban
2. **Memberdayakan tim** — mendelegasikan secara bermakna; tidak mengelola mikro
3. **Menciptakan lingkungan inklusif** — keamanan psikologis; semua orang bisa berkontribusi
4. **Produktif dan berorientasi pada hasil** — membuat tim tetap fokus pada hal yang penting
5. **Merupakan komunikator yang baik** — mendengarkan, berbagi konteks, memberikan arahan yang jelas
6. **Mendukung pengembangan karir** — berbicara tentang pertumbuhan, bukan hanya tugas
7. **Memiliki visi dan strategi yang jelas** — mengetahui tujuan tim dan alasannya
8. **Memiliki keterampilan teknis utama** — dapat memberi saran dan memahami pekerjaan (meskipun tidak melakukannya)
---

## Metodologi Manajemen Proyek
### Tradisional (Air Terjun)
| Fase | Kegiatan |
|-------|-----------|
| **Persyaratan** | Kumpulkan dan dokumentasikan apa saja yang perlu dibangun |
| **Desain** | Arsitektur, spesifikasi, rencana |
| **Implementasi** | Bangun benda |
| **Pengujian** | Verifikasi itu berfungsi seperti yang ditentukan |
| **Penerapan** | Rilis ke produksi/pengguna |
| **Pemeliharaan** | Perbaiki masalah; dukungan berkelanjutan |
**Terbaik untuk**: Konstruksi, manufaktur, industri teregulasi yang persyaratannya tetap dan perubahannya mahal.
### Lincah
Agile adalah pola pikir, bukan metodologi. Itu berasal dari[Agile Manifesto](https://agilemanifesto.org/)(2001):
> *Individu dan interaksi* atas proses dan alat
> *Perangkat lunak yang berfungsi* melalui dokumentasi yang komprehensif
> *Kolaborasi pelanggan* melalui negosiasi kontrak
> *Menanggapi perubahan* dalam mengikuti rencana
| Prinsip Tangkas | Apa Artinya dalam Praktek |
|----------------|--------------------------|
| Sering mengirimkan perangkat lunak yang berfungsi | Iterasi singkat (1–4 minggu) |
| Selamat datang perubahan persyaratan | Bahkan terlambat dalam pengembangan |
| Bisnis dan pengembang bekerja sama | Kolaborasi harian, tidak hanya di awal dan akhir |
| Bangun proyek di sekitar individu yang termotivasi | Beri mereka lingkungan dan kepercayaan yang mereka butuhkan |
| Percakapan tatap muka | Cara paling efisien untuk menyampaikan informasi |
| Perangkat lunak yang berfungsi adalah ukuran utama kemajuan | Bukan dokumen, bukan rencana |
| Kecepatan berkelanjutan | Tanpa batas waktu; tidak ada pawai kematian |
| Perhatian terus menerus terhadap keunggulan teknis | Desain bagus dan kode bersih |
| Kesederhanaan | Maksimalkan pekerjaan yang belum selesai |
| Tim yang mengatur dirinya sendiri | Arsitektur dan desain terbaik muncul darinya |
| Refleksi dan penyesuaian rutin | Retrospektif; perbaikan berkelanjutan |
### Scrum
Scrum adalah framework Agile yang paling banyak digunakan.
| Elemen | Deskripsi |
|---------|-------------|
| **Lari** | Iterasi dengan panjang tetap (biasanya 2 minggu) |
| **Pemilik Produk** | Mendefinisikan dan memprioritaskan simpanan; mewakili pemangku kepentingan |
| **Master Scrum** | Memfasilitasi proses; menghilangkan hambatan; melindungi tim |
| **Tim Pengembang** | Lintas fungsi, mengatur diri sendiri (ideal 5–9 orang) |
| **Backlog Produk** | Daftar prioritas segala sesuatu yang mungkin diperlukan |
| **Sprint Backlog** | Item yang dipilih untuk sprint saat ini + rencana pengirimannya |
| **Standup Harian** | Sinkronisasi 15 menit: Apa yang saya lakukan? Apa yang akan saya lakukan? Ada pemblokir? |
| **Ulasan Sprint** | Demo perangkat lunak yang berfungsi kepada pemangku kepentingan; mengumpulkan umpan balik |
| **Retrospektif Sprint** | Tim merefleksikan bagaimana meningkatkan proses |
### Kanban
Kanban adalah metode berbasis aliran yang berfokus pada visualisasi pekerjaan dan membatasi pekerjaan yang sedang berlangsung.
| Latihan | Deskripsi |
|----------|-------------|
| **Visualisasikan alur kerja** | Papan dengan kolom (Yang Harus Dilakukan → Sedang Berlangsung → Tinjau → Selesai) |
| **Batasi WIP** | Tetapkan jumlah maksimum item di setiap kolom |
| **Kelola aliran** | Ukur waktu siklus; mengidentifikasi dan menghilangkan hambatan |
| **Buat kebijakan eksplisit** | Semua orang sepakat tentang arti "Selesai" untuk setiap kolom |
| **Meningkatkan secara kolaboratif** | Gunakan data dan umpan balik untuk mengembangkan proses |
**Scrum vs Kanban**:
| | banyak | Kanban |
|---|-------|--------|
| **irama** | Sprint tetap (2 minggu) | Aliran terus menerus |
| **Peran** | PO, Scrum Master, Tim | Tidak ada peran yang ditentukan |
| **Ubah** | Tidak ada perubahan di pertengahan sprint | Ubah kapan saja |
| **Metrik** | Kecepatan (poin cerita per sprint) | Waktu siklus, keluaran |
| **Terbaik untuk** | Pengembangan produk dengan rilis reguler | Tim pendukung; pengiriman berkelanjutan |
---

## OKR dan KPI
### OKR (Tujuan dan Hasil Utama)
OKR adalah kerangka penetapan tujuan yang digunakan oleh Google, Intel, Spotify, dan banyak lainnya.
| Komponen | Deskripsi | Contoh |
|-----------|-------------|---------|
| **Tujuan** | Kualitatif, ambisius, inspiratif | "Menjadi platform masuk untuk akuntansi usaha kecil" |
| **Hasil Utama 1** | Terukur; membuktikan tujuan tercapai | Tingkatkan pengguna aktif bulanan dari 10K menjadi 50K |
| **Hasil Utama 2** | Terukur | Raih skor NPS 60+ |
| **Hasil Utama 3** | Terukur | Kurangi waktu orientasi dari 30 menit menjadi 5 menit |
**Praktik terbaik OKR**:
- Tetapkan 3–5 tujuan per kuartal
- Setiap tujuan memiliki 2–5 hasil utama
- Targetkan pencapaian 70% (100% berarti tujuan terlalu mudah)
- OKR terpisah dari tinjauan kinerja
- Transparan: semua orang dapat melihat OKR orang lain
### KPI (Indikator Kinerja Utama)
| Kategori | Contoh KPI |
|----------|-------------|
| **Keuangan** | Pendapatan, margin kotor, laba bersih, EBITDA |
| **Pelanggan** | NPS, CSAT, tingkat churn, CLV |
| **Produk** | DAU/MAU, adopsi fitur, waktu untuk menilai |
| **Teknik** | Frekuensi penerapan, waktu tunggu, MTTR, tingkat kegagalan perubahan |
| **Pemasaran** | CAC, ROAS, tingkat konversi, lalu lintas organik |
| **Orang** | NPS karyawan, tingkat retensi, waktu untuk merekrut |
---

## Manajemen Pemangku Kepentingan
| Tipe Pemangku Kepentingan | Apa yang Mereka Peduli | Cara Terlibat |
|-----------------|---------------------|---------------|
| **Sponsor eksekutif** | ROI, penyelarasan strategis, risiko | Pembaruan bulanan; fokus pada hasil |
| **Pengguna akhir** | Kemudahan penggunaan, keandalan, pemecahan masalah mereka | Riset pengguna; program beta; saluran dukungan |
| **Tim teknis** | Kualitas kode, arsitektur, utang teknis | Tinjauan arsitektur; pembicaraan teknologi; keterlibatan dalam pengambilan keputusan |
| **Pelanggan eksternal** | Jadwal pengiriman, kualitas, nilai | Demo reguler; komunikasi yang jelas; SLA |
| **Regulator / Kepatuhan** | Persyaratan hukum, jalur audit | Dokumentasi; keterlibatan proaktif |
### Jaringan Kekuasaan/Kepentingan
| | Bunga Rendah | Bunga Tinggi |
|---|-------------|---------------|
| **Kekuatan Tinggi** | Tetap puas | Kelola secara dekat (pemain kunci) |
| **Daya Rendah** | Pantau (usaha minimal) | Tetap terinformasi |
---

## Kerangka Komunikasi
| Kerangka | Struktur | Kapan Menggunakan |
|-----------|-----------|-------------|
| **PERSIAPAN** | Poin → Alasan → Contoh → Poin | Komunikasi persuasif; pertemuan |
| **BINTANG** | Situasi → Tugas → Tindakan → Hasil | Wawancara; ulasan kinerja |
| **BLUF** | Garis Bawah Di Depan | Email ke eksekutif; pembaruan status |
| **SBAR** | Situasi → Latar Belakang → Penilaian → Rekomendasi | penyerahan; komunikasi insiden |
| **7 C** | Jelas, Ringkas, Konkret, Benar, Koheren, Lengkap, Santun | Komunikasi tertulis umum |
### Memberikan Masukan
| Pendekatan | Deskripsi |
|----------|-------------|
| **SBI** (Dampak-Situasi-Perilaku) | "Dalam (situasi) pertemuan kemarin, Anda mengganggu (perilaku) klien, yang membuat mereka menutup (dampak)." |
| **Masukan** | Fokus pada perilaku masa depan, bukan kesalahan masa lalu. "Lain kali, coba..." |
| **Keterusterangan Radikal** (Kim Scott) | Peduli secara pribadi + tantang secara langsung. Tidak terlalu baik (empati yang merusak) dan tidak terlalu kasar (agresi yang menjengkelkan). |
---

## Model Pengambilan Keputusan
| Model | Deskripsi | Terbaik Untuk |
|-------|-------------|----------|
| **CEPAT** | Rekomendasikan, Setuju, Lakukan, Masukan, Putuskan — menjelaskan siapa melakukan apa | Keputusan kompleks dengan banyak pemangku kepentingan |
| **RACI** | Bertanggung Jawab, Akuntabel, Berkonsultasi, Terinformasi — kejelasan peran | Tugas dan hasil proyek |
| **Matriks Eisenhower** | Kisi Mendesak/Penting — memprioritaskan tugas | Produktivitas pribadi; triase tugas |
| **Matriks Keputusan** | Pilihan skor terhadap kriteria tertimbang | Memilih di antara alternatif |
| **Loop OODA** | Amati → Orientasikan → Putuskan → Bertindak — siklus keputusan cepat | Situasi kompetitif; respon insiden |
| **Enam Topi Berpikir** | Lihatlah suatu keputusan dari 6 sudut pandang (fakta, emosi, risiko, manfaat, kreativitas, proses) | Keputusan kelompok; menghindari pemikiran kelompok |
### Matriks Eisenhower
| | Mendesak | Tidak Mendesak |
|---|--------|------------|
| **Penting** | **Lakukan dulu** — krisis, tenggat waktu, masalah kritis | **Jadwal** — perencanaan strategis, membangun hubungan, pembelajaran |
| **Tidak Penting** | **Delegasi** — beberapa email, rapat, interupsi | **Hilangkan** — membuang-buang waktu, sibuk bekerja, browsing berlebihan |
---

## Manajemen Risiko
| Langkah | Deskripsi |
|------|-------------|
| **1. Identifikasi risiko** | Pikirkan apa yang salah (teknis, jadwal, sumber daya, eksternal) |
| **2. Menilai probabilitas dan dampak** | Nilai setiap risiko: Tinggi/Sedang/Rendah untuk keduanya |
| **3. Prioritaskan** | Fokus pada risiko dengan probabilitas tinggi dan berdampak tinggi |
| **4. Rencanakan tanggapan** | Hindari, mitigasi, transfer, atau terima setiap risiko |
| **5. Pantau** | Tinjau secara teratur; risiko berubah seiring berkembangnya proyek |
### Strategi Respon Risiko
| Strategi | Deskripsi | Contoh |
|----------|-------------|---------|
| **Hindari** | Ubah rencana untuk menghilangkan risiko | Gunakan teknologi yang telah terbukti daripada yang eksperimental |
| **Mitigasi** | Mengurangi kemungkinan atau dampak | Tambahkan waktu penyangga; mempekerjakan staf tambahan |
| **Transfer** | Mengalihkan risiko ke pihak ketiga | Asuransi; outsourcing; kontrak harga tetap |
| **Terima** | Akui dan rencanakan jika itu terjadi | Dana darurat; rencana mundur |
---

## Manajemen Tim Jarak Jauh
| Tantangan | Solusi |
|-----------|----------|
| **Kesenjangan komunikasi** | Default untuk ditulis; konteks komunikasi yang berlebihan; gunakan alat async-first |
| **Isolasi** | Reguler 1:1; acara sosial virtual; pertemuan tatap muka sesekali |
| **Zona waktu** | Putar waktu pertemuan; mencatat keputusan; meminimalkan ketergantungan sinkron |
| **Visibilitas** | Saluran publik melalui DM; pembaruan status tertulis; dasbor bersama |
| **Kepercayaan** | Ukur hasil, bukan jam; hindari perangkat lunak pengawasan |
| **Orientasi** | Sistem pertemanan terstruktur; proses yang terdokumentasi; tujuan minggu pertama yang jelas |
### Rapat yang Efektif
| Jenis Rapat | Durasi | Frekuensi | Tujuan |
|-------------|----------|-----------|---------|
| **Standup harian** | 15 menit | Harian | Sinkronisasi; pemblokir permukaan |
| **Perencanaan sprint** | 1–2 jam | Setiap sprint | Selaraskan apa yang harus dibangun selanjutnya |
| **Ulasan sprint** | 1 jam | Setiap sprint | Demo; mengumpulkan umpan balik |
| **Retrospektif** | 45–60 menit | Setiap sprint | Peningkatan proses |
| **1:1** | 30 menit | Mingguan/dua mingguan | Dukungan dan pertumbuhan individu |
| **Semua tangan** | 30–60 menit | Bulanan | Pembaruan perusahaan/tim; Tanya Jawab |
**Peraturan rapat**: Setiap rapat memerlukan agenda. Mulai tepat waktu. Berakhir tepat waktu. Tetapkan item tindakan dengan pemilik. Jika bisa berupa email, jadikanlah itu email.
---

## Struktur Organisasi
| Struktur | Deskripsi | Kelebihan | Kontra |
|-----------|-------------|------|------|
| **Fungsional** | Diselenggarakan berdasarkan spesialisasi (teknik, pemasaran, penjualan) | Keahlian yang mendalam; jalur karir yang jelas | Silo; pekerjaan lintas fungsi yang lambat |
| **Divisi** | Diselenggarakan berdasarkan produk, pasar, atau geografi | Fokus; akuntabilitas | Sumber daya duplikat; praktik yang tidak konsisten |
| **Matriks** | Orang-orang melapor kepada manajer fungsional dan proyek | Fleksibilitas; berbagi sumber daya | Prioritas yang bertentangan; kebingungan tentang siapa yang bertanggung jawab |
| **Datar / Holakrasi** | Hierarki minimal; tim yang terorganisir sendiri | Kecepatan; otonomi; inovasi | Keputusan yang tidak jelas; tidak berskala dengan baik |
| **Topologi tim** (Skelton/Pais) | Tim yang selaras dengan arus + tim platform + tim pendukung + tim subsistem yang rumit | Selaras dengan bagaimana pekerjaan sebenarnya mengalir | Membutuhkan desain yang bijaksana; bukan peluru perak |
---

## Dasar-dasar Manajemen Produk
Manajemen produk adalah disiplin dalam memutuskan apa yang akan dibuat, untuk siapa, dan mengapa — serta memastikan produk tersebut memberikan nilai.
| Tanggung jawab | Deskripsi |
|---------------|-------------|
| **Penemuan** | Riset pengguna, analisis pasar, intelijen kompetitif |
| **Strategi** | Visi produk, peta jalan, kerangka prioritas |
| **Eksekusi** | Tulis spesifikasi/cerita pengguna; bekerja dengan teknik dan desain |
| **Peluncuran** | Perencanaan masuk ke pasar; penentuan posisi; pemberdayaan penjualan |
| **Iterasi** | Analisis metrik; mengumpulkan umpan balik; memprioritaskan perbaikan berikutnya |
### Kerangka Prioritas
| Kerangka | Cara Kerja |
|-----------|-------------|
| **MoSCoW** | Harus punya / Harus punya / Bisa punya / Tidak akan punya |
| **BERAS** | Jangkauan × Dampak × Keyakinan ÷ Upaya |
| **Model Kano** | Klasifikasikan fitur sebagai dasar, kinerja, atau kesenangan |
| **Matriks Nilai vs Upaya** | Plot pada kisi 2x2; memprioritaskan barang yang bernilai tinggi dan mudah dilakukan |
| **Penilaian Peluang** | Kepentingan dikurangi kepuasan; temukan kebutuhan yang kurang terlayani |
---

## Ringkasan
Manajemen adalah praktik mencapai tujuan melalui orang lain. Manajer yang efektif menggabungkan pemikiran jernih (kerangka kerja, metodologi, metrik) dengan keterampilan interpersonal (mendengarkan, empati, percaya). Tidak ada metodologi yang dapat menggantikan penilaian yang baik, namun penilaian yang baik akan diperkuat oleh kerangka kerja yang baik. Hal ini harus diterapkan sebagai panduan praktis dan bukan doktrin yang kaku.