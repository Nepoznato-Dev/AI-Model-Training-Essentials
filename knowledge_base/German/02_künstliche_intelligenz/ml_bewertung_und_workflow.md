<!-- 
This file was automatically translated from English to German.
Source: ml_evaluation_and_workflow.md
Note: Technical terms, code examples, and proper nouns may remain in English.
Für Verbesserungen der Genauigkeit bitten wir um Beiträge via Pull Requests.
-->

# Maschinelles Lernen Evaluation und Workflow

Ein praktischer Leitfaden für den ML-Lebenszyklus – von der Problemdefinition bis zum Production-Monitoring – mit Fokus auf Metriken, Validierung und Debugging.

---

## Der ML-Workflow (CRISP-ML)

1. **Geschäftsverständnis**: Definieren Sie das Ziel und die Erfolgskriterien.
2. **Datenverständnis**: Erkunden Sie verfügbare Daten, identifizieren Sie Qualitätsprobleme.
3. **Datenvorbereitung**: Bereinigen, transformieren und aufteilen der Daten.
4. **Modellierung**: Modelle trainieren, Hyperparameter optimieren.
5. **Evaluation**: Leistung anhand von Metriken bewerten.
6. **Bereitstellung**: Das Modell in Produktion bereitstellen.
7. **Monitoring**: Drift, Leistung und Anomalien verfolgen.

Dies ist eine iterative Schleife – Sie werden basierend auf den Evaluationsergebnissen frühere Schritte erneut besuchen.

---

## Datenaufteilung

### Train/Validation/Test-Split
- **Trainingsdatensatz** (~70%): Wird verwendet, um die Modellparameter anzupassen.
- **Validierungsdatensatz** (~15%): Wird verwendet, um Hyperparameter zu optimieren und Modellvarianten auszuwählen.
- **Testdatensatz** (~15%): Wird nur einmal am Ende verwendet, um die Generalisierungsleistung zu schätzen.

**Wichtig:** Der Testdatensatz muss bis zur endgültigen Evaluation vollständig unberührt bleiben, um Datenlecks zu vermeiden.

### Kreuzvalidierung (k-Fold)
Für kleine Datensätze verwenden Sie k-Fold-Kreuzvalidierung: Teilen Sie die Daten in k Folds auf, trainieren Sie auf k-1, validieren Sie auf dem verbleibenden Fold und wiederholen Sie dies k-mal. Mitteln Sie die Leistung. Üblich sind k=5 oder k=10.

### Stratifizierte Aufteilung
Für Klassifizierung mit unausgewogenen Klassen verwenden Sie stratifizierte Aufteilungen, um die Klassenanteile in jeder Teilmenge zu erhalten.

### Zeitbasierte Aufteilung
Für Zeitreihendaten teilen Sie chronologisch auf (auf Vergangenheit trainieren, auf Zukunft testen) anstatt zufällig.

---

## Evaluationsmetriken

### Klassifizierungsmetriken

| Metrik | Was sie misst | Am besten verwendet für |
|--------|--------------|-------------------------|
| **Accuracy** | (TP + TN) / (TP + TN + FP + FN) | Ausgewogene Datensätze |
| **Precision** | TP / (TP + FP) | Wenn falsch-positive Ergebnisse kostspielig sind (z.B. Spam-Erkennung) |
| **Recall** | TP / (TP + FN) | Wenn falsch-negative Ergebnisse kostspielig sind (z.B. Krebs-Screening) |
| **F1-Score** | Harmonisches Mittel aus Precision und Recall | Unausgewogene Datensätze, Ein-Zahlen-Metrik |
| **AUC-ROC** | Fläche unter der ROC-Kurve; Kompromiss zwischen TPR und FPR | Allgemeine Klassifikatorleistung unabhängig vom Schwellenwert |
| **AUC-PR** | Fläche unter der Precision-Recall-Kurve | Stark unausgewogene Datensätze |

**Definitionen:**
- TP = True Positive
- TN = True Negative
- FP = False Positive (Typ-I-Fehler)
- FN = False Negative (Typ-II-Fehler)

### Regressionsmetriken

