<!-- 
This file was automatically translated from English to Korean.
Source: cloud_architecture.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# Cloud 아키텍처

# # Cloud Comput에서g 기초

# ## What is Cloud Comput에서g?
On-dem와 delivery 의 comput에서g resources (servers, storage, 데이터bases, 네트워크에서g, s의tware) over 그 에서ternet 와 함께 pay-as-you-go pric에서g.

# ## Essential Characteristics (NIST Def에서ition)
- **On-Dem와 Self-Service**: Provision resources 와 함께out human 에서teraction
- **Broad 네트워크 Access**: Available over 네트워크 via st와ard mechanisms
- **Resource Pool에서g**: Multi-tenant model 와 함께 dynamic assignment
- **Rapid Elasticity**: Scale outward 와 에서ward rapidly
- **Measured Service**: Resource usage monitored 와 billed

# ## Cloud 배포 Models
- **Public Cloud**: Owned by providers, shared 에서frastructure (AWS, Azure, GCP)
- **Private Cloud**: Dedicated to s에서gle organization (on-premises or hosted)
- **Hybrid Cloud**: Comb에서ation 의 public 와 private clouds
- **Multi-Cloud**: Us에서g multiple public cloud providers
- **Community Cloud**: Shared by organizations 와 함께 common concerns

# ## Service Models

# ### Infrastructure as a Service (IaaS)
- **Provides**: Virtual mach에서es, storage, 네트워크s, operat에서g 시스템
- **예시**: AWS EC2, Google Compute Eng에서e, Azure VMs
- **Use Cases**: Lift-와-shift migrations, 개발 environments, high-control needs

# ### Plat위한m as a Service (PaaS)
- **Provides**: 개발 plat위한ms, 데이터bases, middleware
- **예시**: Heroku, Google App Eng에서e, AWS Elastic Beanstalk
- **Use Cases**: Application 개발, API 배포, microservices

# ### S의tware as a Service (SaaS)
- **Provides**: Complete applications over 에서ternet
- **예시**: Sales위한ce, Google Workspace, Micros의t 365, Slack
- **Use Cases**: Email, CRM, collaboration, bus에서ess applications

# ### Function as a Service (FaaS) / Serverless
- **Provides**: Event-driven function execution
- **예시**: AWS Lambda, Azure Functions, Google Cloud Functions
- **Use Cases**: Event process에서g, APIs, scheduled tasks, real-time process에서g

# # Major Cloud Providers

# ## Amazon 웹 Services (AWS)
- **Market Share**: ~32% (largest provider)
- **Key Services**:
  - Compute: EC2, Lambda, ECS, EKS
  - Storage: S3, EBS, Glacier
  - 데이터base: RDS, DynamoDB, Aurora
  - 네트워크에서g: VPC, Route 53, CloudFront
  - AI/ML: SageMaker, Rekognition, Comprehend

# ## Micros의t Azure
- **Market Share**: ~23%
- **Strengths**: Enterprise 에서tegration, hybrid cloud, Micros의t ecosystem
- **Key Services**:
  - Compute: Virtual Mach에서es, Azure Functions, AKS
  - Storage: Blob Storage, Disk Storage
  - 데이터base: SQL 데이터base, Cosmos DB
  - 네트워크에서g: Virtual 네트워크, Traffic Manager
  - AI/ML: Azure ML, Cognitive Services

# ## Google Cloud Plat위한m (GCP)
- **Market Share**: ~10%
- **Strengths**: 데이터 analytics, AI/ML, Kubernetes
- **Key Services**:
  - Compute: Compute Eng에서e, Cloud Functions, GKE
  - Storage: Cloud Storage, Persistent Disk
  - 데이터base: Cloud SQL, Firestore, Bigtable
  - Analytics: BigQuery, 데이터flow, Pub/Sub
  - AI/ML: Vertex AI, AutoML

# ## O그r Providers
- **IBM Cloud**: Enterprise focus, Watson AI
- **Oracle Cloud**: 데이터base workloads, enterprise applications
- **Alibaba Cloud**: Dom에서ant 에서 Asia-Pacific
- **DigitalOcean**: Developer-friendly, simplified 의fer에서gs

# # Cloud 아키텍처 Patterns

# ## Well-Architected Framework Pr에서ciples

# ### Operational Excellence
- Automate operations
- Make frequent, reversible changes
- Ref에서e procedures cont에서uously
- Anticipate failure

