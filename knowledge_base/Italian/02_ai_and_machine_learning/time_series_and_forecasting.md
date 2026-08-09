---
# Metadata
title: "Time Series and Forecasting"
description: "ARIMA, Prophet, LSTMs, seasonality, anomaly detection"
category: "AI and Machine Learning"
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
reviewed_by: "AI & Machine Learning Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [time, series, forecasting, ai-and-machine-learning]
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
# Serie temporali e previsioni
I dati delle serie temporali sono tutti i dati raccolti nel tempo: prezzi delle azioni, letture della temperatura, traffico del sito web, dati sulle vendite, cardiofrequenzimetri, consumo energetico. Fare previsione significa prevedere valori futuri sulla base di modelli passati. È una delle applicazioni più preziose dal punto di vista pratico della scienza dei dati e una delle più difficili, perché il futuro è veramente incerto e le serie temporali del mondo reale sono piene di rumore, stagionalità e interruzioni strutturali.
---

## Caratteristiche delle serie storiche
| Componente | Descrizione | Esempio |
|-----------|-------------|---------|
| **Tendenza** | Aumento o diminuzione a lungo termine | Temperature globali in aumento nel corso di decenni |
| **Stagionalità** | Schemi regolari e prevedibili a intervalli fissi | Le vendite al dettaglio aumentano ogni dicembre |
| **Ciclicità** | Fluttuazioni a intervalli non fissi (spesso economici) | Recessioni ogni 5-10 anni |
| **Rumore (residuo)** | Variazione casuale che non può essere spiegata | Movimenti giornalieri dei prezzi delle azioni |
| **Autocorrelazione** | I valori attuali dipendono dai valori passati | La temperatura di oggi è simile a quella di ieri |
### Stazionarietà
Una serie temporale è **stazionaria** se le sue proprietà statistiche (media, varianza) non cambiano nel tempo. La maggior parte dei metodi di previsione presuppone la stazionarietà.
| Prova | Scopo |
|------|---------|
| **Dickey-Fuller aumentato (ADF)** | Verifica se è presente una radice unitaria (non stazionaria) |
| **Test KPSS** | Verifica se la serie ha un trend stazionario |
| Trasformazione | Quando usarlo |
|---------------|-------------|
| **Differenza** | Rimuovi tendenza: y'(t) = y(t) - y(t-1) |
| **Trasformazione del registro** | Stabilizzare la varianza (per una crescita esponenziale) |
| **Differenza stagionale** | Rimuovi la stagionalità: y'(t) = y(t) - y(t-s) dove s è la durata della stagione |
---

## Metodi di previsione classici
### Medie mobili
| Metodo | Descrizione | Ideale per |
|--------|-------------|----------|
| **Media mobile semplice (SMA)** | Media delle ultime N osservazioni | Smussamento dei dati rumorosi |
| **Media mobile ponderata** | Le osservazioni più recenti assumono un peso maggiore | Quando i dati recenti contano di più |
| **Media mobile esponenziale (EMA)** | Pesi in diminuzione esponenziale | Monitorare le tendenze con meno ritardi |
### Smoothing esponenziale
| Metodo | Componenti | Caso d'uso |
|--------|-----------|----------|
| **Semplice (SES)** | Solo livello | Nessuna tendenza, nessuna stagionalità |
| **Holt (doppio)** | Livello + tendenza | Dati con trend ma senza stagionalità |
| **Holt-Winters (Triplo)** | Livello + trend + stagionalità | Dati con trend e stagionalità |
### ARIMA e varianti
ARIMA (AutoRegressive Integrated Moving Average) è il cavallo di battaglia delle previsioni di serie temporali classiche.
| Componente | Significato | Parametro |
|-----------|---------|-----------|
| **AR(p)** | Regressione sui valori p precedenti | Quanti valori passati utilizzare |
| **I(d)** | Numero di passaggi di differenziazione per rendere stazionario | Quante volte fare la differenza |
| **MA(q)** | Modellare l'errore come una combinazione di errori passati | Quanti errori passati utilizzare |
| Variante | Estensione | Caso d'uso |
|---------|-----------|----------|
| **SARIMA** | Aggiunge componenti stagionali (P, D, Q, s) | Dati con forte stagionalità |
| **ARIMAX** | Aggiunge variabili esterne | Quando sei a conoscenza dei prossimi eventi |
| **VAR** | ARIMA multivariata; serie multiple interdipendenti | Quando le variabili si influenzano a vicenda |
---

