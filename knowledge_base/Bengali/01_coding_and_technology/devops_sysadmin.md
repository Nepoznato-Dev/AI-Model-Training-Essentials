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
# DevOps এবং সিস্টেম প্রশাসন
সার্ভার পরিচালনা, স্বয়ংক্রিয় ক্রিয়াকলাপ এবং নির্ভরযোগ্য অবকাঠামো বজায় রাখার জন্য একটি ব্যবহারিক গাইড।
---

## SSH (সিকিউর শেল)
### কী জেনারেশন
```bash
ssh-keygen -t ed25519 -C "your_email@example.com"   # Modern and secure
ssh-keygen -t rsa -b 4096 -C "your_email@example.com" # Fallback
```

### সার্ভারে পাবলিক কী কপি করুন
```bash
ssh-copy-id user@host
# Manual alternative:
cat ~/.ssh/id_ed25519.pub | ssh user@host "mkdir -p ~/.ssh && cat >> ~/.ssh/authorized_keys"
```

### SSH কনফিগ (`~/.ssh/config`)
```
Host myserver
    HostName 192.168.1.10
    User ubuntu
    IdentityFile ~/.ssh/mykey
    Port 2222
```

### সাধারণ SSH কমান্ড
```bash
ssh user@host                              # Connect
ssh -J jumpuser@jumphost user@target       # Proxy jump
scp file.txt user@host:/path/              # Copy file to remote
scp user@host:/path/file.txt .             # Copy from remote
rsync -avz -e ssh ./local/ user@host:/remote/  # Efficient sync
```

### SSH শক্ত করা
- রুট লগইন অক্ষম করুন:`PermitRootLogin no`
- শুধুমাত্র কী-ভিত্তিক প্রমাণীকরণ ব্যবহার করুন:`PasswordAuthentication no`
- ডিফল্ট পোর্ট পরিবর্তন করুন (ঐচ্ছিক, অস্পষ্টতার মাধ্যমে নিরাপত্তা)।
- অ্যাক্সেস সীমাবদ্ধ করতে`AllowUsers`বা`AllowGroups`সক্ষম করুন৷
---

## সিস্টেমড (লিনাক্স সার্ভিস ম্যানেজমেন্ট)
### কমন কমান্ড
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

### একটি সিস্টেমড সার্ভিস ইউনিট তৈরি করা
`/etc/systemd/system/myapp.service` তৈরি করুন:
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

তারপর:
```bash
sudo systemctl daemon-reload
sudo systemctl enable myapp
sudo systemctl start myapp
```

---

## Journalctl (লগ দেখুন)
```bash
journalctl -u myapp              # Logs for service
journalctl -f                    # Follow (tail) logs
journalctl --since "1 hour ago"
journalctl _PID=1234             # Filter by process ID
```

---

## লগিং কৌশল
### স্ট্রাকচার্ড লগিং
লগ মেশিন-পার্সেবল করতে JSON ফর্ম্যাট ব্যবহার করুন:
```python
import structlog
logger = structlog.get_logger()
logger.info("user_login", user_id=123, ip="192.168.1.1")
```

### লগ লেভেল
| স্তর | উদ্দেশ্য |
|-------|---------|
| **ডিবাগ** | বিস্তারিত ডায়াগনস্টিক তথ্য |
| **তথ্য** | সাধারণ ঘটনা (শুরু, বন্ধ, স্বাভাবিক লেনদেন) |
| **সতর্ক** | অপ্রত্যাশিত কিন্তু মারাত্মক নয় |
| **ত্রুটি** | ত্রুটি যা একটি নির্দিষ্ট অপারেশন বাধা দেয় |
| **মারাত্মক/গুরুত্বপূর্ণ** | সিস্টেম শাটডাউন |
### লগ অ্যাগ্রিগেশন
- **ELK স্ট্যাক** (Elasticsearch, Logstash, Kibana) বা ইলাস্টিক ক্লাউড।
- **লোকি + গ্রাফানা** (হালকা বিকল্প)।
- **ডেটাডগ, স্প্লঙ্ক, সুমো লজিক** (সাস)।
### লগ রোটেশন (`logrotate`)
ডিস্কগুলি পূরণ করা থেকে লগগুলিকে আটকান৷`/etc/logrotate.d/myapp`কনফিগার করুন:
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

