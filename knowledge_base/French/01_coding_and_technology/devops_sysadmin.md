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
# DevOps et administration système
Un guide pratique pour gérer les serveurs, automatiser les opérations et maintenir une infrastructure fiable.
---

## SSH (shell sécurisé)
### Génération de clé
```bash
ssh-keygen -t ed25519 -C "your_email@example.com"   # Modern and secure
ssh-keygen -t rsa -b 4096 -C "your_email@example.com" # Fallback
```

### Copier la clé publique sur le serveur
```bash
ssh-copy-id user@host
# Manual alternative:
cat ~/.ssh/id_ed25519.pub | ssh user@host "mkdir -p ~/.ssh && cat >> ~/.ssh/authorized_keys"
```

### Configuration SSH (`~/.ssh/config`)
```
Host myserver
    HostName 192.168.1.10
    User ubuntu
    IdentityFile ~/.ssh/mykey
    Port 2222
```

### Commandes SSH courantes
```bash
ssh user@host                              # Connect
ssh -J jumpuser@jumphost user@target       # Proxy jump
scp file.txt user@host:/path/              # Copy file to remote
scp user@host:/path/file.txt .             # Copy from remote
rsync -avz -e ssh ./local/ user@host:/remote/  # Efficient sync
```

### Renforcement de SSH
- Désactiver la connexion root :`PermitRootLogin no`
- Utiliser uniquement l'authentification par clé :`PasswordAuthentication no`
- Changer le port par défaut (facultatif, sécurité par obscurité).
- Activez`AllowUsers`ou`AllowGroups`pour restreindre l'accès.
---

## Systemd (gestion des services Linux)
### Commandes communes
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

### Création d'une unité de service systemd
Créez `/etc/systemd/system/myapp.service` :
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

Alors:
```bash
sudo systemctl daemon-reload
sudo systemctl enable myapp
sudo systemctl start myapp
```

---

## Journalctl (Afficher les journaux)
```bash
journalctl -u myapp              # Logs for service
journalctl -f                    # Follow (tail) logs
journalctl --since "1 hour ago"
journalctl _PID=1234             # Filter by process ID
```

---

## Stratégies de journalisation
### Journalisation structurée
Utilisez le format JSON pour rendre les journaux analysables par machine :
```python
import structlog
logger = structlog.get_logger()
logger.info("user_login", user_id=123, ip="192.168.1.1")
```

### Niveaux de journalisation
| Niveau | Objectif |
|-------|--------------|
| **DÉBOGAGE** | Informations de diagnostic détaillées |
| **INFOS** | Événements généraux (démarrage, arrêt, transactions normales) |
| **AVERTIR** | Inattendu mais pas fatal |
| **ERREUR** | Erreur qui empêche une opération spécifique |
| **FATAL/CRITIQUE** | Arrêt du système |
### Agrégation de journaux
- **ELK Stack** (Elasticsearch, Logstash, Kibana) ou Elastic Cloud.
- **Loki + Grafana** (alternative légère).
- **Datadog, Splunk, Sumo Logic** (SaaS).
### Rotation des journaux (`logrotate`)
Empêchez les journaux de remplir les disques. Configurez `/etc/logrotate.d/myapp` :
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

## Surveillance et alerte
### Métriques à surveiller
| Catégorie | Indicateurs clés |
|--------------|-------------|
| **Système** | CPU, RAM, utilisation du disque, charge moyenne, E/S réseau |
| **Candidature** | Taux de requêtes, latence (p50, p95, p99), taux d'erreur, sessions actives |
| **Base de données** | Nombre de requêtes, requêtes lentes, utilisation du pool de connexions |
| **Entreprise** | Inscriptions des utilisateurs, taux de conversion, revenus |
### Outils
- **Prometheus + Grafana** : pile open source standard.
- **Node Exporter** pour les métriques du système.
- **Blackbox Exporter** pour la disponibilité des points de terminaison.
- **Alertmanager** pour le routage des alertes.
- **Cloud natif** : AWS CloudWatch, Azure Monitor, GCP Monitoring.
### Surveillance de la disponibilité
- Pingdom, Statuspage, Better Uptime, Uptime Kuma (auto-hébergé).
- Contrôles de santé : exposez un point de terminaison`/health`qui renvoie 200 si le service est sain.
---

## Stratégies de sauvegarde
### La règle 3-2-1
- **3** copies de données.
- **2** types de supports différents (par exemple, SSD + bande ou local + cloud).
- **1** copie hors site (par exemple, cloud ou centre de données distant).
### Types de sauvegarde
| Tapez | Descriptif | Compromis |
|------|-------------|---------------|
| **Complet** | Copiez tout | Lent et lourd |
| **Incrémentiel** | Copier uniquement les modifications depuis la dernière version complète ou incrémentielle | Restauration rapide et complexe |
| **Différentiel** | Copier les modifications depuis la dernière version complète | Terrain d'entente |
### Sauvegardes de base de données
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

