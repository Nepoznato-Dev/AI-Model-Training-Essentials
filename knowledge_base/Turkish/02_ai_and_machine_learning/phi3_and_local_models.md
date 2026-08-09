---
# Metadata
title: "Phi-3-mini and the Local AI Model Landscape"
description: "Running models locally"
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
tags: [phi3, local, models, ai-and-machine-learning]
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

# Phi-3-mini ve Yerel Yapay Zeka Modeli Ortamı
Microsoft'un Phi-3-mini modelinin (tasarım felsefesi, mimari seçimleri ve performans özellikleri) analizi ve başarısının bize etkili, verimli yapay zeka sistemleri oluşturma konusunda neler öğrettiği.
---

## Phi-3-mini'ye genel bakış
Phi-3-mini, Microsoft Research tarafından geliştirilen ve Nisan 2026'da piyasaya sürülen küçük bir dil modelidir (SLM). Tanımlayıcı özellikleri şunlardır:
- **3,8 milyar parametre** — Meta'nın Llama 3 8B'sinden kabaca 6 kat daha küçük
- **Ders kitabı kalitesinde eğitim verileri** — olağanüstü performansının anahtarı
- **İki içerik çeşidi**: 4.096 jeton (standart) ve 128.000 jeton (uzun içerik)
- **Tüketici donanımı üzerinde çalışır** — 4 bit nicelemeli 8 GB VRAM'e rahatlıkla sığar
- **Mobil dağıtım** — Microsoft, iPhone 14'te Phi-3-mini'nin çalıştığını gösterdi
- **Açık ağırlıklar** — Hugging Face'te yerel kullanım için mevcuttur
Küçük boyutuna rağmen Phi-3-mini, çeşitli muhakeme ve bilgi kriterlerinde 3-5 kat daha büyük modellerle eşleşir veya onlardan daha iyi performans gösterir.
---

## "Ders Kitabı Kalitesi" Eğitim Felsefesi
Phi serisinin arkasındaki temel fikir, **veri kalitesinin veri miktarından daha önemli olduğudur**. Geleneksel LLM eğitimi, web'den alınan internet ölçeğindeki metinleri (yüz milyarlarca jetonluk çeşitli, gürültülü içerik) kullanır.
Phi ekibi şunu sordu: Ham web metni yerine ders kitaplarında bulunan yoğun, iyi açıklanmış, yapılandırılmış içerik üzerine eğitim alsanız ne olur?
### Phi-1 (2023): Kavram Kanıtı
Orijinal Phi-1 makalesi ("Ders Kitapları İhtiyacınız Olan Tek Şey"), sentetik olarak oluşturulmuş "ders kitabı kalitesinde" Python kodu ve alıştırmaları üzerine bir 1.3B modelini eğitiyordu. HumanEval'de (Python kod oluşturma) kendi boyutunun 10 katı modellerden daha iyi performans gösterdi. Bu, seçilmiş, yapılandırılmış verilerin küçültülmüş model boyutunu telafi edebileceğine dair güçlü bir sinyaldi.
### Phi-1.5 ve Phi-2
Daha sonraki modeller, aşağıdakilerin bir karışımını kullanarak yaklaşımı genel muhakemeye genişletti:
- Eğitimsel değer için seçilen yüksek kaliteli web metni
- GPT-4 tarafından ders kitapları ve alıştırmalar tarzında oluşturulan sentetik veriler
- Dikkatlice tekilleştirilen ve filtrelenen seçilmiş veri kümeleri
### Phi-3-mini: Uygun Ölçekte Tarif
Phi-3-mini, eğitim için yaklaşık 3,3 trilyon token kullanıyor; mutlak standartlara göre büyük, ancak Llama 3 için kullanılan 15T tokenlardan çok daha küçük. En önemli fark, yalnızca yüksek kaliteli içeriği seçen filtreleme ve iyileştirme hattıdır.
Eğitim veri seti şunları içerir:
1. **Yoğun şekilde filtrelenmiş web verileri** — yalnızca eğitici veya açıklayıcı içeriğe sahip, birden fazla kalite sinyaliyle filtrelenen sayfalar
2. **Sentetik ders kitabı verileri** — STEM, beşeri bilimler, kodlama ve muhakeme alanlarındaki kavramların GPT-4 tarafından oluşturulan açıklamaları
3. **Sentetik alıştırmalar** — adım adım akıl yürütmeyle soru-cevap çiftleri (düşünce zinciri stili)
4. **Kod verileri** — seçilmiş programlama örnekleri ve belgeler
---

