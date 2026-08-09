---
# Metadata
title: "Security Best Practices"
description: "OWASP Top 10, input validation, auth, secrets management"
category: "Coding and Technology"
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
reviewed_by: "Coding & Technology Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [security, best, practices, coding-and-technology]
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

# Migliori pratiche di sicurezza
Una guida pratica per proteggere applicazioni, infrastrutture e dati, dallo sviluppo alla produzione.
---

## OWASP Top 10 (2021) — Panoramica
1. **Controllo accesso interrotto**: gli utenti possono accedere a risorse a cui non dovrebbero.
2. **Errori crittografici**: crittografia debole o mancante.
3. **Injection**: SQL, NoSQL, comando del sistema operativo o injection LDAP.
4. **Design insicuro**: difetti architettonici.
5. **Errore di configurazione della sicurezza**: password predefinite, porte aperte, errori dettagliati.
6. **Componenti vulnerabili e obsoleti**: CVE noti nelle dipendenze.
7. **Errori di identificazione e autenticazione**: password deboli, cattiva gestione delle sessioni.
8. **Errori di integrità del software e dei dati**: attacchi alla catena di fornitura, aggiornamenti non firmati.
9. **Errori di registrazione e monitoraggio della sicurezza**: nessun rilevamento di violazioni.
10. **Server-Side Request Forgery (SSRF)**: abuso del server per effettuare richieste ai sistemi interni.
---

## Convalida dell'input e codifica dell'output
### Regole di convalida
- **Lista bianca > Lista nera**: definisce i modelli consentiti (ad esempio, regex per la posta elettronica) anziché bloccare i modelli dannosi noti.
- **Limiti di lunghezza**: applica lunghezze massime per prevenire overflow del buffer e DoS.
- **Controllo del tipo**: garantisce che i numeri interi siano numeri interi e che i booleani siano booleani.
- **Utilizza librerie ben testate**: per la convalida di e-mail, URL e data, utilizza librerie standard (ad esempio,`email-validator`in Python,`validator.js`in Node).
### Codifica dell'output
- **Codifica HTML**: codifica`<`,`>`,`&`,`"`,`'`per impedire XSS.
- **Parametrizzazione SQL**: non concatenare mai l'input dell'utente in query SQL. Utilizzare query parametrizzate (istruzioni preparate) o un ORM.
- **Escape della shell**: evita di creare comandi della shell dall'input dell'utente; se inevitabile, utilizzare`shlex.quote()`o simile.
---

## Autenticazione e autorizzazione
### Gestione delle password
- **Hashing**: archivia le password con un algoritmo di hashing potente e lento: **Argon2id** (preferito), **bcrypt**, **scrypt** o **PBKDF2**.
- **Salting**: aggiungi un salt univoco per utente.
- **Lunghezza minima**: applica almeno 12-16 caratteri.
- **MFA (Multi-Factor Authentication)**: richiede un secondo fattore (TOTP, SMS, chiave hardware) per operazioni sensibili.
- **Limitazione della velocità**: impedisce i tentativi di forza bruta sugli endpoint di accesso (ad esempio, 5 tentativi ogni 5 minuti per IP/utente).
### Gestione delle sessioni
- Utilizzare cookie sicuri, solo HTTP, SameSite per i token di sessione.
- Impostare tempi di scadenza appropriati.
- Invalidare le sessioni al logout e al cambio password.
- Evitare di esporre gli ID di sessione negli URL.
### OAuth2/OIDC
- Utilizzare librerie consolidate (ad esempio Authlib, PyJWT, Passport.js, Spring Security).
- Convalida accuratamente i token ID (firma, emittente, pubblico, scadenza).
- Utilizzare i parametri di stato per prevenire CSRF.
- Mantenere riservati i segreti dei clienti.
### JWT (token Web JSON)
- **Segna**: utilizza RS256 o ES256 (asimmetrico) per una migliore sicurezza; HS256 (simmetrico) è accettabile se i segreti condivisi vengono gestiti correttamente.
- **Convalida**: verifica sempre la firma, l'emittente (`iss`), il pubblico (`aud`) e la scadenza (`exp`).
- **Mantieni scadenza breve**: 15–60 minuti per i token di accesso; utilizzare i token di aggiornamento per sessioni più lunghe.
- **Archivia in modo sicuro**: non archiviare mai i JWT in localStorage (vulnerabile a XSS); utilizzare invece cookie solo HTTP.
---

