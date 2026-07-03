<!-- 
This file was automatically translated from English to German.
Source: cloud_architecture.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# Cloud Architektur

## Cloud Datenverarbeitung Grundlagen

### What is Cloud Datenverarbeitung?
On-demand delivery von Datenverarbeitung resources (servers, storage, databases, networking, software) over der/die/das internet mit pay-as-you-go pricing.

### Essential Characteristics (NIST Definition)
- **On-Demand Self-Service**: Provision resources without human interaction
- **Broad Netzwerk Access**: Verfügbar over Netzwerk via standard mechanisms
- **Resource Pooling**: Multi-tenant model mit dynamic assignment
- **Rapid Elasticity**: Scale outward und inward rapidly
- **Measured Service**: Resource usage monitored und billed

### Cloud Bereitstellung Models
- **Public Cloud**: Owned by providers, shared infrastructure (AWS, Azure, GCP)
- **Private Cloud**: Dedicated to single organization (on-premises or hosted)
- **Hybrid Cloud**: Combination von public und private clouds
- **Multi-Cloud**: Using multiple public cloud providers
- **Community Cloud**: Shared by organizations mit common concerns

### Service Models

#### Infrastructure as a Service (IaaS)
- **Provides**: Virtual machines, storage, networks, operating Systeme
- **Beispiele**: AWS EC2, Google Compute Engine, Azure VMs
- **Use Cases**: Lift-und-shift migrations, Entwicklung environments, high-control needs

#### Platform as a Service (PaaS)
- **Provides**: Entwicklung platforms, databases, middleware
- **Beispiele**: Heroku, Google App Engine, AWS Elastic Beanstalk
- **Use Cases**: Application Entwicklung, API Bereitstellung, microservices

#### Software as a Service (SaaS)
- **Provides**: Vollständig applications over internet
- **Beispiele**: Salesforce, Google Workspace, Microsoft 365, Slack
- **Use Cases**: Email, CRM, collaboration, Geschäft applications

#### Function as a Service (FaaS) / Serverless
- **Provides**: Event-driven function execution
- **Beispiele**: AWS Lambda, Azure Functions, Google Cloud Functions
- **Use Cases**: Event processing, APIs, scheduled tasks, real-time processing

## Major Cloud Providers

### Amazon Web Services (AWS)
- **Market Share**: ~32% (largest provider)
- **Key Services**:
  - Compute: EC2, Lambda, ECS, EKS
  - Storage: S3, EBS, Glacier
  - Datenbank: RDS, DynamoDB, Aurora
  - Networking: VPC, Route 53, CloudFront
  - AI/ML: SageMaker, Rekognition, Comprehend

### Microsoft Azure
- **Market Share**: ~23%
- **Strengths**: Enterprise integration, hybrid cloud, Microsoft ecosystem
- **Key Services**:
  - Compute: Virtual Machines, Azure Functions, AKS
  - Storage: Blob Storage, Disk Storage
  - Datenbank: SQL Datenbank, Cosmos DB
  - Networking: Virtual Netzwerk, Traffic Manager
  - AI/ML: Azure ML, Cognitive Services

### Google Cloud Platform (GCP)
- **Market Share**: ~10%
- **Strengths**: Daten analytics, AI/ML, Kubernetes
- **Key Services**:
  - Compute: Compute Engine, Cloud Functions, GKE
  - Storage: Cloud Storage, Persistent Disk
  - Datenbank: Cloud SQL, Firestore, Bigtable
  - Analytics: BigQuery, Dataflow, Pub/Sub
  - AI/ML: Vertex AI, AutoML

### Other Providers
- **IBM Cloud**: Enterprise focus, Watson AI
- **Oracle Cloud**: Datenbank workloads, enterprise applications
- **Alibaba Cloud**: Dominant in Asia-Pacific
- **DigitalOcean**: Developer-friendly, simplified offerings

## Cloud Architektur Patterns

### Well-Architected Framework Principles

#### Operational Excellence
- Automate operations
- Make frequent, reversible changes
- Refine procedures continuously
- Anticipate failure

#### Sicherheit
- Implement strong identity foundation
- Enable traceability
- Apply Sicherheit at all layers
- Automate Sicherheit Best Practices
- Protect Daten in transit und at rest

#### Reliability
- Test recovery procedures
- Automatically recover from failure
- Scale horizontally für availability
- Stop guessing capacity
- Manage change in automation

#### Leistung Efficiency
- Democratize Fortgeschritten technologies
- Go global in minutes
- Use serverless architectures
- Experiment more often
- Consider mechanical sympathy

#### Cost Optimization
- Adopt consumption model
- Measure overall efficiency
- Stop spending money on undifferentiated work
- Analyze und attribute expenditure
- Use managed services

### Common Architektur Patterns

#### Microservices Architektur
- Decompose applications into small, independent services
- Each service owns its Daten und logic
- Communicate via APIs (REST, gRPC, messaging)
- Deploy independently
- **Benefits**: Scalability, fault isolation, Technologie diversity
- **Challenges**: Distributed complexity, Daten consistency, monitoring

