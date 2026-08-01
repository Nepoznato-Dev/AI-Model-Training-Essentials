<!-- 
This file was automatically translated from English to German.
Source: data_science_and_analytics.md
Note: Technical terms, code examples, and proper nouns may remain in English.
Für Verbesserungen der Genauigkeit bitten wir um Beiträge via Pull Requests.
-->

# Datenwissenschaft und Analytik

## Kernkonzepte

### Was ist Datenwissenschaft?
Datenwissenschaft ist ein interdisziplinäres Feld, das wissenschaftliche Methoden, Prozesse, Algorithmen und Systeme verwendet, um Wissen und Erkenntnisse aus strukturierten und unstrukturierten Daten zu extrahieren. Sie kombiniert:
- **Statistik**: Mathematische Grundlage für Analysen
- **Informatik**: Programmierung, Algorithmen, Datenstrukturen
- **Domänenexpertise**: Fachwissen
- **Datenvisualisierung**: Effektive Kommunikation von Erkenntnissen

### Datentypen
- **Strukturierte Daten**: Organisiert in Zeilen/Spalten (Datenbanken, Tabellenkalkulationen)
- **Unstrukturierte Daten**: Kein vordefiniertes Format (Text, Bilder, Audio, Video)
- **Semistrukturierte Daten**: Einige Organisation, aber nicht starr (JSON, XML, HTML)
- **Zeitreihendaten**: Sequenzielle Datenpunkte in zeitlicher Reihenfolge indiziert
- **Räumliche Daten**: Geografische/standortbasierte Informationen
- **Graphdaten**: Knoten und Kanten, die Beziehungen darstellen

### Der Datenwissenschaftsprozess (CRISP-DM)
1. **Geschäftsverständnis**: Ziele und Anforderungen definieren
2. **Datenverständnis**: Erste Daten sammeln und erkunden
3. **Datenvorbereitung**: Daten bereinigen, transformieren und formatieren (80% der Arbeit)
4. **Modellierung**: Modellierungstechniken auswählen und anwenden
5. **Evaluation**: Modellleistung anhand der Ziele bewerten
6. **Bereitstellung**: Modell in der Produktionsumgebung implementieren

## Statistikgrundlagen

### Deskriptive Statistik
- **Maße der zentralen Tendenz**: Mittelwert, Median, Modus
- **Streuungsmaße**: Spannweite, Varianz, Standardabweichung, Interquartilsabstand
- **Verteilungsform**: Schiefe (Asymmetrie), Kurtosis (Steilheit)
- **Perzentile und Quartile**: Position innerhalb der Verteilung

### Inferenzstatistik
- **Hypothesentests**: Nullhypothese, Alternativhypothese, p-Werte
- **Konfidenzintervalle**: Wertebereich, der wahrscheinlich den Populationsparameter enthält
- **Statistische Signifikanz**: Wahrscheinlichkeit, dass Ergebnisse zufällig aufgetreten sind
- **Fehler 1. Art**: Falsch positiv (Ablehnung einer wahren Nullhypothese)
- **Fehler 2. Art**: Falsch negativ (Nicht-Ablehnung einer falschen Nullhypothese)
- **Teststärke**: Wahrscheinlichkeit, eine falsche Nullhypothese korrekt abzulehnen

### Wahrscheinlichkeitsverteilungen
- **Normalverteilung**: Glockenkurve, Mittelwert = Median = Modus
- **Binomialverteilung**: Erfolg/Misserfolg-Ergebnisse
- **Poisson-Verteilung**: Anzahl von Ereignissen in festem Intervall
- **Gleichverteilung**: Alle Ergebnisse gleich wahrscheinlich
- **Exponentialverteilung**: Zeit zwischen Ereignissen
- **t-Verteilung**: Kleine Stichprobengrößen, unbekannte Populationsvarianz
- **Chi-Quadrat-Verteilung**: Analyse kategorialer Daten

