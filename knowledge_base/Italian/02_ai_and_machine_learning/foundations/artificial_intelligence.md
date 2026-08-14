---
# Metadata
title: "Artificial Intelligence"
description: "AI overview, ML, deep learning, LLMs, ethics"
category: "AI and Machine Learning"
subcategory: "Foundations"
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
    changes: "Moved to foundations/ subfolder; added subcategory field"
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
tags: [artificial, intelligence, ai-and-machine-learning]
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
# Intelligenza artificiale
L’intelligenza artificiale è il tentativo di costruire macchine in grado di fare cose che richiederebbero intelligenza se fossero fatte da un essere umano: riconoscere volti, comprendere il parlato, prendere decisioni, scrivere testi, giocare, guidare automobili, diagnosticare malattie. Il campo è antico quanto l'informatica stessa: Alan Turing si chiedeva "Le macchine possono pensare?" nel 1950, ma la recente esplosione di capacità (anni 2020) ha reso l’intelligenza artificiale una delle tecnologie più importanti e contestate nella storia umana.
---

## Una breve storia
L’intelligenza artificiale ha attraversato cicli di clamore e delusione per decenni. Comprendere questa storia ti aiuta a capire perché le persone sono sia entusiaste che scettiche.
| Epoca | Cosa è successo | Risultato |
|-----|---------------|---------|
| **Anni '50-'60** | Ottimismo iniziale. Proposta del test di Turing (1950). La conferenza di Dartmouth conia "Intelligenza artificiale" (1956). I primi programmi come ELIZA (chatbot) e SHRDLU (comprensione del linguaggio). | Entusiasmo: "Avremo l'AGI tra una generazione!" |
| **Anni '70** | Primo inverno AI. I limiti dei primi approcci diventano chiari. I fondi si esauriscono. | Delusione: promesse non mantenute |
| **anni '80** | Boom dei sistemi esperti: programmi basati su regole che codificano la conoscenza specialistica umana. Il progetto di quinta generazione del Giappone. | Ancora entusiasmo: investimenti aziendali in AI |
| **1987-1993** | Secondo inverno AI. I sistemi esperti si rivelano fragili e costosi da mantenere. | Ancora una volta delusione |
| **anni 2000** | L’apprendimento automatico guadagna terreno. Ulteriori dati disponibili (internet). I metodi statistici sostituiscono le regole codificate manualmente. | Progressi costanti |
| **2012+** | Rivoluzione dell’apprendimento profondo. AlexNet vince la competizione ImageNet utilizzando le GPU. Le reti neurali iniziano a sovraperformare i metodi tradizionali su visione, parola e linguaggio. | Trasformazione rapida |
| **2017** | Il documento "L'attenzione è tutto ciò di cui hai bisogno" introduce l'architettura Transformer. | Fondazione per tutto ciò che segue |
| **2020-2026** | Modelli linguistici di grandi dimensioni (GPT-3, GPT-4, Claude, Gemini, LLaMA). L'intelligenza artificiale genera testo, codice, immagini, video. L’adozione aziendale accelera. | L'intelligenza artificiale diventa parte della vita quotidiana |
---

