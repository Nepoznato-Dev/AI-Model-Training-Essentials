---
# Metadata
title: "Data Engineering and Pipelines"
description: "ETL/ELT, data lakes, orchestration, Kafka, feature stores"
category: "AI and Machine Learning"
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
reviewed_by: "AI & Machine Learning Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [data, engineering, pipelines, ai-and-machine-learning]
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
# Rekayasa Data dan Saluran Pipa
Rekayasa data adalah disiplin membangun sistem yang memindahkan, mengubah, dan menyimpan data dalam skala besar. Tanpa saluran data yang andal, model pembelajaran mesin tidak dapat dilatih, dasbor menunjukkan angka-angka yang sudah ketinggalan zaman, dan keputusan bisnis didasarkan pada dugaan. File ini mencakup arsitektur, alat, dan praktik untuk membangun infrastruktur data yang berfungsi.
---

## ETL vs ELT
| Pendekatan | Cara Kerja | Terbaik Untuk | Alat |
|----------|-------------|----------|-------|
| **ETL** (Ekstrak → Transformasi → Muat) | Transformasi data *sebelum* dimuat ke gudang | Gudang tradisional dengan komputasi terbatas | Informatika, Talend, Apache NiFi |
| **ELT** (Ekstrak → Muat → Transformasi) | Muat data mentah terlebih dahulu; mengubah *di dalam* gudang | Gudang cloud modern dengan komputasi elastis | dbt, Fivetran, Airbyte + BigQuery/Kepingan Salju |
Peralihan dari ETL ke ELT didorong oleh gudang data cloud (BigQuery, Snowflake, Redshift) yang dapat menskalakan komputasi secara independen dari penyimpanan. Tidak perlu lagi memproses semuanya terlebih dahulu sebelum memuat.
---

## Data Lake vs Gudang Data
| Fitur | Danau Data | Gudang Data |
|---------|-----------|---------------|
| **Format Data** | Format asli dan mentah (skema-saat-dibaca) | Terstruktur, diproses (skema-on-write) |
| **Skema** | Didefinisikan pada waktu kueri | Didefinisikan sebelum memuat |
| **Tipe Data** | Terstruktur, semi terstruktur, tidak terstruktur | Terutama terstruktur |
| **Pengguna** | Ilmuwan data, insinyur | Analis bisnis, alat BI |
| **Biaya** | Penyimpanan lebih murah (penyimpanan objek) | Lebih mahal (dioptimalkan untuk pertanyaan) |
| **Contoh** | AWS S3, Danau Data Azure, GCS | Kepingan Salju, BigQuery, Pergeseran Merah |
Pendekatan modern adalah **rumah danau**: menggabungkan penyimpanan danau yang murah dan fleksibel dengan fitur pengelolaan dan kinerja gudang. Delta Lake, Apache Iceberg, dan Apache Hudi adalah teknologi utama di sini.
---

## Arsitektur Saluran Pipa
### Batch vs Streaming
| Modus | Deskripsi | Latensi | Kasus Penggunaan |
|------|-------------|---------|----------|
| **Batch** | Memproses data dalam jumlah besar pada interval terjadwal | Menit ke jam | Laporan harian, pekerjaan ETL, pengayaan data |
| **Streaming** | Memproses data terus menerus saat tiba | Milidetik ke detik | Dasbor waktu nyata, deteksi penipuan, peringatan |
| **Micro-batch** | Batch kecil dengan interval yang sangat singkat | Detik | Hampir real-time dengan kesederhanaan batch |
### Komponen Saluran Pipa
Saluran data pada umumnya memiliki tahapan berikut:
| Tahap | Deskripsi | Alat |
|-------|-------------|-------|
| **Penelanan** | Kumpulkan data dari sumber | Kafka, Airbyte, Fivetran, Debezium |
| **Transformasi** | Bersihkan, perkaya, agregat | dbt, Spark, Panda |
| **Penyimpanan** | Pertahankan data yang diproses | BigQuery, Kepingan Salju, S3, Danau Delta |
| **Melayani** | Menyediakan data bagi konsumen | API, dasbor, penyimpanan fitur ML |
| **Orkestrasi** | Jadwalkan dan kelola dependensi | Aliran Udara, Prefek, Belati |
| **Pemantauan** | Lacak kesehatan saluran pipa dan kualitas data | Harapan Besar, Monte Carlo, lansiran khusus |
---

