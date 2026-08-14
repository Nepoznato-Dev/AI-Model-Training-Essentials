---
# Metadata
title: "Stochastic Processes"
description: "Random variables review, Markov chains, random walks, Brownian motion, Poisson processes, martingales, Monte Carlo methods, and MCMC"
category: "Data Science and Analytics"
subcategory: "Mathematics"
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
    date: "2026-08-10"
    author: "Nepoznato-Dev"
    changes: "Initial deep-dive into stochastic processes"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2027-02-10"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-10"

# Classification
tags: [stochastic-processes, markov-chains, random-walks, brownian-motion, poisson-processes, martingales, monte-carlo, mcmc]
difficulty_level: "advanced"
prerequisites:
  - "statistics_and_probability.md"
  - "real_analysis.md"
estimated_reading_time: "28 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Stochastische Prozesse
Ein **stochastischer Prozess** ist eine Sammlung zeitlich (oder räumlich) indizierter Zufallsvariablen. Während die Wahrscheinlichkeitstheorie einzelne Zufallsereignisse untersucht, untersuchen stochastische Prozesse, wie sich Zufälligkeit im Laufe der Zeit entwickelt. Sie modellieren Aktienkurse, Warteschlangenlängen, Krankheitsausbreitung, Sprachgenerierung und die Trainingsdynamik von Modellen für maschinelles Lernen.
---

## Stiftungen
### Definition
Ein stochastischer Prozess {X_t : t ∈ T} ist eine Familie von Zufallsvariablen, die auf einem gemeinsamen Wahrscheinlichkeitsraum definiert sind. T ist der **Indexsatz** (Zeit):
- **Diskrete Zeit:** T = {0, 1, 2, ...}
- **Kontinuierliche Zeit:** T = [0, ∞)
Der **Zustandsraum** S ist die Menge möglicher Werte, die X_t annehmen kann.
### Schlüsseleigenschaften
| Eigentum | Definition |
|----------|------------|
| **Stationarität** | Gemeinsame Verteilung von (X_{t₁}, ..., X_{tₖ}) wie (X_{t₁+τ}, ..., X_{tₖ+τ}) |
| **Unabhängigkeit** | X_t unabhängig von X_s für t ≠ s |
| **Ergodizität** | Zeitmittelwerte konvergieren zu Ensemblemittelwerten |
| **Markov-Eigenschaft** | Die Zukunft hängt nur von der Gegenwart ab, nicht von der Vergangenheit |
| **Martingal** | Erwarteter zukünftiger Wert entspricht aktuellem Wert |
---

## Markov-Ketten
Eine **Markov-Kette** ist ein stochastischer Prozess, bei dem der zukünftige Zustand nur vom aktuellen Zustand abhängt (gedächtnislose Eigenschaft).
### Zeitdiskrete Markov-Ketten (DTMC)
P(X_{n+1} = j | X_n = i, X_{n-1} = i_{n-1}, ...) = P(X_{n+1} = j | X_n = i) = p_{ij}
Die **Übergangsmatrix** P hat Einträge p_{ij} = P(gehe zu j | derzeit bei i).
| Eigentum | Aussage |
|----------|-----------|
| Zeilensummen | Jede Zeile summiert sich zu 1: Σⱼ p_{ij} = 1 |
| n-stufiger Übergang | P(X_{n+m} = j | X_m = i) = (Pⁿ)_{ij} |
| Stationäre Verteilung | πP = π (linker Eigenvektor mit Eigenwert 1) |
### Klassifizierung der Staaten
| Begriff | Definition |
|------|------------|
| **Wiederkehrend** | Die Kette kehrt mit der Wahrscheinlichkeit 1 | in den Zustand i zurück
| **Vorübergehend** | Die Wahrscheinlichkeit, niemals zurückzukehren, ist ungleich Null |
| **Absorbierend** | p_{ii} = 1 (einmal eingegeben, nie verlassen) |
| **Zeitraum** | GCD der Rückkehrzeiten; Periode 1 = aperiodisch |
| **Kommunikation** | Die Zustände i und j können einander erreichen |
### Stationäre Verteilung
Für eine irreduzible, positiv rekurrente Markov-Kette existiert die stationäre Verteilung π, ist eindeutig und erfüllt:
πP = π, Σᵢ πᵢ = 1
**Interpretation:** πᵢ = langfristiger Anteil der im Zustand i verbrachten Zeit.
**Arbeitsbeispiel:** Wettermodell mit den Zuständen {Sunny, Rainy}.
P = [[0,9, 0,1], [0,5, 0,5]] (Zeilen: von Sunny, von Rainy)
Stationäre Verteilung: πP = π
- π₁ = 0,9π₁ + 0,5π₂
- π₂ = 0,1π₁ + 0,5π₂
- π₁ + π₂ = 1
- Lösung: π₁ = 5/6 ≈ 0,833, π₂ = 1/6 ≈ 0,167
### Konvergenz zur Stationarität
Für eine irreduzible, aperiodische, positiv rekurrente Kette:
- Pⁿ → Π (Matrix mit allen Zeilen gleich π) als n → ∞
- **Mischzeit:** Anzahl der Schritte, bis die Verteilung nahe bei π liegt
- **Spektrale Lücke:** 1 − |λ₂| (wobei λ₂ der zweitgrößte Eigenwert ist) bestimmt die Mischgeschwindigkeit
### Zeitkontinuierliche Markov-Ketten (CTMC)
Übergänge treten zu zufälligen Zeitpunkten auf, die durch Exponentialverteilungen bestimmt werden.
| Konzept | Beschreibung |
|---------|-------------|
| **Ratenmatrix Q** | q_{ij} ≥ 0 für i ≠ j; q_{ii} = −Σ_{j≠i} q_{ij} |
| **Übergangswahrscheinlichkeiten** | P(t) = e^{Qt} (exponentielle Matrix) |
| **Stationäre Verteilung** | πQ = 0 |
| **Haltezeit** | Die Zeit im Zustand i ist Exp(−q_{ii}) |
---

