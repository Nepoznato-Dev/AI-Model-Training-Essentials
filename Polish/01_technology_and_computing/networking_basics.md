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
- 32-bitowy adres zapisany w postaci czterech oktetów: INLINECODE_0_END
- Razem: ~4,3 miliarda adresów (ale w praktyce wyczerpane).

### IPv6
- Adres 128-bitowy zapisany w formacie szesnastkowym: INLINECODE_1_END
- Łącznie: 2¹²⁸ adresów (praktycznie nieskończona liczba).

### Zakresy prywatnych adresów IP (RFC 1918)
Nie można ich trasować w Internecie; używany w sieciach lokalnych:
- INLINECODE_2_END (10.0.0.0 – 10.255.255.255)
- INLINECODE_3_END (172.16.0.0 – 172.31.255.255)
- INLINECODE_4_END (192.168.0.0 – 192.168.255.255)

### Notacja CIDR
INLINECODE_5_END oznacza, że pierwsze 24 bity to prefiks sieci; ostatnie 8 bitów to hosty. Zawiera adresy od INLINECODE_6_END do INLINECODE_7_END.

---

## DNS (system nazw domen)

Mapuje nazwy domen (np. INLINECODE_8_END) na adresy IP.

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
Przecena CODEBLOCK_0_END
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
ELK Stack (Elasticsearch, Logstash, Kibana) lub Elastic Cloud.

Loki + Grafana (lekka alternatywa).

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

ArgoCD: GitOps dla Kubernetesa.

Przykładowa akcja GitHub (prosta):
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