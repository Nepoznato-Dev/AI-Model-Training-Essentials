<!--
---
# Metadata
title: "Causal Inference"
description: "DAGs, confounders, difference-in-differences, instrumental variables"
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
tags: [causal, inference, data-science-and-analytics]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "5 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Kausalschluss
Kausalschluss ist die Wissenschaft, die bestimmt, ob eine Sache tatsächlich eine andere verursacht – und nicht nur, ob sie miteinander korrelieren. Die Korrelation sagt Ihnen, dass sich zwei Variablen gemeinsam bewegen. Die Kausalität sagt Ihnen, dass eine Veränderung des einen auch das andere verändert. Diese Unterscheidung ist in der Medizin (funktioniert dieses Medikament?), in der Politik (reduziert diese Intervention die Armut?), in der Wirtschaft (steigert diese Werbekampagne den Umsatz?) und in der Wissenschaft (erklärt dieser Mechanismus das Phänomen?) von enormer Bedeutung.
---

## Korrelation vs. Kausalität
| Konzept | Beschreibung | Beispiel |
|---------|-------------|---------|
| **Korrelation** | Zwei Variablen bewegen sich zusammen | Sowohl der Verkauf von Eiscreme als auch die Todesfälle durch Ertrinken nehmen im Sommer zu |
| **Ursache** | Eine Variable wirkt sich direkt auf eine andere | aus Rauchen verursacht Lungenkrebs |
| **Verwirrend** | Eine dritte Variable bewirkt beides | Heißes Wetter führt sowohl zum Eisverkauf als auch zum Schwimmen (und Ertrinken) |
| **Umgekehrte Kausalität** | Die Wirkung verursacht tatsächlich die vermeintliche Ursache | Menschen kaufen Nahrungsergänzungsmittel, weil sie krank sind, nicht umgekehrt |
| **Unechte Korrelation** | Zufällige Beziehung | Pro-Kopf-Käsekonsum korreliert mit Todesfällen durch Bettlakenverheddern |
---

## Der Rahmen für potenzielle Ergebnisse
### Rubin-Kausalmodell
| Konzept | Beschreibung |
|---------|-------------|
| **Mögliche Ergebnisse** | Für jede Einheit gibt es ein Ergebnis bei Behandlung Y(1) und ein Ergebnis bei Unbehandlung Y(0) |
| **Behandlungseffekt** | Der Unterschied: Y(1) - Y(0) für eine gegebene Einheit |
| **Grundlegendes Problem** | Wir können niemals sowohl Y(1) als auch Y(0) für dieselbe Einheit beobachten – wir können nur ein | sehen
| **Durchschnittlicher Behandlungseffekt (ATE)** | Der Durchschnitt der einzelnen Behandlungseffekte in der Bevölkerung |
| **Kontrafaktisch** | Das unbeobachtete Ergebnis – was unter der anderen Bedingung passiert wäre |
### Schlüsselannahmen
| Annahme | Bedeutung | So befriedigen Sie |
|-----------|--------|----------------|
| **Ignorierbarkeit (Unbegründetheit)** | Die Behandlungszuweisung ist angesichts der beobachteten Kovariaten unabhängig von potenziellen Ergebnissen | Randomisierung; alle Störfaktoren messen |
| **Positivität (Überlappung)** | Jede Einheit hat eine Wahrscheinlichkeit ungleich Null, eine der beiden Behandlungen zu erhalten | Kovariatenüberlappung zwischen Gruppen prüfen |
| **SUTVA** (Stable Unit Treatment Value Assumption) | Die Behandlung einer Einheit hat keinen Einfluss auf das Ergebnis einer anderen; Behandlung ist konsistent | Keine Einmischung; keine versteckten Behandlungsvarianten |
| **Konsistenz** | Das beobachtete Ergebnis entspricht dem potenziellen Ergebnis der erhaltenen Behandlung | Klar definierte Behandlung |
---

## Methoden zur kausalen Schlussfolgerung
### Experimentelle Methoden
| Methode | Beschreibung | Stärke | Einschränkung |
|--------|-------------|----------|------------|
| **Randomisierte kontrollierte Studie (RCT)** | Weisen Sie Einheiten nach dem Zufallsprinzip der Behandlung oder Kontrolle zu | Goldstandard; beseitigt Verwirrung | Teuer; manchmal unethisch; darf nicht verallgemeinern |
| **A/B-Tests** | RCT im geschäftlichen/technischen Kontext | Einfach; streng | Kurzfristige Kennzahlen; Neuheitseffekte; Einmischung |
| **Switchback-Experimente** | Alternative Behandlung über Zeiträume | Bewältigt Eingriffe in Marktplätze | Erfordert eine stabile Umgebung |
### Quasi-experimentelle Methoden
| Methode | Beschreibung | Schlüsselannahme |
|--------|-------------|----------------|
| **Differenz-in-Differenzen (DiD)** | Vergleichen Sie die Veränderung der Ergebnisse zwischen behandelten und Kontrollgruppen im Laufe der Zeit | Parallele Trends: Gruppen hätten ohne Behandlung den gleichen Verlauf genommen |
| **Regressionsdiskontinuität (RD)** | Vergleichen Sie Einheiten knapp über und knapp unter einem Behandlungsgrenzwert | Einheiten in der Nähe des Cutoffs sind vergleichbar (zufällig) |
| **Instrumentelle Variablen (IV)** | Verwenden Sie eine Variable, die sich auf die Behandlung, aber nicht auf das Ergebnis auswirkt, außer durch die Behandlung | Das Instrument steht in Zusammenhang mit der Behandlung. beeinflusst das Ergebnis nur durch die Behandlung |
| **Synthetische Kontrolle** | Konstruieren Sie eine gewichtete Kombination von Kontrolleinheiten, die der behandelten Einheit entsprechen | Die synthetische Kontrolle stellt das kontrafaktische | der behandelten Einheit genau dar
| **Propensity-Score-Matching** | Vergleichen Sie behandelte und Kontrolleinheiten mit ähnlichen Behandlungswahrscheinlichkeiten | Alle Störfaktoren werden gemessen und in das Neigungsmodell | einbezogen
### Differenz-in-Differenzen (visualisiert)
| Zeitraum | Behandelte Gruppe | Kontrollgruppe | Unterschied |
|--------|--------------|---------------|------------|
| **Vorbehandlung** | Y_t_pre | Y_c_pre | Y_t_pre - Y_c_pre |
| **Nachbehandlung** | Y_t_post | Y_c_post | Y_t_post - Y_c_post |
| **DiD-Schätzung** | | | (Y_t_post – Y_t_pre) – (Y_c_post – Y_c_pre) |
---

