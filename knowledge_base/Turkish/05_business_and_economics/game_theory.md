---
# Metadata
title: "Game Theory and Strategic Thinking"
description: "Nash equilibrium, prisoner's dilemma, mechanism design, auctions"
category: "Business and Economics"
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
reviewed_by: "Business & Economics Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [game, theory, business-and-economics]
difficulty_level: "beginner"
prerequisites: []
estimated_reading_time: "7 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# Oyun Teorisi ve Stratejik Düşünme
Oyun teorisi, stratejik etkileşimlerin (sonucunuzun yalnızca sizin ne yaptığınıza değil, başkalarının ne yaptığına da bağlı olduğu durumların) matematiksel olarak incelenmesidir. Her yerde geçerlidir: iş rekabeti, uluslararası ilişkiler, müzayedeler, müzakereler, evrimsel biyoloji ve trafikte rota seçme gibi günlük kararlar. Temel anlayış, stratejik durumlardaki rasyonel aktörlerin sadece kendi stratejilerini optimize etmekle kalmayıp, diğerlerinin ne yapacağını tahmin etmeleri ve diğerlerinin de aynısını yapmasıdır.
---

## Temel Kavramlar
### Anahtar Terminoloji
| Dönem | Tanımı |
|------|---------------|
| **Oyun** | Seçimleri birbirlerinin sonuçlarını etkileyen iki veya daha fazla karar vericinin (oyuncunun) olduğu herhangi bir durum |
| **Oyuncu** | Oyunda bir karar verici |
| **Strateji** | Ortaya çıkabilecek her durum için eksiksiz bir eylem planı |
| **Getiri** | Bir oyuncunun belirli bir strateji kombinasyonundan elde ettiği sonuç |
| **Nash dengesi** | Hiçbir oyuncunun stratejisini tek taraflı olarak değiştirerek kazancını artıramayacağı bir dizi strateji |
| **Baskın strateji** | Diğer oyuncuların ne yaptığından bağımsız olarak en iyi strateji |
| **Sıfır toplamlı oyun** | Bir oyuncunun kazancı tam olarak diğerinin kaybıdır |
| **Sıfır toplamlı olmayan oyun** | Oyuncuların tümü potansiyel olarak kazanabilir veya kaybedebilir |
| **İşbirlikçi oyun** | Oyuncular bağlayıcı anlaşmalar yapabilirler |
| **İşbirliğine dayalı olmayan oyun** | Bağlayıcı anlaşma yok; her oyuncu kendi çıkarına göre hareket eder |
---

## Klasik Oyunlar
### Mahkumun İkilemi
İki şüpheli tutuklandı. Her biri işbirliği yapabilir (sessiz kalabilir) veya kaçabilir (itiraf edebilir).
| | B İşbirliği Yapıyor | B Kusurları |
|---|-----------------|-----------|
| **A İşbirliği Yapıyor** | A: 1 yıl, B: 1 yıl | A: 10 yıl, B: ücretsiz |
| **A Kusurları** | A: ücretsiz, B: 10 yıl | A: 5 yıl, B: 5 yıl |
| İçgörü | Açıklama |
|-----------|------------|
| **Baskın strateji** | Her iki oyuncuda da kusur baskın |
| **Nash dengesi** | Her ikisi de kusurlu (her biri 5 yıl) |
| **Pareto optimal** | Her ikisi de işbirliği yapıyor (her biri 1 yıl) |
| **Ders** | Rasyonel bireysel kararlar toplu olarak daha kötü sonuçlara yol açabilir |
### Diğer Klasik Oyunlar
| Oyun | Açıklama | Nash Dengesi | Ders |
|------|-------------|------|--------|
| **Tavuk (Şahin-Güvercin)** | İki sürücü birbirine doğru ilerliyor; yoldan çıkın veya düz gidin | Biri yoldan çıkıyor, biri düz gidiyor | Tehlikeyi göze alma; bağlılığın güvenilirliği |
| **Bekarlığa Veda Avı** | Birlikte bir geyik avlayın (yüksek kazanç) veya tek başınıza bir tavşan avlayın (düşük kazanç) | Hem geyik hem de tavşan | Koordinasyon; güven |
| **Cinsiyetlerin Savaşı** | İki oyuncu farklı sonuçları tercih ediyor ancak koordine olmak istiyor | İkisi de aynı etkinliğe gidiyor | Çoklu dengeler; ilk hareket edenin avantajı var |
| **Ültimatom oyunu** | Teklif sahibi parayı böler; yanıtlayan kişi kabul eder veya reddeder (ikisi de hiçbir şey almaz) | Teklif Sahibi minimum teklifi sunar; yanıtlayan kabul ediyor | İnsanlar haksız teklifleri reddediyor (mantıksız ama yaygın) |
| **Kamu malı oyunu** | Paylaşılan bir havuza veya ücretsiz sürüşe katkıda bulunun | Herkes bedava yolculuk | Müştereklerin trajedisi; yaptırım ihtiyacı |
---

