# أساسيات الشبكات

مرجع عملي للمطورين ومسؤولي الأنظمة — المفاهيم الأساسية والبروتوكولات والأوامر واستكشاف الأخطاء وإصلاحها.

---

## نموذج OSI (7 طبقات)

إطار مفاهيمي لفهم اتصالات الشبكة.

| الطبقة | الاسم | الوظيفة | أمثلة البروتوكولات |
|-------|------|----------|-------------------|
| 7 | التطبيق | خدمات المستخدم النهائي | HTTP, HTTPS, FTP, SMTP, DNS, SSH |
| 6 | العرض | تنسيق البيانات، التشفير، الضغط | TLS, JPEG, ASCII |
| 5 | الجلسة | إدارة الاتصال | NetBIOS, RPC |
| 4 | النقل | التسليم من طرف إلى طرف، تصحيح الأخطاء، التحكم في التدفق | TCP, UDP |
| 3 | الشبكة | التوجيه، العنونة | IP, ICMP, OSPF, BGP |
| 2 | ربط البيانات | التأطير، اكتشاف الأخطاء، عناوين MAC | Ethernet, Wi-Fi, PPP |
| 1 | الفيزيائية | نقل البتات الخام | كابلات Ethernet، الألياف الضوئية، الموجات الراديوية |

عمليًا، يُستخدم **نموذج TCP/IP** (4 طبقات: الربط، الإنترنت، النقل، التطبيق) بصورة أكثر شيوعًا على الإنترنت.

---

## عنونة IP

### IPv4
- عنوان بطول 32 بت، يُكتب على شكل أربع ثمانيات: `192.168.1.1`
- الإجمالي: حوالي 4.3 مليار عنوان (لكنها مستنفدة عمليًا).

### IPv6
- عنوان بطول 128 بت، يُكتب بالنظام الست عشري: `2001:0db8:85a3:0000:0000:8a2e:0370:7334`
- الإجمالي: 2¹²⁸ عنوانًا (عمليًا غير محدود).

### نطاقات IP الخاصة (RFC 1918)
هذه النطاقات غير قابلة للتوجيه على الإنترنت؛ وتُستخدم داخل الشبكات المحلية:
- `10.0.0.0/8` (10.0.0.0 – 10.255.255.255)
- `172.16.0.0/12` (172.16.0.0 – 172.31.255.255)
- `192.168.0.0/16` (192.168.0.0 – 192.168.255.255)

### ترميز CIDR
`192.168.1.0/24` يعني أن أول 24 بت هي بادئة الشبكة؛ وآخر 8 بتات مخصصة للمضيفين. ويشمل العناوين من `192.168.1.0` إلى `192.168.1.255`.

---

## DNS (نظام أسماء النطاقات)

يربط أسماء النطاقات (مثل `example.com`) بعناوين IP.

### أنواع السجلات
| النوع | الغرض |
|------|---------|
| **A** | يربط النطاق بعنوان IPv4 |
| **AAAA** | يربط النطاق بعنوان IPv6 |
| **CNAME** | اسم مستعار لاسم نطاق آخر |
| **MX** | خادم تبادل البريد |
| **TXT** | نص اعتباطي (SPF, DKIM, verification) |
| **NS** | خادم أسماء للنطاق |
| **SRV** | سجل خدمة (مثلًا لـ SIP) |

