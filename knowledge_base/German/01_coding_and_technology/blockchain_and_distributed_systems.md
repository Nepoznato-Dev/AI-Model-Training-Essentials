---
# Metadata
title: "Blockchain and Distributed Systems"
description: "Consensus, smart contracts, DeFi, Byzantine fault tolerance"
category: "Coding and Technology"
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
reviewed_by: "Coding & Technology Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [blockchain, distributed, systems, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "7 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Blockchain und verteilte Systeme
Blockchain ist eine spezielle Art von verteiltem System – ein dezentrales, nur anhängbares Hauptbuch, in dem Datensätze (Blöcke) durch kryptografische Hashes verknüpft sind. Verteilte Systeme sind das umfassendere Feld, bei dem mehrere Computer als ein einziger zusammenarbeiten. Beide Konzepte sind wichtig für das Verständnis moderner Infrastrukturen, von Kryptowährungen über verteilte Datenbanken bis hin zu Konsensalgorithmen, die globale Dienste unterstützen.
---

## Grundlagen verteilter Systeme
### Warum verteilte Systeme?
| Motivation | Beschreibung |
|-----------|-------------|
| **Skalierbarkeit** | Fügen Sie weitere Maschinen hinzu, um mehr Last zu bewältigen |
| **Fehlertoleranz** | Das System funktioniert auch dann weiter, wenn einige Maschinen ausfallen |
| **Geografische Verteilung** | Bedienen Sie Benutzer aus nahegelegenen Rechenzentren |
| **Spezialisierung** | Unterschiedliche Maschinen erledigen unterschiedliche Aufgaben |
### Schlüsselkonzepte
| Konzept | Beschreibung | Herausforderung |
|---------|-------------|-----------|
| **Konsens** | Alle Knoten dazu bringen, sich auf einen Wert zu einigen | Netzwerkpartitionen; Byzantinische Fehler |
| **Replikation** | Daten über mehrere Knoten hinweg kopieren | Konsistenz vs. Verfügbarkeit |
| **Partitionierung (Sharding)** | Daten auf Knoten aufteilen | Hotspots; Cross-Shard-Abfragen |
| **Konsistenzmodelle** | Garantien darüber, was verschiedene Leser sehen | Starke Konsistenz ist langsam; letztendliche Konsistenz kann Benutzer überraschen |
| **CAP-Theorem** | Sie können nur zwei der folgenden Optionen haben: Konsistenz, Verfügbarkeit, Partitionstoleranz | In der Praxis ist eine Partitionstoleranz erforderlich; Wählen Sie C oder A |
### Das CAP-Theorem
| Wahl | Was Sie bekommen | Was du aufgibst | Beispiel |
|--------|-------------|-----------------|---------|
| **CP** | Konsistent + partitionstolerant | Einige Knoten sind während der Partitionierung möglicherweise nicht verfügbar | HBase, MongoDB, Redis |
| **AP** | Verfügbar + partitionstolerant | Lesevorgänge können veraltete Daten zurückgeben | Cassandra, DynamoDB, CouchDB |
| **CA** | Konsistent + verfügbar | Netzwerkpartitionen werden nicht toleriert | Einzelknotendatenbanken (nicht wirklich verteilt) |
---

## Konsensalgorithmen
Wie einigen sich verteilte Knoten auf den Zustand des Systems?
| Algorithmus | Geben Sie | ein Fehlertoleranz | Verwendet in |
|-----------|------|----------------|---------|
| **Paxos** | Absturzfehlertolerant | Bis zu f Ausfälle mit 2f+1 Knoten | Google Mollig; grundlegende Theorie |
| **Floß** | Absturzfehlertolerant | Bis zu f Ausfälle mit 2f+1 Knoten | etcd, Konsul, TiKV |
| **PBFT** | Byzantinische Fehlertoleranz | Bis zu f Ausfälle mit 3f+1 Knoten | Hyperledger-Stoff |
| **Arbeitsnachweis** | Byzantinische Fehlertoleranz | Hängt von der Hash-Leistung ab | Bitcoin |
| **Einsatznachweis** | Byzantinische Fehlertoleranz | Abhängig vom Einsatz | Ethereum 2.0, Cardano |
### Floß (vereinfacht)
| Rolle | Verantwortung |
|------|---------------|
| **Anführer** | Behandelt alle Kundenanfragen; sendet Protokolleinträge an Follower |
| **Follower** | Reagiert auf Anfragen des Leiters; Stimmen bei Wahlen |
| **Kandidat** | Fordert Stimmen an, um Anführer zu werden |
1. Alle Knoten beginnen als Follower
2. Wenn ein Anhänger wegen einer Wahlauszeit nichts vom Anführer hört, wird er zum Kandidaten
3. Kandidaten beantragen Stimmen; Derjenige mit den meisten Stimmen wird Anführer
4. Der Leiter repliziert Protokolleinträge an die Follower
5. Wenn eine Mehrheit zustimmt, ist der Eintrag bestätigt
---

