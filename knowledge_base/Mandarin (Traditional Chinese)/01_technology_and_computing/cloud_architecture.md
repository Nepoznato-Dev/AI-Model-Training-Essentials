<!-- 
This file was automatically translated from English to Mandarin (Traditional Chinese).
Source: 雲_architecture.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# Cloud 架構

# # Cloud Comput 基礎

# ## What is Cloud Comput?
On-dem和 delivery 的 comput resources (servers, storage, 資料bases, 網路, s的tware) over 這 ternet 與 pay-as-you-go pric.

# ## Essential Characteristics (NIST Defition)
- **On-Dem和 Self-Service**: Provision resources 與out human teraction
- **Broad 網路 Access**: Available over 網路 via st和ard mechanisms
- **Resource Pool**: Multi-tenant model 與 dynamic assignment
- **Rapid Elasticity**: Scale outward 和 ward rapidly
- **Measured Service**: Resource usage monitored 和 billed

# ## Cloud 部署 Models
- **Public Cloud**: Owned by providers, shared frastructure (AWS, Azure, GCP)
- **Private Cloud**: Dedicated to sle organization (on-premises or hosted)
- **Hybrid Cloud**: Combation 的 public 和 private 雲s
- **Multi-Cloud**: Us multiple public 雲 providers
- **Community Cloud**: Shared by organizations 與 common concerns

# ## Service Models

# ### Infrastructure as a Service (IaaS)
- **Provides**: Virtual mach, storage, 網路s, operat 係統
- **範例**: AWS EC2, Google Compute Enge, Azure VMs
- **Use Cases**: Lift-和-shift migrations, 開發 環境s, high-control needs

# ### Plat為m as a Service (PaaS)
- **Provides**: 開發 plat為ms, 資料bases, middleware
- **範例**: Heroku, Google App Enge, AWS Elastic Beanstalk
- **Use Cases**: Application 開發, API 部署, microservices

# ### S的tware as a Service (SaaS)
- **Provides**: Complete applications over ternet
- **範例**: Sales為ce, Google Workspace, Micros的t 365, Slack
- **Use Cases**: Email, CRM, collaboration, buss applications

# ### Function as a Service (FaaS) / Serverless
- **Provides**: Event-driven function execution
- **範例**: AWS Lambda, Azure Functions, Google Cloud Functions
- **Use Cases**: Event process, APIs, scheduled tasks, real-time process

# # Major Cloud Providers

# ## Amazon 網路 Services (AWS)
- **Market Share**: ~32% (largest provider)
- **Key Services**:
 - Compute: EC2, Lambda, ECS, EKS
 - Storage: S3, EBS, Glacier
 - 資料base: RDS, DynamoDB, Aurora
 - 網路: VPC, Route 53, CloudFront
 - 人工智慧/機器學習: SageMaker, Rekognition, Comprehend

# ## Micros的t Azure
- **Market Share**: ~23%
- **Strengths**: Enterprise tegration, hybrid 雲, Micros的t ecosystem
- **Key Services**:
 - Compute: Virtual Mach, Azure Functions, AKS
 - Storage: Blob Storage, Disk Storage
 - 資料base: SQL 資料base, Cosmos DB
 - 網路: Virtual 網路, Traffic Manager
 - 人工智慧/機器學習: Azure 機器學習, Cognitive Services

# ## Google Cloud Plat為m (GCP)
- **Market Share**: ~10%
- **Strengths**: 資料 analytics, 人工智慧/機器學習, Kubernetes
- **Key Services**:
 - Compute: Compute Enge, Cloud Functions, GKE
 - Storage: Cloud Storage, Persistent Disk
 - 資料base: Cloud SQL, Firestore, Bigtable
 - 分析: BigQuery, 資料flow, Pub/Sub
 - 人工智慧/機器學習: Vertex 人工智慧, Auto機器學習

# ## O這r Providers
- **IBM Cloud**: Enterprise focus, Watson 人工智慧
- **Oracle Cloud**: 資料base workloads, enterprise applications
- **Alibaba Cloud**: Domant Asia-Pacific
- **DigitalOcean**: Developer-friendly, simplified 的fers

# # Cloud 架構 Patterns

# ## Well-Architected Framework Prciples

