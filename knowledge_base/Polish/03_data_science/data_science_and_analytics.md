# Nauka o Danych i Analityka

## Podstawowe Pojęcia

### Czym jest Nauka o Danych?
Nauka o danych to dziedzina interdyscyplinarna, która wykorzystuje metody naukowe, procesy, algorytmy i systemy do wydobywania wiedzy i spostrzeżeń ze strukturyzowanych i niestrukturyzowanych danych. Łączy w sobie:
- **Statystyka**: Matematyczne podstawy analizy
- **Informatyka**: Programowanie, algorytmy, struktury danych
- **Ekspertyza Domenowa**: Wiedza merytoryczna
- **Wizualizacja Danych**: Efektywne komunikowanie wyników

### Typy Danych
- **Dane Strukturyzowane**: Zorganizowane w wierszach/kolumnach (bazy danych, arkusze kalkulacyjne)
- **Dane Niestrukturyzowane**: Bez predefined formatu (tekst, obrazy, audio, wideo)
- **Dane Półstrukturyzowane**: Pewna organizacja, ale nie sztywna (JSON, XML, HTML)
- **Dane Szeregów Czasowych**: Sekwencyjne punkty danych indeksowane w porządku czasowym
- **Dane Przestrzenne**: Informacje geograficzne/lokalizacyjne
- **Dane Grafowe**: Węzły i krawędzie reprezentujące relacje

### Proces Nauki o Danych (CRISP-DM)
1. **Zrozumienie Biznesu**: Zdefiniowanie celów i wymagań
2. **Zrozumienie Danych**: Zebranie i eksploracja początkowych danych
3. **Przygotowanie Danych**: Czyszczenie, transformacja i formatowanie danych (80% pracy)
4. **Modelowanie**: Wybór i zastosowanie technik modelowania
5. **Ewaluacja**: Ocena wydajności modelu względem celów
6. **Wdrożenie**: Implementacja modelu w środowisku produkcyjnym

## Podstawy Statystyki

### Statystyka Opisowa
- **Miary Tendencji Centralnej**: Średnia, mediana, dominanta
- **Miary Dyspersji**: Zakres, wariancja, odchylenie standardowe, rozstęp międzykwartylowy
- **Kształt Rozkładu**: Skośność (asymetria), kurtoza (ogony)
- **Percentyle i Kwartyle**: Pozycja wewnątrz rozkładu

### Statystyka Inferencyjna
- **Testowanie Hipotez**: Hipoteza zerowa, hipoteza alternatywna, wartości p
- **Przedziały Ufności**: Zakres wartości prawdopodobnie zawierający parametr populacji
- **Istotność Statystyczna**: Prawdopodobieństwo, że wyniki wystąpiły przez przypadek
- **Błąd Typu I**: Fałszywie dodatni (odrzucenie prawdziwej hipotezy zerowej)
- **Błąd Typu II**: Fałszywie ujemny (nieodrzucenie fałszywej hipotezy zerowej)
- **Moc**: Prawdopodobieństwo poprawnego odrzucenia fałszywej hipotezy zerowej

### Rozkłady Prawdopodobieństwa
- **Rozkład Normalny**: Krzywa dzwonowa, średnia = mediana = dominanta
- **Rozkład Dwumianowy**: Wyniki sukces/porażka
- **Rozkład Poissona**: Liczba zdarzeń w ustalonym przedziale
- **Rozkład Jednostajny**: Wszystkie wyniki jednakowo prawdopodobne
- **Rozkład Wykładniczy**: Czas między zdarzeniami
- **Rozkład t**: Małe próby, nieznana wariancja populacji
- **Rozkład Chi-Kwadrat**: Analiza danych kategorycznych

