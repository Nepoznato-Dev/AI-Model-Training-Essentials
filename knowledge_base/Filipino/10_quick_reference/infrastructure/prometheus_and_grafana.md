<!--
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

-->
# Prometheus at Grafana
Ang Prometheus ay isang open-source monitoring at alerting toolkit na idinisenyo para sa pagiging maaasahan at scalability. Ang Grafana ay ang nangungunang open-source na platform para sa pag-visualize ng data ng time-series. Magkasama, bumubuo sila ng pinakasikat na monitoring stack para sa modernong imprastraktura at mga application. Kinokolekta at iniimbak ng Prometheus ang mga sukatan; Ipinapakita ng Grafana ang mga ito sa mga dashboard.
---

## Arkitektura ng Prometheus
| Bahagi | Paglalarawan |
|-----------|-------------|
| **Prometheus server** | Kinukuha ang mga sukatan mula sa mga target; nag-iimbak ng data ng time-series; sinusuri ang mga alituntunin ng alerto |
| **Exporter** | Inilalantad ang mga sukatan mula sa isang system (Node Exporter, cAdvisor, atbp.) |
| **Pushgateway** | Tumatanggap ng mga sukatan mula sa mga panandaliang trabaho (batch job, CI) |
| **Alertmanager** | Pinangangasiwaan ang mga alerto: pagpapangkat, pagpapatahimik, pagruruta, pagsugpo |
| **Pagtuklas ng serbisyo** | Awtomatikong natutuklasan ang mga target (Kubernetes, Consul, EC2, atbp.) |
---

## Mga Pangunahing Konsepto
| Konsepto | Paglalarawan |
|---------|-------------|
| **Sukatan** | Isang pinangalanang sukat na may mga opsyonal na label at isang halaga |
| **Serye ng oras** | Isang stream ng mga punto ng data para sa isang partikular na sukatan + kumbinasyon ng label |
| **Trabaho** | Isang koleksyon ng mga target na may parehong layunin |
| **Instance** | Isang target na kakamot (karaniwan ay isang proseso) |
| **Scrape** | Ang Prometheus ay kumukuha ng mga sukatan mula sa isang target sa mga regular na pagitan |
| **Label** | Isang pares ng key-value na dimensyon ng isang sukatan (hal.,`method="GET"`) |
| **Sample** | Isang halaga sa isang punto ng oras: (timestamp, value) |
---

## Mga Uri ng Sukatan
| Uri | Paglalarawan | Use Case |
|------|-------------|----------|
| **Kontra** | Monotonically pagtaas ng halaga (tataas lang) | Bilang ng kahilingan; mga pagkakamali; mga gawaing natapos |
| **Sukat** | Halaga na maaaring tumaas o bumaba | Temperatura; paggamit ng memorya; haba ng pila |
| **Histogram** | Mga obserbasyon na naka-bucket ayon sa halaga | Humiling ng latency; laki ng tugon |
| **Buod** | Katulad ng histogram; kinakalkula ang dami ng client-side | Latency percentiles |
---

## PromQL (Query Language)
### Mga Pangunahing Tanong
| Tanong | Paglalarawan |
|-------|-------------|
| `http_requests_total`| Raw time series |
| `http_requests_total{method="GET"}`| I-filter ayon sa label |
| `http_requests_total{method="GET", status="200"}`| Mga filter ng maramihang label |
| `rate(http_requests_total[5m])`| Per-segundo rate sa loob ng 5 minuto |
| `increase(http_requests_total[1h])`| Kabuuang pagtaas sa loob ng 1 oras |
| `sum(rate(http_requests_total[5m])) by (status)`| Pinagsama-samang rate ayon sa katayuan |
| `histogram_quantile(0.95, rate(http_duration_bucket[5m]))`| 95th percentile latency |
| `avg(node_cpu_seconds_total{mode="idle"})`| Average na CPU idle |
| `1 - avg(rate(node_cpu_seconds_total{mode="idle"}[5m]))`| Paggamit ng CPU |
### Mga Karaniwang Pag-andar
| Function | Paglalarawan | Halimbawa |
|----------|-------------|---------|
| `rate()`| Bawat segundong average na rate ng pagtaas | `rate(requests_total[5m])`|
| `irate()`| Per-segundo rate batay sa huling dalawang punto ng data | `irate(requests_total[1m])`|
| `increase()`| Kabuuang pagtaas sa saklaw ng panahon | `increase(errors_total[1h])`|
| `sum()`| Suma kabuuan ng serye | `sum(rate(requests_total[5m])) by (service)`|
| `avg()`| Average sa buong serye | `avg(node_memory_usage)`|
| `histogram_quantile()`| Kalkulahin ang quantile mula sa histogram | `histogram_quantile(0.99, rate(duration_bucket[5m]))`|
| `topk()`| Nangungunang K series ayon sa halaga | `topk(5, rate(requests_total[5m]))`|
| `predict_linear()`| Linear na hula | `predict_linear(disk_usage[1h], 4*3600)`|
| `absent()`| Tingnan kung kulang ang sukatan | `absent(up{job="myapp"})`|
---

