# Podstawy sieci

Praktyczny podręcznik dla programistów i administratorów systemu — podstawowe pojęcia, protokoły, polecenia i rozwiązywanie problemów.

---

## Model OSI (7 warstw)

Ramy koncepcyjne dla zrozumienia komunikacji sieciowej.

| Warstwa | Imię | Funkcja | Przykładowe protokoły |
|-------|------|----------|--------------------------------|
| 7 | Aplikacja | Usługi dla użytkowników końcowych | HTTP, HTTPS, FTP, SMTP, DNS, SSH |
| 6 | Prezentacja | Formatowanie danych, szyfrowanie, kompresja | TLS, JPEG, ASCII |
| 5 | Sesja | Zarządzanie połączeniami | NetBIOS, RPC |
| 4 | Transport | Dostawa od końca do końca, korekcja błędów, kontrola przepływu | TCP, UDP |
| 3 | Sieć | Routing, adresowanie | IP, ICMP, OSPF, BGP |
| 2 | Łącze danych | Ramkowanie, wykrywanie błędów, adresy MAC | Ethernet, Wi-Fi, PPP |
| 1 | Fizyczne | Transmisja surowego bitu | Kable Ethernet, światłowód, fale radiowe |

W praktyce w Internecie częściej stosowany jest **model TCP/IP** (4 warstwy: łącze, Internet, transport, aplikacja).

---

## Adresowanie IP

### IPv4
- 32-bitowy adres zapisany w postaci czterech oktetów: `192.168.1.1`
- Razem: ~4,3 miliarda adresów (ale w praktyce wyczerpane).

### IPv6
- Adres 128-bitowy, zapisany w formacie szesnastkowym: `2001:0db8:85a3:0000:0000:8a2e:0370:7334`
- Łącznie: 2¹²⁸ adresów (praktycznie nieskończona liczba).

### Zakresy prywatnych adresów IP (RFC 1918)
Nie można ich trasować w Internecie; używany w sieciach lokalnych:
- `10.0.0.0/8` (10.0.0.0 – 10.255.255.255)
- `172.16.0.0/12` (172.16.0.0 – 172.31.255.255)
- `192.168.0.0/16` (192.168.0.0 – 192.168.255.255)

### Notacja CIDR
`192.168.1.0/24` oznacza, że pierwsze 24 bity to prefiks sieci; ostatnie 8 bitów to hosty. Zawiera adresy `192.168.1.0` do `192.168.1.255`.

---

## DNS (system nazw domen)

Mapuje nazwy domen (np. `example.com`) na adresy IP.

### Typy rekordów
| Wpisz | Cel |
|------|-------------|
| **A** | Mapuje domenę na adres IPv4 |
| **AAAA** | Mapuje domenę na adres IPv6 |
| **NAZWA** | Alias ​​do innej nazwy domeny |
| **MX** | Serwer wymiany poczty |
| **TXT** | Dowolny tekst (SPF, DKIM, weryfikacja) |
| **NS** | Serwer nazw dla domeny |
| **SRV** | Historia służby (np. dla SIP) |

### Typowe narzędzia
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

