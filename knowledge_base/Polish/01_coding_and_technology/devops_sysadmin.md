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
# DevOps i administracja systemem
Praktyczny przewodnik po zarządzaniu serwerami, automatyzacji operacji i utrzymywaniu niezawodnej infrastruktury.
---

## SSH (bezpieczna powłoka)
### Generowanie klucza
```bash
ssh-keygen -t ed25519 -C "your_email@example.com"   # Modern and secure
ssh-keygen -t rsa -b 4096 -C "your_email@example.com" # Fallback
```

### Skopiuj klucz publiczny na serwer
```bash
ssh-copy-id user@host
# Manual alternative:
cat ~/.ssh/id_ed25519.pub | ssh user@host "mkdir -p ~/.ssh && cat >> ~/.ssh/authorized_keys"
```

### Konfiguracja SSH (`~/.ssh/config`)
```
Host myserver
    HostName 192.168.1.10
    User ubuntu
    IdentityFile ~/.ssh/mykey
    Port 2222
```

### Typowe polecenia SSH
```bash
ssh user@host                              # Connect
ssh -J jumpuser@jumphost user@target       # Proxy jump
scp file.txt user@host:/path/              # Copy file to remote
scp user@host:/path/file.txt .             # Copy from remote
rsync -avz -e ssh ./local/ user@host:/remote/  # Efficient sync
```

### Utwardzanie SSH
- Wyłącz logowanie roota:`PermitRootLogin no`
- Używaj tylko uwierzytelniania na podstawie klucza:`PasswordAuthentication no`
- Zmień domyślny port (opcjonalnie, bezpieczeństwo poprzez zaciemnienie).
- Włącz`AllowUsers`lub `AllowGroups`, aby ograniczyć dostęp.
---

## Systemd (zarządzanie usługami Linux)
### Typowe polecenia
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

### Tworzenie systemowej jednostki serwisowej
Utwórz`/etc/systemd/system/myapp.service`:
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

Następnie:
```bash
sudo systemctl daemon-reload
sudo systemctl enable myapp
sudo systemctl start myapp
```

---

## Journalctl (wyświetl logi)
```bash
journalctl -u myapp              # Logs for service
journalctl -f                    # Follow (tail) logs
journalctl --since "1 hour ago"
journalctl _PID=1234             # Filter by process ID
```

---

## Strategie rejestrowania
### Rejestrowanie strukturalne
Użyj formatu JSON, aby umożliwić analizę maszynową dzienników:
```python
import structlog
logger = structlog.get_logger()
logger.info("user_login", user_id=123, ip="192.168.1.1")
```

### Poziomy dziennika
| Poziom | Cel |
|-------|-------------|
| **DEBUGOWANIE** | Szczegółowe informacje diagnostyczne |
| **INFO** | Zdarzenia ogólne (start, stop, normalne transakcje) |
| **UWAGA** | Nieoczekiwane, ale nie śmiertelne |
| **BŁĄD** | Błąd uniemożliwiający wykonanie określonej operacji |
| **FATALNY/KRYTYCZNY** | Zamknięcie systemu |
### Agregacja logów
- **ELK Stack** (Elasticsearch, Logstash, Kibana) lub Elastic Cloud.
- **Loki + Grafana** (lekka alternatywa).
- **Datadog, Splunk, Sumo Logic** (SaaS).
### Rotacja dziennika (`logrotate`)
Zapobiegaj zapełnianiu dysków przez dzienniki. Skonfiguruj `/etc/logrotate.d/myapp`:
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

## Monitorowanie i ostrzeganie
### Wskaźniki do monitorowania
| Kategoria | Kluczowe wskaźniki |
|--------------|------------|
| **System** | Procesor, pamięć RAM, wykorzystanie dysku, średnie obciążenie, we/wy sieci |
| **Aplikacja** | Częstotliwość żądań, opóźnienie (p50, p95, p99), stopa błędów, aktywne sesje |
| **Baza danych** | Liczba zapytań, powolne zapytania, wykorzystanie puli połączeń |
| **Biznes** | Rejestracje użytkowników, współczynnik konwersji, przychody |
### Narzędzia
- **Prometheus + Grafana**: Standardowy stos open source.
- **Eksporter węzłów** dla wskaźników systemowych.
- **Eksporter Blackbox** w celu sprawdzenia dostępności punktów końcowych.
- **Alertmanager** do kierowania alertów.
- **Natywny w chmurze**: AWS CloudWatch, Azure Monitor, monitorowanie GCP.
### Monitorowanie czasu działania
- Pingdom, strona stanu, lepszy czas pracy, czas pracy Kuma (samodzielnie hostowany).
- Kontrole kondycji: ujawniają punkt końcowy `/health`, który zwraca 200, jeśli usługa jest w dobrej kondycji.
---

## Strategie tworzenia kopii zapasowych
### Zasada 3-2-1
- **3** kopie danych.
- **2** różne typy nośników (np. dysk SSD + taśma lub lokalny + chmura).
- **1** kopia poza siedzibą firmy (np. w chmurze lub zdalnym centrum danych).
### Typy kopii zapasowych
| Wpisz | Opis | Kompromis |
|------|------------|---------------|
| **Pełny** | Skopiuj wszystko | Powolny, kosmiczny |
| **Przyrostowy** | Kopiuj tylko zmiany od ostatniej pełnej lub przyrostowej | Szybkie, kompleksowe przywracanie |
| **Różnicowy** | Skopiuj zmiany od ostatniego pełnego | Środek |
### Kopie zapasowe baz danych
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

