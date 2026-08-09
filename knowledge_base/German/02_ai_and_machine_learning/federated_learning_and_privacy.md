---
# Metadata
title: "Federated Learning and Privacy"
description: "Decentralised training, differential privacy, secure aggregation"
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
tags: [federated, learning, privacy, ai-and-machine-learning]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "9 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Föderiertes Lernen und Datenschutz
Federated Learning ist eine Technik zum Trainieren von Modellen für maschinelles Lernen über mehrere Geräte oder Organisationen hinweg, ohne die Rohdaten zu teilen. Anstatt Daten an einen zentralen Server zu senden, trainiert jedes Gerät ein lokales Modell und teilt nur die Modellaktualisierungen (Verläufe oder Gewichte). Der zentrale Server aggregiert diese Aktualisierungen, um ein globales Modell zu erstellen. Es wurde von Google zum Trainieren von Tastatursprachenmodellen auf Android-Telefonen entwickelt – und hat sich seitdem zu einer Schlüsseltechnik für die Wahrung der Privatsphäre durch KI entwickelt.
---

## Warum föderiertes Lernen?
| Motivation | Beschreibung | Beispiel |
|------------|-------------|---------|
| **Datenschutz** | Rohdaten verlassen niemals das Gerät | Krankenakten bleiben im Krankenhaus; Fotos bleiben auf dem Handy |
| **Einhaltung gesetzlicher Vorschriften** | DSGVO, HIPAA und andere Vorschriften beschränken den Datenaustausch | Banken können zusammenarbeiten, ohne Kundendaten weiterzugeben |
| **Datenvolumen** | Das Verschieben von Daten ist teuer und langsam | Training auf Milliarden von Telefonen ist unpraktisch, wenn Daten hochgeladen werden müssen |
| **Datensensibilität** | Einige Daten sind selbst mit Einwilligung zu sensibel, um sie weiterzugeben | Geheimdienste der Regierung; persönliche Gesundheitsdaten |
---

## Wie föderiertes Lernen funktioniert
### Das Basisprotokoll (FedAvg)
| Schritt | Was passiert |
|------|-------------|
| **1. Initialisieren** | Zentraler Server erstellt ein globales Modell mit zufälligen Gewichten |
| **2. Verteilen** | Server sendet das aktuelle globale Modell an ausgewählte Geräte |
| **3. Lokale Schulung** | Jedes Gerät trainiert das Modell über mehrere Epochen hinweg anhand seiner lokalen Daten
| **4. Hochladen** | Geräte senden ihre aktualisierten Modellgewichte (keine Daten) zurück an den Server |
| **5. Aggregat** | Der Server mittelt die Gewichte (Federated Averaging), um ein neues globales Modell zu erstellen |
| **6. Wiederholen** | Gehen Sie zurück zu Schritt 2, bis das Modell konvergiert |
```
Server: global_model = average(local_model_1, local_model_2, ..., local_model_n)
```

### Schlüsseleigenschaften
| Eigentum | Beschreibung |
|----------|-------------|
| **Nicht-IID-Daten** | Jedes Gerät verfügt über unterschiedliche Datenverteilungen (nicht unabhängig und identisch verteilt) |
| **Unausgeglichene Daten** | Manche Geräte haben viele Daten, andere nur sehr wenig |
| **Teilweise Teilnahme** | Nicht alle Geräte sind in jeder Runde verfügbar |
| **Kommunikationseffizienz** | Der Flaschenhals ist die Kommunikation, nicht die Berechnung |
---

## Federated Learning-Varianten
| Variante | Beschreibung | Vorteil |
|---------|-------------|-----------|
| **FedAvg** | Durchschnittliche Modellgewichte auf allen Geräten | Einfach; funktioniert gut für IID-Daten |
| **FedProx** | Fügt dem lokalen Training einen proximalen Begriff hinzu | Besser für Nicht-IID-Daten |
| **GERÜST** | Verwendet Kontrollvariablen zur Korrektur der Datenheterogenität | Schnellere Konvergenz bei Nicht-IID-Daten |
| **FedSGD** | Wie FedAvg, jedoch mit einem Gradientenschritt pro Runde | Geringere Kommunikationskosten pro Runde |
| **Personalisierte FL** | Jedes Gerät verwaltet neben dem globalen Modell ein personalisiertes Modell | Bessere Leistung pro Gerät |
| **Vertikale FL** | Unterschiedliche Merkmale (nicht unterschiedliche Stichproben) zwischen den Parteien | Wenn Parteien unterschiedliche Aspekte derselben Daten besitzen |
---

