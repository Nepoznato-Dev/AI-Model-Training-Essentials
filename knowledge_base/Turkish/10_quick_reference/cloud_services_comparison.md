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

# Bulut Hizmetleri Karşılaştırması
Üç büyük bulut sağlayıcısının (AWS, Azure ve Google Cloud) bilgi işlem, depolama, veritabanları, AI/ML, ağ iletişimi, izleme ve kod olarak altyapı genelinde yan yana karşılaştırması. Hangi platformun kullanılacağına karar veren veya hizmetleri bir buluttan diğerine eşleyen mimarlar için kullanışlıdır.
---

## Sağlayıcıya Genel Bakış
| | AWS | Azure | Google Bulut (GCP) |
|---|-----|----------|----------|
| **Pazar payı** | ~%31 (en büyük) | ~%25 (saniye) | ~%11 (üçüncü, en hızlı büyüyen) |
| **Güçlü yönler** | Hizmetlerin genişliği; olgunluk; ekosistem | Kurumsal entegrasyon; hibrit bulut; Microsoft yığını | Veri/Yapay Zeka; Kubernet'ler; küresel ağ |
| **Şunlar için en iyisi** | Startup'lardan işletmelere; en geniş hizmet kataloğu | Microsoft/Active Directory'ye sahip işletmeler; hibrit | Veri yoğunluklu iş yükleri; Kubernetes'te yerel; AI/ML |
| **Bölgeler** | 33 bölge, 105 AZ | 60'tan fazla bölge | 40'tan fazla bölge, 100'den fazla bölge |
| **Ücretsiz katman** | 12 aylık ücretsiz kullanım + her zaman ücretsiz | 12 ay ücretsiz + 200$ kredi | 90 gün boyunca 300$ kredi + her zaman ücretsiz |
---

## Hesapla
| Hizmet Kategorisi | AWS | Azure | GCP |
|----------------||-----|----------|-----|
| **Sanal Makineler** | EC2 (Elastik Bilgi İşlem Bulutu) | Sanal Makineler | Bilgi İşlem Motoru |
| **Otomatik ölçeklendirme** | Otomatik Ölçeklendirme Grupları | Sanal Makine Ölçek Kümeleri | Örnek Grupları |
| **Sunucusuz İşlevler** | Lambda | Azure İşlevleri | Bulut İşlevleri |
| **Konteyner Kaydı** | ECR (Elastik Konteyner Kaydı) | Azure Konteyner Kayıt Defteri | Eser Kaydı |
| **Konteyner Düzenlemesi** | ECS / EKS | ACS/AKS | GKE / Bulut Koşusu |
| **Sunucusuz Konteynerler** | Fargate | Konteyner Uygulamaları | Bulut Koşusu |
| **Uygulama Platformu (PaaS)** | Elastik Fasulye Sırığı, Uygulama Çalıştırıcısı | Uygulama Hizmeti | Uygulama Motoru |
| **Toplu İşleme** | AWS Grubu | Azure Toplu | Bulut Grubu |
| **GPU / Yapay Zeka Bilgi İşlem** | EC2 (P4d, P5 bulut sunucuları) | NC/ND serisi VM'ler | A2/A3 VM'leri; TPU'lar |
### VM Fiyatlandırma Modelleri
| Modeli | AWS | Azure | GCP |
|----------|-----|----------|-----|
| **İsteğe bağlı** | İsteğe Bağlı Bulut Sunucuları | Kullandıkça öde | İsteğe bağlı |
| **Ayrılmış / Taahhüt Edilmiştir** | Rezerve Bulut Sunucuları (1–3 yıl) | Ayrılmış VM'ler (1–3 yıl) | Taahhütlü kullanım indirimleri (1–3 yıl) |
| **Nokta / Kesintili** | Spot Bulut Sunucuları | Spot VM'ler | Öncelikli / Spot VM'ler |
| **Tasarruf planları** | Tasarruf Planları | Tasarruf planları | Taahhütlü kullanım indirimleri |
---

