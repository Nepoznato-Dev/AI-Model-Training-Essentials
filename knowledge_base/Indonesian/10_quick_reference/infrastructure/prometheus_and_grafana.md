---
# Metadata
title: "Prometheus and Grafana"
description: "PromQL, exporters, dashboards, alerting, monitoring stack"
category: "Quick Reference"
subcategory: "Infrastructure"
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
    changes: "Moved to infrastructure/ subfolder; added subcategory field"
  - version: "1.0.0"
    date: "2026-08-05"
    author: "Nepoznato-Dev"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-09"
review_date: "2027-02-05"
reviewed_by: "Quick Reference Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [prometheus, grafana, quick-reference]
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
#Prometheus dan Grafana
Prometheus adalah perangkat pemantauan dan peringatan sumber terbuka yang dirancang untuk keandalan dan skalabilitas. Grafana adalah platform sumber terbuka terkemuka untuk memvisualisasikan data deret waktu. Bersama-sama, mereka membentuk tumpukan pemantauan paling populer untuk infrastruktur dan aplikasi modern. Prometheus mengumpulkan dan menyimpan metrik; Grafana menampilkannya di dashboard.
---

## Arsitektur Prometheus
| Komponen | Deskripsi |
|-----------|-------------|
| **Server Prometheus** | Menghapus metrik dari target; menyimpan data deret waktu; mengevaluasi aturan peringatan |
| **Ekspor** | Mengekspos metrik dari suatu sistem (Node Eksportir, cAdvisor, dll.) |
| **Pintu dorong** | Menerima metrik dari pekerjaan jangka pendek (pekerjaan batch, CI) |
| **Manajer Peringatan** | Menangani peringatan: pengelompokan, pembungkaman, perutean, penghambatan |
| **Penemuan layanan** | Secara otomatis menemukan target (Kubernetes, Konsul, EC2, dll.) |
---

## Konsep Utama
| Konsep | Deskripsi |
|---------|-------------|
| **Metrik** | Pengukuran bernama dengan label opsional dan nilai |
| **Rangkaian waktu** | Aliran titik data untuk kombinasi metrik + label tertentu |
| **Pekerjaan** | Kumpulan target dengan tujuan yang sama |
| **Contoh** | Satu target yang akan dikikis (biasanya sebuah proses) |
| **Mengikis** | Prometheus menarik metrik dari target secara berkala |
| **Label** | Pasangan nilai kunci yang mengukur dimensi metrik (misalnya,`method="GET"`) |
| **Contoh** | Nilai pada suatu titik waktu: (cap waktu, nilai) |
---

## Jenis Metrik
| Ketik | Deskripsi | Kasus Penggunaan |
|------|-------------|----------|
| **Penghitung** | Nilainya meningkat secara monoton (hanya naik) | Jumlah permintaan; kesalahan; tugas selesai |
| **Pengukur** | Nilai yang bisa naik atau turun | Suhu; penggunaan memori; panjang antrian |
| **Histogram** | Pengamatan dikelompokkan berdasarkan nilai | Latensi permintaan; ukuran respons |
| **Ringkasan** | Mirip dengan histogram; menghitung kuantil sisi klien | Persentil latensi |
---

## PromQL (Bahasa Kueri)
### Pertanyaan Dasar
| Kueri | Deskripsi |
|-------|-------------|
| `http_requests_total`| Deret waktu mentah |
| `http_requests_total{method="GET"}`| Filter menurut label |
| `http_requests_total{method="GET", status="200"}`| Filter beberapa label |
| `rate(http_requests_total[5m])`| Tarif per detik selama 5 menit |
| `increase(http_requests_total[1h])`| Total peningkatan selama 1 jam |
| `sum(rate(http_requests_total[5m])) by (status)`| Tarif agregat berdasarkan status |
| `histogram_quantile(0.95, rate(http_duration_bucket[5m]))`| latensi persentil ke-95 |
| `avg(node_cpu_seconds_total{mode="idle"})`| Rata-rata CPU menganggur |
| `1 - avg(rate(node_cpu_seconds_total{mode="idle"}[5m]))`| Pemanfaatan CPU |
### Fungsi Umum
| Fungsi | Deskripsi | Contoh |
|----------|-------------|---------|
| `rate()`| Tingkat kenaikan rata-rata per detik | `rate(requests_total[5m])`|
| `irate()`| Tarif per detik berdasarkan dua titik data terakhir | `irate(requests_total[1m])`|
| `increase()`| Peningkatan total dari rentang waktu | `increase(errors_total[1h])`|
| `sum()`| Jumlahkan seluruh seri | `sum(rate(requests_total[5m])) by (service)`|
| `avg()`| Rata-rata di seluruh seri | `avg(node_memory_usage)`|
| `histogram_quantile()`| Hitung kuantil dari histogram | `histogram_quantile(0.99, rate(duration_bucket[5m]))`|
| `topk()`| Seri K teratas berdasarkan nilai | `topk(5, rate(requests_total[5m]))`|
| `predict_linear()`| Prediksi linier | `predict_linear(disk_usage[1h], 4*3600)`|
| `absent()`| Periksa apakah metrik tidak ada | `absent(up{job="myapp"})`|
---