# ### 보안
- Implement strong identity foundation
- Enable traceability
- Apply 보안 at all layers
- Automate 보안 모범 사례
- Protect 데이터 에서 transit 와 at rest

# ### Reliability
- Test recovery procedures
- Automatically recover from failure
- Scale horizontally 위한 availability
- Stop guess에서g capacity
- Manage change 에서 automation

# ### Per위한mance Efficiency
- Democratize 고급 technologies
- Go global 에서 m에서utes
- Use serverless 아키텍처s
- Experiment more 의ten
- Consider mechanical sympathy

# ### Cost Optimization
- Adopt consumption model
- Measure overall efficiency
- Stop spend에서g money on undifferentiated work
- Analyze 와 attribute expenditure
- Use managed services

# ## Common 아키텍처 Patterns

# ### Microservices 아키텍처
- Decompose applications 에서to small, 에서dependent services
- Each service owns its 데이터 와 logic
- Communicate via APIs (REST, gRPC, messag에서g)
- Deploy 에서dependently
- **Benefits**: Scalability, fault isolation, 기술 diversity
- **Challenges**: Distributed complexity, 데이터 consistency, monitor에서g

# ### Event-Driven 아키텍처
- Components communicate through 이벤트
- Producers emit 이벤트, consumers react
- **Patterns**: Event sourc에서g, CQRS, pub/sub
- **Technologies**: Kafka, SNS/SQS, EventBridge, Pub/Sub
- **Benefits**: Loose coupl에서g, scalability, real-time process에서g

# ### Serverless 아키텍처
- No server 관리 required
- Pay per execution
- Automatic scal에서g
- **Components**: Functions, API Gateway, managed services
- **Benefits**: Cost efficiency, reduced operations, rapid 배포
- **Considerations**: Cold st예술, vendor lock-에서, execution limits

# ### Layered 아키텍처 (N-Tier)
- Presentation layer (UI)
- Application/Bus에서ess logic layer
- 데이터 access layer
- 데이터base layer
- **Benefits**: Separation 의 concerns, ma에서ta에서ability
- **Common**: 3-tier 웹 applications

# ### Space-Based 아키텍처
- H와le high concurrency 와 함께 distributed 데이터
- Virtualized memory across servers
- Process에서g nodes scale 에서dependently
- **Use Cases**: High-volume, low-latency applications

# # Compute Services

# ## Virtual Mach에서es
- **Types**: General purpose, compute optimized, memory optimized, GPU
- **Pric에서g**: On-dem와, reserved 에서stances, spot 에서stances
- **관리**: Auto-scal에서g groups, load balancers
- **모범 사례**: Right-siz에서g, tagg에서g, monitor에서g, patch에서g

# ## Conta에서ers
- **Docker**: Conta에서er runtime st와ard
- **Orchestration**: Kubernetes (EKS, AKS, GKE), ECS, Fargate
- **Benefits**: Portability, efficiency, consistency
- **Registry**: ECR, GCR, ACR, Docker Hub

# ## Serverless Functions
- **Execution Model**: Event-triggered, stateless
- **Limits**: Execution time, memory, concurrent executions
- **Use Cases**: APIs, file process에서g, scheduled jobs, IoT backends
- **Monitor에서g**: Invocation counts, errors, duration, cold st예술

# # Storage Solutions

# ## Object Storage
- **Characteristics**: Flat structure, meta데이터, HTTP access
- **예시**: AWS S3, Google Cloud Storage, Azure Blob
- **Use Cases**: Static assets, backups, 데이터 lakes, archives
- **Storage Classes**: Hot, cool, cold, archive (vary에서g cost/access)

# ## Block Storage
- **Characteristics**: Raw volumes, attached to VMs
- **예시**: AWS EBS, Google Persistent Disk, Azure Disks
- **Use Cases**: 데이터bases, boot volumes, high-per위한mance needs
- **Types**: SSD, HDD, provisioned IOPS

# ## File Storage
- **Characteristics**: Shared file 시스템, NFS/SMB protocols
- **예시**: AWS EFS, Google Filestore, Azure Files
- **Use Cases**: Content 관리, shared configs, lift-와-shift

# ## Archive Storage
- **Characteristics**: Lowest cost, retrieval delays
- **예시**: S3 Glacier, Azure Archive Storage
- **Use Cases**: Compliance, long-term backups, historical 데이터

# # 데이터base Services

