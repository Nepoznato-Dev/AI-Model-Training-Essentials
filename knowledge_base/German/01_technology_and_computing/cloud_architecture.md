# Cloud-Architektur

## Grundlagen des Cloud Computing

### Was ist Cloud Computing?
Bedarfsgerechte Bereitstellung von Rechenressourcen (Server, Speicher, Datenbanken, Netzwerke, Software) über das Internet mit nutzungsbasierter Bezahlung.

### Wesentliche Merkmale (NIST-Definition)
- **On-Demand Self-Service**: Ressourcen ohne menschliche Interaktion bereitstellen
- **Broad Network Access**: Über das Netzwerk über Standardmechanismen verfügbar
- **Resource Pooling**: Multi-Tenant-Modell mit dynamischer Zuweisung
- **Rapid Elasticity**: Schnell nach außen und innen skalieren
- **Measured Service**: Ressourcennutzung wird überwacht und abgerechnet

### Cloud-Bereitstellungsmodelle
- **Public Cloud**: Im Besitz von Anbietern, gemeinsam genutzte Infrastruktur (AWS, Azure, GCP)
- **Private Cloud**: Für eine einzelne Organisation dediziert (On-Premises oder gehostet)
- **Hybrid Cloud**: Kombination aus Public und Private Cloud
- **Multi-Cloud**: Nutzung mehrerer Public-Cloud-Anbieter
- **Community Cloud**: Von Organisationen mit gemeinsamen Anforderungen geteilt

### Servicemodelle

#### Infrastructure as a Service (IaaS)
- **Bietet**: Virtuelle Maschinen, Speicher, Netzwerke, Betriebssysteme
- **Beispiele**: AWS EC2, Google Compute Engine, Azure VMs
- **Anwendungsfälle**: Lift-and-Shift-Migrationen, Entwicklungsumgebungen, Bedarf an hoher Kontrolle

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
- **Wichtige Services**:
  - Compute: EC2, Lambda, ECS, EKS
  - Storage: S3, EBS, Glacier
  - Database: RDS, DynamoDB, Aurora
  - Networking: VPC, Route 53, CloudFront
  - AI/ML: SageMaker, Rekognition, Comprehend

### Microsoft Azure
- **Marktanteil**: ~23%
- **Stärken**: Unternehmensintegration, Hybrid Cloud, Microsoft-Ökosystem
- **Wichtige Services**:
  - Compute: Virtual Machines, Azure Functions, AKS
  - Storage: Blob Storage, Disk Storage
  - Database: SQL Database, Cosmos DB
  - Networking: Virtual Network, Traffic Manager
  - AI/ML: Azure ML, Cognitive Services

### Google Cloud Platform (GCP)
- **Marktanteil**: ~10%
- **Stärken**: Datenanalyse, AI/ML, Kubernetes
- **Wichtige Services**:
  - Compute: Compute Engine, Cloud Functions, GKE
  - Storage: Cloud Storage, Persistent Disk
  - Database: Cloud SQL, Firestore, Bigtable
  - Analytics: BigQuery, Dataflow, Pub/Sub
  - AI/ML: Vertex AI, AutoML

### Weitere Anbieter
- **IBM Cloud**: Unternehmensfokus, Watson AI
- **Oracle Cloud**: Datenbank-Workloads, Unternehmensanwendungen
- **Alibaba Cloud**: Führend im asiatisch-pazifischen Raum
- **DigitalOcean**: Entwicklerfreundlich, vereinfachtes Angebot

## Cloud-Architekturmuster

### Prinzipien von Well-Architected Frameworks

#### Operative Exzellenz
- Abläufe automatisieren
- Häufige, reversible Änderungen vornehmen
- Verfahren kontinuierlich verfeinern
- Mit Ausfällen rechnen

#### Sicherheit
- Starke Identitätsgrundlage umsetzen
- Nachvollziehbarkeit ermöglichen
- Sicherheit auf allen Ebenen anwenden
- Sicherheits-Best-Practices automatisieren
- Daten bei Übertragung und Speicherung schützen

#### Zuverlässigkeit
- Wiederherstellungsverfahren testen
- Sich automatisch von Fehlern erholen
- Horizontal für Verfügbarkeit skalieren
- Nicht länger Kapazitäten schätzen
- Änderungen in der Automatisierung verwalten

#### Performance-Effizienz
- Fortgeschrittene Technologien demokratisieren
- In Minuten global gehen
- Serverless-Architekturen nutzen
- Häufiger experimentieren
- Mechanische Sympathie berücksichtigen

#### Kostenoptimierung
- Verbrauchsmodell übernehmen
- Gesamteffizienz messen
- Kein Geld für undifferenzierte Arbeit ausgeben
- Ausgaben analysieren und zuordnen
- Verwaltete Dienste nutzen

