<!-- 
This file was automatically translated from English to Arabic.
Source: networking_basics.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# أساسيات الشبكات

مرجع عملي للمطورين ومسؤولي الأنظمة — يغطي المفاهيم الأساسية، والبروتوكولات، والأوامر، واستكشاف الأخطاء وإصلاحها.

---

## نموذج OSI (الطبقات السبع)

إطار تصوري لفهم كيفية الاتصال عبر الشبكات.

| الطبقة | الاسم | الوظيفة | أمثلة على البروتوكولات |
|-------|------|----------|-------------------|
| 7 | التطبيق | خدمات المستخدم النهائي | HTTP, HTTPS, FTP, SMTP, DNS, SSH |
| 6 | العرض | تنسيق البيانات، والتشفير، والضغط | TLS, JPEG, ASCII |
| 5 | الجلسة | إدارة الاتصال | NetBIOS, RPC |
| 4 | النقل | التسليم من طرف إلى طرف، وتصحيح الأخطاء، والتحكم في التدفق | TCP, UDP |
| 3 | الشبكة | التوجيه والعنونة | IP, ICMP, OSPF, BGP |
| 2 | ربط البيانات | التأطير، واكتشاف الأخطاء، وعناوين MAC | Ethernet, Wi-Fi, PPP |
| 1 | الفيزيائية | نقل البِتّات الخام | كابلات Ethernet، والألياف الضوئية، والموجات الراديوية |

عمليًا، يُستخدم **نموذج TCP/IP** (أربع طبقات: الربط، والإنترنت، والنقل، والتطبيق) بصورة أكثر شيوعًا على الإنترنت.

---

## عنونة IP

### IPv4
- عنوان بطول 32 بت، ويُكتب على شكل أربع مجموعات ثُمانية: `192.168.1.1`
- الإجمالي: نحو 4.3 مليارات عنوان (لكنه نَفِد عمليًا).

### IPv6
- عنوان بطول 128 بت، ويُكتب بالنظام الست عشري: `2001:0db8:85a3:0000:0000:8a2e:0370:7334`
- الإجمالي: 2¹²⁸ عنوانًا (عدد شبه غير محدود عمليًا).

### نطاقات IP الخاصة (RFC 1918)
هذه العناوين غير قابلة للتوجيه على الإنترنت، وتُستخدم داخل الشبكات المحلية:
- `10.0.0.0/8` (10.0.0.0 – 10.255.255.255)
- `172.16.0.0/12` (172.16.0.0 – 172.31.255.255)
- `192.168.0.0/16` (192.168.0.0 – 192.168.255.255)

### ترميز CIDR
يعني `192.168.1.0/24` أن أول 24 بت تمثل بادئة الشبكة، بينما تمثل آخر 8 بتات المضيفين. ويشمل العناوين من `192.168.1.0` إلى `192.168.1.255`.

---

## DNS (نظام أسماء النطاقات)

يربط أسماء النطاقات (مثل `example.com`) بعناوين IP.

### أنواع السجلات
| النوع | الغرض |
|------|---------|
| **A** | يربط النطاق بعنوان IPv4 |
| **AAAA** | يربط النطاق بعنوان IPv6 |
| **CNAME** | اسم مستعار يشير إلى اسم نطاق آخر |
| **MX** | خادم تبادل البريد |
| **TXT** | نص حر (SPF و DKIM والتحقق) |
| **NS** | خادم الأسماء الخاص بالنطاق |
| **SRV** | سجل خدمة (مثلًا لـ SIP) |

