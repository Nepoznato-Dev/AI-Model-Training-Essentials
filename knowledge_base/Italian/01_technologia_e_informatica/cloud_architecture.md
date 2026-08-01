# Architettura cloud

## Fondamenti di cloud computing

### Cos'è il cloud computing?
Fornitura on-demand di risorse informatiche — come server, storage, database, reti e software — tramite Internet, con un modello di prezzo a consumo.

### Caratteristiche essenziali (definizione NIST)
- **Self-service su richiesta**: fornitura di risorse senza interazione umana
- **Ampio accesso alla rete**: disponibile in rete tramite meccanismi standard
- **Condivisione delle risorse**: modello multi-tenant con allocazione dinamica
- **Elasticità rapida**: scala rapidamente verso l'esterno e verso l'interno
- **Servizio misurato**: utilizzo delle risorse monitorato e fatturato

### Modelli di distribuzione cloud
- **Cloud pubblico**: di proprietà dei fornitori, infrastruttura condivisa (AWS, Azure, GCP)
- **Cloud privato**: dedicato a una singola organizzazione, on-premise o ospitato
- **Cloud ibrido**: combinazione di ambienti pubblici e privati
- **Multi-cloud**: utilizzo di più provider di cloud pubblico
- **Cloud di comunità**: condiviso da organizzazioni con esigenze o vincoli comuni

### Modelli di servizio

#### Infrastruttura come servizio (IaaS)
- **Fornisce**: macchine virtuali, storage, reti, sistemi operativi
- **Esempi**: AWS EC2, Google Compute Engine, VM di Azure
- **Casi d'uso**: migrazioni lift-and-shift, ambienti di sviluppo, esigenze di controllo elevato

#### Piattaforma come servizio (PaaS)
- **Fornisce**: Piattaforme di sviluppo, database, middleware
- **Esempi**: Heroku, Google App Engine, AWS Elastic Beanstalk
- **Casi d'uso**: sviluppo di applicazioni, distribuzione API, microservizi

#### Software come servizio (SaaS)
- **Fornisce**: applicazioni complete su Internet
- **Esempi**: Salesforce, Google Workspace, Microsoft 365, Slack
- **Casi d'uso**: e-mail, CRM, collaborazione, applicazioni aziendali

#### Funzione come servizio (FaaS) / Serverless
- **Fornisce**: esecuzione di funzioni guidate dagli eventi
- **Esempi**: AWS Lambda, Funzioni di Azure, Funzioni Google Cloud
- **Casi d'uso**: elaborazione di eventi, API, attività pianificate, elaborazione in tempo reale

## Principali fornitori di servizi cloud

### Amazon Web Services (AWS)
- **Quota di mercato**: ~32% (maggior fornitore)
- **Servizi chiave**:
  - Calcolo: EC2, Lambda, ECS, EKS
  - Archiviazione: S3, EBS, Glacier
  - Database: RDS, DynamoDB, Aurora
  - Rete: VPC, Route 53, CloudFront
  - AI/ML: SageMaker, Rekognition, Comprehend

### Microsoft Azure
- **Quota di mercato**: ~23%
- **Punti di forza**: integrazione aziendale, cloud ibrido, ecosistema Microsoft
- **Servizi chiave**:
  - Calcolo: macchine virtuali, funzioni di Azure, AKS
  - Archiviazione: archiviazione BLOB, archiviazione su disco
  - Database: database SQL, Cosmos DB
  - Networking: rete virtuale, gestione del traffico
  - AI/ML: Azure ML, Servizi cognitivi

### Google Cloud Platform (GCP)
- **Quota di mercato**: ~10%
- **Punti di forza**: analisi dei dati, AI/ML, Kubernetes
- **Servizi chiave**:
  - Calcolo: Compute Engine, Cloud Functions, GKE
  - Archiviazione: archiviazione cloud, disco permanente
  - Database: Cloud SQL, Firestore, Bigtable
  - Analisi: BigQuery, Dataflow, Pub/Sub
  - AI/ML: Vertex AI, AutoML

