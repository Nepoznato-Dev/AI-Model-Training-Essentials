---
# Metadata
title: "Cloud Architecture"
description: "Cloud providers, architecture patterns, security"
category: "Coding and Technology"
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
reviewed_by: "Coding & Technology Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [cloud, architecture, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "11 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Arsitektur Awan
Komputasi awan telah mengubah secara mendasar cara organisasi membangun, menerapkan, dan menskalakan perangkat lunak. Daripada membeli dan memelihara server fisik, Anda dapat menyediakan sumber daya komputasi sesuai permintaan, membayar sesuai penggunaan, dan melakukan penskalaan secara global dalam hitungan menit. File ini mencakup konsep inti, pola arsitektur, layanan, dan praktik terbaik yang perlu Anda ketahui.
---

## Dasar-dasar Komputasi Awan
### Apa itu Komputasi Awan?
Pengiriman sumber daya komputasi berdasarkan permintaan — server, penyimpanan, database, jaringan, perangkat lunak — melalui internet dengan harga bayar sesuai pemakaian.
### Karakteristik Penting NIST
| Karakteristik | Arti |
|---------------|---------|
| **Layanan Mandiri Sesuai Permintaan** | Penyediaan sumber daya tanpa interaksi manusia |
| **Akses Jaringan Luas** | Tersedia melalui jaringan melalui mekanisme standar |
| **Pengumpulan Sumber Daya** | Model multi-penyewa; sumber daya yang ditetapkan secara dinamis |
| **Elastisitas Cepat** | Skalakan ke luar dan ke dalam dengan cepat |
| **Layanan Terukur** | Penggunaan dipantau dan ditagih |
### Model Penerapan
| Model | Deskripsi | Kapan Menggunakan |
|-------|-------------|-------------|
| **Awan Publik** | Dimiliki oleh penyedia; infrastruktur bersama (AWS, Azure, GCP) | Sebagian besar beban kerja; hemat biaya |
| **Awan Pribadi** | Didedikasikan untuk satu organisasi | Persyaratan peraturan, data sensitif |
| **Awan Hibrid** | Kombinasi publik dan swasta | Fleksibilitas + kepatuhan |
| **Multi-Cloud** | Menggunakan beberapa penyedia cloud publik | Hindari penguncian vendor, yang terbaik dari jenisnya |
### Model Layanan
| Model | Menyediakan | Contoh | Kasus Penggunaan |
|-------|----------|----------|-----------|
| **IaaS** | VM, penyimpanan, jaringan, OS | AWS EC2, VM Azure, Mesin Komputasi GCP | Migrasi angkat dan geser, kontrol penuh |
| **PaaS** | Platform pengembangan, database, middleware | Heroku, Mesin Aplikasi Google, AWS Elastic Beanstalk | Pengembangan aplikasi, penerapan API |
| **SaaS** | Aplikasi lengkap melalui internet | Tenaga Penjualan, Google Workspace, Microsoft 365 | Email, CRM, kolaborasi |
| **FaaS/Tanpa Server** | Eksekusi fungsi berbasis peristiwa | AWS Lambda, Fungsi Azure, Fungsi Cloud GCP | API, pemrosesan acara, tugas terjadwal |
---

## Penyedia Cloud Utama
| Penyedia | Pangsa Pasar | Kekuatan |
|----------|-------------|-----------|
| **AWS** | ~32% | Katalog layanan terluas, ekosistem terbesar |
| **Azure** | ~23% | Integrasi perusahaan, cloud hybrid, tumpukan Microsoft |
| **GCP** | ~10% | Analisis data, AI/ML, Kubernetes |
| **Awan Alibaba** | ~4% | Dominan di Asia-Pasifik |
| **Awan Oracle** | ~2% | Beban kerja basis data, aplikasi perusahaan |
| **IBM Cloud** | ~2% | Fokus perusahaan, Watson AI |
| **Samudra Digital** | ceruk | Penawaran yang ramah pengembang dan disederhanakan |
### Perbandingan Layanan (3 Penyedia Teratas)
| Kategori | AWS | Azure | GCP |
|----------|-----|-------|-----|
| **Hitung** | EC2, Lambda, ECS | VM, Fungsi, AKS | Mesin Komputasi, Fungsi Cloud, GKE |
| **Penyimpanan** | S3, EBS, Gletser | Penyimpanan Blob, Penyimpanan Disk | Penyimpanan Cloud, Disk Persisten |
| **Basis Data** | RDS, DynamoDB, Aurora | Basis Data SQL, Cosmos DB | Cloud SQL, Firestore, Meja Besar |
| **Analitik** | Pergeseran Merah, ESDM | Sinapsis, Databricks | BigQuery, Aliran Data |
| **AI/ML** | SageMaker, Pengakuan | Azure ML, Layanan Kognitif | Vertex AI, AutoML |
| **Jaringan** | VPC, Rute 53, CloudFront | VNet, Manajer Lalu Lintas | VPC, Cloud DNS, Cloud CDN |
---