## Approcci moderni al machine learning
### Modelli basati su LSTM e RNN
| Modello | Architettura | Vantaggio |
|-------|-------------|-----------|
| **LSTM** | Rete di memoria a breve termine lungo | Cattura dipendenze temporali a lungo raggio |
| **GRU** | Unità ricorrente recintata (LSTM più semplice) | Formazione più rapida; prestazioni simili |
| **Seq2Seq** | Codificatore-decodificatore per serie temporali | Lunghezze di ingresso/uscita flessibili |
| **Rete convoluzionale temporale (TCN)** | Circonvoluzioni causali dilatate | Formazione parallela; campo recettivo lungo |
### Profeta (Meta)
Uno strumento pratico di previsione progettato per le serie temporali aziendali.
| Caratteristica | Descrizione |
|---------|-----|
| **Decomposizione** | Tendenza + stagionalità + festività |
| **Flessibile** | Gestisce dati mancanti, valori anomali e interruzioni strutturali |
| **Interpretabile** | I componenti sono leggibili |
| **Automatico** | Inadempienze ragionevoli; messa a punto minima richiesta |
| Forza | Limitazione |
|----------|------------|
| Ottimo per le metriche aziendali (vendite, utenti) | Non ideale per dati ad altissima frequenza |
| Gestisce festività ed eventi speciali | Presuppone stagionalità additiva o moltiplicativa |
| Robusto ai valori anomali | Meno accurato del deep learning per modelli complessi |
### Modelli basati su trasformatore
| Modello | Caratteristica fondamentale |
|-------|-------------|
| **Informatore** | Prob Scarsa attenzione per le sequenze lunghe |
| **Autoformatore** | Meccanismo di autocorrelazione per la scomposizione in serie |
| **PatchTST** | Corregge le serie temporali; indipendente dal canale |
| **TimesFM** (Google) | Modello di fondazione per le serie storiche; pre-addestrato su dati diversi |
| **Chronos** (Amazon) | Tokenizza le serie temporali; utilizza l'architettura in stile LLM |
---

## Rilevamento di anomalie nelle serie temporali
Rilevare modelli insoliti che si discostano dal comportamento previsto.
| Metodo | Avvicinamento | Caso d'uso |
|--------|----------|----------|
| **Statistica** | Punteggio Z, IQR, carte di controllo | Semplice, ben compreso |
| **Foresta di isolamento** | Basato su alberi; isola le anomalie mediante partizionamento casuale | Rilevamento anomalie multivariate |
| **LOF** (fattore anomalo locale) | Basato sulla densità; confronta la densità locale con i vicini | Quando le anomalie si trovano nelle regioni a bassa densità |
| **Codificatori automatici** | Errore di ricostruzione; errore alto = anomalia | Modelli complessi e non lineari |
| **Basato su LSTM** | Prevedere il passo successivo; grande errore di previsione = anomalia | Anomalie sequenziali |
### Applicazioni
| Dominio | Cosa significano le anomalie |
|--------|-----|
| **Finanza** | Frode, crolli del mercato, crolli flash |
| **Assistenza Sanitaria** | Frequenza cardiaca anormale, insorgenza di convulsioni |
| **Produzione** | Guasti alle apparecchiature, difetti di qualità |
| **Sicurezza informatica** | Tentativi di intrusione, attacchi DDoS |
| **Infrastrutture** | Sovraccarico del server, guasti di rete |
---

## Metriche di valutazione
| Metrico | Formula (concettuale) | Quando usarlo |
|--------|----------------------|-----|
| **MAE** (errore medio assoluto) | Media degli errori assoluti | Interpretabile; stesse unità dei dati |
| **RMSE** (errore quadratico medio) | Radice quadrata degli errori quadrati medi | Penalizza di più gli errori grandi |
| **MAPE** (Errore percentuale medio assoluto) | Media degli errori percentuali assoluti | Quando l'errore relativo conta |
| **SMAPE** (MAPE simmetrico) | Versione simmetrica di MAPE | Gestisce meglio i valori vicini allo zero |
| **MASE** (errore medio assoluto scalato) | MAE rispetto ad una previsione ingenua | Confronto tra diverse serie |
---

## Flusso di lavoro pratico
| Passo | Descrizione |
|------|-------------|
| **1. Esplora** | Traccia la serie; identificare trend, stagionalità, valori anomali |
| **2. Decomporre** | Separato in componenti trend, stagionali e residui |
| **3. Stazionariare** | Applica differenze o trasformazioni se necessario |
| **4. Diviso** | Suddivisione basata sul tempo (mai suddivisione casuale per le serie temporali) |
| **5. Riferimento** | Inizia con una previsione ingenua (ultimo valore, ingenua stagionale) |
| **6. Modello** | Prova i metodi classici (ARIMA, Prophet), quindi i metodi ML |
| **7. Valuta** | Utilizzare metriche appropriate; confrontare con il basale |
| **8. Itera** | Aggiungi funzionalità, prova diversi modelli, ottimizza gli iperparametri |
---

## Strumenti e librerie
| Strumento | Scopo |
|------|---------|
| **modelli statistici** | Serie storiche classiche (ARIMA, ETS, scomposizione) |
| **Profeta** (Meta) | Previsione delle serie temporali aziendali |
| **sktime** | Interfaccia ML unificata per serie temporali |
| **Freccette** | Libreria di previsione completa (classica + deep learning) |
| **GluonTS** (Amazon) | Modellazione probabilistica di serie temporali |
| **Profeta neurale** | Profeta con componenti di rete neurale |
| **tsfresh** | Estrazione automatica delle caratteristiche delle serie temporali |
| **panda** | Manipolazione e ricampionamento delle serie temporali |
---

## Riepilogo
La previsione delle serie temporali unisce la statistica classica al moderno machine learning. I metodi classici (ARIMA, livellamento esponenziale, Prophet) sono interpretabili, veloci e spesso sorprendentemente accurati. I metodi di deep learning (LSTM, Transformers) acquisiscono modelli complessi ma richiedono più dati e ottimizzazione. I principi chiave rimangono gli stessi indipendentemente dal metodo: comprendere la struttura dei dati (tendenza, stagionalità, rumore), confrontare sempre con una base di riferimento semplice, valutare con metriche appropriate e ricordare che il futuro non è mai una ripetizione perfetta del passato.