# 資料庫系統

## 資料庫基礎

### 什麼是資料庫？
資料庫是以電子方式儲存的結構化資訊的有組織集合，旨在高效地檢索、插入、更新和刪除資料。

### 資料庫管理系統（DBMS）
DBMS 是與終端使用者、應用程式以及資料庫本身互動的軟體，用於擷取和分析資料。範例：MySQL、PostgreSQL、Oracle、MongoDB。

### 關鍵概念
- **Schema**：資料庫的結構 / 組織方式（表、欄位、關係）
- **Instance**：某一時刻實際儲存的資料
- **ACID Properties**：原子性、一致性、隔離性、持久性
- **CAP Theorem**：一致性、可用性、分區容錯性（通常三者取其二）
- **Normalization**：透過組織資料來減少冗餘
- **Denormalization**：透過增加冗餘來提升讀取效能

## 關係型資料庫（SQL）

### 核心概念
- **Tables**：行（記錄）和列（欄位）
- **Primary Key**：每一行的唯一識別符號
- **Foreign Key**：引用另一張表中的主鍵
- **Indexes**：提升查詢速度的資料結構
- **Views**：基於查詢結果生成的虛擬表
- **Stored Procedures**：預編譯的 SQL 程式碼塊
- **Triggers**：資料變更時自動執行的動作

