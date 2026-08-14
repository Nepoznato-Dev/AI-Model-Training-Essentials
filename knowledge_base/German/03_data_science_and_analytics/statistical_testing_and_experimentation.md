---
# Metadata
title: "Statistical Testing and Experimentation"
description: "Hypothesis testing, A/B testing, effect size, causal inference"
category: "Data Science and Analytics"
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
    date: "2026-08-05"
    author: "Nepoznato-Dev"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-05"
review_date: "2027-02-05"
reviewed_by: "Data Science & Analytics Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [statistical, testing, experimentation, data-science-and-analytics]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "10 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Statistische Tests und Experimente
Statistik ist die Grammatik der Wissenschaft. Es gibt Ihnen die Werkzeuge an die Hand, um reale Muster von zufälligem Rauschen zu unterscheiden, um zu messen, ob eine Änderung tatsächlich zu Verbesserungen geführt hat, und um Entscheidungen unter Unsicherheit zu treffen. Diese Datei behandelt die Kernkonzepte des Hypothesentests, des experimentellen Designs und der häufigsten Fallstricke, die Menschen zum Stolpern bringen.
---

## Das Hypothesentest-Framework
Jeder statistische Test folgt der gleichen Logik:
1. **Formulieren Sie die Nullhypothese (H₀)**: Es gibt keinen Effekt / keinen Unterschied.
2. **Formulieren Sie die Alternativhypothese (H₁)**: Es gibt einen Effekt / einen Unterschied.
3. **Wählen Sie ein Signifikanzniveau (α)**: Normalerweise 0,05 (5 % Chance auf falsch positive Ergebnisse).
4. **Daten sammeln und eine Teststatistik berechnen**.
5. **Berechnen Sie den p-Wert**: Wahrscheinlichkeit, dieses Ergebnis (oder ein extremeres Ergebnis) zu beobachten, wenn H₀ wahr ist.
6. **Treffen Sie eine Entscheidung**: Wenn p < α, lehnen Sie H₀ ab (statistisch signifikant). Andernfalls können Sie H₀ nicht ablehnen.
### Schlüsselkonzepte
| Konzept | Bedeutung | Häufiges Missverständnis |
|---------|---------|-------|
| **p-Wert** | P(Daten \| H₀ ist wahr) | NICHT „die Wahrscheinlichkeit, dass H₀ wahr ist“ |
| **α (Signifikanzniveau)** | Schwelle für die Ablehnung von H₀ | Kein Maß für die Wirkungsbedeutung |
| **Statistische Signifikanz** | Ergebnis allein aufgrund des Zufalls unwahrscheinlich | Bedeutet NICHT praktisch bedeutsam |
| **Effektgröße** | Ausmaß des beobachteten Effekts | Getrennt vom p-Wert; ein kleiner Effekt kann bei großem N | erheblich sein
| **Leistung** | Wahrscheinlichkeit, ein falsches H₀ | korrekt abzulehnen Streben Sie normalerweise 80 %+ | an
| **Konfidenzintervall** | Bereich plausibler Werte für den Parameter | Ein 95 %-KI bedeutet nicht „95 % Wahrscheinlichkeit, dass der wahre Wert in diesem Bereich liegt“ |
---

## Arten von Fehlern
| | H₀ ist wahr | H₀ ist falsch |
|---|-----------|------------|
| **H₀ ablehnen** | Fehler vom Typ I (falsch positiv) | ✅ Richtig (richtig positiv) |
| **H₀ konnte nicht abgelehnt werden** | ✅ Richtig (echt negativ) | Fehler vom Typ II (falsch negativ) |
| Fehler | Symbol | Bedeutung |
|-------|--------|---------|
| **Typ I** | α | Daraus lässt sich schließen, dass es einen Effekt gibt, wenn dieser nicht vorhanden ist |
| **Typ II** | β | Es fehlt ein echter Effekt |
---

