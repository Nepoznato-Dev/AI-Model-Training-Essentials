---
# Metadata
title: "Information Theory"
description: "Shannon entropy, differential entropy, joint and mutual information, KL divergence, cross-entropy, channel capacity, source coding, compression, and connections to machine learning loss functions"
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
    changes: "Initial deep-dive into information theory"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2027-02-10"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-10"

# Classification
tags: [information-theory, entropy, kl-divergence, cross-entropy, mutual-information, channel-capacity, compression, machine-learning]
difficulty_level: "intermediate"
prerequisites:
  - "mathematics.md"
  - "statistics_and_probability.md"
estimated_reading_time: "25 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# Informationstheorie
Die 1948 von Claude Shannon begründete Informationstheorie quantifiziert Informationen selbst. Wie viel sagt Ihnen eine Nachricht? Wie stark können Sie Daten komprimieren? Wie schnell können Sie über einen verrauschten Kanal kommunizieren? Auf diese Fragen gibt es präzise mathematische Antworten. Über die Kommunikation hinaus ist die Informationstheorie zur Grundlage des maschinellen Lernens geworden – Kreuzentropie ist die Standardverlustfunktion für die Klassifizierung, KL-Divergenz misst die Verteilungsähnlichkeit und gegenseitige Informationen steuern die Merkmalsauswahl.
---

## Entropie
**Entropie** misst die durchschnittliche Unsicherheit oder „Überraschung“ einer Zufallsvariablen.
### Shannon-Entropie (diskret)
Für eine diskrete Zufallsvariable X mit Wahrscheinlichkeitsmassenfunktion p(x):
H(X) = −Σₓ p(x) log₂ p(x)
Einheiten: **Bits** (bei Verwendung von log₂) oder **Nats** (bei Verwendung von ln).
| Vertrieb | Entropie | Intuition |
|-------------|---------|-----------|
| Faire Münze (p = 0,5, 0,5) | 1 Bit | Maximale Unsicherheit für binäres Ergebnis |
| Voreingenommene Münze (p = 0,9, 0,1) | 0,469 Bit | Weniger überraschend – überwiegend Köpfe |
| Deterministisch (p = 1, 0) | 0 Bit | Überhaupt keine Unsicherheit |
| Fairer Würfel (6 Seiten) | 2,585 Bit | Mehr Ergebnisse = mehr Unsicherheit |
| Einheitlich über n Ergebnisse | log₂(n) Bits | Maximale Entropie für n Ergebnisse |
### Eigenschaften der Entropie
| Eigentum | Aussage |
|----------|-----------|
| Nicht-Negativität | H(X) ≥ 0 |
| Maximal | H(X) ≤ log₂(\|X\|) mit Gleichheit für Gleichverteilung |
| Kettenregel | H(X, Y) = H(X) + H(Y \| X) |
| Konditionierung reduziert | H(X \| Y) ≤ H(X) |
| Konkavität | H ist eine konkave Funktion der Wahrscheinlichkeitsverteilung |
### Differenzielle Entropie (kontinuierlich)
Für eine kontinuierliche Zufallsvariable X mit Dichte p(x):
h(X) = −∫ p(x) log p(x) dx
Im Gegensatz zur diskreten Entropie kann die differentielle Entropie **negativ** sein.
| Vertrieb | Differenzielle Entropie |
|-------------|-------|
| Einheitlich auf [a,b] | log(b − a) |
| Normal N(μ, σ²) | (1/2) log(2πeσ²) |
| Exponential(λ) | 1 − ln(λ) |
---

## Gemeinsame, bedingte und gegenseitige Information
### Gemeinsame Entropie
H(X, Y) = −Σₓ Σᵧ p(x, y) log p(x, y)
Misst die Gesamtunsicherheit des Paares (X, Y).
### Bedingte Entropie
H(Y | X) = −Σₓ Σᵧ p(x, y) log p(y | x) = H(X, Y) − H(X)
Misst die verbleibende Unsicherheit über Y nach der Beobachtung von X.
### Gegenseitige Information
I(X; Y) = Σₓ Σᵧ p(x, y) log [p(x, y) / (p(x)p(y))]
Misst, wie viel Ihnen die Kenntnis von X über Y verrät (und umgekehrt).
| Eigentum | Aussage |
|----------|-----------|
| Nicht-Negativität | I(X; Y) ≥ 0 |
| Symmetrie | I(X; Y) = I(Y; X) |
| Beziehung zur Entropie | I(X; Y) = H(X) − H(X \| Y) = H(Y) − H(Y \| X) |
| Beziehung zum Gelenk | I(X; Y) = H(X) + H(Y) − H(X, Y) |
| Unabhängigkeit | I(X; Y) = 0 genau dann, wenn X und Y unabhängig sind |
| Selbstauskunft | I(X; X) = H(X) |
### Visuell: Das Entropiediagramm
```
┌─────────────────────────────────────────┐
│            H(X, Y)                      │
│  ┌──────────────┐  ┌──────────────┐    │
│  │   H(X|Y)     │  │   H(Y|X)     │    │
│  │              │I │              │    │
│  │              │( │              │    │
│  │   H(X)−I    │X │   H(Y)−I    │    │
│  │              │; │              │    │
│  │              │Y │              │    │
│  └──────────────┘  └──────────────┘    │
│         H(X)              H(Y)          │
└─────────────────────────────────────────┘
```

