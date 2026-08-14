---
# Metadata
title: "Cloud Services Comparison"
description: "AWS vs Azure vs GCP side-by-side comparison"
category: "Quick Reference"
subcategory: "Infrastructure"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "AI Model Training Team"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.1"
    date: "2026-08-09"
    author: "AI Model Training Team"
    changes: "Moved to infrastructure/ subfolder; added subcategory field"
  - version: "1.0.0"
    date: "2026-08-05"
    author: "AI Model Training Team"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-09"
review_date: "2027-02-05"
reviewed_by: "Quick Reference Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [cloud, services, comparison, quick-reference]
difficulty_level: "beginner"
prerequisites: []
estimated_reading_time: "7 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# 雲端服務比較
將三大雲端供應商（AWS、Azure 和 Google Cloud）在運算、儲存、資料庫、AI/ML、網路、監控和基礎設施即程式碼方面進行並排比較。對於架構師決定使用哪個平台或將服務從一個雲端對應到另一個雲端很有用。
---

## 提供者概述
| |亞馬遜AWS |天藍色|Google雲端（GCP）|
|---|-----|--------------------|---------------------|
| **市場佔有率** | ~31%（最大）| ~25%（第二）| ~11%（第三，成長最快）|
| **優勢** |服務範圍；到期;生態系統|企業整合；混合雲；微軟堆疊|資料/人工智慧；庫伯內特斯；全球網路|
| **最適合** |新創公司到企業；最廣泛的服務目錄|擁有 Microsoft/Active Directory 的企業；混合動力 |資料密集型工作負載； Kubernetes 原生；人工智慧/機器學習 |
| **地区** | 33 个地区，105 个可用区 | 60+ 地区 | 40+地区，100+专区 |
| **免費套餐** | 12 個月免費套餐 + 始終免費 | 12 個月免費 + 200 美元積分 | 90 天 300 美元積分 + 永遠免費 |
---

## 計算
|服務類別 |亞馬遜AWS |天藍色| GCP |
|----------------|-----|--------|-----|
| **虛擬機器** | EC2（彈性運算雲）|虛擬機器 |計算引擎 |
| **自動縮放** | Auto Scaling 群組 |虛擬機器規模集|實例群組 |
| **無伺服器功能** |拉姆達 | Azure 函數 |雲端功能|
| **容器登錄機碼** | ECR（彈性容器登錄）| Azure 容器登錄機碼 |工件登錄機碼 |
| **容器編排** | ECS / EKS | ACS/AKS | GKE / 雲端運作 |
| **無伺服器容器** |法爾蓋特 |容器應用程式 |雲端跑|
| **應用程式平台（PaaS）** | Elastic Beanstalk，應用程式運行器 |應用程式服務|應用程式引擎 |
| **批次** | AWS 批次 | Azure 批次 |雲端批次|
| **GPU / AI 計算** | EC2（P4d、P5 執行個體）| NC/ND 系列虛擬機器 | A2/A3 虛擬機器；TPU |
### VM 定價模型
|型号|亚马逊AWS |天蓝色| GCP |
|--------|-----|--------|-----|
| **按需** |按需實例 |按量付費 |點播 |
| **保留/承諾** |預留實例（1-3 年）|預留虛擬機器（1-3 年）|承諾使用折扣（1-3 年）|
| **現貨/可中斷** |現貨實例 | Spot 虛擬機器 |搶佔式/現貨虛擬機器 |
| **儲蓄計劃** |儲蓄計劃|儲蓄計劃|承諾使用折扣|
---

＃＃ 貯存
|服務類別 |亞馬遜AWS |天藍色| GCP |
|----------------|-----|--------|-----|
| **物件儲存** | S3 | Blob 儲存 |雲端儲存|
| **區塊儲存** |電子BS |託管磁碟 |持久磁碟 |
| **檔案儲存** | EFS、FSx | Azure 檔案 |檔案儲存 |
| **存檔/冷** | S3 冰川，深度存檔 | Blob 酷/存檔層 |雲端儲存 Coldline/Archive |
| **資料傳輸** |雪球、資料同步 |資料盒|轉移設備|
### 儲存類別比較
|使用案例| AWS S3 | AWS S3藍色斑點 | GCP 雲端儲存 |
|----------|--------|------------|--------------------|
| **頻繁存取** | S3標準|熱門 |標準|
| **不頻繁訪問** | S3 標準-IA |酷|近線|
| **稀有訪問** | S3 一區-IA | — |冷線|
| **存檔** | S3 冰川/深度檔案 |檔案 |檔案 |
---