## Alat Orkestrasi
| Alat | Pendekatan | Kekuatan |
|------|----------|----------|
| **Aliran Udara Apache** | DAG berbasis Python; standar industri | Ekosistem besar, matang, fleksibel |
| **Prefek** | Python-asli; API lebih bersih dari Airflow | Desain modern, penanganan kesalahan hebat |
| **Belati** | Berpusat pada aset; pendekatan rekayasa perangkat lunak | Ketik sistem, pengujian, observasi |
| **Luigi** | Alat saluran pipa asli Spotify | Sederhana, namun kurang aktif dikembangkan |
### Contoh Aliran Udara
```python
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def extract():
    # Pull data from source
    pass

def transform():
    # Clean and process
    pass

def load():
    # Write to warehouse
    pass

with DAG("etl_pipeline", start_date=datetime(2024, 1, 1),
         schedule="@daily", catchup=False) as dag:
    e = PythonOperator(task_id="extract", python_callable=extract)
    t = PythonOperator(task_id="transform", python_callable=transform)
    l = PythonOperator(task_id="load", python_callable=load)
    
    e >> t >> l  # Define dependencies
```

---

##Apache Kafka
Kafka adalah tulang punggung banyak sistem data real-time. Ini adalah log peristiwa terdistribusi yang menyediakan pesan dengan throughput tinggi dan toleran terhadap kesalahan.
### Konsep Inti
| Konsep | Deskripsi |
|---------|-------------|
| **Topik** | Kategori pesan (misalnya,`orders`,`user-events`) |
| **Partisi** | Topik dibagi menjadi beberapa partisi untuk paralelisme |
| **Produser** | Aplikasi yang menulis pesan ke topik |
| **Konsumen** | Aplikasi yang membaca pesan dari topik |
| **Kelompok Konsumen** | Sekelompok konsumen yang berbagi beban membaca suatu topik |
| **Mengimbangi** | Posisi konsumen dalam partisi |
| **Broker** | Node server Kafka |
### Kapan Menggunakan Kafka
- **Streaming acara**: Pemrosesan acara real-time dalam skala besar.
- **Layanan pemisahan**: Produsen dan konsumen tidak perlu saling mengenal.
- **Putar Ulang**: Pesan dipertahankan; konsumen dapat membaca ulang dari offset mana pun.
- **Tekanan Balik**: Kafka secara alami menangani perbedaan kecepatan antara produsen dan konsumen.
---

## Pemodelan Data
### Skema Bintang vs Skema Kepingan Salju
| Skema | Struktur | Kelebihan | Kontra |
|--------|-----------|------|------|
| **Bintang** | Tabel fakta pusat dikelilingi oleh tabel dimensi yang didenormalisasi | Pertanyaan sederhana, bacaan cepat | Redundansi data |
| **Kepingan Salju** | Tabel dimensi dinormalisasi (dibagi menjadi sub-tabel) | Lebih sedikit redundansi | Lebih banyak yang bergabung, kueri lebih lambat |
### Tabel Fakta dan Dimensi
| Tipe Tabel | Berisi | Contoh |
|-----------|----------|---------|
| **Fakta** | Peristiwa terukur (metrik) | `orders`(id_pesanan, id_produk, id_pelanggan, jumlah, tanggal) |
| **Dimensi** | Atribut deskriptif | `products`(id_produk, nama, kategori, harga),`customers`(id_pelanggan, nama, kota) |
---