### Statistische Tests
- **t-Test**: Vergleich von Mittelwerten zwischen zwei Gruppen
- **ANOVA**: Vergleich von Mittelwerten über mehrere Gruppen
- **Chi-Quadrat-Test**: Test auf Unabhängigkeit kategorialer Variablen
- **Mann-Whitney-U-Test**: Nicht-parametrische Alternative zum t-Test
- **Pearson-Korrelation**: Lineare Beziehung zwischen kontinuierlichen Variablen
- **Spearman-Korrelation**: Monotone Beziehung (rangbasiert)
- **Kolmogorov-Smirnov-Test**: Vergleich von Verteilungen

## Datensammlung und -speicherung

### Datenquellen
- **Datenbanken**: SQL, NoSQL, relational, Dokumentenspeicher
- **APIs**: REST, GraphQL, Web-Scraping
- **Dateien**: CSV, JSON, XML, Parquet, Avro
- **Streaming-Daten**: Kafka, Kinesis, Echtzeit-Feeds
- **Umfragen und Experimente**: Primäre Datenerhebung
- **Öffentliche Datensätze**: Regierungsdaten, Kaggle, akademische Repositories

### Data Warehousing und Analysespeicher
- **ETL**: Extract, Transform, Load-Prozess
- **Data Lake**: Rohdatenspeicherung im nativen Format
- **Data Warehouse**: Strukturierte, verarbeitete Daten für Analysen
- **Data Mart**: Teilmenge des Warehouses für spezifische Abteilungen
- **OLAP**: Online Analytical Processing, multidimensionale Abfragen
- **Star-Schema**: Faktentabellen umgeben von Dimensionstabellen
- **Snowflake-Schema**: Normalisierte Dimensionstabellen

### Datenbanktypen
- **Relational (SQL)**: MySQL, PostgreSQL, Oracle, SQL Server
- **Dokumentenorientiert**: MongoDB, CouchDB (JSON-ähnliche Dokumente)
- **Key-Value**: Redis, DynamoDB (einfache Schlüssel-Wert-Paare)
- **Spaltenorientiert**: Cassandra, HBase (optimiert für Spalten)
- **Graph**: Neo4j, Amazon Neptune (Knoten und Beziehungen)
- **Zeitreihen**: InfluxDB, TimescaleDB (zeitgestempelte Daten)
- **Vektor**: Pinecone, Milvus (Embedding-Speicher für ML)

## Datenvorverarbeitung

### Datenbereinigung
- **Fehlende Werte**: Imputation (Mittelwert, Median, Modus, Vorhersage), Löschung
- **Ausreißer**: Erkennung (IQR, Z-Wert), Behandlung (Begrenzung, Transformation)
- **Duplikate**: Identifizierung und Entfernung
- **Inkonsistenzen**: Formatstandardisierung, Tippfehlerkorrektur
- **Datenvalidierung**: Prüfung von Constraints, Bereichen, Typen

### Datentransformation
- **Normalisierung**: Skalierung auf 0-1-Bereich
- **Standardisierung**: Z-Wert-Normalisierung (Mittelwert=0, Std=1)
- **Codierung**: One-Hot, Label, ordinal, Target-Codierung
- **Binning**: Gruppierung kontinuierlicher Werte in Kategorien
- **Log-Transformation**: Reduzierung der Schiefe
- **Feature-Skalierung**: Vergleichbarkeit von Merkmalen herstellen

### Feature-Engineering
- **Feature-Erstellung**: Ableitung neuer Merkmale aus bestehenden
- **Feature-Auswahl**: Auswahl der relevantesten Merkmale
  - Filtermethoden (Korrelation, Chi-Quadrat)
  - Wrapper-Methoden (rekursive Feature-Eliminierung)
  - Eingebettete Methoden (LASSO, baumbasierte Wichtigkeit)
- **Dimensionsreduktion**: PCA, t-SNE, UMAP
- **Interaktionsterme**: Multiplikative Kombination von Merkmalen
- **Polynomiale Features**: Erstellung höherer Ordnungen

