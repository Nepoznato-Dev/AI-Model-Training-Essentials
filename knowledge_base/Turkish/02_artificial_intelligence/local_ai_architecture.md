# Yerel AI Mimarisi

Büyük dil modellerini tamamen cihaz üzerinde çalıştırmaya yönelik; donanım gereksinimleri, çıkarım motorları, bellek optimizasyonu ve uç dağıtım için sistem tasarımını kapsayan pratik bir rehber.

---

## AI'yi Neden Yerel Çalıştırmalı?

- **Gizlilik**: Veri cihazdan çıkmaz.
- **Maliyet**: Token başına API ücreti yoktur.
- **Gecikme**: Öngörülebilir, ağdan bağımsız çıkarım sağlar.
- **Çevrimdışı Kullanılabilirlik**: İnternet olmadan çalışır.
- **Kontrol**: Model sürümü, özelleştirme ve ince ayar üzerinde tam kontrol sağlar.

---

## Donanım Gereksinimleri

### GPU Belleği (VRAM)
En kritik kaynaktır. Bellekte model boyutu ≈ **parametre sayısı × parametre başına bayt**.

| Hassasiyet | Parametre başına bayt | 3.8B model | 7B model | 13B model | 70B model |
|-----------|-----------------------|------------|----------|-----------|-----------|
| FP32      | 4                     | ~15 GB     | ~28 GB   | ~52 GB    | ~280 GB   |
| FP16      | 2                     | ~7.6 GB    | ~14 GB   | ~26 GB    | ~140 GB   |
| INT8 (8-bit) | 1                | ~3.8 GB    | ~7 GB    | ~13 GB    | ~70 GB    |
| INT4 (4-bit) | 0.5              | ~1.9 GB    | ~3.5 GB  | ~6.5 GB   | ~35 GB    |

**Pratik yönergeler:**
- 8GB VRAM → 4-bit'te 7B modellere kadar.
- 12GB VRAM → 4-bit'te 13B modellere kadar.
- 24GB VRAM → 4-bit'te 70B modellere kadar (veya 8-bit'te 13B).
- Apple Silicon (birleşik bellek), 64GB+ sistemlerde 70B modelleri çalıştırabilir.

### RAM (Sistem Belleği)
- CPU ile çıkarım için, modeli yükleyecek kadar sistem RAM'i gerekir (yaklaşık VRAM rakamlarına benzer).
- GPU ile çıkarım için, model VRAM'e aktarılmadan önce belleğe alınacağı için sistem RAM'i önemlidir.

### Depolama
- Kuantize edilmiş model ağırlıkları birkaç GB yer kaplar (ör. 4-bit 7B ≈ diskte 4 GB). Birden çok model için en az 20–50 GB boş alan bırakın.

### CPU
- İstem işleme (prefill) ve CPU'ya katman aktarma için modern, çok çekirdekli bir CPU faydalıdır.
- Apple M serisi çipler, birleşik bellek ve Neural Engine sayesinde LLM'lerde çok iyi performans gösterir.

---

## Kuantizasyon

Kuantizasyon, ağırlıkların sayısal hassasiyetini düşürerek doğrulukta küçük bir bedel karşılığında belleği ciddi ölçüde azaltır ve hızı artırır.

### Yaygın Formatlar

| Format | Bit | Açıklama | Tipik kullanım |
|--------|------|----------|----------------|
| **GGUF** | 4–8 | llama.cpp formatı, CPU/GPU hibriti için optimize edilmiştir | Yerel çıkarım için en iyisi |
| **GPTQ** | 4–8 | Yalnızca GPU, CUDA üzerinde verimli | NVIDIA GPU'lar için en iyisi |
| **AWQ** | 4 | Aktivasyon farkındalıklı, yalnızca GPU | GPU'larda toplu çıkarım için iyi |
| **ONNX** | değişken | Standartlaştırılmış, platformlar arası | Üretim ortamında sunum |

