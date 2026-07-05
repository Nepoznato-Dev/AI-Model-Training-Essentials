# พื้นฐานระบบเครือข่าย

ข้อมูลอ้างอิงที่เป็นประโยชน์สำหรับนักพัฒนาและผู้ดูแลระบบ — แนวคิดหลัก โปรโตคอล คำสั่ง และการแก้ไขปัญหา

---

## โมเดล OSI (7 เลเยอร์)

กรอบแนวคิดสำหรับการทำความเข้าใจการสื่อสารผ่านเครือข่าย

| เลเยอร์ | ชื่อ | ฟังก์ชัน | ตัวอย่างโปรโตคอล |
|----------------------|-|---------|-------------------|
| 7 | ใบสมัคร | บริการสำหรับผู้ใช้ปลายทาง | HTTP, HTTPS, FTP, SMTP, DNS, SSH |
| 6 | การนำเสนอ | การจัดรูปแบบข้อมูล การเข้ารหัส การบีบอัด | TLS, JPEG, ASCII |
| 5 | เซสชั่น | การจัดการการเชื่อมต่อ | NetBIOS, RPC |
| 4 | ขนส่ง | การส่งมอบแบบครบวงจร การแก้ไขข้อผิดพลาด การควบคุมการไหล | TCP, UDP |
| 3 | เครือข่าย | การกำหนดเส้นทางการกำหนดแอดเดรส | IP, ICMP, OSPF, BGP |
| 2 | ลิงค์ข้อมูล | การวางกรอบ การตรวจจับข้อผิดพลาด ที่อยู่ MAC | อีเธอร์เน็ต, Wi-Fi, PPP |
| 1 | กายภาพ | การส่งบิตดิบ | สายอีเธอร์เน็ต ไฟเบอร์ออปติก คลื่นวิทยุ |

ในทางปฏิบัติ **โมเดล TCP/IP** (4 เลเยอร์: ลิงก์ อินเทอร์เน็ต การขนส่ง แอปพลิเคชัน) มักใช้กับอินเทอร์เน็ตมากกว่า

---

## ที่อยู่ IP

### IPv4
- ที่อยู่แบบ 32 บิต เขียนเป็นสี่ออคเต็ต: `192.168.1.1`
- ทั้งหมด: ~4.3 พันล้านที่อยู่ (แต่ในทางปฏิบัติหมดแล้ว)

### IPv6
- ที่อยู่ 128 บิต เขียนด้วยเลขฐานสิบหก: `2001:0db8:85a3:0000:0000:8a2e:0370:7334`
- ทั้งหมด: ที่อยู่2¹²⁸ (ในทางปฏิบัติไม่มีที่สิ้นสุด)

### ช่วง IP ส่วนตัว (RFC 1918)
สิ่งเหล่านี้ไม่สามารถกำหนดเส้นทางได้บนอินเทอร์เน็ต ใช้ภายในเครือข่ายท้องถิ่น:
- `10.0.0.0/8` (10.0.0.0 – 10.255.255.255)
- `172.16.0.0/12` (172.16.0.0 – 172.31.255.255)
- `192.168.0.0/16` (192.168.0.0 – 192.168.255.255)

### สัญกรณ์ CIDR
`192.168.1.0/24` หมายถึง 24 บิตแรกเป็นคำนำหน้าเครือข่าย 8 บิตสุดท้ายคือโฮสต์ ประกอบด้วยที่อยู่ `192.168.1.0` ถึง `192.168.1.255`

---

## DNS (ระบบชื่อโดเมน)

จับคู่ชื่อโดเมน (เช่น `example.com`) กับที่อยู่ IP

### ประเภทบันทึก
| พิมพ์ | วัตถุประสงค์ |
|------|---------|
| **เอ** | แมปโดเมนกับที่อยู่ IPv4 |
| **AAAA** | แมปโดเมนกับที่อยู่ IPv6 |
| **CNAME** | นามแฝงไปยังชื่อโดเมนอื่น |
| **เอ็มเอ็กซ์** | เซิร์ฟเวอร์แลกเปลี่ยนจดหมาย |
| **TXT** | ข้อความที่กำหนดเอง (SPF, DKIM, การยืนยัน) |
| **นส** | เนมเซิร์ฟเวอร์สำหรับโดเมน |
| **SRV** | บันทึกการบริการ (เช่น สำหรับ SIP) |

### เครื่องมือทั่วไป
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

