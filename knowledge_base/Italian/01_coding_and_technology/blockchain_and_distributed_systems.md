<!--
---
# Metadata
title: "Blockchain and Distributed Systems"
description: "Consensus, smart contracts, DeFi, Byzantine fault tolerance"
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
tags: [blockchain, distributed, systems, coding-and-technology]
difficulty_level: "intermediate"
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
# Blockchain e sistemi distribuiti
Blockchain è un tipo specifico di sistema distribuito: un registro decentralizzato di sola aggiunta in cui i record (blocchi) sono collegati da hash crittografici. I sistemi distribuiti rappresentano il campo più ampio in cui più computer funzionano insieme come se fossero uno solo. Entrambi i concetti sono importanti per comprendere le infrastrutture moderne, dalla criptovaluta ai database distribuiti agli algoritmi di consenso che alimentano i servizi globali.
---

## Fondamenti di sistemi distribuiti
### Perché i sistemi distribuiti?
| Motivazione | Descrizione |
|-----------|-------------|
| **Scalabilità** | Aggiungi più macchine per gestire più carichi |
| **Tolleranza agli errori** | Il sistema continua a funzionare anche se alcune macchine si guastano |
| **Distribuzione geografica** | Servire gli utenti dai data center vicini |
| **Specializzazione** | Macchine diverse gestiscono compiti diversi |
### Concetti chiave
| Concetto | Descrizione | Sfida |
|---------|-------------|-----------|
| **Consenso** | Far sì che tutti i nodi siano d'accordo su un valore | Partizioni di rete; Difetti bizantini |
| **Replica** | Copia dei dati su più nodi | Coerenza vs disponibilità |
| **Partizionamento (sharding)** | Suddivisione dei dati tra i nodi | Punti caldi; query tra partizioni |
| **Modelli di coerenza** | Garanzie su ciò che vedono i diversi lettori | La consistenza forte è lenta; l'eventuale coerenza può sorprendere gli utenti |
| **Teorema della PAC** | Puoi averne solo 2 tra: Coerenza, Disponibilità, Tolleranza della partizione | In pratica è necessaria la tolleranza della partizione; scegli C o A |
### Il Teorema della PAC
| Scelta | Cosa ottieni | A cosa rinunci | Esempio |
|--------|-------------|-----------------|---------|
| **CP** | Coerente + tollerante alle partizioni | Alcuni nodi potrebbero non essere disponibili durante le partizioni | HBase, MongoDB, Redis |
| **AP** | Disponibile + tollerante alle partizioni | Le letture potrebbero restituire dati non aggiornati | Cassandra, DynamoDB, CouchDB |
| **CA** | Coerente + disponibile | Non è possibile tollerare partizioni di rete | Database a nodo singolo (non realmente distribuiti) |
---

## Algoritmi di consenso
Come si accordano i nodi distribuiti sullo stato del sistema?
| Algoritmo | Digitare | Tolleranza agli errori | Usato in |
|-----------|------|----------------|---------|
| **Paxos** | Tollerante agli errori di crash | Fino a f guasti con 2f+1 nodi | Google Paffuto; teoria fondazionale |
| **Zattera** | Tollerante agli errori di crash | Fino a f guasti con 2f+1 nodi | eccd, Console, TiKV |
| **PBFT** | Tollerante ai guasti bizantino | Fino a f guasti con 3f+1 nodi | Tessuto Hyperledger |
| **Prova di lavoro** | Tollerante ai guasti bizantino | Dipende dall'hash power | Bitcoin |
| **Prova di partecipazione** | Tollerante ai guasti bizantino | Dipende dalla puntata | Ethereum 2.0, Cardano |
### Zattera (semplificato)
| Ruolo | Responsabilità |
|------|--------------|
| **Capo** | Gestisce tutte le richieste dei clienti; invia voci di registro ai follower |
| **Seguace** | Risponde alle richieste del leader; voti alle elezioni |
| **Candidato** | Richiede voti per diventare leader |
1. Tutti i nodi iniziano come follower
2. Se un follower non riceve notizie dal leader per un timeout elettorale, diventa un candidato
3. I candidati richiedono voti; quello con più voti diventa leader
4. Il leader replica le voci di registro ai follower
5. Quando la maggioranza conferma, l'iscrizione è impegnata
---

