<!--
---
# Metadata
title: "AI Ethics and Governance"
description: "AI bias, fairness, accountability, regulation, governance frameworks"
category: "AI and Machine Learning"
subcategory: "Ethics and Safety"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "Nepoznato-Dev"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.1"
    date: "2026-08-09"
    author: "Nepoznato-Dev"
    changes: "Moved to ethics_and_safety/ subfolder; added subcategory field"
  - version: "1.0.0"
    date: "2026-08-05"
    author: "Nepoznato-Dev"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-09"
review_date: "2027-02-05"
reviewed_by: "AI & Machine Learning Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [ai, ethics, governance, ai-and-machine-learning]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "8 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Etica e governance dell'IA
I sistemi di intelligenza artificiale non sono neutrali. Riflettono i dati su cui sono stati formati, i valori dei loro creatori e gli incentivi delle organizzazioni che li implementano. L'etica consiste nel chiedersi non solo "possiamo costruire questo?" ma "dovremmo?" La governance riguarda la creazione di strutture – leggi, standard, organismi di supervisione – che garantiscono che l’intelligenza artificiale sia sviluppata e utilizzata in modo responsabile. Questo file copre le principali dimensioni etiche dell’IA e i quadri di governance che emergono per affrontarle.
---

## Principi etici fondamentali per l'intelligenza artificiale
La maggior parte dei quadri etici dell’IA convergono su una serie di principi condivisi.
| Principio | Cosa significa | Sfida |
|-----------|--------------|-----------|
| **Equità** | L'intelligenza artificiale non dovrebbe discriminare i gruppi protetti | Definire matematicamente l'equità è difficile; diverse definizioni di equità possono essere in conflitto |
| **Trasparenza** | Gli utenti dovrebbero sapere quando interagiscono con l'intelligenza artificiale e come funziona | La piena trasparenza può consentire il gioco; i sistemi proprietari resistono alla divulgazione |
| **Responsabilità** | Qualcuno deve essere responsabile quando l’IA causa danni | Responsabilità diffusa tra sviluppatori, distributori e utenti |
| **Privacy** | L'intelligenza artificiale dovrebbe rispettare i dati personali e l'autonomia | I dati di allenamento spesso includono informazioni personali; conflitto tra privacy e utilità |
| **Sicurezza** | L’intelligenza artificiale non dovrebbe causare danni fisici o psicologici | La definizione del danno dipende dal contesto; i casi limite sono imprevedibili |
| **Supervisione umana** | Gli esseri umani dovrebbero mantenere un controllo significativo | Il pregiudizio dell’automazione significa che gli esseri umani si affidano all’intelligenza artificiale; la supervisione diventa un'approvazione |
---

## Distorsione nei sistemi di intelligenza artificiale
### Da dove vengono i pregiudizi
| Fonte | Descrizione | Esempio |
|--------|-----|---------|
| **Dati di formazione** | Pregiudizi storici codificati nei dati | I dati sulle assunzioni riflettono le discriminazioni passate → il modello discrimina |
| **Pregiudizio sull'etichetta** | Gli annotatori umani impongono i loro pregiudizi | Curriculum con nomi "femminili" valutati inferiori dagli annotatori |
| **Distorsione di selezione** | I dati non rappresentano la popolazione target | Riconoscimento facciale addestrato principalmente su volti dalla pelle chiara |
| **Distorsione di misurazione** | Funzionalità proxy per attributi protetti | Il codice postale è correlato alla razza |
| **Distorsione algoritmica** | L'ottimizzazione amplifica i piccoli pregiudizi | Una piccola lacuna nei dati di addestramento diventa una grande lacuna nelle previsioni |
### Metriche di equità
| Metrico | Definizione | Quando usarlo |
|--------|-----------|-----|
| **Parità demografica** | Il tasso positivo è uguale tra i gruppi | Quando vuoi risultati uguali |
| **Quote pareggiate** | Il tasso di veri positivi e il tasso di falsi positivi sono uguali tra i gruppi | Quando vuoi tassi di errore uguali |
| **Parità predittiva** | La precisione è uguale tra i gruppi | Quando vuoi che i pronostici abbiano lo stesso significato per tutti i gruppi |
| **Equità individuale** | Individui simili vengono trattati in modo simile | Quando vuoi coerenza |
**Teorema dell'impossibilità**: generalmente non è possibile soddisfare più definizioni di equità contemporaneamente. Scegliere quale parametro di equità utilizzare è di per sé un giudizio di valore.
### Mitigazione dei pregiudizi
| Palcoscenico | Tecnica |
|-------|-----------|
| **Pre-elaborazione** | Riequilibrare i dati di allenamento; rimuovere le funzionalità distorte; sovracampionamento sintetico |
| **In elaborazione** | Aggiungere vincoli di equità alla funzione di perdita; debiasing contraddittorio |
| **Post-elaborazione** | Regolare le soglie per gruppo; calibrare le previsioni |
| **Valutazione** | Controlli regolari sull’equità; metriche di prestazione disaggregate |
---

