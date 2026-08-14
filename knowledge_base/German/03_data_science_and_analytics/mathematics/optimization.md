---
# Metadata
title: "Optimization"
description: "Linear programming, convex optimization, gradient descent variants, Lagrange multipliers, KKT conditions, duality, integer programming, and heuristic methods"
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
    changes: "Initial deep-dive into optimization"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2027-02-10"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-10"

# Classification
tags: [optimization, linear-programming, convex-optimization, gradient-descent, lagrange-multipliers, kkt, duality, integer-programming]
difficulty_level: "intermediate"
prerequisites:
  - "mathematics.md"
  - "real_analysis.md"
estimated_reading_time: "30 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# Optimierung
Optimierung ist die Mathematik, aus einer Menge möglicher Lösungen die beste Lösung zu finden. Es wird gefragt: Welche Eingabe minimiert (oder maximiert) bei gegebener Funktion und Einschränkungen die Ausgabe? Optimierung ist der Motor des maschinellen Lernens – das Trainieren eines Modells bedeutet die Minimierung einer Verlustfunktion. Es kommt in den Bereichen Operations Research, Wirtschaftswissenschaften, Ingenieurdesign und praktisch jedem quantitativen Bereich vor.
---

## Problemformulierung
Ein allgemeines **Optimierungsproblem** hat die Form:
f(x) minimieren
Vorbehaltlich: gᵢ(x) ≤ 0 (Ungleichheitsbeschränkungen), hⱼ(x) = 0 (Gleichheitsbeschränkungen)
| Begriff | Bedeutung |
|------|---------|
| **Zielfunktion** f(x) | Die zu minimierende (oder zu maximierende) Menge |
| **Entscheidungsvariablen** x | Die Werte, die wir kontrollieren können |
| **Machbare Region** | Menge aller x, die alle Einschränkungen erfüllen |
| **Globales Minimum** | Zulässiges x* mit f(x*) ≤ f(x) für alle zulässigen x |
| **Lokales Minimum** | Zulässiges x* mit f(x*) ≤ f(x) für alle zulässigen x in einer Umgebung |
| **Konvexes Problem** | f ist konvex, der zulässige Bereich ist eine konvexe Menge (lokales Minimum = globales Minimum) |
---

## Lineare Programmierung (LP)
Wenn sowohl das Ziel als auch alle Einschränkungen **linear** sind, handelt es sich bei dem Problem um ein lineares Programm.
### Standardformular
cᵀx minimieren
Voraussetzung: Ax ≤ b, x ≥ 0
wobei c, x ∈ ℝⁿ, A ∈ ℝᵐˣⁿ, b ∈ ℝᵐ.
### Eigenschaften
| Eigentum | Aussage |
|----------|-----------|
| Konvexität | LP ist immer ein konvexes Problem |
| Optimale Lösung | Immer an einem Scheitelpunkt (Eckpunkt) des zulässigen Polytops |
| Existenz | Wenn der zulässige Bereich begrenzt und nicht leer ist, existiert die optimale Lösung |
| Mehrere Optima | Wenn zwei Eckpunkte optimal sind, ist auch jeder Punkt auf der Kante zwischen ihnen optimal |
### Die Simplex-Methode
Die **Simplex-Methode** (Dantzig, 1947) bewegt sich entlang der Kanten des zulässigen Polytops von Scheitelpunkt zu Scheitelpunkt und verbessert dabei immer das Ziel, bis das Optimum erreicht wird.
| Eigentum | Wert |
|----------|-------|
| Worst-Case-Zeit | O(2ⁿ) (exponentiell – in der Praxis selten) |
| Durchschnittliche Fallzeit | Polynom für die meisten praktischen Probleme |
| Schlüsselidee | Zum benachbarten Scheitelpunkt mit besserem Zielwert wechseln |
**Algorithmus (Übersicht):**
1. Beginnen Sie mit einer grundsätzlich zulässigen Lösung (Scheitelpunkt des Polytops)
2. Wählen Sie eine Einstiegsvariable (eine, die das Ziel verbessert)
3. Wählen Sie eine Austrittsvariable (Machbarkeit beibehalten)
4. Pivot: Zum neuen Scheitelpunkt wechseln
5. Wiederholen, bis keine Verbesserungsrichtung mehr vorhanden ist
### Methoden für innere Punkte
Alternative zu Simplex: Annäherung an das Optimum innerhalb des realisierbaren Bereichs.
| Eigentum | Wert |
|----------|-------|
| Worst-Case-Zeit | Polynom (O(n³·⁵) für einige Varianten) |
| Praktische Leistung | Konkurriert mit Simplex bei großen Problemen |
| Schlüsselidee | Folgen Sie einem „zentralen Weg“ durch das Innere |
### Bearbeitetes LP-Beispiel
**Problem:** Eine Fabrik produziert Stühle (x₁) und Tische (x₂).
- Gewinn: 30 $ pro Stuhl, 50 $ pro Tisch
- Holz: 2x₁ + 4x₂ ≤ 100 (Brettfüße verfügbar)
- Arbeitsaufwand: x₁ + 3x₂ ≤ 60 (verfügbare Stunden)
- Maximieren: 30x₁ + 50x₂
**Lösung (grafische Methode für 2 Variablen):**
- Eckpunkte der zulässigen Region: (0,0), (30,0), (40,10), (0,20)
- Bewerten Sie das Ziel an jedem Scheitelpunkt:
  - (0,0): Gewinn = 0
  - (30,0): Gewinn = 900
  - (40,10): Gewinn = 1700 ← optimal
  - (0,20): Gewinn = 1000
