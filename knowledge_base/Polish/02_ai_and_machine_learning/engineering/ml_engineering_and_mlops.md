<!--
---
# Metadata
title: "ML Engineering and MLOps"
description: "Model serving, registries, deployment strategies, drift monitoring"
category: "AI and Machine Learning"
subcategory: "ML Engineering"
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
    changes: "Moved to engineering/ subfolder; added subcategory field"
  - version: "1.0.0"
    date: "2026-08-05"
    author: "Nepoznato-Dev"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-09"
review_date: "2027-02-05"
reviewed_by: "AI & Machine Learning Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [ml, engineering, mlops, ai-and-machine-learning]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "8 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Inżynieria ML i MLOps
Zbudowanie modelu uczenia maszynowego to tylko połowa sukcesu. Wprowadzanie go do środowiska produkcyjnego, utrzymywanie jego niezawodnego działania, monitorowanie dryfów i wykonywanie iteracji — tu z pomocą przychodzi inżynieria ML i MLOps. Ten plik obejmuje pełny cykl życia, od eksperymentu do systemu produkcyjnego.
---

## Cykl życia uczenia maszynowego
| Faza | Opis | Kluczowe działania |
|-------|------------|--------------|
| **1. Definicja problemu** | Sformułuj problem biznesowy jako zadanie ML | Zdefiniuj metryki, ograniczenia, kryteria sukcesu |
| **2. Gromadzenie danych** | Zbierz i oznacz dane szkoleniowe | ETL, etykietowanie, wzmacnianie |
| **3. Eksperyment** | Trenuj i oceniaj modele | Inżynieria funkcji, strojenie hiperparametrów |
| **4. Wybór modelu** | Wybierz najlepszy model | Porównaj wskaźniki, oceń kompromisy |
| **5. Wdrożenie** | Wyślij model do produkcji | Infrastruktura obsługująca, API, wsadowa |
| **6. Monitorowanie** | Uważaj na dryf i degradację | Dryf danych, dryf koncepcji, wydajność |
| **7. Przekwalifikowanie** | Zaktualizuj model o nowe dane | Zaplanowane lub uruchamiane przekwalifikowanie |
Większość wartości (i trudności) występuje w fazach 5–7. Modelka siedząca w notatniku Jupytera nie tworzy wartości biznesowej.
---

## Modelowe wzorce serwowania
| Wzór | Opis | Opóźnienie | Przypadek użycia |
|--------|------------|---------|--------------|
| **Wnioskowanie wsadowe** | Uruchom model na partii danych zgodnie z harmonogramem | Godziny | Codzienne rekomendacje, punktacja oszustw |
| **Wnioski online** | Przewidywanie w czasie rzeczywistym na żądanie | Milisekundy | Ranking wyszukiwania, klasyfikacja w czasie rzeczywistym |
| **Wnioski dotyczące transmisji strumieniowej** | Prognozy procesów w strumieniu danych | Sekundy | Wykrywanie anomalii, przetwarzanie zdarzeń |
### Infrastruktura obsługująca
| Narzędzie | Wpisz | Najlepsze dla |
|------|------|--------------|
| **Obsługa TensorFlow** | Serwer modelowy | Modele TensorFlow |
| **Służenie Pochodni** | Serwer modelowy | Modele PyTorcha |
| **Serwer wnioskowania Triton** | Wieloplatformowość | Wnioskowanie GPU, wiele frameworków |
| **vLLM** | Obsługa LLM | Wysokoprzepustowe wnioskowanie LLM |
| **BentoML** | Ujednolicone serwowanie | Wdrożenie niezależne od platformy |
| **Seldon** | Natywny dla K8s | Wdrożenie modelu Kubernetes |
| **Służenie promienia** | Skalowalne serwowanie | Duże modele, wnioskowanie rozproszone |
---

