---
# Metadata
title: "AI Ethics and Governance"
description: "AI bias, fairness, accountability, regulation, governance frameworks"
category: "AI and Machine Learning"
subcategory: "Ethics and Safety"
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
    changes: "Moved to ethics_and_safety/ subfolder; added subcategory field"
  - version: "1.0.0"
    date: "2026-08-05"
    author: "Nepoznato-Dev"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-09"
review_date: "2027-02-05"
reviewed_by: "AI & Machine Learning Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [ai, ethics, governance, ai-and-machine-learning]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "8 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Yapay Zeka Etiği ve Yönetişim
Yapay zeka sistemleri tarafsız değildir. Üzerinde eğitim aldıkları verileri, yaratıcılarının değerlerini ve bunları uygulayan kuruluşların teşviklerini yansıtırlar. Etik sadece "bunu yapabilir miyiz?" sorusunu sormakla ilgilidir. ama "yapmalı mıyız?" Yönetişim, yapay zekanın sorumlu bir şekilde geliştirilmesini ve kullanılmasını sağlayan yapıları (yasalar, standartlar, gözetim organları) oluşturmakla ilgilidir. Bu dosya, yapay zekanın temel etik boyutlarını ve bunları ele almak için ortaya çıkan yönetişim çerçevelerini kapsamaktadır.
---

## Yapay Zeka için Temel Etik İlkeler
Çoğu yapay zeka etik çerçevesi bir dizi ortak ilke üzerinde birleşir.
| Prensip | Ne Anlama Geliyor | Mücadelesi |
|-----------|-----------------|-----------|
| **Adillik** | Yapay Zeka, korunan gruplara karşı ayrımcılık yapmamalı | Adaleti matematiksel olarak tanımlamak zordur; farklı adalet tanımları çatışabilir |
| **Şeffaflık** | Kullanıcılar yapay zeka ile ne zaman etkileşime girdiklerini ve yapay zekanın nasıl çalıştığını bilmelidir | Tam şeffaflık oyun oynamayı mümkün kılabilir; tescilli sistemler ifşa edilmeye direniyor |
| **Sorumluluk** | Yapay Zeka zarar verdiğinde birileri sorumlu olmalıdır | Sorumluluğu geliştiriciler, dağıtımcılar ve kullanıcılar arasında dağıtın |
| **Gizlilik** | Yapay Zeka, kişisel verilere ve özerkliğe saygı duymalı | Eğitim verileri genellikle kişisel bilgileri içerir; gizlilik ve fayda çatışması |
| **Güvenlik** | Yapay Zeka fiziksel veya psikolojik zarara neden olmamalıdır | Zararın tanımlanması bağlama bağlıdır; uç durumlar öngörülemez |
| **İnsan gözetimi** | İnsanlar anlamlı kontrolü elinde tutmalıdır | Otomasyon önyargısı, insanların yapay zekaya uyması anlamına gelir; gözetim, damgalama haline geliyor |
---

## Yapay Zeka Sistemlerinde Önyargı
### Önyargı Nereden Geliyor?
| Kaynak | Açıklama | Örnek |
|----------|----------------|------------|
| **Eğitim verileri** | Verilere kodlanmış tarihsel önyargılar | İşe alma verileri geçmiş ayrımcılığı yansıtıyor → model ayrım yapıyor |
| **Etiket önyargısı** | İnsan yorumcular önyargılarını empoze ediyor | Açıklama yapanlar tarafından daha düşük puan alan "kadın" adlarına sahip özgeçmişler |
| **Seçim yanlılığı** | Veriler hedef nüfusu temsil etmiyor | Yüz tanıma çoğunlukla açık tenli yüzler üzerinde eğitildi |
| **Ölçüm sapması** | Korunan nitelikler için proxy özellikleri | Posta kodu ırkla ilişkilidir |
| **Algoritmik önyargı** | Optimizasyon küçük önyargıları güçlendiriyor | Eğitim verilerindeki küçük bir boşluk, tahminlerde büyük bir boşluğa dönüşüyor |
### Adillik Metrikleri
| Metrik | Tanımı | Ne Zaman Kullanılmalı |
|----------|---------------|------------|
| **Demografik eşitlik** | Pozitif oran gruplar arasında eşit | Eşit sonuçlar istediğinizde |
| **Eşitleştirilmiş oranlar** | Gerçek pozitif oranı ve yanlış pozitif oranı gruplar arasında eşittir | Eşit hata oranları istediğinizde |
| **Tahmini eşitlik** | Hassasiyet gruplar arasında eşittir | Tahminlerin tüm gruplar için aynı anlama gelmesini istediğinizde |
| **Bireysel adalet** | Benzer kişilere benzer şekilde davranılıyor | Tutarlılık istediğinizde |
**İmkansızlık teoremi**: Genellikle birden fazla adalet tanımını aynı anda karşılayamazsınız. Hangi adalet ölçüsünün kullanılacağını seçmek başlı başına bir değer yargısıdır.
### Önyargı Azaltma
| Sahne | Tekniği |
|----------|---------------|
| **Ön işleme** | Eğitim verilerini yeniden dengeleyin; önyargılı özellikleri kaldırın; sentetik aşırı örnekleme |
| **İşleniyor** | Kayıp fonksiyonuna adalet kısıtlamaları ekleyin; düşmanca önyargıların ortadan kaldırılması |
| **Son işleme** | Grup başına eşikleri ayarlayın; tahminleri kalibre etme |
| **Değerlendirme** | Düzenli adalet denetimleri; ayrıştırılmış performans ölçümleri |
---

