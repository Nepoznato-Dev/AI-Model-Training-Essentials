---
# Metadata
title: "Control Theory"
description: "Transfer functions, block diagrams, feedback loops, PID controllers, stability analysis, state-space representation, and optimal control"
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
    changes: "Initial deep-dive into control theory"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2027-02-10"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-10"

# Classification
tags: [control-theory, transfer-functions, pid-controllers, feedback, stability, state-space, optimal-control]
difficulty_level: "advanced"
prerequisites:
  - "mathematics.md"
  - "signal_processing.md"
  - "dynamical_systems.md"
estimated_reading_time: "22 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Teoria kontroli
Teoria sterowania to matematyka polegająca na sprawianiu, że systemy zachowują się tak, jak tego chcemy. Od termostatów po autopiloty, od ramion robotów po reaktory chemiczne – systemy sterowania wykrywają, decydują i działają, aby utrzymać pożądane zachowanie. Dziedzina ta zapewnia rygorystyczne narzędzia do analizy stabilności, wydajności i solidności — koncepcji, które przeniosły się do uczenia się przez wzmacnianie, dostrajania hiperparametrów i systemów adaptacyjnych.
---

## Podstawowe pojęcia
### Pętla otwarta a pętla zamknięta
| Wpisz | Opis | Przykład | Zaleta |
|------|-------------|---------|----------|
| **Pętla otwarta** | Działanie sterujące niezależne od wyjścia | Timer pralki | Proste, nie wymaga czujnika |
| **Pętla zamknięta (sprzężenie zwrotne)** | Działanie sterujące zależy od wyjścia | Termostat, tempomat | Odrzuca zakłócenia, solidny |
### Elementy diagramu blokowego
| Element | Symbol | Funkcja |
|--------|--------|---------|
| **Roślina** | G(y) | Kontrolowany system |
| **Kontroler** | C(e) | Oblicza działanie kontrolne |
| **Czujnik** | H(-y) | Mierzy wynik |
| **Węzeł sumujący** | ⊕ | Oblicza błąd: r − y |
| **Odniesienie** | r(t) | Pożądany wynik |
| **Błąd** | e(t) = r(t) − y(t) | Różnica między pożądaną a rzeczywistą |
| **Zaburzenie** | d(t) | Niepożądane dane wpływające na instalację |
### Funkcja transferu w pętli zamkniętej
W przypadku standardowego systemu z ujemnym sprzężeniem zwrotnym:
T(s) = C(s)G(s) / (1 + C(s)G(s)H(s))
| Ilość | Formuła |
|--------------|--------|
| Funkcja transferu w otwartej pętli | L(s) = C(s)G(s)H(s) |
| Funkcja transferu w pętli zamkniętej | T(s) = L(s)/H(s) / (1 + L(s)) |
| Funkcja przesyłania błędów | E(s)/R(s) = 1 / (1 + L(s)) |
| Wrażliwość | S(s) = 1 / (1 + L(s)) |
---

