---
# Metadata
title: "ML Engineering and MLOps"
description: "Model serving, registries, deployment strategies, drift monitoring"
category: "AI and Machine Learning"
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
    date: "2026-08-05"
    author: "AI Model Training Team"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-05"
review_date: "2027-02-05"
reviewed_by: "AI & Machine Learning Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [ml, engineering, mlops, ai-and-machine-learning]
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
# ML Engineering und MLOps
Der Aufbau eines Modells für maschinelles Lernen ist nur die halbe Miete. Es in die Produktion bringen, dafür sorgen, dass es zuverlässig läuft, Abweichungen überwachen und darauf iterieren – hier kommen ML-Engineering und MLOps ins Spiel. Diese Datei deckt den gesamten Lebenszyklus vom Experiment bis zum Produktionssystem ab.
---

## Der ML-Lebenszyklus
| Phase | Beschreibung | Hauptaktivitäten |
|-------|-------------|---------------|
| **1. Problemdefinition** | Gestalten Sie das Geschäftsproblem als ML-Aufgabe | Definieren Sie Metriken, Einschränkungen und Erfolgskriterien |
| **2. Datenerfassung** | Trainingsdaten sammeln und kennzeichnen | ETL, Etikettierung, Erweiterung |
| **3. Experimentieren** | Modelle trainieren und bewerten | Feature Engineering, Hyperparameter-Tuning |
| **4. Modellauswahl** | Wählen Sie das beste Modell | Vergleichen Sie Kennzahlen, bewerten Sie Kompromisse |
| **5. Bereitstellung** | Das Modell an die Produktion senden | Bereitstellung von Infrastruktur, API, Batch |
| **6. Überwachung** | Achten Sie auf Drift und Verschlechterung | Datendrift, Konzeptdrift, Leistung |
| **7. Umschulung** | Aktualisieren Sie das Modell mit neuen Daten | Geplante oder ausgelöste Umschulung |
Der größte Wert (und die Schwierigkeit) liegt in den Phasen 5–7. Ein Modell, das in einem Jupyter-Notebook sitzt, schafft keinen Geschäftswert.
---

## Modellieren Sie Serviermuster
| Muster | Beschreibung | Latenz | Anwendungsfall |
|---------|-------------|---------|----------|
| **Batch-Inferenz** | Modell nach einem Zeitplan für einen Datenstapel ausführen | Stunden | Tägliche Empfehlungen, Betrugsbewertung |
| **Online-Inferenz** | Echtzeitvorhersage pro Anfrage | Millisekunden | Suchranking, Echtzeitklassifizierung |
| **Streaming-Inferenz** | Prozessvorhersagen für einen Datenstrom | Sekunden | Anomalieerkennung, Ereignisverarbeitung |
### Im Dienste der Infrastruktur
| Werkzeug | Geben Sie | ein Am besten für |
|------|------|----------|
| **TensorFlow-Bereitstellung** | Modellserver | TensorFlow-Modelle |
| **Fackelserve** | Modellserver | PyTorch-Modelle |
| **Triton-Inferenzserver** | Multi-Framework | GPU-Inferenz, mehrere Frameworks |
| **vLLM** | LLM-Portion | LLM-Inferenz mit hohem Durchsatz |
| **BentoML** | Einheitliches Servieren | Framework-unabhängige Bereitstellung |
| **Seldon** | K8s-nativ | Kubernetes-Modellbereitstellung |
| **Ray Serve** | Skalierbares Servieren | Große Modelle, verteilte Inferenz |
---

## Modellregister
Eine Modellregistrierung ist ein zentraler Speicher für die Verwaltung von ML-Modellen – ihrer Versionen, Metadaten, Metriken und Bereitstellungsstatus.
| Fähigkeit | Beschreibung |
|-----------|-------------|
| **Versionierung** | Verfolgen Sie jede Modellversion mit eindeutiger ID |
| **Metadaten** | Trainingsdaten, Hyperparameter, Metriken, Autor |
| **Stufenübergänge** | Bewegen Sie Modelle durch die Phasen: Staging → Produktion → Archiviert |
| **Abstammung** | Verfolgen Sie, welche Daten und welcher Code jedes Modell erzeugt hat |
| Werkzeug | Beschreibung |
|------|-------------|
| **MLflow** | Open Source; Modellregistrierung + Experimentverfolgung |
| **Gewichte und Verzerrungen (W&B)** | Kommerziell; Experimentverfolgung + Modellregistrierung |
| **DVC** | Daten- und Modellversionierung mit Git |
| **Azure ML / SageMaker** | Cloud-natives Modellmanagement |
---

