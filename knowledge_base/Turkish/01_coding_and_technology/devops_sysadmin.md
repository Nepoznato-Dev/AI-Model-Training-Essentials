<!--
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

-->
# DevOps ve Sistem Yönetimi
Sunucuları yönetmek, işlemleri otomatikleştirmek ve güvenilir altyapıyı sürdürmek için pratik bir kılavuz.
---

## SSH (Güvenli Kabuk)
### Anahtar Oluşturma
```bash
ssh-keygen -t ed25519 -C "your_email@example.com"   # Modern and secure
ssh-keygen -t rsa -b 4096 -C "your_email@example.com" # Fallback
```

### Genel Anahtarı Sunucuya Kopyala
```bash
ssh-copy-id user@host
# Manual alternative:
cat ~/.ssh/id_ed25519.pub | ssh user@host "mkdir -p ~/.ssh && cat >> ~/.ssh/authorized_keys"
```

### SSH Yapılandırması (`~/.ssh/config`)
```
Host myserver
    HostName 192.168.1.10
    User ubuntu
    IdentityFile ~/.ssh/mykey
    Port 2222
```

### Ortak SSH Komutları
```bash
ssh user@host                              # Connect
ssh -J jumpuser@jumphost user@target       # Proxy jump
scp file.txt user@host:/path/              # Copy file to remote
scp user@host:/path/file.txt .             # Copy from remote
rsync -avz -e ssh ./local/ user@host:/remote/  # Efficient sync
```

### SSH'yi Sağlamlaştırma
- Kök oturum açmayı devre dışı bırakın:`PermitRootLogin no`
- Yalnızca anahtar tabanlı kimlik doğrulamayı kullanın:`PasswordAuthentication no`
- Varsayılan bağlantı noktasını değiştirin (isteğe bağlı, gizlilik yoluyla güvenlik).
- Erişimi kısıtlamak için`AllowUsers`veya`AllowGroups`seçeneğini etkinleştirin.
---

## Systemd (Linux Hizmet Yönetimi)
### Ortak Komutlar
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

### Bir systemd Hizmet Birimi oluşturma
`/etc/systemd/system/myapp.service` oluşturun:
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

Daha sonra:
```bash
sudo systemctl daemon-reload
sudo systemctl enable myapp
sudo systemctl start myapp
```

---

## Journalctl (Günlükleri Görüntüle)
```bash
journalctl -u myapp              # Logs for service
journalctl -f                    # Follow (tail) logs
journalctl --since "1 hour ago"
journalctl _PID=1234             # Filter by process ID
```

---

## Günlüğe Kaydetme Stratejileri
### Yapılandırılmış Günlük Kaydı
Günlükleri makine tarafından ayrıştırılabilir hale getirmek için JSON biçimini kullanın:
```python
import structlog
logger = structlog.get_logger()
logger.info("user_login", user_id=123, ip="192.168.1.1")
```

### Günlük Düzeyleri
| Seviye | Amaç |
|----------|-----------|
| **HATA AYIKLAMA** | Ayrıntılı teşhis bilgileri |
| **BİLGİ** | Genel olaylar (başlatma, durdurma, normal işlemler) |
| **UYARI** | Beklenmedik ama ölümcül değil |
| **HATA** | Belirli bir işlemi engelleyen hata |
| **ÖLÜMCÜL/KRİTİK** | Sistem kapatma |
### Günlük Toplama
- **ELK Stack** (Elasticsearch, Logstash, Kibana) veya Elastic Cloud.
- **Loki + Grafana** (hafif alternatif).
- **Datadog, Splunk, Sumo Logic** (SaaS).
### Günlük Döndürme (`logrotate`)
Günlüklerin diskleri doldurmasını önleyin.`/etc/logrotate.d/myapp`öğesini yapılandırın:
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

