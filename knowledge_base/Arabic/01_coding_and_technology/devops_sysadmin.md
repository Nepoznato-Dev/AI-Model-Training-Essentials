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
# DevOps وإدارة النظام
دليل عملي لإدارة الخوادم، وأتمتة العمليات، والحفاظ على بنية تحتية موثوقة.
---

## SSH (الصدفة الآمنة)
### توليد المفاتيح
```bash
ssh-keygen -t ed25519 -C "your_email@example.com"   # Modern and secure
ssh-keygen -t rsa -b 4096 -C "your_email@example.com" # Fallback
```

### نسخ المفتاح العام إلى الخادم
```bash
ssh-copy-id user@host
# Manual alternative:
cat ~/.ssh/id_ed25519.pub | ssh user@host "mkdir -p ~/.ssh && cat >> ~/.ssh/authorized_keys"
```

### تكوين SSH (`~/.ssh/config`)
```
Host myserver
    HostName 192.168.1.10
    User ubuntu
    IdentityFile ~/.ssh/mykey
    Port 2222
```

### أوامر SSH الشائعة
```bash
ssh user@host                              # Connect
ssh -J jumpuser@jumphost user@target       # Proxy jump
scp file.txt user@host:/path/              # Copy file to remote
scp user@host:/path/file.txt .             # Copy from remote
rsync -avz -e ssh ./local/ user@host:/remote/  # Efficient sync
```

### تصلب SSH
- تعطيل تسجيل الدخول إلى الجذر:`PermitRootLogin no`
- استخدم المصادقة المستندة إلى المفتاح فقط:`PasswordAuthentication no`
- تغيير المنفذ الافتراضي (اختياري، الأمان من خلال الغموض).
- قم بتمكين`AllowUsers`أو`AllowGroups`لتقييد الوصول.
---

## Systemd (إدارة خدمات Linux)
### الأوامر المشتركة
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

### إنشاء وحدة خدمة systemd
إنشاء`/etc/systemd/system/myapp.service`:
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

ثم:
```bash
sudo systemctl daemon-reload
sudo systemctl enable myapp
sudo systemctl start myapp
```

---

## Journalctl (عرض السجلات)
```bash
journalctl -u myapp              # Logs for service
journalctl -f                    # Follow (tail) logs
journalctl --since "1 hour ago"
journalctl _PID=1234             # Filter by process ID
```

---

## استراتيجيات التسجيل
### التسجيل المنظم
استخدم تنسيق JSON لجعل السجلات قابلة للتحليل آليًا:
```python
import structlog
logger = structlog.get_logger()
logger.info("user_login", user_id=123, ip="192.168.1.1")
```

### مستويات السجل
| المستوى | الغرض |
|-------|---------|
| **التصحيح** | معلومات تشخيصية مفصلة |
| **معلومات** | الأحداث العامة (بدء، توقف، المعاملات العادية) |
| **تحذير** | غير متوقع ولكنه ليس قاتلا |
| **خطأ** | خطأ يمنع عملية معينة |
| **قاتل/حرج** | اغلاق النظام |
### تجميع السجل
- **ELK Stack** (Elasticsearch، Logstash، Kibana) أو Elastic Cloud.
- **Loki + Grafana** (بديل خفيف الوزن).
- ** Datadog، Splunk، Sumo Logic ** (SaaS).
### سجل التدوير (`logrotate`)
منع السجلات من ملء الأقراص. تكوين`/etc/logrotate.d/myapp`:
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

