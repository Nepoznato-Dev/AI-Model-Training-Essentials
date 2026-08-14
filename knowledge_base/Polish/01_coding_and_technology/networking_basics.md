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
- Adres 32-bitowy zapisany w postaci czterech oktetów:`192.168.1.1`
- Razem: ~4,3 miliarda adresów (ale w praktyce wyczerpane).
### IPv6
- Adres 128-bitowy, zapisany w formacie szesnastkowym:`2001:0db8:85a3:0000:0000:8a2e:0370:7334`
- Łącznie: 2¹²⁸ adresów (praktycznie nieskończona liczba).
### Zakresy prywatnych adresów IP (RFC 1918)
Nie można ich trasować w Internecie; używany w sieciach lokalnych:
-`10.0.0.0/8`(10.0.0.0 – 10.255.255.255)
-`172.16.0.0/12`(172.16.0.0 – 172.31.255.255)
-`192.168.0.0/16`(192.168.0.0 – 192.168.255.255)
### Notacja CIDR
`192.168.1.0/24`oznacza, że pierwsze 24 bity to prefiks sieci; ostatnie 8 bitów to hosty. Zawiera adresy od`192.168.1.0`do`192.168.1.255`.
---

## DNS (system nazw domen)
Mapuje nazwy domen (np.`example.com`) na adresy IP.
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
### Typowe narzędzia```bash
dig example.com            # DNS lookup (detailed)
nslookup example.com       # DNS lookup (simpler)
host example.com           # Quick lookup
dig -x 8.8.8.8             # Reverse lookup (IP to name)
```

---

## Porty i protokoły
### Dobrze znane porty (0–1023)
| Port | Protokół | Usługa |
|------|----------|--------|
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
| 587 | TCP | SMTP (złożenie) |
| 993 | TCP | IMAPY |
| 995 | TCP | POP3S |
| 3306 | TCP | MySQL |
| 5432 | TCP | PostgreSQL |
| 6379 | TCP | Redis |
| 27017 | TCP | MongoDB |
### Sprawdź otwarte porty
```bash
ss -tulpn                 # Linux: listen and established sockets
netstat -an               # Older tool
lsof -i :8080             # See process using port 8080
nmap localhost            # Scan local ports
```

---

## TCP kontra UDP
| Funkcja | TCP | UDP |
|--------|-----|-----|
| Połączenie | Zorientowany na połączenie (uzgadnianie) | Bezpołączeniowy |
| Niezawodność | Gwarantowana dostawa, retransmisja | Najlepszy wysiłek (może upuścić pakiety) |
| Zamawianie | Zachowuje porządek | Brak gwarancji zamówienia |
| Kontrola przepływu | Tak (przesuwane okno) | Nie |
| Przypadki użycia | WWW (HTTP), e-mail, SSH, transfer plików | DNS, streaming, VoIP, gry, SNMP |
| Rozmiar nagłówka | 20–60 bajtów | 8 bajtów |
---

## HTTP i HTTPS
### Metody HTTP
| Metoda | Opis |
|------------|------------|
| **DOBIERZ** | Odzyskaj zasób (idempotentny, bezpieczny) |
| **POST** | Prześlij dane (nie idempotentne) |
| **UMIEŚĆ** | Aktualizuj/zamień zasób (idempotent) |
| **ŁATKA** | Częściowa aktualizacja |
| **USUŃ** | Usuń zasób (idempotent) |
### Kody stanu
| Kod | Znaczenie |
|------|-------------|
| **1xx** | Informacyjne (100 Kontynuuj) |
| **2xx** | Sukces (200 OK, 201 Utworzono, 204 Brak treści) |
| **3xx** | Przekierowanie (301 przeniesione na stałe, 302 znalezione, 304 niezmodyfikowane) |
| **4xx** | Błąd klienta (400 nieprawidłowe żądanie, 401 nieautoryzowane, 403 zabronione, 404 nie znaleziono, 429 za dużo żądań) |
| **5xx** | Błąd serwera (500 Wewnętrzny błąd serwera, 502 Zła brama, 503 Usługa niedostępna) |
### Nagłówki
| Nagłówek | Cel |
|------------|--------|
| `Content-Type`| Typ nośnika (`application/json`,`text/html`) |
| `Authorization`| Poświadczenia (np.`Bearer <token>`) |
| `Cache-Control`| Polityka buforowania |
| Nagłówki CORS | `Access-Control-Allow-Origin`itp. |
---

## TLS/SSL
Szyfruje ruch HTTP (HTTPS = HTTP przez TLS).
- Certyfikaty z urzędów certyfikacji (CA) uwierzytelniają serwer.
- Sprawdź łańcuch certyfikatów i nazwę hosta po stronie klienta.
---

## Zapory sieciowe i NAT
### Zapora sieciowa
- Filtruje ruch w oparciu o reguły (źródłowy adres IP, docelowy adres IP, port, protokół).
- Zapory stanowe śledzą stany połączeń.
### NAT (tłumaczenie adresów sieciowych)
- Tłumaczy prywatne adresy IP na publiczne adresy IP w celu uzyskania dostępu do Internetu.
- Przekierowanie portów: mapuje port publiczny na wewnętrzny host/port.
---

## Typowe polecenia sieciowe
### Testy łączności
```bash
ping google.com            # ICMP echo request
ping -c 4 8.8.8.8          # ping 4 times
traceroute google.com      # Trace the route (Linux)
tracert google.com         # Windows version
```

### Rozgromienie
```bash
ip route show              # Linux: routing table
route -n                   # Older Linux
netstat -r                 # Windows/Mac
```

### Interfejsy sieciowe
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

### Łączność z portem
```bash
nc -zv google.com 443      # Netcat: check if port 443 is open
telnet google.com 443      # Telnet to port
curl -v https://google.com # Verbose output
```

### Zapora sieciowa (Linux iptables/nftables)
```bash
sudo ufw status            # Ubuntu: simple firewall
sudo iptables -L -n        # List rules
```

### Statystyki sieci
```bash
ss -tulpn                  # Show listening sockets (Linux)
netstat -an                # All sockets (all OS)
```

---

## Podsieci (skrócone omówienie)
| CIDR | Maska sieci | Liczba adresów | Użyteczne hosty |
|------|--------|-----------|-------------|
| /32 | 255.255.255.255 | 1 | 1 |
| /30 | 255.255.255.252 | 4 | 2 |
| /29 | 255.255.255.248 | 8 | 6 |
| /28 | 255.255.255.240 | 16 | 14 |
| /27 | 255.255.255.224 | 32 | 30 |
| /26 | 255.255.255.192 | 64 | 62 |
| /25 | 255.255.255.128 | 128 | 126 |
| /24 | 255.255.255.0 | 256 | 254 |
| /23 | 255.255.254.0 | 512 | 510 |
| /22 | 255.255.252.0 | 1024 | 1022 |
| /16 | 255.255.0.0 | 65536 | 65534 |
| /8 | 255.0.0.0 | 16 777 216 | 16 777 214 |
---

## Równoważenie obciążenia i odwrotne proxy
### Nginx jako odwrotny serwer proxy
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

### Algorytmy równoważenia obciążenia
- **Rynek okrężny**
- **Najmniej połączeń**
- **Skrót IP** (lepkość sesji)
- **Ważony system kołowy**
### Narzędzia
- **Nginx, HAProxy** (oprogramowanie)
- **AWS ELB, Azure Load Balancer, GCP Cloud Load Balancing** (chmura)
---

## Lista kontrolna rozwiązywania problemów
1. Czy połączenie fizyczne działa? (Sprawdź kable i połączenie Wi-Fi).
2. Czy możesz pingować bramę? (np.`ping 192.168.1.1`).
3. Czy możesz pingować zewnętrzny adres IP? (np.`8.8.8.8`).
4. Czy możesz rozwiązać domenę? (`dig google.com`).
5. Czy aplikacja nasłuchuje na oczekiwanym porcie? (`ss -tulpn | grep 8080`).
6. Czy zapora sieciowa blokuje port? (Sprawdź`iptables`/`ufw`lub grupy zabezpieczeń w chmurze).
7. Czy w logach aplikacji są jakieś błędy?
8. Czy certyfikat TLS jest ważny i godny zaufania? (`openssl s_client -connect example.com:443`).