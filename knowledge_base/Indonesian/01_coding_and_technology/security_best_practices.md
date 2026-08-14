---
# Metadata
title: "Security Best Practices"
description: "OWASP Top 10, input validation, auth, secrets management"
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
tags: [security, best, practices, coding-and-technology]
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
# Praktik Terbaik Keamanan
Panduan praktis untuk mengamankan aplikasi, infrastruktur, dan data — mulai dari pengembangan hingga produksi.
---

## OWASP 10 Teratas (2021) — Ikhtisar
1. **Kontrol Akses Rusak**: Pengguna dapat mengakses sumber daya yang tidak seharusnya.
2. **Kegagalan Kriptografi**: Enkripsi lemah atau hilang.
3. **Injeksi**: SQL, NoSQL, perintah OS, atau injeksi LDAP.
4. **Desain Tidak Aman**: Cacat arsitektur.
5. **Kesalahan Konfigurasi Keamanan**: Kata sandi default, port terbuka, kesalahan verbose.
6. **Komponen Rentan dan Kedaluwarsa**: CVE yang diketahui berada dalam ketergantungan.
7. **Kegagalan Identifikasi dan Otentikasi**: Kata sandi lemah, salah urus sesi.
8. **Kegagalan Integritas Perangkat Lunak dan Data**: Serangan rantai pasokan, pembaruan yang tidak ditandatangani.
9. **Kegagalan Pencatatan dan Pemantauan Keamanan**: Tidak ada deteksi pelanggaran.
10. **Pemalsuan Permintaan Sisi Server (SSRF)**: Penyalahgunaan server untuk membuat permintaan ke sistem internal.
---

## Validasi Masukan dan Pengkodean Keluaran
### Aturan Validasi
- **Daftar Putih > Daftar Hitam**: Menentukan pola yang diizinkan (misalnya, regex untuk email) daripada memblokir pola buruk yang diketahui.
- **Batas panjang**: Menerapkan panjang maksimum untuk mencegah buffer overflow dan DoS.
- **Pemeriksaan jenis**: Pastikan bilangan bulat adalah bilangan bulat, boolean adalah boolean.
- **Gunakan pustaka yang telah teruji**: Untuk validasi email, URL, dan tanggal, gunakan pustaka standar (misalnya,`email-validator`di Python,`validator.js`di Node).
### Pengkodean Keluaran
- **Pengkodean HTML**: Enkode`<`,`>`,`&`,`"`,`'`untuk mencegah XSS.
- **Parameterisasi SQL**: Jangan pernah menggabungkan input pengguna ke dalam kueri SQL. Gunakan kueri berparameter (pernyataan yang disiapkan) atau ORM.
- **Shell escape**: Hindari membuat perintah shell dari input pengguna; jika tidak dapat dihindari, gunakan`shlex.quote()`atau serupa.
---

## Otentikasi dan Otorisasi
### Manajemen Kata Sandi
- **Hashing**: Menyimpan kata sandi dengan algoritma hashing yang kuat dan lambat: **Argon2id** (lebih disukai), **bcrypt**, **scrypt**, atau **PBKDF2**.
- **Salting**: Tambahkan garam unik per pengguna.
- **Panjang minimum**: Terapkan setidaknya 12–16 karakter.
- **MFA (Otentikasi Multi-Faktor)**: Memerlukan faktor kedua (TOTP, SMS, kunci perangkat keras) untuk operasi sensitif.
- **Pembatasan kecepatan**: Mencegah upaya brute force pada titik akhir login (misalnya, 5 upaya per 5 menit per IP/pengguna).
### Manajemen Sesi
- Gunakan cookie SameSite yang aman, khusus HTTP, untuk token sesi.
- Tetapkan waktu kedaluwarsa yang sesuai.
- Membatalkan sesi saat logout dan perubahan kata sandi.
- Hindari mengekspos ID sesi di URL.
### OAuth2 / OIDC
- Gunakan perpustakaan yang sudah mapan (misalnya, Authlib, PyJWT, Passport.js, Spring Security).
- Validasi token ID secara menyeluruh (tanda tangan, penerbit, audiens, kedaluwarsa).
- Gunakan parameter status untuk mencegah CSRF.
- Jaga kerahasiaan rahasia klien.
### JWT (Token Web JSON)
- **Tanda**: Gunakan RS256 atau ES256 (asimetris) untuk keamanan yang lebih baik; HS256 (simetris) dapat diterima jika rahasia bersama dikelola dengan baik.
- **Validasi**: Selalu verifikasi tanda tangan, penerbit (`iss`), audiens (`aud`), dan kedaluwarsa (`exp`).
- **Jaga masa berlakunya tetap pendek**: 15–60 menit untuk token akses; gunakan token penyegaran untuk sesi yang lebih lama.
- **Simpan dengan aman**: Jangan pernah menyimpan JWT di Penyimpanan lokal (rentan terhadap XSS); gunakan cookie khusus HTTP saja.
---