### Sauvegardes de fichiers
```bash
# Tar archive
tar -czf backup.tar.gz /var/lib/data

# Rsync to remote
rsync -avz /local/data/ user@backup-server:/backup/data/

# Cloud CLI (e.g., AWS S3)
aws s3 sync /local/data s3://my-bucket/backup/
```

### Planification automatisée des sauvegardes (cron)
```cron
# Run daily at 2am
0 2 * * * /usr/local/bin/backup_script.sh
```

---

## Cron et tâches planifiées
### Syntaxe Cron
```
* * * * * command
│ │ │ │ │
│ │ │ │ └─ Day of week (0-7, 0=Sun)
│ │ │ └─── Month (1-12)
│ │ └───── Day of month (1-31)
│ └─────── Hour (0-23)
└───────── Minute (0-59)
```

### Exemples
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

### Gestion de Cron
```bash
crontab -l          # List current user's cron jobs
crontab -e          # Edit
crontab -r          # Remove all
```

###Anacron
Utilisé pour les systèmes qui ne fonctionnent pas 24h/24 et 7j/7 (par exemple, les ordinateurs portables) ; garantit que les travaux finissent par s'exécuter.
---

## Gestion des packages et mises à jour
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

### Mises à jour de sécurité
Activez`unattended-upgrades`sur Ubuntu pour les correctifs de sécurité :
```bash
sudo apt install unattended-upgrades
sudo dpkg-reconfigure -plow unattended-upgrades
```

---

## Docker en production
### Bonnes pratiques
- Utilisez des balises d'image spécifiques (`python:3.12-slim`) et non`latest`.
- Exécutez les conteneurs en tant qu'utilisateur non root.
- Analyser les images à la recherche de vulnérabilités (`docker scan`,`trivy`).
- Fixer des limites de ressources (`--memory`,`--cpus`).
- Utiliser les secrets (via Docker secrets ou environnement avec précaution).
- Gardez les images petites : constructions en plusieurs étapes, base alpine.
### Docker Compose en production
Définissez les limites de ressources dans `docker-compose.yml` :
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

## Notions de base sur CI/CD
### Étapes du pipeline
| Scène | Descriptif |
|-------|-------------|
| **Construire** | Compiler le code, installer les dépendances |
| **Tester** | Exécuter des vérifications d'unité, d'intégration et de charpie |
| **Conteneriser** | Créer une image Docker |
| **Pousser** | Transférer l'image vers le registre de conteneurs |
| **Déployer** | Mettre à jour l'environnement de préparation/production |
### Outils
| Outil | Remarques |
|------|-------|
| **Actions GitHub** | Intégré à GitHub |
| **GitLabCI** | Intégré à GitLab |
| **Jenkins** | Traditionnel, hautement configurable |
| **CercleCI, Travis CI** | Tiers populaire |
| **ArgoCD** | GitOps pour Kubernetes |
### Exemple d'action GitHub
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

## Réglage et dépannage du système
### Vérifier l'espace disque
```bash
df -h                      # Human-readable disk usage
du -sh /* | sort -h        # Size of top-level directories
```

### Vérifier l'utilisation de la mémoire
```bash
free -m                    # Memory in MB
vmstat 1 10                # Virtual memory statistics
top -o %MEM                # Sort processes by memory
```

### Vérifier la charge du processeur
```bash
uptime                     # Load average over 1,5,15 minutes
top -o %CPU                # Sort processes by CPU
mpstat -P ALL 1 5          # Per-core CPU usage
```

### Vérifier le réseau
```bash
netstat -i                 # Interface statistics
iftop                      # Live bandwidth usage (requires install)
nload                      # Another bandwidth monitor
```

### Rechercher des fichiers volumineux
```bash
find / -type f -size +100M -exec ls -lh {} \; 2>/dev/null
```

---

## Infrastructure en tant que code (IaC)
### Terraforme
Déclarez les ressources cloud dans HCL.
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
Gestion de configuration sans agent à l'aide de YAML.
```yaml
- name: Install nginx
  hosts: webservers
  tasks:
    - name: Install nginx
      apt:
        name: nginx
        state: present
```

### Bonnes pratiques
- Utiliser des modules et des rôles pour la réutilisabilité.
- Stocker l'état à distance (S3, Terraform Cloud).
- Utiliser des variables et des secrets (`AWS_SECRET_ACCESS_KEY`via l'environnement, non codés en dur).
- Contrôlez la version de votre code IaC.
---

## Réponse aux incidents (sur appel)
### Liste de contrôle en cas de panne de service
1. Accusez réception de l'alerte.
2. Évaluez la portée : quels services/utilisateurs sont concernés ?
3. Identifiez le problème (consultez les journaux, les métriques et les déploiements récents).
4. Contenir si possible (disjoncteurs, drapeaux de fonctionnalités).
5. Restaurer ou corriger.
6. Communiquer le statut aux parties prenantes et aux utilisateurs (page de statut).
7. Documentez le calendrier et les actions de l'incident.
8. Post-mortem : dans les 24 à 48 heures, rédigez une analyse des causes profondes (RCA) et des mesures à prendre pour éviter toute récidive.