<!--
---
# Metadata
title: "Software Architecture Patterns"
description: "Monolith, microservices, event-driven, DDD, caching, SOLID"
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
tags: [software, architecture, patterns, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "9 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Modelli di architettura software
L’architettura è l’insieme delle decisioni strutturali su come è organizzato un sistema: quali componenti ha, come comunicano e dove si trovano le responsabilità. Una buona architettura rende un sistema facile da comprendere, modificare e scalare. La cattiva architettura rende ogni cambiamento una lotta. Questo file copre i modelli principali, quando utilizzarli e i compromessi coinvolti.
---

## Monolite vs microservizi
Questa è la decisione architettonica più fondamentale e vale la pena prenderla nel modo giusto.
| Aspetto | Monolite | Microservizi |
|--------|----------|---------------|
| **Struttura** | Unità singola dispiegabile | Molti piccoli servizi distribuibili in modo indipendente |
| **Dati** | Database condiviso | Ogni servizio possiede i propri dati |
| **Comunicazione** | Chiamate di funzioni in-process | Chiamate di rete (HTTP, gRPC, messaggistica) |
| **Ridimensionamento** | Ridimensiona l'intera applicazione | Servizi individuali scala |
| **Distribuzione** | Ciclo di rilascio singolo | Distribuzioni indipendenti |
| **Complessità** | Più semplice da sviluppare inizialmente | Complessità operativa (rete, monitoraggio) |
| **Ideale per** | Piccoli team, prodotti in fase iniziale | Team grandi, domini complessi, scala elevata |
### Quando iniziare con un monolite
La maggior parte delle applicazioni dovrebbe iniziare come monolite. È più semplice creare, testare, distribuire ed eseguire il debug. Puoi sempre estrarre i servizi in un secondo momento quando avrai un quadro più chiaro dei confini del tuo dominio. Questo a volte viene chiamato "monolite modulare" - un monolite con confini interni puliti che ne facilitano l'estrazione in seguito.
### Quando passare ai microservizi
Prendi in considerazione i microservizi quando:
- Le squadre sono abbastanza grandi da rendere il coordinamento un collo di bottiglia.
- Parti diverse del sistema hanno requisiti di ridimensionamento molto diversi.
- È necessaria una distribuzione indipendente dei componenti.
- Il tuo dominio ha contesti delimitati chiari (vedi DDD di seguito).
---

## Architettura a più livelli (N-tier)
Il modello architettonico più comune. Il codice è organizzato in livelli, ciascuno con una responsabilità specifica.
```
â”Œ─────────────────────────┐
│   Presentation Layer    │  ← UI, controllers, API endpoints
├─────────────────────────┤
│   Application Layer     │  ← Use cases, orchestration
├─────────────────────────┤
│   Domain Layer          │  ← Business logic, entities
├─────────────────────────┤
│   Infrastructure Layer  │  ← Database, external services, file I/O
└─────────────────────────┘
```

| Strato | Responsabilità | Regola |
|-------|-------|------|
| **Presentazione** | Gestire le richieste utente/HTTP | Può chiamare solo il livello Applicazione |
| **Applicazione** | Orchestrare casi d'uso | Può chiamare il livello di dominio |
| **Dominio** | Logica aziendale principale | Non dovrebbe dipendere da altri livelli |
| **Infrastrutture** | Preoccupazioni tecniche | Implementa le interfacce definite in Dominio |
**Regola chiave**: le dipendenze puntano verso l'interno. Il livello Dominio non conosce il database o il framework web.
---

## Architettura guidata dagli eventi
I componenti comunicano emettendo e reagendo a **eventi**: cose che sono accadute.
| Modello | Descrizione |
|---------|-----|
| **Notifica evento** | Il servizio A emette "OrderPlaced"; i servizi B, C, D reagiscono |
| **Fonte di eventi** | Memorizza tutti i cambiamenti di stato come una sequenza di eventi (non solo lo stato corrente) |
| **CQRS** | Separa il modello di lettura (query) dal modello di scrittura (comandi) |
### Origine eventi
Invece di archiviare lo "stato corrente" in un database, archivia ogni modifica di stato come un evento:
```
OrderCreated(order_id=123, total=$50)
OrderPaid(order_id=123, payment_id=456)
OrderShipped(order_id=123, tracking=ABC)
```

Vantaggi: traccia di controllo completa, capacità di ricostruire qualsiasi stato passato, consumatori disaccoppiati. Sfide: evoluzione dello schema degli eventi, eventuale coerenza, complessità del debug.
### CQRS (Segregazione delle responsabilità delle query di comando)
| Lato | Scopo | Banca dati |
|------|---------|----------|
| **Comando (Scrivi)** | Gestire le mutazioni; applicare le regole aziendali | Ottimizzato per le scritture (normalizzato) |
| **Query (lettura)** | Servire richieste di lettura | Ottimizzato per le letture (denormalizzato) |
CQRS si abbina naturalmente all'Event Sourcing: gli eventi dal lato della scrittura vengono proiettati in visualizzazioni ottimizzate per la lettura.
---

## Code di messaggi e broker di eventi
Quando i servizi devono comunicare in modo asincrono, le code di messaggi rappresentano la spina dorsale.
| Strumento | Digitare | Ideale per |
|------|------|----------|
| **Apache Kafka** | Registro eventi distribuito | Streaming di eventi ad alto rendimento, sourcing di eventi |
| **ConiglioMQ** | Broker di messaggi con routing | Code di attività, schemi di routing complessi |
| **AWS SQS** | Coda gestita | Accodamento semplice, nativo di AWS |
| **SNS AWS** | Notifica di pubblicazione/sottoscrizione | Fan-out a più abbonati |
| **Google Pub/Sub** | Pub/sub gestito | Streaming di eventi nativi GCP |
| **Stream Redis** | Flusso leggero | Semplice registrazione degli eventi e casi d'uso di memorizzazione nella cache |
### Modelli di messaggistica
| Modello | Descrizione |
|---------|-----|
| **Punto a punto** | Un produttore, un consumatore per messaggio |
| **Pubblica/Iscriviti** | Un produttore, più abbonati |
| **Richiesta/Rispondi** | Stile sincrono su trasporto asincrono |
| **Coda di lettere non consegnate** | I messaggi che non riescono ad essere elaborati vanno in una coda separata per l'ispezione |
---

## Progettazione guidata dal dominio (DDD)
DDD è un approccio strategico alla progettazione del software che centra il codice attorno a concetti aziendali piuttosto che a questioni tecniche.
### Concetti chiave
| Concetto | Descrizione |
|---------|-----|
| **Contesto limitato** | Un confine entro il quale un modello di dominio è coerente (ad esempio, "Ordinazione", "Spedizione", "Fatturazione") |
| **Lingua onnipresente** | Vocabolario condiviso tra sviluppatori ed esperti di dominio |
| **Aggregati** | Cluster di entità correlate trattati come una singola unità per le modifiche dei dati |
| **Enti** | Oggetti con identità (ad esempio, un Utente con un user_id) |
| **Oggetti valore** | Oggetti senza identità; definiti dai loro attributi (ad esempio, Money, Address) |
| **Eventi del dominio** | Qualcosa che è accaduto nel dominio (ad esempio, OrderPlaced) |
| **Livello anticorruzione** | Livello di traduzione tra il tuo dominio e i sistemi esterni |
### Quando DDD aiuta
Il DDD è più prezioso quando l'ambito aziendale è complesso: si pensi all'e-commerce, alla logistica, ai servizi finanziari, all'assistenza sanitaria. Se il tuo dominio è semplice (un blog, un'app di cose da fare), DDD è eccessivo.
---

