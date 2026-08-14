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
# Engenharia de dados e pipelines
A engenharia de dados é a disciplina de construção de sistemas que movem, transformam e armazenam dados em escala. Sem pipelines de dados confiáveis, os modelos de aprendizado de máquina não podem ser treinados, os painéis mostram números obsoletos e as decisões de negócios são baseadas em suposições. Este arquivo cobre a arquitetura, as ferramentas e as práticas para construir uma infraestrutura de dados que funcione.
---

## ETL x ELT
| Abordagem | Como funciona | Melhor para | Ferramentas |
|----------|------------|----------|-------|
| **ETL** (Extrair → Transformar → Carregar) | Transforme os dados *antes* de carregá-los no armazém | Armazéns tradicionais com computação limitada | Informatica, Talend, Apache NiFi |
| **ELT** (Extrair → Carregar → Transformar) | Carregue os dados brutos primeiro; transformar *dentro* do armazém | Armazéns em nuvem modernos com computação elástica | dbt, Fivetran, Airbyte + BigQuery/Snowflake |
A mudança de ETL para ELT foi impulsionada por data warehouses em nuvem (BigQuery, Snowflake, Redshift) que podem dimensionar a computação independentemente do armazenamento. Não há mais necessidade de pré-processar tudo antes de carregar.
---

## Data Lakes x Data Warehouses
| Recurso | Lago de dados | Armazém de dados |
|--------|-----------|---------------|
| **Formato de dados** | Formato bruto e nativo (esquema na leitura) | Estruturado, processado (schema-on-write) |
| **Esquema** | Definido no momento da consulta | Definido antes do carregamento |
| **Tipos de dados** | Estruturados, semiestruturados, não estruturados | Principalmente estruturado |
| **Usuários** | Cientistas de dados, engenheiros | Analistas de negócios, ferramentas de BI |
| **Custo** | Armazenamento mais barato (armazenamento de objetos) | Mais caro (otimizado para consultas) |
| **Exemplos** | AWS S3, Azure Data Lake, GCS | Floco de neve, BigQuery, Redshift |
A abordagem moderna é a **lakehouse**: combina o armazenamento barato e flexível de um lago com os recursos de gerenciamento e desempenho de um armazém. Delta Lake, Apache Iceberg e Apache Hudi são as principais tecnologias aqui.
---

## Arquitetura de pipeline
### Lote vs Streaming
| Modo | Descrição | Latência | Caso de uso |
|------|-------------|---------|----------|
| **Lote** | Processar dados em grandes blocos em intervalos programados | Minutos em horas | Relatórios diários, jobs ETL, enriquecimento de dados |
| **Transmissão** | Processar dados continuamente à medida que chegam | Milissegundos em segundos | Painéis em tempo real, detecção de fraudes, alertas |
| **Microlote** | Pequenos lotes em intervalos muito curtos | Segundos | Quase em tempo real com simplicidade de lote |
### Componentes do pipeline
Um pipeline de dados típico tem estes estágios:
| Palco | Descrição | Ferramentas |
|-------|-------------|-------|
| **Ingestão** | Coletar dados de fontes | Kafka, Airbyte, Fivetran, Debezium |
| **Transformação** | Limpar, enriquecer, agregar | dbt, faísca, pandas |
| **Armazenamento** | Persistir dados processados ​​| BigQuery, floco de neve, S3, Delta Lake |
| **Servindo** | Disponibilizar dados aos consumidores | APIs, painéis, armazenamentos de recursos de ML |
| **Orquestração** | Agendar e gerenciar dependências | Fluxo de ar, prefeito, Dagster |
| **Monitoramento** | Acompanhe a integridade do pipeline e a qualidade dos dados | Grandes Esperanças, Monte Carlo, alertas personalizados |
---

## Ferramentas de orquestração
| Ferramenta | Abordagem | Força |
|------|----------|----------|
| **Fluxo de ar Apache** | DAGs baseados em Python; padrão da indústria | Enorme ecossistema, maduro, flexível |
| **Prefeito** | Nativo de Python; API mais limpa que o Airflow | Design moderno, ótimo tratamento de erros |
| **Punhal** | Centrado em ativos; abordagem de engenharia de software | Sistema de tipos, testes, observabilidade |
| **Luigi** | Ferramenta de pipeline original do Spotify | Simples, mas menos desenvolvido |
### Exemplo de fluxo de ar
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

##Apache Kafka
Kafka é a espinha dorsal de muitos sistemas de dados em tempo real. É um log de eventos distribuído que fornece mensagens de alto rendimento e tolerantes a falhas.
### Conceitos Básicos
| Conceito | Descrição |
|--------|-------------|
| **Tópico** | Uma categoria de mensagens (por exemplo,`orders`,`user-events`) |
| **Partição** | Os tópicos são divididos em partições para paralelismo |
| **Produtor** | Aplicativo que grava mensagens em tópicos |
| **Consumidor** | Aplicativo que lê mensagens de tópicos |
| **Grupo de Consumidores** | Grupo de consumidores que compartilham a carga de leitura de um tema |
| **Compensação** | Posição de um consumidor numa divisória |
| **Corretor** | Um nó de servidor Kafka |
### Quando usar Kafka
- **Streaming de eventos**: processamento de eventos em tempo real em grande escala.
- **Serviços de dissociação**: produtores e consumidores não precisam se conhecer.
- **Replay**: As mensagens são retidas; os consumidores podem reler a partir de qualquer deslocamento.
- **Contrapressão**: Kafka lida naturalmente com diferenças de velocidade entre produtores e consumidores.
---

