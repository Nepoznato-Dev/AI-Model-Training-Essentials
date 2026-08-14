---
# Metadata
title: "API Design and Integration Failures"
description: "API anti-patterns, breaking changes, versioning failures, cascading failures"
category: "Lessons from Failures"
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
reviewed_by: "Lessons from Failures Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [api, design, integration, failures, lessons-from-failures]
difficulty_level: "advanced"
prerequisites: []
estimated_reading_time: "6 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Errori di progettazione e integrazione dell'API
Le API (Application Programming Interfaces) sono il tessuto connettivo del software moderno: consentono ai servizi di comunicare, consentono a terze parti di integrarsi e consentono ai team di lavorare in modo indipendente. Quando la progettazione dell'API va male, le conseguenze si propagano a tutti i sistemi che ne dipendono: integrazioni interrotte, vulnerabilità della sicurezza, frustrazione degli sviluppatori e costose riscritture. Gli errori di integrazione, ovvero i sistemi che non riescono a comunicare in modo affidabile, sono tra le fonti più comuni di incidenti di produzione.
---

## Errori comuni nella progettazione delle API
### Errori di progettazione
| Errore | Descrizione | Conseguenza |
|---------|-----|-----|
| **Nominazione incoerente** | `/getUsers`contro`/list_users`contro`/fetch-users`| Confusione; errori; sviluppo lento |
| **Endpoint sovraccarichi** | Un endpoint che fa 10 cose diverse in base ai parametri | Difficile da capire; difficile da testare; difficile cambiare |
| **Sottorecupero** | Il cliente deve effettuare 5 chiamate API per ottenere i dati correlati | Lento; dispendioso; codice cliente complesso |
| **Recupero eccessivo** | L'API restituisce tutti i campi quando il client necessita solo di 2 | Larghezza di banda sprecata; lento sui dispositivi mobili; rischio per la sicurezza (esposizione di dati non necessari) |
| **Nessun controllo delle versioni** | Modifiche importanti implementate senza preavviso | I clienti si rompono; sviluppatori arrabbiati |
| **Messaggi di errore vaghi** | "Errore 500: errore interno del server" senza dettagli | Impossibile eseguire il debug; risoluzione lenta |
| **Impaginazione mancante** | L'endpoint restituisce tutti i record (potrebbero essere milioni) | Timeout; esaurimento della memoria; client in crash |
| **Codici di stato incoerenti** | 200 OK per errori; 500 per errori del cliente | I clienti non riescono a distinguere il successo dal fallimento |
### Anti-pattern API REST
| Anti-modello | Descrizione | Approccio migliore |
|-------------|-------------|-----------|
| **Utilizzo di GET per le mutazioni** | `GET /delete-user?id=5`| Utilizzare il metodo DELETE |
| **Utilizzare POST per tutto** | `POST /get-users`; `POST /update-user`| Utilizzare metodi HTTP appropriati (GET, POST, PUT, PATCH, DELETE) |
| **Restituzione di HTML dall'API** | L'API restituisce frammenti HTML | Restituisce JSON; lascia che il client esegua il rendering |
| **Logica aziendale negli URL** | `/users/active/premium/from-2023`| Utilizza parametri di query o corpo della richiesta per filtri complessi |
| **Esposizione dello schema del database** | `/api/table_name/column`| Progetta API in base a risorse e concetti di dominio, non a tabelle |
| **Nessun HATEOAS/link** | Il client codifica tutti gli URL | Includere collegamenti a risorse correlate nelle risposte |
---

