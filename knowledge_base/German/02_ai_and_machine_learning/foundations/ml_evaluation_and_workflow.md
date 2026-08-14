<!--
---
# Metadata
title: "Machine Learning Evaluation and Workflow"
description: "ML pipelines, metrics, best practices"
category: "AI and Machine Learning"
subcategory: "Foundations"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "Nepoznato-Dev"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.1"
    date: "2026-08-09"
    author: "Nepoznato-Dev"
    changes: "Moved to foundations/ subfolder; added subcategory field"
  - version: "1.0.0"
    date: "2026-08-05"
    author: "Nepoznato-Dev"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-09"
review_date: "2027-02-05"
reviewed_by: "AI & Machine Learning Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [ml, evaluation, workflow, ai-and-machine-learning]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "8 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Bewertung und Workflow des maschinellen Lernens
Ein praktischer Leitfaden zum ML-Lebenszyklus – von der Problemstellung bis zur Produktionsüberwachung – mit Schwerpunkt auf Metriken, Validierung und Debugging.
---

## Der ML-Workflow (CRISP-ML)
1. **Geschäftsverständnis**: Definieren Sie die Ziel- und Erfolgskriterien.
2. **Datenverständnis**: Verfügbare Daten untersuchen, Qualitätsprobleme identifizieren.
3. **Datenvorbereitung**: Daten bereinigen, transformieren und aufteilen.
4. **Modellierung**: Modelle trainieren, Hyperparameter optimieren.
5. **Bewertung**: Bewerten Sie die Leistung anhand von Kennzahlen.
6. **Bereitstellung**: Stellen Sie das Modell in der Produktion bereit.
7. **Überwachung**: Verfolgen Sie Drift, Leistung und Anomalien.
Dies ist eine iterative Schleife – Sie werden frühere Schritte auf der Grundlage der Bewertungsergebnisse noch einmal durchgehen.
---

## Datenaufteilung
### Trainings-/Validierungs-/Testaufteilung
- **Trainingssatz** (~70 %): Wird zur Anpassung der Modellparameter verwendet.
- **Validierungssatz** (~15 %): Wird zum Optimieren von Hyperparametern und zum Auswählen von Modellvarianten verwendet.
- **Testsatz** (~15 %): Wird nur einmal ganz am Ende verwendet, um die Generalisierungsleistung abzuschätzen.
**Wichtig:** Der Testsatz muss bis zur endgültigen Auswertung völlig unberührt bleiben, um Datenlecks zu vermeiden.
### Kreuzvalidierung (k-fach)
Verwenden Sie für kleine Datensätze die k-fache Kreuzvalidierung: Teilen Sie die Daten in k Falten auf, trainieren Sie auf k-1, validieren Sie auf den verbleibenden und wiederholen Sie k-mal. Durchschnittliche Leistung. k=5 oder k=10 ist üblich.
### Schichtaufteilung
Verwenden Sie für die Klassifizierung mit unausgeglichenen Klassen geschichtete Aufteilungen, um die Klassenanteile in jeder Teilmenge beizubehalten.
### Zeitbasierte Aufteilung
Teilen Sie Zeitreihendaten chronologisch auf (Training auf Vergangenheit, Test auf Zukunft) und nicht zufällig.
---

