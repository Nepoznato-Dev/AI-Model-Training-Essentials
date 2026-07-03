# Ciência de Dados e Analytics

## Conceitos Fundamentais

### O que é Ciência de Dados?
Ciência de dados é um campo interdisciplinar que usa métodos científicos, processos, algoritmos e sistemas para extrair conhecimento e insights de dados estruturados e não estruturados. Ela combina:
- **Estatística**: Base matemática para análise
- **Ciência da Computação**: Programação, algoritmos, estruturas de dados
- **Conhecimento de Domínio**: Conhecimento do assunto
- **Visualização de Dados**: Comunicação eficaz de descobertas

### Tipos de Dados
- **Dados Estruturados**: Organizados em linhas/colunas (bancos de dados, planilhas)
- **Dados Não Estruturados**: Sem formato predefinido (texto, imagens, áudio, vídeo)
- **Dados Semiestruturados**: Algum nível de organização, mas não rígido (JSON, XML, HTML)
- **Dados de Séries Temporais**: Pontos de dados sequenciais indexados em ordem temporal
- **Dados Espaciais**: Informações geográficas/baseadas em localização
- **Dados em Grafo**: Nós e arestas que representam relacionamentos

### O Processo de Ciência de Dados (CRISP-DM)
1. **Entendimento do Negócio**: Definir objetivos e requisitos
2. **Entendimento dos Dados**: Coletar e explorar os dados iniciais
3. **Preparação dos Dados**: Limpar, transformar e formatar os dados (80% do trabalho)
4. **Modelagem**: Selecionar e aplicar técnicas de modelagem
5. **Avaliação**: Medir o desempenho do modelo em relação aos objetivos
6. **Implantação**: Implementar o modelo em ambiente de produção

## Fundamentos de Estatística

### Estatística Descritiva
- **Medidas de Tendência Central**: Média, mediana, moda
- **Medidas de Dispersão**: Amplitude, variância, desvio padrão, intervalo interquartil
- **Forma da Distribuição**: Assimetria (skewness), curtose (kurtosis)
- **Percentis e Quartis**: Posição dentro da distribuição

### Estatística Inferencial
- **Teste de Hipóteses**: Hipótese nula, hipótese alternativa, p-values
- **Intervalos de Confiança**: Faixa de valores que provavelmente contém o parâmetro populacional
- **Significância Estatística**: Probabilidade de os resultados terem ocorrido ao acaso
- **Erro Tipo I**: Falso positivo (rejeitar uma hipótese nula verdadeira)
- **Erro Tipo II**: Falso negativo (não rejeitar uma hipótese nula falsa)
- **Poder Estatístico**: Probabilidade de rejeitar corretamente uma hipótese nula falsa

### Distribuições de Probabilidade
- **Distribuição Normal**: Curva em sino, média = mediana = moda
- **Distribuição Binomial**: Resultados de sucesso/falha
- **Distribuição de Poisson**: Contagem de eventos em um intervalo fixo
- **Distribuição Uniforme**: Todos os resultados são igualmente prováveis
- **Distribuição Exponencial**: Tempo entre eventos
- **Distribuição t**: Tamanhos de amostra pequenos, variância populacional desconhecida
- **Distribuição Qui-Quadrado**: Análise de dados categóricos

### Testes Estatísticos
- **t-test**: Comparar médias entre dois grupos
- **ANOVA**: Comparar médias entre múltiplos grupos
- **Chi-Square Test**: Testar independência entre variáveis categóricas
- **Mann-Whitney U**: Alternativa não paramétrica ao t-test
- **Pearson Correlation**: Relação linear entre variáveis contínuas
- **Spearman Correlation**: Relação monotônica (baseada em ranking)
- **Kolmogorov-Smirnov**: Comparar distribuições

## Coleta e Armazenamento de Dados

### Fontes de Dados
- **Bancos de Dados**: SQL, NoSQL, relacionais, document stores
- **APIs**: REST, GraphQL, web scraping
- **Arquivos**: CSV, JSON, XML, Parquet, Avro
- **Dados em Streaming**: Kafka, Kinesis, feeds em tempo real
- **Pesquisas e Experimentos**: Coleta primária de dados
- **Datasets Públicos**: Dados governamentais, Kaggle, repositórios acadêmicos

