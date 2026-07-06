# Khái niệm cơ bản về mạng

Tài liệu tham khảo thực tế dành cho nhà phát triển và quản trị viên hệ thống — các khái niệm cốt lõi, giao thức, lệnh và cách khắc phục sự cố.

---

## Mô hình OSI (7 lớp)

Một khung khái niệm để hiểu giao tiếp mạng.

| Lớp | Tên | Chức năng | Giao thức ví dụ |
|-------|------|----------|-------------------|
| 7 | Ứng dụng | Dịch vụ người dùng cuối | HTTP, HTTPS, FTP, SMTP, DNS, SSH |
| 6 | Trình bày | Định dạng, mã hóa, nén dữ liệu | TLS, JPEG, ASCII |
| 5 | Phiên | Quản lý kết nối | NetBIOS, RPC |
| 4 | Vận tải | Phân phối từ đầu đến cuối, sửa lỗi, kiểm soát luồng | TCP, UDP |
| 3 | Mạng | Định tuyến, đánh địa chỉ | IP, ICMP, OSPF, BGP |
| 2 | Liên kết dữ liệu | Đóng khung, phát hiện lỗi, địa chỉ MAC | Ethernet, Wi-Fi, PPP |
| 1 | Vật lý | Truyền bit thô | Cáp Ethernet, cáp quang, sóng vô tuyến |

Trong thực tế, **Mô hình TCP/IP** (4 lớp: Liên kết, Internet, Truyền tải, Ứng dụng) được sử dụng phổ biến hơn cho internet.

---

## Địa chỉ IP

###IPv4
- Địa chỉ 32 bit, được viết dưới dạng bốn octet: `192.168.1.1`
- Tổng cộng: ~4,3 tỷ địa chỉ (nhưng đã cạn kiệt trên thực tế).

###IPv6
- Địa chỉ 128 bit, được viết bằng hex: `2001:0db8:85a3:0000:0000:8a2e:0370:7334`
- Tổng cộng: 2¹²⁸ địa chỉ (gần như vô hạn).

### Dãy IP riêng (RFC 1918)
Chúng không thể định tuyến được trên internet; được sử dụng bên trong các mạng cục bộ:
- `10.0.0.0/8` (10.0.0.0 – 10.255.255.255)
- `172.16.0.0/12` (172.16.0.0 – 172.31.255.255)
- `192.168.0.0/16` (192.168.0.0 – 192.168.255.255)

### Ký hiệu CIDR
`192.168.1.0/24` nghĩa là 24 bit đầu tiên là tiền tố mạng; 8 bit cuối cùng là máy chủ. Nó bao gồm các địa chỉ `192.168.1.0` đến `192.168.1.255`.

---

## DNS (Hệ thống tên miền)

Ánh xạ tên miền (ví dụ: `example.com`) tới địa chỉ IP.

### Loại bản ghi
| Loại | Mục đích |
|------|----------|
| **A** | Bản đồ miền tới địa chỉ IPv4 |
| **AAAA** | Ánh xạ miền tới địa chỉ IPv6 |
| **CNAME** | Bí danh cho tên miền khác |
| **MX** | Máy chủ trao đổi thư |
| **TXT** | Văn bản tùy ý (SPF, DKIM, xác minh) |
| **NS** | Máy chủ tên miền |
| **SRV** | Bản ghi dịch vụ (ví dụ: đối với SIP) |

### Công cụ phổ biến
giảm giá ```bash
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

```
# DevOps và Quản trị hệ thống

Hướng dẫn thực tế để quản lý máy chủ, tự động hóa hoạt động và duy trì cơ sở hạ tầng đáng tin cậy.

---

## SSH (Vỏ bảo mật)

