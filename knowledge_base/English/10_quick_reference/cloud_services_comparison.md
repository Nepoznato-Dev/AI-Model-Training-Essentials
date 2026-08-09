---
# Metadata
title: "Cloud Services Comparison"
description: "AWS vs Azure vs GCP side-by-side comparison"
category: "Quick Reference"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "AI Model Training Team"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.0"
    date: "2026-08-05"
    author: "AI Model Training Team"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-05"
review_date: "2027-02-05"
reviewed_by: "Quick Reference Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [cloud, services, comparison, quick-reference]
difficulty_level: "beginner"
prerequisites: []
estimated_reading_time: "7 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# Cloud Services Comparison

A side-by-side comparison of the three major cloud providers — AWS, Azure, and Google Cloud — across compute, storage, databases, AI/ML, networking, monitoring, and infrastructure-as-code. Useful for architects deciding which platform to use, or mapping services from one cloud to another.

---

## Provider Overview

| | AWS | Azure | Google Cloud (GCP) |
|---|-----|-------|---------------------|
| **Market share** | ~31% (largest) | ~25% (second) | ~11% (third, fastest growing) |
| **Strengths** | Breadth of services; maturity; ecosystem | Enterprise integration; hybrid cloud; Microsoft stack | Data/AI; Kubernetes; global network |
| **Best for** | Startups to enterprises; broadest service catalog | Enterprises with Microsoft/Active Directory; hybrid | Data-intensive workloads; Kubernetes-native; AI/ML |
| **Regions** | 33 regions, 105 AZs | 60+ regions | 40+ regions, 100+ zones |
| **Free tier** | 12 months free tier + always-free | 12 months free + $200 credit | $300 credit for 90 days + always-free |

---

## Compute

| Service Category | AWS | Azure | GCP |
|-----------------|-----|-------|-----|
| **Virtual Machines** | EC2 (Elastic Compute Cloud) | Virtual Machines | Compute Engine |
| **Auto-scaling** | Auto Scaling Groups | Virtual Machine Scale Sets | Instance Groups |
| **Serverless Functions** | Lambda | Azure Functions | Cloud Functions |
| **Container Registry** | ECR (Elastic Container Registry) | Azure Container Registry | Artifact Registry |
| **Container Orchestration** | ECS / EKS | ACS / AKS | GKE / Cloud Run |
| **Serverless Containers** | Fargate | Container Apps | Cloud Run |
| **App Platform (PaaS)** | Elastic Beanstalk, App Runner | App Service | App Engine |
| **Batch Processing** | AWS Batch | Azure Batch | Cloud Batch |
| **GPU / AI Compute** | EC2 (P4d, P5 instances) | NC/ND series VMs | A2/A3 VMs; TPUs |

### VM Pricing Models

| Model | AWS | Azure | GCP |
|-------|-----|-------|-----|
| **On-demand** | On-Demand Instances | Pay-as-you-go | On-demand |
| **Reserved / Committed** | Reserved Instances (1–3 yr) | Reserved VMs (1–3 yr) | Committed use discounts (1–3 yr) |
| **Spot / Interruptible** | Spot Instances | Spot VMs | Preemptible / Spot VMs |
| **Savings plans** | Savings Plans | Savings plans | Committed use discounts |

---

## Storage

| Service Category | AWS | Azure | GCP |
|-----------------|-----|-------|-----|
| **Object Storage** | S3 | Blob Storage | Cloud Storage |
| **Block Storage** | EBS | Managed Disks | Persistent Disk |
| **File Storage** | EFS, FSx | Azure Files | Filestore |
| **Archive / Cold** | S3 Glacier, Deep Archive | Blob Cool/Archive tiers | Cloud Storage Coldline/Archive |
| **Data Transfer** | Snowball, DataSync | Data Box | Transfer Appliance |

### Storage Classes Comparison

