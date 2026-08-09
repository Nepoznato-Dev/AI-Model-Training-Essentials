---
# Metadata
title: "Prometheus and Grafana"
description: "PromQL, exporters, dashboards, alerting, monitoring stack"
category: "Quick Reference"
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

# Prometheus und Grafana
Prometheus ist ein Open-Source-Überwachungs- und Alarmierungs-Toolkit, das auf Zuverlässigkeit und Skalierbarkeit ausgelegt ist. Grafana ist die führende Open-Source-Plattform zur Visualisierung von Zeitreihendaten. Zusammen bilden sie den beliebtesten Überwachungsstapel für moderne Infrastruktur und Anwendungen. Prometheus sammelt und speichert Metriken; Grafana zeigt sie in Dashboards an.
---

## Prometheus-Architektur
| Komponente | Beschreibung |
|-----------|-------------|
| **Prometheus-Server** | Entfernt Metriken von Zielen; speichert Zeitreihendaten; wertet Alarmregeln aus |
| **Exporteur** | Macht Metriken von einem System verfügbar (Node Exporter, cAdvisor usw.) |
| **Pushgateway** | Empfängt Metriken von kurzlebigen Jobs (Batch-Jobs, CI) |
| **Alertmanager** | Behandelt Warnungen: Gruppierung, Stummschaltung, Weiterleitung, Sperrung |
| **Diensterkennung** | Erkennt automatisch Ziele (Kubernetes, Consul, EC2 usw.) |
---

## Schlüsselkonzepte
| Konzept | Beschreibung |
|---------|-------------|
| **Metrisch** | Eine benannte Messung mit optionalen Beschriftungen und einem Wert |
| **Zeitreihe** | Ein Stream von Datenpunkten für eine bestimmte Kombination aus Metrik und Beschriftung |
| **Job** | Eine Sammlung von Zielen mit demselben Zweck |
| **Instanz** | Ein einzelnes Ziel zum Scrapen (normalerweise ein Prozess) |
| **Kratzen** | Prometheus ruft in regelmäßigen Abständen Metriken von einem Ziel ab |
| **Beschriftung** | Ein Schlüssel-Wert-Paar, das eine Metrik dimensioniert (z. B.`method="GET"`) |
| **Beispiel** | Ein Wert zu einem bestimmten Zeitpunkt: (Zeitstempel, Wert) |
---

## Metriktypen
| Geben Sie | ein Beschreibung | Anwendungsfall |
|------|-------------|----------|
| **Zähler** | Monoton steigender Wert (steigt nur) | Anzahl der Anfragen; Fehler; erledigte Aufgaben |
| **Messgerät** | Wert, der steigen oder fallen kann | Temperatur; Speichernutzung; Warteschlangenlänge |
| **Histogramm** | Nach Wert gegliederte Beobachtungen | Anforderungslatenz; Antwortgröße |
| **Zusammenfassung** | Ähnlich dem Histogramm; berechnet Quantile clientseitig | Latenzperzentile |
---

## PromQL (Abfragesprache)
### Grundlegende Abfragen
| Abfrage | Beschreibung |
|-------|-------------|
| `http_requests_total`| Rohzeitreihen |
| `http_requests_total{method="GET"}`| Nach Label filtern |
| `http_requests_total{method="GET", status="200"}`| Mehrere Etikettenfilter |
| `rate(http_requests_total[5m])`| Sekundenrate über 5 Minuten |
| `increase(http_requests_total[1h])`| Gesamtanstieg über 1 Stunde |
| `sum(rate(http_requests_total[5m])) by (status)`| Aggregierte Rate nach Status |
| `histogram_quantile(0.95, rate(http_duration_bucket[5m]))`| 95. Perzentillatenz |
| `avg(node_cpu_seconds_total{mode="idle"})`| Durchschnittlicher CPU-Leerlauf |
| `1 - avg(rate(node_cpu_seconds_total{mode="idle"}[5m]))`| CPU-Auslastung |
### Gemeinsame Funktionen
| Funktion | Beschreibung | Beispiel |
|----------|-------------|---------|
| `rate()`| Durchschnittliche Steigerungsrate pro Sekunde | `rate(requests_total[5m])`|
| `irate()`| Rate pro Sekunde basierend auf den letzten beiden Datenpunkten | `irate(requests_total[1m])`|
| `increase()`| Gesamtanstieg im Zeitbereich | `increase(errors_total[1h])`|
| `sum()`| Summe über Reihen | `sum(rate(requests_total[5m])) by (service)`|
| `avg()`| Durchschnitt aller Serien | `avg(node_memory_usage)`|
| `histogram_quantile()`| Berechnen Sie das Quantil aus dem Histogramm | `histogram_quantile(0.99, rate(duration_bucket[5m]))`|
| `topk()`| Top-K-Serie nach Wert | `topk(5, rate(requests_total[5m]))`|
| `predict_linear()`| Lineare Vorhersage | `predict_linear(disk_usage[1h], 4*3600)`|
| `absent()`| Überprüfen Sie, ob die Metrik fehlt | `absent(up{job="myapp"})`|
---

