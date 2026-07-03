# Bulut Mimarisi

## Bulut Bilişimin Temelleri

### Bulut Bilişim Nedir?
İnternet üzerinden, kullandıkça öde fiyatlandırmasıyla sunulan bilişim kaynaklarının (sunucular, depolama, veritabanları, ağ, yazılım) talep üzerine sağlanmasıdır.

### Temel Özellikler (NIST Tanımı)
- **İsteğe Bağlı Self Servis**: Kaynakları insan etkileşimi olmadan sağlama
- **Geniş Ağ Erişimi**: Ağ üzerinden standart mekanizmalarla erişilebilir olma
- **Kaynak Havuzu**: Dinamik atamaya sahip çok kiracılı model
- **Hızlı Esneklik**: Hızlı biçimde ölçeği büyütüp küçültebilme
- **Ölçülen Hizmet**: Kaynak kullanımının izlenmesi ve faturalandırılması

### Bulut Dağıtım Modelleri
- **Genel Bulut**: Sağlayıcılara ait, paylaşımlı altyapı (AWS, Azure, GCP)
- **Özel Bulut**: Tek bir kuruma ayrılmış ortam (on-premises veya barındırılan)
- **Hibrit Bulut**: Genel ve özel bulutların birleşimi
- **Çoklu Bulut**: Birden fazla genel bulut sağlayıcısının kullanılması
- **Topluluk Bulutu**: Ortak ihtiyaçları olan kuruluşlar arasında paylaşılan bulut

### Hizmet Modelleri

#### Infrastructure as a Service (IaaS)
- **Sunar**: Sanal makineler, depolama, ağlar, işletim sistemleri
- **Örnekler**: AWS EC2, Google Compute Engine, Azure VMs
- **Kullanım Alanları**: Lift-and-shift geçişleri, geliştirme ortamları, yüksek kontrol gereksinimleri

#### Platform as a Service (PaaS)
- **Sunar**: Geliştirme platformları, veritabanları, ara katman yazılımları
- **Örnekler**: Heroku, Google App Engine, AWS Elastic Beanstalk
- **Kullanım Alanları**: Uygulama geliştirme, API dağıtımı, mikroservisler

#### Software as a Service (SaaS)
- **Sunar**: İnternet üzerinden tam işlevli uygulamalar
- **Örnekler**: Salesforce, Google Workspace, Microsoft 365, Slack
- **Kullanım Alanları**: E-posta, CRM, iş birliği, iş uygulamaları

#### Function as a Service (FaaS) / Serverless
- **Sunar**: Olay odaklı işlev çalıştırma
- **Örnekler**: AWS Lambda, Azure Functions, Google Cloud Functions
- **Kullanım Alanları**: Olay işleme, API'ler, zamanlanmış görevler, gerçek zamanlı işleme

## Başlıca Bulut Sağlayıcıları

### Amazon Web Services (AWS)
- **Pazar Payı**: ~32% (en büyük sağlayıcı)
- **Temel Hizmetler**:
  - Hesaplama: EC2, Lambda, ECS, EKS
  - Depolama: S3, EBS, Glacier
  - Veritabanı: RDS, DynamoDB, Aurora
  - Ağ: VPC, Route 53, CloudFront
  - AI/ML: SageMaker, Rekognition, Comprehend

### Microsoft Azure
- **Pazar Payı**: ~23%
- **Güçlü Yönleri**: Kurumsal entegrasyon, hibrit bulut, Microsoft ekosistemi
- **Temel Hizmetler**:
  - Hesaplama: Virtual Machines, Azure Functions, AKS
  - Depolama: Blob Storage, Disk Storage
  - Veritabanı: SQL Database, Cosmos DB
  - Ağ: Virtual Network, Traffic Manager
  - AI/ML: Azure ML, Cognitive Services

