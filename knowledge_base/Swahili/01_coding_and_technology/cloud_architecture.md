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

# Usanifu wa Wingu
Kompyuta ya wingu imebadilisha kimsingi jinsi mashirika yanavyounda, kupeleka, na kuongeza programu. Badala ya kununua na kudumisha seva halisi, unaweza kutoa rasilimali za kompyuta unapohitaji, kulipia unachotumia, na kuongeza kimataifa kwa dakika. Faili hii inashughulikia dhana za msingi, mifumo ya usanifu, huduma, na mbinu bora unazohitaji kujua.
---

## Misingi ya Kompyuta ya Wingu
### Cloud Computing ni nini?
Uwasilishaji wa rasilimali za kompyuta unapohitajika - seva, hifadhi, hifadhidata, mtandao, programu - kupitia mtandao kwa bei ya lipa kadri uwezavyo.
### Sifa Muhimu za NIST
| Tabia | Maana |
|---------------|---------|
| **Huduma ya Kujihudumia Unapohitaji** | Utoaji wa rasilimali bila mwingiliano wa kibinadamu |
| **Ufikiaji Mpana wa Mtandao** | Inapatikana kwenye mtandao kupitia mifumo ya kawaida |
| **Ukusanyaji wa Rasilimali** | Mfano wa wapangaji wengi; rasilimali zilizogawiwa kwa nguvu |
| **Msisimko wa Haraka** | Ongeza nje na ndani haraka |
| **Huduma Iliyopimwa** | Matumizi yanafuatiliwa na kutozwa |
### Miundo ya Usambazaji
| Mfano | Maelezo | Wakati wa Kutumia |
|-------|-------------|-------------|
| **Wingu la Umma** | Inamilikiwa na watoa huduma; miundombinu ya pamoja (AWS, Azure, GCP) | Mizigo mingi ya kazi; gharama nafuu |
| **Wingu la Kibinafsi** | Imejitolea kwa shirika moja | Mahitaji ya udhibiti, data nyeti |
| **Wingu Mseto** | Mchanganyiko wa umma na binafsi | Kubadilika + kufuata |
| **Wingu nyingi** | Kutumia watoa huduma wengi wa wingu wa umma | Epuka kufuli kwa muuzaji, aina bora zaidi |
### Miundo ya Huduma
| Mfano | Hutoa | Mifano | Tumia Kesi |
|-------|---------------------|-----------|
| **IaaS** | VM, hifadhi, mitandao, Mfumo wa Uendeshaji | AWS EC2, Azure VMs, GCP Compute Engine | Uhamiaji wa kuinua-na-hamisha, udhibiti kamili |
| **PaaS** | Majukwaa ya maendeleo, hifadhidata, vifaa vya kati | Heroku, Google App Engine, AWS Elastic Beanstalk | Ukuzaji wa programu, uwekaji API |
| **SaaS** | Kamilisha programu kupitia mtandao | Salesforce, Google Workspace, Microsoft 365 | Barua pepe, CRM, ushirikiano |
| **FaaS / Isiyo na Seva** | Utekelezaji wa kitendakazi kinachoendeshwa na tukio | AWS Lambda, Kazi za Azure, Kazi za Wingu la GCP | API, usindikaji wa tukio, kazi zilizopangwa |
---

## Watoa Huduma Wakubwa wa Wingu
| Mtoa huduma | Kushiriki Soko | Nguvu |
|----------|-------------------------|
| **AWS** | ~ 32% | Katalogi pana ya huduma, mfumo mkubwa wa ikolojia |
| **Azure** | ~ 23% | Ujumuishaji wa biashara, wingu mseto, safu ya Microsoft |
| **GCP** | ~10% | Uchanganuzi wa data, AI/ML, Kubernetes |
| **Alibaba Cloud** | ~4% | Inatawala katika Asia-Pasifiki |
| **Oracle Cloud** | ~2% | Upakiaji wa hifadhidata, programu za biashara |
| **Wingu la IBM** | ~2% | Mtazamo wa biashara, Watson AI |
| **DigitalOcean** | Niche | Matoleo yanayofaa kwa wasanidi programu na yaliyorahisishwa |
### Ulinganisho wa Huduma (Watoa Huduma 3 Bora)
| Kitengo | AWS | Azure | GCP |
|----------|-----|-------|-----|
| **Kokotoo** | EC2, Lambda, ECS | VM, Kazi, AKS | Injini ya Kuhesabu, Kazi za Wingu, GKE |
| **Hifadhi** | S3, EBS, Glacier | Hifadhi ya Blob, Hifadhi ya Diski | Hifadhi ya Wingu, Diski ya Kudumu |
| ** Hifadhidata** | RDS, DynamoDB, Aurora | Hifadhidata ya SQL, Cosmos DB | Cloud SQL, Firestore, Bigtable |
| **Uchanganuzi** | Redshift, EMR | Synapse, Databricks | BigQuery, Utiririshaji Data |
| **AI/ML** | SageMaker, Utambuzi | Azure ML, Huduma za Utambuzi | Vertex AI, AutoML |
| **Mtandao** | VPC, Njia ya 53, CloudFront | VNet, Kidhibiti cha Trafiki | VPC, Cloud DNS, Cloud CDN |
---

