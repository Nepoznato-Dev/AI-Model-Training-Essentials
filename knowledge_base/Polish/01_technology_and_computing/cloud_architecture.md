# Architektura chmurowa

## Podstawy przetwarzania w chmurze

### Co to jest przetwarzanie w chmurze?
Dostarczanie na żądanie zasobów obliczeniowych (serwerów, pamięci masowej, baz danych, sieci, oprogramowania) przez Internet po cenach typu pay-as-you-go.

### Podstawowe cechy charakterystyczne (definicja NIST)
- **Samoobsługa na żądanie**: Udostępnianie zasobów bez interakcji człowieka
- **Szeroki dostęp do sieci**: Dostępny przez sieć za pośrednictwem standardowych mechanizmów
- **Łączenie zasobów**: Model wielodostępny z dynamicznym przypisywaniem
- **Szybka elastyczność**: Szybkie skalowanie na zewnątrz i do wewnątrz
- **Usługa pomiarowa**: Monitorowanie i rozliczanie wykorzystania zasobów

### Modele wdrażania w chmurze
- **Public Cloud**: własność dostawców, infrastruktura współdzielona (AWS, Azure, GCP)
- **Private Cloud**: Dedykowane dla jednej organizacji (lokalnie lub hostowane)
- **Chmura hybrydowa**: połączenie chmury publicznej i prywatnej
- **Multi-Cloud**: korzystanie z wielu dostawców chmury publicznej
- **Community Cloud**: udostępniane organizacjom mającym wspólne obawy

### Modele usług

#### Infrastruktura jako usługa (IaaS)
- **Zapewnia**: maszyny wirtualne, pamięć masową, sieci, systemy operacyjne
- **Przykłady**: AWS EC2, Google Compute Engine, maszyny wirtualne Azure
- **Przypadki użycia**: migracje typu „lift-and-shift”, środowiska programistyczne, potrzeby wymagające dużej kontroli

#### Platforma jako usługa (PaaS)
- **Zapewnia**: Platformy programistyczne, bazy danych, oprogramowanie pośrednie
- **Przykłady**: Heroku, Google App Engine, AWS Elastic Beanstalk
- **Przypadki użycia**: Tworzenie aplikacji, wdrażanie API, mikrousługi

#### Oprogramowanie jako usługa (SaaS)
- **Zapewnia**: Kompletne aplikacje przez Internet
- **Przykłady**: Salesforce, Google Workspace, Microsoft 365, Slack
- **Przypadki użycia**: poczta e-mail, CRM, współpraca, aplikacje biznesowe

#### Funkcja jako usługa (FaaS) / bezserwerowa
- **Zapewnia**: Wykonywanie funkcji sterowanych zdarzeniami
- **Przykłady**: AWS Lambda, Azure Functions, Google Cloud Functions
- **Przypadki użycia**: przetwarzanie zdarzeń, interfejsy API, zaplanowane zadania, przetwarzanie w czasie rzeczywistym

## Główni dostawcy usług w chmurze

### Usługi sieciowe Amazon (AWS)
- **Udział w rynku**: ~32% (największy dostawca)
- **Kluczowe usługi**:
  - Obliczenia: EC2, Lambda, ECS, EKS
  - Magazyn: S3, EBS, Lodowiec
  - Baza danych: RDS, DynamoDB, Aurora
  - Sieć: VPC, Route 53, CloudFront
  - AI/ML: SageMaker, rozpoznawanie, zrozumienie

###Microsoft Azure
- **Udział w rynku**: ~23%
- **Mocne strony**: Integracja korporacyjna, chmura hybrydowa, ekosystem Microsoft
- **Kluczowe usługi**:
  - Obliczenia: maszyny wirtualne, Azure Functions, AKS
  - Pamięć masowa: pamięć masowa typu Blob, pamięć dyskowa
  - Baza danych: baza danych SQL, Cosmos DB
  - Sieć: Sieć wirtualna, Menedżer ruchu
  - AI/ML: Azure ML, usługi kognitywne

### Platforma Google Cloud (GCP)
- **Udział w rynku**: ~10%
- **Mocne strony**: Analityka danych, AI/ML, Kubernetes
- **Kluczowe usługi**:
  - Obliczenia: Compute Engine, funkcje chmury, GKE
  - Przechowywanie: przechowywanie w chmurze, dysk trwały
  - Baza danych: Cloud SQL, Firestore, Bigtable
  - Analityka: BigQuery, Dataflow, Pub/Sub
  - AI/ML: Vertex AI, AutoML

