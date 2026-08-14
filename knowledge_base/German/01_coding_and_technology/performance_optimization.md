---
# Metadata
title: "Performance Optimisation"
description: "Profiling, caching, CDN, query optimisation, front-end perf"
category: "Coding and Technology"
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
    date: "2026-08-05"
    author: "Nepoznato-Dev"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-05"
review_date: "2027-02-05"
reviewed_by: "Coding & Technology Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [performance, optimization, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "8 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Leistungsoptimierung
Bei der Leistungsoptimierung geht es darum, Software schneller zu machen – Reaktionszeiten zu verkürzen, den Durchsatz zu erhöhen, die Speichernutzung zu senken und Engpässe zu beseitigen. Es ist eine der wirkungsvollsten Fähigkeiten, die ein Entwickler haben kann, denn langsame Software verliert Benutzer, verschwendet Ressourcen und frustriert alle. Aber es ist auch einer der häufigsten Fehler, wenn Entwickler die falschen Dinge auf der Grundlage ihrer Intuition und nicht auf der Grundlage von Beweisen optimieren.
---

## Die goldene Regel
> **Zuerst messen, dann optimieren.** Optimieren Sie niemals auf der Grundlage von Annahmen. Profilieren Sie den Code, finden Sie den tatsächlichen Engpass und beheben Sie ihn.
| Anti-Muster | Warum es schlecht ist |
|-------------|-------------|
| **Vorzeitige Optimierung** | Zeit damit verbringen, Code zu beschleunigen, der nicht langsam ist |
| **Optimierung ohne Messung** | Den falschen Engpass beheben; keine Möglichkeit, Verbesserung zu überprüfen |
| **Lesbarkeit zugunsten der Geschwindigkeit geopfert** | Unlesbarer Code kostet mehr als der Leistungsgewinn |
| **Alles zwischenspeichern** | Veraltete Daten, aufgeblähter Speicher, Komplexität |
---

## Profilerstellung
Bevor Sie etwas schneller machen können, müssen Sie wissen, *wo* die Zeit aufgewendet wird.
| Werkzeugtyp | Was es misst | Beispiele |
|-----------|-----------------|----------|
| **CPU-Profiler** | Welche Funktionen verbrauchen die meiste CPU-Zeit | cProfile (Python), perf (Linux), Chrome DevTools (JS) |
| **Speicherprofiler** | Speicherzuweisung und -lecks | Tracemalloc (Python), Valgrind, Heaptrack |
| **E/A-Profiler** | Festplatten- und Netzwerk-E/A-Engpässe | iotop, strace, Wireshark |
| **APM (Application Performance Monitoring)** | End-to-End-Anfrage-Timing | Neues Relikt, Datadog, Jaeger |
| **Browser DevTools** | Frontend-Rendering, JavaScript-Ausführung, Netzwerk | Chrome DevTools, Firefox Profiler |
### Profilierungs-Workflow
| Schritt | Beschreibung |
|------|-------------|
| 1. Identifizieren Sie den langsamen Vorgang | Benutzer berichten über langsames Laden der Seite; Überwachung zeigt hohe Latenz |
| 2. Profilieren Sie den vollständigen Pfad | Finden Sie heraus, welche Komponente am meisten Zeit benötigt |
| 3. Drilldown durchführen | Profilieren Sie diese bestimmte Komponente, um die Hot-Funktion zu finden |
| 4. Beheben Sie den Engpass | Wenden Sie die entsprechende Optimierung an |
| 5. Erneut messen | Überprüfen Sie die Verbesserung. auf Regressionen prüfen |
---

## Algorithmische Optimierung
Die größten Leistungssteigerungen ergeben sich aus der Auswahl besserer Algorithmen und nicht aus Mikrooptimierungen.
| Ändern | Verbesserung |
|--------|------------|
| Lineare Suche O(n) → Hash-Tabellensuche O(1) | 100x+ für große Datensätze |
| Verschachtelte Schleife O(n²) → Sortieren + binäre Suche O(n log n) | Größenordnungen für große n |
| Wiederholte Berechnung → Memoisierung / Caching | Eliminiert überflüssige Arbeit |
| String-Verkettung in einer Schleife → Builder / Join | Vermeidet das Kopieren quadratischer Zeichenfolgen |
| Unsortierte Daten → Sortierte Daten mit binärer Suche | O(log n) statt O(n) pro Suche |
---