## Toko Fitur
Penyimpanan fitur adalah gudang terpusat dari fitur-fitur ML — nilai turunan yang digunakan sebagai masukan ke model (misalnya, "nilai pesanan rata-rata pengguna dalam 30 hari terakhir").
| Kemampuan | Deskripsi |
|-----------|-------------|
| **Registrasi Fitur** | Katalog fitur yang tersedia dengan metadata |
| **Toko Offline** | Fitur historis untuk pelatihan model (batch) |
| **Toko Online** | Fitur latensi rendah yang berfungsi untuk inferensi real-time |
| **Pemantauan Fitur** | Deteksi penyimpangan, nilai yang hilang, perubahan distribusi |
| Alat | Deskripsi |
|------|-------------|
| **Pesta** | Sumber terbuka; bekerja dengan kerangka ML apa pun |
| **Tekton** | Komersial; platform fitur waktu nyata |
| **Pekerjaan Hops** | Sumber terbuka; platform ML lengkap dengan toko fitur |
| **Toko Fitur Databricks** | Terintegrasi dengan Databricks/Spark |
---

## Kualitas Data
Kualitas data adalah penyebab utama proyek ML. Sampah masuk, sampah keluar.
### Dimensi Kualitas
| Dimensi | Pertanyaan |
|-----------|----------|
| **Akurasi** | Apakah data mencerminkan kenyataan? |
| **Kelengkapan** | Apakah kolom wajib diisi? |
| **Konsistensi** | Apakah nilai-nilai disepakati di berbagai sumber? |
| **Ketepatan waktu** | Apakah datanya terkini? |
| **Validitas** | Apakah nilai-nilai sesuai dengan aturan yang ditetapkan? |
| **Keunikan** | Apakah ada catatan duplikat? |
### Alat Kualitas Data
| Alat | Pendekatan |
|------|----------|
| **Harapan Besar** | Berbasis Python; tentukan "ekspektasi" tentang data |
| **Monte Carlo** | Platform observasi data yang didukung ML |
| **tes dbt** | Tes bawaan untuk data gudang (unik, not_null, hubungan) |
| **Soda** | Pemindaian kualitas data sumber terbuka |
---

## Tata Kelola Data
Tata kelola data memastikan bahwa data dikelola secara bertanggung jawab di seluruh organisasi.
| Daerah | Deskripsi |
|------|-------------|
| **Katalog Data** | Inventaris kumpulan data dengan metadata yang dapat dicari (Amundsen, DataHub, Atlan) |
| **Silsilah Data** | Lacak dari mana data berasal dan bagaimana transformasinya |
| **Kontrol Akses** | Izin berbasis peran; siapa yang bisa membaca/menulis apa |
| **Kepatuhan** | GDPR, CCPA, kepatuhan HIPAA |
| **Kepemilikan Data** | Kepemilikan yang jelas untuk setiap dataset (pengurusan) |
| **Kebijakan Retensi** | Tentukan berapa lama data disimpan dan kapan dihapus |
---

## Tumpukan Data Modern
"Tumpukan data modern" mengacu pada kombinasi alat yang umum digunakan oleh tim data saat ini:
| Lapisan | Alat Khas |
|-------|--------------|
| **Penelanan** | Fivetran, Airbyte |
| **Gudang** | Kepingan Salju, BigQuery, Pergeseran Merah |
| **Transformasi** | dbt |
| **Orkestrasi** | Aliran Udara, Prefek, Belati |
| **BI / Visualisasi** | Penampil, Metabase, Tableau |
| **Membalikkan ETL** | Sensus, Hightouch (sinkronisasi data gudang kembali ke alat) |
| **Kualitas Data** | Harapan Besar, Monte Carlo |
Trennya mengarah pada alat modular dan terbaik yang dihubungkan dengan standar terbuka (SQL, model dbt, Airflow DAG) dibandingkan platform monolitik.