## Mimari Detaylar
Phi-3-mini, çeşitli verimlilik iyileştirmeleriyle birlikte standart yalnızca kod çözücü Transformatör mimarisini kullanır:
### Gruplandırılmış Sorgu Dikkati (GQA)
Standart çok kafalı dikkat (MHA), dikkat kafası başına bir anahtar-değer (KV) kafasına sahiptir. GQA, aynı KV kafalarını paylaşacak şekilde birden fazla dikkat kafasını gruplandırarak KV önbellek boyutunu (çıkarım sırasında bağlamı depolamak için gereken bellek) azaltır. Bu, Phi-3-mini'yi, özellikle de aksi halde çok büyük KV önbellekleri gerektirecek olan 128k uzun bağlamlı varyant için, çıkarım zamanında önemli ölçüde daha hızlı hale getirir.
### Mimari Numaralar
- Katmanlar: 32
- Dikkat başlıkları: 32 (sorgu), 8 (anahtar/değer, gruplandırılmış)
- Gizli boyut: 3.072
- İleri besleme boyutu: 8.192
- Kelime büyüklüğü: 32.064 (Llama tokenizer ile aynı)
- Aktivasyon fonksiyonu: SiLU (Sigmoid Doğrusal Birim)
### SFT ve RLHF Hizalaması
Tüm dağıtılan sohbet modellerinde olduğu gibi Phi-3-mini de şunları gerçekleştirir:
1. Talimatları takip eden örneklerde **Denetimli İnce Ayar (SFT)**
2. **İnsan tercihi verileri üzerine eğitilmiş bir ödül modeline karşı **Yakınsal Politika Optimizasyonu (PPO)**
Bu, temel sonraki jeton tahmincisini yararlı, talimatları takip eden bir asistana dönüştürür.
---

## Karşılaştırma Performansı
Phi-3-mini, parametre sayısına göre oldukça iyi performans gösteriyor:
| Karşılaştırma | Phi-3-mini (3.8B) | Lama 3 8B | Mistral 7B | GPT-3.5 |
|-----------|-----------|-----------|------------|-----------|
| MMLU | ~%69 | ~%66 | ~%62 | ~%70 |
| İnsan Değerlendirmesi | ~%56 | ~%60 | ~%30 | ~%73 |
| GSM8K | ~%82 | ~%79 | ~%35 | ~%78 |
| ARC Mücadelesi | ~%84 | ~%82 | ~%60 | ~%79 |
**Önemli gözlemler:**
- Phi-3-mini, MMLU'da 50 kat daha az parametreyle GPT-3.5 ile eşleşir
- Daha küçük olmasına rağmen listelenen tüm kıyaslamalarda Mistral 7B'den daha iyi performans gösteriyor
- 2 kat daha küçük olmasına rağmen neredeyse Llama 3 8B ile eşleşir (3.8B vs 8B)
*Kaynak: Microsoft Phi-3 Teknik Raporu (Nisan 2026)*
---

## Küçük Modeller Neden Büyük Modellerden Daha İyi Performans Gösterebilir?
Phi deneyimi birkaç önemli dersi göstermektedir:
### 1. Eğitim Verilerinin Dağıtımı En Önemli Şeydir
Bir modelin elde ettiği kıyaslama puanları, ham parametre sayısından çok, üzerinde eğitim aldığı veri türünü yansıtır. Yüksek kaliteli akıl yürütme örnekleriyle eğitilmiş küçük bir model, akıl yürütme kıyaslamalarında gürültülü web metniyle eğitilmiş büyük bir modelden daha iyi performans gösterecektir.
### 2. Bilgi Yoğunluğu ve Bilgi Hacmi
Bir 3.8B modeli, ağırlıklarında 70B modeli kadar veri depolayamaz. Ancak, eğer gerçekleri ezberlemek yerine yapılandırılmış akıl yürütme kapasitesini kullanacak şekilde eğitilmişse yine de iyi bir şekilde akıl yürütebilir. GSM8K gibi kıyaslamalar, çok adımlı aritmetik akıl yürütmeyi test eder; bu, verimli bir şekilde öğretilebilecek bir beceridir.
### 3. Maliyet Verimlilik Eğrisi
Gerçek dünyadaki pek çok görev için (Soru-Cevap, kodlama yardımı, özetleme), Phi-3-mini düzeyindeki yetenek yeterlidir. 3.8B modelini yerel olarak çalıştırmak:
- **Ücretsiz** — API maliyeti yok
- **Gizli** — cihazdan hiçbir veri çıkmıyor
- **Hızlı** — modern bir dizüstü bilgisayar GPU'sunda gerçek zamanlı olarak jetonlar üretir
- **Her yere dağıtılabilir** — akıllı telefonlar, uç cihazlar, hava boşluklu sistemler
### 4. Kuvvet Çarpanı Olarak Sentetik Veri Üretimi
Küçük bir öğrenci modeli için yüksek kaliteli eğitim verileri oluşturmak amacıyla büyük bir öğretmen modelinin (GPT-4) kullanılması, bilginin ayrıştırılmasının bir biçimidir. Bu "en iyisinden öğren, en ucuzunu kullan" yaklaşımı sektörde giderek daha yaygın hale geliyor.
---

