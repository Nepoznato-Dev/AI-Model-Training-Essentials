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
  - name: "AI Model Training Team"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.1"
    date: "2026-08-09"
    author: "AI Model Training Team"
    changes: "Moved to infrastructure/ subfolder; added subcategory field"
  - version: "1.0.0"
    date: "2026-08-05"
    author: "AI Model Training Team"
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

# Prometeo e Grafana
Prometheus è un toolkit di monitoraggio e avviso open source progettato per affidabilità e scalabilità. Grafana è la principale piattaforma open source per la visualizzazione di dati di serie temporali. Insieme, costituiscono lo stack di monitoraggio più popolare per infrastrutture e applicazioni moderne. Prometheus raccoglie e archivia le metriche; Grafana li visualizza nelle dashboard.
---

## Architettura di Prometeo
| Componente | Descrizione |
|-----------|-------------|
| **Server Prometeo** | Elimina le metriche dagli obiettivi; memorizza i dati delle serie temporali; valuta le regole di avviso |
| **Esportatore** | Espone le metriche da un sistema (Node Exporter, cAdvisor, ecc.) |
| **Pushgateway** | Riceve metriche da lavori di breve durata (lavori batch, CI) |
| **Gestione avvisi** | Gestisce gli avvisi: raggruppamento, silenziamento, instradamento, inibizione |
| **Scoperta di servizi** | Rileva automaticamente i target (Kubernetes, Consul, EC2, ecc.) |
---

## Concetti chiave
| Concetto | Descrizione |
|---------|-----|
| **Metrico** | Una misurazione denominata con etichette facoltative e un valore |
| **Serie storica** | Un flusso di punti dati per una combinazione metrica + etichetta specifica |
| **Lavoro** | Una raccolta di obiettivi con lo stesso scopo |
| **Istanza** | Un unico obiettivo da raschiare (di solito un processo) |
| **Raschiare** | Prometeo estrae parametri da un obiettivo a intervalli regolari |
| **Etichetta** | Una coppia chiave-valore che dimensiona una metrica (ad esempio,`method="GET"`) |
| **Esempio** | Un valore in un determinato momento: (timestamp, valore) |
---

## Tipi di metriche
| Digitare | Descrizione | Caso d'uso |
|------|-------------|----------|
| **Contatore** | Valore monotonicamente crescente (sale solo) | Conteggio richieste; errori; compiti completati |
| **Manometro** | Valore che può salire o scendere | Temperatura; utilizzo della memoria; lunghezza della coda |
| **Istogramma** | Osservazioni raggruppate per valore | Richiedi latenza; dimensione della risposta |
| **Riepilogo** | Simile all'istogramma; calcola i quantili lato client | percentili di latenza |
---

## PromQL (linguaggio di query)
### Query di base
| Domanda | Descrizione |
|-------|-------------|
| `http_requests_total`| Serie temporali grezze |
| `http_requests_total{method="GET"}`| Filtra per etichetta |
| `http_requests_total{method="GET", status="200"}`| Filtri per etichette multiple |
| `rate(http_requests_total[5m])`| Tariffa al secondo su 5 minuti |
| `increase(http_requests_total[1h])`| Incremento totale in 1 ora |
| `sum(rate(http_requests_total[5m])) by (status)`| Tasso aggregato per stato |
| `histogram_quantile(0.95, rate(http_duration_bucket[5m]))`| Latenza del 95° percentile |
| `avg(node_cpu_seconds_total{mode="idle"})`| CPU inattiva media |
| `1 - avg(rate(node_cpu_seconds_total{mode="idle"}[5m]))`| Utilizzo della CPU |
### Funzioni comuni
| Funzione | Descrizione | Esempio |
|----------|-------------|---------|
| `rate()`| Tasso di incremento medio al secondo | `rate(requests_total[5m])`|
| `irate()`| Tariffa al secondo basata sugli ultimi due punti dati | `irate(requests_total[1m])`|
| `increase()`| Incremento totale nell'arco temporale | `increase(errors_total[1h])`|
| `sum()`| Somma delle serie | `sum(rate(requests_total[5m])) by (service)`|
| `avg()`| Media delle serie | `avg(node_memory_usage)`|
| `histogram_quantile()`| Calcola il quantile dall'istogramma | `histogram_quantile(0.99, rate(duration_bucket[5m]))`|
| `topk()`| Principali serie K per valore | `topk(5, rate(requests_total[5m]))`|
| `predict_linear()`| Previsione lineare | `predict_linear(disk_usage[1h], 4*3600)`|
| `absent()`| Controlla se manca la metrica | `absent(up{job="myapp"})`|
---