### Kuantizasyon Düzeyi Seçimi
- **Q8_0** (8-bit): minimum kalite kaybı, en büyük boyut.
- **Q6_K** (6-bit): iyi kalite, makul sıkıştırma.
- **Q5_K_M** (5-bit): yaygın tatlı nokta.
- **Q4_K_M** (4-bit): en küçük boyut, çoğu görev için kabul edilebilir kalite.
- **IQ4_XS** / **IQ3_XS**: 4/3 bit'te daha iyi perplexity sunan geliştirilmiş kuantizasyon.

**Genel kural:** Kalite ve boyut dengesi için Q4_K_M kullanın. Ek VRAM'iniz varsa Q5 veya Q6 kullanın.

---

## Yerel Çıkarım Motorları

### llama.cpp
- C++ ile yazılmıştır.
- GGUF formatını destekler.
- CPU ve GPU için optimize edilmiştir (CUDA, Metal, OpenCL üzerinden).
- Özellikle CPU'da çok hızlıdır.
- Komut satırı, sunucu modu ve Python bağlayıcıları sunar.

**Örnek komut:**
```bash
./llama-cli -m model.Q4_K_M.gguf -p "Tell me a joke" -n 100 -ngl 32
(-ngl 32 offloads 32 layers to GPU)
```

### Ollama
- llama.cpp'yi basit bir CLI ve REST API ile sarmalar.
- Modelleri otomatik indirir ve yönetir.
- Prototipleme ve masaüstü uygulamaları için çok uygundur.
- Sistem istemleri için özel Modelfile'ları destekler.

**Kullanım:**
```bash
ollama run phi3:3.8b
ollama run llama3:8b
```

### LM Studio
- Windows, macOS ve Linux için grafik masaüstü uygulamasıdır.
- Tek tıklamayla indirme ve sohbet arayüzü sunar.
- OpenAI uyumlu API'ye sahip yerleşik bir yerel sunucu içerir.
- Teknik olmayan kullanıcılar ve hızlı testler için uygundur.

### Hugging Face Transformers + bitsandbytes
- Hugging Face modelleri için standart Python kütüphanesidir.
- 4-bit kuantizasyon için bitsandbytes kullanın (`load_in_4bit=True`).
- Fine-tuning açısından daha esnektir, ancak çıkarım için llama.cpp'den daha yavaştır.

### ExLlamaV2
- GPTQ ve AWQ için çok hızlı GPU çıkarımı sağlar.
- NVIDIA GPU'larda en iyi performansı verir.
- Toplu üretimi destekler.

### mlx (Apple)
- Apple'ın M serisi çipler için sunduğu çerçevedir.
- Apple Silicon için yoğun biçimde optimize edilmiştir.
- Python API sunar.

---

## Bellek Yönetimi

### Bağlam Penceresi ve KV Önbelleği
KV önbelleği, bağlamdaki her katman ve her token için anahtar-değer çiftlerini saklar. Bağlam uzunluğuyla doğrusal olarak büyür.

Bellek maliyeti ≈ 2 × katmanlar × (KV başlıkları × başlık boyutu) × token sayısı × değer başına bayt

8 KV başlığı ve 128 başlık boyutuna sahip 32 katmanlı bir model için her token yaklaşık ~32 × 8 × 128 × 2 bayt = token başına 65 KB maliyet oluşturur. 128k token'da bu, yalnızca önbellek için ~8 GB demektir.

### Katman Aktarma Stratejileri
- **Katman Aktarma**: Bazı katmanları GPU'ya, diğerlerini CPU'ya koyun. Tam CPU'ya göre daha hızlıdır, VRAM gereksinimi daha düşüktür.
- **Token Akışı**: Tüm token'ları tek seferde değil, artımlı olarak işleyin.

### İstem Önbellekleme
Prefill aşamasını yeniden hesaplamamak için benzer istemler arasında KV önbelleklerini yeniden kullanın. Bazı çerçeveler bunu destekler (ör. vLLM, `--prompt-cache` ile llama.cpp).

### Bellek Eşlemeli Dosyalar
Model ağırlıklarını tamamen RAM'e almadan doğrudan diskten yükleyin (belleği sınırlı sistemlerde büyük modeller için faydalıdır). llama.cpp varsayılan olarak bellek eşlemeyi kullanır.

---

## Dağıtım Mimarileri

