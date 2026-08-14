<!--
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
  - name: "Nepoznato-Dev"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.0"
    date: "2026-08-10"
    author: "Nepoznato-Dev"
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

-->
# Elektromagnetismus
Elektromagnetismus ist die Untersuchung elektrischer und magnetischer Felder und ihrer Wechselwirkungen. Der Elektromagnetismus wurde in den 1860er Jahren von Maxwell vereinheitlicht und erklärt Licht, Elektrizität, Magnetismus, Radiowellen und die Struktur von Atomen. Sie war die erste fundamentale Kraft, die mathematisch vollständig verstanden wurde, und ihre Gleichungen inspirierten Einsteins spezielle Relativitätstheorie und die moderne Feldtheorie.
---

## Elektrische Felder
### Coulombsches Gesetz
Die Kraft zwischen zwei Punktladungen q₁ und q₂ im Abstand r:
**F** = (1/4πε₀) · (q₁q₂/r²) · r̂
| Konstante | Wert |
|----------|-------|
| ε₀ (Permittivität des freien Raums) | 8,854 × 10⁻¹² F/m |
| 1/4πε₀ (Coulomb-Konstante k) | 8,988 × 10⁹ N·m²/C² |
### Definition des elektrischen Feldes
**E** = **F**/q (Kraft pro Ladungseinheit)
Für eine Punktladung Q: **E** = (1/4πε₀) · (Q/r²) · r̂
### Elektrische Feldlinien
| Eigentum | Regel |
|----------|------|
| Richtung | Zeigen Sie von positiven Ladungen weg, hin zu negativen |
| Dichte | Nähere Linien = stärkeres Feld |
| Kreuzung | Feldlinien kreuzen sich nie |
| Dirigenten | Linien treffen senkrecht auf die Oberfläche |
### Elektrisches Potenzial (Spannung)
V = −∫ **E** · d**l** (Potentialdifferenz ist das negative Linienintegral von E)
**E** = −∇V (Feld ist der negative Gradient des Potentials)
Für eine Punktladung: V = (1/4πε₀) · Q/r
| Konzept | Formel | Einheit |
|---------|---------|------|
| Potenzielle Energie | U = qV | Joule |
| Elektronenvolt | 1 eV = 1,602 × 10⁻¹⁹ J | Energieeinheit |
| Äquipotentialfläche | Oberfläche, auf der V konstant ist | E steht senkrecht dazu |
---

## Gaußsches Gesetz
### Stellungnahme
Der gesamte elektrische Fluss durch eine geschlossene Oberfläche entspricht der eingeschlossenen Ladung dividiert durch ε₀:
∮ **E** · d**A** = Q_enc / ε₀
In Differentialform: ∇ · **E** = ρ/ε₀
### Verwendung des Gaußschen Gesetzes
Das Gaußsche Gesetz ist am nützlichsten, wenn die Symmetrie es erlaubt, E aus dem Integral herauszuziehen.
| Symmetrie | Gaußsche Oberfläche | Ergebnis |
|----------|-----------------|--------|
| Sphärisch | Kugel | E = Q/(4πε₀r²) außerhalb |
| Zylindrisch (Linienladung) | Zylinder | E = λ/(2πε₀r) |
| Planar (unendliches Blatt) | Pillendose | E = σ/(2ε₀) |
| Zwischen parallelen Platten | Pillendose | E = σ/ε₀ |
---

## Leiter und Kondensatoren
### Leiter im elektrostatischen Gleichgewicht
| Eigentum | Erklärung |
|----------|-------------|
| E = 0 innen | Gebühren neu anordnen, um internes Feld zu löschen |
| Alle Ladungen auf der Oberfläche | Keine Nettogebühr im Innenraum |
| E senkrecht zur Oberfläche | Keine tangentiale Komponente (sonst verschieben sich Ladungen) |
| Äquipotential überall | Gleiches V überall innen und auf der Oberfläche |
### Kondensatoren
Ein **Kondensator** speichert Energie in einem elektrischen Feld zwischen zwei Leitern.
| Konfiguration | Kapazität |
|--------------|-------------|
| Parallelplatten | C = ε₀A/d |
| Zylindrisch | C = 2πε₀L / ln(b/a) |
| Sphärisch | C = 4πε₀ab / (b−a) |
| Formel | Ausdruck |
|---------|------------|
| Ladespannung | Q = CV |
| Energie gespeichert | U = ½CV² = ½Q²/C |
| Energiedichte | u = ½ε₀E² |
| Serienkombination | 1/C_total = 1/C₁ + 1/C₂ + ... |
| Parallelkombination | C_total = C₁ + C₂ + ... |
### Dielektrika
Das Einsetzen eines Dielektrikums (Isoliermaterial) mit konstantem κ erhöht die Kapazität: C = κC₀.
---

