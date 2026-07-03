# Ağ Temelleri

Geliştiriciler ve sistem yöneticileri için pratik bir başvuru kaynağı — temel kavramlar, protokoller, komutlar ve sorun giderme.

---

## OSI Modeli (7 Katman)

Ağ iletişimini anlamak için kavramsal bir çerçeve.

| Katman | Ad | İşlev | Örnek protokoller |
|-------|------|----------|-------------------|
| 7 | Uygulama | Son kullanıcı hizmetleri | HTTP, HTTPS, FTP, SMTP, DNS, SSH |
| 6 | Sunum | Veri biçimlendirme, şifreleme, sıkıştırma | TLS, JPEG, ASCII |
| 5 | Oturum | Bağlantı yönetimi | NetBIOS, RPC |
| 4 | Taşıma | Uçtan uca teslim, hata düzeltme, akış kontrolü | TCP, UDP |
| 3 | Ağ | Yönlendirme, adresleme | IP, ICMP, OSPF, BGP |
| 2 | Veri Bağı | Çerçeveleme, hata tespiti, MAC adresleri | Ethernet, Wi-Fi, PPP |
| 1 | Fiziksel | Ham bit iletimi | Ethernet kabloları, fiber optik, radyo dalgaları |

Pratikte, **TCP/IP modeli** (4 katman: Bağlantı, İnternet, Taşıma, Uygulama) internet için daha yaygın olarak kullanılır.

---

## IP Adresleme

### IPv4
- 32 bitlik adres, dört oktet şeklinde yazılır: `192.168.1.1`
- Toplam: ~4,3 milyar adres (ancak pratikte tükenmiştir).

### IPv6
- 128 bitlik adres, onaltılık biçimde yazılır: `2001:0db8:85a3:0000:0000:8a2e:0370:7334`
- Toplam: 2¹²⁸ adres (pratik olarak sonsuz).

### Özel IP Aralıkları (RFC 1918)
Bunlar internette yönlendirilemez; yerel ağların içinde kullanılır:
- `10.0.0.0/8` (10.0.0.0 – 10.255.255.255)
- `172.16.0.0/12` (172.16.0.0 – 172.31.255.255)
- `192.168.0.0/16` (192.168.0.0 – 192.168.255.255)

### CIDR Gösterimi
`192.168.1.0/24`, ilk 24 bitin ağ öneki olduğu; son 8 bitin ise ana bilgisayarlar için ayrıldığı anlamına gelir. `192.168.1.0` ile `192.168.1.255` arasındaki adresleri kapsar.

---

## DNS (Alan Adı Sistemi)

Alan adlarını (ör. `example.com`) IP adreslerine eşler.

### Kayıt Türleri
| Tür | Amaç |
|------|---------|
| **A** | Alan adını IPv4 adresine eşler |
| **AAAA** | Alan adını IPv6 adresine eşler |
| **CNAME** | Başka bir alan adına takma ad |
| **MX** | Posta alışveriş sunucusu |
| **TXT** | Serbest metin (SPF, DKIM, doğrulama) |
| **NS** | Alan adının ad sunucusu |
| **SRV** | Hizmet kaydı (ör. SIP için) |

