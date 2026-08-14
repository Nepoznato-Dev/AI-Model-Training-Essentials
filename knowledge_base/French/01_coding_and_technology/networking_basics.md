<!--
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

-->
# Bases du réseautage
Une référence pratique pour les développeurs et les administrateurs système : concepts de base, protocoles, commandes et dépannage.
---

## Le modèle OSI (7 couches)
Un cadre conceptuel pour comprendre la communication en réseau.
| Couche | Nom | Fonction | Exemples de protocoles |
|-------|------|----------|-------------------|
| 7 | Demande | Services aux utilisateurs finaux | HTTP, HTTPS, FTP, SMTP, DNS, SSH |
| 6 | Présentation | Formatage, chiffrement, compression des données | TLS, JPEG, ASCII |
| 5 | Séance | Gestion des connexions | NetBIOS, RPC |
| 4 | Transports | Livraison de bout en bout, correction d'erreurs, contrôle de flux | TCP, UDP |
| 3 | Réseau | Routage, adressage | IP, ICMP, OSPF, BGP |
| 2 | Liaison de données | Cadrage, détection d'erreurs, adresses MAC | Ethernet, Wi-Fi, PPP |
| 1 | Physique | Transmission de bits bruts | Câbles Ethernet, fibres optiques, ondes radio |
En pratique, le **modèle TCP/IP** (4 couches : Lien, Internet, Transport, Application) est plus couramment utilisé pour Internet.
---

## Adressage IP
### IPv4
- Adresse 32 bits, écrite sur quatre octets :`192.168.1.1`
- Total : ~4,3 milliards d'adresses (mais épuisé en pratique).
###IPv6
- Adresse 128 bits, écrite en hexadécimal :`2001:0db8:85a3:0000:0000:8a2e:0370:7334`
- Total : 2¹²⁸ adresses (pratiquement infinies).
### Plages d'adresses IP privées (RFC 1918)
Ceux-ci ne sont pas routables sur Internet ; utilisé au sein des réseaux locaux :
-`10.0.0.0/8` (10.0.0.0 – 10.255.255.255)
-`172.16.0.0/12` (172.16.0.0 – 172.31.255.255)
-`192.168.0.0/16` (192.168.0.0 – 192.168.255.255)
### Notation CIDR
`192.168.1.0/24`signifie que les 24 premiers bits constituent le préfixe du réseau ; les 8 derniers bits sont des hôtes. Il comprend les adresses`192.168.1.0`à`192.168.1.255`.
---