## Strategie di memorizzazione nella cache
La memorizzazione nella cache è uno dei modi più efficaci per migliorare le prestazioni, ma introduce complessità in termini di coerenza.
| Strategia | Descrizione | Scambio |
|----------|-------------|-----------|
| **Cache-Aside** | L'applicazione controlla prima la cache; caricamenti da DB in caso di mancata | Semplice; eventuale consistenza |
| **Write-Through** | Scrivi contemporaneamente nella cache e nel DB | Coerente; più lento scrive |
| **Scrivi dietro** | Scrivi nella cache; scrittura asincrona su DB | Scritture veloci; rischio di perdita di dati |
| **Leggi attentamente** | Caricamenti della cache dal DB in caso di errore in modo trasparente | Più semplice del cache-aside |
### Cosa memorizzare nella cache
| Strato | Cosa | Strumenti |
|-------|------|-------|
| **CDN** | Asset statici, risposte API | CloudFront, Cloudflare |
| **Applicazione** | Risultati calcolati, dati della sessione | Redis, Memcached |
| **Banca dati** | Risultati della query, righe a cui si accede frequentemente | Cache delle query, viste materializzate |
**L'invalidazione della cache** è notoriamente difficile. Strategie comuni: TTL (time-to-live), invalidazione guidata dagli eventi (svuotare la cache in caso di modifica dei dati) ed eliminazione LRU (utilizzata meno recentemente).
---

