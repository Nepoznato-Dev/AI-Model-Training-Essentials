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
# Klassische Mechanik
Die klassische Mechanik beschreibt die Bewegung von Objekten unter dem Einfluss von Kräften. Von fallenden Äpfeln bis hin zu umkreisenden Planeten, von vibrierenden Saiten bis hin zu kollidierenden Teilchen – seine Prinzipien bestimmen die makroskopische Welt. Über ihre physikalischen Anwendungen hinaus brachte die klassische Mechanik die Variationsrechnung, die symplektische Geometrie und das Hamilton-System hervor, das der Quantenmechanik und der modernen Optimierung zugrunde liegt.
---

## Newtonsche Mechanik
### Newtons drei Gesetze
| Recht | Aussage | Mathematische Form |
|-----|-----------|-------------------|
| **Zuerst (Trägheit)** | Ein Objekt bleibt in Ruhe oder in gleichförmiger Bewegung, sofern nicht eine Kraft auf ihn einwirkt | Wenn F_net = 0, dann ist v = konstant |
| **Sekunde (F = ma)** | Kraft ist gleich Masse mal Beschleunigung | **F** = m**a** = m(d²**x**/dt²) |
| **Drittes (Aktion-Reaktion)** | Jede Aktion hat eine gleiche und entgegengesetzte Reaktion | **F**₁₂ = −**F**₂₁ |
### Freikörperdiagramme
Ein **Freikörperdiagramm** isoliert ein Objekt und zeigt alle auf es wirkenden Kräfte.
**Gemeinsame Kräfte:**
| Kraft | Formel | Richtung |
|-------|---------|-----------|
| Schwerkraft (in der Nähe der Erde) | F = mg | Nach unten |
| Normalkraft | N | Senkrecht zur Oberfläche |
| Reibung (statisch) | f_s ≤ μ_s N | Widersetzt sich dem bevorstehenden Antrag |
| Reibung (kinetisch) | f_k = μ_k N | Lehnt den Antrag ab |
| Frühling (Hookes Gesetz) | F = −kx | Wiederherstellung (in Richtung Gleichgewicht) |
| Spannung | T | Entlang der Schnur/des Seils |
| Ziehen | F_d = ½C_d ρAv² | Entgegengesetzt der Geschwindigkeit |
### Arbeitsbeispiel: Block auf Steigung
Ein Block der Masse m auf einer reibungslosen Neigung im Winkel θ.
- Kräfte: Schwerkraft (mg nach unten), Normalkraft (N senkrecht zur Oberfläche)
- Schwerkraft zerlegen: mg sin θ (entlang der Neigung), mg cos θ (in die Oberfläche)
- N = mg cos θ (keine Bewegung senkrecht zur Oberfläche)
- Beschleunigung entlang der Steigung: a = g sin θ
---

## Energiemethoden
### Arbeit und kinetische Energie
**Arbeit**, die von einer Kraft geleistet wird: W = ∫ **F** · d**r**
**Arbeitsenergie-Theorem:** W_net = ΔKE = ½mv₂² − ½mv₁²
### Potenzielle Energie
| Kraft | Potenzielle Energie | Notizen |
|-------|---|-------|
| Schwerkraft (oberflächennah) | U = mgh | h = Höhe über Referenz |
| Schwerkraft (allgemein) | U = −GMm/r | Null im Unendlichen |
| Frühling | U = ½kx² | x = Verschiebung vom Gleichgewicht |
| Elektrostatisch | U = kq₁q₂/r | Like-Ladungen: positives U |
### Energieeinsparung
Wenn nur konservative Kräfte wirken: E = KE + PE = konstant
½mv₁² + U₁ = ½mv₂² + U₂
**Arbeitsbeispiel:** Ein Ball wurde aus der Höhe h fallen gelassen.
- Anfänglich: KE = 0, PE = mgh
- Kurz vor dem Auftreffen auf den Boden: KE = ½mv², PE = 0
- Erhaltung: mgh = ½mv² → v = √(2gh)
### Leistung
P = dW/dt = **F** · **v** (Arbeitsleistung)
---

## Dynamik und Kollisionen
### Linearer Impuls
**p** = m**v**
Newtons zweites Gesetz (alternative Form): **F** = d**p**/dt
### Erhaltung des Impulses
Wenn keine äußeren Kräfte vorhanden sind: Der Gesamtimpuls bleibt erhalten.
| Kollisionstyp | KE konserviert? | Impuls erhalten? |
|---------------|---------------|---------------------|
| **Elastisch** | Ja | Ja |
| **Unelastisch** | Nein | Ja |
| **Perfekt unelastisch** | Nein (maximaler Verlust) | Ja (Gegenstände kleben zusammen) |
**1D elastischer Stoß:** Zwei Massen m₁, m₂ mit Anfangsgeschwindigkeiten u₁, u₂:
- v₁ = ((m₁−m₂)u₁ + 2m₂u₂) / (m₁+m₂)
- v₂ = ((m₂−m₁)u₂ + 2m₁u₁) / (m₁+m₂)
### Drehimpuls
**L** = **r** × **p** = m(**r** × **v**)
Drehmoment: **τ** = d**L**/dt = **r** × **F**
**Erhaltung:** Wenn kein äußeres Drehmoment vorhanden ist, bleibt der Drehimpuls erhalten.
---

