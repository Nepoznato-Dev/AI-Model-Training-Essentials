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

# DevOps na Utawala wa Mfumo
Mwongozo wa vitendo wa kudhibiti seva, shughuli za kiotomatiki, na kudumisha miundombinu ya kuaminika.
---

## SSH (Shell Salama)
### Kizazi Muhimu
```bash
ssh-keygen -t ed25519 -C "your_email@example.com"   # Modern and secure
ssh-keygen -t rsa -b 4096 -C "your_email@example.com" # Fallback
```

### Nakili Ufunguo wa Umma kwa Seva
```bash
ssh-copy-id user@host
# Manual alternative:
cat ~/.ssh/id_ed25519.pub | ssh user@host "mkdir -p ~/.ssh && cat >> ~/.ssh/authorized_keys"
```

### Usanidi wa SSH (`~/.ssh/config`)
```
Host myserver
    HostName 192.168.1.10
    User ubuntu
    IdentityFile ~/.ssh/mykey
    Port 2222
```

### Amri za SSH za Kawaida
```bash
ssh user@host                              # Connect
ssh -J jumpuser@jumphost user@target       # Proxy jump
scp file.txt user@host:/path/              # Copy file to remote
scp user@host:/path/file.txt .             # Copy from remote
rsync -avz -e ssh ./local/ user@host:/remote/  # Efficient sync
```

### Inaimarisha SSH
- Lemaza kuingia kwa mizizi:`PermitRootLogin no`
- Tumia uthibitisho unaotegemea ufunguo pekee:`PasswordAuthentication no`
- Badilisha bandari chaguo-msingi (hiari, usalama kupitia kutokujulikana).
- Wezesha`AllowUsers`au`AllowGroups`ili kuzuia ufikiaji.
---

## Mfumo (Usimamizi wa Huduma ya Linux)
### Amri za Kawaida
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

### Kuunda Kitengo cha Huduma cha mfumo
Unda`/etc/systemd/system/myapp.service`:
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

Kisha:
```bash
sudo systemctl daemon-reload
sudo systemctl enable myapp
sudo systemctl start myapp
```

---

## Journalctl (Angalia Kumbukumbu)
```bash
journalctl -u myapp              # Logs for service
journalctl -f                    # Follow (tail) logs
journalctl --since "1 hour ago"
journalctl _PID=1234             # Filter by process ID
```

---

## Mikakati ya Kuweka Magogo
### Kuweka Magogo kwa Muundo
Tumia umbizo la JSON kufanya kumbukumbu ziweze kuchanganuliwa kwa mashine:
```python
import structlog
logger = structlog.get_logger()
logger.info("user_login", user_id=123, ip="192.168.1.1")
```

### Viwango vya kumbukumbu
| Kiwango | Kusudi |
|-------|---------|
| **TATUA** | Maelezo ya kina ya uchunguzi |
| **MAELEZO** | Matukio ya jumla (kuanza, kuacha, shughuli za kawaida) |
| **ONYA** | Isiyotarajiwa lakini sio mbaya |
| **KOSA** | Hitilafu inayozuia operesheni maalum |
| **KUFATA/KUKOSOA** | Kuzima kwa mfumo |
### Ukusanyaji wa Kumbukumbu
- **ELK Stack** (Elasticsearch, Logstash, Kibana) au Cloud Elastic.
- **Loki + Grafana** (mbadala nyepesi).
- **Datadog, Splunk, Sumo Logic** (SaaS).
### Mzunguko wa logi (`logrotate`)
Zuia kumbukumbu kutoka kwa kujaza diski. Sanidi`/etc/logrotate.d/myapp`:
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

## Ufuatiliaji na Tahadhari
### Vipimo vya Kufuatilia
| Kitengo | Vipimo Muhimu |
|----------|-------------|
| **Mfumo** | CPU, RAM, matumizi ya diski, wastani wa upakiaji, mtandao I/O |
| **Maombi** | Kiwango cha ombi, muda wa kusubiri (p50, p95, p99), kiwango cha makosa, vipindi vinavyotumika |
| ** Hifadhidata** | Idadi ya hoja, maswali ya polepole, matumizi ya bwawa la unganisho |
| **Biashara** | Usajili wa watumiaji, kiwango cha ubadilishaji, mapato |
### Zana
- **Prometheus + Grafana**: Rafu ya kawaida ya chanzo-wazi.
- **Msafirishaji wa Nodi** kwa vipimo vya mfumo.
- **Blackbox Exporter** kwa upatikanaji wa mwisho.
- **Kidhibiti Alert** kwa uelekezaji wa arifa.
- **Mwingu asili**: AWS CloudWatch, Azure Monitor, GCP Monitoring.
### Ufuatiliaji wa Wakati
- Pingdom, Statuspage, Bora Uptime, Uptime Kuma (self-hosted).
- Ukaguzi wa afya: onyesha mwisho wa`/health`ambao unarudisha 200 ikiwa huduma ni nzuri.
---

## Mikakati ya Hifadhi Nakala
### Kanuni ya 3-2-1
- **3** nakala za data.
- **2** aina tofauti za midia (k.m., SSD + mkanda, au + wingu la ndani).
- **1** nakili nje ya tovuti (k.m., wingu au kituo cha data cha mbali).
### Aina za Hifadhi Nakala
| Andika | Maelezo | Biashara |
|------|-------------|-----------|
| **Kamili** | Nakili kila kitu | Polepole, nafasi nzito |
| **Ongezeko** | Nakili tu mabadiliko tangu mwisho kamili au ya nyongeza | Haraka, urejeshaji tata |
| **Tofauti** | Nakili mabadiliko tangu mwisho kamili | Uwanja wa kati |
### Hifadhidata
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

