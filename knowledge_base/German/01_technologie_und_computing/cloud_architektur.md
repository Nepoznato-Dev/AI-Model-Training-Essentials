<!-- 
This file was automatically translated from English to German.
Source: cloud_architecture.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# Cloud Architektur

## Grundlagen des Cloud Computing

### Was ist Cloud Computing?
Bedarfsgerechte Bereitstellung von Rechenressourcen (Server, Speicher, Datenbanken, Netzwerke, Software) über das Internet mit nutzungsbasierter Preisgestaltung.

### Wesentliche Merkmale (NIST-Definition)
- **On-Demand Self-Service**: Ressourcen ohne menschliche Interaktion bereitstellen
- **Breiter Netzwerkzugriff**: Über Netzwerk via Standardmechanismen verfügbar
- **Ressourcen-Pooling**: Mandantenfähiges Modell mit dynamischer Zuweisung
- **Schnelle Elastizität**: Schnell nach außen und innen skalieren
- **Gemessener Service**: Ressourcennutzung überwacht und abgerechnet

### Cloud-Bereitstellungsmodelle
- **Public Cloud**: Im Besitz von Anbietern, gemeinsame Infrastruktur (AWS, Azure, GCP)
- **Private Cloud**: Dedicated für eine einzelne Organisation (vor Ort oder gehostet)
- **Hybrid Cloud**: Kombination von Public und Private Clouds
- **Multi-Cloud**: Verwendung mehrerer Public Cloud-Anbieter
- **Community Cloud**: Gemeinsam genutzt von Organisationen mit gemeinsamen Anliegen

### Servicemodelle

#### Infrastructure as a Service (IaaS)
- **Bietet**: Virtuelle Maschinen, Speicher, Netzwerke, Betriebssysteme
- **Beispiele**: AWS EC2, Google Compute Engine, Azure VMs
- **Anwendungsfälle**: Lift-and-Shift-Migrationen, Entwicklungsumgebungen, hohe Kontrollanforderungen

#### Platform as a Service (PaaS)
- **Bietet**: Entwicklungsplattformen, Datenbanken, Middleware
- **Beispiele**: Heroku, Google App Engine, AWS Elastic Beanstalk
- **Anwendungsfälle**: Anwendungsentwicklung, API-Bereitstellung, Microservices

#### Software as a Service (SaaS)
- **Bietet**: Vollständige Anwendungen über das Internet
- **Beispiele**: Salesforce, Google Workspace, Microsoft 365, Slack
- **Anwendungsfälle**: E-Mail, CRM, Zusammenarbeit, Geschäftsanwendungen

#### Function as a Service (FaaS) / Serverless
- **Bietet**: Ereignisgesteuerte Funktionsausführung
- **Beispiele**: AWS Lambda, Azure Functions, Google Cloud Functions
- **Anwendungsfälle**: Ereignisverarbeitung, APIs, geplante Aufgaben, Echtzeitverarbeitung

## Wichtige Cloud-Anbieter

### Amazon Web Services (AWS)
- **Marktanteil**: ~32% (größter Anbieter)
- **Hauptdienste**:
  - Compute: EC2, Lambda, ECS, EKS
  - Storage: S3, EBS, Glacier
  - Datenbank: RDS, DynamoDB, Aurora
  - Networking: VPC, Route 53, CloudFront
  - KI/ML: SageMaker, Rekognition, Comprehend

### Microsoft Azure
- **Marktanteil**: ~23%
- **Stärken**: Enterprise-Integration, Hybrid-Cloud, Microsoft-Ökosystem
- **Hauptdienste**:
  - Compute: Virtual Machines, Azure Functions, AKS
  - Storage: Blob Storage, Disk Storage
  - Datenbank: SQL Datenbank, Cosmos DB
  - Networking: Virtual Network, Traffic Manager
  - KI/ML: Azure ML, Cognitive Services

### Google Cloud Platform (GCP)
- **Marktanteil**: ~10%
- **Stärken**: Datenanalyse, KI/ML, Kubernetes
- **Hauptdienste**:
  - Compute: Compute Engine, Cloud Functions, GKE
  - Storage: Cloud Storage, Persistent Disk
  - Datenbank: Cloud SQL, Firestore, Bigtable
  - Analytics: BigQuery, Dataflow, Pub/Sub
  - KI/ML: Vertex AI, AutoML