# ## Managed Relational 데이터bases
- **Services**: AWS RDS/Aurora, Google Cloud SQL, Azure SQL 데이터base
- **Features**: Automated backups, patch에서g, scal에서g, replication
- **Eng에서es**: MySQL, PostgreSQL, MariaDB, Oracle, SQL Server

# ## NoSQL 데이터bases
- **Document**: DocumentDB, Firestore, Cosmos DB
- **Key-Value**: DynamoDB, Redis Cache
- **Wide-Column**: Bigtable, Cass와ra (managed)
- **Graph**: Neptune, Cosmos DB (graph API)

# ## 데이터 Warehous에서g
- **Services**: Snowflake, Redshift, BigQuery, Synapse
- **Characteristics**: Columnar storage, MPP 아키텍처
- **Use Cases**: Analytics, BI, large-scale 데이터 analysis

# ## Cach에서g Services
- **In-Memory**: ElastiCache (Redis/Memcached), Cloud Memorystore
- **CDN Cach에서g**: CloudFront, Cloud CDN, Azure CDN
- **Use Cases**: Session storage, query cach에서g, content delivery

# # 네트워크에서g

# ## Virtual 네트워크s
- **VPC/VNet**: Isolated 네트워크 environments
- **Subnets**: Public (에서ternet-fac에서g), private (에서ternal only)
- **IP Address에서g**: CIDR blocks, IPv4/IPv6
- **Route Tables**: Control traffic flow

# ## Load Balanc에서g
- **Types**: Application (L7), 네트워크 (L4), Gateway
- **Features**: Health checks, SSL term에서ation, sticky sessions
- **Services**: ELB/ALB/NLB, Cloud Load Balanc에서g, Azure Load Balancer

# ## Content Delivery 네트워크s (CDN)
- **Purpose**: Cache content at edge locations
- **Benefits**: Reduced latency, lower orig에서 load, global distribution
- **Services**: CloudFront, Cloud CDN, Azure CDN, Akamai

# ## DNS Services
- **Functions**: Doma에서 registration, rout에서g, health checks
- **Services**: Route 53, Cloud DNS, Azure DNS
- **Rout에서g Policies**: Simple, weighted, latency-based, geolocation, failover

# ## Connectivity Options
- **Internet Gateway**: Public 에서ternet access
- **NAT Gateway**: Private subnet outbound access
- **VPN**: Encrypted tunnels to on-premises
- **Direct Connect/ExpressRoute**: Dedicated private connections
- **VPC Peer에서g**: Connect VPCs 와 함께에서/between accounts

# # 보안 에서 그 Cloud

# ## Shared Responsibility Model
- **Provider Responsibility**: 보안 의 그 cloud (에서frastructure)
- **Customer Responsibility**: 보안 에서 그 cloud (데이터, applications, access)
- **Varies By Service**: More managed = more provider responsibility

# ## Identity 와 Access 관리 (IAM)
- **Users**: Individual identities
- **Groups**: Collections 의 users
- **Roles**: Temporary credentials 위한 services/users
- **Policies**: JSON documents def에서에서g permissions
- **Pr에서ciples**: Least privilege, separation 의 duties

# ## 네트워크 보안
- **보안 Groups**: Stateful firewalls 위한 에서stances
- **네트워크 ACLs**: Stateless firewalls 위한 subnets
- **웹 Application Firewall (WAF)**: Protect aga에서st 웹 exploits
- **DDoS Protection**: Shield, Cloud Armor, DDoS Protection

# ## 데이터 Protection
- **Encryption at Rest**: KMS, customer-managed keys
- **Encryption 에서 Transit**: TLS/SSL, HTTPS
- **Key 관리**: HSM, key rotation, audit trails
- **Secrets 관리**: Secrets Manager, Key Vault

# ## Compliance 와 Governance
- **Certifications**: SOC 2, ISO 27001, HIPAA, PCI-DSS, GDPR
- **Tools**: Policy en위한cement, compliance report에서g, audit logs
- **Frameworks**: Cloud 보안 Alliance, NIST CSF

# # DevOps 에서 그 Cloud

# ## CI/CD Services
- **AWS**: CodePipel에서e, CodeBuild, CodeDeploy
- **Azure**: Azure DevOps, GitHub Actions
- **GCP**: Cloud Build, Cloud Deploy
- **Third-party**: Jenk에서s, CircleCI, GitLab CI

# ## Infrastructure as Code (IaC)
- **Terra위한m**: Multi-cloud, declarative, state 관리
- **CloudFormation**: AWS native, YAML/JSON templates
- **ARM Templates**: Azure native
- **배포 Manager**: GCP native
- **Pulumi**: Infrastructure us에서g programm에서g 언어s
- **Benefits**: Version control, repeatability, documentation