## Zufällige Spaziergänge
Ein **Random Walk** ist ein Weg, der aus aufeinanderfolgenden zufälligen Schritten besteht.
### Einfacher Zufallsgang
X_n = X_{n-1} + Z_n, wobei Z_n ∈ {+1, −1} mit Wahrscheinlichkeiten p, q = 1−p.
| Eigentum | p = 1/2 (symmetrisch) | p ≠ 1/2 (voreingenommen) |
|----------|-------|-------------------|
| E[X_n] | 0 | n(2p−1) |
| Var[X_n] | n | 4npq |
| Rückkehr zum Ursprung? | Ja (mit Wahrscheinlichkeit 1) | Nein (driftet weg) |
| Wiederkehrend? | Ja (in 1D und 2D) | Nein |
### Random Walk in höheren Dimensionen
| Dimension | Wiederkehrend? | Intuition |
|-----------|------------|-----------|
| 1D | Ja | „Ein betrunkener Mann findet immer den Weg nach Hause“ |
| 2D | Ja | „Ein betrunkener Vogel findet immer seinen Weg nach Hause“ |
| 3D+ | Nein | „Ein betrunkener Spatz findet nie den Weg nach Hause“ |
### Verbindung zur Brownschen Bewegung
Skalieren einer Zufallswanderung: Sei S_n = ΣZ_i. Dann gilt als Schrittweite → 0 und Schritte → ∞:
S_{⌊nt⌋} / √n → B(t) (Brownsche Bewegung, nach dem Satz von Donsker)
---

## Brownsche Bewegung
**Brownsche Bewegung** (Wiener-Prozess) B(t) ist das zeitkontinuierliche Limit einer Irrfahrt.
### Definition
B(t) erfüllt:
1. B(0) = 0
2. B(t) hat stetige Pfade
3. Unabhängige Inkremente: B(t) − B(s) ist unabhängig von B(s) − B(r) für r < s < t
4. B(t) − B(s) ~ N(0, t − s) (Gaußsche Inkremente)
### Schlüsseleigenschaften
| Eigentum | Aussage |
|----------|-----------|
| E[B(t)] | = 0 |
| Var[B(t)] | = t |
| Cov[B(s), B(t)] | = min(s, t) |
| Nirgendwo differenzierbar | Pfade sind stetig, haben aber keine Ableitung |
| Fraktale Dimension | Der Graph hat die Hausdorff-Dimension 3/2 |
| Markov-Eigenschaft | Die Zukunft hängt nur von der aktuellen Position ab |
| Martingal | E[B(t) | F_s] = B(s) für s < t |
### Geometrische Brownsche Bewegung
S(t) = S(0) exp((μ − σ²/2)t + σB(t))
Dies ist das Standardmodell für Aktienkurse im Black-Scholes-Modell.
- μ: Drift (erwartete Rendite)
- σ: Volatilität
---

