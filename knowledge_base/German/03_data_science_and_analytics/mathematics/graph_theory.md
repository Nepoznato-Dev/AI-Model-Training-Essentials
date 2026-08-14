---
# Metadata
title: "Graph Theory"
description: "Graph representations, trees, traversals, shortest paths, minimum spanning trees, network flows, and spectral graph theory"
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
    changes: "Initial deep-dive into graph theory"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2027-02-10"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-10"

# Classification
tags: [graph-theory, trees, traversals, shortest-paths, spanning-trees, network-flows, spectral-graph-theory]
difficulty_level: "intermediate"
prerequisites:
  - "mathematics.md"
  - "discrete_mathematics.md"
estimated_reading_time: "28 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# Graphentheorie
Ein **Graph** ist eine mathematische Struktur, die aus Eckpunkten (Knoten) besteht, die durch Kanten (Links) verbunden sind. Diagramme modellieren Beziehungen: soziale Netzwerke, Straßenkarten, neuronale Netze, Abhängigkeiten, Kommunikationskanäle. Die Graphentheorie – die Untersuchung dieser Strukturen – liefert Algorithmen und Theoreme, die für die Informatik, das Operations Research und die Datenwissenschaft von zentraler Bedeutung sind.
---

## Grundlegende Konzepte
### Definitionen
| Begriff | Definition | Notation |
|------|------------|----------|
| **Grafik** | Ein Paar G = (V, E) von Eckpunkten und Kanten | G |
| **Scheitelpunkt (Knoten)** | Ein Element von V | v, u, w |
| **Kante** | Eine Verbindung zwischen zwei Eckpunkten | e = (u, v) oder {u, v} |
| **Bestellung** | Anzahl der Eckpunkte | \|V\| = n |
| **Größe** | Anzahl der Kanten | \|E\| = m |
| **Abschluss** | Anzahl der zu einem Scheitelpunkt inzidenten Kanten | Grad(v) |
| **Pfad** | Folge unterschiedlicher Eckpunkte, die durch Kanten verbunden sind | v₁, v₂, ..., vₖ |
| **Zyklus** | Ein Pfad, der am selben Scheitelpunkt | beginnt und endet v₁ → v₂ → ... → vₖ → v₁ |
| **Verbunden** | Zwischen jedem Eckpunktpaar | existiert ein Pfad — |
| **Komponente** | Ein maximal zusammenhängender Teilgraph | — |
| **Untergraph** | Ein Graph, der aus einer Teilmenge von V und E | gebildet wird H ⊆ G |
### Arten von Diagrammen
| Geben Sie | ein Beschreibung | Beispiel |
|------|-------------|---------|
| **Ungerichtet** | Kanten haben keine Richtung | Freundschaftsnetzwerk |
| **Gerichtet (Digraph)** | Kanten haben eine Richtung (Bögen) | Webseiten-Links |
| **Gewichtet** | Kanten tragen numerische Werte | Straßenentfernungen |
| **Ungewichtet** | Alle Kanten sind äquivalent | Soziale Verbindungen |
| **Einfach** | Keine Schleifen, keine Mehrfachkanten | Die meisten Lehrbuchgrafiken |
| **Multigraph** | Mehrere Kanten zwischen denselben Eckpunkten zulässig | Flugrouten (mehrere Flüge zwischen Städten) |
| **Vollständig** | Jedes Eckpunktpaar ist verbunden | Kₙ hat n(n−1)/2 Kanten |
| **Zweiteilig** | Die Scheitelpunkte sind in zwei Gruppen aufgeteilt; Kanten kreuzen nur Gruppen | Empfehlungsmatrizen für Benutzerelemente |
| **Planar** | Kann ohne Kantenübergänge gezeichnet werden | Leiterplattenlayouts |
| **Baum** | Verbundener, azyklischer Graph | Entscheidungsbäume, Dateisysteme |
| **DAG** | Gezielte, keine gerichteten Zyklen | Aufgabenplanung, Abhängigkeitsdiagramme |
### Das Handshake-Lemma
Die Summe aller Scheitelpunktgrade entspricht der doppelten Anzahl der Kanten:
Σᵥ deg(v) = 2|E|
**Folge:** Jeder Graph hat eine gerade Anzahl von Eckpunkten ungeraden Grades.
**Beispiel:** In einer Gruppe von 10 Personen, in der jeder genau 3 anderen die Hand schüttelt: Σ Grad = 30, also |E| = insgesamt 15 Handshakes.
---

