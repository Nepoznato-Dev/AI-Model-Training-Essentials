<!--
---
# Metadata
title: "Graph Theory"
description: "Graph representations, trees, traversals, shortest paths, minimum spanning trees, network flows, and spectral graph theory"
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
    changes: "Initial deep-dive into graph theory"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2027-02-10"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-10"

# Classification
tags: [graph-theory, trees, traversals, shortest-paths, spanning-trees, network-flows, spectral-graph-theory]
difficulty_level: "intermediate"
prerequisites:
  - "mathematics.md"
  - "discrete_mathematics.md"
estimated_reading_time: "28 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Teoria grafów
**Wykres** to struktura matematyczna składająca się z wierzchołków (węzłów) połączonych krawędziami (ogniwami). Wykresy modelują relacje: sieci społecznościowe, mapy drogowe, sieci neuronowe, zależności, kanały komunikacji. Teoria grafów – badanie tych struktur – dostarcza algorytmów i twierdzeń, które mają kluczowe znaczenie w informatyce, badaniach operacyjnych i nauce o danych.
---

## Podstawowe pojęcia
### Definicje
| Termin | Definicja | Notacja |
|------|------------|--------------|
| **Wykres** | Para G = (V, E) wierzchołków i krawędzi | G |
| **wierzchołek (węzeł)** | Element V | v, u, w |
| **Krawędź** | Połączenie pomiędzy dwoma wierzchołkami | e = (u, v) lub {u, v} |
| **Zamów** | Liczba wierzchołków | \|V\| = n |
| **Rozmiar** | Liczba krawędzi | \|E\| = m |
| **Stopień** | Liczba krawędzi przypadających na wierzchołek | stopień(v) |
| **Ścieżka** | Sekwencja różnych wierzchołków połączonych krawędziami | v₁, v₂, ..., vₖ |
| **Cykl** | Ścieżka rozpoczynająca się i kończąca w tym samym wierzchołku | v₁ → v₂ → ... → vₖ → v₁ |
| **Połączony** | Pomiędzy każdą parą wierzchołków | istnieje ścieżka — |
| **Komponent** | Maksymalny spójny podgraf | — |
| **Podgraf** | Wykres utworzony z podzbioru V i E | H ⊆ G |
### Rodzaje wykresów
| Wpisz | Opis | Przykład |
|------|------------|--------|
| **Nieskierowany** | Krawędzie nie mają kierunku | Sieć przyjaźni |
| **Reżyseria (dwuznak)** | Krawędzie mają kierunek (łuki) | Linki do stron internetowych |
| **Ważona** | Krawędzie noszą wartości liczbowe | Odległości drogowe |
| **Nieważone** | Wszystkie krawędzie są równoważne | Połączenia społeczne |
| **Proste** | Bez pętli, bez wielu krawędzi | Większość podręcznikowych wykresów |
| **Multigraf** | Dopuszczalne jest wielokrotne krawędzie pomiędzy tymi samymi wierzchołkami | Trasy lotów (wiele lotów pomiędzy miastami) |
| **Kompletny** | Każda para wierzchołków jest spójna | Kₙ ma n(n−1)/2 krawędzi |
| **Dwustronny** | Wierzchołki podzielone na dwie grupy; krawędzie tylko przecinają grupy | Matryce rekomendacji elementów użytkownika |
| **Płaski** | Można rysować bez skrzyżowań krawędzi | Układy płytek drukowanych |
| **Drzewo** | Spójny, acykliczny wykres | Drzewa decyzyjne, systemy plików |
| **DAG** | Reżyseria, brak ukierunkowanych cykli | Harmonogramowanie zadań, wykresy zależności |
### Lemat o uścisku dłoni
Suma stopni wszystkich wierzchołków jest równa dwukrotności liczby krawędzi:
Σᵥ deg(v) = 2|E|
**Wniosek:** każdy graf ma parzystą liczbę wierzchołków stopnia nieparzystego.
**Przykład:** W grupie 10 osób, gdzie każdy podaje rękę dokładnie 3 innym osobom: Σ deg = 30, więc |E| = łącznie 15 uścisków dłoni.
---

