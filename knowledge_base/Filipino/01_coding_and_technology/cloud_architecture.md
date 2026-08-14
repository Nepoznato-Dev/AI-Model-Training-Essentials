---
# Metadata
title: "Cloud Architecture"
description: "Cloud providers, architecture patterns, security"
category: "Coding and Technology"
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

# Cloud Architecture
Ang cloud computing ay pangunahing nagbago kung paano bumuo, mag-deploy, at mag-scale ng software ang mga organisasyon. Sa halip na bumili at magpanatili ng mga pisikal na server, maaari kang magbigay ng mga mapagkukunan ng computing kapag hinihiling, magbayad para sa iyong ginagamit, at mag-scale sa buong mundo sa ilang minuto. Sinasaklaw ng file na ito ang mga pangunahing konsepto, pattern ng arkitektura, serbisyo, at pinakamahuhusay na kagawian na kailangan mong malaman.
---

## Cloud Computing Fundamentals
### Ano ang Cloud Computing?
On-demand na paghahatid ng mga mapagkukunan ng computing — mga server, storage, database, networking, software — sa internet na may pay-as-you-go na pagpepresyo.
### Mahahalagang Katangian ng NIST
| Katangian | Ibig sabihin |
|--------------|---------|
| **On-Demand na Self-Service** | Magbigay ng mga mapagkukunan nang walang pakikipag-ugnayan ng tao |
| **Malawak na Access sa Network** | Magagamit sa network sa pamamagitan ng mga karaniwang mekanismo |
| **Resource Pooling** | Multi-nangungupahan modelo; dynamic na itinalaga ang mga mapagkukunan |
| **Mabilis na Pagkalastiko** | Mag-scale palabas at papasok nang mabilis |
| **Sinukat na Serbisyo** | Ang paggamit ay sinusubaybayan at sinisingil |
### Mga Deployment na Modelo
| Modelo | Paglalarawan | Kailan Gagamitin |
|-------|-------------|-------------|
| **Public Cloud** | Pag-aari ng mga provider; nakabahaging imprastraktura (AWS, Azure, GCP) | Karamihan sa mga workload; cost-effective na |
| **Pribadong Ulap** | Nakatuon sa iisang organisasyon | Mga kinakailangan sa regulasyon, sensitibong data |
| **Hybrid Cloud** | Kumbinasyon ng pampubliko at pribado | Kakayahang umangkop + pagsunod |
| **Multi-Cloud** | Paggamit ng maramihang mga pampublikong tagapagbigay ng ulap | Iwasan ang vendor lock-in, best-of-breed |
### Mga Modelo ng Serbisyo
| Modelo | Nagbibigay ng | Mga halimbawa | Use Cases |
|-------|----------|----------|-----------|
| **IaaS** | Mga VM, storage, network, OS | AWS EC2, Azure VMs, GCP Compute Engine | Lift-and-shift migration, ganap na kontrol |
| **PaaS** | Mga platform ng pag-unlad, mga database, middleware | Heroku, Google App Engine, AWS Elastic Beanstalk | Pag-develop ng app, pag-deploy ng API |
| **SaaS** | Kumpletuhin ang mga application sa internet | Salesforce, Google Workspace, Microsoft 365 | Email, CRM, pakikipagtulungan |
| **FaaS / Walang Server** | Pagpapatupad ng function na hinimok ng kaganapan | AWS Lambda, Azure Functions, GCP Cloud Functions | Mga API, pagproseso ng kaganapan, mga naka-iskedyul na gawain |
---

## Pangunahing Cloud Provider
| Provider | Bahagi ng Market | Mga Lakas |
|----------|-------------|-----------|
| **AWS** | ~32% | Pinakamalawak na katalogo ng serbisyo, pinakamalaking ecosystem |
| **Azure** | ~23% | Pagsasama ng enterprise, hybrid cloud, Microsoft stack |
| **GCP** | ~10% | Data analytics, AI/ML, Kubernetes |
| **Alibaba Cloud** | ~4% | Dominant sa Asia-Pacific |
| **Oracle Cloud** | ~2% | Mga workload sa database, mga enterprise app |
| **IBM Cloud** | ~2% | Pokus ng negosyo, Watson AI |
| **DigitalOcean** | Niche | Developer-friendly, pinasimpleng mga alok |
### Paghahambing ng Serbisyo (Nangungunang 3 Provider)
| Kategorya | AWS | Azure | GCP |
|----------|-----|-------|-----|
| **Compute** | EC2, Lambda, ECS | Mga VM, Function, AKS | Compute Engine, Cloud Functions, GKE |
| **Imbakan** | S3, EBS, Glacier | Blob Storage, Disk Storage | Cloud Storage, Persistent Disk |
| **Database** | RDS, DynamoDB, Aurora | SQL Database, Cosmos DB | Cloud SQL, Firestore, Bigtable |
| **Analytics** | Redshift, EMR | Synapse, Databricks | BigQuery, Dataflow |
| **AI/ML** | SageMaker, Recognition | Azure ML, Cognitive Services | Vertex AI, AutoML |
| **Networking** | VPC, Ruta 53, CloudFront | VNet, Tagapamahala ng Trapiko | VPC, Cloud DNS, Cloud CDN |
---

