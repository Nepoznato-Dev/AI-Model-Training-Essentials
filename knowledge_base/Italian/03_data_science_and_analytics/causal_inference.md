---
# Metadata
title: "Causal Inference"
description: "DAGs, confounders, difference-in-differences, instrumental variables"
category: "Data Science and Analytics"
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
reviewed_by: "Data Science & Analytics Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [causal, inference, data-science-and-analytics]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "5 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Inferenza causale
L'inferenza causale è la scienza che determina se una cosa effettivamente ne causa un'altra, non solo se sono correlate. La correlazione ti dice che due variabili si muovono insieme. La causalità ti dice che cambiando uno cambierà anche l’altro. Questa distinzione conta enormemente in medicina (funziona questo farmaco?), politica (questo intervento riduce la povertà?), affari (questa campagna pubblicitaria aumenta le vendite?) e scienza (questo meccanismo spiega il fenomeno?).
---

## Correlazione vs causalità
| Concetto | Descrizione | Esempio |
|---------|-----|---------|
| **Correlazione** | Due variabili si muovono insieme | In estate aumentano le vendite di gelati e le morti per annegamento |
| **Causa** | Una variabile influenza direttamente un'altra | Il fumo provoca il cancro ai polmoni |
| **Confusione** | Una terza variabile causa entrambi | Il caldo provoca sia la vendita di gelati che il nuoto (e l'annegamento) |
| **Causalità inversa** | L'effetto in realtà causa la presunta causa | Le persone acquistano integratori perché sono malate, non il contrario |
| **Correlazione spuria** | Rapporto casuale | Il consumo pro capite di formaggio è correlato ai decessi dovuti a lenzuola impigliate |
---

## Il quadro dei risultati potenziali
### Modello causale di Rubin
| Concetto | Descrizione |
|---------|-----|
| **Risultati potenziali** | Per ogni unità c'è un esito se trattata Y(1) e un esito se non trattata Y(0) |
| **Effetto del trattamento** | La differenza: Y(1) - Y(0) per una data unità |
| **Problema fondamentale** | Non possiamo mai osservare sia Y(1) che Y(0) per la stessa unità: possiamo vederne solo uno |
| **Effetto medio del trattamento (ATE)** | La media degli effetti del trattamento individuale nella popolazione |
| **Controfattuale** | Il risultato non osservato: cosa sarebbe successo nell'altra condizione |
### Presupposti chiave
| Presupposto | Significato | Come soddisfare |
|-----------|--------|----------------|
| **Ignorabilità (inconfondibilità)** | L'assegnazione del trattamento è indipendente dai potenziali risultati, date le covariate osservate | Randomizzazione; misurare tutti i confondenti |
| **Positività (sovrapposizione)** | Ogni unità ha una probabilità diversa da zero di ricevere uno dei trattamenti | Controlla la sovrapposizione della covariata tra i gruppi |
| **SUTVA** (Assunzione del valore del trattamento unitario stabile) | Il trattamento di un'unità non influisce sul risultato di un'altra; il trattamento è coerente | Nessuna interferenza; nessuna versione nascosta del trattamento |
| **Coerenza** | Il risultato osservato è uguale al risultato potenziale con il trattamento ricevuto | Trattamento ben definito |
---

## Metodi per l'inferenza causale
### Metodi sperimentali
| Metodo | Descrizione | Forza | Limitazione |
|--------|-----|----------|----|
| **Studio randomizzato e controllato (RCT)** | Assegnare casualmente le unità al trattamento o al controllo | Standard aureo; elimina la confusione | Costoso; a volte non etico; potrebbe non generalizzare |
| **Test A/B** | RCT in un contesto business/tecnologico | Semplice; rigoroso | Metriche a breve termine; effetti di novità; interferenza |
| **Esperimenti di ritorno** | Trattamento alternativo nel corso dei periodi | Gestisce le interferenze nei mercati | Richiede un ambiente stabile |
### Metodi quasi-sperimentali
| Metodo | Descrizione | Presupposto chiave |
|--------|-------------|----------------|
| **Differenza nelle differenze (DiD)** | Confrontare la variazione dei risultati tra i gruppi trattati e quelli di controllo nel tempo | Tendenze parallele: i gruppi avrebbero seguito la stessa traiettoria senza trattamento |
| **Discontinuità di regressione (RD)** | Confronta le unità appena sopra e appena sotto il limite di trattamento | Le unità vicine al limite sono comparabili (come se fossero casuali) |
| **Variabili strumentali (IV)** | Utilizzare una variabile che influisca sul trattamento ma non sul risultato se non attraverso il trattamento | Lo strumento è correlato al trattamento; influenza l'esito solo attraverso il trattamento |
| **Controllo sintetico** | Costruire una combinazione ponderata di unità di controllo in modo che corrisponda all'unità trattata | Il controllo sintetico rappresenta accuratamente il controfattuale | dell'unità trattata
| **Corrispondenza del punteggio di propensione** | Abbinare le unità trattate e quelle di controllo con probabilità di trattamento simili | Tutti i fattori confondenti vengono misurati e inclusi nel modello di propensione |
### Differenza nelle differenze (visualizzata)
| Periodo | Gruppo trattato | Gruppo di controllo | Differenza |
|--------|--------------|------|------------|
| **Pretrattamento** | Y_t_pre | Y_c_pre | Y_t_pre - Y_c_pre |
| **Post-trattamento** | Y_t_post | Y_c_post | Y_t_post - Y_c_post |
| **Stima DiD** | | | (Y_t_post - Y_t_pre) - (Y_c_post - Y_c_pre) |
---

## Grafici aciclici diretti (DAG)
I DAG sono strumenti visivi per codificare ipotesi causali e identificare i confondenti.
### Strutture di base
| Struttura | Modello | Implicazione |
|-----------|---------|-----|
| **Catena** | A → B → C | A e C sono associati tramite B; controllando per B blocca il percorso |
| **Forchetta** | A ← B → C | A e C vengono confusi da B; controllando per B blocca il percorso |
| **Collider** | A → B ← C | A e C sono indipendenti; il controllo per B apre il percorso (crea un'associazione spuria) |
### Regole per i DAG
| Regola | Descrizione |
|------|-------------|
| **Criterio backdoor** | Per stimare l'effetto causale di X su Y, bloccare tutti i percorsi backdoor (percorsi con una freccia in X) condizionando le variabili appropriate |
| **Criterio della porta d'ingresso** | Se i percorsi backdoor non possono essere bloccati, utilizzare i mediatori: stimare X → M → Y in due fasi |
| **Non condizionare sui collisori** | Il controllo per un effetto comune apre una strada spuria |
| **Non condizionare i discendenti dei collisori** | Stesso problema del condizionamento sul collisore stesso |
---

## Insidie ​​​​comuni
| Trappola | Descrizione | Esempio |
|---------|-----|---------|
| **Distorsione da variabili omesse** | Mancato controllo per un fattore confondente | Stima dell'istruzione → guadagni senza controllo delle capacità |
| **Controllo eccessivo** | Condizionamento su un mediatore o collisore | Controllo del titolo professionale nella stima dell'istruzione → guadagni |
| **Distorsione di selezione** | Condizionamento su una variabile influenzata dal trattamento | Analizzare solo gli occupati durante gli studi di formazione → salari |
| **Distorzione temporale immortale** | Classificazione errata del tempo-persona negli studi di coorte | I pazienti devono sopravvivere abbastanza a lungo per ricevere il trattamento |
| **Regressione alla media** | I valori estremi tendono a spostarsi verso la media | I pazienti malati migliorano nonostante il trattamento |
| **Distorsione post-trattamento** | Condizionamento sulle variabili che si verificano dopo il trattamento | Controllo degli eventi avversi nella stima dell'efficacia del farmaco |
---

## Strumenti e librerie
| Strumento | Lingua | Descrizione |
|------|----------|-------------|
| **FaiPerché** | Pitone | Biblioteca Microsoft; Inferenza causale basata su DAG |
| **CausaleML** | Pitone | Libreria di Uber per la modellazione del sollevamento e il ML causale |
| **EconML** | Pitone | Doppio ML, foreste causali, variabili strumentali |
| **modelli lineari** | Pitone | IV, modelli di dati panel, DiD |
| **Abbinalo** | R | Corrispondenza del punteggio di propensione |
| **dagitty** | R/rete | Analisi DAG; identificare i set di aggiustamento |
| **Impatto causale** | R/Pitone | Serie temporali strutturali bayesiane per l'inferenza causale |
---

## Riepilogo
L'inferenza causale consiste nell'andare oltre "ciò che è accaduto" verso "cosa sarebbe successo se le cose fossero state diverse". La sfida fondamentale è che non possiamo mai osservare sia i risultati trattati che quelli non trattati per la stessa unità: manca sempre il controfattuale. Gli esperimenti randomizzati risolvono questo problema rendendo comparabili i gruppi di trattamento e di controllo. Quando la randomizzazione non è possibile, metodi quasi sperimentali – DiD, discontinuità di regressione, variabili strumentali, controllo sintetico – cercano di ricostruire il controfattuale dai dati osservativi. I DAG aiutano a rendere esplicite le ipotesi e a identificare le giuste variabili da controllare. L'abilità chiave è pensare attentamente al processo di generazione dei dati: cosa causa cosa, cos'è un confondente, cos'è un collisore e cosa sarebbe successo in alternativa.