## Diagrammdarstellungen
Wie Sie ein Diagramm im Speicher speichern, bestimmt die Effizienz jedes darauf ausgeführten Algorithmus.
| Darstellung | Raum | Kantensuche | Nachbarn iterieren | Am besten für |
|----------------|-------|-------------|------|----------|
| **Adjazenzmatrix** | O(n²) | O(1) | O(n) | Dichte Diagramme, schnelle Kantentests |
| **Adjazenzliste** | O(n + m) | O(Grad(v)) | O(Grad(v)) | Spärliche Diagramme, die meisten realen Netzwerke |
| **Kantenliste** | O(m) | O(m) | O(m) | Einfache Algorithmen, Kruskals MST |
| **Inzidenzmatrix** | O(n · m) | O(m) | O(m) | Spezialisierte Algorithmen |
### Adjazenzmatrix
Eine n × n-Matrix A, wobei A[i][j] = 1, wenn Kante (i,j) existiert, andernfalls 0. Für gewichtete Diagramme ist A[i][j] = Gewicht.
**Eigenschaften:**
- Symmetrisch für ungerichtete Graphen
- Aᵏ[i][j] = Anzahl der Spaziergänge der Länge k von i nach j
- Eigenwerte von A offenbaren strukturelle Eigenschaften (siehe Spektralgraphentheorie)
### Adjazenzliste
Ein Array (oder Hash-Map), in dem jeder Scheitelpunkt v eine Liste seiner Nachbarn speichert.
```
Vertex 0: [1, 3]
Vertex 1: [0, 2, 3]
Vertex 2: [1, 3]
Vertex 3: [0, 1, 2]
```

Dies ist die gebräuchlichste Darstellung für reale Graphen, die typischerweise dünn besetzt sind (m ≪ n²).
---

## Bäume
Ein **Baum** ist ein zusammenhängender, azyklischer ungerichteter Graph. Ein **Wald** ist eine disjunkte Vereinigung von Bäumen.
### Eigenschaften von Bäumen
Für einen Baum mit n Eckpunkten:
- Es hat genau n − 1 Kanten
- Zwischen zwei beliebigen Eckpunkten gibt es genau einen Pfad
- Durch das Entfernen einer Kante wird die Verbindung getrennt
- Durch das Hinzufügen einer beliebigen Kante entsteht genau ein Zyklus
### Baumarten
| Geben Sie | ein Beschreibung | Bewerbung |
|------|-------------|-------------|
| **Verwurzelter Baum** | Ein als Wurzel | bezeichneter Scheitelpunkt Dateisysteme, Organigramme |
| **Binärbaum** | Jeder Knoten hat höchstens 2 Kinder | BSTs, Ausdrucksanalyse, Entscheidungsbäume |
| **Ausgeglichener Baum** | Die Höhe beträgt O(log n) | AVL-Bäume, Rot-Schwarz-Bäume (Datenbanken) |
| **Spanning Tree** | Untergraph, der alle Eckpunkte enthält und ein Baum ist | Netzwerkdesign, Approximationsalgorithmen |
| **Minimaler Spannbaum** | Spannbaum mit minimalem Gesamtkantengewicht | Netzwerkdesign, Clustering |
| **Sterndiagramm** | Ein zentraler Knoten, der mit allen anderen verbunden ist | Hub-and-Spoke-Netzwerke |
### Eigenschaften des Binärbaums
| Eigentum | Formel |
|----------|---------|
| Max. Knoten in der Tiefe d | 2ᵈ |
| Max. Knoten im Baum mit der Höhe h | 2ʰ⁺¹ − 1 |
| Mindesthöhe für n Knoten | ⌊log₂(n)⌋ |
| Blattknoten im vollständigen Binärbaum | Interne Knoten + 1 |
### Baumdurchquerungen
| Durchquerung | Bestellen | Anwendungsfall |
|-----------|-------|----------|
| **Vorbestellung** | Wurzel → Links → Rechts | Kopieren eines Baums, Präfixausdruck |
| **In Ordnung** | Links → Wurzel → Rechts | Sortierte Ausgabe von BST |
| **Nachbestellung** | Links → Rechts → Wurzel | Einen Baum löschen, Postfix-Ausdruck |
| **Level-Reihenfolge (BFS)** | Ebene für Ebene, von links nach rechts | Kürzester Pfad im ungewichteten Baum |
---

