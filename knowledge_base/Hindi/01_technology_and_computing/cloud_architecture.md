# क्लाउड आर्किटेक्चर

## क्लाउड कंप्यूटिंग की मूलभूत बातें

### क्लाउड कंप्यूटिंग क्या है?
इंटरनेट के माध्यम से कंप्यूटिंग संसाधनों (सर्वर, स्टोरेज, डेटाबेस, नेटवर्किंग, सॉफ़्टवेयर) की मांग-आधारित डिलीवरी, जिसमें उपयोग के अनुसार भुगतान किया जाता है।

### आवश्यक विशेषताएँ (NIST परिभाषा)
- **मांग-आधारित स्व-सेवा (On-Demand Self-Service)**: मानव हस्तक्षेप के बिना संसाधनों का प्रावधान
- **विस्तृत नेटवर्क पहुँच (Broad Network Access)**: मानक तंत्रों के माध्यम से नेटवर्क पर उपलब्धता
- **संसाधन पूलिंग (Resource Pooling)**: गतिशील आवंटन वाला मल्टी-टेनेंट मॉडल
- **त्वरित लोचशीलता (Rapid Elasticity)**: तेज़ी से स्केल-आउट और स्केल-इन करना
- **मापी गई सेवा (Measured Service)**: संसाधन उपयोग की निगरानी और बिलिंग

### क्लाउड परिनियोजन मॉडल
- **सार्वजनिक क्लाउड (Public Cloud)**: प्रदाताओं के स्वामित्व वाली साझा अवसंरचना (AWS, Azure, GCP)
- **निजी क्लाउड (Private Cloud)**: एकल संगठन के लिए समर्पित (on-premises या hosted)
- **हाइब्रिड क्लाउड (Hybrid Cloud)**: सार्वजनिक और निजी क्लाउड्स का संयोजन
- **मल्टी-क्लाउड (Multi-Cloud)**: कई सार्वजनिक क्लाउड प्रदाताओं का उपयोग
- **कम्युनिटी क्लाउड (Community Cloud)**: समान चिंताओं वाले संगठनों द्वारा साझा

### सेवा मॉडल

#### सेवा के रूप में अवसंरचना (IaaS)
- **प्रदान करता है**: वर्चुअल मशीनें, स्टोरेज, नेटवर्क, ऑपरेटिंग सिस्टम
- **उदाहरण**: AWS EC2, Google Compute Engine, Azure VMs
- **उपयोग के मामले**: लिफ्ट-एंड-शिफ्ट माइग्रेशन, विकास परिवेश, और उच्च नियंत्रण की आवश्यकताएँ

#### सेवा के रूप में प्लेटफ़ॉर्म (PaaS)
- **प्रदान करता है**: विकास प्लेटफ़ॉर्म, डेटाबेस, मिडलवेयर
- **उदाहरण**: Heroku, Google App Engine, AWS Elastic Beanstalk
- **उपयोग के मामले**: अनुप्रयोग विकास, API परिनियोजन, माइक्रोसर्विसेस

#### सेवा के रूप में सॉफ़्टवेयर (SaaS)
- **प्रदान करता है**: इंटरनेट पर पूर्ण अनुप्रयोग
- **उदाहरण**: Salesforce, Google Workspace, Microsoft 365, Slack
- **उपयोग के मामले**: ईमेल, CRM, सहयोग, व्यावसायिक अनुप्रयोग

#### सेवा के रूप में फ़ंक्शन (FaaS) / सर्वरलेस
- **प्रदान करता है**: इवेंट-ड्रिवन फ़ंक्शन निष्पादन
- **उदाहरण**: AWS Lambda, Azure Functions, Google Cloud Functions
- **उपयोग के मामले**: इवेंट प्रोसेसिंग, APIs, अनुसूचित कार्य, रियल-टाइम प्रोसेसिंग

## प्रमुख क्लाउड प्रदाता

### Amazon Web Services (AWS)
- **बाज़ार हिस्सेदारी**: ~32% (सबसे बड़ा प्रदाता)
- **मुख्य सेवाएँ**:
  - कंप्यूट: EC2, Lambda, ECS, EKS
  - स्टोरेज: S3, EBS, Glacier
  - डेटाबेस: RDS, DynamoDB, Aurora
  - नेटवर्किंग: VPC, Route 53, CloudFront
  - AI/ML: SageMaker, Rekognition, Comprehend

