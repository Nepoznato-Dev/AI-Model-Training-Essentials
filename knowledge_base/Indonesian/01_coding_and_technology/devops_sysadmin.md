---
# Metadata
title: "DevOps and System Administration"
description: "SSH, systemd, logging, monitoring, backups, Docker, CI/CD"
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
tags: [devops, sysadmin, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "19 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# DevOps dan Administrasi Sistem
Panduan praktis untuk mengelola server, mengotomatiskan operasi, dan memelihara infrastruktur yang andal.
---

## SSH (Shell Aman)
### Pembuatan Kunci
```bash
ssh-keygen -t ed25519 -C "your_email@example.com"   # Modern and secure
ssh-keygen -t rsa -b 4096 -C "your_email@example.com" # Fallback
```

### Salin Kunci Publik ke Server
```bash
ssh-copy-id user@host
# Manual alternative:
cat ~/.ssh/id_ed25519.pub | ssh user@host "mkdir -p ~/.ssh && cat >> ~/.ssh/authorized_keys"
```

### Konfigurasi SSH (`~/.ssh/config`)
```
Host myserver
    HostName 192.168.1.10
    User ubuntu
    IdentityFile ~/.ssh/mykey
    Port 2222
```

### Perintah SSH Umum
```bash
ssh user@host                              # Connect
ssh -J jumpuser@jumphost user@target       # Proxy jump
scp file.txt user@host:/path/              # Copy file to remote
scp user@host:/path/file.txt .             # Copy from remote
rsync -avz -e ssh ./local/ user@host:/remote/  # Efficient sync
```

### Pengerasan SSH
- Nonaktifkan login root:`PermitRootLogin no`
- Gunakan autentikasi berbasis kunci saja:`PasswordAuthentication no`
- Ubah port default (opsional, keamanan melalui ketidakjelasan).
- Aktifkan`AllowUsers`atau`AllowGroups`untuk membatasi akses.
---

## Systemd (Manajemen Layanan Linux)
### Perintah Umum
```bash
systemctl status nginx           # Check service status
systemctl start nginx            # Start service
systemctl stop nginx
systemctl restart nginx
systemctl reload nginx           # Graceful reload (re-read config)
systemctl enable nginx           # Start on boot
systemctl disable nginx
systemctl list-units --type=service --all   # List all services
systemctl daemon-reload          # Reload unit files after editing
```

### Membuat Unit Layanan systemd
Buat`/etc/systemd/system/myapp.service`:
```ini
[Unit]
Description=My Python App
After=network.target

[Service]
User=myuser
Group=mygroup
WorkingDirectory=/opt/myapp
ExecStart=/usr/bin/python3 /opt/myapp/main.py
Restart=always
RestartSec=10
Environment="ENV=production"

[Install]
WantedBy=multi-user.target
```

Kemudian:
```bash
sudo systemctl daemon-reload
sudo systemctl enable myapp
sudo systemctl start myapp
```

---

## Jurnalctl (Lihat Log)
```bash
journalctl -u myapp              # Logs for service
journalctl -f                    # Follow (tail) logs
journalctl --since "1 hour ago"
journalctl _PID=1234             # Filter by process ID
```

---

## Strategi Pencatatan
### Pencatatan Log Terstruktur
Gunakan format JSON untuk membuat log dapat diurai oleh mesin:
```python
import structlog
logger = structlog.get_logger()
logger.info("user_login", user_id=123, ip="192.168.1.1")
```

### Tingkat Log
| Tingkat | Tujuan |
|-------|---------|
| **DEBUG** | Informasi diagnostik terperinci |
| **INFO** | Peristiwa umum (mulai, berhenti, transaksi normal) |
| **PERINGATAN** | Tak terduga tapi tidak fatal |
| **KESALAHAN** | Kesalahan yang mencegah operasi tertentu |
| **FATAL/KRITIS** | Pematian sistem |
### Agregasi Log
- **ELK Stack** (Elasticsearch, Logstash, Kibana) atau Elastic Cloud.
- **Loki + Grafana** (alternatif ringan).
- **Datadog, Splunk, Logika Sumo** (SaaS).
### Rotasi Log (`logrotate`)
Cegah log agar tidak memenuhi disk. Konfigurasikan`/etc/logrotate.d/myapp`:
```
/var/log/myapp/*.log {
    daily
    rotate 7
    compress
    delaycompress
    missingok
    notifempty
    create 0640 myuser mygroup
}
```

---

## Pemantauan dan Peringatan
### Metrik yang Harus Dipantau
| Kategori | Metrik Utama |
|----------|-------------|
| **Sistem** | CPU, RAM, penggunaan disk, rata-rata beban, I/O jaringan |
| **Aplikasi** | Tingkat permintaan, latensi (p50, p95, p99), tingkat kesalahan, sesi aktif |
| **Basis Data** | Jumlah kueri, kueri lambat, penggunaan kumpulan koneksi |
| **Bisnis** | Pendaftaran pengguna, tingkat konversi, pendapatan |
### Peralatan
- **Prometheus + Grafana**: Tumpukan sumber terbuka standar.
- **Pengekspor Node** untuk metrik sistem.
- **Eksportir Blackbox** untuk ketersediaan titik akhir.
- **Alertmanager** untuk perutean peringatan.
- **Cloud asli**: AWS CloudWatch, Azure Monitor, Pemantauan GCP.
### Pemantauan Waktu Aktif
- Pingdom, Statuspage, Uptime Lebih Baik, Uptime Kuma (dihosting sendiri).
- Pemeriksaan kesehatan: mengekspos titik akhir`/health`yang mengembalikan 200 jika layanannya sehat.
---

## Strategi Cadangan
### Aturan 3-2-1
- **3** salinan data.
- **2** jenis media berbeda (misalnya, SSD + tape, atau lokal + cloud).
- **1** salinan di luar lokasi (misalnya, cloud atau pusat data jarak jauh).
### Jenis Cadangan
| Ketik | Deskripsi | Pertukaran |
|------|-------------|-----------|
| **Penuh** | Salin semuanya | Lambat, penuh ruang |
| **Tambahan** | Salin hanya perubahan sejak | penuh atau tambahan terakhir Pemulihan yang cepat dan rumit |
| **Diferensial** | Salin perubahan sejak penuh terakhir | Jalan tengah |
### Pencadangan Basis Data
```bash
# PostgreSQL
pg_dump dbname > backup.sql
pg_dumpall > all_backup.sql

# MySQL / MariaDB
mysqldump -u root -p dbname > backup.sql

# Restore
psql dbname < backup.sql
mysql -u root -p dbname < backup.sql
```

### Pencadangan File
```bash
# Tar archive
tar -czf backup.tar.gz /var/lib/data

# Rsync to remote
rsync -avz /local/data/ user@backup-server:/backup/data/

# Cloud CLI (e.g., AWS S3)
aws s3 sync /local/data s3://my-bucket/backup/
```

### Penjadwalan Pencadangan Otomatis (cron)
```cron
# Run daily at 2am
0 2 * * * /usr/local/bin/backup_script.sh
```

---

## Cron dan Pekerjaan Terjadwal
### Sintaks Cron
```
* * * * * command
│ │ │ │ │
│ │ │ │ └─ Day of week (0-7, 0=Sun)
│ │ │ └─── Month (1-12)
│ │ └───── Day of month (1-31)
│ └─────── Hour (0-23)
└───────── Minute (0-59)
```

### Contoh
```cron
# Every 5 minutes
*/5 * * * * /path/to/script

# Every day at 3:15 AM
15 3 * * * /path/to/script

# Every Monday at 4 AM
0 4 * * 1 /path/to/script

# Every hour
0 * * * * /path/to/script
```

### Mengelola Cron
```bash
crontab -l          # List current user's cron jobs
crontab -e          # Edit
crontab -r          # Remove all
```

### Anakron
Digunakan untuk sistem yang tidak berjalan 24/7 (misalnya laptop); memastikan pekerjaan berjalan pada akhirnya.
---

## Manajemen dan Pembaruan Paket
### Debian/Ubuntu (`apt`)
```bash
sudo apt update                # Update package list
sudo apt upgrade               # Upgrade all packages
sudo apt install git nginx
sudo apt remove git
sudo apt autoremove            # Remove unused dependencies
```

### RHEL/CentOS/Fedora (`dnf`/`yum`)
```bash
sudo dnf check-update
sudo dnf update
sudo dnf install git nginx
sudo dnf remove git
```

### Pembaruan Keamanan
Aktifkan`unattended-upgrades`di Ubuntu untuk patch keamanan:
```bash
sudo apt install unattended-upgrades
sudo dpkg-reconfigure -plow unattended-upgrades
```

---

## Docker dalam Produksi
### Praktik Terbaik
- Gunakan tag gambar tertentu (`python:3.12-slim`) bukan`latest`.
- Jalankan container sebagai pengguna non-root.
- Pindai gambar untuk mencari kerentanan (`docker scan`,`trivy`).
- Tetapkan batas sumber daya (`--memory`,`--cpus`).
- Gunakan rahasia (melalui rahasia Docker atau lingkungan dengan hati-hati).
- Jaga agar gambar tetap kecil: bangunan multi-tahap, pangkalan alpine.
### Docker Menulis dalam Produksi
Tetapkan batas sumber daya di`docker-compose.yml`:
```yaml
services:
  app:
    image: myapp:1.0
    deploy:
      resources:
        limits:
          memory: 512M
          cpus: '0.5'
```

---

## Dasar-dasar CI/CD
### Tahapan Saluran Pipa
| Tahap | Deskripsi |
|-------|-------------|
| **Bangun** | Kompilasi kode, instal dependensi |
| **Tes** | Jalankan pemeriksaan unit, integrasi, dan lint |
| **Wadah** | Bangun gambar Docker |
| **Dorong** | Dorong gambar ke registri kontainer |
| **Menerapkan** | Perbarui lingkungan pementasan/produksi |
### Peralatan
| Alat | Catatan |
|------|-------|
| **Tindakan GitHub** | Terintegrasi dengan GitHub |
| **GitLab CI** | Dibangun di GitLab |
| **Jenkins** | Tradisional, sangat dapat dikonfigurasi |
| **LingkaranCI, Travis CI** | Pihak ketiga yang populer |
| **ArgoCD** | GitOps untuk Kubernetes |
### Contoh Tindakan GitHub
```yaml
name: CI
on: push
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.12'
      - run: pip install -r requirements.txt
      - run: pytest
```

---

## Penyetelan dan Pemecahan Masalah Sistem
### Periksa Ruang Disk
```bash
df -h                      # Human-readable disk usage
du -sh /* | sort -h        # Size of top-level directories
```

### Periksa Penggunaan Memori
```bash
free -m                    # Memory in MB
vmstat 1 10                # Virtual memory statistics
top -o %MEM                # Sort processes by memory
```

### Periksa Beban CPU
```bash
uptime                     # Load average over 1,5,15 minutes
top -o %CPU                # Sort processes by CPU
mpstat -P ALL 1 5          # Per-core CPU usage
```

### Periksa Jaringan
```bash
netstat -i                 # Interface statistics
iftop                      # Live bandwidth usage (requires install)
nload                      # Another bandwidth monitor
```

### Temukan File Besar
```bash
find / -type f -size +100M -exec ls -lh {} \; 2>/dev/null
```

---

## Infrastruktur sebagai Kode (IaC)
### Terraform
Deklarasikan sumber daya cloud di HCL.
```hcl
provider "aws" {
  region = "us-east-1"
}
resource "aws_instance" "web" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t2.micro"
}
```

### Mungkin
Manajemen konfigurasi tanpa agen menggunakan YAML.
```yaml
- name: Install nginx
  hosts: webservers
  tasks:
    - name: Install nginx
      apt:
        name: nginx
        state: present
```

### Praktik Terbaik
- Gunakan modul dan peran untuk digunakan kembali.
- Simpan status dari jarak jauh (S3, Terraform Cloud).
- Gunakan variabel dan rahasia (`AWS_SECRET_ACCESS_KEY`melalui lingkungan, bukan hardcode).
- Kontrol versi kode IaC Anda.
---

## Respons Insiden (Saat Panggilan)
### Daftar Periksa Gangguan Layanan
1. Akui peringatannya.
2. Menilai cakupan: Layanan/pengguna mana yang terdampak?
3. Identifikasi masalahnya (lihat log, metrik, penerapan terkini).
4. Berisi jika memungkinkan (pemutus sirkuit, tanda fitur).
5. Kembalikan atau perbaiki ke depan.
6. Komunikasikan status kepada pemangku kepentingan dan pengguna (halaman status).
7. Dokumentasikan kronologi kejadian dan tindakannya.
8. Post-mortem: dalam waktu 24–48 jam, tuliskan analisis akar penyebab (RCA) dan item tindakan untuk mencegah terulangnya kembali.