---
# Metadata
title: "Data Science and Analytics"
description: "Data processing, ML, big data, BI"
category: "Data Science and Analytics"
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
reviewed_by: "Data Science & Analytics Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [data, science, analytics, data-science-and-analytics]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "13 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# Nauka o danych i analityka
Nauka o danych to dyscyplina polegająca na przekształcaniu surowych danych w przydatne informacje. Znajduje się na skrzyżowaniu statystyki, informatyki i wiedzy dziedzinowej – i stało się niezbędne w każdym sektorze, od finansów po opiekę zdrowotną. W tym pliku omówiono podstawowe koncepcje, narzędzia i przepływy pracy, które powinien znać każdy specjalista.
---

## Proces nauki o danych
Większość projektów opiera się na pewnych odmianach **CRISP-DM**, standardowego cyklu życia:
| Faza | Co się dzieje | Typowy czas |
|-------|------------|-------------|
| **Zrozumienie biznesowe** | Zdefiniuj cele, wskaźniki sukcesu i ograniczenia | 10–15% |
| **Zrozumienie danych** | Zbieraj, eksploruj i profiluj dane | 10–15% |
| **Przygotowanie danych** | Oczyść, przekształć, zaprojektuj funkcje | ~50–60% |
| **Modelowanie** | Wybierz i trenuj modele | 10–15% |
| **Ocena** | Oceń wydajność względem celów biznesowych | 5–10% |
| **Wdrożenie** | Wyślij model do produkcji | 5–10% |
Powszechnie szacuje się, że przygotowywanie danych, a w szczególności ich czyszczenie, zajmuje około 80% czasu analityka danych.
---

## Typy danych w skrócie
| Wpisz | Opis | Przykład |
|------|------------|--------|
| **Strukturalne** | Uporządkowane w wierszach i kolumnach | Tabele SQL, arkusze kalkulacyjne |
| **Nieustrukturyzowany** | Brak predefiniowanego formatu | Tekst, obrazy, audio, wideo |
| **Półstrukturyzowany** | Pewna organizacja, ale elastyczna | JSON, XML, HTML |
| **Szereg czasowy** | Dane sekwencyjne indeksowane czasowo | Ceny akcji, odczyty czujników |
| **Przestrzenny** | Geograficzne lub oparte na lokalizacji | Współrzędne GPS, dane mapy |
| **Wykres** | Węzły i krawędzie reprezentujące relacje | Sieci społecznościowe, wykresy wiedzy |
---

## Podstawy statystyki
### Statystyka opisowa a statystyka wnioskowania
Statystyki opisowe podsumowują to, co *masz*; statystyki wnioskowania pozwalają wyciągnąć wnioski na temat tego, czego *nie* masz (szersza populacja).
| Koncepcja | Kluczowe pomysły |
|--------|-----------|
| **Tendencja centralna** | Średnia (wrażliwa na wartości odstające), mediana (silna), tryb (najczęściej) |
| **Rozproszenie** | Rozstęp, wariancja, odchylenie standardowe, rozstęp międzykwartylowy |
| **Kształt rozkładu** | Skośność (asymetria), kurtoza (ciężar ogona) |
| **Testowanie hipotez** | Hipoteza zerowa vs hipoteza alternatywna, wartości p, poziom istotności (α) |
| **Przedziały ufności** | Zakres prawdopodobnie zawierający prawdziwy parametr populacji |
| **Błędy typu I / typu II** | Fałszywie dodatnie (odrzucenie prawdziwej wartości null) / fałszywie ujemne (brak prawdziwego efektu) |
### Typowe testy statystyczne
| Testuj | Kiedy stosować |
|------|------------|
| **test t** | Porównaj średnie między dwiema grupami |
| **ANOVA** | Porównaj średnie z trzech lub więcej grup |
| **Chi-kwadrat** | Testuj niezależność zmiennych kategorycznych |
| **Mann-Whitney U** | Nieparametryczna alternatywa dla testu t (bez założenia normalności) |
| **Korelacja Pearsona** | Liniowa zależność pomiędzy dwiema zmiennymi ciągłymi |
| **Korelacja Spearmana** | Relacja monotoniczna (oparta na rangach, bardziej solidna) |
### Rozkłady prawdopodobieństwa, które warto znać
| Dystrybucja | Przypadek użycia |
|------------|---------|
| **Normalny** | Zjawiska naturalne, błędy pomiarowe — klasyczna krzywa dzwonowa |
| **Dwumianowy** | Liczenie sukcesów/porażek (rzuty monetą, współczynniki konwersji) |
| **Poissona** | Zliczanie zdarzeń w ustalonych odstępach czasu (połączenia na godzinę, defekty na partię) |
| **Wykładniczy** | Czas pomiędzy zdarzeniami (czasy oczekiwania, interwały awarii) |
| **t-dystrybucja** | Małe próbki lub nieznana wariancja populacji |
| **Chi-kwadrat** | Kategoryczna analiza danych, testy dobroci dopasowania |
---

