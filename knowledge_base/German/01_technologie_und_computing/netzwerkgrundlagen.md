<!-- 
This file was automatically translated from English to German.
Source: networking_basics.md
Note: Technical terms, code examples, and proper nouns may remain in English.
Für Verbesserungen der Genauigkeit bitten wir um Beiträge via Pull Requests.
-->

# Netzwerkgrundlagen

Eine praktische Referenz für Entwickler und Systemadministratoren – Kernkonzepte, Protokolle, Befehle und Fehlerbehebung.

---

## Das OSI-Modell (7 Schichten)

Ein konzeptioneller Rahmen zum Verständnis der Netzwerkkommunikation.

| Schicht | Name | Funktion | Beispielprotokolle |
|-------|------|----------|-------------------|
| 7 | Anwendung | Endbenutzerdienste | HTTP, HTTPS, FTP, SMTP, DNS, SSH |
| 6 | Darstellung | Datenformatierung, Verschlüsselung, Kompression | TLS, JPEG, ASCII |
| 5 | Sitzung | Verbindungsverwaltung | NetBIOS, RPC |
| 4 | Transport | Ende-zu-Ende-Zustellung, Fehlerkorrektur, Flusskontrolle | TCP, UDP |
| 3 | Netzwerk | Routing, Adressierung | IP, ICMP, OSPF, BGP |
| 2 | Datenverbindung | Framing, Fehlererkennung, MAC-Adressen | Ethernet, Wi-Fi, PPP |
| 1 | Physikalisch | Rohe Bitübertragung | Ethernet-Kabel, Glasfaser, Radiowellen |

In der Praxis wird das **TCP/IP-Modell** (4 Schichten: Verbindung, Internet, Transport, Anwendung) häufiger für das Internet verwendet.

---

## IP-Adressierung

### IPv4
- 32-Bit-Adresse, geschrieben als vier Oktette: `192.168.1.1`
- Gesamt: ~4,3 Milliarden Adressen (in der Praxis jedoch erschöpft).

### IPv6
- 128-Bit-Adresse, geschrieben in Hex: `2001:0db8:85a3:0000:0000:8a2e:0370:7334`
- Gesamt: 2¹²⁸ Adressen (praktisch unendlich).

### Private IP-Bereiche (RFC 1918)
Diese sind nicht im Internet routbar; werden in lokalen Netzwerken verwendet:
- `10.0.0.0/8` (10.0.0.0 – 10.255.255.255)
- `172.16.0.0/12` (172.16.0.0 – 172.31.255.255)
- `192.168.0.0/16` (192.168.0.0 – 192.168.255.255)

### CIDR-Notation
`192.168.1.0/24` bedeutet, dass die ersten 24 Bits das Netzwerkpräfix sind; die letzten 8 Bits sind für Hosts. Es umfasst die Adressen `192.168.1.0` bis `192.168.1.255`.

---

## DNS (Domain Name System)

Ordnet Domainnamen (z. B. `example.com`) IP-Adressen zu.

### Rekordtypen
| Typ | Zweck |
|------|---------|
| **A** | Ordnet Domain einer IPv4-Adresse zu |
| **AAAA** | Ordnet Domain einer IPv6-Adresse zu |
| **CNAME** | Alias zu einem anderen Domainnamen |
| **MX** | Mail-Exchange-Server |
| **TXT** | Beliebiger Text (SPF, DKIM, Verifizierung) |
| **NS** | Nameserver für die Domain |
| **SRV** | Dienst-Rekord (z. B. für SIP) |

### Häufige Werkzeuge
```bash
dig example.com            # DNS-Lookup (detailliert)
nslookup example.com       # DNS-Lookup (einfacher)
host example.com           # Schneller Lookup
dig -x 8.8.8.8             # Reverse-Lookup (IP zu Name)
```

## Ports und Protokolle

### Bekannte Ports (0–1023)
| Port | Protokoll | Dienst |
|------|-----------|--------|
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
| 587 | TCP | SMTP (Submission) |
| 993 | TCP | IMAPS |
| 995 | TCP | POP3S |
| 3306 | TCP | MySQL |
| 5432 | TCP | PostgreSQL |
| 6379 | TCP | Redis |
| 27017 | TCP | MongoDB |

