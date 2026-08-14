---
# Metadata
title: "Cloud Services Comparison"
description: "AWS vs Azure vs GCP side-by-side comparison"
category: "Quick Reference"
subcategory: "Infrastructure"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "AI Model Training Team"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.1"
    date: "2026-08-09"
    author: "AI Model Training Team"
    changes: "Moved to infrastructure/ subfolder; added subcategory field"
  - version: "1.0.0"
    date: "2026-08-05"
    author: "AI Model Training Team"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-09"
review_date: "2027-02-05"
reviewed_by: "Quick Reference Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [cloud, services, comparison, quick-reference]
difficulty_level: "beginner"
prerequisites: []
estimated_reading_time: "7 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# Porównanie usług w chmurze
Bezpośrednie porównanie trzech głównych dostawców usług w chmurze — AWS, Azure i Google Cloud — w zakresie obliczeń, pamięci masowej, baz danych, sztucznej inteligencji/ML, sieci, monitorowania i infrastruktury jako kodu. Przydatne dla architektów decydujących, której platformy użyć lub mapujących usługi z jednej chmury na drugą.
---

## Przegląd dostawcy
| | AWS | Błękit | Google Cloud (GCP) |
|---|-----|-------|----------|
| **Udział w rynku** | ~31% (największy) | ~25% (sekunda) | ~11% (trzeci, najszybciej rosnący) |
| **Mocne strony** | Szeroki zakres usług; dojrzałość; ekosystem | Integracja przedsiębiorstw; chmura hybrydowa; Stos Microsoftu | Dane/AI; Kubernetesa; globalna sieć |
| **Najlepsze dla** | Startupy dla przedsiębiorstw; najszerszy katalog usług | Przedsiębiorstwa posiadające Microsoft/Active Directory; hybrydowy | Obciążenia wymagające dużej ilości danych; Natywny Kubernetes; AI/ML |
| **Regiony** | 33 regiony, 105 AZ | Ponad 60 regionów | Ponad 40 regionów, ponad 100 stref |
| **Poziom bezpłatny** | Poziom bezpłatny na 12 miesięcy + zawsze bezpłatny | 12 miesięcy za darmo + 200 $ kredytu | Kredyt o wartości 300 USD na 90 dni + zawsze bezpłatnie |
---

## Oblicz
| Kategoria usługi | AWS | Błękit | GCP |
|----------------|-----|-------|-----|
| **Maszyny wirtualne** | EC2 (elastyczna chmura obliczeniowa) | Maszyny wirtualne | Silnik obliczeniowy |
| **Automatyczne skalowanie** | Grupy automatycznego skalowania | Zestawy skalowania maszyn wirtualnych | Grupy instancji |
| **Funkcje bezserwerowe** | Lambda | Funkcje platformy Azure | Funkcje chmury |
| **Rejestr kontenerów** | ECR (Elastyczny rejestr kontenerów) | Rejestr kontenerów platformy Azure | Rejestr artefaktów |
| **Orkiestracja kontenerów** | ECS/EKS | ACS/AKS| GKE / Cloud Run |
| **Kontenery bezserwerowe** | Fargate | Aplikacje kontenerowe | Chmura |
| **Platforma aplikacji (PaaS)** | Elastyczna łodyga fasoli, narzędzie do uruchamiania aplikacji | Usługa aplikacji | Silnik aplikacji |
| **Przetwarzanie wsadowe** | Partia AWS | Partia Azure | Partia chmur |
| **Obliczenia GPU / AI** | EC2 (instancje P4d, P5) | Maszyny wirtualne serii NC/ND | maszyny wirtualne A2/A3; TPU |
### Modele cenowe maszyn wirtualnych
| Modelka | AWS | Błękit | GCP |
|-------|-----|-------|-----|
| **Na żądanie** | Instancje na żądanie | Płatność zgodnie z rzeczywistym użyciem | Na żądanie |
| **Zarezerwowane / Zaangażowane** | Instancje zastrzeżone (1–3 lata) | Zarezerwowane maszyny wirtualne (1–3 lata) | Zniżki za zaangażowanie (1–3 lata) |
| **Punktowy / Przerywalny** | Instancje punktowe | Znajdź maszyny wirtualne | Wywłaszczane / dodatkowe maszyny wirtualne |
| **Plany oszczędnościowe** | Plany Oszczędnościowe | Plany oszczędnościowe | Zniżki za zaangażowanie |
---

