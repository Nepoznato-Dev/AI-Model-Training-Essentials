# Arsitektur Awan

## Dasar-dasar Komputasi Awan

### Apa itu Komputasi Awan?
Pengiriman sumber daya komputasi berdasarkan permintaan (server, penyimpanan, database, jaringan, perangkat lunak) melalui internet dengan harga bayar sesuai pemakaian.

### Karakteristik Penting (Definisi NIST)
- **Layanan Mandiri Sesuai Permintaan**: Menyediakan sumber daya tanpa interaksi manusia
- **Akses Jaringan Luas**: Tersedia melalui jaringan melalui mekanisme standar
- **Pengumpulan Sumber Daya**: Model multi-penyewa dengan penetapan dinamis
- **Elastisitas Cepat**: Menskalakan ke luar dan ke dalam dengan cepat
- **Layanan Terukur**: Penggunaan sumber daya dipantau dan ditagih

### Model Penerapan Cloud
- **Public Cloud**: Dimiliki oleh penyedia, infrastruktur bersama (AWS, Azure, GCP)
- **Private Cloud**: Didedikasikan untuk satu organisasi (on-premise atau host)
- **Hybrid Cloud**: Kombinasi cloud publik dan pribadi
- **Multi-Cloud**: Menggunakan beberapa penyedia cloud publik
- **Community Cloud**: Dibagikan oleh organisasi yang memiliki keprihatinan yang sama

### Model Layanan

#### Infrastruktur sebagai Layanan (IaaS)
- **Menyediakan**: Mesin virtual, penyimpanan, jaringan, sistem operasi
- **Contoh**: AWS EC2, Google Compute Engine, Azure VM
- **Kasus Penggunaan**: Migrasi angkat-dan-geser, lingkungan pengembangan, kebutuhan kontrol tinggi

#### Platform sebagai Layanan (PaaS)
- **Menyediakan**: Platform pengembangan, database, middleware
- **Contoh**: Heroku, Google App Engine, AWS Elastic Beanstalk
- **Kasus Penggunaan**: Pengembangan aplikasi, penerapan API, layanan mikro

#### Perangkat Lunak sebagai Layanan (SaaS)
- **Menyediakan**: Aplikasi lengkap melalui internet
- **Contoh**: Salesforce, Google Workspace, Microsoft 365, Slack
- **Kasus Penggunaan**: Email, CRM, kolaborasi, aplikasi bisnis

#### Berfungsi sebagai Layanan (FaaS) / Tanpa Server
- **Menyediakan**: Eksekusi fungsi berdasarkan peristiwa
- **Contoh**: AWS Lambda, Azure Functions, Google Cloud Functions
- **Kasus Penggunaan**: Pemrosesan peristiwa, API, tugas terjadwal, pemrosesan waktu nyata

## Penyedia Cloud Utama

### Layanan Web Amazon (AWS)
- **Pangsa Pasar**: ~32% (penyedia terbesar)
- **Layanan Utama**:
  - Hitung: EC2, Lambda, ECS, EKS
  - Penyimpanan: S3, EBS, Gletser
  - Basis Data: RDS, DynamoDB, Aurora
  - Jaringan: VPC, Route 53, CloudFront
  - AI/ML: SageMaker, Pengakuan, Pemahaman

###Microsoft Azure
- **Pangsa Pasar**: ~23%
- **Kelebihan**: Integrasi perusahaan, cloud hibrid, ekosistem Microsoft
- **Layanan Utama**:
  - Komputasi: Mesin Virtual, Fungsi Azure, AKS
  - Penyimpanan: Penyimpanan Blob, Penyimpanan Disk
  - Basis Data: Basis Data SQL, Cosmos DB
  - Jaringan: Jaringan Virtual, Manajer Lalu Lintas
  - AI/ML: Azure ML, Layanan Kognitif

### Google Cloud Platform (GCP)
- **Pangsa Pasar**: ~10%
- **Kelebihan**: Analisis data, AI/ML, Kubernetes
- **Layanan Utama**:
  - Komputasi: Mesin Komputasi, Fungsi Cloud, GKE
  - Penyimpanan: Penyimpanan Cloud, Disk Persisten
  - Basis Data: Cloud SQL, Firestore, Bigtable
  - Analisis: BigQuery, Aliran Data, Pub/Sub
  - AI/ML: Vertex AI, AutoML

