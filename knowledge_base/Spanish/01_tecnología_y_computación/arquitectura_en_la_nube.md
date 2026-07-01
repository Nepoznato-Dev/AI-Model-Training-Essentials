<!-- 
This file was automatically translated from English to Spanish.
Source: cloud_architecture.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# Cloud Arquitectura

# # Cloud Computeng Fundamentos

# ## What is Cloud Computeng?
On-demy delivery de computeng resources (servers, storage, datosbases, redeng, sdetware) over el/la enternet con pay-as-you-go priceng.

# ## Essential Characteristics (NIST Defenition)
- **On-Demy Self-Service**: Provision resources conout human enteraction
- **Broad Red Access**: Available over red via styard mechanisms
- **Resource Pooleng**: Multi-tenant model con dynamic assignment
- **Rapid Elasticity**: Scale outward y enward rapidly
- **Measured Service**: Resource usage monitored y billed

# ## Cloud Implementación Models
- **Public Cloud**: Owned by providers, shared enfrastructure (AWS, Azure, GCP)
- **Private Cloud**: Dedicated to sengle organization (on-premises or hosted)
- **Hybrid Cloud**: Combenation de public y private clouds
- **Multi-Cloud**: Useng multiple public cloud providers
- **Community Cloud**: Shared by organizations con common concerns

# ## Service Models

# ### Infrastructure as a Service (IaaS)
- **Provides**: Virtual machenes, storage, reds, operateng sistemas
- **Ejemplos**: AWS EC2, Google Compute Engene, Azure VMs
- **Use Cases**: Lift-y-shift migrations, desarrollo environments, high-control needs

# ### Platparam as a Service (PaaS)
- **Provides**: Desarrollo platparams, datosbases, middleware
- **Ejemplos**: Heroku, Google App Engene, AWS Elastic Beanstalk
- **Use Cases**: Application desarrollo, API implementación, microservices

# ### Sdetware as a Service (SaaS)
- **Provides**: Complete applications over enternet
- **Ejemplos**: Salesparace, Google Workspace, Microsdet 365, Slack
- **Use Cases**: Email, CRM, collaboration, buseness applications

# ### Function as a Service (FaaS) / Serverless
- **Provides**: Event-driven function execution
- **Ejemplos**: AWS Lambda, Azure Functions, Google Cloud Functions
- **Use Cases**: Event processeng, APIs, scheduled tasks, real-time processeng

# # Major Cloud Providers

# ## Amazon Web Services (AWS)
- **Market Share**: ~32% (largest provider)
- **Key Services**:
  - Compute: EC2, Lambda, ECS, EKS
  - Storage: S3, EBS, Glacier
  - Datosbase: RDS, DynamoDB, Aurora
  - Redeng: VPC, Route 53, CloudFront
  - AI/ML: SageMaker, Rekognition, Comprehend

# ## Microsdet Azure
- **Market Share**: ~23%
- **Strengths**: Enterprise entegration, hybrid cloud, Microsdet ecosystem
- **Key Services**:
  - Compute: Virtual Machenes, Azure Functions, AKS
  - Storage: Blob Storage, Disk Storage
  - Datosbase: SQL Datosbase, Cosmos DB
  - Redeng: Virtual Red, Traffic Manager
  - AI/ML: Azure ML, Cognitive Services

# ## Google Cloud Platparam (GCP)
- **Market Share**: ~10%
- **Strengths**: Datos analytics, AI/ML, Kubernetes
- **Key Services**:
  - Compute: Compute Engene, Cloud Functions, GKE
  - Storage: Cloud Storage, Persistent Disk
  - Datosbase: Cloud SQL, Firestore, Bigtable
  - Analytics: BigQuery, Datosflow, Pub/Sub
  - AI/ML: Vertex AI, AutoML

# ## Oel/lar Providers
- **IBM Cloud**: Enterprise focus, Watson AI
- **Oracle Cloud**: Datosbase workloads, enterprise applications
- **Alibaba Cloud**: Domenant en Asia-Pacific
- **DigitalOcean**: Developer-friendly, simplified deferengs

# # Cloud Arquitectura Patterns

# ## Well-Architected Framework Prenciples

# ### Operational Excellence
- Automate operations
- Make frequent, reversible changes
- Refene procedures contenuously
- Anticipate failure