### Google Cloud Platform (GCP)
- **Pazar Payı**: ~10%
- **Güçlü Yönleri**: Veri analitiği, AI/ML, Kubernetes
- **Temel Hizmetler**:
  - Hesaplama: Compute Engine, Cloud Functions, GKE
  - Depolama: Cloud Storage, Persistent Disk
  - Veritabanı: Cloud SQL, Firestore, Bigtable
  - Analitik: BigQuery, Dataflow, Pub/Sub
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
- İleri teknolojileri erişilebilir kıl
- Dakikalar içinde küresel ölçekte hizmet ver
- Sunucusuz mimarileri kullan
- Daha sık deney yap
- Donanımın çalışma biçimine uyumlu tasarımı dikkate al

#### Maliyet Optimizasyonu
- Tüketime dayalı modeli benimse
- Genel verimliliği ölç
- Fark yaratmayan işler için para harcamayı bırak
- Harcamaları analiz et ve ilişkilendir
- Yönetilen hizmetleri kullan

### Yaygın Mimari Kalıplar

#### Mikroservis Mimarisi
- Uygulamaları küçük, bağımsız hizmetlere ayır
- Her hizmet kendi verisine ve iş mantığına sahip olur
- API'ler üzerinden iletişim kurar (REST, gRPC, mesajlaşma)
- Bağımsız olarak dağıtılır
- **Avantajlar**: Ölçeklenebilirlik, hata yalıtımı, teknoloji çeşitliliği
- **Zorluklar**: Dağıtık sistem karmaşıklığı, veri tutarlılığı, izleme

#### Olay Odaklı Mimari
- Bileşenler olaylar üzerinden iletişim kurar
- Üreticiler olay yayımlar, tüketiciler bunlara tepki verir
- **Kalıplar**: Event sourcing, CQRS, pub/sub
- **Teknolojiler**: Kafka, SNS/SQS, EventBridge, Pub/Sub
- **Avantajlar**: Gevşek bağlılık, ölçeklenebilirlik, gerçek zamanlı işleme

#### Sunucusuz Mimari
- Sunucu yönetimi gerekmez
- Çalıştırma başına ödeme yapılır
- Otomatik ölçeklenir
- **Bileşenler**: Functions, API Gateway, yönetilen hizmetler
- **Avantajlar**: Maliyet verimliliği, daha az operasyon yükü, hızlı dağıtım
- **Dikkat Edilmesi Gerekenler**: Cold start'lar, üreticiye bağımlılık, çalıştırma sınırları

#### Katmanlı Mimari (N-Tier)
- Sunum katmanı (UI)
- Uygulama/iş mantığı katmanı
- Veri erişim katmanı
- Veritabanı katmanı
- **Avantajlar**: Sorumlulukların ayrılması, sürdürülebilirlik
- **Yaygın Kullanım**: 3 katmanlı web uygulamaları

#### Space-Based Mimari
- Dağıtık veriyle yüksek eşzamanlılığı yönetir
- Sunucular arasında sanallaştırılmış bellek kullanır
- İşleme düğümleri bağımsız ölçeklenir
- **Kullanım Alanları**: Yüksek hacimli, düşük gecikmeli uygulamalar

## Hesaplama Hizmetleri

### Sanal Makineler
- **Türler**: Genel amaçlı, hesaplama için optimize edilmiş, bellek için optimize edilmiş, GPU
- **Fiyatlandırma**: On-demand, reserved instances, spot instances
- **Yönetim**: Otomatik ölçeklendirme grupları, yük dengeleyiciler
- **En İyi Uygulamalar**: Doğru boyutlandırma, etiketleme, izleme, yamalama

### Konteynerler
- **Docker**: Konteyner çalışma zamanı standardı
- **Orkestrasyon**: Kubernetes (EKS, AKS, GKE), ECS, Fargate
- **Avantajlar**: Taşınabilirlik, verimlilik, tutarlılık
- **Kayıt Depoları**: ECR, GCR, ACR, Docker Hub

### Sunucusuz Fonksiyonlar
- **Çalıştırma Modeli**: Olay tetiklemeli, durum tutmayan
- **Sınırlar**: Çalıştırma süresi, bellek, eşzamanlı çalıştırma sayısı
- **Kullanım Alanları**: API'ler, dosya işleme, zamanlanmış işler, IoT arka uçları
- **İzleme**: Çağrı sayısı, hatalar, süre, cold start'lar

## Depolama Çözümleri

