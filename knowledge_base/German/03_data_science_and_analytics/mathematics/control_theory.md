<!--
---
# Metadata
title: "Control Theory"
description: "Transfer functions, block diagrams, feedback loops, PID controllers, stability analysis, state-space representation, and optimal control"
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
    changes: "Initial deep-dive into control theory"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2027-02-10"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-10"

# Classification
tags: [control-theory, transfer-functions, pid-controllers, feedback, stability, state-space, optimal-control]
difficulty_level: "advanced"
prerequisites:
  - "mathematics.md"
  - "signal_processing.md"
  - "dynamical_systems.md"
estimated_reading_time: "22 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Kontrolltheorie
Die Kontrolltheorie ist die Mathematik, mit der man Systeme dazu bringt, sich so zu verhalten, wie man es möchte. Von Thermostaten bis zu Autopiloten, von Roboterarmen bis zu chemischen Reaktoren: Steuerungssysteme erkennen, entscheiden und handeln, um das gewünschte Verhalten aufrechtzuerhalten. Das Fachgebiet bietet strenge Werkzeuge zur Analyse von Stabilität, Leistung und Robustheit – Konzepte, die in Reinforcement Learning, Hyperparameter-Tuning und adaptive Systeme übergegangen sind.
---

## Grundlegende Konzepte
### Open-Loop vs. Closed-Loop
| Geben Sie | ein Beschreibung | Beispiel | Vorteil |
|------|-------------|---------|-----------|
| **Offener Regelkreis** | Steuerwirkung unabhängig von der Ausgabe | Waschmaschinen-Timer | Einfach, kein Sensor erforderlich |
| **Geschlossener Regelkreis (Feedback)** | Die Steuerungsaktion hängt von der Ausgabe ab | Thermostat, Tempomat | Störabweisend, robust |
### Blockdiagrammelemente
| Element | Symbol | Funktion |
|---------|--------|----------|
| **Pflanze** | G(s) | Das gesteuerte System |
| **Controller** | C(s) | Berechnet die Steueraktion |
| **Sensor** | H(s) | Misst die Ausgabe |
| **Summierknotenpunkt** | ⊕ | Berechnet den Fehler: r − y |
| **Referenz** | r(t) | Gewünschte Ausgabe |
| **Fehler** | e(t) = r(t) − y(t) | Differenz zwischen Soll und Ist |
| **Störung** | d(t) | Unerwünschte Eingaben, die die Anlage beeinträchtigen |
### Closed-Loop-Übertragungsfunktion
Für ein Standard-Negativ-Feedback-System:
T(s) = C(s)G(s) / (1 + C(s)G(s)H(s))
| Menge | Formel |
|----------|---------|
| Open-Loop-Übertragungsfunktion | L(s) = C(s)G(s)H(s) |
| Übertragungsfunktion im geschlossenen Regelkreis | T(s) = L(s)/H(s) / (1 + L(s)) |
| Fehlerübertragungsfunktion | E(s)/R(s) = 1 / (1 + L(s)) |
| Empfindlichkeit | S(s) = 1 / (1 + L(s)) |
---

