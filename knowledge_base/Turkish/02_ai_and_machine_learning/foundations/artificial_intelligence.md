---
# Metadata
title: "Artificial Intelligence"
description: "AI overview, ML, deep learning, LLMs, ethics"
category: "AI and Machine Learning"
subcategory: "Foundations"
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
    changes: "Moved to foundations/ subfolder; added subcategory field"
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
tags: [artificial, intelligence, ai-and-machine-learning]
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
# Yapay Zeka
Yapay zeka, bir insanın yapması durumunda zeka gerektirecek şeyleri yapabilen makineler üretme girişimidir: yüzleri tanımak, konuşmayı anlamak, karar vermek, metin yazmak, oyun oynamak, araba kullanmak, hastalıkları teşhis etmek. Bu alan hesaplamanın kendisi kadar eskidir - Alan Turing "Makineler düşünebilir mi?" diye soruyordu. 1950'de - ancak yeteneklerdeki son patlama (2020'ler), yapay zekayı insanlık tarihindeki en önemli ve tartışmalı teknolojilerden biri haline getirdi.
---

## Kısa Bir Tarih
Yapay zeka onlarca yıldır heyecan ve hayal kırıklığı döngülerinden geçti. Bu tarihi anlamak, insanların neden hem heyecanlı hem de şüpheci olduğunu anlamanıza yardımcı olur.
| Çağ | Ne Oldu | Sonuç |
|-----|---------------|-----------|
| **1950'ler-1960'lar** | Erken iyimserlik. Turing Testi önerildi (1950). Dartmouth Konferansı "Yapay Zeka"yı (1956) basıyor. ELIZA (sohbet robotu) ve SHRDLU (dil anlayışı) gibi ilk programlar. | Heyecan: "Bir nesil sonra AGI'mız olacak!" |
| **1970'ler** | İlk AI kışı. Erken yaklaşımların sınırlamaları netleşiyor. Finansman kuruyor. | Hayal kırıklığı: yerine getirilmeyen sözler |
| **1980'ler** | Uzman sistemler patlaması — insanın uzman bilgisini kodlayan kural tabanlı programlar. Japonya'nın Beşinci Nesil projesi. | Yeniden heyecan: kurumsal yapay zeka yatırımları |
| **1987-1993** | İkinci AI kışı. Uzman sistemlerin kırılgan olduğu ve bakımının pahalı olduğu kanıtlanmıştır. | Yine hayal kırıklığı |
| **2000'ler** | Makine öğrenimi ilgi görüyor. Daha fazla veri mevcut (internet). İstatistiksel yöntemler elle kodlanmış kuralların yerini alır. | İstikrarlı ilerleme |
| **2012+** | Derin öğrenme devrimi. AlexNet, GPU'ları kullanan ImageNet yarışmasını kazandı. Sinir ağları görme, konuşma ve dil konusunda geleneksel yöntemlerden daha iyi performans göstermeye başlıyor. | Hızlı dönüşüm |
| **2017** | "İhtiyacınız Olan Tek Şey Dikkat" makalesi Transformer mimarisini tanıtıyor. | Sonraki her şeyin temeli |
| **2020-2026** | Büyük dil modelleri (GPT-3, GPT-4, Claude, Gemini, LLaMA). Yapay zeka metin, kod, görseller ve video üretir. Kurumsal benimseme hızlanır. | Yapay Zeka günlük yaşamın bir parçası haline geliyor |
---

