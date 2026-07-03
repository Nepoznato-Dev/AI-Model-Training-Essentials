# Yapay Zekâ

## Yapay Zekâ Nedir?

Yapay Zekâ (AI), düşünmek, öğrenmek ve problem çözmek üzere programlanmış makinelerde insan zekâsının benzetimini ifade eder. AI sistemleri; konuşmayı tanıma, karar verme, diller arasında çeviri yapma ve görüntülerde nesneleri belirleme gibi normalde insan zekâsı gerektiren görevleri yerine getirebilir. Terim, 1956'da Dartmouth Konferansı'nda John McCarthy tarafından ortaya atılmıştır; bu konferans, AI alanının kurucu etkinliği olarak yaygın biçimde kabul edilir.

Modern AI genel olarak, belirli görevler için tasarlanan Dar AI (Zayıf AI olarak da adlandırılır) ve tüm alanlarda insanın bilişsel yeteneğine eşit ya da onu aşacak kuramsal Yapay Genel Zekâ (AGI) olmak üzere ikiye ayrılır. Günümüzdeki tüm AI sistemleri Dar AI kapsamındadır.

## AI Tarihi

AI tarihinin kapsamı yaklaşık seksen yıla uzanır. Erken kuramsal temeller Alan Turing tarafından atılmıştır; Turing'in 1950 tarihli "Computing Machinery and Intelligence" makalesi, bir makinenin insandan ayırt edilemeyecek zeki davranış sergileyebilme yeteneğini ölçen Turing Testi'ni tanıtmıştır. 1956 Dartmouth Konferansı ise AI'ı resmen akademik bir disiplin olarak kurmuştur.

1950'lerden 1970'lere kadar ELIZA (basit bir sohbet botu) ve LISP (AI için tasarlanmış bir programlama dili) gibi iyimser erken dönem programlar görüldü. 1970'ler ve 1980'lerdeki "AI kışları", karşılanamayan beklentilerin ardından fonların ve ilginin azaldığı dönemlerdi. 1980'lerde kural tabanlı, insan uzmanlığını kodlayan programlar olan uzman sistemlerle yeniden canlanma yaşandı. 2000'ler, internetin ve büyüyen veri kümelerinin beslediği makine öğrenmesi atılımlarını getirdi. 2010'larda derin öğrenmenin yükselişi; bilgisayarlı görü, doğal dil işleme (NLP) ve pekiştirmeli öğrenmeyi dönüştürdü.

## Makine Öğrenmesi

Makine Öğrenmesi (ML), sistemlerin açıkça programlanmadan veriden öğrenmesini sağlayan AI'ın bir alt alanıdır. Başlıca ML kategorileri şunlardır:

**Denetimli Öğrenme**: Model, etiketlenmiş girdi-çıktı çiftleri üzerinde eğitilir. Örnekler arasında spam tespiti ve görüntü sınıflandırma yer alır. Algoritmalar arasında doğrusal regresyon, karar ağaçları, destek vektör makineleri ve sinir ağları bulunur.

**Denetimsiz Öğrenme**: Model, etiketsiz verilerde örüntüler bulur. Örnekler arasında müşteri segmentasyonu ve anomali tespiti yer alır. Algoritmalar arasında k-means kümeleme ve temel bileşen analizi (PCA) bulunur.

**Pekiştirmeli Öğrenme**: Bir ajan, bir ortamla etkileşime girerek ödüller veya cezalar alır ve bu yolla öğrenir. Oyun oynayan AI sistemlerinde (AlphaGo, AlphaZero), robotikte ve öneri sistemlerinde kullanılır.

**Yarı Denetimli ve Öz Denetimli Öğrenme**: Az miktarda etiketli veriyi büyük etiketsiz veri kümeleriyle birleştirir. GPT modelleri, ön eğitim sırasında öz denetimli bir yaklaşım kullanır.

## Derin Öğrenme

Derin Öğrenme, çok katmanlı yapay sinir ağlarını (derin ağları) kullanan makine öğrenmesinin bir alt alanıdır. Beynin sinirsel yapısından genel olarak esinlenen bu ağlar, verinin hiyerarşik temsillerini öğrenir. Derin öğrenme şunları mümkün kılar:

- **Bilgisayarlı Görü**: Görüntü tanıma, nesne tespiti, tıbbi görüntüleme
- **Doğal Dil İşleme**: Makine çevirisi, duygu analizi, soru yanıtlama
- **Konuşma Tanıma**: Siri, Alexa, Google Assistant gibi sesli asistanlar
- **Üretken AI**: Görüntü üretimi (DALL-E, Stable Diffusion), metin üretimi (GPT)