| Use Case | AWS S3 | Azure Blob | GCP Cloud Storage |
|----------|--------|------------|-------------------|
| **Frequent access** | S3 Standard | Hot | Standard |
| **Infrequent access** | S3 Standard-IA | Cool | Nearline |
| **Rare access** | S3 One Zone-IA | — | Coldline |
| **Archive** | S3 Glacier / Deep Archive | Archive | Archive |

---

## Databases

| Service Category | AWS | Azure | GCP |
|-----------------|-----|-------|-----|
| **Relational (managed)** | RDS (MySQL, PostgreSQL, Oracle, SQL Server) | Azure Database (MySQL, PostgreSQL); Azure SQL | Cloud SQL (MySQL, PostgreSQL) |
| **Relational (cloud-native)** | Aurora (MySQL/PostgreSQL compatible) | Azure SQL Database (elastic pools) | Cloud Spanner (globally distributed) |
| **NoSQL (document)** | DynamoDB | Cosmos DB (MongoDB API, SQL API) | Firestore; Datastore |
| **NoSQL (wide-column)** | DynamoDB (also) | Cosmos DB (Cassandra API) | Bigtable |
| **NoSQL (key-value)** | DynamoDB, ElastiCache | Azure Cache for Redis | Memorystore (Redis) |
| **Graph** | Neptune | Cosmos DB (Gremlin API) | — |
| **Time-series** | Timestream | Azure Data Explorer | — |
| **Ledger** | QLDB | Azure Confidential Ledger | — |
| **In-memory cache** | ElastiCache (Redis, Memcached) | Azure Cache for Redis | Memorystore |
| **Search** | OpenSearch Service | Azure AI Search | Cloud Search; Vertex AI Search |
| **Data warehouse** | Redshift | Synapse Analytics | BigQuery |

---

## AI and Machine Learning

| Service Category | AWS | Azure | GCP |
|-----------------|-----|-------|-----|
| **ML Platform** | SageMaker | Azure Machine Learning | Vertex AI |
| **Pre-trained APIs** | Rekognition (vision), Polly (TTS), Comprehend (NLP), Transcribe | Cognitive Services (Vision, Speech, Language, Decision) | Vision AI, Speech-to-Text, Natural Language API |
| **LLM / Generative AI** | Bedrock (Claude, Llama, Titan) | Azure OpenAI Service (GPT-4, DALL-E) | Vertex AI (Gemini); Model Garden |
| **Vector / Embeddings** | OpenSearch (k-NN), Bedrock Knowledge Bases | Azure AI Search (vector) | Vertex AI Vector Search, AlloyDB |
| **MLOps** | SageMaker Pipelines, Model Registry | Azure ML Pipelines, Model Registry | Vertex AI Pipelines, Model Registry |
| **Data labelling** | SageMaker Ground Truth | Azure ML Data Labelling | Vertex AI Data Labelling |
| **Conversational AI** | Lex | Azure Bot Service | Dialogflow CX / ES |
| **Translation** | Translate | Translator | Translation API |

---

## Networking

| Service Category | AWS | Azure | GCP |
|-----------------|-----|-------|-----|
| **Virtual Network** | VPC | Virtual Network (VNet) | VPC |
| **Load Balancing** | ELB/ALB/NLB/CLB | Load Balancer (Application, Network, Gateway) | Cloud Load Balancing |
| **DNS** | Route 53 | Azure DNS | Cloud DNS |
| **CDN** | CloudFront | Azure Front Door | Cloud CDN |
| **API Gateway** | API Gateway | API Management | API Gateway |
| **VPN** | Site-to-Site VPN, Client VPN | VPN Gateway | Cloud VPN |
| **Direct Connect / ExpressRoute** | Direct Connect | ExpressRoute | Cloud Interconnect |
| **Private Link** | PrivateLink, VPC Endpoints | Private Link, Private Endpoints | Private Service Connect |
| **Firewall** | WAF, Network Firewall | Azure Firewall, WAF | Cloud Armor, Firewall |
| **DDoS Protection** | Shield Standard / Advanced | DDoS Protection | Cloud Armor |

---