- **Optimal:** x₁ = 40 Stühle, x₂ = 10 Tische, Gewinn = 1700 $
---

## Konvexe Optimierung
Ein Problem ist **konvex**, wenn die Zielfunktion konvex ist und der zulässige Bereich eine konvexe Menge ist.
### Konvexe Mengen und Funktionen
| Konzept | Definition |
|---------|------------|
| **Konvexe Menge** | Für jedes x, y in der Menge und t ∈ [0,1]: tx + (1−t)y ist auch in der Menge |
| **Konvexe Funktion** | f(tx + (1−t)y) ≤ tf(x) + (1−t)f(y) für alle t ∈ [0,1] |
| **Streng konvex** | Die Ungleichung ist streng für t ∈ (0,1) und x ≠ y |
**Schlüsseleigenschaft:** Bei der konvexen Optimierung ist jedes lokale Minimum ein globales Minimum.
### Gemeinsame konvexe Funktionen
| Funktion | Konvex? | Wo |
|----------|---------|-------|
| ax + b (linear) | Ja (und konkav) | Überall |
| x² | Ja | ℝ |
| eˣ | Ja | ℝ |
| −log(x) | Ja | x > 0 |
| \|x\|ᵖ (p ≥ 1) | Ja | ℝⁿ |
| max(f₁, f₂) wenn f₁, f₂ konvex | Ja | Schnittpunkt von Domänen |
### Gefälleabstieg
Der grundlegendste Optimierungsalgorithmus im maschinellen Lernen.
**Aktualisierungsregel:** x_{k+1} = x_k − α∇f(x_k)
wobei α > 0 die **Lernrate** (Schrittgröße) ist.
| Variante | Aktualisierungsregel | Vorteil |
|---------|-------------|-----------|
| **Chargen-GD** | x ← x − α∇f(x) | Stabile Konvergenz |
| **Stochastischer GD (SGD)** | x ← x − α∇fᵢ(x) (eine Stichprobe) | Schnell pro Iteration, entgeht lokalen Minima |
| **Mini-Charge SGD** | x ← x − α(1/|B|)Σᵢ∈B ∇fᵢ(x) | Gleichgewicht zwischen Batch und Stochastik |
| **Momentum** | v ← βv − α∇f(x); x ← x + v | Beschleunigt durch flache Regionen |
| **Adam** | Adaptive Lernraten pro Parameter | Funktioniert sofort gut für Deep Learning |
| **RMSprop** | Skalieren Sie die Lernrate anhand des laufenden Durchschnitts der Gradientengröße | Gut für RNNs |
### Konvergenzraten
| Methode | Konvex f | Stark konvex f |
|--------|----------|-------------------|
| Gefälleabstieg | O(1/k) | O((1−μ/L)ᵏ) (linear) |
| SGD | O(1/√k) | O(1/k) |
| Beschleunigter GD (Nesterov) | O(1/k²) | O((1−√(μ/L))ᵏ) |
wobei k = Iterationsanzahl, μ = starker Konvexitätsparameter, L = Lipschitz-Konstante.
### Auswahl der Lernrate
| Strategie | Beschreibung |
|----------|-------------|
| Festes α | Einfach, kann aber divergieren (zu groß) oder langsam konvergieren (zu klein) |
| Zeilensuche | Finden Sie α, das f(x − α∇f(x)) entlang der Gradientenrichtung | minimiert
| Zerfallspläne | α_t = α₀ / (1 + βt) oder α_t = α₀ · βᵗ |
| Aufwärmen | Klein anfangen, steigern, dann abklingen (üblich beim Transformer-Training) |
| Adaptiv (Adam) | Lernraten pro Parameter basierend auf Gradientenstatistiken |
---

