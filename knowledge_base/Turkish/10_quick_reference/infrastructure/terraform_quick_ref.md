---
# Metadata
title: "Terraform and Infrastructure as Code"
description: "IaC concepts, Terraform commands, state management, modules"
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
tags: [terraform, quick-reference]
difficulty_level: "beginner"
prerequisites: []
estimated_reading_time: "6 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Kod Olarak Terraform ve Altyapı
Terraform, en yaygın kullanılan Kod Olarak Altyapı (IaC) aracıdır; sürümlendirilebilen, incelenebilen, test edilebilen ve otomatikleştirilebilen bildirime dayalı yapılandırma dosyalarında bulut altyapısını (sunucular, veritabanları, ağlar, izinler) tanımlamanıza olanak tanır. Bir bulut konsoluna tıklamak yerine, altyapınızın istenen durumunu açıklayan kodu yazarsınız ve Terraform hangi değişikliklerin yapılması gerektiğini belirler.
---

## Temel Kavramlar
| Konsept | Açıklama |
|-----------|------------|
| **Sağlayıcı** | Belirli bir bulut platformunu (AWS, Azure, GCP vb.) yöneten eklenti |
| **Kaynak** | Bir altyapı nesnesi (sunucu, veritabanı, ağ) |
| **Devlet** | Terraform'un hangi altyapının mevcut olduğuna dair kaydı; durum dosyasında saklanır |
| **Plan** | Terraform'un yapacağı değişikliklerin önizlemesi |
| **Uygula** | Planı uygulayın; altyapı oluşturma/güncelleme/yok etme |
| **Modül** | Yeniden kullanılabilir kaynak koleksiyonu |
| **Değişken** | Konfigürasyonlar için giriş parametresi |
| **Çıktı** | Bir modülden veya konfigürasyondan aktarılan değer |
| **Veri kaynağı** | Mevcut altyapıdaki bilgileri okuyun |
---

## Temel İş Akışı
| Adım | Komut | Açıklama |
|------|---------|------------|
| **1. Yapılandırmayı yaz** |`.tf`dosyaları oluşturun | Sağlayıcıları, kaynakları, değişkenleri tanımlayın |
| **2. Başlatma** | `terraform init`| Sağlayıcıları indirin; arka uç kurulumu |
| **3. Biçim** | `terraform fmt`| Biçimlendirmeyi standartlaştırın |
| **4. Doğrula** | `terraform validate`| Söz dizimini ve yapılandırmayı kontrol edin |
| **5. Planı** | `terraform plan`| Değişiklikleri önizleyin (deneme) |
| **6. Uygula** | `terraform apply`| Altyapı oluşturun veya güncelleyin |
| **7. Yok et** | `terraform destroy`| Yönetilen tüm altyapıyı yıkın |
---

## Ortak Komutlar
| Komut | Açıklama |
|-----------|------------|
| `terraform init`| Çalışma dizinini başlatın; sağlayıcıları ve modülleri indirme |
| `terraform plan`| Hangi değişikliklerin yapılacağını göster |
| `terraform apply`| Değişiklikleri uygula; onayı atlamak için`-auto-approve`ekleyin |
| `terraform destroy`| Yönetilen tüm kaynakları yok edin |
| `terraform fmt`| Yapılandırma dosyalarını standart stile göre biçimlendirin |
| `terraform validate`| Yapılandırma sözdizimini doğrulayın |
| `terraform output`| Çıkış değerlerini göster |
| `terraform state list`| Durumdaki tüm kaynakları listele |
| `terraform state show <resource>`| Belirli bir kaynağın ayrıntılarını göster |
| `terraform import <resource> <id>`| Mevcut altyapıyı duruma aktarın |
| `terraform taint <resource>`| Bir sonraki başvuruda eğlence için bir kaynağı işaretleyin |
| `terraform refresh`| Durumu gerçek altyapıyla eşleşecek şekilde güncelleyin |
| `terraform graph`| Görsel bir bağımlılık grafiği oluşturun (DOT formatı) |
| `terraform console`| İfadeleri test etmek için etkileşimli konsol |
---

