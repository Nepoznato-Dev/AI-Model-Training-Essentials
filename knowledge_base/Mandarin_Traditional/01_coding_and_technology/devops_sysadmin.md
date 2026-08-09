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

# DevOps 和系統管理
管理伺服器、自動化操作和維護可靠基礎架構的實用指南。
---

## SSH（安全殼）
### 金鑰生成
```bash
ssh-keygen -t ed25519 -C "your_email@example.com"   # Modern and secure
ssh-keygen -t rsa -b 4096 -C "your_email@example.com" # Fallback
```

### 將公鑰複製到伺服器
```bash
ssh-copy-id user@host
# Manual alternative:
cat ~/.ssh/id_ed25519.pub | ssh user@host "mkdir -p ~/.ssh && cat >> ~/.ssh/authorized_keys"
```

### SSH 設定 (`~/.ssh/config`)
```
Host myserver
    HostName 192.168.1.10
    User ubuntu
    IdentityFile ~/.ssh/mykey
    Port 2222
```

### 常用 SSH 指令
```bash
ssh user@host                              # Connect
ssh -J jumpuser@jumphost user@target       # Proxy jump
scp file.txt user@host:/path/              # Copy file to remote
scp user@host:/path/file.txt .             # Copy from remote
rsync -avz -e ssh ./local/ user@host:/remote/  # Efficient sync
```

### 強化 SSH
- 停用root登入：`PermitRootLogin no`
- 僅使用基於金鑰的驗證：`PasswordAuthentication no`
- 更改預設連接埠（可選，透過隱藏實現安全性）。
- 啟用`AllowUsers`或`AllowGroups`以限制存取。
---

## Systemd（Linux 服務管理）
### 常用指令
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

### 建立 systemd 服務單元
建立`/etc/systemd/system/myapp.service`：
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

然後：
```bash
sudo systemctl daemon-reload
sudo systemctl enable myapp
sudo systemctl start myapp
```

---

## Journalctl（查看日誌）
```bash
journalctl -u myapp              # Logs for service
journalctl -f                    # Follow (tail) logs
journalctl --since "1 hour ago"
journalctl _PID=1234             # Filter by process ID
```

---

## 日誌記錄策略
### 結構化日誌記錄
使用 JSON 格式使日誌可供機器解析：
```python
import structlog
logger = structlog.get_logger()
logger.info("user_login", user_id=123, ip="192.168.1.1")
```

### 日誌級別
|水平|目的|
|--------|---------|
| **調試** |詳細診斷資訊|
| **資訊** |一般事件（開始、停止、正常交易） |
| **警告** |意外但非致命|
| **錯誤** |阻止特定操作的錯誤 |
| **致命/嚴重** |系統關閉|
### 日誌聚合
- **ELK Stack**（Elasticsearch、Logstash、Kibana）或 Elastic Cloud。
- **Loki + Grafana**（輕量級替代方案）。
- **Datadog、Splunk、Sumo Logic** (SaaS)。
### 日誌旋轉 (`logrotate`)
防止日志填满磁盘。配置`/etc/logrotate.d/myapp`：
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

## 監控和警報
### 監控指標
|類別 |關鍵指標|
|----------|-------------|
| **系統** | CPU、RAM、磁碟使用率、平均負載、網路 I/O |
| **應用程式** |請求率、延遲（p50、p95、p99）、錯誤率、活動會話 |
| **資料庫** |查詢計數、慢查詢、連線池使用情況 |
| **業務** |用戶註冊、轉換率、收入 |
＃＃＃ 工具
- **Prometheus + Grafana**：標準開源堆疊。
- 用於系統指標的**節點導出器**。
- **Blackbox Exporter** 用於端點可用性。
- **Alertmanager** 用於警報路由。
- **雲端原生**：AWS CloudWatch、Azure Monitor、GCP 監控。
### 正常運作時間監控
- Pingdom、Statuspage、Better Uptime、Uptime Kuma（自架）。
- 執行狀況檢查：公開`/health`端點，如果服務運作狀況良好，則傳回 200。
---

## 備份策略
### 3-2-1 規則
- **3** 資料副本。
- **2** 不同的媒體類型（例如 SSD + 磁帶，或本地 + 雲端）。
- **1** 異地複製（例如雲端或遠端資料中心）。
### 備份類型
|類型 |描述 |權衡|
|------|-------------|------------|
| **完整** |複製所有內容 |速度慢，空間大|
| **增量** |僅複製自上次完整或增量以來的更改 |快速、複雜的恢復 |
| **差速器** |複製自上次完整以來的更改 |中間立場|
### 資料庫備份
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

