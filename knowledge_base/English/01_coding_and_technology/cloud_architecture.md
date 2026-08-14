<!--
---
# Metadata
title: "Cloud Architecture"
description: "Cloud providers, architecture patterns, security"
category: "Coding and Technology"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "Nepoznato-Dev"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.0"
    date: "2026-08-05"
    author: "Nepoznato-Dev"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-05"
review_date: "2027-02-05"
reviewed_by: "Coding & Technology Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [cloud, architecture, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "11 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Cloud Architecture

Cloud computing has fundamentally changed how organisations build, deploy, and scale software. Instead of buying and maintaining physical servers, you can provision computing resources on demand, pay for what you use, and scale globally in minutes. This file covers the core concepts, architecture patterns, services, and best practices you need to know.

---

## Cloud Computing Fundamentals

### What is Cloud Computing?

On-demand delivery of computing resources — servers, storage, databases, networking, software — over the internet with pay-as-you-go pricing.

### NIST Essential Characteristics

| Characteristic | Meaning |
|---------------|---------|
| **On-Demand Self-Service** | Provision resources without human interaction |
| **Broad Network Access** | Available over the network via standard mechanisms |
| **Resource Pooling** | Multi-tenant model; resources dynamically assigned |
| **Rapid Elasticity** | Scale outward and inward quickly |
| **Measured Service** | Usage is monitored and billed |

### Deployment Models

| Model | Description | When to Use |
|-------|-------------|-------------|
| **Public Cloud** | Owned by providers; shared infrastructure (AWS, Azure, GCP) | Most workloads; cost-effective |
| **Private Cloud** | Dedicated to a single organisation | Regulatory requirements, sensitive data |
| **Hybrid Cloud** | Combination of public and private | Flexibility + compliance |
| **Multi-Cloud** | Using multiple public cloud providers | Avoid vendor lock-in, best-of-breed |

### Service Models

| Model | Provides | Examples | Use Cases |
|-------|----------|----------|-----------|
| **IaaS** | VMs, storage, networks, OS | AWS EC2, Azure VMs, GCP Compute Engine | Lift-and-shift migrations, full control |
| **PaaS** | Development platforms, databases, middleware | Heroku, Google App Engine, AWS Elastic Beanstalk | App development, API deployment |
| **SaaS** | Complete applications over the internet | Salesforce, Google Workspace, Microsoft 365 | Email, CRM, collaboration |
| **FaaS / Serverless** | Event-driven function execution | AWS Lambda, Azure Functions, GCP Cloud Functions | APIs, event processing, scheduled tasks |

---

## Major Cloud Providers

| Provider | Market Share | Strengths |
|----------|-------------|-----------|
| **AWS** | ~32% | Broadest service catalog, largest ecosystem |
| **Azure** | ~23% | Enterprise integration, hybrid cloud, Microsoft stack |
| **GCP** | ~10% | Data analytics, AI/ML, Kubernetes |
| **Alibaba Cloud** | ~4% | Dominant in Asia-Pacific |
| **Oracle Cloud** | ~2% | Database workloads, enterprise apps |
| **IBM Cloud** | ~2% | Enterprise focus, Watson AI |
| **DigitalOcean** | Niche | Developer-friendly, simplified offerings |

### Service Comparison (Top 3 Providers)

| Category | AWS | Azure | GCP |
|----------|-----|-------|-----|
| **Compute** | EC2, Lambda, ECS | VMs, Functions, AKS | Compute Engine, Cloud Functions, GKE |
| **Storage** | S3, EBS, Glacier | Blob Storage, Disk Storage | Cloud Storage, Persistent Disk |
| **Database** | RDS, DynamoDB, Aurora | SQL Database, Cosmos DB | Cloud SQL, Firestore, Bigtable |
| **Analytics** | Redshift, EMR | Synapse, Databricks | BigQuery, Dataflow |
| **AI/ML** | SageMaker, Rekognition | Azure ML, Cognitive Services | Vertex AI, AutoML |
| **Networking** | VPC, Route 53, CloudFront | VNet, Traffic Manager | VPC, Cloud DNS, Cloud CDN |

---

## Architecture Patterns

### Well-Architected Framework

All three major providers publish well-architected frameworks built around five pillars:

| Pillar | Key Principles |
|--------|---------------|
| **Operational Excellence** | Automate operations; make frequent, reversible changes; anticipate failure |
| **Security** | Strong identity foundation; apply security at every layer; protect data in transit and at rest |
| **Reliability** | Test recovery procedures; auto-recover from failure; scale horizontally |
| **Performance Efficiency** | Use serverless; go global in minutes; experiment often |
| **Cost Optimization** | Adopt consumption model; use managed services; stop spending on undifferentiated work |

### Common Patterns

| Pattern | Description | Benefits | Challenges |
|---------|-------------|----------|------------|
| **Microservices** | Decompose app into small, independent services | Scalability, fault isolation, independent deployment | Distributed complexity, data consistency |
| **Event-Driven** | Components communicate through events | Loose coupling, real-time processing | Debugging complexity, eventual consistency |
| **Serverless** | No server management; pay per execution | Cost efficiency, rapid deployment | Cold starts, vendor lock-in, execution limits |
| **Layered (N-Tier)** | Presentation → Business logic → Data access → Database | Separation of concerns, maintainability | Can become monolithic |
| **Space-Based** | Distributed data across virtualised memory nodes | Handles high concurrency, low latency | Complex to design and manage |

---

## Core Services

### Compute

| Service Type | Details |
|-------------|---------|
| **Virtual Machines** | General purpose, compute-optimised, memory-optimised, GPU. Pricing: on-demand, reserved, spot. |
| **Containers** | Docker runtime; orchestration via Kubernetes (EKS, AKS, GKE). Registries: ECR, GCR, ACR. |
| **Serverless Functions** | Event-triggered, stateless. Limits on execution time, memory, concurrency. |

### Storage

| Type | Characteristics | Examples | Best For |
|------|----------------|----------|----------|
| **Object** | Flat structure, HTTP access, metadata-rich | S3, Cloud Storage, Azure Blob | Static assets, backups, data lakes |
| **Block** | Raw volumes attached to VMs | EBS, Persistent Disk, Azure Disks | Databases, boot volumes |
| **File** | Shared file systems (NFS/SMB) | EFS, Filestore, Azure Files | Content management, shared configs |
| **Archive** | Lowest cost, retrieval delays | S3 Glacier, Azure Archive | Compliance, long-term backups |

### Databases

| Category | Services | Use Case |
|----------|----------|----------|
| **Managed Relational** | RDS, Cloud SQL, Azure SQL | Traditional apps, ACID transactions |
| **NoSQL — Document** | DocumentDB, Firestore, Cosmos DB | Flexible schemas, JSON data |
| **NoSQL — Key-Value** | DynamoDB, Redis Cache | Caching, sessions, simple lookups |
| **NoSQL — Wide-Column** | Bigtable, Cassandra | Write-heavy, time series |
| **NoSQL — Graph** | Neptune, Cosmos DB (Graph API) | Relationships, social networks |
| **Data Warehousing** | Snowflake, Redshift, BigQuery, Synapse | Analytics, BI |
| **Caching** | ElastiCache, Cloud Memorystore | Session storage, query caching |

---

## Networking

### Virtual Networks

Every cloud deployment lives inside a Virtual Private Cloud (VPC / VNet) — an isolated network you define with CIDR blocks, subnets (public or private), route tables, and gateways.

### Load Balancing and CDN

| Service | Purpose |
|---------|---------|
| **Load Balancers** | Distribute traffic across instances (L4 network, L7 application) |
| **CDN** | Cache content at edge locations for lower latency (CloudFront, Cloud CDN, Azure CDN) |
| **DNS** | Domain registration, routing policies, health checks (Route 53, Cloud DNS, Azure DNS) |

### Connectivity Options

| Option | Description |
|--------|-------------|
| **Internet Gateway** | Public internet access for VPC |
| **NAT Gateway** | Private subnet outbound access |
| **VPN** | Encrypted tunnels to on-premises |
| **Direct Connect / ExpressRoute** | Dedicated private connections |
| **VPC Peering** | Connect VPCs within or between accounts |

---

## Security

### Shared Responsibility Model

| Layer | Provider | Customer |
|-------|----------|----------|
| **Infrastructure** (hardware, facilities) | ✅ | |
| **Compute, Storage, Networking** | ✅ (managed) | ✅ (self-managed) |
| **Data, Applications, Identity** | | ✅ |

