# नेटवर्किंग की बुनियादी बातें

डेवलपर्स और सिस्टम एडमिन्स के लिए एक व्यावहारिक संदर्भ — मुख्य अवधारणाएँ, प्रोटोकॉल, कमांड, और समस्या-निवारण।

---

## OSI मॉडल (7 लेयर)

नेटवर्क संचार को समझने के लिए एक वैचारिक ढाँचा।

| परत | नाम | कार्य | उदाहरण प्रोटोकॉल |
|-------|------|----------|-------------------|
| 7 | Application | अंतिम-उपयोगकर्ता सेवाएँ | HTTP, HTTPS, FTP, SMTP, DNS, SSH |
| 6 | Presentation | डेटा फ़ॉर्मैटिंग, एन्क्रिप्शन, कंप्रेशन | TLS, JPEG, ASCII |
| 5 | Session | कनेक्शन प्रबंधन | NetBIOS, RPC |
| 4 | Transport | एंड-टू-एंड डिलीवरी, त्रुटि-सुधार, फ्लो कंट्रोल | TCP, UDP |
| 3 | Network | रूटिंग, एड्रेसिंग | IP, ICMP, OSPF, BGP |
| 2 | Data Link | फ़्रेमिंग, त्रुटि-पहचान, MAC पते | Ethernet, Wi-Fi, PPP |
| 1 | Physical | कच्चे बिट्स का संचरण | Ethernet cables, fiber optics, radio waves |

व्यवहार में, **TCP/IP model** (4 layers: Link, Internet, Transport, Application) इंटरनेट के लिए अधिक सामान्य रूप से उपयोग किया जाता है।

---

## IP एड्रेसिंग

### IPv4
- 32-bit पता, चार octets के रूप में लिखा जाता है: `192.168.1.1`
- कुल: ~4.3 अरब पते (लेकिन व्यवहार में समाप्त हो चुके हैं)।

### IPv6
- 128-bit पता, hex में लिखा जाता है: `2001:0db8:85a3:0000:0000:8a2e:0370:7334`
- कुल: 2¹²⁸ पते (व्यवहारिक रूप से असीमित)।

### निजी IP रेंज (RFC 1918)
ये इंटरनेट पर routable नहीं होते; स्थानीय नेटवर्क के अंदर उपयोग किए जाते हैं:
- `10.0.0.0/8` (10.0.0.0 – 10.255.255.255)
- `172.16.0.0/12` (172.16.0.0 – 172.31.255.255)
- `192.168.0.0/16` (192.168.0.0 – 192.168.255.255)

### CIDR Notation
`192.168.1.0/24` का अर्थ है कि पहले 24 bits नेटवर्क prefix हैं; अंतिम 8 bits hosts हैं। इसमें `192.168.1.0` से `192.168.1.255` तक के पते शामिल होते हैं।

---

## DNS (Domain Name System)

domain names (उदाहरण के लिए, `example.com`) को IP addresses से मैप करता है।

### रिकॉर्ड प्रकार
| Type | Purpose |
|------|---------|
| **A** | domain को IPv4 address से मैप करता है |
| **AAAA** | domain को IPv6 address से मैप करता है |
| **CNAME** | किसी अन्य domain name का alias |
| **MX** | mail exchange server |
| **TXT** | मनचाहा text (SPF, DKIM, verification) |
| **NS** | domain के लिए nameserver |
| **SRV** | service record (उदाहरण के लिए, SIP के लिए) |