## Składowanie
| Kategoria usługi | AWS | Błękit | GCP |
|----------------|-----|-------|-----|
| **Przechowywanie obiektów** | S3 | Magazyn obiektów BLOB | Przechowywanie w chmurze |
| **Zablokuj przechowywanie** | EBS | Zarządzane dyski | Dysk stały |
| **Przechowywanie plików** | EFS, FSx | Pliki Azure | Magazyn plików |
| **Archiwum / Zimno** | Lodowiec S3, Głębokie Archiwum | Poziomy Blob Cool/Archiwum | Chmurowa linia chłodnicza/archiwum |
| **Transfer danych** | Kula śnieżna, DataSync | Skrzynka danych | Urządzenie do przenoszenia |
### Porównanie klas pamięci
| Przypadek użycia | AWS-a3 | Błękitny Blob | Przechowywanie w chmurze GCP |
|---------|--------|------------|--------------------------------|
| **Częsty dostęp** | Standard S3 | Gorąco | Standardowe |
| **Rzadki dostęp** | S3 Standard-IA | Fajne | Blisko linii |
| **Rzadki dostęp** | S3 One Zone-IA | — | Zimna linia |
| **Archiwum** | Lodowiec S3 / Głębokie Archiwum | Archiwum | Archiwum |
---

## Bazy danych
| Kategoria usługi | AWS | Błękit | GCP |
|----------------|-----|-------|-----|
| **Relacyjny (zarządzany)** | RDS (MySQL, PostgreSQL, Oracle, SQL Server) | Baza danych Azure (MySQL, PostgreSQL); Azure SQL | Chmura SQL (MySQL, PostgreSQL) |
| **Relacyjne (natywne w chmurze)** | Aurora (kompatybilna z MySQL/PostgreSQL) | Azure SQL Database (pule elastyczne) | Cloud Spanner (dystrybucja globalna) |
| **NoSQL (dokument)** | DynamoDB | Cosmos DB (API MongoDB, API SQL) | Magazyn ogniowy; Magazyn danych |
| **NoSQL (szeroka kolumna)** | DynamoDB (też) | Cosmos DB (API Cassandra) | Duży stół |
| **NoSQL (klucz-wartość)** | DynamoDB, ElastiCache | Pamięć podręczna platformy Azure dla Redis | Magazyn pamięci (Redis) |
| **Wykres** | Neptun | Cosmos DB (API Gremlin) | — |
| **Szereg czasowy** | Strumień czasu | Eksplorator danych platformy Azure | — |
| **Księga ** | QLDB | Poufna księga platformy Azure | — |
| **Pamięć podręczna w pamięci** | ElastiCache (Redis, Memcached) | Pamięć podręczna platformy Azure dla Redis | Magazyn pamięci |
| **Szukaj** | Usługa OpenSearch | Wyszukiwanie AI na platformie Azure | Wyszukiwanie w chmurze; Wyszukiwanie AI wierzchołków |
| **Hurtownia danych** | Przesunięcie ku czerwieni | Analiza synaps | BigQuery |
---

