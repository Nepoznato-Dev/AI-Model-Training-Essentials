<!--
---
# Metadata
title: "Data Engineering and Pipelines"
description: "ETL/ELT, data lakes, orchestration, Kafka, feature stores"
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
tags: [data, engineering, pipelines, ai-and-machine-learning]
difficulty_level: "intermediate"
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
# Inżynieria danych i rurociągi
Inżynieria danych to dyscyplina polegająca na budowaniu systemów, które przenoszą, przekształcają i przechowują dane na dużą skalę. Bez niezawodnych potoków danych nie można trenować modeli uczenia maszynowego, na pulpitach nawigacyjnych wyświetlane są nieaktualne liczby, a decyzje biznesowe opierają się na domysłach. Ten plik opisuje architekturę, narzędzia i praktyki tworzenia działającej infrastruktury danych.
---

## ETL kontra ELT
| Podejście | Jak to działa | Najlepsze dla | Narzędzia |
|---------|------------|---------|-------|
| **ETL** (Wyodrębnij → Przekształć → Załaduj) | Przekształć dane *przed* załadowaniem do magazynu | Tradycyjne magazyny z ograniczoną mocą obliczeniową | Informatyka, Talend, Apache NiFi |
| **ELT** (Wyodrębnij → Załaduj → Przekształć) | Najpierw załaduj surowe dane; przekształcić *wewnątrz* magazynu | Nowoczesne magazyny w chmurze z elastycznymi obliczeniami | dbt, Fivetran, Airbyte + BigQuery/Snowflake |
Przejście z ETL na ELT było spowodowane hurtowniami danych w chmurze (BigQuery, Snowflake, Redshift), które mogą skalować obliczenia niezależnie od pamięci masowej. Nie ma już potrzeby wstępnego przetwarzania wszystkiego przed załadowaniem.
---

## Jeziora danych a hurtownie danych
| Funkcja | Jezioro danych | Hurtownia danych |
|--------|-----------|--------------|
| **Format danych** | Surowy, natywny format (schemat podczas odczytu) | Ustrukturyzowany, przetworzony (schemat przy zapisie) |
| **Schemat** | Zdefiniowane w czasie zapytania | Zdefiniowane przed załadowaniem |
| **Typy danych** | Strukturalne, półstrukturalne, niestrukturalne | Głównie strukturyzowane |
| **Użytkownicy** | Analitycy danych, inżynierowie | Analitycy biznesowi, narzędzia BI |
| **Koszt** | Tańsze przechowywanie (przechowywanie obiektów) | Droższe (zoptymalizowane pod kątem zapytań) |
| **Przykłady** | AWS S3, Azure Data Lake, GCS | Płatek śniegu, BigQuery, Redshift |
Nowoczesne podejście to **lakehouse**: połącz tanie i elastyczne przechowywanie w jeziorze z funkcjami zarządzania i wydajnością magazynu. Kluczowymi technologiami są tutaj Delta Lake, Apache Iceberg i Apache Hudi.
---

## Architektura rurociągów
### Wsadowe a strumieniowe
| Tryb | Opis | Opóźnienie | Przypadek użycia |
|------|------------|---------|---------|
| **Partia** | Przetwarzaj dane w dużych porcjach w zaplanowanych odstępach czasu | Minuty do godzin | Codzienne raporty, zadania ETL, wzbogacanie danych |
| **Przesyłanie strumieniowe** | Przetwarzaj dane w sposób ciągły po ich otrzymaniu | Milisekundy do sekund | Panele kontrolne w czasie rzeczywistym, wykrywanie oszustw, alerty |
| **Mikropartia** | Małe partie w bardzo krótkich odstępach czasu | Sekundy | Praca w czasie niemal rzeczywistym i prostota wsadowa |
### Komponenty rurociągu
Typowy potok danych składa się z następujących etapów:
| Scena | Opis | Narzędzia |
|-------|------------|-------|
| **Połknięcie** | Zbieraj dane ze źródeł | Kafka, Airbyte, Fivetran, Debezium |
| **Transformacja** | Oczyść, wzbogacaj, agreguj | dbt, Spark, Pandy |
| **Przechowywanie** | Utrwalaj przetworzone dane | BigQuery, płatek śniegu, S3, jezioro Delta |
| **Podawanie** | Udostępnij dane konsumentom | Interfejsy API, dashboardy, sklepy z funkcjami ML |
| **Orkiestracja** | Planuj i zarządzaj zależnościami | Przepływ powietrza, prefekt, sztylet |
| **Monitorowanie** | Śledź stan rurociągu i jakość danych | Wielkie nadzieje, Monte Carlo, alerty niestandardowe |
---