## Reprezentacje wykresów
Sposób przechowywania wykresu w pamięci określa wydajność każdego algorytmu, który na nim uruchamiasz.
| Reprezentacja | Przestrzeń | Wyszukiwanie krawędzi | Powtarzaj sąsiadów | Najlepsze dla |
|----------------|-------|------------|---------------------------------|--------------|
| **Macierz sąsiedztwa** | O(n²) | O(1) | O(n) | Gęste wykresy, szybkie testy brzegowe |
| **Lista sąsiedztwa** | O(n + m) | O(stopień(v)) | O(stopień(v)) | Rzadkie wykresy, większość sieci świata rzeczywistego |
| **Lista krawędzi** | O(m) | O(m) | O(m) | Proste algorytmy, MST Kruskala |
| **Macierz częstości występowania** | O(n · m) | O(m) | O(m) | Algorytmy specjalistyczne |
### Macierz sąsiedztwa
Macierz A n × n, gdzie A[i][j] = 1, jeśli krawędź (i,j) istnieje, 0 w przeciwnym razie. W przypadku wykresów ważonych A[i][j] = waga.
**Właściwości:**
- Symetryczny dla grafów nieskierowanych
- Aᵏ[i][j] = liczba przejść o długości k od i do j
- Wartości własne A ujawniają właściwości strukturalne (patrz teoria grafów spektralnych)
### Lista sąsiedztwa
Tablica (lub mapa mieszająca), w której każdy wierzchołek v przechowuje listę swoich sąsiadów.
```
Vertex 0: [1, 3]
Vertex 1: [0, 2, 3]
Vertex 2: [1, 3]
Vertex 3: [0, 1, 2]
```

Jest to najczęstsza reprezentacja wykresów świata rzeczywistego, które są zazwyczaj rzadkie (m ≪ n²).
---

## Drzewa
**Drzewo** to spójny, acykliczny graf nieskierowany. **Las** to rozłączny związek drzew.
### Właściwości drzew
Dla drzewa o n wierzchołkach:
- Ma dokładnie n − 1 krawędzi
- Między dowolnymi dwoma wierzchołkami istnieje dokładnie jedna ścieżka
- Usunięcie dowolnej krawędzi powoduje jej rozłączenie
- Dodanie dowolnej krawędzi tworzy dokładnie jeden cykl
### Rodzaje drzew
| Wpisz | Opis | Aplikacja |
|------|------------|------------|
| **Ukorzenione drzewo** | Jeden wierzchołek oznaczony jako pierwiastek | Systemy plików, schematy organizacyjne |
| **Drzewo binarne** | Każdy węzeł ma co najwyżej 2 dzieci | BST, parsowanie wyrażeń, drzewa decyzyjne |
| **Zrównoważone drzewo** | Wysokość wynosi O(log n) | Drzewa AVL, drzewa czerwono-czarne (bazy danych) |
| **Drzewo rozpinające** | Podgraf zawierający wszystkie wierzchołki i będący drzewem | Projektowanie sieci, algorytmy aproksymacyjne |
| **Minimalne drzewo rozpinające** | Drzewo rozpinające o minimalnej całkowitej masie krawędzi | Projektowanie sieci, klastrowanie |
| **Wykres gwiazdowy** | Jeden węzeł centralny połączony ze wszystkimi innymi | Sieci typu hub-and-szprychy |
### Właściwości drzewa binarnego
| Nieruchomość | Formuła |
|--------------|--------|
| Maksymalna liczba węzłów na głębokości d | 2ᵈ |
| Maksymalna liczba węzłów w drzewie o wysokości h | 2ʰ⁺¹ - 1 |
| Minimalna wysokość dla n węzłów | ⌊log₂(n)⌋ |
| Węzły liści w pełnym drzewie binarnym | Węzły wewnętrzne + 1 |
### Przejścia przez drzewa
| Przejście | Zamów | Przypadek użycia |
|----------|-------|---------|
| **Zamów w przedsprzedaży** | Korzeń → Lewo → Prawo | Kopiowanie drzewa, wyrażenie przedrostkowe |
| **W kolejności** | Lewo → Korzeń → Prawo | Posortowane dane wyjściowe z BST |
| **Wysyłka** | Lewo → Prawo → Korzeń | Usuwanie drzewa, wyrażenie przyrostkowe |
| **Kolejność poziomów (BFS)** | Poziom po poziomie, od lewej do prawej | Najkrótsza ścieżka w nieważonym drzewie |
---

