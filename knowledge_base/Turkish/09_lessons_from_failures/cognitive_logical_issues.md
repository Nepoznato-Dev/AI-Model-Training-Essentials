---
# Metadata
title: "Cognitive Biases and Logical Fallacies"
description: "Reasoning errors and cognitive biases"
category: "Lessons from Failures"
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
reviewed_by: "Lessons from Failures Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [cognitive, logical, issues, lessons-from-failures]
difficulty_level: "advanced"
prerequisites: []
estimated_reading_time: "27 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Bilişsel Önyargılar ve Mantıksal Yanılgılar
Bu belge, hem insanın karar verme sürecini hem de yapay zeka sistem çıktılarını etkileyen bilişsel önyargıları, mantıksal yanılgıları ve akıl yürütme hatalarını bir araya getiriyor.
---

## Bilişsel Önyargılar
Bilişsel önyargılar, yargılama ve karar vermede rasyonellikten sistematik sapma kalıplarıdır. Yazılım geliştirme ve yapay zeka sistemlerinde bunlar, zayıf tasarım kararlarına, kusurlu gereksinimlere ve önyargılı model davranışına yol açabilir.
### Onaylama Önyargısı
**Nedir:** Önceden var olan inançları doğrulayacak şekilde bilgiyi arama, yorumlama ve hatırlama eğilimi.
**Geliştirmede Kötü Örnek:**```python
# Developer believes their algorithm is O(n log n)
def analyze_complexity(code):
    # Only looks for evidence supporting O(n log n)
    sees_divide_and_conquer = True
    sees_recursion = True
    
    # Ignores contradictory evidence
    nested_loop_present = True  # Actually makes it O(n²)
    redundant_computation = True  # Adds extra factor
    
    return "O(n log n)"  # Wrong conclusion
```

**Kod İncelemelerinde:**```markdown
Developer A (senior): "This looks good, nice work!"
Developer B (junior): "This has several potential issues..."

Team accepts Developer A's review without scrutiny but questions Developer B's feedback excessively.
```

**Azaltma:**
- Aktif olarak onaylamayan kanıtları arayın
- Kör kod incelemelerini kullanın
- Farklı fikirleri teşvik edin
- Varsayımları açıkça belgeleyin
### Önyargıyı Sabitlemek
**Nedir:** Karşılaşılan ilk bilgiye çok fazla güvenmek.
**Kötü Örnek:**```markdown
Project Manager: "This feature should take about 2 days."
Developer: (Anchored to 2 days, even though realistic estimate is 5 days)
"Okay, I'll try to finish in 2 days."

Result: Rushed work, technical debt, missed deadlines anyway.
```

**Azaltma:**
- Birden fazla bağımsız tahmin alın
- Tahmin için planlama pokerini kullanın
- Nokta tahminleri yerine aralıkları göz önünde bulundurun
- Referans geçmiş verileri
### Batık Maliyet Yanılgısı
**Nedir:** Daha önce yatırılan kaynaklar (zaman, para, çaba) nedeniyle, vazgeçildiğinde bile bir çabaya devam etmek daha iyi olacaktır.
**Kötü Örnek:**```markdown
"We've already spent 6 months building this custom framework. 
We can't switch to the industry standard now, even though 
it would save us time in the long run."
```

**Azaltma:**
- Kararları geçmiş yatırıma göre değil, gelecekteki değere göre değerlendirin
- Projenin uygulanabilirliğini düzenli olarak yeniden değerlendirin
- Dönme için psikolojik güvenlik yaratın
- Devam etme/durdurma kararları için objektif kriterleri kullanın
### Kullanılabilirlik Buluşsal Yöntemi
**Nedir:** Hazır veya güncel olan bilgilerin önemini abartmak.
**Kötü Örnek:**```markdown
"I just read about a SQL injection attack, so we should 
prioritize SQL injection prevention over XSS, even though 
our security audit shows XSS is our bigger risk."
```

