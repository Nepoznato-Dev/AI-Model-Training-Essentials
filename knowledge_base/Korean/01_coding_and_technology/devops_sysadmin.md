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
# DevOps 및 시스템 관리
서버 관리, 운영 자동화, 안정적인 인프라 유지에 대한 실용적인 가이드입니다.
---

## SSH(보안 셸)
### 키 생성
```bash
ssh-keygen -t ed25519 -C "your_email@example.com"   # Modern and secure
ssh-keygen -t rsa -b 4096 -C "your_email@example.com" # Fallback
```

### 공개 키를 서버에 복사
```bash
ssh-copy-id user@host
# Manual alternative:
cat ~/.ssh/id_ed25519.pub | ssh user@host "mkdir -p ~/.ssh && cat >> ~/.ssh/authorized_keys"
```

### SSH 구성(`~/.ssh/config`)
```
Host myserver
    HostName 192.168.1.10
    User ubuntu
    IdentityFile ~/.ssh/mykey
    Port 2222
```

### 일반적인 SSH 명령
```bash
ssh user@host                              # Connect
ssh -J jumpuser@jumphost user@target       # Proxy jump
scp file.txt user@host:/path/              # Copy file to remote
scp user@host:/path/file.txt .             # Copy from remote
rsync -avz -e ssh ./local/ user@host:/remote/  # Efficient sync
```

### SSH 강화
- 루트 로그인 비활성화:`PermitRootLogin no`
- 키 기반 인증만 사용:`PasswordAuthentication no`
- 기본 포트를 변경합니다(선택 사항, 모호함을 통한 보안).
- 액세스를 제한하려면`AllowUsers`또는 `AllowGroups`을(를) 활성화하세요.
---

## Systemd(리눅스 서비스 관리)
### 일반 명령
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

### systemd 서비스 유닛 생성
`/etc/systemd/system/myapp.service` 만들기:
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

그 다음에:
```bash
sudo systemctl daemon-reload
sudo systemctl enable myapp
sudo systemctl start myapp
```

---

## Journalctl(로그 보기)
```bash
journalctl -u myapp              # Logs for service
journalctl -f                    # Follow (tail) logs
journalctl --since "1 hour ago"
journalctl _PID=1234             # Filter by process ID
```

---

## 로깅 전략
### 구조화된 로깅
JSON 형식을 사용하여 로그를 기계에서 구문 분석할 수 있도록 만듭니다.
```python
import structlog
logger = structlog.get_logger()
logger.info("user_login", user_id=123, ip="192.168.1.1")
```

### 로그 수준
| 레벨 | 목적 |
|-------|---------|
| **디버그** | 자세한 진단 정보 |
| **정보** | 일반 이벤트(시작, 중지, 정상 트랜잭션) |
| **경고** | 예상치 못했지만 치명적이지는 않음 |
| **오류** | 특정 작업을 방해하는 오류 |
| **치명적/위험** | 시스템 종료 |
### 로그 집계
- **ELK 스택**(Elasticsearch, Logstash, Kibana) 또는 Elastic Cloud.
- **Loki + Grafana**(경량 대안).
- **Datadog, Splunk, Sumo Logic**(SaaS).
### 로그 회전(`logrotate`)
로그가 디스크를 채우는 것을 방지합니다.`/etc/logrotate.d/myapp`구성:
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

## 모니터링 및 경고
### 모니터링할 측정항목
| 카테고리 | 주요 지표 |
|----------|-------------|
| **시스템** | CPU, RAM, 디스크 사용량, 로드 평균, 네트워크 I/O |
| **신청** | 요청 속도, 대기 시간(p50, p95, p99), 오류 속도, 활성 세션 |
| **데이터베이스** | 쿼리 횟수, 느린 쿼리, 연결 풀 사용량 |
| **비즈니스** | 사용자 가입, 전환율, 수익 |
### 도구
- **Prometheus + Grafana**: 표준 오픈 소스 스택.
- 시스템 측정항목용 **노드 내보내기**.
- 엔드포인트 가용성을 위한 **블랙박스 내보내기**.
- 경고 라우팅을 위한 **Alertmanager**.
- **클라우드 네이티브**: AWS CloudWatch, Azure Monitor, GCP 모니터링.
### 가동시간 모니터링
- Pingdom, Statuspage, Better Uptime, Uptime Kuma(자체 호스팅).
- 상태 확인: 서비스가 정상인 경우 200을 반환하는`/health`엔드포인트를 노출합니다.
---

## 백업 전략
### 3-2-1 규칙
- **3** 데이터 사본.
- **2** 다양한 미디어 유형(예: SSD + 테이프 또는 로컬 + 클라우드)
- **1** 오프사이트(예: 클라우드 또는 원격 데이터 센터)에 복사합니다.
### 백업 유형
| 유형 | 설명 | 트레이드오프 |
|------|-------------|------------|
| **전체** | 모든 것을 복사 | 느리고 공간이 많이 소요됨 |
| **증분** | 마지막 전체 또는 증분 이후 변경 사항만 복사 | 빠르고 복잡한 복원 |
| **차등** | 마지막 전체 이후 변경사항 복사 | 중간지대 |
### 데이터베이스 백업
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

### 파일 백업
```bash
# Tar archive
tar -czf backup.tar.gz /var/lib/data

# Rsync to remote
rsync -avz /local/data/ user@backup-server:/backup/data/

# Cloud CLI (e.g., AWS S3)
aws s3 sync /local/data s3://my-bucket/backup/
```

