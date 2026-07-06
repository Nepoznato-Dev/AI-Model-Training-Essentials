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
- Indirizzo a 32 bit, scritto come quattro ottetti: `192.168.1.1`
- Totale: ~4,3 miliardi di indirizzi (ma in pratica esauriti).

### IPv6
- Indirizzo a 128 bit, scritto in esadecimale: `2001:0db8:85a3:0000:0000:8a2e:0370:7334`
- Totale: 2¹²⁸ indirizzi (praticamente infiniti).

### Intervalli IP privati (RFC 1918)
Questi non sono instradabili su Internet; utilizzato all'interno delle reti locali:
- `10.0.0.0/8` (10.0.0.0 – 10.255.255.255)
- `172.16.0.0/12` (172.16.0.0 – 172.31.255.255)
- `192.168.0.0/16` (192.168.0.0 – 192.168.255.255)

### Notazione CIDR
`192.168.1.0/24` significa che i primi 24 bit sono il prefisso di rete; gli ultimi 8 bit sono host. Include gli indirizzi da `192.168.1.0` a `192.168.1.255`.

---

## DNS (sistema dei nomi di dominio)

Associa i nomi di dominio (ad esempio, `example.com`) agli indirizzi IP.

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

### Strumenti comuni
```bash
dig example.com            # DNS lookup (detailed)
nslookup example.com       # DNS lookup (simpler)
host example.com           # Quick lookup
dig -x 8.8.8.8             # Reverse lookup (IP to name)

Ports and Protocols
Well-Known Ports (0–1023)
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
Check open ports
bash
ss -tulpn                 # Linux: listen and established sockets
netstat -an               # Older tool
lsof -i :8080             # See process using port 8080
nmap localhost            # Scan local ports
TCP vs UDP
Feature	TCP	UDP
Connection	Connection-oriented (handshake)	Connectionless
Reliability	Guaranteed delivery, retransmission	Best effort (may drop packets)
Ordering	Preserves order	No ordering guarantee
Flow control	Yes (sliding window)	No
Use cases	Web (HTTP), email, SSH, file transfer	DNS, streaming, VoIP, gaming, SNMP
Header size	20–60 bytes	8 bytes
HTTP and HTTPS
HTTP Methods
GET: Retrieve a resource (idempotent, safe).

POST: Submit data (not idempotent).

PUT: Update/replace a resource (idempotent).

PATCH: Partial update.

DELETE: Remove a resource (idempotent).

Status Codes
1xx: Informational (100 Continue).

2xx: Success (200 OK, 201 Created, 204 No Content).

3xx: Redirection (301 Moved Permanently, 302 Found, 304 Not Modified).

4xx: Client error (400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found, 429 Too Many Requests).

5xx: Server error (500 Internal Server Error, 502 Bad Gateway, 503 Service Unavailable).

Headers
Content-Type: media type (application/json, text/html).

Authorization: credentials (e.g., Bearer <token>).

Cache-Control: caching policy.

CORS headers: Access-Control-Allow-Origin, etc.

TLS/SSL
Encrypts HTTP traffic (HTTPS = HTTP over TLS).

Certificates from Certificate Authorities (CAs) authenticate the server.

Verify certificate chain and hostname on the client side.

Firewalls and NAT
Firewall
Filters traffic based on rules (source IP, dest IP, port, protocol).

Stateful firewalls track connection states.

NAT (Network Address Translation)
Translates private IPs to a public IP for internet access.

Port forwarding: maps a public port to an internal host/port.

Common Networking Commands
Connectivity Tests
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
Network Interfaces
bash
ip addr show               # List interfaces and IPs
ifconfig                   # Older command
DNS
bash
dig example.com
nslookup example.com
host example.com
Connectivity to a Port
bash
nc -zv google.com 443      # Netcat: check if port 443 is open
telnet google.com 443      # Telnet to port
curl -v https://google.com # Verbose output
Firewall (Linux iptables/nftables)
bash
sudo ufw status            # Ubuntu: simple firewall
sudo iptables -L -n        # List rules
Network Statistics
bash
ss -tulpn                  # Show listening sockets (Linux)
netstat -an                # All sockets (all OS)
Subnetting (Quick Reference)
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
Nginx as Reverse Proxy
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
Load Balancing Algorithms
Round-robin

Least connections

IP hash (session stickiness)

Weighted round-robin

Tools
Nginx, HAProxy (software)

AWS ELB, Azure Load Balancer, GCP Cloud Load Balancing (cloud)

Troubleshooting Checklist
Is the physical link up? (Check cables, Wi-Fi connection).

Can you ping the gateway? (e.g., ping 192.168.1.1).

Can you ping an external IP? (e.g., 8.8.8.8).

Can you resolve a domain? (dig google.com).

Is the application listening on the expected port? (ss -tulpn | grep 8080).

Is the firewall blocking the port? (Check iptables/ufw or cloud security groups).

Are there any errors in the application logs?

Is TLS certificate valid and trusted? (openssl s_client -connect example.com:443).

text

---

## File 6: `devops_sysadmin.md`

```ribasso
# DevOps e amministrazione di sistema

