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
# Ciência de Dados e Análise
A ciência de dados é a disciplina que transforma dados brutos em insights acionáveis. Situa-se na intersecção entre estatísticas, ciência da computação e conhecimentos especializados – e tornou-se essencial em todos os setores, desde finanças até cuidados de saúde. Este arquivo apresenta os principais conceitos, ferramentas e fluxos de trabalho que todo profissional deve conhecer.
---

## O Processo de Ciência de Dados
A maioria dos projetos segue alguma variação do **CRISP-DM**, o ciclo de vida padrão do setor:
| Fase | O que acontece | Horário típico |
|-------|------------|-------------|
| **Entendimento Empresarial** | Definir objetivos, métricas de sucesso e restrições | 10–15% |
| **Entendimento de dados** | Colete, explore e crie o perfil dos dados | 10–15% |
| **Preparação de dados** | Limpe, transforme e projete recursos | ~50–60% |
| **Modelagem** | Selecionar e treinar modelos | 10–15% |
| **Avaliação** | Avalie o desempenho em relação às metas de negócios | 5–10% |
| **Implantação** | Envie o modelo para produção | 5–10% |
Estima-se que a preparação de dados, especialmente a limpeza de dados, consuma cerca de 80% do tempo de um cientista de dados.
---

## Visão geral dos tipos de dados
| Tipo | Descrição | Exemplo |
|------|-------------|---------|
| **Estruturado** | Organizado em linhas e colunas | Tabelas SQL, planilhas |
| **Não estruturado** | Nenhum formato predefinido | Texto, imagens, áudio, vídeo |
| **Semiestruturado** | Alguma organização, mas flexível | JSON, XML, HTML |
| **Série temporal** | Dados sequenciais indexados por tempo | Preços das ações, leituras de sensores |
| **Espacial** | Geográfico ou baseado em localização | Coordenadas GPS, dados cartográficos |
| **Gráfico** | Nós e arestas representando relacionamentos | Redes sociais, gráficos de conhecimento |
---

## Fundamentos de Estatística
### Estatísticas Descritivas vs Inferenciais
As estatísticas descritivas resumem o que você *tem*; estatísticas inferenciais permitem tirar conclusões sobre o que você *não* tem (a população em geral).
| Conceito | Ideias-chave |
|--------|-----------|
| **Tendência central** | Média (sensível a valores discrepantes), mediana (robusta), moda (mais frequente) |
| **Dispersão** | Intervalo, variância, desvio padrão, intervalo interquartil |
| **Forma de distribuição** | Skewness (assimetria), curtose (peso da cauda) |
| **Teste de hipóteses** | Hipótese nula vs alternativa, valores de p, nível de significância (α) |
| **Intervalos de confiança** | Intervalo que provavelmente contém o verdadeiro parâmetro populacional |
| **Erros Tipo I/Tipo II** | Falso positivo (rejeitando um verdadeiro nulo) / falso negativo (faltando um efeito real) |
### Testes estatísticos comuns
| Teste | Quando usar |
|------|-------------|
| **teste t** | Compare médias entre dois grupos |
| **ANOVA** | Comparar médias entre três ou mais grupos |
| **Qui-quadrado** | Teste de independência de variáveis ​​categóricas |
| **Mann-Whitney U** | Alternativa não paramétrica ao teste t (sem pressuposto de normalidade) |
| **Correlação de Pearson** | Relação linear entre duas variáveis ​​contínuas |
| **Correlação de Spearman** | Relacionamento monotônico (baseado em classificação, mais robusto) |
### Distribuições de probabilidade que vale a pena conhecer
| Distribuição | Caso de uso |
|------------|----------|
| **Normal** | Fenômenos naturais, erros de medição — a clássica curva em sino |
| **Binômio** | Contagens de sucesso/fracasso (moedas lançadas, taxas de conversão) |
| **Poison** | Contagens de eventos em intervalo fixo (chamadas por hora, defeitos por lote) |
| **Exonencial** | Tempo entre eventos (tempos de espera, intervalos de falha) |
| **Distribuição t** | Amostras pequenas ou variância populacional desconhecida |
| **Qui-quadrado** | Análise de dados categóricos, testes de adequação |
---