## Caching-Strategien
Beim Caching werden die berechneten Ergebnisse gespeichert, sodass sie nicht erneut berechnet werden müssen.
| Cache-Typ | Standort | Geschwindigkeit | Lebenszeit |
|-----------|----------|-------|----------|
| **CPU-Cache** | L1/L2/L3 | ~1 ns | Automatisch |
| **Im Speicher** | Anwendungs-RAM (dict, HashMap) | ~100 ns | Bis zur Räumung oder Räumung |
| **Verteilter Cache** | Redis, Memcached | ~1 ms | Konfigurierbares TTL |
| **CDN** | Edgeserver weltweit | ~10-50 ms | Konfigurierbares TTL |
| **Browser-Cache** | Browser des Benutzers | ~1 ms | HTTP-Cache-Header |
| **Datenbankabfrage-Cache** | Datenbank- oder ORM-Ebene | ~1-10 ms | Bis sich die Daten ändern |
### Caching-Muster
| Muster | Beschreibung | Wann zu verwenden |
|---------|-------------|-------------|
| **Cache-beiseite** | Anwendung überprüft Cache; Lädt bei Fehlschlag von der DB; speichert im Cache | Am häufigsten; einfach |
| **Durchschreiben** | Gleichzeitig in Cache und DB schreiben | Beim Lesen >> schreibt; Konsistenz wichtig |
| **Write-behind** | In den Cache schreiben; asynchron in DB schreiben | Hoher Schreibdurchsatz; gewisses Datenverlustrisiko |
| **TTL (Time to Live)** | Cache-Einträge verfallen nach einer festgelegten Zeit | Wenn sich Daten regelmäßig ändern |
| **Ungültigkeit** | Veraltete Cache-Einträge explizit entfernen | Wenn Sie genau wissen, wann sich Daten ändern |
### Cache-Ungültigkeit
Die beiden schwierigsten Probleme in der Informatik: Cache-Ungültigmachung, Benennung von Dingen und Fehler, die nicht nacheinander auftreten.
| Strategie | Beschreibung |
|----------|-------------|
| **TTL-basiert** | Einträge verfallen nach N Sekunden; einfach, kann aber veraltete Daten liefern |
| **Ereignisgesteuert** | Ungültig machen, wenn sich Daten ändern; komplexer, aber genauer |
| **Versionsbasiert** | Geben Sie eine Versionsnummer an. Inkrement bei Änderungen |
| **Tag-basiert** | Tag-bezogene Cache-Einträge; Alle Einträge mit einem Tag | ungültig machen
---

## Datenbankoptimierung
Datenbanken sind oft der größte Engpass bei Webanwendungen.
| Technik | Beschreibung | Auswirkungen |
|-----------|-------------|--------|
| **Indizierung** | Fügen Sie Indizes für Spalten hinzu, die in WHERE, JOIN, ORDER BY | verwendet werden 10-1000x schnellere Abfragen |
| **Abfrageoptimierung** | Vermeiden Sie SELECT *; Verwenden Sie EXPLAIN, um Abfragen zu analysieren | I/O reduzieren |
| **Verbindungspooling** | Datenbankverbindungen wiederverwenden, statt neue zu erstellen | Eliminieren Sie den Verbindungsaufwand |
| **Replikate lesen** | Leseabfragen an Replikatdatenbanken weiterleiten | Leselast verteilen |
| **Partitionierung** | Große Tabellen in kleinere Partitionen aufteilen | Schnellere Abfragen großer Datenmengen |
| **Denormalisierung** | Fügen Sie redundante Daten hinzu, um Verknüpfungen zu vermeiden | Schnelleres Lesen; langsamer schreibt |
| **Materialisierte Ansichten** | Vorberechnete Abfrageergebnisse | Sofortige komplexe Abfragen |
| **N+1-Prävention** | Verwenden Sie JOINs, Eager Loading oder Batch-Abfragen | Eliminieren Sie Tausende von Abfragen |
---

## Parallelität und Parallelität
| Konzept | Beschreibung | Wann zu verwenden |
|---------|-------------|-------------|
| **Einfädeln** | Mehrere Threads innerhalb eines einzelnen Prozesses | I/O-gebundene Aufgaben (Netzwerk, Festplatte) |
| **Mehrfachverarbeitung** | Mehrere Prozesse (umgeht GIL in Python) | CPU-gebundene Aufgaben |
| **Asynchron/warten** | Kooperatives Multitasking; einzelner Thread | E/A mit hoher Parallelität (Webserver) |
| **GPU-Computing** | Tausende parallele Kerne | Matrixoperationen; Bildverarbeitung; ML |
### Async vs. Threading
| Aspekt | Asynchron/Warten | Einfädeln |
|--------|------------|-----------|
| **Modell** | Genossenschaft (Aufgaben ergeben Kontrolle) | Präventiv (Betriebssystem wechselt Threads) |
| **Overhead** | Sehr niedrig (kein Kontextwechsel) | Höher (Thread-Erstellung, Kontextwechsel) |
| **Komplexität** | Einfachere Argumentation (einzelner Thread) | Rennbedingungen, Deadlocks, Sperren |
| **Am besten für** | Viele gleichzeitige E/A-Vorgänge | Blockieren von Vorgängen, die nicht asynchron durchgeführt werden können |
| **Einschränkung** | CPU-gebundener Code kann nicht ohne Blockierung verwendet werden | GIL in Python schränkt echte Parallelität ein |
---

