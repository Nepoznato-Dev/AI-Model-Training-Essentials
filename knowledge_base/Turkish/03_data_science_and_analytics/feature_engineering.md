---
# Metadata
title: "Feature Engineering"
description: "Transformations, encodings, feature selection, dimensionality reduction"
category: "Data Science and Analytics"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "Nepoznato-Dev"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.0"
    date: "2026-08-05"
    author: "Nepoznato-Dev"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-05"
review_date: "2027-02-05"
reviewed_by: "Data Science & Analytics Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [feature, engineering, data-science-and-analytics]
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
# Özellik Mühendisliği
Özellik mühendisliği, ham verileri makine öğrenimi modellerini daha etkili hale getiren temsillere dönüştürme sürecidir. Genellikle makine öğrenimi hattındaki en önemli adım olarak tanımlanır; bir modele verdiğiniz özellikler, seçtiğiniz algoritmadan daha önemlidir. İyi hazırlanmış özelliklere sahip basit bir model genellikle ham, işlenmemiş girdilere sahip karmaşık bir modelden daha iyi performans gösterecektir. Sanat, hem alanı hem de verileri, modelin öğrenebileceği sinyalleri yaratacak kadar iyi anlamakta yatmaktadır.
---

## Özellik Mühendisliği Neden Önemlidir
| Faktör | Etki |
|----------|-----------|
| **Sinyal kalitesi** | Daha iyi özellikler = modelin öğrenmesi için daha net modeller |
| **Model basitliği** | İyi özellikler, daha basit modellerin iyi performans göstermesini sağlar; karmaşık mimarilere daha az ihtiyaç |
| **Eğitim hızı** | İlgili, iyi ölçeklendirilmiş özellikler daha hızlı birleşir |
| **Genelleme** | Etki alanı bilgili özellikler, modellerin görünmeyen veriler üzerinde çalışmasına yardımcı olur |
| **Yorumlanabilirlik** | Anlamlı özelliklerin paydaşlara açıklanması daha kolaydır |
---

## Özellik Dönüşümü Türleri
### Sayısal Dönüşümler
| Dönüşüm | Formül / Açıklama | Ne Zaman Kullanılmalı |
|---------------|---------------|---------------|
| **Günlük dönüşümü** | log(x) veya log(x + 1) | Sağa çarpık dağılımlar; parasal değerler |
| **Karekök** | sqrt(x) | Orta derecede eğim; sayım verileri |
| **Box-Cox** | En iyi güç dönüşümünü bulan parametrik dönüşüm | Verileri daha normal şekilde dağıtma |
| **Yeo Johnson** | Box-Cox'a benzer ancak negatif değerleri işler | Negatif değerlere sahip çarpık veriler |
| **Standartlaştırma** | (x - ortalama) / std | Farklı ölçeklerdeki özellikler; normalliği varsayan algoritmalar |
| **Min-maks ölçeklendirme** | (x - dk) / (maks - dk) | Özelliklerin [0, 1]'e sınırlanması; görüntü piksel değerleri |
| **Sağlam ölçeklendirme** | (x - medyan) / IQR | Aykırı değerlere sahip veriler |
| **Bölme** | Sürekliyi kategorik hale dönüştürün | Doğrusal olmayan ilişkiler; karar ağaçları |
| **Polinom özellikleri** | x², x³, x₁×x₂ | Doğrusal modellerde doğrusal olmayan ilişkileri yakalama |
### Kategorik Kodlamalar
| Kodlama | Açıklama | Ne Zaman Kullanılmalı |
|----------|----------------|------------|
| **Tek seferde kodlama** | Her kategori için ikili sütun oluşturun | Düşük kardinaliteli kategoriler; ağaç tabanlı modeller yerel olarak işlenir |
| **Etiket kodlaması** | Her kategoriye tamsayı atayın | Sıralı kategoriler; ağaç tabanlı modeller |
| **Hedef kodlama** | Kategoriyi hedef değişkenin ortalamasıyla değiştirin | Yüksek kardinaliteli kategoriler; yumuşatmayla aşırı uyumdan kaçının |
| **Frekans kodlaması** | Kategoriyi sayısı veya sıklığıyla değiştirin | Frekansın kendisi bilgilendirici olduğunda |
| **İkili kodlama** | Tamsayı kodlu kategorileri ikili rakamlara dönüştürün | Yüksek kardinalite; tek-sıcak vs boyutluluğu azaltır |
| **Gömme** | Yoğun vektör gösterimini öğrenin | Çok yüksek kardinalite; NLP; tavsiye sistemleri |
| **Karma kodlama** | Sabit sayıda özelliğe yönelik karma kategorileri | Çok yüksek kardinalite; çevrimiçi öğrenme |
### Tarih ve Saat Özellikleri
| Özellik | Açıklama |
|-----------|------------|
| **Günün saati** | Günlük kalıpları yakalar (yoğun saatler, gece vakti) |
| **Haftanın günü** | Hafta içi ve hafta sonu etkileri |
| **Ay / çeyrek** | Sezonluk desenler |
| **Hafta sonu** | Hafta sonu için ikili bayrak |
| **Tatil mi** | Resmi tatiller için ikili bayrak |
| **Olayın üzerinden geçen süre** | Son satın alma işleminden bu yana geçen günler; son girişten bu yana geçen saat |
| **Döngüsel kodlama** | sin(2π × saat / 24), cos(2π × saat / 24) — zamanın dairesel doğasını korur |
---