## Blockchain
### Come funziona una Blockchain
| Componente | Descrizione |
|-----------|-------------|
| **Blocca** | Un batch di transazioni + metadati + hash del blocco precedente |
| **Hash** | Impronta crittografica del contenuto del blocco |
| **Catena** | Ogni blocco fa riferimento all'hash del blocco precedente, creando una catena immutabile |
| **Consenso** | I partecipanti alla rete concordano quali blocchi aggiungere |
| **Albero Merkle** | Albero di hash che riassume tutte le transazioni in un blocco |
### Perché la Blockchain è difficile da manomettere
1. Ogni blocco contiene l'hash del blocco precedente
2. La modifica di qualsiasi transazione modifica l'hash del blocco
3. L'hash modificato interrompe la catena: tutti i blocchi successivi diventano non validi
4. Un utente malintenzionato dovrebbe rieseguire il mining di tutti i blocchi successivi E controllare più del 50% della rete
### Tipi di blockchain
| Digitare | Accesso | Validatore | Esempio |
|------|--------|-----------|---------|
| **Pubblico (senza autorizzazione)** | Chiunque può leggere e scrivere | Consenso aperto (PoW, PoS) | Bitcoin, Ethereum |
| **Privato (autorizzato)** | Accesso limitato | Validatori conosciuti | Hyperledger, Corda |
| **Consorzio** | Governato da un gruppo di organizzazioni | Validatori selezionati | R3 Corda per il settore bancario |
### Contratti intelligenti
Codice autoeseguibile memorizzato sulla blockchain che viene eseguito quando vengono soddisfatte condizioni predeterminate.
| Piattaforma | Lingua | Caratteristica notevole |
|----------|----------|-----------|
| **Ethereum** | Solidità, Vyper | Il più grande ecosistema di contratti intelligenti |
| **Solana** | Ruggine, C | Produttività elevata; commissioni basse |
| **Cardano** | Haskell (Pluto) | Revisionato da pari; verifica formale |
| **Hyperledger** | Vai, Java, JavaScript | Impresa; autorizzato |
---

## Criptovaluta
| Valuta | Consenso | Fornitura | Uso primario |
|----------|-----------|--------|-----|
| **Bitcoin** | Prova di lavoro | 21 milioni (limitato) | Riserva di valore; oro digitale |
| **Ethereum** | Prova di puntata | Nessun tetto rigido | Contratti intelligenti; DeFi; NFT |
| **Solana** | Prova di puntata + Prova di storia | Nessun tetto rigido | Transazioni ad alta velocità |
| **Cardano** | Prova di puntata (Ouroboros) | 45 miliardi (limitato) | Approccio accademico; sostenibilità |
---

## Database distribuiti
| Banca dati | Architettura | Coerenza | Ideale per |
|----------|-------------|-------------|----------|
| **Cassandra** | Colonna larga; peer-to-peer | Sintonizzabile (eventuale al quorum) | Velocità di scrittura elevata; serie temporali |
| **MongoDB** | Documento; set di repliche | Eventuale (con opzione di coerenza causale) | Schema flessibile; rapido sviluppo |
| **ScarafaggioDB** | SQL distribuito; Consenso sulla zattera | Forte | SQL distribuito; distribuzione globale |
| **TiDB** | SQL distribuito; Zattera (tramite TiKV) | Forte | Compatibile con MySQL; ridimensionamento orizzontale |
| **DynamoDB** | Valore-chiave; gestito | Eventuale (o forte con letture coerenti) | Senza server; Integrato in AWS |
| **Chiave inglese** | SQL distribuito; Paxos | Forte | GoogleNuvola; coerenza globale |
---

## Modelli di sistema distribuito
| Modello | Descrizione | Caso d'uso |
|---------|-------------|----------|
| **Elezione del leader** | Scegli un nodo da coordinare | Capo zattera; Custode dello zoo |
| **Replica** | Copia i dati per la ridondanza e leggi il ridimensionamento | Repliche di database; CDN |
| **Sharding** | Partizionare i dati per intervallo di chiavi o hash | Banche dati su larga scala |
| **MapReduce** | Suddivisione del calcolo tra i nodi; risultati aggregati | Elaborazione dati di grandi dimensioni |
| **Protocollo Gossip** | I nodi condividono periodicamente lo stato con peer casuali | Appartenenza al cluster; rilevamento guasti |
| **Commit in due fasi** | Coordinare le transazioni su più nodi | Database distribuiti |
| **Modello Saga** | Serie di transazioni locali con azioni compensative | Transazioni di microservizi |
| **Interruttore automatico** | Smettere di chiamare un servizio in errore; fallire velocemente | Resilienza; prevenire guasti a cascata |
---

## Sfide nei sistemi distribuiti
| Sfida | Descrizione | Mitigazione |
|-----------|-------------|------------|
| **Partizioni di rete** | I nodi non possono comunicare | compromesso sulla PAC; riprovare con backoff |
| **Disallineamento dell'orologio** | Nodi diversi hanno orologi diversi | Utilizzare orologi logici; NTP; evitare di fare affidamento sull'ora dell'orologio da parete |
| **Difetti bizantini** | Nodi che mentono o si comportano arbitrariamente | consenso BFT; blockchain |
| **Cervello diviso** | Due nodi pensano entrambi di essere il leader | Scherma; decisioni basate sul quorum |
| **Errori a cascata** | Un fallimento ne innesca altri | Interruttori automatici; paratie; degrado grazioso |
| **Coerenza dei dati** | Mantenere le repliche sincronizzate | Modelli di coerenza; risoluzione dei conflitti |
---

## Riepilogo
I sistemi distribuiti rappresentano il modo in cui il software moderno si adatta, sopravvive ai guasti e serve gli utenti a livello globale. Gli algoritmi di consenso (Raft, Paxos) garantiscono che i nodi siano d'accordo. Le blockchain aggiungono verifica crittografica e decentralizzazione per creare registri affidabili. I database distribuiti (Cassandra, CockroachDB, DynamoDB) gestiscono i dati su larga scala. Il compromesso fondamentale – catturato dal teorema della PAC – è tra coerenza e disponibilità quando la rete è inaffidabile. Comprendere questi concetti è essenziale per costruire sistemi che funzionino su scala Internet.