### Microsoft Azure
- **बाज़ार हिस्सेदारी**: ~23%
- **मज़बूत पक्ष**: एंटरप्राइज़ इंटीग्रेशन, हाइब्रिड क्लाउड, Microsoft इकोसिस्टम
- **मुख्य सेवाएँ**:
  - कंप्यूट: Virtual Machines, Azure Functions, AKS
  - स्टोरेज: Blob Storage, Disk Storage
  - डेटाबेस: SQL Database, Cosmos DB
  - नेटवर्किंग: Virtual Network, Traffic Manager
  - AI/ML: Azure ML, Cognitive Services

### Google Cloud Platform (GCP)
- **बाज़ार हिस्सेदारी**: ~10%
- **मज़बूत पक्ष**: डेटा एनालिटिक्स, AI/ML, Kubernetes
- **मुख्य सेवाएँ**:
  - कंप्यूट: Compute Engine, Cloud Functions, GKE
  - स्टोरेज: Cloud Storage, Persistent Disk
  - डेटाबेस: Cloud SQL, Firestore, Bigtable
  - एनालिटिक्स: BigQuery, Dataflow, Pub/Sub
  - AI/ML: Vertex AI, AutoML

### अन्य प्रदाता
- **IBM Cloud**: एंटरप्राइज़ फोकस, Watson AI
- **Oracle Cloud**: डेटाबेस वर्कलोड्स, एंटरप्राइज़ अनुप्रयोग
- **Alibaba Cloud**: Asia-Pacific में प्रमुख
- **DigitalOcean**: डेवलपर-अनुकूल, सरल ऑफ़रिंग्स

## क्लाउड आर्किटेक्चर पैटर्न

### Well-Architected Framework के सिद्धांत

#### परिचालन उत्कृष्टता
- संचालन को स्वचालित करें
- बार-बार और पलटे जा सकने वाले परिवर्तन करें
- प्रक्रियाओं को लगातार परिष्कृत करें
- विफलता का पूर्वानुमान लगाएँ

#### सुरक्षा
- मज़बूत पहचान आधार लागू करें
- ट्रेसबिलिटी सक्षम करें
- सभी परतों पर सुरक्षा लागू करें
- सुरक्षा के श्रेष्ठ अभ्यासों को स्वचालित करें
- डेटा को संचारण और संग्रहण दोनों अवस्थाओं में सुरक्षित रखें

#### विश्वसनीयता
- पुनर्प्राप्ति प्रक्रियाओं का परीक्षण करें
- विफलता से स्वतः पुनर्प्राप्त हों
- उपलब्धता के लिए क्षैतिज रूप से स्केल करें
- क्षमता का अनुमान लगाकर निर्णय लेना बंद करें
- automation में परिवर्तन को प्रबंधित करें

#### प्रदर्शन दक्षता
- उन्नत प्रौद्योगिकियों तक व्यापक पहुँच दें
- मिनटों में वैश्विक स्तर पर पहुँचें
- सर्वरलेस आर्किटेक्चर्स का उपयोग करें
- अधिक बार प्रयोग करें
- सिस्टम की आधारभूत यांत्रिक सीमाओं को ध्यान में रखें

#### लागत अनुकूलन
- उपभोग मॉडल अपनाएँ
- समग्र दक्षता को मापें
- ऐसे कार्यों पर खर्च बंद करें जो आपको विशिष्ट नहीं बनाते
- expenditure का विश्लेषण करें और उसे सही रूप से आवंटित करें
- प्रबंधित सेवाओं का उपयोग करें

### सामान्य आर्किटेक्चर पैटर्न

#### माइक्रोसर्विसेस आर्किटेक्चर
- अनुप्रयोगों को छोटे, स्वतंत्र सेवाओं में विभाजित करें
- प्रत्येक सेवा अपने डेटा और लॉजिक की स्वामी होती है
- APIs (REST, gRPC, messaging) के माध्यम से संचार करें
- स्वतंत्र रूप से परिनियोजित करें
- **लाभ**: स्केलेबिलिटी, दोष-पृथक्करण, तकनीकी विविधता
- **चुनौतियाँ**: वितरित जटिलता, डेटा संगतता, निगरानी

#### इवेंट-ड्रिवन आर्किटेक्चर
- घटक events के माध्यम से संचार करते हैं
- प्रोड्यूसर्स events emit करते हैं, कंज़्यूमर्स प्रतिक्रिया देते हैं
- **पैटर्न**: event sourcing, CQRS, pub/sub
- **प्रौद्योगिकियाँ**: Kafka, SNS/SQS, EventBridge, Pub/Sub
- **लाभ**: कम युग्मन, स्केलेबिलिटी, रियल-टाइम प्रोसेसिंग