### Nesne Depolama
- **Özellikler**: Düz yapı, üstveri, HTTP erişimi
- **Örnekler**: AWS S3, Google Cloud Storage, Azure Blob
- **Kullanım Alanları**: Statik varlıklar, yedekler, veri gölleri, arşivler
- **Depolama Sınıfları**: Hot, cool, cold, archive (farklı maliyet/erişim düzeyleri)

### Blok Depolama
- **Özellikler**: Ham disk birimleri, sanal makinelere bağlanır
- **Örnekler**: AWS EBS, Google Persistent Disk, Azure Disks
- **Kullanım Alanları**: Veritabanları, önyükleme diskleri, yüksek performans gereksinimleri
- **Türler**: SSD, HDD, provisioned IOPS

### Dosya Depolama
- **Özellikler**: Paylaşımlı dosya sistemleri, NFS/SMB protokolleri
- **Örnekler**: AWS EFS, Google Filestore, Azure Files
- **Kullanım Alanları**: İçerik yönetimi, paylaşılan yapılandırmalar, lift-and-shift senaryoları

### Arşiv Depolama
- **Özellikler**: En düşük maliyet, erişimde gecikme
- **Örnekler**: S3 Glacier, Azure Archive Storage
- **Kullanım Alanları**: Uyumluluk, uzun süreli yedekleme, tarihsel veri

## Veritabanı Hizmetleri

### Yönetilen İlişkisel Veritabanları
- **Hizmetler**: AWS RDS/Aurora, Google Cloud SQL, Azure SQL Database
- **Özellikler**: Otomatik yedekleme, yamalama, ölçekleme, çoğaltma
- **Motorlar**: MySQL, PostgreSQL, MariaDB, Oracle, SQL Server

### NoSQL Veritabanları
- **Belge**: DocumentDB, Firestore, Cosmos DB
- **Anahtar-Değer**: DynamoDB, Redis Cache
- **Geniş Sütunlu**: Bigtable, Cassandra (managed)
- **Graf**: Neptune, Cosmos DB (graph API)

### Veri Ambarı Çözümleri
- **Hizmetler**: Snowflake, Redshift, BigQuery, Synapse
- **Özellikler**: Sütun odaklı depolama, MPP mimarisi
- **Kullanım Alanları**: Analitik, BI, büyük ölçekli veri analizi

### Önbellek Hizmetleri
- **Bellek İçi**: ElastiCache (Redis/Memcached), Cloud Memorystore
- **CDN Önbelleği**: CloudFront, Cloud CDN, Azure CDN
- **Kullanım Alanları**: Oturum depolama, sorgu önbellekleme, içerik dağıtımı

## Ağ

### Sanal Ağlar
- **VPC/VNet**: Yalıtılmış ağ ortamları
- **Alt Ağlar**: Public (internete açık), private (yalnızca iç erişim)
- **IP Adresleme**: CIDR blokları, IPv4/IPv6
- **Yönlendirme Tabloları**: Trafik akışını kontrol eder

### Yük Dengeleme
- **Türler**: Application (L7), Network (L4), Gateway
- **Özellikler**: Health check'ler, SSL sonlandırma, sticky session'lar
- **Hizmetler**: ELB/ALB/NLB, Cloud Load Balancing, Azure Load Balancer

### İçerik Dağıtım Ağları (CDN)
- **Amaç**: İçeriği uç noktalardaki konumlarda önbelleğe almak
- **Avantajlar**: Daha düşük gecikme, origin üzerinde daha az yük, küresel dağıtım
- **Hizmetler**: CloudFront, Cloud CDN, Azure CDN, Akamai

### DNS Hizmetleri
- **İşlevler**: Alan adı kaydı, yönlendirme, health check'ler
- **Hizmetler**: Route 53, Cloud DNS, Azure DNS
- **Yönlendirme İlkeleri**: Simple, weighted, latency-based, geolocation, failover

### Bağlantı Seçenekleri
- **Internet Gateway**: Genel internet erişimi
- **NAT Gateway**: Private subnet'lerden dışarı yönlü erişim
- **VPN**: On-premises ortamlara şifreli tüneller
- **Direct Connect/ExpressRoute**: Ayrılmış özel bağlantılar
- **VPC Peering**: Hesap içi ve hesaplar arası VPC bağlantısı

