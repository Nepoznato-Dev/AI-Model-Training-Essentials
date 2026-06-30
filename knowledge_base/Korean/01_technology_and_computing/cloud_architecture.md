<!-- 
This file was automatically translated from English to Korean.
Source: 클라우드_architecture.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# Cloud 아키텍처

# # Cloud Comput 기초

# ## What is Cloud Comput?
On-dem delivery comput resources (servers, storage, 데이 터bases, 네트워크, stware) over ternet 함께 pay-as-you-go pric.

# ## Essential Characteristics (NIST Defition)
- **On-Dem Self-Service**: Provision resources 함께out human teraction
- **Broad 네트워크 Access**: Available over 네트워크 via stard mechanisms
- **Resource Pool**: Multi-tenant model 함께 dynamic assignment
- **Rapid Elasticity**: Scale outward ward rapidly
- **Measured Service**: Resource usage monitored billed

# ## Cloud 배포 Models
- **Public Cloud**: Owned by providers, shared frastructure (AWS, Azure, GCP)
- **Private Cloud**: Dedicated to sle organization (on-premises or hosted)
- **Hybrid Cloud**: Combation public private 클라우드s
- **Multi-Cloud**: Us multiple public 클라우드 providers
- **Community Cloud**: Shared by organizations 함께 common concerns

# ## Service Models

# ### Infrastructure as a Service (IaaS)
- **Provides**: Virtual mach, storage, 네트워크s, operat 시스템
- **예시**: AWS EC2, Google Compute Enge, Azure VMs
- **Use Cases**: Lift--shift migrations, 개발 환경s, high-control needs

# ### Platm as a Service (PaaS)
- **Provides**: 개발 platms, 데이 터bases, middleware
- **예시**: Heroku, Google App Enge, AWS Elastic Beanstalk
- **Use Cases**: Application 개발, API 배포, microservices

# ### Stware as a Service (SaaS)
- **Provides**: Complete applications over ternet
- **예시**: Salesce, Google Workspace, Microst 365, Slack
- **Use Cases**: Email, CRM, collaboration, buss applications

# ### Function as a Service (FaaS) / Serverless
- **Provides**: Event-driven function execution
- **예시**: AWS Lambda, Azure Functions, Google Cloud Functions
- **Use Cases**: Event process, APIs, scheduled tasks, real-time process

# # Major Cloud Providers

# ## Amazon 웹 Services (AWS)
- **Market Share**: ~32% (largest provider)
- **Key Services**:
 - Compute: EC2, Lambda, ECS, EKS
 - Storage: S3, EBS, Glacier
 - 데이 터base: RDS, DynamoDB, Aurora
 - 네트워크: VPC, Route 53, CloudFront
 - 인공 지능/기계 학습: SageMaker, Rekognition, Comprehend

# ## Microst Azure
- **Market Share**: ~23%
- **Strengths**: Enterprise tegration, hybrid 클라우드, Microst ecosystem
- **Key Services**:
 - Compute: Virtual Mach, Azure Functions, AKS
 - Storage: Blob Storage, Disk Storage
 - 데이 터base: SQL 데이 터base, Cosmos DB
 - 네트워크: Virtual 네트워크, Traffic Manager
 - 인공 지능/기계 학습: Azure 기계 학습, Cognitive Services

# ## Google Cloud Platm (GCP)
- **Market Share**: ~10%
- **Strengths**: 데이 터 analytics, 인공 지능/기계 학습, Kubernetes
- **Key Services**:
 - Compute: Compute Enge, Cloud Functions, GKE
 - Storage: Cloud Storage, Persistent Disk
 - 데이 터base: Cloud SQL, Firestore, Bigtable
 - 분석: BigQuery, 데이 터flow, Pub/Sub
 - 인공 지능/기계 학습: Vertex 인공 지능, Auto기계 학습

# ## Or Providers
- **IBM Cloud**: Enterprise focus, Watson 인공 지능
- **Oracle Cloud**: 데이 터base workloads, enterprise applications
- **Alibaba Cloud**: Domant Asia-Pacific
- **DigitalOcean**: Developer-friendly, simplified fers

