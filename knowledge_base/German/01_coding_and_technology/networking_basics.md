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
# Netzwerkgrundlagen
Eine praktische Referenz für Entwickler und Systemadministratoren – Kernkonzepte, Protokolle, Befehle und Fehlerbehebung.
---

## Das OSI-Modell (7 Schichten)
Ein konzeptioneller Rahmen zum Verständnis der Netzwerkkommunikation.
| Schicht | Name | Funktion | Beispielprotokolle |
|-------|------|----------|-----|
| 7 | Bewerbung | Endbenutzerdienste | HTTP, HTTPS, FTP, SMTP, DNS, SSH |
| 6 | Präsentation | Datenformatierung, Verschlüsselung, Komprimierung | TLS, JPEG, ASCII |
| 5 | Sitzung | Verbindungsverwaltung | NetBIOS, RPC |
| 4 | Transport | End-to-End-Lieferung, Fehlerkorrektur, Flusskontrolle | TCP, UDP |
| 3 | Netzwerk | Routing, Adressierung | IP, ICMP, OSPF, BGP |
| 2 | Datenverbindung | Framing, Fehlererkennung, MAC-Adressen | Ethernet, WLAN, PPP |
| 1 | Physisch | Rohbitübertragung | Ethernet-Kabel, Glasfaser, Funkwellen |
In der Praxis wird für das Internet häufiger das **TCP/IP-Modell** (4 Schichten: Verbindung, Internet, Transport, Anwendung) verwendet.
---

## IP-Adressierung
### IPv4
– 32-Bit-Adresse, geschrieben als vier Oktette:`192.168.1.1`
- Gesamt: ~4,3 Milliarden Adressen (aber in der Praxis erschöpft).
### IPv6
- 128-Bit-Adresse, geschrieben in Hex:`2001:0db8:85a3:0000:0000:8a2e:0370:7334`
- Insgesamt: 2¹²⁸ Adressen (praktisch unendlich).
### Private IP-Bereiche (RFC 1918)
Diese sind im Internet nicht weiterleitbar; Wird in lokalen Netzwerken verwendet:
-`10.0.0.0/8`(10.0.0.0 – 10.255.255.255)
-`172.16.0.0/12`(172.16.0.0 – 172.31.255.255)
-`192.168.0.0/16`(192.168.0.0 – 192.168.255.255)
### CIDR-Notation
`192.168.1.0/24`bedeutet, dass die ersten 24 Bits das Netzwerkpräfix sind; Die letzten 8 Bits sind Hosts. Es umfasst die Adressen`192.168.1.0`bis`192.168.1.255`.
---