## Bulutta Güvenlik

### Paylaşılan Sorumluluk Modeli
- **Sağlayıcının Sorumluluğu**: Bulut altyapısının güvenliği (security OF the cloud)
- **Müşterinin Sorumluluğu**: Bulut içindeki veri, uygulama ve erişimin güvenliği (security IN the cloud)
- **Hizmete Göre Değişir**: Hizmet ne kadar yönetilirse sağlayıcının sorumluluğu da o kadar artar

### Identity and Access Management (IAM)
- **Kullanıcılar**: Bireysel kimlikler
- **Gruplar**: Kullanıcı koleksiyonları
- **Roller**: Hizmetler ve kullanıcılar için geçici kimlik bilgileri
- **İlkeler**: Yetkileri tanımlayan JSON belgeleri
- **Prensipler**: En az ayrıcalık, görevlerin ayrılığı

### Ağ Güvenliği
- **Security Groups**: Instance'lar için stateful firewall'lar
- **Network ACL'ler**: Alt ağlar için stateless firewall'lar
- **Web Application Firewall (WAF)**: Web saldırılarına karşı koruma
- **DDoS Koruması**: Shield, Cloud Armor, DDoS Protection

### Veri Koruma
- **Beklemedeki Şifreleme**: KMS, müşteri tarafından yönetilen anahtarlar
- **Aktarım Sırasında Şifreleme**: TLS/SSL, HTTPS
- **Anahtar Yönetimi**: HSM, anahtar döndürme, denetim izleri
- **Gizli Bilgi Yönetimi**: Secrets Manager, Key Vault

### Uyumluluk ve Yönetişim
- **Sertifikalar**: SOC 2, ISO 27001, HIPAA, PCI-DSS, GDPR
- **Araçlar**: İlke zorlaması, uyumluluk raporlaması, denetim günlükleri
- **Çerçeveler**: Cloud Security Alliance, NIST CSF

## Bulutta DevOps

### CI/CD Hizmetleri
- **AWS**: CodePipeline, CodeBuild, CodeDeploy
- **Azure**: Azure DevOps, GitHub Actions
- **GCP**: Cloud Build, Cloud Deploy
- **Üçüncü Taraf**: Jenkins, CircleCI, GitLab CI

### Infrastructure as Code (IaC)
- **Terraform**: Çoklu bulut, bildirime dayalı yapı, durum yönetimi
- **CloudFormation**: AWS'nin yerel çözümü, YAML/JSON şablonları
- **ARM Templates**: Azure'un yerel çözümü
- **Deployment Manager**: GCP'nin yerel çözümü
- **Pulumi**: Programlama dilleriyle altyapı tanımı
- **Avantajlar**: Sürüm kontrolü, tekrarlanabilirlik, dokümantasyon

### Yapılandırma Yönetimi
- **Ansible**: Agentsız, YAML playbook'ları
- **Chef**: Ruby tabanlı, olgun ekosistem
- **Puppet**: Bildirime dayalı yapı, güçlü raporlama
- **SaltStack**: Hızlı, Python tabanlı

### İzleme ve Gözlemlenebilirlik
- **Metrikler**: CloudWatch, Cloud Monitoring, Azure Monitor
- **Günlükleme**: CloudWatch Logs, Cloud Logging, Log Analytics
- **İz Sürme**: X-Ray, Cloud Trace, Application Insights
- **Gösterge Panelleri**: CloudWatch Dashboards, Cloud Console
- **Uyarılar**: SNS, Cloud Monitoring alerts, Action Groups

### Konteyner Orkestrasyonu
- **Kubernetes**: Endüstri standardı orkestrasyon
- **Yönetilen Hizmetler**: EKS, AKS, GKE
- **Service Mesh**: Istio, Linkerd (trafik yönetimi, güvenlik)
- **GitOps**: ArgoCD, Flux (bildirime dayalı dağıtımlar)

## Maliyet Yönetimi

