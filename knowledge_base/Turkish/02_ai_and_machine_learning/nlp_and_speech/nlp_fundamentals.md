---
# Metadata
title: "NLP Fundamentals"
description: "Text processing, embeddings, Transformers, BERT, GPT"
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
tags: [nlp, ai-and-machine-learning]
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
# NLP'nin Temelleri
Doğal Dil İşleme (NLP), makinelere insan dilini anlamayı, üretmeyi ve onunla çalışmayı öğretme alanıdır. Arama motorlarına, sohbet robotlarına, çeviri sistemlerine, duyarlılık analizine ve 2020'den bu yana yapay zekayı dönüştüren büyük dil modellerine (LLM'ler) güç sağlar. Bu dosya, klasik tekniklerden modern Transformer tabanlı mimarilere kadar olan evrimi kapsar.
---

## Metin Ön İşleme
Ham metin dağınık. Bir modelin onu kullanabilmesi için önce temizlenmesi ve yapılandırılması gerekir.
| Adım | Ne İşe Yarar | Örnek |
|------|-------------|--------|
| **Tokenizasyon** | Metni belirteçlere (kelimelere, alt sözcüklere veya karakterlere) bölme | "NLP'yi seviyorum" →`["I", "love", "NLP"]`|
| **Küçük harfler** | Küçük harfe dönüştür | "Merhaba" → "merhaba" |
| **Kelime kaldırmayı durdur** | Yaygın kelimeleri kaldırın (the, is, at) | "kedi oturdu" → "kedi oturdu" |
| **Köklenme** | Kelime sonlarını doğrayın (kaba) | "çalışıyor" → "koşuyor" |
| **Lemmatizasyon** | Sözlük biçimine azaltın (bağlama duyarlı) | "daha iyi" → "iyi" |
| **Normalleşme** | Kodlamayı düzeltin, özel karakterleri kaldırın, kısaltmaları genişletin | "yapma" → "yapma" |
Modern Transformer modelleri genellikle durdurulan sözcüklerin kaldırılmasını ve köklerini belirlemeyi atlar; bu kalıpları verilerden öğrenirler.
---

## Metin Gösterimi
Makinelerin kelimelere değil sayılara ihtiyacı vardır. Metni vektör olarak nasıl temsil ettiğimiz esastır.
### Klasik Yaklaşımlar
| Yöntem | Açıklama | Sınırlama |
|----------|----------------|-----------|
| **Tek-Hot Kodlama** | Her kelime büyük bir vektörde benzersiz bir konumdur | Seyrek; anlamsal anlamı yok |
| **Kelime Torbası (BoW)** | Kelime frekanslarını sayın; siparişi görmezden gel | Kelime sırasını tamamen kaybediyor |
| **TF-IDF** | Kelimelerin belgedeki sıklığa göre ağırlığı × tümcedeki nadirlik | Sırayı ve bağlamı hâlâ yok sayıyor |
### Kelime Gömmeleri
Gömmeler, kelimeleri benzer kelimelerin birbirine yakın olduğu yoğun vektörlerle eşleştirir.
| Modeli | Anahtar Fikir |
|----------|----------|
| **Word2Vec** (2013) | Kelimeyi bağlamdan (CBOW) veya bağlamı kelimeden (Skip-gram) tahmin edin |
| **Eldiven** (2014) | Küresel birlikte oluşum istatistikleri → yoğun vektörler |
| **Hızlı Metin** (2016) | Word2Vec + alt kelime bilgisi (nadir kelimeleri daha iyi işler) |
Ünlü örnek:`king - man + woman ≈ queen`. Gömmeler anlamsal ilişkileri yakalar.
**Sınırlama**: Klasik yerleştirmeler kelime başına bir vektör atar, bu nedenle çokanlamlılıkla (çok anlamlı kelimeler) başa çıkamazlar. "Nehir bankası" ve "banka hesabı" içindeki "banka" aynı vektörü alır.
---

