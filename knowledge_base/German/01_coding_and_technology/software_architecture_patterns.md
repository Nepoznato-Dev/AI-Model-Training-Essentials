---
# Metadata
title: "Software Architecture Patterns"
description: "Monolith, microservices, event-driven, DDD, caching, SOLID"
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
tags: [software, architecture, patterns, coding-and-technology]
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
# Software-Architekturmuster
Architektur ist eine Reihe struktureller Entscheidungen darüber, wie ein System organisiert ist – welche Komponenten es hat, wie sie kommunizieren und wo die Verantwortlichkeiten liegen. Eine gute Architektur macht ein System leicht zu verstehen, zu modifizieren und zu skalieren. Schlechte Architektur macht jede Veränderung zu einem Kampf. In dieser Datei werden die wichtigsten Muster, deren Verwendung und die damit verbundenen Kompromisse behandelt.
---

## Monolith vs. Microservices
Dies ist die grundlegendste architektonische Entscheidung und es lohnt sich, sie richtig zu treffen.
| Aspekt | Monolith | Microservices |
|--------|----------|---------------|
| **Struktur** | Einzelne einsetzbare Einheit | Viele kleine, unabhängig einsetzbare Dienste |
| **Daten** | Gemeinsame Datenbank | Jeder Dienst besitzt seine Daten |
| **Kommunikation** | In-Process-Funktionsaufrufe | Netzwerkaufrufe (HTTP, gRPC, Messaging) |
| **Skalierung** | Skalieren Sie die gesamte Anwendung | Skalieren Sie einzelne Services |
| **Bereitstellung** | Einzelner Release-Zyklus | Unabhängige Bereitstellungen |
| **Komplexität** | Anfangs einfacher zu entwickeln | Operative Komplexität (Vernetzung, Überwachung) |
| **Am besten für** | Kleine Teams, Produkte im Frühstadium | Große Teams, komplexe Domänen, großer Umfang |
### Wann man mit einem Monolithen beginnen sollte
Die meisten Anwendungen sollten als Monolith beginnen. Es ist einfacher zu erstellen, zu testen, bereitzustellen und zu debuggen. Sie können Dienste jederzeit später extrahieren, wenn Sie ein klareres Bild Ihrer Domänengrenzen haben. Dies wird manchmal als „modularer Monolith“ bezeichnet – ein Monolith mit klaren inneren Grenzen, die die spätere Extraktion erleichtern.
### Wann Sie Microservices nutzen sollten
Ziehen Sie Microservices in Betracht, wenn:
- Die Teams sind groß genug, dass die Koordination zum Engpass wird.
- Verschiedene Teile des Systems haben sehr unterschiedliche Skalierungsanforderungen.
- Sie benötigen eine unabhängige Bereitstellung von Komponenten.
- Ihre Domain verfügt über klar begrenzte Kontexte (siehe DDD unten).
---

## Geschichtete Architektur (N-Tier)
Das häufigste Architekturmuster. Der Code ist in Schichten organisiert, von denen jede eine bestimmte Verantwortung hat.
```
â”Œ─────────────────────────┐
│   Presentation Layer    │  ← UI, controllers, API endpoints
├─────────────────────────┤
│   Application Layer     │  ← Use cases, orchestration
├─────────────────────────┤
│   Domain Layer          │  ← Business logic, entities
├─────────────────────────┤
│   Infrastructure Layer  │  ← Database, external services, file I/O
└─────────────────────────┘
```

| Schicht | Verantwortung | Regel |
|-------|---------------|------|
| **Präsentation** | Behandeln Sie Benutzer-/HTTP-Anfragen | Kann nur die Anwendungsschicht aufrufen |
| **Bewerbung** | Anwendungsfälle orchestrieren | Kann die Domänenschicht | aufrufen
| **Domäne** | Kerngeschäftslogik | Sollte nicht von anderen Schichten abhängen |
| **Infrastruktur** | Technische Bedenken | Implementiert in Domäne | definierte Schnittstellen
**Schlüsselregel**: Abhängigkeiten zeigen nach innen. Die Domänenschicht kennt weder die Datenbank noch das Web-Framework.
---

