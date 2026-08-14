---
# Metadata
title: "Statistics and Probability"
description: "Probability theory, statistical inference, hypothesis testing, regression, and Bayesian methods"
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
    date: "2026-08-09"
    author: "Nepoznato-Dev"
    changes: "Split from mathematics_and_logic.md; expanded into standalone file"

# Review
created: "2026-08-09"
last_modified: "2026-08-09"
review_date: "2027-02-09"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-09"

# Classification
tags: [statistics, probability, hypothesis-testing, regression, bayesian-methods, data-analysis]
difficulty_level: "intermediate"
prerequisites:
  - "../mathematics/mathematics.md"
estimated_reading_time: "14 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Statistik und Wahrscheinlichkeit
Wahrscheinlichkeit und Statistik sind die mathematischen Grundlagen der Datenwissenschaft, des maschinellen Lernens und der wissenschaftlichen Forschung. Die Wahrscheinlichkeit sagt Ihnen, wie wahrscheinlich Ereignisse sind. Statistiken zeigen Ihnen, wie Sie aus Daten Schlussfolgerungen ziehen können. Zusammen verwandeln sie Unsicherheit in quantifizierbares, beherrschbares Wissen.
---

## Wahrscheinlichkeitstheorie
### Kernkonzepte
| Konzept | Beschreibung | Beispiel |
|---------|-------------|---------|
| **Beispielraum** | Menge aller möglichen Ergebnisse | Würfeln: {1, 2, 3, 4, 5, 6} |
| **Ereignis** | Eine Teilmenge des Beispielraums | Eine gerade Zahl würfeln: {2, 4, 6} |
| **Wahrscheinlichkeit** | Zahl zwischen 0 und 1, die die Wahrscheinlichkeit misst | P(6 würfeln) = 1/6 |
| **Bedingte Wahrscheinlichkeit** | P(A|B): Wahrscheinlichkeit, dass A bei gegebenem B aufgetreten ist | P(Regen | bewölkt) |
| **Unabhängigkeit** | Ereignisse, bei denen das eine das andere nicht beeinflusst | Münzwürfe sind unabhängig |
### Wahrscheinlichkeitsregeln
| Regel | Formel | Anwendungsfall |
|------|---------|----------|
| **Additionsregel** | P(A ∪ B) = P(A) + P(B) − P(A ∩ B) | Wahrscheinlichkeit von A oder B |
| **Multiplikationsregel** | P(A ∩ B) = P(A) × P(B|A) | Wahrscheinlichkeit von A und B |
| **Ergänzungsregel** | P(nicht A) = 1 − P(A) | Wahrscheinlichkeit, dass das Ereignis nicht eintritt |
| **Gesetz der Gesamtwahrscheinlichkeit** | P(A) = Σ P(A|Bᵢ) × P(Bᵢ) | Partitionierung durch sich gegenseitig ausschließende Ereignisse |
| **Theorem von Bayes** | P(A|B) = P(B|A) × P(A) / P(B) | Überzeugungen durch Beweise aktualisieren |
### Wahrscheinlichkeitsverteilungen
| Vertrieb | Geben Sie | ein Schlüsselparameter | Anwendungsfall |
|-------------|------|----------------|----------|
| **Normal (Gauß)** | Kontinuierlich | Mittelwert (μ), Standardabweichung (σ) | Naturphänomene, Messfehler |
| **Binomial** | Diskret | n (Versuche), p (Wahrscheinlichkeit) | Erfolg/Misserfolg zählt |
| **Poisson** | Diskret | λ (Rate) | Seltene Ereignisse im Zeit-/Raumverlauf |
| **Exponentiell** | Kontinuierlich | λ (Rate) | Zeit zwischen Ereignissen |
| **Uniform** | Beide | a, b (Grenzen) | Gleichermaßen wahrscheinliche Ergebnisse |
| **Chi-Quadrat** | Kontinuierlich | k (Freiheitsgrade) | Anpassungstests |
| **t-Verteilung** | Kontinuierlich | ν (Freiheitsgrade) | Kleine Stichprobeninferenz |
### Schlüsseleigenschaften von Verteilungen
| Eigentum | Beschreibung |
|----------|-------------|
| **Mittelwert (erwarteter Wert)** | Schwerpunkt der Verteilung: E[X] = Σ xᵢ × P(xᵢ) |
| **Varianz** | Streuung um den Mittelwert: Var(X) = E[(X − μ)²] |
| **Standardabweichung** | Quadratwurzel der Varianz; gleiche Einheiten wie Daten |
| **Schiefe** | Asymmetrie der Verteilung |
| **Kurtosis** | „Tailedness“ – wie schwer die Schwänze sind |
---

