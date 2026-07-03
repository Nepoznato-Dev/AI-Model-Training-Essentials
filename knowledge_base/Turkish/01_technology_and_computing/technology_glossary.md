# Teknoloji Sözlüğü

Modern yapay zekâ ve bilişim dünyasındaki yapay zekâ modelleri, donanım, kıyaslamalar ve temel kavramları kapsayan başvuru sözlüğü.

---

## Yapay Zekâ Dil Modelleri ve Asistanlar

### ChatGPT
ChatGPT, OpenAI tarafından geliştirilen ve ilk kez Kasım 2022'de yayımlanan bir yapay zekâ sohbet botudur.
GPT serisindeki büyük dil modelleri (LLM'ler) tarafından desteklenir. ChatGPT,
tarihte tüketiciye yönelik en hızlı büyüyen yapay zekâ ürünlerinden biridir ve
yayımlandıktan sonraki iki ay içinde 100 milyon kullanıcıya ulaşmıştır. Metin tabanlı
sohbeti, kod üretimini, özetlemeyi ve yaratıcı yazımı destekler. Ücretli katmanlar,
GPT-4 ve GPT-4o gibi daha güçlü modellere erişim sağlar.

### GPT (Generative Pre-trained Transformer)
GPT, OpenAI tarafından geliştirilen büyük dil modelleri ailesidir. Bu mimari,
decoder-only Transformer yapısını kullanır ve çok büyük metin derlemleri üzerinde
bir sonraki belirteci tahmin etme hedefiyle eğitilir. Önemli sürümler arasında
GPT-2 (2019, 1,5 milyar parametre, "yayınlanamayacak kadar tehlikeli" söylemiyle
dikkat çekmiştir), GPT-3 (2020, 175 milyar parametre, API üzerinden yaygın olarak
kullanılmıştır), GPT-3.5 (ilk ChatGPT'nin omurgası) ve GPT-4 (2023, çok kipli,
birçok ölçütte insan uzman düzeyine yakın performans) yer alır.

### Claude
Claude, Anthropic tarafından geliştirilen bir yapay zekâ asistanıdır. Adını,
bilgi kuramının kurucusu Claude Shannon'dan alır. Anthropic, eski OpenAI
araştırmacıları tarafından kurulmuştur ve "constitutional AI" yaklaşımına odaklanır;
bu teknik, modellere bir ilke kümesini izlemeyi öğreterek onları daha güvenli hâle
getirmeyi amaçlar. Claude modelleri (Claude 1, 2, 3 Haiku / Sonnet / Opus), uzun
bağlam pencereleri (200.000 belirtece kadar), incelikli akıl yürütme yetenekleri ve
temel LLM'lere kıyasla daha az zararlı çıktı üretmeleriyle bilinir.

### Gemini
Gemini, Google DeepMind'ın Aralık 2023'te duyurduğu çok kipli yapay zekâ model
ailesidir. Gemini doğuştan çok kiplidir; önceki modellerde olduğu gibi sonradan
ince ayarla kip eklenmemiş, metin, görsel, ses ve video üzerinde en baştan birlikte
eğitilmiştir. Sürümler arasında Gemini Nano (cihaz üstü), Gemini Flash (hızlı,
maliyet açısından verimli) ve Gemini Ultra (en yüksek yetenek düzeyi) bulunur.
Gemini, Google'ın Bard adlı yapay zekâ sohbet botuna (yeniden adlandırıldıktan sonra
Gemini) ve Google Search AI Overviews özelliğine güç verir.

### Phi-3-mini
Phi-3-mini, Microsoft tarafından geliştirilen ve 3,8 milyar parametreye sahip küçük
bir dil modelidir (SLM). Nisan 2024'te yayımlanmıştır. Çoğu büyük modelin aksine,
Phi-3-mini, Microsoft Research'ün öncülük ettiği ve ham hacimden çok veri kalitesine
öncelik veren özenle seçilmiş "ders kitabı kalitesinde" bir veri kümesi üzerinde
eğitilmiştir. GPT-4 veya Claude 3 Opus'tan çok daha küçük olmasına rağmen, MMLU ve
HumanEval gibi akıl yürütme kıyaslamalarında kendisinden birkaç kat büyük modelleri
yakalar veya geride bırakır. Temel sürümünde 4 bin belirteçlik, uzun bağlamlı
sürümünde ise 128 bin belirteçlik bağlam penceresini destekler. Yeterli RAM'e sahip
modern bir akıllı telefonda cihaz üstünde ya da tek bir tüketici GPU'sunda
çalıştırılabilir.

