---
# Metadata
title: "Cloud Services Comparison"
description: "AWS vs Azure vs GCP side-by-side comparison"
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
tags: [cloud, services, comparison, quick-reference]
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
# Cloud-Services-Vergleich
Ein direkter Vergleich der drei großen Cloud-Anbieter – AWS, Azure und Google Cloud – in den Bereichen Rechenleistung, Speicher, Datenbanken, KI/ML, Netzwerk, Überwachung und Infrastruktur als Code. Nützlich für Architekten, die entscheiden, welche Plattform sie verwenden möchten, oder Dienste von einer Cloud in eine andere zuordnen.
---

## Anbieterübersicht
| | AWS | Azure | Google Cloud (GCP) |
|---|-----|-------|-------|
| **Marktanteil** | ~31 % (am größten) | ~25 % (Sekunde) | ~11 % (Dritter, am schnellsten wachsend) |
| **Stärken** | Breite der Dienstleistungen; Reife; Ökosystem | Unternehmensintegration; Hybrid-Cloud; Microsoft-Stack | Daten/KI; Kubernetes; globales Netzwerk |
| **Am besten für** | Startups zu Unternehmen; Umfangreichster Leistungskatalog | Unternehmen mit Microsoft/Active Directory; Hybrid | Datenintensive Arbeitslasten; Kubernetes-nativ; KI/ML |
| **Regionen** | 33 Regionen, 105 AZs | 60+ Regionen | Über 40 Regionen, über 100 Zonen |
| **Kostenloses Kontingent** | 12 Monate kostenloses Kontingent + immer kostenlos | 12 Monate kostenlos + 200 $ Guthaben | 300 $ Guthaben für 90 Tage + immer kostenlos |
---

## Berechnen
| Servicekategorie | AWS | Azure | GCP |
|-----------------|-----|-------|-----|
| **Virtuelle Maschinen** | EC2 (Elastic Compute Cloud) | Virtuelle Maschinen | Compute Engine |
| **Automatische Skalierung** | Auto Scaling-Gruppen | VM-Skalierungsgruppen | Instanzgruppen |
| **Serverlose Funktionen** | Lambda | Azure-Funktionen | Cloud-Funktionen |
| **Container-Registrierung** | ECR (Elastic Container Registry) | Azure Container Registry | Artefaktregister |
| **Container-Orchestrierung** | ECS / EKS | ACS / AKS | GKE/Cloud Run |
| **Serverlose Container** | Fargate | Container-Apps | Cloud Run |
| **App-Plattform (PaaS)** | Elastic Beanstalk, App Runner | App-Service | App Engine |
| **Stapelverarbeitung** | AWS Batch | Azure Batch | Cloud-Batch |
| **GPU/KI-Computing** | EC2 (P4d-, P5-Instanzen) | VMs der NC/ND-Serie | A2/A3-VMs; TPUs |
### VM-Preismodelle
| Modell | AWS | Azure | GCP |
|-------|-----|-------|-----|
| **Auf Anfrage** | On-Demand-Instanzen | Pay-as-you-go | Auf Anfrage |
| **Reserviert / Zugesagt** | Reservierte Instanzen (1–3 Jahre) | Reservierte VMs (1–3 Jahre) | Rabatte für zugesicherte Nutzung (1–3 Jahre) |
| **Spontan / unterbrechbar** | Spot-Instanzen | Spot-VMs | Präemptive/Spot-VMs |
| **Sparpläne** | Sparpläne | Sparpläne | Rabatte für zugesicherte Nutzung |
---

## Lagerung
| Servicekategorie | AWS | Azure | GCP |
|-----------------|-----|-------|-----|
| **Objektspeicher** | S3 | Blob-Speicher | Cloud-Speicher |
| **Blockspeicher** | EBS | Verwaltete Datenträger | Persistente Festplatte |
| **Dateispeicherung** | EFS, FSx | Azure-Dateien | Dateispeicher |
| **Archiv / Kalt** | S3 Glacier, Deep Archive | Blob Cool/Archive-Ebenen | Cloud Storage Coldline/Archiv |
| **Datenübertragung** | Schneeball, DataSync | Datenbox | Übertragungsgerät |
### Vergleich der Speicherklassen
| Anwendungsfall | AWS S3 | Azure-Blob | GCP-Cloud-Speicher |
|----------|--------|------------|-----|
| **Häufiger Zugriff** | S3-Standard | Heiß | Standard |
| **Seltener Zugriff** | S3 Standard-IA | Cool | Nearline |
| **Seltener Zugang** | S3 One Zone-IA | — | Coldline |
| **Archiv** | S3 Glacier / Deep Archive | Archiv | Archiv |
---