## Übertragungsfunktionen
Eine **Übertragungsfunktion** H(s) = Y(s)/X(s) beschreibt die Eingabe-Ausgabe-Beziehung eines linearen zeitinvarianten (LTI) Systems im Laplace-Bereich.
### Standardformulare
| System | Übertragungsfunktion | Parameter |
|--------|-----|------------|
| **Erste Ordnung** | K/(τs + 1) | K = Verstärkung, τ = Zeitkonstante |
| **Zweite Ordnung** | Kωₙ²/(s² + 2ζωₙs + ωₙ²) | ωₙ = Eigenfrequenz, ζ = Dämpfungsverhältnis |
| **Integrator** | K/s | — |
| **Differenzierer** | Ks | — |
| **Verzögerung** | e^{−sT_d} | T_d = Zeitverzögerung |
### Systemverhalten zweiter Ordnung
| Dämpfungsverhältnis ζ | Verhalten | Polstandorte |
|-----------------|-----------|---------------|
| ζ = 0 | Ungedämpfte Schwingung | Reine Einbildung |
| 0< ζ < 1 | Underdamped (oscillates, decays) | Complex with negative real part |
| ζ = 1 | Critically damped (fastest no-oscillation) | Real, repeated |
| ζ >1 | Überdämpft (langsam, keine Schwingung) | Echt, eindeutig |
### Leistungsmetriken (Schrittantwort)
| Metrisch | Formel (2. Ordnung, unterdämpft) | Beschreibung |
|--------|--------------------|-------------|
| Anstiegszeit (t_r) | ≈ 1,8/ωₙ | Zeit, von 10 % auf 90 % zu steigen |
| Spitzenzeit (t_p) | π/(ωₙ√(1−ζ²)) | Zeit bis zum ersten Maximum |
| Überschreitung (M_p) | e^{−πζ/√(1−ζ²)} × 100 % | Maximaler Peak über Endwert |
| Einschwingzeit (t_s) | ≈ 4/(ζωₙ) | Zeit, innerhalb von 2 % des Endwerts zu bleiben |
| Steady-State-Fehler | Abhängig vom Systemtyp | Differenz zwischen Soll und Ist als t → ∞ |
---

## PID-Regler
Der **PID-Regler** ist der am weitesten verbreitete Regler in der Industrie (über 90 % der Industrieregler).
### PID-Formel
u(t) = K_p e(t) + K_i ∫₀ᵗ e(τ)dτ + K_d de(t)/dt
Im Laplace-Bereich: C(s) = K_p + K_i/s + K_d s
| Begriff | Wirkung | Zu viel | Zu wenig |
|------|--------|----------|------------|
| **Proportional (K_p)** | Reagiert auf aktuellen Fehler | Schwingung, Instabilität | Langsame Reaktion, großer Fehler |
| **Integral (K_i)** | Eliminiert stationäre Fehler | Überschwingen, Schwingen | Persistenter Offset |
| **Ableitung (K_d)** | Prognostiziert zukünftige Fehler (Dämpfung) | Rauschverstärkung | Schlechte Störungsunterdrückung |
### PID-Abstimmungsmethoden
| Methode | Ansatz |
|--------|----------|
| **Ziegler-Nichols** | Erhöhe K_u bis zur Schwingung; Verwenden Sie K_u und die Periode P_u, um die Gewinne | festzulegen
| **Cohen-Coon** | Basierend auf Sprungantwortparametern (Verstärkung, Zeitkonstante, Totzeit) |
| **IMC (Interne Modellkontrolle)** | Basierend auf einem Prozessmodell; sorgt für gute Robustheit |
| **Auto-Tuning** | Online-Identifikation + Tuning (viele moderne Controller) |
| **Handbuch** | Beginnen Sie nur mit K_p, fügen Sie K_i hinzu, um den Versatz zu entfernen, und fügen Sie K_d für die Dämpfung hinzu |
### Ziegler-Nichols-Regeln
1. Setze K_i = K_d = 0
2. Erhöhen Sie K_p bis zur anhaltenden Schwingung: endgültige Verstärkung K_u, Periode P_u
3. Verstärkungen einstellen:
| Controller | K_p | K_i | K_d |
|-----------|-----|-----|-----|
| P | 0,5K_u | — | — |
| PI | 0,45K_u | 1,2K_u/P_u | — |
| PID | 0,6K_u | 2K_u/P_u | K_u P_u/8 |
---