### Yaygın Araçlar
```bash
dig example.com            # DNS lookup (detailed)
nslookup example.com       # DNS lookup (simpler)
host example.com           # Quick lookup
dig -x 8.8.8.8             # Reverse lookup (IP to name)

Ports and Protocols
Well-Known Ports (0–1023)
Port	Protocol	Service
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
Check open ports
bash
ss -tulpn                 # Linux: listen and established sockets
netstat -an               # Older tool
lsof -i :8080             # See process using port 8080
nmap localhost            # Scan local ports
TCP vs UDP
Feature	TCP	UDP
Connection	Connection-oriented (handshake)	Connectionless
Reliability	Guaranteed delivery, retransmission	Best effort (may drop packets)
Ordering	Preserves order	No ordering guarantee
Flow control	Yes (sliding window)	No
Use cases	Web (HTTP), email, SSH, file transfer	DNS, streaming, VoIP, gaming, SNMP
Header size	20–60 bytes	8 bytes
HTTP and HTTPS
HTTP Methods
GET: Retrieve a resource (idempotent, safe).

POST: Submit data (not idempotent).

PUT: Update/replace a resource (idempotent).

PATCH: Partial update.

DELETE: Remove a resource (idempotent).

Status Codes
1xx: Informational (100 Continue).

2xx: Success (200 OK, 201 Created, 204 No Content).

3xx: Redirection (301 Moved Permanently, 302 Found, 304 Not Modified).

4xx: Client error (400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found, 429 Too Many Requests).

5xx: Server error (500 Internal Server Error, 502 Bad Gateway, 503 Service Unavailable).

Headers
Content-Type: media type (application/json, text/html).

Authorization: credentials (e.g., ******

Cache-Control: caching policy.

CORS headers: Access-Control-Allow-Origin, etc.

TLS/SSL
Encrypts HTTP traffic (HTTPS = HTTP over TLS).

Certificates from Certificate Authorities (CAs) authenticate the server.

Verify certificate chain and hostname on the client side.

Firewalls and NAT
Firewall
Filters traffic based on rules (source IP, dest IP, port, protocol).

Stateful firewalls track connection states.

NAT (Network Address Translation)
Translates private IPs to a public IP for internet access.

Port forwarding: maps a public port to an internal host/port.

Common Networking Commands
Connectivity Tests
bash
ping google.com            # ICMP echo request
ping -c 4 8.8.8.8          # ping 4 times
traceroute google.com      # Trace the route (Linux)
tracert google.com         # Windows version
Routing
bash
ip route show              # Linux: routing table
route -n                   # Older Linux
netstat -r                 # Windows/Mac
Network Interfaces
bash
ip addr show               # List interfaces and IPs
ifconfig                   # Older command
DNS
bash
dig example.com
nslookup example.com
host example.com
Connectivity to a Port
bash
nc -zv google.com 443      # Netcat: check if port 443 is open
telnet google.com 443      # Telnet to port
curl -v https://google.com # Verbose output
Firewall (Linux iptables/nftables)
bash
sudo ufw status            # Ubuntu: simple firewall
sudo iptables -L -n        # List rules
Network Statistics
bash
ss -tulpn                  # Show listening sockets (Linux)
netstat -an                # All sockets (all OS)
Subnetting (Quick Reference)
CIDR	Netmask	Number of addresses	Usable hosts
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
Load Balancing and Reverse Proxies
Nginx as Reverse Proxy
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
Load Balancing Algorithms
Round-robin

Least connections

IP hash (session stickiness)

Weighted round-robin

Tools
Nginx, HAProxy (software)

AWS ELB, Azure Load Balancer, GCP Cloud Load Balancing (cloud)

Troubleshooting Checklist
Is the physical link up? (Check cables, Wi-Fi connection).

Can you ping the gateway? (e.g., ping 192.168.1.1).

Can you ping an external IP? (e.g., 8.8.8.8).

Can you resolve a domain? (dig google.com).

Is the application listening on the expected port? (ss -tulpn | grep 8080).

Is the firewall blocking the port? (Check iptables/ufw or cloud security groups).

Are there any errors in the application logs?

Is TLS certificate valid and trusted? (openssl s_client -connect example.com:443).

text

---

## File 6: `devops_sysadmin.md`

```markdown
# DevOps and System Administration

A practical guide to managing servers, automating operations, and maintaining reliable infrastructure.

---

## SSH (Secure Shell)

