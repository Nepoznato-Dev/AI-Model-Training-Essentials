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
# DevOps और सिस्टम प्रशासन
सर्वरों को प्रबंधित करने, संचालन को स्वचालित करने और विश्वसनीय बुनियादी ढांचे को बनाए रखने के लिए एक व्यावहारिक मार्गदर्शिका।
---

## एसएसएच (सुरक्षित शैल)
### प्रमुख पीढ़ी
```bash
ssh-keygen -t ed25519 -C "your_email@example.com"   # Modern and secure
ssh-keygen -t rsa -b 4096 -C "your_email@example.com" # Fallback
```

### सार्वजनिक कुंजी को सर्वर पर कॉपी करें
```bash
ssh-copy-id user@host
# Manual alternative:
cat ~/.ssh/id_ed25519.pub | ssh user@host "mkdir -p ~/.ssh && cat >> ~/.ssh/authorized_keys"
```

### एसएसएच कॉन्फ़िगरेशन (__संरक्षित_0__)
```
Host myserver
    HostName 192.168.1.10
    User ubuntu
    IdentityFile ~/.ssh/mykey
    Port 2222
```

### सामान्य एसएसएच कमांड
```bash
ssh user@host                              # Connect
ssh -J jumpuser@jumphost user@target       # Proxy jump
scp file.txt user@host:/path/              # Copy file to remote
scp user@host:/path/file.txt .             # Copy from remote
rsync -avz -e ssh ./local/ user@host:/remote/  # Efficient sync
```

### एसएसएच को सख्त बनाना
- रूट लॉगिन अक्षम करें:`PermitRootLogin no`
- केवल कुंजी-आधारित प्रमाणीकरण का उपयोग करें:`PasswordAuthentication no`
- डिफ़ॉल्ट पोर्ट बदलें (वैकल्पिक, अस्पष्टता के माध्यम से सुरक्षा)।
- पहुंच प्रतिबंधित करने के लिए`AllowUsers`या`AllowGroups`सक्षम करें।
---

## सिस्टमड (लिनक्स सेवा प्रबंधन)
### सामान्य आदेश
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

### एक सिस्टमड सर्विस यूनिट बनाना
`/etc/systemd/system/myapp.service` बनाएं:
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

तब:
```bash
sudo systemctl daemon-reload
sudo systemctl enable myapp
sudo systemctl start myapp
```

---

## जर्नलक्टल (लॉग देखें)
```bash
journalctl -u myapp              # Logs for service
journalctl -f                    # Follow (tail) logs
journalctl --since "1 hour ago"
journalctl _PID=1234             # Filter by process ID
```

---

## लॉगिंग रणनीतियाँ
### संरचित लॉगिंग
लॉग को मशीन-पार्सेबल बनाने के लिए JSON प्रारूप का उपयोग करें:
```python
import structlog
logger = structlog.get_logger()
logger.info("user_login", user_id=123, ip="192.168.1.1")
```

### लॉग स्तर
| स्तर | उद्देश्य |
|------|------|
| **डीबग** | विस्तृत निदान संबंधी जानकारी |
| **जानकारी** | सामान्य घटनाएँ (प्रारंभ, रोकें, सामान्य लेनदेन) |
| **चेतावनी** | अप्रत्याशित लेकिन घातक नहीं |
| **त्रुटि** | त्रुटि जो एक विशिष्ट ऑपरेशन को रोकती है |
| **घातक/गंभीर** | सिस्टम शटडाउन |
### लॉग एकत्रीकरण
- **ईएलके स्टैक** (इलास्टिकसर्च, लॉगस्टैश, किबाना) या इलास्टिक क्लाउड।
- **लोकी + ग्राफाना** (हल्का विकल्प)।
- **डेटाडॉग, स्प्लंक, सूमो लॉजिक** (सास)।
### लॉग रोटेशन (`logrotate`)
लॉग को डिस्क भरने से रोकें। कॉन्फ़िगर करें`/etc/logrotate.d/myapp`:
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