## Mga Pattern ng Arkitektura
### Well-Architected Framework
Ang lahat ng tatlong pangunahing provider ay nag-publish ng mahusay na arkitekto na mga framework na binuo sa paligid ng limang haligi:
| Haligi | Mga Pangunahing Prinsipyo |
|--------|--------------|
| **Kahusayan sa Operasyon** | I-automate ang mga operasyon; gumawa ng madalas, nababaligtad na mga pagbabago; asahan ang kabiguan |
| **Seguridad** | Matibay na pundasyon ng pagkakakilanlan; ilapat ang seguridad sa bawat layer; protektahan ang data sa pagbibiyahe at sa pahinga |
| **Pagiging Maaasahan** | Mga pamamaraan ng pagbawi ng pagsubok; auto-recover mula sa pagkabigo; pahalang na sukat |
| **Kahusayan ng Pagganap** | Gumamit ng walang server; maging global sa ilang minuto; madalas mag-eksperimento |
| **Cost Optimization** | Magpatibay ng modelo ng pagkonsumo; gumamit ng mga pinamamahalaang serbisyo; itigil ang paggastos sa walang pagkakaibang trabaho |
### Mga Karaniwang Pattern
| Pattern | Paglalarawan | Mga Benepisyo | Mga Hamon |
|---------|-------------|----------|------------|
| **Microservices** | I-decompose ang app sa maliit, independiyenteng mga serbisyo | Scalability, fault isolation, independent deployment | Naipamahagi na pagiging kumplikado, pagkakapare-pareho ng data |
| **Batay sa Kaganapan** | Ang mga bahagi ay nakikipag-usap sa pamamagitan ng mga kaganapan | Maluwag na pagkabit, real-time na pagproseso | Pagiging kumplikado sa pag-debug, pagkakapare-pareho sa huli |
| **Walang Server** | Walang pamamahala ng server; pay per execution | Episyente sa gastos, mabilis na pag-deploy | Malamig na pagsisimula, vendor lock-in, mga limitasyon sa pagpapatupad |
| **Layered (N-Tier)** | Presentasyon → Logic ng negosyo → Data access → Database | Paghihiwalay ng mga alalahanin, pagpapanatili | Maaaring maging monolitik |
| **Batay sa Space** | Ibinahagi ang data sa mga virtualised memory node | Hinahawakan ang mataas na concurrency, mababang latency | Kumplikado sa disenyo at pamamahala |
---

## Mga Pangunahing Serbisyo
### Mag-compute
| Uri ng Serbisyo | Mga Detalye |
|-------------|---------|
| **Mga Virtual Machine** | Pangkalahatang layunin, compute-optimized, memory-optimized, GPU. Pagpepresyo: on-demand, nakalaan, lugar. |
| **Mga lalagyan** | Docker runtime; orkestra sa pamamagitan ng Kubernetes (EKS, AKS, GKE). Mga Rehistro: ECR, GCR, ACR. |
| **Serverless Function** | Na-trigger ng kaganapan, walang estado. Mga limitasyon sa oras ng pagpapatupad, memorya, kasabay. |
### Imbakan
| Uri | Mga Katangian | Mga halimbawa | Pinakamahusay Para sa |
|------|----------------|----------|----------|
| **Bagay** | Flat structure, HTTP access, metadata-rich | S3, Cloud Storage, Azure Blob | Mga static na asset, backup, data lakes |
| **Harangan** | Mga raw volume na naka-attach sa mga VM | EBS, Persistent Disk, Azure Disks | Mga database, dami ng boot |
| **File** | Mga shared file system (NFS/SMB) | EFS, Filestore, Azure Files | Pamamahala ng nilalaman, mga nakabahaging config |
| **Archive** | Pinakamababang gastos, mga pagkaantala sa pagkuha | S3 Glacier, Azure Archive | Pagsunod, pangmatagalang backup |
### Mga database
| Kategorya | Mga Serbisyo | Use Case |
|----------|----------|----------|
| **Pinamamahalaang Relasyonal** | RDS, Cloud SQL, Azure SQL | Mga tradisyunal na app, mga transaksyon sa ACID |
| **NoSQL — Dokumento** | DocumentDB, Firestore, Cosmos DB | Mga flexible na schema, data ng JSON |
| **NoSQL — Key-Value** | DynamoDB, Redis Cache | Caching, session, simpleng paghahanap |
| **NoSQL — Wide-Column** | Bigtable, Cassandra | Sumulat-mabigat, serye ng oras |
| **NoSQL — Graph** | Neptune, Cosmos DB (Graph API) | Mga relasyon, mga social network |
| **Data Warehousing** | Snowflake, Redshift, BigQuery, Synapse | Analytics, BI |
| **Pag-cache** | ElasticCache, Cloud Memorystore | Imbakan ng session, pag-cache ng query |
---