The more managed the service, the more the provider handles. With IaaS you manage almost everything; with SaaS, the provider handles nearly all of it.

### Identity and Access Management (IAM)

| Concept | Description |
|---------|-------------|
| **Users** | Individual identities |
| **Groups** | Collections of users |
| **Roles** | Temporary credentials for services or users |
| **Policies** | Documents defining permissions |
| **Principle** | Least privilege, separation of duties |

### Data Protection

- **Encryption at rest**: KMS, customer-managed keys, HSM.
- **Encryption in transit**: TLS/SSL, HTTPS.
- **Secrets management**: Secrets Manager, Key Vault — never hardcode secrets.

---

## DevOps in the Cloud

### Infrastructure as Code (IaC)

| Tool | Description |
|------|-------------|
| **Terraform** | Multi-cloud, declarative HCL, state management |
| **CloudFormation** | AWS-native, YAML/JSON templates |
| **ARM Templates / Bicep** | Azure-native |
| **Pulumi** | Infrastructure using programming languages (Python, Go, etc.) |

### CI/CD Services

| Provider | Tools |
|----------|-------|
| **AWS** | CodePipeline, CodeBuild, CodeDeploy |
| **Azure** | Azure DevOps, GitHub Actions |
| **GCP** | Cloud Build, Cloud Deploy |
| **Third-party** | Jenkins, CircleCI, GitLab CI |

### Monitoring and Observability

| Capability | AWS | Azure | GCP |
|-----------|-----|-------|-----|
| **Metrics** | CloudWatch | Azure Monitor | Cloud Monitoring |
| **Logging** | CloudWatch Logs | Log Analytics | Cloud Logging |
| **Tracing** | X-Ray | Application Insights | Cloud Trace |

---

## Cost Management

### Pricing Models

| Model | Description | Best For |
|-------|-------------|----------|
| **On-Demand** | Pay for what you use, by the second/hour | Variable, short-term workloads |
| **Reserved Instances** | 1–3 year commitment, significant discount | Steady-state workloads |
| **Spot Instances** | Bid for unused capacity; can be interrupted | Fault-tolerant, flexible jobs |
| **Savings Plans** | Flexible commitment pricing | Mixed usage patterns |
| **Free Tier** | Limited free usage for new accounts | Learning, prototyping |

### Optimization Strategies

Right-size instances to match workloads. Use auto-scaling to handle demand spikes. Reserve capacity for predictable loads. Use spot instances for batch jobs. Move infrequently accessed data to cheaper storage tiers. Delete unused resources (orphaned snapshots, idle load balancers, unattached IPs).

---

## High Availability and Disaster Recovery

### Availability Concepts

| Concept | Description |
|---------|-------------|
| **Availability Zone (AZ)** | Physically separate data centres within a region |
| **Region** | Geographic area with multiple AZs |
| **Edge Location** | CDN cache location for content delivery |

### Disaster Recovery Strategies

| Strategy | Cost | RTO | RPO | Description |
|----------|------|-----|-----|-------------|
| **Backup and Restore** | Lowest | Hours | Hours–days | Periodic backups, restore when needed |
| **Pilot Light** | Low | Minutes–hours | Minutes | Core elements always running, scale up on disaster |
| **Warm Standby** | Medium | Minutes | Seconds–minutes | Scaled-down version always running |
| **Multi-Site Active/Active** | Highest | Near-zero | Zero | Full production in multiple regions |

**RTO** (Recovery Time Objective) = maximum acceptable downtime. **RPO** (Recovery Point Objective) = maximum acceptable data loss.

---

## Emerging Trends

| Trend | What's Happening |
|-------|-----------------|
| **Edge Computing** | Processing data closer to the source (AWS Outposts, Wavelength, Azure Edge) |
| **Multi-Cloud** | Avoiding vendor lock-in; leveraging best-of-breed across providers |
| **AI/ML Services** | Pre-trained models (vision, speech, language) + custom training (SageMaker, Vertex AI) |
| **Quantum Computing** | Early-stage experimental services (AWS Braket, Azure Quantum) |
| **Sustainable Cloud** | Carbon footprint tracking, renewable energy commitments, green architecture |
