---
# Metadata
title: "Computer Vision Fundamentals"
description: "CNNs, object detection, segmentation, transfer learning"
category: "AI and Machine Learning"
subcategory: "NLP and Speech"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "AI Model Training Team"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.1"
    date: "2026-08-09"
    author: "AI Model Training Team"
    changes: "Moved to nlp_and_speech/ subfolder; added subcategory field"
  - version: "1.0.0"
    date: "2026-08-05"
    author: "AI Model Training Team"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-09"
review_date: "2027-02-05"
reviewed_by: "AI & Machine Learning Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [computer, vision, ai-and-machine-learning]
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

# Bilgisayarlı Görmenin Temelleri
Bilgisayarlı görme, makinelere dünyadaki görsel bilgileri (görüntüler, videolar ve 3 boyutlu veriler) yorumlama ve anlama yeteneği verir. Telefonunuzdaki yüz tanımadan sürücüsüz arabalara, tıbbi görüntü analizine ve endüstriyel kalite kontrolüne kadar her şeye güç sağlar. Bu dosya temel kavramları, mimarileri ve teknikleri kapsar.
---

## Bilgisayarlar Görselleri Nasıl Görür?
### Piksel ve Kanallar
Dijital görüntü piksellerden oluşan bir ızgaradır. Her pikselin renk yoğunluğunu temsil eden sayısal değerleri vardır.
| Resim Türü | Kanallar | Piksel Başına Değerler | Örnek |
|-----------|----------|------|-----------|
| **Gri tonlamalı** | 1 | 0 (siyah) ila 255 (beyaz) | Tıbbi Röntgenler |
| **RGB** | 3 | Kırmızı, Yeşil, Mavi (her biri 0–255) | Standart renkli fotoğraflar |
| **RGBA** | 4 | RGB + Alfa (şeffaflık) | Şeffaf arka plana sahip resimler |
| **HSV** | 3 | Ton, Doygunluk, Değer | Renk bazlı segmentasyon |
1920×1080 RGB görüntü,`(1080, 1920, 3)`şeklinde bir tensördür; bu, her biri 3 değere sahip 6,2 milyon piksel anlamına gelir.
### Tuş İşlemleri
| Operasyon | Açıklama |
|-----------|----------------|
| **Yeniden boyutlandırma** | Görüntüyü hedef boyutlara göre ölçeklendirin (çift doğrusal, en yakın komşu enterpolasyonu) |
| **Kırpma** | İlgilenilen bölgeyi çıkarın |
| **Normalleşme** | Sinir ağları için piksel değerlerini [0,1] veya [-1,1] olarak ölçeklendirin |
| **Büyütme** | Eğitim verilerini yapay olarak genişletin (döndürme, çevirme, renk değişimi, kırpma) |
---

## Evrişim: Temel Operasyon
Bir evrişim, küçük bir filtreyi (çekirdeği) görüntü boyunca kaydırarak her konumdaki nokta çarpımlarını hesaplar. CNN'ler kenarları, dokuları ve desenleri bu şekilde algılar.
### Evrişim Parametreleri
| Parametre | Efekt |
|-----------|-----------|
| **Çekirdek boyutu** | 3×3, 5×5, 7×7 — daha büyük çekirdekler daha büyük desenleri yakalar |
| **Adım** | Adım boyutu; adım=2 çıktı boyutlarını yarıya indirir |
| **Dolgu** | Uzamsal boyutları korumak için sınırın çevresine sıfır ekleyin |
| **Filtre sayısı** | Her filtre farklı bir özelliği öğrenir (kenar, doku, renk deseni) |
### Evrişimler Ne Öğrenir?
| Katman Derinliği | Özellikler Algılandı |
|---------------|-------|
| **Erken katmanlar** | Kenarlar, köşeler, basit dokular |
| **Orta katmanlar** | Şekiller, nesne parçaları (tekerlekler, gözler, yapraklar) |
| **Derin katmanlar** | Üst düzey kavramlar (yüzler, arabalar, hayvanlar) |
---

