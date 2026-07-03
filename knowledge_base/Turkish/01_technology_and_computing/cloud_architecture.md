# Bulut Mimarisi

## Bulut Bilişimin Temelleri

### Bulut Bilişim Nedir?
İnternet üzerinden, kullandıkça öde fiyatlandırmasıyla sunulan bilişim kaynaklarının (sunucular, depolama, veritabanları, ağ, yazılım) talep üzerine teslim edilmesidir.

### Temel Özellikler (NIST Tanımı)
- **On-Demand Self-Service**: Kaynakları insan etkileşimi olmadan sağlama
- **Broad Network Access**: Ağ üzerinden standart mekanizmalarla erişilebilir olma
- **Resource Pooling**: Dinamik atamaya sahip çok kiracılı model
- **Rapid Elasticity**: Hızlı şekilde dışa ve içe ölçeklenebilme
- **Measured Service**: Kaynak kullanımının izlenmesi ve faturalandırılması

### Bulut Dağıtım Modelleri
- **Public Cloud**: Sağlayıcılara ait, paylaşımlı altyapı (AWS, Azure, GCP)
- **Private Cloud**: Tek bir kuruma ayrılmış ortam (on-premises veya barındırılan)
- **Hybrid Cloud**: Public ve private cloud birleşimi
- **Multi-Cloud**: Birden fazla public cloud sağlayıcısının kullanılması
- **Community Cloud**: Ortak ihtiyaçları olan kuruluşlar arasında paylaşılan bulut

### Hizmet Modelleri

#### Infrastructure as a Service (IaaS)
- **Provides**: Sanal makineler, depolama, ağlar, işletim sistemleri
- **Examples**: AWS EC2, Google Compute Engine, Azure VMs
- **Use Cases**: Lift-and-shift geçişleri, geliştirme ortamları, yüksek kontrol gereksinimleri

#### Platform as a Service (PaaS)
- **Provides**: Geliştirme platformları, veritabanları, middleware
- **Examples**: Heroku, Google App Engine, AWS Elastic Beanstalk
- **Use Cases**: Uygulama geliştirme, API dağıtımı, microservices

#### Software as a Service (SaaS)
- **Provides**: İnternet üzerinden tam uygulamalar
- **Examples**: Salesforce, Google Workspace, Microsoft 365, Slack
- **Use Cases**: E-posta, CRM, iş birliği, iş uygulamaları

#### Function as a Service (FaaS) / Serverless
- **Provides**: Olay odaklı işlev çalıştırma
- **Examples**: AWS Lambda, Azure Functions, Google Cloud Functions
- **Use Cases**: Olay işleme, API'ler, zamanlanmış görevler, gerçek zamanlı işleme

## Başlıca Bulut Sağlayıcıları

### Amazon Web Services (AWS)
- **Market Share**: ~32% (en büyük sağlayıcı)
- **Key Services**:
  - Compute: EC2, Lambda, ECS, EKS
  - Storage: S3, EBS, Glacier
  - Database: RDS, DynamoDB, Aurora
  - Networking: VPC, Route 53, CloudFront
  - AI/ML: SageMaker, Rekognition, Comprehend

### Microsoft Azure
- **Market Share**: ~23%
- **Strengths**: Kurumsal entegrasyon, hybrid cloud, Microsoft ekosistemi
- **Key Services**:
  - Compute: Virtual Machines, Azure Functions, AKS
  - Storage: Blob Storage, Disk Storage
  - Database: SQL Database, Cosmos DB
  - Networking: Virtual Network, Traffic Manager
  - AI/ML: Azure ML, Cognitive Services

### Google Cloud Platform (GCP)
- **Market Share**: ~10%
- **Strengths**: Veri analitiği, AI/ML, Kubernetes
- **Key Services**:
  - Compute: Compute Engine, Cloud Functions, GKE
  - Storage: Cloud Storage, Persistent Disk
  - Database: Cloud SQL, Firestore, Bigtable
  - Analytics: BigQuery, Dataflow, Pub/Sub
  - AI/ML: Vertex AI, AutoML