## الرصد والتنبيه
### المقاييس التي يجب مراقبتها
| الفئة | المقاييس الرئيسية |
|----------|------------|
| **النظام** | وحدة المعالجة المركزية، ذاكرة الوصول العشوائي، استخدام القرص، متوسط ​​التحميل، شبكة الإدخال / الإخراج |
| **التطبيق** | معدل الطلب، زمن الوصول (ص 50، ص 95، ص 99)، معدل الخطأ، الجلسات النشطة |
| **قاعدة البيانات** | عدد الاستعلامات، الاستعلامات البطيئة، استخدام تجمع الاتصال |
| **الأعمال** | اشتراكات المستخدم، معدل التحويل، الإيرادات |
### أدوات
- **Prometheus + Grafana**: مكدس قياسي مفتوح المصدر.
- **Node Exporter** لمقاييس النظام.
- **Blackbox Exporter** لتوفر نقطة النهاية.
- **Alertmanager** لتوجيه التنبيه.
- **السحابة الأصلية**: AWS CloudWatch، وAzure Monitor، ومراقبة GCP.
### مراقبة وقت التشغيل
- Pingdom، صفحة الحالة، وقت تشغيل أفضل، وقت التشغيل Kuma (مستضاف ذاتيًا).
- فحوصات الصحة: ​​كشف نقطة نهاية`/health`التي تُرجع 200 إذا كانت الخدمة سليمة.
---

## استراتيجيات النسخ الاحتياطي
### قاعدة 3-2-1
- **3** نسخ من البيانات.
- **2** أنواع مختلفة من الوسائط (على سبيل المثال، SSD + شريط، أو محلي + سحابي).
- **1** نسخة خارج الموقع (على سبيل المثال، مركز بيانات سحابي أو بعيد).
### أنواع النسخ الاحتياطية
| اكتب | الوصف | المفاضلة |
|------|------------|-----------|
| **كامل** | انسخ كل شيء | بطيئة، ثقيلة المساحة |
| **تزايدي** | انسخ التغييرات فقط منذ آخر تغييرات كاملة أو تزايدية | استعادة سريعة ومعقدة |
| **تفاضلية** | نسخ التغييرات منذ آخر نسخة كاملة | حل وسط |
### النسخ الاحتياطية لقاعدة البيانات
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

### النسخ الاحتياطية للملفات
```bash
# Tar archive
tar -czf backup.tar.gz /var/lib/data

# Rsync to remote
rsync -avz /local/data/ user@backup-server:/backup/data/

# Cloud CLI (e.g., AWS S3)
aws s3 sync /local/data s3://my-bucket/backup/
```

### جدولة النسخ الاحتياطي الآلي (كرون)
```cron
# Run daily at 2am
0 2 * * * /usr/local/bin/backup_script.sh
```

---

## وظائف كرون والمجدولة
### بناء جملة كرون
```
* * * * * command
│ │ │ │ │
│ │ │ │ └─ Day of week (0-7, 0=Sun)
│ │ │ └─── Month (1-12)
│ │ └───── Day of month (1-31)
│ └─────── Hour (0-23)
└───────── Minute (0-59)
```

### أمثلة
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

### إدارة كرون
```bash
crontab -l          # List current user's cron jobs
crontab -e          # Edit
crontab -r          # Remove all
```

### اناكرون
يُستخدم للأنظمة التي لا تعمل على مدار الساعة طوال أيام الأسبوع (مثل أجهزة الكمبيوتر المحمولة)؛ يضمن تشغيل الوظائف في نهاية المطاف.
---

## إدارة الحزم والتحديثات
### ديبيان/أوبونتو (`apt`)
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

### التحديثات الأمنية
قم بتمكين`unattended-upgrades`على Ubuntu لتصحيحات الأمان:
```bash
sudo apt install unattended-upgrades
sudo dpkg-reconfigure -plow unattended-upgrades
```

---

## عامل ميناء في الإنتاج
### أفضل الممارسات
- استخدم علامات صور محددة (`python:3.12-slim`) وليس `latest`.
- تشغيل الحاويات كمستخدم غير جذر.
- مسح الصور بحثًا عن نقاط الضعف (`docker scan`، `trivy`).
- تعيين حدود الموارد (`--memory`,`--cpus`).
- استخدم الأسرار (عبر أسرار Docker أو البيئة بعناية).
- إبقاء الصور صغيرة: بناءات متعددة المراحل، قاعدة جبال الألب.
### Docker Compose قيد الإنتاج
تعيين حدود الموارد في `docker-compose.yml`:
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