# # Cloud 아키텍처 Patterns

# ## Well-Architected Framework Prciples

# ### Operational Excellence
- Automate operations
- Make frequent, reversible changes
- Refe procedures contuously
- Anticipate failure

# ### 보안
- Implement strong identity foundation
- Enable traceability
- Apply 보안 at all layers
- Automate 보안 모범 사례
- Protect 데이 터 transit at rest

# ### Reliability
- Test recovery procedures
- Automatically recover from failure
- Scale horizontally availability
- Stop guess capacity
- Manage change automation

# ### Permance Efficiency
- Democratize 고급 technologies
- Go global mutes
- Use serverless 아키텍처s
- Experiment more ten
- Consider mechanical sympathy

# ### Cost Optimization
- Adopt consumption model
- Measure overall efficiency
- Stop spend money on undifferentiated work
- Analyze attribute expenditure
- Use managed services

# ## Common 아키텍처 Patterns

# ### Microservices 아키텍처
- Decompose applications 로 small, dependent services
- Each service owns its 데이 터 logic
- Communicate via APIs (REST, gRPC, messag)
- Deploy dependently
- **Benefits**: Scalability, fault isolation, 기술 diversity
- **Challenges**: Distributed complexity, 데이 터 consistency, monitor

# ### Event-Driven 아키텍처
- Components communicate through 이 벤트
- Producers emit 이 벤트, consumers react
- **Patterns**: Event sourc, CQRS, pub/sub
- **Technologies**: Kafka, SNS/SQS, EventBridge, Pub/Sub
- **Benefits**: Loose coupl, scalability, real-time process

# ### Serverless 아키텍처
- No server 관리 required
- Pay per execution
- Automatic scal
- **Components**: Functions, API Gateway, managed services
- **Benefits**: Cost efficiency, reduced operations, rapid 배포
- **Considerations**: Cold st예술, vendor lock-, execution limits

# ### Layered 아키텍처 (N-Tier)
- Presentation layer (UI)
- Application/Buss logic layer
- 데이 터 access layer
- 데이 터base layer
- **Benefits**: Separation concerns, mataability
- **Common**: 3-tier 웹 applications

# ### Space-Based 아키텍처
- Hle high concurrency 함께 distributed 데이 터
- Virtualized memory across servers
- Process nodes scale dependently
- **Use Cases**: High-volume, low-latency applications

# # Compute Services

# ## Virtual Mach
- **Types**: General purpose, compute optimized, memory optimized, GPU
- **Pric**: On-dem, reserved stances, spot stances
- **관리**: Auto-scal groups, load balancers
- **모범 사례**: Right-siz, tagg, monitor, patch

# ## Contaers
- **Docker**: Contaer runtime stard
- **Orchestration**: Kubernetes (EKS, AKS, GKE), ECS, Fargate
- **Benefits**: Portability, efficiency, consistency
- **Registry**: ECR, GCR, ACR, Docker Hub

# ## Serverless Functions
- **Execution Model**: Event-triggered, stateless
- **Limits**: Execution time, memory, concurrent executions
- **Use Cases**: APIs, file process, scheduled jobs, IoT backends
- **Monitor**: Invocation counts, errors, duration, cold st예술

# # Storage Solutions

# ## Object Storage
- **Characteristics**: Flat structure, 메타데이 터, HTTP access
- **예시**: AWS S3, Google Cloud Storage, Azure Blob
- **Use Cases**: Static assets, backups, 데이 터 lakes, archives
- **Storage Classes**: Hot, cool, cold, archive (vary cost/access)

# ## Block Storage
- **Characteristics**: Raw volumes, attached to VMs
- **예시**: AWS EBS, Google Persistent Disk, Azure Disks
- **Use Cases**: 데이 터bases, boot volumes, high-permance needs
- **Types**: SSD, HDD, provisioned IOPS

# ## File Storage
- **Characteristics**: Shared file 시스템, NFS/SMB protocols
- **예시**: AWS EFS, Google 파일tore, Azure 파일
- **Use Cases**: Content 관리, shared configs, lift--shift

