# Bases du réseau

Une référence pratique pour les développeurs et les administrateurs système — concepts fondamentaux, protocoles, commandes et dépannage.

---

## Le modèle OSI (7 couches)

Un cadre conceptuel pour comprendre la communication réseau.

| Layer | Name | Function | Example protocols |
|-------|------|----------|-------------------|
| 7 | Application | Services destinés à l'utilisateur final | HTTP, HTTPS, FTP, SMTP, DNS, SSH |
| 6 | Presentation | Formatage des données, chiffrement, compression | TLS, JPEG, ASCII |
| 5 | Session | Gestion des connexions | NetBIOS, RPC |
| 4 | Transport | Livraison de bout en bout, correction d'erreurs, contrôle de flux | TCP, UDP |
| 3 | Network | Routage, adressage | IP, ICMP, OSPF, BGP |
| 2 | Data Link | Tramage, détection d'erreurs, adresses MAC | Ethernet, Wi-Fi, PPP |
| 1 | Physical | Transmission brute des bits | Câbles Ethernet, fibre optique, ondes radio |

En pratique, le **modèle TCP/IP** (4 couches : Link, Internet, Transport, Application) est plus couramment utilisé pour internet.

---

## Adressage IP

### IPv4
- Adresse sur 32 bits, écrite sous forme de quatre octets : `192.168.1.1`
- Total : ~4,3 milliards d'adresses (mais épuisées en pratique).

### IPv6
- Adresse sur 128 bits, écrite en hexadécimal : `2001:0db8:85a3:0000:0000:8a2e:0370:7334`
- Total : 2¹²⁸ adresses (pratiquement infini).

### Plages d'IP privées (RFC 1918)
Elles ne sont pas routables sur internet ; elles sont utilisées dans les réseaux locaux :
- `10.0.0.0/8` (10.0.0.0 – 10.255.255.255)
- `172.16.0.0/12` (172.16.0.0 – 172.31.255.255)
- `192.168.0.0/16` (192.168.0.0 – 192.168.255.255)

### Notation CIDR
`192.168.1.0/24` signifie que les 24 premiers bits sont le préfixe réseau ; les 8 derniers bits représentent les hôtes. Cela inclut les adresses `192.168.1.0` à `192.168.1.255`.

---

## DNS (Domain Name System)

Associe les noms de domaine (ex. `example.com`) à des adresses IP.

### Types d'enregistrements
| Type | Purpose |
|------|---------|
| **A** | Associe un domaine à une adresse IPv4 |
| **AAAA** | Associe un domaine à une adresse IPv6 |
| **CNAME** | Alias vers un autre nom de domaine |
| **MX** | Serveur de messagerie |
| **TXT** | Texte arbitraire (SPF, DKIM, vérification) |
| **NS** | Serveur de noms du domaine |
| **SRV** | Enregistrement de service (ex. pour SIP) |