## Oyun Türleri
### Zamanlamaya Göre
| Tür | Açıklama | Örnek |
|------|-------------|--------|
| **Eşzamanlı** | Oyuncular aynı anda hareket eder (veya diğerlerinin hamlelerini bilmeden) | Taş-kağıt-makas; kapalı teklif açık artırmaları |
| **Sıralı** | Oyuncular birbiri ardına hareket eder; daha sonraki oyuncular daha önceki hamleleri gözlemler | Satranç; pazara giriş kararları |
| **Tekrarlandı** | Aynı oyun birden çok kez oynandı | Tekrarlanan mahkum ikilemi; devam eden ticari rekabet |
### Bilgiye Göre
| Tür | Açıklama | Örnek |
|------|-------------|--------|
| **Mükemmel bilgi** | Tüm oyuncular önceki tüm hamleleri bilir | Satranç; dama |
| **Eksik bilgi** | Bazı hareketler gizli | Poker; ticari rekabet |
| **Bilginin tamamı** | Tüm oyuncular tüm getirileri ve stratejileri bilir | Çoğu ders kitabı oyunu |
| **Eksik bilgi** | Bazı getiriler veya türleri bilinmiyor | Açık artırmalar; müzakereler |
---

## Çözüm Kavramları
### Nash dengesi
| Görünüş | Açıklama |
|----------|----------------|
| **Tanım** | Hiçbir oyuncu tek başına stratejisini değiştirerek kazancını artıramaz |
| **Nasıl bulunur** | Her oyuncu için diğerlerinin stratejilerine en iyi tepkiyi bulun; hepsinin kesiştiği yer Nash dengesidir |
| **Varoluş** | Her sonlu oyunda en az bir Nash dengesi vardır (muhtemelen karma stratejilerde) |
| **Benzersizlik** | Oyunlar birden fazla Nash dengesine sahip olabilir; koordinasyon sorunları ortaya çıkıyor |
| **Sınırlama** | Nash dengesi size hangi dengenin seçileceğini söylemez; adaleti hesaba katmıyor |
### Baskın Strateji Dengesi
| Adım | Açıklama |
|------|-----------------|
| **1. Stratejileri belirleyin** | Her oyuncu için mevcut tüm stratejileri listeleyin |
| **2. Baskın stratejileri bulun** | Başkalarının ne yaptığına bakılmaksızın en iyi strateji |
| **3. Tüm oyuncularda bir tane varsa** | Kombinasyon baskın strateji dengesidir |
| **4. Değilse** | Domine edilen stratejilerin veya Nash dengesinin yinelenen eliminasyonunu kullanın |
### Geriye Dönük Çıkarım (Sıralı Oyunlar)
| Adım | Açıklama |
|------|-----------------|
| **1. Oyun ağacını çizin** | Düğümler = karar noktaları; şubeler = eylemler |
| **2. Sondan başla** | Her terminal düğümünde son oyuncunun en uygun seçimini belirleyin |
| **3. Geriye doğru çalışın** | Her önceki düğümde, en iyi sonuca götüren eylemi seçin |
| **4. Sonuç** | Alt oyun mükemmel dengesi — her karar noktasında en uygun strateji |
---

