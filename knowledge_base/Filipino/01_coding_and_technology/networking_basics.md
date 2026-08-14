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

# Mga Pangunahing Kaalaman sa Networking
Isang praktikal na sanggunian para sa mga developer at sysadmin — mga pangunahing konsepto, protocol, command, at pag-troubleshoot.
---

## Ang OSI Model (7 Layers)
Isang konseptwal na balangkas para sa pag-unawa sa komunikasyon sa network.
| Layer | Pangalan | Function | Mga halimbawang protocol |
|-------|------|----------|-------------------|
| 7 | Application | Mga serbisyo ng end-user | HTTP, HTTPS, FTP, SMTP, DNS, SSH |
| 6 | Pagtatanghal | Pag-format ng data, pag-encrypt, pag-compress | TLS, JPEG, ASCII |
| 5 | Sesyon | Pamamahala ng koneksyon | NetBIOS, RPC |
| 4 | Transportasyon | End-to-end na paghahatid, pagwawasto ng error, kontrol sa daloy | TCP, UDP |
| 3 | Network | Pagruruta, pag-address | IP, ICMP, OSPF, BGP |
| 2 | Link ng Data | Pag-frame, pagtuklas ng error, mga MAC address | Ethernet, Wi-Fi, PPP |
| 1 | Pisikal | Raw bit transmission | Mga Ethernet cable, fiber optics, radio waves |
Sa pagsasagawa, **modelo ng TCP/IP** (4 na layer: Link, Internet, Transport, Application) ay mas karaniwang ginagamit para sa internet.
---

## IP Addressing
### IPv4
- 32-bit na address, nakasulat bilang apat na octet:`192.168.1.1`
- Kabuuan: ~4.3 bilyong address (ngunit naubos sa pagsasanay).
### IPv6
- 128-bit na address, nakasulat sa hex:`2001:0db8:85a3:0000:0000:8a2e:0370:7334`
- Kabuuan: 2¹²⁸ address (halos walang katapusan).
### Mga Pribadong IP Range (RFC 1918)
Ang mga ito ay hindi routable sa internet; ginagamit sa loob ng mga lokal na network:
-`10.0.0.0/8`(10.0.0.0 – 10.255.255.255)
-`172.16.0.0/12`(172.16.0.0 – 172.31.255.255)
-`192.168.0.0/16`(192.168.0.0 – 192.168.255.255)
### CIDR Notation
 Ang ibig sabihin ng`192.168.1.0/24`ay ang unang 24 bits ay ang network prefix; ang huling 8 bit ay mga host. Kabilang dito ang mga address`192.168.1.0`hanggang`192.168.1.255`.
---

