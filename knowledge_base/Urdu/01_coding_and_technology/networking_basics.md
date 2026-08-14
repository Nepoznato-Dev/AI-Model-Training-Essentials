---
# Metadata
title: "Networking Basics"
description: "OSI model, TCP/IP, protocols, security"
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

# نیٹ ورکنگ کی بنیادی باتیں
ڈویلپرز اور سیسڈمینز کے لیے ایک عملی حوالہ — بنیادی تصورات، پروٹوکول، کمانڈز، اور ٹربل شوٹنگ۔
---

## OSI ماڈل (7 پرتیں)
نیٹ ورک مواصلات کو سمجھنے کے لیے ایک تصوراتی فریم ورک۔
| پرت | نام | فنکشن | پروٹوکول کی مثال |
|---------|------|------------|------|
| 7 | درخواست | اختتامی صارف کی خدمات | HTTP, HTTPS, FTP, SMTP, DNS, SSH |
| 6 | پیشکش | ڈیٹا فارمیٹنگ، انکرپشن، کمپریشن | TLS, JPEG, ASCII |
| 5 | سیشن | کنکشن مینجمنٹ | NetBIOS, RPC |
| 4 | ٹرانسپورٹ | اختتام سے آخر تک ترسیل، غلطی کی اصلاح، بہاؤ کنٹرول | TCP، UDP |
| 3 | نیٹ ورک | روٹنگ، ایڈریسنگ | IP، ICMP، OSPF، BGP |
| 2 | ڈیٹا لنک | فریمنگ، غلطی کا پتہ لگانا، میک ایڈریسز | ایتھرنیٹ، وائی فائی، پی پی پی |
| 1 | جسمانی | را بٹ ٹرانسمیشن | ایتھرنیٹ کیبلز، فائبر آپٹکس، ریڈیو لہریں |
عملی طور پر، **TCP/IP ماڈل** (4 تہوں: لنک، انٹرنیٹ، ٹرانسپورٹ، ایپلیکیشن) انٹرنیٹ کے لیے زیادہ استعمال ہوتا ہے۔
---

## آئی پی ایڈریسنگ
### IPv4
- 32 بٹ ایڈریس، چار آکٹٹس کے طور پر لکھا گیا:`192.168.1.1`
- کل: ~4.3 بلین پتے (لیکن عملی طور پر ختم)۔
### IPv6
- 128 بٹ ایڈریس، ہیکس میں لکھا ہوا:`2001:0db8:85a3:0000:0000:8a2e:0370:7334`
- کل: 2¹²⁸ پتے (عملی طور پر لامحدود)۔
### پرائیویٹ IP رینجز (RFC 1918)
یہ انٹرنیٹ پر روٹیبل نہیں ہیں۔ مقامی نیٹ ورک کے اندر استعمال کیا جاتا ہے:
-`10.0.0.0/8`(10.0.0.0 - 10.255.255.255)
-`172.16.0.0/12`(172.16.0.0 - 172.31.255.255)
-`192.168.0.0/16`(192.168.0.0 - 192.168.255.255)
### CIDR نوٹیشن
`192.168.1.0/24`کا مطلب ہے پہلے 24 بٹس نیٹ ورک کا سابقہ ہے۔ آخری 8 بٹس میزبان ہیں۔ اس میں`192.168.1.0`سے`192.168.1.255`پتے شامل ہیں۔
---

