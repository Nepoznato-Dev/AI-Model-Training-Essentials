---
# Metadata
title: "Reinforcement Learning"
description: "MDPs, Q-learning, policy gradients, RLHF, multi-agent systems"
category: "AI and Machine Learning"
subcategory: "Model Architectures"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "AI Model Training Team"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.1"
    date: "2026-08-09"
    author: "AI Model Training Team"
    changes: "Moved to architectures/ subfolder; added subcategory field"
  - version: "1.0.0"
    date: "2026-08-05"
    author: "AI Model Training Team"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-09"
review_date: "2027-02-05"
reviewed_by: "AI & Machine Learning Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [reinforcement, learning, ai-and-machine-learning]
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

# Verstärkungslernen
Beim Reinforcement Learning (RL) lernen Maschinen durch Versuch und Irrtum, Entscheidungssequenzen zu treffen. Im Gegensatz zum überwachten Lernen, bei dem für jedes Beispiel die richtige Antwort bereitgestellt wird, gibt RL einem Agenten lediglich ein Belohnungssignal – und der Agent muss herausfinden, welche Aktionen im Laufe der Zeit zu den besten Ergebnissen führen. Es ist der Ansatz hinter AlphaGo, der Robotersteuerung, der Spiel-KI und – ganz entscheidend – RLHF, der Technik, die verwendet wird, um moderne große Sprachmodelle mit menschlichen Vorlieben in Einklang zu bringen.
---

## Kernkonzepte
RL stellt die Entscheidungsfindung als eine Schleife zwischen einem **Agenten** und einer **Umgebung** dar.
| Komponente | Rolle | Beispiel |
|-----------|------|---------|
| **Agent** | Der Entscheider | Ein Schachprogramm, ein Roboter, ein Sprachmodell |
| **Umwelt** | Die Welt, mit der der Agent interagiert | Das Schachbrett, ein Lagerhaus, ein Gespräch |
| **Staat** | Die aktuelle Situation | Board-Position, Messwerte der Robotersensoren, Chat-Verlauf |
| **Aktion** | Was der Agent tun kann | Eine Figur bewegen, nach links drehen, einen Spielstein erzeugen |
| **Belohnung** | Rückmeldesignal (Skalarzahl) | +1 für Sieg, -1 für Absturz, menschlicher Präferenzwert |
| **Richtlinie** | Strategie, die Zustände Aktionen zuordnet | „Wenn der König bedroht ist, bewegen Sie ihn“ |
| **Wertfunktion** | Erwartete kumulative Belohnung von einem Staat | „Dieser Vorstandsplatz ist etwa +3 Punkte wert“ |
### Die RL-Schleife
```
Agent observes State → chooses Action → Environment returns new State + Reward
        ↑                                                                         |
        └─────────────────────────────────────────────────────────────────────────┘
```

Das Ziel des Agenten besteht darin, die **kumulative Belohnung** im Laufe der Zeit zu maximieren, nicht nur die unmittelbare Belohnung. Dies unterscheidet RL grundlegend vom überwachten Lernen.
---

## Hauptunterschiede zu anderen Lernparadigmen
| Aspekt | Überwachtes Lernen | Unüberwachtes Lernen | Verstärkungslernen |
|--------|-----|-------|----------------------|
| **Signal** | Richtige Bezeichnungen für jedes Beispiel | Keine Etiketten; Struktur finden | Skalare Belohnung, oft verzögert |
| **Feedback** | Sofort | Keine | Verzögert und spärlich |
| **Sequenz** | Jedes Beispiel ist unabhängig | Jedes Beispiel ist unabhängig | Aktionen wirken sich auf zukünftige Zustände aus |
| **Ziel** | Vorhersagefehler minimieren | Muster entdecken | Kumulative Belohnung maximieren |
---

