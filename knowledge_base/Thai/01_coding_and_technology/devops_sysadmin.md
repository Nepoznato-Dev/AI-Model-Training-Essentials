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
# DevOps และการบริหารระบบ
คู่มือเชิงปฏิบัติในการจัดการเซิร์ฟเวอร์ การดำเนินการอัตโนมัติ และการบำรุงรักษาโครงสร้างพื้นฐานที่เชื่อถือได้
---

## SSH (เชลล์ปลอดภัย)
### การสร้างคีย์
```bash
ssh-keygen -t ed25519 -C "your_email@example.com"   # Modern and secure
ssh-keygen -t rsa -b 4096 -C "your_email@example.com" # Fallback
```

### คัดลอกรหัสสาธารณะไปยังเซิร์ฟเวอร์
```bash
ssh-copy-id user@host
# Manual alternative:
cat ~/.ssh/id_ed25519.pub | ssh user@host "mkdir -p ~/.ssh && cat >> ~/.ssh/authorized_keys"
```

### การกำหนดค่า SSH (`~/.ssh/config`)
```
Host myserver
    HostName 192.168.1.10
    User ubuntu
    IdentityFile ~/.ssh/mykey
    Port 2222
```

### คำสั่ง SSH ทั่วไป
```bash
ssh user@host                              # Connect
ssh -J jumpuser@jumphost user@target       # Proxy jump
scp file.txt user@host:/path/              # Copy file to remote
scp user@host:/path/file.txt .             # Copy from remote
rsync -avz -e ssh ./local/ user@host:/remote/  # Efficient sync
```

### SSH แข็งตัว
- ปิดการใช้งานการเข้าสู่ระบบรูท:`PermitRootLogin no`
- ใช้การตรวจสอบสิทธิ์แบบใช้คีย์เท่านั้น:`PasswordAuthentication no`
- เปลี่ยนพอร์ตเริ่มต้น (ไม่จำเป็น, การรักษาความปลอดภัยผ่านความสับสน)
- เปิดใช้งาน`AllowUsers`หรือ`AllowGroups`เพื่อจำกัดการเข้าถึง
---

## Systemd (การจัดการบริการ Linux)
### คำสั่งทั่วไป
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

### การสร้างหน่วยบริการ systemd
สร้าง`/etc/systemd/system/myapp.service`:
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

แล้ว:
```bash
sudo systemctl daemon-reload
sudo systemctl enable myapp
sudo systemctl start myapp
```

---

## Journalctl (ดูบันทึก)
```bash
journalctl -u myapp              # Logs for service
journalctl -f                    # Follow (tail) logs
journalctl --since "1 hour ago"
journalctl _PID=1234             # Filter by process ID
```

---

## กลยุทธ์การบันทึก
### การบันทึกแบบมีโครงสร้าง
ใช้รูปแบบ JSON เพื่อทำให้เครื่องบันทึกแยกวิเคราะห์ได้:
```python
import structlog
logger = structlog.get_logger()
logger.info("user_login", user_id=123, ip="192.168.1.1")
```

### ระดับการบันทึก
| ระดับ | วัตถุประสงค์ |
|-------|---------|
| **แก้ไขข้อบกพร่อง** | ข้อมูลการวินิจฉัยโดยละเอียด |
| **ข้อมูล** | เหตุการณ์ทั่วไป (เริ่ม, หยุด, ธุรกรรมปกติ) |
| **คำเตือน** | ไม่คาดคิดแต่ไม่ร้ายแรง |
| **ข้อผิดพลาด** | ข้อผิดพลาดที่ป้องกันการดำเนินการเฉพาะ |
| **ร้ายแรง/ร้ายแรง** | ปิดระบบ |
### การรวมบันทึก
- **ELK Stack** (Elasticsearch, Logstash, Kibana) หรือ Elastic Cloud
- **Loki + Grafana** (ทางเลือกที่มีน้ำหนักเบา)
- **Datadog, Splunk, ซูโม่ลอจิก** (SaaS)
### การหมุนบันทึก (`logrotate`)
ป้องกันบันทึกจากการเติมดิสก์ กำหนดค่า`/etc/logrotate.d/myapp`:
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

