<!--
---
# Metadata
title: "Graph Neural Networks"
description: "GCNs, GATs, message passing, knowledge graphs, graph tasks"
category: "AI and Machine Learning"
subcategory: "Model Architectures"
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
    changes: "Moved to architectures/ subfolder; added subcategory field"
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
tags: [graph, neural, networks, ai-and-machine-learning]
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
# Graphische neuronale Netze
Graph Neural Networks (GNNs) sind neuronale Netzwerke, die für den Betrieb mit graphstrukturierten Daten konzipiert sind – Netzwerke aus Knoten, die durch Kanten verbunden sind. Während herkömmliche neuronale Netze mit Gittern (Bildern) oder Sequenzen (Texten) arbeiten, verarbeiten GNNs beliebige relationale Strukturen: soziale Netzwerke, molekulare Graphen, Wissensgraphen, Straßennetze, Empfehlungsgraphen und mehr. Sie sind für die Arzneimittelforschung, die Betrugserkennung, Empfehlungssysteme und alle Bereiche, in denen Beziehungen zwischen Unternehmen von Bedeutung sind, unverzichtbar geworden.
---

## Was ist ein Diagramm?
| Komponente | Beschreibung | Beispiel |
|-----------|-------------|---------|
| **Knoten (Scheitelpunkt)** | Eine Entität | Ein Mensch, das Atom eines Moleküls, eine Stadt |
| **Kante** | Eine Beziehung zwischen zwei Knoten | Freundschaft, chemische Bindung, Straße |
| **Kantengewicht** | Stärke oder Art der Beziehung | Entfernung, Ähnlichkeit, Kapazität |
| **Knotenfunktionen** | Attribute jedes Knotens | Alter, Ordnungszahl, Bevölkerung |
| **Kantenmerkmale** | Attribute jeder Kante | Art der Beziehung, Distanz |
| **Adjazenzmatrix** | Matrix A, wobei A[i][j] = 1, wenn die Knoten i und j verbunden sind | Kodiert die Diagrammstruktur |
### Arten von Diagrammen
| Geben Sie | ein Beschreibung | Beispiel |
|------|-------------|---------|
| **Ungerichtet** | Kanten haben keine Richtung | Freundschaftsnetzwerk |
| **Regie** | Kanten haben eine Richtung (A→B ≠ B→A) | Twitter-Follower |
| **Gewichtet** | Kanten haben numerische Werte | Straßennetz mit Entfernungen |
| **Heterogen** | Mehrere Knoten- und Kantentypen | Akademische Grafik (Artikel, Autoren, Veranstaltungsorte) |
| **Dynamisch** | Diagrammstruktur ändert sich im Laufe der Zeit | Soziales Netzwerk entwickelt sich im Laufe der Zeit |
| **Zweiteilig** | Zwei Arten von Knoten; Kanten nur zwischen Typen | Empfehlungsdiagramm für Benutzerelemente |
---

## Warum nicht reguläre neuronale Netze?
| Ansatz | Warum es fehlschlägt |
|----------|-------------|
| **Feed-Forward-Netzwerk** | Erfordert eine Eingabe mit fester Größe; Diagramme variieren in Größe und Struktur |
| **CNN** | Nimmt eine Gitterstruktur an; Diagramme haben kein regelmäßiges Gitter |
| **RNN/Transformer** | Nimmt eine sequentielle Reihenfolge an; Graphen haben keine natürliche Ordnung |
GNNs lösen dieses Problem, indem sie direkt auf die Graphstruktur einwirken und jeden Knoten im Kontext seiner Nachbarn verarbeiten.
---

