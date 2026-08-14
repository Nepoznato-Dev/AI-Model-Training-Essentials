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
# Ulinganisho wa Huduma za Wingu
Ulinganisho wa kando wa watoa huduma wakuu watatu wa wingu - AWS, Azure, na Google Cloud - kwenye kompyuta, hifadhi, hifadhidata, AI/ML, mitandao, ufuatiliaji, na miundombinu-kama-misimbo. Inafaa kwa wasanifu kuamua ni jukwaa gani la kutumia, au huduma za uchoraji ramani kutoka kwa wingu moja hadi nyingine.
---

## Muhtasari wa Mtoa Huduma
| | AWS | Azure | Google Cloud (GCP) |
|---|-----|-------|---------------------|
| **Kushiriki soko** | ~31% (kubwa zaidi) | ~25% (pili) | ~11% (ya tatu, inayokua kwa kasi) |
| **Nguvu** | Upana wa huduma; ukomavu; mfumo ikolojia | Ushirikiano wa biashara; wingu mseto; Rafu ya Microsoft | Data/AI; Kubernetes; mtandao wa kimataifa |
| **Bora kwa** | Kuanzishwa kwa biashara; katalogi pana zaidi ya huduma | Biashara zilizo na Microsoft/Active Directory; mseto | Mzigo wa kazi unaohitaji data; Kubernetes-asili; AI/ML |
| **Mikoa** | Mikoa 33, 105 AZs | Zaidi ya mikoa 60 | Mikoa 40+, kanda 100+ |
| **Kiwango cha bure** | Kiwango cha bure cha miezi 12 + bila malipo kila wakati | Miezi 12 bila malipo + mkopo wa $200 | Salio la $300 kwa siku 90 + bila malipo kila wakati |
---

##Kokotoo
| Kitengo cha Huduma | AWS | Azure | GCP |
|-----------------------|-------|-----|
| **Mashine Halisi** | EC2 (Wingu la Kukokotoa la Elastic) | Mashine Pembeni | Injini ya Kuhesabu |
| **Kuongeza kiotomatiki** | Vikundi vya Kuongeza Kiotomatiki | Seti Pembe za Mizani ya Mashine | Vikundi vya Matukio |
| **Kazi zisizo na Seva** | Lambda | Kazi za Azure | Kazi za Wingu |
| **Usajili wa Kontena** | ECR (Sajili ya Kontena Elastiki) | Usajili wa Kontena ya Azure | Usajili wa Vizalia |
| **Ochestration ya chombo** | ECS / EKS | ACS / AKS | GKE / Cloud Run |
| **Vyombo Visivyo na Seva** | Fargate | Programu za Kontena | Cloud Run |
| **Jukwaa la Programu (PaaS)** | Elastic Beanstalk, App Runner | Huduma ya Programu | Injini ya Programu |
| **Uchakataji Bechi** | Kundi la AWS | Kundi la Azure | Kundi la Wingu |
| **GPU / AI Compute** | EC2 (Matukio ya P4d, P5) | Mfululizo wa NC/ND VM | A2/A3 VMs; TPU |
### Miundo ya Bei ya VM
| Mfano | AWS | Azure | GCP |
|-------|-----|-------|------|
| **Inapohitajika** | Matukio Unapohitaji | Lipa kadri unavyoenda | Inapohitajika |
| **Imehifadhiwa / Imejitolea** | Matukio Yaliyohifadhiwa (mwaka 1-3) | VM Zilizohifadhiwa (mwaka 1–3) | Mapunguzo ya matumizi yaliyowekwa (mwaka 1–3) |
| **Doa/Inayoweza kukatika** | Matukio ya Doa | Doa VM | Preemptible / Spot VMs |
| **Mipango ya kuweka akiba** | Mipango ya Akiba | Mipango ya akiba | Mapunguzo ya matumizi yaliyoahidiwa |
---

