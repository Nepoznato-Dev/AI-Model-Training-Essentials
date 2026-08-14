---
# Metadata
title: "NLP Fundamentals"
description: "Text processing, embeddings, Transformers, BERT, GPT"
category: "AI and Machine Learning"
subcategory: "NLP and Speech"
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
    changes: "Moved to nlp_and_speech/ subfolder; added subcategory field"
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
tags: [nlp, ai-and-machine-learning]
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
# Fondamenti della PNL
L'elaborazione del linguaggio naturale (NLP) è il campo in cui si insegna alle macchine a comprendere, generare e lavorare con il linguaggio umano. Alimenta motori di ricerca, chatbot, sistemi di traduzione, analisi del sentiment e i modelli linguistici di grandi dimensioni (LLM) che hanno trasformato l'intelligenza artificiale dal 2020. Questo file copre l'evoluzione dalle tecniche classiche alle moderne architetture basate su Transformer.
---

## Preelaborazione del testo
Il testo grezzo è disordinato. Prima che un modello possa utilizzarlo, deve essere pulito e strutturato.
| Passo | Cosa fa | Esempio |
|------|-------------|---------|
| **Tokenizzazione** | Suddividi il testo in token (parole, sottoparole o caratteri) | "Adoro la PNL" →`["I", "love", "NLP"]`|
| **In minuscolo** | Converti in minuscolo | "Ciao" → "ciao" |
| **Interrompi la rimozione delle parole** | Rimuovi le parole comuni (il, è, a) | "il gatto si sedette" → "il gatto si sedette" |
| **Determinazione** | Taglia le terminazioni delle parole (grezzo) | "correre" → "correre" |
| **Lemmatizzazione** | Ridurre alla forma del dizionario (consapevole del contesto) | "migliore" → "buono" |
| **Normalizzazione** | Correggi la codifica, rimuovi i caratteri speciali, espandi le contrazioni | "non" → "non" |
I moderni modelli Transformer spesso saltano la rimozione e la radice delle stop word: apprendono questi modelli dai dati.
---

## Rappresentazione del testo
Le macchine hanno bisogno di numeri, non di parole. Il modo in cui rappresentiamo il testo come vettori è fondamentale.
### Approcci classici
| Metodo | Descrizione | Limitazione |
|--------|-------------|-----------|
| **Codifica One-Hot** | Ogni parola occupa una posizione unica in un enorme vettore | Raro; nessun significato semantico |
| **Sacco di parole (arco)** | Contare le frequenze delle parole; ignora l'ordine | Perde completamente l'ordine delle parole |
| **TF-IDF** | Peso delle parole in base alla frequenza nel documento × alla rarità nel corpus | Ignora ancora ordine e contesto |
### Incorporamenti di parole
Gli incorporamenti mappano le parole su vettori densi in cui parole simili sono vicine tra loro.
| Modello | Idea chiave |
|-------|----------|
| **Word2Vec** (2013) | Prevedere la parola dal contesto (CBOW) o il contesto dalla parola (Skip-gram) |
| **Guanto** (2014) | Statistiche globali sulla co-occorrenza → vettori densi |
| **Testo veloce** (2016) | Word2Vec + informazioni sulle sottoparole (gestisce meglio le parole rare) |
Il famoso esempio:`king - man + woman ≈ queen`. Gli incorporamenti catturano le relazioni semantiche.
**Limitazione**: gli incorporamenti classici assegnano un vettore per parola, quindi non possono gestire la polisemia (parole con significati multipli). "Banca" in "riva del fiume" e "conto bancario" ottengono lo stesso vettore.
---

