---
# Metadata
title: "Genetics and Genomics"
description: "DNA, gene expression, CRISPR, GWAS, sequencing technologies"
category: "Natural Sciences"
subcategory: "Life Sciences"
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
  - version: "1.0.1"
    date: "2026-08-09"
    author: "Nepoznato-Dev"
    changes: "Moved to life_sciences/ subfolder; added subcategory field"

# Review
created: "2026-08-05"
last_modified: "2026-08-09"
review_date: "2027-02-05"
reviewed_by: "Natural Sciences Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [genetics, genomics, natural-sciences]
difficulty_level: "beginner"
prerequisites: []
estimated_reading_time: "6 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Genetik ve Genomik
Genetik, kalıtımın incelenmesidir - özelliklerin ebeveynlerden yavrulara DNA yoluyla nasıl aktarıldığı. Genomik, genomun tamamının incelenmesidir: tüm genler, kodlamayan bölgeler, bunların nasıl etkileşime girdiği ve bireyler ve popülasyonlar arasında nasıl değiştiği. Genetikten genomiğe geçiş, dizileme teknolojisi tarafından yönlendirildi; tek seferde bir gen çalışmaktan saatler içinde tüm genomu okumaya, tıp, tarım, adli tıp ve evrim anlayışımızı dönüştüren veriler üretmeye geçtik.
---

## DNA Temelleri
### DNA Yapısı
| Bileşen | Açıklama |
|-----------|----------------|
| **Nükleotid** | DNA'nın yapı taşı; bir şeker (deoksiriboz), bir fosfat grubu ve bir azotlu bazdan oluşur |
| **Bazlar** | Adenin (A), Timin (T), Guanin (G), Sitozin (C) |
| **Baz eşleştirme** | T (2 hidrojen bağı) ile A çifti; C ile G çiftleri (3 hidrojen bağı) |
| **Çift sarmal** | Anti-paralel uzanan iki şerit (5' ila 3' ve 3' ila 5'); sarmal şeklinde bükülmüş |
| **Kromozom** | Histon proteinlerinin etrafına sarılmış tek, uzun bir DNA molekülü; insanlarda 46 (23 çift) |
| **Genom** | Bir organizmadaki DNA'nın tamamı; insan genomu ~3,2 milyar baz çiftidir |
### Moleküler Biyolojinin Merkezi Dogması
| Adım | Süreç | Konum | Ürün |
|------|---------|----------|--------|
| **Çoğaltma** | DNA → DNA | Çekirdek | İki özdeş DNA molekülü |
| **Transkripsiyon** | DNA → mRNA | Çekirdek | Haberci RNA'sı |
| **Çeviri** | mRNA → protein | Ribozom (sitoplazma) | Polipeptit zinciri (protein) |
---

## Gen İfadesi
### Genler Nasıl Düzenlenir?
| Seviye | Mekanizma | Örnek |
|----------|-----------|-----------|
| **Epigenetik** | DNA metilasyonu; histon modifikasyonu; kromatin yeniden yapılanması | Kadınlarda bir X kromozomunun susturulması |
| **Transkripsiyonel** | Transkripsiyon faktörleri promotörleri/arttırıcıları bağlar; etkinleştirin veya bastırın | Bakterilerde Lac operonu; hormona duyarlı genler |
| **Transkripsiyon sonrası** | Alternatif ekleme; mRNA stabilitesi; mikroRNA'lar | Bir gen → birden fazla protein çeşidi |
| **Çeviri** | Ribozom mevcudiyeti; başlatma faktörü düzenlemesi | Ferritin mRNA yoluyla demirin düzenlenmesi |
| **Çeviri sonrası** | Protein modifikasyonu (fosforilasyon, her yerde bulunma); bozulma | Hücre döngüsü kontrolü |
---

