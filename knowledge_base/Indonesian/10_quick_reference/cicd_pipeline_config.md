---
# Metadata
title: "CI/CD Pipeline Configuration"
description: "GitHub Actions, GitLab CI, Jenkins, pipeline YAML patterns"
category: "Quick Reference"
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
reviewed_by: "Quick Reference Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [cicd, pipeline, config, quick-reference]
difficulty_level: "beginner"
prerequisites: []
estimated_reading_time: "9 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# Konfigurasi Saluran CI/CD
Pipeline Continuous Integration (CI) dan Continuous Deployment (CD) mengotomatiskan proses pembuatan, pengujian, dan penerapan perangkat lunak. Referensi ini mencakup pola konfigurasi untuk platform CI/CD paling populer: GitHub Actions, GitLab CI, dan prinsip desain pipeline umum.
---

## Tindakan GitHub
### Struktur Alur Kerja
```yaml
name: CI Pipeline
on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Set up language
        uses: actions/setup-python@v5
        with:
          python-version: '3.12'
      - name: Install dependencies
        run: pip install -r requirements.txt
      - name: Run tests
        run: pytest
      - name: Build
        run: python setup.py build
```

### Pemicu Umum
| Pemicu | Deskripsi |
|---------|-------------|
| `on: push`| Pada setiap dorongan |
| `on: pull_request`| Pada PR buka, perbarui, buka kembali |
| `on: schedule`| Jadwal berbasis cron |
| `on: workflow_dispatch`| Pemicu manual |
| `on: release`| Pada pembuatan rilis |
| `on: workflow_call`| Dipanggil oleh alur kerja lain (dapat digunakan kembali) |
### Fitur Utama
| Fitur | Deskripsi |
|---------|-------------|
| **Strategi matriks** | Jalankan pekerjaan yang sama dengan konfigurasi berbeda |
| **Rahasia** | Variabel lingkungan terenkripsi (`${{ secrets.MY_SECRET }}`) |
| **Lingkungan** | Target penerapan dengan aturan perlindungan |
| **Caching** | Ketergantungan cache antar proses |
| **Artefak** | Unggah file dari pekerjaan (laporan pengujian, build) |
| **Alur kerja yang dapat digunakan kembali** | Bagikan logika alur kerja di seluruh repositori |
| **Tindakan gabungan** | Gabungkan beberapa langkah menjadi satu tindakan |
### Strategi Matriks
```yaml
jobs:
  test:
    strategy:
      matrix:
        python-version: ['3.10', '3.11', '3.12']
        os: [ubuntu-latest, macos-latest]
    runs-on: ${{ matrix.os }}
    steps:
      - uses: actions/setup-python@v5
        with:
          python-version: ${{ matrix.python-version }}
```

---

## GitLab CI
### Struktur Saluran Pipa
```yaml
stages:
  - build
  - test
  - deploy

build:
  stage: build
  script:
    - docker build -t myapp:$CI_COMMIT_SHA .
    - docker push myapp:$CI_COMMIT_SHA

test:
  stage: test
  script:
    - docker run myapp:$CI_COMMIT_SHA pytest

deploy:
  stage: deploy
  script:
    - deploy.sh $CI_COMMIT_SHA
  only:
    - main
  when: manual
```

### Kata Kunci Utama
| Kata kunci | Deskripsi |
|---------|-------------|
| `stages`| Tentukan tahapan saluran pipa dan urutannya |
| `stage`| Tetapkan pekerjaan ke suatu tahapan |
| `script`| Perintah untuk dijalankan |
| `before_script`| Perintah dijalankan sebelum skrip utama |
| `after_script`| Perintah dijalankan setelah skrip utama (bahkan jika gagal) |
| `only / except`| Kontrol kapan pekerjaan dijalankan (cabang, tag) |
| `rules`| Versi yang lebih fleksibel hanya/kecuali |
| `variables`| Tentukan variabel CI/CD |
| `cache`| File cache antar alur dijalankan |
| `artifacts`| File yang akan diteruskan antar pekerjaan |
| `environment`| Lingkungan penerapan |
| `when`| Kontrol eksekusi pekerjaan (on_success, on_failure, manual, selalu) |
| `needs`| Tentukan dependensi pekerjaan (mode DAG) |
| `extends`| Mewarisi konfigurasi dari pekerjaan lain |
| `include`| Impor file YAML eksternal |
### Variabel Standar
| Variabel | Deskripsi |
|----------|-------------|
| `$CI_COMMIT_SHA`| Hash komit saat ini |
| `$CI_COMMIT_REF_NAME`| Nama cabang atau tag |
| `$CI_PIPELINE_ID`| ID Saluran Pipa |
| `$CI_JOB_ID`| ID Pekerjaan |
| `$CI_PROJECT_DIR`| Jalur lengkap menuju proyek |
| `$CI_REGISTRY`| URL registri kontainer |
| `$CI_DEFAULT_BRANCH`| Nama cabang default |
---

