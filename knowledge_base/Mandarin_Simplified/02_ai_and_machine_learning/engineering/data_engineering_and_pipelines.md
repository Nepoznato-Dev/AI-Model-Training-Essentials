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
# 数据工程和管道
数据工程是构建大规模移动、转换和存储数据的系统的学科。如果没有可靠的数据管道，机器学习模型就无法训练，仪表板显示过时的数字，业务决策也基于猜测。该文件涵盖了构建有效的数据基础设施的架构、工具和实践。
---

## ETL 与 ELT
|方法|它是如何运作的 |最适合 |工具|
|----------|-------------|----------|--------|
| **ETL**（提取→转换→加载）| *在*加载到仓库之前转换数据 |计算能力有限的传统仓库 | Informatica、Talend、Apache NiFi |
| **ELT**（提取→加载→转换）|先加载原始数据；改造仓库*内部* |具有弹性计算的现代云仓库| dbt、Fivetran、Airbyte + BigQuery/Snowflake |
从 ETL 到 ELT 的转变是由云数据仓库（BigQuery、Snowflake、Redshift）推动的，这些数据仓库可以独立于存储扩展计算。不再需要在加载之前预处理所有内容。
---

## 数据湖与数据仓库
|特色|数据湖|数据仓库|
|--------|---------|------------|
| **数据格式** |原始、本机格式（读取时架构）|结构化、已处理（写入时模式）|
| **架构** |在查询时定义 |加载前定义 |
| **数据类型** |结构化、半结构化、非结构化 |主要结构|
| **用户** |数据科学家、工程师 |商业分析师、BI 工具 |
| **成本** |更便宜的存储（对象存储）|更贵（针对查询进行了优化）|
| **示例** | AWS S3、Azure 数据湖、GCS |雪花、BigQuery、Redshift |
现代方法是**湖屋**：将湖的廉价、灵活的存储与仓库的管理和性能特征结合起来。 Delta Lake、Apache Iceberg 和 Apache Hudi 是这里的关键技术。
---

## 管道架构
### 批处理与流式处理
|模式|描述 |延迟|使用案例|
|------|-------------|---------|---------|
| **批次** |按预定时间间隔处理大块数据 |分钟到小时 |每日报告、ETL 作业、数据充实 |
| **流媒体** |数据到达时持续进行处理 |毫秒到秒|实时仪表板、欺诈检测、警报 |
| **微批量** |小批量，间隔很短|秒|近乎实时且批量简单 |
### 管道组件
典型的数据管道具有以下阶段：
|舞台|描述 |工具|
|--------|-------------|--------|
| **摄入** |从来源收集数据 |卡夫卡、Airbyte、Fivetran、Debezium |
| **转型** |清洁、丰富、聚合 | dbt、Spark、Pandas |
| **存储** |保留已处理的数据 | BigQuery、雪花、S3、Delta Lake |
| **服务** |向消费者提供数据 | API、仪表板、ML 特征存储 |
| **编排** |安排和管理依赖关系 |气流、Prefect、Dagster |
| **监控** |跟踪管道健康状况和数据质量 |远大前程、蒙特卡洛、自定义警报 |
---

## 编排工具
|工具|方法|实力|
|------|----------|----------|
| **阿帕奇气流** |基于Python的DAG；行业标准|庞大的生态系统，成熟、灵活 |
| **完美** | Python 原生；比 Airflow 更干净的 API |现代设计，出色的错误处理能力 |
| **达格斯特** |以资产为中心；软件工程方法|类型系统、测试、可观测性 |
| **路易吉** | Spotify 原创管道工具 |简单，但开发不太活跃 |
### 气流示例
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

