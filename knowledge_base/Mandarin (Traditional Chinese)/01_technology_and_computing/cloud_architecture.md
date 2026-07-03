# 雲端架構

## 雲端計算基礎

### 什麼是雲端計算？
雲端計算是指透過網際網路按需交付計算資源（伺服器、儲存、資料庫、網路、軟體），並按使用量計費。

### 基本特徵（NIST 定義）
- **按需自助服務**：無需人工介入即可自行佈建資源
- **廣泛的網路存取**：透過標準機制經網路存取
- **資源池化**：採用多租戶模型並動態分配資源
- **快速彈性**：能夠快速向外擴充套件和向內收縮
- **可度量服務**：資源使用情況可被監控並計費

### 雲部署模型
- **公有云**：由雲服務提供商擁有，基礎設施共享（AWS、Azure、GCP）
- **私有云**：專供單個組織使用（本地部署或託管）
- **混合雲**：公有云與私有云的組合
- **多雲**：同時使用多個公有云提供商
- **社群雲**：由具有共同訴求的多個組織共享

### 服務模型

#### 基礎設施即服務（IaaS）
- **提供內容**：虛擬機器、儲存、網路、作業系統
- **範例**：AWS EC2、Google Compute Engine、Azure VMs
- **使用場景**：遷移現有系統、開發環境、需要高度控制的場景

#### 平台即服務（PaaS）
- **提供內容**：開發平台、資料庫、中介軟體
- **範例**：Heroku、Google App Engine、AWS Elastic Beanstalk
- **使用場景**：應用開發、API 部署、微服務

#### 軟體即服務（SaaS）
- **提供內容**：透過網際網路交付的完整應用程式
- **範例**：Salesforce、Google Workspace、Microsoft 365、Slack
- **使用場景**：電子郵件、CRM、協作、業務應用

#### 函式即服務（FaaS）/ 無伺服器
- **提供內容**：事件驅動的函式執行
- **範例**：AWS Lambda、Azure Functions、Google Cloud Functions
- **使用場景**：事件處理、API、定時任務、即時處理

## 主要雲服務提供商

### Amazon Web Services (AWS)
- **市場份額**：約 32%（最大提供商）
- **核心服務**：
  - 計算：EC2、Lambda、ECS、EKS
  - 儲存：S3、EBS、Glacier
  - 資料庫：RDS、DynamoDB、Aurora
  - 網路：VPC、Route 53、CloudFront
  - AI/ML：SageMaker、Rekognition、Comprehend

### Microsoft Azure
- **市場份額**：約 23%
- **優勢**：企業整合、混合雲、微軟生態系統
- **核心服務**：
  - 計算：Virtual Machines、Azure Functions、AKS
  - 儲存：Blob Storage、Disk Storage
  - 資料庫：SQL Database、Cosmos DB
  - 網路：Virtual Network、Traffic Manager
  - AI/ML：Azure ML、Cognitive Services

### Google Cloud Platform (GCP)
- **市場份額**：約 10%
- **優勢**：資料分析、AI/ML、Kubernetes
- **核心服務**：
  - 計算：Compute Engine、Cloud Functions、GKE
  - 儲存：Cloud Storage、Persistent Disk
  - 資料庫：Cloud SQL、Firestore、Bigtable
  - 分析：BigQuery、Dataflow、Pub/Sub
  - AI/ML：Vertex AI、AutoML

### 其他提供商
- **IBM Cloud**：聚焦企業市場，提供 Watson AI
- **Oracle Cloud**：擅長資料庫工作負載和企業應用
- **Alibaba Cloud**：在亞太地區占主導地位
- **DigitalOcean**：對開發者友好，產品更簡潔

## 雲端架構模式

### 良好架構框架原則

#### 卓越運營
- 自動化運維
- 頻繁進行可逆變更
- 持續最佳化流程
- 預判故障

#### 安全性
- 建立強健的身份體系基礎
- 實現可追蹤性
- 在所有層面落實安全防護
- 自動化安全最佳實踐
- 保護傳輸中與靜態資料

