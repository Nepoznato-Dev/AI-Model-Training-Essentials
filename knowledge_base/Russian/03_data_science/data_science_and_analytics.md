<!-- 
Этот файл был автоматически переведён с английского на русский.
Источник: data_science_and_analytics.md
Примечание: технические термины, примеры кода и имена собственные могут оставаться на английском.
Чтобы улучшить точность, присылайте правки через pull request.
-->

# наука о данных и аналитика

## Основные концепции

### Что такое наука о данных?
наука о данных — это междисциплинарная область, которая использует научные методы, процессы, алгоритмы и системы для извлечения знаний и выводов из структурированных и неструктурированных данных. Она объединяет:
- **Статистика**: математическую основу анализа
- **Информатика**: программирование, алгоритмы, структуры данных
- **Предметная экспертиза**: знание предметной области
- **Визуализация данных**: эффективное представление результатов

### Типы данных
- **Структурированные данные**: организованы в строки и столбцы (базы данных, электронные таблицы)
- **Неструктурированные данные**: не имеют заранее заданного формата (текст, изображения, аудио, видео)
- **Полуструктурированные данные**: имеют некоторую организацию, но не жёсткую структуру (JSON, XML, HTML)
- **Временные ряды**: последовательные точки данных, упорядоченные по времени
- **Пространственные данные**: географическая и локационная информация
- **Графовые данные**: узлы и рёбра, представляющие связи

### Процесс работы в науке о данных (CRISP-DM)
1. **Понимание бизнеса**: определить цели и требования
2. **Понимание данных**: собрать и изучить исходные данные
3. **Подготовка данных**: очистить, преобразовать и привести данные к нужному формату (80% работы)
4. **Моделирование**: выбрать и применить методы моделирования
5. **Оценка**: проверить качество модели относительно поставленных целей
6. **Внедрение**: реализовать модель в продуктивной среде

## Основы статистики

### Описательная статистика
- **Меры центральной тенденции**: среднее, медиана, мода
- **Меры разброса**: размах, дисперсия, стандартное отклонение, межквартильный размах
- **Форма распределения**: асимметрия и эксцесс
- **Процентили и квартили**: положение внутри распределения

### Выводная статистика
- **Проверка гипотез**: нулевая гипотеза, альтернативная гипотеза, p-значения
- **Доверительные интервалы**: диапазон значений, который с высокой вероятностью содержит параметр генеральной совокупности
- **Статистическая значимость**: вероятность того, что результат получен случайно
- **Ошибка I рода**: ложноположительный результат (отклонение истинной нулевой гипотезы)
- **Ошибка II рода**: ложноотрицательный результат (неотклонение ложной нулевой гипотезы)
- **Мощность теста**: вероятность правильно отклонить ложную нулевую гипотезу

### Распределения вероятностей
- **Нормальное распределение**: колоколообразная кривая, среднее = медиана = мода
- **Биномиальное распределение**: исходы типа успех/неудача
- **Распределение Пуассона**: число событий в фиксированном интервале
- **Равномерное распределение**: все исходы равновероятны
- **Экспоненциальное распределение**: время между событиями
- **t-распределение**: малые выборки, неизвестная дисперсия генеральной совокупности
- **Распределение хи-квадрат**: анализ категориальных данных

### Статистические тесты
- **t-тест**: сравнение средних двух групп
- **ANOVA**: сравнение средних нескольких групп
- **Критерий хи-квадрат**: проверка независимости категориальных переменных
- **Критерий Манна — Уитни**: непараметрическая альтернатива t-тесту
- **Корреляция Пирсона**: линейная связь между непрерывными переменными
- **Корреляция Спирмена**: монотонная связь (на основе рангов)
- **Критерий Колмогорова — Смирнова**: сравнение распределений

## Сбор и хранение данных

### Источники данных
- **Базы данных**: SQL, NoSQL, реляционные БД, документо-ориентированные хранилища
- **API**: REST, GraphQL, веб-скрейпинг
- **Файлы**: CSV, JSON, XML, Parquet, Avro
- **Потоковые данные**: Kafka, Kinesis, потоки в реальном времени
- **Опросы и эксперименты**: первичный сбор данных
- **Открытые датасеты**: государственные данные, Kaggle, академические репозитории

