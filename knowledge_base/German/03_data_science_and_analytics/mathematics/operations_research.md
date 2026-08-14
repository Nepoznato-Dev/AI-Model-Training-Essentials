---
# Metadata
title: "Operations Research"
description: "Linear programming formulations, transportation and assignment problems, network flow optimization, integer programming, dynamic programming, queueing theory, inventory models, and scheduling"
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
    changes: "Initial deep-dive into operations research"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2027-02-10"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-10"

# Classification
tags: [operations-research, linear-programming, transportation-problem, dynamic-programming, queueing-theory, inventory-models, scheduling, network-flow]
difficulty_level: "intermediate"
prerequisites:
  - "mathematics.md"
  - "optimization.md"
  - "graph_theory.md"
estimated_reading_time: "25 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# Operationsforschung
Unter Operations Research (OR) versteht man die Anwendung mathematischer Methoden zur Entscheidungsfindung. Das im Zweiten Weltkrieg für die Militärlogistik gegründete Unternehmen optimiert heute Lieferketten, plant Fluggesellschaften, leitet Lieferflotten, verwaltet Bestände und verteilt Ressourcen in allen Branchen. OR bietet das mathematische Werkzeug, um unter Randbedingungen die bestmöglichen Entscheidungen zu treffen.
---

## Lineare Programmierformulierungen
### Standardformular
cᵀx minimieren
Vorbehaltlich: Ax = b, x ≥ 0
### Gängige LP-Formulierungen
**Produktmix:**
- Entscheidungsvariablen: xⱼ = Menge des zu produzierenden Produkts j
- Ziel: Gewinn maximieren Σ pⱼxⱼ
- Einschränkungen: Ressourcengrenzen Σ aᵢⱼxⱼ ≤ bᵢ
**Ernährungsproblem:**
- Entscheidungsvariablen: xⱼ = zu kaufende Lebensmittelmenge j
- Ziel: Kosten Σ cⱼxⱼ minimieren
- Einschränkungen: Nährstoffbedarf Σ nᵢⱼxⱼ ≥ rᵢ
**Mischungsproblem:**
- Entscheidungsvariablen: xⱼ = Anteil der Zutat j in der Mischung
- Ziel: Kosten minimieren
- Einschränkungen: Qualitätsanforderungen (Oktanzahl, Festigkeit usw.)
### Arbeitsbeispiel: Produktionsplanung
Eine Fabrik stellt die Produkte A und B her.
- A erfordert 2 Stunden Arbeit, 1 kg Material; Gewinn 30 $
- B erfordert 1 Stunde Arbeit, 3 kg Material; Gewinn 40 $
- Verfügbar: 40 Arbeitsstunden, 30 kg Material
**Formulierung:**
- Maximieren: 30x_A + 40x_B
- Vorbehaltlich: 2x_A + x_B ≤ 40 (Arbeit)
- x_A + 3x_B ≤ 30 (Material)
- x_A, x_B ≥ 0
**Lösung:** Eckpunkte des zulässigen Bereichs: (0,0), (20,0), (18,4), (0,10)
- (0,0): Gewinn = 0
- (20,0): Gewinn = 600
- (18,4): Gewinn = 700 ← optimal
- (0,10): Gewinn = 400
---

## Transportproblem
Transport von Gütern von m Quellen zu n Zielen zu minimalen Kosten.
### Formulierung
- Entscheidungsvariablen: xᵢⱼ = Menge, die von der Quelle i zum Ziel j versendet wird
- Ziel: Σᵢ Σⱼ cᵢⱼxᵢⱼ minimieren
- Vorbehaltlich: Σⱼ xᵢⱼ = sᵢ (Angebotsbeschränkungen)
- Σᵢ xᵢⱼ = dⱼ (Nachfragebeschränkungen)
- xᵢⱼ ≥ 0
### Lösungsmethoden
| Methode | Beschreibung | Qualität der Erstlösung |
|--------|-------------|--------------------------|
| **Nordwestecke** | Oben links beginnen, gierig zuordnen | Machbar, aber oft schlecht |
| **Vogels Näherung** | Strafkosten berücksichtigen | Bessere Erstlösung |
| **MODI / Trittstein** | Ausgangslösung iterativ verbessern | Findet optimale |
### Ausgearbeitetes Beispiel
| | D1 | D2 | D3 | Versorgung |
|---|----|----|----|--------|
| S1 | 2 | 3 | 1 | 50 |
| S2 | 4 | 1 | 5 | 30 |
| S3 | 3 | 2 | 4 | 20 |
| Nachfrage | 40 | 30 | 30 | 100 |
---