## Networking
### Mga Virtual Network
Ang bawat cloud deployment ay nabubuhay sa loob ng isang Virtual Private Cloud (VPC / VNet) — isang nakahiwalay na network na iyong tinukoy sa mga bloke ng CIDR, subnet (pampubliko o pribado), mga talahanayan ng ruta, at mga gateway.
### Load Balancing at CDN
| Serbisyo | Layunin |
|---------|---------|
| **Load Balancers** | Ipamahagi ang trapiko sa mga pagkakataon (L4 network, L7 application) |
| **CDN** | Cache na nilalaman sa mga gilid na lokasyon para sa mas mababang latency (CloudFront, Cloud CDN, Azure CDN) |
| **DNS** | Pagpaparehistro ng domain, mga patakaran sa pagruruta, mga pagsusuri sa kalusugan (Route 53, Cloud DNS, Azure DNS) |
### Mga Opsyon sa Pagkakakonekta
| Pagpipilian | Paglalarawan |
|--------|--------------|
| **Internet Gateway** | Pampublikong internet access para sa VPC |
| **NAT Gateway** | Pribadong subnet outbound na access |
| **VPN** | Mga naka-encrypt na tunnel sa nasa lugar |
| **Direktang Kumonekta / ExpressRoute** | Mga nakatalagang pribadong koneksyon |
| **VPC Peering** | Ikonekta ang mga VPC sa loob o sa pagitan ng mga account |
---

## Seguridad
### Nakabahaging Modelo ng Pananagutan
| Layer | Provider | Customer |
|-------|----------|----------|
| **Imprastraktura** (hardware, pasilidad) | ✅ | |
| **Compute, Storage, Networking** | ✅ (pinamamahalaan) | ✅ (pinamamahalaan sa sarili) |
| **Data, Mga Application, Pagkakakilanlan** | | ✅ |
Kung mas pinamamahalaan ang serbisyo, mas pinangangasiwaan ng provider. Sa IaaS pinamamahalaan mo ang halos lahat; sa SaaS, pinangangasiwaan ng provider ang halos lahat ng ito.
### Pamamahala ng Pagkakakilanlan at Pag-access (IAM)
| Konsepto | Paglalarawan |
|---------|-------------|
| **Mga Gumagamit** | Mga indibidwal na pagkakakilanlan |
| **Mga Pangkat** | Mga koleksyon ng mga user |
| **Mga Tungkulin** | Mga pansamantalang kredensyal para sa mga serbisyo o user |
| **Mga Patakaran** | Mga dokumentong tumutukoy sa mga pahintulot |
| **Prinsipyo** | Pinakamababang pribilehiyo, paghihiwalay ng mga tungkulin |
### Proteksyon ng Data
- **Nakatigil ang pag-encrypt**: KMS, mga key na pinamamahalaan ng customer, HSM.
- **Encryption in transit**: TLS/SSL, HTTPS.
- **Pamamahala ng mga lihim**: Tagapamahala ng mga Lihim, Key Vault — hindi kailanman mga lihim ng hardcode.
---