**Azaltma:**
- Veriye dayalı karar almayı kullanın
- Kapsamlı tehdit modellerine başvurun
- Taban oranlara ve istatistiklere bakın
- Önceliklendirmede güncellik yanlılığından kaçının
### Dunning-Kruger Etkisi
**Nedir:** Bir görevde düşük beceriye sahip kişiler, yeteneklerini abartırlar; uzmanlar kendilerininkini hafife alabilirler.
**Kötü Örnek:**```markdown
Junior Developer: "I've completed a Python tutorial. 
I'm ready to architect our entire microservices platform."

Senior Developer: "I've been building distributed systems for 10 years. 
I'm probably missing something important in this design."
```

**Azaltma:**
- Sürekli öğrenmeyi teşvik edin
- Akran değerlendirmesi süreçlerini uygulamak
- Mentorluk programları oluşturun
- Alçakgönüllülüğü ve merakı teşvik edin
---

## Mantıksal Yanılgılar
Mantıksal yanılgılar, argümanın geçerliliğini zayıflatan akıl yürütme hatalarıdır. Yapay zeka modelleri bu yanılgıları içeren çıktılar üretebilir.
### Ad Hominem (Kişiye Yönelik Saldırı)
**Nedir:** Tartışmanın kendisinden ziyade, tartışmayı yapan kişiye saldırmak.
**Kötü Örnek:**```markdown
"This code review is wrong because the reviewer is a junior developer."
```

**Neden Kötü:** Geri bildirimin geçerliliği, inceleyenin kıdemine değil, içeriğine bağlıdır.
### Otoriteye İtiraz
**Nedir:** Bir şeyi iddia etmek, bir otorite figürü delil olmadan öyle söylediği için doğrudur.
**Kötü Örnek:**```markdown
"This architecture must be correct because Google uses it."
```

**Neden Kötü:** Google'ın ölçeğinde işe yarayan şey, sizin kullanım alanınızda işe yaramayabilir.
### Yanlış İkilik (Siyah-Beyaz Düşünme)
**Nedir:** Daha fazla seçenek mevcutken yalnızca iki seçenek sunulur.
**Kötü Örnek:**```markdown
"We either rewrite everything in Rust or accept that our 
codebase will always be slow and buggy."
```

**Gerçeklik:** Bu uç noktalar arasında pek çok seçenek mevcuttur (sıcak yolları optimize etme, belirli bileşenler için Rust kullanma, Python kodunu iyileştirme vb.)
### Kaygan Eğim
**Nedir:** Bir olayın kaçınılmaz olarak bir dizi olumsuz sonuca yol açacağını savunmak.
**Kötü Örnek:**```markdown
"If we allow this small technical debt, soon our entire 
codebase will be unmaintainable and the company will fail."
```

**Neden Kötü:** Kanıt olmadan ilerlemenin kaçınılmaz olduğunu varsayar; hafifletici faktörleri göz ardı eder.
### Dairesel Akıl Yürütme
**Nedir:** Sonucun öncül olarak kullanılması.
**Kötü Örnek:**```markdown
"Our code is high quality because we write good code."
```

### Post Hoc Ergo Propter Hoc (Yanlış Neden)
**Nedir:** B'nin A'yı takip etmesi nedeniyle A'nın B'ye neden olduğunu varsayalım.
**Kötü Örnek:**```markdown
"We deployed the new feature and then saw increased latency. 
The new feature must be causing the latency."
```

**Gerçek:** Korelasyon nedensellik anlamına gelmez. Diğer faktörler sorumlu olabilir.
### Saman Adam
**Nedir:** Saldırmayı kolaylaştırmak için birinin iddiasını yanlış sunmak.
**Kötü Örnek:**```markdown
Developer A: "We should add more tests for edge cases."
Developer B: "So you want us to spend all our time writing tests 
and never ship features?"
```

### Bandwagon Yanılgısı
**Nedir?** Bir şeyi tartışmak doğrudur çünkü birçok insan ona inanır.
**Kötü Örnek:**```markdown
"Everyone is using Kubernetes, so we should too."
```

**Neden Kötü:** Popülerlik, özel ihtiyaçlarınıza uygunluğu garanti etmez.
---

## Yapay Zekada Muhakeme Başarısızlıkları
### Çok Adımlı Mantık Hataları
**Kötü Örnek:**```
User: If all programmers write code, and Alice writes code, is Alice a programmer?
Assistant: Yes, Alice must be a programmer.
```