## Kern-GNN-Architekturen
### Message Passing Framework
Die meisten GNNs folgen demselben Muster: Jeder Knoten sammelt Informationen von seinen Nachbarn, kombiniert sie und aktualisiert seine eigene Darstellung.
| Schritt | Beschreibung |
|------|-------------|
| **1. Nachricht** | Jeder Knoten sendet eine Nachricht an seine Nachbarn (basierend auf seinen aktuellen Funktionen) |
| **2. Aggregat** | Jeder Knoten sammelt und kombiniert Nachrichten von allen Nachbarn |
| **3. Aktualisieren** | Jeder Knoten aktualisiert seine eigene Darstellung mithilfe der aggregierten Nachricht |
| **4. Wiederholen** | Tun Sie dies für K Schichten → jeder Knoten erfasst Informationen von K Sprüngen entfernt |
### Wichtige GNN-Modelle
| Modell | Aggregationsmethode | Schlüsselinnovation |
|-------|-------------------|----------------|
| **GCN** (Graph Convolutional Network) | Mittelwert der Nachbarmerkmale | Einfach; wirksam; spektrale Motivation |
| **GraphSAGE** | Probe und Aggregat; kann Mittelwert, LSTM oder Pooling | verwenden Induktiv (behandelt unsichtbare Knoten); skalierbar |
| **GAT** (Graph Attention Network) | Aufmerksamkeitsgewichtete Nachbaraggregation | Erfährt, welche Nachbarn am wichtigsten sind |
| **GIN** (Graph Isomorphism Network) | Summe der Nachbarmerkmale | Maximal ausdrucksstark; kann alle durch den WL-Test unterscheidbaren Graphen unterscheiden |
| **MPNN** (Message Passing Neural Network) | Allgemeines Message-Passing-Framework | Vereinheitlicht viele GNN-Varianten |
### Wie GCN funktioniert (Schritt für Schritt)
```
For each layer:
  1. For each node, collect features from all neighbours
  2. Multiply by a learnable weight matrix W
  3. Normalise by node degree (so high-degree nodes don't dominate)
  4. Apply non-linearity (ReLU)
  5. This becomes the node's new representation
```

Nach K Schichten kodiert die Darstellung jedes Knotens Informationen von K Sprüngen weiter im Diagramm.
---

## Aufgaben auf Diagrammebene
| Aufgabe | Beschreibung | Beispiel |
|------|-------------|---------|
| **Knotenklassifizierung** | Sagen Sie die Bezeichnung jedes Knotens voraus | Benutzer als Bots oder Menschen klassifizieren |
| **Linkvorhersage** | Sagen Sie voraus, ob eine Kante existiert (oder existieren wird) | Fehlende Beziehungen vorhersagen; Verbindungen empfehlen |
| **Grafikklassifizierung** | Sagen Sie eine Beschriftung für das gesamte Diagramm voraus | Klassifizieren Sie Moleküle als giftig oder ungiftig |
| **Community-Erkennung** | Finden Sie Cluster dicht verbundener Knoten | Soziale Gruppen identifizieren |
| **Grafikerstellung** | Erzeugen Sie neue Diagramme mit den gewünschten Eigenschaften | Entwerfen Sie neue Moleküle |
---

## Anwendungen
### Wirkstoffentdeckung und Vorhersage molekularer Eigenschaften
| Aufgabe | Wie GNNs helfen |
|------|--------------|
| **Vorhersage molekularer Eigenschaften** | Stellen Sie Moleküle als Graphen dar (Atome=Knoten, Bindungen=Kanten); Vorhersage von Toxizität, Löslichkeit und Bindungsaffinität |
| **Arzneimittelwechselwirkung** | Modellieren Sie Medikamente und Ziele als Diagramm. nachteilige Wechselwirkungen vorhersagen |
| **De-novo-Arzneimitteldesign** | Generieren Sie neuartige molekulare Diagramme mit den gewünschten Eigenschaften |
### Empfehlungssysteme
| Ansatz | Beschreibung |
|----------|-------------|
| **Benutzerelementdiagramm** | Benutzer und Elemente sind Knoten; Käufe/Ansichten sind Kanten |
| **Graphenbasiertes kollaboratives Filtern** | GNNs verbreiten Präferenzen über das Diagramm |
| **Wissensdiagramm-Empfehlungen** | Kombinieren Sie Benutzerpräferenzen mit Artikelwissen (Genres, Schauspieler, Regisseure) |
### Betrugserkennung
| Bewerbung | Diagrammstruktur |
|-------------|----------------|
| **Finanzbetrug** | Transaktionen bilden ein Diagramm; betrügerische Muster entstehen als Subgraph-Strukturen |
| **Versicherungsbetrug** | Antragsteller, Anbieter und Policen bilden ein Diagramm. Betrügerringe werden entdeckt |
| **Kontoübernahmen** | Anmeldemuster bilden ein Diagramm. anormale Verbindungen signalisieren Kompromittierung |
### Wissensgraphen
| Aufgabe | Beschreibung |
|------|-------------|
| **Linkvorhersage** | Sagen Sie fehlende Fakten voraus (z. B. „Paris ist die Hauptstadt von?“) |
| **Entitätsauflösung** | Stellen Sie fest, ob sich zwei Erwähnungen auf dieselbe Entität beziehen |
| **Fragenbeantwortung** | Navigieren Sie durch die Grafik, um Antworten zu finden |
---

