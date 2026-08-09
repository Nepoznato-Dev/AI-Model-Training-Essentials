---
# Metadata
title: "Time Series and Forecasting"
description: "ARIMA, Prophet, LSTMs, seasonality, anomaly detection"
category: "AI and Machine Learning"
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
reviewed_by: "AI & Machine Learning Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [time, series, forecasting, ai-and-machine-learning]
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

# Szeregi czasowe i prognozowanie
Dane szeregów czasowych to wszelkie dane gromadzone w czasie: ceny akcji, odczyty temperatury, ruch na stronie internetowej, dane dotyczące sprzedaży, monitory tętna, zużycie energii. Prognozowanie oznacza przewidywanie przyszłych wartości w oparciu o wzorce z przeszłości. Jest to jedno z najcenniejszych zastosowań analityki danych w praktyce i jedno z najtrudniejszych, ponieważ przyszłość jest naprawdę niepewna, a szeregi czasowe w świecie rzeczywistym są pełne szumów, sezonowości i pęknięć strukturalnych.
---

## Charakterystyka szeregów czasowych
| Składnik | Opis | Przykład |
|---------------|------------|--------|
| **Tendencja** | Długoterminowy wzrost lub spadek | Globalne temperatury rosną od dziesięcioleci |
| **Sezonowość** | Regularne, przewidywalne wzorce w stałych odstępach czasu | Gwałtowny wzrost sprzedaży detalicznej w grudniu |
| **Cykliczność** | Wahania w niestałych odstępach czasu (często ekonomicznych) | Recesje co 5-10 lat |
| **Szum (szumowy)** | Losowa zmienność, której nie można wyjaśnić | Dzienne zmiany cen akcji |
| **Autokorelacja** | Aktualne wartości zależą od przeszłych wartości | Dzisiejsza temperatura jest podobna do wczorajszej |
### Stacjonarność
Szereg czasowy jest **stacjonarny**, jeśli jego właściwości statystyczne (średnia, wariancja) nie zmieniają się w czasie. Większość metod prognozowania zakłada stacjonarność.
| Testuj | Cel |
|------|-------------|
| **Wzmocniony Dickey-Fuller (ADF)** | Sprawdza, czy istnieje pierwiastek jednostkowy (niestacjonarny) |
| **Test KPSS** | Testuje, czy szereg jest stacjonarny w trendzie |
| Transformacja | Kiedy stosować |
|--------------|------------|
| **Różnica** | Usuń trend: y'(t) = y(t) - y(t-1) |
| **Transformacja dziennika** | Stabilizuj wariancję (dla wzrostu wykładniczego) |
| **Różnica sezonowa** | Usuń sezonowość: y'(t) = y(t) - y(t-s) gdzie s to długość sezonu |
---

## Klasyczne metody prognozowania
### Średnie kroczące
| Metoda | Opis | Najlepsze dla |
|------------|------------|---------|
| **Prosta średnia ruchoma (SMA)** | Średnia z ostatnich N obserwacji | Wygładzanie zaszumionych danych |
| **Ważona średnia krocząca** | Nowsze obserwacje zyskują większą wagę | Kiedy najnowsze dane mają większe znaczenie |
| **Wykładnicza średnia krocząca (EMA)** | Wykładniczo malejące wagi | Śledzenie trendów z mniejszym opóźnieniem |
### Wygładzanie wykładnicze
| Metoda | Komponenty | Przypadek użycia |
|--------|-----------|---------|
| **Proste (SES)** | Tylko poziom | Brak trendu, brak sezonowości |
| **Holt (podwójny)** | Poziom + trend | Dane z trendem, ale bez sezonowości |
| **Holt-Winters (potrójny)** | Poziom + trend + sezonowość | Dane z tendencją i sezonowością |
### ARIMA i warianty
ARIMA (AutoRegressive Integrated Moving Average) to koń pociągowy klasycznego prognozowania szeregów czasowych.
| Składnik | Znaczenie | Parametr |
|----------|---------|----------|
| **AR (p)** | Cofnij się do poprzednich wartości p | Ile przeszłych wartości należy użyć |
| **Ja (d)** | Liczba stopni różnicowania, aby uczynić stacjonarnym | Ile razy się różnić |
| **MA (q)** | Modeluj błąd jako kombinację błędów z przeszłości | Ile błędów z przeszłości użyć |
| Wariant | Rozszerzenie | Przypadek użycia |
|--------|-----------|---------|
| **SARIMA** | Dodaje składniki sezonowe (P, D, Q, s) | Dane o silnej sezonowości |
| **ARIMAX** | Dodaje zmienne zewnętrzne | Kiedy dowiesz się o nadchodzących wydarzeniach |
| **VAR** | Wielowymiarowa ARIMA; wiele współzależnych serii | Kiedy zmienne wpływają na siebie |
---