| Metrik | Was sie misst | Empfindlichkeit gegenüber Ausreißern |
|--------|--------------|--------------------------------------|
| **MSE** (Mean Squared Error) | Durchschnittliche quadrierte Differenz | Hoch |
| **RMSE** (Root Mean Squared Error) | Quadratwurzel aus MSE (gleiche Einheiten wie Ziel) | Hoch |
| **MAE** (Mean Absolute Error) | Durchschnittliche absolute Differenz | Niedrig |
| **R²** (Bestimmtheitsmaß) | Anteil der erklärten Varianz | Keine direkte, aber indirekt empfindlich gegenüber Ausreißern |

### Ranking- und Retrieval-Metriken
- **Precision@k**: Anteil relevanter Elemente unter den Top-k-Empfehlungen.
- **Recall@k**: Anteil aller relevanten Elemente, die in den Top-k erscheinen.
- **NDCG** (Normalised Discounted Cumulative Gain): Berücksichtigt positionsabhängige Relevanz.
- **Hit Rate**: Ob ein relevantes Element in den Top-k erscheint.

### Generative/LLM-Metriken
- **Perplexity**: Wie "überrascht" das Modell von einem zurückgehaltenen Text ist (niedriger ist besser).
- **BLEU**: n-gramm-Überschneidung mit Referenzübersetzungen (präzisionsorientiert).
- **ROUGE**: Recall-orientierte Überschneidung für Zusammenfassungen.
- **BERTScore**: Semantische Ähnlichkeit unter Verwendung kontextueller Embeddings (robuster als BLEU).
- **METEOR**: Richtet sich nach WordNet-Synonymen und Stämmen.

---

## Evaluations-Fallstricke

### Datenleck (Data Leakage)
Tritt auf, wenn Informationen aus dem Testdatensatz versehentlich das Training beeinflussen.
- **Vorbeugen:** Verwenden Sie niemals Testdaten für Feature-Engineering, Normalisierung oder Hyperparameter-Tuning.
- **Erkennen:** Wenn Ihr Modell verdächtig hohe Scores erzielt, vermuten Sie ein Leck.

### Overfitting
Das Modell performs gut auf Trainingsdaten, aber schlecht auf Validierung/Test.
- **Abschwächen:** Verwenden Sie Regularisierung, Early Stopping, vereinfachen Sie die Architektur oder sammeln Sie mehr Daten.

### Underfitting
Das Modell performs schlecht sowohl auf Trainings- als auch auf Validierungsdaten.
- **Abschwächen:** Verwenden Sie ein komplexeres Modell, fügen Sie Features hinzu oder reduzieren Sie die Regularisierung.

### Unausgewogene Daten
- **Abschwächen:** Verwenden Sie Klassengewichte, Oversampling (SMOTE), Undersampling oder verwenden Sie geeignete Metriken (F1, AUC-PR) anstelle von Accuracy.

### Temporale Drift (Concept Drift)
Die Beziehung zwischen Features und Ziel ändert sich im Laufe der Zeit.
- **Abschwächen:** Neu trainieren in regelmäßigen Abständen, Leistung überwachen, Drift-Erkennungsalgorithmen verwenden.

---

## Hyperparameter-Tuning

- **Grid Search:** Probieren Sie erschöpfend alle Kombinationen eines vordefinierten Satzes von Hyperparametern aus. Einfach, aber rechenintensiv.
- **Random Search:** Stichproben zufälliger Kombinationen aus Verteilungen. Effizienter als Grid Search für hochdimensionale Räume.
- **Bayesian Optimization:** Baut ein probabilistisches Modell der Zielfunktion auf und wählt Hyperparameter intelligent aus. Bibliotheken: Optuna, Hyperopt, scikit-optimize.
- **Automatisiertes Tuning:** Verwenden Sie Tools wie Optuna, Ray Tune oder Weights & Biases Sweeps für verteiltes Tuning.

**Vorgeschlagene Suchbereiche für häufige Hyperparameter:**

