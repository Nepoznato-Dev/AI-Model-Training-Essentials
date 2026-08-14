<!--
---
# Metadata
title: "API Design and Architecture"
description: "REST, GraphQL, gRPC, versioning, auth, API gateways"
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
tags: [api, design, architecture, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "10 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Progettazione e architettura API
Un'API (Application Programming Interface) è il modo in cui i componenti software comunicano tra loro. Un'API ben progettata è intuitiva, coerente ed è un piacere lavorarci. Uno progettato male provoca confusione, bug e frustrazione. Questo file copre i principi, i modelli e le pratiche per la creazione di API che gli sviluppatori desiderano effettivamente utilizzare.
---

## Principi dell'API REST
REST (Representational State Transfer) è lo stile architettonico dominante per le API Web. Tratta i dati come **risorse** identificate dagli URL e utilizza metodi HTTP per operare su di essi.
### Principi fondamentali
| Principio | Descrizione |
|-----------|-------------|
| **Risorse** | Tutto è una risorsa con un URI (`/users/123`,`/orders/456`) |
| **Metodi HTTP** | GET (leggi), POST (crea), PUT (sostituisci), PATCH (aggiornamento parziale), DELETE (rimuovi) |
| **Apolidia** | Ogni richiesta contiene tutte le informazioni necessarie; nessuno stato della sessione lato server |
| **Interfaccia uniforme** | Denominazione coerente delle risorse, metodi standard, codici di stato standard |
| **Rappresentazione** | Le risorse possono essere rappresentate in più formati (JSON, XML) |
### Convenzioni per la denominazione delle risorse
| Fare | Non |
|----|-------|
| `/users`(sostantivo plurale) | `/user`(singolare) |
| `/users/123/orders`(nidificato) | `/getOrdersForUser?id=123`|
| `/products?category=electronics`(parametri di query per il filtraggio) | `/productsByCategory/electronics`|
| Usa i trattini:`/user-profiles`| Utilizzare i caratteri di sottolineatura:`/user_profiles`|
### Metodi HTTP e idempotenza
| Metodo | Scopo | Idempotente? | Sicuro? |
|--------|---------|-----|-------|
| **OTTIENI** | Leggi una risorsa | ✅ Sì | ✅ Sì |
| **POST** | Crea una risorsa | ❌No | ❌No |
| **METTERE** | Sostituisci interamente una risorsa | ✅ Sì | ❌No |
| **PATCH** | Aggiorna parzialmente una risorsa | ❌No* | ❌No |
| **ELIMINA** | Rimuovere una risorsa | ✅ Sì | ❌No |
*PATCH può essere reso idempotente con un'attenta progettazione.
### Codici di stato HTTP
| Codice | Significato | Quando usarlo |
|------|---------|-----|
| **200** | Va bene | GET, PUT, PATCH, DELETE riusciti |
| **201** | Creato | POST riuscito (risorsa creata) |
| **204** | Nessun contenuto | DELETE riuscita (niente da restituire) |
| **400** | Richiesta errata | Input non valido o richiesta non valida |
| **401** | Non autorizzato | Autenticazione mancante o non valida |
| **403** | Proibito | Autenticato ma non autorizzato |
| **404** | Non trovato | La risorsa non esiste |
| **409** | Conflitto | Risorsa duplicata o conflitto di stato |
| **422** | Entità non elaborabile | JSON valido ma errori semantici |
| **429** | Troppe richieste | Limite tariffario superato |
| **500** | Errore interno del server | Errore imprevisto del server |
| **502** | Cattivo gateway | Errore del servizio upstream |
| **503** | Servizio non disponibile | Sovraccarico temporaneo o manutenzione |
---

## Controllo delle versioni API
Le API si evolvono. Quando è necessario apportare modifiche importanti, il controllo delle versioni consente ai client esistenti di continuare a funzionare.
| Strategia | Esempio | Pro | Contro |
|----------|---------|------|------|
| **Percorso URL** | `/v1/users`,`/v2/users`| Semplice, esplicito | Modifiche URL per versione |
| **Parametro di query** | `/users?version=2`| Flessibile | Facile da dimenticare |
| **Intestazione** | `Accept: application/vnd.myapi.v2+json`| URL puliti | Meno rilevabile |
| **Nessun controllo delle versioni** | Solo evoluzione dello schema | Più semplice | I cambiamenti radicali riguardano tutti |
**Best practice**: utilizza il controllo delle versioni del percorso URL (`/v1/`) per maggiore chiarezza. Supporta almeno una versione precedente. Depreca le vecchie versioni con tempistiche chiare.
---

## Metodi di autenticazione
| Metodo | Come funziona | Ideale per |
|--------|-------------|----------|
| **Chiavi API** | Chiave segreta nell'intestazione (`X-API-Key: abc123`) | Server-to-server, integrazioni semplici |
| **OAuth2** | Delega basata su token con ambiti | Accesso di terze parti, app autorizzate dall'utente |
| **JWT** | Token autonomo con attestazioni | Autenticazione senza stato tra i servizi |
| **Autenticazione di base** | Nome utente: password con codifica Base64 | Solo sviluppo: mai produzione senza TLS |
| **Cookie di sessione** | ID sessione lato server nel cookie solo HTTP | Applicazioni web tradizionali |
### Flusso OAuth2 (semplificato)
1. Il client reindirizza l'utente al server di autorizzazione.
2. L'utente accede e concede l'autorizzazione.
3. Il server di autorizzazione restituisce un codice di autorizzazione.
4. Il client scambia il codice con il token di accesso (e facoltativamente con il token di aggiornamento).
5. Il client utilizza il token di accesso per chiamare l'API.
6. Quando il token di accesso scade, utilizza il token di aggiornamento per ottenerne uno nuovo.
---

## Stili API: REST, GraphQL e gRPC
| Caratteristica | RIPOSO | GraphQL | gRPC |
|---------|------|---------|------|
| **Formato dati** | JSON (tipicamente) | JSON | Protobuf (binario) |
| **Endpoint** | Multipli (uno per risorsa) | Endpoint singolo | Definito dal file .proto |
| **Recupero eccessivo** | Comune (ottieni più del necessario) | Nessuno (il cliente specifica i campi) | Nessuno (definito dallo schema) |
| **Sottorecupero** | Richiede più chiamate | Nessuno (ottieni esattamente ciò di cui hai bisogno) | Nessuno |
| **In tempo reale** | Sono necessari WebSocket | Abbonamenti integrati | Streaming integrato |
| **Memorizzazione nella cache** | La memorizzazione nella cache HTTP funziona in modo naturale | Più difficile da memorizzare nella cache | Limitato |
| **Curva di apprendimento** | Basso | Medio | Medio–Alto |
| **Ideale per** | API pubbliche, app CRUD | Interfacce utente complesse, app mobili | Microservizi interni, ad alte prestazioni |
---

## Impaginazione, filtraggio e ordinamento
Per gli endpoint che restituiscono elenchi:
| Tecnica | Esempio | Quando usarlo |
|-----------|---------|-----|
| **Offset/Limite** | `?offset=20&limit=10`| Semplice; funziona per set di dati di piccole dimensioni |
| **Basato sul cursore** | `?cursor=abc123&limit=10`| Set di dati di grandi dimensioni; risultati coerenti |
| **Set di tasti** | `?created_after=2024-01-01&limit=10`| Molto efficiente; richiede una chiave univoca |
```json
// Cursor-based response
{
  "data": [...],
  "pagination": {
    "next_cursor": "abc123",
    "has_more": true
  }
}
```

---

## Limitazione della velocità
Proteggi la tua API dagli abusi e garantisci un utilizzo corretto.
| Strategia | Come funziona |
|----------|-------------|
| **Finestra fissa** | N richieste per finestra temporale (es. 100/ora) |
| **Finestra scorrevole** | Più granulare; conta le richieste nella finestra mobile |
| **Secchiello per gettoni** | Gettoni aggiunti a tasso fisso; ogni richiesta consuma un token |
Restituisce`429 Too Many Requests`con intestazioni:```
X-RateLimit-Limit: 100
X-RateLimit-Remaining: 0
X-RateLimit-Reset: 1625097600
Retry-After: 60
```

---

## Gestione degli errori
Risposte agli errori coerenti rendono molto più semplice lavorare con le API:
```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Invalid input data",
    "details": [
      {
        "field": "email",
        "issue": "Invalid email format"
      }
    ]
  }
}
```

**Principi**: utilizzare una struttura di errore coerente, includere messaggi utilizzabili, utilizzare codici di stato HTTP standard, registrare errori lato server con ID di correlazione e non esporre mai analisi dello stack o dettagli interni.
---

## Documentazione API
| Strumento | Descrizione |
|------|-------------|
| **OpenAPI (Spavalderia)** | Standard di settore per la documentazione dell'API REST |
| **Interfaccia utente spavalda** | Documentazione API interattiva dalle specifiche OpenAPI |
| **Postino** | Test API, documentazione e condivisione di raccolte |
| **Ridoc.** ​​| Bellissimi documenti di riferimento API dalle specifiche OpenAPI |
| **Parco giochi GraphQL / GraphiQL** | Esplorazione interattiva di GraphQL |
**Best practice**: scrivere prima le specifiche OpenAPI (sviluppo basato sulle specifiche), quindi generare da esse la documentazione e gli SDK client.
---

## Modelli di gateway API
Un gateway API si trova tra i client e i servizi backend, fornendo un unico punto di ingresso.
| Responsabilità | Descrizione |
|---------------|-------------|
| **Percorso** | Richieste dirette ai servizi backend appropriati |
| **Autenticazione** | Convalidare i token a livello di gateway |
| **Limitazione della velocità** | Applicare limiti globali o per cliente |
| **Trasformazione** | Conversione tra protocolli (REST ↔ gRPC) |
| **Memorizzazione nella cache** | Memorizza nella cache le risposte comuni |
| **Monitoraggio** | Registrazione e metriche centralizzate |
| **Bilanciamento del carico** | Distribuire il traffico tra le istanze del servizio |
| Strumento | Digitare |
|------|------|
| **Kong** | Gateway API open source (basato su Nginx) |
| **Gateway API AWS** | Completamente gestito, integrato con AWS |
| **Gestione API di Azure** | Gateway gestito con portale per sviluppatori |
| **Inviato/Istio** | Mesh di servizi con funzionalità gateway API |
| **Traefik** | Rilevamento automatico, integrazione Let's Encrypt |
---

## Webhook
I webhook consentono alla tua API di inviare eventi ai client in tempo reale, anziché chiedere ai client di eseguire il polling per le modifiche.
| Aspetto | Migliori pratiche |
|--------|--------------|
| **Consegna** | Richiesta POST con payload JSON all'URL del cliente |
| **Sicurezza** | Firma i payload con HMAC; il cliente verifica la firma |
| **Affidabilità** | Riprovare le consegne non riuscite con backoff esponenziale |
| **Idempotenza** | Includi ID evento univoco; il client gestisce i duplicati |
| **Versione** | Includi la versione API nel payload del webhook |
---

## Lista di controllo della progettazione
- [ ] Le risorse sono sostantivi plurali (`/users`, non`/getUser`)
- [ ] Metodi HTTP utilizzati correttamente (GET per letture, POST per create, ecc.)
- [ ] Formato di risposta all'errore coerente
- [ ] Impaginazione per tutti gli endpoint dell'elenco
- [ ] Limitazione della velocità con intestazioni chiare
- [] Definizione della strategia di versione dell'API
- [ ] Autenticazione e autorizzazione in atto
- [ ] Convalida dell'input su tutti gli endpoint
- [] Documentazione OpenAPI/Swagger mantenuta
- [ ] CORS configurato correttamente
- [ ] HTTPS applicato in produzione
- [ ] Chiavi di idempotenza per le operazioni POST dove necessario