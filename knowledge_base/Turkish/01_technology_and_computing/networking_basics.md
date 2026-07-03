# Ağ Temelleri

Geliştiriciler ve sistem yöneticileri için temel kavramları, protokolleri, komutları ve sorun gidermeyi kapsayan pratik bir başvuru.

---

## OSI Modeli (7 Katman)

Ağ iletişimini anlamaya yönelik kavramsal bir çerçeve.

| Layer | Name | Function | Example protocols |
|-------|------|----------|-------------------|
| 7 | Application | Son kullanıcı hizmetleri | HTTP, HTTPS, FTP, SMTP, DNS, SSH |
| 6 | Presentation | Veri biçimlendirme, şifreleme, sıkıştırma | TLS, JPEG, ASCII |
| 5 | Session | Bağlantı yönetimi | NetBIOS, RPC |
| 4 | Transport | Uçtan uca teslimat, hata düzeltme, akış kontrolü | TCP, UDP |
| 3 | Network | Yönlendirme, adresleme | IP, ICMP, OSPF, BGP |
| 2 | Data Link | Çerçeveleme, hata tespiti, MAC adresleri | Ethernet, Wi-Fi, PPP |
| 1 | Physical | Ham bit iletimi | Ethernet kabloları, fiber optik, radyo dalgaları |

Pratikte, internet için **TCP/IP model** (4 katman: Link, Internet, Transport, Application) daha yaygın kullanılır.

---

## IP Adresleme

### IPv4
- 32 bit adres, dört oktet olarak yazılır: `192.168.1.1`
- Toplam: yaklaşık 4,3 milyar adres (ancak pratikte tükenmiştir).

### IPv6
- 128 bit adres, hexadecimal biçimde yazılır: `2001:0db8:85a3:0000:0000:8a2e:0370:7334`
- Toplam: 2¹²⁸ adres (pratikte sınırsız).

### Private IP Aralıkları (RFC 1918)
Bunlar internet üzerinde yönlendirilemez; yerel ağların içinde kullanılır:
- `10.0.0.0/8` (10.0.0.0 – 10.255.255.255)
- `172.16.0.0/12` (172.16.0.0 – 172.31.255.255)
- `192.168.0.0/16` (192.168.0.0 – 192.168.255.255)

### CIDR Gösterimi
`192.168.1.0/24`, ilk 24 bitin ağ öneki, son 8 bitin ise host kısmı olduğu anlamına gelir. `192.168.1.0` ile `192.168.1.255` arasındaki adresleri kapsar.

---

## DNS (Domain Name System)

Alan adlarını (ör. `example.com`) IP adreslerine eşler.

### Record Türleri
| Type | Purpose |
|------|---------|
| **A** | Alan adını IPv4 adresine eşler |
| **AAAA** | Alan adını IPv6 adresine eşler |
| **CNAME** | Başka bir alan adına takma ad |
| **MX** | Mail exchange sunucusu |
| **TXT** | Serbest metin (SPF, DKIM, doğrulama) |
| **NS** | Alan adı için nameserver |
| **SRV** | Hizmet kaydı (ör. SIP için) |

