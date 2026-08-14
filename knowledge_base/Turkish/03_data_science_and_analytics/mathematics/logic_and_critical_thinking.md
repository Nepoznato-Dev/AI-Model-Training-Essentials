---
# Metadata
title: "Logic and Critical Thinking"
description: "Formal logic, logical fallacies, argument analysis, and critical thinking frameworks"
category: "Data Science and Analytics"
subcategory: "Mathematics"
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
    date: "2026-08-09"
    author: "AI Model Training Team"
    changes: "Split from mathematics_and_logic.md; expanded into standalone file"

# Review
created: "2026-08-09"
last_modified: "2026-08-09"
review_date: "2027-02-09"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-09"

# Classification
tags: [logic, critical-thinking, fallacies, arguments, reasoning, boolean-algebra]
difficulty_level: "beginner"
prerequisites: []
estimated_reading_time: "12 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# Mantık ve Eleştirel Düşünme
Mantık, geçerli akıl yürütmenin incelenmesidir; sağlam argümanların nasıl oluşturulacağı ve hatalı olanların nasıl belirleneceği. Eleştirel düşünme, varsayımları sorgulama, kanıtları değerlendirme ve dikkatli bir şekilde akıl yürütme gibi disiplinli bir alışkanlıktır. Bu beceriler yalnızca matematik ve bilgisayar bilimlerinde değil, aynı zamanda günlük karar vermede, bilimsel araştırmada ve bilgi açısından zengin bir dünyada gezinmede de gereklidir.
---

## Argüman Nedir?
Mantıkta, bir **argüman** bir sonucu desteklemeyi amaçlayan bir dizi ifadedir (öncüller).
| Bileşen | Rol | Örnek |
|-----------|------|-----------|
| **Tercih** | Kanıt olarak sunulan bir beyan | "Bütün insanlar ölümlüdür" |
| **Sonuç** | Tesisin desteklediği iddiası | "Sokrates ölümlüdür" |
| **Çıkarım** | Öncüllerden sonuca mantıksal adım | "Sokrates insandır, dolayısıyla..." |
### Geçerli ve Ses
| Dönem | Anlamı | Örnek |
|------|---------|--------|
| **Geçerli** | Öncüller doğruysa sonuç da doğru olmalıdır | Öncüller yanlış olsa bile yapı doğrudur |
| **Geçersiz** | Sonuç öncüllerden takip edilmez | Mantıksal yapı bozuldu |
| **Ses** | Geçerli VE tüm öncüller aslında doğrudur | Tartışmanın altın standardı |
| **Sağlıksız** | Geçersiz veya yanlış önermeler içeriyor | En hatalı argümanlar |
---

## Muhakeme Türleri
| Tür | Yön | Güç | Örnek |
|------|-----------|----------|-----------|
| **Tümdengelimli** | Genel → spesifik | Kesin (eğer geçerliyse) | "Bütün memelilerin akciğerleri vardır. Balina bir memelidir. Dolayısıyla balinanın da akciğerleri vardır." |
| **Endüktif** | Özel → genel | Olası | "Gördüğüm her kuğu beyazdır. Bu nedenle muhtemelen tüm kuğular beyazdır." |
| **Kaçırıcı** | Gözlem → en iyi açıklama | makul | "Çimler ıslak. Bunun en iyi açıklaması yağmur yağması." |
---

## Önerme Mantığı
Önerme mantığı basit önermelerle ve bunların nasıl birleştirildiğiyle ilgilenir:
### Mantıksal Bağlaçlar
| Bağlayıcı | Sembol | Anlamı | Doğruluk Durumu |
|-----------|-----------|-----------|----------------|
| **VE** | ∧ (p ∧ q) | Bağlaç | Yalnızca her ikisi de doğru olduğunda doğrudur |
| **VEYA** | ∨ (p ∨ q) | Ayrışma | En az biri doğru olduğunda doğrudur |
| **DEĞİL** | ¬ (¬p) | Olumsuzluk | Karşıt doğruluk değeri |
| **EĞER...SONRA** | → (p → q) | Çıkarım | Yalnızca p doğru ve q yanlış olduğunda yanlış |
| **IFF** | ↔ (p ↔q) | iki koşullu | Her ikisi de aynı doğruluk değerine sahip olduğunda doğru |
### Uygulama için Doğruluk Tablosu (p → q)
| p | q | p → q |
|---|---|-------|
| T | T | T |
| T | F | F |
| F | T | T |
| F | F | T |
Not: Yanlış bir öncül, imanın anlamsız bir şekilde doğru olmasını sağlar. "Ay peynirse, ben de Papayım" sözü mantıksal olarak doğrudur.
---

