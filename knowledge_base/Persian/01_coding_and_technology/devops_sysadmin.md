---
# Metadata
title: "DevOps and System Administration"
description: "SSH, systemd, logging, monitoring, backups, Docker, CI/CD"
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
# DevOps و مدیریت سیستم
راهنمای عملی برای مدیریت سرورها، خودکارسازی عملیات و حفظ زیرساخت قابل اعتماد.
---

## SSH (پوسته ایمن)
### نسل کلید
```bash
ssh-keygen -t ed25519 -C "your_email@example.com"   # Modern and secure
ssh-keygen -t rsa -b 4096 -C "your_email@example.com" # Fallback
```

### کلید عمومی را در سرور کپی کنید
```bash
ssh-copy-id user@host
# Manual alternative:
cat ~/.ssh/id_ed25519.pub | ssh user@host "mkdir -p ~/.ssh && cat >> ~/.ssh/authorized_keys"
```

### پیکربندی SSH (`~/.ssh/config`)
```
Host myserver
    HostName 192.168.1.10
    User ubuntu
    IdentityFile ~/.ssh/mykey
    Port 2222
```

### دستورات رایج SSH
```bash
ssh user@host                              # Connect
ssh -J jumpuser@jumphost user@target       # Proxy jump
scp file.txt user@host:/path/              # Copy file to remote
scp user@host:/path/file.txt .             # Copy from remote
rsync -avz -e ssh ./local/ user@host:/remote/  # Efficient sync
```

### سخت شدن SSH
- غیرفعال کردن ورود به سیستم ریشه:`PermitRootLogin no`
- فقط از احراز هویت مبتنی بر کلید استفاده کنید:`PasswordAuthentication no`
- تغییر پورت پیش فرض (اختیاری، امنیت از طریق مبهم).
- برای محدود کردن دسترسی،`AllowUsers`یا`AllowGroups`را فعال کنید.
---

## Systemd (مدیریت خدمات لینوکس)
### دستورات رایج
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

### ایجاد یک واحد خدمات سیستمی
ایجاد `/etc/systemd/system/myapp.service`:
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

سپس:
```bash
sudo systemctl daemon-reload
sudo systemctl enable myapp
sudo systemctl start myapp
```

---

## Journalctl (مشاهده گزارش‌ها)
```bash
journalctl -u myapp              # Logs for service
journalctl -f                    # Follow (tail) logs
journalctl --since "1 hour ago"
journalctl _PID=1234             # Filter by process ID
```

---

## استراتژی های ورود به سیستم
### ثبت ساختار یافته
از فرمت JSON برای تجزیه‌پذیر کردن لاگ‌ها توسط ماشین استفاده کنید:
```python
import structlog
logger = structlog.get_logger()
logger.info("user_login", user_id=123, ip="192.168.1.1")
```

### سطوح ورود به سیستم
| سطح | هدف |
|-------|---------|
| **اشکال زدایی** | اطلاعات دقیق تشخیصی |
| **اطلاعات** | رویدادهای عمومی (شروع، توقف، معاملات عادی) |
| **اخطار** | غیرمنتظره اما نه کشنده |
| **خطا** | خطایی که از یک عملیات خاص جلوگیری می کند |
| **کشنده/بحرانی** | خاموش شدن سیستم |
### تجمیع گزارش
- **ELK Stack** (Elasticsearch، Logstash، Kibana) یا Elastic Cloud.
- **Loki + Grafana** (جایگزین سبک وزن).
- **Datadog، Splunk، Sumo Logic** (SaaS).
### چرخش گزارش (`logrotate`)
از پر کردن دیسک‌ها از لاگ‌ها جلوگیری کنید. پیکربندی `/etc/logrotate.d/myapp`:
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

## نظارت و هشدار
### معیارهایی برای نظارت
| دسته بندی | معیارهای کلیدی |
|----------|-------------|
| **سیستم** | CPU، RAM، مصرف دیسک، میانگین بارگذاری، شبکه ورودی/خروجی |
| **برنامه** | نرخ درخواست، تأخیر (p50، p95، p99)، میزان خطا، جلسات فعال |
| **پایگاه اطلاعاتی** | تعداد پرس و جو، پرس و جوهای کند، استفاده از استخر اتصال |
| **کسب و کار** | ثبت نام کاربر، نرخ تبدیل، درآمد |
### ابزار
- **Prometheus + Grafana**: پشته منبع باز استاندارد.
- **صادر کننده گره** برای معیارهای سیستم.
- **صادر کننده جعبه سیاه** برای در دسترس بودن نقطه پایانی.
- **Alertmanager** برای مسیریابی هشدار.
- **بومی ابر**: AWS CloudWatch، Azure Monitor، GCP Monitoring.
### نظارت بر زمان کار
- Pingdom، Statuspage، Better Uptime، Uptime Kuma (خود میزبان).
- بررسی های سلامت: نقطه پایانی`/health`را در معرض نمایش قرار دهید که در صورت سالم بودن سرویس، 200 را برمی گرداند.
---

## استراتژی های پشتیبان گیری
### قانون 3-2-1
- **3** کپی از داده ها.
- **2** انواع رسانه های مختلف (به عنوان مثال، SSD + نوار، یا محلی + ابر).
- **1** کپی خارج از سایت (به عنوان مثال، ابر یا مرکز داده از راه دور).
### انواع پشتیبان
| نوع | توضیحات | معامله |
|------|-------------|-----------|
| **کامل** | همه چیز را کپی کنید | آهسته، فضایی سنگین |
| **افزایشی** | کپی فقط تغییرات از آخرین کامل یا افزایشی | بازیابی سریع و پیچیده |
| **دیفرانسیل** | کپی تغییرات از آخرین بار | میانه |
### پشتیبان گیری از پایگاه داده
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

