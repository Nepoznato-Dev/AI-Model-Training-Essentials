<!-- 
This file was automatically translated from English to Korean.
Source: cloud_architecture.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# Cloud 아키텍처

## Cloud 컴퓨팅 기초

### What is Cloud 컴퓨팅?
On-demand delivery 의 컴퓨팅 resources (servers, storage, databases, networking, software) over 그 internet 와 함께 pay-as-you-go pricing.

### Essential Characteristics (NIST Definition)
- **On-Demand Self-Service**: Provision resources without human interaction
- **Broad 네트워크 Access**: Available over 네트워크 via standard mechanisms
- **Resource Pooling**: Multi-tenant model 와 함께 dynamic assignment
- **Rapid Elasticity**: Scale outward 와 inward rapidly
- **Measured Service**: Resource usage monitored 와 billed

### Cloud 배포 Models
- **Public Cloud**: Owned by providers, shared infrastructure (AWS, Azure, GCP)
- **Private Cloud**: Dedicated to single organization (on-premises or hosted)
- **Hybrid Cloud**: Combination 의 public 와 private clouds
- **Multi-Cloud**: Using multiple public cloud providers
- **Community Cloud**: Shared by organizations 와 함께 common concerns

### Service Models

#### Infrastructure as a Service (IaaS)
- **Provides**: Virtual machines, storage, networks, operating 시스템
- **예시**: AWS EC2, Google Compute Engine, Azure VMs
- **Use Cases**: Lift-와-shift migrations, 개발 environments, high-control needs

#### Platform as a Service (PaaS)
- **Provides**: 개발 platforms, databases, middleware
- **예시**: Heroku, Google App Engine, AWS Elastic Beanstalk
- **Use Cases**: Application 개발, API 배포, microservices

#### Software as a Service (SaaS)
- **Provides**: Complete applications over internet
- **예시**: Salesforce, Google Workspace, Microsoft 365, Slack
- **Use Cases**: Email, CRM, collaboration, 비즈니스 applications

#### Function as a Service (FaaS) / Serverless
- **Provides**: Event-driven function execution
- **예시**: AWS Lambda, Azure Functions, Google Cloud Functions
- **Use Cases**: Event processing, APIs, scheduled tasks, real-time processing

## Major Cloud Providers

### Amazon 웹 Services (AWS)
- **Market Share**: ~32% (largest provider)
- **Key Services**:
  - Compute: EC2, Lambda, ECS, EKS
  - Storage: S3, EBS, Glacier
  - 데이터베이스: RDS, DynamoDB, Aurora
  - Networking: VPC, Route 53, CloudFront
  - AI/ML: SageMaker, Rekognition, Comprehend

### Microsoft Azure
- **Market Share**: ~23%
- **Strengths**: Enterprise integration, hybrid cloud, Microsoft ecosystem
- **Key Services**:
  - Compute: Virtual Machines, Azure Functions, AKS
  - Storage: Blob Storage, Disk Storage
  - 데이터베이스: SQL 데이터베이스, Cosmos DB
  - Networking: Virtual 네트워크, Traffic Manager
  - AI/ML: Azure ML, Cognitive Services

### Google Cloud Platform (GCP)
- **Market Share**: ~10%
- **Strengths**: 데이터 analytics, AI/ML, Kubernetes
- **Key Services**:
  - Compute: Compute Engine, Cloud Functions, GKE
  - Storage: Cloud Storage, Persistent Disk
  - 데이터베이스: Cloud SQL, Firestore, Bigtable
  - Analytics: BigQuery, Dataflow, Pub/Sub
  - AI/ML: Vertex AI, AutoML

### Other Providers
- **IBM Cloud**: Enterprise focus, Watson AI
- **Oracle Cloud**: 데이터베이스 workloads, enterprise applications
- **Alibaba Cloud**: Dominant 에서 Asia-Pacific
- **DigitalOcean**: Developer-friendly, simplified offerings

## Cloud 아키텍처 Patterns

### Well-Architected Framework Principles

#### Operational Excellence
- Automate operations
- Make frequent, reversible changes
- Refine procedures continuously
- Anticipate failure

#### 보안
- Implement strong identity foundation
- Enable traceability
- Apply 보안 at all layers
- Automate 보안 모범 사례
- Protect 데이터 에서 transit 와 at rest

#### Reliability
- Test recovery procedures
- Automatically recover from failure
- Scale horizontally 위한 availability
- Stop guessing capacity
- Manage change 에서 automation

#### 성능 Efficiency
- Democratize 고급 technologies
- Go global 에서 minutes
- Use serverless architectures
- Experiment more often
- Consider mechanical sympathy

#### Cost Optimization
- Adopt consumption model
- Measure overall efficiency
- Stop spending money on undifferentiated work
- Analyze 와 attribute expenditure
- Use managed services

### Common 아키텍처 Patterns

