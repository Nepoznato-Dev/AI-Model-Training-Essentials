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
# Nozioni di base sulla rete
Un riferimento pratico per sviluppatori e amministratori di sistema: concetti fondamentali, protocolli, comandi e risoluzione dei problemi.
---

## Il modello OSI (7 livelli)
Un quadro concettuale per comprendere la comunicazione di rete.
| Strato | Nome | Funzione | Protocolli di esempio |
|-------|------|----------|------|
| 7| Applicazione | Servizi per l'utente finale | HTTP, HTTPS, FTP, SMTP, DNS, SSH |
| 6| Presentazione | Formattazione, crittografia, compressione dei dati | TLS, JPEG, ASCII |
| 5| Sessione | Gestione della connessione | NetBIOS, RPC |
| 4| Trasporti | Consegna end-to-end, correzione errori, controllo del flusso | TCP, UDP |
| 3| Rete | Routing, indirizzamento | IP, ICMP, OSPF, BGP |
| 2| Collegamento dati | Framing, rilevamento errori, indirizzi MAC | Ethernet, Wi-Fi, PPP |
| 1| Fisico | Trasmissione in bit grezzo | Cavi Ethernet, fibre ottiche, onde radio |
In pratica, il **modello TCP/IP** (4 livelli: collegamento, Internet, trasporto, applicazione) è più comunemente utilizzato per Internet.
---

## Indirizzamento IP
### IPv4
- Indirizzo a 32 bit, scritto come quattro ottetti:`192.168.1.1`
- Totale: ~4,3 miliardi di indirizzi (ma in pratica esauriti).
### IPv6
- Indirizzo a 128 bit, scritto in esadecimale:`2001:0db8:85a3:0000:0000:8a2e:0370:7334`
- Totale: 2¹²⁸ indirizzi (praticamente infiniti).
### Intervalli IP privati (RFC 1918)
Questi non sono instradabili su Internet; utilizzato all'interno delle reti locali:
-`10.0.0.0/8` (10.0.0.0 – 10.255.255.255)
-`172.16.0.0/12` (172.16.0.0 – 172.31.255.255)
-`192.168.0.0/16` (192.168.0.0 – 192.168.255.255)
### Notazione CIDR
`192.168.1.0/24`significa che i primi 24 bit sono il prefisso di rete; gli ultimi 8 bit sono host. Include gli indirizzi da`192.168.1.0`a`192.168.1.255`.
---

