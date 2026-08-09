---
# Metadata
title: "Game Theory and Strategic Thinking"
description: "Nash equilibrium, prisoner's dilemma, mechanism design, auctions"
category: "Business and Economics"
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
reviewed_by: "Business & Economics Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [game, theory, business-and-economics]
difficulty_level: "beginner"
prerequisites: []
estimated_reading_time: "7 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Teoria dei giochi e pensiero strategico
La teoria dei giochi è lo studio matematico delle interazioni strategiche: situazioni in cui il tuo risultato dipende non solo da ciò che fai, ma da ciò che fanno gli altri. Si applica ovunque: competizione commerciale, relazioni internazionali, aste, negoziazioni, biologia evolutiva e decisioni quotidiane come scegliere un percorso nel traffico. L’intuizione fondamentale è che gli attori razionali in situazioni strategiche non si limitano a ottimizzare la propria strategia, ma anticipano ciò che faranno gli altri e gli altri faranno lo stesso.
---

## Concetti fondamentali
### Terminologia chiave
| Termine | Definizione |
|------|-----------|
| **Gioco** | Qualsiasi situazione con due o più decisori (giocatori) le cui scelte influenzano i reciproci risultati |
| **Giocatore** | Un decisore nel gioco |
| **Strategia** | Un piano d'azione completo per ogni situazione che potrebbe presentarsi |
| **Ricompensa** | Il risultato che un giocatore riceve da una particolare combinazione di strategie |
| **Equilibrio di Nash** | Un insieme di strategie in cui nessun giocatore può migliorare il proprio profitto modificando unilateralmente la propria strategia |
| **Strategia dominante** | Una strategia che è la migliore indipendentemente da ciò che fanno gli altri giocatori |
| **Gioco a somma zero** | Il guadagno di un giocatore è esattamente la perdita di un altro |
| **Gioco a somma non zero** | I giocatori possono potenzialmente guadagnare o perdere tutti |
| **Gioco cooperativo** | I giocatori possono stipulare accordi vincolanti |
| **Gioco non cooperativo** | Nessun accordo vincolante; ogni giocatore agisce nel proprio interesse |
---

## Giochi classici
### Il dilemma del prigioniero
Due sospetti vengono arrestati. Ciascuno può collaborare (tacere) o defezionare (confessare).
| | B Coopera | B Difetti |
|---|-----|---|
| **A collabora** | A: 1 anno, B: 1 anno | A: 10 anni, B: gratis |
| **A Difetti** | A: gratis, B: 10 anni | A: 5 anni, B: 5 anni |
| Approfondimento | Descrizione |
|---------|-----|
| **Strategia dominante** | Il difetto è dominante per entrambi i giocatori |
| **Equilibrio di Nash** | Entrambi difettosi (5 anni ciascuno) |
| **Ottimo paretiano** | Entrambi collaborano (1 anno ciascuno) |
| **Lezione** | Decisioni individuali razionali possono portare a risultati collettivamente peggiori |
### Altri giochi classici
| Gioco | Descrizione | Equilibrio di Nash | Lezione |
|------|---------------------|-----------------|--------|
| **Pollo (Falco-Colomba)** | Due autisti si dirigono l'uno verso l'altro; sterzare o andare dritto | Uno sterza, uno va dritto | politica del rischio calcolato; credibilità dell'impegno |
| **Caccia al cervo** | Cacciare insieme un cervo (risultato alto) o cacciare una lepre da soli (risultato basso) | Entrambi i cervi o entrambi le lepri | Coordinamento; fiducia |
| **Battaglia dei sessi** | Due giocatori preferiscono risultati diversi ma vogliono coordinarsi | Entrambi vanno allo stesso evento | Equilibri multipli; chi muove per primo ha vantaggio |
| **Gioco definitivo** | Il proponente divide i soldi; il risponditore accetta o rifiuta (entrambi non ottengono nulla) | Il proponente offre un minimo; il risponditore accetta | Le persone rifiutano le offerte ingiuste (irrazionali ma comuni) |
| **Gioco di beni pubblici** | Contribuisci a un pool condiviso o fai un giro gratuito | Tutti freeride | Tragedia dei beni comuni; necessità di applicazione |
---