## Zbieranie i przechowywanie danych
### Skąd pochodzą dane
Dane rzeczywiste pochodzą z wielu źródeł: relacyjnych baz danych, interfejsów API (REST, GraphQL), plików płaskich (CSV, JSON, Parquet), platform streamingowych (Kafka, Kinesis), ankiet i repozytoriów publicznych (Kaggle, portale rządowe). Otrzymany format w dużej mierze determinuje strategię przetwarzania wstępnego.
### Koncepcje hurtowni danych
| Koncepcja | Opis |
|--------|------------|
| **ETL** | Wyodrębnij → Przekształć → Załaduj — tradycyjne podejście potokowe |
| **ELT** | Wyodrębnij → Załaduj → Przekształć — nowoczesne podejście do chmury (ładuj surowo, przekształć w magazynie) |
| **Jezioro danych** | Surowe dane przechowywane w formacie natywnym (schemat podczas odczytu) |
| **hurtownia danych** | Ustrukturyzowane, przetworzone dane zoptymalizowane do analizy (schemat-on-write) |
| **Materiał danych** | Podzbiór magazynu ograniczony do jednego działu lub domeny |
| **Schemat gwiazdy** | Centralna tabela faktów otoczona tabelami wymiarów |
| **Schemat płatka śniegu** | Znormalizowane tabele wymiarów (mniejsza redundancja, więcej połączeń) |
### Typy baz danych
| Wpisz | Przykłady | Najlepsze dla |
|------|----------|---------|
| **Relacyjny (SQL)** | PostgreSQL, MySQL, Oracle | Dane strukturalne, transakcje ACID |
| **Dokument** | MongoDB, CouchDB | Elastyczne schematy, dane typu JSON |
| **Klucz-Wartość** | Redis, DynamoDB | Buforowanie, sesje, proste wyszukiwania |
| **Rodzina kolumn** | Cassandra, HBase | Obciążenia wymagające dużej ilości zapisu, szeregi czasowe |
| **Wykres** | Neo4j, Amazon Neptun | Relacje, sieci społecznościowe |
| **Seria czasowa** | InfluxDB, TimescaleDB | Metryki IoT, monitorowanie |
| **Wektor** | Szyszka, Milvus | Osadzanie pamięci dla wyszukiwania ML/AI |
---