### Diğer Sağlayıcılar
- **IBM Cloud**: Kurumsal odak, Watson AI
- **Oracle Cloud**: Veritabanı iş yükleri, kurumsal uygulamalar
- **Alibaba Cloud**: Asya-Pasifik'te baskın oyuncu
- **DigitalOcean**: Geliştirici dostu, sadeleştirilmiş teklifler

## Bulut Mimari Kalıpları

### Well-Architected Framework İlkeleri

#### Operasyonel Mükemmellik
- Operasyonları otomatikleştir
- Sık ve geri alınabilir değişiklikler yap
- Süreçleri sürekli iyileştir
- Arızaları öngör

#### Güvenlik
- Güçlü bir kimlik temeli kur
- İzlenebilirliği etkinleştir
- Tüm katmanlarda güvenlik uygula
- Güvenlik için en iyi uygulamaları otomatikleştir
- Veriyi aktarımda ve depoda koru

#### Güvenilirlik
- Kurtarma prosedürlerini test et
- Arızalardan otomatik olarak kurtul
- Erişilebilirlik için yatay ölçeklen
- Kapasiteyi tahmine dayalı yönetmeyi bırak
- Değişikliği otomasyon içinde yönet

#### Performans Verimliliği
- Gelişmiş teknolojileri demokratikleştir
- Dakikalar içinde küresel ölçekte hizmet ver
- Serverless mimarileri kullan
- Daha sık deney yap
- Mechanical sympathy ilkesini dikkate al

#### Maliyet Optimizasyonu
- Tüketime dayalı modeli benimse
- Genel verimliliği ölç
- Ayrıştırıcı olmayan işler için para harcamayı bırak
- Harcamaları analiz et ve ilişkilendir
- Yönetilen hizmetleri kullan

### Yaygın Mimari Kalıplar

#### Microservices Mimarisi
- Uygulamaları küçük, bağımsız hizmetlere ayır
- Her hizmet kendi verisine ve mantığına sahip olur
- API'ler (REST, gRPC, messaging) üzerinden iletişim kurar
- Bağımsız olarak dağıtılır
- **Benefits**: Ölçeklenebilirlik, hata izolasyonu, teknoloji çeşitliliği
- **Challenges**: Dağıtık karmaşıklık, veri tutarlılığı, izleme

#### Event-Driven Mimari
- Bileşenler olaylar üzerinden iletişim kurar
- Üreticiler olay yayımlar, tüketiciler tepki verir
- **Patterns**: Event sourcing, CQRS, pub/sub
- **Technologies**: Kafka, SNS/SQS, EventBridge, Pub/Sub
- **Benefits**: Gevşek bağlılık, ölçeklenebilirlik, gerçek zamanlı işleme

#### Serverless Mimari
- Sunucu yönetimi gerekmez
- Çalıştırma başına ödeme yapılır
- Otomatik ölçeklenir
- **Components**: Functions, API Gateway, managed services
- **Benefits**: Maliyet verimliliği, daha az operasyon yükü, hızlı dağıtım
- **Considerations**: Cold start'lar, vendor lock-in, yürütme sınırları

#### Katmanlı Mimari (N-Tier)
- Sunum katmanı (UI)
- Uygulama/iş mantığı katmanı
- Veri erişim katmanı
- Veritabanı katmanı
- **Benefits**: Sorumlulukların ayrılması, sürdürülebilirlik
- **Common**: 3 katmanlı web uygulamaları

#### Space-Based Mimari
- Dağıtık veriyle yüksek eşzamanlılığı yönetir
- Sunucular arasında sanallaştırılmış bellek kullanır
- İşleme düğümleri bağımsız ölçeklenir
- **Use Cases**: Yüksek hacimli, düşük gecikmeli uygulamalar

## Compute Hizmetleri

### Virtual Machines
- **Types**: General purpose, compute optimized, memory optimized, GPU
- **Pricing**: On-demand, reserved instances, spot instances
- **Management**: Auto-scaling groups, load balancers
- **Best Practices**: Right-sizing, etiketleme, izleme, yamalama

