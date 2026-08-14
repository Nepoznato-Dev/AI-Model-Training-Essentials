---
# Metadata
title: "Terraform and Infrastructure as Code"
description: "IaC concepts, Terraform commands, state management, modules"
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
tags: [terraform, quick-reference]
difficulty_level: "beginner"
prerequisites: []
estimated_reading_time: "6 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# Terraform dan Infrastruktur sebagai Kode
Terraform adalah alat Infrastruktur sebagai Kode (IaC) yang paling banyak digunakan — alat ini memungkinkan Anda menentukan infrastruktur cloud (server, database, jaringan, izin) dalam file konfigurasi deklaratif yang dapat dibuat versinya, ditinjau, diuji, dan diotomatisasi. Daripada mengklik melalui konsol cloud, Anda menulis kode yang menjelaskan kondisi infrastruktur yang Anda inginkan, dan Terraform mengetahui perubahan apa yang harus dilakukan.
---

## Konsep Inti
| Konsep | Deskripsi |
|---------|-------------|
| **Penyedia** | Plugin yang mengelola platform cloud tertentu (AWS, Azure, GCP, dll.) |
| **Sumberdaya** | Objek infrastruktur (server, database, jaringan) |
| **Negara** | Catatan Terraform tentang infrastruktur yang ada; disimpan dalam file negara |
| **Rencana** | Pratinjau perubahan apa yang akan dilakukan Terraform |
| **Terapkan** | Jalankan rencananya; membuat/memperbarui/menghancurkan infrastruktur |
| **Modul** | Koleksi sumber daya yang dapat digunakan kembali |
| **Variabel** | Parameter masukan untuk konfigurasi |
| **Keluaran** | Nilai yang diekspor dari modul atau konfigurasi |
| **Sumber data** | Baca informasi dari infrastruktur yang ada |
---

## Alur Kerja Dasar
| Langkah | Perintah | Deskripsi |
|------|---------|-------------|
| **1. Tulis konfigurasi** | Buat file`.tf`| Tentukan penyedia, sumber daya, variabel |
| **2. Inisialisasi** | `terraform init`| Penyedia unduhan; menyiapkan backend |
| **3. Format** | `terraform fmt`| Standarisasi pemformatan |
| **4. Validasi** | `terraform validate`| Periksa sintaks dan konfigurasi |
| **5. Rencana** | `terraform plan`| Pratinjau perubahan (uji coba) |
| **6. Terapkan** | `terraform apply`| Membuat atau memperbarui infrastruktur |
| **7. Hancurkan** | `terraform destroy`| Hancurkan semua infrastruktur yang dikelola |
---

## Perintah Umum
| Perintah | Deskripsi |
|---------|-------------|
| `terraform init`| Inisialisasi direktori kerja; unduh penyedia dan modul |
| `terraform plan`| Tunjukkan perubahan apa saja yang akan dilakukan |
| `terraform apply`| Terapkan perubahan; tambahkan`-auto-approve`untuk melewati konfirmasi |
| `terraform destroy`| Hancurkan semua sumber daya yang dikelola |
| `terraform fmt`| Format file konfigurasi ke gaya standar |
| `terraform validate`| Validasi sintaks konfigurasi |
| `terraform output`| Tampilkan nilai keluaran |
| `terraform state list`| Daftar semua sumber daya di negara bagian |
| `terraform state show <resource>`| Tampilkan detail sumber daya tertentu |
| `terraform import <resource> <id>`| Impor infrastruktur yang ada ke negara bagian |
| `terraform taint <resource>`| Tandai sumber daya untuk rekreasi pada lamaran berikutnya |
| `terraform refresh`| Perbarui status agar sesuai dengan infrastruktur nyata |
| `terraform graph`| Hasilkan grafik ketergantungan visual (format DOT) |
| `terraform console`| Konsol interaktif untuk menguji ekspresi |
---

