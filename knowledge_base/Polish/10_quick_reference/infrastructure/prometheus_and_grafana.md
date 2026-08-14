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
# Prometeusz i Grafana
Prometheus to zestaw narzędzi do monitorowania i ostrzegania typu open source, zaprojektowany z myślą o niezawodności i skalowalności. Grafana to wiodąca platforma typu open source do wizualizacji danych szeregów czasowych. Razem tworzą najpopularniejszy stos monitorujący dla nowoczesnej infrastruktury i aplikacji. Prometheus zbiera i przechowuje metryki; Grafana wyświetla je w dashboardach.
---

## Architektura Prometeusza
| Składnik | Opis |
|---------------|------------|
| **Serwer Prometheus** | Pobiera metryki z celów; przechowuje dane szeregów czasowych; ocenia reguły alertów |
| **Eksporter** | Wyświetla metryki z systemu (Node Exporter, cAdvisor itp.) |
| **Brama push** | Otrzymuje metryki z zadań krótkotrwałych (zadania wsadowe, CI) |
| **Menedżer alertów** | Obsługuje alerty: grupowanie, wyciszanie, routing, hamowanie |
| **Wykrywanie usług** | Automatycznie wykrywa cele (Kubernetes, Consul, EC2 itp.) |
---

## Kluczowe pojęcia
| Koncepcja | Opis |
|--------|------------|
| **Metryczne** | Nazwany pomiar z opcjonalnymi etykietami i wartością |
| **Szereg czasowy** | Strumień punktów danych dla określonej kombinacji metryki i etykiety |
| **Praca** | Zbiór celów o tym samym celu |
| **Instancja** | Pojedynczy cel do zeskrobania (zwykle proces) |
| **Zdrap** | Prometeusz pobiera metryki od celu w regularnych odstępach czasu |
| **Etykieta** | Para klucz-wartość wymiarująca metrykę (np.`method="GET"`) |
| **Próbka** | Wartość w danym momencie: (znacznik czasu, wartość) |
---

## Typy metryczne
| Wpisz | Opis | Przypadek użycia |
|------|------------|--------------|
| **Licznik** | Monotonicznie rosnąca wartość (tylko rośnie) | Liczba żądań; błędy; zadania wykonane |
| **Wskaźnik** | Wartość, która może rosnąć lub spadać | Temperatura; wykorzystanie pamięci; długość kolejki |
| **Histogram** | Obserwacje pogrupowane według wartości | Opóźnienie żądania; rozmiar odpowiedzi |
| **Podsumowanie** | Podobny do histogramu; oblicza kwantyle po stronie klienta | Percentyle opóźnienia |
---

## PromQL (język zapytań)
### Podstawowe zapytania
| Zapytanie | Opis |
|-------|------------|
| `http_requests_total`| Surowe serie czasowe |
| `http_requests_total{method="GET"}`| Filtruj według etykiety |
| `http_requests_total{method="GET", status="200"}`| Wiele filtrów etykiet |
| `rate(http_requests_total[5m])`| Stawka na sekundę przez 5 minut |
| `increase(http_requests_total[1h])`| Całkowity wzrost w ciągu 1 godziny |
| `sum(rate(http_requests_total[5m])) by (status)`| Łączna stawka według statusu |
| `histogram_quantile(0.95, rate(http_duration_bucket[5m]))`| Opóźnienie 95. percentyla |
| `avg(node_cpu_seconds_total{mode="idle"})`| Średnia bezczynność procesora |
| `1 - avg(rate(node_cpu_seconds_total{mode="idle"}[5m]))`| Wykorzystanie procesora |
### Wspólne funkcje
| Funkcja | Opis | Przykład |
|--------------|------------|--------|
| `rate()`| Średnie tempo wzrostu na sekundę | `rate(requests_total[5m])`|
| `irate()`| Szybkość na sekundę na podstawie dwóch ostatnich punktów danych | `irate(requests_total[1m])`|
| `increase()`| Całkowity wzrost w przedziale czasowym | `increase(errors_total[1h])`|
| `sum()`| Suma w szeregach | `sum(rate(requests_total[5m])) by (service)`|
| `avg()`| Średnia w całej serii | `avg(node_memory_usage)`|
| `histogram_quantile()`| Oblicz kwantyl z histogramu | `histogram_quantile(0.99, rate(duration_bucket[5m]))`|
| `topk()`| Najlepsza seria K według wartości | `topk(5, rate(requests_total[5m]))`|
| `predict_linear()`| Przewidywanie liniowe | `predict_linear(disk_usage[1h], 4*3600)`|
| `absent()`| Sprawdź, czy brakuje metryki | `absent(up{job="myapp"})`|
---