## Wstępne przetwarzanie danych i inżynieria funkcji
### Lista kontrolna czyszczenia
Każdy prawdziwy zbiór danych ma problemy. Oto standardowe czyszczenie:
| Wydanie | Podejście |
|-------|--------------|
| **Brakujące wartości** | Imputacja (średnia, mediana, przewidywanie) lub usunięcie, jeśli jest rzadkie |
| **Wartości odstające** | Wykryj za pomocą IQR lub Z-score; traktować za pomocą cappingu lub transformacji |
| **Duplikaty** | Zidentyfikuj i usuń |
| **Niespójności** | Standaryzuj formaty, poprawiaj literówki, normalizuj jednostki |
### Techniki transformacji
| Technika | Co to robi |
|---------------|------------|
| **Normalizacja** | Skaluje wartości do zakresu 0–1 |
| **Standardyzacja** | Wynik Z: średnia = 0, std = 1 |
| **Jedno-gorące kodowanie** | Konwertuje kategorie na kolumny binarne |
| **Kodowanie etykiet** | Przypisuje etykiety całkowite do kategorii |
| **Transformacja dziennika** | Zmniejsza przesunięcie danych w prawo |
| **Kosowanie** | Grupuje wartości ciągłe w dyskretne segmenty |
### Inżynieria funkcji
Inżynieria funkcji często stanowi różnicę między modelem przeciętnym a świetnym. Kluczowe techniki obejmują:
- **Tworzenie funkcji**: Wyprowadzanie nowych kolumn z istniejących (np.`age_group`z`age`).
- **Wybór funkcji**: Metody filtrowania (korelacja), metody opakowujące (eliminacja rekurencyjna), metody osadzone (LASSO, znaczenie drzewa).
- **Redukcja wymiarowości**: PCA dla liniowego, t-SNE lub UMAP dla wizualizacji.
- **Warunki interakcji**: Wielokrotne łączenie cech w celu uchwycenia wspólnych efektów.
---

## Eksploracyjna analiza danych (EDA)
EDA to miejsce, w którym rozwijasz intuicję dotyczącą danych przed modelowaniem. Celem jest wykrycie wzorców, anomalii i zależności.
### Wybór odpowiedniego wykresu
| Typ wykresu | Najlepsze dla |
|----------|----------|
| **Histogram** | Rozkład pojedynczej zmiennej |
| **Działanka pudełkowa** | Podsumowanie pięciocyfrowe, wykrywanie wartości odstających |
| **Wykres punktowy** | Związek pomiędzy dwiema zmiennymi ciągłymi |
| **Mapa cieplna** | Macierze korelacji, wizualizacja gęstości |
| **Wykres słupkowy** | Porównywanie kategorii |
| **Wykres liniowy** | Trendy na przestrzeni czasu |
| **Fabuła skrzypcowa** | Gęstość rozkładu + podsumowanie wykresu pudełkowego |
| **Działka w parach** | Szybki przegląd wszystkich par zmiennych |
### Stos EDA języka Python
| Biblioteka | Rola |
|--------|------|
| **pandy** | Manipulacja i analiza danych |
| **nudne** | Obliczenia numeryczne |
| **matplotlib** | Planowanie fundamentów |
| **urodzony w morzu** | Wizualizacja statystyczna (zbudowana na matplotlib) |
| **fabuła** | Interaktywne wizualizacje internetowe |
| **scipy** | Obliczenia naukowe i statystyka |
---

## Uczenie maszynowe w nauce danych
### Nauka nadzorowana w skrócie
| Zadanie | Algorytmy |
|------|-----------|
| **Regresja** (przewiduj liczbę) | Liniowy, grzbiet/LASSO, drzewo decyzyjne, losowy las, wzmacnianie gradientowe (XGBoost, LightGBM) |
| **Klasyfikacja** (przewiduj kategorię) | Regresja logistyczna, k-NN, Naiwny Bayes, SVM, drzewa decyzyjne, losowy las, sieci neuronowe |
### Uczenie się bez nadzoru w skrócie
| Zadanie | Algorytmy |
|------|-----------|
| **Klastrowanie** | k-średnie, hierarchiczne, DBSCAN, modele mieszaniny Gaussa |
| **Redukcja wymiarowości** | PCA, t-SNE, UMAP, Autoenkodery |
| **Regulamin Stowarzyszenia** | Apriori, FP-Wzrost |
### Ocena modelu
| Typ metryki | Kluczowe wskaźniki |
|------------|------------|
| **Klasyfikacja** | Dokładność, precyzja, przypominanie, wynik F1, ROC-AUC, macierz zamieszania |
| **Regresja** | MAE, MSE, RMSE, R², skorygowane R² |
| **Weryfikacja** | k-krotna walidacja krzyżowa, warstwowa, podział szeregów czasowych |
| **Strojenie** | Przeszukiwanie siatki, wyszukiwanie losowe, optymalizacja bayesowska |
---