Başlıca derin öğrenme mimarileri arasında görüntüler için evrişimli sinir ağları (CNN'ler), diziler için tekrarlayan sinir ağları (RNN'ler) ve LSTM'ler, dil için transformer'lar ve sentez için üretici çekişmeli ağlar (GAN'ler) bulunur.

## Büyük Dil Modelleri (LLM'ler)

Büyük Dil Modelleri (LLM'ler), insan dilini anlamak ve üretmek için çok büyük miktarda metin verisi üzerinde eğitilen AI sistemleridir. Vaswani ve arkadaşlarının 2017 tarihli "Attention is All You Need" makalesinde tanıtılan Transformer mimarisine dayanırlar. LLM'ler bir dizideki bir sonraki token'ı (kelime parçasını) tahmin eder; bu da onların tutarlı metin üretmesini, soruları yanıtlamasını, kod yazmasını ve akıl yürütme görevlerini yerine getirmesini sağlar.

Dikkate değer LLM'ler şunlardır:
- **GPT serisi** (OpenAI): GPT-3, GPT-4 ve ardılları — sohbet ve kod için yaygın olarak kullanılır
- **Claude** (Anthropic): Güvenlik ve faydalılığa odaklanır
- **Gemini** (Google DeepMind): Metin, görüntü ve kodu birleştiren çok modlu model
- **LLaMA / Llama 3** (Meta): Araştırma ve yerel dağıtım için açık ağırlıklı modeller
- **Mistral** (Mistral AI): Çok daha büyük LLM'lerle rekabet edebilen verimli açık modeller

LLM'ler iki aşamada eğitilir: ön eğitim (büyük metin derlemleri üzerinde denetimsiz) ve ince ayar (denetimli veya insan geri bildiriminden pekiştirmeli öğrenme, RLHF, yoluyla). Bağlam pencereleri, bir LLM'in tek seferde ne kadar metni işleyebileceğini tanımlar; bu kapasite erken GPT-3'te 4K token'dan, en gelişmiş 2024 modellerinde 1 milyonu aşan token'a kadar değişir.

## AI Etiği ve Güvenliği

AI; önyargı, gizlilik, iş kaybı ve kötüye kullanım riski gibi önemli etik sorular doğurur. Algoritmik önyargı, eğitim verileri tarihsel eşitsizlikleri yansıttığında ortaya çıkar ve AI sistemlerinin ayrımcı çıktılar üretmesine neden olur. Yüz tanıma sistemlerinin koyu tenli bireylerde daha yüksek hata oranları gösterdiği görülmüştür. İşe alım algoritmalarının erkek adayları kayırdığı saptanmıştır.

AI güvenliği, AI sistemlerinin istenmeyen zararlara yol açmadan amaçlandığı gibi davranmasını sağlamaya adanmış alandır. Başlıca kaygılar şunlardır:
- **Hizalanma**: AI hedeflerinin insan değerleriyle uyumlu olmasını sağlama
- **Yorumlanabilirlik / Açıklanabilirlik**: Bir AI'ın neden belirli bir karar verdiğini anlama (tıp, hukuk ve finans alanlarında kritik önemdedir)
- **Kötüye kullanım**: AI tarafından üretilen deepfake'ler, dezenformasyon, siber saldırılar
- **Varoluşsal risk**: Gelecekteki bir AGI'ın insanlığın hayatta kalmasıyla uyumsuz hedefler izleyebileceğine dair kuramsal kaygı

AI güvenliği üzerinde çalışan kuruluşlar arasında OpenAI'ın Safety ekibi, Anthropic (eski OpenAI güvenlik araştırmacıları tarafından kurulmuştur), DeepMind'ın güvenlik ekibi ve MIRI ile ARC gibi bağımsız enstitüler bulunur.

## Toplumda AI

AI neredeyse her sektörü dönüştürmektedir:

- **Sağlık hizmetleri**: AI, tıbbi görüntülerden kanser tanısına yardımcı olur, hasta sonuçlarını öngörür, ilaç keşfini hızlandırır (AlphaFold protein katlanması yapı tahmini sorununu çözmüştür) ve tedavi planlarını kişiselleştirir.
- **Finans**: Dolandırıcılık tespiti, algoritmik alım satım, kredi puanlama ve robo-danışmanlar ML modellerini kullanır.
- **Ulaşım**: Otonom araçlar bilgisayarlı görü, lidar ve pekiştirmeli öğrenme kullanır. Tesla Autopilot, Waymo ve Cruise bu alandaki öncü girişimlerdendir.
- **Eğitim**: Kişiselleştirilmiş öğrenme platformları, içeriği öğrencinin bireysel hızına ve öğrenme tarzına uyarlar.
- **Yaratıcı alanlar**: AI müzik, sanat ve yazı üretir; Midjourney, DALL-E ve GitHub Copilot gibi araçlar yaratıcı iş akışlarını değiştirmiştir.
- **Siber güvenlik**: AI anomalileri tespit eder, tehditleri belirler ve hem saldırıları hem savunmaları güçlendirir.

## Robotik ve Bedenlenmiş AI

Robotik, AI'ı fiziksel makinelerle birleştirir. Modern robotlar, ortamlarda gezinmek ve nesneleri manipüle etmek için algılama (kameralar, lidar), planlama ve kontrol kullanır. Boston Dynamics'in Atlas'ı gelişmiş iki ayaklı hareket yeteneklerini gösterir. ABB ve FANUC gibi şirketlerin endüstriyel robotları üretimi otomatikleştirir. Ev robotları (Roomba) ve cerrahi robotlar (da Vinci System), AI'ı gündelik ve tıbbi ortamlarda uygular. Bedenlenmiş AI araştırmaları, simüle edilmiş ve gerçek ortamlar arasındaki boşluğu kapatarak dünya ile etkileşim yoluyla fiziksel beceriler öğrenen ajanlara odaklanır.

## Güncel AI Eğilimleri (2020'ler)

- **Çok modlu AI**: Metin, görüntü, ses ve videoyu birlikte işleyen sistemler (GPT-4V, Gemini)
- **Ajanlar ve ajansal AI**: Araç kullanabilen, web'de gezinebilen, kod yazabilen ve çok adımlı eylemler gerçekleştirebilen LLM'ler (OpenAI'ın Operator'ı, Anthropic Computer Use)
- **Açık ağırlıklı modeller**: Meta'nın LLaMA'sı, büyük modellere erişimi araştırmacılar için demokratikleştirdi
- **Cihaz üstü AI**: AI modellerini bulut bağlantısı olmadan telefonlarda ve dizüstü bilgisayarlarda yerel olarak çalıştırma (Apple Intelligence, Qualcomm NPU'ları)
- **AI düzenlemeleri**: EU AI Act (2024), AI sistemlerini risk düzeyine göre sınıflandıran dünyanın ilk kapsamlı AI yasasıdır