## Magnetische Felder
### Magnetische Kraft
**F** = q(**v** × **B**) (Lorentzkraft, magnetische Komponente)
| Eigentum | Aussage |
|----------|-----------|
| Richtung | Senkrecht zu v und B (Rechte-Hand-Regel) |
| Arbeit erledigt | Null (Kraft ist senkrecht zur Geschwindigkeit) |
| Kreisbewegung | Radius r = mv/(qB) im einheitlichen B-Feld |
### Biot-Savart-Gesetz
Das Magnetfeld aufgrund eines kleinen Stromelements:
d**B** = (μ₀/4π) · I(d**l** × r̂) / r²
| Konstante | Wert |
|----------|-------|
| μ₀ (Durchlässigkeit des freien Raums) | 4π × 10⁻⁷ T·m/A |
### Amperesches Gesetz
∮ **B** · d**l** = μ₀I_enc
In Differentialform: ∇ × **B** = μ₀**J**
**Anwendungen:**
| Konfiguration | B-Feld |
|--------------|---------|
| Langer gerader Draht | B = μ₀I/(2πr) |
| Magnet (innen) | B = μ₀nI |
| Ringkern (innen) | B = μ₀NI/(2πr) |
---

## Elektromagnetische Induktion
### Faradaysches Gesetz
Ein sich ändernder magnetischer Fluss induziert eine elektromotorische Kraft (EMF):
EMF = −dΦ_B/dt
wobei Φ_B = ∫ **B** · d**A** der magnetische Fluss ist.
In Differentialform: ∇ × **E** = −∂**B**/∂t
**Lenzsches Gesetz:** Die induzierte EMF wirkt der Änderung des Flusses entgegen (das Minuszeichen).
### Anwendungen der Induktion
| Bewerbung | Prinzip |
|-------------|-----------|
| Generator | Rotierende Spule im B-Feld → alternierende EMF |
| Transformator | Stromänderung in der Primärseite → EMF in der Sekundärseite |
| Induktor | Wirkt Stromänderungen entgegen: EMF = −L(dI/dt) |
| Wirbelströme | Induzierte Ströme in Massenleitern (Bremsen, Heizen) |
### Induktoren
| Formel | Ausdruck |
|---------|------------|
| Flussverknüpfung | Φ = LI |
| Energie gespeichert | U = ½LI² |
| Serienkombination | L_total = L₁ + L₂ + ... |
| Parallelkombination | 1/L_total = 1/L₁ + 1/L₂ + ... |
---

## Maxwells Gleichungen
Maxwells Gleichungen vereinen Elektrizität und Magnetismus in einer einzigen Theorie.
### In integraler Form
| Gleichung | Name | Aussage |
|----------|------|-----------|
| ∮ **E** · d**A** = Q/ε₀ | Gaußsches Gesetz (elektrisch) | Elektrischer Fluss = eingeschlossene Ladung |
| ∮ **B** · d**A** = 0 | Gaußsches Gesetz (magnetisch) | Keine magnetischen Monopole |
| ∮ **E** · d**l** = −dΦ_B/dt | Faradaysches Gesetz | Die Änderung von B induziert E |
| ∮ **B** · d**l** = μ₀I + μ₀ε₀ dΦ_E/dt | Ampere-Maxwell-Gesetz | Aktuelles und sich änderndes E erzeugen B |
### In Differentialform
| Gleichung | Name | Ausdruck |
|----------|------|------------|
| Gauß (elektrisch) | ∇ · **E** = ρ/ε₀ |
| Gauß (magnetisch) | ∇ · **B** = 0 |
| Faraday | ∇ × **E** = −∂**B**/∂t |
| Ampere-Maxwell | ∇ × **B** = μ₀**J** + μ₀ε₀ ∂**E**/∂t |
### Der Verschiebungsstrom
Maxwells wichtigster Zusatz: der Term μ₀ε₀ ∂**E**/∂t (Verschiebungsstrom). Dies stellt die Ladungserhaltung sicher und sagt elektromagnetische Wellen voraus.
---