## Come funziona l'intelligenza artificiale moderna
### Apprendimento automatico: imparare dai dati
Invece di programmare regole esplicite, l’apprendimento automatico fornisce dati ad algoritmi che trovano modelli da soli.
| Digitare | Come funziona | Esempio |
|------|-------------|---------|
| **Apprendimento supervisionato** | Addestrarsi su esempi etichettati (input → output corretto) | Rilevamento dello spam: inviagli migliaia di email etichettate come "spam" o "non spam" |
| **Apprendimento non supervisionato** | Trova modelli nei dati senza etichetta | Segmentazione della clientela: raggruppare clienti simili senza predefinire i gruppi |
| **Apprendimento per rinforzo** | L'agente impara per tentativi ed errori, ricevendo premi o penalità | IA di gioco: prova le mosse, ottieni punti per vincere, scopri quali strategie funzionano |
### Apprendimento profondo: reti neurali
L’apprendimento profondo utilizza reti neurali artificiali: strati di semplici operazioni matematiche che, impilati insieme, possono apprendere modelli incredibilmente complessi. Il "profondo" si riferisce al numero di strati.
Architetture chiave:
| Architettura | Il migliore in | Utilizzo nel mondo reale |
|-------------|---------|----------------|
| **CNN** (Rete Neurale Convoluzionale) | Immagine e dati spaziali | Riconoscimento facciale, imaging medico, auto a guida autonoma |
| **RNN/LSTM** | Dati sequenziali (serie temporali) | Riconoscimento vocale, generazione di musica (in gran parte sostituito da Transformers) |
| **Trasformatore** | Tutto: testo, immagini, audio, codice | GPT, Claude, Gemini, BERT, DALL-E — l'architettura dominante |
| **GAN** (Rete generativa avversaria) | Generazione di dati realistici | Sintesi dell'immagine, trasferimento di stile (parzialmente sostituito da modelli diffusivi) |
| **Modelli di diffusione** | Generazione di immagini/video di alta qualità | Diffusione stabile, DALL-E 3, Midjourney, Sora |
### Modelli linguistici di grandi dimensioni (LLM)
Gli LLM sono modelli basati su Transformer addestrati su enormi quantità di testo. Imparano a prevedere il prossimo token (parola) in una sequenza, che risulta richiedere la comprensione della grammatica, dei fatti, del ragionamento e persino di qualcosa che assomiglia alla "conoscenza".
| Modello | Sviluppatore | Caratteristica notevole |
|-------|-----------|-----------------|
| **GPT-4 / GPT-4o** | OpenAI | Multimodale (testo + immagini); ragionamento forte |
| **Claude** | Antropico | Concentrarsi sulla sicurezza e sulla disponibilità; finestre con contesto lungo |
| **Gemelli** | Google DeepMind | Nativamente multimodale; integrato con i servizi Google |
| **LLaMA / Lama 3** | Meta | Peso aperto; può essere eseguito localmente; grande comunità |
| **Maestrale** | Maestrale AI | Modelli aperti efficienti e competitivi con quelli molto più grandi |
**Processo di formazione**:
1. **Pre-formazione**: impara da enormi dati di testo (previsione dei token successivi). È qui che il modello acquisisce "conoscenza".
2. **Perfezionamento**: formazione su compiti specifici o con preferenze umane.
3. **RLHF** (Apprendimento per rinforzo dal feedback umano): gli esseri umani valutano i risultati del modello; il modello impara a produrre gli output preferiti dagli esseri umani.
Le **finestre di contesto** (quantità di testo che il modello può elaborare contemporaneamente) sono cresciute da token 4K (inizio GPT-3) a oltre 1 milione di token nei modelli 2026.
---