### Llama (Meta AI)
Llama (Large Language Model Meta AI), Meta tarafından yayımlanan açık ağırlıklı bir
model ailesidir. Llama 2 (2023), 7 milyardan 70 milyara uzanan parametre boyutlarıyla
araştırma ve ticari kullanım için yayımlanmıştır. Llama 3 (2024), 8 milyardan 70
milyara uzanan (ve daha sonra 400 milyarın üzerine çıkan) modellerle performansı
önemli ölçüde artırmıştır. Ağırlıklar kamuya açık biçimde indirilebildiği için,
Llama modelleri ince ayarlanmış geniş bir varyant ekosisteminin (Mistral, Alpaca,
Vicuna vb.) temelini oluşturur ve yerel/özel yapay zekâ dağıtımlarında yaygın olarak
kullanılır.

### Mistral
Mistral AI, açık ve kapalı kaynaklı LLM'ler geliştiren Fransız bir yapay zekâ
şirketidir. Mistral 7B (2023), kayan pencere dikkati ve grouped-query attention gibi
verimli tekniklerle 7 milyar parametreli bir modelin çok daha büyük modellerin
performansına ulaşabileceğini göstermiştir. Mixtral 8x7B (2024), mixture-of-experts
bir modeldir; her belirteci 8 uzman ağdan oluşan bir alt kümeye yönlendirerek
GPT-3.5 düzeyinde performansı daha düşük hesaplama maliyetiyle sunar. Mistral'ın
modelleri tamamen açık ağırlıklıdır ve yerelde çalıştırılabilir.

---

## GPU Donanımı ve Ekran Kartları

### GPU (Graphics Processing Unit)
GPU, büyük ölçüde paralel hesaplama için tasarlanmış bir işlemcidir. Başlangıçta
3B grafik işleme için geliştirilmiş olsa da, binlerce küçük çekirdek sayesinde aynı
anda binlerce kayan nokta işlemi yapabildiği için yapay zekâ/makine öğrenmesi
eğitimi ve çıkarımında vazgeçilmez hâle gelmiştir. Yapay zekâ için başlıca iki GPU
üreticisi NVIDIA ve AMD'dir.

### NVIDIA GeForce RTX Serisi
RTX (Ray Tracing Texel eXtreme) serisi, NVIDIA'nın tüketici GPU ailesidir. RTX 30xx
(Ampere, 2020) ve RTX 40xx (Ada Lovelace, 2022) nesilleri, yapay zekâ işlemlerini
hızlandırmak için özel Tensor çekirdekleri içerir. Yapay zekâ modellerini yerelde
çalıştırırken VRAM (ekran belleği) kritik önemdedir; 8 GB'lık bir GPU, 4 bit
kuantizasyonla 7 milyar parametreli modelleri çalıştırabilir; 24 GB'lık bir GPU ise
4 bit kuantizasyonla 70 milyar parametreli modelleri kaldırabilir.

### NVIDIA A Serisi ve H Serisi (Veri Merkezi)
A100 (Ampere, 2020) ve H100 (Hopper, 2022), NVIDIA'nın profesyonel yapay zekâ
hızlandırıcılarıdır. H100, 80 GB'a kadar HBM3 belleğe sahiptir ve günümüzde büyük
ölçekli LLM eğitimlerinin çoğunun arkasındaki standart donanımdır. Bu GPU'ların
birim maliyeti 25.000 ila 40.000 ABD doları arasındadır, ancak tüketici sınıfı RTX
kartlara göre 10 ila 30 kat daha yüksek yapay zekâ iş hacmi sunarlar.