Una guida pratica alla gestione dei server, all'automazione delle operazioni e al mantenimento dell'affidabilità dell'infrastruttura.

---

## SSH (Secure Shell)

### Generazione di chiavi
"bash."
ssh-keygen -t ed25519 -C "tua_email@esempio.com" # Moderno e sicuro
ssh-keygen -t rsa -b 4096 -C "tua_email@esempio.com" # Fallback
Copia la chiave pubblica sul server
bash
ssh-copy-id utente@host
# Alternativa manuale:
cat ~/.ssh/id_ed25519.pub | ssh utente@host "mkdir -p ~/.ssh && cat >> ~/.ssh/authorized_keys"
Configurazione SSH (~/.ssh/config)
ssh-config
Ospita il mioserver
    Nome host 192.168.1.10
    Utente Ubuntu
    FileIdentità ~/.ssh/mykey
    Porto 2222
Comandi SSH comuni
bash
ssh utente@host # Connetti
ssh -J utentejump@utentejumphost@destinazione # Salto proxy
scp file.txt utente@host:/percorso/ # Copia il file sul remoto
scp utente@host:/percorso/file.txt .    # Copia da remoto
rsync -avz -e ssh ./local/ utente@host:/remoto/ # Sincronizzazione efficiente
Rafforzamento di SSH
Disabilita accesso root: PermitRootLogin no

Utilizza solo l'autenticazione basata su chiave: PasswordAuthentication no

