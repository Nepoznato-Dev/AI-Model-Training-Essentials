---
# Metadata
title: "Mathematics"
description: "Number systems, algebra, geometry, calculus, set theory, linear algebra, and binary — the mathematical foundations for data science and ML"
category: "Data Science and Analytics"
subcategory: "Mathematics"
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
    date: "2026-08-09"
    author: "AI Model Training Team"
    changes: "Split from math_and_logic.md; expanded into standalone file"

# Review
created: "2026-08-09"
last_modified: "2026-08-09"
review_date: "2027-02-09"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-09"

# Classification
tags: [mathematics, algebra, calculus, geometry, linear-algebra, number-theory, set-theory]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "14 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

#Matematyka
Matematyka to nie tylko przedmiot, którego uczy się w szkole — stanowi podstawę niemal każdej dziedziny techniki. Fizyka używa go do opisu wszechświata. Informatyka wykorzystuje go do projektowania algorytmów. Uczenie maszynowe wykorzystuje je do optymalizacji wag. Finanse wykorzystują to do wyceny ryzyka. Opanowanie każdej gałęzi nie jest konieczne, ale zrozumienie krajobrazu – i wiedza, gdzie każda gałąź ma zastosowanie – ułatwia zrozumienie innych tematów.
---

## Systemy liczbowe
Przede wszystkim warto zrozumieć, z jakimi liczbami pracujesz. Każda warstwa rozszerza poprzednią, aby rozwiązać problem, którego nie mogła rozwiązać stara warstwa.
| Typ numeru | Co zawiera | Dlaczego został wynaleziony | Przykład |
|---|---|---|---|
| Liczby naturalne | 1, 2, 3, 4, ... | Liczenie rzeczy | 5 jabłek |
| Liczby całkowite | 0, 1, 2, 3, ... | Reprezentowanie „nic” | 0 stopni |
| Liczby całkowite | ..., -2, -1, 0, 1, 2, ... | Dług, temperatura poniżej zera | −15°C |
| Liczby wymierne | p/q gdzie q ≠ 0 | Dzielenie rzeczy nierównomiernie | 1/3, 0,75 |
| Liczby niewymierne | Nie można wyrazić w ułamkach | Przekątne, koła, wzrost | √2, π, mi |
| Liczby rzeczywiste | Wszystko racjonalne + irracjonalne | Pełna oś liczbowa | 3.14159... |
| Liczby urojone | Wielokrotność i = √(−1) | Rozwiązywanie x² + 1 = 0 | 3i |
| Liczby zespolone | a + bi (rzeczywisty + urojony) | Elektrotechnika, mechanika kwantowa | 2 + 3i |
---

## Arytmetyka i teoria liczb
Podstawy: dodawanie, odejmowanie, mnożenie, dzielenie i zasady ich kolejności.
**Kolejność działań** (PEMDAS/BODMAS): Nawiasy → Potęgi → Mnożenie/Dzielenie (od lewej do prawej) → Dodawanie/Odejmowanie (od lewej do prawej).
**Liczby pierwsze** — liczby całkowite większe niż 1, które nie mają dzielników innych niż 1 i one same — to atomy teorii liczb. Kilka pierwszych: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29.
Dlaczego liczby pierwsze mają znaczenie poza lekcjami matematyki: współczesne szyfrowanie (RSA) opiera się na fakcie, że pomnożenie dwóch dużych liczb pierwszych jest łatwe, ale uwzględnienie wyniku na czynniki jest brutalne obliczeniowo.
**Przydatne operacje:**
- Rozkład na czynniki pierwsze: 84 = 2² × 3 × 7
- Największy wspólny dzielnik (NWD) 24 i 36: 12
- Najmniejsza wspólna wielokrotność (LCM) 4 i 6: 12
---

## Algebra
Algebra polega na tym, że przestajesz pracować z konkretnymi liczbami i zaczynasz pracować z *relacjami*. Zmienna taka jak`x`nie ma stałej wartości — reprezentuje wszystko, co sprawia, że ​​równanie jest prawdziwe.
**Wzór kwadratowy** rozwiązuje ax² + bx + c = 0:
x = (−b ± √(b² − 4ac)) / 2a
**Typowe typy funkcji i miejsce ich występowania:**
| Funkcja | Formuła | Kształt | Przykład ze świata rzeczywistego |
|---|---|---|---|
| Liniowy | y = mx + b | Linia prosta | Koszt jednostkowy według stawki ryczałtowej |
| Kwadratowy | y = ax² + bx + c | Parabola | Ruch pocisku, droga hamowania |
| wykładniczy | y = a × b² | Szybki wzrost/zanik | Procent składany, wzrost populacji, rozprzestrzenianie się wirusa |
| Logarytmiczny | y = log_b(x) | Powolny wzrost, odwrotność wykładniczego | Skala decybelowa, skala pH, złożoność algorytmu |
**Kluczowe słownictwo:**
- **Domena**: wszystkie prawidłowe dane wejściowe (np. nie można dzielić przez zero, nie można przyjmować √ liczby ujemnej w liczbach rzeczywistych)
- **Zakres**: wszystkie możliwe wyjścia
- **Nachylenie** (m): tempo zmian — „na każdą 1 jednostkę x, y zmian o m”
- **Przecięcie**: miejsce, w którym funkcja przecina oś
---

