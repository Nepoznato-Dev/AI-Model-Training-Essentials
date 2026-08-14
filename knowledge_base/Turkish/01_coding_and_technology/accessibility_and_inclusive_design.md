<!--
---
# Metadata
title: "Accessibility and Inclusive Design"
description: "WCAG, inclusive UX, assistive technology, accessible coding"
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
tags: [accessibility, inclusive, design, coding-and-technology]
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

-->
# Erişilebilirlik ve Kapsayıcı Tasarım
Erişilebilirlik (genellikle a11y olarak kısaltılır), yazılımın görsel, işitsel, motor, bilişsel ve nörolojik engelli kişiler de dahil olmak üzere herkes tarafından kullanılabilir hale getirilmesi uygulamasıdır. Birçok yargı alanında yasal bir zorunluluktur ve standart bir mühendislik uygulamasıdır. Erişilebilir yazılım herkes için daha iyi bir yazılımdır çünkü engelli kullanıcıları destekleyen tasarım kararları (açık yapı, klavyede gezinme, yeterli kontrast, okunabilir metin) tüm kullanıcılar için deneyimi geliştirir.
---

## Erişilebilirlikten Kimler Yararlanır?
| Engellilik Türü | Örnekler | Yardımcı Teknoloji |
|----------------|---------|----------|
| **Görsel** | Körlük, az görme, renk körlüğü | Ekran okuyucular (JAWS, NVDA, VoiceOver); büyüteçler; yüksek kontrastlı modlar |
| **İşitsel** | Sağırlık, işitme güçlüğü | Altyazılar; transkriptler; görsel uyarılar |
| **Motorlu** | Sınırlı el becerisi, felç, titreme | Yalnızca klavyeyle gezinme; ses kontrolü; cihazları değiştir; göz takibi |
| **Bilişsel** | Disleksi, DEHB, otizm, hafıza bozuklukları | Açık dil; tutarlı gezinme; dikkat dağıtıcı unsurların azaltılması |
| **Geçici** | Kırık kol, parlak güneş ışığı, gürültülü ortam | Kalıcı engellilikle aynı konaklama olanakları |
| **Durumsal** | Bir bebeği tutuyor, araba kullanıyor, bir eli meşgul | Ses arayüzleri; büyük dokunmatik hedefler |
**Önemli bilgi**: Engelli kullanıcılar için tasarlanan erişilebilirlik özellikleri herkese yardımcı olur. Kaldırım kesimleri (kaldırımlardaki rampalar) tekerlekli sandalyeler için tasarlanmıştır ancak bebek arabalı ebeveynler, arabalı teslimat işçileri ve bagajlı yolcular tarafından kullanılır.
---

## Web Erişilebilirliği (WCAG)
Web İçeriği Erişilebilirlik Yönergeleri (WCAG), web erişilebilirliğine yönelik uluslararası standarttır.
### WCAG İlkeleri (POUR)
| Prensip | Gereksinim |
|-----------|----------------|
| **Algılanabilir** | Bilgi, kullanıcıların algılayabileceği şekillerde sunulabilir olmalıdır (metin alternatifleri, altyazılar, uyarlanabilir düzen) |
| **Çalıştırılabilir** | Arayüz gezinilebilir ve kullanılabilir olmalıdır (klavyeden erişilebilir, yeterli zaman, ele geçirmeye neden olacak içerik olmamalıdır) |
| **Anlaşılabilir** | Bilgi ve kullanım anlaşılır olmalıdır (okunabilir, öngörülebilir, giriş yardımı) |
| **Sağlam** | İçerik mevcut ve gelecekteki yardımcı teknolojilerle çalışmalıdır |
### WCAG Uyumluluk Seviyeleri
| Seviye | Gereksinimler | Tipik Hedef |
|----------|----------------|---------------|
| **Bir** | Asgari seviye; 30 başarı kriteri | Bazı yargı bölgelerinde yasal minimum |
| **AA** | En yaygın engelleri ele alıyor | Çoğu kuruluş için standart hedef |
| **AAA** | En yüksek seviye; her içerik bunu başaramaz | Uzmanlaşmış içerik; eğitim siteleri |
### Temel Başarı Kriterleri (AA Düzeyi)
| Kriter | Gereksinim | Nasıl Başarıya Ulaşılır |
|-----------|----------------|---------------|
| **1.1.1 Metin dışı içerik** | Tüm resimlerin metin alternatifleri var | `alt`öznitelikleri;  simgeler için`aria-label`|
| **1.3.1 Bilgi ve ilişkiler** | Yapı programlı olarak aktarıldı | Anlamsal HTML; başlıklar; listeler; görülecek yerler |
| **1.4.3 Kontrast (minimum)** | Metnin kontrast oranı en az 4,5:1 | Kontrast denetleyicileriyle test edin; erişilebilir renk paletlerini seçin |
| **1.4.4 Metni yeniden boyutlandır** | Metin kayıpsız olarak %200'e kadar yeniden boyutlandırılabilir | Göreli birimleri kullanın (rem, em); duyarlı tasarım |
| **2.1.1 Klavye** | Tüm işlevler klavye aracılığıyla kullanılabilir | Klavye tuzağı yok; görünür odak göstergeleri |
| **2.4.3 Odaklanma sırası** | Odaklanma sırası anlamı ve kullanılabilirliği korur | Mantıksal sekme sırası; DOM sırası görsel sırayla eşleşiyor |
| **2.4.7 Odak görünür** | Klavye odağı görsel olarak belirtilir | CSS`:focus-visible`stilleri; değiştirilmeden asla`outline: none`|
| **3.3.2 Etiketler veya talimatlar** | Girişlerin etiketleri vardır | `<label>`öğeleri; `aria-label`|
| **4.1.2 Ad, rol, değer** | Kullanıcı arayüzü bileşenlerinin erişilebilir adları ve rolleri vardır | ARIA nitelikleri; anlamsal HTML |
---

