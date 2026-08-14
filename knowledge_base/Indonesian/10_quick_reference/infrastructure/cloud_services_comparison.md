---
# Metadata
title: "Cloud Services Comparison"
description: "AWS vs Azure vs GCP side-by-side comparison"
category: "Quick Reference"
subcategory: "Infrastructure"
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
    changes: "Moved to infrastructure/ subfolder; added subcategory field"
  - version: "1.0.0"
    date: "2026-08-05"
    author: "AI Model Training Team"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-09"
review_date: "2027-02-05"
reviewed_by: "Quick Reference Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [cloud, services, comparison, quick-reference]
difficulty_level: "beginner"
prerequisites: []
estimated_reading_time: "7 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# Perbandingan Layanan Cloud
Perbandingan berdampingan dari tiga penyedia cloud utama — AWS, Azure, dan Google Cloud — dalam bidang komputasi, penyimpanan, database, AI/ML, jaringan, pemantauan, dan infrastruktur sebagai kode. Berguna bagi arsitek yang memutuskan platform mana yang akan digunakan, atau memetakan layanan dari satu cloud ke cloud lainnya.
---

## Ikhtisar Penyedia
| | AWS | Azure | Google Cloud (GCP) |
|---|-----|-------|------|
| **Pangsa pasar** | ~31% (terbesar) | ~25% (detik) | ~11% (ketiga, pertumbuhan tercepat) |
| **Kekuatan** | Luasnya layanan; kematangan; ekosistem | Integrasi perusahaan; awan hibrida; tumpukan Microsoft | Data/AI; Kubernet; jaringan global |
| **Terbaik untuk** | Startup hingga perusahaan; katalog layanan terluas | Perusahaan dengan Microsoft/Active Directory; hibrida | Beban kerja intensif data; Kubernetes-asli; AI/ML |
| **Wilayah** | 33 wilayah, 105 AZ | 60+ wilayah | 40+ wilayah, 100+ zona |
| **Tingkat gratis** | Tingkat gratis 12 bulan + selalu gratis | Gratis 12 bulan + kredit $200 | Kredit $300 selama 90 hari + selalu gratis |
---

## Hitung
| Kategori Layanan | AWS | Azure | GCP |
|-----------------|-----|-------|-----|
| **Mesin Virtual** | EC2 (Awan Komputasi Elastis) | Mesin Virtual | Mesin Komputasi |
| **Penskalaan otomatis** | Grup Penskalaan Otomatis | Kumpulan Skala Mesin Virtual | Grup Instance |
| **Fungsi Tanpa Server** | Lambda | Fungsi Azure | Fungsi Cloud |
| **Registrasi Kontainer** | ECR (Registrasi Kontainer Elastis) | Registri Kontainer Azure | Registri Artefak |
| **Orkestrasi Kontainer** | ECS / EKS | ACS/AKS | GKE / Cloud Jalankan |
| **Kontainer Tanpa Server** | Fargate | Aplikasi Kontainer | Lari Awan |
| **Platform Aplikasi (PaaS)** | Pohon Kacang Elastis, Pelari Aplikasi | Layanan Aplikasi | Mesin Aplikasi |
| **Pemrosesan Batch** | Kumpulan AWS | Kumpulan Azure | Kumpulan Awan |
| **Komputasi GPU / AI** | EC2 (Instans P4d, P5) | VM seri NC/ND | VM A2/A3; TPU |
### Model Penetapan Harga VM
| Model | AWS | Azure | GCP |
|-------|-----|-------|-----|
| **Sesuai permintaan** | Instans Sesuai Permintaan | Bayar sesuai pemakaian | Sesuai permintaan |
| **Dicadangkan / Berkomitmen** | Instans Cadangan (1–3 tahun) | VM yang dicadangkan (1–3 tahun) | Diskon abonemen (1–3 tahun) |
| **Titik / Dapat Diputus** | Instans Spot | Spot VM | VM yang Dapat Diakhiri / Spot |
| **Paket hemat** | Paket Hemat | Paket hemat | Diskon penggunaan berkomitmen |
---

## Penyimpanan
| Kategori Layanan | AWS | Azure | GCP |
|-----------------|-----|-------|-----|
| **Penyimpanan Objek** | S3 | Penyimpanan Gumpalan | Penyimpanan Awan |
| **Blokir Penyimpanan** | EBS | Disk Terkelola | Disk Persisten |
| **Penyimpanan File** | EFS, FSx | File Azure | Penyimpanan file |
| **Arsip / Dingin** | Gletser S3, Arsip Dalam | Tingkatan Blob Cool/Arsip | Coldline/Arsip Penyimpanan Cloud |
| **Transfer Data** | Bola Salju, Sinkronisasi Data | Kotak Data | Alat Pemindahan |
### Perbandingan Kelas Penyimpanan
| Kasus Penggunaan | AWS S3 | Gumpalan Azure | Penyimpanan Cloud GCP |
|----------|--------|------------|-------------------|
| **Akses yang sering** | Standar S3 | Panas | Standar |
| **Akses jarang** | Standar S3-IA | Keren | Garis Dekat |
| **Akses langka** | S3 Satu Zona-IA | — | Garis Dingin |
| **Arsip** | Gletser S3 / Arsip Dalam | Arsip | Arsip |
---