### Häufige Architekturmuster

#### Microservices-Architektur
- Anwendungen in kleine, unabhängige Services zerlegen
- Jeder Service besitzt seine Daten und Logik
- Kommunikation über APIs (REST, gRPC, Messaging)
- Unabhängig bereitstellen
- **Vorteile**: Skalierbarkeit, Fehlerisolation, Technologiediversität
- **Herausforderungen**: Verteilte Komplexität, Datenkonsistenz, Monitoring

#### Ereignisgesteuerte Architektur
- Komponenten kommunizieren über Ereignisse
- Produzenten senden Ereignisse aus, Konsumenten reagieren
- **Muster**: Event Sourcing, CQRS, Pub/Sub
- **Technologien**: Kafka, SNS/SQS, EventBridge, Pub/Sub
- **Vorteile**: Lose Kopplung, Skalierbarkeit, Echtzeitverarbeitung

#### Serverless-Architektur
- Kein Server-Management erforderlich
- Bezahlung pro Ausführung
- Automatische Skalierung
- **Komponenten**: Functions, API Gateway, verwaltete Dienste
- **Vorteile**: Kosteneffizienz, weniger Betriebsaufwand, schnelle Bereitstellung
- **Zu beachten**: Cold Starts, Vendor Lock-in, Ausführungsgrenzen

#### Schichtenarchitektur (N-Tier)
- Präsentationsschicht (UI)
- Anwendungs-/Geschäftslogikschicht
- Datenzugriffsschicht
- Datenbankschicht
- **Vorteile**: Trennung von Zuständigkeiten, Wartbarkeit
- **Häufig**: 3-Tier-Webanwendungen

#### Space-Based Architecture
- Hohe Parallelität mit verteilten Daten bewältigen
- Virtualisierter Speicher über Server hinweg
- Verarbeitungsknoten skalieren unabhängig
- **Anwendungsfälle**: Anwendungen mit hohem Volumen und geringer Latenz

## Compute-Services

### Virtuelle Maschinen
- **Typen**: Allgemeinzweck, rechenoptimiert, speicheroptimiert, GPU
- **Preise**: On-Demand, Reserved Instances, Spot Instances
- **Verwaltung**: Auto-Scaling-Gruppen, Load Balancer
- **Best Practices**: Richtig dimensionieren, taggen, überwachen, patchen

### Container
- **Docker**: Standard für Container-Runtime
- **Orchestrierung**: Kubernetes (EKS, AKS, GKE), ECS, Fargate
- **Vorteile**: Portabilität, Effizienz, Konsistenz
- **Registry**: ECR, GCR, ACR, Docker Hub

### Serverless Functions
- **Ausführungsmodell**: Ereignisgesteuert, zustandslos
- **Grenzen**: Ausführungszeit, Speicher, gleichzeitige Ausführungen
- **Anwendungsfälle**: APIs, Dateiverarbeitung, geplante Jobs, IoT-Backends
- **Monitoring**: Aufrufzahlen, Fehler, Dauer, Cold Starts

## Speicherlösungen

### Objektspeicher
- **Eigenschaften**: Flache Struktur, Metadaten, HTTP-Zugriff
- **Beispiele**: AWS S3, Google Cloud Storage, Azure Blob
- **Anwendungsfälle**: Statische Assets, Backups, Data Lakes, Archive
- **Speicherklassen**: Hot, Cool, Cold, Archive (unterschiedliche Kosten/Zugriffe)

### Blockspeicher
- **Eigenschaften**: Roh-Volumes, an VMs angebunden
- **Beispiele**: AWS EBS, Google Persistent Disk, Azure Disks
- **Anwendungsfälle**: Datenbanken, Boot-Volumes, Anforderungen an hohe Leistung
- **Typen**: SSD, HDD, bereitgestellte IOPS

### Dateispeicher
- **Eigenschaften**: Gemeinsame Dateisysteme, NFS/SMB-Protokolle
- **Beispiele**: AWS EFS, Google Filestore, Azure Files
- **Anwendungsfälle**: Content-Management, geteilte Konfigurationen, Lift-and-Shift

### Archivspeicher
- **Eigenschaften**: Niedrigste Kosten, verzögerte Wiederherstellung
- **Beispiele**: S3 Glacier, Azure Archive Storage
- **Anwendungsfälle**: Compliance, langfristige Backups, historische Daten

## Datenbankdienste

### Verwaltete relationale Datenbanken
- **Services**: AWS RDS/Aurora, Google Cloud SQL, Azure SQL Database
- **Funktionen**: Automatische Backups, Patching, Skalierung, Replikation
- **Engines**: MySQL, PostgreSQL, MariaDB, Oracle, SQL Server