## DNS (Domain Name System)
Ordnet Domänennamen (z. B.`example.com`) IP-Adressen zu.
### Datensatztypen
| Geben Sie | ein Zweck |
|------|---------|
| **A** | Ordnet die Domäne der IPv4-Adresse zu |
| **AAAA** | Ordnet die Domäne der IPv6-Adresse zu |
| **CNAME** | Alias ​​für einen anderen Domainnamen |
| **MX** | Mail-Exchange-Server |
| **TXT** | Beliebiger Text (SPF, DKIM, Verifizierung) |
| **NS** | Nameserver für die Domain |
| **SRV** | Dienstaufzeichnung (z. B. für SIP) |
### Gemeinsame Tools```bash
dig example.com            # DNS lookup (detailed)
nslookup example.com       # DNS lookup (simpler)
host example.com           # Quick lookup
dig -x 8.8.8.8             # Reverse lookup (IP to name)
```

---

## Ports und Protokolle
### Bekannte Häfen (0–1023)
| Hafen | Protokoll | Service |
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
| 587 | TCP | SMTP (Übermittlung) |
| 993 | TCP | IMAPS |
| 995 | TCP | POP3S |
| 3306 | TCP | MySQL |
| 5432 | TCP | PostgreSQL |
| 6379 | TCP | Redis |
| 27017 | TCP | MongoDB |
### Überprüfen Sie die offenen Ports
```bash
ss -tulpn                 # Linux: listen and established sockets
netstat -an               # Older tool
lsof -i :8080             # See process using port 8080
nmap localhost            # Scan local ports
```

---

## TCP vs. UDP
| Funktion | TCP | UDP |
|---------|-----|-----|
| Verbindung | Verbindungsorientiert (Handshake) | Verbindungslos |
| Zuverlässigkeit | Garantierte Lieferung, Weiterverbreitung | Bester Aufwand (kann Pakete verwerfen) |
| Bestellen | Bewahrt die Ordnung | Keine Bestellgarantie |
| Flusskontrolle | Ja (Schiebefenster) | Nein |
| Anwendungsfälle | Web (HTTP), E-Mail, SSH, Dateiübertragung | DNS, Streaming, VoIP, Gaming, SNMP |
| Headergröße | 20–60 Byte | 8 Byte |
---

## HTTP und HTTPS
### HTTP-Methoden
| Methode | Beschreibung |
|--------|-------------|
| **GET** | Eine Ressource abrufen (idempotent, sicher) |
| **POST** | Daten übermitteln (nicht idempotent) |
| **PUT** | Eine Ressource aktualisieren/ersetzen (idempotent) |
| **PATCH** | Teilaktualisierung |
| **LÖSCHEN** | Eine Ressource entfernen (idempotent) |
### Statuscodes
| Code | Bedeutung |
|------|---------|
| **1xx** | Informativ (100 Weiter) |
| **2xx** | Erfolg (200 OK, 201 erstellt, 204 kein Inhalt) |
| **3xx** | Umleitung (301 dauerhaft verschoben, 302 gefunden, 304 nicht geändert) |
| **4xx** | Clientfehler (400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found, 429 Too Many Requests) |
| **5xx** | Serverfehler (500 Interner Serverfehler, 502 Schlechtes Gateway, 503 Dienst nicht verfügbar) |
### Kopfzeilen
| Kopfzeile | Zweck |
|--------|---------|
| `Content-Type`| Medientyp (`application/json`,`text/html`) |
| `Authorization`| Anmeldeinformationen (z. B.`Bearer <token>`) |
| `Cache-Control`| Caching-Richtlinie |
| CORS-Header | `Access-Control-Allow-Origin`usw. |
---

## TLS/SSL
Verschlüsselt den HTTP-Verkehr (HTTPS = HTTP über TLS).
- Zertifikate von Zertifizierungsstellen (CAs) authentifizieren den Server.
– Überprüfen Sie die Zertifikatskette und den Hostnamen auf der Clientseite.
---

## Firewalls und NAT
### Firewall
- Filtert den Datenverkehr basierend auf Regeln (Quell-IP, Ziel-IP, Port, Protokoll).
- Stateful Firewalls verfolgen Verbindungszustände.
### NAT (Network Address Translation)
- Übersetzt private IPs in eine öffentliche IP für den Internetzugang.
- Portweiterleitung: Ordnet einen öffentlichen Port einem internen Host/Port zu.
---

## Allgemeine Netzwerkbefehle
### Konnektivitätstests
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

### Netzwerkschnittstellen
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

### Konnektivität zu einem Port
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

### Netzwerkstatistik
```bash
ss -tulpn                  # Show listening sockets (Linux)
netstat -an                # All sockets (all OS)
```

---

## Subnetting (Kurzreferenz)
| CIDR | Netzmaske | Anzahl der Adressen | Verwendbare Hosts |
|------|---------|-------|--------------|
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

## Load Balancing und Reverse Proxys
### Nginx als Reverse Proxy
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

### Lastausgleichsalgorithmen
- **Round-Robin**
- **Geringste Verbindungen**
- **IP-Hash** (Session Stickiness)
- **Gewichtetes Round-Robin**
### Werkzeuge
- **Nginx, HAProxy** (Software)
- **AWS ELB, Azure Load Balancer, GCP Cloud Load Balancing** (Cloud)
---

## Checkliste zur Fehlerbehebung
1. Ist die physische Verbindung hergestellt? (Überprüfen Sie Kabel und WLAN-Verbindung).
2. Können Sie das Gateway anpingen? (z. B.`ping 192.168.1.1`).
3. Können Sie eine externe IP anpingen? (z. B.`8.8.8.8`).
4. Können Sie eine Domain auflösen? (`dig google.com`).
5. Hört die Anwendung auf dem erwarteten Port? (`ss -tulpn | grep 8080`).
6. Blockiert die Firewall den Port? (Überprüfen Sie`iptables`/`ufw`oder Cloud-Sicherheitsgruppen).
7. Gibt es Fehler in den Anwendungsprotokollen?
8. Ist das TLS-Zertifikat gültig und vertrauenswürdig? (`openssl s_client -connect example.com:443`).