### सामान्य उपकरण
```bash
dig example.com            # DNS lookup (विस्तृत)
nslookup example.com       # DNS lookup (सरल)
host example.com           # त्वरित lookup
dig -x 8.8.8.8             # Reverse lookup (IP से नाम)

पोर्ट और प्रोटोकॉल
प्रसिद्ध पोर्ट (0–1023)
PortProtocolService
20, 21TCPFTP
22TCPSSH
23TCPTelnet
25TCPSMTP
53UDP/TCPDNS
80TCPHTTP
110TCPPOP3
123UDPNTP
143TCPIMAP
443TCPHTTPS
465TCPSMTPS
587TCPSMTP (submission)
993TCPIMAPS
995TCPPOP3S
3306TCPMySQL
5432TCPPostgreSQL
6379TCPRedis
27017TCPMongoDB
खुले पोर्ट जाँचें
bash
ss -tulpn                 # Linux: listening और established sockets
netstat -an               # पुराना tool
lsof -i :8080             # port 8080 का उपयोग करने वाली process देखें
nmap localhost            # local ports scan करें
TCP बनाम UDP
FeatureTCPUDP
ConnectionConnection-oriented (handshake)Connectionless
ReliabilityGuaranteed delivery, retransmissionBest effort (packets छूट सकते हैं)
Orderingक्रम सुरक्षित रखता हैक्रम की कोई गारंटी नहीं
Flow controlहाँ (sliding window)नहीं
Use casesWeb (HTTP), email, SSH, file transferDNS, streaming, VoIP, gaming, SNMP
Header size20–60 bytes8 bytes
HTTP और HTTPS
HTTP मेथड्स
GET: किसी resource को प्राप्त करें (idempotent, safe)।

POST: डेटा submit करें (idempotent नहीं)।

PUT: किसी resource को update/replace करें (idempotent)।

PATCH: आंशिक update।

DELETE: किसी resource को हटाएँ (idempotent)।

स्टेटस कोड
1xx: सूचनात्मक (100 Continue)।

2xx: सफलता (200 OK, 201 Created, 204 No Content)।

3xx: पुनर्निर्देशन (301 Moved Permanently, 302 Found, 304 Not Modified)।

4xx: client त्रुटि (400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found, 429 Too Many Requests)।

5xx: server त्रुटि (500 Internal Server Error, 502 Bad Gateway, 503 Service Unavailable)।

हेडर्स
Content-Type: media type (application/json, text/html)।

Authorization: credentials (उदाहरण के लिए, `******`)।

Cache-Control: caching policy।

CORS हेडर्स: Access-Control-Allow-Origin, आदि।

TLS/SSL
HTTP traffic को encrypt करता है (HTTPS = HTTP over TLS)।

Certificate Authorities (CAs) से certificates server को authenticate करते हैं।

client side पर certificate chain और hostname सत्यापित करें।

Firewalls और NAT
Firewall
नियमों (source IP, dest IP, port, protocol) के आधार पर traffic को फ़िल्टर करता है।

Stateful firewalls connection states को track करते हैं।

NAT (Network Address Translation)
internet access के लिए private IPs को public IP में बदलता है।

Port forwarding: किसी public port को internal host/port से मैप करता है।

Common Networking Commands
Connectivity Tests
bash
ping google.com            # ICMP echo request
ping -c 4 8.8.8.8          # 4 बार ping करें
traceroute google.com      # route trace करें (Linux)
tracert google.com         # Windows version
Routing
bash
ip route show              # Linux: routing table
route -n                   # पुराना Linux
netstat -r                 # Windows/Mac
Network Interfaces
bash
ip addr show               # interfaces और IPs सूचीबद्ध करें
ifconfig                   # पुरानी command
DNS
bash
dig example.com
nslookup example.com
host example.com
Connectivity to a Port
bash
nc -zv google.com 443      # Netcat: जाँचें कि port 443 खुला है या नहीं
telnet google.com 443      # port पर Telnet
curl -v https://google.com # Verbose output
Firewall (Linux iptables/nftables)
bash
sudo ufw status            # Ubuntu: सरल firewall
sudo iptables -L -n        # rules सूचीबद्ध करें
Network Statistics
bash
ss -tulpn                  # listening sockets दिखाएँ (Linux)
netstat -an                # सभी sockets (सभी OS)
Subnetting (त्वरित संदर्भ)
CIDRNetmaskNumber of addressesUsable hosts
/32255.255.255.25511
/30255.255.255.25242
/29255.255.255.24886
/28255.255.255.2401614
/27255.255.255.2243230
/26255.255.255.1926462
/25255.255.255.128128126
/24255.255.255.0256254
/23255.255.254.0512510
/22255.255.252.01,0241,022
/16255.255.0.065,53665,534
/8255.0.0.016,777,21616,777,214
लोड बैलेंसिंग और रिवर्स प्रॉक्सी
Nginx को Reverse Proxy के रूप में
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
लोड बैलेंसिंग एल्गोरिदम
Round-robin

Least connections

IP hash (session stickiness)

Weighted round-robin

उपकरण
Nginx, HAProxy (software)

AWS ELB, Azure Load Balancer, GCP Cloud Load Balancing (cloud)

समस्या-निवारण चेकलिस्ट
क्या physical link up है? (cables, Wi-Fi connection जाँचें)।

क्या आप gateway को ping कर सकते हैं? (उदाहरण के लिए, ping 192.168.1.1)।

क्या आप किसी external IP को ping कर सकते हैं? (उदाहरण के लिए, 8.8.8.8)।

क्या आप किसी domain को resolve कर सकते हैं? (dig google.com)।

क्या application अपेक्षित port पर listening कर रही है? (ss -tulpn | grep 8080)।

क्या firewall port को block कर रहा है? (iptables/ufw या cloud security groups जाँचें)।

क्या application logs में कोई errors हैं?

क्या TLS certificate वैध और विश्वसनीय है? (openssl s_client -connect example.com:443)।

text

---

## फ़ाइल 6: `devops_sysadmin.md`

```markdown
# DevOps और सिस्टम प्रशासन