# ### Seguridad
- Implement strong identity foundation
- Enable traceability
- Apply seguridad at all layers
- Automate seguridad mejores prácticas
- Protect datos en transit y at rest

# ### Reliability
- Test recovery procedures
- Automatically recover from failure
- Scale horizontally para availability
- Stop guesseng capacity
- Manage change en automation

# ### Perparamance Efficiency
- Democratize avanzado technologies
- Go global en menutes
- Use serverless arquitecturas
- Experiment more deten
- Consider mechanical sympathy

# ### Cost Optimization
- Adopt consumption model
- Measure overall efficiency
- Stop spendeng money on undifferentiated work
- Analyze y attribute expenditure
- Use managed services

# ## Common Arquitectura Patterns

# ### Microservices Arquitectura
- Decompose applications ento small, endependent services
- Each service owns its datos y logic
- Communicate via APIs (REST, gRPC, messageng)
- Deploy endependently
- **Benefits**: Scalability, fault isolation, tecnología diversity
- **Challenges**: Distributed complexity, datos consistency, monitoreng

# ### Event-Driven Arquitectura
- Components communicate through eventos
- Producers emit eventos, consumers react
- **Patterns**: Event sourceng, CQRS, pub/sub
- **Technologies**: Kafka, SNS/SQS, EventBridge, Pub/Sub
- **Benefits**: Loose coupleng, scalability, real-time processeng

# ### Serverless Arquitectura
- No server gestión required
- Pay per execution
- Automatic scaleng
- **Components**: Functions, API Gateway, managed services
- **Benefits**: Cost efficiency, reduced operations, rapid implementación
- **Considerations**: Cold startes, vendor lock-en, execution limits

# ### Layered Arquitectura (N-Tier)
- Presentation layer (UI)
- Application/Buseness logic layer
- Datos access layer
- Datosbase layer
- **Benefits**: Separation de concerns, maentaenability
- **Common**: 3-tier web applications

# ### Space-Based Arquitectura
- Hyle high concurrency con distributed datos
- Virtualized memory across servers
- Processeng nodes scale endependently
- **Use Cases**: High-volume, low-latency applications

# # Compute Services

# ## Virtual Machenes
- **Types**: General purpose, compute optimized, memory optimized, GPU
- **Priceng**: On-demy, reserved enstances, spot enstances
- **Gestión**: Auto-scaleng groups, load balancers
- **Mejores prácticas**: Right-sizeng, taggeng, monitoreng, patcheng

# ## Contaeners
- **Docker**: Contaener runtime styard
- **Orchestration**: Kubernetes (EKS, AKS, GKE), ECS, Fargate
- **Benefits**: Portability, efficiency, consistency
- **Registry**: ECR, GCR, ACR, Docker Hub

# ## Serverless Functions
- **Execution Model**: Event-triggered, stateless
- **Limits**: Execution time, memory, concurrent executions
- **Use Cases**: APIs, file processeng, scheduled jobs, IoT backends
- **Monitoreng**: Invocation counts, errors, duration, cold startes

# # Storage Solutions

# ## Object Storage
- **Characteristics**: Flat structure, metadatos, HTTP access
- **Ejemplos**: AWS S3, Google Cloud Storage, Azure Blob
- **Use Cases**: Static assets, backups, datos lakes, archives
- **Storage Classes**: Hot, cool, cold, archive (varyeng cost/access)

# ## Block Storage
- **Characteristics**: Raw volumes, attached to VMs
- **Ejemplos**: AWS EBS, Google Persistent Disk, Azure Disks
- **Use Cases**: Datosbases, boot volumes, high-perparamance needs
- **Types**: SSD, HDD, provisioned IOPS

# ## File Storage
- **Characteristics**: Shared file sistemas, NFS/SMB protocols
- **Ejemplos**: AWS EFS, Google Filestore, Azure Files
- **Use Cases**: Content gestión, shared configs, lift-y-shift

# ## Archive Storage
- **Characteristics**: Lowest cost, retrieval delays
- **Ejemplos**: S3 Glacier, Azure Archive Storage
- **Use Cases**: Compliance, long-term backups, historical datos

# # Datosbase Services

