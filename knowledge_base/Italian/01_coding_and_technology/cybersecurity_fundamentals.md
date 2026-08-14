---
# Metadata
title: "Cybersecurity Fundamentals"
description: "Encryption, TLS, OWASP, secure coding, SDL"
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
tags: [cybersecurity, coding-and-technology]
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
# Fondamenti di sicurezza informatica
La sicurezza è una disciplina che deve essere integrata in ogni livello di un sistema fin dall’inizio, piuttosto che aggiunta in un secondo momento. Che si tratti di creare un'applicazione Web, gestire l'infrastruttura o distribuire un'API, comprendere il panorama delle minacce e i fondamenti della difesa è essenziale.
---

## Crittografia e crittografia
### Crittografia simmetrica e asimmetrica
| Digitare | Come funziona | Velocità | Distribuzione chiave | Esempi |
|------|-------------|-------|-----------|----------|
| **Simmetrico** | Stessa chiave per crittografia e decrittografia | Veloce | Sfida: come condividere la chiave? | AES-256, ChaCha20 |
| **Asimmetrico** | La chiave pubblica crittografa, la chiave privata decrittografa | Più lento | La chiave pubblica può essere condivisa apertamente | RSA, ECC (curva ellittica) |
In pratica, la maggior parte dei sistemi utilizza **entrambi**: crittografia asimmetrica per scambiare in modo sicuro una chiave simmetrica, quindi crittografia simmetrica per la maggior parte dei dati. Ecco come funziona TLS/HTTPS.
### Hashing
L'hashing è una funzione unidirezionale: converte l'input in una stringa di dimensione fissa. Non puoi invertirlo, ma lo stesso input produce sempre lo stesso output.
| Caso d'uso | Algoritmo consigliato | Evitare |
|----------|---------------------|-------|
| **Memoria password** | Argon2id, bcrypt, scrypt | MD5, SHA-1, semplice SHA-256 (troppo veloce) |
| **Integrità dei dati** | SHA-256, SHA-3 | MD5 (rotto), SHA-1 (rotto) |
| **Firme digitali** | Ed25519, RSA-2048+ | DSA |
### TLS/HTTPS
HTTPS è HTTP su TLS (Transport Layer Security). Fornisce:
- **Crittografia**: i dati in transito non possono essere letti dagli intercettatori.
- **Autenticazione**: il server dimostra la propria identità tramite un certificato.
- **Integrità**: i dati non possono essere modificati durante il trasporto senza essere rilevati.
Utilizza TLS 1.2 o 1.3. Disabilita TLS 1.0 e 1.1. Abilita HSTS (HTTP Strict Transport Security) per forzare i browser a utilizzare sempre HTTPS.
---

## Autenticazione e autorizzazione
### Autenticazione: chi sei?
| Metodo | Livello di sicurezza | Caso d'uso |
|--------|---------------|----------|
| **Password** | Basso-Medio | Account di base (applica 12+ caratteri, verifica eventuali violazioni) |
| **AMF (TOTP)** | Alto | Standard per account sensibili (Google Authenticator, Authy) |
| **Chiave hardware (FIDO2/WebAuthn)** | Molto alto | Conti ad alta sicurezza (YubiKey) |
| **Biometrico** | Medio–Alto | Sblocco del dispositivo (impronta digitale, volto): non eccezionale come unico fattore |
| **OAuth2 / OIDC** | Alto | Accesso di terze parti ("Accedi con Google") |
**Regole password**: applicazione della lunghezza minima (12-16 caratteri), controllo degli elenchi di password violate, utilizzo Argon2id o bcrypt per l'hashing con salt per utente.
### Autorizzazione: cosa puoi fare?
| Modello | Descrizione | Esempio |
|-------|-------------|---------|
| **RBAC** (controllo degli accessi basato sui ruoli) | Autorizzazioni assegnate ai ruoli; gli utenti ottengono ruoli | Amministratore, Editor, Visualizzatore |
| **ABAC** (basato sugli attributi) | Regole basate su attributi utente, risorse, ambiente | "I manager possono approvare le richieste della propria squadra" |
| **ACL** (Elenco controllo accessi) | Autorizzazioni esplicite per utente/risorsa | Autorizzazioni file (lettura/scrittura/esecuzione) |
**Principio del privilegio minimo**: concedere a ogni utente, servizio e processo solo l'accesso minimo di cui ha bisogno.
### JWT (token Web JSON)
| Aspetto | Raccomandazione |
|--------|---------------|
| **Firma** | Preferibile RS256 o ES256 (asimmetrico); HS256 accettabile con segreti gestiti |
| **Scadenza** | 15–60 minuti per i token di accesso; utilizzare i token di aggiornamento per sessioni più lunghe |
| **Archiviazione** | Cookie solo HTTP (non localStorage — vulnerabile a XSS) |
| **Convalida** | Verifica sempre firma, emittente, destinatario e scadenza |
---

