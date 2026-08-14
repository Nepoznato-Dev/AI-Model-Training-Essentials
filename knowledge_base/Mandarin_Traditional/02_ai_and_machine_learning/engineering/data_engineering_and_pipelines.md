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
# 數據工程和管道
資料工程是建構大規模移動、轉換和儲存資料的系統的學科。如果沒有可靠的資料管道，機器學習模型就無法訓練，儀表板顯示過時的數字，業務決策也基於猜測。該文件涵蓋了建構有效的資料基礎設施的架構、工具和實踐。
---

## ETL 與 ELT
|方法|它是如何運作的 |最適合 |工具|
|----------|-------------|----------|--------|
| **ETL**（提取→轉換→載入）| *在*載入到倉庫之前轉換資料 |運算能力有限的傳統倉庫 | Informatica、Talend、Apache NiFi |
| **ELT**（提取→載入→轉換）|先載入原始資料；改造倉庫*內部* |具有彈性運算的現代雲端倉庫| dbt、Fivetran、Airbyte + BigQuery/Snowflake |
從 ETL 到 ELT 的轉變是由雲端資料倉儲（BigQuery、Snowflake、Redshift）推動的，這些資料倉儲可以獨立於儲存擴充運算。不再需要在加載之前預處理所有內容。
---

## 資料湖與資料倉儲
|特色 |資料湖|資料倉儲|
|--------|---------|------------|
| **資料格式** |原始、本機格式（讀取時架構）|結構化、已處理（寫入時模式）|
| **架構** |在查詢時定義 |載入前定義 |
| **資料型別** |結構化、半結構化、非結構化 |主要結構|
| **使用者** |資料科學家、工程師 |商業分析師、BI 工具 |
| **成本** |更便宜的儲存（物件儲存）|更貴（針對查詢進行了最佳化）|
| **範例** | AWS S3、Azure 資料湖、GCS |雪花、BigQuery、Redshift |
現代方法是**湖屋**：將湖的廉價、靈活的存儲與倉庫的管理和性能特徵結合起來。 Delta Lake、Apache Iceberg 和 Apache Hudi 是這裡的關鍵技術。
---

## 管道架構
### 批次與串流處理
|模式|描述 |延遲 |使用案例|
|------|-------------|---------|---------|
| **批次** |依預定時間間隔處理大塊資料 |分鐘到小時 |每日報告、ETL 作業、資料充實 |
| **串流媒體** |資料到達時持續處理 |毫秒到秒|即時儀表板、詐欺偵測、警報 |
| **微批量** |小批量，間隔很短|秒|近乎即時且批量簡單 |
### 管道元件
典型的資料管道具有以下階段：
|舞台|描述 |工具|
|--------|-------------|--------|
| **攝取** |從來源收集資料 |卡夫卡、Airbyte、Fivetran、Debezium |
| **轉型** |清潔、豐富、聚合 | dbt、Spark、Pandas |
| **儲存** |保留已處理的資料 | BigQuery、雪花、S3、Delta Lake |
| **服務** |提供消費者資料 | API、儀表板、ML 特徵儲存 |
| **編排** |排程與管理依賴關係 |氣流、Prefect、Dagster |
| **監控** |追蹤管道健康狀況與資料品質 |遠大前程、蒙地卡羅、自訂警報 |
---

## 編排工具
|工具|方法|實力|
|------|----------|----------|
| **阿帕契氣流** |基於Python的DAG；業界標準|龐大的生態系統，成熟、靈活 |
| **完美** | Python 原生；比 Airflow 更乾淨的 API |現代設計，優秀的錯誤處理能力 |
| **達格斯特** |以資產為中心；軟體工程方法|類型系統、測試、可觀測性 |
| **路易吉** | Spotify 原始管道工具 |簡單，但開發不太活躍 |
### 氣流範例
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

