<!-- 
This file was automatically translated from English to Mandarin (Simplified Chinese).
Source: cloud_architecture.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# Cloud 架构

## Cloud 计算 基础

### What is Cloud 计算?
On-demand delivery 的 计算 resources (servers, storage, databases, networking, software) over 这 internet 与 pay-as-you-go pricing.

### Essential Characteristics (NIST Definition)
- **On-Demand Self-Service**: Provision resources without human interaction
- **Broad 网络 Access**: 可用 over 网络 via standard mechanisms
- **Resource Pooling**: Multi-tenant model 与 dynamic assignment
- **Rapid Elasticity**: Scale outward 和 inward rapidly
- **Measured Service**: Resource usage monitored 和 billed

### Cloud 部署 Models
- **Public Cloud**: Owned by providers, shared infrastructure (AWS, Azure, GCP)
- **Private Cloud**: Dedicated to single organization (on-premises or hosted)
- **Hybrid Cloud**: Combination 的 public 和 private clouds
- **Multi-Cloud**: Using multiple public cloud providers
- **Community Cloud**: Shared by organizations 与 common concerns

### Service Models

#### Infrastructure as a Service (IaaS)
- **Provides**: Virtual machines, storage, networks, operating 系统
- **示例**: AWS EC2, Google Compute Engine, Azure VMs
- **Use Cases**: Lift-和-shift migrations, 开发 environments, high-control needs

#### Platform as a Service (PaaS)
- **Provides**: 开发 platforms, databases, middleware
- **示例**: Heroku, Google App Engine, AWS Elastic Beanstalk
- **Use Cases**: Application 开发, API 部署, microservices

#### Software as a Service (SaaS)
- **Provides**: 完整 applications over internet
- **示例**: Salesforce, Google Workspace, Microsoft 365, Slack
- **Use Cases**: Email, CRM, collaboration, 商业 applications

#### Function as a Service (FaaS) / Serverless
- **Provides**: Event-driven function execution
- **示例**: AWS Lambda, Azure Functions, Google Cloud Functions
- **Use Cases**: Event processing, APIs, scheduled tasks, real-time processing

## Major Cloud Providers

### Amazon 网络 Services (AWS)
- **Market Share**: ~32% (largest provider)
- **Key Services**:
  - Compute: EC2, Lambda, ECS, EKS
  - Storage: S3, EBS, Glacier
  - 数据库: RDS, DynamoDB, Aurora
  - Networking: VPC, Route 53, CloudFront
  - AI/ML: SageMaker, Rekognition, Comprehend

### Microsoft Azure
- **Market Share**: ~23%
- **Strengths**: Enterprise integration, hybrid cloud, Microsoft ecosystem
- **Key Services**:
  - Compute: Virtual Machines, Azure Functions, AKS
  - Storage: Blob Storage, Disk Storage
  - 数据库: SQL 数据库, Cosmos DB
  - Networking: Virtual 网络, Traffic Manager
  - AI/ML: Azure ML, Cognitive Services

### Google Cloud Platform (GCP)
- **Market Share**: ~10%
- **Strengths**: 数据 analytics, AI/ML, Kubernetes
- **Key Services**:
  - Compute: Compute Engine, Cloud Functions, GKE
  - Storage: Cloud Storage, Persistent Disk
  - 数据库: Cloud SQL, Firestore, Bigtable
  - Analytics: BigQuery, Dataflow, Pub/Sub
  - AI/ML: Vertex AI, AutoML

### Other Providers
- **IBM Cloud**: Enterprise focus, Watson AI
- **Oracle Cloud**: 数据库 workloads, enterprise applications
- **Alibaba Cloud**: Dominant 在 Asia-Pacific
- **DigitalOcean**: Developer-friendly, simplified offerings

## Cloud 架构 Patterns

### Well-Architected Framework Principles

#### Operational Excellence
- Automate operations
- Make frequent, reversible changes
- Refine procedures continuously
- Anticipate failure

#### 安全
- Implement strong identity foundation
- Enable traceability
- Apply 安全 at all layers
- Automate 安全 最佳实践
- Protect 数据 在 transit 和 at rest

