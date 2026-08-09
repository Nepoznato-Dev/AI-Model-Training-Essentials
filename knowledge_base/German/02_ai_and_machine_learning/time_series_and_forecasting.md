---
# Metadata
title: "Time Series and Forecasting"
description: "ARIMA, Prophet, LSTMs, seasonality, anomaly detection"
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
tags: [time, series, forecasting, ai-and-machine-learning]
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
# Zeitreihen und Prognosen
Unter Zeitreihendaten versteht man alle im Laufe der Zeit erfassten Daten: Aktienkurse, Temperaturwerte, Website-Verkehr, Verkaufszahlen, Herzfrequenzmesser, Energieverbrauch. Forecasting means predicting future values based on past patterns. Es ist eine der praktisch wertvollsten Anwendungen der Datenwissenschaft – und eine der schwierigsten, weil die Zukunft wirklich ungewiss ist und reale Zeitreihen voller Rauschen, Saisonalität und Strukturbrüche sind.
---

## Merkmale von Zeitreihen
| Komponente | Beschreibung | Beispiel |
|-----------|-------------|---------|
| **Trend** | Langfristige Zunahme oder Abnahme | Globale Temperaturen steigen über Jahrzehnte |
| **Saisonalität** | Regelmäßige, vorhersehbare Muster in festen Abständen | Die Einzelhandelsumsätze steigen jedes Jahr im Dezember |
| **Zyklizität** | Schwankungen in nicht festgelegten Abständen (oft wirtschaftlich) | Rezessionen alle 5-10 Jahre |
| **Rauschen (Rest)** | Zufällige Variation, die nicht erklärt werden kann | Tägliche Aktienkursbewegungen |
| **Autokorrelation** | Aktuelle Werte hängen von vergangenen Werten ab | Die heutige Temperatur ähnelt der von gestern |
### Stationarität
Eine Zeitreihe ist **stationär**, wenn sich ihre statistischen Eigenschaften (Mittelwert, Varianz) im Laufe der Zeit nicht ändern. Die meisten Prognosemethoden gehen von Stationarität aus.
| Testen | Zweck |
|------|---------|
| **Erweiterter Dickey-Fuller (ADF)** | Testet, ob eine Einheitswurzel vorhanden ist (nicht stationär) |
| **KPSS-Test** | Testet, ob die Reihe trendstationär ist |
| Transformation | Wann zu verwenden |
|---------------|-------------|
| **Differenzierung** | Trend entfernen: y'(t) = y(t) - y(t-1) |
| **Log-Transformation** | Varianz stabilisieren (für exponentielles Wachstum) |
| **Saisonale Unterschiede** | Saisonalität entfernen: y'(t) = y(t) - y(t-s) wobei s die Saisonlänge | ist
---

## Klassische Prognosemethoden
### Gleitende Durchschnitte
| Methode | Beschreibung | Am besten für |
|--------|-------------|----------|
| **Einfacher gleitender Durchschnitt (SMA)** | Durchschnitt der letzten N Beobachtungen | Glättung verrauschter Daten |
| **Gewichteter gleitender Durchschnitt** | Neuere Beobachtungen erhalten höheres Gewicht | Wenn aktuelle Daten wichtiger sind |
| **Exponentieller gleitender Durchschnitt (EMA)** | Exponentiell abnehmende Gewichte | Trends mit weniger Verzögerung verfolgen |
### Exponentielle Glättung
| Methode | Komponenten | Anwendungsfall |
|--------|-----------|----------|
| **Einfach (SES)** | Nur Ebene | Kein Trend, keine Saisonalität |
| **Holt's (Double)** | Niveau + Trend | Daten mit Trend, aber ohne Saisonalität |
| **Holt-Winters (Triple)** | Niveau + Trend + Saisonalität | Daten mit Trend und Saisonalität |
### ARIMA und Varianten
ARIMA (AutoRegressive Integrated Moving Average) ist das Arbeitspferd der klassischen Zeitreihenprognose.
| Komponente | Bedeutung | Parameter |
|-----------|---------|-----------|
| **AR (p)** | Regress auf die vorherigen p-Werte | Wie viele vergangene Werte sollen verwendet werden |
| **Ich (t)** | Anzahl der Differenzierungsschritte zur Herstellung stationärer | Wie oft soll der Unterschied ausfallen |
| **MA (q)** | Modellieren Sie den Fehler als Kombination vergangener Fehler | Wie viele vergangene Fehler sollen verwendet werden |
| Variante | Erweiterung | Anwendungsfall |
|---------|-----------|----------|
| **SARIMA** | Fügt saisonale Komponenten hinzu (P, D, Q, s) | Daten mit starker Saisonalität |
| **ARIMAX** | Fügt externe Variablen hinzu | Wenn Sie über bevorstehende Ereignisse informiert sind |
| **VAR** | Multivariate ARIMA; mehrere voneinander abhängige Serien | Wenn Variablen sich gegenseitig beeinflussen |
---

