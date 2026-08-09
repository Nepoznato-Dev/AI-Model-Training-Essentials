---
# Metadata
title: "Database Systems"
description: "SQL, NoSQL, design patterns, optimization"
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
tags: [database, systems, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "13 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Datenbanksysteme
## Datenbankgrundlagen
### Was ist eine Datenbank?
Eine Datenbank ist eine organisierte Sammlung strukturierter Informationen, die elektronisch gespeichert werden und für das effiziente Abrufen, Einfügen, Aktualisieren und Löschen von Daten konzipiert sind.
### Datenbankverwaltungssysteme (DBMS)
Software, die mit Endbenutzern, Anwendungen und der Datenbank selbst interagiert, um Daten zu erfassen und zu analysieren. Beispiele: MySQL, PostgreSQL, Oracle, MongoDB.
### Schlüsselkonzepte
- **Schema**: Struktur/Organisation der Datenbank (Tabellen, Felder, Beziehungen)
- **Instanz**: Tatsächliche Daten, die zu einem bestimmten Zeitpunkt gespeichert wurden
- **SÄURE-Eigenschaften**: Atomarität, Konsistenz, Isolierung, Haltbarkeit
- **CAP-Theorem**: Konsistenz, Verfügbarkeit, Partitionstoleranz (wählen Sie 2)
- **Normalisierung**: Daten organisieren, um Redundanz zu reduzieren
- **Denormalisierung**: Hinzufügen von Redundanz zur Verbesserung der Leseleistung
## Relationale Datenbanken (SQL)
### Kernkonzepte
- **Tabellen**: Zeilen (Datensätze) und Spalten (Felder)
- **Primärschlüssel**: Eindeutiger Bezeichner für jede Zeile
- **Fremdschlüssel**: Verweis auf Primärschlüssel in einer anderen Tabelle
- **Indizes**: Datenstrukturen verbessern die Abfragegeschwindigkeit
- **Ansichten**: Virtuelle Tabellen basierend auf Abfrageergebnissen
- **Gespeicherte Prozeduren**: Vorkompilierte SQL-Codeblöcke
- **Trigger**: Automatische Aktionen bei Datenänderungen
### SQL-Operationen (CRUD)```sql
-- Create
INSERT INTO users (name, email) VALUES ('Alice', 'alice@example.com');

-- Read
SELECT * FROM users WHERE id = 1;
SELECT name, email FROM users ORDER BY name LIMIT 10;

-- Update
UPDATE users SET email = 'new@example.com' WHERE id = 1;

-- Delete
DELETE FROM users WHERE id = 1;
```

### Tritt bei
- **INNER JOIN**: Gibt übereinstimmende Zeilen aus beiden Tabellen zurück
- **LEFT JOIN**: Alle Zeilen aus der linken Tabelle, Übereinstimmungen aus der rechten
- **RIGHT JOIN**: Alle Zeilen aus der rechten Tabelle, Übereinstimmungen aus der linken
- **FULL OUTER JOIN**: Alle Zeilen aus beiden Tabellen
- **CROSS JOIN**: Kartesisches Produkt beider Tabellen
- **SELF JOIN**: Tabelle mit sich selbst verbunden
### Normalisierungsformen
- **1NF**: Atomare Werte, keine sich wiederholenden Gruppen
- **2NF**: 1NF + keine Teilabhängigkeiten (alle Nichtschlüsselattribute hängen vom gesamten Primärschlüssel ab)
- **3NF**: 2NF + keine transitiven Abhängigkeiten (Nicht-Schlüsselattribute hängen nicht von anderen Nicht-Schlüsselattributen ab)
- **BCNF**: Stärkere 3NF, jede Determinante ist ein Kandidatenschlüssel
- **4NF**: Keine mehrwertigen Abhängigkeiten
- **5NF**: Keine Join-Abhängigkeiten
### Beliebtes RDBMS
- **PostgreSQL**: Erweiterte Funktionen, erweiterbar, ACID-kompatibel
- **MySQL**: Weit verbreitete, schnell lesbare Webanwendungen
- **Oracle**: Enterprise-Funktionen, Skalierbarkeit, teuer
- **SQL Server**: Microsoft-Ökosystem, integrierte Tools
- **SQLite**: Eingebettet, serverlos, leichtgewichtig
- **MariaDB**: MySQL-Fork, Open Source
## NoSQL-Datenbanken
### Arten von NoSQL-Datenbanken
#### Dokumentenspeicher
- **Struktur**: JSON-ähnliche Dokumente (BSON)
- **Anwendungsfälle**: Content-Management, Kataloge, Benutzerprofile
- **Beispiele**: MongoDB, CouchDB, DocumentDB
- **Abfragebeispiel** (MongoDB):```javascript
db.users.find({ age: { $gt: 25 } }).sort({ name: 1 });
```

#### Schlüsselwertspeicher
- **Struktur**: Einfache Schlüssel-Wert-Paare
- **Anwendungsfälle**: Caching, Sitzungen, Einkaufswagen
- **Beispiele**: Redis, DynamoDB, Riak
- **Eigenschaften**: Schnelle, einfache, eingeschränkte Abfrage
#### Column-Family Stores
- **Struktur**: In Familien gruppierte Spalten
- **Anwendungsfälle**: Big Data, Analysen, Zeitreihen
- **Beispiele**: Cassandra, HBase, ScyllaDB
- **Eigenschaften**: Schreiboptimiert, verteilt, skalierbar
#### Graphdatenbanken
- **Struktur**: Knoten, Kanten, Eigenschaften
- **Anwendungsfälle**: Soziale Netzwerke, Betrugserkennung, Empfehlungen
- **Beispiele**: Neo4j, Amazon Neptune, ArangoDB
- **Abfragesprache**: Cypher (Neo4j), Gremlin
### Wann NoSQL verwendet werden sollte
- Flexibles/sich weiterentwickelndes Schema
- Anforderungen an die horizontale Skalierung
- Hoher Schreibdurchsatz
- Hierarchische/verschachtelte Daten
- Verteilte Systeme
- Echtzeitanwendungen
## Datenbankdesign
### Entity-Relationship-Modellierung
- **Entitäten**: Objekte/Konzepte (Kunde, Produkt, Bestellung)
- **Attribute**: Eigenschaften von Entitäten (Name, Preis, Datum)
- **Beziehungen**: Verbindungen zwischen Entitäten (eins-zu-eins, eins-zu-viele, viele-zu-viele)
- **Kardinalität**: Anzahl der Instanzen in Beziehung
### Schema-Entwurfsmuster
- **Einzeltabellenvererbung**: Alle Typen in einer Tabelle mit Typdiskriminator
- **Vererbung von Klassentabellen**: Separate Tabellen für Basis- und Unterklassen
- **Konkrete Tabellenvererbung**: Separate Tabelle für jede konkrete Klasse
- **Verbindungstabellen**: Viele-zu-viele-Beziehungen auflösen
- **Audit-Tabellen**: Änderungen verfolgen (created_at, aktualisiert_at, gelöscht_at)
### Indexierungsstrategien
- **B-Tree**: Standard, Bereichsabfragen, Sortierung
- **Hash**: Suche nach exakten Übereinstimmungen
- **Bitmap**: Spalten mit niedriger Kardinalität (Geschlecht, Status)
- **Volltext**: Textsuchfunktionen
- **Räumlich**: Geografische Daten (GIS)
- **Zusammengesetzt**: Mehrere Spalten kombiniert
- **Abdeckend**: Enthält alle für die Abfrage erforderlichen Spalten
## Abfrageoptimierung
### Ausführungspläne
- Verstehen, wie die Datenbank Abfragen ausführt
- Identifizieren von Engpässen (vollständige Tabellenscans, fehlende Indizes)
- Werkzeuge: ERKLÄREN, ERKLÄREN, ANALYSE
### Optimierungstechniken
- **Indexverwendung**: Stellen Sie sicher, dass Abfragen geeignete Indizes verwenden
- **Umschreiben von Abfragen**: Vereinfachen Sie komplexe Abfragen
- **Join-Optimierung**: Wählen Sie die richtigen Join-Typen und die richtige Reihenfolge
- **Partitionierung**: Große Tabellen aufteilen (Bereich, Hash, Liste)
- **Materialisierte Ansichten**: Vorberechnete Abfrageergebnisse
- **Abfrage-Caching**: Speichern Sie häufige Abfrageergebnisse
### Häufige Leistungsprobleme
- **N+1-Abfrageproblem**: Zugehörige Daten werden ineffizient abgerufen
- **Fehlende Indizes**: Vollständige Tabellenscans für große Tabellen
- **Überindizierung**: Langsame Schreibvorgänge aufgrund zu vieler Indizes
- **Sperrkonflikt**: Transaktionen, die auf Sperren warten
- **Ineffiziente Abfragen**: SELECT *, unnötige Verknüpfungen
## Transaktionen und Parallelität
### Transaktionsisolationsstufen
- **READ UNCOMMITTED**: Geringste Isolation, Dirty Reads möglich
- **READ COMMITTED**: Nur festgeschriebene Daten sichtbar (Standard in den meisten DBs)
- **WIEDERHOLBARES LESEN**: Dieselbe Abfrage gibt innerhalb der Transaktion dieselben Ergebnisse zurück
- **SERIALISIERBAR**: Höchste Isolation, Transaktionen werden sequentiell ausgeführt
### Parallelitätskontrolle
- **Pessimistisches Sperren**: Ressourcen vor dem Zugriff sperren
- **Optimistisches Sperren**: Überprüfen Sie die Version vor dem Festschreiben
- **MVCC (Multi-Version Concurrency Control)**: Behalten Sie mehrere Versionen von Zeilen bei
- **Sperren auf Zeilenebene**: Bestimmte Zeilen sperren
- **Sperren auf Tabellenebene**: Gesamte Tabelle sperren
### Deadlocks
– Zirkuläre Abhängigkeit, bei der Transaktionen aufeinander warten
- Prävention: Konsistente Sperrreihenfolge, Zeitüberschreitungen, Deadlock-Erkennung
- Lösung: Eine Transaktion abbrechen
## Replikation und Skalierung
### Replikationstypen
- **Master-Slave**: Eine primäre, mehrere Lesereplikate
- **Master-Master**: Mehrere Primärserver, bidirektionale Replikation
- **Multi-Master**: N Vorwahlen, Konfliktlösung erforderlich
- **Kettenreplikation**: Sequentielle Replikation über Knoten
### Skalierungsansätze
- **Vertikale Skalierung**: Erhöhen Sie die Serverressourcen (CPU, RAM, Speicher)
- **Horizontale Skalierung**: Weitere Server hinzufügen (Sharding, Partitionierung)
- **Lesereplikate**: Leseverkehr auslagern
- **Sharding**: Daten nach Schlüssel/Bereich/Hash auf mehrere Server aufteilen
- **Föderation**: Aufteilung nach Funktion/Dienst
### Konsistenzmodelle
- **Starke Konsistenz**: Alle Knoten sehen gleichzeitig dieselben Daten
- **Endgültige Konsistenz**: Knoten konvergieren im Laufe der Zeit
- **Kausale Konsistenz**: Ursache-Wirkungs-Beziehungen bleiben erhalten
- **Read-Your-Writes**: Der Benutzer sieht seine eigenen Updates sofort
## Sicherung und Wiederherstellung
### Backup-Strategien
- **Vollständige Sicherung**: Vollständige Datenbankkopie
- **Inkrementelle Sicherung**: Änderungen seit der letzten Sicherung
- **Differenzielle Sicherung**: Änderungen seit der letzten vollständigen Sicherung
- **Point-in-Time Recovery**: Wiederherstellung zu einem bestimmten Zeitpunkt
- **Kontinuierliche Sicherung**: Echtzeitreplikation zur Sicherung
### Wiederherstellungsverfahren
- **RTO (Recovery Time Objective)**: Maximal akzeptable Ausfallzeit
- **RPO (Recovery Point Objective)**: Maximal akzeptabler Datenverlust
- **Disaster Recovery Plan**: Dokumentierte Verfahren für Ausfälle
- **Testen**: Regelmäßige Erholungsübungen
## Sicherheit
### Zugangskontrolle
- **Authentifizierung**: Benutzeridentität überprüfen
- **Autorisierung**: Berechtigungen erteilen (GRANT, REVOKE)
- **Rollen**: Gruppenberechtigungen zur einfacheren Verwaltung
- **Prinzip der geringsten Rechte**: Minimal erforderlicher Zugriff
### Datenschutz
- **Verschlüsselung im Ruhezustand**: Gespeicherte Daten verschlüsseln
- **Verschlüsselung bei der Übertragung**: TLS/SSL für Verbindungen
- **Maskierung**: Verstecken Sie vertrauliche Daten außerhalb der Produktion
- **Tokenisierung**: Ersetzen Sie sensible Daten durch Token
### Häufige Schwachstellen
- **SQL-Injection**: Schädliches SQL in Benutzereingaben
- **Privilegieneskalation**: Unbefugter Zugriff
- **Audit-Protokollierung**: Verfolgen Sie alle Datenbankaktivitäten
- **Compliance**: DSGVO-, HIPAA-, PCI-DSS-Anforderungen
## Moderne Datenbanktechnologien
### Cloud-Datenbanken
- **AWS**: RDS, Aurora, DynamoDB, Redshift
- **Google Cloud**: Cloud SQL, Spanner, Bigtable, Firestore
- **Azure**: SQL-Datenbank, Cosmos DB, Synapse
- **Vorteile**: Verwalteter Service, automatische Skalierung, Backups inklusive
### NewSQL-Datenbanken
- Kombinieren Sie SQL-Konsistenz mit NoSQL-Skalierbarkeit
- **Beispiele**: CockroachDB, TiDB, YugabyteDB, Google Spanner
- **Funktionen**: Verteilt, ACID-Transaktionen, horizontale Skalierung
### Zeitreihendatenbanken
- Optimiert für zeitgestempelte Daten
- **Beispiele**: InfluxDB, TimescaleDB, Prometheus
- **Anwendungsfälle**: IoT, Überwachung, Finanzdaten
### Vektordatenbanken
- Einbettungsvektoren speichern und abfragen
- **Beispiele**: Pinecone, Milvus, Weaviate, Qdrant
- **Anwendungsfälle**: Semantische Suche, Empfehlungssysteme, KI-Anwendungen
### Multi-Modell-Datenbanken
- Unterstützen Sie mehrere Datenmodelle in einem einzigen System
- **Beispiele**: ArangoDB, OrientDB, Azure Cosmos DB
- **Vorteil**: Flexibilität ohne mehrere Datenbanken
## ORMs und Datenzugriff
### Objektrelationale Zuordnung
- **Zweck**: Datenbanktabellen Programmierobjekten zuordnen
- **Beliebte ORMs**:
  - Python: SQLAlchemy, Django ORM, Peewee
  - JavaScript: Sequelize, Prisma, TypeORM
  - Java: Ruhezustand, JPA
  - Ruby: ActiveRecord
  - .NET: Entity Framework
### Vorteile
- Abstraktion von SQL
- Typensicherheit
- Migrationsmanagement
- APIs zum Erstellen von Abfragen
### Nachteile
- Leistungsaufwand
- Komplexe Abfragen sind schwerer zu schreiben
- N+1-Abfrageprobleme
- Lernkurve
## Datenbankverwaltung
### DBA-Aufgaben
- Installation und Konfiguration
- Leistungsoptimierung
- Sicherung und Wiederherstellung
- Sicherheitsmanagement
- Kapazitätsplanung
- Überwachung und Alarmierung
- Patch-Management
### Überwachungsmetriken
- Antwortzeit der Abfrage
- Durchsatz (Transaktionen pro Sekunde)
- Anzahl der Verbindungen
- Cache-Trefferquote
- Festplatten-E/A
- Wartezeit sperren
- Replikationsverzögerung
### Wartungsaufgaben
- **Vakuumieren/Analysieren**: Statistiken aktualisieren, Speicherplatz zurückgewinnen
- **Indexneuerstellung**: Indizes defragmentieren
- **Statistikaktualisierungen**: Halten Sie den Abfrageoptimierer auf dem Laufenden
- **Protokollrotation**: Protokolldateigrößen verwalten
- **Kapazitätsplanung**: Wachstum vorhersagen, Upgrades planen