## Pola Arsitektur
### Kerangka Kerja yang Terarsitektur dengan Baik
Ketiga penyedia utama tersebut menerbitkan kerangka kerja yang dirancang dengan baik dan dibangun berdasarkan lima pilar:
| Pilar | Prinsip Utama |
|--------|---------------|
| **Keunggulan Operasional** | Mengotomatiskan operasi; sering melakukan perubahan yang dapat dibalik; mengantisipasi kegagalan |
| **Keamanan** | Landasan identitas yang kuat; menerapkan keamanan di setiap lapisan; melindungi data saat transit dan saat istirahat |
| **Keandalan** | Uji prosedur pemulihan; pemulihan otomatis dari kegagalan; skala secara horizontal |
| **Efisiensi Kinerja** | Gunakan tanpa server; mendunia dalam hitungan menit; sering bereksperimen |
| **Optimasi Biaya** | Mengadopsi model konsumsi; menggunakan layanan terkelola; berhenti mengeluarkan uang untuk pekerjaan yang tidak terdiferensiasi |
### Pola Umum
| Pola | Deskripsi | Manfaat | Tantangan |
|---------|-------------|----------|------------|
| **Layanan Mikro** | Dekomposisi aplikasi menjadi layanan kecil dan independen | Skalabilitas, isolasi kesalahan, penerapan independen | Kompleksitas terdistribusi, konsistensi data |
| **Berbasis Peristiwa** | Komponen berkomunikasi melalui peristiwa | Kopling longgar, pemrosesan real-time | Kompleksitas debug, konsistensi akhirnya |
| **Tanpa Server** | Tidak ada manajemen server; bayar per eksekusi | Efisiensi biaya, penerapan cepat | Cold start, penguncian vendor, batas eksekusi |
| **Berlapis (Tingkat N)** | Presentasi → Logika bisnis → Akses data → Database | Pemisahan kekhawatiran, pemeliharaan | Bisa menjadi monolitik |
| **Berbasis Luar Angkasa** | Data terdistribusi ke seluruh node memori tervirtualisasi | Menangani konkurensi tinggi, latensi rendah | Kompleks untuk dirancang dan dikelola |
---

## Layanan Inti
### Hitung
| Jenis Layanan | Detail |
|-------------|---------|
| **Mesin Virtual** | Tujuan umum, komputasi optimal, memori optimal, GPU. Harga: sesuai permintaan, dipesan, spot. |
| **Wadah** | Waktu proses buruh pelabuhan; orkestrasi melalui Kubernetes (EKS, AKS, GKE). Registri: ECR, GCR, ACR. |
| **Fungsi Tanpa Server** | Dipicu oleh peristiwa, tanpa kewarganegaraan. Batasan waktu eksekusi, memori, konkurensi. |
### Penyimpanan
| Ketik | Karakteristik | Contoh | Terbaik Untuk |
|------|----------------|----------|----------|
| **Objek** | Struktur datar, akses HTTP, kaya metadata | S3, Penyimpanan Cloud, Azure Blob | Aset statis, cadangan, data lake |
| **Blokir** | Volume mentah yang dilampirkan ke VM | EBS, Disk Persisten, Disk Azure | Basis data, volume boot |
| **Berkas** | Sistem file bersama (NFS/SMB) | EFS, Penyimpanan File, File Azure | Manajemen konten, konfigurasi bersama |
| **Arsip** | Biaya terendah, penundaan pengambilan | Gletser S3, Arsip Azure | Kepatuhan, pencadangan jangka panjang |
### Basis Data
| Kategori | Layanan | Kasus Penggunaan |
|----------|----------|----------|
| **Relasional Terkelola** | RDS, Cloud SQL, Azure SQL | Aplikasi tradisional, transaksi ACID |
| **NoSQL — Dokumen** | DocumentDB, Firestore, Cosmos DB | Skema fleksibel, data JSON |
| **NoSQL — Nilai Kunci** | DynamoDB, Tembolok Redis | Caching, sesi, pencarian sederhana |
| **NoSQL — Kolom Lebar** | Meja Besar, Cassandra | Seri waktu yang berat dan ditulis |
| **NoSQL — Grafik** | Neptunus, Cosmos DB (Grafik API) | Hubungan, jejaring sosial |
| **Pergudangan Data** | Kepingan Salju, Redshift, BigQuery, Sinaps | Analisis, BI |
| **Caching** | ElastiCache, Penyimpanan Memori Cloud | Penyimpanan sesi, cache kueri |
---

