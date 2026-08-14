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
# Kiến thức cơ bản về mạng
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
Trong thực tế, **Mô hình TCP/IP** (4 lớp: Liên kết, Internet, Truyền tải, Ứng dụng) được sử dụng phổ biến hơn cho Internet.
---

## Địa chỉ IP
###IPv4
- Địa chỉ 32 bit, được viết dưới dạng 4 octet:`192.168.1.1`
- Tổng cộng: ~4,3 tỷ địa chỉ (nhưng đã cạn kiệt trên thực tế).
###IPv6
- Địa chỉ 128 bit, được viết bằng hex:`2001:0db8:85a3:0000:0000:8a2e:0370:7334`
- Tổng cộng: 2¹²⁸ địa chỉ (gần như vô hạn).
### Dãy IP riêng (RFC 1918)
Chúng không thể định tuyến được trên internet; được sử dụng bên trong các mạng cục bộ:
- __BẢO VỆ_0__ (10.0.0.0 – 10.255.255.255)
- __BẢO VỆ_1__ (172.16.0.0 – 172.31.255.255)
- __BẢO VỆ_2__ (192.168.0.0 – 192.168.255.255)
### Ký hiệu CIDR
`192.168.1.0/24`nghĩa là 24 bit đầu tiên là tiền tố mạng; 8 bit cuối cùng là máy chủ. Nó bao gồm các địa chỉ`192.168.1.0`đến`192.168.1.255`.
---

