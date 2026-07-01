<!-- 
Ce fichier a été automatiquement traduit de l'anglais vers le français.
Source: networking_basics.md
Note: Les termes techniques, exemples de code et noms propres peuvent rester en anglais.
Pour améliorer la précision, veuillez contribuer aux modifications via des pull requests.
-->

# Bases des Réseaux

Une référence pratique pour les développeurs et les administrateurs système — concepts de base, protocoles, commandes et dépannage.

---

# Le Modèle OSI (7 Couches)

Un cadre conceptuel pour comprendre la communication réseau.

| Couche | Nom | Fonction | Exemples de protocoles |
|-------|------|----------|-------------------|
| 7 | Application | Services utilisateur final | HTTP, HTTPS, FTP, SMTP, DNS, SSH |
| 6 | Présentation | Formatage des données, chiffrement, compression | TLS, JPEG, ASCII |
| 5 | Session | Gestion de connexion | NetBIOS, RPC |
| 4 | Transport | Livraison de bout en bout, correction d'erreurs, contrôle de flux | TCP, UDP |
| 3 | Réseau | Routage, adressage | IP, ICMP, OSPF, BGP |
| 2 | Liaison de données | Encadrement, détection d'erreurs, adresses MAC | Ethernet, Wi-Fi, PPP |
| 1 | Physique | Transmission de bits bruts | Câbles Ethernet, fibres optiques, ondes radio |

En pratique, le **modèle TCP/IP** (4 couches : Liaison, Internet, Transport, Application) est plus couramment utilisé pour Internet.

---

# Adressage IP

## IPv4
- Adresse 32 bits, écrite en quatre octets : `192.168.1.1`
- Total : ~4,3 milliards d'adresses (mais épuisées en pratique).

## IPv6
- Adresse 128 bits, écrite en hexadécimal : `2001:0db8:85a3:0000:0000:8a2e:0370:7334`
- Total : 2¹²⁸ adresses (pratiquement infinies).

## Plages IP Privées (RFC 1918)
Celles-ci ne sont pas routables sur Internet ; utilisées dans les réseaux locaux :
- `10.0.0.0/8` (10.0.0.0 – 10.255.255.255)
- `172.16.0.0/12` (172.16.0.0 – 172.31.255.255)
- `192.168.0.0/16` (192.168.0.0 – 192.168.255.255)

## Notation CIDR
`192.168.1.0/24` signifie que les 24 premiers bits sont le préfixe du réseau ; les 8 derniers bits sont pour les hôtes. Cela inclut les adresses `192.168.1.0` à `192.168.1.255`.

---

# DNS (Domain Name System)

Mappe les noms de domaine (par exemple, `example.com`) aux adresses IP.

## Types d'Enregistrements
| Type | Objectif |
|------|---------|
| **A** | Mappe le domaine à une adresse IPv4 |
| **AAAA** | Mappe le domaine à une adresse IPv6 |
| **CNAME** | Alias vers un autre nom de domaine |
| **MX** | Serveur d'échange de courrier |
| **TXT** | Texte arbitraire (SPF, DKIM, vérification) |
| **NS** | Serveur de noms pour le domaine |
| **SRV** | Enregistrement de service (par exemple, pour SIP) |

## Outils Courants
```bash
dig example.com            # Recherche DNS (détaillée)
nslookup example.com       # Recherche DNS (plus simple)
host example.com           # Recherche rapide
dig -x 8.8.8.8             # Recherche inverse (IP vers nom)
```

## Ports et Protocoles

### Ports Bien Connus (0–1023)
| Port | Protocole | Service |
|------|-----------|---------|
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
| 587 | TCP | SMTP (soumission) |
| 993 | TCP | IMAPS |
| 995 | TCP | POP3S |
| 3306 | TCP | MySQL |
| 5432 | TCP | PostgreSQL |
| 6379 | TCP | Redis |
| 27017 | TCP | MongoDB |

### Vérifier les ports ouverts
```bash
ss -tulpn                 # Linux : sockets en écoute et établis
netstat -an               # Outil plus ancien
lsof -i :8080             # Voir le processus utilisant le port 8080
nmap localhost            # Scanner les ports locaux
```