## Datenbanken
| Servicekategorie | AWS | Azure | GCP |
|-----------------|-----|-------|-----|
| **Relational (verwaltet)** | RDS (MySQL, PostgreSQL, Oracle, SQL Server) | Azure-Datenbank (MySQL, PostgreSQL); Azure SQL | Cloud SQL (MySQL, PostgreSQL) |
| **Relational (cloudnativ)** | Aurora (MySQL/PostgreSQL-kompatibel) | Azure SQL-Datenbank (elastische Pools) | Cloud Spanner (global verteilt) |
| **NoSQL (Dokument)** | DynamoDB | Cosmos DB (MongoDB-API, SQL-API) | Feuerspeicher; Datenspeicher |
| **NoSQL (breite Spalte)** | DynamoDB (auch) | Cosmos DB (Cassandra-API) | Bigtable |
| **NoSQL (Schlüsselwert)** | DynamoDB, ElastiCache | Azure Cache für Redis | Speicherspeicher (Redis) |
| **Grafik** | Neptun | Cosmos DB (Gremlin-API) | — |
| **Zeitreihe** | Zeitstrom | Azure Data Explorer | — |
| **Hauptbuch** | QLDB | Azure Confidential Ledger | — |
| **In-Memory-Cache** | ElastiCache (Redis, Memcached) | Azure Cache für Redis | Speicher |
| **Suchen** | OpenSearch-Dienst | Azure AI-Suche | Cloud-Suche; Vertex AI-Suche |
| **Data Warehouse** | Rotverschiebung | Synapse-Analyse | BigQuery |
---

## KI und maschinelles Lernen
| Servicekategorie | AWS | Azure | GCP |
|-----------------|-----|-------|-----|
| **ML-Plattform** | SageMaker | Azure Machine Learning | Vertex-KI |
| **Vorab trainierte APIs** | Erkennen (Vision), Polly (TTS), Verstehen (NLP), Transkribieren | Kognitive Dienste (Vision, Sprache, Sprache, Entscheidung) | Vision AI, Speech-to-Text, Natural Language API |
| **LLM / Generative KI** | Grundgestein (Claude, Lama, Titan) | Azure OpenAI-Dienst (GPT-4, DALL-E) | Vertex AI (Zwillinge); Modellgarten |
| **Vektor / Einbettungen** | OpenSearch (k-NN), Bedrock Knowledge Bases | Azure AI Search (Vektor) | Vertex AI-Vektorsuche, AlloyDB |
| **MLOps** | SageMaker Pipelines, Modellregistrierung | Azure ML Pipelines, Modellregistrierung | Vertex AI Pipelines, Modellregistrierung |
| **Datenkennzeichnung** | SageMaker Ground Truth | Azure ML-Datenkennzeichnung | Vertex AI-Datenkennzeichnung |
| **Konversations-KI** | Lex | Azure Bot-Dienst | Dialogflow CX / ES |
| **Übersetzung** | Übersetzen | Übersetzer | Übersetzungs-API |
---

## Vernetzung
| Servicekategorie | AWS | Azure | GCP |
|-----------------|-----|-------|-----|
| **Virtuelles Netzwerk** | VPC | Virtuelles Netzwerk (VNet) | VPC |
| **Lastausgleich** | ELB/ALB/NLB/CLB | Load Balancer (Anwendung, Netzwerk, Gateway) | Cloud-Lastenausgleich |
| **DNS** | Route 53 | Azure DNS | Cloud-DNS |
| **CDN** | CloudFront | Azure-Haustür | Cloud-CDN |
| **API-Gateway** | API-Gateway | API-Management | API-Gateway |
| **VPN** | Site-to-Site-VPN, Client-VPN | VPN-Gateway | Cloud-VPN |
| **Direct Connect / ExpressRoute** | Direktverbindung | ExpressRoute | Cloud-Verbindung |
| **Privater Link** | PrivateLink, VPC-Endpunkte | Private Link, private Endpunkte | Private Service Connect |
| **Firewall** | WAF, Netzwerk-Firewall | Azure Firewall, WAF | Cloud Armor, Firewall |
| **DDoS-Schutz** | Schild Standard/Erweitert | DDoS-Schutz | Wolkenrüstung |
---

## Überwachung und Protokollierung
| Servicekategorie | AWS | Azure | GCP |
|-----------------|-----|-------|-----|
| **Metriken/Überwachung** | CloudWatch | Azure Monitor | Cloud-Überwachung (Stackdriver) |
| **Protokollierung** | CloudWatch-Protokolle | Log Analytics (Azure Monitor-Protokolle) | Cloud-Protokollierung |
| **Nachverfolgung** | Röntgen | Anwendungseinblicke | Cloud Trace |
| **Alarmierung** | CloudWatch-Alarme | Azure Monitor-Warnungen | Cloud-Überwachungswarnungen |
| **Dashboards** | CloudWatch-Dashboards | Azure-Arbeitsmappen/Dashboards | Cloud-Überwachungs-Dashboards |
| **Fehlerverfolgung** | CloudWatch Synthetics | Anwendungseinblicke | Cloud-Fehlerberichterstattung |
| **Drittanbieter** | Datadog, New Relic, PagerDuty | Datadog, New Relic, PagerDuty | Datadog, New Relic, PagerDuty |
---