## Modelagem de dados
### Esquema estrela vs esquema floco de neve
| Esquema | Estrutura | Prós | Contras |
|--------|-----------|------|------|
| **Estrela** | Tabela de fatos central cercada por tabelas de dimensões desnormalizadas | Consultas simples, leituras rápidas | Redundância de dados |
| **Floco de neve** | As tabelas de dimensões são normalizadas (divididas em subtabelas) | Menos redundância | Mais junções, consultas mais lentas |
### Tabelas de fatos e dimensões
| Tipo de tabela | Contém | Exemplo |
|----------|----------|--------|
| **Fato** | Eventos mensuráveis ​​(métricas) | `orders`(order_id, product_id, customer_id, quantidade, data) |
| **Dimensão** | Atributos descritivos | `products`(id_produto, nome, categoria, preço),`customers`(id_cliente, nome, cidade) |
---

## Lojas de recursos
Um feature store é um repositório centralizado de recursos de ML — os valores derivados usados ​​como entrada para modelos (por exemplo, “valor médio do pedido do usuário nos últimos 30 dias”).
| Capacidade | Descrição |
|-----------|------------|
| **Registro de recursos** | Catálogo de funcionalidades disponíveis com metadados |
| **Loja off-line** | Recursos históricos para treinamento de modelo (lote) |
| **Loja On-line** | Recurso de baixa latência servindo para inferência em tempo real |
| **Monitoramento de recursos** | Detectar desvios, valores ausentes, alterações de distribuição |
| Ferramenta | Descrição |
|------|-------------|
| **Festa** | Código aberto; funciona com qualquer estrutura de ML |
| **Tecton** | Comercial; plataforma de recursos em tempo real |
| **Lúpulo funciona** | Código aberto; plataforma de ML completa com armazenamento de recursos |
| **Loja de recursos do Databricks** | Integrado com Databricks/Spark |
---

## Qualidade dos dados
A qualidade dos dados é o assassino silencioso dos projetos de ML. Entra lixo, sai lixo.
### Dimensões de Qualidade
| Dimensão | Pergunta |
|-----------|----------|
| **Precisão** | Os dados refletem a realidade? |
| **Completude** | Os campos obrigatórios estão preenchidos? |
| **Consistência** | Os valores concordam entre as fontes? |
| **Oportunidade** | Os dados são atuais? |
| **Validade** | Os valores estão em conformidade com regras definidas? |
| **Singularidade** | Existem registros duplicados? |
### Ferramentas de qualidade de dados
| Ferramenta | Abordagem |
|------|----------|
| **Grandes Expectativas** | Baseado em Python; definir “expectativas” sobre dados |
| **Monte Carlo** | Plataforma de observabilidade de dados baseada em ML |
| **testes dbt** | Testes integrados para dados de warehouse (relacionamentos exclusivos, not_null) |
| **Refrigerante** | Verificação de qualidade de dados de código aberto |
---

## Governança de dados
A governança de dados garante que os dados sejam gerenciados de forma responsável em toda a organização.
| Área | Descrição |
|------|-------------|
| **Catálogo de dados** | Inventário pesquisável de conjuntos de dados com metadados (Amundsen, DataHub, Atlan) |
| **Linhagem de dados** | Acompanhe de onde vêm os dados e como eles se transformam |
| **Controle de acesso** | Permissões baseadas em funções; quem pode ler/escrever o quê |
| **Conformidade** | Aderência ao GDPR, CCPA, HIPAA |
| **Propriedade de dados** | Propriedade clara de cada conjunto de dados (administração) |
| **Políticas de retenção** | Definir por quanto tempo os dados serão mantidos e quando serão excluídos |
---

## A pilha de dados moderna
A "pilha de dados moderna" refere-se à combinação típica de ferramentas usadas pelas equipes de dados hoje:
| Camada | Ferramentas típicas |
|-------|-------------|
| **Ingestão** | Fivetran, Airbyte |
| **Armazém** | Floco de neve, BigQuery, Redshift |
| **Transformação** | dbt |
| **Orquestração** | Fluxo de ar, prefeito, Dagster |
| **BI / Visualização** | Looker, Metabase, Tableau |
| **ETL reverso** | Censo, Hightouch (sincronizar dados do armazém com ferramentas) |
| **Qualidade dos dados** | Grandes Expectativas, Monte Carlo |
A tendência é para ferramentas modulares de melhor qualidade, conectadas por padrões abertos (SQL, modelos dbt, DAGs Airflow) em vez de plataformas monolíticas.