Modifica la porta predefinita (opzionale, sicurezza attraverso l'oscurità).

Abilita PermettereUtenti o ConsentiGruppi per limitare l'accesso.

Systemd (gestione dei servizi Linux)
Comandi comuni
bash
systemctl status nginx # Controlla lo stato del servizio
systemctl start nginx # Avvia il servizio
systemctl arresta nginx
systemctl riavvia nginx
systemctl ricarica nginx # Ricarica con grazia (rileggi la configurazione)
systemctl abilita nginx # Avvia all'avvio
systemctl disabilita nginx
systemctl list-units --type=service --all # Elenca tutti i servizi
systemctl daemon-reload # Ricarica i file dell'unità dopo la modifica
Creazione di un'unità di servizio systemd
Crea /etc/systemd/system/myapp.service:

ini
[Unità]
Descrizione=La mia app Python
Dopo=rete.destinazione

[Servizio]
Utente=mioutente
Gruppo=miogruppo
Directory di lavoro=/opt/miaapp
ExecStart=/usr/bin/python3 /opt/myapp/main.py
Riavvia=sempre
RiavvioSec=10
Ambiente="ENV=produzione"

[Installa]
WantedBy=multi-utente.target
Quindi:

bash
sudo systemctl daemon-reload
sudo systemctl abilita miaapp
sudo systemctl avvia la mia app
Journalctl (Visualizza registri)
bash
journalctl -u miaapp # Registra il servizio
journalctl -f # Segui i log (coda).
journalctl --da "1 ora fa"
journalctl_PID=1234 # Filtra per ID processo
Strategie di registrazione
Registrazione strutturata
Utilizza il formato JSON per rendere i log analizzabili dal computer:

pitone
importare il log di struttura
logger = structlog.get_logger()
logger.info("user_login", user_id=123, ip="192.168.1.1")
Livelli di registro
DEBUG: diagnostica dettagliata.

INFO: eventi generali (inizio, fine, transazioni normali).

ATTENZIONE: inaspettato ma non fatale.

ERRORE: errore che impedisce una determinata operazione.

FATALE/CRITICO: arresto del sistema.

Aggregazione dei registri
ELK Stack (Elasticsearch, Logstash, Kibana) o Elastic Cloud.Loki + Grafana (alternativa leggera).

Datadog, Splunk, Sumo Logic (SaaS).

Rotazione del registro (logrotate)
Evita che i log riempiano i dischi. Configura /etc/logrotate.d/myapp:

logrotate
/var/log/miaapp/*.log {
    quotidiano
    ruotare 7
    comprimere
    ritardocompress
    mancanteok
    notifempty
    crea 0640 mioutente miogruppo
}
Monitoraggio e avvisi
Metriche da monitorare
Sistema: CPU, RAM, utilizzo del disco, carico medio, I/O di rete.

Applicazione: tasso di richieste, latenza (p50, p95, p99), tasso di errore, sessioni attive.

Database: conteggio delle query, query lente, utilizzo del pool di connessioni.

Business: iscrizioni degli utenti, tasso di conversione, entrate.

Strumenti
Prometeo + Grafana: stack open source standard.

Esportatore di nodi per le metriche di sistema.

Blackbox Exporter per la disponibilità degli endpoint.

Alertmanager per l'instradamento degli avvisi.

Nativo del cloud: AWS CloudWatch, monitoraggio di Azure, monitoraggio GCP.

Monitoraggio dei tempi di attività
Pingdom, Statuspage, Better Uptime, Uptime Kuma (auto-ospitato).

Controlli di integrità: esponi un endpoint /health che restituisce 200 se il servizio è integro.

Strategie di backup
La regola del 3-2-1
3 copie dei dati.

2 diversi tipi di supporto (ad esempio, SSD + nastro o locale + cloud).

1 copia off-site (ad esempio, cloud o data center remoto).

Tipi di backup
Backup completo: copia tutto (lento, occupa molto spazio).

Backup incrementale: copia solo le modifiche dall'ultimo backup completo o incrementale (ripristino rapido e complesso).

Backup differenziale: copia le modifiche dall'ultimo completamento (via di mezzo).

Backup del database
bash
#PostgreSQL
pg_dump nomedb > backup.sql
pg_dumpall > all_backup.sql

#MySQL/MariaDB
mysqldump -u root -p nomedb > backup.sql

#Ripristina
psql nomedb < backup.sql
mysql -u root -p nomedb < backup.sql
Backup dei file
bash
# Archivio Tar
tar -czf backup.tar.gz /var/lib/data

# Rsync al remoto
rsync -avz /local/dati/ utente@server-backup:/backup/dati/

# Cloud CLI (ad esempio, AWS S3)
aws s3 sync /local/data s3://mio-bucket/backup/
Pianificazione backup automatizzata (cron)
cron
# Corri tutti i giorni alle 2 del mattino
0 2 * * * /usr/local/bin/backup_script.sh
Cron e lavori pianificati
Sintassi Cron
testo
* * * * * comando
│ │ │ │ │
│ │ │ │ └─ Giorno della settimana (0-7, 0=Domenica)
│ │ │ └─── Mese (1-12)
│ │ └───── Giorno del mese (1-31)
│ └─────── Ora (0-23)
└───────── Minuto (0-59)
Esempi
cron
# Ogni 5 minuti
*/5 * * * * /percorso/dello/script

# Tutti i giorni alle 3:15
15 3 * * * /percorso/dello/script

# Ogni lunedì alle 4 del mattino
0 4 * * 1 /percorso/dello/script

# Ogni ora
0 * * * * /percorso/dello/script
Gestione Cron
bash
crontab -l # Elenca i processi cron dell'utente corrente
crontab -e # Modifica
crontab -r # Rimuove tutto
Anacron
Utilizzato per i sistemi non in esecuzione 24 ore su 24, 7 giorni su 7 (ad esempio, laptop), garantisce che i lavori vengano eseguiti alla fine.

Gestione dei pacchetti e aggiornamenti
Debian/Ubuntu (adatto)
bash
sudo apt update # Aggiorna l'elenco dei pacchetti
sudo apt upgrade # Aggiorna tutti i pacchetti
sudo apt installa git nginx
sudo apt rimuovi git
sudo apt autoremove # Rimuove le dipendenze inutilizzate
RHEL/CentOS/Fedora (dnf/yum)
bash
sudo dnf verifica aggiornamento
aggiornamento sudo dnf
sudo dnf installa git nginx
sudo dnf rimuovi git
Aggiornamenti di sicurezza
Abilita gli aggiornamenti automatici su Ubuntu per le patch di sicurezza:

bash
sudo apt installa aggiornamenti automatici
sudo dpkg-reconfigure -plow aggiornamenti non presidiati
Docker in produzione
Migliori pratiche
Utilizza tag immagine specifici (python:3.12-slim) non più recenti.

Esegui i contenitori come utente non root.

Scansiona le immagini per individuare eventuali vulnerabilità (scansione docker, banalità).

Imposta i limiti delle risorse (--memory, --cpus).

Utilizzare i segreti (tramite i segreti Docker o l'ambiente con attenzione).

Mantieni le immagini piccole: costruzioni in più fasi, base alpina.

Docker Compose in produzione
Imposta i limiti delle risorse in docker-compose.yml:

yaml
servizi:
  applicazione:
    immagine: miaapp:1.0
    distribuire:
      risorse:
        limiti:
          memoria: 512 MB
          CPU: '0,5'
Nozioni di base su CI/CD
Fasi della pipeline
Compila: compila il codice, installa le dipendenze.

Test: eseguire controlli di unità, integrazione e lanugine.

Containerizzazione: crea un'immagine Docker.

Push: invia l'immagine al registro contenitori.

Distribuisci: aggiorna l'ambiente di gestione temporanea/produzione.

Strumenti
Azioni GitHub: integrato con GitHub.

CI GitLab: integrato in GitLab.

Jenkins: tradizionale, altamente configurabile.

CircleCI, Travis CI: terza parte popolare.

ArgoCD: GitOps per Kubernetes.Esempio di azione GitHub (semplice):
yaml
nome: CI
acceso: spingere
lavori:
  costruire:
    funziona su: ubuntu-latest
    passaggi:
      - utilizza: azioni/checkout@v4
      - utilizza: actions/setup-python@v5
        con:
          versione Python: '3.12'
      - esegui: pip install -r requisiti.txt
      - esegui: pytest
Ottimizzazione del sistema e risoluzione dei problemi
Controlla lo spazio su disco
bash
df -h # Utilizzo del disco leggibile dall'uomo
du -sh /* | sort -h # Dimensione delle directory di livello superiore
Controlla l'utilizzo della memoria
bash
free -m # Memoria in MB
vmstat 1 10 # Statistiche sulla memoria virtuale
top -o %MEM # Ordina i processi per memoria
Controllare il carico della CPU
bash
uptime # Carica media su 1,5,15 minuti
top -o %CPU # Ordina i processi per CPU
mpstat -P ALL 1 5 # Utilizzo della CPU per core
Controlla la rete
bash
netstat -i # Statistiche dell'interfaccia
iftop # Utilizzo della larghezza di banda in tempo reale (richiede l'installazione)
nload # Un altro monitor della larghezza di banda
Trova file di grandi dimensioni
bash
trova / -tipo f -size +100M -exec ls -lh {} \; 2>/dev/null
Infrastruttura come codice (IaC)
Terraformare
Dichiarare le risorse cloud in HCL.

hcl
fornitore "aws" {
  regione = "noi-est-1"
}
risorsa "aws_instance" "web" {
  ami = "ami-0c55b159cbfafe1f0"
  tipo_istanza = "t2.micro"
}
Ansible
Gestione della configurazione senza agente tramite YAML.

yaml
- nome: installa nginx
  host: server web
  compiti:
    - nome: installa nginx
      adatto:
        nome: nginx
        stato: presente
Migliori pratiche
Utilizzare moduli e ruoli per la riusabilità.

Archivia lo stato in remoto (S3, Terraform Cloud).

Utilizza variabili e segreti (AWS_SECRET_ACCESS_KEY tramite ambiente, non hardcoded).

Controlla la versione del tuo codice IaC.

Risposta agli incidenti (su chiamata)
Lista di controllo per l'interruzione del servizio
Riconoscere l'avviso.

Valutare l'ambito: quali servizi/utenti sono interessati?

Identificare il problema (guardare log, parametri, distribuzioni recenti).

Contenere se possibile (interruttori automatici, flag di funzionalità).

Rollback o correzione in avanti.

Comunicare lo stato alle parti interessate e agli utenti (pagina stato).

Documentare la sequenza temporale e le azioni dell'incidente.

Autopsia: entro 24-48 ore, scrivere un'analisi della causa principale (RCA) e azioni da intraprendere per prevenire il ripetersi.