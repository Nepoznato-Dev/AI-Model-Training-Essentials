# Netzwerkgrundlagen

Eine praktische Referenz für Entwickler und Systemadministratoren — Kernkonzepte, Protokolle, Befehle und Fehlersuche.

---

## Das OSI-Modell (7 Schichten)

Ein konzeptioneller Rahmen zum Verständnis der Netzwerkkommunikation.

| Schicht | Name | Funktion | Beispielprotokolle |
|-------|------|----------|-------------------|
| 7 | Anwendung | Dienste für Endbenutzer | HTTP, HTTPS, FTP, SMTP, DNS, SSH |
| 6 | Darstellung | Datenformatierung, Verschlüsselung, Komprimierung | TLS, JPEG, ASCII |
| 5 | Sitzung | Verbindungsverwaltung | NetBIOS, RPC |
| 4 | Transport | Ende-zu-Ende-Übertragung, Fehlerkorrektur, Flusskontrolle | TCP, UDP |
| 3 | Netzwerk | Routing, Adressierung | IP, ICMP, OSPF, BGP |
| 2 | Sicherung | Framing, Fehlererkennung, MAC-Adressen | Ethernet, Wi-Fi, PPP |
| 1 | Bitübertragung | Übertragung roher Bits | Ethernet-Kabel, Glasfaser, Funkwellen |

In der Praxis wird für das Internet häufiger das **TCP/IP-Modell** (4 Schichten: Link, Internet, Transport, Anwendung) verwendet.

---

## IP-Adressierung

### IPv4
- 32-Bit-Adresse, geschrieben als vier Oktette: `192.168.1.1`
- Insgesamt: ~4,3 Milliarden Adressen (in der Praxis jedoch erschöpft).

### IPv6
- 128-Bit-Adresse, hexadezimal geschrieben: `2001:0db8:85a3:0000:0000:8a2e:0370:7334`
- Insgesamt: 2¹²⁸ Adressen (praktisch unendlich).

### Private IP-Bereiche (RFC 1918)
Diese sind im Internet nicht routbar; sie werden innerhalb lokaler Netzwerke verwendet:
- `10.0.0.0/8` (10.0.0.0 – 10.255.255.255)
- `172.16.0.0/12` (172.16.0.0 – 172.31.255.255)
- `192.168.0.0/16` (192.168.0.0 – 192.168.255.255)

### CIDR-Notation
`192.168.1.0/24` bedeutet, dass die ersten 24 Bits das Netzwerkpräfix sind; die letzten 8 Bits sind Hosts. Es umfasst die Adressen `192.168.1.0` bis `192.168.1.255`.

---

## DNS (Domain Name System)

Ordnet Domainnamen (z. B. `example.com`) IP-Adressen zu.

### Record-Typen
| Typ | Zweck |
|------|---------|
| **A** | Ordnet eine Domain einer IPv4-Adresse zu |
| **AAAA** | Ordnet eine Domain einer IPv6-Adresse zu |
| **CNAME** | Alias für einen anderen Domainnamen |
| **MX** | Mail-Exchange-Server |
| **TXT** | Beliebiger Text (SPF, DKIM, Verifizierung) |
| **NS** | Nameserver für die Domain |
| **SRV** | Service-Record (z. B. für SIP) |