#### Microservices 아키텍처
- Decompose applications into small, independent services
- Each service owns its 데이터 와 logic
- Communicate via APIs (REST, gRPC, messaging)
- Deploy independently
- **Benefits**: Scalability, fault isolation, 기술 diversity
- **Challenges**: Distributed complexity, 데이터 consistency, monitoring

#### Event-Driven 아키텍처
- Components communicate through 이벤트
- Producers emit 이벤트, consumers react
- **Patterns**: Event sourcing, CQRS, pub/sub
- **Technologies**: Kafka, SNS/SQS, EventBridge, Pub/Sub
- **Benefits**: Loose coupling, scalability, real-time processing

#### Serverless 아키텍처
- No server 관리 required
- Pay per execution
- Automatic scaling
- **Components**: Functions, API Gateway, managed services
- **Benefits**: Cost efficiency, reduced operations, rapid 배포
- **Considerations**: Cold starts, vendor lock-에서, execution limits

#### Layered 아키텍처 (N-Tier)
- Presentation layer (UI)
- Application/비즈니스 logic layer
- 데이터 access layer
- 데이터베이스 layer
- **Benefits**: Separation 의 concerns, maintainability
- **Common**: 3-tier 웹 applications

#### Space-Based 아키텍처
- Handle high concurrency 와 함께 distributed 데이터
- Virtualized memory across servers
- Processing nodes scale independently
- **Use Cases**: High-volume, low-latency applications

## Compute Services

### Virtual Machines
- **Types**: General purpose, compute optimized, memory optimized, GPU
- **Pricing**: On-demand, reserved instances, spot instances
- **관리**: Auto-scaling groups, load balancers
- **모범 사례**: Right-sizing, tagging, monitoring, patching

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
- **예시**: AWS S3, Google Cloud Storage, Azure Blob
- **Use Cases**: Static assets, backups, 데이터 lakes, archives
- **Storage Classes**: Hot, cool, cold, archive (varying cost/access)

### Block Storage
- **Characteristics**: Raw volumes, attached to VMs
- **예시**: AWS EBS, Google Persistent Disk, Azure Disks
- **Use Cases**: Databases, boot volumes, high-성능 needs
- **Types**: SSD, HDD, provisioned IOPS

### File Storage
- **Characteristics**: Shared file 시스템, NFS/SMB protocols
- **예시**: AWS EFS, Google Filestore, Azure Files
- **Use Cases**: Content 관리, shared configs, lift-와-shift

### Archive Storage
- **Characteristics**: Lowest cost, retrieval delays
- **예시**: S3 Glacier, Azure Archive Storage
- **Use Cases**: Compliance, long-term backups, historical 데이터

## 데이터베이스 Services

### Managed Relational Databases
- **Services**: AWS RDS/Aurora, Google Cloud SQL, Azure SQL 데이터베이스
- **Features**: Automated backups, patching, scaling, replication
- **Engines**: MySQL, PostgreSQL, MariaDB, Oracle, SQL Server

### NoSQL Databases
- **Document**: DocumentDB, Firestore, Cosmos DB
- **Key-Value**: DynamoDB, Redis Cache
- **Wide-Column**: Bigtable, Cassandra (managed)
- **Graph**: Neptune, Cosmos DB (graph API)

### 데이터 Warehousing
- **Services**: Snowflake, Redshift, BigQuery, Synapse
- **Characteristics**: Columnar storage, MPP 아키텍처
- **Use Cases**: Analytics, BI, large-scale 데이터 analysis

### Caching Services
- **에서-Memory**: ElastiCache (Redis/Memcached), Cloud Memorystore
- **CDN Caching**: CloudFront, Cloud CDN, Azure CDN
- **Use Cases**: Session storage, query caching, content delivery

## Networking

### Virtual Networks
- **VPC/VNet**: Isolated 네트워크 environments
- **Subnets**: Public (internet-facing), private (internal only)
- **IP Addressing**: CIDR blocks, IPv4/IPv6
- **Route Tables**: Control traffic flow

### Load Balancing
- **Types**: Application (L7), 네트워크 (L4), Gateway
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

## 보안 에서 그 Cloud

### Shared Responsibility Model
- **Provider Responsibility**: 보안 의 그 cloud (infrastructure)
- **Customer Responsibility**: 보안 에서 그 cloud (데이터, applications, access)
- **Varies By Service**: More managed = more provider responsibility

### Identity 와 Access 관리 (IAM)
- **Users**: Individual identities
- **Groups**: Collections 의 users
- **Roles**: Temporary credentials 위한 services/users
- **Policies**: JSON documents defining permissions
- **Principles**: Least privilege, separation 의 duties

### 네트워크 보안
- **보안 Groups**: Stateful firewalls 위한 instances
- **네트워크 ACLs**: Stateless firewalls 위한 subnets
- **웹 Application Firewall (WAF)**: Protect against 웹 exploits
- **DDoS Protection**: Shield, Cloud Armor, DDoS Protection

### 데이터 Protection
- **Encryption at Rest**: KMS, customer-managed keys
- **Encryption 에서 Transit**: TLS/SSL, HTTPS
- **Key 관리**: HSM, key rotation, audit trails
- **Secrets 관리**: Secrets Manager, Key Vault