## Bewertungsmetriken
### Klassifizierungsmetriken
| Metrisch | Was es misst | Am besten geeignet für |
|--------|----|---------------|
| **Genauigkeit** | (TP + TN) / (TP + TN + FP + FN) | Ausgewogene Datensätze |
| **Präzision** | TP / (TP + FP) | Wenn Fehlalarme kostspielig sind (z. B. Spam-Erkennung) |
| **Rückruf** | TP / (TP + FN) | Wenn falsch negative Ergebnisse kostspielig sind (z. B. Krebsvorsorge) |
| **F1-Punktzahl** | Harmonisches Mittel von Präzision und Erinnerung | Unausgeglichene Datensätze, Einzelzahlmetrik |
| **AUC-ROC** | Fläche unter der ROC-Kurve; Kompromiss zwischen TPR und FPR | Allgemeine Leistung des Klassifikators unabhängig vom Schwellenwert |
| **AUC-PR** | Fläche unter der Precision-Recall-Kurve | Stark unausgeglichene Datensätze |
**Definitionen:**
- TP = Richtig positiv
- TN = Richtig negativ
- FP = False Positive (Typ-I-Fehler)
- FN = Falsch Negativ (Fehler Typ II)
### Regressionsmetriken
| Metrisch | Was es misst | Empfindlichkeit gegenüber Ausreißern |
|--------|----|-----------|
| **MSE** (mittlerer quadratischer Fehler) | Durchschnittliche quadrierte Differenz | Hoch |
| **RMSE** (Root Mean Squared Error) | Quadratwurzel von MSE (gleiche Einheiten wie Ziel) | Hoch |
| **MAE** (mittlerer absoluter Fehler) | Durchschnittliche absolute Differenz | Niedrig |
| **R²** (Bestimmtheitskoeffizient) | Anteil der erklärten Varianz | Keine direkt, aber indirekt empfindlich gegenüber Ausreißern |
### Ranking- und Abrufmetriken
- **Precision@k**: Anteil relevanter Elemente unter den Top-K-Empfehlungen.
- **Recall@k**: Bruchteil aller relevanten Elemente, die in top-k erscheinen.
- **NDCG** (Normalised Discounted Cumulative Gain): Berücksichtigt die Positionsrelevanz.
- **Trefferquote**: Ob ein relevanter Artikel im Top-K erscheint.
### Generative / LLM-Metriken
- **Perplexität**: Wie „überrascht“ das Model von einem vorgehaltenen Text ist (weniger ist besser).
- **BLEU**: N-Gramm-Überlappung mit Referenzübersetzungen (präzisionsorientiert).
- **ROUGE**: Rückruforientierte Überlappung zur Zusammenfassung.
- **BERTScore**: Semantische Ähnlichkeit durch kontextuelle Einbettungen (robuster als BLEU).
- **METEOR**: Passt sich an WordNet-Synonyme und -Stämme an.
---

## Fallstricke bei der Bewertung
### Datenleck
Tritt auf, wenn Informationen aus dem Testsatz unbeabsichtigt das Training beeinflussen.
- **Verhindern:** Verwenden Sie niemals Testdaten für Feature-Engineering, Normalisierung oder Hyperparameter-Optimierung.
- **Erkennen:** Wenn Ihr Modell verdächtig hohe Werte erzielt, vermuten Sie ein Leck.
### Überanpassung
Das Modell schneidet bei Trainingsdaten gut ab, bei Validierung/Tests jedoch schlecht.
- **Abschwächen:** Nutzen Sie Regularisierung, frühzeitiges Stoppen, vereinfachen Sie die Architektur oder sammeln Sie mehr Daten.
### Unteranpassung
Das Modell schneidet sowohl beim Training als auch bei der Validierung schlecht ab.
- **Abschwächen:** Verwenden Sie ein komplexeres Modell, fügen Sie Funktionen hinzu oder reduzieren Sie die Regularisierung.
### Unausgeglichene Daten
- **Abmildern:** Verwenden Sie Klassengewichtungen, Überabtastung (SMOTE), Unterabtastung oder verwenden Sie geeignete Metriken (F1, AUC-PR) anstelle von Genauigkeit.
### Zeitliche Drift (Konzeptdrift)
Die Beziehung zwischen Merkmalen und Ziel ändert sich im Laufe der Zeit.
- **Abmildern:** Regelmäßig neu trainieren, Leistung überwachen, Abweichungserkennungsalgorithmen verwenden.
---

## Hyperparameter-Tuning
- **Gittersuche**: Probieren Sie alle Kombinationen eines vordefinierten Satzes von Hyperparametern ausführlich aus. Einfach, aber rechenintensiv.
- **Zufallssuche**: Probieren Sie zufällige Kombinationen aus Verteilungen aus. Effizienter als die Rastersuche für hochdimensionale Räume.
- **Bayesianische Optimierung**: Erstellt ein probabilistisches Modell der Zielfunktion und wählt Hyperparameter intelligent aus. Bibliotheken: Optuna, Hyperopt, scikit-optimise.
- **Automatisiertes Tuning**: Verwenden Sie Tools wie Optuna, Ray Tune oder Weights & Biases Sweeps für verteiltes Tuning.
**Empfohlene Suchbereiche für gängige Hyperparameter:**
| Parameter | Empfohlener Bereich (Log-Skala) |
|-----------|--------------|
| Lernrate | 1e-5 bis 1e-1 |
| Losgröße | 16, 32, 64, 128, 256 |
| Anzahl der Schichten (NN) | 2 bis 6 |
| Anzahl der Neuronen (NN) | 32 bis 1024 |
| Regularisierung (L2) | 1e-6 bis 1e-2 |
| Baumtiefe (XGBoost) | 3 bis 12 |
---

