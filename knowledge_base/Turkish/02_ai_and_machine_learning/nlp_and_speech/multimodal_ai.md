---
# Metadata
title: "Multimodal AI"
description: "Vision-language models, CLIP, DALL-E, cross-modal learning"
category: "AI and Machine Learning"
subcategory: "NLP and Speech"
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
    changes: "Moved to nlp_and_speech/ subfolder; added subcategory field"
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
tags: [multimodal, ai, ai-and-machine-learning]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "8 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Çok modlu yapay zeka
Çok modlu yapay zeka sistemleri, birden fazla veri türünden (metin, resim, ses, video ve daha fazlası) gelen bilgileri aynı anda işler ve birleştirir. Daha önceki yapay zeka sistemleri genellikle tek modlu (yalnızca metin, yalnızca görüntü) iken, en yetenekli modern sistemler çok modludur. GPT-4V, görselleri ve metni birlikte okur; Gemini metni, görüntüleri, sesi ve videoyu yerel olarak işler; ve Sora gibi sistemler, metin açıklamalarından video oluşturur. Bu dosya çok modlu yapay zekanın nasıl çalıştığını, arkasındaki mimarileri ve yöntemleri birleştirmenin neden bu kadar güçlü olduğunu kapsar.
---

## Neden Multimodal?
| Fayda | Açıklama | Örnek |
|-----------|------------|------------|
| **Daha zengin anlayış** | Farklı yöntemler tamamlayıcı bilgiler sağlar | Bir video, metnin tek başına sağlayamayacağı hareketi, sesi ve bağlamı aktarır |
| **Daha iyi genelleme** | Modaliteler arası öğrenme daha sağlam temsiller yaratır | "Kedi"nin hem resimlerini hem de metin açıklamalarını gören bir model, kavramı daha iyi anlıyor |
| **Daha doğal etkileşim** | İnsanlar birden fazla kanal aracılığıyla iletişim kurar | Neye işaret ettiğinizi gören sesli asistanlar |
| **Modlar arası transfer** | Bir yönteme ait bilgi diğerine yardımcı olur | Görüntü anlama, metin oluşturmayı geliştirir ve bunun tersi de geçerlidir |
---

## Çekirdek Mimariler
### Vizyon-Dil Modelleri (VLM'ler)
Hem görseli hem de metni bir arada işleyen modeller.
| Mimarlık | Nasıl Çalışır | Örnekler |
|-------------|------------|------------|
| **Çift kodlayıcı** | Görüntü ve metin için ayrı kodlayıcılar; daha sonraki bir aşamada birleştirme | KLİP, HİZALAMA |
| **Füzyon kodlayıcı** | Resim ve metin belirteçleri serpiştirilir ve birlikte işlenir | Flamingo, İkizler |
| **Çapraz dikkat** | Metin belirteçleri görüntü özelliklerine katılır (veya tam tersi) | Flamingo, CoCa |
| **Birleşik belirteç oluşturucu** | Resimler jetonlara dönüştürülür ve metin jetonlarıyla birlikte işlenir | İkizler, Bukalemun |
### Vizyon-Dil Modelleri Nasıl Çalışır?
| Adım | Açıklama |
|------|-----------------|
| **1. Görüntüyü kodla** | Bir görüntü kodlayıcı (ViT, SigLIP), görüntüyü bir dizi özellik vektörüne dönüştürür |
| **2. Metni kodlayın** | Bir dil kodlayıcı metin belirteçlerini işler |
| **3. Sigorta yöntemleri** | Görüntü özellikleri dil modelinin yerleştirme alanına yansıtılır |
| **4. Oluştur** | Dil modeli, hem görüntü hem de metin girişlerine göre koşullandırılmış metin üretir |
### Temel Vizyon-Dil Modelleri
| Modeli | Geliştirici | Mimarlık | Önemli Özellik |
|----------|-----------|---------------|-------|
| **KLİP** | OpenAI | Çift kodlayıcı (ViT + metin kodlayıcı) | Metin aracılığıyla sıfır atışlı görüntü sınıflandırması |
| **LLaVA** | Açık kaynak | LLaMA + CLIP görsel kodlayıcı | Açık kaynaklı VLM; güçlü topluluk |
| **GPT-4V / 4o** | OpenAI | Birleşik çok modlu | Metni, görüntüleri ve sesi birlikte işler |
| **İkizler** | Google DeepMind | Eğitimden doğal olarak çok modlu | Baştan sona multimodal için tasarlandı |
| **Claude** | Antropik | Vizyon + metin | Belge ve grafik anlamada güçlü |
| **Qwen-VL** | Alibaba | Açık ağırlıklı VLM | Kapalı modellerle rekabetçi |
| **StajyerVL** | Açık kaynak | Çok ölçekli görüntü kodlayıcı | Güçlü açık kaynak seçeneği |
---

