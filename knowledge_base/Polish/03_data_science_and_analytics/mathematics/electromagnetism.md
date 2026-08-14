---
# Metadata
title: "Electromagnetism"
description: "Electric and magnetic fields, Coulomb's law, Gauss's law, Faraday's law, Ampere's law, Maxwell's equations, electromagnetic waves, and RLC circuits"
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
    changes: "Initial deep-dive into electromagnetism"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2027-02-10"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-10"

# Classification
tags: [electromagnetism, maxwell-equations, electric-fields, magnetic-fields, electromagnetic-waves, circuits, gauss-law, faraday]
difficulty_level: "advanced"
prerequisites:
  - "mathematics.md"
  - "classical_mechanics.md"
  - "real_analysis.md"
estimated_reading_time: "25 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# Elektromagnetyzm
Elektromagnetyzm to nauka o polach elektrycznych i magnetycznych oraz ich interakcjach. Ujednolicony przez Maxwella w latach sześćdziesiątych XIX wieku elektromagnetyzm wyjaśnia światło, elektryczność, magnetyzm, fale radiowe i strukturę atomów. Była to pierwsza fundamentalna siła w pełni poznana matematycznie, a jej równania zainspirowały Einsteina do szczególnej teorii względności i współczesnej teorii pola.
---

## Pola elektryczne
### Prawo Coulomba
Siła między dwoma ładunkami punktowymi q₁ i q₂ oddzielonymi odległością r:
**F** = (1/4πε₀) · (q₁q₂/r²) · r̂
| Stała | Wartość |
|---------|-------|
| ε₀ (przenikalność wolnej przestrzeni) | 8,854 × 10⁻¹² F/m |
| 1/4πε₀ (stała Coulomba k) | 8,988 × 10⁹ N·m²/C² |
### Definicja pola elektrycznego
**E** = **F**/q (siła na jednostkę ładunku)
Dla ładunku punktowego Q: **E** = (1/4πε₀) · (Q/r²) · r̂
### Linie pola elektrycznego
| Nieruchomość | Zasada |
|-------------|------|
| Kierunek | Skieruj od ładunków dodatnich w stronę ujemnych |
| Gęstość | Bliższe linie = silniejsze pole |
| Przeprawa | Linie pola nigdy się nie przecinają |
| Przewodniki | Linie stykają się z powierzchnią prostopadle |
### Potencjał elektryczny (napięcie)
V = −∫ **E** · d**l** (różnica potencjałów to ujemna całka liniowa z E)
**E** = −∇V (pole to ujemny gradient potencjału)
Dla ładunku punktowego: V = (1/4πε₀) · Q/r
| Koncepcja | Formuła | Jednostka |
|--------|---------|------|
| Energia potencjalna | U = qV | Dżule |
| Elektronowolt | 1 eV = 1,602 × 10⁻¹⁹ J | Jednostka energii |
| Powierzchnia ekwipotencjalna | Powierzchnia, na której V jest stałe | E jest do niego prostopadłe |
---

## Prawo Gaussa
### Oświadczenie
Całkowity strumień elektryczny przez dowolną zamkniętą powierzchnię jest równy zamkniętemu ładunkowi podzielonemu przez ε₀:
∮ **E** · d**A** = Q_enc / ε₀
W formie różniczkowej: ∇ · **E** = ρ/ε₀
### Korzystanie z prawa Gaussa
Prawo Gaussa jest najbardziej przydatne, gdy symetria pozwala na wyciągnięcie E z całki.
| Symetria | Powierzchnia Gaussa | Wynik |
|---------|--------------------------------|------------|
| Sferyczny | Kula | E = Q/(4πε₀r²) na zewnątrz |
| Cylindryczny (ładunek liniowy) | Cylinder | E = λ/(2πε₀r) |
| Planarny (nieskończony arkusz) | Pudełko na pigułki | E = σ/(2ε₀) |
| Między równoległymi płytami | Pudełko na pigułki | E = σ/ε₀ |
---

## Przewodniki i kondensatory
### Przewodniki w równowadze elektrostatycznej
| Nieruchomość | Wyjaśnienie |
|---------|------------|
| E = 0 wewnątrz | Ładunki zmieniają kolejność, aby anulować pole wewnętrzne |
| Cały ładunek na powierzchni | Brak opłat netto we wnętrzu |
| E prostopadle do powierzchni | Brak składowej stycznej (w przeciwnym razie ładunki poruszają się) |
| Równopotencjalny w całym | To samo V wszędzie wewnątrz i na powierzchni |
### Kondensatory
**Kondensator** magazynuje energię w polu elektrycznym pomiędzy dwoma przewodnikami.
| Konfiguracja | Pojemność |
|-------------|------------|
| Równoległe płyty | C = ε₀A/d |
| Cylindryczny | C = 2πε₀L / ln(b/a) |
| Sferyczny | C = 4πε₀ab / (b-a) |
| Formuła | Wyrażenie |
|------------|------------|
| Napięcie ładowania | P = CV |
| Energia zmagazynowana | U = ½CV² = ½Q²/C |
| Gęstość energii | u = ½ε₀E² |
| Kombinacja serii | 1/C_całkowita = 1/C₁ + 1/C₂ + ... |
| Połączenie równoległe | C_całkowita = C₁ + C₂ + ... |
### Dielektryki
Włożenie dielektryka (materiału izolacyjnego) o stałym κ zwiększa pojemność: C = κC₀.
---