### Andere Anbieter
- **IBM Cloud**: Enterprise-Fokus, Watson AI
- **Oracle Cloud**: Datenbank-Workloads, Enterprise-Anwendungen
- **Alibaba Cloud**: Dominant im asiatisch-pazifischen Raum
- **DigitalOcean**: Entwicklerfreundlich, vereinfachte Angebote

## Cloud-Architekturmuster

### Prinzipien des Well-Architected Framework

#### Operative Exzellenz
- Operationen automatisieren
- Häufige, reversible Änderungen vornehmen
- Verfahren kontinuierlich verbessern
- Ausfälle antizipieren

#### Sicherheit
- Starke Identitätsgrundlage implementieren
- Nachverfolgbarkeit ermöglichen
- Sicherheit auf allen Ebenen anwenden
- Sicherheits-Best-Practices automatisieren
- Daten während der Übertragung und im Ruhezustand schützen

#### Zuverlässigkeit
- Wiederherstellungsverfahren testen
- Automatisch von Ausfällen erholen
- Horizontal für Verfügbarkeit skalieren
- Kapazität nicht schätzen
- Änderungen in der Automatisierung verwalten

#### Leistungseffizienz
- Fortschrittliche Technologien demokratisieren
- In Minuten global gehen
- Serverlose Architekturen verwenden
- Häufiger experimentieren
- Mechanische Sympathie berücksichtigen

#### Kostenoptimierung
- Verbrauchsmodell übernehmen
- Gesamteffizienz messen
- Kein Geld für undifferenzierte Arbeit ausgeben
- Ausgaben analysieren und zuordnen
- Verwaltete Dienste verwenden

### Häufige Architekturmuster

#### Microservices-Architektur
- Anwendungen in kleine, unabhängige Dienste zerlegen
- Jeder Dienst besitzt seine Daten und Logik
- Kommunikation über APIs (REST, gRPC, Messaging)
- Unabhängig bereitstellen
- **Vorteile**: Skalierbarkeit, Fehlerisolierung, Technologievielfalt
- **Herausforderungen**: Verteilte Komplexität, Datenkonsistenz, Monitoring

#### Ereignisgesteuerte Architektur
- Komponenten kommunizieren über Ereignisse
- Produzenten emittieren Ereignisse, Konsumenten reagieren
- **Muster**: Event Sourcing, CQRS, Pub/Sub
- **Technologien**: Kafka, SNS/SQS, EventBridge, Pub/Sub
- **Vorteile**: Lose Kopplung, Skalierbarkeit, Echtzeitverarbeitung

#### Serverlose Architektur
- Keine Serververwaltung erforderlich
- Bezahlung pro Ausführung
- Automatische Skalierung
- **Komponenten**: Funktionen, API Gateway, verwaltete Dienste
- **Vorteile**: Kosteneffizienz, reduzierte Operationen, schnelle Bereitstellung
- **Überlegungen**: Cold Starts, Vendor Lock-in, Ausführungslimits

#### Schichtenarchitektur (N-Tier)
- Präsentationsschicht (UI)
- Anwendungs-/Geschäftslogikschicht
- Datenzugriffsschicht
- Datenbankschicht
- **Vorteile**: Trennung der Belange, Wartbarkeit
- **Häufig**: 3-stufige Webanwendungen

#### Space-Based-Architektur
- Hohe Nebenläufigkeit mit verteilten Daten handhaben
- Virtualisierter Speicher über Server hinweg
- Verarbeitungsknoten skalieren unabhängig
- **Anwendungsfälle**: Hochvolumige, latenzarme Anwendungen

## Compute-Dienste

### Virtuelle Maschinen
- **Typen**: Allgemein, rechenoptimiert, speicheroptimiert, GPU
- **Preise**: On-Demand, reservierte Instanzen, Spot-Instanzen
- **Verwaltung**: Auto-Scaling-Gruppen, Load Balancer
- **Best Practices**: Right-Sizing, Tagging, Monitoring, Patching