```มาร์กดาวน์
# DevOps และการบริหารระบบ

คู่มือเชิงปฏิบัติในการจัดการเซิร์ฟเวอร์ การดำเนินการอัตโนมัติ และการบำรุงรักษาโครงสร้างพื้นฐานที่เชื่อถือได้

---

## SSH (เชลล์ปลอดภัย)

### การสร้างคีย์
``` ทุบตี
ssh-keygen -t ed25519 -C "your_email@example.com" # ทันสมัยและปลอดภัย
ssh-keygen -t rsa -b 4096 -C "your_email@example.com" # ทางเลือกสำรอง
คัดลอกรหัสสาธารณะไปยังเซิร์ฟเวอร์
ทุบตี
ssh-copy-id ผู้ใช้ @ โฮสต์
# ทางเลือกอื่นด้วยตนเอง:
แมว ~/.ssh/id_ed25519.pub | ผู้ใช้ ssh@host "mkdir -p ~/.ssh && cat >> ~/.ssh/authorized_keys"
การกำหนดค่า SSH (~/.ssh/config)
ssh-config.php
โฮสต์เซิร์ฟเวอร์ของฉัน
    ชื่อโฮสต์ 192.168.1.10
    ผู้ใช้อูบุนตู
    ไฟล์ประจำตัว ~/.ssh/mykey
    พอร์ต 2222
คำสั่ง SSH ทั่วไป
ทุบตี
ผู้ใช้ ssh@host # เชื่อมต่อ
ssh -J jumpuser@jumphost user@target # พร็อกซีกระโดด
scp file.txt user@host:/path/ # คัดลอกไฟล์ไปยังระยะไกล
scp user@host:/path/file.txt    #คัดลอกจากระยะไกล
rsync -avz -e ssh ./local/ user@host:/remote/ # การซิงค์ที่มีประสิทธิภาพ
การชุบแข็ง SSH
ปิดการใช้งานการเข้าสู่ระบบรูท: หมายเลข PermitRootLogin

ใช้การตรวจสอบสิทธิ์แบบใช้คีย์เท่านั้น: หมายเลขการตรวจสอบรหัสผ่าน

เปลี่ยนพอร์ตเริ่มต้น (เป็นทางเลือก การรักษาความปลอดภัยผ่านความสับสน)

เปิดใช้งาน AllowUsers หรือ AllowGroups เพื่อจำกัดการเข้าถึง

Systemd (การจัดการบริการ Linux)
คำสั่งทั่วไป
ทุบตี
systemctl status nginx # ตรวจสอบสถานะการบริการ
systemctl start nginx # เริ่มบริการ
systemctl หยุด nginx
systemctl รีสตาร์ท nginx
systemctl โหลด nginx # โหลดซ้ำอย่างสง่างาม (อ่านการกำหนดค่าอีกครั้ง)
systemctl เปิดใช้งาน nginx # เริ่มเมื่อบู๊ต
systemctl ปิดการใช้งาน nginx
systemctl list-units --type=service --all # แสดงรายการบริการทั้งหมด
systemctl daemon-reload # รีโหลดไฟล์หน่วยหลังจากแก้ไข
การสร้างหน่วยบริการ systemd
สร้าง /etc/systemd/system/myapp.service:

อินี่
[หน่วย]
Description=แอป Python ของฉัน
หลังจาก=network.target

[บริการ]
ผู้ใช้=myuser
กลุ่ม=กลุ่มของฉัน
WorkingDirectory=/opt/myapp
ExecStart=/usr/bin/python3 /opt/myapp/main.py
รีสตาร์ท = เสมอ
รีสตาร์ทวินาที=10
สิ่งแวดล้อม = "ENV = การผลิต"

[ติดตั้ง]
WantedBy=หลายผู้ใช้เป้าหมาย
จากนั้น:

ทุบตี
sudo systemctl daemon- โหลดซ้ำ
sudo systemctl เปิดใช้งาน myapp
sudo systemctl เริ่ม myapp
Journalctl (ดูบันทึก)
ทุบตี
Journalctl -u myapp # บันทึกสำหรับการบริการ
Journalctl -f # ติดตามบันทึก (ส่วนท้าย)
Journalctl --ตั้งแต่ "1 ชั่วโมงที่แล้ว"
Journalctl _PID=1234 # กรองตาม ID กระบวนการ
กลยุทธ์การบันทึก
การบันทึกแบบมีโครงสร้าง
ใช้รูปแบบ JSON เพื่อทำให้เครื่องบันทึกแยกวิเคราะห์ได้:

หลาม
นำเข้าโครงสร้างล็อก
คนตัดไม้ = structlog.get_logger()
logger.info("user_login", user_id=123, ip="192.168.1.1")
ระดับบันทึก
DEBUG: การวินิจฉัยโดยละเอียด

ข้อมูล: เหตุการณ์ทั่วไป (เริ่ม, หยุด, ธุรกรรมปกติ)

คำเตือน: ไม่คาดคิดแต่ไม่ร้ายแรง

ข้อผิดพลาด: ข้อผิดพลาดที่ขัดขวางการดำเนินการเฉพาะ

ร้ายแรง/สำคัญ: การปิดระบบ

การรวมบันทึก
ELK Stack (Elasticsearch, Logstash, Kibana) หรือ Elastic CloudLoki + Grafana (ทางเลือกที่มีน้ำหนักเบา)

Datadog, Splunk, ซูโมลอจิก (SaaS)

การหมุนบันทึก (logrotate)
ป้องกันบันทึกจากการเติมดิสก์ กำหนดค่า /etc/logrotate.d/myapp:

เข้าสู่ระบบ
/var/log/myapp/*.log {
    ทุกวัน
    หมุน 7
    บีบอัด
    ความล่าช้าในการบีบอัด
    หายไป
    การแจ้งเตือน
    สร้าง 0640 myuser mygroup
}
การติดตามและการแจ้งเตือน
ตัวชี้วัดที่ต้องตรวจสอบ
ระบบ: CPU, RAM, การใช้งานดิสก์, ค่าเฉลี่ยการโหลด, I/O เครือข่าย

แอปพลิเคชัน: อัตราคำขอ เวลาแฝง (p50, p95, p99) อัตราข้อผิดพลาด เซสชันที่ใช้งานอยู่

ฐานข้อมูล: จำนวนการสืบค้น การสืบค้นที่ช้า การใช้พูลการเชื่อมต่อ

ธุรกิจ: การสมัครสมาชิก อัตราการแปลง รายได้

เครื่องมือ
Prometheus + Grafana: สแต็กโอเพ่นซอร์สมาตรฐาน

ผู้ส่งออกโหนดสำหรับการวัดระบบ

Blackbox Exporter สำหรับความพร้อมใช้งานของปลายทาง

Alertmanager สำหรับการกำหนดเส้นทางการแจ้งเตือน

คลาวด์เนทีฟ: AWS CloudWatch, Azure Monitor, การตรวจสอบ GCP

การตรวจสอบสถานะการออนไลน์
Pingdom, หน้าสถานะ, Better Uptime, Uptime Kuma (โฮสต์เอง)

การตรวจสอบประสิทธิภาพการทำงาน: เปิดเผยจุดสิ้นสุด /health ที่ส่งคืน 200 หากบริการมีประสิทธิภาพดี

กลยุทธ์การสำรองข้อมูล
กฎ 3-2-1
สำเนาข้อมูล 3 ชุด

สื่อที่แตกต่างกัน 2 ประเภท (เช่น SSD + เทปหรือโลคัล + คลาวด์)

สำเนานอกสถานที่ 1 ชุด (เช่น คลาวด์หรือศูนย์ข้อมูลระยะไกล)

ประเภทการสำรองข้อมูล
การสำรองข้อมูลทั้งหมด: คัดลอกทุกอย่าง (ช้า พื้นที่มาก)

การสำรองข้อมูลส่วนเพิ่ม: คัดลอกเฉพาะการเปลี่ยนแปลงตั้งแต่ครั้งล่าสุดหรือแบบเพิ่มหน่วย (การคืนค่าที่รวดเร็วและซับซ้อน)

การสำรองข้อมูลส่วนต่าง: คัดลอกการเปลี่ยนแปลงตั้งแต่เต็มครั้งล่าสุด (ตรงกลาง)

การสำรองฐานข้อมูล
ทุบตี
#PostgreSQL
pg_dump dbname > สำรองข้อมูล sql
pg_dumpall > all_backup.sql

# MySQL / MariaDB
mysqldump -u root -p dbname > backup.sql

# คืนค่า
psql dbname < สำรอง. sql
mysql -u root -p dbname < backup.sql
การสำรองข้อมูลไฟล์
ทุบตี
# ไฟล์เก็บถาวร Tar
tar -czf backup.tar.gz /var/lib/data

# Rsync ไปยังระยะไกล
rsync -avz /local/data/ user@backup-server:/backup/data/

# Cloud CLI (เช่น AWS S3)
aws s3 ซิงค์ /local/data s3://my-bucket/backup/
กำหนดการสำรองข้อมูลอัตโนมัติ (cron)
ครอน
#วิ่งทุกวันเวลา 02.00 น
0 2 * * * /usr/local/bin/backup_script.sh
Cron และงานที่กำหนดเวลาไว้
ไวยากรณ์ของครอน
ข้อความ
* * * * * คำสั่ง
│ │ │ │ │
│ │ │ │ └─ วันในสัปดาห์ (0-7, 0=วันอาทิตย์)
│ │ │ └─── เดือน (1-12)
│ │ └───── วันของเดือน (1-31)
│ └─────── ชั่วโมง (0-23)
└───────── นาที (0-59)
ตัวอย่าง
ครอน
# ทุก 5 นาที
*/5 * * * * /path/to/script