## CNN Mimarileri
CNN mimarilerinin evrimi, derin öğrenmenin bilgisayar görüşündeki ilerlemesinin öyküsünü anlatıyor.
| Mimarlık | Yıl | Temel Yenilik |
|---------------|----------|---------------|
| **LeNet-5** | 1998 | İlk pratik CNN; rakam tanıma |
| **AlexNet** | 2012 | Deep CNN ImageNet'i kazandı; ReLU, okulu bırakma, GPU eğitimi |
| **VGGNet** | 2014 | Yığılmış 3×3 evrişim (daha derin = daha iyi) |
| **GoogLeNet (Başlangıç)** | 2014 | Başlangıç ​​modülleri (paralel filtre boyutları); 22 katman |
| **ResNet** | 2015 | Bağlantıları atla (artık öğrenme); 152+ katman |
| **EfficientNet** | 2019 | Bileşik ölçeklendirme (derinlik + genişlik + çözünürlük) |
| **ConvNeXt** | 2022 | Modernize Edilmiş ResNet; Transformers'la Rekabetçi |
### ResNet Neden Her Şeyi Değiştirdi?
ResNet'ten önce, gradyan sorununun ortadan kalkması nedeniyle çok derin ağların eğitimi neredeyse imkansızdı. ResNet **bağlantıları atla**'yı (artık bağlantılar da denir) kullanıma sundu: bir katmanın girişi, çıkışına eklenir.
```
output = F(x) + x    # Skip connection
```

Bu basit fikir, 152'den fazla katmana sahip ağların etkili bir şekilde eğitilmesine olanak sağladı ve artık neredeyse tüm derin mimarilerde standart hale geldi.
---

## Temel Vizyon Görevleri
### Görüntü Sınıflandırması
Görüntünün tamamına bir etiket atayın.
| Modeli | Yaklaşım |
|----------|----------|
| CNN'ler (ResNet, EfficientNet) | Geleneksel yaklaşım; mükemmel doğruluk |
| Görüş Transformatörleri (ViT) | Görüntüyü yama dizisi olarak ele alın; Trafo kodlayıcı |
| Öğrenmeyi Aktar | Veri kümenizde önceden eğitilmiş bir modele ince ayar yapın |
### Nesne Algılama
Sınırlayıcı kutularla bir görüntüdeki birden çok nesneyi bulun ve sınıflandırın.
| Modeli | Tür | Hız |
|----------|----------|----------|
| **R-CNN** | İki aşamalı (teklif + sınıflandırma) | Yavaş |
| **Hızlı R-CNN** | Geliştirilmiş iki aşamalı | Orta |
| **Daha hızlı R-CNN** | Bölge Teklif Ağı + dedektör | Orta |
| **YOLO** (v1–v10) | Tek aşamalı; kutuları + sınıfları tek geçişte tahmin etmek | Çok hızlı |
| **DETR** | Trafo bazlı; bağlantı kutusu yok | Orta |
**YOLO** (Yalnızca Bir Kez Bakarsınız) gerçek zamanlı algılama için başvurulacak çözümdür. **Doğruluğun hızdan daha önemli olduğu durumlarda daha hızlı R-CNN** tercih edilir.
### Görüntü Segmentasyonu
Bir görüntüdeki her pikseli sınıflandırın.
| Tür | Açıklama | Kullanım Örneği |
|------|-----------------|----------|
| **Anlamsal Segmentasyon** | Her piksel bir sınıf etiketi alır | Otonom sürüş (yol, araba, yaya) |
| **Örnek Segmentasyonu** | Her piksel + nesne örneği kimliği | Nesneleri sayma, tıbbi görüntüleme |
| **Panoptik Segmentasyon** | Semantik + örnek birleştirildi | Kapsamlı sahne anlayışı |
Anahtar modeller: U-Net (tıbbi görüntüleme), Mask R-CNN (örnek), DeepLab (semantik), Her Şeyi Segmente Ayırma Modeli (SAM — evrensel segmentasyon).
### Görüntü Oluşturma
| Yaklaşım | Açıklama | Örnekler |
|----------|----------------|----------|
| **GAN'lar** | Jeneratöre karşı ayrımcıya karşı çekişmeli eğitim | StilGAN, DöngüGAN |
| **VAE'ler** | Gizli dağıtımı öğrenin; oluşturulacak örnek | Varyasyonel Otomatik Kodlayıcılar |
| **Difüzyon Modelleri** | Rastgele gürültüyü yinelemeli olarak giderme | Kararlı Difüzyon, DALL-E, Yolculuğun Ortası |
Difüzyon modelleri, görüntü oluşturma kalitesi açısından GAN'ları büyük ölçüde geride bıraktı.
---