## Tipi di giochi
### Per tempistica
| Digitare | Descrizione | Esempio |
|------|-------------|---------|
| **Simultaneo** | I giocatori si muovono contemporaneamente (o senza conoscere le mosse degli altri) | Forbici-sasso; aste a busta chiusa |
| **Sequenziale** | I giocatori si muovono uno dopo l'altro; i giocatori successivi osservano le mosse precedenti | Scacchi; decisioni di ingresso sul mercato |
| **Ripetuto** | Stesso gioco giocato più volte | Dilemma del prigioniero ripetuto; concorrenza tra imprese in corso |
### Per informazione
| Digitare | Descrizione | Esempio |
|------|-------------|---------|
| **Informazioni perfette** | Tutti i giocatori conoscono tutte le mosse precedenti | Scacchi; dama |
| **Informazione imperfetta** | Alcune mosse sono nascoste | Poker; concorrenza tra imprese |
| **Informazione completa** | Tutti i giocatori conoscono tutti i guadagni e le strategie | La maggior parte dei giochi da manuale |
| **Informazioni incomplete** | Alcuni pagamenti o tipi sono sconosciuti | Aste; trattative |
---

## Concetti di soluzione
### Equilibrio di Nash
| Aspetto | Descrizione |
|--------|-------------|
| **Definizione** | Nessun giocatore può migliorare il proprio profitto cambiando da solo la propria strategia |
| **Come trovarlo** | Per ogni giocatore, trova la migliore risposta alle strategie degli altri; dove si intersecano tutti è l'equilibrio di Nash |
| **Esistenza** | Ogni gioco finito ha almeno un equilibrio di Nash (possibilmente in strategie miste) |
| **Unicità** | I giochi possono avere più equilibri di Nash; sorgono problemi di coordinamento |
| **Limitazione** | L'equilibrio di Nash non ti dice quale equilibrio verrà selezionato; non tiene conto dell'equità |
### Equilibrio nella strategia dominante
| Passo | Descrizione |
|------|-------------|
| **1. Individuare le strategie** | Elenca tutte le strategie disponibili per ciascun giocatore |
| **2. Trova strategie dominanti** | Una strategia che è la migliore indipendentemente da ciò che fanno gli altri |
| **3. Se tutti i giocatori ne hanno uno** | La combinazione è l’equilibrio della strategia dominante |
| **4. In caso contrario** | Utilizzare l'eliminazione iterata delle strategie dominate o l'equilibrio di Nash |
### Induzione all'indietro (giochi sequenziali)
| Passo | Descrizione |
|------|-------------|
| **1. Disegna l'albero del gioco** | Nodi = punti decisionali; rami = azioni |
| **2. Inizia dalla fine** | Identificare la scelta ottimale dell'ultimo giocatore in ciascun nodo terminale |
| **3. Lavorare all'indietro** | In ogni nodo precedente, scegli l'azione che porta al miglior risultato |
| **4. Risultato** | Equilibrio perfetto del sottogioco: strategia ottimale in ogni punto decisionale |
---

