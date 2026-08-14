---
# Metadata
title: "Federated Learning and Privacy"
description: "Decentralised training, differential privacy, secure aggregation"
category: "AI and Machine Learning"
subcategory: "Model Architectures"
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
    changes: "Moved to architectures/ subfolder; added subcategory field"
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
tags: [federated, learning, privacy, ai-and-machine-learning]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "9 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# Apprendimento federato e privacy
L'apprendimento federato è una tecnica per addestrare modelli di machine learning su più dispositivi o organizzazioni senza condividere i dati grezzi. Invece di inviare dati a un server centrale, ciascun dispositivo addestra un modello locale e condivide solo gli aggiornamenti del modello (gradienti o pesi). Il server centrale aggrega questi aggiornamenti per produrre un modello globale. È stato progettato da Google per addestrare i modelli linguistici della tastiera sui telefoni Android e da allora è diventata una tecnica chiave per l’intelligenza artificiale che preserva la privacy.
---

## Perché l'apprendimento federato?
| Motivazione | Descrizione | Esempio |
|------------|-----|---------|
| **Tutela dei dati** | I dati grezzi non lasciano mai il dispositivo | Le cartelle cliniche rimangono in ospedale; le foto restano sul telefono |
| **Conformità normativa** | GDPR, HIPAA e altre normative limitano la condivisione dei dati | Le banche possono collaborare senza condividere i dati dei clienti |
| **Volume di dati** | Lo spostamento dei dati è costoso e lento | La formazione su miliardi di telefoni è poco pratica se è necessario caricare i dati |
| **Sensibilità dei dati** | Alcuni dati sono troppo sensibili per essere condivisi, anche con il consenso | Intelligence governativa; dati sanitari personali |
---

## Come funziona l'apprendimento federato
### Il protocollo di base (FedAvg)
| Passo | Cosa succede |
|------|-------------|
| **1. Inizializza** | Il server centrale crea un modello globale con pesi casuali |
| **2. Distribuisci** | Il server invia il modello globale corrente ai dispositivi selezionati |
| **3. Formazione locale** | Ciascun dispositivo addestra il modello sui propri dati locali per diverse epoche |
| **4. Carica** | I dispositivi inviano i pesi del modello aggiornato (non i dati) al server |
| **5. Aggregato** | Il server calcola la media dei pesi (Federated Averaging) per creare un nuovo modello globale |
| **6. Ripeti** | Torna al passaggio 2 finché il modello non converge |
```
Server: global_model = average(local_model_1, local_model_2, ..., local_model_n)
```

### Proprietà chiave
| Immobile | Descrizione |
|----------|-------------|
| **Dati non IID** | Ogni dispositivo ha distribuzioni di dati diverse (non indipendenti e distribuite in modo identico) |
| **Dati sbilanciati** | Alcuni dispositivi hanno molti dati, altri ne hanno pochissimi |
| **Partecipazione parziale** | Non tutti i dispositivi sono disponibili in ogni round |
| **Efficienza della comunicazione** | Il collo di bottiglia è la comunicazione, non il calcolo |
---

## Varianti di apprendimento federato
| Variante | Descrizione | Vantaggio |
|---------|-------------|-----------|
| **FedAvg** | Pesi medi dei modelli su tutti i dispositivi | Semplice; funziona bene per i dati IID |
| **FedProx** | Aggiunge un termine prossimale alla formazione locale | Meglio per dati non IID |
| **Ponteggio** | Utilizza le variabili di controllo per correggere l'eterogeneità dei dati | Convergenza più rapida su dati non IID |
| **FedSGD** | Come FedAvg ma con un passaggio di gradiente per round | Costo di comunicazione inferiore per round |
| **FL personalizzato** | Ogni dispositivo mantiene un modello personalizzato accanto a quello globale | Migliori prestazioni per dispositivo |
| **FL verticale** | Caratteristiche diverse (non campioni diversi) tra i partiti | Quando le parti detengono aspetti diversi degli stessi dati |
---