## Sicurezza dell'API
### Autenticazione
- Autenticare sempre le chiamate API (eccetto gli endpoint pubblici).
- Preferire chiavi API o token OAuth2 rispetto all'autenticazione di base (che invia credenziali a ogni richiesta).
### Limitazione e limitazione della velocità
- Applicare limiti di velocità per utente e per IP per prevenire abusi e DoS.
- Restituisce`429 Too Many Requests`con un'intestazione `Retry-After`.
### CORS (condivisione di risorse tra origini)
- Consentire solo origini specifiche (mai`*`in produzione).
- Convalida l'intestazione`Origin`sul lato server.
### Convalida dell'input
- Convalida tutti i parametri della richiesta, incluse intestazioni e corpo.
- Rifiuta campi imprevisti (`"strict": true` o`additionalProperties: false`nello schema JSON).
### HTTPS/TLS
- Applicare HTTPS in produzione.
- Utilizza HSTS (HTTP Strict Transport Security) per forzare i browser a utilizzare HTTPS.
- Utilizza TLS 1.2 o 1.3 (disabilita TLS 1.0/1.1).
---

## Gestione dei segreti
### Non codificare mai i segreti
- Non impegnare segreti (chiavi API, password, URL di database) nel controllo del codice sorgente.
- Utilizzare variabili di ambiente o strumenti di gestione dei segreti.
### Utensili
| Strumento | Descrizione |
|------|-------------|
| **HashiCorp Vault** | Segreti dinamici e di livello aziendale |
| **Gestore dei segreti AWS/Azure Key Vault/Gestore dei segreti GCP** | Nativo del cloud |
| **SOPS** | Crittografa i segreti nei file e confermali (con KMS o GPG) |
| **Segreti di Docker** | Per la modalità Sciame; Segreti Kubernetes (considerare il driver CSI Secrets Store esterno) |
### Rotazione
- Ruota regolarmente i segreti e gli account di servizio.
- Automatizzare la rotazione ove possibile.
---

## Gestione delle dipendenze
### Scansione delle vulnerabilità
| Lingua/Piattaforma | Strumenti |
|-------------------|-------|
| **Pitone** | `safety`,`pip-audit`,`bandit`|
| **Nodo** | `npm audit`,`yarn audit`,`snyk`|
| **Ruggine** | `cargo audit`|
| **Vai** | `govulncheck`|
| **Generale** | `Dependabot`(GitHub),`Renovate`,`Trivy`|
### Patch
- Mantieni le dipendenze aggiornate alle versioni con patch.
- Impostazione di richieste pull automatizzate per aggiornamenti minori/patch.
- Esamina i log delle modifiche per individuare eventuali modifiche sostanziali.
### Integrità della catena di fornitura
- Utilizzare i file di blocco del pacchetto (`package-lock.json`,`Cargo.lock`,`go.sum`) per garantire build riproducibili.
- Verificare i checksum delle dipendenze scaricate.
- Preferisci i registri ufficiali e fidati solo degli editori verificati.
---

