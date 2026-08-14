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
# DevOps اور سسٹم ایڈمنسٹریشن
سرورز کے انتظام، خودکار آپریشنز، اور قابل اعتماد انفراسٹرکچر کو برقرار رکھنے کے لیے ایک عملی گائیڈ۔
---

## SSH (سیکیور شیل)
### کلیدی نسل
```bash
ssh-keygen -t ed25519 -C "your_email@example.com"   # Modern and secure
ssh-keygen -t rsa -b 4096 -C "your_email@example.com" # Fallback
```

### سرور پر عوامی کلید کاپی کریں۔
```bash
ssh-copy-id user@host
# Manual alternative:
cat ~/.ssh/id_ed25519.pub | ssh user@host "mkdir -p ~/.ssh && cat >> ~/.ssh/authorized_keys"
```

### SSH کنفیگ (`~/.ssh/config`)
```
Host myserver
    HostName 192.168.1.10
    User ubuntu
    IdentityFile ~/.ssh/mykey
    Port 2222
```

### عام SSH کمانڈز
```bash
ssh user@host                              # Connect
ssh -J jumpuser@jumphost user@target       # Proxy jump
scp file.txt user@host:/path/              # Copy file to remote
scp user@host:/path/file.txt .             # Copy from remote
rsync -avz -e ssh ./local/ user@host:/remote/  # Efficient sync
```

### SSH کو سخت کرنا
- روٹ لاگ ان کو غیر فعال کریں:`PermitRootLogin no`
- صرف کلید پر مبنی سند استعمال کریں:`PasswordAuthentication no`
- ڈیفالٹ پورٹ کو تبدیل کریں (اختیاری، غیر واضح طور پر سیکورٹی)
- رسائی کو محدود کرنے کے لیے`AllowUsers`یا`AllowGroups`کو فعال کریں۔
---

## سسٹمڈ (لینکس سروس مینجمنٹ)
### کامن کمانڈز
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

### سسٹمڈ سروس یونٹ بنانا
`/etc/systemd/system/myapp.service` بنائیں:
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

پھر:
```bash
sudo systemctl daemon-reload
sudo systemctl enable myapp
sudo systemctl start myapp
```

---

## Journalctl (لاگز دیکھیں)
```bash
journalctl -u myapp              # Logs for service
journalctl -f                    # Follow (tail) logs
journalctl --since "1 hour ago"
journalctl _PID=1234             # Filter by process ID
```

---

## لاگنگ کی حکمت عملی
### سٹرکچرڈ لاگنگ
لاگز مشین کو قابل تجزیہ بنانے کے لیے JSON فارمیٹ استعمال کریں:
```python
import structlog
logger = structlog.get_logger()
logger.info("user_login", user_id=123, ip="192.168.1.1")
```

### لاگ لیولز
| سطح | مقصد |
|---------|---------|
| **ڈیبگ** | تفصیلی تشخیصی معلومات |
| **معلومات** | عام واقعات (شروع، روک، عام لین دین) |
| **خبردار** | غیر متوقع لیکن مہلک نہیں |
| **خرابی** | خرابی جو کسی مخصوص آپریشن کو روکتی ہے |
| **مہلک/نازک** | سسٹم بند |
### لاگ ایگریگیشن
- **ELK Stack** (Elasticsearch، Logstash، Kibana) یا Elastic Cloud۔
- **لوکی + گرافانا** (ہلکا پھلکا متبادل)۔
- **ڈیٹا ڈوگ، اسپلنک، سومو لاجک** (ساس)۔
### لاگ گردش (`logrotate`)
لاگز کو ڈسکوں کو بھرنے سے روکیں۔`/etc/logrotate.d/myapp`ترتیب دیں:
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

