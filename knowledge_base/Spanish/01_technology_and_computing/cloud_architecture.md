<!-- 
This file was automatically translated from English to Spanish.
Source: cloud_architecture.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# Cloud Arquitectura

# # Cloud Informática Fundamentos

# ## What is Cloud Informática?
On-demand delivery de Informática resources (servers, storage, databases, networking, software) over el/la internet con pay-as-you-go pricing.

# ## Essential Characteristics (NIST Definition)
- **On-Demand Self-Service**: Provision resources without human interaction
- **Broad Red Access**: Available over Red via standard mechanisms
- **Resource Pooling**: Multi-tenant model con dynamic assignment
- **Rapid Elasticity**: Scale outward y inward rapidly
- **Measured Service**: Resource usage monitored y billed

# ## Cloud Implementación Models
- **Public Cloud**: Owned by providers, shared infrastructure (AWS, Azure, GCP)
- **Private Cloud**: Dedicated to single organization (on-premises or hosted)
- **Hybrid Cloud**: Combination de public y private clouds
- **Multi-Cloud**: Using multiple public cloud providers
- **Community Cloud**: Shared by organizations con common concerns

# ## Service Models

# ### Infrastructure as a Service (IaaS)
- **Provides**: Virtual machines, storage, networks, operating Sistemas
- **Ejemplos**: AWS EC2, Google Compute Engine, Azure VMs
- **Use Cases**: Lift-y-shift migrations, Desarrollo environments, high-control needs

# ### Platform as a Service (PaaS)
- **Provides**: Desarrollo platforms, databases, middleware
- **Ejemplos**: Heroku, Google App Engine, AWS Elastic Beanstalk
- **Use Cases**: Application Desarrollo, API Implementación, microservices

# ### Software as a Service (SaaS)
- **Provides**: Complete applications over internet
- **Ejemplos**: Salesforce, Google Workspace, Microsoft 365, Slack
- **Use Cases**: Email, CRM, collaboration, Negocios applications

# ### Function as a Service (FaaS) / Serverless
- **Provides**: Event-driven function execution
- **Ejemplos**: AWS Lambda, Azure Functions, Google Cloud Functions
- **Use Cases**: Event processing, APIs, scheduled tasks, real-time processing

# # Major Cloud Providers

# ## Amazon Web Services (AWS)
- **Market Share**: ~32% (largest provider)
- **Key Services**:
  - Compute: EC2, Lambda, ECS, EKS
  - Storage: S3, EBS, Glacier
  - Base de datos: RDS, DynamoDB, Aurora
  - Networking: VPC, Route 53, CloudFront
  - AI/ML: SageMaker, Rekognition, Comprehend

# ## Microsoft Azure
- **Market Share**: ~23%
- **Strengths**: Enterprise integration, hybrid cloud, Microsoft ecosystem
- **Key Services**:
  - Compute: Virtual Machines, Azure Functions, AKS
  - Storage: Blob Storage, Disk Storage
  - Base de datos: SQL Base de datos, Cosmos DB
  - Networking: Virtual Red, Traffic Manager
  - AI/ML: Azure ML, Cognitive Services

# ## Google Cloud Platform (GCP)
- **Market Share**: ~10%
- **Strengths**: Datos analytics, AI/ML, Kubernetes
- **Key Services**:
  - Compute: Compute Engine, Cloud Functions, GKE
  - Storage: Cloud Storage, Persistent Disk
  - Base de datos: Cloud SQL, Firestore, Bigtable
  - Analytics: BigQuery, Dataflow, Pub/Sub
  - AI/ML: Vertex AI, AutoML

# ## Other Providers
- **IBM Cloud**: Enterprise focus, Watson AI
- **Oracle Cloud**: Base de datos workloads, enterprise applications
- **Alibaba Cloud**: Dominant en Asia-Pacific
- **DigitalOcean**: Developer-friendly, simplified offerings

# # Cloud Arquitectura Patterns

# ## Well-Architected Framework Principles

# ### Operational Excellence
- Automate operations
- Make frequent, reversible changes
- Refine procedures continuously
- Anticipate failure

