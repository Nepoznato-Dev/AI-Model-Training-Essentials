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
# Bulut Mimarisi
Bulut bilişim, kuruluşların yazılım oluşturma, dağıtma ve ölçeklendirme biçimini temelden değiştirdi. Fiziksel sunucular satın almak ve bakımını yapmak yerine, talep üzerine bilgi işlem kaynaklarını tedarik edebilir, kullandığınız kadar ödeyebilir ve dakikalar içinde küresel olarak ölçeklendirebilirsiniz. Bu dosya, bilmeniz gereken temel kavramları, mimari kalıpları, hizmetleri ve en iyi uygulamaları kapsar.
---

## Bulut Bilişimin Temelleri
### Bulut Bilişim Nedir?
Kullandıkça öde fiyatlandırmasıyla sunucular, depolama, veritabanları, ağ iletişimi, yazılım gibi bilgi işlem kaynaklarının isteğe bağlı olarak internet üzerinden teslimi.
### NIST Temel Özellikleri
| karakteristik | Anlamı |
|---------------|-----------|
| **İsteğe Bağlı Self Servis** | İnsan etkileşimi olmadan kaynak sağlayın |
| **Geniş Ağ Erişimi** | Ağ üzerinden standart mekanizmalar aracılığıyla kullanılabilir |
| **Kaynak Havuzu** | Çok kiracılı model; dinamik olarak atanan kaynaklar |
| **Hızlı Esneklik** | Hızlı bir şekilde dışa ve içe doğru ölçeklendirin |
| **Ölçülen Hizmet** | Kullanım izleniyor ve faturalandırılıyor |
### Dağıtım Modelleri
| Modeli | Açıklama | Ne Zaman Kullanılmalı |
|----------|----------------|-------------|
| **Genel Bulut** | Sağlayıcılara ait; paylaşılan altyapı (AWS, Azure, GCP) | Çoğu iş yükü; uygun maliyetli |
| **Özel Bulut** | Tek bir kuruluşa adanmış | Mevzuat gereklilikleri, hassas veriler |
| **Hibrit Bulut** | Kamu ve özelin birleşimi | Esneklik + uyumluluk |
| **Çoklu Bulut** | Birden çok genel bulut sağlayıcısını kullanma | Satıcıya bağlı kalmaktan kaçının, türünün en iyisi |
### Hizmet Modelleri
| Modeli | Sağlar | Örnekler | Kullanım Durumları |
|----------|----------|----------|-----------|
| **IaaS** | VM'ler, depolama, ağlar, işletim sistemi | AWS EC2, Azure VM'leri, GCP Compute Engine | Kaldırma ve kaydırma geçişleri, tam kontrol |
| **PaaS** | Geliştirme platformları, veritabanları, ara yazılımlar | Heroku, Google Uygulama Motoru, AWS Elastik Fasulye Sırığı | Uygulama geliştirme, API dağıtımı |
| **SaaS** | Başvuruları internet üzerinden tamamlayın | Salesforce, Google Workspace, Microsoft 365 | E-posta, CRM, işbirliği |
| **FaaS / Sunucusuz** | Olay odaklı fonksiyon yürütme | AWS Lambda, Azure İşlevleri, GCP Bulut İşlevleri | API'ler, olay işleme, zamanlanmış görevler |
---

## Büyük Bulut Sağlayıcıları
| Sağlayıcı | Pazar Payı | Güçlü Yönler |
|----------|----------------|-----------|
| **AWS** | ~%32 | En geniş hizmet kataloğu, en büyük ekosistem |
| **Azure** | ~%23 | Kurumsal entegrasyon, hibrit bulut, Microsoft yığını |
| **GCP** | ~%10 | Veri analizi, AI/ML, Kubernetes |
| **Alibaba Bulutu** | ~%4 | Asya-Pasifik'te Hakim |
| **Oracle Bulutu** | ~%2 | Veritabanı iş yükleri, kurumsal uygulamalar |
| **IBM Bulut** | ~%2 | Kurumsal odaklanma, Watson AI |
| **DigitalOcean** | Niş | Geliştirici dostu, basitleştirilmiş teklifler |
### Hizmet Karşılaştırması (En İyi 3 Sağlayıcı)
| Kategori | AWS | Azure | GCP |
|----------|-----|----------|-----|
| **Hesaplama** | EC2, Lambda, ECS | VM'ler, İşlevler, AKS | Compute Engine, Bulut İşlevleri, GKE |
| **Depolama** | S3, EBS, Buzul | Blob Depolama, Disk Depolama | Bulut Depolama, Kalıcı Disk |
| **Veritabanı** | RDS, DynamoDB, Aurora | SQL Veritabanı, Cosmos DB | Cloud SQL, Firestore, Bigtable |
| **Analiz** | Kırmızıya kayma, EMR | Synapse, Databricks | BigQuery, Veri Akışı |
| **AI/ML** | SageMaker, Tanıma | Azure ML, Bilişsel Hizmetler | Vertex AI, AutoML |
| **Ağ oluşturma** | VPC, Rota 53, CloudFront | VNet, Trafik Yöneticisi | VPC, Bulut DNS, Bulut CDN |
---

