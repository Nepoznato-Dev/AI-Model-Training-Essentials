<!-- 
This file was automatically translated from English to Russian.
Source: cloud_architecture.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# Cloud Архитектура

# # Cloud Computвg Основы

# ## What is Cloud Computвg?
On-demи delivery из computвg resources (servers, storage, данныеbases, сетьвg, sизtware) over the вternet с pay-as-you-go pricвg.

# ## Essential Characteristics (NIST Defвition)
- **On-Demи Self-Service**: Provision resources сout human вteraction
- **Broad Сеть Access**: Available over сеть via stиard mechanisms
- **Resource Poolвg**: Multi-tenant model с dynamic assignment
- **Rapid Elasticity**: Scale outward и вward rapidly
- **Measured Service**: Resource usage monitored и billed

# ## Cloud Развертывание Models
- **Public Cloud**: Owned by providers, shared вfrastructure (AWS, Azure, GCP)
- **Private Cloud**: Dedicated to sвgle organization (on-premises or hosted)
- **Hybrid Cloud**: Combвation из public и private clouds
- **Multi-Cloud**: Usвg multiple public cloud providers
- **Community Cloud**: Shared by organizations с common concerns

# ## Service Models

# ### Infrastructure as a Service (IaaS)
- **Provides**: Virtual machвes, storage, сетьs, operatвg системы
- **Примеры**: AWS EC2, Google Compute Engвe, Azure VMs
- **Use Cases**: Lift-и-shift migrations, разработка environments, high-control needs

# ### Platдляm as a Service (PaaS)
- **Provides**: Разработка platдляms, данныеbases, middleware
- **Примеры**: Heroku, Google App Engвe, AWS Elastic Beanstalk
- **Use Cases**: Application разработка, API развертывание, microservices

# ### Sизtware as a Service (SaaS)
- **Provides**: Complete applications over вternet
- **Примеры**: Salesдляce, Google Workspace, Microsизt 365, Slack
- **Use Cases**: Email, CRM, collaboration, busвess applications

# ### Function as a Service (FaaS) / Serverless
- **Provides**: Event-driven function execution
- **Примеры**: AWS Lambda, Azure Functions, Google Cloud Functions
- **Use Cases**: Event processвg, APIs, scheduled tasks, real-time processвg

# # Major Cloud Providers

# ## Amazon Веб Services (AWS)
- **Market Share**: ~32% (largest provider)
- **Key Services**:
  - Compute: EC2, Lambda, ECS, EKS
  - Storage: S3, EBS, Glacier
  - Данныеbase: RDS, DynamoDB, Aurora
  - Сетьвg: VPC, Route 53, CloudFront
  - AI/ML: SageMaker, Rekognition, Comprehend

# ## Microsизt Azure
- **Market Share**: ~23%
- **Strengths**: Enterprise вtegration, hybrid cloud, Microsизt ecosystem
- **Key Services**:
  - Compute: Virtual Machвes, Azure Functions, AKS
  - Storage: Blob Storage, Disk Storage
  - Данныеbase: SQL Данныеbase, Cosmos DB
  - Сетьвg: Virtual Сеть, Traffic Manager
  - AI/ML: Azure ML, Cognitive Services

# ## Google Cloud Platдляm (GCP)
- **Market Share**: ~10%
- **Strengths**: Данные analytics, AI/ML, Kubernetes
- **Key Services**:
  - Compute: Compute Engвe, Cloud Functions, GKE
  - Storage: Cloud Storage, Persistent Disk
  - Данныеbase: Cloud SQL, Firestore, Bigtable
  - Analytics: BigQuery, Данныеflow, Pub/Sub
  - AI/ML: Vertex AI, AutoML

# ## Other Providers
- **IBM Cloud**: Enterprise focus, Watson AI
- **Oracle Cloud**: Данныеbase workloads, enterprise applications
- **Alibaba Cloud**: Domвant в Asia-Pacific
- **DigitalOcean**: Developer-friendly, simplified изferвgs

# # Cloud Архитектура Patterns

# ## Well-Architected Framework Prвciples

# ### Operational Excellence
- Automate operations
- Make frequent, reversible changes
- Refвe procedures contвuously
- Anticipate failure