### Containers
- **Docker**: Konteyner çalışma zamanı standardı
- **Orchestration**: Kubernetes (EKS, AKS, GKE), ECS, Fargate
- **Benefits**: Taşınabilirlik, verimlilik, tutarlılık
- **Registry**: ECR, GCR, ACR, Docker Hub

### Serverless Functions
- **Execution Model**: Olay tetiklemeli, stateless
- **Limits**: Çalıştırma süresi, bellek, eşzamanlı çalıştırma sayısı
- **Use Cases**: API'ler, dosya işleme, zamanlanmış işler, IoT back-end'leri
- **Monitoring**: Çağrı sayısı, hatalar, süre, cold start'lar

## Depolama Çözümleri

### Object Storage
- **Characteristics**: Düz yapı, metadata, HTTP erişimi
- **Examples**: AWS S3, Google Cloud Storage, Azure Blob
- **Use Cases**: Statik varlıklar, yedekler, data lake'ler, arşivler
- **Storage Classes**: Hot, cool, cold, archive (farklı maliyet/erişim düzeyleri)

### Block Storage
- **Characteristics**: Ham disk birimleri, VM'lere bağlı çalışır
- **Examples**: AWS EBS, Google Persistent Disk, Azure Disks
- **Use Cases**: Veritabanları, önyükleme diskleri, yüksek performans gereksinimleri
- **Types**: SSD, HDD, provisioned IOPS

### File Storage
- **Characteristics**: Paylaşımlı dosya sistemleri, NFS/SMB protokolleri
- **Examples**: AWS EFS, Google Filestore, Azure Files
- **Use Cases**: İçerik yönetimi, paylaşılan yapılandırmalar, lift-and-shift senaryoları

### Archive Storage
- **Characteristics**: En düşük maliyet, erişim gecikmeleri
- **Examples**: S3 Glacier, Azure Archive Storage
- **Use Cases**: Uyumluluk, uzun süreli yedekleme, tarihsel veri

## Veritabanı Hizmetleri

### Managed Relational Databases
- **Services**: AWS RDS/Aurora, Google Cloud SQL, Azure SQL Database
- **Features**: Otomatik yedekleme, yamalama, ölçekleme, çoğaltma
- **Engines**: MySQL, PostgreSQL, MariaDB, Oracle, SQL Server

### NoSQL Databases
- **Document**: DocumentDB, Firestore, Cosmos DB
- **Key-Value**: DynamoDB, Redis Cache
- **Wide-Column**: Bigtable, Cassandra (managed)
- **Graph**: Neptune, Cosmos DB (graph API)

### Data Warehousing
- **Services**: Snowflake, Redshift, BigQuery, Synapse
- **Characteristics**: Sütun odaklı depolama, MPP mimarisi
- **Use Cases**: Analitik, BI, büyük ölçekli veri analizi

### Caching Services
- **In-Memory**: ElastiCache (Redis/Memcached), Cloud Memorystore
- **CDN Caching**: CloudFront, Cloud CDN, Azure CDN
- **Use Cases**: Session storage, sorgu önbellekleme, içerik dağıtımı

## Ağ

### Virtual Networks
- **VPC/VNet**: Yalıtılmış ağ ortamları
- **Subnets**: Public (internete açık), private (yalnızca iç erişim)
- **IP Addressing**: CIDR blokları, IPv4/IPv6
- **Route Tables**: Trafik akışını kontrol eder

### Load Balancing
- **Types**: Application (L7), Network (L4), Gateway
- **Features**: Health check'ler, SSL sonlandırma, sticky session'lar
- **Services**: ELB/ALB/NLB, Cloud Load Balancing, Azure Load Balancer

### Content Delivery Networks (CDN)
- **Purpose**: İçeriği edge lokasyonlarda önbelleğe alır
- **Benefits**: Daha düşük gecikme, origin üzerinde daha az yük, küresel dağıtım
- **Services**: CloudFront, Cloud CDN, Azure CDN, Akamai

