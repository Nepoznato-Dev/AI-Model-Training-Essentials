---
# Metadata
title: "Low-Code and Platform Engineering"
description: "Low-code platforms, internal developer platforms, golden paths"
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
tags: [low, code, platform, engineering, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "5 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Low-Code- und Plattform-Engineering
Mit Low-Code-Plattformen können Benutzer Anwendungen mit minimalem handgeschriebenem Code erstellen – typischerweise über Drag-and-Drop-Schnittstellen, visuelle Workflows und vorgefertigte Konnektoren. Plattform-Engineering ist die Disziplin des Aufbaus interner Entwicklerplattformen (IDPs), die es Produktteams leicht machen, Infrastruktur, CI/CD und Betriebstools selbst zu bedienen. Beide Trends sind Antworten auf dasselbe Problem: die Kluft zwischen der Nachfrage nach Software und dem Angebot an Entwicklern, die diese erstellen können.
---

## Low-Code-Plattformen
### Was Low-Code eigentlich bedeutet
| Aspekt | Beschreibung |
|--------|-------------|
| **Visuelle Entwicklung** | Drag-and-Drop-UI-Builder; visuelle Workflow-Editoren; Formulardesigner |
| **Vorgefertigte Komponenten** | Vorgefertigte Widgets, Konnektoren, Vorlagen und Integrationen |
| **Deklarative Logik** | Konfigurieren Sie das Verhalten durch Regeln und Bedingungen, anstatt Code zu schreiben |
| **Erweiterbarkeit** | Möglichkeit, benutzerdefinierten Code hinzuzufügen, wenn die integrierten Funktionen der Plattform nicht ausreichen |
| **Verwaltete Infrastruktur** | Plattform übernimmt Hosting, Skalierung und Sicherheitspatches |
### Beliebte Low-Code-Plattformen
| Plattform | Stärke | Typischer Anwendungsfall |
|----------|----------|-----------------|
| **Microsoft Power Platform** | Tiefe Microsoft 365/Azure-Integration; Power Apps, Power Automate, Power BI | Unternehmensworkflows; interne Werkzeuge |
| **Salesforce-Plattform** | CRM-nativ; Apex für Erweiterungen; Flow Builder | Kundenorientierte Apps; Vertriebsabläufe |
| **ServiceNow** | IT-Servicemanagement; Workflow-Automatisierung | IT-Betrieb; Personalwesen; Einrichtungen |
| **Appian** | Process-Mining; Fallmanagement | Komplexe Geschäftsprozesse; Compliance |
| **OutSystems** | Full-Stack-Web und Mobile; Unternehmensklasse | Kundenportale; mobile Apps |
| **Umrüsten** | Interner Werkzeugbauer; stellt eine Verbindung zu Datenbanken und APIs her | Admin-Panels; Dashboards; Ops-Tools |
| **Lufttisch** | Tabellenkalkulations-Datenbank-Hybrid; Automatisierungen | Projektverfolgung; leichtes CRM |
### Wenn Low-Code gut funktioniert
| Szenario | Warum Low-Code passt |
|----------|-----|
| **Interne Tools** | Schnell aufzubauen; Benutzer sind intern, daher ist die Flexibilität der Benutzeroberfläche weniger wichtig |
| **Formulare und Genehmigungen** | Visuelle Workflow-Builder zeichnen sich dadurch aus |
| **CRUD-Anwendungen** | Die meisten Low-Code-Plattformen sind für Muster zum Erstellen, Lesen, Aktualisieren und Löschen optimiert
| **Prototyping** | Validieren Sie eine Idee in Stunden statt in Wochen |
| **Bürgerentwicklung** | Geschäftsanalysten können mit IT-Governance ihre eigenen Lösungen entwickeln |
### Wenn Low-Code zu kurz kommt
| Einschränkung | Auswirkungen |
|------------|--------|
| **Anbieterbindung** | Anwendungen können nicht einfach von der Plattform migriert werden |
| **Leistungsobergrenzen** | Nicht geeignet für Anwendungen mit hohem Durchsatz oder latenzempfindlichen Anwendungen |
| **UI-Einschränkungen** | Sonderanfertigungen sind schwierig; Sie sind auf das beschränkt, was die Plattform unterstützt |
| **Integrationskomplexität** | Für die Verbindung mit ungewöhnlichen APIs oder Legacy-Systemen kann ohnehin benutzerdefinierter Code erforderlich sein |
| **Kosten im Maßstab** | Die Preisgestaltung pro Benutzer oder pro App kann mit zunehmender Nutzung teuer werden |
| **Debugging-Schwierigkeit** | Visuelle Abstraktionen erschweren die Diagnose komplexer Probleme |
---

## Plattform-Engineering
### Das Problem, das Platform Engineering löst
| Ohne Plattform-Engineering | Mit Plattform-Engineering |
|---------------|-------------|
| Jedes Team verwaltet seine eigene Infrastruktur | Self-Service-Plattform-Abstracts-Infrastruktur |
| Inkonsistente Tools zwischen den Teams | Standardisierte Toolchain; goldene Wege |
| Entwickler warten darauf, dass der Betrieb Ressourcen bereitstellt | Entwickler stellen Ressourcen nach Bedarf bereit |
| Wissenssilos; Stammeswissen | Dokumentiert; automatisiert; auffindbar |
| Langsames Onboarding für neue Ingenieure | Neue Ingenieure können am ersten Tag einsetzen |
### Kernkomponenten einer internen Entwicklerplattform
| Komponente | Zweck | Beispieltools |
|-----------|---------|---------------|
| **Leistungskatalog** | Zentrales Register aller Dienste und ihrer Eigentümer | Hinter den Kulissen; Hafen; Kortex |
| **Vorgefertigtes Gerüst** | Generieren Sie neue Dienste aus genehmigten Vorlagen | Backstage-Softwarevorlagen; Ausstecher |
| **Selbstbedienungs-Infrastruktur** | Entwickler stellen Cloud-Ressourcen bereit, ohne Tickets einzureichen | Terraform-Module; Pulumi; Crossplane |
| **CI/CD-Pipelines** | Standardisierte Pipelines zum Erstellen, Testen und Bereitstellen | GitHub-Aktionen; GitLab CI; Argo-CD |
| **Umweltmanagement** | Kurzlebige Entwicklungs-/Staging-Umgebungen auf Anfrage | Vcluster; Namensraum; Gitpod |
| **Beobachtbarkeit** | Protokollierung, Metriken und Nachverfolgung sind in jeden Dienst integriert | Prometheus; Grafana; OpenTelemetry; Datenhund |
| **Geheimverwaltung** | Sichere Speicherung und Rotation von Anmeldeinformationen | Gewölbe; AWS Secrets Manager; SOPS |
| **Identität und Zugriff** | SSO; rollenbasierter Zugriff; Dienst-zu-Dienst-Authentifizierung | Okta; Schlüsselumhang; SPIFFE |
### Goldene Wege
Ein goldener Weg ist der unterstützte, eigensinnige Weg, etwas zu tun. Es ist der Weg des geringsten Widerstands – wenn man ihm folgt, funktioniert alles. Sie können vom Weg abweichen, aber Sie sind auf sich allein gestellt.
| Goldener Pfad | Was es bietet |
|-------------|---|
| **Neuer Service** | Vorlagen-Repo; CI/CD; Überwachung; Protokollierung; Bereitstellungskonfiguration |
| **Neue Datenbank** | Bereitgestellte Instanz; Verbindungszeichenfolgen in Geheimnissen; Sicherung konfiguriert |
| **Neues Frontend** | Pipeline erstellen; CDN; Vorschauumgebungen; Leuchtturm-Checks |
| **Datenpipeline** | Orchestrierung; Schemavalidierung; Überwachung; alarmierend |
### Build vs. Buy-Entscheidungen
| Faktor | Benutzerdefiniert erstellen | Vorhandenes Tool verwenden |
|--------|-------------|-------------------|
| **Kernkompetenz** | Einzigartig für Ihr Unternehmen; Wettbewerbsvorteil | Ware; jedes Unternehmen braucht es |
| **Wartungsaufwand** | Sie haben die Kapazität, es aufrechtzuerhalten | Das Tool wird vom Anbieter/der Community gut gepflegt |
| **Integrationsbedarf** | Tiefe Integration mit internen Systemen erforderlich | Standard-APIs und Konnektoren genügen |
| **Kosten** | Günstiger zu bauen als eine Lizenz | Günstiger zu lizenzieren als zu bauen |
---

## Die Beziehung zwischen Low-Code und Plattform-Engineering
| Dimension | Low-Code | Plattform-Engineering |
|-----------|----------|---------------------|
| **Zielbenutzer** | Geschäftsanwender; Bürgerentwickler | Professionelle Softwareentwickler |
| **Ziel** | Code reduzieren; Geschwindigkeit erhöhen | Reduzieren Sie die kognitive Belastung; Autonomie erhöhen |
| **Abstraktionsebene** | Sehr hoch; visuell | Medium; codebasiert, aber vereinfacht |
| **Flexibilität** | Begrenzt durch Plattformfunktionen | Volle Flexibilität; Sie können jeden beliebigen Code schreiben |
| **Governance** | Plattform erzwingt Regeln | Plattform bietet goldene Wege |
Sie ergänzen sich: Plattform-Engineering macht professionelle Entwickler schneller, während Low-Code es Nicht-Entwicklern ermöglicht, einfache Anwendungen zu erstellen. Gemeinsam gehen sie die Lücke bei der Softwarebereitstellung aus verschiedenen Blickwinkeln an.
---

## Zusammenfassung
Sowohl Low-Code-Plattformen als auch interne Entwicklerplattformen zielen darauf ab, die Anzahl der Personen zu erhöhen, die Software bereitstellen können. Low-Code erreicht dies, indem es den Code vollständig abstrahiert – visuelle Builder, vorgefertigte Konnektoren, deklarative Logik. Das Plattform-Engineering ermöglicht dies für professionelle Entwickler, indem es eine Self-Service-Infrastruktur, goldene Pfade und standardisierte Tools bereitstellt, sodass sie weniger Zeit mit Betriebsarbeit und mehr Zeit mit Produktfunktionen verbringen müssen. Beides ist kein Allheilmittel: Low-Code unterliegt einer Anbieterbindung und Leistungseinschränkungen, und die Entwicklung der Plattform erfordert fortlaufende Investitionen in deren Wartung. Aber wenn sie auf die richtigen Probleme angewendet werden – interne Tools, CRUD-Apps, standardisierte Servicebereitstellung – kann beides die Zeit von der Idee bis zur Produktion drastisch verkürzen.