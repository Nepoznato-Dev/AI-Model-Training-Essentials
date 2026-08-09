---
# Metadata
title: "Testing Methodologies"
description: "Unit, integration, E2E, TDD, BDD, test pyramids"
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
tags: [testing, methodologies, coding-and-technology]
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
# Metodologie di test
Il test ti consente di acquisire la certezza che il tuo codice funziona e, cosa ancora più importante, che le modifiche apportate non interrompano ciò che già funziona. Un buon testing rileva i bug prima che lo facciano gli utenti, documenta il comportamento previsto e consente un refactoring senza paura. Questo file copre l'intero spettro delle strategie di test, dai test unitari ai test end-to-end, e i principi che rendono i test efficaci.
---

## La Piramide dei Test
La piramide dei test descrive la distribuzione ideale dei test in un progetto.
```
        /  E2E  \          ← Few; slow; expensive; test the whole system
       /─────────\
      / Integration\       ← Some; test how components work together
     /───────────────\
    /   Unit Tests    \    ← Many; fast; cheap; test individual functions
   /─────────────────────\
```

| Livello | Conte | Velocità | Costo | Cosa prova |
|-------|-------|-------|------|------|
| **Unità** | Molti | Veloce (ms) | Basso | Funzioni individuali, classi, metodi |
| **Integrazione** | Alcuni | Medio (100 ms-s) | Medio | Come interagiscono i componenti; interrogazioni del database; Chiamate API |
| **E2E** | Pochi | Lento (secondi-minuti) | Alto | L'utente completo scorre attraverso il sistema reale |
---

## Test unitari
Testare singole unità di codice in modo isolato.
### Principi
| Principio | Descrizione |
|-----------|-------------|
| **Veloce** | Ogni test dovrebbe essere eseguito in millisecondi |
| **Isolato** | I test non dipendono l'uno dall'altro; nessuno stato condiviso |
| **Deterministico** | Stesso input → stesso output ogni volta (nessuna casualità, nessuna dipendenza dal tempo) |
| **Autocontrollo** | Il test supera o fallisce automaticamente; nessuna ispezione manuale |
| **Puntuale** | Scritto accanto o prima del codice (TDD) |
### Anatomia di un test
| Fase | Descrizione |
|-------|-------------|
| **Disporre** | Configurare i dati di test e le dipendenze |
| **Atto** | Chiama la funzione o il metodo da testare |
| **Affermare** | Verificare che il risultato corrisponda alle aspettative |
### Cosa testare
| Categoria | Esempi |
|----------|---------|
| **Buon cammino** | Gli input normali producono gli output attesi |
| **Casi limite** | Input vuoto, null, zero, valori massimi, singolo elemento |
| **Casi di errore** | Inserimento non valido, dati mancanti, autorizzazione negata |
| **Condizioni al contorno** | Fuori per uno; esattamente ai limiti |
### Derisioni e sciocchezze
| Termine | Descrizione | Quando usarlo |
|------|-------------|-----|
| **Fintura** | Un oggetto falso che registra come è stato chiamato | Verifica delle interazioni (si chiamava questo metodo?) |
| **Stub** | Un oggetto falso che restituisce valori predeterminati | Fornire dati di test (restituire questo utente dal database) |
| **Spia** | Un wrapper che registra le chiamate ad un oggetto reale | Verifica parziale |
| **Falso** | Un'implementazione semplificata ma funzionante | Database in memoria per i test |
| Biblioteca beffarda | Lingua |
|----------------|--------|
| **unittest.mock** | Pitone |
| **Scherzo** | JavaScript/TypeScript |
| **Mockito** | Giava |
| **Moq** | C# |
| **testimoniare / prendere in giro** | Vai |
---