## ARIA (Erişilebilir Zengin İnternet Uygulamaları)
ARIA, yerleşik anlambilime sahip olmayan HTML öğelerine erişilebilirlik bilgileri ekler.
### ARIA Rolleri
| Rol | Amaç | Örnek |
|------|---------|--------|
| `button`| Bir öğeyi düğme olarak tanımlar | Düğme tarzında bir`<div>`|
| `dialog`| Kalıcı veya kalıcı olmayan iletişim | Özel modal bileşenler |
| `tablist`/`tab`/`tabpanel`| Sekme arayüzü | Özel sekme bileşenleri |
| `alert`| Dinamik olarak görünen önemli mesaj | Hata bildirimleri |
| `progressbar`| İlerleme göstergesi | Durumlar yükleniyor |
| `menu`/`menuitem`| Menüde gezinme | Açılır menüler |
### ARIA Nitelikler
| Özellik | Amaç | Örnek |
|-----------|------------|------------|
| `aria-label`| Görünür metin olmadığında erişilebilir ad | Yalnızca simge düğmesi:`aria-label="Search"`|
| `aria-describedby`| Öğeyi açıklamasına bağlar | Yardım metni içeren form alanı |
| `aria-expanded`| Bir bölümün genişletilip genişletilmediğini gösterir | Akordeon; açılır menü |
| `aria-hidden`| Öğeyi yardımcı teknolojiden gizler | Dekoratif simgeler |
| `aria-live`| Dinamik içerik değişikliklerini duyurdu | Canlı güncellemeler; bildirimler |
| `aria-disabled`| Öğenin devre dışı bırakıldığını gösterir | Grileştirilmiş düğmeler |
### ARIA'nın İlk Kuralı
> **Yerel HTML kullanabiliyorsanız ARIA'yı kullanmayın.** Bir `<button>`'ye zaten erişilebilir. `<div role="button">`, klavye yönetimini, odak yönetimini ve ekran okuyucu desteğini manuel olarak eklemenizi gerektirir. Önce anlamsal HTML'yi kullanın; ARIA yalnızca yerel öğeler işi yapamadığında.
---

## Klavye Gezintisi
| Anahtar | Beklenen Davranış |
|-----|---------------------|
| **Sekme** | Odağı bir sonraki etkileşimli öğeye taşı |
| **Üst Karakter + Sekme** | Odağı önceki etkileşimli öğeye taşı |
| **Giriş / Boşluk** | Odaklanılan öğeyi etkinleştirin (düğme, bağlantı) |
| **Ok tuşları** | Bileşenler arasında gezinme (menüler, sekmeler, radyo grupları) |
| **Kaçış** | Bir iletişim kutusunu, menüyü veya açılır pencereyi kapatma |
| **Ana Sayfa / Son** | Listedeki ilk/son öğeye atla |
### Yaygın Klavye Tuzakları
| Sorun | Düzelt |
|-----------|-----|
| Odak bir bileşene giriyor ancak çıkamıyor | Sekmenin odağı dışarı taşıdığından emin olun; kolu Kaçış |
| Modal odağı hapsetmiyor | Odaklanma modal içinde dönmelidir; kapatıldığında tetiğe dön |
| Özel bileşenler klavyeye yanıt vermiyor | Enter, Space, oklar için tuş vuruşu işleyicileri ekleyin |
---