## Graphdurchquerungen
Durchquerungsalgorithmen besuchen systematisch jeden erreichbaren Scheitelpunkt.
### Breitensuche (BFS)
Erkundet Scheitelpunkte Schicht für Schicht mithilfe einer **Warteschlange**.
| Eigentum | Wert |
|----------|-------|
| Datenstruktur | Warteschlange (FIFO) |
| Zeitkomplexität | O(V + E) |
| Raumkomplexität | O(V) |
| Findet den kürzesten Weg? | Ja (ungewichtete Diagramme) |
| Vollständig? | Ja (erkundet alle erreichbaren Scheitelpunkte) |
**Algorithmus:**
1. Beginnen Sie am Quellscheitelpunkt s. Mark ist zu Besuch. s in die Warteschlange stellen.
2. Während die Warteschlange nicht leer ist: Vertex u aus der Warteschlange entfernen. Für jeden nicht besuchten Nachbarn v von u: v besucht markieren, v in die Warteschlange stellen.
**Anwendungen:** kürzester Weg in ungewichteten Diagrammen, verbundene Komponenten, Bipartititätstests, Web-Crawling.
### Tiefensuche (DFS)
Erforscht so tief wie möglich, bevor es zurückgeht, mithilfe eines **Stapels** (oder einer Rekursion).
| Eigentum | Wert |
|----------|-------|
| Datenstruktur | Stapel (LIFO) / Rekursion |
| Zeitkomplexität | O(V + E) |
| Raumkomplexität | O(V) |
| Findet den kürzesten Weg? | Nein |
| Vollständig? | Ja (für endliche Graphen) |
**Algorithmus:**
1. Beginnen Sie am Scheitelpunkt s. Mark ist zu Besuch.
2. Für jeden nicht besuchten Nachbarn v von s: rekursives DFS von v.
**DFS klassifiziert Kanten in:**
- **Baumkanten:** Teil des DFS-Baums
- **Hintere Kanten:** verbinden einen Scheitelpunkt mit seinem Vorgänger (zeigen Zyklen an)
- **Vorwärtskanten:** verbinden einen Scheitelpunkt mit seinem Nachkommen
- **Kanten kreuzen:** Eckpunkte in verschiedenen Zweigen verbinden
**Anwendungen:** Topologische Sortierung, Zykluserkennung, stark verbundene Komponenten, Lösen von Labyrinthen.
### BFS- und DFS-Vergleich
| Kriterium | BFS | DFS |
|-----------|-----|-----|
| Strategie | Breit dann tief | Tief dann breit |
| Erinnerung | Höher (Speichergrenze) | Unten (Speicherpfad) |
| Kürzester Weg (ungewichtet) | Garantiert | Nicht garantiert |
| Verwenden Sie diese Option, wenn die Lösung kurz vor dem Start steht | Besser | Schlimmer noch |
| Verwenden Sie diese Option, wenn das Diagramm sehr tief ist | Schlimmer noch | Besser |
| Topologische Sortierung | Kahns Algorithmusvariante | Standardansatz |
---