---

## KL Divergenz
Die **Kullback-Leibler (KL)-Divergenz** misst, wie unterschiedlich eine Verteilung von einer anderen ist.
D_KL(P || Q) = Σₓ P(x) log [P(x) / Q(x)]
| Eigentum | Aussage |
|----------|-----------|
| Nicht-Negativität | D_KL(P \|\| Q) ≥ 0 (Gibbs‘ Ungleichung) |
| Identität | D_KL(P \|\| Q) = 0 genau dann, wenn P = Q |
| Asymmetrie | D_KL(P \|\| Q) ≠ D_KL(Q \|\| P) im Allgemeinen |
| Keine Metrik | Fehlt Symmetrie und Dreiecksungleichung |
**Interpretation:** D_KL(P || Q) ist die zusätzliche Anzahl von Bits, die zum Codieren von Daten aus P mit einem für Q optimierten Code erforderlich sind.
### Beziehung zu anderen Größen
| Beziehung | Formel |
|-------------|---------|
| Kreuzentropie | H(P, Q) = H(P) + D_KL(P \|\| Q) |
| Gegenseitige Information | I(X; Y) = D_KL(P(X,Y) \|\| P(X)P(Y)) |
| Bedingte KL | D_KL(P(Y\|X) \|\| Q(Y\|X)) gemittelt über X |
---

## Kreuzentropie
**Kreuzentropie** zwischen den Verteilungen P und Q:
H(P, Q) = −Σₓ P(x) log Q(x) = H(P) + D_KL(P || Q)
### Kreuzentropie als Verlustfunktion
Bei der Klassifizierung ist P die wahre Verteilung (One-Hot-codierte Bezeichnung) und Q die vorhergesagte Verteilung des Modells.
**Binäre Kreuzentropie (BCE):**
L = −[y log(ŷ) + (1−y) log(1−ŷ)]
**Kategoriale Kreuzentropie:**
L = −Σᵢ yᵢ log(ŷᵢ)
| Szenario | y (wahr) | ŷ (vorhergesagt) | Verlust |
|----------|----------|---------------|------|
| Richtig, selbstbewusst | 1 | 0,95 | 0,051 |
| Richtig, unsicher | 1 | 0,55 | 0,598 |
| Falsch, zuversichtlich | 1 | 0,05 | 2,996 |
| Falsch, unsicher | 1 | 0,45 | 0,799 |
Die Minimierung der Kreuzentropie ist gleichbedeutend mit der Minimierung der KL-Abweichung von der wahren Verteilung – weshalb sie als Verlustfunktion so gut funktioniert.
---

## Kanalkapazität
### Kommunikationskanalmodell
```
X → [Channel] → Y
```

- X: Zufallsvariable eingeben
- Y: Zufallsvariable ausgeben
- Kanal: definiert durch bedingte Wahrscheinlichkeiten p(y|x)
### Shannons Noisy Channel Coding Theorem
Für einen Kanal mit der Kapazität C und der Übertragungsrate R< C, there exists a coding scheme that achieves arbitrarily small error probability. If R >C ist eine zuverlässige Kommunikation nicht möglich.
**Kanalkapazität:**
C = max_{p(x)} I(X; Y)
### Wichtige Kanalbeispiele
| Kanal | Beschreibung | Kapazität |
|---------|-------------|----------|
| **Binär symmetrisch (BSC)** | Dreht jedes Bit mit der Wahrscheinlichkeit p | um 1 − H(p) Bits |
| **Binäre Löschung (BEC)** | Löscht jedes Bit mit der Wahrscheinlichkeit ε | 1 − ε Bits |
| **Gauß (AWGN)** | Y = X + Z, Z ~ N(0, σ²) | (1/2)log(1 + SNR) Bits |
| **Geräuschlose Binärdatei** | Perfekte Übertragung | 1 Bit |
---

