---
# Metadata
title: "Recommendation Systems"
description: "Collaborative filtering, content-based, hybrid, matrix factorisation"
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
tags: [recommendation, systems, ai-and-machine-learning]
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
# Empfehlungssysteme
Empfehlungssysteme sagen voraus, was ein Benutzer als nächstes sehen, kaufen oder womit interagieren möchte. Sie versorgen die Content-Feeds in sozialen Medien, Produktvorschläge auf E-Commerce-Websites, Filmauswahlen auf Streaming-Plattformen und Suchergebnisse. Obwohl sie für die meisten Nutzer unsichtbar sind, gehören sie zu den kommerziell einflussreichsten KI-Systemen der Welt – Netflix schätzt, dass seine Empfehlungsmaschine durch die Reduzierung der Abonnentenabwanderung über 1 Milliarde US-Dollar pro Jahr einspart.
---

## Warum Empfehlungen schwierig sind
| Herausforderung | Beschreibung |
|-----------|-------------|
| **Maßstab** | Millionen Benutzer × Millionen Elemente = Milliarden möglicher Paare |
| **Sparsamkeit** | Jeder Benutzer hat mit einem winzigen Bruchteil der verfügbaren Elemente interagiert |
| **Kaltstart** | Neue Benutzer und neue Elemente haben keinen Interaktionsverlauf |
| **Dynamische Präferenzen** | Der Geschmack der Nutzer ändert sich mit der Zeit |
| **Jenseits der Genauigkeit** | Empfehlungen müssen außerdem vielfältig, neuartig und zufällig sein |
| **Geschäftsziele** | Maximierung des Engagements ≠ Maximierung des Wohlbefindens der Benutzer |
---

## Kernansätze
### Kollaboratives Filtern
Die Idee: Wenn Benutzer A und B in der Vergangenheit zugestimmt haben, werden sie wahrscheinlich auch in Zukunft zustimmen.
| Geben Sie | ein Wie es funktioniert | Beispiel |
|------|-------------|---------|
| **Benutzerbasiert** | Finden Sie ähnliche Benutzer; empfehlen, was ihnen gefallen hat | „Benutzer, denen das gefallen hat, mochten auch …“ |
| **Artikelbasiert** | Finden Sie ähnliche Artikel, die dem Benutzer bereits gefallen | „Weil du zugesehen hast...“ |
| **Matrixfaktorisierung** | Zerlegen Sie die Benutzer-Element-Interaktionsmatrix in latente Faktoren | SVD, ALS (Alternating Least Squares) |
| Stärke | Schwäche |
|----------|----------|
| Es ist nicht erforderlich, die Elemente selbst zu verstehen | Kaltstartproblem: Neue Artikel können nicht empfohlen werden |
| Erfasst komplexe, implizite Präferenzen | Erfordert viele Interaktionsdaten |
| Funktioniert für jeden Inhaltstyp | Beliebtheitsbias: empfiehlt bereits beliebte Artikel |
### Inhaltsbasierte Filterung
Empfehlen Sie Artikel, die denen ähneln, die dem Benutzer bereits gefallen, basierend auf den Artikelmerkmalen.
| Feature-Typ | Beispiel |
|-------------|---------|
| **Text** | Genre, Beschreibung, Schlüsselwörter, Besetzung |
| **Audio** | Tempo, Genre, Stimmung (für Musik) |
| **Visuell** | Farbpalette, Stil (für Bilder/Mode) |
| **Metadaten** | Preis, Marke, Kategorie |
| Stärke | Schwäche |
|----------|----------|
| Kein Kaltstart für Artikel (Features sind bekannt) | Es können keine Artikel empfohlen werden, die nicht dem aktuellen Geschmack des Benutzers entsprechen |
| Funktioniert mit weniger Interaktionsdaten | Erfordert gutes Feature-Engineering |
| Erklärbar („empfohlen, weil es X ähnlich ist“) | Weniger Zufall |
### Hybride Ansätze
Die meisten Produktionssysteme kombinieren kollaborative und inhaltsbasierte Methoden.
| Hybridstrategie | Beschreibung |
|----------------|-------------|
| **Gewichtet** | Ergebnisse mehrerer Modelle kombinieren |
| **Umschalten** | Nutzen Sie inhaltsbasiert für neue Benutzer, kollaborativ für etablierte Benutzer |
| **Kaskade** | Verwenden Sie zuerst ein einfaches Modell und verfeinern Sie es dann mit einem komplexen |
| **Funktionskombination** | Kollaborations- und Inhaltsfunktionen in einem einzigen Modell zusammenführen |
| **Meta-Lernen** | Erfahren Sie, wie Sie verschiedene Empfehlungsgeber kombinieren |
---

