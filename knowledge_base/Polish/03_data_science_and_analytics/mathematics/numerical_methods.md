<!--
---
# Metadata
title: "Numerical Methods"
description: "Floating-point arithmetic, root finding, numerical integration, ODE solvers, interpolation, numerical stability, and conditioning"
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
    changes: "Initial deep-dive into numerical methods"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2027-02-10"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-10"

# Classification
tags: [numerical-methods, floating-point, root-finding, numerical-integration, ode-solvers, interpolation, stability]
difficulty_level: "intermediate"
prerequisites:
  - "mathematics.md"
  - "real_analysis.md"
estimated_reading_time: "25 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Metody numeryczne
Metody numeryczne stanowią pomost pomiędzy teorią matematyczną a obliczeniami praktycznymi. Chociaż czysta matematyka dowodzi, że istnieją rozwiązania, metody numeryczne w rzeczywistości obliczają przybliżone odpowiedzi ze skończoną precyzją. Każdy model uczenia maszynowego, symulacja fizyki i potok analizy danych ostatecznie opiera się na obliczeniach numerycznych. Zrozumienie tych metod — ich dokładności, stabilności i ograniczeń — jest niezbędne do tworzenia niezawodnego oprogramowania.
---

## Arytmetyka zmiennoprzecinkowa
Komputery reprezentują liczby rzeczywiste ze skończoną precyzją. **Standard IEEE 754** definiuje sposób przechowywania i manipulowania liczbami zmiennoprzecinkowymi.
### Formaty IEEE 754
| Formatuj | Bity | Wykładnik | Mantysa | Przybliżone cyfry dziesiętne | Zakres |
|--------|------|----------|----------|--------------------------|-------|
| Połowa (fp16) | 16 | 5 | 10 | 3.3 | ±6,5 × 10⁴ |
| Singiel (fp32) | 32 | 8 | 23 | 7.2 | ±3,4 × 10³⁸ |
| Podwójny (fp64) | 64 | 11 | 52 | 15,9 | ±1,8 × 10³⁰⁸ |
### Epsilon maszynowy
**Epsilon maszynowy** (ε_mach) to najmniejsza liczba taka, że ​​1 + ε_mach > 1 w liczbach zmiennoprzecinkowych.
| Formatuj | ε_mach |
|------------|------------|
| fp16 | 2⁻¹⁰ ≈ 9,8 × 10⁻⁴ |
| FP32 | 2⁻²³ ≈ 1,2 × 10⁻⁷ |
| FP64 | 2⁻⁵² ≈ 2,2 × 10⁻¹⁶ |
### Typowe pułapki
| Pułapka | Przykład | Konsekwencja |
|--------|---------|------------|
| **Katastrofalne anulowanie** | Obliczanie (1 + x) - 1 dla małego x | Utrata cyfr znaczących |
| **Wchłanianie** | 10⁸ + 1 = 10⁸ w FP32 | Małe wartości utracone w dużych sumach |
| **Brak skojarzenia** | (a + b) + do ≠ a + (b + c) | Kolejność sumy ma znaczenie |
| **Dzielenie przez zero** | 1 / 10⁻³⁰⁰ → przepełnienie | Nieskończoność lub NaN |
### Strategie łagodzenia
| Strategia | Opis |
|---------|------------|
| **Sumowanie Kahana** | Skompensowane sumowanie w celu zmniejszenia błędu absorpcji |
| **Kahan-Babuska-Neumaier** | Ulepszona wersja sumowania Kahana |
| **Posortowane podsumowanie** | Sumuj najpierw małe liczby, aby uniknąć absorpcji |
| **Arytmetyka podwójna-podwójna** | Użyj par podwójnych, aby uzyskać większą precyzję |
| **Analiza kondycji** | Zrozum, czy sam problem wzmacnia błędy |
---