## Mga Karaniwang Exporter
| Exporter | Ano ang Sinusubaybayan Nito |
|----------|-----------------|
| **Node Exporter** | Mga sukatan ng host ng Linux/Unix (CPU, memory, disk, network) |
| **cAdvisor** | Mga sukatan ng container (CPU, memory, network, filesystem) |
| **MySQL Exporter** | MySQL database metrics |
| **PostgreSQL Exporter** | Mga sukatan ng database ng PostgreSQL |
| **Redis Exporter** | Mga sukatan ng Redis |
| **Blackbox Exporter** | Suriin ang mga endpoint sa HTTP, HTTPS, DNS, TCP, ICMP |
| **SNMP Exporter** | Mga sukatan ng device sa network sa pamamagitan ng SNMP |
| **JSON Exporter** | Mga custom na sukatan mula sa mga JSON API |
---

## Grafana
### Mga Pangunahing Konsepto
| Konsepto | Paglalarawan |
|---------|-------------|
| **Pinagmulan ng data** | Koneksyon sa Prometheus (o iba pang mga backend) |
| **Dashboard** | Koleksyon ng mga panel na nakaayos sa isang layout |
| **Panel** | Iisang visualization (graph, gauge, table, heatmap) |
| **Variable** | Dynamic na filter para sa mga dashboard (hal., piliin ang instance) |
| **Annotation** | Markahan ang mga kaganapan sa mga graph (deployment, insidente) |
| **Panuntunan ng alerto** | Pag-alerto na nakabatay sa threshold sa loob ng Grafana |
| **Pag-templat** | Muling magagamit na mga pattern ng dashboard na may mga variable |
### Mga Kapaki-pakinabang na Pattern ng Dashboard
| Pattern | Paglalarawan |
|---------|-------------|
| **Hilera ng Pangkalahatang-ideya** | Mga pangunahing sukatan sa isang sulyap: rate ng error, latency, throughput |
| **Drill-down** | Mag-click mula sa buod hanggang sa detalyadong view gamit ang mga variable |
| **PULA na paraan** | Rate, Error, Tagal — ang tatlong pangunahing sukatan ng serbisyo |
| **GAMIT paraan** | Paggamit, Saturation, Mga Error — para sa imprastraktura |
| **Mga gintong senyales** | Latency, trapiko, mga error, saturation (SRE book ng Google) |
---

## Nag-aalerto
### Istraktura ng Panuntunan ng Alerto
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

### Pagruruta ng Alertmanager
| Konsepto | Paglalarawan |
|---------|-------------|
| **Pangkat** | Pagsamahin ang mga katulad na alerto sa isang notification |
| **Ruta** | Tree of matchers na tumutukoy kung saan napupunta ang mga alerto |
| **Receiver** | Saan magpapadala ng mga alerto (email, Slack, PagerDuty, webhook) |
| **Pagbawalan** | Pigilan ang mga alerto kapag ang isa pang alerto ay nagpapaputok |
| **Katahimikan** | Pansamantalang i-mute ang mga alerto sa pamamagitan ng label matcher |
---

## Pag-troubleshoot
| Problema | Solusyon |
|---------|----------|
| **Target pababa** | Suriin kung tumatakbo ang exporter; suriin ang network/firewall; i-verify ang scrape config |
| **Walang data** | Suriin ang pagbabaybay ng pangalan ng sukatan; suriin ang mga filter ng label; i-verify ang saklaw ng oras |
| **Mataas na cardinality** | Masyadong maraming kumbinasyon ng label; bawasan ang mga halaga ng label; gumamit ng mga panuntunan sa pagre-record |
| **Mabagal na mga query** | Gumamit ng mga panuntunan sa pagre-record para sa mga kumplikadong query; taasan ang pagitan ng scrape |
| **Pag-alerto sa pagkapagod** | Tune threshold; magdagdag ng tagal ng `for`; mga alertong nauugnay sa pangkat |
| **Nawawalang sukatan pagkatapos mag-restart** | Ang Prometheus ay nag-iimbak ng data nang lokal; tingnan ang mga setting ng pagpapanatili |
---

## Buod
Sinusubaybayan ng Prometheus ang mga system sa pamamagitan ng pag-scrap ng mga sukatan mula sa mga exporter sa mga regular na pagitan. May apat na uri ang mga sukatan: mga counter (papataas lang), mga gauge (pataas at pababa), histograms (mga bucket na obserbasyon), at mga buod (quantile). Ang PromQL ay ang query language —`rate()`,`increase()`,`histogram_quantile()`, at aggregation functions (`sum`,`avg`) ay ang pinakakaraniwang mga operasyon. Nakikita ng Grafana ang data ng Prometheus sa mga dashboard na may mga panel, variable, at anotasyon. Gumagamit ang Alerto ng Alertmanager para sa pagpapangkat, pagruruta, pagpapatahimik, at pagpigil sa mga alerto. Ang mga pangunahing pattern ng pagsubaybay ay ang mga ginintuang signal ng Google (latency, traffic, error, saturation) at ang RED method (rate, error, duration) para sa mga serbisyo at USE method (utilization, saturation, errors) para sa imprastraktura.