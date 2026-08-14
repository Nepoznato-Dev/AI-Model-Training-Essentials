<!--
---
# Metadata
title: "Data Engineering and Pipelines"
description: "ETL/ELT, data lakes, orchestration, Kafka, feature stores"
category: "AI and Machine Learning"
subcategory: "ML Engineering"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "Nepoznato-Dev"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.1"
    date: "2026-08-09"
    author: "Nepoznato-Dev"
    changes: "Moved to engineering/ subfolder; added subcategory field"
  - version: "1.0.0"
    date: "2026-08-05"
    author: "Nepoznato-Dev"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-09"
review_date: "2027-02-05"
reviewed_by: "AI & Machine Learning Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [data, engineering, pipelines, ai-and-machine-learning]
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

-->
# Datentechnik und Pipelines
Data Engineering ist die Disziplin des Aufbaus von Systemen, die Daten in großem Maßstab bewegen, transformieren und speichern. Ohne zuverlässige Datenpipelines können Modelle für maschinelles Lernen nicht trainiert werden, Dashboards zeigen veraltete Zahlen an und Geschäftsentscheidungen basieren auf Vermutungen. Diese Datei behandelt die Architektur, Tools und Praktiken zum Aufbau einer funktionierenden Dateninfrastruktur.
---

## ETL vs. ELT
| Ansatz | Wie es funktioniert | Am besten für | Werkzeuge |
|----------|-------------|----------|-------|
| **ETL** (Extrahieren → Transformieren → Laden) | Daten *vor* dem Laden in das Lager transformieren | Traditionelle Lagerhäuser mit begrenzter Rechenleistung | Informatica, Talend, Apache NiFi |
| **ELT** (Extrahieren → Laden → Transformieren) | Laden Sie zuerst die Rohdaten. transformiere *im* Lagerhaus | Moderne Cloud-Warehouses mit elastischem Computing | dbt, Fivetran, Airbyte + BigQuery/Snowflake |
Der Übergang von ETL zu ELT wurde durch Cloud-Data-Warehouses (BigQuery, Snowflake, Redshift) vorangetrieben, die Rechenleistung unabhängig vom Speicher skalieren können. Es ist nicht mehr nötig, alles vor dem Laden vorzuverarbeiten.
---

## Data Lakes vs. Data Warehouses
| Funktion | Datensee | Data Warehouse |
|---------|-----------|---------------|
| **Datenformat** | Rohes, natives Format (Schema-on-Read) | Strukturiert, verarbeitet (Schema-on-Write) |
| **Schema** | Zum Zeitpunkt der Abfrage definiert | Vor dem Laden definiert |
| **Datentypen** | Strukturiert, halbstrukturiert, unstrukturiert | Hauptsächlich strukturiert |
| **Benutzer** | Datenwissenschaftler, Ingenieure | Business-Analysten, BI-Tools |
| **Kosten** | Günstigerer Speicher (Objektspeicher) | Teurer (für Abfragen optimiert) |
| **Beispiele** | AWS S3, Azure Data Lake, GCS | Schneeflocke, BigQuery, Redshift |
Der moderne Ansatz ist das **Lakehouse**: Kombinieren Sie die kostengünstige, flexible Lagerung eines Sees mit den Verwaltungs- und Leistungsmerkmalen eines Lagerhauses. Delta Lake, Apache Iceberg und Apache Hudi sind hier die Schlüsseltechnologien.
---

## Pipeline-Architektur
### Batch vs. Streaming
| Modus | Beschreibung | Latenz | Anwendungsfall |
|------|-------------|---------|----------|
| **Charge** | Verarbeiten Sie Daten in großen Blöcken in geplanten Intervallen | Minuten bis Stunden | Tägliche Berichte, ETL-Jobs, Datenanreicherung |
| **Streaming** | Daten kontinuierlich verarbeiten, sobald sie eintreffen | Millisekunden in Sekunden | Echtzeit-Dashboards, Betrugserkennung, Warnungen |
| **Mikrocharge** | Kleine Chargen in sehr kurzen Abständen | Sekunden | Nahezu in Echtzeit mit Batch-Einfachheit |
### Pipeline-Komponenten
Eine typische Datenpipeline besteht aus diesen Phasen:
| Bühne | Beschreibung | Werkzeuge |
|-------|-------------|-------|
| **Verschlucken** | Sammeln Sie Daten aus Quellen | Kafka, Airbyte, Fivetran, Debezium |
| **Transformation** | Reinigen, anreichern, aggregieren | dbt, Spark, Pandas |
| **Speicher** | Verarbeitete Daten beibehalten | BigQuery, Snowflake, S3, Delta Lake |
| **Servieren** | Daten für Verbraucher verfügbar machen | APIs, Dashboards, ML-Feature-Stores |
| **Orchestrierung** | Abhängigkeiten planen und verwalten | Luftstrom, Präfekt, Dagster |
| **Überwachung** | Verfolgen Sie den Zustand der Pipeline und die Datenqualität | Große Erwartungen, Monte Carlo, benutzerdefinierte Benachrichtigungen |
---

