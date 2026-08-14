---
# Metadata
title: "Feature Engineering"
description: "Transformations, encodings, feature selection, dimensionality reduction"
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
tags: [feature, engineering, data-science-and-analytics]
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
# Ingegneria delle funzionalità
L'ingegneria delle funzionalità è il processo di trasformazione dei dati grezzi in rappresentazioni che rendono i modelli di machine learning più efficaci. Viene spesso descritto come il passaggio più importante nella pipeline ML: le funzionalità fornite a un modello contano più dell'algoritmo scelto. Un modello semplice con funzionalità ben realizzate in genere avrà prestazioni migliori di un modello complesso con input grezzi e non elaborati. L’arte sta nel comprendere sia il dominio che i dati abbastanza bene da creare segnali da cui il modello può imparare.
---

## Perché l'ingegneria delle funzionalità è importante
| Fattore | Impatto |
|--------|--------|
| **Qualità del segnale** | Funzionalità migliori = modelli più chiari da apprendere per il modello |
| **Semplicità del modello** | Le buone caratteristiche consentono ai modelli più semplici di funzionare bene; meno necessità di architetture complesse |
| **Velocità di allenamento** | Funzionalità pertinenti e ben scalabili convergono più velocemente |
| **Generalizzazione** | Le funzionalità basate sul dominio aiutano i modelli a lavorare su dati invisibili |
| **Interpretabilità** | Le caratteristiche significative sono più facili da spiegare alle parti interessate |
---

## Tipi di trasformazioni di feature
### Trasformazioni numeriche
| Trasformazione | Formula / Descrizione | Quando usarlo |
|---------------|----------------------|-----|
| **Trasformazione del registro** | log(x) o log(x + 1) | Distribuzioni distorte a destra; valori monetari |
| **Radice quadrata** | sqrt(x) | Distorsione moderata; contare i dati |
| **Box-Cox** | Trasformata parametrica che trova la migliore trasformazione di potenza | Rendere i dati più normalmente distribuiti |
| **Yeo-Johnson** | Come Box-Cox ma gestisce valori negativi | Dati distorti con valori negativi |
| **Standardizzazione** | (x - media) / std | Caratteristiche con scale diverse; algoritmi che presuppongono la normalità |
| **Ridimensionamento minimo-massimo** | (x - min) / (max - min) | Caratteristiche di delimitazione a [0, 1]; valori dei pixel dell'immagine |
| **Scalatura robusta** | (x - mediana) / IQR | Dati con valori anomali |
| **Cestinamento** | Converti continuo in categorico | Relazioni non lineari; alberi decisionali |
| **Caratteristiche polinomiali** | x², x³, x₁×x₂ | Catturare relazioni non lineari nei modelli lineari |
### Codifiche categoriche
| Codifica | Descrizione | Quando usarlo |
|----------|-------------|-------------|
| **Codifica one-hot** | Crea una colonna binaria per ogni categoria | Categorie a bassa cardinalità; i modelli basati su albero gestiscono in modo nativo |
| **Codifica etichetta** | Assegnare un numero intero a ciascuna categoria | Categorie ordinali; modelli basati su alberi |
| **Codifica target** | Sostituisci la categoria con la media della variabile target | Categorie ad alta cardinalità; evitare un eccessivo adattamento con la levigatura |
| **Codifica della frequenza** | Sostituisci la categoria con il relativo conteggio o frequenza | Quando la frequenza stessa è informativa |
| **Codifica binaria** | Converti categorie con codifica intera in cifre binarie | Alta cardinalità; riduce la dimensionalità rispetto a un caldo |
| **Incorporamento** | Impara la rappresentazione vettoriale densa | Cardinalità molto elevata; PNL; sistemi di raccomandazione |
| **Codifica hash** | Categorie hash su un numero fisso di funzionalità | Cardinalità molto elevata; apprendimento online |
### Funzionalità di data e ora
| Caratteristica | Descrizione |
|---------|-----|
| **Ora del giorno** | Cattura i modelli giornalieri (ore di punta, notturne) |
| **Giorno della settimana** | Effetti nei giorni feriali e nel fine settimana |
| **Mese/trimestre** | Modelli stagionali |
| **È il fine settimana** | Bandiera binaria per il fine settimana |
| **È festivo** | Bandiera binaria per i giorni festivi |
| **Tempo trascorso dall'evento** | Giorni dall'ultimo acquisto; ore dall'ultimo accesso |
| **Codifica ciclica** | sin(2π × ora / 24), cos(2π × ora / 24) — preserva la natura circolare del tempo |
---

## Gestione dei valori mancanti
| Strategia | Descrizione | Quando usarlo |
|----------|-------------|-------------|
| **Tralascia righe** | Rimuovi le righe con valori mancanti | I dati mancanti sono una piccola frazione; MCAR (mancante del tutto a caso) |
| **Rilascia colonne** | Rimuovi elementi con troppi valori mancanti | La funzionalità è per lo più mancante; non importante |
| **Imputazione media/mediana** | Compila con la media o la mediana | della caratteristica Semplice; preserva la media ma riduce la varianza |
| **Imputazione modalità** | Compila la categoria con il valore più frequente | Caratteristiche categoriche |
| **Imputazione KNN** | Utilizzare k-vicini più vicini per stimare il valore mancante | Quando istanze simili aiutano a prevedere il valore mancante |
| **Imputazione basata su modello** | Addestrare un modello per prevedere i valori mancanti | Più accurato; computazionalmente costoso |
| **Indicatore mancante** | Aggiungi una colonna binaria che segnala la mancanza | Quando la mancanza stessa è informativa |
| **Interpolazione** | Riempi con valori interpolati (lineari, spline) | Serie temporali; dati ordinati |
---