| Parameter | Vorgeschlagener Bereich (log-skaliert) |
|-----------|----------------------------------------|
| Lernrate | 1e-5 bis 1e-1 |
| Batch-Größe | 16, 32, 64, 128, 256 |
| Anzahl der Schichten (NN) | 2 bis 6 |
| Anzahl der Neuronen (NN) | 32 bis 1024 |
| Regularisierung (L2) | 1e-6 bis 1e-2 |
| Baumtiefe (XGBoost) | 3 bis 12 |

---

## Modellauswahl und Validierung

1. **Basismodell:** Beginnen Sie mit einer einfachen Heuristik oder einem einfachen Modell (z.B. logistische Regression, Mittelwert-Prädiktor), um eine Untergrenze festzulegen.
2. **Kandidatenmodelle:** Trainieren Sie mehrere Modellfamilien (z.B. Random Forest, XGBoost, neuronales Netz).
3. **Kreuzvalidieren** Sie jeden Kandidaten auf dem Validierungsdatensatz.
4. **Vergleichen Sie Metriken** (mit Konfidenzintervallen) und wählen Sie den besten Kandidaten aus.
5. **Finale Evaluation** auf dem zurückgehaltenen Testdatensatz.
6. **Fehleranalyse:** Betrachten Sie Beispiele, die das Modell falsch klassifiziert. Identifizieren Sie Muster (z.B. seltene Klassen, mehrdeutige Eingaben) und speisen Sie Erkenntnisse zurück in die Datenvorbereitung oder das Feature-Engineering.

---

## Bereitstellung und Monitoring

### Serving-Muster
- **Batch-Inferenz:** Verarbeitung großer Datenmengen offline (z.B. nächtliche Empfehlungen).
- **Online-Inferenz:** Echtzeit-Vorhersagen über API (z.B. Kredit-Scoring, Betrugserkennung).
- **Streaming-Inferenz:** Ereignisgesteuert, echtzeitfähig mit geringer Latenz (z.B. IoT-Sensor-Warnungen).

### Modell-Monitoring
- **Leistungsmonitoring:** Verfolgen Sie Accuracy/F1 im Laufe der Zeit auf Live-Daten (wenn Ground Truth verfügbar ist).
- **Datendrift:** Überwachen Sie Änderungen in den Eingabe-Feature-Verteilungen (z.B. mit PSI – Population Stability Index).
- **Concept Drift:** Überwachen Sie Änderungen in der Beziehung zwischen Eingaben und Ausgaben.
- **Vorhersagedrift:** Verfolgen Sie die Verteilung der vorhergesagten Ausgaben.
- **Latenz und Durchsatz:** Stellen Sie sicher, dass SLAs (Service Level Agreements) eingehalten werden.

### Protokollierung und Alarmierung
- Protokollieren Sie alle Vorhersageanfragen und -antworten (mit Anonymisierung).
- Richten Sie Alarme ein für:
  - Signifikanten Leistungsabfall.
  - Hohen Prozentsatz fehlender oder ungültiger Eingaben.
  - Modellausgaben außerhalb erwarteter Grenzen.

### Modell-Versionierung und Registry
- Verwenden Sie eine Modell-Registry (z.B. MLflow, Weights & Biases, Sagemaker Model Registry), um Modelle, Metadaten und Evaluationsergebnisse zu speichern und zu versionieren.
- Speichern Sie den Trainingscode und die Datenversion (via DVC oder Git LFS) zusammen mit dem Modell.

---

## Praktische Workflow-Checkliste

- [ ] Problem definiert und Erfolgsmetrik festgelegt.
- [ ] Datenexploration durchgeführt (fehlende Werte, Ausreißer, Verteilung).
- [ ] Train/Validation/Test-Split erstellt (stratifiziert bei Bedarf).
- [ ] Basismodell etabliert.
- [ ] Kandidatenmodelle trainiert und validiert.
- [ ] Hyperparameter optimiert.
- [ ] Bestes Modell durch Kreuzvalidierung ausgewählt.
- [ ] Finale Evaluation auf Testdatensatz.
- [ ] Fehleranalyse durchgeführt.
- [ ] Bereitstellungsplan fertig (Serving-Infrastruktur).
- [ ] Monitoring-Dashboard eingerichtet.
- [ ] Dokumentation (Datenkarte, Modellkarte) abgeschlossen.