### Testy Statystyczne
- **Test t**: Porównanie średnich między dwiema grupami
- **ANOVA**: Porównanie średnich w wielu grupach
- **Test Chi-Kwadrat**: Test niezależności zmiennych kategorycznych
- **Manna-Whitneya U**: Nieparametryczna alternatywa dla testu t
- **Korelacja Pearsona**: Liniowa zależność między zmiennymi ciągłymi
- **Korelacja Spearmana**: Zależność monotoniczna (rangowa)
- **Kołmogorowa-Smirnowa**: Porównanie rozkładów

## Gromadzenie i Przechowywanie Danych

### Źródła Danych
- **Bazy Danych**: SQL, NoSQL, relacyjne, magazyny dokumentów
- **API**: REST, GraphQL, web scraping
- **Pliki**: CSV, JSON, XML, Parquet, Avro
- **Dane Strumieniowe**: Kafka, Kinesis, feedy w czasie rzeczywistym
- **Ankiety i Eksperymenty**: Pierwotne gromadzenie danych
- **Publiczne Zbiory Danych**: Dane rządowe, Kaggle, repozytoria akademickie

### Hurtownie Danych
- **ETL**: Proces Extract, Transform, Load
- **Jezioro Danych**: Przechowywanie surowych danych w formacie natywnym
- **Hurtownia Danych**: Strukturyzowane, przetworzone dane do analizy
- **Mart Danych**: Podzbiór hurtowni dla konkretnego działu
- **OLAP**: Online Analytical Processing, zapytania wielowymiarowe
- **Schemat Gwiazdy**: Tabele faktów otoczone tabelami wymiarów
- **Schemat Płatka Śniegu**: Znormalizowane tabele wymiarów

### Typy Baz Danych
- **Relacyjne (SQL)**: MySQL, PostgreSQL, Oracle, SQL Server
- **Dokumentowe**: MongoDB, CouchDB (dokumenty podobne do JSON)
- **Klucz-Wartość**: Redis, DynamoDB (proste pary klucz-wartość)
- **Kolumnowe**: Cassandra, HBase (zoptymalizowane dla kolumn)
- **Grafowe**: Neo4j, Amazon Neptune (węzły i relacje)
- **Szeregów Czasowych**: InfluxDB, TimescaleDB (dane z znacznikami czasu)
- **Wektorowe**: Pinecone, Milvus (przechowywanie embeddingów dla ML)

## Przetwarzanie Wstępne Danych

### Czyszczenie Danych
- **Brakujące Wartości**: Imputacja (średnia, mediana, dominanta, predykcja), usunięcie
- **Wartości Odchylone**: Wykrywanie (IQR, wynik Z), tratamiento (ograniczenie, transformacja)
- **Duplikaty**: Identyfikacja i usuwanie
- **Niespójności**: Standaryzacja formatów, poprawa literówek
- **Walidacja Danych**: Sprawdzanie ograniczeń, zakresów, typów

### Transformacja Danych
- **Normalizacja**: Skalowanie do zakresu 0-1
- **Standaryzacja**: Normalizacja Z-score (średnia=0, odchylenie std=1)
- **Kodowanie**: One-hot, etykietowe, porządkowe, kodowanie targetu
- **Binning**: Grupowanie wartości ciągłych w kategorie
- **Transformacja Logarytmiczna**: Redukcja skośności
- **Skalowanie Cech**: Uczynienie cech porównywalnymi

### Inżynieria Cech
- **Tworzenie Cech**: Wyprowadzanie nowych cech z istniejących
- **Selekcja Cech**: Wybór najbardziej istotnych cech
  - Metody filtrujące (korelacja, chi-kwadrat)
  - Metody opakowaniowe (rekurencyjna eliminacja cech)
  - Metody wbudowane (LASSO, ważność oparta na drzewach)
- **Redukcja Wymiarowości**: PCA, t-SNE, UMAP
- **Wyrazy Interakcji**: Łączenie cech multiplikatywnie
- **Cechy Wielomianowe**: Tworzenie wyrazów wyższego rzędu

## Eksploracyjna Analiza Danych (EDA)

