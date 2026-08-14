<!--
---
# Metadata
title: "Game Theory"
description: "Strategic-form games, Nash equilibrium, dominant strategies, minimax theorem, cooperative games, Shapley value, mechanism design, auction theory, and connections to multi-agent reinforcement learning"
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
    changes: "Initial deep-dive into game theory"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2027-02-10"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-10"

# Classification
tags: [game-theory, nash-equilibrium, minimax, cooperative-games, shapley-value, mechanism-design, auction-theory, multi-agent-rl]
difficulty_level: "intermediate"
prerequisites:
  - "mathematics.md"
  - "optimization.md"
  - "statistics_and_probability.md"
estimated_reading_time: "25 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Spieltheorie
Die Spieltheorie ist die Mathematik der strategischen Interaktion – Situationen, in denen Ihr Ergebnis nicht nur von Ihren eigenen Entscheidungen, sondern auch von den Entscheidungen anderer abhängt. Von Preiskämpfen zwischen Unternehmen bis hin zu nuklearen Wettrüsten, von Online-Auktionen bis hin zur Evolutionsbiologie – die Spieltheorie liefert die Werkzeuge zur Analyse von Konflikten und Kooperationen. Durch Multiagenten-Verstärkungslernen, generative kontradiktorische Netzwerke (Generative Adversarial Networks, GANs) und Mechanismusdesign für Online-Plattformen ist es für maschinelles Lernen immer relevanter geworden.
---

## Spiele in strategischer Form
### Definition
Ein **Spiel in strategischer Form (Normalform)** besteht aus:
- Eine Gruppe von Spielern N = {1, 2, ..., n}
- Strategiesätze S₁, S₂, ..., Sₙ für jeden Spieler
- Auszahlungsfunktionen u₁, u₂, ..., uₙ, die Strategieprofile auf reelle Zahlen abbilden
### Beispiel: Gefangenendilemma
| | Kooperieren (C) | Defekt (D) |
|---|---------------|------------|
| **Kooperieren (C)** | (−1, −1) | (−3, 0) |
| **Defekt (D)** | (0, −3) | (−2, −2) |
| Analyse | Ergebnis |
|----------|--------|
| Dominante Strategie | Defekt (D dominiert C für beide Spieler) |
| Nash-Gleichgewicht | (D, D) mit Auszahlung (−2, −2) |
| Soziales Optimum | (C, C) mit Auszahlung (−1, −1) |
| Dilemma | Individuelle Rationalität führt zu kollektiver Irrationalität |
### Weitere klassische Spiele
**Kampf der Geschlechter:**
| | Oper | Fußball |
|---|-------|----------|
| Oper | (2, 1) | (0, 0) |
| Fußball | (0, 0) | (1, 2) |
Zwei Nash-Gleichgewichte: (Oper, Oper) und (Fußball, Fußball).
**Huhn (Falkentaube):**
| | Falke | Taube |
|---|------|------|
| Falke | (−10, −10) | (5, 0) |
| Taube | (0, 5) | (1, 1) |
Zwei Nash-Gleichgewichte: (Hawk, Dove) und (Dove, Hawk).
---

## Dominante Strategien
| Konzept | Definition |
|---------|------------|
| **Streng dominant** | Strategie-Sᵢ bietet eine höhere Auszahlung als jede andere Strategie, unabhängig von den Entscheidungen des Gegners |
| **Schwach dominant** | Strategie-Sᵢ bietet eine mindestens so hohe Auszahlung wie alle anderen, bei einigen Gegnerprofilen sogar noch höher |
| **Dominierte Strategie** | Eine Strategie, die niemals die beste Antwort ist |
**Iterierte Eliminierung dominierter Strategien:**
1. Entfernen Sie alle streng dominierten Strategien
2. Wiederholen, bis nichts mehr entfernt werden kann
3. Wenn ein Strategieprofil übrig bleibt, ist es das einzigartige Nash-Gleichgewicht
---