## Açıklanabilirlik
### Açıklanabilirlik Neden Önemlidir
| Nedeni | Açıklama |
|----------|----------------|
| **Güven** | Kullanıcıların bir kararın neden verildiğini anlaması gerekiyor |
| **Hata ayıklama** | Geliştiricilerin model hatalarını bulması ve düzeltmesi gerekiyor |
| **Yönetmelik** | GDPR'nin "açıklama hakkı"; AB AI Yasası gereklilikleri |
| **Adillik** | Model davranışını anlamadan önyargıyı tespit edemezsiniz |
| **Sorumluluk** | Kuruluşların otomatik kararları gerekçelendirmesi gerekiyor |
### Açıklama Yöntemleri
| Yöntem | Tür | Nasıl Çalışır | Sınırlama |
|----------|------|------------|------------|
| **ŞAP** | Özelliğin önemi | Oyun teorisini kullanarak her özelliğin katkısını tahmin eder | Hesaplama açısından pahalı; yaklaşımlar |
| **KİREÇ** | Yerel vekil | Tahmin etrafında basit bir modele uyar | Dengesiz; gerçek model mantığını yansıtmıyor |
| **Dikkat görselleştirme** | İç mekanizma | Modelin hangi girdilere katıldığını gösterin | Dikkat ≠ önem; yanıltıcı olabilir |
| **Karşıolgusallar** | Olursa analizi | "Bu özellik farklı olsaydı tahmin değişir miydi?" | Gerçekçi karşıt olgulara dayanır |
| **Özellik ilişkilendirmesi** | Önem puanları | Belirginlik haritaları, entegre gradyanlar | *Nedenini* açıklamıyor; sadece *nerede* |
---

## Yapay Zeka Düzenlemesi
### AB Yapay Zeka Yasası (2026)
Dünyanın ilk kapsamlı yapay zeka yasası.
| Risk Düzeyi | Örnekler | Gereksinimler |
|------------|----------|------------|
| **Kabul edilemez risk** | Sosyal puanlama; bilinçaltı manipülasyon; gerçek zamanlı biyometrik gözetim (istisnalar hariç) | Yasaklandı |
| **Yüksek risk** | Tıbbi AI; otonom araçlar; kanun yaptırımı; kritik altyapı | Uygunluk değerlendirmesi; insan gözetimi; şeffaflık |
| **Sınırlı risk** | Sohbet robotları; derin sahteler; öneri sistemleri | Yapay Zeka katılımını açıklamalıdır |
| **Minimum risk** | Spam filtreleri; video oyunları; çoğu yapay zeka uygulaması | Özel bir gereklilik yok |
### Diğer Düzenleyici Yaklaşımlar
| Bölge | Yaklaşım | Durum |
|----------|----------|----------|
| **Amerika Birleşik Devletleri** | Sektöre özel; idari emirler; gönüllü taahhütler | Parçalanmış; kapsamlı bir federal kanun yok |
| **Birleşik Krallık** | İlkelere dayalı; sektör düzenleyicileri | AI Güvenlik Enstitüsü; yenilik yanlısı yaklaşım |
| **Çin** | Üretken yapay zeka, deepfake'ler ve öneriler için özel düzenlemeler | Aktif yaptırım; içerik gereksinimleri |
| **Kanada** | AIDA (Yapay Zeka ve Veri Yasası) | Önerilen; AB yaklaşımına benzer |
| **Brezilya** | AI düzenleme çerçevesi | Devam ediyor |
---

## Çevresel Etki
Yapay zeka modellerini eğitmek ve çalıştırmak enerji tüketir ve karbon emisyonu üretir.
| Etkinlik | Tahmini Emisyonlar | Karşılaştırma |
|----------|-----------|------------|
| **GPT-4 Eğitimi** | Tahmini 50+ ton CO₂ | Birçok otomobilin yıllık emisyonuna eşdeğer |
| **Büyük bir Transformatörün Eğitimi** | 280-620 ton CO₂ | Bir otomobilin kullanım ömrü boyunca 5 katı emisyon |
| **Günlük çıkarım (1 milyon kullanıcı)** | Devam ediyor; model boyutuna ve donanıma bağlıdır | Zamanla eğitim emisyonlarını aşabilir |
| **7B modeline ince ayar yapma** | 1-5 ton CO₂ | Önemli ama ön eğitimden çok daha az |
### Azaltma
| Strateji | Etki |
|----------|-----------|
| **Verimli donanım** | Yeni GPU'lar hesaplama başına enerji açısından daha verimlidir |
| **Model optimizasyonu** | Daha küçük, nicemlenmiş modeller daha az enerji kullanır |
| **Yeşil enerji** | Yenilenebilir enerjiye sahip güç veri merkezleri |
| **Verimli mimariler** | Uzmanların Karması; seyrek modeller; damıtma |
| **Karbona duyarlı planlama** | Izgara en temiz olduğunda eğitimi çalıştırın |
---