##OWASPTop 10 (2021)
L'OWASP Top 10 è il documento standard di sensibilizzazione per la sicurezza delle applicazioni web. Rappresenta i rischi più critici:
| # | Rischio | Cosa significa |
|---|------|--------------|
| 1| **Controllo accessi interrotto** | Gli utenti possono accedere a risorse a cui non dovrebbero |
| 2| **Errori crittografici** | Crittografia debole o mancante per i dati sensibili |
| 3| **Iniezione** | SQL, NoSQL, comando del sistema operativo o LDAP injection |
| 4| **Design non sicuro** | Difetti architetturali che non possono essere risolti con l'implementazione |
| 5| **Errore di configurazione della sicurezza** | Password predefinite, porte aperte, messaggi di errore dettagliati |
| 6| **Componenti vulnerabili** | CVE noti nelle dipendenze |
| 7| **Errori di autenticazione** | Password deboli, cattiva gestione delle sessioni |
| 8| **Mancanze di integrità** | Attacchi alla catena di fornitura, aggiornamenti non firmati |
| 9| **Errori di registrazione/monitoraggio** | Nessun rilevamento di violazioni |
| 10| **SSRF** | Il server è stato indotto con l'inganno a effettuare richieste ai sistemi interni |
---

## Pratiche di codifica sicure
### Convalida dell'input
| Regola | Perché |
|------|-----|
| **Lista bianca > Lista nera** | Definisci cosa è consentito, non cosa è bloccato |
| **Query parametrizzate** | Non concatenare mai l'input dell'utente in SQL: utilizzare istruzioni preparate o ORM |
| **Codifica HTML** | Codifica`<`,`>`,`&`,`"`,`'`per impedire XSS |
| **Shell in fuga** | Evitare di creare comandi shell dall'input dell'utente; utilizzare`shlex.quote()`|
| **Limiti di lunghezza** | Applicare la lunghezza massima per evitare buffer overflow e DoS |
| **Controllo della digitazione** | Assicurati che i numeri interi siano numeri interi, i booleani siano booleani |
### Vulnerabilità comuni
| Vulnerabilità | Attacco | Difesa |
|--------------|--------|---------|
| **Iniezione SQL** | `' OR 1=1 --`nel modulo di accesso | Query con parametri |
| **XSS** | `<script>alert('hacked')</script>`nel campo commenti | Codifica dell'output, Politica di sicurezza dei contenuti |
| **CSRF** | Indurre il browser dell'utente a effettuare richieste non autorizzate | Token CSRF, cookie SameSite |
| **Attraversamento del percorso** | `../../etc/passwd`nel parametro del file | Convalidare e disinfettare i percorsi dei file |
| **IDOR** | Cambia`/user/123`in`/user/124`per vedere i dati di qualcun altro | Verifiche di autorizzazione su ogni richiesta |
---

## Sicurezza della rete
### Firewall
| Digitare | Descrizione |
|------|-------------|
| **Filtraggio dei pacchetti** | Regole basate su IP, porta, protocollo |
| **Con stato** | Tiene traccia degli stati di connessione; filtraggio più intelligente |
| **A livello di applicazione (WAF)** | Ispeziona il traffico HTTP; blocca SQL injection, XSS, ecc. |
| **Gruppi di sicurezza cloud** | Firewall virtuali per istanze cloud (SG AWS, NSG Azure) |
**Regola pratica**: blocca tutto il traffico in entrata per impostazione predefinita; apri solo ciò che è esplicitamente necessario (80, 443 per il web).
### Segmentazione della rete
Posiziona database e cache in sottoreti private senza accesso diretto a Internet. Utilizza una DMZ per i servizi rivolti al pubblico (server Web, bilanciatori del carico). Applicare il principio del privilegio minimo all'accesso alla rete.
---

