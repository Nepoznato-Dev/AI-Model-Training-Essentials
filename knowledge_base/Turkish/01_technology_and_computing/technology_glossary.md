# Teknoloji Sözlüğü

Modern AI ve bilişim dünyasındaki AI modellerini, donanımı, benchmark'ları ve temel kavramları kapsayan bir başvuru sözlüğü.

---

## AI Dil Modelleri ve Asistanlar

### ChatGPT
ChatGPT, OpenAI tarafından geliştirilen ve ilk kez Kasım 2022'de yayımlanan bir AI sohbet botudur. GPT serisindeki large language model'ler (LLM'ler) tarafından desteklenir. ChatGPT, piyasaya çıktıktan sonraki iki ay içinde 100 milyon kullanıcıya ulaşarak tarihin en hızlı büyüyen tüketici AI ürünlerinden biri olmuştur. Metin tabanlı konuşma, kod üretimi, özetleme ve yaratıcı yazma destekler. Ücretli katmanlar GPT-4 ve GPT-4o gibi daha güçlü modellere erişim sunar.

### GPT (Generative Pre-trained Transformer)
GPT, OpenAI tarafından oluşturulan bir large language model ailesidir. Mimari, çok büyük metin külliyatları üzerinde next-token prediction hedefiyle eğitilmiş yalnızca decoder içeren bir Transformer kullanır. Öne çıkan sürümler arasında GPT-2 (2019, 1.5B parametre, "too dangerous to release" söylemiyle dikkat çekti), GPT-3 (2020, 175B parametre, API üzerinden yaygın kullanım), GPT-3.5 (ilk ChatGPT'nin omurgası) ve GPT-4 (2023, multimodal, birçok benchmark'ta insan uzman düzeyine yakın performans) yer alır.

### Claude
Claude, Anthropic tarafından geliştirilen bir AI asistanıdır. Adını bilgi kuramının kurucusu Claude Shannon'dan alır. Anthropic, eski OpenAI araştırmacıları tarafından kurulmuştur ve modelleri bir ilke setini izleyecek şekilde eğiterek daha güvenli hale getirmeyi amaçlayan "constitutional AI" yaklaşımına odaklanır. Claude modelleri (Claude 1, 2, 3 Haiku / Sonnet / Opus), uzun context window'ları (200.000 token'a kadar), incelikli muhakeme yeteneği ve temel LLM'lere kıyasla daha düşük zararlı çıktı üretmesiyle bilinir.

### Gemini
Gemini, Google DeepMind'ın Aralık 2023'te duyurduğu multimodal AI model ailesidir. Gemini, sonradan fine-tuning ile modality eklenen önceki modellerden farklı olarak, metin, görsel, ses ve videoyu aynı anda işlemek üzere baştan itibaren multimodal biçimde eğitilmiştir. Sürümler arasında Gemini Nano (on-device), Gemini Flash (hızlı, maliyet etkin) ve Gemini Ultra (en yüksek yetenek) bulunur. Gemini, Google'ın AI sohbet botu Bard'a (sonradan Gemini olarak yeniden adlandırıldı) ve Google Search AI Overviews'e güç verir.

### Phi-3-mini
Phi-3-mini, Microsoft tarafından geliştirilen ve 3.8B parametreye sahip küçük bir language model'dir (SLM). Nisan 2024'te yayımlanmıştır. Çoğu büyük modelin aksine Phi-3-mini, Microsoft Research öncülüğünde geliştirilen ve ham hacim yerine veri kalitesine öncelik veren dikkatle seçilmiş "textbook-quality" bir veri kümesi üzerinde eğitilmiştir. GPT-4 veya Claude 3 Opus'tan çok daha küçük olmasına rağmen MMLU ve HumanEval gibi muhakeme benchmark'larında kendisinden birkaç kat büyük modelleri yakalar veya geçer. Temel varyantında 4k token, long-context varyantında ise 128k token context window sunar. Phi-3-mini, tek bir tüketici GPU'sunda hatta yeterli RAM'e sahip modern bir akıllı telefonda on-device çalışabilir.

### Llama (Meta AI)
Llama (Large Language Model Meta AI), Meta tarafından yayımlanan open-weights model ailesidir. Llama 2 (2023), 7B ile 70B parametre arasında değişen boyutlarıyla araştırma ve ticari kullanım için sunuldu. Llama 3 (2024), 8B ile 70B (ve daha sonra 400B+) aralığındaki modellerle performansı önemli ölçüde artırdı. Ağırlıklar herkes tarafından indirilebildiği için Llama modelleri, fine-tuning ile oluşturulan geniş bir varyant ekosisteminin (Mistral, Alpaca, Vicuna vb.) temelini oluşturur ve yerel/özel AI dağıtımlarında yaygın olarak kullanılır.

### Mistral
Mistral AI, open ve proprietary LLM'ler geliştiren Fransız bir AI şirketidir. Mistral 7B (2023), sliding window attention ve grouped-query attention gibi verimli tekniklerle 7B parametreli bir modelin çok daha büyük modellerin performansını yakalayabileceğini gösterdi. Mixtral 8x7B (2024) ise mixture-of-experts modelidir — her token'ı 8 uzman ağdan oluşan bir alt kümeye yönlendirir ve hesaplama maliyetini düşürürken GPT-3.5 düzeyinde performans sağlar. Mistral'ın modelleri tamamen open-weight'tir ve yerel olarak çalıştırılabilir.

---

## GPU Donanımı ve Ekran Kartları

### GPU (Graphics Processing Unit)
A GPU, büyük ölçüde paralel hesaplama için tasarlanmış bir işlemcidir. Başlangıçta 3D grafikleri işlemek için geliştirilmiş olsa da, binlerce küçük çekirdek kullanarak aynı anda binlerce floating-point işlemi yapabildiğinden AI/ML eğitimi ve inference için vazgeçilmez hale gelmiştir. AI alanındaki iki ana GPU üreticisi NVIDIA ve AMD'dir.

### NVIDIA GeForce RTX Series
RTX (Ray Tracing Texel eXtreme) serisi, NVIDIA'nın tüketici GPU ürün hattıdır. RTX 30xx (Ampere, 2020) ve RTX 40xx (Ada Lovelace, 2022) nesilleri, AI işlemlerini hızlandırmak için özel Tensor Cores içerir. AI modellerini yerelde çalıştırmak için VRAM (video RAM) kritik önemdedir — 8GB bir GPU, 4-bit quantisation ile 7B parametreli modelleri; 24GB bir GPU ise 4-bit ile 70B modelleri çalıştırabilir.

### NVIDIA A-Series ve H-Series (Data Centre)
A100 (Ampere, 2020) ve H100 (Hopper, 2022), NVIDIA'nın profesyonel AI hızlandırıcılarıdır. H100, 80GB'a kadar HBM3 bellek sunar ve günümüzde büyük ölçekli LLM eğitimlerinin çoğunun arkasındaki standart donanımdır. Bu GPU'lar adet başına 25.000–40.000 dolar aralığında olsa da, tüketici sınıfı RTX kartlarına göre 10–30× daha yüksek AI throughput sağlar.

### AMD Radeon RX Series
AMD'nin tüketici GPU ürün hattıdır. RX 7900 XTX (2022), 24GB VRAM'e sahiptir ve ROCm (AMD'nin GPU compute yığını) üzerinden yerel LLM'leri çalıştırabilir. AMD GPU'lar, AI framework'leri açısından genelde NVIDIA kadar iyi desteklenmez, ancak destek giderek iyileşmektedir.

### Intel Arc
Intel Arc, Intel'in 2022'den itibaren piyasaya sürülen ayrık GPU ürün serisidir. Arc GPU'lar XeSS'i (Intel'in super-sampling teknolojisi) destekler ve OpenVINO ile IPEX-LLM framework'leri üzerinden AI inference görevleri için sınırlı ama büyüyen destek sunar.

### ARK Intel (ark.intel.com)
ARK, Intel'in ark.intel.com adresindeki resmî ürün teknik özellikleri veritabanıdır. Her Intel CPU, GPU, FPGA ve NUC ürünü için çekirdek sayısı, saat hızları, TDP, desteklenen bellek türleri ve instruction-set özellikleri dâhil ayrıntılı teknik bilgiler sağlar. "Özellikler için ARK'a bak" ifadesi, yetkili donanım bilgisi için bu veritabanına başvurmak anlamına gelir.

---

## AI Performans Benchmark'ları

### MMLU (Massive Multitask Language Understanding)
MMLU, matematik, tarih, hukuk, tıp ve bilgisayar bilimi dâhil 57 akademik konuda LLM bilgisini ölçen bir benchmark'tır. Gerçek üniversite düzeyi sınavlardan alınmış çoktan seçmeli sorulardan oluşur. %70 civarı puan, kabaca lisans öğrencisi düzeyine karşılık gelir; GPT-4 ve Claude 3 %86'nın üzerinde skor alır. Phi-3-mini ise küçük boyutuna rağmen yaklaşık %70 skor elde eder.

### HumanEval
HumanEval, OpenAI'ın kod üretimi benchmark'ıdır. Otomatik test vakalarına sahip 164 Python programlama probleminden oluşur. Modeller, üretilen k çözümden en az birinin tüm testleri geçme olasılığını ölçen pass@k metriğiyle değerlendirilir. GPT-4 yaklaşık %87 (pass@1) skor alır; iyi ayarlanmış 7B'lik bir model ise yaklaşık %50–60 seviyesine çıkabilir.

### HellaSwag
HellaSwag, sağduyu muhakemesini ölçen bir benchmark'tır. Modeller, sıradan bir etkinliği betimleyen bir cümle alır ve dört seçenek arasından en olası devamı seçer. Yanlış seçenekler özellikle makul ama ince biçimde hatalı olacak şekilde tasarlanmıştır. Bu benchmark, modelin fiziksel ve sosyal durumlara dair temellendirilmiş bir anlayışa sahip olup olmadığını ölçer.

### ARC (AI2 Reasoning Challenge)
ARC, Allen Institute for AI tarafından geliştirilen bir benchmark'tır. İlköğretim düzeyinde fen sorularından oluşur ve "Easy" ile "Challenge" kümelerine ayrılır. Challenge kümesindeki sorular, retrieval tabanlı yöntemlerin ve basit istatistiksel modellerin zorlandığı, çok adımlı muhakeme gerektiren sorulardır.

---

## Temel AI/ML Kavramları

### RAG (Retrieval-Augmented Generation)
RAG, bir retrieval sistemiyle (genellikle bir vector database) bir language model'i birleştiren tekniktir. Modelin yalnızca parametrelerine gömülü bilgiye dayanması yerine, RAG önce harici bir knowledge base'den ilgili belgeleri getirir ve ardından bunları modelin context'ine ekler. Bu sayede model, yeniden eğitilmeye gerek kalmadan güncel veya alana özgü bilgiler hakkında yanıt verebilir. Potato.ai, RAG'in bir türünü kullanır — KB'den içerik getirir ve yanıt oluşturmadan önce sonuçları context'e ekler.

### Fine-tuning
Fine-tuning, önceden eğitilmiş bir modeli daha küçük, alana özgü bir veri kümesi üzerinde eğitmeye devam etme sürecidir. Bu, model ağırlıklarını belirli bir görev veya alana uyarlar. Örneğin bir temel LLM, tıbbi kayıtlarda fine-tuning yapılarak tıbbi soru-cevap asistanına dönüştürülebilir. Fine-tuning hesaplama açısından maliyetlidir, ancak sıfırdan eğitimden çok daha ucuzdur.

### Quantisation
Quantisation, model ağırlıklarının sayısal hassasiyetini düşürür (ör. 32-bit float'tan 4-bit integer'a). Bu, bellek ayak izini dramatik biçimde azaltır — 16-bit hassasiyette 7B'lik bir model yaklaşık 14GB VRAM gerektirirken, aynı model 4-bit'te (GGUF formatı) yaklaşık 4GB gerektirir. Quantisation genellikle küçük ama kabul edilebilir bir doğruluk kaybına yol açar ve büyük modellerin tüketici donanımında hatta mobil cihazlarda çalışmasını sağlayan başlıca tekniktir.

### Context Window
Context window, bir modelin aynı anda işleyebileceği azami token sayısıdır; buna hem prompt hem de üretilen yanıt dâhildir. GPT-3.5'in 4.096 token'lık bir penceresi vardı; GPT-4 Turbo ve Claude 3, 128.000 token destekler; Gemini 1.5 Pro ise 1.000.000 token destekler. Daha büyük bir context window, modelin aynı anda daha fazla konuşmayı veya belgeyi "görebilmesini" sağlar ve uzun etkileşimlerde tutarlılığı artırır.

### RLHF (Reinforcement Learning from Human Feedback)
RLHF, yalnızca sonraki token'ı tahmin eden temel bir language model'i, yönergeleri izleyen ve yardımcı davranan bir asistana dönüştüren eğitim tekniğidir. İnsan değerlendiriciler model çıktılarının puanını verir, bu tercihler üzerinden bir reward model eğitilir ve ardından language model, reinforcement learning kullanılarak bu reward model'e göre optimize edilir. ChatGPT, Claude ve Gemini; RLHF'in veya benzer hizalama tekniklerinin (ör. Constitutional AI, Direct Preference Optimisation) varyantlarını kullanır.

### Transformer Architecture
Transformer, tüm modern LLM'lerin temelindeki neural network mimarisidir. Vaswani ve arkadaşlarının 2017 tarihli "Attention Is All You Need" makalesiyle tanıtılmıştır ve token'ları sıralı biçimde değil paralel olarak işlemek için self-attention mekanizmaları kullanır. Yalnızca encoder kullanan Transformer'lar (BERT) anlama görevlerinde; yalnızca decoder kullanan Transformer'lar (GPT, Llama, Mistral) üretim görevlerinde; encoder-decoder Transformer'lar (T5, BART) ise çeviri ve özetleme görevlerinde kullanılır.

### Embeddings ve Vector Databases
Embedding'ler, bir neural network tarafından üretilen yoğun sayısal metin (veya görsel) temsilleridir. Anlamsal olarak benzer metinlerin embedding'leri vector space içinde birbirine yakın olur. Vector database'ler (ChromaDB, Pinecone, Weaviate, Qdrant) bu embedding'leri depolar ve hızlı approximate nearest-neighbour aramasını destekler. Bunlar, Potato.ai'ın cold-memory katmanı dâhil olmak üzere RAG sistemlerinin depolama omurgasını oluşturur.