## Depolamak
| Hizmet Kategorisi | AWS | Azure | GCP |
|----------------||-----|----------|-----|
| **Nesne Depolama** | S3 | Blob Depolama | Bulut Depolama |
| **Blok Depolama** | EBS | Yönetilen Diskler | Kalıcı Disk |
| **Dosya Depolama** | EFS, FSx | Azure Dosyaları | Dosya deposu |
| **Arşiv / Soğuk** | S3 Buzulu, Derin Arşiv | Blob Cool/Arşiv katmanları | Bulut Depolama Soğuk Hattı/Arşiv |
| **Veri Aktarımı** | Kartopu, Veri Senkronizasyonu | Veri Kutusu | Transfer Cihazı |
### Depolama Sınıfları Karşılaştırması
| Kullanım Örneği | AWS S3 | Azure Blobu | GCP Bulut Depolama |
|----------|---------|------------|-----------|
| **Sık erişim** | S3 Standardı | Sıcak | Standart |
| **Sık olmayan erişim** | S3 Standart-IA | Harika | Yakın Hat |
| **Nadir erişim** | S3 Tek Bölge-IA | — | Soğuk Hattı |
| **Arşiv** | S3 Buzulu / Derin Arşiv | Arşiv | Arşiv |
---

## Veritabanları
| Hizmet Kategorisi | AWS | Azure | GCP |
|----------------||-----|----------|-----|
| **İlişkisel (yönetilen)** | RDS (MySQL, PostgreSQL, Oracle, SQL Sunucusu) | Azure Veritabanı (MySQL, PostgreSQL); Azure SQL | Bulut SQL (MySQL, PostgreSQL) |
| **İlişkisel (bulutta yerel)** | Aurora (MySQL/PostgreSQL uyumlu) | Azure SQL Veritabanı (esnek havuzlar) | Cloud Spanner (küresel olarak dağıtılır) |
| **NoSQL (belge)** | DinamoDB | Cosmos DB (MongoDB API'si, SQL API'si) | Yangın deposu; Veri deposu |
| **NoSQL (geniş sütun)** | DynamoDB (ayrıca) | Cosmos DB (Cassandra API'si) | Büyük Masa |
| **NoSQL (anahtar/değer çifti)** | DynamoDB, ElastiCache | Redis için Azure Önbelleği | Bellek Deposu (Redis) |
| **Grafik** | Neptün | Cosmos DB (Gremlin API'si) | — |
| **Zaman serisi** | Zaman Akışı | Azure Veri Gezgini | — |
| **Defter** | QLDB | Azure Gizli Defter | — |
| **Bellek içi önbellek** | ElastiCache (Redis, Memcached) | Redis için Azure Önbelleği | Bellek deposu |
| **Arama** | Açık Arama Hizmeti | Azure Yapay Zeka Arama | Bulut Arama; Vertex Yapay Zeka Arama |
| **Veri ambarı** | Kırmızıya kayma | Sinaps Analizi | BigQuery |
---

## Yapay Zeka ve Makine Öğrenimi
| Hizmet Kategorisi | AWS | Azure | GCP |
|----------------||-----|----------|-----|
| **ML Platformu** | Adaçayı Yapıcı | Azure Makine Öğrenimi | Vertex AI |
| **Önceden eğitilmiş API'ler** | Tanıma (vizyon), Polly (TTS), Anlama (NLP), Metne Dönüştürme | Bilişsel Hizmetler (Görme, Konuşma, Dil, Karar) | Vision AI, Konuşmayı Metne Dönüştürme, Doğal Dil API'si |
| **Yüksek Lisans / Üretken Yapay Zeka** | Ana Kaya (Claude, Lama, Titan) | Azure OpenAI Hizmeti (GPT-4, DALL-E) | Vertex AI (İkizler); Model Bahçesi |
| **Vektör / Gömmeler** | OpenSearch (k-NN), Bedrock Bilgi Tabanları | Azure AI Arama (vektör) | Vertex AI Vektör Arama, AlloyDB |
| **MLOps** | SageMaker Boru Hatları, Model Kaydı | Azure ML İşlem Hatları, Model Kaydı | Vertex AI Pipelines, Model Kaydı |
| **Veri etiketleme** | SageMaker Temel Gerçeği | Azure ML Veri Etiketleme | Vertex AI Veri Etiketleme |
| **Konuşmaya Dayalı Yapay Zeka** | Lex | Azure Bot Hizmeti | Dialogflow CX / ES |
| **Çeviri** | Çevir | Çevirmen | Çeviri API'si |
---

## Ağ İletişimi
| Hizmet Kategorisi | AWS | Azure | GCP |
|----------------||-----|----------|-----|
| **Sanal Ağ** | VPC | Sanal Ağ (VNet) | VPC |
| **Yük Dengeleme** | ELB/ALB/NLB/CLB | Yük Dengeleyici (Uygulama, Ağ, Ağ Geçidi) | Bulut Yük Dengeleme |
| **DNS** | Rota 53 | Azure DNS | Bulut DNS |
| **CDN** | CloudFront | Azure Ön Kapı | Bulut CDN'si |
| **API Ağ Geçidi** | API Ağ Geçidi | API Yönetimi | API Ağ Geçidi |
| **VPN** | Siteden Siteye VPN, İstemci VPN'i | VPN Ağ Geçidi | Bulut VPN'i |
| **Doğrudan Bağlantı / EkspresRota** | Doğrudan Bağlantı | EkspresRota | Bulut Ara Bağlantısı |
| **Özel Bağlantı** | PrivateLink, VPC Uç Noktaları | Özel Bağlantı, Özel Uç Noktalar | Özel Hizmet Bağlantısı |
| **Güvenlik duvarı** | WAF, Ağ Güvenlik Duvarı | Azure Güvenlik Duvarı, WAF | Bulut Zırhı, Güvenlik Duvarı |
| **DDoS Koruması** | Kalkan Standart / Gelişmiş | DDoS Koruması | Bulut Zırhı |
---

## İzleme ve Günlük Kaydı
| Hizmet Kategorisi | AWS | Azure | GCP |
|----------------||-----|----------|-----|
| **Ölçümler / İzleme** | Bulutİzle | Azure Monitör | Bulut İzleme (Stackdriver) |
| **Günlüğe kaydetme** | CloudWatch Günlükleri | Günlük Analizi (Azure Monitör Günlükleri) | Bulut Günlüğü |
| **İzleme** | Röntgen | Uygulama Bilgileri | Bulut İzleme |
| **Uyarı** | CloudWatch Alarmları | Azure Monitör Uyarıları | Bulut İzleme Uyarıları |
| **Kontrol Panelleri** | CloudWatch Kontrol Panelleri | Azure Çalışma Kitapları/Kontrol Panelleri | Bulut İzleme Kontrol Panelleri |
| **Hata takibi** | CloudWatch Sentetikleri | Uygulama Bilgileri | Bulut Hata Raporlaması |
| **Üçüncü taraf** | Datadog, Yeni Kalıntı, PagerDuty | Datadog, Yeni Kalıntı, PagerDuty | Datadog, Yeni Kalıntı, PagerDuty |
---

## Kod ve DevOps Olarak Altyapı
| Hizmet Kategorisi | AWS | Azure | GCP |
|----------------||-----|----------|-----|
| **IaC (yerel)** | Bulut Oluşumu | ARM Şablonları / Pazı | Dağıtım Müdürü / Pulumi |
| **IaC (bulutlar arası)** | Terraform, Pulumi, CDK | Terraform, Pulumi, Bicep | Terraform, Pulumi |
| **CI/CD** | CodePipeline, CodeBuild | Azure DevOps, GitHub Eylemleri | Bulut Yapısı; Bulut Dağıtımı |
| **Konteyner Kaydı** | ECR | Azure Konteyner Kayıt Defteri | Eser Kaydı |
| **GitOps** | Uygulama Mesh + Flux/ArgoCD | AKS'de Flux/ArgoCD | Yapılandırma Senkronizasyonu (Anthos) |
| **Sırlar Yönetimi** | Sırlar Yöneticisi, SSM Parametre Deposu | Anahtar Kasası | Gizli Yönetici |
---

## Fiyatlandırmayla İlgili Hususlar
| Faktör | AWS | Azure | GCP |
|----------|-----|----------|-----|
| **Faturalandırma ayrıntı düzeyi** | Saniyede (bazıları için ilk saatten sonra) | Saniye başına | Saniye başına |
| **Uzun süreli kullanım indirimleri** | Rezerve Edilmiş Bulut Sunucuları / Tasarruf Planları | Ayrılmış VM'ler | Taahhütlü kullanım indirimleri |
| **Örnekleri tespit edin** | %90'a varan indirim | %90'a varan indirim | %91'e varan indirim |
| **Veri çıkışı** | Ücretli (pahalı) | Ücretlendirildi | Varış noktasına bakılmaksızın aynı fiyat (genellikle daha ucuz) |
| **Ücretsiz katman** | 12 ay + her zaman ücretsiz | 12 ay + 200$ kredi | 90 gün boyunca 300$ + her zaman ücretsiz |
| **Kurumsal indirimler** | Kurumsal İndirim Programı (EDP) | MACC (Parasal Taahhüt Sözleşmesi) | Taahhütlü kullanım + CUD'lar |
---

## Hangisi Ne Zaman Kullanılmalı
| Senaryo | Önerilen | Neden |
|----------|----------------|-----|
| **En geniş hizmet seçimi; olgun ekosistem** | AWS | En büyük katalog; çoğu üçüncü taraf entegrasyonu |
| **Microsoft kuruluşu; Aktif Dizin; hibrit** | Azure | Yerel AD entegrasyonu; güçlü hibrit takımlar |
| **Veri depolama; BigQuery; analiz ağırlıklı** | GCP | BigQuery sınıfının en iyisidir; kusursuz veri entegrasyonu |
| **Kubernetes'te yerel geliştirme** | GCP | GKE, yönetilen en gösterişli Kubernetes'tir |
| **Üretici Yapay Zeka / Yüksek Lisans uygulamaları** | Azure veya GCP | GPT modelleri için Azure OpenAI; İkizler için Vertex AI |
| **Küresel ölçekli, düşük gecikmeli uygulamalar** | GCP | Google'ın küresel ağı gerçek bir avantajdır |
| **Devlet / uyumluluk açısından ağır iş yükleri** | AWS veya Azure | Çoğu uyumluluk sertifikası; GovCloud bölgeleri |
| **Maliyete duyarlı girişimler** | GCP veya AWS | GCP'nin ücretsiz katmanı cömerttir; AWS'nin başlangıç ​​kredileri var |
| **Mevcut Microsoft / .NET yığını** | Azure | Visual Studio, .NET, Office 365 ile sıkı entegrasyon |
| **Çoklu bulut stratejisi** | Terraform + üçü de | Buluttaki kaynakları yönetmek için Terraform'u kullanın |
---

## Özet
Her üç bulut da yetenekli, güvenilir ve sürekli genişliyor. Seçim genellikle şunlara bağlıdır: ekibinizin halihazırda ne bildiği, mevcut sözleşmelerinizin neye benzediği ve iş yükünüz için hangi belirli hizmetlerin önemli olduğu. Çoklu bulut giderek daha yaygın hale geliyor; altyapı katmanında satıcıya bağlı kalmayı önlemek için Terraform veya Pulumi kullanın ve her bulutu en iyi yaptığı işe göre seçin.