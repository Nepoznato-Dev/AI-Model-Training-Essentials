---
# Metadata
title: "Technology and Computing"
description: "Computing basics, internet, databases, cloud, security"
category: "General Reference"
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
reviewed_by: "General Reference Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [technology, computing, general-reference]
difficulty_level: "beginner"
prerequisites: []
estimated_reading_time: "8 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Tecnologia e informatica
L'informatica è ovunque: nel telefono, nell'auto, nel frigorifero, nei dispositivi medici e nell'infrastruttura che gestisce la società moderna. Non è necessario essere un programmatore per trarre vantaggio dalla comprensione di come funziona il tutto. Questo file copre gli aspetti fondamentali: cos'è un computer, come funziona Internet, come viene creato il software e i concetti che modellano il mondo digitale.
> **Vuoi approfondire?** Questo file offre un'ampia panoramica. Per una trattazione dettagliata di qualsiasi argomento, consulta i file dedicati in[`01_coding_and_technology/`](../01_coding_and_technology/)— inclusi[web development](../01_coding_and_technology/web_development.md),[database systems](../01_coding_and_technology/database_systems.md),[cloud architecture](../01_coding_and_technology/cloud_architecture.md),[networking](../01_coding_and_technology/networking_basics.md)e[security](../01_coding_and_technology/security_best_practices.md).
---

## Cos'è un computer?
Fondamentalmente, ogni computer, dallo smartphone al supercomputer, fa la stessa cosa: prende input, li elabora secondo istruzioni (un programma) e produce output. La magia sta nella velocità e nella scala.
### L'architettura di Von Neumann
Quasi tutti i computer moderni seguono questo design di base:
| Componente | Cosa fa | Analogia |
|-----------|-------------|---------|
| **CPU** (Unità Centrale di Elaborazione) | Esegue le istruzioni; il "cervello" | Lo chef seguendo una ricetta |
| **RAM** (Memoria) | Memorizza i dati utilizzati attivamente dalla CPU; perso quando si spegne | Il piano di lavoro: accesso rapido, spazio limitato |
| **Archiviazione** (SSD/HDD) | Memorizza i dati in modo permanente | La dispensa: accesso più lento, molto più spazio |
| **Ingresso/Uscita** | Tastiera, mouse, schermo, rete | Come lo chef riceve gli ordini e consegna il cibo |
| **GPU** (Unità di elaborazione grafica) | Processore specializzato per attività parallele (grafica, AI) | Un team di assistenti che svolgono tutti lo stesso compito contemporaneamente |
**Approfondimento chiave**: la RAM è veloce ma temporanea. L'archiviazione è lenta ma permanente. Quando il tuo computer "sembra lento", spesso è perché sta esaurendo la RAM e deve utilizzare l'archiviazione come memoria temporanea (scambio), che è molto più lenta.
---

## Linguaggi di programmazione: parlare con i computer
Un linguaggio di programmazione è un insieme di istruzioni che un computer può eseguire. Lingue diverse sono progettate per scopi diversi. Per una copertura dettagliata di 34 lingue individuali, vedere la cartella [`programming_languages/`](../01_coding_and_technology/programming_languages/).
| Lingua | Ideale per | Perché sceglierlo |
|----------|---------|---------------|
| **Pitone** | Scienza dei dati, intelligenza artificiale, automazione, backend web | Sintassi semplice; enorme ecosistema; ottimo per i principianti |
| **JavaScript** | Frontend Web, stack completo (Node.js) | Funziona in ogni browser; essenziale per lo sviluppo web |
| **Java** | Software aziendale, app Android | Indipendente dalla piattaforma (JVM); grande ecosistema |
| **C/C++** | Programmazione di sistemi, giochi integrati | Massime prestazioni; controllo hardware diretto |
| **Ruggine** | Programmazione di sistemi con garanzie di sicurezza | Sicurezza della memoria senza garbage collection |
| **Vai** | Servizi cloud, microservizi, strumenti CLI | Semplice; eccellente concorrenza; compilazione veloce |
| **SQL** | Query del database | Il linguaggio universale per lavorare con i dati |
| **Script dattiloscritto** | Applicazioni web su larga scala | JavaScript con controllo del tipo; rileva i bug in anticipo |
---

