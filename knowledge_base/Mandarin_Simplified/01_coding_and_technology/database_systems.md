---
# Metadata
title: "Database Systems"
description: "SQL, NoSQL, design patterns, optimization"
category: "Coding and Technology"
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
# 数据库系统
## 数据库基础知识
### 什么是数据库？
数据库是以电子方式存储的结构化信息的有组织的集合，旨在高效检索、插入、更新和删除数据。
### 数据库管理系统 (DBMS)
与最终用户、应用程序和数据库本身交互以捕获和分析数据的软件。示例：MySQL、PostgreSQL、Oracle、MongoDB。
### 关键概念
- **架构**：数据库的结构/组织（表、字段、关系）
- **实例**：特定时刻存储的实际数据
- **ACID 属性**：原子性、一致性、隔离性、耐久性
- **CAP 定理**：一致性、可用性、分区容错性（选择 2）
- **标准化**：组织数据以减少冗余
- **反规范化**：添加冗余以提高读取性能
## 关系数据库 (SQL)
### 核心概念
- **表**：行（记录）和列（字段）
- **主键**：每行的唯一标识符
- **外键**：引用另一个表中的主键
- **索引**：提高查询速度的数据结构
- **视图**：基于查询结果的虚拟表
- **存储过程**：预编译的 SQL 代码块
- **触发器**：数据更改时自动执行操作
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
- **INNER JOIN**：返回两个表中的匹配行
- **LEFT JOIN**：左表中的所有行，从右表开始匹配
- **RIGHT JOIN**：右表中的所有行，从左表开始匹配
- **FULL OUTER JOIN**：两个表中的所有行
- **CROSS JOIN**：两个表的笛卡尔积
- **SELF JOIN**：表与自身连接
### 标准化形式
- **1NF**：原子值，无重复基团
- **2NF**：1NF + 无部分依赖（所有非键属性依赖于整个主键）
- **3NF**：2NF + 无传递依赖（非键属性不依赖于其他非键属性）
- **BCNF**：更强的3NF，每个行列式都是候选键
- **4NF**：没有多值依赖
- **5NF**：无连接依赖性
### 流行的关系型数据库管理系统
- **PostgreSQL**：高级功能、可扩展、符合 ACID
- **MySQL**：广泛使用、快速读取、Web 应用程序
- **Oracle**：企业特性、可扩展性、昂贵
- **SQL Server**：微软生态系统，集成工具
- **SQLite**：嵌入式、无服务器、轻量级
- **MariaDB**：MySQL 分支，开源
## NoSQL 数据库
### NoSQL 数据库的类型
#### 文档存储
- **结构**：类似 JSON 的文档 (BSON)
- **用例**：内容管理、目录、用户配置文件
- **示例**：MongoDB、CouchDB、DocumentDB
- **查询示例** (MongoDB)：```javascript
db.users.find({ age: { $gt: 25 } }).sort({ name: 1 });
```

