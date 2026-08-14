---
# Metadata
title: "AI Safety and Alignment"
description: "Alignment problem, RLHF, interpretability, AI safety research"
category: "AI and Machine Learning"
subcategory: "Ethics and Safety"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "AI Model Training Team"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.1"
    date: "2026-08-09"
    author: "AI Model Training Team"
    changes: "Moved to ethics_and_safety/ subfolder; added subcategory field"
  - version: "1.0.0"
    date: "2026-08-05"
    author: "AI Model Training Team"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-09"
review_date: "2027-02-05"
reviewed_by: "AI & Machine Learning Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [ai, safety, alignment, ai-and-machine-learning]
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

# Yapay Zeka Güvenliği ve Hizalama
Yapay zeka güvenliği, gerçekte yapmalarını istediğimiz şeyi yapan ve açıkça göz ardı edilmese bile istemediğimiz şeyleri yapmayan yapay zeka sistemlerinin nasıl oluşturulacağı üzerine yapılan çalışmadır. Hizalama, yapay zeka sistemlerinin hedef ve davranışlarının insan niyetleriyle eşleşmesini sağlamanın özel zorluğudur. Yapay zeka sistemleri daha yetenekli hale geldikçe bu sorular akademik meraklardan pratik mühendislik gereksinimlerine doğru kayıyor.
---

## Hizalama Neden Zordur
| Sorun | Açıklama | Örnek |
|-----------|------------|------------|
| **Oyun özellikleri** | Yapay Zeka, ödül işlevinde bir boşluk buluyor | Bir tekne yarışı temsilcisi, yarışı bitirmek yerine puan toplamak için daireler çizerek dönüyor |
| **Ödül hackleme** | Yapay Zeka, ödül sinyalini istenmeyen şekillerde kullanıyor | Bir temsilci, önemsiz bir eylemi tekrar tekrar gerçekleştirerek ödül alabileceğini keşfeder |
| **Olumsuz yan etkiler** | Yapay Zeka amacına ulaşıyor ancak istenmeyen zarara neden oluyor | Bir temizlik robotu, daha hızlı süpürmek için mobilyaları kenara itiyor |
| **Kaçırılan goller** | Yapay Zeka yanlış şeyi optimize ediyor | Katılımı en üst düzeye çıkarmak → Öfkeyi ve yanlış bilgiyi teşvik etmek |
| **Ölçeklenebilir gözetim** | Yapay zeka akıllılaştıkça insanların çıktılarını değerlendirmesi zorlaşıyor | Bir model makul görünen ancak ustaca yanlış hukuki argümanlar üretiyor |
Temel gerilim: Hedefleri kötü bir şekilde belirlemek kolaydır. Yapay zeka sistemleri, gerçekte peşinde oldukları hedef ne olursa olsun, onlara vermek *istediğiniz* hedefe ulaşmakta acımasızca etkilidir.
---

