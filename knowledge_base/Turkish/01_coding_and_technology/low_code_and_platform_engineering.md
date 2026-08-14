---
# Metadata
title: "Low-Code and Platform Engineering"
description: "Low-code platforms, internal developer platforms, golden paths"
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
tags: [low, code, platform, engineering, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "5 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Düşük Kod ve Platform Mühendisliği
Düşük kodlu platformlar, insanların minimum düzeyde elle yazılmış kodla (genellikle sürükle ve bırak arayüzleri, görsel iş akışları ve önceden oluşturulmuş bağlayıcılar aracılığıyla) uygulamalar oluşturmasına olanak tanır. Platform mühendisliği, ürün ekiplerinin altyapıyı, CI/CD'yi ve operasyonel araçları kendi kendine hizmet etmesini kolaylaştıran dahili geliştirici platformları (IDP'ler) oluşturma disiplinidir. Her iki eğilim de aynı soruna yanıt veriyor: yazılıma olan talep ile onu geliştirebilecek geliştiricilerin arzı arasındaki uçurum.
---

## Düşük Kodlu Platformlar
### Düşük Kod Aslında Ne Anlama Geliyor
| Görünüş | Açıklama |
|----------|----------------|
| **Görsel gelişim** | Sürükle ve bırak kullanıcı arayüzü oluşturucuları; görsel iş akışı editörleri; form tasarımcıları |
| **Önceden oluşturulmuş bileşenler** | Hazır widget'lar, bağlayıcılar, şablonlar ve entegrasyonlar |
| **Bildirimsel mantık** | Davranışı kod yazmak yerine kurallar ve koşullar aracılığıyla yapılandırma |
| **Genişletilebilirlik** | Platformun yerleşik yetenekleri yeterli olmadığında özel kod ekleyebilme |
| **Yönetilen altyapı** | Platform; barındırma, ölçeklendirme ve güvenlik yamalarını yönetir |
### Popüler Düşük Kodlu Platformlar
| Platformu | Güç | Tipik Kullanım Durumu |
|----------|----------|------|
| **Microsoft Güç Platformu** | Derin Microsoft 365/Azure entegrasyonu; Power Apps, Power Automate, Power BI | Kurumsal iş akışları; dahili aletler |
| **Salesforce Platformu** | CRM'de yerleşik; Uzantılar için apex; Akış Oluşturucu | Müşteriye yönelik uygulamalar; satış iş akışları |
| **Şimdi Hizmet** | BT hizmet yönetimi; iş akışı otomasyonu | BT operasyonları; İK; tesisler |
| **Appian** | Süreç madenciliği; vaka yönetimi | Karmaşık iş süreçleri; uyumluluk |
| **OutSystems** | Tam yığın web ve mobil; kurumsal düzeyde | Müşteri portalları; mobil uygulamalar |
| **Yeniden Düzenleme** | Dahili araç oluşturucu; veritabanlarına ve API'lere bağlanır | Yönetici panelleri; gösterge tabloları; operasyon araçları |
| **Havalandırılabilir** | Elektronik tablo-veritabanı hibriti; otomasyonlar | Proje takibi; hafif CRM |
### Düşük Kod İyi Çalıştığında
| Senaryo | Neden Düşük Kod Uyuyor |
|----------|-----------|
| **Dahili araçlar** | Hızlı inşa edilir; kullanıcılar dahili olduğundan kullanıcı arayüzü esnekliği daha az önemlidir |
| **Formlar ve onaylar** | Görsel iş akışı oluşturucuları bu konuda uzmandır |
| **CRUD uygulamaları** | Düşük kodlu platformların çoğu, oluşturma-okuma-güncelleme-silme kalıpları için optimize edilmiştir |
| **Prototip oluşturma** | Bir fikri haftalar yerine birkaç saat içinde doğrulayın |
| **Vatandaş gelişimi** | İş analistleri BT yönetişimi ile kendi çözümlerini oluşturabilirler |
### Düşük Kod Yetersiz Kaldığında
| Sınırlama | Etki |
|------------|-----------|
| **Satıcıya bağlılık** | Uygulamalar platformdan kolayca taşınamaz |
| **Performans tavanları** | Yüksek verimli veya gecikmeye duyarlı uygulamalar için uygun değildir |
| **Kullanıcı arayüzü kısıtlamaları** | Özel tasarımlar zordur; platformun desteklediği şeylerle sınırlısınız |
| **Entegrasyon karmaşıklığı** | Alışılmadık API'lere veya eski sistemlere bağlanmak yine de özel kod gerektirebilir |
| **Ölçeğe göre maliyet** | Kullanım arttıkça kullanıcı başına veya uygulama başına fiyatlandırma pahalı hale gelebilir |
| **Hata ayıklama zorluğu** | Görsel soyutlamalar karmaşık sorunları teşhis etmeyi zorlaştırıyor |
---