## Ses ve Konuşma Modelleri
### Konuşma Tanıma (ASR)
| Modeli | Mimarlık | Önemli Özellik |
|----------|----------------|------|
| **Fısıltı** (OpenAI) | Kodlayıcı-kod çözücü Transformatörü | 680.000 saatlik çok dilli ses eğitimi aldı; sağlam |
| **Uyumlu** | Evrişim + kendine dikkat | Yerel ve küresel özellikleri birleştiriyor |
| **wav2vec 2.0** | Kendi kendini denetleyen | Etiketlenmemiş konuşmadan öğrenir |
| **USM** (Google) | Evrensel konuşma modeli | 2 milyon saat etiketli veri; 300'den fazla dil |
### Metinden Konuşmaya (TTS)
| Modeli | Yaklaşım | Önemli Özellik |
|----------|----------|------|
| **VALL-E** (Microsoft) | Sinir kodlayıcı | 3 saniyelik örnekten ses klonlama |
| **Havlama** (Suno) | Trafo tabanlı | Çok dilli; konuşma dışı sesleri içerir |
| **ElevenLabs** | Ticari | Yüksek kaliteli ses klonlama |
| **SohbetTTS** | Açık kaynak | Doğal prozodi ile günlük konuşma |
| **Balık Konuşması** | Açık kaynak | Çok dilli; hızlı çıkarım |
### Sesi Anlama
| Modeli | Yetenek |
|----------|---------------|
| **SesLDM** | Metinden ses efekti oluşturma |
| **MüzikGen** (Meta) | Metinden müziğe dönüştürme |
| **Qwen-Ses** | Sesi anlama (konuşma, müzik, çevresel sesler) |
| **SOMON** | Konuşma, ses, dil, müzik ve gürültüyü anlama |
---

## Video Modelleri
Video; görüntüleri, sesi, metni ve zamanı birleştirerek onu en karmaşık yöntem haline getirir.
| Modeli | Tür | Yetenek |
|----------|------|------------|
| **Sora** (OpenAI) | Metinden videoya | 1080p'ye kadar; fiziği anlıyor |
| **İkizler** | Videoyu anlama | Uzun videoları sesli olarak analiz edebilir |
| **Video-LLaVA** | Video + metin | Açık kaynaklı video anlayışı |
| **Pist Gen-3** | Metin/resimden videoya | Ticari video üretimi |
| **Kling** | Metinden videoya | Uzun biçimli video üretimi |
### Videoyu Anlama Zorlukları
| Mücadelesi | Açıklama |
|-----------|----------------|
| **Zamansal akıl yürütme** | Zaman içinde ortaya çıkan olayları anlamak |
| **Uzun bağlam** | Videolar saatlerce sürebilir; tüm çerçevelerin işlenmesi pahalıdır |
| **Görsel-işitsel senkronizasyon** | Söylenenleri gösterilenlerle bağlantılandırma |
| **Nedensellik** | Video dizilerindeki neden ve sonucu anlama |
---

## Modallar Arası Erişim
Farklı yöntemlerde alakalı içeriği bulma.
| Görev | Açıklama | Örnek |
|------|-------------|--------|
| **Metin → Resim** | Bir metin sorgusuyla eşleşen görselleri bulun | Fotoğraf kitaplığında "dağların üzerinden gün batımı" ifadesini arayın |
| **Resim → Metin** | Bir görselle alakalı metni bulun | Resimler için başlıklar oluşturma |
| **Metin → Ses** | Bir açıklamayla eşleşen sesleri bulun | Ses tasarımı: "çakıl üzerinde ayak sesleri" |
| **Resim → Resim** | Görsel olarak benzer görselleri bulun | Resme göre ürün arama |
### Çapraz Mod Erişimi için KLİP
CLIP'in paylaşımlı yerleştirme alanı, sıfır atışlı çapraz mod alımını mümkün kılar:
| Adım | Açıklama |
|------|-----------------|
| 1 | Tüm görüntüleri görsel kodlayıcıyla kodlayın |
| 2 | Metin sorgusunu metin kodlayıcıyla kodlayın |
| 3 | Metin yerleştirme ve tüm görüntü yerleştirmeler arasındaki kosinüs benzerliğini hesaplayın |
| 4 | En yüksek benzerliğe sahip görselleri döndür |
Bu, **sıfır atış** yeteneği adı verilen bir özellik olan, göreve özel herhangi bir eğitim gerektirmeden çalışır.
---