servers को प्रबंधित करने, operations को automate करने, और विश्वसनीय infrastructure बनाए रखने के लिए एक व्यावहारिक मार्गदर्शिका।

---

## SSH (Secure Shell)

### कुंजी निर्माण
```bash
ssh-keygen -t ed25519 -C "your_email@example.com"   # आधुनिक और सुरक्षित
ssh-keygen -t rsa -b 4096 -C "your_email@example.com" # fallback
Public Key को सर्वर पर कॉपी करें
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
सामान्य SSH कमांड
bash
ssh user@host                    # कनेक्ट करें
ssh -J jumpuser@jumphost user@target   # Proxy jump
scp file.txt user@host:/path/     # file को remote पर कॉपी करें
scp user@host:/path/file.txt .    # remote से कॉपी करें
rsync -avz -e ssh ./local/ user@host:/remote/  # कुशल sync
SSH को सुरक्षित बनाना
root login disable करें: PermitRootLogin no

केवल key-based auth का उपयोग करें: PasswordAuthentication no

default port बदलें (वैकल्पिक, अस्पष्टता के माध्यम से सुरक्षा)।

access सीमित करने के लिए AllowUsers या AllowGroups सक्षम करें।

Systemd (Linux सेवा प्रबंधन)
सामान्य कमांड
bash
systemctl status nginx           # service status जाँचें
systemctl start nginx            # service शुरू करें
systemctl stop nginx
systemctl restart nginx
systemctl reload nginx           # graceful reload (config दोबारा पढ़ें)
systemctl enable nginx           # boot पर शुरू करें
systemctl disable nginx
systemctl list-units --type=service --all   # सभी services सूचीबद्ध करें
systemctl daemon-reload          # editing के बाद unit files reload करें
systemd सेवा इकाई बनाना
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
Journalctl (लॉग देखें)
bash
journalctl -u myapp              # service के logs
journalctl -f                    # follow (tail) logs
journalctl --since "1 hour ago"
journalctl _PID=1234             # process ID से filter करें
लॉगिंग रणनीतियाँ
संरचित लॉगिंग
logs को machine-parseable बनाने के लिए JSON format का उपयोग करें:

python
import structlog
logger = structlog.get_logger()
logger.info("user_login", user_id=123, ip="192.168.1.1")
लॉग स्तर
DEBUG: विस्तृत diagnostic।

INFO: सामान्य घटनाएँ (start, stop, normal transactions)।

WARN: अप्रत्याशित लेकिन घातक नहीं।

ERROR: ऐसी त्रुटि जो किसी विशेष operation को रोकती है।

FATAL/CRITICAL: system shutdown।

लॉग एग्रीगेशन
ELK Stack (Elasticsearch, Logstash, Kibana) या Elastic Cloud.

Loki + Grafana (हल्का विकल्प)।

Datadog, Splunk, Sumo Logic (SaaS).

Log Rotation (logrotate)
logs को disks भरने से रोकें। /etc/logrotate.d/myapp कॉन्फ़िगर करें:

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
निगरानी और अलर्टिंग
निगरानी करने योग्य मेट्रिक्स
System: CPU, RAM, disk usage, load average, network I/O.

Application: request rate, latency (p50, p95, p99), error rate, active sessions.

Database: query count, slow queries, connection pool usage.

Business: user signups, conversion rate, revenue.

उपकरण
Prometheus + Grafana: मानक open-source stack.

system metrics के लिए Node Exporter.

endpoint availability के लिए Blackbox Exporter.

alert routing के लिए Alertmanager.

Cloud native: AWS CloudWatch, Azure Monitor, GCP Monitoring.

अपटाइम निगरानी
Pingdom, Statuspage, Better Uptime, Uptime Kuma (self-hosted).

Health checks: ऐसा /health endpoint expose करें जो service के स्वस्थ होने पर 200 लौटाए।

बैकअप रणनीतियाँ
3-2-1 नियम
डेटा की 3 copies.

2 अलग media types (उदाहरण के लिए, SSD + tape, या local + cloud)।

1 copy off-site (उदाहरण के लिए, cloud या remote data centre)।

बैकअप प्रकार
Full backup: सब कुछ कॉपी करें (धीमा, अधिक स्थान लेने वाला)।

Incremental backup: पिछली full या incremental backup के बाद हुए बदलाव ही कॉपी करें (तेज़, restore जटिल)।

Differential backup: पिछली full backup के बाद हुए बदलाव कॉपी करें (मध्य मार्ग)।

डेटाबेस बैकअप
bash
# PostgreSQL
pg_dump dbname > backup.sql
pg_dumpall > all_backup.sql

# MySQL / MariaDB
mysqldump -u root -p dbname > backup.sql

# Restore
psql dbname < backup.sql
mysql -u root -p dbname < backup.sql
फ़ाइल बैकअप
bash
# Tar archive
tar -czf backup.tar.gz /var/lib/data

# Rsync to remote
rsync -avz /local/data/ user@backup-server:/backup/data/

# Cloud CLI (उदाहरण के लिए, AWS S3)
aws s3 sync /local/data s3://my-bucket/backup/
स्वचालित बैकअप शेड्यूलिंग (cron)
cron
# प्रतिदिन 2am पर चलाएँ
0 2 * * * /usr/local/bin/backup_script.sh
Cron और अनुसूचित जॉब्स
Cron सिंटैक्स
text
* * * * * command
│ │ │ │ │
│ │ │ │ └─ सप्ताह का दिन (0-7, 0=Sun)
│ │ │ └─── महीना (1-12)
│ │ └───── महीने का दिन (1-31)
│ └─────── घंटा (0-23)
└───────── मिनट (0-59)
उदाहरण
cron
# हर 5 मिनट में
*/5 * * * * /path/to/script

# हर दिन 3:15 AM पर
15 3 * * * /path/to/script

# हर सोमवार 4 AM पर
0 4 * * 1 /path/to/script

# हर घंटे
0 * * * * /path/to/script
Cron प्रबंधन
bash
crontab -l          # वर्तमान उपयोगकर्ता की cron jobs सूचीबद्ध करें
crontab -e          # edit करें
crontab -r          # सब हटाएँ
Anacron
ऐसे systems के लिए उपयोगी जो 24/7 नहीं चलते (उदाहरण के लिए, laptops), यह सुनिश्चित करता है कि jobs अंततः चलें।

पैकेज प्रबंधन और अपडेट्स
Debian/Ubuntu (apt)
bash
sudo apt update                # package list update करें
sudo apt upgrade               # सभी packages upgrade करें
sudo apt install git nginx
sudo apt remove git
sudo apt autoremove            # अनुपयोगी dependencies हटाएँ
RHEL/CentOS/Fedora (dnf/yum)
bash
sudo dnf check-update
sudo dnf update
sudo dnf install git nginx
sudo dnf remove git
सुरक्षा अपडेट्स
security patches के लिए Ubuntu पर unattended-upgrades सक्षम करें:

bash
sudo apt install unattended-upgrades
sudo dpkg-reconfigure -plow unattended-upgrades
Docker in Production
सर्वोत्तम प्रथाएँ
विशिष्ट image tags (python:3.12-slim) का उपयोग करें, latest का नहीं।

containers को non-root user के रूप में चलाएँ।

images को vulnerabilities के लिए scan करें (docker scan, trivy)।

resource limits सेट करें (--memory, --cpus)।

secrets का उपयोग करें (Docker secrets या environment के माध्यम से, सावधानी से)।

images को छोटा रखें: multi-stage builds, alpine base.

Docker Compose in Production
docker-compose.yml में resource limits सेट करें:

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
पाइपलाइन चरण
Build: code compile करें, dependencies install करें।

Test: unit, integration, और lint checks चलाएँ।

Containerise: Docker image build करें।

Push: image को container registry में push करें।

Deploy: staging/production environment update करें।

उपकरण
GitHub Actions: GitHub के साथ integrated.

GitLab CI: GitLab में built into.

Jenkins: पारंपरिक, अत्यधिक configurable.

CircleCI, Travis CI: लोकप्रिय third-party.

ArgoCD: Kubernetes के लिए GitOps.

Example GitHub Action (सरल):
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
सिस्टम ट्यूनिंग और समस्या-निवारण
डिस्क स्पेस जाँचें
bash
df -h                      # human-readable disk usage
du -sh /* | sort -h        # top-level directories का आकार
मेमोरी उपयोग जाँचें
bash
free -m                    # MB में memory
vmstat 1 10                # virtual memory statistics
top -o %MEM                # processes को memory के अनुसार sort करें
CPU लोड जाँचें
bash
uptime                     # 1,5,15 मिनट का load average
top -o %CPU                # processes को CPU के अनुसार sort करें
mpstat -P ALL 1 5          # per-core CPU usage
नेटवर्क जाँचें
bash
netstat -i                 # interface statistics
iftop                      # live bandwidth usage (install आवश्यक)
nload                      # एक और bandwidth monitor
बड़ी files खोजें
bash
find / -type f -size +100M -exec ls -lh {} \; 2>/dev/null
Infrastructure as Code (IaC)
Terraform
HCL में cloud resources declare करें।

hcl
provider "aws" {
  region = "us-east-1"
}
resource "aws_instance" "web" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t2.micro"
}
Ansible
YAML का उपयोग करने वाला agentless configuration management.

yaml
- name: Install nginx
  hosts: webservers
  tasks:
    - name: Install nginx
      apt:
        name: nginx
        state: present
सर्वोत्तम प्रथाएँ
reusability के लिए modules और roles का उपयोग करें।

state को remotely store करें (S3, Terraform Cloud)।

variables और secrets का उपयोग करें (AWS_SECRET_ACCESS_KEY environment के माध्यम से, hardcoded नहीं)।

अपने IaC code का version control करें।

Incident Response (On-call)
सेवा बाधा के लिए चेकलिस्ट
alert स्वीकार करें।

scope का आकलन करें: कौन-सी services/users प्रभावित हैं?

issue पहचानें (logs, metrics, recent deployments देखें)।

यदि संभव हो तो contain करें (circuit breakers, feature flags)।

rollback करें या आगे बढ़कर fix करें।

stakeholders और users को status बताएँ (status page)।

action timeline और incident का दस्तावेज़ बनाएँ।

Post-mortem: 24–48 घंटे के भीतर, root cause analysis (RCA) और पुनरावृत्ति रोकने के लिए action items लिखें।