### Key Generation
```bash
ssh-keygen -t ed25519 -C "your_email@example.com"   # Modern and secure
ssh-keygen -t rsa -b 4096 -C "your_email@example.com" # Fallback
Copy Public Key to Server
bash
ssh-copy-id user@host
# Manual alternative:
cat ~/.ssh/id_ed25519.pub | ssh user@host "mkdir -p ~/.ssh && cat >> ~/.ssh/authorized_keys"
SSH Config (~/.ssh/config)
ssh-config
Host myserver
    HostName 192.168.1.10
    User ubuntu
    IdentityFile ~/.ssh/mykey
    Port 2222
Common SSH Commands
bash
ssh user@host                    # Connect
ssh -J jumpuser@jumphost user@target   # Proxy jump
scp file.txt user@host:/path/     # Copy file to remote
scp user@host:/path/file.txt .    # Copy from remote
rsync -avz -e ssh ./local/ user@host:/remote/  # Efficient sync
Hardening SSH
Disable root login: PermitRootLogin no

Use key-based auth only: PasswordAuthentication no

Change default port (optional, security through obscurity).

Enable AllowUsers or AllowGroups to restrict access.

Systemd (Linux Service Management)
Common Commands
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
Creating a systemd Service Unit
Create /etc/systemd/system/myapp.service:

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
Then:

bash
sudo systemctl daemon-reload
sudo systemctl enable myapp
sudo systemctl start myapp
Journalctl (View Logs)
bash
journalctl -u myapp              # Logs for service
journalctl -f                    # Follow (tail) logs
journalctl --since "1 hour ago"
journalctl _PID=1234             # Filter by process ID
Logging Strategies
Structured Logging
Use JSON format to make logs machine-parseable:

python
import structlog
logger = structlog.get_logger()
logger.info("user_login", user_id=123, ip="192.168.1.1")
Log Levels
DEBUG: detailed diagnostic.

INFO: general events (start, stop, normal transactions).

WARN: unexpected but not fatal.

ERROR: error that prevents a specific operation.

FATAL/CRITICAL: system shutdown.

Log Aggregation
ELK Stack (Elasticsearch, Logstash, Kibana) or Elastic Cloud.

Loki + Grafana (lightweight alternative).

Datadog, Splunk, Sumo Logic (SaaS).

Log Rotation (logrotate)
Prevent logs from filling up disks. Configure /etc/logrotate.d/myapp:

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
Monitoring and Alerting
Metrics to Monitor
System: CPU, RAM, disk usage, load average, network I/O.

Application: request rate, latency (p50, p95, p99), error rate, active sessions.

Database: query count, slow queries, connection pool usage.

Business: user signups, conversion rate, revenue.

Tools
Prometheus + Grafana: Standard open-source stack.

Node Exporter for system metrics.

Blackbox Exporter for endpoint availability.

Alertmanager for alert routing.

Cloud native: AWS CloudWatch, Azure Monitor, GCP Monitoring.

Uptime Monitoring
Pingdom, Statuspage, Better Uptime, Uptime Kuma (self-hosted).

Health checks: expose a /health endpoint that returns 200 if the service is healthy.

Backup Strategies
The 3-2-1 Rule
3 copies of data.

2 different media types (e.g., SSD + tape, or local + cloud).

1 copy off-site (e.g., cloud or remote data centre).

Backup Types
Full backup: copy everything (slow, space-heavy).

Incremental backup: copy only changes since last full or incremental (fast, complex restore).

Differential backup: copy changes since last full (middle ground).

Database Backups
bash
# PostgreSQL
pg_dump dbname > backup.sql
pg_dumpall > all_backup.sql

# MySQL / MariaDB
mysqldump -u root -p dbname > backup.sql

# Restore
psql dbname < backup.sql
mysql -u root -p dbname < backup.sql
File Backups
bash
# Tar archive
tar -czf backup.tar.gz /var/lib/data

# Rsync to remote
rsync -avz /local/data/ user@backup-server:/backup/data/

# Cloud CLI (e.g., AWS S3)
aws s3 sync /local/data s3://my-bucket/backup/
Automated Backup Scheduling (cron)
cron
# Run daily at 2am
0 2 * * * /usr/local/bin/backup_script.sh
Cron and Scheduled Jobs
Cron Syntax
text
* * * * * command
│ │ │ │ │
│ │ │ │ └─ Day of week (0-7, 0=Sun)
│ │ │ └─── Month (1-12)
│ │ └───── Day of month (1-31)
│ └─────── Hour (0-23)
└───────── Minute (0-59)
Examples
cron
# Every 5 minutes
*/5 * * * * /path/to/script

# Every day at 3:15 AM
15 3 * * * /path/to/script

# Every Monday at 4 AM
0 4 * * 1 /path/to/script

# Every hour
0 * * * * /path/to/script
Managing Cron
bash
crontab -l          # List current user's cron jobs
crontab -e          # Edit
crontab -r          # Remove all
Anacron
Used for systems not running 24/7 (e.g., laptops), ensures jobs run eventually.

Package Management and Updates
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
Security Updates
Enable unattended-upgrades on Ubuntu for security patches:

bash
sudo apt install unattended-upgrades
sudo dpkg-reconfigure -plow unattended-upgrades
Docker in Production
Best Practices
Use specific image tags (python:3.12-slim) not latest.

Run containers as non-root user.

Scan images for vulnerabilities (docker scan, trivy).

Set resource limits (--memory, --cpus).

Use secrets (via Docker secrets or environment with care).

Keep images small: multi-stage builds, alpine base.

Docker Compose in Production
Set resource limits in docker-compose.yml:

yaml
services:
  app:
    image: myapp:1.0
    deploy:
      resources:
        limits:
          memory: 512M
          cpus: '0.5'
CI/CD Basics
Pipeline Stages
Build: Compile code, install dependencies.

Test: Run unit, integration, and lint checks.

Containerise: Build Docker image.

Push: Push image to container registry.

Deploy: Update staging/production environment.

Tools
GitHub Actions: Integrated with GitHub.

GitLab CI: Built into GitLab.

Jenkins: Traditional, highly configurable.

CircleCI, Travis CI: Popular third-party.

ArgoCD: GitOps for Kubernetes.

Example GitHub Action (simple):
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
System Tuning and Troubleshooting
Check Disk Space
bash
df -h                      # Human-readable disk usage
du -sh /* | sort -h        # Size of top-level directories
Check Memory Usage
bash
free -m                    # Memory in MB
vmstat 1 10                # Virtual memory statistics
top -o %MEM                # Sort processes by memory
Check CPU Load
bash
uptime                     # Load average over 1,5,15 minutes
top -o %CPU                # Sort processes by CPU
mpstat -P ALL 1 5          # Per-core CPU usage
Check Network
bash
netstat -i                 # Interface statistics
iftop                      # Live bandwidth usage (requires install)
nload                      # Another bandwidth monitor
Find Large Files
bash
find / -type f -size +100M -exec ls -lh {} \; 2>/dev/null
Infrastructure as Code (IaC)
Terraform
Declare cloud resources in HCL.

hcl
provider "aws" {
  region = "us-east-1"
}
resource "aws_instance" "web" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t2.micro"
}
Ansible
Agentless configuration management using YAML.

yaml
- name: Install nginx
  hosts: webservers
  tasks:
    - name: Install nginx
      apt:
        name: nginx
        state: present
Best Practices
Use modules and roles for reusability.

Store state remotely (S3, Terraform Cloud).

Use variables and secrets (AWS_SECRET_ACCESS_KEY via environment, not hardcoded).

Version control your IaC code.

Incident Response (On-call)
Checklist for Service Outage
Acknowledge the alert.

Assess scope: Which services/users are affected?

Identify the issue (look at logs, metrics, recent deployments).

Contain if possible (circuit breakers, feature flags).

Rollback or fix forward.

Communicate status to stakeholders and users (status page).

Document the incident timeline and actions.

Post-mortem: within 24–48 hours, write a root cause analysis (RCA) and action items to prevent recurrence.