## Basis Data
| Kategori Layanan | AWS | Azure | GCP |
|-----------------|-----|-------|-----|
| **Relasional (terkelola)** | RDS (MySQL, PostgreSQL, Oracle, SQL Server) | Basis Data Azure (MySQL, PostgreSQL); Azure SQL | Cloud SQL (MySQL, PostgreSQL) |
| **Relasional (cloud-native)** | Aurora (kompatibel dengan MySQL/PostgreSQL) | Azure SQL Database (kumpulan elastis) | Cloud Spanner (didistribusikan secara global) |
| **NoSQL (dokumen)** | DynamoDB | Kosmos DB (API MongoDB, API SQL) | pemadam kebakaran; Penyimpanan data |
| **NoSQL (kolom lebar)** | DynamoDB (juga) | Cosmos DB (API Cassandra) | Meja Besar |
| **NoSQL (nilai kunci)** | DynamoDB, ElastiCache | Azure Cache untuk Redis | Penyimpanan Memori (Redis) |
| **Grafik** | Neptunus | Cosmos DB (API Gremlin) | — |
| **Rangkaian waktu** | Aliran waktu | Penjelajah Data Azure | — |
| **Buku Besar** | QLDB | Buku Besar Rahasia Azure | — |
| **Cache dalam memori** | ElastiCache (Redis, Memcached) | Azure Cache untuk Redis | Penyimpanan Memori |
| **Penelusuran** | Layanan Pencarian Terbuka | Pencarian Azure AI | Pencarian Awan; Pencarian Vertex AI |
| **Gudang data** | Pergeseran merah | Analisis Sinaps | Kueri Besar |
---

## AI dan Pembelajaran Mesin
| Kategori Layanan | AWS | Azure | GCP |
|-----------------|-----|-------|-----|
| **Platform ML** | Pembuat Sage | Pembelajaran Mesin Azure | Verteks AI |
| **API terlatih** | Pengakuan (visi), Polly (TTS), Pemahaman (NLP), Transkrip | Layanan Kognitif (Visi, Pidato, Bahasa, Keputusan) | Vision AI, Pidato-ke-Teks, API Bahasa Alami |
| **LLM / AI Generatif** | Batuan Dasar (Claude, Llama, Titan) | Layanan Azure OpenAI (GPT-4, DALL-E) | Verteks AI (Gemini); Model Taman |
| **Vektor / Sematan** | OpenSearch (k-NN), Basis Pengetahuan Batuan Dasar | Pencarian Azure AI (vektor) | Pencarian Vektor Vertex AI, AlloyDB |
| **MLOps** | Saluran Pipa SageMaker, Registri Model | Alur Azure ML, Registri Model | Saluran Pipa Vertex AI, Registri Model |
| **Pelabelan data** | Kebenaran Dasar SageMaker | Pelabelan Data Azure ML | Pelabelan Data Vertex AI |
| **AI Percakapan** | Lex | Layanan Bot Azure | Dialogflow CX/ES |
| **Terjemahan** | Terjemahkan | Penerjemah | API Terjemahan |
---

## Jaringan
| Kategori Layanan | AWS | Azure | GCP |
|-----------------|-----|-------|-----|
| **Jaringan Virtual** | VPC | Jaringan Virtual (VNet) | VPC |
| **Penyeimbangan Beban** | ELB/ALB/NLB/CLB | Load Balancer (Aplikasi, Jaringan, Gateway) | Penyeimbangan Beban Cloud |
| **DNS** | Rute 53 | Azure DNS | DNS Awan |
| **CDN** | CloudFront | Pintu Depan Azure | CDN Awan |
| **Gerbang API** | Gerbang API | Manajemen API | Gerbang API |
| **VPN** | VPN Situs-ke-Situs, VPN Klien | Gerbang VPN | VPN Awan |
| **Sambungan Langsung/ExpressRoute** | Sambungan Langsung | Rute Ekspres | Interkoneksi Awan |
| **Tautan Pribadi** | PrivateLink, Titik Akhir VPC | Tautan Pribadi, Titik Akhir Pribadi | Koneksi Layanan Pribadi |
| **Firewall** | WAF, Firewall Jaringan | Azure Firewall, WAF | Pelindung Awan, Firewall |
| **Perlindungan DDoS** | Perisai Standar / Lanjutan | Perlindungan DDoS | Pelindung Awan |
---

