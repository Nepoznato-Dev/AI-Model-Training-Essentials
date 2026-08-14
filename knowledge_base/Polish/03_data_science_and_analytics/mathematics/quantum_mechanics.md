<!--
---
# Metadata
title: "Quantum Mechanics"
description: "Wave-particle duality, Schrodinger equation, operators and observables, uncertainty principle, quantum states and superposition, entanglement, qubits, quantum gates, and relevance to quantum computing"
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
    changes: "Initial deep-dive into quantum mechanics"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2027-02-10"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-10"

# Classification
tags: [quantum-mechanics, schrodinger-equation, uncertainty-principle, superposition, entanglement, qubits, quantum-gates, quantum-computing]
difficulty_level: "advanced"
prerequisites:
  - "mathematics.md"
  - "abstract_algebra.md"
  - "classical_mechanics.md"
estimated_reading_time: "28 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Mechanika kwantowa
Mechanika kwantowa to teoria fizyki w najmniejszych skalach — atomów, elektronów, fotonów i podstawowych cząstek natury. Zastępuje deterministyczny świat mechaniki klasycznej prawdopodobieństwami, superpozycjami i splątaniem. Pomimo swojej sprzecznej z intuicją natury, mechanika kwantowa jest najdokładniej przetestowaną teorią w całej nauce. Obecnie jego zasady mają bezpośrednie zastosowanie w obliczeniach realizowanych za pomocą komputerów kwantowych, które obiecują rozwiązywać pewne problemy wykładniczo szybciej niż klasyczne maszyny.
---

## Motywacja historyczna
### Błędy fizyki klasycznej
| Problem | Przewidywanie klasyczne | Obserwacja | Rozdzielczość |
|--------|---------------------|------------|------------|
| Promieniowanie ciała doskonale czarnego | Katastrofa ultrafioletowa (nieskończona energia przy krótkim λ) | Skończona długość fali szczytowej | Planck: energia jest skwantowana (E = nhν) |
| Efekt fotoelektryczny | KE zależy od intensywności, a nie częstotliwości | KE zależy od częstotliwości | Einstein: światło jest kwantowane (fotony, E = hν) |
| Widma atomowe | Ciągłe widmo emisji | Dyskretne linie widmowe | Bohr: elektrony zajmują skwantowane orbity |
| Dyfrakcja elektronów | Cząstki nie dyfragują | Elektrony wytwarzają wzory interferencyjne | de Broglie: cząstki mają długość fali λ = h/p |
### Kluczowe stałe
| Stała | Symbol | Wartość |
|---------|--------|-------|
| Stała Plancka | h | 6,626 × 10⁻³⁴ J·s |
| Zredukowana stała Plancka | ℏ = godz./2π | 1,055 × 10⁻³⁴ J·s |
| Prędkość światła | c | 3,0 × 10⁸ m/s |
| Masa elektronu | m_e | 9,109 × 10⁻³¹ kg |
| Opłata podstawowa | e | 1,602 × 10⁻¹⁹ C |
| Promień Bohra | a₀ | 5,292 × 10⁻¹¹ m |
---

## Dualizm falowo-cząsteczkowy
### Długość fali Broglie’a
Każda cząstka o pędzie p ma przypisaną długość fali:
λ = h/p = h/(mv)
| Cząstka | Typowy λ | Obserwowalne zachowanie fal? |
|---------|-----------|----------------|
| Elektron (100 eV) | 0,12 nm | Tak (dyfrakcja kryształu) |
| Proton | 0,003 nm | Tak (rozpraszanie neutronów) |
| Baseball (40 m/s) | 10⁻³⁴m | Nie (zdecydowanie zbyt mały, aby wykryć) |
### Eksperyment z podwójną szczeliną
Kwintesencja eksperymentu kwantowego:
1. Wystrzeliwuj cząstki (elektrony, fotony) pojedynczo w dwie szczeliny
2. Każda cząstka ląduje w jednym punkcie detektora
3. Z biegiem czasu pojawia się wzór interferencyjny — tak jakby każda cząstka przeszła jednocześnie przez obie szczeliny
4. Jeśli zmierzysz, przez którą szczelinę przechodzi cząstka, wzór interferencyjny znika
**Wniosek:** Obiekty kwantowe nie są ani cząstkami, ani falami. Kiedy nie są obserwowane, zachowują się jak fale, a podczas pomiaru zachowują się jak cząstki.
---

