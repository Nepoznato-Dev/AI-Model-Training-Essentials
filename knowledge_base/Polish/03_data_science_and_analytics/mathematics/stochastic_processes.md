---
# Metadata
title: "Stochastic Processes"
description: "Random variables review, Markov chains, random walks, Brownian motion, Poisson processes, martingales, Monte Carlo methods, and MCMC"
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
    date: "2026-08-10"
    author: "AI Model Training Team"
    changes: "Initial deep-dive into stochastic processes"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2027-02-10"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-10"

# Classification
tags: [stochastic-processes, markov-chains, random-walks, brownian-motion, poisson-processes, martingales, monte-carlo, mcmc]
difficulty_level: "advanced"
prerequisites:
  - "statistics_and_probability.md"
  - "real_analysis.md"
estimated_reading_time: "28 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# Procesy stochastyczne
**Proces stochastyczny** to zbiór zmiennych losowych indeksowanych czasowo (lub przestrzennie). Podczas gdy teoria prawdopodobieństwa bada indywidualne zdarzenia losowe, procesy stochastyczne badają ewolucję losowości w czasie. Modelują ceny akcji, długość kolejek, rozprzestrzenianie się chorób, generowanie języka i dynamikę uczenia modeli uczenia maszynowego.
---

## Fundamenty
### Definicja
Proces stochastyczny {X_t : t ∈ T} jest rodziną zmiennych losowych zdefiniowanych na wspólnej przestrzeni prawdopodobieństwa. T to **zestaw indeksów** (czas):
- **Czas dyskretny:** T = {0, 1, 2, ...}
- **Czas ciągły:** T = [0, ∞)
**Przestrzeń stanów** S jest zbiorem możliwych wartości, jakie może przyjąć X_t.
### Właściwości klucza
| Nieruchomość | Definicja |
|-------------|------------|
| **Stacjonarność** | Wspólny rozkład (X_{t₁}, ..., X_{tₖ}) taki sam jak (X_{t₁+τ}, ..., X_{tₖ+τ}) |
| **Niepodległość** | X_t niezależnie od X_s dla t ≠ s |
| **Ergodyczność** | Średnie czasowe zbiegają się ze średnimi zespołowymi |
| **Własność Markowa** | Przyszłość zależy tylko od teraźniejszości, a nie przeszłości |
| **Martyngał** | Oczekiwana przyszła wartość jest równa wartości bieżącej |
---

## Łańcuchy Markowa
**Łańcuch Markowa** to proces stochastyczny, w którym stan przyszły zależy tylko od stanu bieżącego (właściwość pozbawiona pamięci).
### Łańcuchy Markowa w czasie dyskretnym (DTMC)
P(X_{n+1} = j | X_n = i, X_{n-1} = i_{n-1}, ...) = P(X_{n+1} = j | X_n = i) = p_{ij}
**Macierz przejść** P ma wpisy p_{ij} = P(idź do j | aktualnie w i).
| Nieruchomość | Oświadczenie |
|---------|-----------|
| Sumy wierszy | Każdy wiersz sumuje się do 1: Σⱼ p_{ij} = 1 |
| przejście n-etapowe | P(X_{n+m} = j | X_m = i) = (Pⁿ)_{ij} |
| Dystrybucja stacjonarna | πP = π (lewy wektor własny o wartości własnej 1) |
### Klasyfikacja państw
| Termin | Definicja |
|------|------------|
| **Powtarzające się** | Łańcuch powraca do stanu i z prawdopodobieństwem 1 |
| **Przejściowe** | Niezerowe prawdopodobieństwo, że nigdy nie powróci |
| **Wciągające** | p_{ii} = 1 (raz wszedł, nigdy nie wyszedł) |
| **Kropka** | GCD czasów powrotu; okres 1 = aperiodyczny |
| **Komunikowanie** | Stany i oraz j mogą się ze sobą kontaktować |
### Dystrybucja stacjonarna
Dla nieredukowalnego, dodatniego, powtarzającego się łańcucha Markowa rozkład stacjonarny π istnieje, jest unikalny i spełnia:
πP = π, Σᵢ πᵢ = 1
**Interpretacja:** πᵢ = długoterminowa proporcja czasu spędzonego w stanie i.
**Przykład praktyczny:** model pogody ze stanami {słonecznie, deszczowo}.
P = [[0,9, 0,1], [0,5, 0,5]] (wiersze: od Sunny, od Rainy)
Rozkład stacjonarny: πP = π
- π₁ = 0,9π₁ + 0,5π₂
- π₂ = 0,1π₁ + 0,5π₂
- π₁ + π₂ = 1
- Rozwiązywanie: π₁ = 5/6 ≈ 0,833, π₂ = 1/6 ≈ 0,167
### Zbieżność do stacjonarności
Dla nieredukowalnego, aokresowego, dodatniego łańcucha powtarzającego się:
- Pⁿ → Π (macierz ze wszystkimi wierszami równymi π) jako n → ∞
- **Czas mieszania:** Liczba kroków do momentu, aż rozkład będzie bliski π
- **Odstęp widmowy:** 1 − |λ₂| (gdzie λ₂ jest drugą co do wielkości wartością własną) określa prędkość mieszania
### Ciągłe łańcuchy Markowa (CTMC)
Przejścia zachodzą w losowych momentach regulowanych rozkładami wykładniczymi.
| Koncepcja | Opis |
|--------|------------|
| **Macierz stawek Q** | q_{ij} ≥ 0 dla i ≠ j; q_{ii} = −Σ_{j≠i} q_{ij} |
| **Prawdopodobieństwa przejścia** | P(t) = e^{Qt} (macierz wykładnicza) |
| **Dystrybucja stacjonarna** | πQ = 0 |
| **Czas utrzymywania** | Czas w stanie i wynosi Exp(−q_{ii}) |
---