## Keamanan API
### Otentikasi
- Selalu autentikasi panggilan API (kecuali titik akhir publik).
- Lebih memilih kunci API atau token OAuth2 daripada autentikasi dasar (yang mengirimkan kredensial pada setiap permintaan).
### Pembatasan dan Pembatasan Tarif
- Terapkan batas kecepatan per pengguna dan per IP untuk mencegah penyalahgunaan dan DoS.
- Kembalikan`429 Too Many Requests`dengan header `Retry-After`.
### CORS (Berbagi Sumber Daya Lintas Asal)
- Izinkan hanya asal tertentu (jangan pernah`*`dalam produksi).
- Validasi header`Origin`di sisi server.
### Validasi Masukan
- Validasi semua parameter permintaan, termasuk header dan isi.
- Tolak bidang yang tidak terduga (`"strict": true`atau`additionalProperties: false`dalam Skema JSON).
### HTTPS/TLS
- Terapkan HTTPS dalam produksi.
- Gunakan HSTS (HTTP Strict Transport Security) untuk memaksa browser menggunakan HTTPS.
- Gunakan TLS 1.2 atau 1.3 (nonaktifkan TLS 1.0/1.1).
---

## Manajemen Rahasia
### Jangan Pernah Rahasia Hardcode
- Jangan memasukkan rahasia (kunci API, kata sandi, URL basis data) ke kontrol sumber.
- Gunakan variabel lingkungan atau alat manajemen rahasia.
### Peralatan
| Alat | Deskripsi |
|------|-------------|
| ** Gudang HashiCorp ** | Rahasia dinamis tingkat perusahaan |
| **Manajer Rahasia AWS/Azure Key Vault/Manajer Rahasia GCP** | Cloud-asli |
| **SOP** | Enkripsi rahasia dalam file dan komit (dengan KMS atau GPG) |
| **Rahasia buruh pelabuhan** | Untuk mode Kawanan; Rahasia Kubernetes (pertimbangkan driver CSI Secrets Store eksternal) |
### Rotasi
- Rotasi rahasia dan akun layanan secara teratur.
- Otomatiskan rotasi jika memungkinkan.
---

## Manajemen Ketergantungan
### Pemindaian Kerentanan
| Bahasa/Platform | Alat |
|-------------------|-------|
| **Piton** | `safety`,`pip-audit`,`bandit`|
| **Simpul** | `npm audit`,`yarn audit`,`snyk`|
| **Karat** | `cargo audit`|
| **Pergi** | `govulncheck`|
| **Umum** | `Dependabot`(GitHub),`Renovate`,`Trivy`|
### Menambal
- Terus perbarui dependensi ke versi yang ditambal.
- Mengatur permintaan penarikan otomatis untuk pembaruan kecil/tambalan.
- Tinjau log perubahan untuk mengetahui perubahan yang dapat terjadi.
### Integritas Rantai Pasokan
- Gunakan file kunci paket (`package-lock.json`,`Cargo.lock`,`go.sum`) untuk memastikan build yang dapat direproduksi.
- Verifikasi checksum dari dependensi yang diunduh.
- Lebih memilih pendaftar resmi dan hanya mempercayai penerbit terverifikasi.
---

