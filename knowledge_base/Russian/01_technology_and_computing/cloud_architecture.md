<!-- 
This file was automatically translated from English to Russian.
Source: cloud_architecture.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# Cloud Архитектура

## Cloud Вычисления Основы

### What is Cloud Вычисления?
On-demand delivery из Вычисления resources (servers, storage, databases, networking, software) over the internet с pay-as-you-go pricing.

### Essential Characteristics (NIST Definition)
- **On-Demand Self-Service**: Provision resources without human interaction
- **Broad Сеть Access**: Available over Сеть via standard mechanisms
- **Resource Pooling**: Multi-tenant model с dynamic assignment
- **Rapid Elasticity**: Scale outward и inward rapidly
- **Measured Service**: Resource usage monitored и billed

### Cloud Развертывание Models
- **Public Cloud**: Owned by providers, shared infrastructure (AWS, Azure, GCP)
- **Private Cloud**: Dedicated to single organization (on-premises or hosted)
- **Hybrid Cloud**: Combination из public и private clouds
- **Multi-Cloud**: Using multiple public cloud providers
- **Community Cloud**: Shared by organizations с common concerns

### Service Models

#### Infrastructure as a Service (IaaS)
- **Provides**: Virtual machines, storage, networks, operating Системы
- **Примеры**: AWS EC2, Google Compute Engine, Azure VMs
- **Use Cases**: Lift-и-shift migrations, Разработка environments, high-control needs

#### Platform as a Service (PaaS)
- **Provides**: Разработка platforms, databases, middleware
- **Примеры**: Heroku, Google App Engine, AWS Elastic Beanstalk
- **Use Cases**: Application Разработка, API Развертывание, microservices

#### Software as a Service (SaaS)
- **Provides**: Complete applications over internet
- **Примеры**: Salesforce, Google Workspace, Microsoft 365, Slack
- **Use Cases**: Email, CRM, collaboration, Бизнес applications

#### Function as a Service (FaaS) / Serverless
- **Provides**: Event-driven function execution
- **Примеры**: AWS Lambda, Azure Functions, Google Cloud Functions
- **Use Cases**: Event processing, APIs, scheduled tasks, real-time processing

## Major Cloud Providers

### Amazon Веб Services (AWS)
- **Market Share**: ~32% (largest provider)
- **Key Services**:
  - Compute: EC2, Lambda, ECS, EKS
  - Storage: S3, EBS, Glacier
  - База данных: RDS, DynamoDB, Aurora
  - Networking: VPC, Route 53, CloudFront
  - AI/ML: SageMaker, Rekognition, Comprehend

### Microsoft Azure
- **Market Share**: ~23%
- **Strengths**: Enterprise integration, hybrid cloud, Microsoft ecosystem
- **Key Services**:
  - Compute: Virtual Machines, Azure Functions, AKS
  - Storage: Blob Storage, Disk Storage
  - База данных: SQL База данных, Cosmos DB
  - Networking: Virtual Сеть, Traffic Manager
  - AI/ML: Azure ML, Cognitive Services

### Google Cloud Platform (GCP)
- **Market Share**: ~10%
- **Strengths**: Данные analytics, AI/ML, Kubernetes
- **Key Services**:
  - Compute: Compute Engine, Cloud Functions, GKE
  - Storage: Cloud Storage, Persistent Disk
  - База данных: Cloud SQL, Firestore, Bigtable
  - Analytics: BigQuery, Dataflow, Pub/Sub
  - AI/ML: Vertex AI, AutoML

### Other Providers
- **IBM Cloud**: Enterprise focus, Watson AI
- **Oracle Cloud**: База данных workloads, enterprise applications
- **Alibaba Cloud**: Dominant в Asia-Pacific
- **DigitalOcean**: Developer-friendly, simplified offerings

## Cloud Архитектура Patterns

### Well-Architected Framework Principles

#### Operational Excellence
- Automate operations
- Make frequent, reversible changes
- Refine procedures continuously
- Anticipate failure

#### Безопасность
- Implement strong identity foundation
- Enable traceability
- Apply Безопасность at all layers
- Automate Безопасность Лучшие практики
- Protect Данные в transit и at rest

#### Reliability
- Test recovery procedures
- Automatically recover from failure
- Scale horizontally для availability
- Stop guessing capacity
- Manage change в automation

#### Производительность Efficiency
- Democratize Продвинутый technologies
- Go global в minutes
- Use serverless architectures
- Experiment more often
- Consider mechanical sympathy

#### Cost Optimization
- Adopt consumption model
- Measure overall efficiency
- Stop spending money on undifferentiated work
- Analyze и attribute expenditure
- Use managed services

### Common Архитектура Patterns

#### Microservices Архитектура
- Decompose applications into small, independent services
- Each service owns its Данные и logic
- Communicate via APIs (REST, gRPC, messaging)
- Deploy independently
- **Benefits**: Scalability, fault isolation, Технология diversity
- **Challenges**: Distributed complexity, Данные consistency, monitoring