### الأدوات الشائعة
```bash
dig example.com            # DNS lookup (detailed)
nslookup example.com       # DNS lookup (simpler)
host example.com           # Quick lookup
dig -x 8.8.8.8             # Reverse lookup (IP to name)

المنافذ والبروتوكولات
المنافذ المعروفة (0–1023)
المنفذ	البروتوكول	الخدمة
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
فحص المنافذ المفتوحة
bash
ss -tulpn                 # Linux: listen and established sockets
netstat -an               # Older tool
lsof -i :8080             # See process using port 8080
nmap localhost            # Scan local ports
TCP مقابل UDP
الميزة	TCP	UDP
الاتصال	معتمد على الاتصال (مصافحة)	من دون اتصال
الاعتمادية	تسليم مضمون مع إعادة الإرسال	أفضل جهد ممكن (قد تُفقَد الحزم)
الترتيب	يحافظ على الترتيب	لا يوجد ضمان للترتيب
التحكم في التدفق	نعم (sliding window)	لا
حالات الاستخدام	الويب (HTTP)، والبريد الإلكتروني، و SSH، ونقل الملفات	DNS، والبث، و VoIP، والألعاب، و SNMP
حجم الترويسة	20–60 بايت	8 بايت
HTTP و HTTPS
طرائق HTTP
GET: استرجاع مورد (idempotent وآمن).

POST: إرسال بيانات (غير idempotent).

PUT: تحديث مورد أو استبداله (idempotent).

PATCH: تحديث جزئي.

DELETE: إزالة مورد (idempotent).

رموز الحالة
1xx: معلوماتية (100 Continue).

2xx: نجاح (200 OK، و 201 Created، و 204 No Content).

3xx: إعادة توجيه (301 Moved Permanently، و 302 Found، و 304 Not Modified).

4xx: خطأ من جهة العميل (400 Bad Request، و 401 Unauthorized، و 403 Forbidden، و 404 Not Found، و 429 Too Many Requests).

5xx: خطأ من جهة الخادم (500 Internal Server Error، و 502 Bad Gateway، و 503 Service Unavailable).

الترويسات
Content-Type: نوع الوسائط (application/json, text/html).

Authorization: بيانات الاعتماد (مثل: ******

Cache-Control: سياسة التخزين المؤقت.

ترويسات CORS: مثل Access-Control-Allow-Origin وغيرها.

TLS/SSL
يشفّر حركة HTTP (أي أن HTTPS = HTTP over TLS).

تتحقق الشهادات الصادرة من هيئات إصدار الشهادات (CAs) من هوية الخادم.

تحقّق من سلسلة الشهادات واسم المضيف على جهة العميل.

الجدران النارية و NAT
الجدار الناري
يُرشّح حركة المرور وفق القواعد (عنوان IP للمصدر، وعنوان IP للوجهة، والمنفذ، والبروتوكول).

تتعقب الجدران النارية ذات الحالة حالات الاتصال.

NAT (ترجمة عناوين الشبكة)
يحوّل عناوين IP الخاصة إلى عنوان IP عام للوصول إلى الإنترنت.

إعادة توجيه المنافذ: تربط منفذًا عامًا بمضيف/منفذ داخلي.

أوامر الشبكات الشائعة
اختبارات الاتصال
bash
ping google.com            # ICMP echo request
ping -c 4 8.8.8.8          # ping 4 times
traceroute google.com      # Trace the route (Linux)
tracert google.com         # Windows version
التوجيه
bash
ip route show              # Linux: routing table
route -n                   # Older Linux
netstat -r                 # Windows/Mac
واجهات الشبكة
bash
ip addr show               # List interfaces and IPs
ifconfig                   # Older command
DNS
bash
dig example.com
nslookup example.com
host example.com
اختبار الاتصال بمنفذ
bash
nc -zv google.com 443      # Netcat: check if port 443 is open
telnet google.com 443      # Telnet to port
curl -v https://google.com # Verbose output
الجدار الناري (Linux iptables/nftables)
bash
sudo ufw status            # Ubuntu: simple firewall
sudo iptables -L -n        # List rules
إحصاءات الشبكة
bash
ss -tulpn                  # Show listening sockets (Linux)
netstat -an                # All sockets (all OS)
تقسيم الشبكات الفرعية (مرجع سريع)
CIDR	قناع الشبكة	عدد العناوين	المضيفون القابلون للاستخدام
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
موازنة الحمل والوكالات العكسية
استخدام Nginx كوكيل عكسي
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
خوارزميات موازنة الحمل
التوزيع الدوري

أقل الاتصالات

تجزئة IP (ثبات الجلسة)

التوزيع الدوري المُرجّح

الأدوات
Nginx و HAProxy (برمجيات)

AWS ELB و Azure Load Balancer و GCP Cloud Load Balancing (سحابية)

قائمة التحقق لاستكشاف الأخطاء وإصلاحها
هل الوصلة الفيزيائية تعمل؟ (تحقق من الكابلات أو اتصال Wi-Fi).

هل يمكنك تنفيذ ping على البوابة؟ (مثلًا: ping 192.168.1.1).

هل يمكنك تنفيذ ping على عنوان IP خارجي؟ (مثلًا: 8.8.8.8).

هل يمكنك تحليل اسم نطاق؟ (dig google.com).

هل التطبيق يستمع على المنفذ المتوقع؟ (ss -tulpn | grep 8080).

هل يحجب الجدار الناري هذا المنفذ؟ (تحقق من iptables/ufw أو مجموعات الأمان السحابية).

هل توجد أي أخطاء في سجلات التطبيق؟

هل شهادة TLS صالحة وموثوق بها؟ (openssl s_client -connect example.com:443).

text

---

## الملف 6: `devops_sysadmin.md`

```markdown
# التشغيل والتطوير وإدارة الأنظمة