## মনিটরিং এবং সতর্কতা
### মনিটর করার মেট্রিক্স
| বিভাগ | মূল মেট্রিক্স |
|------------|-------------|
| **সিস্টেম** | CPU, RAM, ডিস্ক ব্যবহার, লোড গড়, নেটওয়ার্ক I/O |
| **আবেদন** | অনুরোধের হার, বিলম্ব (p50, p95, p99), ত্রুটির হার, সক্রিয় সেশন |
| **ডাটাবেস** | ক্যোয়ারী গণনা, ধীরগতির প্রশ্ন, সংযোগ পুল ব্যবহার |
| **ব্যবসা** | ব্যবহারকারী সাইনআপ, রূপান্তর হার, রাজস্ব |
### টুলস
- **প্রমিথিউস + গ্রাফানা**: স্ট্যান্ডার্ড ওপেন সোর্স স্ট্যাক।
- সিস্টেম মেট্রিক্সের জন্য **নোড এক্সপোর্টার**।
- **ব্ল্যাকবক্স এক্সপোর্টার** এন্ডপয়েন্ট উপলব্ধতার জন্য।
- **সতর্ক ব্যবস্থাপক** সতর্কতা রাউটিং জন্য.
- **ক্লাউড নেটিভ**: AWS CloudWatch, Azure মনিটর, GCP মনিটরিং।
### আপটাইম মনিটরিং
- পিংডম, স্ট্যাটাসপেজ, বেটার আপটাইম, আপটাইম কুমা (স্ব-হোস্টেড)।
- স্বাস্থ্য পরীক্ষা: একটি`/health`শেষ পয়েন্ট প্রকাশ করুন যা 200 প্রদান করে যদি পরিষেবাটি স্বাস্থ্যকর হয়।
---

## ব্যাকআপ কৌশল
### 3-2-1 নিয়ম
- **3** ডেটার কপি।
- **2** বিভিন্ন ধরনের মিডিয়া (যেমন, SSD + টেপ, বা স্থানীয় + ক্লাউড)।
- **1** অফ-সাইট কপি করুন (যেমন, ক্লাউড বা রিমোট ডেটা সেন্টার)।
### ব্যাকআপ প্রকার
| প্রকার | বর্ণনা | বাণিজ্য বন্ধ |
|------|---------------|------------|
| **সম্পূর্ণ** | সবকিছু কপি | ধীর, স্থান-ভারী |
| **বৃদ্ধিমূলক** | শেষ পূর্ণ বা বৃদ্ধির পর থেকে শুধুমাত্র পরিবর্তনগুলি অনুলিপি করুন | দ্রুত, জটিল পুনরুদ্ধার |
| **পার্থক্য** | শেষ পূর্ণ থেকে পরিবর্তনগুলি অনুলিপি করুন | মধ্য স্থল |
### ডাটাবেস ব্যাকআপ
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

### ফাইল ব্যাকআপ
```bash
# Tar archive
tar -czf backup.tar.gz /var/lib/data

# Rsync to remote
rsync -avz /local/data/ user@backup-server:/backup/data/

# Cloud CLI (e.g., AWS S3)
aws s3 sync /local/data s3://my-bucket/backup/
```

### স্বয়ংক্রিয় ব্যাকআপ শিডিউলিং (ক্রন)
```cron
# Run daily at 2am
0 2 * * * /usr/local/bin/backup_script.sh
```

---

## ক্রোন এবং নির্ধারিত চাকরি
### ক্রোন সিনট্যাক্স
```
* * * * * command
│ │ │ │ │
│ │ │ │ └─ Day of week (0-7, 0=Sun)
│ │ │ └─── Month (1-12)
│ │ └───── Day of month (1-31)
│ └─────── Hour (0-23)
└───────── Minute (0-59)
```

### উদাহরণ
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

### ক্রোন পরিচালনা
```bash
crontab -l          # List current user's cron jobs
crontab -e          # Edit
crontab -r          # Remove all
```

### অ্যানাক্রন
24/7 চলমান না এমন সিস্টেমের জন্য ব্যবহৃত হয় (যেমন, ল্যাপটপ); কাজ শেষ পর্যন্ত চালানো নিশ্চিত করে।
---

## প্যাকেজ ব্যবস্থাপনা এবং আপডেট
### ডেবিয়ান/উবুন্টু (`apt`)
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

### নিরাপত্তা আপডেট
নিরাপত্তা প্যাচের জন্য উবুন্টুতে`unattended-upgrades`সক্ষম করুন:
```bash
sudo apt install unattended-upgrades
sudo dpkg-reconfigure -plow unattended-upgrades
```

---

## উৎপাদনে ডকার
### সর্বোত্তম অভ্যাস
- নির্দিষ্ট ইমেজ ট্যাগ ব্যবহার করুন (`python:3.12-slim`)`latest`নয়।
- নন-রুট ব্যবহারকারী হিসাবে পাত্র চালান।
- দুর্বলতার জন্য ছবি স্ক্যান করুন (`docker scan`, `trivy`)।
- সম্পদ সীমা সেট করুন (`--memory`,`--cpus`)।
- গোপনীয়তা ব্যবহার করুন (ডকার সিক্রেটস বা যত্ন সহ পরিবেশের মাধ্যমে)।
- ছবি ছোট রাখুন: মাল্টি-স্টেজ বিল্ড, আলপাইন বেস।
### উৎপাদনে ডকার কম্পোজ
`docker-compose.yml` এ সম্পদ সীমা সেট করুন:
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