## DNS (système de noms de domaine)
Mappe les noms de domaine (par exemple,`example.com`) aux adresses IP.
### Types d'enregistrements
| Tapez | Objectif |
|------|--------------|
| **A** | Mappe le domaine à l’adresse IPv4 |
| **AAAA** | Mappe le domaine à l’adresse IPv6 |
| **CNAME** | Alias ​​vers un autre nom de domaine |
| **MX** | Serveur d'échange de courrier |
| **TXT** | Texte arbitraire (SPF, DKIM, vérification) |
| **NS** | Serveur de noms pour le domaine |
| **SRV** | Historique de service (par exemple, pour SIP) |
### Outils communs```bash
dig example.com            # DNS lookup (detailed)
nslookup example.com       # DNS lookup (simpler)
host example.com           # Quick lookup
dig -x 8.8.8.8             # Reverse lookup (IP to name)
```

---

## Ports et protocoles
### Ports bien connus (0–1023)
| Port | Protocole | Services |
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
| 465 | TCP | SMTP |
| 587 | TCP | SMTP (soumission) |
| 993 | TCP | IMAPS |
| 995 | TCP | POP3S |
| 3306 | TCP | MySQL |
| 5432 | TCP | PostgreSQL |
| 6379 | TCP | Rédis |
| 27017 | TCP | MongoDB |
### Vérifiez les ports ouverts
```bash
ss -tulpn                 # Linux: listen and established sockets
netstat -an               # Older tool
lsof -i :8080             # See process using port 8080
nmap localhost            # Scan local ports
```

---

## TCP contre UDP
| Fonctionnalité | TCP | UDP |
|---------|-----|-----|
| Connexion | Orienté connexion (poignée de main) | Sans connexion |
| Fiabilité | Livraison garantie, retransmission | Meilleur effort (peut supprimer des paquets) |
| Commande | Préserve l'ordre | Aucune garantie de commande |
| Contrôle de flux | Oui (fenêtre coulissante) | Non |
| Cas d'utilisation | Web (HTTP), courrier électronique, SSH, transfert de fichiers | DNS, streaming, VoIP, jeux, SNMP |
| Taille de l'en-tête | 20 à 60 octets | 8 octets |
---

## HTTP et HTTPS
### Méthodes HTTP
| Méthode | Descriptif |
|--------|-------------|
| **OBTENIR** | Récupérer une ressource (idempotente, sécurisée) |
| **POST** | Soumettre des données (non idempotentes) |
| **METTRE** | Mettre à jour/remplacer une ressource (idempotent) |
| **PATCH** | Mise à jour partielle |
| **SUPPRIMER** | Supprimer une ressource (idempotente) |
### Codes d'état
| Codes | Signification |
|------|--------------|
| **1xx** | Informatif (100 Continuer) |
| **2xx** | Succès (200 OK, 201 Créé, 204 Aucun contenu) |
| **3xx** | Redirection (301 déplacés de façon permanente, 302 trouvés, 304 non modifiés) |
| **4xx** | Erreur client (400 requêtes incorrectes, 401 non autorisées, 403 interdites, 404 introuvables, 429 requêtes trop nombreuses) |
| **5xx** | Erreur de serveur (500 Erreur de serveur interne, 502 Passerelle incorrecte, 503 Service non disponible) |
### En-têtes
| En-tête | Objectif |
|--------|---------|
| `Content-Type`| Type de support (`application/json`,`text/html`) |
| `Authorization`| Informations d'identification (par exemple,`Bearer <token>`) |
| `Cache-Control`| Politique de mise en cache |
| En-têtes CORS | `Access-Control-Allow-Origin`, etc. |
---

## TLS/SSL
Chiffre le trafic HTTP (HTTPS = HTTP over TLS).
- Les certificats des autorités de certification (CA) authentifient le serveur.
- Vérifiez la chaîne de certificats et le nom d'hôte côté client.
---

## Pare-feu et NAT
### Pare-feu
- Filtre le trafic en fonction de règles (IP source, IP de destination, port, protocole).
- Les pare-feu avec état suivent les états de connexion.
### NAT (traduction d'adresses réseau)
- Traduit les IP privées en IP publique pour l'accès à Internet.
- Redirection de port : mappe un port public à un hôte/port interne.
---

## Commandes réseau courantes
### Tests de connectivité
```bash
ping google.com            # ICMP echo request
ping -c 4 8.8.8.8          # ping 4 times
traceroute google.com      # Trace the route (Linux)
tracert google.com         # Windows version
```

### Routage
```bash
ip route show              # Linux: routing table
route -n                   # Older Linux
netstat -r                 # Windows/Mac
```

###Interfaces réseau
```bash
ip addr show               # List interfaces and IPs
ifconfig                   # Older command
```

###DNS
```bash
dig example.com
nslookup example.com
host example.com
```

### Connectivité à un port
```bash
nc -zv google.com 443      # Netcat: check if port 443 is open
telnet google.com 443      # Telnet to port
curl -v https://google.com # Verbose output
```

### Pare-feu (Linux iptables/nftables)
```bash
sudo ufw status            # Ubuntu: simple firewall
sudo iptables -L -n        # List rules
```

### Statistiques du réseau
```bash
ss -tulpn                  # Show listening sockets (Linux)
netstat -an                # All sockets (all OS)
```

---

## Sous-réseaux (référence rapide)
| CIDR | Masque de réseau | Nombre d'adresses | Hôtes utilisables |
|------|---------|-----------|--------------|
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
| /16 | 255.255.0.0 | 65 536 | 65 534 |
| /8 | 255.0.0.0 | 16 777 216 | 16 777 214 |
---

## Équilibrage de charge et proxys inversés
### Nginx comme proxy inverse
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

### Algorithmes d'équilibrage de charge
- **Robin à la ronde**
- **Moins de connexions**
- **Hachage IP** (adhérence de la session)
- **Robin à la ronde pondéré**
### Outils
- **Nginx, HAProxy** (logiciel)
- **AWS ELB, Azure Load Balancer, GCP Cloud Load Balancing** (cloud)
---

## Liste de contrôle de dépannage
1. La liaison physique est-elle établie ? (Vérifiez les câbles, la connexion Wi-Fi).
2. Pouvez-vous envoyer une requête ping à la passerelle ? (par exemple,`ping 192.168.1.1`).
3. Pouvez-vous envoyer une requête ping à une adresse IP externe ? (par exemple,`8.8.8.8`).
4. Pouvez-vous résoudre un domaine ? (`dig google.com`).
5. L'application écoute-t-elle sur le port attendu ? (`ss -tulpn | grep 8080`).
6. Le pare-feu bloque-t-il le port ? (Vérifiez`iptables`/`ufw`ou les groupes de sécurité cloud).
7. Y a-t-il des erreurs dans les journaux d'application ?
8. Le certificat TLS est-il valide et fiable ? (`openssl s_client -connect example.com:443`).