## Den richtigen Test auswählen
| Szenario | Testen | Annahmen |
|----------|------|-------------|
| Vergleichen Sie Mittelwerte von 2 Gruppen | **t-Test** (unabhängig) | Normalverteilung, gleiche Varianz |
| Mittelwerte gepaarter Beobachtungen vergleichen | **Gepaarter t-Test** | Unterschiede sind normalverteilt |
| Vergleichen Sie die Mittelwerte von mehr als 3 Gruppen | **ANOVA** | Normalverteilung, gleiche Varianz |
| Vergleichen Sie kategoriale Verteilungen | **Chi-Quadrat-Test** | Ausreichende Stichprobengröße pro Zelle |
| Vergleichen Sie Verteilungen (nicht parametrisch) | **Mann-Whitney U** | Keine Normalitätsannahme |
| Vergleichen Sie mehr als 3 Gruppen (nicht parametrisch) | **Kruskal-Wallis** | Keine Normalitätsannahme |
| Testkorrelation | **Pearson** (linear) oder **Spearman** (monoton) | Pearson: Normalität; Spearman: rangbasiert |
| Testen Sie, ob die Daten einer Verteilung folgen | **Kolmogorov-Smirnov** | Kontinuierliche Daten |
### Parametrisch vs. nichtparametrisch
| | Parametrisch | Nichtparametrisch |
|---|-----------|---------------|
| **Annahmen** | Die Daten folgen einer bestimmten Verteilung (normalerweise normal) | Keine Verteilungsannahme |
| **Leistung** | Höher, wenn die Annahmen erfüllt sind | Niedriger, aber robuster |
| **Wann zu verwenden** | Große Stichproben, ungefähr normale Daten | Kleine Stichproben, verzerrte Daten, Ordinaldaten |
---

## Spezifische Tests im Detail
### t-Test
Vergleicht die Mittelwerte zweier Gruppen.
| Variante | Anwendungsfall |
|---------|----------|
| **Unabhängiger t-Test** | Zwei getrennte Gruppen (Behandlung vs. Kontrolle) |
| **Gepaarter t-Test** | Dieselbe Gruppe wurde zweimal gemessen (vorher vs. nachher) |
| **T-Test bei einer Stichprobe** | Vergleichen Sie einen Stichprobenmittelwert mit einem bekannten Wert |
```python
from scipy import stats

# Independent t-test
t_stat, p_value = stats.ttest_ind(group_a, group_b)
```

### ANOVA (Varianzanalyse)
Vergleicht Mittelwerte aus drei oder mehr Gruppen. Testet, ob sich mindestens ein Gruppenmittelwert vom Rest unterscheidet.
| Geben Sie | ein Design |
|------|--------|
| **Einfaktorielle ANOVA** | Eine unabhängige Variable mit mehr als 3 Ebenen |
| **Zweifaktorielle ANOVA** | Zwei unabhängige Variablen; testet Interaktionseffekte |
| **ANOVA mit wiederholten Messungen** | Gleiche Probanden unter unterschiedlichen Bedingungen gemessen |
Wenn die ANOVA signifikant ist, führen Sie anschließend **Post-hoc-Tests** (Tukey-HSD) durch, um herauszufinden, welche spezifischen Gruppen sich unterscheiden.
### Chi-Quadrat-Test
Testet, ob zwei kategoriale Variablen unabhängig sind.
| Anwendungsfall | Beispiel |
|----------|---------|
| **Test der Unabhängigkeit** | Ist das Geschlecht mit der Produktpräferenz verknüpft? |
| **Anpassungsgüte** | Folgt ein Würfelwurf einer gleichmäßigen Verteilung? |
**Faustregel**: Jede Zelle sollte eine erwartete Anzahl von mindestens 5 haben.
---

