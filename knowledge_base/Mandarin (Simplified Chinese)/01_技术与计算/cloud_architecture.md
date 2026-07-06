# 云架构

## 云计算基础

### 什么是云计算？
云计算是指通过互联网按需交付计算资源（服务器、存储、数据库、网络、软件），并按使用量计费。

### 基本特征（NIST 定义）
- **按需自助服务**：无需人工交互即可配置资源
- **广泛的网络访问**：通过标准机制经网络访问
- **资源池化**：采用多租户模型并动态分配资源
- **快速弹性**：能够快速向外扩展和向内收缩
- **可度量服务**：资源使用情况可被监控并计费

### 云部署模型
- **公有云**：由云服务提供商拥有，基础设施共享（AWS、Azure、GCP）
- **私有云**：专供单个组织使用（本地部署或托管）
- **混合云**：公有云与私有云的组合
- **多云**：同时使用多个公有云提供商
- **社区云**：由具有共同诉求的多个组织共享

### 服务模型

#### 基础设施即服务（IaaS）
- **提供内容**：虚拟机、存储、网络、操作系统
- **示例**：AWS EC2、Google Compute Engine、Azure VMs
- **使用场景**：迁移现有系统、开发环境、需要高度控制的场景

#### 平台即服务（PaaS）
- **提供内容**：开发平台、数据库、中间件
- **示例**：Heroku、Google App Engine、AWS Elastic Beanstalk
- **使用场景**：应用开发、API 部署、微服务

#### 软件即服务（SaaS）
- **提供内容**：通过互联网交付的完整应用程序
- **示例**：Salesforce、Google Workspace、Microsoft 365、Slack
- **使用场景**：电子邮件、CRM、协作、业务应用

#### 函数即服务（FaaS）/ 无服务器
- **提供内容**：事件驱动的函数执行
- **示例**：AWS Lambda、Azure Functions、Google Cloud Functions
- **使用场景**：事件处理、API、定时任务、实时处理

## 主要云服务提供商

### Amazon Web Services (AWS)
- **市场份额**：约 32%（最大提供商）
- **核心服务**：
  - 计算：EC2、Lambda、ECS、EKS
  - 存储：S3、EBS、Glacier
  - 数据库：RDS、DynamoDB、Aurora
  - 网络：VPC、Route 53、CloudFront
  - AI/ML：SageMaker、Rekognition、Comprehend

### Microsoft Azure
- **市场份额**：约 23%
- **优势**：企业集成、混合云、微软生态系统
- **核心服务**：
  - 计算：Virtual Machines、Azure Functions、AKS
  - 存储：Blob Storage、Disk Storage
  - 数据库：SQL Database、Cosmos DB
  - 网络：Virtual Network、Traffic Manager
  - AI/ML：Azure ML、Cognitive Services

### Google Cloud Platform (GCP)
- **市场份额**：约 10%
- **优势**：数据分析、AI/ML、Kubernetes
- **核心服务**：
  - 计算：Compute Engine、Cloud Functions、GKE
  - 存储：Cloud Storage、Persistent Disk
  - 数据库：Cloud SQL、Firestore、Bigtable
  - 分析：BigQuery、Dataflow、Pub/Sub
  - AI/ML：Vertex AI、AutoML

### 其他提供商
- **IBM Cloud**：聚焦企业市场，提供 Watson AI
- **Oracle Cloud**：擅长数据库工作负载和企业应用
- **Alibaba Cloud**：在亚太地区占主导地位
- **DigitalOcean**：对开发者友好，产品更简洁

## 云架构模式

### 良好架构框架原则

#### 卓越运营
- 自动化运维
- 频繁进行可逆变更
- 持续优化流程
- 预判故障

#### 安全性
- 建立强健的身份体系基础
- 实现可追踪性
- 在所有层面落实安全防护
- 自动化安全最佳实践
- 保护传输中与静态数据

#### 可靠性
- 测试恢复流程
- 在故障发生后自动恢复
- 通过横向扩展提升可用性
- 不再依靠容量猜测
- 通过自动化管理变更

#### 性能效率
- 让高级技术更易获取
- 在几分钟内实现全球部署
- 使用无服务器架构
- 更频繁地进行实验
- 考虑硬件特性适配

#### 成本优化
- 采用按需消费模式
- 衡量整体效率
- 避免在无差异化工作上花钱
- 分析并归因支出
- 使用托管服务

### 常见架构模式

#### 微服务架构
- 将应用拆分为小型、独立的服务
- 每个服务拥有自己的数据和逻辑
- 通过 API（REST、gRPC、消息）通信
- 可独立部署
- **优势**：可扩展性强、故障隔离好、技术栈多样
- **挑战**：分布式复杂性、数据一致性、监控难度

#### 事件驱动架构
- 组件通过事件通信
- 生产者发布事件，消费者作出响应
- **模式**：事件溯源、CQRS、发布/订阅
- **技术**：Kafka、SNS/SQS、EventBridge、Pub/Sub
- **优势**：松耦合、可扩展、适合实时处理

