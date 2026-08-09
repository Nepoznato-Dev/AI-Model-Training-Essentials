---
# Metadata
title: "Data Ethics and Privacy"
description: "GDPR, data consent, algorithmic bias, dark patterns, anonymisation"
category: "Data Science and Analytics"
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
reviewed_by: "Data Science & Analytics Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [data, ethics, privacy, data-science-and-analytics]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "6 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# Veri Etiği ve Gizlilik
Veri etiği, veri toplama, analiz ve dağıtımının insanların haklarını, özerkliğini ve refahını nasıl etkilediğinin incelenmesidir. Gizlilik, kişisel bilgileri kimin kontrol ettiği ve nasıl paylaşıldığıyla ilgili özel bir konudur. Bu konular akademik tartışmalardan ön sayfa haberlerine taşındı: GDPR'nin uygulanması, milyarlarca kullanıcıyı etkileyen veri ihlalleri ve teknoloji şirketlerinin veri uygulamalarının demokrasi, eşitlik ve bireysel özgürlük açısından gerçek sonuçlar doğurduğuna dair artan kamuoyu farkındalığı.
---

## Veri Etiği Neden Önemlidir
| endişe | Açıklama | Gerçek Dünya Etkisi |
|-----------|-------------|------------------|
| **Gözetim kapitalizmi** | Şirketler kişisel verilerden geniş ölçekte para kazanıyor | Mahremiyet kaybı; davranışın manipülasyonu |
| **Algoritmik önyargı** | Önyargılı verilerle eğitilen modeller önyargıyı yeniden üretiyor | İşe alma, ödünç verme ve polislik konularında ayrımcılık |
| **Bilgilendirilmiş onam** | Kullanıcılar neyi kabul ettiklerini anlamıyor | Bir amaç için toplanan veriler başka bir amaç için kullanılıyor |
| **Veri ihlalleri** | Zayıf güvenlik nedeniyle hassas veriler açığa çıkıyor | Kimlik hırsızlığı; mali dolandırıcılık; itibar kaybı |
| **Kabarcıkları filtreleyin** | Kişiselleştirilmiş yayınlar mevcut inançları güçlendiriyor | Siyasi kutuplaşma; yanlış bilgi |
| **Koyu desenler** | Kullanıcıları veri paylaşmaları için kandırmak üzere tasarlanmış kullanıcı arayüzü | İstenmeyen abonelikler; istenmeyen veri paylaşımı |
---

## Gizlilik Çerçeveleri ve Düzenlemeleri
### Başlıca Gizlilik Yasaları
| Yönetmelik | Bölge | Temel Gereksinimler |
|-----------|-----------|------|
| **GDPR** (Genel Veri Koruma Yönetmeliği) | AB / AEA | İşlemenin yasal dayanağı; erişim hakkı; unutulma hakkı; veri taşınabilirliği; 72 saatlik ihlal bildirimi; küresel gelirin %4'üne kadar para cezaları |
| **CCPA / CPRA** (Kaliforniya Gizlilik Hakları Yasası) | Kaliforniya, ABD | Bilme hakkı; silme hakkı; satıştan vazgeçme hakkı; çocuklar için sınırlı katılım |
| **LGPD** (Lei Geral de Proteção de Dados) | Brezilya | GDPR'ye benzer; yasal dayanak; veri sahibi hakları; DPO gerekli |
| **PIPL** (Kişisel Bilgilerin Korunması Kanunu) | Çin | Onay gerekli; veri yerelleştirmesi; sınır ötesi transfer kısıtlamaları |
| **POPIA** (Kişisel Bilgilerin Korunması Yasası) | Güney Afrika | Yasal işleme koşulları; veri sahibi hakları; regülatör |
| **DPDP Yasası** (Dijital Kişisel Verilerin Korunması Yasası) | Hindistan | Onay; amaç sınırlaması; veri sorumlusu hakları; veri güveni yükümlülükleri |
### GDPR Temel İlkeleri
| Prensip | Gereksinim |
|-----------|----------------|
| **Yasallık, adalet, şeffaflık** | Verileri yasal olarak işlemek; kullanıcıları yanıltmayın; Ne topladığınız konusunda açık olun |
| **Amaç sınırlaması** | Verileri yalnızca belirtilen, açık amaçlarla toplayın |
| **Veri minimizasyonu** | Yalnızca gerçekten ihtiyacınız olanı toplayın |
| **Doğruluk** | Verileri doğru tutun; hatalı verileri düzeltin veya silin |
| **Depolama sınırlaması** | Verileri gereğinden uzun süre saklamayın |
| **Bütünlük ve gizlilik** | Verileri yetkisiz erişime ve kayba karşı koruyun |
| **Sorumluluk** | Yukarıdakilerin tümüne uygunluğu gösterin |
---

