# Datenbanksysteme

## Datenbankgrundlagen

### Was ist eine Datenbank?
Eine Datenbank ist eine organisierte Sammlung strukturierter Informationen, die elektronisch gespeichert wird und für effizientes Abrufen, Einfügen, Aktualisieren und Löschen von Daten ausgelegt ist.

### Datenbankmanagementsysteme (DBMS)
Software, die mit Endbenutzern, Anwendungen und der Datenbank selbst interagiert, um Daten zu erfassen und zu analysieren. Beispiele: MySQL, PostgreSQL, Oracle, MongoDB.

### Schlüsselkonzepte
- **Schema**: Struktur/Organisation der Datenbank (Tabellen, Felder, Beziehungen)
- **Instance**: Tatsächlich zu einem bestimmten Zeitpunkt gespeicherte Daten
- **ACID-Eigenschaften**: Atomicity, Consistency, Isolation, Durability
- **CAP-Theorem**: Consistency, Availability, Partition Tolerance (wähle 2)
- **Normalisierung**: Daten so organisieren, dass Redundanz reduziert wird
- **Denormalisierung**: Redundanz hinzufügen, um die Leseleistung zu verbessern

## Relationale Datenbanken (SQL)

### Kernkonzepte
- **Tables**: Zeilen (Datensätze) und Spalten (Felder)
- **Primary Key**: Eindeutiger Bezeichner für jede Zeile
- **Foreign Key**: Verweis auf den Primary Key in einer anderen Tabelle
- **Indexes**: Datenstrukturen zur Verbesserung der Abfragegeschwindigkeit
- **Views**: Virtuelle Tabellen auf Basis von Abfrageergebnissen
- **Stored Procedures**: Vorkompilierte SQL-Codeblöcke
- **Triggers**: Automatische Aktionen bei Datenänderungen

### SQL-Operationen (CRUD)
```sql
-- Erstellen
INSERT INTO users (name, email) VALUES ('Alice', 'alice@example.com');

-- Lesen
SELECT * FROM users WHERE id = 1;
SELECT name, email FROM users ORDER BY name LIMIT 10;

-- Aktualisieren
UPDATE users SET email = 'new@example.com' WHERE id = 1;

-- Löschen
DELETE FROM users WHERE id = 1;
```

### Joins
- **INNER JOIN**: Gibt übereinstimmende Zeilen aus beiden Tabellen zurück
- **LEFT JOIN**: Alle Zeilen aus der linken Tabelle, Übereinstimmungen von rechts
- **RIGHT JOIN**: Alle Zeilen aus der rechten Tabelle, Übereinstimmungen von links
- **FULL OUTER JOIN**: Alle Zeilen aus beiden Tabellen
- **CROSS JOIN**: Kartesisches Produkt beider Tabellen
- **SELF JOIN**: Tabelle mit sich selbst verknüpft

### Normalformen
- **1NF**: Atomare Werte, keine wiederholenden Gruppen
- **2NF**: 1NF + keine partiellen Abhängigkeiten (alle Nicht-Schlüsselattribute hängen vom gesamten Primary Key ab)
- **3NF**: 2NF + keine transitiven Abhängigkeiten (Nicht-Schlüsselattribute hängen nicht von anderen Nicht-Schlüsselattributen ab)
- **BCNF**: Strengere 3NF, jeder Determinant ist ein Candidate Key
- **4NF**: Keine mehrwertigen Abhängigkeiten
- **5NF**: Keine Join-Abhängigkeiten

### Beliebte RDBMS
- **PostgreSQL**: Erweiterte Funktionen, erweiterbar, ACID-konform
- **MySQL**: Weit verbreitet, schnelle Lesezugriffe, Webanwendungen
- **Oracle**: Unternehmensfunktionen, Skalierbarkeit, teuer
- **SQL Server**: Microsoft-Ökosystem, integrierte Werkzeuge
- **SQLite**: Eingebettet, serverlos, leichtgewichtig
- **MariaDB**: MySQL-Fork, Open Source