## نگرانی اور انتباہ
### مانیٹر کرنے کے لیے میٹرکس
| زمرہ | کلیدی میٹرکس |
|------------|---------------|
| **نظام** | CPU، RAM، ڈسک کا استعمال، لوڈ اوسط، نیٹ ورک I/O |
| **درخواست** | درخواست کی شرح، تاخیر (p50, p95, p99)، غلطی کی شرح، فعال سیشنز |
| **ڈیٹا بیس** | سوالات کی گنتی، سست سوالات، کنکشن پول کا استعمال |
| **کاروبار** | صارف کے سائن اپس، تبادلوں کی شرح، آمدنی |
### ٹولز
- **Prometheus + Grafana**: معیاری اوپن سورس اسٹیک۔
- **نوڈ ایکسپورٹر** سسٹم میٹرکس کے لیے۔
- **بلیک باکس ایکسپورٹر** اختتامی نقطہ کی دستیابی کے لیے۔
- الرٹ روٹنگ کے لیے **الرٹ مینیجر**۔
- **کلاؤڈ مقامی**: AWS CloudWatch، Azure Monitor، GCP مانیٹرنگ۔
### اپ ٹائم مانیٹرنگ
- پنگڈم، اسٹیٹس پیج، بہتر اپ ٹائم، اپ ٹائم کما (خود میزبانی)۔
- صحت کی جانچ پڑتال: ایک`/health`اختتامی نقطہ کو ظاہر کریں جو 200 واپس کرتا ہے اگر سروس صحت مند ہے۔
---

## بیک اپ کی حکمت عملی
### 3-2-1 اصول
- **3** ڈیٹا کی کاپیاں۔
- **2** میڈیا کی مختلف اقسام (مثال کے طور پر، SSD + ٹیپ، یا مقامی + کلاؤڈ)۔
- **1** آف سائٹ کاپی کریں (مثال کے طور پر، کلاؤڈ یا ریموٹ ڈیٹا سینٹر)۔
### بیک اپ کی اقسام
| قسم | تفصیل | تجارت بند |
|------|---------------|------------|
| **مکمل** | سب کچھ کاپی کریں | سست، جگہ بھاری |
| **بڑھتی ہوئی** | صرف آخری مکمل یا اضافہ کے بعد کی تبدیلیاں کاپی کریں۔ تیز، پیچیدہ بحالی |
| **فرق** | آخری مکمل سے تبدیلیاں کاپی کریں | درمیانی زمین |
### ڈیٹا بیس بیک اپ
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

### فائل بیک اپ
```bash
# Tar archive
tar -czf backup.tar.gz /var/lib/data

# Rsync to remote
rsync -avz /local/data/ user@backup-server:/backup/data/

# Cloud CLI (e.g., AWS S3)
aws s3 sync /local/data s3://my-bucket/backup/
```

### خودکار بیک اپ شیڈولنگ (کرون)
```cron
# Run daily at 2am
0 2 * * * /usr/local/bin/backup_script.sh
```

---

## کرون اور شیڈول نوکریاں
### کرون نحو
```
* * * * * command
│ │ │ │ │
│ │ │ │ └─ Day of week (0-7, 0=Sun)
│ │ │ └─── Month (1-12)
│ │ └───── Day of month (1-31)
│ └─────── Hour (0-23)
└───────── Minute (0-59)
```

### مثالیں۔
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

### کرون کا انتظام کرنا
```bash
crontab -l          # List current user's cron jobs
crontab -e          # Edit
crontab -r          # Remove all
```

### ایناکرون
24/7 نہ چلنے والے سسٹمز کے لیے استعمال کیا جاتا ہے (جیسے لیپ ٹاپ)؛ یہ یقینی بناتا ہے کہ ملازمتیں آخر کار چلتی ہیں۔
---

## پیکیج مینجمنٹ اور اپ ڈیٹس
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

### سیکیورٹی اپ ڈیٹس
سیکیورٹی پیچ کے لیے اوبنٹو پر`unattended-upgrades`کو فعال کریں:
```bash
sudo apt install unattended-upgrades
sudo dpkg-reconfigure -plow unattended-upgrades
```

---

## پیداوار میں ڈوکر
### بہترین طرز عمل
- مخصوص تصویری ٹیگز استعمال کریں (`python:3.12-slim`) نہ کہ `latest`۔
- کنٹینرز کو غیر جڑ صارف کے طور پر چلائیں۔
- کمزوریوں کے لیے تصاویر اسکین کریں (`docker scan`، `trivy`)۔
- وسائل کی حدیں مقرر کریں (`--memory`، `--cpus`)۔
- رازوں کا استعمال کریں (ڈوکر راز یا ماحول کے ساتھ احتیاط سے)۔
- تصاویر کو چھوٹا رکھیں: ملٹی اسٹیج بلڈز، الپائن بیس۔
### پیداوار میں ڈوکر کمپوز
`docker-compose.yml` میں وسائل کی حدود مقرر کریں:
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