## Znajdowanie korzeni
Znajdowanie x takiego, że f(x) = 0.
### Metoda bisekcji
| Nieruchomość | Wartość |
|---------|-------|
| Wymaga | f ciągłe, f(a) i f(b) mają przeciwne znaki |
| Konwergencja | Liniowy (błąd zmniejsza się o połowę w każdym kroku) |
| Gwarantowane? | Tak — zawsze zbieżny |
| Iteracje dla cyfr d | ≈ d / log₁₀(2) ≈ 3,32d |
**Algorytm:**
1. Zacznij od przedziału [a, b] gdzie f(a) · f(b) < 0
2. Oblicz punkt środkowy c = (a + b) / 2
3. Jeżeli f(c) = 0 lub |b – a| < tolerancja, przestań
4. Jeśli f(a) · f(c) < 0, ustaw b = c; w przeciwnym razie ustaw a = c
5. Powtórz
### Metoda Newtona-Raphsona
| Nieruchomość | Wartość |
|---------|-------|
| Wymaga | f różniczkowalne, f'(x) ≠ 0 u pierwiastka |
| Konwergencja | Kwadratowy (blisko pierwiastka) |
| Gwarantowane? | Nie – może się różnić lub zmieniać się |
| Aktualizuj regułę | x_{n+1} = x_n − f(x_n) / f'(x_n) |
**Przykład praktyczny:** Znajdź √2, rozwiązując f(x) = x² − 2 = 0.
- f'(x) = 2x
- x₀ = 1,5
- x₁ = 1,5 - (2,25 - 2) / 3 = 1,5 - 0,0833 = 1,4167
- x₂ = 1,4167 - (2,0069 - 2) / 2,8333 = 1,4142
- x₃ = 1,41421356... (z dokładnością do 8 miejsc po przecinku)
### Metoda siecznych
Podobnie jak metoda Newtona, ale przybliża pochodną:
x_{n+1} = x_n – f(x_n) · (x_n – x_{n-1}) / (f(x_n) – f(x_{n-1}))
| Nieruchomość | Wartość |
|---------|-------|
| Konwergencja | Superliniowy (rząd ≈ 1,618, złoty podział) |
| Wymaga | Dwa początkowe domysły (nie jest wymagana żadna pochodna) |
### Porównanie metod wyszukiwania korzeni
| Metoda | Konwergencja | Potrzebny instrument pochodny? | Gwarantowane? | Koszt na krok |
|------------|------------|----------------------|------------|--------------|
| Bisekcja | Liniowy (1) | Nie | Tak | 1 funkcja eval |
| Newtona-Raphsona | Kwadratowy (2) | Tak | Nie | 2 wartości funkcji |
| Sieczna | Superliniowy (1,618) | Nie | Nie | 1 funkcja eval |
| Metoda Brenta | Superliniowy | Nie | Tak | Różnie |
**Metoda Brenta** łączy bisekcję (zbieżność gwarantowana) z interpolacją sieczną/odwrotną kwadratową (szybka zbieżność). Jest to domyślna wyszukiwarka korzeni w większości bibliotek numerycznych.
---

## Całkowanie numeryczne (kwadraturowe)
Obliczanie ∫ₐᵇ f(x) dx w przybliżeniu.
### Metody
| Metoda | Formuła | Błąd | Zamów |
|--------|---------|-------|-------|
| **Prostokąt (punkt środkowy)** | (b-a) · f((a+b)/2) | O(h²) | 1 |
| **Trapez** | (b-a)/2 · [f(a) + f(b)] | O(h²) | 2 |
| **1/3 Simpsona** | (b-a)/6 · [f(a) + 4f(m) + f(b)] | O(h⁴) | 3 |
| **Simpson 3/8** | Używa 4 równomiernie rozmieszczonych punktów | O(h⁴) | 4 |
| **Kwadratura Gaussa** | Optymalne rozmieszczenie węzłów | O(h²ⁿ) | n punktów |
### Reguły złożone
Dla n podprzedziałów szerokości h = (b−a)/n:
| Zasada | Formuła złożona | Błąd |
|------|---------|------|
| Kompozytowy trapezowy | h[f(a)/2 + Σf(xᵢ) + f(b)/2] | O(h²) |
| Kompozytowy Simpsona | h/3[f(a) + 4Σf(nieparzysty) + 2Σf(parzysty) + f(b)] | O(h⁴) |
**Przykład praktyczny:** Przybliżone ∫₀¹ e^(−x²) dx przy użyciu złożonego trapezu z n = 4.
- h = 0,25, punkty: 0, 0,25, 0,5, 0,75, 1
- f(0) = 1, f(0,25) = 0,9394, f(0,5) = 0,7788, f(0,75) = 0,5698, f(1) = 0,3679
- T = 0,25[1/2 + 0,9394 + 0,7788 + 0,5698 + 0,3679/2] = 0,25[1/2 + 2,2880 + 0,1840] = 0,7430
- Wartość prawdziwa: ≈ 0,7468 (błąd ≈ 0,5%)
### Adaptacyjna kwadratura
Automatycznie dzieli przedziały, w których funkcja zmienia się szybko, używając mniejszej liczby punktów, gdzie jest gładka. Tego właśnie używa`scipy.integrate.quad`(w oparciu o QUADPACK).
---

