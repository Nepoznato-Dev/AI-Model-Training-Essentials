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
# Data Science at Analytics
Ang agham ng data ay ang disiplina ng paggawa ng hilaw na data sa naaaksyong pananaw. Nakalagay ito sa intersection ng statistics, computer science, at domain expertise — at naging mahalaga ito sa bawat sektor mula sa pananalapi hanggang sa pangangalagang pangkalusugan. Ang file na ito ay nagtuturo sa mga pangunahing konsepto, tool, at daloy ng trabaho na dapat malaman ng bawat practitioner.
---

## Ang Proseso ng Data Science
Karamihan sa mga proyekto ay sumusunod sa ilang pagkakaiba-iba ng **CRISP-DM**, ang pang-industriyang ikot ng buhay:
| Yugto | Ano ang Mangyayari | Karaniwang Oras |
|-------|-------------|--------------|
| **Pag-unawa sa Negosyo** | Tukuyin ang mga layunin, sukatan ng tagumpay, at mga hadlang | 10–15% |
| **Pag-unawa sa Data** | Kolektahin, galugarin, at i-profile ang data | 10–15% |
| **Paghahanda ng Data** | Malinis, ibahin ang anyo, mga tampok ng engineer | ~50–60% |
| **Pagmomodelo** | Pumili at sanayin ang mga modelo | 10–15% |
| **Pagsusuri** | Tayahin ang pagganap laban sa mga layunin sa negosyo | 5–10% |
| **Deployment** | Ipadala ang modelo sa produksyon | 5–10% |
Ang paghahanda ng data, partikular ang paglilinis ng data, ay malawak na tinatantya na kumokonsumo ng humigit-kumulang 80% ng oras ng data scientist.
---

## Mga Uri ng Data sa Isang Sulyap
| Uri | Paglalarawan | Halimbawa |
|------|-------------|---------|
| **Structured** | Nakaayos sa mga row at column | Mga talahanayan ng SQL, mga spreadsheet |
| **Hindi nakabalangkas** | Walang paunang natukoy na format | Teksto, mga larawan, audio, video |
| **Semi-structured** | Ilang organisasyon ngunit nababaluktot | JSON, XML, HTML |
| **Serye ng oras** | Sequential data na na-index ayon sa oras | Mga presyo ng stock, pagbabasa ng sensor |
| **Spatial** | Heograpiko o batay sa lokasyon | Mga coordinate ng GPS, data ng mapa |
| **Graph** | Mga node at gilid na kumakatawan sa mga relasyon | Mga social network, mga graph ng kaalaman |
---