## Gelişmiş Kavramlar
### Karma Stratejiler
| Konsept | Açıklama | Örnek |
|-----------|------------|------------|
| **Karma strateji** | Olasılıklara göre eylemler arasında rastgele seçim yapma | Taş-kağıt-makas: her birini 1/3 olasılıkla oynayın |
| **Neden rastgele seçmelisiniz?** | Rakiplerin hamlenizi tahmin etmesini engeller | Futbolda penaltı vuruşları; vergi denetimleri |
| **Karma strateji Nash dengesi** | Her oyuncu kendi saf stratejileri arasında kayıtsızdır | Hiçbir oyuncu diğerini istismar edemez |
### Tekrarlanan Oyunlar ve Halk Teoremi
| Konsept | Açıklama |
|-----------|------------|
| **Sonsuz tekrarlanan** | Geriye dönük çıkarım işbirliğini çözer; tek atışlık oyunla aynı | Son turda ayrılma geriye doğru yayılıyor |
| **Sonsuzca tekrarlandı** | İşbirliği gelecekte cezalandırılma tehdidiyle sürdürülebilir | Kısasa kısas; acımasız tetikleme stratejileri |
| **Halk teoremi** | Herhangi bir bireysel rasyonel getiri, sonsuz tekrarlanan bir oyunda Nash dengesi olabilir | Gelecek yeterince önemliyse işbirliği mümkündür |
| **İndirim faktörü** | Oyuncuların gelecekteki getirilere ne kadar değer verdiği; daha yüksek = daha fazla işbirliği | Sabırlı oyuncular daha fazla işbirliği yapıyor |
### Mekanizma Tasarımı (Ters Oyun Teorisi)
| Konsept | Açıklama |
|-----------|------------|
| **Gol** | İstenilen sonuca ulaşmak için oyunun kurallarını tasarlayın |
| **Uygulamalar** | Açık artırmalar; oylama sistemleri; sözleşme tasarımı; pazar tasarımı |
| **Vahiy ilkesi** | Herhangi bir mekanizmayla elde edilebilecek her sonuca, gerçek bir doğrudan mekanizmayla ulaşılabilir |
| **Örnek** | Vickrey açık artırması (ikinci fiyat kapalı teklif) — gerçek değerinizi teklif etmek baskın bir stratejidir |
---

## Uygulamalar
### İşletme
| Başvuru | Oyun Teorisi Konsepti | İçgörü |
|------------|-----------|-----------|
| **Fiyat rekabeti** | Mahkumun ikilemi | Fiyat savaşları her iki firmaya da zarar veriyor; tekrarlanan oyunlarda örtülü gizli anlaşma |
| **Pazara giriş** | Sıralı oyun; taahhüt | Görevli firmanın girişle mücadele etme tehdidi ancak kapasiteye yatırım yapmaları durumunda inandırıcıdır |
| **Açık artırmalar** | Mekanizma tasarımı | İkinci fiyat açık artırmaları gerçek değerleri ortaya çıkarır; spektrum açık artırmaları milyarlarca dolar topladı |
| **Müzakere** | Pazarlık oyunu; Nash dengesi | Fazlalığı bölün; ültimatom oyunlarında ilk hamle avantajı |
| **Sinyalizasyon** | Spence'in eğitim modeli | Pahalı sinyaller güvenilirdir çünkü düşük kaliteli tipler bunları karşılayamaz |
### Uluslararası İlişkiler
| Başvuru | Oyun Teorisi Konsepti | İçgörü |
|------------|-----------|-----------|
| **Silahlanma yarışları** | Mahkumun ikilemi | Her iki taraf da silahsızlansa daha iyi olur ama birbirlerine güvenemezler |
| **Ticaret savaşları** | Tekrarlanan oyun | Kısasa kısas: diğer kusurlara kadar işbirliği yapın, ardından misilleme yapın |
| **İklim anlaşmaları** | Kamu Malları oyunu | Serbest sürüş rasyoneldir; yaptırım mekanizmalarına ihtiyaç var |
| **Caydırıcılık** | Tavuk; güvenilir taahhüt | Karşılıklı garantili yıkım bir Nash dengesidir |
---

## Özet
Oyun teorisi, sonucunuzun başkalarının eylemlerine bağlı olduğu stratejik etkileşimleri inceler. Hiçbir oyuncunun yalnızca strateji değiştirmenin fayda sağlamadığı Nash dengesi, merkezi çözüm konseptidir. Mahkumun ikilemi gibi klasik oyunlar, rasyonel bireysel kararların kolektif olarak kötü sonuçlar üretebileceğini göstermektedir. Ardışık oyunlar geriye dönük çıkarımla çözülür. Tekrarlanan oyunlar, gelecekte cezalandırılma tehdidi yoluyla işbirliğini sürdürebilir. Karma stratejiler, öngörülemez kalmak için rastgeleleştirmeyi içerir. Mekanizma tasarımı soruyu tersine çevirir: Sonuçları tahmin etmek yerine, (açık artırmalarda olduğu gibi) istenen sonuçları elde etmek için kurallar tasarlar. Uygulamalar iş (fiyatlandırma, giriş, açık artırmalar), politika (oylama, anlaşmalar), biyoloji (evrimsel kararlı stratejiler) ve günlük yaşamı kapsar. Temel ders, stratejinin sadece ne yaptığınızla ilgili olmadığıdır; başkalarının ne yapacağını tahmin etmek, onların da aynısını yaptığını bilmektir.