### Penyedia Lainnya
- **IBM Cloud**: Fokus perusahaan, Watson AI
- **Oracle Cloud**: Beban kerja basis data, aplikasi perusahaan
- **Alibaba Cloud**: Dominan di Asia-Pasifik
- **DigitalOcean**: Penawaran yang disederhanakan dan ramah pengembang

## Pola Arsitektur Cloud

### Prinsip Kerangka Kerja yang Terarsitektur dengan Baik

#### Keunggulan Operasional
- Mengotomatiskan operasi
- Lakukan perubahan yang sering dan dapat dibalik
- Sempurnakan prosedur secara terus menerus
- Antisipasi kegagalan

#### Keamanan
- Menerapkan landasan identitas yang kuat
- Aktifkan ketertelusuran
- Terapkan keamanan di semua lapisan
- Mengotomatiskan praktik terbaik keamanan
- Lindungi data saat transit dan saat istirahat

#### Keandalan
- Uji prosedur pemulihan
- Secara otomatis pulih dari kegagalan
- Skala secara horizontal untuk ketersediaan
- Berhenti menebak kapasitas
- Kelola perubahan otomatisasi

#### Efisiensi Kinerja
- Mendemokratisasikan teknologi maju
- Mendunia dalam hitungan menit
- Gunakan arsitektur tanpa server
- Bereksperimenlah lebih sering
- Pertimbangkan simpati mekanis

#### Optimasi Biaya
- Mengadopsi model konsumsi
- Ukur efisiensi keseluruhan
- Berhenti menghabiskan uang untuk pekerjaan yang tidak terdiferensiasi
- Menganalisis dan mengatribusikan pengeluaran
- Gunakan layanan terkelola

### Pola Arsitektur Umum

#### Arsitektur Layanan Mikro
- Menguraikan aplikasi menjadi layanan kecil dan independen
- Setiap layanan memiliki data dan logikanya sendiri
- Berkomunikasi melalui API (REST, gRPC, perpesanan)
- Menyebarkan secara mandiri
- **Manfaat**: Skalabilitas, isolasi kesalahan, keragaman teknologi
- **Tantangan**: Kompleksitas terdistribusi, konsistensi data, pemantauan

#### Arsitektur Berbasis Peristiwa
- Komponen berkomunikasi melalui peristiwa
- Produsen mengeluarkan peristiwa, konsumen bereaksi
- **Pola**: Sumber acara, CQRS, pub/sub
- **Teknologi**: Kafka, SNS/SQS, EventBridge, Pub/Sub
- **Manfaat**: Kopling longgar, skalabilitas, pemrosesan real-time#### Arsitektur Tanpa Server
- Tidak diperlukan manajemen server
- Bayar per eksekusi
- Penskalaan otomatis
- **Komponen**: Fungsi, API Gateway, layanan terkelola
- **Manfaat**: Efisiensi biaya, pengurangan operasi, penerapan cepat
- **Pertimbangan**: Cold start, penguncian vendor, batas eksekusi

#### Arsitektur Berlapis (N-Tier)
- Lapisan presentasi (UI)
- Lapisan logika Aplikasi/Bisnis
- Lapisan akses data
- Lapisan basis data
- **Manfaat**: Pemisahan kekhawatiran, pemeliharaan
- **Umum**: Aplikasi web 3 tingkat

#### Arsitektur Berbasis Ruang
- Menangani konkurensi tinggi dengan data terdistribusi
- Memori tervirtualisasi di seluruh server
- Memproses skala node secara independen
- **Kasus Penggunaan**: Aplikasi bervolume tinggi dan latensi rendah

## Layanan Komputasi

### Mesin Virtual
- **Jenis**: Tujuan umum, komputasi dioptimalkan, memori dioptimalkan, GPU
- **Harga**: Instans sesuai permintaan, instans yang dipesan, instans spot
- **Manajemen**: Grup penskalaan otomatis, penyeimbang beban
- **Praktik Terbaik**: Penyesuaian ukuran, penandaan, pemantauan, patching

