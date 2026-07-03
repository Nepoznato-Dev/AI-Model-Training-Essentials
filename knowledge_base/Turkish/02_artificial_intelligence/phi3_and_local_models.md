# Phi-3-mini ve Yerel Yapay Zekâ Model Ekosistemi

Microsoft'un Phi-3-mini modeline; tasarım felsefesine, mimari tercihlerine ve performans özelliklerine yönelik bir inceleme — ve başarısının bize etkili, verimli AI sistemleri kurma konusunda ne öğrettiği.

---

## Phi-3-mini'ye Genel Bakış

Phi-3-mini, Microsoft Research tarafından geliştirilen ve Nisan 2024'te yayımlanan küçük bir dil modelidir (SLM). Ayırt edici özellikleri şunlardır:

- **3.8 milyar parametre** — Meta'nın Llama 3 8B modelinden yaklaşık 6× daha küçüktür
- **Ders kitabı kalitesinde eğitim verisi** — beklenenden yüksek performansının anahtarıdır
- **İki bağlam varyantı**: 4,096 token (standart) ve 128,000 token (uzun bağlam)
- **Tüketici donanımında çalışır** — 4-bit kuantizasyon ile 8GB VRAM'e rahatça sığar
- **Mobil dağıtım** — Microsoft, Phi-3-mini'nin iPhone 14 üzerinde çalıştığını gösterdi
- **Açık ağırlıklar** — yerel kullanım için Hugging Face üzerinde mevcuttur

Küçük boyutuna rağmen Phi-3-mini, akıl yürütme ve bilgi odaklı çeşitli kıyaslama testlerinde kendisinden 3–5× daha büyük modellerle eşleşir ya da onları geride bırakır.

---

## "Ders Kitabı Kalitesi" Eğitim Felsefesi

Phi serisinin merkezindeki içgörü şudur: **veri kalitesi, veri miktarından daha önemlidir**. Geleneksel LLM eğitimi, web'den kazınmış internet ölçeğinde metin kullanır — yüz milyarlarca token'lık çeşitli ve gürültülü içerik.

Phi ekibi şu soruyu sordu: Ham web metni yerine, ders kitaplarında bulunan yoğun, iyi açıklanmış ve yapılandırılmış içerikle eğitim yapılsaydı ne olurdu?

### Phi-1 (2023): Kavramın Kanıtı
İlk Phi-1 makalesi ("Textbooks Are All You Need"), sentetik olarak üretilmiş "ders kitabı kalitesinde" Python kodu ve alıştırmalar üzerinde 1.3B'lik bir modeli eğitti. Model, HumanEval'de (Python kod üretimi) kendi boyutunun 10× üzerindeki modelleri geçti. Bu, özenle seçilmiş ve yapılandırılmış verinin daha küçük model boyutunu telafi edebileceğine dair güçlü bir işaretti.

### Phi-1.5 ve Phi-2
Sonraki modeller, yaklaşımı genel akıl yürütmeye genişletti ve şu karışımı kullandı:
- Eğitsel değeri için seçilmiş yüksek kaliteli web metni
- Ders kitabı ve alıştırma tarzında GPT-4 tarafından üretilmiş sentetik veri
- Yinelenen kayıtları ayıklanmış ve filtrelenmiş, özenle seçilmiş veri kümeleri

### Phi-3-mini: Tarifin Ölçeklenmiş Hâli
Phi-3-mini eğitim için yaklaşık 3.3 trilyon token kullanır — mutlak ölçekte büyük olsa da, Llama 3'ün kullandığı 15T token'dan çok daha küçüktür. Asıl ayrıştırıcı unsur, yalnızca yüksek kaliteli içeriği seçen filtreleme ve kürasyon sürecidir.

Eğitim veri kümesi şunları içerir:
1. **Yoğun biçimde filtrelenmiş web verisi** — yalnızca eğitsel veya açıklayıcı içeriğe sahip sayfalar, birden çok kalite sinyaline göre filtrelenir
2. **Sentetik ders kitabı verisi** — GPT-4 tarafından STEM, beşerî bilimler, kodlama ve akıl yürütme alanlarında üretilmiş kavram açıklamaları
3. **Sentetik alıştırmalar** — adım adım akıl yürütme içeren soru-cevap çiftleri (chain-of-thought tarzı)
4. **Kod verisi** — özenle seçilmiş programlama örnekleri ve dokümantasyon

---

## Mimari Ayrıntılar