## Funkcje przenoszenia
**Funkcja przenoszenia** H(s) = Y(s)/X(s) opisuje zależność wejście-wyjście liniowego układu niezmienniczego w czasie (LTI) w domenie Laplace'a.
### Formularze standardowe
| Systemu | Funkcja przeniesienia | Parametry |
|------------|----------------------|------------|
| **Pierwszego rzędu** | K/(τs + 1) | K = wzmocnienie, τ = stała czasowa |
| **Drugiego rzędu** | Kωₙ²/(s² + 2ζωₙs + ωₙ²) | ωₙ = częstotliwość drgań własnych, ζ = współczynnik tłumienia |
| **Integrator** | K/s | — |
| **Wyróżnik** | Ks | — |
| **Opóźnienie** | e^{−sT_d} | T_d = opóźnienie czasowe |
### Zachowanie systemu drugiego rzędu
| Współczynnik tłumienia ζ | Zachowanie | Lokalizacje biegunów |
|----------------|-----------|--------------|
| ζ = 0 | Nietłumione oscylacje | Czysta wyobraźnia |
| 0< ζ < 1 | Underdamped (oscillates, decays) | Complex with negative real part |
| ζ = 1 | Critically damped (fastest no-oscillation) | Real, repeated |
| ζ >1 | Przetłumiony (powolny, bez oscylacji) | Prawdziwy, wyraźny |
### Metryki wydajności (reakcja krokowa)
| Metryczne | Formuła (2. rzędu, niedotłumiona) | Opis |
|------------|--------------------------------------|------------|
| Czas narastania (t_r) | ≈ 1,8/ωₙ | Czas przejść z 10% do 90% |
| Godzina szczytu (t_p) | π/(ωₙ√(1−ζ²)) | Czas do pierwszego maksimum |
| Przekroczenie (M_p) | e^{−πζ/√(1−ζ²)} × 100% | Maksymalny szczyt powyżej wartości końcowej |
| Czas ustalania (t_s) | ≈ 4/(ζωₙ) | Czas utrzymać się w granicach 2% od ostatecznej wartości |
| Błąd stanu ustalonego | Zależy od typu systemu | Różnica między pożądaną a rzeczywistą jako t → ∞ |
---

## Kontrolery PID
**Regulator PID** jest najczęściej stosowanym regulatorem w przemyśle (ponad 90% regulatorów przemysłowych).
### Formuła PID
u(t) = K_p e(t) + K_i ∫₀ᵗ e(τ)dτ + K_d de(t)/dt
W domenie Laplace'a: C(s) = K_p + K_i/s + K_d s
| Termin | Efekt | Za dużo | Za mało |
|------|------------|--------------|------------|
| **Proporcjonalny (K_p)** | Reaguje na bieżący błąd | Oscylacja, niestabilność | Powolna reakcja, duży błąd |
| **Całka (K_i)** | Eliminuje błąd stanu ustalonego | Przeregulowanie, oscylacja | Stałe przesunięcie |
| **Pochodna (K_d)** | Przewiduje przyszły błąd (tłumienie) | Wzmocnienie hałasu | Słabe tłumienie zakłóceń |
### Metody strojenia PID
| Metoda | Podejście |
|------------|---------|
| **Ziegler-Nichols** | Zwiększaj K_u aż do oscylacji; użyj K_u i okresu P_u, aby ustawić wzmocnienia |
| **Cohen-Coon** | Na podstawie parametrów odpowiedzi skokowej (wzmocnienie, stała czasowa, czas martwy) |
| **IMC (wewnętrzna kontrola modelu)** | W oparciu o model procesu; zapewnia dobrą wytrzymałość |
| **Automatyczne strojenie** | Identyfikacja online + strojenie (wiele nowoczesnych sterowników) |
| **Podręcznik** | Zacznij tylko od K_p, dodaj K_i, aby usunąć przesunięcie, dodaj K_d dla tłumienia |
### Reguły Zieglera-Nicholsa
1. Ustaw K_i = K_d = 0
2. Zwiększaj K_p aż do trwałej oscylacji: wzmocnienie ostateczne K_u, okres P_u
3. Ustal zyski:
| Kontroler | K_p | K_i | K_d |
|----------|-----|-----|-----|
| P | 0,5K_u | — | — |
| PI | 0,45K_u | 1,2K_u/P_u | — |
| PID | 0,6K_u | 2K_u/P_u | K_u P_u/8 |
---