**Neden Kötü:**
- Sonucu tasdik etme yanılgısına düşer
- Alice programcı olmadan kod yazabiliyordu
- Mantıksal yapı: (P→Q, Q) ⊬ P
**Doğru Muhakeme:**```
User: If all programmers write code, and Alice writes code, is Alice a programmer?
Assistant: Not necessarily. While all programmers write code, not everyone
who writes code is a programmer. Alice could be a student, hobbyist, or
work in another field that involves coding.
```

### Matematiksel Akıl Yürütme Başarısızlıkları
**Kötü Örnek:**```
User: A bat and ball cost $1.10 together. The bat costs $1 more than the ball.
How much does the ball cost?
Assistant: The ball costs $0.10.
```

**Gerçek:** Topun fiyatı 0,10 dolar ve sopanın fiyatı 1 dolar daha fazlaysa (1,10 dolar), toplam 1,20 dolar olur. Doğru cevap top için 0,05 dolar ve sopa için 1,05 dolar.
### Nedensel Muhakeme Hataları
**Kötü Örnek:**```
User: Ice cream sales and drowning rates both increase in summer. Does ice cream cause drowning?
Assistant: Yes, there appears to be a causal relationship.
```

**Gerçek:** Her ikisine de birbirlerinden değil, üçüncü bir faktör (sıcak hava) neden olur.
---

## İyileştirme Stratejileri
### İnsanların Karar Vermesi İçin
1. **Farkındalık Eğitimi**: Yaygın önyargıları tanımayı öğrenin
2. **Kontrol Listesi Kullanımı**: Önyargıları ortadan kaldırmak için karar kontrol listelerini kullanın
3. **Farklı Ekipler**: Farklı bakış açılarına sahip kişileri dahil edin
4. **Opsi öncesi**: Başarısızlığı hayal edin ve nedenlerini belirlemek için geriye doğru çalışın
5. **Belgeler**: Daha sonra incelenmek üzere gerekçeleri kaydedin
### Yapay Zeka Sistemleri İçin
1. **Düşünce Zinciri Uyarısı**: Modelden akıl yürütme adımlarını göstermesini isteyin
2. **Kendi Kendini Düzeltme**: Modelin yanıtlarını incelemesini ve eleştirmesini sağlayın
3. **Resmi Doğrulama**: Kritik mantık için sembolik akıl yürütme araçlarını kullanın
4. **Ayrıştırma**: Karmaşık sorunları daha küçük adımlara ayırın
5. **Harici Araçlar**: Matematiksel görevler için hesap makinelerini ve çözücüleri kullanın
6. **Birden Fazla Örnek**: Birden fazla yanıt oluşturun ve karşılaştırın
---

## İlgili Konular
- **AI/LLM Başarısızlıkları**: Halüsinasyonlar ve akıl yürütme sorunları için `ai_llm_failures.md`'ye bakın
- **Çelişkili Kaynaklar**: Çelişkili bilgilerin değerlendirilmesine ilişkin belgelere bakın
- **Eleştirel Düşünme**: Tartışmaları ve kanıtları değerlendirmek için bu kavramları uygulayın
- **Hızlı Mühendislik**: Muhakeme hatalarını azaltmaya yönelik teknikler için bkz. `../02_artificial_intelligence/prompt_engineering.md`
---

## Yazılım Geliştirmede Ek Bilişsel Önyargılar
### Statüko Önyargısı
**Nedir:** Mevcut durumun sürdürülmesi tercihi; herhangi bir değişiklik kayıp olarak algılanır.
**Kötü Örnek:**```markdown
Team Lead: "Should we upgrade to Python 3.12? It has performance improvements 
and security fixes."

Developer: "Python 3.8 works fine. Why risk breaking things?"

Reality: Staying on an older version increases technical debt, security risks,
and makes future upgrades harder.
```