## Test di integrazione
Testare il modo in cui più componenti lavorano insieme.
| Cosa testare | Esempio |
|-------------|---------|
| **Query sul database** | L'ORM produce l'SQL corretto? Vengono utilizzati gli indici? |
| **Endpoint API** | Il ciclo completo di richiesta-risposta funziona? |
| **Interazioni di servizio** | Il servizio A chiama correttamente il servizio B? |
| **Dipendenze esterne** | L'integrazione del gateway di pagamento funziona? |
### Strategie
| Strategia | Descrizione | Scambio |
|----------|-------------|-----------|
| **Dipendenze reali** | Utilizza un database reale, una coda di messaggi reale | Il più realistico; Più lentamente; più difficile da configurare |
| **Contenitori di prova** | Avvia i contenitori Docker per ogni esecuzione di test | Buon equilibrio; riproducibile |
| **Alternative in memoria** | H2 invece di PostgreSQL; bus di messaggi in memoria | Veloce; potrebbero perdere problemi del mondo reale |
| **Test del contratto** | Verificare che i servizi rispettino i contratti API | Cattura le modifiche all'interfaccia |
---

## Test end-to-end (E2E).
Testare il sistema completo dal punto di vista dell'utente.
| Strumento | Digitare | Ideale per |
|------|------|----------|
| **Drammaturgo** | Automazione del browser | Applicazioni Web; cross-browser |
| **Cipresso** | Automazione del browser | Applicazioni Web; esperienza di sviluppatore |
| **Selenio** | Automazione del browser | Eredità; ampio supporto linguistico |
| **Disintossicante** | Cellulare E2E | App React Native |
| **Appio** | Cellulare E2E | App mobili native e ibride |
| **Maestro** | Cellulare E2E | App mobili; semplice sintassi YAML |
| **k6 / Locusta** | Test di carico | Prestazioni sotto carico |
### Migliori pratiche E2E
| Pratica | Perché |
|----------|-----|
| **Testare solo percorsi critici** | I test E2E sono lenti; concentrati su ciò che conta di più |
| **Utilizza data factory di test** | Creare dati di test a livello di codice; non fare affidamento sui dati seed |
| **Pulire dopo i test** | Ogni test dovrebbe lasciare il sistema in uno stato noto |
| **Evita di testare i dettagli dell'interfaccia utente** | Comportamento del test, non classi CSS o posizioni degli elementi |
| **Esegui in CI** | I test E2E devono essere eseguiti automaticamente ad ogni modifica |
---

## Sviluppo basato sui test (TDD)
Scrivi prima il test, poi scrivi il codice per farlo passare.
| Passo | Descrizione |
|------|-------------|
| **1. Rosso** | Scrivere un test fallito che descriva il comportamento desiderato |
| **2. Verde** | Scrivi il codice minimo per far passare il test |
| **3. Refactoring** | Pulisci il codice mantenendo i test verdi |
| Vantaggio | Descrizione |
|---------|-----|
| **Feedback sul design** | I test ti costringono a pensare alle interfacce prima dell'implementazione |
| **Sicurezza della regressione** | Ogni bug viene sottoposto a un test; il bug non potrà mai restituire |
| **Documentazione** | I test servono come documentazione vivente del comportamento atteso |
| **Fiducia** | L'elevata copertura dei test consente un refactoring senza paura |
---

## Sviluppo guidato dal comportamento (BDD)
BDD estende il TDD scrivendo test in linguaggio naturale che descrivono il comportamento dal punto di vista dell'utente.
### Formato dato-quando-allora
```
Given a user with an empty shopping cart
When they add a "Python Book" priced at $29.99
Then the cart total should be $29.99
And the cart should contain 1 item
```

| Strumento | Lingua |
|------|----------|
| **Cetriolo** | Java, JavaScript, Ruby e altri |
| **Comportarsi bene** | Pitone |
| **SpecFlusso** | C# |
| **Jest** (con descrizione/it) | JavaScript |
---