# ## Archive Storage
- **Characteristics**: Lowest cost, retrieval delays
- **예시**: S3 Glacier, Azure Archive Storage
- **Use Cases**: Compliance, long-term backups, historical 데이 터

# # 데이 터base Services

# ## Managed Relational 데이 터bases
- **Services**: AWS RDS/Aurora, Google Cloud SQL, Azure SQL 데이 터base
- **Features**: Automated backups, patch, scal, replication
- **Eng**: MySQL, PostgreSQL, MariaDB, Oracle, SQL Server

# ## NoSQL 데이 터bases
- **Document**: DocumentDB, Firestore, Cosmos DB
- **Key-Value**: DynamoDB, Redis Cache
- **Wide-Column**: Bigtable, Cassra (managed)
- **Graph**: Neptune, Cosmos DB (graph API)

# ## 데이 터 Warehous
- **Services**: Snowflake, Redshift, BigQuery, Synapse
- **Characteristics**: Columnar storage, MPP 아키텍처
- **Use Cases**: 분석, BI, large-scale 데이 터 analysis

# ## Cach Services
- **In-Memory**: ElastiCache (Redis/Memcached), Cloud Memorystore
- **CDN Cach**: CloudFront, Cloud CDN, Azure CDN
- **Use Cases**: Session storage, query cach, 콘텐츠 delivery

# # 네트워크

# ## Virtual 네트워크s
- **VPC/VNet**: Isolated 네트워크 환경s
- **Subnets**: Public (ternet-fac), private (ternal only)
- **IP Address**: CIDR blocks, IPv4/IPv6
- **Route Tables**: Control traffic flow

# ## Load Balanc
- **Types**: Application (L7), 네트워크 (L4), Gateway
- **Features**: Health checks, SSL termation, sticky sessions
- **Services**: ELB/ALB/NLB, Cloud Load Balanc, Azure Load Balancer

# ## Content Delivery 네트워크s (CDN)
- **Purpose**: Cache 콘텐츠 at edge locations
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
- **VPC Peer**: Connect VPCs 함께/between accounts

# # 보안 Cloud

# ## Shared Responsibility Model
- **Provider Responsibility**: 보안 클라우드 (frastructure)
- **Customer Responsibility**: 보안 클라우드 (데이 터, applications, access)
- **Varies By Service**: More managed = more provider responsibility

# ## Identity Access 관리 (IAM)
- **Users**: Individual identities
- **Groups**: Collections users
- **Roles**: Temporary credentials services/users
- **Policies**: JSON documents def permissions
- **Prciples**: Least privilege, separation duties

# ## 네트워크 보안
- **보안 Groups**: Stateful firewalls stances
- **네트워크 ACLs**: Stateless firewalls subnets
- **웹 Application Firewall (WAF)**: Protect 대조 웹 exploits
- **DDoS Protection**: Shield, Cloud Armor, DDoS Protection

# ## 데이 터 Protection
- **Encryption at Rest**: KMS, customer-managed keys
- **Encryption Transit**: TLS/SSL, HTTPS
- **Key 관리**: HSM, key rotation, audit trails
- **Secrets 관리**: Secrets Manager, Key Vault

# ## Compliance Governance
- **Certifications**: SOC 2, ISO 27001, HIPAA, PCI-DSS, GDPR
- **Tools**: Policy encement, compliance report, audit logs
- **Frameworks**: Cloud 보안 Alliance, NIST CSF

# # DevOps Cloud

# ## CI/CD Services
- **AWS**: CodePipele, CodeBuild, CodeDeploy
- **Azure**: Azure DevOps, GitHub Actions
- **GCP**: Cloud Build, Cloud Deploy
- **Third-party**: Jenks, CircleCI, GitLab CI

# ## Infrastructure as Code (IaC)
- **Terram**: Multi-클라우드, declarative, state 관리
- **CloudFormation**: AWS native, YA기계 학습/JSON templates
- **ARM Templates**: Azure native
- **배포 Manager**: GCP native
- **Pulumi**: Infrastructure us programm 언어s
- **Benefits**: Version control, repeatability, documentation