## Narzędzia do orkiestracji
| Narzędzie | Podejście | siła |
|------|----------|---------|
| **Przepływ powietrza Apache** | DAG oparte na Pythonie; standard branżowy | Ogromny ekosystem, dojrzały, elastyczny |
| **Prefekt** | Natywny dla Pythona; czystsze API niż Airflow | Nowoczesny design, świetna obsługa błędów |
| **Dagster** | Skoncentrowany na aktywach; podejście do inżynierii oprogramowania | System typów, testowanie, obserwowalność |
| **Luigi** | Oryginalne narzędzie Spotify | Proste, ale mniej aktywnie rozwijane |
### Przykład przepływu powietrza
```python
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def extract():
    # Pull data from source
    pass

def transform():
    # Clean and process
    pass

def load():
    # Write to warehouse
    pass

with DAG("etl_pipeline", start_date=datetime(2024, 1, 1),
         schedule="@daily", catchup=False) as dag:
    e = PythonOperator(task_id="extract", python_callable=extract)
    t = PythonOperator(task_id="transform", python_callable=transform)
    l = PythonOperator(task_id="load", python_callable=load)
    
    e >> t >> l  # Define dependencies
```

---

## Apache Kafka
Kafka stanowi szkielet wielu systemów danych czasu rzeczywistego. Jest to rozproszony dziennik zdarzeń zapewniający przesyłanie komunikatów o wysokiej przepustowości i odporności na błędy.
### Podstawowe pojęcia
| Koncepcja | Opis |
|--------|------------|
| **Temat** | Kategoria wiadomości (np.`orders`,`user-events`) |
| **Podział** | Tematy są podzielone na partycje ze względu na równoległość |
| **Producent** | Aplikacja pisząca wiadomości do tematów |
| **Konsument** | Aplikacja czytająca wiadomości z tematów |
| **Grupa Konsumencka** | Grupa konsumentów, którzy dzielą obciążenie czytaniem tematu |
| **Przesunięcie** | Pozycja konsumenta w obrębie przegrody |
| **Broker** | Węzeł serwera Kafka |
### Kiedy używać platformy Kafka
- **Przesyłanie strumieniowe zdarzeń**: przetwarzanie zdarzeń w czasie rzeczywistym na dużą skalę.
- **Usługi oddzielenia**: Producenci i konsumenci nie muszą o sobie wiedzieć.
- **Powtórka**: Wiadomości są zachowywane; konsumenci mogą ponownie przeczytać z dowolnego przesunięcia.
- ** Przeciwciśnienie**: Kafka w naturalny sposób radzi sobie z różnicami prędkości pomiędzy producentami i konsumentami.
---

## Modelowanie danych
### Schemat gwiazdy a schemat płatka śniegu
| Schemat | Struktura | Plusy | Wady |
|--------|-----------|------|------|
| **Gwiazda** | Centralna tabela faktów otoczona zdenormalizowanymi tabelami wymiarów | Proste zapytania, szybkie odczyty | Redundancja danych |
| **Płatek śniegu** | Tabele wymiarów są znormalizowane (podzielone na podtabele) | Mniej redundancji | Więcej połączeń, wolniejsze zapytania |
### Tabele faktów i wymiarów
| Typ tabeli | Zawiera | Przykład |
|----------|----------|---------|
| **Fakt** | Mierzalne zdarzenia (metryki) | `orders`(id_zamówienia, identyfikator_produktu, identyfikator_klienta, kwota, data) |
| **Wymiar** | Atrybuty opisowe | `products`(id_produktu, nazwa, kategoria, cena),`customers`(id_klienta, nazwa, miasto) |
---