## Miundo ya Usanifu
### Mfumo Uliosanifiwa Vizuri
Watoa huduma wakuu watatu huchapisha mifumo iliyosanifiwa vizuri iliyojengwa karibu na nguzo tano:
| Nguzo | Kanuni Muhimu |
|--------|---------------|
| **Ubora wa Uendeshaji** | Operesheni otomatiki; kufanya mabadiliko ya mara kwa mara, ya kugeuzwa; tarajia kushindwa |
| **Usalama** | Msingi wenye nguvu wa utambulisho; weka usalama katika kila safu; kulinda data katika usafiri na katika mapumziko |
| **Kuegemea** | Taratibu za kurejesha mtihani; kupona kiotomatiki kutokana na kushindwa; punguza kwa mlalo |
| **Ufanisi wa Utendaji** | Tumia bila seva; kwenda kimataifa kwa dakika; majaribio mara nyingi |
| **Uboreshaji wa Gharama** | Kupitisha mfano wa matumizi; tumia huduma zinazosimamiwa; acha kutumia pesa kwenye kazi zisizo na tofauti |
### Miundo ya Kawaida
| Muundo | Maelezo | Faida | Changamoto |
|---------|------------------------|------------|
| **Huduma Ndogo** | Tengeneza programu katika huduma ndogo, zinazojitegemea | Scalability, kosa kutengwa, kupelekwa huru | Utata uliosambazwa, uthabiti wa data |
| **Inayoendeshwa na Tukio** | Vipengele huwasiliana kupitia matukio | Uunganishaji uliolegea, usindikaji wa wakati halisi | Utata wa kurekebisha, hatimaye uthabiti |
| **Bila seva** | Hakuna usimamizi wa seva; malipo kwa kila utekelezaji | Ufanisi wa gharama, upelekaji wa haraka | Baridi huanza, kufuli kwa muuzaji, vikomo vya utekelezaji |
| **Yenye Tabaka (N-Tier)** | Wasilisho → Mantiki ya biashara → Ufikiaji data → Hifadhidata | Mgawanyo wa wasiwasi, kudumisha | Inaweza kuwa monolithic |
| **Kulingana na Nafasi** | Data iliyosambazwa kwenye nodi za kumbukumbu zilizoboreshwa | Hushughulikia upatanisho wa juu, utulivu wa chini | Ugumu wa kubuni na kudhibiti |
---

##Huduma za Msingi
### Kokotoa
| Aina ya Huduma | Maelezo |
|-----------------------|
| **Mashine Halisi** | Kusudi la jumla, uboreshaji wa hesabu, uboreshaji wa kumbukumbu, GPU. Bei: inapohitajika, imehifadhiwa, mahali. |
| **Vyombo** | Wakati wa kukimbia wa Docker; okestra kupitia Kubernetes (EKS, AKS, GKE). Sajili: ECR, GCR, ACR. |
| **Kazi zisizo na Seva** | Tukio lililoanzishwa, lisilo na uraia. Vizuizi vya muda wa utekelezaji, kumbukumbu, concurrency. |
### Hifadhi
| Andika | Sifa | Mifano | Bora Kwa |
|------|--------------------------|-----------|
| **Kitu** | Muundo tambarare, ufikiaji wa HTTP, metadata-tajiri | S3, Hifadhi ya Wingu, Blob ya Azure | Mali tuli, chelezo, maziwa ya data |
| **Zuia** | Kiasi ghafi kilichoambatishwa kwa VM | EBS, Diski ya Kudumu, Diski za Azure | Hifadhidata, kiasi cha boot |
| **Faili** | Mifumo ya faili iliyoshirikiwa (NFS/SMB) | EFS, Hifadhi ya faili, Faili za Azure | Usimamizi wa maudhui, usanidi ulioshirikiwa |
| **Kumbukumbu** | Gharama ya chini zaidi, ucheleweshaji wa kurejesha | S3 Glacier, Jalada la Azure | Kuzingatia, chelezo za muda mrefu |
### Hifadhidata
| Kitengo | Huduma | Tumia Kesi |
|----------|----------|-----------|
| **Mahusiano Yanayosimamiwa** | RDS, Cloud SQL, Azure SQL | Programu za kitamaduni, miamala ya ACID |
| **NoSQL — Hati** | DocumentDB, Firestore, Cosmos DB | Miradi inayoweza kubadilika, data ya JSON |
| **NoSQL — Thamani-Muhimu** | DynamoDB, Redis Cache | Kuhifadhi akiba, vipindi, utafutaji rahisi |
| **NoSQL — Safu Wima-Pana** | Bigtable, Cassandra | Andika-nzito, mfululizo wa wakati |
| **NoSQL — Grafu** | Neptune, Cosmos DB (Grafu API) | Mahusiano, mitandao ya kijamii |
| **Uhifadhi wa Data** | Snowflake, Redshift, BigQuery, Synapse | Uchanganuzi, BI |
| **Kuhifadhi** | ElastiCache, Cloud Memorystore | Hifadhi ya kipindi, akiba ya hoja |
---

