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
- Alamat 32-bit, ditulis dalam empat oktet: `192.168.1.1`
- Total: ~4,3 miliar alamat (tetapi pada praktiknya sudah habis).

### IPv6
- Alamat 128-bit, ditulis dalam hex: `2001:0db8:85a3:0000:0000:8a2e:0370:7334`
- Total: 2¹²⁸ alamat (praktis tak terbatas).

### Rentang IP Pribadi (RFC 1918)
Ini tidak dapat dirutekan di internet; digunakan di dalam jaringan lokal:
- `10.0.0.0/8` (10.0.0.0 – 10.255.255.255)
- `172.16.0.0/12` (172.16.0.0 – 172.31.255.255)
- `192.168.0.0/16` (192.168.0.0 – 192.168.255.255)

### Notasi CIDR
`192.168.1.0/24` berarti 24 bit pertama adalah awalan jaringan; 8 bit terakhir adalah host. Ini mencakup alamat `192.168.1.0` hingga `192.168.1.255`.

---

## DNS (Sistem Nama Domain)

Memetakan nama domain (misalnya, `example.com`) ke alamat IP.

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

### Alat Umum
```bash
dig example.com            # DNS lookup (detailed)
nslookup example.com       # DNS lookup (simpler)
host example.com           # Quick lookup
dig -x 8.8.8.8             # Reverse lookup (IP to name)

Ports and Protocols
Well-Known Ports (0–1023)
Port	Protocol	Service
20, 21	TCP	FTP
22	TCP	SSH
23	TCP	Telnet
25	TCP	SMTP
53	UDP/TCP	DNS
80	TCP	HTTP
110	TCP	POP3
123	UDP	NTP
143	TCP	IMAP
443	TCP	HTTPS
465	TCP	SMTPS
587	TCP	SMTP (submission)
993	TCP	IMAPS
995	TCP	POP3S
3306	TCP	MySQL
5432	TCP	PostgreSQL
6379	TCP	Redis
27017	TCP	MongoDB
Check open ports
bash
ss -tulpn                 # Linux: listen and established sockets
netstat -an               # Older tool
lsof -i :8080             # See process using port 8080
nmap localhost            # Scan local ports
TCP vs UDP
Feature	TCP	UDP
Connection	Connection-oriented (handshake)	Connectionless
Reliability	Guaranteed delivery, retransmission	Best effort (may drop packets)
Ordering	Preserves order	No ordering guarantee
Flow control	Yes (sliding window)	No
Use cases	Web (HTTP), email, SSH, file transfer	DNS, streaming, VoIP, gaming, SNMP
Header size	20–60 bytes	8 bytes
HTTP and HTTPS
HTTP Methods
GET: Retrieve a resource (idempotent, safe).

POST: Submit data (not idempotent).

PUT: Update/replace a resource (idempotent).

PATCH: Partial update.

DELETE: Remove a resource (idempotent).

Status Codes
1xx: Informational (100 Continue).

2xx: Success (200 OK, 201 Created, 204 No Content).

3xx: Redirection (301 Moved Permanently, 302 Found, 304 Not Modified).

4xx: Client error (400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found, 429 Too Many Requests).

5xx: Server error (500 Internal Server Error, 502 Bad Gateway, 503 Service Unavailable).

Headers
Content-Type: media type (application/json, text/html).

Authorization: credentials (e.g., Bearer <token>).

Cache-Control: caching policy.

CORS headers: Access-Control-Allow-Origin, etc.

TLS/SSL
Encrypts HTTP traffic (HTTPS = HTTP over TLS).

Certificates from Certificate Authorities (CAs) authenticate the server.

Verify certificate chain and hostname on the client side.

Firewalls and NAT
Firewall
Filters traffic based on rules (source IP, dest IP, port, protocol).

Stateful firewalls track connection states.

NAT (Network Address Translation)
Translates private IPs to a public IP for internet access.

Port forwarding: maps a public port to an internal host/port.

Common Networking Commands
Connectivity Tests
bash
ping google.com            # ICMP echo request
ping -c 4 8.8.8.8          # ping 4 times
traceroute google.com      # Trace the route (Linux)
tracert google.com         # Windows version
Routing
bash
ip route show              # Linux: routing table
route -n                   # Older Linux
netstat -r                 # Windows/Mac
Network Interfaces
bash
ip addr show               # List interfaces and IPs
ifconfig                   # Older command
DNS
bash
dig example.com
nslookup example.com
host example.com
Connectivity to a Port
bash
nc -zv google.com 443      # Netcat: check if port 443 is open
telnet google.com 443      # Telnet to port
curl -v https://google.com # Verbose output
Firewall (Linux iptables/nftables)
bash
sudo ufw status            # Ubuntu: simple firewall
sudo iptables -L -n        # List rules
Network Statistics
bash
ss -tulpn                  # Show listening sockets (Linux)
netstat -an                # All sockets (all OS)
Subnetting (Quick Reference)
CIDR	Netmask	Number of addresses	Usable hosts
/32	255.255.255.255	1	1
/30	255.255.255.252	4	2
/29	255.255.255.248	8	6
/28	255.255.255.240	16	14
/27	255.255.255.224	32	30
/26	255.255.255.192	64	62
/25	255.255.255.128	128	126
/24	255.255.255.0	256	254
/23	255.255.254.0	512	510
/22	255.255.252.0	1,024	1,022
/16	255.255.0.0	65,536	65,534
/8	255.0.0.0	16,777,216	16,777,214
Load Balancing and Reverse Proxies
Nginx as Reverse Proxy
nginx
server {
    listen 80;
    server_name example.com;
    location / {
        proxy_pass http://localhost:3000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
Load Balancing Algorithms
Round-robin

Least connections

IP hash (session stickiness)

Weighted round-robin

Tools
Nginx, HAProxy (software)

AWS ELB, Azure Load Balancer, GCP Cloud Load Balancing (cloud)

Troubleshooting Checklist
Is the physical link up? (Check cables, Wi-Fi connection).

Can you ping the gateway? (e.g., ping 192.168.1.1).

Can you ping an external IP? (e.g., 8.8.8.8).

Can you resolve a domain? (dig google.com).

Is the application listening on the expected port? (ss -tulpn | grep 8080).

Is the firewall blocking the port? (Check iptables/ufw or cloud security groups).

Are there any errors in the application logs?

Is TLS certificate valid and trusted? (openssl s_client -connect example.com:443).

text

---

## File 6: `devops_sysadmin.md`

```penurunan harga
# DevOps dan Administrasi Sistem