## Modern Yapay Zeka Nasıl Çalışır?
### Makine Öğrenimi — Verilerden Öğrenme
Makine öğrenimi, açık kurallar programlamak yerine verileri kendi kendine kalıp bulan algoritmalara besler.
| Tür | Nasıl Çalışır | Örnek |
|------|-------------|--------|
| **Denetimli öğrenme** | Etiketli örnekler üzerinde eğitim alın (girdi → doğru çıktı) | Spam tespiti: "spam" veya "spam değil" etiketli binlerce e-postayı besleyin |
| **Denetimsiz öğrenme** | Etiketlenmemiş verilerdeki kalıpları bulun | Müşteri segmentasyonu: grupları önceden tanımlamadan benzer müşterileri gruplandırın |
| **Takviyeli öğrenme** | Temsilci deneme yanılma yoluyla öğrenir, ödül veya ceza alır | Oyun oynama yapay zekası: hamleleri deneyin, kazanmak için puan kazanın, hangi stratejilerin işe yaradığını öğrenin |
### Derin Öğrenme — Sinir Ağları
Derin öğrenme, yapay sinir ağlarını (bir araya toplandığında inanılmaz derecede karmaşık kalıpları öğrenebilen basit matematiksel işlemler katmanlarını) kullanır. "Derin" katman sayısını ifade eder.
Anahtar mimariler:
| Mimarlık | En İyisi | Gerçek Dünyada Kullanım |
|---------------|-----------|----------------|
| **CNN** (Evrişimli Sinir Ağı) | Görüntü ve mekansal veriler | Yüz tanıma, tıbbi görüntüleme, sürücüsüz arabalar |
| **RNN/LSTM** | Sıralı veriler (zaman serisi) | Konuşma tanıma, müzik üretimi (büyük ölçüde Transformers ile değiştirildi) |
| **Trafo** | Her şey — metin, resimler, ses, kod | GPT, Claude, Gemini, BERT, DALL-E — baskın mimari |
| **GAN** (Üretici Rekabet Ağı) | Gerçekçi veriler oluşturma | Görüntü sentezi, stil aktarımı (kısmen yayılma modelleriyle değiştirildi) |
| **Dağıtım modelleri** | Yüksek kaliteli görüntü/video oluşturma | Kararlı Difüzyon, DALL-E 3, Yolculuğun Ortası, Sora |
### Büyük Dil Modelleri (LLM'ler)
LLM'ler muazzam miktarda metin üzerinde eğitilmiş Transformer tabanlı modellerdir. Sıradaki bir sonraki simgeyi (kelime parçasını) tahmin etmeyi öğrenirler; bu da dilbilgisini, gerçekleri, akıl yürütmeyi ve hatta "bilgiye" benzeyen bir şeyi anlamayı gerektirir.
| Modeli | Geliştirici | Önemli Özellik |
|----------|---------------|------|
| **GPT-4 / GPT-4o** | OpenAI | Çok modlu (metin + resimler); güçlü muhakeme |
| **Claude** | Antropik | Güvenliğe ve yardımseverliğe odaklanın; uzun bağlam pencereleri |
| **İkizler** | Google DeepMind | Doğal olarak çok modlu; Google hizmetleriyle entegre |
| **LLaMA / Lama 3** | Meta | Açık ağırlık; yerel olarak çalıştırılabilir; büyük topluluk |
| **Mistral** | Mistral AI | Daha büyük modellerle rekabet edebilecek verimli açık modeller |
**Eğitim süreci**:
1. **Ön eğitim**: Büyük metin verilerinden bilgi edinin (sonraki jetonları tahmin etme). Modelin "bilgiyi" edindiği yer burasıdır.
2. **İnce ayar**: Belirli görevler üzerinde veya insan tercihleri ​​doğrultusunda eğitim alın.
3. **RLHF** (İnsan Geri Bildiriminden Güçlendirilmiş Öğrenme): İnsanlar model çıktılarını derecelendirir; model, insanların tercih ettiği çıktıları üretmeyi öğrenir.
**Bağlam pencereleri** (modelin aynı anda ne kadar metin işleyebileceği) 4K jetondan (GPT-3'ün başlarında) 2026 modellerinde 1 milyon jetonun üzerine çıktı.
---

## Yapay Zeka Neleri Yapabilir ve Yapamaz?
### Mevcut Yetenekler
| Görev | Performans | Sınırlamalar |
|------|-------------|------------|
| **Metin oluşturma** | Mükemmel — tutarlı, bağlamsal, stil açısından çeşitli | Halüsinasyon görebilir (güvenle yanlış bilgi üretebilir) |
| **Kod oluşturma** | Yaygın kalıplar için çok iyi; tüm programları yazabilir | Yeni mimarilerle mücadele; ince hatalara neden olabilir |
| **Görüntü oluşturma** | Fotogerçekçi; sanatsal stiller; düzenleme | Eller ve metin hâlâ kusurlu; kesin mekansal akıl yürütmeyle mücadele ediyor |
| **Çeviri** | Başlıca dil çiftleri için insana yakın | Düşük kaynaklı diller daha az doğru; kültürel nüanslar kaybolabilir |
| **Konuşma tanıma** | Temiz seste insana yakın | Ağır vurgular ve arka plan gürültüsüyle mücadele |
| **Akıl yürütme** | Hızla iyileşiyor; birçok mantıksal sorunu çözebilir | Gerçek bir anlayış gerektiren yeni problemlerde başarısız olunması |
| **Matematik** | Standart problemlerde iyi | Yeni delillerde hata yapar; resmi doğrulamanın yerini almaz |
| **Planlama ve araç kullanımı** | Gelişmekte olan (acenteler) | İnsan gözetiminin olmadığı karmaşık, çok adımlı görevler için hâlâ güvenilmez |
### Yapay Zekanın Yapamayacağı Şeyler (2026 itibariyle)
- **İnsanların yaptığı gibi her şeyi gerçekten anlayın**; anlam değil kalıpları işler
- **Gerçek doğruluğu garanti eder** — halüsinasyon çözülmemiş bir sorun olmaya devam etmektedir
- **Yüksek riskli kararlarda gözetimsiz olarak insan yargısının yerini alın**
- Eğitim verilerinden çok farklı alanlara **mükemmel genelleme**
- **Öngörülemeyen fiziksel ortamlarda bağımsız olarak çalışın** (robotik hala zordur)
---

## Yapay Zeka Etiği ve Güvenliği
Yapay zeka tarafsız değil. Üzerinde eğitim aldığı verileri, geliştiricilerinin seçimlerini ve onu uygulayan kuruluşların teşviklerini yansıtır.
### Temel Kaygılar
| Sayı | Ne Olur | Örnek |
|----------|----------------|-----------|
| **Önyargı** | Yapay zeka sistemleri eğitim verilerindeki önyargıları yeniden üretiyor ve güçlendiriyor | Erkek adayları tercih eden işe alım algoritmaları; koyu tenler için daha yüksek hata oranlarına sahip yüz tanıma |
| **Gizlilik** | Yapay zeka kişisel veriler üzerine eğitilmiştir; gözetim yetenekleri | Telif hakkıyla korunan eserlere ilişkin eğitim; kamusal alanlarda yüz tanıma |
| **Kötüye kullanım** | Deepfake, dezenformasyon, otomatik kimlik avı | Politikacıların yapay zeka tarafından oluşturulan sahte videoları; otomatik dolandırıcılık çağrıları |
| **İş değişikliği** | Daha önce insanlar tarafından yapılan görevlerin otomasyonu | İçerik oluşturma, müşteri hizmetleri, veri girişi, bazı programlama |
| **Hizalama** | Yapay Zeka hedeflerinin insani değerlerle eşleşmesini sağlamak | "Ataş üretimini en üst düzeye çıkarması" söylenen bir yapay zeka, tüm maddeleri ataçlara dönüştürebilir |
| **Varoluşsal risk** | Geleceğin YZG'sine ilişkin teorik kaygılar | Araştırmacılar arasındaki tartışma - bazıları bunu acil, bazıları ise henüz erken buluyor |
### Güvenlik Konusunda Kim Çalışıyor
- **Antropik** — özellikle yapay zeka güvenliğine odaklanan eski OpenAI araştırmacıları tarafından kuruldu
- **DeepMind Güvenliği** — Google DeepMind bünyesindeki araştırma ekibi
- **MIRI** (Makine Zekası Araştırma Enstitüsü) — teorik güvenlik araştırması
- **ARC** (Yapay Zeka Araştırma Merkezi) — ampirik güvenlik araştırması
- **Devlet kurumları** — AB Yapay Zeka Yasası (2026), ABD idari emirleri, uluslararası çerçeveler
---

## Uygulamada Yapay Zeka — Sektöre Göre Sektöre Göre
| Sanayi | Başvuru | Vade |
|----------|----------------|----------|
| **Sağlık Hizmetleri** | Görüntülerden kanser teşhisi; ilaç keşfi (AlphaFold); hasta sonuçlarını tahmin etmek | Konuşlandırıldı ve genişletiliyor |
| **Finans** | Dolandırıcılık tespiti, algoritmik ticaret, kredi puanlama, robot danışmanlar | Yaygın olarak dağıtılan |
| **Ulaşım** | Kendi kendine giden araçlar (Waymo, Tesla Autopilot); rota optimizasyonu | Kısmen konuşlandırılmış; tam özerklik hâlâ sınırlı |
| **Eğitim** | Kişiselleştirilmiş öğrenme; Yapay zeka eğitimi; otomatik sınıflandırma | Hızla büyüyor |
| **Yaratıcı alanlar** | Görüntü oluşturma (Yolculuk Ortası, DALL-E); müzik; yazma yardımı; kod tamamlama | İş akışlarını şimdi dönüştürüyoruz |
| **Siber güvenlik** | Tehdit tespiti; anormallik tespiti; hem saldırı hem de savunma | Silahlanma yarışı sürüyor |
| **Yasal** | Sözleşme analizi; belge incelemesi; hukuki araştırma | Evlat edinilmek; doğruluk endişeleri |
| **Tarım** | Uydu/drone aracılığıyla mahsul izleme; hassas püskürtme; getiri tahmini | Büyüyor |
| **İmalat** | Kalite denetimi; kestirimci bakım; tedarik zinciri optimizasyonu | Yaygın olarak dağıtılan |
---

## Robotik ve Somutlaştırılmış Yapay Zeka
Robotik, yapay zekayı fiziksel makinelerle birleştirir. Onlarca yıllık ilerlemeye rağmen, dünyayla fiziksel etkileşim hâlâ dijital zekadan çok daha zor.
- **Boston Dynamics Atlası** — gelişmiş iki ayaklı hareket; parkur; depo görevleri
- **Endüstriyel robotlar** (ABB, FANUC, KUKA) — üretimi otomatikleştirir; kaynak; montaj
- **Cerrahi robotlar** (da Vinci Sistemi) — insan elinin ötesinde hassasiyetle minimal invaziv cerrahi
- **Ev robotları** (Roomba) — basit ama ticari açıdan başarılı
- **İnsansı robotlar** (Tesla Optimus, Şekil AI) — ortaya çıkıyor; genel amaçlı fiziksel görevler hala çok zor
Muazzam bir ilerleme kaydeden dijital yapay zeka ile (el becerisi, denge ve öngörülemeyen ortamlarla mücadele eden) fiziksel yapay zeka arasındaki uçurum, alanın en büyük zorluklarından biridir.
---

## Güncel Trendler (2020'ler)
| Eğilim | Neler Oluyor |
|----------|-----------|
| **Çok modlu yapay zeka** | Metin, görüntü, ses ve videoyu birlikte işleyen sistemler (GPT-4V, Gemini) |
| **Acenteler** | Araçları kullanabilen, web'de gezinebilen, kod yazabilen ve çok adımlı eylemler gerçekleştirebilen Yüksek Lisans (LLM) |
| **Açık ağırlıklı modeller** | Meta'nın LLaMA'sı ve diğerleri büyük modellere erişimi demokratikleştiriyor |
| **Cihazda yapay zeka** | Modelleri telefonlarda ve dizüstü bilgisayarlarda yerel olarak çalıştırma (Apple Intelligence, Qualcomm NPU'lar) |
| **Yapay zeka düzenlemesi** | AB Yapay Zeka Yasası (2026) — ilk kapsamlı yapay zeka yasası; sistemleri risk düzeyine göre sınıflandırma |
| **Bilimde yapay zeka** | Protein katlanması (AlphaFold), malzeme keşfi, iklim modellemesi, matematiksel kanıtlar |
| **Küçük dil modelleri** | Tüketici donanımında çalışan verimli modeller; kalite daha büyük modellere yaklaşıyor |
---

## Özet
Yapay zeka, 21. yüzyılın şimdiye kadarki en önemli teknolojik gelişmesidir. Bu bir sihir değil; büyük miktarda veri, güçlü donanım ve akıllı mimarilerin mümkün kıldığı ölçekte kalıp eşleştirmedir. Onu dönüştürücü kılan şey, yeterince iyi yapıldığında desen eşleştirmenin daha önce insan zekası gerektiren birçok görevi tekrarlayabilmesidir. Zorluklar da aynı derecede önemli: halüsinasyon, önyargı, işten çıkarma, kötüye kullanım ve dar yapay zekadan genel zekaya giden yolun kısa mı yoksa inanılmayacak kadar uzun mu olduğuna dair açık soru. Açık olan şu ki yapay zeka her sektörü, her mesleği ve günlük yaşamın her yönünü yeniden şekillendirecek. Nasıl çalıştığını ve neleri yapamayacağını anlamak, inşa ettiğimiz dünyada gezinmek için çok önemlidir.