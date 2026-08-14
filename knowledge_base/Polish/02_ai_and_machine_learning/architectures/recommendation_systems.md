---
# Metadata
title: "Recommendation Systems"
description: "Collaborative filtering, content-based, hybrid, matrix factorisation"
category: "AI and Machine Learning"
subcategory: "Model Architectures"
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
    changes: "Moved to architectures/ subfolder; added subcategory field"
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
tags: [recommendation, systems, ai-and-machine-learning]
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
# Systemy rekomendacji
Systemy rekomendacji przewidują, co użytkownik będzie chciał w następnej kolejności zobaczyć, kupić lub z czym wejść w interakcję. Zasilają kanały treści w mediach społecznościowych, sugestie produktów w witrynach e-commerce, wybór filmów na platformach streamingowych i wyniki wyszukiwania. Mimo że są niewidoczne dla większości użytkowników, należą do systemów sztucznej inteligencji o największym wpływie komercyjnym na świecie — Netflix szacuje, że jego silnik rekomendacji pozwala zaoszczędzić ponad 1 miliard dolarów rocznie, zmniejszając odpływ abonentów.
---

## Dlaczego rekomendacje są trudne
| Wyzwanie | Opis |
|---------------|------------|
| **Skala** | Miliony użytkowników × miliony elementów = miliardy możliwych par |
| **Rzadkość** | Każdy użytkownik wszedł w interakcję z niewielką częścią dostępnych elementów |
| **Zimny ​​start** | Nowi użytkownicy i nowe elementy nie mają historii interakcji |
| **Preferencje dynamiczne** | Gusta użytkowników zmieniają się z biegiem czasu |
| **Poza dokładnością** | Zalecenia muszą być również różnorodne, nowatorskie i nieoczekiwane |
| **Cele biznesowe** | Maksymalizacja zaangażowania ≠ maksymalizacja dobrego samopoczucia użytkownika |
---

## Podstawowe podejścia
### Wspólne filtrowanie
Pomysł: jeśli użytkownicy A i B zgodzili się w przeszłości, prawdopodobnie zgodzią się w przyszłości.
| Wpisz | Jak to działa | Przykład |
|------|------------|--------|
| **Oparte na użytkownikach** | Znajdź podobnych użytkowników; polecają to, co im się podobało | „Użytkownicy, którym się to podobało, polubili także…” |
| **Na podstawie przedmiotu** | Znajdź podobne elementy do tego, co użytkownik już lubi | „Ponieważ oglądałeś…” |
| **Faktoryzacja macierzy** | Rozłóż macierz interakcji użytkownik-przedmiot na czynniki ukryte | SVD, ALS (naprzemienne metody najmniejszych kwadratów) |
| siła | słabość |
|---------|----------|
| Nie ma potrzeby rozumienia samych elementów | Problem z zimnym startem: nie mogę polecić nowych produktów |
| Przechwytuje złożone, ukryte preferencje | Wymaga dużej ilości danych dotyczących interakcji |
| Działa z każdym typem treści | Błąd popularności: poleca już popularne przedmioty |
### Filtrowanie oparte na treści
Polecaj przedmioty podobne do tych, które użytkownik już lubi, na podstawie cech przedmiotu.
| Typ funkcji | Przykład |
|------------|------------|
| **Tekst** | Gatunek, opis, słowa kluczowe, obsada |
| **Dźwięk** | Tempo, gatunek, nastrój (dla muzyki) |
| **Wizualne** | Paleta kolorów, styl (dla obrazów/mody) |
| **Metadane** | Cena, marka, kategoria |
| siła | słabość |
|---------|----------|
| Brak zimnego startu dla elementów (funkcje są znane) | Nie można polecać przedmiotów wykraczających poza gust użytkownika |
| Działa z mniejszą ilością danych dotyczących interakcji | Wymaga dobrej inżynierii funkcji |
| Wyjaśnialne („zalecane, ponieważ jest podobne do X”) | Mniej nieoczekiwanych wydarzeń |
### Podejścia hybrydowe
Większość systemów produkcyjnych łączy metody oparte na współpracy i treści.
| Strategia hybrydowa | Opis |
|----------------|------------|
| **Ważona** | Połącz wyniki z wielu modeli |
| **Przełączanie** | Korzystaj z treści w przypadku nowych użytkowników, współpracuj z istniejącymi |
| **Kaskada** | Najpierw użyj prostego modelu, a następnie udoskonal go za pomocą złożonego |
| **Kombinacja funkcji** | Połącz funkcje współpracy i treści w jeden model |
| **Meta-uczenie się** | Dowiedz się, jak łączyć różnych rekomendatorów |
---