## Mga Pangunahing Istatistika
### Descriptive vs Inferential Statistics
Ang mga deskriptibong istatistika ay nagbubuod kung ano ang mayroon ka; Hinahayaan ka ng inferential statistics na gumawa ng mga konklusyon tungkol sa kung ano ang *wala* mo (ang mas malawak na populasyon).
| Konsepto | Mga Pangunahing Ideya |
|---------|------------|
| **Central tendency** | Mean (sensitibo sa mga outlier), median (matatag), mode (pinaka madalas) |
| **Pagkakalat** | Range, variance, standard deviation, interquartile range |
| **Hugis ng pamamahagi** | Skewness (asymmetry), kurtosis (buntot na bigat) |
| **Pagsusuri ng hypothesis** | Null vs alternatibong hypothesis, p-values, antas ng kabuluhan (α) |
| **Mga pagitan ng kumpiyansa** | Ang saklaw na malamang na naglalaman ng totoong parameter ng populasyon |
| **Mga error sa Type I / Type II** | Maling positibo (pagtanggi sa isang tunay na null) / maling negatibo (nawawalang isang tunay na epekto) |
### Mga Karaniwang Pagsusuri sa Istatistika
| Pagsubok | Kailan Gagamitin |
|------|-------------|
| **t-test** | Paghambingin ang ibig sabihin sa pagitan ng dalawang pangkat |
| **ANOVA** | Paghambingin ang ibig sabihin sa tatlo o higit pang mga pangkat |
| **Chi-square** | Subukan ang kalayaan ng mga kategoryang variable |
| **Mann-Whitney U** | Non-parametric na alternatibo sa t-test (walang normality assumption) |
| **Pearson correlation** | Linear na relasyon sa pagitan ng dalawang tuluy-tuloy na variable |
| **Karelasyon ng Spearman** | Monotonic na relasyon (nakabatay sa ranggo, mas matatag) |
### Mga Pamamahagi ng Probability na Dapat Malaman
| Pamamahagi | Use Case |
|-------------|----------|
| **Normal** | Mga likas na phenomena, mga error sa pagsukat — ang klasikong bell curve |
| **Binomial** | Mga bilang ng tagumpay/kabiguan (mga coin flips, conversion rate) |
| **Poisson** | Bilang ng kaganapan sa isang nakapirming agwat (mga tawag kada oras, mga depekto bawat batch) |
| **Exponential** | Oras sa pagitan ng mga kaganapan (mga oras ng paghihintay, mga agwat ng pagkabigo) |
| **t-Pamamahagi** | Maliit na sample o hindi alam na pagkakaiba-iba ng populasyon |
| **Chi-square** | Pangkategoryang data analysis, goodness-of-fit na mga pagsubok |
---

## Pangongolekta at Imbakan ng Data
### Saan Nagmumula ang Data
Dumarating ang real-world na data mula sa maraming source: relational database, API (REST, GraphQL), flat file (CSV, JSON, Parquet), streaming platform (Kafka, Kinesis), survey, at pampublikong repository (Kaggle, government portal). Tinutukoy ng format na natatanggap mo ang karamihan sa iyong diskarte sa preprocessing.
### Mga Konsepto ng Data Warehousing
| Konsepto | Paglalarawan |
|---------|-------------|
| **ETL** | Extract → Transform → Load — tradisyonal na pipeline approach |
| **ELT** | Extract → Load → Transform — modernong cloud approach (load raw, transform in-warehouse) |
| **Data Lake** | Raw data na nakaimbak sa katutubong format (schema-on-read) |
| **Data Warehouse** | Nakabalangkas, naprosesong data na na-optimize para sa pagsusuri (schema-on-write) |
| **Data Mart** | Isang subset ng isang warehouse, na saklaw sa isang departamento o domain |
| **Star Schema** | Central fact table na napapalibutan ng mga talahanayan ng dimensyon |
| **Skema ng Snowflake** | Mga normalized na talahanayan ng dimensyon (mas kaunting redundancy, mas maraming pagsasama) |
### Mga Uri ng Database
| Uri | Mga halimbawa | Pinakamahusay Para sa |
|------|----------|----------|
| **Relational (SQL)** | PostgreSQL, MySQL, Oracle | Structured data, mga transaksyon sa ACID |
| **Dokumento** | MongoDB, CouchDB | Mga flexible na schema, data na mala-JSON |
| **Key-Value** | Redis, DynamoDB | Caching, session, simpleng paghahanap |
| **Column-Family** | Cassandra, HBase | Sumulat ng mabibigat na workload, serye ng oras |
| **Graph** | Neo4j, Amazon Neptune | Mga relasyon, mga social network |
| **Serye ng Oras** | InfluxDB, TimescaleDB | Mga sukatan ng IoT, pagsubaybay |
| **Vector** | Pinecone, Milvus | Pag-embed ng storage para sa paghahanap sa ML/AI |
---

