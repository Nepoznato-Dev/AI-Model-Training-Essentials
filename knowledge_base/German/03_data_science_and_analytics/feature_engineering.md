---
# Metadata
title: "Feature Engineering"
description: "Transformations, encodings, feature selection, dimensionality reduction"
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
tags: [feature, engineering, data-science-and-analytics]
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
# Feature-Engineering
Unter Feature Engineering versteht man den Prozess der Umwandlung von Rohdaten in Darstellungen, die Modelle für maschinelles Lernen effektiver machen. Es wird oft als der wichtigste Schritt in der ML-Pipeline beschrieben – die Funktionen, die Sie einem Modell geben, sind wichtiger als der von Ihnen gewählte Algorithmus. Ein einfaches Modell mit gut ausgearbeiteten Funktionen übertrifft in der Regel ein komplexes Modell mit rohen, unverarbeiteten Eingaben. Die Kunst besteht darin, sowohl die Domäne als auch die Daten gut genug zu verstehen, um Signale zu erzeugen, aus denen das Modell lernen kann.
---

## Warum Feature Engineering wichtig ist
| Faktor | Auswirkungen |
|--------|--------|
| **Signalqualität** | Bessere Funktionen = klarere Muster, die das Modell lernen kann |
| **Modelleinfachheit** | Gute Funktionen sorgen dafür, dass einfachere Modelle eine gute Leistung erbringen. weniger Bedarf an komplexen Architekturen |
| **Trainingsgeschwindigkeit** | Relevante, gut skalierte Features konvergieren schneller |
| **Verallgemeinerung** | Domäneninformierte Funktionen helfen Modellen bei der Arbeit mit unsichtbaren Daten |
| **Interpretierbarkeit** | Sinnvolle Funktionen lassen sich Stakeholdern leichter erklären |
---

## Arten von Feature-Transformationen
### Numerische Transformationen
| Transformation | Formel / Beschreibung | Wann zu verwenden |
|---------------|-------|-------------|
| **Log-Transformation** | log(x) oder log(x + 1) | Rechtsschiefe Verteilungen; Geldwerte |
| **Quadratwurzel** | sqrt(x) | Mäßiger Versatz; Zähldaten |
| **Box-Cox** | Parametrische Transformation, die die beste Leistungstransformation findet | Daten normaler verteilen |
| **Yeo-Johnson** | Wie Box-Cox, verarbeitet jedoch negative Werte | Verzerrte Daten mit negativen Werten |
| **Standardisierung** | (x - Mittelwert) / std | Merkmale mit unterschiedlichen Maßstäben; Algorithmen, die Normalität annehmen |
| **Min-Max-Skalierung** | (x - min) / (max - min) | Begrenzungsfunktionen an [0, 1]; Bildpixelwerte |
| **Robuste Skalierung** | (x – Median) / IQR | Daten mit Ausreißern |
| **Binning** | Kontinuierliche in kategoriale | umwandeln Nichtlineare Beziehungen; Entscheidungsbäume |
| **Polynomfunktionen** | x², x³, x₁×x₂ | Erfassung nichtlinearer Beziehungen in linearen Modellen |
### Kategoriale Kodierungen
| Kodierung | Beschreibung | Wann zu verwenden |
|----------|-------------|-------------|
| **One-Hot-Kodierung** | Erstellen Sie für jede Kategorie eine Binärspalte | Kategorien mit niedriger Kardinalität; Baumbasierte Modelle verarbeiten nativ |
| **Label-Kodierung** | Weisen Sie jeder Kategorie eine Ganzzahl zu | Ordnungskategorien; Baumbasierte Modelle |
| **Zielkodierung** | Ersetzen Sie die Kategorie durch den Mittelwert der Zielvariablen | Kategorien mit hoher Kardinalität; Überanpassung durch Glättung vermeiden |
| **Frequenzkodierung** | Ersetzen Sie die Kategorie durch ihre Anzahl oder Häufigkeit | Wenn die Frequenz selbst informativ ist |
| **Binärkodierung** | Konvertieren Sie ganzzahlig codierte Kategorien in Binärziffern | Hohe Kardinalität; reduziert die Dimensionalität gegenüber One-Hot |
| **Einbettung** | Lernen Sie die dichte Vektordarstellung | Sehr hohe Kardinalität; NLP; Empfehlungssysteme |
| **Hash-Kodierung** | Hash-Kategorien auf eine feste Anzahl von Features | Sehr hohe Kardinalität; Online-Lernen |
### Datums- und Uhrzeitfunktionen
| Funktion | Beschreibung |
|---------|-------------|
| **Tagesstunde** | Erfasst tägliche Muster (Hauptverkehrszeit, Nachtzeit) |
| **Wochentag** | Wochentags- und Wochenendeffekte |
| **Monat / Quartal** | Saisonale Muster |
| **Ist Wochenende** | Binäre Flagge für Wochenende |
| **Ist Feiertag** | Binäre Flagge für Feiertage |
| **Zeit seit dem Ereignis** | Tage seit dem letzten Kauf; Stunden seit dem letzten Login |
| **Zyklische Kodierung** | sin(2π × Stunde / 24), cos(2π × Stunde / 24) – bewahrt die zirkuläre Natur der Zeit |
---

