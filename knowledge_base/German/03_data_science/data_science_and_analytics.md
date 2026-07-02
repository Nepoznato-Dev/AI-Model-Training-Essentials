# Data Science und Analytics

## Grundkonzepte

### Was ist Data Science?
Data Science ist ein interdisziplinäres Feld, das wissenschaftliche Methoden, Prozesse, Algorithmen und Systeme nutzt, um Wissen und Erkenntnisse aus strukturierten und unstrukturierten Daten zu gewinnen. Es kombiniert:
- **Statistik**: Mathematische Grundlage für Analysen
- **Informatik**: Programmierung, Algorithmen, Datenstrukturen
- **Domänenwissen**: Fachliches Wissen
- **Datenvisualisierung**: Ergebnisse wirksam kommunizieren

### Datentypen
- **Strukturierte Daten**: In Zeilen/Spalten organisiert (Datenbanken, Tabellenkalkulationen)
- **Unstrukturierte Daten**: Kein vordefiniertes Format (Text, Bilder, Audio, Video)
- **Semistrukturierte Daten**: Gewisse Organisation, aber nicht starr (JSON, XML, HTML)
- **Zeitreihendaten**: Sequenzielle Datenpunkte, in zeitlicher Reihenfolge indiziert
- **Räumliche Daten**: Geografische/ortsbezogene Informationen
- **Graphdaten**: Knoten und Kanten, die Beziehungen darstellen

### Der Data-Science-Prozess (CRISP-DM)
1. **Business Understanding**: Definiere Ziele und Anforderungen
2. **Data Understanding**: Sammle und erkunde die Ausgangsdaten
3. **Data Preparation**: Bereinige, transformiere und formatiere Daten (80 % der Arbeit)
4. **Modeling**: Wähle Modellierungstechniken aus und wende sie an
5. **Evaluation**: Beurteile die Modellleistung anhand der Ziele
6. **Deployment**: Implementiere das Modell in einer Produktionsumgebung

## Grundlagen der Statistik

### Deskriptive Statistik
- **Lagemaße**: Mittelwert, Median, Modus
- **Streuungsmaße**: Spannweite, Varianz, Standardabweichung, Interquartilsabstand
- **Form der Verteilung**: Schiefe (Asymmetrie), Kurtosis (Schwanzlastigkeit)
- **Perzentile und Quartile**: Position innerhalb der Verteilung

### Inferenzstatistik
- **Hypothesentests**: Nullhypothese, Alternativhypothese, p-Werte
- **Konfidenzintervalle**: Wertebereich, der den Populationsparameter wahrscheinlich enthält
- **Statistische Signifikanz**: Wahrscheinlichkeit, dass Ergebnisse zufällig entstanden sind
- **Fehler Typ I**: False Positive (wahre Nullhypothese verworfen)
- **Fehler Typ II**: False Negative (falsche Nullhypothese nicht verworfen)
- **Power**: Wahrscheinlichkeit, eine falsche Nullhypothese korrekt zu verwerfen

### Wahrscheinlichkeitsverteilungen
- **Normalverteilung**: Glockenkurve, Mittelwert = Median = Modus
- **Binomialverteilung**: Erfolgs-/Misserfolgsausgänge
- **Poisson-Verteilung**: Anzahl von Ereignissen in einem festen Intervall
- **Gleichverteilung**: Alle Ausgänge gleich wahrscheinlich
- **Exponentialverteilung**: Zeit zwischen Ereignissen
- **t-Verteilung**: Kleine Stichprobengrößen, unbekannte Populationsvarianz
- **Chi-Quadrat-Verteilung**: Analyse kategorialer Daten

### Statistische Tests
- **t-Test**: Vergleicht Mittelwerte zwischen zwei Gruppen
- **ANOVA**: Vergleicht Mittelwerte über mehrere Gruppen hinweg
- **Chi-Quadrat-Test**: Testet die Unabhängigkeit kategorialer Variablen
- **Mann-Whitney U**: Nichtparametrische Alternative zum t-Test
- **Pearson-Korrelation**: Lineare Beziehung zwischen kontinuierlichen Variablen
- **Spearman-Korrelation**: Monotone Beziehung (rangbasiert)
- **Kolmogorov-Smirnov**: Vergleicht Verteilungen

## Datenerfassung und Speicherung

### Datenquellen
- **Datenbanken**: SQL, NoSQL, relational, Document Stores
- **APIs**: REST, GraphQL, Web Scraping
- **Dateien**: CSV, JSON, XML, Parquet, Avro
- **Streaming-Daten**: Kafka, Kinesis, Echtzeit-Feeds
- **Umfragen und Experimente**: Primäre Datenerhebung
- **Öffentliche Datensätze**: Regierungsdaten, Kaggle, akademische Repositorien