## 資料庫
|服務類別 |亞馬遜AWS |天藍色| GCP |
|----------------|-----|--------|-----|
| **關係式（託管）** | RDS（MySQL、PostgreSQL、Oracle、SQL Server）| Azure 資料庫（MySQL、PostgreSQL）； Azure SQL |雲端 SQL（MySQL、PostgreSQL）|
| **關係式（雲端原生）** | Aurora（相容於 MySQL/PostgreSQL）| Azure SQL 資料庫（彈性池）| Cloud Spanner（全球分散）|
| **NoSQL（文件）** | DynamoDB | Cosmos DB（MongoDB API、SQL API）|火庫；資料儲存 |
| **NoSQL（寬列）** | DynamoDB（也）| Cosmos DB（卡桑德拉 API）|大表|
| **NoSQL（鍵值）** | DynamoDB、ElastiCache |用於 Redis 的 Azure 快取 |記憶體儲存（Redis）|
| **圖表** |海王星| Cosmos DB（Gremlin API）| — |
| **時間序列** |時間流 | Azure 資料資源管理器 | — |
| **分類帳** | QLDB | Azure 機密帳本 | — |
| **記憶體快取** | ElastiCache（Redis、Memcached）|用於 Redis 的 Azure 快取 |記憶庫|
| **搜尋** |開放搜尋服務| Azure 人工智慧搜尋 |雲端搜尋；頂點人工智慧搜尋 |
| **資料倉儲** |紅移|突觸分析 | BigQuery |
---

## 人工智慧和機器學習
|服務類別 |亞馬遜AWS |天藍色| GCP |
|----------------|-----|--------|-----|
| **機器學習平台** | SageMaker| Azure 機器學習 |頂點人工智慧 |
| **預訓練的 API** | Rekognition（視覺）、Polly (TTS)、理解 (NLP)、轉錄 |認知服務（視覺、言語、語言、決策）|視覺 AI、語音轉文本、自然語言 API |
| **法學碩士/生成人工智慧** |基岩（克勞德、美洲駝、泰坦）| Azure OpenAI 服務（GPT-4、DALL-E）|頂點人工智慧（雙子座）；模型花園|
| **向量/嵌入** | OpenSearch (k-NN)，基岩知識庫 | Azure AI 搜尋（向量）| Vertex AI 向量搜尋、AlloyDB |
| **MLOps** | SageMaker Pipelines、模型登錄 | Azure ML Pipelines、模型登錄 | Vertex AI Pipelines、模型登錄 |
| **資料標籤** | SageMaker 地面真相 | Azure ML 資料標籤 | Vertex AI 資料標籤 |
| **對話式人工智慧** |萊克斯 | Azure 機器人服務 | Dialogflow CX / ES |
| **翻譯** |翻譯 |譯者|翻譯API |
---

## 網路
|服務類別 |亞馬遜AWS |天藍色| GCP |
|----------------|-----|--------|-----|
| **虛擬網路** |專有網路|虛擬網路 (VNet) |專屬網路|
| **負載平衡** | ELB/ALB/NLB/CLB |負載平衡器（應用程式、網路、閘道）|雲端負載平衡|
| **DNS** | 53 號公路 | Azure DNS |雲端網域解析 |
| **CDN** |雲前 |蔚藍前門|雲CDN |
| **API網關** | API網關| API管理| API網關|
| **VPN** |站點到站點 VPN、客戶端 VPN | VPN網關|雲端VPN |
| **直接連接/ ExpressRoute** |直接連接 |快速路線 |雲端互聯|
| **私人連結** | PrivateLink、VPC 端點 |私人連結、私有端點 |私人服務連線 |
| **防火牆** | WAF，網路防火牆| Azure 防火牆、WAF |雲端甲、防火牆|
| **DDoS 防護** |盾牌標準/高級| DDoS 防護 |雲甲|
---