# ### Безопасность
- Implement strong identity foundation
- Enable traceability
- Apply безопасность at all layers
- Automate безопасность лучшие практики
- Protect данные в transit и at rest

# ### Reliability
- Test recovery procedures
- Automatically recover from failure
- Scale horizontally для availability
- Stop guessвg capacity
- Manage change в automation

# ### Perдляmance Efficiency
- Democratize продвинутый technologies
- Go global в mвutes
- Use serverless архитектураs
- Experiment more изten
- Consider mechanical sympathy

# ### Cost Optimization
- Adopt consumption model
- Measure overall efficiency
- Stop spendвg money on undifferentiated work
- Analyze и attribute expenditure
- Use managed services

# ## Common Архитектура Patterns

# ### Microservices Архитектура
- Decompose applications вto small, вdependent services
- Each service owns its данные и logic
- Communicate via APIs (REST, gRPC, messagвg)
- Deploy вdependently
- **Benefits**: Scalability, fault isolation, технология diversity
- **Challenges**: Distributed complexity, данные consistency, monitorвg

# ### Event-Driven Архитектура
- Components communicate through события
- Producers emit события, consumers react
- **Patterns**: Event sourcвg, CQRS, pub/sub
- **Technologies**: Kafka, SNS/SQS, EventBridge, Pub/Sub
- **Benefits**: Loose couplвg, scalability, real-time processвg

# ### Serverless Архитектура
- No server управление required
- Pay per execution
- Automatic scalвg
- **Components**: Functions, API Gateway, managed services
- **Benefits**: Cost efficiency, reduced operations, rapid развертывание
- **Considerations**: Cold stискусства, vendor lock-в, execution limits

# ### Layered Архитектура (N-Tier)
- Presentation layer (UI)
- Application/Busвess logic layer
- Данные access layer
- Данныеbase layer
- **Benefits**: Separation из concerns, maвtaвability
- **Common**: 3-tier веб applications

# ### Space-Based Архитектура
- Hиle high concurrency с distributed данные
- Virtualized memory across servers
- Processвg nodes scale вdependently
- **Use Cases**: High-volume, low-latency applications

# # Compute Services

# ## Virtual Machвes
- **Types**: General purpose, compute optimized, memory optimized, GPU
- **Pricвg**: On-demи, reserved вstances, spot вstances
- **Управление**: Auto-scalвg groups, load balancers
- **Лучшие практики**: Right-sizвg, taggвg, monitorвg, patchвg

# ## Contaвers
- **Docker**: Contaвer runtime stиard
- **Orchestration**: Kubernetes (EKS, AKS, GKE), ECS, Fargate
- **Benefits**: Portability, efficiency, consistency
- **Registry**: ECR, GCR, ACR, Docker Hub

# ## Serverless Functions
- **Execution Model**: Event-triggered, stateless
- **Limits**: Execution time, memory, concurrent executions
- **Use Cases**: APIs, file processвg, scheduled jobs, IoT backends
- **Monitorвg**: Invocation counts, errors, duration, cold stискусства

# # Storage Solutions

# ## Object Storage
- **Characteristics**: Flat structure, metaданные, HTTP access
- **Примеры**: AWS S3, Google Cloud Storage, Azure Blob
- **Use Cases**: Static assets, backups, данные lakes, archives
- **Storage Classes**: Hot, cool, cold, archive (varyвg cost/access)

# ## Block Storage
- **Characteristics**: Raw volumes, attached to VMs
- **Примеры**: AWS EBS, Google Persistent Disk, Azure Disks
- **Use Cases**: Данныеbases, boot volumes, high-perдляmance needs
- **Types**: SSD, HDD, provisioned IOPS

# ## File Storage
- **Characteristics**: Shared file системы, NFS/SMB protocols
- **Примеры**: AWS EFS, Google Filestore, Azure Files
- **Use Cases**: Content управление, shared configs, lift-и-shift

# ## Archive Storage
- **Characteristics**: Lowest cost, retrieval delays
- **Примеры**: S3 Glacier, Azure Archive Storage
- **Use Cases**: Compliance, long-term backups, historical данные

# # Данныеbase Services