## Rejestry modeli
Rejestr modeli to scentralizowany magazyn służący do zarządzania modelami ML — ich wersjami, metadanymi, metrykami i stanem wdrożenia.
| Zdolność | Opis |
|---------------|------------|
| **Wersja** | Śledź każdą wersję modelu za pomocą unikalnego identyfikatora |
| **Metadane** | Dane treningowe, hiperparametry, metryki, autor |
| **Przejścia między etapami** | Przesuwaj modele przez etapy: Etapowanie → Produkcja → Archiwizacja |
| **Rodowód** | Śledź, które dane i kod wytworzyły każdy model |
| Narzędzie | Opis |
|------|------------|
| **MLprzepływ** | Otwarte oprogramowanie; model registry + experiment tracking |
| **Weights & Biases (W&B)** | Handlowy; experiment tracking + model registry |
| **DVC** | Data and model versioning with Git |
| **Azure ML / SageMaker** | Cloud-native model management |
---

## Śledzenie eksperymentu
Każdy eksperyment ML powinien być śledzony: jakie dane zostały wykorzystane, jakie hiperparametry, jakie metryki wynikły.
| Narzędzie | Kluczowe funkcje |
|------|------------|
| **MLprzepływ** | Open-source, hostowany samodzielnie, śledzi parametry/metryki/artefakty |
| **W&B** | Bogaty interfejs użytkownika, przeglądy, wersjonowanie artefaktów, raporty |
| **Neptun** | Magazyn metadanych dla MLOps |
| **Płyta Tensorowa** | Wbudowany w TensorFlow; wizualizuj krzywe treningowe |
### Co śledzić
| Kategoria | Przykłady |
|--------------|--------|
| **Parametry** | Szybkość uczenia się, wielkość partii, architektura modelu, liczba epok |
| **Dane** | Dokładność, strata, F1, AUC-ROC (na epokę i końcową) |
| **Artefakty** | Wagi modeli, macierze zamieszania, próbki predykcyjne |
| **Dane** | Wersja zbioru danych, współczynniki podziału, etapy przetwarzania wstępnego |
| **Środowisko** | Wersja Pythona, wersje bibliotek, sprzęt |
---

## Strategie wdrażania modeli
| Strategia | Jak to działa | Ryzyko |
|---------|------------|------|
| **Rozmieszczenie cienia** | Nowy model współpracuje ze starym; prognozy porównane, ale nie udostępnione | Zerowe ryzyko; sprawdza przed rozpoczęciem transmisji na żywo |
| **Wydanie kanarkowe** | Kieruj niewielki procent ruchu do nowego modelu; zwiększać stopniowo | Niskie ryzyko; szybkie wycofanie |
| **Testy A/B** | Podziel użytkowników na starych i nowych; porównaj wskaźniki biznesowe | Mierzy rzeczywisty wpływ |
| **Niebiesko-zielony** | Dwa identyczne środowiska; przełącz cały ruch na raz | Natychmiastowe wycofanie; podwójny koszt w okresie przejściowym |
| **Flagi funkcji** | Włączanie/wyłączanie modelu dla każdego segmentu użytkownika | Drobnoziarnista kontrola |
---

## Monitorowanie systemów ML
Systemy ML wymagają większego monitorowania niż tradycyjne oprogramowanie, ponieważ same dane mogą się zmieniać.
### Rodzaje driftu
| Typ dryfu | Jakie zmiany | Przykład |
|---------------|------------|--------|
| **Dryft danych** | Zmiany rozkładu wejść | Zmiana demograficzna klientów po kampanii marketingowej |
| **Dryf koncepcyjny** | Związek pomiędzy zmianami wejścia i wyjścia | Zmiany zachowań konsumentów w czasie recesji |
| **Przesunięcie etykiety** | Zmiany w dystrybucji docelowej | Wskaźnik oszustw wzrasta z 1% do 5% |
### Co monitorować
| Kategoria | Metryki |
|--------------|--------|
| **Wydajność modelu** | Dokładność, precyzja, przypominanie, F1, AUC (w porównaniu do wartości wyjściowych) |
| **Jakość danych** | Brakujące wartości, rozkłady cech, wartości odstające |
| **Wykrywanie dryfu** | Testy statystyczne (test KS, PSI, dywergencja KL) |
| **Infrastruktura** | Opóźnienie, przepustowość, wykorzystanie procesora graficznego, pamięć |
| **Wskaźniki biznesowe** | Współczynnik konwersji, wpływ na przychody, zadowolenie użytkowników |
### Narzędzia monitorowania
| Narzędzie | Wpisz |
|------|------|
| **Ewidentnie AI** | Monitorowanie dryfu danych open source i wydajności modelu |
| **Grafana** | Wizualizacja dashboardu (współpracuje z Prometheusem) |
| **DlaczegoLaboratoria** | Platforma obserwacji danych |
| **Arize** | Obserwowalność ML i analiza przyczyn źródłowych |
| **Prometeusz + Grafana** | Wskaźniki infrastruktury i aplikacji |
---