### Compliance 와 Governance
- **Certifications**: SOC 2, ISO 27001, HIPAA, PCI-DSS, GDPR
- **Tools**: Policy enforcement, compliance reporting, audit logs
- **Frameworks**: Cloud 보안 Alliance, NIST CSF

## DevOps 에서 그 Cloud

### CI/CD Services
- **AWS**: CodePipeline, CodeBuild, CodeDeploy
- **Azure**: Azure DevOps, GitHub Actions
- **GCP**: Cloud Build, Cloud Deploy
- **Third-party**: Jenkins, CircleCI, GitLab CI

### Infrastructure as Code (IaC)
- **Terraform**: Multi-cloud, declarative, state 관리
- **CloudFormation**: AWS native, YAML/JSON templates
- **ARM Templates**: Azure native
- **배포 Manager**: GCP native
- **Pulumi**: Infrastructure using programming languages
- **Benefits**: Version control, repeatability, documentation

### Configuration 관리
- **Ansible**: Agentless, YAML playbooks
- **Chef**: Ruby-based, mature ecosystem
- **Puppet**: Declarative, strong reporting
- **SaltStack**: Fast, Python-based

### Monitoring 와 Observability
- **Metrics**: CloudWatch, Cloud Monitoring, Azure Monitor
- **Logging**: CloudWatch Logs, Cloud Logging, Log Analytics
- **Tracing**: X-Ray, Cloud Trace, Application Insights
- **Dashboards**: CloudWatch Dashboards, Cloud Console
- **Alerting**: SNS, Cloud Monitoring alerts, Action Groups

### Container Orchestration
- **Kubernetes**: Industry standard orchestration
- **Managed Services**: EKS, AKS, GKE
- **Service Mesh**: Istio, Linkerd (traffic 관리, 보안)
- **GitOps**: ArgoCD, Flux (declarative deployments)

## Cost 관리

### Pricing Models
- **Pay-as-you-go**: Pay 위한 what you use
- **Reserved Instances**: 1-3 year commitments, significant discounts
- **Spot Instances**: Bid 위한 unused capacity, can be interrupted
- **Savings Plans**: Flexible commitment pricing
- **Free Tier**: Limited free usage 위한 new accounts

### Cost Optimization Strategies
- **Right-sizing**: Match instance types to workload needs
- **Auto-scaling**: Scale based on demand
- **Reserved Capacity**: Commit to steady-state workloads
- **Spot Usage**: Use 위한 fault-tolerant, flexible workloads
- **Storage Tiers**: Move infrequent 데이터 to cheaper tiers
- **Cleanup**: Delete unused resources, snapshots, AMIs

### Cost 관리 Tools
- **AWS**: Cost Explorer, Budgets, Trusted Advisor
- **Azure**: Cost 관리, Advisor
- **GCP**: Billing reports, Recommender
- **Third-party**: CloudHealth, CloudCheckr, Datadog

## High Availability 와 Disaster Recovery

### Availability Concepts
- **Availability Zones**: Physically separate 데이터 centers within region
- **Regions**: Geographic areas 와 함께 multiple AZs
- **Edge Locations**: CDN cache locations globally

### HA Strategies
- **Multi-AZ**: Deploy across availability zones
- **Auto-healing**: Auto-replace failed instances
- **Load Balancing**: Distribute traffic across healthy instances
- **데이터베이스 Replication**: Multi-AZ deployments, read replicas

### Disaster Recovery Strategies
- **Backup 와 Restore**: Periodic backups, restore when needed (lowest cost)
- **Pilot Light**: Core elements running, scale up during disaster
- **Warm Standby**: Scaled-down version always running
- **Multi-Site Active/Active**: Full production 에서 multiple regions (highest cost)

### RTO 와 RPO
- **Recovery Time Objective (RTO)**: Maximum acceptable downtime
- **Recovery Point Objective (RPO)**: Maximum acceptable 데이터 loss
- **Strategy Selection**: Based on 비즈니스 requirements 와 budget

## Emerging Trends

### Edge 컴퓨팅
- Process 데이터 closer to source
- **Services**: AWS Outposts, Wavelength, Azure Edge, Cloud CDN
- **Use Cases**: IoT, real-time analytics, low-latency applications

### Multi-Cloud 와 Hybrid Cloud
- Avoid vendor lock-에서
- Leverage best-의-breed services
- **Tools**: Terraform, Anthos, Arc, CloudHealth

### AI/ML Services
- Pre-trained models: Vision, speech, 언어
- Custom model training: SageMaker, Vertex AI, Azure ML
- MLOps: Model 배포, monitoring, governance

### Quantum 컴퓨팅
- **Services**: AWS Braket, Azure Quantum
- **Status**: Early stage, experimental
- **Potential**: Cryptography, optimization, drug discovery

### Sustainable Cloud
- Carbon footprint tracking
- Renewable energy commitments
- Efficient resource utilization
- Green 아키텍처 patterns