## Nowoczesne podejścia do uczenia maszynowego
### Modele oparte na LSTM i RNN
| Modelka | Architektura | Zaleta |
|-------|------------|---------------|
| **LSTM** | Sieć pamięci długoterminowej | Przechwytuje długoterminowe zależności czasowe |
| **GRU** | Bramkowana jednostka cykliczna (prostsza LSTM) | Szybszy trening; podobna wydajność |
| **Sekw.2Nast.** | Koder-dekoder szeregów czasowych | Elastyczne długości wejścia/wyjścia |
| **Tymczasowa sieć konwolucyjna (TCN)** | Rozszerzone zwoje przyczynowe | Szkolenie równoległe; długie pole recepcyjne |
### Prorok (Meta)
Praktyczne narzędzie prognostyczne przeznaczone dla biznesowych szeregów czasowych.
| Funkcja | Opis |
|--------|------------|
| **Rozkład** | Trend + sezonowość + wakacje |
| **Elastyczny** | Obsługuje brakujące dane, wartości odstające i przerwy strukturalne |
| **Zrozumiałe** | Komponenty są czytelne dla człowieka |
| **Automatyczny** | Rozsądne wartości domyślne; wymagane minimalne dostrojenie |
| siła | Ograniczenie |
|-------------|------------|
| Doskonały do ​​wskaźników biznesowych (sprzedaż, użytkownicy) | Nie jest idealny do danych o bardzo wysokiej częstotliwości |
| Obsługuje święta i imprezy specjalne | Zakłada addytywną lub multiplikatywną sezonowość |
| Odporny na wartości odstające | Mniej dokładne niż głębokie uczenie się w przypadku złożonych wzorców |
### Modele oparte na transformatorach
| Modelka | Kluczowa funkcja |
|-------|------------|
| **Informator** | ProbRzadka uwaga dla długich sekwencji |
| **Autoformator** | Mechanizm autokorelacji rozkładu szeregów |
| **PoprawkaTST** | Poprawia szeregi czasowe; niezależny od kanału |
| **TimesFM** (Google) | Podstawowy model szeregów czasowych; wstępnie przeszkolony na różnych danych |
| **Chronos** (Amazonka) | Tokenizuje szeregi czasowe; wykorzystuje architekturę w stylu LLM |
---

## Wykrywanie anomalii w szeregach czasowych
Wykrywanie nietypowych wzorców odbiegających od oczekiwanego zachowania.
| Metoda | Podejście | Przypadek użycia |
|--------|----------|---------|
| **Statystyczne** | Z-score, IQR, karty kontrolne | Proste, dobrze zrozumiałe |
| **Las Izolacji** | Oparty na drzewie; izoluje anomalie poprzez losowy podział | Wykrywanie anomalii wielowymiarowych |
| **LOF** (lokalny współczynnik odstający) | Oparte na gęstości; porównuje gęstość lokalną z sąsiadami | Gdy anomalie występują w regionach o niskim zagęszczeniu |
| **Autoenkodery** | Błąd rekonstrukcji; wysoki błąd = anomalia | Złożone, nieliniowe wzory |
| **Na podstawie LSTM** | Przewiduj następny krok; duży błąd przewidywania = anomalia | Anomalie sekwencyjne |
### Aplikacje
| Domena | Co oznaczają anomalie |
|------------|----------------------|
| **Finanse** | Oszustwa, krachy na rynku, awarie flash |
| **Opieka zdrowotna** | Nieprawidłowe tętno, początek drgawek |
| **Produkcja** | Awaria sprzętu, wady jakościowe |
| **Cyberbezpieczeństwo** | Próby włamań, ataki DDoS |
| **Infrastruktura** | Przeciążenie serwera, awarie sieci |
---

