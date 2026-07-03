# Prompt Mühendisliği

Prompt mühendisliği, bir dil modelinden mümkün olan en iyi çıktıyı almak için girdi prompt'larını tasarlama, iyileştirme ve optimize etme uygulamasıdır. Hem bir sanat hem de bir bilimdir ve ince ayar yapmadan LLM davranışını kontrol etmenin birincil arayüzüdür.

---

## Temel İlkeler

### Açıklık ve Belirlilik
Açık bir prompt belirsizliğe yer bırakmaz. Biçim, uzunluk ve bakış açısı dâhil olmak üzere ne istediğinizi tam olarak belirtin.

**Belirsiz:**
> "Bana Python'dan bahset."

**Belirli:**
> "Python'ın Global Interpreter Lock'unu (GIL) açıkla. Çok iş parçacıklılığı üzerindeki etkisini anlat, bir geçici çözüm ver ve yanıtını 200 kelimenin altında tut."

### Bağlam Sağlayın
Modeller; rolü, hedef kitleyi ve amacı bildiklerinde daha iyi performans gösterir.

**Bağlam olmadan:**
> "Bir listeyi sıralamak için fonksiyon yaz."

**Bağlamla:**
> "Kıdemli bir Python geliştiricisisin. Verilen bir anahtara göre sözlüklerden oluşan bir listeyi sıralayan bir fonksiyon yaz. Type hint kullan ve uç durumları ele al. Hedef kitle junior geliştiriciler."

### Olumlu Talimatlar Kullanın
Modele ne yapmaması gerektiğini değil, ne yapması gerektiğini söyleyin. "Jargon kullanma" ifadesi, "10 yaşındaki bir çocuğun anlayabileceği basit bir dil kullan" ifadesinden daha zayıftır.

---

## Prompt Yapıları

### System / User / Assistant Rolleri
Çoğu LLM API'si çok turlu bir yapıyı destekler:

- **System message**: Modelin davranışını, kişiliğini ve kısıtlarını belirler (tüm oturum boyunca sürer).
- **User message**: Mevcut soru veya talimat.
- **Assistant message**: Modelin önceki yanıtları (süreklilik için kullanılır).

**Örnek (OpenAI API tarzı):**
System: Yardımcı bir kodlama asistanısın. Kısa kod örnekleri ve öz açıklamalarla yanıt verirsin. Asla güvensiz kod sağlama.
User: Bir URL'den dosya indirmek için Python fonksiyonu yaz.

### Few-Shot Prompting
Modelden görevi gerçekleştirmesini istemeden önce istenen girdi-çıktı biçimine ait 2–3 örnek sağlayın. Bu, örüntüyü öğretir.

**Örnek:**
User: Bu cümleleri edilgen çatıya dönüştür:
Input: The cat chased the mouse.
Output: The mouse was chased by the cat.
Input: The chef cooked the meal.
Output: The meal was cooked by the chef.
Input: The storm destroyed the house.
Output: (model tamamlar)

### Chain-of-Thought (CoT)
Modeli akıl yürütmesini adım adım göstermeye teşvik edin. Bu, aritmetik, mantık ve çok adımlı görevlerde doğruluğu artırır.

**CoT olmadan:**
> "24 × 37 kaçtır?"

**CoT ile:**
> "24 × 37'yi hesapla. Akıl yürütmeni adım adım göster."

Model ara adımlar üretir ve bu da aritmetik hataları azaltır.

### Yapılandırılmış Çıktılar
Ayrıştırmayı güvenilir hâle getirmek için JSON, YAML veya markdown tabloları gibi belirli bir biçim isteyin.
User: Mikroservislerin üç artısını ve üç eksisini listele. Yalnızca "pros" ve "cons" anahtarlarına sahip, her biri string dizisi olan geçerli bir JSON nesnesi döndür.

---

## İleri Teknikler

### Self-Consistency
Aynı prompt için birden çok yanıt üretin (temperature > 0 ile) ve nihai yanıt üzerinde çoğunluk oyu alın. Bu, özellikle akıl yürütme görevlerinde etkilidir.

### Tree-of-Thoughts
Birden çok akıl yürütme yolunu paralel olarak keşfedin, her birini değerlendirin ve en iyisini seçin. Bu araştırma düzeyinde bir tekniktir ancak modelden "alternatif çözümleri keşfetmesini" isteyerek yaklaşık biçimde uygulanabilir.

