---
# Metadata
title: "API Design and Architecture"
description: "REST, GraphQL, gRPC, versioning, auth, API gateways"
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
tags: [api, design, architecture, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "10 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# API-Design und Architektur
Eine API (Application Programming Interface) ist die Art und Weise, wie Softwarekomponenten miteinander kommunizieren. Eine gut gestaltete API ist intuitiv, konsistent und es macht Spaß, damit zu arbeiten. Eine schlecht gestaltete Version führt zu Verwirrung, Fehlern und Frustration. Diese Datei behandelt die Prinzipien, Muster und Praktiken zum Erstellen von APIs, die Entwickler tatsächlich verwenden möchten.
---

## REST-API-Prinzipien
REST (Representational State Transfer) ist der vorherrschende Architekturstil für Web-APIs. Es behandelt Daten als **Ressourcen**, die durch URLs identifiziert werden, und verwendet HTTP-Methoden, um sie zu verarbeiten.
### Grundprinzipien
| Prinzip | Beschreibung |
|-----------|-------------|
| **Ressourcen** | Alles ist eine Ressource mit einem URI (`/users/123`,`/orders/456`) |
| **HTTP-Methoden** | GET (Lesen), POST (Erstellen), PUT (Ersetzen), PATCH (Teilaktualisierung), DELETE (Entfernen) |
| **Staatenlosigkeit** | Jede Anfrage enthält alle benötigten Informationen; kein serverseitiger Sitzungsstatus |
| **Einheitliche Schnittstelle** | Konsistente Ressourcenbenennung, Standardmethoden, Standardstatuscodes |
| **Darstellung** | Ressourcen können in mehreren Formaten dargestellt werden (JSON, XML) |
### Konventionen zur Ressourcenbenennung
| Tun | Nicht |
|----|-------|
| `/users`(Pluralnomen) | `/user`(Singular) |
| `/users/123/orders`(verschachtelt) | `/getOrdersForUser?id=123`|
| `/products?category=electronics`(Abfrageparameter zum Filtern) | `/productsByCategory/electronics`|
| Verwenden Sie Bindestriche:`/user-profiles`| Verwenden Sie Unterstriche:`/user_profiles`|
### HTTP-Methoden und Idempotenz
| Methode | Zweck | Idempotent? | Sicher? |
|--------|---------|-------------|-------|
| **GET** | Eine Ressource lesen | ✅ Ja | ✅ Ja |
| **POST** | Erstellen Sie eine Ressource | ❌ Nein | ❌ Nein |
| **PUT** | Ersetzen Sie eine Ressource vollständig | ✅ Ja | ❌ Nein |
| **PATCH** | Eine Ressource teilweise aktualisieren | ❌ Nein* | ❌ Nein |
| **LÖSCHEN** | Eine Ressource entfernen | ✅ Ja | ❌ Nein |
*PATCH kann durch sorgfältiges Design idempotent gemacht werden.
### HTTP-Statuscodes
| Code | Bedeutung | Wann zu verwenden |
|------|---------|-------------|
| **200** | OK | Erfolgreiches GET, PUT, PATCH, DELETE |
| **201** | Erstellt | Erfolgreicher POST (Ressource erstellt) |
| **204** | Kein Inhalt | Erfolgreiches DELETE (keine Rückgabe möglich) |
| **400** | Ungültige Anfrage | Ungültige Eingabe oder fehlerhafte Anfrage |
| **401** | Nicht autorisiert | Fehlende oder ungültige Authentifizierung |
| **403** | Verboten | Authentifiziert, aber nicht autorisiert |
| **404** | Nicht gefunden | Ressource existiert nicht |
| **409** | Konflikt | Doppelter Ressourcen- oder Statuskonflikt |
| **422** | Nicht verarbeitbare Einheit | Gültiges JSON, aber semantische Fehler |
| **429** | Zu viele Anfragen | Ratenlimit überschritten |
| **500** | Interner Serverfehler | Unerwarteter Serverfehler |
| **502** | Schlechtes Gateway | Ausfall des Upstream-Dienstes |
| **503** | Dienst nicht verfügbar | Vorübergehende Überlastung oder Wartung |
---

## API-Versionierung
APIs entwickeln sich weiter. Wenn Sie wichtige Änderungen vornehmen müssen, sorgt die Versionierung dafür, dass bestehende Clients weiterarbeiten.
| Strategie | Beispiel | Vorteile | Nachteile |
|----------|---------|------|------|
| **URL-Pfad** | `/v1/users`,`/v2/users`| Einfach, explizit | URL-Änderungen pro Version |
| **Abfrageparameter** | `/users?version=2`| Flexibel | Leicht zu vergessen |
| **Kopfzeile** | `Accept: application/vnd.myapi.v2+json`| Saubere URLs | Weniger auffindbar |
| **Keine Versionierung** | Nur Schemaentwicklung | Am einfachsten | Breaking Changes betreffen alle |
**Best Practice**: Verwenden Sie aus Gründen der Übersichtlichkeit die URL-Pfadversionierung (`/v1/`). Unterstützen Sie mindestens eine frühere Version. Verwerfen Sie alte Versionen mit klaren Zeitplänen.
---

## Authentifizierungsmethoden
| Methode | Wie es funktioniert | Am besten für |
|--------|-------------|----------|
| **API-Schlüssel** | Geheimer Schlüssel im Header (`X-API-Key: abc123`) | Server-zu-Server, einfache Integrationen |
| **OAuth2** | Tokenbasierte Delegation mit Bereichen | Zugriff Dritter, vom Benutzer autorisierte Apps |
| **JWT** | Eigenständiger Token mit Ansprüchen | Zustandslose Authentifizierung über Dienste hinweg |
| **Basisauthentifizierung** | Base64-codierter Benutzername:Passwort | Nur Entwicklung – niemals Produktion ohne TLS |
| **Sitzungscookies** | Serverseitige Sitzungs-ID im reinen HTTP-Cookie | Traditionelle Webanwendungen |
### OAuth2-Fluss (vereinfacht)
1. Der Client leitet den Benutzer zum Autorisierungsserver weiter.
2. Der Benutzer meldet sich an und erteilt die Erlaubnis.
3. Der Autorisierungsserver gibt einen Autorisierungscode zurück.
4. Der Client tauscht Code gegen Zugriffstoken (und optional Aktualisierungstoken) aus.
5. Der Client verwendet ein Zugriffstoken, um die API aufzurufen.
6. Wenn das Zugriffstoken abläuft, verwenden Sie das Aktualisierungstoken, um ein neues zu erhalten.
---

## API-Stile: REST vs. GraphQL vs. gRPC
| Funktion | RUHE | GraphQL | gRPC |
|---------|------|---------|------|
| **Datenformat** | JSON (normalerweise) | JSON | Protobuf (binär) |
| **Endpunkte** | Mehrere (eine pro Ressource) | Einzelner Endpunkt | Definiert durch die .proto-Datei |
| **Übermäßiges Abrufen** | Häufig (mehr als nötig bekommen) | Keine (Client gibt Felder an) | Keine (schemadefiniert) |
| **Zu wenig Abruf** | Erfordert mehrere Aufrufe | Keine (genau das bekommen, was benötigt wird) | Keine |
| **Echtzeit** | WebSockets benötigt | Integrierte Abonnements | Integriertes Streaming |
| **Caching** | HTTP-Caching funktioniert natürlich | Schwieriger zu zwischenspeichern | Begrenzt |
| **Lernkurve** | Niedrig | Mittel | Mittel–Hoch |
| **Am besten für** | Öffentliche APIs, CRUD-Apps | Komplexe Benutzeroberflächen, mobile Apps | Interne Microservices, hochperformant |
---

## Paginierung, Filterung und Sortierung
Für Endpunkte, die Listen zurückgeben:
| Technik | Beispiel | Wann zu verwenden |
|-----------|---------|-------------|
| **Offset/Limit** | `?offset=20&limit=10`| Einfach; funktioniert für kleine Datensätze |
| **Cursorbasiert** | `?cursor=abc123&limit=10`| Große Datensätze; konsistente Ergebnisse |
| **Schlüsselsatz** | `?created_after=2024-01-01&limit=10`| Sehr effizient; erfordert einen eindeutigen Schlüssel |
```json
// Cursor-based response
{
  "data": [...],
  "pagination": {
    "next_cursor": "abc123",
    "has_more": true
  }
}
```

---

## Ratenbegrenzung
Schützen Sie Ihre API vor Missbrauch und sorgen Sie für eine faire Nutzung.
| Strategie | Wie es funktioniert |
|----------|-------------|
| **Festes Fenster** | N Anfragen pro Zeitfenster (z. B. 100/Stunde) |
| **Schiebefenster** | Körniger; zählt Anfragen im rollierenden Fenster |
| **Token-Bucket** | Tokens werden zu einem festen Preis hinzugefügt; Jede Anfrage verbraucht ein Token |
Geben Sie`429 Too Many Requests`mit Headern zurück:```
X-RateLimit-Limit: 100
X-RateLimit-Remaining: 0
X-RateLimit-Reset: 1625097600
Retry-After: 60
```

---

## Fehlerbehandlung
Konsistente Fehlerantworten erleichtern die Arbeit mit APIs erheblich:
```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Invalid input data",
    "details": [
      {
        "field": "email",
        "issue": "Invalid email format"
      }
    ]
  }
}
```

**Grundsätze**: Verwenden Sie eine konsistente Fehlerstruktur, schließen Sie umsetzbare Nachrichten ein, verwenden Sie Standard-HTTP-Statuscodes, protokollieren Sie Fehler serverseitig mit Korrelations-IDs und legen Sie niemals Stack-Traces oder interne Details offen.
---

## API-Dokumentation
| Werkzeug | Beschreibung |
|------|-------------|
| **OpenAPI (Swagger)** | Industriestandard für REST-API-Dokumentation |
| **Swagger-Benutzeroberfläche** | Interaktive API-Dokumentation von OpenAPI spec |
| **Postbote** | API-Tests, Dokumentation und Sammlungsfreigabe |
| **Redoc** | Wunderschöne API-Referenzdokumente aus der OpenAPI-Spezifikation |
| **GraphQL Playground / GraphiQL** | Interaktive GraphQL-Erkundung |
**Best Practice**: Schreiben Sie zuerst die OpenAPI-Spezifikation (spezifikationsgesteuerte Entwicklung) und generieren Sie dann daraus Dokumentation und Client-SDKs.
---

## API-Gateway-Muster
Ein API-Gateway sitzt zwischen Clients und Backend-Diensten und bietet einen einzigen Einstiegspunkt.
| Verantwortung | Beschreibung |
|---------------|-------------|
| **Routing** | Direkte Anfragen an entsprechende Backend-Dienste |
| **Authentifizierung** | Validieren Sie Token auf Gateway-Ebene |
| **Ratenbegrenzung** | Anwenden globaler oder pro Client begrenzter Grenzwerte |
| **Transformation** | Konvertieren zwischen Protokollen (REST ↔ gRPC) |
| **Caching** | Häufige Antworten zwischenspeichern |
| **Überwachung** | Zentralisierte Protokollierung und Metriken |
| **Lastausgleich** | Verteilen Sie den Datenverkehr auf Dienstinstanzen |
| Werkzeug | Geben Sie | ein
|------|------|
| **Kong** | Open-Source-API-Gateway (Nginx-basiert) |
| **AWS-API-Gateway** | Vollständig verwaltet, integriert in AWS |
| **Azure API Management** | Verwaltetes Gateway mit Entwicklerportal |
| **Gesandter / Istio** | Service Mesh mit API-Gateway-Funktionen |
| **Traefik** | Automatische Erkennung, Let's Encrypt-Integration |
---

## Webhooks
Mit Webhooks kann Ihre API Ereignisse in Echtzeit an Clients weiterleiten, anstatt dass Clients Änderungen abfragen müssen.
| Aspekt | Best Practice |
|--------|--------------|
| **Lieferung** | POST-Anfrage mit JSON-Nutzlast an die URL des Clients |
| **Sicherheit** | Nutzlasten mit HMAC signieren; Kunde überprüft Signatur |
| **Zuverlässigkeit** | Fehlgeschlagene Lieferungen mit exponentiellem Backoff wiederholen |
| **Idempotenz** | Geben Sie eine eindeutige Ereignis-ID an. Client verarbeitet Duplikate |
| **Versionierung** | API-Version in Webhook-Nutzlast einschließen |
---

## Design-Checkliste
- [ ] Ressourcen sind Substantive im Plural (`/users`, nicht`/getUser`)
- [ ] HTTP-Methoden korrekt verwendet (GET für Lesevorgänge, POST für Erstellungen usw.)
- [ ] Konsistentes Fehlerantwortformat
- [ ] Paginierung für alle Listenendpunkte
- [ ] Ratenbegrenzung mit klaren Headern
- [ ] API-Versionierungsstrategie definiert
- [ ] Authentifizierung und Autorisierung vorhanden
- [ ] Eingabevalidierung auf allen Endpunkten
- [ ] OpenAPI/Swagger-Dokumentation gepflegt
- [ ] CORS korrekt konfiguriert
– [ ] HTTPS wird in der Produktion erzwungen
- [ ] Idempotenzschlüssel für POST-Vorgänge, sofern erforderlich