## Pola magnetyczne
### Siła magnetyczna
**F** = q(**v** × **B**) (siła Lorentza, składowa magnetyczna)
| Nieruchomość | Oświadczenie |
|---------|-----------|
| Kierunek | Prostopadłe do v i B (reguła prawej ręki) |
| Wykonana praca | Zero (siła jest prostopadła do prędkości) |
| Ruch kołowy | Promień r = mv/(qB) w jednolitym polu B |
### Prawo Biota-Savarta
Pole magnetyczne wywołane przez element o małym prądzie:
d**B** = (μ₀/4π) · I(d**l** × r̂) / r²
| Stała | Wartość |
|---------|-------|
| μ₀ (przepuszczalność wolnej przestrzeni) | 4π × 10⁻⁷ T·m/A |
### Prawo Ampera
∮ **B** · d**l** = μ₀I_enc
W formie różniczkowej: ∇ × **B** = μ₀**J**
**Zastosowania:**
| Konfiguracja | Pole B |
|-------------|--------|
| Długi prosty drut | B = μ₀I/(2πr) |
| Elektrozawór (wewnątrz) | B = μ₀nI |
| Toroid (wewnątrz) | B = μ₀NI/(2πr) |
---

## Indukcja elektromagnetyczna
### Prawo Faradaya
Zmieniający się strumień magnetyczny indukuje siłę elektromotoryczną (EMF):
Pole elektromagnetyczne = −dΦ_B/dt
gdzie Φ_B = ∫ **B** · d**A** to strumień magnetyczny.
W formie różniczkowej: ∇ × **E** = −∂**B**/∂t
**Prawo Lenza:** Indukowane pole elektromagnetyczne przeciwdziała zmianie strumienia (znak minus).
### Zastosowania indukcji
| Aplikacja | Zasada |
|------------|---------------|
| Generator | Cewka wirująca w polu B → zmienne pole elektromagnetyczne |
| Transformator | Zmiana prądu w pierwotnym → EMF w wtórnym |
| Cewka | Przeciwstawia się zmianom prądu: EMF = −L(dI/dt) |
| Prądy wirowe | Prądy indukowane w przewodnikach masowych (hamowanie, ogrzewanie) |
### Cewki indukcyjne
| Formuła | Wyrażenie |
|------------|------------|
| Połączenie strumienia | Φ = LI |
| Energia zmagazynowana | U = ½LI² |
| Kombinacja serii | L_całkowita = L₁ + L₂ + ... |
| Połączenie równoległe | 1/L_całkowita = 1/L₁ + 1/L₂ + ... |
---

## Równania Maxwella
Równania Maxwella łączą elektryczność i magnetyzm w jedną teorię.
### W formie integralnej
| Równanie | Imię | Oświadczenie |
|---------|------|-----------|
| ∮ **E** · d**A** = Q/ε₀ | Prawo Gaussa (elektryczne) | Strumień elektryczny = zamknięty ładunek |
| ∮ **B** · d**A** = 0 | Prawo Gaussa (magnetyczne) | Żadnych monopoli magnetycznych |
| ∮ **E** · d**l** = −dΦ_B/dt | Prawo Faradaya | Zmiana B indukuje E |
| ∮ **B** · d**l** = μ₀I + μ₀ε₀ dΦ_E/dt | Prawo Ampera-Maxwella | Aktualne i zmieniające się E wytwarzają B |
### W formie różniczkowej
| Równanie | Imię | Wyrażenie |
|---------|------|------------|
| Gauss (elektryczny) | ∇ · **E** = ρ/ε₀ |
| Gauss (magnetyczny) | ∇ · **B** = 0 |
| Faradaya | ∇ × **E** = −∂**B**/∂t |
| Ampere-Maxwell | ∇ × **B** = μ₀**J** + μ₀ε₀ ∂**E**/∂t |
### Prąd przemieszczenia
Kluczowy dodatek Maxwella: termin μ₀ε₀ ∂**E**/∂t (prąd przemieszczenia). Zapewnia to zachowanie ładunku i przewiduje fale elektromagnetyczne.
---

