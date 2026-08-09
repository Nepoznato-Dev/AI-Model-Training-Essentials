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
# 网络基础知识
开发人员和系统管理员的实用参考 — 核心概念、协议、命令和故障排除。
---

## OSI 模型（7 层）
理解网络通信的概念框架。
|层|名称 |功能|协议示例|
|--------|------|----------|--------------------|
| 7 |应用 |最终用户服务| HTTP、HTTPS、FTP、SMTP、DNS、SSH |
| 6 |演示|数据格式化、加密、压缩| TLS、JPEG、ASCII |
| 5 |会议|连接管理 | NetBIOS、RPC |
| 4 |交通 |端到端交付、纠错、流量控制 | TCP、UDP |
| 3 |网络|路由、寻址| IP、ICMP、OSPF、BGP |
| 2 |数据链接|成帧、错误检测、MAC 地址 |以太网、Wi-Fi、PPP |
| 1 |身体|原始比特传输|以太网电缆、光纤、无线电波 |
在实践中，**TCP/IP 模型**（4 层：链路、互联网、传输、应用程序）更常用于互联网。
---

## IP 寻址
### IPv4
- 32 位地址，写为四个八位字节：`192.168.1.1` 
- 总数：约 43 亿个地址（但在实践中已耗尽）。
### IPv6
- 128 位地址，以十六进制编写：`2001:0db8:85a3:0000:0000:8a2e:0370:7334` 
- 总数：212⁸ 地址（几乎无限）。
### 私有 IP 范围 (RFC 1918)
这些无法在互联网上路由；在本地网络内部使用：
-`10.0.0.0/8`(10.0.0.0 – 10.255.255.255)
-`172.16.0.0/12`(172.16.0.0 – 172.31.255.255)
- __受保护_2__ (192.168.0.0 – 192.168.255.255)
### CIDR 表示法
`192.168.1.0/24`表示前24位是网络前缀；最后 8 位是主机。它包括地址`192.168.1.0`到`192.168.1.255`。
---

## DNS（域名系统）
将域名（例如`example.com`）映射到 IP 地址。
### 记录类型
|类型 |目的|
|------|---------|
| **一个** |将域映射到 IPv4 地址 |
| **AAAA** |将域映射到 IPv6 地址 |
| **别名** |另一个域名的别名 |
| **MX** |邮件交换服务器|
| **TXT** |任意文本（SPF、DKIM、验证）|
| **NS** |域的名称服务器 |
| **SRV** |服务记录（例如，SIP）|
### 常用工具```bash
dig example.com            # DNS lookup (detailed)
nslookup example.com       # DNS lookup (simpler)
host example.com           # Quick lookup
dig -x 8.8.8.8             # Reverse lookup (IP to name)
```

---

## 端口和协议
### 知名端口 (0–1023)
|港口|协议|服务 |
|------|----------|---------|
| 20、21 | TCP | FTP |
| 22 | 22 TCP | SSH |
| 23 | 23 TCP |远程登录 |
| 25 | 25 TCP |邮件发送 |
| 53 | 53 UDP/TCP |域名解析 |
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
### 检查开放端口
```bash
ss -tulpn                 # Linux: listen and established sockets
netstat -an               # Older tool
lsof -i :8080             # See process using port 8080
nmap localhost            # Scan local ports
```

---

## TCP 与 UDP
|特色 | TCP | UDP |
|---------|-----|-----|
|连接|面向连接（握手）|无连接|
|可靠性 |保证传送、重传|尽力而为（可能会丢包）|
|订购 |保留订单 |无订购保证 |
|流量控制|是（滑动窗口）|没有 |
|使用案例 |网络 (HTTP)、电子邮件、SSH、文件传输 | DNS、流媒体、VoIP、游戏、SNMP |
|标头尺寸 | 20–60 字节 | 8 字节 |
---

## HTTP 和 HTTPS
### HTTP 方法
|方法|描述 |
|--------|-------------|
| **获取** |检索资源（幂等、安全）|
| **发布** |提交数据（非幂等）|
| **放置** |更新/替换资源（幂等） |
| **补丁** |部分更新 |
| **删除** |删除资源（幂等）|
### 状态代码
|代码|意义|
|------|---------|
| **1xx** |信息（100 继续）|
| **2xx** |成功（200 正常，201 已创建，204 无内容）|
| **3xx** |重定向（301 永久移动、302 找到、304 未修改）|
| **4xx** |客户端错误（400 错误请求、401 未经授权、403 禁止、404 未找到、429 请求过多）|
| **5xx** |服务器错误（500 内部服务器错误、502 网关错误、503 服务不可用）|
### 标题
|标题 |目的|
|--------|---------|
|  __受保护_0__ |媒体类型（`application/json`、`text/html`）|
|  __受保护_3__ |凭证（例如`Bearer <token>`）|
|  __受保护_5__ |缓存策略 |
| CORS 标头 | `Access-Control-Allow-Origin`等 |
---

## TLS/SSL
加密 HTTP 流量（HTTPS = HTTP over TLS）。
- 来自证书颁发机构 (CA) 的证书对服务器进行身份验证。
- 验证客户端的证书链和主机名。
---

## 防火墙和 NAT
### 防火墙
- 根据规则（源 IP、目标 IP、端口、协议）过滤流量。
- 状态防火墙跟踪连接状态。
### NAT（网络地址转换）
- 将私有 IP 转换为公共 IP 以进行互联网访问。
- 端口转发：将公共端口映射到内部主机/端口。
---

## 常用联网命令
### 连接测试
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

### 网络接口
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

### 与端口的连接
```bash
nc -zv google.com 443      # Netcat: check if port 443 is open
telnet google.com 443      # Telnet to port
curl -v https://google.com # Verbose output
```

### 防火墙（Linux iptables/nftables）
```bash
sudo ufw status            # Ubuntu: simple firewall
sudo iptables -L -n        # List rules
```

### 网络统计
```bash
ss -tulpn                  # Show listening sockets (Linux)
netstat -an                # All sockets (all OS)
```

---

## 子网划分（快速参考）
| CIDR |网络掩码|地址数量 |可用主机 |
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

## 负载均衡和反向代理
### Nginx 作为反向代理
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

### 负载均衡算法
- **循环赛**
- **最少连接**
- **IP 哈希**（会话粘性）
- **加权循环赛**
＃＃＃ 工具
- **Nginx、HAProxy**（软件）
- **AWS ELB、Azure 负载均衡器、GCP 云负载均衡**（云）
---

## 故障排除清单
1. 物理链路是否连通？ （检查电缆、Wi-Fi 连接）。
2. 能否 ping 通网关？ （例如，`ping 192.168.1.1`）。
3. 可以ping通外部IP吗？ （例如，`8.8.8.8`）。
4. 可以解析域名吗？ (`dig google.com`)。
5. 应用程序是否正在侦听预期的端口？ （`ss -tulpn | grep 8080`）。
6. 防火墙是否阻塞了端口？ （检查`iptables`/`ufw`或云安全组）。
7. 应用程序日志中是否有错误？
8. TLS 证书是否有效且可信？ （`openssl s_client -connect example.com:443`）。