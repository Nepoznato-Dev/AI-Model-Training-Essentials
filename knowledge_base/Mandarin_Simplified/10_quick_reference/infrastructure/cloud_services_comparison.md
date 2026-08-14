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
  - name: "Nepoznato-Dev"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.1"
    date: "2026-08-09"
    author: "Nepoznato-Dev"
    changes: "Moved to infrastructure/ subfolder; added subcategory field"
  - version: "1.0.0"
    date: "2026-08-05"
    author: "Nepoznato-Dev"
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
# 云服务比较
对三大云提供商（AWS、Azure 和 Google Cloud）在计算、存储、数据库、AI/ML、网络、监控和基础设施即代码方面进行并排比较。对于架构师决定使用哪个平台或将服务从一个云映射到另一个云很有用。
---

## 提供商概述
| |亚马逊AWS |天蓝色|谷歌云（GCP）|
|---|-----|--------------------|---------------------|
| **市场份额** | ~31%（最大）| ~25%（第二）| ~11%（第三，增长最快）|
| **优势** |服务范围；到期;生态系统|企业整合；混合云；微软堆栈|数据/人工智能；库伯内特斯；全球网络|
| **最适合** |初创企业到企业；最广泛的服务目录|拥有 Microsoft/Active Directory 的企业；混合动力 |数据密集型工作负载； Kubernetes 原生；人工智能/机器学习 |
| **地区** | 33 个地区，105 个可用区 | 60+ 地区 | 40+地区，100+专区 |
| **免费套餐** | 12 个月免费套餐 + 始终免费 | 12 个月免费 + 200 美元积分 | 90 天 300 美元积分 + 永远免费 |
---

## 计算
|服务类别 |亚马逊AWS |天蓝色| GCP |
|----------------|-----|--------|-----|
| **虚拟机** | EC2（弹性计算云）|虚拟机 |计算引擎 |
| **自动缩放** | Auto Scaling 组 |虚拟机规模集|实例组 |
| **无服务器功能** |拉姆达 | Azure 函数 |云功能|
| **容器注册表** | ECR（弹性容器注册表）| Azure 容器注册表 |工件注册表 |
| **容器编排** | ECS / EKS | ACS/AKS | GKE / 云运行 |
| **无服务器容器** |法尔盖特 |容器应用程序 |云跑|
| **应用程序平台（PaaS）** | Elastic Beanstalk，应用程序运行器 |应用服务|应用程序引擎 |
| **批处理** | AWS 批处理 | Azure 批量 |云批量|
| **GPU / AI 计算** | EC2（P4d、P5 实例）| NC/ND 系列虚拟机 | A2/A3 虚拟机； TPU |
### VM 定价模型
|型号|亚马逊AWS |天蓝色| GCP |
|--------|-----|--------|-----|
| **按需** |按需实例 |按量付费 |点播 |
| **保留/承诺** |预留实例（1-3 年）|预留虚拟机（1-3 年）|承诺使用折扣（1-3 年）|
| **现货/可中断** |现货实例 | Spot 虚拟机 |抢占式/现货虚拟机 |
| **储蓄计划** |储蓄计划|储蓄计划|承诺使用折扣|
---

＃＃ 贮存
|服务类别 |亚马逊AWS |天蓝色| GCP |
|----------------|-----|--------|-----|
| **对象存储** | S3 | Blob 存储 |云存储|
| **块存储** |电子BS |托管磁盘 |持久磁盘 |
| **文件存储** | EFS、FSx | Azure 文件 |文件存储 |
| **存档/冷** | S3 冰川，深度存档 | Blob 酷/存档层 |云存储 Coldline/Archive |
| **数据传输** |雪球、数据同步 |数据盒|转移设备|
### 存储类别比较
|使用案例| AWS S3 | AWS S3蓝色斑点 | GCP 云存储 |
|----------|--------|------------|--------------------|
| **频繁访问** | S3标准|热门 |标准|
| **不频繁访问** | S3 标准-IA |酷|近线|
| **稀有访问** | S3 一区-IA | — |冷线|
| **存档** | S3 冰川/深度档案 |档案 |档案 |
---

