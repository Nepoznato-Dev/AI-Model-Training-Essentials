<!--
---
# Metadata
title: "Optimization"
description: "Linear programming, convex optimization, gradient descent variants, Lagrange multipliers, KKT conditions, duality, integer programming, and heuristic methods"
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
    changes: "Initial deep-dive into optimization"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2027-02-10"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-10"

# Classification
tags: [optimization, linear-programming, convex-optimization, gradient-descent, lagrange-multipliers, kkt, duality, integer-programming]
difficulty_level: "intermediate"
prerequisites:
  - "mathematics.md"
  - "real_analysis.md"
estimated_reading_time: "30 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Optymalizacja
Optymalizacja to matematyka polegająca na znalezieniu najlepszego rozwiązania ze zbioru możliwych rozwiązań. Pyta: biorąc pod uwagę funkcję i ograniczenia, jakie dane wejściowe minimalizują (lub maksymalizują) wynik? Optymalizacja jest motorem uczenia maszynowego — uczenie modelu oznacza minimalizację funkcji straty. Pojawia się w badaniach operacyjnych, ekonomii, projektowaniu inżynierskim i praktycznie w każdej dziedzinie ilościowej.
---

## Formułowanie problemu
Ogólny **problem optymalizacji** ma postać:
Minimalizuj f(x)
Z zastrzeżeniem: gᵢ(x) ≤ 0 (ograniczenia nierówności), hⱼ(x) = 0 (ograniczenia równości)
| Termin | Znaczenie |
|------|-------------|
| **Funkcja celu** f(x) | Ilość do zminimalizowania (lub maksymalizacji) |
| **Zmienne decyzyjne** x | Wartości, które możemy kontrolować |
| **Możliwy region** | Zbiór wszystkich x spełniających wszystkie ograniczenia |
| **Minimum globalne** | Wykonalne x* z f(x*) ≤ f(x) dla wszystkich wykonalnych x |
| **Minimum lokalne** | Wykonalne x* z f(x*) ≤ f(x) dla wszystkich wykonalnych x w pewnym sąsiedztwie |
| **Problem wypukły** | f jest wypukłe, możliwy obszar jest zbiorem wypukłym (lokalny min = globalny min) |
---

## Programowanie liniowe (LP)
Kiedy zarówno cel, jak i wszystkie ograniczenia są **liniowe**, problemem jest program liniowy.
### Formularz standardowy
Minimalizuj cᵀx
Z zastrzeżeniem: Ax ≤ b, x ≥ 0
gdzie c, x ∈ ℝⁿ, A ∈ ℝᵐˣⁿ, b ∈ ℝᵐ.
### Właściwości
| Nieruchomość | Oświadczenie |
|---------|-----------|
| Wypukłość | LP jest zawsze problemem wypukłym |
| Optymalne rozwiązanie | Zawsze w wierzchołku (punkcie narożnym) możliwego wielotopu |
| Istnienie | Jeśli obszar wykonalny jest ograniczony i niepusty, istnieje rozwiązanie optymalne |
| Wiele optimów | Jeśli dwa wierzchołki są optymalne, to każdy punkt na krawędzi pomiędzy nimi jest również optymalny |
### Metoda Simplex
**Metoda simpleks** (Dantzig, 1947) porusza się wzdłuż krawędzi możliwego wielotopu od wierzchołka do wierzchołka, zawsze poprawiając cel, aż do osiągnięcia maksimum.
| Nieruchomość | Wartość |
|---------|-------|
| Najgorszy moment | O(2ⁿ) (wykładniczy — rzadki w praktyce) |
| Średni czas rozpatrywania sprawy | Wielomian dla większości praktycznych problemów |
| Kluczowa idea | Przejdź do sąsiedniego wierzchołka z lepszą wartością celu |
**Algorytm (przegląd):**
1. Zacznij od podstawowego rozwiązania wykonalnego (wierzchołek wielokąta)
2. Wybierz zmienną wejściową (taką, która poprawia cel)
3. Wybierz zmienną końcową (zachowaj wykonalność)
4. Pivot: przejdź do nowego wierzchołka
5. Powtarzaj, aż nie będzie już widocznego kierunku poprawy
### Metody punktów wewnętrznych
Alternatywa dla simpleksu: podejście do maksimum z obszaru wykonalnego.
| Nieruchomość | Wartość |
|---------|-------|
| Najgorszy moment | Wielomian (O(n³·⁵) dla niektórych wariantów) |
| Praktyczne wykonanie | Konkurencyjny z simpleksem w przypadku dużych problemów |
| Kluczowa idea | Podążaj „centralną ścieżką” przez wnętrze |
### Przykład przepracowanej płyty LP
**Problem:** Fabryka produkuje krzesła (x₁) i stoły (x₂).
- Zysk: 30 dolarów na krzesło, 50 dolarów na stół
- Drewno: 2x₁ + 4x₂ ≤ 100 (dostępne nóżki do desek)
- Praca: x₁ + 3x₂ ≤ 60 (dostępne godziny)
- Maksymalizuj: 30x₁ + 50x₂
**Rozwiązanie (metoda graficzna dla 2 zmiennych):**
- Wierzchołki obszaru dopuszczalnego: (0,0), (30,0), (40,10), (0,20)
- Oceń cel w każdym wierzchołku:
  - (0,0): zysk = 0
  - (30,0): zysk = 900
  - (40,10): zysk = 1700 ← optymalny
  - (0,20): zysk = 1000
