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
# Misingi ya Mitandao
Marejeleo ya vitendo kwa wasanidi programu na sysadmins - dhana za msingi, itifaki, amri na utatuzi wa matatizo.
---

## Muundo wa OSI (Tabaka 7)
Mfumo wa dhana wa kuelewa mawasiliano ya mtandao.
| Tabaka | Jina | Kazi | Mfano wa itifaki |
|-------|------|------------------------------|
| 7 | Maombi | Huduma za mtumiaji wa mwisho | HTTP, HTTPS, FTP, SMTP, DNS, SSH |
| 6 | Wasilisho | Uumbizaji wa data, usimbaji fiche, mbano | TLS, JPEG, ASCII |
| 5 | Kikao | Usimamizi wa muunganisho | NetBIOS, RPC |
| 4 | Usafiri | Uwasilishaji wa mwisho hadi mwisho, urekebishaji wa makosa, udhibiti wa mtiririko | TCP, UDP |
| 3 | Mtandao | Kuelekeza, kuhutubia | IP, ICMP, OSPF, BGP |
| 2 | Kiungo cha Data | Kutunga, kutambua makosa, anwani za MAC | Ethaneti, Wi-Fi, PPP |
| 1 | Kimwili | Usambazaji wa biti ghafi | Kebo za Ethaneti, optics za nyuzi, mawimbi ya redio |
Kwa vitendo, **Mtindo wa TCP/IP** (safu 4: Kiungo, Mtandao, Usafiri, Programu) hutumiwa zaidi kwa mtandao.
---

## Anwani ya IP
### IPv4
- Anwani ya biti-32, iliyoandikwa kama pweza nne:`192.168.1.1`
- Jumla: ~ anwani bilioni 4.3 (lakini imechoka kimatendo).
### IPv6
- Anwani ya 128-bit, iliyoandikwa kwa hex:`2001:0db8:85a3:0000:0000:8a2e:0370:7334`
- Jumla: 2¹²⁸ anwani (isiyo na kikomo).
### Masafa ya IP ya Kibinafsi (RFC 1918)
Hizi haziwezi kubadilishwa kwenye mtandao; kutumika ndani ya mitandao ya ndani:
-`10.0.0.0/8`(10.0.0.0 - 10.255.255.255)
-`172.16.0.0/12`(172.16.0.0 - 172.31.255.255)
-`192.168.0.0/16`(192.168.0.0 - 192.168.255.255)
### Nukuu ya CIDR
`192.168.1.0/24`inamaanisha biti 24 za kwanza ni kiambishi awali cha mtandao; Biti 8 za mwisho ni wapangishaji. Inajumuisha anwani`192.168.1.0`hadi`192.168.1.255`.
---