### Kontainer
- **Docker**: Standar waktu proses kontainer
- **Orkestrasi**: Kubernetes (EKS, AKS, GKE), ECS, Fargate
- **Manfaat**: Portabilitas, efisiensi, konsistensi
- **Registri**: ECR, GCR, ACR, Docker Hub

### Fungsi Tanpa Server
- **Model Eksekusi**: Dipicu peristiwa, tanpa kewarganegaraan
- **Batas**: Waktu eksekusi, memori, eksekusi bersamaan
- **Kasus Penggunaan**: API, pemrosesan file, pekerjaan terjadwal, backend IoT
- **Pemantauan**: Jumlah pemanggilan, kesalahan, durasi, cold start

## Solusi Penyimpanan

### Penyimpanan Objek
- **Karakteristik**: Struktur datar, metadata, akses HTTP
- **Contoh**: AWS S3, Google Cloud Storage, Azure Blob
- **Kasus Penggunaan**: Aset statis, cadangan, data lake, arsip
- **Kelas Penyimpanan**: Panas, dingin, dingin, arsip (bervariasi biaya/akses)

### Blokir Penyimpanan
- **Karakteristik**: Volume mentah, dilampirkan ke VM
- **Contoh**: AWS EBS, Google Persistent Disk, Azure Disk
- **Kasus Penggunaan**: Basis data, volume boot, kebutuhan kinerja tinggi
- **Jenis**: SSD, HDD, IOPS yang disediakan

### Penyimpanan Berkas
- **Karakteristik**: Sistem file bersama, protokol NFS/SMB
- **Contoh**: AWS EFS, Google Filestore, Azure Files
- **Kasus Penggunaan**: Manajemen konten, konfigurasi bersama, angkat dan geser

### Penyimpanan Arsip
- **Karakteristik**: Biaya terendah, penundaan pengambilan
- **Contoh**: S3 Glacier, Penyimpanan Arsip Azure
- **Kasus Penggunaan**: Kepatuhan, pencadangan jangka panjang, data historis

## Layanan Basis Data

### Basis Data Relasional Terkelola
- **Layanan**: AWS RDS/Aurora, Google Cloud SQL, Azure SQL Database
- **Fitur**: Pencadangan otomatis, patching, penskalaan, replikasi
- **Mesin**: MySQL, PostgreSQL, MariaDB, Oracle, SQL Server

### Basis Data NoSQL
- **Dokumen**: DocumentDB, Firestore, Cosmos DB
- **Nilai-Kunci**: DynamoDB, Redis Cache
- **Kolom Lebar**: Bigtable, Cassandra (dikelola)
- **Grafik**: Neptunus, Cosmos DB (API grafik)

### Pergudangan Data
- **Layanan**: Snowflake, Redshift, BigQuery, Synapse
- **Karakteristik**: Penyimpanan kolom, arsitektur MPP
- **Kasus Penggunaan**: Analisis, BI, analisis data skala besar

### Layanan Cache
- **Dalam Memori**: ElastiCache (Redis/Memcached), Cloud Memorystore
- **Caching CDN**: CloudFront, Cloud CDN, Azure CDN
- **Kasus Penggunaan**: Penyimpanan sesi, cache kueri, pengiriman konten

## Jaringan

### Jaringan Virtual
- **VPC/VNet**: Lingkungan jaringan terisolasi
- **Subnet**: Publik (terhubung ke internet), pribadi (khusus internal)
- **Pengalamatan IP**: Blok CIDR, IPv4/IPv6
- **Tabel Rute**: Mengontrol arus lalu lintas

### Penyeimbangan Beban
- **Jenis**: Aplikasi (L7), Jaringan (L4), Gerbang
- **Fitur**: Pemeriksaan kesehatan, penghentian SSL, sesi melekat
- **Layanan**: ELB/ALB/NLB, Cloud Load Balancing, Azure Load Balancer

### Jaringan Pengiriman Konten (CDN)
- **Tujuan**: Menyimpan konten dalam cache di lokasi edge
- **Manfaat**: Mengurangi latensi, beban asal lebih rendah, distribusi global
- **Layanan**: CloudFront, Cloud CDN, Azure CDN, Akamai

