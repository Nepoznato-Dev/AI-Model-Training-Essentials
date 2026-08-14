---
# Metadata
title: "Prompt Engineering"
description: "Prompt techniques and strategies"
category: "AI and Machine Learning"
subcategory: "Foundations"
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
    changes: "Moved to foundations/ subfolder; added subcategory field"
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
tags: [prompt, engineering, ai-and-machine-learning]
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

# Hızlı Mühendislik
İstem mühendisliği, bir dil modelinden mümkün olan en iyi çıktıyı elde etmek için girdi istemlerini tasarlama, iyileştirme ve optimize etme uygulamasıdır. Hem sanat hem de bilimdir ve LLM davranışını ince ayar yapmadan kontrol etmek için birincil arayüzdür.
---

## Temel İlkeler
### Açıklık ve Özgünlük
Açık bir yönlendirme belirsizliğe yer bırakmaz. Biçim, uzunluk ve perspektif dahil olmak üzere tam olarak ne istediğinizi belirtin.
**Belirsiz:**
> "Bana Python'dan bahset."
**Özel:**
> "Python'un Küresel Yorumlayıcı Kilidini (GIL) açıklayın. Çoklu iş parçacığı üzerindeki etkisini açıklayın, bir geçici çözüm verin ve yanıtınızı 200 kelimenin altında tutun."
### Bağlam Sağlayın
Modeller rolü, hedef kitleyi ve hedefi bildiklerinde daha iyi performans gösterirler.
**Bağlam olmadan:**
> "Listeyi sıralamak için bir işlev yazın."
**Bağlamla birlikte:**
> "Kıdemli bir Python geliştiricisisiniz. Sözlüklerin listesini belirli bir anahtara göre sıralamak için bir işlev yazın. Tür ipuçlarını kullanın ve uç durumları ele alın. Hedef kitlesi kıdemsiz geliştiricilerdir."
### Olumlu Talimatları Kullanın
Modele ne yapması gerektiğini değil ne yapması gerektiğini söyleyin. "Jargon eklemeyin", "10 yaşındaki bir çocuğun anlayabileceği basit bir dil kullanın"dan daha zayıftır.
---

## Bilgi İstemi Yapıları
### Sistem / Kullanıcı / Asistan Rolleri
Çoğu LLM API'si çok dönüşlü bir yapıyı destekler:
- **Sistem mesajı**: Modelin davranışını, kişiliğini ve kısıtlamalarını ayarlar (tüm oturum boyunca devam eder).
- **Kullanıcı mesajı**: Geçerli sorgu veya talimat.
- **Asistan mesajı**: Modelin önceki yanıtları (süreklilik için kullanılır).
**Örnek (OpenAI API stili):**
Sistem: Yardımcı bir kodlama asistanısınız. Kısa kod örnekleri ve kısa açıklamalarla yanıt verirsiniz. Asla güvenli olmayan kod vermeyin.
Kullanıcı: Bir URL'den dosya indirmek için bir Python işlevi yazın.
### Birkaç Atışlı Uyarı
Modelden görevi gerçekleştirmesini istemeden önce istenen giriş-çıkış formatının 2-3 örneğini sağlayın. Bu modeli öğretir.
**Örnek:**
Kullanıcı: Bu cümleleri pasif sese dönüştürün:
Giriş: Kedi fareyi kovaladı.
Sonuç: Fare kedi tarafından kovalandı.
Girdi: Şef yemeği pişirdi.
Çıktı: Yemek şef tarafından pişirildi.
Giriş: Fırtına evi yok etti.
Çıktı: (model tamamlanır)
### Düşünce Zinciri (CoT)
Modeli adım adım mantığını göstermeye teşvik edin. Bu, aritmetik, mantık ve çok adımlı görevlerde doğruluğu artırır.
**CoT'siz:**
> "24 × 37 nedir?"
**CoT ile:**
> "24 × 37'yi hesaplayın. Gerekçenizi adım adım gösterin."
Model, aritmetik hataları azaltan ara adımlar üretecek.
### Yapılandırılmış Çıkışlar
Ayrıştırmayı güvenilir hale getirmek için JSON, YAML veya işaretleme tabloları gibi belirli bir format isteyin.
Kullanıcı: Mikro hizmetlerin üç artısını ve üç eksisini listeleyin. Yalnızca "artıları" ve "eksileri" tuşlarına sahip, her biri bir dizi dizeden oluşan geçerli bir JSON nesnesi döndürün.
---

