<!--
---
# Metadata
title: "Game Theory and Strategic Thinking"
description: "Nash equilibrium, prisoner's dilemma, mechanism design, auctions"
category: "Business and Economics"
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
reviewed_by: "Business & Economics Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [game, theory, business-and-economics]
difficulty_level: "beginner"
prerequisites: []
estimated_reading_time: "7 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Spieltheorie und strategisches Denken
Die Spieltheorie ist die mathematische Untersuchung strategischer Interaktionen – Situationen, in denen Ihr Ergebnis nicht nur davon abhängt, was Sie tun, sondern auch davon, was andere tun. Es gilt überall: geschäftlicher Wettbewerb, internationale Beziehungen, Auktionen, Verhandlungen, Evolutionsbiologie und alltägliche Entscheidungen wie die Wahl einer Route durch den Verkehr. Die Kernerkenntnis ist, dass rationale Akteure in strategischen Situationen nicht nur ihre eigene Strategie optimieren – sie antizipieren, was andere tun werden, und andere tun dasselbe.
---

## Grundlegende Konzepte
### Schlüsselterminologie
| Begriff | Definition |
|------|-----------|
| **Spiel** | Jede Situation mit zwei oder mehr Entscheidungsträgern (Spielern), deren Entscheidungen sich gegenseitig auf die Ergebnisse auswirken |
| **Spieler** | Ein Entscheider im Spiel |
| **Strategie** | Ein vollständiger Aktionsplan für jede Situation, die auftreten könnte |
| **Auszahlung** | Das Ergebnis, das ein Spieler aus einer bestimmten Kombination von Strategien erhält |
| **Nash-Gleichgewicht** | Eine Reihe von Strategien, bei denen kein Spieler seine Auszahlung durch einseitige Änderung seiner Strategie verbessern kann |
| **Dominante Strategie** | Eine Strategie, die unabhängig davon, was andere Spieler tun, am besten ist |
| **Nullsummenspiel** | Der Gewinn eines Spielers ist genau der Verlust eines anderen Spielers |
| **Nicht-Nullsummenspiel** | Spieler können potenziell alle gewinnen oder alle verlieren |
| **Kooperatives Spiel** | Spieler können verbindliche Vereinbarungen treffen |
| **Nicht-kooperatives Spiel** | Keine verbindlichen Vereinbarungen; jeder Spieler handelt im eigenen Interesse |
---

## Klassische Spiele
### Gefangenendilemma
Zwei Verdächtige werden festgenommen. Jeder kann kooperieren (schweigen) oder abtrünnig sein (gestehen).
| | B kooperiert | B Mängel |
|---|-------------|-----------|
| **A kooperiert** | A: 1 Jahr, B: 1 Jahr | A: 10 Jahre, B: kostenlos |
| **A-Mängel** | A: kostenlos, B: 10 Jahre | A: 5 Jahre, B: 5 Jahre |
| Einblick | Beschreibung |
|---------|-------------|
| **Dominante Strategie** | Der Defekt ist für beide Spieler dominant |
| **Nash-Gleichgewicht** | Beide defekt (jeweils 5 Jahre) |
| **Pareto-Optimum** | Beide kooperieren (jeweils 1 Jahr) |
| **Lektion** | Rationale individuelle Entscheidungen können zu insgesamt schlechteren Ergebnissen führen |
### Andere klassische Spiele
| Spiel | Beschreibung | Nash-Gleichgewicht | Lektion |
|------|-------------|-----------------|--------|
| **Huhn (Habichttaube)** | Zwei Fahrer fahren aufeinander zu; ausweichen oder geradeaus fahren | Einer weicht aus, einer geht geradeaus | Brinkmanship; Glaubwürdigkeit des Engagements |
| **Hirschjagd** | Gemeinsam einen Hirsch jagen (hohe Auszahlung) oder alleine einen Hasen jagen (niedrige Auszahlung) | Beide Hirsche oder beide Hasen | Koordinierung; Vertrauen |
| **Kampf der Geschlechter** | Zwei Spieler bevorzugen unterschiedliche Ergebnisse, möchten sich aber koordinieren | Beide gehen zur gleichen Veranstaltung | Mehrere Gleichgewichte; wer zuerst zieht, hat Vorteil |
| **Ultimatum-Spiel** | Der Antragsteller teilt das Geld auf; Antwortender akzeptiert oder lehnt ab (beide bekommen nichts) | Der Antragsteller bietet ein Minimum an; Antwortender akzeptiert | Menschen lehnen unfaire Angebote ab (irrational, aber häufig) |
| **Spiel mit öffentlichen Gütern** | Tragen Sie zu einem Gemeinschaftspool oder einer Freeride-Fahrt bei | Jeder fährt Trittbrett | Tragödie des Gemeinwesens; Notwendigkeit der Durchsetzung |
---