### SQL 操作（CRUD）
```sql
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

### 連線（Joins）
- **INNER JOIN**：返回兩張表中匹配的行
- **LEFT JOIN**：返回左表全部行及右表中的匹配行
- **RIGHT JOIN**：返回右表全部行及左表中的匹配行
- **FULL OUTER JOIN**：返回兩張表中的全部行
- **CROSS JOIN**：返回兩張表的笛卡爾積
- **SELF JOIN**：表與自身連線

### 正規化形式
- **1NF**：值不可再分，不存在重複組
- **2NF**：滿足 1NF，且不存在部分依賴（所有非鍵屬性依賴於整個主鍵）
- **3NF**：滿足 2NF，且不存在傳遞依賴（非鍵屬性不依賴於其他非鍵屬性）
- **BCNF**：比 3NF 更嚴格，每個決定因素都是候選鍵
- **4NF**：不存在多值依賴
- **5NF**：不存在連線依賴

### 常見 RDBMS
- **PostgreSQL**：功能先進、可擴充套件、符合 ACID
- **MySQL**：應用廣泛、讀取速度快、常見於 Web 應用
- **Oracle**：企業特性豐富、可擴充套件性強、成本較高
- **SQL Server**：適合微軟生態，整合工具完善
- **SQLite**：嵌入式、無伺服器、輕量
- **MariaDB**：MySQL 分支，開源

## NoSQL 資料庫

### NoSQL 資料庫的型別

#### 文件資料庫
- **Structure**：類似 JSON 的文件（BSON）
- **Use Cases**：內容管理、目錄、使用者畫像
- **Examples**：MongoDB、CouchDB、DocumentDB
- **Query Example** (MongoDB):
```javascript
db.users.find({ age: { $gt: 25 } }).sort({ name: 1 });
```

#### 鍵值資料庫
- **Structure**：簡單的鍵值對
- **Use Cases**：快取、會話、購物車
- **Examples**：Redis、DynamoDB、Riak
- **Characteristics**：速度快、簡單、查詢能力有限

#### 列族資料庫
- **Structure**：列按族進行分組
- **Use Cases**：大資料、分析、時序資料
- **Examples**：Cassandra、HBase、ScyllaDB
- **Characteristics**：寫入最佳化、分散式、可擴充套件

#### 圖資料庫
- **Structure**：節點、邊、屬性
- **Use Cases**：社交網路、欺詐檢測、推薦
- **Examples**：Neo4j、Amazon Neptune、ArangoDB
- **Query Language**：Cypher（Neo4j）、Gremlin

### 何時使用 NoSQL
- Schema 需要靈活演進
- 需要橫向擴充套件
- 寫入吞吐量高
- 資料具有層次 / 巢狀結構
- 面向分散式系統
- 即時應用場景

## 資料庫設計

### 實體關係建模
- **Entities**：物件 / 概念（Customer、Product、Order）
- **Attributes**：實體的屬性（名稱、價格、日期）
- **Relationships**：實體之間的關係（一對一、一對多、多對多）
- **Cardinality**：關係中例項數量的約束

### Schema 設計模式
- **Single Table Inheritance**：所有型別放在一張表中，用型別識別符號區分
- **Class Table Inheritance**：基類與子類分別使用獨立的表
- **Concrete Table Inheritance**：每個具體類使用獨立的表
- **Junction Tables**：用於解決多對多關係
- **Audit Tables**：跟蹤變更（created_at、updated_at、deleted_at）

### 索引策略
- **B-Tree**：預設索引，適合範圍查詢和排序
- **Hash**：適合精確匹配查詢
- **Bitmap**：適合低基數字段（如 gender、status）
- **Full-Text**：支援全文檢索
- **Spatial**：適合地理資料（GIS）
- **Composite**：多個列組合而成
- **Covering**：包含查詢所需的全部列

## 查詢最佳化

### 執行計劃
- 瞭解資料庫如何執行查詢
- 識別瓶頸（全表掃描、缺少索引）
- 工具：EXPLAIN、EXPLAIN ANALYZE

### 最佳化技術
- **Index Usage**：確保查詢使用合適的索引
- **Query Rewriting**：簡化複雜查詢
- **Join Optimization**：選擇正確的連線型別與順序
- **Partitioning**：拆分大表（範圍、雜湊、列表）
- **Materialized Views**：預先計算查詢結果
- **Query Caching**：快取高頻查詢結果

### 常見效能問題
- **N+1 Query Problem**：關聯資料獲取低效
- **Missing Indexes**：大表查詢發生全表掃描
- **Over-indexing**：索引過多導致寫入變慢
- **Lock Contention**：事務相互等待鎖
- **Inefficient Queries**：`SELECT *`、不必要的連線

## 事務與併發

### 事務隔離級別
- **READ UNCOMMITTED**：隔離性最低，可能出現髒讀
- **READ COMMITTED**：只能看到已提交資料（多數資料庫預設）
- **REPEATABLE READ**：同一事務內同一查詢返回相同結果
- **SERIALIZABLE**：隔離性最高，事務按順序執行

### 併發控制
- **Pessimistic Locking**：在存取前先加鎖
- **Optimistic Locking**：提交前檢查版本
- **MVCC (Multi-Version Concurrency Control)**：維護同一行的多個版本
- **Row-Level Locking**：鎖定特定行
- **Table-Level Locking**：鎖定整張表

### 死鎖
- 事務之間形成迴圈依賴並相互等待
- 預防方式：統一加鎖順序、設定超時、啟用死鎖檢測
- 解決方式：中止其中一個事務

## 複製與擴充套件

### 複製型別
- **Master-Slave**：一個主庫，多個只讀副本
- **Master-Master**：多個主庫，雙向複製
- **Multi-Master**：多個主庫，需要衝突解決機制
- **Chain Replication**：透過節點鏈路順序複製

### 擴充套件方式
- **Vertical Scaling**：提升單臺伺服器資源（CPU、RAM、儲存）
- **Horizontal Scaling**：增加更多伺服器（分片、分區）
- **Read Replicas**：分擔讀流量
- **Sharding**：按鍵 / 範圍 / 雜湊將資料分佈到多臺伺服器
- **Federation**：按功能 / 服務拆分

### 一致性模型
- **Strong Consistency**：所有節點在同一時間看到相同資料
- **Eventual Consistency**：節點經過一段時間後最終收斂
- **Causal Consistency**：保持因果關係順序
- **Read-Your-Writes**：使用者能立即看到自己剛寫入的更新

## 備份與恢復

### 備份策略
- **Full Backup**：完整資料庫副本
- **Incremental Backup**：自上次備份以來的變更
- **Differential Backup**：自上次完整備份以來的變更
- **Point-in-Time Recovery**：恢復到特定時間點
- **Continuous Backup**：即時複製到備份系統

### 恢復流程
- **RTO (Recovery Time Objective)**：可接受的最長停機時間
- **RPO (Recovery Point Objective)**：可接受的最大資料丟失量
- **Disaster Recovery Plan**：針對故障的文件化恢復流程
- **Testing**：定期執行恢復演練

## 安全

### 存取控制
- **Authentication**：驗證使用者身份
- **Authorization**：授予許可權（GRANT、REVOKE）
- **Roles**：將許可權分組，便於管理
- **Principle of Least Privilege**：僅授予必要的最小許可權

### 資料保護
- **Encryption at Rest**：對靜態儲存資料進行加密
- **Encryption in Transit**：連線使用 TLS/SSL 加密
- **Masking**：在非生產環境中隱藏敏感資料
- **Tokenization**：用令牌替代敏感資料

### 常見漏洞
- **SQL Injection**：使用者輸入中包含惡意 SQL
- **Privilege Escalation**：獲得未授權存取權限
- **Audit Logging**：跟蹤所有資料庫活動
- **Compliance**：滿足 GDPR、HIPAA、PCI-DSS 等要求

## 現代資料庫技術

### 雲資料庫
- **AWS**：RDS、Aurora、DynamoDB、Redshift
- **Google Cloud**：Cloud SQL、Spanner、Bigtable、Firestore
- **Azure**：SQL Database、Cosmos DB、Synapse
- **Benefits**：託管服務、自動伸縮、內建備份

### NewSQL 資料庫
- 結合 SQL 的一致性與 NoSQL 的可擴充套件性
- **Examples**：CockroachDB、TiDB、YugabyteDB、Google Spanner
- **Features**：分散式、支援 ACID 事務、橫向擴充套件

### 時序資料庫
- 針對帶時間戳的資料進行了最佳化
- **Examples**：InfluxDB、TimescaleDB、Prometheus
- **Use Cases**：IoT、監控、金融資料

### 向量資料庫
- 用於儲存和查詢嵌入向量
- **Examples**：Pinecone、Milvus、Weaviate、Qdrant
- **Use Cases**：語義搜尋、推薦系統、AI 應用

### 多模型資料庫
- 在單一系統中支援多種資料模型
- **Examples**：ArangoDB、OrientDB、Azure Cosmos DB
- **Benefit**：無需維護多種資料庫也能獲得靈活性

## ORM 與資料存取

### 物件關係映射
- **Purpose**：將資料庫表映射為程式設計物件
- **Popular ORMs**:
  - Python: SQLAlchemy、Django ORM、Peewee
  - JavaScript: Sequelize、Prisma、TypeORM
  - Java: Hibernate、JPA
  - Ruby: ActiveRecord
  - .NET: Entity Framework

### 優勢
- 對 SQL 的抽象
- 型別安全
- 遷移管理
- 查詢構建 API

### 侷限
- 效能開銷
- 複雜查詢更難編寫
- 容易出現 N+1 查詢問題
- 學習曲線較陡

## 資料庫管理

### DBA 職責
- 安裝與設定
- 效能調優
- 備份與恢復
- 安全管理
- 容量規劃
- 監控與告警
- 補丁管理

### 監控指標
- 查詢響應時間
- 吞吐量（每秒事務數）
- 連線數
- 快取命中率
- 磁碟 I/O
- 鎖等待時間
- 複製延遲

### 維護任務
- **Vacuum/Analyze**：更新統計資訊、回收空間
- **Index Rebuilding**：重建索引碎片
- **Statistics Updates**：讓查詢最佳化器掌握最新統計資訊
- **Log Rotation**：管理日誌檔案大小
- **Capacity Planning**：預測成長並規劃升級