- **Optymalnie:** x₁ = 40 krzeseł, x₂ = 10 stołów, zysk = 1700 USD
---

## Optymalizacja wypukła
Problem jest **wypukły**, jeśli funkcja celu jest wypukła, a obszar wykonalny jest zbiorem wypukłym.
### Zbiory wypukłe i funkcje
| Koncepcja | Definicja |
|------------|------------|
| **Zestaw wypukły** | Dla dowolnego x, y w zbiorze i t ∈ [0,1]: tx + (1−t)y również jest w zbiorze |
| **Funkcja wypukła** | f(tx + (1−t)y) ≤ tf(x) + (1−t)f(y) dla wszystkich t ∈ [0,1] |
| **Ściśle wypukły** | Nierówność jest ścisła dla t ∈ (0,1) i x ≠ y |
**Kluczowa właściwość:** W przypadku optymalizacji wypukłej każde minimum lokalne jest minimum globalnym.
### Wspólne funkcje wypukłe
| Funkcja | Wypukły? | Gdzie |
|---------|---------|-------|
| topór + b (liniowy) | Tak (i ​​wklęsłe) | Wszędzie |
| x² | Tak | ℝ |
| eˣ | Tak | ℝ |
| −log(x) | Tak | x > 0 |
| \|x\|ᵖ (p ≥ 1) | Tak | ℝⁿ |
| max(f₁, f₂) jeśli f₁, f₂ wypukły | Tak | Przecięcie domen |
### Zejście gradientowe
Najbardziej podstawowy algorytm optymalizacji w uczeniu maszynowym.
**Reguła aktualizacji:** x_{k+1} = x_k − α∇f(x_k)
gdzie α > 0 to **szybkość uczenia się** (wielkość kroku).
| Wariant | Aktualizuj regułę | Zaleta |
|--------|------------|----------|
| **Partia GD** | x ← x − α∇f(x) | Stabilna konwergencja |
| **Stochastyczny GD (SGD)** | x ← x − α∇fᵢ(x) (jedna próbka) | Szybko na iterację, wymyka się lokalnym minimom |
| **Mini-partia SGD** | x ← x − α(1/|B|)Σᵢ∈B ∇fᵢ(x) | Równowaga między wsadem a stochastycznym |
| **Pęd** | v ← βv – α∇f(x); x ← x + v | Przyspiesza w płaskich obszarach |
| **Adam** | Adaptacyjne współczynniki uczenia się na parametr | Działa dobrze od razu po wyjęciu z pudełka do głębokiego uczenia się |
| **RMSprop** | Skaluj szybkość uczenia się, korzystając ze średniej bieżącej wielkości gradientu | Dobre dla RNN |
### Wskaźniki konwergencji
| Metoda | Wypukłe f | Mocno wypukły f |
|--------|----------|--------------------------------|
| Zejście gradientowe | O(1/k) | O((1-μ/L)ᵏ) (liniowy) |
| SGD | O(1/√k) | O(1/k) |
| Przyspieszony GD (Niestierow) | O(1/k²) | O((1−√(μ/L))ᵏ) |
gdzie k = liczba iteracji, μ = parametr silnej wypukłości, L = stała Lipschitza.
### Wybór szybkości uczenia się
| Strategia | Opis |
|---------|------------|
| Naprawiono α | Proste, ale mogą się różnić (zbyt duże) lub powoli zbiegać się (zbyt małe) |
| Wyszukiwanie linii | Znajdź α, które minimalizuje f(x − α∇f(x)) wzdłuż kierunku gradientu |
| Harmonogramy rozpadu | α_t = α₀ / (1 + βt) lub α_t = α₀ · βᵗ |
| Rozgrzewka | Zacznij od małego, zwiększaj, a następnie zanikaj (powszechne w szkoleniu transformatorów) |
| Adaptacyjny (Adam) | Szybkość uczenia się poszczególnych parametrów w oparciu o statystyki gradientów |
---