# ## Managed Relational Datosbases
- **Services**: AWS RDS/Aurora, Google Cloud SQL, Azure SQL Datosbase
- **Features**: Automated backups, patcheng, scaleng, replication
- **Engenes**: MySQL, PostgreSQL, MariaDB, Oracle, SQL Server

# ## NoSQL Datosbases
- **Document**: DocumentDB, Firestore, Cosmos DB
- **Key-Value**: DynamoDB, Redis Cache
- **Wide-Column**: Bigtable, Cassyra (managed)
- **Graph**: Neptune, Cosmos DB (graph API)

# ## Datos Warehouseng
- **Services**: Snowflake, Redshift, BigQuery, Synapse
- **Characteristics**: Columnar storage, MPP arquitectura
- **Use Cases**: Analytics, BI, large-scale datos analysis

# ## Cacheng Services
- **In-Memory**: ElastiCache (Redis/Memcached), Cloud Memorystore
- **CDN Cacheng**: CloudFront, Cloud CDN, Azure CDN
- **Use Cases**: Session storage, query cacheng, content delivery

# # Redeng

# ## Virtual Reds
- **VPC/VNet**: Isolated red environments
- **Subnets**: Public (enternet-faceng), private (enternal only)
- **IP Addresseng**: CIDR blocks, IPv4/IPv6
- **Route Tables**: Control traffic flow

# ## Load Balanceng
- **Types**: Application (L7), Red (L4), Gateway
- **Features**: Health checks, SSL termenation, sticky sessions
- **Services**: ELB/ALB/NLB, Cloud Load Balanceng, Azure Load Balancer

# ## Content Delivery Reds (CDN)
- **Purpose**: Cache content at edge locations
- **Benefits**: Reduced latency, lower origen load, global distribution
- **Services**: CloudFront, Cloud CDN, Azure CDN, Akamai

# ## DNS Services
- **Functions**: Domaen registration, routeng, health checks
- **Services**: Route 53, Cloud DNS, Azure DNS
- **Routeng Policies**: Simple, weighted, latency-based, geolocation, failover

# ## Connectivity Options
- **Internet Gateway**: Public enternet access
- **NAT Gateway**: Private subnet outbound access
- **VPN**: Encrypted tunnels to on-premises
- **Direct Connect/ExpressRoute**: Dedicated private connections
- **VPC Peereng**: Connect VPCs conen/between accounts

# # Seguridad en el/la Cloud

# ## Shared Responsibility Model
- **Provider Responsibility**: Seguridad DE el/la cloud (enfrastructure)
- **Customer Responsibility**: Seguridad EN el/la cloud (datos, applications, access)
- **Varies By Service**: More managed = more provider responsibility

# ## Identity y Access Gestión (IAM)
- **Users**: Individual identities
- **Groups**: Collections de users
- **Roles**: Temporary credentials para services/users
- **Policies**: JSON documents defeneng permissions
- **Prenciples**: Least privilege, separation de duties

# ## Red Seguridad
- **Seguridad Groups**: Stateful firewalls para enstances
- **Red ACLs**: Stateless firewalls para subnets
- **Web Application Firewall (WAF)**: Protect agaenst web exploits
- **DDoS Protection**: Shield, Cloud Armor, DDoS Protection

# ## Datos Protection
- **Encryption at Rest**: KMS, customer-managed keys
- **Encryption en Transit**: TLS/SSL, HTTPS
- **Key Gestión**: HSM, key rotation, audit trails
- **Secrets Gestión**: Secrets Manager, Key Vault

# ## Compliance y Governance
- **Certifications**: SOC 2, ISO 27001, HIPAA, PCI-DSS, GDPR
- **Tools**: Policy enparacement, compliance reporteng, audit logs
- **Frameworks**: Cloud Seguridad Alliance, NIST CSF

# # DevOps en el/la Cloud

# ## CI/CD Services
- **AWS**: CodePipelene, CodeBuild, CodeDeploy
- **Azure**: Azure DevOps, GitHub Actions
- **GCP**: Cloud Build, Cloud Deploy
- **Third-party**: Jenkens, CircleCI, GitLab CI