### الأدوات الشائعة
```bash
dig example.com            # استعلام DNS (تفصيلي)
nslookup example.com       # استعلام DNS (أبسط)
host example.com           # استعلام سريع
dig -x 8.8.8.8             # استعلام عكسي (من IP إلى الاسم)

المنافذ والبروتوكولات
المنافذ المعروفة (0–1023)
المنفذالبروتوكولالخدمة
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
587TCPSMTP (الإرسال)
993TCPIMAPS
995TCPPOP3S
3306TCPMySQL
5432TCPPostgreSQL
6379TCPRedis
27017TCPMongoDB
التحقق من المنافذ المفتوحة
bash
ss -tulpn                 # Linux: المقابس المستمعة والمُنشأة
netstat -an               # أداة أقدم
lsof -i :8080             # عرض العملية التي تستخدم المنفذ 8080
nmap localhost            # فحص المنافذ المحلية
TCP مقابل UDP
الميزةTCPUDP
الاتصالموجّه بالاتصال (مصافحة)عديم الاتصال
الاعتماديةتسليم مضمون، إعادة إرسالأفضل جهد (قد تُفقد الحزم)
الترتيبيحافظ على الترتيبلا يوجد ضمان للترتيب
التحكم في التدفقنعم (sliding window)لا
حالات الاستخدامالويب (HTTP)، البريد الإلكتروني، SSH، نقل الملفاتDNS، البث، VoIP، الألعاب، SNMP
حجم الترويسة20–60 bytes8 bytes
HTTP و HTTPS
أساليب HTTP
GET: استرجاع مورد (idempotent, safe).

POST: إرسال بيانات (ليس idempotent).

PUT: تحديث/استبدال مورد (idempotent).

PATCH: تحديث جزئي.

DELETE: إزالة مورد (idempotent).

رموز الحالة
1xx: معلوماتي (100 Continue).

2xx: نجاح (200 OK, 201 Created, 204 No Content).

3xx: إعادة توجيه (301 Moved Permanently, 302 Found, 304 Not Modified).

4xx: خطأ من العميل (400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found, 429 Too Many Requests).

5xx: خطأ من الخادم (500 Internal Server Error, 502 Bad Gateway, 503 Service Unavailable).

الترويسات
Content-Type: نوع الوسائط (application/json, text/html).

Authorization: بيانات الاعتماد (مثلًا، Bearer token).

Cache-Control: سياسة التخزين المؤقت.

ترويسات CORS: Access-Control-Allow-Origin، إلخ.

TLS/SSL
يشفّر حركة HTTP (HTTPS = HTTP over TLS).

تتحقق الشهادات الصادرة من Certificate Authorities (CAs) من هوية الخادم.

تحقق من سلسلة الشهادات واسم المضيف على جانب العميل.

جدران الحماية و NAT
جدار الحماية
يرشّح حركة المرور بناءً على القواعد (IP المصدر، IP الوجهة، المنفذ، البروتوكول).

تتبع جدران الحماية ذات الحالة حالات الاتصال.

NAT (Network Address Translation)
يحوّل عناوين IP الخاصة إلى عنوان IP عام للوصول إلى الإنترنت.

توجيه المنافذ: يربط منفذًا عامًا بمضيف/منفذ داخلي.

أوامر الشبكات الشائعة
اختبارات الاتصال
bash
ping google.com            # طلب echo عبر ICMP
ping -c 4 8.8.8.8          # تنفيذ ping 4 مرات
traceroute google.com      # تتبّع المسار (Linux)
tracert google.com         # إصدار Windows
التوجيه
bash
ip route show              # Linux: جدول التوجيه
route -n                   # Linux الأقدم
netstat -r                 # Windows/Mac
واجهات الشبكة
bash
ip addr show               # عرض الواجهات وعناوين IP
ifconfig                   # أمر أقدم
DNS
bash
dig example.com
nslookup example.com
host example.com
الاتصال بمنفذ
bash
nc -zv google.com 443      # Netcat: التحقق مما إذا كان المنفذ 443 مفتوحًا
telnet google.com 443      # Telnet إلى المنفذ
curl -v https://google.com # مخرجات تفصيلية
جدار الحماية (Linux iptables/nftables)
bash
sudo ufw status            # Ubuntu: جدار حماية بسيط
sudo iptables -L -n        # عرض القواعد
إحصاءات الشبكة
bash
ss -tulpn                  # عرض المقابس المستمعة (Linux)
netstat -an                # جميع المقابس (كل أنظمة التشغيل)
تقسيم الشبكات الفرعية (مرجع سريع)
CIDRقناع الشبكةعدد العناوينالمضيفون القابلون للاستخدام
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
موازنة الحمل والوكلاء العكسيون
Nginx كوكيل عكسي
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
التناوب

أقل الاتصالات

تجزئة IP (ثبات الجلسة)

التناوب الموزون

الأدوات
Nginx, HAProxy (برمجيات)

AWS ELB, Azure Load Balancer, GCP Cloud Load Balancing (سحابة)

قائمة التحقق لاستكشاف الأخطاء وإصلاحها
هل الوصلة الفيزيائية تعمل؟ (تحقق من الكابلات واتصال Wi-Fi).

هل يمكنك ping البوابة؟ (مثلًا، ping 192.168.1.1).

هل يمكنك ping عنوان IP خارجي؟ (مثلًا، 8.8.8.8).

هل يمكنك حل اسم نطاق؟ (dig google.com).

هل التطبيق يستمع على المنفذ المتوقع؟ (ss -tulpn | grep 8080).

هل جدار الحماية يحظر المنفذ؟ (تحقق من iptables/ufw أو مجموعات أمان السحابة).

هل توجد أي أخطاء في سجلات التطبيق؟

هل شهادة TLS صالحة وموثوقة؟ (openssl s_client -connect example.com:443).

text

---

## الملف 6: `devops_sysadmin.md`

```markdown
# DevOps وإدارة الأنظمة

