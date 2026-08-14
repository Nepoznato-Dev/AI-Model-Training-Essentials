<!--
---
# Metadata
title: "Data Science and Analytics"
description: "Data processing, ML, big data, BI"
category: "Data Science and Analytics"
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
reviewed_by: "Data Science & Analytics Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [data, science, analytics, data-science-and-analytics]
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

-->
# Datenwissenschaft und Analytik
Data Science ist die Disziplin, Rohdaten in umsetzbare Erkenntnisse umzuwandeln. Es befindet sich an der Schnittstelle von Statistik, Informatik und Fachwissen – und ist in allen Sektoren, vom Finanzwesen bis zum Gesundheitswesen, unverzichtbar geworden. In dieser Datei werden die wichtigsten Konzepte, Tools und Arbeitsabläufe erläutert, die jeder Praktiker kennen sollte.
---

## Der Data-Science-Prozess
Die meisten Projekte folgen einer Variation von **CRISP-DM**, dem branchenüblichen Lebenszyklus:
| Phase | Was passiert | Typische Zeit |
|-------|-------------|--------------|
| **Geschäftsverständnis** | Definieren Sie Ziele, Erfolgskennzahlen und Einschränkungen | 10–15 % |
| **Datenverständnis** | Sammeln, erkunden und profilieren Sie die Daten | 10–15 % |
| **Datenvorbereitung** | Funktionen bereinigen, transformieren, entwickeln | ~50–60 % |
| **Modellieren** | Modelle auswählen und trainieren | 10–15 % |
| **Bewertung** | Bewerten Sie die Leistung anhand der Geschäftsziele | 5–10 % |
| **Bereitstellung** | Das Modell an die Produktion senden | 5–10 % |
Die Datenvorbereitung, insbesondere die Datenbereinigung, nimmt nach weit verbreiteten Schätzungen etwa 80 % der Zeit eines Data Scientists in Anspruch.
---

## Datentypen auf einen Blick
| Geben Sie | ein Beschreibung | Beispiel |
|------|-------------|---------|
| **Strukturiert** | In Zeilen und Spalten organisiert | SQL-Tabellen, Tabellenkalkulationen |
| **Unstrukturiert** | Kein vordefiniertes Format | Text, Bilder, Audio, Video |
| **Halbstrukturiert** | Etwas organisiert, aber flexibel | JSON, XML, HTML |
| **Zeitreihe** | Sequentielle Daten, nach Zeit indiziert | Aktienkurse, Sensorwerte |
| **Räumlich** | Geografisch oder standortbezogen | GPS-Koordinaten, Kartendaten |
| **Grafik** | Knoten und Kanten, die Beziehungen darstellen | Soziale Netzwerke, Wissensgraphen |
---