## Differenzielle Privatsphäre
Differential Privacy (DP) bietet eine mathematische Garantie dafür, dass die Ausgabe eines Algorithmus nicht verrät, ob die Daten einer Person enthalten waren.
### Kerndefinition
Ein Mechanismus M erfüllt die (ε, δ)-differentielle Privatsphäre, wenn für zwei beliebige Datensätze D und D', die sich in einem Datensatz unterscheiden:
```
P(M(D) ∈ S) ≤ e^ε × P(M(D') ∈ S) + Î´
```

| Parameter | Bedeutung |
|-----------|---------|
| **ε (Epsilon)** | Datenschutzbudget. Kleiner = privater. Typische Werte: 0,1–10. |
| **δ (Delta)** | Wahrscheinlichkeit, dass die Datenschutzgarantie versagt. Normalerweise auf 1/N (Kehrwert der Datensatzgröße) eingestellt. |
### Mechanismen zum Hinzufügen von Privatsphäre
| Mechanismus | Wie es funktioniert | Anwendungsfall |
|-----------|-------------|----------|
| **Gaußscher Mechanismus** | Fügen Sie Gaußsches Rauschen hinzu, das auf die Empfindlichkeit der Abfrage kalibriert ist | Kontinuierliche Werte (Modellgewichte) |
| **Laplace-Mechanismus** | Laplace-Rauschen hinzufügen | Abfragen zählen |
| **Exponentieller Mechanismus** | Wählen Sie Ausgaben mit einer Wahrscheinlichkeit proportional zu ihrem Nutzen aus | Diskrete Entscheidungen |
### DP-SGD (Differentially Private Stochastic Gradient Descent)
| Schritt | Beschreibung |
|------|-------------|
| 1. Berechnen Sie die Gradienten pro Stichprobe | Anstelle von Batch-Verläufen |
| 2. Farbverläufe zuschneiden | Begrenzt die maximale Norm jedes Gradienten (begrenzt den Einfluss jeder einzelnen Probe) |
| 3. Rauschen hinzufügen | Kalibriertes Gaußsches Rauschen zum aggregierten Gradienten hinzufügen |
| 4. Parameter aktualisieren | Standardgradientenabstiegsschritt |
| Kompromiss | Beschreibung |
|-----------|-------------|
| **Datenschutz vs. Genauigkeit** | Eine stärkere Privatsphäre (niedrigeres ε) erfordert mehr Rauschen, was die Modellgenauigkeit verringert |
| **Privatsphäre vs. Trainingszeit** | Mehr Rauschen bedeutet langsamere Konvergenz |
| **Datenschutzbudgetverfolgung** | Jeder Trainingsschritt verbraucht einen Teil des Datenschutzbudgets. einmal ausgegeben, kann es nicht wiederhergestellt werden |
---

## Kombination von föderiertem Lernen mit differenzieller Privatsphäre
| Schicht | Schutz |
|-------|-----------|
| **Föderiertes Lernen** | Rohdaten bleiben auf Geräten |
| **Differenzielle Privatsphäre** | Sogar die Modellaktualisierungen sind verrauscht und schützen einzelne Beiträge |
| **Sichere Aggregation** | Der Server sieht nur die Gesamtheit aller Updates, nicht einzelne |
Diese Kombination bietet starke Datenschutzgarantien: Selbst wenn der Server kompromittiert ist, kann er nicht feststellen, ob die Daten einer bestimmten Person im Training verwendet wurden.
---

## Andere Techniken zum Schutz der Privatsphäre
### Sichere Mehrparteienberechnung (SMPC)
Mehrere Parteien berechnen eine Funktion über ihre kombinierten Daten, ohne ihre individuellen Eingaben preiszugeben.
| Funktion | Beschreibung |
|---------|-------------|
| **Wie es funktioniert** | Die Daten werden in über die Parteien verteilte Anteile aufgeteilt; Berechnung erfolgt auf Aktien |
| **Garantie** | Keine Partei erfährt etwas über die Eingaben der anderen |
| **Overhead** | Erheblicher Kommunikations- und Rechenaufwand |
| **Anwendungsfall** | Banken berechnen gemeinsame Risikomodelle, ohne Kundendaten weiterzugeben |
### Homomorphe Verschlüsselung (HE)
Führen Sie Berechnungen direkt mit verschlüsselten Daten durch.
| Geben Sie | ein Was es unterstützt | Overhead |
|------|---|----------|
| **Teilweise ER** | Eine Operation (Addition ODER Multiplikation) | Niedrig |
| **Etwas ER** | Begrenzte Anzahl beider Operationen | Mittel |
| **Vollständig ER** | Beliebige Berechnungen | Sehr hoch (100-1000-fache Verlangsamung) |
| Bewerbung | Beschreibung |
|-------------|-------------|
| **Private Schlussfolgerung** | Führen Sie ML-Modelle mit verschlüsselten Daten aus; verschlüsselte Vorhersagen zurückgeben |
| **Verschlüsseltes Training** | Trainieren Sie mit verschlüsselten Daten (für Deep Learning immer noch größtenteils theoretisch) |
| **Private Anfragen** | Fragen Sie eine Datenbank ab, ohne die Abfrage oder die Daten preiszugeben |
### Vertrauenswürdige Ausführungsumgebungen (TEEs)
Hardwarebasierte Isolierung (Intel SGX, ARM Trustzone), die Daten sogar vor dem Betriebssystem schützt.
| Vorteil | Einschränkung |
|-----------|------------|
| Nahezu native Leistung | Erfordert spezielle Hardware |
| Starke Sicherheitsgarantien | Begrenzter Speicher (Enklavengröße) |
| Kein kryptografischer Overhead | Seitenkanalangriffe möglich |
---

