<!-- 
This file was automatically translated from English to Portuguese.
Source: cloud_architecture.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# Cloud Arquitetura

## Cloud Computação Fundamentos

### What is Cloud Computação?
On-demand delivery de Computação resources (servers, storage, databases, networking, software) over o/a internet com pay-as-you-go pricing.

### Essential Characteristics (NIST Definition)
- **On-Demand Self-Service**: Provision resources without human interaction
- **Broad Rede Access**: Disponível over Rede via standard mechanisms
- **Resource Pooling**: Multi-tenant model com dynamic assignment
- **Rapid Elasticity**: Scale outward e inward rapidly
- **Measured Service**: Resource usage monitored e billed

### Cloud Implantação Models
- **Public Cloud**: Owned by providers, shared infrastructure (AWS, Azure, GCP)
- **Private Cloud**: Dedicated to single organization (on-premises or hosted)
- **Hybrid Cloud**: Combination de public e private clouds
- **Multi-Cloud**: Using multiple public cloud providers
- **Community Cloud**: Shared by organizations com common concerns

### Service Models

#### Infrastructure as a Service (IaaS)
- **Provides**: Virtual machines, storage, networks, operating Sistemas
- **Exemplos**: AWS EC2, Google Compute Engine, Azure VMs
- **Use Cases**: Lift-e-shift migrations, Desenvolvimento environments, high-control needs

#### Platform as a Service (PaaS)
- **Provides**: Desenvolvimento platforms, databases, middleware
- **Exemplos**: Heroku, Google App Engine, AWS Elastic Beanstalk
- **Use Cases**: Application Desenvolvimento, API Implantação, microservices

#### Software as a Service (SaaS)
- **Provides**: Completo applications over internet
- **Exemplos**: Salesforce, Google Workspace, Microsoft 365, Slack
- **Use Cases**: Email, CRM, collaboration, Negócios applications

#### Function as a Service (FaaS) / Serverless
- **Provides**: Event-driven function execution
- **Exemplos**: AWS Lambda, Azure Functions, Google Cloud Functions
- **Use Cases**: Event processing, APIs, scheduled tasks, real-time processing

## Major Cloud Providers

### Amazon Web Services (AWS)
- **Market Share**: ~32% (largest provider)
- **Key Services**:
  - Compute: EC2, Lambda, ECS, EKS
  - Storage: S3, EBS, Glacier
  - Banco de dados: RDS, DynamoDB, Aurora
  - Networking: VPC, Route 53, CloudFront
  - AI/ML: SageMaker, Rekognition, Comprehend

### Microsoft Azure
- **Market Share**: ~23%
- **Strengths**: Enterprise integration, hybrid cloud, Microsoft ecosystem
- **Key Services**:
  - Compute: Virtual Machines, Azure Functions, AKS
  - Storage: Blob Storage, Disk Storage
  - Banco de dados: SQL Banco de dados, Cosmos DB
  - Networking: Virtual Rede, Traffic Manager
  - AI/ML: Azure ML, Cognitive Services

### Google Cloud Platform (GCP)
- **Market Share**: ~10%
- **Strengths**: Dados analytics, AI/ML, Kubernetes
- **Key Services**:
  - Compute: Compute Engine, Cloud Functions, GKE
  - Storage: Cloud Storage, Persistent Disk
  - Banco de dados: Cloud SQL, Firestore, Bigtable
  - Analytics: BigQuery, Dataflow, Pub/Sub
  - AI/ML: Vertex AI, AutoML

### Other Providers
- **IBM Cloud**: Enterprise focus, Watson AI
- **Oracle Cloud**: Banco de dados workloads, enterprise applications
- **Alibaba Cloud**: Dominant em Asia-Pacific
- **DigitalOcean**: Developer-friendly, simplified offerings

## Cloud Arquitetura Patterns

### Well-Architected Framework Principles

#### Operational Excellence
- Automate operations
- Make frequent, reversible changes
- Refine procedures continuously
- Anticipate failure

#### Segurança
- Implement strong identity foundation
- Enable traceability
- Apply Segurança at all layers
- Automate Segurança Melhores práticas
- Protect Dados em transit e at rest

#### Reliability
- Test recovery procedures
- Automatically recover from failure
- Scale horizontally para availability
- Stop guessing capacity
- Manage change em automation

#### Desempenho Efficiency
- Democratize Avançado technologies
- Go global em minutes
- Use serverless architectures
- Experiment more often
- Consider mechanical sympathy

#### Cost Optimization
- Adopt consumption model
- Measure overall efficiency
- Stop spending money on undifferentiated work
- Analyze e attribute expenditure
- Use managed services

### Common Arquitetura Patterns

#### Microservices Arquitetura
- Decompose applications into small, independent services
- Each service owns its Dados e logic
- Communicate via APIs (REST, gRPC, messaging)
- Deploy independently
- **Benefits**: Scalability, fault isolation, Tecnologia diversity
- **Challenges**: Distributed complexity, Dados consistency, monitoring