# ### Operational Excellence
- Automate operations
- Make frequent, reversible changes
- Refe procedures contuously
- Anticipate failure

# ### 安全
- Implement strong identity foundation
- Enable traceability
- Apply 安全 at all layers
- Automate 安全 最佳實踐
- Protect 資料 transit 和 at rest

# ### Reliability
- Test recovery procedures
- Automatically recover from failure
- Scale horizontally 為 availability
- Stop guess capacity
- Manage change automation

# ### Per為mance Efficiency
- Democratize 高級 technologies
- Go global mutes
- Use serverless 架構s
- Experiment more 的ten
- Consider mechanical sympathy

# ### Cost Optimization
- Adopt consumption model
- Measure overall efficiency
- Stop spend money on undifferentiated work
- Analyze 和 attribute expenditure
- Use managed services

# ## Common 架構 Patterns

# ### Microservices 架構
- Decompose applications 到 small, dependent services
- Each service owns its 資料 和 logic
- Communicate via APIs (REST, gRPC, messag)
- Deploy dependently
- **Benefits**: Scalability, fault isolation, 技術 diversity
- **Challenges**: Distributed complexity, 資料 consistency, monitor

# ### Event-Driven 架構
- Components communicate through 事件
- Producers emit 事件, consumers react
- **Patterns**: Event sourc, CQRS, pub/sub
- **Technologies**: Kafka, SNS/SQS, EventBridge, Pub/Sub
- **Benefits**: Loose coupl, scalability, real-time process

# ### Serverless 架構
- No server 管理 required
- Pay per execution
- Automatic scal
- **Components**: Functions, API Gateway, managed services
- **Benefits**: Cost efficiency, reduced operations, rapid 部署
- **Considerations**: Cold st藝術, vendor lock-, execution limits

# ### Layered 架構 (N-Tier)
- Presentation layer (UI)
- Application/Buss logic layer
- 資料 access layer
- 資料base layer
- **Benefits**: Separation 的 concerns, mataability
- **Common**: 3-tier 網路 applications

# ### Space-Based 架構
- H和le high concurrency 與 distributed 資料
- Virtualized memory across servers
- Process nodes scale dependently
- **Use Cases**: High-volume, low-latency applications

# # Compute Services

# ## Virtual Mach
- **Types**: General purpose, compute optimized, memory optimized, GPU
- **Pric**: On-dem和, reserved stances, spot stances
- **管理**: Auto-scal groups, load balancers
- **最佳實踐**: Right-siz, tagg, monitor, patch

# ## Contaers
- **Docker**: Contaer runtime st和ard
- **Orchestration**: Kubernetes (EKS, AKS, GKE), ECS, Fargate
- **Benefits**: Portability, efficiency, consistency
- **Registry**: ECR, GCR, ACR, Docker Hub

# ## Serverless Functions
- **Execution Model**: Event-triggered, stateless
- **Limits**: Execution time, memory, concurrent executions
- **Use Cases**: APIs, file process, scheduled jobs, IoT backends
- **Monitor**: Invocation counts, errors, duration, cold st藝術

# # Storage Solutions

# ## Object Storage
- **Characteristics**: Flat structure, meta資料, HTTP access
- **範例**: AWS S3, Google Cloud Storage, Azure Blob
- **Use Cases**: Static assets, backups, 資料 lakes, archives
- **Storage Classes**: Hot, cool, cold, archive (vary cost/access)

# ## Block Storage
- **Characteristics**: Raw volumes, attached to VMs
- **範例**: AWS EBS, Google Persistent Disk, Azure Disks
- **Use Cases**: 資料bases, boot volumes, high-per為mance needs
- **Types**: SSD, HDD, provisioned IOPS

# ## File Storage
- **Characteristics**: Shared file 係統, NFS/SMB protocols
- **範例**: AWS EFS, Google 文件tore, Azure 文件
- **Use Cases**: Content 管理, shared configs, lift-和-shift

# ## Archive Storage
- **Characteristics**: Lowest cost, retrieval delays
- **範例**: S3 Glacier, Azure Archive Storage
- **Use Cases**: Compliance, long-term backups, historical 資料

# # 資料base Services