## 阿帕契卡夫卡
Kafka 是許多即時資料系統的支柱。它是一個分散式事件日誌，提供高吞吐量、容錯訊息傳遞。
### 核心概念
|概念 |描述 |
|---------|-------------|
| **主題** |訊息類別（例如`orders`、`user-events`） |
| **分區** |主題被分成多個分區以實現並行性 |
| **製片人** |將訊息寫入主題的應用程式 |
| **消費者** |從主題讀取訊息的應用程式 |
| **消費者群體** |分擔閱讀某個主題的負擔的消費者群體 |
| **偏移** |消費者在分區內的位置|
| **經紀人** | Kafka伺服器節點|
### 何時使用 Kafka
- **事件流**：大規模即時事件處理。
- **解耦服務**：生產者和消費者不需要互相了解。
- **重播**：保留訊息；消費者可以從任何偏移量重新讀取。
- **背壓**：Kafka 自然地處理生產者和消費者之間的速度差異。
---

## 資料建模
### 星型模式與雪花模式
|架構|結構|優點 |缺點 |
|--------|---------|------|--------|
| **明星** |中央事實表被非規範化維度表包圍 |簡單查詢，快速讀取 |資料冗餘 |
| **雪花** |維度表標準化（拆分為子表）|減少冗餘 |更多連接，更慢的查詢 |
### 事實與維度表
|表格類型|包含 |範例|
|------------|----------|---------|
| **事實** |可衡量的事件（指標）| `orders`（訂單 ID、產品 ID、客戶 ID、金額、日期）|
| **尺寸** |描述性屬性 | `products`（產品 ID、名稱、類別、價格）、`customers`（客戶 ID、名稱、城市）|
---

## 特徵商店
特徵儲存是 ML 特徵的集中儲存庫 - 用作模型輸入的派生值（例如「過去 30 天內使用者的平均訂單值」）。
|能力|描述 |
|------------|-------------|
| **功能註冊表** |包含元資料的可用功能目錄 |
| **線下商店** |模型訓練的歷史特徵（批量）|
| **網上商店** |低延遲特性服務於即時推理 |
| **功能監控** |偵測漂移、缺失值、分佈變化 |
|工具|描述 |
|------|-------------|
| **盛宴** |開源；適用於任何機器學習框架 |
| **特克頓** |商業的;即時特徵平台|
| **啤酒花工廠** |開源；帶有特徵存儲的完整機器學習平台 |
| **Databricks 特徵儲存** |與 Databricks/Spark 整合 |
---

## 數據質量
數據品質是機器學習專案的無聲殺手。垃圾進來，垃圾出去。
### 品質維度
|尺寸|問題 |
|------------|----------|
| **準確度** |數據反映現實嗎？ |
| **完整性** |必填欄位是否已填入？ |
| **一致性** |不同來源的價值觀是否一致？ |
| **時效性** |數據是最新的嗎？ |
| **有效期限** |價值觀是否符合既定規則？ |
| **獨特性** |是否有重複記錄？ |
### 資料品質工具
|工具|方法|
|------|----------|
| **遠大的期望** |基於Python；定義關於數據的「期望」|
| **蒙特卡羅** |機器學習驅動的資料可觀測平台 |
| **dbt 測試** |倉庫資料的內建測試（unique、not_null、關聯）|
| **蘇打水** |開源資料品質掃描|
---

## 資料治理
資料治理確保整個組織內的資料得到負責任的管理。
|面積 |描述 |
|------|-------------|
| **資料目錄** |可搜尋的包含元資料的資料集清單（Amundsen、DataHub、Atlan）|
| **資料沿襲** |追蹤資料的來源及其轉換方式 |
| **存取控制** |基於角色的權限；誰可以讀/寫什麼 |
| **合規性** | GDPR、CCPA、HIPAA 遵守情況 |
| **資料所有權** |每個資料集的明確所有權（管理權）|
| **保留政策** |定義資料的保留時間以及刪除時間 |
---

## 現代資料堆疊
「現代資料堆疊」是指當今資料團隊所使用的典型工具組合：
|層 |典型工具|
|--------|--------------|
| **攝入** | Fivetran、Airbyte |
| **倉庫** |雪花、BigQuery、Redshift |
| **轉型** |資料庫技術 |
| **編排** |氣流、Prefect、Dagster |
| **商業智慧/視覺化** | Looker、元資料庫、Tableau |
| **反向ETL** |人口普查、Hightouch（將倉庫資料同步回工具）|
| **數據品質** |寄予厚望，蒙地卡羅 |
趨勢是透過開放標準（SQL、dbt 模型、Airflow DAG）連接的模組化、同類最佳工具，而不是單一平台。