### Altri fornitori
- **IBM Cloud**: focus aziendale, Watson AI
- **Oracle Cloud**: carichi di lavoro di database, applicazioni aziendali
- **Alibaba Cloud**: dominante nell'Asia-Pacifico
- **DigitalOcean**: offerte semplificate e adatte agli sviluppatori

## Modelli di architettura cloud

### Principi del Well-Architected Framework

#### Eccellenza operativa
- Automatizzare le operazioni
- Apportare modifiche frequenti e reversibili
- Perfezionare continuamente le procedure
- Anticipare il fallimento

#### Sicurezza
- Implementare una solida base identitaria
- Abilitare la tracciabilità
- Applicare la sicurezza a tutti i livelli
- Automatizzare le migliori pratiche di sicurezza
- Proteggere i dati in transito e a riposo

#### Affidabilità
- Testare le procedure di ripristino
- Ripristino automatico in caso di errore
- Scala orizzontalmente per la disponibilità
- Evitare di stimare la capacità "a intuito"
- Gestire il cambiamento tramite l'automazione

#### Efficienza prestazionale
- Rendere accessibili le tecnologie avanzate
- Espandersi a livello globale in pochi minuti
- Utilizzare architetture serverless
- Sperimentare più spesso
- Considerare le caratteristiche intrinseche dei sistemi

#### Ottimizzazione dei costi
- Adottare un modello basato sul consumo
- Misurare l'efficienza complessiva
- Evitare di spendere per attività poco differenzianti
- Analizzare e attribuire le spese
- Utilizzare i servizi gestiti

### Modelli architettonici comuni

#### Architettura dei microservizi
- Suddividere le applicazioni in piccoli servizi indipendenti
- Ogni servizio possiede i suoi dati e la sua logica
- Comunicare tramite API (REST, gRPC, messaggistica)
- Distribuire in modo indipendente
- **Vantaggi**: scalabilità, isolamento dei guasti, diversità tecnologica
- **Sfide**: complessità distribuita, coerenza dei dati, monitoraggio

#### Architettura guidata dagli eventi
- I componenti comunicano attraverso eventi
- I produttori emettono eventi, i consumatori reagiscono
- **Modelli**: sourcing di eventi, CQRS, pub/sub
- **Tecnologie**: Kafka, SNS/SQS, EventBridge, Pub/Sub
- **Vantaggi**: accoppiamento flessibile, scalabilità, elaborazione in tempo reale

#### Architettura serverless
- Nessuna gestione del server richiesta
- Paga per esecuzione
- Ridimensionamento automatico
- **Componenti**: funzioni, API Gateway, servizi gestiti
- **Vantaggi**: efficienza dei costi, operazioni ridotte, implementazione rapida
- **Considerazioni**: avviamenti a freddo, vincoli del fornitore, limiti di esecuzione

#### Architettura a più livelli (N livelli)
- Livello di presentazione (interfaccia utente)
- Livello applicazione/logica aziendale
- Livello di accesso ai dati
- Livello database
- **Vantaggi**: separazione delle responsabilità, manutenibilità
- **Comune**: applicazioni Web a 3 livelli

#### Architettura basata sullo spazio
- Gestire un'elevata concorrenza con dati distribuiti
- Memoria virtualizzata tra server
- I nodi di elaborazione si ridimensionano in modo indipendente
- **Casi d'uso**: applicazioni a volume elevato e a bassa latenza

## Servizi informatici

### Macchine virtuali
- **Tipi**: uso generico, ottimizzato per il calcolo, ottimizzato per la memoria, GPU
- **Prezzi**: istanze on-demand, riservate, istanze spot
- **Gestione**: gruppi con scalabilità automatica, bilanciatori del carico
- **Best practice**: dimensionamento corretto, tagging, monitoraggio, applicazione di patch