## Fortgeschrittene GNN-Konzepte
### Überglättung
| Problem | Beschreibung | Lösung |
|---------|-------------|----------|
| **Überglättung** | Nach vielen Schichten werden alle Knotendarstellungen ähnlich | Begrenzen Sie die Tiefe (2-4 Schichten); Restverbindungen verwenden; Springwissen nutzen |
### Übermäßiges Quetschen
| Problem | Beschreibung | Lösung |
|---------|-------------|----------|
| **Übermäßiges Quetschen** | Informationen von entfernten Knoten werden in Vektoren fester Größe komprimiert | Verwenden Sie Graphtransformatoren. hierarchisches Pooling |
### Graphtransformatoren
| Modell | Hauptmerkmal |
|-------|-------------|
| **Grafiktransformator** | Wenden Sie die standardmäßige Transformer-Aufmerksamkeit auf alle Knotenpaare an |
| **GPS** (Graph Prompting System) | Kombinieren Sie lokale GNN-Ebenen mit globalen Transformer-Ebenen |
| **Graphormer** | Positionskodierung basierend auf der Diagrammstruktur hinzufügen |
### Heterogene Graphnetzwerke
| Modell | Beschreibung |
|-------|-------------|
| **R-GCN** | Relationales GCN; unterschiedliche Gewichtsmatrizen für unterschiedliche Kantentypen |
| **HAN** | Heterogenes Aufmerksamkeitsnetzwerk; Aufmerksamkeit auf verschiedene Knoten- und Kantentypen |
| **HetGNN** | Heterogenes graphisches neuronales Netzwerk; verarbeitet mehrere Knotentypen |
---

## Skalierbarkeit
| Herausforderung | Lösung |
|-----------|----------|
| **Große Diagramme** (Millionen Knoten) | Mini-Batch-Training; Nachbarprobenahme |
| **Speicher** | Graphpartitionierung über GPUs |
| **Geschwindigkeit** | Sparse-Matrix-Operationen; Fachbibliotheken |
### Sampling-Strategien
| Strategie | Beschreibung |
|----------|-------------|
| **Knoten-Sampling** | Probieren Sie eine Teilmenge von Knoten und ihren K-Hop-Nachbarschaften aus |
| **Kantenabtastung** | Beispielkanten und die Knoten, die sie verbinden |
| **Cluster-Sampling** | Partitionieren Sie den Graphen in Cluster; auf Clustern trainieren |
| **Random Walk Sampling** | Stichprobenknoten über Zufallswanderungen von Zielknoten |
---

## Tools und Frameworks
| Werkzeug | Zweck |
|------|---------|
| **PyTorch Geometrisch (PyG)** | Beliebteste GNN-Bibliothek; Umfangreicher Satz an Modellen und Datensätzen |
| **DGL** (Deep Graph Library) | Framework-agnostisch; unterstützt PyTorch, TensorFlow, MXNet |
| **NetzwerkX** | Klassische Graphalgorithmen; Datenmanipulation |
| **OGB** (Open Graph Benchmark) | Standard-Benchmarks und Datensätze für die GNN-Forschung |
| **CogDL** | Deep Learning für Grafiken; forschungsorientiert |
| **Spektral** | GNN-Bibliothek für TensorFlow/Keras |
---

## Zusammenfassung
Graphische neuronale Netze erweitern Deep Learning auf relationale Daten – Netzwerke, Moleküle, Wissensgraphen und jedes System, in dem Entitäten verbunden sind. Sie funktionieren, indem sie Nachrichten zwischen Nachbarn weiterleiten, sodass jeder Knoten aus seinem lokalen Kontext lernen kann. GNNs haben ihre stärksten Anwendungen in der Arzneimittelforschung, Empfehlungssystemen, Betrugserkennung und Wissensgraphen gefunden. Das Feld entwickelt sich in Richtung Graphtransformatoren, heterogener Graphen und skalierbarem Training für riesige reale Netzwerke. Wenn Ihre Daten Beziehungen aufweisen, sind GNNs wahrscheinlich eine Überlegung wert.