## Statistikgrundlagen
### Beschreibende vs. inferenzielle Statistik
Beschreibende Statistiken fassen zusammen, was Sie *haben*; Mithilfe von Inferenzstatistiken können Sie Rückschlüsse auf das ziehen, was Sie *nicht* haben (die breitere Bevölkerung).
| Konzept | Schlüsselideen |
|---------|-----------|
| **Zentrale Tendenz** | Mittelwert (empfindlich gegenüber Ausreißern), Median (robust), Modus (am häufigsten) |
| **Dispersion** | Bereich, Varianz, Standardabweichung, Interquartilbereich |
| **Verteilungsform** | Schiefe (Asymmetrie), Kurtosis (Schwanzschwere) |
| **Hypothesentest** | Null- vs. Alternativhypothese, p-Werte, Signifikanzniveau (α) |
| **Konfidenzintervalle** | Bereich, der wahrscheinlich den wahren Populationsparameter | enthält
| **Fehler vom Typ I/Typ II** | Falsch positiv (Ablehnung einer echten Null) / falsch negativ (ein echter Effekt fehlt) |
### Allgemeine statistische Tests
| Testen | Wann zu verwenden |
|------|-------------|
| **t-Test** | Mittelwerte zwischen zwei Gruppen vergleichen |
| **ANOVA** | Mittelwerte über drei oder mehr Gruppen vergleichen |
| **Chi-Quadrat** | Testen Sie die Unabhängigkeit kategorialer Variablen |
| **Mann-Whitney U** | Nichtparametrische Alternative zum t-Test (keine Normalitätsannahme) |
| **Pearson-Korrelation** | Lineare Beziehung zwischen zwei kontinuierlichen Variablen |
| **Spearman-Korrelation** | Monotone Beziehung (rangbasiert, robuster) |
### Wissenswerte Wahrscheinlichkeitsverteilungen
| Vertrieb | Anwendungsfall |
|-------------|----------|
| **Normal** | Naturphänomene, Messfehler – die klassische Glockenkurve |
| **Binomial** | Erfolgs-/Misserfolgszählungen (Münzwürfe, Umrechnungskurse) |
| **Poisson** | Ereigniszählungen in einem festen Intervall (Anrufe pro Stunde, Mängel pro Charge) |
| **Exponentiell** | Zeit zwischen Ereignissen (Wartezeiten, Fehlerintervalle) |
| **t-Verteilung** | Kleine Stichproben oder unbekannte Populationsvarianz |
| **Chi-Quadrat** | Kategoriale Datenanalyse, Anpassungstests |
---

## Datenerfassung und -speicherung
### Woher die Daten kommen
Reale Daten kommen aus vielen Quellen: relationale Datenbanken, APIs (REST, GraphQL), Flatfiles (CSV, JSON, Parquet), Streaming-Plattformen (Kafka, Kinesis), Umfragen und öffentliche Repositories (Kaggle, Regierungsportale). Das Format, das Sie erhalten, bestimmt einen Großteil Ihrer Vorverarbeitungsstrategie.
### Data Warehousing-Konzepte
| Konzept | Beschreibung |
|---------|-------------|
| **ETL** | Extrahieren → Transformieren → Laden – traditioneller Pipeline-Ansatz |
| **ELT** | Extrahieren → Laden → Transformieren – moderner Cloud-Ansatz (Rohdaten laden, im Lager transformieren) |
| **Data Lake** | Rohdaten im nativen Format gespeichert (Schema-on-Read) |
| **Data Warehouse** | Strukturierte, verarbeitete Daten optimiert für die Analyse (Schema-on-Write) |
| **Data Mart** | Eine Teilmenge eines Lagers, die auf eine Abteilung oder Domäne beschränkt ist |
| **Sternschema** | Zentrale Faktentabelle umgeben von Dimensionstabellen |
| **Schneeflockenschema** | Normalisierte Dimensionstabellen (weniger Redundanz, mehr Verknüpfungen) |
### Datenbanktypen
| Geben Sie | ein Beispiele | Am besten für |
|------|----------|----------|
| **Relational (SQL)** | PostgreSQL, MySQL, Oracle | Strukturierte Daten, ACID-Transaktionen |
| **Dokument** | MongoDB, CouchDB | Flexible Schemata, JSON-ähnliche Daten |
| **Schlüsselwert** | Redis, DynamoDB | Caching, Sitzungen, einfache Suchvorgänge |
| **Spaltenfamilie** | Cassandra, HBase | Schreibintensive Arbeitslasten, Zeitreihen |
| **Grafik** | Neo4j, Amazon Neptun | Beziehungen, soziale Netzwerke |
| **Zeitreihe** | InfluxDB, TimescaleDB | IoT-Metriken, Überwachung |
| **Vektor** | Tannenzapfen, Milvus | Einbetten von Speicher für die ML/KI-Suche |
---

