---
# Metadata
title: "Local AI Architecture"
description: "Local AI deployment architectures"
category: "AI and Machine Learning"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "AI Model Training Team"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.0"
    date: "2026-08-05"
    author: "AI Model Training Team"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-05"
review_date: "2027-02-05"
reviewed_by: "AI & Machine Learning Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [local, ai, architecture, ai-and-machine-learning]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "10 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Yerel Yapay Zeka Mimarisi
Büyük dil modellerini tamamen cihaz üzerinde çalıştırmaya yönelik pratik bir kılavuz - donanım hususları, çıkarım motorları, bellek optimizasyonu ve uç dağıtım için sistem tasarımı.
---

## Yapay Zekayı Neden Yerel Olarak Çalıştırmalısınız?
- **Gizlilik**: Cihazdan hiçbir veri çıkmaz.
- **Maliyet**: Jeton başına API ücreti yoktur.
- **Gecikme**: Tahmin edilebilir, ağdan bağımsız çıkarım.
- **Çevrimdışı kullanılabilirlik**: İnternet olmadan çalışır.
- **Kontrol**: Model sürümü, özelleştirme ve ince ayar üzerinde tam kontrol.
---

## Donanım Gereksinimleri
### GPU Belleği (VRAM)
En kritik kaynak. Bellekteki model boyutu ≈ **parametreler × parametre başına bayt**.
| Hassasiyet | Parametre başına bayt | 3.8B modeli | 7B modeli | 13B modeli | 70B modeli |
|----------||----------|---------------|----------|-----------|-----------|
| FP32 | 4 | ~15 GB | ~28GB | ~52GB | ~280GB |
| FP16 | 2 | ~7,6 GB | ~14 GB | ~26GB | ~140 GB |
| INT8 (8 bit) | 1 | ~3,8 GB | ~7 GB | ~13 GB | ~70 GB |
| INT4 (4 bit) | 0,5 | ~1,9 GB | ~3,5 GB | ~6,5 GB | ~35 GB |
**Pratik yönergeler:**
- 8 GB VRAM → 4 bitte 7B modele kadar.
- 12 GB VRAM → 4 bitte 13B modele kadar.
- 24 GB VRAM → 4 bitte 70 milyara kadar model (veya 8 bitte 13 B).
- Apple Silicon (birleşik bellek), 64 GB+ sistemlerde 70B modellerini çalıştırabilir.
### RAM (Sistem Belleği)
- CPU çıkarımı için, modeli yüklemek üzere yeterli sistem RAM'ine ihtiyacınız vardır (VRAM numaralarına benzer).
- GPU çıkarımı için sistem RAM'i, modeli VRAM'e aktarmadan önce belleğe yüklemek açısından önemlidir.
### Depolama
- Ölçülen model ağırlıkları birkaç GB yer kaplar (örneğin, diskte 4 bit 7B ≈ 4 GB). Birden fazla model için en az 20-50 GB boş alanın olduğundan emin olun.
### CPU
- Hızlı işleme (ön doldurma) ve CPU boşaltma için modern çok çekirdekli bir CPU yardımcı olur.
- Apple M serisi çipler, birleşik bellek ve Neural Engine sayesinde Yüksek Lisans'lar için mükemmel performansa sahiptir.
---

## Kuantizasyon
Niceleme, ağırlıkların sayısal kesinliğini azaltır, belleği önemli ölçüde azaltır ve küçük bir doğruluk maliyetiyle hızı artırır.
### Popüler Formatlar
| Biçim | Bitler | Açıklama | Tipik kullanım |
|----------|------|------------|------------|
| **GGUF** | 4–8 | llama.cpp formatı, CPU/GPU hibriti için optimize edilmiş | Yerel çıkarım için en iyisi |
| **GPTQ** | 4–8 | Yalnızca GPU, CUDA'da verimli | NVIDIA GPU'lar için en iyisi |
| **AWQ** | 4 | Etkinleştirme özellikli, yalnızca GPU | GPU'larda toplu çıkarım için iyi |
| **ONNX** | değişken | Standartlaştırılmış, platformlar arası | Üretim porsiyonu |
### Bir Niceleme Düzeyinin Seçilmesi
- **Q8_0** (8 bit): minimum kalite kaybı, en büyük boyut.
- **Q6_K** (6-bit): iyi kalite, yeterli sıkıştırma.
- **Q5_K_M** (5-bit): ortak tatlı nokta.
- **Q4_K_M** (4-bit): çoğu görev için en küçük, kabul edilebilir kalite.
- **IQ4_XS** / **IQ3_XS**: 4/3 bitlerde daha iyi şaşkınlıkla iyileştirilmiş nicemleme.
**Genel kural:** İyi bir kalite ve boyut dengesi için Q4_K_M kullanın. Fazladan VRAM'iniz varsa Q5 veya Q6'yı kullanın.
---