## Esportatori comuni
| Esportatore | Cosa monitora |
|----------|-----------|
| **Esportatore nodo** | Metriche host Linux/Unix (CPU, memoria, disco, rete) |
| **cConsulente** | Metriche del contenitore (CPU, memoria, rete, file system) |
| **Esportatore MySQL** | Metriche del database MySQL |
| **Esportatore PostgreSQL** | Metriche del database PostgreSQL |
| **Esportatore Redis** | Metriche Redis |
| **Esportatore Blackbox** | Sonda gli endpoint su HTTP, HTTPS, DNS, TCP, ICMP |
| **Esportatore SNMP** | Metriche del dispositivo di rete tramite SNMP |
| **Esportatore JSON** | Metriche personalizzate dalle API JSON |
---

##Grafana
### Concetti chiave
| Concetto | Descrizione |
|---------|-----|
| **Fonte dati** | Connessione a Prometheus (o altri backend) |
| **Cruscotto** | Collezione di pannelli disposti secondo un layout |
| **Pannello** | Visualizzazione singola (grafico, indicatore, tabella, mappa termica) |
| **Variabile** | Filtro dinamico per dashboard (ad esempio, seleziona istanza) |
| **Annotazione** | Contrassegnare gli eventi sui grafici (distribuzioni, incidenti) |
| **Regola di avviso** | Avvisi basati su soglia all'interno di Grafana |
| **Modelli** | Modelli di dashboard riutilizzabili con variabili |
### Utili modelli di dashboard
| Modello | Descrizione |
|---------|-----|
| **Riga panoramica** | Panoramica dei parametri chiave: tasso di errore, latenza, throughput |
| **Drilldown** | Fare clic dal riepilogo alla visualizzazione dettagliata utilizzando le variabili |
| **Metodo ROSSO** | Tasso, errori, durata: i tre parametri chiave del servizio |
| **Metodo UTILIZZA** | Utilizzo, saturazione, errori — per le infrastrutture |
| **Segnali d'oro** | Latenza, traffico, errori, saturazione (libro SRE di Google) |
---

## Avviso
### Struttura delle regole di avviso
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

### Routing di Alertmanager
| Concetto | Descrizione |
|---------|-----|
| **Gruppo** | Combina avvisi simili in un'unica notifica |
| **Percorso** | Albero di corrispondenze che determina dove vanno gli avvisi |
| **Ricevitore** | Dove inviare avvisi (e-mail, Slack, PagerDuty, webhook) |
| **Inibisci** | Elimina gli avvisi quando viene attivato un altro avviso |
| **Silenzio** | Disattiva temporaneamente gli avvisi tramite il label matcher |
---

## Risoluzione dei problemi
| Problema | Soluzione |
|---------|----------|
| **Obiettivo giù** | Controlla se l'esportatore è in esecuzione; controllare la rete/firewall; verifica la configurazione dello scraping |
| **Nessun dato** | Controllare l'ortografia del nome della metrica; controllare i filtri delle etichette; verificare intervallo temporale |
| **Alta cardinalità** | Troppe combinazioni di etichette; ridurre i valori dell'etichetta; utilizzare le regole di registrazione |
| **Query lente** | Utilizzare le regole di registrazione per query complesse; aumentare l'intervallo di raschiamento |
| **Allerta stanchezza** | Soglie di regolazione; aggiungi durata `for`; avvisi relativi al gruppo |
| **Metriche mancanti dopo il riavvio** | Prometheus memorizza i dati localmente; controlla le impostazioni di conservazione |
---

## Riepilogo
Prometheus monitora i sistemi raccogliendo parametri dagli esportatori a intervalli regolari. Le metriche sono di quattro tipi: contatori (che vanno solo verso l'alto), indicatori (su e giù), istogrammi (osservazioni a intervalli) e riepiloghi (quantili). PromQL è il linguaggio di query:`rate()`,`increase()`,`histogram_quantile()`e le funzioni di aggregazione (`sum`,`avg`) sono le operazioni più comuni. Grafana visualizza i dati Prometheus in dashboard con pannelli, variabili e annotazioni. Alerting utilizza Alertmanager per raggruppare, instradare, silenziare e inibire gli avvisi. I principali modelli di monitoraggio sono i segnali d'oro di Google (latenza, traffico, errori, saturazione) e il metodo RED (tasso, errori, durata) per i servizi e il metodo USE (utilizzo, saturazione, errori) per l'infrastruttura.