## Jaringan
### Jaringan Virtual
Setiap penerapan cloud berada di dalam Virtual Private Cloud (VPC / VNet) — jaringan terisolasi yang Anda tentukan dengan blok CIDR, subnet (publik atau privat), tabel rute, dan gateway.
### Penyeimbangan Beban dan CDN
| Layanan | Tujuan |
|---------|---------|
| **Penyeimbang Beban** | Mendistribusikan lalu lintas ke seluruh instance (jaringan L4, aplikasi L7) |
| **CDN** | Cache konten di lokasi edge untuk latensi lebih rendah (CloudFront, Cloud CDN, Azure CDN) |
| **DNS** | Pendaftaran domain, kebijakan perutean, pemeriksaan kesehatan (Rute 53, Cloud DNS, Azure DNS) |
### Opsi Konektivitas
| Pilihan | Deskripsi |
|--------|-------------|
| **Gerbang Internet** | Akses internet publik untuk VPC |
| **Gerbang NAT** | Akses keluar subnet pribadi |
| **VPN** | Terowongan terenkripsi ke lokal |
| **Sambungan Langsung/ExpressRoute** | Koneksi pribadi khusus |
| **Peering VPC** | Hubungkan VPC di dalam atau antar akun |
---

## Keamanan
### Model Tanggung Jawab Bersama
| Lapisan | Penyedia | Pelanggan |
|-------|----------|----------|
| **Infrastruktur** (perangkat keras, fasilitas) | ✅ | |
| **Komputasi, Penyimpanan, Jaringan** | ✅ (dikelola) | ✅ (kelola sendiri) |
| **Data, Aplikasi, Identitas** | | ✅ |
Semakin banyak layanan yang dikelola, semakin banyak penyedia yang menanganinya. Dengan IaaS Anda mengelola hampir segalanya; dengan SaaS, penyedia menangani hampir semuanya.
### Manajemen Identitas dan Akses (IAM)
| Konsep | Deskripsi |
|---------|-------------|
| **Pengguna** | Identitas individu |
| **Grup** | Koleksi pengguna |
| **Peran** | Kredensial sementara untuk layanan atau pengguna |
| **Kebijakan** | Dokumen yang menjelaskan izin |
| **Prinsip** | Hak istimewa paling kecil, pemisahan tugas |
### Perlindungan Data
- **Enkripsi saat istirahat**: KMS, kunci yang dikelola pelanggan, HSM.
- **Enkripsi saat transit**: TLS/SSL, HTTPS.
- **Manajemen rahasia**: Manajer Rahasia, Key Vault — tidak pernah rahasia hardcode.
---