### Layanan DNS
- **Fungsi**: Pendaftaran domain, perutean, pemeriksaan kesehatan
- **Layanan**: Route 53, Cloud DNS, Azure DNS
- **Kebijakan Perutean**: Sederhana, berbobot, berbasis latensi, geolokasi, failover

### Opsi Konektivitas
- **Internet Gateway**: Akses internet publik
- **NAT Gateway**: Akses keluar subnet pribadi
- **VPN**: Terowongan terenkripsi ke lokal
- **Direct Connect/ExpressRoute**: Koneksi pribadi khusus
- **Peering VPC**: Menghubungkan VPC di dalam/antar akun

## Keamanan di Cloud

### Model Tanggung Jawab Bersama
- **Tanggung Jawab Penyedia**: Keamanan cloud (infrastruktur)
- **Tanggung Jawab Pelanggan**: Keamanan DI cloud (data, aplikasi, akses)
- **Bervariasi Berdasarkan Layanan**: Lebih terkelola = lebih banyak tanggung jawab penyedia

### Manajemen Identitas dan Akses (IAM)
- **Pengguna**: Identitas individu
- **Grup**: Koleksi pengguna
- **Peran**: Kredensial sementara untuk layanan/pengguna
- **Kebijakan**: Dokumen JSON yang menjelaskan izin
- **Prinsip**: Hak istimewa paling kecil, pemisahan tugas### Keamanan Jaringan
- **Grup Keamanan**: Misalnya, firewall stateful
- **ACL Jaringan**: Firewall tanpa status untuk subnet
- **Web Application Firewall (WAF)**: Melindungi dari eksploitasi web
- **Perlindungan DDoS**: Perisai, Cloud Armor, Perlindungan DDoS

### Perlindungan Data
- **Enkripsi Saat Istirahat**: KMS, kunci yang dikelola pelanggan
- **Enkripsi dalam Transit**: TLS/SSL, HTTPS
- **Manajemen Kunci**: HSM, rotasi kunci, jalur audit
- **Manajemen Rahasia**: Manajer Rahasia, Gudang Kunci

### Kepatuhan dan Tata Kelola
- **Sertifikasi**: SOC 2, ISO 27001, HIPAA, PCI-DSS, GDPR
- **Alat**: Penegakan kebijakan, pelaporan kepatuhan, log audit
- **Kerangka Kerja**: Aliansi Keamanan Cloud, NIST CSF

## DevOps di Cloud

### Layanan CI/CD
- **AWS**: CodePipeline, CodeBuild, CodeDeploy
- **Azure**: Azure DevOps, Tindakan GitHub
- **GCP**: Pembuatan Cloud, Penerapan Cloud
- **Pihak ketiga**: Jenkins, CircleCI, GitLab CI

### Infrastruktur sebagai Kode (IaC)
- **Terraform**: Multi-cloud, deklaratif, manajemen negara
- **CloudFormation**: templat YAML/JSON asli AWS
- **Templat ARM**: Azure asli
- **Manajer Penerapan**: asli GCP
- **Pulumi**: Infrastruktur menggunakan bahasa pemrograman
- **Manfaat**: Kontrol versi, pengulangan, dokumentasi

### Manajemen Konfigurasi
- **Mungkin**: Buku pedoman YAML tanpa agen
- **Koki**: Ekosistem matang berbasis Ruby
- **Boneka**: Pelaporan yang deklaratif dan kuat
- **SaltStack**: Cepat, berbasis Python

### Pemantauan dan Observabilitas
- **Metrik**: CloudWatch, Cloud Monitoring, Azure Monitor
- **Logging**: CloudWatch Logs, Cloud Logging, Analisis Log
- **Pelacakan**: X-Ray, Cloud Trace, Wawasan Aplikasi
- **Dasbor**: Dasbor CloudWatch, Cloud Console
- **Peringatan**: SNS, peringatan Cloud Monitoring, Grup Tindakan