## Statistische Schlussfolgerung
### Beschreibende vs. inferenzielle Statistik
| | Beschreibend | Inferenz |
|---|-------------|-------------|
| **Zweck** | Daten zusammenfassen und beschreiben | Aus einer Stichprobe Rückschlüsse auf eine Grundgesamtheit ziehen |
| **Werkzeuge** | Mittelwert, Median, Modus, Standardabweichung, Diagramme | Hypothesentests, Konfidenzintervalle, Regression |
| **Umfang** | Nur die Daten, die Sie haben | Über Ihre Stichprobe hinaus verallgemeinern |
### Hypothesentest-Framework
| Schritt | Beschreibung |
|------|-------------|
| 1. **Staatshypothesen** | Nullhypothese (H₀): kein Effekt; Alternative (H₁): Wirkung vorhanden |
| 2. **Signifikanzniveau auswählen** | α = 0,05 (konventionell) |
| 3. **Test auswählen** | Basierend auf Datentyp, Stichprobengröße und Annahmen |
| 4. **Teststatistik berechnen** | Hängt vom gewählten Test ab |
| 5. **P-Wert finden** | Wahrscheinlichkeit der Beobachtung der Daten, wenn H₀ wahr ist |
| 6. **Entscheidung treffen** | Wenn p < α, verwerfen Sie H₀; andernfalls kann H₀ | nicht abgelehnt werden
### Allgemeine statistische Tests
| Testen | Wann zu verwenden | Was es vergleicht |
|------|-------------|---|
| **t-Test** | Mittelwerte von 1–2 Gruppen vergleichen | Gruppenmittelwerte zu einem Wert oder zueinander |
| **Chi-Quadrat-Test** | Kategoriale Daten | Beobachtete vs. erwartete Häufigkeiten |
| **ANOVA** | Vergleichen Sie Mittelwerte von mehr als 3 Gruppen | Varianz zwischen Gruppen vs. innerhalb der Gruppe |
| **Mann-Whitney U** | Nichtparametrische Alternative zum t-Test | Rangverteilungen zweier Gruppen |
| **Pearson-Korrelation** | Lineare Beziehung zwischen zwei kontinuierlichen Variablen | r-Wert von −1 bis +1 |
| **Spearman-Korrelation** | Monotone Beziehung (rangbasiert) | ρ-Wert für ordinale oder nicht normale Daten |
### Konfidenzintervalle
Ein Konfidenzintervall gibt einen Bereich plausibler Werte für einen Populationsparameter an:
- **95 %-KI für Mittelwert** (bekanntes σ): x̄ ± 1,96 × (σ / √n)
- **Interpretation**: „Wir sind zu 95 % davon überzeugt, dass der wahre Bevölkerungsmittelwert innerhalb dieses Intervalls liegt.“
- **Größeres KI** = mehr Unsicherheit (kleinere Stichprobe, höhere Variabilität oder höheres Konfidenzniveau)
---

