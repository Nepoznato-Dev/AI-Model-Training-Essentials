<!--
---
# Metadata
title: "Operations Research"
description: "Linear programming formulations, transportation and assignment problems, network flow optimization, integer programming, dynamic programming, queueing theory, inventory models, and scheduling"
category: "Data Science and Analytics"
subcategory: "Mathematics"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "Nepoznato-Dev"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.0"
    date: "2026-08-10"
    author: "Nepoznato-Dev"
    changes: "Initial deep-dive into operations research"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2027-02-10"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-10"

# Classification
tags: [operations-research, linear-programming, transportation-problem, dynamic-programming, queueing-theory, inventory-models, scheduling, network-flow]
difficulty_level: "intermediate"
prerequisites:
  - "mathematics.md"
  - "optimization.md"
  - "graph_theory.md"
estimated_reading_time: "25 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Badania operacyjne
Badania operacyjne (OR) to zastosowanie metod matematycznych w procesie decyzyjnym. Urodzony podczas II wojny światowej dla logistyki wojskowej, obecnie optymalizuje łańcuchy dostaw, planuje linie lotnicze, wyznacza trasy flot dostawczych, zarządza zapasami i alokuje zasoby w każdej branży. OR zapewnia matematyczny zestaw narzędzi umożliwiający podejmowanie najlepszych możliwych decyzji w ramach ograniczeń.
---

## Formuły programowania liniowego
### Formularz standardowy
Minimalizuj cᵀx
Z zastrzeżeniem: Ax = b, x ≥ 0
### Typowe formuły LP
**Mieszanka produktów:**
- Zmienne decyzyjne: xⱼ = ilość produktu j do wyprodukowania
- Cel: maksymalizacja zysku Σ pⱼxⱼ
- Ograniczenia: limity zasobów Σ aᵢⱼxⱼ ≤ bᵢ
**Problem z dietą:**
- Zmienne decyzyjne: xⱼ = ilość żywności j do kupienia
- Cel: minimalizacja kosztów Σ cⱼxⱼ
- Ograniczenia: wymagania żywieniowe Σ nᵢⱼxⱼ ≥ rᵢ
**Problem z mieszaniem:**
- Zmienne decyzyjne: xⱼ = proporcja składnika j w mieszance
- Cel: minimalizacja kosztów
- Ograniczenia: wymagania jakościowe (liczba oktanowa, wytrzymałość itp.)
### Przykład praktyczny: planowanie produkcji
Fabryka wytwarza produkty A i B.
- A wymaga 2 godzin pracy, 1 kg materiału; zysk 30 dolarów
- B wymaga 1 godziny pracy, 3 kg materiału; zysk 40 dolarów
- Dostępne: 40 godzin pracy, 30 kg materiału
**Formuła:**
- Maksymalizuj: 30x_A + 40x_B
- Z zastrzeżeniem: 2x_A + x_B ≤ 40 (praca)
- x_A + 3x_B ≤ 30 (materiał)
- x_A, x_B ≥ 0
**Rozwiązanie:** Wierzchołki obszaru wykonalnego: (0,0), (20,0), (18,4), (0,10)
- (0,0): zysk = 0
- (20,0): zysk = 600
- (18,4): zysk = 700 ← optymalny
- (0,10): zysk = 400
---

## Problem z transportem
Przenoszenie towarów z m źródeł do n miejsc docelowych przy minimalnych kosztach.
### Formuła
- Zmienne decyzyjne: xᵢⱼ = ilość wysłana ze źródła i do miejsca przeznaczenia j
- Cel: zminimalizować Σᵢ Σⱼ cᵢⱼxᵢⱼ
- Z zastrzeżeniem: Σⱼ xᵢⱼ = sᵢ (ograniczenia podaży)
- Σᵢ xᵢⱼ = dⱼ (ograniczenia popytu)
- xᵢⱼ ≥ 0
### Metody rozwiązania
| Metoda | Opis | Jakość rozwiązania początkowego |
|------------|------------|-------------------------------|
| **Róg północno-zachodni** | Zacznij od lewego górnego rogu, przydziel łapczywie | Wykonalne, ale często słabe |
| **Przybliżenie Vogla** | Weź pod uwagę koszty kar | Lepsze rozwiązanie początkowe |
| **MODI / Odskocznia** | Ulepsz początkowe rozwiązanie iteracyjnie | Znajduje optymalne |
### Sprawdzony przykład
| | D1 | D2 | D3 | podaż |
|---|----|----|----|--------|
| S1 | 2 | 3 | 1 | 50 |
| S2 | 4 | 1 | 5 | 30 |
| S3 | 3 | 2 | 4 | 20 |
| Popyt | 40 | 30 | 30 | 100 |
---