#### सर्वरलेस आर्किटेक्चर
- सर्वर प्रबंधन की आवश्यकता नहीं
- प्रति निष्पादन भुगतान
- स्वचालित स्केलिंग
- **घटक**: फ़ंक्शन्स, API Gateway, प्रबंधित सेवाएँ
- **लाभ**: लागत दक्षता, कम संचालन, तेज़ परिनियोजन
- **विचारणीय बातें**: cold starts, vendor lock-in, निष्पादन सीमाएँ

#### स्तरीय आर्किटेक्चर (N-Tier)
- प्रस्तुतीकरण परत (UI)
- अनुप्रयोग/व्यावसायिक तर्क परत
- डेटा एक्सेस परत
- डेटाबेस परत
- **लाभ**: जिम्मेदारियों का पृथक्करण, रखरखाव-सुगमता
- **सामान्य**: 3-tier वेब अनुप्रयोग

#### स्पेस-बेस्ड आर्किटेक्चर
- वितरित डेटा के साथ उच्च concurrency सँभालें
- सर्वरों के बीच virtualized memory
- processing nodes स्वतंत्र रूप से स्केल होते हैं
- **उपयोग के मामले**: high-volume, low-latency अनुप्रयोग

## कंप्यूट सेवाएँ

### वर्चुअल मशीनें
- **प्रकार**: सामान्य प्रयोजन, compute-optimized, memory-optimized, GPU
- **मूल्य निर्धारण**: on-demand, reserved instances, spot instances
- **प्रबंधन**: auto-scaling groups, load balancers
- **श्रेष्ठ अभ्यास**: right-sizing, tagging, निगरानी, patching

### कंटेनर्स
- **Docker**: container runtime मानक
- **Orchestration**: Kubernetes (EKS, AKS, GKE), ECS, Fargate
- **लाभ**: portability, efficiency, consistency
- **Registry**: ECR, GCR, ACR, Docker Hub

### सर्वरलेस फ़ंक्शन्स
- **Execution Model**: event-triggered, stateless
- **सीमाएँ**: execution time, memory, concurrent executions
- **उपयोग के मामले**: APIs, फ़ाइल प्रोसेसिंग, scheduled jobs, IoT backends
- **निगरानी**: invocation counts, errors, duration, cold starts

## स्टोरेज समाधान

### ऑब्जेक्ट स्टोरेज
- **विशेषताएँ**: flat structure, metadata, HTTP access
- **उदाहरण**: AWS S3, Google Cloud Storage, Azure Blob
- **उपयोग के मामले**: static assets, backups, data lakes, archives
- **स्टोरेज क्लासेस**: hot, cool, cold, archive (लागत और पहुँच में भिन्नता)

### ब्लॉक स्टोरेज
- **विशेषताएँ**: raw volumes, VMs से जुड़े हुए
- **उदाहरण**: AWS EBS, Google Persistent Disk, Azure Disks
- **उपयोग के मामले**: databases, boot volumes, high-performance needs
- **प्रकार**: SSD, HDD, provisioned IOPS

### फ़ाइल स्टोरेज
- **विशेषताएँ**: shared file systems, NFS/SMB protocols
- **उदाहरण**: AWS EFS, Google Filestore, Azure Files
- **उपयोग के मामले**: content management, shared configs, lift-and-shift

### आर्काइव स्टोरेज
- **विशेषताएँ**: सबसे कम लागत, retrieval delays
- **उदाहरण**: S3 Glacier, Azure Archive Storage
- **उपयोग के मामले**: compliance, long-term backups, historical data

## डेटाबेस सेवाएँ

### प्रबंधित रिलेशनल डेटाबेस
- **सेवाएँ**: AWS RDS/Aurora, Google Cloud SQL, Azure SQL Database
- **विशेषताएँ**: automated backups, patching, scaling, replication
- **डेटाबेस इंजन**: MySQL, PostgreSQL, MariaDB, Oracle, SQL Server

### NoSQL डेटाबेस
- **डॉक्युमेंट**: DocumentDB, Firestore, Cosmos DB
- **की-वैल्यू**: DynamoDB, Redis Cache
- **वाइड-कॉलम**: Bigtable, Cassandra (managed)
- **ग्राफ**: Neptune, Cosmos DB (graph API)