## Mimari Desenler
### İyi Tasarlanmış Çerçeve
Her üç büyük sağlayıcı da beş sütun etrafında inşa edilmiş, iyi tasarlanmış çerçeveler yayınlıyor:
| Sütun | Temel İlkeler |
|----------|---------------|
| **Operasyonel Mükemmellik** | İşlemleri otomatikleştirin; sık sık geri döndürülebilir değişiklikler yapın; başarısızlığı öngörmek |
| **Güvenlik** | Güçlü kimlik temeli; güvenliği her katmana uygulayın; aktarılan ve kullanılmayan verileri koruyun |
| **Güvenilirlik** | Test kurtarma prosedürleri; başarısızlıktan otomatik kurtarma; yatay ölçeklendir |
| **Performans Verimliliği** | Sunucusuz kullanın; dakikalar içinde küreselleşin; sık sık deneyin |
| **Maliyet Optimizasyonu** | Tüketim modelini benimseyin; yönetilen hizmetleri kullanın; farklılaştırılmamış işe harcama yapmayı bırakın |
### Ortak Desenler
| Desen | Açıklama | Faydaları | Zorluklar |
|-----------|---------------|----------|------------|
| **Mikro hizmetler** | Uygulamayı küçük, bağımsız hizmetlere ayırın | Ölçeklenebilirlik, hata izolasyonu, bağımsız dağıtım | Dağıtılmış karmaşıklık, veri tutarlılığı |
| **Olay Odaklı** | Bileşenler olaylar aracılığıyla iletişim kurar | Gevşek bağlantı, gerçek zamanlı işleme | Hata ayıklama karmaşıklığı, nihai tutarlılık |
| **Sunucusuz** | Sunucu yönetimi yok; icra başına ödeme | Maliyet verimliliği, hızlı dağıtım | Soğuk başlangıçlar, satıcıya bağlılık, uygulama sınırları |
| **Katmanlı (N-Katmanlı)** | Sunum → İş mantığı → Veri erişimi → Veritabanı | Endişelerin ayrılması, sürdürülebilirlik | Yekpare hale gelebilir |
| **Uzay Tabanlı** | Veriler sanallaştırılmış bellek düğümleri arasında dağıtıldı | Yüksek eşzamanlılık ve düşük gecikmeyi yönetir | Tasarımı ve yönetimi karmaşık |
---

## Temel Hizmetler
### Hesaplama
| Hizmet Türü | Ayrıntılar |
|---------------|-----------|
| **Sanal Makineler** | Genel amaçlı, hesaplama için optimize edilmiş, bellek için optimize edilmiş, GPU. Fiyatlandırma: isteğe bağlı, rezerve edilmiş, anlık. |
| **Konteynerler** | Docker çalışma zamanı; Kubernetes (EKS, AKS, GKE) aracılığıyla orkestrasyon. Kayıtlar: ECR, GCR, ACR. |
| **Sunucusuz İşlevler** | Olayla tetiklenen, vatansız. Yürütme süresi, bellek ve eşzamanlılığa ilişkin sınırlamalar. |
### Depolamak
| Tür | Özellikler | Örnekler | En İyisi |
|----------|-----|----------|----------|
| **Nesne** | Düz yapı, HTTP erişimi, meta veri açısından zengin | S3, Bulut Depolama, Azure Blob | Statik varlıklar, yedeklemeler, veri gölleri |
| **Engelle** | VM'lere eklenen ham birimler | EBS, Kalıcı Disk, Azure Diskler | Veritabanları, önyükleme birimleri |
| **Dosya** | Paylaşılan dosya sistemleri (NFS/SMB) | EFS, Dosya Deposu, Azure Dosyaları | İçerik yönetimi, paylaşılan yapılandırmalar |
| **Arşiv** | En düşük maliyet, alma gecikmeleri | S3 Buzulu, Azure Arşivi | Uyumluluk, uzun vadeli yedeklemeler |
### Veritabanları
| Kategori | Hizmetler | Kullanım Örneği |
|----------|----------|----------|
| **Yönetilen İlişkisel** | RDS, Bulut SQL, Azure SQL | Geleneksel uygulamalar, ASİT işlemleri |
| **NoSQL — Belge** | DocumentDB, Firestore, Cosmos DB | Esnek şemalar, JSON verileri |
| **NoSQL — Anahtar-Değer** | DynamoDB, Redis Önbelleği | Önbelleğe alma, oturumlar, basit aramalar |
| **NoSQL — Geniş Sütun** | Büyük Masa, Cassandra | Yazma ağırlıklı, zaman serisi |
| **NoSQL — Grafik** | Neptün, Cosmos DB (Grafik API) | İlişkiler, sosyal ağlar |
| **Veri Depolama** | Kar Tanesi, Kırmızıya Kayma, BigQuery, Synapse | Analitik, İş Zekası |
| **Önbelleğe alma** | ElastiCache, Bulut Bellek Deposu | Oturum depolama, sorgu önbelleğe alma |
---

