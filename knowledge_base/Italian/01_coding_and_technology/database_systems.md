<!--
---
# Metadata
title: "Database Systems"
description: "SQL, NoSQL, design patterns, optimization"
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
tags: [database, systems, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "13 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Sistemi di database
## Fondamenti di database
### Cos'è un database?
Un database è una raccolta organizzata di informazioni strutturate archiviate elettronicamente, progettate per il recupero, l'inserimento, l'aggiornamento e la cancellazione efficienti dei dati.
### Sistemi di gestione di database (DBMS)
Software che interagisce con gli utenti finali, le applicazioni e il database stesso per acquisire e analizzare i dati. Esempi: MySQL, PostgreSQL, Oracle, MongoDB.
### Concetti chiave
- **Schema**: Struttura/organizzazione del database (tabelle, campi, relazioni)
- **Istanza**: dati effettivi memorizzati in un momento particolare
- **Proprietà dell'ACIDO**: Atomicità, Consistenza, Isolamento, Durabilità
- **Teorema CAP**: Coerenza, Disponibilità, Tolleranza di partizione (scegliere 2)
- **Normalizzazione**: organizzazione dei dati per ridurre la ridondanza
- **Denormalizzazione**: aggiunta di ridondanza per migliorare le prestazioni di lettura
## Database relazionali (SQL)
### Concetti fondamentali
- **Tabelle**: righe (record) e colonne (campi)
- **Chiave primaria**: identificatore univoco per ogni riga
- **Chiave esterna**: riferimento alla chiave primaria in un'altra tabella
- **Indici**: strutture dati che migliorano la velocità delle query
- **Visualizzazioni**: tabelle virtuali basate sui risultati della query
- **Procedure memorizzate**: blocchi di codice SQL precompilati
- **Trigger**: azioni automatiche sulle modifiche dei dati
### Operazioni SQL (CRUD)```sql
-- Create
INSERT INTO users (name, email) VALUES ('Alice', 'alice@example.com');

-- Read
SELECT * FROM users WHERE id = 1;
SELECT name, email FROM users ORDER BY name LIMIT 10;

-- Update
UPDATE users SET email = 'new@example.com' WHERE id = 1;

-- Delete
DELETE FROM users WHERE id = 1;
```

### Si unisce
- **INNER JOIN**: restituisce le righe corrispondenti da entrambe le tabelle
- **LEFT JOIN**: tutte le righe dalla tabella a sinistra, corrispondenze da destra
- **RIGHT JOIN**: tutte le righe dalla tabella a destra, corrispondenze da sinistra
- **FULL OUTER JOIN**: tutte le righe di entrambe le tabelle
- **CROSS JOIN**: prodotto cartesiano di entrambe le tabelle
- **SELF JOIN**: Tabella unita a se stessa
### Moduli di normalizzazione
- **1NF**: valori atomici, nessun gruppo ripetitivo
- **2NF**: 1NF + nessuna dipendenza parziale (tutti gli attributi non chiave dipendono dall'intera chiave primaria)
- **3NF**: 2NF + nessuna dipendenza transitiva (gli attributi non chiave non dipendono da altri attributi non chiave)
- **BCNF**: 3NF più forte, ogni determinante è una chiave candidata
- **4NF**: nessuna dipendenza multivalore
- **5NF**: nessuna dipendenza di join
### RDBMS popolare
- **PostgreSQL**: funzionalità avanzate, estensibile, compatibile con ACID
- **MySQL**: applicazioni web ampiamente utilizzate, letture veloci
- **Oracle**: funzionalità aziendali, scalabilità, costose
- **SQL Server**: ecosistema Microsoft, strumenti integrati
- **SQLite**: integrato, serverless, leggero
- **MariaDB**: fork MySQL, open source
## Database NoSQL
### Tipi di database NoSQL
#### Archivi di documenti
- **Struttura**: documenti simili a JSON (BSON)
- **Casi d'uso**: gestione dei contenuti, cataloghi, profili utente
- **Esempi**: MongoDB, CouchDB, DocumentDB
- **Esempio di query** (MongoDB):```javascript
db.users.find({ age: { $gt: 25 } }).sort({ name: 1 });
```

#### Negozi di valori-chiave
- **Struttura**: coppie chiave-valore semplici
- **Casi d'uso**: memorizzazione nella cache, sessioni, carrelli della spesa
- **Esempi**: Redis, DynamoDB, Riak
- **Caratteristiche**: interrogazioni veloci, semplici e limitate
#### Negozi di famiglie di colonne
- **Struttura**: colonne raggruppate in famiglie
- **Casi d'uso**: Big Data, analisi, serie temporali
- **Esempi**: Cassandra, HBase, ScyllaDB
- **Caratteristiche**: ottimizzato per la scrittura, distribuito, scalabile
#### Database grafici
- **Struttura**: Nodi, bordi, proprietà
- **Casi d'uso**: social network, rilevamento di frodi, raccomandazioni
- **Esempi**: Neo4j, Amazon Neptune, ArangoDB
- **Linguaggio di query**: Cypher (Neo4j), Gremlin
### Quando utilizzare NoSQL
- Schema flessibile/in evoluzione
- Requisiti di scala orizzontale
- Elevata velocità di scrittura
- Dati gerarchici/annidati
- Sistemi distribuiti
- Applicazioni in tempo reale
## Progettazione di database
### Modellazione entità-relazione
- **Entità**: Oggetti/concetti (Cliente, Prodotto, Ordine)
- **Attributi**: Proprietà delle entità (nome, prezzo, data)
- **Relazioni**: Connessioni tra entità (uno-a-uno, uno-a-molti, molti-a-molti)
- **Cardinalità**: Numero di istanze in relazione
### Modelli di progettazione dello schema
- **Eredità da tabella singola**: tutti i tipi in una tabella con discriminatore di tipo
- **Ereditarietà della tabella delle classi**: tabelle separate per base e sottoclassi
- **Eredità della tabella concreta**: tabella separata per ogni classe concreta
- **Tabelle di giunzione**: risolvi le relazioni molti-a-molti
- **Tabelle di controllo**: tenere traccia delle modifiche (created_at, aggiornato_at, cancellato_at)
### Strategie di indicizzazione
- **B-Tree**: impostazione predefinita, query su intervallo, ordinamento
- **Hash**: ricerche di corrispondenze esatte
- **Bitmap**: colonne con cardinalità bassa (sesso, stato)
- **Full-Text**: funzionalità di ricerca testuale
- **Spaziale**: dati geografici (GIS)
- **Composito**: più colonne combinate
- **Copertura**: include tutte le colonne necessarie per la query
## Ottimizzazione delle query
### Piani di esecuzione
- Comprendere come il database esegue le query
- Identificazione dei colli di bottiglia (scansioni complete di tabelle, indici mancanti)
- Strumenti: SPIEGARE, SPIEGARE ANALIZZARE
### Tecniche di ottimizzazione
- **Utilizzo dell'indice**: assicurati che le query utilizzino indici appropriati
- **Riscrittura delle query**: semplifica le query complesse
- **Ottimizzazione della partecipazione**: scegli i tipi e l'ordine di partecipazione corretti
- **Partizionamento**: suddivisione di tabelle di grandi dimensioni (intervallo, hash, elenco)
- **Visualizzazioni materializzate**: risultati della query precalcolati
- **Memorizzazione nella cache delle query**: archivia i risultati delle query frequenti
### Problemi comuni di prestazioni
- **Problema di query N+1**: recupero dei dati correlati in modo inefficiente
- **Indici mancanti**: scansioni complete di tabelle su tabelle di grandi dimensioni
- **Sovraindicizzazione**: scritture lente a causa di troppi indici
- **Contesa di blocco**: transazioni in attesa di blocco
- **Query inefficienti**: SELECT *, join non necessari
## Transazioni e concorrenza
### Livelli di isolamento delle transazioni
- **READ UNCOMMITTED**: isolamento più basso, letture sporche possibili
- **READ COMMITTED**: visibili solo i dati confermati (impostazione predefinita nella maggior parte dei DB)
- **LETTURA RIPETIBILE**: la stessa query restituisce gli stessi risultati all'interno della transazione
- **SERIALIZZABILE**: massimo isolamento, le transazioni vengono eseguite in sequenza
### Controllo della concorrenza
- **Blocco pessimistico**: blocca le risorse prima dell'accesso
- **Blocco ottimistico**: controlla la versione prima del commit
- **MVCC (Multi-Version Concurrency Control)**: mantiene più versioni di righe
- **Blocco a livello di riga**: blocca righe specifiche
- **Blocco a livello di tabella**: blocca l'intera tabella
### Impasse
- Dipendenza circolare in cui le transazioni si aspettano l'una dall'altra
- Prevenzione: ordinamento coerente dei blocchi, timeout, rilevamento dei deadlock
- Risoluzione: interrompere una transazione
## Replica e ridimensionamento
### Tipi di replica
- **Master-Slave**: una replica primaria e più letture
- **Master-Master**: primari multipli, replica bidirezionale
- **Multi-Master**: N primari, è necessaria la risoluzione dei conflitti
- **Replica a catena**: replica sequenziale attraverso i nodi
### Approcci di scalabilità
- **Scalatura verticale**: aumenta le risorse del server (CPU, RAM, spazio di archiviazione)
- **Scalatura orizzontale**: aggiungi più server (sharding, partizionamento)
- **Repliche di lettura**: scarica il traffico di lettura
- **Sharding**: suddivisione dei dati tra server per chiave/intervallo/hash
- **Federazione**: suddivisa per funzione/servizio
### Modelli di coerenza
- **Coerenza elevata**: tutti i nodi vedono gli stessi dati contemporaneamente
- **Coerenza eventuale**: i nodi convergono nel tempo
- **Coerenza causale**: relazioni causa-effetto preservate
- **Read-Your-Writes**: l'utente vede immediatamente i propri aggiornamenti
## Backup e ripristino
### Strategie di backup
- **Backup completo**: copia completa del database
- **Backup incrementale**: modifiche dall'ultimo backup
- **Backup differenziale**: modifiche dall'ultimo backup completo
- **Recupero point-in-time**: ripristina un momento specifico
- **Backup continuo**: replica in tempo reale sul backup
### Procedure di recupero
- **RTO (Recovery Time Objective)**: tempo di inattività massimo accettabile
- **RPO (Recovery Point Objective)**: massima perdita di dati accettabile
- **Piano di ripristino di emergenza**: procedure documentate in caso di guasti
- **Test**: esercizi di recupero regolari
##Sicurezza
### Controllo degli accessi
- **Autenticazione**: verifica l'identità dell'utente
- **Autorizzazione**: Concedere autorizzazioni (GRANT, REVOKE)
- **Ruoli**: autorizzazioni di gruppo per una gestione più semplice
- **Principio del privilegio minimo**: accesso minimo necessario
### Protezione dei dati
- **Crittografia a riposo**: crittografa i dati archiviati
- **Crittografia in transito**: TLS/SSL per le connessioni
- **Mascheramento**: nasconde i dati sensibili nella non produzione
- **Tokenizzazione**: sostituisci i dati sensibili con token
### Vulnerabilità comuni
- **SQL Injection**: SQL dannoso nell'input dell'utente
- **Escalation dei privilegi**: ottenimento dell'accesso non autorizzato
- **Registrazione di controllo**: traccia tutte le attività del database
- **Conformità**: requisiti GDPR, HIPAA, PCI-DSS
## Moderne tecnologie di database
### Database cloud
- **AWS**: RDS, Aurora, DynamoDB, Redshift
- **Google Cloud**: Cloud SQL, Spanner, Bigtable, Firestore
- **Azure**: database SQL, Cosmos DB, Synapse
- **Vantaggi**: servizio gestito, scalabilità automatica, backup inclusi
### Database NewSQL
- Combina la coerenza SQL con la scalabilità NoSQL
- **Esempi**: CockroachDB, TiDB, YugabyteDB, Google Spanner
- **Caratteristiche**: Distribuito, transazioni ACID, ridimensionamento orizzontale
### Database di serie temporali
- Ottimizzato per dati con timestamp
- **Esempi**: InfluxDB, TimescaleDB, Prometheus
- **Casi d'uso**: IoT, monitoraggio, dati finanziari
### Database vettoriali
- Memorizza ed interroga i vettori di incorporamento
- **Esempi**: Pigna, Milvus, Weaviate, Qdrant
- **Casi d'uso**: ricerca semantica, sistemi di raccomandazione, applicazioni AI
### Database multimodello
- Supporta più modelli di dati in un unico sistema
- **Esempi**: ArangoDB, OrientDB, Azure Cosmos DB
- **Vantaggio**: flessibilità senza più database
## ORM e accesso ai dati
### Mappatura relazionale degli oggetti
- **Scopo**: mappare le tabelle del database sugli oggetti di programmazione
- **ORM popolari**:
  - Python: SQLAlchemy, Django ORM, Peewee
  - JavaScript: Sequelizza, Prisma, TypeORM
  - Java: ibernazione, JPA
  - Rubino: ActiveRecord
  - .NET: struttura dell'entità
### Vantaggi
- Astrazione da SQL
- Digitare la sicurezza
- Gestione della migrazione
- API per la creazione di query
### Inconvenienti
- Sovraccarico delle prestazioni
-Query complesse più difficili da scrivere
- N+1 problemi di query
- Curva di apprendimento
## Amministrazione del database
### Responsabilità del DBA
- Installazione e configurazione
- Ottimizzazione delle prestazioni
- Backup e ripristino
- Gestione della sicurezza
- Pianificazione della capacità
- Monitoraggio e allerta
- Gestione delle patch
### Metriche di monitoraggio
-Tempo di risposta alla domanda
- Throughput (transazioni al secondo)
- Conteggio delle connessioni
- Rapporto di riscontro nella cache
- I/O del disco
- Blocca il tempo di attesa
- Ritardo di replica
### Attività di manutenzione
- **Aspira/Analizza**: aggiorna le statistiche, recupera spazio
- **Ricostruzione dell'indice**: deframmentazione degli indici
- **Aggiornamenti statistici**: tieni informato Query Optimizer
- **Rotazione registri**: gestisci le dimensioni dei file di registro
- **Pianificazione della capacità**: prevedere la crescita, pianificare gli aggiornamenti