## Çıkarım Motorları (Yerel)
### lama.cpp
- C++ ile yazılmıştır.
- GGUF formatını destekler.
- CPU ve GPU için optimize edilmiştir (CUDA, Metal, OpenCL aracılığıyla).
- Özellikle CPU'da çok hızlı.
- Komut satırı, sunucu modu ve Python bağlamaları.
**Örnek komut:**```bash
./llama-cli -m model.Q4_K_M.gguf -p "Tell me a joke" -n 100 -ngl 32
# -ngl 32 offloads 32 layers to GPU
```

### Ollama
- Llama.cpp'yi basit bir CLI ve REST API ile sarar.
- Modelleri otomatik olarak indirir, yönetir.
- Prototip oluşturma ve masaüstü uygulamaları için idealdir.
- Sistem istemleri için özel Model dosyalarını destekler.
```bash
ollama run phi3:3.8b
ollama run llama3:8b
```

### LM Stüdyosu
- Windows, macOS, Linux için grafiksel masaüstü uygulaması.
- Tek tıklamayla indirme ve sohbet arayüzü.
- OpenAI uyumlu API'ye sahip yerleşik yerel sunucu.
- Teknik olmayan kullanıcılar ve hızlı testler için iyidir.
### Sarılma Yüzü Transformers + bitsandbytes
- HF modelleri için standart Python kütüphanesi.
- 4 bitlik niceleme için`bitsandbytes`kullanın (`load_in_4bit=True`).
- İnce ayar için daha esnektir ancak çıkarım için llama.cpp'den daha yavaştır.
### ExLlamaV2
- GPTQ ve AWQ için çok hızlı GPU çıkarımı.
- NVIDIA GPU'larda en iyi performans.
- Toplu üretimi destekler.
### mlx (Elma)
- Apple'ın M serisi çiplere yönelik çerçevesi.
- Apple Silicon için son derece optimize edilmiş.
- Python API'si.
---

## Bellek Yönetimi
### Bağlam Penceresi ve KV Önbelleği
KV önbelleği, bağlamdaki her katman ve her belirteç için anahtar/değer çiftlerini saklar. Bağlam uzunluğuyla doğrusal olarak büyür.
Bellek maliyeti ≈ 2 × katmanlar × (KV kafaları × sönük kafa) × jetonlar × değer başına bayt
8 KV kafalı ve 128 kafalı 32 katmanlı bir model için, her jetonun maliyeti jeton başına ~32 × 8 × 128 × 2 bayt = 65 KB'dir. 128.000 jeton için bu yalnızca önbellek için ~8 GB anlamına gelir.
### Boşaltma Stratejileri
- **Katman boşaltma**: Bazı katmanları GPU'ya, diğerlerini CPU'ya yerleştirin. Saf CPU'dan daha hızlı, daha düşük VRAM gereksinimi.
- **Jeton akışı**: Jetonları tek seferde işlemek yerine aşamalı olarak işleyin.
### İstemi Önbelleğe Alma
Ön doldurma aşamasının yeniden hesaplanmasını önlemek için benzer istemlerde KV önbelleklerini yeniden kullanın. Bazı çerçeveler bunu destekler (örn. vLLM, llama.cpp ile`--prompt-cache`).
### Bellek Eşlemeli Dosyalar
Model ağırlıklarını tamamen RAM'e yüklemeden doğrudan diskten yükleyin (belleği sınırlı sistemlerdeki büyük modeller için kullanışlıdır). llama.cpp varsayılan olarak bellek eşlemeyi kullanır.
---