## Orchestrierungstools
| Werkzeug | Ansatz | Stärke |
|------|----------|----------|
| **Apache Airflow** | Python-basierte DAGs; Industriestandard | Riesiges Ökosystem, ausgereift, flexibel |
| **Präfekt** | Python-nativ; sauberere API als Airflow | Modernes Design, tolle Fehlerbehandlung |
| **Dolch** | Vermögensorientiert; Software-Engineering-Ansatz | Typsystem, Testen, Beobachtbarkeit |
| **Luigi** | Spotifys ursprüngliches Pipeline-Tool | Einfach, aber weniger aktiv entwickelt |
### Luftstrom-Beispiel
```python
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def extract():
    # Pull data from source
    pass

def transform():
    # Clean and process
    pass

def load():
    # Write to warehouse
    pass

with DAG("etl_pipeline", start_date=datetime(2024, 1, 1),
         schedule="@daily", catchup=False) as dag:
    e = PythonOperator(task_id="extract", python_callable=extract)
    t = PythonOperator(task_id="transform", python_callable=transform)
    l = PythonOperator(task_id="load", python_callable=load)
    
    e >> t >> l  # Define dependencies
```

---

## Apache Kafka
Kafka ist das Rückgrat vieler Echtzeit-Datensysteme. Es handelt sich um ein verteiltes Ereignisprotokoll, das fehlertolerante Nachrichten mit hohem Durchsatz bietet.
### Kernkonzepte
| Konzept | Beschreibung |
|---------|-------------|
| **Thema** | Eine Kategorie von Nachrichten (z. B.`orders`,`user-events`) |
| **Partition** | Themen werden aus Gründen der Parallelität in Partitionen aufgeteilt |
| **Produzent** | Anwendung, die Nachrichten zu Themen schreibt |
| **Verbraucher** | Anwendung, die Nachrichten aus Themen liest |
| **Verbrauchergruppe** | Gruppe von Verbrauchern, die sich die Last teilen, ein Thema zu lesen |
| **Versatz** | Position eines Verbrauchers innerhalb einer Partition |
| **Makler** | Ein Kafka-Serverknoten |
### Wann man Kafka verwendet
- **Event-Streaming**: Ereignisverarbeitung in Echtzeit im großen Maßstab.
- **Entkopplungsdienste**: Produzenten und Verbraucher müssen nichts voneinander wissen.
- **Wiedergabe**: Nachrichten bleiben erhalten; Verbraucher können von jedem Offset aus erneut lesen.
- **Gegendruck**: Kafka geht auf natürliche Weise mit Geschwindigkeitsunterschieden zwischen Produzenten und Konsumenten um.
---

## Datenmodellierung
### Sternschema vs. Schneeflockenschema
| Schema | Struktur | Vorteile | Nachteile |
|--------|-----------|------|------|
| **Stern** | Zentrale Faktentabelle umgeben von denormalisierten Dimensionstabellen | Einfache Abfragen, schnelles Lesen | Datenredundanz |
| **Schneeflocke** | Dimensionstabellen sind normalisiert (in Untertabellen aufgeteilt) | Weniger Redundanz | Mehr Verknüpfungen, langsamere Abfragen |
### Fakten- und Dimensionstabellen
| Tabellentyp | Enthält | Beispiel |
|-----------|----------|---------|
| **Tatsache** | Messbare Ereignisse (Metriken) | `orders`(Bestell-ID, Produkt-ID, Kunden-ID, Menge, Datum) |
| **Abmessung** | Beschreibende Attribute | `products`(Produkt-ID, Name, Kategorie, Preis),`customers`(Kunden-ID, Name, Stadt) |
---