## Blockchain
### Wie eine Blockchain funktioniert
| Komponente | Beschreibung |
|-----------|-------------|
| **Blockieren** | Ein Stapel von Transaktionen + Metadaten + Hash des vorherigen Blocks |
| **Hash** | Kryptografischer Fingerabdruck des Blockinhalts |
| **Kette** | Jeder Block referenziert den Hash des vorherigen Blocks und erstellt so eine unveränderliche Kette |
| **Konsens** | Netzwerkteilnehmer einigen sich darauf, welche Blöcke hinzugefügt werden sollen |
| **Merkle-Baum** | Hash-Baum, der alle Transaktionen in einem Block zusammenfasst |
### Warum Blockchain schwer zu manipulieren ist
1. Jeder Block enthält den Hash des vorherigen Blocks
2. Das Ändern einer Transaktion ändert den Hash des Blocks
3. Der geänderte Hash unterbricht die Kette – alle nachfolgenden Blöcke werden ungültig
4. Ein Angreifer müsste alle nachfolgenden Blöcke erneut abbauen UND mehr als 50 % des Netzwerks kontrollieren
### Arten von Blockchains
| Geben Sie | ein Zugriff | Validator | Beispiel |
|------|--------|-----------|---------|
| **Öffentlich (ohne Erlaubnis)** | Jeder kann lesen und schreiben | Offener Konsens (PoW, PoS) | Bitcoin, Ethereum |
| **Privat (erlaubt)** | Eingeschränkter Zugriff | Bekannte Validatoren | Hyperledger, Corda |
| **Konsortium** | Geleitet von einer Gruppe von Organisationen | Ausgewählte Validatoren | R3 Corda für Banking |
### Intelligente Verträge
Selbstausführender Code, der in der Blockchain gespeichert ist und ausgeführt wird, wenn vorgegebene Bedingungen erfüllt sind.
| Plattform | Sprache | Bemerkenswerte Funktion |
|----------|----------|-----------------|
| **Ethereum** | Solidität, Vyper | Größtes Smart-Contract-Ökosystem |
| **Solana** | Rust, C | Hoher Durchsatz; niedrige Gebühren |
| **Cardano** | Haskell (Plutus) | Von Experten begutachtet; formelle Verifizierung |
| **Hyperledger** | Go, Java, JavaScript | Unternehmen; erlaubt |
---

## Kryptowährung
| Währung | Konsens | Versorgung | Hauptverwendung |
|----------|-----------|--------|-------------|
| **Bitcoin** | Arbeitsnachweis | 21 Millionen (gedeckelt) | Wertaufbewahrungsmittel; digitales Gold |
| **Ethereum** | Nachweis des Einsatzes | Keine feste Kappe | Intelligente Verträge; DeFi; NFTs |
| **Solana** | Nachweis des Einsatzes + Nachweis der Geschichte | Keine feste Kappe | Hochgeschwindigkeitstransaktionen |
| **Cardano** | Nachweis des Einsatzes (Ouroboros) | 45 Milliarden (gedeckelt) | Akademischer Ansatz; Nachhaltigkeit |
---