#### Reliability
- Test recovery procedures
- Automatically recover from failure
- Scale horizontally 为 availability
- Stop guessing capacity
- Manage change 在 automation

#### 性能 Efficiency
- Democratize 高级 technologies
- Go global 在 minutes
- Use serverless architectures
- Experiment more often
- Consider mechanical sympathy

#### Cost Optimization
- Adopt consumption model
- Measure overall efficiency
- Stop spending money on undifferentiated work
- Analyze 和 attribute expenditure
- Use managed services

### Common 架构 Patterns

#### Microservices 架构
- Decompose applications into small, independent services
- Each service owns its 数据 和 logic
- Communicate via APIs (REST, gRPC, messaging)
- Deploy independently
- **Benefits**: Scalability, fault isolation, 技术 diversity
- **Challenges**: Distributed complexity, 数据 consistency, monitoring

#### Event-Driven 架构
- Components communicate through 事件
- Producers emit 事件, consumers react
- **Patterns**: Event sourcing, CQRS, pub/sub
- **Technologies**: Kafka, SNS/SQS, EventBridge, Pub/Sub
- **Benefits**: Loose coupling, scalability, real-time processing

#### Serverless 架构
- No server 管理 required
- Pay per execution
- Automatic scaling
- **Components**: Functions, API Gateway, managed services
- **Benefits**: Cost efficiency, reduced operations, rapid 部署
- **Considerations**: Cold starts, vendor lock-在, execution limits

#### Layered 架构 (N-Tier)
- Presentation layer (UI)
- Application/商业 logic layer
- 数据 access layer
- 数据库 layer
- **Benefits**: Separation 的 concerns, maintainability
- **Common**: 3-tier 网络 applications

#### Space-Based 架构
- Handle high concurrency 与 distributed 数据
- Virtualized memory across servers
- Processing nodes scale independently
- **Use Cases**: High-volume, low-latency applications

## Compute Services

### Virtual Machines
- **Types**: General purpose, compute optimized, memory optimized, GPU
- **Pricing**: On-demand, reserved instances, spot instances
- **管理**: Auto-scaling groups, load balancers
- **最佳实践**: Right-sizing, tagging, monitoring, patching

### Containers
- **Docker**: Container runtime standard
- **Orchestration**: Kubernetes (EKS, AKS, GKE), ECS, Fargate
- **Benefits**: Portability, efficiency, consistency
- **Registry**: ECR, GCR, ACR, Docker Hub

### Serverless Functions
- **Execution Model**: Event-triggered, stateless
- **Limits**: Execution time, memory, concurrent executions
- **Use Cases**: APIs, file processing, scheduled jobs, IoT backends
- **Monitoring**: Invocation counts, errors, duration, cold starts

## Storage Solutions

### Object Storage
- **Characteristics**: Flat structure, metadata, HTTP access
- **示例**: AWS S3, Google Cloud Storage, Azure Blob
- **Use Cases**: Static assets, backups, 数据 lakes, archives
- **Storage Classes**: Hot, cool, cold, archive (varying cost/access)

### Block Storage
- **Characteristics**: Raw volumes, attached to VMs
- **示例**: AWS EBS, Google Persistent Disk, Azure Disks
- **Use Cases**: Databases, boot volumes, high-性能 needs
- **Types**: SSD, HDD, provisioned IOPS

### File Storage
- **Characteristics**: Shared file 系统, NFS/SMB protocols
- **示例**: AWS EFS, Google Filestore, Azure Files
- **Use Cases**: Content 管理, shared configs, lift-和-shift

### Archive Storage
- **Characteristics**: Lowest cost, retrieval delays
- **示例**: S3 Glacier, Azure Archive Storage
- **Use Cases**: Compliance, long-term backups, historical 数据

## 数据库 Services

### Managed Relational Databases
- **Services**: AWS RDS/Aurora, Google Cloud SQL, Azure SQL 数据库
- **Features**: Automated backups, patching, scaling, replication
- **Engines**: MySQL, PostgreSQL, MariaDB, Oracle, SQL Server