### Contenitori
- **Docker**: standard di runtime del contenitore
- **Orchestrazioni**: Kubernetes (EKS, AKS, GKE), ECS, Fargate
- **Vantaggi**: portabilità, efficienza, coerenza
- **Registro**: ECR, GCR, ACR, Docker Hub

### Funzioni senza server
- **Modello di esecuzione**: attivato da eventi, senza stato
- **Limiti**: tempo di esecuzione, memoria, esecuzioni simultanee
- **Casi d'uso**: API, elaborazione di file, processi pianificati, backend IoT
- **Monitoraggio**: conteggio delle chiamate, errori, durata, avviamenti a freddo

## Soluzioni di archiviazione

### Archiviazione di oggetti
- **Caratteristiche**: struttura piatta, metadati, accesso HTTP
- **Esempi**: AWS S3, Google Cloud Storage, BLOB di Azure
- **Casi d'uso**: risorse statiche, backup, data lake, archivi
- **Classi di archiviazione**: standard, accesso infrequente, cold, archive (con costi e tempi di accesso differenti)

### Archiviazione a blocchi
- **Caratteristiche**: volumi grezzi, collegati alle VM
- **Esempi**: AWS EBS, Google Persistent Disk, dischi di Azure
- **Casi d'uso**: database, volumi di avvio, esigenze di prestazioni elevate
- **Tipi**: SSD, HDD, IOPS con provisioning

### Archiviazione di file
- **Caratteristiche**: file system condivisi, protocolli NFS/SMB
- **Esempi**: AWS EFS, Google Filestore, File di Azure
- **Casi d'uso**: gestione dei contenuti, configurazioni condivise, lift-and-shift

### Archiviazione di archivio
- **Caratteristiche**: costo più basso, ritardi nel recupero
- **Esempi**: S3 Glacier, Azure Archive Storage
- **Casi d'uso**: conformità, backup a lungo termine, dati storici

## Servizi di database

### Database relazionali gestiti
- **Servizi**: AWS RDS/Aurora, Google Cloud SQL, database SQL di Azure
- **Caratteristiche**: backup automatizzati, patch, scalabilità, replica
- **Motori**: MySQL, PostgreSQL, MariaDB, Oracle, SQL Server

### Database NoSQL
- **Documento**: DocumentDB, Firestore, Cosmos DB
- **Valore-chiave**: DynamoDB, cache Redis
- **Colonna ampia**: Bigtable, Cassandra (gestito)
- **Grafico**: Nettuno, Cosmos DB (API grafico)

### Data warehouse
- **Servizi**: Snowflake, Redshift, BigQuery, Synapse
- **Caratteristiche**: archiviazione colonnare, architettura MPP
- **Casi d'uso**: analisi, BI, analisi dei dati su larga scala

### Servizi di memorizzazione nella cache
- **In memoria**: ElastiCache (Redis/Memcached), Cloud Memorystore
- **Memoria nella cache CDN**: CloudFront, Cloud CDN, CDN di Azure
- **Casi d'uso**: archiviazione delle sessioni, memorizzazione nella cache delle query, distribuzione dei contenuti

## Rete

### Reti virtuali
- **VPC/VNet**: ambienti di rete isolati
- **Sottoreti**: pubblica (rivolta a Internet), privata (solo interna)
- **Indirizzamento IP**: blocchi CIDR, IPv4/IPv6
- **Tabelle di percorso**: controlla il flusso del traffico

### Bilanciamento del carico
- **Tipi**: Applicazione (L7), rete (L4), Gateway
- **Caratteristiche**: controlli di integrità, terminazione SSL, sessioni permanenti
- **Servizi**: ELB/ALB/NLB, bilanciamento del carico nel cloud, bilanciatore del carico di Azure

### Reti per la distribuzione di contenuti (CDN)
- **Scopo**: memorizza nella cache i contenuti nelle edge location
- **Vantaggi**: latenza ridotta, carico di origine inferiore, distribuzione globale
- **Servizi**: CloudFront, Cloud CDN, Azure CDN, Akamai