## Ağ İletişimi
### Sanal Ağlar
Her bulut dağıtımı, CIDR blokları, alt ağlar (genel veya özel), yönlendirme tabloları ve ağ geçitleriyle tanımladığınız yalıtılmış bir ağ olan bir Sanal Özel Bulut (VPC / VNet) içinde bulunur.
### Yük Dengeleme ve CDN
| Hizmet | Amaç |
|-----------|-----------|
| **Yük Dengeleyiciler** | Trafiği örnekler arasında dağıtın (L4 ağı, L7 uygulaması) |
| **CDN** | Daha düşük gecikme süresi için içeriği uç konumlarda önbelleğe alın (CloudFront, Cloud CDN, Azure CDN) |
| **DNS** | Etki alanı kaydı, yönlendirme politikaları, durum denetimleri (Route 53, Cloud DNS, Azure DNS) |
### Bağlantı Seçenekleri
| Seçenek | Açıklama |
|----------|----------------|
| **İnternet Ağ Geçidi** | VPC için genel internet erişimi |
| **NAT Ağ Geçidi** | Özel alt ağ giden erişimi |
| **VPN** | Şirket içi şifreli tüneller |
| **Doğrudan Bağlantı / EkspresRota** | Özel özel bağlantılar |
| **VPC Eşleme** | VPC'leri hesapların içine veya hesaplar arasında bağlayın |
---

## Güvenlik
### Paylaşılan Sorumluluk Modeli
| Katman | Sağlayıcı | Müşteri |
|----------|----------|----------|
| **Altyapı** (donanım, tesisler) | ✅ | |
| **Bilgisayar, Depolama, Ağ İletişimi** | ✅ (yönetilen) | ✅ (kendi kendini yöneten) |
| **Veriler, Uygulamalar, Kimlik** | | ✅ |
Hizmet ne kadar çok yönetilirse, sağlayıcı da o kadar çok şeyle ilgilenir. IaaS ile neredeyse her şeyi yönetirsiniz; SaaS ile sağlayıcı neredeyse tamamını yönetir.
### Kimlik ve Erişim Yönetimi (IAM)
| Konsept | Açıklama |
|-----------|------------|
| **Kullanıcılar** | Bireysel kimlikler |
| **Gruplar** | Kullanıcı koleksiyonları |
| **Roller** | Hizmetler veya kullanıcılar için geçici kimlik bilgileri |
| **Politikalar** | İzinleri tanımlayan belgeler |
| **Prensip** | En az ayrıcalık, görevler ayrılığı |
### Veri Koruma
- **Kullanılmayan şifreleme**: KMS, müşteri tarafından yönetilen anahtarlar, HSM.
- **Aktarım sırasında şifreleme**: TLS/SSL, HTTPS.
- **Gizli sır yönetimi**: Sır Yöneticisi, Key Vault — gizli dizileri hiçbir zaman sabit kodlamayın.
---