## Cosa può e non può fare l'intelligenza artificiale
### Capacità attuali
| Compito | Prestazioni | Limitazioni |
|------|-------------|-----|
| **Generazione di testo** | Eccellente — coerente, contestuale, stilisticamente vario | Può avere allucinazioni (generare false informazioni con sicurezza) |
| **Generazione del codice** | Ottimo per modelli comuni; può scrivere interi programmi | Lotta con nuove architetture; può introdurre bug sottili |
| **Generazione di immagini** | Fotorealistico; stili artistici; modifica | Lancette e testo ancora imperfetti; lotta con un ragionamento spaziale preciso |
| **Traduzione** | Quasi umano per le principali coppie linguistiche | Linguaggi con poche risorse meno accurati; la sfumatura culturale può andare perduta |
| **Riconoscimento vocale** | Quasi umano in un audio pulito | Lotta con accenti pesanti, rumore di fondo |
| **Ragionamento** | Migliorare rapidamente; può risolvere molti problemi logici | Fallisce su problemi nuovi che richiedono una comprensione genuina |
| **Matematica** | Bravo nei problemi standard | Commette errori su nuove dimostrazioni; non sostituisce la verifica formale |
| **Pianificazione e utilizzo degli strumenti** | Emergenti (agenti) | Ancora inaffidabile per compiti complessi in più fasi senza supervisione umana |
### Cosa non può fare l'intelligenza artificiale (dal 2026)
- **Comprendi veramente** qualsiasi cosa nel modo in cui lo fanno gli esseri umani: elabora modelli, non significati
- **Garantire l'accuratezza fattuale**: l'allucinazione rimane un problema irrisolto
- **Sostituisci il giudizio umano** nelle decisioni ad alto rischio senza supervisione
- **Generalizza perfettamente** a domini molto diversi dai dati di addestramento
- **Operare in modo autonomo** in ambienti fisici imprevedibili (la robotica è ancora difficile)
---

## Etica e sicurezza dell'IA
L’intelligenza artificiale non è neutrale. Riflette i dati su cui è stato formato, le scelte dei suoi sviluppatori e gli incentivi delle organizzazioni che lo implementano.
### Preoccupazioni chiave
| Problema | Cosa succede | Esempio |
|-------|-------------|---------|
| **Bias** | I sistemi di intelligenza artificiale riproducono e amplificano i pregiudizi nei dati di addestramento | Algoritmi di assunzione che favoriscono i candidati uomini; riconoscimento facciale con tassi di errore più elevati per la pelle più scura |
| **Privacy** | AI addestrata sui dati personali; capacità di sorveglianza | Formazione sulle opere protette da copyright; riconoscimento facciale negli spazi pubblici |
| **Uso improprio** | Deepfakes, disinformazione, phishing automatizzato | Video falsi di politici generati dall'intelligenza artificiale; chiamate truffe automatizzate |
| **Spostamento di posti di lavoro** | Automazione di compiti precedentemente svolti dagli esseri umani | Creazione di contenuti, servizio clienti, immissione dati, parte di programmazione |
| **Allineamento** | Garantire che gli obiettivi dell’IA corrispondano ai valori umani | Un'intelligenza artificiale a cui viene chiesto di "massimizzare la produzione di graffette" potrebbe convertire tutta la materia in graffette |
| **Rischio esistenziale** | Preoccupazioni teoriche sulla futura AGI | Dibattito tra i ricercatori: alcuni lo ritengono urgente, altri prematuro |
### Chi si occupa di sicurezza
- **Anthropic**: fondata da ex ricercatori di OpenAI focalizzati specificatamente sulla sicurezza dell'IA
- **DeepMind Safety**: team di ricerca all'interno di Google DeepMind
- **MIRI** (Machine Intelligence Research Institute): ricerca teorica sulla sicurezza
- **ARC** (Centro ricerche AI): ricerca empirica sulla sicurezza
- **Organi governativi** — Legge sull'AI dell'UE (2026), ordini esecutivi statunitensi, quadri internazionali
---

## L'intelligenza artificiale nella pratica: settore per settore
| Industria | Applicazione | Maturità |
|----------|-------------|----------|
| **Assistenza Sanitaria** | Diagnosi del cancro dalle immagini; scoperta di farmaci (AlphaFold); prevedere gli esiti dei pazienti | Distribuito ed espansione |
| **Finanza** | Rilevamento delle frodi, trading algoritmico, credit scoring, robo-advisor | Ampiamente distribuito |
| **Trasporti** | Veicoli a guida autonoma (Waymo, Tesla Autopilot); ottimizzazione del percorso | Parzialmente distribuito; piena autonomia ancora limitata |
| **Istruzione** | Apprendimento personalizzato; Tutoraggio sull'intelligenza artificiale; classificazione automatizzata | In rapida crescita |
| **Campi creativi** | Generazione di immagini (Midjourney, DALL-E); musica; assistenza alla scrittura; completamento del codice | Trasformare i flussi di lavoro ora |
| **Sicurezza informatica** | Rilevamento delle minacce; identificazione delle anomalie; sia attacchi che difese | Corsa agli armamenti in corso |
| **Legale** | Analisi contrattuale; revisione dei documenti; ricerca giuridica | Essere adottato; preoccupazioni di precisione |
| **Agricoltura** | Monitoraggio delle colture tramite satellite/drone; spruzzatura di precisione; previsione della resa | Crescere |
| **Produzione** | Ispezione di qualità; manutenzione predittiva; ottimizzazione della catena di fornitura | Ampiamente distribuito |
---

