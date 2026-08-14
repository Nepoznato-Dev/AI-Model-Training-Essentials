<!--
---
# Metadata
title: "Ensemble Methods"
description: "Bagging, boosting, stacking, voting, random forests, XGBoost"
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
tags: [ensemble, methods, data-science-and-analytics]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "7 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Ensemble-Methoden
Ensemble-Methoden kombinieren mehrere Modelle des maschinellen Lernens, um bessere Vorhersagen zu erzielen, als jedes einzelne Modell allein erreichen könnte. Die Intuition ist einfach: Wenn Sie über mehrere Modelle verfügen, die jeweils einigermaßen genau sind, aber unterschiedliche Fehler machen, werden durch die Kombination ihrer Vorhersagen einzelne Fehler ausgeglichen und ein belastbareres Ergebnis erzielt. Ensembles stehen hinter den meisten wettbewerbsfähigen Lösungen für maschinelles Lernen und gehören nach wie vor zu den zuverlässigsten Techniken in Produktionssystemen.
---

## Warum Ensembles funktionieren
| Prinzip | Beschreibung |
|-----------|-------------|
| **Weisheit der Massen** | Mehrere unvollständige Schätzungen sind gemittelt besser als jede einzelne Schätzung |
| **Bias-Varianz-Kompromiss** | Ensembles können die Varianz (Bagging) oder die Verzerrung (Boosting) reduzieren, ohne das andere zu opfern
| **Fehlervielfalt** | Wenn Modelle unterschiedliche Fehler machen, werden durch die Kombination einzelne Fehler aufgehoben |
| **Entscheidungsgrenzenglättung** | Mehrere Modelle schaffen eine robustere Entscheidungsoberfläche als ein Modell |
---

## Bagging (Bootstrap-Aggregation)
### Wie es funktioniert
| Schritt | Beschreibung |
|------|-------------|
| **1. Bootstrap-Sampling** | Ziehen Sie mehrere Zufallsstichproben (mit Ersetzung) aus den Trainingsdaten |
| **2. Zugbasismodelle** | Trainieren Sie ein Modell für jedes Bootstrap-Beispiel (normalerweise Entscheidungsbäume) |
| **3. Aggregat** | Zur Regression: durchschnittliche Vorhersagen. Zur Einstufung: Mehrheitsbeschluss |
### Hauptmerkmale
| Charakteristisch | Beschreibung |
|---------------|-------------|
| **Reduziert die Varianz** | Mittelung glättet individuelle Modellschwankungen |
| **Paralleles Training** | Jedes Basismodell ist unabhängig; können gleichzeitig trainiert werden |
| **Out-of-Bag-Bewertung** | In einigen Bootstrap-Beispielen wird jedes Beispiel weggelassen. Verwenden Sie diese zur Validierung |
| **Dekorrelation** | Zufällige Merkmalsauswahl bei jeder Teilung verringert die Korrelation zwischen Bäumen |
### Zufälliger Wald
| Aspekt | Beschreibung |
|--------|-------------|
| **Basislerner** | Entscheidungsbäume |
| **Schlüsselzusatz** | Berücksichtigen Sie bei jeder Aufteilung nur eine zufällige Teilmenge von Features (normalerweise sqrt(n_features)) |
| **Warum es funktioniert** | Zufällige Merkmalsauswahl dekorreliert Bäume und macht das Ensemble robuster |
| **Hyperparameter** | Anzahl der Bäume; maximale Tiefe; Mindestproben pro Blatt; maximale Funktionen |
| **Stärken** | Verarbeitet hochdimensionale Daten; robust gegenüber Ausreißern; Bietet Feature-Wichtigkeit |
| **Schwächen** | Weniger interpretierbar als Einzelbäume; kann bei verrauschten Regressionsaufgaben überpassen |
---

## Boosten
### Wie es funktioniert
| Schritt | Beschreibung |
|------|-------------|
| **1. Erstes Modell trainieren** | Trainieren Sie ein Basismodell (häufig ein flacher Baum/„Stumpf“) anhand der Daten |
| **2. Fehler identifizieren** | Finden Sie heraus, in welchen Fällen das Modell einen Fehler gemacht hat |
| **3. Nächstes Modell trainieren** | Trainieren Sie ein neues Modell, das sich auf die Fehler konzentriert (neu gewichtet oder restangepasst) |
| **4. Nacheinander kombinieren** | Jedes neue Modell korrigiert die akkumulierten Fehler aller vorherigen Modelle |
| **5. Wiederholen** | Fahren Sie für eine bestimmte Anzahl von Runden fort |
### Boosting-Algorithmen
| Algorithmus | Verlustfunktion | Hauptmerkmal |
|-----------|--------------|-------------|
| **AdaBoost** | Exponentiell | Gewichtet falsch klassifizierte Instanzen neu; einfach; lärmempfindlich |
| **Gradientenverstärkung** | Jeder differenzierbare Verlust | Passt Residuen an (Verlustgradient); flexibler |
| **XGBoost** | Regularisierte Gradientenverstärkung | L1/L2-Regularisierung; Gradienten zweiter Ordnung; Hardwareoptimierung |
| **LightGBM** | Gradientenbasierte einseitige Probenahme | Blattweises Wachstum; histogrammbasiert; schnell bei großen Datensätzen |
| **CatBoost** | Bestellte Verstärkung | Behandelt kategoriale Funktionen nativ; reduziert Überanpassung |
### Boosting vs. Bagging
| Dimension | Absacken | Boosten |
|-----------|---------|----------|
| **Schulung** | Parallel | Sequentielle |
| **Fokus** | Reduziert die Varianz | Reduziert Voreingenommenheit |
| **Basismodelle** | Hohe Varianz, geringer Bias (tiefe Bäume) | Geringe Varianz, hoher Bias (flache Bäume/Stümpfe) |
| **Kombination** | Gleiches Gewicht | Nach Leistung gewichtet |
| **Überanpassung** | Weniger anfällig | Kann bei zu vielen Runden überpassen |
| **Geräuschempfindlichkeit** | Robust | Empfindlich gegenüber verrauschten Daten |
---

