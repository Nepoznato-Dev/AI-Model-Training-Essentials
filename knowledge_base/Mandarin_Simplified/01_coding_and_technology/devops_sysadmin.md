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
# DevOps 和系统管理
管理服务器、自动化操作和维护可靠基础设施的实用指南。
---

## SSH（安全外壳）
### 密钥生成
```bash
ssh-keygen -t ed25519 -C "your_email@example.com"   # Modern and secure
ssh-keygen -t rsa -b 4096 -C "your_email@example.com" # Fallback
```

### 将公钥复制到服务器
```bash
ssh-copy-id user@host
# Manual alternative:
cat ~/.ssh/id_ed25519.pub | ssh user@host "mkdir -p ~/.ssh && cat >> ~/.ssh/authorized_keys"
```

### SSH 配置（`~/.ssh/config`）
```
Host myserver
    HostName 192.168.1.10
    User ubuntu
    IdentityFile ~/.ssh/mykey
    Port 2222
```

### 常用 SSH 命令
```bash
ssh user@host                              # Connect
ssh -J jumpuser@jumphost user@target       # Proxy jump
scp file.txt user@host:/path/              # Copy file to remote
scp user@host:/path/file.txt .             # Copy from remote
rsync -avz -e ssh ./local/ user@host:/remote/  # Efficient sync
```

### 强化 SSH
- 禁用 root 登录：`PermitRootLogin no` 
- 仅使用基于密钥的身份验证：`PasswordAuthentication no` 
- 更改默认端口（可选，通过隐藏实现安全性）。
- 启用`AllowUsers`或`AllowGroups`以限制访问。
---

## Systemd（Linux 服务管理）
### 常用命令
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

### 创建 systemd 服务单元
创建`/etc/systemd/system/myapp.service`：
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

然后：
```bash
sudo systemctl daemon-reload
sudo systemctl enable myapp
sudo systemctl start myapp
```

---

## Journalctl（查看日志）
```bash
journalctl -u myapp              # Logs for service
journalctl -f                    # Follow (tail) logs
journalctl --since "1 hour ago"
journalctl _PID=1234             # Filter by process ID
```

---

## 日志记录策略
### 结构化日志记录
使用 JSON 格式使日志可供机器解析：
```python
import structlog
logger = structlog.get_logger()
logger.info("user_login", user_id=123, ip="192.168.1.1")
```

### 日志级别
|水平|目的|
|--------|---------|
| **调试** |详细诊断信息|
| **信息** |一般事件（开始、停止、正常交易） |
| **警告** |意外但并非致命|
| **错误** |阻止特定操作的错误 |
| **致命/严重** |系统关闭|
### 日志聚合
- **ELK Stack**（Elasticsearch、Logstash、Kibana）或 Elastic Cloud。
- **Loki + Grafana**（轻量级替代方案）。
- **Datadog、Splunk、Sumo Logic** (SaaS)。
### 日志轮转 (`logrotate`)
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

## 监控和警报
### 监控指标
|类别 |关键指标|
|----------|-------------|
| **系统** | CPU、RAM、磁盘使用率、平均负载、网络 I/O |
| **应用** |请求率、延迟（p50、p95、p99）、错误率、活动会话 |
| **数据库** |查询计数、慢查询、连接池使用情况 |
| **业务** |用户注册、转化率、收入 |
＃＃＃ 工具
- **Prometheus + Grafana**：标准开源堆栈。
- 用于系统指标的**节点导出器**。
- **Blackbox Exporter** 用于端点可用性。
- **Alertmanager** 用于警报路由。
- **云原生**：AWS CloudWatch、Azure Monitor、GCP 监控。
### 正常运行时间监控
- Pingdom、Statuspage、Better Uptime、Uptime Kuma（自托管）。
- 运行状况检查：公开`/health`端点，如果服务运行状况良好，则返回 200。
---

## 备份策略
### 3-2-1 规则
- **3** 数据副本。
- **2** 不同的媒体类型（例如 SSD + 磁带，或本地 + 云）。
- **1** 异地复制（例如云或远程数据中心）。
### 备份类型
|类型 |描述 |权衡|
|------|-------------|------------|
| **完整** |复制所有内容 |速度慢，空间大|
| **增量** |仅复制自上次完整或增量以来的更改 |快速、复杂的恢复 |
| **差速器** |复制自上次完整以来的更改 |中间立场|
### 数据库备份
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