## Sıra Modelleri
Transformers'tan önce NLP'nin standart yaklaşımı metni sırayla işlemekti.
| Mimarlık | Nasıl Çalışır | Güç | Zayıflık |
|---------------|---------------|----------|----------|
| **RNN** | Belirteçleri birer birer işleyin; gizli durumu koru | Değişken uzunluklu girişi yönetir | Kaybolan degradeler; uzun bağımlılıklar yakalanamıyor |
| **LSTM** | Bilgi akışını kontrol etmek için kapılı (unutma, giriş, çıkış) RNN | Uzun vadeli bağımlılıklarda daha iyi | Hala sıralı; yavaş eğitim |
| **GRU** | Basitleştirilmiş LSTM (daha az kapı) | LSTM'den daha hızlı; benzer performans | Aynı temel sınırlamalar |
Bu modeller metni soldan sağa işler; bu da eğitilmelerinin yavaş olduğu (paralelleştirilemediği) ve uzun vadeli bağımlılıklarla mücadele ettikleri anlamına gelir.
---

## Dikkat Mekanizması
Dikkat, bir modelin bir sıradaki tüm konumlara aynı anda bakmasına ve hangilerinin mevcut tahminle en alakalı olduğuna karar vermesine olanak tanır.
### Temel Bilgi
Dikkat, tüm cümleyi tek bir gizli duruma sıkıştırmak yerine (RNN'lerin yaptığı gibi), ağırlıkların öğrenildiği tüm gizli durumların ağırlıklı toplamını hesaplar.
```
Attention(Q, K, V) = softmax(QK^T / √d_k) V
```

| Bileşen | Rol |
|-----------|------|
| **Sorgu (S)** | Ne arıyorum? |
| **Anahtar (K)** | Neyi içeriyorum? |
| **Değer (V)** | Hangi bilgileri veriyorum? |
| **√d_k** | Büyük noktalı ürünleri önlemek için ölçeklendirme faktörü |
---

## Transformatör Mimarisi
Transformer (Vaswani ve diğerleri, 2017 — "İhtiyacınız Olan Tek Şey Dikkat") yinelemeyi tamamen dikkatle değiştirdi. Neredeyse tüm modern NLP'nin temelidir.
### Mimarlık
| Bileşen | Açıklama |
|-----------|----------------|
| **Kodlayıcı** | Giriş metnini okur; bağlamsal temsiller üretir |
| **Kod çözücü** | Çıkış metnini oluşturur; kodlayıcı çıkışıyla ilgilenir |
| **Kişisel Dikkat** | Her jeton diğer tüm jetonlarla aynı sırayla ilgilenir |
| **Çok Kafalı Dikkat** | Birden fazla dikkat kafasını paralel olarak çalıştırın; farklı ilişkileri yakalayın |
| **Konumsal Kodlama** | Konum bilgisini enjekte edin (yineleme olmadığından) |
| **İleri Besleme Ağı** | Her pozisyona bağımsız olarak uygulanır |
| **Katman Normalleştirme** | Stabilizasyon eğitimi |
| **Artık Bağlantılar** | Degrade akışı için bağlantıları atla |
### Yalnızca Kodlayıcı, Yalnızca Kod Çözücü, Kodlayıcı-Kod Çözücü
| Varyant | Mimarlık | En İyisi | Örnekler |
|-----------|---------------|----------|-----------|
| **Yalnızca kodlayıcı** | Metni anlar | Sınıflandırma, NER, duyarlılık analizi | BERT, RoBERTa, DeBERTa |
| **Yalnızca kod çözücü** | Metin oluşturur | Dil modelleri, sohbet robotları, kod oluşturma | GPT-3/4, LLaMA, Claude |
| **Kodlayıcı-Kod Çözücü** | Metni dönüştürür | Çeviri, özetleme | T5, BART, mBART |
---

## Başlıca Model Aileler
### BERT Ailesi (Yalnızca Kodlayıcı)
| Modeli | Temel Özellik |
|----------|----------------|
| **BERT** (2018) | Maskelenmiş Dil Modeli + Sonraki Cümle Tahmini |
| **RoBERTa** | NSP kaldırıldı; daha fazla veriyle daha uzun süre eğitildi |
| **ALBERT** | Parametre paylaşımı; daha küçük ayak izi |
| **DeBERTa** | Çözülmüş dikkat; geliştirilmiş NLU |
| **DistilBERT** | %40 daha küçük, %60 daha hızlı, BERT'in performansının %97'sini koruyor |
### GPT Ailesi (Yalnızca Kod Çözücü)
| Modeli | Parametreler | Notlar |
|----------|---------------|----------|
| **GPT-2** | 1.5B | Gösterilen yalnızca kod çözücü modelleri tutarlı metin oluşturabilir |
| **GPT-3** | 175B | Birkaç adımda öğrenme; ince ayar yapmak yerine istemde bulunuldu |
| **GPT-3.5 / GPT-4** | Açıklanmadı | Talimat ayarlı + RLHF; konuşkan |
| **LLaMA** (Meta) | 7B–70B | Açık ağırlık; açık kaynak LLM ekosistemini ortaya çıkardı |
| **Mistral / Mixtral** | 7B / 8×7B (MEB) | Güçlü performansa sahip verimli açık modeller |
---

## Temel NLP Görevleri
| Görev | Açıklama | Tipik Model |
|------|-------------|-------------|
| **Metin Sınıflandırması** | Metne bir etiket atama (spam/spam değil, pozitif/negatif) | BERT, ince ayarlı sınıflandırıcılar |
| **Adlandırılmış Varlık Tanıma (NER)** | Metindeki kişileri, kuruluşları ve yerleri tanımlayın | BERT + CRF katmanı |
| **Duygu Analizi** | Duygusal tonunuzu belirleyin | İnce ayarlı BERT veya sıfır atışlı LLM |
| **Makine Çevirisi** | Diller arasında çeviri | T5, mBART, MarianMT |
| **Soru Yanıtlama** | Bağlam verilen soruları yanıtlayın | BERT (çıkarıcı), GPT (üretken) |
| **Özetleme** | Uzun metni yoğunlaştır | T5, BART, GPT |
| **Metin Oluşturma** | Tutarlı metin üretin | GPT-4, LLaMA, Claude |
---

## İnce Ayarlama ve İsteme Karşılaştırması
| Yaklaşım | Nasıl Çalışır | Ne Zaman Kullanılmalı |
|----------|----------------|------------|
| **İnce ayar** | Göreve özel verilerinizdeki model ağırlıklarını güncelleyin | Verileri etiketlediniz; maksimum performansa ihtiyacınız var |
| **İsteyen** | Model talimatlarını doğal dilde verin | Hızlı prototipleme; sınırlı veri; Yüksek Lisans'ı kullanma |
| **Birkaç atış** | Komut istemine örnekler ekleyin | Birkaç örneğiniz olduğu halde ince ayar için yeterli olmadığında |
| **LoRA / QLoRA** | Verimli ince ayar; küçük düşük dereceli matrisleri güncelleme | Sınırlı GPU belleğiyle büyük modellere ince ayar yapın |
---

## Araçlar ve Çerçeveler
| Araç | Amaç |
|------|------------|
| **Transformers'ı kucaklayan yüz** | Önceden eğitilmiş modeller, belirteçler, ince ayar ardışık düzenleri |
| **SpaCy** | Üretim düzeyinde NLP boru hattı (tokenleştirme, NER, POS, bağımlılık) |
| **NLTK** | Eğitimsel; klasik NLP algoritmaları |
| **Gensim** | Konu modelleme (LDA), kelime yerleştirmeler (Word2Vec, Doc2Vec) |
| **LangChain / LlamaIndex** | Yüksek Lisans destekli uygulamalar oluşturmaya yönelik çerçeveler |
| **vLLM** | Yüksek verimli LLM sunumu |
| **Tokenlaştırıcılar (HF)** | Hızlı tokenizasyon (BPE, WordPiece, SentencePiece) |
---

## Yüksek Lisans Ortamı
Modern NLP ortamına Büyük Dil Modelleri hakimdir:
| Kategori | Örnekler | Notlar |
|----------|------------|-------|
| **Tescilli** | GPT-4, Claude, İkizler | En iyi performans; Yalnızca API erişimi |
| **Açık ağırlık** | LLaMA 3, Mistral, Qwen | Mevcut ağırlıklar; yerel olarak çalıştır |
| **Açık kaynak** | Pythia, OPT | Tamamen açık (veriler, ağırlıklar, kod) |
| **Çok modlu** | GPT-4V, İkizler, LLaVA | Metin + görselleri işle |
| **Kod uzmanlığı** | CodeLlama, StarCoder, DeepSeek Kodlayıcı | Kod eğitimi |
| **Küçük / Verimli** | Phi-3, Gemma, TinyLlama | Küçük ölçekte güçlü performans |
Saha hızla ilerliyor. Bugün en ileri teknoloji, birkaç ay içinde geçerliliğini yitirebilir. Temel unsurlar (dikkat, tokenizasyon, ince ayar, değerlendirme) istikrarlı kalıyor.