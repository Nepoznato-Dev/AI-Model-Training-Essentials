<!--
---
# Metadata
title: "Thermodynamics and Statistical Mechanics"
description: "Laws of thermodynamics, entropy (thermodynamic and statistical), enthalpy, free energy, Carnot cycle, Boltzmann distribution, partition functions, and connections to information-theoretic entropy"
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
    changes: "Initial deep-dive into thermodynamics and statistical mechanics"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2027-02-10"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-10"

# Classification
tags: [thermodynamics, statistical-mechanics, entropy, enthalpy, free-energy, carnot-cycle, boltzmann, partition-function]
difficulty_level: "advanced"
prerequisites:
  - "mathematics.md"
  - "statistics_and_probability.md"
  - "classical_mechanics.md"
estimated_reading_time: "25 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Termodynamika i mechanika statystyczna
Termodynamika opisuje makroskopowe zachowanie układów pod względem temperatury, ciśnienia i entropii – nie wiedząc, jak wyglądają atomy. Mechanika statystyczna wyjaśnia termodynamikę od dołu do góry: wyprowadza właściwości makroskopowe z mikroskopijnego zachowania ogromnej liczby cząstek. Razem zapewniają najgłębsze zrozumienie energii, entropii i równowagi – pojęć, które przeniosły się do teorii informacji, uczenia maszynowego i nie tylko.
---

## Zmienne termodynamiczne i stan
### Zmienne stanu
| Zmienna | Wpisz | Jednostka | Opis |
|---------|------|------|------------|
| Temperatura (T) | Intensywny | Kelwin (K) | Średnia energia kinetyczna na cząstkę |
| Ciśnienie (P) | Intensywny | Pascal (Pa) | Siła na jednostkę powierzchni |
| Objętość (V) | Obszerne | m³ | Miejsce zajęte |
| Energia wewnętrzna (U) | Obszerne | Dżul (J) | Całkowita energia mikroskopijna |
| Entropia (S) | Obszerne | J/K | Miara nieporządku/mikrostanów |
| Liczba cząstek (N) | Obszerne | mole lub liczba | Ilość substancji |
**Intensywne** zmienne nie zależą od rozmiaru systemu; **rozbudowane** zmienne tak.
### Równanie stanu
Dla gazu doskonałego: PV = nRT = Nk_BT
| Stała | Wartość |
|---------|-------|
| R (stała gazowa) | 8,314 J/(mol·K) |
| k_B (stała Boltzmanna) | 1,381 × 10⁻²³ J/K |
| N_A (liczba Avogadra) | 6,022 × 10²³ /mol |
---

## Prawa termodynamiki
### Prawo Zerotha
Jeśli A jest w równowadze termicznej z B, a B z C, to A jest w równowadze termicznej z C.
**Znaczenie:** temperatura jest dobrze określona i możliwa do zmierzenia.
### Pierwsze prawo (oszczędzanie energii)
ΔU = Q - W
| Symbol | Znaczenie |
|------------|--------|
| ΔU | Zmiana energii wewnętrznej |
| P | Ciepło dodane do systemu |
| W | Praca wykonana przez system |
**Postać różniczkowa:** dU = δQ – δW = δQ – PdV
| Proces | Ograniczenie | Konsekwencja |
|--------|-----------|------------|
| Izochoryczny | dV = 0 | W = 0, ΔU = Q |
| Izobaryczny | dP = 0 | W = PΔV |
| Izotermiczny | dT = 0 | ΔU = 0 (gaz doskonały), Q = W |
| Adiabatyczny | δQ = 0 | ΔU = −W |
### Drugie prawo (entropia)
**Stwierdzenie Clausiusa:** Ciepło nie może samoistnie przepływać z zimna do gorąca.
**Stwierdzenie Kelvina-Plancka:** Żaden silnik nie jest w stanie zamienić całego ciepła w pracę.
**Stwierdzenie entropii:** Dla dowolnego procesu: ΔS_universe ≥ 0
| Typ procesu | ΔS_wszechświat |
|------------|------------|
| Odwracalne | = 0 |
| Nieodwracalne (prawdziwe) | > 0 |
**Zmiana entropii:** dS = δQ_rev / T
### Trzecie prawo
Gdy T → 0 K, entropia doskonałego kryształu zbliża się do zera: lim_{T → 0} S = 0
**Znaczenie:** Zero absolutne jest nieosiągalne w skończonych krokach.
---

## Entropia w głębi
### Entropia termodynamiczna
S jest funkcją stanu. Dla procesu odwracalnego pomiędzy stanami A i B:
ΔS = ∫_A^B δQ_rev / T
**Przykład praktyczny:** Zmiana entropii podczas podgrzewania wody od T₁ do T₂ przy stałym ciśnieniu.
ΔS = ∫_{T₁}^{T₂} (mc_p/T) dT = mc_p ln(T₂/T₁)
### Entropia statystyczna (Boltzmann)
S = k_B ln Ω
gdzie Ω jest liczbą mikrostanów zgodnych z makrostanem.
| Makrostan | Mikrostany (Ω) | Entropia |
|----------|--------------------------------|--------|
| Cały gaz w połowie pudełka | Mały | Niski |
| Gaz równomiernie rozprowadzony | Bardzo duży | Wysoki |
| Idealny kryształ w temperaturze 0 K | 1 | 0 |
**Powiązanie:** Drugie prawo staje się statystyczne — systemy ewoluują w kierunku makrostanów z większą liczbą mikrostanów po prostu dlatego, że są one zdecydowanie bardziej prawdopodobne.
---