## Fale elektromagnetyczne
W próżni (bez ładunków i prądów) równania Maxwella dają równania falowe:
∇²**E** = μ₀ε₀ ∂²**E**/∂t²
∇²**B** = μ₀ε₀ ∂²**B**/∂t²
**Prędkość światła:** c = 1/√(μ₀ε₀) ≈ 3 × 10⁸ m/s
### Właściwości fal EM
| Nieruchomość | Opis |
|---------|------------|
| Poprzeczny | E i B są prostopadłe do siebie i do kierunku propagacji |
| W fazie | E i B osiągają maksima jednocześnie |
| Stosunek wielkości | E = cB |
| Strumień energii | S = (1/μ₀)**E** × **B** (wektor Poyntinga) |
| Intensywność | I = ⟨S⟩ = E₀²/(2μ₀c) |
### Widmo elektromagnetyczne
| Wpisz | Długość fali | Częstotliwość | Źródło |
|------|-----------|------|--------|
| Radia | > 1 m | < 300 MHz | Antennas |
| Microwave | 1 mm − 1 m | 300 MHz − 300 GHz | Magnetrons, klystrons |
| Infrared | 700 nm − 1 mm | 300 GHz − 430 THz | Thermal radiation |
| Visible | 400 − 700 nm | 430 − 750 THz | Atomic transitions |
| Ultraviolet | 10 − 400 nm | 750 THz − 30 PHz | Hot objects, stars |
| X-ray | 0.01 − 10 nm | 30 PHz − 30 EHz | Electron deceleration |
| Gamma ray | < 0.01 nm | >30 MHz | Procesy jądrowe |
---

## Obwody prądu przemiennego
### Elementy obwodu RLC
| Składnik | Związek napięcie-prąd | Impedancja |
|----------|----------------------------|----------|
| Rezystor (R) | V = IR | Z_R = R |
| Cewka indukcyjna (L) | V = L(dI/dt) | Z_L = jωL |
| Kondensator (C) | I = C(dV/dt) | Z_C = 1/(jωC) |
### Impedancja i rezonans
Impedancja całkowita (seria RLC): Z = R + j(ωL - 1/ωC)
|ω| = √(R² + (ωL - 1/ωC)²)
**Rezonans:** Gdy ωL = 1/ωC → ω₀ = 1/√(LC)
- Przy rezonansie: impedancja jest minimalna (= R), prąd jest maksymalny
- **Współczynnik jakości:** Q = ω₀L/R (ostrość rezonansu)
### Zasilanie w obwodach prądu przemiennego
| Ilość | Formuła |
|--------------|--------|
| Średnia moc | P_avg = V_rms · I_rms · cos φ |
| Współczynnik mocy | cos φ = R/\|Z\| |
| Napięcie skuteczne | V_rms = V₀/√2 |
---

## Znaczenie dla uczenia maszynowego i nauki o danych
| Koncepcja EM | Aplikacja |
|---------------|------------|
| Równania Maxwella | Sieci neuronowe oparte na fizyce, elektromagnetyka obliczeniowa |
| Równanie falowe | Podstawy przetwarzania sygnałów, motywacja analizy Fouriera |
| Widmo elektromagnetyczne | Dane z czujników (kamery na podczerwień, radar, zdjęcia satelitarne) |
| Obwody prądu przemiennego / impedancja | Zrozumienie sprzętu obsługującego ML (zasilacze, integralność sygnału) |
| wektor wskazujący | Przepływ energii w komunikacji bezprzewodowej (dotyczy IoT/edge ML) |
| Prawo Gaussa | Analogicznie do rozbieżności w rachunku wektorowym, stosowanej w symulacjach dynamiki płynów |
| Kondensatory/induktory | Obliczenia analogowe dla sieci neuronowych, sprzęt neuromorficzny |
| rezonans | Konstrukcja filtrów, analiza w dziedzinie częstotliwości, metody spektralne |
| Problemy wartości brzegowych | Metody elementów skończonych, symulacje oparte na siatkach |
| Rachunek wektorowy (∇·, ∇×) | Podstawowe narzędzia matematyczne stosowane w teorii uczenia maszynowego |
---

## Streszczenie
| Prawo | Co to mówi | Forma różniczkowa |
|---------|------------|--------------------------------|
| Gauss (elektryczny) | Ładunki tworzą rozbieżność pola elektrycznego | ∇ · E = ρ/ε₀ |
| Gauss (magnetyczny) | Żadnych monopoli magnetycznych | ∇ · B = 0 |
| Faradaya | Zmiana B powoduje podkręcenie E | ∇ × E = −∂B/∂t |
| Ampere-Maxwell | Aktualne i zmieniające się E tworzą curling B | ∇ × B = μ₀J + μ₀ε₀∂E/∂t |
Elektromagnetyzm jest najbardziej kompletną i najlepiej przetestowaną teorią fizyczną, jaką kiedykolwiek skonstruowano. Jego równania – tylko cztery – opisują wszystko, od elektryczności statycznej po światło i zachowanie każdego urządzenia elektronicznego, jakie kiedykolwiek zbudowano. Analitykom danych zrozumienie elektromagnetyzmu zapewnia głęboką intuicję zjawisk falowych, rachunku wektorowego i fizyki leżącej u podstaw współczesnego sprzętu komputerowego.