## Errori di sicurezza
### Vulnerabilità API comuni
| Vulnerabilità | Descrizione | Esempio |
|--------------|-----|---------|
| **Autenticazione interrotta** | L'API non verifica correttamente l'identità | Convalida del token mancante; token scaduti accettati |
| **Esposizione eccessiva dei dati** | L'API restituisce più dati di quelli necessari al cliente | L'endpoint utente restituisce gli hash delle password e gli ID interni |
| **Assegnazione di massa** | Il cliente può impostare campi che non dovrebbe | `PATCH /user`consente di impostare`role: "admin"`|
| **Iniezione** | Input dell'utente interpretato come codice | Iniezione SQL; Iniezione NoSQL; comando iniezione |
| **IDOR** (riferimento oggetto diretto non sicuro) | Accesso alle risorse modificando l'ID nell'URL | `/api/users/5`→ cambia in`/api/users/6`per vedere i dati di qualcun altro |
| **Limitazione della velocità mancante** | Nessun limite alle chiamate API | Forza bruta; rifiuto del servizio; raschiando |
| **Configurazione errata CORS** | Accesso multiorigine eccessivamente permissivo | `Access-Control-Allow-Origin: *`sugli endpoint autenticati |
### Errori di autenticazione e autorizzazione
| Fallimento | Descrizione | Impatto |
|---------|-----|--------|
| **Credenziali hardcoded** | Chiavi API o password nel codice sorgente | Trapelato attraverso il controllo della versione; accessibile a tutti gli sviluppatori |
| **Nessuna scadenza del token** | I token non scadono mai | Il token rubato dà accesso permanente |
| **Chiavi segrete deboli** | Chiavi di firma brevi o prevedibili | I gettoni possono essere forgiati |
| **Nessun ambito/permessi** | Tutti i token hanno pieno accesso | Token compromesso = accesso completo al sistema |
| **Registrazione dei dati sensibili** | Token o password nei log | Accessibile a chiunque abbia accesso al registro |
| **Autorizzazione incoerente** | Alcuni endpoint controllano le autorizzazioni; altri no | Accesso non autorizzato tramite endpoint non custoditi |
---

## Errori di integrazione
### Problemi di integrazione del sistema distribuito
| Fallimento | Descrizione | Esempio |
|---------|-----|---------|
| **Accoppiamento stretto** | I servizi dipendono reciprocamente dai dettagli di implementazione interna | La modifica del database di un servizio ne danneggia altri tre |
| **Catene sincrone** | Il servizio A chiama B chiama C chiama D; la latenza si accumula | 200 ms + 300 ms + 500 ms = tempo di risposta 1 secondo |
| **Nessun interruttore automatico** | Un servizio inadeguato provoca errori a catena | Il servizio D è lento; tutti i servizi upstream esauriscono i propri thread in attesa |
| **Nessuna logica di ripetizione** | I guasti temporanei diventano permanenti | Blip di rete = transazione fallita; l'utente deve riprovare manualmente |
| **Numeri tentativi** | I nuovi tentativi senza backoff sovraccaricano il ripristino dei servizi | Problema della mandria tuonante |
| **Nessuna idepotenza** | Il nuovo tentativo di un'operazione non idempotente crea duplicati | Pagamento addebitato due volte; ordine creato due volte |
| **L'eventuale coerenza sorprende** | Il client legge i dati non aggiornati dopo una scrittura | Profilo degli aggiornamenti dell'utente; aggiorna la pagina; vecchi dati ancora mostrati |
### Errori di integrazione di terze parti
| Fallimento | Descrizione | Mitigazione |
|---------|-----|------------|
| **Modifiche all'API del fornitore** | Terze parti modificano la propria API senza preavviso | Blocco della versione; livello di astrazione; monitoraggio dei log delle modifiche dei fornitori |
| **Limitazione della velocità** | Le terze parti limitano le tue richieste | memorizzazione nella cache; richiedere la coda; negoziare limiti più elevati |
| **Tempi di inattività del fornitore** | Il servizio di terze parti non è disponibile | Interruttori automatici; comportamento di riserva; strategia multi-vendor |
| **Modifiche al formato dei dati** | Le terze parti modificano il formato della risposta | Convalida dello schema; strato di trasformazione; avvisi sui cambiamenti di formato |
| **Ritiro senza percorso di migrazione** | Il fornitore depreca l'endpoint senza equivalente | Rimani informato; mantenere l'astrazione; pianificare le migrazioni in anticipo |
---