## Entalpia i darmowa energia
### Entalpia
H = U + PV
Przydatny w procesach pod stałym ciśnieniem (większość chemii i biologii).
ΔH = Q_p (ciepło przy stałym ciśnieniu)
### Darmowa energia Helmholtza
F = U - TS
| Nieruchomość | Oświadczenie |
|---------|-----------|
| Znaczenie | Maksymalna praca możliwa do uzyskania przy stałej T, V |
| Równowaga | System minimalizuje F przy stałym T, V |
| Związek z funkcją podziału | F = −k_BT ln Z |
### Darmowa energia Gibbsa
G = H. – TS = U + PV – TS
| Nieruchomość | Oświadczenie |
|---------|-----------|
| Znaczenie | Maksymalna praca bez rozszerzania przy stałej T, P |
| Równowaga | System minimalizuje G przy stałej T, P |
| Spontaniczność | ΔG < 0 → spontaniczne; ΔG = 0 → równowaga |
| Reakcje chemiczne | ΔG = ΔH – TΔS określa kierunek |
### Podsumowanie potencjałów termodynamicznych
| Potencjał | Zmienne naturalne | Mechanizm różnicowy | Zminimalizowane, gdy |
|----------|----------------------|------------|----------------|
| U (energia wewnętrzna) | S, V | dU = TdS – PdV | Izolowany system |
| H (entalpia) | S, P | dH = TdS + VdP | Stała P, adiabatyczna |
| F (Helmholtz) | T, V | dF = −SdT − PdV | Stała T, V |
| G (Gibbs) | T, P | dG = −SdT + VdP | Stała T, P |
---

## Cykl Carnota
**Cykl Carnota** jest najbardziej wydajnym możliwym silnikiem cieplnym, działającym w zakresie temperatur T_H (gorąco) i T_C (zimno).
### Cztery etapy
| Scena | Proces | Co się dzieje |
|-------|---------|------------|
| 1 → 2 | Rozszerzalność izotermiczna | Pochłaniaj ciepło Q_H z gorącego zbiornika w T_H |
| 2 → 3 | Ekspansja adiabatyczna | Gaz schładza się od T_H do T_C |
| 3 → 4 | Kompresja izotermiczna | Odrzuć ciepło Q_C do zimnego zbiornika w T_C |
| 4 → 1 | Sprężanie adiabatyczne | Gaz nagrzewa się od T_C do T_H |
### Wydajność Carnota
η_Carnot = 1 − T_C/T_H
| T_H | T_C | η_Carnota |
|-----|-----|-----|
| 500 tys. | 300 tys. | 40% |
| 1000 K | 300 tys. | 70% |
| 300 tys. | 299 tys. | 0,33% |
**Żaden prawdziwy silnik nie może przekroczyć wydajności Carnota.** Prawdziwe silniki są zawsze nieodwracalne (tarcie, turbulencje, skończone różnice temperatur).
---

## Mechanika statystyczna
### Dystrybucja Boltzmanna
Dla układu będącego w równowadze termicznej w temperaturze T prawdopodobieństwo znalezienia się w mikrostanie o energii E_i:
P(E_i) = (1/Z) e^{−E_i / k_BT}
gdzie Z jest **funkcją podziału**:
Z = Σᵢ e^{−E_i / k_BT}
### Funkcja partycji
Z koduje wszystkie informacje termodynamiczne o systemie.
| Ilość | Formuła |
|--------------|--------|
| Darmowa energia Helmholtza | F = −k_BT ln Z |
| Średnia energia | ⟨E⟩ = −∂(ln Z)/∂β gdzie β = 1/(k_BT) |
| Entropia | S = k_B(ln Z + β⟨E⟩) |
| Pojemność cieplna | C_V = ∂⟨E⟩/∂T = k_Bβ²(⟨E²⟩ − ⟨E⟩²) |
| Ciśnienie | P = (1/β) ∂(ln Z)/∂V |
### Przykład praktyczny: system dwustanowy
Cząstka może znajdować się w stanie 0 (energia 0) lub stanie 1 (energia ε).
Z = 1 + e^{−βε}
| Ilość | Wynik |
|---------|--------|
| P(stan 0) | 1/(1 + e^{−βε}) |
| P(stan 1) | e^{−βε}/(1 + e^{−βε}) |
| ⟨E⟩ | ε/(1 + e^{βε}) |
| Górna granica T (β → 0) | ⟨E⟩ → ε/2 (równe prawdopodobieństwo) |
| Dolna granica T (β → ∞) | ⟨E⟩ → 0 (stan podstawowy) |
### Twierdzenie o równoważnym podziale
Każdy kwadratowy stopień swobody wnosi ½k_BT do średniej energii.
| Systemu | Stopnie swobody | ⟨E⟩ |
|--------|----------------------|------|
| Gaz jednoatomowy (He) | 3 tłumaczenie | (3/2)k_BT |
| Gaz dwuatomowy (N₂) w pomieszczeniu T | 3 trans + 2 zgnilizna | (5/2)k_BT |
| Gaz dwuatomowy przy wysokim T | 3 trans + 2 rot + 1 wibracja | (7/2)k_BT |
| Stałe (model Einsteina) | 3 wibracyjne (na atom) | 3k_BT |
---