### 檔案備份
```bash
# Tar archive
tar -czf backup.tar.gz /var/lib/data

# Rsync to remote
rsync -avz /local/data/ user@backup-server:/backup/data/

# Cloud CLI (e.g., AWS S3)
aws s3 sync /local/data s3://my-bucket/backup/
```

### 自動備份計畫 (cron)
```cron
# Run daily at 2am
0 2 * * * /usr/local/bin/backup_script.sh
```

---

## Cron 和計畫作業
### Cron 語法
```
* * * * * command
│ │ │ │ │
│ │ │ │ └─ Day of week (0-7, 0=Sun)
│ │ │ └─── Month (1-12)
│ │ └───── Day of month (1-31)
│ └─────── Hour (0-23)
└───────── Minute (0-59)
```

### 範例
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

### 管理 Cron
```bash
crontab -l          # List current user's cron jobs
crontab -e          # Edit
crontab -r          # Remove all
```

### 阿納克朗
用於非 24/7 運作的系統（例如筆記型電腦）；確保作業最終運作。
---

## 套件管理與更新
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

### 安全性更新
在 Ubuntu 上啟用`unattended-upgrades`以獲得安全補丁：
```bash
sudo apt install unattended-upgrades
sudo dpkg-reconfigure -plow unattended-upgrades
```

---

## 生產中的 Docker
### 最佳實踐
- 使用特定圖像標籤 (`python:3.12-slim`) 而不是 `latest`。
- 以非 root 使用者身分執行容器。
- 掃描影像中的漏洞（`docker scan`、`trivy`）。
- 設定資源限制（`--memory`、`--cpus`）。
- 使用秘密（透過 Docker 秘密或小心環境）。
- 保持圖像較小：多階段構建，高山基地。
### 生產中的 Docker Compose
在`docker-compose.yml`中設定資源限制：
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

## CI/CD 基礎知識
### 管道階段
|舞台|描述 |
|--------|-------------|
| **建置** |編譯程式碼，安裝依賴 |
| **測試** |運行單元、整合和 lint 檢查 |
| **集裝箱化** |建置 Docker 映像 |
| **推** |將鏡像推送到容器註冊表 |
| **部署** |更新暫存/生產環境 |
＃＃＃ 工具
|工具|筆記|
|------|--------|
| **GitHub 作業** |與 GitHub 整合 |
| **亞搏體育appGitLab CI** |內建於 GitLab |
| **詹金斯** |傳統的、高度可配置的|
| **CircleCI、Travis CI** |熱門第三方|
| **ArgoCD** | Kubernetes 的 GitOps |
### GitHub 操作範例
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

## 系統調整與故障排除
### 檢查磁碟空間
```bash
df -h                      # Human-readable disk usage
du -sh /* | sort -h        # Size of top-level directories
```

### 檢查記憶體使用情況
```bash
free -m                    # Memory in MB
vmstat 1 10                # Virtual memory statistics
top -o %MEM                # Sort processes by memory
```

### 檢查CPU負載
```bash
uptime                     # Load average over 1,5,15 minutes
top -o %CPU                # Sort processes by CPU
mpstat -P ALL 1 5          # Per-core CPU usage
```

### 檢查網絡
```bash
netstat -i                 # Interface statistics
iftop                      # Live bandwidth usage (requires install)
nload                      # Another bandwidth monitor
```

### 尋找大文件
```bash
find / -type f -size +100M -exec ls -lh {} \; 2>/dev/null
```

---

## 基礎架構即程式碼 (IaC)
### 地形
在 HCL 中聲明雲端資源。
```hcl
provider "aws" {
  region = "us-east-1"
}
resource "aws_instance" "web" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t2.micro"
}
```

### 安塞布爾
使用 YAML 進行無代理程式設定管理。
```yaml
- name: Install nginx
  hosts: webservers
  tasks:
    - name: Install nginx
      apt:
        name: nginx
        state: present
```

### 最佳實踐
- 使用模組和角色來實現可重複使用性。
- 遠端儲存狀態（S3、Terraform Cloud）。
- 使用變數和秘密（`AWS_SECRET_ACCESS_KEY`通過環境，而不是硬編碼）。
- 版本控制您的 IaC 代碼。
---

## 事件回應（待命）
### 服務中斷檢查表
1. 確認警報。
2. 評估範圍：哪些服務/使用者受到影響？
3. 識別問題（查看日誌、指標、最近的部署）。
4. 如果可能的話，包含（斷路器、功能標誌）。
5. 回滾或向前修復。
6. 向利害關係人和使用者傳達狀態（狀態頁）。
7. 記錄事件時間表和行動。
8. 事後分析：在 24-48 小時內，寫出根本原因分析 (RCA) 和行動項目以防止再次發生。