## Coleta e armazenamento de dados
### De onde vêm os dados
Os dados do mundo real chegam de muitas fontes: bancos de dados relacionais, APIs (REST, GraphQL), arquivos simples (CSV, JSON, Parquet), plataformas de streaming (Kafka, Kinesis), pesquisas e repositórios públicos (Kaggle, portais governamentais). O formato que você recebe determina grande parte da sua estratégia de pré-processamento.
### Conceitos de armazenamento de dados
| Conceito | Descrição |
|--------|-------------|
| **ETL** | Extrair → Transformar → Carregar — abordagem tradicional de pipeline |
| **ELT** | Extrair → Carregar → Transformar — abordagem moderna de nuvem (carregar bruto, transformar no armazém) |
| **Lago de Dados** | Dados brutos armazenados em formato nativo (schema-on-read) |
| **Armazém de Dados** | Dados estruturados e processados ​​otimizados para análise (schema-on-write) |
| **DataMart** | Um subconjunto de um warehouse com escopo para um departamento ou domínio |
| **Esquema em estrela** | Tabela central de fatos cercada por tabelas de dimensões |
| **Esquema de floco de neve** | Tabelas de dimensões normalizadas (menos redundância, mais junções) |
### Tipos de banco de dados
| Tipo | Exemplos | Melhor para |
|------|----------|----------|
| **Relacional (SQL)** | PostgreSQL, MySQL, Oracle | Dados estruturados, transações ACID |
| **Documento** | MongoDB, CouchDB | Esquemas flexíveis, dados semelhantes a JSON |
| **Valor-chave** | Redis, DynamoDB | Cache, sessões, pesquisas simples |
| **Coluna-Família** | Cassandra, HBase | Cargas de trabalho com uso intenso de gravação, séries temporais |
| **Gráfico** | Neo4j, Amazon Netuno | Relacionamentos, redes sociais |
| **Série temporal** | InfluxDB, TimescaleDB | Métricas de IoT, monitoramento |
| **Vetor** | Pinha, Milvus | Incorporando armazenamento para pesquisa de ML/AI |
---

## Pré-processamento de dados e engenharia de recursos
### Lista de verificação de limpeza
Todo conjunto de dados real tem problemas. Aqui está a limpeza padrão:
| Edição | Abordagem |
|-------|----------|
| **Valores ausentes** | Imputação (média, mediana, previsão) ou eliminação, se escassa |
| **Outliers** | Detectar via IQR ou Z-score; tratar com capeamento ou transformação |
| **Duplicados** | Identificar e remover |
| **Inconsistências** | Padronize formatos, corrija erros de digitação, normalize unidades |
### Técnicas de Transformação
| Técnica | O que faz |
|-----------|------------|
| **Normalização** | Dimensiona os valores para o intervalo de 0 a 1 |
| **Padronização** | Escore Z: média = 0, padrão = 1 |
| **Codificação one-hot** | Converte categorias em colunas binárias |
| **Codificação de etiqueta** | Atribui rótulos inteiros às categorias |
| **Transformação de log** | Reduz a distorção à direita nos dados |
| **Binning** | Agrupa valores contínuos em intervalos discretos |
### Engenharia de recursos
A engenharia de recursos costuma ser a diferença entre um modelo medíocre e um excelente. As principais técnicas incluem:
- **Criação de recurso**: derivar novas colunas de colunas existentes (por exemplo,`age_group`de`age`).
- **Seleção de recursos**: Métodos de filtro (correlação), métodos wrapper (eliminação recursiva), métodos incorporados (LASSO, importância da árvore).
- **Redução de dimensionalidade**: PCA para linear, t-SNE ou UMAP para visualização.
- **Termos de interação**: Combinar recursos multiplicativamente para capturar efeitos conjuntos.
---

