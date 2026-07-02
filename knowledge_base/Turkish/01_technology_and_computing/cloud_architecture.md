<!-- 
This file was automatically translated from English to Turkish.
Source: cloud_architecture.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# Cloud Mimari

## Cloud Bilişim Temeller

### What is Cloud Bilişim?
On-demand delivery içinde Bilişim resources (servers, storage, databases, networking, software) over bu internet ile pay-as-you-go pricing.

### Essential Characteristics (NIST Definition)
- **On-Demand Self-Service**: Provision resources without human interaction
- **Broad Ağ Access**: Available over Ağ via standard mechanisms
- **Resource Pooling**: Multi-tenant model ile dynamic assignment
- **Rapid Elasticity**: Scale outward ve inward rapidly
- **Measured Service**: Resource usage monitored ve billed

### Cloud Dağıtım Models
- **Public Cloud**: Owned by providers, shared infrastructure (AWS, Azure, GCP)
- **Private Cloud**: Dedicated to single organization (on-premises or hosted)
- **Hybrid Cloud**: Combination içinde public ve private clouds
- **Multi-Cloud**: Using multiple public cloud providers
- **Community Cloud**: Shared by organizations ile common concerns

### Service Models

#### Infrastructure as a Service (IaaS)
- **Provides**: Virtual machines, storage, networks, operating Sistemler
- **Örnekler**: AWS EC2, Google Compute Engine, Azure VMs
- **Use Cases**: Lift-ve-shift migrations, Geliştirme environments, high-control needs

#### Platform as a Service (PaaS)
- **Provides**: Geliştirme platforms, databases, middleware
- **Örnekler**: Heroku, Google App Engine, AWS Elastic Beanstalk
- **Use Cases**: Application Geliştirme, API Dağıtım, microservices

#### Software as a Service (SaaS)
- **Provides**: Complete applications over internet
- **Örnekler**: Salesforce, Google Workspace, Microsoft 365, Slack
- **Use Cases**: Email, CRM, collaboration, İş applications

#### Function as a Service (FaaS) / Serverless
- **Provides**: Event-driven function execution
- **Örnekler**: AWS Lambda, Azure Functions, Google Cloud Functions
- **Use Cases**: Event processing, APIs, scheduled tasks, real-time processing

## Major Cloud Providers

### Amazon Web Services (AWS)
- **Market Share**: ~32% (largest provider)
- **Key Services**:
  - Compute: EC2, Lambda, ECS, EKS
  - Storage: S3, EBS, Glacier
  - Veritabanı: RDS, DynamoDB, Aurora
  - Networking: VPC, Route 53, CloudFront
  - AI/ML: SageMaker, Rekognition, Comprehend

### Microsoft Azure
- **Market Share**: ~23%
- **Strengths**: Enterprise integration, hybrid cloud, Microsoft ecosystem
- **Key Services**:
  - Compute: Virtual Machines, Azure Functions, AKS
  - Storage: Blob Storage, Disk Storage
  - Veritabanı: SQL Veritabanı, Cosmos DB
  - Networking: Virtual Ağ, Traffic Manager
  - AI/ML: Azure ML, Cognitive Services

### Google Cloud Platform (GCP)
- **Market Share**: ~10%
- **Strengths**: Veri analytics, AI/ML, Kubernetes
- **Key Services**:
  - Compute: Compute Engine, Cloud Functions, GKE
  - Storage: Cloud Storage, Persistent Disk
  - Veritabanı: Cloud SQL, Firestore, Bigtable
  - Analytics: BigQuery, Dataflow, Pub/Sub
  - AI/ML: Vertex AI, AutoML

### Other Providers
- **IBM Cloud**: Enterprise focus, Watson AI
- **Oracle Cloud**: Veritabanı workloads, enterprise applications
- **Alibaba Cloud**: Dominant içinde Asia-Pacific
- **DigitalOcean**: Developer-friendly, simplified offerings

## Cloud Mimari Patterns

### Well-Architected Framework Principles

#### Operational Excellence
- Automate operations
- Make frequent, reversible changes
- Refine procedures continuously
- Anticipate failure

#### Güvenlik
- Implement strong identity foundation
- Enable traceability
- Apply Güvenlik at all layers
- Automate Güvenlik En İyi Uygulamalar
- Protect Veri içinde transit ve at rest

#### Reliability
- Test recovery procedures
- Automatically recover from failure
- Scale horizontally için availability
- Stop guessing capacity
- Manage change içinde automation

#### Performans Efficiency
- Democratize İleri Düzey technologies
- Go global içinde minutes
- Use serverless architectures
- Experiment more often
- Consider mechanical sympathy

#### Cost Optimization
- Adopt consumption model
- Measure overall efficiency
- Stop spending money on undifferentiated work
- Analyze ve attribute expenditure
- Use managed services

### Common Mimari Patterns