## Modellauswahl und Validierung
1. **Basismodell**: Beginnen Sie mit einer einfachen Heuristik oder einem einfachen Modell (z. B. logistische Regression, Mittelwertprädiktor), um eine Untergrenze festzulegen.
2. **Kandidatenmodelle**: Trainieren Sie mehrere Modellfamilien (z. B. Random Forest, XGBoost, Neural Network).
3. **Kreuzvalidierung** jedes Kandidaten im Validierungssatz.
4. **Vergleichen Sie die Messwerte** (mit Konfidenzintervallen) und wählen Sie den besten Kandidaten aus.
5. **Abschließende Bewertung** des ausgehaltenen Testsatzes.
6. **Fehleranalyse**: Schauen Sie sich Beispiele an, bei denen das Modell falsch liegt. Identifizieren Sie Muster (z. B. seltene Klassen, mehrdeutige Eingaben) und geben Sie Erkenntnisse zurück in die Datenvorbereitung oder das Feature-Engineering.
---

## Bereitstellung und Überwachung
### Serviermuster
- **Batch-Inferenz**: Große Datenmengen offline verarbeiten (z. B. nächtliche Empfehlungen).
- **Online-Inferenz**: Echtzeitvorhersagen über API (z. B. Kreditbewertung, Betrugserkennung).
- **Streaming-Inferenz**: Ereignisgesteuert, Echtzeit mit geringer Latenz (z. B. IoT-Sensorwarnungen).
### Modellüberwachung
- **Leistungsüberwachung**: Verfolgen Sie die Genauigkeit/F1 im Zeitverlauf anhand von Live-Daten (sofern Ground Truth verfügbar ist).
- **Datendrift**: Überwachen Sie Änderungen in der Verteilung der Eingabemerkmale (z. B. mithilfe des PSI – Population Stability Index).
- **Konzeptdrift**: Überwachen Sie Änderungen in der Beziehung zwischen Eingaben und Ausgaben.
- **Vorhersagedrift**: Verfolgen Sie die Verteilung der vorhergesagten Ergebnisse.
- **Latenz und Durchsatz**: Stellen Sie sicher, dass SLAs (Service Level Agreements) eingehalten werden.
### Protokollierung und Warnung
- Protokollieren Sie alle Vorhersageanfragen und -antworten (mit Anonymisierung).
- Legen Sie Benachrichtigungen fest für:
  - Deutlicher Leistungsabfall.
  - Hoher Prozentsatz fehlender oder ungültiger Eingaben.
  - Modellausgaben außerhalb der erwarteten Grenzen.
### Modellversionierung und Registrierung
- Verwenden Sie eine Modellregistrierung (z. B. MLflow, Weights & Biases, Sagemaker Model Registry), um Modelle, Metadaten und Bewertungsergebnisse zu speichern und zu versionieren.
- Speichern Sie den Trainingscode und die Datenversion (über DVC oder Git LFS) neben dem Modell.
---

## Praktische Workflow-Checkliste
- [ ] Problem formuliert und Erfolgsmetrik definiert.
- [ ] Datenexploration durchgeführt (fehlende Werte, Ausreißer, Verteilung).
- [ ] Trainings-/Validierungs-/Testaufteilung erstellt (bei Bedarf geschichtet).
- [ ] Basismodell erstellt.
- [ ] Kandidatenmodelle trainiert und validiert.
- [ ] Hyperparameter optimiert.
- [ ] Bestes Modell, ausgewählt durch Kreuzvalidierung.
- [ ] Endgültige Bewertung des Testsatzes.
- [ ] Fehleranalyse durchgeführt.
- [ ] Bereitstellungsplan bereit (für die Infrastruktur).
- [ ] Überwachungs-Dashboard eingerichtet.
- [ ] Dokumentation (Datenkarte, Modellkarte) abgeschlossen.