## Gemeinsame Exporteure
| Exporteur | Was es überwacht |
|----------|---|
| **Knotenexporteur** | Linux/Unix-Hostmetriken (CPU, Speicher, Festplatte, Netzwerk) |
| **cAdvisor** | Containermetriken (CPU, Speicher, Netzwerk, Dateisystem) |
| **MySQL-Exporteur** | MySQL-Datenbankmetriken |
| **PostgreSQL-Exporter** | PostgreSQL-Datenbankmetriken |
| **Redis-Exporteur** | Redis-Metriken |
| **Blackbox-Exporteur** | Endpunkte über HTTP, HTTPS, DNS, TCP, ICMP prüfen |
| **SNMP-Exporteur** | Netzwerkgerätemetriken über SNMP |
| **JSON-Exporteur** | Benutzerdefinierte Metriken von JSON-APIs |
---

## Grafana
### Schlüsselkonzepte
| Konzept | Beschreibung |
|---------|-------------|
| **Datenquelle** | Verbindung zu Prometheus (oder anderen Backends) |
| **Dashboard** | Sammlung von in einem Layout angeordneten Tafeln |
| **Panel** | Einzelvisualisierung (Grafik, Messgerät, Tabelle, Heatmap) |
| **Variable** | Dynamischer Filter für Dashboards (z. B. Instanz auswählen) |
| **Anmerkung** | Markieren Sie Ereignisse in Diagrammen (Bereitstellungen, Vorfälle) |
| **Alarmregel** | Schwellenwertbasierte Alarmierung in Grafana |
| **Vorlagen** | Wiederverwendbare Dashboard-Muster mit Variablen |
### Nützliche Dashboard-Muster
| Muster | Beschreibung |
|---------|-------------|
| **Übersichtszeile** | Wichtige Kennzahlen auf einen Blick: Fehlerrate, Latenz, Durchsatz |
| **Drilldown** | Klicken Sie von der Zusammenfassung zur Detailansicht mit Variablen |
| **RED-Methode** | Rate, Fehler, Dauer – die drei wichtigsten Servicekennzahlen |
| **USE-Methode** | Auslastung, Sättigung, Fehler – für die Infrastruktur |
| **Goldene Signale** | Latenz, Datenverkehr, Fehler, Sättigung (Googles SRE-Buch) |
---

## Alarmierung
### Alarmregelstruktur
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

### Alertmanager-Routing
| Konzept | Beschreibung |
|---------|-------------|
| **Gruppe** | Ähnliche Benachrichtigungen in einer Benachrichtigung zusammenfassen |
| **Route** | Baum der Matcher, der bestimmt, wohin die Warnungen gehen |
| **Empfänger** | Wohin Benachrichtigungen gesendet werden sollen (E-Mail, Slack, PagerDuty, Webhook) |
| **Hemmen** | Warnungen unterdrücken, wenn eine andere Warnung ausgelöst wird |
| **Stille** | Warnungen durch Label-Matcher vorübergehend stumm schalten |
---

## Fehlerbehebung
| Problem | Lösung |
|---------|----------|
| **Ziel nach unten** | Überprüfen Sie, ob der Exporter ausgeführt wird. Netzwerk/Firewall prüfen; Scrape-Konfiguration überprüfen |
| **Keine Daten** | Überprüfen Sie die Schreibweise des Metriknamens. Etikettenfilter überprüfen; Zeitbereich überprüfen |
| **Hohe Kardinalität** | Zu viele Etikettenkombinationen; Etikettenwerte reduzieren; Aufzeichnungsregeln verwenden |
| **Langsame Abfragen** | Verwenden Sie Aufzeichnungsregeln für komplexe Abfragen. Scraping-Intervall erhöhen |
| **Alarmmüdigkeit** | Schwellenwerte einstellen;`for`Dauer hinzufügen; gruppenbezogene Warnungen |
| **Fehlende Messwerte nach dem Neustart** | Prometheus speichert Daten lokal; Aufbewahrungseinstellungen prüfen |
---

## Zusammenfassung
Prometheus überwacht Systeme, indem es in regelmäßigen Abständen Metriken von Exporteuren abruft. Es gibt vier Arten von Metriken: Zähler (nur nach oben), Messgeräte (nach oben und unten), Histogramme (Bucket-Beobachtungen) und Zusammenfassungen (Quantile). PromQL ist die Abfragesprache – `rate()`, `increase()`,`histogram_quantile()`und Aggregationsfunktionen (`sum`, `avg`) sind die häufigsten Operationen. Grafana visualisiert Prometheus-Daten in Dashboards mit Panels, Variablen und Anmerkungen. Alerting verwendet Alertmanager zum Gruppieren, Weiterleiten, Stummschalten und Unterdrücken von Warnungen. Die wichtigsten Überwachungsmuster sind die goldenen Signale von Google (Latenz, Datenverkehr, Fehler, Sättigung) und die RED-Methode (Rate, Fehler, Dauer) für Dienste und die USE-Methode (Auslastung, Sättigung, Fehler) für die Infrastruktur.