---
# Metadata
title: "Data Pipeline and ETL Failures"
description: "Schema drift, duplicate data, validation gaps, pipeline monitoring"
category: "Lessons from Failures"
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
reviewed_by: "Lessons from Failures Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [data, pipeline, etl, failures, lessons-from-failures]
difficulty_level: "advanced"
prerequisites: []
estimated_reading_time: "5 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# Veri Hattı ve ETL Arızaları
Veri hatları, modern kuruluşların tesisatıdır; verileri kaynak sistemlerden dönüşümler yoluyla veritabanlarına, depolara ve analiz, makine öğrenimi ve karar alma için kullanıldığı göllere taşırlar. Çalışırken kimse fark etmiyor. Başarısız olduklarında kararlar eski verilerle alınır, modeller çöplerle eğitilir, raporlar imkansız rakamları gösterir ve tüm veri platformuna olan güven erozyona uğrar. Veri hattı arızaları, teknoloji kuruluşlarındaki en yaygın ve en maliyetli arızalar arasındadır.
---

## Yaygın Arıza Modları
### Veri Kalitesi Sorunları
| Başarısızlık | Açıklama | Etki | Tespit Zorluğu |
|-----------|------------|-----------|----------|
| **Sessiz veri bozulması** | Veriler herhangi bir hata ortaya çıkmadan yanlış şekilde değiştirildi | Aşağı akış sistemleri kötü verilere güvenir; yanlış bilgiye dayalı kararlar | Çok zor — hata sinyali yok |
| **Şema kayması** | Kaynak sistemi şemasını değiştirir (sütunları ekler, kaldırır, yeniden adlandırır) | İşlem hattı verileri kesiyor veya sessizce bırakıyor | Orta — ardışık düzen başarısız olabilir veya kısmi sonuçlar doğurabilir |
| **Veri türü uyuşmazlığı** | Kaynak, tam sayının beklendiği yere dize gönderir; şamandıra hassas değişiklikleri | Boru hattı başarısız oluyor; veriler kesildi; yuvarlama hataları | Orta — ardışık düzen hatasına veya ince veri sorunlarına neden olabilir |
| **Yinelenen kayıtlar** | Aynı etkinlik birden çok kez işlendi | Şişirilmiş sayımlar; hatalı toplamalar | Zor — her kayıt ayrı ayrı geçerli görünüyor |
| **Boş / eksik değerler** | Beklenen alanlar boş | Hesaplamalar başarısız; modeller yanlış tahminler üretiyor | Orta - boş değer işlemeye bağlıdır |
| **Aralık dışı değerler** | Beklenen sınırların dışındaki değerler (negatif yaşlar; gelecek tarihler) | Çarpık istatistikler; bozuk iş mantığı | Orta — doğrulama kuralları gerektirir |
| **Geç gelen veriler** | Veriler, işleme penceresi kapandıktan sonra gelir | Eksik sonuçlar; kaçırılan rekorlar | Zor — sonuçlar eksiksiz görünüyor ancak değil |
### Boru Hattı Altyapı Sorunları
| Başarısızlık | Açıklama | Etki |
|-----------|------------|-----------|
| **Düzenleme hatası** | Zamanlayıcı (Airflow, Prefect) boru hattını tetiklemiyor | Veriler eski; hiçbir işlem gerçekleşmez |
| **Kaynak tükenmesi** | Ardışık düzende bellek, CPU veya disk yetersiz | Boru hattı çöküyor; kısmi sonuçlar |
| **Bağımlılık hatası** | Yukarı akış sistemi kapalı veya yavaş | Ardışık düzen süresiz olarak bekliyor veya başarısız oluyor |
| **Eşzamanlılık sorunları** | Birden çok işlem hattı aynı verileri aynı anda değiştirir | Yarış koşulları; veri bozulması |
| **Yapılandırma sapması** | Ortam değişiklikleri (ağ, kimlik bilgileri, uç noktalar) ardışık düzene yansıtılmıyor | Ardışık düzen beklenmedik biçimde başarısız oluyor |
| **Geri basınç** | Veriler, üretim hattının işleyebileceğinden daha hızlı ulaşıyor | Büyüyen kuyruklar; artan gecikme |
---