## การตรวจสอบและการแจ้งเตือน
### ตัวชี้วัดที่ต้องตรวจสอบ
| หมวดหมู่ | ตัวชี้วัดที่สำคัญ |
|----------|-------------|
| **ระบบ** | CPU, RAM, การใช้งานดิสก์, ค่าเฉลี่ยการโหลด, I/O เครือข่าย |
| **ใบสมัคร** | อัตราคำขอ เวลาแฝง (p50, p95, p99) อัตราข้อผิดพลาด เซสชันที่ใช้งาน |
| **ฐานข้อมูล** | จำนวนการสืบค้น การสืบค้นที่ช้า การใช้พูลการเชื่อมต่อ |
| **ธุรกิจ** | การสมัครสมาชิก อัตราการแปลง รายได้ |
### เครื่องมือ
- **Prometheus + Grafana**: สแต็กโอเพ่นซอร์สมาตรฐาน
- **ผู้ส่งออกโหนด** สำหรับการวัดระบบ
- **Blackbox Exporter** เพื่อความพร้อมใช้งานของปลายทาง
- **Alertmanager** สำหรับการกำหนดเส้นทางการแจ้งเตือน
- **เนทิฟคลาวด์**: AWS CloudWatch, Azure Monitor, การตรวจสอบ GCP
### การตรวจสอบสถานะการออนไลน์
- Pingdom, หน้าสถานะ, Better Uptime, Uptime Kuma (โฮสต์เอง)
- การตรวจสุขภาพ: เปิดเผยตำแหน่งข้อมูล`/health`ที่ส่งคืน 200 หากบริการมีประสิทธิภาพดี
---

## กลยุทธ์การสำรองข้อมูล
### กฎ 3-2-1
- **3** สำเนาข้อมูล
- **2** ประเภทสื่อที่แตกต่างกัน (เช่น SSD + เทป หรือโลคัล + คลาวด์)
- **1** คัดลอกนอกสถานที่ (เช่น คลาวด์หรือศูนย์ข้อมูลระยะไกล)
### ประเภทการสำรองข้อมูล
| พิมพ์ | คำอธิบาย | การแลกเปลี่ยน |
|------|-------------|-----------|
| **เต็ม** | คัดลอกทุกอย่าง | ช้า ใช้พื้นที่มาก |
| **ส่วนเพิ่ม** | คัดลอกเฉพาะการเปลี่ยนแปลงตั้งแต่ครั้งล่าสุด | แบบเต็มหรือส่วนเพิ่ม การกู้คืนที่รวดเร็วและซับซ้อน |
| **ส่วนต่าง** | คัดลอกการเปลี่ยนแปลงตั้งแต่ฉบับเต็มครั้งล่าสุด | พื้นกลาง |
### การสำรองฐานข้อมูล
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

### การสำรองข้อมูลไฟล์
```bash
# Tar archive
tar -czf backup.tar.gz /var/lib/data

# Rsync to remote
rsync -avz /local/data/ user@backup-server:/backup/data/

# Cloud CLI (e.g., AWS S3)
aws s3 sync /local/data s3://my-bucket/backup/
```

### กำหนดการสำรองข้อมูลอัตโนมัติ (cron)
```cron
# Run daily at 2am
0 2 * * * /usr/local/bin/backup_script.sh
```

---

## Cron และงานที่กำหนดเวลาไว้
### ไวยากรณ์ของครอน
```
* * * * * command
│ │ │ │ │
│ │ │ │ └─ Day of week (0-7, 0=Sun)
│ │ │ └─── Month (1-12)
│ │ └───── Day of month (1-31)
│ └─────── Hour (0-23)
└───────── Minute (0-59)
```

### ตัวอย่าง
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

### การจัดการ Cron
```bash
crontab -l          # List current user's cron jobs
crontab -e          # Edit
crontab -r          # Remove all
```

### อนาครอน
ใช้สำหรับระบบที่ไม่ได้ทำงานตลอด 24 ชั่วโมงทุกวัน (เช่น แล็ปท็อป) ช่วยให้มั่นใจว่างานดำเนินไปในที่สุด
---

## การจัดการแพ็คเกจและการอัปเดต
### เดเบียน/อูบุนตู (`apt`)
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

### การอัปเดตความปลอดภัย
เปิดใช้งาน`unattended-upgrades`บน Ubuntu สำหรับแพตช์ความปลอดภัย:
```bash
sudo apt install unattended-upgrades
sudo dpkg-reconfigure -plow unattended-upgrades
```

---

## นักเทียบท่าในการผลิต
### แนวทางปฏิบัติที่ดีที่สุด
- ใช้แท็กรูปภาพเฉพาะ (`python:3.12-slim`) ไม่ใช่ `latest`
- เรียกใช้คอนเทนเนอร์ในฐานะผู้ใช้ที่ไม่ใช่รูท
- สแกนภาพเพื่อหาช่องโหว่ (`docker scan`,`trivy`)
- ตั้งค่าขีดจำกัดทรัพยากร (`--memory`,`--cpus`)
- ใช้ความลับ (ผ่านความลับของนักเทียบท่าหรือสภาพแวดล้อมด้วยความระมัดระวัง)
- ทำให้รูปภาพมีขนาดเล็ก: การสร้างแบบหลายขั้นตอน, ฐานอัลไพน์
### นักเทียบท่าเขียนในการผลิต
ตั้งค่าขีดจำกัดทรัพยากรใน`docker-compose.yml`:
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

