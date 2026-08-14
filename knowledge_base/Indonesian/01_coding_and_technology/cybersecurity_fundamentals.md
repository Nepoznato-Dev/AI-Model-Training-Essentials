---
# Metadata
title: "Cybersecurity Fundamentals"
description: "Encryption, TLS, OWASP, secure coding, SDL"
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
tags: [cybersecurity, coding-and-technology]
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
# Dasar-Dasar Keamanan Siber
Keamanan adalah suatu disiplin ilmu yang harus diintegrasikan ke dalam setiap lapisan sistem sejak awal, bukan ditambahkan setelahnya. Baik membangun aplikasi web, mengelola infrastruktur, atau mengirimkan API, memahami lanskap ancaman dan dasar-dasar pertahanan sangatlah penting.
---

## Enkripsi dan Kriptografi
### Enkripsi Simetris vs Asimetris
| Ketik | Cara Kerja | Kecepatan | Distribusi Kunci | Contoh |
|------|-------------|-------|-----------------|----------|
| **Simetris** | Kunci yang sama untuk enkripsi dan dekripsi | Cepat | Tantangan: bagaimana cara membagikan kuncinya? | AES-256, ChaCha20 |
| **Asimetris** | Enkripsi kunci publik, dekripsi kunci pribadi | Lebih lambat | Kunci publik dapat dibagikan secara terbuka | RSA, ECC (Kurva Elips) |
Dalam praktiknya, sebagian besar sistem menggunakan **keduanya**: enkripsi asimetris untuk menukar kunci simetris dengan aman, kemudian enkripsi simetris untuk sebagian besar data. Beginilah cara kerja TLS/HTTPS.
### Pencirian
Hashing adalah fungsi satu arah: mengubah input menjadi string berukuran tetap. Anda tidak dapat membalikkannya, tetapi masukan yang sama selalu menghasilkan keluaran yang sama.
| Kasus Penggunaan | Algoritma yang Direkomendasikan | Hindari |
|----------|----------------------|-------|
| **Penyimpanan kata sandi** | Argon2id, bcrypt, scrypt | MD5, SHA-1, SHA-256 biasa (terlalu cepat) |
| **Integritas data** | SHA-256, SHA-3 | MD5 (rusak), SHA-1 (rusak) |
| **Tanda tangan digital** | Ed25519, RSA-2048+ | DSA |
###TLS/HTTPS
HTTPS adalah HTTP melalui TLS (Transport Layer Security). Ini menyediakan:
- **Enkripsi**: Data dalam perjalanan tidak dapat dibaca oleh penyadap.
- **Otentikasi**: Server membuktikan identitasnya melalui sertifikat.
- **Integritas**: Data tidak dapat diubah saat transit tanpa terdeteksi.
Gunakan TLS 1.2 atau 1.3. Nonaktifkan TLS 1.0 dan 1.1. Aktifkan HSTS (HTTP Strict Transport Security) untuk memaksa browser selalu menggunakan HTTPS.
---

## Otentikasi dan Otorisasi
### Otentikasi: Siapa Anda?
| Metode | Tingkat Keamanan | Kasus Penggunaan |
|--------|---------------|----------|
| **Kata Sandi** | Rendah–Sedang | Akun dasar (menerapkan 12+ karakter, memeriksa pelanggaran) |
| **MFA (TOTP)** | Tinggi | Standar untuk akun sensitif (Google Authenticator, Authy) |
| **Kunci perangkat keras (FIDO2/WebAuthn)** | Sangat Tinggi | Akun dengan keamanan tinggi (YubiKey) |
| **Biometrik** | Sedang–Tinggi | Buka kunci perangkat (sidik jari, wajah) — bukan satu-satunya faktor |
| **OAuth2 / OIDC** | Tinggi | Login pihak ketiga ("Masuk dengan Google") |
**Aturan kata sandi**: menerapkan panjang minimum (12–16 karakter), memeriksa daftar kata sandi yang dilanggar, menggunakan Argon2id atau bcrypt untuk melakukan hashing dengan garam per pengguna.
### Otorisasi: Apa yang Dapat Anda Lakukan?
| Model | Deskripsi | Contoh |
|-------|-------------|---------|
| **RBAC** (Kontrol Akses Berbasis Peran) | Izin yang ditetapkan ke peran; pengguna mendapatkan peran | Admin, Editor, Penampil |
| **ABAC** (Berbasis Atribut) | Aturan berdasarkan atribut pengguna, sumber daya, lingkungan | "Manajer dapat menyetujui permintaan timnya" |
| **ACL** (Daftar Kontrol Akses) | Izin eksplisit per pengguna/sumber daya | Izin file (baca/tulis/eksekusi) |
**Prinsip hak istimewa terendah**: berikan setiap pengguna, layanan, dan proses hanya akses minimum yang mereka perlukan.
### JWT (Token Web JSON)
| Aspek | Rekomendasi |
|--------|---------------|
| **Penandatanganan** | RS256 atau ES256 (asimetris) lebih disukai; HS256 dapat diterima dengan rahasia yang dikelola |
| **Kedaluwarsa** | 15–60 menit untuk token akses; gunakan token penyegaran untuk sesi yang lebih lama |
| **Penyimpanan** | Cookie khusus HTTP (bukan Penyimpanan lokal — rentan terhadap XSS) |
| **Validasi** | Selalu verifikasi tanda tangan, penerbit, audiens, dan kedaluwarsa |
---