#### 可靠性
- 測試恢復流程
- 在故障發生後自動恢復
- 透過橫向擴充套件提升可用性
- 不再依靠容量猜測
- 透過自動化管理變更

#### 效能效率
- 讓高階技術更易獲取
- 在幾分鐘內實現全球部署
- 使用無伺服器架構
- 更頻繁地進行實驗
- 考慮硬體特性適配

#### 成本最佳化
- 採用按需消費模式
- 衡量整體效率
- 避免在無差異化工作上花錢
- 分析並歸因支出
- 使用託管服務

### 常見架構模式

#### 微服務架構
- 將應用拆分為小型、獨立的服務
- 每個服務擁有自己的資料和邏輯
- 透過 API（REST、gRPC、訊息）通訊
- 可獨立部署
- **優勢**：可擴充套件性強、故障隔離好、技術棧多樣
- **挑戰**：分散式複雜性、資料一致性、監控難度

#### 事件驅動架構
- 元件透過事件通訊
- 生產者發布事件，消費者作出響應
- **模式**：事件溯源、CQRS、發布/訂閱
- **技術**：Kafka、SNS/SQS、EventBridge、Pub/Sub
- **優勢**：松耦合、可擴充套件、適合即時處理

#### 無伺服器架構
- 無需管理伺服器
- 按執行次數付費
- 自動伸縮
- **元件**：函式、API Gateway、託管服務
- **優勢**：成本效率高、運維負擔低、部署快速
- **注意事項**：冷啟動、供應商鎖定、執行時長限制

#### 分層架構（N 層）
- 表示層（UI）
- 應用層 / 業務邏輯層
- 資料存取層
- 資料庫層
- **優勢**：關注點分離、易於維護
- **常見場景**：三層 Web 應用

#### 空間基礎架構
- 透過分散式資料處理高併發
- 在多臺伺服器之間實現虛擬化記憶體
- 處理節點可獨立擴充套件
- **使用場景**：高吞吐、低延遲應用

## 計算服務

### 虛擬機器
- **型別**：通用型、計算最佳化型、記憶體最佳化型、GPU
- **計費方式**：按需、預留例項、競價例項
- **管理**：自動伸縮組、負載均衡器
- **最佳實踐**：規格匹配、資源打標、監控、補丁管理

### 容器
- **Docker**：容器執行時標準
- **編排**：Kubernetes（EKS、AKS、GKE）、ECS、Fargate
- **優勢**：可移植性、高效率、一致性
- **映象倉庫**：ECR、GCR、ACR、Docker Hub

### 無伺服器函式
- **執行模型**：事件觸發、無狀態
- **限制**：執行時長、記憶體、併發執行數
- **使用場景**：API、檔案處理、定時任務、IoT 後端
- **監控**：呼叫次數、錯誤、持續時間、冷啟動

## 儲存解決方案

### 物件儲存
- **特點**：扁平結構、後設資料、HTTP 存取
- **範例**：AWS S3、Google Cloud Storage、Azure Blob
- **使用場景**：靜態資源、備份、資料湖、歸檔
- **儲存類別**：熱、冷、歸檔等（成本和存取速度不同）

### 塊儲存
- **特點**：原始卷，掛載到虛擬機器
- **範例**：AWS EBS、Google Persistent Disk、Azure Disks
- **使用場景**：資料庫、啟動卷、高效能需求
- **型別**：SSD、HDD、預置 IOPS

### 檔案儲存
- **特點**：共享檔案系統，使用 NFS/SMB 協議
- **範例**：AWS EFS、Google Filestore、Azure Files
- **使用場景**：內容管理、共享組態、整體遷移

### 歸檔儲存
- **特點**：成本最低，但檢索有延遲
- **範例**：S3 Glacier、Azure Archive Storage
- **使用場景**：合規、長期備份、歷史資料

## 資料庫服務