### Container
- **Docker**: Container-Runtime-Standard
- **Orchestrierung**: Kubernetes (EKS, AKS, GKE), ECS, Fargate
- **Vorteile**: Portabilität, Effizienz, Konsistenz
- **Registry**: ECR, GCR, ACR, Docker Hub

### Serverlose Funktionen
- **Ausführungsmodell**: Ereignisgesteuert, zustandslos
- **Limits**: Ausführungszeit, Speicher, gleichzeitige Ausführungen
- **Anwendungsfälle**: APIs, Dateiverarbeitung, geplante Jobs, IoT-Backends
- **Monitoring**: Aufrufzählungen, Fehler, Dauer, Cold Starts

## Speicherlösungen

### Objektspeicher
- **Merkmale**: Flache Struktur, Metadaten, HTTP-Zugriff
- **Beispiele**: AWS S3, Google Cloud Storage, Azure Blob
- **Anwendungsfälle**: Statische Assets, Backups, Datenseen, Archive
- **Speicherklassen**: Hot, Cool, Cold, Archive (unterschiedliche Kosten/Zugriff)

### Blockspeicher
- **Merkmale**: Raw-Volumes, an VMs angehängt
- **Beispiele**: AWS EBS, Google Persistent Disk, Azure Disks
- **Anwendungsfälle**: Datenbanken, Boot-Volumes, hohe Leistungsanforderungen
- **Typen**: SSD, HDD, provisionierte IOPS

### Dateispeicher
- **Merkmale**: Gemeinsame Dateisysteme, NFS/SMB-Protokolle
- **Beispiele**: AWS EFS, Google Filestore, Azure Files
- **Anwendungsfälle**: Content-Management, gemeinsame Konfigurationen, Lift-and-Shift

### Archivespeicher
- **Merkmale**: Niedrigste Kosten, Abrufverzögerungen
- **Beispiele**: S3 Glacier, Azure Archive Storage
- **Anwendungsfälle**: Compliance, langfristige Backups, historische Daten

## Datenbankdienste

### Verwaltete relationale Datenbanken
- **Dienste**: AWS RDS/Aurora, Google Cloud SQL, Azure SQL Datenbank
- **Funktionen**: Automatisierte Backups, Patching, Skalierung, Replikation
- **Engines**: MySQL, PostgreSQL, MariaDB, Oracle, SQL Server

### NoSQL-Datenbanken
- **Dokument**: DocumentDB, Firestore, Cosmos DB
- **Key-Value**: DynamoDB, Redis Cache
- **Wide-Column**: Bigtable, Cassandra (verwaltet)
- **Graph**: Neptune, Cosmos DB (Graph-API)

### Data Warehousing
- **Dienste**: Snowflake, Redshift, BigQuery, Synapse
- **Merkmale**: Spaltenorientierter Speicher, MPP-Architektur
- **Anwendungsfälle**: Analytics, BI, groß angelegte Datenanalyse

### Caching-Dienste
- **In-Memory**: ElastiCache (Redis/Memcached), Cloud Memorystore
- **CDN-Caching**: CloudFront, Cloud CDN, Azure CDN
- **Anwendungsfälle**: Sitzungsspeicher, Abfrage-Caching, Content-Bereitstellung

## Netzwerke

### Virtuelle Netzwerke
- **VPC/VNet**: Isolierte Netzwerkumgebungen
- **Subnetze**: Öffentlich (internetzugänglich), privat (nur intern)
- **IP-Adressierung**: CIDR-Blöcke, IPv4/IPv6
- **Routentabellen**: Steuern des Datenverkehrsflusses

### Load Balancing
- **Typen**: Application (L7), Netzwerk (L4), Gateway
- **Funktionen**: Health Checks, SSL-Terminierung, Sticky Sessions
- **Dienste**: ELB/ALB/NLB, Cloud Load Balancing, Azure Load Balancer

### Content Delivery Networks (CDN)
- **Zweck**: Inhalte an Edge-Standorten cachen
- **Vorteile**: Reduzierte Latenz, geringere Origin-Last, globale Verteilung
- **Dienste**: CloudFront, Cloud CDN, Azure CDN, Akamai

