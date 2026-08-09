---
# Metadata
title: "Data Ethics and Privacy"
description: "GDPR, data consent, algorithmic bias, dark patterns, anonymisation"
category: "Data Science and Analytics"
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
reviewed_by: "Data Science & Analytics Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [data, ethics, privacy, data-science-and-analytics]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "6 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Etika Data dan Privasi
Etika data adalah studi tentang bagaimana pengumpulan, analisis, dan penyebaran data memengaruhi hak, otonomi, dan kesejahteraan masyarakat. Privasi adalah perhatian khusus mengenai siapa yang mengontrol informasi pribadi dan bagaimana informasi tersebut dibagikan. Topik-topik ini telah beralih dari perdebatan akademis ke berita halaman depan — penegakan GDPR, pelanggaran data yang berdampak pada miliaran pengguna, dan meningkatnya kesadaran masyarakat bahwa praktik data perusahaan teknologi mempunyai konsekuensi nyata terhadap demokrasi, kesetaraan, dan kebebasan individu.
---

## Mengapa Etika Data Penting
| Kekhawatiran | Deskripsi | Dampak Dunia Nyata |
|---------|-------------|-------------------|
| **Pengawasan kapitalisme** | Perusahaan memonetisasi data pribadi dalam skala besar | Hilangnya privasi; manipulasi perilaku |
| **Bias algoritma** | Model yang dilatih berdasarkan data yang bias mereproduksi bias | Diskriminasi dalam perekrutan, peminjaman, kepolisian |
| **Persetujuan berdasarkan informasi** | Pengguna tidak memahami apa yang mereka setujui | Data yang dikumpulkan untuk satu tujuan digunakan untuk tujuan lain |
| **Pelanggaran data** | Data sensitif terekspos melalui keamanan yang buruk | Pencurian identitas; penipuan keuangan; kerusakan reputasi |
| **Filter gelembung** | Umpan yang dipersonalisasi memperkuat keyakinan yang ada | Polarisasi politik; informasi yang salah |
| **Pola gelap** | UI dirancang untuk mengelabui pengguna agar berbagi data | Langganan yang tidak diinginkan; berbagi data yang tidak disengaja |
---

## Kerangka dan Peraturan Privasi
### Hukum Privasi Utama
| Peraturan | Wilayah | Persyaratan Utama |
|-----------|--------|-----------------|
| **GDPR** (Peraturan Perlindungan Data Umum) | UE / EEA | Dasar hukum pemrosesan; hak untuk mengakses; hak untuk dilupakan; portabilitas data; pemberitahuan pelanggaran 72 jam; denda hingga 4% dari pendapatan global |
| **CCPA / CPRA** (Undang-Undang Hak Privasi California) | Kalifornia, AS | Hak untuk mengetahui; hak untuk menghapus; hak untuk tidak ikut serta dalam penjualan; keikutsertaan terbatas untuk anak-anak |
| **LGPD** (Lei Geral de Proteção de Dados) | Brasil | Mirip dengan GDPR; dasar hukum; hak subjek data; Diperlukan DPO |
| **PIPL** (Undang-undang Perlindungan Informasi Pribadi) | Cina | Diperlukan persetujuan; lokalisasi data; pembatasan transfer lintas batas |
| **POPIA** (Undang-Undang Perlindungan Informasi Pribadi) | Afrika Selatan | Syarat-syarat pemrosesan yang sah; hak subjek data; pengatur |
| **UU DPDP** (UU Perlindungan Data Pribadi Digital) | India | Izin; batasan tujuan; hak pokok data; kewajiban fidusia data |
### Prinsip Inti GDPR
| Prinsip | Persyaratan |
|-----------|-------------|
| **Keabsahan, keadilan, transparansi** | Memproses data secara legal; jangan menyesatkan pengguna; terbuka tentang apa yang Anda kumpulkan |
| **Batasan tujuan** | Kumpulkan data hanya untuk tujuan tertentu dan eksplisit |
| **Minimalisasi data** | Kumpulkan hanya yang benar-benar Anda perlukan |
| **Akurasi** | Jaga keakuratan data; memperbaiki atau menghapus data yang tidak akurat |
| **Batasan penyimpanan** | Jangan menyimpan data lebih lama dari yang diperlukan |
| **Integritas dan kerahasiaan** | Amankan data dari akses dan kehilangan yang tidak sah |
| **Akuntabilitas** | Tunjukkan kepatuhan terhadap semua hal di atas |
---

## Teknik Menjaga Privasi
| Teknik | Cara Kerja | Pengorbanan |
|-----------|-------------|-----------|
| **Anonimisasi** | Hapus informasi pengenal pribadi (PII) | Sulit untuk dianonimkan sepenuhnya; risiko identifikasi ulang |
| **Pseudonimisasi** | Ganti pengidentifikasi dengan nama samaran | Reversibel; masih data pribadi berdasarkan GDPR |
| **Privasi diferensial** | Tambahkan kebisingan yang dikalibrasi ke hasil kueri | Mengurangi akurasi; memberikan jaminan privasi matematis |
| **Pembelajaran gabungan** | Latih model di perangkat; hanya berbagi pembaruan model | Pelatihan lebih lambat; overhead komunikasi |
| **Perhitungan multi-pihak yang aman** | Banyak pihak menghitung suatu fungsi tanpa mengungkapkan masukan | Mahal secara komputasi; rumit untuk diimplementasikan |
| **Enkripsi homomorfik** | Lakukan perhitungan pada data terenkripsi | Sangat lambat; dukungan operasi terbatas |
| **Penyembunyian data** | Sembunyikan bagian data (misalnya,`***-**-1234`) | Perlindungan sederhana namun terbatas |
---

