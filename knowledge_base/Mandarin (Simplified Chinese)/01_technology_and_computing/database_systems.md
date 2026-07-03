# 数据库系统

## 数据库基础

### 什么是数据库？
数据库是以电子方式存储的结构化信息的有组织集合，旨在高效地检索、插入、更新和删除数据。

### 数据库管理系统（DBMS）
DBMS 是与终端用户、应用程序以及数据库本身交互的软件，用于采集和分析数据。示例：MySQL、PostgreSQL、Oracle、MongoDB。

### 关键概念
- **Schema**：数据库的结构 / 组织方式（表、字段、关系）
- **Instance**：某一时刻实际存储的数据
- **ACID Properties**：原子性、一致性、隔离性、持久性
- **CAP Theorem**：一致性、可用性、分区容错性（通常三者取其二）
- **Normalization**：通过组织数据来减少冗余
- **Denormalization**：通过增加冗余来提升读取性能

## 关系型数据库（SQL）

### 核心概念
- **Tables**：行（记录）和列（字段）
- **Primary Key**：每一行的唯一标识符
- **Foreign Key**：引用另一张表中的主键
- **Indexes**：提升查询速度的数据结构
- **Views**：基于查询结果生成的虚拟表
- **Stored Procedures**：预编译的 SQL 代码块
- **Triggers**：数据变更时自动执行的动作

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

### 连接（Joins）
- **INNER JOIN**：返回两张表中匹配的行
- **LEFT JOIN**：返回左表全部行及右表中的匹配行
- **RIGHT JOIN**：返回右表全部行及左表中的匹配行
- **FULL OUTER JOIN**：返回两张表中的全部行
- **CROSS JOIN**：返回两张表的笛卡尔积
- **SELF JOIN**：表与自身连接

### 规范化范式
- **1NF**：值不可再分，不存在重复组
- **2NF**：满足 1NF，且不存在部分依赖（所有非键属性依赖于整个主键）
- **3NF**：满足 2NF，且不存在传递依赖（非键属性不依赖于其他非键属性）
- **BCNF**：比 3NF 更严格，每个决定因素都是候选键
- **4NF**：不存在多值依赖
- **5NF**：不存在连接依赖

### 常见 RDBMS
- **PostgreSQL**：功能先进、可扩展、符合 ACID
- **MySQL**：应用广泛、读取速度快、常见于 Web 应用
- **Oracle**：企业特性丰富、可扩展性强、成本较高
- **SQL Server**：适合微软生态，集成工具完善
- **SQLite**：嵌入式、无服务器、轻量
- **MariaDB**：MySQL 分支，开源

## NoSQL 数据库

### NoSQL 数据库的类型

#### 文档数据库
- **Structure**：类似 JSON 的文档（BSON）
- **Use Cases**：内容管理、目录、用户画像
- **Examples**：MongoDB、CouchDB、DocumentDB
- **Query Example** (MongoDB):
```javascript
db.users.find({ age: { $gt: 25 } }).sort({ name: 1 });
```

#### 键值数据库
- **Structure**：简单的键值对
- **Use Cases**：缓存、会话、购物车
- **Examples**：Redis、DynamoDB、Riak
- **Characteristics**：速度快、简单、查询能力有限

#### 列族数据库
- **Structure**：列按族进行分组
- **Use Cases**：大数据、分析、时序数据
- **Examples**：Cassandra、HBase、ScyllaDB
- **Characteristics**：写入优化、分布式、可扩展

#### 图数据库
- **Structure**：节点、边、属性
- **Use Cases**：社交网络、欺诈检测、推荐
- **Examples**：Neo4j、Amazon Neptune、ArangoDB
- **Query Language**：Cypher（Neo4j）、Gremlin

### 何时使用 NoSQL
- Schema 需要灵活演进
- 需要横向扩展
- 写入吞吐量高
- 数据具有层次 / 嵌套结构
- 面向分布式系统
- 实时应用场景

## 数据库设计

### 实体关系建模
- **Entities**：对象 / 概念（Customer、Product、Order）
- **Attributes**：实体的属性（名称、价格、日期）
- **Relationships**：实体之间的关系（一对一、一对多、多对多）
- **Cardinality**：关系中实例数量的约束

### Schema 设计模式
- **Single Table Inheritance**：所有类型放在一张表中，用类型标识符区分
- **Class Table Inheritance**：基类与子类分别使用独立的表
- **Concrete Table Inheritance**：每个具体类使用独立的表
- **Junction Tables**：用于解决多对多关系
- **Audit Tables**：跟踪变更（created_at、updated_at、deleted_at）

### 索引策略
- **B-Tree**：默认索引，适合范围查询和排序
- **Hash**：适合精确匹配查找
- **Bitmap**：适合低基数字段（如 gender、status）
- **Full-Text**：支持全文检索
- **Spatial**：适合地理数据（GIS）
- **Composite**：多个列组合而成
- **Covering**：包含查询所需的全部列

## 查询优化

### 执行计划
- 了解数据库如何执行查询
- 识别瓶颈（全表扫描、缺少索引）
- 工具：EXPLAIN、EXPLAIN ANALYZE

### 优化技术
- **Index Usage**：确保查询使用合适的索引
- **Query Rewriting**：简化复杂查询
- **Join Optimization**：选择正确的连接类型与顺序
- **Partitioning**：拆分大表（范围、哈希、列表）
- **Materialized Views**：预先计算查询结果
- **Query Caching**：缓存高频查询结果

### 常见性能问题
- **N+1 Query Problem**：关联数据获取低效
- **Missing Indexes**：大表查询发生全表扫描
- **Over-indexing**：索引过多导致写入变慢
- **Lock Contention**：事务相互等待锁
- **Inefficient Queries**：`SELECT *`、不必要的连接