## 阿帕奇卡夫卡
Kafka 是许多实时数据系统的支柱。它是一个分布式事件日志，提供高吞吐量、容错消息传递。
### 核心概念
|概念 |描述 |
|---------|-------------|
| **主题** |消息类别（例如`orders`、`user-events`） |
| **分区** |主题被分成多个分区以实现并行性 |
| **制片人** |将消息写入主题的应用程序 |
| **消费者** |从主题读取消息的应用程序 |
| **消费者群体** |分担阅读某个主题的负担的消费者群体 |
| **偏移** |消费者在分区内的位置|
| **经纪人** | Kafka服务器节点|
### 何时使用 Kafka
- **事件流**：大规模实时事件处理。
- **解耦服务**：生产者和消费者不需要互相了解。
- **重播**：保留消息；消费者可以从任何偏移量重新读取。
- **背压**：Kafka 自然地处理生产者和消费者之间的速度差异。
---

## 数据建模
### 星型模式与雪花模式
|架构|结构|优点 |缺点 |
|--------|---------|------|--------|
| **明星** |中央事实表被非规范化维度表包围 |简单查询，快速读取 |数据冗余 |
| **雪花** |维度表标准化（拆分为子表）|减少冗余 |更多连接，更慢的查询 |
### 事实和维度表
|表格类型|包含 |示例|
|------------|----------|---------|
| **事实** |可衡量的事件（指标）|  `orders`（订单 ID、产品 ID、客户 ID、金额、日期）|
| **尺寸** |描述性属性 |  `products`（产品 ID、名称、类别、价格）、`customers`（客户 ID、名称、城市）|
---

## 特征商店
特征存储是 ML 特征的集中存储库 - 用作模型输入的派生值（例如“过去 30 天内用户的平均订单值”）。
|能力|描述 |
|------------|-------------|
| **功能注册表** |包含元数据的可用功能目录 |
| **线下商店** |模型训练的历史特征（批量）|
| **网上商店** |低延迟特性服务于实时推理 |
| **功能监控** |检测漂移、缺失值、分布变化 |
|工具|描述 |
|------|-------------|
| **盛宴** |开源；适用于任何机器学习框架 |
| **特克顿** |商业的;实时特征平台|
| **啤酒花工厂** |开源；带有特征存储的完整机器学习平台 |
| **Databricks 特征存储** |与 Databricks/Spark 集成 |
---

## 数据质量
数据质量是机器学习项目的无声杀手。垃圾进来，垃圾出去。
### 质量维度
|尺寸|问题 |
|------------|----------|
| **准确度** |数据反映现实吗？ |
| **完整性** |必填字段是否已填充？ |
| **一致性** |不同来源的价值观是否一致？ |
| **时效性** |数据是最新的吗？ |
| **有效期** |价值观是否符合既定规则？ |
| **独特性** |是否有重复记录？ |
### 数据质量工具
|工具|方法|
|------|----------|
| **远大的期望** |基于Python；定义关于数据的“期望”|
| **蒙特卡罗** |机器学习驱动的数据可观测平台 |
| **dbt 测试** |仓库数据的内置测试（unique、not_null、关系）|
| **苏打水** |开源数据质量扫描|
---

## 数据治理
数据治理确保整个组织内的数据得到负责任的管理。
|面积 |描述 |
|------|-------------|
| **数据目录** |可搜索的包含元数据的数据集清单（Amundsen、DataHub、Atlan）|
| **数据沿袭** |跟踪数据的来源及其转换方式 |
| **访问控制** |基于角色的权限；谁可以读/写什么 |
| **合规性** | GDPR、CCPA、HIPAA 遵守情况 |
| **数据所有权** |每个数据集的明确所有权（管理权）|
| **保留政策** |定义数据的保留时间以及删除时间 |
---

## 现代数据堆栈
“现代数据堆栈”是指当今数据团队使用的典型工具组合：
|层|典型工具|
|--------|--------------|
| **摄入** | Fivetran、Airbyte |
| **仓库** |雪花、BigQuery、Redshift |
| **转型** |数据库技术 |
| **编排** |气流、Prefect、Dagster |
| **商业智能/可视化** | Looker、元数据库、Tableau |
| **反向ETL** |人口普查、Hightouch（将仓库数据同步回工具）|
| **数据质量** |寄予厚望，蒙特卡洛 |
趋势是通过开放标准（SQL、dbt 模型、Airflow DAG）连接的模块化、同类最佳工具，而不是单一平台。