دليل عملي لإدارة الخوادم وأتمتة العمليات والحفاظ على بنية تحتية موثوقة.

---

## SSH (Secure Shell)

### توليد المفاتيح
```bash
ssh-keygen -t ed25519 -C "your_email@example.com"   # حديث وآمن
ssh-keygen -t rsa -b 4096 -C "your_email@example.com" # بديل احتياطي
نسخ المفتاح العام إلى الخادم
bash
ssh-copy-id user@host
# بديل يدوي:
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
ssh user@host                    # اتصال
ssh -J jumpuser@jumphost user@target   # قفزة وكيلة
scp file.txt user@host:/path/     # نسخ ملف إلى البعيد
scp user@host:/path/file.txt .    # نسخ من البعيد
rsync -avz -e ssh ./local/ user@host:/remote/  # مزامنة فعّالة
تقوية SSH
تعطيل تسجيل دخول root: PermitRootLogin no

استخدام المصادقة بالمفاتيح فقط: PasswordAuthentication no

تغيير المنفذ الافتراضي (اختياري، أمان عبر الإخفاء).

تمكين AllowUsers أو AllowGroups لتقييد الوصول.

Systemd (إدارة الخدمات في Linux)
الأوامر الشائعة
bash
systemctl status nginx           # التحقق من حالة الخدمة
systemctl start nginx            # بدء الخدمة
systemctl stop nginx
systemctl restart nginx
systemctl reload nginx           # إعادة تحميل سلسة (إعادة قراءة الإعداد)
systemctl enable nginx           # البدء عند الإقلاع
systemctl disable nginx
systemctl list-units --type=service --all   # عرض جميع الخدمات
systemctl daemon-reload          # إعادة تحميل ملفات الوحدة بعد التعديل
إنشاء وحدة خدمة systemd
أنشئ /etc/systemd/system/myapp.service:

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
journalctl -u myapp              # سجلات الخدمة
journalctl -f                    # متابعة السجلات (tail)
journalctl --since "1 hour ago"
journalctl _PID=1234             # التصفية حسب معرّف العملية
استراتيجيات التسجيل
التسجيل المنظم
استخدم تنسيق JSON لجعل السجلات قابلة للتحليل آليًا:

python
import structlog
logger = structlog.get_logger()
logger.info("user_login", user_id=123, ip="192.168.1.1")
مستويات السجل
DEBUG: تشخيص تفصيلي.

INFO: أحداث عامة (البدء، التوقف، المعاملات الطبيعية).

WARN: أمر غير متوقع لكنه غير قاتل.

ERROR: خطأ يمنع عملية محددة.

FATAL/CRITICAL: إيقاف النظام.

تجميع السجلات
ELK Stack (Elasticsearch, Logstash, Kibana) أو Elastic Cloud.

Loki + Grafana (بديل خفيف الوزن).

Datadog, Splunk, Sumo Logic (SaaS).

تدوير السجلات (logrotate)
امنع السجلات من ملء الأقراص. اضبط /etc/logrotate.d/myapp:

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
المقاييس الواجب مراقبتها
النظام: CPU، RAM، استخدام القرص، متوسط الحمل، network I/O.

التطبيق: معدل الطلبات، الكمون (p50, p95, p99)، معدل الأخطاء، الجلسات النشطة.

قاعدة البيانات: عدد الاستعلامات، الاستعلامات البطيئة، استخدام مجمّع الاتصالات.

الأعمال: تسجيلات المستخدمين، معدل التحويل، الإيرادات.

الأدوات
Prometheus + Grafana: الحزمة القياسية مفتوحة المصدر.

Node Exporter لمقاييس النظام.

Blackbox Exporter لتوافر نقاط النهاية.

Alertmanager لتوجيه التنبيهات.

حلول السحابة الأصلية: AWS CloudWatch, Azure Monitor, GCP Monitoring.

مراقبة التوافر
Pingdom, Statuspage, Better Uptime, Uptime Kuma (مستضاف ذاتيًا).

فحوصات الصحة: وفّر نقطة نهاية /health تُرجع 200 إذا كانت الخدمة سليمة.

استراتيجيات النسخ الاحتياطي
قاعدة 3-2-1
3 نسخ من البيانات.

2 نوعان مختلفان من وسائط التخزين (مثلًا، SSD + شريط، أو محلي + سحابة).

1 نسخة خارج الموقع (مثلًا، السحابة أو مركز بيانات بعيد).

أنواع النسخ الاحتياطي
نسخ احتياطي كامل: نسخ كل شيء (بطيء ويستهلك مساحة كبيرة).

نسخ احتياطي تزايدي: نسخ التغييرات فقط منذ آخر نسخ كامل أو تزايدي (سريع واستعادة معقدة).

نسخ احتياطي تفاضلي: نسخ التغييرات منذ آخر نسخ كامل (حل وسط).

النسخ الاحتياطي لقواعد البيانات
bash
# PostgreSQL
pg_dump dbname > backup.sql
pg_dumpall > all_backup.sql

# MySQL / MariaDB
mysqldump -u root -p dbname > backup.sql

# استعادة
psql dbname < backup.sql
mysql -u root -p dbname < backup.sql
النسخ الاحتياطي للملفات
bash
# أرشيف Tar
tar -czf backup.tar.gz /var/lib/data

# Rsync إلى جهاز بعيد
rsync -avz /local/data/ user@backup-server:/backup/data/

# واجهة سطر أوامر السحابة (مثل AWS S3)
aws s3 sync /local/data s3://my-bucket/backup/
جدولة النسخ الاحتياطي الآلية (cron)
cron
# التشغيل يوميًا الساعة 2 صباحًا
0 2 * * * /usr/local/bin/backup_script.sh
Cron والمهام المجدولة
بنية Cron
text
* * * * * command
│ │ │ │ │
│ │ │ │ └─ يوم الأسبوع (0-7، 0=الأحد)
│ │ │ └─── الشهر (1-12)
│ │ └───── يوم الشهر (1-31)
│ └─────── الساعة (0-23)
└───────── الدقيقة (0-59)
أمثلة
cron
# كل 5 دقائق
*/5 * * * * /path/to/script

# كل يوم الساعة 3:15 صباحًا
15 3 * * * /path/to/script

# كل يوم اثنين الساعة 4 صباحًا
0 4 * * 1 /path/to/script

# كل ساعة
0 * * * * /path/to/script
إدارة Cron
bash
crontab -l          # عرض مهام cron للمستخدم الحالي
crontab -e          # تعديل
crontab -r          # إزالة الكل
Anacron
يُستخدم للأنظمة التي لا تعمل على مدار 24/7 (مثل الحواسيب المحمولة)، ويضمن تشغيل المهام في النهاية.

إدارة الحزم والتحديثات
Debian/Ubuntu (apt)
bash
sudo apt update                # تحديث قائمة الحزم
sudo apt upgrade               # ترقية جميع الحزم
sudo apt install git nginx
sudo apt remove git
sudo apt autoremove            # إزالة الاعتماديات غير المستخدمة
RHEL/CentOS/Fedora (dnf/yum)
bash
sudo dnf check-update
sudo dnf update
sudo dnf install git nginx
sudo dnf remove git
تحديثات الأمان
فعّل unattended-upgrades على Ubuntu للحصول على تصحيحات الأمان:

bash
sudo apt install unattended-upgrades
sudo dpkg-reconfigure -plow unattended-upgrades
Docker في بيئة الإنتاج
أفضل الممارسات
استخدم وسوم صور محددة (python:3.12-slim) وليس latest.

شغّل الحاويات كمستخدم غير root.

افحص الصور بحثًا عن الثغرات (docker scan, trivy).

اضبط حدود الموارد (--memory, --cpus).

استخدم الأسرار (عبر Docker secrets أو البيئة بحذر).

حافظ على صغر حجم الصور: multi-stage builds، وقاعدة alpine.

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
Build: تجميع الشيفرة، تثبيت الاعتماديات.

Test: تشغيل فحوصات الوحدة والتكامل و lint.

Containerise: بناء صورة Docker.

Push: دفع الصورة إلى سجل الحاويات.

Deploy: تحديث بيئة staging/production.

الأدوات
GitHub Actions: مدمج مع GitHub.

GitLab CI: مدمج في GitLab.

Jenkins: تقليدي وقابل للتخصيص بدرجة عالية.

CircleCI, Travis CI: حلول خارجية شائعة.

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
df -h                      # استخدام القرص بصيغة مقروءة
du -sh /* | sort -h        # حجم الأدلة ذات المستوى الأعلى
التحقق من استخدام الذاكرة
bash
free -m                    # الذاكرة بالميغابايت
vmstat 1 10                # إحصاءات الذاكرة الافتراضية
top -o %MEM                # فرز العمليات حسب الذاكرة
التحقق من حمل CPU
bash
uptime                     # متوسط الحمل خلال 1 و5 و15 دقيقة
top -o %CPU                # فرز العمليات حسب CPU
mpstat -P ALL 1 5          # استخدام CPU لكل نواة
التحقق من الشبكة
bash
netstat -i                 # إحصاءات الواجهات
iftop                      # استخدام عرض النطاق الترددي المباشر (يتطلب التثبيت)
nload                      # مراقب آخر لعرض النطاق الترددي
البحث عن الملفات الكبيرة
bash
find / -type f -size +100M -exec ls -lh {} \; 2>/dev/null
البنية التحتية كرمز (IaC)
Terraform
عرّف موارد السحابة باستخدام HCL.

hcl
provider "aws" {
  region = "us-east-1"
}
resource "aws_instance" "web" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t2.micro"
}
Ansible
إدارة التهيئة دون وكيل باستخدام YAML.

yaml
- name: Install nginx
  hosts: webservers
  tasks:
    - name: Install nginx
      apt:
        name: nginx
        state: present
أفضل الممارسات
استخدم الوحدات والأدوار لإعادة الاستخدام.

خزّن الحالة عن بُعد (S3, Terraform Cloud).

استخدم المتغيرات والأسرار (AWS_SECRET_ACCESS_KEY عبر البيئة، وليس مضمنًا في الشيفرة).

استخدم التحكم في الإصدارات لشيفرة IaC الخاصة بك.

الاستجابة للحوادث (On-call)
قائمة تحقق لانقطاع الخدمة
أقرّ بالتنبيه.

قيّم النطاق: ما الخدمات/المستخدمون المتأثرون؟

حدّد المشكلة (انظر إلى السجلات والمقاييس وعمليات النشر الأخيرة).

احتوِ المشكلة إن أمكن (circuit breakers, feature flags).

نفّذ rollback أو أصلح بالمضي قدمًا.

أبلغ أصحاب المصلحة والمستخدمين بالحالة (صفحة الحالة).

وثّق الجدول الزمني للحادث والإجراءات.

ما بعد الحادث: خلال 24–48 ساعة، اكتب تحليل السبب الجذري (RCA) وعناصر العمل لمنع التكرار.
