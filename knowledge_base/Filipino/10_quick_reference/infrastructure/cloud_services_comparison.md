<!--
---
# Metadata
title: "Cloud Services Comparison"
description: "AWS vs Azure vs GCP side-by-side comparison"
category: "Quick Reference"
subcategory: "Infrastructure"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "Nepoznato-Dev"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.1"
    date: "2026-08-09"
    author: "Nepoznato-Dev"
    changes: "Moved to infrastructure/ subfolder; added subcategory field"
  - version: "1.0.0"
    date: "2026-08-05"
    author: "Nepoznato-Dev"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-09"
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

-->
# Paghahambing ng Mga Serbisyo sa Cloud
Isang magkatabing paghahambing ng tatlong pangunahing tagapagbigay ng cloud — AWS, Azure, at Google Cloud — sa kabuuan ng compute, storage, database, AI/ML, networking, monitoring, at infrastructure-as-code. Kapaki-pakinabang para sa mga arkitekto na nagpapasya kung aling platform ang gagamitin, o mga serbisyo sa pagmamapa mula sa isang ulap patungo sa isa pa.
---

## Pangkalahatang-ideya ng Provider
| | AWS | Azure | Google Cloud (GCP) |
|---|-----|-------|---------------------|
| **Market share** | ~31% (pinakamalaking) | ~25% (segundo) | ~11% (pangatlo, pinakamabilis na paglaki) |
| **Lakas** | Lawak ng mga serbisyo; kapanahunan; ecosystem | Pagsasama ng negosyo; hybrid na ulap; Microsoft stack | Data/AI; Kubernetes; pandaigdigang network |
| **Pinakamahusay para sa** | Mga startup sa mga negosyo; pinakamalawak na katalogo ng serbisyo | Mga negosyong may Microsoft/Active Directory; hybrid | Data-intensive workloads; Kubernetes-native; AI/ML |
| **Mga Rehiyon** | 33 rehiyon, 105 AZ | 60+ na rehiyon | 40+ rehiyon, 100+ zone |
| **Libreng tier** | 12 buwang libreng tier + palaging libre | 12 buwang libre + $200 na kredito | $300 na credit para sa 90 araw + palaging libre |
---

## Mag-compute
| Kategorya ng Serbisyo | AWS | Azure | GCP |
|-----------------|-----|-------|-----|
| **Mga Virtual Machine** | EC2 (Elastic Compute Cloud) | Mga Virtual Machine | Compute Engine |
| **Auto-scaling** | Auto Scaling Groups | Mga Virtual Machine Scale Sets | Mga Pangkat ng Instance |
| **Serverless Function** | Lambda | Azure Function | Mga Pag-andar ng Cloud |
| **Registry ng Container** | ECR (Elastic Container Registry) | Azure Container Registry | Artifact Registry |
| **Orkestrasyon ng Lalagyan** | ECS / EKS | ACS / AKS | GKE / Cloud Run |
| **Mga Lalagyan na Walang Server** | Fargate | Container Apps | Cloud Run |
| **App Platform (PaaS)** | Elastic Beanstalk, App Runner | Serbisyo ng App | App Engine |
| **Batch Processing** | AWS Batch | Azure Batch | Cloud Batch |
| **GPU / AI Compute** | EC2 (P4d, P5 instance) | Mga VM na serye ng NC/ND | Mga A2/A3 VM; Mga TPU |
### Mga Modelo ng Pagpepresyo ng VM
| Modelo | AWS | Azure | GCP |
|-------|-----|-------|-----|
| **On-demand** | On-Demand na Mga Instance | Pay-as-you-go | On-demand |
| **Reserved / Committed** | Mga Reserved Instance (1–3 yr) | Mga Nakareserbang VM (1–3 taon) | Mga diskuwento sa nakatuong paggamit (1–3 taon) |
| **Spot / Interruptible** | Spot Instances | Spot VMs | Mga Preemptible / Spot VM |
| **Mga plano sa pagtitipid** | Mga Plano sa Pagtitipid | Mga plano sa pagtitipid | Mga diskuwento sa nakatuong paggamit |
---

## Imbakan
| Kategorya ng Serbisyo | AWS | Azure | GCP |
|-----------------|-----|-------|-----|
| **Imbakan ng Bagay** | S3 | Blob Storage | Cloud Storage |
| **I-block ang Storage** | EBS | Mga Pinamamahalaang Disk | Persistent Disk |
| **Imbakan ng File** | EFS, FSx | Azure Files | Filestore |
| **Archive / Malamig** | S3 Glacier, Deep Archive | Blob Cool/Archive tier | Cloud Storage Coldline/Archive |
| **Paglipat ng Data** | Snowball, DataSync | Kahon ng Data | Transfer Appliance |
### Paghahambing ng Mga Klase ng Storage
| Use Case | AWS S3 | Azure Blob | GCP Cloud Storage |
|----------|--------|------------|-------------------|
| **Madalas na pag-access** | S3 Standard | Mainit | Pamantayan |
| **Madalang na pag-access** | S3 Standard-IA | Cool | Nearline |
| **Bihirang access** | S3 One Zone-IA | — | Coldline |
| **Archive** | S3 Glacier / Deep Archive | I-archive | I-archive |
---