#### 无服务器架构
- 无需管理服务器
- 按执行次数付费
- 自动伸缩
- **组件**：函数、API Gateway、托管服务
- **优势**：成本效率高、运维负担低、部署快速
- **注意事项**：冷启动、供应商锁定、执行时长限制

#### 分层架构（N 层）
- 表示层（UI）
- 应用层 / 业务逻辑层
- 数据访问层
- 数据库层
- **优势**：关注点分离、易于维护
- **常见场景**：三层 Web 应用

#### 空间基础架构
- 通过分布式数据处理高并发
- 在多台服务器之间实现虚拟化内存
- 处理节点可独立扩展
- **使用场景**：高吞吐、低延迟应用

## 计算服务

### 虚拟机
- **类型**：通用型、计算优化型、内存优化型、GPU
- **计费方式**：按需、预留实例、竞价实例
- **管理**：自动伸缩组、负载均衡器
- **最佳实践**：规格匹配、资源打标、监控、补丁管理

### 容器
- **Docker**：容器运行时标准
- **编排**：Kubernetes（EKS、AKS、GKE）、ECS、Fargate
- **优势**：可移植性、高效率、一致性
- **镜像仓库**：ECR、GCR、ACR、Docker Hub

### 无服务器函数
- **执行模型**：事件触发、无状态
- **限制**：执行时长、内存、并发执行数
- **使用场景**：API、文件处理、定时任务、IoT 后端
- **监控**：调用次数、错误、持续时间、冷启动

## 存储解决方案

### 对象存储
- **特点**：扁平结构、元数据、HTTP 访问
- **示例**：AWS S3、Google Cloud Storage、Azure Blob
- **使用场景**：静态资源、备份、数据湖、归档
- **存储类别**：热、冷、归档等（成本和访问速度不同）

### 块存储
- **特点**：原始卷，挂载到虚拟机
- **示例**：AWS EBS、Google Persistent Disk、Azure Disks
- **使用场景**：数据库、启动卷、高性能需求
- **类型**：SSD、HDD、预置 IOPS

### 文件存储
- **特点**：共享文件系统，使用 NFS/SMB 协议
- **示例**：AWS EFS、Google Filestore、Azure Files
- **使用场景**：内容管理、共享配置、整体迁移

### 归档存储
- **特点**：成本最低，但检索有延迟
- **示例**：S3 Glacier、Azure Archive Storage
- **使用场景**：合规、长期备份、历史数据

## 数据库服务

### 托管关系型数据库
- **服务**：AWS RDS/Aurora、Google Cloud SQL、Azure SQL Database
- **特性**：自动备份、补丁管理、扩缩容、复制
- **引擎**：MySQL、PostgreSQL、MariaDB、Oracle、SQL Server

### NoSQL 数据库
- **文档型**：DocumentDB、Firestore、Cosmos DB
- **键值型**：DynamoDB、Redis Cache
- **列族型**：Bigtable、Cassandra（托管）
- **图数据库**：Neptune、Cosmos DB（graph API）

### 数据仓库
- **服务**：Snowflake、Redshift、BigQuery、Synapse
- **特点**：列式存储、MPP 架构
- **使用场景**：分析、BI、大规模数据分析

### 缓存服务
- **内存型**：ElastiCache（Redis/Memcached）、Cloud Memorystore
- **CDN 缓存**：CloudFront、Cloud CDN、Azure CDN
- **使用场景**：会话存储、查询缓存、内容分发

## 网络

### 虚拟网络
- **VPC/VNet**：隔离的网络环境
- **子网**：公有（面向互联网）、私有（仅内部使用）
- **IP 地址规划**：CIDR 网段、IPv4/IPv6
- **路由表**：控制流量路径

### 负载均衡
- **类型**：应用型（L7）、网络型（L4）、网关型
- **特性**：健康检查、SSL 终止、会话保持
- **服务**：ELB/ALB/NLB、Cloud Load Balancing、Azure Load Balancer

### 内容分发网络（CDN）
- **目的**：在边缘节点缓存内容
- **优势**：降低延迟、减少源站负载、实现全球分发
- **服务**：CloudFront、Cloud CDN、Azure CDN、Akamai

### DNS 服务
- **功能**：域名注册、流量路由、健康检查
- **服务**：Route 53、Cloud DNS、Azure DNS
- **路由策略**：简单、加权、基于延迟、地理位置、故障转移

### 连接选项
- **Internet Gateway**：提供公网访问
- **NAT Gateway**：让私有子网能够出站访问
- **VPN**：连接本地环境的加密隧道
- **Direct Connect/ExpressRoute**：专用私有连接
- **VPC Peering**：连接同一账户或跨账户的 VPC

## 云中的安全

### 共享责任模型
- **提供商责任**：云本身的安全（基础设施）
- **客户责任**：云中内容的安全（数据、应用、访问）
- **因服务而异**：托管程度越高，提供商承担的责任越多

### 身份与访问管理（IAM）
- **用户**：个人身份
- **组**：用户集合
- **角色**：供服务或用户临时使用的凭证
- **策略**：定义权限的 JSON 文档
- **原则**：最小权限、职责分离