## Poisson-Prozesse
Ein **Poisson-Prozess** N(t) zählt die Anzahl der Ereignisse, die in [0, t] auftreten.
### Definition
N(t) ~ Poisson(λt), wobei λ die Rate (Ereignisse pro Zeiteinheit) ist.
| Eigentum | Aussage |
|----------|-----------|
| N(0) = 0 | — |
| Unabhängige Inkremente | Ereignisse in disjunkten Intervallen sind unabhängig |
| Stationäre Inkremente | N(t+s) − N(s) ~ Poisson(λt) |
| E[N(t)] | = λt |
| Var[N(t)] | = λt |
| Zwischenankunftszeiten | Exponentiell verteilt: T_i ~ Exp(λ) |
### Verallgemeinerungen
| Variante | Beschreibung |
|---------|-------------|
| **Inhomogen** | Rate λ(t) variiert mit der Zeit |
| **Zusammengesetztes Gift** | Jedes Ereignis hat eine zufällige Größe: S(t) = Σᵢ₌₁^{N(t)} Yᵢ |
| **Poisson-Zufallsmaß** | Punkte in der Raumzeit, nicht nur in der Zeit |
| **Multivariat** | Mehrere Ereignistypen mit möglichen Interaktionen |
---

## Martingale
Ein **Martingal** ist ein faires Spiel: Der erwartete zukünftige Wert entspricht unter Berücksichtigung aller aktuellen Informationen dem aktuellen Wert.
### Definition
{X_n} ist ein Martingal bezüglich der Filterung {F_n}, wenn:
1. X_n ist F_n-messbar (angepasst)
2. E[|X_n|] < ∞ (integrierbar)
3. E[X_{n+1} | F_n] = X_n (faires Spiel)
| Variante | Zustand | Interpretation |
|---------|-----------|----------------|
| **Martingal** | E[X_{n+1} | F_n] = X_n | Faires Spiel |
| **Submartingal** | E[X_{n+1} | F_n] ≥ X_n | Günstiges Spiel (Tendenz steigend) |
| **Supermartingal** | E[X_{n+1} | F_n] ≤ X_n | Ungünstiges Spiel (Tendenz nach unten) |
### Schlüsselsätze
| Satz | Aussage |
|---------|-----------|
| **Optionales Anhalten** | Unter Bedingungen ist E[X_T] = E[X_0] für eine Stoppzeit T |
| **Konvergenz** | Ein beschränktes Martingal konvergiert fast sicher |
| **Maximale Ungleichheit** | P(max_{k≤n} X_k ≥ λ) ≤ E[X_n] / λ (Doob's) |
---

## Monte-Carlo-Methoden
**Monte-Carlo-Methoden** verwenden Zufallsstichproben, um deterministische Größen zu schätzen.
### Grundidee
So schätzen Sie E[f(X)] mit X ~ P:
1. Zeichnen Sie N Stichproben: x₁, x₂, ..., x_N aus P
2. Berechnen Sie: Î = (1/N) Σᵢ f(xᵢ)
3. Nach dem Gesetz der großen Zahlen: Î → E[f(X)] als N → ∞
**Fehler:** Standardfehler = σ_f / √N, wobei σ_f² = Var[f(X)]
### Techniken zur Varianzreduktion
| Technik | Idee | Beschleunigung |
|-----------|------|---------|
| **Wichtigkeit der Probenahme** | Stichprobe aus Q statt P, Gewichtung nach P/Q | Kann dramatisch sein |
| **Antithetische Variablen** | Verwenden Sie Paare (x, −x), um die Varianz | aufzuheben ~2x |
| **Kontrollvariablen** | Subtrahieren Sie die mit f | korrelierte bekannte Erwartungsfunktion Variiert |
| **Geschichtete Stichprobe** | Domäne aufteilen, jede Schicht beproben | Reduziert die Varianz |
| **Rao-Blackwell** | Voraussetzung für ausreichende Statistiken | Hilft immer |
---

## Markov-Kette Monte Carlo (MCMC)
MCMC konstruiert eine Markov-Kette, deren stationäre Verteilung die Zielverteilung ist. Nach einer „Einbrennphase“ werden die Proben ungefähr dem Ziel entnommen.
### Metropolis-Hastings-Algorithmus
| Schritt | Aktion |
|------|--------|
| 1 | Aktueller Status: x_t |
| 2 | Vorschlag: x* ~ q(x* \| x_t) (Vorschlagsverteilung) |
| 3 | Akzeptanzverhältnis: α = min(1, [π(x*)q(x_t\|x*)] / [π(x_t)q(x*\|x_t)]) |
| 4 | Akzeptiere mit Wahrscheinlichkeit α: x_{t+1} = x* (akzeptiere) oder x_t (ablehne) |
**Sonderfall – Metropolis-Algorithmus:** Symmetrischer Vorschlag q(x*|x) = q(x|x*), also α = min(1, π(x*)/π(x_t)).
### Gibbs-Probenahme
Ein Sonderfall von Metropolis-Hastings, bei dem jede Variable aus ihrer vollständigen bedingten Verteilung aktualisiert wird.
Für Ziel π(x₁, x₂, ..., xₖ):
1. Beispiel x₁^{(t+1)} ~ π(x₁ | x₂^{(t)}, ..., xₖ^{(t)})
2. Beispiel x₂^{(t+1)} ~ π(x₂ | x₁^{(t+1)}, x₃^{(t)}, ..., xₖ^{(t)})
3. Fahren Sie für alle Variablen fort
4. Wiederholen
| Eigentum | Aussage |
|----------|-----------|
| Akzeptiert immer | α = 1 (kein Ablehnungsschritt) |
| Erfordert | Möglichkeit zur Stichprobe aus jeder vollständigen Bedingung |
| Konvergenz | Garantiert für irreduzible, aperiodische Ketten |
### MCMC-Diagnose
| Diagnose | Zweck |
|-----------|---------|
| **Trace-Plot** | Visuelle Prüfung auf Durchmischung und Stationarität |
| **Autokorrelation** | Misst die Stichprobenabhängigkeit (geringe Autokorrelation erforderlich) |
| **Gelman-Rubin (R̂)** | Vergleichen Sie mehrere Ketten; R̂ < 1,05 deutet auf Konvergenz | hin
| **Effektive Stichprobengröße** | N_eff = N / (1 + 2Σρₖ); berücksichtigt Autokorrelation |
| **Einbrennen** | Entsorgen Sie die ersten Proben, bevor die Kette Stationarität erreicht |
---

## Relevanz für maschinelles Lernen und Datenwissenschaft
| Stochastischer Prozess | Bewerbung |
|-----|-------------|
| Markov-Ketten | PageRank (Random Walk on Web Graph), Textgenerierung (n-Gramm-Modelle), MCMC |
| Zufallswanderungen | Node2Vec und DeepWalk (Grapheneinbettungen), Erkundung in RL |
| Brownsche Bewegung | Aktienkursmodellierung, Diffusionsmodelle in generativer KI |
| Poisson-Prozesse | Modellierung des Ereigniseingangs (Klicks, Ausfälle), Warteschlangentheorie |
| Martingale | Finanzmathematik, Beweis der Konvergenz des SGD (stochastische Näherung) |
| Monte-Carlo | Schätzung erwarteter Werte, Bayesianische Inferenz, verstärkendes Lernen (Richtlinienbewertung) |
| MCMC (Metropolis-Hastings) | Bayesianisches Posterior-Sampling, probabilistische Programmierung (Stan, PyMC) |
| Gibbs-Probenahme | Themenmodelle (LDA), Bayesianische Netzwerke, Bildrauschunterdrückung |
| MCMC-Diagnose | Sicherstellung zuverlässiger Schlussfolgerungen aus probabilistischen Modellen |
---

## Zusammenfassung
| Prozess | Zustandsraum | Zeit | Schlüsseleigenschaft |
|---------|-------------|------|--------------|
| Markov-Kette | Diskret/kontinuierlich | Diskret/kontinuierlich | Memoryless (Markov-Eigenschaft) |
| Zufälliger Spaziergang | ℤᵈ | Diskret | Summe von i.i.d. Schritte |
| Brownsche Bewegung | ℝ | Kontinuierlich | Gaußsche Inkremente, kontinuierliche Pfade |
| Poisson-Prozess | ℕ | Kontinuierlich | Zählvorgang mit exponentiellen Lücken |
| Martingal | ℝ | Diskret/kontinuierlich | Faires Spiel (E[X_{t+1}|F_t] = X_t) |
Stochastische Prozesse sind die Mathematik der Zufälligkeit über die Zeit. Sie untermauern die moderne Bayes'sche Inferenz (MCMC), das verstärkende Lernen (Markov-Entscheidungsprozesse), die generative Modellierung (Diffusionsmodelle), die Finanzmathematik und die Warteschlangentheorie. Wenn Sie diese Prozesse verstehen, erhalten Sie die Werkzeuge, um Unsicherheit dynamisch zu modellieren – nicht nur als Momentaufnahme, sondern während sie sich entwickelt.