## Przejścia wykresu
Algorytmy przechodzenia systematycznie odwiedzają każdy osiągalny wierzchołek.
### Wyszukiwanie wszerz (BFS)
Eksploruje wierzchołki warstwa po warstwie, używając **kolejki**.
| Nieruchomość | Wartość |
|---------|-------|
| Struktura danych | Kolejka (FIFO) |
| Złożoność czasowa | O(V + E) |
| Złożoność przestrzeni | O(V) |
| Znajduje najkrótszą ścieżkę? | Tak (wykresy nieważone) |
| Kompletny? | Tak (bada wszystkie osiągalne wierzchołki) |
**Algorytm:**
1. Zacznij od wierzchołka źródłowego s. Marek odwiedził. Kolejkuj s.
2. Gdy kolejka nie jest pusta: usuń wierzchołek z kolejki u. Dla każdego nieodwiedzonego sąsiada v z u: zaznacz v odwiedzone, kolejkuj v.
**Zastosowania:** najkrótsza ścieżka w grafach nieważonych, połączone komponenty, testowanie dwustronności, indeksowanie sieci.
### Wyszukiwanie w głąb (DFS)
Eksploruje tak głęboko, jak to możliwe, przed cofnięciem się, używając **stosu** (lub rekurencji).
| Nieruchomość | Wartość |
|---------|-------|
| Struktura danych | Stos (LIFO) / rekurencja |
| Złożoność czasowa | O(V + E) |
| Złożoność przestrzeni | O(V) |
| Znajduje najkrótszą ścieżkę? | Nie |
| Kompletny? | Tak (dla grafów skończonych) |
**Algorytm:**
1. Zacznij od wierzchołka s. Marek odwiedził.
2. Dla każdego nieodwiedzonego sąsiada v z s: rekurencyjnie DFS z v.
**DFS klasyfikuje krawędzie na:**
- **Brzegi drzewa:** część drzewa DFS
- **Tylne krawędzie:** łączą wierzchołek z jego przodkiem (wskazują cykle)
- **Przednie krawędzie:** łączą wierzchołek z jego potomkiem
- **Krawędzie poprzeczne:** łączą wierzchołki w różnych gałęziach
**Zastosowania:** sortowanie topologiczne, wykrywanie cykli, silnie powiązane komponenty, rozwiązywanie labiryntów.
### Porównanie BFS i DFS
| Kryterium | BFS | DFS |
|----------|-----|-----|
| Strategia | Szerokie, a potem głębokie | Głęboko, a potem szeroko |
| Pamięć | Wyżej (granica sklepów) | Dolna (ścieżka sklepu) |
| Najkrótsza ścieżka (nieważona) | Gwarantowane | Nie gwarantowane |
| Użyj, gdy rozwiązanie jest bliskie rozpoczęcia | Lepiej | Gorzej |
| Użyj, gdy wykres jest bardzo głęboki | Gorzej | Lepiej |
| Sortowanie topologiczne | Wariant algorytmu Kahna | Podejście standardowe |
---