### NoSQL-Datenbanken
- **Document**: DocumentDB, Firestore, Cosmos DB
- **Key-Value**: DynamoDB, Redis Cache
- **Wide-Column**: Bigtable, Cassandra (managed)
- **Graph**: Neptune, Cosmos DB (graph API)

### Data Warehousing
- **Services**: Snowflake, Redshift, BigQuery, Synapse
- **Eigenschaften**: Spaltenorientierte Speicherung, MPP-Architektur
- **Anwendungsfälle**: Analytik, BI, groß angelegte Datenanalyse

### Caching-Services
- **In-Memory**: ElastiCache (Redis/Memcached), Cloud Memorystore
- **CDN-Caching**: CloudFront, Cloud CDN, Azure CDN
- **Anwendungsfälle**: Session-Speicherung, Query-Caching, Content-Auslieferung

## Netzwerke

### Virtuelle Netzwerke
- **VPC/VNet**: Isolierte Netzwerkumgebungen
- **Subnets**: Öffentlich (internetseitig), privat (nur intern)
- **IP-Adressierung**: CIDR-Blöcke, IPv4/IPv6
- **Route Tables**: Steuern den Datenverkehrsfluss

### Lastverteilung
- **Typen**: Application (L7), Network (L4), Gateway
- **Funktionen**: Health Checks, SSL-Terminierung, Sticky Sessions
- **Services**: ELB/ALB/NLB, Cloud Load Balancing, Azure Load Balancer

### Content Delivery Networks (CDN)
- **Zweck**: Inhalte an Edge-Standorten zwischenspeichern
- **Vorteile**: Geringere Latenz, weniger Last auf dem Origin, globale Verteilung
- **Services**: CloudFront, Cloud CDN, Azure CDN, Akamai

### DNS-Services
- **Funktionen**: Domain-Registrierung, Routing, Health Checks
- **Services**: Route 53, Cloud DNS, Azure DNS
- **Routing-Richtlinien**: Simple, Weighted, Latency-Based, Geolocation, Failover

### Konnektivitätsoptionen
- **Internet Gateway**: Öffentlicher Internetzugang
- **NAT Gateway**: Ausgehender Zugriff für private Subnets
- **VPN**: Verschlüsselte Tunnel zu On-Premises
- **Direct Connect/ExpressRoute**: Dedizierte private Verbindungen
- **VPC Peering**: Verbindung von VPCs innerhalb/zwischen Accounts

## Sicherheit in der Cloud

### Modell der geteilten Verantwortung
- **Verantwortung des Anbieters**: Sicherheit DER Cloud (Infrastruktur)
- **Verantwortung des Kunden**: Sicherheit IN der Cloud (Daten, Anwendungen, Zugriff)
- **Variiert je nach Service**: Mehr managed = mehr Verantwortung des Anbieters

### Identity and Access Management (IAM)
- **Users**: Einzelne Identitäten
- **Groups**: Sammlungen von Benutzern
- **Roles**: Temporäre Anmeldedaten für Services/Benutzer
- **Policies**: JSON-Dokumente zur Definition von Berechtigungen
- **Prinzipien**: Least Privilege, Trennung von Zuständigkeiten

### Netzwerksicherheit
- **Security Groups**: Zustandsbehaftete Firewalls für Instanzen
- **Network ACLs**: Zustandslose Firewalls für Subnets
- **Web Application Firewall (WAF)**: Schutz vor Web-Exploits
- **DDoS Protection**: Shield, Cloud Armor, DDoS Protection

### Datenschutz
- **Encryption at Rest**: KMS, kundenseitig verwaltete Schlüssel
- **Encryption in Transit**: TLS/SSL, HTTPS
- **Key Management**: HSM, Schlüsselrotation, Audit Trails
- **Secrets Management**: Secrets Manager, Key Vault

### Compliance und Governance
- **Zertifizierungen**: SOC 2, ISO 27001, HIPAA, PCI-DSS, GDPR
- **Werkzeuge**: Richtliniendurchsetzung, Compliance-Berichte, Audit-Logs
- **Frameworks**: Cloud Security Alliance, NIST CSF

## DevOps in der Cloud

### CI/CD-Services
- **AWS**: CodePipeline, CodeBuild, CodeDeploy
- **Azure**: Azure DevOps, GitHub Actions
- **GCP**: Cloud Build, Cloud Deploy
- **Drittanbieter**: Jenkins, CircleCI, GitLab CI

### Infrastructure as Code (IaC)
- **Terraform**: Multi-Cloud, deklarativ, State-Management
- **CloudFormation**: AWS-nativ, YAML/JSON-Vorlagen
- **ARM Templates**: Azure-nativ
- **Deployment Manager**: GCP-nativ
- **Pulumi**: Infrastruktur mit Programmiersprachen
- **Vorteile**: Versionskontrolle, Wiederholbarkeit, Dokumentation