## Ereignisgesteuerte Architektur
Komponenten kommunizieren, indem sie **Ereignisse** aussenden und darauf reagieren – Dinge, die passiert sind.
| Muster | Beschreibung |
|---------|-------------|
| **Ereignisbenachrichtigung** | Dienst A gibt „OrderPlaced“ aus; Dienste B, C, D reagieren |
| **Event-Sourcing** | Alle Zustandsänderungen als Abfolge von Ereignissen speichern (nicht nur den aktuellen Zustand) |
| **CQRS** | Lesemodell (Abfragen) vom Schreibmodell (Befehle) trennen |
### Event-Sourcing
Anstatt den „aktuellen Zustand“ in einer Datenbank zu speichern, speichern Sie jede Zustandsänderung als Ereignis:
```
OrderCreated(order_id=123, total=$50)
OrderPaid(order_id=123, payment_id=456)
OrderShipped(order_id=123, tracking=ABC)
```

Vorteile: vollständiger Prüfpfad, Möglichkeit zur Rekonstruktion vergangener Zustände, entkoppelte Verbraucher. Herausforderungen: Entwicklung des Ereignisschemas, letztendliche Konsistenz, Komplexität des Debuggens.
### CQRS (Command Query Responsibility Segregation)
| Seite | Zweck | Datenbank |
|------|---------|----------|
| **Befehl (Schreiben)** | Umgang mit Mutationen; Geschäftsregeln durchsetzen | Optimiert für Schreibvorgänge (normalisiert) |
| **Abfrage (Lesen)** | Leseanfragen bedienen | Optimiert für Lesevorgänge (denormalisiert) |
CQRS lässt sich natürlich mit Event Sourcing kombinieren: Ereignisse von der Schreibseite werden in leseoptimierte Ansichten projiziert.
---

## Nachrichtenwarteschlangen und Ereignisbroker
Wenn Dienste asynchron kommunizieren müssen, sind Nachrichtenwarteschlangen das Rückgrat.
| Werkzeug | Geben Sie | ein Am besten für |
|------|------|----------|
| **Apache Kafka** | Verteiltes Ereignisprotokoll | Event-Streaming mit hohem Durchsatz, Event-Sourcing |
| **RabbitMQ** | Nachrichtenbroker mit Routing | Aufgabenwarteschlangen, komplexe Routingmuster |
| **AWS SQS** | Verwaltete Warteschlange | AWS-natives, einfaches Warteschlangensystem |
| **AWS SNS** | Pub/Sub-Benachrichtigung | Weitergabe an mehrere Abonnenten |
| **Google Pub/Sub** | Verwalteter Pub/Sub | GCP-natives Event-Streaming |
| **Redis-Streams** | Leichter Stream | Einfache Ereignisprotokollierung, Caching-Anwendungsfälle |
### Nachrichtenmuster
| Muster | Beschreibung |
|---------|-------------|
| **Punkt-zu-Punkt** | Ein Produzent, ein Konsument pro Nachricht |
| **Veröffentlichen/Abonnieren** | Ein Produzent, mehrere Abonnenten |
| **Anfrage/Antwort** | Synchroner Transport über asynchronen Transport |
| **Warteschlange für unzustellbare Nachrichten** | Nachrichten, deren Verarbeitung fehlschlägt, werden zur Überprüfung in eine separate Warteschlange gestellt |
---

## Domain-Driven Design (DDD)
DDD ist ein strategischer Ansatz für das Softwaredesign, bei dem der Code eher auf Geschäftskonzepten als auf technischen Belangen ausgerichtet ist.
### Schlüsselkonzepte
| Konzept | Beschreibung |
|---------|-------------|
| **Begrenzter Kontext** | Eine Grenze, innerhalb derer ein Domänenmodell konsistent ist (z. B. „Bestellung“, „Versand“, „Abrechnung“) |
| **Allgegenwärtige Sprache** | Gemeinsames Vokabular zwischen Entwicklern und Domänenexperten |
| **Aggregate** | Cluster zusammengehöriger Entitäten, die bei Datenänderungen als eine Einheit behandelt werden |
| **Entitäten** | Objekte mit Identität (z. B. ein Benutzer mit einer Benutzer-ID) |
| **Wertobjekte** | Objekte ohne Identität; definiert durch ihre Attribute (z. B. Geld, Adresse) |
| **Domänenereignisse** | Etwas, das in der Domain passiert ist (z. B. OrderPlaced) |
| **Antikorruptionsschicht** | Übersetzungsschicht zwischen Ihrer Domain und externen Systemen |
### Wenn DDD hilft
DDD ist am wertvollsten, wenn der Geschäftsbereich komplex ist – denken Sie an E-Commerce, Logistik, Finanzdienstleistungen, Gesundheitswesen. Wenn Ihre Domain einfach ist (ein Blog, eine ToDo-App), ist DDD übertrieben.
---