## निगरानी और चेतावनी
### मॉनिटर करने के लिए मेट्रिक्स
| श्रेणी | मुख्य मेट्रिक्स |
|---|----|
| **सिस्टम** | सीपीयू, रैम, डिस्क उपयोग, लोड औसत, नेटवर्क I/O |
| **आवेदन** | अनुरोध दर, विलंबता (पी50, पी95, पी99), त्रुटि दर, सक्रिय सत्र |
| **डेटाबेस** | क्वेरी गिनती, धीमी क्वेरी, कनेक्शन पूल उपयोग |
| **व्यापार** | उपयोगकर्ता साइनअप, रूपांतरण दर, राजस्व |
### औजार
- **प्रोमेथियस + ग्राफाना**: मानक ओपन-सोर्स स्टैक।
- **नोड एक्सपोर्टर** सिस्टम मेट्रिक्स के लिए।
- **एंडपॉइंट उपलब्धता के लिए ब्लैकबॉक्स निर्यातक**।
- अलर्ट रूटिंग के लिए **अलर्टमैनेजर**।
- **क्लाउड नेटिव**: एडब्ल्यूएस क्लाउडवॉच, एज़्योर मॉनिटर, जीसीपी मॉनिटरिंग।
### अपटाइम मॉनिटरिंग
- पीएसटीआई, स्टेटसपेज, बेहतर अपटाइम, अपटाइम कुमा (स्व-होस्टेड)।
- स्वास्थ्य जांच: एक`/health`समापन बिंदु को उजागर करें जो सेवा स्वस्थ होने पर 200 लौटाता है।
---

## बैकअप रणनीतियाँ
### 3-2-1 नियम
- डेटा की **3** प्रतियां।
- **2** विभिन्न मीडिया प्रकार (जैसे, एसएसडी + टेप, या स्थानीय + क्लाउड)।
- **1** कॉपी ऑफ-साइट (उदाहरण के लिए, क्लाउड या रिमोट डेटा सेंटर)।
### बैकअप प्रकार
| प्रकार | विवरण | व्यापार-बंद |
|------|----|----|
| **पूर्ण** | सब कुछ कॉपी करें | धीमा, अंतरिक्ष-भारी |
| **वृद्धिशील** | केवल पिछले पूर्ण या वृद्धिशील परिवर्तनों की प्रतिलिपि बनाएँ | तेज़, जटिल पुनर्स्थापना |
| **विभेदक** | पिछले पूर्ण से परिवर्तन कॉपी करें | मध्य मैदान |
### डेटाबेस बैकअप
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

### फ़ाइल बैकअप
```bash
# Tar archive
tar -czf backup.tar.gz /var/lib/data

# Rsync to remote
rsync -avz /local/data/ user@backup-server:/backup/data/

# Cloud CLI (e.g., AWS S3)
aws s3 sync /local/data s3://my-bucket/backup/
```

### स्वचालित बैकअप शेड्यूलिंग (क्रोन)
```cron
# Run daily at 2am
0 2 * * * /usr/local/bin/backup_script.sh
```

---

## क्रॉन और अनुसूचित नौकरियाँ
### क्रॉन सिंटैक्स
```
* * * * * command
│ │ │ │ │
│ │ │ │ └─ Day of week (0-7, 0=Sun)
│ │ │ └─── Month (1-12)
│ │ └───── Day of month (1-31)
│ └─────── Hour (0-23)
└───────── Minute (0-59)
```

### उदाहरण
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

### क्रॉन का प्रबंधन
```bash
crontab -l          # List current user's cron jobs
crontab -e          # Edit
crontab -r          # Remove all
```

### एनाक्रॉन
24/7 नहीं चलने वाले सिस्टम के लिए उपयोग किया जाता है (उदाहरण के लिए, लैपटॉप); यह सुनिश्चित करता है कि नौकरियाँ अंततः चलती रहें।
---

## पैकेज प्रबंधन और अपडेट
### डेबियन/उबंटू (`apt`)
```bash
sudo apt update                # Update package list
sudo apt upgrade               # Upgrade all packages
sudo apt install git nginx
sudo apt remove git
sudo apt autoremove            # Remove unused dependencies
```

### आरएचईएल/सेंटओएस/फेडोरा (`dnf` / `yum`)
```bash
sudo dnf check-update
sudo dnf update
sudo dnf install git nginx
sudo dnf remove git
```

### सुरक्षा अद्यतन
सुरक्षा पैच के लिए Ubuntu पर`unattended-upgrades`सक्षम करें:
```bash
sudo apt install unattended-upgrades
sudo dpkg-reconfigure -plow unattended-upgrades
```

---

## उत्पादन में डॉकर
### सर्वोत्तम प्रथाएं
- विशिष्ट छवि टैग (`python:3.12-slim`) का उपयोग करें, न कि`latest`का।
- कंटेनरों को गैर-रूट उपयोगकर्ता के रूप में चलाएँ।
- कमजोरियों के लिए छवियों को स्कैन करें (`docker scan`, `trivy`)।
- संसाधन सीमाएँ निर्धारित करें (`--memory` ,`--cpus`)।
- रहस्यों का उपयोग करें (डॉकर रहस्यों या पर्यावरण के माध्यम से सावधानी से)।
- छवियाँ छोटी रखें: मल्टी-स्टेज बिल्ड, अल्पाइन बेस।
### डॉकर कंपोज़ इन प्रोडक्शन
`docker-compose.yml` में संसाधन सीमाएँ निर्धारित करें:
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