### 文件备份
```bash
# Tar archive
tar -czf backup.tar.gz /var/lib/data

# Rsync to remote
rsync -avz /local/data/ user@backup-server:/backup/data/

# Cloud CLI (e.g., AWS S3)
aws s3 sync /local/data s3://my-bucket/backup/
```

### 自动备份计划 (cron)
```cron
# Run daily at 2am
0 2 * * * /usr/local/bin/backup_script.sh
```

---

## Cron 和计划作业
### Cron 语法
```
* * * * * command
│ │ │ │ │
│ │ │ │ └─ Day of week (0-7, 0=Sun)
│ │ │ └─── Month (1-12)
│ │ └───── Day of month (1-31)
│ └─────── Hour (0-23)
└───────── Minute (0-59)
```

### 示例
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

### 阿纳克朗
用于非 24/7 运行的系统（例如笔记本电脑）；确保作业最终运行。
---

## 包管理和更新
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

### 安全更新
在 Ubuntu 上启用`unattended-upgrades`以获得安全补丁：
```bash
sudo apt install unattended-upgrades
sudo dpkg-reconfigure -plow unattended-upgrades
```

---

## 生产中的 Docker
### 最佳实践
- 使用特定图像标签 (`python:3.12-slim`) 而不是`latest`。
- 以非 root 用户身份运行容器。
- 扫描图像中的漏洞（`docker scan`、`trivy`）。
- 设置资源限制（`--memory`、`--cpus`）。
- 使用秘密（通过 Docker 秘密或小心环境）。
- 保持图像较小：多阶段构建，高山基地。
### 生产中的 Docker Compose
在`docker-compose.yml`中设置资源限制：
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

## CI/CD 基础知识
### 管道阶段
|舞台|描述 |
|--------|-------------|
| **构建** |编译代码，安装依赖 |
| **测试** |运行单元、集成和 lint 检查 |
| **集装箱化** |构建 Docker 镜像 |
| **推** |将镜像推送到容器注册表 |
| **部署** |更新暂存/生产环境 |
＃＃＃ 工具
|工具|笔记|
|------|--------|
| **GitHub 操作** |与 GitHub 集成 |
| **亚搏体育appGitLab CI** |内置于 GitLab |
| **詹金斯** |传统的、高度可配置的|
| **CircleCI、Travis CI** |热门第三方|
| **ArgoCD** | Kubernetes 的 GitOps |
### GitHub 操作示例
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

## 系统调整和故障排除
### 检查磁盘空间
```bash
df -h                      # Human-readable disk usage
du -sh /* | sort -h        # Size of top-level directories
```

### 检查内存使用情况
```bash
free -m                    # Memory in MB
vmstat 1 10                # Virtual memory statistics
top -o %MEM                # Sort processes by memory
```

### 检查CPU负载
```bash
uptime                     # Load average over 1,5,15 minutes
top -o %CPU                # Sort processes by CPU
mpstat -P ALL 1 5          # Per-core CPU usage
```

### 检查网络
```bash
netstat -i                 # Interface statistics
iftop                      # Live bandwidth usage (requires install)
nload                      # Another bandwidth monitor
```

### 查找大文件
```bash
find / -type f -size +100M -exec ls -lh {} \; 2>/dev/null
```

---

## 基础设施即代码 (IaC)
### 地形
在 HCL 中声明云资源。
```hcl
provider "aws" {
  region = "us-east-1"
}
resource "aws_instance" "web" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t2.micro"
}
```

### 安塞布尔
使用 YAML 进行无代理配置管理。
```yaml
- name: Install nginx
  hosts: webservers
  tasks:
    - name: Install nginx
      apt:
        name: nginx
        state: present
```

### 最佳实践
- 使用模块和角色来实现可重用性。
- 远程存储状态（S3、Terraform Cloud）。
- 使用变量和秘密（`AWS_SECRET_ACCESS_KEY` 通过环境，而不是硬编码）。
- 版本控制您的 IaC 代码。
---

## 事件响应（待命）
### 服务中断检查表
1. 确认警报。
2. 评估范围：哪些服务/用户受到影响？
3. 识别问题（查看日志、指标、最近的部署）。
4. 如果可能的话，包含（断路器、功能标志）。
5. 回滚或向前修复。
6. 向利益相关者和用户传达状态（状态页面）。
7. 记录事件时间表和行动。
8. 事后分析：在 24-48 小时内，写出根本原因分析 (RCA) 和行动项目以防止再次发生。