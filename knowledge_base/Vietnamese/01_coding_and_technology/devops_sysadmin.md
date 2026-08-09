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
# DevOps và Quản trị hệ thống
Hướng dẫn thực tế để quản lý máy chủ, tự động hóa hoạt động và duy trì cơ sở hạ tầng đáng tin cậy.
---

## SSH (Vỏ bảo mật)
### Tạo khóa
```bash
ssh-keygen -t ed25519 -C "your_email@example.com"   # Modern and secure
ssh-keygen -t rsa -b 4096 -C "your_email@example.com" # Fallback
```

### Sao chép khóa công khai vào máy chủ
```bash
ssh-copy-id user@host
# Manual alternative:
cat ~/.ssh/id_ed25519.pub | ssh user@host "mkdir -p ~/.ssh && cat >> ~/.ssh/authorized_keys"
```

### Cấu hình SSH (`~/.ssh/config`)
```
Host myserver
    HostName 192.168.1.10
    User ubuntu
    IdentityFile ~/.ssh/mykey
    Port 2222
```

### Các lệnh SSH phổ biến
```bash
ssh user@host                              # Connect
ssh -J jumpuser@jumphost user@target       # Proxy jump
scp file.txt user@host:/path/              # Copy file to remote
scp user@host:/path/file.txt .             # Copy from remote
rsync -avz -e ssh ./local/ user@host:/remote/  # Efficient sync
```

### Tăng cường SSH
- Tắt đăng nhập root:`PermitRootLogin no`
- Chỉ sử dụng xác thực dựa trên khóa:`PasswordAuthentication no`
- Thay đổi cổng mặc định (tùy chọn, bảo mật thông qua che khuất).
- Bật`AllowUsers`hoặc`AllowGroups`để hạn chế quyền truy cập.
---

## Systemd (Quản lý dịch vụ Linux)
### Các lệnh thông dụng
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

### Tạo đơn vị dịch vụ systemd
Tạo`/etc/systemd/system/myapp.service`:
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

Sau đó:
```bash
sudo systemctl daemon-reload
sudo systemctl enable myapp
sudo systemctl start myapp
```

---

## Journalctl (Xem nhật ký)
```bash
journalctl -u myapp              # Logs for service
journalctl -f                    # Follow (tail) logs
journalctl --since "1 hour ago"
journalctl _PID=1234             # Filter by process ID
```

---

## Chiến lược ghi nhật ký
### Ghi nhật ký có cấu trúc
Sử dụng định dạng JSON để làm cho nhật ký có thể được phân tích cú pháp bằng máy:
```python
import structlog
logger = structlog.get_logger()
logger.info("user_login", user_id=123, ip="192.168.1.1")
```

### Cấp độ nhật ký
| Cấp độ | Mục đích |
|-------|----------|
| **GỠ LỖI** | Thông tin chẩn đoán chi tiết |
| **THÔNG TIN** | Sự kiện chung (bắt đầu, dừng, giao dịch thông thường) |
| **CẢNH BÁO** | Bất ngờ nhưng không gây tử vong |
| **LỖI** | Lỗi ngăn cản một hoạt động cụ thể |
| **TUYỆT VỜI/TUYỆT VỜI** | Tắt hệ thống |
### Tổng hợp nhật ký
- **ELK Stack** (Elasticsearch, Logstash, Kibana) hoặc Elastic Cloud.
- **Loki + Grafana** (thay thế nhẹ).
- **Datadog, Splunk, Sumo Logic** (SaaS).
### Xoay vòng nhật ký (`logrotate`)
Ngăn chặn nhật ký lấp đầy đĩa. Định cấu hình`/etc/logrotate.d/myapp`:
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