## Zwykli eksporterzy
| Eksporter | Co monitoruje |
|---------|--------------------------------|
| **Eksporter węzłów** | Metryki hosta Linux/Unix (procesor, pamięć, dysk, sieć) |
| **cDoradca** | Metryki kontenerów (procesor, pamięć, sieć, system plików) |
| **Eksporter MySQL** | Metryki bazy danych MySQL |
| **Eksporter PostgreSQL** | Metryki bazy danych PostgreSQL |
| **Eksporter Redis** | Metryki Redis |
| **Eksporter Blackbox** | Sonduj punkty końcowe przez HTTP, HTTPS, DNS, TCP, ICMP |
| **Eksporter SNMP** | Metryki urządzeń sieciowych poprzez SNMP |
| **Eksporter JSON** | Niestandardowe metryki z interfejsów API JSON |
---

## Grafana
### Kluczowe pojęcia
| Koncepcja | Opis |
|--------|------------|
| **Źródło danych** | Połączenie z Prometheusem (lub innymi backendami) |
| **Panel kontrolny** | Kolekcja paneli ułożonych w układzie |
| **Panel** | Pojedyncza wizualizacja (wykres, miernik, tabela, heatmapa) |
| **Zmienna** | Filtr dynamiczny dla dashboardów (np. wybierz instancję) |
| **Adnotacja** | Zaznacz zdarzenia na wykresach (wdrożenia, incydenty) |
| **Reguła ostrzeżenia** | Alerty oparte na progach w Grafanie |
| **Szablon** | Wzory dashboardów wielokrotnego użytku ze zmiennymi |
### Przydatne wzorce pulpitu nawigacyjnego
| Wzór | Opis |
|--------|------------|
| **Wiersz przeglądowy** | Najważniejsze wskaźniki w skrócie: poziom błędów, opóźnienia, przepustowość |
| **Diagnozowanie** | Kliknij od podsumowania do widoku szczegółowego przy użyciu zmiennych |
| **Metoda CZERWONA** | Szybkość, błędy, czas trwania — trzy kluczowe wskaźniki usług |
| **UŻYJ metody** | Wykorzystanie, nasycenie, błędy — dla infrastruktury |
| **Złote sygnały** | Opóźnienie, ruch, błędy, nasycenie (książka Google SRE) |
---

## Alarmowanie
### Struktura reguły alertu
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

### Trasowanie menedżera alertów
| Koncepcja | Opis |
|--------|------------|
| **Grupa** | Połącz podobne alerty w jedno powiadomienie |
| **Trasa** | Drzewo dopasowań, które określa, dokąd trafiają alerty |
| **Odbiorca** | Gdzie wysyłać alerty (e-mail, Slack, PagerDuty, webhook) |
| **Zablokuj** | Pomiń alerty, gdy zostanie uruchomiony inny alert |
| **Cisza** | Tymczasowo wycisz alerty przez funkcję dopasowywania etykiet |
---

## Rozwiązywanie problemów
| Problem | Rozwiązanie |
|--------|----------|
| **Cel w dół** | Sprawdź, czy eksporter działa; sprawdź sieć/zaporę sieciową; sprawdź konfigurację złomowania |
| **Brak danych** | Sprawdź pisownię nazwy metryki; sprawdź filtry etykiet; sprawdź zakres czasu |
| **Wysoka kardynalność** | Zbyt wiele kombinacji etykiet; zmniejszyć wartości etykiet; użyj reguł nagrywania |
| **Powolne zapytania** | Używaj reguł nagrywania w przypadku złożonych zapytań; zwiększyć odstęp między skrobaniami |
| **Uwaga zmęczenie** | Dostosuj progi; dodaj czas trwania `for`; alerty związane z grupą |
| **Brakujące dane po ponownym uruchomieniu** | Prometheus przechowuje dane lokalnie; sprawdź ustawienia przechowywania |
---

## Streszczenie
Prometheus monitoruje systemy, w regularnych odstępach czasu pozyskując dane od eksporterów. Metryki występują w czterech typach: liczniki (tylko w górę), mierniki (w górę i w dół), histogramy (obserwacje zbiorcze) i podsumowania (kwantyle). PromQL to język zapytań — `rate()`, `increase()`,`histogram_quantile()`i funkcje agregujące (`sum`, `avg`) to najczęstsze operacje. Grafana wizualizuje dane Prometheusa w dashboardach z panelami, zmiennymi i adnotacjami. Funkcja alertów wykorzystuje usługę Alertmanager do grupowania, routingu, wyciszania i wstrzymywania alertów. Kluczowymi wzorcami monitorowania są złote sygnały Google (opóźnienie, ruch, błędy, nasycenie) oraz metoda RED (szybkość, błędy, czas trwania) w przypadku usług oraz metoda USE (wykorzystanie, nasycenie, błędy) w przypadku infrastruktury.