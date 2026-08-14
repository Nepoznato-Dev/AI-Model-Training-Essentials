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
# Quantenmechanik
Quantenmechanik ist die Theorie der Physik auf den kleinsten Skalen – Atome, Elektronen, Photonen und die Grundteilchen der Natur. Es ersetzt die deterministische Welt der klassischen Mechanik durch Wahrscheinlichkeiten, Überlagerungen und Verschränkung. Trotz ihres kontraintuitiven Charakters ist die Quantenmechanik die am genauesten geprüfte Theorie in der gesamten Wissenschaft. Heutzutage werden seine Prinzipien durch Quantencomputer, die versprechen, bestimmte Probleme exponentiell schneller zu lösen als klassische Maschinen, direkt für die Datenverarbeitung relevant.
---

## Historische Motivation
### Misserfolge der klassischen Physik
| Problem | Klassische Vorhersage | Beobachtung | Auflösung |
|---------|-------|-------------|------------|
| Schwarzkörperstrahlung | Ultraviolette Katastrophe (unendliche Energie bei kurzem λ) | Endliche Peakwellenlänge | Planck: Energie ist quantisiert (E = nhν) |
| Photoelektrischer Effekt | KE hängt von der Intensität ab, nicht von der Frequenz | KE ist frequenzabhängig | Einstein: Licht ist quantisiert (Photonen, E = hν) |
| Atomspektren | Kontinuierliches Emissionsspektrum | Diskrete Spektrallinien | Bohr: Elektronen besetzen quantisierte Bahnen |
| Elektronenbeugung | Teilchen werden nicht gebeugt | Elektronen erzeugen Interferenzmuster | de Broglie: Teilchen haben die Wellenlänge λ = h/p |
### Schlüsselkonstanten
| Konstante | Symbol | Wert |
|----------|--------|-------|
| Plancksches Wirkungsquantum | h | 6,626 × 10⁻³⁴ J·s |
| Reduziertes Plancksches Wirkungsquantum | ℏ = h/2π | 1,055 × 10⁻³⁴ J·s |
| Lichtgeschwindigkeit | c | 3,0 × 10⁸ m/s |
| Elektronenmasse | m_e | 9,109 × 10⁻³¹ kg |
| Grundgebühr | e | 1,602 × 10⁻¹⁹ C |
| Bohr-Radius | a₀ | 5,292 × 10⁻¹¹ m |
---

## Welle-Teilchen-Dualität
### de Broglie Wellenlänge
Jedem Teilchen mit Impuls p ist eine Wellenlänge zugeordnet:
λ = h/p = h/(mv)
| Partikel | Typisches λ | Beobachtbares Wellenverhalten? |
|----------|-----------|--------------------------|
| Elektron (100 eV) | 0,12 nm | Ja (Kristallbeugung) |
| Proton | 0,003 nm | Ja (Neutronenstreuung) |
| Baseball (40 m/s) | 10⁻³⁴ m | Nein (viel zu klein zum Erkennen) |
### Doppelspaltexperiment
Das Quintessenz des Quantenexperiments:
1. Teilchen (Elektronen, Photonen) nacheinander an zwei Schlitzen abfeuern
2. Jedes Teilchen landet an einem einzelnen Punkt auf dem Detektor
3. Mit der Zeit entsteht ein Interferenzmuster – als ob jedes Teilchen gleichzeitig durch beide Schlitze hindurchtreten würde
4. Wenn man misst, durch welchen Spalt das Teilchen geht, verschwindet das Interferenzmuster
**Schlussfolgerung:** Quantenobjekte sind weder reine Teilchen noch reine Wellen. Sie zeigen im unbeobachteten Zustand ein wellenartiges Verhalten und bei der Messung ein teilchenartiges Verhalten.
---

## Die Wellenfunktion
### Definition
Die **Wellenfunktion** ψ(x, t) beschreibt ein Quantensystem vollständig. Es handelt sich um eine komplexwertige Funktion, deren Modulquadrat die Wahrscheinlichkeitsdichte angibt:
P(x) = |ψ(x)|² = ψ*(x)ψ(x)
### Normalisierung
Die Gesamtwahrscheinlichkeit muss gleich 1 sein:
∫ |ψ(x)|² dx = 1 (über den gesamten Raum)
### Geborene Regel
Die Wahrscheinlichkeit, das Teilchen zwischen x und x + dx zu finden:
P(x bis x+dx) = |ψ(x)|² dx
Für eine allgemeine Observable mit Eigenzuständen φₙ:
P(Messeigenwert aₙ) = |⟨φₙ|ψ⟩|²
---