## Giám sát và cảnh báo
### Số liệu cần theo dõi
| Danh mục | Số liệu chính |
|----------|-------------|
| **Hệ thống** | CPU, RAM, mức sử dụng ổ đĩa, mức tải trung bình, I/O mạng |
| **Ứng tuyển** | Tỷ lệ yêu cầu, độ trễ (p50, p95, p99), tỷ lệ lỗi, phiên hoạt động |
| **Cơ sở dữ liệu** | Số lượng truy vấn, truy vấn chậm, mức sử dụng nhóm kết nối |
| **Kinh doanh** | Đăng ký người dùng, tỷ lệ chuyển đổi, doanh thu |
### Công cụ
- **Prometheus + Grafana**: Ngăn xếp mã nguồn mở tiêu chuẩn.
- **Trình xuất nút** cho số liệu hệ thống.
- **Trình xuất hộp đen** để biết tính khả dụng của điểm cuối.
- **Alertmanager** để định tuyến cảnh báo.
- **Bản địa của đám mây**: AWS CloudWatch, Azure Monitor, Giám sát GCP.
### Giám sát thời gian hoạt động
- Pingdom, Statuspage, Better Uptime, Uptime Kuma (tự lưu trữ).
- Kiểm tra tình trạng: hiển thị điểm cuối`/health`trả về 200 nếu dịch vụ hoạt động tốt.
---

## Chiến lược dự phòng
### Quy tắc 3-2-1
- **3** bản sao dữ liệu.
- **2** các loại phương tiện khác nhau (ví dụ: SSD + băng hoặc cục bộ + đám mây).
- **1** sao chép bên ngoài trang web (ví dụ: trung tâm dữ liệu đám mây hoặc từ xa).
### Các loại sao lưu
| Loại | Mô tả | Đánh đổi |
|------|-------------|----------|
| **Đầy đủ** | Sao chép mọi thứ | Chậm, nặng về không gian |
| **Gia tăng** | Chỉ sao chép các thay đổi kể từ lần cuối đầy đủ hoặc tăng dần | Khôi phục nhanh, phức tạp |
| **Khác biệt** | Sao chép các thay đổi kể từ bản đầy đủ gần đây nhất | Trung địa |
### Sao lưu cơ sở dữ liệu
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

### Sao lưu tệp
```bash
# Tar archive
tar -czf backup.tar.gz /var/lib/data

# Rsync to remote
rsync -avz /local/data/ user@backup-server:/backup/data/

# Cloud CLI (e.g., AWS S3)
aws s3 sync /local/data s3://my-bucket/backup/
```

### Lập kế hoạch sao lưu tự động (cron)
```cron
# Run daily at 2am
0 2 * * * /usr/local/bin/backup_script.sh
```

---

## Cron và công việc theo lịch trình
### Cú pháp Cron
```
* * * * * command
│ │ │ │ │
│ │ │ │ └─ Day of week (0-7, 0=Sun)
│ │ │ └─── Month (1-12)
│ │ └───── Day of month (1-31)
│ └─────── Hour (0-23)
└───────── Minute (0-59)
```

### Ví dụ
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

### Quản lý Cron
```bash
crontab -l          # List current user's cron jobs
crontab -e          # Edit
crontab -r          # Remove all
```

### Anacron
Được sử dụng cho các hệ thống không chạy 24/7 (ví dụ: máy tính xách tay); đảm bảo công việc được thực hiện cuối cùng.
---

## Quản lý và cập nhật gói
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

### Cập nhật bảo mật
Kích hoạt`unattended-upgrades`trên Ubuntu để có các bản vá bảo mật:
```bash
sudo apt install unattended-upgrades
sudo dpkg-reconfigure -plow unattended-upgrades
```

---

## Docker trong sản xuất
### Các phương pháp hay nhất
- Sử dụng thẻ hình ảnh cụ thể (`python:3.12-slim`) không phải`latest`.
- Chạy container với tư cách người dùng không phải root.
- Quét hình ảnh để tìm lỗ hổng (`docker scan`,`trivy`).
- Đặt giới hạn tài nguyên (`--memory`,`--cpus`).
- Sử dụng bí mật (thông qua bí mật Docker hoặc môi trường một cách cẩn thận).
- Giữ hình ảnh nhỏ: xây dựng nhiều tầng, chân núi cao.
### Docker Compose trong sản xuất
Đặt giới hạn tài nguyên trong`docker-compose.yml`:
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