### DNS Services
- **Functions**: Alan adı kaydı, yönlendirme, health check'ler
- **Services**: Route 53, Cloud DNS, Azure DNS
- **Routing Policies**: Simple, weighted, latency-based, geolocation, failover

### Bağlantı Seçenekleri
- **Internet Gateway**: Public internet erişimi
- **NAT Gateway**: Private subnet'lerden dışarı yönlü erişim
- **VPN**: On-premises ortamlara şifreli tüneller
- **Direct Connect/ExpressRoute**: Ayrılmış özel bağlantılar
- **VPC Peering**: Hesap içi/hesaplar arası VPC bağlantısı

## Bulutta Güvenlik

### Shared Responsibility Model
- **Provider Responsibility**: Bulut altyapısının güvenliği (security OF the cloud)
- **Customer Responsibility**: Bulut içindeki verinin, uygulamaların ve erişimin güvenliği (security IN the cloud)
- **Varies By Service**: Hizmet ne kadar yönetilirse sağlayıcı sorumluluğu da o kadar artar

### Identity and Access Management (IAM)
- **Users**: Bireysel kimlikler
- **Groups**: Kullanıcı koleksiyonları
- **Roles**: Hizmetler/kullanıcılar için geçici kimlik bilgileri
- **Policies**: Yetkileri tanımlayan JSON belgeleri
- **Principles**: En az ayrıcalık, görevlerin ayrılığı

### Ağ Güvenliği
- **Security Groups**: Instance'lar için stateful firewall'lar
- **Network ACLs**: Subnet'ler için stateless firewall'lar
- **Web Application Firewall (WAF)**: Web saldırılarına karşı koruma
- **DDoS Protection**: Shield, Cloud Armor, DDoS Protection

### Veri Koruma
- **Encryption at Rest**: KMS, müşteri tarafından yönetilen anahtarlar
- **Encryption in Transit**: TLS/SSL, HTTPS
- **Key Management**: HSM, anahtar döndürme, denetim izleri
- **Secrets Management**: Secrets Manager, Key Vault

### Uyumluluk ve Yönetişim
- **Certifications**: SOC 2, ISO 27001, HIPAA, PCI-DSS, GDPR
- **Tools**: İlke zorlaması, uyumluluk raporlaması, denetim günlükleri
- **Frameworks**: Cloud Security Alliance, NIST CSF

## Bulutta DevOps

### CI/CD Services
- **AWS**: CodePipeline, CodeBuild, CodeDeploy
- **Azure**: Azure DevOps, GitHub Actions
- **GCP**: Cloud Build, Cloud Deploy
- **Third-party**: Jenkins, CircleCI, GitLab CI

### Infrastructure as Code (IaC)
- **Terraform**: Multi-cloud, declarative, state management
- **CloudFormation**: AWS yerel çözümü, YAML/JSON şablonları
- **ARM Templates**: Azure yerel çözümü
- **Deployment Manager**: GCP yerel çözümü
- **Pulumi**: Programlama dilleriyle altyapı tanımı
- **Benefits**: Sürüm kontrolü, tekrarlanabilirlik, dokümantasyon

### Configuration Management
- **Ansible**: Agentsız, YAML playbook'ları
- **Chef**: Ruby tabanlı, olgun ekosistem
- **Puppet**: Declarative, güçlü raporlama
- **SaltStack**: Hızlı, Python tabanlı

### Monitoring and Observability
- **Metrics**: CloudWatch, Cloud Monitoring, Azure Monitor
- **Logging**: CloudWatch Logs, Cloud Logging, Log Analytics
- **Tracing**: X-Ray, Cloud Trace, Application Insights
- **Dashboards**: CloudWatch Dashboards, Cloud Console
- **Alerting**: SNS, Cloud Monitoring alerts, Action Groups

### Container Orchestration
- **Kubernetes**: Endüstri standardı orkestrasyon
- **Managed Services**: EKS, AKS, GKE
- **Service Mesh**: Istio, Linkerd (trafik yönetimi, güvenlik)
- **GitOps**: ArgoCD, Flux (declarative deployments)

