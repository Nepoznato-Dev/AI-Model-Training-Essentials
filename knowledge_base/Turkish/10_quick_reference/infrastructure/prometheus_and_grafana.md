---
# Metadata
title: "Prometheus and Grafana"
description: "PromQL, exporters, dashboards, alerting, monitoring stack"
category: "Quick Reference"
subcategory: "Infrastructure"
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
    changes: "Moved to infrastructure/ subfolder; added subcategory field"
  - version: "1.0.0"
    date: "2026-08-05"
    author: "Nepoznato-Dev"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-09"
review_date: "2027-02-05"
reviewed_by: "Quick Reference Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [prometheus, grafana, quick-reference]
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
# Prometheus ve Grafana
Prometheus, güvenilirlik ve ölçeklenebilirlik için tasarlanmış açık kaynaklı bir izleme ve uyarı araç setidir. Grafana, zaman serisi verilerini görselleştirmek için önde gelen açık kaynaklı platformdur. Birlikte modern altyapı ve uygulamalar için en popüler izleme yığınını oluştururlar. Prometheus metrikleri toplar ve saklar; Grafana bunları kontrol panellerinde görüntüler.
---

## Prometheus Mimarisi
| Bileşen | Açıklama |
|-----------|----------------|
| **Prometheus sunucusu** | Metrikleri hedeflerden sıyırır; zaman serisi verilerini saklar; uyarı kurallarını değerlendirir |
| **İhracatçı** | Bir sistemdeki ölçümleri ortaya çıkarır (Node Exporter, cAdvisor, vb.) |
| **İtme Geçidi** | Kısa ömürlü işlerden (toplu işler, CI) ölçümler alır |
| **Uyarı yöneticisi** | Uyarıları yönetir: gruplama, susturma, yönlendirme, engelleme |
| **Hizmet keşfi** | Hedefleri otomatik olarak keşfeder (Kubernetes, Consul, EC2, vb.) |
---

## Temel Kavramlar
| Konsept | Açıklama |
|-----------|------------|
| **Metrik** | İsteğe bağlı etiketler ve değer içeren adlandırılmış bir ölçüm |
| **Zaman serisi** | Belirli bir metrik + etiket kombinasyonuna ilişkin veri noktaları akışı |
| **İş** | Aynı amaca yönelik hedeflerden oluşan bir koleksiyon |
| **Örnek** | Kazınacak tek bir hedef (genellikle bir süreç) |
| **Kazıyın** | Prometheus düzenli aralıklarla bir hedeften metrikler çekiyor |
| **Etiket** | Bir metriği boyutlandıran anahtar/değer çifti (ör.`method="GET"`) |
| **Örnek** | Zamanın belirli bir noktasındaki değer: (zaman damgası, değer) |
---

## Metrik Türleri
| Tür | Açıklama | Kullanım Örneği |
|------|-----------------|----------|
| **Sayaç** | Monoton olarak artan değer (yalnızca artar) | Talep sayısı; hatalar; tamamlanan görevler |
| **Gösterge** | Yukarı veya aşağı gidebilen değer | Sıcaklık; hafıza kullanımı; kuyruk uzunluğu |
| **Histogram** | Değere göre gruplandırılmış gözlemler | Gecikme isteği; yanıt boyutu |
| **Özet** | Histograma benzer; istemci tarafında yüzdelik dilimleri hesaplar | Gecikme yüzdelik dilimleri |
---

## PromQL (Sorgu Dili)
### Temel Sorgular
| Sorgu | Açıklama |
|----------|----------------|
| `http_requests_total`| Ham zaman serisi |
| `http_requests_total{method="GET"}`| Etikete göre filtrele |
| `http_requests_total{method="GET", status="200"}`| Çoklu etiket filtreleri |
| `rate(http_requests_total[5m])`| 5 dakikanın üzerinde saniye başına oran |
| `increase(http_requests_total[1h])`| 1 saatte toplam artış |
| `sum(rate(http_requests_total[5m])) by (status)`| Duruma göre toplam oran |
| `histogram_quantile(0.95, rate(http_duration_bucket[5m]))`| 95. yüzdelik dilimdeki gecikme |
| `avg(node_cpu_seconds_total{mode="idle"})`| Ortalama CPU boşta |
| `1 - avg(rate(node_cpu_seconds_total{mode="idle"}[5m]))`| CPU kullanımı |
### Ortak İşlevler
| İşlev | Açıklama | Örnek |
|----------|----------------|-----------|
| `rate()`| Saniyede ortalama artış oranı | `rate(requests_total[5m])`|
| `irate()`| Son iki veri noktasına dayalı saniye başına oran | `irate(requests_total[1m])`|
| `increase()`| Zaman aralığına göre toplam artış | `increase(errors_total[1h])`|
| `sum()`| Seriler arası toplam | `sum(rate(requests_total[5m])) by (service)`|
| `avg()`| Seriler genelinde ortalama | `avg(node_memory_usage)`|
| `histogram_quantile()`| Histogramdan niceliği hesaplayın | `histogram_quantile(0.99, rate(duration_bucket[5m]))`|
| `topk()`| Değere göre en iyi K serisi | `topk(5, rate(requests_total[5m]))`|
| `predict_linear()`| Doğrusal tahmin | `predict_linear(disk_usage[1h], 4*3600)`|
| `absent()`| Metriğin eksik olup olmadığını kontrol edin | `absent(up{job="myapp"})`|
---