### Techniki EDA
- **Statystyki Podsumowujące**: Opis tendencji centralnej, dyspersji, kształtu
- **Analiza Jednowymiarowa**: Rozkłady pojedynczej zmiennej
- **Analiza Dwuwymiarowa**: Relacje między dwiema zmiennymi
- **Analiza Wielowymiarowa**: Interakcje wielu zmiennych
- **Analiza Korelacji**: Identyfikacja relacji i multikolinearności
- **Segmentacja**: Grupowanie podobnych obserwacji

### Narzędzia Wizualizacji
- **Histogramy**: Rozkład pojedynczej zmiennej
- **Wykresy Pudełkowe**: Podsumowanie pięcioliczbowe, wykrywanie outliers
- **Wykresy Rozrzutu**: Relacja między dwiema zmiennymi ciągłymi
- **Mapy Cieplne**: Macierze korelacji, gęstość
- **Wykresy Słupkowe**: Porównania kategoryczne
- **Wykresy Liniowe**: Trendy w czasie
- **Wykresy Skrzypcowe**: Gęstość rozkładu z elementami wykresu pudełkowego
- **Pair Plots**: Wiele wykresów rozrzutu dla par zmiennych

### Biblioteki Pythona do EDA
- **pandas**: Manipulacja i analiza danych
- **numpy**: Obliczenia numeryczne
- **matplotlib**: Podstawowe wykresy
- **seaborn**: Wizualizacja statystyczna
- **plotly**: Interaktywne wizualizacje
- **scipy**: Obliczenia naukowe i statystyka

## Uczenie Maszynowe w Nauce o Danych

### Uczenie Nadzorowane
- **Regresja**: Przewidywanie wartości ciągłych
  - Regresja Liniowa
  - Regresja Wielomianowa
  - Ridge/LASSO/Elastic Net
  - Decision Tree Regressor
  - Random Forest Regressor
  - Gradient Boosting (XGBoost, LightGBM, CatBoost)

- **Klasyfikacja**: Przewidywanie etykiet kategorycznych
  - Regresja Logistyczna
  - k-Nearest Neighbors
  - Naive Bayes
  - Support Vector Machines
  - Decision Trees
  - Random Forest
  - Gradient Boosting
  - Neural Networks

### Uczenie Nienadzorowane
- **Klasteryzacja**: Grupowanie podobnych obserwacji
  - k-Means
  - Klasteryzacja Hierarchiczna
  - DBSCAN (oparta na gęstości)
  - Gaussian Mixture Models
  - Spectral Clustering

- **Redukcja Wymiarowości**: Redukcja liczby cech
  - Principal Component Analysis (PCA)
  - t-Distributed Stochastic Neighbor Embedding (t-SNE)
  - Uniform Manifold Approximation (UMAP)
  - Autoencoder

- **Reguły Asocjacji**: Znajdowanie współwystępujących elementów
  - Algorytm Apriori
  - FP-Growth

### Ewaluacja Modelu
- **Metryki Klasyfikacji**: Dokładność, precyzja, recall, F1-score, ROC-AUC, macierz konfuzji
- **Metryki Regresji**: MAE, MSE, RMSE, R², Adjusted R²
- **Cross-Validation**: k-fold, stratified, leave-one-out, time series split
- **Dostrajanie Hiperparametrów**: Grid search, random search, optymalizacja bayesowska
- **Krzywe Uczenia**: Diagnozowanie tradeoff bias-variance

## Technologie Big Data

### Frameworki Obliczeń Rozproszonych
- **Apache Hadoop**: MapReduce, HDFS (Hadoop Distributed File System)
- **Apache Spark**: Przetwarzanie in-memory, szybsze niż Hadoop
  - Spark SQL: Przetwarzanie danych strukturyzowanych
  - Spark Streaming: Dane w czasie rzeczywistym
  - MLlib: Biblioteka uczenia maszynowego
  - GraphX: Przetwarzanie grafów
- **Apache Flink**: Przetwarzanie strumieniowe z niskim opóźnieniem
- **Apache Beam**: Ujednolicone batch i streaming