## Modelli di sequenza
Prima di Transformers, l’approccio standard per la PNL consisteva nell’elaborare il testo in sequenza.
| Architettura | Come funziona | Forza | Debolezza |
|-------------|-------------|----------|----------|
| **RNN** | Elabora i token uno alla volta; mantenere lo stato nascosto | Gestisce input di lunghezza variabile | Gradienti evanescenti; non è possibile acquisire dipendenze lunghe |
| **LSTM** | RNN con porte (forget, input, output) per controllare il flusso di informazioni | Meglio nelle dipendenze a lungo raggio | Ancora sequenziale; lento ad allenarsi |
| **GRU** | LSTM semplificato (meno gate) | Più veloce di LSTM; prestazioni simili | Stesse limitazioni fondamentali |
Questi modelli elaborano il testo da sinistra a destra, il che significa che sono lenti da addestrare (non possono parallelizzare) e lottano con dipendenze a lungo raggio.
---

## Il meccanismo dell'attenzione
L'attenzione consente a un modello di esaminare simultaneamente tutte le posizioni in una sequenza e di decidere quali sono più rilevanti per la previsione corrente.
### Approfondimento chiave
Invece di comprimere un’intera frase in un singolo stato nascosto (come fanno gli RNN), l’attenzione calcola una somma ponderata di tutti gli stati nascosti, dove i pesi vengono appresi.
```
Attention(Q, K, V) = softmax(QK^T / √d_k) V
```

| Componente | Ruolo |
|-----------|------|
| **Interrogazione (Q)** | Cosa sto cercando? |
| **Tasto (K)** | Cosa contengo? |
| **Valore (V)** | Quali informazioni fornisco? |
| **√d_k** | Fattore di scala per evitare prodotti con punti grandi |
---