## Potato.ai için dersler
Phi-3 tasarım felsefesi, Potato.ai'nin KB merkezli yaklaşımıyla yakından uyumludur:
**KB kaynaklarında nicelikten ziyade kalite**: Phi-3-mini'nin daha iyi veriler sayesinde daha büyük modelleri geride bırakması gibi, Potato.ai'nin bilgi tabanı da büyük hacimli gürültülü metinlerden ziyade yoğun, iyi yapılandırılmış kaynak belgelerinden daha fazla yararlanır.
**Akıl yürütme yapısına odaklanma**: Phi-3, adım adım akıl yürütmeyi gösteren örnekler üzerinde eğitilmiştir. Potato.ai de KB kaynaklarının ham gerçekler yerine açıklamalar içermesini sağlayarak benzer şekilde gelişebilir.
**Verimli KB kapsamı**: Phi-3-mini'nin 3,8B parametreleri insan bilgisinin büyük bir bölümünü verimli bir şekilde kapsamalıdır. Potato.ai'nin başlangıç ​​bilgi bankası kaynakları da benzer şekilde kelime başına yaygın sorguların maksimum kapsamını hedeflemelidir.
**Önce yerel uygulanabilir**: Phi-3-mini'nin başarısı, tamamen yerel bir yapay zekanın birçok görev için bulut tabanlı modellerle eşleşebileceğini gösteriyor. Bu, Potato.ai'nin harici API çağrıları olmadan tamamen cihaz üzerinde çalışan mimarisini doğrular.
---

## Diğer Önemli Yerel Modeller (2026)
### Lama 3 (Meta, 2026)
- 8B ve 70B çeşitleri (400B+ geliyor)
- Her boyutta sınıfının en iyisi açık ağırlıklı modeller
- 8.192 token içerik penceresi (genişletilebilir)
- Ticari kullanım için Apache 2.0 lisansı
### Mistral / Mixtral
- **Mistral 7B**: ağırlığının üzerinde yumruklar atıyor, sürgülü pencere dikkat çekiyor
- **Mixtral 8x7B**: uzmanların karışımı, yerel olarak GPT-3.5 seviyesinde performans
- **Mistral-Nemo 12B**: sınıfına göre daha büyük, son teknoloji
### Gemma 2 (Google, 2026)
- Google'dan 2B ve 9B çeşitleri
- Boyutlarına ilişkin güçlü gerekçeler
- Yerel kullanım için izin verilen bir lisans kapsamında mevcuttur
### Qwen 2.5 (Alibaba, 2026)
- 0,5B'den 72B'ye kadar değişkenler
- Güçlü çoklu dil yeteneği
- Özellikle küçük boyutlardaki kodlama görevleri için iyidir
---

## 2026–2025'te Yerel Yapay Zeka Modeli Pazarı
Yerel ve bulut modelleri arasındaki fark 2026'da önemli ölçüde daraldı:
- Dizüstü bilgisayarda çalışan ücretsiz, 4 bitlik nicemlenmiş Phi-3-mini, birçok kıyaslamada GPT-3.5'ten (eğitilmesi milyonlara mal olan bir model) daha iyi performans gösteriyor
- Tüketici 24 GB GPU'lar (NVIDIA RTX 3090, 4090), 70B modellerini 4 bit olarak çalıştırabilir
- Apple Silicon M-serisi Mac'ler, birleşik bellek mimarileri nedeniyle yerel yapay zeka açısından popülerdir — 64 GB belleğe sahip bir M3 Max, 70B modelleri sorunsuzca çalıştırabilir
- Ollama, LM Studio ve llama.cpp, yerel model dağıtımını teknik bilgisi olmayan kullanıcılar için erişilebilir hale getirdi
Bunun anlamı: gizliliğe duyarlı uygulamalar, uç dağıtım veya maliyete duyarlı senaryolar için yerel modeller artık çok çeşitli görevlere yönelik bulut API'lerine güvenilir bir alternatiftir.