### Outils courants
```bash
dig example.com            # Recherche DNS (détaillée)
nslookup example.com       # Recherche DNS (plus simple)
host example.com           # Recherche rapide
dig -x 8.8.8.8             # Recherche inverse (IP vers nom)

Ports et protocoles
Ports bien connus (0–1023)
Port	Protocol	Service
20, 21	TCP	FTP
22	TCP	SSH
23	TCP	Telnet
25	TCP	SMTP
53	UDP/TCP	DNS
80	TCP	HTTP
110	TCP	POP3
123	UDP	NTP
143	TCP	IMAP
443	TCP	HTTPS
465	TCP	SMTPS
587	TCP	SMTP (submission)
993	TCP	IMAPS
995	TCP	POP3S
3306	TCP	MySQL
5432	TCP	PostgreSQL
6379	TCP	Redis
27017	TCP	MongoDB
Vérifier les ports ouverts
bash
ss -tulpn                 # Linux : sockets en écoute et établies
netstat -an               # Outil plus ancien
lsof -i :8080             # Voir le processus utilisant le port 8080
nmap localhost            # Scanner les ports locaux
TCP vs UDP
Feature	TCP	UDP
Connection	Orienté connexion (handshake)	Sans connexion
Reliability	Livraison garantie, retransmission	Best effort (des paquets peuvent être perdus)
Ordering	Préserve l'ordre	Aucune garantie d'ordre
Flow control	Oui (fenêtre glissante)	Non
Use cases	Web (HTTP), e-mail, SSH, transfert de fichiers	DNS, streaming, VoIP, gaming, SNMP
Header size	20–60 bytes	8 bytes
HTTP et HTTPS
Méthodes HTTP
GET: Récupérer une ressource (idempotent, safe).

POST: Soumettre des données (non idempotent).

PUT: Mettre à jour/remplacer une ressource (idempotent).

PATCH: Mise à jour partielle.

DELETE: Supprimer une ressource (idempotent).

Codes de statut
1xx: Informations (100 Continue).

2xx: Succès (200 OK, 201 Created, 204 No Content).

3xx: Redirection (301 Moved Permanently, 302 Found, 304 Not Modified).

4xx: Erreur client (400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found, 429 Too Many Requests).

5xx: Erreur serveur (500 Internal Server Error, 502 Bad Gateway, 503 Service Unavailable).

Headers
Content-Type: type de média (application/json, text/html).

Authorization: identifiants (ex. ******

Cache-Control: politique de cache.

En-têtes CORS : Access-Control-Allow-Origin, etc.

TLS/SSL
Chiffre le trafic HTTP (HTTPS = HTTP sur TLS).

Les certificats délivrés par les autorités de certification (CA) authentifient le serveur.

Vérifiez la chaîne de certificats et le hostname côté client.

Pare-feu et NAT
Firewall
Filtre le trafic selon des règles (IP source, IP dest, port, protocole).

Les pare-feu à états suivent l'état des connexions.

NAT (Network Address Translation)
Traduit des IP privées vers une IP publique pour l'accès à internet.

Port forwarding : associe un port public à un hôte/port interne.

Commandes réseau courantes
Tests de connectivité
bash
ping google.com            # requête ICMP echo
ping -c 4 8.8.8.8          # ping 4 fois
traceroute google.com      # Tracer la route (Linux)
tracert google.com         # Version Windows
Routage
bash
ip route show              # Linux : table de routage
route -n                   # Ancien Linux
netstat -r                 # Windows/Mac
Interfaces réseau
bash
ip addr show               # Lister les interfaces et les IP
ifconfig                   # Commande plus ancienne
DNS
bash
dig example.com
nslookup example.com
host example.com
Connectivité vers un port
bash
nc -zv google.com 443      # Netcat : vérifier si le port 443 est ouvert
telnet google.com 443      # Telnet vers le port
curl -v https://google.com # Sortie verbeuse
Pare-feu (Linux iptables/nftables)
bash
sudo ufw status            # Ubuntu : pare-feu simple
sudo iptables -L -n        # Lister les règles
Statistiques réseau
bash
ss -tulpn                  # Afficher les sockets en écoute (Linux)
netstat -an                # Tous les sockets (tous OS)
Subnetting (référence rapide)
CIDR	Netmask	Number of addresses	Usable hosts
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
Load Balancing and Reverse Proxies
Nginx comme reverse proxy
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
Algorithmes de répartition de charge
Round-robin

Least connections

IP hash (persistance de session)

Weighted round-robin

Outils
Nginx, HAProxy (logiciels)

AWS ELB, Azure Load Balancer, GCP Cloud Load Balancing (cloud)

Checklist de dépannage
Le lien physique est-il actif ? (Vérifiez les câbles, la connexion Wi-Fi).

Pouvez-vous joindre la passerelle en ping ? (ex. ping 192.168.1.1).

Pouvez-vous joindre une IP externe en ping ? (ex. 8.8.8.8).

Pouvez-vous résoudre un domaine ? (dig google.com).

L'application écoute-t-elle sur le port attendu ? (ss -tulpn | grep 8080).

Le pare-feu bloque-t-il le port ? (Vérifiez iptables/ufw ou les security groups cloud).

Y a-t-il des erreurs dans les logs de l'application ?

Le certificat TLS est-il valide et approuvé ? (openssl s_client -connect example.com:443).

text

---

## File 6: `devops_sysadmin.md`

```markdown
# DevOps et administration système

Un guide pratique pour gérer des serveurs, automatiser les opérations et maintenir une infrastructure fiable.

---

## SSH (Secure Shell)