## Come funziona Internet
Internet non è la stessa cosa del web. Internet è la rete fisica: cavi, router, server e protocolli che collegano miliardi di dispositivi. Il World Wide Web è un servizio che funziona su Internet (insieme a posta elettronica, trasferimento di file, streaming, giochi, ecc.).
### Il viaggio di una richiesta web
Quando digiti`https://www.example.com`nel browser:
1. **Ricerca DNS**: il tuo browser chiede a un server DNS di tradurre "www.example.com" in un indirizzo IP (come 93.184.216.34).
2. **Connessione TCP**: il dispositivo stabilisce una connessione a quell'indirizzo IP utilizzando TCP (un protocollo che garantisce una consegna affidabile).
3. **Handshake TLS**: se utilizzi HTTPS, il tuo browser e il server negoziano una connessione crittografata.
4. **Richiesta HTTP**: il tuo browser invia una richiesta: "Dammi la pagina su /index.html."
5. **Elaborazione del server**: il server web trova la pagina, eventualmente interroga un database e prepara una risposta.
6. **Risposta HTTP**: il server restituisce HTML, CSS e JavaScript.
7. **Rendering**: il tuo browser analizza l'HTML, applica gli stili CSS ed esegue JavaScript per visualizzare la pagina.
L'intero processo richiede in genere meno di un secondo.
### Protocolli chiave
| Protocollo | Cosa fa | Strato |
|----------|-------------|-------|
| **IP** (Protocollo Internet) | Instrada i pacchetti tra le reti | Rete |
| **TCP** | Consegna affidabile e ordinata (ritrasmette i pacchetti persi) | Trasporti |
| **UDP** | Consegna veloce e inaffidabile (nessuna ritrasmissione) | Trasporti |
| **HTTP/HTTPS** | Trasferimento di pagine Web (HTTPS aggiunge crittografia) | Applicazione |
| **DNS** | Traduce i nomi di dominio in indirizzi IP | Applicazione |
| **SSH** | Accesso remoto sicuro ai computer | Applicazione |
| **SMTP/IMAP** | Invio e ricezione di e-mail | Applicazione |
---

