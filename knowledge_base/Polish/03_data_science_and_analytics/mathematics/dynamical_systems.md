<!--
---
# Metadata
title: "Dynamical Systems"
description: "Ordinary and partial differential equations, phase portraits, equilibrium and stability, Lyapunov functions, chaos theory, Lorenz attractor, bifurcation diagrams, and PDEs"
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
    changes: "Initial deep-dive into dynamical systems"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2027-02-10"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-10"

# Classification
tags: [dynamical-systems, ode, pde, phase-portraits, stability, chaos, lorenz-attractor, bifurcation, lyapunov]
difficulty_level: "advanced"
prerequisites:
  - "mathematics.md"
  - "real_analysis.md"
  - "numerical_methods.md"
estimated_reading_time: "28 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Systemy dynamiczne
**System dynamiczny** opisuje ewolucję stanu w czasie zgodnie z ustaloną regułą. Od orbit planet po dynamikę populacji, od wzorców pogodowych po szkolenie sieci neuronowych – teoria systemów dynamicznych dostarcza języka i narzędzi pozwalających zrozumieć, jak wszystko się zmienia. Ten plik obejmuje równania różniczkowe zwyczajne (ODE), równania różniczkowe cząstkowe (PDE), analizę stabilności, chaos i bifurkacje.
---

## Równania różniczkowe zwyczajne (ODE)
ODE wiąże funkcję z jej pochodnymi w odniesieniu do pojedynczej zmiennej niezależnej (zwykle czasu).
### Klasyfikacja
| Nieruchomość | Typy |
|---------|-------|
| **Zamów** | Najwyższy obecny pochodny (pierwszy rząd, drugi rząd itd.) |
| **Liniowy a nieliniowy** | Liniowe: y'' + p(t)y' + q(t)y = g(t); Nieliniowy: cokolwiek innego |
| **Jednorodne** | g(t) = 0 (brak składnika wymuszającego) |
| **Autonomiczny** | Brak wyraźnej zależności od czasu: dy/dt = f(y) |
| **Współczynniki stałe** | p, q są stałymi |
### ODE pierwszego rzędu
**Forma ogólna:** dy/dt = f(t, y)
| Wpisz | Formularz | Metoda rozwiązania |
|------|------|--------------------------------|
| Rozłączne | dy/dt = g(t)h(y) | Oddziel i całkuj: ∫dy/h(y) = ∫g(t)dt |
| Liniowy pierwszego rzędu | dy/dt + p(t)y = q(t) | Współczynnik całkujący: μ(t) = e^(∫p dt) |
| Dokładnie | M(t,y)dt + N(t,y)dy = 0 przy ∂M/∂y = ∂N/∂t | Znajdź potencjalną funkcję F(t,y) |
| Bernoulliego | dy/dt + p(t)y = q(t)yⁿ | Zastąp v = y^(1−n), aby linearyzować |
**Przykład praktyczny (czynnik całkujący):** Rozwiąż dy/dt + 2y = e^(−t), y(0) = 1.
- Współczynnik całkujący: μ(t) = e^(∫2 dt) = e^(2t)
- Pomnóż: d/dt[e^(2t)y] = e^(2t) · e^(−t) = e^t
- Całkuj: e^(2t)y = e^t + C
- y(t) = e^(−t) + Ce^(−2t)
- Warunek początkowy: y(0) = 1 → 1 = 1 + C → C = 0
- Rozwiązanie: y(t) = e^(−t)
### Liniowe ODE drugiego rzędu
**Forma ogólna:** ay'' + by' + cy = g(t)
**Przypadek jednorodny** (g ​​= 0): Rozwiąż równanie charakterystyczne ar² + br + c = 0.
| Dyskryminujący | Korzenie | Rozwiązanie ogólne |
|------------|-------|--------------------------------|
| b² > 4ac (przetłumiony) | Dwa różne rzeczywiste r₁, r₂ | y = C₁e^(r₁t) + C₂e^(r₂t) |
| b² = 4ac (tłumiony krytycznie) | Powtórzony pierwiastek rzeczywisty r | y = (C₁ + C₂t)e^(rt) |
| b² < 4ac (niedotłumiony) | Złożone pierwiastki α ± βi | y = e^(αt)(C₁ cos βt + C₂ sin βt) |
**Interpretacja fizyczna:** Układ masa-sprężyna-tłumik mx'' + bx' + kx = 0.
- Przetłumione: silne tłumienie, brak oscylacji (zamykacz)
- Krytycznie tłumione: najszybszy powrót bez oscylacji (docelowy projekt zawieszenia samochodu)
- Underdamped: oscyluje ze zmniejszającą się amplitudą (struna gitarowa)
### Systemy ODE
Wiele rzeczywistych systemów obejmuje wiele oddziałujących na siebie zmiennych:
dx/dt = f(x, y)
dy/dt = g(x, y)
Można to zapisać w postaci wektorowej: d**x**/dt = **F**(**x**)
**Układy liniowe:** d**x**/dt = A**x**, gdzie A jest macierzą.
Rozwiązanie zależy od wartości własnych A:
| Wartości własne | Zachowanie |
|------------|---------------|
| Zarówno prawdziwe, jak i negatywne | Węzeł stabilny (wszystkie trajektorie zbiegają się do początku) |
| Obydwa prawdziwe, pozytywne | Niestabilny węzeł |
| Prawdziwe, przeciwne znaki | Punkt siodłowy (niestabilny) |
| Złożona, ujemna część rzeczywista | Stabilna spirala (oscylacje tłumione) |
| Złożona, dodatnia część rzeczywista | Niestabilna spirala |
| Czysta wyobraźnia | Centrum (orbity zamknięte) |
---