## Lagrange-Mechanik
Die **Lagrange-Formulierung** ersetzt Kräfte durch Energie und bietet so einen eleganteren und allgemeineren Rahmen.
### Der Lagrange-Operator
L = T − V (kinetische Energie minus potentielle Energie)
### Prinzip der geringsten Wirkung (Hamilton-Prinzip)
Der tatsächliche Weg, den ein System zwischen den Zeitpunkten t₁ und t₂ nimmt, minimiert (genauer gesagt, macht es stationär) die **Aktion**:
S = ∫_{t₁}^{t₂} L(q, q̇, t) dt
### Euler-Lagrange-Gleichungen
Die Bedingung δS = 0 ergibt:
d/dt(∂L/∂q̇) − ∂L/∂q = 0
für jede verallgemeinerte Koordinate q.
**Arbeitsbeispiel:** Einfaches Pendel (Länge l, Masse m, Winkel θ von der Vertikalen).
- T = ½ml²θ̇²
- V = −mgl cos θ
- L = ½ml²θ̇² + mgl cos θ
- ∂L/∂θ = −mgl sin θ
- ∂L/∂θ̇ = ml²θ̇ → d/dt(∂L/∂θ̇) = ml²θ̈
- Euler-Lagrange: ml²θ̈ + mgl sin θ = 0 → θ̈ + (g/l) sin θ = 0
### Vorteile der Lagrange-Mechanik
| Vorteil | Erklärung |
|-----------|-------------|
| Koordinatenunabhängig | Funktioniert in jedem Koordinatensystem |
| Behandelt Einschränkungen auf natürliche Weise | Es müssen keine Zwangskräfte | berechnet werden
| Symmetrie → Erhaltung | Der Satz von Noether verbindet Symmetrien mit Erhaltungsgrößen |
| Lässt sich leicht verallgemeinern | Zu Feldern, Relativität, Quantenmechanik |
---

## Hamiltonsche Mechanik
Die **Hamiltonsche** Formulierung ist eine Neuformulierung der Lagrange-Mechanik, die Positionen und Impulse (anstelle von Positionen und Geschwindigkeiten) verwendet.
### Der Hamiltonianer
H = Σᵢ pᵢq̇ᵢ − L = T + V (für die meisten mechanischen Systeme)
wobei pᵢ = ∂L/∂q̇ᵢ die **verallgemeinerten Impulse** sind.
### Hamiltons Gleichungen
q̇ᵢ = ∂H/∂pᵢ
ṗᵢ = −∂H/∂qᵢ
Dies sind 2n ODEs erster Ordnung (gegenüber n Euler-Lagrange-Gleichungen zweiter Ordnung).
**Arbeitsbeispiel:** Harmonischer Oszillator (Masse m, Federkonstante k).
- H = p²/(2m) + ½kx²
- ẋ = ∂H/∂p = p/m → p = mẋ (wie erwartet)
- ṗ = −∂H/∂x = −kx → mẍ = −kx (Hookes Gesetz)
### Poisson-Klammern
Für Funktionen f(q, p) und g(q, p):
{f, g} = Σᵢ (∂f/∂qᵢ · ∂g/∂pᵢ − ∂f/∂pᵢ · ∂g/∂qᵢ)
| Eigentum | Aussage |
|----------|-----------|
| Zeitentwicklung | df/dt = {f, H} + ∂f/∂t |
| Erhaltung | f bleibt erhalten, wenn {f, H} = 0 (und ∂f/∂t = 0) |
| Grundklammern | {qᵢ, pⱼ} = δᵢⱼ, {qᵢ, qⱼ} = 0, {pᵢ, pⱼ} = 0 |
**Verbindung zur Quantenmechanik:** Poisson-Klammern werden zu Kommutatoren: {f, g} → (1/iℏ)[f̂, ĝ]
---

## Erhaltungssätze und Noether-Theorem
### Noethers Theorem
Jede stetige Symmetrie des Lagrange-Operators entspricht einer Erhaltungsgröße.
| Symmetrie | Konservierte Menge |
|----------|-----|
| Zeitübersetzungsinvarianz | Energie |
| Räumliche Übersetzungsinvarianz | Linearer Impuls |
| Rotationsinvarianz | Drehimpuls |
| Gauge-Invarianz | Elektrische Ladung |
Dies ist eines der tiefgreifendsten Ergebnisse der gesamten Physik – es verbindet die Geometrie der Raumzeit mit den grundlegenden Erhaltungsgesetzen.
---

