---
# Metadata
title: "Database Systems"
description: "SQL, NoSQL, design patterns, optimization"
category: "Coding and Technology"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "AI Model Training Team"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.0"
    date: "2026-08-05"
    author: "AI Model Training Team"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-05"
review_date: "2027-02-05"
reviewed_by: "Coding & Technology Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [database, systems, coding-and-technology]
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
# 資料庫系統
## 資料庫基礎知識
### 什麼是資料庫？
資料庫是以電子方式儲存的結構化資訊的有組織的集合，旨在有效地檢索、插入、更新和刪除資料。
### 資料庫管理系統 (DBMS)
與最終用戶、應用程式和資料庫本身互動以捕獲和分析數據的軟體。範例：MySQL、PostgreSQL、Oracle、MongoDB。
### 關鍵概念
- **架構**：資料庫的結構/組織（表格、欄位、關係）
- **實例**：特定時刻儲存的實際數據
- **ACID 屬性**：原子性、一致性、隔離性、耐久性
- **CAP 定理**：一致性、可用性、分區容錯性（選擇 2）
- **標準化**：組織資料以減少冗餘
- **反規範化**：增加冗餘以提高讀取效能
## 關聯式資料庫 (SQL)
### 核心概念
- **表格**：行（記錄）和列（欄位）
- **主鍵**：每行的唯一識別符
- **外鍵**：引用另一個表中的主鍵
- **索引**：提高查詢速度的資料結構
- **檢視**：基於查詢結果的虛擬表
- **預存程序**：預先編譯的 SQL 程式碼區塊
- **觸發器**：資料變更時自動執行操作
### SQL 操作（CRUD）```sql
-- Create
INSERT INTO users (name, email) VALUES ('Alice', 'alice@example.com');

-- Read
SELECT * FROM users WHERE id = 1;
SELECT name, email FROM users ORDER BY name LIMIT 10;

-- Update
UPDATE users SET email = 'new@example.com' WHERE id = 1;