## Moderne Deep-Learning-Ansätze
### Zwei-Tower-Modelle
Die vorherrschende Architektur für groß angelegte Empfehlungen (verwendet von YouTube, Pinterest, Spotify).
| Komponente | Rolle |
|-----------|------|
| **Benutzerturm** | Neuronales Netzwerk, das Benutzerfunktionen und -verlauf in ein eingebettetes | kodiert
| **Gegenstandsturm** | Neuronales Netzwerk, das Artikelmerkmale in eine Einbettung kodiert |
| **Ähnlichkeit** | Skalarprodukt- oder Kosinusähnlichkeit zwischen Benutzer- und Artikeleinbettungen |
| Schritt | Beschreibung |
|------|-------------|
| 1 | Trainieren Sie beide Türme, um ähnliche Einbettungen für interagierende Benutzer-Element-Paare zu erzeugen |
| 2 | Berechnen Sie zum Bereitstellungszeitpunkt die Artikeleinbettungen vorab |
| 3 | Berechnen Sie für eine Benutzeranfrage die Benutzereinbettung |
| 4 | Verwenden Sie die ANN-Suche (Approximation Next Neighbor), um die ähnlichsten Elemente zu finden |
### Sequenzmodelle für Empfehlungen
Das Nutzerverhalten ist sequentiell – was Sie gestern gesehen haben, beeinflusst, was Sie heute sehen werden.
| Modell | Ansatz |
|-------|----------|
| **GRU4Rec** | GRU-basiertes Modell für sitzungsbasierte Empfehlungen |
| **SASRec** | Auf Selbstaufmerksamkeit basierender sequenzieller Empfehlungsgeber |
| **BERT4Rec** | Bidirektionaler Transformator für sequentielle Empfehlungen |
| **YouTube DNN** | Tiefes neuronales Netzwerk, das den Uhrenverlauf als Sequenz behandelt |
### Retrieval vs. Ranking
Moderne Systeme unterteilen Empfehlungen in zwei Phasen:
| Bühne | Zweck | Methode |
|-------|---------|--------|
| **Abruf (Kandidatengenerierung)** | Millionen von Artikeln auf ca. 1.000 Kandidaten eingrenzen | Zwei-Turm-Modell; ANN-Suche; schnell, aber ungefähr |
| **Rangliste (Wertung)** | Präzise Bewertung und Reihenfolge der Kandidaten | Tiefes Modell mit vielen Funktionen; langsamer, aber genau |
| **Neue Rangfolge** | Anpassung an Vielfalt, Geschäftsregeln und Frische | Kontextuelle Banditen; Einschränkungsoptimierung |
---

## Bewertungsmetriken
| Metrisch | Was es misst | Wann zu verwenden |
|--------|---|-------------|
| **Präzision@K** | Anteil relevanter Top-K-Empfehlungen | Wenn Ihnen die Genauigkeit der Top-Tipps am Herzen liegt |
| **Recall@K** | Anteil relevanter Elemente, die in Top-K | gefunden wurden Wenn es Ihnen wichtig ist, keine guten Artikel zu verpassen |
| **NDCG** (Normalisierter diskontierter kumulativer Gewinn) | Ranking-Qualität; Belohnungen, die relevante Artikel höher setzen | Wenn die Rangfolge wichtig ist |
| **MAP** (mittlere durchschnittliche Präzision) | Durchschnittliche Präzision aller Benutzer | Qualität des Gesamtrankings |
| **Trefferquote@K** | Ob mindestens ein relevantes Element in Top-K | erscheint Binäre Relevanzszenarien |
| **Abdeckung** | Anteil der Artikel, die empfohlen werden | Vielfalt und Fairness |
| **Zufall** | Unerwartete, aber relevante Empfehlungen | Benutzerzufriedenheit |
---

## Das Kaltstartproblem
| Szenario | Herausforderung | Lösungen |
|----------|-----------|-----------|
| **Neuer Benutzer** | Kein Interaktionsverlauf | Nutzen Sie demografische Daten; beliebte Artikel anzeigen; Kontextsignale verwenden (Standort, Gerät, Zeit) |
| **Neuer Artikel** | Bisher hat noch niemand damit interagiert | Inhaltsfunktionen nutzen; Exploration-Exploit-Strategien; Bandit-Algorithmen |
| **Neues System** | Überhaupt keine Daten | Lernen aus ähnlichen Bereichen übertragen; Erstinhalte kuratieren |
---

