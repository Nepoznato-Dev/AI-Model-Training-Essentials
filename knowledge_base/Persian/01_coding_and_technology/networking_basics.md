<!--
---
# Metadata
title: "Networking Basics"
description: "OSI model, TCP/IP, protocols, security"
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
tags: [networking, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "12 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
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
- آدرس 32 بیتی که به صورت چهار اکتت نوشته شده است:`192.168.1.1`
- مجموع: ~4.3 میلیارد آدرس (اما در عمل خسته شده است).
### IPv6
- آدرس 128 بیتی که به صورت هگز نوشته شده است:`2001:0db8:85a3:0000:0000:8a2e:0370:7334`
- مجموع: 2¹²8 آدرس (عملا بی نهایت).
### محدوده IP خصوصی (RFC 1918)
اینها در اینترنت قابل مسیریابی نیستند. مورد استفاده در شبکه های محلی:
-`10.0.0.0/8`(10.0.0.0 – 10.255.255.255)
-`172.16.0.0/12`(172.16.0.0 – 172.31.255.255)
-`192.168.0.0/16`(192.168.0.0 – 192.168.255.255)
### نماد CIDR
`192.168.1.0/24`به این معنی است که 24 بیت اول پیشوند شبکه هستند. 8 بیت آخر میزبان هستند. این شامل آدرس های`192.168.1.0`تا`192.168.1.255`است.
---

## DNS (سیستم نام دامنه)
نام های دامنه (مانند`example.com`) را به آدرس های IP نگاشت می کند.
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
### ابزارهای رایج```bash
dig example.com            # DNS lookup (detailed)
nslookup example.com       # DNS lookup (simpler)
host example.com           # Quick lookup
dig -x 8.8.8.8             # Reverse lookup (IP to name)
```

---

## پورت ها و پروتکل ها
### پورت های شناخته شده (0–1023)
| بندر | پروتکل | خدمات |
|------|----------|---------|
| 20، 21 | TCP | FTP |
| 22 | TCP | SSH |
| 23 | TCP | شبکه راه دور |
| 25 | TCP | SMTP |
| 53 | UDP/TCP | DNS |
| 80 | TCP | HTTP |
| 110 | TCP | POP3 |
| 123 | UDP | NTP |
| 143 | TCP | IMAP |
| 443 | TCP | HTTPS |
| 465 | TCP | SMTPS |
| 587 | TCP | SMTP (ارسال) |
| 993 | TCP | IMAPS |
| 995 | TCP | POP3S |
| 3306 | TCP | MySQL |
| 5432 | TCP | PostgreSQL |
| 6379 | TCP | ردیس |
| 27017 | TCP | MongoDB |
### پورت های باز را بررسی کنید
```bash
ss -tulpn                 # Linux: listen and established sockets
netstat -an               # Older tool
lsof -i :8080             # See process using port 8080
nmap localhost            # Scan local ports
```

---

## TCP در مقابل UDP
| ویژگی | TCP | UDP |
|---------|-----|-----|
| اتصال | اتصال گرا (دست دادن) | بدون اتصال |
| قابلیت اطمینان | تحویل تضمینی، ارسال مجدد | بهترین تلاش (ممکن است بسته ها را رها کند) |
| سفارش | حفظ سفارش | بدون ضمانت سفارش |
| کنترل جریان | بله (پنجره کشویی) | نه |
| موارد استفاده | وب (HTTP)، ایمیل، SSH، انتقال فایل | DNS، جریان، VoIP، بازی، SNMP |
| اندازه سربرگ | 20-60 بایت | 8 بایت |
---

## HTTP و HTTPS
### روش های HTTP
| روش | توضیحات |
|--------|------------|
| **دریافت ** | بازیابی یک منبع (ناتوان، ایمن) |
| **پست** | ارسال داده ها (نه بی قدرت) |
| ** قرار دادن ** | به روز رسانی/ جایگزینی یک منبع (idempotent) |
| **پچ** | به روز رسانی جزئی |
| **حذف ** | حذف یک منبع (idempotent) |
### کدهای وضعیت
| کد | معنی |
|------|---------|
| **1xx** | اطلاع رسانی (100 ادامه) |
| **2xx** | موفقیت (200 OK، 201 ایجاد، 204 بدون محتوا) |
| **3xx** | تغییر مسیر (301 به طور دائم منتقل شد، 302 مورد یافت شد، 304 تغییر نشد) |
| **4xx** | خطای مشتری (400 درخواست بد، 401 غیرمجاز، 403 ممنوع، 404 یافت نشد، 429 درخواست خیلی زیاد) |
| **5xx** | خطای سرور (500 خطای داخلی سرور، 502 دروازه بد، 503 سرویس در دسترس نیست) |
### سرصفحه ها
| سربرگ | هدف |
|--------|---------|
| `Content-Type`| نوع رسانه (`application/json`,`text/html`) |
| `Authorization`| اعتبارنامه (به عنوان مثال، `Bearer <token>`) |
| `Cache-Control`| سیاست ذخیره سازی |
| سربرگ CORS | `Access-Control-Allow-Origin`و غیره |
---

## TLS/SSL
ترافیک HTTP را رمزگذاری می کند (HTTPS = HTTP از طریق TLS).
- گواهینامه های مراجع صدور گواهی (CAs) سرور را احراز هویت می کنند.
- زنجیره گواهی و نام میزبان را در سمت مشتری تأیید کنید.
---

## فایروال و NAT
### فایروال
- ترافیک را بر اساس قوانین (IP منبع، IP مقصد، پورت، پروتکل) فیلتر می کند.
- فایروال های Stateful وضعیت های اتصال را ردیابی می کنند.
### NAT (ترجمه آدرس شبکه)
- IP های خصوصی را به یک IP عمومی برای دسترسی به اینترنت ترجمه می کند.
- ارسال پورت: یک پورت عمومی را به یک میزبان/پورت داخلی نگاشت می کند.
---

## دستورات رایج شبکه
### تست های اتصال
```bash
ping google.com            # ICMP echo request
ping -c 4 8.8.8.8          # ping 4 times
traceroute google.com      # Trace the route (Linux)
tracert google.com         # Windows version
```

### مسیریابی
```bash
ip route show              # Linux: routing table
route -n                   # Older Linux
netstat -r                 # Windows/Mac
```

### رابط های شبکه
```bash
ip addr show               # List interfaces and IPs
ifconfig                   # Older command
```

### DNS
```bash
dig example.com
nslookup example.com
host example.com
```

### اتصال به پورت
```bash
nc -zv google.com 443      # Netcat: check if port 443 is open
telnet google.com 443      # Telnet to port
curl -v https://google.com # Verbose output
```

### فایروال (iptables/nftables لینوکس)
```bash
sudo ufw status            # Ubuntu: simple firewall
sudo iptables -L -n        # List rules
```

### آمار شبکه
```bash
ss -tulpn                  # Show listening sockets (Linux)
netstat -an                # All sockets (all OS)
```

---

## زیرشبکه (ارجاع سریع)
| سیدر | ماسک شبکه | تعداد آدرس ها | هاست های قابل استفاده |
|------|---------|--------------------|-------------|
| /32 | 255.255.255.255 | 1 | 1 |
| /30 | 255.255.255.252 | 4 | 2 |
| /29 | 255.255.255.248 | 8 | 6 |
| /28 | 255.255.255.240 | 16 | 14 |
| /27 | 255.255.255.224 | 32 | 30 |
| /26 | 255.255.255.192 | 64 | 62 |
| /25 | 255.255.255.128 | 128 | 126 |
| /24 | 255.255.255.0 | 256 | 254 |
| /23 | 255.255.254.0 | 512 | 510 |
| /22 | 255.255.252.0 | 1024 | 1022 |
| /16 | 255.255.0.0 | 65,536 | 65,534 |
| /8 | 255.0.0.0 | 16,777,216 | 16,777,214 |
---

## Load Balancing و Reverse Proxies
### Nginx به عنوان پروکسی معکوس
```nginx
server {
    listen 80;
    server_name example.com;
    location / {
        proxy_pass http://localhost:3000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

### الگوریتم های متعادل کننده بار
- **دوباره**
- **کمترین اتصالات**
- ** هش IP ** (چسبندگی جلسه)
- **دوباره وزن دار**
### ابزار
- **Nginx، HAProxy** (نرم افزار)
- **AWS ELB، Azure Load Balancer، GCP Cloud Load Balancing** (ابر)
---

## چک لیست عیب یابی
1. آیا پیوند فیزیکی بالا است؟ (کابل ها، اتصال Wi-Fi را بررسی کنید).
2. آیا می توانید دروازه را پینگ کنید؟ (به عنوان مثال، `ping 192.168.1.1`).
3. آیا می توانید یک IP خارجی را پینگ کنید؟ (به عنوان مثال، `8.8.8.8`).
4. آیا می توانید یک دامنه را حل کنید؟ (`dig google.com`).
5. آیا برنامه در پورت مورد انتظار گوش می دهد؟ (`ss -tulpn | grep 8080`).
6. آیا فایروال پورت را مسدود می کند؟ (`iptables` /`ufw`یا گروه های امنیتی ابری را بررسی کنید).
7. آیا در لاگ برنامه ها خطایی وجود دارد؟
8. آیا گواهی TLS معتبر و قابل اعتماد است؟ (`openssl s_client -connect example.com:443`).