## İzleme ve Uyarı
### İzlenecek Metrikler
| Kategori | Temel Metrikler |
|----------|----------------|
| **Sistem** | CPU, RAM, disk kullanımı, yük ortalaması, ağ G/Ç |
| **Uygulama** | İstek oranı, gecikme (p50, p95, p99), hata oranı, aktif oturumlar |
| **Veritabanı** | Sorgu sayısı, yavaş sorgular, bağlantı havuzu kullanımı |
| **İş** | Kullanıcı kayıtları, dönüşüm oranı, gelir |
### Aletler
- **Prometheus + Grafana**: Standart açık kaynak yığını.
- Sistem ölçümleri için **Düğüm Aktarıcı**.
- Uç nokta kullanılabilirliği için **Blackbox Exporter**.
- Uyarı yönlendirme için **Alertmanager**.
- **Bulutta yerel**: AWS CloudWatch, Azure Monitor, GCP İzleme.
### Çalışma Süresi İzleme
- Pingdom, Durum Sayfası, Daha İyi Çalışma Süresi, Çalışma Süresi Kuma (kendi kendine barındırılan).
- Durum denetimleri: Hizmetin sağlıklı olması durumunda 200 değerini döndüren bir`/health`uç noktasını açığa çıkarın.
---

## Yedekleme Stratejileri
### 3-2-1 Kuralı
- **3** veri kopyası.
- **2** farklı ortam türleri (ör. SSD + bant veya yerel + bulut).
- **1** site dışına kopyalayın (ör. bulut veya uzak veri merkezi).
### Yedekleme Türleri
| Tür | Açıklama | Takas |
|------|-------------|-----------|
| **Dolu** | Her şeyi kopyala | Yavaş, yer ağırlıklı |
| **Artımlı** | Yalnızca son tam veya artımlı tarihten bu yana yapılan değişiklikleri kopyala | Hızlı, karmaşık geri yükleme |
| **Diferansiyel** | Son dolumdan bu yana yapılan değişiklikleri kopyala | Orta yol |
### Veritabanı Yedeklemeleri
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

### Dosya Yedeklemeleri
```bash
# Tar archive
tar -czf backup.tar.gz /var/lib/data

# Rsync to remote
rsync -avz /local/data/ user@backup-server:/backup/data/

# Cloud CLI (e.g., AWS S3)
aws s3 sync /local/data s3://my-bucket/backup/
```

### Otomatik Yedekleme Planlaması (cron)
```cron
# Run daily at 2am
0 2 * * * /usr/local/bin/backup_script.sh
```

---

## Cron ve Zamanlanmış İşler
### Cron Söz Dizimi
```
* * * * * command
│ │ │ │ │
│ │ │ │ └─ Day of week (0-7, 0=Sun)
│ │ │ └─── Month (1-12)
│ │ └───── Day of month (1-31)
│ └─────── Hour (0-23)
└───────── Minute (0-59)
```

### Örnekler
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

### Cron'u Yönetmek
```bash
crontab -l          # List current user's cron jobs
crontab -e          # Edit
crontab -r          # Remove all
```

### Anakron
7/24 çalışmayan sistemler için kullanılır (ör. dizüstü bilgisayarlar); işlerin eninde sonunda çalışmasını sağlar.
---

## Paket Yönetimi ve Güncellemeler
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

### Güvenlik Güncellemeleri
Güvenlik yamaları için Ubuntu'da`unattended-upgrades`özelliğini etkinleştirin:
```bash
sudo apt install unattended-upgrades
sudo dpkg-reconfigure -plow unattended-upgrades
```

---

## Üretimde Docker
### En İyi Uygulamalar
-`latest`yerine belirli resim etiketleri (`python:3.12-slim`) kullanın.
- Kapları root olmayan kullanıcı olarak çalıştırın.
- Görüntüleri güvenlik açıklarına karşı tarayın (`docker scan`,`trivy`).
- Kaynak sınırlarını ayarlayın (`--memory`,`--cpus`).
- Sırları kullanın (Docker sırları veya ortam aracılığıyla dikkatli olun).
- Resimleri küçük tutun: çok aşamalı yapılar, dağ üssü.
### Üretimde Docker Compose
`docker-compose.yml` içinde kaynak sınırlarını ayarlayın:
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

