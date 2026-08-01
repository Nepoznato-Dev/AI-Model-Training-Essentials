<!-- 
This file was automatically translated from English to Korean.
Source: networking_basics.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# 네트워킹 기본

개발자와 시스템 관리자를 위한 실용적인 참조 자료로, 핵심 개념, 프로토콜, 명령어, 문제 해결 방법을 다룹니다.

---

## OSI 모델 (7계층)

네트워크 통신을 이해하기 위한 개념적 프레임워크입니다.

| 계층 | 이름 | 기능 | 예시 프로토콜 |
|-------|------|----------|-------------------|
| 7 | Application | 최종 사용자 서비스 | HTTP, HTTPS, FTP, SMTP, DNS, SSH |
| 6 | Presentation | 데이터 형식화, 암호화, 압축 | TLS, JPEG, ASCII |
| 5 | Session | 연결 관리 | NetBIOS, RPC |
| 4 | Transport | 종단 간 전달, 오류 수정, 흐름 제어 | TCP, UDP |
| 3 | Network | 라우팅, 주소 지정 | IP, ICMP, OSPF, BGP |
| 2 | Data Link | 프레이밍, 오류 감지, MAC 주소 | Ethernet, Wi-Fi, PPP |
| 1 | Physical | 원시 비트 전송 | Ethernet cables, fiber optics, radio waves |

실무에서는 인터넷을 설명할 때 **TCP/IP model**(4계층: Link, Internet, Transport, Application)을 더 자주 사용합니다.

---

## IP 주소 지정

### IPv4
- 32비트 주소이며, 네 개의 옥텟으로 표기합니다: `192.168.1.1`
- 전체 주소 수: 약 43억 개(실제로는 이미 고갈됨).

### IPv6
- 128비트 주소이며, 16진수로 표기합니다: `2001:0db8:85a3:0000:0000:8a2e:0370:7334`
- 전체 주소 수: 2¹²⁸개(사실상 무한대).

### 사설 IP 대역 (RFC 1918)
이 주소들은 인터넷에서 라우팅되지 않으며, 로컬 네트워크 내부에서 사용됩니다.
- `10.0.0.0/8` (10.0.0.0 – 10.255.255.255)
- `172.16.0.0/12` (172.16.0.0 – 172.31.255.255)
- `192.168.0.0/16` (192.168.0.0 – 192.168.255.255)

### CIDR 표기법
`192.168.1.0/24`는 앞의 24비트가 네트워크 prefix이고 마지막 8비트가 호스트 부분임을 뜻합니다. 이 범위에는 `192.168.1.0`부터 `192.168.1.255`까지의 주소가 포함됩니다.

---

## DNS (Domain Name System)

도메인 이름(예: `example.com`)을 IP 주소로 매핑합니다.

### 레코드 유형
| Type | Purpose |
|------|---------|
| **A** | 도메인을 IPv4 주소에 매핑 |
| **AAAA** | 도메인을 IPv6 주소에 매핑 |
| **CNAME** | 다른 도메인 이름에 대한 별칭 |
| **MX** | 메일 교환 서버 |
| **TXT** | 임의 텍스트(SPF, DKIM, verification) |
| **NS** | 해당 도메인의 네임서버 |
| **SRV** | 서비스 레코드(예: SIP용) |