## Erkundung vs. Ausbeutung
| Strategie | Beschreibung | Kompromiss |
|----------|-------------|-----------|
| **ε-gierig** | Zufällige Elemente mit Wahrscheinlichkeit ε | anzeigen Einfach, aber ineffizient |
| **Thompson-Probenahme** | Stichprobe aus der hinteren Verteilung der Artikelqualität | Prinzipiell; gute theoretische Eigenschaften |
| **Obere Vertrauensgrenze (UCB)** | Bevorzugen Sie Elemente mit hoher Unsicherheit | Gutes Gleichgewicht zwischen Exploration und Ausbeutung |
| **Kontextuelle Banditen** | Vom Benutzerkontext abhängige Erkundung | Effizienter als blinde Erkundung |
| **Diversity-Injektion** | Bewusst verschiedene oder neuartige Elemente einbeziehen | Einfach; kann kurzfristiges Engagement reduzieren |
---

## Voreingenommenheit und Fairness
| Bias-Typ | Beschreibung | Auswirkungen |
|-----------|-------------|--------|
| **Beliebtheitsbias** | Beliebte Artikel werden häufiger empfohlen und werden immer beliebter | Long-Tail-Artikel sind unterversorgt |
| **Auswahlverzerrung** | Modelle lernen aus beobachteten Interaktionen, nicht aus allen möglichen | Auf aktive Benutzer ausgerichtet |
| **Positionsbias** | Artikel, die an höheren Positionen angezeigt werden, erhalten unabhängig von ihrer Qualität mehr Klicks | Stärkt Spitzenpositionen |
| **Belichtungsfehler** | Angezeigte Elemente erhalten mehr Trainingssignal | Rückkopplungsschleife |
| **Demografischer Bias** | Empfehlungen unterscheiden sich je nach Bevölkerungsgruppe auf unfaire Weise | Diskriminierung; schlechte Erfahrung für einige Gruppen |
### Minderungsstrategien
| Strategie | Beschreibung |
|----------|-------------|
| **Inverse Propensity-Gewichtung** | Beliebte Trainingsgegenstände abgewichten |
| **Debiasing-Schichten** | Fügen Sie dem Modell eine Debiasing-Komponente hinzu |
| **Fairnessbeschränkungen** | Fügen Sie Einschränkungen hinzu, um eine Gleichbehandlung sicherzustellen |
| **Diverse Empfehlungen** | Explizit auf Diversität und Relevanz optimieren |
| **Prüfung und Überwachung** | Überprüfen Sie die Empfehlungen regelmäßig auf gruppenübergreifende Voreingenommenheit |
---

## Branchenbeispiele
| Unternehmen | System | Ansatz |
|---------|--------|----------|
| **Netflix** | Film-/TV-Empfehlungen | Zwei-Turm-Abruf + tiefes Ranking + kontextbezogene Banditen für Kunstwerke |
| **YouTube** | Videoempfehlungen | Tiefes neuronales Netzwerk zur Kandidatengenerierung; separates Ranking-Modell |
| **Spotify** | Musikempfehlungen | Kollaboratives Filtern + NLP auf Playlists + Audioanalyse |
| **Amazon** | Produktempfehlungen | Kollaborative Filterung von Artikel zu Artikel; personalisiert im Maßstab |
| **TikTok** | Kurzer Video-Feed | Verstärkungslernen; starker Schwerpunkt auf Erkundung |
| **Pinterest** | Visuelle Empfehlungen | Zwei-Turm-Modell; visuelle Ähnlichkeit |
---

## Tools und Frameworks
| Werkzeug | Zweck |
|------|---------|
| **TensorFlow-Empfehler (TFRS)** | Zwei-Turm-Modelle, Retrieval, Ranking |
| **PyTorch RecSys** | Forschungsorientierte Empfehlungsmodelle |
| **Überraschung** | Klassische kollaborative Filterung (SVD, NMF, KNN) |
| **Implizit** | Schnelle kollaborative Filterung für implizites Feedback (ALS, BPR) |
| **Faiss** (Meta) | Ungefähre Suche nach nächsten Nachbarn im Maßstab |
| **Milvus / Tannenzapfen / Weaviate** | Vektordatenbanken zur Ähnlichkeitssuche |
| **Recbole** | Umfassende Empfehlungsrecherchebibliothek |
| **Merlin** (NVIDIA) | GPU-beschleunigte Empfehlungspipeline |
---

## Zusammenfassung
Empfehlungssysteme gehören zu den wirkungsvollsten KI-Anwendungen in der Industrie. Der Bereich hat sich von einfacher kollaborativer Filterung zu Deep-Learning-Architekturen entwickelt, die Benutzerhistorie, Artikelinhalte, kontextbezogene Signale und Geschäftsziele kombinieren. Moderne Systeme nutzen eine Retrieval-Ranking-Re-Ranking-Pipeline mit Zwei-Turm-Modellen für eine schnelle Kandidatengenerierung und tiefen Modellen für eine präzise Bewertung. Die Herausforderungen – Kaltstart, Voreingenommenheit, Erkundung und das Ausbalancieren der Benutzerzufriedenheit mit den Geschäftszielen – bleiben aktive Bereiche der Forschung und Technik.