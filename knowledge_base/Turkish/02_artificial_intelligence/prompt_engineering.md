# İstem Mühendisliği

İstem mühendisliği (prompt engineering), bir dil modelinden mümkün olan en iyi çıktıyı almak için giriş istemlerini tasarlama, iyileştirme ve optimize etme pratiğidir. Hem bir sanat hem de bir bilimdir ve fine-tuning yapmadan LLM davranışını kontrol etmenin başlıca arayüzüdür.

---

## Temel İlkeler

### Açıklık ve Özgüllük
Açık bir istem, belirsizliğe yer bırakmaz. Formatı, uzunluğu ve bakış açısını da dâhil ederek tam olarak ne istediğinizi belirtin.

**Belirsiz:**
> "Bana Python hakkında bilgi ver."

**Spesifik:**
> "Python'daki Global Interpreter Lock'u (GIL) açıklayın. Multithreading üzerindeki etkisini anlatın, bir geçici çözüm verin ve yanıtınızı 200 kelimenin altında tutun."

### Bağlam Sağlayın
Modeller; rolü, hedef kitleyi ve amacı bildiklerinde daha iyi performans gösterir.

**Bağlam olmadan:**
> "Bir listeyi sıralayan bir fonksiyon yaz."

**Bağlamla birlikte:**
> "Kıdemli bir Python geliştiricisisiniz. Verilen bir anahtara göre sözlüklerden oluşan bir listeyi sıralayan bir fonksiyon yazın. Type hint kullanın ve edge case'leri ele alın. Hedef kitle junior geliştiriciler."

### Pozitif Talimatlar Kullanın
Modele ne yapmaması gerektiğini değil, ne yapması gerektiğini söyleyin. "Jargon kullanma" ifadesi, "10 yaşındaki bir çocuğun anlayabileceği basit bir dil kullan" demekten daha zayıftır.

---

## İstem Yapıları

### System / User / Assistant Rolleri
Çoğu LLM API'si çok turlu bir yapı destekler:

- **System message**: Modelin davranışını, personasını ve kısıtlarını belirler (tüm oturum boyunca kalıcıdır).
- **User message**: Mevcut sorgu veya talimattır.
- **Assistant message**: Modelin önceki yanıtlarıdır (süreklilik için kullanılır).

**Örnek (OpenAI API tarzı):**
System: Yardımsever bir kodlama asistanısınız. Kısa kod örnekleri ve kısa açıklamalarla yanıt verirsiniz. Asla güvensiz kod sağlamazsınız.
User: Bir URL'den dosya indiren bir Python fonksiyonu yaz.

### Few-Shot Prompting
Modelden görevi yapmasını istemeden önce istenen giriş-çıkış biçiminden 2–3 örnek verin. Bu, örüntüyü öğretir.

**Örnek:**
User: Bu cümleleri edilgen çatıya dönüştür:
Input: The cat chased the mouse.
Output: The mouse was chased by the cat.
Input: The chef cooked the meal.
Output: The meal was cooked by the chef.
Input: The storm destroyed the house.
Output: (model completes)

### Chain-of-Thought (CoT)
Modeli, akıl yürütmesini adım adım göstermeye teşvik edin. Bu, aritmetik, mantık ve çok adımlı görevlerde doğruluğu artırır.

**CoT olmadan:**
> "24 × 37 kaçtır?"

**CoT ile:**
> "24 × 37 işlemini hesapla. Akıl yürütmeni adım adım göster."

Model ara adımlar üreterek aritmetik hatalarını azaltır.

### Yapılandırılmış Çıktılar
Ayrıştırmayı güvenilir hâle getirmek için JSON, YAML veya markdown tabloları gibi belirli bir format isteyin.
User: Mikroservislerin üç avantajını ve üç dezavantajını listele. Yalnızca "pros" ve "cons" anahtarlarına sahip, her biri string dizisi olan geçerli bir JSON nesnesi döndür.

---

## İleri Teknikler

### Self-Consistency
Aynı istem için birden fazla yanıt üretin (temperature > 0 ile) ve nihai yanıtta çoğunluk oylaması yapın. Bu yaklaşım özellikle akıl yürütme görevlerinde etkilidir.

### Tree-of-Thoughts
Birden fazla akıl yürütme yolunu paralel olarak keşfedin, her birini değerlendirin ve en iyisini seçin. Bu araştırma düzeyinde bir tekniktir ancak modele "alternatif çözümleri keşfet" diyerek yaklaşık olarak uygulanabilir.