## Losowe spacery
**Spacer losowy** to ścieżka utworzona przez kolejne losowe kroki.
### Prosty losowy spacer
X_n = X_{n-1} + Z_n, gdzie Z_n ∈ {+1, −1} z prawdopodobieństwami p, q = 1−p.
| Nieruchomość | p = 1/2 (symetryczny) | p ≠ 1/2 (stronniczy) |
|---------|---------------------|--------------------------------|
| E[X_n] | 0 | n(2p−1) |
| Var[X_n] | n | 4npq |
| Powrót do źródła? | Tak (z prawdopodobieństwem 1) | Nie (odpływa) |
| Powtarzający się? | Tak (w 1D i 2D) | Nie |
### Losowy spacer w wyższych wymiarach
| Wymiar | Powtarzający się? | Intuicja |
|----------|------------|----------|
| 1D | Tak | „Pijany człowiek zawsze odnajdzie drogę do domu” |
| 2D | Tak | „Pijany ptak zawsze znajdzie drogę do domu” |
| 3D+ | Nie | „Pijany wróbel nigdy nie trafia do domu” |
### Połączenie z ruchem Browna
Skalowanie spaceru losowego: niech S_n = ΣZ_i. Następnie jako wielkość kroku → 0 i kroki → ∞:
S_{⌊nt⌋} / √n → B(t) (ruchy Browna, zgodnie z twierdzeniem Donskera)
---

## Ruchy Browna
**Ruch Browna** (proces Wienera) B(t) to ciągła granica błądzenia losowego.
### Definicja
B(t) spełnia:
1. B(0) = 0
2. B(t) ma ścieżki ciągłe
3. Przyrosty niezależne: B(t) − B(s) jest niezależne od B(s) − B(r) dla r < s < t
4. B(t) − B(s) ~ N(0, t − s) (przyrosty Gaussa)
### Właściwości klucza
| Nieruchomość | Oświadczenie |
|---------|-----------|
| E[B(t)] | = 0 |
| Var[B(t)] | = t |
| Cov[B(s), B(t)] | = min(s, t) |
| Nigdzie różniczkowalne | Ścieżki są ciągłe, ale nie mają pochodnej |
| Wymiar fraktalny | Wykres ma wymiar Hausdorffa 3/2 |
| Własność Markowa | Przyszłość zależy tylko od aktualnej pozycji |
| Martingale | E[B(t) | F_s] = B(s) dla s < t |
### Geometryczne ruchy Browna
S(t) = S(0) exp((μ - σ²/2)t + σB(t))
Jest to standardowy model cen akcji w modelu Blacka-Scholesa.
- μ: dryf (oczekiwany zwrot)
- σ: zmienność
---

