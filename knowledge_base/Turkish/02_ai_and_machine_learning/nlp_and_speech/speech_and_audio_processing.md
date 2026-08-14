<!--
---
# Metadata
title: "Speech and Audio Processing"
description: "ASR, TTS, audio features, Whisper, speech pipelines"
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
tags: [speech, audio, processing, ai-and-machine-learning]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "9 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Konuşma ve Ses İşleme
Konuşma ve ses işleme, makinelerin sesi duymasını, anlamasını, üretmesini ve değiştirmesini sağlayan teknolojileri kapsar. Bu, konuşma tanımayı (konuşulan kelimeleri metne dönüştürme), konuşma sentezini (metni konuşulan kelimelere dönüştürme), konuşmacıyı tanımlamayı, müzik üretmeyi ve çevresel ses anlayışını içerir. Alan, derin öğrenmeyle dönüşüme uğradı; modern sistemler, konuşma tanıma için insan düzeyindeki doğruluğa yaklaşıyor ve ürkütücü derecede doğal sentetik sesler üretiyor.
---

## Dijital Sesin Temelleri
Ses bir basınç dalgasıdır. Dijital olarak işlemek için dalgayı düzenli aralıklarla örnekliyoruz.
| Konsept | Açıklama | Tipik Değer |
|-----------|---------------|---------------|
| **Örnek oranı** | Ses saniyede kaç kez ölçülür | 8 kHz (telefon), 16 kHz (konuşma), 44,1 kHz (CD), 48 kHz (profesyonel) |
| **Bit derinliği** | Her numunenin hassasiyeti | 16 bit (CD), 24 bit (profesyonel), 32 bit kayan nokta (işleme) |
| **Kanallar** | Mono (1), stereo (2), surround (5.1, 7.1) | Müzik için stereo; konuşma için mono |
| **Süre** | Sesin uzunluğu | Değişir |
16 kHz'de 1 dakikalık mono kayıt, 16 bit = 1,92 MB. 44,1 kHz'de 3 dakikalık stereo şarkı, 16 bit = 30,3 MB.
---

## Ses Özelliği Çıkarma
Ham ses dalga formlarıyla modellerin doğrudan çalışması zordur. Sesin önemli özelliklerini yakalayan özellikleri çıkarıyoruz.
| Özellik | Ne Yakalar | Kullanım Örneği |
|-----------|----------|----------|
| **Mel spektrogramı** | Zaman içindeki frekans içeriği, insan işitme algısıyla eşleştirildi | Konuşma tanıma, müzik sınıflandırması |
| **MFCC** (Mel-Frekans Cepstral Katsayıları) | Spektral zarfın kompakt gösterimi | Geleneksel konuşma tanıma |
| **Kromagram** | Perde sınıfı dağılımı (hangi notaların çaldığı) | Müzik analizi, akor algılama |
| **Sıfır geçiş oranı** | Sinyal sıfırı ne sıklıkta geçer | Sesli ve sessiz algılama |
| **RMS enerjisi** | Zaman içindeki sinyal yüksekliği | Ses etkinliği algılama |
| **Aralık (F0)** | Temel frekans | Konuşmacı tanımlama, müzik transkripsiyonu |
### Mel Spektrogramı
Derin öğrenme için en yaygın ses temsili. Sesi 2 boyutlu görüntü benzeri bir formata dönüştürür:
| Eksen | Temsil eder |
|------|---------------|
| **X ekseni** | Zaman |
| **Y ekseni** | Frekans (Mel ölçeğinde — algısal olarak aralıklı) |
| **Renk/yoğunluk** | Bu frekans ve zamandaki enerji |
Mel ölçeği insan işitmesine yakındır: Düşük frekansları ayırt etmede yüksek frekanslardan daha iyiyiz.
---