### Data Warehousing
- **ETL**: Extract, Transform, Load-Prozess
- **Data Lake**: Speicherung roher Daten im nativen Format
- **Data Warehouse**: Strukturierte, verarbeitete Daten für Analysen
- **Data Mart**: Teilmenge eines Warehouses für eine bestimmte Abteilung
- **OLAP**: Online Analytical Processing, multidimensionale Abfragen
- **Star Schema**: Faktentabellen, umgeben von Dimensionstabellen
- **Snowflake Schema**: Normalisierte Dimensionstabellen

### Datenbanktypen
- **Relational (SQL)**: MySQL, PostgreSQL, Oracle, SQL Server
- **Document**: MongoDB, CouchDB (JSON-ähnliche Dokumente)
- **Key-Value**: Redis, DynamoDB (einfache Schlüssel-Wert-Paare)
- **Column-Family**: Cassandra, HBase (für Spalten optimiert)
- **Graph**: Neo4j, Amazon Neptune (Knoten und Beziehungen)
- **Time-Series**: InfluxDB, TimescaleDB (mit Zeitstempeln versehene Daten)
- **Vector**: Pinecone, Milvus (Embedding-Speicher für ML)

## Datenvorverarbeitung

### Datenbereinigung
- **Fehlende Werte**: Imputation (Mittelwert, Median, Modus, Vorhersage), Löschung
- **Ausreißer**: Erkennung (IQR, Z-score), Behandlung (Capping, Transformation)
- **Duplikate**: Identifikation und Entfernung
- **Inkonsistenzen**: Formate standardisieren, Tippfehler korrigieren
- **Datenvalidierung**: Prüfen von Constraints, Bereichen und Typen

### Datentransformation
- **Normalisierung**: Skalierung auf den Bereich 0-1
- **Standardisierung**: Z-score-Normalisierung (mean=0, std=1)
- **Encoding**: One-hot-, Label-, Ordinal- und Target-Encoding
- **Binning**: Gruppieren kontinuierlicher Werte in Kategorien
- **Log-Transformation**: Reduziert Schiefe
- **Feature Scaling**: Macht Features vergleichbar

### Feature Engineering
- **Feature-Erstellung**: Neue Features aus vorhandenen ableiten
- **Feature-Auswahl**: Die relevantesten Features auswählen
  - Filtermethoden (Korrelation, Chi-Quadrat)
  - Wrapper-Methoden (rekursive Feature-Eliminierung)
  - Eingebettete Methoden (LASSO, baumbasierte Wichtigkeit)
- **Dimensionalitätsreduktion**: PCA, t-SNE, UMAP
- **Interaktionsterme**: Features multiplikativ kombinieren
- **Polynomial Features**: Terme höherer Ordnung erzeugen

## Explorative Datenanalyse (EDA)

### EDA-Techniken
- **Zusammenfassende Statistiken**: Beschreiben Lage, Streuung und Form
- **Univariate Analyse**: Verteilungen einzelner Variablen
- **Bivariate Analyse**: Beziehungen zwischen zwei Variablen
- **Multivariate Analyse**: Interaktionen mehrerer Variablen
- **Korrelationsanalyse**: Beziehungen und Multikollinearität identifizieren
- **Segmentierung**: Ähnliche Beobachtungen gruppieren

### Visualisierungswerkzeuge
- **Histogramme**: Verteilung einer einzelnen Variablen
- **Box Plots**: Fünf-Punkte-Zusammenfassung, Ausreißererkennung
- **Scatter Plots**: Beziehung zwischen zwei kontinuierlichen Variablen
- **Heatmaps**: Korrelationsmatrizen, Dichte
- **Bar Charts**: Vergleiche kategorialer Werte
- **Line Charts**: Trends über die Zeit
- **Violin Plots**: Verteilungsdichte mit Box-Plot-Elementen
- **Pair Plots**: Mehrere Scatter Plots für Variablenpaare

### Python-Bibliotheken für EDA
- **pandas**: Datenmanipulation und -analyse
- **numpy**: Numerisches Rechnen
- **matplotlib**: Grundlegendes Plotting
- **seaborn**: Statistische Visualisierung
- **plotly**: Interaktive Visualisierungen
- **scipy**: Wissenschaftliches Rechnen und Statistik

## Machine Learning in Data Science

### Überwachtes Lernen
- **Regression**: Kontinuierliche Werte vorhersagen
  - Linear Regression
  - Polynomial Regression
  - Ridge/LASSO/Elastic Net
  - Decision Tree Regressor
  - Random Forest Regressor
  - Gradient Boosting (XGBoost, LightGBM, CatBoost)
  