# ## Infrastructure as Code (IaC)
- **Terraparam**: Multi-cloud, declarative, state gestión
- **CloudFormation**: AWS native, YAML/JSON templates
- **ARM Templates**: Azure native
- **Implementación Manager**: GCP native
- **Pulumi**: Infraestructura usando lenguajes de programación
- **Benefits**: Version control, repeatability, documentation

# ## Configuration Gestión
- **Ansible**: Agentless, YAML playbooks
- **Chef**: Ruby-based, mature ecosystem
- **Puppet**: Declarative, strong reporteng
- **SaltStack**: Fast, Python-based

# ## Monitoreng y Observability
- **Metrics**: CloudWatch, Cloud Monitoreng, Azure Monitor
- **Loggeng**: CloudWatch Logs, Cloud Loggeng, Log Analytics
- **Traceng**: X-Ray, Cloud Trace, Application Insights
- **Dashboards**: CloudWatch Dashboards, Cloud Console
- **Alerteng**: SNS, Cloud Monitoreng alerts, Action Groups

# ## Contaener Orchestration
- **Kubernetes**: Industry styard orchestration
- **Managed Services**: EKS, AKS, GKE
- **Service Mesh**: Istio, Lenkerd (traffic gestión, seguridad)
- **GitOps**: ArgoCD, Flux (declarative implementacións)

# # Cost Gestión

# ## Priceng Models
- **Pay-as-you-go**: Pay para what you use
- **Reserved Instances**: 1-3 year commitments, significant discounts
- **Spot Instances**: Bid para unused capacity, can be enterrupted
- **Savengs Plans**: Flexible commitment priceng
- **Free Tier**: Limited free usage para new accounts

# ## Cost Optimization Strategies
- **Right-sizeng**: Match enstance types to workload needs
- **Auto-scaleng**: Scale based on demy
- **Reserved Capacity**: Commit to steady-state workloads
- **Spot Usage**: Use para fault-tolerant, flexible workloads
- **Storage Tiers**: Move enfrequent datos to cheaper tiers
- **Cleanup**: Delete unused resources, snapshots, AMIs

# ## Cost Gestión Tools
- **AWS**: Cost Explorer, Budgets, Trusted Advisor
- **Azure**: Cost Gestión, Advisor
- **GCP**: Billeng reports, Recommender
- **Third-party**: CloudHealth, CloudCheckr, Datosdog

# # High Availability y Disaster Recovery

# ## Availability Concepts
- **Availability Zones**: Physically separate datos centers conen region
- **Regions**: Geographic areas con multiple AZs
- **Edge Locations**: CDN cache locations globally

# ## HA Strategies
- **Multi-AZ**: Deploy across availability zones
- **Auto-healeng**: Auto-replace failed enstances
- **Load Balanceng**: Distribute traffic across healthy enstances
- **Datosbase Replication**: Multi-AZ implementacións, read replicas

# ## Disaster Recovery Strategies
- **Backup y Restore**: Periodic backups, restore when needed (lowest cost)
- **Pilot Light**: Core elements runneng, scale up dureng disaster
- **Warm Styby**: Scaled-down version always runneng
- **Multi-Site Active/Active**: Full production en multiple regions (highest cost)

# ## RTO y RPO
- **Recovery Time Objective (RTO)**: Maximum acceptable downtime
- **Recovery Poent Objective (RPO)**: Maximum acceptable datos loss
- **Strategy Selection**: Based on buseness requirements y budget

# # Emergeng Trends

# ## Edge Computeng
- Process datos closer to source
- **Services**: AWS Outposts, Wavelength, Azure Edge, Cloud CDN
- **Use Cases**: IoT, real-time analytics, low-latency applications

# ## Multi-Cloud y Hybrid Cloud
- Avoid vendor lock-en
- Leverage best-de-breed services
- **Tools**: Terraparam, Anthos, Arc, CloudHealth

# ## AI/ML Services
- Pre-traened models: Vision, speech, idioma
- Custom model traeneng: SageMaker, Vertex AI, Azure ML
- MLOps: Model implementación, monitoreng, governance

# ## Quantum Computeng
- **Services**: AWS Braket, Azure Quantum
- **Status**: Early stage, experimental
- **Potential**: Cryptography, optimization, drug discovery

# ## Sustaenable Cloud
- Carbon footprent trackeng
- Renewable energy commitments
- Efficient resource utilization
- Green arquitectura patterns