## 監控和日誌記錄
|服務類別 |亞馬遜AWS |天藍色| GCP |
|----------------|-----|--------|-----|
| **指標/監控** |雲端觀察| Azure 監視器 |雲端監控（Stackdriver）|
| **記錄** | CloudWatch 日誌 |日誌分析（Azure Monitor 日誌）|雲日誌|
| **追蹤** | X 射線 |應用洞察 |雲踪|
| **警報** | CloudWatch 警報 | Azure 監視器警報 |雲端監控警報|
| **儀表板** | CloudWatch 儀表板 | Azure 工作簿/儀表板 |雲端監控儀表板|
| **錯誤追蹤** | CloudWatch 合成 |應用洞察 |雲端錯誤報告 |
| **第三方** | Datadog、New Relic、PagerDuty | Datadog、New Relic、PagerDuty | Datadog、New Relic、PagerDuty |
---

## 基礎架構即程式碼與 DevOps
|服務類別 |亞馬遜AWS |天藍色| GCP |
|----------------|-----|--------|-----|
| **IaC（本地）** |雲形成| ARM 模板/二頭肌 |部署經理/Pulumi |
| **IaC（跨雲）** | Terraform、Pulumi、CDK | Terraform、Pulumi、二頭肌 | Terraform，普魯米 |
| **CI/CD** |程式碼管道、程式碼建置 | Azure DevOps、GitHub 作業 |雲端建置；雲端部署|
| **容器註冊表** |電子CR | Azure 容器註冊表 |工件註冊表 |
| **GitOps** |套用網格 + Flux/ArgoCD | AKS 上的 Flux/ArgoCD |設定同步 (Anthos) |
| **秘密管理** |秘密管理器，SSM 參數儲存 |金鑰庫 |秘密經理|
---

## 定價考慮因素
|因素|亞馬遜AWS |天藍色| GCP |
|--------|-----|--------|-----|
| **計費粒度** |每秒（對於某些人來說，第一個小時之後）|每秒 |每秒 |
| **持續使用折扣** |預留實例/節省計畫 |預約虛擬機器 |承諾使用折扣|
| **現貨實例** |高達 90% 折扣 |高達 90% 折扣 |高達 91% 折扣 |
| **資料出口** |收費（昂貴）|收費|無論目的地為何，價格相同（通常較便宜）|
| **免費套餐** | 12 個月 + 永遠免費 | 12 個月 + 200 美元積分 | 90 天 300 美元 + 永久免費 |
| **企業折扣** |企業折扣計劃 (EDP) | MACC（貨幣承諾合約）|承諾使用 + CUD |
---

## 何時使用哪一個
|場景|推薦|為什麼 |
|----------|-------------|-----|
| **最廣泛的服務選擇；成熟的生態系統** |亞馬遜AWS |最大的目錄；大多數第三方整合|
| **微軟企業；活動目錄；混合** |天藍色|原生AD整合；強大的混合工具|
| **資料倉儲；大查詢；分析重度** | GCP | BigQuery 是同類中最好的；無縫資料整合|
| **Kubernetes 原生開發** | GCP | GKE 是最完善的託管 Kubernetes |
| **生成式人工智慧/法學碩士應用** | Azure 或 GCP |適用於 GPT 模式的 Azure OpenAI； Vertex AI 雙子座 |
| **全球規模、低延遲應用** | GCP |Google的全球網路是真正的優勢|
| **政府/合規性工作負載** | AWS 或 Azure |大多數合規認證；GovCloud 區域 |
| **成本敏感的新創公司** | GCP 或 AWS | GCP 的免費套餐非常慷慨； AWS 擁有啟動積分 |
| **現有的 Microsoft / .NET 堆疊** |天藍色|與 Visual Studio、.NET、Office 365 緊密整合 |
| **多雲策略** | Terraform + 所有三個 |使用 Terraform 跨雲管理資源 |
---

＃＃ 概括
這三種雲端都是強大、可靠且不斷擴展的。選擇通常歸結為：您的團隊已經知道什麼，您現有的合約是什麼樣的，以及哪些特定服務對您的工作負載很重要。多雲越來越普遍——使用 Terraform 或 Pulumi 來避免基礎設施層的供應商鎖定，並選擇每種雲端最擅長的功能。