## Vaka Çalışmaları
### Örnek Olay 1: Sessiz Veri Çoğaltma
| Görünüş | Açıklama |
|----------|----------------|
| **Senaryo** | Bir e-ticaret şirketinin sipariş hattı, bir mesaj kuyruğundaki olayları işler |
| **Ne yanlış gitti** | Tüketicinin yeniden başlatılması, mesajların yeniden kullanılmasına neden oldu; tekilleştirme mantığı mevcut değildi |
| **Etki** | Gelir rakamları kimse farkına varmadan 3 hafta boyunca %15 oranında şişirildi |
| **Temel neden** | İdempotency anahtarı yok; tekilleştirme olmadan en az bir kez teslimat |
| **Düzeltme** | Sipariş kimliğine dayalı olarak idempotency anahtarları eklendi; tam olarak bir kez anlambilim uygulandı |
| **Ders** | En az bir kez teslimat tekilleştirme gerektirir; toplamları her zaman kaynak sistemlere göre doğrulayın |
### Örnek Olay 2: Şema Değişikliği Aşağı yönde bozuluyor
| Görünüş | Açıklama |
|----------|----------------|
| **Senaryo** | Bir ödeme sağlayıcı, API yanıtında bir alan adını değiştirir |
| **Ne yanlış gitti** | ETL hattı sessizce boş değerler yazmaya başladı; şema doğrulaması yok |
| **Etki** | Mali raporlar bu ödeme yönteminden 2 ay boyunca sıfır gelir elde edildiğini gösterdi |
| **Temel neden** | Besleme sırasında şema doğrulaması yok; boş değerler geçerli olarak değerlendirilir |
| **Düzeltme** | Uyarılarla şema doğrulama eklendi; zorunlu alanlar zorunlu kılındı; boş kontroller |
| **Ders** | Dış şemaların istikrarlı kalmasına asla güvenmeyin; sınırda doğrulama |
### Örnek Olay 3: Zaman Dilimi Felaketi
| Görünüş | Açıklama |
|----------|----------------|
| **Senaryo** | Küresel bir şirket, ofislerdeki günlük ölçümleri bir araya getiriyor |
| **Ne yanlış gitti** | Bazı kaynaklar UTC'yi, bazıları ise yerel saati kullanıyordu; boru hattı normalleşmedi |
| **Etki** | Günlük toplamlar eşleşmedi; bazı işlemler yanlış günde sayıldı; ay sonu kapanışı yanlıştı |
| **Temel neden** | Standart bir saat dilimi politikası yok; zaman damgaları tutarsız bir şekilde saklanıyor |
| **Düzeltme** | Tüm zaman damgaları UTC olarak saklanır; yalnızca sunum katmanında yerel saate dönüştürme |
| **Ders** | Her yerde UTC'yi standartlaştırın; her sınırdaki saat dilimleri konusunda açık olun |
---