## Moderne ML-Ansätze
### LSTM- und RNN-basierte Modelle
| Modell | Architektur | Vorteil |
|-------|-------------|-----------|
| **LSTM** | Langes Kurzzeitgedächtnisnetzwerk | Erfasst zeitliche Abhängigkeiten über große Entfernungen |
| **GRU** | Gated Recurrent Unit (einfacheres LSTM) | Schnelleres Training; ähnliche Leistung |
| **Seq2Seq** | Encoder-Decoder für Zeitreihen | Flexible Ein-/Ausgangslängen |
| **Temporal Convolutional Network (TCN)** | Erweiterte kausale Windungen | Paralleles Training; langes Empfangsfeld |
### Prophet (Meta)
Ein praktisches Prognosetool für Geschäftszeitreihen.
| Funktion | Beschreibung |
|---------|-------------|
| **Zersetzung** | Trend + Saisonalität + Feiertage |
| **Flexibel** | Behandelt fehlende Daten, Ausreißer und Strukturbrüche |
| **Interpretierbar** | Komponenten sind für Menschen lesbar |
| **Automatisch** | Angemessene Standardvorgaben; minimale Abstimmung erforderlich |
| Stärke | Einschränkung |
|----------|------------|
| Ideal für Geschäftskennzahlen (Verkäufe, Benutzer) | Nicht ideal für sehr hochfrequente Daten |
| Behandelt Feiertage und besondere Ereignisse | Nimmt additive oder multiplikative Saisonalität an |
| Robust gegenüber Ausreißern | Weniger genau als Deep Learning für komplexe Muster |
### Transformatorbasierte Modelle
| Modell | Hauptmerkmal |
|-------|-------------|
| **Informant** | ProbSparse Aufmerksamkeit für lange Sequenzen |
| **Autoformer** | Autokorrelationsmechanismus für die Serienzerlegung |
| **PatchTST** | Patcht die Zeitreihe; kanalunabhängig |
| **TimesFM** (Google) | Grundlagenmodell für Zeitreihen; auf verschiedene Daten vorab trainiert |
| **Chronos** (Amazon) | Tokenisiert Zeitreihen; verwendet Architektur im LLM-Stil |
---

## Anomalieerkennung in Zeitreihen
Erkennen ungewöhnlicher Muster, die vom erwarteten Verhalten abweichen.
| Methode | Ansatz | Anwendungsfall |
|--------|----------|----------|
| **Statistisch** | Z-Score, IQR, Kontrollkarten | Einfach, gut verständlich |
| **Isolationswald** | Baumbasiert; isoliert Anomalien durch zufällige Partitionierung | Multivariate Anomalieerkennung |
| **LOF** (Lokaler Ausreißerfaktor) | Dichtebasiert; vergleicht die lokale Dichte mit der der Nachbarn | Wenn Anomalien in Regionen mit geringer Dichte auftreten |
| **Autoencoder** | Rekonstruktionsfehler; hoher Fehler = Anomalie | Komplexe, nichtlineare Muster |
| **LSTM-basiert** | Den nächsten Schritt vorhersagen; großer Vorhersagefehler = Anomalie | Sequentielle Anomalien |
### Anwendungen
| Domäne | Was Anomalien bedeuten |
|--------|-----|
| **Finanzen** | Betrug, Marktcrashs, Flash-Crashs |
| **Gesundheitswesen** | Abnormale Herzfrequenz, Beginn eines Anfalls |
| **Fertigung** | Geräteausfall, Qualitätsmängel |
| **Cybersicherheit** | Einbruchsversuche, DDoS-Angriffe |
| **Infrastruktur** | Serverüberlastung, Netzwerkausfälle |
---

