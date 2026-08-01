<!-- 
This file was automatically translated from English to German.
Source: database_systems.md
Note: Technical terms, code examples, and proper nouns may remain in English.
Für Verbesserungen der Genauigkeit bitten wir um Beiträge via Pull Requests.
-->

# Datenbanksysteme

## Datenbankgrundlagen

### Was ist eine Datenbank?
Eine Datenbank ist eine organisierte Sammlung strukturierter Informationen, die elektronisch gespeichert wird und für effizientes Abrufen, Einfügen, Aktualisieren und Löschen von Daten ausgelegt ist.

### Datenbankverwaltungssysteme (DBMS)
Software, die mit Endbenutzern, Anwendungen und der Datenbank selbst interagiert, um Daten zu erfassen und zu analysieren. Beispiele: MySQL, PostgreSQL, Oracle, MongoDB.

### Schlüsselkonzepte
- **Schema**: Struktur/Organisation der Datenbank (Tabellen, Felder, Beziehungen)
- **Instanz**: Tatsächliche Daten, die zu einem bestimmten Zeitpunkt gespeichert sind
- **ACID-Eigenschaften**: Atomarität, Konsistenz, Isolation, Dauerhaftigkeit
- **CAP-Theorem**: Konsistenz, Verfügbarkeit, Partitionstoleranz (wähle 2)
- **Normalisierung**: Organisieren von Daten zur Reduzierung von Redundanz
- **Denormalisierung**: Hinzufügen von Redundanz zur Verbesserung der Leseleistung

## Relationale Datenbanken (SQL)

### Kernkonzepte
- **Tabellen**: Zeilen (Datensätze) und Spalten (Felder)
- **Primärschlüssel**: Eindeutiger Identifikator für jede Zeile
- **Fremdschlüssel**: Verweis auf Primärschlüssel in einer anderen Tabelle
- **Indizes**: Datenstrukturen zur Verbesserung der Abfragegeschwindigkeit
- **Sichten**: Virtuelle Tabellen basierend auf Abfrageergebnissen
- **Gespeicherte Prozeduren**: Vorkompilierte SQL-Codeblöcke
- **Trigger**: Automatische Aktionen bei Datenänderungen

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
- **LEFT JOIN**: Alle Zeilen der linken Tabelle, Übereinstimmungen von der rechten
- **RIGHT JOIN**: Alle Zeilen der rechten Tabelle, Übereinstimmungen von der linken
- **FULL OUTER JOIN**: Alle Zeilen aus beiden Tabellen
- **CROSS JOIN**: Kartesisches Produkt beider Tabellen
- **SELF JOIN**: Tabelle wird mit sich selbst verknüpft

### Normalisierungsformen
- **1NF**: Atomare Werte, keine wiederholenden Gruppen
- **2NF**: 1NF + keine partiellen Abhängigkeiten (alle Nicht-Schlüssel-Attribute hängen vom gesamten Primärschlüssel ab)
- **3NF**: 2NF + keine transitiven Abhängigkeiten (Nicht-Schlüssel-Attribute hängen nicht von anderen Nicht-Schlüssel-Attributen ab)
- **BCNF**: Stärkere 3NF, jeder Determinant ist ein Kandidatenschlüssel
- **4NF**: Keine mehrwertigen Abhängigkeiten
- **5NF**: Keine Join-Abhängigkeiten

### Beliebte RDBMS
- **PostgreSQL**: Fortgeschrittene Funktionen, erweiterbar, ACID-konform
- **MySQL**: Weit verbreitet, schnelle Lesevorgänge, Webanwendungen
- **Oracle**: Enterprise-Funktionen, Skalierbarkeit, teuer
- **SQL Server**: Microsoft-Ökosystem, integrierte Tools
- **SQLite**: Eingebettet, serverlos, leichtgewichtig
- **MariaDB**: Quelloffene MySQL-Abspaltung

## NoSQL-Datenbanken

### Typen von NoSQL-Datenbanken