## Eingeschränkte Optimierung
### Lagrange-Multiplikatoren
Für das Problem: Minimieren Sie f(x) unter der Bedingung, dass h(x) = 0.
**Lagrange:** L(x, λ) = f(x) + λh(x)
Im Optimum: ∇ₓL = 0 und ∇_λL = 0 (was h(x) = 0 ergibt).
**Arbeitsbeispiel:** Minimieren Sie f(x,y) = x² + y² unter der Bedingung, dass x + y = 1 ist.
- L = x² + y² + λ(x + y − 1)
- ∂L/∂x = 2x + λ = 0 → x = −λ/2
- ∂L/∂y = 2y + λ = 0 → y = −λ/2
- Einschränkung: x + y = 1 → −λ = 1 → λ = −1
- Lösung: x = 1/2, y = 1/2, f = 1/2
### KKT-Bedingungen
Die **Karush-Kuhn-Tucker (KKT)-Bedingungen** verallgemeinern Lagrange-Multiplikatoren auf Ungleichheitsbeschränkungen.
Für: Minimiere f(x) unter der Bedingung, dass gᵢ(x) ≤ 0, hⱼ(x) = 0.
**Lagrange:** L(x, λ, ν) = f(x) + Σᵢ λᵢgᵢ(x) + Σⱼ νⱼhⱼ(x)
**KKT-Bedingungen** (notwendig für Optimalität):
| Zustand | Gleichung |
|-----------|----------|
| Stationarität | ∇ₓL = 0 |
| Ursprüngliche Machbarkeit | gᵢ(x) ≤ 0, hⱼ(x) = 0 |
| Doppelte Machbarkeit | λᵢ ≥ 0 |
| Komplementäre Lockerheit | λᵢgᵢ(x) = 0 für alle i |
**Komplementäre Slackness** bedeutet: Wenn die Einschränkung gᵢ nicht aktiv ist (gᵢ(x) < 0), dann ist λᵢ = 0 (die Einschränkung hat keinen Einfluss auf die Lösung).
Für konvexe Probleme, die die Slater-Bedingung erfüllen, sind KKT-Bedingungen sowohl notwendig als auch ausreichend.
---

## Dualität
Jedem Optimierungsproblem (dem **Primalproblem**) ist ein **duales** Problem zugeordnet.
### Schwache und starke Dualität
| Konzept | Aussage |
|---------|-----------|
| **Doppelfunktion** | g(λ, ν) = infₓ L(x, λ, ν) |
| **Doppelproblem** | Maximiere g(λ, ν) unter der Bedingung, dass λ ≥ 0 |
| **Schwache Dualität** | Dual optimal ≤ Primal optimal (gilt immer) |
| **Starke Dualität** | Dual optimal = Primal optimal (gilt für konvexe Probleme mit Slater-Bedingung) |
| **Dualitätslücke** | Primal optimal − Dual optimal (Null unter starker Dualität) |
### Warum Dualität wichtig ist
| Bewerbung | Wie Dualität hilft |
|-------------|-------------------|
| Untergrenzen | Dual bescheinigt, wie gut die Urlösung ist |
| SVMs | Der Dual des SVM-Problems führt zum Kernel-Trick |
| Sensitivitätsanalyse | Duale Variablen messen, wie stark sich das Optimum ändert, wenn die Einschränkungen gelockert werden |
| Zersetzung | Große Probleme können über das duale | in kleinere Teilprobleme zerlegt werden
---

## Ganzzahlprogrammierung
Wenn einige oder alle Variablen **Ganzzahlen** sein müssen, wird das Problem viel schwieriger (im Allgemeinen NP-schwer).
### Typen
| Geben Sie | ein Beschreibung |
|------|-------------|
| Reine IP | Alle Variablen müssen ganze Zahlen sein |
| Gemischte IP (MIP) | Einige Variablen sind ganzzahlig, andere kontinuierlich |
| Binäre IP | Variablen beschränkt auf {0, 1} |
### Lösungsmethoden
| Methode | Idee |
|--------|------|
| **Verzweigung** | In Teilprobleme aufteilen, LP-Relaxierungen lösen, bereinigen |
| **Flugzeuge schneiden** | Fügen Sie lineare Einschränkungen hinzu, um die LP-Relaxierung | zu verschärfen
| **Verzweigen und schneiden** | Kombinieren Sie Branch-and-Bound mit Schnittebenen |
| **Heuristik** | Greedy, lokale Suche, simuliertes Tempern für Näherungslösungen |
---