### Platformy Chmurowe
- **AWS**: S3, EMR, Redshift, SageMaker, Glue
- **Google Cloud**: BigQuery, Dataproc, AI Platform, Cloud Storage
- **Azure**: Synapse Analytics, Databricks, Machine Learning, Data Lake
- **Snowflake**: Chmurowa hurtownia danych

### Narzędzia Pipeline Danych
- **Apache Airflow**: Orkiestracja workflow
- **Luigi**: Zarządzanie pipeline (Spotify)
- **Prefect**: Nowoczesna orkiestracja workflow
- **Dagster**: Orchestrator danych z fokusem na assetach
- **dbt**: Transformacja danych w hurtowni

## Business Intelligence i Analityka

### Narzędzia BI
- **Tableau**: Platforma analityki wizualnej
- **Power BI**: Analityka biznesowa Microsoft
- **Looker**: Eksploracja danych i insights (Google)
- **Qlik Sense**: Analityka asocjacyjna
- **Metabase**: Open-source BI
- **Superset**: Apache open-source BI

### Zasady Projektowania Dashboardów
- **Poznaj Swoją Publiczność**: Dostosuj do potrzeb użytkownika
- **Wybierz Właściwe Wizualizacje**: Dopasuj wykres do typu danych
- **Używaj Koloru Strategicznie**: Podkreślaj ważne informacje
- **Utrzymuj Spójność**: Standaryzuj formaty i skale
- **Włącz Interaktywność**: Filtry, drill-downs, tooltipy
- **Optymalizuj Wydajność**: Szybkie ładowanie, efektywne zapytania
- **Rozważenia Mobilne**: Design responsywny

### Key Performance Indicators (KPI)
- **Finansowe**: Przychody, marża zysku, ROI, customer lifetime value
- **Klienckie**: Koszt akwizycji, wskaźnik churn, score satysfakcji, NPS
- **Operacyjne**: Wskaźniki efektywności, czas cyklu, wskaźniki defektów
- **Marketingowe**: Wskaźniki konwersji, click-through rates, atrybucja
- **Produktowe**: Aktywni użytkownicy, engagement, retencja, adopcja funkcji

## Zaawansowana Analityka

### Analityka Predykcyjna
- **Prognozowanie**: Predykcja szeregów czasowych (ARIMA, Prophet, LSTM)
- **Modelowanie Ryzyka**: Scoring kredytowy, wykrywanie fraudów, ubezpieczenia
- **Analityka Klienta**: Predykcja churn, modelowanie skłonności
- **Prognozowanie Popytu**: Optymalizacja zapasów, łańcuch dostaw
- **Predykcja Konserwacji**: Antycypacja awarii sprzętu

### Analityka Preskryptywna
- **Optymalizacja**: Programowanie liniowe, programowanie całkowitoliczbowe
- **Symulacja**: Metody Monte Carlo, symulacja zdarzeń dyskretnych
- **Analiza Decyzyjna**: Drzewa decyzyjne, diagramy wpływu
- **Testy A/B**: Projektowanie eksperymentalne, istotność statystyczna
- **Multi-Armed Bandits**: Adaptatywne eksperymentowanie

### Text Analytics (NLP)
- **Przetwarzanie Wstępne Tekstu**: Tokenizacja, stemming, lemmatyzacja
- **Analiza Sentimentu**: Klasyfikacja pozytywny/negatywny/neutralny
- **Modelowanie Tematów**: LDA, NMF do odkrywania tematów
- **Named Entity Recognition**: Identyfikacja osób, miejsc, organizacji
- **Klasyfikacja Tekstu**: Wykrywanie spamu, kategoryzacja
- **Word Embeddings**: Word2Vec, GloVe, BERT

## Etyka i Zarządzanie Danymi