##Mitandao
### Mitandao Pepe
Kila utumaji wa wingu huishi ndani ya Wingu la Kibinafsi la Virtual (VPC/VNet) - mtandao uliotengwa unaofafanua kwa vizuizi vya CIDR, neti ndogo (za umma au za faragha), majedwali ya njia na lango.
### Kusawazisha Mizigo na CDN
| Huduma | Kusudi |
|---------|---------|
| **Mizani ya Mizigo** | Sambaza trafiki katika matukio (mtandao wa L4, programu ya L7) |
| **CDN** | Maudhui ya akiba kwenye maeneo makali kwa muda wa kusubiri wa chini (CloudFront, Cloud CDN, Azure CDN) |
| **DNS** | Usajili wa kikoa, sera za uelekezaji, ukaguzi wa afya (Njia ya 53, Cloud DNS, Azure DNS) |
### Chaguzi za Muunganisho
| Chaguo | Maelezo |
|--------|-------------|
| **Lango la Mtandao** | Ufikiaji wa mtandao wa umma kwa VPC |
| **Lango la NAT** | Ufikiaji wa nje wa subnet ya kibinafsi |
| **VPN** | Njia zilizosimbwa kwa njia fiche kwenye majengo |
| **Unganisha moja kwa moja / ExpressRoute** | Miunganisho ya kibinafsi iliyojitolea |
| **VPC Peering** | Unganisha VPC ndani au kati ya akaunti |
---

##Usalama
### Muundo wa Wajibu wa Pamoja
| Tabaka | Mtoa huduma | Mteja |
|-------|----------------------|
| **Miundombinu** (vifaa, vifaa) | ✅ | |
| **Kokotoo, Hifadhi, Mitandao** | ✅ (inasimamiwa) | ✅ (kujisimamia) |
| **Data, Maombi, Utambulisho** | | ✅ |
Kadiri huduma inavyosimamiwa, ndivyo mtoa huduma anavyoshughulikia zaidi. Ukiwa na IaaS unasimamia karibu kila kitu; na SaaS, mtoa huduma hushughulikia karibu yote.
### Usimamizi wa Utambulisho na Ufikiaji (IAM)
| Dhana | Maelezo |
|---------|-------------|
| **Watumiaji** | Vitambulisho vya mtu binafsi |
| **Vikundi** | Mikusanyiko ya watumiaji |
| **Majukumu** | Vitambulisho vya muda vya huduma au watumiaji |
| **Sera** | Hati zinazofafanua ruhusa |
| **Kanuni** | Upendeleo mdogo, mgawanyo wa majukumu |
### Ulinzi wa Data
- **Usimbaji fiche ukiwa umepumzika**: KMS, funguo zinazodhibitiwa na mteja, HSM.
- **Usimbaji fiche katika usafiri**: TLS/SSL, HTTPS.
- **Udhibiti wa Siri**: Kidhibiti cha Siri, Vault muhimu - kamwe si siri za msimbo mgumu.
---