## Otomatik Konuşma Tanıma (ASR)
ASR konuşulan dili metne dönüştürür. Ses yapay zekasının ticari açıdan en önemli uygulamalarından biridir.
### ASR'nin Evrimi
| Çağ | Yaklaşım | Sınırlama |
|-----|----------|---------------|
| **2010 Öncesi** | Gizli Markov Modelleri + Gauss Karışım Modelleri | Kapsamlı el mühendisliği gerektiriyordu; gürültülü koşullarda kötü |
| **2010-2015** | DNN-HMM hibrit | Sinir ağları GMM'lerin yerini aldı; önemli gelişme |
| **2015-2020** | Uçtan uca modeller (Derin Konuşma, LAS) | Sesten metne tek sinir ağı |
| **2020+** | Trafo Tabanlı (Whisper, Conformer) | En gelişmiş doğruluk; çok dilli; sağlam |
### Önemli ASR Modelleri
| Modeli | Mimarlık | Eğitim Verileri | Önemli Özellik |
|----------|----------------|---------------|------|
| **Fısıltı** (OpenAI) | Kodlayıcı-kod çözücü Transformatörü | 680.000 saat, 99 dil | Çok dilli; vurgulara ve gürültüye karşı dayanıklı; açık kaynak |
| **Uyumlu** | Evrişim + kendine dikkat | Çeşitli | Yerel (dönüşüm) ve küresel (dikkat) özellikleri birleştirir |
| **wav2vec 2.0** | Kendinden Denetimli Trafo | Etiketsiz konuşma | Transkripsiyon olmadan ham sesten öğrenir |
| **USM** (Google) | Evrensel konuşma modeli | 2 milyon saat, 300'den fazla dil | Çoğu dil kapsanmaktadır |
| **MMS** (Meta) | Devasa Çok Dilli Konuşma | 1.400+ dil | Kapsamı düşük kaynaklı dilleri kapsayacak şekilde genişletiyor |
### ASR Metrikleri
| Metrik | Açıklama |
|----------|----------------|
| **WER** (Kelime Hata Oranı) | Yanlış yazılan kelimelerin yüzdesi. Daha düşük olması daha iyidir. Temiz İngilizce için insan performansı ~%4-5'tir. |
| **CER** (Karakter Hata Oranı) | WER ile aynı ancak karakter düzeyinde. Kelime sınırları olmayan diller (Çince, Japonca) için kullanılır. |
### Yaygın ASR Zorlukları
| Mücadelesi | Açıklama |
|-----------|----------------|
| **Aksanlar ve lehçeler** | Standart dışı vurgularda performans önemli ölçüde düşüyor |
| **Arka plan gürültüsü** | Müzik, trafik ve diğer hoparlörler doğruluğu azaltır |
| **Kod değiştirme** | Konuşmacılar cümlenin ortasında diller arasında geçiş yapıyor |
| **Homofonlar** | "Orada", "onların" ve "onlar" — bağlam gerektirir |
| **Noktalama işaretleri ve biçimlendirme** | ASR çıktısı genellikle noktalama işaretsizdir; son işleme ihtiyacı var |
| **Düşük kaynaklı diller** | Çoğu model, çok az eğitim verisine sahip diller için düşük performans gösteriyor |
---