### Konfigurationsmanagement
- **Ansible**: Agentenlos, YAML-Playbooks
- **Chef**: Ruby-basiert, ausgereiftes Ökosystem
- **Puppet**: Deklarativ, starkes Reporting
- **SaltStack**: Schnell, Python-basiert

### Monitoring und Observability
- **Metriken**: CloudWatch, Cloud Monitoring, Azure Monitor
- **Logging**: CloudWatch Logs, Cloud Logging, Log Analytics
- **Tracing**: X-Ray, Cloud Trace, Application Insights
- **Dashboards**: CloudWatch Dashboards, Cloud Console
- **Alerting**: SNS, Cloud-Monitoring-Benachrichtigungen, Action Groups

### Container-Orchestrierung
- **Kubernetes**: Industriestandard für Orchestrierung
- **Managed Services**: EKS, AKS, GKE
- **Service Mesh**: Istio, Linkerd (Traffic-Management, Sicherheit)
- **GitOps**: ArgoCD, Flux (deklarative Deployments)

## Kostenmanagement

### Preismodelle
- **Pay-as-you-go**: Bezahle nur, was du nutzt
- **Reserved Instances**: 1-3 Jahre Bindung, deutliche Rabatte
- **Spot Instances**: Auf ungenutzte Kapazität bieten, kann unterbrochen werden
- **Savings Plans**: Flexible Preismodelle mit Verpflichtung
- **Free Tier**: Begrenzte kostenlose Nutzung für neue Accounts

### Strategien zur Kostenoptimierung
- **Right-Sizing**: Instanztypen an Workload-Anforderungen anpassen
- **Auto-Scaling**: Nach Bedarf skalieren
- **Reserved Capacity**: Für stabile Dauerlasten fest zusagen
- **Spot Usage**: Für fehlertolerante, flexible Workloads nutzen
- **Storage Tiers**: Selten genutzte Daten in günstigere Klassen verschieben
- **Cleanup**: Ungenutzte Ressourcen, Snapshots, AMIs löschen

### Werkzeuge für Kostenmanagement
- **AWS**: Cost Explorer, Budgets, Trusted Advisor
- **Azure**: Cost Management, Advisor
- **GCP**: Billing-Berichte, Recommender
- **Drittanbieter**: CloudHealth, CloudCheckr, Datadog

## Hochverfügbarkeit und Disaster Recovery

### Verfügbarkeitskonzepte
- **Availability Zones**: Physisch getrennte Rechenzentren innerhalb einer Region
- **Regions**: Geografische Gebiete mit mehreren AZs
- **Edge Locations**: CDN-Cache-Standorte weltweit

### HA-Strategien
- **Multi-AZ**: Über Availability Zones hinweg bereitstellen
- **Auto-Healing**: Fehlgeschlagene Instanzen automatisch ersetzen
- **Load Balancing**: Datenverkehr auf gesunde Instanzen verteilen
- **Database Replication**: Multi-AZ-Deployments, Read Replicas

### Strategien für Disaster Recovery
- **Backup and Restore**: Regelmäßige Backups, Wiederherstellung bei Bedarf (niedrigste Kosten)
- **Pilot Light**: Kernkomponenten laufen, bei Disaster hochskalieren
- **Warm Standby**: Herunterskalierte Version läuft dauerhaft
- **Multi-Site Active/Active**: Vollständige Produktion in mehreren Regionen (höchste Kosten)

### RTO und RPO
- **Recovery Time Objective (RTO)**: Maximal akzeptable Ausfallzeit
- **Recovery Point Objective (RPO)**: Maximal akzeptabler Datenverlust
- **Strategiewahl**: Basierend auf Geschäftsanforderungen und Budget

## Neue Trends

### Edge Computing
- Daten näher an der Quelle verarbeiten
- **Services**: AWS Outposts, Wavelength, Azure Edge, Cloud CDN
- **Anwendungsfälle**: IoT, Echtzeitanalytik, Anwendungen mit niedriger Latenz

### Multi-Cloud und Hybrid Cloud
- Vendor Lock-in vermeiden
- Best-of-Breed-Services nutzen
- **Tools**: Terraform, Anthos, Arc, CloudHealth

### AI/ML-Services
- Vortrainierte Modelle: Vision, Sprache, Text
- Benutzerdefiniertes Modelltraining: SageMaker, Vertex AI, Azure ML
- MLOps: Modellbereitstellung, Monitoring, Governance

### Quantencomputing
- **Services**: AWS Braket, Azure Quantum
- **Status**: Frühe Phase, experimentell
- **Potenzial**: Kryptografie, Optimierung, Wirkstoffforschung

### Nachhaltige Cloud
- Nachverfolgung des CO2-Fußabdrucks
- Verpflichtungen zu erneuerbaren Energien
- Effiziente Ressourcennutzung
- Grüne Architekturmuster