## CI/CD بنیادی باتیں
### پائپ لائن کے مراحل
| اسٹیج | تفصیل |
|---------|---------------|
| **تعمیر** | کوڈ مرتب کریں، انحصار انسٹال کریں |
| **ٹیسٹ** | یونٹ، انضمام، اور لنٹ چیکز چلائیں |
| **کنٹینریز** | ڈوکر امیج بنائیں |
| **دھکا** | تصویر کو کنٹینر رجسٹری میں پش کریں |
| **تعینات** | اسٹیجنگ/پروڈکشن ماحول کو اپ ڈیٹ کریں |
### ٹولز
| ٹول | نوٹس |
|------|---------|
| **گٹ ہب ایکشنز** | GitHub کے ساتھ مربوط |
| **گٹ لیب سی آئی** | GitLab میں بنایا گیا |
| **جینکنز** | روایتی، انتہائی قابل ترتیب |
| **سرکل سی آئی، ٹریوس سی آئی** | مقبول تیسری پارٹی |
| **ArgoCD** | GitOps for Kubernetes |
### مثال GitHub ایکشن
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

## سسٹم ٹیوننگ اور ٹربل شوٹنگ
### ڈسک کی جگہ چیک کریں۔
```bash
df -h                      # Human-readable disk usage
du -sh /* | sort -h        # Size of top-level directories
```

### میموری کا استعمال چیک کریں۔
```bash
free -m                    # Memory in MB
vmstat 1 10                # Virtual memory statistics
top -o %MEM                # Sort processes by memory
```

### CPU لوڈ چیک کریں۔
```bash
uptime                     # Load average over 1,5,15 minutes
top -o %CPU                # Sort processes by CPU
mpstat -P ALL 1 5          # Per-core CPU usage
```

### نیٹ ورک چیک کریں۔
```bash
netstat -i                 # Interface statistics
iftop                      # Live bandwidth usage (requires install)
nload                      # Another bandwidth monitor
```

### بڑی فائلیں تلاش کریں۔
```bash
find / -type f -size +100M -exec ls -lh {} \; 2>/dev/null
```

---

## بنیادی ڈھانچہ بطور کوڈ (IaC)
### ٹیرافارم
HCL میں کلاؤڈ وسائل کا اعلان کریں۔
```hcl
provider "aws" {
  region = "us-east-1"
}
resource "aws_instance" "web" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t2.micro"
}
```

### جوابدہ
YAML کا استعمال کرتے ہوئے ایجنٹ لیس کنفیگریشن مینجمنٹ۔
```yaml
- name: Install nginx
  hosts: webservers
  tasks:
    - name: Install nginx
      apt:
        name: nginx
        state: present
```

### بہترین طرز عمل
- دوبارہ استعمال کے لیے ماڈیولز اور کردار استعمال کریں۔
- اسٹیٹ کو دور سے اسٹور کریں (S3، Terraform Cloud)۔
- متغیرات اور راز استعمال کریں (`AWS_SECRET_ACCESS_KEY`بذریعہ ماحول، ہارڈ کوڈ نہیں)۔
- ورژن آپ کے IaC کوڈ کو کنٹرول کرتا ہے۔
---

## واقعہ کا جواب (آن کال)
### سروس کی بندش کے لیے چیک لسٹ
1. الرٹ کو تسلیم کریں۔
2. دائرہ کار کا اندازہ کریں: کون سی خدمات/صارفین متاثر ہوئے ہیں؟
3. مسئلے کی نشاندہی کریں (نوشتہ جات، میٹرکس، حالیہ تعیناتیوں کو دیکھیں)۔
4. اگر ممکن ہو تو (سرکٹ بریکرز، فیچر جھنڈے) پر مشتمل ہو۔
5. رول بیک یا آگے درست کریں۔
6. اسٹیک ہولڈرز اور صارفین (اسٹیٹس پیج) کو سٹیٹس سے آگاہ کریں۔
7. واقعے کی ٹائم لائن اور اعمال کو دستاویز کریں۔
8. پوسٹ مارٹم: 24-48 گھنٹوں کے اندر، دوبارہ ہونے سے بچنے کے لیے بنیادی وجہ تجزیہ (RCA) اور ایکشن آئٹمز لکھیں۔