## Stabilitätsanalyse
Ein System ist **stabil**, wenn seine Ausgabe für begrenzte Eingaben begrenzt bleibt (BIBO-Stabilität).
### Polbasierte Stabilität
| Zustand | Stabilität |
|-----------|-----------|
| Alle Pole in der linken Halbebene (Re(s)< 0) | Stable |
| Any pole in right half-plane (Re(s) >0) | Instabil |
| Pole auf imaginärer Achse (Re(s) = 0) | Etwas stabil (oder wiederholt instabil) |
### Routh-Hurwitz-Kriterium
Bestimmt die Stabilität, ohne die Pole explizit zu berechnen. Konstruiert das Routh-Array aus den charakteristischen Polynomkoeffizienten.
**Regel:** Die Anzahl der Vorzeichenwechsel in der ersten Spalte entspricht der Anzahl der Pole der rechten Halbebene.
### Nyquist-Stabilitätskriterium
Stellt den Frequenzgang L(jω) im offenen Regelkreis in der komplexen Ebene dar.
**Regel:** Das System mit geschlossenem Regelkreis ist stabil, wenn das Nyquist-Diagramm den Punkt (−1, 0) so oft gegen den Uhrzeigersinn umkreist, wie es der Anzahl der instabilen Pole im offenen Regelkreis entspricht.
**Gewinnspielraum:** Wie viel Gewinn kann vor Instabilität erhöht werden (Abstand vom Diagramm zu −1 auf der realen Achse).
**Phasenspielraum:** Wie viel Phasenverzögerung kann vor Instabilität zunehmen (Winkel vom Diagramm zum Einheitskreis beim Verstärkungsübergang).
### Bode-Plot-Analyse
Stellt Verstärkung (dB) und Phase (Grad) im Vergleich zur Frequenz (logarithmische Skala) dar.
| Metrisch | Definition | Gewünschter Wert |
|--------|-----------|---------------|
| **Gewinnmarge (GM)** | Verstärkungserhöhung, um 0 dB bei Phase = −180° | zu erreichen > 6 dB |
| **Phasenrand (PM)** | Phase bei Verstärkungsübergang (0 dB) + 180° | > 45° |
| **Crossover gewinnen** | Frequenz mit Verstärkung = 0 dB | — |
| **Phasenübergang** | Frequenz mit Phase = −180° | — |
---

## Zustandsraumdarstellung
Für Multi-Input-Multi-Output-Systeme (MIMO) ist die Zustandsraumform natürlicher als Übertragungsfunktionen.
### Standardformular
ẋ(t) = Ax(t) + Bu(t) (Zustandsgleichung)
y(t) = Cx(t) + Du(t) (Ausgabegleichung)
| Matrix | Name | Abmessungen |
|--------|------|-----------|
| A | System-/Zustandsmatrix | n × n |
| B | Eingabematrix | n × m |
| C | Ausgabematrix | p × n |
| D | Durchführungsmatrix | p × m |
### Übertragungsfunktion aus dem Zustandsraum
G(s) = C(sI − A)⁻¹B + D
### Kontrollierbarkeit und Beobachtbarkeit
| Eigentum | Test | Bedeutung |
|----------|------|---------|
| **Steuerbar** | Rang[C_B] = n (wobei C_B = [B, AB, A²B, ...]) | Kann jeden Zustand ansteuern |
| **Beobachtbar** | Rang[O_B] = n (wobei O_B = [C; CA; CA²; ...]) | Kann den Status anhand der Ausgabe ermitteln |
Ein System muss steuerbar sein, um durch Rückkopplung stabilisiert werden zu können, und für die Zustandsschätzung beobachtbar sein.
### Status-Feedback
u = −Kx + r (vollständige Zustandsrückmeldung)
Geschlossener Regelkreis: ẋ = (A − BK)x + Br
**Polplatzierung:** Wählen Sie K so, dass A − BK die gewünschten Eigenwerte (Pole) hat.
---

