<!--
---
# Metadata
title: "Game Theory"
description: "Strategic-form games, Nash equilibrium, dominant strategies, minimax theorem, cooperative games, Shapley value, mechanism design, auction theory, and connections to multi-agent reinforcement learning"
category: "Data Science and Analytics"
subcategory: "Mathematics"
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
    date: "2026-08-10"
    author: "Nepoznato-Dev"
    changes: "Initial deep-dive into game theory"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2027-02-10"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-10"

# Classification
tags: [game-theory, nash-equilibrium, minimax, cooperative-games, shapley-value, mechanism-design, auction-theory, multi-agent-rl]
difficulty_level: "intermediate"
prerequisites:
  - "mathematics.md"
  - "optimization.md"
  - "statistics_and_probability.md"
estimated_reading_time: "25 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Oyun Teorisi
Oyun teorisi, stratejik etkileşimin matematiğidir; sonucunuzun yalnızca kendi seçimlerinize değil, başkalarının seçimlerine de bağlı olduğu durumlar. Şirketler arasındaki fiyat savaşlarından nükleer silah yarışlarına, çevrimiçi müzayedelerden evrimsel biyolojiye kadar oyun teorisi, çatışma ve işbirliğini analiz etmek için araçlar sağlar. Çok aracılı takviyeli öğrenme, üretken çekişmeli ağlar (GAN'ler) ve çevrimiçi platformlar için mekanizma tasarımı yoluyla makine öğrenimiyle giderek daha alakalı hale geldi.
---

## Stratejik Formlu Oyunlar
### Tanım
**Stratejik biçimli (normal biçimli) bir oyun** şunlardan oluşur:
- Bir dizi oyuncu N = {1, 2, ..., n}
- Her oyuncu için strateji S₁, S₂, ..., Sₙ setleri
- Kazanç fonksiyonları u₁, u₂, ..., uₙ strateji profillerini gerçek sayılarla eşleştirir
### Örnek: Mahkumun İkilemi
| | İşbirliği (C) | Kusur (D) |
|---|---------------|------------|
| **İşbirliği Yap (C)** | (−1, −1) | (−3, 0) |
| **Kusur (D)** | (0, −3) | (−2, −2) |
| Analiz | Sonuç |
|----------|-----------|
| Baskın strateji | Kusur (D, her iki oyuncu için de C'ye hakimdir) |
| Nash dengesi | (D, D) getirisi olan (−2, −2) |
| Sosyal optimum | (C, C) getirisi olan (−1, −1) |
| İkilem | Bireysel rasyonellik kolektif mantıksızlığa yol açar |
### Daha Fazla Klasik Oyun
**Cinsiyetlerin Savaşı:**
| | Opera | Futbol |
|---|----------|----------|
| Opera | (2, 1) | (0, 0) |
| Futbol | (0, 0) | (1, 2) |
İki Nash dengesi: (Opera, Opera) ve (Futbol, ​​Futbol).
**Tavuk (Şahin-Güvercin):**
| | Şahin | Güvercin |
|---|------|------|
| Şahin | (−10, −10) | (5, 0) |
| Güvercin | (0, 5) | (1, 1) |
İki Nash dengesi: (Şahin, Güvercin) ve (Güvercin, Şahin).
---

## Baskın Stratejiler
| Konsept | Tanımı |
|-----------|------------|
| **Kesinlikle baskın** | Strateji sᵢ, rakiplerin tercihlerinden bağımsız olarak diğer stratejilerden daha yüksek kazanç sağlar |
| **Zayıf baskın** | Strateji en az diğerleri kadar yüksek getiri sağlar ve bazı rakip profilleri için kesinlikle daha yüksektir |
| **Hakim strateji** | Hiçbir zaman en iyi tepki olmayan bir strateji |
**Domine edilen stratejilerin tekrar tekrar ortadan kaldırılması:**
1. Kesinlikle domine edilen stratejileri kaldırın
2. Artık kaldırılmayana kadar tekrarlayın
3. Eğer tek bir strateji profili kalırsa, bu benzersiz Nash dengesidir
---

## Nash dengesi
**Nash dengesi**, hiçbir oyuncunun stratejisini tek taraflı olarak değiştirerek kazancını artıramayacağı bir strateji profilidir.
### Tanım
(s₁*, s₂*, ..., sₙ*) her oyuncu i için aşağıdaki durumda bir Nash dengesidir:
uᵢ(sᵢ*, s₋ᵢ*) ≥ uᵢ(sᵢ, s₋ᵢ*) tüm sᵢ ∈ Sᵢ için
### Nash Dengelerini Bulma (2×2 Oyunlar)
**En iyi yanıt yöntemi:**
1. Her sütun için 1. oyuncunun en iyi tepkisinin altını çizin
2. Her satırda 2. oyuncunun en iyi tepkisinin altını çizin
3. Her ikisinin de altı çizili olan hücreler Nash dengesidir
### Varoluş (Nash Teoremi)
Her sonlu oyunun en az bir Nash dengesi vardır (muhtemelen karma stratejilerde).
### Karma Stratejiler
**Karma strateji**, saf stratejiler üzerindeki olasılık dağılımıdır.
| Konsept | Tanımı |
|-----------|------------|
| Karma strateji σᵢ | Sᵢ üzerinden olasılık dağılımı |
| Karma strateji NE | Hiçbir oyuncu karışımını değiştirerek beklenen getiriyi artıramaz |
| Destek | Pozitif olasılıkla oynanan saf stratejiler seti |
**Çalışılan Örnek: Paraların Eşleştirilmesi**
| | Kafalar | Kuyruklar |
|---|-------|-------|
| Kafalar | (1, −1) | (−1, 1) |
| Kuyruklar | (−1, 1) | (1, −1) |
Saf strateji NE yok. Karışık NE: Her ikisi de ½ olasılıkla H ve T oynar.
---

## Minimax Teoremi
### Sıfır Toplamlı Oyunlar
**Sıfır toplamlı oyunda**, bir oyuncunun kazancı tam olarak diğerinin kaybıdır: u₁ + u₂ = 0.
### Von Neumann'ın Minimax Teoremi
Her sonlu iki oyunculu sıfır toplamlı oyun için:
max_{σ₁} min_{σ₂} u₁(σ₁, σ₂) = min_{σ₂} max_{σ₁} u₁(σ₁, σ₂)
**maximin** (oyuncu 1 için en kötü durum) **minimax**'a (oyuncu 2 için en iyi en kötü durum) eşittir. Bu ortak değer **oyunun değeridir**.
### Sıfır Toplamlı Oyunları Çözme
Matrisli 2×2 sıfır toplamlı bir oyun için:
| | L | R |
|---|---|---|
| T | bir | b |
| B | c | d |
Oyuncu 1'in optimal karma stratejisi: p = (d−c)/((a−b)+(d−c)) olasılıkla T oynayın
Oyun değeri: v = (ad−bc)/((a−b)+(d−c))
---

## Kapsamlı Form Oyunları
Sıralı hamlelere sahip oyunlar **oyun ağaçları** olarak temsil edilir.
### Temel Kavramlar
| Konsept | Tanımı |
|-----------|------------|
| **Oyun ağacı** | Olası tüm hamle dizilerini gösteren ağaç |
| **Bilgi seti** | Bir oyuncunun ayırt edemeyeceği düğümler kümesi |
| **Mükemmel bilgi** | Her bilgi kümesi bir tekildir (tüm hareketler gözlemlenebilir) |
| **Alt oyun mükemmel NE** | Her alt oyunda Nash dengesi |
| **Geriye dönük çıkarım** | Ağacın sonundan geriye doğru çözün |
### Zermelo Teoremi
Sonlu, mükemmel bilgi içeren, şansı olmayan iki oyunculu oyunlarda: ya bir oyuncunun kazanma stratejisi vardır ya da her ikisi de beraberliği zorlayabilir (örneğin satranç).
---

## İşbirliği Oyunları
**İşbirlikçi oyunlarda** oyuncular bağlayıcı anlaşmalar ve koalisyonlar kurabilirler.
### Karakteristik Fonksiyon
İşbirliğine dayalı bir oyun **karakteristik fonksiyon** v: 2^N → ℝ ile tanımlanır; burada v(S), S'nin elde edebileceği değer koalisyonudur.
| Emlak | Tanımı |
|----------|---------------|
| **Süper katkı maddesi** | ayrık S, T için v(S ∪ T) ≥ v(S) + v(T) |
| **Dışbükey** | S ⊂ T için v(S ∪ {i}) − v(S) ≤ v(T ∪ {i}) − v(T) |
### Çekirdek
**Çekirdek**, hiçbir koalisyonun ayrılarak gelişemeyeceği tahsisler kümesidir:
Çekirdek = {x ∈ ℝⁿ : Σᵢ∈N xᵢ = v(N), Σᵢ∈S xᵢ ≥ v(S) tüm S ⊂ N için}
Çekirdek boş olabilir; bu durumda istikrarlı bir tahsis mevcut değildir.
### Shapley Değeri
**Shapley değeri**, marjinal katkılara dayalı olarak benzersiz bir adil dağıtım sağlar:
φᵢ = Σ_{S ⊂ N\{i}} (|S|!(n−|S|−1)!/n!) · [v(S ∪ {i}) − v(S)]
| Emlak | Açıklama |
|----------|-----------|
| Verimlilik | Σ φᵢ = v(N) (tüm değerler dağıtılır) |
| Simetri | Eşit katkıda bulunanlar eşit kazanç elde eder |
| Kukla oyuncu | Katkıda bulunmayanlar sıfır alır |
| Toplanabilirlik | φ(v + w) = φ(v) + φ(w) |
**Yorum:** Her oyuncunun Shapley değeri, koalisyon oluşumuna ilişkin olası tüm sıralamalardaki ortalama marjinal katkısıdır.
### Çalışılan Örnek
Üç oyuncu: v(∅) = 0, v({1}) = 0, v({2}) = 0, v({3}) = 0, v({1,2}) = 50, v({1,3}) = 70, v({2,3}) = 60, v({1,2,3}) = 100.
| Oyuncu | Marjinal katkılar (sıralamalara göre ortalama) | Shapley değeri |
|----------|-----------------------------------------------------|---------------|
| 1 | (100+50+70+70+50+0)/6 = 56,7 | 37.5 |
| 2 | (100+50+60+60+50+0)/6 | 27.5 |
| 3 | (100+70+60+70+60+0)/6 | 35.0 |
(Her permütasyon için Shapley formülü kullanılarak kesin olarak hesaplanır.)
---

## Mekanizma Tasarımı
**Mekanizma tasarımı** "ters oyun teorisidir"; verilen oyunları analiz etmek yerine, istenen sonuçları üreten oyunlar tasarlar.
### Vahiy Prensibi
İstenilen sonuca ulaşan herhangi bir mekanizma, doğruyu söylemenin bir Nash dengesi olduğu **doğrudan açıklama mekanizması** ile değiştirilebilir.
### Açık Artırma Teorisi
| Açık Artırma Türü | Kurallar | Gelir Denkliği |
|---------------|----------|----------|
| **İlk fiyat kapalı teklif** | En yüksek teklifi veren kazanır, teklifini öder | Tüm standart açık artırmalar aynı beklenen geliri sağlar |
| **İkinci fiyat kapalı teklif (Vickrey)** | En yüksek teklifi veren kazanır, ikinci en yüksek teklifi öder | (bağımsız özel değerler altında) |
| **İngilizce (artan)** | Fiyat yükselir; ilk kabul eden kazanır | — |
| **Hollandaca (azalan)** | Fiyat düşer; ilk kabul eden kazanır | — |
### Vickrey Açık Artırma (İkinci Fiyat)
**Baskın strateji:** Gerçek değerinizi teklif edin.
| Emlak | Açıklama |
|----------|-----------|
| Doğru teklif | Zayıf baskın strateji |
| Verimlilik | Ürün en yüksek değeri teklif edene gider |
| Gelir | İlk fiyatla aynı beklenen gelir (Gelir Denklik Teoremi) |
### Optimum Açık Artırma Tasarımı (Myerson)
Geliri maksimize eden açık artırma:
- **sanal değerleme** en yüksek olan teklif sahibine tahsis edilir
- Bir rezerv fiyatı belirler
- Sanal değerleme: ψ(v) = v − (1−F(v))/f(v)
---

## Makine Öğrenimine Bağlantılar
### Üretken Rekabetçi Ağlar (GAN'lar)
GAN'lar, jeneratör G ile ayırıcı D arasındaki iki oyunculu bir oyundur:
min_G max_D V(D, G) = E[log D(x)] + E[log(1 − D(G(z))))]
| Oyun Teorisi Konsepti | GAN Eşdeğeri |
|----------------------|-----------------|
| İki oyunculu sıfır toplamlı oyun | Jeneratör ve Ayırıcı |
| Nash dengesi | G gerçek veriler üretir, D her yerde ½ çıktı verir |
| Minimaks | GAN amaç fonksiyonu |
| Mod daralt | Dengeye Ulaşılamaması |
### Çok Aracılı Takviyeli Öğrenme (MARL)
| Konsept | MARL Başvurusu |
|-----------|------|
| Nash dengesi | Çoklu aracı ayarlarında kararlı politikalar |
| Minimaks | Rakip rakiplere karşı sağlam politikalar |
| İşbirliğine dayalı oyunlar | Koalisyon oluşumu, görev dağılımı |
| Shapley değeri | Kredi tahsisi (hangi temsilci ne katkıda bulundu?) |
| Mekanizma tasarımı | Çok aracılı sistemlerde teşviklerin tasarlanması |
| Kurgusal oyun | Nash dengesine yakınlaşan öğrenme algoritması |
### Diğer ML Bağlantıları
| Başvuru | Oyun Teorisi Aracı |
|---------------|------|
| Reklam açık artırma tasarımı (Google, Facebook) | Mekanizma tasarımı, açık artırma teorisi |
| Pazar yeri tasarımı (Uber, Airbnb) | Eşleştirme teorisi, mekanizma tasarımı |
| Rakiplere karşı sağlamlık | Saldıran ve savunan arasındaki sıfır toplamlı oyunlar |
| Fuar bölümü | Shapley değeri, kıskançlıktan uzak tahsis |
| Birleşik öğrenme | Katkı ölçümü için işbirlikçi oyun teorisi |
| Öneri sistemleri | Doğru tercihlerin ortaya çıkarılması için mekanizma tasarımı |
---

## Özet
| Konsept | Temel Fikir | Temel Sonuç |
|-----------|-----------|------------|
| Stratejik biçimli oyunlar | Oyuncular, stratejiler, getiriler | Oyun matrisi gösterimi |
| Baskın stratejiler | Başkalarından bağımsız olarak en iyisi | Yinelenen eleme |
| Nash dengesi | Kârlı tek taraflı sapma yok | Her sonlu oyunda mevcuttur |
| Karma stratejiler | Eylemler arasında rastgele seçim yap | Nash'in varoluş teoremi |
| Minimaks | En iyi en kötü durum (sıfır toplam) | Von Neumann'ın minimax teoremi |
| Kapsamlı biçim | Sıralı hareketler | Geriye dönük çıkarım, alt oyun mükemmelliği |
| İşbirliğine dayalı oyunlar | Bağlayıcı koalisyonlar | Çekirdek, Shapley değeri |
| Mekanizma tasarımı | Sonuçlara yönelik oyunlar tasarlayın | Vahiy ilkesi, optimal açık artırmalar |
| Açık artırma teorisi | Rekabet Yoluyla Satış | Gelir denkliği, Vickrey açık artırması |
Oyun teorisi stratejik düşünmenin matematiğidir. Etkileşim halindeki yapay zeka aracıları, otomatikleştirilmiş pazar yerleri ve rakip sistemlerle giderek daha fazla nüfuslanan bir dünyada oyun teorisi, davranışı tahmin etmek, mekanizmalar tasarlamak ve sağlam çoklu aracılı sistemler oluşturmak için temel araç setini sağlar. Veri bilimcileri için GAN'ların nasıl çalıştığını, çevrimiçi açık artırmaların nasıl milyarlarca gelir sağladığını ve rekabetçi ortamlarda iyi performans gösteren yapay zeka sistemlerinin nasıl oluşturulacağını açıklıyor.