## Datenvorverarbeitung und Feature Engineering
### Reinigungscheckliste
Jeder reale Datensatz hat Probleme. Hier ist die Standardbereinigung:
| Problem | Ansatz |
|-------|----------|
| **Fehlende Werte** | Imputation (Mittelwert, Median, Vorhersage) oder Löschung, wenn spärlich |
| **Ausreißer** | Erkennung über IQR oder Z-Score; mit Kappung oder Transformation behandeln |
| **Duplikate** | Identifizieren und entfernen |
| **Inkonsistenzen** | Formate standardisieren, Tippfehler korrigieren, Einheiten normalisieren |
### Transformationstechniken
| Technik | Was es tut |
|-----------|-------------|
| **Normalisierung** | Skaliert Werte auf einen Bereich von 0–1 |
| **Standardisierung** | Z-Score: Mittelwert = 0, Standard = 1 |
| **One-Hot-Kodierung** | Konvertiert Kategorien in Binärspalten |
| **Label-Kodierung** | Weist Kategorien Ganzzahlbezeichnungen zu |
| **Protokolltransformation** | Reduziert den Rechtsversatz in Daten |
| **Binning** | Gruppiert kontinuierliche Werte in diskrete Buckets |
### Feature-Engineering
Feature Engineering macht oft den Unterschied zwischen einem mittelmäßigen und einem großartigen Modell aus. Zu den wichtigsten Techniken gehören:
- **Funktionserstellung**: Ableitung neuer Spalten aus vorhandenen (z. B.`age_group`von`age`).
- **Funktionsauswahl**: Filtermethoden (Korrelation), Wrapper-Methoden (rekursive Eliminierung), eingebettete Methoden (LASSO, Baumwichtigkeit).
- **Dimensionalitätsreduzierung**: PCA für lineare, t-SNE oder UMAP für die Visualisierung.
- **Interaktionsterme**: Multiplikatives Kombinieren von Features, um gemeinsame Effekte zu erfassen.
---

## Explorative Datenanalyse (EDA)
Bei EDA entwickeln Sie vor der Modellierung ein Gespür für Ihre Daten. Ziel ist es, Muster, Anomalien und Zusammenhänge zu erkennen.
### Das richtige Diagramm auswählen
| Diagrammtyp | Am besten für |
|-----------|----------|
| **Histogramm** | Verteilung einer einzelnen Variablen |
| **Boxplot** | Fünf-Zahlen-Zusammenfassung, Ausreißererkennung |
| **Streudiagramm** | Beziehung zwischen zwei kontinuierlichen Variablen |
| **Heatmap** | Korrelationsmatrizen, Dichtevisualisierung |
| **Balkendiagramm** | Kategorien vergleichen |
| **Liniendiagramm** | Trends im Laufe der Zeit |
| **Geigenhandlung** | Verteilungsdichte + Boxplot-Zusammenfassung |
| **Paarplot** | Schneller Überblick über alle Variablenpaare |
### Der Python-EDA-Stack
| Bibliothek | Rolle |
|---------|------|
| **Pandas** | Datenmanipulation und -analyse |
| **numpy** | Numerisches Rechnen |
| **matplotlib** | Fundamentplanung |
| **seegeboren** | Statistische Visualisierung (basiert auf Matplotlib) |
| **plotierend** | Interaktive, webbasierte Visualisierungen |
| **scipy** | Wissenschaftliches Rechnen und Statistik |
---