## Análise Exploratória de Dados (EDA)
EDA é onde você desenvolve intuição sobre seus dados antes da modelagem. O objetivo é detectar padrões, anomalias e relacionamentos.
### Escolhendo o gráfico certo
| Tipo de gráfico | Melhor para |
|-----------|----------|
| **Histograma** | Distribuição de uma única variável |
| **Gráfico de caixa** | Resumo de cinco números, detecção de valores discrepantes |
| **Gráfico de dispersão** | Relação entre duas variáveis ​​contínuas |
| **Mapa de calor** | Matrizes de correlação, visualização de densidade |
| **Gráfico de barras** | Comparando categorias |
| **Gráfico de linhas** | Tendências ao longo do tempo |
| **Enredo de violino** | Densidade de distribuição + resumo do box plot |
| **Gráfico de pares** | Visão geral rápida de todos os pares de variáveis ​​|
### A pilha Python EDA
| Biblioteca | Função |
|--------|------|
| **pandas** | Manipulação e análise de dados |
| **entorpecido** | Computação numérica |
| **matplotlib** | Plotagem de fundação |
| **Nascido no mar** | Visualização estatística (construída em matplotlib) |
| **enredo** | Visualizações interativas baseadas na web |
| **scipy** | Computação científica e estatística |
---

## Aprendizado de máquina em ciência de dados
### Visão geral da aprendizagem supervisionada
| Tarefa | Algoritmos |
|------|-----------|
| **Regressão** (prever um número) | Linear, Ridge/LASSO, Árvore de Decisão, Floresta Aleatória, Gradient Boosting (XGBoost, LightGBM) |
| **Classificação** (prever uma categoria) | Regressão Logística, k-NN, Naive Bayes, SVM, Árvores de Decisão, Floresta Aleatória, Redes Neurais |
### Visão geral da aprendizagem não supervisionada
| Tarefa | Algoritmos |
|------|-----------|
| **Agrupamento** | k-Médias, Hierárquicas, DBSCAN, Modelos de Mistura Gaussiana |
| **Redução de Dimensionalidade** | PCA, t-SNE, UMAP, Autoencoders |
| **Regras de Associação** | A priori, FP-Crescimento |
### Avaliação do modelo
| Tipo de métrica | Principais métricas |
|------------|------------|
| **Classificação** | Precisão, precisão, recall, pontuação F1, ROC-AUC, matriz de confusão |
| **Regressão** | MAE, MSE, RMSE, R², R² Ajustado |
| **Validação** | validação cruzada k-fold, estratificada, divisão de série temporal |
| **Ajuste** | Pesquisa em grade, pesquisa aleatória, otimização bayesiana |
---

## Tecnologias de Big Data
Quando os conjuntos de dados excedem o que uma única máquina pode suportar, a computação distribuída entra em cena.
| Estrutura | Força |
|-----------|----------|
| **Apache Spark** | Processamento na memória; Spark SQL, Streaming, MLlib, GraphX ​​|
| **Apache Hadoop** | MapReduce + HDFS — a pilha original de big data |
| **Apache Flink** | Processamento de fluxo de baixa latência |
| **Apache Beam** | Modelo unificado de lote e streaming |
### Plataformas de dados em nuvem
| Provedor | Principais serviços |
|----------|------------|
| **AWS** | S3, EMR, Redshift, SageMaker, Cola |
| **Google Nuvem** | BigQuery, Dataproc, plataforma de IA, armazenamento em nuvem |
| **Azul** | Synapse Analytics, Databricks, Machine Learning, Data Lake |
| **Floco de neve** | Data warehouse nativo da nuvem (independente de provedor) |
### Orquestração de pipeline
| Ferramenta | Notas |
|------|-------|
| **Fluxo de ar Apache** | Padrão da indústria; DAGs baseados em Python |
| **Prefeito** | Alternativa moderna com API mais limpa |
| **Punhal** | Orquestração centrada em ativos |
| **dbt** | Transformação de dados SQL primeiro no armazém |
---

