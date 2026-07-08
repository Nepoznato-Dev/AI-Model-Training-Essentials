# Valutazione e flusso di lavoro dell'apprendimento automatico

Una guida pratica al ciclo di vita del machine learning, dall'inquadramento dei problemi al monitoraggio della produzione, con particolare attenzione alle metriche, alla convalida e al debug.

---

## Il flusso di lavoro ML (CRISP-ML)

1. **Comprensione aziendale**: definire l'obiettivo e i criteri di successo.
2. **Comprensione dei dati**: esplorare i dati disponibili, identificare i problemi di qualità.
3. **Preparazione dei dati**: pulisci, trasforma e dividi i dati.
4. **Modellazione**: addestrare modelli, ottimizzare gli iperparametri.
5. **Valutazione**: valutare le prestazioni rispetto ai parametri.
6. **Deployment**: servire il modello in produzione.
7. **Monitoraggio**: traccia deriva, prestazioni e anomalie.

Si tratta di un ciclo iterativo: rivisiterai i passaggi precedenti in base ai risultati della valutazione.

---

## Suddivisione dei dati

### Formazione/Convalida/Test suddiviso
- **Set di training** (~70%): utilizzato per adattare i parametri del modello.
- **Set di convalida** (~15%): utilizzato per ottimizzare gli iperparametri e selezionare le varianti del modello.
- **Set di test** (~15%): utilizzato solo una volta alla fine per stimare le prestazioni di generalizzazione.

**Importante:** il set di test deve essere mantenuto completamente intatto fino alla valutazione finale per evitare perdite di dati.

### Convalida incrociata (k-fold)
Per set di dati di piccole dimensioni, utilizza la convalida incrociata k-fold: dividi i dati in k fold, esegui il training su k-1, convalida sui rimanenti e ripeti k volte. Media della prestazione. k=5 o k=10 è comune.

### Divisione stratificata
Per la classificazione con classi sbilanciate, utilizzare suddivisioni stratificate per preservare le proporzioni delle classi in ciascun sottoinsieme.

### Suddivisione basata sul tempo
Per i dati di serie temporali, suddivisi in ordine cronologico (allenamento sul passato, test sul futuro) anziché in modo casuale.

---

## Metriche di valutazione

### Metriche di classificazione

| Metrico | Cosa misura | Ideale per |
|--------|------------|---------------|
| **Precisione** | (TP + TN) / (TP + TN + FP + FN) | Set di dati bilanciati |
| **Precisione** | PT / (PT + FP) | Quando i falsi positivi sono costosi (ad esempio, rilevamento dello spam) |
| **Richiamo** | TP / (TP + FN) | Quando i falsi negativi sono costosi (ad esempio, screening del cancro) |
| **Punteggio F1** | Media armonica di precisione e richiamo | Set di dati sbilanciati, metrica a numero singolo |
| **AUC-ROC** | Area sotto la curva ROC; compromesso tra TPR e FPR | Prestazioni generali del classificatore indipendenti dalla soglia |
| **AUC-PR** | Area sotto la curva di richiamo di precisione | Set di dati altamente sbilanciati |

**Definizioni:**
- TP = vero positivo
- TN = vero negativo
- FP = falso positivo (errore di tipo I)
- FN = falso negativo (errore di tipo II)

### Metriche di regressione