## Regressionsanalyse
### Arten der Regression
| Geben Sie | ein Abhängige Variable | Anwendungsfall |
|------|-----|----------|
| **Lineare Regression** | Kontinuierlich | Vorhersage von Immobilienpreisen und -verkäufen |
| **Logistische Regression** | Binär (0/1) | Klassifizierung: Spam-Erkennung, Krankheitsdiagnose |
| **Polynomielle Regression** | Kontinuierlich (gebogen) | Wachstumskurven, nichtlineare Trends |
| **Multiple Regression** | Kontinuierlich (2+ Prädiktoren) | Confounder-Kontrolle |
| **Grat / Lasso** | Kontinuierlich (reguliert) | Überanpassung verhindern, Funktionsauswahl |
### Grundlagen der linearen Regression
Das Modell: **y = β₀ + β₁x + ε**
| Komponente | Bedeutung |
|-----------|---------|
| β₀ (Achsenabschnitt) | Wert von y, wenn x = 0 |
| β₁ (Steigung) | Änderung in y für eine Änderung in x um eine Einheit |
| ε (Fehlerterm) | Ungeklärte Variation |
**Wichtige Kennzahlen:**
- **R² (Bestimmtheitskoeffizient)**: Anteil der durch das Modell erklärten Varianz (0 bis 1)
- **Angepasstes R²**: R² wird aufgrund der Anzahl der Prädiktoren bestraft
- **RMSE**: Root Mean Squared Error – durchschnittlicher Vorhersagefehler in denselben Einheiten wie y
### Annahmen der linearen Regression
| Annahme | Was es bedeutet | So überprüfen Sie |
|-----------|--------------|--------------|
| **Linearität** | Die Beziehung zwischen X und Y ist linear | Streudiagramme |
| **Unabhängigkeit** | Beobachtungen sind unabhängig | Studiendesign |
| **Homoskedastizität** | Konstante Varianz der Residuen | Restparzellen |
| **Normalität** | Residuen sind normalverteilt | Q-Q-Diagramm, Shapiro-Wilk-Test |
| **Keine Multikollinearität** | Prädiktoren sind nicht stark korreliert | VIF (Varianz-Inflationsfaktor) |
---

## Bayesianische Statistik
### Frequentist vs. Bayesian
| | Frequentist | Bayesian |
|---|-------------|----------|
| **Wahrscheinlichkeit bedeutet** | Langzeitfrequenz | Grad des Glaubens |
| **Parameter sind** | Behoben, aber unbekannt | Zufallsvariablen mit Verteilungen |
| **Verwendungen** | p-Werte, Konfidenzintervalle | Posterior-Verteilungen, glaubwürdige Intervalle |
| **Stärken** | Objektiv, fundiert | Berücksichtigt Vorkenntnisse und intuitive Interpretation |
### Satz von Bayes in der Praxis
**Posterior = (Wahrscheinlichkeit × Prior) / Evidenz**
Beispiel – medizinischer Test:
- Krankheitsprävalenz: 1 % (vorher)
- Testempfindlichkeit: 95 % (richtig positive Rate)
- Testspezifität: 90 % (richtig negative Rate)
- Wenn Ihr Test positiv ist: P(Krankheit | positiv) = (0,95 × 0,01) / (0,95 × 0,01 + 0,10 × 0,99) ≈ 8,8 %
Dieses kontraintuitive Ergebnis – die meisten positiven Ergebnisse sind falsch positiv, wenn die Krankheit selten ist – ist der **Basiszins-Irrtum** und zeigt, warum das bayesianische Denken wichtig ist.
---

## Praktische Tipps
- **Visualisieren Sie Ihre Daten immer**, bevor Sie einen statistischen Test durchführen
- **Annahmen prüfen** – Verstöße können die Ergebnisse ungültig machen
- **Die Effektstärke ist wichtig** – ein statistisch signifikantes Ergebnis kann praktisch bedeutungslos sein
- **Korrelation ist keine Kausalität** – selbst starke Korrelationen können Störfaktoren haben
- **Mehrere Vergleiche** erhöhen die Falsch-Positiv-Rate – wenden Sie Korrekturen an (Bonferroni, FDR)
- **Konfidenzintervalle angeben**, nicht nur p-Werte
---

## Warum das wichtig ist
Statistiken sind das Rückgrat der wissenschaftlichen Forschung, der Geschäftsanalyse und des maschinellen Lernens. Ohne sie ist es nicht möglich, Signale von Rauschen zu unterscheiden, echte Auswirkungen aus zufälligen Schwankungen zu erkennen oder Vorhersagen mit quantifizierter Unsicherheit zu treffen. Unabhängig davon, ob Sie A/B-Tests analysieren, ML-Modelle trainieren oder Forschungsarbeiten lesen, sind statistische Kenntnisse unerlässlich.