### Orkestrasi Kontainer
- **Kubernetes**: Orkestrasi standar industri
- **Layanan Terkelola**: EKS, AKS, GKE
- **Service Mesh**: Istio, Linkerd (manajemen lalu lintas, keamanan)
- **GitOps**: ArgoCD, Flux (penerapan deklaratif)

## Manajemen Biaya

### Model Penetapan Harga
- **Bayar sesuai pemakaian**: Bayar sesuai penggunaan
- **Instans Cadangan**: komitmen 1-3 tahun, diskon signifikan
- **Instans Spot**: Tawaran untuk kapasitas yang tidak terpakai, dapat diinterupsi
- **Paket Tabungan**: Harga komitmen fleksibel
- **Tingkat Gratis**: Penggunaan gratis terbatas untuk akun baru

### Strategi Optimasi Biaya
- **Ukuran yang tepat**: Mencocokkan jenis instans dengan kebutuhan beban kerja
- **Penskalaan otomatis**: Menskalakan berdasarkan permintaan
- **Kapasitas Cadangan**: Berkomitmen pada beban kerja kondisi stabil
- **Penggunaan Spot**: Gunakan untuk beban kerja yang fleksibel dan toleran terhadap kesalahan
- **Tingkat Penyimpanan**: Pindahkan data yang jarang ke tingkat yang lebih murah
- **Pembersihan**: Hapus sumber daya, snapshot, AMI yang tidak digunakan

### Alat Manajemen Biaya
- **AWS**: Penjelajah Biaya, Anggaran, Penasihat Tepercaya
- **Azure**: Manajemen Biaya, Penasihat
- **GCP**: Laporan penagihan, Rekomendasi
- **Pihak ketiga**: CloudHealth, CloudCheckr, Datadog

## Ketersediaan Tinggi dan Pemulihan Bencana

### Konsep Ketersediaan
- **Availability Zone**: Pusat data yang terpisah secara fisik dalam wilayah
- **Wilayah**: Wilayah geografis dengan beberapa AZ
- **Lokasi Edge**: Lokasi cache CDN secara global

### Strategi HA
- **Multi-AZ**: Disebarkan di seluruh zona ketersediaan
- **Penyembuhan otomatis**: Penggantian otomatis instance yang gagal
- **Load Balancing**: Mendistribusikan lalu lintas ke seluruh instance yang sehat
- **Replikasi Basis Data**: Penerapan multi-AZ, replika baca

### Strategi Pemulihan Bencana
- **Pencadangan dan Pemulihan**: Pencadangan berkala, pemulihan bila diperlukan (biaya terendah)
- **Pilot Light**: Elemen inti berjalan, ditingkatkan selama bencana
- **Siaga Hangat**: Versi yang diperkecil selalu berjalan
- **Multi-Situs Aktif/Aktif**: Produksi penuh di beberapa wilayah (biaya tertinggi)

### RTO dan RPO
- **Tujuan Waktu Pemulihan (RTO)**: Waktu henti maksimum yang dapat diterima
- **Recovery Point Objective (RPO)**: Kehilangan data maksimum yang dapat diterima
- **Pemilihan Strategi**: Berdasarkan kebutuhan bisnis dan anggaran

## Tren yang Muncul

### Komputasi Tepi
- Memproses data lebih dekat ke sumbernya
- **Layanan**: AWS Outposts, Wavelength, Azure Edge, Cloud CDN
- **Kasus Penggunaan**: IoT, analisis real-time, aplikasi latensi rendah

### Multi-Cloud dan Cloud Hibrid
- Hindari penguncian vendor
- Memanfaatkan layanan terbaik
- **Alat**: Terraform, Anthos, Arc, CloudHealth

### Layanan AI/ML
- Model terlatih: Penglihatan, ucapan, bahasa
- Pelatihan model khusus: SageMaker, Vertex AI, Azure ML
- MLOps: Penerapan model, pemantauan, tata kelola

### Komputasi Kuantum
- **Layanan**: AWS Braket, Azure Quantum
- **Status**: Tahap awal, eksperimental
- **Potensi**: Kriptografi, optimasi, penemuan obat

### Cloud Berkelanjutan
- Pelacakan jejak karbon
- Komitmen energi terbarukan
- Pemanfaatan sumber daya yang efisien
- Pola arsitektur hijau