## Data Preprocessing at Feature Engineering
### Checklist ng Paglilinis
Ang bawat totoong dataset ay may mga isyu. Narito ang karaniwang paglilinis:
| Isyu | Diskarte |
|-------|----------|
| **Nawawalang halaga** | Imputation (mean, median, prediction), o pagtanggal kung kalat-kalat |
| **Mga Outlier** | I-detect sa pamamagitan ng IQR o Z-score; treat na may capping o transformation |
| **Mga Duplicate** | Tukuyin at alisin ang |
| **Hindi pagkakapare-pareho** | I-standardize ang mga format, ayusin ang mga typo, gawing normal ang mga unit |
### Mga Teknik sa Pagbabago
| Teknik | Ano ang Ginagawa Nito |
|-----------|-------------|
| **Normalization** | I-scale ang mga value sa 0–1 range |
| **Standardisasyon** | Z-score: mean = 0, std = 1 |
| **One-hot encoding** | Kino-convert ang mga kategorya sa mga binary column |
| **Pag-encode ng label** | Nagtatalaga ng mga integer na label sa mga kategorya |
| **Pagbabago ng log** | Binabawasan ang right-skew sa data |
| **Binning** | Pinagpangkat ang tuluy-tuloy na mga halaga sa mga discrete na bucket |
### Feature Engineering
Ang feature engineering ay kadalasang ang pagkakaiba sa pagitan ng isang pangkaraniwang modelo at isang mahusay. Kabilang sa mga pangunahing pamamaraan ang:
- **Paggawa ng feature**: Pagkuha ng mga bagong column mula sa mga dati nang column (hal.,`age_group`mula sa`age`).
- **Pagpipilian ng feature**: Mga paraan ng filter (kaugnayan), mga paraan ng wrapper (recursive elimination), mga naka-embed na pamamaraan (LASSO, kahalagahan ng puno).
- **Pagbabawas ng dimensyon**: PCA para sa linear, t-SNE o UMAP para sa visualization.
- **Mga tuntunin sa pakikipag-ugnayan**: Pinagsasama-sama ang mga feature nang maramihan upang makuha ang magkasanib na epekto.
---

## Exploratory Data Analysis (EDA)
Ang EDA ay kung saan ka bumuo ng intuwisyon tungkol sa iyong data bago magmodelo. Ang layunin ay makita ang mga pattern, anomalya, at relasyon.
### Pagpili ng Tamang Chart
| Uri ng Tsart | Pinakamahusay Para sa |
|-----------|----------|
| **Histogram** | Distribusyon ng isang variable |
| **Kahon na plot** | Limang-numero na buod, outlier detection |
| **Scatter plot** | Relasyon sa pagitan ng dalawang tuluy-tuloy na variable |
| **Heatmap** | Correlation matrice, density visualization |
| **Bar chart** | Paghahambing ng mga kategorya |
| **Line chart** | Mga uso sa paglipas ng panahon |
| **biyolin plot** | Densidad ng pamamahagi + buod ng plot ng kahon |
| **Pair plot** | Mabilis na pangkalahatang-ideya ng lahat ng variable na pares |
### Ang Python EDA Stack
| Aklatan | Tungkulin |
|---------|------|
| **pandas** | Pagmamanipula at pagsusuri ng data |
| **numpy** | Numerical computing |
| **matplotlib** | Foundation plotting |
| **seaborn** | Statistical visualization (built on matplotlib) |
| **plotly** | Interactive, web-based na visualization |
| **scipy** | Scientific computing at istatistika |
---

## Machine Learning sa Data Science
### Pinangangasiwaang Pag-aaral sa isang Sulyap
| Gawain | Algorithm |
|------|-----------|
| **Regression** (hulaan ang isang numero) | Linear, Ridge/LASSO, Decision Tree, Random Forest, Gradient Boosting (XGBoost, LightGBM) |
| **Pag-uuri** (hulaan ang isang kategorya) | Logistic Regression, k-NN, Naive Bayes, SVM, Decision Trees, Random Forest, Neural Networks |
### Unsupervised Learning sa isang Sulyap
| Gawain | Algorithm |
|------|-----------|
| **Clustering** | k-Means, Hierarchical, DBSCAN, Gaussian Mixture Models |
| **Pagbabawas ng Dimensyon** | PCA, t-SNE, UMAP, Autoencoders |
| **Mga Panuntunan ng Asosasyon** | Apriori, FP-Paglago |
### Pagsusuri ng Modelo
| Uri ng Sukatan | Mga Pangunahing Sukatan |
|-------------|-------------|
| **Pag-uuri** | Katumpakan, katumpakan, recall, F1-score, ROC-AUC, confusion matrix |
| **Regression** | MAE, MSE, RMSE, R², Naayos na R² |
| **Pagpapatunay** | k-fold cross-validation, stratified, time series split |
| **Pag-tune** | Grid search, random na paghahanap, Bayesian optimization |
---