## Technologie dużych zbiorów danych
Kiedy zbiory danych przekraczają możliwości pojedynczej maszyny, na scenę wchodzi przetwarzanie rozproszone.
| Ramy | siła |
|----------|----------|
| **Iskra Apache** | Przetwarzanie w pamięci; Spark SQL, przesyłanie strumieniowe, MLlib, GraphX ​​|
| **Apache Hadoop** | MapReduce + HDFS — oryginalny stos dużych zbiorów danych |
| **Apache Flink** | Przetwarzanie strumieniowe z niskim opóźnieniem |
| **Promień Apache** | Ujednolicony model wsadowy i strumieniowy |
### Platformy danych w chmurze
| Dostawca | Kluczowe usługi |
|---------|------------|
| **AWS** | S3, EMR, przesunięcie ku czerwieni, SageMaker, klej |
| **Chmura Google** | BigQuery, Dataproc, platforma AI, przechowywanie w chmurze |
| **Lazur** | Synapse Analytics, kostki danych, uczenie maszynowe, jezioro danych |
| **Płatek śniegu** | Hurtownia danych natywna w chmurze (niezależna od dostawcy) |
### Orkiestracja rurociągów
| Narzędzie | Notatki |
|------|-------|
| **Przepływ powietrza Apache** | Norma branżowa; DAG oparte na Pythonie |
| **Prefekt** | Nowoczesna alternatywa z czystszym API |
| **Dagster** | Orkiestracja skoncentrowana na aktywach |
| **db** | Transformacja danych w oparciu o SQL w magazynie |
---

## Inteligencja biznesowa i analityka
### Porównanie narzędzi BI
| Narzędzie | Wpisz | siła |
|------|------|--------------|
| **Obraz** | Komercyjne | Bogata analityka wizualna, przeciągnij i upuść |
| **Power BI** | Komercyjne (Microsoft) | Głęboka integracja z Office/Azure |
| **Patrząc** | Komercyjne (Google) | Eksploracja danych, modelowanie LookML |
| **Metabaza** | Otwarte oprogramowanie | Łatwa konfiguracja, natywny język SQL |
| **Nadzbiór** | Oprogramowanie typu open source (Apache) | Skalowalny, oparty na SQL |
### Zasady projektowania pulpitów nawigacyjnych
Efektywne dashboardy opierają się na ustalonych zasadach: identyfikuj odbiorców, wybieraj odpowiednią wizualizację dla każdego wskaźnika, używaj kolorów strategicznie (a nie dekoracyjnie), utrzymuj spójne skale i umożliwiaj interaktywność (filtry, drążenie). Wydajność jest również ważna — pulpity nawigacyjne z długim czasem ładowania ograniczają adopcję użytkowników.
### Typowe kategorie KPI
| Kategoria | Przykłady |
|--------------|--------|
| **Finansowe** | Przychody, marża zysku, ROI, wartość życiowa klienta |
| **Klient** | Koszt nabycia (CAC), wskaźnik rezygnacji, NPS, wskaźnik satysfakcji |
| **Operacyjny** | Wskaźniki wydajności, czas cyklu, wskaźniki defektów |
| **Marketing** | Współczynnik konwersji, współczynnik klikalności, ROAS, atrybucja |
| **Produkt** | Aktywni użytkownicy dziennie, zaangażowanie, utrzymanie, przyjęcie funkcji |
---