## Thông tin cơ bản về CI/CD
### Các giai đoạn đường ống
| Sân khấu | Mô tả |
|-------|-------------|
| **Xây dựng** | Biên dịch mã, cài đặt phụ thuộc |
| **Kiểm tra** | Chạy kiểm tra đơn vị, tích hợp và tìm lỗi mã nguồn |
| **Containerise** | Xây dựng hình ảnh Docker |
| **Đẩy** | Đẩy hình ảnh vào sổ đăng ký container |
| **Triển khai** | Cập nhật môi trường dàn dựng/sản xuất |
### Công cụ
| Công cụ | Ghi chú |
|------|-------|
| **Hành động GitHub** | Tích hợp với GitHub |
| **CI GitLab** | Được tích hợp vào GitLab |
| **Jenkins** | Truyền thống, cấu hình cao |
| **CircleCI, Travis CI** | Bên thứ ba phổ biến |
| **ArgoCD** | GitOps cho Kubernetes |
### Ví dụ hành động GitHub
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

## Tinh chỉnh và khắc phục sự cố hệ thống
### Kiểm tra dung lượng ổ đĩa
```bash
df -h                      # Human-readable disk usage
du -sh /* | sort -h        # Size of top-level directories
```

### Kiểm tra việc sử dụng bộ nhớ
```bash
free -m                    # Memory in MB
vmstat 1 10                # Virtual memory statistics
top -o %MEM                # Sort processes by memory
```

### Kiểm tra tải CPU
```bash
uptime                     # Load average over 1,5,15 minutes
top -o %CPU                # Sort processes by CPU
mpstat -P ALL 1 5          # Per-core CPU usage
```

### Kiểm tra mạng
```bash
netstat -i                 # Interface statistics
iftop                      # Live bandwidth usage (requires install)
nload                      # Another bandwidth monitor
```

### Tìm tệp lớn
```bash
find / -type f -size +100M -exec ls -lh {} \; 2>/dev/null
```

---

## Cơ sở hạ tầng dưới dạng mã (IaC)
### Địa hình
Khai báo tài nguyên đám mây trong HCL.
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
Quản lý cấu hình không cần tác nhân bằng YAML.
```yaml
- name: Install nginx
  hosts: webservers
  tasks:
    - name: Install nginx
      apt:
        name: nginx
        state: present
```

### Các phương pháp hay nhất
- Sử dụng các module và vai trò để tái sử dụng.
- Lưu trữ trạng thái từ xa (S3, Terraform Cloud).
- Sử dụng các biến và bí mật (`AWS_SECRET_ACCESS_KEY`thông qua môi trường, không được mã hóa cứng).
- Phiên bản kiểm soát mã IaC của bạn.
---

## Ứng phó sự cố (Theo yêu cầu)
### Danh sách kiểm tra khi ngừng dịch vụ
1. Xác nhận cảnh báo.
2. Đánh giá phạm vi: Dịch vụ/người dùng nào bị ảnh hưởng?
3. Xác định vấn đề (xem nhật ký, số liệu, hoạt động triển khai gần đây).
4. Chứa nếu có thể (bộ ngắt mạch, cờ tính năng).
5. Quay lại hoặc sửa về phía trước.
6. Truyền đạt trạng thái cho các bên liên quan và người dùng (trang trạng thái).
7. Ghi lại dòng thời gian và hành động xảy ra sự cố.
8. Khám nghiệm tử thi: trong vòng 24–48 giờ, viết bản phân tích nguyên nhân gốc rễ (RCA) và các mục hành động để ngăn ngừa tái diễn.