### Kopie zapasowe plików
```bash
# Tar archive
tar -czf backup.tar.gz /var/lib/data

# Rsync to remote
rsync -avz /local/data/ user@backup-server:/backup/data/

# Cloud CLI (e.g., AWS S3)
aws s3 sync /local/data s3://my-bucket/backup/
```

### Automatyczne planowanie kopii zapasowych (cron)
```cron
# Run daily at 2am
0 2 * * * /usr/local/bin/backup_script.sh
```

---

## Cron i zaplanowane zadania
### Składnia Crona
```
* * * * * command
│ │ │ │ │
│ │ │ │ └─ Day of week (0-7, 0=Sun)
│ │ │ └─── Month (1-12)
│ │ └───── Day of month (1-31)
│ └─────── Hour (0-23)
└───────── Minute (0-59)
```

### Przykłady
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

### Zarządzanie Cronem
```bash
crontab -l          # List current user's cron jobs
crontab -e          # Edit
crontab -r          # Remove all
```

### Anakron
Używany w systemach, które nie działają 24 godziny na dobę, 7 dni w tygodniu (np. laptopy); zapewnia ostateczne uruchomienie zadań.
---

## Zarządzanie pakietami i aktualizacje
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

### Aktualizacje zabezpieczeń
Włącz`unattended-upgrades`w systemie Ubuntu, aby uzyskać poprawki zabezpieczeń:
```bash
sudo apt install unattended-upgrades
sudo dpkg-reconfigure -plow unattended-upgrades
```

---

## Doker w produkcji
### Najlepsze praktyki
- Użyj określonych tagów graficznych (`python:3.12-slim`), a nie`latest`.
- Uruchamiaj kontenery jako użytkownik inny niż root.
- Skanuj obrazy w poszukiwaniu luk (`docker scan`,`trivy`).
- Ustaw limity zasobów (`--memory`,`--cpus`).
- Ostrożnie używaj sekretów (przez sekrety Dockera lub środowisko).
- Staraj się, aby obrazy były małe: wieloetapowe kompilacje, baza alpejska.
### Docker Compose w fazie produkcyjnej
Ustaw limity zasobów w `docker-compose.yml`:
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

## Podstawy CI/CD
### Etapy rurociągu
| Scena | Opis |
|-------|------------|
| **Buduj** | Skompiluj kod, zainstaluj zależności |
| **Test** | Uruchom sprawdzanie jednostek, integracji i lint |
| **Konteneruj** | Zbuduj obraz Dockera |
| **Pchnij** | Wypchnij obraz do rejestru kontenerów |
| **Wdrożenie** | Zaktualizuj środowisko testowe/produkcyjne |
### Narzędzia
| Narzędzie | Notatki |
|------|-------|
| **Działania na GitHubie** | Zintegrowany z GitHubem |
| **GitLab CI** | Wbudowany w GitLab |
| **Jenkins** | Tradycyjne, wysoce konfigurowalne |
| **CircleCI, Travis CI** | Popularne strony trzecie |
| **ArgoCD** | GitOps dla Kubernetesa |
### Przykładowa akcja GitHub
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

## Strojenie systemu i rozwiązywanie problemów
### Sprawdź miejsce na dysku
```bash
df -h                      # Human-readable disk usage
du -sh /* | sort -h        # Size of top-level directories
```

### Sprawdź użycie pamięci
```bash
free -m                    # Memory in MB
vmstat 1 10                # Virtual memory statistics
top -o %MEM                # Sort processes by memory
```

### Sprawdź obciążenie procesora
```bash
uptime                     # Load average over 1,5,15 minutes
top -o %CPU                # Sort processes by CPU
mpstat -P ALL 1 5          # Per-core CPU usage
```

### Sprawdź sieć
```bash
netstat -i                 # Interface statistics
iftop                      # Live bandwidth usage (requires install)
nload                      # Another bandwidth monitor
```

### Znajdź duże pliki
```bash
find / -type f -size +100M -exec ls -lh {} \; 2>/dev/null
```

---

## Infrastruktura jako kod (IaC)
### Terraforma
Zadeklaruj zasoby chmury w HCL.
```hcl
provider "aws" {
  region = "us-east-1"
}
resource "aws_instance" "web" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t2.micro"
}
```

###Ansible
Bezagentowe zarządzanie konfiguracją przy użyciu YAML.
```yaml
- name: Install nginx
  hosts: webservers
  tasks:
    - name: Install nginx
      apt:
        name: nginx
        state: present
```

### Najlepsze praktyki
- Używaj modułów i ról do ponownego użycia.
- Zdalny stan sklepu (S3, Terraform Cloud).
- Używaj zmiennych i sekretów (`AWS_SECRET_ACCESS_KEY`poprzez środowisko, a nie zakodowane na stałe).
- Kontrola wersji Twojego kodu IaC.
---

## Reagowanie na incydenty (na wezwanie)
### Lista kontrolna w przypadku awarii usługi
1. Potwierdź alert.
2. Oceń zakres: jakich usług/użytkowników dotyczy problem?
3. Zidentyfikuj problem (przejrzyj logi, metryki, ostatnie wdrożenia).
4. Jeśli to możliwe, uwzględnij (wyłączniki automatyczne, flagi funkcyjne).
5. Cofnij lub napraw do przodu.
6. Przekaż status zainteresowanym stronom i użytkownikom (strona statusu).
7. Udokumentuj harmonogram zdarzenia i działania.
8. Sekcja zwłok: w ciągu 24–48 godzin sporządź analizę pierwotnej przyczyny (RCA) i określ działania, aby zapobiec nawrotom.