## Hifadhi
| Kitengo cha Huduma | AWS | Azure | GCP |
|-----------------------|-------|-----|
| **Hifadhi ya Kitu** | S3 | Hifadhi ya Blob | Hifadhi ya Wingu |
| **Zuia Hifadhi** | EBS | Diski Zinazosimamiwa | Diski ya Kudumu |
| **Hifadhi ya Faili** | EFS, FSx | Faili za Azure | Hifadhi ya faili |
| **Kumbukumbu / Baridi** | S3 Glacier, Hifadhi ya Kina | Viwango vya Blob Cool/Hifadhi Kumbukumbu | Cloud Storage Coldline/Archive |
| **Uhamisho wa Data** | Mpira wa theluji, Usawazishaji Data | Sanduku la Data | Hamisha Kifaa |
### Ulinganisho wa Madarasa ya Hifadhi
| Tumia Kesi | AWS S3 | Azure Blob | Hifadhi ya Wingu ya GCP |
|----------|---------------------|------------------|
| **Ufikiaji wa mara kwa mara** | S3 Kawaida | Moto | Kawaida |
| **Upatikanaji mara kwa mara** | S3 Kawaida-IA | Cool | Karibu |
| **Ufikiaji adimu** | S3 Kanda Moja-IA | - | Mstari wa baridi |
| **Kumbukumbu** | S3 Glacier / Hifadhi ya Kina | Hifadhi | Hifadhi |
---

## Hifadhidata
| Kitengo cha Huduma | AWS | Azure | GCP |
|-----------------------|-------|-----|
| **Kihusiano (kinasimamiwa)** | RDS (MySQL, PostgreSQL, Oracle, Seva ya SQL) | Hifadhidata ya Azure (MySQL, PostgreSQL); Azure SQL | SQL ya Wingu (MySQL, PostgreSQL) |
| **Kimahusiano (asili ya wingu)** | Aurora (MySQL/PostgreSQL patanifu) | Hifadhidata ya Azure SQL (mabwawa ya elastic) | Cloud Spanner (inasambazwa duniani kote) |
| **NoSQL (hati)** | DynamoDB | Cosmos DB (MongoDB API, SQL API) | Hifadhi ya moto; Hifadhidata |
| **NoSQL (safu wima-pana)** | DynamoDB (pia) | Cosmos DB (Cassandra API) | Kubwa |
| **NoSQL (thamani-msingi)** | DynamoDB, ElastiCache | Cache ya Azure kwa Redis | Hifadhi ya kumbukumbu (Redis) |
| **Grafu** | Neptune | Cosmos DB (Gremlin API) | - |
| **Mfululizo wa saa** | Muda | Azure Data Explorer | - |
| **Leja** | QLDB | Leja ya Siri ya Azure | - |
| **Kache ya kumbukumbu** | ElastiCache (Redis, Memcached) | Cache ya Azure kwa Redis | Hifadhi ya kumbukumbu |
| **Tafuta** | Huduma ya OpenSearch | Utafutaji wa Azure AI | Utafutaji wa Wingu; Utafutaji wa Vertex AI |
| **Ghala la data** | Redshift | Uchanganuzi wa Synapse | BigQuery |
---

## AI na Kujifunza kwa Mashine
| Kitengo cha Huduma | AWS | Azure | GCP |
|-----------------------|-------|-----|
| **Jukwaa la ML** | SageMaker | Kujifunza kwa Mashine ya Azure | Vertex AI |
| **API zilizopewa mafunzo ya awali** | Utambuzi (maono), Polly (TTS), Fahamu (NLP), Nakili | Huduma za Utambuzi (Maono, Hotuba, Lugha, Uamuzi) | Maono AI, Hotuba-kwa-Maandishi, API ya Lugha Asilia |
| **LLM / AI ya Kuzalisha** | Bedrock (Claude, Llama, Titan) | Huduma ya Azure OpenAI (GPT-4, DALL-E) | Vertex AI (Gemini); Bustani ya Mfano |
| **Vekta / Upachikaji** | OpenSearch (k-NN), Misingi ya Maarifa ya Bedrock | Utafutaji wa Azure AI (vekta) | Utaftaji wa Vekta ya Vertex AI, AloiDB |
| **MLOps** | Mabomba ya SageMaker, Usajili wa Mfano | Mabomba ya Azure ML, Usajili wa Mfano | Mabomba ya Vertex AI, Usajili wa Mfano |
| **Kuweka lebo ya data** | SageMaker Ground Ukweli | Uwekaji Data ya Azure ML | Uwekaji Data wa Vertex AI |
| **Mazungumzo AI** | Leksi | Huduma ya Azure Bot | Dialogflow CX / ES |
| **Tafsiri** | Tafsiri | Mtafsiri | API ya Tafsiri |
---