## Eksportir Umum
| Eksportir | Apa yang Dipantaunya |
|----------|-----------------|
| **Ekspor Node** | Metrik host Linux/Unix (CPU, memori, disk, jaringan) |
| **penasihat c** | Metrik kontainer (CPU, memori, jaringan, sistem file) |
| **Ekspor MySQL** | Metrik basis data MySQL |
| **Ekspor PostgreSQL** | Metrik basis data PostgreSQL |
| **Ekspor Redis** | Metrik Redis |
| **Eksportir Blackbox** | Selidiki titik akhir melalui HTTP, HTTPS, DNS, TCP, ICMP |
| **Ekspor SNMP** | Metrik perangkat jaringan melalui SNMP |
| **Ekspor JSON** | Metrik khusus dari API JSON |
---

## Grafana
### Konsep Utama
| Konsep | Deskripsi |
|---------|-------------|
| **Sumber data** | Koneksi ke Prometheus (atau backend lainnya) |
| **Dasbor** | Kumpulan panel yang disusun dalam tata letak |
| **Panel** | Visualisasi tunggal (grafik, pengukur, tabel, peta panas) |
| **Variabel** | Filter dinamis untuk dasbor (misalnya, pilih instance) |
| **Anotasi** | Tandai peristiwa pada grafik (penyebaran, insiden) |
| **Aturan peringatan** | Peringatan berbasis ambang batas dalam Grafana |
| **Templat** | Pola dasbor yang dapat digunakan kembali dengan variabel |
### Pola Dasbor yang Berguna
| Pola | Deskripsi |
|---------|-------------|
| **Baris Ikhtisar** | Sekilas tentang metrik utama: tingkat kesalahan, latensi, throughput |
| **Perincian** | Klik dari ringkasan ke tampilan detail menggunakan variabel |
| **Metode MERAH** | Nilai, Kesalahan, Durasi — tiga metrik layanan utama |
| **GUNAKAN metode** | Pemanfaatan, Saturasi, Kesalahan — untuk infrastruktur |
| **Sinyal emas** | Latensi, lalu lintas, kesalahan, saturasi (buku SRE Google) |
---

## Peringatan
### Struktur Aturan Peringatan
```yaml
groups:
  - name: example
    rules:
      - alert: HighErrorRate
        expr: rate(http_requests_total{status=~"5.."}[5m]) / rate(http_requests_total[5m]) > 0.05
        for: 5m
        labels:
          severity: critical
        annotations:
          summary: "High error rate on {{ $labels.instance }}"
          description: "Error rate is {{ $value | humanizePercentage }}"
```

### Perutean Manajer Peringatan
| Konsep | Deskripsi |
|---------|-------------|
| **Grup** | Gabungkan peringatan serupa menjadi satu pemberitahuan |
| **Rute** | Pohon pencocokan yang menentukan kemana perginya peringatan |
| **Penerima** | Tempat mengirim peringatan (email, Slack, PagerDuty, webhook) |
| **Menghambat** | Menekan peringatan ketika peringatan lain diaktifkan |
| **Diam** | Nonaktifkan sementara peringatan oleh pencocokan label |
---

## Pemecahan masalah
| Masalah | Solusi |
|---------|----------|
| **Targetkan turun** | Periksa apakah eksportir sedang berjalan; periksa jaringan/firewall; verifikasi konfigurasi scrape |
| **Tidak ada data** | Periksa ejaan nama metrik; periksa filter label; verifikasi rentang waktu |
| **Kardinalitas tinggi** | Terlalu banyak kombinasi label; mengurangi nilai label; gunakan aturan pencatatan |
| **Kueri lambat** | Gunakan aturan pencatatan untuk kueri kompleks; meningkatkan interval gesekan |
| **Waspada kelelahan** | Sesuaikan ambang batas; tambahkan durasi `for`; peringatan terkait grup |
| **Metrik tidak ada setelah restart** | Prometheus menyimpan data secara lokal; periksa pengaturan retensi |
---

## Ringkasan
Prometheus memantau sistem dengan mengambil metrik dari eksportir secara berkala. Metrik terdiri dari empat jenis: penghitung (hanya naik), pengukur (naik dan turun), histogram (pengamatan dalam keranjang), dan ringkasan (kuantil). PromQL adalah bahasa kueri —`rate()`,`increase()`,`histogram_quantile()`, dan fungsi agregasi (`sum`,`avg`) adalah operasi yang paling umum. Grafana memvisualisasikan data Prometheus di dasbor dengan panel, variabel, dan anotasi. Peringatan menggunakan Alertmanager untuk mengelompokkan, merutekan, membungkam, dan menghambat peringatan. Pola pemantauan utama adalah sinyal emas Google (latensi, lalu lintas, kesalahan, saturasi) dan metode RED (tingkat, kesalahan, durasi) untuk layanan dan metode USE (pemanfaatan, saturasi, kesalahan) untuk infrastruktur.