## Portrety fazowe
**Portret fazowy** wizualizuje trajektorie układu dynamicznego w przestrzeni stanów (bez bezpośredniego rozwiązywania).
### Kluczowe funkcje
| Funkcja | Opis |
|--------|------------|
| **Punkt stały (równowaga)** | Gdzie dx/dt = 0 (brak ruchu) |
| **Trajektoria** | Ścieżka śledzona przez system w przestrzeni stanów |
| **Nullcline** | Krzywa, w której pochodna jednej ze składowych wynosi zero |
| **Cykl graniczny** | Izolowana orbita zamknięta (oscylacja samopodtrzymująca) |
| **Basen atrakcji** | Zbiór warunków początkowych prowadzących do danego atraktora |
| **Separator** | Granica pomiędzy różnymi basenami przyciągania |
### Model drapieżnika-ofiary (Lotka-Volterra)
dx/dt = αx - βxy (ofiara)
dy/dt = δxy - γy (drapieżnik)
**Stałe punkty:**
1. (0, 0) — wygaszanie (punkt siodłowy)
2. (γ/δ, α/β) — współistnienie (centrum — orbity zamknięte)
System wykazuje okresowe oscylacje: wzrost liczby ofiar → wzrost liczby drapieżników → spadek liczby ofiar → spadek liczby drapieżników → cykl się powtarza.
---

## Analiza stabilności
### Stabilność liniowa
Dla stałego punktu x* dokonaj linearyzacji wokół niego: niech u = x − x*, następnie du/dt ≈ J(x*)u gdzie J jest macierzą Jakobianu.
**Kryterium stabilności:** Punkt stały to:
- **Stabilny**, jeśli wszystkie wartości własne J mają ujemne części rzeczywiste
- **Niestabilny** jeśli jakakolwiek wartość własna ma dodatnią część rzeczywistą
- **Marginalnie stabilny** jeśli wartości własne mają zerowe części rzeczywiste (wymagana jest analiza nieliniowa)
### Stabilność Lapunowa
**Bezpośrednia metoda Lapunowa** określa stabilność bez linearyzacji.
A **Funkcja Lapunowa** V(x) spełnia:
1. V(x*) = 0 i V(x) > 0 dla x ≠ x* (dodatnie określone)
2. dV/dt ≤ 0 wzdłuż trajektorii (nierosnące)
| Stan | Wniosek |
|--------------|------------|
| dV/dt< 0 (negative definite) | Asymptotically stable |
| dV/dt ≤ 0 (negative semi-definite) | Stable (but may not converge) |
| dV/dt >0 | Niestabilny |
**Przykład praktyczny:** System dx/dt = −x + y², dy/dt = −y.
- Spróbuj V(x,y) = x² + y² (funkcja podobna do energii)
- dV/dt = 2x(−x + y²) + 2y(−y) = −2x² + 2xy² − 2y²
- Bliski początek: dV/dt ≈ −2x² − 2y² < 0 (dla małego y dominuje −2y²)
- Wniosek: pochodzenie jest lokalnie asymptotycznie stabilne
---

