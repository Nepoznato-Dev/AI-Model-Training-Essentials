# مبانی شبکه

یک مرجع عملی برای توسعه دهندگان و sysadmin ها - مفاهیم اصلی، پروتکل ها، دستورات و عیب یابی.

---

## مدل OSI (7 لایه)

چارچوب مفهومی برای درک ارتباطات شبکه

| لایه | نام | تابع | نمونه پروتکل ها |
|-------|------|---------|------------------|
| 7 | برنامه | خدمات کاربر نهایی | HTTP، HTTPS، FTP، SMTP، DNS، SSH |
| 6 | ارائه | قالب بندی داده ها، رمزگذاری، فشرده سازی | TLS، JPEG، ASCII |
| 5 | جلسه | مدیریت اتصال | NetBIOS، RPC |
| 4 | حمل و نقل | تحویل سرتاسر، تصحیح خطا، کنترل جریان | TCP، UDP |
| 3 | شبکه | مسیریابی، آدرس دهی | IP، ICMP، OSPF، BGP |
| 2 | لینک داده | کادربندی، تشخیص خطا، آدرس های مک | اترنت، وای فای، PPP |
| 1 | فیزیکی | انتقال بیت خام | کابل اترنت، فیبر نوری، امواج رادیویی |

در عمل، ** مدل TCP/IP ** (4 لایه: پیوند، اینترنت، حمل و نقل، برنامه) بیشتر برای اینترنت استفاده می شود.

---

## آدرس IP

### IPv4
- آدرس 32 بیتی، نوشته شده به صورت چهار اکتت: `192.168.1.1`
- مجموع: ~4.3 میلیارد آدرس (اما در عمل خسته شده است).

### IPv6
- آدرس 128 بیتی، به صورت هگز نوشته شده است: `2001:0db8:85a3:0000:0000:8a2e:0370:7334`
- مجموع: 2¹²8 آدرس (عملا بی نهایت).

### محدوده IP خصوصی (RFC 1918)
اینها در اینترنت قابل مسیریابی نیستند. مورد استفاده در شبکه های محلی:
- `10.0.0.0/8` (10.0.0.0 – 10.255.255.255)
- `172.16.0.0/12` (172.16.0.0 – 172.31.255.255)
- `192.168.0.0/16` (192.168.0.0 – 192.168.255.255)

### نماد CIDR
`192.168.1.0/24` یعنی 24 بیت اول پیشوند شبکه هستند. 8 بیت آخر میزبان هستند. این شامل آدرس‌های `192.168.1.0` تا `192.168.1.255` است.

---

## DNS (سیستم نام دامنه)

نام های دامنه (به عنوان مثال، `example.com`) را به آدرس های IP نگاشت می کند.

### انواع رکورد
| نوع | هدف |
|------|---------|
| **A** | دامنه نقشه ها به آدرس IPv4 |
| **AAAA** | دامنه نقشه ها به آدرس IPv6 |
| **CNAME** | نام مستعار به نام دامنه دیگر |
| **MX** | سرور تبادل ایمیل |
| **TXT** | متن دلخواه (SPF، DKIM، تأیید) |
| **NS** | سرور نام برای دامنه |
| **SRV** | سابقه خدمات (به عنوان مثال، برای SIP) |

### ابزارهای رایج
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

Authorization: credentials (e.g., Bearer <token>).

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