## Optimale Kontrolle
### Linearer quadratischer Regler (LQR)
Minimieren: J = ∫₀^∞ (xᵀQx + uᵀRu) dt
wobei Q ≥ 0 (Staatskosten) und R > 0 (Kontrollkosten) ist.
**Lösung:** u = −Kx, wobei K = R⁻¹BᵀP und P die **algebraische Riccati-Gleichung löst:**
AᵀP + PA − PBR⁻¹BᵀP + Q = 0
| Abstimmung | Wirkung |
|--------|--------|
| Q | erhöhen Schnellere Reaktion, mehr Kontrollaufwand |
| R | erhöhen Langsamere Reaktion, weniger Steuerungsaufwand |
| Q ≫ R | Aggressive Kontrolle (wie hoher K_p) |
### Kalman-Filter
Der optimale Zustandsschätzer für lineare Systeme mit Gauß-Rauschen.
**Systemmodell:**
ẋ = Ax + Bu + w (Prozessrauschen w ~ N(0, Q))
y = Cx + v (Messrauschen v ~ N(0, R))
**Kalman-Filtergleichungen:**
- Vorhersagen: x̂⁻ = Ax̂ + Bu, P⁻ = APAᵀ + Q
- Aktualisierung: K = P⁻Cᵀ(CP⁻Cᵀ + R)⁻¹, x̂ = x̂⁻ + K(y − Cx̂⁻), P = (I − KC)P⁻
Der Kalman-Filter ist der LQR-Dualfilter – er minimiert die Schätzfehlervarianz.
---

## Relevanz für maschinelles Lernen und Datenwissenschaft
| Konzept der Kontrolltheorie | Bewerbung |
|--------|-------------|
| Feedback-Steuerung | Adaptive Lernraten, Trainingsstabilisierung |
| PID-Regler | Hyperparameter-Tuning, Temperaturkontrolle in Rechenzentren |
| Zustandsraummodelle | Zeitreihenmodellierung, wiederkehrende neuronale Netze |
| Kalman-Filter | Tracking, Sensorfusion, Zustandsschätzung, Zeitreihenvorhersage |
| LQR / optimale Kontrolle | Reinforcement Learning (LQG-Steuerung), Robotik |
| Stabilitätsanalyse | Trainingsdynamik von GANs, Konvergenz von RL-Algorithmen |
| Kontrollierbarkeit/Beobachtbarkeit | Verständnis der RNN-Ausdruckskraft und Systemidentifikation |
| Übertragungsfunktionen | CNNs als lineare Filter verstehen, Frequenzbereichsanalyse |
| Nyquist/Bode | Robustheitsanalyse für adaptive Systeme |
| Polplatzierung | Entwerfen der Dynamik erlernter Systeme (Neuronale ODEs) |
---

## Zusammenfassung
| Konzept | Kernidee | Schlüsselwerkzeug |
|---------|-----------|----------|
| Feedback | Verwenden Sie die Ausgabe, um die Eingabe zu korrigieren | Übertragungsfunktion im geschlossenen Regelkreis |
| Übertragungsfunktion | Eingabe-Ausgabe-Beziehung im S-Bereich | G(s) = Y(s)/X(s) |
| PID-Steuerung | Proportional + Integral + Ableitung | Am weitesten verbreitete Industriesteuerung |
| Stabilität | Begrenzte Ausgabe für begrenzte Eingabe | Routh-Hurwitz, Nyquist, Bode |
| Zustandsraum | Interne Landesvertretung | ẋ = Ax + Bu, y = Cx + Du |
| Kontrollierbarkeit | Können wir jeden Staat erreichen? | Rangtest zur Kontrollierbarkeitsmatrix |
| Beobachtbarkeit | Können wir auf den Zustand schließen? | Rangtest zur Beobachtbarkeitsmatrix |
| LQR | Optimales Zustandsfeedback | Riccati-Gleichung |
| Kalman-Filter | Optimale Zustandsschätzung | Vorhersage-Aktualisierungszyklus |
Die Kontrolltheorie ist die Mathematik, mit der man Systeme dazu bringt, das zu tun, was man will – zuverlässig, robust und effizient. Seine Prinzipien des Feedbacks, der Stabilität und der Optimalität haben sich als universell erwiesen und tauchen in Bereichen von der Robotik bis zum verstärkenden Lernen, von der Ökonomie bis zur Biologie auf. Für Datenwissenschaftler liefert die Kontrolltheorie die Sprache zum Verständnis adaptiver Systeme, zum Entwerfen stabiler Trainingsverfahren und zum Aufbau intelligenter Agenten, die mit dynamischen Umgebungen interagieren.