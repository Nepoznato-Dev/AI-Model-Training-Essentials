---
# Metadata
title: "Graph Neural Networks"
description: "GCNs, GATs, message passing, knowledge graphs, graph tasks"
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
tags: [graph, neural, networks, ai-and-machine-learning]
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
# Sinir Ağlarının Grafikleri
Grafik Sinir Ağları (GNN'ler), grafik yapılı veriler (kenarlarla birbirine bağlanan düğüm ağları) üzerinde çalışmak üzere tasarlanmış sinir ağlarıdır. Geleneksel sinir ağları ızgaralar (görüntüler) veya diziler (metin) üzerinde çalışırken, GNN'ler keyfi ilişkisel yapıları yönetir: sosyal ağlar, moleküler grafikler, bilgi grafikleri, yol ağları, öneri grafikleri ve daha fazlası. İlaç keşfi, sahtekarlık tespiti, öneri sistemleri ve kuruluşlar arasındaki ilişkilerin önemli olduğu herhangi bir alan için vazgeçilmez hale geldiler.
---

## Grafik Nedir?
| Bileşen | Açıklama | Örnek |
|-----------|----------------|-----------|
| **Düğüm (tepe noktası)** | Bir varlık | Bir insan, bir molekülün atomu, bir şehir |
| **Kenar** | İki düğüm arasındaki ilişki | Dostluk, kimyasal bağ, yol |
| **Kenar ağırlığı** | İlişkinin gücü veya türü | Mesafe, benzerlik, kapasite |
| **Düğüm özellikleri** | Her düğümün özellikleri | Yaş, atom numarası, nüfus |
| **Kenar özellikleri** | Her kenarın özellikleri | İlişki türü, mesafe |
| **Bitişiklik matrisi** | Matris A burada A[i][j] = 1, eğer i ve j düğümleri bağlıysa | Grafik yapısını kodlar |
### Grafik Türleri
| Tür | Açıklama | Örnek |
|------|-------------|--------|
| **Yönlendirilmemiş** | Kenarların yönü yoktur | Arkadaşlık ağı |
| **Yönetilmiş** | Kenarların yönü vardır (A→B ≠ B→A) | Twitter takipçileri |
| **Ağırlıklı** | Kenarların sayısal değerleri vardır | Mesafeli yol ağı |
| **Heterojen** | Çoklu düğüm ve kenar türleri | Akademik grafik (makaleler, yazarlar, mekanlar) |
| **Dinamik** | Grafik yapısı zamanla değişir | Zamanla gelişen sosyal ağ |
| **İki parçalı** | İki tür düğüm; yalnızca türler arasındaki kenarlar | Kullanıcı öğesi öneri grafiği |
---

## Neden Düzenli Sinir Ağları Değil?
| Yaklaşım | Neden Başarısız?
|----------|----------------|
| **İleri beslemeli ağ** | Sabit boyutlu giriş gerektirir; grafiklerin boyutu ve yapısı farklılık gösterir |
| **CNN** | Izgara yapısını varsayar; grafiklerin düzenli bir ızgarası yoktur |
| **RNN/Transformatör** | Sıralı sırayı varsayar; grafiklerin doğal sıralaması yoktur |
GNN'ler bunu doğrudan grafik yapısı üzerinde çalışarak, her düğümü komşuları bağlamında işleyerek çözer.
---

## Temel GNN Mimarileri
### Mesaj Aktarma Çerçevesi
Çoğu GNN aynı modeli izler: her düğüm komşularından bilgi toplar, bunları birleştirir ve kendi temsilini günceller.
| Adım | Açıklama |
|------|-----------------|
| **1. Mesaj** | Her düğüm komşularına bir mesaj gönderir (mevcut özelliklerine göre) |
| **2. Toplam** | Her düğüm tüm komşulardan gelen mesajları toplar ve birleştirir |
| **3. Güncelleme** | Her düğüm, birleştirilmiş mesajı kullanarak kendi gösterimini günceller |
| **4. Tekrarla** | Bunu K katman için yapın → her düğüm K atlama uzaklığından bilgi yakalar |
### Temel GNN Modelleri
| Modeli | Toplama Yöntemi | Temel Yenilik |
|----------|-----------|----------------|
| **GCN** (Grafik Evrişimli Ağ) | Komşu özelliklerinin ortalaması | Basit; etkili; spektral motivasyon |
| **GrafikSAGE** | Örnek ve toplu; ortalama, LSTM veya havuzlama kullanılabilir | Endüktif (görünmeyen düğümleri yönetir); ölçeklenebilir |
| **GAT** (Grafik Dikkat Ağı) | Dikkat ağırlıklı komşu toplama | Hangi komşuların en önemli olduğunu öğrenir |
| **CİN** (Grafik İzomorfizm Ağı) | Komşu özelliklerinin toplamı | Maksimum derecede etkileyici; WL testiyle ayırt edilebilen herhangi bir grafiği ayırt edebilir |
| **MPNN** (Mesaj Aktaran Sinir Ağı) | Genel mesaj aktarma çerçevesi | Birçok GNN çeşidini birleştirir |
### GCN Nasıl Çalışır (Adım Adım)
```
For each layer:
  1. For each node, collect features from all neighbours
  2. Multiply by a learnable weight matrix W
  3. Normalise by node degree (so high-degree nodes don't dominate)
  4. Apply non-linearity (ReLU)
  5. This becomes the node's new representation
```

K katmandan sonra, her düğümün temsili, grafikteki K atlamadan gelen bilgiyi kodlar.
---

## Grafik Düzeyinde Görevler
| Görev | Açıklama | Örnek |
|------|-------------|--------|
| **Düğüm sınıflandırması** | Her düğümün etiketini tahmin edin | Kullanıcıları bot veya insan olarak sınıflandırın |
| **Bağlantı tahmini** | Bir kenarın var olup olmadığını (veya var olacağını) tahmin edin | Eksik ilişkileri tahmin edin; bağlantı tavsiyesi |
| **Grafik sınıflandırması** | Grafiğin tamamı için bir etiket tahmin edin | Molekülleri toksik veya toksik olmayan olarak sınıflandırın |
| **Topluluk tespiti** | Yoğun şekilde bağlı düğüm kümelerini bulun | Sosyal grupları tanımlayın |
| **Grafik oluşturma** | İstenilen özelliklere sahip yeni grafikler oluşturun | Yeni moleküller tasarlayın |
---

## Uygulamalar
### İlaç Keşfi ve Moleküler Özellik Tahmini
| Görev | GNN'ler Nasıl Yardım Ediyor |
|------|-----------------|
| **Moleküler özellik tahmini** | Molekülleri grafiklerle temsil edin (atomlar=düğümler, bağlar=kenarlar); toksisiteyi, çözünürlüğü ve bağlanma afinitesini tahmin etme |
| **İlaç-ilaç etkileşimi** | İlaçları ve hedefleri grafik olarak modelleyin; Olumsuz etkileşimleri tahmin edin |
| **De novo ilaç tasarımı** | İstenilen özelliklere sahip yeni moleküler grafikler oluşturun |
### Öneri Sistemleri
| Yaklaşım | Açıklama |
|----------|----------------|
| **Kullanıcı öğesi grafiği** | Kullanıcılar ve öğeler düğümlerdir; satın almalar/görüntülemeler kenarlardır |
| **Grafik tabanlı işbirliğine dayalı filtreleme** | GNN'ler tercihleri ​​grafik aracılığıyla yayar |
| **Bilgi grafiği önerileri** | Kullanıcı tercihlerini öğe bilgisiyle birleştirin (türler, aktörler, yönetmenler) |
### Dolandırıcılık Tespiti
| Başvuru | Grafik Yapısı |
|---------------|----------------|
| **Mali dolandırıcılık** | İşlemler bir grafik oluşturur; sahte kalıplar alt grafik yapıları olarak ortaya çıkıyor |
| **Sigorta dolandırıcılığı** | Talep sahipleri, sağlayıcılar ve politikalar bir grafik oluşturur; Dolandırıcı çeteleri tespit edildi |
| **Hesap devralmaları** | Oturum açma kalıpları bir grafik oluşturur; anormal bağlantılar sinyal ihlaline neden oluyor |
### Bilgi Grafikleri
| Görev | Açıklama |
|------|-----------------|
| **Bağlantı tahmini** | Eksik bilgileri tahmin edin (örneğin, "Paris başkentidir?") |
| **Varlık çözümü** | İki bahsin aynı varlığa atıfta bulunup bulunmadığını belirleyin |
| **Soru yanıtlama** | Yanıtları bulmak için grafikte gezinin |
---

## Gelişmiş GNN Kavramları
### Aşırı Yumuşatma
| Sorun | Açıklama | Çözüm |
|-----------|---------------|----------|
| **Aşırı yumuşatma** | Birçok katmandan sonra tüm düğüm gösterimleri benzer hale gelir | Sınır derinliği (2-4 katman); artık bağlantıları kullanın; Zıplama Bilgisini Kullan |
### Aşırı Ezme
| Sorun | Açıklama | Çözüm |
|-----------|---------------|----------|
| **Aşırı ezme** | Uzak düğümlerden gelen bilgiler sabit boyutlu vektörlere sıkıştırılır | Grafik transformatörlerini kullanın; hiyerarşik havuzlama |
### Grafik Transformatörleri
| Modeli | Temel Özellik |
|----------|----------------|
| **Grafik Transformatörü** | Tüm düğüm çiftlerine standart Transformer dikkatini uygulayın |
| **GPS** (Grafik Uyarı Sistemi) | Yerel GNN katmanlarını küresel Transformer katmanlarıyla birleştirin |
| **Graformer** | Grafik yapısına dayalı konumsal kodlama ekleyin |
### Heterojen Grafik Ağları
| Modeli | Açıklama |
|----------|----------------|
| **R-GCN** | İlişkisel GCN; farklı kenar tipleri için farklı ağırlık matrisleri |
| **HAN** | Heterojen Dikkat Ağı; farklı düğüm ve kenar türlerine dikkat |
| **HetGNN** | Heterojen Graf Sinir Ağı; birden çok düğüm türünü yönetir |
---

## Ölçeklenebilirlik
| Mücadelesi | Çözüm |
|---------------|----------|
| **Büyük grafikler** (milyonlarca düğüm) | Mini toplu eğitim; komşu örneklemesi |
| **Bellek** | GPU'lar arasında grafik bölümleme |
| **Hız** | Seyrek matris işlemleri; uzman kütüphaneler |
### Örnekleme Stratejileri
| Strateji | Açıklama |
|----------|----------------|
| **Düğüm örneklemesi** | Düğümlerin bir alt kümesini ve bunların K-hop mahallelerini örnekleyin |
| **Kenar örnekleme** | Örnek kenarlar ve bağlandıkları düğümler |
| **Küme örneklemesi** | Grafiği kümelere ayırın; kümeler üzerinde tren |
| **Rastgele yürüyüş örneklemesi** | Hedef düğümlerden rastgele yürüyüşler yoluyla örnek düğümler |
---

## Araçlar ve Çerçeveler
| Araç | Amaç |
|------|------------|
| **PyTorch Geometrik (PyG)** | En popüler GNN kütüphanesi; zengin model ve veri seti seti |
| **DGL** (Derin Grafik Kütüphanesi) | Çerçeveden bağımsız; PyTorch, TensorFlow, MXNet'i destekler |
| **AğX** | Klasik grafik algoritmaları; veri manipülasyonu |
| **OGB** (Açık Grafik Karşılaştırması) | GNN araştırması için standart kıyaslamalar ve veri kümeleri |
| **CogDL** | Grafikler için derin öğrenme; araştırma odaklı |
| **Spektral** | TensorFlow/Keras için GNN kitaplığı |
---

## Özet
Grafik Sinir Ağları, derin öğrenmeyi ağlar, moleküller, bilgi grafikleri ve varlıkların bağlı olduğu herhangi bir sistem gibi ilişkisel verilere genişletir. Komşular arasında mesaj ileterek çalışırlar ve her düğümün kendi yerel bağlamından öğrenmesine olanak tanırlar. GNN'ler en güçlü uygulamalarını ilaç keşfi, öneri sistemleri, sahtekarlık tespiti ve bilgi grafiklerinde buldu. Alan, büyük gerçek dünya ağları için grafik transformatörlerine, heterojen grafiklere ve ölçeklenebilir eğitime doğru gelişiyor. Verilerinizin ilişkileri varsa GNN'ler muhtemelen dikkate alınmaya değerdir.