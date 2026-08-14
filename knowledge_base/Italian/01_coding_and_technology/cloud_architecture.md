---
# Metadata
title: "Cloud Architecture"
description: "Cloud providers, architecture patterns, security"
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
# Architettura cloud
Il cloud computing ha cambiato radicalmente il modo in cui le organizzazioni creano, distribuiscono e scalano il software. Invece di acquistare e mantenere server fisici, puoi fornire risorse informatiche su richiesta, pagare per ciò che utilizzi e scalare a livello globale in pochi minuti. Questo file copre i concetti fondamentali, i modelli di architettura, i servizi e le migliori pratiche che devi conoscere.
---

## Fondamenti di cloud computing
### Cos'è il cloud computing?
Distribuzione on-demand di risorse informatiche (server, storage, database, reti, software) su Internet con prezzi a consumo.
### Caratteristiche essenziali del NIST
| Caratteristico | Significato |
|---------------|---------|
| **Self-service su richiesta** | Fornire risorse senza interazione umana |
| **Ampio accesso alla rete** | Disponibile in rete tramite meccanismi standard |
| **Condivisione delle risorse** | Modello multi-tenant; risorse assegnate dinamicamente |
| **Elasticità rapida** | Scala rapidamente verso l'esterno e verso l'interno |
| **Servizio Misurato** | L'utilizzo viene monitorato e fatturato |
### Modelli di distribuzione
| Modello | Descrizione | Quando usarlo |
|-------|-------------|-----|
| **Cloud pubblico** | Di proprietà dei fornitori; infrastruttura condivisa (AWS, Azure, GCP) | La maggior parte dei carichi di lavoro; conveniente |
| **Cloud privato** | Dedicato ad una singola organizzazione | Requisiti normativi, dati sensibili |
| **Cloud ibrido** | Combinazione di pubblico e privato | Flessibilità + conformità |
| **Multicloud** | Utilizzo di più provider di cloud pubblici | Evita i vincoli al fornitore, il meglio della razza |
### Modelli di servizio
| Modello | Fornisce | Esempi | Casi d'uso |
|-------|----------|----------|-----------|
| **IaaS** | VM, storage, reti, sistema operativo | AWS EC2, VM di Azure, GCP Compute Engine | Migrazioni lift-and-shift, controllo completo |
| **PaaS** | Piattaforme di sviluppo, database, middleware | Heroku, Google App Engine, AWS Elastic Beanstalk | Sviluppo di app, distribuzione API |
| **SaaS** | Applicazioni complete su Internet | Salesforce, Google Workspace, Microsoft 365 | E-mail, CRM, collaborazione |
| **FaaS/senza server** | Esecuzione di funzioni guidate da eventi | AWS Lambda, Funzioni di Azure, Funzioni cloud GCP | API, elaborazione eventi, attività pianificate |
---

## Principali fornitori di servizi cloud
| Fornitore | Quota di mercato | Punti di forza |
|----------|-------------|-----------|
| **AWS** | ~32% | Il più ampio catalogo di servizi, il più grande ecosistema |
| **Azzurro** | ~23% | Integrazione aziendale, cloud ibrido, stack Microsoft |
| **GCP** | ~10% | Analisi dei dati, AI/ML, Kubernetes |
| **Nuvola Alibaba** | ~4% | Dominante nell'Asia-Pacifico |
| **Oracle Cloud** | ~2% | Carichi di lavoro di database, app aziendali |
| **IBM Cloud** | ~2% | Focus aziendale, Watson AI |
| **OceanoDigitale** | Nicchia | Offerte semplificate e intuitive per gli sviluppatori |
### Confronto dei servizi (i 3 principali fornitori)
| Categoria | AWS | Azzurro | PCG |
|----------|-----|-------|-----|
| **Calcola** | EC2, Lambda, ECS | Macchine virtuali, funzioni, AKS | Compute Engine, Funzioni cloud, GKE |
| **Archiviazione** | S3, EBS, Ghiacciaio | Archiviazione BLOB, archiviazione su disco | Archiviazione nel cloud, disco permanente |
| **Banca dati** | RDS, DynamoDB, Aurora | Database SQL, Cosmos DB | Cloud SQL, Firestore, Bigtable |
| **Analisi** | Redshift, EMR | Sinapsi, Databricks | BigQuery, flusso di dati |
| **AI/ML** | SageMaker, Riconoscimento | Azure ML, Servizi cognitivi | AI vertice, AutoML |
| **Rete** | VPC, Route 53, CloudFront | Rete virtuale, Gestione traffico | VPC, Cloud DNS, Cloud CDN |
---