## TCP vs UDP
| Caractéristique | TCP | UDP |
|-----------------|-----|-----|
| Connexion | Orienté connexion (poignée de main) | Sans connexion |
| Fiabilité | Livraison garantie, retransmission | Meilleur effort (peut perdre des paquets) |
| Ordonnancement | Préserve l'ordre | Aucune garantie d'ordre |
| Contrôle de flux | Oui (fenêtre glissante) | Non |
| Cas d'usage | Web (HTTP), courriel, SSH, transfert de fichiers | DNS, streaming, VoIP, jeux, SNMP |
| Taille d'en-tête | 20–60 octets | 8 octets |

## HTTP et HTTPS

### Méthodes HTTP
- **GET** : Récupérer une ressource (idempotent, sûr).
- **POST** : Soumettre des données (non idempotent).
- **PUT** : Mettre à jour/remplacer une ressource (idempotent).
- **PATCH** : Mise à jour partielle.
- **DELETE** : Supprimer une ressource (idempotent).

### Codes de Statut
- **1xx** : Informationnel (100 Continue).
- **2xx** : Succès (200 OK, 201 Created, 204 No Content).
- **3xx** : Redirection (301 Moved Permanently, 302 Found, 304 Not Modified).
- **4xx** : Erreur client (400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found, 429 Too Many Requests).
- **5xx** : Erreur serveur (500 Internal Server Error, 502 Bad Gateway, 503 Service Unavailable).

### En-têtes HTTP
- **Content-Type** : Type de média (application/json, text/html).
- **Authorization** : Identifiants (par exemple, Bearer `<token>`).
- **Cache-Control** : Politique de mise en cache.
- **En-têtes CORS** : Access-Control-Allow-Origin, etc.

## TLS/SSL
- Chiffre le trafic HTTP (HTTPS = HTTP sur TLS).
- Les certificats émis par des Autorités de Certification (CA) authentifient le serveur.
- Vérifiez la chaîne de certificats et le nom d'hôte côté client.

## Pare-feu et NAT

### Pare-feu
- Filtre le trafic selon des règles (IP source, IP de destination, port, protocole).
- Les pare-feu avec état suivent les états de connexion.

### NAT (Network Address Translation)
- Traduit les IP privées en une IP publique pour l'accès Internet.
- **Redirection de port** : mappe un port public vers un hôte/port interne.

## Commandes Réseau Courantes

### Tests de Connectivité
```bash
ping google.com            # Requête echo ICMP
ping -c 4 8.8.8.8          # ping 4 fois
traceroute google.com      # Tracer la route (Linux)
tracert google.com         # Version Windows
```

### Routage
```bash
ip route show              # Linux : table de routage
route -n                   # Linux (ancien)
netstat -r                 # Windows/Mac
```

### Interfaces Réseau
```bash
ip addr show               # Lister les interfaces et IPs
ifconfig                   # Commande ancienne
```

### DNS
```bash
dig example.com
nslookup example.com
host example.com
```

### Connectivité à un Port
```bash
nc -zv google.com 443      # Netcat : vérifier si le port 443 est ouvert
telnet google.com 443      # Telnet vers le port
curl -v https://google.com # Sortie verbeuse
```

### Pare-feu (Linux iptables/nftables)
```bash
sudo ufw status            # Ubuntu : pare-feu simple
sudo iptables -L -n        # Lister les règles
```

### Statistiques Réseau
```bash
ss -tulpn                  # Afficher les sockets en écoute (Linux)
netstat -an                # Tous les sockets (tous les OS)
```

## Sous-réseau (Référence Rapide)
| CIDR | Masque de sous-réseau | Nombre d'adresses | Hôtes utilisables |
|------|----------------------|-------------------|-------------------|
| /32 | 255.255.255.255 | 1 | 1 |
| /30 | 255.255.255.252 | 4 | 2 |
| /29 | 255.255.255.248 | 8 | 6 |
| /28 | 255.255.255.240 | 16 | 14 |
| /27 | 255.255.255.224 | 32 | 30 |
| /26 | 255.255.255.192 | 64 | 62 |
| /25 | 255.255.255.128 | 128 | 126 |
| /24 | 255.255.255.0 | 256 | 254 |
| /23 | 255.255.254.0 | 512 | 510 |
| /22 | 255.255.252.0 | 1 024 | 1 022 |
| /16 | 255.0.0.0 | 65 536 | 65 534 |
| /8 | 255.0.0.0 | 16 777 216 | 16 777 214 |