### Tek Cihaz Modu
Tek bir model, tek bir makinede çalışır (dizüstü bilgisayar, akıllı telefon, uç cihaz). Kişisel asistanlar, not alma uygulamaları ve kod tamamlama için kullanılır.

### Hibrit Uç-Bulut
Yerel model yaygın sorguları işler; karmaşık sorular için bulut modeline geri düşer. Böylece iki dünyanın da en iyi yanlarını sunar: çoğu durumda hız ve mahremiyet, uç durumlarda ise daha yüksek yetenek.

### Dağıtık Çıkarım (Multi-GPU)
Daha büyük modeller için katmanları birden fazla GPU'ya bölün (tensor parallelism) veya bağlamı cihazlar arasında bölün (pipeline parallelism). llama.cpp'de `-ngl` ya da ExLlamaV2'de `--num-gpu-layers` kullanın.

### Mobil Dağıtım
- **Android**: JNI bağlayıcıları veya ML Kit üzerinden llama.cpp kullanın.
- **iOS**: Swift bağlayıcıları veya mlx üzerinden llama.cpp kullanın.
- **Web**: WebLLM (ONNX runtime üzerinden WebGPU'da çalışır) veya transformers.js kullanın.

---

## Performans Optimizasyonu

### Flash Attention
Attention hesaplamasını hızlandırır ve bellek kullanımını azaltır. llama.cpp, ExLlamaV2 ve modern Transformer kütüphanelerinde bulunur.

### Toplu Çıkarım
Birden fazla istemi tek bir forward pass içinde işleyin. İş hacmini ciddi biçimde artırır. llama-batch veya vLLM kullanın.

### Erken Durdurma / Token Bütçeleme
Sınırsız üretimi önlemek için maksimum token bütçesi belirleyin.

### Spekülatif Kod Çözme
Küçük ve hızlı bir taslak model, token'ları tahmin eder; büyük model bunları paralel olarak doğrular. 2–3× hızlanma sağlayabilir.

---

## Pratik Kurulum Rehberi

1. Ollama'yı kurun
```bash
curl -fsSL https://ollama.com/install.sh | sh
```

2. Bir model çekin
```bash
ollama pull phi3:3.8b-q4_K_M
```

3. API ile çalıştırın
```bash
ollama serve
```
Ardından istekleri `http://localhost:11434/api/generate` adresine gönderin.

4. Python Entegrasyonu
```python
import requests

response = requests.post(
    "http://localhost:11434/api/generate",
    json={"model": "phi3:3.8b", "prompt": "Hello", "stream": False}
)
print(response.json()["response"])
```

5. (Alternatif) Doğrudan llama.cpp kullanın
```bash
# Download GGUF from Hugging Face
wget https://huggingface.co/microsoft/Phi-3-mini-4k-instruct-gguf/resolve/main/Phi-3-mini-4k-instruct-q4_K_M.gguf

# Run server
./llama-server -m Phi-3-mini-4k-instruct-q4_K_M.gguf --host 0.0.0.0 --port 8080
```

---

## İzleme ve Gözlemlenebilirlik

- GPU kullanımını izleyin (`nvidia-smi` Linux'ta, Activity Monitor macOS'te).
- Bellek kullanımını izleyin (RAM ve VRAM).
- Saniye başına token sayısını izleyin (iş hacmi).
- İlk token'a kadar geçen süreyi izleyin (gecikme).
- llama.cpp veya Ollama'nın yerleşik log'larını kullanın.

---

## Sınırlamalar ve Ödünleşimler

- **Kalite farkı**: Küçük yerel modeller (3.8B–7B), karmaşık akıl yürütmede genellikle büyük bulut modellerinin (GPT-4, Claude 3.5) gerisinde kalır.
- **Bilgi sınırı**: Model bilgisi eğitim anında donar; güncel bilgiyi eklemek için RAG kullanın.
- **Çok Dillilik**: Daha küçük modellerin çok dilli yetenekleri daha sınırlı olabilir.
- **Araç Kullanımı**: Ajan tabanlı iş akışları (function calling), küçük modellerde daha az güvenilir olabilir.

Birçok gündelik görev için (özetleme, soru-cevap, kod tamamlama, sınıflandırma) yerel modeller şimdiden yeterlidir ve hızla gelişmektedir.