-- Delete
DELETE FROM users WHERE id = 1;
```

### 加入
- **INNER JOIN**：傳回兩個表中的符合行
- **LEFT JOIN**：左表中的所有行，從右表開始匹配
- **RIGHT JOIN**：右表中的所有行，從左表開始匹配
- **FULL OUTER JOIN**：兩個表中的所有行
- **CROSS JOIN**：兩個表格的笛卡爾積
- **SELF JOIN**：表格與自身連接
### 標準化形式
- **1NF**：原子值，無重複基團
- **2NF**：1NF + 無部分依賴（所有非鍵屬性都依賴整個主鍵）
- **3NF**：2NF + 無傳遞依賴（非鍵屬性不依賴其他非鍵屬性）
- **BCNF**：更強的3NF，每個行列式都是候選鍵
- **4NF**：沒有多值依賴
- **5NF**：無連結依賴性
### 流行的關係型資料庫管理系統
- **PostgreSQL**：進階功能、可擴充、符合 ACID
- **MySQL**：廣泛使用、快速讀取、Web 應用程式
- **Oracle**：企業特性、可擴充性、昂貴
- **SQL Server**：微軟生態系統，整合工具
- **SQLite**：嵌入式、無伺服器、輕量級
- **MariaDB**：MySQL 分支，開源
## NoSQL 資料庫
### NoSQL 資料庫的類型
#### 文檔存儲
- **結構**：類似 JSON 的文檔 (BSON)
- **用例**：內容管理、目錄、使用者設定文件
- **範例**：MongoDB、CouchDB、DocumentDB
- **查詢範例** (MongoDB)：```javascript
db.users.find({ age: { $gt: 25 } }).sort({ name: 1 });
```

#### 鍵值存儲
- **結構**：簡單的鍵值對
- **用例**：快取、會話、購物車
- **範例**：Redis、DynamoDB、Riak
- **特點**：快速、簡單、有限查詢
#### 專欄-家族店
- **結構體**：按族分組的列
- **用例**：大數據、分析、時間序列
- **範例**：Cassandra、HBase、ScyllaDB
- **特性**：寫入最佳化、分散式、可擴展
#### 圖表資料庫
- **結構**：節點、邊、屬性
- **用例**：社群網路、詐欺偵測、建議
- **範例**：Neo4j、Amazon Neptune、ArangoDB
- **查詢語言**：Cypher (Neo4j)、Gremlin
### 何時使用 NoSQL
- 靈活/不斷發展的模式
- 水平縮放要求
- 高寫入吞吐量
- 分層/嵌套數據
- 分散式系統
- 即時應用程式
## 資料庫設計
### 實體關係建模
- **實體**：物件/概念（顧客、產品、訂單）
- **屬性**：實體的屬性（名稱、價格、日期）
- **關係**：實體之間的連結（一對一、一對多、多對多）
- **基數**：關係中實例的數量
### 架構設計模式
- **單表繼承**：所有類型都在一個帶有類型鑑別器的表中
- **類別表繼承**：基底類別和子類別的單獨表
- **具體表繼承**：每個具體類別都有單獨的表
- **連接表**：解決多對多關係
- **審核表**：追蹤變更（created_at、updated_at、deleted_at）
### 索引策略
- **B-Tree**：預設、範圍查詢、排序
- **哈希**：精確匹配查找
- **點陣圖**：低基數列（性別、狀態）
- **全文**：文字搜尋功能
- **空間**：地理資料 (GIS)
- **複合**：多列組合
- **覆蓋**：包含查詢所需的所有列
## 查詢最佳化
### 執行計劃
- 了解資料庫如何執行查詢
- 辨識瓶頸（全表掃描、缺失索引）
- 工具：解釋、解釋分析
### 優化技術
- **索引使用**：確保查詢使用適當的索引
- **查詢重寫**：簡化複雜查詢
- **連線最佳化**：選擇正確的連接類型和順序
- **分割區**：分割大表（範圍、雜湊、清單）
- **物化視圖**：預先計算的查詢結果
- **查詢快取**：儲存頻繁的查詢結果
### 常見效能問題
- **N+1查詢問題**：取得相關資料效率低下
- **缺少索引**：大型表上的全表掃描
- **過度索引**：由於索引太多而導致寫入緩慢
- **鎖爭用**：等待鎖的事務
- **低效率查詢**：SELECT *，不必要的連接
## 事務和並發
### 交易隔離級別
- **READ UNCOMMITTED**：最低隔離度，可能出現髒讀
- **READ COMMITTED**：僅提交的資料可見（大多數資料庫中預設）
- **可重複讀取**：相同查詢在事務中傳回相同的結果
- **SERIALIZABLE**：最高隔離，交易依序執行
### 並發控制
- **悲觀鎖定**：在訪問之前鎖定資源
- **樂觀鎖定**：提交前檢查版本
- **MVCC（多版本並發控制）**：維護行的多個版本
- **行級鎖定**：鎖定特定行
- **表級鎖定**：鎖定整個表
### 死鎖
- 事務相互等待的循環依賴
- 預防：一致的鎖定順序、逾時、死鎖偵測
- 解決方案：中止一筆交易
## 複製和擴充
### 複製類型
- **主從**：一個主，多個只讀副本
- **主-主**：多個主節點，雙向複製
- **多主控**：N 個初選，需要解決衝突
- **鏈複製**：透過節點順序複製
### 擴充方法
- **垂直擴充**：增加伺服器資源（CPU、RAM、儲存）
- **水平擴充**：新增更多伺服器（分片、分割區）
- **唯讀副本**：卸載讀取流量
- **分片**：按鍵/範圍/雜湊跨伺服器分割數據
- **聯合**：依功能/服務劃分
### 一致性模型
- **強一致性**：所有節點同時看到相同的數據
- **最終一致性**：節點隨著時間的推移而收斂
- **因果一致性**：保留因果關係
- **閱讀您的文章**：用戶立即看到自己的更新
## 備份與還原
### 備份策略
- **完整備份**：完整的資料庫副本
- **增量備份**：自上次備份以來的更改
- **差異備份**：自上次完整備份以來的更改
- **時間點恢復**：恢復到特定時刻
- **連續備份**：即時複製到備份
### 復原程序
- **RTO（恢復時間目標）**：最大可接受的停機時間
- **RPO（恢復點目標）**：可接受的最大資料遺失
- **災難復原計畫**：記錄失敗的程序
- **測試**：定期恢復訓練
＃＃ 安全
### 存取控制
- **身份驗證**：驗證使用者身份
- **授權**：授予權限（GRANT、REVOKE）
- **角色**：分組權限，更輕鬆管理
- **最小權限原則**：最低限度的必要訪問
### 資料保護
- **靜態加密**：加密儲存的數據
- **傳輸中加密**：用於連線的 TLS/SSL
- **屏蔽**：隱藏非生產中的敏感數據
- **標記化**：用標記取代敏感數據
### 常見漏洞
- **SQL注入**：使用者輸入中的惡意SQL
- **權限提升**：獲得未經授權的訪問
- **審核日誌記錄**：追蹤所有資料庫活動
- **合規性**：GDPR、HIPAA、PCI-DSS 要求
## 現代資料庫技術
### 雲端資料庫
- **AWS**：RDS、Aurora、DynamoDB、Redshift
- **Google Cloud**：Cloud SQL、Spanner、Bigtable、Firestore
- **Azure**：SQL 資料庫、Cosmos DB、Synapse
- **優點**：託管服務、自動擴充、包含備份
### NewSQL 資料庫
- 將 SQL 一致性與 NoSQL 可擴充性結合
- **範例**：CockroachDB、TiDB、YugabyteDB、Google Spanner
- **特性**：分散式、ACID 事務、水平擴展
### 時間序列資料庫
- 針對帶有時間戳記的資料進行了最佳化
- **範例**：InfluxDB、TimescaleDB、Prometheus
- **用例**：物聯網、監控、財務數據
### 向量資料庫
- 儲存和查詢嵌入向量
- **範例**：Pinecone、Milvus、Weaviate、Qdrant
- **用例**：語意搜尋、推薦系統、人工智慧應用
### 多模型資料庫
- 在單一系統中支援多種資料模型
- **範例**：ArangoDB、OrientDB、Azure Cosmos DB
- **優點**：無需多個資料庫即可實現彈性
## ORM 和資料訪問
### 物件關係映射
- **目的**：將資料庫表映射到程式設計對象
- **流行的 ORM**：
  - Python：SQLAlchemy、Django ORM、Peewee
  - JavaScript：Sequelize、Prisma、TypeORM
  - Java：Hibernate、JPA
  - 紅寶石：ActiveRecord
  - .NET：實體框架
### 好處
- 從 SQL 抽象
- 類型安全
- 遷移管理
- 查詢建置API
### 缺點
- 效能開銷
- 複雜的查詢更難編寫
- N+1查詢問題
- 學習曲線
## 資料庫管理
### DBA 職責
- 安裝和配置
- 性能調整
- 備份和還原
- 安全管理
- 容量規劃
- 監控和警報
- 補丁管理
### 監控指標
- 查詢回應時間
- 吞吐量（每秒交易數）
- 連接數
- 緩存命中率
- 磁碟輸入/輸出
- 鎖定等待時間
- 複製滯後
### 維護任務
- **真空/分析**：更新統計數據，回收空間
- **索引重建**：整理索引片段
- **統計更新**：讓查詢優化器隨時了解狀況
- **日誌輪替**：管理日誌檔案大小
- **容量規劃**：預測成長，規劃升級