## Zaawansowana analityka
| Podejście | Techniki | Kiedy stosować |
|---------|-----------|------------|
| **Przewidywanie** | Szeregi czasowe (ARIMA, Prophet, LSTM), modelowanie ryzyka, przewidywanie rezygnacji | Prognozowanie przyszłych wartości |
| **Przepisowy** | Programowanie liniowe, symulacja Monte Carlo, testy A/B, wieloręcy bandyci | Optymalizacja decyzji |
| **Analiza tekstu** | Tokenizacja, analiza sentymentów, modelowanie tematów (LDA), NER, osadzanie słów (Word2Vec, BERT) | Wydobywanie spostrzeżeń z tekstu |
---

## Etyka i zarządzanie danymi
### Regulamin prywatności
| Rozporządzenie | Zakres |
|----------|-------|
| **RODO** | podmioty danych z UE; prawo do usunięcia, zgody, przenoszenia danych |
| **CCPA** | Konsumenci z Kalifornii; rezygnacja ze sprzedaży danych |
| **HIPA** | Dane dotyczące opieki zdrowotnej w USA; ścisłe zasady poufności |
### Wymiary jakości danych
| Wymiar | Pytanie |
|----------|----------|
| **Dokładność** | Czy dane są prawidłowe? |
| **Kompletność** | Czy czegoś brakuje? |
| **Spójność** | Czy źródła są zgodne? |
| **Terminowość** | Czy jest aktualne? |
| **Ważność** | Czy jest zgodny z oczekiwanymi formatami? |
| **Wyjątkowość** | Czy są duplikaty? |
### Stronniczość i uczciwość
Błąd systematyczny może pojawić się na każdym etapie: błąd próbkowania (dane niereprezentatywne), błąd pomiaru (wadliwe instrumenty) lub błąd algorytmiczny (przewidywania dyskryminacyjne). Strategie łagodzące obejmują przetwarzanie wstępne (naprawianie danych), przetwarzanie w trakcie (ograniczanie modelu) i przetwarzanie końcowe (dostosowywanie wyników). Miary uczciwości, takie jak parytet demograficzny i równość szans, pomagają ilościowo określić problem.
---

## Ścieżki kariery
| Rola | Skup się |
|------|-------|
| **Analityk danych** | Analityka opisowa, dashboardy, raportowanie |
| **Naukowiec zajmujący się danymi** | Modelowanie statystyczne, ML, zaawansowana analityka |
| **Inżynier ML** | Produkcyjne systemy ML, wdrażanie modeli, MLOps |
| **Inżynier danych** | Potoki danych, infrastruktura, ETL |
| **Menedżer ds. analityki** | Kierowanie zespołem, strategia, zarządzanie interesariuszami |
| **Naukowiec** | Nowe algorytmy, publikacje |
---

## Pojawiające się trendy
- **AutoML**: Automatyczne tworzenie potoków i wybór modelu.
- **MLOps**: praktyki DevOps stosowane do zarządzania cyklem życia ML.
- **Sklepy z funkcjami**: Scentralizowane zarządzanie funkcjami do ponownego wykorzystania przez zespoły.
- **Data Mesh**: Zdecentralizowana architektura danych należąca do domeny.
- **LLM i generatywna sztuczna inteligencja**: duże modele językowe przekształcające przepływy pracy związane z tekstem, kodem i obrazem.
- **Edge Analytics**: przetwarzanie danych na urządzeniu, a nie w chmurze.
- **Wnioskowanie przyczynowe**: Wyjście poza korelację, aby zrozumieć rzeczywistą przyczynę i skutek.
- **Federacyjne uczenie się**: Uczenie modeli w oparciu o zdecentralizowane dane bez ich przenoszenia.
- **Odpowiedzialna sztuczna inteligencja**: etyka, wyjaśnialność i przejrzystość stają się standardowymi wymogami.