# ### Seguridad
- Implement strong identity foundation
- Enable traceability
- Apply Seguridad at all layers
- Automate Seguridad Mejores prácticas
- Protect Datos en transit y at rest

# ### Reliability
- Test recovery procedures
- Automatically recover from failure
- Scale horizontally para availability
- Stop guessing capacity
- Manage change en automation

# ### Rendimiento Efficiency
- Democratize Avanzado technologies
- Go global en minutes
- Use serverless architectures
- Experiment more often
- Consider mechanical sympathy

# ### Cost Optimization
- Adopt consumption model
- Measure overall efficiency
- Stop spending money on undifferentiated work
- Analyze y attribute expenditure
- Use managed services

# ## Common Arquitectura Patterns

# ### Microservices Arquitectura
- Decompose applications into small, independent services
- Each service owns its Datos y logic
- Communicate via APIs (REST, gRPC, messaging)
- Deploy independently
- **Benefits**: Scalability, fault isolation, Tecnología diversity
- **Challenges**: Distributed complexity, Datos consistency, monitoring

# ### Event-Driven Arquitectura
- Components communicate through Eventos
- Producers emit Eventos, consumers react
- **Patterns**: Event sourcing, CQRS, pub/sub
- **Technologies**: Kafka, SNS/SQS, EventBridge, Pub/Sub
- **Benefits**: Loose coupling, scalability, real-time processing

# ### Serverless Arquitectura
- No server Gestión required
- Pay per execution
- Automatic scaling
- **Components**: Functions, API Gateway, managed services
- **Benefits**: Cost efficiency, reduced operations, rapid Implementación
- **Considerations**: Cold starts, vendor lock-en, execution limits

# ### Layered Arquitectura (N-Tier)
- Presentation layer (UI)
- Application/Negocios logic layer
- Datos access layer
- Base de datos layer
- **Benefits**: Separation de concerns, maintainability
- **Common**: 3-tier Web applications

# ### Space-Based Arquitectura
- Handle high concurrency con distributed Datos
- Virtualized memory across servers
- Processing nodes scale independently
- **Use Cases**: High-volume, low-latency applications

# # Compute Services

# ## Virtual Machines
- **Types**: General purpose, compute optimized, memory optimized, GPU
- **Pricing**: On-demand, reserved instances, spot instances
- **Gestión**: Auto-scaling groups, load balancers
- **Mejores prácticas**: Right-sizing, tagging, monitoring, patching

# ## Containers
- **Docker**: Container runtime standard
- **Orchestration**: Kubernetes (EKS, AKS, GKE), ECS, Fargate
- **Benefits**: Portability, efficiency, consistency
- **Registry**: ECR, GCR, ACR, Docker Hub

# ## Serverless Functions
- **Execution Model**: Event-triggered, stateless
- **Limits**: Execution time, memory, concurrent executions
- **Use Cases**: APIs, file processing, scheduled jobs, IoT backends
- **Monitoring**: Invocation counts, errors, duration, cold starts

# # Storage Solutions

# ## Object Storage
- **Characteristics**: Flat structure, metadata, HTTP access
- **Ejemplos**: AWS S3, Google Cloud Storage, Azure Blob
- **Use Cases**: Static assets, backups, Datos lakes, archives
- **Storage Classes**: Hot, cool, cold, archive (varying cost/access)

# ## Block Storage
- **Characteristics**: Raw volumes, attached to VMs
- **Ejemplos**: AWS EBS, Google Persistent Disk, Azure Disks
- **Use Cases**: Databases, boot volumes, high-Rendimiento needs
- **Types**: SSD, HDD, provisioned IOPS

# ## File Storage
- **Characteristics**: Shared file Sistemas, NFS/SMB protocols
- **Ejemplos**: AWS EFS, Google Filestore, Azure Files
- **Use Cases**: Content Gestión, shared configs, lift-y-shift

# ## Archive Storage
- **Characteristics**: Lowest cost, retrieval delays
- **Ejemplos**: S3 Glacier, Azure Archive Storage
- **Use Cases**: Compliance, long-term backups, historical Datos

# # Base de datos Services