### Offene Ports prüfen
```bash
ss -tulpn                 # Linux: lauschende und etablierte Sockets
netstat -an               # Älteres Tool
lsof -i :8080             # Prozess auf Port 8080 anzeigen
nmap localhost            # Lokale Ports scannen
```

## TCP vs UDP

| Merkmal | TCP | UDP |
|---------|-----|-----|
| Verbindung | Verbindungsorientiert (Handshake) | Verbindungslos |
| Zuverlässigkeit | Garantierte Zustellung, Neuübertragung | Best-Effort-Übertragung (Pakete können verloren gehen) |
| Reihenfolge | Erhält Reihenfolge | Keine Reihenfolgegarantie |
| Flusskontrolle | Ja (Sliding Window) | Nein |
| Einsatzgebiete | Webzugriffe (HTTP), E-Mail, SSH, Dateiübertragung | DNS, Streaming, VoIP, Online-Spiele, SNMP |
| Header-Größe | 20–60 Bytes | 8 Bytes |
HTTP und HTTPS
HTTP-Methoden
GET: Ruft eine Ressource ab (idempotent, sicher).

POST: Sendet Daten an den Server (nicht idempotent).

PUT: Aktualisiert oder ersetzt eine Ressource (idempotent).

PATCH: Führt eine teilweise Aktualisierung durch.

DELETE: Entfernt eine Ressource (idempotent).

Statuscodes
1xx: Informativ (100 Continue).

2xx: Erfolg (200 OK, 201 Created, 204 No Content).

3xx: Umleitung (301 Moved Permanently, 302 Found, 304 Not Modified).

4xx: Clientfehler (400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found, 429 Too Many Requests).

5xx: Serverfehler (500 Internal Server Error, 502 Bad Gateway, 503 Service Unavailable).

Header
Content-Type: Medientyp (application/json, text/html).

Authorization: credentials (e.g., Bearer <token>).

Cache-Control: Caching-Richtlinie.

CORS-Header: Access-Control-Allow-Origin usw.

TLS/SSL
Verschlüsselt HTTP-Datenverkehr (HTTPS = HTTP über TLS).

Zertifikate von Certificate Authorities (CAs) authentifizieren den Server.

Prüfe auf Client-Seite die Zertifikatskette und den Hostnamen.

Firewalls und NAT
Firewall
Filtert Datenverkehr anhand von Regeln (Quell-IP, Ziel-IP, Port, Protokoll).

Zustandsbehaftete Firewalls verfolgen den Zustand von Verbindungen.

NAT (Netzwerkadressübersetzung)
Übersetzt private IPs für den Internetzugang in eine öffentliche IP.

Portweiterleitung: Ordnet einen öffentlichen Port einem internen Host/Port zu.

Häufige Netzwerkbefehle
Verbindungstests
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
Netzwerkschnittstellen
bash
ip addr show               # List interfaces and IPs
ifconfig                   # Older command
DNS
bash
dig example.com
nslookup example.com
host example.com
Verbindung zu einem Port
bash
nc -zv google.com 443      # Netcat: check if port 443 is open
telnet google.com 443      # Telnet to port
curl -v https://google.com # Verbose output
Firewall (Linux iptables/nftables)
bash
sudo ufw status            # Ubuntu: simple firewall
sudo iptables -L -n        # List rules
Netzwerkstatistiken
bash
ss -tulpn                  # Show listening sockets (Linux)
netstat -an                # All sockets (all OS)
Subnetting (Kurzreferenz)
CIDR	Netzmaske	Anzahl der Adressen	Nutzbare Hosts
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
Load Balancing und Reverse Proxys
Nginx als Reverse Proxy
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
Load-Balancing-Algorithmen
Round-Robin

Wenigste Verbindungen

IP-Hash (Sitzungsbindung)

Gewichtetes Round-Robin

Werkzeuge
Nginx, HAProxy (Software)

AWS ELB, Azure Load Balancer, GCP Cloud Load Balancing (Cloud)

Checkliste zur Fehlerbehebung
Ist die physische Verbindung aktiv? (Kabel, Wi-Fi-Verbindung prüfen.)