## พื้นฐาน CI/ซีดี
### ขั้นตอนไปป์ไลน์
| เวที | คำอธิบาย |
|-------|-------------|
| **สร้าง** | คอมไพล์โค้ด ติดตั้งการอ้างอิง |
| **ทดสอบ** | เรียกใช้หน่วย การรวม และการตรวจสอบผ้าสำลี |
| **ตู้คอนเทนเนอร์** | สร้างอิมเมจนักเทียบท่า |
| **ดัน** | พุชอิมเมจไปที่คอนเทนเนอร์รีจิสตรี |
| **ปรับใช้** | อัปเดตสภาพแวดล้อมการจัดเตรียม/การใช้งานจริง |
### เครื่องมือ
| เครื่องมือ | หมายเหตุ |
|-|-------|
| **การดำเนินการ GitHub** | บูรณาการกับ GitHub |
| **GitLab CI** | สร้างขึ้นใน GitLab |
| **เจนกินส์** | แบบดั้งเดิม กำหนดค่าได้สูง |
| **CircleCI, ทราวิส CI** | บุคคลที่สามยอดนิยม |
| **อาร์โกซีดี** | GitOps สำหรับ Kubernetes |
### ตัวอย่างการดำเนินการ GitHub
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

## การปรับแต่งระบบและการแก้ไขปัญหา
### ตรวจสอบพื้นที่ดิสก์
```bash
df -h                      # Human-readable disk usage
du -sh /* | sort -h        # Size of top-level directories
```

### ตรวจสอบการใช้หน่วยความจำ
```bash
free -m                    # Memory in MB
vmstat 1 10                # Virtual memory statistics
top -o %MEM                # Sort processes by memory
```

### ตรวจสอบโหลด CPU
```bash
uptime                     # Load average over 1,5,15 minutes
top -o %CPU                # Sort processes by CPU
mpstat -P ALL 1 5          # Per-core CPU usage
```

### ตรวจสอบเครือข่าย
```bash
netstat -i                 # Interface statistics
iftop                      # Live bandwidth usage (requires install)
nload                      # Another bandwidth monitor
```

### ค้นหาไฟล์ขนาดใหญ่
```bash
find / -type f -size +100M -exec ls -lh {} \; 2>/dev/null
```

---

## โครงสร้างพื้นฐานเป็นรหัส (IaC)
### เทอร์ราฟอร์ม
ประกาศทรัพยากรระบบคลาวด์ใน HCL
```hcl
provider "aws" {
  region = "us-east-1"
}
resource "aws_instance" "web" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t2.micro"
}
```

### วิเคราะห์ได้
การจัดการการกำหนดค่าแบบไร้ตัวแทนโดยใช้ YAML
```yaml
- name: Install nginx
  hosts: webservers
  tasks:
    - name: Install nginx
      apt:
        name: nginx
        state: present
```

### แนวทางปฏิบัติที่ดีที่สุด
- ใช้โมดูลและบทบาทเพื่อนำมาใช้ซ้ำ
- จัดเก็บสถานะจากระยะไกล (S3, Terraform Cloud)
- ใช้ตัวแปรและข้อมูลลับ (`AWS_SECRET_ACCESS_KEY`ผ่านสภาพแวดล้อม ไม่ใช่ฮาร์ดโค้ด)
- เวอร์ชันควบคุมรหัส IaC ของคุณ
---

## การตอบสนองต่อเหตุการณ์ (โทร)
### รายการตรวจสอบสำหรับการหยุดให้บริการ
1. รับทราบการแจ้งเตือน
2. ประเมินขอบเขต: บริการ/ผู้ใช้ใดบ้างที่ได้รับผลกระทบ?
3. ระบุปัญหา (ดูบันทึก ตัวชี้วัด การใช้งานล่าสุด)
4. บรรจุไว้หากเป็นไปได้ (เบรกเกอร์ แฟล็กคุณลักษณะ)
5. ย้อนกลับหรือแก้ไขไปข้างหน้า
6. สื่อสารสถานะไปยังผู้มีส่วนได้ส่วนเสียและผู้ใช้ (หน้าสถานะ)
7. บันทึกลำดับเวลาและการดำเนินการของเหตุการณ์
8. การชันสูตรพลิกศพ: ภายใน 24–48 ชั่วโมง ให้เขียนการวิเคราะห์สาเหตุที่แท้จริง (RCA) และรายการดำเนินการเพื่อป้องกันการเกิดซ้ำ