## Pemantauan dan Pencatatan
| Kategori Layanan | AWS | Azure | GCP |
|-----------------|-----|-------|-----|
| **Metrik / Pemantauan** | CloudWatch | Monitor Azure | Pemantauan Cloud (Stackdriver) |
| **Pencatatan** | Log CloudWatch | Analisis Log (Log Azure Monitor) | Pencatatan Awan |
| **Pelacakan** | Sinar-X | Wawasan Aplikasi | Jejak Awan |
| **Peringatan** | Alarm CloudWatch | Peringatan Azure Monitor | Peringatan Pemantauan Cloud |
| **Dasbor** | Dasbor CloudWatch | Buku Kerja / Dasbor Azure | Dasbor Pemantauan Cloud |
| **Pelacakan kesalahan** | Sintetis CloudWatch | Wawasan Aplikasi | Pelaporan Kesalahan Cloud |
| **Pihak ketiga** | Datadog, Relik Baru, PagerDuty | Datadog, Relik Baru, PagerDuty | Datadog, Relik Baru, PagerDuty |
---

## Infrastruktur sebagai Kode dan DevOps
| Kategori Layanan | AWS | Azure | GCP |
|-----------------|-----|-------|-----|
| **IaC (asli)** | Formasi Awan | Templat ARM / Bisep | Manajer Penerapan / Pulumi |
| **IaC (lintas cloud)** | Terraform, Pulumi, CDK | Terraform, Pulumi, Bisep | Terraform, Pulumi |
| **CI/CD** | CodePipeline, CodeBuild | Azure DevOps, Tindakan GitHub | Pembangunan Awan; Penerapan Cloud |
| **Registrasi Kontainer** | ECR | Registri Kontainer Azure | Registri Artefak |
| **GitOps** | Aplikasi Mesh + Fluks/ArgoCD | Fluks/ArgoCD di AKS | Sinkronisasi Konfigurasi (Anthos) |
| **Manajemen Rahasia** | Manajer Rahasia, Penyimpanan Parameter SSM | Gudang Kunci | Manajer Rahasia |
---

## Pertimbangan Harga
| Faktor | AWS | Azure | GCP |
|--------|-----|-------|-----|
| **Perincian penagihan** | Per detik (setelah jam pertama untuk beberapa orang) | Per detik | Per detik |
| **Diskon penggunaan berkelanjutan** | Instans Cadangan/Paket Penghematan | VM yang dicadangkan | Diskon penggunaan berkomitmen |
| **Contoh spot** | Diskon hingga 90% | Diskon hingga 90% | Diskon hingga 91% |
| **Keluarnya data** | Dikenakan biaya (mahal) | Dibebankan | Harga sama terlepas dari tujuannya (seringkali lebih murah) |
| **Tingkat gratis** | 12 bulan + selalu gratis | 12 bulan + kredit $200 | $300 selama 90 hari + selalu gratis |
| **Diskon perusahaan** | Program Diskon Perusahaan (EDP) | MACC (Kontrak Komitmen Moneter) | Penggunaan berkomitmen + CUD |
---

## Kapan Menggunakan Yang Mana
| Skenario | Direkomendasikan | Mengapa |
|----------|-------------|-----|
| **Pilihan layanan terluas; ekosistem dewasa** | AWS | Katalog terbesar; sebagian besar integrasi pihak ketiga |
| **Perusahaan Microsoft; Direktori Aktif; hibrida** | Azure | Integrasi IKLAN asli; perkakas hibrida yang kuat |
| **Pergudangan data; BigQuery; analitik-berat** | GCP | BigQuery adalah yang terbaik di kelasnya; integrasi data yang mulus |
| **Pengembangan asli Kubernetes** | GCP | GKE adalah Kubernet terkelola yang paling canggih |
| **Aplikasi AI / LLM Generatif** | Azure atau GCP | Azure OpenAI untuk model GPT; Vertex AI untuk Gemini |
| **Aplikasi berskala global dengan latensi rendah** | GCP | Jaringan global Google adalah keunggulan sejati |
| **Beban kerja yang berat bagi pemerintah/kepatuhan** | AWS atau Azure | Sebagian besar sertifikasi kepatuhan; Wilayah GovCloud |
| **Startup yang sensitif terhadap biaya** | GCP atau AWS | Paket gratis GCP sangat banyak; AWS memiliki kredit startup |
| **Tumpukan Microsoft / .NET yang ada** | Azure | Integrasi yang erat dengan Visual Studio, .NET, Office 365 |
| **Strategi multi-cloud** | Terraform + ketiganya | Gunakan Terraform untuk mengelola sumber daya di seluruh cloud |
---

## Ringkasan
Ketiga cloud tersebut mampu, andal, dan terus berkembang. Pilihannya biasanya tergantung pada: apa yang sudah diketahui tim Anda, seperti apa kontrak yang ada, dan layanan spesifik apa yang penting bagi beban kerja Anda. Multi-cloud kini semakin umum — gunakan Terraform atau Pulumi untuk menghindari vendor lock-in di lapisan infrastruktur, dan pilih masing-masing cloud sesuai dengan kemampuan terbaiknya.