## Sztuczna inteligencja i uczenie maszynowe
| Kategoria usługi | AWS | Błękit | GCP |
|----------------|-----|-------|-----|
| **Platforma ML** | SageMaker | Uczenie maszynowe platformy Azure | Wierzchołkowa sztuczna inteligencja |
| **Wstępnie przeszkolone interfejsy API** | Rozpoznawanie (wizja), Polly (TTS), Rozumienie (NLP), Transkrypcja | Usługi poznawcze (wzrok, mowa, język, decyzja) | Wizja AI, zamiana mowy na tekst, API języka naturalnego |
| **LLM / Generatywna sztuczna inteligencja** | Skała podstawowa (Claude, Lama, Tytan) | Usługa Azure OpenAI (GPT-4, DALL-E) | Wierzchołkowa sztuczna inteligencja (Bliźnięta); Modelowy ogród |
| **Wektor / Osadzenia** | OpenSearch (k-NN), Bazy wiedzy Bedrock | Wyszukiwanie AI platformy Azure (wektor) | Wyszukiwanie wektorów Vertex AI, AlloyDB |
| **MLops** | Potoki SageMaker, rejestr modeli | Potoki Azure ML, rejestr modeli | Potoki Vertex AI, rejestr modeli |
| **Oznaczanie danych** | Prawda SageMakera | Etykietowanie danych usługi Azure ML | Etykietowanie danych Vertex AI |
| **Konwersacyjna sztuczna inteligencja** | Lex | Usługa bota platformy Azure | Dialogflow CX/ES |
| **Tłumaczenie** | Przetłumacz | Tłumacz | Tłumaczenie API |
---

## Sieć
| Kategoria usługi | AWS | Błękit | GCP |
|----------------|-----|-------|-----|
| **Sieć wirtualna** | VPC | Sieć wirtualna (sieć wirtualna) | VPC |
| **Równoważenie obciążenia** | ELB/ALB/NLB/CLB | Load Balancer (aplikacja, sieć, brama) | Równoważenie obciążenia w chmurze |
| **DNS** | Trasa 53 | Azure DNS | Chmura DNS |
| **CDN** | CloudFront | Drzwi wejściowe Azure | Chmura CDN |
| **Brama API** | Brama API | Zarządzanie API | Brama API |
| **VPN** | VPN typu lokacja-lokacja, VPN klienta | Brama VPN | Chmura VPN |
| **Połączenie bezpośrednie / ExpressRoute** | Bezpośrednie połączenie | ExpressRoute | Połączenie w chmurze |
| **Link prywatny** | PrivateLink, punkty końcowe VPC | Prywatne łącze, prywatne punkty końcowe | Prywatne połączenie usług |
| **Zapora sieciowa** | WAF, zapora sieciowa | Zapora platformy Azure, WAF | Chmura Zbroi, Zapora sieciowa |
| **Ochrona DDoS** | Tarcza Standardowa / Zaawansowana | Ochrona DDoS | Pancerz Chmur |
---

## Monitorowanie i rejestrowanie
| Kategoria usługi | AWS | Błękit | GCP |
|----------------|-----|-------|-----|
| **Metryki / Monitorowanie** | ChmuraWatch | Azure Monitor | Monitorowanie w chmurze (Stackdriver) |
| **Logowanie** | Dzienniki CloudWatch | Log Analytics (dzienniki Azure Monitor) | Rejestrowanie w chmurze |
| **Śledzenie** | Rentgen | Informacje o aplikacji | Śledzenie chmur |
| **Alarm** | Alarmy CloudWatch | Alerty Azure Monitor | Alerty monitorowania chmury |
| **Panele ** | Panele CloudWatch | Skoroszyty/pulpity nawigacyjne platformy Azure | Panele monitorowania chmury |
| **Śledzenie błędów** | Syntetyki CloudWatch | Informacje o aplikacji | Raportowanie błędów w chmurze |
| **Inna strona** | Datadog, New Relic, PagerDuty | Datadog, New Relic, PagerDuty | Datadog, New Relic, PagerDuty |
---