# ## Configuration 관리
- **Ansible**: Agentless, YAML playbooks
- **Chef**: Ruby-based, mature ecosystem
- **Puppet**: Declarative, strong report에서g
- **SaltStack**: Fast, Python-based

# ## Monitor에서g 와 Observability
- **Metrics**: CloudWatch, Cloud Monitor에서g, Azure Monitor
- **Logg에서g**: CloudWatch Logs, Cloud Logg에서g, Log Analytics
- **Trac에서g**: X-Ray, Cloud Trace, Application Insights
- **Dashboards**: CloudWatch Dashboards, Cloud Console
- **Alert에서g**: SNS, Cloud Monitor에서g alerts, Action Groups

# ## Conta에서er Orchestration
- **Kubernetes**: Industry st와ard orchestration
- **Managed Services**: EKS, AKS, GKE
- **Service Mesh**: Istio, L에서kerd (traffic 관리, 보안)
- **GitOps**: ArgoCD, Flux (declarative 배포s)

# # Cost 관리

# ## Pric에서g Models
- **Pay-as-you-go**: Pay 위한 what you use
- **Reserved Instances**: 1-3 year commitments, significant discounts
- **Spot Instances**: Bid 위한 unused capacity, can be 에서terrupted
- **Sav에서gs Plans**: Flexible commitment pric에서g
- **Free Tier**: Limited free usage 위한 new accounts

# ## Cost Optimization Strategies
- **Right-siz에서g**: Match 에서stance types to workload needs
- **Auto-scal에서g**: Scale based on dem와
- **Reserved Capacity**: Commit to steady-state workloads
- **Spot Usage**: Use 위한 fault-tolerant, flexible workloads
- **Storage Tiers**: Move 에서frequent 데이터 to cheaper tiers
- **Cleanup**: Delete unused resources, snapshots, AMIs

# ## Cost 관리 Tools
- **AWS**: Cost Explorer, Budgets, Trusted Advisor
- **Azure**: Cost 관리, Advisor
- **GCP**: Bill에서g reports, Recommender
- **Third-party**: CloudHealth, CloudCheckr, 데이터dog

# # High Availability 와 Disaster Recovery

# ## Availability Concepts
- **Availability Zones**: Physically separate 데이터 centers 와 함께에서 region
- **Regions**: Geographic areas 와 함께 multiple AZs
- **Edge Locations**: CDN cache locations globally

# ## HA Strategies
- **Multi-AZ**: Deploy across availability zones
- **Auto-heal에서g**: Auto-replace failed 에서stances
- **Load Balanc에서g**: Distribute traffic across healthy 에서stances
- **데이터base Replication**: Multi-AZ 배포s, read replicas

# ## Disaster Recovery Strategies
- **Backup 와 Restore**: Periodic backups, restore when needed (lowest cost)
- **Pilot Light**: Core elements runn에서g, scale up dur에서g disaster
- **Warm St와by**: Scaled-down version always runn에서g
- **Multi-Site Active/Active**: Full production 에서 multiple regions (highest cost)

# ## RTO 와 RPO
- **Recovery Time Objective (RTO)**: Maximum acceptable downtime
- **Recovery Po에서t Objective (RPO)**: Maximum acceptable 데이터 loss
- **Strategy Selection**: Based on bus에서ess requirements 와 budget

# # Emerg에서g Trends

# ## Edge Comput에서g
- Process 데이터 closer to source
- **Services**: AWS Outposts, Wavelength, Azure Edge, Cloud CDN
- **Use Cases**: IoT, real-time analytics, low-latency applications

# ## Multi-Cloud 와 Hybrid Cloud
- Avoid vendor lock-에서
- Leverage best-의-breed services
- **Tools**: Terra위한m, Anthos, Arc, CloudHealth

# ## AI/ML Services
- Pre-tra에서ed models: Vision, speech, 언어
- Custom model tra에서에서g: SageMaker, Vertex AI, Azure ML
- MLOps: Model 배포, monitor에서g, governance

# ## Quantum Comput에서g
- **Services**: AWS Braket, Azure Quantum
- **Status**: Early stage, experimental
- **Potential**: Cryptography, optimization, drug discovery

# ## Susta에서able Cloud
- Carbon footpr에서t track에서g
- Renewable energy commitments
- Efficient resource utilization
- Green 아키텍처 patterns
