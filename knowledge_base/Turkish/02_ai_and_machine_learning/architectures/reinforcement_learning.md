---
# Metadata
title: "Reinforcement Learning"
description: "MDPs, Q-learning, policy gradients, RLHF, multi-agent systems"
category: "AI and Machine Learning"
subcategory: "Model Architectures"
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
    changes: "Moved to architectures/ subfolder; added subcategory field"
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
tags: [reinforcement, learning, ai-and-machine-learning]
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
# Takviyeli Öğrenme
Takviyeli öğrenme (RL), makinelerin deneme yanılma yoluyla bir dizi karar almayı öğrenmesidir. Her örnek için doğru cevabın sağlandığı denetimli öğrenmenin aksine, RL aracıya yalnızca bir ödül sinyali verir ve aracının zaman içinde hangi eylemlerin en iyi sonuçlara yol açtığını bulması gerekir. AlphaGo'nun, robotik kontrolün, oyun oynayan yapay zekanın ve modern büyük dil modellerini insan tercihleriyle uyumlu hale getirmek için kullanılan teknik olan RLHF'nin arkasındaki yaklaşım budur.
---

## Temel Kavramlar
RL, karar almayı bir **temsilci** ile **ortam** arasındaki bir döngü olarak çerçeveler.
| Bileşen | Rol | Örnek |
|-----------|------|-----------|
| **Acente** | Karar verici | Bir satranç programı, bir robot, bir dil modeli |
| **Çevre** | Temsilcinin etkileşimde bulunduğu dünya | Satranç tahtası, depo, sohbet |
| **Devlet** | Mevcut durum | Pano konumu, robot sensörü okumaları, sohbet geçmişi |
| **Eylem** | Acentenin yapabilecekleri | Bir parçayı hareket ettirin, sola dönün, jeton oluşturun |
| **Ödül** | Geri bildirim sinyali (skaler sayı) | Kazanmak için +1, çökmek için -1, insan tercihi puanı |
| **Politika** | Durumları eylemlerle eşleyen strateji | "Kral tehdit edilirse hareket ettirin" |
| **Değer işlevi** | Bir eyaletten beklenen kümülatif ödül | "Bu tahta pozisyonu yaklaşık +3 puan değerinde" |
### RL Döngüsü
```
Agent observes State → chooses Action → Environment returns new State + Reward
        ↑                                                                         |
        └─────────────────────────────────────────────────────────────────────────┘
```

Temsilcinin hedefi, yalnızca anlık ödülü değil, zaman içinde **kümülatif ödülü** en üst düzeye çıkarmaktır. RL'yi denetimli öğrenmeden temel olarak farklı kılan şey budur.
---

## Diğer Öğrenme Paradigmalarından Temel Farklılıklar
| Görünüş | Denetimli Öğrenme | Denetimsiz Öğrenme | Takviyeli Öğrenme |
|----------|-----------|---------------------|-----------|
| **Sinyal** | Her örnek için doğru etiketler | Etiket yok; yapıyı bul | Skaler ödül, sıklıkla gecikmeli |
| **Geri bildirim** | Hemen | Yok | Gecikmeli ve seyrek |
| **Sıra** | Her örnek bağımsızdır | Her örnek bağımsızdır | Eylemler gelecekteki durumları etkiler |
| **Gol** | Tahmin hatasını en aza indirin | Desenleri keşfedin | Kümülatif ödülü en üst düzeye çıkarın |
---