### Data Warehousing
- **ETL**: Processo de Extract, Transform, Load
- **Data Lake**: Armazenamento de dados brutos em formato nativo
- **Data Warehouse**: Dados estruturados e processados para análise
- **Data Mart**: Subconjunto do warehouse para um departamento específico
- **OLAP**: Online Analytical Processing, consultas multidimensionais
- **Star Schema**: Tabelas fato cercadas por tabelas dimensão
- **Snowflake Schema**: Tabelas dimensão normalizadas

### Tipos de Banco de Dados
- **Relacional (SQL)**: MySQL, PostgreSQL, Oracle, SQL Server
- **Document**: MongoDB, CouchDB (documentos no estilo JSON)
- **Key-Value**: Redis, DynamoDB (pares simples de chave e valor)
- **Column-Family**: Cassandra, HBase (otimizados para colunas)
- **Graph**: Neo4j, Amazon Neptune (nós e relacionamentos)
- **Time-Series**: InfluxDB, TimescaleDB (dados com timestamp)
- **Vector**: Pinecone, Milvus (armazenamento de embeddings para ML)

## Pré-processamento de Dados

### Limpeza de Dados
- **Valores Ausentes**: Imputação (média, mediana, moda, predição), exclusão
- **Outliers**: Detecção (IQR, Z-score), tratamento (capping, transformação)
- **Duplicatas**: Identificação e remoção
- **Inconsistências**: Padronização de formatos, correção de erros de digitação
- **Validação de Dados**: Verificação de restrições, faixas e tipos

### Transformação de Dados
- **Normalization**: Escalonamento para a faixa 0-1
- **Standardization**: Normalização por Z-score (média=0, desvio padrão=1)
- **Encoding**: One-hot, label, ordinal, target encoding
- **Binning**: Agrupamento de valores contínuos em categorias
- **Log Transformation**: Redução da assimetria
- **Feature Scaling**: Tornar features comparáveis

### Feature Engineering
- **Criação de Features**: Derivar novas features a partir das existentes
- **Seleção de Features**: Escolher as features mais relevantes
  - Métodos de filtro (correlação, chi-square)
  - Métodos wrapper (recursive feature elimination)
  - Métodos embutidos (LASSO, importância baseada em árvores)
- **Redução de Dimensionalidade**: PCA, t-SNE, UMAP
- **Termos de Interação**: Combinar features de forma multiplicativa
- **Polynomial Features**: Criar termos de ordem superior

## Análise Exploratória de Dados (EDA)

### Técnicas de EDA
- **Estatísticas Resumo**: Descrever tendência central, dispersão e forma
- **Análise Univariada**: Distribuições de uma única variável
- **Análise Bivariada**: Relações entre duas variáveis
- **Análise Multivariada**: Interações entre múltiplas variáveis
- **Análise de Correlação**: Identificar relações e multicolinearidade
- **Segmentação**: Agrupar observações semelhantes

### Ferramentas de Visualização
- **Histogramas**: Distribuição de uma única variável
- **Box Plots**: Resumo de cinco números, detecção de outliers
- **Scatter Plots**: Relação entre duas variáveis contínuas
- **Heatmaps**: Matrizes de correlação, densidade
- **Bar Charts**: Comparações categóricas
- **Line Charts**: Tendências ao longo do tempo
- **Violin Plots**: Densidade da distribuição com elementos de box plot
- **Pair Plots**: Múltiplos scatter plots para pares de variáveis

### Bibliotecas Python para EDA
- **pandas**: Manipulação e análise de dados
- **numpy**: Computação numérica
- **matplotlib**: Plotagem básica
- **seaborn**: Visualização estatística
- **plotly**: Visualizações interativas
- **scipy**: Computação científica e estatística

## Machine Learning em Ciência de Dados

### Aprendizado Supervisionado
- **Regression**: Prever valores contínuos
  - Linear Regression
  - Polynomial Regression
  - Ridge/LASSO/Elastic Net
  - Decision Tree Regressor
  - Random Forest Regressor
  - Gradient Boosting (XGBoost, LightGBM, CatBoost)
  