### Hifadhi Nakala za Faili
```bash
# Tar archive
tar -czf backup.tar.gz /var/lib/data

# Rsync to remote
rsync -avz /local/data/ user@backup-server:/backup/data/

# Cloud CLI (e.g., AWS S3)
aws s3 sync /local/data s3://my-bucket/backup/
```

### Upangaji Nakala Kiotomatiki (cron)
```cron
# Run daily at 2am
0 2 * * * /usr/local/bin/backup_script.sh
```

---

## Cron na Kazi Zilizoratibiwa
### Sintaksia ya Cron
```
* * * * * command
│ │ │ │ │
│ │ │ │ └─ Day of week (0-7, 0=Sun)
│ │ │ └─── Month (1-12)
│ │ └───── Day of month (1-31)
│ └─────── Hour (0-23)
└───────── Minute (0-59)
```

### Mifano
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

### Kusimamia Cron
```bash
crontab -l          # List current user's cron jobs
crontab -e          # Edit
crontab -r          # Remove all
```

### Anacron
Inatumika kwa mifumo isiyoendesha 24/7 (kwa mfano, kompyuta ndogo); kuhakikisha kazi zinaendeshwa hatimaye.
---

## Usimamizi wa Kifurushi na Usasisho
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

### Masasisho ya Usalama
Washa`unattended-upgrades`kwenye Ubuntu kwa viraka vya usalama:
```bash
sudo apt install unattended-upgrades
sudo dpkg-reconfigure -plow unattended-upgrades
```

---

## Docker katika Uzalishaji
### Mbinu Bora
- Tumia tagi maalum za picha (`python:3.12-slim`) sio`latest`.
- Endesha vyombo kama mtumiaji asiye na mizizi.
- Changanua picha za udhaifu (`docker scan`,`trivy`).
- Weka mipaka ya rasilimali (`--memory`,`--cpus`).
- Tumia siri (kupitia siri za Docker au mazingira kwa uangalifu).
- Weka picha ndogo: ujenzi wa hatua nyingi, msingi wa alpine.
### Utungaji wa Docker katika Uzalishaji
Weka mipaka ya rasilimali katika`docker-compose.yml`:
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

## Misingi ya CI/CD
### Hatua za Bomba
| Jukwaa | Maelezo |
|-------|-------------|
| **Jenga** | Kusanya msimbo, sakinisha vitegemezi |
| **Mtihani** | Endesha kitengo, ujumuishaji, na ukaguzi wa pamba |
| ** Chombo ** | Jenga picha ya Docker |
| **sukuma** | Sukuma picha kwenye sajili ya kontena |
| **Weka** | Sasisha mazingira ya jukwaa/uzalishaji |
### Zana
| Zana | Vidokezo |
|------|-------|
| **Vitendo vya GitHub** | Imeunganishwa na GitHub |
| **GitLab CI** | Imejengwa ndani ya GitLab |
| **Jenkins** | Jadi, inaweza kusanidiwa sana |
| **CircleCI, Travis CI** | Maarufu kwa wahusika wengine |
| **ArgoCD** | GitOps kwa Kubernetes |
### Mfano Kitendo cha GitHub
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

## Marekebisho ya Mfumo na Utatuzi wa Matatizo
### Angalia Nafasi ya Disk
```bash
df -h                      # Human-readable disk usage
du -sh /* | sort -h        # Size of top-level directories
```

### Angalia Matumizi ya Kumbukumbu
```bash
free -m                    # Memory in MB
vmstat 1 10                # Virtual memory statistics
top -o %MEM                # Sort processes by memory
```

### Angalia Upakiaji wa CPU
```bash
uptime                     # Load average over 1,5,15 minutes
top -o %CPU                # Sort processes by CPU
mpstat -P ALL 1 5          # Per-core CPU usage
```

### Angalia Mtandao
```bash
netstat -i                 # Interface statistics
iftop                      # Live bandwidth usage (requires install)
nload                      # Another bandwidth monitor
```

### Tafuta Faili Kubwa
```bash
find / -type f -size +100M -exec ls -lh {} \; 2>/dev/null
```

---

## Miundombinu kama Kanuni (IaC)
### Mwonekano wa hali ya juu
Tangaza rasilimali za wingu katika HCL.
```hcl
provider "aws" {
  region = "us-east-1"
}
resource "aws_instance" "web" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t2.micro"
}
```

### Inastahili
Usimamizi wa usanidi bila wakala kwa kutumia YAML.
```yaml
- name: Install nginx
  hosts: webservers
  tasks:
    - name: Install nginx
      apt:
        name: nginx
        state: present
```

### Mbinu Bora
- Tumia moduli na majukumu kwa reusability.
- Hifadhi hali kwa mbali (S3, Terraform Cloud).
- Tumia vigezo na siri (`AWS_SECRET_ACCESS_KEY`kupitia mazingira, sio ngumu).
- Toleo kudhibiti msimbo wako wa IaC.
---

## Mwitikio wa Tukio (On-call)
### Orodha ya Hakiki ya Kukatika kwa Huduma
1. Thibitisha tahadhari.
2. Tathmini upeo: Ni huduma/watumiaji gani wameathirika?
3. Tambua suala (angalia kumbukumbu, vipimo, uwekaji wa hivi majuzi).
4. Vyenye ikiwezekana (wavunjaji wa mzunguko, bendera za kipengele).
5. Rollback au kurekebisha mbele.
6. Kuwasilisha hali kwa wadau na watumiaji (ukurasa wa hali).
7. Andika kalenda ya matukio na vitendo.
8. Uchunguzi wa baada ya maiti: ndani ya saa 24-48, andika uchanganuzi wa sababu ya mizizi (RCA) na hatua za kuzuia kujirudia.