## Elektromagnetische Wellen
Im Vakuum (keine Ladungen, keine Ströme) ergeben die Maxwell-Gleichungen Wellengleichungen:
∇²**E** = μ₀ε₀ ∂²**E**/∂t²
∇²**B** = μ₀ε₀ ∂²**B**/∂t²
**Lichtgeschwindigkeit:** c = 1/√(μ₀ε₀) ≈ 3 × 10⁸ m/s
### Eigenschaften von EM-Wellen
| Eigentum | Beschreibung |
|----------|-------------|
| Quer | E und B stehen senkrecht zueinander und zur Ausbreitungsrichtung |
| In Phase | E und B erreichen gleichzeitig Maxima |
| Größenverhältnis | E = cB |
| Energiefluss | S = (1/μ₀)**E** × **B** (Poynting-Vektor) |
| Intensität | I = ⟨S⟩ = E₀²/(2μ₀c) |
### Das elektromagnetische Spektrum
| Geben Sie | ein Wellenlänge | Häufigkeit | Quelle |
|------|-----------|-----------|--------|
| Radio | > 1m | < 300 MHz | Antennas |
| Microwave | 1 mm − 1 m | 300 MHz − 300 GHz | Magnetrons, klystrons |
| Infrared | 700 nm − 1 mm | 300 GHz − 430 THz | Thermal radiation |
| Visible | 400 − 700 nm | 430 − 750 THz | Atomic transitions |
| Ultraviolet | 10 − 400 nm | 750 THz − 30 PHz | Hot objects, stars |
| X-ray | 0.01 − 10 nm | 30 PHz − 30 EHz | Electron deceleration |
| Gamma ray | < 0.01 nm | >30 EHz | Nukleare Prozesse |
---

## Wechselstromkreise
### RLC-Schaltungskomponenten
| Komponente | Spannungs-Strom-Beziehung | Impedanz |
|-----------|---------|-----------|
| Widerstand (R) | V = IR | Z_R = R |
| Induktor (L) | V = L(dI/dt) | Z_L = jωL |
| Kondensator (C) | I = C(dV/dt) | Z_C = 1/(jωC) |
### Impedanz und Resonanz
Gesamtimpedanz (Serie RLC): Z = R + j(ωL − 1/ωC)
|ω| = √(R² + (ωL − 1/ωC)²)
**Resonanz:** Wenn ωL = 1/ωC → ω₀ = 1/√(LC)
- Bei Resonanz: Impedanz minimal (= R), Strom maximal
- **Qualitätsfaktor:** Q = ω₀L/R (Resonanzschärfe)
### Strom in Wechselstromkreisen
| Menge | Formel |
|----------|---------|
| Durchschnittliche Leistung | P_avg = V_rms · I_rms · cos φ |
| Leistungsfaktor | cos φ = R/\|Z\| |
| RMS-Spannung | V_rms = V₀/√2 |
---

## Relevanz für maschinelles Lernen und Datenwissenschaft
| EM-Konzept | Bewerbung |
|-----------|-------------|
| Maxwell-Gleichungen | Physikinformierte neuronale Netze, computergestützte Elektromagnetik |
| Wellengleichung | Grundlagen der Signalverarbeitung, Motivation der Fourier-Analyse |
| Elektromagnetisches Spektrum | Sensordaten (Infrarotkameras, Radar, Satellitenbilder) |
| Wechselstromkreise / Impedanz | Hardware verstehen, die ML ausführt (Stromversorgung, Signalintegrität) |
| Poynting-Vektor | Energiefluss in der drahtlosen Kommunikation (relevant für IoT/Edge ML) |
| Gaußsches Gesetz | Analog zur Divergenz in der Vektorrechnung, die in Simulationen der Fluiddynamik verwendet wird |
| Kondensatoren/Induktivitäten | Analoges Rechnen für neuronale Netze, neuromorphe Hardware |
| Resonanz | Filterdesign, Frequenzbereichsanalyse, Spektralmethoden |
| Grenzwertprobleme | Finite-Elemente-Methoden, netzbasierte Simulationen |
| Vektorrechnung (∇·, ∇×) | Wesentliche mathematische Werkzeuge, die in der gesamten ML-Theorie verwendet werden |
---

## Zusammenfassung
| Recht | Was es sagt | Differentialform |
|-----|-------------|-------------------|
| Gauß (elektrisch) | Ladungen erzeugen Divergenz im elektrischen Feld | ∇ · E = ρ/ε₀ |
| Gauß (magnetisch) | Keine magnetischen Monopole | ∇ · B = 0 |
| Faraday | Durch Ändern von B entsteht Curling E | ∇ × E = −∂B/∂t |
| Ampere-Maxwell | Aktuelles und wechselndes E erzeugen Curling B | ∇ × B = μ₀J + μ₀ε₀∂E/∂t |
Der Elektromagnetismus ist die vollständigste und am besten geprüfte physikalische Theorie, die jemals aufgestellt wurde. Seine Gleichungen – nur vier – beschreiben alles von statischer Elektrizität über Licht bis hin zum Verhalten jedes jemals gebauten elektronischen Geräts. Für Datenwissenschaftler bietet das Verständnis des Elektromagnetismus ein tiefes Verständnis für Wellenphänomene, Vektorrechnung und die Physik, die jeder modernen Computerhardware zugrunde liegt.