## Heuristische und metaheuristische Methoden
Wenn eine exakte Optimierung nicht möglich ist, finden Heuristiken gute (nicht unbedingt optimale) Lösungen.
| Methode | Schlüsselidee | Am besten für |
|--------|----------|----------|
| **Gefälleabstieg** | Folgen Sie dem steilsten Abstieg | Glatte, differenzierbare Funktionen |
| **Newtons Methode** | Informationen zweiter Ordnung (Krümmung) verwenden | Glatte, gut konditionierte Probleme |
| **Simuliertes Glühen** | Schlechtere Lösungen mit abnehmender Wahrscheinlichkeit akzeptieren | Globale Optimierung, kombinatorisch |
| **Genetische Algorithmen** | Entwickeln Sie eine Population mithilfe von Selektion, Crossover und Mutation | Multiobjektiv, nicht differenzierbar |
| **Partikelschwarm** | Agenten erkunden den Weltraum, beeinflusst von den bekanntesten Positionen | Kontinuierlich, nicht konvex |
| **Bayesianische Optimierung** | Ersatzmodell erstellen, Erfassungsfunktion verwenden | Teure Black-Box-Funktionen (Hyperparameter-Tuning) |
### Newtons Methode zur Optimierung
**Aktualisierungsregel:** x_{k+1} = x_k − [H(x_k)]⁻¹ ∇f(x_k)
wobei H die Hessesche Matrix (Matrix der zweiten Ableitungen) ist.
| Eigentum | Wert |
|----------|-------|
| Konvergenzrate | Quadratisch (nahezu optimal) |
| Kosten pro Iteration | O(n³) für die hessische Inversion |
| Erfordert | Zweimal differenzierbar, positiv definit hessisch |
| Quasi-Newton (BFGS) | Ungefähres Hessisches aus Farbverläufen | O(n²) pro Iteration |
---

## Relevanz für maschinelles Lernen und Datenwissenschaft
| Optimierungskonzept | Bewerbung |
|-------|-------------|
| Gefälleabstieg | Training neuronaler Netze, logistische Regression, jedes differenzierbare Modell |
| SGD und Varianten | Groß angelegtes ML (Mini-Batch-Training), Online-Lernen |
| Adam, RMSprop | Standardoptimierer für Deep Learning |
| Konvexe Optimierung | SVMs, logistische Regression, LASSO, Ridge (garantiertes globales Optimum) |
| Lagrange-Multiplikatoren | Eingeschränktes Lernen, faires ML, Ressourcenzuweisung |
| KKT-Bedingungen | SVM dual ableiten, Einschränkungsaktivität verstehen |
| Dualität | SVM-Kernel-Trick, Sensitivitätsanalyse, Zerlegungsmethoden |
| Lineare Programmierung | Ressourcenallokation, Portfoliooptimierung, Netzwerkfluss |
| Ganzzahlprogrammierung | Funktionsauswahl (binär), Planung, kombinatorische Probleme |
| Bayesianische Optimierung | Hyperparameter-Tuning (Optuna, Hyperopt) |
| Newton/Quasi-Newton | Methoden zweiter Ordnung für kleine bis mittlere Probleme (L-BFGS) |
---

## Zusammenfassung
| Methode | Problemtyp | Garantien | Maßstab |
|--------|-------------|------------|-------|
| Simplex | Lineare Programmierung | Exaktes Optimum | Millionen von Variablen |
| Innenpunkt | Konvex (LP, QP, SOCP) | Exaktes Optimum | Großformat |
| Gefälleabstieg | Glatt, uneingeschränkt | Konvergiert zu lokalem min | Sehr groß (Deep Learning) |
| SGD | Großes empirisches Risiko | Konvergiert (mit Zerfall) | Riesige Datensätze |
| Newton / BFGS | Glatt, zweifach differenzierbar | Quadratische Konvergenz | Klein bis mittel |
| KKT / Lagrange | Eingeschränkt (konvex) | Exakt unter Bedingungen | Mittel |
| Verzweigt und gebunden | Ganzzahlprogrammierung | Exaktes Optimum | Klein bis mittel |
| Heuristik | Beliebig (nicht konvex, kombinatorisch) | Keine Garantie | Variiert |
Optimierung ist wohl das wichtigste mathematische Werkzeug beim maschinellen Lernen. Jedes Modell, das Sie trainieren – von der linearen Regression bis hin zu großen Sprachmodellen – beinhaltet die Lösung eines Optimierungsproblems. Wenn Sie verstehen, wann ein Problem konvex ist (garantiertes globales Optimum), wann der Gradientenabstieg konvergiert und wie mit Einschränkungen umgegangen wird, erhalten Sie die theoretische Grundlage zum Entwerfen, Debuggen und Verbessern von Lernalgorithmen.