<!--
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

-->
# Confronto dei servizi cloud
Un confronto fianco a fianco dei tre principali fornitori di servizi cloud (AWS, Azure e Google Cloud) tra elaborazione, archiviazione, database, AI/ML, rete, monitoraggio e infrastruttura come codice. Utile per gli architetti che devono decidere quale piattaforma utilizzare o mappare i servizi da un cloud all'altro.
---

## Panoramica del fornitore
| | AWS | Azzurro | Google Cloud (GCP) |
|---|-----|-------|---------------------|
| **Quota di mercato** | ~31% (maggiore) | ~25% (secondo) | ~11% (terzo, in più rapida crescita) |
| **Punti di forza** | Ampiezza dei servizi; scadenza; ecosistema | Integrazione aziendale; cloud ibrido; Pila Microsoft | Dati/AI; Kubernetes; rete globale |
| **Ideale per** | Startup alle imprese; il più ampio catalogo di servizi | Aziende con Microsoft/Active Directory; ibrido | Carichi di lavoro ad alta intensità di dati; Nativo di Kubernetes; AI/ML |
| **Regioni** | 33 regioni, 105 AZ | 60+ regioni | Oltre 40 regioni, oltre 100 zone |
| **Livello gratuito** | 12 mesi di livello gratuito + sempre gratuito | 12 mesi gratuiti + credito di $ 200 | Credito di $ 300 per 90 giorni + sempre gratuito |
---

## Calcola
| Categoria di servizio | AWS | Azzurro | PCG |
|-----------------|-----|-------|-----|
| **Macchine virtuali** | EC2 (Elastic Compute Cloud) | Macchine virtuali | Motore di calcolo |
| **Ridimensionamento automatico** | Gruppi di ridimensionamento automatico | Set di scalabilità di macchine virtuali | Gruppi di istanze |
| **Funzioni serverless** | Lambda | Funzioni di Azure | Funzioni cloud |
| **Registro dei contenitori** | ECR (Registro dei contenitori elastici) | Registro contenitori di Azure | Registro degli artefatti |
| **Orchestrazione dei contenitori** | ECS / EKS | ACS/AKS | GKE/Cloud Run |
| **Contenitori serverless** | Fargate | App contenitore | Corsa sulle nuvole |
| **Piattaforma app (PaaS)** | Elastic Beanstalk, App Runner | Servizio app | Motore dell'app |
| **Elaborazione batch** | Lotto AWS | Lotto azzurro | Lotto cloud |
| **Calcolo GPU/AI** | EC2 (istanze P4d, P5) | VM serie NC/ND | VM A2/A3; TPU |
### Modelli di prezzo delle VM
| Modello | AWS | Azzurro | PCG |
|-------|-----|-------|-----|
| **Su richiesta** | Istanze su richiesta | Pagamento a consumo | Su richiesta |
| **Riservato/Impegnato** | Istanze riservate (1–3 anni) | VM riservate (1-3 anni) | Sconti per impegno di utilizzo (1–3 anni) |
| **Spot / Interrompibile** | Istanze Spot | Individua le VM | VM prerilasciabili/spot |
| **Piani di risparmio** | Piani di risparmio | Piani di risparmio | Sconti per impegno |
---

## Magazzinaggio
| Categoria di servizio | AWS | Azzurro | PCG |
|-----------------|-----|-------|-----|
| **Archiviazione di oggetti** | S3 | Archiviazione BLOB | Archiviazione nel cloud |
| **Archiviazione a blocchi** | EBS | Dischi gestiti | Disco permanente |
| **Archiviazione file** | EFS, FSx | File di Azure | Archivio file |
| **Archivio / Freddo** | Ghiacciaio S3, Archivio profondo | Livelli di raffreddamento/archivio BLOB | Coldline/Archivio di archiviazione cloud |
| **Trasferimento dati** | Palla di neve, sincronizzazione dati | Casella dati | Dispositivo di trasferimento |
### Confronto delle classi di archiviazione
| Caso d'uso | AWS S3 | Blob azzurro | Archiviazione cloud GCP |
|----------|--------|------------|-----|
| **Accesso frequente** | Norma S3 | Caldo | Norma |
| **Accesso poco frequente** | S3 Standard-IA | Bello | Vicino |
| **Accesso raro** | S3 Una Zona-IA | — | Linea Fredda |
| **Archivio** | S3 Ghiacciaio / Archivio profondo | Archivio | Archivio |
---