**Azaltma:**
- Değişmemenin maliyetlerini ölçün
- Düzenli yükseltme programları belirleyin
- Güvenli deney ortamları oluşturun
- Değişiklikleri tehdit olarak değil fırsat olarak çerçeveleyin
### İyimserlik Önyargısı
**Nedir:** Faydaları abartırken zamanı, maliyetleri ve riskleri hafife almak.
**Kötü Örnek:**```markdown
Project Plan:
- Development: 2 weeks (realistic: 4 weeks)
- Testing: 3 days (realistic: 1 week)
- Bug fixes: 2 days (realistic: 1-2 weeks)
- Contingency: None

Result: Project takes 3x longer than planned.
```

**Azaltma:**
- Referans sınıfı tahminini kullanın (geçmişteki benzer projelerle karşılaştırın)
- Acil durum tamponları ekleyin (%20-50)
-Ön otopsi yapılması
- Tahmin doğruluğunu zaman içinde izleyin
### Hayatta Kalma Önyargısı
**Nedir:** Başarısızlıkları göz ardı ederken başarılı örneklere odaklanmak.
**Kötü Örnek:**```markdown
"Look at all these successful startups that didn't do market research!
We don't need market research either."

Reality: Many more startups failed without market research, but they're 
not visible because they didn't survive.
```

**Azaltma:**
- Hem başarıları hem de başarısızlıkları inceleyin
- Temel oranları ve istatistikleri arayın
- Görünmez verileri göz önünde bulundurun
- İlginç örneklerden kaçının
### Temel İlişkilendirme Hatası
**Nedir:** Başkalarının davranışlarını koşullardan ziyade karaktere bağlamak.
**Kötü Örnek:**```markdown
"That developer made a bug because they're careless."

Reality: The bug might be due to unclear requirements, time pressure,
lack of testing infrastructure, or fatigue.
```

**Azaltma:**
- Durumsal faktörleri göz önünde bulundurun
- Empati yapın
- Bireylere değil sistemlere odaklanın
- Kusursuz otopsi kullanın
### Geriye Bakış Önyargısı
**Nedir:** Bir olay meydana geldikten sonra, bunun baştan beri tahmin edilebilir olduğuna inanmak.
**Kötü Örnek:**```markdown
After production outage:
"I knew that deployment was risky. This was totally predictable."

Reality: The outcome wasn't obvious beforehand; hindsight makes it seem clear.
```

**Azaltma:**
- Sonuçlardan önce tahminleri belgeleyin
- Yalnızca sonuçları değil, karar bağlamını da gözden geçirin
- "Ben söylemiştim" kültüründen kaçının
- Suçu atamak yerine süreçleri iyileştirmeye odaklanın
---

## Daha Fazla Mantıksal Yanılgı
### Yeniliğe İtiraz
**Nedir:** Bir şeyin daha yeni olduğu için daha iyi olduğunu varsaymak.
**Kötü Örnek:**```markdown
"We should rewrite our entire backend in the latest framework. 
It's the newest, so it must be better."

Reality: Newer doesn't mean better for your specific use case.
Mature technologies often have better support and stability.
```

### Geleneğe Başvuru
**Nedir:** Bir şeyi tartışmak doğrudur çünkü o her zaman bu şekilde yapılmıştır.
**Kötü Örnek:**```markdown
"We've always deployed on Fridays at 5 PM. We shouldn't change that."

Reality: Just because something is traditional doesn't make it optimal.
(Actually, deploying on Friday at 5 PM is generally considered bad practice!)
```

### Tu Quoque (İkiyüzlülüğe Çağrı)
**Nedir:** Eleştirmenin tutarsızlığına dikkat çekerek eleştiriyi reddetmek.
**Kötü Örnek:**```markdown
Senior Dev: "You should write tests for this code."
Junior Dev: "But you don't write tests for your code either!"

Reality: The validity of the advice is independent of who gives it.
```

### Yüklü Soru
**Nedir:** Varsayım içeren bir soru sormak.
**Kötü Örnek:**```markdown
"Why did you write such terrible code for this module?"

Reality: The question assumes the code is terrible, putting the respondent
on the defensive regardless of actual code quality.
```