## Eksik Değerleri Ele Alma
| Strateji | Açıklama | Ne Zaman Kullanılmalı |
|----------|----------------|------------|
| **Satırları bırak** | Değerleri eksik olan satırları kaldırın | Eksik veriler küçük bir kısımdır; MCAR (tamamen rastgele eksik) |
| **Sütunları bırakın** | Çok fazla eksik değeri olan özellikleri kaldırın | Özellik çoğunlukla eksik; önemli değil |
| **Ortalama / medyan atama** | Özelliğin ortalamasını veya ortancasını doldurun | Basit; ortalamayı korur ancak varyansı azaltır |
| **Mod atama** | Kategoriyi en sık değerle doldur | Kategorik özellikler |
| **KNN'ye atıf** | Eksik değeri tahmin etmek için k-en yakın komşuları kullanın | Benzer örnekler eksik değeri tahmin etmeye yardımcı olduğunda |
| **Model tabanlı atama** | Eksik değerleri tahmin etmek için bir model eğitin | Daha doğru; hesaplama açısından pahalı |
| **Eksik gösterge** | Eksikliği işaretleyen bir ikili sütun ekleyin | Eksikliğin kendisi bilgilendirici olduğunda |
| **Enterpolasyon** | Enterpolasyonlu değerlerle doldurma (doğrusal, spline) | Zaman serisi; sıralı veriler |
---

## Özellik Seçimi
### Filtre Yöntemleri
| Yöntem | Açıklama |
|----------|----------------|
| **Korelasyon** | Birbirleriyle yüksek düzeyde ilişkili özellikleri kaldırın |
| **Fark eşiği** | Sıfıra yakın farka sahip özellikleri kaldırın |
| **Karşılıklı bilgi** | Her özelliğin hedef hakkında sağladığı bilgileri ölçün |
| **Ki-kare** | Kategorik özellikler ile hedef arasındaki bağımsızlığı test edin |
| **ANOVA F testi** | Sayısal özellik araçlarının hedef sınıflara göre farklılık gösterip göstermediğini test edin |
### Sarma Yöntemleri
| Yöntem | Açıklama |
|----------|----------------|
| **İleri seçim** | Boş başlayın; en iyi özelliği birer birer ekleyin |
| **Geriye doğru eleme** | Hepsiyle başlayın; en kötü özelliği birer birer kaldırın |
| **Özyinelemeli özellik ortadan kaldırma (RFE)** | Modeli tekrar tekrar eğitin; en az önemli özellikleri kaldırın |
### Gömülü Yöntemler
| Yöntem | Açıklama |
|----------|----------------|
| **L1 düzenlemesi (Kement)** | İlgisiz özellik ağırlıklarını sıfıra indirir |
| **Ağaç bazlı önem** | Ağaç modellerinden özellik önemini kullanın |
| **SHAP değerleri** | Her özelliğin tahminlere katkısını ölçün |
---