## Połączenie z teorią informacji
### Entropia Shannona a entropia termodynamiczna
| Aspekt | Entropia Shannona H(X) | Entropia termodynamiczna S |
|--------|---------------------|----------------------------|
| Definicja | −Σ pᵢ log pᵢ | k_B ln Ω (lub −k_B Σ pᵢ ln pᵢ) |
| Maksimum, gdy | Równomierny rozkład | Równowaga termiczna |
| Środki | Niepewność / treść informacyjna | Liczba dostępnych mikrostanów |
| Jednostki | Bity lub NAT | J/K |
**Wzór na entropię Gibbsa:** S = −k_B Σᵢ pᵢ ln pᵢ (identyczny w formie z entropią Shannona)
### Zasada maksymalnej entropii
Obie dziedziny korzystają z tej samej zasady: rozkład, który najlepiej reprezentuje nasz stan wiedzy, to ten, który maksymalizuje entropię z zastrzeżeniem znanych ograniczeń.
| Ograniczenie | Wynikowy rozkład |
|--------------|----------------------|
| Znana średnia | Rozkład wykładniczy |
| Znana średnia i wariancja | Rozkład Gaussa |
| Znana energia ⟨E⟩ | Rozkład Boltzmanna |
| Żadnych ograniczeń | Równomierny rozkład |
### Zasada Landauera
Usunięcie jednego bitu informacji powoduje rozproszenie co najmniej k_BT ln 2 energii w postaci ciepła. Łączy to przetwarzanie informacji bezpośrednio z termodynamiką — obliczenia wiążą się z podstawowym kosztem energii.
---

## Znaczenie dla uczenia maszynowego i nauki o danych
| Koncepcja Thermo/StatMech | Aplikacja |
|------------------------|------------|
| Rozkład Boltzmanna | Funkcja Softmax, modele energetyczne, symulowane wyżarzanie |
| Funkcja podziału | Stała normalizująca w modelach probabilistycznych, ogólnie trudna do rozwiązania |
| Darmowa energia | Wnioskowanie wariacyjne (minimalizacja wariacyjnej energii swobodnej = minimalizacja rozbieżności KL) |
| Entropia | Regularyzacja, eksploracja w RL (entropia maksymalna RL), drzewa decyzyjne |
| Zasada maksymalnej entropii | Klasyfikatory MaxEnt, selekcja wstępna, estymacja rozkładu |
| Symulowane wyżarzanie | Globalna optymalizacja poprzez stopniowe obniżanie „temperatury” |
| Mechanika statystyczna | Zrozumienie przejść fazowych w uczeniu się (grokking, podwójne opadanie) |
| Równipodział | Zrozumienie rozkładu energii w symulacjach fizycznych |
| Zasada Landauera | Podstawowe ograniczenia obliczeń, obliczenia odwracalne |
| Próbkowanie Gibbsa | Metoda MCMC bezpośrednio inspirowana mechaniką statystyczną |
| Temperatura (w softmax) | Kontroluje losowość przewidywań: P(i) ∝ exp(z_i/T) |
---

## Streszczenie
| Prawo/koncepcja | Podstawowy pomysł | Formuła |
|------------|-----------|--------|
| Prawo Zerotha | Temperatura jest dobrze określona | Przechodniość równowagi termicznej |
| Pierwsze prawo | Energia jest oszczędzana | ΔU = Q - W |
| Drugie prawo | Entropia wszechświata wzrasta | ΔS ≥ 0 |
| Trzecie prawo | Zero absolutne jest nieosiągalne | S → 0 jako T → 0 |
| Entropia Boltzmanna | Entropia liczy mikrostany | S = k_B ln Ω |
| Rozkład Boltzmanna | Prawdopodobieństwo stanów energetycznych | P ∝ e^{−E/k_BT} |
| Funkcja podziału | Koduje całą informację termodynamiczną | Z = Σ e^{−E_i/k_BT} |
| Darmowa energia | Dostępna przydatna praca | F = U - TS, G = H - TS |
| Efektywność Carnota | Maksymalna wydajność silnika cieplnego | η = 1 − T_C/T_H |
Termodynamika i mechanika statystyczna to obszary, w których fizyka spotyka się z teorią informacji. Ta sama entropia, która rządzi silnikami cieplnymi, reguluje kompresję danych. Ten sam rozkład Boltzmanna, który opisuje cząsteczki gazu, zasila warstwę softmax w każdym klasyfikatorze. Zrozumienie tych powiązań zapewnia ujednolicony obraz fizyki, prawdopodobieństwa i uczenia maszynowego.