## Concetti avanzati
### Strategie miste
| Concetto | Descrizione | Esempio |
|---------|-----|---------|
| **Strategia mista** | Randomizzazione tra le azioni in base alle probabilità | Sasso-carta-forbici: gioca ciascuno con 1/3 di probabilità |
| **Perché randomizzare?** | Impedisce agli avversari di prevedere la tua mossa | Calci di rigore nel calcio; verifiche fiscali |
| **Equilibrio di Nash in strategia mista** | Ogni giocatore è indifferente tra le proprie strategie pure | Nessun giocatore può sfruttare l'altro |
### Giochi ripetuti e teoremi popolari
| Concetto | Descrizione |
|---------|-----|
| **Ripetuto infinitamente** | L’induzione all’indietro svela la cooperazione; come il gioco one-shot | La defezione dell'ultimo round si propaga all'indietro |
| **Ripetuto all'infinito** | La cooperazione può essere sostenuta attraverso la minaccia di future punizioni | Pan per focaccia; strategie di attivazione cupe |
| **Teorema popolare** | Qualsiasi payoff individualmente razionale può essere un equilibrio di Nash in un gioco ripetuto all’infinito | La cooperazione è possibile se il futuro conta abbastanza |
| **Fattore di sconto** | Quanto i giocatori apprezzano i guadagni futuri; più alto = maggiore cooperazione | I giocatori pazienti collaborano di più |
### Progettazione di meccanismi (teoria dei giochi inversi)
| Concetto | Descrizione |
|---------|-----|
| **Gol** | Progettare le regole di un gioco per ottenere il risultato desiderato |
| **Applicazioni** | Aste; sistemi di voto; progettazione contrattuale; progettazione del mercato |
| **Principio di rivelazione** | Qualsiasi risultato ottenibile con qualsiasi meccanismo può essere ottenuto mediante un meccanismo diretto veritiero |
| **Esempio** | Asta Vickrey (offerta sigillata al secondo prezzo): offrire il proprio valore reale è una strategia dominante |
---

## Applicazioni
### Attività commerciale
| Applicazione | Concetto di teoria dei giochi | Approfondimento |
|-------------|-----|---------|
| **Concorrenza sui prezzi** | Il dilemma del prigioniero | Le guerre sui prezzi danneggiano entrambe le aziende; collusione tacita in giochi ripetuti |
| **Ingresso sul mercato** | Gioco sequenziale; impegno | La minaccia dell'operatore storico di combattere l'ingresso è credibile solo se ha investito in capacità |
| **Aste** | Progettazione del meccanismo | Le aste di secondo prezzo suscitano valori reali; le aste dello spettro raccolgono miliardi |
| **Negoziazione** | Gioco di contrattazione; Equilibrio di Nash | Dividere il surplus; vantaggio della prima mossa nei giochi dell'ultimatum |
| **Segnalazione** | Il modello educativo di Spence | I segnali costosi sono credibili perché i tipi di bassa qualità non possono permetterseli |
### Relazioni internazionali
| Applicazione | Concetto di teoria dei giochi | Approfondimento |
|-------------|-----|---------|
| **Corsa agli armamenti** | Il dilemma del prigioniero | Entrambe le parti farebbero meglio a disarmarsi ma non possono fidarsi l'una dell'altra |
| **Guerre commerciali** | Gioco ripetuto | Tit-to-tat: cooperare fino a quando gli altri difetti, poi vendicarsi |
| **Accordi sul clima** | Gioco dei beni pubblici | Il free riding è razionale; necessari meccanismi di applicazione |
| **Deterrenza** | Pollo; impegno credibile | La distruzione reciprocamente assicurata è un equilibrio di Nash |
---

## Riepilogo
La teoria dei giochi studia le interazioni strategiche in cui il tuo risultato dipende dalle azioni degli altri. L’equilibrio di Nash – dove nessun giocatore trae beneficio dal solo cambiamento di strategia – è il concetto di soluzione centrale. Giochi classici come il dilemma del prigioniero mostrano che le decisioni individuali razionali possono produrre risultati collettivamente negativi. I giochi sequenziali vengono risolti per induzione all'indietro. I giochi ripetuti possono sostenere la cooperazione attraverso la minaccia di punizioni future. Le strategie miste implicano la randomizzazione per rimanere imprevedibili. La progettazione del meccanismo ribalta la questione: invece di prevedere i risultati, progetta regole per ottenere i risultati desiderati (come nelle aste). Le applicazioni spaziano dal mondo degli affari (prezzi, ingresso, aste), alla politica (voto, trattati), alla biologia (strategie evolutive stabili) e alla vita di tutti i giorni. La lezione fondamentale è che la strategia non riguarda solo ciò che si fa: si tratta di anticipare ciò che faranno gli altri, sapendo che anche loro faranno lo stesso.