## Geometria
Geometria bada kształty, rozmiary i relacje przestrzenne. Pojawia się wszędzie: silniki gier używają go do renderowania, robotyka używa go do planowania ścieżek, architektura używa go do projektowania strukturalnego.
**Podstawowe formuły:**
| Kształt | Nieruchomość | Formuła |
|---|---|---|
| Trójkąt | Suma kątów | 180° |
| Czworokąt | Suma kątów | 360° |
| Koło | Obwód | 2πr |
| Koło | Powierzchnia | πr² |
| Kula | Tom | (4/3)πr³ |
| Trójkąt prawy | Twierdzenie Pitagorasa | a² + b² = c² |
**π (pi)** ≈ 3,14159 — stosunek obwodu dowolnego koła do jego średnicy. Pojawia się w miejscach, których się nie spodziewasz: prawdopodobieństwo (rozkład normalny), inżynieria (przetwarzanie sygnału), a nawet równanie zasady nieoznaczoności Heisenberga.
---

## Obliczenie
Badania rachunku różniczkowego *zmiana* i *akumulacja*. Jeśli algebra obsługuje migawki, rachunek różniczkowy obsługuje filmy.
### Rachunek różniczkowy
Tempo zmian. Pochodna f'(x) informuje, jak szybko f zmienia się w dowolnym punkcie.
| Funkcja f(x) | Pochodna f'(x) | Intuicja |
|---|---|---|
| xⁿ | n·xⁿ⁻¹ | Reguła mocy |
| eˣ | eˣ | Jedyna funkcja równa własnej pochodnej |
| ln(x) | 1/x | Tempo wzrostu zwalnia wraz ze wzrostem x |
| grzech(x) | cos(x) | Szybkość zmian oscylacji |
**Dlaczego pochodne mają znaczenie w ML:** zejście gradientowe — algorytm uczący większość sieci neuronowych — działa poprzez obliczanie pochodnych funkcji straty i podążanie w kierunku, który zmniejsza błąd.
### Kluczowe reguły różnicowania
| Zasada | Formuła | Przypadek użycia |
|------|---------|--------------|
| **Zasada łańcucha** | (f∘g)' = f'(g(x)) · g'(x) | Funkcje zagnieżdżone — propagacja wsteczna w sieciach neuronowych |
| **Zasada dotycząca produktu** | (fg)' = f'g + fg' | Mnożenie dwóch funkcji x |
| **Reguła ilorazu** | (f/g)' = (f'g - fg') / g² | Dzielenie dwóch funkcji x |
### Rachunek całkowy
Akumulacja. Całka reprezentuje obszar pod krzywą. Jeśli pochodne odpowiadają na pytanie „jak szybko się to zmienia?”, całki odpowiadają na pytanie „ile się zgromadziło?”
**Podstawowe twierdzenie rachunku różniczkowego** łączy oba: różniczkowanie i całkowanie są operacjami odwrotnymi.
| Całka | Wynik | Przypadek użycia |
|---------|--------|---------|
| ∫ xⁿ dx | xⁿ⁺¹/(n+1) + C | Pole pod krzywymi wielomianowymi |
| ∫ eˣ dx | eˣ + C | Całkowity skumulowany wzrost |
| ∫ 1/x dx | ln|x| + C | Kumulacja logarytmiczna |
---

## Zestawy
**Zbiór** to zbiór odrębnych obiektów — podstawa współczesnej matematyki.
| Operacja | Symbol | Znaczenie | Przykład (A={1,2,3}, B={2,4}) |
|---|---|---|---|
| Unia | A ∪ B | Elementy w dowolnym zestawie | {1, 2, 3, 4} |
| Przecięcie | A ∩ B | Elementy w obu zestawach | {2} |
| Różnica | A \ B | Elementy w A, ale nie B | {1, 3} |
| Pusty zestaw | ∅ | Nie zawiera niczego | {} |
| Podzbiór | A ⊂ B | Wszystkie elementy A znajdują się w B | {1,2} ⊂ {1,2,3} |
Teoria mnogości pojawia się w bazach danych (złączenia SQL JOIN to zasadniczo operacje na zbiorach), prawdopodobieństwie (zdarzenia to zbiory wyników) i programowaniu (zbiory, mapy skrótów).
---