### ReAct (Reasoning + Acting)
Modelin akıl yürütmeyi araç çağrılarıyla iç içe geçirmesine izin verin. Düşünebilir, sonra eyleme geçebilir (ör. web'de arama yapmak, kod çalıştırmak), ardından sonuca göre yeniden düşünebilir.

**İstem yapısı:**
Bir hesap makinesine ve bir arama motoruna erişiminiz var. Her adım için şu çıktıyı verin:
Thought: (akıl yürütmeniz)
Action: (araç adı, girdi)
Observation: (araç çıktısı)
... nihai yanıta ulaşana kadar devam edin.

### Persona Ataması
Yanıtı çerçevelemek için belirli bir persona atayın.

**Örnekler:**
- "Bellek yönetimini yeni mezun birine açıklayan bir Linux kernel geliştiricisisiniz."
- "Bir danışana genel tavsiye veren dost canlısı bir nutritionist'siniz."
- "Yeni bir gadget'ı değerlendiren alaycı bir teknoloji eleştirmenisiniz."

---

## Parametre Ayarlama

- **Temperature** (0.0 – 1.0+): Rastgeleliği kontrol eder. Düşük = daha deterministik, yüksek = daha yaratıcı. Olgusal yanıtlar için 0.0–0.3; yaratıcı yazı için 0.7–1.0 kullanın.
- **Top-p** (nucleus sampling): Olasılık kütlesini belirli bir kümülatif eşikte keser. 0.9, modelin en olası token'ların üst %90'ından örnekleme yaptığı anlamına gelir. Genellikle temperature veya top-p ayarlanır, ikisi birden değil.
- **Max tokens**: Çıktının en fazla uzunluğunu belirler. Context window içinde yanıt için yer ayırmayı unutmayın.
- **Frequency penalty**: Aynı token'ların tekrarını azaltır.
- **Presence penalty**: Modeli yeni konular açmaya teşvik eder.

---

## Yaygın Sorunlar ve Çözümleri

| Problem | Olası neden | Çözüm |
|---------|-------------|-------|
| Model istemin bazı bölümlerini yok sayıyor | İstem çok uzun ya da aşırı yüklü | Kısaltın; en önemli talimatı sona koyun |
| Çıktı çok uzun | Uzunluk kısıtı yok | "3 cümleyle sınırla" ekleyin veya max_tokens ayarlayın |
| Çıktı çok kısa | Aşırı kısıtlayıcı istem | "Ayrıntılı açıkla" ekleyin veya temperature'ı düşürün |
| Olgusal halüsinasyonlar | Yetersiz bağlam veya belirsiz soru | "Emin değilsen 'I don't know' de" ekleyin ve RAG bağlamı sağlayın |
| Biçim tutarsız | Açık format talimatı yok | JSON, markdown table veya bullet list isteyin |
| Model yanlış dilde yanıtlıyor | Dil talimatı yok | Açıkça "Respond in English" (veya hedef dilinizi) belirtin |

---

## Yaygın Görevler için İstem Şablonları

### Summarisation
Aşağıdaki metni 3 madde hâlinde özetle. Ana argümanlara odaklan ve ayrıntılardan kaçın.

Text: [insert text]


### Code Generation
[Dil] dilinde [X işlemini yapan] bir fonksiyon yaz.
Requirements:

Use type hints.

Include a docstring.

Handle edge cases: [list].

Do not use external libraries unless specified.


### Explanation
[Konsept]'i [uzman olmayan biri / üniversite öğrencisi / çocuk] için açıkla. Uygun olduğunda bir benzetme kullan.

### Brainstorming
[Topic] için 10 fikir üret. Her fikir için tek cümlelik bir açıklama ve olası bir zorluk ver.

text

### Classification
Aşağıdaki müşteri geri bildirimini [positive, neutral, negative] olarak sınıflandır.
0-100 arasında bir confidence score ve kısa bir gerekçe ver.

Feedback: [insert text]

### Translation with Style
Aşağıdaki English metni Spanish diline çevir. Sosyal medya gönderisine uygun samimi bir ton kullan.
Text: [insert text]

---

## İstemlerin Değerlendirilmesi

İstemlere kod gibi davranın: sürümleyin, test edin ve yineleyin.

- Elde tutulmuş bir sorgu kümesi üzerinde farklı istem varyantlarını **A/B test** ile karşılaştırın.
- Başarıyı insan değerlendirmesi veya otomatik metriklerle ölçün (ör. exact match, BLEU, özel puanlama).
- İstemi, sürümünü ve gözlenen performansı içeren bir **prompt registry** (basit bir metin dosyası veya spreadsheet) tutun.

---