### 일반적인 도구
```bash
dig example.com            # DNS lookup (detailed)
nslookup example.com       # DNS lookup (simpler)
host example.com           # Quick lookup
dig -x 8.8.8.8             # Reverse lookup (IP to name)

포트와 프로토콜
잘 알려진 포트 (0–1023)
포트	프로토콜	서비스
20, 21	TCP	FTP
22	TCP	SSH
23	TCP	Telnet
25	TCP	SMTP
53	UDP/TCP	DNS
80	TCP	HTTP
110	TCP	POP3
123	UDP	NTP
143	TCP	IMAP
443	TCP	HTTPS
465	TCP	SMTPS
587	TCP	SMTP (submission)
993	TCP	IMAPS
995	TCP	POP3S
3306	TCP	MySQL
5432	TCP	PostgreSQL
6379	TCP	Redis
27017	TCP	MongoDB
열린 포트 확인
bash
ss -tulpn                 # Linux: listen and established sockets
netstat -an               # Older tool
lsof -i :8080             # See process using port 8080
nmap localhost            # Scan local ports
TCP vs UDP
특성	TCP	UDP
연결	연결 지향형 (핸드셰이크)	비연결형
신뢰성	전달 보장, 재전송	최선형 전달(패킷 유실 가능)
순서 보장	순서 유지	순서 보장 없음
흐름 제어	예 (sliding window)	아니오
사용 사례	웹(HTTP), 이메일, SSH, 파일 전송	DNS, 스트리밍, VoIP, 게임, SNMP
헤더 크기	20–60 bytes	8 bytes
HTTP와 HTTPS
HTTP 메서드
GET: 리소스를 조회합니다(idempotent, safe).

POST: 데이터를 제출합니다(not idempotent).

PUT: 리소스를 갱신/교체합니다(idempotent).

PATCH: 부분 업데이트를 수행합니다.

DELETE: 리소스를 삭제합니다(idempotent).

상태 코드
1xx: 정보 응답(100 Continue).

2xx: 성공(200 OK, 201 Created, 204 No Content).

3xx: 리다이렉션(301 Moved Permanently, 302 Found, 304 Not Modified).

4xx: 클라이언트 오류(400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found, 429 Too Many Requests).

5xx: 서버 오류(500 Internal Server Error, 502 Bad Gateway, 503 Service Unavailable).

헤더
Content-Type: 미디어 타입(application/json, text/html).

Authorization: 자격 증명(예: ******

Cache-Control: 캐시 정책.

CORS headers: Access-Control-Allow-Origin 등.

TLS/SSL
HTTP 트래픽을 암호화합니다(HTTPS = HTTP over TLS).

Certificate Authorities(CA)가 발급한 인증서는 서버의 신원을 확인합니다.

클라이언트 측에서는 인증서 체인과 호스트명을 검증해야 합니다.

방화벽과 NAT
방화벽
규칙(출발지 IP, 목적지 IP, 포트, 프로토콜)에 따라 트래픽을 필터링합니다.

상태 저장형 방화벽은 연결 상태를 추적합니다.

NAT (Network Address Translation)
인터넷 접속을 위해 사설 IP를 공인 IP로 변환합니다.

포트 포워딩: 공인 포트를 내부 호스트/포트에 매핑합니다.

일반적인 네트워킹 명령
연결 테스트
bash
ping google.com            # ICMP echo request
ping -c 4 8.8.8.8          # ping 4 times
traceroute google.com      # Trace the route (Linux)
tracert google.com         # Windows version
라우팅
bash
ip route show              # Linux: routing table
route -n                   # Older Linux
netstat -r                 # Windows/Mac
네트워크 인터페이스
bash
ip addr show               # List interfaces and IPs
ifconfig                   # Older command
DNS
bash
dig example.com
nslookup example.com
host example.com
포트 연결 확인
bash
nc -zv google.com 443      # Netcat: check if port 443 is open
telnet google.com 443      # Telnet to port
curl -v https://google.com # Verbose output
방화벽 (Linux iptables/nftables)
bash
sudo ufw status            # Ubuntu: simple firewall
sudo iptables -L -n        # List rules
네트워크 통계
bash
ss -tulpn                  # Show listening sockets (Linux)
netstat -an                # All sockets (all OS)
서브넷팅 (빠른 참조)
CIDR	넷마스크	주소 개수	사용 가능한 호스트
/32	255.255.255.255	1	1
/30	255.255.255.252	4	2
/29	255.255.255.248	8	6
/28	255.255.255.240	16	14
/27	255.255.255.224	32	30
/26	255.255.255.192	64	62
/25	255.255.255.128	128	126
/24	255.255.255.0	256	254
/23	255.255.254.0	512	510
/22	255.255.252.0	1,024	1,022
/16	255.255.0.0	65,536	65,534
/8	255.0.0.0	16,777,216	16,777,214
로드 밸런싱과 리버스 프록시
리버스 프록시로서의 Nginx
nginx
server {
    listen 80;
    server_name example.com;
    location / {
        proxy_pass http://localhost:3000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
로드 밸런싱 알고리즘
라운드 로빈

최소 연결

IP 해시 (세션 고정)

가중 라운드 로빈

도구
Nginx, HAProxy (소프트웨어)

AWS ELB, Azure Load Balancer, GCP Cloud Load Balancing (클라우드)

문제 해결 체크리스트
물리적 링크가 살아 있나요? (케이블, Wi-Fi 연결 확인)

게이트웨이에 ping이 되나요? (예: ping 192.168.1.1)

외부 IP에 ping이 되나요? (예: 8.8.8.8)

도메인 이름을 해석할 수 있나요? (dig google.com)

애플리케이션이 예상한 포트에서 수신 중인가요? (ss -tulpn | grep 8080)

방화벽이 포트를 차단하고 있나요? (iptables/ufw 또는 클라우드 security group 확인)

애플리케이션 로그에 오류가 있나요?

TLS 인증서가 유효하고 신뢰되나요? (openssl s_client -connect example.com:443)

text

---

## 파일 6: `devops_sysadmin.md`

```markdown
# DevOps와 시스템 관리

