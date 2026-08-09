---
# Metadata
title: "Data Structures and Algorithms"
description: "Arrays, trees, graphs, sorting, searching, complexity"
category: "Coding and Technology"
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
reviewed_by: "Coding & Technology Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [data, structures, algorithms, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "6 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Veri Yapıları ve Algoritmalar
Veri yapıları, bellekteki verileri, üzerinde yapılan işlemlerin verimli olmasını sağlayacak şekilde düzenlemenin yollarıdır. Algoritmalar problemlerin çözümü için adım adım uygulanan prosedürlerdir. Birlikte bilgisayar biliminin temelini oluştururlar; şimdiye kadar kullandığınız her program bunlara dayanır. Doğru veri yapısını seçmek inanılmaz derecede yavaş bir programı hızlı bir programa dönüştürebilir ve doğru algoritmayı bilmek çözülemeyen bir sorunu önemsiz bir soruna dönüştürebilir.
---

## Temel Veri Yapıları
### Doğrusal Yapılar
| Yapı | Erişim | Ara | Ekle | Sil | Kullanım Örneği |
|-----------|-----------|-----------|-----------|-----------|----------|
| **Dizi** | O(1) dizine göre | O(n) | O(n) | O(n) | Sabit boyutlu koleksiyonlar; rastgele erişim |
| **Bağlantılı Liste** | O(n) | O(n) | O(1) başta | O(1) başta | Dinamik boyut; ekleme/silme |
| **Yığın** | O(n) | O(n) | O(1) bas/aç | O(1) pop | İşlev çağrıları; geri al; ayrıştırma |
| **Sıra** | O(n) | O(n) | O(1) kuyruğa alma | O(1) kuyruktan çıkarma | Görev planlama; BFS; mesaj kuyrukları |
| **Deque** | O(1) her iki uçta | O(n) | O(1) her iki uçta | O(1) her iki uçta | Sürgülü pencere; iş hırsızlığı |
### Hash Tabanlı Yapılar
| Yapı | Ara | Ekle | Sil | Kullanım Örneği |
|-----------|-----------|-----------|-----------|----------|
| **Karma Tablosu** | O(1) ortalama | O(1) ortalama | O(1) ortalama | Anahtar/değer aramaları; önbellekler; setleri |
| **Karma Kümesi** | Ç(1) | Ç(1) | Ç(1) | Üyelik testi; tekilleştirme |
**Karma çarpışmaları**: İki anahtar aynı yuvaya karma oluşturduğunda, bağlantılı bir listede (zincirleme) veya bir sonraki kullanılabilir yuvada (açık adresleme) depolanırlar. İyi hash fonksiyonları çarpışmaları en aza indirir.
### Ağaç Yapıları
| Yapı | Ara | Ekle | Sil | Kullanım Örneği |
|-----------|-----------|-----------|-----------|----------|
| **İkili Arama Ağacı** | O(log n) ortalama | O(log n) | O(log n) | Sıralanmış veriler; aralık sorguları |
| **AVL / Kırmızı-Siyah Ağaç** | O(log n) garantili | O(log n) | O(log n) | Kendini dengeleme; haritalarda/setlerde kullanılır |
| **B-Ağaç / B+ Ağaç** | O(log n) | O(log n) | O(log n) | Veritabanı indeksleri; dosya sistemleri |
| **Trie** | O(k) burada k = anahtar uzunluğu | O(k) | O(k) | Otomatik tamamlama; önek eşleştirme |
| **Yığın (İkili)** | O(n) | O(log n) | O(log n) | Öncelik kuyrukları; planlama |
### Grafik Gösterimleri
| Temsil | Uzay | Kenar Arama | Kenar Ekle | Yinelenen Komşular |
|---------------|----------|------------|----------|--------|
| **Bitişiklik matrisi** | O(V²) | Ç(1) | Ç(1) | Ç(V) |
| **Komşuluk listesi** | O(V + E) | O(derece) | Ç(1) | O(derece) |
| **Kenar listesi** | Ç(E) | Ç(E) | Ç(1) | Ç(E) |
---

## Algoritma Karmaşıklığı (Büyük-O)
Big-O notasyonu, girdi boyutu arttıkça bir algoritmanın zaman veya alan gereksinimlerinin nasıl büyüdüğünü açıklar.
| Karmaşıklık | İsim | Örnek |
|-----------|------|-----------|
| **O(1)** | Sabit | Karma tablo araması; indekse göre dizi erişimi |
| **O(log n)** | Logaritmik | İkili arama; dengeli ağaç işlemleri |
| **O(n)** | Doğrusal | Doğrusal arama; bir dizi yineleniyor |
| **O(n log n)** | Doğrusal | Sıralamayı birleştir; yığın sıralaması; en verimli genel amaçlı çeşitler |
| **O(n²)** | İkinci Dereceden | Kabarcık sıralaması; aynı veriler üzerinde iç içe geçmiş döngüler |
| **O(2^n)** | Üstel | Kaba kuvvet altkümesi üretimi; saf yinelemeli Fibonacci |
| **O(n!)** | Faktöriyel | Gezgin satıcı (kaba kuvvet); permütasyonlar |
### Yaygın Yanlış Kanılar
| Yanlış anlama | gerçeklik |
|-------------|------------|
| "O(n) her zaman O(n²)'den daha hızlıdır" | Küçük n için sabit faktör daha önemlidir |
| "Düşük Big-O her zaman daha iyidir" | Uzay-zaman değiş tokuşları mevcuttur; O(1) araması O(n) belleğini kullanır |
| "Big-O size tam hızı söyler" | Mutlak zamanı değil, büyüme oranını tanımlar |
---