## DevOps katika Cloud
### Miundombinu kama Kanuni (IaC)
| Zana | Maelezo |
|------|-------------|
| **Terraform** | Wingu nyingi, HCL ya kutangaza, usimamizi wa serikali |
| **CloudFormation** | Violezo vya asili vya AWS, YAML/JSON |
| **Violezo vya ARM / Bicep** | Asili ya Azure |
| **Pulumi** | Miundombinu inayotumia lugha za programu (Python, Go, n.k.) |
### Huduma za CI/CD
| Mtoa huduma | Zana |
|----------|-------|
| **AWS** | CodePipeline, CodeBuild, CodeDeploy |
| **Azure** | Azure DevOps, Vitendo vya GitHub |
| **GCP** | Cloud Build, Cloud Deploy |
| **Mhusika wa tatu** | Jenkins, CircleCI, GitLab CI |
### Ufuatiliaji na Kuzingatiwa
| Uwezo | AWS | Azure | GCP |
|-----------|-----|-------|-----|
| **Vipimo** | CloudWatch | Azure Monitor | Ufuatiliaji wa Wingu |
| **Kuweka kumbukumbu** | Kumbukumbu za CloudWatch | Uchanganuzi wa Kumbukumbu | Kuweka Magogo kwa Wingu |
| **Kufuatilia** | X-Ray | Maarifa ya Programu | Ufuatiliaji wa Wingu |
---

## Usimamizi wa Gharama
### Miundo ya Bei
| Mfano | Maelezo | Bora Kwa |
|-------|-------------|-----------|
| **Inapohitajika** | Lipia unachotumia, kwa sekunde/saa | Inayoweza kubadilika, mizigo ya kazi ya muda mfupi |
| **Matukio Yaliyohifadhiwa** | Ahadi ya mwaka 1-3, punguzo kubwa | Mizigo ya hali thabiti |
| **Matukio ya doa** | Zabuni kwa uwezo usiotumika; inaweza kuingiliwa | Kazi zinazostahimili makosa, zinazonyumbulika |
| **Mipango ya Akiba** | Bei inayobadilika ya ahadi | Mitindo mchanganyiko ya matumizi |
| **Ngazi Huria** | Matumizi machache ya bila malipo kwa akaunti mpya | Kujifunza, prototyping |
### Mikakati ya Uboreshaji
Matukio ya ukubwa wa kulia ili kulinganisha mizigo ya kazi. Tumia kuongeza kiotomatiki ili kushughulikia ongezeko la mahitaji. Hifadhi uwezo kwa mizigo inayoweza kutabirika. Tumia mifano ya doa kwa kazi za kundi. Hamisha data ambayo haipatikani mara kwa mara hadi viwango vya bei nafuu vya hifadhi. Futa rasilimali ambazo hazijatumiwa (picha za mayatima, mizani ya mizigo isiyo na kazi, IP zisizounganishwa).
---

## Upatikanaji wa Juu na Ahueni ya Maafa
### Dhana za Upatikanaji
| Dhana | Maelezo |
|---------|-------------|
| **Eneo la Upatikanaji (AZ)** | Tenganisha vituo vya data ndani ya eneo |
| **Mkoa** | Eneo la kijiografia lenye AZ nyingi |
| **Edge Location** | Mahali pa akiba ya CDN kwa uwasilishaji wa yaliyomo |
### Mikakati ya Kuokoa Maafa
| Mkakati | Gharama | RTO | RPO | Maelezo |
|----------|------|-----|-----|-------------|
| **Hifadhi na Urejeshe** | Chini | Saa | Saa-siku | Hifadhi nakala za mara kwa mara, rudisha inapohitajika |
| **Taa ya Majaribio** | Chini | Dakika–saa | Dakika | Vipengele vya msingi vinaendeshwa kila wakati, ongeza juu ya maafa |
| **Kusubiri Hali Joto** | Kati | Dakika | Sekunde–dakika | Toleo lililopunguzwa linaendelea kila wakati |
| **Tovuti Nyingi Inayotumika/Inayotumika** | Juu | Karibu na sufuri | Sifuri | Uzalishaji kamili katika mikoa mingi |
**RTO** (Lengo la Muda wa Kuokoa) = muda wa juu unaokubalika wa kupumzika. **RPO** (Lengo la Urejeshaji) = upotezaji wa data unaokubalika wa juu zaidi.
---

## Mitindo Inayoibuka
| Mitindo | Nini Kinaendelea |
|-------|-----------------|
| **Edge Computing** | Inachakata data karibu na chanzo (AWS Outposts, Wavelength, Azure Edge) |
| **Wingu nyingi** | Kuepuka kufuli kwa muuzaji; kutumia ufugaji bora kati ya watoa huduma |
| **Huduma za AI/ML** | Mitindo iliyofunzwa mapema (maono, hotuba, lugha) + mafunzo maalum (SageMaker, Vertex AI) |
| **Quantum Computing** | Huduma za majaribio za hatua ya awali (Braket ya AWS, Azure Quantum) |
| **Wingu Endelevu** | Ufuatiliaji wa nyayo za kaboni, ahadi za nishati mbadala, usanifu wa kijani kibichi |