## Boole Cebiri
Boole cebiri doğru/yanlış değerlerinin matematiğidir ve dijital devre tasarımı ve programlamanın temelidir:
| Hukuk | İfade | Anlamı |
|-----|-----------|-----------|
| **Değişmeli** | Bir ∧ B = B ∧ Bir | Sıra önemli değil |
| **İlişkili** | (Bir ∧ B) ∧ C = Bir ∧ (B ∧ C) | Gruplama önemli değil |
| **Dağıtımsal** | Bir ∧ (B ∨ C) = (A ∧ B) ∨ (A ∧ C) | VE VEYA |
| **De Morgan'ın** | ¬(A ∧ B) = ¬A ∨ ¬B | Olumsuzluk VE'yi VEYA'ya çevirir |
| **De Morgan'ın** | ¬(A ∨ B) = ¬A ∧ ¬B | Olumsuzluk VEYA'yı VE'ye çevirir |
| **Çifte Olumsuzluk** | ¬(¬A) = A | İki olumsuzluk iptal |
| **Kimlik** | Bir ∧ T = Bir; Bir ∨ F = Bir | Kimlik öğeleri |
| **Tamamlayıcı** | bir ∧ ¬A = F; bir ∨ ¬A = T | Çelişki ve totoloji |
---

## Yaygın Mantıksal Yanılgılar
Yanlışlıkları tanımak eleştirel düşünme için önemlidir:
### Biçimsel Yanılgılar (Yapısal Hatalar)
| Yanılgı | Yapı | Örnek |
|-----------|-----------|-----------|
| **Sonucun Onaylanması** | Eğer P ise Q. Q. Bu nedenle P. | "Yağmur yağarsa yer ıslaktır. Yer ıslaktır. Bu nedenle yağmur yağdı." (Bir yağmurlama sistemi olabilir.) |
| **Öncekileri İnkar Etmek** | P ise Q. P değil. Bu nedenle Q değil. | "Yağmur yağarsa zemin ıslaktır. Yağmur yağmamıştır. Dolayısıyla zemin ıslak değildir." |
### Resmi Olmayan Yanılgılar (İçerik Hataları)
| Yanılgı | Açıklama | Örnek |
|-----------|------------|------------|
| **Ad Hominem** | Tartışmaya değil kişiye saldırmak | "Onun ekonomik planına güvenemezsiniz; o bir ekonomist bile değil." |
| **Saman Adam** | Saldırmayı kolaylaştırmak için bir argümanı yanlış sunmak | "Askeri harcamaları azaltmak mı istiyorsunuz? Yani ülkeyi savunmasız bırakmak istiyorsunuz!" |
| **Yetkiye İtiraz** | İlgili alanda uzman olmayan bir otoriteye atıfta bulunulması | "Bu ünlü bu diyetin işe yaradığını, dolayısıyla etkili olması gerektiğini söylüyor." |
| **Yanlış İkilem** | Daha fazlası mevcutken yalnızca iki seçeneğin sunulması | "Ya bizimlesin ya da bize karşısın." |
| **Kaygan Eğim** | Bir olayın kaçınılmaz olarak aşırı bir sonuca yol açacağını savunmak | "Eğer buna izin verirsek, bir sonraki adım tam bir kaos olacaktır." |
| **Döngüsel Akıl Yürütme** | Sonuç tesis içinde varsayılmaktadır | "Kitap doğrudur çünkü doğru olduğunu söyler." |
| **Aceleci Genelleme** | Yetersiz kanıttan geniş bir sonuca varmak | "O şehirden iki kaba insanla tanıştım. Oradaki herkes kaba olmalı." |
| **Post Hoc Ergo Propter Hoc** | Zamansal diziden nedensellik varsayımı | "Bu takviyeyi aldım ve kendimi daha iyi hissettim, bu yüzden işe yaramalı." |
| **Kırmızı Ringa balığı** | Dikkat dağıtmak için alakasız bir konuya giriş | "Eğitim politikamı soruyorsunuz ama asıl önemli olan ekonomi." |
| **Çoğunluk** | Bir şey doğrudur çünkü birçok insan buna inanır | "Herkes bu ürünü satın alıyor, bu yüzden en iyisi bu olmalı." |
---

## Argümanların Değerlendirilmesi: Bir Kontrol Listesi
| Adım | Soru |
|----------|----------|
| 1. **Sonucu tanımlayın** | Kanıtlamaya çalıştığı argüman nedir? |
| 2. **Tesisleri tanımlayın** | Hangi kanıtlar sunuluyor? |
| 3. **Geçerliliği kontrol edin** | Sonuç öncüllerden mi çıkıyor? |
| 4. **Sağlamlığı kontrol edin** | Öncüller gerçekten doğru mu? |
| 5. **Yanlış anlamaları arayın** | Yapısal veya içeriksel hatalar var mı? |
| 6. **Karşı iddiaları dikkate alın** | Ne gibi itirazlar olabilir? |
| 7. **Kanıt kalitesini değerlendirin** | Kanıtlar güvenilir, yeterli ve konuyla ilgili mi? |
---

## Bu Neden Önemli?
Mantık ve eleştirel düşünme matematiğin, bilgisayar biliminin, hukukun ve bilimsel araştırmanın temelidir. Yanlış bilgi, reklam ve ikna edici söylemlerle dolu bir dünyada, argümanları titizlikle değerlendirme yeteneği sadece akademik bir beceri değil, aynı zamanda bir hayatta kalma becerisidir. İster kodda hata ayıklıyor olun, ister algoritma tasarlıyor olun, ister hayati kararlar veriyor olun, açık akıl yürütme, iyi kararları kötü olanlardan ayırır.