## Experimentverfolgung
Jedes ML-Experiment sollte nachverfolgt werden: Welche Daten wurden verwendet, welche Hyperparameter und welche Metriken resultierten.
| Werkzeug | Hauptmerkmale |
|------|-------------|
| **MLflow** | Open-Source, selbstgehostet, verfolgt Parameter/Metriken/Artefakte |
| **W&B** | Rich UI, Sweeps, Artefaktversionierung, Berichte |
| **Neptun** | Metadatenspeicher für MLOps |
| **TensorBoard** | Integriert in TensorFlow; Trainingskurven visualisieren |
### Was zu verfolgen ist
| Kategorie | Beispiele |
|----------|---------|
| **Parameter** | Lernrate, Batchgröße, Modellarchitektur, Anzahl der Epochen |
| **Metriken** | Genauigkeit, Verlust, F1, AUC-ROC (pro Epoche und endgültig) |
| **Artefakte** | Modellgewichte, Verwirrungsmatrizen, Vorhersagestichproben |
| **Daten** | Datensatzversion, Aufteilungsverhältnisse, Vorverarbeitungsschritte |
| **Umwelt** | Python-Version, Bibliotheksversionen, Hardware |
---

## Modellbereitstellungsstrategien
| Strategie | Wie es funktioniert | Risiko |
|----------|-------------|------|
| **Schattenbereitstellung** | Neues Modell läuft neben altem; Vorhersagen verglichen, aber nicht zugestellt | Kein Risiko; validiert, bevor es live geht |
| **Kanarische Veröffentlichung** | Leiten Sie einen kleinen Prozentsatz des Datenverkehrs auf das neue Modell um. schrittweise erhöhen | Geringes Risiko; schnelles Rollback |
| **A/B-Tests** | Teilen Sie Benutzer zwischen alten und neuen auf; Geschäftskennzahlen vergleichen | Misst die tatsächliche Wirkung |
| **Blau-Grün** | Zwei identische Umgebungen; Den gesamten Verkehr auf einmal umschalten | Sofortiger Rollback; doppelte Kosten während des Übergangs |
| **Feature-Flags** | Modell pro Benutzersegment ein-/ausschalten | Feinkörnige Kontrolle |
---

## Überwachung von ML-Systemen
ML-Systeme benötigen mehr Überwachung als herkömmliche Software, da sich die Daten selbst ändern können.
### Arten von Drift
| Drifttyp | Welche Änderungen | Beispiel |
|-----------|-------------|---------|
| **Datendrift** | Änderungen der Eingabeverteilung | Kundendemografischer Wandel nach einer Marketingkampagne |
| **Konzeptdrift** | Zusammenhang zwischen Eingabe- und Ausgabeänderungen | Verbraucherverhalten ändert sich während einer Rezession |
| **Etikettendrift** | Änderungen der Zielverteilung | Betrugsrate steigt von 1 % auf 5 % |
### Was zu überwachen ist
| Kategorie | Metriken |
|----------|---------|
| **Modellleistung** | Genauigkeit, Präzision, Erinnerung, F1, AUC (im Vergleich zum Ausgangswert) |
| **Datenqualität** | Fehlende Werte, Merkmalsverteilungen, Ausreißer |
| **Drift-Erkennung** | Statistische Tests (KS-Test, PSI, KL-Divergenz) |
| **Infrastruktur** | Latenz, Durchsatz, GPU-Auslastung, Speicher |
| **Geschäftskennzahlen** | Conversion-Rate, Umsatzauswirkungen, Benutzerzufriedenheit |
### Überwachungstools
| Werkzeug | Geben Sie | ein
|------|------|
| **Offensichtlich KI** | Open-Source-Datendrift und Modellleistungsüberwachung |
| **Grafana** | Dashboard-Visualisierung (funktioniert mit Prometheus) |
| **WhyLabs** | Datenbeobachtungsplattform |
| **Arize** | ML-Beobachtbarkeit und Ursachenanalyse |
| **Prometheus + Grafana** | Infrastruktur- und Anwendungsmetriken |
---