## Gizliliği Koruma Teknikleri
| Tekniği | Nasıl Çalışır | Takas |
|-----------|----------------|-----------|
| **Anonimleştirme** | Kişisel olarak tanımlanabilir bilgileri (PII) kaldırın | Tamamen anonimleştirmek zor; yeniden kimlik riski |
| **Takma ad kullanma** | Tanımlayıcıları takma adlarla değiştirin | Geri dönüşümlü; GDPR kapsamında hala kişisel veriler |
| **Farklı gizlilik** | Sorgu sonuçlarına kalibre edilmiş gürültü ekleme | Doğruluğu azaltır; matematiksel gizlilik garantisi sağlar |
| **Birleşik öğrenim** | Modelleri cihazda eğitin; yalnızca model güncellemelerini paylaş | Daha yavaş eğitim; iletişim yükü |
| **Güvenli çok taraflı hesaplama** | Birden çok taraf, girdileri açıklamadan bir işlevi hesaplar | Hesaplama açısından pahalı; uygulanması karmaşık |
| **Homomorfik şifreleme** | Şifrelenmiş veriler üzerinde hesaplamalar yapın | Çok yavaş; sınırlı operasyon desteği |
| **Veri maskeleme** | Verilerin bazı kısımlarını gizleyin (ör.`***-**-1234`) | Basit ama sınırlı koruma |
---

## Etik Veri Toplama
### Etik Koleksiyon İlkeleri
| Prensip | Açıklama |
|-----------|----------------|
| **Bilgilendirilmiş onam** | Kullanıcılar neye rıza gösterdiklerini anlar; legalese'ye gömülmemiş |
| **Amaç şeffaflığı** | Verilerin neden toplandığını ve nasıl kullanılacağını açıkça belirtin |
| **Minimum koleksiyon** | Yalnızca belirtilen amaç için gerekenleri toplayın |
| **Kullanıcı kontrolü** | Kullanıcıların verilerine erişmesine, düzeltmesine, indirmesine ve silmesine izin verin |
| **Sınırlı saklama** | Artık ihtiyaç duyulmadığında verileri silin |
| **Etki değerlendirmesi** | Hassas verileri toplamadan önce olası zararları değerlendirin |
### Yaygın Koyu Desenler
| Desen | Açıklama | Örnek |
|-----------|------------|------------|
| **Gizlilik hırsızlığı** | Kullanıcıları amaçladıklarından daha fazlasını paylaşmaları için kandırın | Kayıt sırasında "Arkadaşlarınızla paylaşın" seçeneği önceden işaretlendi |
| **Roach moteli** | Kaydolmak kolaydır; iptal edilmesi zor | Hesabın silinmesi için telefon görüşmesi veya faks gerekir |
| **Zorunlu süreklilik** | Ücretsiz deneme, önceden haber verilmeden ücretliye dönüştürülür | Abonelik ücretleri kredi kartında görünür |
| **Utanmayı onaylayın** | Kullanıcıları katılma konusunda suçlayın | "Hayır teşekkürler, tasarruf etmek istemiyorum" |
| **Gizli ayarlar** | Menülerin derinliklerine gömülü gizlilik denetimleri | Devre dışı bırakma 5 ayar düzeyi altında gizlenmiştir |
---

