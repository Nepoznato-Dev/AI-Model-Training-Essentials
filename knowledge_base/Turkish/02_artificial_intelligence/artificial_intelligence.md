# Yapay Zekâ

## Yapay Zekâ Nedir?

Yapay Zekâ (AI), düşünmek, öğrenmek ve sorun çözmek üzere programlanmış makinelerde insan zekâsının simüle edilmesini ifade eder. AI sistemleri; konuşmayı tanıma, karar verme, dilleri çevirme ve görsellerdeki nesneleri tanımlama gibi normalde insan zekâsı gerektiren görevleri yerine getirebilir. Bu terim, AI alanının kuruluş anı olarak yaygın biçimde kabul edilen 1956 Dartmouth Konferansı'nda John McCarthy tarafından ortaya atılmıştır.

Modern AI genel olarak, belirli görevler için tasarlanmış Dar AI'ye (Narrow AI, diğer adıyla Weak AI) ve tüm alanlarda insan bilişsel yeteneğine eşit ya da onu aşacak teorik Artificial General Intelligence'a (AGI) ayrılır. Günümüzdeki tüm AI sistemleri Dar AI'dir.

## Yapay Zekâ Tarihi

AI'nin tarihi yaklaşık seksen yıla yayılır. İlk kuramsal temeller, Alan Turing'in 1950 tarihli "Computing Machinery and Intelligence" makalesiyle atıldı; bu makale, bir makinenin insandan ayırt edilemeyecek kadar zekice davranış sergileme yetisini ölçen Turing Testi'ni tanıttı. 1956 Dartmouth Konferansı ise AI'yi resmî olarak akademik bir disiplin hâline getirdi.

1950'ler–1970'lerde ELIZA (basit bir chatbot) ve LISP (AI için tasarlanmış bir programlama dili) gibi iyimser erken dönem programlar ortaya çıktı. 1970'ler ve 1980'lerdeki "AI winters", beklentilerin karşılanmaması sonrasında fonların ve ilginin azaldığı dönemlerdi. 1980'lerdeki yeniden canlanma, insan uzmanlığını kodlayan kural tabanlı programlar olan uzman sistemlerle geldi. 2000'lerde internet ve büyüyen veri kümeleriyle beslenen makine öğrenimi atılımları yaşandı. 2010'larda ise derin öğrenme yükselişe geçti ve computer vision, natural language processing (NLP) ile reinforcement learning alanlarını dönüştürdü.

## Makine Öğrenimi

Makine Öğrenimi (ML), sistemlerin açıkça programlanmadan veriden öğrenmesini sağlayan bir AI alt alanıdır. Başlıca ML kategorileri şunlardır:

**Denetimli Öğrenme**: Model, etiketli giriş-çıkış çiftleri üzerinde eğitilir. Örnekler arasında spam tespiti ve görüntü sınıflandırma bulunur. Algoritmalar arasında linear regression, decision trees, support vector machines ve neural networks yer alır.

**Denetimsiz Öğrenme**: Model, etiketsiz veride örüntüler bulur. Örnekler arasında müşteri segmentasyonu ve anomali tespiti vardır. Algoritmalar arasında k-means clustering ve principal component analysis (PCA) bulunur.

**Pekiştirmeli Öğrenme**: Bir ajan, bir ortamla etkileşime girerek ve ödül ya da ceza alarak öğrenir. Oyun oynayan AI'lerde (AlphaGo, AlphaZero), robotikte ve recommendation systems alanında kullanılır.

**Yarı Denetimli ve Öz Denetimli Öğrenme**: Az miktarda etiketli veriyi büyük etiketsiz veri kümeleriyle birleştirir. GPT modelleri, ön eğitim sırasında öz denetimli bir yaklaşım kullanır.

## Derin Öğrenme

Derin Öğrenme, çok katmanlı yapay sinir ağları (deep networks) kullanan bir makine öğrenimi alt alanıdır. Beynin sinirsel yapısından gevşek biçimde ilham alan bu ağlar, verinin hiyerarşik temsillerini öğrenir. Derin öğrenme şu alanlara güç verir:

- **Computer Vision**: Görüntü tanıma, nesne tespiti, medical imaging
- **Natural Language Processing**: Machine translation, sentiment analysis, question answering
- **Speech Recognition**: Siri, Alexa, Google Assistant gibi sesli asistanlar
- **Generative AI**: Görüntü üretimi (DALL-E, Stable Diffusion), metin üretimi (GPT)

Başlıca derin öğrenme mimarileri arasında görüntüler için convolutional neural networks (CNNs), diziler için recurrent neural networks (RNNs) ve LSTM'ler, dil için transformers ve sentez için generative adversarial networks (GANs) yer alır.

## Büyük Dil Modelleri (LLM'ler)