### Inni dostawcy
- **IBM Cloud**: skupienie się na przedsiębiorstwach, Watson AI
- **Oracle Cloud**: obciążenia baz danych, aplikacje korporacyjne
- **Alibaba Cloud**: dominująca w regionie Azji i Pacyfiku
- **DigitalOcean**: Uproszczone oferty przyjazne dla programistów

## Wzorce architektury chmur

### Dobrze zaprojektowane zasady ramowe

#### Doskonałość operacyjna
- Automatyzuj operacje
- Dokonuj częstych, odwracalnych zmian
- Ciągłe udoskonalanie procedur
- Przewiduj porażkę

#### Bezpieczeństwo
- Wdrożyć silny fundament tożsamości
- Włącz identyfikowalność
- Zastosuj zabezpieczenia na wszystkich warstwach
- Automatyzuj najlepsze praktyki bezpieczeństwa
- Chroń dane w transporcie i w stanie spoczynku

#### Niezawodność
- Procedury odzyskiwania testów
- Automatyczne przywracanie sprawności po awarii
- Skaluj poziomo pod kątem dostępności
- Przestań zgadywać pojemność
- Zarządzanie zmianami w automatyzacji

#### Wydajność wydajności
- Demokratyzacja zaawansowanych technologii
- Wejdź na rynek globalny w ciągu kilku minut
- Używaj architektur bezserwerowych
- Eksperymentuj częściej
- Weź pod uwagę mechaniczne współczucie

#### Optymalizacja kosztów
- Przyjęcie modelu konsumpcji
- Zmierz ogólną wydajność
- Przestań wydawać pieniądze na niezróżnicowaną pracę
- Analizuj i przypisuj wydatki
- Korzystaj z usług zarządzanych

### Powszechne wzorce architektoniczne

#### Architektura mikrousług
- Rozłóż aplikacje na małe, niezależne usługi
- Każda usługa jest właścicielem swoich danych i logiki
- Komunikuj się za pośrednictwem interfejsów API (REST, gRPC, przesyłanie wiadomości)
- Wdrażaj niezależnie
- **Korzyści**: Skalowalność, izolacja usterek, różnorodność technologii
- **Wyzwania**: Rozproszona złożoność, spójność danych, monitorowanie

#### Architektura sterowana zdarzeniami
- Komponenty komunikują się poprzez zdarzenia
- Producenci emitują zdarzenia, konsumenci reagują
- **Wzorce**: pozyskiwanie zdarzeń, CQRS, pub/sub
- **Technologie**: Kafka, SNS/SQS, EventBridge, Pub/Sub
- **Korzyści**: Luźne powiązanie, skalowalność, przetwarzanie w czasie rzeczywistym#### Architektura bezserwerowa
- Nie jest wymagane zarządzanie serwerem
- Zapłać za wykonanie
- Automatyczne skalowanie
- **Komponenty**: Funkcje, bramka API, usługi zarządzane
- **Korzyści**: Oszczędność kosztów, ograniczenie operacji, szybkie wdrożenie
- **Rozważania**: Zimny start, uzależnienie od dostawcy, limity wykonania

#### Architektura warstwowa (N-poziom)
- Warstwa prezentacji (UI)
- Warstwa logiki aplikacji/biznesowej
- Warstwa dostępu do danych
- Warstwa bazy danych
- **Korzyści**: Oddzielenie problemów, łatwość konserwacji
- **Wspólne**: trójwarstwowe aplikacje internetowe

#### Architektura kosmiczna
- Obsługa dużej współbieżności z rozproszonymi danymi
- Zwirtualizowana pamięć na serwerach
- Węzły przetwarzające skalują się niezależnie
- **Przypadki użycia**: aplikacje o dużej objętości i małych opóźnieniach

## Usługi obliczeniowe

### Maszyny wirtualne
- **Typy**: ogólnego przeznaczenia, zoptymalizowane pod kątem obliczeń, zoptymalizowane pod kątem pamięci, GPU
- **Cennik**: Instancje na żądanie, instancje zarezerwowane, instancje typu spot
- **Zarządzanie**: Grupy automatycznego skalowania, moduły równoważenia obciążenia
- **Najlepsze praktyki**: Dopasowywanie rozmiaru, tagowanie, monitorowanie, łatanie