## Metryki oceny
| Metryczne | Formuła (koncepcyjna) | Kiedy stosować |
|--------|---------------------|------------|
| **MAE** (średni błąd bezwzględny) | Średnia błędów bezwzględnych | Interpretowalne; te same jednostki co dane |
| **RMSE** (średnia kwadratowa błędu) | Pierwiastek kwadratowy ze średniokwadratowych błędów | Karze za duże błędy więcej |
| **MAPE** (średni bezwzględny błąd procentowy) | Średnia bezwzględnych błędów procentowych | Kiedy liczy się błąd względny |
| **SMAPE** (MAPA symetryczna) | Symetryczna wersja MAPE | Lepiej radzi sobie z wartościami bliskimi zeru |
| **MASE** (średni bezwzględny błąd skalowany) | MAE względem naiwnej prognozy | Porównanie różnych serii |
---

## Praktyczny przebieg pracy
| Krok | Opis |
|------|------------|
| **1. Eksploruj** | Narysuj serię; zidentyfikować trend, sezonowość, wartości odstające |
| **2. Rozłożyć** | Podziel na komponenty trendowe, sezonowe i rezydualne |
| **3. Stacjonarne** | W razie potrzeby zastosuj różnicowanie lub przekształcenia |
| **4. Podziel** | Podział czasowy (nigdy nie losowy podział szeregów czasowych) |
| **5. Wartość bazowa** | Zacznij od naiwnej prognozy (ostatnia wartość, naiwność sezonowa) |
| **6. Modelka** | Wypróbuj metody klasyczne (ARIMA, Prophet), następnie metody ML |
| **7. Oceń** | Użyj odpowiednich wskaźników; porównać z wartością bazową |
| **8. Iteruj** | Dodaj funkcje, wypróbuj różne modele, dostosuj hiperparametry |
---

## Narzędzia i biblioteki
| Narzędzie | Cel |
|------|-------------|
| **modele statystyczne** | Klasyczne szeregi czasowe (ARIMA, ETS, dekompozycja) |
| **Prorok** (Meta) | Prognozowanie biznesowych szeregów czasowych |
| **czas** | Ujednolicony interfejs ML dla szeregów czasowych |
| **Rzutki** | Kompleksowa biblioteka prognostyczna (klasyczna + głębokie uczenie się) |
| **GluonTS** (Amazonka) | Probabilistyczne modelowanie szeregów czasowych |
| **NeuralProrok** | Prorok z elementami sieci neuronowej |
| **tsfresh** | Automatyczna ekstrakcja cech szeregów czasowych |
| **pandy** | Manipulacja szeregami czasowymi i ponowne próbkowanie |
---

## Streszczenie
Prognozowanie szeregów czasowych łączy klasyczne statystyki z nowoczesnym uczeniem maszynowym. Klasyczne metody (ARIMA, wygładzanie wykładnicze, Prorok) są łatwe w interpretacji, szybkie i często zaskakująco dokładne. Metody głębokiego uczenia się (LSTM, Transformers) wychwytują złożone wzorce, ale wymagają większej ilości danych i dostrojenia. Kluczowe zasady pozostają takie same niezależnie od metody: poznaj strukturę danych (trend, sezonowość, szum), zawsze porównuj je z prostą wartością bazową, oceniaj za pomocą odpowiednich wskaźników i pamiętaj, że przyszłość nigdy nie jest idealnym powtórzeniem przeszłości.