## Önleme Stratejileri
### Veri Doğrulaması
| Strateji | Açıklama | Araç Örnekleri |
|----------|----------------|---------------|
| **Şema doğrulama** | Verilerin her aşamada beklenen şemayla eşleştiğini doğrulayın | Büyük Beklentiler; Deequ; Soda |
| **Aralık kontrolleri** | Değerler beklenen sınırlar dahilinde | Özel iddialar; dbt testleri |
| **Tazelik kontrolleri** | Veriler yararlı olacak kadar günceldir | Zaman damgalarını izleme; SLA uyarıları |
| **Hacim kontrolleri** | Satır sayıları beklenen aralıkta | Satır sayılarında anormallik tespiti |
| **Referans bütünlüğü** | Yabancı anahtarlar eşleşiyor; yetim kayıtlara hayır | SQL kısıtlamaları; veri kalitesi araçları |
| **Kaynaklar arası mutabakat** | Kaynak ve hedef arasındaki toplamlar eşleşiyor | Otomatik mutabakat işleri |
### Boru Hattı Tasarım Modelleri
| Desen | Açıklama | Fayda |
|-----------|------------|------------|
| **İdempotans** | İşlem hattını birden çok kez çalıştırmak aynı sonucu verir | Yeniden denemek güvenlidir; kopya yok |
| **Atomite** | İşlem hattı ya tamamen başarılı olur ya da tamamen başarısız olur (kısmi durum yok) | Yarı işlenmiş veri yok |
| **Kontrol noktası oluşturma** | Her aşamada ilerlemeyi kaydedin; son kontrol noktasından devam et | Hata toleransı; yeniden işlemeye gerek yok |
| **Ölü mektup kuyrukları** | Başarısız olan kayıtlar incelenmek üzere ayrı bir kuyruğa gider | Veri kaybı yok; araştırabilir ve tekrar oynatabilirsiniz |
| **Devre kesiciler** | Aşağı akış başarısız olduğunda işlemeyi durdurun | Art arda gelen arızaları önleyin |
| **Veri sözleşmeleri** | Üreticiler ve tüketiciler arasında veri formatına ilişkin anlaşma | Şema değişiklikleri koordine ediliyor |
### İzleme ve Uyarı
| Neler İzlenmeli | Neden | Nasıl |
|----------------|-----|-----|
| **Ardışık düzen süresi** | Sürenin artması sorunlara işaret ediyor | Trend analizi; SLA takibi |
| **Satır sayıları** | Ani değişiklikler sorunlara işaret eder | Geçmiş ortalamalarla karşılaştırın |
| **Boş oranlar** | Artan boş değerler şema veya kaynak sorunlarına işaret ediyor | Sütun düzeyinde boş izleme |
| **Veri güncelliği** | Eski veriler, işlem hattının çalışmadığı anlamına gelir | En son kaydın zaman damgası |
| **Aşağı yönlü etki** | Raporlar ve modeller doğru verileri kullanıyor mu? | Uçtan uca veri kökeni |
| **Kaynak kullanımı** | İŞLEMCİ; hafıza; disk; ağ | Altyapı izleme |
---

## Kurtarma Stratejileri
| Durum | Strateji |
|---------------|----------|
| **Kötü veriler zaten depoda** | Etkilenen zaman aralığını belirleyin; kaynaktan yeniden işleyin; alt tüketicilere bildirimde bulunun |
| **Çalışma ortasında boru hattı arızası** | Idempotent tasarım güvenli yeniden çalıştırmaya olanak tanır; kontrol noktası özgeçmişe izin verir |
| **Şema değişikliği satış hattını bozdu** | Dönüşümü düzeltin; etkilenen verileri doldurun; şema geliştirme yönetimi ekleme |
| **Sessiz yolsuzluk geç keşfedildi** | Kök neden analizi; patlama yarıçapını belirleyin; yeniden işleme; tekrarlamayı yakalamak için izleme ekleyin |
| **Veri kaybı** | Yedeklemeden geri yükleyin; kaynaktan tekrar oynatma; kaybın geri kazanılabilir olup olmadığının değerlendirilmesi |
---

## Özet
Veri hattı arızaları her yerde bulunur ve genellikle uygulama kesintilerinden daha maliyetlidir çünkü bariz hatalar yerine yanlış yanıtlara neden olurlar. Sessiz veri bozulması, şema kayması, kopyalar, saat dilimi hataları ve eksik değerler en yaygın suçlulardır. Temel önleme stratejileri şunlardır: verileri her sınırda (şema, aralık, hacim, tazelik) doğrulamak; boru hatlarını bağımsız ve atomik olacak şekilde tasarlamak; her şeyi izleyin (süre, satır sayısı, sıfır oranları, tazelik); başarısız kayıtlar için geçersiz mektup kuyruklarını kullanın; ve üreticiler ile tüketiciler arasında veri sözleşmeleri kurulması. Arızalar meydana geldiğinde, müdahale kök neden analizini, etkilenen verilerin yeniden işlenmesini, alt tüketicilere bildirimi ve - daha da önemlisi - gelecekte aynı sınıftaki arızaları yakalamak için izlemenin eklenmesini içermelidir. Bunu doğru anlayan kuruluşlar, veri hatlarına üretim yazılımıyla aynı titizlikle davranır: test etme, izleme, uyarı verme, olay müdahalesi ve otopsi.