## Umgang mit fehlenden Werten
| Strategie | Beschreibung | Wann zu verwenden |
|----------|-------------|-------------|
| **Zeilen löschen** | Zeilen mit fehlenden Werten entfernen | Fehlende Daten machen einen kleinen Bruchteil aus; MCAR (fehlt völlig zufällig) |
| **Spalten löschen** | Features mit zu vielen fehlenden Werten entfernen | Funktion fehlt größtenteils; nicht wichtig |
| **Mittelwert/Median-Imputation** | Füllen Sie den Wert mit dem Mittelwert oder Median | des Features aus Einfach; bewahrt den Mittelwert, reduziert aber die Varianz |
| **Modusimputation** | Kategorial mit dem häufigsten Wert füllen | Kategoriale Merkmale |
| **KNN-Imputation** | Verwenden Sie k-nächste Nachbarn, um den fehlenden Wert | zu schätzen Wenn ähnliche Instanzen helfen, den fehlenden Wert vorherzusagen |
| **Modellbasierte Imputation** | Trainieren Sie ein Modell, um fehlende Werte vorherzusagen | Genauer; rechenintensiv |
| **Fehlender Indikator** | Fügen Sie eine binäre Spalte hinzu, die das Fehlen markiert | Wenn das Fehlen selbst informativ ist |
| **Interpolation** | Mit interpolierten Werten füllen (linear, Spline) | Zeitreihen; geordnete Daten |
---

## Funktionsauswahl
### Filtermethoden
| Methode | Beschreibung |
|--------|-------------|
| **Korrelation** | Entfernen Sie Features, die stark miteinander korrelieren |
| **Varianzschwelle** | Entfernen Sie Features mit einer Varianz nahe Null |
| **Gegenseitige Information** | Messen Sie die Informationen, die jede Funktion über das Ziel bereitstellt |
| **Chi-Quadrat** | Testen Sie die Unabhängigkeit zwischen kategorialen Merkmalen und dem Ziel |
| **ANOVA F-Test** | Testen Sie, ob numerische Merkmalsmittelwerte zwischen den Zielklassen unterschiedlich sind |
### Wrapper-Methoden
| Methode | Beschreibung |
|--------|-------------|
| **Auswahl weiterleiten** | Leer beginnen; Fügen Sie die beste Funktion einzeln hinzu |
| **Rückwärtseliminierung** | Beginnen Sie mit allem; Entfernen Sie jeweils die schlechteste Funktion |
| **Rekursive Merkmalseliminierung (RFE)** | Modell wiederholt trainieren; unwichtigste Funktionen entfernen |
### Eingebettete Methoden
| Methode | Beschreibung |
|--------|-------------|
| **L1-Regularisierung (Lasso)** | Reduziert irrelevante Feature-Gewichte auf Null |
| **Baumbasierte Wichtigkeit** | Feature-Wichtigkeit aus Baummodellen nutzen |
| **SHAP-Werte** | Messen Sie den Beitrag jedes Features zu Vorhersagen |
---