## Problem z przypisaniem
Przypisanie n pracowników do n stanowisk (jeden do jednego), aby zminimalizować całkowity koszt.
### Formuła
- Zmienne decyzyjne: xᵢⱼ ∈ {0, 1} (1 jeśli pracownik został przypisany do pracy j)
- Minimalizuj: Σᵢ Σⱼ cᵢⱼxᵢⱼ
- Z zastrzeżeniem: Σⱼ xᵢⱼ = 1 (każdy pracownik otrzymuje jedno miejsce pracy)
- Σᵢ xᵢⱼ = 1 (na każde stanowisko przypada jeden pracownik)
### Algorytm węgierski
| Nieruchomość | Wartość |
|---------|-------|
| Złożoność czasowa | O(n³) |
| Optymalny? | Tak |
| Podejście | Redukcja matrycy + pokrycie minimalne |
**Kroki:**
1. Odejmij minimum wierszy od każdego wiersza
2. Odejmij minimum kolumn od każdej kolumny
3. Zakryj wszystkie zera minimalną liczbą linii
4. Jeśli linie = n, znaleziono optymalne przypisanie wśród zer
5. W przeciwnym razie dostosuj matrycę i powtórz
---

## Optymalizacja przepływu sieci
### Minimalny przepływ kosztów
Biorąc pod uwagę sieć o przepustowości i kosztach na brzegach, znajdź przepływ, który zaspokoi wymagania przy minimalnych kosztach.
**Formuła:**
- Minimalizuj: Σ cᵢⱼxᵢⱼ
- Z zastrzeżeniem: zachowania przepływu w każdym węźle
- Ograniczenia wydajności: 0 ≤ xᵢⱼ ≤ uᵢⱼ
### Najkrótsza ścieżka jako przepływ sieci
Problem najkrótszej ścieżki jest szczególnym przypadkiem przepływu o minimalnych kosztach (wysłanie 1 jednostki z s do t).
### Aplikacje
| Aplikacja | Model sieci |
|------------|-------------|
| Łańcuch dostaw | Węzły = magazyny, krawędzie = szlaki żeglugowe |
| Komunikacja | Węzły = routery, krawędzie = łącza o przepustowości |
| Ruch | Węzły = skrzyżowania, krawędzie = drogi o przepustowości |
| Zarządzanie projektami | Sieci CPM/PERT |
---

## Programowanie dynamiczne
**Programowanie dynamiczne (DP)** rozwiązuje złożone problemy, dzieląc je na nakładające się podproblemy.
### Zasada optymalności Bellmana
Polityka optymalna ma tę właściwość, że niezależnie od stanu początkowego i decyzji, pozostałe decyzje muszą stanowić optymalną politykę dla stanu wynikowego.
### Kluczowe elementy
| Element | Opis |
|--------|------------|
| **Scena** | Punkt decyzji (krok czasowy, indeks pozycji) |
| **Stan** | Informacje potrzebne do podjęcia decyzji |
| **Decyzja** | Wybór dokonywany na każdym etapie |
| **Nawrót** | Optymalna wartość na etapie n ze względu na etap n−1 |
### Klasyczne problemy z DP
| Problem | Nawrót | Złożoność |
|--------|-----------|------------|
| **Fibonacciego** | F(n) = F(n−1) + F(n−2) | O(n) z zapamiętywaniem |
| **Plecak** | V(i,w) = max(V(i−1,w), vᵢ + V(i−1,w−wᵢ)) | O(nW) |
| **Najkrótsza ścieżka** | d(i) = min_j(d(j) + cⱼᵢ) | O(V²) lub O(E log V) |
| **Edytuj odległość** | D(i,j) = min(D(i−1,j)+1, D(i,j−1)+1, D(i−1,j−1)+koszt) | O(mn) |
| **Najdłuższy wspólny podciąg** | L(i,j) = L(i−1,j−1)+1, jeśli pasuje, w przeciwnym razie max(L(i−1,j), L(i,j−1)) | O(mn) |
| **Mnożenie łańcucha macierzy** | M(i,j) = min_k(M(i,k) + M(k+1,j) + pᵢ₋₁pₖpⱼ) | O(n³) |
### Przykład praktyczny: plecak 0/1
Pozycje: {waga: wartość} = {(2, 12), (3, 10), (4, 8), (5, 11)}. Pojemność W = 7.
V(i, w) = wartość maksymalna przy użyciu pierwszych elementów i o pojemności w
| ja\w | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|-----|---|---|---|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 1 | 0 | 0 | 12 | 12 | 12 | 12 | 12 | 12 |
| 2 | 0 | 0 | 12 | 12 | 12 | 22 | 22 | 22 |
| 3 | 0 | 0 | 12 | 12 | 12 | 22 | 22 | 22 |
| 4 | 0 | 0 | 12 | 12 | 12 | 22 | 23 | 23 |
Optymalnie: V(4, 7) = 23 (poz. 1 i 4: waga 2+5=7, wartość 12+11=23).
---

