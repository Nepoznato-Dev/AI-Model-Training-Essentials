---
# Metadata
title: "DevOps and CI/CD"
description: "CI/CD pipelines, Docker, Kubernetes, Terraform, GitOps"
category: "Coding and Technology"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "AI Model Training Team"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.0"
    date: "2026-08-05"
    author: "AI Model Training Team"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-05"
review_date: "2027-02-05"
reviewed_by: "Coding & Technology Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [devops, cicd, coding-and-technology]
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
# DevOps i CI/CD
DevOps to połączenie filozofii kulturowej, praktyk i narzędzi, które umożliwia zespołom szybsze i bardziej niezawodne dostarczanie oprogramowania. Burzy mur pomiędzy programistami (którzy chcą wprowadzać zmiany) a operacjami (którzy chcą stabilności). CI/CD — ciągła integracja i ciągłe dostarczanie — to szkielet automatyzacji, który to umożliwia.
---

## Rurociągi CI/CD
### Co właściwie oznacza CI/CD
| Termin | Co to robi |
|------|------------|
| **Ciągła integracja (CI)** | Programiści często łączą kod; każde połączenie uruchamia automatyczne kompilacje i testy |
| **Dostawa ciągła (CD)** | Kod jest zawsze w stanie umożliwiającym wdrożenie; wypuszczenie do produkcji jest decyzją ręczną |
| **Ciągłe wdrożenie** | Każda zmiana, która przejdzie testy, automatycznie trafia do produkcji — bez ręcznej bramy |
### Typowe etapy rurociągu
| Scena | Co się dzieje | Narzędzia |
|-------|------------|-------|
| **Źródło** | Deweloper przesyła kod do Git | GitHub, GitLab, Bitbucket |
| **Buduj** | Skompiluj kod, zainstaluj zależności | Maven, Gradle, npm, pip |
| **Test** | Uruchom jednostkę, integrację, sprawdzanie lint | Jest, pytest, JUnit |
| **Pakiet** | Zbuduj obraz lub artefakt Dockera | Docker, pakiety kompilacji |
| **Wdrożenie (w fazie tymczasowej)** | Wdróż w środowisku przejściowym | Kubernetes, ECS, VM |
| **Test (staging)** | Testy integracyjne, testy dymne | Selen, listonosz |
| **Wdrożenie (produkcja)** | Dopuszczenie do produkcji | Niebiesko-zielony, kanarek, toczący się |
| **Monitor** | Obserwuj stan zdrowia, błędy, wydajność | Prometeusz, Grafana, Datadog |
### Porównanie narzędzi CI/CD
| Narzędzie | Wpisz | siła |
|------|------|--------------|
| **Działania na GitHubie** | Chmura CI/CD | Głęboko zintegrowany z GitHub; Przepływy pracy YAML |
| **GitLab CI** | Wbudowany CI/CD | Jedna platforma dla repo + potok |
| **Jenkins** | Własny host CI/CD | Wysoce konfigurowalne; ogromny ekosystem wtyczek |
| **KołoCI** | Chmura CI/CD | Szybko; dobre dla konteneryzowanych przepływów pracy |
| **ArgoCD** | GitOps dla Kubernetesa | Deklaratywne wdrożenia oparte na Git |
---

## Doker i kontenery
### Dlaczego kontenery?
Przed kontenerami klasyczny problem brzmiał: „działa na mojej maszynie”. Kontenery rozwiązują ten problem, pakując aplikację ze wszystkimi jej zależnościami – bibliotekami, środowiskiem wykonawczym, konfiguracją – w jedną, przenośną jednostkę, która działa identycznie w dowolnym miejscu.
### Podstawy Dockera
| Koncepcja | Opis |
|--------|------------|
| **Obraz** | Szablon tylko do odczytu z aplikacją + zależnościami |
| **Pojemnik** | Uruchamianie instancji obrazu |
| **Plik Dockera** | Przepis na budowanie wizerunku |
| **Rejestracja** | Przechowywanie obrazów (Docker Hub, ECR, GCR) |
| **Objętość** | Pamięć trwała, która przetrwa ponowne uruchomienie kontenera |
| **Sieć** | Izolowana warstwa sieciowa dla kontenerów |
### Najlepsze praktyki dotyczące pliku Dockerfile
```dockerfile
# Use specific base image tags, not 'latest'
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy dependency file first (leverage Docker layer caching)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Run as non-root user
USER appuser

# Expose port and define entrypoint
EXPOSE 8000
CMD ["python", "main.py"]
```