## Analiza stabilności
System jest **stabilny**, jeśli jego dane wyjściowe pozostają ograniczone dla ograniczonych wejść (stabilność BIBO).
### Stabilność oparta na słupach
| Stan | Stabilność |
|----------|-----------|
| Wszystkie bieguny w lewej półpłaszczyźnie (Re(s)< 0) | Stable |
| Any pole in right half-plane (Re(s) >0) | Niestabilny |
| Bieguny na urojonej osi (Re(s) = 0) | Marginalnie stabilny (lub niestabilny w przypadku powtarzających się) |
### Kryterium Routha-Hurwitza
Określa stabilność bez jawnego obliczania biegunów. Konstruuje tablicę Routha na podstawie charakterystycznych współczynników wielomianu.
**Reguła:** Liczba zmian znaku w pierwszej kolumnie jest równa liczbie biegunów prawej półpłaszczyzny.
### Kryterium stabilności Nyquista
Rysuje charakterystykę częstotliwościową L(jω) w otwartej pętli na płaszczyźnie zespolonej.
**Reguła:** Układ w pętli zamkniętej jest stabilny, jeśli wykres Nyquista otacza punkt (-1, 0) w kierunku przeciwnym do ruchu wskazówek zegara liczbę razy równą liczbie niestabilnych biegunów w pętli otwartej.
**Margines wzmocnienia:** O ile wzmocnienie może wzrosnąć przed niestabilnością (odległość od wykresu do -1 na osi rzeczywistej).
**Margines fazy:** Jak duże opóźnienie fazowe może wzrosnąć przed niestabilnością (kąt od wykresu do okręgu jednostkowego przy przejściu wzmocnienia).
### Analiza wykresu Bodego
Wykresy wzmocnienia (dB) i fazy (stopnie) w funkcji częstotliwości (skala logarytmiczna).
| Metryczne | Definicja | Pożądana wartość |
|--------|-----------|--------------|
| **Zyskaj marżę (GM)** | Zwiększenie wzmocnienia do 0 dB w fazie = −180° | > 6 dB |
| **Marża fazowa (PM)** | Faza przy zwrotnicy wzmocnienia (0 dB) + 180° | > 45° |
| **Zyskaj zwrotnicę** | Częstotliwość, gdzie wzmocnienie = 0 dB | — |
| **Zwrotnica faz** | Częstotliwość, gdzie faza = −180° | — |
---

## Reprezentacja w przestrzeni stanów
W przypadku systemów z wieloma wejściami i wieloma wyjściami (MIMO) forma przestrzeni stanów jest bardziej naturalna niż funkcje przenoszenia.
### Formularz standardowy
ẋ(t) = Ax(t) + Bu(t) (równanie stanu)
y(t) = Cx(t) + Du(t) (równanie wyjściowe)
| Matryca | Imię | Wymiary |
|------------|------|---------------|
| | Macierz systemu/stanu | n × n |
| B | Macierz wejściowa | n × m |
| C | Macierz wyjściowa | p × n |
| D | Macierz przelotowa | p × m |
### Funkcja przeniesienia z przestrzeni stanów
G(s) = C(sI – A)⁻¹B + D
### Sterowanie i obserwowalność
| Nieruchomość | Testuj | Znaczenie |
|---------|------|--------|
| **Sterowane** | Ranga[C_B] = n (gdzie C_B = [B, AB, A²B, ...]) | Może skierować się do dowolnego stanu |
| **Zaobserwowalne** | Ranga[O_B] = n (gdzie O_B = [C; CA; CA²; ...]) | Potrafi określić stan na podstawie wyjścia |
System musi być sterowalny, aby można go było ustabilizować za pomocą sprzężenia zwrotnego i aby był obserwowalny w celu oszacowania stanu.
### Opinia o stanie
u = −Kx + r (pełne sprzężenie zwrotne stanu)
Pętla zamknięta: ẋ = (A - BK)x + Br
**Umieszczenie biegunów:** Wybierz K tak, aby A − BK posiadało pożądane wartości własne (bieguny).
---