#### Event-Driven Архитектура
- Components communicate through События
- Producers emit События, consumers react
- **Patterns**: Event sourcing, CQRS, pub/sub
- **Technologies**: Kafka, SNS/SQS, EventBridge, Pub/Sub
- **Benefits**: Loose coupling, scalability, real-time processing

#### Serverless Архитектура
- No server Управление required
- Pay per execution
- Automatic scaling
- **Components**: Functions, API Gateway, managed services
- **Benefits**: Cost efficiency, reduced operations, rapid Развертывание
- **Considerations**: Cold starts, vendor lock-в, execution limits

#### Layered Архитектура (N-Tier)
- Presentation layer (UI)
- Application/Бизнес logic layer
- Данные access layer
- База данных layer
- **Benefits**: Separation из concerns, maintainability
- **Common**: 3-tier Веб applications

#### Space-Based Архитектура
- Handle high concurrency с distributed Данные
- Virtualized memory across servers
- Processing nodes scale independently
- **Use Cases**: High-volume, low-latency applications

## Compute Services

### Virtual Machines
- **Types**: General purpose, compute optimized, memory optimized, GPU
- **Pricing**: On-demand, reserved instances, spot instances
- **Управление**: Auto-scaling groups, load balancers
- **Лучшие практики**: Right-sizing, tagging, monitoring, patching

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
- **Примеры**: AWS S3, Google Cloud Storage, Azure Blob
- **Use Cases**: Static assets, backups, Данные lakes, archives
- **Storage Classes**: Hot, cool, cold, archive (varying cost/access)

### Block Storage
- **Characteristics**: Raw volumes, attached to VMs
- **Примеры**: AWS EBS, Google Persistent Disk, Azure Disks
- **Use Cases**: Databases, boot volumes, high-Производительность needs
- **Types**: SSD, HDD, provisioned IOPS

### File Storage
- **Characteristics**: Shared file Системы, NFS/SMB protocols
- **Примеры**: AWS EFS, Google Filestore, Azure Files
- **Use Cases**: Content Управление, shared configs, lift-и-shift

### Archive Storage
- **Characteristics**: Lowest cost, retrieval delays
- **Примеры**: S3 Glacier, Azure Archive Storage
- **Use Cases**: Compliance, long-term backups, historical Данные

## База данных Services

### Managed Relational Databases
- **Services**: AWS RDS/Aurora, Google Cloud SQL, Azure SQL База данных
- **Features**: Automated backups, patching, scaling, replication
- **Engines**: MySQL, PostgreSQL, MariaDB, Oracle, SQL Server

### NoSQL Databases
- **Document**: DocumentDB, Firestore, Cosmos DB
- **Key-Value**: DynamoDB, Redis Cache
- **Wide-Column**: Bigtable, Cassandra (managed)
- **Graph**: Neptune, Cosmos DB (graph API)

### Данные Warehousing
- **Services**: Snowflake, Redshift, BigQuery, Synapse
- **Characteristics**: Columnar storage, MPP Архитектура
- **Use Cases**: Analytics, BI, large-scale Данные analysis

### Caching Services
- **в-Memory**: ElastiCache (Redis/Memcached), Cloud Memorystore
- **CDN Caching**: CloudFront, Cloud CDN, Azure CDN
- **Use Cases**: Session storage, query caching, content delivery

## Networking

### Virtual Networks
- **VPC/VNet**: Isolated Сеть environments
- **Subnets**: Public (internet-facing), private (internal only)
- **IP Addressing**: CIDR blocks, IPv4/IPv6
- **Route Tables**: Control traffic flow

### Load Balancing
- **Types**: Application (L7), Сеть (L4), Gateway
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

## Безопасность в the Cloud

### Shared Responsibility Model
- **Provider Responsibility**: Безопасность из the cloud (infrastructure)
- **Customer Responsibility**: Безопасность в the cloud (Данные, applications, access)
- **Varies By Service**: More managed = more provider responsibility

### Identity и Access Управление (IAM)
- **Users**: Individual identities
- **Groups**: Collections из users
- **Roles**: Temporary credentials для services/users
- **Policies**: JSON documents defining permissions
- **Principles**: Least privilege, separation из duties

### Сеть Безопасность
- **Безопасность Groups**: Stateful firewalls для instances
- **Сеть ACLs**: Stateless firewalls для subnets
- **Веб Application Firewall (WAF)**: Protect against Веб exploits
- **DDoS Protection**: Shield, Cloud Armor, DDoS Protection

### Данные Protection
- **Encryption at Rest**: KMS, customer-managed keys
- **Encryption в Transit**: TLS/SSL, HTTPS
- **Key Управление**: HSM, key rotation, audit trails
- **Secrets Управление**: Secrets Manager, Key Vault