## Bulutta DevOps
### Kod Olarak Altyapı (IaC)
| Araç | Açıklama |
|------|-----------------|
| **Terraform** | Çoklu bulut, bildirim tabanlı HCL, durum yönetimi |
| **Bulut Oluşumu** | AWS'de yerel, YAML/JSON şablonları |
| **ARM Şablonları / Pazı** | Azure'da yerel |
| **Pulumi** | Programlama dillerini (Python, Go vb.) kullanan altyapı |
### CI/CD Hizmetleri
| Sağlayıcı | Araçlar |
|----------|----------|
| **AWS** | CodePipeline, CodeBuild, CodeDeploy |
| **Azure** | Azure DevOps, GitHub Eylemleri |
| **GCP** | Bulut Oluşturma, Bulut Dağıtımı |
| **Üçüncü taraf** | Jenkins, CircleCI, GitLab CI |
### İzleme ve Gözlemlenebilirlik
| Yetenek | AWS | Azure | GCP |
|-----------|-----|----------|-----|
| **Metrikler** | Bulutİzle | Azure Monitör | Bulut İzleme |
| **Günlüğe kaydetme** | CloudWatch Günlükleri | Günlük Analizi | Bulut Günlüğü |
| **İzleme** | Röntgen | Uygulama Bilgileri | Bulut İzleme |
---

## Maliyet Yönetimi
### Fiyatlandırma Modelleri
| Modeli | Açıklama | En İyisi |
|----------|----------------|----------|
| **Talep Üzerine** | Kullandığınız kadarını saniye/saat bazında ödeyin | Değişken, kısa vadeli iş yükleri |
| **Ayrılmış Örnekler** | 1–3 yıllık taahhüt, önemli indirim | Kararlı durum iş yükleri |
| **Spot Bulut Sunucuları** | Kullanılmayan kapasite için teklif verin; kesintiye uğratılabilir | Hataya dayanıklı, esnek işler |
| **Tasarruf Planları** | Esnek taahhüt fiyatlandırması | Karma kullanım modelleri |
| **Ücretsiz Katman** | Yeni hesaplar için sınırlı ücretsiz kullanım | Öğrenme, prototip oluşturma |
### Optimizasyon Stratejileri
İş yüklerine uyacak doğru boyutlu örnekler. Talep ani artışlarını karşılamak için otomatik ölçeklendirmeyi kullanın. Tahmin edilebilir yükler için yedek kapasite. Toplu işler için spot örnekleri kullanın. Nadiren erişilen verileri daha ucuz depolama katmanlarına taşıyın. Kullanılmayan kaynakları (artık anlık görüntüler, boşta kalan yük dengeleyiciler, eklenmemiş IP'ler) silin.
---

## Yüksek Erişilebilirlik ve Olağanüstü Durum Kurtarma
### Kullanılabilirlik Kavramları
| Konsept | Açıklama |
|-----------|------------|
| **Erişilebilirlik Alanı (AZ)** | Bir bölge içindeki veri merkezlerini fiziksel olarak ayırın |
| **Bölge** | Birden fazla AZ'nin bulunduğu coğrafi bölge |
| **Kenar Konumu** | İçerik dağıtımı için CDN önbellek konumu |
### Felaket Kurtarma Stratejileri
| Strateji | Maliyet | RTO | RPO | Açıklama |
|----------|------|-----|-----|-------------|
| **Yedekle ve Geri Yükle** | En düşük | Saat | Saat–gün | Periyodik yedeklemeler, gerektiğinde geri yükleme |
| **Pilot Işığı** | Düşük | Dakika–saat | Dakika | Temel öğeler her zaman çalışıyor, felakete karşı ölçeği artırın |
| **Sıcak Bekleme** | Orta | Dakika | Saniye–dakika | Küçültülmüş sürüm her zaman çalışıyor |
| **Çoklu Site Aktif/Etkin** | En yüksek | Sıfıra Yakın | Sıfır | Birden fazla bölgede tam üretim |
**RTO** (Kurtarma Süresi Hedefi) = kabul edilebilir maksimum kesinti süresi. **RPO** (Kurtarma Noktası Hedefi) = kabul edilebilir maksimum veri kaybı.
---

## Yükselen Trendler
| Eğilim | Neler Oluyor |
|----------|----------|
| **Son Bilgi İşlem** | Verileri kaynağa daha yakın işleme (AWS Outposts, Wavelength, Azure Edge) |
| **Çoklu Bulut** | Satıcıya bağımlı kalmanın önlenmesi; sağlayıcılar arasında türünün en iyilerinden yararlanılıyor |
| **AI/ML Hizmetleri** | Önceden eğitilmiş modeller (görme, konuşma, dil) + özel eğitim (SageMaker, Vertex AI) |
| **Kuantum Hesaplama** | Erken aşama deneysel hizmetler (AWS Braket, Azure Quantum) |
| **Sürdürülebilir Bulut** | Karbon ayak izi takibi, yenilenebilir enerji taahhütleri, yeşil mimari |