## L'architettura del trasformatore
The Transformer (Vaswani et al., 2017 — "L'attenzione è tutto ciò di cui hai bisogno") ha sostituito interamente la ricorrenza con l'attenzione. È il fondamento di praticamente tutta la PNL moderna.
### Architettura
| Componente | Descrizione |
|-----------|-------------|
| **Codificatore** | Legge il testo immesso; produce rappresentazioni contestuali |
| **Decodificatore** | Genera testo di output; si occupa dell'uscita dell'encoder |
| **Attenzione a se stessi** | Ogni token si occupa di tutti gli altri token nella stessa sequenza |
| **Attenzione multi-testa** | Esegui più teste di attenzione in parallelo; catturare relazioni diverse |
| **Codifica posizionale** | Iniettare informazioni sulla posizione (poiché non c'è ricorrenza) |
| **Rete feed-forward** | Applicato a ciascuna posizione in modo indipendente |
| **Normalizzazione dei livelli** | Stabilizzare la formazione |
| **Connessioni residue** | Salta connessioni per flusso gradiente |
### Solo codificatore, Solo decodificatore, Codificatore-decodificatore
| Variante | Architettura | Ideale per | Esempi |
|---------|-----|----------|---------|
| **Solo encoder** | Comprende il testo | Classificazione, NER, analisi del sentiment | BERT, Roberta, DeBERTa |
| **Solo decodificatore** | Genera testo | Modelli linguistici, chatbot, generazione di codice | GPT-3/4, LLaMA, Claude |
| **Codificatore-Decodificatore** | Trasforma il testo | Traduzione, sintesi | T5, BART, mBART |
---

## Principali famiglie modello
### Famiglia BERT (solo encoder)
| Modello | Caratteristica fondamentale |
|-------|-------------|
| **BERT** (2018) | Modello di linguaggio mascherato + Previsione della frase successiva |
| **RoBERTa** | NSP rimosso; addestrato più a lungo con più dati |
| **ALBERTO** | Condivisione dei parametri; ingombro ridotto |
| **DeBERTa** | Attenzione districata; NLU migliorata |
| **DistilBERT** | 40% più piccolo, 60% più veloce, mantiene il 97% delle prestazioni di BERT |
### Famiglia GPT (solo decoder)
| Modello | Parametri | Note |
|-------|-----------|-------|
| **GPT-2** | 1,5B| I modelli mostrati solo con decoder possono generare testo coerente |
| **GPT-3** | 175B| Apprendimento con pochi colpi; richiesto anziché ottimizzato |
| **GPT-3.5 / GPT-4** | Non divulgato | Sintonizzato sulle istruzioni + RLHF; colloquiale |
| **LLaMA** (Meta) | 7B–70B | Peso aperto; ha generato l'ecosistema LLM open source |
| **Mistral / Mixtral** | 7B / 8×7B (MoE) | Modelli aperti efficienti con prestazioni elevate |
---

## Compiti fondamentali della PNL
| Compito | Descrizione | Modello tipico |
|------|-------------|------|
| **Classificazione del testo** | Assegna un'etichetta al testo (spam/non spam, positivo/negativo) | BERT, classificatori ottimizzati |
| **Riconoscimento dell'entità denominata (NER)** | Identificare persone, organizzazioni, posizioni nel testo | BERT + strato CRF |
| **Analisi del sentiment** | Determinare il tono emotivo | BERT ottimizzato o LLM zero-shot |
| **Traduzione automatica** | Tradurre tra le lingue | T5, mBART, MarianMT |
| **Risposte alle domande** | Rispondi alle domande in base al contesto | BERT (estrattivo), GPT (generativo) |
| **Riepilogo** | Condensa testo lungo | T5, BART, GPT |
| **Generazione di testo** | Produrre testo coerente | GPT-4, LLaMA, Claude |
---

## Ottimizzazione e richiesta di suggerimenti
| Avvicinamento | Come funziona | Quando usarlo |
|----------|-------------|-------------|
| **Regolazione** | Aggiorna i pesi del modello sui dati specifici dell'attività | Hai etichettato i dati; necessitano delle massime prestazioni |
| **Suggerimento** | Fornire istruzioni al modello in linguaggio naturale | Prototipazione rapida; dati limitati; utilizzando LLM |
| **Pochi colpi** | Includere esempi nel prompt | Quando hai pochi esempi ma non abbastanza per mettere a punto |
| **LoRA/QLoRA** | Messa a punto efficiente; aggiornare matrici piccole di rango basso | Ottimizza i modelli di grandi dimensioni con memoria GPU limitata |
---

## Strumenti e framework
| Strumento | Scopo |
|------|---------|
| **Trasformatori di volti abbracciati** | Modelli pre-addestrati, tokenizzatori, pipeline di fine tuning |
| **spazio** | Pipeline NLP di livello produttivo (tokenizzazione, NER, POS, dipendenza) |
| **NLTK** | Educativo; algoritmi PNL classici |
| **Gensim** | Modellazione degli argomenti (LDA), incorporamenti di parole (Word2Vec, Doc2Vec) |
| **LangChain / LlamaIndex** | Framework per la creazione di applicazioni basate su LLM |
| **vLLM** | Servizio LLM ad alto rendimento |
| **Tokenizzatori (HF)** | Tokenizzazione rapida (BPE, WordPiece, SentencePiece) |
---

## Il panorama del LLM
Il moderno panorama della PNL è dominato da grandi modelli linguistici:
| Categoria | Esempi | Note |
|----------|---------|-------|
| **Proprietario** | GPT-4, Claude, Gemelli | Miglior prestazione; Solo accesso API |
| **Peso aperto** | LLaMA 3, Mistral, Qwen | Pesi disponibili; eseguito localmente |
| **Open source** | Pizia, OPT | Completamente aperto (dati, pesi, codice) |
| **Multimodale** | GPT-4V, Gemelli, LLaVA | Elabora testo + immagini |
| **Specializzato in codici** | CodeLlama, StarCoder, DeepSeek Coder | Addestrato sul codice |
| **Piccolo / Efficiente** | Phi-3, Gemma, TinyLlama | Ottime prestazioni su piccola scala |
Il campo si sta muovendo velocemente. Ciò che è all'avanguardia oggi potrebbe essere sostituito tra pochi mesi. I fondamentali – attenzione, tokenizzazione, messa a punto, valutazione – rimangono stabili.