## Markov-Entscheidungsprozesse (MDPs)
MDPs sind der mathematische Rahmen für RL. Sie gehen davon aus, dass die Zukunft nur vom aktuellen Zustand abhängt, nicht von der Geschichte, wie Sie dorthin gelangt sind (die **Markov-Eigenschaft**).
| Komponente | Notation | Bedeutung |
|-----------|----------|---------|
| **Staaten** | S | Alle möglichen Situationen, in denen sich der Agent befinden kann |
| **Aktionen** | A | Alles, was der Agent tun kann |
| **Übergangsfunktion** | P(s' \| s, a) | Wahrscheinlichkeit, den Zustand s' zu erreichen, nachdem die Aktion a im Zustand s | durchgeführt wurde
| **Belohnungsfunktion** | R(s, a, s') | Belohnung für den Übergang erhalten |
| **Rabattfaktor** | γ (Gamma) | Wie hoch ist der Wert zukünftiger Belohnungen im Vergleich zu unmittelbaren Belohnungen (0 zu 1) |
Die **Rückgabe** (Gesamtrabattprämie) beträgt:
```
G = R₁ + γR₂ + γ²R₃ + ...
```

Ein hoher Abzinsungsfaktor (γ nahe 1) bedeutet, dass der Agent weitsichtig ist. Ein niedriger Wert bedeutet, dass es kurzsichtig ist.
---

## Klassische RL-Algorithmen
### Wertbasierte Methoden
Diese erfahren, wie gut jeder Zustand (oder jedes Zustands-Aktionspaar) ist.
| Algorithmus | Schlüsselidee | Einschränkung |
|-----------|----------|------------|
| **Q-Learning** | Lernen Sie eine Tabelle mit Q-Werten: Q(Zustand, Aktion) = erwartete Belohnung | Lässt sich nicht auf große Zustandsräume skalieren |
| **Deep Q-Network (DQN)** | Verwenden Sie ein neuronales Netzwerk, um Q-Werte anzunähern | Verarbeitet nur diskrete Aktionen; kann instabil sein |
| **Doppelter DQN** | Korrigieren Sie den Überschätzungsbias von Q-Learning | Immer noch auf diskrete Aktionen beschränkt |
Q-Learning-Aktualisierungsregel:
```
Q(s, a) ← Q(s, a) + α [r + γ max Q(s', a') - Q(s, a)]
```

### Richtlinienbasierte Methoden
Diese erlernen direkt die Politik (Strategie), ohne Werte abzuschätzen.
| Algorithmus | Schlüsselidee | Vorteil |
|-----------|----------|-----------|
| **VERSTÄRKEN** | Monte-Carlo-Politikgradient; Politik in Richtung guter Ergebnisse aktualisieren | Einfach; arbeitet mit kontinuierlichen Aktionen |
| **PPO** (Proximale Richtlinienoptimierung) | Beschneiden Sie Richtlinienaktualisierungen, um große, destabilisierende Änderungen zu verhindern | Stabil; weit verbreitet; guter Standard |
| **TRPO** | Methode der Vertrauensregion für Richtlinienaktualisierungen | Prinzipientreuer als PPO; schwieriger umzusetzen |
### Schauspieler-kritische Methoden
Kombinieren Sie das Beste aus beiden: einem **Akteur** (Richtlinie) und einem **Kritiker** (Wertfunktion).
| Algorithmus | Schlüsselidee |
|-----------|----------|
| **A2C / A3C** | Vorteil Schauspieler-Kritiker; nutzt die Vorteilsschätzung, um die Varianz zu reduzieren |
| **SAC** (Soft Actor-Critic) | Maximierung der Belohnung bei gleichzeitiger Aufrechterhaltung der Erkundung (Entropie-Regularisierung) |
| **TD3** (Twin Delayed DDPG) | Überschätzung in kontinuierlichen Handlungsräumen ansprechen |
---

## RLHF: Verstärkung des Lernens aus menschlichem Feedback
RLHF ist die Technik, die ChatGPT ermöglicht hat. Es schließt die Lücke zwischen einem Modell, das Text vorhersagen kann, und einem Modell, das Ergebnisse erzeugt, die für Menschen tatsächlich hilfreich sind.
### Die drei Schritte
| Schritt | Was passiert | Ausgabe |
|------|-------------|--------|
| **1. Überwachte Feinabstimmung (SFT)** | Feinabstimmung eines vorab trainierten Modells anhand hochwertiger, von Menschen geschriebener Beispiele | Ein Modell, das Anweisungen einigermaßen gut befolgt |
| **2. Schulung zum Belohnungsmodell** | Menschen vergleichen Paare von Modellausgaben; Ein Modell trainieren, um menschliche Vorlieben vorherzusagen | Ein Belohnungsmodell, das die Ausgabequalität bewertet |
| **3. RL-Optimierung** | Verwenden Sie PPO zur Feinabstimmung des SFT-Modells, um die Ergebnisse des Belohnungsmodells zu maximieren | Ein Modell, das auf menschliche Vorlieben ausgerichtet ist |
### Warum RLHF wichtig ist
Ohne RLHF ist ein Sprachmodell wie ein Student, der jedes Buch gelesen hat, aber nicht weiß, wie er sich in einer Konversation verhalten soll. Es kann Text generiert werden, aber der Text ist möglicherweise nicht hilfreich, giftig oder geht völlig am Kern der Sache vorbei. RLHF bringt dem Modell bei, *was Menschen wollen* – nicht nur, wie Text aussieht.
### Varianten und Alternativen
| Methode | Beschreibung | Vorteil |
|--------|-------------|-----------|
| **DPO** (Direct Preference Optimization) | Überspringen Sie das Belohnungsmodell. Richtlinien direkt anhand menschlicher Präferenzen optimieren | Einfacher; kein separates Belohnungsmodell zum Trainieren |
| **RLAIF** | Verwenden Sie KI (anstelle von Menschen), um Präferenzetiketten zu generieren | Günstiger als menschliche Etikettierung |
| **Verfassungsmäßige KI** | Verwenden Sie eine Reihe von Prinzipien, um das Modellverhalten ohne menschliche Etiketten zu leiten | Skalierbarer; Anthropics Ansatz |
| **GRPO** (Group Relative Policy Optimization) | Vergleichen Sie die Ausgaben innerhalb einer Gruppe statt mit einem separaten Modell | Wird in DeepSeek-R1 verwendet; reduziert den Bedarf an Wertschöpfungsnetzwerken |
---

## Erkundung vs. Ausbeutung
Dies ist die zentrale Spannung in RL. **Ausbeutung** bedeutet, Aktionen zu wählen, von denen Sie wissen, dass sie gut funktionieren. **Exploration** bedeutet, neue Dinge auszuprobieren, um potenziell bessere Strategien zu entdecken.
| Strategie | Wie es funktioniert | Kompromiss |
|----------|-------------|-----------|
| **ε-gierig** | Wählen Sie meistens die beste Aktion. zufällige Aktion mit Wahrscheinlichkeit ε | Einfach, aber ineffizient |
| **Boltzmann-Erkundung** | Wählen Sie Aktionen probabilistisch basierend auf ihren geschätzten Werten aus | Glatter als ε-gierig |
| **UCB** (Obere Vertrauensgrenze) | Bevorzugen Sie Handlungen mit hoher Unsicherheit (Optimismus angesichts der Unsicherheit) | Gute theoretische Garantien |
| **Entropie-Regularisierung** | Fügen Sie einen Bonus für den Besuch verschiedener Staaten hinzu (verwendet in SAC, PPO) | Fördert die Erkundung der Natur |
---

## Multi-Agent-Verstärkungslernen
Wenn mehrere Agenten gleichzeitig lernen, wird die Dynamik weitaus komplexer.
| Szenario | Herausforderung | Beispiel |
|----------|-----------|---------|
| **Genossenschaft** | Agenten müssen sich koordinieren; Kreditvergabe ist schwierig | Roboterfußballmannschaften; verteilte Sensornetzwerke |
| **Wettbewerbsfähig** | Gegner passen sich an; die Umgebung ist instationär | Spiel-KI (Poker, StarCraft); Cybersicherheit |
| **Gemischt** | Einige Agenten kooperieren, andere konkurrieren | Auktionsmärkte; Verkehrssysteme |
| Algorithmus | Beschreibung |
|-----------|-------------|
| **MADDPG** | Multi-Agent-Version von DDPG; zentraler Kritiker, dezentrale Akteure |
| **MAPPO** | Multi-Agent-PPO; in der Praxis weit verbreitet |
| **Selbstspiel** | Agenten trainieren gegen Kopien ihrer selbst (AlphaGo, AlphaStar) |
---

## Sim-zu-Real-Übertragung
Das Training von Robotern in der realen Welt ist langsam und gefährlich. Stattdessen trainieren Agenten die Simulation und den Transfer in die Realität.
| Herausforderung | Lösung |
|-----------|----------|
| **Realitätslücke** (Simulation ≠ reale Welt) | Domänen-Randomisierung: Physikparameter während des Trainings variieren |
| **Beispielineffizienz** | Verwenden Sie modellbasiertes RL oder trainieren Sie große parallele Simulationen |
| **Safety** | Eingeschränkter RL: Unsichere Aktionen während des Trainings bestrafen |
| **Teilweise Beobachtbarkeit** | Trainieren Sie mit verrauschten Sensoren und verzögerten Beobachtungen |
Unternehmen wie Boston Dynamics und Tesla nutzen Simulationen in großem Umfang, aber die Lücke zwischen simulierter und physischer Leistung bleibt eine der größten Herausforderungen in diesem Bereich.
---

## Tools und Frameworks
| Werkzeug | Zweck | Am besten für |
|------|---------|----------|
| **Stable-Baselines3** | Saubere Python-Implementierungen von PPO, SAC, TD3, DQN | Lernen und Prototyping |
| **RLlib** | Skalierbare RL-Bibliothek basierend auf Ray | Groß angelegte verteilte Schulung |
| **CleanRL** | Einzeldatei-Implementierungen für die Forschung | Algorithmen gründlich verstehen |
| **Gymnasium (OpenAI)** | Standardisierte Umgebungsschnittstelle | RL-Probleme definieren |
| **Isaac Gym / Isaac Lab** | GPU-beschleunigte Physiksimulation | Robotik, Sim-to-Real |
| **TRL** (Transformer RL-Bibliothek) | RLHF, DPO, PPO für Sprachmodelle | LLMs ausrichten |
| **OpenRLHF** | Verteiltes RLHF-Framework | Große Modelle mit RLHF trainieren |
---

## Praktische Tipps
- **Beginnen Sie mit PPO.** Es ist der zuverlässigste Allzweckalgorithmus. Wenn Sie nicht sicher sind, was Sie verwenden sollen, ist PPO die Standardeinstellung.
- **Normalisieren Sie Ihre Belohnungen.** Die Belohnungsskalierung wirkt sich dramatisch auf die Trainingsstabilität aus.
- **Verwenden Sie vektorisierte Umgebungen.** Das parallele Ausführen vieler Umgebungen (z. B. 8–64) stabilisiert die Gradientenschätzungen und beschleunigt das Training enorm.
- **Belohnung und Entropie überwachen.** Wenn die Entropie auf Null sinkt, hat Ihr Agent die Erkundung beendet und steckt möglicherweise in einem lokalen Optimum fest.
- **Belohnungsgestaltung ist eine Kunst.** Die Gestaltung der richtigen Belohnungsfunktion ist oft der schwierigste Teil. Geringe Belohnungen (nur am Ende) machen das Lernen extrem langsam. Dichte, wohlgeformte Belohnungen leiten den Agenten, können jedoch zu unbeabsichtigtem Verhalten führen.
- **RLHF ist fragil.** Kleine Änderungen am Belohnungsmodell oder an PPO-Hyperparametern können zu großen Qualitätsverlusten führen. DPO ist eine stabilere Alternative, wenn Sie nicht die vollständige RLHF-Pipeline benötigen.
---

## Zusammenfassung
Unter Reinforcement Learning versteht man die Untersuchung, wie Agenten lernen, Entscheidungen durch Interaktion zu treffen. Es reicht von klassischen Algorithmen wie Q-Learning bis hin zu modernen Deep-RL-Methoden wie PPO und SAC und untermauert einige der wichtigsten jüngsten Fortschritte in der KI – vom Spielen bis zur Ausrichtung von Sprachmodellen. Die Kernherausforderung bleibt dieselbe: Wie lernt man optimales Verhalten, wenn das Feedback verzögert, spärlich und laut ist? Die Antwort – Versuch und Irrtum, geleitet von cleverer Mathematik – erweist sich als eine der mächtigsten Ideen in der gesamten künstlichen Intelligenz.