## Dağıtım Mimarileri
### Tek Cihaz Modu
Bir model tek bir makinede (dizüstü bilgisayar, akıllı telefon, uç cihaz) çalışır. Kişisel asistanlar, not alma uygulamaları ve kod tamamlama için kullanılır.
### Hibrit Uç Bulut
Yerel model yaygın sorguları yönetir; Karmaşık sorular için bir bulut modeline geri dönüş. Bu, her iki dünyanın da en iyisini sunar; çoğu için hız/özel, uç durumlar için yetenek.
### Dağıtılmış Çıkarım (Çoklu GPU)
Daha büyük modeller için katmanları birden fazla GPU'ya bölün (tensör paralelliği) veya bağlamı cihazlar arasında bölün (ardışık düzen paralelliği). llama.cpp'yi`-ngl`ile veya ExLlamaV2'yi`--num-gpu-layers`ile kullanın.
### Mobil Dağıtım
- **Android**: Llama.cpp'yi JNI bağlamaları veya ML Kit aracılığıyla kullanın.
- **iOS**: Llama.cpp'yi Swift bağlamaları veya mlx aracılığıyla kullanın.
- **Web**: WebLLM'yi (ONNX çalışma zamanı aracılığıyla WebGPU'da çalışır) veya transformatörler.js'yi kullanın.
---

## Performans Optimizasyonu
### Flaş Dikkati
Dikkat hesaplamasını hızlandırır ve bellek kullanımını azaltır. llama.cpp, ExLlamaV2 ve modern transformatör kitaplıklarında mevcuttur.
### Toplu Çıkarım
Tek bir ileri geçişte birden fazla istemi işleyin. Verimi önemli ölçüde artırır.`llama-batch`veya vLLM'yi kullanın.
### Erken Durdurma / Token Bütçeleme
Sınırsız üretimi önlemek için maksimum token bütçesi belirleyin.
### Spekülatif Kod Çözme
Belirteçleri tahmin etmek için küçük bir hızlı model (taslak) kullanın, ardından büyük modelle paralel olarak doğrulayın. 2–3 kat hızlanma sağlayabilir.
---

## Pratik Kurulum Kılavuzu
### 1. Ollama'yı yükleyin
```bash
curl -fsSL https://ollama.com/install.sh | sh
```

### 2. Bir Model Çekin
```bash
ollama pull phi3:3.8b-q4_K_M
```

### 3. API ile çalıştırın
```bash
ollama serve
```

Daha sonra isteklerinizi`http://localhost:11434/api/generate`adresine gönderin.
### 4. Python Entegrasyonu
```python
import requests

response = requests.post(
    "http://localhost:11434/api/generate",
    json={"model": "phi3:3.8b", "prompt": "Hello", "stream": False}
)
print(response.json()["response"])
```

### 5. (Alternatif) Llama.cpp'yi doğrudan kullanın
```bash
# Download GGUF from Hugging Face
wget https://huggingface.co/microsoft/Phi-3-mini-4k-instruct-gguf/resolve/main/Phi-3-mini-4k-instruct-q4_K_M.gguf

# Run server
./llama-server -m Phi-3-mini-4k-instruct-q4_K_M.gguf --host 0.0.0.0 --port 8080
```

---

## İzleme ve Gözlemlenebilirlik
- GPU kullanımını izleyin (Linux'ta `nvidia-smi`, macOS'ta Activity Monitor).
- Bellek kullanımını izleyin (RAM ve VRAM).
- Saniye başına jetonları takip edin (verim).
- İlk jetona kadar geçen süreyi (gecikme) izleyin.
- Llama.cpp veya Ollama'daki yerleşik günlük kaydını kullanın.
---

## Sınırlamalar ve Takaslar
- **Kalite farkı**: Küçük yerel modeller (3.8B–7B), karmaşık mantık yürütme açısından genellikle büyük bulut modellerinden (GPT-4, Claude 3.5) daha düşük performans gösterir.
- **Bilgi kesintisi**: Model bilgisi eğitim sırasında dondurulur; Güncel bilgileri eklemek için RAG'ı kullanın.
- **Çok dilli**: Daha küçük modellerin birden fazla dil kapasitesi daha az olabilir.
- **Araç kullanımı**: Aracı iş akışları (işlev çağırma) küçük modellerde daha az güvenilir olabilir.
Pek çok günlük görev (özetleme, Soru-Cevap, kod tamamlama, sınıflandırma) için yerel modeller halihazırda yeterlidir ve hızla gelişmektedir.