## Sviluppo software: come vengono creati i programmi
### Il processo di sviluppo
1. **Scrivi codice**: gli sviluppatori scrivono istruzioni in un linguaggio di programmazione.
2. **Codice di prova**: esegui il codice per verificare che funzioni correttamente.
3. **Controllo della versione**: tieni traccia delle modifiche utilizzando Git, lo standard universale.
4. **Revisione**: altri sviluppatori controllano gli errori e la qualità del codice.
5. **Build**: converte il codice sorgente in un programma eseguibile (compilazione).
6. **Distribuisci**: rilascia il programma agli utenti (server, app store, ecc.).
7. **Monitoraggio**: verifica errori e problemi di prestazioni nella produzione.
### Concetti chiave
| Concetto | Cosa significa | Perché è importante |
|---------|---------------|----------------|
| **Controllo della versione (Git)** | Tieni traccia di ogni modifica al codice nel tempo | Collaborazione; capacità di annullare gli errori |
| **API** (interfaccia di programmazione dell'applicazione) | Un modo definito per comunicare tra i componenti software | Consente a diversi sistemi di lavorare insieme |
| **Banca dati** | Archiviazione organizzata per i dati | Ogni applicazione deve archiviare e recuperare dati |
| **Test** | Controlli automatizzati che il codice funzioni correttamente | Impedisce ai bug di raggiungere gli utenti |
| **CI/CD** (Integrazione/Consegna continua) | Pipeline automatizzata dal commit del codice alla produzione | Rilasci più rapidi e sicuri |
| **Containerizzazione (Docker)** | Crea un pacchetto di un'applicazione con tutte le sue dipendenze | "Funziona sulla mia macchina" diventa "funziona ovunque" |
---

## Database: dove risiedono i dati
Ogni applicazione deve archiviare dati. I database sono i sistemi che lo fanno in modo efficiente e affidabile.
| Digitare | Come vengono archiviati i dati | Ideale per | Esempi |
|------|-------------|----------|---------|
| **Relazionale (SQL)** | Tabelle con righe e colonne; schema rigoroso | Dati strutturati; query complesse; transazioni | PostgreSQL, MySQL, SQLite |
| **Documento (NoSQL)** | Documenti simili a JSON; schema flessibile | Dati semistrutturati; iterazione rapida | MongoDB, CouchDB |
| **Valore-chiave** | Chiave semplice → coppie di valori | memorizzazione nella cache; archiviazione della sessione; ricerche veloci | Redis, DynamoDB |
| **Grafico** | Nodi e spigoli (relazioni) | Reti sociali; motori di raccomandazione | Neo4j, JanusGraph |
| **Serie storica** | Ottimizzato per dati con timestamp | Monitoraggio; analisi; IoT | DB afflusso, DB scala temporale |
**SQL** (Structured Query Language) è il linguaggio standard per i database relazionali. È una delle competenze tecniche più preziose che puoi apprendere: quasi tutte le organizzazioni utilizzano database e SQL è il modo in cui comunichi con loro.
---

## Sistemi operativi
Il sistema operativo (OS) è lo strato software tra te (e i tuoi programmi) e l'hardware. Gestisce memoria, processi, file e dispositivi.
| Sistema operativo | Dove domina | Caratteristica fondamentale |
|----|-------------|-----|
| **Finestre** | PC desktop/laptop (quota di mercato ~72%) | La più ampia compatibilità software/hardware |
| **macOS** | Professionisti creativi, sviluppatori | Basato su Unix; interfaccia utente raffinata; Ecosistema Apple |
| **Linux** | Server (~96%), supercomputer (100%), embedded, sviluppatori | Fonte aperta; gratuito; estremamente personalizzabile |
| **Android** | Mobile (quota di mercato globale ~72%) | Basato sul kernel Linux; open source |
| **iOS** | Mobile (~27% globale, ma ricavi più elevati) | Ecosistema chiuso; lucido; incentrato sulla privacy |
Linux merita una menzione speciale: alimenta la maggior parte di Internet, tutti i supercomputer top 500, la maggior parte delle infrastrutture cloud e tutti i telefoni Android. È gratuito, open source e gestito da una comunità globale.
---

##Il cloud computing
Il cloud computing significa noleggiare risorse informatiche (server, spazio di archiviazione, database, ecc.) su Internet invece di acquistare e mantenere il proprio hardware. Per una guida completa all'architettura cloud, ai modelli di servizio e ai confronti tra fornitori, consulta[cloud architecture](../01_coding_and_technology/cloud_architecture.md).
| Modello di servizio | Cosa ottieni | Analogia | Esempi |
|---------------|-----|---------|---------|
| **IaaS** (Infrastrutture) | Server virtuali, storage, reti | Affittare un terreno e costruire ciò che desideri | AWS EC2, Google Compute Engine |
| **PaaS** (Piattaforma) | Ambiente di esecuzione; porti il ​​codice | Affittare un appartamento ammobiliato | Heroku, Google App Engine |
| **SaaS** (Software) | Applicazione completa; lo usi e basta | Soggiornare in un albergo | Gmail, Slack, Salesforce |
I tre principali fornitori di servizi cloud sono **AWS** (Amazon, quota di mercato ~32%), **Azure** (Microsoft, ~23%) e **GCP** (Google, ~10%). Offrono centinaia di servizi che coprono elaborazione, archiviazione, database, intelligenza artificiale, rete e altro ancora.
---

## Sicurezza informatica: protezione dei sistemi digitali
La sicurezza informatica è la pratica di difendere computer, reti e dati dagli attacchi. È importante perché tutto è connesso e il costo delle violazioni è enorme. Per una guida completa che copre OWASP Top 10, ciclo di vita di sviluppo sicuro e gestione dei segreti, vedere[security best practices](../01_coding_and_technology/security_best_practices.md).
### Minacce comuni
| Minaccia | Cos'è | Prevenzione |
|--------|-----------|----|
| **Malware** | Software dannoso (virus, worm, trojan) | antivirus; mantenere aggiornato il software |
| **Phishing** | Email/messaggi falsi che ti inducono a rivelare informazioni | Formazione; filtraggio della posta elettronica; scetticismo |
| **Ransomware** | Crittografa i tuoi dati; esige il pagamento della chiave | Backup; sistemi di patch; non pagare |
| **DDoS** | Travolge un servizio con traffico | Filtraggio del traffico; Protezione CDN |
| **Iniezione SQL** | Inserimento di SQL dannoso nei campi di input | Query parametrizzate; convalida dell'input |
| **Uomo nel mezzo** | Intercettare la comunicazione tra due parti | Crittografia HTTPS/TLS |
### Fondamenti di sicurezza
- **Crittografia**: codifica i dati in modo che solo le parti autorizzate possano leggerli. HTTPS utilizza TLS per crittografare il traffico web.
- **Autenticazione**: verifica l'identità. Utilizza l'autenticazione a più fattori (MFA): password + qualcos'altro (codice, biometrico).
- **Autorizzazione**: verifica le autorizzazioni. Solo perché hai effettuato l'accesso non significa che dovresti accedere a tutto.
- **Principio del privilegio minimo**: concedere agli utenti e ai sistemi solo l'accesso di cui hanno bisogno, niente di più.
- **Gestione patch**: mantieni aggiornato il software. La maggior parte delle violazioni sfrutta vulnerabilità note che dispongono già di patch.
---

## Formati di dati
I programmi scambiano dati in formati specifici. Il più comune:
| Formato | Struttura | Usato per |
|--------|-----------|----------|
| **JSON** | Coppie chiave-valore; leggibile dall'uomo | API; configurazione; scambio dati |
| **XML** | Basato su tag; prolisso ma flessibile | Sistemi legacy; documenti; API SOAP |
| **YAML** | Basato sul rientro; molto leggibile | Configurazione (Docker, Kubernetes, CI/CD) |
| **CSV** | Righe e colonne di testo semplice | Importazione/esportazione dati; fogli di calcolo |
---

## Riepilogo
L’informatica non è magia: è ingegneria. I computer seguono le istruzioni a una velocità incredibile. Internet ne collega miliardi utilizzando protocolli standardizzati. Il software è creato da team di persone che scrivono, testano e distribuiscono codice in cicli iterativi. I database archiviano e recuperano i dati. Il cloud computing consente a chiunque di accedere a enormi risorse informatiche su richiesta. E la sicurezza informatica è la battaglia in corso per tenere tutto questo al sicuro dalle persone che vogliono sfruttarlo. Comprendere questi fondamenti ti aiuta a navigare nel mondo digitale, che tu sia un utente, uno sviluppatore o semplicemente qualcuno che cerca di dare un senso alla tecnologia che modella la vita moderna.