### Génération de clés
```bash
ssh-keygen -t ed25519 -C "your_email@example.com"   # Moderne et sécurisé
ssh-keygen -t rsa -b 4096 -C "your_email@example.com" # Solution de repli
Copier la clé publique vers le serveur
bash
ssh-copy-id user@host
# Alternative manuelle :
cat ~/.ssh/id_ed25519.pub | ssh user@host "mkdir -p ~/.ssh && cat >> ~/.ssh/authorized_keys"
Configuration SSH (~/.ssh/config)
ssh-config
Host myserver
    HostName 192.168.1.10
    User ubuntu
    IdentityFile ~/.ssh/mykey
    Port 2222
Commandes SSH courantes
bash
ssh user@host                    # Se connecter
ssh -J jumpuser@jumphost user@target   # Saut via proxy
scp file.txt user@host:/path/     # Copier un fichier vers la machine distante
scp user@host:/path/file.txt .    # Copier depuis la machine distante
rsync -avz -e ssh ./local/ user@host:/remote/  # Synchronisation efficace
Renforcer SSH
Désactiver la connexion root : PermitRootLogin no

Utiliser uniquement l'authentification par clé : PasswordAuthentication no

Changer le port par défaut (optionnel, sécurité par l'obscurité).

Activer AllowUsers ou AllowGroups pour restreindre l'accès.

Systemd (gestion des services Linux)
Commandes courantes
bash
systemctl status nginx           # Vérifier l'état du service
systemctl start nginx            # Démarrer le service
systemctl stop nginx
systemctl restart nginx
systemctl reload nginx           # Rechargement propre (relire la configuration)
systemctl enable nginx           # Démarrer au boot
systemctl disable nginx
systemctl list-units --type=service --all   # Lister tous les services
systemctl daemon-reload          # Recharger les unit files après modification
Créer une unité de service systemd
Créer /etc/systemd/system/myapp.service:

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
Then:

bash
sudo systemctl daemon-reload
sudo systemctl enable myapp
sudo systemctl start myapp
Journalctl (afficher les logs)
bash
journalctl -u myapp              # Logs du service
journalctl -f                    # Suivre les logs (tail)
journalctl --since "1 hour ago"
journalctl _PID=1234             # Filtrer par ID de processus
Stratégies de journalisation
Journalisation structurée
Utilisez le format JSON pour rendre les logs lisibles par machine :

python
import structlog
logger = structlog.get_logger()
logger.info("user_login", user_id=123, ip="192.168.1.1")
Niveaux de log
DEBUG: diagnostic détaillé.

INFO: événements généraux (démarrage, arrêt, transactions normales).

WARN: inattendu mais non fatal.

ERROR: erreur empêchant une opération spécifique.

FATAL/CRITICAL: arrêt du système.

Agrégation des logs
ELK Stack (Elasticsearch, Logstash, Kibana) ou Elastic Cloud.

Loki + Grafana (alternative légère).

Datadog, Splunk, Sumo Logic (SaaS).

Rotation des logs (logrotate)
Empêcher les logs de remplir les disques. Configurer /etc/logrotate.d/myapp :

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
Monitoring et alerting
Métriques à surveiller
Système : CPU, RAM, utilisation disque, load average, network I/O.

Application : taux de requêtes, latence (p50, p95, p99), taux d'erreur, sessions actives.

Base de données : nombre de requêtes, requêtes lentes, utilisation du pool de connexions.

Métier : inscriptions utilisateur, taux de conversion, revenus.

Outils
Prometheus + Grafana : stack open-source standard.

Node Exporter pour les métriques système.

Blackbox Exporter pour la disponibilité des endpoints.

Alertmanager pour le routage des alertes.

Cloud native : AWS CloudWatch, Azure Monitor, GCP Monitoring.

Uptime Monitoring
Pingdom, Statuspage, Better Uptime, Uptime Kuma (self-hosted).

Health checks : exposer un endpoint /health qui renvoie 200 si le service est sain.

Stratégies de sauvegarde
La règle 3-2-1
3 copies des données.

2 types de supports différents (ex. SSD + bande, ou local + cloud).

1 copie hors site (ex. cloud ou centre de données distant).

Types de sauvegarde
Sauvegarde complète : tout copier (lent, gourmand en espace).

Sauvegarde incrémentielle : copier uniquement les changements depuis la dernière sauvegarde complète ou incrémentielle (rapide, restauration complexe).

Sauvegarde différentielle : copier les changements depuis la dernière sauvegarde complète (compromis).

Sauvegardes de bases de données
bash
# PostgreSQL
pg_dump dbname > backup.sql
pg_dumpall > all_backup.sql

# MySQL / MariaDB
mysqldump -u root -p dbname > backup.sql

# Restaurer
psql dbname < backup.sql
mysql -u root -p dbname < backup.sql
Sauvegardes de fichiers
bash
# Archive Tar
tar -czf backup.tar.gz /var/lib/data

# Rsync vers une machine distante
rsync -avz /local/data/ user@backup-server:/backup/data/

# CLI cloud (ex. AWS S3)
aws s3 sync /local/data s3://my-bucket/backup/
Planification automatisée des sauvegardes (cron)
cron
# Exécuter chaque jour à 2 h
0 2 * * * /usr/local/bin/backup_script.sh
Cron et tâches planifiées
Syntaxe cron
text
* * * * * command
│ │ │ │ │
│ │ │ │ └─ Jour de la semaine (0-7, 0=Sun)
│ │ │ └─── Mois (1-12)
│ │ └───── Jour du mois (1-31)
│ └─────── Heure (0-23)
└───────── Minute (0-59)
Exemples
cron
# Toutes les 5 minutes
*/5 * * * * /path/to/script

# Chaque jour à 3:15 AM
15 3 * * * /path/to/script

# Chaque lundi à 4 AM
0 4 * * 1 /path/to/script

# Toutes les heures
0 * * * * /path/to/script
Gestion de cron
bash
crontab -l          # Lister les tâches cron de l'utilisateur courant
crontab -e          # Éditer
crontab -r          # Tout supprimer
Anacron
Utilisé pour les systèmes qui ne tournent pas 24/7 (ex. laptops), garantit que les tâches s'exécutent finalement.

Gestion des packages et mises à jour
Debian/Ubuntu (apt)
bash
sudo apt update                # Mettre à jour la liste des packages
sudo apt upgrade               # Mettre à niveau tous les packages
sudo apt install git nginx
sudo apt remove git
sudo apt autoremove            # Supprimer les dépendances inutilisées
RHEL/CentOS/Fedora (dnf/yum)
bash
sudo dnf check-update
sudo dnf update
sudo dnf install git nginx
sudo dnf remove git
Mises à jour de sécurité
Activer unattended-upgrades sur Ubuntu pour les correctifs de sécurité :

bash
sudo apt install unattended-upgrades
sudo dpkg-reconfigure -plow unattended-upgrades
Docker en production
Bonnes pratiques
Utiliser des tags d'image spécifiques (python:3.12-slim) et non latest.

Exécuter les conteneurs avec un utilisateur non root.

Scanner les images pour détecter les vulnérabilités (docker scan, trivy).

Définir des limites de ressources (--memory, --cpus).

Utiliser des secrets (via Docker secrets ou l'environnement avec prudence).

Conserver des images petites : builds multi-stage, base alpine.

Docker Compose en production
Définir les limites de ressources dans docker-compose.yml :

yaml
services:
  app:
    image: myapp:1.0
    deploy:
      resources:
        limits:
          memory: 512M
          cpus: '0.5'
Principes de base CI/CD
Étapes du pipeline
Build : compiler le code, installer les dépendances.

Test : exécuter les tests unitaires, d'intégration et les vérifications de lint.

Containerise: construire l'image Docker.

Push : envoyer l'image vers le registry de conteneurs.

Deploy : mettre à jour l'environnement de staging/production.

Outils
GitHub Actions : intégré à GitHub.

GitLab CI : intégré à GitLab.

Jenkins : traditionnel, très configurable.

CircleCI, Travis CI : solutions tierces populaires.

ArgoCD : GitOps pour Kubernetes.

Exemple de GitHub Action (simple) :
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
Réglage du système et dépannage
Vérifier l'espace disque
bash
df -h                      # Utilisation disque lisible
du -sh /* | sort -h        # Taille des répertoires de premier niveau
Vérifier l'utilisation mémoire
bash
free -m                    # Mémoire en MB
vmstat 1 10                # Statistiques de mémoire virtuelle
top -o %MEM                # Trier les processus par mémoire
Vérifier la charge CPU
bash
uptime                     # Load average sur 1,5,15 minutes
top -o %CPU                # Trier les processus par CPU
mpstat -P ALL 1 5          # Utilisation CPU par cœur
Vérifier le réseau
bash
netstat -i                 # Statistiques des interfaces
iftop                      # Utilisation de bande passante en direct (installation requise)
nload                      # Autre moniteur de bande passante
Trouver les gros fichiers
bash
find / -type f -size +100M -exec ls -lh {} \; 2>/dev/null
Infrastructure as Code (IaC)
Terraform
Déclarer les ressources cloud en HCL.

hcl
provider "aws" {
  region = "us-east-1"
}
resource "aws_instance" "web" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t2.micro"
}
Ansible
Gestion de configuration sans agent avec YAML.

yaml
- name: Install nginx
  hosts: webservers
  tasks:
    - name: Install nginx
      apt:
        name: nginx
        state: present
Bonnes pratiques
Utiliser des modules et des rôles pour la réutilisabilité.

Stocker l'état à distance (S3, Terraform Cloud).

Utiliser des variables et des secrets (AWS_SECRET_ACCESS_KEY via l'environnement, pas codé en dur).

Versionner votre code IaC.

Réponse aux incidents (astreinte)
Checklist pour une panne de service
Accuser réception de l'alerte.

Évaluer l'étendue : quels services/utilisateurs sont affectés ?

Identifier le problème (regarder les logs, métriques, déploiements récents).

Contenir si possible (circuit breakers, feature flags).

Rollback ou correction directe.

Communiquer le statut aux parties prenantes et aux utilisateurs (status page).

Documenter la chronologie de l'incident et les actions.

Post-mortem : sous 24 à 48 heures, rédiger une analyse des causes racines (RCA) et des actions pour éviter une récidive.