## NoSQL-Datenbanken

### Typen von NoSQL-Datenbanken

#### Document Stores
- **Struktur**: JSON-ähnliche Dokumente (BSON)
- **Anwendungsfälle**: Content-Management, Kataloge, Benutzerprofile
- **Beispiele**: MongoDB, CouchDB, DocumentDB
- **Abfragebeispiel** (MongoDB):
```javascript
db.users.find({ age: { $gt: 25 } }).sort({ name: 1 });
```

#### Key-Value Stores
- **Struktur**: Einfache Schlüssel-Wert-Paare
- **Anwendungsfälle**: Caching, Sessions, Warenkörbe
- **Beispiele**: Redis, DynamoDB, Riak
- **Eigenschaften**: Schnell, einfach, eingeschränkte Abfragen

#### Column-Family Stores
- **Struktur**: Spalten, die zu Familien gruppiert sind
- **Anwendungsfälle**: Big Data, Analytik, Zeitreihen
- **Beispiele**: Cassandra, HBase, ScyllaDB
- **Eigenschaften**: Für Schreibzugriffe optimiert, verteilt, skalierbar

#### Graph Databases
- **Struktur**: Knoten, Kanten, Eigenschaften
- **Anwendungsfälle**: Soziale Netzwerke, Betrugserkennung, Empfehlungen
- **Beispiele**: Neo4j, Amazon Neptune, ArangoDB
- **Abfragesprache**: Cypher (Neo4j), Gremlin

### Wann NoSQL verwenden?
- Flexibles/weiterentwickelbares Schema
- Anforderungen an horizontale Skalierung
- Hoher Schreibdurchsatz
- Hierarchische/verschachtelte Daten
- Verteilte Systeme
- Echtzeitanwendungen

## Datenbankdesign

### Entity-Relationship-Modellierung
- **Entities**: Objekte/Konzepte (Customer, Product, Order)
- **Attributes**: Eigenschaften von Entities (name, price, date)
- **Relationships**: Verbindungen zwischen Entities (one-to-one, one-to-many, many-to-many)
- **Cardinality**: Anzahl der Instanzen in einer Beziehung

### Muster für Schemas
- **Single Table Inheritance**: Alle Typen in einer Tabelle mit Typ-Diskriminator
- **Class Table Inheritance**: Separate Tabellen für Basisklasse und Unterklassen
- **Concrete Table Inheritance**: Separate Tabelle für jede konkrete Klasse
- **Junction Tables**: Lösen Many-to-Many-Beziehungen auf
- **Audit Tables**: Änderungen nachverfolgen (created_at, updated_at, deleted_at)

### Indexierungsstrategien
- **B-Tree**: Standard, Bereichsabfragen, Sortierung
- **Hash**: Exakte Treffer
- **Bitmap**: Spalten mit niedriger Kardinalität (gender, status)
- **Full-Text**: Textsuchfunktionen
- **Spatial**: Geografische Daten (GIS)
- **Composite**: Mehrere kombinierte Spalten
- **Covering**: Enthält alle für die Abfrage benötigten Spalten

## Abfrageoptimierung

### Ausführungspläne
- Verstehen, wie die Datenbank Abfragen ausführt
- Engpässe identifizieren (vollständige Tabellenscans, fehlende Indizes)
- Werkzeuge: EXPLAIN, EXPLAIN ANALYZE

### Optimierungstechniken
- **Index Usage**: Sicherstellen, dass Abfragen geeignete Indizes verwenden
- **Query Rewriting**: Komplexe Abfragen vereinfachen
- **Join Optimization**: Richtige Join-Typen und Reihenfolge wählen
- **Partitioning**: Große Tabellen aufteilen (range, hash, list)
- **Materialized Views**: Vorberechnete Abfrageergebnisse
- **Query Caching**: Häufige Abfrageergebnisse speichern