## OWASP 10 Teratas (2021)
OWASP Top 10 adalah dokumen kesadaran standar untuk keamanan aplikasi web. Ini mewakili risiko paling kritis:
| # | Resiko | Apa Artinya |
|---|------|--------------|
| 1 | **Kontrol Akses Rusak** | Pengguna dapat mengakses sumber daya yang tidak seharusnya |
| 2 | **Kegagalan Kriptografi** | Enkripsi lemah atau hilang untuk data sensitif |
| 3 | **Injeksi** | SQL, NoSQL, perintah OS, atau injeksi LDAP |
| 4 | **Desain Tidak Aman** | Cacat arsitektur yang tidak dapat diperbaiki dengan implementasi |
| 5 | **Kesalahan Konfigurasi Keamanan** | Kata sandi default, port terbuka, pesan kesalahan panjang |
| 6 | **Komponen Rentan** | CVE yang diketahui dalam dependensi |
| 7 | **Kegagalan Otentikasi** | Kata sandi lemah, salah urus sesi |
| 8 | **Kegagalan Integritas** | Serangan rantai pasokan, pembaruan yang tidak ditandatangani |
| 9 | **Kegagalan Pencatatan/Pemantauan** | Tidak ada deteksi pelanggaran |
| 10 | **SSRF** | Server ditipu untuk membuat permintaan ke sistem internal |
---

## Praktik Pengkodean yang Aman
### Validasi Masukan
| Aturan | Mengapa |
|------|-----|
| **Daftar Putih > Daftar Hitam** | Tentukan apa yang diperbolehkan, bukan apa yang diblokir |
| **Kueri berparameter** | Jangan pernah menggabungkan input pengguna ke dalam SQL — gunakan pernyataan yang telah disiapkan atau ORM |
| **Pengkodean HTML** | Enkode`<`,`>`,`&`,`"`,`'`untuk mencegah XSS |
| **Cangkangnya lolos** | Hindari membuat perintah shell dari input pengguna; gunakan`shlex.quote()`|
| **Batas panjang** | Terapkan panjang maksimum untuk mencegah buffer overflows dan DoS |
| **Pemeriksaan jenis** | Pastikan bilangan bulat adalah bilangan bulat, boolean adalah boolean |
### Kerentanan Umum
| Kerentanan | Serangan | Pertahanan |
|--------------|--------|---------|
| **Injeksi SQL** | `' OR 1=1 --`dalam formulir login | Kueri yang diparameterisasi |
| **XSS** | `<script>alert('hacked')</script>`di kolom komentar | Pengkodean keluaran, Kebijakan Keamanan Konten |
| **CSRF** | Menipu browser pengguna agar membuat permintaan tidak sah | Token CSRF, cookie SameSite |
| **Penjelajahan Jalur** | `../../etc/passwd`dalam parameter file | Validasi dan sanitasi jalur file |
| **IDOR** | Ubah`/user/123`menjadi`/user/124`untuk melihat data orang lain | Pemeriksaan otorisasi pada setiap permintaan |
---