### Tạo khóa
``` bash
ssh-keygen -t ed25519 -C "your_email@example.com" # Hiện đại và an toàn
ssh-keygen -t rsa -b 4096 -C "your_email@example.com" # Dự phòng
Sao chép khóa công khai vào máy chủ
đánh đập
ssh-copy-id người dùng@host
# Thay thế thủ công:
mèo ~/.ssh/id_ed25519.pub | ssh user@host "mkdir -p ~/.ssh && cat >> ~/.ssh/authorized_keys"
Cấu hình SSH (~/.ssh/config)
ssh-config
Lưu trữ máy chủ của tôi
    Tên máy chủ 192.168.1.10
    Người dùng Ubuntu
    IdentityFile ~/.ssh/mykey
    Cảng 2222
Các lệnh SSH phổ biến
đánh đập
người dùng ssh@host # Kết nối
ssh -J jumpuser@jumphost user@target # Nhảy proxy
scp file.txt user@host:/path/ # Sao chép tập tin vào remote
scp user@host:/path/file.txt .    # Sao chép từ xa
rsync -avz -e ssh ./local/ user@host:/remote/ # Đồng bộ hóa hiệu quả
Tăng cường SSH
Vô hiệu hóa đăng nhập root: PermitRootLogin no

Chỉ sử dụng xác thực dựa trên khóa: Mật khẩu xác thực không

Thay đổi cổng mặc định (tùy chọn, bảo mật thông qua che khuất).

Bật AllowUsers hoặc AllowGroups để hạn chế quyền truy cập.

Systemd (Quản lý dịch vụ Linux)
Các lệnh chung
đánh đập
trạng thái systemctl nginx # Kiểm tra trạng thái dịch vụ
systemctl start nginx # Bắt đầu dịch vụ
systemctl dừng nginx
systemctl khởi động lại nginx
systemctl tải lại nginx # Tải lại duyên dáng (đọc lại cấu hình)
systemctl kích hoạt nginx # Bắt đầu khi khởi động
systemctl vô hiệu hóa nginx
systemctl list-units --type=service --all # Liệt kê tất cả các dịch vụ
systemctl daemon-reload # Tải lại tập tin đơn vị sau khi chỉnh sửa
Tạo một đơn vị dịch vụ systemd
Tạo /etc/systemd/system/myapp.service:

đầu tiên
[Đơn vị]
Mô tả=Ứng dụng Python của tôi
Sau=network.target

[Dịch vụ]
Người dùng=người dùng của tôi
Nhóm=nhóm của tôi
WorkingDirectory=/opt/myapp
ExecStart=/usr/bin/python3 /opt/myapp/main.py
Khởi động lại=luôn luôn
Khởi động lại giây=10
Môi trường="ENV=sản xuất"

[Cài đặt]
WantedBy=multi-user.target
Sau đó:

đánh đập
sudo systemctl daemon-tải lại
sudo systemctl kích hoạt ứng dụng của tôi
sudo systemctl bắt đầu ứng dụng của tôi
Journalctl (Xem nhật ký)
đánh đập
tạp chí -u myapp # Nhật ký dịch vụ
tạp chí -f # Theo dõi (đuôi) nhật ký
tạp chí --kể từ "1 giờ trước"
tạp chí _PID=1234 # Lọc theo ID tiến trình
Chiến lược ghi nhật ký
Ghi nhật ký có cấu trúc
Sử dụng định dạng JSON để làm cho nhật ký có thể được phân tích cú pháp bằng máy:

trăn
nhập cấu trúc
logger = structlog.get_logger()
logger.info("user_login", user_id=123, ip="192.168.1.1")
Cấp độ nhật ký
DEBUG: chẩn đoán chi tiết.

THÔNG TIN: các sự kiện chung (bắt đầu, dừng, giao dịch bình thường).

CẢNH BÁO: bất ngờ nhưng không gây tử vong.

LỖI: lỗi ngăn cản một hoạt động cụ thể.

TUYỆT VỜI/TUYỆT VỜI: tắt hệ thống.

Tổng hợp nhật ký
ELK Stack (Elasticsearch, Logstash, Kibana) hoặc Đám mây đàn hồi.Loki + Grafana (thay thế nhẹ).

Datadog, Splunk, Sumo Logic (SaaS).

Xoay vòng nhật ký (logrotate)
Ngăn chặn nhật ký lấp đầy đĩa. Định cấu hình /etc/logrotate.d/myapp:

logrot
/var/log/myapp/*.log {
    hàng ngày
    xoay 7
    nén
    nén trễ
    thiếu sót
    sự thông báo
    tạo 0640 myuser mygroup
}
Giám sát và cảnh báo
Số liệu cần theo dõi
Hệ thống: CPU, RAM, mức sử dụng đĩa, mức tải trung bình, I/O mạng.

Ứng dụng: tỷ lệ yêu cầu, độ trễ (p50, p95, p99), tỷ lệ lỗi, phiên hoạt động.

Cơ sở dữ liệu: số lượng truy vấn, truy vấn chậm, sử dụng nhóm kết nối.

Kinh doanh: đăng ký người dùng, tỷ lệ chuyển đổi, doanh thu.

Công cụ
Prometheus + Grafana: Ngăn xếp mã nguồn mở tiêu chuẩn.

Trình xuất nút cho số liệu hệ thống.

Trình xuất hộp đen để cung cấp tính khả dụng của điểm cuối.

Alertmanager để định tuyến cảnh báo.

Bản địa đám mây: AWS CloudWatch, Azure Monitor, Giám sát GCP.

Giám sát thời gian hoạt động
Pingdom, Trang trạng thái, Thời gian hoạt động tốt hơn, Thời gian hoạt động Kuma (tự lưu trữ).

Kiểm tra tình trạng: hiển thị điểm cuối /health trả về 200 nếu dịch vụ tốt.

Chiến lược dự phòng
Quy tắc 3-2-1
3 bản sao dữ liệu.

2 loại phương tiện khác nhau (ví dụ: SSD + băng hoặc cục bộ + đám mây).

1 bản sao bên ngoài trang web (ví dụ: trung tâm dữ liệu đám mây hoặc từ xa).

Các loại dự phòng
Sao lưu toàn bộ: sao chép mọi thứ (chậm, nặng dung lượng).

Sao lưu gia tăng: chỉ sao chép các thay đổi kể từ lần cuối đầy đủ hoặc tăng dần (khôi phục nhanh, phức tạp).

Sao lưu khác biệt: sao chép các thay đổi kể từ bản đầy đủ gần đây nhất (trung bình).

Sao lưu cơ sở dữ liệu
đánh đập
#PostgreSQL
tên pg_dump db > backup.sql
pg_dumpall > all_backup.sql

#MySQL/MariaDB
mysqldump -u root -p dbname > backup.sql

# Khôi phục
tên db psql < backup.sql
mysql -u root -p dbname < backup.sql
Sao lưu tệp
đánh đập
# Lưu trữ tar
tar -czf backup.tar.gz /var/lib/data

# Rsync với điều khiển từ xa
rsync -avz /local/data/ user@backup-server:/backup/data/

# Đám mây CLI (ví dụ: AWS S3)
đồng bộ hóa aws s3 /local/data s3://my-bucket/backup/
Lập kế hoạch sao lưu tự động (cron)
cron
# Chạy vào lúc 2h sáng hàng ngày
0 2 * * * /usr/local/bin/backup_script.sh
Cron và công việc theo lịch trình
Cú pháp Cron
văn bản
lệnh * * * * *
│ │ │ │ │
│ │ │ │ └─ Ngày trong tuần (0-7, 0=Chủ Nhật)
│ │ │ └─── Tháng (1-12)
│ │ └───── Ngày trong tháng (1-31)
│ └─────── Giờ (0-23)
└───────── Phút (0-59)
Ví dụ
cron
# Cứ sau 5 phút
*/5 * * * * /path/to/script

# Hàng ngày vào lúc 3h15 sáng
15 3 * * * /path/to/script

# Thứ Hai hàng tuần lúc 4 giờ sáng
0 4 * * 1 /path/to/script

# Mỗi giờ
0 * * * * /path/to/script
Quản lý cron
đánh đập
crontab -l # Liệt kê cron jobs của người dùng hiện tại
crontab -e # Chỉnh sửa
crontab -r # Xóa tất cả
Anacron
Được sử dụng cho các hệ thống không chạy 24/7 (ví dụ: máy tính xách tay), đảm bảo công việc sẽ được thực hiện cuối cùng.

Quản lý và cập nhật gói
Debian/Ubuntu (apt)
đánh đập
sudo apt update # Cập nhật danh sách gói
nâng cấp sudo apt # Nâng cấp tất cả các gói
sudo apt cài đặt git nginx
sudo apt loại bỏ git
sudo apt autoremove # Xóa các phụ thuộc không sử dụng
RHEL/CentOS/Fedora (dnf/yum)
đánh đập
kiểm tra cập nhật sudo dnf
cập nhật sudo dnf
sudo dnf cài đặt git nginx
sudo dnf loại bỏ git
Cập nhật bảo mật
Kích hoạt tính năng nâng cấp không giám sát trên Ubuntu cho các bản vá bảo mật:

đánh đập
sudo apt cài đặt nâng cấp không giám sát
sudo dpkg-reconfigure -plow nâng cấp không giám sát
Docker trong sản xuất
Thực tiễn tốt nhất
Sử dụng thẻ hình ảnh cụ thể (python:3.12-slim) không mới nhất.

Chạy container với tư cách người dùng không phải root.

Quét hình ảnh để tìm lỗ hổng (quét docker, trivy).

Đặt giới hạn tài nguyên (--memory, --cpus).

Sử dụng bí mật (thông qua bí mật Docker hoặc môi trường một cách cẩn thận).

Giữ hình ảnh nhỏ: xây dựng nhiều giai đoạn, cơ sở trên núi cao.

Docker Compose trong sản xuất
Đặt giới hạn tài nguyên trong docker-compose.yml:

yaml
dịch vụ:
  ứng dụng:
    hình ảnh: myapp:1.0
    triển khai:
      tài nguyên:
        giới hạn:
          bộ nhớ: 512M
          bộ vi xử lý: '0,5'
Kiến thức cơ bản về CI/CD
Giai đoạn đường ống
Build: Biên dịch mã, cài đặt phụ thuộc.

Kiểm tra: Chạy kiểm tra đơn vị, tích hợp và tìm lỗi mã nguồn.

Containerise: Xây dựng hình ảnh Docker.

Đẩy: Đẩy hình ảnh vào sổ đăng ký vùng chứa.

Triển khai: Cập nhật môi trường dàn dựng/sản xuất.

Công cụ
Hành động GitHub: Được tích hợp với GitHub.

GitLab CI: Được tích hợp vào GitLab.

Jenkins: Truyền thống, cấu hình cao.

CircleCI, Travis CI: Bên thứ ba phổ biến.

ArgoCD: GitOps cho Kubernetes.Ví dụ về hành động GitHub (đơn giản):
yaml
tên: CI
trên: đẩy
công việc:
  xây dựng:
    đang chạy: ubuntu-mới nhất
    các bước:
      - sử dụng: hành động/checkout@v4
      - sử dụng: hành động/setup-python@v5
        với:
          phiên bản python: '3.12'
      - chạy: cài đặt pip -r require.txt
      - chạy: pytest
Tinh chỉnh và khắc phục sự cố hệ thống
Kiểm tra dung lượng ổ đĩa
đánh đập
df -h # Cách sử dụng đĩa mà con người có thể đọc được
du -sh /* | sắp xếp -h # Kích thước của thư mục cấp cao nhất
Kiểm tra việc sử dụng bộ nhớ
đánh đập
free -m # Bộ nhớ tính bằng MB
vmstat 1 10 # Thống kê bộ nhớ ảo
top -o %MEM # Sắp xếp các tiến trình theo bộ nhớ
Kiểm tra tải CPU
đánh đập
thời gian hoạt động # Tải trung bình trên 1,5,15 phút
top -o %CPU # Sắp xếp các tiến trình theo CPU
mpstat -P ALL 1 5 # Sử dụng CPU trên mỗi lõi
Kiểm tra mạng
đánh đập
netstat -i # Thống kê giao diện
iftop # Sử dụng băng thông trực tiếp (yêu cầu cài đặt)
nload # Một trình giám sát băng thông khác
Tìm tệp lớn
đánh đập
tìm / -type f -size +100M -exec ls -lh {} \; 2>/dev/null
Cơ sở hạ tầng dưới dạng mã (IaC)
địa hình
Khai báo tài nguyên đám mây trong HCL.

hcl
nhà cung cấp "ôi" {
  vùng = "us-đông-1"
}
tài nguyên "aws_instance" "web" {
  ami = "ami-0c55b159cbfafe1f0"
  instance_type = "t2.micro"
}
Ansible
Quản lý cấu hình không cần tác nhân bằng YAML.

yaml
- tên: Cài đặt nginx
  máy chủ: máy chủ web
  nhiệm vụ:
    - tên: Cài đặt nginx
      thích hợp:
        Tên: nginx
        trạng thái: hiện tại
Thực tiễn tốt nhất
Sử dụng các mô-đun và vai trò để có thể sử dụng lại.

Lưu trữ trạng thái từ xa (S3, Terraform Cloud).

Sử dụng các biến và bí mật (AWS_SECRET_ACCESS_KEY thông qua môi trường, không được mã hóa cứng).

Phiên bản kiểm soát mã IaC của bạn.

Ứng phó sự cố (Theo yêu cầu)
Danh sách kiểm tra khi ngừng dịch vụ
Xác nhận cảnh báo.

Đánh giá phạm vi: Dịch vụ/người dùng nào bị ảnh hưởng?

Xác định vấn đề (xem nhật ký, số liệu, hoạt động triển khai gần đây).

Chứa nếu có thể (bộ ngắt mạch, cờ tính năng).

Quay lại hoặc sửa về phía trước.

Truyền đạt trạng thái cho các bên liên quan và người dùng (trang trạng thái).

Ghi lại dòng thời gian và hành động của sự cố.

Khám nghiệm tử thi: trong vòng 24–48 giờ, viết bản phân tích nguyên nhân gốc rễ (RCA) và các mục hành động để ngăn ngừa tái diễn.