## Database
| Categoria di servizio | AWS | Azzurro | PCG |
|-----------------|-----|-------|-----|
| **Relazionale (gestito)** | RDS (MySQL, PostgreSQL, Oracle, SQL Server) | Database di Azure (MySQL, PostgreSQL); SQL di Azure | Cloud SQL (MySQL, PostgreSQL) |
| **Relazionale (nativo del cloud)** | Aurora (compatibile con MySQL/PostgreSQL) | Database SQL di Azure (pool elastici) | Cloud Spanner (distribuito a livello globale) |
| **NoSQL (documento)** | DynamoDB | Cosmos DB (API MongoDB, API SQL) | Firestore; Archivio dati |
| **NoSQL (colonna larga)** | DynamoDB (anche) | Cosmos DB (API Cassandra) | Grande tavolo |
| **NoSQL (valore-chiave)** | DynamoDB, ElastiCache | Cache di Azure per Redis | Memoria (Redis) |
| **Grafico** | Nettuno | Cosmos DB (API Gremlin) | — |
| **Serie storica** | Flusso temporale | Esplora dati di Azure | — |
| **Registro** | QLDB | Registro riservato di Azure | — |
| **Cache in memoria** | ElastiCache (Redis, Memcached) | Cache di Azure per Redis | Memoria |
| **Cerca** | Servizio OpenSearch | Ricerca AI di Azure | Ricerca nel cloud; Ricerca AI vertice |
| **Magazzino dati** | Spostamento verso il rosso | Analisi sinapsi | BigQuery |
---

## Intelligenza artificiale e apprendimento automatico
| Categoria di servizio | AWS | Azzurro | PCG |
|-----------------|-----|-------|-----|
| **Piattaforma ML** | SageMaker | Apprendimento automatico di Azure | Vertice AI |
| **API preaddestrate** | Riconoscimento (visione), Polly (TTS), Comprendere (PNL), Trascrivere | Servizi Cognitivi (Visione, Discorso, Linguaggio, Decisione) | Vision AI, sintesi vocale, API linguaggio naturale |
| **LLM / AI generativa** | Bedrock (Claude, Lama, Titano) | Servizio Azure OpenAI (GPT-4, DALL-E) | Vertice AI (Gemelli); Giardino modello |
| **Vettore / Incorporamenti** | OpenSearch (k-NN), basi di conoscenza Bedrock | Ricerca AI di Azure (vettore) | Ricerca vettoriale Vertex AI, AlloyDB |
| **MLOps** | Pipeline SageMaker, registro dei modelli | Pipeline di Azure ML, registro dei modelli | Pipeline AI Vertex, registro dei modelli |
| **Etichettatura dei dati** | SageMaker Verità fondamentale | Etichettatura dei dati di Azure ML | Etichettatura dei dati AI vertice |
| **AI conversazionale** | Lex | Servizio Bot di Azure | Dialogflow CX/ES |
| **Traduzione** | Traduci | Traduttore | API di traduzione |
---

##Rete
| Categoria di servizio | AWS | Azzurro | PCG |
|-----------------|-----|-------|-----|
| **Rete virtuale** | VPC | Rete virtuale (VNet) | VPC |
| **Bilanciamento del carico** | ELB/ALB/NLB/CLB | Bilanciatore del carico (applicazione, rete, gateway) | Bilanciamento del carico nel cloud |
| **DNS** | Itinerario 53 | DNS di Azure | DNS cloud |
| **CDN** | CloudFront | Porta d'ingresso azzurra | CDN cloud |
| **Gateway API** | Gateway API | Gestione API | Gateway API |
| **VPN** | VPN da sito a sito, VPN client | Gateway VPN | VPN cloud |
| **Connessione diretta/ExpressRoute** | Connessione diretta | ExpressRoute | Interconnessione cloud |
| **Link privato** | PrivateLink, endpoint VPC | Collegamento privato, endpoint privati ​​| Connessione al servizio privato |
| **Firewall** | WAF, firewall di rete | Firewall di Azure, WAF | Armatura cloud, firewall |
| **Protezione DDoS** | Scudo Standard/Avanzato | Protezione DDoS | Armatura nuvolosa |
---

