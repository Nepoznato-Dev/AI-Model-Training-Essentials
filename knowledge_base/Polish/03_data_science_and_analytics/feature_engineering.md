---
# Metadata
title: "Feature Engineering"
description: "Transformations, encodings, feature selection, dimensionality reduction"
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
tags: [feature, engineering, data-science-and-analytics]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "7 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# Inżynieria funkcji
Inżynieria cech to proces przekształcania surowych danych w reprezentacje, które zwiększają efektywność modeli uczenia maszynowego. Często określa się go jako najważniejszy krok w procesie uczenia maszynowego — funkcje, które nadajesz modelowi, mają większe znaczenie niż wybrany algorytm. Prosty model z dobrze przygotowanymi funkcjami zazwyczaj będzie przewyższał złożony model z surowymi, nieprzetworzonymi danymi wejściowymi. Sztuka polega na wystarczająco dobrym zrozumieniu zarówno dziedziny, jak i danych, aby stworzyć sygnały, z których model będzie mógł się uczyć.
---

## Dlaczego inżynieria funkcji ma znaczenie
| Czynnik | Wpływ |
|------------|------------|
| **Jakość sygnału** | Lepsze funkcje = wyraźniejsze wzorce do nauczenia się modelu |
| **Prostota modelu** | Dobre funkcje pozwalają prostszym modelom dobrze działać; mniejsze zapotrzebowanie na złożone architektury |
| **Prędkość treningu** | Odpowiednie, dobrze skalowane funkcje łączą się szybciej |
| **Uogólnienie** | Funkcje oparte na domenie pomagają modelom pracować na niewidocznych danych |
| **Interpretowalność** | Znaczące funkcje są łatwiejsze do wyjaśnienia zainteresowanym stronom |
---

## Rodzaje transformacji cech
### Przekształcenia numeryczne
| Transformacja | Formuła / Opis | Kiedy stosować |
|--------------|----------------------|------------|
| **Transformacja dziennika** | log(x) lub log(x + 1) | Rozkłady prawoskośne; wartości pieniężne |
| **Pierwiastek kwadratowy** | sqrt(x) | Umiarkowane pochylenie; zliczyć dane |
| **Box-Cox** | Transformacja parametryczna znajdująca najlepszą transformację mocy | Tworzenie bardziej normalnego rozkładu danych |
| **Yeo-Johnson** | Podobnie jak Box-Cox, ale obsługuje wartości ujemne | Przekrzywione dane z wartościami ujemnymi |
| **Standardyzacja** | (x - średnia) / std | Funkcje o różnych skalach; algorytmy zakładające normalność |
| **Skalowanie min.-maks.** | (x - min) / (maks. - min) | Ograniczanie funkcji do [0, 1]; wartości pikseli obrazu |
| **Solidne skalowanie** | (x - mediana) / IQR | Dane z wartościami odstającymi |
| **Kosowanie** | Konwertuj ciągłą na kategoryczną | Zależności nieliniowe; drzewa decyzyjne |
| **Cechy wielomianowe** | x², x³, x₁×x₂ | Wychwytywanie zależności nieliniowych w modelach liniowych |
### Kodowanie kategoryczne
| Kodowanie | Opis | Kiedy stosować |
|--------------|------------|------------|
| **Jedno-gorące kodowanie** | Utwórz kolumnę binarną dla każdej kategorii | Kategorie o niskiej kardynalności; modele oparte na drzewie obsługują natywnie |
| **Kodowanie etykiet** | Przypisz liczbę całkowitą do każdej kategorii | Kategorie porządkowe; modele oparte na drzewach |
| **Kodowanie docelowe** | Zamień kategorię na średnią zmiennej docelowej | Kategorie o dużej kardynalności; unikaj nadmiernego dopasowania przy wygładzaniu |
| **Kodowanie częstotliwości** | Zastąp kategorię liczbą lub częstotliwością | Kiedy sama częstotliwość ma charakter informacyjny |
| **Kodowanie binarne** | Konwertuj kategorie zakodowane w postaci liczb całkowitych na cyfry binarne | Wysoka kardynalność; zmniejsza wymiarowość w porównaniu z jednym gorącym |
| **Osadzanie** | Naucz się gęstej reprezentacji wektorowej | Bardzo wysoka kardynalność; NLP; systemy rekomendacyjne |
| **Kodowanie skrótu** | Hashuj kategorie do ustalonej liczby funkcji | Bardzo wysoka kardynalność; nauka online |
### Funkcje daty i godziny
| Funkcja | Opis |
|--------|------------|
| **Godzina** | Rejestruje wzorce dnia (godziny szczytu, noc) |
| **Dzień tygodnia** | Efekty dnia powszedniego a weekendu |
| **Miesiąc / kwartał** | Wzory sezonowe |
| **Jest weekend** | Flaga binarna na weekend |
| **Czy wakacje** | Flaga binarna na święta |
| **Czas od zdarzenia** | Dni od ostatniego zakupu; godziny od ostatniego logowania |
| **Kodowanie cykliczne** | sin(2π × godzina / 24), cos(2π × godzina / 24) — zachowuje cykliczną naturę czasu |
---