### डेटा वेयरहाउसिंग
- **सेवाएँ**: Snowflake, Redshift, BigQuery, Synapse
- **विशेषताएँ**: columnar storage, MPP architecture
- **उपयोग के मामले**: analytics, BI, large-scale data analysis

### कैशिंग सेवाएँ
- **इन-मेमोरी**: ElastiCache (Redis/Memcached), Cloud Memorystore
- **CDN कैशिंग**: CloudFront, Cloud CDN, Azure CDN
- **उपयोग के मामले**: session storage, query caching, content delivery

## नेटवर्किंग

### वर्चुअल नेटवर्क्स
- **VPC/VNet**: isolated network environments
- **Subnets**: public (internet-facing), private (केवल internal)
- **IP Addressing**: CIDR blocks, IPv4/IPv6
- **Route Tables**: traffic flow नियंत्रित करती हैं

### लोड बैलेंसिंग
- **प्रकार**: application (L7), network (L4), gateway
- **विशेषताएँ**: health checks, SSL termination, sticky sessions
- **सेवाएँ**: ELB/ALB/NLB, Cloud Load Balancing, Azure Load Balancer

### Content Delivery Networks (CDN)
- **उद्देश्य**: edge locations पर content cache करना
- **लाभ**: कम latency, origin पर कम load, वैश्विक वितरण
- **सेवाएँ**: CloudFront, Cloud CDN, Azure CDN, Akamai

### DNS सेवाएँ
- **कार्य**: domain registration, routing, health checks
- **सेवाएँ**: Route 53, Cloud DNS, Azure DNS
- **रूटिंग नीतियाँ**: simple, weighted, latency-based, geolocation, failover

### कनेक्टिविटी विकल्प
- **Internet Gateway**: public internet access
- **NAT Gateway**: private subnet से outbound access
- **VPN**: on-premises तक encrypted tunnels
- **Direct Connect/ExpressRoute**: dedicated private connections
- **VPC Peering**: accounts के भीतर/बीच VPCs को जोड़ना

## क्लाउड में सुरक्षा

### Shared Responsibility Model
- **Provider Responsibility**: cloud की सुरक्षा (infrastructure)
- **Customer Responsibility**: cloud के भीतर की सुरक्षा (data, applications, access)
- **सेवा के अनुसार भिन्नता**: जितनी अधिक managed सेवा, उतनी अधिक provider responsibility

### पहचान और अभिगम प्रबंधन (IAM)
- **Users**: व्यक्तिगत पहचानें
- **Groups**: उपयोगकर्ताओं के समूह
- **Roles**: services/users के लिए अस्थायी credentials
- **Policies**: permissions परिभाषित करने वाले JSON दस्तावेज़
- **सिद्धांत**: न्यूनतम विशेषाधिकार, कर्तव्यों का पृथक्करण

### नेटवर्क सुरक्षा
- **Security Groups**: instances के लिए stateful firewalls
- **Network ACLs**: subnets के लिए stateless firewalls
- **Web Application Firewall (WAF)**: web exploits से सुरक्षा
- **DDoS Protection**: Shield, Cloud Armor, DDoS Protection

### डेटा संरक्षण
- **Encryption at Rest**: KMS, customer-managed keys
- **Encryption in Transit**: TLS/SSL, HTTPS
- **Key Management**: HSM, key rotation, audit trails
- **Secrets Management**: Secrets Manager, Key Vault

### अनुपालन और गवर्नेंस
- **Certifications**: SOC 2, ISO 27001, HIPAA, PCI-DSS, GDPR
- **Tools**: policy enforcement, compliance reporting, audit logs
- **Frameworks**: Cloud Security Alliance, NIST CSF

## क्लाउड में DevOps

### CI/CD सेवाएँ
- **AWS**: CodePipeline, CodeBuild, CodeDeploy
- **Azure**: Azure DevOps, GitHub Actions
- **GCP**: Cloud Build, Cloud Deploy
- **Third-party**: Jenkins, CircleCI, GitLab CI

### Infrastructure as Code (IaC)
- **Terraform**: multi-cloud, declarative, state management
- **CloudFormation**: AWS native, YAML/JSON templates
- **ARM Templates**: Azure native
- **Deployment Manager**: GCP native
- **Pulumi**: programming languages का उपयोग करके infrastructure
- **लाभ**: version control, repeatability, documentation

### Configuration Management
- **Ansible**: agentless, YAML playbooks
- **Chef**: Ruby-based, mature ecosystem
- **Puppet**: declarative, strong reporting
- **SaltStack**: fast, Python-based