| Metrico | Cosa misura | Sensibilità ai valori anomali |
|--------|---------------------------|--------------------------|
| **MSE** (errore quadratico medio) | Differenza quadrata media | Alto |
| **RMSE** (errore quadratico medio) | Radice quadrata di MSE (stesse unità dell'obiettivo) | Alto |
| **MAE** (errore medio assoluto) | Differenza media assoluta | Basso |
| **R²** (Coefficiente di determinazione) | Spiegazione della proporzione della varianza | Nessuno direttamente, ma sensibile ai valori anomali indirettamente |

### Metriche di posizionamento e recupero
- **Precision@k**: frazione di elementi rilevanti tra le raccomandazioni top-k.
- **Recall@k**: frazione di tutti gli elementi rilevanti che appaiono in top-k.
- **NDCG** (guadagno cumulativo scontato normalizzato): tiene conto della pertinenza della posizione.
- **Tasso di successo**: se un elemento rilevante appare nella top-k.

### Metriche generative/LLM
- **Perplessità**: Quanto "sorpreso" il modello da un testo trattenuto (più basso è meglio).
- **BLEU**: sovrapposizione di n-grammi con traduzioni di riferimento (focalizzata sulla precisione).
- **ROUGE**: sovrapposizione orientata al richiamo per il riepilogo.
- **BERTScore**: somiglianza semantica utilizzando incorporamenti contestuali (più robusti di BLEU).
- **METEOR**: si allinea ai sinonimi e alle radici di WordNet.

---

## Insidie della valutazione

### Perdita di dati
Si verifica quando le informazioni del set di test influenzano inavvertitamente l'addestramento.
- **Prevenzione:** non utilizzare mai i dati di test per l'ingegneria delle funzionalità, la normalizzazione o l'ottimizzazione degli iperparametri.
- **Rileva:** se il tuo modello ottiene punteggi sospettosamente alti, sospetta una perdita.

### Adattamento eccessivo
Il modello funziona bene con i dati di training ma male con la convalida/test.
- **Mitigazione:** utilizza la regolarizzazione, l'interruzione anticipata, semplifica l'architettura o raccogli più dati.

### Sottoadattamento
Il modello ha prestazioni scarse sia in termini di formazione che di convalida.
- **Mitigazione:** utilizza un modello più complesso, aggiungi funzionalità o riduci la regolarizzazione.

### dati sbilanciati
- **Mitigazione:** utilizza pesi di classe, sovracampionamento (SMOTE), sottocampionamento o utilizza metriche appropriate (F1, AUC-PR) anziché l'accuratezza.

### Deriva temporale (deriva dei concetti)
La relazione tra caratteristiche e target cambia nel tempo.
- **Mitigazione:** riqualifica periodicamente, monitora le prestazioni, utilizza algoritmi di rilevamento della deriva.

---

## Ottimizzazione degli iperparametri- **Ricerca a griglia**: prova in modo esaustivo tutte le combinazioni di un insieme predefinito di iperparametri. Semplice ma computazionalmente costoso.
- **Ricerca casuale**: esempi di combinazioni casuali da distribuzioni. Più efficiente della ricerca su griglia per spazi ad alta dimensione.
- **Ottimizzazione bayesiana**: costruisce un modello probabilistico della funzione obiettivo e seleziona gli iperparametri in modo intelligente. Librerie: Optuna, Hyperopt, scikit-optimise.
- **Ottimizzazione automatizzata**: utilizza strumenti come Optuna, Ray Tune o Weights & Biases Sweeps per l'ottimizzazione distribuita.

**Intervalli di ricerca suggeriti per gli iperparametri comuni:**

| Parametro | Intervallo suggerito (scala logaritmica) |
|-----------|-------------------------------|
| Tasso di apprendimento | 1e-5 a 1e-1 |
| Dimensione del lotto | 16, 32, 64, 128, 256|
| Numero di strati (NN) | da 2 a 6 |
| Numero di neuroni (NN) | 32-1024 |
| Regolarizzazione (L2) | 1e-6 a 1e-2 |
| Profondità dell'albero (XGBoost) | da 3 a 12 |

---

## Selezione e convalida del modello

1. **Modello di base**: iniziare con un modello euristico semplice o semplice (ad esempio, regressione logistica, predittore medio) per stabilire un limite inferiore.
2. **Modelli candidati**: addestra più famiglie di modelli (ad esempio, Random Forest, XGBoost, Neural Network).
3. **Convalida incrociata** di ciascun candidato nel set di convalida.
4. **Confronta le metriche** (con intervalli di confidenza) e seleziona il miglior candidato.
5. **Valutazione finale** sul set di test resistiti.
6. **Analisi degli errori**: guarda gli esempi in cui il modello sbaglia. Identificare modelli (ad esempio classi rare, input ambigui) e fornire informazioni sulla preparazione dei dati o sulla progettazione delle funzionalità.

---

## Distribuzione e monitoraggio

### Modelli di servizio
- **Inferenza batch**: elabora grandi volumi di dati offline (ad esempio, consigli notturni).
- **Inferenza online**: previsioni in tempo reale tramite API (ad es. credit scoring, rilevamento di frodi).
- **Inferenza di streaming**: basata sugli eventi, in tempo reale con bassa latenza (ad esempio, avvisi dei sensori IoT).

### Monitoraggio del modello
- **Monitoraggio delle prestazioni**: traccia la precisione/F1 nel tempo sui dati in tempo reale (quando è disponibile la verità sul terreno).
- **Deriva dei dati**: monitorare i cambiamenti nella distribuzione delle caratteristiche di input (ad esempio, utilizzando il PSI – indice di stabilità della popolazione).
- **Driva dei concetti**: monitorare i cambiamenti nella relazione tra input e output.
- **Driva della previsione**: monitora la distribuzione dei risultati previsti.
- **Latenza e throughput**: assicurati che gli SLA (accordi sul livello di servizio) siano rispettati.

### Registrazione e avvisi
- Registra tutte le richieste e le risposte di previsione (con anonimizzazione).
- Imposta avvisi per:
  - Calo significativo delle prestazioni.
  - Alta percentuale di input mancanti o non validi.
  - Risultati del modello al di fuori dei limiti previsti.

### Versioning e registro dei modelli
- Utilizzare un registro dei modelli (ad esempio MLflow, Weights & Biases, Sagemaker Model Registry) per archiviare e creare versioni di modelli, metadati e risultati di valutazione.
- Memorizza il codice di addestramento e la versione dei dati (tramite DVC o Git LFS) insieme al modello.

---

## Elenco di controllo pratico del flusso di lavoro

- [] Problema inquadrato e metrica di successo definita.
- [ ] Esplorazione dei dati eseguita (valori mancanti, valori anomali, distribuzione).
- [ ] Suddivisione treno/convalida/test creata (stratificata se necessario).
- [] Modello di base stabilito.
- [ ] Modelli candidati addestrati e convalidati.
- [ ] Iperparametri ottimizzati.
- [] Miglior modello selezionato tramite convalida incrociata.
- [ ] Valutazione finale sul set di prova.
- [ ] Analisi degli errori eseguita.
- [ ] Piano di implementazione pronto (al servizio dell'infrastruttura).
- [ ] Configurazione del dashboard di monitoraggio.
- [ ] Documentazione (scheda dati, scheda modello) completata.