## Zuweisungsproblem
Zuweisen von n Arbeitskräften zu n Jobs (eins zu eins), um die Gesamtkosten zu minimieren.
### Formulierung
- Entscheidungsvariablen: xᵢⱼ ∈ {0, 1} (1, wenn Arbeiter i dem Job j zugewiesen ist)
- Minimieren: Σᵢ Σⱼ cᵢⱼxᵢⱼ
- Vorbehaltlich: Σⱼ xᵢⱼ = 1 (jeder Arbeiter bekommt einen Job)
- Σᵢ xᵢⱼ = 1 (jeder Job bekommt einen Arbeiter)
### Ungarischer Algorithmus
| Eigentum | Wert |
|----------|-------|
| Zeitkomplexität | O(n³) |
| Optimal? | Ja |
| Ansatz | Matrixreduktion + Mindestdeckung |
**Schritte:**
1. Subtrahieren Sie die Zeilenminima von jeder Zeile
2. Subtrahieren Sie die Spaltenminima von jeder Spalte
3. Überdecken Sie alle Nullen mit der minimalen Anzahl von Zeilen
4. Wenn Zeilen = n, wird die optimale Zuordnung zwischen Nullen gefunden
5. Ansonsten Matrix anpassen und wiederholen
---

## Netzwerkflussoptimierung
### Minimaler Kostenfluss
Finden Sie bei einem Netzwerk mit Kapazitäten und Kosten an den Rändern den Fluss, der die Anforderungen bei minimalen Kosten erfüllt.
**Formulierung:**
- Minimieren: Σ cᵢⱼxᵢⱼ
- Vorbehaltlich: Flusserhaltung an jedem Knoten
- Kapazitätsbeschränkungen: 0 ≤ xᵢⱼ ≤ uᵢⱼ
### Kürzester Pfad als Netzwerkfluss
Das Kürzeste-Wege-Problem ist ein Sonderfall des Minimalkostenflusses (1 Einheit von s nach t senden).
### Anwendungen
| Bewerbung | Netzwerkmodell |
|-------------|--------------|
| Lieferkette | Knoten = Lager, Kanten = Schifffahrtswege |
| Kommunikation | Knoten = Router, Kanten = Verbindungen mit Bandbreite |
| Verkehr | Knoten = Kreuzungen, Kanten = Straßen mit Kapazität |
| Projektmanagement | CPM/PERT-Netzwerke |
---

## Dynamische Programmierung
**Dynamische Programmierung (DP)** löst komplexe Probleme, indem sie sie in überlappende Teilprobleme aufteilt.
### Bellmans Optimalitätsprinzip
Eine optimale Richtlinie hat die Eigenschaft, dass unabhängig vom Ausgangszustand und der Ausgangsentscheidung die verbleibenden Entscheidungen eine optimale Richtlinie für den resultierenden Zustand darstellen müssen.
### Schlüsselelemente
| Element | Beschreibung |
|---------|-------------|
| **Bühne** | Entscheidungszeitpunkt (Zeitschritt, Itemindex) |
| **Staat** | Zur Entscheidungsfindung benötigte Informationen |
| **Entscheidung** | In jeder Phase getroffene Entscheidungen |
| **Wiederholung** | Optimaler Wert auf Stufe n im Hinblick auf Stufe n−1 |
### Klassische DP-Probleme
| Problem | Wiederholung | Komplexität |
|---------|-----------|------------|
| **Fibonacci** | F(n) = F(n−1) + F(n−2) | O(n) mit Memoisierung |
| **Rucksack** | V(i,w) = max(V(i−1,w), vᵢ + V(i−1,w−wᵢ)) | O(nW) |
| **Kürzester Weg** | d(i) = min_j(d(j) + cⱼᵢ) | O(V²) oder O(E log V) |
| **Entfernung bearbeiten** | D(i,j) = min(D(i−1,j)+1, D(i,j−1)+1, D(i−1,j−1)+Kosten) | O(mn) |
| **Längste gemeinsame Teilsequenz** | L(i,j) = L(i−1,j−1)+1 bei Übereinstimmung, sonst max(L(i−1,j), L(i,j−1)) | O(mn) |
| **Matrixkettenmultiplikation** | M(i,j) = min_k(M(i,k) + M(k+1,j) + pᵢ₋₁pₖpⱼ) | O(n³) |
### Arbeitsbeispiel: 0/1 Rucksack
Elemente: {Gewicht: Wert} = {(2, 12), (3, 10), (4, 8), (5, 11)}. Kapazität W = 7.
V(i, w) = Maximalwert unter Verwendung der ersten i Elemente mit der Kapazität w
| ich\w | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|-----|---|---|---|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 1 | 0 | 0 | 12 | 12 | 12 | 12 | 12 | 12 |
| 2 | 0 | 0 | 12 | 12 | 12 | 22 | 22 | 22 |
| 3 | 0 | 0 | 12 | 12 | 12 | 22 | 22 | 22 |
| 4 | 0 | 0 | 12 | 12 | 12 | 22 | 23 | 23 |
Optimal: V(4, 7) = 23 (Items 1 und 4: Gewicht 2+5=7, Wert 12+11=23).
---