### Kontenery
- **Docker**: Standard środowiska uruchomieniowego kontenera
- **Orkiestracja**: Kubernetes (EKS, AKS, GKE), ECS, Fargate
- **Korzyści**: Przenośność, wydajność, spójność
- **Rejestr**: ECR, GCR, ACR, Docker Hub

### Funkcje bezserwerowe
- **Model wykonawczy**: wyzwalany zdarzeniem, bezstanowy
- **Ograniczenia**: czas wykonania, pamięć, równoczesne wykonania
- **Przypadki użycia**: interfejsy API, przetwarzanie plików, zaplanowane zadania, backendy IoT
- **Monitorowanie**: Liczba wywołań, błędy, czas trwania, zimne starty

## Rozwiązania w zakresie przechowywania

### Przechowywanie obiektów
- **Charakterystyka**: Płaska struktura, metadane, dostęp HTTP
- **Przykłady**: AWS S3, Google Cloud Storage, Azure Blob
- **Przypadki użycia**: zasoby statyczne, kopie zapasowe, jeziora danych, archiwa
- **Klasy przechowywania**: Gorąca, chłodna, zimna, archiwalna (różny koszt/dostęp)

### Blokuj pamięć
- **Charakterystyka**: Surowe woluminy dołączone do maszyn wirtualnych
- **Przykłady**: AWS EBS, dysk trwały Google, dyski Azure
- **Przypadki użycia**: bazy danych, woluminy rozruchowe, potrzeby związane z wysoką wydajnością
- **Typy**: SSD, HDD, zapewnione IOPS

### Przechowywanie plików
- **Charakterystyka**: Współdzielone systemy plików, protokoły NFS/SMB
- **Przykłady**: AWS EFS, Google Filestore, Azure Files
- **Przypadki użycia**: zarządzanie treścią, współdzielone konfiguracje, podnoszenie i przesuwanie

### Przechowywanie archiwalne
- **Charakterystyka**: Najniższy koszt, opóźnienia w pobieraniu
- **Przykłady**: Lodowiec S3, Azure Archive Storage
- **Przypadki użycia**: zgodność, długoterminowe kopie zapasowe, dane historyczne

## Usługi baz danych

### Zarządzane relacyjne bazy danych
- **Usługi**: AWS RDS/Aurora, Google Cloud SQL, Azure SQL Database
- **Funkcje**: Automatyczne kopie zapasowe, łatanie, skalowanie, replikacja
- **Silniki**: MySQL, PostgreSQL, MariaDB, Oracle, SQL Server

### Bazy danych NoSQL
- **Dokument**: DocumentDB, Firestore, Cosmos DB
- **Klucz-wartość**: DynamoDB, pamięć podręczna Redis
- **Szeroka kolumna**: Bigtable, Cassandra (zarządzana)
- **Wykres**: Neptun, Cosmos DB (interfejs API wykresów)

### Hurtownia danych
- **Usługi**: Płatek śniegu, Redshift, BigQuery, Synapse
- **Charakterystyka**: Magazyn kolumnowy, architektura MPP
- **Przypadki użycia**: analityka, BI, analiza danych na dużą skalę

### Usługi buforowania
- **In-Memory**: ElastiCache (Redis/Memcached), Cloud Memorystore
- **Buforowanie CDN**: CloudFront, Cloud CDN, Azure CDN
- **Przypadki użycia**: przechowywanie sesji, buforowanie zapytań, dostarczanie treści

## Sieć

### Sieci wirtualne
- **VPC/VNet**: Izolowane środowiska sieciowe
- **Podsieci**: publiczne (z dostępem do Internetu), prywatne (tylko wewnętrzne)
- **Adresowanie IP**: bloki CIDR, IPv4/IPv6
- **Tabele tras**: Kontroluj przepływ ruchu

### Równoważenie obciążenia
- **Typy**: Aplikacja (L7), Sieć (L4), Brama
- **Funkcje**: Kontrole stanu, zakończenie protokołu SSL, sesje trwałe
- **Usługi**: ELB/ALB/NLB, równoważenie obciążenia w chmurze, Azure Load Balancer

### Sieci dostarczania treści (CDN)
- **Cel**: Zawartość pamięci podręcznej w lokalizacjach brzegowych
- **Korzyści**: Mniejsze opóźnienia, mniejsze obciążenie początkowe, dystrybucja globalna
- **Usługi**: CloudFront, Cloud CDN, Azure CDN, Akamai