## Modelli di architettura
### Framework ben architettato
Tutti e tre i principali fornitori pubblicano framework ben architettati costruiti attorno a cinque pilastri:
| Pilastro | Principi chiave |
|--------|---------------|
| **Eccellenza operativa** | Automatizzare le operazioni; apportare modifiche frequenti e reversibili; anticipare il fallimento |
| **Sicurezza** | Forte base identitaria; applicare la sicurezza a ogni livello; proteggere i dati in transito e a riposo |
| **Affidabilità** | Procedure di recupero test; ripristino automatico in caso di errore; scala orizzontalmente |
| **Efficienza prestazionale** | Utilizza senza server; diventare globale in pochi minuti; sperimentare spesso |
| **Ottimizzazione dei costi** | Adottare un modello di consumo; utilizzare i servizi gestiti; smettere di spendere per il lavoro indifferenziato |
### Modelli comuni
| Modello | Descrizione | Vantaggi | Sfide |
|---------|-----|----------|------------|
| **Microservizi** | Suddividi l'app in piccoli servizi indipendenti | Scalabilità, isolamento dei guasti, distribuzione indipendente | Complessità distribuita, consistenza dei dati |
| **Basato sugli eventi** | I componenti comunicano attraverso eventi | Accoppiamento lento, elaborazione in tempo reale | Complessità del debug, coerenza finale |
| **Senza server** | Nessuna gestione del server; pagamento per esecuzione | Efficienza dei costi, implementazione rapida | Riavvii a freddo, lock-in del fornitore, limiti di esecuzione |
| **A strati (livello N)** | Presentazione → Logica aziendale → Accesso ai dati → Database | Separazione degli interessi, manutenibilità | Può diventare monolitico |
| **Basato sullo spazio** | Dati distribuiti su nodi di memoria virtualizzati | Gestisce concorrenza elevata e bassa latenza | Complesso da progettare e gestire |
---

## Servizi principali
### Calcola
| Tipo di servizio | Dettagli |
|-------------|---------|
| **Macchine virtuali** | GPU per uso generico, ottimizzata per il calcolo e per la memoria. Prezzi: su richiesta, riservati, spot. |
| **Contenitori** | Tempo di esecuzione della finestra mobile; orchestrazione tramite Kubernetes (EKS, AKS, GKE). Registri: ECR, GCR, ACR. |
| **Funzioni serverless** | Attivato da eventi, apolide. Limiti su tempo di esecuzione, memoria, concorrenza. |
### Magazzinaggio
| Digitare | Caratteristiche | Esempi | Ideale per |
|------|----------|----------|----------|
| **Oggetto** | Struttura piatta, accesso HTTP, ricco di metadati | S3, archiviazione cloud, BLOB di Azure | Asset statici, backup, data lake |
| **Blocca** | Volumi grezzi collegati alle VM | EBS, disco permanente, dischi di Azure | Database, volumi di avvio |
| **File** | File system condivisi (NFS/SMB) | EFS, archivio file, file di Azure | Gestione dei contenuti, configurazioni condivise |
| **Archivio** | Costo più basso, ritardi nel recupero | S3 Glacier, Archivio di Azure | Conformità, backup a lungo termine |
### Database
| Categoria | Servizi | Caso d'uso |
|----------|----------|----------|
| **Relazionale Gestito** | RDS, Cloud SQL, Azure SQL | App tradizionali, transazioni ACID |
| **NoSQL — Documento** | DocumentDB, Firestore, Cosmos DB | Schemi flessibili, dati JSON |
| **NoSQL — Valore-chiave** | DynamoDB, cache Redis | Caching, sessioni, ricerche semplici |
| **NoSQL — Colonna larga** | Bigtable, Cassandra | Scrittura pesante, serie temporali |
| **NoSQL — Grafico** | Nettuno, Cosmos DB (API grafico) | Relazioni, social network |
| **Archiviazione dati** | Fiocco di neve, Redshift, BigQuery, Synapse | Analisi, BI |
| **Memorizzazione nella cache** | ElastiCache, Cloud Memorystore | Archiviazione delle sessioni, memorizzazione nella cache delle query |
---

