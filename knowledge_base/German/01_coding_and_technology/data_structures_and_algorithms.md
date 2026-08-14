<!--
---
# Metadata
title: "Data Structures and Algorithms"
description: "Arrays, trees, graphs, sorting, searching, complexity"
category: "Coding and Technology"
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
reviewed_by: "Coding & Technology Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [data, structures, algorithms, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "6 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Datenstrukturen und Algorithmen
Datenstrukturen sind die Art und Weise, wie wir Daten im Speicher organisieren, damit Operationen darauf effizient sind. Algorithmen sind die schrittweisen Vorgehensweisen zur Lösung von Problemen. Zusammen bilden sie die Grundlage der Informatik – jedes Programm, das Sie jemals verwendet haben, basiert auf ihnen. Die Wahl der richtigen Datenstruktur kann ein unglaublich langsames Programm in ein schnelles verwandeln, und die Kenntnis des richtigen Algorithmus kann ein unlösbares Problem in ein triviales Problem verwandeln.
---

## Grundlegende Datenstrukturen
### Lineare Strukturen
| Struktur | Zugriff | Suche | Einfügen | Löschen | Anwendungsfall |
|-----------|--------|--------|--------|--------|----------|
| **Array** | O(1) nach Index | O(n) | O(n) | O(n) | Sammlungen mit fester Größe; Direktzugriff |
| **Verknüpfte Liste** | O(n) | O(n) | O(1) an der Spitze | O(1) an der Spitze | Dynamische Größe; Einfügungen/Löschungen |
| **Stapel** | O(n) | O(n) | O(1) Push/Pop | O(1) Pop | Funktionsaufrufe; rückgängig machen; Parsen |
| **Warteschlange** | O(n) | O(n) | O(1) in die Warteschlange stellen | O(1) aus der Warteschlange entfernen | Aufgabenplanung; BFS; Nachrichtenwarteschlangen |
| **Deque** | O(1) an beiden Enden | O(n) | O(1) an beiden Enden | O(1) an beiden Enden | Schiebefenster; Arbeitsdiebstahl |
### Hash-basierte Strukturen
| Struktur | Suche | Einfügen | Löschen | Anwendungsfall |
|-----------|--------|--------|--------|----------|
| **Hash-Tabelle** | O(1) Durchschnitt | O(1) Durchschnitt | O(1) Durchschnitt | Schlüsselwertsuche; Caches; setzt |
| **Hash-Set** | O(1) | O(1) | O(1) | Mitgliedschaftsprüfung; Deduplizierung |
**Hash-Kollisionen**: Wenn zwei Schlüssel an denselben Slot gesendet werden, werden sie in einer verknüpften Liste (Verkettung) oder im nächsten verfügbaren Slot (offene Adressierung) gespeichert. Gute Hash-Funktionen minimieren Kollisionen.
### Baumstrukturen
| Struktur | Suche | Einfügen | Löschen | Anwendungsfall |
|-----------|--------|--------|--------|----------|
| **Binärer Suchbaum** | O(log n) Durchschnitt | O(log n) | O(log n) | Sortierte Daten; Bereichsabfragen |
| **AVL / Rot-Schwarzer Baum** | O(log n) garantiert | O(log n) | O(log n) | Selbstausgleichend; wird in Karten/Sets verwendet |
| **B-Baum / B+ Baum** | O(log n) | O(log n) | O(log n) | Datenbankindizes; Dateisysteme |
| **Versuchen** | O(k) wobei k = Schlüssellänge | O(k) | O(k) | Automatische Vervollständigung; Präfixübereinstimmung |
| **Heap (binär)** | O(n) | O(log n) | O(log n) | Prioritätswarteschlangen; Terminplanung |
### Diagrammdarstellungen
| Darstellung | Raum | Kantensuche | Kante hinzufügen | Nachbarn iterieren |
|---------------|-------|-------------|----------|-----|
| **Adjazenzmatrix** | O(V²) | O(1) | O(1) | O(V) |
| **Adjazenzliste** | O(V + E) | O(Grad) | O(1) | O(Grad) |
| **Kantenliste** | O(E) | O(E) | O(1) | O(E) |
---

## Algorithmuskomplexität (Big-O)
Die Big-O-Notation beschreibt, wie der Zeit- oder Platzbedarf eines Algorithmus mit zunehmender Eingabegröße wächst.
| Komplexität | Name | Beispiel |
|-----------|------|---------|
| **O(1)** | Konstante | Hash-Tabellensuche; Array-Zugriff über Index |
| **O(log n)** | Logarithmisch | Binäre Suche; ausgewogene Baumoperationen |
| **O(n)** | Linear | Lineare Suche; Iterieren eines Arrays |
| **O(n log n)** | Linearithmisch | Sortierung zusammenführen; Heap-Sortierung; effizienteste Allzwecksortierungen |
| **O(n²)** | Quadratisch | Blasensortierung; verschachtelte Schleifen über dieselben Daten |
| **O(2^n)** | Exponentiell | Brute-Force-Teilmengengenerierung; naives rekursives Fibonacci |
| **O(n!)** | Fakultät | Handlungsreisender (brutale Gewalt); Permutationen |
### Häufige Missverständnisse
| Missverständnis | Realität |
|--------------|---------|
| „O(n) ist immer schneller als O(n²)“ | Für kleine n ist der konstante Faktor wichtiger |
| „Lower Big-O ist immer besser“ | Es gibt Raum-Zeit-Kompromisse; O(1)-Suche verwendet O(n)-Speicher |
| „Big-O sagt Ihnen die genaue Geschwindigkeit“ | Es beschreibt die Wachstumsrate, nicht die absolute Zeit |
---

