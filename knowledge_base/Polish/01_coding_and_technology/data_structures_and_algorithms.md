---
# Metadata
title: "Data Structures and Algorithms"
description: "Arrays, trees, graphs, sorting, searching, complexity"
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
tags: [data, structures, algorithms, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "6 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Struktury danych i algorytmy
Struktury danych to sposób, w jaki organizujemy dane w pamięci, aby operacje na nich były wydajne. Algorytmy to procedury rozwiązywania problemów krok po kroku. Razem stanowią one podstawę informatyki — opiera się na nich każdy program, którego kiedykolwiek używałeś. Wybór właściwej struktury danych może zamienić niemożliwie powolny program w szybki, a znajomość odpowiedniego algorytmu może zamienić nierozwiązywalny problem w trywialny.
---

## Podstawowe struktury danych
### Struktury liniowe
| Struktura | Dostęp | Szukaj | Wstaw | Usuń | Przypadek użycia |
|----------|--------|--------|--------|--------|---------------|
| **Tablica** | O(1) według indeksu | O(n) | O(n) | O(n) | Kolekcje o stałym rozmiarze; losowy dostęp |
| **Lista połączona** | O(n) | O(n) | O(1) na czele | O(1) na czele | Rozmiar dynamiczny; wstawienia/usunięcia |
| **Stos** | O(n) | O(n) | O(1) push/pop | O(1) pop | Wywołania funkcji; anulować; parsowanie |
| **Kolejka** | O(n) | O(n) | O(1) kolejka | O(1) usuń z kolejki | Planowanie zadań; BFS; kolejki wiadomości |
| **Deque** | O(1) na obu końcach | O(n) | O(1) na obu końcach | O(1) na obu końcach | Przesuwane okno; kradzież pracy |
### Struktury oparte na skrótach
| Struktura | Szukaj | Wstaw | Usuń | Przypadek użycia |
|----------|--------|--------|--------|----------|
| **Tabela mieszająca** | O(1) średnia | O(1) średnia | O(1) średnia | Wyszukiwanie klucz-wartość; skrytki; zestawy |
| **Zestaw skrótów** | O(1) | O(1) | O(1) | Testowanie członkostwa; deduplikacja |
**Kolizje skrótów**: gdy dwa klucze łączą się z tym samym gniazdem, są one przechowywane na połączonej liście (łączenie w łańcuch) lub w następnym dostępnym gnieździe (otwarte adresowanie). Dobre funkcje mieszające minimalizują kolizje.
### Struktury drzewne
| Struktura | Szukaj | Wstaw | Usuń | Przypadek użycia |
|----------|--------|--------|--------|----------|
| **Drzewo wyszukiwania binarnego** | O(log n) średnia | O(log n) | O(log n) | Posortowane dane; zapytania o zakres |
| **AVL / Drzewo czerwono-czarne** | O(log n) gwarantowane | O(log n) | O(log n) | Samorównoważenie; używane w mapach/zestawach |
| **B-Drzewo / B+ Drzewo** | O(log n) | O(log n) | O(log n) | Indeksy baz danych; systemy plików |
| **Spróbuj** | O(k) gdzie k = długość klucza | O(k) | O(k) | Autouzupełnianie; dopasowanie przedrostka |
| **Sterta (binarna)** | O(n) | O(log n) | O(log n) | Kolejki priorytetowe; planowanie |
### Reprezentacje wykresów
| Reprezentacja | Przestrzeń | Wyszukiwanie krawędzi | Dodaj krawędź | Powtarzaj sąsiadów |
|--------------|-------|-------------|--------------|---------------------------------|
| **Macierz sąsiedztwa** | O(V²) | O(1) | O(1) | O(V) |
| **Lista sąsiedztwa** | O(V + E) | O(stopień) | O(1) | O(stopień) |
| **Lista krawędzi** | O(E) | O(E) | O(1) | O(E) |
---

## Złożoność algorytmu (duże-O)
Notacja Big-O opisuje, w jaki sposób wymagania algorytmu dotyczące czasu i miejsca rosną wraz ze wzrostem rozmiaru danych wejściowych.
| Złożoność | Imię | Przykład |
|----------|------|--------|
| **O(1)** | Stała | Wyszukiwanie tabeli mieszającej; dostęp do tablicy według indeksu |
| **O(log n)** | Logarytmiczny | Wyszukiwanie binarne; zrównoważone operacje na drzewie |
| **O(n)** | Liniowy | Wyszukiwanie liniowe; iteracja tablicy |
| **O(n log n)** | Liniowy | Sortowanie przez scalanie; sortowanie sterty; najskuteczniejsze rodzaje ogólnego przeznaczenia |
| **O(n²)** | Kwadratowy | sortowanie bąbelkowe; zagnieżdżone pętle na tych samych danych |
| **O(2^n)** | wykładniczy | Generowanie podzbiorów metodą brute-force; naiwny rekurencyjny Fibonacciego |
| **O(n!)** | Silnia | Sprzedawca podróżujący (brutalna siła); permutacje |
### Powszechne błędne przekonania
| Błędne przekonanie | Rzeczywistość |
|-------------|--------|
| „O(n) jest zawsze szybsze niż O(n²)” | Dla małego n większy współczynnik ma znaczenie |
| „Niższe Big-O jest zawsze lepsze” | Istnieją kompromisy czasoprzestrzenne; Wyszukiwanie O(1) wykorzystuje pamięć O(n) |
| „Duże-O podaje dokładną prędkość” | Opisuje tempo wzrostu, a nie czas bezwzględny
---

## Algorytmy sortowania
| Algorytm | Najlepszy | Średnia | Najgorsze | Przestrzeń | Stabilny | Na miejscu |
|----------|------|---------|-------|-------|--------|---------------|
| **Sortowanie bąbelkowe** | O(n) | O(n²) | O(n²) | O(1) | Tak | Tak |
| **Sortowanie przez wstawianie** | O(n) | O(n²) | O(n²) | O(1) | Tak | Tak |
| **Sortowanie przez wybór** | O(n²) | O(n²) | O(n²) | O(1) | Nie | Tak |
| **Sortowanie przez scalanie** | O(n log n) | O(n log n) | O(n log n) | O(n) | Tak | Nie |
| **Szybkie sortowanie** | O(n log n) | O(n log n) | O(n²) | O(log n) | Nie | Tak |
| **Sortowanie sterty** | O(n log n) | O(n log n) | O(n log n) | O(1) | Nie | Tak |
| **Tim Sort** | O(n) | O(n log n) | O(n log n) | O(n) | Tak | Nie |
**Praktyczna rada**: użyj sortowania wbudowanego w swój język (`sorted()` w Pythonie,`Array.sort()`w JavaScript). Używają wysoce zoptymalizowanych algorytmów (Tim Sort, Introsort), które obsługują wszystkie przypadki Edge.
---

## Algorytmy wyszukiwania
| Algorytm | Struktura danych | Złożoność | Wymóg |
|----------|---------------|----------|------------|
| **Wyszukiwanie liniowe** | Dowolny | O(n) | Brak |
| **Wyszukiwanie binarne** | Posortowana tablica | O(log n) | Dane muszą być posortowane |
| **Wyszukiwanie tabeli mieszającej** | Tabela mieszająca | O(1) średnia | Dobra funkcja skrótu |
| **BFS** (wyszukiwanie wszerz) | Wykres / drzewo | O(V + E) | Nieważona najkrótsza ścieżka |
| **DFS** (przeszukiwanie w głąb) | Wykres / drzewo | O(V + E) | Znajdowanie ścieżki; wykrywanie cyklu |
| **Dijkstry** | Wykres ważony | O((V + E) log V) | Wagi nieujemne; najkrótsza ścieżka |
| **A* Szukaj** | Wykres ważony | O((V + E) log V) | Kierowane heurystyką; optymalny z dopuszczalną heurystyką |
---

## Kluczowe wzorce algorytmów
| Wzór | Opis | Przykładowe problemy |
|--------|------------|--------------------------------|
| **Dziel i zwyciężaj** | Podziel problem na podproblemy; rozwiązywać rekurencyjnie; połączyć | Sortowanie przez scalanie; szybkie sortowanie; wyszukiwanie binarne |
| **Programowanie dynamiczne** | Podziel się na nakładające się podproblemy; wyniki w pamięci podręcznej | Fibonacciego; plecak; najdłuższy wspólny podciąg |
| **Chciwy** | Na każdym etapie dokonaj lokalnie optymalnego wyboru | Dijkstry; kodowanie Huffmana; wybór aktywności |
| **Cofanie się** | Wypróbuj możliwości; cofnąć złe wybory; wypróbuj alternatywy | rozwiązanie sudoku; N-królowe; permutacje |
| **Przesuwane okno** | Utrzymuj okno elementów; przesuń go po danych | Maksymalna suma podtablicy o rozmiarze K; najdłuższy podciąg bez powtórzeń |
| **Dwa wskaźniki** | Użyj dwóch wskaźników poruszających się ku sobie lub w tym samym kierunku | Suma par w posortowanej tablicy; usuń duplikaty |
| **Wyszukiwanie binarne odpowiedzi** | Przeszukiwanie binarne przestrzeń odpowiedzi | Przydziel minimalną liczbę stron; agresywne krowy |
---

## Kiedy czego używać
| Problem | Struktura danych | Algorytm |
|--------|---------------|----------|
| Szybkie wyszukiwanie klucz-wartość | Tabela mieszająca / słownik | Haszowanie |
| Zachowaj posortowany porządek | Zrównoważony BST (TreeMap, std::set) | Operacje na drzewach |
| Przetwarzanie oparte na priorytetach | Kolejka sterty/priorytetu | Operacje na stercie |
| Najkrótsza ścieżka (nieważona) | Wykres (lista sąsiedztwa) | BFS |
| Najkrótsza ścieżka (ważona) | Wykres (lista sąsiedztwa) | Dijkstry / A* |
| Testowanie członkostwa | Zestaw skrótów / filtr Blooma | Haszowanie |
| Dopasowanie prefiksu | Spróbuj | Spróbuj przejścia |
| Zapytania o zakres | Drzewo segmentowe / drzewo Fenwicka | Operacje na drzewach |
| Pamięć podręczna LRU | Mapa mieszająca + podwójnie połączona lista | Połączone operacje |
| Połączone komponenty | Suma zbiorów rozłącznych (znalezienie Unii) | Związek i Znajdź |
---

## Streszczenie
Struktury danych i algorytmy to nie tylko tematy rozmów kwalifikacyjnych — to elementy składowe wydajnego oprogramowania. Tablice i tabele skrótów obsługują większość codziennych potrzeb. Drzewa i wykresy obsługują dane hierarchiczne i relacyjne. Sortowanie i wyszukiwanie to rozwiązane problemy w standardowych bibliotekach. Wzorce algorytmiczne – dziel i zwyciężaj, programowanie dynamiczne, zachłanność, wycofywanie się – to strategie wielokrotnego użytku do rozwiązywania nowych problemów. Kluczową umiejętnością nie jest zapamiętywanie algorytmów; polega na rozpoznaniu, który wzorzec pasuje do danego problemu i wybraniu odpowiedniej struktury danych dla danego zadania.