#### Dokumentenspeicher
- **Struktur**: JSON-ähnliche Dokumente (BSON)
- **Einsatzgebiete**: Content-Verwaltung, Kataloge, Benutzerprofile
- **Beispiele**: MongoDB, CouchDB, DocumentDB
- **Abfragebeispiel** (MongoDB):
```javascript
db.users.find({ age: { $gt: 25 } }).sort({ name: 1 });
```

#### Schlüssel-Wert-Speicher
- **Struktur**: Einfache Schlüssel-Wert-Paare
- **Einsatzgebiete**: Caching, Sitzungen, Einkaufswagen
- **Beispiele**: Redis, DynamoDB, Riak
- **Eigenschaften**: Schnell, einfach, begrenzte Abfragemöglichkeiten

#### Spaltenorientierte Speicher
- **Struktur**: Spalten gruppiert in Familien
- **Einsatzgebiete**: Big Data, Analysen, Zeitreihen
- **Beispiele**: Cassandra, HBase, ScyllaDB
- **Eigenschaften**: Schreiboptimiert, verteilt, skalierbar

#### Graphdatenbanken
- **Struktur**: Knoten, Kanten, Eigenschaften
- **Einsatzgebiete**: Soziale Netzwerke, Betrugserkennung, Empfehlungen
- **Beispiele**: Neo4j, Amazon Neptune, ArangoDB
- **Abfragesprache**: Cypher (Neo4j), Gremlin

### Wann NoSQL verwenden?
- Flexibles/sich entwickelndes Schema
- Anforderungen an horizontale Skalierung
- Hoher Schreibdurchsatz
- Hierarchische/genestete Daten
- Verteilte Systeme
- Echtzeitanwendungen

## Datenbankdesign

### Entitäts-Beziehungs-Modellierung
- **Entitäten**: Objekte/Konzepte (Kunde, Produkt, Bestellung)
- **Attribute**: Eigenschaften von Entitäten (Name, Preis, Datum)
- **Beziehungen**: Verbindungen zwischen Entitäten (eins-zu-eins, eins-zu-viele, viele-zu-viele)
- **Kardinalität**: Anzahl von Instanzen in einer Beziehung

### Schemadesign-Muster
- **Vererbung in einer Tabelle**: Alle Typen in einer Tabelle mit Typ-Diskriminator
- **Vererbung mit Klassentabellen**: Separate Tabellen für Basis- und Unterklassen
- **Vererbung mit konkreten Tabellen**: Separate Tabelle für jede konkrete Klasse
- **Verknüpfungstabellen**: Lösen von viele-zu-viele-Beziehungen
- **Audit-Tabellen**: Verfolgen von Änderungen (created_at, updated_at, deleted_at)

### Indexierungsstrategien
- **B-Baum**: Standardbereichsabfragen, Sortierung
- **Hash**: Exakte Übereinstimmungssuchen
- **Bitmap**: Spalten mit geringer Kardinalität (Geschlecht, Status)
- **Volltext**: Textsuchfunktionen
- **Räumlich**: Geografische Daten (GIS)
- **Zusammengesetzt**: Mehrere Spalten kombiniert
- **Abdeckend**: Enthält alle für die Abfrage benötigten Spalten

## Abfrageoptimierung

### Ausführungspläne
- Verstehen, wie die Datenbank Abfragen ausführt
- Engpässe identifizieren (vollständige Tabellenscans, fehlende Indizes)
- Tools: EXPLAIN, EXPLAIN ANALYZE

### Optimierungstechniken
- **Indexverwendung**: Sicherstellen, dass Abfragen geeignete Indizes verwenden
- **Abfrageumschreibung**: Komplexe Abfragen vereinfachen
- **Join-Optimierung**: Richtige Join-Typen und Reihenfolge wählen
- **Partitionierung**: Große Tabellen aufteilen (Bereich, Hash, Liste)
- **Materialisierte Sichten**: Vorberechnete Abfrageergebnisse
- **Abfrage-Caching**: Häufige Abfrageergebnisse speichern