## 数据库
|服务类别 |亚马逊AWS |天蓝色| GCP |
|----------------|-----|--------|-----|
| **关系（托管）** | RDS（MySQL、PostgreSQL、Oracle、SQL Server）| Azure 数据库（MySQL、PostgreSQL）； Azure SQL |云 SQL（MySQL、PostgreSQL）|
| **关系（云原生）** | Aurora（兼容 MySQL/PostgreSQL）| Azure SQL 数据库（弹性池）| Cloud Spanner（全球分布）|
| **NoSQL（文档）** | DynamoDB | Cosmos DB（MongoDB API、SQL API）|火库；数据存储 |
| **NoSQL（宽列）** | DynamoDB（也）| Cosmos DB（卡桑德拉 API）|大表|
| **NoSQL（键值）** | DynamoDB、ElastiCache |用于 Redis 的 Azure 缓存 |内存存储（Redis）|
| **图表** |海王星| Cosmos DB（Gremlin API）| — |
| **时间序列** |时间流 | Azure 数据资源管理器 | — |
| **分类帐** | QLDB | Azure 机密账本 | — |
| **内存缓存** | ElastiCache（Redis、Memcached）|用于 Redis 的 Azure 缓存 |记忆库|
| **搜索** |开放搜索服务| Azure 人工智能搜索 |云搜索；顶点人工智能搜索 |
| **数据仓库** |红移|突触分析 | BigQuery |
---

## 人工智能和机器学习
|服务类别 |亚马逊AWS |天蓝色| GCP |
|----------------|-----|--------|-----|
| **机器学习平台** | SageMaker| Azure 机器学习 |顶点人工智能 |
| **预训练的 API** | Rekognition（视觉）、Polly (TTS)、理解 (NLP)、转录 |认知服务（视觉、言语、语言、决策）|视觉 AI、语音转文本、自然语言 API |
| **法学硕士/生成人工智能** |基岩（克劳德、美洲驼、泰坦）| Azure OpenAI 服务（GPT-4、DALL-E）|顶点人工智能（双子座）；模型花园|
| **矢量/嵌入** | OpenSearch (k-NN)，基岩知识库 | Azure AI 搜索（矢量）| Vertex AI 矢量搜索、AlloyDB |
| **MLOps** | SageMaker Pipelines、模型注册表 | Azure ML Pipelines、模型注册表 | Vertex AI Pipelines、模型注册表 |
| **数据标签** | SageMaker 地面真相 | Azure ML 数据标签 | Vertex AI 数据标签 |
| **对话式人工智能** |莱克斯 | Azure 机器人服务 | Dialogflow CX / ES |
| **翻译** |翻译 |译者|翻译API |
---

## 网络
|服务类别 |亚马逊AWS |天蓝色| GCP |
|----------------|-----|--------|-----|
| **虚拟网络** |专有网络|虚拟网络 (VNet) |专有网络|
| **负载平衡** | ELB/ALB/NLB/CLB |负载均衡器（应用程序、网络、网关）|云负载均衡|
| **DNS** | 53 号公路 | Azure DNS |云域名解析 |
| **CDN** |云前 |蔚蓝前门|云CDN |
| **API网关** | API网关| API管理| API网关|
| **VPN** |站点到站点 VPN、客户端 VPN | VPN网关|云VPN |
| **直接连接/ ExpressRoute** |直接连接 |快速路线 |云互联|
| **私人链接** | PrivateLink、VPC 端点 |私有链接、私有端点 |私人服务连接 |
| **防火墙** | WAF，网络防火墙| Azure 防火墙、WAF |云甲、防火​​墙|
| **DDoS 防护** |盾牌标准/高级| DDoS 防护 |云甲|
---