## Datenschutzbestimmungen und ML
| Verordnung | Region | Auswirkungen auf ML |
|------------|--------|-------------|
| **DSGVO** | EU | Recht auf Erklärung; Datenminimierung; Einwilligung zur Verarbeitung; Recht auf Löschung |
| **CCPA** | Kalifornien | Recht auf Auskunft, Löschung und Ablehnung des Datenverkaufs |
| **HIPAA** | USA (Gesundheitswesen) | Strenge Kontrollen von Gesundheitsdaten; Anonymisierungsanforderungen |
| **PIPL** | China | Datenlokalisierung; Einwilligungsanforderungen; Regeln für grenzüberschreitende Übermittlungen |
| **KI-Gesetz** | EU | Transparenzanforderungen; Risikoklassifizierung; verbotene Praktiken |
### Auswirkungen auf ML-Workflows
| DSGVO-Prinzip | ML-Implikation |
|----------------|---------------|
| **Datenminimierung** | Sammeln Sie nur das, was benötigt wird; Verbundlernen hilft |
| **Zweckbindung** | Daten können ohne neue Einwilligung nicht weiterverwendet werden |
| **Recht auf Löschung** | Muss in der Lage sein, die Daten einer Person aus einem trainierten Modell zu entfernen (maschinelles Verlernen) |
| **Recht auf Erklärung** | Modelle müssen ausreichend interpretierbar sein, um einzelne Vorhersagen zu erklären |
| **Privacy by Design** | Datenschutz muss von Anfang an in Systeme integriert werden |
---

## Herausforderungen
| Herausforderung | Beschreibung |
|-----------|-------------|
| **Kommunikationskosten** | Das Versenden von Modellaktualisierungen über Millionen von Geräten ist teuer |
| **Nicht-IID-Daten** | Geräte haben sehr unterschiedliche Datenverteilungen, was die Konvergenz beeinträchtigt |
| **Nachzügler** | Langsame Geräte verzögern die gesamte Runde |
| **Kompromiss zwischen Datenschutz und Nutzen** | Stärkere Privatsphäre bedeutet schlechtere Modellleistung |
| **Vergiftungsanfälle** | Böswillige Teilnehmer können das globale Modell beschädigen |
| **Modellextraktion** | Sogar gemeinsame Modellaktualisierungen können Informationen über Trainingsdaten preisgeben |
| **Hardware-Heterogenität** | Verschiedene Geräte verfügen über unterschiedliche Rechenkapazitäten |
---

## Tools und Frameworks
| Werkzeug | Zweck |
|------|---------|
| **Blume** | Open-Source-Framework für föderiertes Lernen; Framework-agnostisch |
| **TensorFlow Federated** | Googles FL-Framework für TensorFlow-Modelle |
| **PySyft** (OpenMined) | Datenschutzschonendes ML in PyTorch |
| **FATE** (Webbank) | Verbundlernplattform auf Industrieniveau |
| **BLATT** | Benchmark-Suite für föderierte Lernforschung |
| **Opacus** (Meta) | Differenzierter Datenschutz für PyTorch |
| **Googles TF-Datenschutz** | Differenzierter Datenschutz für TensorFlow |
---

## Zusammenfassung
Föderiertes Lernen und Techniken zur Wahrung der Privatsphäre lösen ein grundlegendes Spannungsfeld: Wie baut man leistungsstarke KI-Modelle auf, wenn die Daten verteilt, vertraulich oder reguliert sind? Föderiertes Lernen speichert Daten auf Geräten und gibt nur Modellaktualisierungen weiter. Differential Privacy bietet mathematische Garantien dafür, dass einzelne Beiträge nicht erkannt werden können. Sichere Berechnungen und homomorphe Verschlüsselung gehen noch einen Schritt weiter und ermöglichen die Berechnung verschlüsselter Daten. Jede Technik ist mit Kosten verbunden – Kommunikationsaufwand, verringerte Genauigkeit, Rechenaufwand –, aber zusammen bilden sie ein Toolkit zum Aufbau einer KI, die die Privatsphäre respektiert und gleichzeitig aus den Daten der Welt lernt.