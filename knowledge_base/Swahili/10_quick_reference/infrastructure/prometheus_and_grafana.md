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
# Prometheus na Grafana
Prometheus ni zana huria ya ufuatiliaji na arifa iliyoundwa kwa ajili ya kutegemewa na kubadilika. Grafana ndio jukwaa linaloongoza la chanzo-wazi la kuibua data ya mfululizo wa saa. Kwa pamoja, huunda safu maarufu ya ufuatiliaji kwa miundombinu ya kisasa na programu. Prometheus hukusanya na kuhifadhi metrics; Grafana anazionyesha kwenye dashibodi.
---

## Usanifu wa Prometheus
| Sehemu | Maelezo |
|-----------|-------------|
| **Seva ya Prometheus** | Hufuta vipimo kutoka kwa malengo; huhifadhi data ya mfululizo wa wakati; hutathmini sheria za tahadhari |
| **Msafirishaji** | Inaonyesha vipimo kutoka kwa mfumo (Node Exporter, cAdvisor, n.k.) |
| **Pushgateway** | Hupokea vipimo kutoka kwa kazi za muda mfupi (batch jobs, CI) |
| **Msimamizi wa Tahadhari** | Hushughulikia arifa: kupanga vikundi, kunyamazisha, kuelekeza, kuzuia |
| **Ugunduzi wa huduma** | Hugundua malengo kiotomatiki (Kubernetes, Consul, EC2, n.k.) |
---

## Dhana Muhimu
| Dhana | Maelezo |
|---------|-------------|
| **Kipimo** | Kipimo kilichopewa jina chenye lebo za hiari na thamani |
| **Msururu wa saa** | Mtiririko wa pointi za data za mchanganyiko mahususi wa metriki + lebo |
| **Kazi** | Mkusanyiko wa malengo yenye madhumuni sawa |
| **Mfano** | Lengo moja la kukwangua (kawaida ni mchakato) |
| **Kufuta** | Prometheus akivuta vipimo kutoka kwa lengo mara kwa mara |
| **Lebo** | Jozi ya thamani-msingi inayopima kipimo (k.m.,`method="GET"`) |
| **Sampuli** | Thamani kwa wakati mmoja: (muhuri wa muda, thamani) |
---

## Aina za kipimo
| Aina | Maelezo | Tumia Kesi |
|------|-------------|-----------|
| **Kaunta** | Thamani inayoongezeka kwa kiasi kikubwa (hupanda tu) | Idadi ya ombi; makosa; kazi zimekamilika |
| **Kipimo** | Thamani inayoweza kupanda au kushuka | Joto; matumizi ya kumbukumbu; urefu wa foleni |
| **Histogram** | Uchunguzi uliowekwa kwa thamani | Omba muda wa kusubiri; saizi ya majibu |
| **Muhtasari** | Sawa na histogram; hukokotoa quantiles upande wa mteja | Asilimia za kusubiri |
---

## PromQL (Lugha ya Maswali)
### Maswali ya Msingi
| Swali | Maelezo |
|-------|-------------|
| `http_requests_total`| Saa ghafi mfululizo |
| `http_requests_total{method="GET"}`| Chuja kwa lebo |
| `http_requests_total{method="GET", status="200"}`| Vichungi vya lebo nyingi |
| `rate(http_requests_total[5m])`| Kiwango cha kila sekunde kwa zaidi ya dakika 5 |
| `increase(http_requests_total[1h])`| Jumla ya ongezeko zaidi ya saa 1 |
| `sum(rate(http_requests_total[5m])) by (status)`| Ongeza kiwango kwa hali |
| `histogram_quantile(0.95, rate(http_duration_bucket[5m]))`| Muda wa kusubiri wa asilimia 95 |
| `avg(node_cpu_seconds_total{mode="idle"})`| Wastani wa CPU bila kufanya kitu |
| `1 - avg(rate(node_cpu_seconds_total{mode="idle"}[5m]))`| Matumizi ya CPU |
### Kazi za Kawaida
| Kazi | Maelezo | Mfano |
|----------|-----------------------|
| `rate()`| Kiwango cha wastani cha ongezeko la kila sekunde | `rate(requests_total[5m])`|
| `irate()`| Kiwango cha kila sekunde kulingana na pointi mbili za mwisho za data | `irate(requests_total[1m])`|
| `increase()`| Jumla ya ongezeko la muda | `increase(errors_total[1h])`|
| `sum()`| Jumla katika mfululizo | `sum(rate(requests_total[5m])) by (service)`|
| `avg()`| Wastani katika mfululizo | `avg(node_memory_usage)`|
| `histogram_quantile()`| Kukokotoa quantile kutoka histogram | `histogram_quantile(0.99, rate(duration_bucket[5m]))`|
| `topk()`| Mfululizo wa Juu wa K kwa thamani | `topk(5, rate(requests_total[5m]))`|
| `predict_linear()`| Utabiri wa mstari | `predict_linear(disk_usage[1h], 4*3600)`|
| `absent()`| Angalia ikiwa metriki haipo | `absent(up{job="myapp"})`|
---