#### Event-Driven Arquitetura
- Components communicate through Eventos
- Producers emit Eventos, consumers react
- **Patterns**: Event sourcing, CQRS, pub/sub
- **Technologies**: Kafka, SNS/SQS, EventBridge, Pub/Sub
- **Benefits**: Loose coupling, scalability, real-time processing

#### Serverless Arquitetura
- No server Gerenciamento required
- Pay per execution
- Automatic scaling
- **Components**: Functions, API Gateway, managed services
- **Benefits**: Cost efficiency, reduced operations, rapid Implantação
- **Considerations**: Cold starts, vendor lock-em, execution limits

#### Layered Arquitetura (N-Tier)
- Presentation layer (UI)
- Application/Negócios logic layer
- Dados access layer
- Banco de dados layer
- **Benefits**: Separation de concerns, maintainability
- **Common**: 3-tier Web applications

#### Space-Based Arquitetura
- Handle high concurrency com distributed Dados
- Virtualized memory across servers
- Processing nodes scale independently
- **Use Cases**: High-volume, low-latency applications

## Compute Services

### Virtual Machines
- **Types**: General purpose, compute optimized, memory optimized, GPU
- **Pricing**: On-demand, reserved instances, spot instances
- **Gerenciamento**: Auto-scaling groups, load balancers
- **Melhores práticas**: Right-sizing, tagging, monitoring, patching

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
- **Exemplos**: AWS S3, Google Cloud Storage, Azure Blob
- **Use Cases**: Static assets, backups, Dados lakes, archives
- **Storage Classes**: Hot, cool, cold, archive (varying cost/access)

### Block Storage
- **Characteristics**: Raw volumes, attached to VMs
- **Exemplos**: AWS EBS, Google Persistent Disk, Azure Disks
- **Use Cases**: Databases, boot volumes, high-Desempenho needs
- **Types**: SSD, HDD, provisioned IOPS

### File Storage
- **Characteristics**: Shared file Sistemas, NFS/SMB protocols
- **Exemplos**: AWS EFS, Google Filestore, Azure Files
- **Use Cases**: Content Gerenciamento, shared configs, lift-e-shift

### Archive Storage
- **Characteristics**: Lowest cost, retrieval delays
- **Exemplos**: S3 Glacier, Azure Archive Storage
- **Use Cases**: Compliance, long-term backups, historical Dados

## Banco de dados Services

### Managed Relational Databases
- **Services**: AWS RDS/Aurora, Google Cloud SQL, Azure SQL Banco de dados
- **Features**: Automated backups, patching, scaling, replication
- **Engines**: MySQL, PostgreSQL, MariaDB, Oracle, SQL Server

### NoSQL Databases
- **Document**: DocumentDB, Firestore, Cosmos DB
- **Key-Value**: DynamoDB, Redis Cache
- **Wide-Column**: Bigtable, Cassandra (managed)
- **Graph**: Neptune, Cosmos DB (graph API)

### Dados Warehousing
- **Services**: Snowflake, Redshift, BigQuery, Synapse
- **Characteristics**: Columnar storage, MPP Arquitetura
- **Use Cases**: Analytics, BI, large-scale Dados analysis

### Caching Services
- **em-Memory**: ElastiCache (Redis/Memcached), Cloud Memorystore
- **CDN Caching**: CloudFront, Cloud CDN, Azure CDN
- **Use Cases**: Session storage, query caching, content delivery

## Networking

### Virtual Networks
- **VPC/VNet**: Isolated Rede environments
- **Subnets**: Public (internet-facing), private (internal only)
- **IP Addressing**: CIDR blocks, IPv4/IPv6
- **Route Tables**: Control traffic flow

### Load Balancing
- **Types**: Application (L7), Rede (L4), Gateway
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

## Segurança em o/a Cloud

### Shared Responsibility Model
- **Provider Responsibility**: Segurança de o/a cloud (infrastructure)
- **Customer Responsibility**: Segurança em o/a cloud (Dados, applications, access)
- **Varies By Service**: More managed = more provider responsibility

### Identity e Access Gerenciamento (IAM)
- **Users**: Individual identities
- **Groups**: Collections de users
- **Roles**: Temporary credentials para services/users
- **Policies**: JSON documents defining permissions
- **Principles**: Least privilege, separation de duties

### Rede Segurança
- **Segurança Groups**: Stateful firewalls para instances
- **Rede ACLs**: Stateless firewalls para subnets
- **Web Application Firewall (WAF)**: Protect against Web exploits
- **DDoS Protection**: Shield, Cloud Armor, DDoS Protection

### Dados Protection
- **Encryption at Rest**: KMS, customer-managed keys
- **Encryption em Transit**: TLS/SSL, HTTPS
- **Key Gerenciamento**: HSM, key rotation, audit trails
- **Secrets Gerenciamento**: Secrets Manager, Key Vault

