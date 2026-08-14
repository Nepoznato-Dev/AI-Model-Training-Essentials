<!--
---
# Metadata
title: "Cloud Architecture"
description: "Cloud providers, architecture patterns, security"
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
tags: [cloud, architecture, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "11 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Architektura chmurowa
Przetwarzanie w chmurze zasadniczo zmieniło sposób, w jaki organizacje tworzą, wdrażają i skalują oprogramowanie. Zamiast kupować i utrzymywać serwery fizyczne, możesz udostępniać zasoby obliczeniowe na żądanie, płacić za to, czego używasz i skalować globalnie w ciągu kilku minut. Ten plik obejmuje podstawowe koncepcje, wzorce architektury, usługi i najlepsze praktyki, które musisz znać.
---

## Podstawy przetwarzania w chmurze
### Co to jest przetwarzanie w chmurze?
Dostarczanie na żądanie zasobów obliczeniowych — serwerów, pamięci masowej, baz danych, sieci, oprogramowania — przez Internet po cenach typu pay-as-you-go.
### Podstawowe cechy NIST
| Charakterystyka | Znaczenie |
|-------------------|--------|
| **Samoobsługa na żądanie** | Udostępnianie zasobów bez interakcji człowieka |
| **Szeroki dostęp do sieci** | Dostępne w sieci za pośrednictwem standardowych mechanizmów |
| **Łączenie zasobów** | Model wielodostępny; zasoby przydzielane dynamicznie |
| **Szybka elastyczność** | Szybkie skalowanie na zewnątrz i do wewnątrz |
| **Wymierna usługa** | Użycie jest monitorowane i rozliczane |
### Modele wdrażania
| Modelka | Opis | Kiedy stosować |
|-------|------------|------------|
| **Chmura publiczna** | Należy do dostawców; infrastruktura współdzielona (AWS, Azure, GCP) | Większość obciążeń; opłacalne |
| **Chmura prywatna** | Dedykowane jednej organizacji | Wymogi regulacyjne, dane wrażliwe |
| **Chmura hybrydowa** | Połączenie publicznego i prywatnego | Elastyczność + zgodność |
| **Wiele chmur** | Korzystanie z wielu dostawców chmury publicznej | Unikaj uzależnienia od dostawcy, najlepszy w swojej klasie |
### Modele usług
| Modelka | Zapewnia | Przykłady | Przypadki użycia |
|-------|----------|----------|---------------|
| **IaaS** | Maszyny wirtualne, pamięć masowa, sieci, system operacyjny | AWS EC2, maszyny wirtualne Azure, GCP Compute Engine | Migracje typu „lift-and-shift”, pełna kontrola |
| **PaaS** | Platformy programistyczne, bazy danych, oprogramowanie pośredniczące | Heroku, Google App Engine, AWS Elastic Beanstalk | Tworzenie aplikacji, wdrażanie API |
| **SaaS** | Kompletne wnioski przez Internet | Salesforce, Google Workspace, Microsoft 365 | E-mail, CRM, współpraca |
| **FaaS / bezserwerowy** | Wykonanie funkcji sterowanej zdarzeniami | AWS Lambda, Azure Functions, GCP Cloud Functions | API, przetwarzanie zdarzeń, zaplanowane zadania |
---

## Główni dostawcy usług w chmurze
| Dostawca | Udział w rynku | Mocne strony |
|---------|-------------|----------|
| **AWS** | ~32% | Najszerszy katalog usług, największy ekosystem |
| **Lazur** | ~23% | Integracja przedsiębiorstw, chmura hybrydowa, stos Microsoft |
| **GCP** | ~10% | Analityka danych, AI/ML, Kubernetes |
| **Chmura Alibaba** | ~4% | Dominujący w regionie Azji i Pacyfiku |
| **Chmura Oracle** | ~2% | Obciążenia baz danych, aplikacje dla przedsiębiorstw |
| **Chmura IBM** | ~2% | Koncentracja na przedsiębiorstwach, Watson AI |
| **Cyfrowy Ocean** | Nisza | Przyjazne dla programistów, uproszczone oferty |
### Porównanie usług (3 najlepszych dostawców)
| Kategoria | AWS | Błękit | GCP |
|---------|-----|-------|-----|
| **Oblicz** | EC2, Lambda, ECS | Maszyny wirtualne, funkcje, AKS | Compute Engine, funkcje chmury, GKE |
| **Przechowywanie** | S3, EBS, Lodowiec | Magazyn obiektów BLOB, magazyn dyskowy | Przechowywanie w chmurze, dysk stały |
| **Baza danych** | RDS, DynamoDB, Aurora | Baza danych SQL, Cosmos DB | Cloud SQL, Firestore, Bigtable |
| **Analiza** | Przesunięcie ku czerwieni, EMR | Synapsa, kostki danych | BigQuery, przepływ danych |
| **AI/ML** | SageMaker, Rozpoznanie | Azure ML, usługi poznawcze | Vertex AI, AutoML |
| **Sieć** | VPC, Route 53, CloudFront | Sieć wirtualna, Menedżer ruchu | VPC, Cloud DNS, Cloud CDN |
---

## Wzorce architektoniczne
### Dobrze zaprojektowana struktura
Wszyscy trzej główni dostawcy publikują dobrze zaprojektowane frameworki zbudowane na pięciu filarach:
| Filar | Kluczowe zasady |
|--------|-------------------|
| **Doskonałość operacyjna** | Automatyzować operacje; dokonywać częstych, odwracalnych zmian; przewidywać porażkę |
| **Bezpieczeństwo** | Silny fundament tożsamości; stosuj zabezpieczenia na każdej warstwie; chronić dane w transporcie i w stanie spoczynku |
| **Niezawodność** | Procedury odzyskiwania testów; automatyczne odzyskiwanie po awarii; skaluj poziomo |
| **Wydajność** | Użyj bezserwerowego; wejdź na rynek globalny w ciągu kilku minut; często eksperymentuj |
| **Optymalizacja kosztów** | Przyjmij model konsumpcji; korzystać z usług zarządzanych; przestań wydawać pieniądze na niezróżnicowaną pracę |
### Typowe wzorce
| Wzór | Opis | Korzyści | Wyzwania |
|-------------|------------|----------|------------|
| **Mikrousługi** | Rozłóż aplikację na małe, niezależne usługi | Skalowalność, izolacja błędów, niezależne wdrożenie | Rozproszona złożoność, spójność danych |
| **Sterowane zdarzeniami** | Komponenty komunikują się poprzez zdarzenia | Luźne połączenie, przetwarzanie w czasie rzeczywistym | Złożoność debugowania, ostateczna spójność |
| **Bezserwerowy** | Brak zarządzania serwerem; płacić za wykonanie | Oszczędność kosztów, szybkie wdrożenie | Zimny ​​start, uzależnienie od dostawcy, limity wykonania |
| **Warstwowe (N-poziomowe)** | Prezentacja → Logika biznesowa → Dostęp do danych → Baza danych | Rozdzielenie problemów, łatwość konserwacji | Może stać się monolityczny |
| **Kosmiczny** | Rozproszone dane w zwirtualizowanych węzłach pamięci | Obsługuje wysoką współbieżność i małe opóźnienia | Złożone w projektowaniu i zarządzaniu |
---

## Usługi podstawowe
### Oblicz
| Rodzaj usługi | Szczegóły |
|------------|------------|
| **Maszyny wirtualne** | Ogólnego przeznaczenia, zoptymalizowany pod kątem obliczeń, zoptymalizowany pod kątem pamięci, procesor graficzny. Ceny: na żądanie, zarezerwowane, na miejscu. |
| **Kontenery** | Środowisko wykonawcze Dockera; orkiestracja poprzez Kubernetes (EKS, AKS, GKE). Rejestry: ECR, GCR, ACR. |
| **Funkcje bezserwerowe** | Wyzwalane zdarzeniami, bezstanowe. Ograniczenia czasu wykonania, pamięci, współbieżności. |
### Składowanie
| Wpisz | Charakterystyka | Przykłady | Najlepsze dla |
|------|----------------|----------|---------|
| **Obiekt** | Płaska struktura, dostęp HTTP, bogata w metadane | S3, przechowywanie w chmurze, obiekt Blob Azure | Zasoby statyczne, kopie zapasowe, jeziora danych |
| **Blok** | Surowe woluminy dołączone do maszyn wirtualnych | EBS, dysk trwały, dyski platformy Azure | Bazy danych, woluminy rozruchowe |
| **Plik** | Współdzielone systemy plików (NFS/SMB) | EFS, magazyn plików, pliki Azure | Zarządzanie treścią, współdzielone konfiguracje |
| **Archiwum** | Najniższy koszt, opóźnienia w pobieraniu | Lodowiec S3, Archiwum Azure | Zgodność, długoterminowe kopie zapasowe |
### Bazy danych
| Kategoria | Usługi | Przypadek użycia |
|---------|----------|---------|
| **Zarządzane relacje** | RDS, Cloud SQL, Azure SQL | Tradycyjne aplikacje, transakcje ACID |
| **NoSQL — dokument** | DocumentDB, Firestore, Cosmos DB | Elastyczne schematy, dane JSON |
| **NoSQL — para klucz-wartość** | DynamoDB, pamięć podręczna Redis | Buforowanie, sesje, proste wyszukiwania |
| **NoSQL — szeroka kolumna** | Bigtable, Cassandra | Dużo zapisu, szeregi czasowe |
| **NoSQL — Wykres** | Neptun, Cosmos DB (Graph API) | Relacje, sieci społecznościowe |
| **hurtownia danych** | Płatek śniegu, przesunięcie ku czerwieni, BigQuery, synapsa | Analityka, BI |
| **Buforowanie** | ElastiCache, magazyn pamięci w chmurze | Przechowywanie sesji, buforowanie zapytań |
---

## Sieć
### Sieci wirtualne
Każde wdrożenie w chmurze odbywa się w wirtualnej chmurze prywatnej (VPC/VNet) — izolowanej sieci definiowanej za pomocą bloków CIDR, podsieci (publicznych lub prywatnych), tabel tras i bram.
### Równoważenie obciążenia i CDN
| Usługa | Cel |
|--------|---------|
| **Systemy równoważenia obciążenia** | Rozdzielaj ruch pomiędzy instancje (sieć L4, aplikacja L7) |
| **CDN** | Zawartość pamięci podręcznej w lokalizacjach brzegowych w celu zmniejszenia opóźnień (CloudFront, Cloud CDN, Azure CDN) |
| **DNS** | Rejestracja domeny, zasady routingu, kontrole stanu (Route 53, Cloud DNS, Azure DNS) |
### Opcje łączności
| Opcja | Opis |
|------------|------------|
| **Brama internetowa** | Publiczny dostęp do Internetu dla VPC |
| **Brama NAT** | Dostęp wychodzący do podsieci prywatnej |
| **VPN** | Szyfrowane tunele do lokalnych |
| **Połączenie bezpośrednie / ExpressRoute** | Dedykowane połączenia prywatne |
| **Połączenie równorzędne VPC** | Połącz VPC w obrębie kont lub pomiędzy nimi |
---

## Bezpieczeństwo
### Model wspólnej odpowiedzialności
| Warstwa | Dostawca | Klient |
|-------|----------|---------|
| **Infrastruktura** (sprzęt, wyposażenie) | ✅ | |
| **Obliczenia, pamięć masowa, sieć** | ✅ (zarządzane) | ✅ (samodzielnie zarządzany) |
| **Dane, aplikacje, tożsamość** | | ✅ |
Im lepiej zarządzana jest usługa, tym więcej obsługuje dostawca. Dzięki IaaS zarządzasz prawie wszystkim; w przypadku SaaS dostawca obsługuje prawie wszystko.
### Zarządzanie tożsamością i dostępem (IAM)
| Koncepcja | Opis |
|--------|------------|
| **Użytkownicy** | Tożsamości indywidualne |
| **Grupy** | Kolekcje użytkowników |
| **Role** | Tymczasowe dane uwierzytelniające dla usług lub użytkowników |
| **Zasady** | Dokumenty określające uprawnienia |
| **Zasada** | Najmniejsze przywileje, rozdzielenie obowiązków |
### Ochrona danych
- **Szyfrowanie w spoczynku**: KMS, klucze zarządzane przez klienta, HSM.
- **Szyfrowanie podczas przesyłania**: TLS/SSL, HTTPS.
- **Zarządzanie sekretami**: Menedżer sekretów, Key Vault — nigdy nie koduj sekretów na stałe.
---

## DevOps w chmurze
### Infrastruktura jako kod (IaC)
| Narzędzie | Opis |
|------|------------|
| **Terraforma** | Multicloud, deklaratywny HCL, zarządzanie stanem |
| **Formacja chmury** | Natywne szablony AWS, YAML/JSON |
| **Szablony ARM / Bicep** | Natywny dla platformy Azure |
| **Pulumi** | Infrastruktura wykorzystująca języki programowania (Python, Go itp.) |
### Usługi CI/CD
| Dostawca | Narzędzia |
|---------|-------|
| **AWS** | CodePipeline, CodeBuild, CodeDeploy |
| **Lazur** | Azure DevOps, akcje GitHub |
| **GCP** | Kompilacja w chmurze, wdrażanie w chmurze |
| **Inna strona** | Jenkins, CircleCI, GitLab CI |
### Monitorowanie i obserwowalność
| Zdolność | AWS | Błękit | GCP |
|----------|-----|-------|-----|
| **Dane** | ChmuraWatch | Azure Monitor | Monitorowanie w chmurze |
| **Logowanie** | Dzienniki CloudWatch | Analiza dzienników | Rejestrowanie w chmurze |
| **Śledzenie** | Rentgen | Informacje o aplikacji | Śledzenie chmur |
---

## Zarządzanie kosztami
### Modele cenowe
| Modelka | Opis | Najlepsze dla |
|-------|------------|---------|
| **Na żądanie** | Płać za to, czego używasz, według sekundy/godziny | Zmienne, krótkotrwałe obciążenia pracą |
| **Instancje zastrzeżone** | Zobowiązanie na 1–3 lata, znaczny rabat | Obciążenia w stanie ustalonym |
| **Instancje punktowe** | Oferta na niewykorzystaną przepustowość; można przerwać | Odporne na błędy, elastyczne zadania |
| **Plany Oszczędnościowe** | Elastyczne ceny zobowiązań | Mieszane wzorce użytkowania |
| **Bezpłatny poziom** | Ograniczone bezpłatne korzystanie z nowych kont | Nauka, prototypowanie |
### Strategie optymalizacji
Instancje o odpowiednim rozmiarze dopasowane do obciążeń. Użyj automatycznego skalowania, aby obsłużyć skoki popytu. Rezerwa pojemności dla przewidywalnych obciążeń. Użyj instancji punktowych do zadań wsadowych. Przenieś rzadko używane dane do tańszych warstw pamięci masowej. Usuń nieużywane zasoby (osierocone migawki, bezczynne moduły równoważenia obciążenia, niezałączone adresy IP).
---

## Wysoka dostępność i odzyskiwanie po awarii
### Koncepcje dostępności
| Koncepcja | Opis |
|--------|------------|
| **Strefa dostępności (AZ)** | Fizycznie oddzielne centra danych w regionie |
| **Region** | Obszar geograficzny z wieloma AZ |
| **Lokalizacja krawędzi** | Lokalizacja pamięci podręcznej CDN do dostarczania treści |
### Strategie odzyskiwania po awarii
| Strategia | Koszt | RTO | RPO | Opis |
|---------|------|-----|-----|--------|
| **Kopia zapasowa i przywracanie** | Najniższy | Godziny | Godziny – dni | Okresowe kopie zapasowe, przywracanie w razie potrzeby |
| **Światło kontrolne** | Niski | Minuty – godziny | Minuty | Podstawowe elementy zawsze działające, skalowanie w przypadku katastrofy |
| **Ciepły tryb gotowości** | Średni | Minuty | Sekundy–minuty | Zmniejszona wersja zawsze działająca |
| **Wiele lokalizacji aktywne/aktywne** | Najwyższy | Blisko zera | Zero | Pełna produkcja w wielu regionach |
**RTO** (docelowy czas odzyskiwania) = maksymalny akceptowalny czas przestoju. **RPO** (cel punktu odzyskiwania) = maksymalna akceptowalna utrata danych.
---

## Pojawiające się trendy
| Trend | Co się dzieje |
|------|--------------------------------|
| **Przetwarzanie brzegowe** | Przetwarzanie danych bliżej źródła (placówki AWS, długość fali, Azure Edge) |
| **Wiele chmur** | Unikanie uzależnienia od dostawcy; wykorzystanie najlepszych w swojej klasie dostawców |
| **Usługi AI/ML** | Wstępnie wyszkolone modele (wzrok, mowa, język) + niestandardowe szkolenie (SageMaker, Vertex AI) |
| **Obliczenia kwantowe** | Usługi eksperymentalne na wczesnym etapie (AWS Braket, Azure Quantum) |
| **Zrównoważona chmura** | Śledzenie śladu węglowego, zobowiązania dotyczące energii odnawialnej, zielona architektura |