## Optymalna kontrola
### Liniowy regulator kwadratowy (LQR)
Minimalizacja: J = ∫₀^∞ (xᵀQx + uᵀRu) dt
gdzie Q ≥ 0 (koszt stanu) i R > 0 (koszt kontroli).
**Rozwiązanie:** u = −Kx gdzie K = R⁻¹BᵀP, a P rozwiązuje **algebraiczne równanie Riccatiego:**
AᵀP + PA – PBR⁻¹BᵀP + Q = 0
| Strojenie | Efekt |
|------------|------------|
| Zwiększ Q | Szybsza reakcja, większy wysiłek w zakresie kontroli |
| Zwiększ R | Wolniejsza reakcja, mniejszy wysiłek w zakresie kontroli |
| Q ≫ R | Agresywna kontrola (jak wysokie K_p) |
### Filtr Kalmana
Optymalny estymator stanu układów liniowych z szumem Gaussa.
**Model systemu:**
ẋ = Ax + Bu + w (szum procesu w ~ N(0, Q))
y = Cx + v (szum pomiarowy v ~ N(0, R))
**Równania filtra Kalmana:**
- Przewiduj: x̂⁻ = Ax̂ + Bu, P⁻ = APAᵀ + Q
- Aktualizacja: K = P⁻Cᵀ(CP⁻Cᵀ + R)⁻¹, x̂ = x̂⁻ + K(y - Cx̂⁻), P = (I - KC)P⁻
Filtr Kalmana jest podwójnym filtrem LQR — minimalizuje wariancję błędu estymacji.
---

## Znaczenie dla uczenia maszynowego i nauki o danych
| Koncepcja teorii sterowania | Aplikacja |
|----------------------|------------|
| Kontrola sprzężenia zwrotnego | Adaptacyjne tempo uczenia się, stabilizacja treningu |
| regulatory PID | Strojenie hiperparametrów, kontrola temperatury w centrach danych |
| Modele przestrzeni stanów | Modelowanie szeregów czasowych, rekurencyjne sieci neuronowe |
| Filtr Kalmana | Śledzenie, fuzja czujników, estymacja stanu, prognozowanie szeregów czasowych |
| LQR / optymalna kontrola | Uczenie się przez wzmacnianie (sterowanie LQG), robotyka |
| Analiza stabilności | Dynamika uczenia sieci GAN, zbieżność algorytmów RL |
| Kontrolowalność/obserwowalność | Zrozumienie wyrazistości RNN, identyfikacja systemu |
| Funkcje przenoszenia | Zrozumienie CNN jako filtrów liniowych, analiza w dziedzinie częstotliwości |
| Nyquista/Bode | Analiza wytrzymałości dla systemów adaptacyjnych |
| Umieszczenie bieguna | Projektowanie dynamiki systemów wyuczonych (Neural ODE) |
---

## Streszczenie
| Koncepcja | Podstawowy pomysł | Kluczowe narzędzie |
|--------|-----------|---------|
| Informacje zwrotne | Użyj wyjścia, aby poprawić dane wejściowe | Funkcja transferu w pętli zamkniętej |
| Funkcja przenoszenia | Relacja wejście-wyjście w domenie s | G(s) = Y(s)/X(s) |
| Sterowanie PID | Proporcjonalne + Całkowanie + Pochodna | Najpopularniejszy sterownik przemysłowy |
| Stabilność | Ograniczone wyjście dla ograniczonego wejścia | Routh-Hurwitz, Nyquist, Bode |
| Przestrzeń stanów | Reprezentacja stanu wewnętrznego | ẋ = Ax + Bu, y = Cx + Du |
| Sterowność | Czy możemy dotrzeć do dowolnego stanu? | Test rangowy na macierzy sterowalności |
| Obserwowalność | Czy możemy określić stan? | Test rangowy na macierzy obserwowalności |
| LQR | Optymalna informacja zwrotna o stanie | Równanie Riccatiego |
| Filtr Kalmana | Optymalne oszacowanie stanu | Cykl przewidywania i aktualizacji |
Teoria sterowania to matematyka polegająca na sprawianiu, że systemy robią to, co chcesz — niezawodnie, solidnie i wydajnie. Zawarte w nim zasady sprzężenia zwrotnego, stabilności i optymalności okazały się uniwersalne, pojawiając się w dziedzinach od robotyki po uczenie się przez wzmacnianie, od ekonomii po biologię. Analitykom zajmującym się danymi teoria sterowania zapewnia język umożliwiający zrozumienie systemów adaptacyjnych, projektowanie stabilnych procedur szkoleniowych i budowanie inteligentnych agentów wchodzących w interakcję z dynamicznymi środowiskami.