## Maschinelles Lernen in der Datenwissenschaft
### Überwachtes Lernen auf einen Blick
| Aufgabe | Algorithmen |
|------|-----------|
| **Regression** (eine Zahl vorhersagen) | Linear, Ridge/LASSO, Entscheidungsbaum, Random Forest, Gradient Boosting (XGBoost, LightGBM) |
| **Klassifizierung** (eine Kategorie vorhersagen) | Logistische Regression, k-NN, Naive Bayes, SVM, Entscheidungsbäume, Random Forest, Neuronale Netze |
### Unüberwachtes Lernen auf einen Blick
| Aufgabe | Algorithmen |
|------|-----------|
| **Clustering** | k-Means, Hierarchisch, DBSCAN, Gaußsche Mischungsmodelle |
| **Dimensionalitätsreduzierung** | PCA, t-SNE, UMAP, Autoencoder |
| **Vereinsregeln** | Apriori, FP-Wachstum |
### Modellbewertung
| Metriktyp | Schlüsselkennzahlen |
|-------------|-------------|
| **Klassifizierung** | Genauigkeit, Präzision, Rückruf, F1-Score, ROC-AUC, Verwirrungsmatrix |
| **Regression** | MAE, MSE, RMSE, R², angepasstes R² |
| **Validierung** | k-fache Kreuzvalidierung, geschichtet, Zeitreihenaufteilung |
| **Tuning** | Rastersuche, Zufallssuche, Bayesianische Optimierung |
---

## Big-Data-Technologien
Wenn Datensätze die Kapazität einer einzelnen Maschine überschreiten, kommt verteiltes Rechnen ins Spiel.
| Rahmen | Stärke |
|-----------|----------|
| **Apache Spark** | In-Memory-Verarbeitung; Spark SQL, Streaming, MLlib, GraphX ​​|
| **Apache Hadoop** | MapReduce + HDFS – der ursprüngliche Big-Data-Stack |
| **Apache Flink** | Stream-Verarbeitung mit geringer Latenz |
| **Apache Beam** | Einheitliches Batch- und Streaming-Modell |
### Cloud-Datenplattformen
| Anbieter | Schlüsseldienste |
|----------|-------------|
| **AWS** | S3, EMR, Redshift, SageMaker, Glue |
| **Google Cloud** | BigQuery, Dataproc, KI-Plattform, Cloud-Speicher |
| **Azurblau** | Synapse Analytics, Databricks, maschinelles Lernen, Data Lake |
| **Schneeflocke** | Cloud-natives Data Warehouse (anbieterunabhängig) |
### Pipeline-Orchestrierung
| Werkzeug | Notizen |
|------|-------|
| **Apache Airflow** | Industriestandard; Python-basierte DAGs |
| **Präfekt** | Moderne Alternative mit sauberer API |
| **Dolch** | Assetzentrierte Orchestrierung |
| **dbt** | SQL-First-Datentransformation im Lager |
---

## Business Intelligence und Analytics
### BI-Tools im Vergleich
| Werkzeug | Geben Sie | ein Stärke |
|------|------|----------|
| **Tableau** | Kommerziell | Umfangreiche visuelle Analysen, Drag-and-Drop |
| **Power BI** | Kommerziell (Microsoft) | Deep Office/Azure-Integration |
| **Hingucker** | Kommerziell (Google) | Datenexploration, LookML-Modellierung |
| **Metabasis** | Open-Source | Einfache Einrichtung, SQL-nativ |
| **Obermenge** | Open-Source (Apache) | Skalierbar, SQL-first |
### Prinzipien des Dashboard-Designs
Gute Dashboards folgen einigen Regeln: Kennen Sie Ihre Zielgruppe, wählen Sie die richtige Visualisierung für jede Metrik, setzen Sie Farben strategisch (nicht dekorativ) ein, behalten Sie konsistente Skalen bei und ermöglichen Sie Interaktivität (Filter, Drilldowns). Auch die Leistung zählt – niemand wartet auf ein langsames Dashboard.
### Gemeinsame KPI-Kategorien
| Kategorie | Beispiele |
|----------|---------|
| **Finanzielle** | Umsatz, Gewinnspanne, ROI, Customer Lifetime Value |
| **Kunde** | Akquisitionskosten (CAC), Abwanderungsrate, NPS, Zufriedenheitswert |
| **Betriebsbereit** | Effizienzraten, Zykluszeit, Fehlerraten |
| **Marketing** | Conversion-Rate, Klickrate, ROAS, Attribution |
| **Produkt** | Täglich aktive Benutzer, Engagement, Bindung, Funktionsakzeptanz |
---