## İleri Teknikler
### Öz Tutarlılık
Aynı istem için birden fazla yanıt oluşturun (sıcaklık > 0 ile) ve son yanıt için çoğunluk oyu alın. Bu özellikle muhakeme görevleri için etkilidir.
### Düşünce Ağacı
Birden fazla akıl yürütme yolunu paralel olarak keşfedin, her birini değerlendirin ve en iyisini seçin. Bu araştırma düzeyinde bir tekniktir ancak modelden "alternatif çözümler keşfetmesi" istenerek yaklaşık bir değer elde edilebilir.
### ReAct (Akıl Yürütme + Oyunculuk)
Modelin akıl yürütmeyi araç çağrılarıyla bir araya getirmesine izin verin. Düşünebilir, sonra harekete geçebilir (örneğin, web'de arama yapabilir, kod çalıştırabilir), sonra sonuca göre yeniden düşünebilir.
**Bilgi istemi yapısı:**
Bir hesap makinesine ve bir arama motoruna erişiminiz var. Her adım için çıktı:
Düşünce: (mantığınız)
Eylem: (araç adı, giriş)
Gözlem: (araç çıkışı)
... son cevabı alana kadar devam edin.
### Kişilik Ataması
Yanıtı çerçevelemek için belirli bir kişiyi atayın.
**Örnekler:**
- "Yeni mezun birine bellek yönetimini açıklayan bir Linux çekirdek geliştiricisisiniz."
- "Müşteriye genel tavsiyeler veren dost canlısı bir beslenme uzmanısınız."
- "Yeni bir cihazı inceleyen alaycı bir teknoloji eleştirmenisiniz."
---

## Parametre Ayarlama
- **Sıcaklık** (0,0 – 1,0+): Rastgeleliği kontrol eder. Düşük = daha belirleyici, yüksek = daha yaratıcı. Gerçek cevaplar için 0,0–0,3 kullanın; Yaratıcı yazma için 0,7–1,0.
- **Top-p** (çekirdek örneklemesi): Olasılık kütlesini belirli bir kümülatif eşikte keser. 0,9, modelin olası tokenların ilk %90'ından örnek aldığı anlamına gelir. Genellikle sıcaklığı veya üst-p'yi ayarlayın, ikisini birden değil.
- **Maksimum belirteç**: Maksimum çıktı uzunluğunu ayarlar. Bağlam penceresinde yanıt için yer ayırmayı unutmayın.
- **Frekans cezası**: Aynı jetonların tekrarını azaltır.
- **Mevcudiyet cezası**: Modeli yeni konuları tanıtmaya teşvik eder.
---

## Yaygın Tuzaklar ve Çözümler
| Sorun | Olası neden | Düzelt |
|-----------|----------------|-----|
| Model, istemin bazı kısımlarını yok sayar | İstem çok uzun veya aşırı yüklenmiş | Kısaltın; en önemli talimatı en sona koy |
| Çıktı çok ayrıntılı | Uzunluk sınırlaması yok | "3 cümleyle sınırla" seçeneğini ekleyin veya max_tokens |
| Çıktı çok kısa | Aşırı kısıtlayıcı | "Ayrıntılı olarak açıklayın" seçeneğini ekleyin veya sıcaklığı düşürün |
| Gerçek halüsinasyonlar | Yetersiz bağlam veya belirsiz soru | "Emin değilseniz 'Bilmiyorum' deyin" ifadesini ekleyin ve bir RAG bağlamı sağlayın |
| Tutarsız biçimlendirme | Açık format talimatı yok | JSON, işaretleme tablosu veya madde işareti listesi isteyin |
| Model yanıtları yanlış dilde | Dil eğitimi yok | Açıkça "İngilizce yanıt verin" seçeneğini (veya hedef dilinizi) belirtin |
---

## Ortak Görevler için Bilgi İstemi Şablonları
### Özetleme
Aşağıdaki metni 3 madde işaretiyle özetleyin. Ana argümanlara odaklanın ve ayrıntılardan kaçının.
Metin: [metin girin]

### Kod Oluşturma
[X yapan] bir [language] fonksiyonu yazın.
Gereksinimler:
Yazım ipuçlarını kullanın.
Bir doktrin ekleyin.
Uç durumları ele alın: [liste].
Belirtilmediği sürece harici kütüphaneleri kullanmayın.

### Açıklama
[Kavramı] bir [uzman olmayan kişiye/üniversite öğrencisine/çocuğa] açıklayın. Uygun olduğu yerde bir benzetme kullanın.
### Beyin fırtınası
[Konu] için 10 fikir üretin. Her fikir için tek cümlelik bir açıklama ve olası bir zorluk belirtin.
metin
### Sınıflandırma
Aşağıdaki müşteri geri bildirimlerini [olumlu, nötr, olumsuz] olarak sınıflandırın.
Bir güven puanı (0-100) ve kısa bir neden belirtin.
Geri bildirim: [metin ekleyin]
### Stilli Çeviri
Aşağıdaki İngilizce metni İspanyolcaya çevirin. Sosyal medya gönderisine uygun resmi olmayan bir ton kullanın.
Metin: [metin girin]
---

## İstemlerin Değerlendirilmesi
İstemleri kod olarak değerlendirin: sürümlerini oluşturun, test edin ve yineleyin.
- **A/B testi** uzun süreli sorgular üzerinde farklı bilgi istemi çeşitleri.
- **İnsan değerlendirmesi veya otomatik ölçümler (ör. tam eşleşme, BLEU, özel puanlama) aracılığıyla **başarıyı ölçün**.
- **İstem, sürüm ve gözlemlenen performansı içeren bir istem kaydı** (basit bir metin dosyası veya e-tablo) tutun.
---