## Sicurezza delle infrastrutture
### Firewall
- Blocca tutte le porte in entrata tranne quelle esplicitamente necessarie (ad esempio, 80, 443).
- Limita l'accesso SSH a intervalli IP specifici (o utilizza un host VPN/bastione).
- Utilizza gruppi di sicurezza (AWS) o NSG (Azure) per un controllo granulare.
### Rafforzamento del sistema operativo
- Applicare regolarmente gli aggiornamenti di sicurezza (`sudo apt upgrade`, `yum update`).
- Disattiva i servizi non necessari e gli account predefiniti.
- Usa fail2ban per bloccare i tentativi di forza bruta su SSH.
- Rafforzare SSH: disabilita l'accesso root, usa l'autenticazione basata su chiave, cambia la porta predefinita (opzionale).
### Segmentazione della rete
- Posiziona database e cache in sottoreti private senza accesso a Internet.
- Utilizzare una DMZ per i servizi rivolti al pubblico.
- Applicare il principio del privilegio minimo all'accesso alla rete.
### Segreti nelle infrastrutture
- Non archiviare mai i segreti nelle variabili di ambiente CI/CD a meno che non siano crittografati.
- Utilizza i ruoli IAM del fornitore di servizi cloud per le istanze EC2/VM invece delle chiavi di lunga durata.
---

## Registrazione e monitoraggio
### Cosa registrare
- Eventi di autenticazione (successo/fallimento).
- Decisioni di controllo degli accessi (mancate autorizzazioni).
- Azioni di amministrazione (creazione di utenti, eliminazione, modifiche delle autorizzazioni).
- Modifiche allo schema del database.
- Errori ed eccezioni di sistema.
- Richieste e risposte API (cancellare dati sensibili).
### Cosa non registrare
- Password, segreti, token, PII (informazioni di identificazione personale) a meno che non siano sottoposte ad hashing/censurate.
- Numeri completi delle carte di credito.
### Avviso
- Imposta avvisi per:
  - Numerosi accessi non riusciti (potenziale forza bruta).
  - Schemi di accesso insoliti (ad esempio, da nuove località, in orari strani).
  - Nuovi account amministratore creati.
  - Tassi di errore elevati o picchi di latenza.
- Utilizzare un SIEM (Security Information and Event Management) per la correlazione avanzata.
### Conservazione dei registri
- Conservare i registri per almeno 30-90 giorni a seconda dei requisiti normativi.
- Archiviare i log in un sistema centralizzato a prova di manomissione (ad esempio, ELK Stack, Splunk, Datadog).
---

## Ciclo di vita dello sviluppo sicuro (SDL)
1. **Formazione**: assicurati che gli sviluppatori comprendano le vulnerabilità comuni.
2. **Modellazione delle minacce**: identificare le potenziali minacce nelle prime fasi della progettazione.
3. **Standard di codifica sicuri**: applicazione tramite linter e liste di controllo per la revisione del codice.
4. **SAST** (Static Application Security Testing): scansione del codice sorgente per individuare eventuali vulnerabilità (SonarQube, CodeQL).
5. **DAST** (Dynamic Application Security Testing): scansione delle applicazioni in esecuzione (OWASP ZAP, Burp Suite).
6. **SCA** (Analisi della composizione software): scansione delle dipendenze.
7. **Test di penetrazione**: esercizi regolari di hacking etico.
8. **Bug bounty**: incoraggia i ricercatori esterni a individuare le vulnerabilità in modo responsabile.
9. **Piano di risposta agli incidenti**: disporre di un piano chiaro per quando viene rilevata una violazione.
---

## Lista di controllo di emergenza (quando si sospetta una violazione)
1. **Non farti prendere dal panico**, ma agisci rapidamente.
2. **Isolare** i sistemi interessati (disconnettersi dalla rete se necessario).
3. **Conserva prove**: acquisisci log, dump della memoria e immagini del disco.
4. **Identificare** l'ambito: quali sistemi, quali dati.
5. **Ruota** tutte le credenziali e i segreti compromessi.
6. **Correggere** la vulnerabilità.
7. **Informare** gli utenti interessati e gli organismi di regolamentazione, se necessario (entro i termini legali).
8. **Condurre un'autopsia** per comprendere la causa principale e migliorare i processi.