## Arten von Spielen
### Nach Timing
| Geben Sie | ein Beschreibung | Beispiel |
|------|-------------|---------|
| **Gleichzeitig** | Spieler bewegen sich gleichzeitig (oder ohne die Bewegungen anderer zu kennen) | Stein-Papier-Schere; Auktionen mit versiegelten Geboten |
| **Sequentiell** | Die Spieler bewegen sich nacheinander; spätere Spieler beobachten frühere Züge | Schach; Markteintrittsentscheidungen |
| **Wiederholt** | Dasselbe Spiel wurde mehrmals gespielt | Wiederholtes Gefangenendilemma; anhaltender geschäftlicher Wettbewerb |
### Nach Informationen
| Geben Sie | ein Beschreibung | Beispiel |
|------|-------------|---------|
| **Perfekte Informationen** | Alle Spieler kennen alle vorherigen Züge | Schach; Dame |
| **Unvollkommene Informationen** | Einige Bewegungen sind verborgen | Poker; Geschäftswettbewerb |
| **Vollständige Informationen** | Alle Spieler kennen alle Auszahlungen und Strategien | Die meisten Lehrbuchspiele |
| **Unvollständige Informationen** | Einige Auszahlungen oder Arten sind unbekannt | Auktionen; Verhandlungen |
---

## Lösungskonzepte
### Nash-Gleichgewicht
| Aspekt | Beschreibung |
|--------|-------------|
| **Definition** | Kein Spieler kann seine Auszahlung verbessern, indem er allein seine Strategie ändert |
| **So finden Sie** | Finden Sie für jeden Spieler die beste Reaktion auf die Strategien anderer. wo sie sich alle schneiden, ist das Nash-Gleichgewicht |
| **Existenz** | Jedes endliche Spiel hat mindestens ein Nash-Gleichgewicht (ggf. bei gemischten Strategien) |
| **Einzigartigkeit** | Spiele können mehrere Nash-Gleichgewichte haben; Koordinationsprobleme entstehen |
| **Einschränkung** | Das Nash-Gleichgewicht sagt Ihnen nicht, welches Gleichgewicht ausgewählt wird; berücksichtigt keine Gerechtigkeit |
### Dominantes Strategiegleichgewicht
| Schritt | Beschreibung |
|------|-------------|
| **1. Strategien identifizieren** | Listen Sie alle verfügbaren Strategien für jeden Spieler auf |
| **2. Finden Sie dominante Strategien** | Eine Strategie, die unabhängig davon, was andere tun, am besten ist |
| **3. Wenn alle Spieler eins haben** | Die Kombination ist das dominante Strategiegleichgewicht |
| **4. Wenn nicht** | Verwenden Sie die iterierte Eliminierung dominierter Strategien oder das Nash-Gleichgewicht |
### Rückwärtsinduktion (sequentielle Spiele)
| Schritt | Beschreibung |
|------|-------------|
| **1. Zeichne den Spielbaum** | Knoten = Entscheidungspunkte; Branches = Aktionen |
| **2. Beginnen Sie am Ende** | Identifizieren Sie die optimale Wahl des letzten Spielers an jedem Endknoten |
| **3. Rückwärts arbeiten** | Wählen Sie an jedem früheren Knoten die Aktion aus, die zum besten Ergebnis führt |
| **4. Ergebnis** | Perfektes Gleichgewicht des Teilspiels – optimale Strategie an jedem Entscheidungspunkt |
---