## Nash-Gleichgewicht
Ein **Nash-Gleichgewicht** ist ein Strategieprofil, bei dem kein Spieler seine Auszahlung durch einseitige Änderung seiner Strategie verbessern kann.
### Definition
(s₁*, s₂*, ..., sₙ*) ist ein Nash-Gleichgewicht, wenn für jeden Spieler i:
uᵢ(sᵢ*, s₋ᵢ*) ≥ uᵢ(sᵢ, s₋ᵢ*) für alle sᵢ ∈ Sᵢ
### Nash-Gleichgewichte finden (2×2 Spiele)
**Beste Antwortmethode:**
1. Unterstreichen Sie in jeder Spalte die beste Antwort von Spieler 1
2. Unterstreichen Sie in jeder Zeile die beste Antwort von Spieler 2
3. Zellen, in denen beide unterstrichen sind, sind Nash-Gleichgewichte
### Existenz (Nashs Theorem)
Jedes endliche Spiel hat mindestens ein Nash-Gleichgewicht (ggf. bei gemischten Strategien).
### Gemischte Strategien
Eine **gemischte Strategie** ist eine Wahrscheinlichkeitsverteilung über reine Strategien.
| Konzept | Definition |
|---------|------------|
| Gemischte Strategie σᵢ | Wahrscheinlichkeitsverteilung über Sᵢ |
| Gemischte Strategie NE | Kein Spieler kann die erwartete Auszahlung verbessern, indem er seine Mischung ändert |
| Unterstützung | Satz reiner Strategien, die mit positiver Wahrscheinlichkeit gespielt werden |
**Arbeitsbeispiel: Passende Pennies**
| | Köpfe | Schwänze |
|---|-------|-------|
| Köpfe | (1, −1) | (−1, 1) |
| Schwänze | (−1, 1) | (1, −1) |
Keine reine Strategie NE. Gemischtes NE: beide spielen H und T mit jeweils ½ Wahrscheinlichkeit.
---

## Minimax-Theorem
### Nullsummenspiele
In einem **Nullsummenspiel** ist der Gewinn eines Spielers genau der Verlust des anderen: u₁ + u₂ = 0.
### Von Neumanns Minimax-Theorem
Für jedes endliche Nullsummenspiel für zwei Spieler:
max_{σ₁} min_{σ₂} u₁(σ₁, σ₂) = min_{σ₂} max_{σ₁} u₁(σ₁, σ₂)
Das **Maximum** (bester Worst-Case für Spieler 1) entspricht dem **Minimax** (bester Worst-Case für Spieler 2). Dieser gemeinsame Wert ist der **Wert des Spiels**.
### Nullsummenspiele lösen
Für ein 2×2-Nullsummenspiel mit Matrix:
| | L | R |
|---|---|---|
| T | ein | b |
| B | c | d |
Die optimale gemischte Strategie von Spieler 1: Spielen Sie T mit der Wahrscheinlichkeit p = (d−c)/((a−b)+(d−c))
Spielwert: v = (ad−bc)/((a−b)+(d−c))
---

## Extensive-Form-Spiele
Spiele mit aufeinanderfolgenden Zügen werden als **Spielbäume** dargestellt.
### Schlüsselkonzepte
| Konzept | Definition |
|---------|------------|
| **Wildbaum** | Baum mit allen möglichen Zugfolgen |
| **Informationssatz** | Satz von Knoten, die ein Spieler nicht unterscheiden kann |
| **Perfekte Informationen** | Jeder Informationssatz ist ein Singleton (alle Bewegungen beobachtbar) |
| **Teilspiel perfekt NE** | Nash-Gleichgewicht in jedem Teilspiel |
| **Rückwärtsinduktion** | Lösen Sie vom Ende des Baums nach hinten |
### Zermelos Satz
Bei endlichen Spielen mit perfekter Information und ohne Chance für zwei Spieler: Entweder hat ein Spieler eine Gewinnstrategie, oder beide können ein Unentschieden erzwingen (z. B. Schach).
---