## Caching-Strategien
Caching ist eine der effektivsten Methoden zur Verbesserung der Leistung, bringt jedoch Komplexität in Bezug auf die Konsistenz mit sich.
| Strategie | Beschreibung | Kompromiss |
|----------|-------------|-----------|
| **Cache-beiseite** | Die Anwendung überprüft zuerst den Cache. Lädt aus der Datenbank bei Fehlschlag | Einfach; letztendliche Konsistenz |
| **Durchschreiben** | Gleichzeitig in Cache und DB schreiben | Konsistent; langsamer schreibt |
| **Write-Behind** | In den Cache schreiben; asynchrones Schreiben in die Datenbank | Schnelles Schreiben; Risiko von Datenverlust |
| **Durchlesen** | Cache-Ladevorgänge aus der Datenbank bei Fehlern transparent | Einfacher als Cache-beiseite |
### Was zwischengespeichert werden soll
| Schicht | Was | Werkzeuge |
|-------|------|-------|
| **CDN** | Statische Assets, API-Antworten | CloudFront, Cloudflare |
| **Bewerbung** | Berechnete Ergebnisse, Sitzungsdaten | Redis, Memcached |
| **Datenbank** | Abfrageergebnisse, häufig aufgerufene Zeilen | Abfragecache, materialisierte Ansichten |
**Cache-Ungültigmachung** ist bekanntermaßen schwierig. Gängige Strategien: TTL (Time-to-Live), ereignisgesteuerte Invalidierung (Cache bei Datenänderung leeren) und LRU-Eviction (zuletzt verwendet).
---

## Designmuster
### SOLIDE Prinzipien
| Prinzip | Was es bedeutet |
|-----------|--------------|
| **S** – Einzelverantwortung | Eine Klasse sollte einen Grund haben, sich zu ändern |
| **O** – Offen/Geschlossen | Offen für Erweiterung, geschlossen für Änderung |
| **L** – Liskov-Ersatz | Untertypen sollten durch ihre Basistypen | ersetzt werden können
| **I** – Schnittstellentrennung | Viele spezifische Schnittstellen > eine Allzweckschnittstelle |
| **D** – Abhängigkeitsumkehr | Verlassen Sie sich auf Abstraktionen, nicht auf Konkretionen |
### Gemeinsame Muster
| Muster | Absicht | Beispiel |
|---------|--------|---------|
| **Singleton** | Stellen Sie sicher, dass eine Klasse nur eine Instanz | hat Datenbankverbindungspool |
| **Fabrik** | Erstellen Sie Objekte, ohne die genaue Klasse | anzugeben `UserFactory.create(type="admin")`|
| **Beobachter** | Angehörige benachrichtigen, wenn sich der Status ändert | Ereignis-Listener, Pub/Sub |
| **Strategie** | Algorithmen zur Laufzeit austauschen | Zahlungsstrategie: Kreditkarte, PayPal, Krypto |
| **Repository** | Abstrakter Datenzugriff hinter einer sauberen Schnittstelle | `UserRepository.find_by_id(123)`|
| **Dekorateur** | Verhalten dynamisch hinzufügen | Logging-Dekorator rund um einen Dienst |
| **Adapter** | Sorgen Sie dafür, dass inkompatible Schnittstellen zusammenarbeiten | Legacy-API-Adapter |
---

## Die richtige Architektur wählen
Es gibt keine allgemein „beste“ Architektur. Die richtige Wahl hängt ab von:
| Faktor | Bevorzugen Sie Monolith, wenn... | Bevorzugen Sie Microservices, wenn... |
|--------|----------|-----------------------------|
| **Teamgröße** | < 10 developers | >20 Entwickler, mehrere Teams |
| **Domänenkomplexität** | Einfach oder gut verstanden | Komplexe, viele begrenzte Kontexte |
| **Maßstabsanforderungen** | Einheitliche Skalierungsanforderungen | Unterschiedliche Komponenten erfordern unterschiedliche Skalierungen |
| **Bereitstellungsrhythmus** | Einzelner Release-Zyklus | Unabhängige Bereitstellungen erforderlich |
| **Technologievielfalt** | Ein Stapel ist in Ordnung | Unterschiedliche Dienste erfordern unterschiedliche Technologie |
**Praktischer Rat**: Beginnen Sie mit einem modularen Monolithen. Extrahieren Sie Dienste nur, wenn Sie einen klaren Bedarf und klare Domänengrenzen haben. Vorzeitige Microservices gehören zu den häufigsten Architekturfehlern in der Branche.