## DevOps di Cloud
### Infrastruktur sebagai Kode (IaC)
| Alat | Deskripsi |
|------|-------------|
| **Terraform** | Multi-cloud, HCL deklaratif, manajemen negara |
| **CloudFormation** | Templat YAML/JSON asli AWS |
| **Templat ARM / Bisep** | Azure-asli |
| **Pulumi** | Infrastruktur menggunakan bahasa pemrograman (Python, Go, dll) |
### Layanan CI/CD
| Penyedia | Alat |
|----------|-------|
| **AWS** | CodePipeline, CodeBuild, CodeDeploy |
| **Azure** | Azure DevOps, Tindakan GitHub |
| **GCP** | Pembuatan Cloud, Penerapan Cloud |
| **Pihak ketiga** | Jenkins, CircleCI, GitLab CI |
### Pemantauan dan Observabilitas
| Kemampuan | AWS | Azure | GCP |
|-----------|-----|-------|-----|
| **Metrik** | CloudWatch | Monitor Azure | Pemantauan Awan |
| **Pencatatan** | Log CloudWatch | Analisis Log | Pencatatan Awan |
| **Pelacakan** | Sinar-X | Wawasan Aplikasi | Jejak Awan |
---

## Manajemen Biaya
### Model Penetapan Harga
| Model | Deskripsi | Terbaik Untuk |
|-------|-------------|----------|
| **Sesuai Permintaan** | Bayar untuk apa yang Anda gunakan, per detik/jam | Variabel, beban kerja jangka pendek |
| **Instans Cadangan** | Komitmen 1–3 tahun, diskon signifikan | Beban kerja kondisi stabil |
| **Instans Spot** | Tawaran untuk kapasitas yang tidak terpakai; dapat diganggu | Pekerjaan yang toleran terhadap kesalahan dan fleksibel |
| **Paket Hemat** | Penetapan harga komitmen yang fleksibel | Pola penggunaan campuran |
| **Tingkat Gratis** | Penggunaan gratis terbatas untuk akun baru | Belajar, membuat prototipe |
### Strategi Pengoptimalan
Instans berukuran tepat agar sesuai dengan beban kerja. Gunakan penskalaan otomatis untuk menangani lonjakan permintaan. Kapasitas cadangan untuk beban yang dapat diprediksi. Gunakan instans spot untuk pekerjaan batch. Pindahkan data yang jarang diakses ke tingkat penyimpanan yang lebih murah. Hapus sumber daya yang tidak digunakan (snapshot yatim piatu, penyeimbang beban yang menganggur, IP yang tidak terikat).
---

## Ketersediaan Tinggi dan Pemulihan Bencana
### Konsep Ketersediaan
| Konsep | Deskripsi |
|---------|-------------|
| **Zona Ketersediaan (AZ)** | Pusat data yang terpisah secara fisik dalam suatu wilayah |
| **Wilayah** | Wilayah geografis dengan banyak AZ |
| **Lokasi Tepi** | Lokasi cache CDN untuk pengiriman konten |
### Strategi Pemulihan Bencana
| Strategi | Biaya | RTO | RPO | Deskripsi |
|----------|------|-----|-----|-------------|
| **Cadangkan dan Pulihkan** | Terendah | Jam | Jam–hari | Backup berkala, pulihkan bila diperlukan |
| **Lampu Percontohan** | Rendah | Menit–jam | Menit | Elemen inti selalu berjalan, tingkatkan skala bencana |
| **Siaga Hangat** | Sedang | Menit | Detik–menit | Versi yang diperkecil selalu berjalan |
| **Multi-Situs Aktif/Aktif** | Tertinggi | Mendekati nol | Nol | Produksi penuh di berbagai wilayah |
**RTO** (Tujuan Waktu Pemulihan) = waktu henti maksimum yang dapat diterima. **RPO** (Recovery Point Objective) = kehilangan data maksimum yang dapat diterima.
---

## Tren yang Muncul
| Tren | Apa yang Terjadi |
|-------|-----------------|
| **Komputasi Tepi** | Memproses data lebih dekat ke sumbernya (AWS Outposts, Wavelength, Azure Edge) |
| **Multi-Cloud** | Menghindari penguncian vendor; memanfaatkan yang terbaik di seluruh penyedia |
| **Layanan AI/ML** | Model terlatih (penglihatan, ucapan, bahasa) + pelatihan khusus (SageMaker, Vertex AI) |
| **Komputasi Kuantum** | Layanan eksperimental tahap awal (AWS Braket, Azure Quantum) |
| **Awan Berkelanjutan** | Pelacakan jejak karbon, komitmen energi terbarukan, arsitektur hijau |