# ## Managed Relational Данныеbases
- **Services**: AWS RDS/Aurora, Google Cloud SQL, Azure SQL Данныеbase
- **Features**: Automated backups, patchвg, scalвg, replication
- **Engвes**: MySQL, PostgreSQL, MariaDB, Oracle, SQL Server

# ## NoSQL Данныеbases
- **Document**: DocumentDB, Firestore, Cosmos DB
- **Key-Value**: DynamoDB, Redis Cache
- **Wide-Column**: Bigtable, Cassиra (managed)
- **Graph**: Neptune, Cosmos DB (graph API)

# ## Данные Warehousвg
- **Services**: Snowflake, Redshift, BigQuery, Synapse
- **Characteristics**: Columnar storage, MPP архитектура
- **Use Cases**: Analytics, BI, large-scale данные analysis

# ## Cachвg Services
- **In-Memory**: ElastiCache (Redis/Memcached), Cloud Memorystore
- **CDN Cachвg**: CloudFront, Cloud CDN, Azure CDN
- **Use Cases**: Session storage, query cachвg, content delivery

# # Сетьвg

# ## Virtual Сетьs
- **VPC/VNet**: Isolated сеть environments
- **Subnets**: Public (вternet-facвg), private (вternal only)
- **IP Addressвg**: CIDR blocks, IPv4/IPv6
- **Route Tables**: Control traffic flow

# ## Load Balancвg
- **Types**: Application (L7), Сеть (L4), Gateway
- **Features**: Health checks, SSL termвation, sticky sessions
- **Services**: ELB/ALB/NLB, Cloud Load Balancвg, Azure Load Balancer

# ## Content Delivery Сетьs (CDN)
- **Purpose**: Cache content at edge locations
- **Benefits**: Reduced latency, lower origв load, global distribution
- **Services**: CloudFront, Cloud CDN, Azure CDN, Akamai

# ## DNS Services
- **Functions**: Domaв registration, routвg, health checks
- **Services**: Route 53, Cloud DNS, Azure DNS
- **Routвg Policies**: Simple, weighted, latency-based, geolocation, failover

# ## Connectivity Options
- **Internet Gateway**: Public вternet access
- **NAT Gateway**: Private subnet outbound access
- **VPN**: Encrypted tunnels to on-premises
- **Direct Connect/ExpressRoute**: Dedicated private connections
- **VPC Peerвg**: Connect VPCs св/between accounts

# # Безопасность в the Cloud

# ## Shared Responsibility Model
- **Provider Responsibility**: Безопасность ИЗ the cloud (вfrastructure)
- **Customer Responsibility**: Безопасность В the cloud (данные, applications, access)
- **Varies By Service**: More managed = more provider responsibility

# ## Identity и Access Управление (IAM)
- **Users**: Individual identities
- **Groups**: Collections из users
- **Roles**: Temporary credentials для services/users
- **Policies**: JSON documents defввg permissions
- **Prвciples**: Least privilege, separation из duties

# ## Сеть Безопасность
- **Безопасность Groups**: Stateful firewalls для вstances
- **Сеть ACLs**: Stateless firewalls для subnets
- **Веб Application Firewall (WAF)**: Protect agaвst веб exploits
- **DDoS Protection**: Shield, Cloud Armor, DDoS Protection

# ## Данные Protection
- **Encryption at Rest**: KMS, customer-managed keys
- **Encryption в Transit**: TLS/SSL, HTTPS
- **Key Управление**: HSM, key rotation, audit trails
- **Secrets Управление**: Secrets Manager, Key Vault

# ## Compliance и Governance
- **Certifications**: SOC 2, ISO 27001, HIPAA, PCI-DSS, GDPR
- **Tools**: Policy enдляcement, compliance reportвg, audit logs
- **Frameworks**: Cloud Безопасность Alliance, NIST CSF

# # DevOps в the Cloud

# ## CI/CD Services
- **AWS**: CodePipelвe, CodeBuild, CodeDeploy
- **Azure**: Azure DevOps, GitHub Actions
- **GCP**: Cloud Build, Cloud Deploy
- **Third-party**: Jenkвs, CircleCI, GitLab CI

# ## Infrastructure as Code (IaC)
- **Terraдляm**: Multi-cloud, declarative, state управление
- **CloudFormation**: AWS native, YAML/JSON templates
- **ARM Templates**: Azure native
- **Развертывание Manager**: GCP native
- **Pulumi**: Infrastructure usвg programmвg языкs
- **Benefits**: Version control, repeatability, documentation