### 託管關係型資料庫
- **服務**：AWS RDS/Aurora、Google Cloud SQL、Azure SQL Database
- **特性**：自動備份、補丁管理、擴縮容、複製
- **引擎**：MySQL、PostgreSQL、MariaDB、Oracle、SQL Server

### NoSQL 資料庫
- **文件型**：DocumentDB、Firestore、Cosmos DB
- **鍵值型**：DynamoDB、Redis Cache
- **列族型**：Bigtable、Cassandra（託管）
- **圖資料庫**：Neptune、Cosmos DB（graph API）

### 資料倉儲
- **服務**：Snowflake、Redshift、BigQuery、Synapse
- **特點**：列式儲存、MPP 架構
- **使用場景**：分析、BI、大規模資料分析

### 快取服務
- **記憶體型**：ElastiCache（Redis/Memcached）、Cloud Memorystore
- **CDN 快取**：CloudFront、Cloud CDN、Azure CDN
- **使用場景**：會話儲存、查詢快取、內容分發

## 網路

### 虛擬網路
- **VPC/VNet**：隔離的網路環境
- **子網**：公有（面向網際網路）、私有（僅內部使用）
- **IP 地址規劃**：CIDR 網段、IPv4/IPv6
- **路由表**：控制流量路徑

### 負載均衡
- **型別**：應用型（L7）、網路型（L4）、閘道器型
- **特性**：健康檢查、SSL 終止、會話保持
- **服務**：ELB/ALB/NLB、Cloud Load Balancing、Azure Load Balancer

### 內容分發網路（CDN）
- **目的**：在邊緣節點快取內容
- **優勢**：降低延遲、減少源站負載、實現全球分發
- **服務**：CloudFront、Cloud CDN、Azure CDN、Akamai

### DNS 服務
- **功能**：網域名稱註冊、流量路由、健康檢查
- **服務**：Route 53、Cloud DNS、Azure DNS
- **路由策略**：簡單、加權、基於延遲、地理位置、故障轉移

### 連線選項
- **Internet Gateway**：提供公網存取
- **NAT Gateway**：讓私有子網能夠對外存取
- **VPN**：連線本地環境的加密隧道
- **Direct Connect/ExpressRoute**：專用私有連線
- **VPC Peering**：連線同一賬戶或跨賬戶的 VPC

## 雲中的安全

### 共享責任模型
- **提供商責任**：雲本身的安全（基礎設施）
- **客戶責任**：雲中內容的安全（資料、應用、存取）
- **因服務而異**：託管程度越高，提供商承擔的責任越多

### 身分與存取管理（IAM）
- **使用者**：個人身份
- **組**：使用者集合
- **角色**：供服務或使用者臨時使用的憑證
- **策略**：定義許可權的 JSON 文件
- **原則**：最小許可權、職責分離

### 網路安全
- **安全組**：面向例項的有狀態防火牆
- **網路 ACL**：面向子網的無狀態防火牆
- **Web 應用防火牆（WAF）**：防禦 Web 攻擊
- **DDoS 防護**：Shield、Cloud Armor、DDoS Protection

### 資料保護
- **靜態加密**：KMS、客戶管理金鑰
- **傳輸加密**：TLS/SSL、HTTPS
- **金鑰管理**：HSM、金鑰輪換、審計追蹤
- **金鑰與憑據管理**：Secrets Manager、Key Vault

### 合規與治理
- **認證**：SOC 2、ISO 27001、HIPAA、PCI-DSS、GDPR
- **工具**：策略執行、合規報告、審計日誌
- **框架**：Cloud Security Alliance、NIST CSF

## 雲中的 DevOps

### CI/CD 服務
- **AWS**：CodePipeline、CodeBuild、CodeDeploy
- **Azure**：Azure DevOps、GitHub Actions
- **GCP**：Cloud Build、Cloud Deploy
- **第三方**：Jenkins、CircleCI、GitLab CI