##Mitandao
| Kitengo cha Huduma | AWS | Azure | GCP |
|-----------------------|-------|-----|
| **Mtandao wa Mtandao** | VPC | Mtandao Pepe (VNet) | VPC |
| **Kusawazisha Mizigo** | ELB/ALB/NLB/CLB | Kisawazisha cha Pakia (Maombi, Mtandao, Lango) | Kusawazisha Mzigo wa Wingu |
| **DNS** | Njia ya 53 | Azure DNS | Cloud DNS |
| **CDN** | CloudFront | Mlango wa mbele wa Azure | Cloud CDN |
| **Lango la API** | Lango la API | Usimamizi wa API | Lango la API |
| **VPN** | VPN ya tovuti-kwa-Site, VPN ya Mteja | Lango la VPN | Cloud VPN |
| **Unganisha moja kwa moja / ExpressRoute** | Unganisha moja kwa moja | Njia ya Express | Muunganisho wa Wingu |
| **Kiungo cha Kibinafsi** | PrivateLink, VPC Endpoints | Kiungo cha Binafsi, Miisho ya Kibinafsi | Unganisha Huduma ya Kibinafsi |
| **Firewall** | WAF, Mtandao Firewall | Azure Firewall, WAF | Cloud Armour, Firewall |
| **Ulinzi wa DDoS** | Ngao ya Kawaida / ya Juu | Ulinzi wa DDoS | Silaha za Wingu |
---

## Ufuatiliaji na Uwekaji Magogo
| Kitengo cha Huduma | AWS | Azure | GCP |
|-----------------------|-------|-----|
| **Vipimo / Ufuatiliaji** | CloudWatch | Azure Monitor | Ufuatiliaji wa Wingu (Stackdriver) |
| **Kuweka kumbukumbu** | Kumbukumbu za CloudWatch | Uchanganuzi wa Kumbukumbu (Kumbukumbu za Kufuatilia Azure) | Kuweka Magogo kwa Wingu |
| **Kufuatilia** | X-Ray | Maarifa ya Programu | Ufuatiliaji wa Wingu |
| **Inatahadharisha** | Kengele za CloudWatch | Arifa za Kufuatilia Azure | Tahadhari za Ufuatiliaji wa Wingu |
| **Dashibodi** | Dashibodi za CloudWatch | Vitabu vya Kazi vya Azure / Dashibodi | Dashibodi za Ufuatiliaji wa Wingu |
| **Hitilafu katika kufuatilia** | CloudWatch Synthetics | Maarifa ya Programu | Kuripoti Kosa la Wingu |
| **Mhusika wa tatu** | Datadog, Relic Mpya, PagerDuty | Datadog, Relic Mpya, PagerDuty | Datadog, Relic Mpya, PagerDuty |
---