## Monitoraggio e registrazione
| Categoria di servizio | AWS | Azzurro | PCG |
|-----------------|-----|-------|-----|
| **Metriche/Monitoraggio** | CloudWatch | Monitoraggio di Azure | Monitoraggio cloud (Stackdriver) |
| **Registrazione** | Log di CloudWatch | Log Analytics (log di monitoraggio di Azure) | Registrazione nel cloud |
| **Tracciamento** | Raggi X | Approfondimenti sull'applicazione | Traccia nuvola |
| **Avviso** | Allarmi CloudWatch | Avvisi di monitoraggio di Azure | Avvisi di monitoraggio del cloud |
| **Cruscotti** | Dashboard CloudWatch | Cartelle di lavoro/Dashboard di Azure | Dashboard di monitoraggio del cloud |
| **Tracciamento errori** | Sintetici CloudWatch | Approfondimenti sull'applicazione | Segnalazione errori cloud |
| **Di terze parti** | Datadog, Nuova Reliquia, PagerDuty | Datadog, Nuova Reliquia, PagerDuty | Datadog, Nuova Reliquia, PagerDuty |
---

## Infrastruttura come codice e DevOps
| Categoria di servizio | AWS | Azzurro | PCG |
|-----------------|-----|-------|-----|
| **IaC (nativo)** | CloudFormazione | Modelli BRACCIO / Bicipiti | Responsabile della distribuzione / Pulumi |
| **IaC (tra cloud)** | Terraform, Pulumi, CDK | Terraformare, Pulumi, Bicipite | Terraformazione, Pulumi |
| **CI/CD** | CodePipeline, CodeBuild | Azure DevOps, azioni GitHub | Creazione del cloud; Distribuzione nel cloud |
| **Registro dei contenitori** | Racc. | Registro contenitori di Azure | Registro degli artefatti |
| **GitOps** | App Mesh + Flux/ArgoCD | Flux/ArgoCD su AKS | Sincronizzazione configurazione (Anthos) |
| **Gestione dei segreti** | Responsabile dei segreti, Archivio parametri SSM | Archivio chiavi | Direttore segreto |
---

## Considerazioni sui prezzi
| Fattore | AWS | Azzurro | PCG |
|--------|-----|-------|-----|
| **Granularità della fatturazione** | Al secondo (dopo la prima ora per alcuni) | Al secondo | Al secondo |
| **Sconti per uso sostenuto** | Istanze riservate/Piani di risparmio | VM riservate | Sconti per impegno |
| **Istanze Spot** | Fino al 90% di sconto | Fino al 90% di sconto | Fino al 91% di sconto |
| **Uscita dati** | Addebitato (costoso) | Caricato | Stesso prezzo indipendentemente dalla destinazione (spesso più economico) |
| **Livello gratuito** | 12 mesi + sempre gratis | 12 mesi + credito di $ 200 | $ 300 per 90 giorni + sempre gratuito |
| **Sconti aziendali** | Programma di sconti aziendali (EDP) | MACC (Contratto di impegno monetario) | Utilizzo impegnato + CUD |
---

## Quando utilizzare quale
| Scenario | Consigliato | Perché |
|----------|-------------|-----|
| **La più ampia selezione di servizi; ecosistema maturo** | AWS | Catalogo più grande; la maggior parte delle integrazioni di terze parti |
| **Microsoft Enterprise; Directory attiva; ibrido** | Azzurro | Integrazione AD nativa; forte utensileria ibrida |
| **Archiviazione dei dati; BigQuery; ad alto contenuto di analisi** | PCG | BigQuery è il migliore della categoria; integrazione perfetta dei dati |
| **Sviluppo nativo di Kubernetes** | PCG | GKE è il Kubernetes gestito più raffinato |
| **Applicazioni AI/LLM generative** | Azure o GCP | Azure OpenAI per modelli GPT; Vertex AI per Gemelli |
| **Applicazioni su scala globale e a bassa latenza** | PCG | La rete globale di Google è un vero vantaggio |
| **Carichi di lavoro pesanti per governo/conformità** | AWS o Azure | La maggior parte delle certificazioni di conformità; Regioni GovCloud |
| **Startup sensibili ai costi** | GCP o AWS | Il livello gratuito di GCP è generoso; AWS ha crediti di avvio |
| **Stack Microsoft/.NET esistente** | Azzurro | Stretta integrazione con Visual Studio, .NET, Office 365 |
| **Strategia multi-cloud** | Terraform + tutti e tre | Utilizza Terraform per gestire le risorse tra cloud |
---

## Riepilogo
Tutti e tre i cloud sono capaci, affidabili e in costante espansione. La scelta di solito dipende da: cosa già sa il tuo team, come si presentano i tuoi contratti esistenti e quali servizi specifici sono importanti per il tuo carico di lavoro. Il multi-cloud è sempre più comune: utilizza Terraform o Pulumi per evitare vincoli al fornitore a livello di infrastruttura e scegli ciascun cloud per ciò che sa fare meglio.