---
# Metadata
title: "DevOps and CI/CD"
description: "CI/CD pipelines, Docker, Kubernetes, Terraform, GitOps"
category: "Coding and Technology"
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
reviewed_by: "Coding & Technology Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [devops, cicd, coding-and-technology]
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
# DevOps dan CI/CD
DevOps adalah kombinasi filosofi budaya, praktik, dan alat yang memungkinkan tim menghadirkan perangkat lunak dengan lebih cepat dan andal. Ini meruntuhkan tembok antara pengembang (yang ingin melakukan perubahan) dan operasi (yang menginginkan stabilitas). CI/CD — Integrasi Berkelanjutan dan Pengiriman Berkelanjutan — adalah tulang punggung otomatisasi yang memungkinkan hal ini.
---

## Saluran Pipa CI/CD
### Arti Sebenarnya CI/CD
| Istilah | Apa Fungsinya |
|------|-------------|
| **Integrasi Berkelanjutan (CI)** | Pengembang sering menggabungkan kode; setiap penggabungan memicu pembuatan dan pengujian otomatis |
| **Pengiriman Berkelanjutan (CD)** | Kode selalu dalam keadaan dapat diterapkan; merilis ke produksi adalah keputusan manual |
| **Penerapan Berkelanjutan** | Setiap perubahan yang lolos pengujian akan masuk ke produksi secara otomatis — tanpa gerbang manual |
### Tahapan Saluran Pipa Biasa
| Tahap | Apa yang Terjadi | Alat |
|-------|-------------|-------|
| **Sumber** | Pengembang memasukkan kode ke Git | GitHub, GitLab, Bitbucket |
| **Bangun** | Kompilasi kode, instal dependensi | Maven, Gradle, npm, pip |
| **Tes** | Jalankan unit, integrasi, pemeriksaan lint | Bercanda, pytest, JUnit |
| **Paket** | Bangun image atau artefak Docker | Docker, Paket Bangun |
| **Menerapkan (pementasan)** | Terapkan ke lingkungan pementasan | Kubernetes, ECS, VM |
| **Tes (pementasan)** | Tes integrasi, tes asap | Selenium, Tukang Pos |
| **Penerapan (produksi)** | Rilis ke produksi | Biru-hijau, kenari, bergulir |
| **Pemantau** | Amati kesehatan, kesalahan, kinerja | Prometheus, Grafana, Datadog |
### Alat CI/CD Dibandingkan
| Alat | Ketik | Kekuatan |
|------|------|----------|
| **Tindakan GitHub** | Cloud CI/CD | Sangat terintegrasi dengan GitHub; Alur kerja YAML |
| **GitLab CI** | CI/CD bawaan | Platform tunggal untuk repo + pipeline |
| **Jenkins** | CI/CD yang dihosting sendiri | Sangat dapat dikonfigurasi; ekosistem plugin besar-besaran |
| **LingkaranCI** | Cloud CI/CD | Cepat; bagus untuk alur kerja dalam container |
| **ArgoCD** | GitOps untuk Kubernetes | Penerapan deklaratif berbasis Git |
---

## Docker dan Kontainer
### Mengapa Kontainer?
Sebelum container, masalah klasiknya adalah "ini berfungsi di mesin saya". Kontainer mengatasi masalah ini dengan mengemas aplikasi beserta semua dependensinya — pustaka, runtime, konfigurasi — ke dalam satu unit portabel yang berjalan secara identik di mana saja.
### Dasar-Dasar Docker
| Konsep | Deskripsi |
|---------|-------------|
| **Gambar** | Templat hanya-baca dengan aplikasi + dependensi |
| **Wadah** | Menjalankan contoh gambar |
| **File Docker** | Resep untuk membangun sebuah gambar |
| **Registrasi** | Penyimpanan gambar (Docker Hub, ECR, GCR) |
| **Volume** | Penyimpanan persisten yang bertahan saat kontainer dimulai ulang |
| **Jaringan** | Lapisan jaringan terisolasi untuk kontainer |
### Praktik Terbaik Dockerfile
```dockerfile
# Use specific base image tags, not 'latest'
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy dependency file first (leverage Docker layer caching)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Run as non-root user
USER appuser

# Expose port and define entrypoint
EXPOSE 8000
CMD ["python", "main.py"]
```