## DNS (Mfumo wa Jina la Kikoa)
Majina ya vikoa vya Ramani (k.m.,`example.com`) hadi anwani za IP.
### Aina za Rekodi
| Andika | Kusudi |
|------|----------|
| **A** | Kikoa cha Ramani hadi anwani ya IPv4 |
| **AAAA** | Kikoa cha Ramani hadi anwani ya IPv6 |
| **CNAME** | Lakabu kwa jina lingine la kikoa |
| **MX** | Seva ya kubadilishana barua |
| **TXT** | Maandishi ya kiholela (SPF, DKIM, uthibitishaji) |
| **NS** | Nameserver kwa kikoa |
| **SRV** | Rekodi ya huduma (k.m., kwa SIP) |
### Zana za Kawaida```bash
dig example.com            # DNS lookup (detailed)
nslookup example.com       # DNS lookup (simpler)
host example.com           # Quick lookup
dig -x 8.8.8.8             # Reverse lookup (IP to name)
```

---

## Bandari na Itifaki
### Bandari Zinazojulikana (0–1023)
| Bandari | Itifaki | Huduma |
|------|---------------------|
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
| 587 | TCP | SMTP (mawasilisho) |
| 993 | TCP | IMAPS |
| 995 | TCP | POP3S |
| 3306 | TCP | MySQL |
| 5432 | TCP | PostgreSQL |
| 6379 | TCP | Redi |
| 27017 | TCP | MongoDB |
### Angalia Bandari Zilizofunguliwa
```bash
ss -tulpn                 # Linux: listen and established sockets
netstat -an               # Older tool
lsof -i :8080             # See process using port 8080
nmap localhost            # Scan local ports
```

---

## TCP dhidi ya UDP
| Kipengele | TCP | UDP |
|---------|-----|-----|
| Muunganisho | Mwelekeo wa kuunganisha (kupeana mkono) | Isiyounganishwa |
| Kuegemea | Uwasilishaji uliohakikishwa, uhamishaji upya | Juhudi bora (inaweza kuacha pakiti) |
| Kuagiza | Huhifadhi agizo | Hakuna dhamana ya kuagiza |
| Udhibiti wa mtiririko | Ndiyo (dirisha linaloteleza) | Hapana |
| Tumia kesi | Wavuti (HTTP), barua pepe, SSH, uhamishaji wa faili | DNS, utiririshaji, VoIP, michezo ya kubahatisha, SNMP |
| Ukubwa wa kichwa | 20-60 baiti | baiti 8 |
---

## HTTP na HTTPS
### Mbinu za HTTP
| Mbinu | Maelezo |
|--------|-------------|
| **PATA** | Rejesha rasilimali (isiyo na uwezo, salama) |
| **POST** | Wasilisha data (sio ujinga) |
| **WEKA** | Sasisha/badilisha rasilimali (isiyo na uwezo) |
| **PATCH** | Usasishaji kiasi |
| **FUTA** | Ondoa rasilimali (isiyo na uwezo) |
### Misimbo ya Hali
| Msimbo | Maana |
|------|----------|
| **1xx** | Taarifa (100 Endelea) |
| **2xx** | Mafanikio (200 Sawa, 201 Imeundwa, 204 Hakuna Maudhui) |
| **3xx** | Kuelekeza Kwingine (301 Imehamishwa Kabisa, 302 Imepatikana, 304 Haijarekebishwa) |
| **4xx** | Hitilafu ya Mteja (Ombi Mbaya 400, 401 Haijaidhinishwa, 403 Haramu, 404 Haijapatikana, Maombi 429 Nyingi Sana) |
| **5xx** | Hitilafu ya seva (Hitilafu 500 ya Seva ya Ndani, Lango Mbaya 502, Huduma ya 503 Haipatikani) |
### Vichwa
| Kichwa | Kusudi |
|--------|----------|
| `Content-Type`| Aina ya media (`application/json`,`text/html`) |
| `Authorization`| Kitambulisho (k.m.,`Bearer <token>`) |
| `Cache-Control`| Sera ya akiba |
| Vichwa vya CORS | `Access-Control-Allow-Origin`, nk. |
---

## TLS/SSL
Husimba trafiki ya HTTP (HTTPS = HTTP juu ya TLS).
- Vyeti kutoka kwa Mamlaka za Cheti (CAs) huthibitisha seva.
- Thibitisha msururu wa cheti na jina la mwenyeji kwenye upande wa mteja.
---

## Firewalls na NAT
### Firewall
- Filters trafiki kulingana na sheria (chanzo IP, dest IP, bandari, itifaki).
- Stateful firewalls kufuatilia majimbo uhusiano.
### NAT (Tafsiri ya Anwani ya Mtandao)
- Inatafsiri IP za kibinafsi kwa IP ya umma kwa ufikiaji wa mtandao.
- Usambazaji wa lango: huweka lango la umma kwa mwenyeji/mlango wa ndani.
---

## Amri za Kawaida za Mitandao
### Majaribio ya Muunganisho
```bash
ping google.com            # ICMP echo request
ping -c 4 8.8.8.8          # ping 4 times
traceroute google.com      # Trace the route (Linux)
tracert google.com         # Windows version
```

### Uelekezaji
```bash
ip route show              # Linux: routing table
route -n                   # Older Linux
netstat -r                 # Windows/Mac
```

### Violesura vya Mtandao
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

### Muunganisho kwenye Bandari
```bash
nc -zv google.com 443      # Netcat: check if port 443 is open
telnet google.com 443      # Telnet to port
curl -v https://google.com # Verbose output
```

### Firewall (Linux iptables/nfttables)
```bash
sudo ufw status            # Ubuntu: simple firewall
sudo iptables -L -n        # List rules
```

### Takwimu za Mtandao
```bash
ss -tulpn                  # Show listening sockets (Linux)
netstat -an                # All sockets (all OS)
```

---

## Subnetting (Rejea ya Haraka)
| CIDR | Netmask | Idadi ya anwani | Wapangishi wanaoweza kutumika |
|------|---------------------------------------------|
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

## Kusawazisha Mizigo na Wakala wa Nyuma
### Nginx kama Wakala wa Kinyume
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

### Kanuni za Kusawazisha Mizigo
- **Robin-raundi**
- **Miunganisho ndogo zaidi **
- ** IP hash ** (kunata kwa kikao)
- ** robin yenye uzani **
### Zana
- **Nginx, HAProxy** (programu)
- **AWS ELB, Kisawazisha cha Mzigo wa Azure, Usawazishaji wa Mzigo wa Wingu wa GCP** (wingu)
---

Orodha ## ya Utatuzi wa Matatizo
1. Je, kiungo cha kimwili kiko juu? (Angalia nyaya, muunganisho wa Wi-Fi).
2. Je, unaweza kupenyeza lango? (k.m.,`ping 192.168.1.1`).
3. Je, unaweza kubandika IP ya nje? (k.m.,`8.8.8.8`).
4. Je, unaweza kutatua kikoa? (`dig google.com`).
5. Je, programu inasikilizwa kwenye bandari inayotarajiwa? (`ss -tulpn | grep 8080`).
6. Je, firewall inazuia bandari? (Angalia`iptables`/`ufw`au vikundi vya usalama vya wingu).
7. Je, kuna makosa yoyote katika kumbukumbu za programu?
8. Je, cheti cha TLS ni halali na kinaaminika? (`openssl s_client -connect example.com:443`).