دليل عملي لإدارة الخوادم، وأتمتة العمليات، والحفاظ على بنية تحتية موثوقة.

---

## SSH (Secure Shell)

### إنشاء المفاتيح
```bash
ssh-keygen -t ed25519 -C "your_email@example.com"   # Modern and secure
ssh-keygen -t rsa -b 4096 -C "your_email@example.com" # Fallback
نسخ المفتاح العام إلى الخادم
bash
ssh-copy-id user@host
# Manual alternative:
cat ~/.ssh/id_ed25519.pub | ssh user@host "mkdir -p ~/.ssh && cat >> ~/.ssh/authorized_keys"
إعداد SSH (~/.ssh/config)
ssh-config
Host myserver
    HostName 192.168.1.10
    User ubuntu
    IdentityFile ~/.ssh/mykey
    Port 2222
أوامر SSH الشائعة
bash
ssh user@host                    # Connect
ssh -J jumpuser@jumphost user@target   # Proxy jump
scp file.txt user@host:/path/     # Copy file to remote
scp user@host:/path/file.txt .    # Copy from remote
rsync -avz -e ssh ./local/ user@host:/remote/  # Efficient sync
تقوية إعدادات SSH
تعطيل تسجيل دخول root: PermitRootLogin no

استخدم المصادقة بالمفاتيح فقط: PasswordAuthentication no

غيّر المنفذ الافتراضي (اختياريًا، كإجراء أمني محدود الفاعلية).

فعّل AllowUsers أو AllowGroups لتقييد الوصول.

Systemd (إدارة الخدمات في Linux)
الأوامر الشائعة
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
إنشاء وحدة خدمة systemd
أنشئ الملف /etc/systemd/system/myapp.service:

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
ثم:

bash
sudo systemctl daemon-reload
sudo systemctl enable myapp
sudo systemctl start myapp
Journalctl (عرض السجلات)
bash
journalctl -u myapp              # Logs for service
journalctl -f                    # Follow (tail) logs
journalctl --since "1 hour ago"
journalctl _PID=1234             # Filter by process ID
استراتيجيات التسجيل
التسجيل المنظّم
استخدم تنسيق JSON لجعل السجلات قابلة للتحليل آليًا:

python
import structlog
logger = structlog.get_logger()
logger.info("user_login", user_id=123, ip="192.168.1.1")
مستويات السجل
DEBUG: تشخيص تفصيلي.

INFO: أحداث عامة (البدء، والتوقف، والمعاملات العادية).

WARN: أمر غير متوقع لكنه غير قاتل.

ERROR: خطأ يمنع تنفيذ عملية محددة.

FATAL/CRITICAL: توقف النظام.

تجميع السجلات
ELK Stack (Elasticsearch, Logstash, Kibana) أو Elastic Cloud.

Loki + Grafana (بديل خفيف الوزن).

Datadog و Splunk و Sumo Logic (SaaS).

تدوير السجلات (logrotate)
امنع السجلات من ملء الأقراص. اضبط /etc/logrotate.d/myapp كما يلي:

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
المراقبة والتنبيه
المقاييس التي ينبغي مراقبتها
النظام: CPU، و RAM، واستخدام القرص، ومتوسط الحمل، وإدخال/إخراج الشبكة.

التطبيق: معدل الطلبات، وزمن الاستجابة (p50 و p95 و p99)، ومعدل الأخطاء، والجلسات النشطة.

قاعدة البيانات: عدد الاستعلامات، والاستعلامات البطيئة، واستخدام مجمع الاتصالات.

الأعمال: تسجيلات المستخدمين، ومعدل التحويل، والإيرادات.

الأدوات
Prometheus + Grafana: الحزمة المفتوحة المصدر القياسية.

Node Exporter لمقاييس النظام.

Blackbox Exporter لتوافر نقاط النهاية.

Alertmanager لتوجيه التنبيهات.

حلول سحابية أصلية: AWS CloudWatch و Azure Monitor و GCP Monitoring.

مراقبة التوافر
Pingdom و Statuspage و Better Uptime و Uptime Kuma (مستضاف ذاتيًا).

فحوصات السلامة: وفّر نقطة نهاية /health تُرجع 200 إذا كانت الخدمة سليمة.

استراتيجيات النسخ الاحتياطي
قاعدة 3-2-1
3 نسخ من البيانات.

نوعان مختلفان من وسائط التخزين (مثل SSD + tape، أو محلي + سحابي).

نسخة واحدة خارج الموقع (مثل السحابة أو مركز بيانات بعيد).

أنواع النسخ الاحتياطي
نسخ احتياطي كامل: نسخ كل شيء (بطيء ويستهلك مساحة كبيرة).

نسخ احتياطي تزايدي: ينسخ التغييرات فقط منذ آخر نسخة كاملة أو تزايدية (سريع لكن الاستعادة معقدة).

نسخ احتياطي تفاضلي: ينسخ التغييرات منذ آخر نسخة كاملة (حل وسط).

النسخ الاحتياطي لقواعد البيانات
bash
# PostgreSQL
pg_dump dbname > backup.sql
pg_dumpall > all_backup.sql

# MySQL / MariaDB
mysqldump -u root -p dbname > backup.sql

# Restore
psql dbname < backup.sql
mysql -u root -p dbname < backup.sql
النسخ الاحتياطي للملفات
bash
# Tar archive
tar -czf backup.tar.gz /var/lib/data

# Rsync to remote
rsync -avz /local/data/ user@backup-server:/backup/data/

# Cloud CLI (e.g., AWS S3)
aws s3 sync /local/data s3://my-bucket/backup/
جدولة النسخ الاحتياطي تلقائيًا (cron)
cron
# Run daily at 2am
0 2 * * * /usr/local/bin/backup_script.sh
Cron والمهام المجدولة
صيغة Cron
text
* * * * * command
│ │ │ │ │
│ │ │ │ └─ Day of week (0-7, 0=Sun)
│ │ │ └─── Month (1-12)
│ │ └───── Day of month (1-31)
│ └─────── Hour (0-23)
└───────── Minute (0-59)
أمثلة
cron
# Every 5 minutes
*/5 * * * * /path/to/script

# Every day at 3:15 AM
15 3 * * * /path/to/script

# Every Monday at 4 AM
0 4 * * 1 /path/to/script

# Every hour
0 * * * * /path/to/script
إدارة Cron
bash
crontab -l          # List current user's cron jobs
crontab -e          # Edit
crontab -r          # Remove all
Anacron
يُستخدم للأنظمة التي لا تعمل على مدار الساعة طوال أيام الأسبوع (مثل الحواسيب المحمولة)، ويضمن تشغيل المهام في نهاية المطاف.

إدارة الحزم والتحديثات
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
تحديثات الأمان
فعّل unattended-upgrades في Ubuntu لتثبيت التصحيحات الأمنية:

bash
sudo apt install unattended-upgrades
sudo dpkg-reconfigure -plow unattended-upgrades
Docker في بيئة الإنتاج
أفضل الممارسات
استخدم وسوم صور محددة (python:3.12-slim) بدلًا من latest.

شغّل الحاويات كمستخدم غير root.

افحص الصور بحثًا عن الثغرات (docker scan و trivy).

اضبط حدود الموارد (--memory و --cpus).

استخدم الأسرار (عبر Docker secrets أو متغيرات البيئة بحذر).

اجعل الصور صغيرة: بنى متعددة المراحل وقاعدة alpine.

Docker Compose في بيئة الإنتاج
اضبط حدود الموارد في docker-compose.yml:

yaml
services:
  app:
    image: myapp:1.0
    deploy:
      resources:
        limits:
          memory: 512M
          cpus: '0.5'
أساسيات CI/CD
مراحل خط الأنابيب
البناء: ترجمة الشيفرة وتثبيت الاعتماديات.

الاختبار: تشغيل اختبارات الوحدة، والتكامل، وفحوص lint.

التحويل إلى حاوية: بناء صورة Docker.

الدفع: رفع الصورة إلى سجل الحاويات.

النشر: تحديث بيئة staging/production.

الأدوات
GitHub Actions: مدمج مع GitHub.

GitLab CI: مدمج في GitLab.

Jenkins: تقليدي وقابل للتخصيص بدرجة عالية.

CircleCI و Travis CI: أدوات خارجية شائعة.

ArgoCD: GitOps لـ Kubernetes.

مثال على GitHub Action (بسيط):
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
ضبط النظام واستكشاف الأخطاء وإصلاحها
التحقق من مساحة القرص
bash
df -h                      # Human-readable disk usage
du -sh /* | sort -h        # Size of top-level directories
التحقق من استخدام الذاكرة
bash
free -m                    # Memory in MB
vmstat 1 10                # Virtual memory statistics
top -o %MEM                # Sort processes by memory
التحقق من حمل CPU
bash
uptime                     # Load average over 1,5,15 minutes
top -o %CPU                # Sort processes by CPU
mpstat -P ALL 1 5          # Per-core CPU usage
التحقق من الشبكة
bash
netstat -i                 # Interface statistics
iftop                      # Live bandwidth usage (requires install)
nload                      # Another bandwidth monitor
العثور على الملفات الكبيرة
bash
find / -type f -size +100M -exec ls -lh {} \; 2>/dev/null
البنية التحتية كرمز (IaC)
Terraform
تعريف الموارد السحابية بلغة HCL.

hcl
provider "aws" {
  region = "us-east-1"
}
resource "aws_instance" "web" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t2.micro"
}
Ansible
إدارة التهيئة من دون وكيل باستخدام YAML.

yaml
- name: Install nginx
  hosts: webservers
  tasks:
    - name: Install nginx
      apt:
        name: nginx
        state: present
أفضل الممارسات
استخدم الوحدات والأدوار لتعزيز إعادة الاستخدام.

خزّن الحالة عن بُعد (S3 أو Terraform Cloud).

استخدم المتغيرات والأسرار (مثل AWS_SECRET_ACCESS_KEY عبر البيئة، وليس بشكل مُضمَّن في الشيفرة).

استخدم التحكم بالإصدارات لشيفرة IaC الخاصة بك.

الاستجابة للحوادث (المناوبة)
قائمة التحقق عند انقطاع الخدمة
أقِرّ التنبيه.

قيّم النطاق: ما الخدمات أو المستخدمون المتأثرون؟

حدّد المشكلة (راجع السجلات، والمقاييس، وعمليات النشر الأخيرة).

احتوِ المشكلة إن أمكن (قواطع الدارات وأعلام الميزات).

نفّذ التراجع أو أصلح بالمضي قدمًا.

أبلغ أصحاب المصلحة والمستخدمين بالحالة (صفحة الحالة).

وثّق التسلسل الزمني للحادث والإجراءات المتخذة.