## Verteilte Datenbanken
| Datenbank | Architektur | Konsistenz | Am besten für |
|----------|-------------|-------------|----------|
| **Kassandra** | Breitspaltig; Peer-to-Peer | Einstellbar (eventuell auf Quorum) | Hoher Schreibdurchsatz; Zeitreihe |
| **MongoDB** | Dokumentieren; Replika-Sets | Eventuell (mit kausaler Konsistenzoption) | Flexibles Schema; rasante Entwicklung |
| **KakerlakeDB** | Verteiltes SQL; Floßkonsens | Stark | Verteiltes SQL; globale Bereitstellung |
| **TiDB** | Verteiltes SQL; Floß (über TiKV) | Stark | MySQL-kompatibel; horizontale Skalierung |
| **DynamoDB** | Schlüsselwert; verwaltet | Eventuell (oder stark mit konsistenten Lesevorgängen) | Serverlos; AWS-integriert |
| **Schraubenschlüssel** | Verteiltes SQL; Paxos | Stark | Google Cloud; globale Konsistenz |
---

## Verteilte Systemmuster
| Muster | Beschreibung | Anwendungsfall |
|---------|-------------|----------|
| **Anführerwahl** | Wählen Sie einen Knoten zum Koordinieren | aus Floßführer; ZooKeeper |
| **Replikation** | Daten für Redundanz und Leseskalierung kopieren | Datenbankrepliken; CDN |
| **Sharding** | Partitionieren Sie Daten nach Schlüsselbereich oder Hash | Große Datenbanken |
| **MapReduce** | Aufteilung der Berechnung auf mehrere Knoten; Gesamtergebnisse | Große Datenverarbeitung |
| **Klatschprotokoll** | Knoten teilen regelmäßig ihren Status mit zufälligen Peers | Clustermitgliedschaft; Fehlererkennung |
| **Zwei-Phasen-Commit** | Koordinieren Sie Transaktionen über mehrere Knoten hinweg | Verteilte Datenbanken |
| **Saga-Muster** | Reihe lokaler Transaktionen mit kompensierenden Aktionen | Microservice-Transaktionen |
| **Leistungsschalter** | Hören Sie auf, einen fehlerhaften Dienst anzurufen; schnell scheitern | Widerstandsfähigkeit; kaskadierende Ausfälle verhindern |
---

## Herausforderungen in verteilten Systemen
| Herausforderung | Beschreibung | Schadensbegrenzung |
|-----------|-------------|------------|
| **Netzwerkpartitionen** | Knoten können nicht kommunizieren | GAP-Kompromiss; Mit Backoff erneut versuchen |
| **Uhrzeitversatz** | Verschiedene Knoten haben unterschiedliche Uhren | Verwenden Sie logische Uhren. NTP; Vermeiden Sie es, sich auf die Zeit an der Wand zu verlassen |
| **Byzantinische Fehler** | Knoten, die liegen oder sich willkürlich verhalten | BFT-Konsens; Blockchain |
| **Gespaltenes Gehirn** | Zwei Knoten denken beide, dass sie der Anführer sind | Fechten; Entscheidungen auf Quorumsbasis |
| **Kaskadierende Fehler** | Ein Fehler löst weitere aus | Leistungsschalter; Schotte; anmutige Erniedrigung |
| **Datenkonsistenz** | Replikate synchron halten | Konsistenzmodelle; Konfliktlösung |
---

## Zusammenfassung
Mithilfe verteilter Systeme lässt sich moderne Software skalieren, Ausfälle überstehen und Benutzern weltweit dienen. Konsensalgorithmen (Raft, Paxos) stellen sicher, dass die Knoten übereinstimmen. Blockchains fügen kryptografische Verifizierung und Dezentralisierung hinzu, um vertrauenswürdige Hauptbücher zu erstellen. Verteilte Datenbanken (Cassandra, CockroachDB, DynamoDB) verarbeiten Daten im großen Maßstab. Der grundlegende Kompromiss – erfasst durch das CAP-Theorem – besteht zwischen Konsistenz und Verfügbarkeit, wenn das Netzwerk unzuverlässig ist. Das Verständnis dieser Konzepte ist für den Aufbau von Systemen, die im Internetmaßstab funktionieren, von entscheidender Bedeutung.