<!--
---
# Metadata
title: "Machine Learning Project Failures"
description: "Data leakage, expectation mismatches, deployment failures, model decay"
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
tags: [ml, project, failures, lessons-from-failures]
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

-->
# Errori nei progetti di machine learning
I progetti di machine learning falliscono a un ritmo allarmante: le stime del settore suggeriscono che il 60-85% dei progetti ML non raggiungono mai la produzione. I fallimenti di solito non sono negli algoritmi; sono nel processo, nei dati, nelle aspettative e nel contesto organizzativo. Capire perché i progetti ML falliscono è essenziale per chiunque crei sistemi ML, perché le modalità di fallimento sono prevedibili e in gran parte evitabili.
---

## Perché i progetti ML falliscono
### Categorie di errori
| Categoria | Quota di fallimenti | Descrizione |
|----------|------------|-------------|
| **Problemi con i dati** | ~30% | I dati sono insufficienti, distorti, obsoleti o inaccessibili |
| **Definizione del problema** | ~20% | Il problema del machine learning non corrisponde alle esigenze aziendali |
| **Mancata corrispondenza delle aspettative** | ~15% | Le parti interessate si aspettano la magia; la realtà è un miglioramento incrementale |
| **Errore di distribuzione** | ~15% | Il modello funziona sui notebook ma non può essere messo in produzione |
| **questioni organizzative** | ~10% | Nessuna proprietà chiara; la squadra non ha competenze; nessun supporto esecutivo |
| **Prestazioni del modello** | ~10% | Il modello non raggiunge la precisione richiesta o si generalizza male |
---

## Errori relativi ai dati
### Problemi comuni con i dati
| Problema | Descrizione | Esempio |
|---------|-----|---------|
| **Dati insufficienti** | Esempi insufficienti per apprendere modelli significativi | Formazione su un modello di rilevamento delle frodi su 500 transazioni |
| **Qualità dell'etichetta** | Le etichette di formazione sono sbagliate, incoerenti o soggettive | Immagini mediche etichettate da non esperti; etichette di sentiment con basso accordo tra valutatori |
| **Perdita di dati** | Informazioni dal futuro o obiettivi si diffondono nelle funzionalità | Utilizzare il risultato del tasso di abbandono dei clienti come caratteristica; compresi i dati dei test nella formazione |
| **Distorsione di selezione** | I dati di addestramento non rappresentano la popolazione della distribuzione | Addestramento di un modello medico sui dati di un ospedale; distribuzione a livello nazionale |
| **Deriva del concetto** | La relazione tra caratteristiche e target cambia nel tempo | Il comportamento dei consumatori cambia dopo una pandemia; modello addestrato su dati pre-pandemia |
| **Mancata corrispondenza delle funzionalità** | Le funzionalità disponibili durante la formazione differiscono da quelle disponibili in produzione | Formazione con etichette manuali; la produzione utilizza etichette automatizzate con diversa distribuzione |
| **Squilibrio di classe** | Le classi target sono altamente distorte | 99% negativo, 1% positivo; il modello impara a prevedere sempre | negativo
### Il problema della fuga di dati
| Digitare | Descrizione | Esempio |
|------|-------------|---------|
| **Perdita di target** | Una funzionalità è disponibile solo dopo che si è verificata la destinazione | "Risultato del trattamento" utilizzato come caratteristica per prevedere il "successo del trattamento" |
| **Contaminazione da test del treno** | I dati dei test influenzano l'allenamento | Scalabilità con statistiche globali (include dati di test); aumento dei dati che perde |
| **Distorsione campionaria** | La formazione e la produzione utilizzano campionamenti diversi | Formazione sul traffico web; distribuzione sul traffico delle app mobili |
| **Perdita pre-elaborazione** | La fase di preelaborazione utilizza le informazioni dell'intero set di dati | Assegnazione dei valori mancanti con la media globale (include dati di test) |
---