### Хранилища данных
- **ETL**: процесс извлечения, преобразования и загрузки
- **Озеро данных (Data Lake)**: хранение сырых данных в исходном формате
- **Хранилище данных (Data Warehouse)**: структурированные, обработанные данные для анализа
- **Витрина данных (Data Mart)**: подмножество хранилища для конкретного подразделения
- **OLAP**: многомерная аналитическая обработка, многомерные запросы
- **Звездообразная схема**: таблицы фактов, окружённые таблицами измерений
- **Снежинка**: нормализованные таблицы измерений

### Типы баз данных
- **Реляционные (SQL)**: MySQL, PostgreSQL, Oracle, SQL Server
- **Документные**: MongoDB, CouchDB (JSON-подобные документы)
- **Ключ-значение**: Redis, DynamoDB (простые пары ключ-значение)
- **Семейства столбцов**: Cassandra, HBase (оптимизированы под колоночное хранение)
- **Графовые**: Neo4j, Amazon Neptune (узлы и связи)
- **Временные ряды**: InfluxDB, TimescaleDB (данные с временными метками)
- **Векторные**: Pinecone, Milvus (хранение векторных представлений для ML)

## Предобработка данных

### Очистка данных
- **Пропущенные значения**: импутация (среднее, медиана, мода, предсказание), удаление
- **Выбросы**: обнаружение (IQR, Z-score), обработка (ограничение, преобразование)
- **Дубликаты**: выявление и удаление
- **Несогласованности**: стандартизация форматов, исправление опечаток
- **Валидация данных**: проверка ограничений, диапазонов, типов

### Преобразование данных
- **Нормализация**: масштабирование в диапазон 0-1
- **Стандартизация**: Z-score-нормализация (mean=0, std=1)
- **Кодирование**: one-hot, label, ordinal, target encoding
- **Биннинг**: группировка непрерывных значений по категориям
- **Логарифмическое преобразование**: уменьшение асимметрии
- **Масштабирование признаков**: приведение признаков к сопоставимому виду

### Инженерия признаков
- **Создание признаков**: вывод новых признаков из существующих
- **Отбор признаков**: выбор наиболее релевантных признаков
  - Методы фильтрации (корреляция, chi-square)
  - Методы-обёртки (рекурсивное исключение признаков)
  - Встроенные методы (LASSO, важность признаков в деревьях)
- **Снижение размерности**: PCA, t-SNE, UMAP
- **Признаки взаимодействия**: мультипликативное комбинирование признаков
- **Полиномиальные признаки**: создание членов более высокого порядка

## Разведочный анализ данных (EDA)

### Техники EDA
- **Сводная статистика**: описание центральной тенденции, разброса и формы
- **Одномерный анализ**: распределения одной переменной
- **Двумерный анализ**: связи между двумя переменными
- **Многомерный анализ**: взаимодействия нескольких переменных
- **Корреляционный анализ**: выявление связей и мультиколлинеарности
- **Сегментация**: группировка похожих наблюдений

### Инструменты визуализации
- **Гистограммы**: распределение одной переменной
- **Ящики с усами**: сводка по пяти числам, обнаружение выбросов
- **Диаграммы рассеяния**: связь между двумя непрерывными переменными
- **Тепловые карты**: матрицы корреляций, плотность
- **Столбчатые диаграммы**: сравнение категорий
- **Линейные графики**: тренды во времени
- **Скрипичные диаграммы**: плотность распределения с элементами box plot
- **Матрица парных диаграмм**: набор диаграмм рассеяния для пар переменных

### Библиотеки Python для EDA
- **pandas**: обработка и анализ данных
- **numpy**: численные вычисления
- **matplotlib**: базовая визуализация
- **seaborn**: статистическая визуализация
- **plotly**: интерактивные визуализации
- **scipy**: научные вычисления и статистика

## Машинное обучение в науке о данных