- **Klassifikation**: Kategoriale Labels vorhersagen
  - Logistic Regression
  - k-Nearest Neighbors
  - Naive Bayes
  - Support Vector Machines
  - Decision Trees
  - Random Forest
  - Gradient Boosting
  - Neural Networks

### Unüberwachtes Lernen
- **Clustering**: Ähnliche Beobachtungen gruppieren
  - k-Means
  - Hierarchisches Clustering
  - DBSCAN (dichtebasiert)
  - Gaussian Mixture Models
  - Spectral Clustering
  
- **Dimensionalitätsreduktion**: Anzahl der Features reduzieren
  - Principal Component Analysis (PCA)
  - t-Distributed Stochastic Neighbor Embedding (t-SNE)
  - Uniform Manifold Approximation (UMAP)
  - Autoencoders
  
- **Assoziationsregeln**: Gemeinsam auftretende Elemente finden
  - Apriori Algorithm
  - FP-Growth

### Modellbewertung
- **Klassifikationsmetriken**: Accuracy, Precision, Recall, F1-score, ROC-AUC, Confusion Matrix
- **Regressionsmetriken**: MAE, MSE, RMSE, R², Adjusted R²
- **Cross-Validation**: k-fold, stratified, leave-one-out, time series split
- **Hyperparameter-Tuning**: Grid Search, Random Search, Bayes'sche Optimierung
- **Learning Curves**: Bias-Variance-Trade-off diagnostizieren

## Big-Data-Technologien

### Frameworks für verteiltes Rechnen
- **Apache Hadoop**: MapReduce, HDFS (Hadoop Distributed File System)
- **Apache Spark**: In-Memory-Verarbeitung, schneller als Hadoop
  - Spark SQL: Verarbeitung strukturierter Daten
  - Spark Streaming: Echtzeitdaten
  - MLlib: Machine-Learning-Bibliothek
  - GraphX: Graphverarbeitung
- **Apache Flink**: Stream-Verarbeitung mit geringer Latenz
- **Apache Beam**: Einheitlich für Batch und Streaming

### Cloud-Plattformen
- **AWS**: S3, EMR, Redshift, SageMaker, Glue
- **Google Cloud**: BigQuery, Dataproc, AI Platform, Cloud Storage
- **Azure**: Synapse Analytics, Databricks, Machine Learning, Data Lake
- **Snowflake**: Cloud Data Warehouse

### Datenpipeline-Tools
- **Apache Airflow**: Workflow-Orchestrierung
- **Luigi**: Pipeline-Management (Spotify)
- **Prefect**: Moderne Workflow-Orchestrierung
- **Dagster**: Datenorchestrator mit Fokus auf Assets
- **dbt**: Datentransformation im Warehouse

## Business Intelligence und Analytics

### BI-Tools
- **Tableau**: Plattform für visuelle Analysen
- **Power BI**: Microsoft Business Analytics
- **Looker**: Datenexploration und Erkenntnisse (Google)
- **Qlik Sense**: Assoziative Analytik
- **Metabase**: Open-Source-BI
- **Superset**: Apache Open-Source-BI

### Prinzipien für Dashboard-Design
- **Kenne dein Publikum**: Auf die Bedürfnisse der Nutzer zuschneiden
- **Wähle die richtigen Visualisierungen**: Diagramm an Datentyp anpassen
- **Farbe strategisch einsetzen**: Wichtige Informationen hervorheben
- **Konsistenz wahren**: Formate und Skalen standardisieren
- **Interaktivität ermöglichen**: Filter, Drill-downs, Tooltips
- **Leistung optimieren**: Schnelles Laden, effiziente Abfragen
- **Mobile Aspekte**: Responsives Design

### Key Performance Indicators (KPIs)
- **Finanziell**: Umsatz, Gewinnmarge, ROI, Customer Lifetime Value
- **Kundenbezogen**: Akquisitionskosten, Churn Rate, Zufriedenheitsscore, NPS
- **Operativ**: Effizienzraten, Durchlaufzeit, Fehlerraten
- **Marketing**: Conversion Rates, Click-Through-Rates, Attribution
- **Produkt**: Aktive Nutzer, Engagement, Retention, Feature-Adoption

## Fortgeschrittene Analytik

### Prädiktive Analytik
- **Forecasting**: Zeitreihenvorhersage (ARIMA, Prophet, LSTM)
- **Risikomodellierung**: Kredit-Scoring, Betrugserkennung, Versicherungen
- **Kundenanalytik**: Churn-Vorhersage, Propensity Modeling
- **Nachfrageprognose**: Bestandsoptimierung, Lieferkette
- **Wartungsvorhersage**: Antizipation von Geräteausfällen

