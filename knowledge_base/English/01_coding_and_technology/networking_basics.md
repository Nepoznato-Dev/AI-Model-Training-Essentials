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

# Networking Basics

A practical reference for developers and sysadmins — core concepts, protocols, commands, and troubleshooting.

---

## The OSI Model (7 Layers)

A conceptual framework for understanding network communication.

| Layer | Name | Function | Example protocols |
|-------|------|----------|-------------------|
| 7 | Application | End-user services | HTTP, HTTPS, FTP, SMTP, DNS, SSH |
| 6 | Presentation | Data formatting, encryption, compression | TLS, JPEG, ASCII |
| 5 | Session | Connection management | NetBIOS, RPC |
| 4 | Transport | End-to-end delivery, error correction, flow control | TCP, UDP |
| 3 | Network | Routing, addressing | IP, ICMP, OSPF, BGP |
| 2 | Data Link | Framing, error detection, MAC addresses | Ethernet, Wi-Fi, PPP |
| 1 | Physical | Raw bit transmission | Ethernet cables, fiber optics, radio waves |

In practice, **TCP/IP model** (4 layers: Link, Internet, Transport, Application) is more commonly used for the internet.

---

## IP Addressing

### IPv4
- 32-bit address, written as four octets: `192.168.1.1`
- Total: ~4.3 billion addresses (but exhausted in practice).

### IPv6
- 128-bit address, written in hex: `2001:0db8:85a3:0000:0000:8a2e:0370:7334`
- Total: 2¹²⁸ addresses (practically infinite).

### Private IP Ranges (RFC 1918)
These are not routable on the internet; used inside local networks:
- `10.0.0.0/8` (10.0.0.0 – 10.255.255.255)
- `172.16.0.0/12` (172.16.0.0 – 172.31.255.255)
- `192.168.0.0/16` (192.168.0.0 – 192.168.255.255)

### CIDR Notation
`192.168.1.0/24` means the first 24 bits are the network prefix; the last 8 bits are hosts. It includes addresses `192.168.1.0` to `192.168.1.255`.

---

## DNS (Domain Name System)

Maps domain names (e.g., `example.com`) to IP addresses.

### Record Types
| Type | Purpose |
|------|---------|
| **A** | Maps domain to IPv4 address |
| **AAAA** | Maps domain to IPv6 address |
| **CNAME** | Alias to another domain name |
| **MX** | Mail exchange server |
| **TXT** | Arbitrary text (SPF, DKIM, verification) |
| **NS** | Nameserver for the domain |
| **SRV** | Service record (e.g., for SIP) |

### Common Tools
```bash
dig example.com            # DNS lookup (detailed)
nslookup example.com       # DNS lookup (simpler)
host example.com           # Quick lookup
dig -x 8.8.8.8             # Reverse lookup (IP to name)
```

---

## Ports and Protocols

### Well-Known Ports (0–1023)

| Port | Protocol | Service |
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
| 587 | TCP | SMTP (submission) |
| 993 | TCP | IMAPS |
| 995 | TCP | POP3S |
| 3306 | TCP | MySQL |
| 5432 | TCP | PostgreSQL |
| 6379 | TCP | Redis |
| 27017 | TCP | MongoDB |

### Check Open Ports

```bash
ss -tulpn                 # Linux: listen and established sockets
netstat -an               # Older tool
lsof -i :8080             # See process using port 8080
nmap localhost            # Scan local ports
```

---

## TCP vs UDP

| Feature | TCP | UDP |
|---------|-----|-----|
| Connection | Connection-oriented (handshake) | Connectionless |
| Reliability | Guaranteed delivery, retransmission | Best effort (may drop packets) |
| Ordering | Preserves order | No ordering guarantee |
| Flow control | Yes (sliding window) | No |
| Use cases | Web (HTTP), email, SSH, file transfer | DNS, streaming, VoIP, gaming, SNMP |
| Header size | 20–60 bytes | 8 bytes |

---

## HTTP and HTTPS

### HTTP Methods

| Method | Description |
|--------|-------------|
| **GET** | Retrieve a resource (idempotent, safe) |
| **POST** | Submit data (not idempotent) |
| **PUT** | Update/replace a resource (idempotent) |
| **PATCH** | Partial update |
| **DELETE** | Remove a resource (idempotent) |

### Status Codes

| Code | Meaning |
|------|---------|
| **1xx** | Informational (100 Continue) |
| **2xx** | Success (200 OK, 201 Created, 204 No Content) |
| **3xx** | Redirection (301 Moved Permanently, 302 Found, 304 Not Modified) |
| **4xx** | Client error (400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found, 429 Too Many Requests) |
| **5xx** | Server error (500 Internal Server Error, 502 Bad Gateway, 503 Service Unavailable) |

### Headers

| Header | Purpose |
|--------|---------|
| `Content-Type` | Media type (`application/json`, `text/html`) |
| `Authorization` | Credentials (e.g., `Bearer <token>`) |
| `Cache-Control` | Caching policy |
| CORS headers | `Access-Control-Allow-Origin`, etc. |

---

## TLS/SSL

Encrypts HTTP traffic (HTTPS = HTTP over TLS).

- Certificates from Certificate Authorities (CAs) authenticate the server.
- Verify certificate chain and hostname on the client side.

---

## Firewalls and NAT

### Firewall
- Filters traffic based on rules (source IP, dest IP, port, protocol).
- Stateful firewalls track connection states.

### NAT (Network Address Translation)
- Translates private IPs to a public IP for internet access.
- Port forwarding: maps a public port to an internal host/port.

---

## Common Networking Commands

### Connectivity Tests

```bash
ping google.com            # ICMP echo request
ping -c 4 8.8.8.8          # ping 4 times
traceroute google.com      # Trace the route (Linux)
tracert google.com         # Windows version
```

### Routing

```bash
ip route show              # Linux: routing table
route -n                   # Older Linux
netstat -r                 # Windows/Mac
```

### Network Interfaces

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

### Connectivity to a Port

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

### Network Statistics

```bash
ss -tulpn                  # Show listening sockets (Linux)
netstat -an                # All sockets (all OS)
```

---

## Subnetting (Quick Reference)

| CIDR | Netmask | Number of addresses | Usable hosts |
|------|---------|---------------------|--------------|
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

## Load Balancing and Reverse Proxies

### Nginx as Reverse Proxy

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
- **Least connections**
- **IP hash** (session stickiness)
- **Weighted round-robin**

### Tools

- **Nginx, HAProxy** (software)
- **AWS ELB, Azure Load Balancer, GCP Cloud Load Balancing** (cloud)

---

## Troubleshooting Checklist

1. Is the physical link up? (Check cables, Wi-Fi connection).
2. Can you ping the gateway? (e.g., `ping 192.168.1.1`).
3. Can you ping an external IP? (e.g., `8.8.8.8`).
4. Can you resolve a domain? (`dig google.com`).
5. Is the application listening on the expected port? (`ss -tulpn | grep 8080`).
6. Is the firewall blocking the port? (Check `iptables`/`ufw` or cloud security groups).
7. Are there any errors in the application logs?
8. Is TLS certificate valid and trusted? (`openssl s_client -connect example.com:443`).