Praktik utama: menggunakan gambar dasar slim/alpine, dijalankan sebagai non-root, memanfaatkan cache lapisan, menggunakan`.dockerignore`, memindai gambar untuk mencari kerentanan (`trivy`,`docker scan`), dan menetapkan batas sumber daya.
### Penulisan Docker
Untuk menjalankan beberapa container secara bersamaan (aplikasi + database + cache):
```yaml
services:
  app:
    build: .
    ports: ["8000:8000"]
    depends_on: [db, redis]
    environment:
      DATABASE_URL: postgresql://user:pass@db:5432/mydb
  db:
    image: postgres:16
    volumes: [pgdata:/var/lib/postgresql/data]
  redis:
    image: redis:7-alpine
volumes:
  pgdata:
```

---

## Kubernetes (K8)
Kubernetes adalah orkestrator container berstandar industri. Ia mengelola penerapan, penskalaan, dan pengoperasian aplikasi dalam container.
### Arsitektur Inti
| Komponen | Peran |
|-----------|------|
| **Bidang Kendali** | Mengelola cluster (server API, penjadwal, dll, manajer pengontrol) |
| **Simpul** | Mesin pekerja (VM atau fisik) yang menjalankan container |
| **Pod** | Unit terkecil yang dapat digunakan; satu atau lebih kontainer yang berbagi jaringan |
| **Layanan** | Titik akhir jaringan stabil yang merutekan lalu lintas ke pod |
| **Penerapan** | Definisi deklaratif status pod yang diinginkan (replika, gambar, dll.) |
| **Masuk** | Aturan perutean HTTP untuk lalu lintas eksternal |
| **ConfigMap / Rahasia** | Konfigurasi dan data sensitif dimasukkan ke dalam pod |
### Perintah penting kubectl
```bash
kubectl get pods                    # List pods
kubectl get services                # List services
kubectl describe pod <name>         # Detailed pod info
kubectl logs <pod-name>             # View pod logs
kubectl exec -it <pod> -- /bin/sh   # Shell into a pod
kubectl apply -f deployment.yaml    # Apply a manifest
kubectl rollout status deploy/myapp # Check rollout progress
kubectl scale deploy/myapp --replicas=5  # Scale to 5 replicas
```

### Helm
Helm adalah manajer paket untuk Kubernetes. **Bagan** adalah kumpulan sumber daya Kubernetes yang telah dikonfigurasi sebelumnya. Anggap saja sebagai`apt`atau`brew`untuk K8.
```bash
helm install my-release bitnami/postgresql   # Install a chart
helm upgrade my-release bitnami/postgresql   # Upgrade
helm rollback my-release 1                   # Rollback to revision 1
helm list                                    # List releases
```

---

## Infrastruktur sebagai Kode (IaC)
IaC memperlakukan konfigurasi infrastruktur dengan cara yang sama seperti Anda memperlakukan kode aplikasi: dikontrol versi, diuji, dan diterapkan melalui pipeline.
### Terraform vs Kemungkinan
| Alat | Ketik | Pendekatan | Terbaik Untuk |
|------|------|----------|----------|
| **Terraform** | Penyediaan | Deklaratif (HCL); berbasis negara | Membuat sumber daya cloud (VPC, VM, database) |
| **Mungkin** | Konfigurasi | Deklaratif (YAML); tanpa agen | Konfigurasi server, instalasi perangkat lunak |
| **Pulumi** | Penyediaan | Imperatif (Python, Go, TS) | Tim yang lebih menyukai bahasa pemrograman nyata |
| **CloudFormation** | Penyediaan | Deklaratif (YAML/JSON); AWS-asli | Infrastruktur khusus AWS |
### Contoh Terraform
```hcl
provider "aws" {
  region = "us-east-1"
}

resource "aws_instance" "web" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t3.micro"

  tags = {
    Name = "web-server"
  }
}
```

Praktik terbaik: gunakan modul agar dapat digunakan kembali, simpan status dari jarak jauh (S3 + DynamoDB untuk penguncian), jangan pernah melakukan hardcode rahasia, dan mengontrol versi semuanya.
---