### Häufige Werkzeuge
```bash
dig example.com            # DNS-Lookup (detailliert)
nslookup example.com       # DNS-Lookup (einfacher)
host example.com           # Schneller Lookup
dig -x 8.8.8.8             # Reverse Lookup (IP zu Name)

Ports und Protokolle
Well-Known-Ports (0–1023)
PortProtokollDienst
20, 21TCPFTP
22TCPSSH
23TCPTelnet
25TCPSMTP
53UDP/TCPDNS
80TCPHTTP
110TCPPOP3
123UDPNTP
143TCPIMAP
443TCPHTTPS
465TCPSMTPS
587TCPSMTP (submission)
993TCPIMAPS
995TCPPOP3S
3306TCPMySQL
5432TCPPostgreSQL
6379TCPRedis
27017TCPMongoDB
Open Ports prüfen
bash
ss -tulpn                 # Linux: lauschende und aufgebaute Sockets
netstat -an               # Älteres Werkzeug
lsof -i :8080             # Prozess anzeigen, der Port 8080 verwendet
nmap localhost            # Lokale Ports scannen
TCP vs UDP
MerkmalTCPUDP
VerbindungVerbindungsorientiert (Handshake)Verbindungslos
ZuverlässigkeitGarantierte Zustellung, erneute ÜbertragungBest Effort (Pakete können verloren gehen)
ReihenfolgeBehält die Reihenfolge beiKeine Garantie für Reihenfolge
FlusskontrolleJa (Sliding Window)Nein
AnwendungsfälleWeb (HTTP), E-Mail, SSH, DateiübertragungDNS, Streaming, VoIP, Gaming, SNMP
Header-Größe20–60 Bytes8 Bytes
HTTP und HTTPS
HTTP-Methoden
GET: Eine Ressource abrufen (idempotent, sicher).

POST: Daten senden (nicht idempotent).

PUT: Eine Ressource aktualisieren/ersetzen (idempotent).

PATCH: Teilaktualisierung.

DELETE: Eine Ressource entfernen (idempotent).

Status-Codes
1xx: Informativ (100 Continue).

2xx: Erfolg (200 OK, 201 Created, 204 No Content).

3xx: Umleitung (301 Moved Permanently, 302 Found, 304 Not Modified).

4xx: Client-Fehler (400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found, 429 Too Many Requests).

5xx: Serverfehler (500 Internal Server Error, 502 Bad Gateway, 503 Service Unavailable).

Header
Content-Type: Medientyp (application/json, text/html).

Authorization: Anmeldedaten (z. B. Bearer <token>).

Cache-Control: Caching-Richtlinie.

CORS-Header: Access-Control-Allow-Origin usw.

TLS/SSL
Verschlüsselt HTTP-Verkehr (HTTPS = HTTP über TLS).

Zertifikate von Certificate Authorities (CAs) authentifizieren den Server.

Prüfe Zertifikatskette und Hostname auf Client-Seite.

Firewalls und NAT
Firewall
Filtert Datenverkehr anhand von Regeln (Quell-IP, Ziel-IP, Port, Protokoll).

Zustandsbehaftete Firewalls verfolgen Verbindungszustände.

NAT (Network Address Translation)
Übersetzt private IPs in eine öffentliche IP für den Internetzugang.

Portweiterleitung: Ordnet einen öffentlichen Port einem internen Host/Port zu.

Häufige Netzwerkbefehle
Konnektivitätstests
bash
ping google.com            # ICMP-Echo-Request
ping -c 4 8.8.8.8          # 4-mal pingen
traceroute google.com      # Route verfolgen (Linux)
tracert google.com         # Windows-Version
Routing
bash
ip route show              # Linux: Routing-Tabelle
route -n                   # Älteres Linux
netstat -r                 # Windows/Mac
Netzwerkschnittstellen
bash
ip addr show               # Schnittstellen und IPs auflisten
ifconfig                   # Älterer Befehl
DNS
bash
dig example.com
nslookup example.com
host example.com
Konnektivität zu einem Port
bash
nc -zv google.com 443      # Netcat: prüfen, ob Port 443 offen ist
telnet google.com 443      # Telnet zu Port
curl -v https://google.com # Ausführliche Ausgabe
Firewall (Linux iptables/nftables)
bash
sudo ufw status            # Ubuntu: einfache Firewall
sudo iptables -L -n        # Regeln auflisten
Netzwerkstatistiken
bash
ss -tulpn                  # Lauschende Sockets anzeigen (Linux)
netstat -an                # Alle Sockets (alle Betriebssysteme)
Subnetting (Kurzübersicht)
CIDRNetmaskAnzahl der AdressenNutzbare Hosts
/32255.255.255.25511
/30255.255.255.25242
/29255.255.255.24886
/28255.255.255.2401614
/27255.255.255.2243230
/26255.255.255.1926462
/25255.255.255.128128126
/24255.255.255.0256254
/23255.255.254.0512510
/22255.255.252.01,0241,022
/16255.255.0.065,53665,534
/8255.0.0.016,777,21616,777,214
Load Balancing und Reverse Proxies
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

Least Connections

IP-Hash (Session-Stickiness)

Gewichtetes Round-Robin

Werkzeuge
Nginx, HAProxy (Software)

AWS ELB, Azure Load Balancer, GCP Cloud Load Balancing (Cloud)

Checkliste zur Fehlersuche
Ist die physische Verbindung aktiv? (Kabel, Wi-Fi-Verbindung prüfen).

Kannst du das Gateway anpingen? (z. B. ping 192.168.1.1).

Kannst du eine externe IP anpingen? (z. B. 8.8.8.8).

Kannst du eine Domain auflösen? (dig google.com).

Lauscht die Anwendung auf dem erwarteten Port? (ss -tulpn | grep 8080).

Blockiert die Firewall den Port? (iptables/ufw oder Cloud-Security-Groups prüfen).

Gibt es Fehler in den Anwendungslogs?

Ist das TLS-Zertifikat gültig und vertrauenswürdig? (openssl s_client -connect example.com:443).

text

---

## Datei 6: `devops_sysadmin.md`

```markdown
# DevOps und Systemadministration