## Explorative Datenanalyse (EDA)

### EDA-Techniken
- **Zusammenfassungsstatistiken**: Beschreibung von zentraler Tendenz, Streuung, Form
- **Univariate Analyse**: Verteilungen einzelner Variablen
- **Bivariate Analyse**: Beziehungen zwischen zwei Variablen
- **Multivariate Analyse**: Interaktionen mehrerer Variablen
- **Korrelationsanalyse**: Identifizierung von Beziehungen und Multikollinearität
- **Segmentierung**: Gruppierung ähnlicher Beobachtungen

### Visualisierungstools
- **Histogramme**: Verteilung einer einzelnen Variable
- **Boxplots**: Fünf-Zahlen-Zusammenfassung, Ausreißererkennung
- **Streudiagramme**: Beziehung zwischen zwei kontinuierlichen Variablen
- **Heatmaps**: Korrelationsmatrizen, Dichte
- **Balkendiagramme**: Kategorische Vergleiche
- **Liniendiagramme**: Trends über die Zeit
- **Violinplots**: Verteilungsdichte mit Boxplot-Elementen
- **Pairplots**: Mehrere Streudiagramme für Variablenpaare

### Python-Bibliotheken für EDA
- **pandas**: Datenmanipulation und -analyse
- **numpy**: Numerische Datenverarbeitung
- **matplotlib**: Grundlegendes Plotten
- **seaborn**: Statistische Visualisierung
- **plotly**: Interaktive Visualisierungen
- **scipy**: Wissenschaftliche Datenverarbeitung und Statistik

## Maschinelles Lernen in der Datenwissenschaft

### Überwachtes Lernen
- **Regression**: Vorhersage kontinuierlicher Werte
  - Lineare Regression
  - Polynomiale Regression
  - Ridge/LASSO/Elastic Net
  - Entscheidungsbaum-Regressor
  - Random-Forest-Regressor
  - Gradient Boosting (XGBoost, LightGBM, CatBoost)
  
- **Klassifikation**: Vorhersage kategorialer Labels
  - Logistische Regression
  - k-Nächste-Nachbarn
  - Naive Bayes
  - Support Vector Machines
  - Entscheidungsbäume
  - Random Forest
  - Gradient Boosting
  - Neuronale Netze

### Unüberwachtes Lernen
- **Clustering**: Gruppierung ähnlicher Beobachtungen
  - k-Means
  - Hierarchisches Clustering
  - DBSCAN (dichtebasiert)
  - Gaußsche Mischmodelle
  - Spektrales Clustering
  
- **Dimensionsreduktion**: Merkmalsanzahl reduzieren
  - Hauptkomponentenanalyse (PCA)
  - t-Distributed Stochastic Neighbor Embedding (t-SNE)
  - Uniform Manifold Approximation (UMAP)
  - Autoencoder
  
- **Assoziationsregeln**: Gemeinsam auftretende Elemente identifizieren
  - Apriori-Algorithmus
  - FP-Growth

### Modellevaluation
- **Klassifikationsmetriken**: Genauigkeit, Präzision, Recall, F1-Score, ROC-AUC, Konfusionsmatrix
- **Regressionsmetriken**: MAE, MSE, RMSE, R², adjustiertes R²
- **Kreuzvalidierung**: k-Fold, stratifiziert, Leave-One-Out, Zeitreihen-Split
- **Hyperparameter-Tuning**: Grid Search, Random Search, bayessche Optimierung
- **Lernkurven**: Diagnose des Bias-Varianz-Kompromisses

## Big-Data-Technologien

### Frameworks für verteilte Datenverarbeitung
- **Apache Hadoop**: MapReduce, HDFS (Hadoop Distributed File System)
- **Apache Spark**: In-Memory-Verarbeitung, schneller als Hadoop
  - Spark SQL: Verarbeitung strukturierter Daten
  - Spark Streaming: Echtzeitdaten
  - MLlib: Bibliothek für maschinelles Lernen
  - GraphX: Graphverarbeitung