## 事务与并发

### 事务隔离级别
- **READ UNCOMMITTED**：隔离性最低，可能出现脏读
- **READ COMMITTED**：只能看到已提交数据（多数数据库默认）
- **REPEATABLE READ**：同一事务内同一查询返回相同结果
- **SERIALIZABLE**：隔离性最高，事务按顺序执行

### 并发控制
- **Pessimistic Locking**：访问前先加锁
- **Optimistic Locking**：提交前检查版本
- **MVCC (Multi-Version Concurrency Control)**：维护同一行的多个版本
- **Row-Level Locking**：锁定特定行
- **Table-Level Locking**：锁定整张表

### 死锁
- 事务之间形成循环依赖并相互等待
- 预防方式：统一加锁顺序、设置超时、启用死锁检测
- 解决方式：中止其中一个事务

## 复制与扩展

### 复制类型
- **Master-Slave**：一个主库，多个只读副本
- **Master-Master**：多个主库，双向复制
- **Multi-Master**：多个主库，需要冲突解决机制
- **Chain Replication**：通过节点链路顺序复制

### 扩展方式
- **Vertical Scaling**：提升单台服务器资源（CPU、RAM、存储）
- **Horizontal Scaling**：增加更多服务器（分片、分区）
- **Read Replicas**：分担读流量
- **Sharding**：按键 / 范围 / 哈希将数据分布到多台服务器
- **Federation**：按功能 / 服务拆分

### 一致性模型
- **Strong Consistency**：所有节点在同一时间看到相同数据
- **Eventual Consistency**：节点经过一段时间后最终收敛
- **Causal Consistency**：保持因果关系顺序
- **Read-Your-Writes**：用户能立即看到自己刚写入的更新

## 备份与恢复

### 备份策略
- **Full Backup**：完整数据库副本
- **Incremental Backup**：自上次备份以来的变更
- **Differential Backup**：自上次完整备份以来的变更
- **Point-in-Time Recovery**：恢复到特定时间点
- **Continuous Backup**：实时复制到备份系统

### 恢复流程
- **RTO (Recovery Time Objective)**：可接受的最长停机时间
- **RPO (Recovery Point Objective)**：可接受的最大数据丢失量
- **Disaster Recovery Plan**：针对故障的文档化恢复流程
- **Testing**：定期执行恢复演练

## 安全

### 访问控制
- **Authentication**：验证用户身份
- **Authorization**：授予权限（GRANT、REVOKE）
- **Roles**：将权限分组，便于管理
- **Principle of Least Privilege**：仅授予必要的最小权限

### 数据保护
- **Encryption at Rest**：对静态存储数据进行加密
- **Encryption in Transit**：连接使用 TLS/SSL 加密
- **Masking**：在非生产环境中隐藏敏感数据
- **Tokenization**：用令牌替代敏感数据

### 常见漏洞
- **SQL Injection**：用户输入中包含恶意 SQL
- **Privilege Escalation**：获得未授权访问权限
- **Audit Logging**：跟踪所有数据库活动
- **Compliance**：满足 GDPR、HIPAA、PCI-DSS 等要求

## 现代数据库技术

### 云数据库
- **AWS**：RDS、Aurora、DynamoDB、Redshift
- **Google Cloud**：Cloud SQL、Spanner、Bigtable、Firestore
- **Azure**：SQL Database、Cosmos DB、Synapse
- **Benefits**：托管服务、自动伸缩、内置备份

### NewSQL 数据库
- 结合 SQL 的一致性与 NoSQL 的可扩展性
- **Examples**：CockroachDB、TiDB、YugabyteDB、Google Spanner
- **Features**：分布式、支持 ACID 事务、横向扩展

### 时序数据库
- 针对带时间戳的数据进行了优化
- **Examples**：InfluxDB、TimescaleDB、Prometheus
- **Use Cases**：IoT、监控、金融数据

### 向量数据库
- 用于存储和查询嵌入向量
- **Examples**：Pinecone、Milvus、Weaviate、Qdrant
- **Use Cases**：语义搜索、推荐系统、AI 应用

### 多模型数据库
- 在单一系统中支持多种数据模型
- **Examples**：ArangoDB、OrientDB、Azure Cosmos DB
- **Benefit**：无需维护多种数据库也能获得灵活性

## ORM 与数据访问

### 对象关系映射
- **Purpose**：将数据库表映射为编程对象
- **Popular ORMs**:
  - Python: SQLAlchemy、Django ORM、Peewee
  - JavaScript: Sequelize、Prisma、TypeORM
  - Java: Hibernate、JPA
  - Ruby: ActiveRecord
  - .NET: Entity Framework

### 优势
- 对 SQL 的抽象
- 类型安全
- 迁移管理
- 查询构建 API

### 局限
- 性能开销
- 复杂查询更难编写
- 容易出现 N+1 查询问题
- 学习曲线较陡

## 数据库管理

### DBA 职责
- 安装与配置
- 性能调优
- 备份与恢复
- 安全管理
- 容量规划
- 监控与告警
- 补丁管理

### 监控指标
- 查询响应时间
- 吞吐量（每秒事务数）
- 连接数
- 缓存命中率
- 磁盘 I/O
- 锁等待时间
- 复制延迟

### 维护任务
- **Vacuum/Analyze**：更新统计信息、回收空间
- **Index Rebuilding**：重建索引碎片
- **Statistics Updates**：让查询优化器掌握最新统计信息
- **Log Rotation**：管理日志文件大小
- **Capacity Planning**：预测增长并规划升级
