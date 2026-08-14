<!--
---
# Metadata
title: "Numerical Methods"
description: "Floating-point arithmetic, root finding, numerical integration, ODE solvers, interpolation, numerical stability, and conditioning"
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
    changes: "Initial deep-dive into numerical methods"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2027-02-10"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-10"

# Classification
tags: [numerical-methods, floating-point, root-finding, numerical-integration, ode-solvers, interpolation, stability]
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
# Numerische Methoden
Numerische Methoden sind die Brücke zwischen mathematischer Theorie und praktischer Berechnung. Während die reine Mathematik beweist, dass es Lösungen gibt, berechnen numerische Methoden tatsächlich Näherungslösungen mit endlicher Genauigkeit. Jedes maschinelle Lernmodell, jede physikalische Simulation und jede Datenanalyse-Pipeline basiert letztendlich auf numerischen Berechnungen. Das Verständnis dieser Methoden – ihrer Genauigkeit, Stabilität und Einschränkungen – ist für die Entwicklung zuverlässiger Software von entscheidender Bedeutung.
---

## Gleitkomma-Arithmetik
Computer repräsentieren reelle Zahlen mit endlicher Genauigkeit. Der **IEEE 754-Standard** definiert, wie Gleitkommazahlen gespeichert und manipuliert werden.
### IEEE 754-Formate
| Formatieren | Bits | Exponent | Mantisse | Ungefähre Dezimalstellen | Reichweite |
|--------|------|----------|----------|---------------------------|-------|
| Halbzeit (fp16) | 16 | 5 | 10 | 3.3 | ±6,5 × 10⁴ |
| Single (fp32) | 32 | 8 | 23 | 7.2 | ±3,4 × 10³⁸ |
| Doppelt (fp64) | 64 | 11 | 52 | 15,9 | ±1,8 × 10³⁰⁸ |
### Maschinen-Epsilon
**Maschinen-Epsilon** (ε_mach) ist die kleinste Zahl, sodass 1 + ε_mach > 1 im Gleitkommawert ist.
| Formatieren | ε_mach |
|--------|--------|
| fp16 | 2⁻¹⁰ ≈ 9,8 × 10⁻⁴ |
| fp32 | 2⁻²³ ≈ 1,2 × 10⁻⁷ |
| fp64 | 2⁻⁵² ≈ 2,2 × 10⁻¹⁶ |
### Häufige Fallstricke
| Fallstrick | Beispiel | Konsequenz |
|---------|---------|-------------|
| **Katastrophale Absage** | Berechnen von (1 + x) − 1 für kleine x | Verlust signifikanter Ziffern |
| **Absorption** | 10⁸ + 1 = 10⁸ in fp32 | Kleine Werte in großen Summen verloren |
| **Nicht-Assoziativität** | (a + b) + c ≠ a + (b + c) | Summenreihenfolge zählt |
| **Division durch nahe Null** | 1 / 10⁻³⁰⁰ → Überlauf | Unendlich oder NaN |
### Minderungsstrategien
| Strategie | Beschreibung |
|----------|-------------|
| **Kahan-Zusammenfassung** | Kompensierte Summierung zur Reduzierung des Absorptionsfehlers |
| **Kahan-Babuska-Neumaier** | Verbesserte Version der Kahan-Summierung |
| **Sortierte Summierung** | Summieren Sie zuerst kleine Zahlen, um eine Absorption zu vermeiden |
| **Doppel-Doppel-Arithmetik** | Verwenden Sie Doppelpaare für eine höhere Präzision |
| **Konditionierungsanalyse** | Verstehen Sie, ob das Problem selbst Fehler verstärkt |
---