# ## Managed Relational Databases
- **Services**: AWS RDS/Aurora, Google Cloud SQL, Azure SQL Base de datos
- **Features**: Automated backups, patching, scaling, replication
- **Engines**: MySQL, PostgreSQL, MariaDB, Oracle, SQL Server

# ## NoSQL Databases
- **Document**: DocumentDB, Firestore, Cosmos DB
- **Key-Value**: DynamoDB, Redis Cache
- **Wide-Column**: Bigtable, Cassandra (managed)
- **Graph**: Neptune, Cosmos DB (graph API)

# ## Datos Warehousing
- **Services**: Snowflake, Redshift, BigQuery, Synapse
- **Characteristics**: Columnar storage, MPP Arquitectura
- **Use Cases**: Analytics, BI, large-scale Datos analysis

# ## Caching Services
- **en-Memory**: ElastiCache (Redis/Memcached), Cloud Memorystore
- **CDN Caching**: CloudFront, Cloud CDN, Azure CDN
- **Use Cases**: Session storage, query caching, content delivery

# # Networking

# ## Virtual Networks
- **VPC/VNet**: Isolated Red environments
- **Subnets**: Public (internet-facing), private (internal only)
- **IP Addressing**: CIDR blocks, IPv4/IPv6
- **Route Tables**: Control traffic flow

# ## Load Balancing
- **Types**: Application (L7), Red (L4), Gateway
- **Features**: Health checks, SSL termination, sticky sessions
- **Services**: ELB/ALB/NLB, Cloud Load Balancing, Azure Load Balancer

# ## Content Delivery Networks (CDN)
- **Purpose**: Cache content at edge locations
- **Benefits**: Reduced latency, lower origin load, global distribution
- **Services**: CloudFront, Cloud CDN, Azure CDN, Akamai

# ## DNS Services
- **Functions**: Domain registration, routing, health checks
- **Services**: Route 53, Cloud DNS, Azure DNS
- **Routing Policies**: Simple, weighted, latency-based, geolocation, failover

# ## Connectivity Options
- **Internet Gateway**: Public internet access
- **NAT Gateway**: Private subnet outbound access
- **VPN**: Encrypted tunnels to on-premises
- **Direct Connect/ExpressRoute**: Dedicated private connections
- **VPC Peering**: Connect VPCs within/between accounts

# # Seguridad en el/la Cloud

# ## Shared Responsibility Model
- **Provider Responsibility**: Seguridad de el/la cloud (infrastructure)
- **Customer Responsibility**: Seguridad en el/la cloud (Datos, applications, access)
- **Varies By Service**: More managed = more provider responsibility

# ## Identity y Access Gestión (IAM)
- **Users**: Individual identities
- **Groups**: Collections de users
- **Roles**: Temporary credentials para services/users
- **Policies**: JSON documents defining permissions
- **Principles**: Least privilege, separation de duties

# ## Red Seguridad
- **Seguridad Groups**: Stateful firewalls para instances
- **Red ACLs**: Stateless firewalls para subnets
- **Web Application Firewall (WAF)**: Protect against Web exploits
- **DDoS Protection**: Shield, Cloud Armor, DDoS Protection

# ## Datos Protection
- **Encryption at Rest**: KMS, customer-managed keys
- **Encryption en Transit**: TLS/SSL, HTTPS
- **Key Gestión**: HSM, key rotation, audit trails
- **Secrets Gestión**: Secrets Manager, Key Vault

# ## Compliance y Governance
- **Certifications**: SOC 2, ISO 27001, HIPAA, PCI-DSS, GDPR
- **Tools**: Policy enforcement, compliance reporting, audit logs
- **Frameworks**: Cloud Seguridad Alliance, NIST CSF

# # DevOps en el/la Cloud

# ## CI/CD Services
- **AWS**: CodePipeline, CodeBuild, CodeDeploy
- **Azure**: Azure DevOps, GitHub Actions
- **GCP**: Cloud Build, Cloud Deploy
- **Third-party**: Jenkins, CircleCI, GitLab CI

# ## Infrastructure as Code (IaC)
- **Terraform**: Multi-cloud, declarative, state Gestión
- **CloudFormation**: AWS native, YAML/JSON templates
- **ARM Templates**: Azure native
- **Implementación Manager**: GCP native
- **Pulumi**: Infrastructure using programming languages
- **Benefits**: Version control, repeatability, documentation