## Sortieralgorithmen
| Algorithmus | Am besten | Durchschnittlich | Am schlimmsten | Raum | Stabil | Vor Ort |
|-----------|------|---------|-------|-------|--------|----------|
| **Blasensortierung** | O(n) | O(n²) | O(n²) | O(1) | Ja | Ja |
| **Einfügesortierung** | O(n) | O(n²) | O(n²) | O(1) | Ja | Ja |
| **Auswahl sortieren** | O(n²) | O(n²) | O(n²) | O(1) | Nein | Ja |
| **Sortierung zusammenführen** | O(n log n) | O(n log n) | O(n log n) | O(n) | Ja | Nein |
| **Schnellsortierung** | O(n log n) | O(n log n) | O(n²) | O(log n) | Nein | Ja |
| **Heap-Sortierung** | O(n log n) | O(n log n) | O(n log n) | O(1) | Nein | Ja |
| **Tim Sort** | O(n) | O(n log n) | O(n log n) | O(n) | Ja | Nein |
**Praktischer Rat**: Verwenden Sie die integrierte Sortierung Ihrer Sprache (Pythons`sorted()`, JavaScripts`Array.sort()`). Sie verwenden hochoptimierte Algorithmen (Tim Sort, Introsort), die alle Randfälle verarbeiten.
---

## Suchalgorithmen
| Algorithmus | Datenstruktur | Komplexität | Anforderung |
|-----------|---------------|-----------|-------------|
| **Lineare Suche** | Irgendein | O(n) | Keine |
| **Binäre Suche** | Sortiertes Array | O(log n) | Daten müssen sortiert werden |
| **Hash-Tabellensuche** | Hash-Tabelle | O(1) Durchschnitt | Gute Hash-Funktion |
| **BFS** (Breite-First-Suche) | Diagramm / Baum | O(V + E) | Ungewichteter kürzester Weg |
| **DFS** (Tiefensuche) | Diagramm / Baum | O(V + E) | Wegfindung; Zykluserkennung |
| **Dijkstras** | Gewichtetes Diagramm | O((V + E) log V) | Nicht negative Gewichte; kürzester Weg |
| **A* Suche** | Gewichtetes Diagramm | O((V + E) log V) | Heuristisch geführt; optimal mit zulässiger Heuristik |
---

## Schlüsselalgorithmusmuster
| Muster | Beschreibung | Beispielprobleme |
|---------|-------------|-----------------|
| **Teile und herrsche** | Problem in Teilprobleme aufteilen; rekursiv lösen; kombinieren | Sortierung zusammenführen; Quicksort; binäre Suche |
| **Dynamische Programmierung** | In überlappende Teilprobleme aufteilen; Cache-Ergebnisse | Fibonacci; Tornister; längste gemeinsame Teilfolge |
| **Gierig** | Treffen Sie bei jedem Schritt die lokal optimale Wahl | Dijkstras; Huffman-Codierung; Aktivitätsauswahl |
| **Zurückverfolgen** | Probieren Sie Möglichkeiten aus; schlechte Entscheidungen rückgängig machen; Alternativen ausprobieren | Sudoku-Löser; N-Königinnen; Permutationen |
| **Schiebefenster** | Behalten Sie ein Fenster mit Elementen bei; Schieben Sie es über die Daten | Maximales Summen-Subarray der Größe K; längster Teilstring ohne Wiederholungen |
| **Zwei Hinweise** | Verwenden Sie zwei Zeiger, die sich aufeinander zu oder in die gleiche Richtung bewegen | Paarsumme in sortiertem Array; Duplikate entfernen |
| **Binäre Suche nach Antwort** | Binäre Suche im Antwortraum | Mindestseiten zuweisen; aggressive Kühe |
---

## Wann was zu verwenden ist
| Problem | Datenstruktur | Algorithmus |
|---------|---------------|-----------|
| Schnelle Schlüsselwertsuche | Hash-Tabelle / Wörterbuch | Hashing |
| Sortierte Reihenfolge beibehalten | Ausgeglichenes BST (TreeMap, std::set) | Baumoperationen |
| Prioritätsbasierte Verarbeitung | Heap/Prioritätswarteschlange | Heap-Operationen |
| Kürzester Weg (ungewichtet) | Diagramm (Adjazenzliste) | BFS |
| Kürzester Weg (gewichtet) | Diagramm (Adjazenzliste) | Dijkstras / A* |
| Mitgliedschaftstest | Hash-Set / Bloom-Filter | Hashing |
| Präfixübereinstimmung | Versuchen | Trie-Durchquerung |
| Bereichsabfragen | Segmentbaum / Fenwick-Baum | Baumoperationen |
| LRU-Cache | Hash-Map + doppelt verknüpfte Liste | Kombinierte Operationen |
| Verbundene Komponenten | Disjunkte Mengenvereinigung (Union-Find) | Vereinigung und Suche |
---

## Zusammenfassung
Datenstrukturen und Algorithmen sind nicht nur Interviewthemen – sie sind die Bausteine ​​effizienter Software. Arrays und Hash-Tabellen erfüllen die meisten alltäglichen Anforderungen. Bäume und Diagramme verarbeiten hierarchische und relationale Daten. Sortieren und Suchen sind gelöste Probleme in Standardbibliotheken. Die algorithmischen Muster – Teilen und Herrschen, dynamische Programmierung, Gier, Backtracking – sind wiederverwendbare Strategien zur Bewältigung neuer Probleme. Die Schlüsselkompetenz besteht nicht darin, sich Algorithmen zu merken; Es geht darum, zu erkennen, welches Muster zu einem bestimmten Problem passt, und die richtige Datenstruktur für die Aufgabe auszuwählen.