## Renk ve Görsel Tasarım
| Kılavuz | Gereksinim |
|-----------|----------------|
| **Kontrast oranı** | normal metin için 4,5:1; Büyük metinler için 3:1 (18pt+ veya 14pt+kalın) |
| **Yalnızca renge güvenmeyin** | Rengin yanı sıra simgeler, metinler veya desenler kullanın |
| **Odak göstergeleri** | Her zaman görünür; yüksek kontrast; değiştirilmeden asla çıkarılmaz |
| **Metni yeniden boyutlandırma** | Düzen %200 yakınlaştırmada çalışmalıdır |
| **Duyarlı** | İçerik 320 piksel genişliğinde yeniden akıtılmalıdır (mobil) |
### Renk Körlüğüyle İlgili Dikkat Edilmesi Gerekenler
| Tür | Etkilenen Renkler | Tasarım İpucu |
|-----||----------|------------|
| **Döteranopi** | Kırmızı-yeşil (en yaygın) | Durumu iletmek için kırmızı/yeşil kullanmayın; simgeleri + rengi kullan |
| **Protanopi** | Kırmızı-yeşil | Yukarıdakinin aynısı |
| **Tritanopi** | Mavi-sarı | Tek farklılaştırıcı olarak mavi/sarı kullanmayın |
---

## Erişilebilirliği Test Etme
| Yöntem | Araç | Ne Yakalar |
|----------|----------|----------------|
| **Otomatik tarama** | balta, Deniz Feneri, DALGA | Alternatif metin eksik; kontrast sorunları; ARIA hataları |
| **Klavye testi** | Kılavuz: Fareyi çıkarın, yalnızca klavyeyi kullanın | Odaklanma sırası; klavye tuzakları; eksik işleyiciler |
| **Ekran okuyucu testi** | NVDA (ücretsiz), VoiceOver (macOS), JAWS | Eksik etiketler; zayıf yapı; habersiz değişiklikler |
| **Yakınlaştırma testi** | Tarayıcıyı %200, %400 yakınlaştırma | Düzen bozulması; kırpılmış metin; taşma sorunları |
| **Renk kontrastı** | WebAIM kontrast denetleyicisi, Stark eklentisi | Yetersiz kontrast oranları |
| **Kullanıcı testi** | Engelli kullanıcılarla test edin | Otomatik araçların gözden kaçırdığı gerçek dünya engelleri |
---

## Yasal Gereksinimler
| Hukuk | Bölge | Gereksinimler |
|-----|-----------|------------|
| **ADA** (Engelli Amerikalılar Yasası) | ABD | Kamuya açık konaklama yerlerinin web siteleri erişilebilir olmalıdır |
| **Bölüm 508** | ABD (federal) | Federal kurumların BİT'i erişilebilir olmalıdır |
| **EAA** (Avrupa Erişilebilirlik Yasası) | AB (2025+) | Ürün ve hizmetler erişilebilirlik gereksinimlerini karşılamalıdır |
| **EN 301 549** | AB | BİT erişilebilirliğine yönelik teknik standart |
| **ACA** (Erişilebilirlik Kanada Yasası) | Kanada | Kamu ve denetime tabi endüstriler |
| **Eşitlik Yasası 2010** | İngiltere | Hizmet sağlayıcılar makul ayarlamalar yapmalıdır |
---

## Mobil Erişilebilirlik
| Platformu | Yönergeler | Anahtar Araçlar |
|----------|---------------|-----------|
| **iOS** | Apple İnsan Arayüzü Yönergeleri (Erişilebilirlik bölümü) | Seslendirme; Dinamik Tip; Anahtar Kontrolü |
| **Android** | Android Erişilebilirlik yönergeleri | TalkBack; Erişimi Değiştir; Konuşmak İçin Seçin |
| Mobil Sorun | Çözüm |
|---------------|----------|
| **Hedeflere dokunun** | Minimum 44×44 punto (iOS) / 48×48 dp (Android) |
| **Ekran okuyucu desteği** | İçerik açıklamaları; erişilebilirlik etiketleri |
| **Hareket hassasiyeti** | `prefers-reduced-motion`'ye saygı gösterin; otomatik oynatılan animasyonlardan kaçının |
| **Dinamik metin boyutlandırma** | Destek sistemi yazı tipi boyutları; ölçeklenebilir metin birimleri kullanın |
---

## Özet
Erişilebilirlik, sonunda eklenen bir özellik değil, her kararı baştan itibaren bilgilendirmesi gereken bir tasarım ilkesidir. Anlamsal HTML kullanın. Klavye navigasyonunun çalıştığından emin olun. Yeterli renk kontrastını koruyun. Metin olmayan içerikler için metin alternatifleri sağlayın. Ekran okuyucularla ve engelli kullanıcılarla test edin. Sonuç, herkes için daha iyi çalışan bir yazılımdır; buna geçici sorunlar, durumsal sınırlamalar, eski cihazlar, yavaş bağlantılar ve gerçek dünya kullanımının kontrollü bir geliştirme ortamından farklı olduğu pek çok nokta da dahildir.