# ทุกวัน เวลา 03:15 น
15 3 * * * /path/to/script

# ทุกวันจันทร์ เวลา 04.00 น
0 4 * * 1 /path/to/script

#ทุกชั่วโมง
0 * * * * /path/to/script
การจัดการครอน
ทุบตี
crontab -l # แสดงรายการงาน cron ของผู้ใช้ปัจจุบัน
crontab -e # แก้ไข
crontab -r # ลบทั้งหมด
อนาครอน
ใช้สำหรับระบบที่ไม่ได้ทำงานตลอด 24 ชั่วโมงทุกวัน (เช่น แล็ปท็อป) ช่วยให้มั่นใจว่างานต่างๆ จะดำเนินต่อไปในที่สุด

การจัดการแพ็คเกจและการอัพเดต
เดเบียน/อูบุนตู (เหมาะ)
ทุบตี
sudo apt update # อัปเดตรายการแพ็คเกจ
sudo apt upgrade # อัปเกรดแพ็คเกจทั้งหมด
sudo apt ติดตั้ง git nginx
sudo apt ลบคอมไพล์
sudo apt autoremove # ลบการอ้างอิงที่ไม่ได้ใช้
RHEL/CentOS/Fedora (dnf/ยำ)
ทุบตี
sudo dnf ตรวจสอบการอัปเดต
อัปเดต sudo dnf
sudo dnf ติดตั้ง git nginx
sudo dnf ลบคอมไพล์
การอัปเดตความปลอดภัย
เปิดใช้งานการอัปเกรดแบบอัตโนมัติบน Ubuntu สำหรับแพตช์ความปลอดภัย:

ทุบตี
sudo apt ติดตั้งการอัพเกรดแบบอัตโนมัติ
sudo dpkg-reconfigure - ไถการอัพเกรดแบบไม่ต้องดูแล
นักเทียบท่าในการผลิต
แนวทางปฏิบัติที่ดีที่สุด
ใช้แท็กรูปภาพเฉพาะ (python:3.12-slim) ไม่ใช่เวอร์ชันล่าสุด

รันคอนเทนเนอร์ในฐานะผู้ใช้ที่ไม่ใช่รูท

สแกนภาพเพื่อหาช่องโหว่ (docker scan, trivy)

ตั้งค่าขีดจำกัดทรัพยากร (--memory, --cpus)

ใช้ความลับ (ผ่านความลับของนักเทียบท่าหรือสภาพแวดล้อมด้วยความระมัดระวัง)

ทำให้รูปภาพมีขนาดเล็ก: การสร้างแบบหลายขั้นตอน ฐานอัลไพน์

นักเทียบท่าเขียนในการผลิต
ตั้งค่าขีดจำกัดทรัพยากรใน docker-compose.yml:

yaml
บริการ:
  แอพ:
    ภาพ: myapp:1.0
    ปรับใช้:
      ทรัพยากร:
        ขีดจำกัด:
          หน่วยความจำ: 512M
          ซีพียู: '0.5'
ข้อมูลเบื้องต้นเกี่ยวกับ CI/ซีดี
ขั้นตอนไปป์ไลน์
โครงสร้าง: คอมไพล์โค้ด ติดตั้งการอ้างอิง

ทดสอบ: เรียกใช้หน่วย บูรณาการ และการตรวจสอบผ้าสำลี

Containerise: สร้างอิมเมจ Docker

พุช: พุชอิมเมจไปที่คอนเทนเนอร์รีจิสตรี

ปรับใช้: อัปเดตสภาพแวดล้อมการจัดเตรียม/การใช้งานจริง

เครื่องมือ
การดำเนินการ GitHub: บูรณาการกับ GitHub

GitLab CI: สร้างขึ้นใน GitLab