## Sklepy z funkcjami
Magazyn funkcji to scentralizowane repozytorium funkcji ML — wartości pochodnych używanych jako dane wejściowe do modeli (np. „średnia wartość zamówienia użytkownika z ostatnich 30 dni”).
| Zdolność | Opis |
|---------------|------------|
| **Rejestr funkcji** | Katalog dostępnych funkcji z metadanymi |
| **Sklep offline** | Historyczne funkcje uczenia modeli (wsadowego) |
| **Sklep internetowy** | Funkcja o niskim opóźnieniu służąca do wnioskowania w czasie rzeczywistym |
| **Monitorowanie funkcji** | Wykryj dryf, brakujące wartości, zmiany rozkładu |
| Narzędzie | Opis |
|------|------------|
| **Uczta** | Otwarte oprogramowanie; współpracuje z dowolnym frameworkiem ML |
| **Tekton** | Handlowy; platforma funkcji czasu rzeczywistego |
| **Chmiel** | Otwarte oprogramowanie; pełna platforma ML ze sklepem z funkcjami |
| **Magazyn funkcji Databricks** | Zintegrowany z Databricks/Spark |
---

## Jakość danych
Jakość danych to cichy zabójca projektów ML. Śmieci w środku, śmieci na zewnątrz.
### Wymiary jakości
| Wymiar | Pytanie |
|----------|----------|
| **Dokładność** | Czy dane odzwierciedlają rzeczywistość? |
| **Kompletność** | Czy wymagane pola są wypełnione? |
| **Spójność** | Czy wartości są zgodne we wszystkich źródłach? |
| **Terminowość** | Czy dane są aktualne? |
| **Ważność** | Czy wartości odpowiadają określonym regułom? |
| **Wyjątkowość** | Czy istnieją duplikaty rekordów? |
### Narzędzia do sprawdzania jakości danych
| Narzędzie | Podejście |
|------|--------------|
| **Wielkie oczekiwania** | Oparty na Pythonie; zdefiniuj „oczekiwania” dotyczące danych |
| **Monte Carlo** | Platforma obserwacji danych oparta na technologii ML |
| **testy dbt** | Wbudowane testy dla danych hurtowni (unique, not_null, relacje) |
| **Soda** | Skanowanie jakości danych typu open source |
---

## Zarządzanie danymi
Zarządzanie danymi zapewnia odpowiedzialne zarządzanie danymi w całej organizacji.
| Powierzchnia | Opis |
|------|------------|
| **Katalog danych** | Przeszukiwalna inwentaryzacja zbiorów danych z metadanymi (Amundsen, DataHub, Atlan) |
| **Pochodzenie danych** | Śledź, skąd pochodzą dane i jak je przekształcają |
| **Kontrola dostępu** | Uprawnienia oparte na rolach; kto co potrafi czytać/pisać |
| **Zgodność** | Przestrzeganie RODO, CCPA, HIPAA |
| **Własność danych** | Wyczyść własność każdego zbioru danych (zarządzanie) |
| **Zasady przechowywania** | Określ, jak długo dane są przechowywane i kiedy są usuwane |
---

## Nowoczesny stos danych
„Nowoczesny stos danych” odnosi się do typowej kombinacji narzędzi używanych obecnie przez zespoły zajmujące się danymi:
| Warstwa | Typowe narzędzia |
|-------|------------------|
| **Połknięcie** | Fivetran, Airbyte |
| **Magazyn** | Płatek śniegu, BigQuery, Redshift |
| **Transformacja** | db |
| **Orkiestracja** | Przepływ powietrza, prefekt, sztylet |
| **BI / Wizualizacja** | Looker, Metabaza, Tableau |
| **Odwrócony ETL** | Census, Hightouch (synchronizacja danych magazynowych z narzędziami) |
| **Jakość danych** | Wielkie nadzieje, Monte Carlo |
Trend zmierza w kierunku modułowych, najlepszych w swojej klasie narzędzi połączonych otwartymi standardami (SQL, modele dbt, DAG Airflow), a nie platformami monolitycznymi.