## Die Schrödinger-Gleichung
### Zeitabhängige Schrödinger-Gleichung
iℏ ∂ψ/∂t = Ĥψ
wobei Ĥ der **Hamiltonsche Operator** (Gesamtenergieoperator) ist.
### Zeitunabhängige Schrödinger-Gleichung
Für stationäre Zustände (Energieeigenzustände):
Ĥψ = Eψ
Dies ist eine Eigenwertgleichung: Die zulässigen Energien E sind die Eigenwerte von Ĥ.
### Partikel in einer Box (Infinite Square Well)
Das einfachste Quantensystem: Teilchen beschränkt auf 0 < x < L.
| Menge | Ergebnis |
|----------|--------|
| Wellenfunktionen | ψₙ(x) = √(2/L) sin(nπx/L) |
| Energieniveaus | Eₙ = n²π²ℏ²/(2mL²) = n²h²/(8mL²) |
| Grundzustand | n = 1, E₁ = h²/(8mL²) |
| Nullpunktsenergie | E₁ > 0 (Teilchen kann nicht vollkommen ruhig sein) |
| Quantenzahl | n = 1, 2, 3, ... (nur positive ganze Zahlen) |
### Quantenharmonischer Oszillator
V(x) = ½mω²x²
| Menge | Ergebnis |
|----------|--------|
| Energieniveaus | Eₙ = (n + ½)ℏω |
| Nullpunktsenergie | E₀ = ½ℏω |
| Abstand | ΔE = ℏω (einheitlich) |
| Wellenfunktionen | Hermite-Polynome × Gaußsche |
---

## Operatoren und Observablen
In der Quantenmechanik entspricht jede physikalische Observable einem **Hermiteschen Operator**.
### Hauptoperatoren
| Beobachtbar | Operator (Positionsraum) | Eigenwerte |
|-----------|-----------|-------------|
| Position | x̂ = x | Alles echtes x |
| Dynamik | p̂ = −iℏ ∂/∂x | Alles echte p |
| Energie (Hamiltonian) | Ĥ = −(ℏ²/2m)∂²/∂x² + V(x) | Eₙ (diskret für gebundene Zustände) |
| Drehimpuls | L̂ = r × p̂ | ℏ√(l(l+1)) |
| Drehen | Ŝ = (ℏ/2)σ (Pauli-Matrizen) | ±ℏ/2 (für Spin-½) |
### Erwartungswerte
Das durchschnittliche Ergebnis der Messung der Observablen A im Zustand ψ:
⟨A⟩ = ⟨ψ|Â|ψ⟩ = ∫ ψ*(x) Â ψ(x) dx
### Kommutierungsbeziehungen
[Â, B̂] = ÂB̂ − B̂Â
| Kommutator | Ergebnis | Bedeutung |
|-----------|--------|-------------|
| [x̂, p̂] | ichℏ | Position und Impuls sind inkompatibel |
| [L̂ₓ, L̂ᵧ] | iℏL̂_z | Drehimpulskomponenten sind inkompatibel |
| [σ̂ₓ, σ̂ᵧ] | 2iσ̂_z | Pauli-Matrizen (Spinkomponenten) |
Wenn [Â, B̂] = 0, können die Observablen gleichzeitig gemessen werden (gemeinsame Eigenzustände).
---

## Unsicherheitsprinzip
### Heisenberg-Unsicherheitsprinzip
Δx · Δp ≥ ℏ/2
Allgemeiner gilt für zwei beliebige Observablen A und B:
ΔA · ΔB ≥ (1/2)|⟨[Â, B̂]⟩|
### Unsicherheitsbeziehungen
| Paar | Beziehung | Interpretation |
|------|----------|----------------|
| Ortsimpuls | ΔxΔp ≥ ℏ/2 | Kann beides nicht genau wissen |
| Energie-Zeit | ΔEΔt ≥ ℏ/2 | Kurzlebige Staaten haben ungewisse Energie |
| Drehimpuls | ΔLₓΔLᵧ ≥ (ℏ/2)\|⟨L_z⟩\| | Kann nicht alle Komponenten gleichzeitig kennen |
**Wichtig:** Bei der Unsicherheit geht es nicht um Messstörungen – sie ist eine grundlegende Eigenschaft von Quantenzuständen. Ein Teilchen hat nicht gleichzeitig einen bestimmten Ort und Impuls.
---

