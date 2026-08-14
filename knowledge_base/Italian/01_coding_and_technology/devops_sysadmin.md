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
# DevOps e amministrazione di sistema
Una guida pratica alla gestione dei server, all'automazione delle operazioni e al mantenimento dell'affidabilità dell'infrastruttura.
---

## SSH (Secure Shell)
### Generazione di chiavi
```bash
ssh-keygen -t ed25519 -C "your_email@example.com"   # Modern and secure
ssh-keygen -t rsa -b 4096 -C "your_email@example.com" # Fallback
```

### Copia la chiave pubblica sul server
```bash
ssh-copy-id user@host
# Manual alternative:
cat ~/.ssh/id_ed25519.pub | ssh user@host "mkdir -p ~/.ssh && cat >> ~/.ssh/authorized_keys"
```

### Configurazione SSH (`~/.ssh/config`)
```
Host myserver
    HostName 192.168.1.10
    User ubuntu
    IdentityFile ~/.ssh/mykey
    Port 2222
```

### Comandi SSH comuni
```bash
ssh user@host                              # Connect
ssh -J jumpuser@jumphost user@target       # Proxy jump
scp file.txt user@host:/path/              # Copy file to remote
scp user@host:/path/file.txt .             # Copy from remote
rsync -avz -e ssh ./local/ user@host:/remote/  # Efficient sync
```