## 监控和日志记录
|服务类别 |亚马逊AWS |天蓝色| GCP |
|----------------|-----|--------|-----|
| **指标/监控** |云观察| Azure 监视器 |云监控（Stackdriver）|
| **记录** | CloudWatch 日志 |日志分析（Azure Monitor 日志）|云日志|
| **追踪** | X 射线 |应用洞察 |云踪|
| **警报** | CloudWatch 警报 | Azure 监视器警报 |云监控警报|
| **仪表板** | CloudWatch 仪表板 | Azure 工作簿/仪表板 |云监控仪表板|
| **错误跟踪** | CloudWatch 合成 |应用洞察 |云错误报告 |
| **第三方** | Datadog、New Relic、PagerDuty | Datadog、New Relic、PagerDuty | Datadog、New Relic、PagerDuty |
---

## 基础设施即代码和 DevOps
|服务类别 |亚马逊AWS |天蓝色| GCP |
|----------------|-----|--------|-----|
| **IaC（本地）** |云形成| ARM 模板/二头肌 |部署经理/Pulumi |
| **IaC（跨云）** | Terraform、Pulumi、CDK | Terraform、Pulumi、二头肌 | Terraform，普鲁米 |
| **CI/CD** |代码管道、代码构建 | Azure DevOps、GitHub 操作 |云构建；云部署|
| **容器注册表** |电子CR | Azure 容器注册表 |工件注册表 |
| **GitOps** |应用网格 + Flux/ArgoCD | AKS 上的 Flux/ArgoCD |配置同步 (Anthos) |
| **秘密管理** |秘密管理器，SSM 参数存储 |密钥库 |秘密经理|
---

## 定价考虑因素
|因素|亚马逊AWS |天蓝色| GCP |
|--------|-----|--------|-----|
| **计费粒度** |每秒（对于某些人来说，第一个小时之后）|每秒 |每秒 |
| **持续使用折扣** |预留实例/节省计划 |预留虚拟机 |承诺使用折扣|
| **现货实例** |高达 90% 折扣 |高达 90% 折扣 |高达 91% 折扣 |
| **数据出口** |收费（昂贵）|收费|无论目的地如何，价格相同（通常更便宜）|
| **免费套餐** | 12 个月 + 永远免费 | 12 个月 + 200 美元积分 | 90 天 300 美元 + 永久免费 |
| **企业折扣** |企业折扣计划 (EDP) | MACC（货币承诺合同）|承诺使用 + CUD |
---

## 何时使用哪个
|场景|推荐|为什么 |
|----------|-------------|-----|
| **最广泛的服务选择；成熟的生态系统** |亚马逊AWS |最大的目录；大多数第三方集成|
| **微软企业；活动目录；混合** |天蓝色|原生AD集成；强大的混合工具|
| **数据仓库；大查询；分析重度** | GCP | BigQuery 是同类中最好的；无缝数据集成|
| **Kubernetes 原生开发** | GCP | GKE 是最完善的托管 Kubernetes |
| **生成式人工智能/法学硕士应用** | Azure 或 GCP |适用于 GPT 模型的 Azure OpenAI； Vertex AI 双子座 |
| **全球规模、低延迟应用** | GCP |谷歌的全球网络是真正的优势|
| **政府/合规性工作负载** | AWS 或 Azure |大多数合规认证； GovCloud 区域 |
| **成本敏感的初创公司** | GCP 或 AWS | GCP 的免费套餐非常慷慨； AWS 拥有启动积分 |
| **现有的 Microsoft / .NET 堆栈** |天蓝色|与 Visual Studio、.NET、Office 365 紧密集成 |
| **多云策略** | Terraform + 所有三个 |使用 Terraform 跨云管理资源 |
---

＃＃ 概括
这三种云都是强大、可靠且不断扩展的。选择通常归结为：您的团队已经知道什么，您现有的合同是什么样的，以及哪些特定服务对您的工作负载很重要。多云越来越普遍——使用 Terraform 或 Pulumi 来避免基础设施层的供应商锁定，并选择每种云最擅长的功能。