## Quantenzustände und Überlagerung
### Dirac-Notation (Bra-Ket)
| Symbol | Name | Bedeutung |
|--------|------|---------|
| \|ψ⟩ | Ket | Zustandsvektor (Spaltenvektor) |
| ⟨ψ\| | BH | Konjugierte Transponierung (Zeilenvektor) |
| ⟨φ\|ψ⟩ | Inneres Produkt | Amplitude für ψ im Zustand φ | zu finden
| \|ψ\|² | Norm im Quadrat | Wahrscheinlichkeit |
### Superpositionsprinzip
Wenn \|ψ₁⟩ und \|ψ₂⟩ gültige Quantenzustände sind, dann ist auch jede Linearkombination gültig:
\|ψ⟩ = α\|ψ₁⟩ + β\|ψ₂⟩

wobei |α|² + |β|² = 1 (Normalisierung).
**Messung:** Bei der Messung „kollabiert“ das System auf \|ψ₁⟩ mit der Wahrscheinlichkeit |α|² oder \|ψ₂⟩ mit der Wahrscheinlichkeit |β|².
### Qubits
Ein **Qubit** ist ein Quantenbit: ein Zwei-Ebenen-Quantensystem.
\|ψ⟩ = α\|0⟩ + β\|1⟩, wobei |α|² + |β|² = 1
| Darstellung | \|0⟩ | \|1⟩ |
|---------------|------|------|
| Drehen | Hochdrehen ↑ | Herunterdrehen ↓ |
| Photonenpolarisation | Horizontal | Vertikal |
| Energieniveau | Grundzustand | Aufgeregter Zustand |
| Schaltung | \|0⟩ = [1, 0]ᵀ | \|1⟩ = [0, 1]ᵀ |
**Bloch-Kugel:** Jeder Qubit-Zustand kann wie folgt geschrieben werden:
\|ψ⟩ = cos(θ/2)\|0⟩ + e^{iφ} sin(θ/2)\|1⟩
wobei θ ∈ [0, π] und φ ∈ [0, 2π). Der Zustandsraum ist eine Kugel.
---

## Verstrickung
Zwei Qubits sind **verschränkt**, wenn ihr gemeinsamer Zustand nicht als Produkt einzelner Zustände geschrieben werden kann.
### Glockenzustände (maximal verschränkt)
| Staat | Ausdruck | Name |
|-------|-----------|------|
| \|Φ⁺⟩ | (1/√2)(\|00⟩ + \|11⟩) | Glockenstaat |
| \|Φ⁻⟩ | (1/√2)(\|00⟩ − \|11⟩) | Glockenstaat |
| \|Ψ⁺⟩ | (1/√2)(\|01⟩ + \|10⟩) | Glockenstaat |
| \|Ψ⁻⟩ | (1/√2)(\|01⟩ − \|10⟩) | Singulett-Zustand |
### Eigenschaften der Verschränkung
| Eigentum | Beschreibung |
|----------|-------------|
| Korrelation | Die Messung eines Qubits bestimmt sofort das andere, unabhängig von der Entfernung |
| Keine Kommunikation | Verschränkung allein kann nicht verwendet werden, um Informationen schneller als Licht zu senden |
| Monogamie | Wenn A maximal mit B verschränkt ist, kann es nicht mit C | verschränkt werden
| Zerbrechlichkeit | Die Interaktion mit der Umwelt zerstört die Verschränkung (Dekohärenz) |
### EPR-Paradoxon und Bell-Theorem
Einstein, Podolsky und Rosen argumentierten, dass die Quantenmechanik unvollständig sein muss (verborgene Variablen). Bell zeigte, dass jede Theorie lokaler versteckter Variablen bestimmte Ungleichungen erfüllt. Experimente verstoßen gegen die Bell-Ungleichungen – sie bestätigen die Quantenmechanik und schließen lokale versteckte Variablen aus.
---

## Quantentore
Quantengatter sind einheitliche Operationen an Qubits.
### Single-Qubit-Gates
| Tor | Matrix | Wirkung |
|------|--------|--------|
| **Pauli-X** (NICHT) | [[0,1],[1,0]] | Bit-Flip: \|0⟩ ↔ \|1⟩ |
| **Pauli-Y** | [[0,−i],[i,0]] | Bit + Phasenumkehr |
| **Pauli-Z** | [[1,0],[0,−1]] | Phasenumkehr: \|1⟩ → −\|1⟩ |
| **Hadamard** (H) | (1/√2)[[1,1],[1,−1]] | Erzeugt Überlagerung: \|0⟩ → (\|0⟩+\|1⟩)/√2 |
| **Phase** (S) | [[1,0],[0,i]] | π/2 Drehung um Z |
| **T-Tor** | [[1,0],[0,e^{iπ/4}]] | π/4 Drehung um Z |
| **Rotation** Rₓ(θ) | cos(θ/2)I − i sin(θ/2)σₓ | Drehung um θ um die X-Achse |
### Zwei-Qubit-Tore
| Tor | Beschreibung | Wirkung |
|------|-------------|--------|
| **CNOT** | Kontrolliert-NICHT | Dreht das Ziel um, wenn die Kontrolle \|1⟩ | ist
| **CZ** | Kontrolliertes Z | Wendet Z auf das Ziel an, wenn die Kontrolle \|1⟩ | ist
| **TAUSCHEN** | Qubits austauschen | \|ab⟩ → \|ba⟩ |
### Verstrickung schaffen
Wenden Sie H auf Qubit 1 an, dann CNOT mit Qubit 1 als Kontrolle:
\|00⟩ → (H⊗I)\|00⟩ → CNOT → (1/√2)(\|00⟩ + \|11⟩) = \|Φ⁺⟩
---