Panduan praktis untuk mengelola server, mengotomatiskan operasi, dan memelihara infrastruktur yang andal.

---

## SSH (Shell Aman)

### Pembuatan Kunci
``` pesta
ssh-keygen -t ed25519 -C "your_email@example.com" # Modern dan aman
ssh-keygen -t rsa -b 4096 -C "email_anda@example.com" # Pengganti
Salin Kunci Publik ke Server
pesta
ssh-copy-id pengguna@host
# Alternatif manual:
kucing ~/.ssh/id_ed25519.pub | ssh pengguna@host "mkdir -p ~/.ssh && cat >> ~/.ssh/authorized_keys"
Konfigurasi SSH (~/.ssh/config)
ssh-config
Tuan rumah server saya
    Nama Host 192.168.1.10
    Pengguna ubuntu
    IdentityFile ~/.ssh/mykey
    Pelabuhan 2222
Perintah SSH Umum
pesta
ssh pengguna@host # Hubungkan
ssh -J jumpuser@jumphost pengguna@target # Proksi lompat
scp file.txt pengguna@host:/path/ # Salin file ke jarak jauh
scp pengguna@host:/path/file.txt .    # Salin dari jarak jauh
rsync -avz -e ssh ./local/ user@host:/remote/ # Sinkronisasi yang efisien
Pengerasan SSH
Nonaktifkan login root: PermitRootLogin no

Gunakan autentikasi berbasis kunci saja: Otentikasi Kata Sandi no

Ubah port default (opsional, keamanan melalui ketidakjelasan).

Aktifkan AllowUsers atau AllowGroups untuk membatasi akses.

Systemd (Manajemen Layanan Linux)
Perintah Umum
pesta
systemctl status nginx # Periksa status layanan
systemctl mulai nginx # Mulai layanan
systemctl menghentikan nginx
systemctl restart nginx
systemctl reload nginx # Graceful reload (baca ulang konfigurasi)
systemctl aktifkan nginx # Mulai saat boot
systemctl menonaktifkan nginx
systemctl list-units --type=service --all # Daftar semua layanan
systemctl daemon-reload # Muat ulang file unit setelah diedit
Membuat Unit Layanan systemd
Buat /etc/systemd/system/myapp.service:

ini
[Satuan]
Deskripsi=Aplikasi Python Saya
Setelah=jaringan.target

[Layanan]
Pengguna=pengguna saya
Grup=grup saya
Direktori Kerja=/opt/myapp
ExecStart=/usr/bin/python3 /opt/myapp/main.py
Mulai ulang=selalu
Mulai UlangSec=10
Lingkungan = "ENV = produksi"

[Instal]
WantedBy=multi-pengguna.target
Kemudian:

pesta
sudo systemctl daemon-reload
sudo systemctl aktifkan aplikasi saya
sudo systemctl mulai aplikasi saya
Jurnalctl (Lihat Log)
pesta
journalctl -u myapp # Log untuk layanan
journalctl -f # Ikuti (ekor) log
journalctl --sejak "1 jam yang lalu"
journalctl _PID=1234 # Filter berdasarkan ID proses
Strategi Penebangan
Pencatatan Terstruktur
Gunakan format JSON untuk membuat log dapat diurai oleh mesin:

ular piton
impor structlog
pencatat = structlog.get_logger()
logger.info("user_login", user_id=123, ip="192.168.1.1")
Tingkat Log
DEBUG: diagnostik terperinci.

INFO: kejadian umum (mulai, berhenti, transaksi normal).

PERINGATAN: tidak terduga tetapi tidak fatal.

ERROR: kesalahan yang mencegah operasi tertentu.

FATAL/KRITIS: mematikan sistem.

Agregasi Log
ELK Stack (Elasticsearch, Logstash, Kibana) atau Elastic Cloud.Loki + Grafana (alternatif ringan).

Datadog, Splunk, Logika Sumo (SaaS).

Rotasi Log (logrotate)
Cegah log agar tidak memenuhi disk. Konfigurasikan /etc/logrotate.d/myapp:

logrotate
/var/log/aplikasi saya/*.log {
    setiap hari
    memutar 7
    kompres
    kompresi penundaan
    hilangok
    pemberitahuan kosong
    buat 0640 pengguna saya grup saya
}
Pemantauan dan Peringatan
Metrik untuk Dipantau
Sistem: CPU, RAM, penggunaan disk, rata-rata beban, I/O jaringan.

Aplikasi: tingkat permintaan, latensi (p50, p95, p99), tingkat kesalahan, sesi aktif.

Basis data: jumlah kueri, kueri lambat, penggunaan kumpulan koneksi.

Bisnis: pendaftaran pengguna, tingkat konversi, pendapatan.

Alat
Prometheus + Grafana: Tumpukan sumber terbuka standar.

Pengekspor Node untuk metrik sistem.

Eksportir Blackbox untuk ketersediaan titik akhir.

Alertmanager untuk perutean peringatan.

Cloud asli: AWS CloudWatch, Azure Monitor, Pemantauan GCP.

Pemantauan Waktu Aktif
Pingdom, Statuspage, Uptime Lebih Baik, Uptime Kuma (dihosting sendiri).

Pemeriksaan kesehatan: mengekspos titik akhir /health yang mengembalikan 200 jika layanannya sehat.

Strategi Cadangan
Aturan 3-2-1
3 salinan data.

2 jenis media berbeda (misalnya, SSD + tape, atau lokal + cloud).

1 salinan di luar lokasi (misalnya, cloud atau pusat data jarak jauh).

Jenis Cadangan
Cadangan penuh: salin semuanya (lambat, banyak ruang).

Pencadangan tambahan: hanya menyalin perubahan sejak pencadangan penuh terakhir atau tambahan (pemulihan cepat dan rumit).

Pencadangan diferensial: menyalin perubahan sejak penuh terakhir (jalan tengah).

Pencadangan Basis Data
pesta
# PostgreSQL
pg_dump nama db > cadangan.sql
pg_dumpall > all_backup.sql

# MySQL / MariaDB
mysqldump -u root -p nama db > cadangan.sql

# Pulihkan
nama db psql <cadangan.sql
mysql -u root -p nama db < cadangan.sql
Pencadangan File
pesta
# Arsip tar
tar -czf backup.tar.gz /var/lib/data

# Rsync ke jarak jauh
rsync -avz /lokal/data/ pengguna@server cadangan:/cadangan/data/

# Cloud CLI (misalnya, AWS S3)
aws sinkronisasi s3 /lokal/data s3://my-bucket/backup/
Penjadwalan Pencadangan Otomatis (cron)
cron
# Jalankan setiap hari pada jam 2 pagi
0 2 * * * /usr/local/bin/backup_script.sh
Cron dan Pekerjaan Terjadwal
Sintaks Cron
teks
* * * * * perintah
│ │ │ │ │
│ │ │ │ └─ Hari dalam seminggu (0-7, 0=Minggu)
│ │ │ └─── Bulan (1-12)
│ │ └───── Hari dalam sebulan (1-31)
│ └─────── Jam (0-23)
└───────── Menit (0-59)
Contoh
cron
# Setiap 5 menit
*/5 * * * * /path/ke/script

# Setiap hari pukul 03.15
15 3 * * * /path/ke/script

# Setiap hari Senin jam 4 pagi
0 4 * * 1 /path/ke/script

# Setiap jam
0 * * * * /path/ke/script
Mengelola Cron
pesta
crontab -l # Daftar tugas cron pengguna saat ini
crontab -e # Sunting
crontab -r # Hapus semua
Anakron
Digunakan untuk sistem yang tidak berjalan 24/7 (misalnya laptop), memastikan pekerjaan berjalan pada akhirnya.

Manajemen dan Pembaruan Paket
Debian/Ubuntu (sesuai)
pesta
sudo apt update # Perbarui daftar paket
sudo apt upgrade # Tingkatkan semua paket
sudo tepat instal git nginx
sudo tepat hapus git
sudo apt autoremove # Hapus dependensi yang tidak digunakan
RHEL/CentOS/Fedora (dnf/yum)
pesta
sudo dnf periksa pembaruan
sudo pembaruan dnf
sudo dnf instal git nginx
sudo dnf hapus git
Pembaruan Keamanan
Aktifkan peningkatan tanpa pengawasan di Ubuntu untuk patch keamanan:

pesta
sudo apt install pemutakhiran tanpa pengawasan
sudo dpkg-reconfigure -plow tanpa pengawasan-upgrade
Docker dalam Produksi
Praktik Terbaik
Gunakan tag gambar tertentu (python:3.12-slim) bukan yang terbaru.

Jalankan container sebagai pengguna non-root.

Pindai gambar untuk mencari kerentanan (pemindaian buruh pelabuhan, trivy).

Tetapkan batas sumber daya (--memory, --cpus).

Gunakan rahasia (melalui rahasia Docker atau lingkungan dengan hati-hati).

Jaga agar gambar tetap kecil: bangunan multi-tahap, pangkalan alpine.

Docker Menulis dalam Produksi
Tetapkan batas sumber daya di docker-compose.yml:

yaml
layanan:
  aplikasi:
    gambar: aplikasi saya:1.0
    menyebarkan:
      sumber daya:
        batas:
          memori: 512M
          CPU: '0,5'
Dasar-dasar CI/CD
Tahapan Saluran Pipa
Build: Kompilasi kode, instal dependensi.

Pengujian: Jalankan pemeriksaan unit, integrasi, dan lint.

Containerise: Membangun image Docker.

Dorong: Dorong gambar ke registri kontainer.

Deploy: Perbarui lingkungan pementasan/produksi.

Alat
Tindakan GitHub: Terintegrasi dengan GitHub.

GitLab CI: Dibangun di GitLab.

Jenkins: Tradisional, sangat dapat dikonfigurasi.

CircleCI, Travis CI: Pihak ketiga yang populer.

ArgoCD: GitOps untuk Kubernetes.Contoh Tindakan GitHub (sederhana):
yaml
nama: CI
pada: dorong
pekerjaan:
  membangun:
    berjalan-on: ubuntu-terbaru
    langkah-langkah:
      - penggunaan: tindakan/checkout@v4
      - menggunakan: tindakan/setup-python@v5
        dengan:
          versi python: '3.12'
      - jalankan: pip install -r persyaratan.txt
      - jalankan: pytest
Penyetelan dan Pemecahan Masalah Sistem
Periksa Ruang Disk
pesta
df -h # Penggunaan disk yang dapat dibaca manusia
du -sh /* | sort -h # Ukuran direktori tingkat atas
Periksa Penggunaan Memori
pesta
gratis -m # Memori dalam MB
vmstat 1 10 # Statistik memori virtual
top -o %MEM # Urutkan proses berdasarkan memori
Periksa Beban CPU
pesta
uptime # Memuat rata-rata selama 1,5,15 menit
top -o %CPU # Urutkan proses berdasarkan CPU
mpstat -P ALL 1 5 # Penggunaan CPU per inti
Periksa Jaringan
pesta
netstat -i # Statistik antarmuka
iftop # Penggunaan bandwidth langsung (membutuhkan instalasi)
nload # Monitor bandwidth lain
Temukan File Besar
pesta
temukan / -ketik f -ukuran +100M -exec ls -lh {} \; 2>/dev/null
Infrastruktur sebagai Kode (IaC)
terraform
Deklarasikan sumber daya cloud di HCL.

hcl
penyedia "aws" {
  wilayah = "kita-timur-1"
}
sumber daya "aws_instance" "web" {
  ami = "ami-0c55b159cbfafe1f0"
  instance_type = "t2.mikro"
}
Mungkin
Manajemen konfigurasi tanpa agen menggunakan YAML.

yaml
- nama: Instal nginx
  host: server web
  tugas:
    - nama: Instal nginx
      tepat:
        nama: nginx
        negara: sekarang
Praktik Terbaik
Gunakan modul dan peran untuk digunakan kembali.

Simpan status dari jarak jauh (S3, Terraform Cloud).

Gunakan variabel dan rahasia (AWS_SECRET_ACCESS_KEY melalui lingkungan, bukan hardcode).

Kontrol versi kode IaC Anda.

Respons Insiden (On-call)
Daftar Periksa untuk Gangguan Layanan
Akui peringatannya.

Menilai cakupan: Layanan/pengguna mana yang terpengaruh?

Identifikasi masalahnya (lihat log, metrik, penerapan terkini).

Berisi jika memungkinkan (pemutus sirkuit, tanda fitur).

Kembalikan atau perbaiki ke depan.

Komunikasikan status kepada pemangku kepentingan dan pengguna (halaman status).

Dokumentasikan garis waktu kejadian dan tindakan.

Post-mortem: dalam waktu 24–48 jam, tulis analisis akar penyebab (RCA) dan item tindakan untuk mencegah terulangnya kembali.