### Präskriptive Analytik
- **Optimierung**: Lineare Programmierung, ganzzahlige Programmierung
- **Simulation**: Monte-Carlo-Methoden, diskrete Ereignissimulation
- **Entscheidungsanalyse**: Entscheidungsbäume, Einflussdiagramme
- **A/B-Testing**: Versuchsdesign, statistische Signifikanz
- **Multi-Armed Bandits**: Adaptive Experimente

### Textanalytik (NLP)
- **Text Preprocessing**: Tokenization, Stemming, Lemmatization
- **Sentiment Analysis**: Klassifikation positiv/negativ/neutral
- **Topic Modeling**: LDA, NMF zur Themenerkennung
- **Named Entity Recognition**: Personen, Orte, Organisationen identifizieren
- **Textklassifikation**: Spam-Erkennung, Kategorisierung
- **Word Embeddings**: Word2Vec, GloVe, BERT

## Datenethik und Governance

### Datenschutz
- **GDPR**: EU General Data Protection Regulation
- **CCPA**: California Consumer Privacy Act
- **HIPAA**: Health Insurance Portability and Accountability Act (US healthcare)
- **Anonymisierung**: Entfernen personenbezogener Daten
- **Differential Privacy**: Hinzufügen von Rauschen zum Schutz von Individuen
- **Consent Management**: Opt-in-/Opt-out-Mechanismen

### Datenqualität
- **Accuracy**: Korrektheit der Daten
- **Completeness**: Alle erforderlichen Daten vorhanden
- **Consistency**: Keine Widersprüche zwischen Quellen
- **Timeliness**: Daten verfügbar, wenn sie benötigt werden
- **Validity**: Entspricht definierten Regeln
- **Uniqueness**: Keine Duplikate

### Bias und Fairness
- **Sampling Bias**: Nicht repräsentative Datenerhebung
- **Measurement Bias**: Fehlerhafte Datenerfassungsinstrumente
- **Algorithmic Bias**: Diskriminierende Modellvorhersagen
- **Fairness Metrics**: Demographic Parity, Equal Opportunity
- **Bias Mitigation**: Pre-processing, in-processing, post-processing

### Data-Governance-Framework
- **Data Stewardship**: Verantwortung für Datenbestände
- **Metadata Management**: Dokumentation von Daten über Daten
- **Data Lineage**: Datenfluss und Transformationen nachverfolgen
- **Access Control**: Rollenbasierte Berechtigungen
- **Audit Trails**: Protokollierung von Datenzugriffen und Änderungen
- **Compliance**: Einhaltung regulatorischer Vorgaben

## Karrierepfade in Data Science

### Rollen
- **Data Analyst**: Fokus auf deskriptive Analytik, Dashboards, Reporting
- **Data Scientist**: Statistische Modellierung, Machine Learning, fortgeschrittene Analytik
- **ML Engineer**: Produktive ML-Systeme, Model Deployment, MLOps
- **Data Engineer**: Datenpipelines, Infrastruktur, ETL-Prozesse
- **Analytics Manager**: Teamführung, Strategie, Stakeholder-Management
- **BI Developer**: Dashboard-Erstellung, Berichtsentwicklung
- **Research Scientist**: Neue Algorithmen, Publikationen, fortgeschrittene Forschung

### Kompetenzmatrix
- **Technisch**: Python/R, SQL, Statistik, ML-Frameworks, Cloud-Plattformen
- **Analytisch**: Problemlösung, kritisches Denken, experimentelles Design
- **Kommunikation**: Storytelling, Visualisierung, Präsentationsfähigkeiten
- **Business**: Domänenwissen, Stakeholder-Management, ROI-Analyse
- **Tools**: Git, Jupyter, Docker, CI/CD, Versionskontrolle für Modelle

## Neue Trends

### Aktuelle Entwicklungen
- **AutoML**: Automatisierte Erstellung von Machine-Learning-Pipelines
- **MLOps**: DevOps-Praktiken für Machine Learning
- **Feature Stores**: Zentralisiertes Feature-Management
- **Data Mesh**: Dezentrale Datenarchitektur
- **LLMs und Generative AI**: Große Sprachmodelle, Content-Erzeugung
- **Edge Analytics**: Datenverarbeitung an den Quellgeräten
- **Real-Time Analytics**: Streaming-Datenanalyse
- **Augmented Analytics**: AI-gestützte Datenvorbereitung und Erkenntnisse

### Zukünftige Richtungen
- **Quantum Machine Learning**: Quantencomputing für ML
- **Federated Learning**: Training von Modellen über dezentrale Daten hinweg
- **Causal Inference**: Von Korrelation zu Kausalität übergehen
- **Responsible AI**: Ethik, Erklärbarkeit, Transparenz
- **Data Fabric**: Integriertes Datenmanagement über Umgebungen hinweg