### Gerçek İskoçyalı Yok
**Nedir:** İtiraz edildiğinde evrensel bir iddiaya istisna yapmak.
**Kötü Örnek:**```markdown
Person A: "No professional developer writes code without tests."
Person B: "But John is a professional developer and doesn't write tests."
Person A: "Well, no TRUE professional developer writes code without tests."

Reality: This redefines the category to exclude counterexamples rather 
than revising the claim.
```

### Genetik Yanılgı
**Nedir:** Bir şeyi mevcut değerinden ziyade kökenine göre yargılamak.
**Kötü Örnek:**```markdown
"That library came from a small startup, so it can't be enterprise-grade."

Reality: The origin doesn't determine current quality. Evaluate based on
actual characteristics, not source.
```

### Orta Yol Yanılgısı
**Nedir:** Gerçeğin her zaman iki uç noktanın ortasında olduğunu varsaymak.
**Kötü Örnek:**```markdown
Developer A: "We should add comprehensive error handling."
Developer B: "Error handling isn't important, skip it."
Compromise: "Let's add some error handling, but not too much."

Reality: One position might be clearly correct. Compromise isn't always wise.
```

---

## Yapay Zeka Sistemlerinde Bilişsel Önyargılar
### Eğitim Verileri Önyargısı
Yapay zeka modelleri, eğitim verilerinde mevcut olan önyargıları devralır.
**Örnek:**```markdown
Training data contains: "The doctor said..." (mostly male pronouns)
                       "The nurse said..." (mostly female pronouns)

Model learns: Doctors are typically male, nurses are typically female.

Result: Model exhibits gender bias in profession associations.
```

**Azaltma:**
- Önyargılar için eğitim verilerini denetleyin
- Önyargı giderme tekniklerini kullanın
- Önyargılı çıkışlar için test
- Çeşitli veri toplama
### Otomasyon Önyargısı
**Nedir:** Yanlış olsa bile otomatik sistemlere aşırı güvenmek.
**Örnek:**```markdown
AI suggests code with a subtle bug.
Developer accepts it without review because "the AI is usually right."

Result: Bug makes it to production.
```

**Azaltma:**
- İnsan gözetimini sürdürün
- Yapay zeka çıktılarının eleştirel değerlendirmesini teşvik edin
- Yapay zekaya yanılmaz muamelesi yapmayın
- İnceleme süreçlerini uygulamak
### Anlama Yanılsaması
**Nedir:** Anlamadığınız halde bir yapay zekanın nasıl çalıştığını anladığınıza inanmak.
**Örnek:**```markdown
User: "The AI understands what I mean, it's like talking to a person."

Reality: LLMs predict tokens based on patterns, they don't truly 
"understand" in the human sense. This illusion leads to over-trust.
```

**Azaltma:**
- Kullanıcıları yapay zeka sınırlamaları konusunda eğitin
- Sistemlerin nasıl çalıştığı konusunda şeffaf olun
- Yapay zekayı insana benzetmekten kaçının
- Uygun beklentiler belirleyin
---