## Algorithmen für den kürzesten Weg
Das Finden des kürzesten Weges zwischen Knoten ist eines der praktisch wichtigsten Diagrammprobleme.
### Dijkstras Algorithmus
Findet kürzeste Pfade von einer einzelnen Quelle zu allen anderen Eckpunkten in einem Diagramm mit **nicht negativen** Kantengewichten.
| Eigentum | Wert |
|----------|-------|
| Kantengewichte | Muss ≥ 0 | sein
| Zeit (binärer Heap) | O((V + E) log V) |
| Zeit (Fibonacci-Haufen) | O(E + V log V) |
| Gierig? | Ja |
| Verarbeitet negative Gewichte? | Nein |
**Algorithmus:**
1. Initialisieren Sie dist[s] = 0, dist[v] = ∞ für alle v ≠ s. Prioritätswarteschlange Q mit allen Eckpunkten.
2. Während Q nicht leer ist: Extrahieren Sie den Scheitelpunkt u mit minimalem Abstand. Für jeden Nachbarn v von u mit Kantengewicht w: Wenn dist[u] + w < dist[v], aktualisiere dist[v] = dist[u] + w.
**Arbeitsbeispiel:**```
Graph: A --1-- B --2-- C --1-- D
       A --4-- C
       B --1-- D

Shortest paths from A:
A → B: 1 (direct)
A → D: 2 (A→B→D)
A → C: 3 (A→B→C, NOT A→C=4)
```

### Bellman-Ford-Algorithmus
Verarbeitet **negative** Kantengewichte und erkennt negative Zyklen.
| Eigentum | Wert |
|----------|-------|
| Kantengewichte | Beliebig (erkennt negative Zyklen) |
| Zeitkomplexität | O(V · E) |
| Raumkomplexität | O(V) |
| Bewältigt man negative Zyklen? | Ja (erkennt und meldet) |
**Algorithmus:**
1. Initialisieren Sie dist[s] = 0, dist[v] = ∞ für alle v ≠ s.
2. Wiederholen Sie V − 1 Mal: ​​für jede Kante (u, v) mit Gewicht w: Wenn dist[u] + w < dist[v], aktualisieren Sie dist[v].
3. Auf negative Zyklen prüfen: Wenn eine Kante noch entspannt werden kann, liegt ein negativer Zyklus vor.
### Floyd-Warshall-Algorithmus
Findet die kürzesten Pfade zwischen **allen Paaren** von Scheitelpunkten.
| Eigentum | Wert |
|----------|-------|
| Zeitkomplexität | O(V³) |
| Raumkomplexität | O(V²) |
| Verarbeitet negative Gewichte? | Ja (aber keine negativen Zyklen) |
| Ansatz | Dynamische Programmierung |
**Wiederholung:** dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]) für jeden Zwischenscheitelpunkt k.
### Leitfaden zur Algorithmusauswahl
| Szenario | Algorithmus |
|----------|-----------|
| Einzelne Quelle, nicht negative Gewichte | Dijkstra |
| Einzelquelle, negative Gewichte möglich | Bellman-Ford |
| Alle Paare, dichter Graph | Floyd-Warshall |
| Alle Paare, spärlicher Graph | Führen Sie Dijkstra von jedem Scheitelpunkt aus | aus
| Ungewichtetes Diagramm | BFS |
| DAG (keine Zyklen) | Topologische Sortierung + Entspannung |
| A* (heuristisch gesteuert) | A*-Suche (zur Pfadfindung mit guter Heuristik) |
---