- **Apache Flink**: Stream-Verarbeitung mit geringer Latenz
- **Apache Beam**: Vereinheitlichtes Batch- und Streaming

### Cloud-Plattformen
- **AWS**: S3, EMR, Redshift, SageMaker, Glue
- **Google Cloud**: BigQuery, Dataproc, AI Platform, Cloud Storage
- **Azure**: Synapse Analytics, Databricks, Machine Learning, Data Lake
- **Snowflake**: Cloud-Data-Warehouse

### Datenpipeline-Tools
- **Apache Airflow**: Workflow-Orchestrierung
- **Luigi**: Pipeline-Verwaltung (Spotify)
- **Prefect**: Moderne Workflow-Orchestrierung
- **Dagster**: Datenorchestrator mit Fokus auf Assets
- **dbt**: Datentransformation im Warehouse

## Business Intelligence und Analytik

### BI-Tools
- **Tableau**: Visuelle Analyseplattform
- **Power BI**: Microsoft-Business-Analytics
- **Looker**: Datenexploration und -einblicke (Google)
- **Qlik Sense**: Assoziative Analytik
- **Metabase**: Open-Source-BI
- **Superset**: Apache Open-Source-BI

### Prinzipien des Dashboard-Designs
- **Zielgruppe kennen**: Auf Benutzerbedürfnisse zuschneiden
- **Richtige Visualisierungen wählen**: Diagramm an Datentyp anpassen
- **Farbe strategisch einsetzen**: Wichtige Informationen hervorheben
- **Konsistenz wahren**: Formate und Skalen standardisieren
- **Interaktivität ermöglichen**: Filter, Drill-Downs, Tooltips
- **Leistung optimieren**: Schnelles Laden, effiziente Abfragen
- **Mobile-Überlegungen**: Responsives Design

### Leistungskennzahlen (Key Performance Indicators, KPIs)
- **Finanziell**: Umsatz, Gewinnmarge, ROI, Customer Lifetime Value
- **Kunde**: Akquisitionskosten, Churn-Rate, Zufriedenheitswert, NPS
- **Operativ**: Effizienzraten, Zykluszeit, Fehlerraten
- **Marketing**: Conversion-Raten, Klickraten, Attribution
- **Produkt**: Aktive Nutzer, Engagement, Retention, Feature-Adoption

## Erweiterte Analytik

### Prädiktive Analytik
- **Prognose**: Zeitreihenvorhersage (ARIMA, Prophet, LSTM)
- **Risikomodellierung**: Kredit-Scoring, Betrugserkennung, Versicherung
- **Kundenanalytik**: Churn-Vorhersage, Propensity-Modellierung
- **Bedarfsprognose**: Bestandsoptimierung, Lieferkette
- **Wartungsvorhersage**: Vorhersage von Geräteausfällen

### Präskriptive Analytik
- **Optimierung**: Lineare Programmierung, ganzzahlige Programmierung
- **Simulation**: Monte-Carlo-Methoden, diskrete Ereignissimulation
- **Entscheidungsanalyse**: Entscheidungsbäume, Einflussdiagramme
- **A/B-Tests**: Versuchsplanung, statistische Signifikanz
- **Multi-Armed Bandits**: Adaptive Experimentierung

### Textanalytik (NLP)
- **Textvorverarbeitung**: Tokenisierung, Stemming, Lemmatisierung
- **Sentiment-Analyse**: Positive/negative/neutrale Klassifikation
- **Themenmodellierung**: LDA, NMF für Themenentdeckung
- **Named Entity Recognition**: Identifizierung von Personen, Orten, Organisationen
- **Textklassifikation**: Spam-Erkennung, Kategorisierung
- **Word Embeddings**: Word2Vec, GloVe, BERT

## Datenethik und Governance