## Miundombinu kama Kanuni na DevOps
| Kitengo cha Huduma | AWS | Azure | GCP |
|-----------------------|-------|-----|
| **IaC (asili)** | CloudFormation | Violezo vya ARM / Bicep | Meneja Usambazaji / Pulumi |
| **IaC (wingu-msalaba)** | Terraform, Pulumi, CDK | Terraform, Pulumi, Bicep | Terraform, Pulumi |
| **CI/CD** | CodePipeline, CodeBuild | Azure DevOps, Vitendo vya GitHub | Kujenga Wingu; Usambazaji wa Wingu |
| **Usajili wa Kontena** | ECR | Usajili wa Kontena ya Azure | Usajili wa Vizalia |
| **GitOps** | App Mesh + Flux/ArgoCD | Flux/ArgoCD kwenye AKS | Usawazishaji wa Mipangilio (Anthos) |
| **Usimamizi wa Siri** | Meneja wa Siri, Duka la Vigezo vya SSM | Vault muhimu | Meneja wa Siri |
---

## Mazingatio ya Bei
| Sababu | AWS | Azure | GCP |
|--------|-----|-------|------|
| **Uzito wa bili** | Kwa kila sekunde (baada ya saa ya kwanza kwa baadhi) | kwa sekunde | kwa sekunde |
| **Punguzo la matumizi endelevu** | Matukio Yaliyohifadhiwa / Mipango ya Akiba | VM Zilizohifadhiwa | Mapunguzo ya matumizi yaliyoahidiwa |
| **Matukio matupu** | Punguzo la hadi 90% | Punguzo la hadi 90% | Punguzo la hadi 91% |
| **Kutoka kwa data** | Imetozwa (ghali) | Imeshtakiwa | Bei sawa bila kujali marudio (mara nyingi ni nafuu) |
| **Kiwango cha bure** | Miezi 12 + bila malipo kila wakati | Miezi 12 + mkopo wa $200 | $300 kwa siku 90 + bila malipo kila wakati |
| **Punguzo la biashara** | Mpango wa Punguzo la Biashara (EDP) | MACC (Mkataba wa Ahadi ya Fedha) | Matumizi ya kujitolea + CUDs |
---

## Wakati wa Kutumia Ambayo
| Hali | Imependekezwa | Kwa nini |
|----------|-------------|-----|
| **Uteuzi mpana wa huduma; mfumo ikolojia uliokomaa** | AWS | Katalogi kubwa zaidi; miunganisho mingi ya wahusika wengine |
| ** Biashara ya Microsoft; Saraka Inayotumika; mseto** | Azure | Ujumuishaji wa asili wa AD; zana kali za mseto |
| **Uhifadhi wa data; BigQuery; analytics-nzito** | GCP | BigQuery ni bora katika darasa; muunganisho wa data usio na mshono |
| **Maendeleo ya asili ya Kubernetes** | GCP | GKE ndiyo Kubernetes inayosimamiwa vyema zaidi |
| **Programu za Uzalishaji za AI / LLM** | Azure au GCP | Azure OpenAI kwa mifano ya GPT; Vertex AI ya Gemini |
| **Programu za kimataifa, za kusubiri muda wa chini** | GCP | Mtandao wa kimataifa wa Google ni faida ya kweli |
| **Serikali / utiifu-mzigo mzito** | AWS au Azure | Vyeti vingi vya kufuata; GovCloud mikoa |
| **Vianzishaji vinavyozingatia gharama** | GCP au AWS | Kiwango cha bure cha GCP ni cha ukarimu; AWS ina mikopo ya kuanzia |
| **Raka iliyopo ya Microsoft / .NET** | Azure | Ushirikiano mkali na Visual Studio, .NET, Ofisi ya 365 |
| **Mkakati wa mawingu mengi** | Terraform + zote tatu | Tumia Terraform kudhibiti rasilimali kwenye mawingu |
---

## Muhtasari
Mawingu yote matatu yana uwezo, yanategemewa, na yanapanuka kila mara. Chaguo kwa kawaida hutegemea: timu yako tayari inafahamu nini, mikataba yako iliyopo inafananaje, na ni huduma zipi mahususi muhimu kwa mzigo wako wa kazi. Wingu nyingi inazidi kuwa kawaida - tumia Terraform au Pulumi ili kuzuia kutoingia kwa muuzaji kwenye safu ya miundombinu, na uchague kila wingu kwa kile kinachofanya vizuri zaidi.