Ein praktischer Leitfaden zur Verwaltung von Servern, zur Automatisierung von Betriebsabläufen und zur Aufrechterhaltung einer zuverlässigen Infrastruktur.

---

## SSH (Secure Shell)

### Schlüsselerzeugung
```bash
ssh-keygen -t ed25519 -C "your_email@example.com"   # Modern und sicher
ssh-keygen -t rsa -b 4096 -C "your_email@example.com" # Fallback
Öffentlichen Schlüssel auf den Server kopieren
bash
ssh-copy-id user@host
# Manuelle Alternative:
cat ~/.ssh/id_ed25519.pub | ssh user@host "mkdir -p ~/.ssh && cat >> ~/.ssh/authorized_keys"
SSH-Konfiguration (~/.ssh/config)
ssh-config
Host myserver
    HostName 192.168.1.10
    User ubuntu
    IdentityFile ~/.ssh/mykey
    Port 2222
Häufige SSH-Befehle
bash
ssh user@host                    # Verbinden
ssh -J jumpuser@jumphost user@target   # Proxy-Jump
scp file.txt user@host:/path/     # Datei auf Remote-System kopieren
scp user@host:/path/file.txt .    # Von Remote-System kopieren
rsync -avz -e ssh ./local/ user@host:/remote/  # Effiziente Synchronisierung
SSH härten
Root-Login deaktivieren: PermitRootLogin no

Nur schlüsselbasierte Authentifizierung verwenden: PasswordAuthentication no

Standardport ändern (optional, Security through obscurity).

AllowUsers oder AllowGroups aktivieren, um den Zugriff einzuschränken.

Systemd (Linux-Service-Verwaltung)
Häufige Befehle
bash
systemctl status nginx           # Service-Status prüfen
systemctl start nginx            # Service starten
systemctl stop nginx
systemctl restart nginx
systemctl reload nginx           # Schonendes Neuladen (Konfiguration neu einlesen)
systemctl enable nginx           # Beim Booten starten
systemctl disable nginx
systemctl list-units --type=service --all   # Alle Services auflisten
systemctl daemon-reload          # Unit-Dateien nach dem Bearbeiten neu laden
Eine systemd-Service-Unit erstellen
Erstelle /etc/systemd/system/myapp.service:

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
Dann:

bash
sudo systemctl daemon-reload
sudo systemctl enable myapp
sudo systemctl start myapp
Journalctl (Logs anzeigen)
bash
journalctl -u myapp              # Logs für den Service
journalctl -f                    # Logs mitverfolgen (tail)
journalctl --since "1 hour ago"
journalctl _PID=1234             # Nach Prozess-ID filtern
Logging-Strategien
Strukturiertes Logging
JSON-Format verwenden, damit Logs maschinell auswertbar sind:

python
import structlog
logger = structlog.get_logger()
logger.info("user_login", user_id=123, ip="192.168.1.1")
Log-Level
DEBUG: detaillierte Diagnose.

INFO: allgemeine Ereignisse (Start, Stopp, normale Transaktionen).

WARN: unerwartet, aber nicht fatal.

ERROR: Fehler, der eine bestimmte Operation verhindert.

FATAL/CRITICAL: Systemabschaltung.

Log-Aggregation
ELK Stack (Elasticsearch, Logstash, Kibana) oder Elastic Cloud.

Loki + Grafana (leichtgewichtige Alternative).

Datadog, Splunk, Sumo Logic (SaaS).

Log Rotation (logrotate)
Verhindert, dass Logs die Festplatten füllen. Konfiguriere /etc/logrotate.d/myapp:

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

Anwendung: Request-Rate, Latenz (p50, p95, p99), Fehlerrate, aktive Sessions.

Datenbank: Anzahl der Abfragen, langsame Abfragen, Nutzung des Connection Pools.

Business: Benutzeranmeldungen, Conversion Rate, Umsatz.

Werkzeuge
Prometheus + Grafana: Standard-Open-Source-Stack.

Node Exporter für Systemmetriken.

Blackbox Exporter für Endpunktverfügbarkeit.

Alertmanager für Alert-Routing.

Cloud-nativ: AWS CloudWatch, Azure Monitor, GCP Monitoring.

Uptime-Monitoring
Pingdom, Statuspage, Better Uptime, Uptime Kuma (self-hosted).

Health Checks: Einen `/health`-Endpunkt bereitstellen, der 200 zurückgibt, wenn der Service gesund ist.

Backup-Strategien
Die 3-2-1-Regel
3 Kopien der Daten.

2 verschiedene Medientypen (z. B. SSD + Band oder lokal + Cloud).

1 Kopie außerhalb des Standorts (z. B. Cloud oder entferntes Rechenzentrum).

Backup-Typen
Full Backup: alles kopieren (langsam, speicherintensiv).

Incremental Backup: nur Änderungen seit dem letzten Full oder Incremental kopieren (schnell, komplexe Wiederherstellung).

Differential Backup: Änderungen seit dem letzten Full kopieren (Mittelweg).

Datenbank-Backups
bash
# PostgreSQL
pg_dump dbname > backup.sql
pg_dumpall > all_backup.sql

# MySQL / MariaDB
mysqldump -u root -p dbname > backup.sql

# Wiederherstellen
psql dbname < backup.sql
mysql -u root -p dbname < backup.sql
Datei-Backups
bash
# Tar-Archiv
tar -czf backup.tar.gz /var/lib/data

# Rsync auf Remote-System
rsync -avz /local/data/ user@backup-server:/backup/data/

# Cloud-CLI (z. B. AWS S3)
aws s3 sync /local/data s3://my-bucket/backup/
Automatisierte Backup-Planung (cron)
cron
# Täglich um 2 Uhr ausführen
0 2 * * * /usr/local/bin/backup_script.sh
Cron und geplante Jobs
Cron-Syntax
text
* * * * * command
│ │ │ │ │
│ │ │ │ └─ Wochentag (0-7, 0=Sun)
│ │ │ └─── Monat (1-12)
│ │ └───── Tag des Monats (1-31)
│ └─────── Stunde (0-23)
└───────── Minute (0-59)
Beispiele
cron
# Alle 5 Minuten
*/5 * * * * /path/to/script

# Jeden Tag um 3:15 Uhr
15 3 * * * /path/to/script

# Jeden Montag um 4 Uhr
0 4 * * 1 /path/to/script

# Jede Stunde
0 * * * * /path/to/script
Cron verwalten
bash
crontab -l          # Cron-Jobs des aktuellen Benutzers auflisten
crontab -e          # Bearbeiten
crontab -r          # Alle entfernen
Anacron
Wird für Systeme verwendet, die nicht rund um die Uhr laufen (z. B. Laptops), und stellt sicher, dass Jobs schließlich ausgeführt werden.

Paketverwaltung und Updates
Debian/Ubuntu (apt)
bash
sudo apt update                # Paketliste aktualisieren
sudo apt upgrade               # Alle Pakete aktualisieren
sudo apt install git nginx
sudo apt remove git
sudo apt autoremove            # Nicht verwendete Abhängigkeiten entfernen
RHEL/CentOS/Fedora (dnf/yum)
bash
sudo dnf check-update
sudo dnf update
sudo dnf install git nginx
sudo dnf remove git
Sicherheitsupdates
Aktiviere unattended-upgrades auf Ubuntu für Sicherheitspatches:

bash
sudo apt install unattended-upgrades
sudo dpkg-reconfigure -plow unattended-upgrades
Docker im Produktionseinsatz
Best Practices
Spezifische Image-Tags verwenden (python:3.12-slim) statt latest.

Container als Non-Root-Benutzer ausführen.

Images auf Schwachstellen scannen (docker scan, trivy).

Ressourcenlimits setzen (--memory, --cpus).

Secrets verwenden (über Docker secrets oder vorsichtig über Environment).

Images klein halten: Multi-Stage-Builds, alpine base.

Docker Compose in Produktion
Ressourcenlimits in docker-compose.yml setzen:

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
Pipeline-Phasen
Build: Code kompilieren, Abhängigkeiten installieren.

Test: Unit-, Integrations- und Lint-Prüfungen ausführen.

Containerisieren: Docker-Image bauen.

Push: Image in die Container-Registry pushen.

Deploy: Staging-/Produktionsumgebung aktualisieren.

Werkzeuge
GitHub Actions: Mit GitHub integriert.

GitLab CI: In GitLab integriert.

Jenkins: Traditionell, hochgradig konfigurierbar.

CircleCI, Travis CI: Beliebte Drittanbieter.

ArgoCD: GitOps für Kubernetes.

Beispiel für eine GitHub Action (einfach):
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
Systemoptimierung und Fehlersuche
Festplattenspeicher prüfen
bash
df -h                      # Lesbare Festplattennutzung
du -sh /* | sort -h        # Größe der Verzeichnisse auf oberster Ebene
Speichernutzung prüfen
bash
free -m                    # Speicher in MB
vmstat 1 10                # Virtuelle Speicherstatistiken
top -o %MEM                # Prozesse nach Speicher sortieren
CPU-Last prüfen
bash
uptime                     # Load Average über 1,5,15 Minuten
top -o %CPU                # Prozesse nach CPU sortieren
mpstat -P ALL 1 5          # CPU-Nutzung pro Kern
Netzwerk prüfen
bash
netstat -i                 # Schnittstellenstatistiken
iftop                      # Live-Bandbreitennutzung (Installation erforderlich)
nload                      # Weiterer Bandbreitenmonitor
Große Dateien finden
bash
find / -type f -size +100M -exec ls -lh {} \; 2>/dev/null
Infrastructure as Code (IaC)
Terraform
Cloud-Ressourcen in HCL deklarieren.

hcl
provider "aws" {
  region = "us-east-1"
}
resource "aws_instance" "web" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t2.micro"
}
Ansible
Agentenloses Konfigurationsmanagement mit YAML.

yaml
- name: Install nginx
  hosts: webservers
  tasks:
    - name: Install nginx
      apt:
        name: nginx
        state: present
Best Practices
Module und Rollen für Wiederverwendbarkeit nutzen.

State remote speichern (S3, Terraform Cloud).

Variablen und Secrets verwenden (AWS_SECRET_ACCESS_KEY per Environment, nicht fest codiert).

IaC-Code versionieren.

Incident Response (On-call)
Checkliste für einen Dienstausfall
Den Alert bestätigen.

Umfang bewerten: Welche Services/Benutzer sind betroffen?

Das Problem identifizieren (Logs, Metriken, aktuelle Deployments ansehen).

Wenn möglich eindämmen (Circuit Breakers, Feature Flags).

Rollback durchführen oder vorwärts beheben.

Status an Stakeholder und Benutzer kommunizieren (Statusseite).

Den Zeitverlauf und die Maßnahmen des Incidents dokumentieren.

Post-Mortem: innerhalb von 24–48 Stunden eine Root Cause Analysis (RCA) und Maßnahmen verfassen, um eine Wiederholung zu verhindern.