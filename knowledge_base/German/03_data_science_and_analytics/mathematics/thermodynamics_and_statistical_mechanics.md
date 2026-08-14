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
# Thermodynamik und statistische Mechanik
Die Thermodynamik beschreibt das makroskopische Verhalten von Systemen in Bezug auf Temperatur, Druck und Entropie – ohne zu wissen, wie Atome aussehen. Die statistische Mechanik erklärt die Thermodynamik von Grund auf: Sie leitet makroskopische Eigenschaften aus dem mikroskopischen Verhalten einer großen Anzahl von Teilchen ab. Zusammen bieten sie das tiefste Verständnis von Energie, Entropie und Gleichgewicht – Konzepte, die in die Informationstheorie, das maschinelle Lernen und darüber hinaus Eingang gefunden haben.
---

## Thermodynamische Variablen und Zustand
### Zustandsvariablen
| Variable | Geben Sie | ein Einheit | Beschreibung |
|----------|------|------|-------------|
| Temperatur (T) | Intensiv | Kelvin (K) | Durchschnittliche kinetische Energie pro Teilchen |
| Druck (P) | Intensiv | Pascal (Pa) | Kraft pro Flächeneinheit |
| Volumen (V) | Umfangreich | m³ | Platz belegt |
| Innere Energie (U) | Umfangreich | Joule (J) | Gesamte mikroskopische Energie |
| Entropie (S) | Umfangreich | J/K | Maß für Unordnung/Mikrozustände |
| Anzahl der Partikel (N) | Umfangreich | Maulwürfe oder zählen | Stoffmenge |
**Intensive** Variablen hängen nicht von der Systemgröße ab; **umfangreiche** Variablen tun dies.
### Zustandsgleichung
Für ein ideales Gas: PV = nRT = Nk_BT
| Konstante | Wert |
|----------|-------|
| R (Gaskonstante) | 8,314 J/(mol·K) |
| k_B (Boltzmann-Konstante) | 1,381 × 10⁻²³ J/K |
| N_A (Avogadros Nummer) | 6,022 × 10²³ /mol |
---

## Die Gesetze der Thermodynamik
### Nulltes Gesetz
Wenn A mit B im thermischen Gleichgewicht steht und B mit C, dann steht A mit C im thermischen Gleichgewicht.
**Bedeutung:** Die Temperatur ist genau definiert und messbar.
### Erster Hauptsatz (Energieeinsparung)
ΔU = Q − W
| Symbol | Bedeutung |
|--------|---------|
| ΔU | Veränderung der inneren Energie |
| Q | Dem System hinzugefügte Wärme |
| W | Vom System geleistete Arbeit |
**Differentialform:** dU = δQ − δW = δQ − PdV
| Prozess | Einschränkung | Konsequenz |
|---------|-----------|-------------|
| Isochorisch | dV = 0 | W = 0, ΔU = Q |
| Isobar | dP = 0 | W = PΔV |
| Isotherm | dT = 0 | ΔU = 0 (ideales Gas), Q = W |
| Adiabatisch | δQ = 0 | ΔU = −W |
### Zweites Gesetz (Entropie)
**Clausius-Aussage:** Wärme kann nicht spontan von kalt nach heiß fließen.
**Kelvin-Planck-Aussage:** Kein Motor kann die gesamte Wärme in Arbeit umwandeln.
**Entropieaussage:** Für jeden Prozess: ΔS_universum ≥ 0
| Prozesstyp | ΔS_universum |
|-------------|-------------|
| Reversibel | = 0 |
| Irreversibel (real) | > 0 |
**Entropieänderung:** dS = δQ_rev / T
### Drittes Gesetz
Da T → 0 K, geht die Entropie eines perfekten Kristalls gegen Null: lim_{T→0} S = 0
**Bedeutung:** Der absolute Nullpunkt ist in endlichen Schritten unerreichbar.
---

## Entropie im Detail
### Thermodynamische Entropie
S ist eine Zustandsfunktion. Für einen reversiblen Prozess zwischen den Zuständen A und B:
ΔS = ∫_A^B δQ_rev / T
**Arbeitsbeispiel:** Entropieänderung beim Erhitzen von Wasser von T₁ auf T₂ bei konstantem Druck.
ΔS = ∫_{T₁}^{T₂} (mc_p/T) dT = mc_p ln(T₂/T₁)
### Statistische Entropie (Boltzmann)
S = k_B ln Ω
wobei Ω die Anzahl der Mikrozustände ist, die mit dem Makrozustand übereinstimmen.
| Makrozustand | Mikrozustände (Ω) | Entropie |
|-----------|-----------------|---------|
| Alles Gas in einer Boxhälfte | Klein | Niedrig |
| Gas gleichmäßig verteilt | Sehr groß | Hoch |
| Perfekter Kristall bei 0 K | 1 | 0 |
**Verbindung:** Der zweite Hauptsatz wird statistisch – Systeme entwickeln sich in Richtung Makrozustände mit mehr Mikrozuständen, einfach weil diese überwältigend wahrscheinlicher sind.
---