## Warteschlangentheorie
Die Warteschlangentheorie untersucht Warteschlangen – wie lang sie sind, wie lange Sie warten und wie Sie beides reduzieren können.
### Kendalls Notation
A/B/c/K/N/D wobei:
- A = Ankunftsprozess (M = Markovian/Poisson, D = deterministisch, G = allgemein)
- B = Serviceprozess (gleiche Optionen)
- c = Anzahl der Server
- K = Kapazität (Standard ∞)
- N = Bevölkerung (Standard ∞)
- D = Disziplin (FIFO, LIFO, Priorität)
### M/M/1-Warteschlange (Einzelserver)
| Metrisch | Formel |
|--------|---------|
| Nutzung | ρ = λ/μ |
| Durchschnittliche Anzahl im System | L = ρ/(1−ρ) |
| Durchschnittliche Zeit im System | W = 1/(μ−λ) |
| Durchschnittliche Anzahl in der Warteschlange | L_q = ρ²/(1−ρ) |
| Durchschnittliche Wartezeit | W_q = ρ/(μ−λ) |
wobei λ = Ankunftsrate, μ = Servicerate, ρ = Auslastung.
### M/M/c-Warteschlange (mehrere Server)
| Metrisch | Formel |
|--------|---------|
| Nutzung | ρ = λ/(cμ) |
| Wartewahrscheinlichkeit (Erlang C) | P_w = komplexe Formel mit ρ und c |
| Durchschnittliche Warteschlangenlänge | L_q = P_w · ρ/(1−ρ) |
### Littles Gesetz
L = λW (durchschnittliche Anzahl im System = Ankunftsrate × durchschnittliche Zeit)
Dies gilt für JEDES Warteschlangensystem, unabhängig von Ankunfts-/Dienstverteilungen.
### Anwendungsbeispiele
| Szenario | Warteschlangenmodell |
|----------|-------------|
| Callcenter | M/M/c (c-Agenten) |
| Webserver-Anfragen | M/M/1 oder M/G/1 |
| Krankenhausnotfall | M/G/c mit Prioritäten |
| Fertigungslinie | Netzwerk von Warteschlangen |
| Computer-CPU-Planung | M/M/1-Prozessorfreigabe |
---

## Inventarmodelle
### Wirtschaftliche Bestellmenge (EOQ)
Die optimale Bestellmenge, die die gesamten Lagerkosten minimiert.
Q* = √(2DS/H)
| Variable | Bedeutung |
|----------|---------|
| D | Jährlicher Bedarf |
| S | Bestellkosten pro Bestellung |
| H | Haltekosten pro Einheit und Jahr |
| Q* | Optimale Bestellmenge |
**Gesamtkosten bei Q*:** TC = √(2DSH)
### Erweiterungen
| Modell | Erweiterung |
|-------|-----------|
| **EOQ mit Rabatten** | Mengenrabatte verändern die Kostenfunktion |
| **Produktionsauftragsmenge** | Artikel werden nach und nach hergestellt und nicht auf einmal geliefert |
| **(s, Q)-Modell** | Bestellen Sie Q-Einheiten neu, wenn der Lagerbestand auf Level s sinkt |
| **(s, S)-Modell** | Bestellen Sie bis zu S, wenn der Lagerbestand auf s | sinkt
| **Newsvendor-Modell** | Einzelperiodische, unsichere Nachfrage |
### Newsvendor-Modell
Optimale Bestellmenge für verderbliche Lagerbestände in einem Zeitraum:
P(D ≤ Q*) = c_u / (c_u + c_o)
wobei c_u = Minderkosten (entgangener Gewinn) und c_o = Mehrkosten (Verschwendung).
---