### Usługi DNS
- **Funkcje**: rejestracja domeny, routing, kontrola stanu
- **Usługi**: Route 53, Cloud DNS, Azure DNS
- **Zasady routingu**: proste, ważone, oparte na opóźnieniach, geolokalizacja, przełączanie awaryjne

### Opcje łączności
- **Brama internetowa**: Publiczny dostęp do Internetu
- **Brama NAT**: Dostęp wychodzący do prywatnej podsieci
- **VPN**: szyfrowane tunele do lokalizacji lokalnej
- **Połączenie bezpośrednie/ExpressRoute**: Dedykowane połączenia prywatne
- **VPC Peering**: łącz VPC w ramach kont/pomiędzy kontami

## Bezpieczeństwo w chmurze

### Model wspólnej odpowiedzialności
- **Odpowiedzialność Dostawcy**: Bezpieczeństwo chmury (infrastruktury)
- **Odpowiedzialność Klienta**: Bezpieczeństwo W chmurze (dane, aplikacje, dostęp)
- **Różni się w zależności od usługi**: Lepsze zarządzanie = większa odpowiedzialność dostawcy

### Zarządzanie tożsamością i dostępem (IAM)
- **Użytkownicy**: Tożsamości indywidualne
- **Grupy**: Kolekcje użytkowników
- **Role**: Tymczasowe dane uwierzytelniające dla usług/użytkowników
- **Zasady**: dokumenty JSON definiujące uprawnienia
- **Zasady**: Najmniejsze przywileje, rozdział obowiązków### Bezpieczeństwo sieci
- **Grupy zabezpieczeń**: Zapory stanowe dla instancji
- **Sieciowe listy ACL**: Bezstanowe zapory ogniowe dla podsieci
- **Zapora aplikacji internetowej (WAF)**: Ochrona przed exploitami internetowymi
- **Ochrona DDoS**: Tarcza, Cloud Armor, Ochrona DDoS

### Ochrona danych
- **Szyfrowanie w spoczynku**: KMS, klucze zarządzane przez klienta
- **Szyfrowanie w transporcie**: TLS/SSL, HTTPS
- **Zarządzanie kluczami**: HSM, rotacja kluczy, ścieżki audytu
- **Zarządzanie tajemnicami**: Menedżer tajemnic, Key Vault

### Zgodność i zarządzanie
- **Certyfikaty**: SOC 2, ISO 27001, HIPAA, PCI-DSS, RODO
- **Narzędzia**: egzekwowanie zasad, raportowanie zgodności, dzienniki audytu
- **Frameworks**: Cloud Security Alliance, NIST CSF

## DevOps w chmurze

### Usługi CI/CD
- **AWS**: CodePipeline, CodeBuild, CodeDeploy
- **Azure**: Azure DevOps, akcje GitHub
- **GCP**: kompilacja w chmurze, wdrażanie w chmurze
- **Firma trzecia**: Jenkins, CircleCI, GitLab CI

### Infrastruktura jako kod (IaC)
- **Terraform**: Multi-cloud, deklaratywny, zarządzanie stanem
- **CloudFormation**: natywne szablony AWS, YAML/JSON
- **Szablony ARM**: natywna platforma Azure
- **Menedżer wdrażania**: natywny GCP
- **Pulumi**: Infrastruktura wykorzystująca języki programowania
- **Korzyści**: Kontrola wersji, powtarzalność, dokumentacja

### Zarządzanie konfiguracją
- **Ansible**: Bezagentowe podręczniki YAML
- **Szef kuchni**: Dojrzały ekosystem oparty na rubinach
- **Marionetka**: Deklaratywna, mocna sprawozdawczość
- **SaltStack**: Szybki, oparty na Pythonie

### Monitorowanie i obserwowalność
- **Metryki**: CloudWatch, monitorowanie chmury, Azure Monitor
- **Logowanie**: dzienniki CloudWatch, rejestrowanie w chmurze, analiza logów
- **Śledzenie**: prześwietlenie, śledzenie w chmurze, wgląd w aplikacje
- ** Panele**: Panele CloudWatch, konsola Cloud
- **Alerty**: SNS, alerty monitorowania chmury, grupy akcji

### Orkiestracja kontenerów
- **Kubernetes**: orkiestracja spełniająca standardy branżowe
- **Usługi zarządzane**: EKS, AKS, GKE
- **Service Mesh**: Istio, Linkerd (zarządzanie ruchem, bezpieczeństwo)
- **GitOps**: ArgoCD, Flux (wdrożenia deklaratywne)