## DNS (Hệ thống tên miền)
Ánh xạ tên miền (ví dụ:`example.com`) thành địa chỉ IP.
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
### Công cụ phổ biến```bash
dig example.com            # DNS lookup (detailed)
nslookup example.com       # DNS lookup (simpler)
host example.com           # Quick lookup
dig -x 8.8.8.8             # Reverse lookup (IP to name)
```

---

## Cổng và giao thức
### Cổng nổi tiếng (0–1023)
| Cảng | Giao thức | Dịch vụ |
|------|----------|----------|
| 20, 21 | TCP | FTP |
| 22 | TCP | SSH |
| 23 | TCP | Telnet |
| 25 | TCP | SMTP |
| 53 | UDP/TCP | DNS |
| 80 | TCP | HTTP |
| 110 | TCP | POP3 |
| 123 | UDP | NTP |
| 143 | TCP | IMAP |
| 443 | TCP | HTTPS |
| 465 | TCP | SMTPS |
| 587 | TCP | SMTP (gửi) |
| 993 | TCP | HÌNH ẢNH |
| 995 | TCP | POP3S |
| 3306 | TCP | MySQL |
| 5432 | TCP | PostgreSQL |
| 6379 | TCP | Làm lại |
| 27017 | TCP | MongoDB |
### Kiểm tra các cổng đang mở
```bash
ss -tulpn                 # Linux: listen and established sockets
netstat -an               # Older tool
lsof -i :8080             # See process using port 8080
nmap localhost            # Scan local ports
```

---

## TCP và UDP
| Tính năng | TCP | UDP |
|----------|------|------|
| Kết nối | Hướng kết nối (bắt tay) | Không kết nối |
| Độ tin cậy | Đảm bảo giao hàng, truyền lại | Nỗ lực hết mình (có thể làm rơi gói tin) |
| Đặt hàng | Giữ gìn trật tự | Không đảm bảo đặt hàng |
| Kiểm soát dòng chảy | Có (cửa sổ trượt) | Không |
| Trường hợp sử dụng | Web (HTTP), email, SSH, truyền tệp | DNS, phát trực tuyến, VoIP, chơi game, SNMP |
| Kích thước tiêu đề | 20–60 byte | 8 byte |
---

## HTTP và HTTPS
### Phương thức HTTP
| Phương pháp | Mô tả |
|--------|-------------|
| ** NHẬN ** | Truy xuất tài nguyên (bình thường, an toàn) |
| **BÀI ĐĂNG** | Gửi dữ liệu (không bình thường) |
| **ĐƯA** | Cập nhật/thay thế tài nguyên (idempotent) |
| ** VÁ ** | Cập nhật một phần |
| **XÓA** | Xóa tài nguyên (idempotent) |
### Mã trạng thái
| Mã | Ý nghĩa |
|------|----------|
| **1xx** | Thông tin (100 Tiếp tục) |
| **2xx** | Thành công (200 OK, 201 Đã tạo, 204 Không có nội dung) |
| **3xx** | Chuyển hướng (301 Đã di chuyển vĩnh viễn, 302 được tìm thấy, 304 không được sửa đổi) |
| **4xx** | Lỗi máy khách (400 Yêu cầu không hợp lệ, 401 trái phép, 403 Bị cấm, 404 Không tìm thấy, 429 Quá nhiều yêu cầu) |
| **5xx** | Lỗi máy chủ (Lỗi máy chủ nội bộ 500, Cổng xấu 502, Dịch vụ 503 không khả dụng) |
### Tiêu đề
| Tiêu đề | Mục đích |
|--------|----------|
|  __BẢO VỆ_0__ | Loại phương tiện ( `application/json`, `text/html`) |
|  __BẢO VỆ_3__ | Thông tin xác thực (ví dụ:`Bearer <token>`) |
|  __BẢO VỆ_5__ | Chính sách bộ nhớ đệm |
| Tiêu đề CORS | `Access-Control-Allow-Origin`, v.v. |
---

##TLS/SSL
Mã hóa lưu lượng HTTP (HTTPS = HTTP qua TLS).
- Chứng chỉ từ Cơ quan cấp chứng chỉ (CA) xác thực máy chủ.
- Xác minh chuỗi chứng chỉ và tên máy chủ ở phía máy khách.
---

## Tường lửa và NAT
### Tường lửa
- Lọc lưu lượng truy cập dựa trên các quy tắc (IP nguồn, IP đích, cổng, giao thức).
- Tường lửa trạng thái theo dõi trạng thái kết nối.
### NAT (Dịch địa chỉ mạng)
- Dịch IP riêng sang IP công cộng để truy cập internet.
- Chuyển tiếp cổng: ánh xạ một cổng công cộng tới một máy chủ/cổng nội bộ.
---

## Các lệnh mạng thông dụng
### Kiểm tra kết nối
```bash
ping google.com            # ICMP echo request
ping -c 4 8.8.8.8          # ping 4 times
traceroute google.com      # Trace the route (Linux)
tracert google.com         # Windows version
```

### Lộ trình
```bash
ip route show              # Linux: routing table
route -n                   # Older Linux
netstat -r                 # Windows/Mac
```

### Giao diện mạng
```bash
ip addr show               # List interfaces and IPs
ifconfig                   # Older command
```

###DNS
```bash
dig example.com
nslookup example.com
host example.com
```

### Kết nối với cổng
```bash
nc -zv google.com 443      # Netcat: check if port 443 is open
telnet google.com 443      # Telnet to port
curl -v https://google.com # Verbose output
```

### Tường lửa (Linux iptables/nftables)
```bash
sudo ufw status            # Ubuntu: simple firewall
sudo iptables -L -n        # List rules
```

### Thống kê mạng
```bash
ss -tulpn                  # Show listening sockets (Linux)
netstat -an                # All sockets (all OS)
```

---

## Mạng con (Tham khảo nhanh)
| CIDR | Mặt nạ mạng | Số lượng địa chỉ | Máy chủ có thể sử dụng |
|------|----------|----------------------|--------------|
| /32 | 255.255.255.255 | 1 | 1 |
| /30 | 255.255.255.252 | 4 | 2 |
| /29 | 255.255.255.248 | 8 | 6 |
| /28 | 255.255.255.240 | 16 | 14 |
| /27 | 255.255.255.224 | 32 | 30 |
| /26 | 255.255.255.192 | 64 | 62 |
| /25 | 255.255.255.128 | 128 | 126 |
| /24 | 255.255.255.0 | 256 | 254 |
| /23 | 255.255.254.0 | 512 | 510 |
| /22 | 255.255.252.0 | 1.024 | 1.022 |
| /16 | 255.255.0.0 | 65.536 | 65.534 |
| /8 | 255.0.0.0 | 16.777.216 | 16.777.214 |
---

## Cân bằng tải và proxy ngược
### Nginx làm Proxy ngược
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

### Thuật toán cân bằng tải
- **Vòng tròn**
- **Ít kết nối nhất**
- **IP hash** (độ dính của phiên)
- **Vòng tròn có trọng số**
### Công cụ
- **Nginx, HAProxy** (phần mềm)
- **AWS ELB, Azure Load Balancer, Cân bằng tải đám mây GCP** (đám mây)
---

## Danh sách kiểm tra khắc phục sự cố
1. Liên kết vật lý có tốt không? (Kiểm tra cáp, kết nối Wi-Fi).
2. Bạn có thể ping cổng không? (ví dụ:`ping 192.168.1.1`).
3. Bạn có thể ping IP bên ngoài không? (ví dụ:`8.8.8.8`).
4. Bạn có thể giải quyết một tên miền không? ( __BẢO VỆ_2__ ).
5. Ứng dụng có đang nghe trên cổng dự kiến ​​không? ( __BẢO VỆ_3__ ).
6. Tường lửa có chặn cổng không? (Kiểm tra`iptables`/`ufw`hoặc nhóm bảo mật đám mây).
7. Có lỗi nào trong nhật ký ứng dụng không?
8. Chứng chỉ TLS có hợp lệ và đáng tin cậy không? ( __BẢO VỆ_6__ ).