### Common Tools
```bash
dig example.com            # DNS lookup (detailed)
nslookup example.com       # DNS lookup (simpler)
host example.com           # Quick lookup
dig -x 8.8.8.8             # Reverse lookup (IP to name)

Bağlantı Noktaları ve Protokoller
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
Açık portları kontrol et
bash
ss -tulpn                 # Linux: listen and established sockets
netstat -an               # Older tool
lsof -i :8080             # See process using port 8080
nmap localhost            # Scan local ports
TCP ve UDP
Özellik	TCP	UDP
Bağlantı	Connection-oriented (handshake)	Connectionless
Güvenilirlik	Guaranteed delivery, retransmission	Best effort (may drop packets)
Sıralama	Preserves order	No ordering guarantee
Akış kontrolü	Yes (sliding window)	No
Kullanım alanları	Web (HTTP), email, SSH, file transfer	DNS, streaming, VoIP, gaming, SNMP
Başlık boyutu	20–60 bytes	8 bytes
HTTP ve HTTPS
HTTP Methods
GET: Bir kaynağı alır (idempotent, safe).

POST: Veri gönderir (idempotent değildir).

PUT: Bir kaynağı günceller/değiştirir (idempotent).

PATCH: Kısmi güncelleme.

DELETE: Bir kaynağı kaldırır (idempotent).

Status Codes
1xx: Bilgilendirme (100 Continue).

2xx: Başarı (200 OK, 201 Created, 204 No Content).

3xx: Yönlendirme (301 Moved Permanently, 302 Found, 304 Not Modified).

4xx: İstemci hatası (400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found, 429 Too Many Requests).

5xx: Sunucu hatası (500 Internal Server Error, 502 Bad Gateway, 503 Service Unavailable).

Headers
Content-Type: medya türü (application/json, text/html).

Authorization: kimlik bilgileri (ör. ******

Cache-Control: önbellekleme politikası.

CORS headers: Access-Control-Allow-Origin, vb.

TLS/SSL
HTTP trafiğini şifreler (HTTPS = TLS üzerinden HTTP).

Certificate Authority'lerden (CA) gelen sertifikalar sunucunun kimliğini doğrular.

İstemci tarafında sertifika zincirini ve hostname'i doğrulayın.

Firewalls and NAT
Firewall
Kurallara göre trafiği filtreler (source IP, dest IP, port, protocol).

Stateful firewall'lar bağlantı durumlarını izler.

NAT (Network Address Translation)
Private IP'leri internet erişimi için public IP'ye çevirir.

Port forwarding: public bir portu içteki bir host/port'a eşler.

Yaygın Ağ Komutları
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
Bir Porta Erişim
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
Subnetting (Hızlı Başvuru)
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
Reverse Proxy olarak Nginx
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

Araçlar
Nginx, HAProxy (yazılım)

AWS ELB, Azure Load Balancer, GCP Cloud Load Balancing (bulut)

Sorun Giderme Kontrol Listesi
Fiziksel bağlantı açık mı? (Kabloları, Wi-Fi bağlantısını kontrol edin.)

Gateway'e ping atabiliyor musunuz? (ör. ping 192.168.1.1).

Harici bir IP'ye ping atabiliyor musunuz? (ör. 8.8.8.8).

Bir alan adını çözümleyebiliyor musunuz? (dig google.com).

Uygulama beklenen portta dinliyor mu? (ss -tulpn | grep 8080).

Firewall portu engelliyor mu? (iptables/ufw veya cloud security group'ları kontrol edin.)

Uygulama loglarında hata var mı?

TLS sertifikası geçerli ve güvenilir mi? (openssl s_client -connect example.com:443).

text

---

## File 6: `devops_sysadmin.md`

```markdown
# DevOps ve Sistem Yönetimi

Sunucuları yönetmek, operasyonları otomatikleştirmek ve güvenilir altyapıyı sürdürmek için pratik bir rehber.

---

## SSH (Secure Shell)