## Casi di studio
### Caso di studio 1: L'API che ha restituito tutto
| Aspetto | Descrizione |
|--------|-------------|
| **Scenario** | L'API utente di un'azienda SaaS ha restituito tutti i campi utente inclusi i metadati interni |
| **Cosa è andato storto** | Nessun filtraggio del campo; la risposta includeva hash delle password, note interne e flag di amministrazione |
| **Impatto** | I ricercatori di sicurezza hanno scoperto l'esposizione; divulgazione pubblica; Indagine GDPR |
| **Causa principale** | L'API ha serializzato l'intero modello di database senza filtraggio |
| **Correzione** | Modelli di risposta esplicita; controllo degli accessi a livello di campo; revisione della sicurezza di tutti gli endpoint |
| **Lezione** | Non esporre mai il modello di database direttamente tramite un'API; utilizzare DTO (oggetti di trasferimento dati) |
### Caso di studio 2: Il fallimento a cascata
| Aspetto | Descrizione |
|--------|-------------|
| **Scenario** | Un'architettura di microservizi con comunicazione interservizi sincrona |
| **Cosa è andato storto** | Un servizio ha subito un rallentamento del database; i servizi a monte attendevano risposte; pool di thread esauriti |
| **Impatto** | Interruzione completa del sistema per 45 minuti; tutti i servizi interessati |
| **Causa principale** | Nessun interruttore automatico; nessun timeout; catena di dipendenze sincrone |
| **Correzione** | Interruttori automatici; timeout; comunicazione asincrona ove possibile; paratie |
| **Lezione** | Le chiamate sincrone tra servizi creano catene fragili; progettare per il fallimento |
---

## Migliori pratiche
### Elenco di controllo per la progettazione dell'API
| Zona | Pratica |
|------|----------|
| **Nominazione** | Usa nomi per risorse; Metodi HTTP per le azioni; convenzione di denominazione coerente |
| **Versione** | Versione dal primo giorno; utilizzare il controllo delle versioni dell'URL (`/v1/`) o il controllo delle versioni dell'intestazione |
| **Impaginazione** | Paginare sempre gli endpoint dell'elenco; utilizzare l'impaginazione basata su cursore per set di dati di grandi dimensioni |
| **Gestione degli errori** | Formato errore coerente; includere codici di errore; fornire messaggi utilizzabili |
| **Limitazione della velocità** | Implementare limiti di velocità; restituisce 429 con l'intestazione retry-after |
| **Idempotenza** | Supporta le chiavi di idempotenza per gli endpoint di mutazione |
| **Documentazione** | Specifiche OpenAPI/Swagger; tienilo aggiornato; fornire esempi |
| **Test** | Prove contrattuali; test di integrazione; test contrattuali orientati al consumatore |
| **Monitoraggio** | Traccia la latenza; tassi di errore; produttività; salute della dipendenza |
| **Deprecazione** | Annunciare le deprecazioni con largo anticipo; fornire guide alla migrazione |
---

## Riepilogo
Gli errori di progettazione dell'API vanno da quelli cosmetici (denominazione incoerente) a catastrofici (vulnerabilità della sicurezza, errori a cascata). Gli errori di progettazione più comuni (endpoint sovraccarichi, recupero eccessivo, impaginazione mancante, errori vaghi) rendono le API difficili da utilizzare e mantenere. I fallimenti della sicurezza – autenticazione interrotta, IDOR, assegnazione di massa, esposizione eccessiva dei dati – espongono i sistemi ad attacchi. I fallimenti di integrazione – accoppiamento stretto, catene sincrone, interruttori mancanti, assenza di idempotenza – creano sistemi fragili in cui un fallimento si riversa a cascata su tutti i servizi. Le integrazioni di terze parti aggiungono rischi esterni: modifiche API, limitazioni di velocità e tempi di inattività dei fornitori. Le strategie di prevenzione sono consolidate: utilizzare modelli di risposta espliciti; versione dal primo giorno; implementare interruttori automatici e timeout; progettazione per l'idempotenza; convalidare e disinfettare tutti gli input; monitorare tutto; e trattare i contratti API come accordi vincolanti che richiedono coordinamento per cambiare. Le migliori API sono noiose: prevedibili, coerenti, ben documentate e resistenti ai guasti.