## Ograniczona optymalizacja
### Mnożniki Lagrange’a
Dla problemu: zminimalizować f(x) pod warunkiem, że h(x) = 0.
**Lagranżian:** L(x, λ) = f(x) + λh(x)
Optymalnie: ∇ₓL = 0 i ∇_λL = 0 (co daje h(x) = 0).
**Przykład praktyczny:** Minimalizuj f(x,y) = x² + y² pod warunkiem, że x + y = 1.
- L = x² + y² + λ(x + y - 1)
- ∂L/∂x = 2x + λ = 0 → x = −λ/2
- ∂L/∂y = 2y + λ = 0 → y = −λ/2
- Ograniczenie: x + y = 1 → −λ = 1 → λ = −1
- Rozwiązanie: x = 1/2, y = 1/2, f = 1/2
### Warunki KKT
**Warunki Karusha-Kuhna-Tuckera (KKT)** uogólniają mnożniki Lagrange'a na ograniczenia nierówności.
Dla: minimalizuj f(x) pod warunkiem gᵢ(x) ≤ 0, hⱼ(x) = 0.
**Lagranżian:** L(x, λ, ν) = f(x) + Σᵢ λᵢgᵢ(x) + Σⱼ νⱼhⱼ(x)
**Warunki KKT** (niezbędne dla optymalności):
| Stan | Równanie |
|----------|----------|
| Stacjonarność | ∇ₓL = 0 |
| Pierwotna wykonalność | gᵢ(x) ≤ 0, hⱼ(x) = 0 |
| Podwójna wykonalność | λᵢ ≥ 0 |
| Uzupełniający luz | λᵢgᵢ(x) = 0 dla wszystkich i |
** Luz uzupełniający** oznacza: jeśli wiązanie gᵢ nie jest aktywne (gᵢ(x) < 0), to λᵢ = 0 (więzienie nie ma wpływu na rozwiązanie).
Dla problemów wypukłych spełniających warunek Slatera warunki KKT są zarówno konieczne, jak i wystarczające.
---

## Dwoistość
Z każdym problemem optymalizacyjnym (**pierwotnym**) jest powiązany problem **podwójny**.
### Słaby i silny dualizm
| Koncepcja | Oświadczenie |
|--------|-----------|
| **Podwójna funkcja** | g(λ, ν) = infₓ L(x, λ, ν) |
| **Podwójny problem** | Maksymalizuj g(λ, ν) pod warunkiem λ ≥ 0 |
| **Słaba dwoistość** | Podwójny optymalny ≤ Pierwotny optymalny (zawsze zachodzi) |
| **Silna dwoistość** | Podwójny optymalny = Pierwotny optymalny (dotyczy problemów wypukłych ze stanem Slatera) |
| **Luka dualności** | Optymalny pierwotny − Optymalny podwójny (zero w przypadku silnej dualności) |
### Dlaczego dualizm ma znaczenie
| Aplikacja | Jak dualność pomaga |
|------------|----------------------|
| Dolne granice | Dual daje świadectwo jak dobre jest rozwiązanie pierwotne |
| SVM | Podwójny problem SVM prowadzi do sztuczki z jądrem |
| Analiza wrażliwości | Zmienne podwójne mierzą, jak bardzo optymalne zmiany zostaną złagodzone
| Rozkład | Duże problemy można podzielić na mniejsze podproblemy za pomocą podwójnego |
---

## Programowanie liczb całkowitych
Kiedy niektóre lub wszystkie zmienne muszą być **liczbami całkowitymi**, problem staje się znacznie trudniejszy (ogólnie NP-trudny).
### Typy
| Wpisz | Opis |
|------|------------|
| Czyste IP | Wszystkie zmienne muszą być liczbami całkowitymi |
| Mieszane IP (MIP) | Niektóre zmienne są liczbami całkowitymi, inne ciągłymi |
| Binarne IP | Zmienne ograniczone do {0, 1} |
### Metody rozwiązania
| Metoda | Pomysł |
|------------|------|
| **Oddział i związany** | Podziel na podproblemy, rozwiąż relaksacje LP, przytnij |
| **Płaszczyzny tnące** | Dodaj wiązania liniowe, aby zaostrzyć relaksację LP |
| **Odgałęzienie i cięcie** | Połącz rozgałęzione z płaszczyznami tnącymi |
| **Heurystyka** | Zachłanne, lokalne wyszukiwanie, symulowane wyżarzanie w celu uzyskania przybliżonych rozwiązań |
---