## Stapeln
### Wie es funktioniert
| Schritt | Beschreibung |
|------|-------------|
| **1. Zugbasismodelle** | Trainieren Sie verschiedene Modelle (z. B. Random Forest, SVM, neuronales Netzwerk, Gradient Boosting) |
| **2. Vorhersagen generieren** | Out-of-Fold-Vorhersagen (Kreuzvalidierung) als Eingabemerkmale verwenden |
| **3. Metamodell trainieren** | Trainieren Sie ein Modell der zweiten Ebene anhand der Vorhersagen der Basismodelle |
| **4. Endgültige Vorhersage** | Basismodelle sagen voraus; Meta-Modell kombiniert ihre Vorhersagen |
### Best Practices für das Stapeln
| Üben | Grund |
|----------|--------|
| **Verschiedene Basismodelle verwenden** | Unterschiedliche Algorithmen machen unterschiedliche Fehler; Diversität ist der springende Punkt |
| **Kreuzvalidierung für Basisvorhersagen verwenden** | Verhindert, dass das Metamodell lernt, überangepasste Basismodelle auszunutzen |
| **Halten Sie das Metamodell einfach** | Logistische Regression oder flacher Baum; Die Basismodelle erledigen die schwere Arbeit |
| **Rohfunktionen in Metamodell einbeziehen** | Manchmal hilfreich, um dem Metamodell auch Zugriff auf Originalfunktionen zu gewähren |
---

## Abstimmung und Mittelwertbildung
### Harte Abstimmung (Klassifizierung)
| Modell | Vorhersage |
|-------|-----------|
| Modell A | Klasse 1 |
| Modell B | Klasse 0 |
| Modell C | Klasse 1 |
| **Mehrheitsvotum** | **Klasse 1** |
### Soft Voting (Klassifizierung)
| Modell | P(Klasse 0) | P(Klasse 1) |
|-------|-----------|-----------|
| Modell A | 0,3 | 0,7 |
| Modell B | 0,6 | 0,4 |
| Modell C | 0,4 | 0,6 |
| **Durchschnitt** | **0,43** | **0,57** |
| **Vorhersage** | | **Klasse 1** |
### Gewichtete Mittelung
| Modell | Gewicht | Vorhersage |
|-------|--------|-----------|
| Modell A | 0,5 | 0,8 |
| Modell B | 0,3 | 0,6 |
| Modell C | 0,2 | 0,9 |
| **Gewichteter Durchschnitt** | | 0,5×0,8 + 0,3×0,6 + 0,2×0,9 = 0,76 |
---

## Praktische Anleitung
### Wann welches Ensemble verwendet werden sollte
| Szenario | Empfohlene Methode |
|----------|-----|
| **Schnelle Grundlinie; tabellarische Daten** | Zufälliger Wald |
| **Maximale Genauigkeit; tabellarische Daten** | XGBoost / LightGBM / CatBoost |
| **Verrauschte Daten** | Bagging (durch die Verstärkung wird der Lärm übertrieben) |
| **Interpretierbarkeit erforderlich** | Einzelmodell oder kleines Ensemble mit Merkmalsbedeutung |
| **Verschiedene Modelltypen** | Stapeln oder abstimmen |
| **Online-Lernen** | Streaming-Ensemble-Methoden; adaptives Boosting |
| **Unausgeglichene Daten** | Ausgewogener Zufallswald; kostensensitives Boosten |
### Ensemble-Diversity-Strategien
| Strategie | Beschreibung |
|----------|-------------|
| **Verschiedene Algorithmen** | Kombinieren Sie baumbasierte, lineare und neuronale Modelle |
| **Verschiedene Funktionen** | Trainieren Sie Modelle auf verschiedenen Feature-Teilmengen |
| **Verschiedene Datenteilmengen** | Absacken; Unterabtastung |
| **Verschiedene Hyperparameter** | Gleicher Algorithmus mit unterschiedlichen Konfigurationen |
| **Verschiedene Zeiträume** | Trainieren Sie in verschiedenen Zeitfenstern |
---

## Zusammenfassung
Ensemble-Methoden funktionieren, weil sie mehrere unvollständige Modelle zu einem einzigen robusten Prädiktor kombinieren. Bagging (zufällige Wälder) reduziert die Varianz durch paralleles Training von Modellen anhand von Bootstrap-Stichproben und Mittelwertbildung. Boosting (XGBoost, LightGBM, CatBoost) reduziert Verzerrungen, indem Modelle nacheinander trainiert werden, wobei jedes die vorherigen Fehler korrigiert. Stacking verwendet ein Metamodell, um verschiedene Basismodelle zu kombinieren. Abstimmung und Mittelwertbildung sind die einfachsten Ensembles. Der rote Faden ist die Vielfalt: Ensembles funktionieren am besten, wenn ihre Komponentenmodelle individuell sinnvoll sind, aber unterschiedliche Fehler machen. In der Praxis ist die Gradientenverstärkung bei tabellarischen Daten häufig der leistungsstärkste Einzelansatz, während das Stapeln verschiedener Modelle die Genauigkeit bei Wettbewerben und Anwendungen mit hohen Einsätzen weiter steigert.