Lässt sich das Gateway pingen? (z. B. `ping 192.168.1.1`).

Lässt sich eine externe IP pingen? (z. B. `8.8.8.8`).

Lässt sich eine Domain auflösen? (`dig google.com`).

Lauscht die Anwendung auf dem erwarteten Port? (`ss -tulpn | grep 8080`).

Blockiert die Firewall den Port? (iptables/ufw oder Cloud-Sicherheitsgruppen prüfen.)

Gibt es Fehler in den Anwendungsprotokollen?

Ist das TLS-Zertifikat gültig und vertrauenswürdig? (`openssl s_client -connect example.com:443`).

text

---

## Datei 6: `devops_sysadmin.md`

```markdown
# DevOps und System Administration

A practical Leitfaden to managing servers, automating operations, und maintaining reliable infrastructure.

---

## SSH (Secure Shell)

### Schlüsselerzeugung
```bash
ssh-keygen -t ed25519 -C "your_email@example.com"   # Modern and secure
ssh-keygen -t rsa -b 4096 -C "your_email@example.com" # Fallback
Öffentlichen Schlüssel auf den Server kopieren
bash
ssh-copy-id user@host
# Manual alternative:
cat ~/.ssh/id_ed25519.pub | ssh user@host "mkdir -p ~/.ssh && cat >> ~/.ssh/authorized_keys"
SSH-Konfiguration (`~/.ssh/config`)
ssh-config
Host myserver
    HostName 192.168.1.10
    User ubuntu
    IdentityFile ~/.ssh/mykey
    Port 2222
Häufige SSH-Befehle
bash
ssh user@host                    # Connect
ssh -J jumpuser@jumphost user@target   # Proxy jump
scp file.txt user@host:/path/     # Copy file to remote
scp user@host:/path/file.txt .    # Copy from remote
rsync -avz -e ssh ./local/ user@host:/remote/  # Efficient sync
SSH absichern
Root-Anmeldung deaktivieren: PermitRootLogin no

Nur schlüsselbasierte Authentifizierung verwenden: PasswordAuthentication no

Standardport ändern (optional, Sicherheit durch Unauffälligkeit).

AllowUsers oder AllowGroups aktivieren, um den Zugriff einzuschränken.

Systemd (Linux-Dienstverwaltung)
Häufige Befehle
bash
systemctl status nginx           # Check service status
systemctl start nginx            # Start service
systemctl stop nginx
systemctl restart nginx
systemctl reload nginx           # Graceful reload (re-read config)
systemctl enable nginx           # Start on boot
systemctl disable nginx
systemctl list-units --type=service --all   # List all services
systemctl daemon-reload          # Reload unit files after editing
Erstellen einer systemd-Service-Unit
Erstelle `/etc/systemd/system/myapp.service`:

ini
[Unit]
Description=My Python App
After=network.target

[Service]
User=myuser
Group=mygroup
WorkingDirectory=/opt/myapp
ExecStart=/usr/bin/python3 /opt/myapp/main.py
Restart=always
RestartSec=10
Environment="ENV=production"

[Install]
WantedBy=multi-user.target
Danach:

bash
sudo systemctl daemon-reload
sudo systemctl enable myapp
sudo systemctl start myapp
Journalctl (Logs anzeigen)
bash
journalctl -u myapp              # Logs for service
journalctl -f                    # Follow (tail) logs
journalctl --since "1 hour ago"
journalctl _PID=1234             # Filter by process ID
Logging-Strategien
Strukturiertes Logging
Verwende JSON, damit Logs maschinell auswertbar sind:

python
import structlog
logger = structlog.get_logger()
logger.info("user_login", user_id=123, ip="192.168.1.1")
Log-Level
DEBUG: detaillierte Diagnoseinformationen.

INFO: allgemeine Ereignisse (Start, Stopp, normale Transaktionen).

WARN: unerwartet, aber nicht kritisch.

ERROR: Fehler, der eine bestimmte Operation verhindert.

FATAL/CRITICAL: Systemausfall oder sofortiges Eingreifen erforderlich.

Log-Aggregation
ELK Stack (Elasticsearch, Logstash, Kibana) or Elastic Cloud.

Loki + Grafana (lightweight alternative).