## DNS (Domain Name System)
Mga mapa ng domain name (hal.,`example.com`) sa mga IP address.
### Mga Uri ng Record
| Uri | Layunin |
|------|---------|
| **A** | Maps domain sa IPv4 address |
| **AAAA** | Maps domain sa IPv6 address |
| **CNAME** | Alias ​​sa ibang domain name |
| **MX** | Mail exchange server |
| **TXT** | Arbitrary text (SPF, DKIM, verification) |
| **NS** | Nameserver para sa domain |
| **SRV** | Tala ng serbisyo (hal., para sa SIP) |
### Mga Karaniwang Tool```bash
dig example.com            # DNS lookup (detailed)
nslookup example.com       # DNS lookup (simpler)
host example.com           # Quick lookup
dig -x 8.8.8.8             # Reverse lookup (IP to name)
```

---

## Mga Port at Protocol
### Mga Kilalang Port (0–1023)
| Port | Protocol | Serbisyo |
|------|----------|---------|
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
| 587 | TCP | SMTP (pagsumite) |
| 993 | TCP | IMAPS |
| 995 | TCP | POP3S |
| 3306 | TCP | MySQL |
| 5432 | TCP | PostgreSQL |
| 6379 | TCP | Redis |
| 27017 | TCP | MongoDB |
### Suriin ang Mga Bukas na Port
```bash
ss -tulpn                 # Linux: listen and established sockets
netstat -an               # Older tool
lsof -i :8080             # See process using port 8080
nmap localhost            # Scan local ports
```

---

## TCP vs UDP
| Tampok | TCP | UDP |
|---------|-----|-----|
| Koneksyon | Nakatuon sa koneksyon (pagkakamay) | Walang koneksyon |
| Pagiging maaasahan | Garantisadong paghahatid, muling pagpapadala | Pinakamahusay na pagsisikap (maaaring mag-drop ng mga packet) |
| Pag-order | Pinapanatili ang order | Walang garantiya sa pag-order |
| Kontrol ng daloy | Oo (sliding window) | Hindi |
| Mga kaso ng paggamit | Web (HTTP), email, SSH, paglilipat ng file | DNS, streaming, VoIP, gaming, SNMP |
| Laki ng header | 20–60 byte | 8 byte |
---

## HTTP at HTTPS
### Mga Paraan ng HTTP
| Paraan | Paglalarawan |
|--------|--------------|
| **KUMUHA** | Kumuha ng mapagkukunan (idempotent, ligtas) |
| **POST** | Magsumite ng data (hindi idempotent) |
| **PUT** | I-update/palitan ang isang mapagkukunan (idempotent) |
| **PATCH** | Bahagyang pag-update |
| **TANGGAL** | Mag-alis ng mapagkukunan (idempotent) |
### Mga Code ng Katayuan
| Code | Ibig sabihin |
|------|---------|
| **1xx** | Impormasyon (100 Magpatuloy) |
| **2xx** | Tagumpay (200 OK, 201 Ginawa, 204 Walang Nilalaman) |
| **3xx** | Pag-redirect (301 Permanenteng Inilipat, 302 Nahanap, 304 Hindi Binago) |
| **4xx** | Error ng kliyente (400 Masamang Kahilingan, 401 Hindi Pinahintulutan, 403 Ipinagbabawal, 404 Hindi Nahanap, 429 Napakaraming Kahilingan) |
| **5xx** | Error sa server (500 Internal Server Error, 502 Bad Gateway, 503 Service Unavailable) |
### Mga Header
| Header | Layunin |
|--------|---------|
| `Content-Type`| Uri ng media (`application/json`,`text/html`) |
| `Authorization`| Mga kredensyal (hal.,`Bearer <token>`) |
| `Cache-Control`| Patakaran sa pag-cache |
| Mga header ng CORS | `Access-Control-Allow-Origin`, atbp. |
---

## TLS/SSL
Ini-encrypt ang trapiko ng HTTP (HTTPS = HTTP sa TLS).
- Ang mga sertipiko mula sa Mga Awtoridad ng Sertipiko (CAs) ay nagpapatunay sa server.
- I-verify ang chain ng certificate at hostname sa panig ng kliyente.
---

## Mga Firewall at NAT
### Firewall
- Sinasala ang trapiko batay sa mga panuntunan (pinagmulan ng IP, dest IP, port, protocol).
- Ang mga stateful na firewall ay sumusubaybay sa mga estado ng koneksyon.
### NAT (Pagsasalin ng Address ng Network)
- Nagsasalin ng mga pribadong IP sa isang pampublikong IP para sa internet access.
- Port forwarding: nagmamapa ng pampublikong port sa isang panloob na host/port.
---

## Mga Karaniwang Utos sa Networking
### Mga Pagsusuri sa Pagkakakonekta
```bash
ping google.com            # ICMP echo request
ping -c 4 8.8.8.8          # ping 4 times
traceroute google.com      # Trace the route (Linux)
tracert google.com         # Windows version
```

### Pagruruta
```bash
ip route show              # Linux: routing table
route -n                   # Older Linux
netstat -r                 # Windows/Mac
```

### Mga Interface ng Network
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

### Pagkakakonekta sa isang Port
```bash
nc -zv google.com 443      # Netcat: check if port 443 is open
telnet google.com 443      # Telnet to port
curl -v https://google.com # Verbose output
```

### Firewall (Linux iptables/nftables)
```bash
sudo ufw status            # Ubuntu: simple firewall
sudo iptables -L -n        # List rules
```

### Mga Istatistika ng Network
```bash
ss -tulpn                  # Show listening sockets (Linux)
netstat -an                # All sockets (all OS)
```

---

## Subnetting (Mabilis na Sanggunian)
| CIDR | Netmask | Bilang ng mga address | Mga magagamit na host |
|------|--------|---------------------|--------------|
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

## Load Balancing at Reverse Proxies
### Nginx bilang Reverse Proxy
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

### Load Balancing Algorithms
- **Round-robin**
- **Hindi bababa sa mga koneksyon**
- **IP hash** (kadikit ng session)
- **Tinimbang na round-robin**
### Mga tool
- **Nginx, HAProxy** (software)
- **AWS ELB, Azure Load Balancer, GCP Cloud Load Balancing** (cloud)
---

## Checklist sa Pag-troubleshoot
1. Nakataas ba ang pisikal na link? (Suriin ang mga cable, koneksyon sa Wi-Fi).
2. Maaari mo bang i-ping ang gateway? (hal.,`ping 192.168.1.1`).
3. Maaari ka bang mag-ping ng isang panlabas na IP? (hal.,`8.8.8.8`).
4. Maaari mo bang lutasin ang isang domain? (`dig google.com`).
5. Nakikinig ba ang application sa inaasahang port? (`ss -tulpn | grep 8080`).
6. Hinaharang ba ng firewall ang port? (Suriin ang`iptables`/`ufw`o cloud security group).
7. Mayroon bang anumang mga error sa mga log ng aplikasyon?
8. May bisa at pinagkakatiwalaan ba ang TLS certificate? (`openssl s_client -connect example.com:443`).