### Rafforzamento di SSH
- Disabilita accesso root:`PermitRootLogin no`
- Utilizza solo l'autenticazione basata su chiave:`PasswordAuthentication no`
- Modifica la porta predefinita (opzionale, sicurezza attraverso l'oscurità).
- Abilita`AllowUsers`o`AllowGroups`per limitare l'accesso.
---

## Systemd (Gestione dei servizi Linux)
### Comandi comuni
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

### Creazione di un'unità di servizio systemd
Crea `/etc/systemd/system/myapp.service`:
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

Poi:
```bash
sudo systemctl daemon-reload
sudo systemctl enable myapp
sudo systemctl start myapp
```

---

## Journalctl (Visualizza registri)
```bash
journalctl -u myapp              # Logs for service
journalctl -f                    # Follow (tail) logs
journalctl --since "1 hour ago"
journalctl _PID=1234             # Filter by process ID
```

---

## Strategie di registrazione
### Registrazione strutturata
Utilizza il formato JSON per rendere i log analizzabili dal computer:
```python
import structlog
logger = structlog.get_logger()
logger.info("user_login", user_id=123, ip="192.168.1.1")
```

### Livelli di registro
| Livello | Scopo |
|-------|---------|
| **DEBUG** | Informazioni diagnostiche dettagliate |
| **INFO** | Eventi generali (inizio, fine, transazioni normali) |
| **ATTENZIONE** | Inaspettato ma non fatale |
| **ERRORE** | Errore che impedisce un'operazione specifica |
| **FATALE/CRITICO** | Arresto del sistema |
### Aggregazione dei registri
- **ELK Stack** (Elasticsearch, Logstash, Kibana) o Elastic Cloud.
- **Loki + Grafana** (alternativa leggera).
- **Datadog, Splunk, Sumo Logic** (SaaS).
### Rotazione registro (`logrotate`)
Evita che i log riempiano i dischi. Configura `/etc/logrotate.d/myapp`:
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

## Monitoraggio e avvisi
### Metriche da monitorare
| Categoria | Metriche chiave |
|----------|-------------|
| **Sistema** | CPU, RAM, utilizzo del disco, carico medio, I/O di rete |
| **Applicazione** | Tasso di richiesta, latenza (p50, p95, p99), tasso di errore, sessioni attive |
| **Banca dati** | Conteggio query, query lente, utilizzo del pool di connessioni |
| **Affari** | Iscrizioni degli utenti, tasso di conversione, entrate |
### Utensili
- **Prometheus + Grafana**: stack open source standard.
- **Esportatore di nodi** per le metriche di sistema.
- **Blackbox Exporter** per la disponibilità degli endpoint.
- **Alertmanager** per l'instradamento degli avvisi.
- **Nativo cloud**: AWS CloudWatch, Monitoraggio di Azure, Monitoraggio GCP.
### Monitoraggio del tempo di attività
- Pingdom, Statuspage, Better Uptime, Uptime Kuma (auto-ospitato).
- Controlli di integrità: esponi un endpoint`/health`che restituisce 200 se il servizio è integro.
---

## Strategie di backup
### La regola del 3-2-1
- **3** copie dei dati.
- **2** tipi di supporti diversi (ad esempio, SSD + nastro o locale + cloud).
- **1** copia off-site (ad esempio, cloud o data center remoto).
### Tipi di backup
| Digitare | Descrizione | Scambio |
|------|-------------|-----------|
| **Completo** | Copia tutto | Lento, pesante nello spazio |
| **Incrementale** | Copia solo le modifiche dall'ultimo | completo o incrementale Ripristino rapido e complesso |
| **Differenziale** | Copia le modifiche dall'ultimo completo | Terra di mezzo |
### Backup del database
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

### Backup dei file
```bash
# Tar archive
tar -czf backup.tar.gz /var/lib/data

# Rsync to remote
rsync -avz /local/data/ user@backup-server:/backup/data/

# Cloud CLI (e.g., AWS S3)
aws s3 sync /local/data s3://my-bucket/backup/
```

### Pianificazione backup automatizzata (cron)
```cron
# Run daily at 2am
0 2 * * * /usr/local/bin/backup_script.sh
```

---

## Cron e lavori pianificati
### Sintassi Cron
```
* * * * * command
│ │ │ │ │
│ │ │ │ └─ Day of week (0-7, 0=Sun)
│ │ │ └─── Month (1-12)
│ │ └───── Day of month (1-31)
│ └─────── Hour (0-23)
└───────── Minute (0-59)
```

### Esempi
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

### Gestione Cron
```bash
crontab -l          # List current user's cron jobs
crontab -e          # Edit
crontab -r          # Remove all
```

### Anacron
Utilizzato per sistemi non in funzione 24 ore su 24, 7 giorni su 7 (ad esempio laptop); garantisce che i lavori vengano eseguiti alla fine.
---

## Gestione e aggiornamenti dei pacchetti
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

### Aggiornamenti di sicurezza
Abilita`unattended-upgrades`su Ubuntu per le patch di sicurezza:
```bash
sudo apt install unattended-upgrades
sudo dpkg-reconfigure -plow unattended-upgrades
```

---

## Docker in produzione
### Migliori pratiche
- Utilizza tag immagine specifici (`python:3.12-slim`) e non`latest`.
- Esegui i contenitori come utente non root.
- Scansiona le immagini per individuare eventuali vulnerabilità (`docker scan`,`trivy`).
- Imposta i limiti delle risorse (`--memory`,`--cpus`).
- Utilizzare i segreti (tramite i segreti Docker o l'ambiente con cura).
- Mantieni le immagini piccole: build a più fasi, base alpina.
### Docker Compose in produzione
Imposta i limiti delle risorse in `docker-compose.yml`:
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

## Nozioni di base su CI/CD
### Fasi della pipeline
| Palcoscenico | Descrizione |
|-------|-------------|
| **Costruisci** | Compila il codice, installa le dipendenze |
| **Prova** | Esegui controlli di unità, integrazione e lanugine |
| **Contenire** | Costruisci immagine Docker |
| **Spingi** | Invia l'immagine al registro del contenitore |
| **Distribuisci** | Aggiornamento dell'ambiente di staging/produzione |
### Utensili
| Strumento | Note |
|------|-------|
| **Azioni GitHub** | Integrato con GitHub |
| **CI GitLab** | Integrato in GitLab |
| **Jenkins** | Tradizionale, altamente configurabile |
| **CircleCI, Travis CI** | Terze parti popolari |
| **ArgoCD** | GitOps per Kubernetes |
### Esempio di azione GitHub
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

## Ottimizzazione e risoluzione dei problemi del sistema
### Controlla lo spazio su disco
```bash
df -h                      # Human-readable disk usage
du -sh /* | sort -h        # Size of top-level directories
```

### Controlla l'utilizzo della memoria
```bash
free -m                    # Memory in MB
vmstat 1 10                # Virtual memory statistics
top -o %MEM                # Sort processes by memory
```

### Controlla il carico della CPU
```bash
uptime                     # Load average over 1,5,15 minutes
top -o %CPU                # Sort processes by CPU
mpstat -P ALL 1 5          # Per-core CPU usage
```

### Controlla la rete
```bash
netstat -i                 # Interface statistics
iftop                      # Live bandwidth usage (requires install)
nload                      # Another bandwidth monitor
```

### Trova file di grandi dimensioni
```bash
find / -type f -size +100M -exec ls -lh {} \; 2>/dev/null
```

---

## Infrastruttura come codice (IaC)
### Terraformare
Dichiarare le risorse cloud in HCL.
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
Gestione della configurazione senza agente tramite YAML.
```yaml
- name: Install nginx
  hosts: webservers
  tasks:
    - name: Install nginx
      apt:
        name: nginx
        state: present
```

### Migliori pratiche
- Utilizzare moduli e ruoli per la riusabilità.
- Archivia lo stato in remoto (S3, Terraform Cloud).
- Utilizza variabili e segreti (`AWS_SECRET_ACCESS_KEY` tramite ambiente, non hardcoded).
- Controlla la versione del tuo codice IaC.
---

## Risposta agli incidenti (su chiamata)
### Elenco di controllo per l'interruzione del servizio
1. Riconoscere l'avviso.
2. Valutare l'ambito: quali servizi/utenti sono interessati?
3. Identificare il problema (guardare log, parametri, distribuzioni recenti).
4. Contenere se possibile (interruttori automatici, indicatori di funzionalità).
5. Rollback o correzione in avanti.
6. Comunicare lo stato alle parti interessate e agli utenti (pagina stato).
7. Documentare la tempistica e le azioni dell'incidente.
8. Autopsia: entro 24-48 ore, scrivere un'analisi della causa principale (RCA) e azioni da intraprendere per prevenire il ripetersi.