## DNS (ڈومین نیم سسٹم)
ڈومین ناموں کا نقشہ (مثال کے طور پر،`example.com`) IP پتوں پر۔
### ریکارڈ کی اقسام
| قسم | مقصد |
|------|---------|
| **A** | IPv4 ایڈریس پر نقشہ ڈومین |
| **AAAA** | IPv6 ایڈریس پر نقشہ ڈومین |
| **CNAME** | دوسرے ڈومین نام کا عرف |
| **MX** | میل ایکسچینج سرور |
| **TXT** | صوابدیدی متن (SPF, DKIM, تصدیق) |
| **NS** | ڈومین کے لیے نام سرور |
| **SRV** | سروس ریکارڈ (جیسے، SIP کے لیے) |
### عام ٹولز```bash
dig example.com            # DNS lookup (detailed)
nslookup example.com       # DNS lookup (simpler)
host example.com           # Quick lookup
dig -x 8.8.8.8             # Reverse lookup (IP to name)
```

---

## بندرگاہیں اور پروٹوکول
### معروف بندرگاہیں (0–1023)
| پورٹ | پروٹوکول | سروس |
|------|------------|---------|
| 20، 21 | TCP | FTP |
| 22 | TCP | SSH |
| 23 | TCP | ٹیل نیٹ |
| 25 | TCP | SMTP |
| 53 | UDP/TCP | DNS |
| 80 | TCP | HTTP |
| 110 | TCP | POP3 |
| 123 | UDP | NTP |
| 143 | TCP | IMAP |
| 443 | TCP | HTTPS |
| 465 | TCP | SMTPS |
| 587 | TCP | SMTP (جمع کرانے) |
| 993 | TCP | IMAPS |
| 995 | TCP | POP3S |
| 3306 | TCP | MySQL |
| 5432 | TCP | PostgreSQL |
| 6379 | TCP | Redis |
| 27017 | TCP | MongoDB |
### کھلی بندرگاہوں کو چیک کریں۔
```bash
ss -tulpn                 # Linux: listen and established sockets
netstat -an               # Older tool
lsof -i :8080             # See process using port 8080
nmap localhost            # Scan local ports
```

---

## TCP بمقابلہ UDP
| خصوصیت | TCP | UDP |
|---------|------|------|
| کنکشن | کنکشن پر مبنی (ہاتھ ملانا) | کنکشن کے بغیر |
| وشوسنییتا | ضمانت شدہ ترسیل، دوبارہ منتقلی | بہترین کوشش (پیکٹ چھوڑ سکتا ہے) |
| آرڈرنگ | آرڈر کو محفوظ رکھتا ہے | کوئی آرڈرنگ گارنٹی نہیں |
| بہاؤ کنٹرول | ہاں (سلائیڈنگ ونڈو) | نہیں |
| کیسز استعمال کریں | ویب (HTTP)، ای میل، SSH، فائل ٹرانسفر | DNS، سٹریمنگ، VoIP، گیمنگ، SNMP |
| ہیڈر کا سائز | 20-60 بائٹس | 8 بائٹس |
---

## HTTP اور HTTPS
### HTTP طریقے
| طریقہ | تفصیل |
|---------|---------------|
| ** حاصل کریں** | ایک وسیلہ بازیافت کریں (آدمی، محفوظ) |
| **پوسٹ** | ڈیٹا جمع کروائیں (ناکارہ نہیں) |
| ** ڈالیں** | وسیلہ کو اپ ڈیٹ/تبدیل کریں (آئیڈیمپوٹینٹ) |
| **پیچ** | جزوی اپ ڈیٹ |
| **ڈیلیٹ** | ایک وسیلہ کو ہٹا دیں (آدمی) |
### اسٹیٹس کوڈز
| کوڈ | معنی |
|------|---------|
| **1xx** | معلوماتی (100 جاری رکھیں) |
| **2xx** | کامیابی (200 ٹھیک، 201 تخلیق، 204 کوئی مواد نہیں) |
| **3xx** | ری ڈائریکشن (301 مستقل طور پر منتقل، 302 ملا، 304 تبدیل نہیں ہوا) |
| **4xx** | کلائنٹ کی غلطی (400 غلط درخواست، 401 غیر مجاز، 403 ممنوع، 404 نہیں ملی، 429 بہت زیادہ درخواستیں) |
| **5xx** | سرور کی خرابی (500 اندرونی سرور کی خرابی، 502 خراب گیٹ وے، 503 سروس دستیاب نہیں) |
### ہیڈرز
| ہیڈر | مقصد |
|---------|---------|
| `Content-Type`| میڈیا کی قسم (`application/json`,`text/html`) |
| `Authorization`| اسناد (مثال کے طور پر،`Bearer <token>`) |
| `Cache-Control`| کیشنگ پالیسی |
| CORS ہیڈر |  `Access-Control-Allow-Origin`، وغیرہ |
---

## TLS/SSL
HTTP ٹریفک کو خفیہ کرتا ہے (HTTPS = HTTP پر TLS)۔
- سرٹیفکیٹ اتھارٹیز (CAs) کے سرٹیفکیٹس سرور کی تصدیق کرتے ہیں۔
- کلائنٹ کی طرف سے سرٹیفکیٹ چین اور میزبان نام کی تصدیق کریں۔
---

## فائر والز اور NAT
### فائر وال
- قوانین کی بنیاد پر ٹریفک کو فلٹر کرتا ہے (ماخذ آئی پی، ڈیسٹ آئی پی، پورٹ، پروٹوکول)۔
- ریاستی فائر وال کنکشن کی حالتوں کو ٹریک کرتے ہیں۔
### NAT (نیٹ ورک ایڈریس کا ترجمہ)
- انٹرنیٹ تک رسائی کے لیے نجی آئی پی کا عوامی IP میں ترجمہ کرتا ہے۔
- پورٹ فارورڈنگ: ایک عوامی بندرگاہ کو اندرونی میزبان/پورٹ سے نقشہ بناتا ہے۔
---

## عام نیٹ ورکنگ کمانڈز
### کنیکٹیویٹی ٹیسٹ
```bash
ping google.com            # ICMP echo request
ping -c 4 8.8.8.8          # ping 4 times
traceroute google.com      # Trace the route (Linux)
tracert google.com         # Windows version
```

### روٹنگ
```bash
ip route show              # Linux: routing table
route -n                   # Older Linux
netstat -r                 # Windows/Mac
```

### نیٹ ورک انٹرفیس
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

### بندرگاہ سے رابطہ
```bash
nc -zv google.com 443      # Netcat: check if port 443 is open
telnet google.com 443      # Telnet to port
curl -v https://google.com # Verbose output
```

### فائر وال (لینکس iptables/nftables)
```bash
sudo ufw status            # Ubuntu: simple firewall
sudo iptables -L -n        # List rules
```

### نیٹ ورک کے اعدادوشمار
```bash
ss -tulpn                  # Show listening sockets (Linux)
netstat -an                # All sockets (all OS)
```

---

## سب نیٹنگ (فوری حوالہ)
| CIDR | نیٹ ماسک | پتوں کی تعداد | قابل استعمال میزبان |
|------|---------|---------|---------------|
| /32 | 255.255.255.255 | 1 | 1 |
| /30 | 255.255.255.252 | 4 | 2 |
| /29 | 255.255.255.248 | 8 | 6 |
| /28 | 255.255.255.240 | 16 | 14 |
| /27 | 255.255.255.224 | 32 | 30 |
| /26 | 255.255.255.192 | 64 | 62 |
| /25 | 255.255.255.128 | 128 | 126 |
| /24 | 255.255.255.0 | 256 | 254 |
| /23 | 255.255.254.0 | 512 | 510 |
| /22 | 255.255.252.0 | 1,024 | 1,022 |
| /16 | 255.255.0.0 | 65,536 | 65,534 |
| /8 | 255.0.0.0 | 16,777,216 | 16,777,214 |
---

## لوڈ بیلنسنگ اور ریورس پراکسیز
### Nginx ریورس پراکسی کے طور پر
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

### لوڈ بیلنسنگ الگورتھم
- **راؤنڈ رابن**
- **کم سے کم رابطے**
- **IP ہیش** (سیشن چپچپا)
- **وزن والا راؤنڈ رابن**
### ٹولز
- **Nginx، HAProxy** (سافٹ ویئر)
- **AWS ELB، Azure Load Balancer، GCP کلاؤڈ لوڈ بیلنسنگ** (کلاؤڈ)
---

## ٹربل شوٹنگ چیک لسٹ
1. کیا جسمانی تعلق ہے؟ (کیبلز، وائی فائی کنکشن چیک کریں)۔
2. کیا آپ گیٹ وے کو پنگ لگا سکتے ہیں؟ (مثال کے طور پر،`ping 192.168.1.1`)
3. کیا آپ ایک بیرونی IP پنگ کر سکتے ہیں؟ (مثال کے طور پر،`8.8.8.8`)
4. کیا آپ ڈومین کو حل کر سکتے ہیں؟ (`dig google.com`)
5. کیا درخواست متوقع پورٹ پر سن رہی ہے؟ (`ss -tulpn | grep 8080`)
6. کیا فائر وال بندرگاہ کو روک رہا ہے؟ (`iptables` /`ufw`یا کلاؤڈ سیکیورٹی گروپس کو چیک کریں)۔
7. کیا ایپلیکیشن لاگز میں کوئی خامیاں ہیں؟
8. کیا TLS سرٹیفکیٹ درست اور قابل اعتماد ہے؟ (`openssl s_client -connect example.com:443`)۔