## Infrastruktur als Code und DevOps
| Servicekategorie | AWS | Azure | GCP |
|-----------------|-----|-------|-----|
| **IaC (nativ)** | CloudFormation | ARM-Vorlagen / Bizeps | Bereitstellungsmanager / Pulumi |
| **IaC (cloudübergreifend)** | Terraform, Pulumi, CDK | Terraform, Pulumi, Bizeps | Terraform, Pulumi |
| **CI/CD** | CodePipeline, CodeBuild | Azure DevOps, GitHub-Aktionen | Cloud-Build; Cloud-Bereitstellung |
| **Container-Registrierung** | ECR | Azure Container Registry | Artefaktregister |
| **GitOps** | App Mesh + Flux/ArgoCD | Flux/ArgoCD auf AKS | Konfigurationssynchronisierung (Anthos) |
| **Geheimnisverwaltung** | Secrets Manager, SSM-Parameterspeicher | Schlüsseltresor | Geheimmanager |
---

## Preisüberlegungen
| Faktor | AWS | Azure | GCP |
|--------|-----|-------|-----|
| **Abrechnungsgranularität** | Pro Sekunde (bei einigen nach der ersten Stunde) | Pro Sekunde | Pro Sekunde |
| **Rabatte für kontinuierliche Nutzung** | Reservierte Instanzen / Sparpläne | Reservierte VMs | Rabatte für zugesicherte Nutzung |
| **Spot-Instanzen** | Bis zu 90 % Rabatt | Bis zu 90 % Rabatt | Bis zu 91 % Rabatt |
| **Datenausgang** | Aufgeladen (teuer) | Aufgeladen | Gleicher Preis unabhängig vom Zielort (oft günstiger) |
| **Kostenloses Kontingent** | 12 Monate + immer kostenlos | 12 Monate + 200 $ Guthaben | 300 $ für 90 Tage + immer kostenlos |
| **Unternehmensrabatte** | Enterprise Discount Program (EDP) | MACC (Monetary Commitment Contract) | Zugesicherte Nutzung + CUDs |
---

## Wann welche zu verwenden ist
| Szenario | Empfohlen | Warum |
|----------|-------------|-----|
| **Größte Serviceauswahl; ausgereiftes Ökosystem** | AWS | Größter Katalog; die meisten Integrationen von Drittanbietern |
| **Microsoft Enterprise; Active Directory; Hybrid** | Azure | Native AD-Integration; starke Hybridwerkzeuge |
| **Data Warehousing; BigQuery; Analyselastig** | GCP | BigQuery ist das Beste seiner Klasse; nahtlose Datenintegration |
| **Kubernetes-native Entwicklung** | GCP | GKE ist das ausgefeilteste verwaltete Kubernetes |
| **Generative KI/LLM-Anwendungen** | Azure oder GCP | Azure OpenAI für GPT-Modelle; Vertex AI für Zwillinge |
| **Globale Anwendungen mit geringer Latenz** | GCP | Das globale Netzwerk von Google ist ein echter Vorteil |
| **Regierungs-/Compliance-intensive Arbeitsbelastung** | AWS oder Azure | Die meisten Compliance-Zertifizierungen; GovCloud-Regionen |
| **Kostensensitive Startups** | GCP oder AWS | Das kostenlose Kontingent von GCP ist großzügig; AWS verfügt über Startguthaben |
| **Vorhandener Microsoft/.NET-Stack** | Azure | Enge Integration mit Visual Studio, .NET, Office 365 |
| **Multi-Cloud-Strategie** | Terraform + alle drei | Verwenden Sie Terraform, um Ressourcen cloudübergreifend zu verwalten |
---

## Zusammenfassung
Alle drei Clouds sind leistungsfähig, zuverlässig und werden ständig erweitert. Bei der Wahl kommt es in der Regel darauf an, was Ihr Team bereits weiß, wie Ihre bestehenden Verträge aussehen und welche spezifischen Dienstleistungen für Ihr Arbeitspensum wichtig sind. Multi-Cloud wird immer häufiger eingesetzt – verwenden Sie Terraform oder Pulumi, um eine Anbieterbindung auf der Infrastrukturebene zu vermeiden, und wählen Sie jede Cloud nach dem aus, was sie am besten kann.