## Kalıtım Kalıpları
### Mendel Genetiği
| Desen | Açıklama | Örnek |
|-----------|------------|------------|
| **Otozomal dominant** | Alelin bir kopyası yeterlidir | Huntington hastalığı; akondroplazi |
| **Otozomal resesif** | İki kopya gereklidir | Kistik fibrozis; orak hücreli anemi |
| **X'e bağlı baskın** | X kromozomundaki gen; bir kopya yeterli | Rett sendromu |
| **X'e bağlı resesif** | X kromozomundaki gen; erkekler daha çok etkileniyor | Hemofili; renk körlüğü |
| **Eş hakimiyet** | Her iki alel de eşit şekilde ifade edildi | ABO kan grupları (A ve B) |
| **Eksik hakimiyet** | Heterozigot orta düzeydedir | Kırmızı ve beyaz ebeveynlerden pembe çiçekler |
| **Poligenik** | Birden fazla gen bir özelliğe katkıda bulunur | Yükseklik; ten rengi; istihbarat |
| **Pleiotropi** | Bir gen birden fazla özelliği etkiler | Marfan sendromu (bağ dokusu, gözler, kalp) |
---

## Genomik
### Genomik Türleri
| Tür | Odaklanma | Başvuru |
|------|----------|------------|
| **Yapısal genomik** | Bir genomdaki tüm proteinlerin 3 boyutlu yapısı | İlaç tasarımı; protein mühendisliği |
| **İşlevsel genomik** | Genler ne işe yarar; gen etkileşimleri; ifade kalıpları | Hastalık mekanizmalarını anlamak |
| **Karşılaştırmalı genomik** | Türler arasında genomların karşılaştırılması | Evrimsel ilişkiler; korunan bölgelerin belirlenmesi |
| **Metagenomik** | Çevresel örneklerden DNA (kültürlenmemiş) | Mikrobiyom çalışmaları; yeni organizmaların keşfi |
| **Farmakogenomik** | Genler ilaç tepkisini nasıl etkiler | Kişiselleştirilmiş tıp; ilaç dozajı |
| **Epigenomik** | Genom çapında epigenetik modifikasyonlar | Kanser tanısı; gelişimsel biyoloji |
### DNA Sıralama Teknolojileri
| Nesil | Teknoloji | Okuma Uzunluğu | Verim | Temel Özellik |
|-----------|-----------|------------|------------|------------|
| **Birinci nesil** | Sanger sıralaması | ~1,000 baz puan | Düşük | Altın standart doğruluğu; doğrulama için kullanılır |
| **İkinci nesil** | Illumina (Solexa) | 50–300 baz çifti | Çok yüksek | Kısa okumalar; baskın platform; baz başına düşük maliyet |
| **İkinci nesil** | İyon Torrenti | 200–400 baz çifti | Yüksek | Yarı iletken tabanlı; optik yok |
| **Üçüncü nesil** | PacBio (SMRT) | 10.000–100.000 bp | Orta | Uzun okumalar; tekrarlayan bölgeleri çözer |
| **Üçüncü nesil** | Oxford Nanogözenek | Milyonlarca bp'ye kadar | Orta ila yüksek | Ultra uzun okumalar; taşınabilir (MinION); gerçek zamanlı |
---

## Genetik Çeşitlilik
### Varyasyon Türleri
| Tür | Açıklama | Frekans |
|------|-------------|-----------|
| **SNP** (Tek Nükleotid Polimorfizmi) | Tek baz değişimi | En yaygın olanı; ~1.000 bazda 1 |
| **Ekleme / Silme (indel)** | Bazların eklenmesi veya çıkarılması | Çerçeve kayması mutasyonlarına neden olabilir |
| **CNV** (Kopya Numarası Değişikliği) | Çoğaltılmış veya silinmiş segmentler (1 kb – birkaç Mb) | Hastalık ve evrime katkıda bulunur |
| **Yapısal çeşitlilik** | İnversiyonlar; translokasyonlar; büyük yeniden düzenlemeler | Daha az yaygın; patojen olabilir |
| **Mikrosatellit (STR)** | Kısa ardışık tekrarlar (2–6 bp tekrarlandı) | Adli tıp; babalık testi |
### GWAS (Genom Genelinde İlişki Çalışmaları)
| Adım | Açıklama |
|------|-----------------|
| **1. Örnekleri toplayın** | Vakalar (hastalıklı) ve kontroller (hastalıksız) |
| **2. Genotip** | Yüzbinlerce varyantın genotipini belirlemek için SNP dizilerini kullanın |
| **3. İstatistiksel test** | Her SNP'yi özellikle ilişkilendirme açısından test edin |
| **4. Manhattan arsası** | Tüm kromozomlardaki sonuçları görselleştirin |
| **5. Çoğaltma** | Bulguları bağımsız örneklerde doğrulayın |
---