## Bewertungsmetriken
| Metrisch | Formel (konzeptionell) | Wann zu verwenden |
|--------|------|-------------|
| **MAE** (mittlerer absoluter Fehler) | Durchschnitt der absoluten Fehler | Interpretierbar; gleiche Einheiten wie Daten |
| **RMSE** (Root Mean Squared Error) | Quadratwurzel der durchschnittlichen quadratischen Fehler | Bestraft große Fehler mehr |
| **MAPE** (mittlerer absoluter prozentualer Fehler) | Durchschnitt der absoluten prozentualen Fehler | Wenn der relative Fehler wichtig ist |
| **SMAPE** (Symmetrisches MAPE) | Symmetrische Version von MAPE | Behandelt Werte nahe Null besser |
| **MASE** (mittlerer absoluter skalierter Fehler) | MAE im Vergleich zu einer naiven Prognose | Vergleich verschiedener Serien |
---

## Praktischer Arbeitsablauf
| Schritt | Beschreibung |
|------|-------------|
| **1. Entdecken** | Plotten Sie die Serie; Trend, Saisonalität und Ausreißer identifizieren |
| **2. Zerlegen** | Aufteilen in Trend-, Saison- und Restkomponenten |
| **3. Stationarisieren** | Wenden Sie bei Bedarf Differenzierungen oder Transformationen an |
| **4. Split** | Zeitbasierte Aufteilung (niemals zufällige Aufteilung für Zeitreihen) |
| **5. Grundlinie** | Beginnen Sie mit einer naiven Prognose (letzter Wert, saisonal naiv) |
| **6. Modell** | Probieren Sie klassische Methoden (ARIMA, Prophet) und dann ML-Methoden aus |
| **7. Bewerten** | Verwenden Sie geeignete Kennzahlen; mit Grundlinie vergleichen |
| **8. Iterieren** | Funktionen hinzufügen, verschiedene Modelle ausprobieren, Hyperparameter optimieren |
---

## Tools und Bibliotheken
| Werkzeug | Zweck |
|------|---------|
| **Statistikmodelle** | Klassische Zeitreihen (ARIMA, ETS, Zerlegung) |
| **Prophet** (Meta) | Prognose von Geschäftszeitreihen |
| **Skizeit** | Einheitliche ML-Schnittstelle für Zeitreihen |
| **Dart** | Umfassende Prognosebibliothek (klassisch + Deep Learning) |
| **GluonTS** (Amazon) | Probabilistische Zeitreihenmodellierung |
| **NeuralProphet** | Prophet mit neuronalen Netzwerkkomponenten |
| **tsfresh** | Automatische Extraktion von Zeitreihenmerkmalen |
| **Pandas** | Manipulation und Resampling von Zeitreihen |
---

## Zusammenfassung
Zeitreihenprognosen verbinden klassische Statistik mit modernem maschinellem Lernen. Klassische Methoden (ARIMA, exponentielle Glättung, Prophet) sind interpretierbar, schnell und oft überraschend genau. Deep-Learning-Methoden (LSTM, Transformers) erfassen komplexe Muster, erfordern jedoch mehr Daten und Abstimmung. Die Grundprinzipien bleiben unabhängig von der Methode dieselben: Verstehen Sie die Struktur Ihrer Daten (Trend, Saisonalität, Rauschen), vergleichen Sie sie immer mit einer einfachen Basislinie, bewerten Sie sie mit geeigneten Metriken und denken Sie daran, dass die Zukunft niemals eine perfekte Wiederholung der Vergangenheit ist.