서버를 운영하고, 작업을 자동화하며, 신뢰할 수 있는 인프라를 유지하기 위한 실용적인 가이드입니다.

---

## SSH (Secure Shell)

### 키 생성
```bash
ssh-keygen -t ed25519 -C "your_email@example.com"   # Modern and secure
ssh-keygen -t rsa -b 4096 -C "your_email@example.com" # Fallback
서버에 공개 키 복사
bash
ssh-copy-id user@host
# Manual alternative:
cat ~/.ssh/id_ed25519.pub | ssh user@host "mkdir -p ~/.ssh && cat >> ~/.ssh/authorized_keys"
SSH 설정 (~/.ssh/config)
ssh-config
Host myserver
    HostName 192.168.1.10
    User ubuntu
    IdentityFile ~/.ssh/mykey
    Port 2222
일반적인 SSH 명령
bash
ssh user@host                    # Connect
ssh -J jumpuser@jumphost user@target   # Proxy jump
scp file.txt user@host:/path/     # Copy file to remote
scp user@host:/path/file.txt .    # Copy from remote
rsync -avz -e ssh ./local/ user@host:/remote/  # Efficient sync
SSH 강화
root 로그인 비활성화: PermitRootLogin no

키 기반 인증만 사용: PasswordAuthentication no

기본 포트를 변경합니다(선택 사항이지만 보안상 큰 보호는 아님).

접근을 제한하려면 AllowUsers 또는 AllowGroups를 사용합니다.

Systemd (Linux 서비스 관리)
일반적인 명령
bash
systemctl status nginx           # Check service status
systemctl start nginx            # Start service
systemctl stop nginx
systemctl restart nginx
systemctl reload nginx           # Graceful reload (re-read config)
systemctl enable nginx           # Start on boot
systemctl disable nginx
systemctl list-units --type=service --all   # List all services
systemctl daemon-reload          # Reload unit files after editing
systemd 서비스 유닛 만들기
/etc/systemd/system/myapp.service 파일을 생성합니다:

ini
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
그다음:

bash
sudo systemctl daemon-reload
sudo systemctl enable myapp
sudo systemctl start myapp
Journalctl (로그 보기)
bash
journalctl -u myapp              # Logs for service
journalctl -f                    # Follow (tail) logs
journalctl --since "1 hour ago"
journalctl _PID=1234             # Filter by process ID
로깅 전략
구조화된 로깅
로그를 기계가 파싱하기 쉽도록 JSON 형식을 사용합니다:

python
import structlog
logger = structlog.get_logger()
logger.info("user_login", user_id=123, ip="192.168.1.1")
로그 레벨
DEBUG: 자세한 진단 정보.

INFO: 일반 이벤트(시작, 중지, 정상 트랜잭션).

WARN: 예상 밖이지만 치명적이지는 않은 상황.

ERROR: 특정 작업을 막는 오류.

FATAL/CRITICAL: 시스템 중단 수준의 심각한 오류.

로그 집계
ELK Stack (Elasticsearch, Logstash, Kibana) 또는 Elastic Cloud.

Loki + Grafana (가벼운 대안).

Datadog, Splunk, Sumo Logic (SaaS).

로그 회전 (logrotate)
로그가 디스크를 가득 채우지 않도록 /etc/logrotate.d/myapp을 설정합니다:

logrotate
/var/log/myapp/*.log {
    daily
    rotate 7
    compress
    delaycompress
    missingok
    notifempty
    create 0640 myuser mygroup
}
모니터링과 알림
모니터링할 메트릭
시스템: CPU, RAM, 디스크 사용량, load average, 네트워크 I/O.

애플리케이션: 요청 수, 지연 시간(p50, p95, p99), 오류율, 활성 세션.

데이터베이스: 쿼리 수, 느린 쿼리, connection pool 사용량.

비즈니스: 사용자 가입 수, 전환율, 매출.

도구
Prometheus + Grafana: 표준 오픈소스 스택.

Node Exporter: 시스템 메트릭 수집용.

Blackbox Exporter: 엔드포인트 가용성 점검용.

Alertmanager: 알림 라우팅용.

Cloud native: AWS CloudWatch, Azure Monitor, GCP Monitoring.

업타임 모니터링
Pingdom, Statuspage, Better Uptime, Uptime Kuma (self-hosted).

헬스 체크: 서비스가 정상일 때 200을 반환하는 /health 엔드포인트를 노출합니다.

백업 전략
3-2-1 규칙
데이터 사본 3개.

서로 다른 매체 2종(예: SSD + tape, 또는 local + cloud).

원격지에 보관하는 사본 1개(예: cloud 또는 원격 데이터 센터).

백업 유형
전체 백업: 모든 것을 복사합니다(느리고 공간을 많이 차지함).

증분 백업: 마지막 전체 또는 증분 백업 이후의 변경분만 복사합니다(빠르지만 복구는 복잡함).

차등 백업: 마지막 전체 백업 이후의 변경분을 복사합니다(중간 정도의 절충안).

데이터베이스 백업
bash
# PostgreSQL
pg_dump dbname > backup.sql
pg_dumpall > all_backup.sql

# MySQL / MariaDB
mysqldump -u root -p dbname > backup.sql

# Restore
psql dbname < backup.sql
mysql -u root -p dbname < backup.sql
파일 백업
bash
# Tar archive
tar -czf backup.tar.gz /var/lib/data

# Rsync to remote
rsync -avz /local/data/ user@backup-server:/backup/data/

# Cloud CLI (e.g., AWS S3)
aws s3 sync /local/data s3://my-bucket/backup/
자동 백업 스케줄링 (cron)
cron
# Run daily at 2am
0 2 * * * /usr/local/bin/backup_script.sh
Cron과 예약 작업
Cron 문법
text
* * * * * command
│ │ │ │ │
│ │ │ │ └─ Day of week (0-7, 0=Sun)
│ │ │ └─── Month (1-12)
│ │ └───── Day of month (1-31)
│ └─────── Hour (0-23)
└───────── Minute (0-59)
예시
cron
# Every 5 minutes
*/5 * * * * /path/to/script

# Every day at 3:15 AM
15 3 * * * /path/to/script

# Every Monday at 4 AM
0 4 * * 1 /path/to/script

# Every hour
0 * * * * /path/to/script
Cron 관리
bash
crontab -l          # List current user's cron jobs
crontab -e          # Edit
crontab -r          # Remove all
Anacron
24시간 내내 켜져 있지 않은 시스템(예: 노트북)에서 작업이 결국 실행되도록 보장합니다.

패키지 관리와 업데이트
Debian/Ubuntu (apt)
bash
sudo apt update                # Update package list
sudo apt upgrade               # Upgrade all packages
sudo apt install git nginx
sudo apt remove git
sudo apt autoremove            # Remove unused dependencies
RHEL/CentOS/Fedora (dnf/yum)
bash
sudo dnf check-update
sudo dnf update
sudo dnf install git nginx
sudo dnf remove git
보안 업데이트
Ubuntu에서 보안 패치를 위해 unattended-upgrades를 활성화합니다:

bash
sudo apt install unattended-upgrades
sudo dpkg-reconfigure -plow unattended-upgrades
프로덕션 환경의 Docker
모범 사례
latest 대신 구체적인 이미지 태그(python:3.12-slim)를 사용합니다.

컨테이너는 non-root 사용자로 실행합니다.

이미지 취약점을 검사합니다(docker scan, trivy).

리소스 제한(--memory, --cpus)을 설정합니다.

비밀값은 Docker secrets 등을 활용하고 환경 변수는 주의해서 사용합니다.

멀티 스테이지 빌드와 alpine 베이스 등을 사용해 이미지를 작게 유지합니다.

프로덕션 환경의 Docker Compose
docker-compose.yml에서 리소스 제한을 설정합니다:

yaml
services:
  app:
    image: myapp:1.0
    deploy:
      resources:
        limits:
          memory: 512M
          cpus: '0.5'
CI/CD 기초
파이프라인 단계
Build: 코드를 컴파일하고 의존성을 설치합니다.

Test: 단위 테스트, 통합 테스트, lint 검사를 실행합니다.

Containerise: Docker 이미지를 빌드합니다.

Push: 이미지를 컨테이너 레지스트리에 푸시합니다.

Deploy: staging/production 환경을 업데이트합니다.

도구
GitHub Actions: GitHub와 통합됨.

GitLab CI: GitLab에 내장됨.

Jenkins: 전통적이며 높은 구성 가능성을 제공함.

CircleCI, Travis CI: 널리 쓰이는 서드파티 도구.

ArgoCD: Kubernetes용 GitOps.

간단한 GitHub Action 예시:
yaml
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
시스템 튜닝과 문제 해결
디스크 공간 확인
bash
df -h                      # Human-readable disk usage
du -sh /* | sort -h        # Size of top-level directories
메모리 사용량 확인
bash
free -m                    # Memory in MB
vmstat 1 10                # Virtual memory statistics
top -o %MEM                # Sort processes by memory
CPU 부하 확인
bash
uptime                     # Load average over 1,5,15 minutes
top -o %CPU                # Sort processes by CPU
mpstat -P ALL 1 5          # Per-core CPU usage
네트워크 확인
bash
netstat -i                 # Interface statistics
iftop                      # Live bandwidth usage (requires install)
nload                      # Another bandwidth monitor
큰 파일 찾기
bash
find / -type f -size +100M -exec ls -lh {} \; 2>/dev/null
Infrastructure as Code (IaC)
Terraform
HCL로 클라우드 리소스를 선언합니다.

hcl
provider "aws" {
  region = "us-east-1"
}
resource "aws_instance" "web" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t2.micro"
}
Ansible
YAML을 사용하는 에이전트리스 구성 관리 도구입니다.

yaml
- name: Install nginx
  hosts: webservers
  tasks:
    - name: Install nginx
      apt:
        name: nginx
        state: present
모범 사례
재사용성을 위해 모듈과 역할을 사용합니다.

상태 파일은 원격(S3, Terraform Cloud)에 저장합니다.

변수와 비밀값을 사용하고(AWS_SECRET_ACCESS_KEY는 환경 변수로), 하드코딩하지 않습니다.

IaC 코드는 버전 관리합니다.

인시던트 대응 (On-call)
서비스 장애 체크리스트
알림을 확인하고 대응을 시작합니다.

범위를 평가합니다: 어떤 서비스/사용자가 영향을 받았나요?

문제를 식별합니다(로그, 메트릭, 최근 배포 확인).

가능하면 영향을 격리합니다(circuit breakers, feature flags).

롤백하거나 정방향으로 수정합니다.

이해관계자와 사용자에게 상태를 공유합니다(status page).

인시던트 타임라인과 조치를 문서화합니다.

사후 분석: 24–48시간 이내에 근본 원인 분석(RCA)과 재발 방지 action items를 작성합니다.