#### Microservices Mimari
- Decompose applications into small, independent services
- Each service owns its Veri ve logic
- Communicate via APIs (REST, gRPC, messaging)
- Deploy independently
- **Benefits**: Scalability, fault isolation, Teknoloji diversity
- **Challenges**: Distributed complexity, Veri consistency, monitoring

#### Event-Driven Mimari
- Components communicate through Olaylar
- Producers emit Olaylar, consumers react
- **Patterns**: Event sourcing, CQRS, pub/sub
- **Technologies**: Kafka, SNS/SQS, EventBridge, Pub/Sub
- **Benefits**: Loose coupling, scalability, real-time processing

#### Serverless Mimari
- No server Yönetim required
- Pay per execution
- Automatic scaling
- **Components**: Functions, API Gateway, managed services
- **Benefits**: Cost efficiency, reduced operations, rapid Dağıtım
- **Considerations**: Cold starts, vendor lock-içinde, execution limits

#### Layered Mimari (N-Tier)
- Presentation layer (UI)
- Application/İş logic layer
- Veri access layer
- Veritabanı layer
- **Benefits**: Separation içinde concerns, maintainability
- **Common**: 3-tier Web applications

#### Space-Based Mimari
- Handle high concurrency ile distributed Veri
- Virtualized memory across servers
- Processing nodes scale independently
- **Use Cases**: High-volume, low-latency applications

## Compute Services

### Virtual Machines
- **Types**: General purpose, compute optimized, memory optimized, GPU
- **Pricing**: On-demand, reserved instances, spot instances
- **Yönetim**: Auto-scaling groups, load balancers
- **En İyi Uygulamalar**: Right-sizing, tagging, monitoring, patching

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
- **Örnekler**: AWS S3, Google Cloud Storage, Azure Blob
- **Use Cases**: Static assets, backups, Veri lakes, archives
- **Storage Classes**: Hot, cool, cold, archive (varying cost/access)

### Block Storage
- **Characteristics**: Raw volumes, attached to VMs
- **Örnekler**: AWS EBS, Google Persistent Disk, Azure Disks
- **Use Cases**: Databases, boot volumes, high-Performans needs
- **Types**: SSD, HDD, provisioned IOPS

### File Storage
- **Characteristics**: Shared file Sistemler, NFS/SMB protocols
- **Örnekler**: AWS EFS, Google Filestore, Azure Files
- **Use Cases**: Content Yönetim, shared configs, lift-ve-shift

### Archive Storage
- **Characteristics**: Lowest cost, retrieval delays
- **Örnekler**: S3 Glacier, Azure Archive Storage
- **Use Cases**: Compliance, long-term backups, historical Veri

## Veritabanı Services

### Managed Relational Databases
- **Services**: AWS RDS/Aurora, Google Cloud SQL, Azure SQL Veritabanı
- **Features**: Automated backups, patching, scaling, replication
- **Engines**: MySQL, PostgreSQL, MariaDB, Oracle, SQL Server

### NoSQL Databases
- **Document**: DocumentDB, Firestore, Cosmos DB
- **Key-Value**: DynamoDB, Redis Cache
- **Wide-Column**: Bigtable, Cassandra (managed)
- **Graph**: Neptune, Cosmos DB (graph API)

### Veri Warehousing
- **Services**: Snowflake, Redshift, BigQuery, Synapse
- **Characteristics**: Columnar storage, MPP Mimari
- **Use Cases**: Analytics, BI, large-scale Veri analysis

### Caching Services
- **içinde-Memory**: ElastiCache (Redis/Memcached), Cloud Memorystore
- **CDN Caching**: CloudFront, Cloud CDN, Azure CDN
- **Use Cases**: Session storage, query caching, content delivery

## Networking

### Virtual Networks
- **VPC/VNet**: Isolated Ağ environments
- **Subnets**: Public (internet-facing), private (internal only)
- **IP Addressing**: CIDR blocks, IPv4/IPv6
- **Route Tables**: Control traffic flow

### Load Balancing
- **Types**: Application (L7), Ağ (L4), Gateway
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

## Güvenlik içinde bu Cloud

### Shared Responsibility Model
- **Provider Responsibility**: Güvenlik içinde bu cloud (infrastructure)
- **Customer Responsibility**: Güvenlik içinde bu cloud (Veri, applications, access)
- **Varies By Service**: More managed = more provider responsibility

### Identity ve Access Yönetim (IAM)
- **Users**: Individual identities
- **Groups**: Collections içinde users
- **Roles**: Temporary credentials için services/users
- **Policies**: JSON documents defining permissions
- **Principles**: Least privilege, separation içinde duties

### Ağ Güvenlik
- **Güvenlik Groups**: Stateful firewalls için instances
- **Ağ ACLs**: Stateless firewalls için subnets
- **Web Application Firewall (WAF)**: Protect against Web exploits
- **DDoS Protection**: Shield, Cloud Armor, DDoS Protection

### Veri Protection
- **Encryption at Rest**: KMS, customer-managed keys
- **Encryption içinde Transit**: TLS/SSL, HTTPS
- **Key Yönetim**: HSM, key rotation, audit trails
- **Secrets Yönetim**: Secrets Manager, Key Vault