## Gerichtete azyklische Graphen (DAGs)
DAGs sind visuelle Werkzeuge zur Kodierung kausaler Annahmen und zur Identifizierung von Störfaktoren.
### Grundstrukturen
| Struktur | Muster | Implikation |
|-----------|---------|-------------|
| **Kette** | A → B → C | A und C sind über B verbunden; Steuerung für B blockiert den Pfad |
| **Gabel** | A ← B → C | A und C werden durch B verwechselt; Steuerung für B blockiert den Pfad |
| **Collider** | A → B ← C | A und C sind unabhängig; Die Steuerung für B öffnet den Pfad (erstellt eine falsche Assoziation) |
### Regeln für DAGs
| Regel | Beschreibung |
|------|-------------|
| **Backdoor-Kriterium** | Um den kausalen Effekt von
| **Haustürkriterium** | Wenn Hintertürpfade nicht blockiert werden können, verwenden Sie Mediatoren: Schätzen Sie X → M → Y in zwei Stufen |
| **Keine Bedingung auf Collider setzen** | Die Kontrolle auf einen gemeinsamen Effekt eröffnet einen falschen Weg |
| **Keine Bedingung auf Nachkommen von Collidern setzen** | Gleiches Problem wie die Konditionierung am Collider selbst |
---

## Häufige Fallstricke
| Fallstrick | Beschreibung | Beispiel |
|---------|-------------|---------|
| **Ausgelassene Variablenverzerrung** | Fehler bei der Kontrolle eines Störfaktors | Schätzung von Bildung → Einkommen ohne Kontrolle der Fähigkeiten |
| **Überkontrolle** | Konditionierung auf einen Mediator oder Collider | Kontrolle der Berufsbezeichnung bei der Schätzung von Bildung → Verdienst |
| **Auswahlverzerrung** | Konditionierung auf eine von der Behandlung betroffene Variable | Analyse nur Berufstätige im Studium Ausbildung → Löhne |
| **Unsterbliche Zeitvoreingenommenheit** | Fehlklassifizierung der Personenzeit in Kohortenstudien | Patienten müssen lange genug überleben, um behandelt zu werden |
| **Regression zum Mittelwert** | Extremwerte bewegen sich tendenziell in Richtung Durchschnitt | Erkrankten Patienten geht es nach der Behandlung trotzdem besser |
| **Verzerrung nach der Behandlung** | Konditionierung auf Variablen, die nach der Behandlung auftreten | Kontrolle unerwünschter Ereignisse bei der Abschätzung der Arzneimittelwirksamkeit |
---

## Tools und Bibliotheken
| Werkzeug | Sprache | Beschreibung |
|------|----------|-------------|
| **Warum tun** | Python | Microsoft-Bibliothek; DAG-basierter Kausalschluss |
| **CausalML** | Python | Ubers Bibliothek für Uplift-Modellierung und kausales ML |
| **EconML** | Python | Doppelte ML, kausale Wälder, instrumentelle Variablen |
| **lineare Modelle** | Python | IV, Panel-Datenmodelle, DiD |
| **MatchIt** | R | Propensity-Score-Matching |
| **dagitty** | R / web | DAG-Analyse; Anpassungssätze identifizieren |
| **Kausale Auswirkung** | R / Python | Bayesianische Strukturzeitreihen für kausale Schlussfolgerungen |
---

## Zusammenfassung
Beim Kausalschluss geht es darum, über „was passiert ist“ hinauszugehen und zu „was passiert wäre, wenn die Dinge anders gewesen wären“. Die grundlegende Herausforderung besteht darin, dass wir niemals sowohl die behandelten als auch die unbehandelten Ergebnisse für dieselbe Einheit beobachten können – das Kontrafaktische fehlt immer. Randomisierte Experimente lösen dieses Problem, indem sie Behandlungs- und Kontrollgruppen vergleichbar machen. Wenn eine Randomisierung nicht möglich ist, versuchen quasi-experimentelle Methoden – DiD, Regressionsdiskontinuität, instrumentelle Variablen, synthetische Kontrolle – das Kontrafaktische aus Beobachtungsdaten zu rekonstruieren. DAGs helfen dabei, Annahmen explizit zu machen und die richtigen Variablen für die Kontrolle zu identifizieren. Die Schlüsselkompetenz besteht darin, sorgfältig über den Datengenerierungsprozess nachzudenken: Was verursacht was, was ist ein Confounder, was ist ein Collider und was wäre bei der Alternative passiert.