## Erweiterte Analysen
| Ansatz | Techniken | Wann zu verwenden |
|----------|-----------|-------------|
| **Vorausschauend** | Zeitreihen (ARIMA, Prophet, LSTM), Risikomodellierung, Abwanderungsvorhersage | Prognose zukünftiger Werte |
| **Vorschreibend** | Lineare Programmierung, Monte-Carlo-Simulation, A/B-Tests, mehrarmige Banditen | Entscheidungen optimieren |
| **Textanalyse** | Tokenisierung, Stimmungsanalyse, Themenmodellierung (LDA), NER, Worteinbettungen (Word2Vec, BERT) | Erkenntnisse aus Texten gewinnen |
---

## Datenethik und Governance
### Datenschutzbestimmungen
| Verordnung | Geltungsbereich |
|-----------|-------|
| **DSGVO** | EU-Datensubjekte; Recht auf Löschung, Einwilligung, Datenübertragbarkeit |
| **CCPA** | Verbraucher in Kalifornien; Opt-out vom Datenverkauf |
| **HIPAA** | US-Gesundheitsdaten; strenge Vertraulichkeitsregeln |
### Datenqualitätsdimensionen
| Dimension | Frage |
|-----------|----------|
| **Genauigkeit** | Sind die Daten korrekt? |
| **Vollständigkeit** | Fehlt etwas? |
| **Konsistenz** | Stimmen die Quellen überein? |
| **Aktualität** | Ist es aktuell? |
| **Gültigkeit** | Entspricht es den erwarteten Formaten? |
| **Einzigartigkeit** | Gibt es Duplikate? |
### Voreingenommenheit und Fairness
Verzerrungen können in jeder Phase auftreten: Stichprobenverzerrungen (nicht repräsentative Daten), Messverzerrungen (fehlerhafte Instrumente) oder algorithmische Verzerrungen (diskriminierende Vorhersagen). Zu den Abhilfestrategien gehören die Vorverarbeitung (Korrektur der Daten), die In-Verarbeitung (Einschränkung des Modells) und die Nachverarbeitung (Anpassung der Ergebnisse). Fairnessmetriken wie demografische Parität und Chancengleichheit helfen, das Problem zu quantifizieren.
---

## Karrierewege
| Rolle | Fokus |
|------|-------|
| **Datenanalyst** | Beschreibende Analysen, Dashboards, Reporting |
| **Datenwissenschaftler** | Statistische Modellierung, ML, erweiterte Analytik |
| **ML-Ingenieur** | Produktions-ML-Systeme, Modellbereitstellung, MLOps |
| **Dateningenieur** | Datenpipelines, Infrastruktur, ETL |
| **Analytics-Manager** | Teamführung, Strategie, Stakeholder-Management |
| **Forschungswissenschaftler** | Neuartige Algorithmen, Veröffentlichungen |
---

## Neue Trends
- **AutoML**: Automatisierte Pipeline-Erstellung und Modellauswahl.
- **MLOps**: DevOps-Praktiken, die auf das ML-Lebenszyklusmanagement angewendet werden.
- **Feature Stores**: Zentralisierte Feature-Verwaltung zur Wiederverwendung in allen Teams.
- **Data Mesh**: Dezentrale, domäneneigene Datenarchitektur.
- **LLMs und generative KI**: Große Sprachmodelle, die Text-, Code- und Bild-Workflows transformieren.
- **Edge Analytics**: Daten auf dem Gerät und nicht in der Cloud verarbeiten.
- **Kausale Schlussfolgerung**: Über die Korrelation hinausgehen, um tatsächliche Ursache und Wirkung zu verstehen.
- **Federated Learning**: Modelle über dezentrale Daten hinweg trainieren, ohne sie zu verschieben.
- **Verantwortungsvolle KI**: Ethik, Erklärbarkeit und Transparenz werden zu Standardanforderungen.