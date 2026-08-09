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

# 網路基礎知識
開發人員和系統管理員的實用參考 — 核心概念、協定、命令和故障排除。
---

## OSI 模型（7 層）
理解網路通訊的概念架構。
|層|名稱 |功能|協定範例|
|--------|------|----------|--------------------|
| 7 |應用 |最終用戶服務| HTTP、HTTPS、FTP、SMTP、DNS、SSH |
| 6 |示範|資料格式化、加密、壓縮| TLS、JPEG、ASCII |
| 5 |會議|連線管理 | NetBIOS、RPC |
| 4 |交通 |端對端交付、糾錯、流量控制 | TCP、UDP |
| 3 |網路|路由、尋址| IP、ICMP、OSPF、BGP |
| 2 |資料連結|成幀、錯誤偵測、MAC 位址 |乙太網路、Wi-Fi、PPP |
| 1 |身體|原始位元傳輸|乙太網路線、光纖、無線電波 |
在實務中，**TCP/IP 模型**（4 層：連結、網際網路、傳輸、應用程式）更常用於網際網路。
---

## IP 位址
### IPv4
- 32 位元位址，寫為四個八位元組：`192.168.1.1`
- 總數：約 43 億個位址（但在實踐中已耗盡）。
### IPv6
- 128位址，以十六進位書寫：`2001:0db8:85a3:0000:0000:8a2e:0370:7334`
- 總數：212⁸ 地址（幾乎無限）。
### 私有 IP 範圍 (RFC 1918)
這些無法在網際網路上路由；在本地網路內部使用：
-`10.0.0.0/8`(10.0.0.0 – 10.255.255.255)
-`172.16.0.0/12`(172.16.0.0 – 172.31.255.255)
-`192.168.0.0/16`(192.168.0.0 – 192.168.255.255)
### CIDR 表示法
 `192.168.1.0/24`表示前24位元是網路前綴；最後 8 位元是主機。它包括地址`192.168.1.0`到`192.168.1.255`。
---