Datadog, Splunk, Sumo Logic (SaaS).

Log Rotation (logrotate)
Prevent logs from filling up disks. Configure /etc/logrotate.d/myapp:

logrotate
/var/log/myapp/*.log {
    daily
    rotate 7
    compress
    delaycompress
    missingok
    notifempty
    create 0640 myuser mygroup
}
Monitoring und Alarmierung
Zu überwachende Metriken
System: CPU, RAM, Festplattennutzung, Load Average, Netzwerk-I/O.

Anwendung: Anfragevolumen, Latenz (p50, p95, p99), Fehlerrate, aktive Sitzungen.

Datenbank: Anzahl der Abfragen, langsame Abfragen, Nutzung des Connection Pools.

Geschäftsmetriken: Nutzeranmeldungen, Konversionsrate, Umsatz.

Werkzeuge
Prometheus + Grafana: Standard-Stack aus der Open-Source-Welt.

Node Exporter für Systemmetriken.

Blackbox Exporter für die Verfügbarkeit von Endpunkten.

Alertmanager für die Weiterleitung von Alarmen.

Cloud-nativ: AWS CloudWatch, Azure Monitor, GCP Monitoring.

Verfügbarkeitsüberwachung
Pingdom, Statuspage, Better Uptime, Uptime Kuma (selbst gehostet).

Health Checks: Stelle einen `/health`-Endpunkt bereit, der bei gesundem Dienst `200` zurückgibt.

Backup-Strategien
Die 3-2-1-Regel
3 Kopien der Daten.

2 unterschiedliche Speichermedien (z. B. SSD + Band oder lokal + Cloud).

1 Kopie an einem externen Standort (z. B. Cloud oder entferntes Rechenzentrum).

Backup-Typen
Vollbackup: Kopiert alles (langsam, hoher Speicherbedarf).

Inkrementelles Backup: Kopiert nur Änderungen seit dem letzten Voll- oder inkrementellen Backup (schnell, aber komplexere Wiederherstellung).

Differenzielles Backup: Kopiert Änderungen seit dem letzten Vollbackup (Mittelweg).

Datenbank-Backups
bash
# PostgreSQL
pg_dump dbname > backup.sql
pg_dumpall > all_backup.sql

# MySQL / MariaDB
mysqldump -u root -p dbname > backup.sql

# Restore
psql dbname < backup.sql
mysql -u root -p dbname < backup.sql
Datei-Backups
bash
# Tar archive
tar -czf backup.tar.gz /var/lib/data

# Rsync to remote
rsync -avz /local/data/ user@backup-server:/backup/data/

# Cloud CLI (e.g., AWS S3)
aws s3 sync /local/data s3://my-bucket/backup/
Automatisierte Backup-Planung (cron)
cron
# Run daily at 2am
0 2 * * * /usr/local/bin/backup_script.sh
Cron und geplante Aufgaben
Cron-Syntax
text
* * * * * command
│ │ │ │ │
│ │ │ │ └─ Wochentag (0-7, 0=So)
│ │ │ └─── Monat (1-12)
│ │ └───── Tag des Monats (1-31)
│ └─────── Stunde (0-23)
└───────── Minute (0-59)
Beispiele
cron
# Every 5 minutes
*/5 * * * * /path/to/script

# Every day at 3:15 AM
15 3 * * * /path/to/script

# Every Monday at 4 AM
0 4 * * 1 /path/to/script

# Every hour
0 * * * * /path/to/script
Cron verwalten
bash
crontab -l          # List current user's cron jobs
crontab -e          # Edit
crontab -r          # Remove all
Anacron
Wird für Systeme verwendet, die nicht rund um die Uhr laufen (z. B. Laptops), und stellt sicher, dass Aufgaben schließlich ausgeführt werden.

Paketverwaltung und Updates
Debian/Ubuntu (apt)
bash
sudo apt update                # Update package list
sudo apt upgrade               # Upgrade all packages
sudo apt install git nginx
sudo apt remove git
sudo apt autoremove            # Remove unused dependencies
RHEL/CentOS/Fedora (dnf/yum)
bash
sudo dnf check-update
sudo dnf update
sudo dnf install git nginx
sudo dnf remove git
Sicherheitsupdates
Aktiviere unter Ubuntu `unattended-upgrades` für Sicherheitspatches:

bash
sudo apt install unattended-upgrades
sudo dpkg-reconfigure -plow unattended-upgrades
Docker in Produktion
Bewährte Praktiken
Verwende konkrete Image-Tags (`python:3.12-slim`) statt `latest`.

Lass Container nicht als Root-Benutzer laufen.

Prüfe Images auf Schwachstellen (`docker scan`, `trivy`).

Setze Ressourcenlimits (`--memory`, `--cpus`).

Verwende Geheimnisse sorgfältig (etwa über Docker secrets oder Umgebungsvariablen).

Halte Images klein: Multi-Stage-Builds, schlanke Basis-Images.

Docker Compose in Produktion
Setze Ressourcenlimits in `docker-compose.yml`:

yaml
services:
  app:
    image: myapp:1.0
    deploy:
      resources:
        limits:
          memory: 512M
          cpus: '0.5'
CI/CD-Grundlagen
Pipeline-Stufen
Build: Code kompilieren, Abhängigkeiten installieren.

Test: Unit-, Integrations- und Lint-Prüfungen ausführen.

Containerise: Docker-Image bauen.

Push: Image in die Container-Registry hochladen.

Deploy: Staging- oder Produktionsumgebung aktualisieren.

Werkzeuge
GitHub Actions: In GitHub integriert.

GitLab CI: Direkt in GitLab integriert.

Jenkins: Traditionell und stark konfigurierbar.

CircleCI, Travis CI: Beliebte Drittanbieter.

ArgoCD: GitOps für Kubernetes.

Beispiel für eine einfache GitHub Action:
yaml
name: CI
on: push
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.12'
      - run: pip install -r requirements.txt
      - run: pytest
Systemoptimierung und Fehlerbehebung
Festplattenspeicher prüfen
bash
df -h                      # Human-readable disk usage
du -sh /* | sort -h        # Size of top-level directories
Speicherauslastung prüfen
bash
free -m                    # Memory in MB
vmstat 1 10                # Virtual memory statistics
top -o %MEM                # Sort processes by memory
CPU-Last prüfen
bash
uptime                     # Load average over 1,5,15 minutes
top -o %CPU                # Sort processes by CPU
mpstat -P ALL 1 5          # Per-core CPU usage
Netzwerk prüfen
bash
netstat -i                 # Interface statistics
iftop                      # Live bandwidth usage (requires install)
nload                      # Another bandwidth monitor
Große Dateien finden
bash
find / -type f -size +100M -exec ls -lh {} \; 2>/dev/null
Infrastruktur als Code (IaC)
Terraform
Definiere Cloud-Ressourcen in HCL.

hcl
provider "aws" {
  region = "us-east-1"
}
resource "aws_instance" "web" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t2.micro"
}
Ansible
Agentenlose Konfigurationsverwaltung mit YAML.

yaml
- name: Install nginx
  hosts: webservers
  tasks:
    - name: Install nginx
      apt:
        name: nginx
        state: present
Bewährte Praktiken
Verwende Module und Rollen für bessere Wiederverwendbarkeit.

Speichere den Zustand remote (S3, Terraform Cloud).

Verwende Variablen und Geheimnisse (`AWS_SECRET_ACCESS_KEY` über die Umgebung, nicht fest im Code).

Verwalte deinen IaC-Code in der Versionskontrolle.

Incident Response (Bereitschaftsdienst)
Checkliste für Dienstausfälle
Alarm bestätigen.

Umfang bewerten: Welche Dienste oder Nutzer sind betroffen?

Problem eingrenzen (Logs, Metriken, aktuelle Deployments prüfen).

Wenn möglich eindämmen (Circuit Breaker, Feature Flags).

Rollback durchführen oder vorwärts beheben.

Status an Stakeholder und Nutzer kommunizieren (Statusseite).

Zeitverlauf und Maßnahmen des Vorfalls dokumentieren.

Post-Mortem: Innerhalb von 24–48 Stunden eine Ursachenanalyse (RCA) und Maßnahmen zur Vermeidung von Wiederholungen verfassen.