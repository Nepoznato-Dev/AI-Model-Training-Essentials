# Bewertung und Workflow im Machine Learning

Ein praktischer Leitfaden für den ML-Lebenszyklus — von der Problemdefinition bis zum Monitoring in Produktion — mit Fokus auf Metriken, Validierung und Debugging.

---

## Der ML-Workflow (CRISP-ML)

1. **Business Understanding**: Definiere das Ziel und die Erfolgskriterien.
2. **Data Understanding**: Erkunde die verfügbaren Daten und identifiziere Qualitätsprobleme.
3. **Data Preparation**: Bereinige, transformiere und splitte die Daten.
4. **Modelling**: Trainiere Modelle und optimiere Hyperparameter.
5. **Evaluation**: Bewerte die Leistung anhand von Metriken.
6. **Deployment**: Stelle das Modell in Produktion bereit.
7. **Monitoring**: Überwache Drift, Leistung und Anomalien.

Dies ist ein iterativer Kreislauf — du wirst auf Basis der Bewertungsergebnisse zu früheren Schritten zurückkehren.

---

## Datensplitting

### Train / Validation / Test Split
- **Training set** (~70%): Wird verwendet, um die Modellparameter anzupassen.
- **Validation set** (~15%): Wird verwendet, um Hyperparameter abzustimmen und Modellvarianten auszuwählen.
- **Test set** (~15%): Wird nur einmal ganz am Ende verwendet, um die Generalisierungsleistung zu schätzen.

**Wichtig:** Das Test set muss bis zur abschließenden Bewertung vollständig unberührt bleiben, um Data Leakage zu vermeiden.

### Cross-Validation (k-fold)
Für kleine Datensätze verwende k-fold cross-validation: Teile die Daten in k Folds, trainiere auf k-1, validiere auf dem verbleibenden Fold und wiederhole das k-mal. Üblich sind k=5 oder k=10.

### Stratified Splitting
Für Klassifikation mit unausgewogenen Klassen verwende stratifizierte Splits, um die Klassenverhältnisse in jedem Teilset zu erhalten.

### Time-Based Splitting
Für Zeitreihendaten splitte chronologisch (Training auf der Vergangenheit, Test auf der Zukunft) statt zufällig.

---

## Bewertungsmetriken

### Klassifikationsmetriken

| Metrik | Was sie misst | Am besten geeignet für |
|--------|----------------|------------------------|
| **Accuracy** | (TP + TN) / (TP + TN + FP + FN) | Ausgewogene Datensätze |
| **Precision** | TP / (TP + FP) | Wenn False Positives teuer sind (z. B. Spam-Erkennung) |
| **Recall** | TP / (TP + FN) | Wenn False Negatives teuer sind (z. B. Krebs-Screening) |
| **F1-score** | Harmonisches Mittel aus Precision und Recall | Unausgewogene Datensätze, Ein-Zahl-Metrik |
| **AUC-ROC** | Fläche unter der ROC-Kurve; Abwägung zwischen TPR und FPR | Allgemeine Klassifikatorleistung unabhängig vom Schwellenwert |
| **AUC-PR** | Fläche unter der Precision-Recall-Kurve | Stark unausgewogene Datensätze |

**Definitionen:**
- TP = True Positive
- TN = True Negative
- FP = False Positive (Fehler Typ I)
- FN = False Negative (Fehler Typ II)

### Regressionsmetriken

| Metrik | Was sie misst | Empfindlichkeit gegenüber Ausreißern |
|--------|----------------|--------------------------------------|
| **MSE** (Mean Squared Error) | Durchschnittliche quadrierte Abweichung | Hoch |
| **RMSE** (Root Mean Squared Error) | Quadratwurzel aus MSE (gleiche Einheiten wie das Ziel) | Hoch |
| **MAE** (Mean Absolute Error) | Durchschnittliche absolute Abweichung | Gering |
| **R²** (Bestimmtheitsmaß) | Erklärter Varianzanteil | Nicht direkt, aber indirekt empfindlich gegenüber Ausreißern |

### Ranking- und Retrieval-Metriken
- **Precision@k**: Anteil relevanter Elemente unter den Top-k-Empfehlungen.
- **Recall@k**: Anteil aller relevanten Elemente, die in den Top-k erscheinen.
- **NDCG** (Normalised Discounted Cumulative Gain): Berücksichtigt die Relevanz der Position.
- **Hit Rate**: Ob ein relevantes Element in den Top-k erscheint.

### Generative / LLM-Metriken
- **Perplexity**: Wie „überrascht“ das Modell von einem zurückgehaltenen Text ist (niedriger ist besser).
- **BLEU**: n-Gramm-Überlappung mit Referenzübersetzungen (fokussiert auf Präzision).
- **ROUGE**: Recall-orientierte Überlappung für Zusammenfassungen.
- **BERTScore**: Semantische Ähnlichkeit mit kontextuellen Embeddings (robuster als BLEU).
- **METEOR**: Gleicht WordNet-Synonyme und Wortstämme ab.

---

## Fallstricke bei der Bewertung

### Data Leakage
Tritt auf, wenn Informationen aus dem Test set unbeabsichtigt das Training beeinflussen.
- **Vermeiden:** Verwende Testdaten niemals für Feature Engineering, Normalisierung oder Hyperparameter-Tuning.
- **Erkennen:** Wenn dein Modell verdächtig hoch scored, vermute Leakage.