## Reproduzierbares Training
Reproduzierbarkeit bedeutet, dass Sie ein Experiment erneut durchführen und das gleiche Ergebnis erhalten können. Es ist für Debugging, Auditing und Compliance unerlässlich.
### Anforderungen
| Anforderung | So erreichen Sie es |
|-------------|-------------------|
| **Datenversionierung** | DVC-, Delta Lake- oder Datensatz-Snapshots mit Hashes |
| **Codeversionierung** | Git für alle Trainingscodes |
| **Umgebungsfixierung** | `requirements.txt`,`conda env`, Docker-Images mit genauen Versionen |
| **Saateinstellung** | Zufällige Seeds für Numpy, Torch, Tensorflow reparieren |
| **Konfigurationsverwaltung** | Hydra-, OmegaConf- oder YAML-Konfigurationen für alle Hyperparameter |
| **Artefaktverfolgung** | MLflow oder W&B zum Protokollieren jedes Experiments |
---

## Skalierungsinferenz
Wenn ein Modell Millionen von Anfragen pro Tag bedienen muss, kommt es auf die Leistung an.
| Technik | Beschreibung |
|-----------|-------------|
| **Batchverarbeitung** | Mehrere Anfragen in einem einzigen Weiterleitungsdurchlauf gruppieren |
| **Quantisierung** | Reduzieren Sie die Modellgenauigkeit (FP32 → INT8 oder INT4) für eine schnellere Inferenz |
| **Modelldestillation** | Trainieren Sie ein kleineres Modell, um ein größeres nachzuahmen |
| **Beschneiden** | Entfernen Sie unwichtige Gewichte oder Neuronen |
| **Caching** | Häufige Vorhersagen zwischenspeichern, um Neuberechnungen zu vermeiden |
| **GPU-Optimierung** | TensorRT, ONNX Runtime, Flash Achtung |
| **Horizontale Skalierung** | Führen Sie mehrere Modellreplikate hinter einem Load Balancer aus |
---

## Feature-Flags für ML
Mithilfe von Feature-Flags können Sie steuern, welche Modellversion welche Benutzer bedient, ohne eine erneute Bereitstellung durchzuführen.
| Anwendungsfall | Beschreibung |
|----------|-------------|
| **Schrittweise Einführung** | Neues Modell für 5 % der Nutzer bereitstellen und dann erhöhen |
| **Kill-Schalter** | Bei erkannten Problemen sofort zum Vorgängermodell zurückkehren |
| **Segmentbasiert** | Verschiedene Modelle für unterschiedliche Benutzersegmente |
| **Experimentieren** | A/B-Testmodellvarianten mit Geschäftsmetriken |
Tools: LaunchDarkly, Unleash, Flagsmith oder einfache datenbankgestützte Feature-Flags.
---

## Die MLOps-Reifekurve
| Ebene | Eigenschaften |
|-------|----------------|
| **Stufe 0 – Manuell** | Manuelle Schulung, manuelle Bereitstellung, keine Überwachung |
| **Stufe 1 – Experimentieren** | Experimentverfolgung, Modellregistrierung, grundlegendes CI |
| **Stufe 2 – Automatisierung** | Automatisiertes Umschulen, CI/CD für Modelle, automatisiertes Testen |
| **Stufe 3 – Vollständige Pipeline** | Durchgängig automatisierte Pipeline mit Überwachung, Abweichungserkennung und automatischer Neuschulung |
Die meisten Organisationen liegen irgendwo zwischen Level 0 und Level 1. Das Ziel ist Level 2–3, wo der ML-Lebenszyklus automatisiert und selbstheilend ist.