## Teoria chaosu
**Chaos** jest deterministyczny, ale nieprzewidywalny: system kieruje się dokładnymi regułami, ale niewielkie różnice w warunkach początkowych prowadzą do zupełnie różnych wyników.
### Wymagania dla Chaosu
| Nieruchomość | Opis |
|---------|------------|
| Deterministyczny | Żadnej losowości — regulowanej dokładnymi równaniami |
| Wrażliwy na warunki początkowe | Pobliskie trajektorie rozchodzą się wykładniczo |
| Ograniczony | Trajektorie nie uciekają w nieskończoność |
| Nieokresowe | Nigdy nie powtarza się dokładnie |
### System Lorenza
Klasyczny przykład chaosu deterministycznego:
dx/dt = σ(y - x)
dy/dt = x(ρ – z) – y
dz/dt = xy – βz
Przy standardowych parametrach σ = 10, ρ = 28, β = 8/3:
- System ma trzy stałe punkty, wszystkie niestabilne
- Trajektorie krążą wokół jednego stałego punktu, a następnie nagle przełączają się na drugi
- Rezultatem jest **atraktor Lorenza** — dziwny atraktor o strukturze fraktalnej
**Wykładnik Lapunowa:** Mierzy stopień rozbieżności pobliskich trajektorii.
- Dodatni wykładnik Lapunowa → chaos
- Dla układu Lorenza o parametrach standardowych: największy wykładnik ≈ 0,9 > 0
### Mapa logistyczna
Prosty system dyskretny wykazujący chaos:
x_{n+1} = rx_n(1 − x_n)
| Parametr r | Zachowanie |
|------------|---------------|
| 0 < r < 1 | Populacja wymiera (x → 0) |
| 1 < r < 3 | Stabilny punkt stały przy x = 1 - 1/r |
| 3 < r < 3,449 | Oscylacja okresu 2 |
| 3,449 < r < 3,544 | Oscylacja okresu 4 |
| 3,544 < r < 3,570 | Okres-8, 16, 32, ... (kaskada podwajania okresu) |
| r ≈ 3,570 | Początek chaosu |
| 3,570 < r < 4 | Przeważnie chaotyczny, z okresowymi oknami |
| r = 4 | Całkowicie chaotyczny na [0, 1] |
### Efekt motyla
Popularna nazwa wrażliwej zależności od warunków początkowych. W systemach pogodowych (modelowanych za pomocą równań Lorenza) motyl trzepoczący skrzydłami w Brazylii może wywołać tornado w Teksasie – nie dlatego, że motyl je powoduje, ale dlatego, że drobne zakłócenia rosną wykładniczo.
---

## Teoria bifurkacji
**Rozwidlenie** to jakościowa zmiana w zachowaniu systemu w wyniku zmiany parametru.
### Rodzaje bifurkacji
| rozwidlenie | Normalna forma | Co się dzieje |
|------------|------------|-------------|
| **Węzeł siodłowy** | dx/dt = r - x² | Pojawiają się/znikają dwa stałe punkty |
| **Transkrytyczny** | dx/dt = rx – x² | Stabilność wymiany dwóch punktów stałych |
| **Widły (nadkrytyczne)** | dx/dt = rx – x³ | Jeden stabilny punkt dzieli się na dwa stabilne + jeden niestabilny |
| **Widły (podkrytyczne)** | dx/dt = rx + x³ | Niestabilne gałęzie zapadają się (często katastrofalnie) |
| **Hop** | Układ 2D | Punkt stały staje się niestabilny, pojawia się cykl graniczny |
### Diagram bifurkacji
Wykres punktów stałych w funkcji wartości parametru, pokazujący stabilność (ciągły = stabilny, przerywany = niestabilny). Diagram bifurkacji mapy logistycznej ukazuje drogę prowadzącą do chaosu przez podwojenie okresu i słynną **stała Feigenbauma** δ ≈ 4,669 (uniwersalny stosunek pomiędzy kolejnymi przedziałami bifurkacji).
---