## Minimale Spannbäume
Ein **Minimum Spanning Tree (MST)** verbindet alle Eckpunkte mit minimalem Gesamtkantengewicht.
### Eigenschaften
- Ein MST hat genau n − 1 Kanten (für n Ecken)
- Ein MST existiert genau dann, wenn der Graph verbunden ist
- Ein Graph mit unterschiedlichen Kantengewichten hat einen eindeutigen MST
- MST erfüllt die **Schnitteigenschaft**: Die Kante mit minimalem Gewicht, die jeden Schnitt kreuzt, gehört zum MST
- MST erfüllt die **Zykluseigenschaft**: Die Kante mit dem maximalen Gewicht in einem Zyklus gehört nicht zum MST
### Kruskals Algorithmus
| Eigentum | Wert |
|----------|-------|
| Strategie | Gierig – Kanten in Gewichtsreihenfolge hinzufügen |
| Datenstruktur | Disjunkte Menge (Vereinigungsfindung) |
| Zeitkomplexität | O(E log E) |
| Am besten für | Spärliche Diagramme |
**Algorithmus:**
1. Sortieren Sie alle Kanten nach Gewicht.
2. Für jede Kante (in der Reihenfolge): Wenn durch das Hinzufügen kein Zyklus erstellt wird (überprüfen Sie dies mit Union-Find), fügen Sie ihn dem MST hinzu.
3. Stoppen Sie, wenn n − 1 Kanten ausgewählt sind.
### Prims Algorithmus
| Eigentum | Wert |
|----------|-------|
| Strategie | Gierig – Baum von einem Startscheitelpunkt aus wachsen lassen |
| Datenstruktur | Prioritätswarteschlange (Min-Heap) |
| Zeitkomplexität | O(E log V) mit binärem Heap |
| Am besten für | Dichte Diagramme |
**Algorithmus:**
1. Beginnen Sie an einem beliebigen Scheitelpunkt. Markieren Sie es als Teil des MST.
2. Fügen Sie wiederholt die Kante mit minimalem Gewicht hinzu, die einen Scheitelpunkt im MST mit einem Scheitelpunkt außerhalb davon verbindet.
3. Stoppen Sie, wenn alle Scheitelpunkte enthalten sind.
### MST-Anwendungen
| Bewerbung | Wie MST hilft |
|-------------|---------------|
| Netzwerkdesign | Verlegen Sie die Mindestmenge an Kabeln/Rohren, um alle Standorte zu verbinden |
| Clustering | Entfernen Sie die k − 1 längsten MST-Kanten, um k Cluster | zu erhalten
| Approximationsalgorithmen | 2-Näherung für metrisches TSP |
| Bildsegmentierung | Pixel nach MST der Farbähnlichkeit gruppieren |
| Eliminierung von Merkmalen | Entfernen Sie redundante Features mit MST des Korrelationsdiagramms |
---

## Netzwerkfluss
Netzwerkflussprobleme modellieren die Bewegung von Ressourcen durch ein System.
### Flussnetzwerkdefinition
Ein **Flussnetzwerk** ist ein gerichteter Graph mit:
- Ein **Quellen**-Scheitelpunkt s (erzeugt Fluss)
- Ein **Senken**-Scheitelpunkt t (verbraucht Fluss)
- **Kapazitäten** c(u,v) ≥ 0 an jeder Kante
- **Fluss** f(u,v) erfüllt:
  - **Kapazitätsbeschränkung:** 0 ≤ f(u,v) ≤ c(u,v)
  - **Flusserhaltung:** Einströmen = Ausströmen an jedem Scheitelpunkt außer s und t
### Problem mit maximalem Durchfluss
Finden Sie den maximalen Gesamtfluss von s nach t.
**Ford-Fulkerson-Methode:**
1. Während es im Restgraphen einen Erweiterungspfad von s nach t gibt:
2. Finden Sie die Engpasskapazität entlang des Pfades
3. Erhöhen Sie den Fluss entlang des Pfads um den Engpassbetrag
4. Restkapazitäten aktualisieren
| Algorithmus | Zeitkomplexität | Notizen |
|-----------|----------------|-------|
| Ford-Fulkerson (DFS) | O(m · f*) wobei f* der maximale Durchfluss | ist Darf nicht mit irrationalen Fähigkeiten enden |
| Edmonds-Karp (BFS) | O(V · E²) | Wird immer beendet und wählt den kürzesten Erweiterungspfad |
| Dinics Algorithmus | O(V² · E) | Verwendet blockierende Flüsse; O(V^(1/2) · E) für Einheitskapazitäten |
### Max-Flow-Min-Cut-Theorem
Der **maximale Durchfluss** von s nach t entspricht der **minimalen Schnittkapazität**, die s von t trennt.
Ein **Schnitt** (S, T) unterteilt Eckpunkte in S (enthält s) und T (enthält t). Die Schnittkapazität ist die Summe der Kapazitäten der Kanten von S bis T.
**Anwendungen mit maximalem Durchfluss:**
- Bipartite Matching (Arbeiter den Jobs zuweisen)
- Bildsegmentierung (Vorder- und Hintergrund trennen)
- Baseball-Ausscheidung (Kann Team X noch gewinnen?)
- Netzwerkzuverlässigkeit (maximaler Datendurchsatz)
### Bipartite Matching über Max Flow
Gegeben sei ein bipartiter Graph G = (L ∪ R, E):
1. Fügen Sie Quell-s mit Kanten zu allen Eckpunkten in L hinzu (Kapazität 1).
2. Senke t mit Kanten von allen Eckpunkten in R hinzufügen (Kapazität 1)
3. Setzen Sie alle ursprünglichen Kantenkapazitäten auf 1
4. Maximaler Durchfluss = maximale Übereinstimmung
---