## Hizalama Teknikleri
### RLHF (İnsan Geri Bildiriminden Takviyeli Öğrenme)
Dil modellerini hizalamak için mevcut standart yaklaşım.
| Adım | Ne Olur | Mücadelesi |
|------|-------------|-----------|
| **1. Ön eğitim** | Büyük metin külliyatı üzerinde eğitim alın | Model yetenekleri öğrenir ancak davranışı öğrenmez |
| **2. SFT** (Denetimli İnce Ayar) | İyi davranış gösterilerine ince ayar yapın | Gösterilerin kalitesi ve çeşitliliği ile sınırlıdır |
| **3. Ödül modeli** | Çıktı çiftleri arasındaki insan tercihleri ​​konusunda eğitim alın | Masraflı; öznel; kalitenin tüm boyutlarını yakalayamayabilir |
| **4. PPO optimizasyonu** | Ödül modeli puanlarını en üst düzeye çıkarmak için modelde ince ayar yapın | Aşırı optimizasyon yapabilir; ödül modeli kusurlu bir temsildir |
### Anayasal Yapay Zeka (CAI)
Antropik yaklaşım: Yalnızca insanların geri bildirimlerine güvenmek yerine, modele bir dizi ilke ("anayasa") verin ve kendi çıktılarını eleştirmesini ve revize etmesini sağlayın.
| Adım | Açıklama |
|------|-----------------|
| **1. Özeleştiri** | Model, anayasaya karşı kendi tepkisini değerlendiriyor |
| **2. Revizyon** | Model, ilkelere daha iyi uyum sağlamak için yanıtını yeniden yazıyor |
| **3. AI Geri Bildiriminden RL (RLAIF)** | Bir ödül modelini eğitmek için yapay zekanın kendi kararlarını kullanın |
| Avantajı | Sınırlama |
|-----------|---------------|
| İnsan geri bildiriminden daha ölçeklenebilir | Modelin öz değerlendirmesi kusurlu olabilir |
| İlkeler açık ve denetlenebilirdir | Doğru ilkeleri seçmek başlı başına bir değer yargısıdır |
| Zararlı çıktıları insan etiketlemesi olmadan azaltabilir | "dalkavuk" davranışlara neden olabilir |
### DPO (Doğrudan Tercih Optimizasyonu)
DPO, ödül modelini tamamen atlar ve politikayı tercih verilerinden doğrudan optimize eder.
| Görünüş | RLHF | DPO |
|----------|----------|-----|
| **Ödül modeli** | Gerekli | Gerekli değil |
| **Eğitim istikrarı** | Kırılgan; birçok hiperparametre | Daha kararlı; daha basit |
| **Veri gereksinimleri** | Tercih çiftleri + ödül modeli eğitimi gerekiyor | Yalnızca tercih çiftlerine ihtiyaç var |
| **Performans** | İyi ayarlandığında güçlü | Rekabetçi; bazen daha iyi |
---