## أساسيات CI/CD
### مراحل خطوط الأنابيب
| المرحلة | الوصف |
|-------|------------|
| **بناء** | ترجمة التعليمات البرمجية وتثبيت التبعيات |
| **اختبار** | تشغيل الوحدة والتكامل وفحوصات الوبر |
| **حاويات** | بناء صورة عامل الميناء |
| **ادفع** | دفع الصورة إلى حاوية التسجيل |
| **نشر** | تحديث بيئة التدريج/الإنتاج |
### أدوات
| أداة | ملاحظات |
|------|-------|
| ** إجراءات جيثب ** | متكامل مع جيثب |
| **جيتلاب سي** | مدمج في GitLab |
| **جنكينز** | تقليدية وقابلة للتكوين بدرجة كبيرة |
| ** سيركل سي آي، ترافيس سي آي ** | شعبية طرف ثالث |
| **أرجو سي دي** | GitOps لـ Kubernetes |
### مثال على إجراء GitHub
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

## ضبط النظام واستكشاف الأخطاء وإصلاحها
### التحقق من مساحة القرص
```bash
df -h                      # Human-readable disk usage
du -sh /* | sort -h        # Size of top-level directories
```

### التحقق من استخدام الذاكرة
```bash
free -m                    # Memory in MB
vmstat 1 10                # Virtual memory statistics
top -o %MEM                # Sort processes by memory
```

### التحقق من تحميل وحدة المعالجة المركزية
```bash
uptime                     # Load average over 1,5,15 minutes
top -o %CPU                # Sort processes by CPU
mpstat -P ALL 1 5          # Per-core CPU usage
```

### فحص الشبكة
```bash
netstat -i                 # Interface statistics
iftop                      # Live bandwidth usage (requires install)
nload                      # Another bandwidth monitor
```

### البحث عن الملفات الكبيرة
```bash
find / -type f -size +100M -exec ls -lh {} \; 2>/dev/null
```

---

## البنية التحتية كرمز (IaC)
### تيرافورم
قم بتعريف الموارد السحابية في HCL.
```hcl
provider "aws" {
  region = "us-east-1"
}
resource "aws_instance" "web" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t2.micro"
}
```

### غير مقبول
إدارة التكوين بدون وكيل باستخدام YAML.
```yaml
- name: Install nginx
  hosts: webservers
  tasks:
    - name: Install nginx
      apt:
        name: nginx
        state: present
```

### أفضل الممارسات
- استخدام الوحدات والأدوار لإعادة الاستخدام.
- تخزين الحالة عن بعد (S3، Terraform Cloud).
- استخدم المتغيرات والأسرار (`AWS_SECRET_ACCESS_KEY` عبر البيئة، وليس ضمن التعليمات البرمجية).
- التحكم في الإصدار رمز IAC الخاص بك.
---

## الاستجابة للحوادث (عند الطلب)
### قائمة التحقق من انقطاع الخدمة
1. أقر التنبيه.
2. تقييم النطاق: ما هي الخدمات/المستخدمين المتأثرين؟
3. حدد المشكلة (انظر إلى السجلات والمقاييس وعمليات النشر الأخيرة).
4. تحتوي إن أمكن على (قواطع دوائر، أعلام مميزة).
5. التراجع أو الإصلاح للأمام.
6. قم بإبلاغ الحالة إلى أصحاب المصلحة والمستخدمين (صفحة الحالة).
7. توثيق الجدول الزمني للحادث والإجراءات.
8. بعد الوفاة: في غضون 24 إلى 48 ساعة، اكتب تحليل السبب الجذري (RCA) وعناصر العمل لمنع تكرارها.