## Gestione dei segreti
### La regola d'oro
**Non codificare mai i segreti.** Nessuna chiave API, password o URL di database nel codice sorgente. Nessun segreto nelle variabili di ambiente impegnate in Git. Nessun segreto nelle immagini Docker.
### Utensili
| Strumento | Digitare | Ideale per |
|------|------|----------|
| **HashiCorp Vault** | Responsabile dei segreti aziendali | Segreti dinamici, crittografia come servizio |
| **Gestore dei segreti AWS** | Nativo del cloud | Ambienti AWS |
| **Azure Key Vault** | Nativo del cloud | Ambienti azzurri |
| **SOPS** | File crittografati | Crittografa i segreti in Git (con KMS o GPG) |
| **Segreti di Docker** | Nativo del contenitore | Docker Swarm (per K8, considera Secrets Store CSI) |
| **dotenv (.env)** | Sviluppo locale | Solo sviluppo: mai in produzione o impegnato |
### Rotazione
Ruota i segreti regolarmente e automaticamente. Se un segreto viene divulgato (ad esempio, depositato in un repository pubblico), ruotalo immediatamente, anche se pensi che nessuno lo abbia visto.
---

## Sicurezza delle dipendenze
La tua applicazione è sicura tanto quanto la sua dipendenza più debole.
### Strumenti di scansione
| Lingua | Strumenti |
|----------|-------|
| **Pitone** | `safety`,`pip-audit`,`bandit`|
| **Node.js** | `npm audit`,`yarn audit`,`snyk`|
| **Ruggine** | `cargo audit`|
| **Vai** | `govulncheck`|
| **Generale** | `Dependabot`(GitHub),`Renovate`,`Trivy`|
### Integrità della catena di fornitura
- Utilizzare i file di blocco (`package-lock.json`,`Cargo.lock`,`go.sum`) per build riproducibili.
- Verificare i checksum delle dipendenze scaricate.
- Preferire registri ufficiali ed editori verificati.
- Automatizza aggiornamenti minori/patch tramite Dependabot o Renovate.
---

## Ciclo di vita dello sviluppo della sicurezza (SDL)
| Fase | Attività |
|-------|----------|
| **Formazione** | Assicurarsi che gli sviluppatori comprendano le vulnerabilità comuni |
| **Modellazione delle minacce** | Identificare potenziali minacce durante la progettazione |
| **Standard di codifica sicura** | Applicare tramite linter e liste di controllo per la revisione del codice |
| **SAST** | Analisi statica del codice sorgente (SonarQube, CodeQL) |
| **DAST** | Analisi dinamica dell'applicazione in esecuzione (OWASP ZAP, Burp Suite) |
| **SCA** | Analisi della composizione del software: scansione delle dipendenze |
| **Test di penetrazione** | Esercizi regolari di hacking etico |
| **Bug Bounty** | Incoraggiare i ricercatori esterni a trovare le vulnerabilità |
| **Piano di risposta agli incidenti** | Avere un piano chiaro per quando viene rilevata una violazione |
---

## Lista di controllo di emergenza
Quando sospetti una violazione:
1. **Niente panico**, ma agisci rapidamente.
2. **Isolare** i sistemi interessati (disconnettersi dalla rete se necessario).
3. **Preservare le prove**: acquisire registri, dump della memoria, immagini del disco.
4. **Identificare l'ambito**: quali sistemi, quali dati?
5. **Ruota** tutte le credenziali e i segreti compromessi.
6. **Correggere** la vulnerabilità.
7. **Informare** gli utenti interessati e le autorità di regolamentazione, se necessario (entro i termini legali).
8. **Post mortem**: documentare la causa principale e le azioni da intraprendere entro 24–48 ore.