### Servizi DNS
- **Funzioni**: registrazione del dominio, routing, controlli sanitari
- **Servizi**: Route 53, Cloud DNS, DNS di Azure
- **Politiche di routing**: semplice, ponderato, basato sulla latenza, geolocalizzazione, failover

### Opzioni di connettività
- **Gateway Internet**: accesso pubblico a Internet
- **NAT Gateway**: accesso in uscita alla sottorete privata
- **VPN**: tunnel crittografati verso locali
- **Direct Connect/ExpressRoute**: connessioni private dedicate
- **Peering VPC**: collega i VPC all'interno/tra account

## Sicurezza nel cloud

### Modello di responsabilità condivisa
- **Responsabilità del fornitore**: sicurezza del cloud, cioè dell’infrastruttura sottostante
- **Responsabilità del cliente**: sicurezza nel cloud, quindi dati, applicazioni e accessi
- **Varia in base al servizio**: più il servizio è gestito dal provider, più responsabilità ricadono su di lui

### Gestione delle identità e degli accessi (IAM)
- **Utenti**: identità individuali
- **Gruppi**: raccolte di utenti
- **Ruoli**: credenziali temporanee assegnate a servizi o utenti
- **Politiche**: documenti JSON che definiscono le autorizzazioni
- **Principi**: privilegio minimo e separazione dei compiti

### Sicurezza della rete
- **Gruppi di sicurezza**: firewall con stato per le istanze
- **ACL di rete**: firewall stateless per sottoreti
- **Web Application Firewall (WAF)**: protezione dagli exploit web
- **Protezione DDoS**: Shield, Cloud Armor, protezione DDoS gestita

### Protezione dei dati
- **Crittografia a riposo**: KMS, chiavi gestite dal cliente
- **Crittografia in transito**: TLS/SSL, HTTPS
- **Gestione delle chiavi**: HSM, rotazione delle chiavi, audit trail
- **Gestione dei segreti**: Secrets Manager, Key Vault e strumenti equivalenti

### Conformità e governance
- **Certificazioni**: SOC 2, ISO 27001, HIPAA, PCI-DSS, GDPR
- **Strumenti**: applicazione delle policy, reporting sulla conformità, registri di controllo
- **Framework**: Cloud Security Alliance, NIST CSF

## DevOps nel cloud

### Servizi CI/CD
- **AWS**: CodePipeline, CodeBuild, CodeDeploy
- **Azure**: Azure DevOps, azioni GitHub
- **GCP**: Cloud Build, Cloud Deploy
- **Terze parti**: Jenkins, CircleCI, GitLab CI

### Infrastruttura come codice (IaC)
- **Terraform**: multi-cloud, dichiarativo, gestione dello stato
- **CloudFormation**: modelli YAML/JSON nativi AWS
- **Modelli ARM**: nativo di Azure
- **Gestore distribuzione**: nativo di GCP
- **Pulumi**: infrastruttura definita tramite linguaggi di programmazione
- **Vantaggi**: controllo della versione, ripetibilità, documentazione

### Gestione della configurazione
- **Ansible**: playbook YAML senza agente
- **Chef**: ecosistema maturo, basato su Ruby
- **Puppet**: approccio dichiarativo e ampio ecosistema
- **SaltStack**: veloce, basato su Python

### Monitoraggio e osservabilità
- **Metriche**: CloudWatch, Cloud Monitoring, Azure Monitor
- **Logging**: CloudWatch Logs, Cloud Logging, Azure Log Analytics
- **Tracing**: X-Ray, Cloud Trace, Application Insights
- **Dashboard**: dashboard di CloudWatch, Cloud Console e strumenti equivalenti
- **Avvisi**: SNS, alert di Cloud Monitoring, action group di Azure