## Mga database
| Kategorya ng Serbisyo | AWS | Azure | GCP |
|-----------------|-----|-------|-----|
| **Relational (pinamamahalaan)** | RDS (MySQL, PostgreSQL, Oracle, SQL Server) | Azure Database (MySQL, PostgreSQL); Azure SQL | Cloud SQL (MySQL, PostgreSQL) |
| **Relational (cloud-native)** | Aurora (MySQL/PostgreSQL compatible) | Azure SQL Database (mga nababanat na pool) | Cloud Spanner (naipamahagi sa buong mundo) |
| **NoSQL (dokumento)** | DynamoDB | Cosmos DB (MongoDB API, SQL API) | Firestore; Datastore |
| **NoSQL (wide-column)** | DynamoDB (din) | Cosmos DB (Cassandra API) | Bigtable |
| **NoSQL (key-value)** | DynamoDB, ElastiCache | Azure Cache para sa Redis | Memorystore (Redis) |
| **Graph** | Neptune | Cosmos DB (Gremlin API) | — |
| **Time-serye** | Timestream | Azure Data Explorer | — |
| **Ledger** | QLDB | Azure Confidential Ledger | — |
| **In-memory cache** | ElastiCache (Redis, Memcached) | Azure Cache para sa Redis | Memorystore |
| **Paghahanap** | Serbisyo ng OpenSearch | Azure AI Search | Cloud Search; Paghahanap ng Vertex AI |
| **Data warehouse** | Redshift | Synapse Analytics | BigQuery |
---

## AI at Machine Learning
| Kategorya ng Serbisyo | AWS | Azure | GCP |
|-----------------|-----|-------|-----|
| **ML Platform** | SageMaker | Azure Machine Learning | Vertex AI |
| **Mga Pre-trained na API** | Recognition (vision), Polly (TTS), Comprehend (NLP), Transcribe | Mga Serbisyong nagbibigay-malay (Vision, Pagsasalita, Wika, Desisyon) | Vision AI, Speech-to-Text, Natural Language API |
| **LLM / Generative AI** | Bedrock (Claude, Llama, Titan) | Serbisyo ng Azure OpenAI (GPT-4, DALL-E) | Vertex AI (Gemini); Modelong Hardin |
| **Vector / Mga Pag-embed** | OpenSearch (k-NN), Bedrock Knowledge Bases | Azure AI Search (vector) | Vertex AI Vector Search, AlloyDB |
| **MLOps** | Mga Pipeline ng SageMaker, Registry ng Modelo | Azure ML Pipelines, Registry ng Modelo | Vertex AI Pipelines, Registry ng Modelo |
| **Pag-label ng data** | SageMaker Ground Truth | Azure ML Data Labeling | Pag-label ng Data ng Vertex AI |
| **Pag-uusap AI** | Lex | Serbisyo ng Azure Bot | Dialogflow CX / ES |
| **Pagsasalin** | Isalin | Tagasalin | Translation API |
---

## Networking
| Kategorya ng Serbisyo | AWS | Azure | GCP |
|-----------------|-----|-------|-----|
| **Virtual Network** | VPC | Virtual Network (VNet) | VPC |
| **Pagbabalanse ng Pag-load** | ELB/ALB/NLB/CLB | Load Balancer (Application, Network, Gateway) | Cloud Load Balancing |
| **DNS** | Ruta 53 | Azure DNS | Cloud DNS |
| **CDN** | CloudFront | Azure Front Door | Cloud CDN |
| **API Gateway** | API Gateway | Pamamahala ng API | API Gateway |
| **VPN** | Site-to-Site VPN, Client VPN | VPN Gateway | Cloud VPN |
| **Direktang Kumonekta / ExpressRoute** | Direktang Kumonekta | ExpressRoute | Cloud Interconnect |
| **Pribadong Link** | PrivateLink, Mga Endpoint ng VPC | Pribadong Link, Mga Pribadong Endpoint | Pribadong Serbisyo Connect |
| **Firewall** | WAF, Network Firewall | Azure Firewall, WAF | Cloud Armor, Firewall |
| **Proteksyon ng DDoS** | Shield Standard / Advanced | Proteksyon ng DDoS | Cloud Armor |
---