## Frontend-Leistung
| Technik | Beschreibung | Auswirkungen |
|-----------|-------------|--------|
| **Minimierung** | Leerzeichen entfernen und Variablennamen kürzen | 20-40 % kleinere Dateien |
| **Bündelung** | Kombinieren Sie mehrere Dateien in weniger Anfragen | Weniger HTTP-Anfragen |
| **Code-Splitting** | Laden Sie nur den Code, der für die aktuelle Seite benötigt wird | Schnelleres anfängliches Laden |
| **Verzögertes Laden** | Laden Sie Bilder und Komponenten, wenn sie benötigt werden | Schnelleres anfängliches Rendern |
| **Baum zittert** | Nicht verwendeten Code aus Bundles entfernen | Kleinere Bündel |
| **Bildoptimierung** | Verwenden Sie WebP/AVIF; reaktionsfähige Bilder; Lazy Loading | 50-80 % kleinere Bilder |
| **CDN** | Statische Assets von Edgeservern bereitstellen | Globale geringere Latenz |
| **HTTP/2 und HTTP/3** | Multiplexen; Header-Komprimierung; 0-RTT | Schnellerer Protokoll-Overhead |
| **Servicemitarbeiter** | Cache-Assets für die Offline-Nutzung; Push-Benachrichtigungen | Schnellere Wiederholungsbesuche |
---

## Speicheroptimierung
| Technik | Beschreibung |
|-----------|-------------|
| **Objektpooling** | Objekte wiederverwenden, statt neue zu erstellen |
| **Streaming** | Verarbeiten Sie Daten in Blöcken, anstatt alles in den Speicher zu laden |
| **Generatoren / Iteratoren** | Ertragswerte einzeln angeben, statt Listen zu erstellen |
| **Speicherzugeordnete Dateien** | Greifen Sie auf große Dateien zu, ohne sie vollständig zu laden |
| **Optimierung der Garbage Collection** | Passen Sie die GC-Parameter an Ihre Arbeitslast an |
| **Auswahl der Datenstruktur** | Verwenden Sie Arrays anstelle verknüpfter Listen für die Cache-Lokalität. Verwenden Sie Sets zum Testen der Mitgliedschaft |
---

## Netzwerkoptimierung
| Technik | Beschreibung |
|-----------|-------------|
| **Komprimierung** | gzip, Brotli für HTTP-Antworten |
| **Wiederverwendung von Verbindungen** | Keep-Alive-Verbindungen; HTTP/2-Multiplexing |
| **Batching anfordern** | Kombinieren Sie mehrere API-Aufrufe zu einem |
| **Paginierung** | Laden Sie Daten seitenweise statt alle auf einmal |
| **Kompression im Ruhezustand** | Daten in Datenbanken und Caches komprimieren |
| **Protokollauswahl** | gRPC (binär, effizient) vs. REST (für Menschen lesbar) |
---

## Überwachung und Alarmierung
| Metrisch | Was es Ihnen sagt |
|--------|----|
| **P50 / P95 / P99 Latenz** | Reaktionszeit bei verschiedenen Perzentilen |
| **Durchsatz** | Anfragen pro Sekunde |
| **Fehlerquote** | Prozentsatz fehlgeschlagener Anfragen |
| **CPU-Auslastung** | Wie viel Verarbeitungskapazität wird genutzt |
| **Speichernutzung** | RAM-Verbrauch; stößt man an Grenzen? |
| **Datenbankabfragezeit** | Langsame Abfragen, die optimiert werden müssen |
---

## Zusammenfassung
Leistungsoptimierung ist ein systematischer Prozess: messen, den Engpass identifizieren, beheben, erneut messen. Die größten Erfolge entstehen durch algorithmische Verbesserungen und die Eliminierung unnötiger Arbeit – nicht durch Mikrooptimierungen. Caching, Datenbankindizierung und Parallelität sind die leistungsstärksten Tools. Die Leistung des Frontends hängt von der Minimierung der Nutzlastgröße und der Roundtrips ab. Und die wichtigste Regel ist immer die gleiche: Raten Sie nicht – Profil.