## Errori nella definizione del problema
### Modelli di disallineamento
| Modello | Descrizione | Conseguenza |
|---------|-----|-----|
| **Risolvere il problema sbagliato** | L'azienda ha bisogno di X; la squadra costruisce Y | Il modello è tecnicamente buono ma inutile |
| **ML quando basterebbero le regole** | Il problema ha regole deterministiche; Il machine learning aggiunge complessità | Troppo ingegnerizzato; più difficile da mantenere; meno interpretabile |
| **ML quando i dati non esistono** | Il problema richiede dati che non sono stati raccolti | Il progetto non può iniziare; mesi sprecati sulla fattibilità |
| **Obiettivo di precisione senza contesto aziendale** | "Abbiamo bisogno di una precisione del 95%": ma cosa significa questo per l'azienda? | Il modello soddisfa la precisione ma non risolve il problema aziendale |
| **Ignorando il costo degli errori** | Falsi positivi e falsi negativi hanno costi diversi | Il modello ottimizza la metrica sbagliata |
| **Nessuna linea di base** | Nessun confronto con l'approccio esistente | Non posso dire se ML sia effettivamente migliore di una semplice euristica |
---

## Aspettative fallite
### Il ciclo dell'hype nei progetti ML
| Fase | Descrizione | Rischio |
|-------|-----|------|
| **Emozione** | "L'intelligenza artificiale risolverà tutto!" | Troppo promettente; risorse insufficienti |
| **Prova di concetto** | Il modello funziona su dati puliti nei notebook | Falsa fiducia; "funziona!" |
| **Verifica della realtà** | I dati di produzione sono confusi; le prestazioni scendono | Delusione; "ML non funziona" |
| **Marcia della morte** | Il team cerca di forzarlo nella produzione | Debito tecnico; esaurimento |
| **Abbandono o distribuzione silenziosa** | Progetto annullato o implementato senza monitoraggio | Investimento sprecato |
### Gestire le aspettative
| Strategia | Descrizione |
|----------|-------------|
| **Inizia con una linea di base** | Confrontare con l'approccio più semplice possibile (regole; prestazioni umane) |
| **Definire in anticipo le metriche di successo** | Metriche aziendali (entrate; risparmi sui costi) non solo metriche ML (precisione; F1) |
| **Esplorazione della scatola del tempo** | Concedere al team 2-4 settimane per valutare la fattibilità prima di impegnarsi |
| **Mostra cosa il machine learning non può fare** | Sii onesto riguardo ai limiti; stabilire aspettative realistiche |
| **Itera in modo incrementale** | Distribuire prima un modello semplice; migliorare iterativamente |
| **Quantificare il costo degli errori** | Tradurre le prestazioni del modello in impatto aziendale |
---

## Errori di distribuzione
### Perché le modelle non arrivano alla produzione
| Problema | Descrizione | Soluzione |
|---------|-------------|----------|
| **Notebook al gap produttivo** | Il codice funziona in Jupyter ma non è pronto per la produzione | pratiche MLOps; CI/CD per ML; revisione del codice |
| **Requisiti di latenza** | L'inferenza del modello è troppo lenta per l'uso in tempo reale | Ottimizzazione del modello; quantizzazione; memorizzazione nella cache |
| **Scalabilità** | Il modello non può gestire il traffico di produzione | Elaborazione batch; ridimensionamento orizzontale; modello al servizio delle infrastrutture |
| **Monitoraggio delle lacune** | Nessun modo per rilevare quando il modello si degrada | Monitoraggio della deriva dei dati; monitoraggio delle prestazioni; avviso |
| **Gestione delle dipendenze** | Gli ambienti di formazione e di servizio differiscono | Containerizzazione; ambienti riproducibili |
| **Nessun piano di ripristino** | Impossibile ripristinare il modello precedente quando il nuovo modello fallisce | Registro dei modelli; controllo delle versioni; rollback automatizzato |
### Decadimento del modello
| Digitare | Descrizione | Rilevazione |
|------|-------------|-----------|
| **Deriva dei dati** | Le distribuzioni delle funzionalità di input cambiano | Monitorare le statistiche delle funzionalità; divergenza KL; PSI |
| **Deriva del concetto** | Relazione tra caratteristiche e modifiche del target | Monitorare l'accuratezza della previsione nel tempo |
| **Deriva dell'etichetta** | Definizione o distribuzione delle modifiche target | Tieni traccia delle distribuzioni delle etichette; correlazione metrica aziendale |
| **Modifiche a monte** | L'origine dati cambia formato, tempistica o qualità | Convalida dello schema; monitoraggio della freschezza |
---