## Kooperative Spiele
In **kooperativen Spielen** können Spieler verbindliche Vereinbarungen und Koalitionen bilden.
### Charakteristische Funktion
Ein kooperatives Spiel wird durch eine **charakteristische Funktion** v: 2^N → ℝ definiert, wobei v(S) der Wert ist, den die Koalition S erreichen kann.
| Eigentum | Definition |
|----------|------------|
| **Superadditiv** | v(S ∪ T) ≥ v(S) + v(T) für disjunkte S, T |
| **Konvex** | v(S ∪ {i}) − v(S) ≤ v(T ∪ {i}) − v(T) für S ⊂ T |
### Der Kern
Der **Kern** ist die Menge der Zuteilungen, bei der sich keine Koalition durch Abspaltung verbessern kann:
Kern = {x ∈ ℝⁿ : Σᵢ∈N xᵢ = v(N), Σᵢ∈S xᵢ ≥ v(S) für alle S ⊂ N}
Der Kern kann leer sein – in diesem Fall ist keine stabile Zuordnung vorhanden.
### Shapley-Wert
Der **Shapley-Wert** bietet eine einzigartige faire Allokation basierend auf Grenzbeiträgen:
φᵢ = Σ_{S ⊂ N\{i}} (|S|!(n−|S|−1)!/n!) · [v(S ∪ {i}) − v(S)]
| Eigentum | Aussage |
|----------|-----------|
| Effizienz | Σ φᵢ = v(N) (alle Werte sind verteilt) |
| Symmetrie | Gleiche Beitragszahler erhalten gleiche Auszahlungen |
| Dummy-Spieler | Nicht-Mitwirkende erhalten null |
| Additivität | φ(v + w) = φ(v) + φ(w) |
**Interpretation:** Der Shapley-Wert jedes Spielers ist sein durchschnittlicher Grenzbeitrag über alle möglichen Reihenfolgen der Koalitionsbildung hinweg.
### Ausgearbeitetes Beispiel
Drei Spieler: v(∅) = 0, v({1}) = 0, v({2}) = 0, v({3}) = 0, v({1,2}) = 50, v({1,3}) = 70, v({2,3}) = 60, v({1,2,3}) = 100.
| Spieler | Grenzbeiträge (gemittelt über Bestellungen) | Shapley-Wert |
|--------|------------------------------------|---------------|
| 1 | (100+50+70+70+50+0)/6 = 56,7 | 37,5 |
| 2 | (100+50+60+60+50+0)/6 | 27,5 |
| 3 | (100+70+60+70+60+0)/6 | 35,0 |
(Präzise berechnet unter Verwendung der Shapley-Formel für jede Permutation.)
---

## Mechanismusdesign
**Mechanismusdesign** ist „inverse Spieltheorie“ – anstatt gegebene Spiele zu analysieren, entwerfen Sie Spiele, die die gewünschten Ergebnisse liefern.
### Das Offenbarungsprinzip
Jeder Mechanismus, der ein gewünschtes Ergebnis erzielt, kann durch einen **Mechanismus der direkten Offenbarung** ersetzt werden, bei dem die Wahrheitsfindung ein Nash-Gleichgewicht ist.
### Auktionstheorie
| Auktionstyp | Regeln | Umsatzäquivalenz |
|-------------|-------|-------|
| **Versiegeltes Erstpreisangebot** | Höchstbietender gewinnt, zahlt sein Gebot | Alle Standardauktionen bringen den gleichen erwarteten Umsatz |
| **Versiegeltes Gebot zum zweiten Preis (Vickrey)** | Der Höchstbietende gewinnt, das zweithöchste Gebot zahlt | (unter unabhängigen privaten Werten) |
| **Englisch (aufsteigend)** | Preiserhöhungen; Erster, der Siege akzeptiert | — |
| **Niederländisch (absteigend)** | Preis fällt; Erster, der Siege akzeptiert | — |
### Vickrey-Auktion (Zweiter Preis)
**Dominante Strategie:** Bieten Sie Ihren wahren Wert.
| Eigentum | Aussage |
|----------|-----------|
| Ehrliches Bieten | Schwach dominante Strategie |
| Effizienz | Artikel geht an den Meistbietenden |
| Umsatz | Gleicher erwarteter Umsatz wie beim Erstpreis (Revenue Equivalence Theorem) |
### Optimales Auktionsdesign (Myerson)
Die umsatzmaximierende Auktion:
- Zuweisung an den Bieter mit der höchsten **virtuellen Bewertung**
- Legt einen Mindestpreis fest
- Virtuelle Bewertung: ψ(v) = v − (1−F(v))/f(v)
---