## সিআই/সিডি বেসিক
### পাইপলাইনের পর্যায়
| মঞ্চ | বর্ণনা |
|-------|---------------|
| **বিল্ড** | কোড কম্পাইল করুন, নির্ভরতা ইনস্টল করুন |
| **পরীক্ষা** | ইউনিট, ইন্টিগ্রেশন এবং লিন্ট চেক চালান |
| **কন্টেইনারাইজ** | ডকার ইমেজ তৈরি করুন |
| **ধাক্কা** | কন্টেইনার রেজিস্ট্রিতে ছবি পুশ করুন |
| **মোতায়েন** | মঞ্চায়ন/উৎপাদন পরিবেশ আপডেট করুন |
### টুলস
| টুল | নোট |
|------|---------|
| **গিটহাব অ্যাকশন** | GitHub এর সাথে ইন্টিগ্রেটেড |
| **গিটল্যাব সিআই** | গিটল্যাবে নির্মিত |
| **জেনকিন্স** | ঐতিহ্যগত, অত্যন্ত কনফিগারযোগ্য |
| **সার্কেলসিআই, ট্র্যাভিস সিআই** | জনপ্রিয় তৃতীয় পক্ষ |
| **ArgoCD** | Kubernetes জন্য GitOps |
### উদাহরণ গিটহাব অ্যাকশন
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

## সিস্টেম টিউনিং এবং ট্রাবলশুটিং
### ডিস্ক স্পেস পরীক্ষা করুন
```bash
df -h                      # Human-readable disk usage
du -sh /* | sort -h        # Size of top-level directories
```

### মেমরির ব্যবহার পরীক্ষা করুন
```bash
free -m                    # Memory in MB
vmstat 1 10                # Virtual memory statistics
top -o %MEM                # Sort processes by memory
```

### CPU লোড চেক করুন
```bash
uptime                     # Load average over 1,5,15 minutes
top -o %CPU                # Sort processes by CPU
mpstat -P ALL 1 5          # Per-core CPU usage
```

### নেটওয়ার্ক চেক করুন
```bash
netstat -i                 # Interface statistics
iftop                      # Live bandwidth usage (requires install)
nload                      # Another bandwidth monitor
```

### বড় ফাইল খুঁজুন
```bash
find / -type f -size +100M -exec ls -lh {} \; 2>/dev/null
```

---

## কোড হিসাবে পরিকাঠামো (IaC)
### টেরাফর্ম
HCL-এ ক্লাউড রিসোর্স ঘোষণা করুন।
```hcl
provider "aws" {
  region = "us-east-1"
}
resource "aws_instance" "web" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t2.micro"
}
```

### উত্তরযোগ্য
YAML ব্যবহার করে এজেন্টলেস কনফিগারেশন ম্যানেজমেন্ট।
```yaml
- name: Install nginx
  hosts: webservers
  tasks:
    - name: Install nginx
      apt:
        name: nginx
        state: present
```

### সর্বোত্তম অভ্যাস
- পুনঃব্যবহারযোগ্যতার জন্য মডিউল এবং ভূমিকা ব্যবহার করুন।
- স্টেট রিমোটলি স্টোর করুন (S3, Terraform Cloud)।
- ভেরিয়েবল এবং গোপনীয়তা ব্যবহার করুন (`AWS_SECRET_ACCESS_KEY`পরিবেশের মাধ্যমে, হার্ডকোড নয়)।
- সংস্করণ আপনার IaC কোড নিয়ন্ত্রণ.
---

## ঘটনার প্রতিক্রিয়া (অন-কল)
### পরিষেবা বিভ্রাটের জন্য চেকলিস্ট
1. সতর্কতা স্বীকার করুন।
2. সুযোগ মূল্যায়ন: কোন পরিষেবা/ব্যবহারকারীরা প্রভাবিত হয়?
3. সমস্যাটি চিহ্নিত করুন (লগ, মেট্রিক্স, সাম্প্রতিক স্থাপনা দেখুন)।
4. সম্ভব হলে ধারণ করুন (সার্কিট ব্রেকার, বৈশিষ্ট্য পতাকা)।
5. রোলব্যাক বা এগিয়ে ঠিক করুন.
6. স্টেকহোল্ডার এবং ব্যবহারকারীদের সাথে যোগাযোগ করুন (স্থিতি পৃষ্ঠা)।
7. ঘটনার সময়রেখা এবং কর্ম নথিভুক্ত করুন।
8. পোস্ট-মর্টেম: 24-48 ঘন্টার মধ্যে, পুনরাবৃত্তি প্রতিরোধ করার জন্য একটি মূল কারণ বিশ্লেষণ (RCA) এবং অ্যাকশন আইটেম লিখুন।