## Feature-Stores
Ein Feature Store ist ein zentrales Repository für ML-Features – die abgeleiteten Werte, die als Eingabe für Modelle verwendet werden (z. B. „durchschnittlicher Bestellwert des Benutzers in den letzten 30 Tagen“).
| Fähigkeit | Beschreibung |
|-----------|-------------|
| **Feature-Registrierung** | Katalog der verfügbaren Funktionen mit Metadaten |
| **Offline-Shop** | Historische Funktionen für das Modelltraining (Batch) |
| **Online-Shop** | Funktion mit geringer Latenz für Echtzeit-Inferenz |
| **Funktionsüberwachung** | Drift, fehlende Werte, Verteilungsänderungen erkennen |
| Werkzeug | Beschreibung |
|------|-------------|
| **Fest** | Open Source; funktioniert mit jedem ML-Framework |
| **Tecton** | Kommerziell; Echtzeit-Feature-Plattform |
| **Hopfenwerke** | Open Source; Vollständige ML-Plattform mit Feature Store |
| **Databricks Feature Store** | Integriert in Databricks/Spark |
---

## Datenqualität
Datenqualität ist der stille Killer von ML-Projekten. Müll rein, Müll raus.
### Qualitätsdimensionen
| Dimension | Frage |
|-----------|----------|
| **Genauigkeit** | Entsprechen die Daten der Realität? |
| **Vollständigkeit** | Sind Pflichtfelder ausgefüllt? |
| **Konsistenz** | Stimmen die Werte über alle Quellen hinweg überein? |
| **Aktualität** | Sind die Daten aktuell? |
| **Gültigkeit** | Entsprechen Werte definierten Regeln? |
| **Einzigartigkeit** | Gibt es doppelte Datensätze? |
### Datenqualitätstools
| Werkzeug | Ansatz |
|------|----------|
| **Große Erwartungen** | Python-basiert; Definieren Sie „Erwartungen“ an Daten |
| **Monte Carlo** | ML-gestützte Datenbeobachtungsplattform |
| **DBT-Tests** | Integrierte Tests für Warehouse-Daten (einzigartig, nicht_null, Beziehungen) |
| **Soda** | Open-Source-Datenqualitätsscan |
---

## Daten-Governance
Data Governance stellt sicher, dass Daten im gesamten Unternehmen verantwortungsvoll verwaltet werden.
| Bereich | Beschreibung |
|------|-------------|
| **Datenkatalog** | Durchsuchbares Inventar von Datensätzen mit Metadaten (Amundsen, DataHub, Atlan) |
| **Datenherkunft** | Verfolgen Sie, woher die Daten kommen und wie sie sich verändern |
| **Zugriffskontrolle** | Rollenbasierte Berechtigungen; Wer kann was lesen/schreiben |
| **Compliance** | Einhaltung von DSGVO, CCPA, HIPAA |
| **Dateneigentum** | Klare Eigentümerschaft für jeden Datensatz (Verwaltung) |
| **Aufbewahrungsrichtlinien** | Legen Sie fest, wie lange Daten aufbewahrt werden und wann sie gelöscht werden |
---

## Der moderne Datenstapel
Der „moderne Datenstapel“ bezieht sich auf die typische Kombination von Tools, die heute von Datenteams verwendet werden:
| Schicht | Typische Werkzeuge |
|-------|--------------|
| **Verschlucken** | Fivetran, Airbyte |
| **Lager** | Schneeflocke, BigQuery, Redshift |
| **Transformation** | dbt |
| **Orchestrierung** | Luftstrom, Präfekt, Dagster |
| **BI / Visualisierung** | Looker, Metabasis, Tableau |
| **Reverse ETL** | Volkszählung, Hightouch (Lagerdaten wieder mit Tools synchronisieren) |
| **Datenqualität** | Große Erwartungen, Monte Carlo |
Der Trend geht zu modularen Best-of-Breed-Tools, die durch offene Standards (SQL, DBT-Modelle, Airflow DAGs) verbunden sind, statt zu monolithischen Plattformen.