## Zarządzanie kosztami

### Modele cenowe
- **Płatność zgodnie z rzeczywistym użyciem**: Płać za to, czego używasz
- **Instancje zastrzeżone**: zobowiązania na 1-3 lata, znaczne rabaty
- **Instancje punktowe**: Licytacja niewykorzystanej pojemności może zostać przerwana
- **Plany oszczędnościowe**: Elastyczne ceny zobowiązań
- **Poziom bezpłatny**: ograniczone bezpłatne korzystanie z nowych kont

### Strategie optymalizacji kosztów
- **Dopasowanie rozmiaru**: Dopasuj typy instancji do potrzeb obciążenia
- **Automatyczne skalowanie**: Skalowanie w oparciu o zapotrzebowanie
- **Zarezerwowana pojemność**: Zaangażuj się w stałe obciążenia
- **Wykorzystanie punktowe**: Użyj w przypadku odpornych na awarie, elastycznych obciążeń
- **Poziomy pamięci masowej**: Przenieś rzadkie dane do tańszych warstw
- **Oczyszczanie**: Usuń nieużywane zasoby, migawki, AMI

### Narzędzia do zarządzania kosztami
- **AWS**: Eksplorator kosztów, budżety, zaufany doradca
- **Azure**: Zarządzanie kosztami, Doradca
- **GCP**: Raporty rozliczeniowe, Osoba polecająca
- **Firma trzecia**: CloudHealth, CloudCheckr, Datadog

## Wysoka dostępność i odzyskiwanie po awarii

### Koncepcje dostępności
- **Strefy dostępności**: Fizycznie oddzielne centra danych w obrębie regionu
- **Regiony**: obszary geograficzne z wieloma strefami AZ
- **Lokalizacja brzegowa**: lokalizacje pamięci podręcznej CDN na całym świecie

### Strategie wysokiej dostępności
- **Multi-AZ**: wdrażanie w różnych strefach dostępności
- **Automatyczne leczenie**: Automatyczna wymiana uszkodzonych instancji
- ** Równoważenie obciążenia**: Rozłóż ruch na zdrowe instancje
- **Replikacja bazy danych**: wdrożenia z wieloma AZ, odczyt replik

### Strategie odzyskiwania po awarii
- **Kopia zapasowa i przywracanie**: Okresowe kopie zapasowe, przywracanie w razie potrzeby (najniższy koszt)
- **Światło kontrolne**: Podstawowe elementy działają, skalowanie w przypadku awarii
- **Ciepły tryb gotowości**: Zmniejszona wersja zawsze działa
- **Wiele lokalizacji Aktywne/Aktywne**: Pełna produkcja w wielu regionach (najwyższy koszt)

### RTO i RPO
- **Docelowy czas odzyskiwania (RTO)**: Maksymalny akceptowalny czas przestoju
- **Cel punktu odzyskiwania (RPO)**: Maksymalna akceptowalna utrata danych
- **Wybór strategii**: Na podstawie wymagań biznesowych i budżetu

## Pojawiające się trendy

### Przetwarzanie brzegowe
- Przetwarzaj dane bliżej źródła
- **Usługi**: placówki AWS, długość fali, Azure Edge, Cloud CDN
- **Przypadki użycia**: IoT, analityka w czasie rzeczywistym, aplikacje o niskim opóźnieniu

### Chmura wielochmurowa i chmura hybrydowa
- Unikaj uzależnienia od dostawcy
- Korzystaj z najlepszych w swojej klasie usług
- **Narzędzia**: Terraform, Anthos, Arc, CloudHealth

### Usługi AI/ML
- Wstępnie przeszkolone modele: wzrok, mowa, język
- Szkolenie z modeli niestandardowych: SageMaker, Vertex AI, Azure ML
- MLOps: wdrażanie modelu, monitorowanie, zarządzanie

### Obliczenia kwantowe
- **Usługi**: AWS Braket, Azure Quantum
- **Stan**: Wczesny etap, eksperymentalny
- **Potencjał**: kryptografia, optymalizacja, odkrywanie leków

### Zrównoważona chmura
- Śledzenie śladu węglowego
- Zobowiązania dotyczące energii odnawialnej
- Efektywne wykorzystanie zasobów
- Wzory zielonej architektury