## Sıralama Algoritmaları
| Algoritma | En İyi | Ortalama | En kötü | Uzay | Kararlı | Yerinde |
|-----------|------|-----------|----------|-------|-----------|----------|
| **Kabarcık Sıralaması** | O(n) | O(n²) | O(n²) | Ç(1) | Evet | Evet |
| **Ekleme Sıralaması** | O(n) | O(n²) | O(n²) | Ç(1) | Evet | Evet |
| **Seçim Sıralaması** | O(n²) | O(n²) | O(n²) | Ç(1) | Hayır | Evet |
| **Birleştir Sırala** | O(n log n) | O(n log n) | O(n log n) | O(n) | Evet | Hayır |
| **Hızlı Sıralama** | O(n log n) | O(n log n) | O(n²) | O(log n) | Hayır | Evet |
| **Yığın Sıralaması** | O(n log n) | O(n log n) | O(n log n) | Ç(1) | Hayır | Evet |
| **Tim Sıralaması** | O(n) | O(n log n) | O(n log n) | O(n) | Evet | Hayır |
**Pratik tavsiye**: Dilinizin yerleşik sıralamasını kullanın (Python'un`sorted()`, JavaScript'in`Array.sort()`). Tüm uç durumları ele alan yüksek düzeyde optimize edilmiş algoritmalar (Tim Sort, Introsort) kullanırlar.
---

## Arama Algoritmaları
| Algoritma | Veri Yapısı | Karmaşıklık | Gereksinim |
|-----------|---------------|-----------|---------------|
| **Doğrusal arama** | Herhangi biri | O(n) | Yok |
| **İkili arama** | Sıralanmış dizi | O(log n) | Veriler sıralanmalıdır |
| **Karma tablo araması** | Hash tablosu | O(1) ortalama | İyi karma işlevi |
| **BFS** (Genişlik-Önce Arama) | Grafik / ağaç | O(V + E) | Ağırlıklandırılmamış en kısa yol |
| **DFS** (Derinlik-Önce Arama) | Grafik / ağaç | O(V + E) | Yol bulma; döngü tespiti |
| **Dijkstra'nın** | Ağırlıklı grafik | O((V + E) log V) | Negatif olmayan ağırlıklar; en kısa yol |
| **A* Arama** | Ağırlıklı grafik | O((V + E) log V) | Sezgisel kılavuzlu; kabul edilebilir buluşsal yöntemle optimal |
---

## Anahtar Algoritma Modelleri
| Desen | Açıklama | Örnek Sorunlar |
|-----------|---------------|------|
| **Böl ve yönet** | Problemi alt problemlere ayırın; yinelemeli olarak çöz; birleştirme | Sıralamayı birleştir; hızlı sıralama; ikili arama |
| **Dinamik programlama** | Örtüşen alt problemlere bölün; önbellek sonuçları | Fibonacci; sırt çantası; en uzun ortak alt dizi |
| **Açgözlü** | Her adımda yerel olarak en uygun seçimi yapın | Dijkstra'nın; Huffman kodlaması; aktivite seçimi |
| **Geri izleme** | Olasılıkları deneyin; kötü seçimleri geri alın; alternatifleri deneyin | Sudoku çözücü; N-kraliçeler; permütasyonlar |
| **Sürgülü pencere** | Bir öğe penceresini koruyun; veriler üzerinde kaydırın | K boyutunun maksimum toplam alt dizisi; tekrarsız en uzun alt dize |
| **İki işaretçi** | Birbirine doğru veya aynı yönde hareket eden iki işaretçiyi kullanın | Sıralanmış dizideki çift toplamı; kopyaları kaldır |
| **Cevapta ikili arama** | Cevap alanında ikili arama | Minimum sayfaları tahsis edin; agresif inekler |
---

## Ne Zaman Ne Kullanılmalı
| Sorun | Veri Yapısı | Algoritma |
|-----------|---------------|-----------|
| Hızlı anahtar/değer araması | Hash tablosu / sözlük | Karma |
| Sıralanmış düzeni koru | Dengeli BST (TreeMap, std::set) | Ağaç işlemleri |
| Önceliğe dayalı işleme | Yığın/öncelik kuyruğu | Yığın işlemleri |
| En kısa yol (ağırlıklandırılmamış) | Grafik (komşuluk listesi) | BFS |
| En kısa yol (ağırlıklı) | Grafik (komşuluk listesi) | Dijkstra'nın / A* |
| Üyelik testi | Hash seti / Bloom filtresi | Karma |
| Önek eşleştirme | Trie | Üç geçiş |
| Aralık sorguları | Segment ağacı / Fenwick ağacı | Ağaç işlemleri |
| LRU önbelleği | Hash haritası + çift bağlantılı liste | Kombine operasyonlar |
| Bağlı bileşenler | Ayrık Küme Birliği (Birleşim-Bul) | Birleştir ve Bul |
---

## Özet
Veri yapıları ve algoritmalar yalnızca görüşme konuları değildir; verimli yazılımın yapı taşlarıdır. Diziler ve karma tablolar günlük ihtiyaçların çoğunu karşılar. Ağaçlar ve grafikler hiyerarşik ve ilişkisel verileri işler. Sıralama ve arama, standart kütüphanelerdeki çözülmüş problemlerdir. Algoritmik kalıplar (böl ve yönet, dinamik programlama, açgözlülük, geri izleme) yeni sorunların üstesinden gelmek için yeniden kullanılabilir stratejilerdir. Anahtar beceri algoritmaları ezberlemek değil; belirli bir soruna hangi modelin uyduğunu tanımak ve iş için doğru veri yapısını seçmektir.