Kluczowe praktyki: używaj obrazów podstawowych typu slim/alpine, uruchamiaj jako użytkownik inny niż root, korzystaj z buforowania warstw, używaj `.dockerignore`, skanuj obrazy w poszukiwaniu luk ( `trivy`, `docker scan`) i ustawiaj limity zasobów.
### Tworzenie Dockera
Do jednoczesnego uruchamiania wielu kontenerów (aplikacja + baza danych + pamięć podręczna):
```yaml
services:
  app:
    build: .
    ports: ["8000:8000"]
    depends_on: [db, redis]
    environment:
      DATABASE_URL: postgresql://user:pass@db:5432/mydb
  db:
    image: postgres:16
    volumes: [pgdata:/var/lib/postgresql/data]
  redis:
    image: redis:7-alpine
volumes:
  pgdata:
```

---

## Kubernetes (K8s)
Kubernetes to standardowy w branży koordynator kontenerów. Zarządza wdrażaniem, skalowaniem i działaniem skonteneryzowanych aplikacji.
### Architektura podstawowa
| Składnik | Rola |
|----------|------|
| **Płaszczyzna sterująca** | Zarządza klastrem (serwer API, harmonogram itp., menedżer kontrolerów) |
| **Węzeł** | Maszyna robocza (VM lub fizyczna), na której działają kontenery |
| **Pod** | Najmniejsza jednostka do rozmieszczenia; jeden lub więcej kontenerów współdzielących sieć |
| **Obsługa** | Stabilny punkt końcowy sieci, który kieruje ruch do podów |
| **Wdrożenie** | Deklaratywna definicja pożądanego stanu pod (repliki, obraz itp.) |
| **Wejście** | Reguły routingu HTTP dla ruchu zewnętrznego |
| **Mapa konfiguracji / Sekret** | Konfiguracja i poufne dane wprowadzone do kapsuł |
### Podstawowe polecenia kubectl
```bash
kubectl get pods                    # List pods
kubectl get services                # List services
kubectl describe pod <name>         # Detailed pod info
kubectl logs <pod-name>             # View pod logs
kubectl exec -it <pod> -- /bin/sh   # Shell into a pod
kubectl apply -f deployment.yaml    # Apply a manifest
kubectl rollout status deploy/myapp # Check rollout progress
kubectl scale deploy/myapp --replicas=5  # Scale to 5 replicas
```

### Hełm
Helm jest menedżerem pakietów dla Kubernetes. **Wykres** to pakiet wstępnie skonfigurowanych zasobów Kubernetes. Pomyśl o tym jako o`apt`lub`brew`w przypadku K8.
```bash
helm install my-release bitnami/postgresql   # Install a chart
helm upgrade my-release bitnami/postgresql   # Upgrade
helm rollback my-release 1                   # Rollback to revision 1
helm list                                    # List releases
```

---

## Infrastruktura jako kod (IaC)
IaC traktuje konfigurację infrastruktury w ten sam sposób, w jaki traktujesz kod aplikacji: kontrolowaną wersję, testowaną i wdrażaną za pośrednictwem potoków.
### Terraform kontra Ansible
| Narzędzie | Wpisz | Podejście | Najlepsze dla |
|------|------|----------|---------|
| **Terraforma** | Zaopatrzenie | Deklaratywny (HCL); państwowe | Tworzenie zasobów chmurowych (VPC, VM, bazy danych) |
| **Ansible** | Konfiguracja | Deklaratywny (YAML); bez agenta | Konfiguracja serwerów, instalacja oprogramowania |
| **Pulumi** | Zaopatrzenie | Imperatyw (Python, Go, TS) | Zespoły preferujące prawdziwe języki programowania |
| **Formacja chmury** | Zaopatrzenie | Deklaratywny (YAML/JSON); Natywny dla AWS | Infrastruktura dostępna wyłącznie w AWS |
### Przykład Terraformy
```hcl
provider "aws" {
  region = "us-east-1"
}

resource "aws_instance" "web" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t3.micro"

  tags = {
    Name = "web-server"
  }
}
```

Najlepsze praktyki: używaj modułów do ponownego wykorzystania, przechowuj zdalnie stan (S3 + DynamoDB do blokowania), nigdy nie koduj na stałe sekretów i kontroluj wersję wszystkiego.
---