## Verilerde Önyargı ve Adalet
| Önyargı Kaynağı | Açıklama | Örnek |
|----------------|----------------|-----------|
| **Seçim yanlılığı** | Veriler hedef nüfusu temsil etmiyor | İşe alma modelini yalnızca tek bir demografiden elde edilen verilerle eğitmek |
| **Tarihsel önyargı** | Verilere kodlanmış geçmiş ayrımcılık | Önyargılı polislik uygulamalarını yansıtan tutuklama kayıtları |
| **Ölçüm sapması** | Proxy olarak kullanılan değişkenler hatalı | Posta kodunu kredi itibarı için proxy olarak kullanma |
| **Toplama önyargısı** | Farklı grupları homojen olarak ele almak | Tüm etnik kökenler için tek model; gruba özgü kalıpları yok sayar |
| **Hayatta kalma önyargısı** | Yalnızca başarılı vakalara bakıyoruz | Başarısız olanları göz ardı ederken başarılı girişimleri incelemek |
### Etki Azaltma Stratejileri
| Strateji | Açıklama |
|----------|----------------|
| **Çeşitli veri toplama** | Eğitim verilerinin etkilenen tüm grupları temsil ettiğinden emin olun |
| **Önyargı denetimi** | Modelleri gruplar arasında farklı etkiler açısından düzenli olarak test edin |
| **Adillik ölçütleri** | Demografik eşitliği, fırsat eşitliğini, eşitlenmiş oranları ölçün |
| **İnsan incelemesi** | İnsanların yüksek riskli kararları gözden geçirmesini sağlayın |
| **Şeffaflık raporları** | Demografi genelinde model performansına ilişkin verileri yayınlayın |
| **Topluluk katılımı** | Etkilenen toplulukları tasarım ve değerlendirmeye dahil edin |
---

## Veri Yönetişimi
### Veri Yönetişimindeki Roller
| Rol | Sorumluluk |
|------|---------------|
| **Veri sahibi** | Veri alanından sorumlu kıdemli lider |
| **Veri sorumlusu** | Günlük yönetim; kalite; sınıflandırma |
| **Veri koruma görevlisi (DPO)** | GDPR uyumluluğu; gizlilik etki değerlendirmeleri; düzenleyicilerle irtibat |
| **Veri mühendisi** | Boru hatları; depolamak; dönüşüm |
| **Veri bilimcisi** | Analiz; modelleme; raporlama |
| **Veri gizliliği analisti** | Uyumluluğu izleyin; veri sahibinin isteklerini ele almak |
### Veri Sınıflandırması
| Sınıflandırma | Açıklama | İşleme |
|---------------|---------------|----------|
| **Herkese açık** | Özgürce paylaşılabilir | Kısıtlama yok |
| **Dahili** | Yalnızca çalışanlar için | Erişim kontrolleri; harici paylaşım yok |
| **Gizli** | Hassas iş verileri | Şifreleme; sıkı erişim kontrolleri; denetim günlüğü |
| **Kısıtlı** | Son derece hassas; düzenlenmiş (PII, sağlık, finans) | Beklemede ve aktarım sırasında şifreleme; DLP'yi; minimum erişim |
---

## Özet
Veri etiği ve gizlilik artık isteğe bağlı konular değil; bunlar yasal gereklilikler, iş zorunlulukları ve ahlaki yükümlülüklerdir. GDPR ve benzeri düzenlemeler net kurallar belirler: minimum düzeyde toplayın, şeffaf bir şekilde kullanın, titizlikle koruyun ve kontrolü kullanıcılara verin. Farklı gizlilik, birleştirilmiş öğrenme ve şifreleme gibi gizliliği koruyan teknikler, bireyleri ifşa etmeden verilerden değer elde edilmesini mümkün kılar. Ancak teknoloji tek başına yeterli değildir. Kuruluşların veri yönetişim yapılarına, önyargı denetim uygulamalarına ve kişisel verileri yalnızca sömürülmekle kalmayıp, yönetilmesi gereken bir şey olarak ele alan bir kültüre ihtiyacı var. Bunu doğru yapan şirketler güven kazanacak; olmayanlar ise düzenleyici para cezalarıyla, kamuoyunun tepkisiyle ve kullanıcılarının veri paylaşma isteğinin yavaş yavaş azalmasıyla karşı karşıya kalacak.