Phi-3-mini, birkaç verimlilik iyileştirmesiyle birlikte standart, yalnızca kod çözücüden oluşan Transformer mimarisini kullanır:

### Gruplanmış Sorgu Dikkati (GQA)
Standart multi-head attention (MHA), her attention head için bir key-value (KV) head kullanır. GQA, birden fazla attention head'in aynı KV head'leri paylaşmasını sağlayarak KV cache boyutunu — yani çıkarım sırasında bağlamı saklamak için gereken belleği — azaltır. Bu da özellikle 128k uzun bağlam varyantında, aksi hâlde çok büyük KV cache'ler gerekeceği için, Phi-3-mini'yi çıkarım sırasında belirgin biçimde daha hızlı kılar.

### Mimari Değerler
- Katmanlar: 32
- Dikkat başlıkları: 32 (sorgu), 8 (anahtar-değer, gruplanmış)
- Gizli boyut: 3,072
- Feed-forward boyutu: 8,192
- Sözlük boyutu: 32,064 (Llama tokenlaştırıcısı ile aynı)
- Aktivasyon fonksiyonu: SiLU (Sigmoid Linear Unit)

### SFT ve RLHF Hizalaması
Tüm dağıtılmış sohbet modelleri gibi Phi-3-mini de şu aşamalardan geçer:
1. Talimat izleme örnekleri üzerinde **Supervised Fine-Tuning (SFT)**
2. İnsan tercih verileri üzerinde eğitilmiş bir ödül modeline karşı **Proximal Policy Optimisation (PPO)**

Bu süreç, sonraki token'ı tahmin eden temel modeli; talimatları izleyen, faydalı bir asistana dönüştürür.

---

## Karşılaştırma Testi Performansı

Phi-3-mini, parametre sayısına göre dikkat çekici derecede iyi performans gösterir:

| Test | Phi-3-mini (3.8B) | Llama 3 8B | Mistral 7B | GPT-3.5 |
|-----------|-------------------|------------|------------|---------|
| MMLU      | ~69%              | ~66%       | ~62%       | ~70%    |
| HumanEval | ~56%              | ~60%       | ~30%       | ~73%    |
| GSM8K     | ~82%              | ~79%       | ~35%       | ~78%    |
| ARC Challenge | ~84%          | ~82%       | ~60%       | ~79%    |

**Temel gözlemler:**
- Phi-3-mini, MMLU'da 50× daha az parametreyle GPT-3.5 seviyesine ulaşır
- Daha küçük olmasına rağmen listelenen her kıyaslama testinde Mistral 7B'yi geçer
- 2× daha küçük olmasına karşın (3.8B vs 8B), Llama 3 8B ile neredeyse aynı düzeydedir

*Kaynak: Microsoft Phi-3 Technical Report (Nisan 2024)*

---

## Küçük Modeller Neden Büyükleri Geçebilir?

Phi deneyimi birkaç önemli ders gösteriyor:

### 1. Eğitim Verisinin Dağılımı En Belirleyici Etkendir
Bir modelin kıyaslama testlerinde aldığı skorlar, ham parametre sayısından çok eğitildiği veri türünü yansıtır. Yüksek kaliteli akıl yürütme örnekleri üzerinde eğitilmiş küçük bir model, akıl yürütme testlerinde gürültülü web metniyle eğitilmiş büyük bir modeli geçecektir.

### 2. Bilgi Yoğunluğu ve Bilgi Hacmi
3.8B'lik bir model, ağırlıklarında 70B'lik bir model kadar çok olgusal bilgiyi depolayamaz. Ancak kapasitesini olgu ezberlemek yerine yapılandırılmış akıl yürütme için kullanacak şekilde eğitilmişse yine de iyi akıl yürütebilir. GSM8K gibi kıyaslama testleri çok adımlı aritmetik akıl yürütmeyi ölçer — ve bu beceri verimli biçimde öğretilebilir.

### 3. Maliyet-Verimlilik Eğrisi
Birçok gerçek dünya görevi için (soru-cevap, kodlama yardımı, özetleme) Phi-3-mini düzeyinde yetenek yeterlidir. 3.8B'lik bir modeli yerel olarak çalıştırmak:
- **Ücretsizdir** — API maliyeti yoktur
- **Özeldir** — veri cihazdan çıkmaz
- **Hızlıdır** — modern bir dizüstü bilgisayar GPU'sunda gerçek zamanlı token üretir
- **Her yere dağıtılabilir** — akıllı telefonlar, uç cihazlar, air-gapped sistemler