##Rete
### Reti virtuali
Ogni distribuzione cloud si trova all'interno di un Virtual Private Cloud (VPC/VNet), una rete isolata definita con blocchi CIDR, sottoreti (pubbliche o private), tabelle di routing e gateway.
### Bilanciamento del carico e CDN
| Servizio | Scopo |
|---------|---------|
| **Bilanciatori del carico** | Distribuire il traffico tra istanze (rete L4, applicazione L7) |
| **CDN** | Memorizza nella cache i contenuti nelle edge location per una latenza inferiore (CloudFront, Cloud CDN, Azure CDN) |
| **DNS** | Registrazione domini, policy di routing, controlli di integrità (Route 53, Cloud DNS, Azure DNS) |
### Opzioni di connettività
| Opzione | Descrizione |
|--------|-------------|
| **Gateway Internet** | Accesso pubblico a Internet per VPC |
| **Gateway NAT** | Accesso in uscita alla sottorete privata |
| **VPN** | Tunnel crittografati verso locali |
| **Connessione diretta/ExpressRoute** | Collegamenti privati ​​dedicati |
| **Peering VPC** | Connetti VPC all'interno o tra account |
---

##Sicurezza
### Modello di responsabilità condivisa
| Strato | Fornitore | Cliente |
|-------|----------|----------|
| **Infrastrutture** (hardware, strutture) | ✅| |
| **Calcolo, archiviazione, rete** | ✅ (gestito) | ✅ (autogestito) |
| **Dati, applicazioni, identità** | | ✅ |
Più il servizio è gestito, più il fornitore gestisce. Con IaaS gestisci quasi tutto; con SaaS, il provider gestisce quasi tutto.
### Gestione delle identità e degli accessi (IAM)
| Concetto | Descrizione |
|---------|-----|
| **Utenti** | Identità individuali |
| **Gruppi** | Collezioni di utenti |
| **Ruoli** | Credenziali temporanee per servizi o utenti |
| **Politiche** | Documenti che definiscono le autorizzazioni |
| **Principio** | Privilegio minimo, separazione dei compiti |
### Protezione dei dati
- **Crittografia a riposo**: KMS, chiavi gestite dal cliente, HSM.
- **Crittografia in transito**: TLS/SSL, HTTPS.
- **Gestione dei segreti**: Gestione dei segreti, Key Vault: mai i segreti codificati.
---