### Orchestrazione dei contenitori
- **Kubernetes**: orchestrazione standard del settore
- **Servizi gestiti**: EKS, AKS, GKE
- **Service Mesh**: Istio, Linkerd (gestione del traffico, sicurezza)
- **GitOps**: ArgoCD, Flux (distribuzioni dichiarative)

## Gestione dei costi

### Modelli di prezzo
- **Pagamento in base al consumo**: paga in base all'utilizzo
- **Istanze riservate**: impegni da 1 a 3 anni, sconti significativi
- **Istanze Spot**: offerte per capacità inutilizzata, possono essere interrotte
- **Piani di risparmio**: prezzi flessibili con impegno
- **Livello gratuito**: utilizzo gratuito limitato per i nuovi account

### Strategie di ottimizzazione dei costi
- **Ridimensionamento corretto**: abbina i tipi di istanza alle esigenze del carico di lavoro
- **Ridimensionamento automatico**: ridimensiona in base alla domanda
- **Capacità riservata**: impegno per carichi di lavoro stazionari
- **Utilizzo Spot**: da utilizzare per carichi di lavoro flessibili e con tolleranza agli errori
- **Livelli di storage**: sposta i dati poco frequenti su livelli più economici
- **Pulizia**: elimina risorse, snapshot e AMI inutilizzati

### Strumenti di gestione dei costi
- **AWS**: Cost Explorer, Budget, Trusted Advisor
- **Azure**: gestione dei costi, advisor
- **GCP**: rapporti di fatturazione, recommender
- **Di terze parti**: CloudHealth, CloudCheckr, Datadog

## Alta disponibilità e ripristino di emergenza

### Concetti di disponibilità
- **Zone di disponibilità**: data center fisicamente separati all'interno della regione
- **Regioni**: aree geografiche che comprendono più zone di disponibilità
- **Edge location**: nodi CDN distribuiti a livello globale

### Strategie HA
- **Multi-AZ**: distribuzione in zone di disponibilità
- **Riparazione automatica**: sostituzione automatica delle istanze non riuscite
- **Bilanciamento del carico**: distribuire il traffico tra istanze sane
- **Replica del database**: implementazioni Multi-AZ, repliche di lettura

### Strategie di ripristino di emergenza
- **Backup e ripristino**: backup periodici, ripristino quando necessario (costo più basso)
- **Pilot Light**: componenti essenziali sempre attivi, ampliati solo in caso di emergenza
- **Warm Standby**: ambiente ridotto ma sempre operativo
- **Multi-sito attivo/attivo**: produzione completa in più regioni (costo più elevato)

### RTO e RPO
- **Recovery Time Objective (RTO)**: tempo di inattività massimo accettabile
- **Recovery Point Objective (RPO)**: massima perdita di dati accettabile
- **Selezione della strategia**: in base ai requisiti aziendali e al budget

## Tendenze emergenti

### Edge computing
- Elaborare i dati più vicino alla fonte
- **Servizi**: AWS Outposts, Wavelength, Azure Edge, Cloud CDN
- **Casi d'uso**: IoT, analisi in tempo reale, applicazioni a bassa latenza

### Multi-cloud e cloud ibrido
- Evitare il lock-in del fornitore
- Sfruttare i migliori servizi
- **Strumenti**: Terraform, Anthos, Arc, CloudHealth

### Servizi IA/ML
- Modelli pre-addestrati: visione, parola, linguaggio
- Formazione del modello personalizzato: SageMaker, Vertex AI, Azure ML
- MLOps: implementazione del modello, monitoraggio, governance

### Informatica quantistica
- **Servizi**: AWS Braket, Azure Quantum
- **Stato**: tecnologia ancora iniziale e sperimentale
- **Potenziale**: crittografia, ottimizzazione, scoperta di farmaci

### Cloud sostenibile
- Monitoraggio dell'impronta di carbonio
- Impegni per le energie rinnovabili
- Utilizzo efficiente delle risorse
- Modelli di architettura verde