## Monitoring and Logging

| Service Category | AWS | Azure | GCP |
|-----------------|-----|-------|-----|
| **Metrics / Monitoring** | CloudWatch | Azure Monitor | Cloud Monitoring (Stackdriver) |
| **Logging** | CloudWatch Logs | Log Analytics (Azure Monitor Logs) | Cloud Logging |
| **Tracing** | X-Ray | Application Insights | Cloud Trace |
| **Alerting** | CloudWatch Alarms | Azure Monitor Alerts | Cloud Monitoring Alerts |
| **Dashboards** | CloudWatch Dashboards | Azure Workbooks / Dashboards | Cloud Monitoring Dashboards |
| **Error tracking** | CloudWatch Synthetics | Application Insights | Cloud Error Reporting |
| **Third-party** | Datadog, New Relic, PagerDuty | Datadog, New Relic, PagerDuty | Datadog, New Relic, PagerDuty |

---

## Infrastructure as Code and DevOps

| Service Category | AWS | Azure | GCP |
|-----------------|-----|-------|-----|
| **IaC (native)** | CloudFormation | ARM Templates / Bicep | Deployment Manager / Pulumi |
| **IaC (cross-cloud)** | Terraform, Pulumi, CDK | Terraform, Pulumi, Bicep | Terraform, Pulumi |
| **CI/CD** | CodePipeline, CodeBuild | Azure DevOps, GitHub Actions | Cloud Build; Cloud Deploy |
| **Container Registry** | ECR | Azure Container Registry | Artifact Registry |
| **GitOps** | App Mesh + Flux/ArgoCD | Flux/ArgoCD on AKS | Config Sync (Anthos) |
| **Secrets Management** | Secrets Manager, SSM Parameter Store | Key Vault | Secret Manager |

---

## Pricing Considerations

| Factor | AWS | Azure | GCP |
|--------|-----|-------|-----|
| **Billing granularity** | Per-second (after first hour for some) | Per-second | Per-second |
| **Sustained use discounts** | Reserved Instances / Savings Plans | Reserved VMs | Committed use discounts |
| **Spot instances** | Up to 90% off | Up to 90% off | Up to 91% off |
| **Data egress** | Charged (expensive) | Charged | Same price regardless of destination (often cheaper) |
| **Free tier** | 12 months + always-free | 12 months + $200 credit | $300 for 90 days + always-free |
| **Enterprise discounts** | Enterprise Discount Program (EDP) | MACC (Monetary Commitment Contract) | Committed use + CUDs |

---

## When to Use Which

| Scenario | Recommended | Why |
|----------|-------------|-----|
| **Broadest service selection; mature ecosystem** | AWS | Largest catalog; most third-party integrations |
| **Microsoft enterprise; Active Directory; hybrid** | Azure | Native AD integration; strong hybrid tooling |
| **Data warehousing; BigQuery; analytics-heavy** | GCP | BigQuery is best-in-class; seamless data integration |
| **Kubernetes-native development** | GCP | GKE is the most polished managed Kubernetes |
| **Generative AI / LLM applications** | Azure or GCP | Azure OpenAI for GPT models; Vertex AI for Gemini |
| **Global-scale, low-latency applications** | GCP | Google's global network is a genuine advantage |
| **Government / compliance-heavy workloads** | AWS or Azure | Most compliance certifications; GovCloud regions |
| **Cost-sensitive startups** | GCP or AWS | GCP's free tier is generous; AWS has startup credits |
| **Existing Microsoft / .NET stack** | Azure | Tight integration with Visual Studio, .NET, Office 365 |
| **Multi-cloud strategy** | Terraform + all three | Use Terraform to manage resources across clouds |

---

## Summary

All three clouds are capable, reliable, and constantly expanding. The choice usually comes down to: what your team already knows, what your existing contracts look like, and which specific services matter for your workload. Multi-cloud is increasingly common — use Terraform or Pulumi to avoid vendor lock-in at the infrastructure layer, and choose each cloud for what it does best.