Large Language Models (LLM'ler), insan dilini anlamak ve üretmek için çok büyük miktarda metin verisi üzerinde eğitilen AI sistemleridir. Temelleri, Vaswani ve arkadaşlarının 2017 tarihli "Attention is All You Need" makalesinde tanıtılan Transformer mimarisine dayanır. LLM'ler bir dizideki sonraki token'ı (kelime parçasını) tahmin eder; bu da onların tutarlı metin üretmesine, soruları yanıtlamasına, kod yazmasına ve akıl yürütme görevlerini yerine getirmesine olanak tanır.

Öne çıkan LLM'ler şunlardır:
- **GPT serisi** (OpenAI): GPT-3, GPT-4 ve devam modelleri — sohbet ve kod için yaygın olarak kullanılır
- **Claude** (Anthropic): Güvenlik ve faydalılık odağıyla geliştirilmiştir
- **Gemini** (Google DeepMind): Metin, görsel ve kodu birleştiren multimodal modeller
- **LLaMA / Llama 3** (Meta): Araştırma ve yerel dağıtım için open-weight modeller
- **Mistral** (Mistral AI): Çok daha büyük LLM'lerle rekabet eden verimli açık modeller

LLM'ler iki aşamada eğitilir: pre-training (büyük metin külliyatları üzerinde denetimsiz eğitim) ve fine-tuning (denetimli olarak ya da insan geri bildiriminden pekiştirmeli öğrenme, RLHF, yoluyla). Context window, bir LLM'in aynı anda ne kadar metni işleyebildiğini anlatır; bu pencere erken GPT-3'te 4K token'dan, 2024'ün en gelişmiş modellerinde 1 milyondan fazla token'a kadar uzanır.

## Yapay Zekâ Etiği ve Güvenliği

AI; önyargı, mahremiyet, iş kaybı ve kötüye kullanım riski gibi önemli etik sorular doğurur. Algoritmik önyargı, eğitim verileri tarihsel eşitsizlikleri yansıttığında ortaya çıkar ve AI sistemlerinin ayrımcı çıktılar üretmesine neden olur. Facial recognition sistemlerinin koyu tenli bireylerde daha yüksek hata oranları gösterdiği görülmüştür. İşe alım algoritmalarının erkek adayları kayırdığı da tespit edilmiştir.

AI güvenliği, AI sistemlerinin amaçlandığı gibi davranmasını ve istenmeyen zararlar vermemesini sağlamaya adanmış alandır. Başlıca kaygılar şunlardır:
- **Alignment**: AI hedeflerinin insan değerleriyle uyumlu olmasını sağlamak
- **Interpretability / Explainability**: Bir AI'nin neden belirli bir karar verdiğini anlamak (tıp, hukuk, finans için kritik)
- **Misuse**: AI tarafından üretilen deepfake'ler, dezenformasyon, siber saldırılar
- **Existential risk**: Gelecekteki bir AGI'nin insanlığın hayatta kalmasıyla uyumsuz hedefler izleyebileceğine dair teorik kaygı

AI güvenliği üzerinde çalışan kuruluşlar arasında OpenAI'nin Safety ekibi, Anthropic (eski OpenAI güvenlik araştırmacıları tarafından kuruldu), DeepMind'ın safety ekibi ve MIRI ile ARC gibi bağımsız enstitüler bulunur.

## Toplumda Yapay Zekâ

AI neredeyse her sektörü dönüştürüyor:

- **Healthcare**: AI; medical imaging üzerinden kanser teşhisine yardımcı olur, hasta sonuçlarını tahmin eder, ilaç keşfini hızlandırır (AlphaFold protein katlanma yapısı tahminini çözdü) ve tedavi planlarını kişiselleştirir.
- **Finance**: Fraud detection, algorithmic trading, credit scoring ve robo-advisors ML modellerini kullanır.
- **Transportation**: Otonom araçlar computer vision, lidar ve reinforcement learning kullanır. Tesla Autopilot, Waymo ve Cruise başlıca girişimlerdir.
- **Education**: Kişiselleştirilmiş öğrenme platformları, içeriği öğrencinin bireysel hızına ve öğrenme tarzına göre uyarlar.
- **Creative fields**: AI müzik, sanat ve yazı üretir; Midjourney, DALL-E ve GitHub Copilot gibi araçlar yaratıcı iş akışlarını değiştirmiştir.
- **Cybersecurity**: AI anomalileri tespit eder, tehditleri belirler ve hem saldırılara hem savunmalara güç verir.

## Robotik ve Bedensel Yapay Zekâ

Robotik, AI'yi fiziksel makinelerle birleştirir. Modern robotlar, ortamlarda gezinmek ve nesneleri manipüle etmek için algılama (kameralar, lidar), planlama ve kontrol kullanır. Boston Dynamics'in Atlas'ı gelişmiş iki ayaklı hareket kabiliyetini gösterir. ABB ve FANUC gibi şirketlerin endüstriyel robotları üretimi otomatikleştirir. Ev robotları (Roomba) ve cerrahi robotlar (da Vinci System), AI'yi günlük ve tıbbi ortamlarda uygular. Bedensel AI araştırmaları, dünyayla etkileşim yoluyla fiziksel beceriler öğrenen ajanlara odaklanır ve simüle edilmiş ortamlarla gerçek ortamlar arasındaki boşluğu kapatmayı amaçlar.

## Güncel Yapay Zekâ Eğilimleri (2020'ler)

- **Multimodal AI**: Metin, görsel, ses ve videoyu birlikte işleyen sistemler (GPT-4V, Gemini)
- **Agents ve agentic AI**: Araç kullanabilen, web'de gezinebilen, kod yazabilen ve çok adımlı eylemler gerçekleştirebilen LLM'ler (OpenAI's Operator, Anthropic Computer Use)
- **Open-weight models**: Meta'nın LLaMA'sı, araştırmacılar için büyük modellere erişimi demokratikleştirdi
- **On-device AI**: AI modellerini cloud bağlantısı olmadan telefonlarda ve dizüstü bilgisayarlarda yerel olarak çalıştırmak (Apple Intelligence, Qualcomm NPUs)
- **AI regulation**: EU AI Act (2024), AI sistemlerini risk düzeyine göre sınıflandıran dünyanın ilk kapsamlı AI yasasıdır