## Spektralgraphentheorie
Die Spektralgraphentheorie untersucht Graphen anhand der Eigenwerte und Eigenvektoren der mit dem Graphen verbundenen Matrizen.
### Schlüsselmatrizen
| Matrix | Definition | Was es erfasst |
|--------|------------|------------------|
| **Adjazenzmatrix** A | A[i][j] = 1, wenn Kante (i,j) existiert | Konnektivitätsmuster |
| **Gradmatrix** D | Diagonale; D[i][i] = deg(i) | Scheitelpunktbedeutung nach Grad |
| **Laplace-Operator** L = D − A | L[i][j] = −1 wenn Kante, Grad(i) auf Diagonale | Glätte von Funktionen im Diagramm |
| **Normalisierter Laplace-Operator** L_norm = D^(−1/2) L D^(−1/2) | Skaleninvariante Version | Gemeinschaftsstruktur |
### Eigenwerte des Laplace-Operators
Der Laplace-Operator L ist positiv semidefinit, daher sind alle Eigenwerte ≥ 0.
| Eigenwert | Bedeutung |
|------------|---------|
| λ₁ = 0 | Immer Null; Eigenvektor ist der konstante Vektor |
| λ₂ (algebraische Konnektivität) | > 0, wenn der Graph zusammenhängend ist; größer = besser verbunden |
| Anzahl der Null-Eigenwerte | Entspricht der Anzahl verbundener Komponenten |
| λₙ | Bezogen auf Maximalgrad und Graphenausdehnung |
### Anwendungen spektraler Methoden
| Bewerbung | Methode |
|-------------|--------|
| **Grafikpartitionierung** | Verwenden Sie Eigenvektoren von L, um den Graphen in ausgeglichene Teile aufzuteilen |
| **Community-Erkennung** | Spektrales Clustering: Eckpunkte mithilfe der unteren Eigenvektoren einbetten, dann Cluster |
| **PageRank** | Eigenvektor der Adjazenzmatrix (oder Übergangsmatrix) des Webgraphen |
| **Grafikzeichnung** | Positionieren Sie Eckpunkte mithilfe von Eigenvektoren des Laplace-Operators |
| **Halbüberwachtes Lernen** | Verteilen Sie Beschriftungen mithilfe des Laplace-Graphs (Label-Weitergabe) |
| **Graphische neuronale Netze** | Spektrale Faltungen: Filtern Sie Signale in Diagrammen mithilfe von Eigenvektoren von L |
### Cheegers Ungleichung
Setzt den zweiten Eigenwert λ₂ mit der **Erweiterung** des Graphen in Beziehung (wie gut er verbunden ist):
λ₂ / 2 ≤ h(G) ≤ √(2λ₂)
wobei h(G) die Cheeger-Konstante (isoperimetrische Zahl) ist. Das bedeutet, dass λ₂ ungefähr misst, wie schwer es ist, den Graphen in zwei Teile zu zerlegen – eine wichtige Erkenntnis für die Clusterbildung.
---