## DevOps nel cloud
### Infrastruttura come codice (IaC)
| Strumento | Descrizione |
|------|-------------|
| **Terraforma** | Multi-cloud, HCL dichiarativo, gestione dello stato |
| **CloudFormation** | Modelli YAML/JSON nativi AWS |
| **Modelli BRACCIO / Bicipiti** | Nativo di Azure |
| **Pulumi** | Infrastruttura che utilizza linguaggi di programmazione (Python, Go, ecc.) |
### Servizi CI/CD
| Fornitore | Strumenti |
|----------|-------|
| **AWS** | CodePipeline, CodeBuild, CodeDeploy |
| **Azzurro** | Azure DevOps, azioni GitHub |
| **GCP** | Creazione nel cloud, distribuzione nel cloud |
| **Di terze parti** | Jenkins, CircleCI, GitLab CI |
### Monitoraggio e osservabilità
| Capacità | AWS | Azzurro | PCG |
|-----------|-----|-------|-----|
| **Metriche** | CloudWatch | Monitoraggio di Azure | Monitoraggio del cloud |
| **Registrazione** | Log di CloudWatch | Analisi dei registri | Registrazione nel cloud |
| **Tracciamento** | Raggi X | Approfondimenti sull'applicazione | Traccia nuvola |
---

## Gestione dei costi
### Modelli di prezzo
| Modello | Descrizione | Ideale per |
|-------|-------------|----------|
| **Su richiesta** | Paga quello che consumi, al secondo/ora | Carichi di lavoro variabili e a breve termine |
| **Istanze riservate** | Impegno di 1–3 anni, sconto significativo | Carichi di lavoro in stato stazionario |
| **Istanze Spot** | Offerta per capacità non utilizzata; può essere interrotto | Lavori flessibili e tolleranti ai guasti |
| **Piani di risparmio** | Prezzi con impegno flessibile | Modelli di utilizzo misti |
| **Livello gratuito** | Utilizzo gratuito limitato per i nuovi account | Apprendimento, prototipazione |
### Strategie di ottimizzazione
Istanze delle dimensioni giuste per soddisfare i carichi di lavoro. Utilizza la scalabilità automatica per gestire i picchi di domanda. Riservare capacità per carichi prevedibili. Utilizza istanze spot per processi batch. Sposta i dati a cui si accede raramente su livelli di storage più economici. Elimina le risorse inutilizzate (snapshot orfani, bilanciatori del carico inattivi, IP non collegati).
---

## Alta disponibilità e ripristino di emergenza
### Concetti di disponibilità
| Concetto | Descrizione |
|---------|-----|
| **Zona di disponibilità (AZ)** | Data center fisicamente separati all'interno di una regione |
| **Regione** | Area geografica con più AZ |
| **Posizione bordo** | Posizione della cache CDN per la distribuzione dei contenuti |
### Strategie di ripristino di emergenza
| Strategia | Costo | RTO | RPO | Descrizione |
|----------|------|-----|-----|-----|
| **Backup e ripristino** | Più basso | Ore | Ore–giorni | Backup periodici, ripristino quando necessario |
| **Luce pilota** | Basso | Minuti–ore | Minuti | Gli elementi principali sono sempre attivi, aumentano in caso di disastro |
| **Standby caldo** | Medio | Minuti | Secondi–minuti | Versione ridotta sempre in esecuzione |
| **Multisito attivo/attivo** | Più alto | Vicino allo zero | Zero | Produzione completa in più regioni |
**RTO** (Recovery Time Objective) = tempo di inattività massimo accettabile. **RPO** (Recovery Point Objective) = massima perdita di dati accettabile.
---

## Tendenze emergenti
| Tendenza | Cosa sta succedendo |
|-------|-----------------|
| **Edge computing** | Elaborazione dei dati più vicino alla fonte (AWS Outposts, Wavelength, Azure Edge) |
| **Multicloud** | Evitare il vincolo del fornitore; sfruttare l'eccellenza tra i fornitori |
| **Servizi IA/ML** | Modelli pre-addestrati (visione, parola, linguaggio) + formazione personalizzata (SageMaker, Vertex AI) |
| **Informatica quantistica** | Servizi sperimentali in fase iniziale (AWS Braket, Azure Quantum) |
| **Cloud sostenibile** | Monitoraggio dell'impronta di carbonio, impegni per l'energia rinnovabile, architettura verde |