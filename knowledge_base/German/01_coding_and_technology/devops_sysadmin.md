<!--
---
# Metadata
title: "DevOps and System Administration"
description: "SSH, systemd, logging, monitoring, backups, Docker, CI/CD"
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
tags: [devops, sysadmin, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "19 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# DevOps und Systemadministration
Ein praktischer Leitfaden zur Verwaltung von Servern, zur Automatisierung von Abläufen und zur Aufrechterhaltung einer zuverlässigen Infrastruktur.
---

## SSH (Secure Shell)
### Schlüsselgenerierung
```bash
ssh-keygen -t ed25519 -C "your_email@example.com"   # Modern and secure
ssh-keygen -t rsa -b 4096 -C "your_email@example.com" # Fallback
```

### Öffentlichen Schlüssel auf Server kopieren
```bash
ssh-copy-id user@host
# Manual alternative:
cat ~/.ssh/id_ed25519.pub | ssh user@host "mkdir -p ~/.ssh && cat >> ~/.ssh/authorized_keys"
```

### SSH-Konfiguration (`~/.ssh/config`)
```
Host myserver
    HostName 192.168.1.10
    User ubuntu
    IdentityFile ~/.ssh/mykey
    Port 2222
```

### Allgemeine SSH-Befehle
```bash
ssh user@host                              # Connect
ssh -J jumpuser@jumphost user@target       # Proxy jump
scp file.txt user@host:/path/              # Copy file to remote
scp user@host:/path/file.txt .             # Copy from remote
rsync -avz -e ssh ./local/ user@host:/remote/  # Efficient sync
```

### SSH härten
- Root-Login deaktivieren:`PermitRootLogin no`
– Nur schlüsselbasierte Authentifizierung verwenden:`PasswordAuthentication no`
- Standardport ändern (optional, Sicherheit durch Unklarheit).
- Aktivieren Sie`AllowUsers`oder `AllowGroups`, um den Zugriff einzuschränken.
---

## Systemd (Linux-Dienstverwaltung)
### Allgemeine Befehle
```bash
systemctl status nginx           # Check service status
systemctl start nginx            # Start service
systemctl stop nginx
systemctl restart nginx
systemctl reload nginx           # Graceful reload (re-read config)
systemctl enable nginx           # Start on boot
systemctl disable nginx
systemctl list-units --type=service --all   # List all services
systemctl daemon-reload          # Reload unit files after editing
```

### Erstellen einer systemd-Serviceeinheit
Erstellen Sie `/etc/systemd/system/myapp.service`:
```ini
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
```

Dann:
```bash
sudo systemctl daemon-reload
sudo systemctl enable myapp
sudo systemctl start myapp
```

---

## Journalctl (Protokolle anzeigen)
```bash
journalctl -u myapp              # Logs for service
journalctl -f                    # Follow (tail) logs
journalctl --since "1 hour ago"
journalctl _PID=1234             # Filter by process ID
```

---

## Protokollierungsstrategien
### Strukturierte Protokollierung
Verwenden Sie das JSON-Format, um Protokolle maschinenlesbar zu machen:
```python
import structlog
logger = structlog.get_logger()
logger.info("user_login", user_id=123, ip="192.168.1.1")
```

### Protokollebenen
| Ebene | Zweck |
|-------|---------|
| **DEBUG** | Detaillierte Diagnoseinformationen |
| **INFO** | Allgemeine Ereignisse (Start, Stopp, normale Transaktionen) |
| **WARNUNG** | Unerwartet, aber nicht tödlich |
| **FEHLER** | Fehler, der einen bestimmten Vorgang verhindert |
| **FATAL/KRITISCH** | Systemabschaltung |
### Protokollaggregation
- **ELK Stack** (Elasticsearch, Logstash, Kibana) oder Elastic Cloud.
- **Loki + Grafana** (leichte Alternative).
- **Datadog, Splunk, Sumo Logic** (SaaS).
### Protokollrotation (`logrotate`)
Verhindern Sie, dass Protokolle die Festplatten füllen. Konfigurieren Sie `/etc/logrotate.d/myapp`:
```
/var/log/myapp/*.log {
    daily
    rotate 7
    compress
    delaycompress
    missingok
    notifempty
    create 0640 myuser mygroup
}
```

---

## Überwachung und Alarmierung
### Zu überwachende Metriken
| Kategorie | Schlüsselkennzahlen |
|----------|-------------|
| **System** | CPU, RAM, Festplattennutzung, durchschnittliche Auslastung, Netzwerk-E/A |
| **Bewerbung** | Anforderungsrate, Latenz (p50, p95, p99), Fehlerrate, aktive Sitzungen |
| **Datenbank** | Anzahl der Abfragen, langsame Abfragen, Nutzung des Verbindungspools |
| **Geschäft** | Benutzeranmeldungen, Conversion-Rate, Umsatz |
### Werkzeuge
- **Prometheus + Grafana**: Standard-Open-Source-Stack.
- **Node Exporter** für Systemmetriken.
- **Blackbox Exporter** für Endpunktverfügbarkeit.
- **Alertmanager** für die Alarmweiterleitung.
- **Cloud-nativ**: AWS CloudWatch, Azure Monitor, GCP-Überwachung.
### Betriebszeitüberwachung
- Pingdom, Statuspage, Better Uptime, Uptime Kuma (selbst gehostet).
- Gesundheitsprüfungen: Stellen Sie einen `/health`-Endpunkt bereit, der 200 zurückgibt, wenn der Dienst fehlerfrei ist.
---

## Backup-Strategien
### Die 3-2-1-Regel
- **3** Kopien der Daten.
- **2** verschiedene Medientypen (z. B. SSD + Band oder lokal + Cloud).
- **1** Kopie außerhalb des Standorts (z. B. Cloud oder Remote-Rechenzentrum).
### Sicherungstypen
| Geben Sie | ein Beschreibung | Kompromiss |
|------|-------------|-----------|
| **Voll** | Alles kopieren | Langsam, raumlastig |
| **Inkrementell** | Nur Änderungen seit dem letzten vollständigen oder inkrementellen | kopieren Schnelle, komplexe Wiederherstellung |
| **Differenzial** | Änderungen seit dem letzten vollständigen | kopieren Mittelweg |
### Datenbanksicherungen
```bash
# PostgreSQL
pg_dump dbname > backup.sql
pg_dumpall > all_backup.sql

# MySQL / MariaDB
mysqldump -u root -p dbname > backup.sql

# Restore
psql dbname < backup.sql
mysql -u root -p dbname < backup.sql
```

### Dateisicherungen
```bash
# Tar archive
tar -czf backup.tar.gz /var/lib/data

# Rsync to remote
rsync -avz /local/data/ user@backup-server:/backup/data/

# Cloud CLI (e.g., AWS S3)
aws s3 sync /local/data s3://my-bucket/backup/
```

### Automatisierte Backup-Planung (cron)
```cron
# Run daily at 2am
0 2 * * * /usr/local/bin/backup_script.sh
```

---

## Cron und geplante Jobs
### Cron-Syntax
```
* * * * * command
│ │ │ │ │
│ │ │ │ └─ Day of week (0-7, 0=Sun)
│ │ │ └─── Month (1-12)
│ │ └───── Day of month (1-31)
│ └─────── Hour (0-23)
└───────── Minute (0-59)
```

### Beispiele
```cron
# Every 5 minutes
*/5 * * * * /path/to/script

# Every day at 3:15 AM
15 3 * * * /path/to/script

# Every Monday at 4 AM
0 4 * * 1 /path/to/script

# Every hour
0 * * * * /path/to/script
```

### Cron verwalten
```bash
crontab -l          # List current user's cron jobs
crontab -e          # Edit
crontab -r          # Remove all
```

### Anacron
Wird für Systeme verwendet, die nicht rund um die Uhr laufen (z. B. Laptops); stellt sicher, dass Jobs irgendwann ausgeführt werden.
---

## Paketverwaltung und Updates
### Debian/Ubuntu (`apt`)
```bash
sudo apt update                # Update package list
sudo apt upgrade               # Upgrade all packages
sudo apt install git nginx
sudo apt remove git
sudo apt autoremove            # Remove unused dependencies
```

### RHEL/CentOS/Fedora (`dnf`/`yum`)
```bash
sudo dnf check-update
sudo dnf update
sudo dnf install git nginx
sudo dnf remove git
```

### Sicherheitsupdates
Aktivieren Sie`unattended-upgrades`unter Ubuntu für Sicherheitspatches:
```bash
sudo apt install unattended-upgrades
sudo dpkg-reconfigure -plow unattended-upgrades
```

---

## Docker in der Produktion
### Best Practices
– Verwenden Sie bestimmte Bild-Tags (`python:3.12-slim`), nicht `latest`.
- Führen Sie Container als Nicht-Root-Benutzer aus.
- Scannen Sie Bilder auf Schwachstellen (`docker scan`,`trivy`).
- Legen Sie Ressourcenlimits fest (`--memory`,`--cpus`).
- Verwenden Sie Geheimnisse (über Docker-Geheimnisse oder die Umgebung mit Vorsicht).
- Halten Sie die Bilder klein: mehrstufige Aufbauten, alpine Basis.
### Docker Compose in der Produktion
Legen Sie Ressourcenlimits in`docker-compose.yml`fest:
```yaml
services:
  app:
    image: myapp:1.0
    deploy:
      resources:
        limits:
          memory: 512M
          cpus: '0.5'
```

---

## CI/CD-Grundlagen
### Pipeline-Stufen
| Bühne | Beschreibung |
|-------|-------------|
| **Bauen** | Code kompilieren, Abhängigkeiten installieren |
| **Test** | Führen Sie Einheiten-, Integrations- und Flusenprüfungen durch |
| **Containerisieren** | Docker-Image erstellen |
| **Drücken** | Bild in die Container-Registrierung übertragen |
| **Bereitstellen** | Staging-/Produktionsumgebung aktualisieren |
### Werkzeuge
| Werkzeug | Notizen |
|------|-------|
| **GitHub-Aktionen** | Integriert mit GitHub |
| **GitLab CI** | In GitLab integriert |
| **Jenkins** | Traditionell, hochgradig konfigurierbar |
| **CircleCI, Travis CI** | Beliebte Drittanbieter |
| **ArgoCD** | GitOps für Kubernetes |
### Beispiel einer GitHub-Aktion
```yaml
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
```

---

## Systemoptimierung und Fehlerbehebung
### Überprüfen Sie den Speicherplatz
```bash
df -h                      # Human-readable disk usage
du -sh /* | sort -h        # Size of top-level directories
```

### Überprüfen Sie die Speichernutzung
```bash
free -m                    # Memory in MB
vmstat 1 10                # Virtual memory statistics
top -o %MEM                # Sort processes by memory
```

### CPU-Auslastung prüfen
```bash
uptime                     # Load average over 1,5,15 minutes
top -o %CPU                # Sort processes by CPU
mpstat -P ALL 1 5          # Per-core CPU usage
```

### Überprüfen Sie das Netzwerk
```bash
netstat -i                 # Interface statistics
iftop                      # Live bandwidth usage (requires install)
nload                      # Another bandwidth monitor
```

### Große Dateien finden
```bash
find / -type f -size +100M -exec ls -lh {} \; 2>/dev/null
```

---

## Infrastruktur als Code (IaC)
### Terraform
Deklarieren Sie Cloud-Ressourcen in HCL.
```hcl
provider "aws" {
  region = "us-east-1"
}
resource "aws_instance" "web" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t2.micro"
}
```

### Ansible
Agentenloses Konfigurationsmanagement mit YAML.
```yaml
- name: Install nginx
  hosts: webservers
  tasks:
    - name: Install nginx
      apt:
        name: nginx
        state: present
```

### Best Practices
- Nutzen Sie Module und Rollen zur Wiederverwendbarkeit.
- Status aus der Ferne speichern (S3, Terraform Cloud).
- Verwenden Sie Variablen und Geheimnisse (`AWS_SECRET_ACCESS_KEY`über die Umgebung, nicht fest codiert).
- Versionskontrolle Ihres IaC-Codes.
---

## Reaktion auf Vorfälle (Bereitschaftsbereitschaft)
### Checkliste für Serviceausfälle
1. Bestätigen Sie die Warnung.
2. Umfang beurteilen: Welche Dienste/Benutzer sind betroffen?
3. Identifizieren Sie das Problem (sehen Sie sich Protokolle, Metriken und aktuelle Bereitstellungen an).
4. Wenn möglich eindämmen (Leistungsschalter, Funktionsflags).
5. Rollback oder Fix Forward.
6. Kommunizieren Sie den Status an Stakeholder und Benutzer (Statusseite).
7. Dokumentieren Sie den Zeitplan und die Maßnahmen des Vorfalls.
8. Obduktion: Schreiben Sie innerhalb von 24–48 Stunden eine Ursachenanalyse (RCA) und Maßnahmen, um ein erneutes Auftreten zu verhindern.