## Robotica e intelligenza artificiale incarnata
La robotica combina l’intelligenza artificiale con le macchine fisiche. Nonostante decenni di progressi, l’interazione fisica con il mondo rimane molto più difficile dell’intelligenza digitale.
- **Atlante di Boston Dynamics**: movimento bipede avanzato; parkour; compiti di magazzino
- **Robot industriali** (ABB, FANUC, KUKA) — automatizzano la produzione; saldatura; assemblaggio
- **Robot chirurgici** (sistema da Vinci): chirurgia minimamente invasiva con una precisione che va oltre le mani umane
- **Robot domestici** (Roomba): semplici ma di successo commerciale
- **Robot umanoidi** (Tesla Optimus, Figura AI) — emergenti; i compiti fisici generici sono ancora molto difficili
Il divario tra l’intelligenza artificiale digitale (che ha fatto enormi progressi) e l’intelligenza artificiale fisica (che lotta con destrezza, equilibrio e ambienti imprevedibili) è una delle grandi sfide del settore.
---

## Tendenze attuali (anni 2020)
| Tendenza | Cosa sta succedendo |
|-------|-----|
| **AI multimodale** | Sistemi che elaborano insieme testo, immagini, audio e video (GPT-4V, Gemini) |
| **Agenti** | LLM in grado di utilizzare strumenti, navigare sul Web, scrivere codice ed eseguire azioni in più passaggi |
| **Modelli a peso aperto** | LLaMA di Meta e altri democratizzano l'accesso ai modelli di grandi dimensioni |
| **AI sul dispositivo** | Esecuzione di modelli localmente su telefoni e laptop (Apple Intelligence, Qualcomm NPU) |
| **Regolamento IA** | Legge dell’UE sull’IA (2026): prima legge globale sull’IA; sistemi di classificazione per livello di rischio |
| **L'intelligenza artificiale nella scienza** | Ripiegamento delle proteine ​​(AlphaFold), scoperta dei materiali, modellazione climatica, prove matematiche |
| **Piccoli modelli linguistici** | Modelli efficienti che funzionano su hardware consumer; qualità che si avvicina ai modelli più grandi |
---

## Riepilogo
L’intelligenza artificiale rappresenta finora lo sviluppo tecnologico più significativo del 21° secolo. Non si tratta di magia: si tratta di una corrispondenza di modelli su larga scala, resa possibile da enormi quantità di dati, hardware potente e architetture intelligenti. Ciò che lo rende trasformativo è che la corrispondenza dei modelli, eseguita sufficientemente bene, può replicare molti compiti che in precedenza richiedevano l’intelligenza umana. Le sfide sono ugualmente significative: allucinazioni, pregiudizi, spostamento di posti di lavoro, abusi e la questione aperta se il percorso dall’intelligenza artificiale ristretta all’intelligenza generale sia breve o incredibilmente lungo. Ciò che è chiaro è che l’intelligenza artificiale rimodellerà ogni settore, ogni professione e ogni aspetto della vita quotidiana. Capire come funziona – e cosa non può fare – è essenziale per navigare nel mondo che stiamo costruendo.