## Wasafirishaji wa Kawaida
| Msafirishaji | Kinachofuatilia |
|----------|-----------------|
| **Msafirishaji wa nodi** | Vipimo vya mwenyeji wa Linux/Unix (CPU, kumbukumbu, diski, mtandao) |
| **cAdvisor** | Vipimo vya kontena (CPU, kumbukumbu, mtandao, mfumo wa faili) |
| **Msafirishaji wa MySQL** | Vipimo vya hifadhidata vya MySQL |
| **Msafirishaji wa PostgreSQL** | Vipimo vya hifadhidata vya PostgreSQL |
| **Redis Msafirishaji** | Redis metrics |
| **Blackbox Exporter** | Chunguza sehemu za mwisho juu ya HTTP, HTTPS, DNS, TCP, ICMP |
| **Msafirishaji wa SNMP** | Vipimo vya kifaa cha mtandao kupitia SNMP |
| **JSON Msafirishaji** | Vipimo maalum kutoka kwa API za JSON |
---

## Grafana
### Dhana Muhimu
| Dhana | Maelezo |
|---------|-------------|
| **Chanzo cha data** | Muunganisho wa Prometheus (au sehemu zingine za nyuma) |
| **Dashibodi** | Mkusanyiko wa paneli zilizopangwa kwa mpangilio |
| **Jopo** | Taswira moja (grafu, geji, jedwali, ramani ya joto) |
| **Kigezo** | Kichujio chenye nguvu cha dashibodi (k.m., chagua mfano) |
| **Ufafanuzi** | Weka alama kwenye grafu (utumaji, matukio) |
| **Kanuni ya tahadhari** | Arifa kulingana na kizingiti ndani ya Grafana |
| **Kiolezo** | Miundo ya dashibodi inayoweza kutumika tena yenye vigeu |
### Miundo Muhimu ya Dashibodi
| Muundo | Maelezo |
|---------|-------------|
| **Safu mlalo ya muhtasari** | Vipimo muhimu kwa muhtasari: kiwango cha makosa, muda wa kusubiri, matokeo |
| **chimbua-chini** | Bofya kutoka kwa muhtasari hadi mtazamo wa kina kwa kutumia vigeu |
| **Njia NYEKUNDU** | Kadiria, Hitilafu, Muda — vipimo vitatu muhimu vya huduma |
| **TUMIA mbinu** | Matumizi, Kueneza, Makosa — kwa miundombinu |
| **Ishara za dhahabu** | Muda wa kusubiri, trafiki, makosa, kueneza (kitabu cha Google SRE) |
---

##Kutahadharisha
### Muundo wa Kanuni ya Tahadhari
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

### Uelekezaji wa Kidhibiti Alert
| Dhana | Maelezo |
|---------|-------------|
| **Kikundi** | Changanya arifa sawa katika arifa moja |
| **Njia** | Mti wa vilinganishi ambao huamua arifa ziende wapi |
| **Mpokeaji** | Mahali pa kutuma arifa (barua pepe, Slack, PagerDuty, webhook) |
| **Zuia** | Zuia arifa wakati tahadhari nyingine inaporushwa |
| **Kimya** | Zima arifa kwa muda kwa kilinganishi cha lebo |
---

## Utatuzi wa matatizo
| Tatizo | Suluhisho |
|---------|----------|
| **Lenga chini** | Angalia ikiwa muuzaji nje anaendesha; angalia mtandao / firewall; thibitisha usanidi wa scrape |
| **Hakuna data** | Angalia tahajia ya jina la kipimo; angalia vichungi vya lebo; thibitisha kipindi |
| **Ukadinali wa hali ya juu** | Mchanganyiko wa lebo nyingi sana; kupunguza maadili ya lebo; tumia sheria za kurekodi |
| **Maswali ya polepole** | Tumia sheria za kurekodi kwa maswali magumu; kuongeza muda wa scrape |
| **Tahadhari uchovu** | Tune vizingiti; ongeza muda wa `for`; arifa zinazohusiana na kikundi |
| **Vipimo vinavyokosekana baada ya kuwasha upya** | Prometheus huhifadhi data ndani ya nchi; angalia mipangilio ya kubaki |
---

## Muhtasari
Prometheus hufuatilia mifumo kwa kufuta metrics kutoka kwa wauzaji bidhaa nje mara kwa mara. Vipimo vinakuja katika aina nne: vihesabio (kwenda juu tu), geji (juu na chini), histogram (uchunguzi uliowekwa kwenye ndoo), na muhtasari (quantiles). PromQL ndiyo lugha ya kuuliza maswali —`rate()`,`increase()`,`histogram_quantile()`, na vitendaji vya kujumlisha (`sum`,`avg`) ndizo shughuli zinazotumika zaidi. Grafana anaonyesha data ya Prometheus katika dashibodi zilizo na paneli, vigeuzo na vidokezo. Kutahadharisha hutumia Alertmanager kwa kupanga, kuelekeza, kunyamazisha na kuzuia arifa. Mifumo muhimu ya ufuatiliaji ni mawimbi ya dhahabu ya Google (muda wa kusubiri, trafiki, hitilafu, uenezaji) na mbinu ya RED (kiwango, makosa, muda) kwa huduma na mbinu ya MATUMIZI (matumizi, uenezi, hitilafu) kwa miundombinu.