## Obsługa brakujących wartości
| Strategia | Opis | Kiedy stosować |
|--------------|------------|------------|
| **Upuść wiersze** | Usuń wiersze z brakującymi wartościami | Brakujące dane to niewielki ułamek; MCAR (brak całkowicie losowo) |
| **Upuść kolumny** | Usuń obiekty ze zbyt dużą liczbą brakujących wartości | Najczęściej brakuje tej funkcji; nie ważne |
| **Średnia/mediana imputacji** | Wypełnij średnią lub medianą | Prosty; zachowuje średnią, ale zmniejsza wariancję |
| **Przypisanie trybu** | Wypełnij kategoryczne najczęstszą wartością | Cechy kategoryczne |
| **imputacja KNN** | Użyj k-najbliższych sąsiadów, aby oszacować brakującą wartość | Gdy podobne przypadki pomagają przewidzieć brakującą wartość |
| **Przypisanie oparte na modelu** | Trenuj model w zakresie przewidywania brakujących wartości | Dokładniejsze; drogie obliczeniowo |
| **Brakujący wskaźnik** | Dodaj kolumnę binarną oznaczającą brak | Kiedy brak sam w sobie ma charakter informacyjny |
| **Interpolacja** | Wypełnij wartościami interpolowanymi (liniowe, splajnowe) | szeregi czasowe; uporządkowane dane |
---

## Wybór funkcji
### Metody filtrowania
| Metoda | Opis |
|------------|------------|
| **Korelacja** | Usuń cechy silnie ze sobą skorelowane |
| **Próg wariancji** | Usuń funkcje o wariancji bliskiej zeru |
| **Wzajemna informacja** | Zmierz informacje, jakie każda funkcja dostarcza na temat obiektu docelowego |
| **Chi-kwadrat** | Testuj niezależność między cechami kategorycznymi a celem |
| **Test F ANOVA** | Sprawdź, czy średnie wartości liczbowe różnią się w klasach docelowych |
### Metody opakowań
| Metoda | Opis |
|------------|------------|
| **Wybór do przodu** | Zacznij pusty; dodaj najlepszą funkcję pojedynczo |
| **Eliminacja wsteczna** | Zacznij od wszystkiego; usuń po kolei najgorszą cechę |
| **Eliminacja funkcji rekurencyjnych (RFE)** | Wielokrotnie trenuj model; usuń najmniej ważne funkcje |
### Metody wbudowane
| Metoda | Opis |
|------------|------------|
| **Regularyzacja L1 (Lasso)** | Zmniejsza nieistotne wagi funkcji do zera |
| **Ważność oparta na drzewie** | Użyj ważności funkcji z modeli drzewa |
| **Wartości SHAP** | Zmierz udział każdej funkcji w prognozach |
---

## Inżynieria funkcji specyficzna dla domeny
### Funkcje tekstowe
| Funkcja | Opis |
|--------|------------|
| **TF-IDF** | Częstotliwość terminów ważona odwrotną częstotliwością dokumentów |
| **Osadzanie słów** | Gęste wektory przechwytujące znaczenie semantyczne (Word2Vec, GloVe) |
| **N-gramy znaków** | Przechwytuj wzorce podsłów; przydatne w przypadku literówek i morfologii |
| **Statystyki tekstowe** | Długość; liczba słów; liczba zdań; średnia długość słowa |
| **Wyniki czytelności** | Flesch-Kincaid; Indeks mgły strzelającej |
### Funkcje szeregów czasowych
| Funkcja | Opis |
|--------|------------|
| **Funkcje opóźnienia** | Poprzednie wartości: y(t-1), y(t-7), y(t-30) |
| **Roczne statystyki** | Średnia, std, min, max nad oknem |
| **Różnica** | y(t) - y(t-1); oddaje trend |
| **Różnica sezonowa** | y(t) - y(t-12) dla danych miesięcznych z roczną sezonowością |
| **Warunki Fouriera** | Warunki sinus i cosinus dla wzorców sezonowych |
### Funkcje obrazu (przed głębokim uczeniem się)
| Funkcja | Opis |
|--------|------------|
| **HOG** (Histogram zorientowanych gradientów) | Rozkład kierunków krawędzi |
| **LBP** (lokalne wzorce binarne) | Opis tekstury |
| **SIFT** (Transformacja funkcji niezmiennej skali) | Deskryptory kluczowych punktów |
| **Histogramy kolorów** | Rozkład kolorów w obrazie |
---

## Najlepsze praktyki w zakresie inżynierii cech
| Praktyka | Opis |
|--------------|------------|
| **Unikaj wycieku danych** | Nigdy nie używaj informacji z przyszłości lub zestawu testowego do tworzenia funkcji |
| **Udokumentuj wszystko** | Zapisz, jakie przekształcenia zostały zastosowane i dlaczego |
| **Wersja Twoich funkcji** | Śledź zmiany funkcji wraz ze zmianami modelu |
| **Sprawdź z i bez** | Sprawdź, czy nowa funkcja rzeczywiście poprawia wydajność modelu |
| **Zachowaj powtarzalność** | Rurociągi inżynieryjne cech powinny być deterministyczne i powtarzalne |
| **Monitoruj dryf funkcji** | Dystrybucja funkcji może zmieniać się z biegiem czasu; monitorować i przekwalifikowywać |
---

## Streszczenie
Inżynieria funkcji to miejsce, w którym wiedza dziedzinowa łączy się z uczeniem maszynowym. To proces przekształcania surowych danych — niechlujnych, niekompletnych i wielowymiarowych — w czyste, informacyjne reprezentacje, z których modele mogą się uczyć. Transformacje numeryczne obsługują pochylenie i skalę. Kodowanie kategoryczne przekształca etykiety w liczby, z których mogą korzystać modele. Funkcje daty rejestrują wzorce czasowe. Strategie braku wartości obsługują niekompletne dane. Wybór funkcji eliminuje szum i redundancję. Najlepsi inżynierowie funkcji myślą jak detektywi: pytają, jakie sygnały powinny znajdować się w danych, gdzie te sygnały mogą być ukryte i jak je wyodrębnić w sposób uczciwy (bez wycieku danych), odtwarzalny i odporny na zmiany w czasie.