## Gen Düzenleme
### CRISPR-Cas9
| Bileşen | İşlev |
|---------------|----------|
| **Kılavuz RNA (gRNA)** | ~20 nükleotid; hedef DNA dizisiyle eşleşiyor |
| **Cas9 proteini** | Moleküler makas; DNA'yı hedef bölgede kesiyor |
| **PAM dizisi** | Hedefin yanında kısa motif (NGG); Cas9 bağlama için gereklidir |
| **HDR** (Homolojiye Yönelik Onarım) | Bağışçı şablonu kullanarak hassas düzenleme |
| **NHEJ** (Homolog Olmayan Uç Birleştirme) | Hataya açık onarım; ekleme/silme işlemleri oluşturur (nakavt) |
### Gen Düzenleme Uygulamaları
| Başvuru | Açıklama |
|------------|------------|
| **Terapötik** | Hastalığa neden olan mutasyonları düzeltin (orak hücre; beta-talasemi) |
| **Tarım** | Hastalığa dayanıklı ürünler; geliştirilmiş hayvancılık |
| **Araştırma** | Nakavt modelleri oluşturun; gen fonksiyonunun incelenmesi |
| **Gen sürücüsü** | Genetik modifikasyonun bir popülasyona yayılması (örneğin, sıtmaya dirençli sivrisinekler) |
---

## Etik Hususlar
| Sayı | endişe |
|----------|-----------|
| **Genetik gizlilik** | Genom verilerinizin sahibi kim? İşverenler veya sigortacılar bunu kullanabilir mi? |
| **Embriyolarda gen düzenleme** | Kalıtsal değişiklikler; tasarımcı bebekler; istenmeyen hedef dışı etkiler |
| **Genetik ayrımcılık** | GINA (ABD) bazı ayrımcılığa karşı koruma sağlıyor ancak boşlukları var |
| **Bilgilendirilmiş onam** | Genomik veriler, rıza göstermeyen akrabalar hakkındaki bilgileri ortaya koyuyor |
| **Veri depolama** | Genomlar büyüktür (~200 GB ham); uzun vadeli depolama ve güvenlik zorlukları |
| **Özsermaye** | Genomik tıp, yalnızca zengin nüfuslara sunulabilirse sağlık eşitsizliklerini artırma riski taşıyor |
---

## Özet
Genetik, bireysel genlerin nasıl çalıştığını ve kalıtsal olarak aktarıldığını inceler. Genomik, genomun tamamını, yani tüm genleri, bunların etkileşimlerini ve varyasyonlarını inceler. DNA, proteinlere çevrilen RNA'ya kopyalanır. Gen ekspresyonu birçok seviyede düzenlenir: epigenetik, transkripsiyonel, transkripsiyon sonrası, translasyon ve translasyon sonrası. Kalıtım, özelliklerin nesiller arasında nasıl aktarılacağını belirleyen kalıpları (baskın, resesif, poligenik) takip eder. Modern sıralama teknolojileri (Illumina, PacBio, Nanopore) genomun tamamını hızlı ve ucuz bir şekilde okuyabilir. CRISPR-Cas9, tıp ve tarımda dönüştürücü potansiyele sahip hassas gen düzenlemeyi mümkün kılıyor. En büyük zorluklar etik sorunlardır: Genomik verileri kimin kontrol ettiği, embriyolarda gen düzenlemesinin nasıl düzenleneceği ve genomik tıbbın sadece ayrıcalıklı olanlara değil herkese fayda sağlamasının nasıl sağlanacağı.