## Metody heurystyczne i metaheurystyczne
Kiedy dokładna optymalizacja jest niemożliwa, heurystyki znajdują dobre (niekoniecznie optymalne) rozwiązania.
| Metoda | Kluczowa idea | Najlepsze dla |
|--------|----------|---------|
| **Zejście gradientowe** | Podążaj najbardziej stromym zejściem | Gładkie, różniczkowalne funkcje |
| **Metoda Newtona** | Użyj informacji drugiego rzędu (krzywizny) | Gładkie, dobrze uwarunkowane problemy |
| **Symulowane wyżarzanie** | Akceptuj gorsze rozwiązania z malejącym prawdopodobieństwem | Optymalizacja globalna, kombinatoryczna |
| **Algorytmy genetyczne** | Ewoluuj populację za pomocą selekcji, krzyżowania i mutacji | Wieloobiektywowy, niezróżnicowalny |
| **Rój cząstek** | Agenci eksplorują przestrzeń pod wpływem najbardziej znanych stanowisk | Ciągły, niewypukły |
| **Optymalizacja Bayesa** | Zbuduj model zastępczy, użyj funkcji akwizycji | Drogie funkcje czarnej skrzynki (strojenie hiperparametrów) |
### Metoda optymalizacji Newtona
**Reguła aktualizacji:** x_{k+1} = x_k − [H(x_k)]⁻¹ ∇f(x_k)
gdzie H jest macierzą Hesja (macierz drugich pochodnych).
| Nieruchomość | Wartość |
|---------|-------|
| Stopa konwergencji | Kwadratowy (prawie optymalny) |
| Koszt per iteracji | O(n³) dla inwersji Hessego |
| Wymaga | Dwukrotnie różniczkowalna, dodatnio określona Hesja |
| Quasi-Newton (BFGS) | Przybliżony hesjan z gradientów | O(n²) na iterację |
---

## Znaczenie dla uczenia maszynowego i nauki o danych
| Koncepcja optymalizacji | Aplikacja |
|----------------------------------|------------|
| Zejście gradientowe | Uczenie sieci neuronowych, regresja logistyczna, dowolny model różniczkowalny |
| SGD i warianty | ML na dużą skalę (szkolenia mini-batch), nauka online |
| Adam, RMSprop | Domyślne optymalizatory do głębokiego uczenia się |
| Optymalizacja wypukła | SVM, regresja logistyczna, LASSO, Ridge (gwarantowane optymalne globalne) |
| Mnożniki Lagrange'a | Ograniczone uczenie się, sprawiedliwe uczenie maszynowe, alokacja zasobów |
| Warunki KKT | Wyprowadzenie dualnego SVM, zrozumienie działania ograniczeń |
| Dwoistość | Sztuczka z jądrem SVM, analiza wrażliwości, metody dekompozycji |
| Programowanie liniowe | Alokacja zasobów, optymalizacja portfela, przepływ sieci |
| Programowanie całkowite | Selekcja cech (binarna), szeregowanie, problemy kombinatoryczne |
| Optymalizacja Bayesa | Strojenie hiperparametrów (Optuna, Hyperopt) |
| Newton/quasi-Newton | Metody drugiego rzędu dla problemów małych i średnich (L-BFGS) |
---

## Streszczenie
| Metoda | Typ problemu | Gwarancje | Skala |
|------------|------------|------------|-------|
| Simplex | Programowanie liniowe | Dokładne optymalne | Miliony zmiennych |
| Punkt wewnętrzny | Wypukły (LP, QP, SOCP) | Dokładne optymalne | Duża skala |
| Zejście gradientowe | Gładka, nieograniczona | Zbiega się do lokalnego min | Bardzo duży (głębokie uczenie się) |
| SGD | Ryzyko empiryczne na dużą skalę | Zbiega się (z zanikiem) | Ogromne zbiory danych |
| Newtona / BFGS | Gładkie, dwukrotnie różniczkowalne | Zbieżność kwadratowa | Mały i średni |
| KKT / Lagrange | Ograniczony (wypukły) | Dokładne pod warunkami | Średni |
| Oddział i związany | Programowanie całkowite | Dokładne optymalne | Mały i średni |
| Heurystyka | Dowolny (niewypukły, kombinatoryczny) | Brak gwarancji | Różnie |
Optymalizacja jest prawdopodobnie najważniejszym narzędziem matematycznym w uczeniu maszynowym. Każdy trenowany model — od regresji liniowej po duże modele językowe — wymaga rozwiązania problemu optymalizacyjnego. Zrozumienie, kiedy problem jest wypukły (gwarantowane optymalne globalne), kiedy opadanie gradientu będzie zbieżne i jak radzić sobie z ograniczeniami, daje teoretyczne podstawy do projektowania, debugowania i ulepszania algorytmów uczenia się.