## Domänenspezifisches Feature-Engineering
### Textfunktionen
| Funktion | Beschreibung |
|---------|-------------|
| **TF-IDF** | Begriffshäufigkeit gewichtet mit inverser Dokumenthäufigkeit |
| **Worteinbettungen** | Dichte Vektoren, die semantische Bedeutung erfassen (Word2Vec, GloVe) |
| **Zeichen n-Gramm** | Unterwortmuster erfassen; nützlich für Tippfehler und Morphologie |
| **Textstatistik** | Länge; Wortanzahl; Satzanzahl; durchschnittliche Wortlänge |
| **Lesbarkeitswerte** | Flesch-Kincaid; Gunning-Nebel-Index |
### Zeitreihenfunktionen
| Funktion | Beschreibung |
|---------|-------------|
| **Lag-Funktionen** | Vorherige Werte: y(t-1), y(t-7), y(t-30) |
| **Laufende Statistiken** | Mittelwert, Standard, Min., Max. über ein Fenster |
| **Unterschied** | y(t) - y(t-1); fängt Trend ein |
| **Saisonbedingter Unterschied** | y(t) - y(t-12) für monatliche Daten mit jährlicher Saisonalität |
| **Fourier-Terme** | Sinus- und Kosinusterme für saisonale Muster |
### Bildfunktionen (Pre-Deep Learning)
| Funktion | Beschreibung |
|---------|-------------|
| **HOG** (Histogramm orientierter Gradienten) | Verteilung der Kantenrichtungen |
| **LBP** (Lokale Binärmuster) | Texturbeschreibung |
| **SIFT** (Scale-Invariante Feature Transform) | Schlüsselpunktdeskriptoren |
| **Farbhistogramme** | Verteilung der Farben im Bild |
---

## Best Practices für Feature Engineering
| Üben | Beschreibung |
|----------|-------------|
| **Datenlecks vermeiden** | Verwenden Sie niemals Informationen aus der Zukunft oder dem Testsatz, um Features zu erstellen |
| **Alles dokumentieren** | Notieren Sie, welche Transformationen angewendet wurden und warum |
| **Versionieren Sie Ihre Funktionen** | Verfolgen Sie Funktionsänderungen neben Modelländerungen |
| **Mit und ohne validieren** | Testen Sie, ob eine neue Funktion tatsächlich die Modellleistung verbessert |
| **Halten Sie es reproduzierbar** | Feature-Engineering-Pipelines sollten deterministisch und wiederholbar sein |
| **Funktionsdrift überwachen** | Feature-Verteilungen können sich im Laufe der Zeit ändern; überwachen und umschulen |
---

## Zusammenfassung
Beim Feature Engineering trifft Domänenwissen auf maschinelles Lernen. Dabei handelt es sich um den Prozess der Umwandlung von Rohdaten – chaotisch, unvollständig, hochdimensional – in saubere, informative Darstellungen, aus denen Modelle lernen können. Numerische Transformationen behandeln Schiefe und Skalierung. Kategoriale Kodierungen wandeln Beschriftungen in Zahlen um, die Modelle verwenden können. Datumsfunktionen erfassen zeitliche Muster. Missing-Value-Strategien verarbeiten unvollständige Daten. Durch die Funktionsauswahl werden Rauschen und Redundanz beseitigt. Die besten Feature-Ingenieure denken wie Detektive: Sie fragen, welche Signale in den Daten vorhanden sein sollten, wo diese Signale versteckt sein könnten und wie sie auf eine Weise extrahiert werden können, die ehrlich (kein Datenverlust), reproduzierbar und robust gegenüber Veränderungen im Laufe der Zeit ist.