## Mga Teknolohiya ng Big Data
Kapag lumampas ang mga dataset sa kung ano ang kayang pangasiwaan ng isang makina, papasok sa larawan ang distributed computing.
| Balangkas | Lakas |
|-----------|----------|
| **Apache Spark** | Pagproseso sa memorya; Spark SQL, Streaming, MLlib, GraphX ​​|
| **Apache Hadoop** | MapReduce + HDFS — ang orihinal na malaking data stack |
| **Apache Flink** | Low-latency stream processing |
| **Apache Beam** | Pinag-isang batch at streaming na modelo |
### Cloud Data Platform
| Provider | Mga Pangunahing Serbisyo |
|----------|-------------|
| **AWS** | S3, EMR, Redshift, SageMaker, Glue |
| **Google Cloud** | BigQuery, Dataproc, AI Platform, Cloud Storage |
| **Azure** | Synapse Analytics, Databricks, Machine Learning, Data Lake |
| **Snowflake** | Cloud-native na data warehouse (provider-agnostic) |
### Pipeline Orchestration
| Tool | Mga Tala |
|------|-------|
| **Apache Airflow** | Pamantayan sa industriya; Mga DAG na nakabase sa Python |
| **Prefect** | Modernong alternatibo na may mas malinis na API |
| **Dagster** | Asset-centric orkestrasyon |
| **dbt** | SQL-first data transformation in-warehouse |
---

## Business Intelligence at Analytics
### BI Tools Kumpara
| Tool | Uri | Lakas |
|------|------|----------|
| **Tableau** | Komersyal | Rich visual analytics, drag-and-drop |
| **Power BI** | Komersyal (Microsoft) | Deep Office/Azure integration |
| **Looker** | Komersyal (Google) | Paggalugad ng data, pagmomodelo ng LookML |
| **Metabase** | Open-source | Madaling setup, SQL-native |
| **Superset** | Open-source (Apache) | Nasusukat, SQL-una |
### Mga Prinsipyo sa Disenyo ng Dashboard
Ang mga epektibong dashboard ay sumusunod sa mga itinatag na prinsipyo: tukuyin ang audience, piliin ang naaangkop na visualization para sa bawat sukatan, gamitin ang kulay sa madiskarteng paraan (hindi pandekorasyon), panatilihin ang pare-parehong mga sukat, at paganahin ang interaktibidad (mga filter, drill-down). Mahalaga rin ang performance — ang mga dashboard na may mabagal na oras ng pag-load ay nakakabawas sa paggamit ng user.
### Mga Karaniwang Kategorya ng KPI
| Kategorya | Mga halimbawa |
|----------|---------|
| **Pananalapi** | Kita, margin ng tubo, ROI, panghabambuhay na halaga ng customer |
| **Customer** | Gastos sa pagkuha (CAC), churn rate, NPS, satisfaction score |
| **Pagpapatakbo** | Mga rate ng kahusayan, oras ng pag-ikot, mga rate ng depekto |
| **Marketing** | Rate ng conversion, click-through rate, ROAS, attribution |
| **Produkto** | Pang-araw-araw na aktibong user, pakikipag-ugnayan, pagpapanatili, pagpapatibay ng tampok |
---