- **Classification**: Prever rótulos categóricos
  - Logistic Regression
  - k-Nearest Neighbors
  - Naive Bayes
  - Support Vector Machines
  - Decision Trees
  - Random Forest
  - Gradient Boosting
  - Neural Networks

### Aprendizado Não Supervisionado
- **Clustering**: Agrupar observações semelhantes
  - k-Means
  - Hierarchical Clustering
  - DBSCAN (baseado em densidade)
  - Gaussian Mixture Models
  - Spectral Clustering
  
- **Redução de Dimensionalidade**: Reduzir o número de features
  - Principal Component Analysis (PCA)
  - t-Distributed Stochastic Neighbor Embedding (t-SNE)
  - Uniform Manifold Approximation (UMAP)
  - Autoencoders
  
- **Association Rules**: Encontrar itens que ocorrem juntos
  - Apriori Algorithm
  - FP-Growth

### Avaliação de Modelos
- **Métricas de Classificação**: Accuracy, precision, recall, F1-score, ROC-AUC, confusion matrix
- **Métricas de Regressão**: MAE, MSE, RMSE, R², Adjusted R²
- **Cross-Validation**: k-fold, estratificada, leave-one-out, time series split
- **Hyperparameter Tuning**: Grid search, random search, Bayesian optimization
- **Learning Curves**: Diagnosticar o tradeoff bias-variance

## Tecnologias de Big Data

### Frameworks de Computação Distribuída
- **Apache Hadoop**: MapReduce, HDFS (Hadoop Distributed File System)
- **Apache Spark**: Processamento em memória, mais rápido que o Hadoop
  - Spark SQL: Processamento de dados estruturados
  - Spark Streaming: Dados em tempo real
  - MLlib: Biblioteca de machine learning
  - GraphX: Processamento de grafos
- **Apache Flink**: Processamento de streams com baixa latência
- **Apache Beam**: Batch e streaming unificados

### Plataformas de Nuvem
- **AWS**: S3, EMR, Redshift, SageMaker, Glue
- **Google Cloud**: BigQuery, Dataproc, AI Platform, Cloud Storage
- **Azure**: Synapse Analytics, Databricks, Machine Learning, Data Lake
- **Snowflake**: Data warehouse em nuvem

### Ferramentas de Data Pipeline
- **Apache Airflow**: Orquestração de workflows
- **Luigi**: Gerenciamento de pipelines (Spotify)
- **Prefect**: Orquestração moderna de workflows
- **Dagster**: Orquestrador de dados com foco em assets
- **dbt**: Transformação de dados no warehouse

## Business Intelligence e Analytics

### Ferramentas de BI
- **Tableau**: Plataforma de analytics visual
- **Power BI**: Analytics de negócios da Microsoft
- **Looker**: Exploração de dados e insights (Google)
- **Qlik Sense**: Analytics associativo
- **Metabase**: BI open-source
- **Superset**: BI open-source da Apache

### Princípios de Design de Dashboards
- **Conheça seu Público**: Adapte-se às necessidades do usuário
- **Escolha as Visualizações Certas**: Relacione o gráfico ao tipo de dado
- **Use Cor de Forma Estratégica**: Destaque informações importantes
- **Mantenha Consistência**: Padronize formatos e escalas
- **Habilite Interatividade**: Filtros, drill-downs, tooltips
- **Otimize o Desempenho**: Carregamento rápido, consultas eficientes
- **Considerações Mobile**: Design responsivo

### Key Performance Indicators (KPIs)
- **Financial**: Revenue, profit margin, ROI, customer lifetime value
- **Customer**: Acquisition cost, churn rate, satisfaction score, NPS
- **Operational**: Efficiency rates, cycle time, defect rates
- **Marketing**: Conversion rates, click-through rates, attribution
- **Product**: Active users, engagement, retention, feature adoption

## Analytics Avançado

### Predictive Analytics
- **Forecasting**: Predição de séries temporais (ARIMA, Prophet, LSTM)
- **Risk Modeling**: Credit scoring, detecção de fraude, seguros
- **Customer Analytics**: Predição de churn, propensity modeling
- **Demand Forecasting**: Otimização de inventário, supply chain
- **Maintenance Prediction**: Antecipação de falhas de equipamentos