## Metinden Konuşmaya (TTS)
TTS yazılı metni sözlü sese dönüştürür. Modern sistemler genellikle insan kayıtlarından ayırt edilemeyen konuşmalar üretir.
### TTS'nin Evrimi
| Çağ | Yaklaşım | Kalite |
|-----|----------|-----------|
| **2010 Öncesi** | Birleştirici (kaydedilen parçaların birleştirilmesi) | Robotik; sınırlı ifade gücü |
| **2010-2017** | İstatistiksel parametrik (HMM'ler, erken sinirsel) | Daha iyi ama yine de sentetik olarak tanınabilir |
| **2017-2020** | Sinirsel (Tacotron, WaveNet) | İnsana yakın kalite; etkileyici |
| **2020+** | Sinir codec'i (VALL-E, Bark) | Ses klonlama; birkaç atış; son derece doğal |
### Temel TTS Modelleri
| Modeli | Mimarlık | Önemli Özellik |
|----------|----------------|------|
| **WaveNet** (DeepMind) | Otoregresif üretken model | İlk gerçekten doğal ses veren TTS |
| **Tacotron 2** (Google) | Seq2seq + ses kodlayıcı | Uçtan uca; yüksek kalite |
| **VITS** | Varyasyonel çıkarım + çekişmeli eğitim | Hızlı; kaliteli; yaygın olarak kullanılan |
| **VALL-E** (Microsoft) | Sinir kodlayıcı dil modeli | 3 saniyelik örnekten ses klonlama |
| **Havlama** (Suno) | Trafo tabanlı | Çok dilli; konuşma dışı sesler (kahkahalar, müzik) |
| **ElevenLabs** | Ticari | Sektör lideri ses klonlama |
| **SohbetTTS** | Açık kaynak | Konuşma konuşması için optimize edildi |
| **Balık Konuşması** | Açık kaynak | Hızlı; çok dilli |
### Ses Klonlama
Ses klonlama, kısa bir ses örneğinden belirli bir kişiye benzeyen sentetik bir ses oluşturur.
| Yöntem | Gerekli Veriler | Kalite |
|----------|---------------|-----------|
| **İnce ayar** | 10-60 dakika konuşma | Yüksek kalite; konuşmacıya özel |
| **Birkaç atış** | 3-30 saniyelik konuşma | Kaliteli; hızlı kurulum |
| **Sıfır atış** | Hedef konuşmacı verisi yok | Çıkarım anında referans sesi kullanır |
**Etik kaygı**: Ses klonlama; kimliğe bürünme, sahtekarlık ve deepfake amacıyla kullanılabilir. Çoğu ticari sağlayıcı sesli onay gerektirir.
---

## Konuşmacı Tanıma
| Görev | Açıklama | Başvuru |
|------|-------------|------------|
| **Konuşmacı doğrulaması** | "Bu iddia ettikleri kişi mi?" | Telefon bankacılığı, cihaz kilidini açma |
| **Konuşmacı tanımlama** | "Kim konuşuyor?" | Toplantı transkripsiyonu, adli tıp |
| **Konuşmacı günlüğü** | "Kim ne zaman konuştu?" (çok hoparlörlü ses modunda) | Toplantı özetleri, alt başlık oluşturma |
| Modeli | Yaklaşım |
|----------|----------|
| **ECAPA-TDNN** | Gömme tabanlı; doğrulama için son teknoloji |
| **d-vektör** | DNN'den basit hoparlör yerleştirmeleri |
| **x-vektör** | Geliştirilmiş hoparlör yerleştirmeleri; yaygın olarak kullanılan |
---

## Müzik Bilgisine Erişim
| Görev | Açıklama | Araçlar/Modeller |
|------|-------------|------------|
| **Müzik transkripsiyonu** | Sesi notalara / MIDI'ye dönüştürün | Spotify Temel Konuşma, Spleeter |
| **Kaynak ayrımı** | Bireysel enstrümanları veya vokalleri izole edin | Demucs, Spleeter, Müzik Kaynağı Ayırma |
| **Tür sınıflandırması** | Müziği türe göre kategorilere ayırın | Spektrogramlarda CNN'ler |
| **Vuruş takibi** | Tempoyu ve vuruş pozisyonlarını tespit edin | Librosa, Madmom |
| **Akor tanıma** | Müzikteki akorları tanımlama | Akor-CNN, CRF modelleri |
| **Müzik üretimi** | Yeni müzik yaratın | MusicGen, MuseNet, AIVA |
---

## Çevresel Ses Algılama
| Görev | Açıklama | Başvuru |
|------|-------------|------------|
| **Ses olayı algılama** | Ortamdaki sesleri tanımlama | Akıllı ev (cam kırma, bebek ağlaması) |
| **Akustik sahne sınıflandırması** | Ortamı sınıflandırın (ofis, park, trafik) | Bağlama duyarlı cihazlar |
| **Anormallik tespiti** | Olağandışı sesleri tespit edin | Endüstriyel izleme (makineæ•…éšœ) |
| Veri Kümesi | Sesler | Boyut |
|-----------|-----------|------|
| **Ses Seti** | 632 ses sınıfı | 2 milyondan fazla YouTube klibi |
| **ESC-50** | 50 çevresel ses sınıfı | 2.000 klip |
| **UrbanSound8K** | Kentsel sesler | 8.732 klip |
---

## Araçlar ve Çerçeveler
| Araç | Amaç |
|------|------------|
| **Librosa** | Ses analizi için Python kütüphanesi (özellikler, efektler, görselleştirme) |
| **Pydub** | Basit ses işleme (kesme, birleştirme, dışa aktarma) |
| **FFmpeg** | Komut satırı ses/video işleme (İsviçre Çakısı) |
| **Meşale sesi** | PyTorch ses işleme (dönüştürür, veri kümeleri, modeller) |
| **Sarılma Yüzü (transformatörler)** | Önceden eğitilmiş ASR ve TTS modelleri |
| **Fısıltı (OpenAI)** | Konuşma tanıma (açık kaynak) |
| **Coqui TTS** | Açık kaynaklı TTS araç seti |
| **Demucs** | Müzik kaynağı ayrımı |
| **SpeechBrain** | Hepsi bir arada konuşma araç seti (ASR, TTS, konuşmacı tanıma) |
---

## Pratik İpuçları
- **Her zaman verilerinizi dinleyin.** Herhangi bir şeyi eğitmeden önce örnek sesi dinleyin. Örnekleme hızına, gürültü düzeyine ve hoparlör özelliklerine dikkat edin.
- **Örnekleme hızlarını eşleştirin.** Whisper 16 kHz bekliyor. Sesiniz 44,1 kHz ise yeniden örnekleyin; ancak alt örneklemenin bilgi kaybına yol açacağını unutmayın.
- **Ses verilerini artırın.** Arka plan gürültüsü ekleyin, hızı ve perdeyi değiştirin, farklı mikrofonları simüle edin. Bu, sağlamlığı önemli ölçüde artırır.
- **Önceden eğitilmiş modelleri kullanın.** ASR için Whisper ve TTS için VITS/Bark mükemmel başlangıç ​​noktalarıdır. İnce ayar neredeyse her zaman sıfırdan eğitimden daha iyidir.
- **Sessizliği yönetin.** Ses Etkinliği Algılama (VAD), işlemden önce sessizliği ortadan kaldırır, bilgi işlemden tasarruf sağlar ve doğruluğu artırır. Silero VAD ve WebRTC VAD popüler seçimlerdir.
- **Ses seviyesini normalleştirin.** Farklı kayıtların çok farklı ses yüksekliği seviyeleri vardır. İşlemeden önce tutarlı bir seviyeye normalleştirin.
---

## Özet
Konuşma ve ses işlemede derin öğrenme devrim yarattı. Whisper gibi modern ASR sistemleri düzinelerce dilde insan düzeyinde doğruluğa yaklaşıyor. TTS sistemleri, insan kayıtlarından giderek ayırt edilemeyen konuşmalar üretir. Ses klonlama, saniyeler süren sesten itibaren çalışır. Müzik üretimi, kaynak ayırma ve çevresel ses algılama hızla gelişiyor. Bu alan, düşük kaynaklı diller, gürültülü ortamlar, ses klonlamayla ilgili etik kaygılar gibi devam eden zorluklarla karşı karşıyadır, ancak gidişat açıktır: makineler, sesi duyma, anlama ve üretme konusunda insanlar kadar iyi hale gelmektedir.