## Nowoczesne podejścia do głębokiego uczenia się
### Modele z dwiema wieżami
Dominująca architektura rekomendacji na dużą skalę (wykorzystywana przez YouTube, Pinterest, Spotify).
| Składnik | Rola |
|----------|------|
| **Wieża użytkownika** | Sieć neuronowa, która koduje funkcje użytkownika i historię w osadzaniu |
| **Wieża przedmiotów** | Sieć neuronowa, która koduje cechy elementu w osadzaniu |
| **Podobieństwo** | Podobieństwo iloczynu kropkowego lub cosinusa pomiędzy osadzeniem użytkownika i elementu |
| Krok | Opis |
|------|------------|
| 1 | Wytrenuj obie wieże, aby tworzyły podobne osady dla par użytkownika-przedmiotów, które wchodzą w interakcję |
| 2 | W momencie udostępniania wstępnie oblicz osadzenie elementów |
| 3 | Na żądanie użytkownika oblicz osadzanie użytkownika |
| 4 | Użyj przybliżonego wyszukiwania najbliższego sąsiada (ANN), aby znaleźć najbardziej podobne elementy |
### Modele sekwencji dla rekomendacji
Zachowania użytkowników mają charakter sekwencyjny — to, co oglądałeś wczoraj, wpływa na to, co obejrzysz dzisiaj.
| Modelka | Podejście |
|-------|--------------|
| **GRU4Rec** | Model oparty na GRU dla rekomendacji opartych na sesjach |
| **SASRec** | Rekomendator sekwencyjny oparty na samouwadze |
| **BERT4Rec** | Transformator dwukierunkowy dla zaleceń sekwencyjnych |
| **DNN YouTube** | Głęboka sieć neuronowa traktująca historię oglądania jako sekwencję |
### Pobieranie a ranking
Nowoczesne systemy dzielą rekomendacje na dwa etapy:
| Scena | Cel | Metoda |
|-------|---------|--------|
| **Pobieranie (generowanie kandydatów)** | Zawęź miliony pozycji do ~1000 kandydatów | Model dwuwieżowy; wyszukiwanie ANN; szybki, ale przybliżony |
| **Ranking (punktacja)** | Precyzyjnie oceniaj i porządkuj kandydatów | Głęboki model z wieloma funkcjami; wolniej, ale dokładnie |
| **Ponowna klasyfikacja** | Dostosuj się do różnorodności, zasad biznesowych, świeżości | Kontekstowi bandyci; optymalizacja ograniczeń |
---

## Metryki oceny
| Metryczne | Co to mierzy | Kiedy stosować |
|------------|----------------------|------------|
| **Precyzja@K** | Część najważniejszych rekomendacji, które są istotne | Gdy zależy Ci na trafności najlepszych typów |
| **Przypomnij@K** | Część odpowiednich elementów znalezionych w górnym K | Kiedy zależy Ci na tym, żeby nie przegapić dobrych rzeczy |
| **NDCG** (znormalizowany zdyskontowany skumulowany zysk) | Jakość rankingu; nagrody podnoszące odpowiednie elementy | Kiedy kolejność w rankingu ma znaczenie |
| **MAPA** (średnia średnia precyzja) | Średnia precyzja wśród wszystkich użytkowników | Ogólna jakość rankingu |
| **Współczynnik trafień@K** | Czy co najmniej jeden odpowiedni element pojawia się w górnym K | Scenariusze trafności binarnej |
| **Zasięg** | Odsetek elementów, które są polecane | Różnorodność i sprawiedliwość |
| **Niezwykły przypadek** | Nieoczekiwane, ale istotne zalecenia | Zadowolenie użytkownika |
---

## Problem zimnego rozruchu
| Scenariusz | Wyzwanie | Rozwiązania |
|---------|-----------|----------|
| **Nowy użytkownik** | Brak historii interakcji | Użyj danych demograficznych; pokaż popularne przedmioty; używać sygnałów kontekstowych (lokalizacja, urządzenie, czas) |
| **Nowa pozycja** | Nikt jeszcze z tym nie współpracował | Korzystaj z funkcji treści; strategie eksploracji i eksploracji; algorytmy bandytów |
| **Nowy system** | Brak danych | Przenieś naukę z podobnych dziedzin; wikary początkową treść |
---

## Eksploracja a eksploatacja
| Strategia | Opis | Kompromis |
|---------|-------------|----------|
| **ε-chciwy** | Pokaż losowe elementy z prawdopodobieństwem ε | Proste, ale nieefektywne |
| **Próbkowanie Thompsona** | Próbka późniejszego rozkładu jakości przedmiotu | z zasadami; dobre właściwości teoretyczne |
| **Górna granica ufności (UCB)** | Preferuj pozycje o dużej niepewności | Dobra równowaga poszukiwań i eksploatacji |
| **Kontekstowi bandyci** | Eksploracja uwarunkowana kontekstem użytkownika | Bardziej efektywne niż ślepa eksploracja |
| **Zastrzyk różnorodności** | Celowo uwzględniaj różnorodne lub nowatorskie elementy | Prosty; może zmniejszyć zaangażowanie krótkoterminowe |
---