## Częściowe równania różniczkowe (PDE)
PDE obejmują funkcje wielu zmiennych i ich pochodne cząstkowe.
### Klasyfikacja liniowych PDE drugiego rzędu
Dla Au_xx + 2Bu_xy + Cu_yy + ... = 0:
| Wpisz | Stan | Zachowanie | Przykład |
|------|-----------|-----------|---------|
| **Eliptyczny** | B² – AC< 0 | Steady-state, no time dependence | Laplace's equation: ∇²u = 0 |
| **Parabolic** | B² − AC = 0 | Diffusion, smoothing over time | Heat equation: u_t = αu_xx |
| **Hyperbolic** | B² − AC >0 | Propagacja fal, zachowuje ostre rysy | Równanie falowe: u_tt = c²u_xx |
### Równanie ciepła
∂u/∂t = α ∂²u/∂x²
Modele dyfuzji ciepła, rozproszenia populacji, wyceny opcji (Black-Scholes).
| Nieruchomość | Oświadczenie |
|---------|-----------|
| Wygładzanie | Rozwiązania stają się płynne natychmiast, nawet w przypadku nieciągłych danych początkowych
| Zasada maksimum | Maksymalna temperatura występuje w czasie granicznym lub początkowym |
| Odwracalność w czasie | Nieodwracalne — nie można cofnąć się |
### Równanie fali
∂²u/∂t² = c² ∂²u/∂x²
Modele drgań strun, dźwięku, fal elektromagnetycznych.
| Nieruchomość | Oświadczenie |
|---------|-----------|
| Rozmnażanie | Zakłócenia poruszają się z prędkością c |
| Odwracalność | Odwracalne w czasie |
| rozwiązanie d'Alemberta | u(x,t) = f(x−ct) + g(x+ct) (superpozycja fal lewych/prawych) |
### Równanie Laplace’a
∇²u = ∂²u/∂x² + ∂²u/∂y² = 0
Rozwiązania (funkcje harmoniczne) reprezentują temperaturę w stanie ustalonym, potencjał elektrostatyczny, nieściśliwy przepływ płynu.
| Nieruchomość | Oświadczenie |
|---------|-----------|
| Właściwość wartości średniej | u(x₀) = średnia u w dowolnym okręgu o środku w x₀ |
| Zasada maksimum | Brak wewnętrznych maksimów i minimów |
| Wyjątkowość | Wyznaczone całkowicie przez warunki brzegowe |
---

## Znaczenie dla uczenia maszynowego i nauki o danych
| Koncepcja DS | Aplikacja |
|---------------|------------|
| ODE | Neuronowe ODE (sieci o ciągłej głębokości), rekurencyjna dynamika sieci |
| Analiza stabilności | Dynamika treningu opadania gradientowego (czy strata maleje stabilnie?) |
| Funkcje Łapunowa | Wykazanie zbieżności algorytmów uczenia się, wzmacnianie stabilności uczenia się |
| Chaos | Zrozumienie wrażliwości RNN (zanikające/eksplodujące gradienty), prognozowanie pogody |
| rozwidlenie | Przejścia fazowe w uczeniu się (grokking), zmiany reżimu w dynamice treningu |
| PDE | Modele dyfuzyjne (modele generatywne oparte na wynikach), sieci neuronowe oparte na fizyce |
| Równanie ciepła | Procesy dyfuzyjne w modelowaniu generatywnym, wykres wygładzania Laplaciana |
| Równanie falowe | Przetwarzanie danych sejsmicznych, modelowanie sygnału audio |
| Lotka-Volterra | Dynamika populacji, epidemiologia, konkurencyjne czynniki ML |
| Portrety fazowe | Wizualizacja dynamiki krajobrazu strat, zrozumienie szkolenia GAN |
---

## Streszczenie
| Temat | Podstawowy pomysł | Kluczowe narzędzie |
|-------|-----------|---------|
| ODE | Funkcje i ich pochodne po czasie | Równania charakterystyczne, czynniki całkujące |
| Systemy ODE | Wiele oddziałujących zmiennych | Analiza wartości własnych Jakobianu |
| Portrety fazowe | Wizualizacja dynamiki w przestrzeni stanów | Punkty stałe, linie zerowe, cykle graniczne |
| Stabilność | Czy system powróci do równowagi? | Linearyzacja, funkcje Lapunowa |
| Chaos | Deterministyczna nieprzewidywalność | Wykładniki Lapunowa, dziwne atraktory |
| rozwidlenia | Zmiany jakościowe z parametrami | Formy normalne, diagramy bifurkacji |
| PDE | Funkcje wielu zmiennych | Równania ciepła, fali i Laplace'a |
Teoria systemów dynamicznych to matematyka zmian. Wyjaśnia, dlaczego niektóre systemy się stabilizują, dlaczego niektóre oscylują i dlaczego niektóre zachowują się chaotycznie. Analitykom danych zapewnia narzędzia do zrozumienia dynamiki uczenia się, projektowania stabilnych algorytmów, modelowania szeregów czasowych i tworzenia nowej generacji modeli uczenia maszynowego opartych na fizyce.