## Ortak İhracatçılar
| İhracatçı | Neleri İzler |
|----------|----------|
| **Düğüm Aktarıcı** | Linux/Unix ana bilgisayar ölçümleri (CPU, bellek, disk, ağ) |
| **cDanışman** | Kapsayıcı ölçümleri (CPU, bellek, ağ, dosya sistemi) |
| **MySQL Aktarıcı** | MySQL veritabanı ölçümleri |
| **PostgreSQL Aktarıcı** | PostgreSQL veritabanı ölçümleri |
| **Redis İhracatçısı** | Redis metrikleri |
| **Kara Kutu İhracatçısı** | HTTP, HTTPS, DNS, TCP, ICMP üzerinden uç noktaları inceleyin |
| **SNMP Aktarıcı** | SNMP aracılığıyla ağ cihazı ölçümleri |
| **JSON Aktarıcı** | JSON API'lerinden özel ölçümler |
---

## Grafana
### Temel Kavramlar
| Konsept | Açıklama |
|-----------|------------|
| **Veri kaynağı** | Prometheus'a (veya diğer arka uçlara) bağlantı |
| **Kontrol Paneli** | Bir düzende düzenlenmiş paneller koleksiyonu |
| **Panel** | Tek görselleştirme (grafik, gösterge, tablo, ısı haritası) |
| **Değişken** | Gösterge tabloları için dinamik filtre (ör. örnek seç) |
| **Ek açıklama** | Olayları grafiklerde işaretleyin (dağıtımlar, olaylar) |
| **Uyarı kuralı** | Grafana'da eşik tabanlı uyarı |
| **Şablon oluşturma** | Değişkenlerle yeniden kullanılabilir kontrol paneli modelleri |
### Faydalı Kontrol Paneli Modelleri
| Desen | Açıklama |
|-----------|------------|
| **Genel bakış satırı** | Bir bakışta temel ölçümler: hata oranı, gecikme, verim |
| **Detaylı inceleme** | Değişkenleri kullanarak özetten ayrıntılı görünüme tıklayın |
| **KIRMIZI yöntem** | Oran, Hatalar, Süre — üç temel hizmet ölçümü |
| **Yöntemi KULLANIN** | Kullanım, Doygunluk, Hatalar — altyapı için |
| **Altın sinyaller** | Gecikme, trafik, hatalar, doygunluk (Google'ın SRE kitabı) |
---

## Uyarı
### Uyarı Kuralı Yapısı
```yaml
groups:
  - name: example
    rules:
      - alert: HighErrorRate
        expr: rate(http_requests_total{status=~"5.."}[5m]) / rate(http_requests_total[5m]) > 0.05
        for: 5m
        labels:
          severity: critical
        annotations:
          summary: "High error rate on {{ $labels.instance }}"
          description: "Error rate is {{ $value | humanizePercentage }}"
```

### Uyarı Yöneticisi Yönlendirmesi
| Konsept | Açıklama |
|-----------|------------|
| **Grup** | Benzer uyarıları tek bir bildirimde birleştirin |
| **Rota** | Uyarıların nereye gideceğini belirleyen eşleştirici ağacı |
| **Alıcı** | Uyarıların nereye gönderileceği (e-posta, Slack, PagerDuty, webhook) |
| **Engelle** | Başka bir uyarı tetiklendiğinde uyarıları bastır |
| **Sessizlik** | Uyarıları etiket eşleştiriciye göre geçici olarak sessize alın |
---

## Sorun Giderme
| Sorun | Çözüm |
|-----------|----------|
| **Hedef aşağı** | Dışa aktarıcının çalışıp çalışmadığını kontrol edin; ağı/güvenlik duvarını kontrol edin; kazıma yapılandırmasını doğrulayın |
| **Veri yok** | Metrik adının yazılışını kontrol edin; etiket filtrelerini kontrol edin; zaman aralığını doğrulayın |
| **Yüksek kardinalite** | Çok fazla etiket kombinasyonu; etiket değerlerini azaltın; kayıt kurallarını kullan |
| **Yavaş sorgular** | Karmaşık sorgular için kayıt kurallarını kullanın; kazıma aralığını artırın |
| **Uyarı yorgunluğu** | Eşikleri ayarlayın;`for`süresini ekleyin; grupla ilgili uyarılar |
| **Yeniden başlatmanın ardından eksik ölçümler** | Prometheus verileri yerel olarak saklar; saklama ayarlarını kontrol edin |
---

## Özet
Prometheus, ihracatçılardan düzenli aralıklarla ölçümler alarak sistemleri izliyor. Metrikler dört türde gelir: sayaçlar (yalnızca yukarıya doğru), göstergeler (yukarı ve aşağı), histogramlar (gruplanmış gözlemler) ve özetler (nicelikler). PromQL sorgulama dilidir — `rate()`, `increase()`,`histogram_quantile()`ve toplama işlevleri (`sum`, `avg`) en yaygın işlemlerdir. Grafana, Prometheus verilerini paneller, değişkenler ve açıklamalarla kontrol panellerinde görselleştirir. Alerting, uyarıları gruplamak, yönlendirmek, susturmak ve engellemek için Alertmanager'ı kullanır. Temel izleme modelleri, hizmetler için Google'ın altın sinyalleri (gecikme, trafik, hatalar, doygunluk) ve KIRMIZI yöntemi (oran, hatalar, süre) ve altyapı için USE yöntemidir (kullanım, doygunluk, hatalar).