## Wurzelfindung
Finden von x mit f(x) = 0.
### Halbierungsmethode
| Eigentum | Wert |
|----------|-------|
| Erfordert | f stetig, f(a) und f(b) haben entgegengesetzte Vorzeichen |
| Konvergenz | Linear (Fehler halbiert jeden Schritt) |
| Garantiert? | Ja – konvergiert immer |
| Iterationen für d Ziffern | ≈ d / log₁₀(2) ≈ 3,32d |
**Algorithmus:**
1. Beginnen Sie mit dem Intervall [a, b], wobei f(a) · f(b) < 0 ist
2. Berechnen Sie den Mittelpunkt c = (a + b) / 2
3. Wenn f(c) = 0 oder |b − a| < Toleranz, stopp
4. Wenn f(a) · f(c) < 0, setze b = c; sonst setze a = c
5. Wiederholen
### Newton-Raphson-Methode
| Eigentum | Wert |
|----------|-------|
| Erfordert | f differenzierbar, f'(x) ≠ 0 an der Wurzel |
| Konvergenz | Quadratisch (nahe der Wurzel) |
| Garantiert? | Nein – kann divergieren oder zyklisch |
| Regel aktualisieren | x_{n+1} = x_n − f(x_n) / f'(x_n) |
**Arbeitsbeispiel:** Finden Sie √2, indem Sie f(x) = x² − 2 = 0 lösen.
- f'(x) = 2x
- x₀ = 1,5
- x₁ = 1,5 − (2,25 − 2) / 3 = 1,5 − 0,0833 = 1,4167
- x₂ = 1,4167 − (2,0069 − 2) / 2,8333 = 1,4142
- x₃ = 1,41421356... (korrekt auf 8 Dezimalstellen)
### Sekantenmethode
Wie Newtons Methode, nähert sich aber der Ableitung an:
x_{n+1} = x_n − f(x_n) · (x_n − x_{n-1}) / (f(x_n) − f(x_{n-1}))
| Eigentum | Wert |
|----------|-------|
| Konvergenz | Superlinear (Ordnung ≈ 1,618, der Goldene Schnitt) |
| Erfordert | Zwei anfängliche Schätzungen (keine Ableitung erforderlich) |
### Vergleich der Wurzelfindungsmethoden
| Methode | Konvergenz | Derivat erforderlich? | Garantiert? | Kosten pro Schritt |
|--------|-------------|-----|-------------|---------------|
| Halbierung | Linear (1) | Nein | Ja | 1 Funktionsauswertung |
| Newton-Raphson | Quadratisch (2) | Ja | Nein | 2 Funktionsauswertungen |
| Sekante | Superlinear (1.618) | Nein | Nein | 1 Funktionsauswertung |
| Brents Methode | Superlinear | Nein | Ja | Variiert |
**Brents Methode** kombiniert Halbierung (garantierte Konvergenz) mit Sekante/inverse quadratische Interpolation (schnelle Konvergenz). Es ist der Standard-Root-Finder in den meisten numerischen Bibliotheken.
---

## Numerische Integration (Quadratur)
Ungefähre Berechnung von ∫ₐᵇ f(x) dx.
### Methoden
| Methode | Formel | Fehler | Bestellen |
|--------|---------|-------|-------|
| **Rechteck (Mittelpunkt)** | (b−a) · f((a+b)/2) | O(h²) | 1 |
| **Trapezförmig** | (b−a)/2 · [f(a) + f(b)] | O(h²) | 2 |
| **Simpsons 1/3** | (b−a)/6 · [f(a) + 4f(m) + f(b)] | O(h⁴) | 3 |
| **Simpsons 3/8** | Verwendet 4 gleichmäßig verteilte Punkte | O(h⁴) | 4 |
| **Gaußsche Quadratur** | Optimale Knotenplatzierung | O(h²ⁿ) | n Punkte |
### Zusammengesetzte Regeln
Für n Teilintervalle der Breite h = (b−a)/n:
| Regel | Zusammengesetzte Formel | Fehler |
|------|-----|-------|
| Verbundtrapez | h[f(a)/2 + Σf(xᵢ) + f(b)/2] | O(h²) |
| Zusammengesetzte Simpsons | h/3[f(a) + 4Σf(ungerade) + 2Σf(gerade) + f(b)] | O(h⁴) |
**Arbeitsbeispiel:** Ungefähr ∫₀¹ e^(−x²) dx unter Verwendung eines zusammengesetzten Trapezes mit n = 4.
- h = 0,25, Punkte: 0, 0,25, 0,5, 0,75, 1
- f(0) = 1, f(0,25) = 0,9394, f(0,5) = 0,7788, f(0,75) = 0,5698, f(1) = 0,3679
- T = 0,25[1/2 + 0,9394 + 0,7788 + 0,5698 + 0,3679/2] = 0,25[1/2 + 2,2880 + 0,1840] = 0,7430
- Wahrer Wert: ≈ 0,7468 (Fehler ≈ 0,5 %)
### Adaptive Quadratur
Unterteilt automatisch Intervalle, in denen die Funktion schnell variiert, und verwendet weniger Punkte, an denen sie glatt ist. Dies ist, was`scipy.integrate.quad`verwendet (basierend auf QUADPACK).
---