### Häufige Performance-Probleme
- **N+1 Query Problem**: Verwandte Daten ineffizient abrufen
- **Missing Indexes**: Vollständige Tabellenscans auf großen Tabellen
- **Over-indexing**: Langsame Schreibvorgänge durch zu viele Indizes
- **Lock Contention**: Transaktionen warten auf Sperren
- **Inefficient Queries**: SELECT *, unnötige Joins

## Transaktionen und Nebenläufigkeit

### Isolationsstufen von Transaktionen
- **READ UNCOMMITTED**: Niedrigste Isolation, Dirty Reads möglich
- **READ COMMITTED**: Nur bestätigte Daten sichtbar (Standard in den meisten DBs)
- **REPEATABLE READ**: Dieselbe Abfrage liefert innerhalb der Transaktion dieselben Ergebnisse
- **SERIALIZABLE**: Höchste Isolation, Transaktionen werden sequentiell ausgeführt

### Nebenläufigkeitskontrolle
- **Pessimistic Locking**: Ressourcen vor dem Zugriff sperren
- **Optimistic Locking**: Version vor dem Commit prüfen
- **MVCC (Multi-Version Concurrency Control)**: Mehrere Versionen von Zeilen verwalten
- **Row-Level Locking**: Bestimmte Zeilen sperren
- **Table-Level Locking**: Ganze Tabelle sperren

### Deadlocks
- Zirkuläre Abhängigkeit, bei der Transaktionen aufeinander warten
- Vermeidung: Konsistente Sperrreihenfolge, Timeouts, Deadlock-Erkennung
- Behebung: Eine Transaktion abbrechen

## Replikation und Skalierung

### Replikationstypen
- **Master-Slave**: Ein Primary, mehrere Read Replicas
- **Master-Master**: Mehrere Primaries, bidirektionale Replikation
- **Multi-Master**: N Primaries, Konfliktauflösung erforderlich
- **Chain Replication**: Sequenzielle Replikation über Knoten

### Skalierungsansätze
- **Vertikale Skalierung**: Serverressourcen erhöhen (CPU, RAM, Storage)
- **Horizontale Skalierung**: Mehr Server hinzufügen (Sharding, Partitionierung)
- **Read Replicas**: Leseverkehr auslagern
- **Sharding**: Daten nach Schlüssel/Bereich/Hash auf Server aufteilen
- **Federation**: Nach Funktion/Service aufteilen

### Konsistenzmodelle
- **Strong Consistency**: Alle Knoten sehen dieselben Daten zur selben Zeit
- **Eventual Consistency**: Knoten konvergieren mit der Zeit
- **Causal Consistency**: Ursache-Wirkungs-Beziehungen bleiben erhalten
- **Read-Your-Writes**: Benutzer sehen ihre eigenen Aktualisierungen sofort

## Backup und Wiederherstellung

### Backup-Strategien
- **Full Backup**: Vollständige Kopie der Datenbank
- **Incremental Backup**: Änderungen seit dem letzten Backup
- **Differential Backup**: Änderungen seit dem letzten Full Backup
- **Point-in-Time Recovery**: Wiederherstellung auf einen bestimmten Zeitpunkt
- **Continuous Backup**: Echtzeit-Replikation in ein Backup

### Wiederherstellungsverfahren
- **RTO (Recovery Time Objective)**: Maximal akzeptable Ausfallzeit
- **RPO (Recovery Point Objective)**: Maximal akzeptabler Datenverlust
- **Disaster Recovery Plan**: Dokumentierte Verfahren für Ausfälle
- **Testing**: Regelmäßige Wiederherstellungsübungen

## Sicherheit

### Zugriffskontrolle
- **Authentication**: Benutzeridentität verifizieren
- **Authorization**: Berechtigungen vergeben (GRANT, REVOKE)
- **Roles**: Berechtigungen für einfachere Verwaltung gruppieren
- **Principle of Least Privilege**: Minimal notwendiger Zugriff