## Devlet Yönetimi
| En İyi Uygulama | Açıklama |
|----------------|------------|
| **Uzak durum** | Durumu S3, GCS, Azure Blob veya Terraform Cloud'da depolayın; asla yerel olarak değil |
| **Durum kilitleme** | Eş zamanlı değişiklikleri önlemek için DynamoDB (S3 arka uç) veya yerel kilitleme kullanın |
| **Durum şifrelemesi** | Durum dosyaları için kullanımda olmayan şifrelemeyi etkinleştirin (hassas veriler içerirler) |
| **Devlet ayrımı** | Farklı ortamlar veya ekipler için ayrı durum dosyaları kullanın |
| **Durum yedeklemesi** | Uzak arka uçların otomatik olarak sürüm durumu; bunu etkin tut |
| **Durumu asla manuel olarak düzenlemeyin** | Bunun yerine`terraform state mv`,`rm`,`import`kullanın |
---

## Modül Yapısı
```
module/
├── main.tf          # Primary resources
├── variables.tf     # Input variables
├── outputs.tf       # Output values
├── versions.tf      # Provider and Terraform version constraints
├── README.md        # Documentation
└── examples/        # Example usage
    └── basic/
        └── main.tf
```

---

## Değişken Türleri
| Tür | Örnek | Kullanım Örneği |
|------|------------|----------|
| **dize** | `variable "region" { type = string }`| Tek metin değeri |
| **sayı** | `variable "count" { type = number }`| Sayısal değer |
| **bool** | `variable "enable" { type = bool }`| Doğru/yanlış işareti |
| **liste** | `variable "zones" { type = list(string) }`| Sipariş edilen koleksiyon |
| **harita** | `variable "tags" { type = map(string) }`| Anahtar/değer çiftleri |
| **nesne** | `variable "config" { type = object({...}) }`| Yapılandırılmış konfigürasyon |
---

## Ortak Desenler
| Desen | Açıklama |
|-----------|------------|
| **Say** | `count = 3`bir kaynağın birden çok örneğini oluşturur |
| **Her biri için** | `for_each = var.items`bir harita veya küme üzerinde yinelenir |
| **Dinamik bloklar** | Tekrarlanan iç içe geçmiş bloklar oluşturun (ör. giriş kuralları) |
| **Yerel değerler** |  Hesaplanan değerler ve tekrarların azaltılması için`locals { ... }`|
| **Veri kaynakları** | Mevcut altyapıyı okuyun (ör. mevcut bir VPC'yi bulun) |
| **Tedarikçiler** | Oluşturulduktan sonra kaynaklarda komut dosyaları çalıştırın (az miktarda kullanın) |
| **Çalışma alanları** | Aynı yapılandırmada farklı ortamlar için ayrı durum |
---

## Sorun Giderme
| Sorun | Çözüm |
|-----------|----------|
| **Devlet kayması** | Farklılıkları görmek için `terraform plan`'yi çalıştırın; `terraform apply`uzlaşacak |
| **Kilitli durum** | Kilidin kimde olduğunu kontrol edin; Güvenliyse`terraform force-unlock`kullanın |
| **Sağlayıcı hataları** | Kimlik bilgilerini kontrol edin; sağlayıcı sürümünü güncelleyin; API sınırlarını kontrol edin |
| **İçe aktarma çakışmaları** | Kaynak zaten durumda; önce `terraform state rm`'yi kullanın |
| **Döngüsel bağımlılıklar** | Kaynakları yeniden yapılandırın; `depends_on`'yi dikkatli kullanın |
| **Büyük devlet** | Modüllere bölünmüş; kısmi işlemler için`-target`kullanın |
---

## Özet
Terraform, bildirime dayalı yapılandırma dosyaları aracılığıyla altyapıyı yönetir. İş akışı şu şekildedir: konfigürasyonu yaz → başlat → planla → uygula. Durum, kilitleme ile mevcut olanı ve uzaktan saklanması gerekenleri izler. Modüller yeniden kullanıma olanak sağlar. Değişkenler konfigürasyonları parametreleştirir. Temel ilkeler şunlardır: altyapıyı kod olarak ele alın (sürüm kontrolü; inceleme; test); durumu hiçbir zaman manuel olarak düzenlemeyin; uygulamadan önce planlayın; kilitleme ile uzak durumu kullanın; ve bakım kolaylığı için modüller içeren yapı konfigürasyonları.