## Teoria kolejkowania
Teoria kolejek bada kolejki oczekujących – jak długie są, jak długo czekasz i jak skrócić obie te sytuacje.
### Notacja Kendalla
A/B/c/K/N/D gdzie:
- A = proces dotarcia (M = Markovian/Poissona, D = deterministyczny, G = ogólny)
- B = proces serwisowy (te same opcje)
- c = liczba serwerów
- K = pojemność (domyślnie ∞)
- N = populacja (domyślnie ∞)
- D = dyscyplina (FIFO, LIFO, Priorytet)
### Kolejka M/M/1 (pojedynczy serwer)
| Metryczne | Formuła |
|------------|--------|
| Wykorzystanie | ρ = λ/μ |
| Średnia liczba w systemie | L = ρ/(1−ρ) |
| Średni czas w systemie | W = 1/(μ-λ) |
| Średnia liczba w kolejce | L_q = ρ²/(1−ρ) |
| Średni czas oczekiwania | W_q = ρ/(μ−λ) |
gdzie λ = wskaźnik przybycia, μ = stawka za usługę, ρ = wykorzystanie.
### Kolejka M/M/c (wiele serwerów)
| Metryczne | Formuła |
|------------|--------|
| Wykorzystanie | ρ = λ/(cμ) |
| Prawdopodobieństwo oczekiwania (Erlang C) | P_w = złożona formuła zawierająca ρ i c |
| Średnia długość kolejki | L_q = P_w · ρ/(1−ρ) |
### Prawo Little’a
L = λW (średnia liczba w systemie = wskaźnik przybycia × średni czas)
Dotyczy to KAŻDEGO systemu kolejkowego, niezależnie od przylotów/rozkładu usług.
### Przykłady zastosowań
| Scenariusz | Model kolejki |
|---------|------------|
| Centrum telefoniczne | M/M/c (agenci c) |
| Żądania serwera WWW | M/M/1 lub M/G/1 |
| Nagły wypadek w szpitalu | M/G/c z priorytetami |
| Linia produkcyjna | Sieć kolejek |
| Planowanie procesora komputera | Udostępnianie procesora M/M/1 |
---

## Modele zapasów
### Ekonomiczna ilość zamówienia (EOQ)
Optymalna wielkość zamówienia minimalizująca całkowite koszty magazynowania.
Q* = √(2DS/H)
| Zmienna | Znaczenie |
|--------------|--------|
| D | Roczne zapotrzebowanie |
| S | Koszt zamówienia na zamówienie |
| H. | Koszt utrzymania na jednostkę rocznie |
| P* | Optymalna ilość zamówienia |
**Całkowity koszt w Q*:** TC = √(2DSH)
### Rozszerzenia
| Modelka | Rozszerzenie |
|-------|-----------|
| **EOQ ze zniżkami** | Rabaty ilościowe zmieniają funkcję kosztu |
| **Ilość zlecenia produkcyjnego** | Artykuły produkowane stopniowo, a nie dostarczane w całości |
| **Model (s, Q)** | Zmień kolejność jednostek Q, gdy zapasy spadną do poziomu s |
| **Model (s, S)** | Zamów do S, gdy stan zapasów spadnie do s |
| **Model sprzedawcy wiadomości** | Popyt jednookresowy, niepewny |
### Model sprzedawcy gazet
Optymalna wielkość zamówienia dla zapasów łatwo psujących się w jednym okresie:
P(D ≤ Q*) = c_u / (c_u + c_o)
gdzie c_u = koszt niepełnoletni (utracony zysk) i c_o = koszt nadwyżkowy (marnotrawstwo).
---