## Interpolation
Schätzen von Werten zwischen bekannten Datenpunkten.
### Methoden
| Methode | Beschreibung | Glätte | Schwingung |
|--------|-------------|------------|-------------|
| **Nächster Nachbar** | Nächsten Datenpunkt verwenden | Diskontinuierlich | Keine |
| **Linear** | Punkte mit Geraden verbinden | C⁰ (kontinuierlich) | Keine |
| **Polynom (Lagrange)** | Einzelnes Polynom durch alle Punkte | C^∞ | In vielen Punkten schwerwiegend (Runge-Phänomen) |
| **Kubischer Spline** | Stückweise kubisch, an den Stoßstellen glatt | C² | Minimal |
| **Radiale Basisfunktion** | Gewichtete Summe der Radialkerne | Hängt vom Kernel ab | Niedrig |
### Lagrange-Interpolation
Gegeben n+1 Punkte (x₀, y₀), ..., (xₙ, yₙ), das eindeutige Polynom vom Grad ≤ n, das durch alle Punkte geht:
P(x) = Σᵢ₌₀ⁿ yᵢ · Πⱼ≠ᵢ (x − xⱼ) / (xᵢ − xⱼ)
**Runges Phänomen:** Polynominterpolation hohen Grades an Punkten mit gleichem Abstand kann in der Nähe der Kanten stark schwanken. Wird durch die Verwendung von Tschebyscheff-Knoten oder Splines gemildert.
### Kubische Splines
Stückweise kubische Polynome, die C²-stetig sind (stetige zweite Ableitungen).
| Geben Sie | ein Randbedingung |
|------|-----|
| Natürlicher Spline | S''(x₀) = S''(xₙ) = 0 |
| Geklemmter Spline | S'(x₀) und S'(xₙ) angegeben |
| Kein Knoten | Dritte Ableitung stetig bei x₁ und xₙ₋₁ |
---

## ODE-Löser
Gewöhnliche Differentialgleichungen dy/dt = f(t, y) numerisch lösen.
### Eulers Methode
Der einfachste ODE-Löser.
**Update:** y_{n+1} = y_n + h · f(t_n, y_n)
| Eigentum | Wert |
|----------|-------|
| Bestellen | 1 (Fehler pro Schritt: O(h²), global: O(h)) |
| Stabilität | Bedingt stabil (kleines h erforderlich) |
| Kosten | 1 Funktionsauswertung pro Schritt |
### Runge-Kutta-Methoden
| Methode | Bestellen | Stufen | Notizen |
|--------|-------|--------|-------|
| **Euler** | 1 | 1 | Am einfachsten |
| **Mittelpunkt** | 2 | 2 | Höhere Genauigkeit |
| **Heuns (RK2)** | 2 | 2 | Prädiktor-Korrektor |
| **Klassisches RK4** | 4 | 4 | Standard-Arbeitstier |
| **Dormand-Prince (RK45)** | 4(5) | 6 | Adaptive Schrittgröße (verwendet in ode45) |
### Classic RK4 (Runge-Kutta 4. Ordnung)
k₁ = f(t_n, y_n)
k₂ = f(t_n + h/2, y_n + hk₁/2)
k₃ = f(t_n + h/2, y_n + hk₂/2)
k₄ = f(t_n + h, y_n + hk₃)
y_{n+1} = y_n + h(k₁ + 2k₂ + 2k₃ + k₄) / 6
| Eigentum | Wert |
|----------|-------|
| Bestellen | 4 (globaler Fehler: O(h⁴)) |
| Kosten | 4 Funktionsauswertungen pro Schritt |
| Stabilität | Viel besser als Euler |
| Verwendung | Standard für nicht steife ODEs |
### Steife ODEs
Eine **steife** ODE hat Komponenten, die auf sehr unterschiedlichen Zeitskalen variieren. Explizite Methoden (Euler, RK4) erfordern unpraktisch kleine Schrittweiten.
| Methode | Geben Sie | ein Stabilität |
|--------|------|-----------|
| Impliziter Euler | Implizit | A-stabil (bedingungslos stabil) |
| Rückwärtsdifferenzierungsformel (BDF) | Implizit | A-stabil (bis Ordnung 5) |
| Implizites Runge-Kutta | Implizit | Es gibt L-stabile Varianten |
| LSODA | Automatisch | Wechselt zwischen steif/nicht steif |
---