## Somutlaştırılmış Yapay Zeka
Somutlaştırılmış yapay zeka, çok modlu algıyı fiziksel eylemle birleştirir.
| Sistem | Modalite | Başvuru |
|----------|----------|------------|
| **RT-2** (Google) | Görme + dil → robot eylemleri | Metin talimatlarından genel amaçlı robot kontrolü |
| **Ekto** | Açık kaynaklı robot politikası | Çeşitli robot verileri üzerine eğitim |
| **Tesla Optimus** | Vizyon + dil → fiziksel görevler | Genel görevler için insansı robot |
| **Şekil 01** | Görme + dil + konuşma | Konuşma yeteneğine sahip insansı robot |
### Somutlaştırılmış Yapay Zekadaki Zorluklar
| Mücadelesi | Neden Zor |
|-----------|-----------------|
| **Simülasyon ile gerçek arasındaki fark** | Simülasyon, gerçek dünya fiziğini mükemmel şekilde yakalayamıyor |
| **Beceri** | İnce motor kontrolü (eller, parmaklar) son derece zordur |
| **Güvenlik** | Fiziksel robotlar gerçek zarara neden olabilir |
| **Gerçek zamanlı işleme** | Milisaniyeler içinde algılamalı, karar vermeli ve harekete geçmelidir |
| **Genelleme** | Kırmızı bardakları almak üzere eğitilmiş bir robot, mavi bardakları almakta başarısız olabilir |
---

## Veri ve Eğitim
### Çok Modlu Eğitim Verileri
| Veri Kümesi | Modaliteler | Boyut |
|-----------|-----------|------|
| **LAION-5B** | Resim-metin çiftleri | 5,85 milyar çift |
| **DataComp** | Seçilmiş resim metni | Veri kümesi tasarımı için karşılaştırma noktası |
| **WIT** (Wikipedia) | Wikipedia'dan resim metni | 11,5 milyon çift |
| **Nasıl Yapılır100M** | Video metni (nasıl yapılır videoları) | 100 milyon klip |
| **LibriSpeech** | Konuşma metni | 1.000 saat İngilizce |
| **Ortak Ses** | Konuşma metni | Çok dilli; topluluk katkılı |
### Eğitim Stratejileri
| Strateji | Açıklama | Ne Zaman Kullanılmalı |
|----------|----------------|------------|
| **Ortak eğitim** | Tüm yöntemler üzerinde aynı anda eğitim alın | Çok modlu verileri hizaladığınızda |
| **Müfredat öğrenimi** | Kolay örneklerle başlayın; zorluğu arttır | Yakınsamayı iyileştirir |
| **Karşılaştırmalı öğrenme** | İlgili çiftleri modaliteler arasında eşleştirmeyi öğrenin (CLIP stili) | Paylaşılan temsiller oluşturmak |
| **Talimat ayarlama** | Çok modlu talimat-yanıt çiftleri üzerine eğitim | Modellerin çok modlu talimatları takip etmesini sağlamak |
---

## Değerlendirme
| Karşılaştırma | Modaliteler | Neyi Test Ediyor |
|-----------|---------------|---------------|
| **MMLU** | Metin | 57 konu genelinde bilgi |
| **MMMU** | Metin + resimler | Diyagramlarla üniversite düzeyinde akıl yürütme |
| **MatematikVista** | Metin + resimler | Görsel verilerle matematiksel akıl yürütme |
| **Video-MME** | Metin + video | Videoyu anlama ve zamansal akıl yürütme |
| **KASK** | Metin + ses | Uzun bağlamlı çok modlu değerlendirme |
| **SWE tezgahı** | Metin + kod | Gerçek dünyadaki yazılım mühendisliği görevleri |
---

## Özet
Çok modlu yapay zeka, tek amaçlı modellerden tüm veri türlerini algılayan ve mantık yürüten sistemlere geçişi temsil eder. GPT-4V ve Gemini gibi görüş dili modelleri, görselleri ve metni birlikte anlayabilir; Whisper ve VALL-E gibi konuşma modelleri sesi yönetir; video modelleri, sesli hareketli görüntülerin tüm karmaşıklığını işlemeye başlıyor. Trend açık: Geleceğin en yetenekli yapay zeka sistemleri, doğal olarak çok modlu olacak ve her tür bilgiyi aynı anda işleyecek. Veri hizalama, hesaplama maliyeti, değerlendirme ve somutlaştırılmış dağıtım gibi zorluklar önemlidir, ancak 2024-2026'daki ilerleme hızlı olmuştur.