## Funkcja falowa
### Definicja
**Funkcja falowa** ψ(x, t) całkowicie opisuje układ kwantowy. Jest to funkcja o wartościach zespolonych, której kwadratowy moduł daje gęstość prawdopodobieństwa:
P(x) = |ψ(x)|² = ψ*(x)ψ(x)
### Normalizacja
Całkowite prawdopodobieństwo musi wynosić 1:
∫ |ψ(x)|² dx = 1 (w całej przestrzeni)
### Urodzona zasada
Prawdopodobieństwo znalezienia cząstki pomiędzy x a x + dx:
P(x do x+dx) = |ψ(x)|² dx
Dla ogólnej obserwowalności ze stanami własnymi φₙ:
P(pomiar wartości własnej aₙ) = |⟨φₙ|ψ⟩|²
---

## Równanie Schrodingera
### Równanie Schrodingera zależne od czasu
iℏ ∂ψ/∂t = Ĥψ
gdzie Ĥ jest **operatorem Hamiltona** (operatorem energii całkowitej).
### Niezależne od czasu równanie Schrodingera
Dla stanów stacjonarnych (stany własne energii):
Ĥψ = Eψ
Jest to równanie wartości własnej: dozwolone energie E są wartościami własnymi Ĥ.
### Cząstka w pudełku (nieskończona studnia kwadratowa)
Najprostszy układ kwantowy: cząstka ograniczona do 0 < x < L.
| Ilość | Wynik |
|---------|--------|
| Funkcje falowe | ψₙ(x) = √(2/L) sin(nπx/L) |
| Poziomy energii | Eₙ = n²π²ℏ²/(2mL²) = n²h²/(8mL²) |
| Stan podstawowy | n = 1, E₁ = h²/(8mL²) |
| Energia punktu zerowego | E₁ > 0 (cząstka nie może być idealnie nieruchoma) |
| Liczba kwantowa | n = 1, 2, 3, ... (tylko dodatnie liczby całkowite) |
### Kwantowy oscylator harmoniczny
V(x) = ½mω²x²
| Ilość | Wynik |
|---------|--------|
| Poziomy energii | Eₙ = (n + ½)ℏω |
| Energia punktu zerowego | E₀ = ½ℏω |
| Odstępy | ΔE = ℏω (jednolite) |
| Funkcje falowe | Wielomiany Hermite’a × Gaussa |
---

## Operatory i obserwacje
W mechanice kwantowej każda fizyczna obserwowalność odpowiada **operatorowi hermitowskiemu**.
### Kluczowi operatorzy
| obserwowalne | Operator (przestrzeń pozycji) | Wartości własne |
|----------|--------------------------|------------|
| Pozycja | x̂ = x | Wszystko prawdziwe x |
| Pęd | p̂ = −iℏ ∂/∂x | Wszystko prawdziwe p |
| Energia (Hamiltonowska) | Ĥ = −(ℏ²/2m)∂²/∂x² + V(x) | Eₙ (dyskretny dla stanów związanych) |
| Moment pędu | L̂ = r × p̂ | ℏ√(l(l+1)) |
| Zakręć | Ŝ = (ℏ/2)σ (macierze Pauliego) | ±ℏ/2 (dla spinu-½) |
### Wartości oczekiwane
Średni wynik pomiaru obserwowalnego A w stanie ψ:
⟨A⟩ = ⟨ψ|Â|ψ⟩ = ∫ ψ*(x) Â ψ(x) dx
### Relacje komutacyjne
[Â, B̂] = ÂB̂ - B̂Â
| Komutator | Wynik | Znaczenie |
|---------------|--------|------------|
| [x̂, p̂] | jaℏ | Położenie i pęd są niezgodne |
| [L̂ₓ, L̂ᵧ] | iℏL̂_z | Składniki momentu pędu są niezgodne |
| [σ̂ₓ, σ̂ᵧ] | 2iσ̂_z | Macierze Pauliego (składowe spinowe) |
Jeśli [Â, B̂] = 0, obserwable można mierzyć jednocześnie (współdzielone stany własne).
---

## Zasada nieoznaczoności
### Zasada nieoznaczoności Heisenberga
Δx · Δp ≥ ℏ/2
Mówiąc bardziej ogólnie, dla dowolnych dwóch obserwowalnych A i B:
ΔA · ΔB ≥ (1/2)|⟨[Â, B̂]⟩|
### Relacje niepewności
| Para | Relacja | Interpretacja |
|------|----------|----------------|
| Pozycja-pęd | ΔxΔp ≥ ℏ/2 | Nie mogę znać obu dokładnie |
| Czas energii | ΔEΔt ≥ ℏ/2 | Stany krótkotrwałe mają niepewną energię |
| Moment pędu | ΔLₓΔLᵧ ≥ (ℏ/2)\|⟨L_z⟩\| | Nie można znać wszystkich komponentów jednocześnie |
**Ważne:** Niepewność nie dotyczy zakłóceń pomiaru — jest podstawową właściwością stanów kwantowych. Cząstka nie ma jednocześnie określonego położenia i pędu.
---