## Procesy Poissona
A **Proces Poissona** N(t) zlicza liczbę zdarzeń zachodzących w [0, t].
### Definicja
N(t) ~ Poissona(λt), gdzie λ jest szybkością (zdarzenia na jednostkę czasu).
| Nieruchomość | Oświadczenie |
|---------|-----------|
| N(0) = 0 | — |
| Niezależne przyrosty | Zdarzenia w rozłącznych przedziałach są niezależne |
| Przyrosty stacjonarne | N(t+s) − N(s) ~ Poissona(λt) |
| E[N(t)] | = λt |
| Var[N(t)] | = λt |
| Godziny przylotów | Rozkład wykładniczy: T_i ~ Exp(λ) |
### Uogólnienia
| Wariant | Opis |
|--------|------------|
| **Niejednorodny** | Szybkość λ(t) zmienia się w czasie |
| **Związek Poissona** | Każde zdarzenie ma losowy rozmiar: S(t) = Σᵢ₌₁^{N(t)} Yᵢ |
| **Losowa miara Poissona** | Punkty w czasoprzestrzeni, nie tylko czasie |
| **Wielowymiarowe** | Wiele typów zdarzeń z możliwymi interakcjami |
---

## Martingale
**Martyngał** to uczciwa gra: oczekiwana przyszła wartość, biorąc pod uwagę wszystkie aktualne informacje, jest równa wartości bieżącej.
### Definicja
{X_n} jest martyngałem względem filtracji {F_n} jeśli:
1. X_n jest F_n-mierzalne (dostosowane)
2. E[|X_n|] < ∞ (całkowalne)
3. E[X_{n+1} | F_n] = X_n (uczciwa gra)
| Wariant | Stan | Interpretacja |
|--------|-----------|----------------|
| **Martyngał** | E[X_{n+1} | F_n] = X_n | Uczciwa gra |
| **Podmartyngał** | E[X_{n+1} | F_n] ≥ X_n | Korzystna gra (trend w górę) |
| **Supermartingale** | E[X_{n+1} | F_n] ≤ X_n | Niekorzystna gra (trend spadkowy) |
### Kluczowe twierdzenia
| Twierdzenie | Oświadczenie |
|--------|-----------|
| **Opcjonalne zatrzymanie** | W określonych warunkach E[X_T] = E[X_0] dla czasu zatrzymania T |
| **Konwergencja** | Ograniczony martyngał jest zbieżny prawie na pewno |
| **Maksymalna nierówność** | P(max_{k≤n} X_k ≥ λ) ≤ E[X_n] / λ (Doob'a) |
---

## Metody Monte Carlo
**Metody Monte Carlo** wykorzystują losowe próbkowanie do oszacowania wielkości deterministycznych.
### Podstawowy pomysł
Aby oszacować E[f(X)] gdzie X ~ P:
1. Pobierz N próbek: x₁, x₂, ..., x_N z P
2. Oblicz: Î = (1/N) Σᵢ f(xᵢ)
3. Z prawa wielkich liczb: Î → E[f(X)] jako N → ∞
**Błąd:** Błąd standardowy = σ_f / √N, gdzie σ_f² = Var[f(X)]
### Techniki redukcji wariancji
| Technika | Pomysł | Przyspieszenie |
|----------|------|--------|
| **Ważność pobierania próbek** | Próbka z Q zamiast P, waga według P/Q | Może być dramatyczny |
| **Antytetyczne różnice** | Użyj par (x, −x), aby anulować wariancję | ~2x |
| **Kontrola jest zmienna** | Odejmij znaną funkcję oczekiwań skorelowaną z f | Różnie |
| **Pobieranie próbek warstwowych** | Podziel domenę, wypróbuj każdą warstwę | Zmniejsza wariancję |
| **Rao-Blackwell** | Warunek wystarczających statystyk | Zawsze pomaga |
---

## Łańcuch Markowa Monte Carlo (MCMC)
MCMC konstruuje łańcuch Markowa, którego rozkład stacjonarny jest rozkładem docelowym. Po okresie „wypalania” próbki są przybliżone do wartości docelowej.
### Algorytm Metropolisa-Hastingsa
| Krok | Akcja |
|------|------------|
| 1 | Stan obecny: x_t |
| 2 | Zaproponuj: x* ~ q(x* \| x_t) (rozkład propozycji) |
| 3 | Współczynnik akceptacji: α = min(1, [π(x*)q(x_t\|x*)] / [π(x_t)q(x*\|x_t)]) |
| 4 | Zaakceptuj z prawdopodobieństwem α: x_{t+1} = x* (zaakceptuj) lub x_t (odrzuć) |
**Przypadek szczególny — algorytm Metropolis:** Propozycja symetryczna q(x*|x) = q(x|x*), więc α = min(1, π(x*)/π(x_t)).
### Próbkowanie Gibbsa
Specjalny przypadek Metropolis-Hastings, w którym każda zmienna jest aktualizowana na podstawie pełnego rozkładu warunkowego.
Dla docelowego π(x₁, x₂, ..., xₖ):
1. Próbka x₁^{(t+1)} ~ π(x₁ | x₂^{(t)}, ..., xₖ^{(t)})
2. Próbka x₂^{(t+1)} ~ π(x₂ | x₁^{(t+1)}, x₃^{(t)}, ..., xₖ^{(t)})
3. Kontynuuj dla wszystkich zmiennych
4. Powtórz
| Nieruchomość | Oświadczenie |
|---------|-----------|
| Zawsze akceptuje | α = 1 (bez etapu odrzucenia) |
| Wymaga | Możliwość próbkowania z każdego pełnego warunku |
| Konwergencja | Gwarantowane dla nieredukowalnych, nieokresowych łańcuchów |
### Diagnostyka MCMC
| Diagnostyczny | Cel |
|---------------|--------|
| **Wykres śledzenia** | Wizualna kontrola mieszania i stacjonarności |
| **Autokorelacja** | Mierzy zależność próbki (chcesz niską autokorelację) |
| **Gelman-Rubin (R̂)** | Porównaj wiele łańcuchów; R̂ < 1,05 sugeruje zbieżność |
| **Efektywna wielkość próby** | N_eff = N / (1 + 2Σρₖ); uwzględnia autokorelację |
| **Wypalenie** | Odrzuć początkowe próbki, zanim łańcuch osiągnie stacjonarność |
---

## Znaczenie dla uczenia maszynowego i nauki o danych
| Proces stochastyczny | Aplikacja |
|--------------------------------|------------|
| Łańcuchy Markowa | PageRank (losowy spacer po wykresie internetowym), generowanie tekstu (modele n-gramowe), MCMC |
| Przypadkowe spacery | Node2Vec i DeepWalk (osadzanie wykresów), eksploracja w RL |
| Ruchy Browna | Modelowanie cen akcji, modele dyfuzyjne w generatywnej AI |
| Procesy Poissona | Modelowanie nadejścia zdarzeń (kliknięcia, niepowodzenia), teoria kolejkowania |
| Martingale | Matematyka finansowa, dowodzenie zbieżności SGD (przybliżenie stochastyczne) |
| Monte Carlo | Szacowanie wartości oczekiwanych, wnioskowanie bayesowskie, uczenie się przez wzmacnianie (ewaluacja polityki) |
| MCMC (Metropolis-Hastings) | Próbkowanie późniejsze Bayesa, programowanie probabilistyczne (Stan, PyMC) |
| Próbkowanie Gibbsa | Modele tematyczne (LDA), sieci Bayesa, odszumianie obrazu |
| Diagnostyka MCMC | Zapewnienie rzetelnego wnioskowania z modeli probabilistycznych |
---

## Streszczenie
| Proces | Przestrzeń stanu | Czas | Kluczowa właściwość |
|-------------|------------|------|------------|
| Łańcuch Markowa | Dyskretny/ciągły | Dyskretny/ciągły | Bez pamięci (własność Markowa) |
| Przypadkowy spacer | ℤᵈ | Dyskretny | Suma i.i.d. kroki |
| Ruchy Browna | ℝ | Ciągłe | Przyrosty Gaussa, ścieżki ciągłe |
| Proces Poissona | ℕ | Ciągłe | Proces zliczania z lukami wykładniczymi |
| Martingale | ℝ | Dyskretny/ciągły | Uczciwa gra (E[X_{t+1}|F_t] = X_t) |
Procesy stochastyczne to matematyka losowości w czasie. Stanowią one podstawę współczesnego wnioskowania bayesowskiego (MCMC), uczenia się przez wzmacnianie (procesy decyzyjne Markowa), modelowania generatywnego (modele dyfuzji), matematyki finansowej i teorii kolejek. Zrozumienie tych procesów daje narzędzia do dynamicznego modelowania niepewności — nie tylko w postaci migawki, ale w miarę jej ewolucji.