## Fikri Mülkiyet ve Telif Hakkı
| Sayı | Açıklama | Durum |
|----------|----------------|-----------|
| **Telif hakkıyla korunan eserlere ilişkin eğitim** | Modeller izinsiz olarak kitaplar, makaleler ve görseller üzerinde eğitildi | Aktif davalar; adil kullanım tartışması |
| **Yapay zeka tarafından oluşturulan çıktı** | Yapay zeka tarafından oluşturulan içeriğin sahibi kim? | ABD Telif Hakkı Bürosu: Yapay zeka tarafından oluşturulan içerik, yeterli insan yazarlığı olmadan telif hakkına tabi değildir |
| **Stil taklidi** | Yapay Zeka bir sanatçının tarzını taklit edebilir | Yasal olarak gri; etik kaygılar |
| **Opt-out mekanizmaları** | Bazı sağlayıcılar içerik oluşturucuların eğitimden vazgeçmesine izin veriyor | robots.txt; içerik filtreleme |
---

## Sorumlu Açıklama
| Prensip | Açıklama |
|-----------|----------------|
| **Dağıtım öncesi testler** | Kırmızı ekip oluşturma, önyargı denetimleri, piyasaya sürülmeden önce güvenlik değerlendirmeleri |
| **Kademeli dağıtım** | Sınırlı erişimle başlayın; Güvenlik kanıtlandıkça genişletin |
| **Olay raporlama** | Arızalar ve zararlarla ilgili bilgileri belgeleyin ve paylaşın |
| **Hata ödülleri** | Güvenlik açıklarını buldukları için harici araştırmacıları ödüllendirin |
| **Model kartları** | Belge modeli yetenekleri, sınırlamaları ve kullanım amacı |
---

## Veri Kaynağı
| endişe | Açıklama |
|-----------|------------|
| **Eğitim verileri şeffaflığı** | Çoğu sınır modeli eğitim verilerini açıklamıyor |
| **Onay** | Kişilerin verileri bilgisi ve izni dahilinde mi kullanıldı? |
| **Veri zehirlenmesi** | Saldırganlar eğitim setlerine kötü amaçlı veriler ekleyebilir mi? |
| **Veri kümesi kartları** | Veri kümesi bileşimi, toplama yöntemleri ve sınırlamalara ilişkin belgeleme |
| **Filigranlama** | Yapay zeka tarafından oluşturulan içeriği tanımlamak için ona görünmez işaretleyiciler yerleştirme |
---

## Pratik Etik Çerçeveler
### Yapay Zeka Geliştiricileri İçin
| Soru | Neden Önemlidir |
|----------|---------------|
| **Bu sistemden kimler zarar görebilir?** | Etkilenen paydaşları belirler |
| **Model yanlışsa ne olur?** | Hataların maliyetini değerlendirir |
| **Modelin kararları açıklanabilir mi?** | Açıklanabilirlik gerekliliklerini belirler |
| **Eğitim verileri temsili mi?** | Seçim ve ölçüm önyargısını kontrol eder |
| **Arıza modları nelerdir?** | Uç durumları ve yanlış kullanımı öngörür |
| **Sistem nasıl izlenecek?** | Devam eden gözetim planları |
### Yapay Zeka Kullanan Kuruluşlar İçin
| Alıştırma | Açıklama |
|----------|----------------|
| **Yapay zeka yönetim kurulu** | Yapay zeka dağıtımlarını inceleyen işlevler arası ekip |
| **Etki değerlendirmeleri** | Dağıtımdan önce potansiyel zararları değerlendirin |
| **İnsan gözetim süreçleri** | Yapay zeka hata yaptığında üst kademeye iletme yollarını temizleyin |
| **Düzenli denetimler** | Önyargıyı, sapmayı ve istenmeyen sonuçları kontrol edin |
| **Kullanıcı geri bildirim kanalları** | Etkilenen kişilerin sorunları bildirmesine izin verin |
| **Belgeler** | Model kararlarının ve gerekçelerinin kayıtlarını tutun |
---

## Özet
Yapay zeka etiği ve yönetişim mühendislik gereksinimleridir. Önyargı, şeffaflık, çevresel maliyet ve mahremiyet ihlalleri yalnızca etik kaygılar değildir; bunlar gerçek zarara neden olan kusurlardır. Yönetişim ortamı hızla gelişiyor ve AB Yapay Zeka Yasası küresel standardı belirliyor. Düzenleme tek başına yeterli değildir; adalet, açıklanabilirlik ve hesap verebilirlik her yapay zeka geliştiricisinin günlük çalışmasına entegre edilmelidir. Temel soru, güvenilmeye değer sistemlerin nasıl oluşturulacağıdır.