### Обучение с учителем
- **Регрессия**: предсказание непрерывных значений
  - Линейная регрессия
  - Полиномиальная регрессия
  - Ridge/LASSO/Elastic Net
  - Регрессор на дереве решений
  - Регрессор случайного леса
  - Градиентный бустинг (XGBoost, LightGBM, CatBoost)
  
- **Классификация**: предсказание категориальных меток
  - Логистическая регрессия
  - k-ближайших соседей
  - Naive Bayes
  - Метод опорных векторов
  - Деревья решений
  - Случайный лес
  - Градиентный бустинг
  - Нейронные сети

### Обучение без учителя
- **Кластеризация**: группировка похожих наблюдений
  - k-Means
  - Иерархическая кластеризация
  - DBSCAN (на основе плотности)
  - Модели гауссовых смесей
  - Спектральная кластеризация
  
- **Снижение размерности**: Reduce feature count
  - Principal Component Analysis (PCA)
  - t-Distributed Stochastic Neighbor Embedding (t-SNE)
  - Uniform Manifold Approximation (UMAP)
  - Autoencoders
  
- **Association Rules**: Find co-occurring items
  - Apriori Algorithm
  - FP-Growth

### Model Evaluation
- **Классификация Metrics**: Accuracy, precision, recall, F1-score, ROC-AUC, confusion matrix
- **Регрессия Metrics**: MAE, MSE, RMSE, R², Adjusted R²
- **Cross-Validation**: k-fold, stratified, leave-one-out, time series split
- **Hyperparameter Tuning**: Grid search, random search, Bayesian optimization
- **Learning Curves**: Diagnose bias-variance tradeoff

## Big Данные Technologies

### Distributed Вычисления Frameworks
- **Apache Hadoop**: MapReduce, HDFS (Hadoop Distributed File System)
- **Apache Spark**: в-memory processing, faster than Hadoop
  - Spark SQL: Структурированные данные processing
  - Spark Streaming: Real-time Данные
  - MLlib: Машинное обучение library
  - ГрафовыеX: Графовые processing
- **Apache Flink**: Stream processing с low latency
- **Apache Beam**: Unified batch и streaming

### Cloud Platforms
- **AWS**: S3, EMR, Redshift, SageMaker, Glue
- **Google Cloud**: BigQuery, Dataproc, AI Platform, Cloud Storage
- **Azure**: Synapse аналитика, Databricks, Машинное обучение, Данные Lake
- **Snowflake**: Cloud Данные warehouse

### Данные Pipeline Tools
- **Apache Airflow**: Workflow orchestration
- **Luigi**: Pipeline Управление (Spotify)
- **Prefect**: Modern workflow orchestration
- **Dagster**: Данные orchestrator с asset focus
- **dbt**: Данные transformation в warehouse

## Бизнес Intelligence и аналитика

### BI Tools
- **Tableau**: Visual analytics platform
- **Мощность теста BI**: Microsoft Бизнес analytics
- **Looker**: Данные exploration и insights (Google)
- **Qlik Sense**: Associative analytics
- **Metabase**: Open-source BI
- **Superset**: Apache open-source BI

### Dashboard Design Principles
- **Know Your Audience**: Tailor to user needs
- **Choose Right Visualizations**: Match chart to Данные type
- **Use Color Strategically**: Highlight important information
- **Maintain Consistency**: Standardize formats и scales
- **Enable Interactivity**: Filters, drill-downs, tooltips
- **Optimize Производительность**: Fast loading, efficient queries
- **Mobile Considerations**: Responsive design

### Key Производительность Indicators (KPIs)
- **Financial**: Revenue, profit margin, ROI, customer lifetime value
- **Customer**: Acquisition cost, churn rate, satisfaction score, NPS
- **Operational**: Efficiency rates, cycle time, defect rates
- **Marketing**: Conversion rates, click-through rates, attribution
- **Product**: Active users, engagement, retention, feature adoption

## Продвинутый аналитика

### Predictive аналитика
- **Forecasting**: Time series prediction (ARIMA, Prophet, LSTM)
- **Risk Modeling**: Credit scoring, fraud detection, insurance
- **Customer аналитика**: Churn prediction, propensity modeling
- **Demand Forecasting**: Inventory optimization, supply chain
- **Maintenance Prediction**: Equipment failure anticipation