```przecena
# DevOps i administracja systemem

Praktyczny przewodnik po zarządzaniu serwerami, automatyzacji operacji i utrzymywaniu niezawodnej infrastruktury.

---

## SSH (bezpieczna powłoka)

### Generowanie klucza
,,bicie
ssh-keygen -t ed25519 -C "twój_email@example.com" # Nowoczesny i bezpieczny
ssh-keygen -t rsa -b 4096 -C "twój_e-mail@example.com" # Rozwiązanie awaryjne
Skopiuj klucz publiczny na serwer
walnąć
ssh-copy-id użytkownik@host
# Alternatywa ręczna:
kot ~/.ssh/id_ed25519.pub | ssh użytkownik@host "mkdir -p ~/.ssh && cat >> ~/.ssh/authorized_keys"
Konfiguracja SSH (~/.ssh/config)
konfiguracja ssh
Hostuj mój serwer
    Nazwa hosta 192.168.1.10
    Użytkownik Ubuntu
    Plik tożsamości ~/.ssh/mykey
    Port 2222
Typowe polecenia SSH
walnąć
ssh użytkownik@host # Połącz
ssh -J jumpuser@jumphost użytkownik@target # Skok proxy
scp plik.txt użytkownik@host:/ścieżka/ # Skopiuj plik do zdalnego
scp użytkownik@host:/ścieżka/plik.txt .    # Skopiuj z pilota
rsync -avz -e ssh ./local/ użytkownik@host:/remote/ # Wydajna synchronizacja
Hartowanie SSH
Wyłącz logowanie roota: PermitRootLogin no

Używaj tylko uwierzytelniania na podstawie klucza: HasłoNr uwierzytelnienia

Zmień domyślny port (opcjonalnie, bezpieczeństwo poprzez zaciemnienie).

Włącz opcję ZezwólUżytkownikom lub ZezwólGroupom, aby ograniczyć dostęp.

Systemd (zarządzanie usługami Linux)
Wspólne polecenia
walnąć
systemctl status nginx # Sprawdź status usługi
systemctl start nginx # Uruchom usługę
systemctl zatrzymaj nginx
systemctl uruchom ponownie Nginx
systemctl reload nginx # Ładne przeładowanie (przeczytaj ponownie konfigurację)
systemctl włącz nginx # Uruchom przy starcie
systemctl wyłącz nginx
systemctl list-units --type=service --all # Wyświetla listę wszystkich usług
systemctl daemon-reload # Załaduj ponownie pliki jednostek po edycji
Tworzenie systemowej jednostki usługowej
Utwórz /etc/systemd/system/myapp.service:

ini
[Jednostka]
Opis=Moja aplikacja w języku Python
Po=sieć.cel

[Usługa]
Użytkownik=mójużytkownik
Grupa=mojagrupa
WorkingDirectory=/opt/mojaaplikacja
ExecStart=/usr/bin/python3 /opt/myapp/main.py
Uruchom ponownie = zawsze
Uruchom ponownieSek=10
Środowisko="ENV=produkcja"

[Zainstaluj]
WantedBy=wielu użytkowników.target
Następnie:

walnąć
sudo systemctl demon-reload
sudo systemctl włącz moją aplikację
sudo systemctl uruchom moją aplikację
Journalctl (wyświetl logi)
walnąć
journalctl -u myapp # Dzienniki usługi
journalctl -f # Śledź (ogon) logi
journalctl --od „1 godzinę temu”
journalctl _PID=1234 # Filtruj według identyfikatora procesu
Strategie rejestrowania
Logowanie strukturalne
Użyj formatu JSON, aby umożliwić analizę maszynową dzienników:

pyton
zaimportuj dziennik struktur
logger = structlog.get_logger()
logger.info("logowanie_użytkownika", id_użytkownika=123, ip="192.168.1.1")
Poziomy dziennika
DEBUG: szczegółowa diagnostyka.

INFORMACJE: zdarzenia ogólne (start, stop, normalne transakcje).

OSTRZEŻENIE: nieoczekiwane, ale nie śmiertelne.

BŁĄD: błąd uniemożliwiający wykonanie określonej operacji.

KRYTYCZNY/KRYTYCZNY: zamknięcie systemu.

Agregacja dziennika
ELK Stack (Elasticsearch, Logstash, Kibana) lub Elastic Cloud.Loki + Grafana (lekka alternatywa).

Datadog, Splunk, Sumo Logic (SaaS).

Obrót kłody (logrotat)
Zapobiegaj zapełnianiu dysków przez dzienniki. Skonfiguruj /etc/logrotate.d/myapp:

logrotat
/var/log/myapp/*.log {
    codziennie
    obrócić 7
    kompresować
    opóźnij kompresję
    brak ok
    powiadomieniepuste
    utwórz 0640 myuser moja grupa
}
Monitorowanie i ostrzeganie
Metryki do monitorowania
System: procesor, pamięć RAM, wykorzystanie dysku, średnie obciążenie, we/wy sieci.

Zastosowanie: częstotliwość żądań, opóźnienie (p50, p95, p99), stopa błędów, aktywne sesje.

Baza danych: liczba zapytań, powolne zapytania, wykorzystanie puli połączeń.

Biznes: rejestracje użytkowników, współczynnik konwersji, przychody.

Narzędzia
Prometheus + Grafana: standardowy stos open source.

Eksporter węzłów dla metryk systemowych.

Eksporter Blackbox zapewniający dostępność punktów końcowych.

Menedżer alertów do routingu alertów.

Natywna chmura: AWS CloudWatch, Azure Monitor, monitorowanie GCP.

Monitorowanie czasu pracy
Pingdom, strona stanu, lepszy czas działania, czas działania Kuma (własny hosting).

Kontrole kondycji: udostępniaj punkt końcowy /health, który zwraca 200, jeśli usługa jest w dobrej kondycji.

Strategie tworzenia kopii zapasowych
Zasada 3-2-1
3 kopie danych.

2 różne typy nośników (np. SSD + taśma lub lokalny + chmura).

1 kopia poza siedzibą firmy (np. w chmurze lub zdalnym centrum danych).

Typy kopii zapasowych
Pełna kopia zapasowa: skopiuj wszystko (powolne, zajmujące dużo miejsca).

Przyrostowa kopia zapasowa: kopiuj tylko zmiany od ostatniej pełnej lub przyrostowej kopii zapasowej (szybkie, złożone przywracanie).

Kopia różnicowa: kopiuj zmiany od ostatniego zapełnienia (środek).

Kopie zapasowe baz danych
walnąć
#PostgreSQL
pg_dump nazwa_bazy danych > kopia zapasowa.sql
pg_dumpall > all_backup.sql

#MySQL/MariaDB
mysqldump -u root -p nazwa bazy danych > kopia zapasowa.sql

# Przywróć
nazwa bazy danych psql < kopia zapasowa.sql
mysql -u root -p nazwa bazy danych < kopia zapasowa.sql
Kopie zapasowe plików
walnąć
# Archiwum tar
tar -czf kopia zapasowa.tar.gz /var/lib/data

# Rsync do pilota
rsync -avz /local/data/ użytkownik@backup-server:/backup/data/

# Cloud CLI (np. AWS S3)
aws s3 sync /local/data s3://my-bucket/backup/
Automatyczne planowanie kopii zapasowych (cron)
cron
# Uruchamiaj codziennie o 2 w nocy
0 2 * * * /usr/local/bin/backup_script.sh
Cron i zaplanowane zadania
Składnia Crona
tekst
* * * * * polecenie
│ │ │ │ │
│ │ │ │ └─ Dzień tygodnia (0-7, 0=niedziela)
│ │ │ └─── Miesiąc (1-12)
│ │ └───── Dzień miesiąca (1-31)
│ └─────── Godzina (0-23)
└───────── Minuta (0-59)
Przykłady
cron
# Co 5 minut
*/5 * * * * /ścieżka/do/skryptu

# Codziennie o 3:15
15 3 * * * /ścieżka/do/skryptu

# W każdy poniedziałek o 4 rano
0 4 * * 1 /ścieżka/do/skryptu

# Co godzinę
0 * * * * /ścieżka/do/skryptu
Zarządzanie Cronem
walnąć
crontab -l # Wyświetla zadania cron bieżącego użytkownika
crontab -e # Edytuj
crontab -r # Usuń wszystko
Anakron
Używany w systemach, które nie działają 24 godziny na dobę, 7 dni w tygodniu (np. laptopach), zapewnia ostateczne wykonanie zadań.

Zarządzanie pakietami i aktualizacje
Debian/Ubuntu (apt)
walnąć
sudo apt update # Zaktualizuj listę pakietów
sudo apt upgrade # Zaktualizuj wszystkie pakiety
sudo apt zainstaluj git nginx
sudo apt usuń git
sudo apt autorove # Usuń nieużywane zależności
RHEL/CentOS/Fedora (dnf/mniam)
walnąć
Aktualizacja sprawdzania sudo dnf
aktualizacja sudo dnf
sudo dnf zainstaluj git nginx
sudo dnf usuń git
Aktualizacje zabezpieczeń
Włącz aktualizacje nienadzorowane w systemie Ubuntu w celu uzyskania poprawek zabezpieczeń:

walnąć
sudo apt install unattended-upgrades
sudo dpkg-reconfigure -plow unattended-upgrades
Docker w produkcji
Najlepsze praktyki
Użyj określonych tagów obrazu (python:3.12-slim), a nie najnowszych.

Uruchamiaj kontenery jako użytkownik inny niż root.

Skanuj obrazy w poszukiwaniu luk w zabezpieczeniach (skanowanie okna dokowanego, trivy).

Ustaw limity zasobów (--memory, --cpus).

Ostrożnie używaj wpisów tajnych (poprzez sekrety Dockera lub środowisko).

Staraj się, aby obrazy były małe: wieloetapowe kompilacje, baza alpejska.

Docker Compose w produkcji
Ustaw limity zasobów w pliku docker-compose.yml:

yaml
usługi:
  aplikacja:
    obraz: mojaaplikacja:1.0
    wdrożyć:
      zasoby:
        limity:
          pamięć: 512M
          procesor: „0,5”
Podstawy CI/CD
Etapy rurociągu
Kompilacja: Skompiluj kod, zainstaluj zależności.

Testuj: uruchom testy jednostkowe, integracyjne i lintowe.

Konteneryzacja: Zbuduj obraz Dockera.

Wypychanie: wypychanie obrazu do rejestru kontenerów.

Wdrożenie: zaktualizuj środowisko przejściowe/produkcyjne.

Narzędzia
Akcje GitHub: Zintegrowane z GitHub.

GitLab CI: Wbudowany w GitLab.

Jenkins: tradycyjny, wysoce konfigurowalny.

CircleCI, Travis CI: popularne strony trzecie.

ArgoCD: GitOps dla Kubernetesa.Przykładowa akcja GitHub (prosta):
yaml
nazwa: CI
wł.: pchnij
praca:
  zbuduj:
    działa: Ubuntu-latest
    kroki:
      - używa: akcje/checkout@v4
      - używa: action/setup-python@v5
        z:
          wersja Pythona: „3.12”
      - uruchom: pip install -r wymagania.txt
      - uruchom: pytest
Strojenie systemu i rozwiązywanie problemów
Sprawdź miejsce na dysku
walnąć
df -h # Użycie dysku czytelne dla człowieka
du -sh /* | sort -h # Rozmiar katalogów najwyższego poziomu
Sprawdź użycie pamięci
walnąć
free -m # Pamięć w MB
vmstat 1 10 # Statystyki pamięci wirtualnej
top -o %MEM # Sortuj procesy według pamięci
Sprawdź obciążenie procesora
walnąć
uptime # Średnie obciążenie w ciągu 1,5,15 minut
top -o %CPU # Sortuj procesy według procesora
mpstat -P ALL 1 5 # Użycie procesora na rdzeń
Sprawdź sieć
walnąć
netstat -i # Statystyki interfejsu
iftop # Wykorzystanie przepustowości na żywo (wymaga instalacji)
nload # Kolejny monitor przepustowości
Znajdź duże pliki
walnąć
znajdź / -wpisz f -rozmiar +100M -exec ls -lh {} \; 2>/dev/null
Infrastruktura jako kod (IaC)
Terraforma
Zadeklaruj zasoby chmury w HCL.

hcl
dostawca „och” {
  region = „us-wschód-1”
}
zasób „aws_instance” „web” {
  ami = "ami-0c55b159cbfafe1f0"
  typ_instancji = "t2.micro"
}
Ansible
Bezagentowe zarządzanie konfiguracją przy użyciu YAML.

yaml
- nazwa: Zainstaluj nginx
  hosty: serwery internetowe
  zadania:
    - nazwa: Zainstaluj nginx
      trafny:
        nazwa: Nginx
        stan: obecny
Najlepsze praktyki
Używaj modułów i ról do ponownego użycia.

Zdalny stan przechowywania (S3, Terraform Cloud).

Używaj zmiennych i sekretów (AWS_SECRET_ACCESS_KEY za pośrednictwem środowiska, a nie zakodowanych na stałe).

Kontrola wersji Twojego kodu IaC.

Reagowanie na incydenty (na wezwanie)
Lista kontrolna w przypadku awarii usługi
Potwierdź alert.

Oceń zakres: jakich usług/użytkowników dotyczy problem?

Zidentyfikuj problem (przejrzyj logi, metryki, ostatnie wdrożenia).

Jeśli to możliwe, należy uwzględnić (wyłączniki automatyczne, flagi funkcji).

Cofnij lub napraw do przodu.

Przekaż status zainteresowanym stronom i użytkownikom (strona statusu).

Udokumentuj harmonogram zdarzenia i działania.

Sekcja zwłok: w ciągu 24–48 godzin sporządź analizę pierwotnej przyczyny (RCA) i określ działania, aby zapobiec nawrotom.