### AMD Radeon RX Serisi
AMD'nin tüketici GPU serisidir. RX 7900 XTX (2022), 24 GB VRAM'e sahiptir ve ROCm
(AMD'nin GPU hesaplama yığını) aracılığıyla yerel LLM'leri çalıştırabilir. Yapay
zekâ çerçevelerinde AMD GPU'lara verilen destek, NVIDIA'ya kıyasla genelde daha
sınırlıdır; ancak giderek iyileşmektedir.

### Intel Arc
Intel Arc, Intel'in 2022'den itibaren piyasaya sürdüğü ayrık GPU ürün ailesidir.
Arc GPU'lar XeSS'i (Intel'in süper örnekleme teknolojisi) destekler ve OpenVINO ile
IPEX-LLM çerçeveleri üzerinden yapay zekâ çıkarım görevleri için sınırlı ama büyüyen
bir desteğe sahiptir.

### ARK Intel (ark.intel.com)
ARK, Intel'in ark.intel.com adresindeki resmî ürün özellikleri veritabanıdır. Her
Intel CPU, GPU, FPGA ve NUC ürünü için çekirdek sayıları, saat hızları, TDP,
desteklenen bellek türleri ve komut kümesi özellikleri dâhil ayrıntılı teknik
özellikler sunar. "Özellikler için ARK'a bak" dendiğinde kastedilen, yetkin donanım
bilgisi için bu veritabanını ziyaret etmektir.

---

## Yapay Zekâ Performans Kıyaslamaları

### MMLU (Massive Multitask Language Understanding)
MMLU, matematik, tarih, hukuk, tıp ve bilgisayar bilimi dâhil 57 akademik alandaki
LLM bilgisini ölçen bir kıyaslamadır. Gerçek üniversite düzeyi sınavlardan alınmış
çoktan seçmeli sorulardan oluşur. %70'lik bir skor yaklaşık lisans öğrencisi
düzeyine karşılık gelir; GPT-4 ve Claude 3 ise %86'nın üzerinde puan alır.
Phi-3-mini, küçük boyutuna rağmen yaklaşık %70 puan alır.

### HumanEval
HumanEval, OpenAI'ın kod üretimi için geliştirdiği kıyaslamadır. Otomatik test
vakalarıyla değerlendirilen 164 Python programlama probleminden oluşur. Modeller,
pass@k metriğiyle ölçülür; bu, üretilen k çözümden en az birinin tüm testleri geçme
olasılığıdır. GPT-4 yaklaşık %87 (pass@1) skor alır; iyi ayarlanmış 7 milyar
parametreli bir model yaklaşık %50–60 aralığına ulaşabilir.

### HellaSwag
HellaSwag, sağduyu temelli akıl yürütme kıyaslamasıdır. Modelle, sıradan bir
etkinliği anlatan bir cümle verilir ve dört seçenek arasından en olası devamı
seçmesi beklenir. Yanlış seçenekler, makul görünecek ama ince biçimde hatalı olacak
şekilde özel olarak tasarlanmıştır. Bu kıyaslama, modelin fiziksel ve sosyal
durumları yerleşik bir anlayışla kavrayıp kavramadığını ölçer.

### ARC (AI2 Reasoning Challenge)
ARC, Allen Institute for AI tarafından hazırlanmış bir kıyaslamadır. İlköğretim
seviyesi fen sorularından oluşur ve "Easy" ile "Challenge" olarak iki kümeye ayrılır.
Challenge kümesi, geri getirme tabanlı yöntemlerin ve basit istatistiksel modellerin
zorlandığı, çok adımlı akıl yürütme gerektiren sorular içerir.

---

## Temel Yapay Zekâ / Makine Öğrenmesi Kavramları

### RAG (Retrieval-Augmented Generation)
RAG, bir bilgi getirme sistemiyle (genellikle bir vektör veritabanı) bir dil
modelini birleştiren tekniktir. Modelin yalnızca parametrik bilgisine dayanmak
yerine, RAG önce harici bir bilgi tabanından ilgili belgeleri getirir ve ardından
bunları modelin bağlamına ekler. Bu sayede model, yeniden eğitilmeden güncel veya
alana özgü soruları yanıtlayabilir. Potato.ai bir RAG türü kullanır; kendi bilgi
tabanından içerik getirir ve yanıt üretmeden önce sonuçları bağlama ekler.

### Fine-tuning
Fine-tuning, önceden eğitilmiş bir modeli daha küçük ve alana özgü bir veri kümesi
üzerinde eğitmeye devam etme sürecidir. Bu işlem, modelin ağırlıklarını belirli bir
göreve veya alana uyarlar. Örneğin temel bir LLM, tıbbi kayıtlara göre ince ayarlanıp
tıbbi soru-cevap asistanına dönüştürülebilir. Fine-tuning hesaplama açısından
maliyetlidir, ancak sıfırdan eğitimden çok daha ucuzdur.

### Quantisation
Quantisation, model ağırlıklarının sayısal hassasiyetini düşürür (örneğin 32 bit
floating-point değerden 4 bit tamsayıya). Bu işlem bellek ayak izini dramatik
biçimde azaltır; 16 bit hassasiyette 7 milyar parametreli bir model yaklaşık 14 GB
VRAM gerektirirken, aynı model 4 bit (GGUF biçiminde) yaklaşık 4 GB gerektirir.
Quantisation genelde küçük ama kabul edilebilir bir doğruluk kaybına yol açar ve
büyük modellerin tüketici donanımında hatta mobil cihazlarda çalışmasını mümkün
kılan başlıca tekniktir.

### Bağlam Penceresi
Bağlam penceresi, bir modelin aynı anda işleyebileceği azami belirteç sayısıdır;
buna hem istem hem de üretilen yanıt dâhildir. GPT-3.5'in bağlam penceresi 4.096
belirteçti; GPT-4 Turbo ile Claude 3, 128.000 belirteci destekler; Gemini 1.5 Pro
ise 1.000.000 belirteci destekler. Daha geniş bir bağlam penceresi, modelin bir
konuşmanın veya belgenin daha büyük bölümünü aynı anda "görebilmesini" sağlar ve
uzun etkileşimlerde tutarlılığı artırır.

### RLHF (Reinforcement Learning from Human Feedback)
RLHF, yalnızca bir sonraki belirteci tahmin eden temel bir dil modelini, yönergeleri
izleyen ve faydalı davranan bir asistana dönüştüren eğitim tekniğidir. İnsan
puanlayıcılar model çıktılarının kalitesini değerlendirir, bu tercihler üzerinden bir
ödül modeli eğitilir ve dil modeli daha sonra reinforcement learning ile bu ödül
modeline göre optimize edilir. ChatGPT, Claude ve Gemini; RLHF'nin ya da benzer
hizalama tekniklerinin (ör. Constitutional AI, Direct Preference Optimisation)
çeşitli sürümlerini kullanır.

### Transformer Mimarisi
Transformer, tüm modern LLM'lerin temelindeki sinir ağı mimarisidir. Vaswani ve
arkadaşlarının 2017 tarihli "Attention Is All You Need" makalesiyle tanıtılmıştır ve
belirteçleri sıralı biçimde değil, self-attention mekanizmalarıyla paralel olarak
işler. Yalnızca encoder kullanan Transformer'lar (BERT) anlama görevlerinde;
yalnızca decoder kullanan Transformer'lar (GPT, Llama, Mistral) üretim görevlerinde;
encoder-decoder Transformer'lar (T5, BART) ise çeviri ve özetleme görevlerinde
kullanılır.

### Embedding'ler ve Vektör Veritabanları
Embedding'ler, bir sinir ağı tarafından üretilen yoğun sayısal metin (veya görsel)
temsilleridir. Anlamsal olarak benzer metinlerin embedding'leri vektör uzayında
birbirine yakın olur. Vektör veritabanları (ChromaDB, Pinecone, Weaviate, Qdrant),
bu embedding'leri saklar ve hızlı yaklaşık en yakın komşu aramasını destekler.
RAG sistemlerinin depolama omurgasını bunlar oluşturur; Potato.ai'ın cold-memory
katmanı da buna dâhildir.