### Compliance и Governance
- **Certifications**: SOC 2, ISO 27001, HIPAA, PCI-DSS, GDPR
- **Tools**: Policy enforcement, compliance reporting, audit logs
- **Frameworks**: Cloud Безопасность Alliance, NIST CSF

## DevOps в the Cloud

### CI/CD Services
- **AWS**: CodePipeline, CodeBuild, CodeDeploy
- **Azure**: Azure DevOps, GitHub Actions
- **GCP**: Cloud Build, Cloud Deploy
- **Third-party**: Jenkins, CircleCI, GitLab CI

### Infrastructure as Code (IaC)
- **Terraform**: Multi-cloud, declarative, state Управление
- **CloudFormation**: AWS native, YAML/JSON templates
- **ARM Templates**: Azure native
- **Развертывание Manager**: GCP native
- **Pulumi**: Infrastructure using programming languages
- **Benefits**: Version control, repeatability, documentation

### Configuration Управление
- **Ansible**: Agentless, YAML playbooks
- **Chef**: Ruby-based, mature ecosystem
- **Puppet**: Declarative, strong reporting
- **SaltStack**: Fast, Python-based

### Monitoring и Observability
- **Metrics**: CloudWatch, Cloud Monitoring, Azure Monitor
- **Logging**: CloudWatch Logs, Cloud Logging, Log Analytics
- **Tracing**: X-Ray, Cloud Trace, Application Insights
- **Dashboards**: CloudWatch Dashboards, Cloud Console
- **Alerting**: SNS, Cloud Monitoring alerts, Action Groups

### Container Orchestration
- **Kubernetes**: Industry standard orchestration
- **Managed Services**: EKS, AKS, GKE
- **Service Mesh**: Istio, Linkerd (traffic Управление, Безопасность)
- **GitOps**: ArgoCD, Flux (declarative deployments)

## Cost Управление

### Pricing Models
- **Pay-as-you-go**: Pay для what you use
- **Reserved Instances**: 1-3 year commitments, significant discounts
- **Spot Instances**: Bid для unused capacity, can be interrupted
- **Savings Plans**: Flexible commitment pricing
- **Free Tier**: Limited free usage для new accounts

### Cost Optimization Strategies
- **Right-sizing**: Match instance types to workload needs
- **Auto-scaling**: Scale based on demand
- **Reserved Capacity**: Commit to steady-state workloads
- **Spot Usage**: Use для fault-tolerant, flexible workloads
- **Storage Tiers**: Move infrequent Данные to cheaper tiers
- **Cleanup**: Delete unused resources, snapshots, AMIs

### Cost Управление Tools
- **AWS**: Cost Explorer, Budgets, Trusted Advisor
- **Azure**: Cost Управление, Advisor
- **GCP**: Billing reports, Recommender
- **Third-party**: CloudHealth, CloudCheckr, Datadog

## High Availability и Disaster Recovery

### Availability Concepts
- **Availability Zones**: Physically separate Данные centers within region
- **Regions**: Geographic areas с multiple AZs
- **Edge Locations**: CDN cache locations globally

### HA Strategies
- **Multi-AZ**: Deploy across availability zones
- **Auto-healing**: Auto-replace failed instances
- **Load Balancing**: Distribute traffic across healthy instances
- **База данных Replication**: Multi-AZ deployments, read replicas

### Disaster Recovery Strategies
- **Backup и Restore**: Periodic backups, restore when needed (lowest cost)
- **Pilot Light**: Core elements running, scale up during disaster
- **Warm Standby**: Scaled-down version always running
- **Multi-Site Active/Active**: Full production в multiple regions (highest cost)

### RTO и RPO
- **Recovery Time Objective (RTO)**: Maximum acceptable downtime
- **Recovery Point Objective (RPO)**: Maximum acceptable Данные loss
- **Strategy Selection**: Based on Бизнес requirements и budget

## Emerging Trends

### Edge Вычисления
- Process Данные closer to source
- **Services**: AWS Outposts, Wavelength, Azure Edge, Cloud CDN
- **Use Cases**: IoT, real-time analytics, low-latency applications

### Multi-Cloud и Hybrid Cloud
- Avoid vendor lock-в
- Leverage best-из-breed services
- **Tools**: Terraform, Anthos, Arc, CloudHealth

### AI/ML Services
- Pre-trained models: Vision, speech, Язык
- Custom model training: SageMaker, Vertex AI, Azure ML
- MLOps: Model Развертывание, monitoring, governance

### Quantum Вычисления
- **Services**: AWS Braket, Azure Quantum
- **Status**: Early stage, experimental
- **Potential**: Cryptography, optimization, drug discovery

### Sustainable Cloud
- Carbon footprint tracking
- Renewable energy commitments
- Efficient resource utilization
- Green Архитектура patterns