## Keamanan Jaringan
### Firewall
| Ketik | Deskripsi |
|------|-------------|
| **Pemfilteran paket** | Aturan berdasarkan IP, port, protokol |
| **Status** | Melacak status koneksi; penyaringan yang lebih cerdas |
| **Tingkat aplikasi (WAF)** | Memeriksa lalu lintas HTTP; memblokir injeksi SQL, XSS, dll |
| **Grup keamanan cloud** | Firewall virtual untuk instans cloud (AWS SGs, Azure NSGs) |
**Aturan praktis**: memblokir semua lalu lintas masuk secara default; hanya buka apa yang secara eksplisit dibutuhkan (80, 443 untuk web).
### Segmentasi Jaringan
Tempatkan database dan cache di subnet pribadi tanpa akses internet langsung. Gunakan DMZ untuk layanan publik (server web, penyeimbang beban). Terapkan prinsip hak istimewa paling rendah pada akses jaringan.
---

## Manajemen Rahasia
### Aturan Emas
**Jangan pernah melakukan rahasia hardcode.** Tidak ada kunci API, sandi, atau URL database dalam kode sumber. Tidak ada rahasia dalam variabel lingkungan yang dikomit ke Git. Tidak ada rahasia di image Docker.
### Peralatan
| Alat | Ketik | Terbaik Untuk |
|------|------|----------|
| ** Gudang HashiCorp ** | Manajer rahasia perusahaan | Rahasia dinamis, enkripsi sebagai layanan |
| **Manajer Rahasia AWS** | Cloud-asli | Lingkungan AWS |
| **Gudang Kunci Azure** | Cloud-asli | Lingkungan Azure |
| **SOP** | File terenkripsi | Enkripsi rahasia di Git (dengan KMS atau GPG) |
| **Rahasia Docker** | Asli kontainer | Docker Swarm (untuk K8, pertimbangkan Secrets Store CSI) |
| **dotenv (.env)** | Pembangunan lokal | Hanya pengembangan — tidak pernah dalam produksi atau berkomitmen |
### Rotasi
Putar rahasia secara teratur dan otomatis. Jika sebuah rahasia bocor (misalnya, dimasukkan ke dalam repo publik), segera putar rahasia tersebut — bahkan jika menurut Anda tidak ada yang melihatnya.
---

## Keamanan Ketergantungan
Aplikasi Anda hanya seaman ketergantungan terlemahnya.
### Alat Pemindaian
| Bahasa | Alat |
|----------|-------|
| **Piton** | `safety`,`pip-audit`,`bandit`|
| **Node.js** | `npm audit`,`yarn audit`,`snyk`|
| **Karat** | `cargo audit`|
| **Pergi** | `govulncheck`|
| **Umum** | `Dependabot`(GitHub),`Renovate`,`Trivy`|
### Integritas Rantai Pasokan
- Gunakan file kunci (`package-lock.json`,`Cargo.lock`,`go.sum`) untuk build yang dapat direproduksi.
- Verifikasi checksum dari dependensi yang diunduh.
- Lebih memilih pendaftar resmi dan penerbit terverifikasi.
- Otomatiskan pembaruan kecil/tambalan melalui Dependabot atau Renovasi.
---

## Siklus Hidup Pengembangan Keamanan (SDL)
| Fase | Aktivitas |
|-------|----------|
| **Pelatihan** | Pastikan pengembang memahami kerentanan umum |
| **Pemodelan Ancaman** | Identifikasi potensi ancaman selama desain |
| **Standar Pengodean Aman** | Terapkan melalui linter dan daftar periksa tinjauan kode |
| **SAST** | Analisis statis kode sumber (SonarQube, CodeQL) |
| **DAST** | Analisis dinamis aplikasi yang sedang berjalan (OWASP ZAP, Burp Suite) |
| **SCA** | Analisis komposisi perangkat lunak — ketergantungan pemindaian |
| **Uji Penetrasi** | Latihan peretasan etis secara teratur |
| **Hadiah Serangga** | Mendorong peneliti eksternal untuk menemukan kerentanan |
| **Rencana Respons Insiden** | Miliki rencana yang jelas ketika pelanggaran terdeteksi |
---

## Daftar Periksa Darurat
Saat Anda mencurigai adanya pelanggaran:
1. **Jangan panik** — tetapi bertindak cepat.
2. **Isolasi** sistem yang terkena dampak (putuskan sambungan dari jaringan jika diperlukan).
3. **Simpan bukti**: ambil log, dump memori, image disk.
4. **Identifikasi cakupan**: sistem yang mana, data yang mana?
5. **Putar** semua kredensial dan rahasia yang disusupi.
6. **Menambal** kerentanan.
7. **Beri tahu** pengguna dan regulator yang terkena dampak jika diperlukan (dalam jangka waktu yang sah).
8. **Post-mortem**: mendokumentasikan akar permasalahan dan tindakan dalam waktu 24–48 jam.