## Monitorowanie i obserwowalność
### Trzy filary
| Filar | Co ci to mówi | Narzędzia |
|--------|----------------------|------|
| **Dane** | Pomiary numeryczne w czasie (procesor, liczba żądań, stopa błędów) | Prometheus, CloudWatch, Datadog |
| **Dzienniki** | Dyskretne zdarzenia z kontekstem (błędy, żądania, zmiany stanu) | Stos ELK, Loki, dzienniki CloudWatch |
| **Ślady** | Kompleksowa podróż żądań między usługami | Jaeger, X-Ray, Zipkin |
### Prometeusz + stos Grafany
Standardowy stos monitorowania typu open source:
| Składnik | Rola |
|----------|------|
| **Prometeusz** | Baza danych szeregów czasowych; pobiera metryki z usług |
| **Grafana** | Wizualizacja i dashboardy |
| **Menedżer alertów** | Kieruje alerty do Slack, PagerDuty, e-mail |
| **Eksporter węzłów** | Ujawnia metryki na poziomie systemu (procesor, pamięć RAM, dysk) |
| **Eksporter Blackbox** | Sondy punktów końcowych (HTTP, TCP, ICMP) |
### Kluczowe wskaźniki do śledzenia
| Kategoria | Metryki |
|--------------|--------|
| **Infrastruktura** | Procesor, pamięć RAM, wykorzystanie dysku, sieciowe wejścia/wyjścia |
| **Aplikacja** | Częstotliwość żądań, opóźnienie (p50, p95, p99), stopa błędów |
| **Baza danych** | Liczba zapytań, powolne zapytania, wykorzystanie puli połączeń |
| **Biznes** | Rejestracje, konwersje, przychody |
---

## Strategie wdrażania
| Strategia | Jak to działa | Ryzyko | Wycofanie |
|---------|------------|------|---------|
| **Roczna aktualizacja** | Stopniowo zastępuj stare instancje nowymi | Niektórzy użytkownicy na starej, niektórzy na nowej wersji | Wróć do poprzedniego obrazu |
| **Niebiesko-zielony** | Uruchom dwa identyczne środowiska; przełączyć ruch | Podwójny koszt infrastruktury w okresie przejściowym | Natychmiastowe przełączenie z powrotem |
| **Kanarek** | Kieruj niewielki procent ruchu do nowej wersji; zwiększać stopniowo | Kompleksowe zarządzanie ruchem | Skieruj ruch z powrotem do stabilnej |
| **Flagi funkcji** | Wdróż kod, ale ukryj funkcje za przełącznikami | Złożoność kodu z logiki warunkowej | Wyłącz |
---

## GitOps
GitOps prowadzi IaC do logicznego wniosku: repozytorium Git jest jedynym źródłem prawdy o pożądanym stanie Twojej infrastruktury i aplikacji.
| Zasada | Opis |
|---------------|------------|
| **Oznajmujący** | Wszystko opisane jako kod (YAML, HCL) |
| **Wersja** | Git jest źródłem prawdy |
| **Automatyczne** | Narzędzia w sposób ciągły uzgadniają stan pożądany ze stanem rzeczywistym |
| **Audytowane** | Każda zmiana jest zatwierdzeniem Git |
**ArgoCD** i **Flux** to wiodące narzędzia GitOps dla Kubernetes. Wypychasz zmianę do repozytorium Git, a narzędzie automatycznie wdraża ją w klastrze.
---

## Reakcja na incydenty
Kiedy coś się psuje o 3 nad ranem:
1. **Potwierdź** alert.
2. **Oceń zakres**: jakich usług, użytkowników i danych dotyczy problem?
3. **Zidentyfikuj** główną przyczynę — sprawdź logi, metryki i ostatnie wdrożenia.
4. **Zawiera**, jeśli to możliwe — wyłączniki automatyczne, flagi charakterystyczne, zmiany ruchu.
5. **Napraw** — wycofanie lub aktualizacja.
6. **Komunikuj** — aktualizuj interesariuszy i użytkowników (strona statusu).
7. **Sekcja zwłok** — w ciągu 24–48 godzin udokumentować pierwotną przyczynę i kroki, jakie należy podjąć.
Celem nie jest tylko naprawienie incydentu, ale upewnienie się, że ten sam incydent nie powtórzy się.