## Algorytmy najkrótszej ścieżki
Znalezienie najkrótszej ścieżki pomiędzy wierzchołkami jest jednym z najważniejszych praktycznie problemów grafów.
### Algorytm Dijkstry
Znajduje najkrótsze ścieżki z jednego źródła do wszystkich pozostałych wierzchołków grafu z **nieujemnymi** wagami krawędzi.
| Nieruchomość | Wartość |
|---------|-------|
| Ciężary krawędzi | Musi wynosić ≥ 0 |
| Czas (sterta binarna) | O((V + E) log V) |
| Czas (sterta Fibonacciego) | O(E + Vlog V) |
| Chciwy? | Tak |
| Obsługuje wagi ujemne? | Nie |
**Algorytm:**
1. Zainicjuj dist[s] = 0, dist[v] = ∞ dla wszystkich v ≠ s. Kolejka priorytetowa Q ze wszystkimi wierzchołkami.
2. Gdy Q nie jest puste: wyodrębnij wierzchołek u o minimalnej odległości. Dla każdego sąsiada v u o wadze krawędzi w: jeśli dist[u] + w < dist[v], zaktualizuj dist[v] = dist[u] + w.
**Przykład praktyczny:**```
Graph: A --1-- B --2-- C --1-- D
       A --4-- C
       B --1-- D

Shortest paths from A:
A → B: 1 (direct)
A → D: 2 (A→B→D)
A → C: 3 (A→B→C, NOT A→C=4)
```

### Algorytm Bellmana-Forda
Obsługuje **ujemne** wagi krawędzi i wykrywa cykle ujemne.
| Nieruchomość | Wartość |
|---------|-------|
| Ciężary krawędzi | Dowolny (wykrywa cykle ujemne) |
| Złożoność czasowa | O(V · E) |
| Złożoność przestrzeni | O(V) |
| Obsługuje cykle ujemne? | Tak (wykrywa i raportuje) |
**Algorytm:**
1. Zainicjuj dist[s] = 0, dist[v] = ∞ dla wszystkich v ≠ s.
2. Powtórz V − 1 razy: dla każdej krawędzi (u, v) o wadze w: jeśli dist[u] + w < dist[v], zaktualizuj dist[v].
3. Sprawdź, czy nie ma cykli ujemnych: jeśli którąkolwiek krawędź można nadal rozluźnić, oznacza to, że istnieje cykl ujemny.
### Algorytm Floyda-Warshalla
Znajduje najkrótsze ścieżki pomiędzy **wszystkimi parami** wierzchołków.
| Nieruchomość | Wartość |
|---------|-------|
| Złożoność czasowa | O(V3) |
| Złożoność przestrzeni | O(V²) |
| Obsługuje wagi ujemne? | Tak (ale nie cykle ujemne) |
| Podejście | Programowanie dynamiczne |
**Rekurencja:** dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]) dla każdego wierzchołka pośredniego k.
### Przewodnik po wyborze algorytmu
| Scenariusz | Algorytm |
|---------|-----------|
| Pojedyncze źródło, wagi nieujemne | Dijkstra |
| Pojedyncze źródło, możliwe wagi ujemne | Bellman-Ford |
| Wszystkie pary, graf gęsty | Floyd-Warshall |
| Wszystkie pary, rzadki wykres | Uruchom Dijkstrę z każdego wierzchołka |
| Wykres nieważony | BFS |
| DAG (bez cykli) | Sortowanie topologiczne + relaksacja |
| A* (kierowane heurystyką) | Wyszukiwanie A* (w celu znalezienia ścieżki z dobrą heurystyką) |
---