## Advanced na Analytics
| Diskarte | Mga diskarte | Kailan Gagamitin |
|----------|-----------|-------------|
| **Mahuhula** | Serye ng oras (ARIMA, Propeta, LSTM), pagmomodelo ng panganib, hula ng churn | Pagtataya ng mga halaga sa hinaharap |
| **Nagrereseta** | Linear programming, Monte Carlo simulation, A/B testing, multi-armed bandits | Pag-optimize ng mga desisyon |
| **Text Analytics** | Tokenization, pagsusuri ng sentimento, pagmomodelo ng paksa (LDA), NER, mga pag-embed ng salita (Word2Vec, BERT) | Kinukuha ang insight mula sa text |
---

## Etika at Pamamahala ng Data
### Mga Regulasyon sa Privacy
| Regulasyon | Saklaw |
|-----------|-------|
| **GDPR** | mga paksa ng data ng EU; karapatang burahin, pahintulot, data portability |
| **CCPA** | Mga mamimili ng California; mag-opt out sa mga benta ng data |
| **HIPAA** | Data ng pangangalagang pangkalusugan ng US; mahigpit na mga panuntunan sa pagiging kompidensiyal |
### Mga Dimensyon ng Kalidad ng Data
| Dimensyon | Tanong |
|-----------|----------|
| **Katumpakan** | Tama ba ang data? |
| **Pagiging kumpleto** | May kulang ba? |
| **Consistency** | Sumasang-ayon ba ang mga mapagkukunan? |
| **Pagiging napapanahon** | Ito ba ay kasalukuyang? |
| **Katotohanan** | Naaayon ba ito sa mga inaasahang format? |
| **Kakaiba** | Mayroon bang mga duplicate? |
### Bias at Pagkamakatarungan
Maaaring pumasok ang bias sa anumang yugto: sampling bias (hindi kinatawan ng data), bias sa pagsukat (mga may sira na instrumento), o algorithmic bias (diskriminatoryong mga hula). Kasama sa mga diskarte sa pagpapagaan ang paunang pagproseso (pag-aayos ng data), in-processing (pagpigil sa modelo), at post-processing (pagsasaayos ng mga output). Ang mga sukatan ng pagiging patas tulad ng demograpikong parity at pantay na pagkakataon ay nakakatulong sa pag-quantify ng problema.
---

## Mga Landas sa Karera
| Tungkulin | Tumutok |
|------|-------|
| **Data Analyst** | Descriptive analytics, dashboard, pag-uulat |
| **Data Scientist** | Statistical modelling, ML, advanced analytics |
| **ML Engineer** | Produksyon ng ML system, pag-deploy ng modelo, MLOps |
| **Data Engineer** | Mga pipeline ng data, imprastraktura, ETL |
| **Analytics Manager** | Pamumuno ng pangkat, diskarte, pamamahala ng stakeholder |
| **Research Scientist** | Novel algorithm, mga publikasyon |
---

## Mga Umuusbong na Trend
- **AutoML**: Awtomatikong paggawa ng pipeline at pagpili ng modelo.
- **MLOps**: Inilapat ang mga kasanayan sa DevOps sa pamamahala ng lifecycle ng ML.
- **Mga Tindahan ng Tampok**: Sentralisadong pamamahala ng tampok para sa muling paggamit sa mga koponan.
- **Data Mesh**: Desentralisado, arkitektura ng data na pagmamay-ari ng domain.
- **LLMs at Generative AI**: Mga malalaking modelo ng wika na nagpapabago ng mga daloy ng trabaho sa text, code, at larawan.
- **Edge Analytics**: Pagproseso ng data sa device kaysa sa cloud.
- **Causal Inference**: Paglipat sa kabila ng ugnayan upang maunawaan ang aktwal na sanhi at epekto.
- **Federated Learning**: Mga modelo ng pagsasanay sa desentralisadong data nang hindi ito ginagalaw.
- **Responsable AI**: Ang etika, kakayahang maipaliwanag, at transparency ay nagiging mga karaniwang kinakailangan.