## Spiegabilità
### Perché la spiegabilità è importante
| Motivo | Descrizione |
|--------|-------------|
| **Fiducia** | Gli utenti devono capire perché è stata presa una decisione |
| **Debug** | Gli sviluppatori devono trovare e correggere gli errori del modello |
| **Regolamento** | Il “diritto alla spiegazione” del GDPR; Requisiti della legge UE sull'IA |
| **Equità** | Non è possibile rilevare bias senza comprendere il comportamento del modello |
| **Responsabilità** | Le organizzazioni devono giustificare le decisioni automatizzate |
### Metodi di spiegazione
| Metodo | Digitare | Come funziona | Limitazione |
|--------|------|-----|------------|
| **SHAP** | Importanza delle caratteristiche | Stima il contributo di ciascuna funzionalità utilizzando la teoria dei giochi | Computazionalmente costoso; approssimazioni |
| **CALCE** | Surrogato locale | Adatta un modello semplice attorno alla previsione | Instabile; non riflette la logica del modello reale |
| **Visualizzazione dell'attenzione** | Meccanismo interno | Mostra a quali input si occupa il modello | Attenzione ≠ importanza; può essere fuorviante |
| **Controfattuali** | Analisi what-if | "Se questa caratteristica fosse diversa, la previsione cambierebbe?" | Dipende da controfattuali realistici |
| **Attribuzione funzionalità** | Punteggi di importanza | Mappe di salienza, gradienti integrati | Non spiega *perché*; proprio *dove* |
---