### 자동 백업 예약(cron)
```cron
# Run daily at 2am
0 2 * * * /usr/local/bin/backup_script.sh
```

---

## 크론 및 예약된 작업
### 크론 구문
```
* * * * * command
│ │ │ │ │
│ │ │ │ └─ Day of week (0-7, 0=Sun)
│ │ │ └─── Month (1-12)
│ │ └───── Day of month (1-31)
│ └─────── Hour (0-23)
└───────── Minute (0-59)
```

### 예
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

### 크론 관리
```bash
crontab -l          # List current user's cron jobs
crontab -e          # Edit
crontab -r          # Remove all
```

### 아나크론
연중무휴로 실행되지 않는 시스템(예: 노트북)에 사용됩니다. 작업이 결국 실행되도록 보장합니다.
---

## 패키지 관리 및 업데이트
### 데비안/우분투(`apt`)
```bash
sudo apt update                # Update package list
sudo apt upgrade               # Upgrade all packages
sudo apt install git nginx
sudo apt remove git
sudo apt autoremove            # Remove unused dependencies
```

### RHEL/CentOS/Fedora(`dnf`/`yum`)
```bash
sudo dnf check-update
sudo dnf update
sudo dnf install git nginx
sudo dnf remove git
```

### 보안 업데이트
보안 패치를 위해 Ubuntu에서 `unattended-upgrades`을 활성화합니다.
```bash
sudo apt install unattended-upgrades
sudo dpkg-reconfigure -plow unattended-upgrades
```

---

## 프로덕션 중인 도커
### 모범 사례
- `latest`이 아닌 특정 이미지 태그(`python:3.12-slim`)를 사용하세요.
- 루트가 아닌 사용자로 컨테이너를 실행합니다.
- 이미지에서 취약점을 스캔합니다(`docker scan`,`trivy`).
- 리소스 제한을 설정합니다(`--memory`,`--cpus`).
- 비밀을 사용하십시오(Docker 비밀 또는 환경을 통해 주의해서).
- 이미지를 작게 유지하세요: 다단계 빌드, 알파인 기반.
### 프로덕션의 Docker Compose
`docker-compose.yml`에서 리소스 제한을 설정합니다.
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

## CI/CD 기본 사항
### 파이프라인 단계
| 무대 | 설명 |
|-------|-------------|
| **빌드** | 코드 컴파일, 종속성 설치 |
| **테스트** | 단위, 통합 및 Lint 검사 실행 |
| **컨테이너화** | Docker 이미지 빌드 |
| **푸시** | 컨테이너 레지스트리에 이미지 푸시 |
| **배포** | 스테이징/프로덕션 환경 업데이트 |
### 도구
| 도구 | 메모 |
|------|---------|
| **GitHub 작업** | GitHub와 통합 |
| **GitLab CI** | GitLab에 내장 |
| **젠킨스** | 전통적이며 고도로 구성 가능 |
| **서클CI, 트래비스 CI** | 인기 있는 타사 |
| **아르고CD** | Kubernetes용 GitOps |
### GitHub 작업 예시
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

## 시스템 튜닝 및 문제 해결
### 디스크 공간 확인
```bash
df -h                      # Human-readable disk usage
du -sh /* | sort -h        # Size of top-level directories
```

### 메모리 사용량 확인
```bash
free -m                    # Memory in MB
vmstat 1 10                # Virtual memory statistics
top -o %MEM                # Sort processes by memory
```

### CPU 부하 확인
```bash
uptime                     # Load average over 1,5,15 minutes
top -o %CPU                # Sort processes by CPU
mpstat -P ALL 1 5          # Per-core CPU usage
```

### 네트워크 확인
```bash
netstat -i                 # Interface statistics
iftop                      # Live bandwidth usage (requires install)
nload                      # Another bandwidth monitor
```

### 대용량 파일 찾기
```bash
find / -type f -size +100M -exec ls -lh {} \; 2>/dev/null
```

---

## 코드형 인프라(IaC)
### 테라폼
HCL에서 클라우드 리소스를 선언합니다.
```hcl
provider "aws" {
  region = "us-east-1"
}
resource "aws_instance" "web" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t2.micro"
}
```

### 앤서블
YAML을 사용한 에이전트 없는 구성 관리.
```yaml
- name: Install nginx
  hosts: webservers
  tasks:
    - name: Install nginx
      apt:
        name: nginx
        state: present
```

### 모범 사례
- 재사용성을 위해 모듈과 역할을 사용합니다.
- 상태를 원격으로 저장합니다(S3, Terraform Cloud).
- 변수와 비밀을 사용하세요(하드코딩되지 않은 환경을 통해 `AWS_SECRET_ACCESS_KEY`).
- IaC 코드의 버전을 관리하세요.
---

## 사고 대응(대기 중)
### 서비스 중단 체크리스트
1. 경고를 확인합니다.
2. 평가 범위: 어떤 서비스/사용자가 영향을 받나요?
3. 문제를 식별합니다(로그, 지표, 최근 배포 확인).
4. 가능하면 포함합니다(회로 차단기, 기능 플래그).
5. 롤백하거나 앞으로 수정합니다.
6. 이해관계자 및 사용자에게 상태를 전달합니다(상태 페이지).
7. 사건 타임라인과 조치를 문서화합니다.
8. 사후 분석: 24~48시간 이내에 근본 원인 분석(RCA) 및 재발 방지 조치 항목을 작성합니다.