### Häufige Leistungsprobleme
- **N+1-Abfrageproblem**: Ineffizientes Abrufen verknüpfter Daten
- **Fehlende Indizes**: Vollständige Tabellenscans bei großen Tabellen
- **Überindexierung**: Langsame Schreibvorgänge durch zu viele Indizes
- **Lock-Konflikte**: Transaktionen warten auf Sperren
- **Ineffiziente Abfragen**: SELECT *, unnötige Joins

## Transaktionen und Nebenläufigkeit

### Transaktions-Isolationsebenen
- **READ UNCOMMITTED**: Niedrigste Isolation, Dirty Reads möglich
- **READ COMMITTED**: Nur committete Daten sichtbar (Standard in den meisten DBs)
- **REPEATABLE READ**: Gleiche Abfrage liefert innerhalb der Transaktion gleiche Ergebnisse
- **SERIALIZABLE**: Höchste Isolation, Transaktionen werden sequenziell ausgeführt

### Nebenläufigkeitskontrolle
- **Pessimistisches Sperren**: Ressourcen vor dem Zugriff sperren
- **Optimistisches Sperren**: Version vor dem Commit prüfen
- **MVCC (Multi-Version Concurrency Control)**: Mehrere Versionen von Zeilen verwalten
- **Sperren auf Zeilenebene**: Bestimmte Zeilen sperren
- **Sperren auf Tabellenebene**: Gesamte Tabelle sperren

### Deadlocks
- Zirkuläre Abhängigkeit, bei der Transaktionen aufeinander warten
- Prävention: Konsistente Sperrreihenfolge, Timeouts, Deadlock-Erkennung
- Lösung: Eine Transaktion abbrechen

## Replikation und Skalierung

### Replikationstypen
- **Primär-Sekundär**: Ein primärer Knoten, mehrere Lesereplikate
- **Primär-Primär**: Mehrere primäre Knoten, bidirektionale Replikation
- **Multi-Primär**: N primäre Knoten, Konfliktlösung erforderlich
- **Kettenreplikation**: Sequenzielle Replikation durch Knoten

### Skalierungsansätze
- **Vertikale Skalierung**: Serverressourcen erhöhen (CPU, RAM, Speicher)
- **Horizontale Skalierung**: Weitere Server hinzufügen (Sharding, Partitionierung)
- **Lesereplikate**: Last von Lesevorgängen verteilen
- **Sharding**: Daten auf Server nach Schlüssel/Bereich/Hash verteilen
- **Föderation**: Aufteilung nach Funktion/Dienst

### Konsistenzmodelle
- **Starke Konsistenz**: Alle Knoten sehen gleiche Daten zur gleichen Zeit
- **Eventuelle Konsistenz**: Knoten konvergieren über die Zeit
- **Kausale Konsistenz**: Ursache-Wirkungs-Beziehungen erhalten
- **Eigene Schreibvorgänge direkt lesen**: Benutzer sieht eigene Updates sofort

## Backup und Wiederherstellung

### Backup-Strategien
- **Vollbackup**: Vollständige Datenbankkopie
- **Inkrementelles Backup**: Änderungen seit dem letzten Backup
- **Differenzielles Backup**: Änderungen seit dem letzten Vollbackup
- **Zeitpunktgenaue Wiederherstellung**: Wiederherstellung zu einem bestimmten Zeitpunkt
- **Kontinuierliches Backup**: Echtzeit-Replikation zum Backup

### Wiederherstellungsverfahren
- **RTO (Recovery Time Objective)**: Maximal akzeptable Ausfallzeit
- **RPO (Recovery Point Objective)**: Maximal akzeptabler Datenverlust
- **Disaster Recovery Plan**: Dokumentierte Verfahren für Ausfälle
- **Tests**: Regelmäßige Wiederherstellungsübungen

## Sicherheit

### Zugriffskontrolle
- **Authentifizierung**: Benutzeridentität überprüfen
- **Autorisierung**: Berechtigungen erteilen (GRANT, REVOKE)
- **Rollen**: Gruppenberechtigungen für einfachere Verwaltung
- **Prinzip der geringsten Rechte**: Minimal notwendiger Zugriff