## Infrastruktura jako kod i DevOps
| Kategoria usługi | AWS | Błękit | GCP |
|----------------|-----|-------|-----|
| **IaC (natywny)** | Formacja Chmury | Szablony ARM / Biceps | Menedżer wdrożeń / Pulumi |
| **IaC (między chmurami)** | Terraform, Pulumi, CDK | Terraforma, Pulumi, Biceps | Terraform, Pulumi |
| **CI/CD** | CodePipeline, CodeBuild | Azure DevOps, akcje GitHub | Kompilacja w chmurze; Wdrożenie w chmurze |
| **Rejestr kontenerów** | ECR | Rejestr kontenerów platformy Azure | Rejestr artefaktów |
| **GitOps** | Aplikacja Mesh + Flux/ArgoCD | Flux/ArgoCD na AKS | Synchronizacja konfiguracji (Anthos) |
| **Zarządzanie tajemnicami** | Menedżer sekretów, magazyn parametrów SSM | Magazyn kluczy | Tajny menadżer |
---

## Względy cenowe
| Czynnik | AWS | Błękit | GCP |
|--------|-----|-------|-----|
| **Szczegółowość rozliczeń** | Na sekundę (dla niektórych po pierwszej godzinie) | Na sekundę | Na sekundę |
| **Zniżki za długotrwałe użytkowanie** | Instancje Zarezerwowane / Plany Oszczędnościowe | Zarezerwowane maszyny wirtualne | Zniżki za zaangażowanie |
| **Instancje punktowe** | Do 90% zniżki | Do 90% zniżki | Do 91% zniżki |
| **Wyjście danych** | Opłata (droga) | Naładowany | Ta sama cena niezależnie od kierunku podróży (często taniej) |
| **Poziom bezpłatny** | 12 miesięcy + zawsze bezpłatnie | 12 miesięcy + kredyt o wartości 200 USD | 300 $ za 90 dni + zawsze bezpłatnie |
| **Zniżki dla przedsiębiorstw** | Program rabatowy dla przedsiębiorstw (EDP) | MACC (umowa zaangażowania pieniężnego) | Zaangażowane użycie + CUD |
---

## Kiedy używać którego
| Scenariusz | Polecane | Dlaczego |
|---------|------------|-----|
| **Najszerszy wybór usług; dojrzały ekosystem** | AWS | Największy katalog; większość integracji stron trzecich |
| **Przedsiębiorstwo Microsoft; Aktywny katalog; hybrydowy** | Błękit | Natywna integracja z AD; mocne oprzyrządowanie hybrydowe |
| **Hurtownia danych; BigQuery; analityczne** | GCP | BigQuery jest najlepszy w swojej klasie; bezproblemowa integracja danych |
| **Rozwój natywny dla Kubernetes** | GCP | GKE to najlepiej zarządzany Kubernetes |
| **Generatywne aplikacje AI / LLM** | Azure lub GCP | Azure OpenAI dla modeli GPT; Vertex AI dla Gemini |
| **Aplikacje na skalę globalną i o niskim opóźnieniu** | GCP | Globalna sieć Google to prawdziwa zaleta |
| **Rząd / obciążenia wymagające dużej zgodności** | AWS lub Azure | Większość certyfikatów zgodności; Regiony GovCloud |
| **Start-upy wrażliwe na koszty** | GCP lub AWS | Bezpłatny poziom GCP jest hojny; AWS ma kredyty startowe |
| **Istniejący stos Microsoft / .NET** | Błękit | Ścisła integracja z Visual Studio, .NET, Office 365 |
| **Strategia wielu chmur** | Terraform + wszystkie trzy | Użyj Terraform do zarządzania zasobami w chmurach |
---

## Streszczenie
Wszystkie trzy chmury są wydajne, niezawodne i stale się rozwijają. Wybór zwykle sprowadza się do tego, co już wie Twój zespół, jak wyglądają Twoje obecne umowy i jakie konkretne usługi mają znaczenie dla Twojego obciążenia pracą. Coraz popularniejsze staje się korzystanie z wielu chmur — użyj Terraform lub Pulumi, aby uniknąć uzależnienia od dostawców w warstwie infrastruktury i wybierz każdą chmurę pod kątem tego, co robi najlepiej.