## Stronniczość i uczciwość
| Typ odchylenia | Opis | Wpływ |
|---------------|------------|-------|
| **Stronniczość popularności** | Popularne przedmioty są coraz częściej polecane i stają się coraz bardziej popularne | Pozycje z długim ogonem są niedoceniane |
| **Błąd selekcji** | Modele uczą się na podstawie zaobserwowanych interakcji, a nie wszystkich możliwych | Skierowany w stronę aktywnych użytkowników |
| **Stronniczość stanowiska** | Przedmioty wyświetlane na wyższych pozycjach uzyskują więcej kliknięć niezależnie od jakości | Wzmacnia najwyższe pozycje |
| **Błąd ekspozycji** | Przedmioty, które zostały pokazane, otrzymują więcej sygnału szkoleniowego | Pętla informacji zwrotnej |
| **Uprzedzenia demograficzne** | Zalecenia różnią się w zależności od grupy demograficznej w niesprawiedliwy sposób | Dyskryminacja; słabe doświadczenie niektórych grup |
### Strategie łagodzenia
| Strategia | Opis |
|---------|------------|
| **Odwrotne ważenie skłonności** | Puchowe popularne przedmioty na treningu |
| **Obniżanie warstw** | Dodaj komponent obniżający wartość do modelu |
| **Ograniczenia sprawiedliwości** | Dodaj ograniczenia, aby zapewnić równe traktowanie |
| **Różne rekomendacje** | Jawnie optymalizuj pod kątem różnorodności i trafności |
| **Audyt i monitoring** | Regularnie sprawdzaj zalecenia dotyczące stronniczości w różnych grupach |
---

## Przykłady branżowe
| Firma | Systemu | Podejście |
|--------|--------|---------|
| **Netflix** | Rekomendacje filmów/programów telewizyjnych | Odzyskiwanie dwóch wież + głęboki ranking + kontekstowi bandyci dla dzieł sztuki |
| **YouTube** | Rekomendacje wideo | Głęboka sieć neuronowa dla generacji kandydatów; odrębny model rankingowy |
| **Spotify** | Rekomendacje muzyczne | Wspólne filtrowanie + NLP na listach odtwarzania + analiza audio |
| **Amazonka** | Rekomendacje produktów | Wspólne filtrowanie „od elementu do elementu”; spersonalizowane na dużą skalę |
| **TikTok** | Krótki materiał wideo | Uczenie się przez wzmacnianie; duży nacisk na eksplorację |
| **Pinterest** | Rekomendacje wizualne | Model dwuwieżowy; podobieństwo wizualne |
---

## Narzędzia i struktury
| Narzędzie | Cel |
|------|-------------|
| **Rekomendatory TensorFlow (TFRS)** | Modele dwuwieżowe, wyszukiwanie, ranking |
| **PyTorch RecSys** | Modele rekomendacji zorientowane na badania |
| **Niespodzianka** | Klasyczne filtrowanie kooperacyjne (SVD, NMF, KNN) |
| **Ukryte** | Szybkie wspólne filtrowanie ukrytych informacji zwrotnych (ALS, BPR) |
| **Faiss** (Meta) | Przybliżone wyszukiwanie najbliższego sąsiada w skali |
| **Milvus / Pinecone / Weaviate** | Bazy danych wektorowych do wyszukiwania podobieństw |
| **Recbol** | Obszerna biblioteka badań rekomendacyjnych |
| **Merlin** (NVIDIA) | Potok rekomendacji przyspieszany przez GPU |
---

## Streszczenie
Systemy rekomendacji należą do najbardziej wpływowych zastosowań sztucznej inteligencji w przemyśle. Dziedzina ta ewoluowała od prostego filtrowania opartego na współpracy do architektur głębokiego uczenia się, które łączą historię użytkownika, zawartość przedmiotu, sygnały kontekstowe i cele biznesowe. Nowoczesne systemy wykorzystują potok wyszukiwania, rankingu i ponownego rankingu, z modelami dwuwieżowymi do szybkiego generowania kandydatów i głębokimi modelami do precyzyjnej punktacji. Wyzwania — zimny start, stronniczość, eksploracja i równoważenie zadowolenia użytkowników z celami biznesowymi — pozostają aktywnymi obszarami badań i inżynierii.