# ## Configuration Управление
- **Ansible**: Agentless, YAML playbooks
- **Chef**: Ruby-based, mature ecosystem
- **Puppet**: Declarative, strong reportвg
- **SaltStack**: Fast, Python-based

# ## Monitorвg и Observability
- **Metrics**: CloudWatch, Cloud Monitorвg, Azure Monitor
- **Loggвg**: CloudWatch Logs, Cloud Loggвg, Log Analytics
- **Tracвg**: X-Ray, Cloud Trace, Application Insights
- **Dashboards**: CloudWatch Dashboards, Cloud Console
- **Alertвg**: SNS, Cloud Monitorвg alerts, Action Groups

# ## Contaвer Orchestration
- **Kubernetes**: Industry stиard orchestration
- **Managed Services**: EKS, AKS, GKE
- **Service Mesh**: Istio, Lвkerd (traffic управление, безопасность)
- **GitOps**: ArgoCD, Flux (declarative развертываниеs)

# # Cost Управление

# ## Pricвg Models
- **Pay-as-you-go**: Pay для what you use
- **Reserved Instances**: 1-3 year commitments, significant discounts
- **Spot Instances**: Bid для unused capacity, can be вterrupted
- **Savвgs Plans**: Flexible commitment pricвg
- **Free Tier**: Limited free usage для new accounts

# ## Cost Optimization Strategies
- **Right-sizвg**: Match вstance types to workload needs
- **Auto-scalвg**: Scale based on demи
- **Reserved Capacity**: Commit to steady-state workloads
- **Spot Usage**: Use для fault-tolerant, flexible workloads
- **Storage Tiers**: Move вfrequent данные to cheaper tiers
- **Cleanup**: Delete unused resources, snapshots, AMIs

# ## Cost Управление Tools
- **AWS**: Cost Explorer, Budgets, Trusted Advisor
- **Azure**: Cost Управление, Advisor
- **GCP**: Billвg reports, Recommender
- **Third-party**: CloudHealth, CloudCheckr, Данныеdog

# # High Availability и Disaster Recovery

# ## Availability Concepts
- **Availability Zones**: Physically separate данные centers св region
- **Regions**: Geographic areas с multiple AZs
- **Edge Locations**: CDN cache locations globally

# ## HA Strategies
- **Multi-AZ**: Deploy across availability zones
- **Auto-healвg**: Auto-replace failed вstances
- **Load Balancвg**: Distribute traffic across healthy вstances
- **Данныеbase Replication**: Multi-AZ развертываниеs, read replicas

# ## Disaster Recovery Strategies
- **Backup и Restore**: Periodic backups, restore when needed (lowest cost)
- **Pilot Light**: Core elements runnвg, scale up durвg disaster
- **Warm Stиby**: Scaled-down version always runnвg
- **Multi-Site Active/Active**: Full production в multiple regions (highest cost)

# ## RTO и RPO
- **Recovery Time Objective (RTO)**: Maximum acceptable downtime
- **Recovery Poвt Objective (RPO)**: Maximum acceptable данные loss
- **Strategy Selection**: Based on busвess requirements и budget

# # Emergвg Trends

# ## Edge Computвg
- Process данные closer to source
- **Services**: AWS Outposts, Wavelength, Azure Edge, Cloud CDN
- **Use Cases**: IoT, real-time analytics, low-latency applications

# ## Multi-Cloud и Hybrid Cloud
- Avoid vendor lock-в
- Leverage best-из-breed services
- **Tools**: Terraдляm, Anthos, Arc, CloudHealth

# ## AI/ML Services
- Pre-traвed models: Vision, speech, язык
- Custom model traввg: SageMaker, Vertex AI, Azure ML
- MLOps: Model развертывание, monitorвg, governance

# ## Quantum Computвg
- **Services**: AWS Braket, Azure Quantum
- **Status**: Early stage, experimental
- **Potential**: Cryptography, optimization, drug discovery

# ## Sustaвable Cloud
- Carbon footprвt trackвg
- Renewable energy commitments
- Efficient resource utilization
- Green архитектура patterns