#### Event-Driven Architektur
- Components communicate through Ereignisse
- Producers emit Ereignisse, consumers react
- **Patterns**: Event sourcing, CQRS, pub/sub
- **Technologies**: Kafka, SNS/SQS, EventBridge, Pub/Sub
- **Benefits**: Loose coupling, scalability, real-time processing

#### Serverless Architektur
- No server Verwaltung required
- Pay per execution
- Automatic scaling
- **Components**: Functions, API Gateway, managed services
- **Benefits**: Cost efficiency, reduced operations, rapid Bereitstellung
- **Considerations**: Cold starts, vendor lock-in, execution limits

#### Layered Architektur (N-Tier)
- Presentation layer (UI)
- Application/Geschäft logic layer
- Daten access layer
- Datenbank layer
- **Benefits**: Separation von concerns, maintainability
- **Common**: 3-tier Web applications

#### Space-Based Architektur
- Handle high concurrency mit distributed Daten
- Virtualized memory across servers
- Processing nodes scale independently
- **Use Cases**: High-volume, low-latency applications

## Compute Services

### Virtual Machines
- **Types**: General purpose, compute optimized, memory optimized, GPU
- **Pricing**: On-demand, reserved instances, spot instances
- **Verwaltung**: Auto-scaling groups, load balancers
- **Best Practices**: Right-sizing, tagging, monitoring, patching

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
- **Beispiele**: AWS S3, Google Cloud Storage, Azure Blob
- **Use Cases**: Static assets, backups, Daten lakes, archives
- **Storage Classes**: Hot, cool, cold, archive (varying cost/access)

### Block Storage
- **Characteristics**: Raw volumes, attached to VMs
- **Beispiele**: AWS EBS, Google Persistent Disk, Azure Disks
- **Use Cases**: Databases, boot volumes, high-Leistung needs
- **Types**: SSD, HDD, provisioned IOPS

### File Storage
- **Characteristics**: Shared file Systeme, NFS/SMB protocols
- **Beispiele**: AWS EFS, Google Filestore, Azure Files
- **Use Cases**: Content Verwaltung, shared configs, lift-und-shift

### Archive Storage
- **Characteristics**: Lowest cost, retrieval delays
- **Beispiele**: S3 Glacier, Azure Archive Storage
- **Use Cases**: Compliance, long-term backups, historical Daten

## Datenbank Services

### Managed Relational Databases
- **Services**: AWS RDS/Aurora, Google Cloud SQL, Azure SQL Datenbank
- **Features**: Automated backups, patching, scaling, replication
- **Engines**: MySQL, PostgreSQL, MariaDB, Oracle, SQL Server

### NoSQL Databases
- **Document**: DocumentDB, Firestore, Cosmos DB
- **Key-Value**: DynamoDB, Redis Cache
- **Wide-Column**: Bigtable, Cassandra (managed)
- **Graph**: Neptune, Cosmos DB (graph API)

### Daten Warehousing
- **Services**: Snowflake, Redshift, BigQuery, Synapse
- **Characteristics**: Columnar storage, MPP Architektur
- **Use Cases**: Analytics, BI, large-scale Daten analysis

### Caching Services
- **in-Memory**: ElastiCache (Redis/Memcached), Cloud Memorystore
- **CDN Caching**: CloudFront, Cloud CDN, Azure CDN
- **Use Cases**: Session storage, query caching, content delivery

## Networking

### Virtual Networks
- **VPC/VNet**: Isolated Netzwerk environments
- **Subnets**: Public (internet-facing), private (internal only)
- **IP Addressing**: CIDR blocks, IPv4/IPv6
- **Route Tables**: Control traffic flow

### Load Balancing
- **Types**: Application (L7), Netzwerk (L4), Gateway
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

## Sicherheit in der/die/das Cloud

### Shared Responsibility Model
- **Provider Responsibility**: Sicherheit von der/die/das cloud (infrastructure)
- **Customer Responsibility**: Sicherheit in der/die/das cloud (Daten, applications, access)
- **Varies By Service**: More managed = more provider responsibility

### Identity und Access Verwaltung (IAM)
- **Users**: Individual identities
- **Groups**: Collections von users
- **Roles**: Temporary credentials für services/users
- **Policies**: JSON documents defining permissions
- **Principles**: Least privilege, separation von duties

### Netzwerk Sicherheit
- **Sicherheit Groups**: Stateful firewalls für instances
- **Netzwerk ACLs**: Stateless firewalls für subnets
- **Web Application Firewall (WAF)**: Protect against Web exploits
- **DDoS Protection**: Shield, Cloud Armor, DDoS Protection

### Daten Protection
- **Encryption at Rest**: KMS, customer-managed keys
- **Encryption in Transit**: TLS/SSL, HTTPS
- **Key Verwaltung**: HSM, key rotation, audit trails
- **Secrets Verwaltung**: Secrets Manager, Key Vault