## Fallimenti organizzativi
| Fallimento | Descrizione | Prevenzione |
|---------|-----|------------|
| **Nessuna proprietà chiara** | Nessuno è responsabile del modello in produzione | Assegnare i proprietari del modello; definire RACI |
| **Squadre isolate** | I data scientist costruiscono modelli; gli ingegneri si schierano; nessuno comunica | Team interfunzionali; obiettivi condivisi |
| **Nessuna scadenza MLOps** | Nessun registro dei modelli; nessun CI/CD; nessun monitoraggio | Investire in modo incrementale nell'infrastruttura MLOps |
| **Cronologia non realistica** | "Costruisci un sistema ML di produzione in 2 settimane" | Esplorazione della scatola del tempo; ripetere; comunicare la complessità |
| **Mancanza di esperienza nel settore** | Il team ML non comprende il problema aziendale | Incorpora esperti di dominio nei team ML |
| **Nessun quadro di valutazione** | Non riesco a capire se il modello funziona in produzione | Definire le metriche aziendali; impostare dashboard; recensioni regolari |
---

## Lezioni apprese
### La lista di controllo del progetto ML
| Fase | Domanda chiave |
|-------|-------------|
| **Definizione del problema** | Si tratta effettivamente di un problema di machine learning? Qual è la linea di base? Che aspetto ha il successo? |
| **Valutazione dei dati** | Abbiamo abbastanza dati? È rappresentativo? Le etichette sono affidabili? |
| **Fattibilità** | Possiamo costruire un prototipo funzionante in 2-4 settimane? Quali sono i rischi? |
| **Sviluppo** | C'è perdita di dati? Stiamo utilizzando la giusta metrica di valutazione? |
| **Pre-produzione** | Funziona con i dati di produzione? È abbastanza veloce? È monitorato? |
| **Distribuzione** | Possiamo tornare indietro? Chi è di guardia? Cosa succede quando si degrada? |
| **Post-distribuzione** | Stiamo monitorando la deriva? I parametri aziendali vengono monitorati? Esiste un piano di riqualificazione? |
---

## Riepilogo
I progetti ML falliscono non perché gli algoritmi siano troppo complessi, ma perché il processo che li circonda è interrotto. I problemi relativi ai dati (dati insufficienti, etichette inadeguate, perdite, deviazioni) rappresentano la quota maggiore di fallimenti. Gli errori nella definizione del problema (risolvere il problema sbagliato, utilizzare il machine learning quando le regole sarebbero sufficienti, ignorare il costo degli errori) sprecano mesi di impegno. I fallimenti delle aspettative (promesse eccessive, risultati insufficienti e mancata gestione degli stakeholder) distruggono la fiducia dell'organizzazione nel machine learning. Gli errori di distribuzione (divari tra notebook e produzione, problemi di latenza, assenza di monitoraggio) fanno sì che i modelli che funzionano in fase di sviluppo non creino mai valore in produzione. I fallimenti organizzativi – nessuna proprietà, team isolati, nessun MLOps – rendono strutturalmente impossibile il successo. L'antidoto è una pratica disciplinata: iniziare con una linea di base; esplorazione della scatola del tempo; convalidare i dati in modo rigoroso; verificare eventuali perdite; definire le metriche aziendali; distribuire in modo incrementale; monitorare continuamente; e ripetere. I migliori team di ML dedicano più tempo ai dati e ai processi che ai modelli.