### پشتیبان گیری از فایل
```bash
# Tar archive
tar -czf backup.tar.gz /var/lib/data

# Rsync to remote
rsync -avz /local/data/ user@backup-server:/backup/data/

# Cloud CLI (e.g., AWS S3)
aws s3 sync /local/data s3://my-bucket/backup/
```

### برنامه ریزی خودکار پشتیبان گیری (cron)
```cron
# Run daily at 2am
0 2 * * * /usr/local/bin/backup_script.sh
```

---

## Cron and Scheduled Jobs
### Cron Syntax
```
* * * * * command
│ │ │ │ │
│ │ │ │ └─ Day of week (0-7, 0=Sun)
│ │ │ └─── Month (1-12)
│ │ └───── Day of month (1-31)
│ └─────── Hour (0-23)
└───────── Minute (0-59)
```

### مثالها
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

### مدیریت کرون
```bash
crontab -l          # List current user's cron jobs
crontab -e          # Edit
crontab -r          # Remove all
```

### آناکرون
برای سیستم هایی که 24/7 کار نمی کنند (به عنوان مثال، لپ تاپ ها) استفاده می شود. تضمین می کند که مشاغل در نهایت اجرا می شوند.
---

## مدیریت بسته و به روز رسانی
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

### به‌روزرسانی‌های امنیتی
`unattended-upgrades` را در اوبونتو برای وصله‌های امنیتی فعال کنید:
```bash
sudo apt install unattended-upgrades
sudo dpkg-reconfigure -plow unattended-upgrades
```

---

## داکر در حال تولید
### بهترین شیوه ها
- از برچسب های تصویر خاص (`python:3.12-slim`) استفاده کنید نه `latest`.
- کانتینرها را به عنوان کاربر غیر ریشه اجرا کنید.
- تصاویر را برای آسیب‌پذیری‌ها اسکن کنید (`docker scan`، `trivy`).
- محدودیت های منابع را تنظیم کنید (`--memory`، `--cpus`).
- از اسرار (از طریق Docker Secrets یا محیط با دقت) استفاده کنید.
- تصاویر را کوچک نگه دارید: ساخت های چند مرحله ای، پایه های آلپ.
### Docker Compose در حال تولید است
محدودیت منابع را در`docker-compose.yml`تنظیم کنید:
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

## اصول CI/CD
### مراحل خط لوله
| مرحله | توضیحات |
|-------|------------|
| **ساخت ** | کامپایل کد، نصب وابستگی |
| **تست** | بررسی واحد، ادغام و پرز |
| **ظروف** | ساخت تصویر داکر |
| **فشار ** | فشار دادن تصویر به رجیستری ظرف |
| **استقرار** | به روز رسانی محیط صحنه سازی/تولید |
### ابزار
| ابزار | یادداشت ها |
|------|-------|
| **اقدامات گیت هاب** | یکپارچه با GitHub |
| **GitLab CI** | ساخته شده در GitLab |
| **جنکینز** | سنتی، بسیار قابل تنظیم |
| **CircleCI، Travis CI** | شخص ثالث محبوب |
| **ArgoCD** | GitOps برای Kubernetes |
### مثال اکشن GitHub
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

## تنظیم و عیب یابی سیستم
### فضای دیسک را بررسی کنید
```bash
df -h                      # Human-readable disk usage
du -sh /* | sort -h        # Size of top-level directories
```

### میزان استفاده از حافظه را بررسی کنید
```bash
free -m                    # Memory in MB
vmstat 1 10                # Virtual memory statistics
top -o %MEM                # Sort processes by memory
```

### بار CPU را بررسی کنید
```bash
uptime                     # Load average over 1,5,15 minutes
top -o %CPU                # Sort processes by CPU
mpstat -P ALL 1 5          # Per-core CPU usage
```

### شبکه را بررسی کنید
```bash
netstat -i                 # Interface statistics
iftop                      # Live bandwidth usage (requires install)
nload                      # Another bandwidth monitor
```

### فایل های بزرگ را پیدا کنید
```bash
find / -type f -size +100M -exec ls -lh {} \; 2>/dev/null
```

---

## زیرساخت به عنوان کد (IaC)
### Terraform
منابع ابری را در HCL اعلام کنید.
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
مدیریت پیکربندی بدون عامل با استفاده از YAML.
```yaml
- name: Install nginx
  hosts: webservers
  tasks:
    - name: Install nginx
      apt:
        name: nginx
        state: present
```

### بهترین شیوه ها
- از ماژول ها و نقش ها برای قابلیت استفاده مجدد استفاده کنید.
- حالت ذخیره از راه دور (S3، Terraform Cloud).
- از متغیرها و اسرار استفاده کنید (`AWS_SECRET_ACCESS_KEY`از طریق محیط، نه کدگذاری شده).
- نسخه کنترل کد IaC شما.
---

## پاسخ به حادثه (در حال تماس)
### چک لیست برای قطع سرویس
1. هشدار را تصدیق کنید.
2. ارزیابی دامنه: کدام خدمات/کاربران تحت تأثیر قرار می گیرند؟
3. مشکل را شناسایی کنید (به گزارش‌ها، معیارها، استقرارهای اخیر نگاه کنید).
4. در صورت امکان شامل (شکن های مدار، پرچم های ویژگی).
5. عقب نشینی یا تعمیر به جلو.
6. ارتباط وضعیت با ذینفعان و کاربران (صفحه وضعیت).
7. جدول زمانی حادثه و اقدامات را مستند کنید.
8. پس از مرگ: ظرف 24 تا 48 ساعت، یک تجزیه و تحلیل علت ریشه ای (RCA) و موارد اقدام برای جلوگیری از عود بنویسید.