## Verbindungen zum maschinellen Lernen
### Generative Adversarial Networks (GANs)
GANs sind ein Zwei-Spieler-Spiel zwischen einem Generator G und einem Diskriminator D:
min_G max_D V(D, G) = E[log D(x)] + E[log(1 − D(G(z)))]
| Spieltheorie-Konzept | GAN-Äquivalent |
|------|-----------------|
| Nullsummenspiel für zwei Spieler | Generator vs. Diskriminator |
| Nash-Gleichgewicht | G generiert reale Daten, D gibt überall ½ aus |
| Minimax | Die GAN-Zielfunktion |
| Moduszusammenbruch | Nichterreichen des Gleichgewichts |
### Multi-Agent Reinforcement Learning (MARL)
| Konzept | MARL-Anwendung |
|---------|---|
| Nash-Gleichgewicht | Stabile Richtlinien in Multi-Agent-Einstellungen |
| Minimax | Robuste Richtlinien gegen gegnerische Gegner |
| Kooperative Spiele | Koalitionsbildung, Aufgabenverteilung |
| Shapley-Wert | Kreditzuweisung (Welcher Agent hat was beigetragen?) |
| Mechanismusdesign | Gestaltung von Anreizen in Multi-Agenten-Systemen |
| Fiktives Theaterstück | Lernalgorithmus konvergiert zum Nash-Gleichgewicht |
### Andere ML-Verbindungen
| Bewerbung | Spieltheorie-Tool |
|-------------|---|
| Anzeigenauktionsdesign (Google, Facebook) | Mechanismusdesign, Auktionstheorie |
| Marktplatzgestaltung (Uber, Airbnb) | Matching-Theorie, Mechanismusdesign |
| Gegnerische Robustheit | Nullsummenspiele zwischen Angreifer und Verteidiger |
| Messeaufteilung | Shapley-Wert, neidfreie Zuteilung |
| Föderiertes Lernen | Kooperative Spieltheorie zur Beitragsmessung |
| Empfehlungssysteme | Mechanismusdesign zur wahrheitsgetreuen Präferenzerhebung |
---

## Zusammenfassung
| Konzept | Kernidee | Wichtigstes Ergebnis |
|---------|-----------|------------|
| Strategische Formspiele | Spieler, Strategien, Auszahlungen | Spielmatrixdarstellung |
| Dominante Strategien | Am besten unabhängig von anderen | Iterierte Eliminierung |
| Nash-Gleichgewicht | Keine gewinnbringende einseitige Abweichung | Existiert in jedem endlichen Spiel |
| Gemischte Strategien | Über Aktionen randomisieren | Nashs Existenzsatz |
| Minimax | Bester Worst-Case (Nullsumme) | Von Neumanns Minimax-Theorem |
| Umfangreiche Form | Sequentielle Bewegungen | Rückwärtsinduktion, Teilspielperfektion |
| Kooperative Spiele | Verbindliche Koalitionen | Kern, Shapley-Wert |
| Mechanismusdesign | Entwerfen Sie Spiele für Ergebnisse | Offenbarungsprinzip, optimale Auktionen |
| Auktionstheorie | Verkauf über Konkurrenz | Einnahmenäquivalenz, Vickrey-Auktion |
Spieltheorie ist die Mathematik des strategischen Denkens. In einer Welt, die zunehmend von interagierenden KI-Agenten, automatisierten Marktplätzen und gegnerischen Systemen bevölkert ist, stellt die Spieltheorie das wesentliche Werkzeug zur Verhaltensvorhersage, zum Entwurf von Mechanismen und zum Aufbau robuster Multi-Agenten-Systeme bereit. Für Datenwissenschaftler erklärt es, wie GANs funktionieren, wie Online-Auktionen Einnahmen in Milliardenhöhe generieren und wie man KI-Systeme aufbaut, die im Wettbewerbsumfeld gut funktionieren.