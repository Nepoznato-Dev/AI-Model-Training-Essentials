---
# Metadata
title: "Prompt Engineering"
description: "Prompt techniques and strategies"
category: "AI and Machine Learning"
subcategory: "Foundations"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "AI Model Training Team"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.1"
    date: "2026-08-09"
    author: "AI Model Training Team"
    changes: "Moved to foundations/ subfolder; added subcategory field"
  - version: "1.0.0"
    date: "2026-08-05"
    author: "AI Model Training Team"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-09"
review_date: "2027-02-05"
reviewed_by: "AI & Machine Learning Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [prompt, engineering, ai-and-machine-learning]
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

# Ingegneria rapida
Il prompt engineering è la pratica di progettare, perfezionare e ottimizzare i prompt di input per ottenere il miglior output possibile da un modello linguistico. È sia un'arte che una scienza ed è l'interfaccia principale per controllare il comportamento LLM senza messa a punto.
---

## Principi fondamentali
### Chiarezza e specificità
Un suggerimento chiaro non lascia spazio ad ambiguità. Specifica esattamente ciò che desideri, inclusi formato, lunghezza e prospettiva.
**Vago:**
> "Parlami di Python."
**Specifico:**
> "Spiega il Global Interpreter Lock (GIL) di Python. Descrivi il suo impatto sul multithreading, fornisci una soluzione alternativa e mantieni la tua risposta sotto le 200 parole."
### Fornisci il contesto
I modelli ottengono risultati migliori quando conoscono il ruolo, il pubblico e l'obiettivo.
**Senza contesto:**
> "Scrivi una funzione per ordinare un elenco."
**Con contesto:**
> "Sei uno sviluppatore Python senior. Scrivi una funzione per ordinare un elenco di dizionari in base a una determinata chiave. Utilizza suggerimenti di tipo e gestisci casi limite. Il pubblico è composto da sviluppatori junior."
### Usa istruzioni positive
Di' al modello cosa fare, non cosa evitare. "Non includere il gergo" è più debole di "Usa un linguaggio semplice accessibile a un bambino di 10 anni".
---