## Stany kwantowe i superpozycja
### Notacja Diraca (bra-ket)
| Symbol | Imię | Znaczenie |
|------------|------|--------|
| \|ψ⟩ | Ket | Wektor stanu (wektor kolumnowy) |
| ⟨ψ\| | Biustonosz | Transpozycja koniugatu (wektor wierszowy) |
| ⟨φ\|ψ⟩ | Produkt wewnętrzny | Amplituda dla ψ w stanie φ |
| \|ψ\|² | Norma do kwadratu | Prawdopodobieństwo |
### Zasada superpozycji
Jeśli \|ψ₁⟩ i \|ψ₂⟩ są poprawnymi stanami kwantowymi, to obowiązuje również dowolna kombinacja liniowa:
\|ψ⟩ = α\|ψ₁⟩ + β\|ψ₂⟩

gdzie |α|² + |β|² = 1 (normalizacja).
**Pomiar:** Podczas pomiaru system „zapada się” do \|ψ₁⟩ z prawdopodobieństwem |α|² lub \|ψ₂⟩ z prawdopodobieństwem |β|².
### Kubity
**Kubit** to bit kwantowy: dwupoziomowy układ kwantowy.
\|ψ⟩ = α\|0⟩ + β\|1⟩, gdzie |α|² + |β|² = 1
| Reprezentacja | \|0⟩ | \|1⟩ |
|--------------|------|------|
| Zakręć | Rozkręć ↑ | Obróć się ↓ |
| Polaryzacja fotonów | Poziome | Pionowe |
| Poziom energii | Stan podstawowy | Stan podekscytowania |
| Obwód | \|0⟩ = [1, 0]ᵀ | \|1⟩ = [0, 1]ᵀ |
**Sfera Blocha:** Dowolny stan kubitu można zapisać jako:
\|ψ⟩ = cos(θ/2)\|0⟩ + e^{iφ} grzech(θ/2)\|1⟩
gdzie θ ∈ [0, π] i φ ∈ [0, 2π). Przestrzeń stanów jest kulą.
---

## Uwikłanie
Dwa kubity są **splątane**, gdy ich wspólnego stanu nie można zapisać jako iloczynu poszczególnych stanów.
### Stany Bella (maksymalnie splątane)
| stan | Wyrażenie | Imię |
|-------|-----------|------|
| \|Φ⁺⟩ | (1/√2)(\|00⟩ + \|11⟩) | Stan dzwonka |
| \|Φ⁻⟩ | (1/√2)(\|00⟩ − \|11⟩) | Stan dzwonka |
| \|Ψ⁺⟩ | (1/√2)(\|01⟩ + \|10⟩) | Stan dzwonka |
| \|Ψ⁻⟩ | (1/√2)(\|01⟩ − \|10⟩) | Stan singletu |
### Właściwości splątania
| Nieruchomość | Opis |
|---------|------------|
| Korelacja | Pomiar jednego kubitu natychmiast określa drugi, niezależnie od odległości |
| Brak komunikacji | Nie można używać samego splątania do przesyłania informacji szybciej niż światło |
| Monogamia | Jeżeli A jest maksymalnie splątane z B, to nie może być splątane z C |
| Kruchość | Interakcja z otoczeniem niszczy splątanie (dekoherencję) |
### Paradoks EPR i twierdzenie Bella
Einstein, Podolski i Rosen argumentowali, że mechanika kwantowa musi być niekompletna (zmienne ukryte). Bell pokazał, że każda teoria lokalnych zmiennych ukrytych spełnia pewne nierówności. Eksperymenty naruszają nierówności Bella — potwierdzając mechanikę kwantową i wykluczając lokalne zmienne ukryte.
---