### Datenschutz
- **DSGVO**: EU-Datenschutz-Grundverordnung
- **CCPA**: California Consumer Privacy Act
- **HIPAA**: Health Insurance Portability and Accountability Act (US-Gesundheitswesen)
- **Anonymisierung**: Entfernen personenbezogener Daten
- **Differenzieller Datenschutz**: Hinzufügen von Rauschen zum Schutz von Einzelpersonen
- **Einwilligungsverwaltung**: Opt-in/Opt-out-Mechanismen

### Datenqualität
- **Genauigkeit**: Korrektheit der Daten
- **Vollständigkeit**: Alle erforderlichen Daten vorhanden
- **Konsistenz**: Keine Widersprüche zwischen Quellen
- **Aktualität**: Daten verfügbar, wenn benötigt
- **Gültigkeit**: Einhaltung definierter Regeln
- **Einzigartigkeit**: Keine Duplikate

### Bias und Fairness
- **Sampling-Bias**: Nicht-repräsentative Datenerhebung
- **Messbias**: Fehlerhafte Datenerhebungsinstrumente
- **Algorithmischer Bias**: Diskriminierende Modellvorhersagen
- **Fairness-Metriken**: Demografische Parität, Chancengleichheit
- **Bias-Minderung**: Vorverarbeitung, In-Processing, Nachverarbeitung

### Rahmenwerk für Daten-Governance
- **Datenverantwortung**: Verantwortung für Datenassets
- **Metadatenverwaltung**: Dokumentation von Daten über Daten
- **Datenherkunft**: Verfolgung des Datenflusses und der Transformationen
- **Zugriffskontrolle**: Rollenbasierte Berechtigungen
- **Audit-Trails**: Protokollierung des Datenzugriffs und der Änderungen
- **Compliance**: Einhaltung gesetzlicher Vorschriften

## Karrierewege in der Datenwissenschaft

### Rollen
- **Datenanalyst**: Fokus auf deskriptiver Analytik, Dashboards, Berichterstattung
- **Datenwissenschaftler**: Statistische Modellierung, maschinelles Lernen, erweiterte Analytik
- **ML-Ingenieur**: Produktive ML-Systeme, Modellbereitstellung, MLOps
- **Dateningenieur**: Datenpipelines, Infrastruktur, ETL-Prozesse
- **Analytics-Manager**: Teamleitung, Strategie, Stakeholder-Verwaltung
- **BI-Entwickler**: Dashboard-Erstellung, Reportentwicklung
- **Forschungswissenschaftler**: Neue Algorithmen, Publikationen, fortgeschrittene Forschung

### Kompetenzmatrix
- **Technisch**: Python/R, SQL, Statistik, ML-Frameworks, Cloud-Plattformen
- **Analytisch**: Problemlösung, kritisches Denken, Versuchsplanung
- **Kommunikation**: Storytelling, Visualisierung, Präsentationsfähigkeiten
- **Geschäftlich**: Domänenwissen, Stakeholder-Verwaltung, ROI-Analyse
- **Tools**: Git, Jupyter, Docker, CI/CD, Versionskontrolle für Modelle

## Neue Trends

### Aktuelle Entwicklungen
- **AutoML**: Automatisierte Erstellung von ML-Pipelines
- **MLOps**: DevOps-Praktiken für maschinelles Lernen
- **Feature Stores**: Zentralisierte Feature-Verwaltung
- **Data Mesh**: Dezentrale Datenarchitektur
- **LLMs und generative KI**: Große Sprachmodelle, Inhaltsgenerierung
- **Edge Analytics**: Datenverarbeitung an Quellgeräten
- **Echtzeit-Analytik**: Streaming-Datenanalyse
- **Augmented Analytics**: KI-gestützte Datenvorbereitung und -einblicke

### Zukünftige Richtungen
- **Quantum Machine Learning**: Quantenverarbeitung für ML
- **Federated Learning**: Training von Modellen über dezentrale Daten
- **Kausalinferenz**: Von Korrelation zu Kausalität
- **Responsible AI**: Ethik, Erklärbarkeit, Transparenz
- **Data Fabric**: Integrierte Datenverwaltung über Umgebungen hinweg