## A/B-Tests
A/B-Tests sind die Anwendung von Hypothesentests auf Geschäftsentscheidungen – typischerweise der Vergleich einer Kontrolle (A) mit einer Variante (B).
### Designprozess
| Schritt | Beschreibung |
|------|-------------|
| **1. Hypothese definieren** | „Das Ändern der Schaltflächenfarbe von Blau auf Grün erhöht die Klickrate“ |
| **2. Wählen Sie Metrik** | Primär: Klickrate. Sekundär: Conversion-Rate, Umsatz. |
| **3. Stichprobengröße berechnen** | Basierend auf dem minimal erkennbaren Effekt, der Stärke (80 %) und der Signifikanz (5 %) |
| **4. Randomisieren** | Weisen Sie Benutzer nach dem Zufallsprinzip der Kontrolle und Behandlung zu. |
| **5. Experiment durchführen** | Sammeln Sie Daten, bis die Zielstichprobengröße erreicht ist |
| **6. Analysieren** | Vergleichen Sie Metriken mit geeigneten statistischen Tests |
| **7. Entscheiden** | Implementieren, wenn statistisch und praktisch signifikant |
### Berechnung der Stichprobengröße
Die benötigte Stichprobengröße hängt ab von:
| Faktor | Auswirkung auf die Stichprobengröße |
|--------|--------|
| **Kleinerer zu erkennender Effekt** | Benötigen Sie weitere Proben |
| **Höhere Leistung** | Benötigen Sie weitere Proben |
| **Unteres Signifikanzniveau** | Benötigen Sie weitere Proben |
| **Höhere Varianz** | Benötigen Sie weitere Proben |
### Häufige A/B-Testfehler
| Fehler | Warum es falsch ist |
|---------|---------------|
| **Früh gucken** | Die tägliche Überprüfung der Ergebnisse erhöht die Falsch-Positiv-Rate |
| **Mehrere Messwerte ohne Korrektur** | Testen von 20 Metriken bei α=0,05 → Erwarten Sie zufällig 1 falsch positives Ergebnis |
| **Anhalten vor Ziel N** | Test mit unzureichender Leistung kann keine tatsächlichen Auswirkungen erkennen |
| **Saisonalität ignorieren** | Durchführung eines Tests über einen Feiertag im Vergleich zu einer normalen Woche |
| **Nicht zufällige Zuweisung** | Auswahlverzerrung (z. B. Zuweisung neuer Benutzer zur Behandlung) |
| **Bedeutung mit Wichtigkeit verwechseln** | Eine Steigerung um 0,1 % kann statistisch signifikant sein, ist aber keinen Versand wert |
---

## Mehrere Vergleiche
Wenn Sie viele Tests gleichzeitig durchführen, steigt die Wahrscheinlichkeit, dass mindestens ein falsch positives Ergebnis vorliegt, dramatisch an.
| Anzahl der Tests | Wahrscheinlichkeit von ≥1 falsch positiv (bei α=0,05) |
|----------------|--------------------------------------------|
| 1 | 5 % |
| 5 | 23 % |
| 10 | 40 % |
| 20 | 64 % |
### Korrekturen
| Methode | Wie es funktioniert | Wann zu verwenden |
|--------|-------------|-------------|
| **Bonferroni** | Teilen Sie α durch die Anzahl der Tests (α/n) | Konservativ; wenige Vergleiche |
| **Holm-Bonferroni** | Step-down-Verfahren; weniger konservativ | Allgemeine Verwendung |
| **Benjamini-Hochberg (FDR)** | Steuert die Falscherkennungsrate | Viele Tests; explorative Analyse |
---

## Effektgröße
P-Werte sagen Ihnen, *ob* ein Effekt vorliegt. Die Effektgröße gibt an, *wie groß* sie ist.
| Messen | Für | Interpretation |
|---------|-----|---------------|
| **Cohens Tod** | Differenz zwischen zwei Mitteln | 0,2 = klein, 0,5 = mittel, 0,8 = groß |
| **Pearsons r** | Korrelation | 0,1 = klein, 0,3 = mittel, 0,5 = groß |
| **η² (eta-Quadrat)** | ANOVA | 0,01 = klein, 0,06 = mittel, 0,14 = groß |
| **Chancenverhältnis** | Kategoriale Ergebnisse | 1,0 = keine Auswirkung; >1 oder <1 = Wirkung |
**Geben Sie die Effektstärke immer zusammen mit den p-Werten an.** Ein Ergebnis kann statistisch signifikant, aber praktisch bedeutungslos sein.
---