## Équilibrage de Charge et Proxies Inverses

### Nginx comme Proxy Inverse
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

### Algorithmes d'Équilibrage de Charge
- **Round-robin** : Tour à tour.
- **Moins de connexions** : Dirige vers le serveur avec le moins de connexions actives.
- **Hachage IP** : Persistance de session (stickiness).
- **Round-robin pondéré** : Attribution de poids différents aux serveurs.

### Outils
- **Logiciels** : Nginx, HAProxy
- **Cloud** : AWS ELB, Azure Load Balancer, GCP Cloud Load Balancing

## Liste de Vérification pour le Dépannage
1. La liaison physique est-elle active ? (Vérifiez les câbles, la connexion Wi-Fi).
2. Pouvez-vous pinguer la passerelle ? (par exemple, `ping 192.168.1.1`).
3. Pouvez-vous pinguer une IP externe ? (par exemple, `8.8.8.8`).
4. Pouvez-vous résoudre un nom de domaine ? (`dig google.com`).
5. L'application écoute-t-elle sur le port attendu ? (`ss -tulpn | grep 8080`).
6. Le pare-feu bloque-t-il le port ? (Vérifiez iptables/ufw ou les groupes de sécurité cloud).
7. Y a-t-il des erreurs dans les journaux de l'application ?
8. Le certificat TLS est-il valide et fiable ? (`openssl s_client -connect example.com:443`).

---

## Résumé

Ce guide couvre les fondamentaux des réseaux essentiels pour les développeurs et les administrateurs système. Pour approfondir, consultez la documentation RFC, les guides des fournisseurs cloud et les ressources spécifiques aux protocoles.
- **Sauvegarde complète** : tout copier (lent, lourd en espace)
- **Sauvegarde incrémentielle** : copier uniquement les changements depuis la dernière sauvegarde complète ou incrémentielle (rapide, restauration complexe)
- **Sauvegarde différentielle** : copier les changements depuis la dernière sauvegarde complète (compromis)

## Sauvegardes de Base de Données
```bash
# PostgreSQL
pg_dump dbname > backup.sql
pg_dumpall > all_backup.sql

# MySQL / MariaDB
mysqldump -u root -p dbname > backup.sql

# Restauration
psql dbname < backup.sql
mysql -u root -p dbname < backup.sql
```

## Sauvegardes de Fichiers
```bash
# Archive tar
tar -czf backup.tar.gz /var/lib/data

# Rsync vers distant
rsync -avz /local/data/ user@backup-server:/backup/data/

# CLI Cloud (par exemple, AWS S3)
aws s3 sync /local/data s3://my-bucket/backup/
```

## Planification Automatique des Sauvegardes (cron)
```cron
# Exécuter quotidiennement à 2h du matin
0 2 * * * /usr/local/bin/backup_script.sh
```

# Cron et Tâches Planifiées

## Syntaxe Cron
```text
* * * * * command
│ │ │ │ │
│ │ │ │ └─ Jour de la semaine (0-7, 0=Dim)
│ │ │ └─── Mois (1-12)
│ │ └───── Jour du mois (1-31)
│ └─────── Heure (0-23)
└───────── Minute (0-59)
```

## Exemples
```cron
# Toutes les 5 minutes
*/5 * * * * /path/to/script

# Tous les jours à 3h15 du matin
15 3 * * * /path/to/script

# Tous les lundis à 4h du matin
0 4 * * 1 /path/to/script

# Toutes les heures
0 * * * * /path/to/script
```

## Gestion de Cron
```bash
crontab -l          # Lister les tâches cron de l'utilisateur actuel
crontab -e          # Éditer
crontab -r          # Supprimer tout
```

## Anacron
Utilisé pour les systèmes ne fonctionnant pas 24h/24 et 7j/7 (par exemple, ordinateurs portables), garantit que les tâches s'exécutent éventuellement.

# Gestion des Paquets et Mises à Jour

## Debian/Ubuntu (apt)
```bash
sudo apt update                # Mettre à jour la liste des paquets
sudo apt upgrade               # Mettre à niveau tous les paquets
sudo apt install git nginx
sudo apt remove git
sudo apt autoremove            # Supprimer les dépendances inutilisées
```