### NoSQL Databases
- **Document**: DocumentDB, Firestore, Cosmos DB
- **Key-Value**: DynamoDB, Redis Cache
- **Wide-Column**: Bigtable, Cassandra (managed)
- **Graph**: Neptune, Cosmos DB (graph API)

### 数据 Warehousing
- **Services**: Snowflake, Redshift, BigQuery, Synapse
- **Characteristics**: Columnar storage, MPP 架构
- **Use Cases**: Analytics, BI, large-scale 数据 analysis

### Caching Services
- **在-Memory**: ElastiCache (Redis/Memcached), Cloud Memorystore
- **CDN Caching**: CloudFront, Cloud CDN, Azure CDN
- **Use Cases**: Session storage, query caching, content delivery

## Networking

### Virtual Networks
- **VPC/VNet**: Isolated 网络 environments
- **Subnets**: Public (internet-facing), private (internal only)
- **IP Addressing**: CIDR blocks, IPv4/IPv6
- **Route Tables**: Control traffic flow

### Load Balancing
- **Types**: Application (L7), 网络 (L4), Gateway
- **Features**: Health checks, SSL termination, sticky sessions
- **Services**: ELB/ALB/NLB, Cloud Load Balancing, Azure Load Balancer

### Content Delivery Networks (CDN)
- **Purpose**: Cache content at edge locations
- **Benefits**: Reduced latency, lower origin load, global distribution
- **Services**: CloudFront, Cloud CDN, Azure CDN, Akamai

### DNS Services
- **Functions**: Domain registration, routing, health checks
- **Services**: Route 53, Cloud DNS, Azure DNS
- **Routing Policies**: Simple, weighted, latency-based, geolocation, failover

### Connectivity Options
- **Internet Gateway**: Public internet access
- **NAT Gateway**: Private subnet outbound access
- **VPN**: Encrypted tunnels to on-premises
- **Direct Connect/ExpressRoute**: Dedicated private connections
- **VPC Peering**: Connect VPCs within/between accounts

## 安全 在 这 Cloud

### Shared Responsibility Model
- **Provider Responsibility**: 安全 的 这 cloud (infrastructure)
- **Customer Responsibility**: 安全 在 这 cloud (数据, applications, access)
- **Varies By Service**: More managed = more provider responsibility

### Identity 和 Access 管理 (IAM)
- **Users**: Individual identities
- **Groups**: Collections 的 users
- **Roles**: Temporary credentials 为 services/users
- **Policies**: JSON documents defining permissions
- **Principles**: Least privilege, separation 的 duties

### 网络 安全
- **安全 Groups**: Stateful firewalls 为 instances
- **网络 ACLs**: Stateless firewalls 为 subnets
- **网络 Application Firewall (WAF)**: Protect against 网络 exploits
- **DDoS Protection**: Shield, Cloud Armor, DDoS Protection

### 数据 Protection
- **Encryption at Rest**: KMS, customer-managed keys
- **Encryption 在 Transit**: TLS/SSL, HTTPS
- **Key 管理**: HSM, key rotation, audit trails
- **Secrets 管理**: Secrets Manager, Key Vault

### Compliance 和 Governance
- **Certifications**: SOC 2, ISO 27001, HIPAA, PCI-DSS, GDPR
- **Tools**: Policy enforcement, compliance reporting, audit logs
- **Frameworks**: Cloud 安全 Alliance, NIST CSF

## DevOps 在 这 Cloud

### CI/CD Services
- **AWS**: CodePipeline, CodeBuild, CodeDeploy
- **Azure**: Azure DevOps, GitHub Actions
- **GCP**: Cloud Build, Cloud Deploy
- **Third-party**: Jenkins, CircleCI, GitLab CI

### Infrastructure as Code (IaC)
- **Terraform**: Multi-cloud, declarative, state 管理
- **CloudFormation**: AWS native, YAML/JSON templates
- **ARM Templates**: Azure native
- **部署 Manager**: GCP native
- **Pulumi**: Infrastructure using programming languages
- **Benefits**: Version control, repeatability, documentation

