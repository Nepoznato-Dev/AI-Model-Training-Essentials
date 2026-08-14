<!--
---
# Metadata
title: "Mobile Development"
description: "iOS, Android, React Native, Flutter, mobile architecture"
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
tags: [mobile, development, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "7 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Mobil Geliştirme
Mobil geliştirme, akıllı telefonlar ve tabletler için, özellikle de iOS (Apple) ve Android (Google) için uygulamalar oluşturma uygulamasıdır. Küçük ekranlar için kullanıcı arayüzü tasarımından pil ömrünün yönetilmesine, ağ istikrarsızlığının yönetilmesine ve uygulamaların mağazalar aracılığıyla dağıtılmasına kadar her şeyi kapsar. Platformlar arası çerçevelerin artık çoğu kullanım durumunda yerel geliştirmeyle rekabet etmesiyle bu alan önemli ölçüde olgunlaştı.
---

## Mobil Ortam
| Platformu | Geliştirici | Dil(ler) | Mağaza | Pazar Payı (Küresel) |
|----------|-----------|------------|----------|-----------|
| **Android** | Google | Kotlin, Java | Google Play | ~%72 |
| **iOS** | elma | Swift, Objective-C | Uygulama Mağazası | ~%27 |
---

## Yerel Kalkınma
### Android
| Görünüş | Ayrıntılar |
|----------|------------|
| **Dil** | Kotlin (birincil), Java (eski) |
| **Kullanıcı Arayüzü Çerçevesi** | Jetpack Compose (modern), XML düzenleri (eski) |
| **Sistem oluştur** | Kepçe |
| **IDE** | Android Stüdyosu |
| **Min. SDK** | Geliştirici seçer; çoğu hedef API 24+ (Android 7.0, 2016) |
| **Dağıtım** | Google Oyun Mağazası; bazı pazarlarda alternatif mağazalar |
### iOS
| Görünüş | Ayrıntılar |
|----------|------------|
| **Dil** | Swift (birincil), Objective-C (eski) |
| **Kullanıcı Arayüzü Çerçevesi** | SwiftUI (modern), UIKit (olgun) |
| **Sistem oluştur** | Xcode derleme sistemi |
| **IDE** | Xcode (yalnızca macOS) |
| **Min. sürüm** | Geliştirici seçer; çoğu hedef iOS 16+ |
| **Dağıtım** | Apple App Store (çoğu uygulama için yalnızca seçenek) |
---

## Platformlar Arası Çerçeveler
Bir kez oluşturun, hem iOS hem de Android'e dağıtın.
| Çerçeve | Dil | İşleme | Performans | En İyisi |
|-----------|----------|-----------|---------------|----------|
| **Çarpıntı** | Dart | Özel motor (Skia/Pervane) | Yerliye yakın | Zengin özel kullanıcı arayüzleri; farklı platformlarda tutarlı görünüm |
| **Yerel Tepki** | JavaScript/TypeScript | Köprü aracılığıyla yerel bileşenler | İyi (Yeni Mimari bunu geliştirir) | Web/JS deneyimi olan ekipler |
| **Kotlin Çoklu Platform** | Kotlin | Platform başına yerel kullanıcı arayüzü | Yerli | İş mantığını paylaşmak; yerel kullanıcı arayüzü |
| **MAUI** (.NET) | C# | Yerel kontroller | İyi | .NET ekipleri; kurumsal uygulamalar |
| **İyonik / Kapasitör** | HTML/CSS/JS | Web Görünümü | Aşağı | Basit uygulamalar; web ekipleri |
### Flutter vs React Native
| Görünüş | Çarpıntı | Yerel Tepki |
|-----------|------------|-------------|
| **Dil** | Dart | JavaScript/TypeScript |
| **Kullanıcı arayüzü oluşturma** | Her şeyi kendisi çizer (platformlar arasında tutarlıdır) | Yerel bileşenleri kullanır (platforma özel görünüm) |
| **Sıcak yeniden yükleme** | Mükemmel | İyi |
| **Ekosistem** | Hızla büyüyor; widget tabanlı | Büyük; npm ekosistemi |
| **Öğrenme eğrisi** | Dart'ı öğrenmeniz gerekiyor | Web geliştiricileri için daha kolay |
| **Platform entegrasyonu** | Yerel kod için platform kanalları | Köprü aracılığıyla yerel modüller |
| **Performans** | Harika; yerliye yakın | İyi; köprünün yükü (Yeni Mimari ile azaltılmıştır) |
---

## Mobil Mimari Desenleri
| Desen | Açıklama | Ne Zaman Kullanılmalı |
|-----------|---------------|------------|
| **MVC** | Model-Görünüm-Denetleyici | Basit uygulamalar; web geliştiricilerine tanıdık |
| **MVVM** | Model-Görünüm-GörünümModel; veri bağlama | En modern mobil uygulamalar |
| **MVI** | Model-Görünüm-Niyet; tek yönlü veri akışı | Karmaşık devlet yönetimi; Flutter (BLoC/Riverpod ile) |
| **Temiz Mimari** | Bağımlılığı tersine çeviren katmanlar | Büyük takımlar; karmaşık iş mantığı |
---

## Mobil Cihazlarla İlgili Önemli Sorunlar
### Çevrimdışı İlk Tasarım
Mobil uygulamalar güvenilir internet olmadan çalışmalıdır.
| Strateji | Açıklama |
|----------|----------------|
| **Yerel veritabanı** | Verileri cihazda depolayın (SQLite, Room, CoreData, Realm) |
| **Senkronizasyon stratejisi** | Çevrimiçiyken sunucuyla senkronize edin; anlaşmazlıkları çözmek |
| **İyimser kullanıcı arayüzü** | Kullanıcı arayüzünü hemen güncelleyin; sunucu yanıt verdiğinde uzlaştır |
| **Önbellek** | API yanıtlarını önbelleğe alın; çevrimdışıyken önbellekten hizmet ver |
### Performans
| endişe | Çözüm |
|-----------|----------|
| **Uygulama başlatma süresi** | Tembel yükleme; başlatma işini en aza indirin |
| **Bellek kullanımı** | Görüntü sıkıştırma; bellek sızıntılarını önleyin; profil oluşturma araçlarını kullanın |
| **Pil tüketimi** | Arka planda çalışmayı azaltın; toplu ağ istekleri; verimli konum hizmetlerini kullanın |
| **Ağ verimliliği** | Yükleri sıkıştırın; sayfalandırmayı kullanın; agresif bir şekilde önbelleğe alma |
| **Liste kaydırma** | Görünümleri geri dönüştürün; görüntüler için yavaş yüklemeyi kullanın |
### Güvenlik
| endişe | Çözüm |
|-----------|----------|
| **Kullanılmayan veriler** | Hassas verileri şifreleyin (iOS'ta Anahtar Zinciri, Android'de EncryptedSharedPreferences) |
| **Ağ** | Her zaman HTTPS; hassas uygulamalar için sertifika sabitleme |
| **Kimlik doğrulama** | Biyometri (Yüz Kimliği, parmak izi); OAuth; jeton depolama |
| **Kod gizleme** | Android için ProGuard/R8; iOS için bit kodu |
| **Jailbreak/kök algılama** | Güvenliği ihlal edilmiş cihazları tespit edin; işlevselliği sınırla |
---

## Uygulama Yaşam Döngüsü
| Devlet | Açıklama | Ne Yapmalı |
|----------|----------------|------------|
| **Ön plan (etkin)** | Kullanıcı uygulamayla etkileşimde bulunuyor | Normal çalışma |
| **Arkaplan** | Uygulama görünmüyor ancak hâlâ bellekte | Animasyonları duraklatın; durumu kaydet |
| **Askıya alındı** | İşletim sistemi kaynakları korumak için uygulamayı dondurdu | Hiç bir şey; uygulama donduruldu |
| **Sonlandırıldı** | İşletim sistemi hafızayı boşaltmak için uygulamayı sonlandırdı | Bir sonraki başlatmada durumu geri yükle |
---

## Anında Bildirimler
| Platformu | Hizmet | Protokol |
|----------|------------|----------|
| **iOS** | APN'ler (Apple Anında Bildirim hizmeti) | HTTP/2 |
| **Android** | FCM (Firebase Bulut Mesajlaşma) | HTTP/v1 |
| Bildirim Türü | Açıklama |
|---------------------|----------------|
| **Veri bildirimi** | Sessiz; uygulaması yükü işler | Arka plan güncellemeleri |
| **Bildirimi görüntüle** | Bildirim tepsisinde gösterilir | Kullanıcı uyarıları |
| **Zengin bildirim** | Görüntüler, eylemler veya özel kullanıcı arayüzü içerir | Geliştirilmiş kullanıcı etkileşimi |
---

## Uygulama Dağıtımı
| Platformu | Mağaza | İnceleme Zamanı | Gelir Kesintisi |
|----------|-------|------------|-------------|
| **iOS** | Uygulama Mağazası | 24-48 saat | %30 (küçük işletmeler için %15) |
| **Android** | Google Play | Saatlerden günlere | %30 (ilk 1 milyon dolar için %15) |
| **Android (alternatif)** | Samsung Galaxy Mağazası, Amazon Uygulama Mağazası, F-Droid | Değişir | Değişir |
### Mobil Cihazlar için CI/CD
| Araç | Amaç |
|------|------------|
| **Hızlı Yol** | Derlemeleri, ekran görüntülerini, imzalamayı ve dağıtımı otomatikleştirin |
| **GitHub Eylemleri** | iOS derlemeleri için macOS çalıştırıcılarına sahip CI/CD |
| **Bitris** | Mobil odaklı CI/CD |
| **Uygulama Merkezi** (Microsoft) | İnşa edin, test edin, dağıtın (gün batımı; alternatifler ortaya çıkıyor) |
| **EAS** (Expo Uygulama Hizmetleri) | React Native/Expo için bulut derlemeleri |
---

## Test etme
| Tür | Araçlar | Amaç |
|------|----------|-----------|
| **Birim testleri** | JUnit, XCTest | İş mantığını test edin |
| **Widget testleri** | Flutter Widget Testi, Robolectric | Kullanıcı arayüzü bileşenlerini ayrı ayrı test edin |
| **Entegrasyon testleri** | Espresso (Android), XCUITest (iOS), Flutter Entegrasyonu | Bileşen etkileşimlerini test edin |
| **E2E testleri** | Detoks, Appium, Maestro | Gerçek/simüle edilmiş cihazlarda tam kullanıcı akışlarını test edin |
| **Performans testleri** | Android Profiler, Araçlar (iOS) | Kare hızını, belleği, CPU'yu ölçün |
---

## Özet
Mobil geliştirme, yerel (en iyi performans, platforma özel) ve platformlar arası (paylaşılan kod tabanı, daha hızlı yineleme) arasında bir seçim sunar. Flutter ve React Native, çoğu uygulama için çapraz platformların doğru seçim olduğu noktaya kadar olgunlaştı. Temel zorluklar çerçeveden bağımsız olarak aynı kalıyor: çevrimdışı öncelikli tasarım, sınırlı donanımda performans, pil verimliliği, güvenilmeyen cihazlarda güvenlik ve uygulama mağazası inceleme süreçlerinde gezinme. Bu alan, hızlı başlatma, sorunsuz kaydırma ve zayıf bağlantının zarif bir şekilde ele alınması gibi ilk önce kullanıcı deneyimini düşünen geliştiricileri ödüllendiriyor.