## Maliyet Yönetimi

### Fiyatlandırma Modelleri
- **Pay-as-you-go**: Yalnızca kullandığın kadar öde
- **Reserved Instances**: 1-3 yıllık taahhüt, önemli indirimler
- **Spot Instances**: Kullanılmayan kapasite için teklif verme, kesintiye uğrayabilir
- **Savings Plans**: Esnek taahhüt bazlı fiyatlandırma
- **Free Tier**: Yeni hesaplar için sınırlı ücretsiz kullanım

### Maliyet Optimizasyon Stratejileri
- **Right-sizing**: Instance tiplerini iş yükü ihtiyacına göre eşleştirme
- **Auto-scaling**: Talebe göre ölçekleme
- **Reserved Capacity**: Sürekli çalışan iş yükleri için taahhüt verme
- **Spot Usage**: Hata toleranslı, esnek iş yüklerinde kullanma
- **Storage Tiers**: Seyrek kullanılan veriyi daha ucuz katmanlara taşıma
- **Cleanup**: Kullanılmayan kaynakları, snapshot'ları ve AMI'leri silme

### Cost Management Tools
- **AWS**: Cost Explorer, Budgets, Trusted Advisor
- **Azure**: Cost Management, Advisor
- **GCP**: Faturalama raporları, Recommender
- **Third-party**: CloudHealth, CloudCheckr, Datadog

## High Availability ve Disaster Recovery

### Erişilebilirlik Kavramları
- **Availability Zones**: Bölge içindeki fiziksel olarak ayrı veri merkezleri
- **Regions**: Birden fazla AZ içeren coğrafi alanlar
- **Edge Locations**: Dünya geneline yayılmış CDN önbellek noktaları

### HA Stratejileri
- **Multi-AZ**: Availability zone'lara yayılmış dağıtım
- **Auto-healing**: Arızalı instance'ları otomatik değiştirme
- **Load Balancing**: Trafiği sağlıklı instance'lara dağıtma
- **Database Replication**: Multi-AZ kurulumlar, read replica'lar

### Disaster Recovery Stratejileri
- **Backup and Restore**: Periyodik yedekler, gerektiğinde geri yükleme (en düşük maliyet)
- **Pilot Light**: Temel bileşenler çalışır durumda, afet anında büyütülür
- **Warm Standby**: Sürekli çalışan küçültülmüş sürüm
- **Multi-Site Active/Active**: Birden fazla bölgede tam üretim ortamı (en yüksek maliyet)

### RTO ve RPO
- **Recovery Time Objective (RTO)**: Kabul edilebilir azami kesinti süresi
- **Recovery Point Objective (RPO)**: Kabul edilebilir azami veri kaybı
- **Strategy Selection**: İş gereksinimleri ve bütçeye göre belirlenir

## Yükselen Eğilimler

### Edge Computing
- Veriyi kaynağa daha yakın yerde işler
- **Services**: AWS Outposts, Wavelength, Azure Edge, Cloud CDN
- **Use Cases**: IoT, gerçek zamanlı analitik, düşük gecikmeli uygulamalar

### Multi-Cloud ve Hybrid Cloud
- Vendor lock-in riskini azaltır
- Her sağlayıcının en iyi hizmetlerinden yararlanır
- **Tools**: Terraform, Anthos, Arc, CloudHealth

### AI/ML Services
- Önceden eğitilmiş modeller: Vision, speech, language
- Özel model eğitimi: SageMaker, Vertex AI, Azure ML
- MLOps: Model dağıtımı, izleme, yönetişim

### Quantum Computing
- **Services**: AWS Braket, Azure Quantum
- **Status**: Erken aşama, deneysel
- **Potential**: Kriptografi, optimizasyon, ilaç keşfi

### Sürdürülebilir Bulut
- Karbon ayak izi takibi
- Yenilenebilir enerji taahhütleri
- Verimli kaynak kullanımı
- Yeşil mimari kalıpları