### 4. Güç Çarpanı Olarak Sentetik Veri Üretimi
Büyük bir öğretmen modelin (GPT-4), küçük bir öğrenci model için yüksek kaliteli eğitim verisi üretmesi bir bilgi damıtımı biçimidir. Bu "en iyiden öğren, en ekonomik olanı dağıt" yaklaşımı sektörde giderek daha yaygın hâle geliyor.

---

## Potato.ai için Çıkarımlar

Phi-3 tasarım felsefesi, Potato.ai'nin KB merkezli yaklaşımıyla yakından örtüşür:

**KB kaynaklarında nicelikten çok nitelik**: Nasıl ki Phi-3-mini daha iyi veriler sayesinde daha büyük modelleri geride bırakıyorsa, Potato.ai'nin bilgi tabanı da büyük miktarda gürültülü metinden çok yoğun ve iyi yapılandırılmış kaynak belgelerden daha fazla fayda görür.

**Akıl yürütme yapısına odaklanma**: Phi-3, adım adım akıl yürütmeyi gösteren örneklerle eğitilmiştir. Potato.ai de KB kaynaklarının ham olgular yerine açıklamalar içermesini sağlayarak benzer şekilde iyileşebilir.

**Verimli KB kapsamı**: Phi-3-mini'nin 3.8B parametresi, insan bilgisinin büyük bir bölümünü verimli biçimde kapsamak zorundadır. Potato.ai'nin başlangıçta eklenen KB kaynakları da benzer şekilde, kelime başına yaygın sorguların mümkün olan en geniş kapsamını hedeflemelidir.

**Yerel öncelikli yaklaşım uygulanabilirdir**: Phi-3-mini'nin başarısı, tamamen yerel bir AI'nin birçok görevde bulut tabanlı modellerle eşleşebileceğini gösterir. Bu da Potato.ai'nin harici API çağrıları olmadan tamamen cihaz üzerinde çalışan mimarisini doğrular.

---

## Diğer Dikkat Çekici Yerel Modeller (2024)

### Llama 3 (Meta, 2024)
- 8B ve 70B varyantları (ve yakında 400B+)
- Her boyutta sınıfının en iyisi açık ağırlıklı modeller
- 8,192 token bağlam penceresi (genişletilebilir)
- Ticari kullanım için Apache 2.0 lisansı

### Mistral / Mixtral
- **Mistral 7B**: Boyutunun ötesinde performans gösterir, sliding-window attention kullanır
- **Mixtral 8x7B**: Mixture of experts, yerelde GPT-3.5 düzeyinde performans
- **Mistral-Nemo 12B**: Daha büyük, sınıfı için son teknoloji

### Gemma 2 (Google, 2024)
- Google'dan 2B ve 9B varyantları
- Boyutlarına göre güçlü akıl yürütme
- Yerel kullanım için izin verici bir lisansla sunulur

### Qwen 2.5 (Alibaba, 2024)
- 0.5B ile 72B arasında varyantlar
- Güçlü çok dilli yetenek
- Özellikle küçük boyutlarda kodlama görevlerinde iyidir

---

## 2024–2025'te Yerel Yapay Zekâ Model Pazarı

2024'te yerel ve bulut modelleri arasındaki fark dramatik biçimde daraldı:

- Laptop üzerinde çalışan ücretsiz, 4-bit kuantize bir Phi-3-mini; eğitimi milyonlarca dolara mal olmuş GPT-3.5'i birçok kıyaslama testinde geride bırakıyor
- Tüketici sınıfı 24GB GPU'lar (NVIDIA RTX 3090, 4090), 70B modelleri 4-bit çalıştırabiliyor
- Apple Silicon M serisi Mac'ler, birleşik bellek mimarileri nedeniyle yerel yapay zekâ için popüler; 64GB belleğe sahip bir M3 Max, 70B modelleri akıcı biçimde çalıştırabiliyor
- Ollama, LM Studio ve llama.cpp, yerel model dağıtımını teknik olmayan kullanıcılar için erişilebilir hâle getirdi

Bunun anlamı şu: Mahremiyetin kritik olduğu uygulamalar, uç dağıtım veya maliyet duyarlı senaryolar için yerel modeller artık çok çeşitli görevlerde bulut API'lerine karşı inandırıcı bir alternatiftir.