# ## Configuration 관리
- **Ansible**: Agentless, YA기계 학습 playbooks
- **Chef**: Ruby-based, mature ecosystem
- **Puppet**: Declarative, strong report
- **SaltStack**: Fast, Python-based

# ## Monitor Observability
- **Metrics**: CloudWatch, Cloud Monitor, Azure Monitor
- **Logg**: CloudWatch Logs, Cloud Logg, Log 분석
- **Trac**: X-Ray, Cloud Trace, Application Insights
- **Dashboards**: CloudWatch Dashboards, Cloud Console
- **Alert**: SNS, Cloud Monitor alerts, Action Groups

# ## Contaer Orchestration
- **Kubernetes**: Industry stard orchestration
- **Managed Services**: EKS, AKS, GKE
- **Service Mesh**: Istio, Lkerd (traffic 관리, 보안)
- **GitOps**: ArgoCD, Flux (declarative 배포s)

# # Cost 관리

# ## Pric Models
- **Pay-as-you-go**: Pay what you use
- **Reserved Instances**: 1-3 year commitments, significant discounts
- **Spot Instances**: Bid unused capacity, can be terrupted
- **Savs Plans**: Flexible commitment pric
- **Free Tier**: Limited free usage new accounts

# ## Cost Optimization Strategies
- **Right-siz**: Match stance types to workload needs
- **Auto-scal**: Scale based on dem
- **Reserved Capacity**: Commit to steady-state workloads
- **Spot Usage**: Use fault-tolerant, flexible workloads
- **Storage Tiers**: Move frequent 데이 터 to cheaper tiers
- **Cleanup**: Delete unused resources, snapshots, AMIs

# ## Cost 관리 Tools
- **AWS**: Cost 탐색r, Budgets, Trusted Advisor
- **Azure**: Cost 관리, Advisor
- **GCP**: Bill reports, Recommender
- **Third-party**: CloudHealth, CloudCheckr, 데이 터dog

# # High Availability Disaster Recovery

# ## Availability Concepts
- **Availability Zones**: Physically separate 데이 터 centers 함께 region
- **Regions**: Geographic areas 함께 multiple AZs
- **Edge Locations**: CDN cache locations globally

# ## HA Strategies
- **Multi-AZ**: Deploy across availability zones
- **Auto-heal**: Auto-replace failed stances
- **Load Balanc**: Distribute traffic across healthy stances
- **데이 터base Replication**: Multi-AZ 배포s, read replicas

# ## Disaster Recovery Strategies
- **Backup Restore**: Periodic backups, restore when needed (lowest cost)
- **Pilot Light**: Core elements runn, scale up dur disaster
- **Warm Stby**: Scaled-down version always runn
- **Multi-Site Active/Active**: Full production multiple regions (highest cost)

# ## RTO RPO
- **Recovery Time Objective (RTO)**: Maximum acceptable downtime
- **Recovery Pot Objective (RPO)**: Maximum acceptable 데이 터 loss
- **Strategy Selection**: Based on buss requirements budget

# # Emerg Trends

# ## Edge Comput
- Process 데이 터 closer to source
- **Services**: AWS Outposts, Wavelength, Azure Edge, Cloud CDN
- **Use Cases**: IoT, real-time analytics, low-latency applications

# ## Multi-Cloud Hybrid Cloud
- Avoid vendor lock-
- Leverage best--breed services
- **Tools**: Terram, Anthos, Arc, CloudHealth

# ## 인공 지능/기계 학습 Services
- Pre-traed models: Vision, speech, 언어
- Custom model tra: SageMaker, Vertex 인공 지능, Azure 기계 학습
- 기계 학습Ops: Model 배포, monitor, governance

# ## Quantum Comput
- **Services**: AWS Braket, Azure Quantum
- **Status**: Early stage, experimental
- **Potential**: Cryptography, optimization, drug discovery

# ## Sustaable Cloud
- Carbon footprt track
- Renewable energy commitments
- Efficient resource utilization
- Green 아키텍처 patterns