### Compliance und Governance
- **Certifications**: SOC 2, ISO 27001, HIPAA, PCI-DSS, GDPR
- **Tools**: Policy enforcement, compliance reporting, audit logs
- **Frameworks**: Cloud Sicherheit Alliance, NIST CSF

## DevOps in der/die/das Cloud

### CI/CD Services
- **AWS**: CodePipeline, CodeBuild, CodeDeploy
- **Azure**: Azure DevOps, GitHub Actions
- **GCP**: Cloud Build, Cloud Deploy
- **Third-party**: Jenkins, CircleCI, GitLab CI

### Infrastructure as Code (IaC)
- **Terraform**: Multi-cloud, declarative, state Verwaltung
- **CloudFormation**: AWS native, YAML/JSON templates
- **ARM Templates**: Azure native
- **Bereitstellung Manager**: GCP native
- **Pulumi**: Infrastructure using programming languages
- **Benefits**: Version control, repeatability, documentation

### Configuration Verwaltung
- **Ansible**: Agentless, YAML playbooks
- **Chef**: Ruby-based, mature ecosystem
- **Puppet**: Declarative, strong reporting
- **SaltStack**: Fast, Python-based

### Monitoring und Observability
- **Metrics**: CloudWatch, Cloud Monitoring, Azure Monitor
- **Logging**: CloudWatch Logs, Cloud Logging, Log Analytics
- **Tracing**: X-Ray, Cloud Trace, Application Insights
- **Dashboards**: CloudWatch Dashboards, Cloud Console
- **Alerting**: SNS, Cloud Monitoring alerts, Action Groups

### Container Orchestration
- **Kubernetes**: Industry standard orchestration
- **Managed Services**: EKS, AKS, GKE
- **Service Mesh**: Istio, Linkerd (traffic Verwaltung, Sicherheit)
- **GitOps**: ArgoCD, Flux (declarative deployments)

## Cost Verwaltung

### Pricing Models
- **Pay-as-you-go**: Pay für what you use
- **Reserved Instances**: 1-3 year commitments, significant discounts
- **Spot Instances**: Bid für unused capacity, can be interrupted
- **Savings Plans**: Flexible commitment pricing
- **Free Tier**: Limited free usage für new accounts

### Cost Optimization Strategies
- **Right-sizing**: Match instance types to workload needs
- **Auto-scaling**: Scale based on demand
- **Reserved Capacity**: Commit to steady-state workloads
- **Spot Usage**: Use für fault-tolerant, flexible workloads
- **Storage Tiers**: Move infrequent Daten to cheaper tiers
- **Cleanup**: Delete unused resources, snapshots, AMIs

### Cost Verwaltung Tools
- **AWS**: Cost Explorer, Budgets, Trusted Advisor
- **Azure**: Cost Verwaltung, Advisor
- **GCP**: Billing reports, Recommender
- **Third-party**: CloudHealth, CloudCheckr, Datadog

## High Availability und Disaster Recovery

### Availability Concepts
- **Availability Zones**: Physically separate Daten centers within region
- **Regions**: Geographic areas mit multiple AZs
- **Edge Locations**: CDN cache locations globally

### HA Strategies
- **Multi-AZ**: Deploy across availability zones
- **Auto-healing**: Auto-replace failed instances
- **Load Balancing**: Distribute traffic across healthy instances
- **Datenbank Replication**: Multi-AZ deployments, read replicas

### Disaster Recovery Strategies
- **Backup und Restore**: Periodic backups, restore when needed (lowest cost)
- **Pilot Light**: Core elements running, scale up during disaster
- **Warm Standby**: Scaled-down version always running
- **Multi-Site Active/Active**: Full production in multiple regions (highest cost)

### RTO und RPO
- **Recovery Time Objective (RTO)**: Maximum acceptable downtime
- **Recovery Point Objective (RPO)**: Maximum acceptable Daten loss
- **Strategy Selection**: Based on Geschäft requirements und budget

## Emerging Trends

### Edge Datenverarbeitung
- Process Daten closer to source
- **Services**: AWS Outposts, Wavelength, Azure Edge, Cloud CDN
- **Use Cases**: IoT, real-time analytics, low-latency applications

### Multi-Cloud und Hybrid Cloud
- Avoid vendor lock-in
- Leverage best-von-breed services
- **Tools**: Terraform, Anthos, Arc, CloudHealth

### AI/ML Services
- Pre-trained models: Vision, speech, Sprache
- Custom model training: SageMaker, Vertex AI, Azure ML
- MLOps: Model Bereitstellung, monitoring, governance

### Quantum Datenverarbeitung
- **Services**: AWS Braket, Azure Quantum
- **Status**: Early stage, experimental
- **Potential**: Cryptography, optimization, drug discovery

### Sustainable Cloud
- Carbon footprint tracking
- Renewable energy commitments
- Efficient resource utilization
- Green Architektur patterns