## Pengumpulan Data Etis
### Prinsip Pengumpulan yang Etis
| Prinsip | Deskripsi |
|-----------|-------------|
| **Persetujuan berdasarkan informasi** | Pengguna memahami apa yang mereka setujui; tidak dikuburkan dalam bahasa legal |
| **Transparansi tujuan** | Nyatakan dengan jelas mengapa data dikumpulkan dan bagaimana data tersebut akan digunakan |
| **Koleksi minimal** | Hanya kumpulkan apa yang dibutuhkan untuk tujuan yang dinyatakan |
| **Kontrol pengguna** | Izinkan pengguna mengakses, memperbaiki, mengunduh, dan menghapus data mereka |
| **Retensi terbatas** | Hapus data bila tidak diperlukan lagi |
| **Penilaian dampak** | Evaluasi potensi bahaya sebelum mengumpulkan data sensitif |
### Pola Gelap Umum
| Pola | Deskripsi | Contoh |
|---------|-------------|---------|
| **Penghinaan privasi** | Menipu pengguna agar berbagi lebih dari yang mereka inginkan | "Bagikan dengan teman" sudah diperiksa sebelumnya saat mendaftar |
| **Motel kecoak** | Mudah untuk mendaftar; sulit untuk dibatalkan | Penghapusan akun memerlukan panggilan telepon atau fax |
| **Kontinuitas yang dipaksakan** | Uji coba gratis diubah menjadi berbayar tanpa pemberitahuan yang jelas | Biaya berlangganan muncul di kartu kredit |
| **Konfirmasi mempermalukan** | Bersalah pengguna agar ikut serta | "Tidak, terima kasih, saya tidak ingin menghemat uang" |
| **Pengaturan tersembunyi** | Kontrol privasi terkubur jauh di dalam menu | Penyisihan tersembunyi di bawah 5 tingkat pengaturan |
---

## Bias dan Keadilan dalam Data
| Sumber Bias | Deskripsi | Contoh |
|----------------|-------------|---------|
| **Bias seleksi** | Data tidak mewakili populasi sasaran | Melatih model perekrutan berdasarkan data hanya dari satu demografi |
| **Bias sejarah** | Diskriminasi di masa lalu dikodekan dalam data | Catatan penangkapan mencerminkan praktik kepolisian yang bias |
| **Bias pengukuran** | Variabel yang digunakan sebagai proxy memiliki kelemahan | Menggunakan kode pos sebagai proksi kelayakan kredit |
| **Bias agregasi** | Memperlakukan kelompok yang beragam sebagai homogen | Satu model untuk semua etnis; mengabaikan pola spesifik kelompok |
| **Bias bertahan hidup** | Hanya melihat kasus yang berhasil | Mempelajari startup yang sukses sambil mengabaikan yang gagal |
### Strategi Mitigasi
| Strategi | Deskripsi |
|----------|-------------|
| **Pengumpulan data yang beragam** | Pastikan data pelatihan mewakili semua kelompok yang terkena dampak |
| **Audit bias** | Uji model secara berkala untuk mengetahui dampak yang berbeda antar kelompok |
| **Metrik keadilan** | Ukur paritas demografis, kesempatan yang sama, peluang yang setara |
| **Ulasan manusia** | Mintalah manusia meninjau kembali keputusan berisiko tinggi |
| **Laporan Transparansi** | Publikasikan data tentang kinerja model di seluruh demografi |
| **Keterlibatan komunitas** | Melibatkan masyarakat yang terkena dampak dalam desain dan evaluasi |
---

## Tata Kelola Data
### Peran dalam Tata Kelola Data
| Peran | Tanggung jawab |
|------|---------------|
| **Pemilik data** | Pemimpin senior yang bertanggung jawab atas domain data |
| **Petugas data** | Manajemen sehari-hari; kualitas; klasifikasi |
| **Petugas perlindungan data (DPO)** | kepatuhan terhadap GDPR; penilaian dampak privasi; hubungan dengan regulator |
| **Insinyur data** | Saluran pipa; penyimpanan; transformasi |
| **Ilmuwan data** | Analisa; pemodelan; pelaporan |
| **Analis privasi data** | Pantau kepatuhan; menangani permintaan subjek data |
### Klasifikasi Data
| Klasifikasi | Deskripsi | Penanganan |
|---------------|-------------|----------|
| **Publik** | Dapat dibagikan secara bebas | Tidak ada batasan |
| **Internal** | Hanya untuk karyawan | Kontrol akses; tidak ada berbagi eksternal |
| **Rahasia** | Data bisnis sensitif | Enkripsi; kontrol akses yang ketat; pencatatan audit |
| **Dibatasi** | Sangat sensitif; diatur (PII, kesehatan, keuangan) | Enkripsi saat diam dan dalam perjalanan; DLP; akses minimal |
---

## Ringkasan
Etika dan privasi data bukan lagi pertimbangan opsional — melainkan persyaratan hukum, keharusan bisnis, dan kewajiban moral. GDPR dan peraturan serupa menetapkan aturan yang jelas: mengumpulkan secara minimal, menggunakan secara transparan, melindungi dengan ketat, dan memberikan kendali kepada pengguna. Teknik menjaga privasi seperti privasi diferensial, pembelajaran gabungan, dan enkripsi memungkinkan untuk memperoleh nilai dari data tanpa mengekspos individu. Namun teknologi saja tidak cukup. Organisasi memerlukan struktur tata kelola data, praktik audit bias, dan budaya yang memperlakukan data pribadi sebagai sesuatu yang harus dikelola, bukan sekadar dieksploitasi. Perusahaan yang mendapatkan hak ini akan mendapatkan kepercayaan; perusahaan yang tidak melakukan hal tersebut akan menghadapi denda peraturan, reaksi publik, dan perlahan-lahan terkikisnya keinginan penggunanya untuk berbagi data.