## Markov Karar Süreçleri (MDP'ler)
MDP'ler RL'nin matematiksel çerçevesidir. Geleceğin, oraya nasıl ulaştığınızın geçmişine (**Markov özelliği**) değil, yalnızca mevcut duruma bağlı olduğunu varsayıyorlar.
| Bileşen | Gösterim | Anlamı |
|-----------|----------|-----------|
| **Eyaletler** | S | Temsilcinin içinde bulunabileceği tüm olası durumlar |
| **Eylemler** | bir | Temsilcinin yapabileceği her şey |
| **Geçiş işlevi** | P(s' \| s, a) | s durumunda a eylemi yapıldıktan sonra s' durumuna ulaşma olasılığı |
| **Ödül işlevi** | R(s, a, s') | Geçiş için alınan ödül |
| **İndirim faktörü** | γ (gamma) | Gelecekteki ödüllere, anlık olanlara göre ne kadar değer verilecek (0'dan 1'e) |
**Getiri** (toplam indirimli ödül):
```
G = R₁ + γR₂ + γ²R₃ + ...
```

Yüksek indirim faktörü (γ 1'e yakın), temsilcinin ileri görüşlü olduğu anlamına gelir. Düşük olanı, kısa görüşlü olduğu anlamına gelir.
---

## Klasik RL Algoritmaları
### Değer Tabanlı Yöntemler
Bunlar her bir durumun (veya durum-eylem çiftinin) ne kadar iyi olduğunu öğrenir.
| Algoritma | Anahtar Fikir | Sınırlama |
|-----------|----------|------------|
| **Q-Öğrenim** | Q değerleri tablosunu öğrenin: Q(durum, eylem) = beklenen ödül | Büyük durum alanlarına ölçeklenmiyor |
| **Derin Q-Ağı (DQN)** | Q değerlerine yaklaşmak için bir sinir ağı kullanın | Yalnızca ayrı eylemleri yönetir; kararsız olabilir |
| **Çift DQN** | Q-öğrenmenin aşırı tahmin önyargısını düzeltin | Hala ayrık eylemlerle sınırlı |
Q-öğrenme güncelleme kuralı:
```
Q(s, a) ← Q(s, a) + α [r + γ max Q(s', a') - Q(s, a)]
```

### Politika Tabanlı Yöntemler
Bunlar değerleri tahmin etmeden doğrudan politikayı (stratejiyi) öğrenirler.
| Algoritma | Anahtar Fikir | Avantajı |
|-----------|----------|-----------|
| **GÜÇLENDİR** | Monte Carlo politikasının eğimi; politikayı iyi sonuçlar doğrultusunda güncelleme | Basit; sürekli eylemlerle çalışır |
| **PPO** (Yakın Politika Optimizasyonu) | Büyük, istikrarı bozan değişiklikleri önlemek için politika güncellemelerini kırpın | Stabil; yaygın olarak kullanılır; iyi varsayılan |
| **TRPO** | İlke güncellemeleri için güven bölgesi yöntemi | PPO'dan daha ilkeli; uygulaması daha zor |
### Aktör-Eleştirmen Yöntemleri
İkisinin de en iyilerini birleştirin: bir **aktör** (politika) ve bir **eleştirmen** (değer işlevi).
| Algoritma | Anahtar Fikir |
|---------------|----------|
| **A2C / A3C** | Avantaj Oyuncu-Eleştirmen; varyansı azaltmak için avantaj tahminini kullanır |
| **SAC** (Yumuşak Aktör-Eleştirmen) | Keşfi sürdürürken ödülü en üst düzeye çıkarın (entropi düzenlemesi) |
| **TD3** (İkiz Gecikmeli DDPG) | Sürekli eylem alanlarında aşırı tahminin ele alınması |
---

## RLHF: İnsan Geri Bildiriminden Takviyeli Öğrenme
RLHF, ChatGPT'yi mümkün kılan tekniktir. Metni tahmin edebilen bir model ile insanların gerçekten yararlı bulduğu çıktılar üreten bir model arasındaki boşluğu dolduruyor.
### Üç Adım
| Adım | Ne Olur | Çıkış |
|------|-------------|-------|
| **1. Denetimli İnce Ayar (SFT)** | Yüksek kaliteli, insan tarafından yazılmış örnekler üzerinde önceden eğitilmiş bir modele ince ayar yapın | Talimatları oldukça iyi takip eden bir model |
| **2. Ödül Modeli Eğitimi** | İnsanlar model çıktı çiftlerini karşılaştırır; insan tercihlerini tahmin edecek bir model eğitmek | Çıktı kalitesini puanlayan bir ödül modeli |
| **3. RL Optimizasyonu** | Ödül modelinin puanlarını en üst düzeye çıkarmak amacıyla SFT modelinde ince ayar yapmak için PPO'yu kullanın | İnsan tercihlerine uygun bir model |
### RLHF Neden Önemlidir
RLHF olmadan dil modeli, her kitabı okumuş ancak bir konuşma sırasında nasıl davranacağını bilmeyen bir öğrenciye benzer. Metin üretebilir ancak metin yararsız olabilir, zehirli olabilir veya asıl amacı tamamen gözden kaçırabilir. RLHF modele *insanların ne istediğini* öğretir; yalnızca metnin neye benzediğini değil.
### Varyantlar ve Alternatifler
| Yöntem | Açıklama | Avantajı |
|----------|----------------|-----------|
| **DPO** (Doğrudan Tercih Optimizasyonu) | Ödül modelini atlayın; politikayı doğrudan insan tercihlerine göre optimize edin | Daha basit; eğitilecek ayrı bir ödül modeli yok |
| **RLAIF** | Tercih etiketleri oluşturmak için yapay zekayı (insanlar yerine) kullanın | İnsan etiketlemesinden daha ucuz |
| **Anayasal AI** | İnsan etiketleri olmadan model davranışını yönlendirmek için bir dizi ilke kullanın | Daha ölçeklenebilir; Antropik'in yaklaşımı |
| **GRPO** (Grup Göreli Politika Optimizasyonu) | Çıktıları ayrı bir model yerine bir grup içinde karşılaştırın | DeepSeek-R1'de kullanılır; değer ağına olan ihtiyacı azaltır |
---

## Keşif ve Sömürü
Bu RL'deki merkezi gerilimdir. **Sömürü** işe yaradığını bildiğiniz eylemleri seçmek anlamına gelir. **Keşif** potansiyel olarak daha iyi stratejiler keşfetmek için yeni şeyler denemek anlamına gelir.
| Strateji | Nasıl Çalışır | Takas |
|----------|----------------|-----------|
| **ε-açgözlü** | Çoğu zaman en iyi eylemi seçin; olasılıklı rastgele eylem ε | Basit ama verimsiz |
| **Boltzmann keşfi** | Eylemleri tahmini değerlerine göre olasılıksal olarak seçin | ε-açgözlüden daha pürüzsüz |
| **UCB** (Üst Güven Sınırı) | Belirsizliğin yüksek olduğu eylemleri tercih edin (belirsizlik karşısında iyimserlik) | İyi teorik garantiler |
| **Entropi düzenlemesi** | Farklı eyaletleri ziyaret etmek için bir bonus ekleyin (SAC, PPO'da kullanılır) | Doğal keşifleri teşvik eder |
---

## Çok Aracılı Takviye Öğrenimi
Birden fazla etmen aynı anda öğrendiğinde dinamikler çok daha karmaşık hale gelir.
| Senaryo | Mücadelesi | Örnek |
|----------|-----------|-----------|
| **Kooperatif** | Temsilciler koordine etmelidir; kredi tahsisi zordur | Robot futbol takımları; dağıtılmış sensör ağları |
| **Rekabetçi** | Rakipler uyum sağlıyor; ortam sabit değil | Oyun AI (poker, StarCraft); siber güvenlik |
| **Karışık** | Bazı temsilciler işbirliği yapar, diğerleri rekabet eder | Açık artırma pazarları; trafik sistemleri |
| Algoritma | Açıklama |
|-----------|----------------|
| **MADDPG** | DDPG'nin çok aracılı versiyonu; merkezi eleştirmen, merkezi olmayan aktörler |
| **MAPPO** | Çok aracılı PPO; pratikte yaygın olarak kullanılıyor |
| **Kendi Kendine Oynama** | Temsilciler kendilerinin kopyalarına karşı eğitim alıyor (AlphaGo, AlphaStar) |
---

## Sim'den Gerçeğe Aktarım
Robotları gerçek dünyada eğitmek yavaş ve tehlikelidir. Bunun yerine ajanlar simülasyon konusunda eğitim alıyor ve gerçekliğe transfer oluyor.
| Mücadelesi | Çözüm |
|---------------|----------|
| **Gerçeklik farkı** (simülasyon ≠ gerçek dünya) | Etki alanı rastgeleleştirmesi: eğitim sırasında fizik parametrelerini değiştirin |
| **Numune verimsizliği** | Model tabanlı RL kullanın veya büyük paralel simülasyonlar üzerinde eğitim alın |
| **Güvenlik** | Kısıtlı RL: eğitim sırasında güvenli olmayan eylemleri cezalandırın |
| **Kısmi gözlemlenebilirlik** | Gürültülü sensörler ve gecikmeli gözlemlerle eğitim |
Boston Dynamics ve Tesla gibi şirketler simülasyonu yoğun bir şekilde kullanıyor ancak simüle edilmiş performans ile fiziksel performans arasındaki fark, alanın en büyük zorluklarından biri olmaya devam ediyor.
---

## Araçlar ve Çerçeveler
| Araç | Amaç | En İyisi |
|------|------------|----------|
| **Durağan-Temel Çizgiler3** | PPO, SAC, TD3, DQN'nin temiz Python uygulamaları | Öğrenme ve prototip oluşturma |
| **RLlib** | Ray üzerine inşa edilmiş ölçeklenebilir RL kütüphanesi | Büyük ölçekli dağıtılmış eğitim |
| **TemizRL** | Araştırma için tek dosya uygulamaları | Algoritmaları derinlemesine anlamak |
| **Spor Salonu (OpenAI)** | Standartlaştırılmış ortam arayüzü | RL problemlerini tanımlama |
| **Isaac Spor Salonu / Isaac Laboratuvarı** | GPU ile hızlandırılmış fizik simülasyonu | Robotik, simden gerçeğe |
| **TRL** (Transformer RL Kütüphanesi) | Dil modelleri için RLHF, DPO, PPO | Yüksek Lisans'ları Hizalama |
| **AçıkRLHF** | Dağıtılmış RLHF çerçevesi | Büyük modelleri RLHF ile eğitmek |
---

## Pratik İpuçları
- **PPO ile başlayın.** En güvenilir genel amaçlı algoritmadır. Ne kullanacağınızdan emin değilseniz PPO varsayılandır.
- **Ödüllerinizi normalleştirin.** Ödül ölçeklendirmesi, eğitim istikrarını önemli ölçüde etkiler.
- **Vektörleştirilmiş ortamları kullanın.** Birçok ortamı paralel olarak çalıştırmak (ör. 8-64), eğim tahminlerini dengeler ve eğitimi büyük ölçüde hızlandırır.
- **Hem ödülü hem de entropiyi izleyin.** Entropi sıfıra düşerse, temsilciniz araştırmayı bırakmıştır ve yerel bir optimumda sıkışıp kalmış olabilir.
- **Ödül şekillendirme bir sanattır.** Doğru ödül fonksiyonunu tasarlamak çoğu zaman en zor kısımdır. Az sayıda ödül (yalnızca sonunda) öğrenmeyi aşırı derecede yavaşlatır. Yoğun, iyi şekillendirilmiş ödüller temsilciye rehberlik eder ancak istenmeyen davranışlara yol açabilir.
- **RLHF hassastır.** Ödül modelinde veya PPO hiperparametrelerinde yapılan küçük değişiklikler, büyük kalite düşüşlerine neden olabilir. Tam RLHF hattına ihtiyacınız yoksa DPO daha kararlı bir alternatiftir.
---

## Özet
Takviyeli öğrenme, etmenlerin etkileşim yoluyla karar vermeyi nasıl öğrendiklerinin incelenmesidir. Q-öğrenme gibi klasik algoritmalardan PPO ve SAC gibi modern derin RL yöntemlerine kadar uzanır ve oyun oynamaktan dil modeli hizalamaya kadar yapay zekadaki en önemli son gelişmelerin bazılarının temelini oluşturur. Temel zorluk aynı kalıyor: Geri bildirim geciktiğinde, seyrek ve gürültülü olduğunda en uygun davranışı nasıl öğrenirsiniz? Cevabın (akıllı matematik tarafından yönlendirilen deneme yanılma) yapay zekanın en güçlü fikirlerinden biri olduğu ortaya çıkıyor.