## Enthalpie und Freie Energie
### Enthalpie
H = U + PV
Nützlich für Prozesse bei konstantem Druck (meist Chemie und Biologie).
ΔH = Q_p (Wärme bei konstantem Druck)
### Freie Helmholtz-Energie
F = U − TS
| Eigentum | Aussage |
|----------|-----------|
| Bedeutung | Maximal entnehmbare Arbeit bei konstantem T, V |
| Gleichgewicht | System minimiert F bei konstantem T, V |
| Beziehung zur Partitionsfunktion | F = −k_BT ln Z |
### Gibbs freie Energie
G = H − TS = U + PV − TS
| Eigentum | Aussage |
|----------|-----------|
| Bedeutung | Maximale Nichtdehnungsarbeit bei konstantem T, P |
| Gleichgewicht | System minimiert G bei konstantem T, P |
| Spontaneität | ΔG < 0 → spontan; ΔG = 0 → Gleichgewicht |
| Chemische Reaktionen | ΔG = ΔH − TΔS bestimmt die Richtung |
### Zusammenfassung der thermodynamischen Potentiale
| Potenzial | Natürliche Variablen | Differential | Minimiert, wenn |
|-----------|-----|-------------|----------------|
| U (innere Energie) | S, V | dU = TdS − PdV | Isoliertes System |
| H (Enthalpie) | S, P | dH = TdS + VdP | Konstante P, adiabatisch |
| F (Helmholtz) | T, V | dF = −SdT − PdV | Konstante T, V |
| G (Gibbs) | T, P | dG = −SdT + VdP | Konstante T, P |
---

## Der Carnot-Zyklus
Der **Carnot-Zyklus** ist die effizienteste Wärmekraftmaschine überhaupt und arbeitet zwischen den Temperaturen T_H (heiß) und T_C (kalt).
### Vier Stufen
| Bühne | Prozess | Was passiert |
|-------|---------|-------------|
| 1 → 2 | Isotherme Expansion | Nehmen Sie Wärme Q_H aus dem heißen Reservoir bei T_H | auf
| 2 → 3 | Adiabatische Expansion | Gas kühlt von T_H auf T_C | ab
| 3 → 4 | Isotherme Kompression | Wärme Q_C an kaltes Reservoir bei T_C | abgeben
| 4 → 1 | Adiabatische Kompression | Gas erwärmt sich von T_C auf T_H |
### Carnot-Effizienz
η_Carnot = 1 − T_C/T_H
| T_H | T_C | η_Carnot |
|-----|-----|----------|
| 500 K | 300 K | 40 % |
| 1000 K | 300 K | 70 % |
| 300 K | 299 K | 0,33 % |
**Kein echter Motor kann den Wirkungsgrad von Carnot übertreffen.** Echte Motoren sind immer irreversibel (Reibung, Turbulenzen, endliche Temperaturunterschiede).
---

## Statistische Mechanik
### Die Boltzmann-Verteilung
Für ein System im thermischen Gleichgewicht bei der Temperatur T beträgt die Wahrscheinlichkeit, sich in einem Mikrozustand mit der Energie E_i zu befinden:
P(E_i) = (1/Z) e^{−E_i / k_BT}
wobei Z die **Partitionsfunktion** ist:
Z = Σᵢ e^{−E_i / k_BT}
### Die Partitionsfunktion
Z kodiert alle thermodynamischen Informationen über das System.
| Menge | Formel |
|----------|---------|
| Helmholtz freie Energie | F = −k_BT ln Z |
| Durchschnittliche Energie | ⟨E⟩ = −∂(ln Z)/∂β wobei β = 1/(k_BT) |
| Entropie | S = k_B(ln Z + β⟨E⟩) |
| Wärmekapazität | C_V = ∂⟨E⟩/∂T = k_Bβ²(⟨E²⟩ − ⟨E⟩²) |
| Druck | P = (1/β) ∂(ln Z)/∂V |
### Arbeitsbeispiel: Zwei-Staaten-System
Ein Teilchen kann sich im Zustand 0 (Energie 0) oder im Zustand 1 (Energie ε) befinden.
Z = 1 + e^{−βε}
| Menge | Ergebnis |
|----------|--------|
| P(Zustand 0) | 1/(1 + e^{−βε}) |
| P(Zustand 1) | e^{−βε}/(1 + e^{−βε}) |
| ⟨E⟩ | ε/(1 + e^{βε}) |
| Hoher T-Grenzwert (β→0) | ⟨E⟩ → ε/2 (gleiche Wahrscheinlichkeit) |
| Untere T-Grenze (β→∞) | ⟨E⟩ → 0 (Grundzustand) |
### Äquipartitionssatz
Jeder quadratische Freiheitsgrad trägt ½k_BT zur durchschnittlichen Energie bei.
| System | Freiheitsgrade | ⟨E⟩ |
|--------|-----|------|
| Einatomiges Gas (He) | 3 translatorisch | (3/2)k_BT |
| Zweiatomiges Gas (N₂) bei Raum T | 3 trans + 2 rot | (5/2)k_BT |
| Zweiatomiges Gas bei hoher T | 3 trans + 2 rot + 1 vib | (7/2)k_BT |
| Solid (Einstein-Modell) | 3 Schwingungen (pro Atom) | 3k_BT |
---