## Fortgeschrittene Konzepte
### Gemischte Strategien
| Konzept | Beschreibung | Beispiel |
|---------|-------------|---------|
| **Gemischte Strategie** | Randomisierung zwischen Aktionen nach Wahrscheinlichkeiten | Stein-Schere-Papier: jeweils mit 1/3 Wahrscheinlichkeit spielen |
| **Warum randomisieren?** | Verhindert, dass Gegner Ihren Zug vorhersagen | Elfmeterschießen im Fußball; Steuerprüfungen |
| **Gemischte Strategie Nash-Gleichgewicht** | Jeder Spieler ist zwischen seinen reinen Strategien gleichgültig | Kein Spieler kann den anderen ausnutzen |
### Wiederholte Spiele und Volkssatz
| Konzept | Beschreibung |
|---------|-------------|
| **Endlich wiederholt** | Rückwärtsinduktion entwirrt die Zusammenarbeit; dasselbe wie One-Shot-Spiel | Der Defekt in der letzten Runde breitet sich rückwärts aus |
| **Unendlich wiederholt** | Die Zusammenarbeit kann durch die Androhung künftiger Strafen aufrechterhalten werden | Wie du mir so ich dir; düstere Triggerstrategien |
| **Volkssatz** | Jede individuell rationale Auszahlung kann ein Nash-Gleichgewicht in einem unendlich wiederholten Spiel sein | Zusammenarbeit ist möglich, wenn die Zukunft wichtig genug ist |
| **Rabattfaktor** | Wie sehr schätzen Spieler zukünftige Auszahlungen? höher = mehr Zusammenarbeit | Geduldige Spieler kooperieren mehr |
### Mechanismusdesign (Umgekehrte Spieltheorie)
| Konzept | Beschreibung |
|---------|-------------|
| **Ziel** | Entwerfen Sie die Regeln eines Spiels, um ein gewünschtes Ergebnis zu erzielen |
| **Anwendungen** | Auktionen; Abstimmungssysteme; Vertragsgestaltung; Marktdesign |
| **Offenbarungsprinzip** | Jedes durch einen beliebigen Mechanismus erreichbare Ergebnis kann durch einen wahrheitsgetreuen direkten Mechanismus erreicht werden |
| **Beispiel** | Vickrey-Auktion (versiegeltes Gebot zum zweiten Preis) – Das Bieten auf Ihren wahren Wert ist eine vorherrschende Strategie |
---

## Anwendungen
### Geschäft
| Bewerbung | Spieltheorie-Konzept | Einblick |
|-------------|-----|---------|
| **Preiswettbewerb** | Gefangenendilemma | Preiskämpfe schadeten beiden Unternehmen; stillschweigende Absprache bei wiederholten Spielen |
| **Markteintritt** | Sequentielles Spiel; Engagement | Die Drohung des etablierten Betreibers, den Markteintritt zu bekämpfen, ist nur dann glaubwürdig, wenn er in Kapazitäten investiert hat |
| **Auktionen** | Mechanismusdesign | Zweitpreisauktionen bringen wahre Werte hervor; Frequenzauktionen bringen Milliarden ein |
| **Verhandlung** | Verhandlungsspiel; Nash-Gleichgewicht | Teilen Sie den Überschuss auf; First-Mover-Vorteil bei Ultimatum-Spielen |
| **Signalisierung** | Spences Bildungsmodell | Teure Signale sind glaubwürdig, weil sich minderwertige Typen sie nicht leisten können |
### Internationale Beziehungen
| Bewerbung | Spieltheorie-Konzept | Einblick |
|-------------|-----|---------|
| **Wettrüsten** | Gefangenendilemma | Beide Seiten wären besser dran, abzurüsten, aber sie können einander nicht vertrauen |
| **Handelskriege** | Wiederholtes Spiel | Tit-for-Tat: Kooperieren Sie, bis die anderen Mängel auftreten, und schlagen Sie dann zurück |
| **Klimaabkommen** | Spiel um öffentliche Güter | Trittbrettfahren ist rational; Durchsetzungsmechanismen erforderlich |
| **Abschreckung** | Huhn; glaubwürdiges Engagement | Gegenseitig zugesicherte Zerstörung ist ein Nash-Gleichgewicht |
---

## Zusammenfassung
Die Spieltheorie untersucht strategische Interaktionen, bei denen Ihr Ergebnis von den Aktionen anderer abhängt. Das Nash-Gleichgewicht – bei dem kein Spieler allein von einer Strategieänderung profitiert – ist das zentrale Lösungskonzept. Klassische Spiele wie das Gefangenendilemma zeigen, dass rationale Einzelentscheidungen zu kollektiv schlechten Ergebnissen führen können. Sequentielle Spiele werden durch Rückwärtsinduktion gelöst. Wiederholte Spiele können die Zusammenarbeit durch die Androhung künftiger Strafen aufrechterhalten. Gemischte Strategien erfordern eine Randomisierung, um unvorhersehbar zu bleiben. Das Mechanismusdesign kehrt die Frage um: Anstatt Ergebnisse vorherzusagen, entwirft es Regeln, um gewünschte Ergebnisse zu erzielen (wie bei Auktionen). Die Anwendungen umfassen Wirtschaft (Preise, Eintritt, Auktionen), Politik (Abstimmungen, Verträge), Biologie (evolutionäre stabile Strategien) und den Alltag. Die grundlegende Lektion ist, dass es bei der Strategie nicht nur darum geht, was man tut – es geht darum, vorherzusehen, was andere tun werden, in dem Wissen, dass sie dasselbe tun.