## Altri tipi di test
| Digitare | Cosa prova | Strumenti |
|------|--------------|-------|
| **Prestazioni/Carico** | Comportamento del sistema sotto carico | k6, JMeter, Locusta, Gatling |
| **Sicurezza** | Vulnerabilità e vettori di attacco | OWASP ZAP, Burp Suite, Snyk |
| **Accessibilità** | Conformità WCAG | ascia, faro, pa11y |
| **Contratto** | Compatibilità API tra servizi | Patto, Contratto Cloud di Primavera |
| **Mutazione** | Qualità della suite di test stessa | Stryker, Mumut, PIT |
| **Regressione visiva** | Modifiche all'interfaccia utente tra le versioni | Percy, Cromatico, BackstopJS |
| **Caos** | Resilienza del sistema ai guasti | Scimmia del caos, tornasole, gremlin |
| **Fumo** | Funzionalità di base dopo la distribuzione | Script personalizzati; controlli sanitari |
| **Immergere** | Comportamento del sistema nel tempo prolungato | Prove di carico a lungo termine |
---

## Organizzazione delle prove
| Modello | Descrizione | Quando usarlo |
|---------|-----|-----|
| **Co-localizzato** | Test accanto al codice che testano (`src/utils.test.ts`) | La maggior parte dei progetti; facile da trovare |
| **Directory separata** | Test in una cartella`tests/`o`__tests__/`| Grandi progetti; netta separazione |
| **Apparecchi di prova** | Dati di test condivisi in una directory`fixtures/`| Quando più test necessitano degli stessi dati |
| **Utilità di test** | Helper condivisi in una directory`test-utils/`| Quando la logica di installazione è complessa |
---

## Copertura del codice
| Metrico | Cosa misura | Limitazione |
|--------|-----------|------------|
| **Copertura della linea** | Percentuale di righe di codice eseguite dai test | Non misura la qualità delle asserzioni |
| **Copertura filiale** | Percentuale di filiali (se/altro) occupate | Migliore della copertura della linea; ancora non rileva tutti i bug |
| **Copertura del percorso** | Percentuale di percorsi di esecuzione seguiti | Molto approfondito; esponenziale in codice complesso |
| **Punteggio di mutazione** | Percentuale di mutazioni rilevate dai test | Migliore misura della qualità del test |
**Obiettivo**: la copertura della linea dell'80% è un valore predefinito ragionevole. Ma la copertura è una guida, non un obiettivo: una copertura del 100% con asserzioni deboli è peggiore di una copertura del 70% con test approfonditi.
---

## Integrazione e test continui
| Pratica | Descrizione |
|----------|-------------|
| **Esegui tutti i test unitari su ogni commit** | Risposte veloci; rileva immediatamente le regressioni |
| **Esegui test di integrazione su PR** | Rileva i problemi che i test unitari non rilevano |
| **Esegui test E2E ogni notte o durante l'unione a principale** | Lento ma approfondito |
| **Fallire velocemente** | Interrompere la pipeline al primo guasto per risparmiare tempo |
| **Politica di test instabile** | Mettere in quarantena o eliminare immediatamente i test instabili; non ignorare mai |
| **Test di parallelizzazione** | Esegui test in parallelo per ridurre il tempo CI |
---

## Consigli pratici
- **Nomina i test in modo chiaro.**`test_calculates_tax_for_high_earner`ti dice cosa si è rotto. `test_1`non ti dice nulla.
- **Un'asserzione per test (quando pratico).** Semplifica la diagnosi dei guasti.
- **Non testare i dettagli di implementazione.** Testare il comportamento. Se si esegue il refactoring interno, i test non dovrebbero interrompersi.
- **Evita di testare codice di terze parti.** Librerie esterne fittizie; testa l'interazione del tuo codice con loro.
- **Esegui test velocemente.** Se la tua suite di test impiega 10 minuti, gli sviluppatori ne interromperanno l'esecuzione. Ottimizza incessantemente.
- **Elimina i test non funzionanti.** I test che superano sempre o testano il codice rimosso sono rumorosi.
- **Tratta il codice di test come codice di produzione.** Dovrebbe essere leggibile, gestibile e ben strutturato.
---

## Riepilogo
Il test non è facoltativo: è il modo in cui crei un software che non si rompe. La piramide dei test ti guida verso numerosi test unitari rapidi, alcuni test di integrazione e alcuni test E2E. TDD e BDD forniscono approcci strutturati. La simulazione isola le unità per i test. La copertura del codice misura l’ampiezza ma non la profondità. Il principio più importante è questo: se non viene testato, è rotto: semplicemente non lo sai ancora.