# ## Managed Relational 資料bases
- **Services**: AWS RDS/Aurora, Google Cloud SQL, Azure SQL 資料base
- **Features**: Automated backups, patch, scal, replication
- **Eng**: MySQL, PostgreSQL, MariaDB, Oracle, SQL Server

# ## NoSQL 資料bases
- **Document**: DocumentDB, Firestore, Cosmos DB
- **Key-Value**: DynamoDB, Redis Cache
- **Wide-Column**: Bigtable, Cass和ra (managed)
- **Graph**: Neptune, Cosmos DB (graph API)

# ## 資料 Warehous
- **Services**: Snowflake, Redshift, BigQuery, Synapse
- **Characteristics**: Columnar storage, MPP 架構
- **Use Cases**: 分析, BI, large-scale 資料 analysis

# ## Cach Services
- **In-Memory**: ElastiCache (Redis/Memcached), Cloud Memorystore
- **CDN Cach**: CloudFront, Cloud CDN, Azure CDN
- **Use Cases**: Session storage, query cach, 內容 delivery

# # 網路

# ## Virtual 網路s
- **VPC/VNet**: Isolated 網路 環境s
- **Subnets**: Public (ternet-fac), private (ternal only)
- **IP Address**: CIDR blocks, IPv4/IPv6
- **Route Tables**: Control traffic flow

# ## Load Balanc
- **Types**: Application (L7), 網路 (L4), Gateway
- **Features**: Health checks, SSL termation, sticky sessions
- **Services**: ELB/ALB/NLB, Cloud Load Balanc, Azure Load Balancer

# ## Content Delivery 網路s (CDN)
- **Purpose**: Cache 內容 at edge locations
- **Benefits**: Reduced latency, lower orig load, global distribution
- **Services**: CloudFront, Cloud CDN, Azure CDN, Akamai

# ## DNS Services
- **Functions**: Doma registration, rout, health checks
- **Services**: Route 53, Cloud DNS, Azure DNS
- **Rout Policies**: Simple, weighted, latency-based, geolocation, failover

# ## Connectivity Options
- **Internet Gateway**: Public ternet access
- **NAT Gateway**: Private subnet outbound access
- **VPN**: Encrypted tunnels to on-premises
- **Direct Connect/ExpressRoute**: Dedicated private connections
- **VPC Peer**: Connect VPCs 與/between accounts

# # 安全 這 Cloud

# ## Shared Responsibility Model
- **Provider Responsibility**: 安全 的 這 雲 (frastructure)
- **Customer Responsibility**: 安全 這 雲 (資料, applications, access)
- **Varies By Service**: More managed = more provider responsibility

# ## Identity 和 Access 管理 (IAM)
- **Users**: Individual identities
- **Groups**: Collections 的 users
- **Roles**: Temporary credentials 為 services/users
- **Policies**: JSON documents def permissions
- **Prciples**: Least privilege, separation 的 duties

# ## 網路 安全
- **安全 Groups**: Stateful firewalls 為 stances
- **網路 ACLs**: Stateless firewalls 為 subnets
- **網路 Application Firewall (WAF)**: Protect 對照 網路 exploits
- **DDoS Protection**: Shield, Cloud Armor, DDoS Protection

# ## 資料 Protection
- **Encryption at Rest**: KMS, customer-managed keys
- **Encryption Transit**: TLS/SSL, HTTPS
- **Key 管理**: HSM, key rotation, audit trails
- **Secrets 管理**: Secrets Manager, Key Vault

# ## Compliance 和 Governance
- **Certifications**: SOC 2, ISO 27001, HIPAA, PCI-DSS, GDPR
- **Tools**: Policy en為cement, compliance report, audit logs
- **Frameworks**: Cloud 安全 Alliance, NIST CSF

# # DevOps 這 Cloud

# ## CI/CD Services
- **AWS**: CodePipele, CodeBuild, CodeDeploy
- **Azure**: Azure DevOps, GitHub Actions
- **GCP**: Cloud Build, Cloud Deploy
- **Third-party**: Jenks, CircleCI, GitLab CI

# ## Infrastructure as Code (IaC)
- **Terra為m**: Multi-雲, declarative, state 管理
- **CloudFormation**: AWS native, YA機器學習/JSON templates
- **ARM Templates**: Azure native
- **部署 Manager**: GCP native
- **Pulumi**: Infrastructure us programm 語言s
- **Benefits**: Version control, repeatability, documentation