## Pagsubaybay at Pag-log
| Kategorya ng Serbisyo | AWS | Azure | GCP |
|-----------------|-----|-------|-----|
| **Mga Sukatan / Pagsubaybay** | CloudWatch | Azure Monitor | Cloud Monitoring (Stackdriver) |
| **Pag-log** | Mga Log ng CloudWatch | Log Analytics (Mga Log ng Azure Monitor) | Cloud Logging |
| **Pagsubaybay** | X-Ray | Mga Insight sa Application | Cloud Trace |
| **Nag-aalerto** | Mga Alarm ng CloudWatch | Mga Alerto ng Azure Monitor | Mga Alerto sa Pagsubaybay sa Cloud |
| **Mga Dashboard** | Mga Dashboard ng CloudWatch | Mga Azure Workbook / Dashboard | Mga Dashboard ng Cloud Monitoring |
| **Error sa pagsubaybay** | CloudWatch Synthetics | Mga Insight sa Application | Pag-uulat ng Cloud Error |
| **Third-party** | Datadog, Bagong Relic, PagerDuty | Datadog, Bagong Relic, PagerDuty | Datadog, Bagong Relic, PagerDuty |
---

## Imprastraktura bilang Code at DevOps
| Kategorya ng Serbisyo | AWS | Azure | GCP |
|-----------------|-----|-------|-----|
| **IaC (katutubo)** | CloudFormation | Mga Template ng ARM / Bicep | Deployment Manager / Pulumi |
| **IaC (cross-cloud)** | Terraform, Pulumi, CDK | Terraform, Pulumi, Bicep | Terraform, Pulumi |
| **CI/CD** | CodePipeline, CodeBuild | Azure DevOps, GitHub Actions | Cloud Build; Cloud Deploy |
| **Registry ng Container** | ECR | Azure Container Registry | Artifact Registry |
| **GitOps** | App Mesh + Flux/ArgoCD | Flux/ArgoCD sa AKS | Config Sync (Anthos) |
| **Pamamahala ng Mga Lihim** | Secrets Manager, SSM Parameter Store | Key Vault | Lihim na Tagapamahala |
---

## Mga Pagsasaalang-alang sa Pagpepresyo
| Salik | AWS | Azure | GCP |
|--------|-----|-------|-----|
| **Granility ng pagsingil** | Bawat segundo (pagkatapos ng unang oras para sa ilan) | Bawat segundo | Bawat segundo |
| **Mga diskwento sa patuloy na paggamit** | Mga Reserved Instances / Savings Plan | Mga Nakareserbang VM | Mga diskuwento sa nakatuong paggamit |
| **Spot instance** | Hanggang 90% diskwento | Hanggang 90% diskwento | Hanggang 91% diskwento |
| **Paglabas ng data** | Siningil (mahal) | Siningil | Parehong presyo anuman ang destinasyon (kadalasang mas mura) |
| **Libreng tier** | 12 buwan + palaging libre | 12 buwan + $200 na kredito | $300 para sa 90 araw + palaging libre |
| **Mga diskwento sa negosyo** | Enterprise Discount Program (EDP) | MACC (Monetary Commitment Contract) | Nakatalagang paggamit + CUDs |
---

## Kailan Gamitin ang Alin
| Sitwasyon | Inirerekomenda | Bakit |
|----------|-------------|-----|
| **Pinakamalawak na pagpili ng serbisyo; mature na ecosystem** | AWS | Pinakamalaking katalogo; karamihan sa mga pagsasama ng third-party |
| **Microsoft enterprise; Aktibong Direktoryo; hybrid** | Azure | Pagsasama ng katutubong AD; malakas na hybrid tooling |
| **Data warehousing; BigQuery; analytics-heavy** | GCP | Pinakamahusay sa klase ang BigQuery; tuluy-tuloy na pagsasama ng data |
| **Kubernetes-katutubong pag-unlad** | GCP | Ang GKE ay ang pinakapinong pinamamahalaang Kubernetes |
| **Mga Generative AI / LLM application** | Azure o GCP | Azure OpenAI para sa mga modelo ng GPT; Vertex AI para sa Gemini |
| **Global-scale, low-latency na mga application** | GCP | Ang pandaigdigang network ng Google ay isang tunay na kalamangan |
| **Mga workload ng gobyerno / mabibigat sa pagsunod** | AWS o Azure | Karamihan sa mga sertipikasyon sa pagsunod; Mga rehiyon ng GovCloud |
| **Mga startup na sensitibo sa gastos** | GCP o AWS | Ang libreng tier ng GCP ay mapagbigay; Ang AWS ay may mga kredito sa pagsisimula |
| **Umiiral na Microsoft / .NET stack** | Azure | Mahigpit na pagsasama sa Visual Studio, .NET, Office 365 |
| **Multi-cloud na diskarte** | Terraform + lahat ng tatlo | Gamitin ang Terraform upang pamahalaan ang mga mapagkukunan sa mga ulap |
---

## Buod
Lahat ng tatlong ulap ay may kakayahan, maaasahan, at patuloy na lumalawak. Ang pagpili ay karaniwang napupunta sa: kung ano ang alam na ng iyong team, kung ano ang hitsura ng iyong mga kasalukuyang kontrata, at kung aling mga partikular na serbisyo ang mahalaga para sa iyong workload. Lalong nagiging karaniwan ang multi-cloud — gumamit ng Terraform o Pulumi upang maiwasan ang pag-lock-in ng vendor sa layer ng imprastraktura, at piliin ang bawat cloud para sa kung ano ang pinakamahusay na ginagawa nito.