## Terminplanung
### Werkstattplanung
| Notation | Bedeutung |
|----------|---------|
| n/m/J/C_max | n Jobs, m Maschinen, Job-Shop, Makespan minimieren |
| Flow-Shop | Alle Jobs besuchen Maschinen in derselben Reihenfolge |
| Lohnfertigung | Jeder Job hat seinen eigenen Maschinenablauf |
| Shop eröffnen | Keine Bestellbeschränkungen |
### Prioritätsregeln
| Regel | Beschreibung | Wirkung |
|------|-------------|--------|
| FCFS | Wer zuerst kommt, mahlt zuerst | In Ordnung, aber nicht optimal |
| SPT | Kürzeste Bearbeitungszeit zuerst | Minimiert die durchschnittliche Fertigstellung |
| EDD | Frühester Fälligkeitstermin zuerst | Minimiert maximale Verspätung |
| CR | Kritisches Verhältnis (verbleibendes Fälligkeitsdatum / Bearbeitungszeit) | Ausgewogen |
| LPT | Längste Bearbeitungszeit zuerst | Gut für Makespan auf parallelen Maschinen |
### Johnsons Algorithmus (2-Machine Flow Shop)
Für n Jobs auf 2 Maschinen, Minimierung der Makespan:
1. Finden Sie den Auftrag mit der kürzesten Bearbeitungszeit
2. Wenn es sich auf Maschine 1 befindet, planen Sie es zuerst; Wenn auf Maschine 2, planen Sie es zuletzt
3. Entfernen Sie den Job und wiederholen Sie den Vorgang
Optimal für 2 Maschinen; NP-hart für 3+ Maschinen.
---

## Relevanz für maschinelles Lernen und Datenwissenschaft
| ODER-Konzept | Bewerbung |
|-----------|-------------|
| Lineare Programmierung | Ressourcenallokation, Portfoliooptimierung, Werbebudgetallokation |
| Transport/Auftrag | Logistik, Ride-Sharing-Matching, Aufgabenzuweisung |
| Netzwerkfluss | Optimierung der Lieferkette, Datenverkehrsrouting im Rechenzentrum |
| Dynamische Programmierung | Sequenzausrichtung (Bioinformatik), Viterbi-Algorithmus (HMMs), RL (Bellman-Gleichung) |
| Warteschlangentheorie | Serverkapazitätsplanung, Latenzmodellierung, Cloud-Ressourcenzuweisung |
| Inventarmodelle | Integration der Nachfrageprognose, Supply Chain ML |
| Terminplanung | ML-Pipeline-Orchestrierung, GPU-Jobplanung, Hyperparameter-Suchplanung |
| Ganzzahlprogrammierung | Funktionsauswahl (binär), Modellauswahl, Netzwerkdesign |
---

## Zusammenfassung
| Thema | Kernproblem | Schlüsselmethode |
|-------|-------------|------------|
| LP-Formulierungen | Lineares Ziel mit Einschränkungen optimieren | Simplex, Innenpunkt |
| Transport | Waren zu minimalen Kosten versenden | MODI, Sprungbrett |
| Aufgabe | Arbeitskräfte den Jobs zuordnen | Ungarischer Algorithmus |
| Netzwerkfluss | Routenfluss durch ein Netzwerk | Min-Cost-Flow-Algorithmen |
| Dynamische Programmierung | Überlappende Teilprobleme | Bellmans Prinzip, Auswendiglernen |
| Warteschlangentheorie | Warteschlangenanalyse | M/M/1, Little'sches Gesetz |
| Inventar | Wann und wie viel bestellen | EOQ, Nachrichtenanbieter |
| Terminplanung | Sequenzjobs auf Maschinen | Prioritätsregeln, Johnsons Algorithmus |
Operations Research transformiert die Entscheidungsfindung von der Kunst zur Wissenschaft. Durch die mathematische Formulierung realer Probleme bietet OR nachweislich optimale (oder nahezu optimale) Lösungen für Logistik-, Terminplanungs-, Ressourcenzuweisungs- und Planungsprobleme, die jede Branche betreffen. Für Datenwissenschaftler ergänzen OR-Methoden maschinelles Lernen: Während ML vorhersagt, schreibt OR vor – und zusammen bilden sie die Grundlage intelligenter Entscheidungssysteme.