## सीआई/सीडी मूल बातें
### पाइपलाइन चरण
| स्टेज | विवरण |
|-------|----||
| **निर्माण** | कोड संकलित करें, निर्भरताएँ स्थापित करें |
| **टेस्ट** | इकाई, एकीकरण और लिंट जाँच चलाएँ |
| **कंटेनराइज़** | डॉकर छवि बनाएं |
| **धक्का** | कंटेनर रजिस्ट्री में छवि पुश करें |
| **तैनाती** | अद्यतन स्टेजिंग/उत्पादन वातावरण |
### औजार
| उपकरण | नोट्स |
|------|-------|
| **गिटहब क्रियाएँ** | GitHub के साथ एकीकृत |
| **गिटलैब सीआई** | GitLab में निर्मित |
| **जेनकींस** | पारंपरिक, अत्यधिक विन्यास योग्य |
| **सर्किलसीआई, ट्रैविस सीआई** | लोकप्रिय तृतीय पक्ष |
| **आर्गोसीडी** | कुबेरनेट्स के लिए GitOps |
### उदाहरण GitHub कार्रवाई
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

## सिस्टम ट्यूनिंग और समस्या निवारण
### डिस्क स्थान की जाँच करें
```bash
df -h                      # Human-readable disk usage
du -sh /* | sort -h        # Size of top-level directories
```

### मेमोरी उपयोग की जाँच करें
```bash
free -m                    # Memory in MB
vmstat 1 10                # Virtual memory statistics
top -o %MEM                # Sort processes by memory
```

### सीपीयू लोड की जाँच करें
```bash
uptime                     # Load average over 1,5,15 minutes
top -o %CPU                # Sort processes by CPU
mpstat -P ALL 1 5          # Per-core CPU usage
```

### नेटवर्क जांचें
```bash
netstat -i                 # Interface statistics
iftop                      # Live bandwidth usage (requires install)
nload                      # Another bandwidth monitor
```

### बड़ी फ़ाइलें ढूंढें
```bash
find / -type f -size +100M -exec ls -lh {} \; 2>/dev/null
```

---

## कोड के रूप में इन्फ्रास्ट्रक्चर (IaC)
### टेराफॉर्म
एचसीएल में क्लाउड संसाधनों की घोषणा करें।
```hcl
provider "aws" {
  region = "us-east-1"
}
resource "aws_instance" "web" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t2.micro"
}
```

### उत्तर देने योग्य
YAML का उपयोग करके एजेंट रहित कॉन्फ़िगरेशन प्रबंधन।
```yaml
- name: Install nginx
  hosts: webservers
  tasks:
    - name: Install nginx
      apt:
        name: nginx
        state: present
```

### सर्वोत्तम प्रथाएं
- पुन: प्रयोज्यता के लिए मॉड्यूल और भूमिकाओं का उपयोग करें।
- स्टोर स्थिति को दूरस्थ रूप से (S3, टेराफॉर्म क्लाउड)।
- चर और रहस्यों का उपयोग करें (पर्यावरण के माध्यम से `AWS_SECRET_ACCESS_KEY`, हार्डकोडेड नहीं)।
- संस्करण आपके IaC कोड को नियंत्रित करता है।
---

## घटना प्रतिक्रिया (ऑन-कॉल)
### सेवा आउटेज के लिए चेकलिस्ट
1. अलर्ट स्वीकार करें.
2. दायरे का आकलन करें: कौन सी सेवाएँ/उपयोगकर्ता प्रभावित हैं?
3. समस्या की पहचान करें (लॉग, मेट्रिक्स, हालिया तैनाती देखें)।
4. यदि संभव हो तो (सर्किट ब्रेकर, फीचर फ़्लैग) शामिल करें।
5. रोलबैक करें या आगे की ओर ठीक करें।
6. हितधारकों और उपयोगकर्ताओं को स्थिति के बारे में बताएं (स्थिति पृष्ठ)।
7. घटना की समय-सीमा और कार्रवाइयों का दस्तावेजीकरण करें।
8. पोस्टमार्टम: 24-48 घंटों के भीतर, पुनरावृत्ति को रोकने के लिए मूल कारण विश्लेषण (आरसीए) और कार्रवाई आइटम लिखें।