## Bramy kwantowe
Bramy kwantowe to operacje unitarne na kubitach.
### Bramy jednokubitowe
| Brama | Matryca | Efekt |
|------|------------|-------|
| **Pauli-X** (NIE) | [[0,1], [1,0]] | Odwrócenie bitu: \|0⟩ ↔ \|1⟩ |
| **Pauli-Y** | [[0,−i],[i,0]] | Bit + odwrócenie fazy |
| **Pauli-Z** | [[1,0],[0,−1]] | Odwrócenie fazy: \|1⟩ → −\|1⟩ |
| **Hadamard** (H) | (1/√2)[[1,1],[1,−1]] | Tworzy superpozycję: \|0⟩ → (\|0⟩+\|1⟩)/√2 |
| **Faza** (S) | [[1,0],[0,i]] | obrót π/2 wokół Z |
| **brama T** | [[1,0],[0,e^{iπ/4}]] | obrót π/4 wokół Z |
| **Obrót** Rₓ(θ) | cos(θ/2)I – i sin(θ/2)σₓ | Obrót o θ wokół osi X |
### Bramy dwukubitowe
| Brama | Opis | Efekt |
|------|------------|-------|
| **NIE** | Kontrolowane-NIE | Odwraca cel, jeśli kontrola wynosi \|1⟩ |
| **CZ** | Kontrolowane-Z | Stosuje Z do celu, jeśli kontrola wynosi \|1⟩ |
| **ZMIANA** | Wymiana kubitów | \|ab⟩ → \|ba⟩ |
### Tworzenie splątania
Zastosuj H do kubitu 1, a następnie CNOT z kubitem 1 jako kontrolą:
\|00⟩ → (H⊗I)\|00⟩ → CNOT → (1/√2)(\|00⟩ + \|11⟩) = \|Φ⁺⟩
---

## Algorytmy kwantowe
| Algorytm | Przyspieszenie | Aplikacja |
|----------|---------|------------|
| **Shor** | Wykładniczy (faktoring) | Łamie szyfrowanie RSA |
| **Grovera** | Kwadratowy (szukaj) | Wyszukiwanie niestrukturalne w O(√N) |
| **VQE** | Heurystyka | Znajdowanie energii stanu podstawowego (chemia, materiały) |
| **QAOA** | Heurystyka | Optymalizacja kombinatoryczna |
| **HHL** | Wykładniczy (w warunkach) | Rozwiązywanie układów liniowych |
| **Symulacja kwantowa** | wykładniczy | Symulowanie układów kwantowych (oryginalna motywacja Feynmana) |
---

## Znaczenie dla uczenia maszynowego i nauki o danych
| Koncepcja kwantowa | Aplikacja |
|----------------|------------|
| Kubity i superpozycja | Kwantowe uczenie maszynowe, próbkowanie wzmocnione kwantowo |
| Splątanie | Komunikacja kwantowa, kwantowa dystrybucja klucza (QKD) |
| Bramy kwantowe | Projekt obwodu kwantowego dla podprogramów ML |
| Algorytm Grovera | Przyspieszenie kwadratowe dla optymalizacji opartej na wyszukiwaniu |
| Algorytm Shora | Zagrożenie dla współczesnej kryptografii; motywuje kryptowalutę postkwantową |
| Symulacja kwantowa | Odkrywanie leków, inżynieria materiałowa, symulacja chemii |
| Algorytmy wariacyjne (VQE, QAOA) | Krótkoterminowe kwantowe ML na urządzeniach NISQ |
| Urodzona zasada | Wyniki probabilistyczne analogiczne do próbkowania z rozkładów |
| Produkty Tensora | Systemy wielokubitowe (wykładnicza przestrzeń stanów — taka sama matematyka jak algebra wieloliniowa w ML) |
| Macierze unitarne | Kwantowe analogi przekształceń ortogonalnych |
---

## Streszczenie
| Koncepcja | Podstawowy pomysł | Kluczowe równanie |
|--------|-----------|------------|
| Dualizm korpuskularno-falowy | Materia ma właściwości falowe | λ = h/p |
| Funkcja falowa | Pełny opis stanu kwantowego | P(x) = \|ψ(x)\|² |
| Równanie Schrodingera | Jak ewoluują stany kwantowe | iℏ ∂ψ/∂t = Ĥψ |
| Operatorzy | Obserwowalne są operatorami hermitowskimi | ⟨A⟩ = ⟨ψ\|Â\|ψ⟩ |
| Niepewność | Podstawowe ograniczenia wiedzy jednoczesnej | ΔxΔp ≥ ℏ/2 |
| Superpozycja | Można dodawać stany | \|ψ⟩ = α\|0⟩ + β\|1⟩ |
| Splątanie | Nierozłączne stany wspólne | \|Φ⁺⟩ = (\|00⟩ + \|11⟩)/√2 |
| Bramy kwantowe | Operacje jednostkowe na kubitach | H, CNOT i zestawy bramek uniwersalnych |
Mechanika kwantowa kwestionuje nasze najgłębsze intuicje dotyczące rzeczywistości – cząstek będących falami, obiektów w dwóch miejscach jednocześnie, korelacji wymykających się klasycznym wyjaśnieniom. Jednak jego matematyka jest precyzyjna, a przewidywania niezrównane pod względem dokładności. Dla badaczy danych mechanika kwantowa staje się bezpośrednio istotna dzięki informatyce kwantowej, która może zmienić optymalizację, kryptografię, symulację i potencjalnie samo uczenie maszynowe.