## Pemantauan dan Observabilitas
### Tiga Pilar
| Pilar | Apa yang Diberitahukannya kepada Anda | Alat |
|--------|------------------|-------|
| **Metrik** | Pengukuran numerik dari waktu ke waktu (CPU, tingkat permintaan, tingkat kesalahan) | Prometheus, CloudWatch, Datadog |
| **Log** | Peristiwa terpisah dengan konteks (kesalahan, permintaan, perubahan status) | ELK Stack, Loki, CloudWatch Logs |
| **Jejak** | Perjalanan permintaan ujung ke ujung di seluruh layanan | Jaeger, X-Ray, Zipkin |
### Prometheus + Tumpukan Grafana
Tumpukan pemantauan sumber terbuka standar:
| Komponen | Peran |
|-----------|------|
| **Prometheus** | Basis data deret waktu; mengambil metrik dari layanan |
| **Grafana** | Visualisasi dan dasbor |
| **Manajer Peringatan** | Merutekan peringatan ke Slack, PagerDuty, email |
| **Ekspor Node** | Mengekspos metrik tingkat sistem (CPU, RAM, disk) |
| **Eksportir Blackbox** | Titik akhir pemeriksaan (HTTP, TCP, ICMP) |
### Metrik Utama untuk Dilacak
| Kategori | Metrik |
|----------|---------|
| **Infrastruktur** | CPU, RAM, penggunaan disk, I/O jaringan |
| **Aplikasi** | Tingkat permintaan, latensi (p50, p95, p99), tingkat kesalahan |
| **Basis Data** | Jumlah kueri, kueri lambat, penggunaan kumpulan koneksi |
| **Bisnis** | Pendaftaran, konversi, pendapatan |
---

## Strategi Penerapan
| Strategi | Cara Kerja | Resiko | Kembalikan |
|----------|-------------|------|----------|
| **Pembaruan Bergulir** | Ganti instance lama dengan yang baru secara bertahap | Beberapa pengguna di versi lama, beberapa di versi baru | Kembali ke gambar sebelumnya |
| **Biru-Hijau** | Jalankan dua lingkungan yang identik; beralih lalu lintas | Biaya infrastruktur ganda selama transisi | Beralih kembali secara instan |
| **kenari** | Rutekan % kecil lalu lintas ke versi baru; meningkat secara bertahap | Manajemen lalu lintas yang kompleks | Rutekan lalu lintas kembali ke stabil |
| **Bendera Fitur** | Terapkan kode tetapi sembunyikan fitur di balik matikan | Kompleksitas kode dari logika kondisional | Matikan |
---

## GitOps
GitOps membawa IaC pada kesimpulan logisnya: repositori Git adalah satu-satunya sumber kebenaran untuk kondisi infrastruktur dan aplikasi yang Anda inginkan.
| Prinsip | Deskripsi |
|-----------|-------------|
| **Deklaratif** | Semuanya digambarkan sebagai kode (YAML, HCL) |
| **Berversi** | Git adalah sumber kebenaran |
| **Otomatis** | Alat terus-menerus merekonsiliasi keadaan yang diinginkan dengan keadaan sebenarnya |
| **Dapat diaudit** | Setiap perubahan adalah komitmen Git |
**ArgoCD** dan **Flux** adalah alat GitOps terkemuka untuk Kubernetes. Anda memasukkan perubahan ke repo Git Anda, dan alat tersebut secara otomatis menyebarkannya ke cluster.
---

## Respons Insiden
Ketika ada sesuatu yang rusak pada jam 3 pagi:
1. **Mengakui** peringatan tersebut.
2. **Menilai cakupan**: layanan, pengguna, dan data mana yang terpengaruh?
3. **Identifikasi** penyebab utama — periksa log, metrik, penerapan terkini.
4. **Berisi** jika memungkinkan — pemutus arus, tanda fitur, peralihan lalu lintas.
5. **Perbaikan** — memutar kembali atau menambal ke depan.
6. **Berkomunikasi** — memperbarui pemangku kepentingan dan pengguna (halaman status).
7. **Post-mortem** — dalam waktu 24–48 jam, dokumentasikan akar penyebab dan item tindakan.
Tujuannya bukan hanya untuk menyelesaikan insiden tersebut tetapi untuk memastikan kejadian yang sama tidak terulang kembali.