## Modelli di progettazione
### Principi SOLIDI
| Principio | Cosa significa |
|-----------|--------------|
| **S** — Responsabilità unica | Una classe dovrebbe avere un motivo per cambiare |
| **O** — Aperto/Chiuso | Aperto per estensione, chiuso per modifica |
| **L** — Sostituzione Liskov | I sottotipi dovrebbero essere sostituibili con i loro tipi base |
| **I** — Segregazione delle interfacce | Molte interfacce specifiche > un'interfaccia generica |
| **D** — Inversione delle dipendenze | Dipendono dalle astrazioni, non dalle concrezioni |
### Modelli comuni
| Modello | Intento | Esempio |
|---------|--------|---------|
| **Singolo** | Assicurati che una classe abbia solo un'istanza | Pool di connessioni al database |
| **Fabbrica** | Crea oggetti senza specificare la classe esatta | `UserFactory.create(type="admin")`|
| **Osservatore** | Notifica ai dipendenti quando lo stato cambia | Ascoltatori di eventi, pub/sub |
| **Strategia** | Scambia algoritmi in fase di esecuzione | Strategia di pagamento: carta di credito, PayPal, criptovaluta |
| **Archivio** | Accesso ai dati astratti dietro un'interfaccia pulita | `UserRepository.find_by_id(123)`|
| **Decoratore** | Aggiungi comportamento in modo dinamico | Decoratore di registrazione attorno a un servizio |
| **Adattatore** | Far funzionare insieme le interfacce incompatibili | Adattatore API legacy |
---

## Scegliere la giusta architettura
Non esiste un'architettura universalmente "migliore". La scelta giusta dipende da:
| Fattore | Favorisci il monolite quando... | Privilegiare i microservizi quando... |
|--------|-----------------------|------------------------------|
| **Dimensione della squadra** | < 10 developers | >20 sviluppatori, più team |
| **Complessità del dominio** | Semplice o ben compreso | Contesti complessi e con molti limiti |
| **Requisiti di scala** | Esigenze di ridimensionamento uniformi | Componenti diversi necessitano di scale diverse |
| **Ccadenza di distribuzione** | Ciclo di rilascio singolo | Sono necessarie implementazioni indipendenti |
| **Diversità tecnologica** | Uno stack va bene | Servizi diversi necessitano di tecnologie diverse |
**Consiglio pratico**: inizia con un monolite modulare. Estrai i servizi solo quando hai una necessità chiara e chiari i confini del dominio. I microservizi prematuri sono uno degli errori architetturali più comuni nel settore.