#### 键值存储
- **结构**：简单的键值对
- **用例**：缓存、会话、购物车
- **示例**：Redis、DynamoDB、Riak
- **特点**：快速、简单、有限查询
#### 专栏-家族店
- **结构**：按族分组的列
- **用例**：大数据、分析、时间序列
- **示例**：Cassandra、HBase、ScyllaDB
- **特性**：写入优化、分布式、可扩展
#### 图数据库
- **结构**：节点、边、属性
- **用例**：社交网络、欺诈检测、建议
- **示例**：Neo4j、Amazon Neptune、ArangoDB
- **查询语言**：Cypher (Neo4j)、Gremlin
### 何时使用 NoSQL
- 灵活/不断发展的模式
- 水平缩放要求
- 高写入吞吐量
- 分层/嵌套数据
- 分布式系统
- 实时应用程序
## 数据库设计
### 实体关系建模
- **实体**：对象/概念（客户、产品、订单）
- **属性**：实体的属性（名称、价格、日期）
- **关系**：实体之间的连接（一对一、一对多、多对多）
- **基数**：关系中实例的数量
### 架构设计模式
- **单表继承**：所有类型都在一个带有类型鉴别器的表中
- **类表继承**：基类和子类的单独表
- **具体表继承**：每个具体类都有单独的表
- **连接表**：解决多对多关系
- **审核表**：跟踪更改（created_at、updated_at、deleted_at）
### 索引策略
- **B-Tree**：默认、范围查询、排序
- **哈希**：精确匹配查找
- **位图**：低基数列（性别、状态）
- **全文**：文本搜索功能
- **空间**：地理数据 (GIS)
- **复合**：多列组合
- **覆盖**：包括查询所需的所有列
## 查询优化
### 执行计划
- 了解数据库如何执行查询
- 识别瓶颈（全表扫描、缺失索引）
- 工具：解释、解释分析
### 优化技术
- **索引使用**：确保查询使用适当的索引
- **查询重写**：简化复杂查询
- **连接优化**：选择正确的连接类型和顺序
- **分区**：分割大表（范围、散列、列表）
- **物化视图**：预先计算的查询结果
- **查询缓存**：存储频繁的查询结果
### 常见性能问题
- **N+1查询问题**：获取相关数据效率低下
- **缺失索引**：大型表上的全表扫描
- **过度索引**：由于索引太多而导致写入缓慢
- **锁争用**：等待锁的事务
- **低效查询**：SELECT *，不必要的连接
## 事务和并发
### 事务隔离级别
- **READ UNCOMMITTED**：最低隔离度，可能出现脏读
- **READ COMMITTED**：仅提交的数据可见（大多数数据库中默认）
- **可重复读取**：同一查询在事务中返回相同的结果
- **SERIALIZABLE**：最高隔离，事务按顺序执行
### 并发控制
- **悲观锁定**：在访问之前锁定资源
- **乐观锁定**：提交前检查版本
- **MVCC（多版本并发控制）**：维护行的多个版本
- **行级锁定**：锁定特定行
- **表级锁定**：锁定整个表
### 死锁
- 事务相互等待的循环依赖
- 预防：一致的锁顺序、超时、死锁检测
- 解决方案：中止一笔交易
## 复制和扩展
### 复制类型
- **主从**：一个主，多个只读副本
- **主-主**：多个主节点，双向复制
- **多主控**：N 个初选，需要解决冲突
- **链复制**：通过节点顺序复制
### 扩展方法
- **垂直扩展**：增加服务器资源（CPU、RAM、存储）
- **水平扩展**：添加更多服务器（分片、分区）
- **只读副本**：卸载读取流量
- **分片**：按键/范围/散列跨服务器分割数据
- **联合**：按功能/服务划分
### 一致性模型
- **强一致性**：所有节点同时看到相同的数据
- **最终一致性**：节点随着时间的推移而收敛
- **因果一致性**：保留因果关系
- **阅读您的文章**：用户立即看到自己的更新
## 备份与恢复
### 备份策略
- **完整备份**：完整的数据库副本
- **增量备份**：自上次备份以来的更改
- **差异备份**：自上次完整备份以来的更改
- **时间点恢复**：恢复到特定时刻
- **连续备份**：实时复制到备份
### 恢复程序
- **RTO（恢复时间目标）**：最大可接受的停机时间
- **RPO（恢复点目标）**：可接受的最大数据丢失
- **灾难恢复计划**：记录失败的程序
- **测试**：定期恢复训练
＃＃ 安全
### 访问控制
- **身份验证**：验证用户身份
- **授权**：授予权限（GRANT、REVOKE）
- **角色**：分组权限，更轻松管理
- **最小权限原则**：最低限度的必要访问
### 数据保护
- **静态加密**：加密存储的数据
- **传输中加密**：用于连接的 TLS/SSL
- **屏蔽**：隐藏非生产中的敏感数据
- **标记化**：用标记替换敏感数据
### 常见漏洞
- **SQL注入**：用户输入中的恶意SQL
- **权限提升**：获得未经授权的访问
- **审核日志记录**：跟踪所有数据库活动
- **合规性**：GDPR、HIPAA、PCI-DSS 要求
## 现代数据库技术
### 云数据库
- **AWS**：RDS、Aurora、DynamoDB、Redshift
- **Google Cloud**：Cloud SQL、Spanner、Bigtable、Firestore
- **Azure**：SQL 数据库、Cosmos DB、Synapse
- **优点**：托管服务、自动扩展、包括备份
### NewSQL 数据库
- 将 SQL 一致性与 NoSQL 可扩展性相结合
- **示例**：CockroachDB、TiDB、YugabyteDB、Google Spanner
- **特性**：分布式、ACID 事务、水平扩展
### 时间序列数据库
- 针对带时间戳的数据进行了优化
- **示例**：InfluxDB、TimescaleDB、Prometheus
- **用例**：物联网、监控、财务数据
### 矢量数据库
- 存储和查询嵌入向量
- **示例**：Pinecone、Milvus、Weaviate、Qdrant
- **用例**：语义搜索、推荐系统、人工智能应用
### 多模型数据库
- 在单个系统中支持多种数据模型
- **示例**：ArangoDB、OrientDB、Azure Cosmos DB
- **优点**：无需多个数据库即可实现灵活性
## ORM 和数据访问
### 对象关系映射
- **目的**：将数据库表映射到编程对象
- **流行的 ORM**：
  - Python：SQLAlchemy、Django ORM、Peewee
  - JavaScript：Sequelize、Prisma、TypeORM
  - Java：Hibernate、JPA
  - 红宝石：ActiveRecord
  - .NET：实体框架
### 好处
- 从 SQL 中抽象
- 类型安全
- 迁移管理
- 查询构建API
### 缺点
- 性能开销
- 复杂的查询更难编写
- N+1查询问题
- 学习曲线
## 数据库管理
### DBA 职责
- 安装和配置
- 性能调整
- 备份和恢复
- 安全管理
- 容量规划
- 监控和警报
- 补丁管理
### 监控指标
- 查询响应时间
- 吞吐量（每秒事务数）
- 连接数
- 缓存命中率
- 磁盘输入/输出
- 锁定等待时间
- 复制滞后
### 维护任务
- **真空/分析**：更新统计数据，回收空间
- **索引重建**：整理索引碎片
- **统计更新**：让查询优化器随时了解情况
- **日志轮换**：管理日志文件大小
- **容量规划**：预测增长，规划升级