## Spezielle Graphstrukturen
| Diagramm | Eckpunkte | Kanten | Eigenschaften |
|-------|----------|-------|------------|
| Komplette Kₙ | n | n(n−1)/2 | Jedes Paar verbunden; Durchmesser 1 |
| Zyklus Cₙ | n | n | 2-normal; verbunden |
| Pfad Pₙ | n | n−1 | Baum; Durchmesser n−1 |
| Hypercube Qₖ | 2ᵏ | k·2ᵏ⁻¹ | k-regulär; Durchmesser k; zweiteilig |
| Vollständiges zweiteiliges K_{m,n} | m+n | m·n | Jeder Scheitelpunkt in einem Teil verbindet sich mit allen in einem anderen |
| Petersen-Grafik | 10 | 15 | 3-normal; Durchmesser 2; nicht planar; kein Hamilton-Zyklus |
---

## Relevanz für maschinelles Lernen und Datenwissenschaft
| Diagrammkonzept | Bewerbung |
|---------------|-------------|
| BFS / DFS | Web-Crawling, Analyse sozialer Netzwerke, Kennzeichnung verbundener Komponenten |
| Dijkstra / A* | Routenplanung, Spiel-KI-Pfadfindung, Robotik-Navigation |
| Minimaler Spannbaum | Clustering (Single-Linkage), Funktionsauswahl, Netzwerkdesign |
| Max. Durchfluss / Min. Schnitt | Bildsegmentierung, zweiteiliges Matching, Empfehlungszuweisung |
| Spektrale Methoden | Spektrales Clustering, graphische neuronale Netze, Dimensionsreduktion (Laplace-Eigenkarten) |
| PageRank | Suchmaschinenranking, Einflussanalyse in sozialen Netzwerken |
| DAGs | Bayesianische Netzwerke, kausale Schlussfolgerung, Aufgabenplanung, Berechnungsgraphen im Deep Learning |
| Bipartite Graphen | Benutzer-Item-Matrizen in Empfehlungssystemen, zweiseitige Märkte |
| Baumstrukturen | Entscheidungsbäume, zufällige Wälder, hierarchisches Clustering, Dateisystemnavigation |
| Diagrammdarstellungen | Wissensgraphen (Wikidata, DBpedia), molekulare Graphen (Arzneimittelentdeckung), Zitiernetzwerke |
---

## Zusammenfassung
| Thema | Kernidee | Schlüsselalgorithmus / Ergebnis |
|-------|-----------|--------|
| Grundlagen | Eckpunkte, Kanten, Grade, Pfade | Handshake-Lemma |
| Darstellungen | So speichern Sie Diagramme | Adjazenzmatrix vs. Adjazenzliste |
| Bäume | Verbundene azyklische Graphen | n Eckpunkte → n−1 Kanten |
| Durchquerungen | Systematische Scheitelpunkterkundung | BFS (kürzester Weg), DFS (tiefe Erkundung) |
| Kürzeste Wege | Routen mit minimalem Gewicht | Dijkstra, Bellman-Ford, Floyd-Warshall |
| Minimaler Spanning Tree | Günstigste Möglichkeit, alle Eckpunkte zu verbinden | Kruskals, Prims |
| Netzwerkfluss | Maximaler Durchsatz | Ford-Fulkerson, Max-Flow-Min-Cut-Theorem |
| Spektraltheorie | Eigenwerte offenbaren Struktur | Laplace-Eigenwerte, spektrale Clusterbildung |
Die Graphentheorie ist wohl der Zweig der Mathematik, der am direktesten auf die moderne Datenwissenschaft anwendbar ist. Soziale Netzwerke, Wissensgraphen, molekulare Strukturen, Berechnungsgraphen in Deep-Learning-Frameworks, Abhängigkeitsauflösung, Empfehlungssysteme – alles sind grundsätzlich Graphprobleme. Die hier behandelten Algorithmen sind nicht nur theoretisch; Sie laufen jeden Tag im großen Maßstab in Produktionssystemen.