## Etki Alanına Özel Özellik Mühendisliği
### Metin Özellikleri
| Özellik | Açıklama |
|-----------|------------|
| **TF-IDF** | Ters belge sıklığına göre ağırlıklandırılmış terim sıklığı |
| **Kelime yerleştirmeleri** | Anlamsal anlamı yakalayan yoğun vektörler (Word2Vec, GloVe) |
| **Karakter n-gramı** | Alt kelime kalıplarını yakalayın; yazım hataları ve morfoloji için faydalıdır |
| **Metin istatistikleri** | Uzunluk; kelime sayısı; cümle sayısı; ortalama kelime uzunluğu |
| **Okunabilirlik puanları** | Flesch-Kincaid; Sisli sis indeksi |
### Zaman Serisi Özellikleri
| Özellik | Açıklama |
|-----------|------------|
| **Gecikme özellikleri** | Önceki değerler: y(t-1), y(t-7), y(t-30) |
| **Devamlı istatistikler** | Bir pencere üzerinde ortalama, std, min, max |
| **Fark** | y(t) - y(t-1); trendi yakalıyor |
| **Mevsimsel fark** | yıllık mevsimsellik içeren aylık veriler için y(t) - y(t-12) |
| **Fourier terimleri** | Mevsimsel desenler için sinüs ve kosinüs terimleri |
### Görüntü Özellikleri (Derin Öğrenme Öncesi)
| Özellik | Açıklama |
|-----------|------------|
| **HOG** (Yönlendirilmiş Degradelerin Histogramı) | Kenar yönlerinin dağılımı |
| **LBP** (Yerel İkili Modeller) | Doku açıklaması |
| **SIFT** (Ölçekle Değişmeyen Özellik Dönüşümü) | Anahtar nokta tanımlayıcıları |
| **Renkli histogramlar** | Görüntüdeki renklerin dağılımı |
---

## Özellik Mühendisliği En İyi Uygulamaları
| Alıştırma | Açıklama |
|----------|----------------|
| **Veri sızıntısını önleyin** | Özellikler oluşturmak için asla gelecekten veya test setinden gelen bilgileri kullanmayın |
| **Her şeyi belgeleyin** | Hangi dönüşümlerin uygulandığını ve nedenini kaydedin |
| **Özelliklerinizi sürümlendirin** | Model değişikliklerinin yanı sıra özellik değişikliklerini de izleyin |
| **Şunu kullanarak ve olmadan doğrula** | Yeni bir özelliğin model performansını gerçekten iyileştirip iyileştirmediğini test edin |
| **Tekrarlanabilir olmasını sağlayın** | Özellik mühendisliği ardışık düzenleri belirleyici ve tekrarlanabilir olmalıdır |
| **Monitör özelliği kayması** | Özellik dağılımları zamanla değişebilir; izleyin ve yeniden eğitin |
---

## Özet
Özellik mühendisliği, alan bilgisinin makine öğrenimiyle buluştuğu yerdir. Dağınık, eksik, yüksek boyutlu ham verileri, modellerin öğrenebileceği temiz, bilgilendirici temsillere dönüştürme sürecidir. Sayısal dönüşümler çarpıklık ve ölçeği yönetir. Kategorik kodlamalar, etiketleri modellerin kullanabileceği sayılara dönüştürür. Tarih özellikleri zamansal kalıpları yakalar. Eksik değer stratejileri eksik verileri işler. Özellik seçimi gürültüyü ve fazlalığı ortadan kaldırır. En iyi özellik mühendisleri dedektifler gibi düşünürler: Verilerde hangi sinyallerin bulunması gerektiğini, bu sinyallerin nerede gizlenebileceğini ve bunları dürüst (veri sızıntısı olmayan), tekrarlanabilir ve zaman içinde değişmeye dayanıklı bir şekilde nasıl çıkarabileceklerini sorarlar.