## Minimalne drzewa rozpinające
**minimalne drzewo rozpinające (MST)** łączy wszystkie wierzchołki z minimalną całkowitą wagą krawędzi.
### Właściwości
- MST ma dokładnie n − 1 krawędzi (dla n wierzchołków)
- MST istnieje, jeśli wykres jest spójny
- Wykres z różnymi wagami krawędzi ma unikalny MST
- MST spełnia **właściwość cięcia**: krawędź o minimalnym ciężarze przechodząca przez dowolne cięcie należy do MST
- MST spełnia **właściwość cyklu**: krawędź o maksymalnej wadze w żadnym cyklu nie należy do MST
### Algorytm Kruskala
| Nieruchomość | Wartość |
|---------|-------|
| Strategia | Chciwy — dodaj krawędzie w kolejności wagowej |
| Struktura danych | Zbiór rozłączny (znalezienie związku) |
| Złożoność czasowa | O(E log E) |
| Najlepsze dla | Rzadkie wykresy |
**Algorytm:**
1. Posortuj wszystkie krawędzie według wagi.
2. Dla każdej krawędzi (w kolejności): jeśli dodanie jej nie utworzy cyklu (sprawdź w Union-find), dodaj ją do MST.
3. Zatrzymaj po wybraniu n - 1 krawędzi.
### Algorytm Prima
| Nieruchomość | Wartość |
|---------|-------|
| Strategia | Chciwy — wyhoduj drzewo z wierzchołka początkowego |
| Struktura danych | Kolejka priorytetowa (min-sterta) |
| Złożoność czasowa | O(E log V) ze stertą binarną |
| Najlepsze dla | Gęste wykresy |
**Algorytm:**
1. Zacznij od dowolnego wierzchołka. Oznacz to jako część MST.
2. Wielokrotnie dodawaj krawędź o minimalnej wadze łączącą wierzchołek w MST z wierzchołkiem na zewnątrz.
3. Zatrzymaj, gdy uwzględnione zostaną wszystkie wierzchołki.
### Aplikacje MST
| Aplikacja | Jak MST pomaga |
|------------|-------------|
| Projekt sieci | Ułóż minimalną ilość kabli/rur, aby połączyć wszystkie lokalizacje |
| Klastrowanie | Usuń k - 1 najdłuższych krawędzi MST, aby otrzymać k klastrów |
| Algorytmy aproksymacyjne | 2-przybliżenie dla metrycznego TSP |
| Segmentacja obrazu | Grupuj piksele według MST podobieństwa kolorów |
| Eliminacja funkcji | Usuń zbędne funkcje za pomocą MST wykresu korelacji |
---

## Przepływ sieci
Problemy z przepływem sieci modelują przepływ zasobów w systemie.
### Definicja sieci przepływu
**sieć przepływów** to graf skierowany, w którym:
- Wierzchołek **źródłowy** (wytwarza przepływ)
- A **ujście** wierzchołka t (zużywa przepływ)
- **Pojemności** c(u,v) ≥ 0 na każdej krawędzi
- **Przepływ** f(u,v) spełniający:
  - **Ograniczenie wydajności:** 0 ≤ f(u,v) ≤ c(u,v)
  - **Zachowanie przepływu:** dopływ = odpływ w każdym wierzchołku z wyjątkiem s i t
### Problem z maksymalnym przepływem
Znajdź maksymalny całkowity przepływ od s do t.
**Metoda Forda-Fulkersona:**
1. Chociaż na wykresie resztowym istnieje ścieżka rozszerzająca od s do t:
2. Znajdź przepustowość wąskiego gardła na ścieżce
3. Zwiększ przepływ wzdłuż ścieżki o wielkość wąskiego gardła
4. Zaktualizuj pozostałe moce produkcyjne
| Algorytm | Złożoność czasu | Notatki |
|----------|----------------|-------|
| Ford-Fulkerson (DFS) | O(m · f*) gdzie f* to maksymalny przepływ | Nie może kończyć się irracjonalnymi zdolnościami |
| Edmonds-Karp (BFS) | O(V · E²) | Zawsze kończy, wybiera najkrótszą ścieżkę rozszerzającą |
| Algorytm Dinica | O(V² · E) | Wykorzystuje przepływy blokujące; O(V^(1/2) · E) dla pojemności jednostkowych |
### Twierdzenie o maksymalnym przepływie i minimalnym cięciu
**maksymalny przepływ** od s do t jest równy **minimalnej wydajności cięcia** oddzielającej s od t.
A **cięcie** (S, T) dzieli wierzchołki na S (zawierające s) i T (zawierające t). Wydajność cięcia jest sumą wydajności krawędzi od S do T.
**Zastosowania przepływu maksymalnego:**
- Dopasowywanie dwustronne (przydzielanie pracowników do stanowisk)
- Segmentacja obrazu (oddzielenie pierwszego planu od tła)
- Eliminacja baseballu (czy drużyna X nadal może wygrać?)
- Niezawodność sieci (maksymalna przepustowość danych)
### Dopasowanie dwustronne poprzez Max Flow
Biorąc pod uwagę graf dwudzielny G = (L ∪ R, E):
1. Dodaj źródła z krawędziami do wszystkich wierzchołków w L (pojemność 1)
2. Dodaj ujście t z krawędziami ze wszystkich wierzchołków w R (pojemność 1)
3. Ustaw wszystkie oryginalne pojemności brzegowe na 1
4. Maksymalny przepływ = maksymalne dopasowanie
---