### Datenschutz
- **Encryption at Rest**: Gespeicherte Daten verschlüsseln
- **Encryption in Transit**: TLS/SSL für Verbindungen
- **Masking**: Sensible Daten in Nicht-Produktionsumgebungen verbergen
- **Tokenization**: Sensible Daten durch Tokens ersetzen

### Häufige Schwachstellen
- **SQL Injection**: Bösartiges SQL in Benutzereingaben
- **Privilege Escalation**: Unbefugten Zugriff erlangen
- **Audit Logging**: Alle Datenbankaktivitäten nachverfolgen
- **Compliance**: Anforderungen von GDPR, HIPAA, PCI-DSS

## Moderne Datenbanktechnologien

### Cloud-Datenbanken
- **AWS**: RDS, Aurora, DynamoDB, Redshift
- **Google Cloud**: Cloud SQL, Spanner, Bigtable, Firestore
- **Azure**: SQL Database, Cosmos DB, Synapse
- **Vorteile**: Verwalteter Service, Auto-Scaling, Backups inklusive

### NewSQL-Datenbanken
- Kombinieren SQL-Konsistenz mit NoSQL-Skalierbarkeit
- **Beispiele**: CockroachDB, TiDB, YugabyteDB, Google Spanner
- **Merkmale**: Verteilt, ACID-Transaktionen, horizontale Skalierung

### Zeitreihendatenbanken
- Für Daten mit Zeitstempel optimiert
- **Beispiele**: InfluxDB, TimescaleDB, Prometheus
- **Anwendungsfälle**: IoT, Monitoring, Finanzdaten

### Vektor-Datenbanken
- Speichern und durchsuchen Embedding-Vektoren
- **Beispiele**: Pinecone, Milvus, Weaviate, Qdrant
- **Anwendungsfälle**: Semantische Suche, Empfehlungssysteme, AI-Anwendungen

### Multi-Model-Datenbanken
- Unterstützen mehrere Datenmodelle in einem einzigen System
- **Beispiele**: ArangoDB, OrientDB, Azure Cosmos DB
- **Vorteil**: Flexibilität ohne mehrere Datenbanken

## ORMs und Datenzugriff

### Objekt-relationale Abbildung
- **Zweck**: Datenbanktabellen auf Programmierobjekte abbilden
- **Beliebte ORMs**:
  - Python: SQLAlchemy, Django ORM, Peewee
  - JavaScript: Sequelize, Prisma, TypeORM
  - Java: Hibernate, JPA
  - Ruby: ActiveRecord
  - .NET: Entity Framework

### Vorteile
- Abstraktion von SQL
- Typensicherheit
- Migrationsverwaltung
- APIs zum Erstellen von Abfragen

### Nachteile
- Performance-Overhead
- Komplexe Abfragen schwerer zu schreiben
- N+1-Query-Probleme
- Lernkurve

## Datenbankadministration

### Verantwortlichkeiten eines DBA
- Installation und Konfiguration
- Performance-Tuning
- Backup und Wiederherstellung
- Sicherheitsmanagement
- Kapazitätsplanung
- Monitoring und Alarmierung
- Patch-Management

### Monitoring-Metriken
- Antwortzeit von Abfragen
- Durchsatz (Transaktionen pro Sekunde)
- Anzahl der Verbindungen
- Cache-Hit-Rate
- Disk I/O
- Wartezeit auf Sperren
- Replikationsverzögerung

### Wartungsaufgaben
- **Vacuum/Analyze**: Statistiken aktualisieren, Speicherplatz zurückgewinnen
- **Index Rebuilding**: Indizes defragmentieren
- **Statistics Updates**: Den Query Optimizer aktuell halten
- **Log Rotation**: Größe von Logdateien verwalten
- **Capacity Planning**: Wachstum prognostizieren, Upgrades planen