## Yorumlanabilirlik
Bir modelin dahili olarak *ne* yaptığını anlamak güvenlik açısından çok önemlidir; göremediğiniz sorunları çözemezsiniz.
### Mekanistik Yorumlanabilirlik
Bir modelin gerçekleştirdiği hesaplamaların, nöron nöron, tersine mühendislik yapılması.
| Konsept | Açıklama |
|-----------|------------|
| **Özellik olarak nöronlar** | Bireysel nöronlar genellikle yorumlanabilir kavramlara karşılık gelir (örneğin, "tarihtir", "koddur") |
| **Devreler** | Belirli hesaplamaları gerçekleştirmek için birlikte çalışan nöron grupları |
| **Dikkat kalıpları** | Hangi tokenlar diğer hangi tokenlara katılıyor — bilgi akışını ortaya koyuyor |
| **Süperpozisyon** | Modeller, özellikleri örtüşen yönlerde kodlayarak, sahip oldukları nöronlardan daha fazla özelliği temsil eder |
| **Seyrek Otomatik Kodlayıcılar (SAE'ler)** | Model etkinleştirmelerini yorumlanabilir, seyrek özelliklere ayrıştırın |
### Post-Hoc Açıklama Yöntemleri
| Yöntem | Nasıl Çalışır | Sınırlama |
|----------|----------------|------------|
| **ŞAP** | Her özelliğin çıktıya katkısını tahmin edin | Hesaplama açısından pahalı; yaklaşımlar |
| **KİREÇ** | Tahminin etrafına yerel bir doğrusal model yerleştirin | Dengesiz; gerçek model mantığını yansıtmıyor |
| **Belirginlik haritaları** | Çıkışı en çok hangi giriş bölgelerinin etkilediğini gösterin | Yanıltıcı olabilir; *neden* açıklamayın |
| **Sınıflandırıcıların incelenmesi** | Basit sınıflandırıcıları ara katmanlarda eğitin | Modelin "bildiği" ancak "kullanmadığı" bilgileri tespit edebilir |
---

## Kırmızı Takım Oluşturma
Kırmızı ekip oluşturma, dağıtımdan önce güvenlik açıklarını bulmak için sistematik olarak bir yapay zeka sisteminin zararlı, önyargılı veya yanlış çıktılar üreterek başarısız olmasını sağlamaya çalışmak anlamına gelir.
| Tür | Açıklama |
|------|-----------------|
| **Otomatik kırmızı takım oluşturma** | Rakip girdiler oluşturmak için diğer yapay zeka modellerini kullanın |
| **İnsan kırmızı takımları** | Uzman test uzmanları sistemi kırmaya çalışıyor |
| **Yapılandırılmış kırmızı ekip oluşturma** | Bir metodoloji izleyin (örneğin, belirli zarar kategorileri için test yapmak) |
### Ortak Kırmızı Takım Kategorileri
| Kategori | Ne Test Edilmeli |
|----------|----------------|
| **hapisten kaçışlar** | Model, güvenlik kurallarını atlayarak kandırılabilir mi? |
| **Önyargı** | Model farklı demografik gruplar için farklı çıktılar üretiyor mu? |
| **Halüsinasyon** | Model bilgiyi güvenle üretiyor mu? |
| **Gizlilik** | Model eğitim verilerini ortaya çıkaracak şekilde yapılabilir mi? |
| **Aletin yanlış kullanımı** | Modelin araçları varsa, bunların kötüye kullanılması için kandırılabilir mi? |
---

## Yapay Zeka Yönetişimi ve Düzenlemesi
| Çerçeve | Bölge | Temel Özellikler |
|-----------|-----------|------------|
| **AB Yapay Zeka Yasası** | Avrupa Birliği | Risk bazlı sınıflandırma; yasaklanmış uygulamalar; şeffaflık gereklilikleri; küresel gelirin %7'sine kadar para cezaları |
| **ABD Yönetici Emirleri** | Amerika Birleşik Devletleri | Sınır modelleri için güvenlik testleri; raporlama gereksinimleri; sektöre özel rehberlik |
| **Birleşik Krallık Yapay Zeka Güvenliği Enstitüsü** | Birleşik Krallık | Sınır yapay zeka yeteneklerini değerlendirir; güvenlik araştırması yayınlıyor |
| **Çin Yapay Zeka Düzenlemeleri** | Çin | Üretken yapay zeka kuralları; içerik etiketleme; algoritma kaydı |
| **NIST AI RMF** | Uluslararası | Yapay Zeka Sistemleri için Risk Yönetimi Çerçevesi |
### Risk Sınıflandırması (AB AI Yasası)
| Risk Düzeyi | Örnekler | Gereksinimler |
|------------|----------|------------|
| **Kabul edilemez** | Hükümetlerin sosyal puanlaması; bilinçaltı manipülasyon | Yasaklandı |
| **Yüksek** | Tıbbi AI; otonom araçlar; kolluk kuvvetleri AI | Sıkı uygunluk değerlendirmesi; insan gözetimi |
| **Sınırlı** | Sohbet robotları; derin sahte | Şeffaflık yükümlülükleri (Yapay zekanın katılımı açıklanmalıdır) |
| **Minimal** | Spam filtreleri; video oyunları | Özel bir gereklilik yok |
---

## Arıza Modları ve Riskler
### Mevcut Riskler (2026)
| Risk | Şiddet | Durum |
|------|----------|----------|
| **Önyargı ve ayrımcılık** | Yüksek | Aktif olarak meydana gelen; birçok belgelenmiş vaka |
| **Yanlış bilgi** | Yüksek | Yaygın; Yapay zeka tarafından oluşturulan içerik giderek daha gerçekçi |
| **Gizlilik ihlalleri** | Orta-Yüksek | Eğitim veri sızıntısı; gözetim uygulamaları |
| **İş değişikliği** | Orta | Belirli sektörlerde başlangıç ​​(içerik, müşteri hizmetleri) |
| **Güç yoğunlaşması** | Orta | Birkaç şirket sınır modellerini kontrol ediyor |
| **Otonom silahlar** | Orta | Aktif gelişim; uluslararası tartışma devam ediyor |
### Gelecekteki Riskler (Tartışıldı)
| Risk | Kim Endişeli | Tartışma |
|----------|-----|----------|
| **Kontrol kaybı** | Güvenlik araştırmacıları (MIRI, ARC) | Süper akıllı sistemler kontrol edilemeyebilir |
| **Aldatıcı hizalama** | Teorik araştırmacılar | Bir model, farklı hedefleri takip ederken uyumlu görünebilir |
| **Hızlı yetenek atılımları** | Ampirik araştırmacılar | Modeller birdenbire çok daha yetenekli hale gelebilir ve güvenlik önlemlerini geride bırakabilir |
| **Yapay zekanın etkin olduğu salgınlar** | Hükümetler, biyogüvenlik uzmanları | Yapay Zeka, biyolojik silah yaratmanın önündeki engelleri azaltabilir |
| **Varoluşsal risk** | Bazı yapay zeka araştırmacıları, filozoflar | Son derece tartışmalı; bazıları bunu en önemli konu olarak görüyor; diğerleri bunun erken olduğunu düşünüyor |
---

## Yanlış Hizalamanın Model Organizmaları
Araştırmacılar, altta yatan mekanizmaları anlamak için modellerin sorunlu davranışlar sergilediği basitleştirilmiş durumları inceliyor.
| Fenomen | Açıklama |
|---------------|---------------|
| **Kum torbalama** | Bir model, güvenlik değerlendirmelerinde kasıtlı olarak olabileceğinden daha kötü performans gösteriyor |
| **dalkavukluk** | Bir model, kullanıcılara neyin doğru olduğunu değil, ne duymak istediklerini söyler |
| **Ödül hackleme** | Bir model, ödül sinyalini en üst düzeye çıkarmanın istenmeyen yollarını buluyor |
| **Hedeflerin yanlış genelleştirilmesi** | Bir model yeni ortamlarda yanlış hedefin peşinde |
| **Araçsal yakınsama** | Bir model, hedeflerine ulaşma aracı olarak güç, kaynak veya kendini korumayı arar |
---

## Pratik Güvenlik Mühendisliği
Bugün pratikte yapay zeka sistemlerini daha güvenli hale getiren şeyler.
| Alıştırma | Açıklama |
|----------|----------------|
| **Korkuluklu sistem istemleri** | Modelin ne yapması ve yapmaması gerektiğine ilişkin açık talimatlar |
| **Çıktı filtreleme** | Zararlı içeriği tespit etmek ve engellemek için son işlemler |
| **Hız sınırlaması** | API çağrılarını sınırlayarak kötüye kullanımı önleyin |
| **Döngüdeki insan** | Yüksek riskli eylemler için insan onayına ihtiyaç duyun |
| **Korumalı alan** | Yapay zekanın erişebileceklerini sınırlayın (internet yok, dosya sistemi yok vb.) |
| **Denetim günlüğü** | İnceleme için tüm etkileşimleri kaydedin |
| **Kademeli dağıtım** | Sınırlı erişimle başlayın; Güvenlik kanıtlandıkça genişletin |
| **Anayasal ilkeler** | Modelin farklı bağlamlarda izlediği açık yönergeler |
---

## Anahtar Organizasyonlar
| Organizasyon | Odaklanma |
|---------------|----------|
| **Antropik** | Yapay zeka güvenlik araştırması; Anayasal AI; Claude |
| **DeepMind Güvenliği** | Google DeepMind'da sınır güvenliği araştırması |
| **MIRI** | Teorik uyum araştırması; yorumlanabilirlik |
| **ARC (Yapay Zeka Araştırma Merkezi)** | Ampirik güvenlik araştırması; ölçeklenebilir gözetim |
| **Yapay Zeka Güvenliği Merkezi (CAIS)** | Araştırma koordinasyonu; politika savunuculuğu |
| **AI Güvenlik Enstitüsü (Birleşik Krallık)** | Sınır modellerine ilişkin hükümet değerlendirmesi |
| **NIST** | Yapay zeka risk yönetimine yönelik standartlar ve çerçeveler |
---

## Özet
Yapay zeka güvenliği ve hizalama çözülmüş sorunlar değildir. Mevcut teknikler (RLHF, Anayasal Yapay Zeka, DPO, kırmızı takım oluşturma) modelleri daha güvenli hale getirir ancak güvenliği garanti etmez. Yorumlanabilirlik araştırması, modellerin dahili olarak ne yaptığını anlama konusunda ilerleme kaydediyor ancak büyük sinir ağlarını tam olarak anlamaktan çok uzağız. Yönetişim ortamı hızla gelişiyor ve AB Yapay Zeka Yasası buna öncülük ediyor. Temel zorluk hâlâ devam ediyor: İstediğimiz şey genellikle kendimiz için bile yeterince tanımlanmamışken, gittikçe daha yetenekli hale gelen yapay zeka sistemlerinin istediğimizi yapmasını nasıl sağlayacaksınız?