### 基礎設施即程式碼（IaC）
- **Terraform**：多雲、宣告式、帶狀態管理
- **CloudFormation**：AWS 原生，使用 YAML/JSON 模板
- **ARM Templates**：Azure 原生
- **Deployment Manager**：GCP 原生
- **Pulumi**：使用程式語言定義基礎設施
- **優勢**：版本控制、可重複性、文件化

### 組態管理
- **Ansible**：無代理，使用 YAML Playbook
- **Chef**：基於 Ruby，生態成熟
- **Puppet**：宣告式，報告能力強
- **SaltStack**：速度快，基於 Python

### 監控與可觀測性
- **指標**：CloudWatch、Cloud Monitoring、Azure Monitor
- **日誌**：CloudWatch Logs、Cloud Logging、Log Analytics
- **鏈路追蹤**：X-Ray、Cloud Trace、Application Insights
- **儀表板**：CloudWatch Dashboards、Cloud Console
- **告警**：SNS、Cloud Monitoring alerts、Action Groups

### 容器編排
- **Kubernetes**：行業標準編排平台
- **託管服務**：EKS、AKS、GKE
- **服務網格**：Istio、Linkerd（流量管理、安全）
- **GitOps**：ArgoCD、Flux（宣告式部署）

## 成本管理

### 定價模型
- **按需付費**：按實際使用量計費
- **預留例項**：承諾使用 1-3 年，折扣顯著
- **競價例項**：競拍閒置容量，可能被中斷
- **Savings Plans**：更靈活的承諾式定價
- **免費層**：新賬戶可享有限免費額度

### 成本最佳化策略
- **合理選型**：讓例項規格匹配工作負載需求
- **自動伸縮**：根據需求自動擴縮容
- **預留容量**：適用於穩定負載的長期承諾
- **使用競價資源**：適用於容錯性強、彈性大的工作負載
- **儲存分層**：將低頻資料遷移到更便宜的層級
- **清理**：刪除未使用的資源、快照、AMI

### 成本管理工具
- **AWS**：Cost Explorer、Budgets、Trusted Advisor
- **Azure**：Cost Management、Advisor
- **GCP**：Billing reports、Recommender
- **第三方**：CloudHealth、CloudCheckr、Datadog

## 高可用性與災難恢復

### 可用性概念
- **可用區**：區域內物理隔離的資料中心
- **區域**：包含多個可用區的地理區域
- **邊緣節點**：全球分佈的 CDN 快取節點

### 高可用策略
- **Multi-AZ**：跨可用區部署
- **自動修復**：自動替換故障例項
- **負載均衡**：將流量分配到健康例項
- **資料庫複製**：多可用區部署、只讀副本

### 災難恢復策略
- **備份與恢復**：定期備份，災難發生時恢復（成本最低）
- **Pilot Light**：核心元件持續執行，災難時再擴容
- **Warm Standby**：始終執行縮小版環境
- **多站點 Active/Active**：多個區域同時執行完整生產環境（成本最高）

### RTO 與 RPO
- **恢復時間目標（RTO）**：可接受的最長停機時間
- **恢復點目標（RPO）**：可接受的最大資料丟失量
- **策略選擇**：取決於業務需求和預算

## 新興趨勢

### 邊緣計算
- 在更接近資料來源的位置處理資料
- **服務**：AWS Outposts、Wavelength、Azure Edge、Cloud CDN
- **使用場景**：IoT、即時分析、低延遲應用

### 多雲與混合雲
- 避免供應商鎖定
- 利用各家最優服務
- **工具**：Terraform、Anthos、Arc、CloudHealth

### AI/ML 服務
- 預訓練模型：視覺、語音、語言
- 自定義模型訓練：SageMaker、Vertex AI、Azure ML
- MLOps：模型部署、監控、治理

### 量子計算
- **服務**：AWS Braket、Azure Quantum
- **階段**：仍處於早期實驗階段
- **潛力**：密碼學、最佳化、藥物發現

### 可持續雲
- 碳足跡追蹤
- 可再生能源承諾
- 高效利用資源
- 綠色架構模式
