---
# Metadata
title: "Networking Basics"
description: "OSI model, TCP/IP, protocols, security"
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
tags: [networking, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "12 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Dasar-Dasar Jaringan
Referensi praktis untuk pengembang dan sysadmin — konsep inti, protokol, perintah, dan pemecahan masalah.
---

## Model OSI (7 Lapisan)
Kerangka konseptual untuk memahami komunikasi jaringan.
| Lapisan | Nama | Fungsi | Contoh protokol |
|-------|------|----------|-------------------|
| 7 | Aplikasi | Layanan pengguna akhir | HTTP, HTTPS, FTP, SMTP, DNS, SSH |
| 6 | Presentasi | Pemformatan data, enkripsi, kompresi | TLS, JPEG, ASCII |
| 5 | Sesi | Manajemen koneksi | NetBIOS, RPC |
| 4 | Transportasi | Pengiriman ujung ke ujung, koreksi kesalahan, kontrol aliran | TCP, UDP |
| 3 | Jaringan | Perutean, pengalamatan | IP, ICMP, OSPF, BGP |
| 2 | Tautan Data | Pembingkaian, deteksi kesalahan, alamat MAC | Ethernet, Wi-Fi, PPP |
| 1 | Fisik | Transmisi bit mentah | Kabel Ethernet, serat optik, gelombang radio |
Dalam praktiknya, **model TCP/IP** (4 lapisan: Link, Internet, Transport, Aplikasi) lebih umum digunakan untuk internet.
---

## Pengalamatan IP
### IPv4
- Alamat 32-bit, ditulis dalam empat oktet:`192.168.1.1`
- Total: ~4,3 miliar alamat (tetapi pada praktiknya sudah habis).
### IPv6
- Alamat 128-bit, ditulis dalam hex:`2001:0db8:85a3:0000:0000:8a2e:0370:7334`
- Total: 2¹²⁸ alamat (hampir tak terbatas).
### Rentang IP Pribadi (RFC 1918)
Ini tidak dapat dirutekan di internet; digunakan di dalam jaringan lokal:
-`10.0.0.0/8`(10.0.0.0 – 10.255.255.255)
-`172.16.0.0/12`(172.16.0.0 – 172.31.255.255)
-`192.168.0.0/16`(192.168.0.0 – 192.168.255.255)
### Notasi CIDR
`192.168.1.0/24`berarti 24 bit pertama adalah awalan jaringan; 8 bit terakhir adalah host. Ini mencakup alamat`192.168.1.0`hingga`192.168.1.255`.
---

## DNS (Sistem Nama Domain)
Memetakan nama domain (misalnya,`example.com`) ke alamat IP.
### Jenis Catatan
| Ketik | Tujuan |
|------|---------|
| **SEBUAH** | Memetakan domain ke alamat IPv4 |
| **AAAA** | Memetakan domain ke alamat IPv6 |
| **CNAME** | Alias ​​ke nama domain lain |
| **MX** | Server pertukaran surat |
| **TXT** | Teks sewenang-wenang (SPF, DKIM, verifikasi) |
| **NS** | Server nama untuk domain |
| **SRV** | Catatan layanan (misalnya, untuk SIP) |
### Alat Umum```bash
dig example.com            # DNS lookup (detailed)
nslookup example.com       # DNS lookup (simpler)
host example.com           # Quick lookup
dig -x 8.8.8.8             # Reverse lookup (IP to name)
```

---

## Port dan Protokol
### Pelabuhan Terkenal (0–1023)
| Pelabuhan | Protokol | Layanan |
|------|----------|---------|
| 20, 21 | TCP | FTP |
| 22 | TCP | SSH |
| 23 | TCP | Telnet |
| 25 | TCP | SMTP |
| 53 | UDP/TCP | DNS |
| 80 | TCP | HTTP |
| 110 | TCP | POP3 |
| 123 | UDP | NTP |
| 143 | TCP | IMAP |
| 443 | TCP | HTTPS |
| 465 | TCP | SMTPS |
| 587 | TCP | SMTP (pengajuan) |
| 993 | TCP | IMAP |
| 995 | TCP | POP3S |
| 3306 | TCP | MySQL |
| 5432 | TCP | PostgreSQL |
| 6379 | TCP | Redis |
| 27017 | TCP | MongoDB |
### Periksa Port Terbuka
```bash
ss -tulpn                 # Linux: listen and established sockets
netstat -an               # Older tool
lsof -i :8080             # See process using port 8080
nmap localhost            # Scan local ports
```

---

## TCP vs UDP
| Fitur | TCP | UDP |
|---------|-----|-----|
| Koneksi | Berorientasi koneksi (jabat tangan) | Tanpa koneksi |
| Keandalan | Pengiriman terjamin, transmisi ulang | Upaya terbaik (mungkin menjatuhkan paket) |
| Memesan | Mempertahankan pesanan | Tidak ada jaminan pemesanan |
| Kontrol aliran | Ya (jendela geser) | Tidak |
| Kasus penggunaan | Web (HTTP), email, SSH, transfer file | DNS, streaming, VoIP, permainan, SNMP |
| Ukuran tajuk | 20–60 byte | 8 byte |
---

## HTTP dan HTTPS
### Metode HTTP
| Metode | Deskripsi |
|--------|-------------|
| **DAPATKAN** | Ambil sumber daya (idempoten, aman) |
| **POSTING** | Kirim data (tidak idempoten) |
| **MASUKKAN** | Perbarui/ganti sumber daya (idempoten) |
| **tambalan** | Pembaruan sebagian |
| **HAPUS** | Hapus sumber daya (idempoten) |
### Kode Status
| Kode | Arti |
|------|---------|
| **1xx** | Informasi (100 Lanjutan) |
| **2xx** | Sukses (200 OK, 201 Dibuat, 204 Tanpa Konten) |
| **3xx** | Pengalihan (301 Dipindahkan Secara Permanen, 302 Ditemukan, 304 Tidak Dimodifikasi) |
| **4xx** | Kesalahan klien (400 Permintaan Buruk, 401 Tidak Sah, 403 Dilarang, 404 Tidak Ditemukan, 429 Permintaan Terlalu Banyak) |
| **5xx** | Kesalahan server (500 Kesalahan Server Internal, 502 Gerbang Buruk, 503 Layanan Tidak Tersedia) |
### Tajuk
| Tajuk | Tujuan |
|--------|---------|
| `Content-Type`| Jenis media (`application/json`,`text/html`) |
| `Authorization`| Kredensial (misalnya,`Bearer <token>`) |
| `Cache-Control`| Kebijakan cache |
| Tajuk CORS | `Access-Control-Allow-Origin`, dll.|
---

##TLS/SSL
Mengenkripsi lalu lintas HTTP (HTTPS = HTTP melalui TLS).
- Sertifikat dari Otoritas Sertifikat (CA) mengautentikasi server.
- Verifikasi rantai sertifikat dan nama host di sisi klien.
---

## Firewall dan NAT
### Firewall
- Menyaring lalu lintas berdasarkan aturan (IP sumber, IP tujuan, port, protokol).
- Firewall stateful melacak status koneksi.
### NAT (Terjemahan Alamat Jaringan)
- Menerjemahkan IP pribadi ke IP publik untuk akses internet.
- Penerusan port: memetakan port publik ke host/port internal.
---

## Perintah Jaringan Umum
### Tes Konektivitas
```bash
ping google.com            # ICMP echo request
ping -c 4 8.8.8.8          # ping 4 times
traceroute google.com      # Trace the route (Linux)
tracert google.com         # Windows version
```

### Perutean
```bash
ip route show              # Linux: routing table
route -n                   # Older Linux
netstat -r                 # Windows/Mac
```

### Antarmuka Jaringan
```bash
ip addr show               # List interfaces and IPs
ifconfig                   # Older command
```

### DNS
```bash
dig example.com
nslookup example.com
host example.com
```

### Konektivitas ke Pelabuhan
```bash
nc -zv google.com 443      # Netcat: check if port 443 is open
telnet google.com 443      # Telnet to port
curl -v https://google.com # Verbose output
```

### Firewall (Linux iptables/nftables)
```bash
sudo ufw status            # Ubuntu: simple firewall
sudo iptables -L -n        # List rules
```

### Statistik Jaringan
```bash
ss -tulpn                  # Show listening sockets (Linux)
netstat -an                # All sockets (all OS)
```

---

## Subnetting (Referensi Cepat)
| CIDR | Masker Jaringan | Jumlah alamat | Host yang dapat digunakan |
|------|---------|---------------------|--------------|
| /32 | 255.255.255.255 | 1 | 1 |
| /30 | 255.255.255.252 | 4 | 2 |
| /29 | 255.255.255.248 | 8 | 6 |
| /28 | 255.255.255.240 | 16 | 14 |
| /27 | 255.255.255.224 | 32 | 30 |
| /26 | 255.255.255.192 | 64 | 62 |
| /25 | 255.255.255.128 | 128 | 126 |
| /24 | 255.255.255.0 | 256 | 254 |
| /23 | 255.255.254.0 | 512 | 510 |
| /22 | 255.255.252.0 | 1.024 | 1.022 |
| /16 | 255.255.0.0 | 65.536 | 65.534 |
| /8 | 255.0.0.0 | 16.777.216 | 16.777.214 |
---

## Load Balancing dan Reverse Proxy
### Nginx sebagai Proksi Terbalik
```nginx
server {
    listen 80;
    server_name example.com;
    location / {
        proxy_pass http://localhost:3000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

### Algoritma Penyeimbangan Beban
- **Persaingan penuh**
- **Koneksi paling sedikit**
- **hash IP** (kelekatan sesi)
- **Round-robin berbobot**
### Peralatan
- **Nginx, HAProxy** (perangkat lunak)
- **AWS ELB, Azure Load Balancer, Penyeimbangan Beban Cloud GCP** (cloud)
---

## Daftar Periksa Pemecahan Masalah
1. Apakah sambungan fisiknya sudah terpasang? (Periksa kabel, koneksi Wi-Fi).
2. Bisakah Anda melakukan ping ke gateway? (misalnya,`ping 192.168.1.1`).
3. Bisakah Anda melakukan ping ke IP eksternal? (misalnya,`8.8.8.8`).
4. Bisakah Anda menyelesaikan domain? (`dig google.com`).
5. Apakah aplikasi mendengarkan pada port yang diharapkan? (`ss -tulpn | grep 8080`).
6. Apakah firewall memblokir port tersebut? (Periksa`iptables`/`ufw`atau grup keamanan cloud).
7. Apakah ada kesalahan pada log aplikasi?
8. Apakah sertifikat TLS valid dan terpercaya? (`openssl s_client -connect example.com:443`).