### Compliance e Governance
- **Certifications**: SOC 2, ISO 27001, HIPAA, PCI-DSS, GDPR
- **Tools**: Policy enforcement, compliance reporting, audit logs
- **Frameworks**: Cloud Segurança Alliance, NIST CSF

## DevOps em o/a Cloud

### CI/CD Services
- **AWS**: CodePipeline, CodeBuild, CodeDeploy
- **Azure**: Azure DevOps, GitHub Actions
- **GCP**: Cloud Build, Cloud Deploy
- **Third-party**: Jenkins, CircleCI, GitLab CI

### Infrastructure as Code (IaC)
- **Terraform**: Multi-cloud, declarative, state Gerenciamento
- **CloudFormation**: AWS native, YAML/JSON templates
- **ARM Templates**: Azure native
- **Implantação Manager**: GCP native
- **Pulumi**: Infrastructure using programming languages
- **Benefits**: Version control, repeatability, documentation

### Configuration Gerenciamento
- **Ansible**: Agentless, YAML playbooks
- **Chef**: Ruby-based, mature ecosystem
- **Puppet**: Declarative, strong reporting
- **SaltStack**: Fast, Python-based

### Monitoring e Observability
- **Metrics**: CloudWatch, Cloud Monitoring, Azure Monitor
- **Logging**: CloudWatch Logs, Cloud Logging, Log Analytics
- **Tracing**: X-Ray, Cloud Trace, Application Insights
- **Dashboards**: CloudWatch Dashboards, Cloud Console
- **Alerting**: SNS, Cloud Monitoring alerts, Action Groups

### Container Orchestration
- **Kubernetes**: Industry standard orchestration
- **Managed Services**: EKS, AKS, GKE
- **Service Mesh**: Istio, Linkerd (traffic Gerenciamento, Segurança)
- **GitOps**: ArgoCD, Flux (declarative deployments)

## Cost Gerenciamento

### Pricing Models
- **Pay-as-you-go**: Pay para what you use
- **Reserved Instances**: 1-3 year commitments, significant discounts
- **Spot Instances**: Bid para unused capacity, can be interrupted
- **Savings Plans**: Flexible commitment pricing
- **Free Tier**: Limited free usage para new accounts

### Cost Optimization Strategies
- **Right-sizing**: Match instance types to workload needs
- **Auto-scaling**: Scale based on demand
- **Reserved Capacity**: Commit to steady-state workloads
- **Spot Usage**: Use para fault-tolerant, flexible workloads
- **Storage Tiers**: Move infrequent Dados to cheaper tiers
- **Cleanup**: Delete unused resources, snapshots, AMIs

### Cost Gerenciamento Tools
- **AWS**: Cost Explorer, Budgets, Trusted Advisor
- **Azure**: Cost Gerenciamento, Advisor
- **GCP**: Billing reports, Recommender
- **Third-party**: CloudHealth, CloudCheckr, Datadog

## High Availability e Disaster Recovery

### Availability Concepts
- **Availability Zones**: Physically separate Dados centers within region
- **Regions**: Geographic areas com multiple AZs
- **Edge Locations**: CDN cache locations globally

### HA Strategies
- **Multi-AZ**: Deploy across availability zones
- **Auto-healing**: Auto-replace failed instances
- **Load Balancing**: Distribute traffic across healthy instances
- **Banco de dados Replication**: Multi-AZ deployments, read replicas

### Disaster Recovery Strategies
- **Backup e Restore**: Periodic backups, restore when needed (lowest cost)
- **Pilot Light**: Core elements running, scale up during disaster
- **Warm Standby**: Scaled-down version always running
- **Multi-Site Active/Active**: Full production em multiple regions (highest cost)

### RTO e RPO
- **Recovery Time Objective (RTO)**: Maximum acceptable downtime
- **Recovery Point Objective (RPO)**: Maximum acceptable Dados loss
- **Strategy Selection**: Based on Negócios requirements e budget

## Emerging Trends

### Edge Computação
- Process Dados closer to source
- **Services**: AWS Outposts, Wavelength, Azure Edge, Cloud CDN
- **Use Cases**: IoT, real-time analytics, low-latency applications

### Multi-Cloud e Hybrid Cloud
- Avoid vendor lock-em
- Leverage best-de-breed services
- **Tools**: Terraform, Anthos, Arc, CloudHealth

### AI/ML Services
- Pre-trained models: Vision, speech, Idioma
- Custom model training: SageMaker, Vertex AI, Azure ML
- MLOps: Model Implantação, monitoring, governance

### Quantum Computação
- **Services**: AWS Braket, Azure Quantum
- **Status**: Early stage, experimental
- **Potential**: Cryptography, optimization, drug discovery

### Sustainable Cloud
- Carbon footprint tracking
- Renewable energy commitments
- Efficient resource utilization
- Green Arquitetura patterns
