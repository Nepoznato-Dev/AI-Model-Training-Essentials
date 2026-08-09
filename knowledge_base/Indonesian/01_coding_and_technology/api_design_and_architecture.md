---
# Metadata
title: "API Design and Architecture"
description: "REST, GraphQL, gRPC, versioning, auth, API gateways"
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
tags: [api, design, architecture, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "10 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# Desain dan Arsitektur API
API (Application Programming Interface) adalah bagaimana komponen perangkat lunak berkomunikasi satu sama lain. API yang dirancang dengan baik bersifat intuitif, konsisten, dan menyenangkan untuk digunakan. Desain yang buruk menyebabkan kebingungan, bug, dan frustrasi. File ini mencakup prinsip, pola, dan praktik pembuatan API yang sebenarnya ingin digunakan oleh pengembang.
---

## Prinsip REST API
REST (Representational State Transfer) adalah gaya arsitektur dominan untuk API web. Ia memperlakukan data sebagai **sumber daya** yang diidentifikasi oleh URL, dan menggunakan metode HTTP untuk mengoperasikannya.
### Prinsip Inti
| Prinsip | Deskripsi |
|-----------|-------------|
| **Sumber Daya** | Semuanya adalah sumber daya dengan URI (`/users/123`,`/orders/456`) |
| **Metode HTTP** | GET (baca), POST (buat), PUT (ganti), PATCH (pembaruan sebagian), DELETE (hapus) |
| **Tanpa kewarganegaraan** | Setiap permintaan berisi semua informasi yang dibutuhkan; tidak ada status sesi sisi server |
| **Antarmuka Seragam** | Penamaan sumber daya yang konsisten, metode standar, kode status standar |
| **Representasi** | Sumber daya dapat direpresentasikan dalam berbagai format (JSON, XML) |
### Konvensi Penamaan Sumber Daya
| Lakukan | Jangan |
|----|-------|
| `/users`(kata benda jamak) | `/user`(tunggal) |
| `/users/123/orders`(bersarang) | `/getOrdersForUser?id=123`|
| `/products?category=electronics`(param kueri untuk pemfilteran) | `/productsByCategory/electronics`|
| Gunakan tanda hubung:`/user-profiles`| Gunakan garis bawah:`/user_profiles`|
### Metode HTTP dan Idempotensi
| Metode | Tujuan | Idempoten? | Aman? |
|--------|---------|-------------|-------|
| **DAPATKAN** | Baca sumber daya | ✅ Ya | ✅ Ya |
| **POSTING** | Buat sumber daya | ❌ Tidak | ❌ Tidak |
| **MASUKKAN** | Ganti seluruh sumber daya | ✅ Ya | ❌ Tidak |
| **tambalan** | Perbarui sebagian sumber daya | ❌ Tidak* | ❌ Tidak |
| **HAPUS** | Hapus sumber daya | ✅ Ya | ❌ Tidak |
*PATCH dapat dibuat idempoten dengan desain yang cermat.
### Kode Status HTTP
| Kode | Arti | Kapan Menggunakan |
|------|---------|-------------|
| **200** | oke | Berhasil GET, PUT, PATCH, DELETE |
| **201** | Dibuat | POST Berhasil (sumber daya dibuat) |
| **204** | Tidak Ada Konten | HAPUS Berhasil (tidak ada yang dikembalikan) |
| **400** | Permintaan Buruk | Masukan tidak valid atau permintaan salah |
| **401** | Tidak sah | Otentikasi hilang atau tidak valid |
| **403** | Dilarang | Diautentikasi tetapi tidak diotorisasi |
| **404** | Tidak Ditemukan | Sumber daya tidak ada |
| **409** | Konflik | Sumber daya duplikat atau konflik negara |
| **422** | Entitas yang Tidak Dapat Diproses | JSON valid tetapi kesalahan semantik |
| **429** | Terlalu Banyak Permintaan | Batas tarif terlampaui |
| **500** | Kesalahan Server Internal | Kesalahan server tak terduga |
| **502** | Gerbang Buruk | Kegagalan layanan hulu |
| **503** | Layanan Tidak Tersedia | Kelebihan beban atau pemeliharaan sementara |
---

## Versi API
API berkembang. Saat Anda perlu membuat perubahan yang dapat menyebabkan gangguan, pembuatan versi memungkinkan klien yang ada tetap bekerja.
| Strategi | Contoh | Kelebihan | Kontra |
|----------|---------|------|------|
| **Jalur URL** | `/v1/users`,`/v2/users`| Sederhana, eksplisit | Perubahan URL per versi |
| **Parameter kueri** | `/users?version=2`| Fleksibel | Mudah untuk dilupakan |
| **Tajuk** | `Accept: application/vnd.myapi.v2+json`| Bersihkan URL | Kurang dapat ditemukan |
| **Tidak ada versi** | Hanya evolusi skema | paling sederhana | Perubahan besar mempengaruhi semua orang |
**Praktik terbaik**: gunakan pembuatan versi jalur URL (`/v1/`) untuk kejelasan. Mendukung setidaknya satu versi sebelumnya. Hentikan versi lama dengan garis waktu yang jelas.
---

## Metode Otentikasi
| Metode | Cara Kerja | Terbaik Untuk |
|--------|-------------|----------|
| **Kunci API** | Kunci rahasia di header (`X-API-Key: abc123`) | Integrasi sederhana server-ke-server |
| **OAuth2** | Delegasi berbasis token dengan cakupan | Akses pihak ketiga, aplikasi resmi pengguna |
| **JWT** | Token mandiri dengan klaim | Otentikasi tanpa kewarganegaraan di seluruh layanan |
| **Otentikasi Dasar** | Nama pengguna yang dikodekan Base64: kata sandi | Hanya pengembangan — tidak pernah produksi tanpa TLS |
| **Cookie sesi** | ID sesi sisi server dalam cookie khusus HTTP | Aplikasi web tradisional |
### Alur OAuth2 (Sederhana)
1. Klien mengarahkan pengguna ke server otorisasi.
2. Pengguna masuk dan memberikan izin.
3. Server otorisasi mengembalikan kode otorisasi.
4. Klien menukarkan kode untuk token akses (dan secara opsional menyegarkan token).
5. Klien menggunakan token akses untuk memanggil API.
6. Ketika token akses habis masa berlakunya, gunakan token penyegaran untuk mendapatkan yang baru.
---

## Gaya API: REST vs GraphQL vs gRPC
| Fitur | Istirahat | GrafikQL | gRPC |
|---------|------|---------|------|
| **Format Data** | JSON (biasanya) | JSON | Protobuf (biner) |
| **Titik Akhir** | Banyak (satu per sumber daya) | Titik akhir tunggal | Didefinisikan oleh file .proto |
| **Pengambilan berlebihan** | Umum (mendapatkan lebih dari yang dibutuhkan) | Tidak ada (klien menentukan kolom) | Tidak ada (ditentukan skema) |
| **Kurang diambil** | Membutuhkan banyak panggilan | Tidak ada (dapatkan apa yang dibutuhkan) | Tidak ada |
| **Waktu Nyata** | Diperlukan WebSocket | Langganan bawaan | Streaming bawaan |
| **Caching** | Caching HTTP bekerja secara alami | Lebih sulit untuk di-cache | Terbatas |
| **Kurva Pembelajaran** | Rendah | Sedang | Sedang–Tinggi |
| **Terbaik Untuk** | API Publik, aplikasi CRUD | UI yang kompleks, aplikasi seluler | Layanan mikro internal, berkinerja tinggi |
---

## Paginasi, Pemfilteran, dan Penyortiran
Untuk titik akhir yang mengembalikan daftar:
| Teknik | Contoh | Kapan Menggunakan |
|-----------|---------|-------------|
| **Offset/Batas** | `?offset=20&limit=10`| Sederhana; berfungsi untuk kumpulan data kecil |
| **Berbasis kursor** | `?cursor=abc123&limit=10`| Kumpulan data besar; hasil yang konsisten |
| **Keset Kunci** | `?created_after=2024-01-01&limit=10`| Sangat efisien; membutuhkan kunci unik |
```json
// Cursor-based response
{
  "data": [...],
  "pagination": {
    "next_cursor": "abc123",
    "has_more": true
  }
}
```

---

## Pembatasan Nilai
Lindungi API Anda dari penyalahgunaan dan pastikan penggunaan wajar.
| Strategi | Cara Kerja |
|----------|-------------|
| **Jendela diperbaiki** | N permintaan per jangka waktu (mis., 100/jam) |
| **Jendela geser** | Lebih terperinci; menghitung permintaan di jendela bergulir |
| **Ember token** | Token ditambahkan dengan tarif tetap; setiap permintaan menggunakan token |
Kembalikan`429 Too Many Requests`dengan header:```
X-RateLimit-Limit: 100
X-RateLimit-Remaining: 0
X-RateLimit-Reset: 1625097600
Retry-After: 60
```

---

## Penanganan Kesalahan
Respons kesalahan yang konsisten membuat API lebih mudah digunakan:
```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Invalid input data",
    "details": [
      {
        "field": "email",
        "issue": "Invalid email format"
      }
    ]
  }
}
```

**Prinsip**: gunakan struktur kesalahan yang konsisten, sertakan pesan yang dapat ditindaklanjuti, gunakan kode status HTTP standar, catat kesalahan di sisi server dengan ID korelasi, dan jangan pernah mengekspos jejak tumpukan atau detail internal.
---

## Dokumentasi API
| Alat | Deskripsi |
|------|-------------|
| **OpenAPI (Keangkuhan)** | Standar industri untuk dokumentasi REST API |
| **UI Keangkuhan** | Dokumentasi API interaktif dari spesifikasi OpenAPI |
| **Tukang Pos** | Pengujian API, dokumentasi, dan berbagi koleksi |
| **Doktasi Ulang** | Dokumen referensi API yang indah dari spesifikasi OpenAPI |
| **Taman Bermain GraphQL / GraphiQL** | Eksplorasi GraphQL Interaktif |
**Praktik terbaik**: tulis spesifikasi OpenAPI terlebih dahulu (pengembangan berbasis spesifikasi), lalu buat dokumentasi dan SDK klien darinya.
---

## Pola Gerbang API
Gerbang API berada di antara klien dan layanan backend, menyediakan satu titik masuk.
| Tanggung jawab | Deskripsi |
|---------------|-------------|
| **Perutean** | Permintaan langsung ke layanan backend yang sesuai |
| **Otentikasi** | Validasi token di tingkat gateway |
| **Pembatasan Tarif** | Terapkan batasan global atau per klien |
| **Transformasi** | Konversi antar protokol (REST ↔ gRPC) |
| **Caching** | Tembolok tanggapan umum |
| **Pemantauan** | Pencatatan log dan metrik terpusat |
| **Penyeimbangan Beban** | Mendistribusikan lalu lintas di seluruh contoh layanan |
| Alat | Ketik |
|------|------|
| **Kong** | Gerbang API sumber terbuka (berbasis Nginx) |
| **Gerbang API AWS** | Dikelola sepenuhnya, terintegrasi dengan AWS |
| **Manajemen API Azure** | Gerbang terkelola dengan portal pengembang |
| **Utusan / Istio** | Jala layanan dengan kemampuan gateway API |
| **Traefik** | Penemuan otomatis, Mari Enkripsi integrasi |
---

## Webhook
Webhook memungkinkan API Anda mengirimkan peristiwa ke klien secara real-time, alih-alih membuat klien melakukan polling untuk mengetahui perubahan.
| Aspek | Praktik Terbaik |
|--------|--------------|
| **Pengiriman** | Permintaan POST dengan payload JSON ke URL klien |
| **Keamanan** | Menandatangani muatan dengan HMAC; klien memverifikasi tanda tangan |
| **Keandalan** | Coba lagi pengiriman yang gagal dengan backoff eksponensial |
| **Idempotensi** | Sertakan ID acara unik; klien menangani duplikat |
| **Versi** | Sertakan versi API dalam payload webhook |
---

## Daftar Periksa Desain
- [ ] Sumber daya adalah kata benda jamak (`/users`, bukan`/getUser`)
- [ ] Metode HTTP digunakan dengan benar (GET untuk membaca, POST untuk membuat, dll.)
- [ ] Format respons kesalahan yang konsisten
- [ ] Paginasi untuk semua titik akhir daftar
- [ ] Pembatasan nilai dengan header yang jelas
- [ ] Strategi pembuatan versi API ditentukan
- [ ] Otentikasi dan otorisasi sudah ada
- [ ] Masukkan validasi pada semua titik akhir
- [ ] Dokumentasi OpenAPI/Swagger dipertahankan
- [ ] CORS dikonfigurasi dengan benar
- [ ] HTTPS diterapkan dalam produksi
- [ ] Kunci idempotensi untuk operasi POST jika diperlukan