## Vizyon için Öğrenmeyi Aktarın
Bir CNN'yi sıfırdan eğitmek, büyük miktarda veri ve bilgi işlem gerektirir. Transfer öğrenimi, halihazırda milyonlarca görüntü (ImageNet) üzerinde eğitilmiş bir modelle başlamanıza ve onu özel göreviniz için ince ayar yapmanıza olanak tanır.
### Adımlar
1. **Önceden eğitilmiş bir model seçin** (ResNet50, EfficientNet-B0, ViT).
2. **Sınıflandırma başlığını** kendinizinkiyle değiştirin (sınıf sayınıza uygun).
3. **İlk katmanları dondurun** (kenarlar gibi genel özellikleri yakalarlar).
4. Veri kümenizde düşük öğrenme oranıyla **ince ayar yapın**.
5. **Daha fazla adaptasyona ihtiyacınız varsa, yavaş yavaş çözün**.
Bu yaklaşım rutin olarak 1.000-10.000 kadar az etiketli görüntüyle yüksek doğruluk elde eder.
---

## Veri Arttırma
Artırma, dönüşümler uygulayarak eğitim veri kümenizi yapay olarak genişletir.
| Büyütme | Efekt | Ne Zaman Kullanılmalı |
|-------------|-----------|-------------|
| **Rastgele kırpma** | Rastgele bölgeye kırp | Neredeyse her zaman |
| **Yatay çevirme** | Ayna görüntüsü | Yön önemli olmadığında |
| **Döndürme** | Rastgele açıyla döndür | Nesneler herhangi bir açıda göründüğünde |
| **Renk titremesi** | Parlaklığı, kontrastı ve doygunluğu rastgele ayarlayın | Aydınlatma değiştiğinde |
| **Rastgele silme** | Rastgele bölgeleri maskele | Sağlamlığı artırır |
| **Karıştır / KesKarıştır** | İki görseli ve etiketi karıştırın | Düzenleme |
Kütüphaneler:`torchvision.transforms`,`albumentations`,`imgaug`,`tf.keras.preprocessing`.
---

## Araçlar ve Çerçeveler
| Araç | Amaç |
|------|------------|
| **AçıkCV** | Klasik CV işlemleri (filtreleme, kenar algılama, geometrik dönüşümler) |
| **meşale görüşü** | PyTorch görüş modelleri, dönüşümler, veri kümeleri |
| **tf.keras.applications** | TensorFlow/Keras'ta önceden eğitilmiş modeller |
| **Ultralitik (YOLOv8/v11)** | Nesne algılama, segmentasyon, sınıflandırma |
| **Sarılma Yüzü (transformatörler)** | Görüş Transformatörleri, SegFormer, DETR |
| **Her Şeyi Bölümlere Ayırın (SAM)** | Meta'dan evrensel görüntü segmentasyonu |
| **Albümler** | Hızlı, esnek görüntü büyütme kitaplığı |
---

## Pratik İpuçları
- **Transfer öğrenimiyle başlayın.** Önceden eğitilmiş bir modele ince ayar yapmak neredeyse her durumda sıfırdan eğitimden üstündür.
- **Girişlerinizi normalleştirin.** Önceden eğitilmiş modelin beklediği normalleştirmeyi eşleştirin (genellikle ImageNet ortalama/std).
- **Uygun ölçümleri kullanın.** Dengeli veri kümeleri için doğruluk; Dengesiz veya algılama görevleri için F1, mAP veya IoU.
- **Verilerinizi görselleştirin.** Örnek görsellere bakın, sınıf dağılımlarını kontrol edin, model tahminlerini inceleyin.
- **Akıllıca artırın.** Yalnızca alanınız için anlamlı olan dönüşümleri uygulayın (tıbbi görselleri dikey olarak çevirmeyin).
- **Aşırı uyumu izleyin.** Eğitim doğruluğu yüksek ancak doğrulama düşükse, artırmayı artırın veya bırakma ekleyin.