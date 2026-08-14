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
# DevOps at System Administration
Isang praktikal na gabay sa pamamahala ng mga server, pag-automate ng mga operasyon, at pagpapanatili ng maaasahang imprastraktura.
---

## SSH (Secure Shell)
### Key Generation
```bash
ssh-keygen -t ed25519 -C "your_email@example.com"   # Modern and secure
ssh-keygen -t rsa -b 4096 -C "your_email@example.com" # Fallback
```

### Kopyahin ang Public Key sa Server
```bash
ssh-copy-id user@host
# Manual alternative:
cat ~/.ssh/id_ed25519.pub | ssh user@host "mkdir -p ~/.ssh && cat >> ~/.ssh/authorized_keys"
```

### SSH Config (`~/.ssh/config`)
```
Host myserver
    HostName 192.168.1.10
    User ubuntu
    IdentityFile ~/.ssh/mykey
    Port 2222
```

### Mga Karaniwang Utos ng SSH
```bash
ssh user@host                              # Connect
ssh -J jumpuser@jumphost user@target       # Proxy jump
scp file.txt user@host:/path/              # Copy file to remote
scp user@host:/path/file.txt .             # Copy from remote
rsync -avz -e ssh ./local/ user@host:/remote/  # Efficient sync
```

### Pagpapatigas ng SSH
- Huwag paganahin ang root login:`PermitRootLogin no`
- Gumamit ng key-based na auth lang:`PasswordAuthentication no`
- Baguhin ang default na port (opsyonal, seguridad sa pamamagitan ng kalabuan).
- Paganahin ang`AllowUsers`o`AllowGroups`upang paghigpitan ang pag-access.
---

## Systemd (Pamamahala ng Serbisyo ng Linux)
### Mga Karaniwang Utos
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

### Paggawa ng isang Systemd Service Unit
Lumikha ng`/etc/systemd/system/myapp.service`:
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

Pagkatapos:
```bash
sudo systemctl daemon-reload
sudo systemctl enable myapp
sudo systemctl start myapp
```

---

## Journalctl (Tingnan ang Mga Log)
```bash
journalctl -u myapp              # Logs for service
journalctl -f                    # Follow (tail) logs
journalctl --since "1 hour ago"
journalctl _PID=1234             # Filter by process ID
```

---

## Mga Istratehiya sa Pag-log
### Nakabalangkas na Pag-log
Gumamit ng JSON na format upang gawing na-parseable ng makina ang mga log:
```python
import structlog
logger = structlog.get_logger()
logger.info("user_login", user_id=123, ip="192.168.1.1")
```

### Mga Antas ng Log
| Antas | Layunin |
|-------|---------|
| **DEBUG** | Detalyadong impormasyon sa diagnostic |
| **INFO** | Pangkalahatang mga kaganapan (pagsisimula, paghinto, mga normal na transaksyon) |
| **BABALA** | Hindi inaasahan ngunit hindi nakamamatay |
| **ERROR** | Error na pumipigil sa isang partikular na operasyon |
| **FATAL/KRITIKAL** | Pagsara ng system |
### Log Aggregation
- **ELK Stack** (Elasticsearch, Logstash, Kibana) o Elastic Cloud.
- **Loki + Grafana** (lightweight alternative).
- **Datadog, Splunk, Sumo Logic** (SaaS).
### Pag-ikot ng Log (`logrotate`)
Pigilan ang mga log mula sa pagpuno ng mga disk. I-configure ang`/etc/logrotate.d/myapp`:
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

## Pagsubaybay at Pag-alerto
### Mga Sukatan na Susubaybayan
| Kategorya | Mga Pangunahing Sukatan |
|----------|-------------|
| **System** | CPU, RAM, paggamit ng disk, average ng pag-load, network I/O |
| **Aplikasyon** | Rate ng kahilingan, latency (p50, p95, p99), rate ng error, aktibong session |
| **Database** | Bilang ng query, mabagal na query, paggamit ng pool ng koneksyon |
| **Negosyo** | Mga pag-signup ng user, rate ng conversion, kita |
### Mga tool
- **Prometheus + Grafana**: Karaniwang open-source stack.
- **Node Exporter** para sa mga sukatan ng system.
- **Blackbox Exporter** para sa availability ng endpoint.
- **Alertmanager** para sa pagruruta ng alerto.
- **Cloud native**: AWS CloudWatch, Azure Monitor, GCP Monitoring.
### Uptime na Pagsubaybay
- Pingdom, Statuspage, Better Uptime, Uptime Kuma (self-hosted).
- Mga pagsusuri sa kalusugan: ilantad ang isang`/health`na endpoint na nagbabalik ng 200 kung malusog ang serbisyo.
---

## Mga Istratehiya sa Pag-backup
### Ang 3-2-1 na Panuntunan
- **3** kopya ng data.
- **2** iba't ibang uri ng media (hal., SSD + tape, o lokal + cloud).
- **1** kopya sa labas ng site (hal., cloud o remote data center).
### Mga Uri ng Backup
| Uri | Paglalarawan | Trade-off |
|------|-------------|-----------|
| **Buong** | Kopyahin ang lahat | Mabagal, mabigat sa espasyo |
| **Incremental** | Kopyahin lamang ang mga pagbabago mula noong huling puno o incremental | Mabilis, kumplikadong pagpapanumbalik |
| **Differential** | Kopyahin ang mga pagbabago mula noong huling buong | Gitnang lupa |
### Mga Backup ng Database
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