### Configuration 管理
- **Ansible**: Agentless, YAML playbooks
- **Chef**: Ruby-based, mature ecosystem
- **Puppet**: Declarative, strong reporting
- **SaltStack**: Fast, Python-based

### Monitoring 和 Observability
- **Metrics**: CloudWatch, Cloud Monitoring, Azure Monitor
- **Logging**: CloudWatch Logs, Cloud Logging, Log Analytics
- **Tracing**: X-Ray, Cloud Trace, Application Insights
- **Dashboards**: CloudWatch Dashboards, Cloud Console
- **Alerting**: SNS, Cloud Monitoring alerts, Action Groups

### Container Orchestration
- **Kubernetes**: Industry standard orchestration
- **Managed Services**: EKS, AKS, GKE
- **Service Mesh**: Istio, Linkerd (traffic 管理, 安全)
- **GitOps**: ArgoCD, Flux (declarative deployments)

## Cost 管理

### Pricing Models
- **Pay-as-you-go**: Pay 为 what you use
- **Reserved Instances**: 1-3 year commitments, significant discounts
- **Spot Instances**: Bid 为 unused capacity, can be interrupted
- **Savings Plans**: Flexible commitment pricing
- **Free Tier**: Limited free usage 为 new accounts

### Cost Optimization Strategies
- **Right-sizing**: Match instance types to workload needs
- **Auto-scaling**: Scale based on demand
- **Reserved Capacity**: Commit to steady-state workloads
- **Spot Usage**: Use 为 fault-tolerant, flexible workloads
- **Storage Tiers**: Move infrequent 数据 to cheaper tiers
- **Cleanup**: Delete unused resources, snapshots, AMIs

### Cost 管理 Tools
- **AWS**: Cost Explorer, Budgets, Trusted Advisor
- **Azure**: Cost 管理, Advisor
- **GCP**: Billing reports, Recommender
- **Third-party**: CloudHealth, CloudCheckr, Datadog

## High Availability 和 Disaster Recovery

### Availability Concepts
- **Availability Zones**: Physically separate 数据 centers within region
- **Regions**: Geographic areas 与 multiple AZs
- **Edge Locations**: CDN cache locations globally

### HA Strategies
- **Multi-AZ**: Deploy across availability zones
- **Auto-healing**: Auto-replace failed instances
- **Load Balancing**: Distribute traffic across healthy instances
- **数据库 Replication**: Multi-AZ deployments, read replicas

### Disaster Recovery Strategies
- **Backup 和 Restore**: Periodic backups, restore when needed (lowest cost)
- **Pilot Light**: Core elements running, scale up during disaster
- **Warm Standby**: Scaled-down version always running
- **Multi-Site Active/Active**: Full production 在 multiple regions (highest cost)

### RTO 和 RPO
- **Recovery Time Objective (RTO)**: Maximum acceptable downtime
- **Recovery Point Objective (RPO)**: Maximum acceptable 数据 loss
- **Strategy Selection**: Based on 商业 requirements 和 budget

## Emerging Trends

### Edge 计算
- Process 数据 closer to source
- **Services**: AWS Outposts, Wavelength, Azure Edge, Cloud CDN
- **Use Cases**: IoT, real-time analytics, low-latency applications

### Multi-Cloud 和 Hybrid Cloud
- Avoid vendor lock-在
- Leverage best-的-breed services
- **Tools**: Terraform, Anthos, Arc, CloudHealth

### AI/ML Services
- Pre-trained models: Vision, speech, 语言
- Custom model training: SageMaker, Vertex AI, Azure ML
- MLOps: Model 部署, monitoring, governance

### Quantum 计算
- **Services**: AWS Braket, Azure Quantum
- **Status**: Early stage, experimental
- **Potential**: Cryptography, optimization, drug discovery

### Sustainable Cloud
- Carbon footprint tracking
- Renewable energy commitments
- Efficient resource utilization
- Green 架构 patterns