## Verbindung zur Informationstheorie
### Shannon-Entropie vs. thermodynamische Entropie
| Aspekt | Shannon-Entropie H(X) | Thermodynamische Entropie S |
|--------|-------|---------|
| Definition | −Σ pᵢ log pᵢ | k_B ln Ω (oder −k_B Σ pᵢ ln pᵢ) |
| Maximum, wenn | Gleichmäßige Verteilung | Thermisches Gleichgewicht |
| Maßnahmen | Unsicherheit / Informationsgehalt | Anzahl der zugänglichen Mikrozustände |
| Einheiten | Bits oder Nats | J/K |
**Gibbs-Entropieformel:** S = −k_B Σᵢ pᵢ ln pᵢ (identisch in der Form mit der Shannon-Entropie)
### Prinzip der maximalen Entropie
Beide Bereiche nutzen das gleiche Prinzip: Die Verteilung, die unseren Wissensstand am besten repräsentiert, ist diejenige, die unter bekannten Einschränkungen die Entropie maximiert.
| Einschränkung | Resultierende Verteilung |
|-----------|--------|
| Bekannter Mittelwert | Exponentielle Verteilung |
| Bekannter Mittelwert und bekannte Varianz | Gaußsche Verteilung |
| Bekannte Energie ⟨E⟩ | Boltzmann-Verteilung |
| Keine Einschränkungen | Gleichmäßige Verteilung |
### Landauers Prinzip
Durch das Löschen eines Informationsbits werden mindestens k_BT ln 2 Energie in Form von Wärme abgegeben. Dies verbindet die Informationsverarbeitung direkt mit der Thermodynamik – Berechnungen verursachen grundlegende Energiekosten.
---

## Relevanz für maschinelles Lernen und Datenwissenschaft
| Thermo/StatMech-Konzept | Bewerbung |
|----------|-------------|
| Boltzmann-Verteilung | Softmax-Funktion, energiebasierte Modelle, simuliertes Tempern |
| Partitionsfunktion | Normalisierende Konstante in Wahrscheinlichkeitsmodellen, im Allgemeinen unlösbar |
| Freie Energie | Variationsinferenz (Minimierung der freien Variationsenergie = Minimierung der KL-Divergenz) |
| Entropie | Regularisierung, Erkundung in RL (maximale Entropie RL), Entscheidungsbäume |
| Prinzip der maximalen Entropie | MaxEnt-Klassifikatoren, Vorauswahl, Verteilungsschätzung |
| Simuliertes Glühen | Globale Optimierung durch schrittweise Reduzierung der „Temperatur“ |
| Statistische Mechanik | Phasenübergänge beim Lernen verstehen (Grokking, Double Descent) |
| Gleichverteilung | Energieverteilung in physikalischen Simulationen verstehen |
| Landauers Prinzip | Grundlegende Grenzen der Berechnung, reversibles Rechnen |
| Gibbs-Probenahme | Direkt von der statistischen Mechanik inspirierte MCMC-Methode |
| Temperatur (in Softmax) | Steuert die Zufälligkeit von Vorhersagen: P(i) ∝ exp(z_i/T) |
---

## Zusammenfassung
| Recht/Konzept | Kernidee | Formel |
|------------|-----------|---------|
| Nulltes Gesetz | Die Temperatur ist wohldefiniert | Transitivität des thermischen Gleichgewichts |
| Erstes Gesetz | Energie bleibt erhalten | ΔU = Q − W |
| Zweites Gesetz | Die Entropie des Universums nimmt zu | ΔS ≥ 0 |
| Drittes Gesetz | Der absolute Nullpunkt ist unerreichbar | S → 0 als T → 0 |
| Boltzmann-Entropie | Entropie zählt Mikrozustände | S = k_B ln Ω |
| Boltzmann-Verteilung | Wahrscheinlichkeit von Energiezuständen | P ∝ e^{−E/k_BT} |
| Partitionsfunktion | Kodiert alle thermodynamischen Informationen | Z = Σ e^{−E_i/k_BT} |
| Freie Energie | Nützliche Arbeit verfügbar | F = U − TS, G = H − TS |
| Carnot-Effizienz | Maximale Effizienz der Wärmekraftmaschine | η = 1 − T_C/T_H |
In der Thermodynamik und der statistischen Mechanik trifft Physik auf Informationstheorie. Dieselbe Entropie, die Wärmekraftmaschinen beherrscht, regelt auch die Datenkomprimierung. Dieselbe Boltzmann-Verteilung, die Gasmoleküle beschreibt, treibt die Softmax-Schicht in jedem Klassifikator an. Wenn Sie diese Zusammenhänge verstehen, erhalten Sie einen einheitlichen Überblick über Physik, Wahrscheinlichkeit und maschinelles Lernen.