## Platform Mühendisliği
### Platform Mühendisliği Sorununu Çözüyor
| Platform Mühendisliği Olmadan | Platform Mühendisliği ile |
|------------------|----------------|
| Her takım kendi altyapısını yönetir | Self-servis platform altyapıyı özetliyor |
| Ekipler arasında tutarsız araçlar | Standartlaştırılmış takım zinciri; altın yollar |
| Geliştiriciler operasyonların kaynak sağlamasını bekliyor | Geliştiriciler isteğe bağlı olarak kaynak sağlıyor |
| Bilgi siloları; kabile bilgisi | Belgelenmiş; otomatik; keşfedilebilir |
| Yeni mühendisler için işe alım yavaş | Yeni mühendisler ilk günden göreve başlayabilir |
### Dahili Geliştirici Platformunun Temel Bileşenleri
| Bileşen | Amaç | Örnek Araçlar |
|-----------|------------|---------------|
| **Hizmet kataloğu** | Tüm hizmetlerin ve sahiplerinin merkezi kaydı | Kulis; Liman; Korteks |
| **Şablonlu iskele** | Onaylanmış şablonlardan yeni hizmetler oluşturun | Sahne arkası yazılım şablonları; Kurabiye kesici |
| **Self-servis altyapısı** | Geliştiriciler, bildirimde bulunmadan bulut kaynaklarını tedarik ediyor | Terraform modülleri; Pulumi; Çapraz düzlem |
| **CI/CD ardışık düzenleri** | Standartlaştırılmış işlem hatları oluşturma, test etme ve dağıtma | GitHub Eylemleri; GitLab CI; Argo CD'si |
| **Çevre yönetimi** | Talep üzerine geçici geliştirme/hazırlama ortamları | Vkümesi; Ad alanı; Gitpod |
| **Gözlemlenebilirlik** | Her hizmette yerleşik olarak günlüğe kaydetme, ölçümler ve izleme | Prometheus; Grafana; Açık Telemetri; Datadog |
| **Gizli yönetim** | Kimlik bilgilerinin güvenli şekilde saklanması ve döndürülmesi | Kasa; AWS Secrets Yöneticisi; SOPS |
| **Kimlik ve erişim** | TOA; rol tabanlı erişim; hizmetten hizmete yetkilendirme | Okta; Anahtarlık; SPIFFE |
### Altın Yollar
Altın yol, bir şeyi yapmanın desteklenen, üzerinde düşünülmüş yoludur. Bu en az dirençli yoldur; eğer onu takip ederseniz her şey işe yarar. Yolun dışına çıkabilirsin ama tek başınasın.
| Altın Yol | Ne Sağlar |
|---------------|------|
| **Yeni hizmet** | Şablon deposu; CI/CD; izleme; günlüğe kaydetme; dağıtım yapılandırması |
| **Yeni veritabanı** | Sağlanan örnek; sırlardaki bağlantı dizeleri; yedekleme yapılandırıldı |
| **Yeni kullanıcı arayüzü** | Boru hattı oluşturun; CDN; önizleme ortamları; deniz feneri kontrolleri |
| **Veri hattı** | Orkestrasyon; şema doğrulama; izleme; uyarı |
### Oluşturma ve Satın Alma Kararları
| Faktör | Özel Oluştur | Mevcut Aracı Kullan |
|----------|----------------|---------------------|
| **Temel yeterlilik** | İşletmenize özel; rekabet avantajı | Emtia; her şirketin buna ihtiyacı var |
| **Bakım yükü** | Bunu sürdürme kapasiteniz var | Araç satıcı/topluluk tarafından iyi korunuyor |
| **Entegrasyon ihtiyaçları** | Dahili sistemlerle derin entegrasyon gereklidir | Standart API'ler ve bağlayıcılar yeterlidir |
| **Maliyet** | Oluşturulması lisanstan daha ucuz | Lisanslamak inşa etmekten daha ucuz |
---

## Düşük Kod ve Platform Mühendisliği Arasındaki İlişki
| Boyut | Düşük Kod | Platform Mühendisliği |
|-----------|----------|----------|
| **Hedef kullanıcı** | İş kullanıcıları; vatandaş geliştiricileri | Profesyonel yazılım mühendisleri |
| **Gol** | Kodu azaltın; hızı arttır | Bilişsel yükü azaltın; özerkliği artırmak |
| **Soyutlama düzeyi** | Çok yüksek; görsel | Orta; kod tabanlı ancak basitleştirilmiş |
| **Esneklik** | Platform yetenekleriyle sınırlıdır | Tam esneklik; herhangi bir kod yazabilirsiniz |
| **Yönetim** | Platform kuralları uygular | Platform altın yollar sunuyor |
Tamamlayıcıdırlar: Platform mühendisliği profesyonel geliştiricileri daha hızlı hale getirirken düşük kod, geliştirici olmayanların basit uygulamalar oluşturmasına olanak tanır. Birlikte, yazılım teslimi boşluğunu farklı açılardan ele alıyorlar.
---

## Özet
Düşük kodlu platformlar ve dahili geliştirici platformlarının her ikisi de, yazılım sunabilecek kişi sayısını artırmayı amaçlamaktadır. Düşük kod, kodu tamamen soyutlayarak (görsel oluşturucular, önceden oluşturulmuş bağlayıcılar, bildirimsel mantık) bunu yapar. Platform mühendisliği bunu profesyonel geliştiricilere self-servis altyapı, altın yollar ve standartlaştırılmış araçlar sağlayarak yapar, böylece operasyon çalışmalarına daha az, ürün özelliklerine daha fazla zaman harcarlar. İkisi de sihirli değnek değildir: Düşük kodun satıcıya bağlılığı ve performans sınırlamaları vardır ve platform mühendisliğinin sürdürülmesi için sürekli yatırım yapılması gerekir. Ancak doğru sorunlara (dahili araçlar, CRUD uygulamaları, standart hizmet sunumu) uygulandığında her ikisi de fikirden üretime kadar geçen süreyi önemli ölçüde azaltabilir.