## Keamanan Infrastruktur
### Firewall
- Blokir semua port masuk kecuali yang diperlukan secara eksplisit (mis., 80, 443).
- Batasi akses SSH pada rentang IP tertentu (atau gunakan VPN/bastion host).
- Gunakan grup keamanan (AWS) atau NSG (Azure) untuk kontrol yang lebih detail.
### Pengerasan OS
- Terapkan pembaruan keamanan secara berkala (`sudo apt upgrade`,`yum update`).
- Nonaktifkan layanan yang tidak perlu dan akun default.
- Gunakan fail2ban untuk memblokir upaya brute force pada SSH.
- Perkuat SSH: nonaktifkan login root, gunakan autentikasi berbasis kunci, ubah port default (opsional).
### Segmentasi Jaringan
- Tempatkan database dan cache di subnet pribadi tanpa akses internet.
- Gunakan DMZ untuk layanan publik.
- Menerapkan prinsip hak istimewa paling rendah pada akses jaringan.
### Rahasia dalam Infrastruktur
- Jangan pernah menyimpan rahasia dalam variabel lingkungan CI/CD kecuali dienkripsi.
- Gunakan peran IAM penyedia cloud untuk instans EC2/VM, bukan kunci yang berumur panjang.
---

## Pencatatan dan Pemantauan
### Apa yang Harus Dicatat
- Peristiwa otentikasi (berhasil/gagal).
- Keputusan kontrol akses (kegagalan otorisasi).
- Tindakan Admin (pembuatan pengguna, penghapusan, perubahan izin).
- Perubahan skema database.
- Kesalahan dan pengecualian sistem.
- Permintaan dan tanggapan API (menyunting data sensitif).
### Yang Tidak Perlu Dicatat
- Kata sandi, rahasia, token, PII (Informasi Identifikasi Pribadi) kecuali di-hash/disunting.
- Nomor kartu kredit lengkap.
### Peringatan
- Atur peringatan untuk:
  - Beberapa login gagal (potensi kekerasan).
  - Pola akses yang tidak biasa (misalnya, dari lokasi baru, pada jam-jam ganjil).
  - Akun admin baru dibuat.
  - Tingkat kesalahan tinggi atau lonjakan latensi.
- Gunakan SIEM (Informasi Keamanan dan Manajemen Acara) untuk korelasi tingkat lanjut.
### Retensi Log
- Simpan log setidaknya selama 30–90 hari tergantung pada persyaratan peraturan.
- Simpan log dalam sistem terpusat dan anti kerusakan (mis., ELK Stack, Splunk, Datadog).
---

## Siklus Hidup Pengembangan Aman (SDL)
1. **Pelatihan**: Pastikan pengembang memahami kerentanan umum.
2. **Pemodelan ancaman**: Identifikasi potensi ancaman di awal desain.
3. **Standar pengkodean yang aman**: Ditegakkan melalui linter dan daftar periksa peninjauan kode.
4. **SAST** (Pengujian Keamanan Aplikasi Statis): Pindai kode sumber untuk mencari kerentanan (SonarQube, CodeQL).
5. **DAST** (Pengujian Keamanan Aplikasi Dinamis): Memindai aplikasi yang sedang berjalan (OWASP ZAP, Burp Suite).
6. **SCA** (Analisis Komposisi Perangkat Lunak): Memindai dependensi.
7. **Pengujian penetrasi**: Latihan peretasan etis secara teratur.
8. **Bug bounty**: Mendorong peneliti eksternal untuk menemukan kerentanan secara bertanggung jawab.
9. **Rencana respons insiden**: Miliki rencana yang jelas ketika pelanggaran terdeteksi.
---

## Daftar Periksa Darurat (Bila Diduga Ada Pelanggaran)
1. **Jangan panik** — tetapi bertindak cepat.
2. **Isolasi** sistem yang terkena dampak (putuskan sambungan dari jaringan jika diperlukan).
3. **Simpan bukti**: Ambil log, dump memori, dan image disk.
4. **Identifikasi** cakupannya: sistem mana, data apa.
5. **Putar** semua kredensial dan rahasia yang disusupi.
6. **Menambal** kerentanan.
7. **Beri tahu** pengguna dan badan pengatur yang terkena dampak jika diperlukan (dalam jangka waktu yang sah).
8. **Lakukan pemeriksaan mayat** untuk memahami akar permasalahan dan meningkatkan proses.