## DevOps sa Cloud
### Imprastraktura bilang Code (IaC)
| Tool | Paglalarawan |
|------|-------------|
| **Terraform** | Multi-cloud, declarative HCL, pamamahala ng estado |
| **CloudFormation** | AWS-native, YAML/JSON na mga template |
| **Mga Template ng ARM / Bicep** | Azure-native |
| **Pulumi** | Imprastraktura gamit ang mga programming language (Python, Go, atbp.) |
### Mga Serbisyo ng CI/CD
| Provider | Mga tool |
|----------|-------|
| **AWS** | CodePipeline, CodeBuild, CodeDeploy |
| **Azure** | Azure DevOps, GitHub Actions |
| **GCP** | Cloud Build, Cloud Deploy |
| **Third-party** | Jenkins, CircleCI, GitLab CI |
### Pagsubaybay at Pagmamasid
| Kakayahan | AWS | Azure | GCP |
|-----------|-----|-------|-----|
| **Mga Sukatan** | CloudWatch | Azure Monitor | Cloud Monitoring |
| **Pag-log** | Mga Log ng CloudWatch | Log Analytics | Cloud Logging |
| **Pagsubaybay** | X-Ray | Mga Insight sa Application | Cloud Trace |
---

## Pamamahala ng Gastos
### Mga Modelo sa Pagpepresyo
| Modelo | Paglalarawan | Pinakamahusay Para sa |
|-------|-------------|----------|
| **On-Demand** | Magbayad para sa iyong ginagamit, sa pamamagitan ng segundo/oras | Variable, panandaliang workload |
| **Reserved Instance** | 1–3 taong pangako, makabuluhang diskwento | Mga steady-state na workload |
| **Spot Instance** | Mag-bid para sa hindi nagamit na kapasidad; maaaring maputol | Fault-tolerant, flexible na mga trabaho |
| **Mga Savings Plan** | Flexible na pagpepresyo ng pangako | Pinaghalong mga pattern ng paggamit |
| **Libreng Tier** | Limitadong libreng paggamit para sa mga bagong account | Pag-aaral, prototyping |
### Mga Istratehiya sa Pag-optimize
Tamang laki ng mga instance upang tumugma sa mga workload. Gumamit ng auto-scaling upang mahawakan ang mga spike ng demand. I-reserve ang kapasidad para sa predictable load. Gumamit ng mga spot instance para sa mga batch na trabaho. Ilipat ang madalang ma-access na data sa mas murang mga tier ng storage. Tanggalin ang mga hindi nagamit na mapagkukunan (mga naulilang snapshot, idle load balancer, hindi naka-attach na mga IP).
---

## Mataas na Availability at Disaster Recovery
### Mga Konsepto sa Availability
| Konsepto | Paglalarawan |
|---------|-------------|
| **Availability Zone (AZ)** | Pisikal na hiwalay na mga sentro ng data sa loob ng isang rehiyon |
| **Rehiyon** | Heyograpikong lugar na may maraming AZ |
| **Edge Location** | Lokasyon ng cache ng CDN para sa paghahatid ng nilalaman |
### Diskarte sa Pagbawi ng Sakuna
| Diskarte | Gastos | RTO | RPO | Paglalarawan |
|----------|------|-----|-----|-------------|
| **Backup at Restore** | Pinakamababa | Oras | Oras–araw | Pana-panahong pag-backup, ibalik kapag kinakailangan |
| **Pilot Light** | Mababa | Minuto–oras | Mga minuto | Palaging tumatakbo ang mga pangunahing elemento, pinalaki ang sakuna |
| **Warm Standby** | Katamtaman | Mga minuto | Segundo–minuto | Palaging tumatakbo ang naka-scale-down na bersyon |
| **Multi-Site Aktibo/Aktibo** | Pinakamataas | Malapit sa zero | Zero | Buong produksyon sa maraming rehiyon |
**RTO** (Layunin ng Oras ng Pagbawi) = maximum na katanggap-tanggap na downtime. **RPO** (Recovery Point Objective) = maximum na katanggap-tanggap na pagkawala ng data.
---

## Mga Umuusbong na Trend
| Uso | Ano ang Nangyayari |
|-------|----------------|
| **Edge Computing** | Pinoproseso ang data na mas malapit sa pinagmulan (AWS Outposts, Wavelength, Azure Edge) |
| **Multi-Cloud** | Pag-iwas sa vendor lock-in; paggamit ng pinakamahusay na lahi sa mga provider |
| **Mga Serbisyo ng AI/ML** | Mga pre-trained na modelo (vision, speech, language) + custom na pagsasanay (SageMaker, Vertex AI) |
| **Quantum Computing** | Mga serbisyong pang-eksperimento sa maagang yugto (AWS Braket, Azure Quantum) |
| **Sustainable Cloud** | Carbon footprint tracking, renewable energy commitments, green architecture |