## Strutture di prompt
### Ruoli Sistema/Utente/Assistente
La maggior parte delle API LLM supportano una struttura multiturno:
- **Messaggio di sistema**: imposta il comportamento, la personalità e i vincoli del modello (persiste per l'intera sessione).
- **Messaggio utente**: la query o l'istruzione corrente.
- **Messaggio dell'assistente**: le risposte precedenti del modello (utilizzate per continuità).
**Esempio (stile API OpenAI):**
Sistema: sei un utile assistente di codifica. Rispondi con esempi di codice concisi e brevi spiegazioni. Non fornire mai codice non sicuro.
Utente: Scrivi una funzione Python per scaricare un file da un URL.
### Richiesta di pochi colpi
Fornisci 2-3 esempi del formato input-output desiderato prima di chiedere al modello di eseguire l'attività. Questo insegna il modello.
**Esempio:**
Utente: converti queste frasi in voce passiva:
Input: il gatto ha inseguito il topo.
Risultato: Il topo è stato inseguito dal gatto.
Input: lo chef ha cucinato il pasto.
Risultato: il pasto è stato cucinato dallo chef.
Input: La tempesta ha distrutto la casa.
Output: (il modello viene completato)
### Catena di pensiero (CoT)
Incoraggia il modello a mostrare il suo ragionamento passo dopo passo. Ciò migliora la precisione nelle attività aritmetiche, logiche e in più passaggi.
**Senza CdT:**
> "Che cos'è 24 × 37?"
**Con CoT:**
> "Calcola 24 × 37. Mostra il tuo ragionamento passo dopo passo."
Il modello produrrà passaggi intermedi, riducendo gli errori aritmetici.
### Risultati strutturati
Richiedi un formato specifico come JSON, YAML o tabelle di markdown per rendere affidabile l'analisi.
Utente: elenca tre vantaggi e tre svantaggi dei microservizi. Restituisce solo un oggetto JSON valido con le chiavi "pro" e "contro", ciascuno un array di stringhe.
---

##Tecniche avanzate
### Autocoerenza
Genera più risposte per lo stesso prompt (con una temperatura > 0) e ottieni un voto a maggioranza sulla risposta finale. Ciò è particolarmente efficace per i compiti di ragionamento.
### Albero dei pensieri
Esplora più percorsi di ragionamento in parallelo, valuta ciascuno e scegli quello migliore. Si tratta di una tecnica a livello di ricerca, ma può essere approssimata chiedendo al modello di "esplorare soluzioni alternative".
### ReAct (ragionamento + azione)
Lasciamo che il modello intercali il ragionamento con le chiamate agli strumenti. Può pensare, quindi agire (ad esempio, effettuare ricerche sul Web, eseguire codice), quindi ripensare in base al risultato.
**Struttura rapida:**
Hai accesso a una calcolatrice e a un motore di ricerca. Per ogni passaggio, output:
Pensiero: (il tuo ragionamento)
Azione: (nome strumento, input)
Osservazione: (output dello strumento)
... continua finché non avrai la risposta finale.
### Assegnazione della persona
Assegna un personaggio specifico per inquadrare la risposta.
**Esempi:**
- "Sei uno sviluppatore del kernel Linux e stai spiegando la gestione della memoria a un neolaureato."
- "Sei un nutrizionista amichevole che dà consigli generali a un cliente."
- "Sei un cinico critico tecnologico che recensisce un nuovo gadget."
---

## Regolazione dei parametri
- **Temperatura** (0,0 – 1,0+): controlla la casualità. Inferiore = più deterministico, superiore = più creativo. Utilizzare 0,0–0,3 per risposte basate sui fatti; 0,7–1,0 per la scrittura creativa.
- **Top-p** (campionamento del nucleo): elimina la massa di probabilità a una determinata soglia cumulativa. 0,9 significa che il modello campiona dal 90% dei token più probabili. Di solito regola la temperatura o la temperatura superiore, non entrambe.
- **Token massimi**: imposta la lunghezza massima dell'output. Ricordati di riservare spazio per la risposta all'interno della finestra di contesto.
- **Penalità di frequenza**: Riduce la ripetizione degli stessi token.
- **Penalità di presenza**: incoraggia il modello a introdurre nuovi argomenti.
---

## Insidie ​​​​e soluzioni comuni
| Problema | Probabile causa | Correzione |
|---------|------|-----|
| Il modello ignora parti del prompt | Richiesta troppo lunga o sovraccarica | Accorciare; metti l'istruzione più importante alla fine |
| L'output è troppo dettagliato | Nessun vincolo di lunghezza | Aggiungi "Limita a 3 frasi" o imposta max_tokens |
| L'output è troppo conciso | Eccessivamente restrittivo | Aggiungi "Spiega in dettaglio" o abbassa la temperatura |
| Allucinazioni reali | Contesto insufficiente o domanda ambigua | Aggiungi "Se non sei sicuro, dì 'Non lo so'" e fornisci un contesto RAG |
| Formattazione incoerente | Nessuna istruzione di formato esplicita | Richiedi JSON, tabella di ribasso o elenco puntato |
| Il modello risponde nella lingua sbagliata | Nessuna istruzione linguistica | Dichiara esplicitamente "Rispondi in inglese" (o nella lingua di destinazione) |
---

## Modelli di prompt per attività comuni
### Riepilogo
Riassumi il seguente testo in 3 punti elenco. Concentrarsi sugli argomenti principali ed evitare i dettagli.
Testo: [inserisci testo]

### Generazione di codici
Scrivi una funzione [linguaggio] che [fa X].
Requisiti:
Utilizza i suggerimenti sul tipo.
Includi una stringa di documento.
Gestire i casi limite: [elenco].
Non utilizzare librerie esterne se non diversamente specificato.

### Spiegazione
Spiegare [concetto] a un [non esperto/studente universitario/bambino]. Usa un'analogia dove appropriato.
### Brainstorming
Genera 10 idee per [argomento]. Per ogni idea, fornisci una descrizione di una frase e una potenziale sfida.
testo
### Classificazione
Classificare il seguente feedback dei clienti come [positivo, neutro, negativo].
Fornire un punteggio di confidenza (0-100) e una breve motivazione.
Feedback: [inserire testo]
### Traduzione con stile
Traduci il seguente testo dall'inglese allo spagnolo. Utilizza un tono informale adatto a un post sui social media.
Testo: [inserisci testo]
---

## Valutazione dei suggerimenti
Tratta i prompt come codice: eseguine la versione, testali e ripeti.
- **Test A/B** diverse varianti di prompt su una serie di query trattenute.
- **Misura il successo** tramite valutazione umana o metriche automatizzate (ad es. corrispondenza esatta, BLEU, punteggio personalizzato).
- **Conserva un registro dei prompt** (un semplice file di testo o foglio di calcolo) con il prompt, la versione e le prestazioni osservate.
---