---
# Metadata
title: "Cloud Architecture"
description: "Cloud providers, architecture patterns, security"
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
tags: [cloud, architecture, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "11 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Cloud-Architektur
Cloud Computing hat die Art und Weise, wie Unternehmen Software erstellen, bereitstellen und skalieren, grundlegend verändert. Anstatt physische Server zu kaufen und zu warten, können Sie Rechenressourcen nach Bedarf bereitstellen, für die Nutzung bezahlen und innerhalb von Minuten global skalieren. Diese Datei deckt die Kernkonzepte, Architekturmuster, Dienste und Best Practices ab, die Sie kennen müssen.
---

## Cloud Computing-Grundlagen
### Was ist Cloud Computing?
On-Demand-Bereitstellung von Computerressourcen – Server, Speicher, Datenbanken, Netzwerke, Software – über das Internet mit nutzungsbasierter Bezahlung.
### Wesentliche NIST-Merkmale
| Charakteristisch | Bedeutung |
|---------------|---------|
| **Selbstbedienung auf Abruf** | Bereitstellung von Ressourcen ohne menschliche Interaktion |
| **Breiter Netzwerkzugriff** | Verfügbar über das Netzwerk über Standardmechanismen |
| **Ressourcenpooling** | Multi-Tenant-Modell; Ressourcen dynamisch zugewiesen |
| **Schnelle Elastizität** | Schnell nach außen und innen skalieren |
| **Gemessener Service** | Die Nutzung wird überwacht und abgerechnet |
### Bereitstellungsmodelle
| Modell | Beschreibung | Wann zu verwenden |
|-------|-------------|-------------|
| **Öffentliche Cloud** | Im Besitz von Anbietern; Gemeinsame Infrastruktur (AWS, Azure, GCP) | Die meisten Arbeitsbelastungen; kostengünstig |
| **Private Cloud** | Einer einzelnen Organisation gewidmet | Regulatorische Anforderungen, sensible Daten |
| **Hybrid Cloud** | Kombination von öffentlich und privat | Flexibilität + Compliance |
| **Multi-Cloud** | Verwendung mehrerer öffentlicher Cloud-Anbieter | Vermeiden Sie Anbieterbindung, Best-of-Breed |
### Servicemodelle
| Modell | Bietet | Beispiele | Anwendungsfälle |
|-------|----------|----------|-----------|
| **IaaS** | VMs, Speicher, Netzwerke, Betriebssystem | AWS EC2, Azure-VMs, GCP Compute Engine | Lift-and-Shift-Migrationen, volle Kontrolle |
| **PaaS** | Entwicklungsplattformen, Datenbanken, Middleware | Heroku, Google App Engine, AWS Elastic Beanstalk | App-Entwicklung, API-Bereitstellung |
| **SaaS** | Vollständige Bewerbungen über das Internet | Salesforce, Google Workspace, Microsoft 365 | E-Mail, CRM, Zusammenarbeit |
| **FaaS / Serverlos** | Ereignisgesteuerte Funktionsausführung | AWS Lambda, Azure Functions, GCP Cloud Functions | APIs, Ereignisverarbeitung, geplante Aufgaben |
---

## Große Cloud-Anbieter
| Anbieter | Marktanteil | Stärken |
|----------|-------------|-----------|
| **AWS** | ~32% | Umfangreichster Servicekatalog, größtes Ökosystem |
| **Azurblau** | ~23% | Unternehmensintegration, Hybrid Cloud, Microsoft Stack |
| **GCP** | ~10 % | Datenanalyse, KI/ML, Kubernetes |
| **Alibaba Cloud** | ~4% | Dominant im asiatisch-pazifischen Raum |
| **Orakelwolke** | ~2% | Datenbank-Workloads, Unternehmensanwendungen |
| **IBM Cloud** | ~2% | Unternehmensfokus, Watson AI |
| **DigitalOcean** | Nische | Entwicklerfreundliche, vereinfachte Angebote |
### Leistungsvergleich (Top 3 Anbieter)
| Kategorie | AWS | Azure | GCP |
|----------|-----|-------|-----|
| **Berechnen** | EC2, Lambda, ECS | VMs, Funktionen, AKS | Compute Engine, Cloud Functions, GKE |
| **Speicher** | S3, EBS, Gletscher | Blob-Speicher, Festplattenspeicher | Cloud-Speicher, persistente Festplatte |
| **Datenbank** | RDS, DynamoDB, Aurora | SQL-Datenbank, Cosmos DB | Cloud SQL, Firestore, Bigtable |
| **Analytik** | Rotverschiebung, EMR | Synapse, Databricks | BigQuery, Datenfluss |
| **KI/ML** | SageMaker, Anerkennung | Azure ML, kognitive Dienste | Vertex AI, AutoML |
| **Netzwerk** | VPC, Route 53, CloudFront | VNet, Verkehrsmanager | VPC, Cloud DNS, Cloud CDN |
---

## Architekturmuster
### Gut strukturiertes Framework
Alle drei großen Anbieter veröffentlichen gut strukturierte Frameworks, die auf fünf Säulen basieren:
| Säule | Grundprinzipien |
|--------|---------------|
| **Betriebliche Exzellenz** | Abläufe automatisieren; häufige, reversible Änderungen vornehmen; mit einem Scheitern rechnen |
| **Sicherheit** | Starkes Identitätsfundament; Sicherheit auf jeder Ebene anwenden; Daten während der Übertragung und im Ruhezustand schützen |
| **Zuverlässigkeit** | Testwiederherstellungsverfahren; automatische Wiederherstellung nach einem Fehler; horizontal skalieren |
| **Leistungseffizienz** | Serverlos verwenden; Werden Sie in wenigen Minuten global; experimentiere oft |
| **Kostenoptimierung** | Konsummodell übernehmen; Managed Services nutzen; Hören Sie auf, für undifferenzierte Arbeit auszugeben |
### Gemeinsame Muster
| Muster | Beschreibung | Vorteile | Herausforderungen |
|---------|-------------|----------|------------|
| **Microservices** | App in kleine, unabhängige Dienste zerlegen | Skalierbarkeit, Fehlerisolierung, unabhängige Bereitstellung | Verteilte Komplexität, Datenkonsistenz |
| **Ereignisgesteuert** | Komponenten kommunizieren über Ereignisse | Lose Kopplung, Echtzeitverarbeitung | Debugging-Komplexität, letztendliche Konsistenz |
| **Serverlos** | Keine Serververwaltung; Bezahlung pro Ausführung | Kosteneffizienz, schnelle Bereitstellung | Kaltstarts, Lieferantenbindung, Ausführungsbeschränkungen |
| **Mehrschichtig (N-Tier)** | Präsentation → Geschäftslogik → Datenzugriff → Datenbank | Trennung von Belangen, Wartbarkeit | Kann monolithisch werden |
| **Weltraumbasiert** | Verteilte Daten über virtualisierte Speicherknoten | Bewältigt hohe Parallelität und geringe Latenz | Komplex zu entwerfen und zu verwalten |
---

## Kerndienste
### Berechnen
| Servicetyp | Einzelheiten |
|-------------|---------|
| **Virtuelle Maschinen** | Universell einsetzbar, rechenoptimiert, speicheroptimiert, GPU. Preise: auf Anfrage, reserviert, vor Ort. |
| **Container** | Docker-Laufzeit; Orchestrierung über Kubernetes (EKS, AKS, GKE). Register: ECR, GCR, ACR. |
| **Serverlose Funktionen** | Ereignisgesteuert, zustandslos. Beschränkungen der Ausführungszeit, des Speichers und der Parallelität. |
### Lagerung
| Geben Sie | ein Eigenschaften | Beispiele | Am besten für |
|------|----------------|----------|----------|
| **Objekt** | Flache Struktur, HTTP-Zugriff, reich an Metadaten | S3, Cloud-Speicher, Azure Blob | Statische Assets, Backups, Data Lakes |
| **Blockieren** | An VMs angehängte Rohdatenträger | EBS, Persistente Festplatte, Azure Disks | Datenbanken, Boot-Volumes |
| **Datei** | Freigegebene Dateisysteme (NFS/SMB) | EFS, Filestore, Azure Files | Inhaltsverwaltung, freigegebene Konfigurationen |
| **Archiv** | Niedrigste Kosten, Abrufverzögerungen | S3 Glacier, Azure-Archiv | Compliance, Langzeitsicherungen |
### Datenbanken
| Kategorie | Dienstleistungen | Anwendungsfall |
|----------|----------|----------|
| **Verwaltet relational** | RDS, Cloud SQL, Azure SQL | Traditionelle Apps, ACID-Transaktionen |
| **NoSQL – Dokument** | DocumentDB, Firestore, Cosmos DB | Flexible Schemata, JSON-Daten |
| **NoSQL – Schlüsselwert** | DynamoDB, Redis-Cache | Caching, Sitzungen, einfache Suchvorgänge |
| **NoSQL – Wide-Column** | Bigtable, Cassandra | Schreiblastige Zeitreihen |
| **NoSQL – Diagramm** | Neptune, Cosmos DB (Graph-API) | Beziehungen, soziale Netzwerke |
| **Data Warehousing** | Schneeflocke, Redshift, BigQuery, Synapse | Analytik, BI |
| **Caching** | ElastiCache, Cloud Memorystore | Sitzungsspeicher, Abfrage-Caching |
---

## Vernetzung
### Virtuelle Netzwerke
Jede Cloud-Bereitstellung befindet sich in einer Virtual Private Cloud (VPC/VNet) – einem isolierten Netzwerk, das Sie mit CIDR-Blöcken, Subnetzen (öffentlich oder privat), Routing-Tabellen und Gateways definieren.
### Load Balancing und CDN
| Service | Zweck |
|---------|---------|
| **Load Balancer** | Verteilen Sie den Datenverkehr auf Instanzen (L4-Netzwerk, L7-Anwendung) |
| **CDN** | Zwischenspeichern von Inhalten an Edge-Standorten für geringere Latenz (CloudFront, Cloud CDN, Azure CDN) |
| **DNS** | Domänenregistrierung, Routing-Richtlinien, Gesundheitsprüfungen (Route 53, Cloud DNS, Azure DNS) |
### Konnektivitätsoptionen
| Option | Beschreibung |
|--------|-------------|
| **Internet-Gateway** | Öffentlicher Internetzugang für VPC |
| **NAT-Gateway** | Ausgehender Zugriff auf das private Subnetz |
| **VPN** | Verschlüsselte Tunnel zum lokalen Standort |
| **Direct Connect / ExpressRoute** | Dedizierte private Verbindungen |
| **VPC-Peering** | VPCs innerhalb oder zwischen Konten verbinden |
---

## Sicherheit
### Modell der geteilten Verantwortung
| Schicht | Anbieter | Kunde |
|-------|----------|----------|
| **Infrastruktur** (Hardware, Einrichtungen) | ✅ | |
| **Computing, Speicher, Netzwerk** | ✅ (verwaltet) | ✅ (selbstverwaltet) |
| **Daten, Anwendungen, Identität** | | ✅ |
Je besser der Dienst verwaltet wird, desto mehr übernimmt der Anbieter. Mit IaaS verwalten Sie fast alles; Bei SaaS übernimmt der Anbieter fast alles.
### Identitäts- und Zugriffsmanagement (IAM)
| Konzept | Beschreibung |
|---------|-------------|
| **Benutzer** | Individuelle Identitäten |
| **Gruppen** | Sammlungen von Benutzern |
| **Rollen** | Temporäre Anmeldeinformationen für Dienste oder Benutzer |
| **Richtlinien** | Dokumente, die Berechtigungen definieren |
| **Prinzip** | Geringste Privilegien, Aufgabentrennung |
### Datenschutz
- **Verschlüsselung im Ruhezustand**: KMS, vom Kunden verwaltete Schlüssel, HSM.
- **Verschlüsselung während der Übertragung**: TLS/SSL, HTTPS.
- **Geheimnisverwaltung**: Secrets Manager, Key Vault – Geheimnisse niemals fest codieren.
---

## DevOps in der Cloud
### Infrastruktur als Code (IaC)
| Werkzeug | Beschreibung |
|------|-------------|
| **Terraform** | Multi-Cloud, deklarative HCL, Zustandsverwaltung |
| **CloudFormation** | AWS-native YAML/JSON-Vorlagen |
| **ARM-Vorlagen / Bizeps** | Azure-nativ |
| **Pulumi** | Infrastruktur mit Programmiersprachen (Python, Go usw.) |
### CI/CD-Dienste
| Anbieter | Werkzeuge |
|----------|-------|
| **AWS** | CodePipeline, CodeBuild, CodeDeploy |
| **Azurblau** | Azure DevOps, GitHub-Aktionen |
| **GCP** | Cloud-Build, Cloud-Bereitstellung |
| **Drittanbieter** | Jenkins, CircleCI, GitLab CI |
### Überwachung und Beobachtbarkeit
| Fähigkeit | AWS | Azure | GCP |
|-----------|-----|-------|-----|
| **Metriken** | CloudWatch | Azure Monitor | Cloud-Überwachung |
| **Protokollierung** | CloudWatch-Protokolle | Protokollanalyse | Cloud-Protokollierung |
| **Nachverfolgung** | Röntgen | Anwendungseinblicke | Cloud Trace |
---

## Kostenmanagement
### Preismodelle
| Modell | Beschreibung | Am besten für |
|-------|-------------|----------|
| **On-Demand** | Bezahlen Sie für das, was Sie nutzen, sekunden-/stundengenau | Variable, kurzfristige Arbeitsbelastungen |
| **Reservierte Instanzen** | 1–3 Jahre Laufzeit, erheblicher Rabatt | Steady-State-Workloads |
| **Spot-Instanzen** | Gebot für ungenutzte Kapazität; kann unterbrochen werden | Fehlertolerante, flexible Arbeitsplätze |
| **Sparpläne** | Flexible Vertragspreise | Gemischte Nutzungsmuster |
| **Kostenloses Kontingent** | Begrenzte kostenlose Nutzung für neue Konten | Lernen, Prototyping |
### Optimierungsstrategien
Instanzen in der richtigen Größe passend zur Arbeitslast. Verwenden Sie die automatische Skalierung, um Nachfragespitzen zu bewältigen. Reservekapazität für vorhersehbare Belastungen. Verwenden Sie Spot-Instanzen für Batch-Jobs. Verschieben Sie Daten, auf die selten zugegriffen wird, auf günstigere Speicherebenen. Löschen Sie ungenutzte Ressourcen (verwaiste Snapshots, inaktive Load Balancer, nicht verbundene IPs).
---

## Hohe Verfügbarkeit und Notfallwiederherstellung
### Verfügbarkeitskonzepte
| Konzept | Beschreibung |
|---------|-------------|
| **Verfügbarkeitszone (AZ)** | Physisch getrennte Rechenzentren innerhalb einer Region |
| **Region** | Geografisches Gebiet mit mehreren AZs |
| **Edge-Standort** | CDN-Cache-Speicherort für die Inhaltsbereitstellung |
### Disaster-Recovery-Strategien
| Strategie | Kosten | RTO | RPO | Beschreibung |
|----------|------|-----|-----|-------------|
| **Sichern und Wiederherstellen** | Niedrigster | Stunden | Stunden–Tage | Regelmäßige Backups, Wiederherstellung bei Bedarf |
| **Pilotlicht** | Niedrig | Minuten–Stunden | Minuten | Kernelemente laufen immer und können im Katastrophenfall hochskaliert werden |
| **Warm-Standby** | Mittel | Minuten | Sekunden–Minuten | Verkleinerte Version läuft immer |
| **Multi-Site Aktiv/Aktiv** | Höchste | Nahe Null | Null | Volle Produktion in mehreren Regionen |
**RTO** (Recovery Time Objective) = maximal akzeptable Ausfallzeit. **RPO** (Recovery Point Objective) = maximal akzeptabler Datenverlust.
---

## Neue Trends
| Trend | Was passiert |
|-------|-----------------|
| **Edge Computing** | Daten näher an der Quelle verarbeiten (AWS Outposts, Wavelength, Azure Edge) |
| **Multi-Cloud** | Vermeidung einer Lieferantenbindung; Nutzung des Best-of-Breed aller Anbieter |
| **KI/ML-Dienste** | Vorab trainierte Modelle (Sehen, Sprache, Sprache) + individuelles Training (SageMaker, Vertex AI) |
| **Quantencomputing** | Experimentelle Dienste im Frühstadium (AWS Braket, Azure Quantum) |
| **Nachhaltige Cloud** | Verfolgung des CO2-Fußabdrucks, Engagements für erneuerbare Energien, grüne Architektur |