## Interpolacja
Szacowanie wartości pomiędzy znanymi punktami danych.
### Metody
| Metoda | Opis | Gładkość | Oscylacja |
|------------|------------|------------|------------|
| **Najbliższy sąsiad** | Użyj najbliższego punktu danych | Nieciągły | Brak |
| **Liniowy** | Połącz punkty liniami prostymi | C⁰ (ciągły) | Brak |
| **Wielomian (Lagrange’a)** | Pojedynczy wielomian przechodzący przez wszystkie punkty | C^∞ | Ciężki w wielu punktach (zjawisko Runge'a) |
| **Splajn sześcienny** | Kawałki sześcienne, gładkie na łączeniach | C² | Minimalne |
| **Promieniowa funkcja bazowa** | Suma ważona jąder promieniowych | Zależy od jądra | Niski |
### Interpolacja Lagrange’a
Biorąc pod uwagę n+1 punktów (x₀, y₀), ..., (xₙ, yₙ), unikalny wielomian stopnia ≤ n przechodzący przez wszystkie punkty:
P(x) = Σᵢ₌₀ⁿ yᵢ · Πⱼ≠ᵢ (x - xⱼ) / (xᵢ - xⱼ)
**Zjawisko Runge'a:** Interpolacja wielomianowa wysokiego stopnia w równomiernie rozmieszczonych punktach może gwałtownie oscylować w pobliżu krawędzi. Łagodzone za pomocą węzłów lub splajnów Czebyszewa.
### Splajny sześcienne
Odcinkowe wielomiany sześcienne, które są ciągłe C² (ciągłe drugie pochodne).
| Wpisz | Warunek brzegowy |
|------|----------------------|
| Naturalny splajn | S''(x₀) = S''(xₙ) = 0 |
| Zaciśnięty wielowypust | Określono S'(x₀) i S'(xₙ) |
| Nie-węzeł | Trzecia pochodna ciągła przy x₁ i xₙ₋₁ |
---

## Rozwiązywanie ODE
Rozwiązywanie równań różniczkowych zwyczajnych dy/dt = f(t, y) numerycznie.
### Metoda Eulera
Najprostsze rozwiązanie ODE.
**Aktualizacja:** y_{n+1} = y_n + h · f(t_n, y_n)
| Nieruchomość | Wartość |
|---------|-------|
| Zamów | 1 (błąd na krok: O(h²), globalnie: O(h)) |
| Stabilność | Warunkowo stabilny (wymagane małe h) |
| Koszt | 1 ocena funkcji na krok |
### Metody Runge-Kutty
| Metoda | Zamów | Etapy | Notatki |
|--------|-------|--------|-------|
| **Eulera** | 1 | 1 | Najprostszy |
| **Punkt środkowy** | 2 | 2 | Lepsza dokładność |
| **Heuna (RK2)** | 2 | 2 | Predyktor-korektor |
| **Klasyczny RK4** | 4 | 4 | Standardowy koń pociągowy |
| **Dormand-Prince (RK45)** | 4 ust. 5 | 6 | Adaptacyjny rozmiar kroku (używany w ode45) |
### Klasyczny RK4 (Runge-Kutta czwartego rzędu)
k₁ = f(t_n, y_n)
k₂ = f(t_n + h/2, y_n + hk₁/2)
k₃ = f(t_n + h/2, y_n + hk₂/2)
k₄ = f(t_n + h, y_n + hk₃)
y_{n+1} = y_n + h(k₁ + 2k₂ + 2k₃ + k₄) / 6
| Nieruchomość | Wartość |
|---------|-------|
| Zamów | 4 (błąd globalny: O(h⁴)) |
| Koszt | 4 oceny funkcji na krok |
| Stabilność | Znacznie lepszy od Eulera |
| Użycie | Domyślne dla niesztywnych ODE |
### Sztywne ODE
**Sztywna** ODE ma komponenty, które różnią się w bardzo różnych skalach czasowych. Metody jawne (Euler, RK4) wymagają niepraktycznie małych rozmiarów kroków.
| Metoda | Wpisz | Stabilność |
|------------|------|---------------|
| Ukryty Euler | Ukryte | A-stabilny (bezwarunkowo stabilny) |
| Wzór różniczkowania wstecznego (BDF) | Ukryte | A-stabilny (do rzędu 5) |
| Ukryte Runge-Kutta | Ukryte | Istnieją warianty L-stabilne |
| LSODA | Automatyczny | Przełącza pomiędzy sztywnym/niesztywnym |
---

## Stabilność numeryczna i kondycjonowanie
### Numer warunku
**Numer warunku** mierzy, jak bardzo zmienia się wynik problemu w porównaniu z małymi zmianami na wejściu.
Dla układu liniowego Ax = b: κ(A) = ||A|| · ||A⁻¹||
| κ(A) | Interpretacja |
|-------|----------------------------|
| ≈ 1 | Dobrze uwarunkowany |
| 10³ | Lekko wrażliwy |
| 10⁸ | Źle uwarunkowany (straci ~8 cyfr dokładności) |
| → ∞ | Liczba pojedyncza (brak unikalnego rozwiązania) |
### Stabilność algorytmów
Algorytm jest **stabilny numerycznie**, jeśli małe zakłócenia na wejściu prowadzą do małych zaburzeń na wyjściu (w odniesieniu do numeru warunku problemu).
| Algorytm | Stabilny? | Notatki |
|----------|---------|-------|
| Eliminacja Gaussa z częściowym obracaniem | Tak | Podejście standardowe |
| Obliczanie wartości własnych za pomocą QR | Tak | Wstecznie stabilny |
| Sumowanie naiwne (najpierw duże + małe) | Nie | Użyj sumowania Kahana |
| Obliczanie wariancji jako E[X²] − (E[X])² | Potencjalnie nie | Użyj algorytmu online Welforda |
### Algorytm sieciowy Welforda
Numerycznie stabilne obliczanie średniej bieżącej i wariancji:
```
mean_new = mean_old + (x − mean_old) / n
M2_new = M2_old + (x − mean_old)(x − mean_new)
variance = M2 / (n − 1)
```

Pozwala to uniknąć katastrofalnego anulowania, które ma miejsce w naiwnej formule dwuprzebiegowej.
---

## Znaczenie dla uczenia maszynowego i nauki o danych
| Metoda numeryczna | Aplikacja |
|----------------|------------|
| Zmiennoprzecinkowy (fp16/fp32/bf16) | Trening o mieszanej precyzji, kwantyzacja modelu, wydajność pamięci |
| Znalezienie korzenia | Oszacowanie największej wiarygodności (znalezienie, gdzie gradient = 0) |
| Całkowanie numeryczne | Wnioskowanie bayesowskie (obliczanie prawdopodobieństw krańcowych), wartości oczekiwane |
| Interpolacja | Wygładzanie, imputacja, modele zastępcze, funkcje aktywacji |
| Rozwiązania ODE | Neuronowe ODE, RNN w czasie ciągłym, dynamika populacji, ML oparte na fizyce |
| Numer warunku | Rozumienie zagadnień numerycznych w regresji liniowej, równania normalne |
| Stabilne sumowanie | Obliczanie funkcji strat, statystyki normalizacji wsadowej |
| RK4 / solwery adaptacyjne | Symulacja systemów dynamicznych, szkolenie sieci o ciągłej głębokości |
---

## Streszczenie
| Temat | Podstawowy pomysł | Kluczowa metoda |
|-------|-----------|------------|
| Zmiennoprzecinkowy | Reprezentacja o skończonej precyzji | IEEE 754, podsumowanie Kahana |
| Znalezienie korzenia | Rozwiąż f(x) = 0 | Bisekcja, Newton-Raphson, Brenta |
| Całkowanie numeryczne | Przybliżone ∫f(x)dx | Trapezoidalny, Simpsona, kwadratura Gaussa |
| Interpolacja | Oszacowanie między punktami danych | Splajny sześcienne, Lagrange'a, RBF |
| Rozwiązania ODE | Rozwiąż dy/dt = f(t,y) | Euler, RK4, metody adaptacyjne |
| Stabilność | Wrażliwość na błędy zaokrągleń | Numer warunku, stabilne algorytmy |
Metody numeryczne to miejsce, w którym matematyka spotyka się z rzeczywistością. Żaden komputer nie jest w stanie dokładnie przedstawić większości liczb rzeczywistych, w praktyce żadna pochodna nie jest obliczana symbolicznie, a żadna całka nie jest obliczana w postaci zamkniętej dla problemów świata rzeczywistego. Zrozumienie metod numerycznych pozwala wybrać właściwy algorytm, przewidzieć jego dokładność i uniknąć subtelnych błędów, które wynikają z arytmetyki o skończonej precyzji.