### Prywatność Danych
- **GDPR**: Rozporządzenie Ogólne o Ochronie Danych UE
- **CCPA**: California Consumer Privacy Act
- **HIPAA**: Health Insurance Portability and Accountability Act (amerykańska ochrona zdrowia)
- **Anonimizacja**: Usuwanie informacji identyfikujących osoby
- **Prywatność Różnicowa**: Dodawanie szumu do ochrony jednostek
- **Zarządzanie Zgodą**: Mechanizmy opt-in/opt-out

### Jakość Danych
- **Trafność**: Poprawność danych
- **Kompletność**: Wszystkie wymagane dane obecne
- **Spójność**: Brak sprzeczności między źródłami
- **Aktualność**: Dane dostępne gdy potrzebne
- **Ważność**: Zgodność z zdefiniowanymi regułami
- **Unikalność**: Brak duplikatów

### Bias i Sprawiedliwość
- **Bias Próbkowania**: Niereprezentatywne gromadzenie danych
- **Bias Pomiaru**: Wadliwe instrumenty gromadzenia danych
- **Bias Algorytmiczny**: Dyskryminujące predykcje modelu
- **Metryki Sprawiedliwości**: Paritet demograficzny, równość szans
- **Mitigacja Biasu**: Pre-processing, in-processing, post-processing

### Framework Zarządzania Danymi
- **Data Stewardship**: Odpowiedzialność za aktywa danych
- **Zarządzanie Metadanymi**: Dokumentacja danych o danych
- **Lineage Danych**: Śledzenie przepływu i transformacji danych
- **Kontrola Dostępu**: Uprawnienia oparte na rolach
- **Ścieżki Audytu**: Logowanie dostępu i zmian danych
- **Compliance**: Przestrzeganie regulacji

## Ścieżki Kariery w Nauce o Danych

### Role
- **Analityk Danych**: Fokus na analityce opisowej, dashboardach, raportowaniu
- **Data Scientist**: Modelowanie statystyczne, uczenie maszynowe, zaawansowana analityka
- **ML Engineer**: Produkcyjne systemy ML, wdrażanie modeli, MLOps
- **Data Engineer**: Pipeline danych, infrastruktura, procesy ETL
- **Analytics Manager**: Przywództwo zespołu, strategia, zarządzanie stakeholderami
- **BI Developer**: Tworzenie dashboardów, rozwój raportów
- **Research Scientist**: Nowe algorytmy, publikacje, zaawansowane badania

### Macierz Umiejętności
- **Techniczne**: Python/R, SQL, statystyka, frameworki ML, platformy chmurowe
- **Analityczne**: Rozwiązywanie problemów, myślenie krytyczne, projektowanie eksperymentów
- **Komunikacyjne**: Storytelling, wizualizacja, umiejętności prezentacji
- **Biznesowe**: Wiedza domenowa, zarządzanie stakeholderami, analiza ROI
- **Narzędzia**: Git, Jupyter, Docker, CI/CD, version control dla modeli

## Emerging Trends

### Obecne Rozwoje
- **AutoML**: Automatyczne tworzenie pipeline'ów uczenia maszynowego
- **MLOps**: Praktyki DevOps dla uczenia maszynowego
- **Feature Stores**: Centralizowane zarządzanie cechami
- **Data Mesh**: Zdecentralizowana architektura danych
- **LLM i AI Generatywne**: Duże modele językowe, generowanie treści
- **Edge Analytics**: Przetwarzanie danych na urządzeniach źródłowych
- **Analityka Rzeczywistego Czasu**: Analiza danych strumieniowych
- **Augmented Analytics**: Przygotowanie danych i insights wspomagane AI

### Przyszłe Kierunki
- **Quantum Machine Learning**: Obliczenia kwantowe dla ML
- **Federated Learning**: Trenowanie modeli na zdecentralizowanych danych
- **Inferencja Przyczynowa**: Przejście od korelacji do kauzalności
- **Responsywna AI**: Etyka, wyjaśnialność, transparentność
- **Data Fabric**: Zintegrowane zarządzanie danymi między środowiskami