## Podstawy binarne i liczbowe
Komputery myślą binarnie (podstawa 2): tylko 0 i 1. Ludzie myślą w systemie dziesiętnym (podstawa 10). Programiści często używają systemu szesnastkowego (podstawa 16) jako zwartego sposobu reprezentacji binarnej.
| Baza | Używane cyfry | Przykład | Odpowiednik dziesiętny |
|---|---|---|---|
| Binarny (podstawa 2) | 0, 1 | 1011 | 8 + 0 + 2 + 1 = 11 |
| Dziesiętny (podstawa 10) | 0–9 | 11 | 11 |
| Szesnastkowy (podstawa 16) | 0–9, A–F | B | 11 |
| Szesnastkowy | 0–9, A–F | A3 | 160 + 3 = 163 |
**Dlaczego to ma znaczenie:** każdy fragment danych na komputerze — tekst, obrazy, dźwięk i wideo — jest ostatecznie binarny. Bajt (8 bitów) może reprezentować 256 różnych wartości. Kolory w CSS (#FF5733), adresy pamięci (0x7FFF) i adresy IP używają wartości szesnastkowych, ponieważ kompresują długie ciągi binarne w coś czytelnego.
---

## Algebra liniowa dla uczenia maszynowego i grafiki
Algebra liniowa — wektory, macierze i transformacje — to silnik matematyczny leżący u podstaw uczenia maszynowego, grafiki komputerowej, symulacji fizycznych i wyszukiwarek.
### Wektory
**Wektory** to uporządkowane listy liczb. W ML każdy punkt danych jest wektorem cech:
- [23, 1,8, 75] może reprezentować wiek osoby, wzrost w metrach i wagę w kg.
| Operacja wektorowa | Formuła | Przypadek użycia |
|-----------------|---------|---------|
| **Dodatek** | a + b = [a₁+b₁, a₂+b₂, ...] | Łączenie wektorów cech |
| **Mnożenie skalarne** | ca·a = [c·a₁, ca·a₂, ...] | Funkcje skalowania |
| **Produkt kropkowy** | a·b = Σ aᵢbᵢ | Podobieństwo, prognozy |
| **Norma (wielkość)** | ||a|| = √(Σ aᵢ²) | Długość wektora |
| **Produkty krzyżowe** | a × b (tylko 3D) | Wektor prostopadły, obszar |
### Macierze
**Macierze** to dwuwymiarowe tablice liczb. Wagi sieci neuronowej są przechowywane w postaci macierzy. Partia 100 obrazów może mieć postać macierzy o kształcie (100, 784) — 100 wierszy, każdy o wartościach 784 pikseli.
**Kluczowe operacje:**
| Operacja | Co to robi | Gdzie się pojawia |
|---|---|---|
| Produkt kropkowy | Mierzy podobieństwo między dwoma wektorami | Systemy rekomendacji, podobieństwo cosinus |
| Mnożenie macierzy | Łączy przekształcenia liniowe | Każda warstwa sieci neuronowej |
| Wartości własne/wektory własne | Kierunki macierzy skalują się (nie obracają) | Redukcja wymiarowości PCA, PageRank |
| Ranga matrycy | Ilość niezależnych informacji | Kompresja, przybliżenie niskiego rzędu |
| Transpozycja | Odwraca wiersze i kolumny | Obliczanie gradientu |
| Odwrotność | A⁻¹ taki, że A·A⁻¹ = I | Rozwiązywanie układów liniowych |
**Cosinus podobieństwa** = (a·b) / (||a|| × ||b||) — waha się od -1 (przeciwnie) do 1 (ten sam kierunek). W ten sposób wyszukiwarki mierzą, czy dwa dokumenty „dotyczą tej samej rzeczy” i jak modele osadzania porównują podobieństwo semantyczne.
---

## Streszczenie
| Oddział | Podstawowe pytanie | Kluczowa aplikacja |
|---|---|---|
| Arytmetyka i teoria liczb | Jak zachowują się liczby? | Kryptografia, haszowanie |
| Algebra | Jak powiązane są niewiadome? | Modelowanie, równania |
| Geometria | Jak działają kształty i przestrzenie? | Grafika, robotyka, architektura |
| Rachunek | Jak sprawy się zmieniają? | Trening sieci neuronowych, fizyka |
| Teoria mnogości | W jaki sposób kolekcje są ze sobą powiązane? | Bazy danych, prawdopodobieństwo |
| Algebra liniowa | Jak działają transformacje? | ML, grafika, wyszukiwarki |
Nie wszystkie z tych tematów są potrzebne od razu. Jednakże w miarę zagłębiania się w jakąkolwiek dziedzinę techniczną podstawy te stają się coraz bardziej istotne. Każda gałąź staje się jaśniejsza, gdy zrozumie się problem, do rozwiązania którego została zaprojektowana.