### Datenschutz
- **Verschlüsselung im Ruhezustand**: Gespeicherte Daten verschlüsseln
- **Verschlüsselung während der Übertragung**: TLS/SSL für Verbindungen
- **Maskierung**: Sensible Daten in Nicht-Produktionsumgebungen verbergen
- **Tokenisierung**: Sensible Daten durch Tokens ersetzen

### Häufige Schwachstellen
- **SQL-Injection**: Bösartiges SQL in Benutzereingaben
- **Privilegienausweitung**: Unbefugter Zugriff erlangen
- **Audit-Logging**: Alle Datenbankaktivitäten protokollieren
- **Compliance**: GDPR, HIPAA, PCI-DSS Anforderungen

## Moderne Datenbanktechnologien

### Cloud-Datenbanken
- **AWS**: RDS, Aurora, DynamoDB, Redshift
- **Google Cloud**: Cloud SQL, Spanner, Bigtable, Firestore
- **Azure**: SQL Database, Cosmos DB, Synapse
- **Vorteile**: Verwalteter Dienst, automatische Skalierung, Backups inklusive

### NewSQL-Datenbanken
- Kombinieren SQL-Konsistenz mit NoSQL-Skalierbarkeit
- **Beispiele**: CockroachDB, TiDB, YugabyteDB, Google Spanner
- **Funktionen**: Verteilt, ACID-Transaktionen, horizontale Skalierung

### Zeitreihendatenbanken
- Optimiert für zeitgestempelte Daten
- **Beispiele**: InfluxDB, TimescaleDB, Prometheus
- **Einsatzgebiete**: IoT, Monitoring, Finanzdaten

### Vektordatenbanken
- Speichern und abfragen von Einbettungsvektoren
- **Beispiele**: Pinecone, Milvus, Weaviate, Qdrant
- **Einsatzgebiete**: Semantische Suche, Empfehlungssysteme, KI-Anwendungen

### Multimodelldatenbanken
- Unterstützen mehrere Datenmodelle in einem System
- **Beispiele**: ArangoDB, OrientDB, Azure Cosmos DB
- **Vorteil**: Flexibilität ohne mehrere Datenbanken

## ORMs und Datenzugriff

### Objektrelationale Abbildung
- **Zweck**: Datenbanktabellen auf Programmierobjekte abbilden
- **Beliebte ORMs**:
  - Python: SQLAlchemy, Django ORM, Peewee
  - JavaScript: Sequelize, Prisma, TypeORM
  - Java: Hibernate, JPA
  - Ruby: ActiveRecord
  - .NET: Entity Framework

### Vorteile
- Abstraktion von SQL
- Typsicherheit
- Migrationsverwaltung
- APIs zum Erstellen von Abfragen

### Nachteile
- Leistungsoverhead
- Komplexe Abfragen schwerer zu schreiben
- N+1-Abfrageprobleme
- Lernkurve

## Datenbankadministration

### DBA-Aufgaben
- Installation und Konfiguration
- Leistungsoptimierung
- Backup und Wiederherstellung
- Sicherheitsverwaltung
- Kapazitätsplanung
- Monitoring und Alarmierung
- Patch-Verwaltung

### Überwachungsmetriken
- Abfrageantwortzeit
- Durchsatz (Transaktionen pro Sekunde)
- Verbindungsanzahl
- Cache-Trefferquote
- Festplatten-E/A
- Sperrwartezeit
- Replikationsverzögerung

### Wartungsaufgaben
- **Vacuum/Analyze**: Statistiken aktualisieren und Speicher zurückgewinnen
- **Neuaufbau von Indizes**: Indizes defragmentieren
- **Aktualisierung von Statistiken**: Den Abfrageoptimierer auf dem neuesten Stand halten
- **Log-Rotation**: Die Größe von Log-Dateien verwalten
- **Kapazitätsplanung**: Wachstum vorhersagen, Upgrades planen