## Powtarzalne szkolenie
Powtarzalność oznacza, że ​​można przeprowadzić eksperyment ponownie i uzyskać ten sam wynik. Jest to niezbędne do debugowania, inspekcji i zapewniania zgodności.
### Wymagania
| Wymóg | Jak to osiągnąć |
|------------|----------------------|
| **Wersjonowanie danych** | DVC, Delta Lake lub migawki zestawu danych z skrótami |
| **Wersja kodu** | Git dla całego kodu szkoleniowego |
| **Przypinanie środowiska** | `requirements.txt`,`conda env`, Obrazy Dockera z dokładnymi wersjami |
| **Ustawienie nasion** | Napraw losowe nasiona dla numpy, torch, tensorflow |
| **Zarządzanie konfiguracją** | Konfiguracje Hydra, OmegaConf lub YAML dla wszystkich hiperparametrów |
| **Śledzenie artefaktów** | MLflow lub W&B do rejestrowania każdego eksperymentu |
---

## Wnioskowanie o skalowaniu
Gdy model musi obsłużyć miliony żądań dziennie, liczy się wydajność.
| Technika | Opis |
|---------------|------------|
| **Dozowanie** | Grupuj wiele żądań w jednym przekazie do przodu |
| **Kwantyzacja** | Zmniejsz precyzję modelu (FP32 → INT8 lub INT4), aby uzyskać szybsze wnioskowanie |
| **Destylacja modelowa** | Trenuj mniejszy model, aby naśladował większy |
| **Przycinanie** | Usuń nieistotne ciężary lub neurony |
| **Buforowanie** | Buforuj częste przewidywania, aby uniknąć ponownego obliczania |
| **Optymalizacja GPU** | TensorRT, środowisko wykonawcze ONNX, uwaga Flash |
| **Skalowanie poziome** | Uruchom wiele replik modelu za modułem równoważenia obciążenia |
---

## Flagi funkcji dla ML
Flagi funkcji pozwalają kontrolować, która wersja modelu obsługuje poszczególnych użytkowników, bez konieczności ponownego wdrażania.
| Przypadek użycia | Opis |
|---------|------------|
| **Stopniowe wdrażanie** | Podaj nowy model 5% użytkowników, a następnie zwiększ |
| **Wyłącznik awaryjny** | Natychmiast powróć do poprzedniego modelu, jeśli wykryte zostaną problemy |
| **Oparte na segmentach** | Różne modele dla różnych segmentów użytkowników |
| **Eksperymenty** | Warianty modelu testów A/B z metrykami biznesowymi |
Narzędzia: LaunchDarkly, Unleash, Flagsmith lub proste flagi funkcji oparte na bazie danych.
---

## Krzywa dojrzałości MLOps
| Poziom | Charakterystyka |
|------|----------------|
| **Poziom 0 — Ręczny** | Szkolenie ręczne, wdrażanie ręczne, brak monitorowania |
| **Poziom 1 — Eksperymentowanie** | Śledzenie eksperymentów, rejestr modeli, podstawowe CI |
| **Poziom 2 — Automatyka** | Automatyczne przekwalifikowanie, CI/CD dla modeli, testy automatyczne |
| **Poziom 3 — Pełny rurociąg** | Kompleksowy, zautomatyzowany potok z monitorowaniem, wykrywaniem dryftu i automatycznym ponownym szkoleniem |
Większość organizacji znajduje się gdzieś pomiędzy poziomem 0 a poziomem 1. Celem jest poziom 2–3, gdzie cykl życia uczenia maszynowego jest zautomatyzowany i samonaprawiający.