### Prescriptive аналитика
- **Optimization**: Linear programming, integer programming
- **Simulation**: Monte Carlo methods, discrete event simulation
- **Decision Analysis**: Decision trees, influence diagrams
- **A/B Тестирование**: Experimental design, statistical significance
- **Multi-Armed Bandits**: Adaptive experimentation

### Text аналитика (NLP)
- **Text Preprocessing**: Tokenization, stemming, lemmatization
- **Sentiment Analysis**: Positive/negative/neutral classification
- **Topic Modeling**: LDA, NMF для theme discovery
- **Named Entity Recognition**: Identifying people, places, organizations
- **Text Классификация**: Spam detection, categorization
- **Word Embeddings**: Word2Vec, GloVe, BERT

## Данные Ethics и Governance

### Данные Privacy
- **GDPR**: EU General Данные Protection Regulation
- **CCPA**: California Consumer Privacy Act
- **HIPAA**: Health Insurance Portability и Accountability Act (US Здравоохранение)
- **Anonymization**: Removing personally identifiable information
- **Differential Privacy**: Adding noise to protect individuals
- **Consent Управление**: Opt-в/opt-out mechanisms

### Данные Quality
- **Accuracy**: Correctness из Данные
- **Completeness**: All required Данные present
- **Consistency**: No contradictions across sources
- **Timeliness**: Данные Доступно when needed
- **Validity**: Conforms to defined rules
- **Uniqueness**: No duplicates

### Bias и Fairness
- **Sampling Bias**: Non-representative Данные collection
- **Measurement Bias**: Flawed Данные collection instruments
- **Algorithmic Bias**: Discriminatory model predictions
- **Fairness Metrics**: Demographic parity, equal opportunity
- **Bias Mitigation**: Pre-processing, в-processing, post-processing

### Данные Governance Framework
- **Данные Stewardship**: Responsibility для Данные assets
- **Metadata Управление**: Данные about Данные documentation
- **Данные Lineage**: Tracking Данные flow и transformations
- **Access Control**: Role-based permissions
- **Audit Trails**: Logging Данные access и changes
- **Compliance**: Regulatory adherence

## Career Paths в наука о данных

### Roles
- **Данные Analyst**: Focus on descriptive analytics, dashboards, reporting
- **Данные Scientist**: Statistical modeling, Машинное обучение, Продвинутый analytics
- **ML Engineer**: Production ML Системы, model Развертывание, MLOps
- **Данные Engineer**: Данные pipelines, infrastructure, ETL processes
- **аналитика Manager**: Team leadership, strategy, stakeholder Управление
- **BI Developer**: Dashboard creation, report Разработка
- **Research Scientist**: Novel algorithms, publications, Продвинутый research

### Skills Matrix
- **Technical**: Python/R, SQL, Статистика, ML frameworks, cloud platforms
- **Analytical**: Problem-solving, critical thinking, experimental design
- **Коммуникация**: Storytelling, visualization, presentation skills
- **Бизнес**: Domain knowledge, stakeholder Управление, ROI analysis
- **Tools**: Git, Jupyter, Docker, CI/CD, version control для models

## Emerging Trends

### Current Developments
- **AutoML**: Automated Машинное обучение pipeline creation
- **MLOps**: DevOps practices для Машинное обучение
- **Feature Stores**: Centralized feature Управление
- **Данные Mesh**: Decentralized Данные Архитектура
- **LLMs и Generative AI**: Large Язык models, content generation
- **Edge аналитика**: Processing Данные at source devices
- **Real-Time аналитика**: Потоковые данные analysis
- **Augmented аналитика**: AI-assisted Данные preparation и insights

### Будущее Directions
- **Quantum Машинное обучение**: Quantum Вычисления для ML
- **Federated Learning**: Training models across decentralized Данные
- **Causal Inference**: Moving beyond correlation to causation
- **Responsible AI**: Ethics, explainability, transparency
- **Данные Fabric**: Integrated Данные Управление across environments