## Manajemen Negara
| Praktik Terbaik | Deskripsi |
|--------------|-------------|
| **Negara terpencil** | Simpan status di S3, GCS, Azure Blob, atau Terraform Cloud — tidak pernah secara lokal |
| **Penguncian status** | Gunakan DynamoDB (backend S3) atau penguncian asli untuk mencegah modifikasi bersamaan |
| **Enkripsi negara** | Aktifkan enkripsi saat istirahat untuk file negara (berisi data sensitif) |
| **Pemisahan negara** | Gunakan file status terpisah untuk lingkungan atau tim berbeda |
| **Cadangan negara** | Backend jarak jauh secara otomatis menyatakan versi; tetap aktifkan ini |
| **Jangan pernah mengedit status secara manual** | Gunakan`terraform state mv`,`rm`,`import`sebagai gantinya |
---

## Struktur Modul
```
module/
├── main.tf          # Primary resources
├── variables.tf     # Input variables
├── outputs.tf       # Output values
├── versions.tf      # Provider and Terraform version constraints
├── README.md        # Documentation
└── examples/        # Example usage
    └── basic/
        └── main.tf
```

---

## Jenis Variabel
| Ketik | Contoh | Kasus Penggunaan |
|------|---------|----------|
| **string** | `variable "region" { type = string }`| Nilai teks tunggal |
| **nomor** | `variable "count" { type = number }`| Nilai numerik |
| **bodoh** | `variable "enable" { type = bool }`| Bendera benar/salah |
| **daftar** | `variable "zones" { type = list(string) }`| Koleksi yang dipesan |
| **peta** | `variable "tags" { type = map(string) }`| Pasangan nilai kunci |
| **objek** | `variable "config" { type = object({...}) }`| Konfigurasi terstruktur |
---

## Pola Umum
| Pola | Deskripsi |
|---------|-------------|
| **Hitung** | `count = 3`membuat beberapa contoh sumber daya |
| **Untuk setiap** | `for_each = var.items`melakukan iterasi pada peta atau kumpulan |
| **Blok dinamis** | Hasilkan blok bersarang yang berulang (misalnya, aturan ingress) |
| **Nilai lokal** | `locals { ... }`untuk nilai yang dihitung dan mengurangi pengulangan |
| **Sumber data** | Baca infrastruktur yang ada (misalnya, temukan VPC yang ada) |
| **Penyedia** | Jalankan skrip pada sumber daya setelah pembuatan (gunakan dengan hemat) |
| **Ruang Kerja** | Pisahkan status untuk lingkungan berbeda dalam konfigurasi yang sama |
---

## Pemecahan masalah
| Masalah | Solusi |
|---------|----------|
| **Penyimpangan status** | Jalankan`terraform plan`untuk melihat perbedaannya; `terraform apply`untuk merekonsiliasi |
| **Keadaan terkunci** | Periksa siapa yang memiliki kuncinya; gunakan`terraform force-unlock`jika aman |
| **Kesalahan penyedia** | Periksa kredensial; perbarui versi penyedia; periksa batas API |
| **Impor konflik** | Sumber daya sudah ada di negara bagian; gunakan`terraform state rm`dulu |
| **Ketergantungan melingkar** | Merestrukturisasi sumber daya; gunakan`depends_on`dengan hati-hati |
| **Negara bagian besar** | Dibagi menjadi beberapa modul; gunakan`-target`untuk operasi parsial |
---

## Ringkasan
Terraform mengelola infrastruktur melalui file konfigurasi deklaratif. Alur kerjanya adalah: tulis konfigurasi → init → rencana → terapkan. Negara melacak apa yang ada dan harus disimpan jarak jauh dengan penguncian. Modul memungkinkan penggunaan kembali. Variabel membuat parameter konfigurasi. Prinsip utamanya adalah: memperlakukan infrastruktur sebagai kode (kontrol versi; tinjauan; pengujian); jangan pernah mengedit status secara manual; rencanakan sebelum melamar; gunakan keadaan jarak jauh dengan penguncian; dan konfigurasi struktur dengan modul untuk pemeliharaan.