### Monitoring and Observability
- **Metrics**: CloudWatch, Cloud Monitoring, Azure Monitor
- **Logging**: CloudWatch Logs, Cloud Logging, Log Analytics
- **Tracing**: X-Ray, Cloud Trace, Application Insights
- **Dashboards**: CloudWatch Dashboards, Cloud Console
- **Alerting**: SNS, Cloud Monitoring alerts, Action Groups

### Container Orchestration
- **Kubernetes**: industry standard orchestration
- **Managed Services**: EKS, AKS, GKE
- **Service Mesh**: Istio, Linkerd (traffic management, security)
- **GitOps**: ArgoCD, Flux (declarative deployments)

## लागत प्रबंधन

### मूल्य निर्धारण मॉडल
- **Pay-as-you-go**: जितना उपयोग करें, उतना भुगतान करें
- **Reserved Instances**: 1-3 वर्ष की प्रतिबद्धताएँ, महत्वपूर्ण छूट
- **Spot Instances**: unused capacity के लिए बोली लगाएँ, ये बाधित हो सकती हैं
- **Savings Plans**: flexible commitment pricing
- **Free Tier**: नए accounts के लिए सीमित निःशुल्क उपयोग

### लागत अनुकूलन रणनीतियाँ
- **Right-sizing**: workload की आवश्यकताओं के अनुसार instance types चुनें
- **Auto-scaling**: demand के आधार पर scale करें
- **Reserved Capacity**: steady-state workloads के लिए प्रतिबद्ध हों
- **Spot Usage**: fault-tolerant, flexible workloads के लिए उपयोग करें
- **Storage Tiers**: कम उपयोग वाले data को सस्ते tiers में ले जाएँ
- **Cleanup**: unused resources, snapshots, AMIs हटाएँ

### लागत प्रबंधन उपकरण
- **AWS**: Cost Explorer, Budgets, Trusted Advisor
- **Azure**: Cost Management, Advisor
- **GCP**: Billing reports, Recommender
- **Third-party**: CloudHealth, CloudCheckr, Datadog

## उच्च उपलब्धता और आपदा पुनर्प्राप्ति

### उपलब्धता की अवधारणाएँ
- **Availability Zones**: region के भीतर भौतिक रूप से अलग data centers
- **Regions**: कई AZs वाले भौगोलिक क्षेत्र
- **Edge Locations**: वैश्विक CDN cache locations

### HA रणनीतियाँ
- **Multi-AZ**: availability zones में deployment करें
- **Auto-healing**: failed instances को स्वतः बदलें
- **Load Balancing**: traffic को स्वस्थ instances में वितरित करें
- **Database Replication**: Multi-AZ deployments, read replicas

### आपदा पुनर्प्राप्ति रणनीतियाँ
- **Backup and Restore**: आवधिक backups, आवश्यकता होने पर restore (सबसे कम लागत)
- **Pilot Light**: core elements चलते रहते हैं, और आपदा के दौरान scale up किए जाते हैं
- **Warm Standby**: scaled-down version हमेशा चलता रहता है
- **Multi-Site Active/Active**: कई regions में पूर्ण production (सबसे अधिक लागत)

### RTO और RPO
- **Recovery Time Objective (RTO)**: अधिकतम स्वीकार्य downtime
- **Recovery Point Objective (RPO)**: अधिकतम स्वीकार्य data loss
- **रणनीति चयन**: business requirements और budget के आधार पर

## उभरते रुझान

### Edge Computing
- data को source के अधिक निकट process करें
- **सेवाएँ**: AWS Outposts, Wavelength, Azure Edge, Cloud CDN
- **उपयोग के मामले**: IoT, real-time analytics, low-latency applications

### Multi-Cloud और Hybrid Cloud
- vendor lock-in से बचें
- best-of-breed services का लाभ उठाएँ
- **उपकरण**: Terraform, Anthos, Arc, CloudHealth

### AI/ML सेवाएँ
- pre-trained models: vision, speech, language
- custom model training: SageMaker, Vertex AI, Azure ML
- MLOps: model deployment, monitoring, governance

### Quantum Computing
- **सेवाएँ**: AWS Braket, Azure Quantum
- **स्थिति**: प्रारंभिक चरण, प्रायोगिक
- **संभावना**: cryptography, optimization, drug discovery

### Sustainable Cloud
- carbon footprint tracking
- renewable energy commitments
- efficient resource utilization
- green architecture patterns