## Selezione delle funzionalità
### Metodi di filtro
| Metodo | Descrizione |
|--------|-------------|
| **Correlazione** | Rimuovere funzionalità altamente correlate tra loro |
| **Soglia di varianza** | Rimuovere le funzionalità con varianza prossima allo zero |
| **Informazione reciproca** | Misurare le informazioni fornite da ciascuna funzione sul target |
| **Chi quadrato** | Testare l'indipendenza tra caratteristiche categoriali e target |
| **Test ANOVA F** | Verificare se i significati delle caratteristiche numeriche differiscono tra le classi target |
### Metodi wrapper
| Metodo | Descrizione |
|--------|-------------|
| **Selezione avanti** | Inizia vuoto; aggiungi la funzionalità migliore una alla volta |
| **Eliminazione all'indietro** | Inizia con tutto; rimuovere la caratteristica peggiore una alla volta |
| **Eliminazione delle funzionalità ricorsive (RFE)** | Addestrare ripetutamente il modello; rimuovere le funzionalità meno importanti |
### Metodi incorporati
| Metodo | Descrizione |
|--------|-------------|
| **Regolarizzazione L1 (Lazo)** | Riduce a zero i pesi delle caratteristiche irrilevanti |
| **Importanza basata sugli alberi** | Utilizza l'importanza delle funzionalità dai modelli ad albero |
| **Valori SHAP** | Misurare il contributo di ciascuna funzionalità alle previsioni |
---

## Ingegneria delle funzionalità specifiche del dominio
### Caratteristiche del testo
| Caratteristica | Descrizione |
|---------|-----|
| **TF-IDF** | Frequenza dei termini ponderata in base alla frequenza inversa del documento |
| **Incorporamenti di parole** | Vettori densi che catturano il significato semantico (Word2Vec, GloVe) |
| **Carattere n-grammi** | Cattura modelli di sottoparole; utile per errori di battitura e morfologia |
| **Statistiche del testo** | Lunghezza; conteggio delle parole; conteggio delle frasi; lunghezza media delle parole |
| **Punteggi di leggibilità** | Flesch-Kincaid; Indice della nebbia sparante |
### Funzionalità delle serie temporali
| Caratteristica | Descrizione |
|---------|-----|
| **Funzioni di ritardo** | Valori precedenti: y(t-1), y(t-7), y(t-30) |
| **Statistiche mobili** | Media, std, min, max su una finestra |
| **Differenza** | y(t) - y(t-1); cattura la tendenza |
| **Differenza stagionale** | y(t) - y(t-12) per dati mensili con stagionalità annuale |
| **Termini di Fourier** | Termini seno e coseno per modelli stagionali |
### Funzionalità dell'immagine (Pre-Deep Learning)
| Caratteristica | Descrizione |
|---------|-----|
| **HOG** (Istogramma dei gradienti orientati) | Distribuzione delle direzioni dei bordi |
| **LBP** (modelli binari locali) | Descrizione della struttura |
| **SIFT** (Trasformazione di caratteristiche invarianti di scala) | Descrittori dei punti chiave |
| **Istogrammi di colore** | Distribuzione dei colori nell'immagine |
---

## Migliori pratiche di ingegneria delle funzionalità
| Pratica | Descrizione |
|----------|-------------|
| **Evita la fuga di dati** | Non utilizzare mai informazioni provenienti dal futuro o dal set di test per creare funzionalità |
| **Documenta tutto** | Registrare quali trasformazioni sono state applicate e perché |
| **Versiona le tue funzionalità** | Tieni traccia delle modifiche alle funzionalità insieme alle modifiche del modello |
| **Convalidare con e senza** | Verifica se una nuova funzionalità migliora effettivamente le prestazioni del modello |
| **Mantienilo riproducibile** | Le pipeline di progettazione delle funzionalità dovrebbero essere deterministiche e ripetibili |
| **Monitora la deriva delle funzionalità** | La distribuzione delle funzionalità può cambiare nel tempo; monitorare e riqualificare |
---

## Riepilogo
L'ingegneria delle funzionalità è il luogo in cui la conoscenza del dominio incontra l'apprendimento automatico. È il processo di trasformazione dei dati grezzi – disordinati, incompleti, ad alta dimensionalità – in rappresentazioni pulite e informative da cui i modelli possono imparare. Le trasformazioni numeriche gestiscono l'inclinazione e la scala. Le codifiche categoriche convertono le etichette in numeri utilizzabili dai modelli. Le funzionalità della data catturano modelli temporali. Le strategie di valore mancante gestiscono dati incompleti. La selezione delle funzionalità rimuove rumore e ridondanza. La caratteristica migliore che gli ingegneri pensano come investigatori: chiedono quali segnali dovrebbero essere presenti nei dati, dove tali segnali potrebbero essere nascosti e come estrarli in modo onesto (senza perdita di dati), riproducibile e resistente al cambiamento nel tempo.