## Bayesian vs. Frequentist
| Aspekt | Frequentist | Bayesian |
|--------|------------|----------|
| **Wahrscheinlichkeit** | Langfristige Häufigkeit von Ereignissen | Grad des Glaubens |
| **Parameter** | Behoben, aber unbekannt | Zufallsvariablen mit Verteilungen |
| **Verwendungen** | p-Werte, Konfidenzintervalle, Hypothesentests | Posterior-Verteilungen, glaubwürdige Intervalle |
| **Vorher** | Keine Einbeziehung früherer Überzeugungen | Explizite vorherige Verteilung |
| **Interpretation** | „Wenn wir dieses Experiment viele Male wiederholen würden…“ | „Angesichts der Daten ist die Wahrscheinlichkeit, dass…“ |
| **Stärken** | Objektiv, fundiert, einfach | Intuitive Interpretation, berücksichtigt Vorkenntnisse |
| **Schwächen** | p-Werte werden weitgehend missverstanden | Die Wahl des Priors kann subjektiv sein |
---

## Grundlagen der Kausalinferenz
Korrelation ist keine Kausalität. Aber manchmal muss man wissen, *ob X Y verursacht hat*, und nicht nur, ob sie miteinander verbunden sind.
| Methode | Beschreibung | Wann zu verwenden |
|--------|-------------|-------------|
| **Randomisierte Experimente** | Goldstandard; Zufallszuweisung eliminiert Störfaktoren | Wenn Sie randomisieren können |
| **Differenz-in-Differenzen (DiD)** | Vergleichen Sie zeitliche Veränderungen zwischen Behandlung und Kontrolle | Politische Veränderungen, natürliche Experimente |
| **Regressionsdiskontinuität (RDD)** | Eine Grenzschwelle ausnutzen | Stipendien, Förderschwellen |
| **Instrumentelle Variablen (IV)** | Verwenden Sie ein Instrument, das die Behandlung beeinflusst, aber nicht direkt das Ergebnis | Wenn eine Randomisierung nicht möglich ist |
| **Propensity Score Matching** | Vergleichen Sie behandelte und Kontrolleinheiten anhand der beobachteten Merkmale | Beobachtungsstudien |
---

## Häufige statistische Fehler
| Fehler | Beschreibung |
|---------|-------------|
| **P-Hacking** | Versuchen Sie viele Analysen, bis Sie p < 0,05 | finden
| **HARKing** | Hypothesen aufstellen, nachdem die Ergebnisse bekannt sind |
| **Überlebensbias** | Nur auf Erfolge schauen (z. B. erfolgreiche Unternehmen) |
| **Simpsons Paradoxon** | Der Trend kehrt sich um, wenn Daten aggregiert oder nach Gruppen aufgeteilt werden |
| **Vernachlässigung des Grundzinssatzes** | Ignorieren der A-priori-Wahrscheinlichkeit bei der Interpretation der Ergebnisse |
| **Ökologischer Irrtum** | Ableitung individuellen Verhaltens aus Daten auf Gruppenebene |
| **Verwirrend** | Eine dritte Variable erklärt die beobachtete Beziehung |
| **Überanpassung** | Modell erfasst Rauschen, kein Signal |
---

## Zusammenfassung
Bei statistischen Tests geht es darum, Entscheidungen unter Unsicherheit mit intellektueller Ehrlichkeit zu treffen. Geben Sie immer Ihre Hypothesen an, bevor Sie Daten sammeln. Wählen Sie den richtigen Test für Ihren Datentyp. Geben Sie Effektgrößen an, nicht nur p-Werte. Korrekt für mehrere Vergleiche. Und denken Sie daran: Statistische Signifikanz ist nicht dasselbe wie praktische Signifikanz.