## DNS（網域名稱系統）
將網域名稱（例如`example.com`）對應到 IP 位址。
### 記錄類型
|類型 |目的|
|------|---------|
| **一個** |將網域對應到 IPv4 位址 |
| **AAAA** |將網域對應到 IPv6 位址 |
| **別名** |另一個網域的別名 |
| **MX** |郵件交換伺服器|
| **TXT** |任意文字（SPF、DKIM、驗證）|
| **NS** |網域的名稱伺服器 |
| **SRV** |服務記錄（例如，SIP）|
### 常用工具```bash
dig example.com            # DNS lookup (detailed)
nslookup example.com       # DNS lookup (simpler)
host example.com           # Quick lookup
dig -x 8.8.8.8             # Reverse lookup (IP to name)
```

---

## 連接埠和協定
### 知名埠 (0–1023)
|港口|協定|服務 |
|------|----------|---------|
| 20、21 | TCP | FTP |
| 22 | 22 TCP | SSH |
| 23 | 23 TCP |遠端登入 |
| 25 | 25 TCP |郵件發送 |
| 53 | 53 UDP/TCP |網域解析 |
| 80| TCP | HTTP |
| 110 | 110 TCP | POP3 |
| 123 | 123 UDP | NTP |
| 143 | 143 TCP | IMAP |
| 443 | 443 TCP | HTTPS |
| 465 | 465 TCP | SMTPS |
| 587 | 587 TCP | SMTP（提交）|
| 993 | 993 TCP | IMAPS |
| 995 | 995 TCP | POP3S |
| 3306| TCP | MySQL |
| 5432 | TCP | PostgreSQL |
| 6379 | TCP | Redis |
| 27017 | 27017 TCP | MongoDB |
### 檢查開放端口
```bash
ss -tulpn                 # Linux: listen and established sockets
netstat -an               # Older tool
lsof -i :8080             # See process using port 8080
nmap localhost            # Scan local ports
```

---

## TCP 與 UDP
|特色 | TCP | UDP |
|---------|-----|-----|
|連接|面向連接（握手）|無連接|
|可靠性 |保證傳送、重送|盡力而為（可能會丟包）|
|訂購 |保留訂單 |無訂購保固 |
|流量控制|是（滑動視窗）|沒有 |
|使用案例 |網路 (HTTP)、電子郵件、SSH、檔案傳輸 | DNS、串流媒體、VoIP、遊戲、SNMP |
|標頭尺寸 | 20–60 位元組 | 8 位元組 |
---

## HTTP 和 HTTPS
### HTTP 方法
|方法|描述 |
|--------|-------------|
| **取得** |檢索資源（冪等、安全）|
| **發布** |提交資料（非冪等）|
| **放置** |更新/替換資源（冪等） |
| **補丁** |部分更新 |
| **刪除** |刪除資源（冪等）|
### 狀態程式碼
|程式碼|意義|
|------|---------|
| **1xx** |訊息（100 繼續）|
| **2xx** |成功（200 正常，201 已創建，204 無內容）|
| **3xx** |重定向（301 永久移動、302 找到、304 未修改）|
| **4xx** |客戶端錯誤（400 錯誤請求、401 未經授權、403 禁止、404 未找到、429 請求過多）|
| **5xx** |伺服器錯誤（500 內部伺服器錯誤、502 閘道錯誤、503 服務無法使用）|
### 標題
|標題 |目的|
|--------|---------|
|`Content-Type`|媒體類型（`application/json`、`text/html`）|
|`Authorization`|憑證（例如`Bearer <token>`）|
|`Cache-Control`|快取策略 |
| CORS 標頭 | `Access-Control-Allow-Origin`等|
---

## TLS/SSL
加密 HTTP 流量（HTTPS = HTTP over TLS）。
- 來自憑證授權單位 (CA) 的憑證對伺服器進行驗證。
- 驗證客戶端的憑證鏈和主機名稱。
---

## 防火牆和 NAT
### 防火牆
- 依照規則（來源 IP、目標 IP、連接埠、協定）過濾流量。
- 狀態防火牆追蹤連線狀態。
### NAT（網路位址轉換）
- 將私人 IP 轉換為公用 IP 以進行網際網路存取。
- 連接埠轉送：將公共連接埠對應到內部主機/連接埠。
---

## 常用聯網指令
### 連線測試
```bash
ping google.com            # ICMP echo request
ping -c 4 8.8.8.8          # ping 4 times
traceroute google.com      # Trace the route (Linux)
tracert google.com         # Windows version
```

### 路由
```bash
ip route show              # Linux: routing table
route -n                   # Older Linux
netstat -r                 # Windows/Mac
```

### 網路介面
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

### 與連接埠的連接
```bash
nc -zv google.com 443      # Netcat: check if port 443 is open
telnet google.com 443      # Telnet to port
curl -v https://google.com # Verbose output
```

### 防火牆（Linux iptables/nftables）
```bash
sudo ufw status            # Ubuntu: simple firewall
sudo iptables -L -n        # List rules
```

### 網路統計
```bash
ss -tulpn                  # Show listening sockets (Linux)
netstat -an                # All sockets (all OS)
```

---

## 子網劃分（快速參考）
| CIDR |網路遮罩|位址數量 |可用主機 |
|------|---------|---------------------|--------------|
| /32 | 255.255.255.255 | 255.255.255.255 1 | 1 |
| /30 | 255.255.255.252 | 255.255.255.252 4 | 2 |
| /29 | 255.255.255.248 | 255.255.255.248 8 | 6 |
| /28 | 255.255.255.240 | 255.255.255.240 16 | 16 14 | 14
| /27 | 255.255.255.224 | 255.255.255.224 32 | 32 30|
| /26 | 255.255.255.192 | 255.255.255.192 64 | 64 62 | 62
| /25 | 255.255.255.128 | 128 | 128 126 | 126
| /24 | 255.255.255.0 | 256 | 256 254 | 254
| /23 | 255.255.254.0 | 512 | 512 510 | 510
| /22 | 255.255.252.0 | 1,024 | 1,024 1,022 | 1,022
| /16 | 255.255.0.0 | 65,536 | 65,536 65,534 | 65,534
| /8 | 255.0.0.0 | 16,777,216 | 16,777,216 16,777,214 | 16,777,214
---

## 負載平衡和反向代理
### Nginx 作為反向代理
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

### 負載平衡演算法
- **循環賽**
- **最少連線**
- **IP 哈希**（會話黏性）
- **加權循環賽**
＃＃＃ 工具
- **Nginx、HAProxy**（軟體）
- **AWS ELB、Azure 負載平衡器、GCP 雲端負載平衡**（雲）
---

## 故障排除清單
1. 實體鏈路是否連通？ （檢查電纜、Wi-Fi 連線）。
2. 能否 ping 通網關？ （例如，`ping 192.168.1.1`）。
3. 可以ping通外部IP嗎？ （例如，`8.8.8.8`）。
4. 可以解析網域名稱嗎？ （`dig google.com`）。
5. 應用程式是否正在偵聽預期的連接埠？ （`ss -tulpn | grep 8080`）。
6. 防火牆是否阻塞了連接埠？ （檢查`iptables`/`ufw`或雲端安全群組）。
7. 應用程式日誌中是否有錯誤？
8. TLS 憑證是否有效且可信？ （`openssl s_client -connect example.com:443`）。