# ## Configuration Gestión
- **Ansible**: Agentless, YAML playbooks
- **Chef**: Ruby-based, mature ecosystem
- **Puppet**: Declarative, strong reporting
- **SaltStack**: Fast, Python-based

# ## Monitoring y Observability
- **Metrics**: CloudWatch, Cloud Monitoring, Azure Monitor
- **Logging**: CloudWatch Logs, Cloud Logging, Log Analytics
- **Tracing**: X-Ray, Cloud Trace, Application Insights
- **Dashboards**: CloudWatch Dashboards, Cloud Console
- **Alerting**: SNS, Cloud Monitoring alerts, Action Groups

# ## Container Orchestration
- **Kubernetes**: Industry standard orchestration
- **Managed Services**: EKS, AKS, GKE
- **Service Mesh**: Istio, Linkerd (traffic Gestión, Seguridad)
- **GitOps**: ArgoCD, Flux (declarative deployments)

# # Cost Gestión

# ## Pricing Models
- **Pay-as-you-go**: Pay para what you use
- **Reserved Instances**: 1-3 year commitments, significant discounts
- **Spot Instances**: Bid para unused capacity, can be interrupted
- **Savings Plans**: Flexible commitment pricing
- **Free Tier**: Limited free usage para new accounts

# ## Cost Optimization Strategies
- **Right-sizing**: Match instance types to workload needs
- **Auto-scaling**: Scale based on demand
- **Reserved Capacity**: Commit to steady-state workloads
- **Spot Usage**: Use para fault-tolerant, flexible workloads
- **Storage Tiers**: Move infrequent Datos to cheaper tiers
- **Cleanup**: Delete unused resources, snapshots, AMIs

# ## Cost Gestión Tools
- **AWS**: Cost Explorer, Budgets, Trusted Advisor
- **Azure**: Cost Gestión, Advisor
- **GCP**: Billing reports, Recommender
- **Third-party**: CloudHealth, CloudCheckr, Datadog

# # High Availability y Disaster Recovery

# ## Availability Concepts
- **Availability Zones**: Physically separate Datos centers within region
- **Regions**: Geographic areas con multiple AZs
- **Edge Locations**: CDN cache locations globally

# ## HA Strategies
- **Multi-AZ**: Deploy across availability zones
- **Auto-healing**: Auto-replace failed instances
- **Load Balancing**: Distribute traffic across healthy instances
- **Base de datos Replication**: Multi-AZ deployments, read replicas

# ## Disaster Recovery Strategies
- **Backup y Restore**: Periodic backups, restore when needed (lowest cost)
- **Pilot Light**: Core elements running, scale up during disaster
- **Warm Standby**: Scaled-down version always running
- **Multi-Site Active/Active**: Full production en multiple regions (highest cost)

# ## RTO y RPO
- **Recovery Time Objective (RTO)**: Maximum acceptable downtime
- **Recovery Point Objective (RPO)**: Maximum acceptable Datos loss
- **Strategy Selection**: Based on Negocios requirements y budget

# # Emerging Trends

# ## Edge Informática
- Process Datos closer to source
- **Services**: AWS Outposts, Wavelength, Azure Edge, Cloud CDN
- **Use Cases**: IoT, real-time analytics, low-latency applications

# ## Multi-Cloud y Hybrid Cloud
- Avoid vendor lock-en
- Leverage best-de-breed services
- **Tools**: Terraform, Anthos, Arc, CloudHealth

# ## AI/ML Services
- Pre-trained models: Vision, speech, Idioma
- Custom model training: SageMaker, Vertex AI, Azure ML
- MLOps: Model Implementación, monitoring, governance

# ## Quantum Informática
- **Services**: AWS Braket, Azure Quantum
- **Status**: Early stage, experimental
- **Potential**: Cryptography, optimization, drug discovery

# ## Sustainable Cloud
- Carbon footprint tracking
- Renewable energy commitments
- Efficient resource utilization
- Green Arquitectura patterns
