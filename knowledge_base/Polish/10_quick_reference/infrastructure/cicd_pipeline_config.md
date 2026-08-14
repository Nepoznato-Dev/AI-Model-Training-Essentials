<!--
---
# Metadata
title: "CI/CD Pipeline Configuration"
description: "GitHub Actions, GitLab CI, Jenkins, pipeline YAML patterns"
category: "Quick Reference"
subcategory: "Infrastructure"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "Nepoznato-Dev"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.1"
    date: "2026-08-09"
    author: "Nepoznato-Dev"
    changes: "Moved to infrastructure/ subfolder; added subcategory field"
  - version: "1.0.0"
    date: "2026-08-05"
    author: "Nepoznato-Dev"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-09"
review_date: "2027-02-05"
reviewed_by: "Quick Reference Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [cicd, pipeline, config, quick-reference]
difficulty_level: "beginner"
prerequisites: []
estimated_reading_time: "9 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Konfiguracja potoku CI/CD
Potoki ciągłej integracji (CI) i ciągłego wdrażania (CD) automatyzują proces tworzenia, testowania i wdrażania oprogramowania. W tym dokumencie omówiono wzorce konfiguracji dla najpopularniejszych platform CI/CD: GitHub Actions, GitLab CI i ogólne zasady projektowania potoków.
---

## Akcje w GitHubie
### Struktura przepływu pracy
```yaml
name: CI Pipeline
on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Set up language
        uses: actions/setup-python@v5
        with:
          python-version: '3.12'
      - name: Install dependencies
        run: pip install -r requirements.txt
      - name: Run tests
        run: pytest
      - name: Build
        run: python setup.py build
```

### Typowe wyzwalacze
| Wyzwalacz | Opis |
|--------|------------|
| `on: push`| Przy każdym naciśnięciu |
| `on: pull_request`| Na PR otwórz, zaktualizuj, otwórz ponownie |
| `on: schedule`| Harmonogram oparty na Cron |
| `on: workflow_dispatch`| Ręczny spust |
| `on: release`| Podczas tworzenia wydania |
| `on: workflow_call`| Wywoływane przez inny przepływ pracy (do ponownego użycia) |
### Kluczowe funkcje
| Funkcja | Opis |
|--------|------------|
| **Strategia matrycowa** | Uruchom to samo zadanie z różnymi konfiguracjami |
| **Sekrety** | Zaszyfrowane zmienne środowiskowe (`${{ secrets.MY_SECRET }}`) |
| **Środowiska** | Cele wdrożenia z regułami ochrony |
| **Buforowanie** | Zależności pamięci podręcznej między uruchomieniami |
| **Artefakty** | Prześlij pliki z zadań (raporty z testów, kompilacje) |
| **Przepływy pracy wielokrotnego użytku** | Udostępnij logikę przepływu pracy w repozytoriach |
| **Działania złożone** | Połącz wiele kroków w jedną akcję |
### Strategia matrycowa
```yaml
jobs:
  test:
    strategy:
      matrix:
        python-version: ['3.10', '3.11', '3.12']
        os: [ubuntu-latest, macos-latest]
    runs-on: ${{ matrix.os }}
    steps:
      - uses: actions/setup-python@v5
        with:
          python-version: ${{ matrix.python-version }}
```

---

## GitLab CI
### Struktura rurociągu
```yaml
stages:
  - build
  - test
  - deploy

build:
  stage: build
  script:
    - docker build -t myapp:$CI_COMMIT_SHA .
    - docker push myapp:$CI_COMMIT_SHA

test:
  stage: test
  script:
    - docker run myapp:$CI_COMMIT_SHA pytest

deploy:
  stage: deploy
  script:
    - deploy.sh $CI_COMMIT_SHA
  only:
    - main
  when: manual
```

### Słowa kluczowe
| Słowo kluczowe | Opis |
|--------|------------|
| `stages`| Zdefiniuj etapy rurociągu i ich kolejność |
| `stage`| Przypisz zadanie do etapu |
| `script`| Polecenia do wykonania |
| `before_script`| Polecenia uruchamiane przed głównym skryptem |
| `after_script`| Polecenia uruchamiane po skrypcie głównym (nawet w przypadku awarii) |
| `only / except`| Kontrola uruchamiania zadań (gałęzie, znaczniki) |
| `rules`| Bardziej elastyczna wersja tylko/z wyjątkiem |
| `variables`| Zdefiniuj zmienne CI/CD |
| `cache`| Pliki pamięci podręcznej między uruchomieniami potoku |
| `artifacts`| Pliki do przekazania pomiędzy zadaniami |
| `environment`| Środowisko wdrożenia |
| `when`| Kontroluj wykonanie zadania (w przypadku_sukcesu, w przypadku_porażki, ręcznie, zawsze) |
| `needs`| Określ zależności zadań (tryb DAG) |
| `extends`| Dziedzicz konfigurację z innego zadania |
| `include`| Importuj zewnętrzne pliki YAML |
### Predefiniowane zmienne
| Zmienna | Opis |
|---------|------------|
| `$CI_COMMIT_SHA`| Aktualny skrót zatwierdzenia |
| `$CI_COMMIT_REF_NAME`| Nazwa oddziału lub znacznika |
| `$CI_PIPELINE_ID`| Identyfikator rurociągu |
| `$CI_JOB_ID`| Identyfikator stanowiska |
| `$CI_PROJECT_DIR`| Pełna ścieżka do projektu |
| `$CI_REGISTRY`| Adres URL rejestru kontenerów |
| `$CI_DEFAULT_BRANCH`| Domyślna nazwa oddziału |
---