### DNS-Dienste
- **Funktionen**: Domain-Registrierung, Routing, Health Checks
- **Dienste**: Route 53, Cloud DNS, Azure DNS
- **Routing-Richtlinien**: Einfach, gewichtet, latenzbasiert, Geolokation, Failover

### Konnektivitätsoptionen
- **Internet Gateway**: Öffentlicher Internetzugang
- **NAT Gateway**: Ausgehender Zugriff für private Subnetze
- **VPN**: Verschlüsselte Tunnel zu On-Premises
- **Direct Connect/ExpressRoute**: Dedizierte private Verbindungen
- **VPC Peering**: VPCs innerhalb/zwischen Konten verbinden

## Sicherheit in der Cloud

### Shared Responsibility Model
- **Anbieterverantwortung**: Sicherheit DER Cloud (Infrastruktur)
- **Kundenverantwortung**: Sicherheit IN der Cloud (Daten, Anwendungen, Zugriff)
- **Variiert nach Dienst**: Mehr verwaltet = mehr Anbieterverantwortung

### Identity and Access Management (IAM)
- **Benutzer**: Einzelne Identitäten
- **Gruppen**: Sammlungen von Benutzern
- **Rollen**: Temporäre Anmeldeinformationen für Dienste/Benutzer
- **Richtlinien**: JSON-Dokumente, die Berechtigungen definieren
- **Prinzipien**: Geringste Privilegien, Trennung der Aufgaben

### Netzwerksicherheit
- **Sicherheitsgruppen**: Stateful-Firewalls für Instanzen
- **Netzwerk-ACLs**: Stateless-Firewalls für Subnetze
- **Web Application Firewall (WAF)**: Schutz vor Web-Exploits
- **DDoS-Schutz**: Shield, Cloud Armor, DDoS Protection

### Datenschutz
- **Verschlüsselung im Ruhezustand**: KMS, kundenseitig verwaltete Schlüssel
- **Verschlüsselung während der Übertragung**: TLS/SSL, HTTPS
- **Schlüsselverwaltung**: HSM, Schlüsselrotation, Audit-Trails
- **Secrets-Verwaltung**: Secrets Manager, Key Vault

### Compliance und Governance
- **Zertifizierungen**: SOC 2, ISO 27001, HIPAA, PCI-DSS, GDPR
- **Tools**: Richtliniendurchsetzung, Compliance-Berichterstattung, Audit-Logs
- **Frameworks**: Cloud Sicherheit Alliance, NIST CSF

## DevOps in der Cloud

### CI/CD-Dienste
- **AWS**: CodePipeline, CodeBuild, CodeDeploy
- **Azure**: Azure DevOps, GitHub Actions
- **GCP**: Cloud Build, Cloud Deploy
- **Drittanbieter**: Jenkins, CircleCI, GitLab CI

### Infrastructure as Code (IaC)
- **Terraform**: Multi-Cloud, deklarativ, Statusverwaltung
- **CloudFormation**: AWS nativ, YAML/JSON-Vorlagen
- **ARM-Vorlagen**: Azure nativ
- **Deployment Manager**: GCP nativ
- **Pulumi**: Infrastruktur mit Programmiersprachen
- **Vorteile**: Versionskontrolle, Wiederholbarkeit, Dokumentation

### Konfigurationsverwaltung
- **Ansible**: Agentenlos, YAML-Playbooks
- **Chef**: Ruby-basiert, ausgereiftes Ökosystem
- **Puppet**: Deklarativ, starke Berichterstattung
- **SaltStack**: Schnell, Python-basiert

### Monitoring und Observability
- **Metriken**: CloudWatch, Cloud Monitoring, Azure Monitor
- **Logging**: CloudWatch Logs, Cloud Logging, Log Analytics
- **Tracing**: X-Ray, Cloud Trace, Application Insights
- **Dashboards**: CloudWatch Dashboards, Cloud Console
- **Alerting**: SNS, Cloud Monitoring-Warnungen, Action Groups