## CI/CD Temelleri
### Boru Hattı Aşamaları
| Sahne | Açıklama |
|----------|----------------|
| **İnşa** | Kodu derleyin, bağımlılıkları yükleyin |
| **Test** | Birim, entegrasyon ve tüy bırakma kontrollerini çalıştırın |
| **Konteynerleştirme** | Docker görüntüsü oluşturun |
| **İtin** | Görüntüyü kapsayıcı kayıt defterine aktar |
| **Dağıtım** | Aşama/üretim ortamını güncelleyin |
### Aletler
| Araç | Notlar |
|------|----------|
| **GitHub Eylemleri** | GitHub ile entegre |
| **GitLab CI** | GitLab'da yerleşik |
| **Jenkins** | Geleneksel, son derece yapılandırılabilir |
| **CircleCI, Travis CI** | Popüler üçüncü taraf |
| **ArgoCD** | Kubernetes için GitOps |
### Örnek GitHub Eylemi
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

## Sistem Ayarlama ve Sorun Giderme
### Disk Alanını Kontrol Edin
```bash
df -h                      # Human-readable disk usage
du -sh /* | sort -h        # Size of top-level directories
```

### Bellek Kullanımını Kontrol Edin
```bash
free -m                    # Memory in MB
vmstat 1 10                # Virtual memory statistics
top -o %MEM                # Sort processes by memory
```

### CPU Yükünü Kontrol Edin
```bash
uptime                     # Load average over 1,5,15 minutes
top -o %CPU                # Sort processes by CPU
mpstat -P ALL 1 5          # Per-core CPU usage
```

### Ağı Kontrol Et
```bash
netstat -i                 # Interface statistics
iftop                      # Live bandwidth usage (requires install)
nload                      # Another bandwidth monitor
```

### Büyük Dosyaları Bulun
```bash
find / -type f -size +100M -exec ls -lh {} \; 2>/dev/null
```

---

## Kod Olarak Altyapı (IaC)
### Terraform
Bulut kaynaklarını HCL'de bildirin.
```hcl
provider "aws" {
  region = "us-east-1"
}
resource "aws_instance" "web" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t2.micro"
}
```

### Ansible
YAML kullanarak aracısız yapılandırma yönetimi.
```yaml
- name: Install nginx
  hosts: webservers
  tasks:
    - name: Install nginx
      apt:
        name: nginx
        state: present
```

### En İyi Uygulamalar
- Yeniden kullanılabilirlik için modülleri ve rolleri kullanın.
- Durumu uzaktan saklayın (S3, Terraform Cloud).
- Değişkenleri ve sırları kullanın (`AWS_SECRET_ACCESS_KEY`ortam aracılığıyla, sabit kodlanmış değil).
- IaC kodunuzun sürümünü kontrol edin.
---

## Olay Müdahalesi (Çağrı Üzerine)
### Hizmet Kesintisi için Kontrol Listesi
1. Uyarıyı kabul edin.
2. Kapsamı değerlendirin: Hangi hizmetler/kullanıcılar etkileniyor?
3. Sorunu tanımlayın (günlüklere, ölçümlere, son dağıtımlara bakın).
4. Mümkünse (devre kesiciler, özellik işaretleri) muhafaza edin.
5. Geri alın veya ileri doğru düzeltin.
6. Durumu paydaşlara ve kullanıcılara iletin (durum sayfası).
7. Olay zaman çizelgesini ve eylemleri belgeleyin.
8. Ölüm sonrası: 24-48 saat içinde bir temel neden analizi (RCA) ve tekrarı önlemek için eylem öğeleri yazın.