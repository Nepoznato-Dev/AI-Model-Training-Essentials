---
# Metadata
title: "Software Architecture Patterns"
description: "Monolith, microservices, event-driven, DDD, caching, SOLID"
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
tags: [software, architecture, patterns, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "9 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# Yazılım Mimarisi Kalıpları
Mimarlık, bir sistemin nasıl organize edildiğine, hangi bileşenlere sahip olduğuna, bunların nasıl iletişim kurduğuna ve sorumlulukların nerede olduğuna ilişkin yapısal kararlar dizisidir. İyi mimari, sistemin anlaşılmasını, değiştirilmesini ve ölçeklendirilmesini kolaylaştırır. Kötü mimari her değişikliği bir mücadeleye dönüştürür. Bu dosya ana kalıpları, her birinin ne zaman kullanılacağını ve ilgili ödünleşimleri kapsar.
---

## Monolith ve Mikro Hizmetler
Bu en temel mimari karardır ve doğru kararı vermeye değer.
| Görünüş | Monolit | Mikro hizmetler |
|----------|----------|---------------|
| **Yapı** | Tek konuşlandırılabilir birim | Birçok küçük, bağımsız olarak dağıtılabilen hizmet |
| **Veri** | Paylaşılan veritabanı | Her hizmet kendi verilerine sahiptir |
| **İletişim** | Süreç içi işlev çağrıları | Ağ aramaları (HTTP, gRPC, mesajlaşma) |
| **Ölçeklendirme** | Uygulamanın tamamını ölçeklendirin | Bireysel hizmetleri ölçeklendirin |
| **Dağıtım** | Tek sürüm döngüsü | Bağımsız dağıtımlar |
| **Karmaşıklık** | Başlangıçta geliştirmesi daha kolay | Operasyonel karmaşıklık (ağ oluşturma, izleme) |
| **En İyisi** | Küçük ekipler, erken aşama ürünler | Büyük ekipler, karmaşık alanlar, yüksek ölçek |
### Bir Monolitle Ne Zaman Başlamalı
Çoğu uygulama monolit olarak başlamalıdır. Oluşturmak, test etmek, dağıtmak ve hata ayıklamak daha kolaydır. Etki alanı sınırlarınızın daha net bir resmini elde ettiğinizde hizmetleri daha sonra istediğiniz zaman çıkarabilirsiniz. Buna bazen "modüler monolit" adı verilir; bu, daha sonra çıkarılmasını kolaylaştıracak temiz iç sınırları olan bir monolittir.
### Mikro Hizmetlere Ne Zaman Gidilmeli
Aşağıdaki durumlarda mikro hizmetleri düşünün:
- Ekipler koordinasyonun darboğaza dönüşmesine neden olacak kadar büyüktür.
- Sistemin farklı bölümlerinin çok farklı ölçeklendirme gereksinimleri vardır.
- Bileşenlerin bağımsız dağıtımına ihtiyacınız var.
- Alan adınız net sınırlı bağlamlara sahip (aşağıdaki DDD'ye bakın).
---

## Katmanlı Mimari (N-Katmanlı)
En yaygın mimari desen. Kod, her biri belirli bir sorumluluğa sahip olan katmanlar halinde düzenlenmiştir.
```
â”Œ─────────────────────────┐
│   Presentation Layer    │  ← UI, controllers, API endpoints
├─────────────────────────┤
│   Application Layer     │  ← Use cases, orchestration
├─────────────────────────┤
│   Domain Layer          │  ← Business logic, entities
├─────────────────────────┤
│   Infrastructure Layer  │  ← Database, external services, file I/O
└─────────────────────────┘
```

| Katman | Sorumluluk | Kural |
|----------|---------------|------|
| **Sunum** | Kullanıcı/HTTP isteklerini işleme | Yalnızca Uygulama katmanını arayabilir |
| **Uygulama** | Kullanım örneklerini düzenleyin | Etki Alanı katmanını arayabilir |
| **Alan adı** | Temel iş mantığı | Diğer katmanlara bağımlı olmamalıdır |
| **Altyapı** | Teknik kaygılar | Etki Alanında tanımlanan arayüzleri uygular |
**Temel kural**: bağımlılıklar içe dönüktür. Etki Alanı katmanı veritabanı veya web çerçevesi hakkında bilgi sahibi değildir.
---

## Olay Odaklı Mimari
Bileşenler, **olaylara** yani gerçekleşmiş olaylara tepki vererek ve yayın yaparak iletişim kurar.
| Desen | Açıklama |
|-----------|------------|
| **Olay Bildirimi** | A Hizmeti "OrderPlaced" mesajını verir; hizmetler B, C, D tepkisi |
| **Olay Kaynak Kullanımı** | Tüm durum değişikliklerini bir olaylar dizisi olarak saklayın (yalnızca geçerli durumu değil) |
| **CQRS** | Okuma modelini (sorgular) yazma modelinden (komutlar) ayırın |
### Etkinlik Kaynağı
"Geçerli durumu" bir veritabanında saklamak yerine, her durum değişikliğini bir olay olarak saklayın:
```
OrderCreated(order_id=123, total=$50)
OrderPaid(order_id=123, payment_id=456)
OrderShipped(order_id=123, tracking=ABC)
```

Faydaları: eksiksiz denetim takibi, geçmiş herhangi bir durumu yeniden yapılandırma yeteneği, ayrıştırılmış tüketiciler. Zorluklar: olay şemasının gelişimi, nihai tutarlılık, hata ayıklama karmaşıklığı.
### CQRS (Komut Sorgusu Sorumluluk Ayrımı)
| Yan | Amaç | Veritabanı |
|------|------------|----------|
| **Komut (Yazma)** | Mutasyonları ele alın; iş kurallarını uygulamak | Yazma için optimize edildi (normalleştirilmiş) |
| **Sorgu (Okuma)** | Okuma isteklerini sun | Okumalar için optimize edildi (normalleştirilmedi) |
CQRS, Event Sourcing ile doğal olarak eşleşir: yazma tarafındaki olaylar, okuma için optimize edilmiş görünümlere yansıtılır.
---

## Mesaj Kuyrukları ve Etkinlik Aracıları
Hizmetlerin eşzamansız olarak iletişim kurması gerektiğinde, mesaj kuyrukları omurgayı oluşturur.
| Araç | Tür | En İyisi |
|------|----------|----------|
| **Apache Kafka** | Dağıtılmış olay günlüğü | Yüksek verimli olay akışı, olay kaynağı bulma |
| **TavşanMQ** | Yönlendirmeli mesaj komisyoncusu | Görev kuyrukları, karmaşık yönlendirme modelleri |
| **AWS SQS** | Yönetilen kuyruk | AWS'de yerel, basit sıraya alma |
| **AWS SNS** | Yayıncı/abone bildirimi | Birden fazla aboneye yayılma |
| **Google Pub/Sub** | Yönetilen pub/sub | GCP'de yerel etkinlik akışı |
| **Redis Akışları** | Hafif akış | Basit olay kaydı, önbelleğe alma kullanım durumları |
### Mesajlaşma Kalıpları
| Desen | Açıklama |
|-----------|------------|
| **Noktadan Noktaya** | Mesaj başına bir üretici, bir tüketici |
| **Yayınla/Abone Ol** | Bir yapımcı, birden fazla abone |
| **İstek/Yanıt** | Eşzamansız aktarım üzerinden eşzamanlı stil |
| **Ölü Mektup Sırası** | İşlenemeyen iletiler incelenmek üzere ayrı bir kuyruğa gider |
---

## Etki Alanı Odaklı Tasarım (DDD)
DDD, kodu teknik kaygılar yerine iş kavramları etrafında merkezleyen, yazılım tasarımına yönelik stratejik bir yaklaşımdır.
### Temel Kavramlar
| Konsept | Açıklama |
|-----------|------------|
| **Sınırlı Bağlam** | Alan modelinin tutarlı olduğu sınır (ör. "Sipariş", "Gönderim", "Faturalandırma") |
| **Her Yerde Bulunan Dil** | Geliştiriciler ve alan uzmanları arasında paylaşılan terimler |
| **Toplamlar** | Veri değişiklikleri için ilgili varlık kümeleri tek bir birim olarak ele alınır |
| **Varlıklar** | Kimliği olan nesneler (örneğin, user_id'ye sahip bir Kullanıcı) |
| **Değer Nesneleri** | Kimliği olmayan nesneler; niteliklerine göre tanımlanır (örn. Para, Adres) |
| **Alan Adı Etkinlikleri** | Alan adında meydana gelen bir şey (ör. OrderPlaced) |
| **Yolsuzlukla Mücadele Katmanı** | Alanınız ile harici sistemler arasında çeviri katmanı |
### DDD Yardımcı Olduğunda
DDD en çok iş alanının karmaşık olduğu durumlarda değerlidir; örneğin e-ticaret, lojistik, finansal hizmetler, sağlık hizmetlerini düşünün. Etki alanınız basitse (bir blog, yapılacaklar uygulaması), DDD aşırıya kaçıyor.
---

## Önbelleğe Alma Stratejileri
Önbelleğe alma, performansı artırmanın en etkili yollarından biridir ancak tutarlılık konusunda karmaşıklığa neden olur.
| Strateji | Açıklama | Takas |
|----------|----------------|-----------|
| **Önbellek Kenarı** | Uygulama önce önbelleği kontrol eder; kaçırıldığında DB'den yüklemeler | Basit; nihai tutarlılık |
| **İçinden Yazma** | Önbelleğe ve veritabanına aynı anda yaz | Tutarlı; daha yavaş yazar |
| **Arkasına Yaz** | Önbelleğe yaz; DB'ye eşzamansız yazma | Hızlı yazar; veri kaybı riski |
| **Tamamını Okuma** | DB'den gelen yüklemeleri şeffaf bir şekilde önbelleğe alın | Önbellek kenarından daha basit |
### Neler Önbelleğe Alınır?
| Katman | Ne | Araçlar |
|----------|----------|----------|
| **CDN** | Statik varlıklar, API yanıtları | CloudFront, Cloudflare |
| **Uygulama** | Hesaplanan sonuçlar, oturum verileri | Redis, Memcached |
| **Veritabanı** | Sorgu sonuçları, sık erişilen satırlar | Sorgu önbelleği, gerçekleştirilmiş görünümler |
**Önbelleğin geçersiz kılınması** herkesin bildiği gibi zordur. Ortak stratejiler: TTL (yaşam süresi), olaya dayalı geçersiz kılma (veri değişikliğinde önbelleği temizleme) ve LRU (en son kullanılan) çıkarma.
---

## Tasarım Desenleri
### SAĞLAM İlkeler
| Prensip | Ne Anlama Geliyor |
|-----------|-----------------|
| **S** — Tek Sorumluluk | Bir sınıfın değişmek için tek bir nedeni olmalıdır |
| **O** — Açık/Kapalı | Uzatmaya açık, değişikliğe kapalı |
| **L** — Liskov Oyuncu Değişikliği | Alt türler, temel türlerinin yerine kullanılabilir olmalıdır |
| **I** — Arayüz Ayrımı | Birçok özel arayüz > tek bir genel amaçlı arayüz |
| **D** — Bağımlılığı Tersine Çevirme | Somutlaştırmalara değil, soyutlamalara güvenin |
### Ortak Desenler
| Desen | Niyet | Örnek |
|-----------|-----------|------------|
| **Singleton** | Bir sınıfın yalnızca bir örneğinin olduğundan emin olun | Veritabanı bağlantı havuzu |
| **Fabrika** | Tam sınıf belirtmeden nesneler oluşturun | `UserFactory.create(type="admin")`|
| **Gözlemci** | Durum değiştiğinde bakmakla yükümlü olduğunuz kişileri bilgilendirin | Etkinlik dinleyicileri, pub/sub |
| **Strateji** | Çalışma zamanında algoritmaları değiştirin | Ödeme Stratejisi: Kredi Kartı, PayPal, Kripto |
| **Depo** | Temiz bir arayüzün arkasında soyut veri erişimi | `UserRepository.find_by_id(123)`|
| **Dekoratör** | Davranışı dinamik olarak ekleyin | Bir hizmetin etrafında günlüğe kaydetme dekoratörü |
| **Adaptör** | Uyumsuz arayüzlerin birlikte çalışmasını sağlayın | Eski API bağdaştırıcısı |
---

## Doğru Mimariyi Seçmek
Evrensel olarak "en iyi" mimari yoktur. Doğru seçim şunlara bağlıdır:
| Faktör | Monolit'i Tercih Ettiğinizde... | Mikro Hizmetleri Tercih Edin... |
|----------|-------------|-----------------------------|
| **Takım büyüklüğü** | < 10 developers | >20 geliştirici, birden fazla ekip |
| **Alan karmaşıklığı** | Basit veya iyi anlaşılmış | Karmaşık, birçok sınırlı bağlam |
| **Ölçek gereksinimleri** | Tek tip ölçeklendirme ihtiyaçları | Farklı bileşenler farklı ölçeğe ihtiyaç duyar |
| **Dağıtım temposu** | Tek sürüm döngüsü | Bağımsız dağıtımlara ihtiyaç var |
| **Teknoloji çeşitliliği** | Bir yığın iyidir | Farklı hizmetler farklı teknolojilere ihtiyaç duyar |
**Pratik tavsiye**: Modüler bir monolitle başlayın. Hizmetleri yalnızca net bir ihtiyacınız olduğunda ve etki alanı sınırlarınız net olduğunda çıkarın. Erken mikro hizmetler sektördeki en yaygın mimari hatalardan biridir.