## Regolamento AI
### Legge dell'UE sull'IA (2026)
La prima legge completa al mondo sull’IA.
| Livello di rischio | Esempi | Requisiti |
|------------|----------|-------------|
| **Rischio inaccettabile** | Punteggio sociale; manipolazione subliminale; sorveglianza biometrica in tempo reale (con eccezioni) | Vietato |
| **Alto rischio** | IA medica; veicoli autonomi; forze dell'ordine; infrastrutture critiche | Valutazione della conformità; supervisione umana; trasparenza |
| **Rischio limitato** | Chatbot; falsi profondi; sistemi di raccomandazione | Deve rivelare il coinvolgimento dell'IA |
| **Rischio minimo** | Filtri anti-spam; videogiochi; la maggior parte delle applicazioni AI | Nessun requisito specifico |
### Altri approcci normativi
| Regione | Avvicinamento | Stato |
|--------|----------|--------|
| **Stati Uniti** | Specifico del settore; ordini esecutivi; impegni volontari | Frammentato; nessuna legge federale completa |
| **Regno Unito** | Basato su principi; regolatori del settore | Istituto per la sicurezza AI; approccio pro-innovazione |
| **Cina** | Norme specifiche per AI generativa, deepfake, raccomandazioni | Applicazione attiva; requisiti di contenuto |
| **Canada** | AIDA (Legge sull'intelligenza artificiale e sui dati) | Proposto; approccio simile all'UE |
| **Brasile** | Quadro normativo sull'IA | In corso |
---

## Impatto ambientale
L’addestramento e l’esecuzione di modelli di intelligenza artificiale consumano energia e generano emissioni di carbonio.
| Attività | Emissioni stimate | Confronto |
|----------|-------------|------------|
| **Formazione GPT-4** | Stimate oltre 50 tonnellate di CO₂ | Equivalente alle emissioni annue di diverse automobili |
| **Addestramento di un grande trasformatore** | 280-620 tonnellate di CO₂ | 5 volte le emissioni di un'auto nel corso della sua vita |
| **Inferenza giornaliera (1 milione di utenti)** | In corso; dipende dalle dimensioni del modello e dall'hardware | Può superare le emissioni di addestramento nel tempo |
| **Perfezionamento di un modello 7B** | 1-5 tonnellate di CO₂ | Significativo ma molto meno della pre-formazione |
### Mitigazione
| Strategia | Impatto |
|----------|--------|
| **Hardware efficiente** | Le nuove GPU sono più efficienti dal punto di vista energetico per calcolo |
| **Ottimizzazione del modello** | I modelli più piccoli e quantizzati utilizzano meno energia |
| **Energia verde** | Alimentare i data center con energia rinnovabile |
| **Architetture efficienti** | Miscela di esperti; modelli sparsi; distillazione |
| **Pianificazione consapevole del carbonio** | Esegui l'allenamento quando la griglia è più pulita |
---

## Proprietà intellettuale e diritto d'autore
| Problema | Descrizione | Stato |
|-------|-------------|--------|
| **Formazione sulle opere protette da copyright** | Modelli addestrati su libri, articoli, immagini senza autorizzazione | Cause attive; dibattito sul fair use |
| **Output generato dall'intelligenza artificiale** | Chi possiede i contenuti generati dall'intelligenza artificiale? | US Copyright Office: i contenuti generati dall'intelligenza artificiale non sono protetti da copyright senza una sufficiente paternità umana |
| **Imitazione di stile** | L'intelligenza artificiale può imitare lo stile di un artista | Legalmente grigio; preoccupazioni etiche |
| **Meccanismi di opt-out** | Alcuni fornitori consentono ai creatori di rinunciare alla formazione | robots.txt; filtraggio dei contenuti |
---

## Divulgazione responsabile
| Principio | Descrizione |
|-----------|-------------|
| **Test pre-implementazione** | Red teaming, controlli di bias, valutazioni di sicurezza prima del rilascio |
| **Distribuzione graduale** | Inizia con un accesso limitato; espandersi man mano che la sicurezza viene dimostrata |
| **Segnalazione degli incidenti** | Documentare e condividere informazioni su guasti e danni |
| **Premi bug** | Premiare i ricercatori esterni per aver trovato le vulnerabilità |
| **Schede modello** | Funzionalità, limitazioni e uso previsto del modello documentale |
---

## Provenienza dei dati
| Preoccupazione | Descrizione |
|---------|-----|
| **Trasparenza dei dati formativi** | La maggior parte dei modelli di frontiera non divulgano i propri dati di addestramento |
| **Consenso** | I dati degli individui sono stati utilizzati con la loro consapevolezza e autorizzazione? |
| **Avvelenamento dei dati** | Gli aggressori possono inserire dati dannosi nei set di addestramento? |
| **Schede con set di dati** | Documentazione della composizione del set di dati, metodi di raccolta e limitazioni |
| **Filigrana** | Incorporamento di marcatori invisibili nei contenuti generati dall'intelligenza artificiale per identificarli |
---

## Quadri etici pratici
### Per gli sviluppatori IA
| Domanda | Perché è importante |
|----------|---------------|
| **Chi potrebbe essere danneggiato da questo sistema?** | Identifica le parti interessate interessate |
| **Cosa succede se il modello è sbagliato?** | Valuta il costo degli errori |
| **Si possono spiegare le decisioni del modello?** | Determina i requisiti di spiegabilità |
| **I dati di allenamento sono rappresentativi?** | Controlla la selezione e la distorsione della misurazione |
| **Quali sono le modalità di errore?** | Anticipa casi limite e abusi |
| **Come verrà monitorato il sistema?** | Piani per la sorveglianza continua |
### Per le organizzazioni che utilizzano l'intelligenza artificiale
| Pratica | Descrizione |
|----------|-------------|
| **Consiglio di governance dell'IA** | Team interfunzionale che esamina le implementazioni dell'intelligenza artificiale |
| **Valutazioni d'impatto** | Valutare i potenziali danni prima della distribuzione |
| **Processi di supervisione umana** | Chiari percorsi di escalation quando l'IA commette errori |
| **Audit periodici** | Verificare la presenza di bias, derive e conseguenze indesiderate |
| **Canali di feedback degli utenti** | Consentire alle persone interessate di segnalare problemi |
| **Documentazione** | Conservare i registri delle decisioni e delle motivazioni del modello |
---

## Riepilogo
L'etica e la governance dell'IA non sono ripensamenti: sono requisiti ingegneristici. I pregiudizi, l’opacità, i costi ambientali e le violazioni della privacy non sono solo preoccupazioni etiche; sono bug che causano danni reali a persone reali. Il panorama della governance si sta evolvendo rapidamente e la legge dell’UE sull’intelligenza artificiale stabilisce lo standard globale. Ma la regolamentazione da sola non basta. Ogni sviluppatore di intelligenza artificiale deve pensare all'equità, alla spiegabilità e alla responsabilità come parte del proprio lavoro quotidiano. La domanda non è se l’intelligenza artificiale debba essere governata, ma come costruire sistemi degni di fiducia.