## Teoria wykresów spektralnych
Teoria grafów spektralnych bada wykresy poprzez wartości własne i wektory własne macierzy powiązanych z wykresem.
### Kluczowe macierze
| Matryca | Definicja | Co przechwytuje |
|------------|------------|--------------------------------|
| **Macierz sąsiedztwa** A | A[i][j] = 1 jeśli krawędź (i,j) istnieje | Wzór łączności |
| **Macierz stopni** D | Przekątna; D[i][i] = stopień(i) | Znaczenie wierzchołków według stopnia |
| **Laplazja** L = D - A | L[i][j] = −1 jeśli krawędź, stopień(i) na przekątnej | Gładkość funkcji na wykresie |
| **Znormalizowany laplacjan** L_norm = D^(−1/2) L D^(−1/2) | Wersja niezmiennicza skali | Struktura społeczności |
### Wartości własne Laplaciana
Laplacian L jest dodatni półokreślony, więc wszystkie wartości własne wynoszą ≥ 0.
| Wartość własna | Znaczenie |
|------------|------------|
| λ₁ = 0 | Zawsze zero; wektor własny jest wektorem stałym |
| λ₂ (łączność algebraiczna) | > 0 jeśli wykres jest podłączony; większy = lepiej połączony |
| Liczba zerowych wartości własnych | Równa się liczbie połączonych komponentów |
| λₙ | Związane z maksymalnym stopniem i rozwinięciem wykresu |
### Zastosowania metod spektralnych
| Aplikacja | Metoda |
|------------|------------|
| **Podział wykresu** | Użyj wektorów własnych L, aby podzielić wykres na zrównoważone części |
| **Wykrywanie społeczności** | Grupowanie widmowe: osadzaj wierzchołki za pomocą dolnych wektorów własnych, a następnie grupuj |
| **PageRank** | Wektor własny macierzy sąsiedztwa (lub macierzy przejścia) grafu sieciowego |
| **Rysunek graficzny** | Ustaw wierzchołki za pomocą wektorów własnych Laplaciana |
| **Uczenie się częściowo nadzorowane** | Propaguj etykiety za pomocą wykresu Laplacian (propagacja etykiet) |
| **Wykresy sieci neuronowych** | Sploty widmowe: filtrowanie sygnałów na wykresach za pomocą wektorów własnych L |
### Nierówność Cheegera
Wiąże drugą wartość własną λ₂ z **rozszerzeniem** wykresu (jak dobrze jest on powiązany):
λ₂ / 2 ≤ h(G) ≤ √(2λ₂)
gdzie h(G) jest stałą Cheegera (liczbą izoperymetryczną). Oznacza to, że λ₂ w przybliżeniu mierzy, jak trudno jest podzielić wykres na dwie części – jest to kluczowy spostrzeżenie przy grupowaniu.
---