### ReAct (Reasoning + Acting)
Modelin akıl yürütmeyi araç çağrılarıyla iç içe yürütmesine izin verin. Düşünebilir, ardından eyleme geçebilir (ör. web'de arama yapma, kod çalıştırma), sonra sonuca göre yeniden düşünebilir.

**Prompt yapısı:**
Bir hesap makinesine ve arama motoruna erişimin var. Her adım için şunları çıktıyla ver:
Thought: (akıl yürütmen)
Action: (araç adı, girdi)
Observation: (araç çıktısı)
... nihai yanıta ulaşana kadar devam et.

### Persona Atama
Yanıtı çerçevelemek için belirli bir persona atayın.

**Örnekler:**
- "Bellek yönetimini yeni mezun birine açıklayan bir Linux kernel geliştiricisisin."
- "Bir danışana genel tavsiyeler veren samimi bir beslenme uzmanısın."
- "Yeni bir cihazı inceleyen alaycı bir teknoloji eleştirmenisin."

---

## Parametre Ayarı

- **Temperature** (0.0 – 1.0+): Rastlantısallığı kontrol eder. Daha düşük = daha deterministik, daha yüksek = daha yaratıcı. Olgusal yanıtlar için 0.0–0.3; yaratıcı yazım için 0.7–1.0 kullanın.
- **Top-p** (nucleus sampling): Olasılık kütlesini belirli bir kümülatif eşikte keser. 0.9, modelin olası token'ların en üst %90'ından örneklediği anlamına gelir. Genellikle temperature veya top-p'den birini ayarlayın, ikisini birden değil.
- **Max tokens**: En fazla çıktı uzunluğunu belirler. Bağlam penceresinde yanıt için yer ayırmayı unutmayın.
- **Frequency penalty**: Aynı token'ların tekrarını azaltır.
- **Presence penalty**: Modeli yeni konular tanıtmaya teşvik eder.

---

## Yaygın Tuzaklar ve Çözümler

| Sorun | Olası neden | Çözüm |
|-------|-------------|-------|
| Model prompt'un bazı bölümlerini yok sayıyor | Prompt çok uzun veya aşırı yüklü | Kısaltın; en önemli talimatı sona koyun |
| Çıktı çok uzun | Uzunluk kısıtı yok | "3 cümleyle sınırla" ekleyin veya max_tokens ayarlayın |
| Çıktı çok kısa | Aşırı kısıtlayıcı | "Ayrıntılı açıkla" ekleyin veya temperature'ı düşürün |
| Olgusal hallucination | Yetersiz bağlam veya belirsiz soru | "Emin değilsen 'bilmiyorum' de" ekleyin ve RAG bağlamı sağlayın |
| Tutarsız biçimlendirme | Açık biçim talimatı yok | JSON, markdown tablo veya madde listesi isteyin |
| Model yanlış dilde yanıtlıyor | Dil talimatı yok | Açıkça "İngilizce yanıt ver" (veya hedef dilinizi) belirtin |

---

## Yaygın Görevler İçin Prompt Şablonları

### Özetleme
Aşağıdaki metni 3 maddeyle özetle. Ana argümanlara odaklan ve ayrıntılardan kaçın.

Metin: [metin ekle]


### Kod Üretimi
[Şu işi yapan] bir [dil] fonksiyonu yaz.
Gereksinimler:

Type hint kullan.

Docstring ekle.

Uç durumları ele al: [liste].

Belirtilmedikçe harici kütüphane kullanma.


### Açıklama
[kavramı] bir [uzman olmayan kişiye / üniversite öğrencisine / çocuğa] açıkla. Uygun olduğunda bir benzetme kullan.

### Beyin Fırtınası
[konu] için 10 fikir üret. Her fikir için tek cümlelik bir açıklama ve bir olası zorluk ver.

metin

### Sınıflandırma
Aşağıdaki müşteri geri bildirimini [olumlu, nötr, olumsuz] olarak sınıflandır.
Bir güven skoru (0-100) ve kısa bir gerekçe sağla.

Geri bildirim: [metin ekle]

### Üsluba Göre Çeviri
Aşağıdaki İngilizce metni İspanyolcaya çevir. Sosyal medya gönderisine uygun samimi bir ton kullan.
Metin: [metin ekle]

---

## Prompt'ların Değerlendirilmesi

Prompt'ları kod gibi ele alın: sürümleyin, test edin ve yineleyin.

- Ayrılmış bir sorgu kümesi üzerinde farklı prompt varyantlarını **A/B testine** tabi tutun.
- Başarıyı insan değerlendirmesi veya otomatik metriklerle (ör. exact match, BLEU, özel puanlama) **ölçün**.
- Prompt'u, sürümü ve gözlenen performansı içeren bir **prompt registry** (basit bir metin dosyası veya elektronik tablo) tutun.

---