### Anahtar Üretimi
```bash
ssh-keygen -t ed25519 -C "your_email@example.com"   # Modern and secure
ssh-keygen -t rsa -b 4096 -C "your_email@example.com" # Fallback
Public Key'yi Sunucuya Kopyalama
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
Yaygın SSH Komutları
bash
ssh user@host                    # Connect
ssh -J jumpuser@jumphost user@target   # Proxy jump
scp file.txt user@host:/path/     # Copy file to remote
scp user@host:/path/file.txt .    # Copy from remote
rsync -avz -e ssh ./local/ user@host:/remote/  # Efficient sync
SSH'yi Sıkılaştırma
Disable root login: PermitRootLogin no

Use key-based auth only: PasswordAuthentication no

Varsayılan portu değiştirin (isteğe bağlı, security through obscurity).

Erişimi kısıtlamak için AllowUsers veya AllowGroups'u etkinleştirin.

Systemd (Linux Hizmet Yönetimi)
Yaygın Komutlar
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
Bir systemd Service Unit Oluşturma
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
Ardından:

bash
sudo systemctl daemon-reload
sudo systemctl enable myapp
sudo systemctl start myapp
Journalctl (Logları Görüntüleme)
bash
journalctl -u myapp              # Logs for service
journalctl -f                    # Follow (tail) logs
journalctl --since "1 hour ago"
journalctl _PID=1234             # Filter by process ID
Logging Stratejileri
Structured Logging
Logları makine tarafından ayrıştırılabilir hale getirmek için JSON formatı kullanın:

python
import structlog
logger = structlog.get_logger()
logger.info("user_login", user_id=123, ip="192.168.1.1")
Log Seviyeleri
DEBUG: ayrıntılı teşhis.

INFO: genel olaylar (başlatma, durdurma, normal işlemler).

WARN: beklenmedik ama kritik olmayan durum.

ERROR: belirli bir işlemi engelleyen hata.

FATAL/CRITICAL: sistem kapanması.

Log Aggregation
ELK Stack (Elasticsearch, Logstash, Kibana) veya Elastic Cloud.

Loki + Grafana (hafif alternatif).

Datadog, Splunk, Sumo Logic (SaaS).

Log Rotation (logrotate)
Logların diskleri doldurmasını önleyin. /etc/logrotate.d/myapp yapılandırması:

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
İzlenecek Metrikler
Sistem: CPU, RAM, disk kullanımı, load average, network I/O.

Uygulama: istek oranı, gecikme (p50, p95, p99), hata oranı, aktif oturumlar.

Veritabanı: sorgu sayısı, yavaş sorgular, connection pool kullanımı.

İş: kullanıcı kayıtları, dönüşüm oranı, gelir.

Araçlar
Prometheus + Grafana: Standart open-source yığın.

Sistem metrikleri için Node Exporter.

Uç nokta erişilebilirliği için Blackbox Exporter.

Uyarı yönlendirme için Alertmanager.

Cloud native: AWS CloudWatch, Azure Monitor, GCP Monitoring.

Uptime Monitoring
Pingdom, Statuspage, Better Uptime, Uptime Kuma (self-hosted).

Health check'ler: hizmet sağlıklıysa 200 döndüren bir /health endpoint'i sunun.

Backup Strategies
3-2-1 Kuralı
3 veri kopyası.

2 farklı ortam türü (ör. SSD + tape veya local + cloud).

1 off-site kopya (ör. cloud veya uzak veri merkezi).

Backup Türleri
Full backup: her şeyi kopyalar (yavaş, çok yer kaplar).

Incremental backup: son full veya incremental yedekten beri yalnızca değişiklikleri kopyalar (hızlı, restore karmaşık).

Differential backup: son full backup'tan beri değişiklikleri kopyalar (orta yol).

Veritabanı Yedekleri
bash
# PostgreSQL
pg_dump dbname > backup.sql
pg_dumpall > all_backup.sql

# MySQL / MariaDB
mysqldump -u root -p dbname > backup.sql

# Restore
psql dbname < backup.sql
mysql -u root -p dbname < backup.sql
Dosya Yedekleri
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
Cron ve Zamanlanmış İşler
Cron Söz Dizimi
text
* * * * * command
│ │ │ │ │
│ │ │ │ └─ Day of week (0-7, 0=Sun)
│ │ │ └─── Month (1-12)
│ │ └───── Day of month (1-31)
│ └─────── Hour (0-23)
└───────── Minute (0-59)
Örnekler
cron
# Every 5 minutes
*/5 * * * * /path/to/script

# Every day at 3:15 AM
15 3 * * * /path/to/script

# Every Monday at 4 AM
0 4 * * 1 /path/to/script

# Every hour
0 * * * * /path/to/script
Cron Yönetimi
bash
crontab -l          # List current user's cron jobs
crontab -e          # Edit
crontab -r          # Remove all
Anacron
24/7 çalışmayan sistemlerde (ör. laptop'lar) kullanılır, işlerin eninde sonunda çalışmasını sağlar.

Paket Yönetimi ve Güncellemeler
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
Ubuntu'da güvenlik yamaları için unattended-upgrades'ı etkinleştirin:

bash
sudo apt install unattended-upgrades
sudo dpkg-reconfigure -plow unattended-upgrades
Production'da Docker
En İyi Uygulamalar
latest yerine belirli image tag'leri kullanın (python:3.12-slim).

Container'ları non-root kullanıcıyla çalıştırın.

Image'ları açıklar için tarayın (docker scan, trivy).

Kaynak sınırları belirleyin (--memory, --cpus).

Secret'ları kullanın (Docker secrets veya dikkatli çevre değişkeni kullanımıyla).

Image'ları küçük tutun: multi-stage build'ler, alpine base.

Production'da Docker Compose
docker-compose.yml içinde kaynak sınırları belirleyin:

yaml
services:
  app:
    image: myapp:1.0
    deploy:
      resources:
        limits:
          memory: 512M
          cpus: '0.5'
CI/CD Temelleri
Pipeline Aşamaları
Build: Kodu derle, bağımlılıkları kur.

Test: Unit, integration ve lint kontrollerini çalıştır.

Containerise: Docker image'ını oluştur.

Push: Image'ı container registry'ye gönder.

Deploy: Staging/production ortamını güncelle.

Araçlar
GitHub Actions: GitHub ile entegre.

GitLab CI: GitLab'a yerleşik.

Jenkins: Geleneksel, yüksek düzeyde yapılandırılabilir.

CircleCI, Travis CI: Popüler üçüncü taraf araçlar.

ArgoCD: Kubernetes için GitOps.

Örnek GitHub Action (basit):
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
Sistem Ayarı ve Sorun Giderme
Disk Alanını Kontrol Et
bash
df -h                      # Human-readable disk usage
du -sh /* | sort -h        # Size of top-level directories
Bellek Kullanımını Kontrol Et
bash
free -m                    # Memory in MB
vmstat 1 10                # Virtual memory statistics
top -o %MEM                # Sort processes by memory
CPU Yükünü Kontrol Et
bash
uptime                     # Load average over 1,5,15 minutes
top -o %CPU                # Sort processes by CPU
mpstat -P ALL 1 5          # Per-core CPU usage
Ağı Kontrol Et
bash
netstat -i                 # Interface statistics
iftop                      # Live bandwidth usage (requires install)
nload                      # Another bandwidth monitor
Büyük Dosyaları Bul
bash
find / -type f -size +100M -exec ls -lh {} \; 2>/dev/null
Infrastructure as Code (IaC)
Terraform
Cloud kaynaklarını HCL ile tanımlayın.

hcl
provider "aws" {
  region = "us-east-1"
}
resource "aws_instance" "web" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t2.micro"
}
Ansible
YAML kullanan agentsız yapılandırma yönetimi.

yaml
- name: Install nginx
  hosts: webservers
  tasks:
    - name: Install nginx
      apt:
        name: nginx
        state: present
En İyi Uygulamalar
Yeniden kullanılabilirlik için module ve role'ler kullanın.

State'i uzakta saklayın (S3, Terraform Cloud).

Değişken ve secret kullanın (AWS_SECRET_ACCESS_KEY'i hardcode etmeyin, environment üzerinden verin).

IaC kodunuzu sürüm kontrolünde tutun.

Incident Response (On-call)
Hizmet Kesintisi İçin Kontrol Listesi
Uyarıyı kabul edin.

Kapsamı değerlendirin: Hangi hizmetler/kullanıcılar etkilendi?

Sorunu belirleyin (loglara, metriklere, son dağıtımlara bakın).

Mümkünse sınırlandırın (circuit breaker'lar, feature flag'ler).

Rollback yapın veya ileriye dönük düzeltin.

Durumu paydaşlara ve kullanıcılara iletin (status page).

Olay zaman çizelgesini ve yapılan işlemleri belgelendirin.

Post-mortem: 24–48 saat içinde root cause analysis (RCA) ve tekrarını önleyecek action item'lar yazın.