## Numerische Stabilität und Konditionierung
### Bedingungsnummer
Die **Bedingungszahl** misst, wie stark sich die Ausgabe eines Problems im Verhältnis zu kleinen Änderungen in der Eingabe ändert.
Für ein lineares System Ax = b: κ(A) = ||A|| · ||A⁻¹||
| κ(A) | Interpretation |
|-------|---------------|
| ≈ 1 | Gut konditioniert |
| 10³ | Leicht empfindlich |
| 10⁸ | Schlecht konditioniert (~8 Stellen an Genauigkeit verlieren) |
| → ∞ | Singular (keine eindeutige Lösung) |
### Stabilität von Algorithmen
Ein Algorithmus ist **numerisch stabil**, wenn kleine Störungen in der Eingabe zu kleinen Störungen in der Ausgabe führen (relativ zur Bedingungszahl des Problems).
| Algorithmus | Stabil? | Notizen |
|-----------|---------|-------|
| Gaußsche Eliminierung mit teilweiser Pivotierung | Ja | Standardansatz |
| Berechnung von Eigenwerten über QR | Ja | Rückwärtsstabil |
| Naive Summierung (groß + klein zuerst) | Nein | Verwenden Sie die Kahan-Summierung |
| Berechnen der Varianz als E[X²] − (E[X])² | Möglicherweise nein | Verwenden Sie den Online-Algorithmus von Welford |
### Welfords Online-Algorithmus
Numerisch stabile Berechnung des laufenden Mittelwerts und der Varianz:
```
mean_new = mean_old + (x − mean_old) / n
M2_new = M2_old + (x − mean_old)(x − mean_new)
variance = M2 / (n − 1)
```

Dadurch wird der katastrophale Abbruch vermieden, der in der naiven Zwei-Durchgangs-Formel auftritt.
---

## Relevanz für maschinelles Lernen und Datenwissenschaft
| Numerische Methode | Bewerbung |
|-----------------|-------------|
| Gleitkomma (fp16/fp32/bf16) | Mixed-Precision-Training, Modellquantisierung, Speichereffizienz |
| Wurzelfindung | Maximum-Likelihood-Schätzung (Ermitteln, wo Gradient = 0 ist) |
| Numerische Integration | Bayesianische Inferenz (Berechnung von Grenzwahrscheinlichkeiten), erwartete Werte |
| Interpolation | Glättung, Imputation, Ersatzmodelle, Aktivierungsfunktionen |
| ODE-Löser | Neuronale ODEs, zeitkontinuierliche RNNs, Populationsdynamik, physikinformiertes ML |
| Konditionsnummer | Numerische Probleme bei linearer Regression und Normalgleichungen verstehen |
| Stabile Summierung | Berechnen von Verlustfunktionen, Batch-Normalisierungsstatistiken |
| RK4 / Adaptive Löser | Dynamische Systeme simulieren, Netzwerke mit kontinuierlicher Tiefe trainieren |
---

## Zusammenfassung
| Thema | Kernidee | Schlüsselmethode |
|-------|-----------|------------|
| Gleitkomma | Darstellung endlicher Präzision | IEEE 754, Kahan-Summierung |
| Wurzelfindung | Lösen Sie f(x) = 0 | Halbierung, Newton-Raphson, Brent's |
| Numerische Integration | Ungefähr ∫f(x)dx | Trapez, Simpson, Gaußsche Quadratur |
| Interpolation | Schätzung zwischen Datenpunkten | Kubische Splines, Lagrange, RBF |
| ODE-Löser | Lösen Sie dy/dt = f(t,y) | Euler, RK4, adaptive Methoden |
| Stabilität | Empfindlichkeit gegenüber Rundungsfehlern | Bedingungszahl, stabile Algorithmen |
Bei numerischen Methoden trifft Mathematik auf Realität. Kein Computer kann die meisten reellen Zahlen exakt darstellen, in der Praxis wird keine Ableitung symbolisch berechnet und für reale Probleme wird kein Integral in geschlossener Form ausgewertet. Wenn Sie numerische Methoden verstehen, können Sie den richtigen Algorithmus auswählen, seine Genauigkeit vorhersagen und die subtilen Fehler vermeiden, die sich aus der Arithmetik mit endlicher Genauigkeit ergeben.