## Quantenalgorithmen
| Algorithmus | Beschleunigung | Bewerbung |
|-----------|---------|-------------|
| **Shors** | Exponential (Factoring) | Unterbricht die RSA-Verschlüsselung |
| **Grover's** | Quadratisch (Suche) | Unstrukturierte Suche in O(√N) |
| **VQE** | Heuristik | Auffinden von Grundzustandsenergien (Chemie, Materialien) |
| **QAOA** | Heuristik | Kombinatorische Optimierung |
| **HHL** | Exponentiell (unter Bedingungen) | Lineare Systeme lösen |
| **Quantensimulation** | Exponentiell | Simulation von Quantensystemen (Feynmans ursprüngliche Motivation) |
---

## Relevanz für maschinelles Lernen und Datenwissenschaft
| Quantenkonzept | Bewerbung |
|----------------|-------------|
| Qubits und Überlagerung | Quantenmaschinelles Lernen, quantenverstärktes Sampling |
| Verstrickung | Quantenkommunikation, Quantenschlüsselverteilung (QKD) |
| Quantentore | Quantenschaltungsdesign für ML-Unterprogramme |
| Grovers Algorithmus | Quadratische Beschleunigung für suchbasierte Optimierung |
| Shors Algorithmus | Bedrohung der aktuellen Kryptographie; motiviert Post-Quanten-Krypto |
| Quantensimulation | Arzneimittelentdeckung, Materialwissenschaft, Chemiesimulation |
| Variationsalgorithmen (VQE, QAOA) | Kurzfristiges Quanten-ML auf NISQ-Geräten |
| Geborene Regel | Wahrscheinlichkeitsergebnisse analog zur Stichprobe aus Verteilungen |
| Tensorprodukte | Multi-Qubit-Systeme (exponentieller Zustandsraum – gleiche Mathematik wie multilineare Algebra in ML) |
| Einheitliche Matrizen | Quantenanaloga orthogonaler Transformationen |
---

## Zusammenfassung
| Konzept | Kernidee | Schlüsselgleichung |
|---------|-----------|-------------|
| Welle-Teilchen-Dualität | Materie hat Welleneigenschaften | λ = h/p |
| Wellenfunktion | Vollständige Beschreibung des Quantenzustands | P(x) = \|ψ(x)\|² |
| Schrödinger-Gleichung | Wie Quantenzustände entstehen | iℏ ∂ψ/∂t = Ĥψ |
| Operatoren | Observable sind hermitesche Operatoren | ⟨A⟩ = ⟨ψ\|Â\|ψ⟩ |
| Unsicherheit | Grundlegende Grenzen des Simultanwissens | ΔxΔp ≥ ℏ/2 |
| Überlagerung | Staaten können hinzugefügt werden | \|ψ⟩ = α\|0⟩ + β\|1⟩ |
| Verstrickung | Nicht trennbare gemeinsame Staaten | \|Φ⁺⟩ = (\|00⟩ + \|11⟩)/√2 |
| Quantentore | Unitäre Operationen auf Qubits | H-, CNOT- und Universal-Tor-Sets |
Die Quantenmechanik stellt unsere tiefsten Vorstellungen über die Realität in Frage – Teilchen, die Wellen sind, Objekte an zwei Orten gleichzeitig, Korrelationen, die sich einer klassischen Erklärung entziehen. Doch seine Mathematik ist präzise und seine Vorhersagen sind unübertroffen in ihrer Genauigkeit. Für Datenwissenschaftler gewinnt die Quantenmechanik durch Quantencomputing unmittelbar an Bedeutung, was verspricht, Optimierung, Kryptographie, Simulation und möglicherweise auch maschinelles Lernen selbst zu verändern.