Jenkins: แบบดั้งเดิม กำหนดค่าได้สูง

CircleCI, Travis CI: บุคคลที่สามยอดนิยม

ArgoCD: GitOps สำหรับ Kubernetesตัวอย่างการดำเนินการ GitHub (แบบง่าย):
yaml
ชื่อ: ซีไอ
บน: ดัน
งาน:
  สร้าง:
    วิ่งบน: ubuntu-ล่าสุด
    ขั้นตอน:
      - การใช้งาน: actions/checkout@v4
      - การใช้งาน: actions/setup-python@v5
        ด้วย:
          หลามเวอร์ชัน: '3.12'
      - รัน: pip install -r needs.txt
      - วิ่ง: pytest
การปรับแต่งระบบและการแก้ไขปัญหา
ตรวจสอบพื้นที่ดิสก์
ทุบตี
df -h # การใช้ดิสก์ที่มนุษย์สามารถอ่านได้
ดู่ -sh /* | sort -h # ขนาดของไดเรกทอรีระดับบนสุด
ตรวจสอบการใช้หน่วยความจำ
ทุบตี
ฟรี -m # หน่วยความจำเป็น MB
vmstat 1 10 # สถิติหน่วยความจำเสมือน
top -o %MEM # เรียงลำดับกระบวนการตามหน่วยความจำ
ตรวจสอบโหลด CPU
ทุบตี
สถานะการออนไลน์ # โหลดเฉลี่ยมากกว่า 1,5,15 นาที
top -o %CPU # เรียงลำดับกระบวนการตาม CPU
mpstat -P ทั้งหมด 1 5 # การใช้งาน CPU ต่อคอร์
ตรวจสอบเครือข่าย
ทุบตี
netstat -i # สถิติอินเทอร์เฟซ
iftop # การใช้แบนด์วิธสด (ต้องติดตั้ง)
nload # มอนิเตอร์แบนด์วิธอื่น
ค้นหาไฟล์ขนาดใหญ่
ทุบตี
ค้นหา / -พิมพ์ f -size +100M -exec ls -lh {} \; 2>/dev/null
โครงสร้างพื้นฐานเป็นรหัส (IaC)
เทอร์ราฟอร์ม
ประกาศทรัพยากรระบบคลาวด์ใน HCL

เอชซีแอล
ผู้ให้บริการ "aws" {
  ภูมิภาค = "us-east-1"
}
ทรัพยากร "aws_instance" "เว็บ" {
  อามิ = "ami-0c55b159cbfafe1f0"
  instance_type = "t2.ไมโคร"
}
เข้าใจได้
การจัดการการกำหนดค่าแบบไร้ตัวแทนโดยใช้ YAML

yaml
- ชื่อ: ติดตั้ง nginx
  โฮสต์: เว็บเซิร์ฟเวอร์
  งาน:
    - ชื่อ: ติดตั้ง nginx
      ฉลาด:
        ชื่อ: nginx
        รัฐ: ปัจจุบัน
แนวทางปฏิบัติที่ดีที่สุด
ใช้โมดูลและบทบาทเพื่อการนำกลับมาใช้ใหม่

จัดเก็บสถานะจากระยะไกล (S3, Terraform Cloud)

ใช้ตัวแปรและข้อมูลลับ (AWS_SECRET_ACCESS_KEY ผ่านสภาพแวดล้อม ไม่ใช่ฮาร์ดโค้ด)

เวอร์ชันควบคุมรหัส IaC ของคุณ

การตอบสนองต่อเหตุการณ์ (โทร)
รายการตรวจสอบสำหรับการหยุดให้บริการ
รับทราบการแจ้งเตือน

ประเมินขอบเขต: บริการ/ผู้ใช้ใดบ้างที่ได้รับผลกระทบ

ระบุปัญหา (ดูบันทึก ตัวชี้วัด การใช้งานล่าสุด)

มีถ้าเป็นไปได้ (เบรกเกอร์ แฟล็กคุณลักษณะ)

ย้อนกลับหรือแก้ไขไปข้างหน้า

สื่อสารสถานะไปยังผู้มีส่วนได้ส่วนเสียและผู้ใช้ (หน้าสถานะ)

บันทึกลำดับเวลาและการดำเนินการของเหตุการณ์

ภายหลังชันสูตร: ภายใน 24–48 ชั่วโมง ให้เขียนการวิเคราะห์สาเหตุที่แท้จริง (RCA) และรายการดำเนินการเพื่อป้องกันการเกิดซ้ำ