### Fiyatlandırma Modelleri
- **Pay-as-you-go**: Yalnızca kullandığın kadar öde
- **Reserved Instances**: 1-3 yıllık taahhüt, önemli indirimler
- **Spot Instances**: Kullanılmayan kapasite için teklif verme, kesintiye uğrayabilir
- **Savings Plans**: Esnek taahhüt bazlı fiyatlandırma
- **Free Tier**: Yeni hesaplar için sınırlı ücretsiz kullanım

### Maliyet Optimizasyon Stratejileri
- **Doğru Boyutlandırma**: Instance türlerini iş yükü ihtiyacına göre eşleştirme
- **Otomatik Ölçekleme**: Talebe göre ölçekleme
- **Ayrılmış Kapasite**: Sürekli çalışan iş yükleri için taahhüt verme
- **Spot Kullanımı**: Hata toleranslı, esnek iş yüklerinde kullanma
- **Depolama Katmanları**: Seyrek kullanılan veriyi daha ucuz katmanlara taşıma
- **Temizlik**: Kullanılmayan kaynakları, snapshot'ları ve AMI'leri silme

### Maliyet Yönetimi Araçları
- **AWS**: Cost Explorer, Budgets, Trusted Advisor
- **Azure**: Cost Management, Advisor
- **GCP**: Faturalama raporları, Recommender
- **Üçüncü Taraf**: CloudHealth, CloudCheckr, Datadog

## Yüksek Erişilebilirlik ve Felaket Kurtarma

### Erişilebilirlik Kavramları
- **Availability Zones**: Bölge içindeki fiziksel olarak ayrı veri merkezleri
- **Bölgeler**: Birden fazla AZ içeren coğrafi alanlar
- **Uç Nokta Konumları**: Dünya geneline yayılmış CDN önbellek noktaları

### HA Stratejileri
- **Multi-AZ**: Availability zone'lara yayılmış dağıtım
- **Auto-healing**: Arızalı instance'ları otomatik değiştirme
- **Yük Dengeleme**: Trafiği sağlıklı instance'lara dağıtma
- **Veritabanı Çoğaltma**: Multi-AZ kurulumlar, read replica'lar

### Felaket Kurtarma Stratejileri
- **Yedekleme ve Geri Yükleme**: Periyodik yedekler, gerektiğinde geri yükleme (en düşük maliyet)
- **Pilot Light**: Temel bileşenler çalışır durumda olur, afet anında büyütülür
- **Warm Standby**: Sürekli çalışan küçültülmüş sürüm
- **Çoklu Bölge Active/Active**: Birden fazla bölgede tam üretim ortamı (en yüksek maliyet)

### RTO ve RPO
- **Recovery Time Objective (RTO)**: Kabul edilebilir azami kesinti süresi
- **Recovery Point Objective (RPO)**: Kabul edilebilir azami veri kaybı
- **Strateji Seçimi**: İş gereksinimleri ve bütçeye göre belirlenir

## Yükselen Eğilimler

### Uç Bilişim
- Veriyi kaynağa daha yakın noktalarda işler
- **Hizmetler**: AWS Outposts, Wavelength, Azure Edge, Cloud CDN
- **Kullanım Alanları**: IoT, gerçek zamanlı analitik, düşük gecikmeli uygulamalar

### Çoklu Bulut ve Hibrit Bulut
- Üreticiye bağımlılığı azaltır
- Her sağlayıcının en iyi hizmetlerinden yararlanır
- **Araçlar**: Terraform, Anthos, Arc, CloudHealth

### AI/ML Hizmetleri
- Önceden eğitilmiş modeller: Vision, speech, language
- Özel model eğitimi: SageMaker, Vertex AI, Azure ML
- MLOps: Model dağıtımı, izleme, yönetişim

### Kuantum Bilişim
- **Hizmetler**: AWS Braket, Azure Quantum
- **Durum**: Erken aşama, deneysel
- **Potansiyel**: Kriptografi, optimizasyon, ilaç keşfi

### Sürdürülebilir Bulut
- Karbon ayak izi takibi
- Yenilenebilir enerji taahhütleri
- Verimli kaynak kullanımı
- Yeşil mimari kalıpları
