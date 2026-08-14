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
# DevOps and System Administration

A practical guide to managing servers, automating operations, and maintaining reliable infrastructure.

---

## SSH (Secure Shell)

### Key Generation

```bash
ssh-keygen -t ed25519 -C "your_email@example.com"   # Modern and secure
ssh-keygen -t rsa -b 4096 -C "your_email@example.com" # Fallback
```

### Copy Public Key to Server

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

### Common SSH Commands

```bash
ssh user@host                              # Connect
ssh -J jumpuser@jumphost user@target       # Proxy jump
scp file.txt user@host:/path/              # Copy file to remote
scp user@host:/path/file.txt .             # Copy from remote
rsync -avz -e ssh ./local/ user@host:/remote/  # Efficient sync
```

### Hardening SSH

- Disable root login: `PermitRootLogin no`
- Use key-based auth only: `PasswordAuthentication no`
- Change default port (optional, security through obscurity).
- Enable `AllowUsers` or `AllowGroups` to restrict access.

---

## Systemd (Linux Service Management)

### Common Commands

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

### Creating a systemd Service Unit

Create `/etc/systemd/system/myapp.service`:

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

Then:

```bash
sudo systemctl daemon-reload
sudo systemctl enable myapp
sudo systemctl start myapp
```

---

## Journalctl (View Logs)

```bash
journalctl -u myapp              # Logs for service
journalctl -f                    # Follow (tail) logs
journalctl --since "1 hour ago"
journalctl _PID=1234             # Filter by process ID
```

---

## Logging Strategies

### Structured Logging

Use JSON format to make logs machine-parseable:

```python
import structlog
logger = structlog.get_logger()
logger.info("user_login", user_id=123, ip="192.168.1.1")
```

### Log Levels

| Level | Purpose |
|-------|---------|
| **DEBUG** | Detailed diagnostic information |
| **INFO** | General events (start, stop, normal transactions) |
| **WARN** | Unexpected but not fatal |
| **ERROR** | Error that prevents a specific operation |
| **FATAL/CRITICAL** | System shutdown |

### Log Aggregation

- **ELK Stack** (Elasticsearch, Logstash, Kibana) or Elastic Cloud.
- **Loki + Grafana** (lightweight alternative).
- **Datadog, Splunk, Sumo Logic** (SaaS).

### Log Rotation (`logrotate`)

Prevent logs from filling up disks. Configure `/etc/logrotate.d/myapp`:

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

## Monitoring and Alerting

### Metrics to Monitor

| Category | Key Metrics |
|----------|-------------|
| **System** | CPU, RAM, disk usage, load average, network I/O |
| **Application** | Request rate, latency (p50, p95, p99), error rate, active sessions |
| **Database** | Query count, slow queries, connection pool usage |
| **Business** | User signups, conversion rate, revenue |

### Tools

- **Prometheus + Grafana**: Standard open-source stack.
- **Node Exporter** for system metrics.
- **Blackbox Exporter** for endpoint availability.
- **Alertmanager** for alert routing.
- **Cloud native**: AWS CloudWatch, Azure Monitor, GCP Monitoring.

### Uptime Monitoring

- Pingdom, Statuspage, Better Uptime, Uptime Kuma (self-hosted).
- Health checks: expose a `/health` endpoint that returns 200 if the service is healthy.

---

## Backup Strategies

### The 3-2-1 Rule

- **3** copies of data.
- **2** different media types (e.g., SSD + tape, or local + cloud).
- **1** copy off-site (e.g., cloud or remote data centre).

### Backup Types

| Type | Description | Trade-off |
|------|-------------|-----------|
| **Full** | Copy everything | Slow, space-heavy |
| **Incremental** | Copy only changes since last full or incremental | Fast, complex restore |
| **Differential** | Copy changes since last full | Middle ground |

### Database Backups

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

### File Backups

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

### Examples

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

### Managing Cron

```bash
crontab -l          # List current user's cron jobs
crontab -e          # Edit
crontab -r          # Remove all
```

### Anacron

Used for systems not running 24/7 (e.g., laptops); ensures jobs run eventually.

---

## Package Management and Updates

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

### Security Updates

Enable `unattended-upgrades` on Ubuntu for security patches:

```bash
sudo apt install unattended-upgrades
sudo dpkg-reconfigure -plow unattended-upgrades
```

---

## Docker in Production

### Best Practices

- Use specific image tags (`python:3.12-slim`) not `latest`.
- Run containers as non-root user.
- Scan images for vulnerabilities (`docker scan`, `trivy`).
- Set resource limits (`--memory`, `--cpus`).
- Use secrets (via Docker secrets or environment with care).
- Keep images small: multi-stage builds, alpine base.

### Docker Compose in Production

Set resource limits in `docker-compose.yml`:

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

## CI/CD Basics

### Pipeline Stages

| Stage | Description |
|-------|-------------|
| **Build** | Compile code, install dependencies |
| **Test** | Run unit, integration, and lint checks |
| **Containerise** | Build Docker image |
| **Push** | Push image to container registry |
| **Deploy** | Update staging/production environment |

### Tools

| Tool | Notes |
|------|-------|
| **GitHub Actions** | Integrated with GitHub |
| **GitLab CI** | Built into GitLab |
| **Jenkins** | Traditional, highly configurable |
| **CircleCI, Travis CI** | Popular third-party |
| **ArgoCD** | GitOps for Kubernetes |

### Example GitHub Action

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

## System Tuning and Troubleshooting

### Check Disk Space

```bash
df -h                      # Human-readable disk usage
du -sh /* | sort -h        # Size of top-level directories
```

### Check Memory Usage

```bash
free -m                    # Memory in MB
vmstat 1 10                # Virtual memory statistics
top -o %MEM                # Sort processes by memory
```

### Check CPU Load

```bash
uptime                     # Load average over 1,5,15 minutes
top -o %CPU                # Sort processes by CPU
mpstat -P ALL 1 5          # Per-core CPU usage
```

### Check Network

```bash
netstat -i                 # Interface statistics
iftop                      # Live bandwidth usage (requires install)
nload                      # Another bandwidth monitor
```

### Find Large Files

```bash
find / -type f -size +100M -exec ls -lh {} \; 2>/dev/null
```

---

## Infrastructure as Code (IaC)

### Terraform

Declare cloud resources in HCL.

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

Agentless configuration management using YAML.

```yaml
- name: Install nginx
  hosts: webservers
  tasks:
    - name: Install nginx
      apt:
        name: nginx
        state: present
```

### Best Practices

- Use modules and roles for reusability.
- Store state remotely (S3, Terraform Cloud).
- Use variables and secrets (`AWS_SECRET_ACCESS_KEY` via environment, not hardcoded).
- Version control your IaC code.

---

## Incident Response (On-call)

### Checklist for Service Outage

1. Acknowledge the alert.
2. Assess scope: Which services/users are affected?
3. Identify the issue (look at logs, metrics, recent deployments).
4. Contain if possible (circuit breakers, feature flags).
5. Rollback or fix forward.
6. Communicate status to stakeholders and users (status page).
7. Document the incident timeline and actions.
8. Post-mortem: within 24–48 hours, write a root cause analysis (RCA) and action items to prevent recurrence.
