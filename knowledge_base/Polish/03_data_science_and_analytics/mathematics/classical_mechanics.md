<!--
---
# Metadata
title: "Classical Mechanics"
description: "Newton's laws, free-body diagrams, work-energy theorem, conservation laws, Lagrangian mechanics, Hamiltonian mechanics, rigid body dynamics, and orbital mechanics"
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
    changes: "Initial deep-dive into classical mechanics"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2027-02-10"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-10"

# Classification
tags: [classical-mechanics, newton, lagrangian, hamiltonian, conservation-laws, orbital-mechanics, rigid-body]
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
# Mechanika klasyczna
Mechanika klasyczna opisuje ruch obiektów pod wpływem sił. Od spadających jabłek po orbitujące planety, od wibrujących strun po zderzające się cząstki – jego zasady rządzą makroskopowym światem. Oprócz zastosowań fizycznych mechanika klasyczna dała początek rachunku wariacyjnego, geometrii symplektycznej i modelu Hamiltona, który leży u podstaw mechaniki kwantowej i współczesnej optymalizacji.
---

## Mechanika Newtona
### Trzy prawa Newtona
| Prawo | Oświadczenie | Forma matematyczna |
|-----|-----------|--------------------------------|
| **Pierwszy (bezwładność)** | Obiekt pozostaje w spoczynku lub w ruchu jednostajnym, chyba że działa na niego siła | Jeśli F_net = 0, to v = stała |
| **Drugi (F = ma)** | Siła równa się masa razy przyspieszenie | **F** = m**a** = m(d²**x**/dt²) |
| **Trzeci (akcja-reakcja)** | Każda akcja ma równą i przeciwną reakcję | **F**₁₂ = −**F**₂₁ |
### Diagramy swobodnego ciała
**Schemat swobodnego ciała** izoluje obiekt i pokazuje wszystkie działające na niego siły.
**Wspólne siły:**
| Siła | Formuła | Kierunek |
|-------|---------|---------------|
| Grawitacja (blisko Ziemi) | F = mg | W dół |
| Normalna siła | N | Prostopadle do powierzchni |
| Tarcie (statyczne) | f_s ≤ μ_s N | Sprzeciwia się zbliżającemu się ruchowi |
| Tarcie (kinetyczne) | f_k = μ_k N | Sprzeciwia się ruchowi |
| Wiosna (prawo Hooke'a) | F = −kx | Przywrócenie (w kierunku równowagi) |
| Napięcie | T | Wzdłuż sznurka/liny |
| Przeciągnij | F_d = ½C_d ρAv² | Przeciwstawia się prędkości |
### Przykład praktyczny: blok na pochyłości
Blok o masie m leżący na pochyłości bez tarcia pod kątem θ.
- Siły: grawitacja (mg w dół), siła normalna (N prostopadle do powierzchni)
- Rozkład grawitacyjny: mg sin θ (wzdłuż pochyłości), mg cos θ (do powierzchni)
- N = mg cos θ (brak ruchu prostopadłego do powierzchni)
- Przyspieszenie na wzniesieniu: a = g sin θ
---

## Metody energetyczne
### Praca i energia kinetyczna
**Praca** wykonana przez siłę: W = ∫ **F** · d**r**
**Twierdzenie o pracy i energii:** W_net = ΔKE = ½mv₂² − ½mv₁²
### Energia potencjalna
| Siła | Energia potencjalna | Notatki |
|-------|----------------------|------|
| Grawitacja (blisko powierzchni) | U = mg | h = wysokość nad punktem odniesienia |
| Grawitacja (ogólnie) | U = −GMm/r | Zero w nieskończoności |
| Wiosna | U = ½kx² | x = wychylenie z równowagi |
| Elektrostatyczny | U = kq₁q₂/r | Ładunki podobne: dodatnie U |
### Oszczędzanie energii
Jeśli działają tylko siły zachowawcze: E = KE + PE = stała
½mv₁² + U₁ = ½mv₂² + U₂
**Przykład praktyczny:** Piłka upuszczona z wysokości h.
- Wartość początkowa: KE = 0, PE = mgh
- Tuż przed uderzeniem w ziemię: KE = ½mv², PE = 0
- Konserwacja: mgh = ½mv² → v = √(2gh)
### Moc
P = dW/dt = **F** · **v** (szybkość wykonywania pracy)
---

## Pęd i kolizje
### Pęd liniowy
**p** = m**v**
Drugie prawo Newtona (forma alternatywna): **F** = d**p**/dt
### Zasada zachowania pędu
Jeżeli nie ma sił zewnętrznych: całkowity pęd zostaje zachowany.
| Typ kolizji | Zachowane KE? | Pęd zachowany? |
|--------------|-------------------|---------------------------------|
| **Elastyczny** | Tak | Tak |
| **Nieelastyczny** | Nie | Tak |
| **Idealnie nieelastyczny** | Nie (maksymalna strata) | Tak (obiekty sklejają się ze sobą) |
**Zderzenie sprężyste 1D:** Dwie masy m₁, m₂ z prędkościami początkowymi u₁, u₂:
- v₁ = ((m₁−m₂)u₁ + 2m₂u₂) / (m₁+m₂)
- v₂ = ((m₂−m₁)u₂ + 2m₁u₁) / (m₁+m₂)
### Moment pędu
**L** = **r** × **p** = m(**r** × **v**)
Moment obrotowy: **τ** = d**L**/dt = **r** × **F**
**Zachowanie:** Jeśli nie ma zewnętrznego momentu obrotowego, zachowany jest moment pędu.
---

## Mechanika Lagrange'a
Formuła **Lagrangianu** zastępuje siły energią, zapewniając bardziej eleganckie i ogólne ramy.
### Lagrangianu
L = T - V (energia kinetyczna minus energia potencjalna)
### Zasada najmniejszego działania (zasada Hamiltona)
Rzeczywista droga pokonana przez system pomiędzy momentami t₁ i t₂ minimalizuje (a dokładniej sprawia, że ​​jest stacjonarny) **akcja**:
S = ∫_{t₁}^{t₂} L(q, q̇, t) dt
### Równania Eulera-Lagrange’a
Warunek δS = 0 daje:
d/dt(∂L/∂q̇) − ∂L/∂q = 0
dla każdej uogólnionej współrzędnej q.
**Przykład praktyczny:** Wahadło proste (długość l, masa m, kąt θ od pionu).
- T = ½ml²θ̇²
- V = −mgl cos θ
- L = ½ml²θ̇² + mgl cos θ
- ∂L/∂θ = −mgl sin θ
- ∂L/∂θ̇ = ml²θ̇ → d/dt(∂L/∂θ̇) = ml²θ̈
- Euler-Lagrange: ml²θ̈ + mgl sin θ = 0 → θ̈ + (g/l) sin θ = 0
### Zalety mechaniki Lagrange'a
| Zaleta | Wyjaśnienie |
|---------------|------------|
| Niezależne od współrzędnych | Działa w dowolnym układzie współrzędnych |
| Naturalnie radzi sobie z ograniczeniami | Nie ma potrzeby obliczania sił ograniczających |
| Symetria → konserwacja | Twierdzenie Noether łączy symetrie z wielkościami zachowanymi |
| Łatwo generalizuje | Do pól, teorii względności, mechaniki kwantowej |
---

## Mechanika Hamiltona
Formuła **Hamiltonowska** jest przeformułowaniem mechaniki Lagrangianu, która wykorzystuje położenia i pędy (zamiast pozycji i prędkości).
### Hamiltonian
H = Σᵢ pᵢq̇ᵢ - L = T + V (dla większości układów mechanicznych)
gdzie pᵢ = ∂L/∂q̇ᵢ to **uogólnione pędy**.
### Równania Hamiltona
q̇ᵢ = ∂H/∂pᵢ
ṗᵢ = −∂H/∂qᵢ
Są to 2n ODE pierwszego rzędu (w porównaniu z n równaniami Eulera-Lagrange'a drugiego rzędu).
**Przykład praktyczny:** Oscylator harmoniczny (masa m, stała sprężyny k).
- H = p²/(2m) + ½kx²
- ẋ = ∂H/∂p = p/m → p = mẋ (zgodnie z oczekiwaniami)
- ṗ = −∂H/∂x = −kx → mẍ = −kx (prawo Hooke’a)
### Nawiasy Poissona
Dla funkcji f(q, p) i g(q, p):
{f, g} = Σᵢ (∂f/∂qᵢ · ∂g/∂pᵢ − ∂f/∂pᵢ · ∂g/∂qᵢ)
| Nieruchomość | Oświadczenie |
|---------|-----------|
| Ewolucja czasu | df/dt = {f, H} + ∂f/∂t |
| Ochrona | f jest zachowane, jeśli {f, H} = 0 (i ∂f/∂t = 0) |
| Nawiasy podstawowe | {qᵢ, pⱼ} = δᵢⱼ, {qᵢ, qⱼ} = 0, {pᵢ, pⱼ} = 0 |
**Powiązanie z mechaniką kwantową:** Nawiasy Poissona stają się komutatorami: {f, g} → (1/iℏ)[f̂, ĝ]
---

## Prawa zachowania i twierdzenie Noether
### Twierdzenie Noether
Każda ciągła symetria Lagrangianu odpowiada zachowanej wielkości.
| Symetria | Ilość zachowana |
|---------|----------------------|
| Niezmienniczość tłumaczenia czasu | Energia |
| Niezmienniczość translacji przestrzennej | Pęd liniowy |
| Niezmienność rotacyjna | Moment pędu |
| Niezmienniczość miernika | Ładunek elektryczny |
Jest to jeden z najgłębszych wniosków w całej fizyce — łączy geometrię czasoprzestrzeni z podstawowymi prawami zachowania.
---

## Dynamika ciała sztywnego
**Ciało sztywne** to obiekt, w którym wszystkie odległości wewnętrzne pozostają stałe.
### Kluczowe pojęcia
| Koncepcja | Formuła | Opis |
|--------|---------|------------|
| **Moment bezwładności** | I = Σmᵢrᵢ² lub I = ∫r² dm | Odporność na przyspieszenie obrotowe |
| **Obrotowy KE** | KE = ½Iω² | Energia obrotu |
| **Moment pędu** | L = Iω | Obrotowy analog p = mv |
| **Moment obrotowy** | τ = Iα | Obrotowy odpowiednik F = ma |
### Momenty bezwładności (typowe kształty)
| Kształt | Oś | ja |
|-------|------|---|
| Stała kula | Przez środek | (2/5)MR² |
| Pusta kula | Przez środek | (2/3)MR² |
| Solidny cylinder | Wzdłuż osi | (1/2)MR² |
| Cienki pręt | Przez środek, prostopadle | (1/12)ML² |
| Cienki pręt | Przez koniec, prostopadle | (1/3)ML² |
| Dysk | Przez środek, prostopadle | (1/2)MR² |
---

## Mechanika orbitalna
### Prawa Keplera
| Prawo | Oświadczenie |
|-----|-----------|
| **Pierwszy (elipsa)** | Planety poruszają się po elipsach, a Słońce jest w jednym z ognisk |
| **Drugi (Równe obszary)** | Linia łącząca Słońce z planetą przecina równe obszary w równych czasach |
| **Trzecia (harmoniczna)** | T² ∝ a³ (okres do kwadratu proporcjonalny do półosi wielkiej do sześcianu) |
### Energia orbitalna
E = ½mv² – GMm/obr
| E | Typ orbity |
|---|-----------|
| E< 0 | Elliptical (bound) |
| E = 0 | Parabolic (escape trajectory) |
| E >0 | Hiperboliczny (bez ograniczeń) |
### Prędkość ucieczki
v_escape = √(2GM/R)
Dla Ziemi: v_escape ≈ 11,2 km/s
---

## Znaczenie dla uczenia maszynowego i nauki o danych
| Koncepcja mechaniki | Aplikacja |
|--------------------------------|------------|
| Prawa Newtona | Silniki fizyczne w symulacjach, gra AI, robotyka |
| Metody energetyczne | Modele energetyczne, sieci Hopfielda, maszyny Boltzmanna |
| Mechanika Lagrange'a | Sieci neuronowe oparte na fizyce, sterowanie optymalne, optymalizacja trajektorii |
| Mechanika Hamiltona | Hamiltonowskie sieci neuronowe (HNN), integratory symplektyczne do symulacji |
| Prawa ochronne | Odchylenia indukcyjne w modelach ML, ekwiwariantne sieci neuronowe |
| Twierdzenie Noether | Uczenie maszynowe uwzględniające symetrię, głębokie uczenie geometryczne |
| Dynamika ciała sztywnego | Symulacja robotyki, dynamika molekularna, animacja 3D |
| Mechanika orbitalna | Pozycjonowanie satelitarne (GPS dla ML opartego na lokalizacji), projektowanie misji kosmicznych |
| Przestrzeń fazowa (Hamiltonowska) | Zrozumienie układów dynamicznych, sieci atraktorów |
| Rachunek wariacyjny | Transport optymalny, modelowanie generatywne (dopasowanie przepływu) |
---

## Streszczenie
| Ramy | Równanie podstawowe | siła |
|----------|-------------|---------|
| Newtona | **F** = m**a** | Intuicyjna, bezpośrednia analiza siły |
| Lagrangianu | d/dt(∂L/∂q̇) − ∂L/∂q = 0 | Bez współrzędnych, obsługuje wiązania |
| Hamiltonian | q̇ = ∂H/∂p, ṗ = −∂H/∂q | Struktura symplektyczna, łączy się z QM |
| Prawa ochronne | Twierdzenie Noether | Głębokie połączenie z zachowaniem symetrii |
Mechanika klasyczna to nie tylko spadające kule i wahadła. Jej ramy matematyczne — mechanika Lagrangianu i Hamiltona — należą do najbardziej wpływowych idei w całej nauce. Dokonują uogólnień na mechanikę kwantową, teorię pola, a nawet współczesne uczenie maszynowe, w przypadku których modele oparte na energii i sieci neuronowe oparte na fizyce czerpią bezpośrednio z tych wielowiekowych sformułowań.