## DNS (sistema dei nomi di dominio)
Mappa i nomi di dominio (ad esempio,`example.com`) su indirizzi IP.
### Tipi di record
| Digitare | Scopo |
|------|---------|
| **A** | Mappa il dominio sull'indirizzo IPv4 |
| **AAAA** | Mappa il dominio sull'indirizzo IPv6 |
| **CNAME** | Alias ​​ad un altro nome di dominio |
| **MX** | Server di scambio posta |
| **TXT** | Testo arbitrario (SPF, DKIM, verifica) |
| **NS** | Server dei nomi per il dominio |
| **SRV** | Record di servizio (ad esempio per SIP) |
### Strumenti comuni```bash
dig example.com            # DNS lookup (detailed)
nslookup example.com       # DNS lookup (simpler)
host example.com           # Quick lookup
dig -x 8.8.8.8             # Reverse lookup (IP to name)
```

---

## Porte e protocolli
### Porte conosciute (0–1023)
| Porto | Protocollo | Servizio |
|------|----------|---------|
| 20, 21| TCP | FTP |
| 22| TCP | SSH |
| 23| TCP | Telnet |
| 25| TCP | SMTP |
| 53| UDP/TCP | DNS |
| 80| TCP | HTTP |
| 110| TCP | POP3 |
| 123| UDP | NTP |
| 143| TCP | IMAP |
| 443| TCP | HTTPS |
| 465| TCP | SMTP |
| 587| TCP | SMTP (invio) |
| 993| TCP | IMAP |
| 995| TCP | POP3S |
| 3306| TCP | MySQL |
| 5432| TCP | PostgreSQL |
| 6379| TCP | Redis |
| 27017| TCP | MongoDB |
### Controlla le porte aperte
```bash
ss -tulpn                 # Linux: listen and established sockets
netstat -an               # Older tool
lsof -i :8080             # See process using port 8080
nmap localhost            # Scan local ports
```

---

## TCP contro UDP
| Caratteristica | TCP | UDP |
|---------|-----|-----|
| Connessione | Orientato alla connessione (stretta di mano) | Senza connessione |
| Affidabilità | Consegna garantita, ritrasmissione | Miglior sforzo (potrebbero perdere i pacchetti) |
| Ordinare | Conserva l'ordine | Nessuna garanzia sull'ordine |
| Controllo del flusso | Sì (finestra scorrevole) | No |
| Casi d'uso | Web (HTTP), e-mail, SSH, trasferimento file | DNS, streaming, VoIP, giochi, SNMP |
| Dimensione intestazione | 20–60 byte | 8 byte |
---

##HTTP e HTTPS
### Metodi HTTP
| Metodo | Descrizione |
|--------|-------------|
| **OTTIENI** | Recuperare una risorsa (idempotente, sicura) |
| **POST** | Invia dati (non idempotente) |
| **METTERE** | Aggiorna/sostituisci una risorsa (idempotente) |
| **PATCH** | Aggiornamento parziale |
| **ELIMINA** | Rimuovere una risorsa (idempotente) |
### Codici di stato
| Codice | Significato |
|------|---------|
| **1xx** | Informativo (100 Continua) |
| **2xx** | Successo (200 OK, 201 Creato, 204 Nessun contenuto) |
| **3xx** | Reindirizzamento (301 spostato permanentemente, 302 trovato, 304 non modificato) |
| **4xx** | Errore client (400 Richiesta errata, 401 Non autorizzata, 403 Vietata, 404 Non trovata, 429 Troppe richieste) |
| **5xx** | Errore del server (500 Errore interno del server, 502 Gateway non valido, 503 Servizio non disponibile) |
### Intestazioni
| Intestazione | Scopo |
|--------|---------|
| `Content-Type`| Tipo di supporto (`application/json`,`text/html`) |
| `Authorization`| Credenziali (ad esempio,`Bearer <token>`) |
| `Cache-Control`| Politica di memorizzazione nella cache |
| Intestazioni CORS | `Access-Control-Allow-Origin`, ecc. |
---

##TLS/SSL
Crittografa il traffico HTTP (HTTPS = HTTP over TLS).
- I certificati delle autorità di certificazione (CA) autenticano il server.
- Verificare la catena di certificati e il nome host sul lato client.
---

## Firewall e NAT
### Firewall
- Filtra il traffico in base a regole (IP di origine, IP di destinazione, porta, protocollo).
- I firewall con stato tengono traccia degli stati di connessione.
### NAT (Traduzione degli indirizzi di rete)
- Converte gli IP privati in IP pubblici per l'accesso a Internet.
- Port forwarding: mappa una porta pubblica su un host/porta interno.
---

## Comandi di rete comuni
### Test di connettività
```bash
ping google.com            # ICMP echo request
ping -c 4 8.8.8.8          # ping 4 times
traceroute google.com      # Trace the route (Linux)
tracert google.com         # Windows version
```

### Itinerario
```bash
ip route show              # Linux: routing table
route -n                   # Older Linux
netstat -r                 # Windows/Mac
```

### Interfacce di rete
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

### Connettività a una porta
```bash
nc -zv google.com 443      # Netcat: check if port 443 is open
telnet google.com 443      # Telnet to port
curl -v https://google.com # Verbose output
```

### Firewall (iptables/nftables Linux)
```bash
sudo ufw status            # Ubuntu: simple firewall
sudo iptables -L -n        # List rules
```

### Statistiche di rete
```bash
ss -tulpn                  # Show listening sockets (Linux)
netstat -an                # All sockets (all OS)
```

---

## Sottoreti (riferimento rapido)
| CIDR | Maschera di rete | Numero di indirizzi | Host utilizzabili |
|------|---------|----------------------|-----|
| /32 | 255.255.255.255 | 1| 1|
| /30 | 255.255.255.252| 4| 2|
| /29 | 255.255.255.248| 8| 6|
| /28 | 255.255.255.240 | 16| 14|
| /27 | 255.255.255.224| 32| 30|
| /26 | 255.255.255.192| 64| 62|
| /25 | 255.255.255.128| 128| 126|
| /24 | 255.255.255.0 | 256| 254|
| /23 | 255.255.254.0 | 512| 510|
| /22 | 255.255.252.0 | 1.024 | 1.022 |
| /16 | 255.255.0.0 | 65.536| 65.534 |
| /8 | 255.0.0.0 | 16.777.216| 16.777.214|
---

## Bilanciamento del carico e proxy inversi
### Nginx come proxy inverso
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

### Algoritmi di bilanciamento del carico
- **Girone all'italiana**
- **Minimo connessioni**
- **Hash IP** (persistenza della sessione)
- **Girone all'italiana ponderato**
### Utensili
- **Nginx, HAProxy** (software)
- **AWS ELB, bilanciatore del carico di Azure, bilanciamento del carico sul cloud GCP** (cloud)
---

## Elenco di controllo per la risoluzione dei problemi
1. Il collegamento fisico è attivo? (Controllare cavi, connessione Wi-Fi).
2. È possibile eseguire il ping del gateway? (ad esempio,`ping 192.168.1.1`).
3. È possibile eseguire il ping di un IP esterno? (ad esempio,`8.8.8.8`).
4. Puoi risolvere un dominio? (`dig google.com`).
5. L'applicazione è in ascolto sulla porta prevista? (`ss -tulpn | grep 8080`).
6. Il firewall sta bloccando la porta? (Controlla`iptables`/`ufw`o i gruppi di sicurezza cloud).
7. Sono presenti errori nei registri dell'applicazione?
8. Il certificato TLS è valido e affidabile? (`openssl s_client -connect example.com:443`).