## Pola Desain Saluran Pipa
### Pola Umum
| Pola | Deskripsi |
|---------|-------------|
| **Bangun sekali, terapkan banyak** | Bangun artefak sekali; menyebarkan artefak yang sama ke setiap lingkungan |
| **Pemeriksaan gerbang** | Persetujuan manual sebelum penerapan produksi |
| **Bendera fitur** | Terapkan ke produksi tetapi bersembunyi di balik tanda fitur |
| **Penyebaran Canary** | Tersebar ke persentase kecil; memantau; meluncurkan |
| **Penyebaran biru-hijau** | Dua lingkungan yang identik; beralih lalu lintas |
| **Pengujian paralel** | Jalankan rangkaian pengujian secara paralel untuk mengurangi waktu pipeline |
| **Serat dulu** | Jalankan linter sebelum pengujian yang mahal; gagal cepat |
| **Ketergantungan cache** | Cache node_modules, pip, Maven untuk mempercepat pembangunan |
### Tahapan Saluran Pipa (Khas)
| Tahap | Tujuan |
|-------|---------|
| **Serat** | Gaya kode dan analisis statis |
| **Bangun** | Menyusun; bundel; membuat artefak |
| **Uji satuan** | Tes cepat; tidak ada ketergantungan eksternal |
| **Uji integrasi** | Tes dengan database; Lebah; layanan eksternal |
| **Pemindaian keamanan** | Kerentanan ketergantungan; pemindaian rahasia; SAST |
| **Paket** | Buat gambar Docker; membangun artefak rilis |
| **Menerapkan pementasan** | Terapkan ke lingkungan pementasan |
| **Tes E2E** | Tes sistem penuh terhadap pementasan |
| **Menerapkan produksi** | Penerapan ke produksi (manual atau otomatis) |
| **Tes asap** | Verifikasi penerapan yang sehat |
---

## Strategi Caching
| Bahasa / Alat | Jalur Tembolok | Contoh |
|----------------|-----------|---------|
| **Python (pip)** | `~/.cache/pip`| `actions/cache`dengan kunci dari hash`requirements.txt`|
| **Node.js (npm)** | `~/.npm`| `actions/setup-node`dengan cache bawaan |
| **Jawa (Maven)** | `~/.m2/repository`| Cache dengan kunci dari hash`pom.xml`|
| **Java (Kelas)** | `~/.gradle/caches`| Cache dengan kunci dari hash`build.gradle`|
| **Pergi** | `~/go/pkg/mod`| Cache dengan kunci dari hash`go.sum`|
| **Karat (Kargo)** | `~/.cargo/registry`| Cache dengan kunci dari hash`Cargo.lock`|
| **Buruh pelabuhan** | Caching lapisan Docker | `docker/build-push-action`dengan cache-dari |
---

## Pemecahan masalah
| Masalah | Solusi |
|---------|----------|
| **Pipa lambat** | Ketergantungan cache; memparalelkan pekerjaan; gunakan gambar dasar yang lebih kecil |
| **Rahasia tidak tersedia** | Periksa nama rahasia; memverifikasi ruang lingkup lingkungan; periksa batasan PR garpu |
| **Artefak terlalu besar** | Kecualikan file yang tidak diperlukan; kompres; gunakan retensi yang lebih pendek |
| **Matriks terlalu besar** | Kurangi kombinasi; gunakan`include`/`exclude`|
| **Tes tidak stabil** | Tes tidak stabil karantina; memperbaiki akar permasalahan; coba lagi dengan`retry:`|
| **Izin ditolak** | Periksa cakupan token; verifikasi izin pelari |
---

## Ringkasan
Pipeline CI/CD mengotomatiskan pembuatan, pengujian, dan penerapan perangkat lunak. GitHub Actions menggunakan alur kerja YAML yang dipicu oleh peristiwa repositori; GitLab CI menggunakan tahapan dan pekerjaan dengan aturan yang fleksibel. Pola utamanya meliputi: membangun sekali menyebarkan banyak; pemeriksaan gerbang sebelum produksi; serat terlebih dahulu untuk umpan balik yang cepat; ketergantungan cache untuk mempercepat pembangunan; dan memparalelkan tes. Tahapan pipeline biasanya berlangsung dari lint → build → test → security → package → deploy → smoke test. Strategi caching bervariasi berdasarkan bahasa tetapi mengikuti prinsip yang sama: direktori ketergantungan cache dikunci oleh hash file kunci. Sasarannya adalah umpan balik yang cepat dan andal pada setiap perubahan serta penerapan yang aman dan berulang pada produksi.