## Specjalne struktury grafów
| Wykres | Wierzchołki | Krawędzie | Właściwości |
|-------|----------|-------|------------|
| Ukończ Kₙ | n | n(n−1)/2 | Każda para połączona; średnica 1 |
| Cykl Cₙ | n | n | 2-regularny; podłączony |
| Ścieżka Pₙ | n | n−1 | Drzewo; średnica n−1 |
| Hypercube Qₖ | 2ᵏ | k·2ᵏ⁻¹ | k-regularny; średnica k; dwustronny |
| Kompletny dwustronny K_{m,n} | m+n | m·n | Każdy wierzchołek w jednej części łączy się ze wszystkimi w drugiej |
| Wykres Petersena | 10 | 15 | 3-regularny; średnica 2; nie płaski; brak cyklu Hamiltona |
---

## Znaczenie dla uczenia maszynowego i nauki o danych
| Koncepcja wykresu | Aplikacja |
|--------------|------------|
| BFS / DFS | Indeksowanie sieci, analiza sieci społecznościowych, etykietowanie podłączonych komponentów |
| Dijkstra / A* | Planowanie tras, znajdowanie ścieżki AI w grach, nawigacja robotyczna |
| Minimalne drzewo rozpinające | Klastrowanie (pojedyncze połączenie), wybór funkcji, projektowanie sieci |
| Maks. przepływ / min. cięcie | Segmentacja obrazu, dopasowanie dwustronne, przypisanie rekomendacji |
| Metody spektralne | Grupowanie widmowe, grafowe sieci neuronowe, redukcja wymiarowości (mapy własne Laplaciana) |
| PageRank | Ranking wyszukiwarek, analiza wpływu w sieciach społecznościowych |
| DAG | Sieci Bayesa, wnioskowanie przyczynowe, planowanie zadań, grafy obliczeniowe w uczeniu głębokim |
| Wykresy dwudzielne | Macierze pozycji użytkownika w systemach rekomendacyjnych, rynki dwustronne |
| Struktury drzewne | Drzewa decyzyjne, lasy losowe, grupowanie hierarchiczne, nawigacja w systemie plików |
| Reprezentacje wykresów | Wykresy wiedzy (Wikidane, DBpedia), wykresy molekularne (odkrywanie leków), sieci cytowań |
---

## Streszczenie
| Temat | Podstawowy pomysł | Kluczowy algorytm / wynik |
|-------|-----------|----------------------|
| Podstawy | Wierzchołki, krawędzie, stopnie, ścieżki | Lemat o uścisku dłoni |
| Reprezentacje | Jak przechowywać wykresy | Macierz sąsiedztwa a lista sąsiedztwa |
| Drzewa | Połączone grafy acykliczne | n wierzchołków → n−1 krawędzi |
| Przejścia | Systematyczna eksploracja wierzchołków | BFS (najkrótsza ścieżka), DFS (głęboka eksploracja) |
| Najkrótsze ścieżki | Trasy o minimalnej wadze | Dijkstra, Bellman-Ford, Floyd-Warshall |
| Minimalne drzewo opinające | Najtańszy sposób na połączenie wszystkich wierzchołków | Kruskala, Prima |
| Przepływ sieci | Maksymalna przepustowość | Forda-Fulkersona, twierdzenie o maksymalnym przepływie i minimalnym przekroju |
| Teoria widmowa | Wartości własne ujawniają strukturę | Wartości własne Laplaciana, grupowanie widmowe |
Teoria grafów jest prawdopodobnie najbardziej bezpośrednio stosowaną gałęzią matematyki we współczesnej nauce o danych. Sieci społecznościowe, grafy wiedzy, struktury molekularne, grafy obliczeniowe w ramach głębokiego uczenia się, rozwiązywanie zależności, systemy rekomendacji – wszystkie są zasadniczo problemami grafowymi. Algorytmy tu omówione nie mają wyłącznie charakteru teoretycznego; codziennie działają na dużą skalę w systemach produkcyjnych.