## Wzorce projektowe rurociągów
### Typowe wzorce
| Wzór | Opis |
|--------|------------|
| **Buduj raz, wdrażaj wiele** | Zbuduj artefakt raz; wdrożyć ten sam artefakt w każdym środowisku |
| **Kontrola bramek** | Ręczna akceptacja przed wdrożeniem produkcyjnym |
| **Flagi funkcji** | Wdróż w środowisku produkcyjnym, ale ukryj się za flagą funkcji |
| **Wdrożenie na Wyspach Kanaryjskich** | Wdróż w niewielkim procencie; monitor; rozwinąć |
| **Niebiesko-zielone wdrożenie** | Dwa identyczne środowiska; przełączyć ruch |
| **Testowanie równoległe** | Uruchamiaj zestawy testów równolegle, aby skrócić czas potoku |
| **Najpierw kłaczki** | Uruchom linters przed kosztownymi testami; szybko zawieść |
| **Zależności pamięci podręcznej** | Buforuj moduły węzłów, pip, Maven, aby przyspieszyć kompilacje |
### Etapy rurociągu (typowe)
| Scena | Cel |
|-------|-------------|
| **Lint** | Styl kodu i analiza statyczna |
| **Buduj** | Skompilować; pakiet; tworzyć artefakty |
| **Test jednostkowy** | Szybkie testy; brak zależności zewnętrznych |
| **Test integracji** | Testy z bazami danych; Pszczoła; usługi zewnętrzne |
| **Skanowanie bezpieczeństwa** | Luki w zabezpieczeniach zależności; tajne skanowanie; SAST |
| **Pakiet** | Utwórz obraz Dockera; artefakty wydania kompilacji |
| **Wdróż etapowanie** | Wdróż w środowisku przejściowym |
| **Test E2E** | Pełne testy systemu względem stagingu |
| **Wdrożenie produkcji** | Wdrożenie w środowisku produkcyjnym (ręczne lub automatyczne) |
| **Test dymu** | Sprawdź, czy wdrożenie jest w dobrym stanie |
---

## Strategie buforowania
| Język / Narzędzie | Ścieżka pamięci podręcznej | Przykład |
|----------------|-----------|--------|
| **Python (pip)** | `~/.cache/pip`| `actions/cache`z kluczem z skrótu`requirements.txt`|
| **Node.js (npm)** | `~/.npm`| `actions/setup-node`z wbudowanym buforowaniem |
| **Java (Maven)** | `~/.m2/repository`| Pamięć podręczna z kluczem z hasha`pom.xml`|
| **Java (Gradle)** | `~/.gradle/caches`| Pamięć podręczna z kluczem z hasha`build.gradle`|
| **Idź** | `~/go/pkg/mod`| Pamięć podręczna z kluczem z hasha`go.sum`|
| **Rdza (ładunek)** | `~/.cargo/registry`| Pamięć podręczna z kluczem z hasha`Cargo.lock`|
| **Doker** | Buforowanie warstwy Dockera | `docker/build-push-action`z pamięcią podręczną z |
---

## Rozwiązywanie problemów
| Problem | Rozwiązanie |
|--------|----------|
| **Rurociąg jest powolny** | Zależności pamięci podręcznej; zrównoleglać zadania; użyj mniejszych obrazów bazowych |
| **Sekrety niedostępne** | Sprawdź tajną nazwę; zweryfikować zakres środowiska; sprawdź ograniczenia PR widelca |
| **Artefakt za duży** | Wyklucz niepotrzebne pliki; kompres; użyj krótszego przechowywania |
| **Macierz za duża** | Zmniejsz kombinacje; użyj`include`/`exclude`|
| **Niestabilne testy** | Testy łuszczące się w kwarantannie; naprawić pierwotną przyczynę; spróbuj ponownie za pomocą`retry:`|
| **Odmowa pozwolenia** | Sprawdź zakresy tokenów; sprawdź uprawnienia biegacza |
---

## Streszczenie
Potoki CI/CD automatyzują tworzenie, testowanie i wdrażanie oprogramowania. GitHub Actions korzysta z przepływów pracy YAML wyzwalanych przez zdarzenia w repozytorium; GitLab CI wykorzystuje etapy i zadania z elastycznymi regułami. Kluczowe wzorce obejmują: kompilację raz, wdrożenie wielu; kontrole bram przed produkcją; najpierw lint, aby uzyskać szybką informację zwrotną; zależności pamięci podręcznej w celu przyspieszenia kompilacji; i zrównoleglić testy. Etapy potoku zazwyczaj przebiegają od lint → kompilacja → test → bezpieczeństwo → pakiet → wdrożenie → test dymu. Strategie buforowania różnią się w zależności od języka, ale opierają się na tej samej zasadzie: katalogi zależności pamięci podręcznej oznaczone skrótami plików blokujących. Celem jest szybka i niezawodna informacja zwrotna na temat każdej zmiany oraz bezpieczne i powtarzalne wdrożenia na produkcję.