## Starrkörperdynamik
Ein **starrer Körper** ist ein Objekt, bei dem alle inneren Abstände fest bleiben.
### Schlüsselkonzepte
| Konzept | Formel | Beschreibung |
|---------|---------|-------------|
| **Trägheitsmoment** | I = Σmᵢrᵢ² oder I = ∫r² dm | Widerstand gegen Rotationsbeschleunigung |
| **Rotations-KE** | KE = ½Iω² | Rotationsenergie |
| **Drehimpuls** | L = Iω | Rotationsanalogon von p = mv |
| **Drehmoment** | τ = Iα | Rotationsanalogon von F = ma |
### Trägheitsmomente (gängige Formen)
| Form | Achse | Ich |
|-------|------|---|
| Massive Kugel | Durch die Mitte | (2/5)MR² |
| Hohlkugel | Durch die Mitte | (2/3)MR² |
| Vollzylinder | Entlang der Achse | (1/2)MR² |
| Dünner Stab | Durch die Mitte, senkrecht | (1/12)ML² |
| Dünner Stab | Durchgehendes Ende, senkrecht | (1/3)ML² |
| Scheibe | Durch die Mitte, senkrecht | (1/2)MR² |
---

## Orbitalmechanik
### Keplers Gesetze
| Recht | Aussage |
|-----|-----------|
| **Erste (Ellipsen)** | Planeten bewegen sich in Ellipsen mit der Sonne in einem Brennpunkt |
| **Zweiter (gleiche Flächen)** | Eine Linie von der Sonne zum Planeten überstreicht in gleichen Zeiten gleiche Flächen |
| **Terz (Harmonisch)** | T² ∝ a³ (Periode im Quadrat proportional zur dritten Halbachse) |
### Orbitalenergie
E = ½mv² − GMm/r
| E | Orbittyp |
|---|-----------|
| E< 0 | Elliptical (bound) |
| E = 0 | Parabolic (escape trajectory) |
| E >0 | Hyperbolisch (ungebunden) |
### Fluchtgeschwindigkeit
v_escape = √(2GM/R)
Für die Erde: v_escape ≈ 11,2 km/s
---

## Relevanz für maschinelles Lernen und Datenwissenschaft
| Mechanik-Konzept | Bewerbung |
|------------------|-------------|
| Newtons Gesetze | Physik-Engines in Simulationen, Spiel-KI, Robotik |
| Energiemethoden | Energiebasierte Modelle, Hopfield-Netzwerke, Boltzmann-Maschinen |
| Lagrange-Mechanik | Physikinformierte neuronale Netze, optimale Steuerung, Flugbahnoptimierung |
| Hamiltonsche Mechanik | Hamiltonsche neuronale Netze (HNNs), symplektische Integratoren für die Simulation |
| Naturschutzgesetze | Induktive Verzerrungen in ML-Modellen, äquivariante neuronale Netze |
| Noethers Theorem | Symmetriebewusstes maschinelles Lernen, geometrisches Deep Learning |
| Starrkörperdynamik | Robotiksimulation, Molekulardynamik, 3D-Animation |
| Orbitalmechanik | Satellitenpositionierung (GPS für standortbasiertes ML), Design von Weltraummissionen |
| Phasenraum (Hamiltonian) | Dynamische Systeme und Attraktornetzwerke verstehen |
| Variationsrechnung | Optimaler Transport, generative Modellierung (Flow Matching) |
---

## Zusammenfassung
| Rahmen | Kerngleichung | Stärke |
|-----------|--------------|----------|
| Newtonsche | **F** = m**a** | Intuitive, direkte Kraftanalyse |
| Lagrange | d/dt(∂L/∂q̇) − ∂L/∂q = 0 | Koordinatenfrei, verarbeitet Einschränkungen |
| Hamilton-Operator | q̇ = ∂H/∂p, ṗ = −∂H/∂q | Symplektische Struktur, verbindet sich mit QM |
| Naturschutzgesetze | Noethers Theorem | Tiefer Symmetrie-Erhaltungs-Zusammenhang |
In der klassischen Mechanik geht es nicht nur um fallende Bälle und schwingende Pendel. Seine mathematischen Rahmenwerke – die Lagrange- und Hamilton-Mechanik – gehören zu den einflussreichsten Ideen in der gesamten Wissenschaft. Sie verallgemeinern sich auf die Quantenmechanik, die Feldtheorie und sogar auf modernes maschinelles Lernen, wo energiebasierte Modelle und physikalisch fundierte neuronale Netze direkt auf diesen jahrhundertealten Formulierungen basieren.