## Quellkodierung und Komprimierung
### Quellkodierungssatz
Die durchschnittliche Anzahl von Bits, die zum Kodieren einer Quelle benötigt werden, wird durch ihre Entropie begrenzt:
L ≥ H(X)
Ein optimaler Code erreicht L ≈ H(X).
### Huffman-Codierung
Ein **präfixfreier** Code, der kürzere Codes wahrscheinlicheren Symbolen zuweist.
| Symbol | Wahrscheinlichkeit | Huffman-Code | Länge |
|--------|-------------|-------------|--------|
| A | 0,5 | 0 | 1 |
| B | 0,25 | 10 | 2 |
| C | 0,125 | 110 | 3 |
| D | 0,125 | 111 | 3 |
Durchschnittliche Länge: 0,5(1) + 0,25(2) + 0,125(3) + 0,125(3) = 1,75 Bits/Symbol
Entropie: H = 1,75 Bits/Symbol (in diesem Fall optimal!)
### Verlustfreie vs. verlustbehaftete Komprimierung
| Geben Sie | ein Prinzip | Beispiele | Grenze |
|------|-----------|----------|-------|
| **Verlustfrei** | Statistische Redundanz entfernen | ZIP, PNG, FLAC | Entropierate H(X) |
| **Verlustbehaftet** | Wahrnehmungsirrelevante Informationen entfernen | JPEG, MP3, H.264 | Geschwindigkeitsverzerrungsfunktion R(D) |
**Ratenverzerrungstheorie:** Für verlustbehaftete Komprimierung mit maximaler Verzerrung D beträgt die minimale Rate R(D) = min I(X; X̂) vorbehaltlich E[d(X, X̂)] ≤ D.
---

## Verbindungen zu anderen Bereichen
### Informationstheorie und Thermodynamik
| Konzept | Informationstheorie | Thermodynamik |
|---------|-------------------|----------------|
| Entropie | Shannon-Entropie H(X) | Boltzmann-Entropie S = k_B ln W |
| Maximale Entropie | Gleichmäßige Verteilung | Thermisches Gleichgewicht |
| KL-Divergenz | Verteilungsunterschied | Freie Energiedifferenz |
| Gegenseitige Information | Geteilte Informationen | Korrelationen in physikalischen Systemen |
Die mathematischen Formen sind identisch – Shannon hat den Begriff „Entropie“ bewusst aus der statistischen Mechanik übernommen.
### Informationstheorie und Statistik
| Konzept | Bewerbung |
|---------|-------------|
| Maximale Wahrscheinlichkeit | Entspricht der Minimierung der KL-Divergenz von der empirischen zur Modellverteilung |
| Fisher-Informationen | Krümmung der KL-Divergenz; Untergrenze der Schätzervarianz (Cramér-Rao) |
| Mindestbeschreibungslänge (MDL) | Modellauswahl durch Minimierung der gesamten Kodierungslänge |
| AIC / BIC | Ungefähre KL-basierte Modellauswahlkriterien |
---

## Relevanz für maschinelles Lernen und Datenwissenschaft
| IT-Konzept | ML-Anwendung |
|-----------|----------------|
| Kreuzentropieverlust | Standardklassifizierungsverlust (binär und mehrklassig) |
| KL-Divergenz | VAE-Verlust (Regularisierungsbegriff), Verteilungsanpassung, Destillation |
| Gegenseitige Information | Merkmalsauswahl (MIFS), Repräsentationslernen (InfoMax), Entflechtung |
| Entropie | Entscheidungsbaum-Aufteilungskriterium (Informationsgewinn), Erkundung in RL (maximale Entropie RL) |
| Kanalkapazität | Kommunikationskomplexität, Verallgemeinerungsgrenzen verstehen |
| Quellkodierung | Datenkomprimierung zur Speicherung und Übertragung, effiziente Kodierung |
| Maximale Entropie | MaxEnt-Klassifikatoren, vorherige Auswahl in der Bayes'schen Inferenz |
| Ratenverzerrung | Kompromisse bei verlustbehafteter Komprimierung und Quantisierung in neuronalen Netzen verstehen |
| Fisher-Informationen | Natürlicher Gradientenabstieg, Verständnis der Parameterempfindlichkeit |
| MDL / AIC / BIC | Modellauswahl, Überanpassung verhindern |
---

## Zusammenfassung
| Menge | Formel (diskret) | Bedeutung |
|----------|-----|---------|
| Entropie H(X) | −Σ p(x) log p(x) | Durchschnittliche Unsicherheit |
| Gemeinsame Entropie H(X,Y) | −Σ p(x,y) log p(x,y) | Gesamtunsicherheit des Paares |
| Bedingte Entropie H(Y\|X) | H(X,Y) − H(X) | Verbleibende Unsicherheit über Y bei gegebenem X |
| Gegenseitige Information I(X;Y) | H(X) − H(X\|Y) | Zwischen X und Y geteilte Informationen |
| KL-Divergenz D_KL(P\|\|Q) | Σ P(x) log(P(x)/Q(x)) | „Abstand“ zwischen Verteilungen |
| Kreuzentropie H(P,Q) | −Σ P(x) log Q(x) | Kodierungskosten bei falscher Verteilung |
| Kanalkapazität C | max I(X;Y) | Maximale zuverlässige Kommunikationsrate |
Die Informationstheorie liefert die grundlegenden Grenzen dessen, was gelernt, komprimiert und kommuniziert werden kann. Für Praktiker des maschinellen Lernens erklärt es, warum Kreuzentropie als Verlustfunktion funktioniert, wie man die Qualität erlernter Darstellungen misst und wie man über den Kompromiss zwischen Modellkomplexität und Datenanpassung nachdenkt. Shannons Erkenntnisse aus dem Jahr 1948 bleiben für die moderne KI ebenso relevant wie für die Telekommunikation.