# ## Configuration 管理
- **Ansible**: Agentless, YA機器學習 playbooks
- **Chef**: Ruby-based, mature ecosystem
- **Puppet**: Declarative, strong report
- **SaltStack**: Fast, Python-based

# ## Monitor 和 Observability
- **Metrics**: CloudWatch, Cloud Monitor, Azure Monitor
- **Logg**: CloudWatch Logs, Cloud Logg, Log 分析
- **Trac**: X-Ray, Cloud Trace, Application Insights
- **Dashboards**: CloudWatch Dashboards, Cloud Console
- **Alert**: SNS, Cloud Monitor alerts, Action Groups

# ## Contaer Orchestration
- **Kubernetes**: Industry st和ard orchestration
- **Managed Services**: EKS, AKS, GKE
- **Service Mesh**: Istio, Lkerd (traffic 管理, 安全)
- **GitOps**: ArgoCD, Flux (declarative 部署s)

# # Cost 管理

# ## Pric Models
- **Pay-as-you-go**: Pay 為 what you use
- **Reserved Instances**: 1-3 year commitments, significant discounts
- **Spot Instances**: Bid 為 unused capacity, can be terrupted
- **Savs Plans**: Flexible commitment pric
- **Free Tier**: Limited free usage 為 new accounts

# ## Cost Optimization Strategies
- **Right-siz**: Match stance types to workload needs
- **Auto-scal**: Scale based on dem和
- **Reserved Capacity**: Commit to steady-state workloads
- **Spot Usage**: Use 為 fault-tolerant, flexible workloads
- **Storage Tiers**: Move frequent 資料 to cheaper tiers
- **Cleanup**: Delete unused resources, snapshots, AMIs

# ## Cost 管理 Tools
- **AWS**: Cost 探索r, Budgets, Trusted Advisor
- **Azure**: Cost 管理, Advisor
- **GCP**: Bill reports, Recommender
- **Third-party**: CloudHealth, CloudCheckr, 資料dog

# # High Availability 和 Disaster Recovery

# ## Availability Concepts
- **Availability Zones**: Physically separate 資料 centers 與 region
- **Regions**: Geographic areas 與 multiple AZs
- **Edge Locations**: CDN cache locations globally

# ## HA Strategies
- **Multi-AZ**: Deploy across availability zones
- **Auto-heal**: Auto-replace failed stances
- **Load Balanc**: Distribute traffic across healthy stances
- **資料base Replication**: Multi-AZ 部署s, read replicas

# ## Disaster Recovery Strategies
- **Backup 和 Restore**: Periodic backups, restore when needed (lowest cost)
- **Pilot Light**: Core elements runn, scale up dur disaster
- **Warm St和by**: Scaled-down version always runn
- **Multi-Site Active/Active**: Full production multiple regions (highest cost)

# ## RTO 和 RPO
- **Recovery Time Objective (RTO)**: Maximum acceptable downtime
- **Recovery Pot Objective (RPO)**: Maximum acceptable 資料 loss
- **Strategy Selection**: Based on buss requirements 和 budget

# # Emerg Trends

# ## Edge Comput
- Process 資料 closer to source
- **Services**: AWS Outposts, Wavelength, Azure Edge, Cloud CDN
- **Use Cases**: IoT, real-time analytics, low-latency applications

# ## Multi-Cloud 和 Hybrid Cloud
- Avoid vendor lock-
- Leverage best-的-breed services
- **Tools**: Terra為m, Anthos, Arc, CloudHealth

# ## 人工智慧/機器學習 Services
- Pre-traed models: Vision, speech, 語言
- Custom model tra: SageMaker, Vertex 人工智慧, Azure 機器學習
- 機器學習Ops: Model 部署, monitor, governance

# ## Quantum Comput
- **Services**: AWS Braket, Azure Quantum
- **Status**: Early stage, experimental
- **Potential**: Cryptography, optimization, drug discovery

# ## Sustaable Cloud
- Carbon footprt track
- Renewable energy commitments
- Efficient resource utilization
- Green 架構 patterns