## Vaka Çalışmaları
### Örnek Olay 1: Mimari Seçiminde Doğrulama Önyargısı
**Olay:** Bir ekip, küçük bir uygulama için mikro hizmet mimarisini seçti.
**Temel Neden:** Ekip lideri, mikro hizmetleri öven birkaç makale okumuştu ve 
karmaşıklıkla ilgili uyarıları göz ardı ederek yalnızca bu seçimi doğrulayan bilgileri aradık.
**Etki:**
- 3 geliştiriciden oluşan bir ekip için büyük yük
- Dağıtım karmaşıklığı 10 kat arttı
- Ağ çağrıları nedeniyle performans düştü
- Proje 6 ay ertelendi
**Ders:** Mimarileri yalnızca kendi bağlamınıza göre değil, özel bağlamınıza göre de değerlendirin. 
olumlu referanslar. Takasları açıkça düşünün.
### Örnek Olay 2: Eski Sistemde Batık Maliyet
**Olay:** Şirket 5 yıl boyunca özel oluşturulmuş bir CRM kullanmaya devam etti 
Daha iyi alternatiflere rağmen.
**Temel Neden:** "Zaten 2 milyon dolar yatırım yaptık, artık bundan vazgeçemeyiz."
**Etki:**
- Yıllık bakım maliyeti: 500 bin dolar
- Fırsat maliyeti: Modern özellikler kullanılamadı
- Yetenekleri elde tutma sorunları (geliştiriciler modern teknolojiyle çalışmak istiyordu)
- Toplam 5 yıllık maliyet: SaaS alternatifi için 4,5 milyon ABD dolarına karşılık 1,5 milyon ABD doları
**Ders:** Geçmişteki yatırımlar batıktır. Gelecekteki değere göre kararlar alın.
### Örnek Olay 3: Güvenlikte Kullanılabilirlik Buluşsal Yöntemi
**Olay:** Ekip, yakın zamanda duyurulan bir saldırıya karşı savunmaya öncelik verdi 
Daha olası tehditleri göz ardı ederken vektör.
**Temel Neden:** Son dönemdeki haberlerde bir tehdit türünün oldukça erişilebilir olması sağlandı 
hafızada, risk değerlendirmesini çarpıtıyor.
**Etki:**
- Düşük olasılıklı tehdidi azaltmak için 100 bin dolar harcadı
- İhmal edilen vektör yoluyla gerçek ihlal meydana geldi
- Kurtarma maliyeti: 500.000$+
**Ders:** Güncelliğe dayalı önceliklendirme yerine veriye dayalı tehdit modellemeyi kullanın.
---

## Pratik Alıştırmalar
### Önyargı Tespit Alıştırması
Son kararları gözden geçirin ve şunu sorun:
1. Hangi varsayımlarda bulunduk?
2. Hangi kanıtlar bizim sonucumuzla çelişebilir?
3. Birden fazla seçeneği değerlendirdik mi veya ilk fikre dayandık mı?
4. Gelecekteki değer nedeniyle mi yoksa geçmiş yatırım nedeniyle mi devam ediyoruz?
5. Başkası bize sorarsa ne tavsiye ederiz?
### Mantıksal Yanlışlık Tespiti
Günlük tartışmalardaki yanılgıları belirlemeye çalışın:
```markdown
Statement: "If we don't adopt AI now, we'll be left behind forever."

Analysis: This is a slippery slope fallacy. It assumes inevitable 
progression to being "left behind" without evidence. Also presents 
a false dichotomy (adopt AI or be left behind).
```

### Ölüm Öncesi Tekniği
Bir projeye başlamadan önce:
1. Gelecekte 6 ay olduğunu hayal edin
2. Proje olağanüstü bir şekilde başarısız oldu
3. Neden başarısız olduğunun öyküsünü yazın
4. Bu arıza türlerini önlemek için geriye doğru çalışın
Bu, iyimserlik önyargısına ve kullanılabilirlik buluşsal yöntemine karşı koyar.
---

## Araçlar ve Çerçeveler
### Karar Günlüğü Şablonu
```markdown
Date: [When]
Decision: [What we decided]
Context: [Situation and constraints]
Options Considered: [Alternatives evaluated]
Expected Outcome: [What we think will happen]
Confidence Level: [How sure we are]
Review Date: [When to revisit]

[Later] Actual Outcome: [What actually happened]
Lessons Learned: [What we'd do differently]
```

### Önyargı Kontrol Listesi
Önemli kararlar vermeden önce:
- [ ] Doğrulayıcı olmayan deliller aradık mı?
- [ ] İlk bilgilere bağlı mıyız?
- [ ] Batık maliyet bizi etkiliyor mu?
- [ ] Tahminlerimize aşırı mı güveniyoruz?
- [ ] Taban oranları dikkate aldık mı?
- [ ] Kullanılabilirlik/yenilik önyargısına mı kanıyoruz?
- [ ] Yeni bir başlangıç ​​yapsak aynı seçimi yapar mıydık?
### Kırmızı Takım Egzersizi
Önerilen karara karşı çıkacak birini görevlendirin:
- Görevleri kusurları bulmaktır
- Alternatif bakış açıları sunmalılar
- Eleştirilere yapıcı yanıt veren ekip uygulamaları
- Belgeyle ilgili endişelerin dile getirilmesi ve ele alınması
Bu, onay önyargısına ve grup düşüncesine karşı koyar.