## Privacy differenziale
La privacy differenziale (DP) fornisce una garanzia matematica che l'output di un algoritmo non rivela se sono stati inclusi i dati di un individuo.
### Definizione fondamentale
Un meccanismo M soddisfa la privacy differenziale (ε, δ) se per due insiemi di dati D e D' che differiscono in un record:
```
P(M(D) ∈ S) ≤ e^ε × P(M(D') ∈ S) + Î´
```

| Parametro | Significato |
|-----------|---------|
| **ε (epsilon)** | Bilancio della privacy. Più piccolo = più privato. Valori tipici: 0,1–10. |
| **δ (delta)** | Probabilità di fallimento della garanzia della privacy. Solitamente impostato su 1/N (inverso della dimensione del set di dati). |
### Meccanismi per aggiungere privacy
| Meccanismo | Come funziona | Caso d'uso |
|-----------|-------------|----------|
| **Meccanismo gaussiano** | Aggiungi rumore gaussiano calibrato sulla sensibilità della query | Valori continui (pesi del modello) |
| **Meccanismo di Laplace** | Aggiungi il rumore di Laplace | Conteggio delle query |
| **Meccanismo esponenziale** | Selezionare gli output con probabilità proporzionale alla loro utilità | Scelte discrete |
### DP-SGD (discesa del gradiente stocastico differenzialmente privato)
| Passo | Descrizione |
|------|-------------|
| 1. Calcolare i gradienti per campione | Invece di gradienti batch |
| 2. Clip gradienti | Limitata la norma massima di ciascun gradiente (limita l'influenza di ogni singolo campione) |
| 3. Aggiungi rumore | Aggiungi rumore gaussiano calibrato al gradiente aggregato |
| 4. Aggiorna parametri | Gradino di discesa pendenza standard |
| Scambio | Descrizione |
|-----------|-------------|
| **Privacy vs accuratezza** | Una privacy più forte (ε inferiore) richiede più rumore, il che riduce la precisione del modello |
| **Privacy vs tempo di formazione** | Più rumore significa convergenza più lenta |
| **Monitoraggio del budget per la privacy** | Ciascuna fase di formazione consuma parte del budget per la privacy; una volta speso non è più recuperabile |
---

## Combinazione dell'apprendimento federato con la privacy differenziale
| Strato | Protezione |
|-------|-----------|
| **Apprendimento federato** | I dati grezzi rimangono sui dispositivi |
| **Privacy differenziale** | Anche gli aggiornamenti del modello sono rumorosi, proteggendo i contributi individuali |
| **Aggregazione sicura** | Il server vede solo l'insieme di tutti gli aggiornamenti, non quelli individuali |
Questa combinazione fornisce forti garanzie di privacy: anche se il server è compromesso, non può determinare se i dati di un individuo specifico sono stati utilizzati durante la formazione.
---

## Altre tecniche di tutela della privacy
### Calcolo multipartito sicuro (SMPC)
Più parti calcolano una funzione sui dati combinati senza rivelare i propri input individuali.
| Caratteristica | Descrizione |
|---------|-----|
| **Come funziona** | I dati vengono suddivisi in parti distribuite tra le parti; il calcolo avviene sulle azioni |
| **Garanzia** | Nessun partito apprende nulla dagli input degli altri |
| **In alto** | Costi di comunicazione e calcolo significativi |
| **Caso d'uso** | Le banche elaborano modelli di rischio congiunto senza condividere i dati dei clienti |
### Crittografia omomorfa (HE)
Esegui calcoli direttamente sui dati crittografati.
| Digitare | Cosa supporta | In testa |
|------|-----------|----------|
| **Parzialmente LUI** | Una operazione (addizione O moltiplicazione) | Basso |
| **Un po' LUI** | Numero limitato di entrambe le operazioni | Medio |
| **Completamente LUI** | Calcoli arbitrari | Molto alto (rallentamento 100-1000x) |
| Applicazione | Descrizione |
|-------------|-------------|
| **Inferenza privata** | Esegui modelli ML su dati crittografati; restituire previsioni crittografate |
| **Formazione crittografata** | Formazione sui dati crittografati (ancora per lo più teorico per il deep learning) |
| **Query private** | Interrogare un database senza rivelare la query o i dati |
### Ambienti di esecuzione attendibili (TEE)
Isolamento basato su hardware (Intel SGX, ARM Trustzone) che protegge i dati anche dal sistema operativo.
| Vantaggio | Limitazione |
|-----------|------------|
| Prestazioni quasi native | Richiede hardware specifico |
| Forti garanzie di sicurezza | Memoria limitata (dimensione dell'enclave) |
| Nessun sovraccarico crittografico | Possibili attacchi dal canale laterale |
---

##Normativa Privacy e ML
| Regolamento | Regione | Impatto sul machine learning |
|------------|--------|-----|
| **GDPR** | UE | Diritto alla spiegazione; minimizzazione dei dati; consenso al trattamento; diritto alla cancellazione |
| **CCPA** | California | Diritto di conoscere, cancellare e opporsi alla vendita dei dati |
| **HIPAAA** | USA (sanità) | Controlli severi sui dati sanitari; requisiti di anonimizzazione |
| **PIPL** | Cina | Localizzazione dei dati; requisiti di consenso; norme sui trasferimenti transfrontalieri |
| **Legge sull'intelligenza artificiale** | UE | Requisiti di trasparenza; classificazione del rischio; pratiche vietate |
### Impatto sui flussi di lavoro ML
| Principio GDPR | Implicazione ML |
|----------------|---------------|
| **Minimizzazione dei dati** | Raccogli solo ciò che ti serve; l'apprendimento federato aiuta |
| **Limitazione dello scopo** | Impossibile riutilizzare i dati senza un nuovo consenso |
| **Diritto alla cancellazione** | Deve essere in grado di rimuovere i dati di una persona da un modello addestrato (machine unlearning) |
| **Diritto alla spiegazione** | I modelli devono essere sufficientemente interpretabili per spiegare le previsioni individuali |
| **Privacy fin dalla progettazione** | La privacy deve essere integrata nei sistemi fin dall'inizio |
---

## Sfide
| Sfida | Descrizione |
|-----------|-------------|
| **Costo di comunicazione** | L'invio degli aggiornamenti dei modelli su milioni di dispositivi è costoso |
| **Dati non IID** | I dispositivi hanno distribuzioni di dati molto diverse, compromettendo la convergenza |
| **Rtardatari** | I dispositivi lenti ritardano l'intero round |
| **Compromesso tra privacy e utilità** | Una privacy più forte significa prestazioni peggiori del modello |
| **Attacchi di avvelenamento** | I partecipanti dannosi possono corrompere il modello globale |
| **Estrazione del modello** | Anche gli aggiornamenti dei modelli condivisi possono far trapelare informazioni sui dati di addestramento |
| **Eterogeneità hardware** | Dispositivi diversi hanno capacità di calcolo diverse |
---

## Strumenti e framework
| Strumento | Scopo |
|------|---------|
| **Fiore** | Framework di apprendimento federato open source; indipendente dal framework |
| **TensorFlow Federato** | Framework FL di Google per i modelli TensorFlow |
| **PySyft** (OpenMined) | ML che preserva la privacy in PyTorch |
| **DESTINO** (Webank) | Piattaforma di apprendimento federata di livello industriale |
| **FOGLIA** | Suite di benchmark per la ricerca sull'apprendimento federato |
| **Opacus** (Meta) | Privacy differenziale per PyTorch |
| **Privacy TF di Google** | Privacy differenziale per TensorFlow |
---

## Riepilogo
Le tecniche di apprendimento federato e di tutela della privacy affrontano una tensione fondamentale: come si costruiscono potenti modelli di intelligenza artificiale quando i dati sono distribuiti, sensibili o regolamentati? L'apprendimento federato conserva i dati sui dispositivi e condivide solo gli aggiornamenti dei modelli. La privacy differenziale aggiunge garanzie matematiche che i contributi individuali non possono essere rilevati. Il calcolo sicuro e la crittografia omomorfica vanno oltre, consentendo il calcolo su dati crittografati. Ciascuna tecnica ha dei costi – sovraccarico di comunicazione, precisione ridotta, spese di calcolo – ma insieme formano un kit di strumenti per costruire un’intelligenza artificiale che rispetti la privacy pur imparando dai dati del mondo.