## Inteligência de Negócios e Análise
### Ferramentas de BI comparadas
| Ferramenta | Tipo | Força |
|------|------|----------|
| **Quadro** | Comercial | Análise visual avançada, arrastar e soltar |
| **Power BI** | Comercial (Microsoft) | Integração profunda Office/Azure |
| **Olhador** | Comercial (Google) | Exploração de dados, modelagem LookML |
| **Metabase** | Código aberto | Configuração fácil, nativo de SQL |
| **Superconjunto** | Código aberto (Apache) | Escalável, SQL primeiro |
### Princípios de design do painel
Painéis eficazes seguem princípios estabelecidos: identificar o público, escolher a visualização apropriada para cada métrica, usar cores estrategicamente (não decorativamente), manter escalas consistentes e permitir interatividade (filtros, detalhamentos). O desempenho também é importante: painéis com tempos de carregamento lentos reduzem a adoção pelo usuário.
### Categorias de KPI comuns
| Categoria | Exemplos |
|----------|---------|
| **Financeiro** | Receita, margem de lucro, ROI, valor da vida do cliente |
| **Cliente** | Custo de aquisição (CAC), taxa de rotatividade, NPS, índice de satisfação |
| **Operacional** | Taxas de eficiência, tempo de ciclo, taxas de defeitos |
| **Marketing** | Taxa de conversão, taxa de cliques, ROAS, atribuição |
| **Produto** | Usuários ativos diariamente, engajamento, retenção, adoção de recursos |
---

## Análise Avançada
| Abordagem | Técnicas | Quando usar |
|----------|-----------|------------|
| **Preditivo** | Séries temporais (ARIMA, Prophet, LSTM), modelagem de risco, previsão de rotatividade | Previsão de valores futuros |
| **Prescritivo** | Programação linear, simulação de Monte Carlo, testes A/B, bandidos multi-armados | Otimizando decisões |
| **Análise de texto** | Tokenização, análise de sentimento, modelagem de tópicos (LDA), NER, embeddings de palavras (Word2Vec, BERT) | Extraindo insights do texto |
---

## Ética e Governança de Dados
### Regulamentos de Privacidade
| Regulamento | Escopo |
|-----------|-------|
| **RGPD** | Titulares dos dados da UE; direito ao apagamento, consentimento, portabilidade de dados |
| **CCPA** | Consumidores da Califórnia; cancelamento de vendas de dados |
| **HIPAA** | Dados de saúde dos EUA; regras rigorosas de confidencialidade |
### Dimensões de qualidade de dados
| Dimensão | Pergunta |
|-----------|----------|
| **Precisão** | Os dados estão corretos? |
| **Completude** | Está faltando alguma coisa? |
| **Consistência** | As fontes concordam? |
| **Oportunidade** | É atual? |
| **Validade** | Está em conformidade com os formatos esperados? |
| **Singularidade** | Existem duplicatas? |
### Preconceito e justiça
O viés pode ocorrer em qualquer estágio: viés de amostragem (dados não representativos), viés de medição (instrumentos falhos) ou viés algorítmico (previsões discriminatórias). As estratégias de mitigação incluem pré-processamento (corrigir os dados), processamento (restringir o modelo) e pós-processamento (ajustar os resultados). Métricas de justiça, como paridade demográfica e igualdade de oportunidades, ajudam a quantificar o problema.
---

## Planos de carreira
| Função | Foco |
|------|-------|
| **Analista de Dados** | Análise descritiva, painéis, relatórios |
| **Cientista de Dados** | Modelagem estatística, ML, análise avançada |
| **Engenheiro de ML** | Sistemas de ML de produção, implantação de modelo, MLOps |
| **Engenheiro de Dados** | Pipelines de dados, infraestrutura, ETL |
| **Gerente de análise** | Liderança de equipes, estratégia, gestão de stakeholders |
| **Cientista pesquisador** | Novos algoritmos, publicações |
---

## Tendências emergentes
- **AutoML**: criação automatizada de pipeline e seleção de modelo.
- **MLOps**: práticas DevOps aplicadas ao gerenciamento do ciclo de vida de ML.
- **Feature Stores**: gerenciamento centralizado de recursos para reutilização entre equipes.
- **Data Mesh**: arquitetura de dados descentralizada e de propriedade do domínio.
- **LLMs e IA generativa**: grandes modelos de linguagem que transformam fluxos de trabalho de texto, código e imagem.
- **Edge Analytics**: processamento de dados no dispositivo, e não na nuvem.
- **Inferência causal**: ir além da correlação para compreender a causa e o efeito reais.
- **Aprendizagem Federada**: modelos de treinamento em dados descentralizados sem movê-los.
- **IA responsável**: Ética, explicabilidade e transparência tornam-se requisitos padrão.