### Compliance ve Governance
- **Certifications**: SOC 2, ISO 27001, HIPAA, PCI-DSS, GDPR
- **Tools**: Policy enforcement, compliance reporting, audit logs
- **Frameworks**: Cloud Güvenlik Alliance, NIST CSF

## DevOps içinde bu Cloud

### CI/CD Services
- **AWS**: CodePipeline, CodeBuild, CodeDeploy
- **Azure**: Azure DevOps, GitHub Actions
- **GCP**: Cloud Build, Cloud Deploy
- **Third-party**: Jenkins, CircleCI, GitLab CI

### Infrastructure as Code (IaC)
- **Terraform**: Multi-cloud, declarative, state Yönetim
- **CloudFormation**: AWS native, YAML/JSON templates
- **ARM Templates**: Azure native
- **Dağıtım Manager**: GCP native
- **Pulumi**: Infrastructure using programming languages
- **Benefits**: Version control, repeatability, documentation

### Configuration Yönetim
- **Ansible**: Agentless, YAML playbooks
- **Chef**: Ruby-based, mature ecosystem
- **Puppet**: Declarative, strong reporting
- **SaltStack**: Fast, Python-based

### Monitoring ve Observability
- **Metrics**: CloudWatch, Cloud Monitoring, Azure Monitor
- **Logging**: CloudWatch Logs, Cloud Logging, Log Analytics
- **Tracing**: X-Ray, Cloud Trace, Application Insights
- **Dashboards**: CloudWatch Dashboards, Cloud Console
- **Alerting**: SNS, Cloud Monitoring alerts, Action Groups

### Container Orchestration
- **Kubernetes**: Industry standard orchestration
- **Managed Services**: EKS, AKS, GKE
- **Service Mesh**: Istio, Linkerd (traffic Yönetim, Güvenlik)
- **GitOps**: ArgoCD, Flux (declarative deployments)

## Cost Yönetim

### Pricing Models
- **Pay-as-you-go**: Pay için what you use
- **Reserved Instances**: 1-3 year commitments, significant discounts
- **Spot Instances**: Bid için unused capacity, can be interrupted
- **Savings Plans**: Flexible commitment pricing
- **Free Tier**: Limited free usage için new accounts

### Cost Optimization Strategies
- **Right-sizing**: Match instance types to workload needs
- **Auto-scaling**: Scale based on demand
- **Reserved Capacity**: Commit to steady-state workloads
- **Spot Usage**: Use için fault-tolerant, flexible workloads
- **Storage Tiers**: Move infrequent Veri to cheaper tiers
- **Cleanup**: Delete unused resources, snapshots, AMIs

### Cost Yönetim Tools
- **AWS**: Cost Explorer, Budgets, Trusted Advisor
- **Azure**: Cost Yönetim, Advisor
- **GCP**: Billing reports, Recommender
- **Third-party**: CloudHealth, CloudCheckr, Datadog

## High Availability ve Disaster Recovery

### Availability Concepts
- **Availability Zones**: Physically separate Veri centers within region
- **Regions**: Geographic areas ile multiple AZs
- **Edge Locations**: CDN cache locations globally

### HA Strategies
- **Multi-AZ**: Deploy across availability zones
- **Auto-healing**: Auto-replace failed instances
- **Load Balancing**: Distribute traffic across healthy instances
- **Veritabanı Replication**: Multi-AZ deployments, read replicas

### Disaster Recovery Strategies
- **Backup ve Restore**: Periodic backups, restore when needed (lowest cost)
- **Pilot Light**: Core elements running, scale up during disaster
- **Warm Standby**: Scaled-down version always running
- **Multi-Site Active/Active**: Full production içinde multiple regions (highest cost)

### RTO ve RPO
- **Recovery Time Objective (RTO)**: Maximum acceptable downtime
- **Recovery Point Objective (RPO)**: Maximum acceptable Veri loss
- **Strategy Selection**: Based on İş requirements ve budget

## Emerging Trends

### Edge Bilişim
- Process Veri closer to source
- **Services**: AWS Outposts, Wavelength, Azure Edge, Cloud CDN
- **Use Cases**: IoT, real-time analytics, low-latency applications

### Multi-Cloud ve Hybrid Cloud
- Avoid vendor lock-içinde
- Leverage best-içinde-breed services
- **Tools**: Terraform, Anthos, Arc, CloudHealth

### AI/ML Services
- Pre-trained models: Vision, speech, Dil
- Custom model training: SageMaker, Vertex AI, Azure ML
- MLOps: Model Dağıtım, monitoring, governance

### Quantum Bilişim
- **Services**: AWS Braket, Azure Quantum
- **Status**: Early stage, experimental
- **Potential**: Cryptography, optimization, drug discovery

### Sustainable Cloud
- Carbon footprint tracking
- Renewable energy commitments
- Efficient resource utilization
- Green Mimari patterns