### Mga Backup ng File
```bash
# Tar archive
tar -czf backup.tar.gz /var/lib/data

# Rsync to remote
rsync -avz /local/data/ user@backup-server:/backup/data/

# Cloud CLI (e.g., AWS S3)
aws s3 sync /local/data s3://my-bucket/backup/
```

### Automated Backup Scheduling (cron)
```cron
# Run daily at 2am
0 2 * * * /usr/local/bin/backup_script.sh
```

---

## Cron at Mga Naka-iskedyul na Trabaho
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

### Mga halimbawa
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

### Pamamahala ng Cron
```bash
crontab -l          # List current user's cron jobs
crontab -e          # Edit
crontab -r          # Remove all
```

### Anacron
Ginagamit para sa mga system na hindi tumatakbo 24/7 (hal., mga laptop); tinitiyak na ang mga trabaho ay tatakbo sa kalaunan.
---

## Pamamahala ng Package at Mga Update
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

### Mga Update sa Seguridad
Paganahin ang`unattended-upgrades`sa Ubuntu para sa mga patch ng seguridad:
```bash
sudo apt install unattended-upgrades
sudo dpkg-reconfigure -plow unattended-upgrades
```

---

## Docker sa Produksyon
### Pinakamahuhusay na Kasanayan
- Gumamit ng mga partikular na tag ng larawan (`python:3.12-slim`) hindi`latest`.
- Patakbuhin ang mga container bilang non-root user.
- I-scan ang mga larawan para sa mga kahinaan (`docker scan`,`trivy`).
- Magtakda ng mga limitasyon sa mapagkukunan (`--memory`,`--cpus`).
- Gumamit ng mga lihim (sa pamamagitan ng mga lihim ng Docker o kapaligiran nang may pag-iingat).
- Panatilihing maliit ang mga larawan: multi-stage build, alpine base.
### Docker Compose sa Production
Magtakda ng mga limitasyon sa mapagkukunan sa`docker-compose.yml`:
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

## Mga Pangunahing Kaalaman sa CI/CD
### Mga Yugto ng Pipeline
| Yugto | Paglalarawan |
|-------|-------------|
| **Bumuo** | Mag-compile ng code, mag-install ng mga dependencies |
| **Pagsubok** | Patakbuhin ang unit, integration, at lint checks |
| **Lalagyan** | Bumuo ng larawan ng Docker |
| **Tulak** | Itulak ang larawan sa container registry |
| **I-deploy** | I-update ang kapaligiran sa pagtatanghal ng dula/produksyon |
### Mga tool
| Tool | Mga Tala |
|------|-------|
| **Mga Pagkilos sa GitHub** | Pinagsama sa GitHub |
| **GitLab CI** | Built in sa GitLab |
| **Jenkins** | Tradisyonal, lubos na nako-configure |
| **CircleCI, Travis CI** | Sikat na third-party |
| **ArgoCD** | GitOps para sa Kubernetes |
### Halimbawa ng GitHub Action
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

## System Tuning at Troubleshooting
### Suriin ang Disk Space
```bash
df -h                      # Human-readable disk usage
du -sh /* | sort -h        # Size of top-level directories
```

### Suriin ang Paggamit ng Memory
```bash
free -m                    # Memory in MB
vmstat 1 10                # Virtual memory statistics
top -o %MEM                # Sort processes by memory
```

### Suriin ang Pag-load ng CPU
```bash
uptime                     # Load average over 1,5,15 minutes
top -o %CPU                # Sort processes by CPU
mpstat -P ALL 1 5          # Per-core CPU usage
```

### Suriin ang Network
```bash
netstat -i                 # Interface statistics
iftop                      # Live bandwidth usage (requires install)
nload                      # Another bandwidth monitor
```

### Maghanap ng Malalaking File
```bash
find / -type f -size +100M -exec ls -lh {} \; 2>/dev/null
```

---

## Imprastraktura bilang Code (IaC)
### Terraform
Ipahayag ang mga mapagkukunan ng ulap sa HCL.
```hcl
provider "aws" {
  region = "us-east-1"
}
resource "aws_instance" "web" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t2.micro"
}
```

### Magagawa
Pamamahala ng configuration na walang ahente gamit ang YAML.
```yaml
- name: Install nginx
  hosts: webservers
  tasks:
    - name: Install nginx
      apt:
        name: nginx
        state: present
```

### Pinakamahuhusay na Kasanayan
- Gumamit ng mga module at tungkulin para sa muling paggamit.
- Mag-imbak ng estado nang malayuan (S3, Terraform Cloud).
- Gumamit ng mga variable at lihim (`AWS_SECRET_ACCESS_KEY`sa pamamagitan ng kapaligiran, hindi hardcoded).
- Kontrolin ng bersyon ang iyong IaC code.
---

## Tugon sa Insidente (Nasa tawag)
### Checklist para sa Outage ng Serbisyo
1. Kilalanin ang alerto.
2. Tayahin ang saklaw: Aling mga serbisyo/user ang apektado?
3. Tukuyin ang isyu (tingnan ang mga log, sukatan, kamakailang pag-deploy).
4. Maglaman kung maaari (mga circuit breaker, tampok na mga flag).
5. Rollback o ayusin pasulong.
6. Makipagkomunika sa katayuan sa mga stakeholder at user (pahina ng katayuan).
7. Idokumento ang timeline ng insidente at mga aksyon.
8. Post-mortem: sa loob ng 24–48 oras, sumulat ng root cause analysis (RCA) at mga item ng aksyon upang maiwasan ang pag-ulit.