### Prescriptive Analytics
- **Optimization**: Programação linear, programação inteira
- **Simulation**: Métodos de Monte Carlo, simulação de eventos discretos
- **Decision Analysis**: Árvores de decisão, influence diagrams
- **A/B Testing**: Design experimental, significância estatística
- **Multi-Armed Bandits**: Experimentação adaptativa

### Text Analytics (NLP)
- **Text Preprocessing**: Tokenization, stemming, lemmatization
- **Sentiment Analysis**: Classificação positiva/negativa/neutra
- **Topic Modeling**: LDA, NMF para descoberta de temas
- **Named Entity Recognition**: Identificação de pessoas, lugares e organizações
- **Text Classification**: Detecção de spam, categorização
- **Word Embeddings**: Word2Vec, GloVe, BERT

## Ética e Governança de Dados

### Privacidade de Dados
- **GDPR**: EU General Data Protection Regulation
- **CCPA**: California Consumer Privacy Act
- **HIPAA**: Health Insurance Portability and Accountability Act (saúde nos EUA)
- **Anonymization**: Remoção de informações pessoalmente identificáveis
- **Differential Privacy**: Adição de ruído para proteger indivíduos
- **Consent Management**: Mecanismos de opt-in/opt-out

### Qualidade de Dados
- **Accuracy**: Correção dos dados
- **Completeness**: Todos os dados necessários presentes
- **Consistency**: Sem contradições entre fontes
- **Timeliness**: Dados disponíveis quando necessário
- **Validity**: Conformidade com regras definidas
- **Uniqueness**: Ausência de duplicatas

### Viés e Fairness
- **Sampling Bias**: Coleta de dados não representativa
- **Measurement Bias**: Instrumentos de coleta de dados falhos
- **Algorithmic Bias**: Predições discriminatórias do modelo
- **Fairness Metrics**: Demographic parity, equal opportunity
- **Bias Mitigation**: Pre-processing, in-processing, post-processing

### Framework de Governança de Dados
- **Data Stewardship**: Responsabilidade pelos ativos de dados
- **Metadata Management**: Documentação sobre os dados
- **Data Lineage**: Rastreamento do fluxo e das transformações dos dados
- **Access Control**: Permissões baseadas em papéis
- **Audit Trails**: Registro de acessos e alterações nos dados
- **Compliance**: Conformidade regulatória

## Carreiras em Ciência de Dados

### Papéis
- **Data Analyst**: Foco em analytics descritivo, dashboards e relatórios
- **Data Scientist**: Modelagem estatística, machine learning, analytics avançado
- **ML Engineer**: Sistemas de ML em produção, implantação de modelos, MLOps
- **Data Engineer**: Pipelines de dados, infraestrutura, processos de ETL
- **Analytics Manager**: Liderança de equipe, estratégia, gestão de stakeholders
- **BI Developer**: Criação de dashboards, desenvolvimento de relatórios
- **Research Scientist**: Novos algoritmos, publicações, pesquisa avançada

### Matriz de Habilidades
- **Technical**: Python/R, SQL, estatística, frameworks de ML, plataformas de nuvem
- **Analytical**: Resolução de problemas, pensamento crítico, design experimental
- **Communication**: Storytelling, visualização, habilidades de apresentação
- **Business**: Conhecimento de domínio, gestão de stakeholders, análise de ROI
- **Tools**: Git, Jupyter, Docker, CI/CD, version control para modelos

## Tendências Emergentes

### Desenvolvimentos Atuais
- **AutoML**: Criação automatizada de pipelines de machine learning
- **MLOps**: Práticas de DevOps para machine learning
- **Feature Stores**: Gerenciamento centralizado de features
- **Data Mesh**: Arquitetura de dados descentralizada
- **LLMs and Generative AI**: Large language models, geração de conteúdo
- **Edge Analytics**: Processamento de dados nos dispositivos de origem
- **Real-Time Analytics**: Análise de dados em streaming
- **Augmented Analytics**: Preparação de dados e insights assistidos por IA

### Direções Futuras
- **Quantum Machine Learning**: Computação quântica para ML
- **Federated Learning**: Treinamento de modelos em dados descentralizados
- **Causal Inference**: Ir além da correlação rumo à causalidade
- **Responsible AI**: Ética, explicabilidade, transparência
- **Data Fabric**: Gerenciamento integrado de dados entre ambientes