## RHEL/CentOS/Fedora (dnf/yum)
```bash
sudo dnf check-update
sudo dnf update
sudo dnf install git nginx
sudo dnf remove git
```

## Mises à Jour de Sécurité
Activez `unattended-upgrades` sur Ubuntu pour les correctifs de sécurité :

```bash
sudo apt install unattended-upgrades
sudo dpkg-reconfigure -plow unattended-upgrades
```

# Docker en Production

## Bonnes Pratiques
- Utilisez des balises d'image spécifiques (`python:3.12-slim`) pas `latest`
- Exécutez les conteneurs en tant qu'utilisateur non-root
- Analysez les images pour les vulnérabilités (`docker scan`, `trivy`)
- Définissez des limites de ressources (`--memory`, `--cpus`)
- Utilisez des secrets (via Docker secrets ou environnement avec précaution)
- Gardez les images petites : builds multi-étapes, base alpine

## Docker Compose en Production
Définissez des limites de ressources dans `docker-compose.yml` :

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

# Bases CI/CD

## Étapes du Pipeline
1. **Build** : Compiler le code, installer les dépendances
2. **Test** : Exécuter les tests unitaires, d'intégration et de linting
3. **Containerisation** : Construire l'image Docker
4. **Push** : Pousser l'image vers le registre de conteneurs
5. **Deploy** : Mettre à jour l'environnement de staging/production

## Outils
- **GitHub Actions** : Intégré à GitHub
- **GitLab CI** : Intégré à GitLab
- **Jenkins** : Traditionnel, hautement configurable
- **CircleCI, Travis CI** : Tiers populaires
- **ArgoCD** : GitOps pour Kubernetes

## Exemple GitHub Action (simple) :
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

# Réglage Système et Dépannage

## Vérifier l'Espace Disque
```bash
df -h                      # Utilisation du disque lisible par l'homme
du -sh /* | sort -h        # Taille des répertoires de premier niveau
```

## Vérifier l'Utilisation de la Mémoire
```bash
free -m                    # Mémoire en Mo
vmstat 1 10                # Statistiques de mémoire virtuelle
top -o %MEM                # Trier les processus par mémoire
```

## Vérifier la Charge CPU
```bash
uptime                     # Charge moyenne sur 1, 5, 15 minutes
top -o %CPU                # Trier les processus par CPU
mpstat -P ALL 1 5          # Utilisation CPU par cœur
```

## Vérifier le Réseau
```bash
netstat -i                 # Statistiques d'interface
iftop                      # Utilisation de la bande passante en direct (nécessite installation)
nload                      # Un autre moniteur de bande passante
```

## Trouver les Fichiers Volumineux
```bash
find / -type f -size +100M -exec ls -lh {} \; 2>/dev/null
```

# Infrastructure as Code (IaC)

## Terraform
Déclarez les ressources cloud en HCL.

```hcl
provider "aws" {
  region = "us-east-1"
}

resource "aws_instance" "web" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t2.micro"
}
```

## Ansible
Gestion de configuration sans agent utilisant YAML.

```yaml
- name: Installer nginx
  hosts: webservers
  tasks:
    - name: Installer nginx
      apt:
        name: nginx
        state: present
```

## Bonnes Pratiques
- Utilisez des modules et des rôles pour la réutilisabilité
- Stockez l'état à distance (S3, Terraform Cloud)
- Utilisez des variables et des secrets (`AWS_SECRET_ACCESS_KEY` via environnement, pas en dur)
- Versionnez votre code IaC

# Réponse aux Incidents (Astreinte)

## Liste de Vérification pour Panne de Service
1. Accusez réception de l'alerte
2. Évaluez la portée : Quels services/utilisateurs sont affectés ?
3. Identifiez le problème (consultez les journaux, métriques, déploiements récents)
4. Contenez si possible (disjoncteurs, indicateurs de fonctionnalité)
5. Rollback ou correction vers l'avant
6. Communiquez le statut aux parties prenantes et utilisateurs (page de statut)
7. Documentez la chronologie de l'incident et les actions
8. **Post-mortem** : dans les 24 à 48 heures, rédigez une analyse de cause racine (RCA) et des éléments d'action pour prévenir la récurrence