### Container-Orchestrierung
- **Kubernetes**: Industriestandard für Orchestrierung
- **Verwaltete Dienste**: EKS, AKS, GKE
- **Service Mesh**: Istio, Linkerd (Datenverkehrsverwaltung, Sicherheit)
- **GitOps**: ArgoCD, Flux (deklarative Bereitstellungen)

## Kostenverwaltung

### Preismodelle
- **Pay-as-you-go**: Bezahlung nach Nutzung
- **Reservierte Instanzen**: 1-3-Jahres-Verpflichtungen, erhebliche Rabatte
- **Spot-Instanzen**: Gebot für ungenutzte Kapazität, kann unterbrochen werden
- **Savings Plans**: Flexible Verpflichtungspreise
- **Free Tier**: Begrenzte kostenlose Nutzung für neue Konten

### Kostenoptimierungsstrategien
- **Right-Sizing**: Instanztypen an Workload-Anforderungen anpassen
- **Auto-Scaling**: Skalierung basierend auf Nachfrage
- **Reservierte Kapazität**: Verpflichtung für gleichmäßige Workloads
- **Spot-Nutzung**: Für fehlertolerante, flexible Workloads verwenden
- **Speicherebenen**: Selten genutzte Daten in günstigere Ebenen verschieben
- **Bereinigung**: Nicht verwendete Ressourcen, Snapshots, AMIs löschen

### Kostenverwaltungstools
- **AWS**: Cost Explorer, Budgets, Trusted Advisor
- **Azure**: Cost Management, Advisor
- **GCP**: Abrechnungsberichte, Recommender
- **Drittanbieter**: CloudHealth, CloudCheckr, Datadog

## Hochverfügbarkeit und Disaster Recovery

### Verfügbarkeitskonzepte
- **Availability Zones**: Physisch getrennte Rechenzentren innerhalb einer Region
- **Regionen**: Geografische Bereiche mit mehreren AZs
- **Edge Locations**: CDN-Cache-Standorte weltweit

### HA-Strategien
- **Multi-AZ**: Bereitstellung über Availability Zones hinweg
- **Auto-Healing**: Fehlgeschlagene Instanzen automatisch ersetzen
- **Load Balancing**: Datenverkehr auf gesunde Instanzen verteilen
- **Datenbank-Replikation**: Multi-AZ-Bereitstellungen, Lesereplikate

### Disaster Recovery-Strategien
- **Backup und Wiederherstellung**: Periodische Backups, bei Bedarf wiederherstellen (niedrigste Kosten)
- **Pilot Light**: Kernelemente laufen, während der Katastrophe hochskalieren
- **Warm Standby**: Verkleinerte Version läuft immer
- **Multi-Site Active/Active**: Vollständige Produktion in mehreren Regionen (höchste Kosten)

### RTO und RPO
- **Recovery Time Objective (RTO)**: Maximal akzeptable Ausfallzeit
- **Recovery Point Objective (RPO)**: Maximal akzeptabler Datenverlust
- **Strategieauswahl**: Basierend auf Geschäftsanforderungen und Budget

## Aufkommende Trends

### Edge Computing
- Daten näher an der Quelle verarbeiten
- **Dienste**: AWS Outposts, Wavelength, Azure Edge, Cloud CDN
- **Anwendungsfälle**: IoT, Echtzeit-Analytics, latenzarme Anwendungen

### Multi-Cloud und Hybrid Cloud
- Vendor Lock-in vermeiden
- Best-of-Breed-Dienste nutzen
- **Tools**: Terraform, Anthos, Arc, CloudHealth

### KI/ML-Dienste
- Vorgefertigte Modelle: Vision, Sprache, Sprachverarbeitung
- Benutzerdefiniertes Modelltraining: SageMaker, Vertex AI, Azure ML
- MLOps: Modellbereitstellung, Monitoring, Governance

### Quantencomputing
- **Dienste**: AWS Braket, Azure Quantum
- **Status**: Frühphase, experimentell
- **Potenzial**: Kryptographie, Optimierung, Arzneimittelentwicklung

### Nachhaltige Cloud
- CO2-Fußabdruck-Tracking
- Verpflichtungen zu erneuerbaren Energien
- Effiziente Ressourcennutzung
- Green Architecture-Muster