### Overfitting
Das Modell performt auf Trainingsdaten gut, aber auf Validation/Test schlecht.
- **Abmildern:** Verwende Regularisierung, Early Stopping, vereinfache die Architektur oder sammle mehr Daten.

### Underfitting
Das Modell performt sowohl auf Training als auch auf Validation schlecht.
- **Abmildern:** Verwende ein komplexeres Modell, füge Features hinzu oder reduziere die Regularisierung.

### Imbalanced Data
- **Abmildern:** Verwende Klassengewichte, Oversampling (SMOTE), Undersampling oder geeignete Metriken (F1, AUC-PR) statt Accuracy.

### Temporal Drift (Concept Drift)
Die Beziehung zwischen Features und Ziel verändert sich im Lauf der Zeit.
- **Abmildern:** Trainiere regelmäßig neu, überwache die Leistung und verwende Drift-Erkennungsalgorithmen.

---

## Hyperparameter-Tuning

- **Grid Search**: Probiere alle Kombinationen eines vordefinierten Satzes von Hyperparametern vollständig aus. Einfach, aber rechnerisch teuer.
- **Random Search**: Ziehe zufällige Kombinationen aus Verteilungen. Für hochdimensionale Räume effizienter als grid search.
- **Bayesian Optimisation**: Erstellt ein probabilistisches Modell der Zielfunktion und wählt Hyperparameter intelligent aus. Bibliotheken: Optuna, Hyperopt, scikit-optimise.
- **Automated Tuning**: Verwende Tools wie Optuna, Ray Tune oder Weights & Biases Sweeps für verteiltes Tuning.

**Vorgeschlagene Suchbereiche für häufige Hyperparameter:**

| Parameter | Vorgeschlagener Bereich (log-scale) |
|-----------|-------------------------------------|
| Learning rate | 1e-5 to 1e-1 |
| Batch size | 16, 32, 64, 128, 256 |
| Number of layers (NN) | 2 to 6 |
| Number of neurons (NN) | 32 to 1024 |
| Regularisation (L2) | 1e-6 to 1e-2 |
| Tree depth (XGBoost) | 3 to 12 |

---

## Modellauswahl und Validierung

1. **Baseline model**: Beginne mit einer einfachen Heuristik oder einem einfachen Modell (z. B. logistischer Regression, mean predictor), um eine Untergrenze festzulegen.
2. **Candidate models**: Trainiere mehrere Modellfamilien (z. B. Random Forest, XGBoost, Neural Network).
3. **Cross-validate** jeden Kandidaten auf dem Validation set.
4. **Vergleiche Metriken** (mit Konfidenzintervallen) und wähle den besten Kandidaten aus.
5. **Abschließende Bewertung** auf dem zurückgehaltenen Test set.
6. **Error analysis**: Betrachte Beispiele, die das Modell falsch vorhersagt. Identifiziere Muster (z. B. seltene Klassen, mehrdeutige Eingaben) und führe die Erkenntnisse in Data Preparation oder Feature Engineering zurück.

---

## Deployment und Monitoring

### Serving-Muster
- **Batch inference**: Verarbeite große Datenmengen offline (z. B. nächtliche Empfehlungen).
- **Online inference**: Echtzeitvorhersagen per API (z. B. Kredit-Scoring, Betrugserkennung).
- **Streaming inference**: Ereignisgetrieben, in Echtzeit mit geringer Latenz (z. B. IoT-Sensorwarnungen).

### Modell-Monitoring
- **Performance monitoring**: Verfolge Accuracy/F1 im Zeitverlauf auf Live-Daten (wenn Ground Truth verfügbar ist).
- **Data drift**: Überwache Veränderungen in den Verteilungen der Eingabefeatures (z. B. mit PSI – Population Stability Index).
- **Concept drift**: Überwache Veränderungen in der Beziehung zwischen Eingaben und Ausgaben.
- **Prediction drift**: Verfolge die Verteilung der vorhergesagten Ausgaben.
- **Latency and throughput**: Stelle sicher, dass SLAs (Service Level Agreements) eingehalten werden.

### Logging und Alerting
- Protokolliere alle Vorhersageanfragen und -antworten (mit Anonymisierung).
- Richte Alerts ein für:
  - Deutlichen Leistungsabfall.
  - Hohen Anteil fehlender oder ungültiger Eingaben.
  - Modellausgaben außerhalb der erwarteten Grenzen.

### Modellversionierung und Registry
- Verwende eine model registry (z. B. MLflow, Weights & Biases, Sagemaker Model Registry), um Modelle, Metadaten und Bewertungsergebnisse zu speichern und zu versionieren.
- Speichere den Trainingscode und die Datenversion (via DVC oder Git LFS) zusammen mit dem Modell.

---

## Checkliste für den praktischen Workflow

- [ ] Problem formuliert und Erfolgsmetrik definiert.
- [ ] Datenexploration durchgeführt (fehlende Werte, Ausreißer, Verteilung).
- [ ] Train/validation/test split erstellt (falls nötig stratifiziert).
- [ ] Baseline model festgelegt.
- [ ] Candidate models trainiert und validiert.
- [ ] Hyperparameter optimiert.
- [ ] Bestes Modell via cross-validation ausgewählt.
- [ ] Abschließende Bewertung auf dem Test set.
- [ ] Error analysis durchgeführt.
- [ ] Deployment-Plan bereit (Serving-Infrastruktur).
- [ ] Monitoring-Dashboard eingerichtet.
- [ ] Dokumentation (data card, model card) abgeschlossen.