### 网络安全
- **安全组**：面向实例的有状态防火墙
- **网络 ACL**：面向子网的无状态防火墙
- **Web 应用防火墙（WAF）**：防御 Web 攻击
- **DDoS 防护**：Shield、Cloud Armor、DDoS Protection

### 数据保护
- **静态加密**：KMS、客户管理密钥
- **传输加密**：TLS/SSL、HTTPS
- **密钥管理**：HSM、密钥轮换、审计追踪
- **密钥与凭据管理**：Secrets Manager、Key Vault

### 合规与治理
- **认证**：SOC 2、ISO 27001、HIPAA、PCI-DSS、GDPR
- **工具**：策略执行、合规报告、审计日志
- **框架**：Cloud Security Alliance、NIST CSF

## 云中的 DevOps

### CI/CD 服务
- **AWS**：CodePipeline、CodeBuild、CodeDeploy
- **Azure**：Azure DevOps、GitHub Actions
- **GCP**：Cloud Build、Cloud Deploy
- **第三方**：Jenkins、CircleCI、GitLab CI

### 基础设施即代码（IaC）
- **Terraform**：多云、声明式、带状态管理
- **CloudFormation**：AWS 原生，使用 YAML/JSON 模板
- **ARM Templates**：Azure 原生
- **Deployment Manager**：GCP 原生
- **Pulumi**：使用编程语言定义基础设施
- **优势**：版本控制、可重复性、文档化

### 配置管理
- **Ansible**：无代理，使用 YAML Playbook
- **Chef**：基于 Ruby，生态成熟
- **Puppet**：声明式，报告能力强
- **SaltStack**：速度快，基于 Python

### 监控与可观测性
- **指标**：CloudWatch、Cloud Monitoring、Azure Monitor
- **日志**：CloudWatch Logs、Cloud Logging、Log Analytics
- **链路追踪**：X-Ray、Cloud Trace、Application Insights
- **仪表板**：CloudWatch Dashboards、Cloud Console
- **告警**：SNS、Cloud Monitoring alerts、Action Groups

### 容器编排
- **Kubernetes**：行业标准编排平台
- **托管服务**：EKS、AKS、GKE
- **服务网格**：Istio、Linkerd（流量管理、安全）
- **GitOps**：ArgoCD、Flux（声明式部署）

## 成本管理

### 定价模型
- **按需付费**：按实际使用量计费
- **预留实例**：承诺使用 1-3 年，折扣显著
- **竞价实例**：竞拍闲置容量，可能被中断
- **Savings Plans**：更灵活的承诺式定价
- **免费层**：新账户可享有限免费额度

### 成本优化策略
- **合理选型**：让实例规格匹配工作负载需求
- **自动伸缩**：根据需求自动扩缩容
- **预留容量**：适用于稳定负载的长期承诺
- **使用竞价资源**：适用于容错性强、弹性大的工作负载
- **存储分层**：将低频数据迁移到更便宜的层级
- **清理**：删除未使用的资源、快照、AMI

### 成本管理工具
- **AWS**：Cost Explorer、Budgets、Trusted Advisor
- **Azure**：Cost Management、Advisor
- **GCP**：Billing reports、Recommender
- **第三方**：CloudHealth、CloudCheckr、Datadog

## 高可用性与灾难恢复

### 可用性概念
- **可用区**：区域内物理隔离的数据中心
- **区域**：包含多个可用区的地理区域
- **边缘节点**：全球分布的 CDN 缓存节点

### 高可用策略
- **Multi-AZ**：跨可用区部署
- **自动修复**：自动替换故障实例
- **负载均衡**：将流量分配到健康实例
- **数据库复制**：多可用区部署、只读副本

### 灾难恢复策略
- **备份与恢复**：定期备份，灾难发生时恢复（成本最低）
- **Pilot Light**：核心组件持续运行，灾难时再扩容
- **Warm Standby**：始终运行缩小版环境
- **多站点 Active/Active**：多个区域同时运行完整生产环境（成本最高）

### RTO 与 RPO
- **恢复时间目标（RTO）**：可接受的最长停机时间
- **恢复点目标（RPO）**：可接受的最大数据丢失量
- **策略选择**：取决于业务需求和预算

## 新兴趋势

### 边缘计算
- 在更接近数据源的位置处理数据
- **服务**：AWS Outposts、Wavelength、Azure Edge、Cloud CDN
- **使用场景**：IoT、实时分析、低延迟应用

### 多云与混合云
- 避免供应商锁定
- 利用各家最优服务
- **工具**：Terraform、Anthos、Arc、CloudHealth

### AI/ML 服务
- 预训练模型：视觉、语音、语言
- 自定义模型训练：SageMaker、Vertex AI、Azure ML
- MLOps：模型部署、监控、治理

### 量子计算
- **服务**：AWS Braket、Azure Quantum
- **阶段**：仍处于早期实验阶段
- **潜力**：密码学、优化、药物发现

### 可持续云
- 碳足迹追踪
- 可再生能源承诺
- 高效利用资源
- 绿色架构模式