## Planowanie
### Planowanie sklepu pracy
| Notacja | Znaczenie |
|--------------|--------|
| n/m/J/C_max | n miejsc pracy, m maszyn, warsztat pracy, minimalizuj czas produkcji |
| Sklep z przepływem | Wszystkie zadania odwiedzają maszyny w tej samej kolejności |
| Sklep z pracą | Każde zadanie ma swoją własną sekwencję maszynową |
| Otwórz sklep | Brak ograniczeń dotyczących zamawiania |
### Zasady priorytetowe
| Zasada | Opis | Efekt |
|------|------------|-------|
| FCFS | Kto pierwszy, ten lepszy | Uczciwe, ale nie optymalne |
| SPT | Najpierw najkrótszy czas przetwarzania | Minimalizuje średnie ukończenie |
| EDD | Najpierw najwcześniejszy termin | Minimalizuje maksymalne spóźnienia |
| CR | Współczynnik krytyczny (pozostały termin płatności / czas przetwarzania) | Zrównoważony |
| LPT | Najpierw najdłuższy czas przetwarzania | Dobry do tworzenia kopii zapasowych na maszynach równoległych |
### Algorytm Johnsona (warsztat z przepływem 2 maszyn)
Dla n zadań na 2 maszynach, minimalizując czas trwania:
1. Znajdź ofertę z najkrótszym czasem przetwarzania
2. Jeśli jest na komputerze 1, zaplanuj go najpierw; jeśli na komputerze 2, zaplanuj to jako ostatnie
3. Usuń tę pracę i powtórz
Optymalny dla 2 maszyn; NP-twardy dla maszyn powyżej 3.
---

## Znaczenie dla uczenia maszynowego i nauki o danych
| Koncepcja LUB | Aplikacja |
|---------------|------------|
| Programowanie liniowe | Alokacja zasobów, optymalizacja portfolio, alokacja budżetu reklamowego |
| Transport/przydział | Logistyka, kojarzenie wspólnych przejazdów, przydzielanie zadań |
| Przepływ sieci | Optymalizacja łańcucha dostaw, routing ruchu w centrach danych |
| Programowanie dynamiczne | Dopasowanie sekwencji (bioinformatyka), algorytm Viterbiego (HMM), RL (równanie Bellmana) |
| Teoria kolejkowania | Planowanie wydajności serwerów, modelowanie opóźnień, alokacja zasobów w chmurze |
| Modele zapasów | Integracja prognozowania popytu, łańcuch dostaw ML |
| Harmonogram | Orkiestracja potoku ML, planowanie zadań GPU, planowanie wyszukiwania hiperparametrów |
| Programowanie całkowite | Wybór funkcji (binarny), wybór modelu, projekt sieci |
---

## Streszczenie
| Temat | Podstawowy problem | Kluczowa metoda |
|-------|------------|------------|
| Formuły LP | Optymalizuj cel liniowy z ograniczeniami | Simplex, punkt wewnętrzny |
| Transport | Wysyłaj towary po minimalnych kosztach | MODI, odskocznia |
| Zadanie | Dopasuj pracowników do stanowisk pracy | Algorytm węgierski |
| Przepływ sieci | Przepływ tras przez sieć | Algorytmy przepływu kosztów minimalnych |
| Programowanie dynamiczne | Nakładające się podproblemy | Zasada Bellmana, zapamiętywanie |
| Teoria kolejkowania | Analiza linii oczekujących | M/M/1, Prawo Little'a |
| Inwentarz | Kiedy i ile zamówić | EOQ, sprzedawca wiadomości |
| Harmonogram | Zadania sekwencyjne na maszynach | Reguły priorytetów, algorytm Johnsona |
Badania operacyjne przekształcają proces decyzyjny ze sztuki w naukę. Formułując matematycznie problemy rzeczywiste, OR zapewnia optymalne (lub prawie optymalne) rozwiązania problemów związanych z logistyką, planowaniem, alokacją zasobów i planowaniem, które mają wpływ na każdą branżę. Dla analityków danych metody OR uzupełniają uczenie maszynowe: podczas gdy ML przewiduje, OR zaleca – i razem tworzą one podstawę inteligentnych systemów decyzyjnych.