```نشانه گذاری
# DevOps و مدیریت سیستم

راهنمای عملی برای مدیریت سرورها، خودکارسازی عملیات و حفظ زیرساخت قابل اعتماد.

---

## SSH (پوسته ایمن)

### نسل کلید
``باش
ssh-keygen -t ed25519 -C "your_email@example.com" # مدرن و ایمن
ssh-keygen -t rsa -b 4096 -C "your_email@example.com" # بازگشت
کلید عمومی را در سرور کپی کنید
بش
ssh-copy-id user@host
# جایگزین دستی:
cat ~/.ssh/id_ed25519.pub | ssh user@host "mkdir -p ~/.ssh && cat >> ~/.ssh/authorized_keys"
پیکربندی SSH (~/.ssh/config)
ssh-config
سرور من را میزبانی کنید
    نام میزبان 192.168.1.10
    کاربر اوبونتو
    IdentityFile ~/.ssh/mykey
    پورت 2222
دستورات رایج SSH
بش
ssh user@host # اتصال
ssh -J jumpuser@jumphost user@target # پرش پروکسی
scp file.txt user@host:/path/ # فایل را به ریموت کپی کنید
scp user@host:/path/file.txt.    # کپی از راه دور
rsync -avz -e ssh ./local/ user@host:/remote/ # همگام سازی کارآمد
سخت شدن SSH
غیرفعال کردن ورود به ریشه: PermitRootLogin no

فقط از احراز هویت مبتنی بر کلید استفاده کنید: PasswordAuthentication no

پورت پیش فرض را تغییر دهید (اختیاری، امنیت از طریق مبهم).

AllowUsers یا AllowGroups را برای محدود کردن دسترسی فعال کنید.

Systemd (مدیریت خدمات لینوکس)
دستورات مشترک
بش
systemctl status nginx # وضعیت سرویس را بررسی کنید
systemctl start nginx # سرویس را شروع کنید
systemctl stop nginx
systemctl nginx را ریستارت کنید
systemctl reload nginx # بارگذاری مجدد برازنده (پیکربندی مجدد را بخوانید)
systemctl nginx # Start را در بوت فعال کنید
systemctl nginx را غیرفعال کنید
systemctl list-unit --type=service --all # لیست همه سرویس ها
systemctl daemon-reload # فایل های واحد را پس از ویرایش مجدد بارگیری کنید
ایجاد یک واحد خدمات سیستمی
/etc/systemd/system/myapp.service را ایجاد کنید:

ini
[واحد]
توضیحات=برنامه پایتون من
بعد=network.target

[سرویس]
User=myuser
گروه = گروه من
WorkingDirectory=/opt/myapp
ExecStart=/usr/bin/python3 /opt/myapp/main.py
راه اندازی مجدد = همیشه
RestartSec=10
Environment="ENV=production"

[نصب]
WantedBy=multi-user.target
سپس:

بش
sudo systemctl daemon-reload
sudo systemctl myapp را فعال می کند
sudo systemctl myapp را راه اندازی می کند
Journalctl (مشاهده گزارش‌ها)
بش
journalctl -u myapp # گزارش برای سرویس
journalctl -f # سیاهههای مربوط (دم) را دنبال کنید
journalctl -- از "1 ساعت پیش"
journalctl _PID=1234 # فیلتر بر اساس شناسه فرآیند
استراتژی های ورود به سیستم
ورود به سیستم ساختار یافته
از فرمت JSON برای تجزیه‌پذیر کردن لاگ‌ها توسط ماشین استفاده کنید:

پایتون
واردات structlog
logger = structlog.get_logger()
logger.info("user_login", user_id=123, ip="192.168.1.1")
سطوح ورود به سیستم
DEBUG: تشخیص دقیق.

اطلاعات: رویدادهای عمومی (شروع، توقف، معاملات عادی).

هشدار: غیرمنتظره اما کشنده نیست.

ERROR: خطایی که از انجام یک عملیات خاص جلوگیری می کند.

FATAL/CRITICAL: خاموش شدن سیستم.

تجمیع ورود به سیستم
ELK Stack (Elasticsearch، Logstash، Kibana) یا Elastic Cloud.Loki + Grafana (جایگزین سبک وزن).

Datadog، Splunk، Sumo Logic (SaaS).

چرخش گزارش (logrotate)
از پر کردن دیسک‌ها از لاگ‌ها جلوگیری کنید. /etc/logrotate.d/myapp را پیکربندی کنید:

logrotate
/var/log/myapp/*.log {
    روزانه
    چرخش 7
    فشرده کنید
    تأخیر فشرده سازی
    missingok
    اطلاع رسانی
    0640 myuser mygroup را ایجاد کنید
}
نظارت و هشدار
معیارهایی برای نظارت
سیستم: CPU، RAM، استفاده از دیسک، میانگین بارگذاری، شبکه ورودی/خروجی.

برنامه: نرخ درخواست، تأخیر (p50، p95، p99)، میزان خطا، جلسات فعال.

پایگاه داده: تعداد پرس و جو، پرس و جوهای کند، استفاده از استخر اتصال.

کسب و کار: ثبت نام کاربر، نرخ تبدیل، درآمد.

ابزار
Prometheus + Grafana: پشته منبع باز استاندارد.

صادرکننده گره برای معیارهای سیستم.

صادرکننده Blackbox برای در دسترس بودن نقطه پایانی.

Alertmanager برای مسیریابی هشدار.

بومی ابر: AWS CloudWatch، Azure Monitor، GCP Monitoring.

مانیتورینگ آپتایم
Pingdom، Statuspage، Better Uptime، Uptime Kuma (خود میزبان).

بررسی سلامت: نقطه پایانی /health را در معرض دید قرار دهید که در صورت سالم بودن سرویس، 200 را برمی گرداند.

استراتژی های پشتیبان گیری
قانون 3-2-1
3 کپی از داده ها

2 نوع رسانه مختلف (به عنوان مثال، SSD + نوار، یا محلی + ابر).

1 کپی خارج از سایت (به عنوان مثال، ابر یا مرکز داده از راه دور).

انواع پشتیبان گیری
پشتیبان گیری کامل: همه چیز را کپی کنید (آهسته، فضای سنگین).

پشتیبان گیری افزایشی: فقط کپی تغییرات از آخرین مرحله کامل یا افزایشی (بازیابی سریع و پیچیده).

پشتیبان گیری دیفرانسیل: کپی تغییرات از آخرین بار کامل (میانه).

پشتیبان گیری از پایگاه داده
بش
# PostgreSQL
pg_dump dbname > backup.sql
pg_dumpall > all_backup.sql

# MySQL / MariaDB
mysqldump -u root -p dbname > backup.sql

#بازیابی
psql dbname < backup.sql
mysql -u root -p dbname < backup.sql
پشتیبان گیری از فایل ها
بش
# آرشیو تار
tar -czf backup.tar.gz /var/lib/data

# همگام سازی با کنترل از راه دور
rsync -avz /local/data/ user@backup-server:/backup/data/

# CLI Cloud (به عنوان مثال، AWS S3)
aws s3 sync /local/data s3://my-bucket/backup/
برنامه ریزی خودکار پشتیبان گیری (cron)
کرون
# هر روز ساعت 2 بامداد اجرا کنید
0 2 * * * /usr/local/bin/backup_script.sh
Cron و Jobs Scheduled
Cron Syntax
متن
* * * * * دستور
│ │ │ │ │
│ │ │ │ └─ روز هفته (0-7، 0 = خورشید)
│ │ │ └─── ماه (1-12)
│ │ └───── روز ماه (1-31)
│ └─────── ساعت (0-23)
└───────── دقیقه (0-59)
نمونه ها
کرون
# هر 5 دقیقه
*/5 * * * * /path/to/script

# هر روز ساعت 3:15 صبح
15 3 * * * /path/to/script

# هر دوشنبه ساعت 4 صبح
0 4 * * 1 /path/to/script

#هر ساعت
0 * * * * /path/to/script
مدیریت کرون
بش
crontab -l # فهرست کارهای cron کاربر فعلی
crontab -e # ویرایش
crontab -r # حذف همه
آناکرون
برای سیستم هایی که 24/7 کار نمی کنند (مثلاً لپ تاپ ها) استفاده می شود، تضمین می کند که کارها در نهایت اجرا می شوند.

مدیریت بسته و به روز رسانی
Debian/Ubuntu (Apt)
بش
به روز رسانی sudo apt # لیست بسته را به روز کنید
sudo apt upgrade # همه بسته ها را ارتقا دهید
sudo apt نصب git nginx
sudo apt حذف git
sudo apt autoremove # حذف وابستگی های استفاده نشده
RHEL/CentOS/Fedora (dnf/yum)
بش
به روز رسانی چک dnf sudo
به روز رسانی sudo dnf
sudo dnf نصب git nginx
sudo dnf git را حذف کنید
به روز رسانی های امنیتی
به روز رسانی های بدون نظارت را در اوبونتو برای وصله های امنیتی فعال کنید:

بش
sudo apt ارتقاءهای بدون نظارت را نصب می کند
sudo dpkg-reconfigure-plow unattended-upgrades
داکر در تولید
بهترین شیوه ها
از برچسب های تصویری خاص (python:3.12-slim) نه جدیدترین استفاده کنید.

کانتینرها را به عنوان کاربر غیر ریشه اجرا کنید.

تصاویر را برای آسیب‌پذیری‌ها اسکن کنید (اسکن docker، trivy).

محدودیت های منابع را تنظیم کنید (--حافظه، --cpus).

از اسرار استفاده کنید (از طریق Docker Secrets یا محیط با دقت).

تصاویر را کوچک نگه دارید: ساخت های چند مرحله ای، پایه های آلپاین.

Docker Compose در حال تولید
محدودیت منابع را در docker-compose.yml تنظیم کنید:

یامل
خدمات:
  برنامه:
    تصویر: myapp:1.0
    استقرار:
      منابع:
        محدودیت ها:
          حافظه: 512 مگابایت
          cpus: '0.5'
مبانی CI/CD
مراحل خط لوله
ساخت: کامپایل کد، نصب وابستگی ها.

تست: بررسی های واحد، ادغام و پرز را اجرا کنید.

Containerise: ساخت تصویر Docker.

Push: تصویر را به رجیستری کانتینر فشار دهید.

استقرار: محیط صحنه سازی/تولید را به روز کنید.

ابزار
اقدامات GitHub: یکپارچه با GitHub.

GitLab CI: ساخته شده در GitLab.

جنکینز: سنتی، بسیار قابل تنظیم.

CircleCI، Travis CI: شخص ثالث محبوب.

ArgoCD: GitOps برای Kubernetes.نمونه اکشن GitHub (ساده):
یامل
نام: CI
در: فشار دادن
مشاغل:
  ساخت:
    اجرا می شود: ubuntu-latest
    مراحل:
      - موارد استفاده: actions/checkout@v4
      - موارد استفاده: actions/setup-python@v5
        با:
          نسخه پایتون: '3.12'
      - run: pip install -r requires.txt
      - اجرا: pytest
تنظیم سیستم و عیب یابی
فضای دیسک را بررسی کنید
بش
df -h # استفاده از دیسک قابل خواندن توسط انسان
دو -ش /* | sort -h # اندازه دایرکتوری های سطح بالا
میزان استفاده از حافظه را بررسی کنید
بش
رایگان -m # حافظه در مگابایت
vmstat 1 10 # آمار حافظه مجازی
top -o %MEM # مرتب سازی فرآیندها بر اساس حافظه
بار CPU را بررسی کنید
بش
uptime # میانگین بارگیری بیش از 1،5،15 دقیقه
top -o %CPU # مرتب سازی فرآیندها بر اساس CPU
mpstat -P ALL 1 5 # استفاده از CPU در هر هسته
شبکه را بررسی کنید
بش
netstat -i # آمار رابط
iftop # استفاده از پهنای باند زنده (نیاز به نصب دارد)
nload # مانیتور پهنای باند دیگری
فایل های بزرگ را پیدا کنید
بش
find / -type f -size +100M -exec ls -lh {} \; 2>/dev/null
زیرساخت به عنوان کد (IaC)
Terraform
منابع ابری را در HCL اعلام کنید.

hcl
ارائه دهنده "aws" {
  region = "us-east-1"
}
منبع "aws_instance" "web" {
  ami = "ami-0c55b159cbfafe1f0"
  instance_type = "t2.micro"
}
پاسخگو
مدیریت پیکربندی بدون عامل با استفاده از YAML.

یامل
- نام: nginx را نصب کنید
  میزبان: وب سرورها
  وظایف:
    - نام: nginx را نصب کنید
      apt:
        نام: nginx
        حالت: حال
بهترین شیوه ها
از ماژول ها و نقش ها برای قابلیت استفاده مجدد استفاده کنید.

حالت ذخیره از راه دور (S3، Terraform Cloud).

از متغیرها و اسرار استفاده کنید (AWS_SECRET_ACCESS_KEY از طریق محیط، نه کدگذاری شده).

نسخه کنترل کد IaC شما.

پاسخ به حادثه (در حال تماس)
چک لیست برای قطع سرویس
هشدار را تصدیق کنید.

دامنه ارزیابی: کدام خدمات/کاربران تحت تأثیر قرار می گیرند؟

مشکل را شناسایی کنید (به گزارش‌ها، معیارها، استقرارهای اخیر نگاه کنید).

در صورت امکان شامل (شکن های مدار، پرچم های ویژگی).

عقبگرد یا اصلاح به جلو.

ارتباط وضعیت با ذینفعان و کاربران (صفحه وضعیت).

جدول زمانی حادثه و اقدامات را مستند کنید.

پس از مرگ: ظرف 24 تا 48 ساعت، یک تجزیه و تحلیل علت ریشه ای (RCA) و موارد اقدام برای جلوگیری از عود بنویسید.